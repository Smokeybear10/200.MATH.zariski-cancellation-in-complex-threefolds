# Primitive return rigidity for two triangular middle shears

A particular two-shear deformation of the divided-difference frame
cannot produce a primitive correction failure. The first shear may
initially have arbitrary polynomial dependence on the second invariant
parameter. If the reconstructed frame returns to the dense three-good
quadratic profile with acceleration outside the good-speed quadratic
span, that dependence disappears. Both correction gates then pass,
with corrected invariant equal to the original coordinate \(-a\).

This concerns the explicit family below, not arbitrary elementary
words. The construction starts with a translation whose invariant ring
is already a polynomial ring. It gives a restriction on a search for
counterexamples, not a new recognition theorem for unknown kernels.

## 1. The actual two-shear family and its inverse

Work in \(\mathcal B=\mathbb C[u,v,a,b]\), with
\(E=\partial_u\). First use the actual coordinates
\((u,Y,a,b)\), where \(Y=v+au\).
Choose arbitrary polynomials
\(R\in\mathbb C[u,Y,b]\) and
\(G\in\mathbb C[u,Y,A]\). Perform the successive elementary
shears
\(A=a+R(u,Y,b)\) and
\(B_1=b+G(u,Y,A)\), holding \(u,Y\) fixed.

Use the cubic divided difference from the actual frame129:[^1]
\[
\begin{gathered}
\Delta(A,V,u)=\frac32AV^2+\frac32A^2Vu+\frac12A^3u^2,
\qquad
u\Delta(A,V,u)=\frac{(V+Au)^3-V^3}{2},\\
V=Y-Au,\qquad X=u,\qquad
W=B_1+\Delta(A,V,u),\\
Z=A-\frac{V^3}{2}+B_1u
  =A-\frac{Y^3}{2}+uW.
\end{gathered}
\tag{1}
\]
Every displayed expression is polynomial, including on \(u=0\).
The complete endpoint inverse is
\[
\begin{gathered}
u=X,\qquad A=Z-XW+Y^3/2,\qquad V=Y-AX,\\
B_1=W-\Delta(A,V,X),\qquad
b=B_1-G(X,Y,A),\\
a=A-R(X,Y,b),\qquad v=Y-aX.
\end{gathered}
\tag{2}
\]
For the forward substitution, the divided-difference identity recovers
\(A\), after which each remaining line reverses one previous step.
Conversely, (2) gives \(V+AX=Y\) and
\(B_1+\Delta(A,V,X)=W\). The divided-difference identity then
gives
\(A-V^3/2+B_1X=A-Y^3/2+XW=Z\).
The two shear inverses recover the original \(a,b,v\).
Thus both inverse orders hold in polynomial rings. In particular,
\(X,Y,Z,W\) are actual coordinates, with no localization.

## 2. Hypotheses and conclusion

Assume the endpoint has the target profile:
\[
\begin{gathered}
E^2Z=0,\qquad E^3W=0,\qquad q=E^2W\ne0,\qquad r=EZ,\\
EX=1,\qquad EY=a,\qquad
a,r\text{ algebraically independent},\\
W_2=\operatorname{span}_{\mathbb C}
 \{1,a,r,a^2,ar,r^2\},\qquad q\notin W_2.\\[2pt]
\text{Then }R=P_3(u,Y)+P_2(u,Y)+P_1(u,Y)+P_0,
\quad P_j\in\mathbb C[u,Y]_j,\quad P_0\in\mathbb C.
\end{gathered}
\tag{3}
\]
Here \(\mathbb C[u,Y]_j\) means homogeneous degree \(j\).
The independence of \(a,r\) is exactly density of the homogeneous
speed cone for the row \((1,a,r)\). Its ideal is automatically the
unit ideal because its first entry is \(1\).
The nonmembership condition is the fixed-good nonremovability
condition used in128.[^2]

In fact the degree reductions below use only the weaker condition
\(q\notin\operatorname{span}_{\mathbb C}\{1,a,a^2\}\).
The full hypotheses in (3) specify the intended primitive-profile
application.

## 3. The first degree reduction

Put
\(\Psi(u,Y,A)=G(u,Y,A)+\Delta(A,Y-Au,u)\).
Then \(W=b+\Psi(u,Y,A)\).
Since \(A=Z-uW+Y^3/2\), its \(E\)-degree is at most three.

