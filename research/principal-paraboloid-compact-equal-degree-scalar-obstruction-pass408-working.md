# A compact equal-degree family cannot have a nonzero scalar determinant

Working algebraic obstruction. Unlike406's final calculation, the
slope below may depend on both coefficient parameters. Commuting
coefficient derivatives force incompatible equations for the same
nonzero derivative of the middle intercept.

The first result is a standalone differential-field lemma. Its
application to normalized actual coefficients is conditional on
establishing that family and all original chart hypotheses.

## 1. Exact coefficient-field lemma

Let L be finite over C(a,z), with a,z algebraically independent.
Use its unique commuting characteristic-zero coordinate partials,
dot=partial_a and prime=partial_z. Let eta be complex and
lambda,G,K0,V arbitrary elements of L. For algebraically independent
polynomial indeterminates X,R over L define
\[
\begin{aligned}
Y&=(X+\lambda)R-zX/2+G,\\
Z&=R^2+K_0,\\
W&=-2\lambda R^2+(zX-2G+2\eta\lambda)R
                     +(K_0-\eta z)X+V.
\end{aligned}
\tag{1}
\]
The claim is
\[
\boxed{J:=\det\frac{\partial(Y,Z,W)}{\partial(a,z,R)}
\text{ cannot belong to }L^*.}
\tag{2}
\]
Membership in L* means independent of X,R and nonzero. In
particular lambda'=0 is NOT assumed.

Suppose otherwise. The X-squared coefficient is
\[
[X^2]J=(z-2\eta)\dot K_0/2.
\tag{3}
\]
The element z-2eta is nonzero, so dot K0=0. Also K0' is nonzero:
otherwise the Z differential row would be (0,0,2R), contradicting
nonzero scalar calibration at R=0.

After dot K0=0 the entire determinant ledger is
\[
\begin{aligned}
[XR]J={}&2\eta\dot G-2\eta K_0'\dot\lambda
                       +zK_0'\dot\lambda-\dot V,\\
[X]J={}&K_0'(z\dot G-\dot V),\\
[R^2]J={}&2[-2\eta\dot G\lambda'+2\eta G'\dot\lambda
              -K_0'\lambda\dot\lambda
              +\dot V\lambda'-V'\dot\lambda],\\
[R]J={}&-2[GK_0'\dot\lambda+\dot G K_0'\lambda
                                      +\dot G V'-G'\dot V],\\
[1]J={}&K_0'[-2G\dot G+2\eta\lambda\dot G-\lambda\dot V].
\end{aligned}
\tag{4}
\]
There are no other terms. The X and XR equations give
\[
\dot V=z\dot G,\qquad \dot G=K_0'\dot\lambda.
\tag{5}
\]
If dot lambda were zero, these identities and dot K0=0 would
make the whole a column of the differential matrix zero. Thus
\[
\dot\lambda\ne0,\qquad K_0'\ne0.
\tag{6}
\]
Substitution in the R-squared and R equations now gives
\[
\begin{aligned}
V'&=2\eta G'-K_0'\lambda+(z-2\eta)K_0'\lambda',\\
G-(z-2\eta)G'+(z-2\eta)K_0'\lambda'&=0.
\end{aligned}
\tag{7}
\]
Only the proved nonzero factors in (6) were canceled.

Define actual coefficient elements
\[
G_0=G-K_0'\lambda,\qquad V_0=V-zK_0'\lambda.
\tag{8}
\]
Their dot derivatives vanish by (5) and commutation. By commutation,
the dot derivatives of G0' and V0' also vanish. Substituting (8) into (7) cancels
every lambda' term and gives
\[
\begin{aligned}
\lambda[2K_0'+(z-2\eta)K_0'']+V_0'-2\eta G_0'&=0,\\
\lambda[K_0'-(z-2\eta)K_0'']+G_0-(z-2\eta)G_0'&=0.
\end{aligned}
\tag{9}
\]
Differentiate by dot and use dot lambda nonzero. Both brackets
must vanish. Their sum is 3K0', contradicting (6). This proves
(2), retaining arbitrary lambda', eta=0 and zero lower functions.
No rationality of the dot-constant field has been assumed.

## 2. Conditional application to normalized actual coefficients

Retain the complete actual264 degree-one chart as stated in401:
the original global slice, full initial kernel, literal selected
partial, both returns and calibrated scalar all remain imposed.
Suppose its actual coefficients have already been shown to satisfy
\[
n=-s^2/(4t^2)+\eta s/t,\qquad
\mu=s/t-2t\lambda,\qquad\eta\in\mathbb C.
\tag{10}
\]
Here lambda may depend on both t,s. No assertion that arbitrary
charts can be normalized to (10) is being made.

Put q=s/t and define
\[
\begin{gathered}
z=q+2t\lambda,\qquad R=P+tX+q/2,\qquad
\nu=(\eta-q/2)/t,\\
K_0=2tr+h+\eta q-q^2/2,\qquad G=r-\lambda q/2,\\
V=\ell+rq-\nu h-\eta\lambda q.
\end{gathered}
\tag{11}
\]
The complete literal rows become exactly (1). This is an algebraic
identity in the coefficients, independent of any derivative of
lambda, so it remains valid for lambda_s nonzero. In this section
z denotes the new coefficient element in (11), not the original
Z-intercept usually called z.

If this z is not complex, it is transcendental over C. At least
one of (t,z),(s,z) is a separating coefficient basis: take a=t if
z_s is nonzero, and a=s otherwise. In the latter case z_t is
nonzero by the joint-constant property. Thus L is finite over
C(a,z) with a nonzero coefficient-base Jacobian. The affine change
P to R at fixed actual X has R_P=1. Hence the full actual
determinant in (a,z,R) remains a nonzero element of L independent
of X,R. The original X,P are algebraically independent over L,
and so are X,R. Lemma (2) contradicts that scalar condition.
Consequently
\[
\boxed{\text{Any supplied actual member of (10) must have }z\in\mathbb C.}
\tag{12}
\]
No coefficient element or moving R is asserted to be an original
polynomial coordinate.

Let Dscript=partial_t+mu*partial_s and
Kcal=Dscript(mu)+4lambda, as in401. Directly from (10),(11),
\[
\mathscr Dq=-2\lambda,\qquad
\mathscr Dz=2t\mathscr D\lambda=-\mathcal K.
\tag{13}
\]
If Kcal is nonzero, z cannot be complex, giving the useful
conditional exclusion
\[
\boxed{\text{Full actual degree-one entry}+(10)+\mathcal K\ne0
\quad\text{is impossible}.}
\tag{14}
\]
The Kcal=0 boundary is explicitly left to a separate argument;
it is not divided away in this lemma.

## 3. Verification and scope

Fresh unsaved c9db5f rebuilt the entire generic determinant with
arbitrary lambda', dot(lambda), G', dot(G), K0', dot(K0), V' and
dot(V). It produced (3),(4), retaining all mixed terms. The earlier
10431d independently verified the full row substitution (11) from
the literal401 equations. That polynomial identity did not use a
derivative restriction on lambda.

Geometry's separate outline reconstruction0ee6ba verified the full
generic determinant and both derivative cancellations with lambda'
retained. In particular differentiating the first relation in (7)
cancels its lambda_a,z terms exactly. The saved source still
requires its own full review before canonical acceptance.

The result obstructs a specified compact family, not all remaining
degree-one data. Higher degrees, general coupling, other initial
ideals, arbitrary-chart entry and original-ring recognition remain
open. No saved checker was executed, imported, compiled or rerun;
no held earlier source was edited. No novelty, human-expert review,
formal certification or unrestricted cancellation result is claimed.
