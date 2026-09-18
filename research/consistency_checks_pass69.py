"""Read-only integrity audit of the combined working69 proof packet.

The pinned frozen68 integrity program is reused after its own file and
packet hashes are validated. No mathematical suite or regression runner
is executed. This program only reads files and prints JSON evidence.
"""

import ast
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shlex


ROOT = Path(__file__).resolve().parent.parent
FROZEN68 = "research/checkpoint-pass68-working.json"
FROZEN68_SHA256 = "435d09c341a80c1b3f6ae7ba46316b89e64d9f6f5291cce0fa6f1bb3413a0b50"
VERIFICATION = "research/verification-pass69-working.json"
VERIFICATION_SHA256 = "0e058799b5d1af27c628d690dc11999613f5ac047b4ccaa3b25ff457c1a6c51b"
CHECKPOINT = "research/checkpoint-pass69-working.json"
ARTIFACTS = [
    "research/projected-cubic-defects-pass69.md",
    "research/rational-two-direction-recognition-pass69.md",
    "research/cubic-rank-drop-nonconstant-speed-pass69.md",
    "research/vertical-top-exclusion-pass69.md",
    "research/cubic-rank-drop-constant-speed-closure-pass69.md",
    "research/normalized-defect-projection-controls-pass69.md",
    "research/normalized_defect_projection_checks_pass69.py",
    "research/rational_two_direction_checks_pass69.py",
    "research/cubic_shear_vertical_checks_pass69.py",
    "research/proof-audits-pass69-working.md",
    "research/independent-cubic-closure-pass69.md",
    "research/run_regression_pass69.py",
    VERIFICATION,
    "research/consistency_checks_pass69.py",
]
EXPECTED_EQUATIONS = {
    ARTIFACTS[0]: 9, ARTIFACTS[1]: 14, ARTIFACTS[2]: 16,
    ARTIFACTS[3]: 8, ARTIFACTS[4]: 13, ARTIFACTS[5]: 12,
    ARTIFACTS[10]: 5,
}
CHECKERS = {
    ARTIFACTS[6]: 3,
    ARTIFACTS[7]: 3,
    ARTIFACTS[8]: 2,
}
ADDITIONS = [
    ("research/independent_higher_constant_checks_pass68.py", 2, False),
    *[(path, count, True) for path, count in CHECKERS.items()],
]


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def frozen_integrity():
    # Pin the already reported packet independently of its internal records.
    assert digest(FROZEN68) == FROZEN68_SHA256
    packet = read_json(FROZEN68)
    records = packet["artifact_integrity"]["artifacts"]
    assert len(records) == len({r["path"] for r in records}) == 11
    for record in records:
        assert digest(record["path"]) == record["sha256"], record["path"]
    integrity_path = "research/consistency_checks_pass68.py"
    assert integrity_path in {r["path"] for r in records}
    spec = importlib.util.spec_from_file_location("frozen_integrity68", ROOT / integrity_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = io.StringIO()
    with redirect_stdout(output):
        result = module.main()
    assert result == 0
    evidence = json.loads(output.getvalue())
    assert evidence["all_passed"] is True
    assert evidence["artifacts"] == records
    assert evidence["prior_packets"] == packet["artifact_integrity"]["prior_packets"]
    assert evidence["old_full60_nonmutable_records"] == 168
    assert evidence["historical_registry_and_manifest_records"] == 2
    assert evidence["central_claim_count"] == 544
    for number, count in ((64, 13), (65, 11), (66, 9), (67, 10)):
        assert evidence[f"prior_working{number}_artifacts"] == count
    assert evidence["frozen67_checkpoint_sha256"] == (
        "e6aef37fc9a9c860febf533cf06298b6a48cfcb56a53be1bf73e2b325b126d47"
    )
    assert evidence["last_full_regression"] == {
        "suites": 132, "methods": 1011, "all_passed": True,
    }
    assert evidence["fresh_full68_regression_performed"] is False
    assert evidence["central_claim_registry_integrated"] is False
    assert evidence["general_cancellation_verified"] is False
    assert packet["all_profile_height_threshold"] == 9
    for key in (
        "central_registry_integrated", "general_conjecture_solved",
        "universal_frame_existence_proved", "novelty_claimed",
        "human_expert_review", "proof_assistant_verified",
        "interpretation_confirmed_by_professor", "external_contact_or_submission",
        "entire_two_quadratic_profile_recognized",
    ):
        assert packet[key] is False, key
    return module, evidence


def capture_integrity():
    assert digest(VERIFICATION) == VERIFICATION_SHA256
    capture = read_json(VERIFICATION)
    previous = read_json("research/verification-pass67-working.json")
    assert previous["all_passed"] is True
    assert previous["total_suites"] == len(previous["suites"]) == 132
    assert previous["total_test_methods"] == sum(
        s["test_methods"] for s in previous["suites"]
    ) == 1011
    expected = [{
        "name": s["name"], "command": s["command"],
        "expected_test_methods": s["test_methods"],
        "working_addition": s.get("working_addition", False),
        "current_pass_addition": False,
    } for s in previous["suites"]]
    expected.extend({
        "name": Path(path).stem,
        "command": shlex.join(["/opt/anaconda3/bin/python", path]),
        "expected_test_methods": count, "working_addition": True,
        "current_pass_addition": current,
    } for path, count, current in ADDITIONS)
    assert len(expected) == len({tuple(shlex.split(s["command"])) for s in expected}) == 136
    suites = capture["suites"]
    assert len(suites) == capture["total_suites"] == capture["expected_total_suites"] == 136
    assert capture["all_passed"] is True
    assert capture["central_registry_integrated"] is False
    assert capture["general_cancellation_verified"] is False
    for key, value in {
        "runner": "research/run_regression_pass69.py",
        "subprocess_helper": "research/run_regression_pass67.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "inherited_record": "research/verification-pass67-working.json",
        "inherited_suites": 132, "inherited_methods": 1011,
        "expected_total_test_methods": 1021, "total_test_methods": 1021,
    }.items():
        assert capture[key] == value, key
    start = datetime.fromisoformat(capture["started_at_utc"])
    finish = datetime.fromisoformat(capture["finished_at_utc"])
    assert start == datetime.fromisoformat("2026-09-14T02:03:29.218741+00:00")
    assert finish == datetime.fromisoformat("2026-09-14T02:05:03.238131+00:00")
    retained = []
    for actual, planned in zip(suites, expected):
        for key, value in planned.items():
            assert actual[key] == value, (actual["name"], key)
        assert actual["all_passed"] is True and actual["exit_code"] == 0
        assert actual["launch_error"] is None and actual["method_count_matches"] is True
        assert actual["test_methods"] == actual["expected_test_methods"] > 0
        began = datetime.fromisoformat(actual["started_at_utc"])
        ended = datetime.fromisoformat(actual["finished_at_utc"])
        assert start <= began <= ended <= finish
        assert began.utcoffset() == ended.utcoffset() == start.utcoffset()
        assert abs(actual["elapsed_seconds"] - (ended - began).total_seconds()) < 0.004
        assert 0 <= actual["unittest_seconds"] <= actual["elapsed_seconds"] + 0.002
        summary = re.fullmatch(r"Ran (\d+) tests? in ([\d.]+)s", actual["unittest_summary"])
        assert summary and int(summary[1]) == actual["test_methods"]
        assert float(summary[2]) == actual["unittest_seconds"]
        assert re.fullmatch(r"[0-9a-f]{64}", actual["stdout_sha256"])
        assert actual["stdout_sha256"] != hashlib.sha256(b"").hexdigest()
        if actual["current_pass_addition"]:
            output = actual["output"]
            assert hashlib.sha256(output.encode()).hexdigest() == actual["stdout_sha256"]
            summaries = re.findall(r"(?m)^Ran (\d+) tests? in ([\d.]+)s$", output)
            assert len(summaries) == 1
            assert int(summaries[0][0]) == actual["test_methods"]
            assert float(summaries[0][1]) == actual["unittest_seconds"]
            assert re.search(r"(?m)^OK\s*$", output)
            assert not re.search(r"(?m)^FAILED\b", output)
            retained.append({
                "path": shlex.split(actual["command"])[1],
                "methods": actual["test_methods"],
                "unittest_seconds": actual["unittest_seconds"],
                "stdout_sha256": actual["stdout_sha256"],
            })
        else:
            assert actual["output"] == ""
    assert sum(s["test_methods"] for s in suites) == 1021
    working = [s for s in suites if s["working_addition"]]
    assert len(working) == capture["working_addition_suites"] == 10
    assert sum(s["test_methods"] for s in working) == capture["working_addition_methods"] == 21
    assert len(retained) == capture["current_pass_addition_suites"] == 3
    assert sum(s["methods"] for s in retained) == capture["current_pass_addition_methods"] == 8
    assert [s["unittest_seconds"] for s in retained] == [0.157, 0.189, 0.091]
    return {
        "path": VERIFICATION, "sha256": VERIFICATION_SHA256,
        "suites": 136, "methods": 1021, "all_passed": True,
        "started_at_utc": capture["started_at_utc"],
        "finished_at_utc": capture["finished_at_utc"],
        "elapsed_seconds": (finish - start).total_seconds(),
        "exact_inherited67_commands": 132, "rerun68_methods": 2,
        "new69_suites": 3, "new69_methods": 8,
        "retained_outputs_rehashed": retained,
        "omitted_successful_outputs": 133,
        "omitted_stdout_hashes_recomputed": False,
    }


def checker_integrity():
    records = []
    for path, count in CHECKERS.items():
        tree = ast.parse((ROOT / path).read_text())
        methods = [n.name for n in ast.walk(tree)
                   if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
        imports = [alias.name for n in ast.walk(tree) if isinstance(n, ast.Import)
                   for alias in n.names]
        assert len(methods) == len(set(methods)) == count
        assert imports == ["unittest", "sympy"]
        assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))
        records.append({"path": path, "methods": methods, "imports": imports})
    assert len(records) == 3 and sum(len(r["methods"]) for r in records) == 8
    return records


