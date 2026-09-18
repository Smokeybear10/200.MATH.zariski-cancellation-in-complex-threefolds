"""Read-only integrity audit for the working67 proof packet.

Checks frozen files, actual captured evidence, links, and scope accounting.
It neither verifies theorem truth nor writes any record or checkpoint.
The first integrity capture precedes its own checkpoint, whose link is
explicitly deferred instead of inventing a circular preexisting packet.
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
    "research/dependent-constant-cubic-closure-pass67.md",
    "research/independent-cubic-graph-closure-pass67.md",
    "research/constant-cubic-nonomission-control-pass67.md",
    "research/constant_cubic_nonomission_checks_pass67.py",
    "research/constant_cubic_graph_checks_pass67.py",
    "research/run_regression_pass67.py",
    "research/verification-pass67-working.json",
    "research/constant-cubic-closure-pass67.md",
    "research/proof-audits-pass67-working.md",
    "research/consistency_checks_pass67.py",
]
MUTABLE = {"README.md", "research-ledger.md", "claims.json", "experiment-manifest.json"}
CURRENT_CHECKERS = [
    ("research/constant_cubic_nonomission_checks_pass67.py", 2),
    ("research/constant_cubic_graph_checks_pass67.py", 1),
]
CHECKPOINT = "research/checkpoint-pass67-working.json"


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def verify_records(records):
    for record in records:
        assert digest(record["path"]) == record["sha256"], record["path"]
    return len(records)


def link_prose(text):
    """Exclude TeX and fenced code before recognizing Markdown links.

    A commutator such as [E,T](x) in TeX is not a link to a file x.
    This does not suppress or defer links in the surrounding prose.
    """
    text = re.sub(r"(?ms)^(```|~~~)[^\n]*\n.*?^\1[ \t]*$", "", text)
    return re.sub(r"\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]", "", text)


def main():
    full = read_json("consistency-pass-60.json")
    old_records = [
        record
        for group in ("artifacts", "suite_sources", "source_inputs")
        for record in full[group]
        if record["path"] not in MUTABLE
    ]
    assert len(old_records) == 168
    old_count = verify_records(old_records)
    prior_packets = []
    prior_counts = {}
    for number, count in ((64, 13), (65, 11), (66, 9)):
        path = f"research/checkpoint-pass{number}-working.json"
        packet = read_json(path)
        records = packet["artifact_integrity"]["artifacts"]
        assert len(records) == count
        prior_counts[number] = verify_records(records)
        prior_packets.append({"path": path, "sha256": digest(path)})
    p65 = read_json(prior_packets[1]["path"])
    p66 = read_json(prior_packets[2]["path"])
    assert prior_packets[0]["sha256"] == p65["artifact_integrity"]["prior_packet"]["sha256"]
    assert prior_packets[:2] == p66["artifact_integrity"]["prior_packets"]

    old_run = read_json("research/verification-pass66-working.json")
    run = read_json("research/verification-pass67-working.json")
    suites = run["suites"]
    assert run["runner"] == "research/run_regression_pass67.py"
    assert run["baseline_record"] == "verification-pass-60.json"
    assert (run["baseline_suites"], run["baseline_methods"]) == (126, 1000)
    assert run["inherited_record"] == "research/verification-pass66-working.json"
    assert (run["inherited_suites"], run["inherited_methods"]) == (130, 1008)
    assert len(suites) == run["total_suites"] == run["expected_total_suites"] == 132
    assert sum(s["test_methods"] for s in suites) == run["total_test_methods"] == 1011
    assert run["expected_total_test_methods"] == 1011
    assert all(s["all_passed"] and s["exit_code"] == 0 for s in suites)
    assert run["all_passed"] is True
    assert run["general_cancellation_verified"] is False
    assert run["central_registry_integrated"] is False
    assert [s["command"] for s in suites[:130]] == [s["command"] for s in old_run["suites"]]
    assert [s["name"] for s in suites[:130]] == [s["name"] for s in old_run["suites"]]
    assert [s["test_methods"] for s in suites[:130]] == [s["test_methods"] for s in old_run["suites"]]
    assert [s["working_addition"] for s in suites[:130]] == [s["working_addition"] for s in old_run["suites"]]
    assert len({tuple(shlex.split(s["command"])) for s in suites}) == 132
    working = [s for s in suites if s["working_addition"]]
    current = [s for s in suites if s["current_pass_addition"]]
    assert len(working) == run["working_addition_suites"] == 6
    assert sum(s["test_methods"] for s in working) == run["working_addition_methods"] == 11
    assert len(current) == run["current_pass_addition_suites"] == 2
    assert sum(s["test_methods"] for s in current) == run["current_pass_addition_methods"] == 3
    assert current == suites[130:]
    started = datetime.fromisoformat(run["started_at_utc"])
    finished = datetime.fromisoformat(run["finished_at_utc"])
    assert started.tzinfo is not None and finished.tzinfo is not None
    assert started <= finished
    for suite in suites:
        assert suite["method_count_matches"] is True
        assert suite["test_methods"] == suite["expected_test_methods"]
        assert suite["launch_error"] is None
        assert re.fullmatch(r"[0-9a-f]{64}", suite["stdout_sha256"])
        match = re.fullmatch(r"Ran (\d+) tests? in ([\d.]+)s", suite["unittest_summary"])
        assert match and int(match[1]) == suite["test_methods"]
        assert float(match[2]) == suite["unittest_seconds"]
        assert suite["unittest_seconds"] >= 0 and suite["elapsed_seconds"] >= 0
        s_start = datetime.fromisoformat(suite["started_at_utc"])
        s_end = datetime.fromisoformat(suite["finished_at_utc"])
        assert started <= s_start <= s_end <= finished
        assert bool(suite["output"]) == suite["current_pass_addition"]
        if suite["output"]:
            assert hashlib.sha256(suite["output"].encode()).hexdigest() == suite["stdout_sha256"]
            assert suite["unittest_summary"] in suite["output"]
            assert re.search(r"(?m)^OK\s*$", suite["output"])
            assert not re.search(r"(?m)^FAILED\b", suite["output"])

    checker_records = []
    for (checker, count), captured in zip(CURRENT_CHECKERS, current):
        tree = ast.parse((ROOT / checker).read_text())
        methods = [n.name for n in ast.walk(tree)
                   if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
        imports = [a.name for n in ast.walk(tree) if isinstance(n, ast.Import)
                   for a in n.names]
        assert len(methods) == count == captured["test_methods"]
        assert imports == ["unittest", "sympy"]
        assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))
        assert captured["name"] == Path(checker).stem
        assert shlex.split(captured["command"])[1:] == [checker]
        checker_records.append({"path": checker, "methods": methods, "imports": imports})
    runner_tree = ast.parse((ROOT / "research/run_regression_pass67.py").read_text())
    additions = next(ast.literal_eval(n.value) for n in runner_tree.body
                     if isinstance(n, ast.Assign) and any(
                         isinstance(t, ast.Name) and t.id == "ADDITIONS" for t in n.targets))
    assert additions == CURRENT_CHECKERS

    records = []
    links = 0
    deferred_links = []
    assert len(ARTIFACTS) == len(set(ARTIFACTS)) == 10
    for name in ARTIFACTS:
        path = ROOT / name
        raw = path.read_bytes()
        text = raw.decode()
        assert raw.endswith(b"\n"), name
        assert "\r" not in text and "\u2014" not in text, name
        assert all(line == line.rstrip() for line in text.splitlines()), name
        equations = [int(n) for n in re.findall(r"\\tag\{(\d+)\}", text)]
        assert equations == list(range(1, len(equations) + 1)), name
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
        "prior_working64_artifacts": prior_counts[64],
        "prior_working65_artifacts": prior_counts[65],
        "prior_working66_artifacts": prior_counts[66],
        "prior_packets": prior_packets,
        "local_link_paths_checked": links,
        "deferred_future_checkpoint_links": deferred_links,
        "link_anchors_checked": False,
        "current_new_checkers": checker_records,
        "regression": {"suites": 132, "methods": 1011, "all_passed": True},
        "current_additions": {"suites": 2, "methods": 3},
        "all_working61_through67_additions": {"suites": 6, "methods": 11},
        "retained_output_hashes_recomputed": len(current),
        "omitted_legacy_output_hashes_recomputed": False,
        "central_claim_registry_integrated": False,
        "general_cancellation_verified": False,
        "scope": "Artifact integrity and actual captured finite-test accounting, not mathematical proof verification. An absent current checkpoint link is deferred because this capture precedes that packet; omitted legacy output is not reconstructed from hashes.",
        "artifacts": records,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
