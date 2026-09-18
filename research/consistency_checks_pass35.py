"""Read-only pass-35 artifact integrity, not additional mathematical tests."""

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
    packet = manifest["cylinder_pencil_and_nodal_exhaustion_pass35"]
    verification = read_json("verification-pass-35.json")
    prior = read_json("verification-pass-34.json")
    claim_count = packet["claim_count"]
    assert len(claims["claims"]) == claim_count
    assert [v["id"] for v in claims["claims"]] == [
        f"Z{i:03d}" for i in range(1, claim_count+1)
    ]
    assert packet["claim_ids"] == [f"Z{i:03d}" for i in range(335, claim_count+1)]
    for key in (
        "general_conjecture_solved", "novelty_claimed",
        "expert_review_completed", "full_formalization_completed",
        "interpretation_confirmed_by_professor",
    ):
        assert claims[key] is False, key
    assert verification["all_passed"] is True
    total = verification["total_test_methods"]
    count = verification["total_suites"]
    assert prior["total_test_methods"] == 777
    assert prior["total_suites"] == 73
    assert total == 777+packet["new_test_methods"]
    assert count == 73+packet["new_suite_count"]
    assert manifest["validation"]["total_tests"] == total
    assert manifest["validation"]["suite_count"] == count
    assert manifest["validation"]["latest_verification_log"] == "verification-pass-35.json"
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
        if index >= 73:
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    imports.append(node.module)
            assert sorted(imports) == ["sympy", "unittest"], (name, imports)
            new_imports[name] = imports
    assert sum(item["test_methods"] for item in suite_checks) == total
    assert packet["checkers"] == verification["suites"][73:]
    assert verification["new_suite_test_methods"] == packet["new_test_methods"]
    assert verification["new_suite_count"] == packet["new_suite_count"]
    for key in ("general_cancellation_verified", "human_expert_review",
                "proof_assistant_verified", "novelty_established"):
        assert verification[key] is False, key
    artifact_checks, links = [], set()
    names = packet["artifacts"]
    assert len(names) == len(set(names))
    required = {"README.md", "claims.json", "experiment-manifest.json",
                "research-ledger.md", "verification-pass-35.json", "deep-pass-35.md",
                "research/isolated-node-realization-pass35.md",
                "research/run_regression_pass35.py", "research/consistency_checks_pass35.py"}
    assert required.issubset(names)
    for name in names:
        path = ROOT/name
        content = path.read_text()
        assert content.endswith("\n"), name
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
    report = (ROOT/"deep-pass-35.md").read_text()
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
        "artifact_count": len(artifact_checks), "artifacts": artifact_checks,
        "suite_sources": suite_checks,
        "link_parser_controls": 2,
        "link_parser_controls_counted_as_mathematical_tests": False,
        "scope": "JSON, AST counts, flags, whitespace, links, numbering and SHA256 integrity. Not mathematical proof verification.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
