# Quadratic time does not imply Jacobian nilpotence

Status: bounded primary-source applicability audit and an actual negative
control for a proposed route. The supplied globally sliced exact1122
condition concerns degree in the action parameter. It neither makes the
action a quasi-translation nor forces the coefficient vector field to
have nilpotent Jacobian. Even replacing the vector field by its coordinate
accelerations does not automatically produce a quasi-translation.

The countercontrol below is the already recognized height-two family212,
not a new cancellation example. Its kernel is explicitly a polynomial
three-ring. The literature checks identify usable conditional endpoints,
not a theorem recognizing all globally sliced exact1122 frames.

## 1. Three different hypotheses

Work in characteristic zero. Write a polynomial derivation in the supplied
coordinates as
\[
E=\sum_{i=1}^n H_i\partial_{x_i},\qquad
H=(H_1,\ldots,H_n)^{\mathsf t},\qquad
K=(EH_1,\ldots,EH_n)^{\mathsf t}=JH\,H.
\tag{1}
\]
Here \(JH\) is the ordinary Jacobian matrix of the coefficient vector.
The condition that every supplied generator has E-time degree at most two
is
\[
E^3x_i=0\quad\text{for every }i,
\qquad\text{equivalently }JK\,H=0.
\tag{2}
\]
It gives the flow formula
\[
\exp(sE)(x)=x+sH+\frac{s^2}{2}K.
\tag{3}
\]
The indeterminate \(s\) in (3) is the action parameter, not an ordinary
coordinate. No ordinary total-degree bound on \(H\) occurs here.
Nor does (2) say that \(E^3\) is the zero operator on the whole ring:
if \(Eu=1\), then \(E^3(u^3)=6\).

A quasi-translation \(x+H\) instead satisfies \(JH\,H=0\), so the
corresponding derivation has \(E^2x_i=0\) for all supplied generators.
Separately, a Jacobian nilpotency-index hypothesis such as
\((JH)^3=0\) is a matrix identity. Neither it nor \(JH\,H=0\) is
the identity \(JK\,H=0\) in (2).

These distinctions also apply when two supplied coordinates have time
degree one and two have time degree two. The
[earlier literature audit199](time-degree-1122-primary-literature-audit-pass199-working.md)
already gives examples with that exact profile and unbounded ordinary
coefficient degree. Sections2--4 give a stronger obstruction: even
nilpotence of \(JH\) fails in an actual height-two frame.

## 2. Actual globally sliced frame, with both inverse orders

Start with independent coordinates \((u,t,y,z)\) and
\[
B=\mathbb C[u,t,y,z],\qquad E=\partial_u,
\qquad A=\ker E=\mathbb C[t,y,z].
\tag{4}
\]
Use the n=4 member of the
[actual family212](height-two-no-quadratic-relation-actual-control-pass212-working.md):
\[
\begin{aligned}
X&=u,&Y&=y+tu,\\
Z&=z+(3t^2y+t^4)u+t^3u^2,&
W&=t+XZ-Y^3\\
&&&=t-y^3+(z-3ty^2)u+t^4u^2.
\end{aligned}
\tag{5}
\]
The cubic terms in the last expression cancel exactly. In independent
capital coordinates define, in order,
\[
T=W-XZ+Y^3,\qquad
\widehat u=X,\qquad \widehat y=Y-XT,\qquad
\widehat z=Z-(3T^2\widehat y+T^4)X-T^3X^2.
\tag{6}
\]
After (5), the first expression gives \(T=t\), and the others give
\(\widehat u=u,\widehat y=y,\widehat z=z\). Conversely, substitute
(6) in (5): the first three reconstructed coordinates are \(X,Y,Z\)
by their definitions; the fourth is \(T+XZ-Y^3=W\).
Thus both compositions are identities in polynomial rings.

In particular \(B=\mathbb C[X,Y,Z,W]=A[u]\), with coordinate slice
\(EX=1\). The supplied time degrees are exactly1122 and
\[
(\operatorname{lc}_E X,\operatorname{lc}_E Y,
  \operatorname{lc}_E Z,\operatorname{lc}_E W)
=(1,t,t^3,t^4).
\tag{7}
\]
The initial image is \(\mathbb C[\eta,t\eta,t^3\eta^2,t^4\eta^2]\)
inside \(\mathbb C[t,\eta]\), with fraction field \(\mathbb C(t,\eta)\).
It has transcendence degree two, so the full initial kernel has height
two. The full ideal calculation in212 gives
\[
\ker\Theta=(\mathsf X\mathsf Z-\mathsf Y^3,
             \mathsf X\mathsf W-\mathsf Y\mathsf Z,
             \mathsf Y^2\mathsf W-\mathsf Z^2).
\tag{8}
\]
The height assertion here already follows from the displayed fraction
field, independently of using those ideal generators.

