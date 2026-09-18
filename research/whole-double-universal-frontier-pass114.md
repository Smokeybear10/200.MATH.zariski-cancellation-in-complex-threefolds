# The proper whole-double obstruction is excluded

Within the supplied actual nonconical quadratic frame, the proper
second-image whole-double alternative is impossible. The new argument
uses a simple root of an auxiliary cubic and works at every residual
colength, including when both residual generators are singular.
Consequently every fixed closed fiber in that frame is an entire
double line with an actual local cyclic-conic presentation.

This is a conditional local result, not a proof of cancellation. The
working target remains the unconfirmed interpretation of Luo's email:
A[u] isomorphic to C^[4] implies A isomorphic to C^[3]. The literal
emailed A^1 conclusion has a dimensional mismatch for general r.
No field or dimension clarification has been obtained from Luo.

## 1. The coefficient obstruction and its resolution

The actual proper branch supplies a complete regular local surface R
with maximal ideal m, an m-primary ideal J=(a,b), and coefficients

\[
b^2=sh+a^2u+abv,\qquad
B_2\in\mathfrak m(h)+\mathfrak m(a^2)+\mathfrak m(ab)+\mathfrak m^2(b^2),
\qquad P=ah+bB_2\ne0.
\]

The [product-index112 proof](whole-double-product-index-pass112.md)
obtains these conditions from actual finite free degree modules,
divisor determinants and pure residue contraction. The
[ramified113 proof, Sections 2--3](whole-double-ramified-completion-descent-pass113.md)
independently makes P a power of a single prime that remains prime
after base completion. That analytic-prime input is indispensable.

Absorb the last B2 ideal summand using the b-squared relation. This
gives B2=h eta+a(az+bt), with eta,z,t in m. The cubic

\[
F(T)=(T+\eta)(1-T^2u-Tv)+sT^2z+sTt
\]

has a simple root at zero modulo m. Complete local Newton lifting
therefore gives rho in m with F(rho)=0. Set D=1-rho squared u-rho v,
a unit, and L=a-rho b. The
[explicit-cofactor proof114](whole-double-universal-factorization-pass114.md)
constructs H in R and proves P=LH. Its exact denominator-free identity
is checked without substituting an unproved factorization.

The decisive extra step is the joint ideal, not just reducibility.
Modulo L the formula for H is a unit times h. The coefficient
relation also puts b squared in (L,h). Hence

\[
(L,H)=(L,h),\qquad J^2\subseteq(L,H),\qquad
L,H\in\mathfrak m\setminus\{0\}.
\]

Thus (L,H) is m-primary. In the regular local UFD, both factors cannot
be positive powers of the sole prime supporting P. This excludes the
entire actual proper branch.

The [independent cubic-division proof114](whole-double-cubic-division-exclusion-pass114.md)
instead homogenizes F, divides by its lifted linear factor, and obtains
sP=LQ2(a,b). It proves gcd(s,L)=1 before removing s, and uses the unit
F'(rho) to prove the cofactor is a nonunit and J squared lies in the
joint ideal. It remains valid when L is reducible or nonreduced.
These are two reconstructions of one theorem, not two resolved strata.

## 2. Exact consequence for fixed fibers

The [fixed-profile bound97](quadratic-tangent-and-coordinate-frontier-pass97.md),
Sections 1--3, leaves only profiles (2) and (2,1) for a closed fiber
containing a fixed point in this supplied frame. The
[all-normal mixed exclusion111](quadratic-all-normal-mixed-exclusion-pass111.md)
already excludes (2,1), with no nonzero-speed-normal premise.

For a noncollapsed double, the
[cyclic module theorem103](noncollapsed-cyclic-degree-module-pass103.md)
already gives the local conic. For a collapsed whole double,
Section 6 of all-normal111 and the
[second-degree dichotomy111](whole-double-second-degree-dichotomy-pass111.md)
leave the hidden-parameter and proper-image alternatives. The new
theorem removes the latter.

Therefore, over the actual local invariant base R=S_m, there is an
actual U in F2, with r=NU, p=Nr in m and nonzero, and eta=2pU-r squared in m,
such that

\[
A_R=R[U,r]\simeq
R[\mathsf U,\mathsf r]/(\mathsf r^2-2p\mathsf U+\eta),\qquad
I_1=I_2=pR,
\]
\[
F_j=\bigoplus_{2i\le j}R\,U^i
\ \oplus\!\bigoplus_{2i+1\le j}R\,rU^i,\qquad
A_R/\mathfrak mA_R\simeq\mathbb C[U,r]/(r^2).
\]

The parameter is actual over R, not merely a formal function over Rhat.
Its existence follows by excluding the other actual alternative, not
by descending the cubic root rho as a coordinate. This distinction
avoids reintroducing the former completion-descent gap.

