"""Read-only integrity checks for the completed pass-21 research packet.

These are artifact-consistency checks, not additional mathematical tests.
The command prints JSON and does not write any file.
"""

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = [
    "README.md", "research-ledger.md", "claims.json",
    "experiment-manifest.json", "verification-pass-21.json",
    "deep-pass-21.md",
    "research/primitive-noninvariant-bridge-pass21.md",
    "research/arbitrary-slice-frame-pass21.md",
    "research/universal-bridge-pass21.md",
    "research/nodal-embedding-pass21.md",
    "research/primitive-bridge-audit-pass21.md",
    "research/universal-bridge-audit-pass21.md",
    "research/nodal-audit-pass21.md",
    "research/proof-audits-pass21.md",
    "research/priority-comparison-pass21.md",
    "research/primitive_bridge_checks_pass21.py",
    "research/run_regression_pass21.py",
    "research/consistency_checks_pass21.py",
]


def read_json(name):
    return json.loads((ROOT/name).read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    claims = read_json("claims.json")
    manifest = read_json("experiment-manifest.json")
    verification = read_json("verification-pass-21.json")
    prior = read_json("verification-pass-20.json")
    assert len(claims["claims"]) == 194
    assert [v["id"] for v in claims["claims"]] == [
        f"Z{i:03d}" for i in range(1, 195)
    ]
    for key in (
        "general_conjecture_solved", "novelty_claimed",
        "expert_review_completed", "full_formalization_completed",
        "interpretation_confirmed_by_professor",
    ):
        assert claims[key] is False, key
    assert verification["all_passed"] is True
    assert verification["total_suites"] == 34
    assert verification["total_test_methods"] == 451
    assert manifest["validation"]["total_tests"] == 451
    assert manifest["validation"]["suite_count"] == 34
    assert manifest["validation"]["latest_verification_log"] == "verification-pass-21.json"
    assert {v["command"] for v in prior["suites"]}.issubset(
        {v["command"] for v in verification["suites"]}
    )
    readme = (ROOT/"README.md").read_text()
    suite_checks = []
    for suite in verification["suites"]:
        assert suite["all_passed"] and suite["exit_code"] == 0
        assert suite["command"] in readme, suite["command"]
        source_name = shlex.split(suite["command"])[1]
        source = ROOT/source_name
        tree = ast.parse(source.read_text())
        count = sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name.startswith("test_") for node in ast.walk(tree)
        )
        assert count == suite["test_methods"], (source_name, count)
        suite_checks.append({
            "path": source_name, "test_methods": count,
            "sha256": digest(source),
        })
    assert sum(item["test_methods"] for item in suite_checks) == 451
    tree = ast.parse((ROOT/"research/primitive_bridge_checks_pass21.py").read_text())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    assert sorted(imports) == ["sympy", "unittest"]
    assert manifest["noninvariant_and_universal_bridge_pass21"]["checkers"] == [verification["suites"][-1]]
    artifact_checks, links = [], set()
    for name in ARTIFACTS:
        path = ROOT/name
        content = path.read_text()
        assert content.endswith("\n"), name
        assert all(line.rstrip() == line for line in content.splitlines()), name
        if path.suffix == ".json":
            json.loads(content)
        elif path.suffix == ".py":
            ast.parse(content)
        elif path.suffix == ".md":
            for target in re.findall(r"\]\(([^)\n]+)\)", content):
                target = target.strip().strip("<>")
                if target.startswith(("https:", "http:", "mailto:", "#", "codex:")):
                    continue
                target = unquote(target.split("#", 1)[0])
                target = re.sub(r":\d+$", "", target)
                destination = (path.parent/target).resolve()
                assert destination.exists(), (name, target)
                links.add((name, target))
        artifact_checks.append({"path": name, "sha256": digest(path)})
    report = (ROOT/"deep-pass-21.md").read_text()
    tags = [int(value) for value in re.findall(r"\\tag\{(\d+)\}", report)]
    assert tags == list(range(1, 27))
    definitions = re.findall(r"(?m)^\[\^(\d+)\]:", report)
    references = set(re.findall(r"\[\^(\d+)\]", report))
    assert len(definitions) == len(set(definitions))
    assert set(definitions) == references
    assert all(value is False for value in (
        verification["general_cancellation_verified"],
        verification["human_expert_review"],
        verification["proof_assistant_verified"],
        verification["novelty_established"],
    ))
    result = {
        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "all_passed": True, "claim_count": 194, "last_claim": "Z194",
        "test_method_count": 451, "suite_count": 34,
        "new_checker_imports": imports, "current_local_links_checked": len(links),
        "report_line_count": len(report.splitlines()),
        "report_numbered_equations": len(tags), "report_footnotes": len(definitions),
        "artifact_count": len(artifact_checks), "artifacts": artifact_checks,
        "suite_sources": suite_checks,
        "scope": "JSON, AST counts, flags, whitespace, local links, equation/footnote numbering and SHA256 integrity. Not mathematical proof verification.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