## 3. Exact original coefficient vector and a nonnilpotent Jacobian

Put
\[
F=3T^2Y+T^4-XT^3.
\tag{9}
\]
Differentiating (5) in \(u\), and using \(y=Y-XT\), gives the
following coefficient vector entirely in the original capital ring:
\[
\boxed{H=(EX,EY,EZ,EW)^{\mathsf t}
       =(1,T,F,Z+XF-3TY^2)^{\mathsf t}.}
\tag{10}
\]
Directly from \(T=W-XZ+Y^3\),
\[
ET=(Z+XF-3TY^2)-Z-XF+3Y^2T=0.
\tag{11}
\]
At the actual point \(p=(X,Y,Z,W)=(0,0,0,1)\), the matrix is
\[
JH(p)=
\begin{pmatrix}
0&0&0&0\\
0&0&0&1\\
-1&3&0&4\\
1&0&1&0
\end{pmatrix}.
\tag{12}
\]
For example the third row follows by differentiating (9), using
\(T(p)=1\) and \(dT(p)=dW\); the last row follows from (10).
Its characteristic polynomial and second trace are
\[
\det(\lambda I-JH(p))=\lambda^4-4\lambda^2-3\lambda,
\qquad \operatorname{tr}(JH(p)^2)=8.
\tag{13}
\]
Consequently this matrix is not nilpotent. If the polynomial matrix
\(JH\) had any nilpotence index, every point specialization would be
nilpotent. Hence no matrix-nilpotence theorem applies to this frame
merely from its exact1122 time profile.

This does not obstruct a different coordinate system with simpler
coefficients: (4) already provides one. Ordinary Jacobian nilpotence is
being tested in the supplied frame, exactly as required by the proposed
direct application.

## 4. The acceleration vector is not automatically a nice derivation

The second time derivatives in this same frame are
\[
K=(E^2X,E^2Y,E^2Z,E^2W)^{\mathsf t}
  =(0,0,2T^3,2T^4)^{\mathsf t}.
\tag{14}
\]
Equation(11) proves \(EK_i=0\), hence \(E^3x_i=0\), without a
large expansion. Form the different, actual polynomial derivation
\[
\mathcal K=2T^3\partial_Z+2T^4\partial_W.
\tag{15}
\]
Its action on the invariant \(T\) of the original derivation is
\[
\mathcal K(T)=2T^3(T-X),\qquad
\mathcal K^2(Z)=12T^5(T-X)\ne0.
\tag{16}
\]
Thus \(x+K\) is not a quasi-translation. In fact \(\mathcal K\) is
not locally nilpotent: a locally nilpotent derivation on a characteristic
zero domain cannot satisfy \(D(f)=gf\ne0\), by its degree function,
whereas (16) has this form for \(f=T\).

Also \([\mathcal K,E](Y)=\mathcal K(T)=2T^3(T-X)\ne0\).
The coordinatewise fact \(E(K_i)=0\) therefore supplies neither local
nilpotence nor commutation for the vector field formed from the \(K_i\).

## 5. Primary-source theorem audit

The following statements were checked against the linked primary
sources. The two publisher-abstract entries are identified as such;
this note does not represent their full articles as independently read.

### 5.1 Quasi-translations and ordinary quadratic hypotheses

