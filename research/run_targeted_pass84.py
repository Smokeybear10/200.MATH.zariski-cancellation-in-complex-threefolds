"""Print fresh finite pass84 evidence without writing saved captures."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
RUNNER = "research/run_targeted_pass84.py"
PREVIOUS = "research/verification-pass75-working.json"
SUITES = (
    ("research/strict_slice_checks_pass84.py", 2),
    ("research/embedded_square_controls_pass84.py", 1),
)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def run_suite(spec):
    path, expected = spec
    command = [sys.executable, path]
    started, timer = stamp(), time.monotonic()
    completed = subprocess.run(
        command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=60)
    output = completed.stdout
    match = re.search(r"Ran (\d+) tests? in ([\d.]+)s", output)
    count = int(match.group(1)) if match else None
    passed = (completed.returncode == 0 and count == expected
              and re.search(r"(?m)^OK$", output) is not None)
    return {
        "path": path, "command": command,
        "started_at_utc": started, "finished_at_utc": stamp(),
        "wall_seconds": round(time.monotonic() - timer, 6),
        "exit_code": completed.returncode,
        "expected_methods": expected, "test_methods": count,
        "method_count_matches": count == expected,
        "all_passed": passed,
        "unittest_seconds": float(match.group(2)) if match else None,
        "output": output,
        "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
    }


def main():
    paths = [path for path, _ in SUITES] + [RUNNER, PREVIOUS]
    before = {path: digest(path) for path in paths}
    old = json.loads((ROOT / PREVIOUS).read_text())
    if (not old["all_passed"] or old["total_suites"] != 146
            or old["total_test_methods"] != 1047):
        raise ValueError("Expected preserved full75 evidence")
    started, timer = stamp(), time.monotonic()
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(run_suite, SUITES))
    after = {path: digest(path) for path in paths}
    passed = all(item["all_passed"] for item in results) and before == after
    record = {
        "kind": "Fresh targeted84 capture, not a full regression",
        "started_at_utc": started, "finished_at_utc": stamp(),
        "wall_seconds": round(time.monotonic() - timer, 6),
        "total_suites": len(results),
        "total_test_methods": sum(item["test_methods"] or 0 for item in results),
        "all_passed": passed,
        "new84_suites": 2, "new84_test_methods": 3,
        "fresh_full84_regression_performed": False,
        "last_full_regression": {
            "path": PREVIOUS, "sha256": before[PREVIOUS],
            "suites": 146, "test_methods": 1047,
        },
        "source_hashes_before": before,
        "source_hashes_after": after,
        "source_inputs_unchanged": before == after,
        "bounded_search_executed": False,
        "search_candidates_are_test_methods": False,
        "central_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": (
            "Three finite exact methods in two suites: two actual sliced "
            "polynomial actions and their strict Taylor certificates, "
            "plus one ideal-only embedded-square and trace-boundary "
            "control. Not a universal proof, an action realization of "
            "the ideal data, or a full regression. Repeats and helper "
            "calculations do not add methods. No search is executed."
        ),
        "suites": results,
    }
    print(json.dumps(record, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
