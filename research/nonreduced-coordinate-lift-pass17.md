# Polynomial coordinates across a nonreduced plinth divisor

## Statement

Work over \(\mathbb C\). For every integer \(n\ge1\), put
\[
f=xz-y^2,\quad r=-x^3-yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,\quad g=f^nh,
\]
and let \(D_n=\operatorname{Jac}(f,h,\cdot)\). Then
\(D_nr=g\), \(D_nx=2f^nr\), and \(\ker D_n=C=\mathbb C[f,h]\).
This is the \(m=2,F(t_1,t_2)=t_1^2\) subfamily of the known
rank-three family in Dasgupta--Gaifullin, Theorem 5.7.

For \(A,B\in C\), suppose
\[
(A,B)C=C,\qquad B=1+fhQ(f,h),\quad Q\in C.
\tag{1}
\]
Then \(E=AD_n+B\partial_t\) is polynomially conjugate to a
coordinate translation. The proof constructs four polynomial
coordinates and a polynomial inverse. It does not require
\(B\equiv1\pmod{f^nh}\). A nonzero constant residue other than
one is treated by dividing \(E\) and its coefficients by that constant.

The separate all-degree image-ideal argument gives necessity of (1),
with a nonzero constant residue, for the existence of a slice. Thus,
subject to those explicitly stated inputs, this is a full invariant-pair
classification for this family. It is not a reduction of an arbitrary
rank-three derivation to the family, or a proof of general cancellation.
Novelty has not been established.

## 1. The affine slice and invariant numerator

Condition (1) makes \(B\) a unit modulo \(g=f^nh\). Indeed
\(fhQ\) is nilpotent modulo \(g\). Together with \((A,B)=C\),
this gives polynomials \(U,V\in C\) such that
\[
AgU+BV=1.
\tag{2}
\]
Define
\[
\rho=Br-Ag t,\qquad s=Ur+Vt.
\tag{3}
\]
Then \(E\rho=0\), \(Es=1\), and the inverse matrix identity is
\[
r=V\rho+Ags,\qquad t=-U\rho+Bs.
\tag{4}
\]
We will replace \(x,y,z\) by invariant coordinates \(X,Y,Z\).
The identity \(xh=r^2+f^{2n+1}\) suggests
\[
X=\frac{\rho^2+f^{2n+1}}{h}.
\tag{5}
\]
This is a polynomial in the original ring \(R[t]\). In fact
\[
X=B^2x+\frac{1-B^2}{h}f^{2n+1}
 -2BAf^nrt+A^2f^{2n}h t^2.
\tag{6}
\]
The only displayed quotient is polynomial because \(B\equiv1\pmod h\).
Moreover \(X\equiv x\pmod f\), so the irreducible polynomial
\(f=xz-y^2\) does not divide \(X\).

The naive next formula \(-(\rho+X^3)/f^n\) need not be polynomial
when \(n>1\). A finite correction of \(X^2\) repairs precisely
that divisibility failure.

## 2. The finite correction

Temporarily regard \(X,f\) as independent indeterminates. In
\(\mathbb C[X,f]/(f^n)\), there is a unique \(J\equiv1\pmod f\)
satisfying
\[
J=B(f,X^5J^2)^{-5}.
\tag{7}
\]
The inverse power means a finite polynomial expression in this quotient:
if \(B=1+N\), use
\(\sum_{j=0}^{n-1}\binom{-5}{j}N^j\).
To construct \(J\), start with \(J_0=1\), apply the right side
of (7) exactly \(n-1\) times, and reduce modulo \(f^n\) after each
update. Choose the resulting representative of degree less than \(n\)
in \(f\).

This iteration is finite and exact. The difference between its values
at two inputs congruent modulo \(f^k\) is divisible by \(f^{k+1}\),
because \(B(f,H)-1\) is divisible by \(f\). This contraction
proves both the error improvement and uniqueness. The same uniqueness
argument holds after any specialization to an algebra in which \(f^n=0\).

Put
\[
F(X,f)=X^2J(X,f).
\tag{8}
\]
For the example \(B=1+fh\) and \(n=2\), this is
\(F=X^2(1-5fX^5)\). For \(n=1\), it is simply \(F=X^2\).

## 3. The other invariant coordinates are polynomials

Define in the fraction field
\[
Y=-\frac{\rho+XF(X,f)}{f^n},\qquad
Z=\frac{h+2\rho F(X,f)+XF(X,f)^2}{f^{2n}}.
\tag{9}
\]
Both expressions belong to \(R[t]\).

First work modulo \(f^n\). The original relations and (6) give
\[
r\equiv-x^3,\quad h\equiv x^5,\quad
\rho\equiv Br,\quad X\equiv B^2x.
\]
Since \(B\equiv1\pmod f\), it is invertible in this quotient.
Consequently
\[
\rho\equiv-B^{-5}X^3,\qquad h\equiv B^{-10}X^5.
\tag{10}
\]
The element \(B(f,h)^{-5}\) satisfies (7), after substituting the
actual \(X,f\). Uniqueness of the finite correction makes it
equal to \(J(X,f)\) modulo \(f^n\). Thus the numerator of \(Y\)
is divisible by \(f^n\), proving that \(Y\) is polynomial.

