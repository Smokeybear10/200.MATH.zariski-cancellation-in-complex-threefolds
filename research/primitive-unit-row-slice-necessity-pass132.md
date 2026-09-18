# A unit speed row forces a constant-speed primitive lift

In the unit-speed-row branch, a successful primitive cubic
correction forces its affine leading good coordinate to be
a coordinate slice. Thus this correction method cannot newly
recognize an action in that branch that has no constant-speed
affine good direction. This is a necessary condition for
success, not an assertion that every primitive relation succeeds.

The proof first treats an invariant in normalized cubic form.
That argument requires only local nilpotence and the unit row,
not a pre-existing global slice. Applying it to a general
successful primitive correction uses the retained
invariant-suspension recognition theorem to obtain the
normal form.[^1]

The separate [normalized classification](normalized-cubic-action-classification-pass132.md)
now removes the unit-row hypothesis from the sliced primitive application
by using Wang's generic classification. The elementary proof here is
retained as an independent argument with a smaller external dependency.

## 1. An invariant cannot become constant on a moving coordinate hyperplane

Let \(B=\mathbb C[X,Y,Z,W]\), let
\(E\in\operatorname{LND}_{\mathbb C}(B)\), and suppose \(EX\ne0\).
For every nonconstant \(f\in\ker E\),
\[
f\bmod XB\notin\mathbb C,\qquad (f,X)B\ne B.
\tag{1}
\]
The first assertion includes the possibility of zero as a constant.

Indeed, if \(f-\lambda=Xh\) for \(\lambda\in\mathbb C\),
then \(h\ne0\). For any nonzero polynomials \(g,h\), local
nilpotence in a characteristic-zero domain gives
\(\deg_E(gh)=\deg_E g+\deg_E h\). This follows from the
Leibniz formula: at the sum of the two degrees, precisely
one nonzero product of top derivatives survives.
Consequently every nonzero factor of an invariant product
is invariant. Applied to \(f-\lambda=Xh\), this contradicts
\(EX\ne0\).
The product-degree identity is also recorded in
Dasgupta--Lahiri, Lemma 2.8.[^3]

For the second assertion, the fact that \(X\) is an actual
polynomial coordinate is essential:
\(B/XB\simeq\mathbb C^{[3]}\) has only constant units.
If \((f,X)B=B\), the image of \(f\) would be a nonzero
constant unit, contradicting the first assertion.
This is not a general claim about the units on an arbitrary
prime hypersurface.

## 2. The normalized cubic lemma

Assume that the following are actual polynomial coordinates
and that all derivatives are taken with respect to the same
locally nilpotent derivation:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad
E^2X=E^2Y=E^2Z=0,\qquad E^3W=0,\\
I=XW-F(Y)-\delta Z\in\ker E,\qquad
F(T)=\gamma T^3+f_2T^2+f_1T+f_0,\qquad \gamma\delta\ne0,\\
s=EX\ne0,\quad t=EY,\quad r=EZ,\quad q=E^2W,\qquad
(s,t,r)B=B.
\end{gathered}
\tag{2}
\]
Then \(s\in\mathbb C^*\).
No pre-existing slice, rank-two hypothesis, or cone-density
hypothesis is needed for this normalized statement.

The first and third derivatives of \(I\) give
\[
\delta r=sW+XEW-F'(Y)t,\qquad sq=2\gamma t^3.
\tag{3}
\]
Here the second identity follows from
\(0=E^3I=3sq-6\gamma t^3\).
Suppose \(s\) has an irreducible factor \(p\) in the UFD \(B\).
Since \(s\in\ker E\), factorial closure makes \(p\) invariant.
The second identity in (3) gives \(p\mid t\).
The first identity now gives
\[
s,t,r\in(p,X)B.
\tag{4}
\]
But (1) says that \((p,X)B\) is proper. This contradicts
the unit-row assumption in (2).
Thus \(s\) has no irreducible factor and is a nonzero
constant.

In particular \(X/s\) is an actual coordinate slice.
Writing \(A=\ker E\), the slice theorem gives
\[
B=A[X/s],\qquad
A\simeq B/XB\simeq\mathbb C^{[3]}.
\tag{5}
\]
This last recognition is direct. It does not require
a further theorem about kernels fixing an invariant
coordinate.
One may see the slice equality explicitly by putting
\(T=X/s\): the finite Taylor map
\(\pi(f)=\sum_{j\ge0}(-T)^jE^j(f)/j!\) takes values
in \(A\), and
\(f=\sum_{j\ge0}\pi(E^j f)T^j/j!\).
Uniqueness follows by applying the highest nonzero
derivative to a polynomial relation over \(A\).

## 3. Consequence for a successful primitive mixed relation

Return to the actual sliced frame of the mixed-cubic
criterion:[^2]
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad E=\partial_u,\quad
E^2x_i=0,\quad a_i=Ex_i,\quad E^3z=0,\quad q=E^2z\ne0,\\
P(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }P,\qquad
(a_1,a_2,a_3)B=B,\\
L(a)q=2F_3(a),\qquad
L\ne0\text{ homogeneous linear},\quad
F_3\text{ homogeneous cubic},\quad \gcd(L,F_3)=1.
\end{gathered}
\tag{6}
\]
One may also retain the rank-two speed hypothesis from
that criterion; it is not used in the argument below.
Assume both corrections succeed, so that
\[
I=(L(x)+\rho)z-F_3(x)-G_2(x)-G_1(x)-G_0\in A,
\tag{7}
\]
with the stated constant, quadratic and linear corrections.
Then
\[
\boxed{L(a)\in\mathbb C^*.}
\tag{8}
\]

