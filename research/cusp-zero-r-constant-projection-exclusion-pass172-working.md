# The zero-r, zero-second-coefficient cusp branch is impossible

**Status: complete working argument, pending independent review of this saved artifact.**

In the actual cusp chart159, the branch \(k_\rho=n_\rho=0\)
would have an original coordinate partial commuting with the sliced
action. This gives a polynomial three-variable restriction. The two
alternatives in Wang's published two-coordinate classification both
contradict the actual cusp relation among its leading coefficients.
Consequently this branch cannot occur.

The key coefficient-field equality is proved from the actual
polynomial inverse. No generic parameter is assumed to be an original
coordinate, and no slice is transferred to the three-variable
restriction. All171 and earlier artifacts remain unchanged.

## 1. Actual chart and the constant projected entries

Retain the complete actual hypotheses of
[cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
including
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\\
a=EX\ne0,\quad N=[u^3](\partial_Z|_A)\ne0,\quad
S=\ker_A N,\quad L=\operatorname{Frac}S,\quad A_L=L[v],\quad Nv=1 .
\end{gathered}
\tag{1}
\]
The four displayed variables are actual polynomial coordinates.
The initial-kernel assertion in (1) is the full one, in weights
\((1,1,2,2)\). Set \(b=EY\) and \(e=E^2Z/2\). It gives
\(ae=b^3\), with \(a,b,e\ne0\).

Put \(t=EY/a\) and \(\rho=(E^2W/2)/a^2\). The exact field \(L\)
is finite separable over \(\mathbb C(t,\rho)\); its coefficient
partials extend from that rational field and fix \(v\).
In particular \(t,\rho\) are algebraically independent over
\(\mathbb C\), so \(t\) is not a complex constant.
In the actual invariant localization at \(a\),
\[
\begin{gathered}
B_a=A_a[X],\qquad A_a=\mathbb C[y,z,w]_{a_0},\qquad
a=a_0(y,z,w)\in L^*,\\
\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\qquad
L[y,z,w]=L[v],\\
Y=y+tX,\qquad Z=z+\sigma X+t^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
\sigma=3t^2y+k,\qquad
z=3ty^2+k_t y+k_\rho\vartheta+n,\qquad k,n\in L .
\end{gathered}
\tag{2}
\]
In particular \(y,z,w\) are algebraically independent over
\(\mathbb C\), not merely a generating triple after extension to \(L\).

Assume the branch
\[
r:=k_\rho=0,\qquad n_\rho=0 .
\tag{3}
\]
The \(X^2\) determinant potential159 then reads
\[
y^3+\tfrac12 k_{tt}y^2+n_t y=\ell,\qquad \ell\in L .
\tag{4}
\]
This monic equation makes \(y\in L[v]\) algebraic over \(L\);
therefore \(y\in L\). Equations (2) give \(z,\sigma\in L\).

For clarity, the remaining constant-coefficient conclusion can be
reconstructed from the actual calibrated determinant. Its rows are
the coefficient derivatives of \(Y,Z,W\), with \(X\) fixed, and
\[
J(X)=
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
=-a^3 .
\]
Because \(Y,Z\in L[X]\), this factors as
\[
M(X)(w_v+\vartheta_vX)=-a^3,\qquad
M(X)=\det\frac{\partial(Y,Z)}{\partial(t,\rho)}\in L[X] .
\tag{5}
\]
The two factors belong to the domain \(L[v][X]\) and their product
is a nonzero element of \(L\). Each is a unit. Consequently
\(M\in L^*\), \(\vartheta_v=0\), and \(w_v=-a^3/M\in L^*\).
Thus
\[
y,z,\sigma,\vartheta\in L,\qquad
w=\alpha v+\beta,\quad \alpha\in L^*,\quad\beta\in L,\qquad
L(v)=L(w).
\tag{6}
\]
No integral slice for \(N\) has been inferred.

## 2. The actual inverse identifies the entire coefficient field

Let \(L_0=\mathbb C(y,z)\), a subfield of \(L\).
From (2) and (6),
\[
L_0(w)=\mathbb C(y,z,w)=\operatorname{Frac}A=L(w).
\]
The element \(w\) is transcendental over \(L\). For any subfield
\(L_0\subset L\) and such an indeterminate,
\(L\cap L_0(w)=L_0\): if \(\xi\in L\) is \(P(w)/Q(w)\) with
\(P,Q\in L_0[w]\), then \(P-\xi Q=0\); comparison at any nonzero
coefficient of \(Q\) gives \(\xi\in L_0\).
Intersecting the displayed equality with \(L\) proves
\[
L=\mathbb C(y,z).
\tag{7}
\]
In particular this exact field is now rational, as a consequence
of actual field return. That conclusion was not an assumption
about \(\ker_A N\), and does not assert
\(S=\mathbb C[y,z]\). The elements \(y,z\) may still require
localization to belong to the original ring.

