"""Read-only full60 artifact consistency, not mathematical proof verification."""

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
MUTABLE = {"README.md", "research-ledger.md", "claims.json", "experiment-manifest.json"}


def read_json(name):
    return json.loads((ROOT / name).read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_targets(content):
    prose = re.sub(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)", "", content)
    return re.findall(r"\]\(([^)\n]+)\)", prose)


def main():
    assert markdown_targets(r"\([L,h](f)\)") == []
    assert markdown_targets(r"\[[L,h](f)\] [proof](note.md)") == ["note.md"]
    claims = read_json("claims.json")
    manifest = read_json("experiment-manifest.json")
    packet = manifest["coordinate_compatibility_and_speed_exclusion_pass60"]
    verification = read_json("verification-pass-60.json")
    previous = read_json("verification-pass-57.json")
    assert packet["claim_count"] == 544
    assert len(claims["claims"]) == packet["claim_count"]
    assert [c["id"] for c in claims["claims"]] == [f"Z{i:03d}" for i in range(1, 545)]
    assert packet["claim_ids"] == [f"Z{i:03d}" for i in range(540, 545)]
    for key in ("general_conjecture_solved", "novelty_claimed",
                "expert_review_completed", "full_formalization_completed",
                "interpretation_confirmed_by_professor"):
        assert claims[key] is False, key
    for key in ("general_cancellation_solved", "human_expert_review",
                "proof_assistant_verified", "novelty_established"):
        assert packet[key] is False, key
    for key in ("general_cancellation_verified", "human_expert_review",
                "proof_assistant_verified", "novelty_established"):
        assert verification[key] is False, key
    assert previous["all_passed"] and verification["all_passed"]
    assert verification["total_test_methods"] == previous["total_test_methods"] + 5 == 1000
    assert verification["total_suites"] == previous["total_suites"] + 3 == 126
    assert verification["new_suite_test_methods"] == packet["new_test_methods"] == 5
    assert verification["new_suite_count"] == packet["new_suite_count"] == 3
    assert packet["checkers"] == verification["suites"][123:]
    assert verification["new_written_passes"] == [58, 59, 60]
    assert manifest["validation"]["latest_verification_log"] == "verification-pass-60.json"
    assert manifest["validation"]["total_tests"] == 1000
    assert manifest["validation"]["suite_count"] == 126
    assert [s["command"] for s in verification["suites"][:123]] == [
        s["command"] for s in previous["suites"]
    ]
    readme = (ROOT / "README.md").read_text()
    suites = []
    for suite in verification["suites"]:
        assert suite["all_passed"] and suite["exit_code"] == 0
        assert suite["command"] in readme, suite["command"]
        name = shlex.split(suite["command"])[1]
        path = ROOT / name
        tree = ast.parse(path.read_text())
        methods = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and n.name.startswith("test_") for n in ast.walk(tree))
        assert methods == suite["test_methods"], (name, methods)
        suites.append({"path": name, "test_methods": methods, "sha256": digest(path)})
    assert len(suites) == 126 and sum(s["test_methods"] for s in suites) == 1000
    for suite in verification["suites"][123:]:
        tree = ast.parse((ROOT / shlex.split(suite["command"])[1]).read_text())
        assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))
        imports = {alias.name for n in ast.walk(tree) if isinstance(n, ast.Import)
                   for alias in n.names}
        assert imports == {"sympy", "unittest"}, (suite["name"], imports)
    qualification = claims["claims"][531]["qualification_from_pass60"]
    assert qualification and claims["claims"][531]["id"] == "Z532"

    artifacts, links = [], set()
    names = packet["artifacts"]
    assert len(names) == len(set(names)) == 32
    required = MUTABLE | {
        "verification-pass-60.json", "deep-pass-60.md",
        "research/run_regression_pass60.py", "research/consistency_checks_pass60.py",
        "research/synthesis-audit-pass60.md", "consistency-pass-57.json",
        "research/checkpoint-pass60-working.json",
    }
    assert required.issubset(names)
    for name in names:
        path = ROOT / name
        content = path.read_text()
        assert content.endswith("\n"), name
        assert all(ord(c) >= 32 or c in "\n\t" for c in content), name
        assert all(line.rstrip() == line for line in content.splitlines()), name
        if path.suffix == ".json":
            json.loads(content)
        elif path.suffix == ".py":
            ast.parse(content)
        elif path.suffix == ".md":
            assert "\u2014" not in content, name
            for target in markdown_targets(content):
                target = target.strip().strip("<>")
                if target.startswith(("https:", "http:", "mailto:", "#", "codex:")):
                    continue
                target = re.sub(r":\d+$", "", unquote(target.split("#", 1)[0]))
                assert (path.parent / target).resolve().exists(), (name, target)
                links.add((name, target))
        artifacts.append({"path": name, "sha256": digest(path)})
    source_checks = []
    for item in packet["source_inputs"]:
        path = ROOT / item["path"]
        assert path.is_file() and path.stat().st_size > 0
        source_checks.append({**item, "bytes": path.stat().st_size, "sha256": digest(path)})
    assert len(source_checks) == 14
    old_integrity = read_json("consistency-pass-57.json")
    frozen = []
    for group in ("artifacts", "suite_sources", "source_inputs"):
        for item in old_integrity[group]:
            if item["path"] in MUTABLE:
                continue
            assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
            frozen.append({"group": group, "path": item["path"]})
    assert len(frozen) == 166
    working = []
    old = read_json("research/checkpoint-pass60-working.json")
    items = old["artifact_integrity"]["artifacts"]
    assert len(items) == 13
    for item in items:
        assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
        assert item["path"] in names
        working.append(item["path"])
    assert len(working) == 13
    report = (ROOT / "deep-pass-60.md").read_text()
    tags = [int(v) for v in re.findall(r"\\tag\{(\d+)\}", report)]
    assert tags == list(range(1, 30))
    definitions = re.findall(r"(?m)^\[\^(\d+)\]:", report)
    references = set(re.findall(r"\[\^(\d+)\]", report))
    assert len(definitions) == len(set(definitions)) == 4
    assert set(definitions) == references
    result = {
        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "all_passed": True, "claim_count": 544, "last_claim": "Z544",
        "test_method_count": 1000, "suite_count": 126,
        "new_test_methods": 5, "new_suite_count": 3,
        "current_local_links_checked": len(links),
        "report_line_count": len(report.splitlines()),
        "report_numbered_equations": len(tags), "report_footnotes": len(definitions),
        "previous_frozen_records_checked": len(frozen),
        "audited_working_records_checked": len(working),
        "artifact_count": len(artifacts), "artifacts": artifacts,
        "suite_sources": suites, "source_inputs": source_checks,
        "hash_record_count": len(artifacts) + len(suites) + len(source_checks),
        "link_parser_controls": 2,
        "link_parser_controls_counted_as_mathematical_tests": False,
        "scope": "JSON, AST counts, flags, whitespace, links, numbering and SHA256 integrity. Not mathematical proof verification.",
    }
    assert result["hash_record_count"] == 172
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
