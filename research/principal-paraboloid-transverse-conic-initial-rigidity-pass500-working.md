# Initial-form rigidity of the transverse conic family

Working necessary result: retain the FULL actual principal chart264,
affine nonconstant intrinsic sigma, quadratic theta, quadratic
\(S=\sigma^2+k_t\sigma+m\theta\), and \(m_s\ne0\).
The reciprocal-square-root family498 has a much more restricted
time coefficient:
\[
\boxed{\gamma\in\mathbb C^*\quad\hbox{or}\quad
       \gamma=\frac{C}{(t-\tau)^2},\qquad C\in\mathbb C^*,\ \tau\in\mathbb C.}
\tag{1}
\]
Here gamma is the EXISTING function \(m_s/m^3\), not an adjoined
root or an ambient coordinate. The two alternatives are disjoint.
In the constant-gamma alternative, y is affine in the intrinsic
parameter and its slope is algebraic over \(\mathbb C(1+ma)\).
These are necessary restrictions, not a full conic exclusion,
coordinate recognition, or a solution of cancellation.

## 1. Retained actual hypotheses and the exact multiplier

Retain every hypothesis and conclusion of
[498](principal-paraboloid-transverse-coupling-conic-reduction-pass498-working.md),
including all of its actual264/296/327 inputs and the universal
first part of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=A[u_{\rm glob}]=\mathbb C[X,Y,Z,W],\quad E=\partial_{u_{\rm glob}},
\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad O=L[P],\\
\theta=aP^2+bP+c,\quad a\ne0,\quad \delta=1+ma\ne0,
\quad h=m_s\ne0.
\end{gathered}
\tag{2}
\]
The original global slice, entire weighted initial kernel, literal
selected partial, both actual returns and nonzero full scalar
\(-a_0^4/\rho\) remain assumptions. X is transcendental over L(P).
The exact coefficient partials commute and have joint constants C.

Write the already proved498 conclusions as
\[
\begin{gathered}
y=eP^2+lP+r,\qquad h_s=3h^2/m,\\
F_0=\ker_L\partial_s\text{ finite over }\mathbb C(t),\qquad
\gamma=h/m^3\in F_0^*,\\
m^{-2}=B_0-2\gamma s,\qquad k=K_0-1/(\gamma m),
\qquad B_0,K_0\in F_0.
\end{gathered}
\tag{3}
\]
Neither exact coefficient field is assumed rational. Primes mean
the exact t derivative on F0, whose constants are C.

The full494 multiplier equations give
\(\mathcal B_1=-\kappa f\), with \(f=H_U^{\rm ev}\) and
\(\kappa\in L^*\). After the cubic y term has been excluded,
the COMPLETE cubic coefficients are
\[
[P^3]\mathcal B_1=2a(a_s+ha/m),\qquad [P^3]f=-2ha/m.
\tag{4}
\]
Thus
\[
\boxed{\delta_s=ma_s+ha=h\kappa\ne0.}
\tag{5}
\]
All divisions here use nonzero a,m,h. In particular (t,delta) is
a separating coefficient basis. This is not an ambient coordinate
assertion.

## 2. One coefficient of the entire cubic level fixes the quadratic slope

Put \(p=m_t\), allowing p to be zero. The full literal formal
polynomial used in498 is
\[
\begin{aligned}
F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2+n_tP+n_sV,\\
G(U,P,V)&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H(U,P,V)&=U^2+F_PU+F_VG+H_3(k;P,V)+H_2(n;P,V)
                         -\ell_tP-\ell_sV.
\end{aligned}
\tag{6}
\]
Its ACTUAL level is \(H(y,P,\theta)=h_0\in L\).
Using only (3), the coefficient of P to the fifth power is
\[
[P^5]H(y,P,\theta)
   =-\frac{a}{2m}(3ahp-am h_t+4eh)=0.
\tag{7}
\]
For direct reconstruction, the highest part of H3 is
\(k_{ttt}P^3/6+m_{tt}P^2V/2+h_tPV^2/2+h_sV^3/6\).
All lower n,ell and moving-level terms remain in (6); none has
been frozen to obtain (7).

