# Original-ring recognition for an affine radical projected pair

Status: bounded working recognition theorem. In the supplied actual
radical chart, if both original projected entries \(y,\vartheta\) are
affine and nonconstant on the generic line, the original sliced
derivation fixes an ambient polynomial coordinate. Wang's alternatives
are used only over \(\mathbb C(X)\); their descent is proved separately
in the original ring.

One alternative gives an actual auxiliary slice. The remaining
nonconstant-slope alternative contradicts factorial closure after a
polynomial-kernel contraction. No generic parameter is presumed to
be an original coordinate.

## 1. Actual hypotheses and the auxiliary derivation

Retain the full actual hypotheses of
[radical eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad a=EX\ne0,\quad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
L/\mathbb C(t,\rho)\text{ finite},\quad A_L=L[v],\quad Nv=1,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n,\qquad
J_0=-a^3\in L^*,\\
\deg_v y=\deg_v\vartheta=1.
\end{gathered}
\tag{1}
\]
The selected derivation is the actual coefficient
\(N=[u^3](\partial_Z|_A)\), annihilating all initial coefficients.
The coefficient partials commute and have joint constants
\(\mathbb C\). In particular \(t,\rho\) are algebraically independent,
by the full initial kernel. The speed \(a\) need not be a unit.

Set \(h=\vartheta\). The third potential makes \(w\) affine in \(h\):
its numerator is at most quadratic in \(h\), its denominator
\(R=2h+k_\rho\) is linear, and \(w\) is already polynomial in \(h\).
Thus
\[
y=\mu h+\nu,\qquad w=\lambda h+\omega,\qquad
\mu\in L^*,\quad \nu,\lambda,\omega\in L.
\tag{2}
\]
The second potential makes \(z\) a monic quadratic in \(h\).

Extend \(N\) to \(A[u]\) by \(Nu=0\), and set
\[
P=aN-(NX)E,\qquad \tau=aN\vartheta\in L^*.
\tag{3}
\]
This is an actual LND: on \(B_a=A_a[X]\) it fixes \(X\) and
restricts to the locally nilpotent derivation \(aN\) on \(A_a\).
It preserves \(B\) by its displayed formula.
Also \([E,P]=0\), since \(E(NX)=Na=0\).
These are the actual localization arguments fully written in
[constant-second210](weight-four-constant-second-projection-recognition-pass210-working.md).

The literal chart gives
\[
\begin{gathered}
PX=0,\quad PY=\tau\mu,\quad PW=\tau(X+\lambda),\\
PZ=\tau(2h+2\rho X+2\rho\lambda+k_t\mu+k_\rho),\\
P^2Y=P^2W=0,\qquad P^2Z=2\tau^2,\quad P^3Z=0.
\end{gathered}
\tag{4}
\]
In particular \(\tau^2\in B\). Normality of \(B\) and
\(\tau\in\operatorname{Frac}B\) give \(\tau\in B\).
It is killed by both \(E,P\), as are the original polynomials
\(PY=\tau\mu\) and \(PW-\tau X=\tau\lambda\).

Let \(\Delta\) be a gcd of \(PY,PW,PZ\) in \(B\).
The nonzero coefficient \(PY\) is killed by \(E,P\).
Factorial closure of their kernels gives \(E\Delta=P\Delta=0\).
Consequently
\[
\begin{gathered}
D=P/\Delta\in\operatorname{LND}(B),\quad [E,D]=0,\quad DX=0,\\
D^2Y=D^2W=0,\quad D^2Z=2\tau_0^2,\quad
\tau_0=\tau/\Delta\in B\setminus\{0\},\quad E\tau_0=D\tau_0=0 .
\end{gathered}
\tag{5}
\]
The iterate identity \(P^j=\Delta^jD^j\) proves local nilpotence.
Normality applied to \(D^2Z/2\) proves the membership of \(\tau_0\).
The derivation \(D\) is irreducible, also after extension to
\(\mathbb C(X)[Y,W,Z]\): a nonconstant common factor after that
localization would give one in \(B\), by Gauss's lemma.

## 2. Exact primary inputs

Write \(K=\mathbb C(X)\). We use the following freshly checked
statements from
[Dasgupta--Gupta, *Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1):

- Theorem4.1, restating Wang, applies to irreducible \(D\) on
  \(K[Y,W,Z]\) with \(D^2Y=D^2W=0\). Either a nonzero \(K\)-linear
  form in \(Y,W\) is fixed, or a coordinate \(F\) satisfies
  \(K[Y,W,Z]=K[F,Y,W]\), \(DF=0\), and \(DY,DW\in K[F]\).
