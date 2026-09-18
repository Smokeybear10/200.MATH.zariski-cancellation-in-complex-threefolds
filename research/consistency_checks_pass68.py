"""Read-only integrity audit for the working68 proof packet.

Checks files and the actual two-method targeted capture. It does not run
mathematical suites, create a full68 regression, or write any evidence.
An absent current checkpoint link is explicitly deferred because this
integrity capture is an input to that future packet.
"""

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex


ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = [
    "research/independent-higher-constant-closure-pass68.md",
    "research/dependent-constant-quartic-closure-pass68.md",
    "research/dependent-constant-quintic-closure-pass68.md",
    "research/moving-cubic-coordinate-local-slice-pass68.md",
    "research/moving-cubic-graph-recognition-pass68.md",
    "research/moving-cubic-constant-speed-recognition-pass68.md",
    "research/independent_higher_constant_checks_pass68.py",
    "research/proof-audits-pass68-working.md",
    "research/constant-and-moving-closure-pass68.md",
    "research/verification-pass68-working.json",
    "research/consistency_checks_pass68.py",
]
EXPECTED_EQUATIONS = {
    ARTIFACTS[0]: 22, ARTIFACTS[1]: 30, ARTIFACTS[2]: 27,
    ARTIFACTS[3]: 18, ARTIFACTS[4]: 13, ARTIFACTS[5]: 11,
    ARTIFACTS[8]: 7,
}
MUTABLE = {"README.md", "research-ledger.md", "claims.json", "experiment-manifest.json"}
CHECKER = "research/independent_higher_constant_checks_pass68.py"
CHECKPOINT = "research/checkpoint-pass68-working.json"
FROZEN67_SHA256 = "e6aef37fc9a9c860febf533cf06298b6a48cfcb56a53be1bf73e2b325b126d47"


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def verify_records(records):
    for record in records:
        assert digest(record["path"]) == record["sha256"], record["path"]
    return len(records)


def link_prose(text):
    """Exclude complete fenced code and TeX regions, not surrounding links."""
    text = re.sub(r"(?ms)^([\x60]{3}|~~~)[^\n]*\n.*?^\1[ \t]*$", "", text)
    return re.sub(r"\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]", "", text)


