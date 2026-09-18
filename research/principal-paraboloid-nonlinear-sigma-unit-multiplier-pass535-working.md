# A denominator-free unit multiplier for nonconstant intrinsic sigma

Working conditional lemma: in the FULL actual principal chart264
with \(m=k_s\ne0\), assume only that sigma is nonconstant in
the original intrinsic line parameter v. Put \(\beta=\sigma_v\).
The complete scalar identities imply polynomial equations
\[
\boxed{\mathcal A_\beta=\kappa_0 H_V^{\rm ev},\qquad
       \mathcal B_\beta=-\kappa_0 H_U^{\rm ev},\qquad
       \kappa_0\in L^*.}
\tag{1}
\]
Their explicit left sides are given below. They have no
denominator involving beta and remain valid at every critical
point of sigma.

This extends the unit-multiplier mechanism of494 beyond affine
sigma. The proof does NOT assume that the pair of evaluated
gradient components \((H_U,H_V)\) is coprime. That assumption
can fail at a critical point. Instead the full primitive tangent,
the full gradient-minor unit ideal, and an exact constant-scalar
certificate force the multiplier to lie in \(L^*\).

This is a necessary identity, not exclusion of nonlinear sigma,
a projected-plane normality assertion, an actual normalization,
or an entry theorem for arbitrary cancellation data.

## 1. Full actual hypotheses, original parameter and scalar

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the genuine fourth potential and unit ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A\in\operatorname{LND}(A),
\qquad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad
O=L[A]=L[v],\qquad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v],\\
m=k_s\ne0,\qquad O=L[y,\sigma,\theta],\qquad
\sigma\notin L.
\end{gathered}
\tag{2}
\]
The intercept \(z_{\rm int}\) is the literal original
Z-intercept, not its difference with \(2ty\). Both returns,
the original global slice, the selected literal partial and
the entire initial-kernel hypothesis remain required.

All coefficient partials are the exact commuting extensions
from \(\mathbb C(t,s)\) to L, extended to fix the original v.
No rationality of L is assumed. In particular this note does
not replace v by sigma as a polynomial coordinate. We have
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+n
                            +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-F(\sigma,\theta),\\
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
J(X)&=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
                      =-a_0^4\in L^*.
\end{aligned}
\tag{3}
\]
The coefficient field and the speed \(Nv=1\) are those of264.
The scalar may depend on t,s, but not on X or v.

The genuine formal polynomials \(H,Q\in L[U,P,V]\) from296
satisfy
\[
H(y,\sigma,\theta)=h_0,\qquad
Q(y,\sigma,\theta)=q_0,\qquad h_0,q_0\in L.
\tag{4}
\]
Formal U,P,V derivatives are always taken BEFORE evaluation.
Write
\[
f=H_U^{\rm ev},\qquad j=H_P^{\rm ev},\qquad g=H_V^{\rm ev},
\qquad \beta=\sigma_v\ne0.
\tag{5}
\]
Beta is a nonzero polynomial, not necessarily a unit of O.
The evaluated full H-gradient and the three evaluated minors
of the H,Q gradients generate the unit ideal of O, by296.

## 2. The full cross-gradient is a primitive tangent

The two genuine levels give
\[
\mathcal T:=fy_v+j\beta+g\theta_v=0,\qquad
Q_U^{\rm ev}y_v+Q_P^{\rm ev}\beta+Q_V^{\rm ev}\theta_v=0.
\tag{6}
\]
The vector \((y_v,\beta,\theta_v)\) is primitive in \(O^3\).
Indeed the whole return in (2) supplies a polynomial
\(\Psi(U,P,V)\in L[U,P,V]\) with
\(\Psi(y,\sigma,\theta)=v\). Differentiating at fixed L gives
\[
\Psi_U^{\rm ev}y_v+\Psi_P^{\rm ev}\beta+
                          \Psi_V^{\rm ev}\theta_v=1.
\tag{7}
\]
This assertion uses the three-generator polynomial return,
not projected-plane normality or a rational inverse alone.

Let \(M_{UP},M_{UV},M_{PV}\) be the evaluated gradient
minors in the formal variable order U,P,V. Over \(L(v)\)
the gradients are independent, since their minors generate O.
Their common nullspace is one-dimensional. Equations (6),(7)
therefore give a nonzero rational multiplier \(\tau\) with
\[
(M_{PV},-M_{UV},M_{UP})
                  =\tau(y_v,\beta,\theta_v).
\tag{8}
\]
Taking the linear combination prescribed by (7) shows
\(\tau\in O\). Since the three minors generate O, (8) then
forces \(\tau\) to be a polynomial unit. Thus
\[
\boxed{\tau\in L^*,\qquad
\mathcal W:=fQ_V^{\rm ev}-gQ_U^{\rm ev}
                         =-\tau\beta.}
\tag{9}
\]
The sign is fixed by the displayed cross-product order.
In contrast to the affine-sigma setting, \(\mathcal W\)
need NOT be a unit of O. Its exact polynomial factor is beta.
Neither (8) nor (9) requires \(f,g\) to be coprime.

