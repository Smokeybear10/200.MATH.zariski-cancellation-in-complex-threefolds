# A zero normalized offset is impossible for a moving conic leader

Working boundary exclusion: retain the FULL actual conic hypotheses
of496 and suppose
\[
a_t\ne0,\qquad (v_1)_s=b_s-pa\ne0,\qquad h''=0.
\]
Use the licensed complex normalization of503 Section3 to put
\(m=t\), \(k=ts\), and \(h=H\in\mathbb C\). Then
\[
\boxed{H\ne0.}
\tag{1}
\]
This note excludes only the added boundary H=0. It does not infer
h''=0 in the remaining moving-leader sector, and does not exclude
the normalized H-nonzero case. The proof retains every lower
coefficient and uses the constant intrinsic coefficient of the
ENTIRE calibrated scalar.

## 1. Full actual input and the normalization license

Retain every hypothesis and necessary identity of
[496](principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md),
including the full actual264/296/327 data and the unit multiplier494.
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\quad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{2}
\]
Both actual returns, the original global slice and the genuine
moving H,Q levels remain required. Neither a0 nor rho is assumed
to be an actual unit. Exact coefficient partials commute, and
their joint constants are C.

Before normalization,496 gives
\[
\begin{gathered}
F_0=\ker_L\partial_s\text{ finite over }\mathbb C(t),\qquad
m=pt+d_0,\quad p\in\mathbb C^*,\quad d_0\in\mathbb C,\\
k=ms+f,\qquad
n=p^2s^2/4+(pf'/2-h)s+n_0,\qquad f,h,n_0\in F_0,\\
a\in F_0^*,\quad 1+ma\ne0,\quad
f''''=6ah''.
\end{gathered}
\tag{3}
\]
Primes on F0 denote the exact t derivative; its constants are C.
The EXTRA assumption h''=0 therefore makes h complex affine and f
a complex polynomial of degree at most three. This follows by
successive subtraction in F0, not by assuming F0=C(t).

For precision, the actual normalization used here is the one
proved in
[503 Section3](principal-paraboloid-moving-conic-leader-zero-transverse-exclusion-pass503-working.md).
It does not require that \((v_1)_s\) vanish. Its maps are
\[
\begin{aligned}
X_1&=X,&Y_1&=Y+\tau X^2,&
Z_1&=Z+2\tau Y+\tau^2X^2,&W_1&=pW,\qquad \tau=d_0/p,\\
X_2&=X_1,&Y_2&=Y_1,&Z_2&=Z_1-c_0X_1,&
W_2&=W_1+c_3Z_1+c_2Y_1+c_1X_1^2,\\
X_*&=X_2+x,&Y_*&=Y_2,&Z_*&=Z_2,&W_*&=W_2+2xY_2.
\end{aligned}
\tag{4}
\]
Here the intermediate coupling is
\(t_1s_1+\sum_{i=0}^3c_it_1^i\); all ci are complex. In the
subsequent k=ts frame write h=h1*t+H and set x=h1/2. In particular
W2 uses the OLD Z1. The composite inverse is polynomial: set
\(X=X_*-x\), then
\[
\begin{aligned}
Y&=Y_*-\tau X^2,\\
Z&=Z_*+c_0X-2\tau Y-\tau^2X^2,\\
W&=\{W_*-2xY_*-c_3(Z_*+c_0X)-c_2Y_*-c_1X^2\}/p.
\end{aligned}
\tag{5}
\]
The only constant divided here is nonzero complex p. The full
transport and selected-partial license are those of426 and503,
including the entire initial kernel and both actual returns.

The coefficient transport before imposing either zero or nonzero
transverse slope gives
\[
a_*=pa,\qquad
(b_*)_{s_*}-a_*=b_s-pa,\qquad
(a_*)_{t_*}=pa',\qquad N_*=N,\quad NP_*=\rho,
\tag{6}
\]
with \(P_*=P-2xt_1\). Row and coefficient-parameter determinants
are both p, and a0 is unchanged. Thus a' and the transverse slope
remain nonzero, while (2) retains its original global-slice and
speed interpretation. All maps have complex coefficients even
though a is nonconstant.

We now assume the normalized constant H is zero and derive a
contradiction. This is an additional boundary assumption, not a
consequence of the preceding normalization.

## 2. The full normalized rows and the exact coefficient basis

Drop stars. From496, with m=t, k=ts and h=0, the necessary
coefficient identities are
\[
\begin{gathered}
a\in F_0^*,\quad a'\ne0,\quad\delta=1+ta\ne0,\qquad
\lambda=0,\quad r=r_0\in F_0,\\
n=s^2/4+n_0,\quad n_0\in F_0,\qquad
z=b-as,\quad z_s=b_s-a\ne0,\\
\theta=aP^2+(as+z)P+c,\qquad y=-\theta/2+r,\qquad c\in L.
\end{gathered}
\tag{7}
\]
The symbol z is this NEW coefficient-field element, not the
intrinsic first-potential generator used in264. Since z_s is
nonzero, (t,z) is an exact separating basis. Write
\[
S=s\in L,\qquad S_z=1/z_s\ne0,\qquad
\partial_t|_z=\partial_t|_s-\frac{z_t|_s}{z_s}\partial_s.
\tag{8}
\]
The z-constant field is still F0. No identification L=F0(z) is
made. Henceforth t,z derivatives mean this basis. Derivatives of
elements of F0 are unchanged. At fixed actual X,
\[
J_{t,z,P}(X)=-\frac{a_0^4S_z}{\rho}\in L^*.
\tag{9}
\]
Its coefficient-field value need not be constant in either
coefficient direction.

Put \(K=(2r+n_0')/t\in F_0\). The full second potential simplifies
EXACTLY to \(w_{\rm int}=-KP+(\ell-Sr)/t\), because its theta
terms cancel. Thus the COMPLETE literal rows are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+SP+t\theta+S^2/4+n_0
                                  +(2tP+tS)X+t^2X^2,\\
W&=-KP+(\ell-Sr)/t+\theta X+SX^2.
\end{aligned}
\tag{10}
\]
Neither c nor ell, nor any of their moving derivatives, has been
set to zero.

Define the two actual rows U=Z and T=W+2XY, and the moving row
V=-2Y-aZ. The exact496 connection, now with h''=0, is
\[
J_{t,z,P}=\frac12\det\bigl(dU,\ dV+a'U\,dt,\ dT\bigr).
\tag{11}
\]
V is generally NOT an actual complex coordinate. Omitting its
connection term would change the complete scalar.

## 3. The cubic coefficient and the complete centered rows

At fixed X make the horizontal change
\[
\xi=P+S/2+tX.
\tag{12}
\]
The determinant of (t,z,P) to (t,z,xi) is one. This does not assert
that xi lies in A or that its original N speed equals rho. The
full scalar (9) remains independent of X and xi after this change.

Set
\[
\begin{gathered}
\overline U=2tr+n_0\in F_0,\qquad
v=z-2\delta X,\qquad w=2X^2-K,\qquad B=2r+tK\in F_0,\\
\overline V=c-2r-a\overline U-aS^2/4-zS/2
                         +at^2X^2+(S-tz)X.
\end{gathered}
\tag{13}
\]
Direct substitution in (10) gives
\(U=\xi^2+\overline U\) and \(V=v\xi+\overline V\).
Before using the next scalar coefficient, the complete T row is
\[
T=w\xi+\overline T,\qquad
\overline T=(\ell-Sr)/t+KS/2+BX.
\tag{14}
\]
In particular its uncentered constant term contains 2tX^3; that
term has canceled against the centering of wP, not been discarded.

The complete cubic coefficient496(28), or its exact integration496(29),
gives in the present basis
\[
\overline T_z=-K'/a',\qquad
\overline T=-\eta z+BX+C_0,\quad \eta=K'/a',\quad C_0\in F_0.
\tag{15}
\]
Only a' is divided, already nonzero. K,K' and eta are allowed zero.
For example one can reconstruct the retained lower potential as
\(\ell=t(-\eta z+C_0-KS/2)+Sr\). Integration in (15) means that the
remaining z derivative vanishes; it makes no rationality claim.

## 4. The constant intrinsic coefficient is already impossible

At xi=0 the entire corrected matrix in (11) is
\[
\begin{pmatrix}
\overline U'&0&0\\
\overline V_t+a'\overline U&\overline V_z&v\\
\overline T_t&-\eta&w
\end{pmatrix}.
\tag{16}
\]
All lower t derivatives remain present. Expanding this full matrix,
with the factor one half from (11), gives
\[
\mathcal J_0=[\xi^0]J
 =\frac{\overline U'}2(\overline V_z w+\eta v).
\tag{17}
\]
The calibrated value (9) is nonzero, so \(\overline U'\ne0\).
There is no division by a potentially zero lower derivative without
first treating this case: if it were zero, (17) itself would
contradict (9).

From the ENTIRE expression (13),
\[
\overline V_z=(S_z-t)X+Q,\qquad
Q=c_z-\frac{aS+z}{2}S_z-\frac S2.
\tag{18}
\]
The symbol Q in (18) is only an intercept abbreviation, not the
genuine fourth potential. It need not be nonzero. Substitution of
(13),(18) into (17) gives the full polynomial identity
\[
\mathcal J_0=\frac{\overline U'}2
 \left\{((S_z-t)X+Q)(2X^2-K)+\eta(z-2\delta X)\right\}.
\tag{19}
\]
Since (9) has no X dependence, its X-cubed coefficient forces
S_z=t. Its X-squared coefficient then forces Q=0. The remaining
X coefficient is \(-\overline U'\eta\delta\), so eta=0 because both
\(\overline U'\) and delta are nonzero. Equation (19) is now
identically zero, again contradicting (9).

This sequence retains the branches eta=0, K=0, Q=0 and every value
of the remaining lower functions. It does not divide by z, w,
a root of w, or the value of the calibrated scalar. Nor does it
differentiate that value and call its derivative zero. Only
coefficients of a polynomial already known to be independent of X
are compared.

## 5. Verification and the remaining boundary

The full held496 was reread through EOF3a836a+e55985 at
SHA55552b3859862962a4573b91a9792854873eac527bf0403f4cfbb7d84a501565.
The actual normalization and its general slope transport are the
fully checked503 Section3 maps, not an application of503's
zero-transverse-slope exclusion to this nonzero-slope case.

Fresh dc1f47 rebuilds all three original rows (10), the entire
centered U,V,T identities, the corrected constant-xi determinant,
and every coefficient in (19), with zero residuals. Jet's
independent fresh3212ee, completed dc1de8, rebuilds the same literal
rows and complete corrected connection, including the exact basis
factor in (9), and independently verifies the contradiction.
A full saved-source review is recorded separately in the ledger.

Thus the added h''=0, normalized H=0 boundary is empty under the
FULL actual hypotheses and the retained nonzero a', transverse
slope assumptions. The normalized H-nonzero case and the
h''-nonzero moving-frame case remain separate. No general conic
exclusion, arbitrary chart entry, cancellation theorem, historical
novelty or proof-assistant certification is claimed. All saved
checkers remain frozen: none was executed, imported, compiled or
rerun. No earlier mathematical source or canonical file was edited.