Let \(N=h+2\rho F+XF^2\), the numerator defining \(Z\). Then
\[
XN=(\rho+XF)^2+f^{2n+1}=f^{2n}(Y^2+f).
\tag{11}
\]
The ring \(R[t]\) is a UFD, and \(f\) is coprime to \(X\)
by (6). Hence \(f^{2n}\mid N\), proving that \(Z\) is polynomial.
In particular
\[
f=XZ-Y^2,\quad
\rho=-XF-Yf^n,\quad
h=XF^2+2YFf^n+Zf^{2n}.
\tag{12}
\]
The derivation kills \(f,h,\rho\). Cancellation of the nonzero
denominators in (5) and (9) shows that it kills \(X,Y,Z\).

## 4. Polynomial inverse

To prove coordinate generation without assuming cancellation, regard
\(X,Y,Z,s\) now as independent polynomial variables. Define
\(f,\rho,h\) by (12), using the same polynomial \(F(X,f)\).
Evaluate \(A,B,U,V\) at these \(f,h\), set \(g=f^nh\), and
define \(r,t\) by (4).

Since \(B\equiv1\pmod h\), (2) implies
\(V\equiv1\pmod h\). Therefore
\[
W=\frac{V-1}{h}\rho+Af^ns,
\qquad x=X+W(r+\rho)
\tag{13}
\]
are polynomials. They satisfy \(xh=r^2+f^{2n+1}\).
We claim that
\[
y=-\frac{r+x^3}{f^n},\qquad
z=\frac{h+2x^2r+x^5}{f^{2n}}
\tag{14}
\]
are polynomials in these independent variables as well.

Modulo \(f^n\), identity (2) gives \(V=B^{-1}\), while
(12)-(13) give
\[
h\equiv XF^2,\qquad r\equiv-VXF,\qquad x\equiv V^2X.
\]
For the last congruence, (13) gives
\(x\equiv X+((V^2-1)/h)\rho^2\pmod{f^n}\).
The quotient is polynomial and \(\rho^2=Xh-f^{2n+1}\), so
the claimed congruence follows without canceling \(h\) in a
nonreduced quotient ring.
The defining finite correction satisfies
\[
F\equiv X^2 B(f,XF^2)^{-5}\equiv V^5X^2\pmod{f^n}.
\]
It follows that \(r+x^3\equiv0\pmod{f^n}\), proving that
\(y\) is polynomial. All these congruences are polynomial identities
after substituting \(f=XZ-Y^2\), not an assumption that this
polynomial is a coordinate.

The numerator \(N_0=h+2x^2r+x^5\) for \(z\) satisfies
\[
xN_0=(r+x^3)^2+f^{2n+1}=f^{2n}(y^2+f).
\tag{15}
\]
Here \(f=XZ-Y^2\) is irreducible and \(x\equiv X\pmod f\).
Thus \(\gcd(f,x)=1\), and (15) proves that \(z\) is polynomial.
This constructs a polynomial expression for every original coordinate
\(x,y,z,t\) in terms of \(X,Y,Z,s\).

Substitution back into the original ring returns \(r,t\) by the
inverse matrix identity, then \(x\) by \(xh=r^2+f^{2n+1}\),
then \(y,z\) by their defining relations. Therefore
\(\mathbb C[X,Y,Z,s]\to R[t]\) is surjective. Both rings are
polynomial domains of dimension four, so its kernel is zero.
This gives the required coordinate system, with \(EX=EY=EZ=0\)
and \(Es=1\).

## 5. Why this does not assert a relative lift

The new expression for \(f\) has the original quadratic form, but
the new expression for \(h\) uses \(F(X,f)\), not necessarily
\(X^2\). Hence the isomorphism of the two polynomial three-rings
does not in general preserve the original embedding of
\(\mathbb C[f,h]\). This is substantive, not just a change of
notation. The separate Danielewski comparison tests and can obstruct
a lift required to fix this entire common invariant ring.

For this reason a failure of the older common-invariant-ring matrix
formula is compatible with the coordinates constructed here. The
result handles these nonreduced plinth thickenings by changing the
polynomial presentation of the quotient, not by asserting a missing
scalar congruence modulo \(f^nh\).

## A closed coefficient control for the basic jet

When \(B=1+fh\), put \(w=fX^5\). Equation (7) becomes
\(J=(1+wJ^2)^{-5}\). Its formal solution has coefficients
\[
[w^k]J=\frac{(-1)^k}{2k+1}\binom{11k+4}{k},\qquad k\ge0.
\]
For a derivation, set \(z=wJ^2\). Then
\(z=w(1+z)^{-10}\) and \(J=(1+z)^{-5}\).
For \(k\ge1\), formal Lagrange inversion gives
\[
[w^k]J=-\frac5k[u^{k-1}](1+u)^{-10k-6}
=\frac{(-1)^k5}{k}\binom{11k+4}{k-1}.
\]
The last binomial expression equals the displayed coefficient.
Truncating at \(k<n\) gives the finite jet in the theorem.
This is an independent coefficient control, not an additional
hypothesis or an analytic convergence assertion.

## Sources and verification status

The base family and its rank and ordinary plinth are from
[Dasgupta--Gaifullin, Theorem 5.7](https://www.mathnet.ru/eng/sm10094).
The complete higher-image reconstruction is in
[nonreduced-rank-three-images-pass17.md](nonreduced-rank-three-images-pass17.md).
The abstract affine-replacement implication uses the preceding
[whole-component and torsion result](whole-plinth-component-pass16.md).
The finite correction, polynomial divisibility argument, and inverse
have a completed separate algebraic reconstruction and finite checks.
The [full-family proof](general-local-slice-lift-pass17.md) gives a broader
version with arbitrary exponents and polynomial parameters. No assertion of
human expert review, formal proof-assistant verification, or novelty
is made.