## 3. Complete scalar and corrected-gradient expressions

For evaluated coefficient polynomials define
\[
\nu=\frac{F_V(\sigma,\theta)}m,\qquad
D=\frac{2\sigma+k_t}{m},\qquad
B_f=\frac{2y+F_P(\sigma,\theta)}m.
\tag{10}
\]
The notation \(B_f\) distinguishes this polynomial from both
the ambient ring and the derivative beta in (5).
Result296 gives \(J(X)=J_0+XJ_1+X^2J_2\), with
\(J_2=\mathcal T\), \(J_1=0\), and \(J_0=-a_0^4\).
Its complete linear coefficient is
\[
\begin{aligned}
J_1={}&f\{(\sigma_t+\theta_s+\nu)y_v
                         -y_t\beta-y_s\theta_v\}\\
 &+j\{y_v+(\theta_s+\nu)\beta-\sigma_s\theta_v\}\\
 &+g\{\sigma_t\theta_v-\beta\theta_t
                         -B_f\beta-Dy_v\}.
\end{aligned}
\tag{11}
\]
For the complete constant coefficient, put
\(\Omega=\det(\partial(y,\sigma,\theta)/\partial(t,s,v))\)
and
\[
\begin{aligned}
K_U&=\Omega+(B_fy_s-\nu y_t)\beta+
                              (\nu\sigma_t-B_f\sigma_s)y_v,\\
K_P&=y_v(\theta_s+D\sigma_s+\nu)
                              -y_s(\theta_v+D\beta),\\
K_V&=y_t(\theta_v+D\beta)
                              -y_v(\theta_t+D\sigma_t+B_f),\\
J_0&=fK_U+jK_P+gK_V.
\end{aligned}
\tag{12}
\]
Every derivative here fixes the original v.

The two corrected formal gradients needed below evaluate to
\[
\begin{aligned}
Q_U^{\rm ev}&=j-Dg+\nu f,\\
Q_V^{\rm ev}&=H_s^{\rm ev}-h_{0,s}
                         =-fy_s-j\sigma_s-g\theta_s.
\end{aligned}
\tag{13}
\]
The second equality differentiates the full actual H level.
In particular its moving level term \(h_{0,s}\) has not been
discarded. Equations (11)--(13) retain every lower contribution
of the genuine scalar and potentials.

## 4. Three exact polynomial certificates

Define the following polynomials in O:
\[
\begin{aligned}
\mathcal A_\beta
  &:=\beta^2y_t+\beta\theta_vy_s+y_v^2
                      -\beta\sigma_ty_v-\sigma_sy_v\theta_v,\\
\mathcal B_\beta
  &:=\beta^2(\theta_t+B_f)+D\beta y_v+y_v\theta_v
       +\beta(\theta_s+\nu-\sigma_t)\theta_v-\sigma_s\theta_v^2.
\end{aligned}
\tag{14}
\]
Their definitions contain no division by beta, f or g.
For the first certificate put
\[
\Lambda=y_v+\beta(\theta_s+\nu)-\sigma_s\theta_v.
\]
Direct expansion of the complete expression (11) gives
\[
\boxed{\beta J_1+f\mathcal A_\beta+g\mathcal B_\beta
                                      =\Lambda\mathcal T.}
\tag{15}
\]
This is an exact polynomial identity before using
\(\mathcal T=0\).

For the constant coefficient define
\[
\begin{aligned}
\mathcal R={}&
f\{(\beta y_s-\sigma_sy_v)\mathcal B_\beta
      -(\beta(\theta_s+\nu)-\sigma_s\theta_v)\mathcal A_\beta\}\\
&+g\{(\theta_v+D\beta)\mathcal A_\beta-y_v\mathcal B_\beta\}.
\end{aligned}
\tag{16}
\]
Expansion using (12),(14) gives the second exact certificate
\[
\boxed{\beta^2J_0-\mathcal R=\beta K_P\mathcal T.}
\tag{17}
\]
Finally put
\[
\begin{aligned}
\mathcal S={}&(-\beta y_s+\sigma_sy_v)f^2\\
 &+\{y_v+\sigma_s\theta_v-\beta(\theta_s+\nu)\}fg
                  +(\theta_v+D\beta)g^2.
\end{aligned}
\tag{18}
\]
The complete formulas (13) give the third certificate
\[
\boxed{\beta\mathcal W-\mathcal S
                           =-(\sigma_sf+g)\mathcal T.}
\tag{19}
\]
These three identities use only polynomial expansion of the
displayed full expressions. In particular they do not result
from evaluating at a moving root and then omitting its
derivatives.

## 5. The rational syzygy multiplier is a coefficient-field unit

Equations (6),(15) and \(J_1=0\) imply
\[
f\mathcal A_\beta+g\mathcal B_\beta=0.
\tag{20}
\]
The polynomials f and g cannot both vanish identically. If they
did, \(\mathcal T=j\beta=0\) and \(\beta\ne0\) would give
j=0, contradicting the unit full H-gradient.

