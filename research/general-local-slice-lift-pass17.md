# Finite-jet coordinates for the full rank-three local-slice family

The finite correction extends to the entire Dasgupta--Gaifullin
Theorem 5.7 family, including its nonhomogeneous members. The result
below is a coordinate construction with a polynomial inverse. It is
not a classification of arbitrary rank-three derivations or a proof
of threefold cancellation.

## 1. Statement and source boundary

Work over \(\mathbb C\). Fix integers \(m\ge2\), \(n\ge1\),
and a polynomial \(P\in\mathbb C[x,f]\) with
\(P(x,0)\notin\mathbb C\). Put

\[
\begin{gathered}
R=\mathbb C[x,y,z],\qquad f=xz-y^m,\qquad L=mn+1,\\
r=xP(x,f)+yf^n,\qquad
h=\frac{r^m+f^L}{x},\qquad g=f^nh,\\
\delta=-\operatorname{Jac}(f,h,\cdot).
\end{gathered}
\tag{1}
\]

The quotient defining \(h\) is polynomial, by the binomial
expansion and \(y^m+f=xz\). The cited family theorem and its proof
give that \(\delta\) is a primitive rank-three LND, its kernel is
\(C=\mathbb C[f,h]\), \(\delta r=g\), and its plinth ideal is
\(gC\). Our sign convention reverses that source's derivation.[^1]

**Coordinate theorem.** Suppose \(A,B\in C\) satisfy

\[
(A,B)C=C,\qquad B=1+fhQ(f,h),\quad Q\in C.
\tag{2}
\]

Then \(E=A\delta+B\partial_t\) on \(R[t]\) has a polynomial
coordinate system \((X,Y,Z,s)\) such that

\[
EX=EY=EZ=0,\qquad Es=1,
\qquad f=XZ-Y^m.
\tag{3}
\]

In particular \(\ker E=\mathbb C[X,Y,Z]\). A nonzero constant
residue \(B\equiv c\pmod{fh}\) is handled by applying the theorem
to \(E/c\), with both \(A\) and \(B\) divided by \(c\).
This gives a coordinate translation of speed \(c\) for \(E\),
which is normalized to speed one by replacing \(s\) with \(s/c\).

The proof of sufficiency below uses no general cancellation theorem,
no principality assertion for higher image ideals, and no pointwise
plinth theorem. Necessity for arbitrary slices, if invoked, is a
separate consequence of the general affine-replacement result and
must cite that result with its full hypotheses.

## 2. An affine slice and its invariant companion

Since \(fhQ\) is nilpotent modulo \(g=f^nh\), \(B\) is a unit
modulo \(g\). Combining this with \((A,B)=C\) gives
\((Ag,B)=C\). Choose \(U,V\in C\) with

\[
AgU+BV=1.
\tag{4}
\]

Define

\[
\rho=Br-Agt,\qquad s=Ur+Vt.
\tag{5}
\]

Then \(E\rho=0\), \(Es=1\), and the inverse matrix is

\[
r=V\rho+Ags,\qquad t=-U\rho+Bs.
\tag{6}
\]

In the fraction field define

\[
X=\frac{\rho^m+f^L}{h}.
\tag{7}
\]

This lies in \(R[t]\): the term \((Br)^m\) contributes
\(B^m x+(1-B^m)f^L/h\), and every other term in the expansion
of \((Br-Af^nht)^m\) contains \(h\). The displayed quotient
is polynomial because \(B\equiv1\pmod h\). Moreover

\[
X\equiv B^mx\pmod{f^n},\qquad X\equiv x\pmod f.
\tag{8}
\]

## 3. The finite polynomial correction

For this section only, regard \(X,f\) as independent variables.
There is a unique \(H\in\mathbb C[X,f]/(f^n)\) satisfying

\[
\begin{gathered}
b_H=B(f,X^{m-1}H^m),\\
H=b_H^{1-m}P(b_H^{-m}X,f),
\qquad H\equiv P(X,0)\pmod f.
\end{gathered}
\tag{9}
\]

All inverse powers mean finite binomial expansions modulo \(f^n\),
since \(b_H\equiv1\pmod f\). Starting with
\(H_0=P(X,f)\bmod f^n\), apply the right side of (9) exactly
\(n-1\) times. Reduce modulo \(f^n\) after each iteration and
choose the final representative of degree less than \(n\) in \(f\).

To justify the construction, if two inputs differ by an element of
\((f^k)\), the corresponding \(b_H\)'s differ by an element of
\((f^{k+1})\). The extra factor comes from
\(B(f,h)-1=fhQ(f,h)\). Taking inverse powers of units and
substituting into \(P\) preserves this improved divisibility.
Thus each iteration improves agreement by one order. The zeroth
approximation is correct modulo \(f\), so \(n-1\) iterations
give a fixed point modulo \(f^n\). The same argument proves
uniqueness in every algebra with \(f^n=0\), after specialization
of \(X\).

## 4. Forward polynomial divisibility

In \(R[t]/(f^n)\), the old relations and (8) give

\[
r=xP(x,f),\quad
h=x^{m-1}P(x,f)^m,\quad
\rho=BxP(x,f),\quad X=B^mx.
\tag{10}
\]

Here \(B\) is a unit. Set
\(H_*=B^{1-m}P(B^{-m}X,f)\) in this quotient. Then
\(X^{m-1}H_*^m=h\), so \(H_*\) is a fixed point of (9).
Its reduction modulo \(f\) is \(P(X,0)\); uniqueness makes it
equal to the specialized polynomial \(H(X,f)\). Hence

