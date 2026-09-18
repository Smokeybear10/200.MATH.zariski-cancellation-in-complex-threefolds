# A finite homogeneous invariant-coordinate recognition criterion

## 1. Exact scope and the published input

Let B=C[X1,X2,X3,X4] be an actual polynomial ring, let E be a
locally nilpotent derivation with a supplied polynomial slice u,
and put A=ker E. Thus Eu=1 and B=A[u]. Choose any positive integer
weights w_i on these actual coordinates and put

\[
D=\sum_{i=1}^4 w_iX_i\partial_{X_i}.
\tag{1}
\]

The weights need not equal the E-degrees. No Euler-shift assumption is
needed. There is an exact finite linear criterion for whether A contains
an actual coordinate of B that is homogeneous for D. Success proves
A is a polynomial three-ring, by the published regular-kernel theorem
below. It does not follow that this test always succeeds at shift one,
or in any arbitrary sliced presentation.

The external recognition input is Bhatwadekar, Gupta and Lokhande,
Theorem 3.5: over a characteristic-zero field k, a nonzero k[T]-linear
LND on k[T,X,Y,Z] whose kernel is regular has kernel k[T]^[2].
The invariant T must be an actual polynomial coordinate, not merely a
nonconstant invariant. This is a published theorem being applied, not
a theorem claimed as new here. [Primary statement and proof](https://arxiv.org/html/1501.01438v1#S3)

The finite search and the actual-coordinate implication below are proved
directly. The regular-kernel recognition itself remains dependent on
that published theorem; an algebra computation is not a substitute for it.

## 2. Homogeneous coordinates are exactly the candidates with a linear term

Write B_lambda for the finite-dimensional space of polynomials of
weight lambda. Suppose a nonconstant f in B_lambda is a coordinate of
B. The Jacobian of a polynomial coordinate system is invertible at the
origin, so the gradient of f there is nonzero. Thus f has a nonzero
linear term. Such a term must be some X_i of weight lambda. In
particular every possible weight belongs to the finite set

\[
\Lambda_0=\{w_1,w_2,w_3,w_4\}.
\tag{2}
\]

Conversely, suppose f is homogeneous of positive weight lambda and
has a nonzero linear term. Positivity of all weights forces the whole
polynomial to have the form

\[
f=\sum_{w_j=\lambda}c_jX_j+
P(X_j:w_j<\lambda),\qquad \text{some }c_i\ne0.
\tag{3}
\]

Indeed a monomial containing a variable of weight lambda can contain
no other positive-weight factor. No variable of larger weight can occur.
Replacing X_i by f and fixing the other three coordinates has the
explicit polynomial inverse

\[
X_i=c_i^{-1}\left(f-\sum_{\substack{j\ne i\\w_j=\lambda}}c_jX_j
-P(X_j:w_j<\lambda)\right).
\tag{4}
\]

This proves actual coordinate status, not only a submersion or a generic
coordinate property. It does not assert that every polynomial with a
nonzero linear term is a coordinate: homogeneity and positive weights
are essential to the form (3).

## 3. The exact finite systems

For each lambda in (2), enumerate all monomials X^alpha with
sum w_j alpha_j=lambda. Put

\[
f=\sum_{\sum w_j\alpha_j=\lambda}t_\alpha X^\alpha.
\tag{5}
\]

For each i with w_i=lambda, impose the polynomial identity E(f)=0
and normalize the coefficient of the linear monomial X_i to one:

\[
\sum_\alpha t_\alpha E(X^\alpha)=0,
\qquad t_{e_i}=1.
\tag{6}
\]

Comparing all source-coordinate coefficients gives a finite affine-linear
system over C. It is important to compare the whole polynomial E(f),
not only its leading term. A successful system gives an invariant f
with the coordinate inverse (4). Conversely, any homogeneous invariant
coordinate has a nonzero coefficient c_i by Section 2; dividing it by
c_i gives a solution of one of (6). Hence the union of these finitely
many systems is an exact existence criterion for homogeneous invariant
coordinates of the displayed grading.

No presentation of A, generators of a recovered LND kernel, or unbounded
search over weights is involved. This is not an implemented solver.
Effective execution requires an exactly specified effective coefficient
field; arbitrary uneffectively specified complex coefficients do not
automatically become computational inputs.

## 4. Why success recognizes A

A is regular under the actual slice hypotheses. To see this without
assuming u is a coordinate, the slice presentation gives A isomorphic
to B/(u). Express E in the source coordinates. The identity

\[
1=E(u)=\sum_i E(X_i)\,\frac{\partial u}{\partial X_i}
\tag{7}
\]

makes the gradient ideal of u the unit ideal. The hypersurface u=0
is therefore smooth over C by the Jacobian criterion. Thus its ring A
is regular. Its finite generation follows as well from B/(u).

A successful f in (6), together with the other three coordinates in
(4), gives B=C[f]^[3]. Since E(f)=0, E is C[f]-linear in that actual
presentation; E is nonzero because Eu=1. All hypotheses of the cited
regular-kernel theorem now hold, and it gives

\[
A=\mathbb C[f]^{[2]},\qquad A\simeq\mathbb C^{[3]}.
\tag{8}
\]

The finite linear test supplies f and its ambient coordinate completion.
This note does not supply an algorithm or explicit formulas for the two
remaining invariant generators asserted by the external theorem. They
must not be described as computed merely because (6) is finite.

## 5. Actual success and the boundary of the criterion

In the whole first-shift control585, the displayed frame has weights
(1,1,1,2) and f=Y-X=a satisfies E(f)=0. It is a weight-one coordinate,
with inverse Y=f+X. Thus the present invariant-coordinate criterion
recognizes that control even though neither of the two tests disproved
in585 succeeds. This is not a repair of their false universal disjunction:
it is a different sufficient condition.

For a boundary not relying on a generic or formal frame, use the entire
actual control565, also reproduced in revised582:

\[
X_1=a+u^4,\quad X_2=b+u^5,\quad
X_3=c+u^6+u^3,\quad X_4=u+X_2^2-X_1X_3.
\tag{9}
\]

It has the whole inverse U=X4-X2^2+X1X3, u=U,
a=X1-U^4, b=X2-U^5, c=X3-U^6-U^3. Its actual positive weights are
(4,5,6,7), and its Euler shift is12, not1. At each candidate weight
4,5,6,7 the homogeneous space is just C X_i: two positive-weight
factors already have weight at least8. None of E(X_i) is zero.
For the fourth row the whole derivative is

\[
E(X_4)=1-7u^6-6au^5+10bu^4-4cu^3-3au^2.
\tag{10}
\]

So no system (6) succeeds in this actual known-polynomial control.
Revised582 also proves it has no homogeneous slice. The combined
homogeneous-invariant-coordinate and homogeneous-slice tests therefore
do not cover arbitrary positive-shift frames. This is not a shift-one
counterexample and must not be used as one.

Whether a homogeneous invariant coordinate or homogeneous slice must
exist for every actual first-shift frame remains an unproved candidate
bridge here. It is not inferred from the slice presentation B=A[u].

## 6. Verification and status

The finite search and coordinate inverse are exact mathematical
arguments. Fresh unsaved algebra checks the entire success control,
the finite weight spaces in the failure control and the polynomial
identities there. The cited regular-kernel theorem was checked against
its primary statement with its nonzero, coordinate and regularity
hypotheses, not inferred from the title of a paper.

No saved checker was executed, imported or compiled. This criterion is
not a solution of cancellation, a terminating coordinate-reduction
algorithm, formal verification, or a novelty claim. It requires a
separate saved-source review before being accepted in the current ledger.
