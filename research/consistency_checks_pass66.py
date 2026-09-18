"""Read-only integrity audit for the working66 proof packet.

This checks files, captured evidence and scope flags, not theorem truth.
It never writes or updates historical artifacts.
"""

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = [
    "research/rank-three-speed-curve-pass66.md",
    "research/dependent-constant-cubic-pass66.md",
    "research/constant-top-cubic-good-fields-pass66.md",
    "research/dependent_low_flow_rank_checks_pass66.py",
    "research/run_regression_pass66.py",
    "research/verification-pass66-working.json",
    "research/low-flow-closure-pass66.md",
    "research/proof-audits-pass66-working.md",
    "research/consistency_checks_pass66.py",
]
MUTABLE = {"README.md", "research-ledger.md", "claims.json", "experiment-manifest.json"}


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def verify_records(records):
    for record in records:
        assert digest(record["path"]) == record["sha256"], record["path"]
    return len(records)


def main():
    full = json.loads((ROOT / "consistency-pass-60.json").read_text())
    old_records = [
        record
        for group in ("artifacts", "suite_sources", "source_inputs")
        for record in full[group]
        if record["path"] not in MUTABLE
    ]
    assert len(old_records) == 168
    old_count = verify_records(old_records)
    p64 = json.loads((ROOT / "research/checkpoint-pass64-working.json").read_text())
    p65 = json.loads((ROOT / "research/checkpoint-pass65-working.json").read_text())
    # The prior packet schemas deliberately remain historical.
    a64 = p64["artifact_integrity"]["artifacts"]
    a65 = p65["artifact_integrity"]["artifacts"]
    prior64 = verify_records(a64)
    prior65 = verify_records(a65)
    assert (prior64, prior65) == (13, 11)
    prior_packets = [
        {
            "path": "research/checkpoint-pass64-working.json",
            "sha256": digest("research/checkpoint-pass64-working.json"),
        },
        {
            "path": "research/checkpoint-pass65-working.json",
            "sha256": digest("research/checkpoint-pass65-working.json"),
        },
    ]
    assert prior_packets[0]["sha256"] == p65["artifact_integrity"]["prior_packet"]["sha256"]

    run = json.loads((ROOT / "research/verification-pass66-working.json").read_text())
    suites = run["suites"]
    assert len(suites) == run["total_suites"] == 130
    assert sum(s["test_methods"] for s in suites) == run["total_test_methods"] == 1008
    assert all(s["all_passed"] and s["exit_code"] == 0 for s in suites)
    assert run["all_passed"] is True
    assert run["general_cancellation_verified"] is False
    assert run["central_registry_integrated"] is False
    additions = [s for s in suites if s["working_addition"]]
    assert len(additions) == 4
    assert sum(s["test_methods"] for s in additions) == 8
    assert len({s["command"] for s in suites}) == 130
    for suite in suites:
        assert re.fullmatch(r"[0-9a-f]{64}", suite["stdout_sha256"])
        match = re.fullmatch(r"Ran (\d+) tests? in ([\d.]+)s", suite["unittest_summary"])
        assert match and int(match[1]) == suite["test_methods"]
        if suite["output"]:
            assert hashlib.sha256(suite["output"].encode()).hexdigest() == suite["stdout_sha256"]

    checker = "research/dependent_low_flow_rank_checks_pass66.py"
    tree = ast.parse((ROOT / checker).read_text())
    methods = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]
    imports = [
        alias.name for node in ast.walk(tree)
        if isinstance(node, ast.Import) for alias in node.names
    ]
    assert len(methods) == 3
    assert imports == ["unittest", "sympy"]
    assert not any(isinstance(node, ast.ImportFrom) for node in ast.walk(tree))
    new_suite = [s for s in additions if s["name"] == "dependent_low_flow_rank_checks_pass66"]
    assert len(new_suite) == 1 and new_suite[0]["test_methods"] == len(methods)

    records = []
    links = 0
    for name in ARTIFACTS:
        path = ROOT / name
        raw = path.read_bytes()
        text = raw.decode()
        assert raw.endswith(b"\n"), name
        assert "\r" not in text and "\u2014" not in text, name
        assert all(line == line.rstrip() for line in text.splitlines()), name
        equations = [int(number) for number in re.findall(r"\\tag\{(\d+)\}", text)]
        assert equations == list(range(1, len(equations) + 1)), name
        if path.suffix == ".py":
            ast.parse(text)
        elif path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
                target = target.strip("<>")
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                local = target.split("#", 1)[0]
                if local:
                    assert (path.parent / local).resolve().exists(), (name, target)
                    links += 1
        records.append({
            "path": name, "bytes": len(raw), "sha256": digest(name),
            "lines": len(text.splitlines()), "numbered_equations": len(equations),
            "source_footnotes": len(re.findall(r"(?m)^\[\^[^\]]+\]:", text)),
        })
    print(json.dumps({
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "all_passed": True,
        "old_full60_nonmutable_records": old_count,
        "prior_working64_artifacts": prior64,
        "prior_working65_artifacts": prior65,
        "prior_packets": prior_packets,
        "local_link_paths_checked": links,
        "link_anchors_checked": False,
        "current_new_checker": {"path": checker, "methods": methods, "imports": imports},
        "regression": {"suites": 130, "methods": 1008, "all_passed": True},
        "central_claim_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Artifact integrity and captured finite-test accounting, not mathematical proof verification.",
        "artifacts": records,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