\[
Y=\frac{\rho-XH(X,f)}{f^n}
\tag{11}
\]

is polynomial. Define the binomial expression

\[
S_m(X,H,Y,f)
=\sum_{k=0}^{m-1}\binom{m}{k}
X^{m-k-1}H^{m-k}Y^k f^{nk}.
\tag{12}
\]

The identity \(Xh=\rho^m+f^L\), together with
\(\rho=XH+Yf^n\), gives

\[
X\bigl(h-S_m(X,H,Y,f)\bigr)
=f^{mn}(Y^m+f).
\tag{13}
\]

The polynomial \(f=xz-y^m\) is irreducible, and (8) implies
\(f\nmid X\). Since \(R[t]\) is a UFD, (13) proves that

\[
Z=\frac{h-S_m(X,H,Y,f)}{f^{mn}}
\tag{14}
\]

is polynomial. It gives \(f=XZ-Y^m\). Since \(E\) kills
\(f,h,\rho\), equations (7), (11), and (14) also show that
it kills \(X,Y,Z\).

## 5. Polynomial inverse in independent variables

Now let \(T=\mathbb C[X,Y,Z,s]\) be an independent polynomial
ring. In \(T\), define

\[
f=XZ-Y^m,\quad
\rho=XH(X,f)+Yf^n,\quad
h=S_m(X,H(X,f),Y,f)+Zf^{mn}.
\tag{15}
\]

These satisfy \(Xh=\rho^m+f^L\). Evaluate
\(A,B,U,V\) at these \(f,h\), set \(g=f^nh\), and use
(6) to define polynomial \(r,t\).
The polynomial \(h\) is nonzero in this independent ring:
setting \(Y=Z=0\) gives
\(h=X^{m-1}P(X,0)^m\ne0\). Thus subsequent cancellation in
the domain is legitimate when checking inverse compositions.

Equation (4) and \(B\equiv1\pmod h\) imply
\(V\equiv1\pmod h\). Thus

\[
\begin{gathered}
W=\frac{V-1}{h}\rho+Af^ns,\\
x=X+W\sum_{i=0}^{m-1}r^{m-1-i}\rho^i
\end{gathered}
\tag{16}
\]

are polynomials. Here \(r-\rho=hW\), so
\(xh=r^m+f^L\). Modulo \(f^n\), we have

\[
V=B^{-1},\qquad h=X^{m-1}H^m,
\qquad r=VXH,\qquad x=V^mX.
\tag{17}
\]

The last congruence does not require canceling \(h\) in a
nonreduced ring. Namely, reduce (16), use
\((V^m-1)/h\in T\), and obtain

\[
x\equiv X+\frac{V^m-1}{h}\rho^m
=V^mX-\frac{V^m-1}{h}f^L
\equiv V^mX\pmod{f^n}.
\tag{18}
\]

The fixed-point equation (9), together with (17), says
\(H\equiv V^{m-1}P(V^mX,f)\pmod{f^n}\). Therefore
\(r\equiv xP(x,f)\pmod{f^n}\), and

\[
y=\frac{r-xP(x,f)}{f^n}
\tag{19}
\]

is polynomial in \(T\). The same binomial identity gives

\[
x\bigl(h-S_m(x,P(x,f),y,f)\bigr)
=f^{mn}(y^m+f).
\tag{20}
\]

In \(T\), \(f=XZ-Y^m\) is irreducible, and (17) modulo
\(f\) gives \(x\equiv X\pmod f\). Consequently
\(\gcd(f,x)=1\), and

\[
z=\frac{h-S_m(x,P(x,f),y,f)}{f^{mn}}
\tag{21}
\]

is polynomial. This constructs \(x,y,z,t\) in \(T\).

Substitution into the forward map recovers \(r,t\) by the inverse
matrix, then \(x\) from \(xh=r^m+f^L\), then \(y\) from
(19), and \(z\) from (21). Thus the homomorphism
\(T\to R[t]\) defined by the forward coordinates is surjective.
Its kernel is zero, since both are polynomial domains of dimension
four. Equations (3) follow, completing the coordinate theorem.

## 6. What changes in the invariant presentation

The construction keeps the form \(f=XZ-Y^m\), but replaces the
polynomial \(P(x,f)\) in the presentation of \(h\) by the
finite correction \(H(X,f)\). It need not fix the original
embedding of \(\mathbb C[f,h]\) into a polynomial three-ring.
This distinction is necessary: relative isomorphism obstructions
in the quadratic subfamily can coexist with this abstract polynomial
coordinate system.

The construction uses the specific identities of (1), especially
the binomial exponent \(m\), the denominator \(f^n\), and
\(f=xz-y^m\). It has not been extended here to arbitrary
local-slice constructions, arbitrary rank-three derivations, or
arbitrary slice derivations on polynomial four-space.

## Sources and verification status

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Theorem 5.7 and its proof. The published full HTML was read directly. The condition \(n\ge1\), not printed explicitly in that HTML display, is explicit in the [arXiv v2 family definition](https://arxiv.org/html/2306.00510v2).

The finite-jet lift and its polynomial inverse are the deduction
proved in this note. The known rank-three family is credited to the
source; no priority, human-review, or formal proof-assistant claim is
made for the lift. The independent finite checks in
[general_jet_lift_checks.py](general_jet_lift_checks.py)
are regression controls, not the proof for arbitrary parameters.
