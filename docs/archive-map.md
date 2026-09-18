# Repository and archive map

[Home](../README.md) · [Current status](current-status.md) · [Review guide](review-guide.md)

The repository keeps working proofs and historical evidence at their
existing paths. Navigation pages organize the reading without relocating
files that earlier notes, manifests, and scripts refer to.

## Reader-facing pages

| Location | Purpose |
| --- | --- |
| [README.md](../README.md) | Short GitHub front page and starting points. |
| [start-here.md](start-here.md) | Plain-English question, latest result, and glossary. |
| [current-status.md](current-status.md) | Current checkpoint and the exact remaining gap. |
| [review-guide.md](review-guide.md) | Proof-reading order and questions for a mathematical reviewer. |
| [research/README.md](../research/README.md) | Selected technical index, rather than a list of every archived file. |

## Working proofs and research history

| Location or pattern | How to use it |
| --- | --- |
| `research/*.md` | Detailed proofs, route tests, counterexamples to methods, and source audits. Follow the selected index first. |
| [research-ledger.md](../research-ledger.md) | Dated evidence and decisions. Administrative entries are not new mathematical results. |
| [README-history.md](../README-history.md) | The former long front page, preserved in full beneath an archive banner. It is a snapshot, not a live status page. |
| [research-note.md](../research-note.md) | The first pedagogical investigation and early baselines. It is not the latest frontier. |
| `deep-pass-*.md` | Earlier investigation narratives. Read in their original historical context. |

Pass numbers track investigation sessions. They are not publication
numbers, counts of independent theorems, or evidence of novelty. A filename
ending in `working` does not itself establish or refute a claim: read the
assumptions, proof, review record, and later corrections.

## Registries, scripts, and verification records

| Location or pattern | Status |
| --- | --- |
| [claims.json](../claims.json) | Historical registry dated September 13, 2026; 544 entries ending at Z544. It does not cover the latest checkpoint. |
| [experiment-manifest.json](../experiment-manifest.json) | Historical manifest describing the frozen pass58–60 packet. Do not treat its counts as current. |
| `verification-pass-*.json`, `consistency-pass-*.json` | Saved results from their stated passes, not a current whole-project certificate. |
| `research/verification-*.json`, `research/checkpoint-*.json` | Pass-specific evidence; scope and later supersession matter. |
| `verify_*.py`, `research/*.py` | Archived checker and experiment code. **Frozen: do not run, import, compile, or edit.** |

No code or mathematical proof was changed to make the front page easier
to read. Historical script outputs remain historical; this cleanup is
not a fresh execution of the experiments or proof checks.

Some old consistency scripts expect historical command lists inside
`README.md`. Those lists now live in `README-history.md`, so that old
navigation assumption no longer holds. The scripts have deliberately
not been run or changed to accommodate the new front page. Older notes
linking to README for commands should use the historical-page link instead.

## Material intentionally absent from GitHub

The local `tmp/` tree contains downloaded papers and extracted previews.
It is excluded from version control, as are Python bytecode caches and
local environment files. Source notes retain bibliographic links, but
some historical local download paths will not exist in a fresh clone.

The repository remains private. It contains project attribution and local
paths and has not been cleared for public release. Public posting, expert
outreach, submission, and public novelty claims require explicit approval.

## Keeping the navigation current

When the mathematical checkpoint changes, update the front page and
current-status page together, link the exact proof and ledger evidence,
and retain qualifications about unproved hypotheses. Do not silently
promote an old registry or a successful computation into a universal proof.

Keep the historical front-page snapshot intact. Navigation updates do not
unfreeze saved checkers or authorize automatic GitHub pushes.