- Theorem3.6 gives a fixed linear form over the PID \(\mathbb C[X]\)
  for an irreducible nice derivation of its polynomial three-ring.
  Lemma2.3(ii) puts an irreducible nice derivation of a two-variable
  polynomial ring over an invariant UFD in coefficient form over that base.
- Theorem4.8, restating Daigle, supplies an invariant coordinate for
  an irreducible LND on \(\mathbb C^{[3]}\) with a nonfixed coordinate
  of derivation-degree one.

Finally,
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
recognizes a regular kernel when the original nonzero LND on a
polynomial four-ring fixes an ambient coordinate.
The global slice supplies regularity here.
Wang's second alternative alone supplies no descent over
\(\mathbb C[X]\).

## 3. Recognition for constant mu

Suppose \(\mu\in\mathbb C^*\).
The actual elementary shear
\[
T=Z-Y^2/\mu^2
\tag{6}
\]
has inverse \(Z=T+Y^2/\mu^2\). Equation (4) makes \(P\), and its
primitive \(D\), nice on \(X,Y,W,T\).
With
\[
M=2(\rho-t/\mu),\qquad
H=2\rho\lambda+k_t\mu+k_\rho-2\nu/\mu,
\tag{7}
\]
one has \(PT=\tau(MX+H)\). The element \(M\) is transcendental
over \(\mathbb C\).

If \(\lambda\in\mathbb C\), use the actual fixed coordinate
\[
U=(X+\lambda)Y-\mu W,\qquad
B=\mathbb C[X,U,Y,T].
\tag{8}
\]
Its inverse is \(W=((X+\lambda)Y-U)/\mu\), together with (6).
Its E-degree is two, with leading coefficient
\(a^2(t-\mu\rho)\).

If \(\lambda\notin\mathbb C\), Theorem3.6 gives a nonzero row
over \(\mathbb C[X]\) annihilating \(PY,PW,PT\).
Cancelling \(\tau\) yields
\[
l(X)\mu+m(X)(X+\lambda)+n(X)(MX+H)=0 .
\tag{9}
\]
Here \(n\ne0\), since otherwise independence of \(1,\lambda\)
over \(\mathbb C\) would make both other row entries zero.
Equation (9) implies
\[
M=m_1\lambda+m_0,\qquad H=h_1\lambda+h_0,\qquad
m_i,h_i\in\mathbb C,\quad m_1\ne0.
\tag{10}
\]
Indeed reduce it modulo the complex vector subspace
\(\mathbb C+\mathbb C\lambda\) of \(L\).
Multiplication by the nonzero scalar polynomial \(n(X)\) is
injective on this quotient vector space's polynomial module,
so the classes of \(M,H\) vanish.
The transcendence of \(M\) gives \(m_1\ne0\).

Then
\[
U=T-(m_1X+h_1)W+
\frac{(m_1X+h_1)X-m_0X-h_0}{\mu}\,Y
\tag{11}
\]
is fixed by \(P,D\). Its inverse solves for \(T\), with coefficient
one, and then recovers \(Z\) by (6).
Thus \(B=\mathbb C[X,U,Y,W]\).
Its E-degree is three, with leading coefficient
\[
m_1a^3(t/\mu-\rho)=-m_1a^3M/2 .
\tag{12}
\]

Write \(V=T\) in (8)'s presentation and \(V=W\) in (11)'s.
Lemma2.3(ii) over \(\mathbb C[X,U]\) gives
\[
DY=b(X,U)\ne0,\qquad DV=c(X,U).
\tag{13}
\]
Also \(E(DY)=0\), since \(E(PY)=E\Delta=0\).

Here is the precise weighted gate forcing \(b\) to be constant.
The weights of \(X,U\) are \(1,d\), where \(d=2\) or \(3\).
Their leaders are \(a,a^d f(t,\rho)\), where \(f\) is respectively
\(t-\mu\rho\) or \(-m_1M/2\), both transcendental over
\(\mathbb C\). The leading evaluation of a nonzero weighted
homogeneous polynomial of weight \(n\) is
\(a^n\sum_{i+dj=n}c_{ij}f^j\), which is nonzero.
Thus every nonconstant polynomial in \(\mathbb C[X,U]\) has
positive E-degree. This does not assert algebraic independence
of the raw scalar \(a\), which could be constant.
It follows that \(b\in\mathbb C^*\).

There is consequently an actual presentation
\[
H_0=V-\frac{c(X,U)}bY,\qquad
B=\mathbb C[X,U,H_0,Y],\qquad \ker D=\mathbb C[X,U,H_0].
\tag{14}
\]
Both inverse orders follow from \(V=H_0+c(X,U)Y/b\);
\(Y/b\) is a \(D\)-slice.