Work temporarily in the fraction field \(L(v)\). If \(g\ne0\),
take \(\widetilde\kappa=\mathcal A_\beta/g\); (20) gives
\(\mathcal B_\beta=-\widetilde\kappa f\). This includes
the case \(f=0\), in which \(\mathcal B_\beta=0\).
If \(g=0\), then \(f\ne0\), \(\mathcal A_\beta=0\),
and take \(\widetilde\kappa=-\mathcal B_\beta/f\).
Thus in every case
\[
\mathcal A_\beta=\widetilde\kappa g,\qquad
\mathcal B_\beta=-\widetilde\kappa f,\qquad
\widetilde\kappa\in L(v).
\tag{21}
\]
There is no coprimality claim and no evaluation at a zero of
one of these denominators.

Substitute (21) into the ENTIRE expression (16).
It gives \(\mathcal R=\widetilde\kappa\mathcal S\).
Now use \(\mathcal T=0\), (17),(19) and (9):
\[
\beta^2J_0=\mathcal R
 =\widetilde\kappa\mathcal S
 =\widetilde\kappa\beta\mathcal W
 =-\widetilde\kappa\tau\beta^2.
\tag{22}
\]
Beta is a nonzero element of the domain O. Cancellation in its
fraction field proves
\[
\boxed{\widetilde\kappa=\kappa_0
       =-\frac{J_0}{\tau}=\frac{a_0^4}{\tau}\in L^*.}
\tag{23}
\]
Both entries of (21) are therefore polynomial identities with
a nonzero coefficient-field multiplier. This proves (1).
It also proves that any poles introduced by the temporary
choice in (21) are removable as identities, not by deleting
points of the intrinsic line.

In particular (1) holds at every zero of beta, including a
point where f and g both vanish. The proof cancels a nonzero
polynomial to establish a global identity; it does not assert
that beta has nonzero value everywhere. No transformation of
the original coordinates or line parameter has occurred.

## 6. Critical points and the coprimality boundary

If sigma has degree two, beta has degree one and (9) says that
the UV minor has its single simple zero at precisely the
critical point of sigma. The other minors still generate the
unit ideal with it. One must not replace this statement by a
unit assertion for the UV minor or for the pair \((f,g)\).

More explicitly, at a zero of beta, the polynomial identities
(14),(21) specialize to
\[
\kappa_0g=y_v(y_v-\sigma_s\theta_v),\qquad
-\kappa_0f=\theta_v(y_v-\sigma_s\theta_v).
\tag{24}
\]
All quantities are differentiated first at fixed original v,
then evaluated. Formula (24) does not differentiate a moving
critical value. It is a necessary critical-point restriction,
not a claim that the projected curve is normal or immersed.

For a formal countercontrol to the coprimality inference alone,
take
\[
(y,\sigma,\theta)=(v,v^2,0),\qquad
H=P-U^2,\qquad Q=V.
\tag{25}
\]
On this polynomial line the two gradients are
\((-2v,1,0)\) and \((0,0,1)\). Their cross product is
\((1,2v,0)\), exactly the primitive tangent, and their minors
generate the unit ideal. Nevertheless
\[
(H_U^{\rm ev},H_V^{\rm ev})=(-2v,0)
\]
does not generate \(L[v]\). Its UV minor is \(-2v=-\beta\),
as the orientation in (9) predicts.
This control supplies no genuine264/296 potential pedigree,
full calibrated scalar or actual chart. In particular it is
NOT a counterexample to (1). It only shows why the affine
coprimality proof of494 cannot be reused at nonlinear critical
points.

## 7. Verification and exact scope

The entire264 and296 sources were freshly read through EOF,
including296's full \(J_0,J_1\) and corrected-gradient formulas.
The actual whole-line and projection distinction from290 was
also read completely. No birationality, projected-plane
normality or irreducibility of H has been added.

Fresh unsaved a99ed0 reconstructed (15),(17),(19) directly from
the full generic-jet expressions (11)--(14), with f,g,j and
all coordinate derivatives left independent. It verified the
EXACT multiples \(\Lambda\mathcal T\), \(\beta K_P\mathcal T\)
and \(-(\sigma_sf+g)\mathcal T\), not just the identities after
imposing tangency. Every residual was zero. It also checked
the complete substitution \(\mathcal R=\widetilde\kappa\mathcal S\).
The primitive tangent and field-unit arguments are the written
proofs above, not inferences from symbolic samples.

The lemma requires nonconstant sigma only to ensure that beta
is a nonzero polynomial. It covers arbitrary positive degree,
including affine sigma and all critical-point multiplicities.
It does not claim an actual reframe lowering that degree, a
nonlinear-sigma exclusion, a chart-entry reduction, recognition
of the original kernel, unrestricted cancellation, novelty or
external certification.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical record was edited. A complete
independent saved-source review remains separate from this
author verification.
