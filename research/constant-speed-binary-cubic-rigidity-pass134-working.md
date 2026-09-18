# A constant leading speed forces a pure-cube binary residue

The statement below is a working mathematical result with the listed dependencies.

For an actual three-good quadratic frame, a primitive mixed-cubic
relation whose leading linear speed is a nonzero constant has a
pure-cube binary residue. This restriction precedes both correction
tests. The actual Jacobian first makes complementary factors units
on a selected generic component, then excludes the remaining
double-root line component.

This is leading-form rigidity, not a new cancellation recognition.
A nonzero constant speed of an actual affine-linear good coordinate
already gives a coordinate slice and a polynomial kernel.
Neither correction test is proved to pass here.

## 1. Normalized statement and original-coordinate scope

It suffices to prove the following assertion:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}(B),\qquad EX=1,\\
E^2Y=E^2Z=0,\qquad t=EY,\quad r=EZ,\qquad
t,r\text{ algebraically independent},\\
E^2W=2C(t,r),\qquad E^3W=0,\qquad
0\ne C\in\mathbb C[T,R]_3.
\end{gathered}
\tag{1}
\]
Here the subscript denotes homogeneous degree three, and all four
generators are actual polynomial coordinates. The conclusion is
\[
C(T,R)=\gamma(\alpha T+\beta R)^3,\qquad
\gamma\in\mathbb C^*,\quad(\alpha,\beta)\ne(0,0).
\tag{2}
\]

For the application, suppose a dense three-good frame has a
primitive relation \(L(a)q=2F_3(a)\) with \(L(a)\in\mathbb C^*\).
A constant linear good change and rescaling make \(EX=1\) and
rewrite the relation as \(q=2\widetilde F_3(1,t,r)\).
Write
\(\widetilde F_3(X,Y,Z)=XJ_2(X,Y,Z)+C(Y,Z)\).
The actual bad shear \(W=z-J_2(x)\) gives (1).
Primitivity makes \(C\ne0\); density makes \(t,r\) independent.
Conclusion (2) therefore says that the restriction of the
original \(F_3\) to \(\ker L\) is a nonzero cube, up to scalar.
No correction test is used in this normalization.[^1]

Put \(u=X\), \(A=\ker E\). The slice theorem and the actual
coordinate \(X\) give \(B=A[u]\) and
\(A\simeq B/(X)\simeq\mathbb C^{[3]}\).
Finite Taylor projection to \(u=0\) yields actual generators
\(y,z,w\) of \(A\), and \(d\in A\), with
\[
Y=y+tu,\qquad Z=z+ru,\qquad
W=w+du+C(t,r)u^2,\qquad A=\mathbb C[y,z,w].
\tag{3}
\]
Thus the displayed map from \((u,y,z,w)\) to \((X,Y,Z,W)\)
is an actual polynomial automorphism. Its Jacobian is \(1\):
it is a complex unit, and at \(u=0\) its three-by-three block
on the last three variables is the identity.

## 2. A normalized generic intrinsic parameter

Let \(T=\partial_W\), holding \(X,Y,Z\) fixed. The actual dense
cofactor theorem gives \(T(A)\subset A[u]_{\le2}\), with a
nonzero quadratic coefficient.[^2] Here \(Tu=0\), because \(u=X\).
Put \(N(f)=[u^2]T(f)\) for \(f\in A\).
This is a nonzero derivation of \(A\), and the coefficient of
\(u^{2j}\) in \(T^j(f)\) is \(N^j(f)\). Local nilpotence of
\(T\) proves that \(N\) is locally nilpotent.
The cubic coefficients of \(T(Y)=T(Z)=0\) give \(N(t)=N(r)=0\).

Let \(S=\ker_A N\) and \(L=\operatorname{Frac}S\).
A local slice divided by its nonzero invariant derivative gives
\[
A_L=L[v],\qquad Nv=1,\qquad
F:=\operatorname{Frac}A=L(v),\qquad
[L:\mathbb C(t,r)]<\infty.
\tag{4}
\]
The first assertions follow from the finite local-slice Taylor
formula.[^3] For the last one, \(t,r,v\) are a transcendence
basis of the finitely generated field \(F\), so
\(F/\mathbb C(t,r,v)\) is finite. Linear independence over
\(\mathbb C(t,r)\) persists after adjoining the transcendental
element \(v\), proving finiteness of \(L/\mathbb C(t,r)\).

Extend \(\partial_t,\partial_r\) uniquely through this finite
separable extension, then to \(F=L(v)\) by killing \(v\).
Let \(\partial_v\) kill \(L\). These derivations commute, and
the constants of \(\partial_v\) are exactly \(L\).
The functions in (3), and all their \(t,r\) derivatives, belong
to \(L[v]\). No rationality of \(L/\mathbb C(t,r)\), global
\(N\)-slice, or global equality \(A=S[v]\) is assumed.
No identification of \(S\) as an affine plane is needed.