The restriction of \(E\) to this polynomial three-ring is nonzero,
with \(EX=a\ne0,E^2X=0\). Divide its coefficients by their gcd.
That gcd divides the nonzero invariant \(a\), so factorial closure
and the iterate argument justify primitive division and preserve
the degree-one coordinate \(X\). Theorem4.8 gives an invariant
coordinate of this three-ring, which is ambient by (14).
The original kernel \(A\simeq B/(u)\) is regular, since \(Eu=1\)
expresses one as a polynomial combination of the partials of \(u\).
Theorem3.5 therefore gives
\[
A\simeq\mathbb C^{[3]}\quad\text{when }\mu\in\mathbb C^*.
\tag{15}
\]

## 4. Wang's alternatives and the linear relation exception

If \(r=(X+\lambda)/\mu\) is algebraic over \(K\), the coefficient
partials \(\partial_t,\partial_\rho\), extended to fix \(X\), kill
\(r\) by its separable minimal polynomial over \(K\).
Comparing coefficients of \(X\) in
\(\mu\lambda_i-(X+\lambda)\mu_i=0\) gives
\(\mu_i=\lambda_i=0\) for \(i=t,\rho\).
Joint constants give \(\mu,\lambda\in\mathbb C\).
In particular Wang's first alternative is recognized by (15).

Suppose \(\mu\notin\mathbb C\). Then the ratio is transcendental
over \(K\). Only Wang's second alternative can hold, giving
\[
F=Z+Q(Y,W),\qquad Q\in K[Y,W],\qquad DY,DW\in K[F],\quad DF=0 .
\tag{16}
\]
Indeed replacing the single variable \(Z\) over \(K[Y,W]\) has
degree one and unit leading coefficient, which can be scaled to one.
For a nonzero homogeneous \(Q_j\), \(Q_j(PY,PW)\ne0\), by
transcendence of \(PW/PY\). Thus the P-degree of \(Q\) is its
ordinary degree. Equations (4) and \(PF=0\) force degree two.
The homogeneous quadratic part gives
\[
1+A(X)\mu^2+B(X)\mu(X+\lambda)
 +C(X)(X+\lambda)^2=0,\qquad A,B,C\in K.
\tag{17}
\]

Clearing denominators and comparing powers of the independent
\(X\) proves that \(\mu,\lambda\) are algebraically dependent over
\(\mathbb C\). Their relation ideal is a height-one prime, because
\(\mu\) is nonconstant; write its irreducible generator as
\(G_0(M_0,L_0)\). Equation (17) gives \(\deg G_0\le2\).
Extension of this relation ideal to \(K\) is exact: clearing
denominators reduces any relation over \(K\) to coefficient
relations over \(\mathbb C\), since \(X\) is transcendental over \(L\).

If \(\deg G_0=2\), its scalar multiple over \(K\) is (17)'s
formal polynomial. A nonzero \(L_0^2\) coefficient makes the
ratio of its \(L_0\) and \(L_0^2\) coefficients equal to \(2X\),
impossible for a fixed complex polynomial. Hence \(C=0\).
A nonzero \(M_0L_0\) coefficient then makes the ratio of the
\(M_0\) and \(M_0L_0\) coefficients equal to \(X\), so \(B=0\).
The remainder \(1+A(X)M_0^2\) would force an irreducible
univariate quadratic over the algebraically closed field
\(\mathbb C\), again impossible. Thus the relation is linear:
\[
\lambda=r_0\mu+s_0,\qquad r_0,s_0\in\mathbb C.
\tag{18}
\]
This exception cannot be discarded: it satisfies the quadratic
identity with \(Q_2=-(W-r_0Y)^2/(X+s_0)^2\).
It is a necessary generic restriction, not a claimed actual
realization for arbitrary \(\mu\).

## 5. Normalization using only actual elementary maps

First change \(W_1=W-r_0Y,\ X_1=X+s_0\), leaving \(Y,Z\) fixed.
The inverse is \(X=X_1-s_0,\ W=W_1+r_0Y\).
The new projections satisfy
\(\vartheta_1=\vartheta-r_0t-2s_0\rho\),
\(y_1=y-s_0t\), and \(w_1\in L\).
The slope \(\mu\) is unchanged. Relabel, so that
\[
y=\mu\vartheta+\nu,\qquad w=\omega\in L,\qquad K_0=k_t\mu+k_\rho.
\tag{19}
\]
These lower-time changes preserve the full initial kernel,
literal \(\partial_Z\), \(N,L,t,\rho,a\), and the derivation \(P\).

