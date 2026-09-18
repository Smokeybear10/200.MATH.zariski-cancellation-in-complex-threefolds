# A higher-slope bound on the first intercept

Working result: in the FULL actual principal chart264, with nonzero
coupling and affine nonconstant intrinsic sigma, a theta of intrinsic
degree at least three has degree at least that of y:
\[
 \boxed{\deg_P\theta\ge3\quad\Longrightarrow\quad
        \deg_Py\le\deg_P\theta,\qquad P=\sigma.}
\tag{1}
\]
The zero polynomial y is included by taking its degree to be minus
infinity. The proof uses the genuine monic third level and the
universal coefficient-field multiplier from494. It does not use
327's quadratic parity statement or assume that m_s vanishes.

This is a necessary degree restriction, not recognition or exclusion
of the remaining higher-theta sector. It supplies neither an actual
coordinate change nor a bound on coefficient-field complexity.

## 1. Exact actual inputs and derivative conventions

Retain EVERY actual hypothesis of the fully read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and scalar identities of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the universal multiplier result in Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular
\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad E=\partial_{u_{\rm glob}},
 \quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\quad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the FULL initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
 L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\quad m=k_s\ne0,\quad
 \deg_v\sigma=1,\quad P=\sigma,\quad NP=\rho\in L^*,\\
 O=L[P]=L[y,\sigma,\theta],\quad
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w).
 \end{gathered}
\tag{2}
\]
Here z_int is the literal original Z-intercept, namely Z at X=0;
it is not the corrected expression obtained by subtracting 2ty.
Both actual returns, the original global slice and the selected
literal partial remain required. The original slice is not assumed
equal to X/a_0. All coefficient partials are the exact commuting
extensions from C(t,s) to L. They fix P after this intrinsic affine
reparameterization. No rationality of L is assumed.

The literal coordinates and first two potentials are
\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-\mathcal F(P,\theta),\\
 \mathcal F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
 J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
 \end{aligned}
\tag{3}
\]
Here the potential n is an element of L. We use N_theta for
the degree of theta below, to avoid confusing that integer with n.

With U,P,V independent formal variables, set
\[
 \begin{aligned}
 \mathfrak g(U,P,V)&=
       \frac{\ell-(2P+k_t)U-\mathcal F(P,V)}m,\\
 H&=U^2+\mathcal F_PU+\mathcal F_V\mathfrak g
        +H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV,\\
 H(y,P,\theta)&=h_0\in L.
 \end{aligned}
\tag{4}
\]
The Taylor terms are the exact formal ones from264. Formal U,P,V
derivatives are taken before evaluation. Moving coefficient
derivatives in t,s hold those formal variables fixed; derivatives
of y and theta below are total coefficient derivatives at fixed P.

## 2. The universal multiplier, with no conic restriction

Write
\[
 \begin{aligned}
 f&=H_U(y,P,\theta),\qquad g=H_V(y,P,\theta),\\
 \nu&=\mathcal F_V(P,\theta)/m,\quad
 \beta_f=(2y+\mathcal F_P(P,\theta))/m,
 \quad D_f=(2P+k_t)/m,\\
 \mathcal A&=y_t+\theta_Py_s+y_P^2,\\
 \mathcal B_1&=\theta_t+
       \theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P.
 \end{aligned}
\tag{5}
\]
The complete linear and constant-X scalar identities, together with
296's unit evaluated gradient-minor ideal, give exactly
\[
 \mathcal A=\kappa g,\qquad
 \mathcal B_1=-\kappa f,\qquad \kappa\in L^*.
\tag{6}
\]
This is the universal conclusion of494 before its conic Section4.
It includes zero f or g; no division by either is used here. In
particular kappa has no P dependence. Only its coefficient-field
membership, not its value or constancy in t,s, is used in the degree
comparisons below.

