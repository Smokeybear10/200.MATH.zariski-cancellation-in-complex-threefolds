# Recognition of the birational projected plane-line sector

Working scoped synthesis, conditional on the retained recognition
dependencies below: under EVERY actual hypothesis of264, suppose
\(m=k_s\ne0\), the full equation of the projected plane curve
\(L[\sigma,\theta]\) has degree one, and its function-field projection
has degree one. Then
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
In the variable-coupling part there is a stronger necessary conclusion:
\[
\boxed{m\notin\mathbb C\quad\Longrightarrow\quad
\sigma\in L,\qquad m_s=m_{tt}=0,\qquad
m=at+d\quad(a\in\mathbb C^*,\ d\in\mathbb C).}
\tag{2}
\]
Here \(\sigma\in L\) means constant in the intrinsic line parameter.
It does NOT mean that sigma is a complex constant.

The new synthesis closes the nonconstant-sigma alternatives by the
last exclusion491. The recognition endpoints473 and478 are retained
working proofs, not newly reconstructed in all their ancestors here.
This is not a proof that an arbitrary cancellation candidate enters
the chart or has a projected plane line. The general cancellation
problem remains unsolved.

## 1. Full actual hypotheses and the geometric line condition

Retain the entire actual setup of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), not
just its formal coefficient equations. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad X=a_0u+x_0,\quad a_0\ne0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\qquad Nv=1,\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w_{\rm int}),\\
O=L[v]=L[y,z,w_{\rm int}]=L[y,\sigma,\theta].
\end{gathered}
\tag{3}
\]
The final return uses the stipulated nonzero coupling. The original
slice u is not replaced by X/a0, and a0 is not assumed an original
ring unit. All original localizations and returns remain required.
The commuting coefficient partials have joint constants exactly C.

The literal rows and first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w_{\rm int}+\theta X+sX^2,\\
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\\
mw_{\rm int}&=\ell-(2\sigma+k_t)y-F(\sigma,\theta),\\
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
J_{t,s,v}(X)&=-a_0^4\in L^*.
\end{aligned}
\tag{4}
\]
The genuine cubic and quartic levels, and evaluated gradient-minor
units of [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
are retained consequences of this actual setup. They are not
replaced by arbitrary cubic or quartic polynomials.

Precisely, the additional line assumptions in this note say that
\(C_{\rm proj}=L[\sigma,\theta]\) has transcendence degree one,
its prime equation in the specified two plane variables has total
degree one, and
\[
[L(v):\operatorname{Frac}C_{\rm proj}]=1.
\tag{5}
\]
A nonlinear plane curve can be abstractly isomorphic to an affine
line. That does not make its equation degree one and does not put
it within this theorem. Birationality alone also does not supply
the polynomial return used below.

By the complete retained
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md),
these precise assumptions imply
\[
C_{\rm proj}=O,
\qquad \deg_v y,\deg_v\sigma,\deg_v\theta\le1.
\tag{6}
\]
Its proof uses the original derivation to establish
\(L[\mathcal B]=L[X,v]\), then all-X specialization, rather than
assuming generation for an arbitrary formal map. Neither325 nor
the case split below requires a factorization of the genuine cubic
surface. No extra irreducibility assumption is added here.

## 2. Constant coupling and constant intrinsic sigma

If \(m\in\mathbb C^*\), the retained synthesis
[473](principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md)
recognizes A without any projected-line hypothesis or longitudinal
derivative restriction. This proves (1) in that alternative.

Suppose henceforth \(m\notin\mathbb C\). If \(\sigma\in L\),
then theta is nonconstant by (5), and the retained theorem
[478](principal-paraboloid-constant-sigma-variable-coupling-recognition-pass478-working.md)
gives all of (1),(2). Its actual-coordinate endpoint, retained
from475, is essential. A coordinate over the field C(X) is not
being promoted to an original complex polynomial coordinate.

It remains only to exclude \(\sigma\notin L\) in this
variable-coupling line sector. Equation (6) then licenses
\[
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\qquad
y=\lambda P+r_{\rm old},\quad\theta=\mu P+h,\quad
w_{\rm int}=\omega P^2+bP+c,
\tag{7}
\]
where every displayed coefficient is in L. The quadratic form of
w follows from the second potential in (4). The scalar becomes
\(J_{t,s,P}=-a_0^4/\rho\); the nonzero original speed rho is
not normalized away by an ambient coordinate assertion.

## 3. Exhaustive exclusion of nonconstant intrinsic sigma

All sources in this section retain the full actual hypotheses
above, including the scalar, both returns and original global
slice. The initial exclusions are applied successively:

1. If \(\lambda\in\mathbb C\),
   [483](principal-paraboloid-constant-linear-slope-exclusion-pass483-working.md)
   excludes the chart. Its complex-omega subcase retains477.
2. For the remaining \(\lambda\notin\mathbb C\), if
   \(\omega\in\mathbb C\),
   [479](principal-paraboloid-complex-quadratic-slope-two-quasi-exclusion-pass479-working.md)
   excludes the chart, using its complete480 input and both
   alternatives of the cited two-quasi theorem.
3. For the remaining noncomplex slopes, set
   \(\mathcal D=\partial_t+\mu\partial_s\) and
   \(\beta=\mathcal Dm\). If \(\beta=0\),
   [481](principal-paraboloid-variable-coupling-zero-direction-exclusion-pass481-working.md)
   excludes the chart, including its zero moving-intercept
   derivative alternative.

