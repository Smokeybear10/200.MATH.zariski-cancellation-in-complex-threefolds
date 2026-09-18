# Proof and execution audit for the whole-fiber frontier

The [synthesis99](quadratic-whole-fiber-frontier-pass99.md)
integrates the original-volume normal splitting and whole-fiber
equations. General cancellation remains unsolved. All proof
reviews below are separate AI reconstructions, not human review,
formal verification, or historical novelty clearance.

## 1. Volume-normal splitting and its stronger consequences

Root wrote [the eight-equation proof](quadratic-volume-normal-splitting-pass99.md).
Its complete saved read is f003e2, followed by a corrected literal
TeX spacing command. The final readiness SHA is
ff7360eced28f2f863cf668e8f20207e1700e80d67e23228eb284fba64677e73.
Root reread the entire original volume88, collapsed-plane92 and
global-Jacobian91 proofs (b68f24,45eb68,c22519), as well as the
full conormal, weighted, volume-factor and whole-thickening inputs
used during98.

General, Geometry and Jet independently reconstructed the initial
volume sign, constant centered residue, original normal basis and
constant left inverse. Geometry and Jet then gave clean full saved
eight-equation reconstructions, including the all-point transverse
coefficient, strict weighted cubic coefficient and affine column.
Jet explicitly checked N^2a in mS and N^2F in m^2S using the
full kernel and component stability, not a generic coefficient
field. The coefficient g=f-a(c)x is not presumed invariant.

General's final full saved proof and code-only audit is clean,
with both readiness hashes verified in dc8722.

The new proof eliminates the nonconstant zero-normal row sector
only when L(m) is nonzero. It does not turn the remaining
constant data into invariant coordinates or make NF zero.

## 2. Exact nonreduced fiber

Geometry wrote [the seven-equation whole-fiber proof](quadratic-whole-plane-fiber-pass99.md).
Root's full saved reconstruction is f8a24a. General independently
checked the global CM/primary/DVR contraction and the exact
polynomial-extension length argument before saving. Jet's full
saved seven-equation reconstruction is clean, including the actual
G,c presentation and ordinary sigma=0 injectivity over nilpotents.
General's final full saved seven-equation audit is also clean,
with the proof hash verified in 5c8a07.

The essential gates are ell in the whole ideal mB, absence of
embedded primary components, contraction of each primary ideal
from its DVR, and actual generic multiplicity lengths. Removing
any of those gates would not justify the whole-ideal equality.
The actual slice-retraction argument supplies the kernel, while
ordinary evaluation supplies injectivity. No dimension count or
reduced quotient substitutes for that injection.

Root freshly read the complete displayed
[Stacks 0BUS](https://stacks.math.columbia.edu/tag/0BUS)
statement and proof on CM associated primes. This does not
represent a fresh audit of every cited background result. No
new literature recognition or historical novelty result was found
or claimed in99; the bounded source-scope limits of98 remain.

## 3. Earlier99 diagnostics and their current status

The six-equation [plane-normal proof](quadratic-parallel-plane-normal-pass99.md)
has complete saved reconstructions by Root (b5ddf1), General
(76bab1 with canonical orientation read c56359), and Jet.
The exact canonical J^3 identity, its affine conjugation, units
on the simple plane, and the discarded linear ell term all check.

The six-equation
[nonconstant zero-normal compatibility note](quadratic-zero-normal-companion-compatibility-pass99.md)
was reconstructed by Root (32384b), General (76bab1), and Geometry.
The later volume identity excludes its actual hypothesis sector.
Jet added an explicit forward-status paragraph, read by Root in
4d84b6, without changing its equations. Its current SHA is
ce6d8427a2df8c7a89f97932fea1218f06a29bcfc622e04398b80a0d80a16661.
It is retained as a diagnostic, not an existence result or an
additional surviving case.
General read and checked the final status delta in 2b7164.

## 4. Canonical finite check

The [standalone checker](quadratic_volume_normal_checks_pass99.py)
has exactly one method and imports only unittest and SymPy.
Root read the entire saved code (69517e), and Geometry provided
an independent full code-only reconstruction. It verifies formal
weighted coefficients, affine and non-affine specializations,
constant-left-inverse matrix algebra, and both directions of an
intrinsic polynomial coordinate change used for a full-square
countercontrol. No actual original four-coordinate exceptional
action is constructed by this code.

The [canonical capture](verification-pass99-working.json), chunk
3d24bd, began 2026-09-14T18:13:04.897Z and ended 18:13:05.574Z.
One suite/one method passed, exit zero, in 0.670470625 wall seconds
and 0.073 unittest seconds. The input digest before and after was
44f260454d3c4c2e0936a5304cc546794dd12b686b11a336543ff5fb6a36dbc5.
The exact stdout/newline/stderr digest is
2173d15ee4d741adc43f2daa5aea56ddd29a921c0bb5977da8852d6380ed08b8.

Jet's author run passed the same method in 0.039 seconds,
chunk 9eb9f6, wall 0.308369041 seconds. This repeat is not extra
coverage. No new full regression was performed. Historical full75
remains 146 suites/1047 methods; the central registry remains 544
historical claims without integration of later working proofs.

## 5. Integrity and incomplete objective

Pass98 was frozen with six artifacts plus its checkpoint, bringing
the prior record count to 593. General's final independent98 audit
was clean (bcd21a,83f0e4,16e809), including all 781 local links.
The99 continuation revalidated all 593 predecessor records
unchanged (e4ce90 and a43031). It then proved the stronger volume
and whole-fiber results, so this continuation is progress rather
than another status restatement.

The [checkpoint99](checkpoint-pass99-working.json) records final
artifact and execution accounting after integration. Its hashes
are integrity checks, not a proof of the geometric claims. No
later100 scratch work is included among the99 results.

The research skill influenced the complete cited synthesis and
separation of proved conditional statements, failed shortcuts,
finite controls and missing global conclusions. The full goal
is still active. No unrestricted recognition, arbitrary-frame
reduction, human review, formal certificate, novelty clearance,
outreach, posting, submission or automation occurred.

General's full synthesis99, audit99 and latest README/ledger
integration review is clean (a9fd0d,fbdc5e,f156eb). Its read-only
capture audit confirms four synthesis equations, one AST method,
the sole current input hash and the complete output hash, without
rerunning the finite checker. Root's corresponding complete reads
are c3f17d,bbbd01,8ffc67,97f2b6.
