# Working72 proof and verification audit

The conditional result recognizes every original joint-rank-at-most-two
case under the actual two-quadratic coordinate frame and original
polynomial slice. This includes the newly completed terminal quintic.
It does not provide a frame for an arbitrary sliced action or solve
complex-threefold cancellation. The intended field and dimension
remain unconfirmed by the professor.

## Written arguments and separate reviews

| Artifact | Author | Separate full-file AI reconstructions |
| --- | --- | --- |
| [Higher rank-drop bridge](independent-higher-rank-drop-pass72.md), 17 equations | Jet | Root, General, Geometry |
| [Third full-image lemma](quintic-rank-drop-third-image-pass72.md), 8 equations | Geometry | Root, General, Jet |
| [Polynomial clearing](quintic-rank-drop-polynomial-symmetry-pass72.md), 16 equations | Jet | Root, General, Geometry |
| [Fixed-good-base lemma](fixed-good-base-coefficient-pass72.md), 5 equations | Geometry | Root, General, Jet |
| [Terminal quintic recognition](terminal-quintic-recognition-pass72.md), 22 equations | Root | General, Geometry, Jet |
| [Joint-rank-two synthesis](joint-rank-two-frame-closure-pass72.md), 6 equations | Geometry | Root, General, Jet |
| [Five-method checker](quintic_rank_drop_checks_pass72.py) and [scope note](quintic-rank-drop-controls-pass72.md) | Jet | Root and General complete reads; General separate execution |

Author self-review is not counted as independent reconstruction.
These are AI checks of written deductions, not human expert review
or proof-assistant verification. The finite computations have a
separate, strictly narrower scope.

The terminal audits include both values of the normalized acceleration,
the nonzero-speed and zero-speed alternatives, both coefficient-relation
branches, actual polynomial inverses, and the normalized defect signs.
The fixed-base lemma explicitly uses a nonzero second adjoint. Its
coefficient proportionality factor need not be constant. The radial
two-direction endpoint does not require the output partial to be good;
the parallel endpoint instead retains and uses the good fixed-base
partial. The full rational69 argument and exact original-slice gates
were reconstructed before using these endpoints.

The synthesis checks all original dependent cases from71 and the
independent low-flow, constant-top and moving rank-drop cases. It does
not silently identify original defect rank with normalized defect rank.
The independent joint-rank-three extension is separate pass73 work.

## Changes and failed shortcuts retained

The failed direct quartic-to-quintic shear remains a valid negative
calculation: the changed bad output has second adjoint minus the old
defect, not zero. The new fixed-base lemma uses that nonzero defect.
The third full image gives constant normalized acceleration, not
automatically zero original second derivative.

The bridge received a forward-status link after the later quintic
argument was completed. Its earlier failure statements were preserved.
A joined-word transcription in the terminal note was corrected without
changing an identity. The computational harness was extended from four
to five methods to include actual positive and zero-defect controls.

## Source applicability

The linear-invariant input remains Dasgupta--Gupta, Theorem3.1(i),
over a characteristic-zero field, as scoped in the
[pass71 source audit](nice-linear-invariant-source-pass71.md).
Only the nice symmetry is extended over C(w). The original action
need not fix w. No fresh access to the full original Wang proof is
claimed. The regular-original-kernel and actual-plane endpoints retain
their separately stated source hypotheses from rational69.

General's [coordinate-local-slice comparison](good-coordinate-local-slice-scope-pass72.md)
records three selected primary-source limitations. Root read the
complete comparison. The comparison is not a fresh root reconstruction
of all those historical proofs and is not used as a new recognition
theorem. In particular, Daigle's actual three-variable theorem was not
applied to the four-variable ring or to its unknown kernel.

## Actual bounded computation

The canonical [capture](verification-pass72-working.json) ran:

~~~sh
/opt/anaconda3/bin/python research/quintic_rank_drop_checks_pass72.py
~~~

The five methods passed, exit zero, from 2026-09-14T03:57:03.415Z
through 2026-09-14T03:57:04.038Z: 0.239 unittest seconds and
0.623 wall seconds. Complete stdout followed by complete stderr has
SHA-256 b7bd52d7856101919dba89eb0bcd4ed3fbbddf75c87eb3d9ca7c61ae0b2c4ab6.
The capture records the exact checker hash.

Jet's completed five-method author run passed in 0.234 seconds;
General's independent run passed in 0.239 seconds. Root's intervening
status-check run also passed in 0.239 seconds. Earlier four-method
development runs passed in 0.149 and 0.203 seconds. These executions
are not additional methods or suites.

The full-image and flow tables are formal algebraic controls, not
realizations of the terminal frame. Actual polynomial inverse maps
and the positive fixed-base LND are checked directly. The zero-defect
control disproves deletion of that lemma's nonvanishing premise.
None of these computations certifies the universal written theorem
or the external classification inputs.

No fresh full regression was run for72. The last full regression
remains the captured69 result, 136 suites and 1021 methods.
The current one-suite addition is not silently incorporated into
a fresh full-run total.

## Preservation and remaining scope

The [working72 checkpoint](checkpoint-pass72-working.json) records
file integrity separately from mathematics. Frozen71 and earlier
files are preserved. The central registry and manifest remain at
their full60 integrated state with 544 claims.

This packet excludes subsequent73 drafts. At its boundary the
independent joint-rank-three moving quartic and quintic sectors and
universal-frame existence remain unresolved. There is no unrestricted
solution, historical novelty verdict, human review, Lean certificate,
external contact, public posting or submission.
