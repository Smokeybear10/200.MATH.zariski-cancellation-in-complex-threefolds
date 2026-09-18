# Zariski cancellation research

Can adding one independent coordinate make a complicated algebraic space
look like ordinary coordinate space? This private notebook investigates
that question in the complex three-dimensional case.

**The main conjecture is not solved.** The repository contains conditional
proofs and counterexamples to proposed proof methods. Novelty is unknown;
there has been no human expert review or proof-assistant certification.

## Start here

| What you want | Read this |
| --- | --- |
| Understand the question without the technical background | [Plain-English introduction](docs/start-here.md) |
| See the current results and the missing step | [Current status](docs/current-status.md) |
| Examine the mathematics and challenge the proofs | [Reviewer reading guide](docs/review-guide.md) |
| Find older notes, sources, scripts, or records | [Archive map](docs/archive-map.md) |

You do not need to read the archive chronologically.

## Current work

The latest mathematical notes are **703 and 702**, dated September 18, 2026.
These numbers identify research passes, not separate publications.

- [703: a conditional translation criterion](research/raw-projection-centralizer-slice-criterion-pass703-working.md).
  A nonzero vector field commuting with all the specified raw projected
  coordinate directions must be locally nilpotent and have a slice.
  The proof does not show that such a field always exists.
- [702: why a direct extraction method can fail](research/all-slice-projected-lnd-obstruction-pass702-working.md).
  In a particular polynomial example, arbitrary slice changes, constant
  reframings, and common-factor removal do not produce a fixed-point-free
  locally nilpotent field by that method. Nonlinear recombination succeeds.
  This is not a counterexample to cancellation.

**The main gap:** construct a useful compatible field or coordinate frame
for every input to the cancellation problem, rather than assume one exists.
The [status page](docs/current-status.md) separates proved implications,
method limitations, and unproved existence claims.

## Where things live

- [Selected proof notes](research/README.md): a short, dependency-aware index.
- [Research ledger](research-ledger.md): dated evidence, checks, corrections,
  and failed approaches. It is a detailed record, not an introduction.
- [Historical front page and recorded command lists](README-history.md):
  the previous long README, preserved in full with its original links.
- [Initial investigation](research-note.md): background and early baselines,
  not the latest research status.

The older `claims.json`, `experiment-manifest.json`, and verification
records are historical snapshots, not current certification. Existing
proof files and checker paths have been preserved. **Saved checkers remain
frozen: do not run, import, compile, or edit them.**

## Scope and provenance

This is AI-assisted research prompted by a question from Xiangrui Luo.
The working interpretation is complex-threefold affine-space cancellation;
confirmation of the original field and dimension is still pending.
Separate AI reviews and symbolic calculations are documented, but do not
establish originality or replace expert review.

The GitHub repository is private. Public release, external outreach,
submission, and public novelty claims require Thomas's explicit approval.
