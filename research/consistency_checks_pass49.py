"""Read-only pass-49 artifact integrity, not additional mathematical tests."""

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent


def read_json(name):
    return json.loads((ROOT/name).read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_targets(content):
    # A Lie bracket followed by (f) inside TeX is not a Markdown link.
    prose = re.sub(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)", "", content)
    return re.findall(r"\]\(([^)\n]+)\)", prose)


def main():
    assert markdown_targets(r"\([L,h](f)\)") == []
    assert markdown_targets(r"\[[L,h](f)\] [proof](note.md)") == ["note.md"]
    claims = read_json("claims.json")
    manifest = read_json("experiment-manifest.json")
    packet = manifest["normalized_cover_and_frame_pass49"]
    verification = read_json("verification-pass-49.json")
    prior = read_json("verification-pass-48.json")
    claim_count = packet["claim_count"]
    assert len(claims["claims"]) == claim_count
    assert [v["id"] for v in claims["claims"]] == [
        f"Z{i:03d}" for i in range(1, claim_count+1)
    ]
    assert packet["claim_ids"] == [f"Z{i:03d}" for i in range(493, claim_count+1)]
    for key in (
        "general_conjecture_solved", "novelty_claimed",
        "expert_review_completed", "full_formalization_completed",
        "interpretation_confirmed_by_professor",
    ):
        assert claims[key] is False, key
    assert verification["all_passed"] is True
    total = verification["total_test_methods"]
    count = verification["total_suites"]
    assert prior["total_test_methods"] == 979
    assert prior["total_suites"] == 115
    assert total == 979+packet["new_test_methods"]
    assert count == 115+packet["new_suite_count"]
    assert manifest["validation"]["total_tests"] == total
    assert manifest["validation"]["suite_count"] == count
    assert manifest["validation"]["latest_verification_log"] == "verification-pass-49.json"
    assert {v["command"] for v in prior["suites"]}.issubset(
        {v["command"] for v in verification["suites"]}
    )
    readme = (ROOT/"README.md").read_text()
    suite_checks = []
    new_imports = {}
    for index, suite in enumerate(verification["suites"]):
        assert suite["all_passed"] and suite["exit_code"] == 0
        assert suite["command"] in readme, suite["command"]
        name = shlex.split(suite["command"])[1]
        path = ROOT/name
        tree = ast.parse(path.read_text())
        methods = sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and node.name.startswith("test_") for node in ast.walk(tree))
        assert methods == suite["test_methods"], (name, methods)
        suite_checks.append({"path": name, "test_methods": methods,
                             "sha256": digest(path)})
        if index >= 115:
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    imports.append(node.module)
            assert sorted(imports) == ["sympy", "unittest"], (name, imports)
            new_imports[name] = imports
    assert sum(item["test_methods"] for item in suite_checks) == total
    assert packet["checkers"] == verification["suites"][115:]
    assert verification["new_suite_test_methods"] == packet["new_test_methods"]
    assert verification["new_suite_count"] == packet["new_suite_count"]
    for key in ("general_cancellation_verified", "human_expert_review",
                "proof_assistant_verified", "novelty_established"):
        assert verification[key] is False, key
    for key in ("general_cancellation_solved", "human_expert_review",
                "proof_assistant_verified", "novelty_established"):
        assert packet[key] is False, key
    artifact_checks, links = [], set()
    names = packet["artifacts"]
    assert len(names) == len(set(names))
    required = set(["README.md","research-ledger.md","claims.json","experiment-manifest.json","verification-pass-49.json","deep-pass-49.md","research/normalized-cover-surjectivity-pass49.md","research/nodal-plinth-obstruction-pass49.md","research/frame-filtration-generation-pass49.md","research/proof-audits-pass49.md","research/synthesis-audit-pass49.md","research/frame_filtration_generation_checks_pass49.py","research/run_regression_pass49.py","research/consistency_checks_pass49.py","research/checkpoint-pass49-working.json","deep-pass-48.md","verification-pass-48.json","consistency-pass-48.json","research/consistency_checks_pass48.py","research/second-image-vector-bundle-pass47.md","research/flat-conic-topology-gate-pass47.md","research/intrinsic-pointwise-plinth-pass47.md","research/minimal-quadratic-slice-pass46.md","research/quadratic-monodromy-pass46.md","research/generic-bad-pair-pass44.md","research/pointwise-plinth-pass17.md","research/third-image-cubic-gate-pass48.md","research/initial-conic-fiber-pass48.md","research/repeated-smooth-support-pass48.md"])
    assert required.issubset(names)
    for name in names:
        path = ROOT/name
        content = path.read_text()
        assert content.endswith("\n"), name
        assert all(ord(character) >= 32 or character in "\n\t"
                   for character in content), ("unexpected control character", name)
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
                target = unquote(target.split("#", 1)[0])
                target = re.sub(r":\d+$", "", target)
                assert (path.parent/target).resolve().exists(), (name, target)
                links.add((name, target))
        artifact_checks.append({"path": name, "sha256": digest(path)})
    source_checks = []
    for item in packet["source_inputs"]:
        path = ROOT/item["path"]
        assert path.is_file() and path.stat().st_size > 0
        source_checks.append({**item, "bytes": path.stat().st_size,
                              "sha256": digest(path)})
    # Historical proof/checker/source hashes are frozen, shared metadata is not.
    old_integrity = read_json("consistency-pass-48.json")
    mutable = {"README.md", "research-ledger.md", "claims.json", "experiment-manifest.json"}
    frozen_checks = []
    for group in ("artifacts", "suite_sources", "source_inputs"):
        for item in old_integrity[group]:
            name = item["path"]
            if name in mutable:
                continue
            assert digest(ROOT/name) == item["sha256"], ("changed frozen input", name)
            frozen_checks.append({"group": group, "path": name})
    assert len(frozen_checks) == 155
    working_checkpoint = read_json("research/checkpoint-pass49-working.json")
    working_checks = []
    for item in working_checkpoint["artifact_integrity"]["artifacts"]:
        assert digest(ROOT/item["path"]) == item["sha256"], ("changed audited working input", item["path"])
        working_checks.append(item["path"])
    assert len(working_checks) == 5
    report = (ROOT/"deep-pass-49.md").read_text()
    tags = [int(value) for value in re.findall(r"\\tag\{(\d+)\}", report)]
    assert tags == list(range(1, len(tags)+1))
    definitions = re.findall(r"(?m)^\[\^(\d+)\]:", report)
    references = set(re.findall(r"\[\^(\d+)\]", report))
    assert len(definitions) == len(set(definitions))
    assert set(definitions) == references
    result = {
        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "all_passed": True, "claim_count": claim_count, "last_claim": f"Z{claim_count:03d}",
        "test_method_count": total, "suite_count": count,
        "new_checker_imports": new_imports, "current_local_links_checked": len(links),
        "report_line_count": len(report.splitlines()),
        "report_numbered_equations": len(tags), "report_footnotes": len(definitions),
        "previous_frozen_records_checked": len(frozen_checks),
        "audited_working_records_checked": len(working_checks),
        "artifact_count": len(artifact_checks), "artifacts": artifact_checks,
        "suite_sources": suite_checks, "source_inputs": source_checks,
        "link_parser_controls": 2,
        "link_parser_controls_counted_as_mathematical_tests": False,
        "scope": "JSON, AST counts, flags, whitespace, links, numbering and SHA256 integrity. Not mathematical proof verification.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
