# Nonconstant projection forces rho-constant R in the absent-variable chart

**Status: working necessary-condition proof, not global coordinate recognition.**

In a supplied actual weight-four chart with \(q_\rho=0\) and
\(q'''\ne0\), assume \(R=k_\rho\ne0\). If the first projected
coordinate \(y\) is nonconstant on the selected generic line, then
\(R_\rho=0\). The proof uses the actual scalar determinant and
the leading form of a plane curve whose coordinate ring is the
whole affine line. It does not assume that the exact coefficient
field is rational.

This applies in particular to the absent-variable initial form
\(X^2Z-Y^4\), where \(q=t^4\). It does not exclude constant
projection or recognize the invariant ring.

## 1. Actual hypotheses and the nonzero scalar return

Retain a supplied actual frame from
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(F),\quad \operatorname{wt}F=4,\quad F_{\mathsf Z}\ne0,\\
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
a=EX\in L^*,\quad t=EY/a,\quad
\rho=(E^2W/2)/a^2,\quad q=(E^2Z/2)/a^2,\quad
[L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{1}
\]
The initial ideal in (1) is the full kernel, not one vanishing
relation. The ratios \(t,\rho\) are independent; their coefficient
partials extend uniquely and commute on \(L\), initially fixing \(v\).
For this note additionally assume
\[
q_\rho=0,\qquad q'''=\partial_t^3q\ne0,\qquad R=k_\rho\ne0.
\tag{2}
\]
Primes refer to the coefficient \(t\)-partial, not a projected
parameter derivative. The coefficient \(q\) is allowed to be
algebraic over \(\mathbb C(t)\).

The actual chart supplies projected polynomials in \(L[v]\) with
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad
J_0=\det\frac{\partial(y,z,w)}{\partial(t,\rho,v)}
    =-a^3\in L^* .
\end{gathered}
\tag{3}
\]
Let \(H_j\) denote the divided coefficient Taylor forms of184.
For independent \(U,V,W_0\) define
\[
\begin{gathered}
f=q''U^2/2+k_tU+RV+n,\quad
S=q'''U^3/6+H_2(k;U,V)+H_1(n;U,V),\\
A_1=S_V=R_tU+R_\rho V+n_\rho,\quad
T=q''''U^4/24+H_3(k;U,V)+H_2(n;U,V),\\
\mathcal P=RW_0+S-\ell,\qquad
\Psi=A_1W_0+T-\ell_tU-\ell_\rho V,\qquad k,n,\ell,m\in L .
\end{gathered}
\tag{4}
\]
The universal potentials give
\(z=f(y,\vartheta)\), \(\mathcal P(y,\vartheta,w)=0\), and
\(\Psi(y,\vartheta,w)=m\).
Because \(R\) is a nonzero element of the field \(L\), rather
than a nonconstant projected polynomial, they immediately give
\[
w=\frac{\ell-S(y,\vartheta)}R,\qquad
L[y,\vartheta]=L[y,z,w]=L[v].
\tag{5}
\]
The first containment uses the formula for \(z\) and \(w\);
the opposite containment uses \(y,\vartheta\in L[v]\).
At least one of \(y,\vartheta\) is nonconstant.
No inverse in the original ring is inferred from \(1/R\in L\).

## 2. A nonzero eliminant with unit evaluated cofactor

Eliminate \(W_0\) in the polynomial ring:
\[
\mathcal H
 =R(T-\ell_tU-\ell_\rho V-m)+A_1(\ell-S)
 =R(\Psi-m)-A_1\mathcal P .
\tag{6}
\]
It has degree at most four and vanishes at \((y,\vartheta)\).
We will obtain its nonvanishing and the cofactor assertion from
the actual determinant, without importing the special two-form
conclusion of selected-component184.

Use evaluated quantities
\[
A=A_1(y,\vartheta),\quad B_1=S_U(y,\vartheta),\quad
C_i=S_i(y,\vartheta)+R_iw-\ell_i,\qquad i=t,\rho .
\tag{7}
\]
Every subscript on a formal polynomial in this definition
differentiates coefficients before evaluation.
The formal gradients of \(\mathcal P\) and \(\Psi\), after evaluation,
are \((B_1,A,R)\) and \((C_t,C_\rho,A)\).
Indeed \((A_1)_U=R_t\), \((A_1)_V=R_\rho\),
\(T_U=S_t\), and \(T_V=S_\rho\).
The determinant row reduction of the actual chart and the
differential of the first potential give
\[
\begin{gathered}
J_0=
[dy\wedge(R\,d\vartheta+B_1dt+A\,d\rho)\wedge dw]_{dt\wedge d\rho\wedge dv},\\
R\,dw=-B_1dy-A\,d\vartheta-C_tdt-C_\rho d\rho .
\end{gathered}
\tag{8}
\]
There is no \(w\,dq_\rho\) term, because \(q_\rho=0\) here.
Differentiating (6) and imposing the two potentials only afterwards
gives
\[
\begin{gathered}
\mathcal H_U(y,\vartheta)=RC_t-AB_1,\qquad
\mathcal H_V(y,\vartheta)=RC_\rho-A^2,\\
R^2J_0=C_U\mathcal H_U(y,\vartheta)+C_V\mathcal H_V(y,\vartheta),\\
C_U=R(\vartheta_\rho y_v-y_\rho\vartheta_v)+Ay_v,\qquad
C_V=R(y_t\vartheta_v-\vartheta_ty_v)-B_1y_v .
\end{gathered}
\tag{9}
\]
For completeness, the last linear combination expands to \(R\) times
\[
-(RC_t-AB_1)(y_\rho\vartheta_v-y_v\vartheta_\rho)
 +(RC_\rho-A^2)(y_t\vartheta_v-y_v\vartheta_t)
 +(AC_t-B_1C_\rho)y_v.
\]
Substitution for \(R\,dw\) in (8) gives exactly \(R^2J_0\).
This reconstructs the cleared identity used in the earlier
whole-plane argument, with the present scalar \(R\).