Set \(p=(y,z)^T\), \(a=(t,r)^T\), and
\(M=(\partial p_i/\partial a_j)_{i,j}\).
At fixed \(u\), let \(j(u)\) be the Jacobian determinant of
\((Y,Z,W)\) with respect to \((t,r,v)\).
The actual unit Jacobian following (3) gives
\(j(u)=j(0)=j_0\in F^*\).
Cramer's rule then gives
\[
T(v)=\frac{\det(M+uI_2)}{j_0},\qquad
[u^2]T(v)=\frac1{j_0}=N(v)=1,
\qquad j(u)=1.
\tag{5}
\]
The coefficient map on rational functions is the quotient-rule
extension of \(N\), so the comparison applies to the localized
slice \(v\). The conclusion \(j_0=1\) uses this particular
normalization. It is not a claim that arbitrary rational-frame
volume denominators are constants.

## 3. Three exact coefficient identities

All coefficient gradients and Hessians use \((t,r)\).
The block determinant expands as
\[
\begin{aligned}
j(u)={}&\det(M+uI_2)(w_v+u d_v)\\
&-(\nabla w+u\nabla d+u^2\nabla C)^T
           \operatorname{adj}(M+uI_2)p_v.
\end{aligned}
\tag{6}
\]
Its cubic coefficient is \(d_v-\nabla C^Tp_v\), so
\(d=\nabla C^Tp+k\) with \(k\in L\).
Using
\(\operatorname{adj}(M+uI_2)=\operatorname{adj}M+uI_2\) and
\(M+\operatorname{adj}M=(\operatorname{tr}M)I_2\),
the quadratic coefficient reduces to
\(w_v-(\operatorname{Hess}C\,p+\nabla k)^Tp_v\).
After its integration, the linear coefficient is
\(-\nu^Tp_v\), where
\(\nu=\nabla C(p)+\operatorname{Hess}k\,p+\nabla\ell\).
Symmetry of the constant third derivative tensor of \(C\)
identifies the first term with \(\nabla C(p)\). Consequently
\[
\begin{gathered}
d=\nabla C(t,r)^Tp+k,\\
w=\tfrac12p^T\operatorname{Hess}C(t,r)p+\nabla k^Tp+\ell,\\
C(p)+\tfrac12p^T\operatorname{Hess}k\,p+\nabla\ell^Tp=m,
\qquad k,\ell,m\in L.
\end{gathered}
\tag{7}
\]
Each element of \(L\) is obtained by subtracting the displayed
expression and observing that its \(v\) derivative is zero.
No existence of antiderivatives in \(L\) is assumed.

Define the nonzero formal plane cubic
\[
\begin{gathered}
G(U,V)=C(U,V)+\tfrac12(U,V)\operatorname{Hess}k\,(U,V)^T
                  +\nabla\ell^T(U,V)^T-m,\\
G(p)=0,\qquad
1=-\nabla G(p)^T\operatorname{adj}M\,p_v.
\end{gathered}
\tag{8}
\]
The last equality is the constant coefficient of (6).
These are actual coefficient identities, not a proposed
Jacobian array asserted to be realizable.

## 4. The selected component and its complementary factor

Equation (7) makes \(w\) polynomial in \(y,z\) over \(L\).
Hence \(A_L=L[y,z,w]=L[y,z]=L[v]\).
The evaluation map \(L[U,V]\to L[v]\) is surjective with
kernel generated by an irreducible polynomial \(P\).
Its degree is between one and three because \(P\mid G\).
Writing \(G=PR\), (8) becomes
\[
1=-R(p)\,\nabla P(p)^T\operatorname{adj}M\,p_v.
\tag{9}
\]
Every factor belongs to \(L[v]\), so \(R(p)\in L^*\).
In particular this component has multiplicity one.
The full cubic has not been assumed irreducible.

If \(\deg P=2\), the complementary \(R\) has degree one.
But \(R(p)=c\in L^*\) implies \(P\mid R-c\), impossible by
degree. This case is excluded.

If \(\deg P=3\), its curve is a closed embedded affine line
of degree three. Its leading form is a pure cube by the
elementary low-degree embedded-line argument.[^4]
Here is the needed algebraic proof. Over an algebraic closure
of \(L\), a closed-immersion parametrization has maximum
coordinate degree equal to the curve degree: pull back a
generic projective line along the birational completion.
After canceling equal leading terms, the only possibility
with both degrees greater than one is \((3,2)\).
Affine plane and parameter changes put that case in the form
\((av^3+bv,v^2)\), \(a\ne0\). If \(b\ne0\), two distinct
nonzero opposite parameters have the same image; if \(b=0\),
both coordinate derivatives vanish at zero. Neither is a
closed immersion. Thus one coordinate is linear in the
parameter and the curve is an affine-linear graph.
Its leading cubic is a pure cube.
As this leading form is proportional to the fixed complex
cubic \(C\), the conclusion descends to a cube over \(\mathbb C\).

