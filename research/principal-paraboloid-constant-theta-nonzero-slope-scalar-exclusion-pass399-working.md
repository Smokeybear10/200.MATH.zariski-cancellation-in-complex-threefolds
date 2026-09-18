# The constant-theta nonzero-slope family fails the full scalar

Working exclusion in the supplied actual principal chart: the
normalized nonzero-slope constant-theta family specified below admits
no nonzero calibrated scalar determinant. The proof keeps eta=0.
Together with the exact necessity397 and actual normalization398,
this excludes the nonzero-slope branch of386.

The changes of coefficient and intrinsic parameters used in the
scalar calculation are not original polynomial-coordinate changes.
No nonconstant-theta rank condition is imported into this boundary.

## 1. Actual input and the normalized family

Retain the full actual264 chart and the constant-theta line conclusion
of [386](principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\quad E_0=\partial_{u_0},
\quad \deg_{E_0}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a_0=E_0X\ne0,\quad N=[u_0^4]\partial_Z|_{A_0}\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad K=\operatorname{Frac}A_0=L(P)=\mathbb C(y,z,w),\\
P=\sigma,\quad O=L[P]=L[y,\sigma,\theta]=L[y,z,w],
\quad \tau=NP\in L^*,\quad k=s.
\end{gathered}
\tag{1}
\]
Thus t,s are algebraically independent, the exact coefficient
partials commute and have joint constants C, and P is an affine
intrinsic parameter. The selected partial is the literal actual
Z-partial. First assume specifically the normalized family
\[
\begin{gathered}
\lambda=\frac{s}{2t^2},\qquad
n=-\frac{s^2}{4t^2}+\frac{\eta s}{t},\qquad \eta\in\mathbb C,\\
\nu=n_s=\frac\eta t-\frac{s}{2t^2},\qquad
a=n_t=\frac{s^2}{2t^3}-\frac{\eta s}{t^2},\\
\theta=h\in L,\qquad y=\lambda P+r,\qquad r\in L.
\end{gathered}
\tag{2}
\]
The letter a in (2) is n_t, not the actual nonzero leader a0.
No eta division occurs anywhere in this proof.

The complete literal rows, with ell in L, are
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+2t(\lambda P+r)+h+n+(2tP+s)X+t^2X^2,\\
W&=-2\lambda P^2-(2r+a)P+\ell-\nu h+hX+sX^2.
\end{aligned}
\tag{3}
\]
The actual scalar condition is
\[
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-\frac{a_0^4}{\tau}\in L^*.
\tag{4}
\]
All derivatives in (4) fix the actual X, and the coefficient
derivatives fix P. Source386 also supplies
ell_t=n_ts*h+(lambda-nu)(2r+a). The contradiction below does not
need to substitute that additional equation: it already follows
from the full rows (3) and nonzero scalar (4).

## 2. A coefficient basis and a moving intrinsic parameter

Set q=s/t. Then C(t,q)=C(t,s), so L is still finite over the
displayed rational coefficient field. Denote its exact partials by
\[
\dot f=\left(\partial_t+q\partial_s\right)f,
\qquad f'=t\partial_s f\quad(f\in L).
\tag{5}
\]
Thus dot means t derivative at fixed q, not the old t derivative
at fixed s; prime means q derivative at fixed t. These derivations
commute, satisfy dot(t)=1, dot(q)=0, t'=0, q'=1, and have joint
constants C. The last assertion follows from the invertible change
of basis (5), not from a rationality assumption on L.

At fixed formal X define
\[
\xi=P+\frac q2+tX,
\qquad s=tq,\qquad P=\xi-\frac q2-tX.
\tag{6}
\]
This is an invertible change of the parameter presentation over
L[X], not an automorphism asserted on the original four-ring.
Its coefficient-dependent and X-dependent parts are differentiated
in full. In particular
\[
\det\frac{\partial(t,s,P)}{\partial(t,q,\xi)}=t,
\qquad
\widetilde J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,q,\xi)}
               =tJ(X)=-\frac{t a_0^4}{\tau}\in L^*.
\tag{7}
\]
The determinant on the left holds X fixed; its t,q partials fix
xi and restrict to (5) on L. Its nonzero scalar value has no X
or xi dependence. No moving-root evaluation is substituted for
the parameter chain rule.

