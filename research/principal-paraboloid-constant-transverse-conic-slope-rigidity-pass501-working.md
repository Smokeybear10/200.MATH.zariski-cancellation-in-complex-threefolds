# Slope rigidity in the constant transverse conic family

Working necessary result: retain the FULL actual principal chart264
and the transverse conic family of498 and500, in the alternative
\(\gamma=m_s/m^3\in\mathbb C^*\). Then the existing coefficient K
and the intrinsic affine slope l satisfy
\[
\boxed{
K'''=0,\qquad K\in\mathbb C[t]_{\le2},\qquad
l=L_c(\delta-1)-\frac{K''}{4},\quad L_c\in\mathbb C,
}
\tag{1}
\]
where \(\delta=1+ma\). The coefficient \(L_c\) may be zero.
The linear coefficient of theta is also fixed:
\[
\boxed{b=aK'+\frac{B'}{2\gamma}.}
\tag{2}
\]
Here B,K are the EXACT elements in
\(m^{-2}=B-2\gamma s\), \(k=K-1/(\gamma m)\).
No actual coordinate normalization is made. These conclusions do
not exclude or recognize this remaining conic family.

## 1. Full actual inputs and the constant-gamma alternative

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and gradient-minor units of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the exact parity/return theorem
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
Thus the original ring and slice are
\(\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}]\),
\(E=\partial_{u_{\rm glob}}\), with the entire initial kernel,
literal selected nonzero N, both actual returns and full scalar
of264, not just their leading formal equations.

Use the intrinsic affine parameter and exact coefficient field
\[
\begin{gathered}
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\quad
[L:\mathbb C(t,s)]<\infty,\\
\theta=aP^2+bP+c,\quad a\ne0,\quad
m=k_s\ne0,\quad h=m_s\ne0,\quad \delta=1+ma\ne0,\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{3}
\]
The original X has \(X=a_0u_{\rm glob}+x_0\). Neither its speed
nor \(\rho\) is replaced by one. Coefficient partials commute,
have joint constants C, and extend to fix P. All actual-ring and
original-slice requirements remain in force after this intrinsic
reparameterization.

The held necessary reduction
[498](principal-paraboloid-transverse-coupling-conic-reduction-pass498-working.md)
and initial-form rigidity
[500](principal-paraboloid-transverse-conic-initial-rigidity-pass500-working.md)
give, in the present alternative,
\[
\begin{gathered}
F_0=\ker_L\partial_s\text{ finite over }\mathbb C(t),\qquad
\gamma\in\mathbb C^*,\quad B,K\in F_0,\\
m^{-2}=B-2\gamma s,\qquad k=K-\frac1{\gamma m},
\qquad h=\gamma m^3,\\
y=lP+r,\qquad \delta_s=h\kappa\ne0,\qquad
dl\wedge d\delta=0,\quad \kappa\in L^*.
\end{gathered}
\tag{4}
\]
The exact t derivative on \(F_0\) has constants C. Primes denote
this derivative. No rationality of \(F_0\), L or l is assumed.
In particular l is permitted to be zero or complex.

For later use, the universal unit-multiplier identity from
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md)
is
\[
\mathcal A=y_t+\theta_Py_s+y_P^2
             =\kappa H_V^{\rm ev}.
\tag{5}
\]
The evaluated polynomial \(H_V^{\rm ev}\) is the full formal
V derivative of the genuine third potential, evaluated afterward.
The multiplier is a coefficient-field unit because of the full
scalar and genuine fourth-potential tangent minor. It is not an
arbitrary polynomial multiplier.

## 2. Exact parity fixes the linear theta coefficient

Put \(p=m_t\), allowing p to vanish, and differentiate (4):
\[
p=-\frac{B'm^3}{2},\qquad
k_t=K'-\frac{B'm}{2\gamma}.
\tag{6}
\]
The polynomial retained by327 is
\[
S=P^2+k_tP+m\theta
  =\delta P^2+\varepsilon P+mc,
\qquad \varepsilon=k_t+mb.
\tag{7}
\]
Center it only over the coefficient field:
\(P=P_0+\xi\), \(P_0=-\varepsilon/(2\delta)\).
The quadratic theta coefficient remains a, while y is still
affine. Thus its even quadratic coefficient is zero.327's exact
reflection criterion, including the reflection-fixed point, says
\[
0=-\frac a2\left(p-\frac{g_0h}{m}\right),
\qquad
g_0=2P_0+k_t=\frac{m(ak_t-b)}\delta.
\tag{8}
\]
Every denominator used here is nonzero by (3). Since a is nonzero,
(8) is equivalently
\[
p\delta=h(ak_t-b).
\tag{9}
\]
Substitute (6) and \(h=\gamma m^3\). The terms involving amB'
cancel, leaving exactly (2). No division by p, B', b or l has
occurred. The parity criterion also retains its nonzero constant
reflection coefficient; no claim is made that (2) alone implies
that entire criterion or any other actual-chart condition.

## 3. One full cubic coefficient and its evaluated gradient

For reconstruction, retain independent formal variables U,P,V and
the complete polynomial
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2+n_tP+n_sV,\\
G(U,P,V)&=\frac{\ell-(2P+k_t)U-F(P,V)}m,\\
H(U,P,V)&=U^2+F_PU+F_VG+H_3(k;P,V)+H_2(n;P,V)
                              -\ell_tP-\ell_sV.
\end{aligned}
\tag{10}
\]
The actual level is \(H(y,P,\theta)=h_0\in L\). The Taylor forms
have their usual factorial denominators; in particular
\[
H_3(k;P,V)=\frac{k_{ttt}}6P^3+\frac{m_{tt}}2P^2V
                      +\frac{h_t}2PV^2+\frac{h_s}6V^3.
\tag{11}
\]
All n,ell and moving-level coefficients remain. Differentiation
of the exact family (4),(6) gives
\[
\begin{aligned}
h_s&=3\gamma^2m^5,\qquad h_t=3\gamma m^2p,\\
m_{tt}&=-\frac{B''m^3}{2}-\frac{3B'm^2p}{2},\\
k_{tt}&=K''-\frac{B''m+B'p}{2\gamma}.
\end{aligned}
\tag{12}
\]
These are identities of the exact coefficient field, not
independently frozen Taylor coefficients.

Substitute \(y=lP+r\), theta from (3), b from (2), and (12) in
the entire polynomial (10). Its fourth coefficient is
\[
[P^4]H(y,P,\theta)
 =-\frac a2\left(K''\gamma m^2+3a\gamma m^2n_s
                         -a n_{ss}+4\gamma lm^2\right)=0.
\tag{13}
\]
This calculation includes the quartic term of evaluated G and its
product with \(F_V\). It is not a truncated replacement for H.
Equivalently,
\[
n_{ss}=3\gamma m^2n_s+\frac{\gamma m^2}{a}(K''+4l).
\tag{14}
\]
Taking the formal V derivative of the complete H BEFORE evaluating
and using (14) then yields
\[
\boxed{[P^2]H_V^{\rm ev}=\frac{\gamma m^2}{2}(K''+4l).}
\tag{15}
\]
Terms involving B',B'',b,c,r and lower potentials cancel in this
coefficient. No assumption that its value is nonzero has been made.

## 4. The exact coefficient basis forces K to be complex quadratic

As y is affine, the entire expression on the left of (5) has
quadratic coefficient
\[
[P^2]\mathcal A=2a l_s.
\tag{16}
\]
The contributions \(y_t\) and \(y_P^2\) have smaller degree;
the displayed term is exactly the quadratic part of
\(\theta_Py_s\). Equations (5),(15),(16) give
\[
2a l_s=\kappa\frac{\gamma m^2}{2}(K''+4l).
\tag{17}
\]

Because \(\delta_s\ne0\), the pair (t,delta) is an exact
separating coefficient basis. From (4),
\(\partial_t|_\delta l=0\), and
\(l_s=l_\delta\delta_s=l_\delta\gamma m^3\kappa\).
Canceling only the nonzero \(\gamma,m,\kappa\) in (17) proves
\[
\boxed{4(\delta-1)l_\delta=K''+4l.}
\tag{18}
\]
Here \(\delta-1=ma\ne0\); the equation is still valid when either
side vanishes. The exact commuting partials in this basis are
\(\partial_\delta|_t=\delta_s^{-1}\partial_s\) and
\(\partial_t|_\delta=\partial_t-(\delta_t/\delta_s)\partial_s\).
In particular the latter acts on K and all its derivatives as the
original t partial, because \(K\in F_0\).

Apply \(\partial_t|_\delta\) to (18). It kills l, delta and
\(l_\delta\), so \(K'''=0\). Repeated subtraction of the explicit
quadratic antiderivative, in the exact field \(F_0\), then shows
that K has complex coefficients and degree at most two. This does
not require \(F_0=\mathbb C(t)\).

Finally define the EXISTING element
\[
L_c=\frac{l+K''/4}{\delta-1}\in L.
\tag{19}
\]
Equation (18) gives \((L_c)_\delta=0\). Also
\(\partial_t|_\delta L_c=0\), using \(K'''=0\) and
\(\partial_t|_\delta l=0\). These two coefficient partials span
the original ones, whose joint constants are C. Therefore
\(L_c\in\mathbb C\), proving (1). The possibility \(L_c=0\),
including a zero or complex constant l, has not been discarded.

## 5. Verification and precise remaining scope

The entire current264,296,327,494,498 and500 sources were read for
the selected inputs.500 was revalidated at
SHA b599267f7c3465fff510a9294d5edf06728112dcad9c52e9911d86255845a139.
Fresh unsaved dbc043 rebuilt the complete formal H and its formal
V derivative, then verified the parity identity (9), full fourth
coefficient (13) and complete evaluated coefficient (15), all with
zero residuals. The field integrations and all zero-coefficient
cases are supplied by the written argument.

The new conclusions are exactly (1),(2), with (14) also retained
as a necessary lower-potential identity. B, n, ell, a, c, r and the
remaining full scalar and fourth-level equations are not solved.
No complex ambient transformation removes K or rescales gamma in
this note, and no coefficient-field change is promoted to such a
transformation. The nonconstant-gamma alternative of500, zero-ms
branches, delta-zero boundary, other projected curves and arbitrary
actual entry remain outside this result. It is not a conic
exclusion, recognition theorem or proof of general cancellation.
All saved checkers remain frozen; none was executed, imported,
compiled or rerun. No earlier source or canonical file was edited.