## 3. An original coordinate partial commutes with E

Consider the derivation \(T_0=\partial_w\) of the common field
\[
\operatorname{Frac}B=L(X,w),
\]
defined to fix \(L\) and \(X\). By (2), (6), and (7),
\[
T_0X=T_0Y=T_0Z=0,\qquad T_0W=1.
\]
A derivation of the rational field is determined by its values
on the actual transcendence basis \(X,Y,Z,W\).
Therefore \(T_0\) is exactly the extension of the original
polynomial partial \(\partial_W\).

On the other hand, \(E=a\partial_X\) on \(L(X,w)\), fixing
\(L\) and \(w\). Its coefficient \(a\in L\) is killed by \(T_0\).
It follows first in the fraction field and hence in \(B\) that
\[
[E,\partial_W]=0 .
\tag{8}
\]
This argument does not assume that a rational change of projected
coordinates is a global polynomial coordinate change.

Write the polynomial coefficients of \(E\) in its original frame.
Equation (8) says their \(W\) derivatives vanish. In characteristic
zero they all lie in \(R:=\mathbb C[X,Y,Z]\). Thus
\[
E=D+f\partial_W,\qquad
D\in\operatorname{LND}_{\mathbb C}(R),\quad f\in R,\qquad
DX=a\ne0,\quad D^2X=D^2Y=0 .
\tag{9}
\]
The ring \(R\) is stable under \(E\), so its restriction \(D\)
is locally nilpotent. Its nonzero value on \(X\) follows from
the original exact time degree. Its time degrees on \(X,Y,Z\)
are exactly \((1,1,2)\), and the relation \(ae=b^3\) holds in \(R\).
Nothing in (9) asserts that \(D\) has a slice, that \(f\) is a unit,
or that \(f\) is a constant plus an image under \(D\).

## 4. Primitive division preserves the cusp identity

Let \(\delta\ne0\) be a polynomial greatest common divisor in \(R\)
of \(DX,DY,DZ\), and put \(D=\delta D_0\). Then \(D_0\) is a
polynomial derivation with coefficients having no common nonunit.

Here the primitive division preserves local nilpotence for an
elementary reason. Since \(D\delta=\delta D_0\delta\), a nonzero
value would have contradictory \(D\)-degrees: the degree of
\(D\delta\) is \(\deg_D\delta-1\), whereas additivity of the
LND degree on nonzero products makes the right side have degree
at least \(\deg_D\delta\). The product-degree rule follows from
the top nonzero Leibniz coefficient in a characteristic-zero
domain. Hence \(D\delta=0\), and the domain property gives
\(D_0\delta=0\). Induction now gives
\[
D^j g=\delta^j D_0^j g\quad(g\in R,\ j\ge0),\qquad
D_0\in\operatorname{LND}_{\mathbb C}(R),\qquad
D_0X\ne0,\quad D_0^2X=D_0^2Y=0 .
\tag{10}
\]
Thus \(D_0\) is nonzero and irreducible in the polynomial
coefficient sense used by the cited theorem. Equation (10) also
preserves all degrees of elements under these derivations.
Put
\[
\begin{gathered}
a_*=D_0X,\qquad b_*=D_0Y,\qquad e_*=\tfrac12D_0^2Z,\\
a=\delta a_*,\qquad b=\delta b_*,\qquad e=\delta^2e_*,
\qquad a_*e_*=b_*^3,\qquad t=b_*/a_*,\\
a_*,b_*,e_*\ne0,\qquad \deg_{D_0}Z=2 .
\end{gathered}
\tag{11}
\]
The relation follows by cancelling \(\delta^3\) in the domain
from \(ae=b^3\). It is not obtained by changing the selected
coefficient field or adjoining a root.

## 5. Both published classification alternatives are impossible

Wang's theorem, as stated in Dasgupta--Gupta Theorem 4.1,
applies over a characteristic-zero field to a nonzero irreducible
LND of an actual polynomial three-ring whose second iterate
vanishes on the first two displayed coordinates.[^wang]
All these hypotheses hold for \(D_0\) on \(R=\mathbb C[X,Y,Z]\).
Its two alternatives imply the following conclusions used here.