## 3. Scope of the advance

| Question | Status after this argument |
| --- | --- |
| Proper second-image whole double in the supplied frame | Excluded for all residual colengths |
| Fixed closed fibers in that frame | Entire double line and actual local cyclic conic |
| First-image scalar p must be a base coordinate | Not proved; intrinsic conics103 allow higher order |
| Closed fibers without fixed points | Not classified by this new argument |
| Patching the local conics into a global polynomial threefold | Open |
| Relative cubic lane and arbitrary original-frame entry | Open |
| Full complex-threefold cancellation | Not solved |
| Human expert review, formal verification and novelty clearance | Not obtained |

No conclusion says all quadratic strata are solved. The fixed-point-free
fibers and global recognition remain distinct obligations. The intrinsic
polynomial examples103 also show why smoothness and a local conic do
not force first-order p.

## 4. Earlier bounded work retained as history

Before the universal cubic was found, this pass produced complete
[smooth-a](whole-double-smooth-a-exclusion-pass114.md),
[smooth-b](whole-double-smooth-second-generator-exclusion-pass114.md),
[square-ideal](whole-double-square-ideal-exclusion-pass114.md), and
[equal-weight initial-form](whole-double-weighted-initial-exclusion-pass114.md)
exclusions. Their arguments remain saved, with their original narrower
scope statements. They are superseded as the active route, and none is
a necessary premise of the universal proof.

In particular the final proof does not require h in m squared, a smooth
generator, h in J squared, coprime initial forms, or any chosen weights.
It uses neither completed-kernel rigidity113 nor formal slice descent.
Exploratory length-four and length-five discussions are not counted as
additional retained theorems or as needed intermediate cases.

## 5. Exact checks and independent reviews

The [canonical capture114](verification-pass114-working.json) records

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.whole_double_universal_factorization_checks_pass114 \
  research.whole_double_newton_checks_pass114 \
  research.whole_double_square_ideal_checks_pass114 \
  research.whole_double_conormal_checks_pass112 \
  research.quadratic_degree_module_checks_pass102 \
  research.quadratic_divisor_filtration_checks_pass107
```

All eight methods in six suites passed: four new methods and four
retained methods. Elapsed time was 3.449506209 seconds; unittest
reported 3.081 seconds. The complete stdout-newline-stderr hash is
bbfe85f190e362412ea7a1062b16b9e46e2816f7d394817449fdb13b980f9290.

The two universal methods check polynomial factor/ideal certificates
and five coefficients of a formal root for singular a,b. The other
new methods retain the earlier smooth-a and Artinian-coefficient
controls, including noncanonical coefficient lifts and a double-root
cofactor. Those finite controls are not additional proof of the
geometric theorem or universal all-order lifting.

Separate AI reviewers read both complete universal proofs, checked
the nonunit and joint-ideal arguments, and rechecked the exact
112--113 dependency interface. The checker imports neither a solver
nor another checker. These reviews and tests are not human expert
review or Lean verification.

All709 frozen records through113 were freshly revalidated unchanged.
The historical full75 run remains146 suites/1047 methods and the
registry544, without a full rerun. The
[checkpoint114](checkpoint-pass114-working.json) records current
artifact hashes and review scope.

## 6. Sources and remaining work

The external algebra inputs are the Stacks Project's
[simple-root Newton/Hensel argument04GM](https://stacks.math.columbia.edu/tag/04GM)
and [regular-local UFD theorem0AG0](https://stacks.math.columbia.edu/tag/0AG0).
Their complete displayed statements and proofs were freshly read;
deeper referenced results were not all reconstructed. The potentially
nonmonic cubic's Newton argument is written directly in both proofs.
The earlier square-ideal route separately used the conormal algebra
references identified in that note.

A current source search also resurfaced arXiv:2512.15590v2. Reading its
introduction and Example 2.6 reconfirmed the incompatibility already
documented in the [retained source audit](global-symmetry-bridge-literature.md),
Section 8: it both describes characteristic-zero cancellation as open
and claims complex counterexamples. It remains excluded as an authority.
No theorem, status conclusion or novelty claim is taken from it.
The Gupta and Dubouloz--Ghosh arXiv abstract/version records were checked,
not their full proofs anew. This was not an exhaustive novelty audit.

The next investigation should audit the lowest missing bridge from
these fixed-fiber conics to global recognition in the supplied frame,
including the fixed-point-free fibers. More special cases of the now
excluded proper branch would not advance that bridge. The relative
cubic lane and arbitrary-frame entry remain explicit, separate routes.

No external contact, posting, submission, paid access, financial action
or new automation was undertaken. The full goal remains active.
