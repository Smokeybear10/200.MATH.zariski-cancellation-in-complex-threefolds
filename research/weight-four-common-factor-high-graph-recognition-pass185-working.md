# Recognition of the high-graph branch for the common-factor quartic

**Status: working restricted proof; lower graph degrees and constant
projection are not recognized by this note.**

Assume an actual sliced two-linear/two-quadratic frame with full
weighted initial kernel
\[
(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\]
If its selected projected \(y\) is an affine line parameter and the
projected graph \(\vartheta=P(y)\) has degree at least three, then the
coefficient equations force an actual invariant ambient coordinate.
Thus the invariant ring is a polynomial three-ring by the regular-kernel
recognition endpoint recorded below.

The proof first forces graph degree five. It then obtains, rather than
assumes, the constant-translation normalization needed for that endpoint.

## 1. Actual inputs and the graph hypothesis

Retain the actual setup, exact field, partials and chart of
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md),
with the specific full initial kernel above. In particular
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
N=[u^3](\partial_Z|_A)\ne0,\quad L=\operatorname{Frac}(\ker_A N),
\quad A_L=L[v],\quad Nv=1,\\
a=EX\in L^*,\quad t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad
q=(E^2Z/2)/a^2=-t\rho+t^4 .
\end{gathered}
\tag{1}
\]
The extension \(L/\mathbb C(t,\rho)\) is finite separable.
The coefficient partials commute and initially fix \(v\).
Assume
\[
y=\gamma v+\eta,\quad \gamma\in L^*,\quad
\vartheta=P(y),\quad P\in L[U],\quad D:=\deg P\ge3 .
\tag{2}
\]
This is an explicit branch hypothesis, not an arbitrary-entry statement.
The full actual chart supplies
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
\sigma=(-\rho+4t^3)y-t\vartheta+k,\\
z=-tw+6t^2y^2+k_t y+(k_\rho-y)\vartheta+n,\qquad k,n\in L .
\end{gathered}
\tag{3}
\]
Put
\[
\begin{gathered}
R(U)=k_\rho-U,\quad
S(U,V)=4tU^3+H_2(k;U,V)+H_1(n;U,V),\\
A_1(U,V)=H_1(k_\rho;U,V)+n_\rho,\quad
T(U,V)=U^4+H_3(k;U,V)+H_2(n;U,V),\\
\mathcal H=R\{T-\ell_tU-\ell_\rho V-m\}
                 +A_1(\ell-S),\qquad \ell,m\in L .
\end{gathered}
\tag{4}
\]
The actual potentials say \(R(y)w+S(y,\vartheta)=\ell\) and
\(A_1(y,\vartheta)w+T(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m\).
The eliminant has exact total degree five and top part \(-U^5\).
Also \(R(y)\ne0\).

We use the unit-selected-cofactor conclusion for this chart:
\[
\mathcal H=GQ,\qquad G=V-P(U),\qquad Q(y,\vartheta)\in L^* .
\tag{5}
\]
Its full proof is the
[selected-component argument184](weight-four-bad-linear-selected-component-pass184-working.md),
following the whole-plane proof184. This is a required input, not
inferred from birationality or a nonzero Jacobian alone.

## 2. The eliminant is pure and the graph has degree five

Because \(\deg G=D\ge3\) and \(\deg\mathcal H=5\),
\(\deg Q=5-D<D\). For \(c=Q(y,\vartheta)\in L^*\),
the polynomial \(Q-c\) belongs to the plane evaluation kernel
\((G)\). Its degree is smaller than \(\deg G\), so it is zero.
Consequently
\[
\mathcal H=c\{V-P(U)\},\qquad c\in L^*,\qquad D=5 .
\tag{6}
\]
This is where the lower graph degrees are excluded from the
present proof: for them an evaluated unit need not be a constant
polynomial cofactor.

The coefficient of \(V^3\) in the literal expression (4) is
\[
[V^3]\mathcal H
 =\frac{k_\rho-U}{6}k_{\rho\rho\rho}
    -\frac{k_{\rho\rho}^2}{2}.
\tag{7}
\]
It must vanish by (6). Its coefficient of \(U\) first gives
\(k_{\rho\rho\rho}=0\), then its constant term gives
\(k_{\rho\rho}=0\). With that identity, the \(V^2\) coefficient
of (4) becomes \((k_\rho-U)n_{\rho\rho}/2\), so
\(n_{\rho\rho}=0\) too.

Let \(K=\ker_L\partial_\rho\). It is a finite extension of
\(\mathbb C(t)\): for an element of \(K\), differentiate its monic
minimal polynomial over \(\mathbb C(t,\rho)\); minimality forces
all coefficient derivatives to vanish, so those coefficients lie
in \(\mathbb C(t)\). Any \(\mathbb C(t)\)-independent finite set
in \(K\) remains independent after adjoining the transcendental
\(\rho\); its size is therefore bounded by
\([L:\mathbb C(t,\rho)]\).
The field \(K\) is stable under \(\partial_t\). Its
\(\partial_t\)-constant field is \(\mathbb C\), by the same
minimal-polynomial argument and algebraic closedness.
Subtracting explicit primitives, not assuming arbitrary
antiderivatives, gives
\[
k=r\rho+k_0,\qquad n=s\rho+n_0,\qquad r,s,k_0,n_0\in K .
\tag{8}
\]

## 3. The linear V coefficient supplies constant translations

Primes in this section mean \(\partial_t\) on \(K\). The \(V\)
coefficient of (4), after (8), is
\[
[V]\mathcal H
 =(r-U)\{r''U^2/2+s'U-\ell_\rho\}-(r'U+s)^2=c.
\tag{9}
\]
Its coefficients of \(U^3,U^2,U\), in that order, give
\[
r''=0,\qquad s'=-(r')^2,\qquad
\ell_\rho=2r's-rs' .
\tag{10}
\]
The exact constant field just proved implies
\[
\begin{gathered}
r=\mu t+\nu,\quad s=-\mu^2t+s_0,\quad
\mu,\nu,s_0\in\mathbb C,\quad d=\mu\nu+s_0,\\
\ell_\rho=2\mu d-\mu^2r,\qquad
c=-d^2,\qquad d\in\mathbb C^* .
\end{gathered}
\tag{11}
\]
The nonzero scalar assertion is essential and follows from \(c\ne0\),
not from an unproved global unit property of \(a\).