Since \(h=\gamma m^3\), at fixed s one has
\(h_t=\gamma' m^3+3\gamma m^2p\). Substitution in (7) gives
\[
\boxed{e=\frac{(\delta-1)\gamma'}{4\gamma}.}
\tag{8}
\]
This identity includes gamma-prime zero and p zero. The only
divisors are nonzero a,m,h,gamma; \(\delta-1=ma\ne0\).

## 3. Actual locally nilpotent derivation and the initial-form test

Extend N to A[u_glob] by killing u_glob and define
\[
\Delta=a_0N-(NX)E.
\tag{9}
\]
This preserves the ACTUAL polynomial ring and fixes X. Since
\(NX=Nx_0\), its restriction to A is a0N, and
\(\Delta^j u_{\rm glob}=-a_0^{j-1}N^jx_0\) for j at least one.
Thus it is locally nilpotent on the actual ring. In L[X,P] it is
\(g_0\partial_P\), with \(g_0=a_0\rho\in L^*\). No claim that
g0 is an actual polynomial unit is needed.
Localize only at the nonzero elements of C[X], obtaining
\[
R_X=\mathbb C(X)[Y,Z,W]=\mathbb C(X)^{[3]}.
\tag{10}
\]
Delta is a nonzero locally nilpotent C(X)-derivation there.

We use the following elementary initial-form test. If the three
actual coordinates have positive Delta-degrees d1,d2,d3 and
intrinsic leading coefficients c1,c2,c3 in L(X), their initial
images may be represented by
\(c_i g_0^{d_i}\Xi^{d_i}\), where Xi is independent of L(X).
If those three images are algebraically independent over C(X),
the weighted initial map is injective. The top weighted part of
every nonconstant polynomial then has nonzero image and positive
Delta-degree. This would force \(\ker_{R_X}\Delta=\mathbb C(X)\).
That is impossible: localizing at the nonzero last derivative of
any positive-degree element supplies a local slice, so the
invariant fraction field has transcendence degree two over C(X).
The slice construction is also the standard characteristic-zero
[slice theorem](https://arxiv.org/html/1701.03635v1), Theorem2.1.

The initial-form test concerns this ACTUAL polynomial ring, not
an arbitrary coefficient-field polynomial parametrization.

## 4. Nonconstant gamma forces an inverse square

Suppose \(\gamma'\ne0\). Formula (8) makes e nonzero. From the
literal full rows in494, the leading coefficients are
\[
[P^2]Y=e,\qquad [P^2]Z=z_2=2te+\delta,\qquad
[P^4]W=w_4=-\frac{ha^2}{2m}=-\frac\gamma2(\delta-1)^2.
\tag{11}
\]
The last coefficient comes from the full G in (6); its quartic
term cannot be discarded. Both e and w4 are nonzero.
Also z2 is nonzero: putting q_gamma=gamma-prime/(4gamma),
\(z_2=(1+2tq_\gamma)\delta-2tq_\gamma\). If it vanished,
differentiation in s and (5) would give \(1+2tq_\gamma=0\),
after which z2 would equal one. Thus the ACTUAL Delta-degrees
are exactly (2,2,4).

Their two degree-zero initial ratios are
\[
R=\frac{z_2}{e}=2t+\frac{4\gamma\delta}{\gamma'(\delta-1)},
\qquad S=\frac{w_4}{e^2}=-\frac{8\gamma^3}{(\gamma')^2}\in F_0^*.
\tag{12}
\]
One has
\[
R_s=-\frac{4\gamma\delta_s}{\gamma'(\delta-1)^2}\ne0.
\tag{13}
\]
If S-prime were nonzero, the (t,s) Jacobian of R,S would be
\(-R_sS'\ne0\). In characteristic zero this makes them
algebraically independent over C, and hence over C(X), since X
is transcendental over L. The field of the three initial images
contains R,S and the additional element \(g_0^2e\Xi^2\), which
is transcendental over L(X). Those images would be algebraically
independent, contradicting Section3. Therefore S-prime is zero.

Differentiating its exact expression gives
\[
0=S'=\frac{8\gamma^2}{(\gamma')^3}
                   \{2\gamma\gamma''-3(\gamma')^2\}.
\tag{14}
\]
Define the EXISTING element \(T_\gamma=-2\gamma/\gamma'\in F_0^*\).
Equation (14) implies \(T_\gamma'=1\). Thus
\(T_\gamma=t-\tau\), with tau in C. Furthermore
\((\gamma T_\gamma^2)'=0\), so
\[
\gamma T_\gamma^2=C\in\mathbb C^*.
\tag{15}
\]
This proves the nonconstant alternative of (1) without adjoining
a root or assuming F0 rational. It does not constrain B0,K0 in
(3) to be complex functions of any specified degree.

## 5. Constant gamma and the affine slope

If \(\gamma'=0\), then \(\gamma\in\mathbb C^*\), and (8) gives
e=0. Now y=lP+r, and the ACTUAL Delta-degrees are exactly (1,2,4):
\[
[P]Y=X+l,\qquad [P^2]Z=\delta,\qquad
[P^4]W=-\gamma(\delta-1)^2/2.
\tag{16}
\]
The first coefficient cannot vanish in L(X), even when l is zero
or complex. The other coefficients are nonzero by (2).
Put
\[
R_0=\frac\delta{(X+l)^2},\qquad
S_0=\frac{-\gamma(\delta-1)^2}{2(X+l)^4},\qquad
H_0=\frac{S_0}{R_0^2}=-\frac{\gamma(\delta-1)^2}{2\delta^2}.
\tag{17}
\]
Here H0 is just an initial ratio, not the genuine third level h0.
Its derivative as a rational function of delta is
\(-\gamma(\delta-1)/\delta^3\ne0\).
With coefficient differentials at fixed X,
\[
dR_0\wedge dH_0
 =-\frac{2\delta}{(X+l)^3}\frac{dH_0}{d\delta}
                                      \,dl\wedge d\delta.
\tag{18}
\]
If the last wedge were nonzero, R0,H0, and hence R0,S0, would
be algebraically independent over C(X). Their initial images
would contradict Section3 exactly as before. Thus
\[
\boxed{dl\wedge d\delta=0.}
\tag{19}
\]
Since delta_s is nonzero, (19) says \(\partial_t|_\delta l=0\).
Equivalently l is algebraic over C(delta), by the characteristic-zero
differential criterion for algebraic dependence. No rationality,
nonzero slope, or complex constancy of l is asserted.

## 6. Verification and unresolved scope

Complete held494 and498 were read before this continuation.
Fresh unsaved root9f0213, completedc58125, rebuilt the full H,
its evaluated formal derivatives and the complete leading
multiplier coefficients. Fresh acef00 independently reconstructs
the whole fifth coefficient (7), its substitution (8), the exact
ratio derivative (13), the ODE factor (14) and both integrations
(15). All corresponding residuals are zero. The actual-ring
and invariant-field licenses are the written argument, not a
numerical test or bounded search. Independent reviews are
recorded separately in the research ledger.

This restricts the transverse-coupling conic family498, including
its zero time derivative. It leaves the lower potentials, both
time-coefficient alternatives, all-X realization and recognition
open. The m_s=0 and delta-zero sectors are separate. No arbitrary
chart-entry theorem, general cancellation proof, historical novelty,
human expert review or proof-assistant certification is claimed.
All saved checkers remain frozen; none was executed, imported,
compiled or rerun. No earlier mathematical source was edited.
