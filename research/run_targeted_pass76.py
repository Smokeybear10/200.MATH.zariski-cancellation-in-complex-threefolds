"""Print a fresh targeted pass76 capture; never alter saved evidence."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
CHECKER = "research/nice_frontier_checks_pass76.py"
PREVIOUS = "research/verification-pass75-working.json"
RUNNER = "research/run_targeted_pass76.py"


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    before = {path: digest(path) for path in [CHECKER, RUNNER, PREVIOUS]}
    old = json.loads((ROOT / PREVIOUS).read_text())
    if (not old["all_passed"] or old["total_suites"] != 146
            or old["total_test_methods"] != 1047):
        raise ValueError("Expected the preserved full75 capture")
    started, timer = stamp(), time.monotonic()
    command = [sys.executable, CHECKER]
    completed = subprocess.run(command, cwd=ROOT, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               timeout=120)
    finished, elapsed = stamp(), time.monotonic() - timer
    output = completed.stdout
    found = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    count = int(found.group(1)) if found else None
    after = {path: digest(path) for path in before}
    passed = (completed.returncode == 0 and count == 6
              and re.search(r"(?m)^OK$", output) is not None and before == after)
    record = {
        "kind": "Fresh targeted76 capture, not a full regression",
        "started_at_utc": started, "finished_at_utc": finished,
        "wall_seconds": round(elapsed, 6),
        "total_suites": 1, "total_test_methods": count,
        "all_passed": passed,
        "new76_suites": 1, "new76_test_methods": 6,
        "fresh_full76_regression_performed": False,
        "last_full_regression": {
            "path": PREVIOUS, "sha256": before[PREVIOUS],
            "suites": 146, "test_methods": 1047,
        },
        "source_hashes_before": before, "source_hashes_after": after,
        "source_inputs_unchanged": before == after,
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Finite exact examples and operator identities. Not verification of universal written theorems, geometric sources, novelty or a formal proof. Repeated executions are not extra test methods.",
        "suites": [{
            "path": CHECKER, "command": command,
            "exit_code": completed.returncode, "expected_methods": 6,
            "test_methods": count, "all_passed": passed,
            "unittest_seconds": float(found.group(2)) if found else None,
            "output": output,
            "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
        }],
    }
    print(json.dumps(record, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