In the first alternative there is a nonzero complex linear form
\(\alpha X+\beta Y\) killed by \(D_0\). Consequently
\(\alpha a_*+\beta b_*=0\). Since \(a_*,b_*\ne0\), both
coefficients are nonzero, and \(t=b_*/a_*=-\alpha/\beta\)
is complex. This contradicts the independence in Section 1.

In the second alternative there is an actual coordinate
\(\xi\) with
\[
R=\mathbb C[\xi,X,Y],\qquad
D_0\xi=0,\qquad a_*,b_*\in\mathbb C[\xi].
\tag{12}
\]
Because this coordinate change holds \(X,Y\) fixed,
\(\mathbb C[X,Y][\xi]=\mathbb C[X,Y][Z]\).
Polynomial degrees in \(Z\), and then in \(\xi\), show that
\[
\xi=cZ+h(X,Y),\qquad c\in\mathbb C^*,\quad
h\in\mathbb C[X,Y],\qquad
D_0Z=-\{h_Xa_*+h_Yb_*\}/c .
\tag{13}
\]
Indeed both degrees must be one; their leading coefficients
multiply to one in \(\mathbb C[X,Y]\), whose units are
nonzero complex constants.

If \(a_*,b_*\) had a common nonconstant factor in
\(\mathbb C[\xi]\), equation (13) would make it divide
all three original coefficients \(D_0X,D_0Y,D_0Z\) in \(R\).
It remains a nonunit because \(\xi\) is an actual coordinate.
This contradicts irreducibility of \(D_0\).
Thus \(a_*,b_*\) are relatively prime in the PID
\(\mathbb C[\xi]\), hence also generate the unit ideal in \(R\).
Together with \(a_*e_*=b_*^3\), this forces \(a_*\) to be
a unit of \(R\), so \(a_*\in\mathbb C^*\).
Since \(t=b_*/a_*\) is nonconstant, \(b_*\) is a nonconstant
polynomial in \(\xi\), and is transcendental over \(\mathbb C\).

Let \(d_h\) be the ordinary total degree of \(h(X,Y)\), when
\(h\) is nonconstant, and let \(h_{d_h}\) be its highest
homogeneous part. In the presentation (12), \(D_0\) fixes \(\xi\)
and acts as \(a_*\partial_X+b_*\partial_Y\). Therefore
\[
D_0^{d_h}h=d_h!\,h_{d_h}(a_*,b_*)\ne0,\qquad
D_0^{d_h+1}h=0 .
\tag{14}
\]
The nonvanishing is exact: for \(a_*\in\mathbb C^*\), evaluation
of a nonzero homogeneous polynomial at \((a_*,T)\) is a nonzero
polynomial in \(T\); it cannot vanish at transcendental \(b_*\).
Also \(h\) cannot be constant, since (13) would give \(D_0Z=0\).
The equality \(\xi=cZ+h\) with invariant \(\xi\) identifies
the positive \(D_0\)-degrees of \(h\) and \(Z\).
Equations (11) and (14) thus give \(d_h=2\).

Taking the second derivative of (13)'s coordinate identity now
gives
\[
e_*=-h_2(a_*,b_*)/c,\qquad
b_*^3=-a_*h_2(a_*,b_*)/c .
\tag{15}
\]
The right side is a polynomial of degree at most two in the
transcendental \(b_*\), while the left side has degree three.
This contradiction excludes the second alternative as well.

The assumed branch \(k_\rho=n_\rho=0\) therefore cannot occur
under the actual hypotheses (1). This conclusion uses the exact
cusp relation, not merely the existence of a commuting partial.
It does not exclude every constant-\(y\) branch or every zero-\(r\)
branch. Other initial forms, arbitrary coordinate entry, and
unrestricted cancellation remain separate.

## Sources and evidence boundary

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 1--3 and 6, supplies the actual projected ring,
   determinant calibration and monic relation. The required
   constant projected entries and field intersection are
   reconstructed above.
2. Nikhilesh Dasgupta and Neena Gupta,
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   Theorem 4.1, printed p. 9. Both exact alternatives were
   freshly read. The authors attribute the theorem to
   Z. Wang, Theorem 4.7 and Remark 5 of their reference [14].
   Wang's original proof and the entire historical dependency
   chain were not re-audited. No regular-kernel theorem is
   needed for the contradiction.
3. [Autonomous two-quasi boundary142](autonomous-two-quasi-suspension-boundary-pass142.md),
   Sections 2--3, records a related invariant-content division
   and Wang application. The present argument does not assume
   that the action is an autonomous suspension.

No finite checker is used as proof of these universal conclusions.
No historical novelty, human expert review, proof-assistant
certification, or recursive audit of every retained input is claimed.
No171 or earlier artifact is modified.

[^wang]: Source 2.
