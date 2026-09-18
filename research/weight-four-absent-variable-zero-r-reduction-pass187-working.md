# The zero-R branch of the absent-variable quartic has an affine projection

**Status: working actual-chart reduction, not recognition.**

For the full initial relation \(X^2Z-Y^4\), assume that the
selected universal-chart coefficient \(R=k_\rho\) is zero.
Then \(n_\rho\ne0\), the first projected entry is an affine
parameter over the exact coefficient field, and the other
projected entries are explicit polynomials in it. Their remaining
determinant identities impose a quadratic coefficient-field cover.
None of these conclusions is an original-ring coordinate assertion.

A constant projected \(y\) is excluded using an actual commuting
coordinate partial and Wang's two-coordinate theorem. A proposed
shorter coefficient argument does not work: in that branch the
second projected slope is also constant in the generic parameter,
so its formal coefficient cannot be compared independently.

## 1. Actual supplied frame and the zero-R equations

Retain the actual hypotheses of
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md),
specialized to
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\qquad
a^2e=b^4 .
\end{gathered}
\tag{1}
\]
Here the four coordinates are actual polynomial coordinates and
\(\theta_0\) is the full weighted initial map with weights
\((1,1,2,2)\), sending the variables to
\(a\tau,b\tau,e\tau^2,h\tau^2\). In particular (1) is not merely
one vanishing leading relation.