It therefore suffices to assume
\[
\lambda,\omega\notin\mathbb C,\qquad\beta\ne0.
\tag{8}
\]
Retain the full high system of
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
With
\[
B_2=\frac12(m_{tt}+2\mu m_{ts}+\mu^2m_{ss})+m_s\omega,
\tag{9}
\]
the zero-safe contact reduction
[482](principal-paraboloid-nonzero-direction-contact-reduction-pass482-working.md)
proves \(B_2\ne0\). Thus its existing coefficient elements
\[
q=B_2/\beta,\quad a_c=1/q,\quad
\tau=t+a_c,\quad
\mathfrak v=\mu+2a_c\omega,\quad
\mathfrak b=s+a_c\mu+a_c^2\omega
\tag{10}
\]
are defined and satisfy
\[
d\mathfrak b=\mathfrak v\,d\tau.
\tag{11}
\]
This notation a_c is unrelated to the constant a in (2).
No parameter change is licensed merely by defining these elements.

The remaining field alternatives are exactly these:

| Contact parameter | Directional derivative | Complete exclusion |
| --- | --- | --- |
| \(\tau\in\mathbb C\) | \(\mathcal D\omega=0\) | 487 |
| \(\tau\in\mathbb C\) | \(\mathcal D\omega\ne0\) | 486 followed by488 |
| \(\tau\notin\mathbb C\) | \(\mathcal D\tau=0\) | 484 followed by485 |
| \(\tau\notin\mathbb C\) | \(\mathcal D\tau\ne0\) | 489 followed by490 and491 |

For the first two rows, (11) makes \(\mathfrak b\) complex.
The actual constant normalization in
[486](principal-paraboloid-constant-contact-transverse-reduction-pass486-working.md)
removes these two constants. It does not assume that
\(\mathfrak v\) is complex. The exact invariant-omega proof
[487](principal-paraboloid-constant-contact-invariant-omega-exclusion-pass487-working.md)
excludes the first row with the full scalar. The quadratic
coefficient reduction486 and full lower-scalar exclusion
[488](principal-paraboloid-transverse-contact-scalar-exclusion-pass488-working.md)
exclude the second row, including both zero and nonzero values of
its residual complex constant.

For the third row, the exact finite-field reduction
[484](principal-paraboloid-invariant-contact-parameter-reduction-pass484-working.md)
and full residual determinant identity
[485](principal-paraboloid-invariant-contact-scalar-exclusion-pass485-working.md)
exclude the entire family. The zero moving-intercept derivative
and zero effective-coupling derivative are explicit cases, not
silently divided factors.

For the last row, the existing-root reduction
[489](principal-paraboloid-transverse-contact-square-root-reduction-pass489-working.md)
proves the necessary square-root family. The full high scalar in
[490](principal-paraboloid-transverse-contact-universal-normalization-pass490-working.md)
then forces h0=0 and a nonzero constant scale. Its explicit actual
polynomial map and inverse normalize to
\[
s=r^2/2,\quad k=tr,\quad
\lambda=w/2,\quad\omega=w^2/2,\quad\mu=-rw,
\qquad r,w,\mathcal Dw\ne0.
\tag{12}
\]
The two roots in (12) were already elements of L. The new scalar
integrations are repeated in the new actual frame with NEW
constants, not copied unchanged from the old frame.

Finally,
[491](principal-paraboloid-square-root-contact-scalar-exclusion-pass491-working.md)
excludes the whole normalized family. In its separating basis
\((w,v_*=r+tw)\), let
\(\jmath=\alpha/4+b_c/(2v_*^2)\), with
\(\alpha,b_c\in\mathbb C\). If jmath is zero, the complete
Z differential has the nonconstant intrinsic factor
\(\xi+v_*/2\), contradicting the scalar unit. If jmath is
nonzero, two full lower coefficients give
\[
(1+4\jmath')w+4f'=0,\qquad f\in\ker_L\partial_w.
\tag{13}
\]
Primes denote the exact v* derivative. Here w is transcendental
over that exact finite one-variable field. Thus \(1+4\jmath'=0\), which says
\(v_*^3=4b_c\) and contradicts the nonzero exact v* derivative.
The actual scalar is
\(-r a_0^4/(\rho\mathcal Dw)\ne0\), not an assumed complex
constant. Its parameter-dependent constant term is never set
to zero. This closes the fourth row.

The table is exhaustive: either tau is complex or it is not;
within each alternative the indicated derivative is zero or it
is not. In the final row489 proves \(\mathcal D\omega\ne0\)
rather than adding it as a further unexamined assumption.
Together with the preceding three successive splits, no
nonconstant-sigma case remains. This proves (2), and Section2
then proves (1).

## 4. Retained endpoints and verification boundary

For constant coupling,473 retains422/457 and their specified
recognition ancestors. For variable coupling and constant sigma,
478 retains475's actual-coordinate endpoint. Those endpoints
ultimately use published invariant-coordinate and regular-kernel
theorems with their actual hypotheses. This synthesis does not
recursively re-certify those ancestors or replace them with
coefficient-field parametrizations.

The same473 also retains recognition of m=0 through268/294.
Consequently the zero-coupling chart is already recognized
separately. No expression requiring the nonzero-coupling
three-generator projection is extended to m=0 without proof.

The complete current264,325,473,478,482,490 and491 were read
for this assembly. Earlier full source reviews of the exclusions
are retained, with their held hashes revalidated before use.
490 and491 have separate complete AI source reviews and fresh
unsaved whole-determinant reconstructions. The exact evidence
and the separate review of this synthesis belong in the ledger.
This table is a written logical exhaustion, not a finite-grid
test and not proof-assistant certification.

Nonlinear projected plane curves, other initial kernels and time
profiles, and arbitrary entry into an appropriate actual frame
remain unresolved. The intended field and dimension in Luo's
email remain unconfirmed. No historical novelty, human expert
review, publication readiness or unrestricted cancellation is
claimed. All saved checkers remain frozen. No external contact,
public submission, git mutation or automation occurs in this note.