Let
\[
 N_\theta=\deg_P\theta\ge3,\quad
 \theta=aP^{N_\theta}+\text{lower terms},\quad a\in L^*.
\tag{7}
\]
If y is zero or constant, (1) is immediate. Otherwise put
d=deg_P(y). Assume first d>N_theta+1 and write
y=rP^d+lower terms, with r in L*.
The exact formula
\[
 f=2y+\mathcal F_P(P,\theta)
                 -\frac{(2P+k_t)\mathcal F_V(P,\theta)}m
\tag{8}
\]
has degree at most max(d,N_theta+1)=d. In B1 the term
theta_P y_P is uniquely highest, of degree N_theta+d-2 and
coefficient N_theta*d*a*r. Every other term has degree at most
max(2N_theta-1,d,N_theta). Since N_theta>=3 and d>N_theta+1,
that unique degree exceeds both this maximum and d. Equation (6)
is impossible. Hence
\[
 d\le N_\theta+1.
\tag{9}
\]

## 3. An exact off-level decomposition of the monic relation

Put h=m_s and p=m_t, and define formal polynomials in P by
\[
 B=pP+n_s,\qquad F_0=\frac{k_{tt}}2P^2+n_tP,
 \qquad \gamma=2P+k_t.
\]
Then \(\mathcal F=F_0+BV+hV^2/2\) and \(\mathcal F_V=B+hV\).
Expansion of the ENTIRE
formal polynomial in (4), without evaluating U or V, gives
\[
 H-h_0=U^2+(C_1+C_2V)U+C_3V^3+C_4V^2+C_5V+C_6,
\tag{10}
\]
where
\[
 \begin{aligned}
 C_1&=k_{tt}P+n_t-\gamma B/m,&
 C_2&=p-\gamma h/m,\\
 C_3&=h_s/6-h^2/(2m),&
 C_4&=h_tP/2+n_{ss}/2-3hB/(2m),\\
 C_5&=m_{tt}P^2/2+n_{ts}P-\ell_s
                    +(h\ell-B^2-hF_0)/m,\\
 C_6&=k_{ttt}P^3/6+n_{tt}P^2/2-\ell_tP-h_0
                    +B(\ell-F_0)/m.
 \end{aligned}
\tag{11}
\]
Their formal degrees are bounded, respectively, by
2,1,0,1,2,3. These expressions retain every lower coefficient,
including the moving level h_0. In particular differentiating
BEFORE evaluation gives
\[
 H_V=C_2U+3C_3V^2+2C_4V+C_5.
\tag{12}
\]
No derivative of an evaluated equality is substituted for this
formal gradient.

Suppose now d=N_theta+1. If h=0, then h_s=h_t=0,
C_2=p, C_3=0 and C_4=n_ss/2. Thus after V=theta the U
coefficient in (10) has degree at most N_theta and the free
coefficient has degree at most 2N_theta. Indeed their possible
degrees are bounded by max(2,N_theta) and
max(2N_theta,N_theta+2,3). The term y^2 has degree
2N_theta+2, uniquely exceeding all the other terms in the
actual level (4). This is impossible. Therefore
\[
 h=m_s\ne0\quad\text{whenever }d=N_\theta+1.
\tag{13}
\]
This includes the h=0,p=0 boundary without any division by p.

## 4. Excluding the last excess degree

Continue under d=N_theta+1 and h nonzero. For clarity write
N=N_theta in the coefficient calculations in this section only;
this integer N is not the selected derivation in (2). Thus N>=3,
theta=aP^N+lower terms and y=rP^{N+1}+lower terms, with a,r
nonzero in L.

In (10), the term C_3 theta^3 has degree 3N if C_3 is
nonzero. Every other term has degree at most 2N+2<3N.
The full H level therefore gives
\[
 [P^{3N}](H(y,P,\theta)-h_0)=a^3C_3=0,
 \qquad h_s=3h^2/m.
\tag{14}
\]
Consequently C_3=0 as a coefficient identity, so the ENTIRE
theta^3 term disappears. This is stronger than removing only its
leading monomial. The next coefficient of the full level is then
\[
 [P^{2N+2}](H(y,P,\theta)-h_0)=r^2-2har/m=0,
 \qquad r=2ha/m.
\tag{15}
\]
Indeed y^2 and the leading part of C_2 theta*y are the only
terms of that degree. All remaining terms have degree at most
2N+1. Dividing by r in (15) is licensed by its exact degree.