The occurring \(Z\)-pivot supplies the exact data
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad L=\operatorname{Frac}(\ker_A N),
\quad A_L=L[v],\quad Nv=1,\quad a\in L^*,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2=t^4,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad
\mathbb C(y,z,w)=\operatorname{Frac}A=L(v),\\
J(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
      =-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent, their partials
extend uniquely and commute on the finite separable field \(L\),
and initially fix \(v\). The actual projections \(y,z,w\) are
algebraically independent over \(\mathbb C\).
On the localized chart \(E=a\partial_X\), fixing \(L[v]\).

Assume throughout this note
\[
R=k_\rho=0,\qquad K=\ker_L\partial_\rho,\qquad k\in K .
\tag{3}
\]
The field \(K\) is finite over \(\mathbb C(t)\), stable under
\(\partial_t\), and its \(\partial_t\)-constants are \(\mathbb C\).
For algebraicity, differentiate the monic minimal polynomial of
an element of \(K\) over \(\mathbb C(t,\rho)\). Minimality forces
all coefficients into \(\mathbb C(t)\). Finite independent sets
over \(\mathbb C(t)\) remain independent after adjoining the
transcendental \(\rho\), so their sizes are bounded by the finite
degree in (2). The same minimal-polynomial argument and algebraic
closedness of \(\mathbb C\) give the constant assertion.
No equality \(K=\mathbb C(t)\) is assumed.

For readability use primes for \(t\)-derivatives of \(q,k\in K\);
derivatives of other coefficients retain subscripts. The four
universal potentials specialize to
\[
\begin{gathered}
\sigma=q'y+k,\qquad z=\frac{q''}{2}y^2+k'y+n,\qquad n\in L,\\
\frac{q'''}6y^3+\frac{k''}{2}y^2+n_t y+n_\rho\vartheta=\ell,\\
n_\rho w+\mathcal T(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,
\qquad \ell,m\in L,\\
\mathcal T(U,V)=\frac{q''''}{24}U^4+\frac{k'''}6U^3
 +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2 .
\end{gathered}
\tag{4}
\]
For the literal form (1), \(q'''=24t\ne0\) and \(q''''=24\).
These equations involve the coefficient partials before evaluation,
not derivatives of formal \(U,V\).

## 2. What the constant-y determinant actually says

Suppose first that \(y\in L\). Then \(z,\sigma\in L\), and
the whole-line equality in (2) gives \(L[w]=L[v]\).
Thus \(w_v\in L^*\). As usual, \(y_\rho\ne0\): otherwise the
first row of \(J(X)\) is \((X+y_t,0,0)\), making its nonzero
constant value divisible by a positive-degree polynomial in \(X\).

Since the first two rows have zero \(v\)-entry, the literal
determinant factors. Direct substitution of (4) gives
\[
J(X)=(w_v+\vartheta_vX)(n_\rho X+C_0),\qquad
C_0=y_tz_\rho-y_\rho z_t\in L .
\tag{5}
\]
Indeed the \(X^2\) term of the second factor is
\(\sigma_\rho-y_\rho q'=0\); its \(X\) term is
\(z_\rho+y_t\sigma_\rho-y_\rho\sigma_t=n_\rho\).
The factors in (5) lie in the domain \(L[v][X]\).
Their product is a nonzero element of \(L\), hence a unit, so
\[
n_\rho=0,\qquad \vartheta_v=0,\qquad
C_0\in L^*,\qquad
y,z,\sigma,\vartheta\in L,\quad w_v\in L^* .
\tag{6}
\]

This does not force \(\ell_\rho=0\).
In fact, with \(n_\rho=0\), differentiating the cubic identity
in (4) shows
\[
C_0=-y_\rho\left(\frac{q'''}2y^2+k''y+n_t\right)
    =-\ell_\rho,\qquad
J(0)=-w_v\ell_\rho\ne0 .
\tag{7}
\]
The second potential in (4) contains \(-\ell_\rho\vartheta\),
but now \(\vartheta\in L\). It is not a polynomial identity in an
independent variable \(\vartheta\). Comparing its purported
\(\vartheta\) coefficient would therefore be invalid.
The next section supplies the additional argument that is needed.

## 3. An actual coordinate partial and the constant-y exclusion

Put \(L_0=\mathbb C(y,z)\subset L\). Equations (2) and (6) give
\[
L_0(w)=\mathbb C(y,z,w)=L(v)=L(w).
\]
Since \(w\) is transcendental over \(L\), one has
\(L\cap L_0(w)=L_0\).
To see this, write any element of the intersection as \(P(w)/Q(w)\)
with \(P,Q\in L_0[w]\), \(Q\ne0\), and compare a nonzero
coefficient in \(P-\xi Q=0\).
Intersecting the displayed fields with \(L\) proves
\[
L=\mathbb C(y,z).
\tag{8}
\]
This is a field consequence of the actual inverse, not a conclusion
that \(\ker_A N=\mathbb C[y,z]\) as an original ring.

The derivation \(\partial_w\) of \(L(X,w)\), fixing \(L,X\),
kills the actual \(X,Y,Z\) and sends the actual \(W\) to one.
It is consequently the original polynomial partial \(\partial_W\).
Since \(E=a\partial_X\) and \(a\in L\), it commutes with \(E\).
Thus the original three-ring is stable:
\[
[E,\partial_W]=0,\qquad
D:=E|_{\mathbb C[X,Y,Z]}\in
\operatorname{LND}_{\mathbb C}(\mathbb C[X,Y,Z])\setminus\{0\},
\qquad D^2X=D^2Y=0 .
\tag{9}
\]
No slice for \(D\) is assumed.

Divide the polynomial coefficient gcd \(\delta\) to write
\(D=\delta D_0\). The identity \(D\delta=\delta D_0\delta\)
and additivity of LND degree imply \(D\delta=0\):
a nonzero left side would have degree \(\deg_D\delta-1\),
while the right side has degree at least \(\deg_D\delta\).
Then \(D_0\delta=0\), and
\(D^j f=\delta^jD_0^j f\).
Therefore \(D_0\) is a nonzero irreducible LND with the same kernel,
and \(D_0^2X=D_0^2Y=0\).

Wang's theorem, in Dasgupta--Gupta Theorem 4.1, now applies to
the actual coordinates \(X,Y,Z\).
Its first alternative supplies an invariant nonzero complex
linear form in \(X,Y\), forcing a complex linear relation
between \(1\) and the transcendental \(t=b/a\). This is impossible.
The second supplies an invariant \(\xi\) with
\(\mathbb C[X,Y,\xi]=\mathbb C[X,Y,Z]\).
The inverse one-variable polynomial presentations over
\(\mathbb C[X,Y]\) force
\[
\xi=cZ+Q(X,Y),\qquad c\in\mathbb C^*,\quad
Q\in\mathbb C[X,Y],\qquad E\xi=0 .
\tag{10}
\]
For a nonzero highest homogeneous part \(Q_j\),
\(Q_j(a,b)=a^jQ_j(1,t)\ne0\), since \(t\) is transcendental.
Thus a nonconstant \(Q(X,Y)\) has time degree equal to its
ordinary degree. Invariance in (10), and \(\deg_E Z=2\),
force that degree to be two. The leading coefficient then gives
\[
0=ce+Q_2(a,b)
  =a^2\{ct^4+Q_2(1,t)\},
\tag{11}
\]
which is impossible. This excludes \(y\in L\).

The argument reproduces the actual field and commuting-partial
steps of the earlier
[cusp zero-second-coefficient exclusion172](cusp-zero-r-constant-projection-exclusion-pass172-working.md),
but uses the present quartic relation in its final contradiction.
No cusp relation or cusp recognition conclusion is imported.

## 4. The remaining zero-R branch is an exact cubic graph

We now know that \(y\in L[v]\) is nonconstant, hence transcendental
over \(L\). If \(n_\rho=0\), the first potential in (4) would
give a nonzero cubic equation in \(y\), whose leading coefficient
is \(q'''/6=4t\ne0\). This is impossible. Therefore
\[
s:=n_\rho\ne0 .
\tag{12}
\]
Define exact polynomials over \(L\) by
\[
\begin{aligned}
P(U)&=\frac{\ell-q'''U^3/6-k''U^2/2-n_tU}{s},\\
\mathcal W(U)&=
 \frac{m-\mathcal T(U,P(U))+\ell_tU+\ell_\rho P(U)}{s}.
\end{aligned}
\tag{13}
\]
The potentials prove
\[
\vartheta=P(y),\quad \deg P=3,\qquad
w=\mathcal W(y),\quad\deg\mathcal W\le6,\qquad
z=\frac{q''}{2}y^2+k'y+n .
\tag{14}
\]
All divisions are by nonzero field elements, not original-ring
units. Since \(L[y,z,w]=L[v]\), these identities give
\[
L[y]=L[v],\qquad y=\gamma v+\eta,\qquad
\gamma\in L^*,\quad\eta\in L .
\tag{15}
\]
The equality of rings, not just function fields, makes \(y\)
an affine parameter: the degrees of inverse one-variable
polynomial expressions multiply to one.

This proof does not use the common-factor whole-plane or
selected-component arguments184. In the present branch the
two undivided potentials themselves produce (13)--(15).

## 5. Exact remaining determinant identities

For coefficient partials now extended to fix the independent
\(U\), put
\[
B_1(U)=\frac{q'''}2U^2+k''U+n_t=-sP_U(U).
\]
The universal determinant-preserving row reduction in this
zero-R branch reads
\[
dY=dy+Xdt,\qquad dZ_{\rm red}=B_1(y)dt+s\,d\rho,\qquad
dW=dw+X\,d\vartheta+X^2d\rho .
\tag{16}
\]
Its coefficient of \(X\), followed by its constant term, gives
\[
\begin{gathered}
0=s\{w_v-(P_t+P_UP_\rho)(y)y_v\},\\
J(0)=-s\{\mathcal W_t+P_U\mathcal W_\rho\}(y)y_v=-a^3 .
\end{gathered}
\tag{17}
\]
Here the formal polynomial coefficient derivatives precede
evaluation at \(y\). For example
\(d\vartheta=P_U(y)dy+P_t(y)dt+P_\rho(y)d\rho\);
the \(P_Udy\) contribution vanishes in the relevant first wedge.
This gives the signs displayed in (17).

Evaluation at the affine \(y\) is injective on \(L[U]\), so
\[
\mathcal W_U=P_t+P_UP_\rho,\qquad
\mathcal W_t+P_U\mathcal W_\rho=\frac{a^3}{s\gamma}\in L^*,
\qquad \gamma=Ny .
\tag{18}
\]
In particular the factor \(\gamma\) cannot be dropped or replaced
by one. Equivalently the recalibrated determinant is
\(J_y=-a^3/\gamma\).

A further necessary condition follows from the highest coefficient.
Let \(A_3=-q'''/(6s)\ne0\), the cubic coefficient of \(P\).
The first identity in (18) gives
\([\!U^6\!]\mathcal W=A_3(A_3)_\rho/2\).
The \(U^8\) coefficient of the second is consequently
\[
\frac32 A_3\{(A_3)_\rho^2+A_3(A_3)_{\rho\rho}\}=0,\qquad
\partial_\rho^2(A_3^2)=0,\qquad
\partial_\rho^2(s^{-2})=0 .
\tag{19}
\]
The last equivalence uses \(q'''\in K^*\). A vanishing degree-six
coefficient of \(\mathcal W\) causes no exception to this computation.

## 6. A quadratic coefficient-field cover, not global descent

Set \(\eta_0=1/s\) and use the derivation
\(\partial_n=\eta_0\partial_\rho\) on \(L\). It has
\(\partial_n n=1\) and constant field \(K\).
Equation (19) gives
\[
\partial_n^2\eta_0
 =\frac{\eta_0}{2}\partial_\rho^2(\eta_0^2)=0.
\]
Subtracting explicit primitives twice yields
\[
\eta_0=A_cn+B_c,\qquad
\rho=\frac{A_c}{2}n^2+B_cn+C_c,\qquad A_c,B_c,C_c\in K .
\tag{20}
\]
Indeed \(A_c=\partial_n\eta_0\) is in \(K\),
\(B_c=\eta_0-A_cn\) is killed by \(\partial_n\), and then so is
\(C_c=\rho-A_cn^2/2-B_cn\).
The two coefficients \(A_c,B_c\) cannot both be zero.

This is not an assertion that \(A_c\) is complex, that
\(s_\rho=0\), or that \(L=K(n)\). It permits a genuine quadratic
cover in the coefficient variables. Further identities or actual
field-return arguments would be required for any stronger claim.

## Scope, sources and the unresolved step

The conclusion proved here is the bounded implication
\[
\boxed{\quad k_\rho=0
 \ \Longrightarrow\ n_\rho\ne0,\quad L[y]=L[v],\quad
 \deg_U P=3,\quad \deg_U\mathcal W\le6,\quad
 \text{identities (18)--(20).}\quad}
\tag{21}
\]
The constant-y branch required the commuting-partial and Wang
argument, not the invalid coefficient comparison discussed after (7).

For that external step, the exact two alternatives and hypotheses
of Wang's theorem were checked in N. Dasgupta and N. Gupta,
[Nice derivations over principal ideal domains](https://arxiv.org/pdf/1701.03635v1),
Theorem 4.1, printed page 9. This retains the published classification
as an input, without claiming a recursive audit of Wang's proof.
The earlier [zero-r cusp reduction160](cusp-zero-r-generic-graph-pass160-working.md)
was fully read; (16)--(20) above rederive the needed identities
with the nonconstant cubic coefficient \(q'''/6=4t\).

More generally, the same reduction is valid in a supplied actual
universal chart with \(q_\rho=0\) and \(q'''\ne0\):
the putative equation \(cq+Q_2(1,t)=0\) in (11) is contradicted
by differentiating three times in \(t\). This observation is
conditional on that actual chart, not a classification of initial forms.

No invariant ambient coordinate has been obtained from (13).
Its coefficients lie in \(L\), the speed \(a\) need not be a global
unit, and the affine normalization factor \(Ny\) remains present.
The next task is to solve enough of the remaining scalar identities
and exact actual return \(\mathbb C(y,z,w)=L(y)\) to construct an
original polynomial coordinate, or to find a valid further obstruction.
A rational graph or a coefficient-field polynomial alone does not do so.

The branch \(k_\rho\ne0\), other quartic normal forms, height-two
initial kernels, arbitrary coordinate entry and unrestricted
cancellation remain separate. No test was executed, imported or
compiled, and no186 or earlier source was changed. This is not
a historical novelty claim, human expert certification, proof-assistant
verification, submission or external contact.
