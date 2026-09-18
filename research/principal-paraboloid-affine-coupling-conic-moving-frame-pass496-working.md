# An exact moving frame for affine coupling and a nonlinear conic

Working result: retain the FULL actual principal chart264 and the
nonlinear conic assumptions
\[
m=k_s\notin\mathbb C,\qquad m_s=m_{tt}=0,\qquad
P=\sigma,\quad\deg_v\sigma=1,\qquad
\theta=aP^2+bP+c,\quad a(1+ma)\ne0.
\]
The complete scalar and the unit multiplier494 force explicit
coefficient integrations and an exact moving polynomial row frame.
Its derivative correction is essential. In particular,
\[
\boxed{f''''=6a h''.}
\tag{1}
\]
The functions f,h are defined from the original coupling and first
potential below; they are not freely chosen replacements.
If additionally \(a_t=0\), then \(h''=0\), and the moving frame
becomes an ACTUAL complex polynomial coordinate frame with intrinsic
degrees \((2,1,1)\). No exclusion or recognition of this branch is
claimed here. The case \(a_t\ne0\) remains a moving-frame problem.

## 1. Exact actual inputs, coefficient fields and parameter speed

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine third and fourth levels and gradient-minor units of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the all-X return and parity result of
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad X=a_0u_{\rm glob}+x_0,
\quad a_0\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad Nv=1,\quad
O=L[v]=L[y,z_0,w_{\rm int}]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w_{\rm int}),\qquad
L[X,Y,Z,W]=L[X,v].
\end{gathered}
\tag{2}
\]
Both returns, the original global slice and the literal selected
partial remain assumptions. No unit condition on \(a_0\) in A is
added. The exact coefficient partials on L commute and have joint
constant field C.

Since sigma is affine nonconstant, use only the intrinsic change
\[
P=\sigma,\qquad O=L[P],\qquad NP=\rho\in L^*.
\tag{3}
\]
The coefficient partials extend to fix P. At fixed actual X the full
calibrated determinant is therefore
\[
J(X,P)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-a_0^4/\rho\in L^*.
\tag{4}
\]
One does not set \(\rho=1\), or identify P with the original slice.

Let \(F_0=\ker_L\partial_s\). As proved in494, this is a finite
extension of C(t), with t-derivative constants exactly C. No
identification \(F_0=\mathbb C(t)\) or \(L=F_0(s)\) is made.
The assumptions on m give
\[
p=m_t\in\mathbb C^*,\qquad m=pt+d,\quad d\in\mathbb C,
\qquad k=ms+f,\quad f\in F_0.
\tag{5}
\]
Indeed p has both coefficient derivatives zero, and p cannot vanish
because m is noncomplex. Primes below mean the exact t derivative
on \(F_0\), holding s fixed in L.

The monic surface \(H-h_0\) and the genuine fourth level \(Q-q_0\)
are retained, including both moving levels. No factorization of H
is assumed or used. Thus the argument applies in the irreducible-H
frontier without importing the separate reducible-surface endpoints.

## 2. Parity, the unit multiplier and the first scalar integrations

Put \(\delta=1+ma\ne0\). The polynomial
\(P^2+k_tP+m\theta\) has exact degree two. Since \(m_s=0\),327
eliminates the cubic term of y and determines its quadratic term:
\[
\theta=aP^2+bP+c,\qquad
y=-\frac p2\theta+\lambda P+r,\qquad a\ne0.
\tag{6}
\]
The functions b,c,lambda,r initially lie in L. The complete unit
multiplier result
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md)
then gives, WITHOUT dividing by \(m_{tt}\),
\[
a_s=0,\qquad a\in F_0^*,\qquad
\kappa=\frac{m}{2p}(a'-2pa^2+2ab_s)\in L^*.
\tag{7}
\]
Here kappa is the ratio of the actual nonzero scalar (4) to the
genuine primitive tangent minor from296. It need not be complex.
This is where the full fourth potential and its unit-minor conclusion
enter. Neither moving level is replaced by zero.

For direct scalar reconstruction the literal rows are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w_{\rm int}+\theta X+sX^2,\\
mw_{\rm int}
 &=\ell-(2P+k_t)y-\frac{f''}{2}P^2-pP\theta-n_tP-n_s\theta.
\end{aligned}
\tag{8}
\]
All coefficient derivatives of these rows are retained. Expanding
the complete determinant (4), before imposing a form on n, gives
\[
[X^2P^3]J=-a^2(p^2-2n_{ss}).
\tag{9}
\]
Hence \(n_{ss}=p^2/2\). Integrating by subtracting an explicit
polynomial in s puts
\[
n=\frac{p^2}{4}s^2+\left(\frac{pf'}2-h\right)s+n_0,
\qquad h,n_0\in F_0.
\tag{10}
\]
The notation h in (10) is a coefficient function, not the third
level \(h_0\). The exact integration only says that the remaining
s derivative is zero; it does not assume a rational constant field.

After (10), the next full coefficient is
\[
[X^2P^2]J=
\frac{3ak_tp^2-3af''mp+6am n_{ts}-6an_sp-3f''p+mf'''-12p\lambda}
     {2m}.
\tag{11}
\]
Define coefficient functions in \(F_0\) by
\[
K=ph-mh',\qquad
A_c=\frac{K}{2p},\qquad
B_c=-\frac{f''}{4}+\frac{mf'''}{12p}.
\tag{12}
\]
Using \(n_s=p^2s/2+pf'/2-h\), the vanishing of (11) is exactly
\[
\lambda=A_ca+B_c\in F_0.
\tag{13}
\]
In particular \(\lambda_s=0\). Coefficient derivatives of (13),
not independent frozen jets, must be used in the next calculation.

## 3. The two remaining high coefficients and the exact r integration

With (5)--(13) substituted, the full \(XP^4\) coefficient cancels
identically. The full next coefficient, retaining all lower
coefficients and their first derivatives, is
\[
\begin{aligned}
[XP^3]J=\frac1{6m}\bigl(&6a^2Kp-12ab_sK+3af''p^2-af'''mp\\
 &-12ah'p-6ah''m+24ap r_s+mf''''\bigr).
\end{aligned}
\tag{14}
\]
This gives r_s without dividing by any possibly zero lower
coefficient. After making exactly that substitution in the entire
\(P^4\) coefficient at X=0, the result is
\[
\begin{aligned}
[P^4]J
 &=\frac{(6ah''-f'''')(2pa^2-2ab_s-a')}{12a}\\
 &=-\frac{p\kappa}{6am}(6ah''-f'''').
\end{aligned}
\tag{15}
\]
Every displayed denominator and kappa is nonzero under the retained
hypotheses. Since the scalar (4) has no P dependence, (15) proves
(1), including the cases \(h''=0\) and \(f''''=0\). No division by
either of those functions occurs.

For clarity, (11),(14),(15) are coefficient identities from the
complete literal rows (8), not equations obtained after deleting
lower-potential terms. Terms in c,ell and their derivatives cancel
in these particular coefficients; those functions remain present
in the complete map and in every later scalar equation.

Set
\[
D_c=-\frac{paA_c}{2}+\frac{pB_c}{2}+\frac{h'}2.
\tag{16}
\]
Substitution of (1) in (14) now gives precisely
\[
r_s=A_cb_s+D_c,\qquad
r=A_cb+D_cs+r_0,\quad r_0\in F_0.
\tag{17}
\]
Again this is an exact-field integration by subtraction.
Two useful derivative identities, with all moving coefficients kept,
are
\[
A_c'=-\frac{mh''}{2p},\qquad
\lambda'=A_ca'-\frac{f'''}6.
\tag{18}
\]
The second uses (1); it is not valid for arbitrary independent f,h,a.

## 4. A complete polynomial row frame over the coefficient field

Define, at fixed original X,
\[
\begin{aligned}
U&=Z+\frac{2d}{p}Y,\\
V&=-\frac2pY-aU,\\
T&=W+\frac2p\left(X+\frac{h'}p\right)Y+\frac{f'''}{6p}U.
\end{aligned}
\tag{19}
\]
The first row U is already an actual polynomial coordinate because
d,p are complex. In general V and T are only coefficient-field
polynomial expressions. Their coefficients a,h',f''' must NOT be
treated as complex or as constants for t differentiation.

The exact inverse is
\[
Y=-\frac p2(V+aU),\qquad
Z=U-\frac{2d}{p}Y,\qquad
W=T-\frac2p\left(X+\frac{h'}p\right)Y-\frac{f'''}{6p}U.
\tag{20}
\]
The row Jacobian of (19) with respect to (Y,Z,W), with coefficient
functions held fixed, is \(2/p\). Both inverse orders are polynomial
over \(F_0[X]\); this alone is not an actual complex coordinate
change.

The full intrinsic rows have the form
\[
U=P^2+uP+U_0,\qquad V=v_1P+V_0,\qquad T=w_1P+T_0,
\tag{21}
\]
where
\[
\begin{aligned}
u&=k_t+\frac{2m}{p}(X+\lambda),\qquad u_s=p,\\
U_0&=\frac{2m}{p}r+n+kX+\left(t^2+\frac{2dt}{p}\right)X^2,\\
v_1&=b-ak_t-\frac{2(1+ma)}p(X+\lambda),
       \qquad (v_1)_s=b_s-pa,\\
V_0&=c-\frac{2r}{p}-\frac{2t}{p}X^2-aU_0,\\
w_1&=\frac2p\left(X+\frac{h'}p\right)(X+\lambda)
       +\frac{f'''f'}{6p}
       +\frac{f'''m(X+\lambda)}{3p^2}
       -\frac{2r_0+f'\lambda+n_0'}m,\\
T_0&=\frac{hc+\ell-k_tr}{m}+cX+sX^2
       +\frac2p\left(X+\frac{h'}p\right)
                    \left(-\frac{pc}{2}+r+tX^2\right)
       +\frac{f'''}{6p}U_0.
\end{aligned}
\tag{22}
\]
These are full rows, with no omitted coefficient. In particular
\[
w_1\in F_0[X],\qquad (w_1)_s=0,\qquad
\deg_X w_1=2,\quad [X^2]w_1=2/p\ne0.
\tag{23}
\]
The cancellations in w1 use the entire r expression (17).
The constant-P row T0 includes \(2tX^3/p\). Dropping that term
would change subsequent scalar equations even in the constant-a
case. No root of w1 is excluded by (23).

## 5. Exact derivative corrections and one more scalar coefficient

Write the original row vector in the order (Y,U,W) as
\[
\begin{pmatrix}Y\\U\\W\end{pmatrix}
=eU+f_1V+gT,\qquad
\begin{aligned}
e&=\begin{pmatrix}-pa/2\\1\\a(X+h'/p)-f'''/(6p)\end{pmatrix},\\
f_1&=\begin{pmatrix}-p/2\\0\\X+h'/p\end{pmatrix},\qquad
g=\begin{pmatrix}0\\0\\1\end{pmatrix}.
\end{aligned}
\tag{24}
\]
Using (1), these coefficient columns satisfy
\[
e'=a'f_1,\qquad f_1'=(h''/p)g,\qquad
\det(e,f_1,g)=p/2.
\tag{25}
\]
They have zero s and P derivatives. Subtracting the constant multiple
\(2dY/p\) from U returns Z without changing the determinant. Thus
the ENTIRE original scalar is
\[
\boxed{
J=\frac p2\det\left(dU,\ dV+a'U\,dt,
                         \ dT+\frac{h''}{p}V\,dt\right),
}
\tag{26}
\]
in the basis \((dt,ds,dP)\), with X fixed. The determinant of plain
\((dU,dV,dT)\) would generally be wrong.

Using (21)--(23), the three corrected rows in (26) have entries
\[
\begin{pmatrix}
u_tP+(U_0)_t &pP+(U_0)_s &2P+u\\
a'P^2+((v_1)_t+a'u)P+(V_0)_t+a'U_0
 &(v_1)_sP+(V_0)_s &v_1\\
((w_1)_t+(h''/p)v_1)P+(T_0)_t+(h''/p)V_0
 &(T_0)_s &w_1
\end{pmatrix}.
\tag{27}
\]
Consequently its exact cubic-P coefficient is
\[
\boxed{
-pa'w_1+2a'(T_0)_s
       -2(v_1)_s\left((w_1)_t+\frac{h''}{p}v_1\right)=0.
}
\tag{28}
\]
This is the coefficient before the nonzero factor p/2 in (26).
All lower intercept derivatives remain in (27); only those not
contributing to the indicated coefficient disappear from (28).

For the other boundary, if \(a'\ne0\), (28) can be integrated
without dividing by \((v_1)_s\):
\[
T_0=\frac p2w_1s+\frac{(w_1)_t}{a'}v_1
       +\frac{h''}{2pa'}v_1^2+C_0,\qquad C_0\in F_0[X].
\tag{29}
\]
Indeed subtracting the displayed expression has zero s derivative,
coefficient by coefficient in X. This remains valid if
\((v_1)_s=0\), and makes no rationality claim about \(C_0\).
The remaining full scalar equations are not solved by (29).

## 6. Constant-a boundary: an actual frame, with every root retained

Suppose \(a'=0\). Since \(a\in F_0\), this means \(a\in\mathbb C^*\).
Equations (7),(22) give
\[
\kappa=\frac{ma}{p}(v_1)_s\ne0,
\qquad (v_1)_s\ne0.
\tag{30}
\]
Thus the possibly zero \((v_1)_s\) boundary is impossible in this
subcase; it was not discarded by division in the general argument.
Equation (28) now gives
\[
(w_1)_t+(h''/p)v_1=0.
\tag{31}
\]
Differentiate (31) in s. By (23) and commutation of the exact
partials, its first term has zero derivative. As \(h''\in F_0\),
the result is \(h''(v_1)_s/p=0\). Equation (30) forces
\[
\boxed{h''=0,\qquad f''''=0,\qquad (w_1)_t=0.}
\tag{32}
\]
Therefore \(h',f'''\in\mathbb C\), and (19),(20) now have complex
polynomial coefficients, including their X dependence. They give
the genuine actual equality
\[
\mathcal B=\mathbb C[X,U,V,T],\qquad
w_1\in\mathbb C[X],\quad \deg_Xw_1=2.
\tag{33}
\]
No division by w1 or specialization away from its roots was used.
In particular (33) does not assert that w1 is a unit in C[X].
Its zero polynomial case is impossible by (23), but every finite
root remains available in later actual-fiber arguments.
Nor is a claim made that this new frame still has the old E-degree
profile: T contains an actual XY term.

There is a useful exact LND consequence, not a recognition theorem.
Extend N to \(A[u_{\rm glob}]\) by \(Nu_{\rm glob}=0\), and put
\[
\Delta=a_0N-(NX)E.
\tag{34}
\]
This is a polynomial locally nilpotent derivation of the actual
ring, fixing X. To check local nilpotence globally, write
\(NX=Nx_0\in A\). On A it is \(a_0N\), while
\(\Delta u_{\rm glob}=-Nx_0\), so repeated application gives
\(-a_0^{j-1}N^jx_0\) for j at least one. These expressions eventually
vanish, as do iterates on any finite set of A generators.
At fixed X, in the localized ring \(L[X,P]\), it acts as
\(a_0\rho\partial_P\). Therefore the ACTUAL rows (33) satisfy
\[
\Delta^2V=\Delta^2T=0,\qquad
\Delta^2U=2(a_0\rho)^2\ne0,
\quad \Delta V=a_0\rho v_1,
\quad \Delta T=a_0\rho w_1.
\tag{35}
\]
These equalities do not assume that the displayed speed is an
actual unit. They follow in an injective localization from a
globally polynomial derivation. No generic-field invariant from
this frame is promoted here to an actual invariant coordinate.

## 7. Verification and retained frontier

The full current264,296,327 and494 sources were read, and494 was
revalidated at SHA b2d675fbf721954b79490f79b31c9165d4f4393f101e1af65c75953a6d546c37.
Fresh unsaved symbolic reconstruction checked the complete
coefficients (11),(14),(15), their exact integrations and (18),
all zero residuals. A separate reconstruction checked the full
row coefficients (22), both inverse orders (20), the frame Jacobian,
the connection (25) and the complete cubic coefficient (28).
The scalar calculation kept c,ell and all relevant first jets,
and did not impose any equation on the coefficient-field value
\(-a_0^4/\rho\).

This note proves necessary q=0 coefficient identities and the stated
constant-a actual-frame reduction. It does not solve the remaining
lower scalar, prove a conic exclusion, or supply a recognition
endpoint. In particular (29) leaves the moving-a branch open,
and (33)--(35) alone do not close the constant-a branch.
The separate delta-zero case and arbitrary principal-chart entry
are not covered. All saved checkers remain frozen: none was
executed, imported, compiled or rerun. No earlier source or
canonical file was changed.