Make the actual constant translation
\[
\widetilde X=X+\mu,\quad \widetilde Y=Y-\nu,\quad
\widetilde Z=Z,\quad\widetilde W=W .
\tag{12}
\]
Its inverse subtracts \(\mu\) and adds \(\nu\). The top homogeneous
initials are unchanged, so the full initial kernel and exact profile
are retained. The original partial \(\partial_Z\), its intrinsic
\(N\), the field \(L\), and the ratios \(t,\rho,q\) are unchanged.
The projected entries transform as
\[
\begin{gathered}
\widetilde y=y-r,\qquad
\widetilde\vartheta=\vartheta-2\mu\rho,\qquad
\widetilde w=w-\mu\vartheta+\mu^2\rho,\\
\widetilde\sigma=\sigma-2\mu q,\qquad
\widetilde z=z-\mu\sigma+\mu^2q .
\end{gathered}
\tag{13}
\]
Substituting (13) in the two identities (3) gives
\[
\begin{aligned}
\widetilde k
 &=k-r\rho+4rt^3-2\mu t^4
   =k_0+4rt^3-2\mu t^4\in K,\\
\widetilde n
 &=d\rho+\widetilde n_0,\qquad
\widetilde n_0=n_0-\mu k_0+r k_0'
                   +6t^2r^2-4\mu t^3r+\mu^2t^4\in K .
\end{aligned}
\tag{14}
\]
For a direct derivation valid before substituting \(q=-t\rho+t^4\),
the first transformed coefficient is
\(k+q_t r+2\mu\rho q_\rho-2\mu q\); the second is
\[
n-\mu k+r k_t+2\mu\rho k_\rho+
H_2(q;r,2\mu\rho)-\mu q_t r+\mu^2(q-\rho q_\rho).
\tag{15}
\]
Expansion of the two Taylor polynomials in the original and translated
projected entries gives these formulas. In particular the coefficient
of \(\rho\) in (15) is \(s+\mu r=d\), as required in (14).

The new graph remains of degree five. Apply the universal chart
and the unit-cofactor conclusion in the translated actual frame;
the degree argument of Section 2 still makes its eliminant pure.
Its \(V\) coefficient, with (14), is
\(\widetilde\ell_\rho U-d^2\). Purity forces
\[
\widetilde\ell\in K .
\tag{16}
\]
This derives the needed normalization without assuming a
formula for how the previous coefficient \(\ell\) transforms.