Decompose \(R\) into homogeneous parts in \(u,Y\), with
coefficients in \(\mathbb C[b]\). For a nonzero part of degree
\(j>0\), substitution of \(Y=v+au\) gives
\[
[u^j]R_j(u,v+au,b)=R_j(1,a,b)\ne0.
\quad
\text{If }c(a,b)\notin\mathbb C[a],\text{ then }
(\tau,a\tau,c(a,b)\tau^j)
\text{ are algebraically independent.}
\tag{4}
\]
The first assertion follows because distinct powers of \(Y\) give
distinct powers of the independent variable \(a\).
Thus the degree of \(R\) in \(u,Y\) is at most three.

For the second assertion, a polynomial depending nontrivially on
\(b\) is transcendental over \(\mathbb C(a)\).
Consequently \(a,c(a,b),\tau\) are independent. The three displayed
initials recover them rationally, so are also independent.
This proves that the \(E\)-degree on the three-generator subalgebra
is exactly the weighted polynomial degree with weights \((1,1,j)\).
It does not assert that any coordinate initials generate the full
associated graded ring of \(\mathcal B\).

If \(R_3(1,a,b)\) depended on \(b\), (4) with \(j=3\)
would apply to \(u,Y,A\). Because \(b\) is invariant and
\(W=b+\Psi\) has degree two, \(\Psi\) would have weighted
degree at most two. It could not involve \(A\), and would be an
ordinary polynomial of degree at most two in \(u,Y\).
Then \(q\) would lie in \(\operatorname{span}\{1,a,a^2\}\),
a contradiction.

Therefore \(R_3=P_3(u,Y)\) has constant coefficients. Set
\(A_2=A-P_3(u,Y)\), and rewrite \(W\) polynomially in
\(u,Y,A_2\). Comparison of the \(u^3\) coefficients in
\(Z=A_2+P_3-Y^3/2+uW\) gives
\[
q=Q(a):=a^3-2P_3(1,a),\qquad \deg Q=3.
\tag{5}
\]
The degree is exactly three because a polynomial of degree at most
two in \(a\) would belong to \(W_2\).

## 4. The quadratic and linear parts

Suppose \(c_2=R_2(1,a,b)\) depends on \(b\).
The initials of \(u,Y,A_2\) are independent with weights
\((1,1,2)\). The degree bound on \(W\) therefore gives
\[
\begin{array}{ll}
j=2:&
q=2\kappa c_2+H_2(a),
\quad \kappa\in\mathbb C,\quad \deg H_2\le2;\\
j=1:&
q=2K_2(1,a,c_1),
\quad K_2\text{ a constant-coefficient homogeneous quadratic},
\quad c_1=R_1(1,a,b).
\end{array}
\tag{6}
\]
In the first line, the only possible dependence of a weight-at-most-two
polynomial on \(A_2\) is a constant multiple of \(A_2\).
Since \(q=Q(a)\) and \(c_2\) depends on \(b\), this forces
\(\kappa=0\), contradicting (5).
Thus \(R_2=P_2(u,Y)\) has constant coefficients.

Now set \(A_1=A_2-P_2(u,Y)\) and again rewrite \(W\) in
\(u,Y,A_1\). If \(c_1\) depends on \(b\), (4) with
\(j=1\) gives the second line of (6).
The independence of \(a,c_1\) means that equality with \(Q(a)\)
forces all terms involving \(c_1\) to vanish. What remains has
degree at most two in \(a\), again contradicting (5).
Therefore \(R_1=P_1(u,Y)\) has constant coefficients.

## 5. The degree-zero coefficient also cannot depend on \(b\)

After the preceding subtractions, put
\(A_0=A_1-P_1(u,Y)=a+R_0(b)\).
It is invariant, and \(W=b+\Psi_0(u,Y,A_0)\) for a polynomial
\(\Psi_0\). If \(R_0\) were nonconstant, then \(a,A_0\)
would be algebraically independent. The initial map
\[
\mathbb C[U_0,Y_0,A_0]\longrightarrow
\mathbb C[a,b,\tau],\qquad
(U_0,Y_0,A_0)\longmapsto(\tau,a\tau,a+R_0(b))
\tag{7}
\]
would be injective, with weights \((1,1,0)\).
Equivalently, every nonzero homogeneous part in \(U_0,Y_0\),
with coefficients in \(\mathbb C[A_0]\), keeps its degree after
substitution. Its coefficients cannot cancel because \(a,A_0\)
are independent.