In particular \(\mathcal H\ne0\).
The kernel of \(L[U,V]\to L[v]\) is a height-one prime, generated
by an irreducible polynomial \(G\). Write \(\mathcal H=GQ\).
The gradient identities in (9) show that \(Q(y,\vartheta)\)
divides the nonzero field scalar \(R^2J_0\) in \(L[v]\).
Consequently
\[
Q(y,\vartheta)=\omega\in L^*,\qquad
Q-\omega\in(G),\qquad
\mathcal H=\omega G+G^2D,\quad D\in L[U,V].
\tag{10}
\]
This also proves simple selection. It does not assert that \(Q\)
itself is constant as a polynomial.

## 3. A polynomially parametrized line has one point at infinity

We record the precise leading-form fact used below.
For the actual equality \(L[y,\vartheta]=L[v]\), the top
homogeneous part of \(G\), over an algebraic closure \(\overline L\),
is a scalar times a power of one linear form.

Here is a direct justification. Put
\(d=\max(\deg_v y,\deg_v\vartheta)>0\). Homogenize the
parametrization to degree \(d\):
\[
[s:t_0]\longmapsto
[\,t_0^d y(s/t_0):t_0^d\vartheta(s/t_0):t_0^d\,].
\tag{11}
\]
These homogeneous polynomials have no common zero. At a finite
parameter value the last entry is nonzero, and at \(t_0=0\)
at least one of the first two entries is nonzero by the definition
of \(d\). Thus (11) is a morphism from the projective line.
Its image is closed, since the projective line is proper, and
contains the dense affine curve defined by \(G\).
The image is therefore exactly the projective closure of that curve.
The equality of coordinate rings in (5) remains true after
base extension to \(\overline L\), so this curve is geometrically
integral, with the same principal defining equation up to a scalar.

The last entry of (11) vanishes only at \([1:0]\).
Hence the projective closure has only one point on the line at
infinity. Its homogeneous defining equation restricts there to
the top homogeneous part of \(G\). A binary homogeneous polynomial
over an algebraically closed field with only one projective root
is a nonzero scalar times one linear form to its full degree.
This proves the stated leading-form fact.
No plane-embedding classification theorem is needed.

## 4. The nonsquare quartic top leaves only constant y

Suppose for contradiction to the stated implication that
\(R_\rho\ne0\). From (4) and (6), the degree-four part is
\[
\mathcal H_4=U^3
\left[
 \left(\frac{Rq''''}{24}-\frac{R_tq'''}6\right)U
 -\frac{R_\rho q'''}6 V
\right]=U^3\Lambda(U,V).
\tag{12}
\]
The \(V\) coefficient of \(\Lambda\) is nonzero by (2).
Thus \(U,\Lambda\) are distinct linear factors, of multiplicities
three and one. In particular \(\deg\mathcal H=4\).
Let \(g=\deg G\); then \(1\le g\le4\).

If \(g=4\), then \(Q\) is constant, so \(\mathcal H\) is a scalar
multiple of \(G\). Section 3 would make its top part a fourth
power of a linear form, contradicting (12).

If \(g=3\), then \(\deg Q=1\). The divisibility
\(G\mid Q-\omega\) in (10) forces \(Q=\omega\).
This would make \(\deg\mathcal H=3\), again impossible.

If \(g=2\), equation (10) and degree four force \(D\) to be
a nonzero constant. Hence \(\mathcal H_4=D G_2^2\).
Over \(\overline L\) all its linear-factor multiplicities would
be even. This contradicts the multiplicities in (12).

Finally let \(g=1\). In (10), \(D\) must have degree two, and
\(\mathcal H_4=G_1^2D_2\).
The linear form \(G_1\) divides \(U^3\Lambda\), but its square
cannot divide the factor \(\Lambda\) of multiplicity one.
Thus \(G_1\) is a scalar multiple of \(U\). Since \(G\) has degree
one, its vanishing at the projected pair gives \(y\in L\).

All possible degrees have been addressed. The exact conclusion is
\[
\boxed{R\ne0,\ R_\rho\ne0\ \Longrightarrow\ y\in L;
\qquad R\ne0,\ y\notin L\ \Longrightarrow\ R_\rho=0.}
\tag{13}
\]

## Scope and verification

The actual scalar determinant is essential to (10).
Merely knowing that the projected curve is birational to a line
would not suffice; the proof establishes its entire ring in (5).
The point at infinity argument is used only for degree four;
the other three possibilities use exact polynomial degrees and
the unit evaluated cofactor.

When \(R_\rho=0\), the top form in (12) can become a fourth power
or can vanish. Those cases were not excluded by this proof.
Likewise the constant-\(y\) branch is a remaining case, not a
contradiction derived here. No coordinate is returned to the
original ring, and no claim \(K=\mathbb C(t)\) is made.

The zero-\(R\) branch has its separate
[reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md).
Combining it with this necessary condition does not yet recognize
all absent-variable quartics, much less arbitrary sliced actions.
No earlier source was changed. This is not a historical novelty,
human expert review, proof-assistant certification, public claim,
submission or unrestricted cancellation result.