If \(\deg P=1\), then \(R(p)=c\) gives \(R=c+PQ\).
Thus \(G=cP+P^2Q\), and the top cubic is divisible by the
square of the leading linear form of \(P\).
Since \(C\) splits into constant complex linear factors,
that leading form is proportional over \(L\) to a constant
factor of \(C\).
This excludes squarefree \(C\). Apart from the conclusion
(2), only a double factor with one distinct factor remains.

## 5. The double-root line contradicts the actual Jacobian

In the remaining case, a constant linear change of the two
good coordinates and their speeds makes
\(C(T,R)=\gamma T^2R\), \(\gamma\ne0\).
The line component is \(U=f\) for some \(f\in L\), so the
actual base coordinate \(y\) equals \(f\).
Also \(L[y,z]=L[v]=L[z]\); polynomial identities on the line
can therefore be compared as polynomials in \(z\).
We have
\[
\begin{gathered}
G(U,V)=\gamma U^2V+\tfrac12k_{tt}U^2+k_{tr}UV+
        \tfrac12k_{rr}V^2+\ell_tU+\ell_rV-m,\\
G(f,z)=0\ \Longrightarrow\quad
k_{rr}=0,\qquad \gamma f^2+k_{tr}f+\ell_r=0,\\
R(f,z)\in L^*\ \Longrightarrow\quad
G_U(f,z)\in L^*\ \Longrightarrow\ k_{tr}=-2\gamma f.
\end{gathered}
\tag{10}
\]
Differentiating the last equality in \(r\), and using
commutativity with \(k_{rr}=0\), gives \(f_r=0\).

An element of \(L\) killed by \(\partial_r\) is algebraic
over \(\mathbb C(t)\). To see this, differentiate its monic
minimal polynomial over \(\mathbb C(t)(r)\). The resulting
lower-degree annihilating polynomial is zero, so every
coefficient has zero \(r\) derivative and lies in \(\mathbb C(t)\).
Thus \(y=f\) is algebraic over \(\mathbb C(t)\).
The actual coordinate \(y\) is nonconstant, so \(t\) is in
turn algebraic over \(\mathbb C(y)\).

But \(t\in A=\mathbb C[y,z,w]\), and \(\mathbb C(y)\) is
relatively algebraically closed in \(\mathbb C(y,z,w)\).
Therefore \(t\in\mathbb C(y)\cap A=\mathbb C[y]\).
It is nonconstant because \(t,r\) are independent.
Now \(Y=y+t(y)u\). The first two rows of the actual Jacobian
from \((u,y,z,w)\) to \((X,Y,Z,W)\) make its determinant
divisible by \(1+u t'(y)\). This is a nonconstant polynomial
in characteristic zero, contradicting the unit Jacobian.
The double-root case is impossible, proving (2).

## 6. The correction gap is still separate

For \(H=XW-C(Y,Z)\), equations (3) and (7) give \(E^2H=2k\).
The first correction condition is still the separate claim
\[
k\in\operatorname{span}_{\mathbb C}
\{C(t,r),1,t,r,t^2,tr,r^2\}.
\]
Neither that membership nor the second correction test is
proved here. The result only restricts the leading binary cubic.

It does not make a nonconstant \(L(a)\) constant or supply a
three-good frame for an arbitrary sliced action. The actual
coordinate slice in (1) already recognizes the kernel,
independently of this leading-form restriction.

## Sources

1. [Correcting a mixed cubic relation to an invariant coordinate](three-good-mixed-cubic-correction-criterion-pass130.md),
   Sections 1--3. Leading relations, primitivity, and covariance under
   fixed-good quadratic bad shears.
2. [Dense three-good speeds force exact bad-partial adjoint degree two](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5. Actual cofactor bounds and the nonzero quadratic coefficient.
3. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. Leading local nilpotence and finite local-slice Taylor formula.
   No affine-plane quotient theorem is needed here.
4. [Cubic slices with a variable occurring linearly](cubic-linear-variable-pass.md),
   Section 2, “The smooth irreducible fiber.” Its elementary degree-three
   embedded-line argument is reproduced above in algebraically closed
   characteristic zero, without invoking a general line-embedding theorem.

[^1]: [Mixed-cubic criterion130](three-good-mixed-cubic-correction-criterion-pass130.md), Sections 1--3.
[^2]: [Actual dense cofactor theorem132](dense-three-good-adjoint-degree-pass132.md), Sections 2--5.
[^3]: [Intrinsic-speed construction125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^4]: [Elementary cubic plane lemma](cubic-linear-variable-pass.md), Section 2.