For completeness, the normalization is as follows.
Set \(X=L(x)+\rho\), and choose two affine-linear
complementary good coordinates \(Y_0,Z_0\).
Write \(I=Xz-g(X,Y_0,Z_0)\), with ordinary degree
\(\deg g\le3\), and divide
\(g=XJ+g_0(Y_0,Z_0)\).
The actual triangular shear \(W=z-J\) has
\(\deg J\le2\), hence \(E^3W=0\).
The retained invariant-suspension theorem makes \(g_0\)
a plane coordinate.[^1]

Primitivity implies \(F_3|_{\ker L}\ne0\), so \(g_0\)
has exact degree three. The elementary cubic
plane-coordinate criterion makes it
\(F(Y)+\delta Z\), with \(\gamma\delta\ne0\),
after an affine-linear change in the two plane
coordinates.[^2] This leaves all three goods
\(E\)-affine. Their speed row is an invertible constant
linear transform of the original row, so it remains
a unit row. Cone density ensures \(EX=L(a)\ne0\).
All hypotheses of (2) are now satisfied, proving (8).

The shift by \(\rho\) does not affect this derivative.
Thus \(L(x)/L(a)\), as well as
\((L(x)+\rho)/L(a)\), is an actual coordinate slice
already affine-linear in the original good coordinates.

The contrapositive is useful but must be stated exactly:
an **actual** frame satisfying (6) with nonconstant
\(L(a)\) cannot pass both derivative corrections.
At least one of the two tests must fail. This does not
identify which test fails, prove that such a frame
exists, or turn an arbitrary choice of speed polynomials
into an actual polynomial coordinate system.

In particular, in the unit-row branch the primitive
correction route cannot recognize a previously
unrecognized action that lacks any constant-speed
affine good direction. This elementary argument itself makes no such
assertion outside the unit-row branch; the separate normalized
classification supplies that stronger conclusion.

## 4. Primitivity cannot be omitted

There is an actual successful nonprimitive example
with a unit row, dense speed cone, rank two, a global
slice, and nonconstant \(L(a)\).
In \(\mathbb C[a,b,v,u]\), with \(E=\partial_u\), take
\[
\begin{gathered}
X=u,\qquad Y=v+au,\qquad
Z=a+bY,\qquad W=b+u^2/2,\\
u=X,\qquad b=W-X^2/2,\qquad
a=Z-bY,\qquad v=Y-aX.
\end{gathered}
\tag{9}
\]
The displayed inverse is polynomial in both orders.
The good speeds are \((1,a,ab)\), and \(q=1\).
They generate the unit ideal and a field of
transcendence degree two. Their cone is dense:
the ratios \(a,ab\) are algebraically independent,
as follows by substituting in a polynomial relation
and comparing powers of \(b\).

For the nonprimitive pair \(L=Y\),
\(F_3=YX^2/2\), one has
\[
\begin{gathered}
L(a)=a,\qquad
H=YW-YX^2/2=bY,\qquad E^2H=0,\qquad EH=ab=EZ,\\
H-Z=-a\in\ker E,\qquad \gcd(L,F_3)=Y.
\end{gathered}
\tag{10}
\]
Thus both corrections pass with \(\rho=0,G_2=0,G_1=Z\),
even though \(L(a)\) is nonconstant.
The invariant \(-a\) is an actual coordinate.
This refutes the statement obtained by deleting
primitivity, while leaving the other stated
frame hypotheses intact. It is not a counterexample
to cancellation.

## 5. Remaining construction problem

The necessary condition (8) changes the target for
counterexample construction. In the unit-row branch,
an actual primitive relation with nonconstant leading
speed would already force a failure of the correction
method. An explicit polynomial inverse remains part
of what must be proved; a Jacobian test alone is not
an inverse.

The separate
[two-shear return calculation](two-shear-primitive-return-rigidity-pass132.md)
excludes a natural compensated construction while
holding two specified coordinates fixed.
Neither that bounded family nor (8) proves universal
gate passage, the existence of a primitive mixed
relation in every frame, unrestricted coordinate
entry, or full cancellation.

## Sources

1. [An invariant linear suspension in a sliced polynomial fourfold](invariant-linear-suspension-recognition-pass130.md).
   Sections 1--6 prove the conditional plane-coordinate
   recognition used in Section 3, with its classical
   topological and plane-line inputs.
2. [Correcting a mixed cubic relation to an invariant coordinate](three-good-mixed-cubic-correction-criterion-pass130.md).
   Sections 1--3 define the two correction tests and
   primitivity; Section 5 gives the elementary cubic
   plane-coordinate normalization.
3. Nikhilesh Dasgupta and Animesh Lahiri.
   *On image ideals of nice and quasi-nice derivations on
   R[X1, X2]*. arXiv:2302.13787v6, July 24, 2026,
   Lemma 2.8, printed p. 5.
   [Primary source](https://arxiv.org/pdf/2302.13787v6).
   Only the elementary product-degree identity is invoked;
   the specialized image-ideal theorems are not used.

[^1]: [Invariant linear-suspension recognition](invariant-linear-suspension-recognition-pass130.md),
    especially Section 6.
[^2]: [Mixed-cubic correction criterion](three-good-mixed-cubic-correction-criterion-pass130.md),
    Sections 1--3 and 5.
[^3]: Dasgupta--Lahiri, Lemma 2.8, printed p. 5.
    [Source](https://arxiv.org/pdf/2302.13787v6).