Thus \(\Psi_0\) has degree at most two in \(u,Y\) over
\(\mathbb C[A_0]\). It follows that \(q\) is a polynomial of
degree at most two in \(a\), with coefficients in
\(\mathbb C[A_0]\). Equality with the cubic \(Q(a)\) is
impossible in the polynomial ring \(\mathbb C[a,A_0]\).
Hence \(R_0=P_0\in\mathbb C\), proving (3).

## 6. Explicit successful correction

Define the homogeneous cubic and its mixed expression by
\(F_3(X,Y,Z)=Y^3/2-P_3(X,Y)\) and
\(H=XW-F_3(X,Y,Z)\). Equations (1) and (3) give
\[
\begin{gathered}
EX\,q=2F_3(EX,EY,EZ),\qquad
\gcd(X,F_3)=1,\\
\rho=0,\qquad G_2=-P_2(X,Y),\qquad
G_1=Z-P_1(X,Y),\qquad G_0=-P_0,\\
E^2H=-2P_2(1,a),\qquad
E(H+P_2)=r-P_1(1,a),\\
H+\rho W-G_2-G_1-G_0=-a.
\end{gathered}
\tag{8}
\]
Primitivity follows from (5): the coefficient of \(a^3\) in
\(Q(a)\) is twice the coefficient of \(Y^3\) in \(F_3\),
so \(X\) does not divide \(F_3\).
The two derivative identities are precisely the two correction
gates130.[^3] The corrected invariant \(-a\) is an actual
coordinate by the original adapted presentation, independently of
any recognition theorem.

## 7. Scope of the restriction

The conclusion excludes genuinely coupled \(b\)-dependence in the
first of these two middle shears when the endpoint has the stated
primitive profile. It allows non-equivariant terms in
\(P(u,Y)\), including quadratic and cubic terms; their effect is
accounted for by the explicit correction.

No conclusion is asserted for an endpoint with \(q\in W_2\),
for a path with further intervening elementary moves, or for a family
that changes the held coordinate \(Y\).
In particular this does not contradict the seven-shear control131:
its middle invariant shear holds \(v\), not the old
\(Y=v+au\), fixed while changing \(a\).
Nor does this establish that arbitrary sliced derivations possess
any selected profile or primitive mixed relation.

The proof uses exact polynomial inverses and independence of specified
initials. It makes no inference from polynomial coordinate generation
to generation of the full associated graded ring.

## Sources

1. [Cubic acceleration outside the fixed-good quadratic span](three-good-cubic-acceleration-span-obstruction-pass129.md).
   Private research note `three-good-cubic-acceleration-span-obstruction-pass129.md`,
   Sections 1 and 5. The polynomial inverse is re-established here;
   the distinction between the coordinate initial subalgebra and
   the full associated graded ring is retained.
2. [A first-commutator obstruction in an actual unit rank-two frame](three-good-rank-two-commutator-instability-pass128.md).
   Private research note `three-good-rank-two-commutator-instability-pass128.md`,
   Section 7, the dense-cone degree and fixed-good-shear criteria.
   The weighted independence arguments needed for this family
   are proved directly above.
3. [Correcting a mixed cubic relation to an invariant coordinate](three-good-mixed-cubic-correction-criterion-pass130.md).
   Private research note `three-good-mixed-cubic-correction-criterion-pass130.md`,
   Sections 1--3. Only the definitions of the two correction gates
   and their primitive-profile scope are used, not the topological
   recognition theorem.

[^1]: [Actual divided-difference frame129](three-good-cubic-acceleration-span-obstruction-pass129.md), Sections 1 and 5.
[^2]: [Dense-cone and fixed-good degree restriction128](three-good-rank-two-commutator-instability-pass128.md), Section 7.
[^3]: [Mixed-cubic correction criterion130](three-good-mixed-cubic-correction-criterion-pass130.md), Sections 1--3.
