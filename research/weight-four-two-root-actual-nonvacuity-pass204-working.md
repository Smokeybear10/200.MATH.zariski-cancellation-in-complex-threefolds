# An actual nonvacuity witness for the two-root full initial kernel

Status: explicit construction, pending independent saved-source review.
This example verifies that the restricted hypotheses of synthesis203
can occur in an actual polynomial ring with a global slice.
It is not a counterexample to cancellation, a new general theorem,
or a substitute for the recognition proof.

## 1. Independent coordinates and a globally sliced derivation

Start with the independent polynomial ring
\(B=\mathbb C[x,y,z,g]\), and write \(i^2=-1\). Set
\[
a=1+2ig,\qquad b=g^2,\qquad c=g(1+ig),\qquad
E=a\partial_x+b\partial_y .
\tag{1}
\]
Since \(E\) fixes \(z,g,a,b\), it is locally nilpotent.
The two polynomials
\[
u=(1-2ig)x-4y,\qquad v=ay-bx
\tag{2}
\]
satisfy \(Eu=1,\ Ev=0\). Indeed
\((1-2ig)a-4b=1\). The inverse is
\(x=au+4v,\ y=bu+(1-2ig)v\).
Consequently \(B=\mathbb C[z,g,v,u]\) and
\(A:=\ker E=\mathbb C[z,g,v]\), with no localization.

## 2. An actual four-coordinate frame

Put
\[
j=-z^2/2+xg-iy,\qquad
X=x,\quad Y=y,\quad
Z=z+xj,\quad
W=g+\frac{xy(y-x)}2+zj+\frac{xj^2}2 .
\tag{3}
\]
These are actual polynomial coordinates. Their inverse is the
specialization \(\alpha=i,\beta=1,\gamma=\delta=0\) of the
[explicit inverse pair203](weight-four-two-root-monomial-coordinate-recognition-pass203-working.md),
but it can also be checked directly. Given independent \(X,Y,Z,W\), set
\[
\begin{gathered}
I=Z^2-X^2Y(X-Y)-2XW,\qquad J=(-I-2iY)/2,\\
x=X,\quad y=Y,\quad z=Z-XJ,\quad
g=W-ZJ+XJ^2/2-XY(Y-X)/2 .
\end{gathered}
\tag{4}
\]
Substituting (3) in (4) gives \(J=j\) and all four original entries;
substituting (4) in (3) returns the four independent supplied entries.
The equality \(J=j\) is the same polynomial cancellation in both orders.
No denominator other than a nonzero complex constant occurs.

## 3. Exact time degrees and the entire leading kernel

The identities \(Ej=c\) and \(c^2=b(a-b)\) give
\[
EX=a,\quad EY=b,\quad
e:=E^2Z/2=ac,\quad
h:=E^2W/2=-\frac a2(cz^2+av),\qquad
E^3Z=E^3W=0 .
\tag{5}
\]
For example the possible cubic time coefficient of \(W\) is
\(a\{b(b-a)+c^2\}/2=0\); the remaining quadratic coefficient is
the displayed \(h\). Both \(e,h\) are nonzero polynomials, as are
\(a,b\). Thus the supplied profile is exactly \((1,1,2,2)\).

For the weighted initial map of synthesis203,
\[
t=b/a=\frac{g^2}{1+2ig},\qquad
q=e/a^2=c/a,\qquad
\rho=h/a^2=-\frac v2-\frac q2z^2,\qquad q^2=t(1-t).
\tag{6}
\]
The element \(t\) is a nonconstant rational function of \(g\);
\(\rho\) is affine in the independent variable \(v\), with nonzero
coefficient. Hence \(t,\rho\) are algebraically independent over
\(\mathbb C\). The field \(\mathbb C(t,q,\rho)\) has transcendence
degree two since \(q\) is algebraic over \(\mathbb C(t)\).

Adjoin a symbol \(\tau\) independent over \(A\). The fraction field of
the initial image is
\(\mathbb C(a\tau,b\tau,e\tau^2,h\tau^2)
 =\mathbb C(a\tau,t,q,\rho)\).
It has transcendence degree three, since \(a\tau\) is independent
over \(\operatorname{Frac}A\). The source kernel therefore has height
one and contains
\[
F=\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y).
\tag{7}
\]
The polynomial \(F\) is irreducible: its right-hand square candidate
\(\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)\) has odd valuations at
the distinct prime factors \(\mathsf Y\) and \(\mathsf X-\mathsf Y\).
Gauss's lemma applies to the monic quadratic in \(\mathsf Z\).
Thus the height-one prime kernel is exactly \((F)\), also after
adjoining the unused source variable \(\mathsf W\).

This verifies fullness of the initial kernel, not just one leading
relation. It also confirms that the recognized class is not empty.

## 4. Evidence and scope

Fresh inline exact arithmetic3aca84 checked the global slice,
the invariant \(v\), \(Ej=c\), the conic identity, third iterates,
the leading relation and the polynomial \(u,v\) inverse.
The follow-up43d23f expressed \(h\) in \((z,g,v)\); its exploratory
guess omitted the factor \(a^2\) on \(v\), and was rejected by a
nonzero residual. The corrected formula in (5) is the literal
computed coefficient, not that rejected guess.

The independence and height-one argument above is a written proof,
not a conclusion inferred from a finite Jacobian check.
There is no claim that this example is historically new.
It supplies a positive control for the exact hypotheses of203;
general cancellation remains unsolved. No saved checker was run
for204, no frozen source was edited, and no external action occurred.

