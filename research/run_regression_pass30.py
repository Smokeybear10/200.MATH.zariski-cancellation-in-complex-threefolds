"""Run the recorded 55-suite checkpoint and three independent pass-30 suites.

Print JSON to stdout. No source or evidence files are written. Direct suite
commands are also listed in README.md. A unittest summary may be followed by
a suite's JSON report, so success is not required to be the final line.
"""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shlex
import subprocess
import time


ROOT = Path(__file__).resolve().parent.parent


def stamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def passed_summary(output, exit_code):
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    return (
        exit_code == 0 and match is not None
        and re.search(r"(?m)^OK\s*$", output) is not None
        and re.search(r"(?m)^FAILED\b", output) is None
    )


def run_one(suite):
    started = time.monotonic()
    process = subprocess.run(
        shlex.split(suite["command"]), cwd=ROOT,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        check=False,
    )
    output = process.stdout
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    result = {
        "name": suite["name"], "command": suite["command"],
        "test_methods": int(match[1]) if match else None,
        "elapsed_seconds": round(time.monotonic()-started, 3),
        "unittest_seconds": float(match[2]) if match else None,
        "exit_code": process.returncode,
        "all_passed": passed_summary(output, process.returncode),
    }
    if not result["all_passed"]:
        result["output"] = output
    return result


def main():
    # Orchestration parser controls, not mathematical unittest methods.
    assert passed_summary("Ran 1 test in 0.1s\n\nOK\n", 0)
    assert passed_summary('Ran 2 tests in 0.1s\n\nOK\n{"successful": true}\n', 0)
    assert not passed_summary("Ran 1 test in 0.1s\n\nFAILED (failures=1)\n", 1)
    assert not passed_summary("Ran 1 test in 0.1s\n\nOK\n", 1)
    assert not passed_summary('{"successful": true}\n', 0)
    with (ROOT/"verification-pass-29.json").open() as source:
        suites = json.load(source)["suites"]
    suites.extend([
        {
            "name": "finite_closure_frame",
            "command": "/opt/anaconda3/bin/python research/finite_closure_frame_checks_pass30.py",
        },
        {
            "name": "horizontal_gauge",
            "command": "/opt/anaconda3/bin/python research/horizontal_gauge_checks_pass30.py",
        },
        {
            "name": "all_noninvariant_surface",
            "command": "/opt/anaconda3/bin/python research/all_noninvariant_surface_checks_pass30.py",
        },
    ])
    started = stamp()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run_one, suites))
    result = {
        "checked_at_utc": started, "completed_at_utc": stamp(),
        "working_directory": str(ROOT), "suites": results,
        "total_test_methods": sum(s["test_methods"] or 0 for s in results),
        "all_passed": all(s["all_passed"] for s in results),
        "total_suites": len(results),
        "new_suite_test_methods": sum(s["test_methods"] or 0 for s in results[55:]),
        "new_suite_count": 3,
        "runner": "research/run_regression_pass30.py",
        "orchestration_parser_controls": 5,
        "orchestration_controls_counted_as_test_methods": False,
        "scope": (
            "Finite exact controls and prior regression checks. Written general "
            "proofs and cited classification inputs are not replaced by these tests; "
            "no Lean proof, human expert review, novelty certification, or unrestricted "
            "complex threefold cancellation solution."
        ),
        "general_cancellation_verified": False, "human_expert_review": False,
        "proof_assistant_verified": False, "novelty_established": False,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
