# Excluding the zero-cubic fourth row at the conic degree drop

Working bounded result: in the FULL actual degree-drop sector of512,
the literal cubic coefficient of the fourth intrinsic row cannot
vanish. The direct entry514 and the two-branch curvature reduction516
permit an actual complex normalization. The full remaining scalar
then gives a contradiction in each of the four cases determined by
the transverse slope derivative and a complex normalized offset.

This is an exclusion of the subcase \(g_3=0\), not of every case
in512. It does not assert generic chart entry, unrestricted conic
recognition or general cancellation. No nonzero-delta theorem is
applied at delta zero.

## 1. Actual input and the precise remaining subcase

Retain all actual hypotheses and both exact ring returns of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine third and fourth levels of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
the universal unit multiplier of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md),
and the degree-drop conclusions of
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
O=L[P],\quad L[X,Y,Z,W]=L[X,P],\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_0,w_{\rm int}),\qquad
L[y,z_0,w_{\rm int}]=O.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and have joint constants C.
The field \(F_0=\ker_L\partial_s\) is finite over C(t), and the
constants of its t derivative are C. Neither F_0 nor L is presumed
rational. The calibrated original scalar is
\[
J_{t,s,P}=-a_0^4/\rho\in L^*.
\tag{2}
\]
It is independent of the polynomial variables X and P, but need not
be a complex constant.