def artifact_integrity(mask):
    records, deferred = [], []
    links = 0
    assert len(ARTIFACTS) == len(set(ARTIFACTS)) == 14
    assert all("pass70" not in path for path in ARTIFACTS)
    for name in ARTIFACTS:
        path = ROOT / name
        raw = path.read_bytes()
        text = raw.decode()
        assert raw.endswith(b"\n"), name
        assert "\r" not in text and "\u2014" not in text, name
        assert all(line == line.rstrip() for line in text.splitlines()), name
        equations = [int(n) for n in re.findall(r"\\tag\{(\d+)\}", text)]
        assert equations == list(range(1, len(equations) + 1)), name
        assert len(equations) == EXPECTED_EQUATIONS.get(name, 0), name
        if path.suffix == ".py":
            ast.parse(text)
        elif path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", mask(text)):
                target = target.strip("<>")
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                local = target.split("#", 1)[0]
                if not local:
                    continue
                resolved = (path.parent / local).resolve()
                if resolved == (ROOT / CHECKPOINT).resolve() and not resolved.exists():
                    deferred.append({"source": name, "target": CHECKPOINT})
                    continue
                assert resolved.exists(), (name, target)
                links += 1
        records.append({
            "path": name, "bytes": len(raw), "sha256": digest(name),
            "lines": len(text.splitlines()), "numbered_equations": len(equations),
            "source_footnotes": len(re.findall(r"(?m)^\[\^[^\]]+\]:", text)),
        })
    assert len(deferred) <= 1
    return records, links, deferred


