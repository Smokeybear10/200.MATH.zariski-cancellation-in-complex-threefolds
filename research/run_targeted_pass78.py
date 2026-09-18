"""Print fresh finite pass78 evidence without overwriting saved captures."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
CHECKER = "research/nice_binary_ramification_checks_pass78.py"
RUNNER = "research/run_targeted_pass78.py"
PREVIOUS = "research/verification-pass75-working.json"
EXPECTED_METHODS = 4


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    before = {path: digest(path) for path in (CHECKER, RUNNER, PREVIOUS)}
    old = json.loads((ROOT / PREVIOUS).read_text())
    if (not old["all_passed"] or old["total_suites"] != 146
            or old["total_test_methods"] != 1047):
        raise ValueError("Expected preserved full75 evidence")
    started, timer = stamp(), time.monotonic()
    command = [sys.executable, CHECKER]
    completed = subprocess.run(
        command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=120)
    finished, elapsed = stamp(), time.monotonic() - timer
    output = completed.stdout
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    count = int(match.group(1)) if match else None
    after = {path: digest(path) for path in before}
    passed = (completed.returncode == 0 and count == EXPECTED_METHODS
              and re.search(r"(?m)^OK$", output) is not None
              and before == after)
    record = {
        "kind": "Fresh targeted78 capture, not a full regression",
        "started_at_utc": started,
        "finished_at_utc": finished,
        "wall_seconds": round(elapsed, 6),
        "total_suites": 1,
        "total_test_methods": count,
        "all_passed": passed,
        "new78_suites": 1,
        "new78_test_methods": EXPECTED_METHODS,
        "fresh_full78_regression_performed": False,
        "last_full_regression": {
            "path": PREVIOUS, "sha256": before[PREVIOUS],
            "suites": 146, "test_methods": 1047,
        },
        "source_hashes_before": before,
        "source_hashes_after": after,
        "source_inputs_unchanged": before == after,
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": (
            "Finite exact examples, inverse maps, ideal reductions and "
            "operator identities. Not verification of universal proofs, "
            "primary geometric inputs, historical novelty or cancellation. "
            "Repeated runs are not additional test methods."
        ),
        "suites": [{
            "path": CHECKER, "command": command,
            "exit_code": completed.returncode,
            "expected_methods": EXPECTED_METHODS,
            "test_methods": count, "all_passed": passed,
            "unittest_seconds": float(match.group(2)) if match else None,
            "output": output,
            "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
        }],
    }
    print(json.dumps(record, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