## 4. Recognition in the normalized actual frame

Drop tildes. We now have
\[
k\in K,\qquad n=d\rho+n_0,\quad n_0\in K,\qquad
\ell\in K,\qquad d\in\mathbb C^* .
\tag{17}
\]
The normalized potentials solve polynomially:
\[
\begin{aligned}
w&=\frac md-\frac{y^4}{d}
       -\frac{k'''}{6d}y^3-\frac{n_0''}{2d}y^2+\frac{\ell'}d y,\\
\vartheta&=\frac{yw-4ty^3-k''y^2/2-n_0'y+\ell}{d},\\
z&=-tw+6t^2y^2+k'y-y\vartheta+d\rho+n_0 .
\end{aligned}
\tag{18}
\]
Changing from \(v\) to the affine \(y\) changes the calibrated
determinant to \(J_y=-a^3/\gamma\in L^*\); the factor
\(\gamma=Ny\) is not discarded.
At fixed \(y\), direct differentiation of (18) gives
\[
\begin{aligned}
J_y={}&\frac{m_\rho}{d}
 \left\{\frac{5y^4}{d}+\frac{2k'''}{3d}y^3
   +\left(12t+\frac{3n_0''}{2d}\right)y^2
   +\left(k''-\frac{2\ell'}d\right)y+n_0'-\frac md\right\}\\
&-m_t+\frac{k''''}{6}y^3+\frac{n_0'''}2y^2-\ell''y .
\end{aligned}
\tag{19}
\]
Its \(y^4\) coefficient forces \(m_\rho=0\).
The remaining positive coefficients force
\(k''''=n_0'''=\ell''=0\), and \(J_y=-m'\ne0\).
The exact constant field of \(K\) yields
\[
k=k_3t^3+k_2t^2+k_1t+k_0,\quad
n_0=n_2t^2+n_1t+n_{00},\quad
\ell=\ell_1t+\ell_0 ,
\tag{20}
\]
with all displayed coefficients in \(\mathbb C\).

Let \(K_3(X,Y)=X^3k(Y/X)\) and \(N_2(X,Y)=X^2n_0(Y/X)\);
these are polynomials by (20). Then the actual polynomial
\[
I=dW-(X^2Z+XYW-Y^4)+K_3(X,Y)+N_2(X,Y)-\ell_1Y-\ell_0X
\tag{21}
\]
equals \(m\in L\) in the chart. Hence \(EI=0\) in the original
domain, not only on the localized presentation.
Writing \(I=-X^2Z+(d-XY)W+P_0(X,Y)\), the companion
\(J=(d+XY)Z+Y^2W\) has inverse
\[
Z=\frac{(d-XY)J-Y^2(I-P_0)}{d^2},\qquad
W=\frac{(d+XY)(I-P_0)+X^2J}{d^2}.
\tag{22}
\]
The coefficient matrix has determinant \(-d^2\), so both compositions
are the identity in the original polynomial ring.
Thus \(B=\mathbb C[X,Y,I,J]\) and \(I\) is an invariant coordinate.
The [normalized recognition note185](weight-four-normalized-common-factor-recognition-pass185-working.md)
records the same endpoint:
the slice makes \(A\) regular, and the retained
Bhatwadekar--Gupta--Lokhande Theorem3.5 applied over \(\mathbb C[I]\)
gives \(A=\mathbb C[I]^{[2]}\).

## 5. Exact remaining scope

The conclusion covers only the stated high-graph branch.
It does not dispose of a constant projected \(y\), or graphs of
degree zero, one or two without a separate exclusion.
Nor does it solve the other quartic initial forms, height-two
initial kernels, arbitrary time profiles, or unrestricted cancellation.

All coordinate translations and inverse formulas are polynomial with
complex-constant denominators. The exact coefficient field has not
been replaced by a rational field, and a generic affine parameter
has not been declared an original coordinate.
The main inputs are the actual universal chart184 and the separate
whole-plane/unit-cofactor arguments184--185. They are required
written working proofs, not consequences of finite tests.

This is not a historical novelty claim, human expert certification,
proof-assistant verification, submission or external contact.
All183 and earlier frozen files remain unchanged.
