"""Read-only full regression of the captured73 suites plus additions74--75.

Print actual subprocess evidence without changing any saved verification
record, checkpoint, or registry. Finite tests do not prove cancellation.
"""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import shlex
import sys
import time

from run_regression_pass67 import ROOT, run_one, stamp


INHERITED_RECORD = "research/verification-pass73-working.json"
ADDITIONS = [
    ("research/affine_linear_adapted_checks_pass74.py", 2),
    ("research/nice_slice_adjoint_checks_pass74.py", 3),
    ("research/slice_projection_checks_pass74.py", 2),
    ("research/nice_good_partial_checks_pass75.py", 1),
    ("research/nice_common_slice_checks_pass75.py", 2),
    ("research/conic_slice_family_checks_pass75.py", 3),
]


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load_suites():
    inherited = json.loads((ROOT / INHERITED_RECORD).read_text())
    if (not inherited["all_passed"]
            or inherited["total_suites"] != 140
            or len(inherited["suites"]) != 140
            or inherited["total_test_methods"] != 1034
            or sum(s["test_methods"] for s in inherited["suites"]) != 1034
            or not all(s["all_passed"] and s["exit_code"] == 0
                       for s in inherited["suites"])):
        raise ValueError("Expected the complete successful140-suite73 capture")
    suites = [{
        "name": s["name"], "command": s["command"],
        "working_addition": s.get("working_addition", False),
        "current_pass_addition": False,
        "expected_test_methods": s["test_methods"],
    } for s in inherited["suites"]]
    for filename, count in ADDITIONS:
        suites.append({
            "name": Path(filename).stem,
            "command": shlex.join([sys.executable, filename]),
            "working_addition": True,
            # The helper retains output for all additions since full73.
            "current_pass_addition": True,
            "expected_test_methods": count,
        })
    if len(suites) != 146 or len({tuple(shlex.split(s["command"]))
                                 for s in suites}) != 146:
        raise ValueError("Expected146 distinct commands")
    if sum(s["expected_test_methods"] for s in suites) != 1047:
        raise ValueError("Expected1047 method executions")
    return suites


def main():
    suites = load_suites()
    source_paths = [path for path, _ in ADDITIONS] + [
        "research/run_regression_pass75.py", "research/run_regression_pass67.py",
        INHERITED_RECORD,
    ]
    before = {path: digest(path) for path in source_paths}
    started = stamp()
    timer = time.monotonic()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    after = {path: digest(path) for path in source_paths}
    additions = [s for s in results if s["current_pass_addition"]]
    working = [s for s in results if s["working_addition"]]
    result = {
        "started_at_utc": started,
        "finished_at_utc": stamp(),
        "wall_seconds": round(time.monotonic()-timer, 6),
        "runner": "research/run_regression_pass75.py",
        "subprocess_helper": "research/run_regression_pass67.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "inherited_record": INHERITED_RECORD,
        "inherited_suites": 140, "inherited_methods": 1034,
        "expected_total_suites": 146,
        "expected_total_test_methods": 1047,
        "total_suites": len(results),
        "total_test_methods": sum(s["test_methods"] or 0 for s in results),
        "working_addition_suites": len(working),
        "working_addition_methods": sum(s["test_methods"] or 0 for s in working),
        "additions_since_last_full_run_suites": len(additions),
        "additions_since_last_full_run_methods": sum(s["test_methods"] or 0
                                                     for s in additions),
        "new75_suites": 3, "new75_methods": 6,
        "all_passed": all(s["all_passed"] for s in results) and before == after,
        "source_hashes_before": before,
        "source_hashes_after": after,
        "source_inputs_unchanged": before == after,
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Actual finite regression only. Not verification of written proofs, source theorems, novelty, human review, a proof-assistant certificate or general cancellation.",
        "output_policy": "The frozen67 helper hashes complete combined stdout/stderr for every command. Successful inherited output is omitted; failed output and all six additions74--75 are retained. current_pass_addition in suite records means addition since full73, not new75 authorship.",
        "suites": results,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
