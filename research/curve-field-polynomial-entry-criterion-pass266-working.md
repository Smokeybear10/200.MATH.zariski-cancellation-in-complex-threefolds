# A curve-field polynomial-entry criterion, with an actual rational boundary

Let a globally sliced LND on a complex polynomial four-ring be given.
If one actual coordinate is polynomial in the other three over a
one-variable subfield of the invariant fraction field, then the kernel is
a polynomial three-ring. No bound on any coordinate's time degree is needed.

This is a sufficient entry criterion, not a proof that the entry condition
always holds. An explicit sliced, quadratic-time example below shows that
rational rather than polynomial entry cannot justify the same coordinate
construction. The example itself has a polynomial kernel.

## 1. Exact statement

Suppose
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\quad A=\ker E.
\tag{1}
\]
Assume that there is a finitely generated field
\[
\mathbb C\subset F\subset\operatorname{Frac}A,\qquad
\operatorname{trdeg}_{\mathbb C}F=1,\qquad
W\in F[X,Y,Z].
\tag{2}
\]
All four letters in (1) are actual polynomial coordinates.
No coordinate change over \(F\) is presumed to descend to \(\mathbb C\).
The polynomial membership in (2) concerns the fixed actual \(X,Y,Z\);
the weaker membership \(W\in F(X,Y,Z)\) is not the stated hypothesis.

Then there is \(P_0\in\mathbb C[X,Y,Z]\) such that
\[
E(W-P_0)=0,\qquad B=\mathbb C[X,Y,Z,W-P_0],
\qquad A\simeq\mathbb C^{[3]}.
\tag{3}
\]
In particular the coordinate conclusion is an ordinary triangular
polynomial automorphism, not merely a fraction-field parametrization.

## 2. The polynomial coefficient pencil is automatically birational

Since \(F\subset\operatorname{Frac}B\) and \(W\in F[X,Y,Z]\), both
field inclusions give
\[
\operatorname{Frac}B
=F(X,Y,Z)=\mathbb C(X,Y,Z)(W).
\tag{4}
\]
The three elements \(X,Y,Z\) are independent over \(F\), because the
field on the left has transcendence degree four over \(\mathbb C\).
Write \(W\) as a finite polynomial with distinct monomials in them
and coefficients in \(F\).

The curve-pencil argument of
[262, Section 4](two-affine-quadratic-cubic-graph-pencil-pass262-working.md)
works unchanged with three independent monomial variables in place
of two. Here is its full necessary content.
On the nonsingular projective curve with function field \(F\), let
\(D\) be the maximum of the polar divisors of all coefficients.
After extending the constant field to \(\mathbb C(X,Y,Z)\), the
leading polar coefficient at any point of \(D\) is a nonzero complex
linear combination of distinct monomials in \(X,Y,Z\).
It cannot cancel. The pole divisor of \(W\) is therefore exactly the
base extension of \(D\).

