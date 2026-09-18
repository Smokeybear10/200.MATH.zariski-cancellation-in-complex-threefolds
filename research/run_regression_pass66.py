"""Rerun the frozen full60 suite set and all working61--66 additions.

Read-only runner: evidence is printed to stdout, not written into old packets.
Finite checks do not verify the cited classification theorems or cancellation.
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
ADDITIONS = [
    "research/square_speed_leading_checks_pass61.py",
    "research/moving_frame_divisibility_checks_pass65.py",
    "research/speed_curve_graph_checks_pass65.py",
    "research/dependent_low_flow_rank_checks_pass66.py",
]


def stamp():
    return datetime.now(timezone.utc).isoformat()


def run_one(suite):
    started = stamp()
    timer = time.monotonic()
    process = subprocess.run(
        shlex.split(suite["command"]), cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", process.stdout)
    success = (
        process.returncode == 0 and match is not None
        and re.search(r"(?m)^OK\s*$", process.stdout) is not None
        and re.search(r"(?m)^FAILED\b", process.stdout) is None
    )
    return {
        "name": suite["name"], "command": suite["command"],
        "working_addition": suite.get("working_addition", False),
        "started_at_utc": started, "finished_at_utc": stamp(),
        "test_methods": int(match[1]) if match else None,
        "elapsed_seconds": round(time.monotonic() - timer, 3),
        "unittest_seconds": float(match[2]) if match else None,
        "exit_code": process.returncode, "all_passed": success,
        "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
        "unittest_summary": match[0] if match else None,
        "output": process.stdout if (not success or suite.get("working_addition", False)) else "",
    }


def main():
    with (ROOT / "verification-pass-60.json").open() as source:
        baseline = json.load(source)
    suites = [
        {"name": suite["name"], "command": suite["command"]}
        for suite in baseline["suites"]
    ]
    assert len(suites) == 126
    assert baseline["total_test_methods"] == 1000
    for path in ADDITIONS:
        suites.append({
            "name": Path(path).stem,
            "command": shlex.join([sys.executable, path]),
            "working_addition": True,
        })
    assert len({suite["command"] for suite in suites}) == len(suites)
    started = stamp()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    methods = sum(suite["test_methods"] or 0 for suite in results)
    additions = [suite for suite in results if suite["working_addition"]]
    result = {
        "started_at_utc": started, "finished_at_utc": stamp(),
        "runner": "research/run_regression_pass66.py",
        "baseline_record": "verification-pass-60.json",
        "baseline_suites": 126, "baseline_methods": 1000,
        "total_suites": len(results), "total_test_methods": methods,
        "working_addition_suites": len(additions),
        "working_addition_methods": sum(s["test_methods"] or 0 for s in additions),
        "all_passed": all(s["all_passed"] for s in results),
        "central_registry_integrated": False,
        "scope": "Finite exact regression only. Written proofs, external source gates, human expert review, formal verification, novelty and the general conjecture are not verified by this run.",
        "general_cancellation_verified": False,
        "suites": results,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