def main():
    previous_module, previous = frozen_integrity()
    capture = capture_integrity()
    checkers = checker_integrity()
    records, links, deferred = artifact_integrity(previous_module.link_prose)
    print(json.dumps({
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "all_passed": True,
        "frozen68_checkpoint": {"path": FROZEN68, "sha256": FROZEN68_SHA256},
        "old_full60_nonmutable_records": previous["old_full60_nonmutable_records"],
        "historical_registry_and_manifest_records": previous["historical_registry_and_manifest_records"],
        "central_claim_count": previous["central_claim_count"],
        "prior_working64_artifacts": 13, "prior_working65_artifacts": 11,
        "prior_working66_artifacts": 9, "prior_working67_artifacts": 10,
        "prior_working68_artifacts": 11,
        "prior_packets": previous["prior_packets"] + [
            {"path": FROZEN68, "sha256": FROZEN68_SHA256}
        ],
        "frozen68_integrity_reexecuted": True,
        "mathematical_suites_executed": 0,
        "regression_runners_executed": 0,
        "current_new_checkers": checkers,
        "combined_verification": capture,
        "local_link_paths_checked": links,
        "deferred_future_checkpoint_links": deferred,
        "link_anchors_checked": False,
        "central_claim_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Read-only artifact integrity and actual captured finite-test accounting. No mathematical proof, source theorem, human review, formal verification, novelty, universal frame or general cancellation is verified. The only potentially deferred local path is this pass's future checkpoint; pass70 drafts are excluded.",
        "artifacts": records,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