Its degree is one by (4) and the equality between the degree of a
nonconstant curve function and the degree of its pole divisor.
The precise projective-model and degree inputs are
[Stacks 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
[0AYZ](https://stacks.math.columbia.edu/tag/0AYZ), and
[02NY](https://stacks.math.columbia.edu/tag/02NY), freshly checked for262.
Thus \(D\) is one simple complex point. A nonconstant coefficient
\(\alpha\) has that single simple pole and generates \(F\).
Every coefficient is affine in \(\alpha\). Consequently
\[
F=\mathbb C(\alpha),\qquad
W=P_0(X,Y,Z)+\alpha P_1(X,Y,Z),
\quad P_0,P_1\in\mathbb C[X,Y,Z],\quad P_1\ne0 .
\tag{5}
\]
The nonzero condition follows from (4), or from algebraic independence
of the original four coordinates. This step has not assumed that
\(\alpha\) itself is an ambient polynomial coordinate.

## 3. The actual LND removes the nonconstant pencil multiplier

Put \(Q=W-P_0\). In the UFD \(B\), the elements \(Q,P_1\) are
coprime: \(Q\) is monic of degree one in \(W\), while \(P_1\) is
independent of \(W\). Differentiating (5), using \(E\alpha=0\),
gives the polynomial identity
\[
P_1E(Q)=Q E(P_1).
\tag{6}
\]
Thus \(P_1\mid E(P_1)\).
For an LND on a characteristic-zero domain, if a nonzero element
divides its derivative, that derivative vanishes.
Indeed a hypothetical \(E(f)=fg\ne0\) would give
\(\deg_E f-1=\deg_E f+\deg_E g\), using additivity of LND degree
on products, a contradiction.
Hence \(E(P_1)=0\), and (6) gives \(E(Q)=0\).

The map fixing \(X,Y,Z\) and replacing \(W\) by \(Q=W-P_0\)
has inverse \(W=Q+P_0\). This proves the coordinate assertion.
The ring \(A\) is regular by descent from \(A[u]=B\), and is finitely
generated since it is isomorphic to \(B/(u)\).
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applied to \(E\) on \(\mathbb C[Q,X,Y,Z]\) now proves (3).
The argument does not require \(P_1\) to be a unit.

## 4. An actual sliced example with only rational entry

Use independent actual variables \(X,Y,Z,W\), and define
\[
I=XW-Y^2,\qquad J=W+2IY+I^2X .
\tag{7}
\]
Define a derivation \(D\), fixing \(Z\), by
\[
DX=2Y+2IX,\qquad DY=W-I^2X,\qquad
DW=-2IW-2I^2Y .
\tag{8}
\]
Direct substitution gives
\[
DI=DJ=0,\qquad
D^2X=2J,\quad D^2Y=-2IJ,\quad D^2W=2I^2J,
\qquad D^3X=D^3Y=D^3W=0 .
\tag{9}
\]
Thus \(D\) is locally nilpotent on the polynomial ring. It commutes
with \(\partial_Z\). The derivation
\[
E=\partial_Z+D
\tag{10}
\]
is locally nilpotent and has the actual slice \(EZ=1\).
Its time degrees in the ordered coordinates \(X,Y,Z,W\) are
\((2,2,1,2)\), since every displayed second derivative is nonzero.
Its kernel is already polynomial: the automorphism
\(\exp(-ZD)\) fixes \(Z\) and transforms \(X,Y,W\) into three
invariants of \(E\). Its inverse is \(\exp(ZD)\); all series are
finite because \(D\) is an LND and fixes \(Z\).

The field \(F=\mathbb C(I)\) lies in \(\operatorname{Frac}\ker E\).
There is exact rational entry
\[
\operatorname{Frac}B=F(X,Y,Z),\qquad
W=\frac{I+Y^2}{X}.
\tag{11}
\]
But \(W\notin F[X,Y,Z]\), because \(I+Y^2\) is not divisible by
\(X\) in that polynomial ring. The equality (11) also proves
that \(X,Y,Z\) are independent over \(F\).

More strongly, there is no \(P\in\mathbb C[X,Y,Z]\) for which
\(W-P\) is invariant under this \(E\).
After substituting \(I=XW-Y^2\), the coefficient of \(W^2\) in
the proposed identity \(E(W-P)=0\) is
\[
X^3P_Y-2X^2Y-2X=0 .
\tag{12}
\]
It would require \(X^2P_Y=2XY+2\), impossible on setting \(X=0\).
The coefficient calculation retains the term \(-P_Z\), which
has no \(W\)-dependence, and \(DX\,P_X\), whose \(W\)-degree is at
most one. There is no suppressed contribution at degree two.

Thus rational entry alone does not give the specific invariant
coordinate \(W-P_0(X,Y,Z)\) promised in (3).
This is not a counterexample to cancellation, nor a disproof that
some different recognition theorem could use rational entry.
Here the invariant coordinates from \(\exp(-ZD)\) explicitly exist.

## 5. Research significance and boundary

The sufficient criterion is independent of all small time profiles
and selected-shift restrictions. It identifies one possible global
entry target: establish polynomial membership over an invariant
curve field in some actual coordinate frame.
Neither the slice nor an equality of rational function fields proves
that target. Section 4 supplies an actual, globally sliced boundary
example, stronger than a formal Jacobian-only example.

The pencil argument and regular-kernel theorem are identified inputs;
the divisibility endpoint and boundary example are explicit.
There is no historical novelty claim, independent human certification,
or unrestricted cancellation solution. Existing proof sources are unchanged.
