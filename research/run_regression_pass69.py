"""Read-only combined regression of frozen67, targeted68, and three new69 suites.

The frozen subprocess helper is reused without modifying it. It records each
actual exit, timing, count and full-output hash. Successful inherited output
is omitted; all three current69 outputs are retained. No file is written.
Finite exact tests are not formal proof verification or general cancellation.
"""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shlex
import sys

from run_regression_pass67 import ROOT, run_one, stamp


INHERITED_RECORD = "research/verification-pass67-working.json"
ADDITIONS = [
    ("research/independent_higher_constant_checks_pass68.py", 2, False),
    ("research/normalized_defect_projection_checks_pass69.py", 3, True),
    ("research/rational_two_direction_checks_pass69.py", 3, True),
    ("research/cubic_shear_vertical_checks_pass69.py", 2, True),
]


def load_suites():
    inherited = json.loads((ROOT / INHERITED_RECORD).read_text())
    assert inherited["all_passed"] is True
    assert inherited["total_suites"] == len(inherited["suites"]) == 132
    assert inherited["total_test_methods"] == sum(s["test_methods"] for s in inherited["suites"]) == 1011
    assert all(s["all_passed"] and s["exit_code"] == 0 for s in inherited["suites"])
    suites = [{
        "name": s["name"], "command": s["command"],
        "working_addition": s.get("working_addition", False),
        "current_pass_addition": False,
        "expected_test_methods": s["test_methods"],
    } for s in inherited["suites"]]
    for path, count, current in ADDITIONS:
        suites.append({
            "name": Path(path).stem,
            "command": shlex.join([sys.executable, path]),
            "working_addition": True, "current_pass_addition": current,
            "expected_test_methods": count,
        })
    assert len(suites) == len({tuple(shlex.split(s["command"])) for s in suites}) == 136
    assert sum(s["expected_test_methods"] for s in suites) == 1021
    working = [s for s in suites if s["working_addition"]]
    current = [s for s in suites if s["current_pass_addition"]]
    assert len(working) == 10 and sum(s["expected_test_methods"] for s in working) == 21
    assert len(current) == 3 and sum(s["expected_test_methods"] for s in current) == 8
    return suites


def main():
    suites = load_suites()
    started = stamp()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    working = [s for s in results if s["working_addition"]]
    current = [s for s in results if s["current_pass_addition"]]
    result = {
        "started_at_utc": started, "finished_at_utc": stamp(),
        "runner": "research/run_regression_pass69.py",
        "subprocess_helper": "research/run_regression_pass67.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "inherited_record": INHERITED_RECORD,
        "inherited_suites": 132, "inherited_methods": 1011,
        "expected_total_suites": 136, "expected_total_test_methods": 1021,
        "total_suites": len(results),
        "total_test_methods": sum(s["test_methods"] or 0 for s in results),
        "working_addition_suites": len(working),
        "working_addition_methods": sum(s["test_methods"] or 0 for s in working),
        "current_pass_addition_suites": len(current),
        "current_pass_addition_methods": sum(s["test_methods"] or 0 for s in current),
        "all_passed": all(s["all_passed"] for s in results),
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Actual finite exact regression. Written proofs, source theorems, human expert review, proof-assistant verification, novelty and general cancellation are not verified by this run.",
        "output_policy": "The frozen67 subprocess helper hashes full combined stdout/stderr for every launched command. Successful inherited output, including the now-rerun68 suite, is omitted. Failed and current69 output is retained; launch errors are separate.",
        "suites": results,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