Before normalization, the particular hypotheses are
\[
\begin{gathered}
m=k_s,\quad m_s=0,\quad m\notin\mathbb C,\quad p=m_t\ne0,\\
\theta=-P^2/m+bP+c,\quad y=eP^2+lP+r_{\rm old},\qquad
g_3=[P^3]w_{\rm int}=(p-2me)/m^2=0.
\end{gathered}
\tag{3}
\]
The direct actual normalization and raw coefficient argument in
[514](principal-paraboloid-degree-drop-quadratic-row-moving-frame-pass514-working.md)
give
\[
\begin{gathered}
m=t,\quad k=ts+f,\quad a=-1/t,\quad a'=1/t^2,\\
\theta=aP^2+bP+c,\qquad y=-\theta/2+\lambda P+r,\\
n=s^2/4+(f'/2-h)s+n_0,\qquad f,h,n_0\in F_0.
\end{gathered}
\tag{4}
\]
This uses the actual affine-coupling time translation and nonzero
complex W scaling of514, with the original slice and selected
partial retained. It is not an application of327's parity theorem.

The full literal proof in
[516](principal-paraboloid-degree-drop-moving-curvature-exclusion-pass516-working.md)
handles both alternatives for the derivative of
\(v_1=b+(s+f')/t\) and proves
\[
h''=0,\qquad f''''=0.
\tag{5}
\]
Consequently h is complex affine and f is complex cubic. This follows
by repeated subtraction of existing derivatives whose constants are
C, not by an assumption \(F_0=\mathbb C(t)\). The rest of this note
uses (5), and supplies the remaining scalar proof directly.

## 2. Actual normalization of the lower complex coefficients

Write \(f=c_3t^3+c_2t^2+c_1t+c_0\), with all \(c_i\in\mathbb C\).
Apply the actual polynomial automorphism
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z-c_0X,\qquad
W_1=W+c_3Z+c_2Y+c_1X^2.
\tag{6}
\]
The Z on the right of the W equation is the OLD Z. The polynomial
inverse is
\[
X=X_1,\quad Y=Y_1,\quad Z=Z_1+c_0X_1,\quad
W=W_1-c_3(Z_1+c_0X_1)-c_2Y_1-c_1X_1^2.
\]
The literal coefficient transport is
\[
\begin{gathered}
t_1=t,\quad s_1=s+c_3t^2+c_2t+c_1,\quad P_1=P,\quad y_1=y,\\
k_1=ts_1,\qquad
\theta_1=\theta+(c_2+2c_3t)P+c_3k,\qquad
\boxed{n_1=n-c_3tk},\\
a_1=-1/t,\quad b_1=b+c_2+2c_3t,\qquad
\boxed{h_1=h-c_2t/2}.
\end{gathered}
\tag{7}
\]
Here \(n_1=s_1^2/4-h_1s_1+n_{01}\), with \(n_{01}\in F_0\);
its coefficient independent of \(s_1\) is retained. In particular h
is not claimed unchanged by (6). Comparing the ENTIRE Z intercept
gives the displayed \(n_1\), and reexpressing it in \(s_1\) gives
the displayed \(h_1\). The moving slope satisfies
\[
b_1+s_1/t=b+(s+f')/t=v_1.
\tag{8}
\]

Let \(\eta\in\mathbb C\) be the slope of the new affine function
\(h_1\), and put \(x=\eta/2\). The next actual polynomial map is
\[
X_2=X_1+x,\quad Y_2=Y_1,\quad Z_2=Z_1,\qquad
W_2=W_1+2xY_1.
\tag{9}
\]
Its inverse subtracts x from \(X_2\) and \(2xY_2\) from \(W_2\).
In the following formulas all right sides denote the coefficients
after (6):
\[
\begin{gathered}
t_2=t,\quad s_2=s_1+2xt,\quad P_2=P_1-2tx,\quad
y_2=y_1-xP_1+tx^2,\\
\theta_2=\theta_1+2xP_1-2x(s_1+2xt),\quad
k_2=ts_2,\quad a_2=-1/t,\quad b_2=b_1-2x,\\
n_2=n_1+3xs_1t+3x^2t^2,\quad
h_2=h_1-2xt=H\in\mathbb C,\qquad
b_2+s_2/t=b_1+s_1/t.
\end{gathered}
\tag{10}
\]
Thus the zero/nonzero transverse slope split is preserved exactly.
No coefficient-field function was substituted for a complex map
constant.

Both maps belong to the actual filtered family of
[426](general-coupling-normalization-obstruction-pass426-working.md).
Their invertible weighted leading maps preserve the ENTIRE initial
kernel and exact profile. Formula426(15), using its retained omitted
W-partial bound, gives
\(\partial_{Z_1}=\partial_Z-c_3\partial_W\) and \(N_1=N\);
the second map leaves the selected N unchanged. Also \(a_0\) is
unchanged and \(NP_2=\rho\), since \(Nt=0\).
The bad-coordinate row determinant and the coefficient-parameter
determinant are both one. The original global slice, actual
localizations, both returns and (2) therefore survive. No roots of a
polynomial in X are deleted or specialized in this normalization.
The intrinsic quadratic coefficient of theta remains \(-1/t\).
The old Y and Z rows have intrinsic degree at most two, so their
addition to W in (6),(9), together with the affine translation of P,
does not introduce a cubic intrinsic term. Thus the zero-cubic
subcase and the literal entry hypotheses of514 are retained.

Reapply the literal formulas514 to the new chart, and rename its
existing lower coefficients. Dropping subscripts, they read
\[
\begin{gathered}
m=t,\quad k=ts,\quad a=-1/t,\quad h=H\in\mathbb C,\quad
\lambda=-H/(2t),\\
z:=b+s/t,\qquad b=z-s/t,\qquad
r=Hz/2-Hs/(4t)+R,\qquad R\in F_0,\\
n=s^2/4-Hs+n_0,\qquad
K=(2R+n_0')/t\in F_0,\quad n_0'=tK-2R,\\
\boxed{\kappa=1/(2t)-z_s\ne0.}
\end{gathered}
\tag{11}
\]
The field element z is nonzero by512's epsilon conclusion. No
argument below needs division by z. The lower functions R and n_0
are the NEW ones after (6),(9), not constants carried unchanged
from the old chart.

## 3. Three complete rows and the exact scalar licenses

Define an auxiliary horizontal parameter and two coefficients by
\[
Q=P+s/2,\qquad C=c-zs/2+s^2/(4t),\qquad
L=\frac{\ell-sr+Hc}{t}+\frac K2s.
\tag{12}
\]
The letters C and L in (12) denote coefficient functions; C is not
the complex constant field and L is not a new coefficient field.
The exact coefficient field is still the \(L\) of (1) when used in
field notation. To avoid any use of a field/function ambiguity, all
occurrences of \(L_t,L_s,L_z,L_0\) below refer only to the function
in (12).

Put \(U=Z\) and \(T=W+2XY\). The frame \((X,Y,U,T)\) is actual,
with inverse \(Z=U,\ W=T-2XY\). We use it only as an actual
determinant-one row change, not as an assertion that T retains the
old E-degree. Fresh expansion of the original rows gives
\[
\begin{aligned}
Y={}&\frac{Q^2}{2t}
 +\left(X-\frac z2-\frac H{2t}\right)Q
 -\frac C2+\frac{Hz}{2}+R-\frac{Xs}{2}+tX^2,\\
U={}&Q^2+(2tX-H)Q+H(tz-s)+2tR+n_0+t^2X^2,\\
T={}&\left(2X^2-\frac HtX-K\right)Q
 +(Hz+2R)X+L+2tX^3.
\end{aligned}
\tag{13}
\]
In particular the full \(2tX^3\) term is present.
Every lower c and ell remains through C and L.
At fixed actual X, the triangular horizontal change from P to Q
has determinant one. Hence
\[
J=\det\frac{\partial(Y,U,T)}{\partial(t,s,Q)}
  =-a_0^4/\rho.
\tag{14}
\]
Q is an auxiliary horizontal parameter, not an asserted original
ambient coordinate. Only the displayed coefficient-basis change is
needed. No moving-frame derivative correction is omitted in (14),
because Y,U,T are actual rows and are differentiated in full.

If \(z_s=0\), then \(z\in F_0\), and we keep the basis \((t,s)\).
If \(z_s\ne0\), use the exact basis \((t,z)\) and write
\(s=S(t,z)\). In that case
\[
[L:\mathbb C(t,z)]<\infty,\quad
S_z=1/z_s\ne0,\quad S_z\ne2t,\qquad
J_{t,z,Q}=-a_0^4S_z/\rho\ne0.
\tag{15}
\]
The second inequality follows from the genuine unit kappa in (11).
The kernel of \(\partial_z\) is the same exact F_0. The symbol t
derivative in this basis is rebased at fixed z. It agrees with the
old derivative on F_0. The substitutions in (13) and every derivative
of S below are literal, not frozen coefficients.

All positive-X or positive-Q coefficients of the corresponding J
must vanish. Its constant coefficient may depend on the coefficient
parameters and is NEVER silently set to zero.

## 4. Zero transverse slope, zero offset

First suppose \(z_s=0\) and \(H=0\). Differentiate (13) in
\((t,s,Q)\), retaining the arbitrary function z(t) and arbitrary
C(t,s), L(t,s). The complete cubic-Q coefficient is
\[
[Q^3]J=L_s/t^2.
\]
Thus \(L_s=0\). The next complete coefficients, in the stated order,
are
\[
[XQ^2]J=K',\qquad
[X^2Q]J=-K+tK'-2R',\qquad
[X^2]J=-tL_t.
\tag{16}
\]
They imply \(K'=0,\ R'=-K/2,\ L_t=0\). There was no division by
z, z', C or one of their derivatives.

At these gates the ENTIRE determinant (14) is zero. One can also
see this without any remaining coefficient comparison: with
\(q=Q+tX\), the complete U and T become
\[
U=q^2+D,\qquad T=(2X^2-K)q+B_*X+L,
\]
where \(D=2tR+n_0\) has derivative
\(D'=t(K+2R')=0\), and \(B_*=2R+tK\) also has zero
derivative. Thus \(D,B_*,K,L\) are coefficient constants.
At fixed X their differentials are proportional. This contradicts
(14), for arbitrary remaining Y and C.

## 5. Zero transverse slope, nonzero offset

Now suppose \(z_s=0,\ H\ne0\), still in the original \((t,s)\)
basis. The coefficient \([Q^3]J=L_s/t^2\) gives \(L_s=0\).
The complete \(XQ^2\) coefficient then gives
\[
C_s=\frac H{2t}+\frac{t^2K'}H\in F_0.
\tag{17}
\]
Here \(C_s\) is the derivative of the CENTERED function C in (12),
not the derivative of the original c.
After (17), the full \(Q^2\) coefficient is zero exactly when
\[
K+tK'=\frac{2t^4(K')^2}{H^2}.
\tag{18}
\]
Its raw value is
\((-H^2K-H^2tK'+2t^4(K')^2)/(2Ht^2)\).

Differentiate the vanishing COMPLETE \(X^2\) coefficient in s.
Because \(z_s=L_s=0\) and \(C_s\in F_0\), the result is
\[
H(C_s)'=0.
\tag{19}
\]
This differentiates a coefficient required to be zero, not the
possibly nonconstant scalar value in (14). Since H is nonzero,
\(C_s=C_*\in\mathbb C\). Existing-difference integration of (17)
now gives
\[
K'=\frac{HC_*}{t^2}-\frac{H^2}{2t^3},\qquad
K=-\frac{HC_*}{t}+\frac{H^2}{4t^2}+K_0,\quad K_0\in\mathbb C.
\tag{20}
\]
Substitution in (18) yields
\[
K_0-2C_*^2+\frac{2HC_*}{t}-\frac{3H^2}{4t^2}=0.
\tag{21}
\]
This is impossible: t is transcendental over C and the constant
coefficient after multiplying by \(t^2\) is \(-3H^2/4\ne0\).
The argument retains \(C_*=0\) and does not divide by K'.

## 6. Nonzero transverse slope, zero offset

Suppose \(z_s\ne0,\ H=0\), and use (15). All occurrences of s in
(13) are now S(t,z). The COMPLETE \(Q^3\) coefficient is
\[
[Q^3]J=(t^2K'+L_z)/t^2.
\]
Thus
\[
L=-t^2K'z+L_0(t),\qquad L_0\in F_0.
\tag{22}
\]
Put \(A=K+2R'\) temporarily. The full \(X^2Q\) and \(XQ^2\)
coefficients give, respectively,
\[
(-A+tK')S_z-2t^2K'=0,\qquad
-A-2tK'+K'S_z=0.
\tag{23}
\]
Their zero-safe elimination implies
\[
K'(S_z-t)(S_z-2t)=0.
\tag{24}
\]
The factor \(S_z-2t\) is nonzero by kappa, not discarded by an
unproved slope assumption.

If \(K'=0\), (23) gives \(R'=-K/2\) and (22) gives \(L_z=0\).
The remaining \(Q^2\) coefficient gives \(L_t=0\).
The same complete-row factorization used in Section4 makes the
ENTIRE J zero. This contradiction covers this whole zero branch.

Assume instead \(K'\ne0\). Then \(S_z=t\), so
\[
S=tz+S_0,\quad S_0\in F_0,\qquad R'=-(K+tK')/2.
\tag{25}
\]
The complete \(Q^2\) and \(X^2\) coefficients respectively give
\[
L_t=K'C_z,\qquad L_t=-tK'S_0'.
\]
Use (22). Since z is transcendental over F_0, the z coefficient
of this last equation is \((t^2K')'=0\). Consequently
\[
\begin{gathered}
K'=d/t^2,\quad K=K_0-d/t,\quad d\in\mathbb C^*,\quad K_0\in\mathbb C,\\
R'=-K_0/2,\quad L_0'=-dS_0'/t,\qquad C_z=-tS_0'.
\end{gathered}
\tag{26}
\]
These are integrations of existing functions in F_0. No rational
description of that finite field has been imposed.

After (26), the full \(XQ\) coefficient is \(-dS_0'\). Hence
\(S_0'=0\), and \(C=C_0(t)\in F_0,\ L_0'=0\).
At this stage the ENTIRE scalar, with no premature equation for
its constant coefficient, is
\[
J=-\frac d2(K_0t-d+2tC_0')
             \left(X+\frac Qt\right)-\frac{d^2z}{2}.
\tag{27}
\]
In particular its X coefficient forces
\[
C_0'=\frac d{2t}-\frac{K_0}{2}.
\tag{28}
\]
This is impossible in the exact finite extension F_0/C(t).
For completeness, in characteristic zero the derivative on C(t)
has a unique extension to any finite algebraic extension. Its
commutation with all embeddings shows that differentiation
commutes with field trace. If \(n=[F_0:\mathbb C(t)]\), (28)
therefore makes the derivative of the rational function
\(\operatorname{Tr}_{F_0/\mathbb C(t)}C_0\) equal
\(nd/(2t)-nK_0/2\).
The derivative of a rational function has zero residue at every
finite pole: termwise differentiation of a Laurent expansion
cannot produce a nonzero \(t^{-1}\) coefficient. Here that residue
would be \(nd/2\ne0\), a contradiction.

The point \(t=0\) is used only in this rational-function trace
argument, not as an actual ambient fiber or as a deleted divisor.
The allowed parameter-dependent constant value \(-d^2z/2\) in
(27) was not required to vanish.

## 7. Nonzero transverse slope, nonzero offset

Finally suppose \(z_s\ne0,\ H\ne0\), in the exact basis (15).
Write \(B=K'\). As before the complete cubic coefficient gives
\[
L=-t^2Bz+L_0,\qquad L_0\in F_0.
\tag{29}
\]
Combining the full \(X^2Q\) and \(XQ^2\) coefficients, without
dividing by B, gives
\[
(2t-S_z)\{2t^2(K+2R')+2t^3B+H^2\}=0.
\]
By kappa the first factor is nonzero. The same two coefficients
then yield
\[
\begin{gathered}
R'=-(K+tB)/2-H^2/(4t^2),\\
C_z=\left(\frac H{2t}+\frac{Bt^2}H\right)S_z-\frac{Bt^3}H,\\
C=\left(\frac H{2t}+\frac{Bt^2}H\right)S-\frac{Bt^3}H z+C_0,
\qquad C_0\in F_0.
\end{gathered}
\tag{30}
\]
The t derivatives of these formulas include the derivatives of S,
B and C_0.

After (29),(30), the ENTIRE \(X^2\) coefficient is
\[
\frac{S_z}{2t^2}\left\{
(4Bt^3+2B't^4-H^2)S+
2Ht^2C_0'+HKt^2-2t^3L_0'\right\}.
\tag{31}
\]
The element S is transcendental over F_0 because \(S_z\ne0\).
Thus its coefficient and the remaining F_0 term both vanish:
\[
B'+2B/t=H^2/(2t^4),\qquad
C_0'=tL_0'/H-K/2.
\tag{32}
\]
Integrating the existing functions gives
\[
B=\frac d{t^2}-\frac{H^2}{2t^3},\qquad
K=K_0-\frac dt+\frac{H^2}{4t^2},\qquad d,K_0\in\mathbb C.
\tag{33}
\]
The value \(d=0\) is retained. No step divides by d or B.

Define the exact nonzero function
\[
\begin{aligned}
G&=K+tB-\frac{2B^2t^4}{H^2}\\
 &=K_0-\frac{2d^2}{H^2}+\frac{2d}{t}
                         -\frac{3H^2}{4t^2}\ne0.
\end{aligned}
\tag{34}
\]
Indeed \(4H^2t^2G\) is a complex polynomial in t whose constant
coefficient is \(-3H^4\ne0\). This is a field nonvanishing argument;
it does not remove its possible finite roots from the actual ring.

The full \(Q^2\) coefficient, with (29)--(33) retained, is
equivalent to
\[
S_z=t+\frac H Gz+\frac{Bt^2-2t^2L_0'/H}{G}.
\tag{35}
\]
Integrating in the exact z direction gives
\[
S=tz+\frac H{2G}z^2+
       \frac{Bt^2-2t^2L_0'/H}{G}z+S_0,\qquad S_0\in F_0.
\]
Substitute this entire expression and its actual t derivative in
the full \(XQ\) coefficient. Its coefficient of z is
\[
-\frac H G(L_0'-HB/2).
\tag{36}
\]
Thus \(L_0'=HB/2\), and
\[
S=tz+\frac H{2G}z^2+S_0,\qquad
S_t=z-\frac{HG'}{2G^2}z^2+S_0'.
\tag{37}
\]
In the remaining complete coefficient of Q, the coefficient of
\(z^2\) is now exactly
\[
\boxed{\frac{3H^2(4dt-3H^2)}{8t^3G}\ne0.}
\tag{38}
\]
This contradicts the required independence of the scalar from Q.
The numerator cannot vanish identically, including when d is zero,
since H is nonzero and t is transcendental over C. All lower
functions \(S_0,C_0,R,n_0,L_0\), with their required derivatives,
remain in the calculation. No residual scalar constant was
mistakenly set to zero.

## 8. Exhaustion, verification and scope

The alternatives \(z_s=0\) or \(z_s\ne0\), and \(H=0\) or
\(H\ne0\), are exhaustive. Sections4--7 contradict the genuine
nonzero scalar in every case. Hence the hypotheses (1)--(3)
are impossible:
\[
\boxed{\text{In the full512 sector, }[P^3]w_{\rm int}\ne0.}
\tag{39}
\]
This note does not settle the complementary nonzero cubic row.
It makes no ambient coordinate claim about z, Q, S, C or the
exact coefficient fields.

The complete514 and426 were read through EOF, and516's completed
two-branch proof is the explicit curvature input. Fresh1b7c08
reconstructs both COMPLETE Z normalization identities, the full Y
identity, the corrected n and h transports in (7),(10), and both
slope invariances. Freshc8d550 reconstructs the full zero-slope
scalar, its coefficient gates and the entire zero-offset endpoint.
Fresh0a1537 reconstructs all three complete rows (13) directly
from the original264 rows with every lower coefficient retained.
Freshf21360 reconstructs the nonzero-slope cubic and both high
coefficients, the complete integrated \(X^2\) expression (31), and
the complete remaining determinant (27). Fresh6f4b14 checks the
whole \(Q^2\) substitution, the \(XQ\) z coefficient (36) and the
terminal \(Qz^2\) coefficient (38), including actual t derivatives.
All reported residuals are zero.

Earlier independent outline checks are separate from author
verification: the peer calculations4397de,9a5a8a,576d9a,fd749d
reconstruct the full nonzero-slope/nonzero-offset chain from the
original rows; the root calculations085047,a2b45b reconstruct both
zero-offset branches, and a098bf,33985d reconstruct the zero-slope
nonzero-offset branch. Their conclusions were not used to omit
any written zero case. A saved-source audit remains separate from
these outline checks.

All saved checkers remained frozen and were neither executed,
imported, compiled nor rerun. No earlier source or canonical file
was edited. No recursive recertification of earlier recognition
ancestors, external expert verification, proof-assistant
certification, historical novelty or public submission is claimed.
