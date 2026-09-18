"""Print fresh finite pass83 evidence without writing saved captures."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
RUNNER = "research/run_targeted_pass83.py"
PREVIOUS = "research/verification-pass75-working.json"
CHECKER = "research/rank_one_return_checks_pass83.py"
EXPECTED_METHODS = 3


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    paths = [CHECKER, RUNNER, PREVIOUS]
    before = {path: digest(path) for path in paths}
    old = json.loads((ROOT / PREVIOUS).read_text())
    if (not old["all_passed"] or old["total_suites"] != 146
            or old["total_test_methods"] != 1047):
        raise ValueError("Expected preserved full75 evidence")
    command = [sys.executable, CHECKER]
    started, timer = stamp(), time.monotonic()
    completed = subprocess.run(
        command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=60)
    finished = stamp()
    wall = round(time.monotonic() - timer, 6)
    output = completed.stdout
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    count = int(match.group(1)) if match else None
    suite_passed = (completed.returncode == 0 and count == EXPECTED_METHODS
                    and re.search(r"(?m)^OK$", output) is not None)
    after = {path: digest(path) for path in paths}
    passed = suite_passed and before == after
    suite = {
        "path": CHECKER, "command": command,
        "started_at_utc": started, "finished_at_utc": finished,
        "wall_seconds": wall, "exit_code": completed.returncode,
        "expected_methods": EXPECTED_METHODS, "test_methods": count,
        "method_count_matches": count == EXPECTED_METHODS,
        "all_passed": suite_passed,
        "unittest_seconds": float(match.group(2)) if match else None,
        "output": output,
        "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
    }
    record = {
        "kind": "Fresh targeted83 capture, not a full regression",
        "started_at_utc": started, "finished_at_utc": finished,
        "wall_seconds": wall, "total_suites": 1,
        "total_test_methods": count or 0, "all_passed": passed,
        "new83_suites": 1, "new83_test_methods": EXPECTED_METHODS,
        "fresh_full83_regression_performed": False,
        "last_full_regression": {
            "path": PREVIOUS, "sha256": before[PREVIOUS],
            "suites": 146, "test_methods": 1047,
        },
        "source_hashes_before": before, "source_hashes_after": after,
        "source_inputs_unchanged": before == after,
        "bounded_search_executed": False,
        "search_candidates_are_test_methods": False,
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": (
            "Three finite exact methods: an actual two-speed action and "
            "rational return with frozen Taylor identities, a polynomial "
            "isolated jet failing its full lift determinant, and ideal "
            "integrality versus membership and valuation controls. Not "
            "a proof of arbitrary action recognition or a universal "
            "source theorem. Repeated runs do not add methods."
        ),
        "suites": [suite],
    }
    print(json.dumps(record, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
