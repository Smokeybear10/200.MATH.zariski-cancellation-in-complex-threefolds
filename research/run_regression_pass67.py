"""Rerun the actual 130-command pass66 capture plus the two pass67 suites.

Read-only runner: JSON evidence is printed to stdout. No verification record,
checkpoint, registry, or frozen packet is written by this script. Successful
legacy output is compacted only after hashing its full captured text. Finite
checks do not verify the written classification arguments or cancellation.
"""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent.parent
INHERITED_RECORD = "research/verification-pass66-working.json"
ADDITIONS = [
    ("research/constant_cubic_nonomission_checks_pass67.py", 2),
    ("research/constant_cubic_graph_checks_pass67.py", 1),
]


def stamp():
    return datetime.now(timezone.utc).isoformat()


def load_suites():
    with (ROOT / INHERITED_RECORD).open() as source:
        inherited = json.load(source)
    if (
        inherited["total_suites"] != 130
        or inherited["total_test_methods"] != 1008
        or not inherited["all_passed"]
        or len(inherited["suites"]) != 130
        or sum(s["test_methods"] for s in inherited["suites"]) != 1008
        or not all(s["all_passed"] and s["exit_code"] == 0
                   for s in inherited["suites"])
    ):
        raise ValueError("Expected the successful 130-suite, 1008-method pass66 capture")
    suites = [
        {
            "name": s["name"], "command": s["command"],
            "working_addition": s.get("working_addition", False),
            "current_pass_addition": False,
            "expected_test_methods": s["test_methods"],
        }
        for s in inherited["suites"]
    ]
    for path, methods in ADDITIONS:
        suites.append({
            "name": Path(path).stem,
            "command": shlex.join([sys.executable, path]),
            "working_addition": True, "current_pass_addition": True,
            "expected_test_methods": methods,
        })
    if len({tuple(shlex.split(s["command"])) for s in suites}) != 132:
        raise ValueError("The 132 commands must be distinct after shell-word parsing")
    if sum(s["expected_test_methods"] for s in suites) != 1011:
        raise ValueError("Expected exactly 1011 distinct test methods in this command set")
    historical = [s for s in suites if s["working_addition"]
                  and not s["current_pass_addition"]]
    if len(historical) != 4 or sum(s["expected_test_methods"] for s in historical) != 8:
        raise ValueError("Expected the four historical working61--66 suites and eight methods")
    return suites


def run_one(suite):
    started = stamp()
    timer = time.monotonic()
    launch_error = None
    try:
        process = subprocess.run(
            shlex.split(suite["command"]), cwd=ROOT, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
        )
        output, exit_code = process.stdout, process.returncode
    except OSError as error:
        output, exit_code = "", None
        launch_error = f"{type(error).__name__}: {error}"
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    methods = int(match[1]) if match else None
    count_matches = methods == suite["expected_test_methods"]
    success = (
        exit_code == 0 and match is not None and count_matches
        and re.search(r"(?m)^OK\s*$", output) is not None
        and re.search(r"(?m)^FAILED\b", output) is None
    )
    return {
        "name": suite["name"], "command": suite["command"],
        "working_addition": suite["working_addition"],
        "current_pass_addition": suite["current_pass_addition"],
        "started_at_utc": started, "finished_at_utc": stamp(),
        "expected_test_methods": suite["expected_test_methods"],
        "test_methods": methods, "method_count_matches": count_matches,
        "elapsed_seconds": round(time.monotonic() - timer, 3),
        "unittest_seconds": float(match[2]) if match else None,
        "exit_code": exit_code, "all_passed": success,
        "launch_error": launch_error,
        "stdout_sha256": hashlib.sha256(output.encode()).hexdigest(),
        "unittest_summary": match[0] if match else None,
        "output": output if (not success or suite["current_pass_addition"]) else "",
    }


def main():
    suites = load_suites()
    started = stamp()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    methods = sum(s["test_methods"] or 0 for s in results)
    working = [s for s in results if s["working_addition"]]
    current = [s for s in results if s["current_pass_addition"]]
    result = {
        "started_at_utc": started, "finished_at_utc": stamp(),
        "runner": "research/run_regression_pass67.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "inherited_record": INHERITED_RECORD,
        "inherited_suites": 130, "inherited_methods": 1008,
        "expected_total_suites": 132, "expected_total_test_methods": 1011,
        "total_suites": len(results), "total_test_methods": methods,
        "working_addition_suites": len(working),
        "working_addition_methods": sum(s["test_methods"] or 0 for s in working),
        "current_pass_addition_suites": len(current),
        "current_pass_addition_methods": sum(s["test_methods"] or 0 for s in current),
        "all_passed": all(s["all_passed"] for s in results),
        "central_registry_integrated": False,
        "scope": "Finite exact regression only. Written proofs, external source gates, human expert review, formal verification, novelty and the general conjecture are not verified by this run.",
        "output_policy": "Full combined stdout/stderr text is hashed for every launched command; successful inherited output is omitted, while failed and current-pass output is retained. Launch errors are reported separately.",
        "general_cancellation_verified": False,
        "suites": results,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