Introduce only coefficient-field elements
\[
\begin{aligned}
K_{\rm aux}&=2tr+h+\eta q-\frac{q^2}{2},\\
M&=t\ell+\frac{qK_{\rm aux}}2+\frac{q^3}{4}
                  -\eta q^2-\eta h.
\end{aligned}
\tag{8}
\]
Here Kaux is not the function field K. Direct substitution in the
FULL (3) gives
\[
\boxed{
\begin{aligned}
Y&=(\xi-q)X+\frac{q\xi+K_{\rm aux}-h-\eta q}{2t},\\
Z&=\xi^2+K_{\rm aux},\\
W&=[K_{\rm aux}+2q(\xi-\eta)]X
 +\frac{-q\xi^2+(h-K_{\rm aux}+2\eta q)\xi+M}{t}.
\end{aligned}}
\tag{9}
\]
Both coefficient substitutions are invertible in L:
r=(Kaux-h-eta*q+q^2/2)/(2t) and
ell=(M-q*Kaux/2-q^3/4+eta*q^2+eta*h)/t.
No constancy of Kaux or M has yet been assumed.

## 3. Highest X and intrinsic coefficients integrate exactly

Write Cij=[X^i xi^j]Jtilde. The rows (9) are polynomial in X,xi
over L. Expanding their determinant, retaining all coefficient
derivatives, first gives
\[
C_{20}=2(q-\eta)\dot K_{\rm aux}.
\tag{10}
\]
Since q is transcendental over C and eta is complex, q-eta is a
nonzero field element. Calibration forces
\[
\dot K_{\rm aux}=0.
\tag{11}
\]
Define
\[
G=M+\eta h-\frac\eta2K_{\rm aux}+\eta^2q.
\tag{12}
\]
After (11), two further exact coefficient identities are
\[
\begin{aligned}
C_{11}&=-\frac{2(t\dot G-G)+\eta K_{\rm aux}
                           +q(q-\eta)K_{\rm aux}'}{t^2},\\
2t^3C_{02}+t^2C_{11}&=2qG'.
\end{aligned}
\tag{13}
\]
The coefficients on the left all vanish, so q nonzero gives
\[
G'=0,\qquad
2(t\dot G-G)+\eta K_{\rm aux}
                       +q(q-\eta)K_{\rm aux}'=0.
\tag{14}
\]
This keeps eta=0 and uses no h or h-derivative as a denominator.

Differentiate the second identity in (14) by prime. Commutation,
G'=0, and the product rule give
\[
q\,[2K_{\rm aux}'+(q-\eta)K_{\rm aux}'']=0.
\tag{15}
\]
Consequently ((q-eta)^2*Kaux')'=0. Its dot derivative is also
zero by (11) and commutation. Joint constants therefore give a
complex c1, and then a complex k0, with
\[
\boxed{K_{\rm aux}=k_0-\frac{c_1}{q-\eta},
\qquad k_0,c_1\in\mathbb C.}
\tag{16}
\]
Indeed (q-eta)^2*Kaux'=c1 and
(Kaux+c1/(q-eta))'=0; the latter expression is also dot-constant.
This is exact integration inside L, not an assertion that L=C(t,q).

Substituting (16) into (14) yields
2(t*dot(G)-G)+eta*k0+c1=0. Differentiate by dot to obtain
ddot(G)=0, since t is nonzero. Now G'=0 implies both integration
constants are joint constants. Thus
\[
\boxed{G=g_1t+\frac{\eta k_0+c_1}{2},\qquad g_1\in\mathbb C.}
\tag{17}
\]
No eta, c1 or unknown derivative was divided out to reach (16),(17).

## 4. The zero-residue case already violates calibration

If c1=0, (16) makes Kaux=k0 complex. The middle row of the
Jacobian of (9), in columns t,q,xi, is then exactly
\[
(0,0,2\xi).
\tag{18}
\]
Hence Jtilde is divisible by xi in L[X,xi]. Evaluating xi=0 makes
it zero, contrary to the nonzero scalar (7). This treats c1=0
without dividing it, using a square-root rationality claim, or
requiring a separate original-ring valuation theorem.

## 5. The nonzero-residue case has an impossible remaining coefficient

Assume c1 nonzero and set omega=q-eta, a nonzero coefficient-field
element. After (16),(17), the complete constant-in-xi linear-X
coefficient is
\[
C_{10}=\frac{c_1}{2t^2\omega^3}
 \left[2\omega^2(h-t\dot h+\eta q-k_0)+c_1(3q-2\eta)\right].
\tag{19}
\]
Every prefactor is nonzero, so calibration gives
\[
h-t\dot h=H_0,\qquad
H_0=k_0-\eta q-\frac{c_1(3q-2\eta)}{2\omega^2}.
\tag{20}
\]
Here dot(H0)=0. Put F0=ker_L(dot). Direct differentiation of
(h-H0)/t shows that it lies in F0. Thus the exact general form is
\[
h=t\psi+H_0,\qquad \psi\in F_0.
\tag{21}
\]
There is no assertion that psi is rational in q. Commutation makes
psi' belong to F0 as well.

Now substitute (16),(17),(21) in the full rows (9). The coefficient
linear in xi and constant in X is exactly
\[
\boxed{
C_{01}=\frac{c_1q}{4t^3\omega^4}
       \left[3c_1q+2t\omega^2(\omega\psi'-\psi)\right].}
\tag{22}
\]
Its derivation retains the arbitrary coefficient psi and its full
q derivative. In particular no normalization of this last function
is made.

The prefactor in (22) is nonzero, and C01 must vanish. All elements
q,omega,psi,psi' are dot-constant. Differentiating the resulting bracket
identity by dot and subtracting t times that derivative from the
identity therefore gives
\[
3c_1q=0,
\tag{23}
\]
which is impossible. Equivalently t is transcendental over F0,
and the bracket is a polynomial in t with nonzero constant term.
The differential proof already gives the contradiction without
identifying F0 with C(q).

Both alternatives for c1 are now excluded. Therefore the literal
rows (3) in the normalized family (2) cannot satisfy the nonzero
scalar (4), including eta=0.

## 6. Composition with the actual family normalization

The complete held necessity source
[397](principal-paraboloid-constant-theta-nonzero-slope-coefficient-family-pass397-working.md)
proves, in the nonzero-slope branch of386, the exact family
\[
\lambda=\frac{s-s_0}{2(t-\tau_0)^2},\qquad
n=-\frac{(s-s_0)^2}{4(t-\tau_0)^2}
  +\frac{\eta(s-s_0)}{t-\tau_0}+\gamma t+c_0,
\quad \tau_0,s_0,\eta,\gamma,c_0\in\mathbb C.
\tag{24}
\]
Here tau0 is a complex time shift, distinct from the intrinsic
speed tau in (1). Source397 separately proves eta=0 and eta nonzero,
and transfers only the autonomous coefficient-field lemma in387,
not that source's nonconstant-theta Omega contradiction.

The complete held actual normalization
[398](principal-paraboloid-constant-theta-coefficient-family-actual-normalization-pass398-working.md)
then supplies the complex polynomial automorphism
\[
\begin{aligned}
X^*&=X,\qquad Y^*=Y-\tau_0X^2+\gamma/2,\\
Z^*&=Z-2\tau_0Y+\tau_0^2X^2-s_0X-(\gamma\tau_0+c_0),\\
W^*&=W-s_0X^2 .
\end{aligned}
\tag{25}
\]
Its polynomial inverse, full initial kernel, exact time profile,
identity of literal Z-partials, unchanged N and exact fields, both
returns and full scalar are all proved there. Its parameters become
t*=t-tau0, s*=s-s0, n*=-s*^2/(4t*^2)+eta*s*/t*, and its slope
becomes lambda*=s*/(2t*^2). In particular theta*=theta is still in L.
Thus it provides the actual normalized input (1),(2), including eta=0.
The scalar contradiction above excludes every supplied member of (24).

This composition only excludes the nonzero-slope constant-theta
branch in the retained actual chart with k=s and n_ss nonzero.
The separate zero-slope exclusion396 is not needed or re-proved
here, even though397 cites it to enter its nonzero-slope discussion.
No arbitrary normalization of k or of another initial-kernel sector
is asserted.

## 7. Verification record and scope

The complete386 source was freshly read through EOF in6c6c11 at
SHA087020cf2f9694cb83110223e06c2910a711abd7205248661583097fdc1163d4.
Its whole-line parameter and literal scalar are the inputs used
here, not a gradient conclusion from a sliced surface.
The complete397 and398 sources were read through EOF in b8e36f
and cd02e1, with fresh hashes05f2c6 confirming their held versions
9f9ecb415addb7ceefad5a11e77f09bc28b97bd984dd625b063e4538ea3628d4
and c823018d086a523d0bddef41c62678af40c1c214843accac3020ab26f5e6fff3.
No use is made of the nonconstant-theta Omega gate from385/387.

Fresh unsaved917786 independently checked all three compact rows
(9), the parameter determinant t in (7), both identities (13),
and the full coefficient (19), with zero residuals. Fresh raw
d3d30f rebuilt the complete determinant with arbitrary Kaux,h,M
and their exact first coefficient derivatives. Fresh25d5b7 then
rebuilt the full determinant after (16),(17),(21), retaining psi'
as an independent derivative, and obtained (22). These calculations
are generic identities, not numerical sampling or a converse to
the actual entry.

No invariant original coordinate is constructed, and no equality
L=C(t,s) or F0=C(q) is used. No claim about equal intrinsic degrees,
arbitrary-chart entry, unrestricted cancellation, novelty or
formal certification is made. No saved checker was executed,
imported, compiled or rerun. No held source, canonical index or
ledger was edited.
