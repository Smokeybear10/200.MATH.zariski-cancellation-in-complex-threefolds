# Recognition for the full square-root initial kernel

Status: working restricted theorem synthesis. The supplied exact1122
configuration with entire initial kernel \(Z^2-X^3Y\) is recognized
by composing the results listed below. The newest normalization and
two exclusions have independent AI source reconstructions and passing
finite algebra checks. Their verification packets are recorded separately.
This is not a solution of unrestricted cancellation.

## 1. Restricted theorem and the coordinate-entry boundary

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\mathcal A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2).
\end{gathered}
\tag{1}
\]
Write \(a=EX,\ b=EY,\ e=E^2Z/2,\ h=E^2W/2\).
For an independent symbol \(\tau\), require that the entire initial
kernel is
\[
\ker\!\left(
\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
\longrightarrow\mathcal A[\tau],\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\tau,b\tau,e\tau^2,h\tau^2)
\right)
=(\mathsf Z^2-\mathsf X^3\mathsf Y).
\tag{2}
\]
Then the composed restricted conclusion is
\[
\mathcal A\simeq\mathbb C^{[3]}.
\tag{3}
\]
The original entries in (1) are actual polynomial coordinates.
Condition (2) is stronger than a single relation among leading
coefficients. No result here puts an arbitrary sliced action into
(1)--(2). That missing coordinate-entry result alone prevents using
(3) to claim general complex-threefold cancellation.

## 2. Exhaustion of the supplied configuration

The [universal actual chart184](weight-four-universal-chart-potentials-pass184-working.md)
constructs the selected nonzero LND \(N\), its exact coefficient field
\(L\), the ratios \(t,\rho,q\), and the projected entries \(y,z,w\).
Here \(q^2=t\), the coefficient-constant field \(K\) is finite over
\(\mathbb C(q)\), and the actual projected field return is
\[
\mathbb C(y,z,w)=L(v).
\tag{4}
\]
Its scalar Jacobian is calibrated using the selected original partial,
not imposed as a sufficient formal inverse criterion.

The [zero-R recognition195](weight-four-double-root-zero-r-coordinate-recognition-pass195-working.md)
treats \(R=k_\rho=0\) by an actual invariant-coordinate construction.
Together with the published invariant-coordinate endpoint used there,
it gives (3) in that case.

For \(R\ne0\), the
[double-cover reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
excludes constant projection, the degenerate quartic top, and the
pure-quartic branch. The only remaining alternatives are the quadratic
graph and quadratic projection, with all their nonzero coefficient
gates. The [complete two-gate classification195](weight-four-square-root-two-gate-classification-pass195-working.md)
then restricts \(f=1/R\) to
\[
f=\beta q,\qquad f=\beta/q,\qquad
f=at+bq\quad(a,b\ne0),
\tag{5}
\]
where all displayed constants are complex and the indicated
\(\beta\) is nonzero. This classification is valid inside the exact
finite field; it is not a rational-function search.

Each entire remaining family is now accounted for:

- For \(f=\beta q\), the actual
  [normalization196](weight-four-square-root-monomial-actual-normalization-pass196-working.md)
  and [graph exclusion196](weight-four-normalized-square-root-graph-obstruction-pass196-working.md)
  reduce to the projection branch. Its
  [polynomial inverse197](weight-four-normalized-square-root-quadratic-projection-recognition-pass197-working.md)
  exhibits \(B=\mathbb C[X,y,z,q]\), with \(y,z,q\) actual invariants.
  The global slice forces \(EX\) to be a nonzero complex constant,
  so \(\mathcal A=\mathbb C[y,z,q]\).

- For \(f=\beta/q\), the
  [reciprocal synthesis198](weight-four-reciprocal-square-root-frontier-synthesis-pass198-working.md)
  composes its actual normalization with both exclusions.
  The graph violates a quadratic field degree, and independently an
  original-ring square obstruction. The projection violates a cubic
  field degree. Hence this family cannot occur.

- For \(f=at+bq\), \(ab\ne0\), the actual
  [normalization199](weight-four-nonmonomial-square-root-actual-normalization-pass199-working.md)
  first scales to \(f=q(q+1)\) and then removes every lower term in
  \(k,n\) using polynomial maps with explicit polynomial inverses.
  The selected fields, full initial kernel and generic alternatives
  are preserved. The [graph proof200](weight-four-normalized-nonmonomial-graph-obstruction-pass200-working.md)
  contradicts a cubic degree. The
  [projection proof200](weight-four-nonmonomial-quadratic-field-obstruction-pass200-working.md)
  contradicts an irreducible quartic over the actual projected field.
  Thus this family also cannot occur.

There are no additional families in (5) or a dropped boundary
\(a=0\): that boundary is exactly the first family.
The zero-R case was treated separately rather than divided away.
This completes the composed restricted proof of (3).

## 3. What the newest exclusions actually use

After normalization199, put
\[
R=\frac1{q(q+1)},\qquad
h=\frac y{2q}-\frac{\rho}{q(q+1)(3q-1)},\qquad
\xi=R(\vartheta-P(y)),\qquad g=\ell_0/R .
\]
Both branches have
\[
z=\xi-\frac32h^2,\qquad
w=(h+y)z+\frac12h^3+g.
\tag{6}
\]
In the graph, the eliminant forces \(g\) complex. Actual field return
would then make the cubic \(h^3+2zh-2(w-yz-g)\) have a rational root
over \(\mathbb C(y,z,w)\), although it is irreducible.

In the projection, scalarity forces
\(g=\alpha q+\beta/(3q-1)+\gamma\).
Its remaining coefficients imply
\[
3h^4+12zh^2-\{24(w-yz-\gamma)+8\alpha\}h
  +24\alpha y-4z^2-4\delta=0.
\tag{7}
\]
For all allowed constants this is irreducible over
\(\mathbb C(y,z,w)\), yet the actual \(h\) belongs to that very field.
Neither argument assumes \(K=\mathbb C(q)\), uses a scalar determinant
as an inverse, or calls a generic parameter an original coordinate.

## 4. Verification status and the genuine remaining target

The written sources distinguish finite algebra controls from the
field and geometric proofs. The standalone
[normalization controls199](weight_four_nonmonomial_normalization_controls_pass199.py)
passed three methods in 0.924 seconds, and the
[obstruction controls200](weight_four_nonmonomial_obstruction_controls_pass200.py)
passed four methods in 0.922 seconds. Each suite ran once and completed
through its original execution handle with exit status zero. Their
source reviews and canonical captures are recorded separately.
Passing them cannot establish actual field return,
finite-field solution completeness, or irreducibility on its own.

The [bounded primary-literature audit199](time-degree-1122-primary-literature-audit-pass199-working.md)
checks only selected statements with nearby hypotheses. It does not
establish novelty or replace an expert review.
The restricted theorem currently has AI source reconstructions,
not human certification or proof-assistant verification.

Still open in this program are the nonzero-R branch for the different
initial kernel \(Z^2-X^2Y(X-Y)\), other initial forms and ranks,
height-two initial kernels, higher time profiles, and arbitrary
coordinate entry. In particular the goal
\(\mathcal A[u]\simeq\mathbb C^{[4]}\Rightarrow
\mathcal A\simeq\mathbb C^{[3]}\) remains active and unsolved.
No external contact, posting, submission or novelty claim is authorized
or has been made. All198 and earlier frozen sources are preserved.