def main():
    full = read_json("consistency-pass-60.json")
    old_records = [
        r for group in ("artifacts", "suite_sources", "source_inputs")
        for r in full[group] if r["path"] not in MUTABLE
    ]
    assert len(old_records) == 168
    old_count = verify_records(old_records)
    packets, packet_records, prior_counts = {}, [], {}
    for number, count in ((64, 13), (65, 11), (66, 9), (67, 10)):
        path = f"research/checkpoint-pass{number}-working.json"
        packets[number] = read_json(path)
        records = packets[number]["artifact_integrity"]["artifacts"]
        assert len(records) == count
        prior_counts[number] = verify_records(records)
        packet_records.append({"path": path, "sha256": digest(path)})
    assert packet_records[0]["sha256"] == packets[65]["artifact_integrity"]["prior_packet"]["sha256"]
    assert packet_records[:2] == packets[66]["artifact_integrity"]["prior_packets"]
    assert packet_records[:3] == packets[67]["artifact_integrity"]["prior_packets"]
    assert packet_records[3]["sha256"] == FROZEN67_SHA256

    # These two historical integration files also remain at their full60 hashes.
    registry_records = [
        r for group in ("artifacts", "suite_sources", "source_inputs")
        for r in full[group] if r["path"] in {"claims.json", "experiment-manifest.json"}
    ]
    assert len(registry_records) == 2
    verify_records(registry_records)
    claims = read_json("claims.json")
    assert len(claims["claims"]) == 544
    for key in (
        "interpretation_confirmed_by_professor", "general_conjecture_solved",
        "novelty_claimed", "expert_review_completed", "full_formalization_completed",
    ):
        assert claims[key] is False, key

    # The previous complete regression is preserved, not rerun or augmented here.
    previous = read_json("research/verification-pass67-working.json")
    assert previous["all_passed"] is True
    assert previous["total_suites"] == len(previous["suites"]) == 132
    assert previous["total_test_methods"] == sum(s["test_methods"] for s in previous["suites"]) == 1011
    assert all(s["all_passed"] and s["exit_code"] == 0 for s in previous["suites"])
    assert previous["central_registry_integrated"] is False
    assert previous["general_cancellation_verified"] is False

    targeted = read_json("research/verification-pass68-working.json")
    assert targeted["fresh_full_regression_performed"] is False
    assert targeted["central_registry_integrated"] is False
    assert targeted["general_cancellation_verified"] is False
    assert targeted["new_targeted_suites"] == 1
    assert targeted["new_targeted_methods"] == 2
    assert targeted["last_full_regression"] == {
        "path": "research/verification-pass67-working.json",
        "test_methods": 1011, "suites": 132,
    }
    suite = targeted["suite"]
    assert suite["name"] == Path(CHECKER).stem
    assert shlex.split(suite["command"]) == ["/opt/anaconda3/bin/python", CHECKER]
    assert suite["test_methods"] == 2
    assert suite["exit_code"] == 0 and suite["all_passed"] is True
    output = suite["output"]
    summaries = re.findall(r"(?m)^Ran (\d+) tests? in ([\d.]+)s$", output)
    assert len(summaries) == 1
    assert int(summaries[0][0]) == 2
    assert float(summaries[0][1]) == suite["unittest_seconds"]
    assert re.search(r"(?m)^OK\s*$", output)
    assert not re.search(r"(?m)^FAILED\b", output)
    assert suite["tool_chunk_id"] == "bcc2e2"
    precision = targeted["clock_precision_seconds"]
    assert precision == 1
    started = datetime.strptime(targeted["started_at_utc"], "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    finished = datetime.strptime(targeted["finished_at_utc"], "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    assert started <= finished
    # Equal coarse timestamps do not falsely imply a zero-duration test run.
    assert 0 <= suite["unittest_seconds"] <= (finished - started).total_seconds() + precision
    output_sha256 = hashlib.sha256(output.encode()).hexdigest()

    tree = ast.parse((ROOT / CHECKER).read_text())
    methods = [
        n.name for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
    ]
    imports = [
        a.name for n in ast.walk(tree) if isinstance(n, ast.Import)
        for a in n.names
    ]
    assert len(methods) == len(set(methods)) == suite["test_methods"] == 2
    assert imports == ["unittest", "sympy"]
    assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))

    records, deferred_links = [], []
    links = 0
    assert len(ARTIFACTS) == len(set(ARTIFACTS)) == 11
    for name in ARTIFACTS:
        path = ROOT / name
        raw = path.read_bytes()
        text = raw.decode()
        assert raw.endswith(b"\n"), name
        assert "\r" not in text and "\u2014" not in text, name
        assert all(line == line.rstrip() for line in text.splitlines()), name
        equations = [int(n) for n in re.findall(r"\\tag\{(\d+)\}", text)]
        assert equations == list(range(1, len(equations) + 1)), name
        assert len(equations) == EXPECTED_EQUATIONS.get(name, 0), name
        if path.suffix == ".py":
            ast.parse(text)
        elif path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", link_prose(text)):
                target = target.strip("<>")
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                local = target.split("#", 1)[0]
                if not local:
                    continue
                resolved = (path.parent / local).resolve()
                if resolved == (ROOT / CHECKPOINT).resolve() and not resolved.exists():
                    deferred_links.append({"source": name, "target": CHECKPOINT})
                    continue
                assert resolved.exists(), (name, target)
                links += 1
        records.append({
            "path": name, "bytes": len(raw), "sha256": digest(name),
            "lines": len(text.splitlines()), "numbered_equations": len(equations),
            "source_footnotes": len(re.findall(r"(?m)^\[\^[^\]]+\]:", text)),
        })
    print(json.dumps({
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "all_passed": True,
        "old_full60_nonmutable_records": old_count,
        "historical_registry_and_manifest_records": len(registry_records),
        "central_claim_count": 544,
        "prior_working64_artifacts": prior_counts[64],
        "prior_working65_artifacts": prior_counts[65],
        "prior_working66_artifacts": prior_counts[66],
        "prior_working67_artifacts": prior_counts[67],
        "prior_packets": packet_records,
        "frozen67_checkpoint_sha256": FROZEN67_SHA256,
        "local_link_paths_checked": links,
        "deferred_future_checkpoint_links": deferred_links,
        "link_anchors_checked": False,
        "current_new_checker": {"path": CHECKER, "methods": methods, "imports": imports},
        "targeted_verification": {
            "path": "research/verification-pass68-working.json",
            "suites": 1, "methods": 2, "all_passed": True,
            "unittest_seconds": suite["unittest_seconds"],
            "stdout_sha256": output_sha256,
            "clock_precision_seconds": precision,
        },
        "last_full_regression": {"suites": 132, "methods": 1011, "all_passed": True},
        "fresh_full68_regression_performed": False,
        "central_claim_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Artifact integrity and actual targeted finite-test accounting, not mathematical proof verification or a fresh full68 regression. An absent current checkpoint link is explicitly deferred because this capture precedes that packet.",
        "artifacts": records,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
