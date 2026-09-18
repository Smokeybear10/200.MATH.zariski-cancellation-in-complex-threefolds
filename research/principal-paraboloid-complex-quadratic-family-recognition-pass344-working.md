# Recognition of the supplied complex-quadratic coefficient family

Working theorem, with the proof dependencies stated below: the full
actual principal chart264 is recognized whenever its first two
coefficient potentials satisfy
\[
k_s=m_0\in\mathbb C^*,\qquad k_{ttt}=0,\qquad
n_{ss}=n_{ts}=n_{ttt}=0.
\tag{1}
\]
There is no additional hypothesis on the remaining potential ell and
no restriction on334's quadratic residual. Thus the entire specified
coefficient family, not just its zero-residual part, has original
kernel C^[3]. This does not prove that arbitrary candidates satisfy(1).

A separate consequence applies to a broader one-variable first
potential: under the same full chart, k=s and n_s=0 force ell_ss=0.
That necessity does not recognize every such nonlinear first potential.

## 1. Full actual entry is retained

The input is the actual polynomial ring and its globally sliced
derivation from[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\quad\text{is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad [L:\mathbb C(t,s)]<\infty,\\
Nv=1,\quad K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
L[y,z,w]=L[y,\sigma,\theta]=L[v],\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
All coefficient partials are the exact commuting extensions to L.
In particular the potentials in(1) are those of this actual chart,
not arbitrary polynomial functions on a separately chosen field.
Both ring returns and the particular scalar calibration remain part
of every invocation below.

## 2. Every normalized complex-quadratic first potential is covered

First suppose k=s and n=g t^2 with g in C. If g=0, the retained
working theorem[330](principal-paraboloid-normalized-potential-family-recognition-pass330-working.md)
applies, including its explicit298 and mandatory-corrected301 inputs.
The withdrawn auxiliary argument in the original301 Section3 is not
used. Hence consider g nonzero.

If ell_s=0, both n and ell belong to the exact one-variable coefficient
field, so[337](principal-paraboloid-two-one-variable-potentials-recognition-pass337-working.md)
applies. If ell_s and ell_ss are both nonzero,
[340](principal-paraboloid-quadratic-first-nonlinear-second-exclusion-pass340-working.md)
excludes the case by the complete calibrated determinant.

In the remaining case ell_s nonzero and ell_ss=0, the fully retained
reduction[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md)
gives, with r=ell,
\[
s=cr+d(t),\quad \mathcal L=b(t)r+e(t),\quad c\in\mathbb C^*,
\qquad gb^2-\frac{d''}{2}b-(1+gc)^2=0.
\tag{3}
\]
Here b,d,e initially belong to the exact finite field F over C(t),
not necessarily C(t). For b nonzero put
\[
\kappa=1+gc,\quad h=\kappa/b,\quad
\rho=hd'-b'r-e',\quad U=x-h\sigma,\quad x=y+gt.
\tag{4}
\]
The selected plane level is -bU^2+d'U+rho sigma=q in L.
The exhaustive remaining cases are as follows.

| Actual coefficient branch | Working endpoint |
| --- | --- |
| b=0 |339: a literal shift-zero partial or an actual three-good reframe |
| b nonzero, rho nonzero, kappa nonzero |341: explicit polynomial inverse gives B=C[X,t,r,V], A=C[t,r,V] |
| b nonzero, rho nonzero, kappa=0 |341: an actual cubic shear gives profile1122 or three-good |
| b nonzero, rho=0, g+h^2 nonzero |342: a literal polynomial LND preserves A and has an actual E-stable polynomial three-ring |
| b nonzero, rho=0, g+h^2=0 |342: a nonsquare quadratic discriminant contradicts K=C(y,z,w) |

The sources are
[339](principal-quadratic-first-zero-plane-slope-recognition-pass339-working.md),
[341](principal-quadratic-first-genuine-conic-inverse-pass341-working.md), and
[342](principal-quadratic-first-selected-line-recognition-pass342-working.md).
In the rho=0 cases, b is proved complex before h is used as a constant.
The kappa=0 selected line belongs to the nonresonant row, so there is
no lost zero parameter. All divisions in these sources have explicit
nonzero hypotheses. These alternatives exhaust(3),(4).

Consequently, subject to these retained working proofs,
\[
\boxed{\text{Under(2),}\quad k=s,\quad n=g t^2,\quad g\in\mathbb C
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{5}
\]
The actual constant translations Y*=Y+f1/2, Z*=Z-f0 also include
n=g t^2+f1 t+f0 with complex f1,f0, as established in333.
No surface-factorization hypothesis or rationality of L was imposed.

## 3. Transport completes the full coefficient family(1)

The exact integration and actual polynomial map of
[334](principal-paraboloid-complex-quadratic-normalization-composition-pass334-working.md)
show that(1) is equivalent to
\[
k=m_0s+\frac{\gamma}{2}t^2+bt+d,\qquad
n=(B_0+\gamma/2)k+Dt^2+A_1t+C_1,
\tag{6}
\]
where every displayed coefficient is complex and m0 is nonzero.
The scalar b here is not the plane coefficient of Section2.
334 supplies the actual map
\[
X_*=X+B_0,\quad Y_*=Y+A_1/2,\quad Z_*=Z-C_1,\quad
W_*=m_0W+(\gamma/2+2B_0)Z+bY+dX^2.
\tag{7}
\]
Its inverse divides only by m0. It retains every actual hypothesis(2),
including the full initial ideal, selected N, both returns, and the
calibrated determinant. Its exact coefficient data are
\[
t_*=t,\qquad s_*=k+2B_0t^2,\qquad k_*=s_*,\qquad
n_*=(D-B_0^2)t^2.
\tag{8}
\]
The second potential is transported completely in334; its form or
derivatives need not be constrained, because(5) now allows arbitrary
ell*. Apply(5) with g=D-B0^2, whether this number vanishes or not.
This proves the working conclusion announced in(1).

Equivalently, this family consists of k,n that are complex linear
combinations of 1,t,t^2,s, with the s-coefficient of k nonzero.
There are no ts or s^2 terms in this description. It does not include
arbitrary quadratic polynomials in two variables or arbitrary functions
in L. Neither(1) nor an ability to reach it is proved for a general
principal chart, much less for every globally sliced four-ring.

## 4. A broader necessary condition for one-variable first potentials

Now retain(2), assume k=s and n_s=0, and allow n=f in
F=ker_L(partial_s) to be arbitrary. Put g=f''/2 in F.
We prove
\[
\boxed{k=s,\quad n_s=0\quad\Longrightarrow\quad\ell_{ss}=0.}
\tag{9}
\]
If ell_s=0, this follows by differentiation. Suppose ell_s nonzero
and, for a contradiction, ell_ss nonzero. In333's coefficient variables
r=ell and s=H(t,r), this says H_r and H_rr are nonzero.

If g=0, exact constants give f=f1 t+f0 with complex f1,f0. The
actual translations specified after(5) put n*=0 without changing ell.
330's necessary ell_ss=0 contradicts the assumed nonzero derivative.

If g is nonzero,333's quartic-top argument forces
\[
x=\alpha\sigma+\beta,\qquad \alpha^2=-g,\quad
\alpha\in\mathbb F^*,\quad\beta\in L,\qquad L[\sigma]=L[v].
\tag{10}
\]
Its complete formal primitive is
\[
\begin{aligned}
\Phi(U,P)={}&\frac{H_{rr}}2(U^2+gP^2)^2
 +H_{tr}(U^2+gP^2)P+\frac{H_{tt}}2P^2\\
&+2(1+gH_r)UP+H_tU+\frac{H_rg'}3P^3
 -\mathcal L_r(U^2+gP^2)-\mathcal L_tP.
\end{aligned}
\tag{11}
\]
The value at(x,sigma) belongs to L. After substituting U=alpha P+beta,
the expression U^2+gP^2 is 2alpha beta P+beta^2. Every term in(11)
then has P-degree at most two except H_r g' P^3/3. Because sigma is
transcendental over L, the cubic coefficient must vanish. Hence g'=0,
and exact constants give g in C* and
f=g t^2+f1 t+f0 with complex f1,f0.

Actual constant translations again remove only the affine terms.
The normalized chart now satisfies every hypothesis of340, whose
full determinant contradiction excludes it. This proves(9).
No differentiation after formal substitution or moving-root derivative
was used in the cubic-coefficient argument.

## 5. Remaining obligations and verification limits

The coefficient-family theorem(1) is an exhaustive composition within
its stated inputs. Its main remaining inherited recognition inputs
include156 and257 in339/341, and298 plus mandatory-corrected301 through
330. The literal three-ring branches use the precise published
three-variable theorem and regular-kernel theorem linked in337,339,342.
The explicit inverse in341's nonzero-kappa case does not use those
recognition endpoints. This synthesis does not recursively certify
every retained proof or claim historical novelty.

The broader necessity(9) leaves, for general nonlinear f, the branch
ell_s nonzero with H=c(t)r+d(t), where c may still vary in the finite
coefficient field. The argument making c complex in333 explicitly
uses constant g, so it is not silently reused here. The one-variable
pair branch ell_s=0 is already337. General k,n and arbitrary-chart
entry also remain open.

All direct sources264,330,332--334,337,339--342 were read in full
for this synthesis. Separate source-review and finite-check evidence
are recorded in the ledger. The finite controls verify identities and
specific inverse formulas, not all field arguments or retained global
recognition theorems. No human expert review, Lean verification,
publication, external contact, or unrestricted cancellation solution
is asserted. The interpretation of the professor's original question
as complex three-dimensional cancellation remains unconfirmed.
