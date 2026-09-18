"""Read-only full regression of the captured69 suites plus additions70--73.

This runner prints actual subprocess evidence and does not edit records.
Finite computations are not proofs of the written recognition theorems.
"""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shlex
import sys

from run_regression_pass67 import ROOT, run_one, stamp


INHERITED_RECORD = "research/verification-pass69-working.json"
ADDITIONS = [
    ("research/finite_root_top_checks_pass70.py", 2),
    ("research/terminal_quartic_recognition_checks_pass71.py", 3),
    ("research/quintic_rank_drop_checks_pass72.py", 5),
    ("research/higher_joint_rank_checks_pass73.py", 3),
]


def load_suites():
    inherited = json.loads((ROOT / INHERITED_RECORD).read_text())
    if (not inherited["all_passed"]
            or inherited["total_suites"] != 136
            or len(inherited["suites"]) != 136
            or inherited["total_test_methods"] != 1021
            or sum(s["test_methods"] for s in inherited["suites"]) != 1021
            or not all(s["all_passed"] and s["exit_code"] == 0
                       for s in inherited["suites"])):
        raise ValueError("Expected the complete successful136-suite69 capture")
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
            # Retain output of every addition since the last full run.
            "current_pass_addition": True,
            "expected_test_methods": count,
        })
    if len(suites) != 140 or len({tuple(shlex.split(s["command"]))
                                 for s in suites}) != 140:
        raise ValueError("Expected140 distinct commands")
    if sum(s["expected_test_methods"] for s in suites) != 1034:
        raise ValueError("Expected1034 method executions")
    return suites


def main():
    suites = load_suites()
    started = stamp()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    additions = [s for s in results if s["current_pass_addition"]]
    working = [s for s in results if s["working_addition"]]
    result = {
        "started_at_utc": started,
        "finished_at_utc": stamp(),
        "runner": "research/run_regression_pass73.py",
        "subprocess_helper": "research/run_regression_pass67.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "inherited_record": INHERITED_RECORD,
        "inherited_suites": 136, "inherited_methods": 1021,
        "expected_total_suites": 140,
        "expected_total_test_methods": 1034,
        "total_suites": len(results),
        "total_test_methods": sum(s["test_methods"] or 0 for s in results),
        "working_addition_suites": len(working),
        "working_addition_methods": sum(s["test_methods"] or 0 for s in working),
        "additions_since_last_full_run_suites": len(additions),
        "additions_since_last_full_run_methods": sum(s["test_methods"] or 0
                                                     for s in additions),
        "new73_suites": 1, "new73_methods": 3,
        "all_passed": all(s["all_passed"] for s in results),
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Actual finite regression only. Not verification of written proofs, source theorems, novelty, human review, a proof-assistant certificate or general cancellation.",
        "output_policy": "The frozen67 helper hashes complete combined stdout/stderr for every command. Successful inherited output is omitted; failed output and all four additions70--73 are retained. current_pass_addition in suite records means addition since the last full69 capture, not new73 authorship.",
        "suites": results,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