The quadratic part of (17) is now uniquely \(-W^2/X^2\),
by comparison of powers of the transcendental \(\mu\).
Write \(F=Z-W^2/X^2+q_1(X)Y+q_2(X)W+q_0(X)\).
Then \(PF=0\), in the fraction field, is
\[
K_0-\frac{2\omega}{X}+q_1(X)\mu+q_2(X)X=0 .
\tag{20}
\]
Apply the quotient-vector argument of (10) to
\(L/(\mathbb C+\mathbb C\mu)\), clearing denominators in \(X\).
It gives
\[
K_0=c_1\mu+c_0,\qquad \omega=d_1\mu+d_0,\qquad c_i,d_i\in\mathbb C.
\tag{21}
\]

The actual maps
\[
Z_1=Z-c_1Y,\qquad W_1=W+(c_0/2)X-d_0
\tag{22}
\]
have inverse obtained by adding \(c_1Y\) and subtracting
\((c_0/2)X-d_0\), respectively.
The first decreases \(k_t\) by \(c_1\); the second increases
\(\vartheta\) by \(c_0/2\) and decreases \(k\) by \(c_0\rho\).
Thus after relabeling
\[
k_t\mu+k_\rho=0,\qquad w=d_1\mu,\qquad d_1\in\mathbb C^*.
\tag{23}
\]
If \(d_1=0\), the projected \(w\) is zero and the calibrated
Jacobian vanishes. All these maps preserve the literal pivot,
coefficient field and nonconstant \(\mu\).
They are not specializations of rational coefficients.

Wang's second alternative is preserved: the good variables undergo
only a constant linear combination and additions from \(K\),
and \(Z\) changes by a linear expression in a good variable.
Equation (20) now forces \(q_1=2d_1/X,\ q_2=0\).
Its fixed coordinate therefore differs from \(F_0/X^2\) by
an element of \(K\), where
\[
F_0=X^2Z-W^2+2d_1XY,\qquad
DY,DW\in K[F_0],\quad DF_0=0,\quad DW=\tau_0X .
\tag{24}
\]
No ambient-coordinate status of \(F_0\) is asserted.

## 6. Polynomial contraction and the odd-even contradiction

In the original fraction field,
\[
K[F_0]\cap B=\mathbb C[X,F_0].
\tag{25}
\]
Indeed \(X,F_0\) are algebraically independent.
For each \(c\in\mathbb C\), \(F_0\) modulo \(X-c\) is
transcendental over \(\mathbb C\): for \(c\ne0\) it is linear in
\(Z\), while for \(c=0\) it is \(-W^2\).
Thus \((X-c)B\cap\mathbb C[X,F_0]=(X-c)\mathbb C[X,F_0]\).
An element of the left side of (25) has a polynomial denominator
in \(X\). Factor it into \(X-c\)'s and repeatedly apply this
contraction to strip a minimal denominator. This proves (25).

Let \(b_0=DY\). Since \(\tau_0=DW/X\) is in \(K[F_0]\) and was
already proved to be an original polynomial, (25) gives
\[
b_0,\tau_0\in\mathbb C[X,F_0],\qquad
X\,DZ=2\tau_0W-2d_1b_0 .
\tag{26}
\]
The second equality follows by differentiating \(F_0\) and
cancelling one nonzero factor \(X\) in the domain.
It does not declare \(X\) invertible in \(B\).
Reduction modulo \(X\), where \(F_0=-W^2\), gives
\[
\tau_0(0,-W^2)\,W=d_1b_0(0,-W^2).
\tag{27}
\]
The left side is odd in the independent original variable \(W\);
the right side is even. Both vanish.
The substitution \(\mathbb C[T]\to\mathbb C[W]\), \(T\mapsto-W^2\),
is injective, so \(\tau_0(0,T)=0\).
Hence \(X\mid\tau_0\) in \(B\).
Since \(\tau_0\ne0\) and \(E\tau_0=0\), factorial closure of
\(\ker E\) forces \(EX=0\), contradicting \(a\ne0\).

This excludes the nonconstant-\(\mu\) alternative. Together with
Section3 it proves that under (1), \(E\) fixes an ambient coordinate
and \(A\simeq\mathbb C^{[3]}\).
It does not make \(a\) a unit, identify \(L\) with a rational field,
or give arbitrary entry into this degree profile and initial kernel.
The other degree and center reductions remain separate composition
inputs, not assumptions silently added to the present proof.

The actual chart and auxiliary-derivation sources were fully read,
and the exact primary statements were checked before use.
Independent outline reconstructions preceded this source; a complete
saved-source review is a separate check.
No saved checker was executed, imported or compiled, and no earlier
source or index was edited. This is working mathematics, not expert
review, proof-assistant certification, or historical novelty clearance.