In de Bondt,
[Quasi-translations and singular Hessians](https://arxiv.org/pdf/1501.05168),
Proposition1.3 equates the quasi-translation condition with
\(JH\,H=0\). Corollary5.6 gives a constant linear-span bound in
dimension at most three, or in dimension at most four when \(H\) is
homogeneous. Corollary5.9 gives the corresponding homogeneous
four-dimensional normal form. These require the nice condition
\(E^2x_i=0\), not merely (2); homogeneity is also additional in the
four-dimensional statement. The acceleration substitution is ruled out
by (16).

Sun's published paper
[On quadratic homogeneous quasi-translations](https://doi.org/10.1016/j.jpaa.2009.12.034),
JPAA214(2010),1962--1972, states in its publisher abstract that quadratic
homogeneous quasi-translations in dimension at most nine are linearly
triangularizable. Here quadratic homogeneous refers to the ordinary
coefficient polynomials, and quasi-translation still imposes the
straight-line condition. Neither hypothesis follows from quadratic time.

Liu, Du and Sun,
[Quadratic linear Keller maps of nilpotency index three](https://www.sciencedirect.com/science/article/pii/S0024379508000712),
Linear Algebra Appl.429(2008),12--17, states in its publisher abstract a
linear-triangularization result for \(F_A=x+(Ax)^{(2)}\) with
\((J((Ax)^{(2)}))^3=0\). The notation \((Ax)^{(2)}\) means coordinatewise
squaring. This is an ordinary power-linear quadratic map and a matrix
index condition. Formula(13) excludes even the latter inference here.

### 5.2 The actual dimension and fixed-coordinate gates

Dasgupta--Gupta,
[Nice derivations over principal ideal domains](https://arxiv.org/html/1701.03635v1),
contains these characteristic-zero statements:

- Corollary3.8 requires an irreducible LND on \(K^{[4]}\) with
  \(DX_1=0\) and \(D^2X_i=0\) for \(i=2,3,4\); its kernel is \(K^{[3]}\).
- Theorem4.1 restates Wang for an irreducible nonzero LND on
  \(K[X,Y,Z]\) with \(D^2X=D^2Y=0\). Its alternatives concern this
  three-variable polynomial ring over a field.
- Theorem4.8 restates Daigle for an irreducible LND on \(k^{[3]}\)
  with a variable \(Y\) satisfying \(DY\ne0,D^2Y=0\), and produces
  a triangular coordinate system retaining \(Y\).

The supplied E is not a derivation over \(\mathbb C(X)\) or
\(\mathbb C(Y)\), since it moves both good slots. Applying either
three-variable theorem over a coefficient field therefore requires a
separately constructed derivation fixing that field. A field coordinate
obtained afterward is not automatically an ambient coordinate.

Finally, Bhatwadekar--Gupta--Lokhande,
[Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]](https://arxiv.org/html/1501.01438v1),
Theorem3.5 assumes \(0\ne D\in\operatorname{LND}_{k[T]}k[T,X,Y,Z]\)
and a regular kernel, and concludes \(\ker D=k[T]^{[2]}\).
This is directly useful once an actual invariant ambient coordinate
\(T\) has been found. In the globally sliced setting the kernel is
regular: \(B=A[u]\) is regular, and regularity descends along this
faithfully flat polynomial extension. The invariant-coordinate
hypothesis, not regularity, is the missing input in a general
height-two frame.

## 6. What remains usable for the height-two branch

The audit establishes no published theorem that recognizes the entire
supplied globally sliced exact1122 setup from its time profile alone.
This is a statement about the exact theorems inspected, not a claim of
historical novelty or an exhaustive negative literature result.

The clean published endpoint is still to prove that the original E
annihilates an ambient polynomial coordinate, equivalently that its
rank is at most three. For example, a nonzero constant linear relation
between \(EX\) and \(EY\) supplies such a coordinate immediately.
This sufficient condition does not follow from height two of the full
initial ideal: the actual example above has good speeds \(1,t\).

An auxiliary-derivation route remains legitimate only with its original
ring hypotheses proved separately: local nilpotence, the annihilated
coefficient ring, primitive division if used, and a polynomial return
from any coefficient-field normal form. The
[retained commuting recognition criterion205](nice-commuting-invariant-coefficients-recognition-pass205-working.md)
is a conditional route of that kind. The acceleration derivation
(15) shows why replacing those gates by coordinatewise E-invariance
is invalid.

The construction also does not validate a uniform low-weight relation
strategy. Family212 allows arbitrarily large least weight of a second
initial relation while retaining a weight-three actual invariant
coordinate. Initial-ideal complexity and coordinate recognition are
different issues.

## 7. Audit boundaries

Sources199 and212 were reread completely for this note. The actual
frame, inverse and full initial ideal are retained from212; the matrix,
characteristic polynomial and acceleration computations above are
independent direct calculations. Fresh unsaved algebra corroborated
(10)--(16). No saved checker was executed, imported or compiled.
No earlier proof, checker, index or verification packet was changed.

Recent unverified preprint claims were not used as recognition inputs.
This note proves neither arbitrary coordinate entry nor unrestricted
complex threefold cancellation. Its example is already recognized by
\(EX=1\), is not a hypothetical nonpolynomial-kernel frame, and makes
no assertion of novelty, expert certification or formal verification.