Since deg f<=N+1 and 2N-1>N+1, the complete multiplier equation
B1=-kappa f gives
\[
 \begin{aligned}
 [P^{2N-1}]\mathcal B_1
   &=Na\big((N+1)r+a_s+ha/m\big)=0,\\
 a_s&=-(2N+3)ha/m.
 \end{aligned}
\tag{16}
\]
The three contributions in the first line are theta_P y_P,
theta_P theta_s and theta_P nu. All other terms have smaller
degree, including theta_t. Equations (14)--(16) are identities
in the existing exact coefficient field L. Differentiating (15)
with the original fixed-t coefficient partial, and using m_s=h,
gives
\[
 r_s=2\left(\frac{h_sa+ha_s}{m}-\frac{h^2a}{m^2}\right)
     =-(4N+2)\frac{h^2a}{m^2}.
\tag{17}
\]

Now return to the formal gradient (12). Because C_3=0, its
evaluation is exactly
\[
 g=C_2y+2C_4\theta+C_5,\qquad \deg_Pg\le N+2.
\tag{18}
\]
This bound does not assume that the evaluated leading coefficient
is nonzero. The full A expression in (5), however, has
\[
 \begin{aligned}
 [P^{2N}]\mathcal A
  &=Na r_s+(N+1)^2r^2\\
  &=(6N+4)\frac{h^2a^2}{m^2}\ne0.
 \end{aligned}
\tag{19}
\]
Here y_t has degree at most N+1. Characteristic zero, m!=0,
h!=0 and a!=0 make the final coefficient nonzero. Since
2N>N+2 for every N>=3, (18),(19) contradict A=kappa g with
kappa in L*. This eliminates d=N_theta+1, including N_theta=3.
Together with (9), it proves (1).

All divisions were by the nonzero field elements m, a, r or
nonzero integers. No nonvanishing of h_t and no choice of a
root or actual coordinate fiber was used. The lower
coefficients of y, theta, n and ell were never fixed or discarded.

## 5. Verification and retained scope

The complete264,296,299 and494 sources were read before this
note. The genuine formal decomposition (10)--(12) makes all
degree comparisons directly inspectable. Fresh unsaved inline
algebra b9bcc4/b891b5 reconstructed the full formal H and H_V,
then evaluated arbitrary lower coefficients for N_theta=3 through12.
It checked (14),(15),(16),(19) before their final substitutions
and the degree bound in (18), with every residual zero. Earlier
721722 independently rebuilt the full h=0 formal gradients and
their leading coefficients. These exact symbolic checks supplement
the uniform degree proof, which applies to every N_theta>=3.
Fresh f10f10 separately reconstructed the complete written
decomposition (10),(11), its formal gradient (12), and the all-N
identities (17),(19), returning four zero residuals.

Root and Geometry independently reconstructed the same off-level
decomposition and the complete high coefficients before authoring.
Geometry's fresh5cb0bf/5bdac4 differentiated formal H_V before
evaluation and checked all lower coefficients for degrees3 through6.
A complete saved-source review remains a separate step after the
author hold.

The accepted bound
[299](principal-paraboloid-generic-degree-bound-pass299-working.md)
is only finite-window context: in this supplied actual chart the
nonzero-coupling intrinsic degrees are at most twelve. Thus the
remaining higher-theta degrees lie in 3 through12, with y no larger.
No coefficient-field complexity bound or classification follows.

The separate positive-degree three-ring initial-kernel argument
explored before this direct proof is not needed here and is not
asserted as an additional theorem in this note. In particular no
provisional cubic-theta exception is retained: (19) covers it.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. There is no claim
of realization, actual recognition, arbitrary chart entry,
unrestricted cancellation, novelty or external certification.
