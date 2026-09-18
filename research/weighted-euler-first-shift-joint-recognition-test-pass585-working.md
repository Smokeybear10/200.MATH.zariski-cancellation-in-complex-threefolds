# The two proposed first-shift recognition tests can both fail

## 1. Exact conclusion and the general gap it addresses

There is an actual all-positive polynomial coordinate frame of a known
translation four-ring with exact weighted Euler shift one for which
neither of the following features is present:

1. A slice for the original LND that is homogeneous for the displayed
   weighted Euler derivation.
2. A slice for the recovered LND on the invariant ring, even after
   primitive normalization.

Thus the proposed universal disjunction between these two tests is
false. The countercontrol has a complete polynomial inverse, and the
recovered derivation is already primitive and has a genuine zero. It is
not an assigned initial tuple, a coefficient-field construction, or a
formal vector field unconnected to the actual Euler derivation.

The invariant ring is explicitly polynomial in this example. The result
does not refute general recognition at Euler shift one, recognition by
other methods, changing the coordinate frame before testing, or a
sequence of other actual reductions. It is not a cancellation
counterexample or a globally minimizing-frame claim. No novelty is
claimed, and no recognition theorem is being asserted merely from the
presence or absence of either proposed feature.

The meaning of exact Euler shift and corrected recovery is that of
retained576--577. The finite homogeneous-slice test is proved in revised
582, whose first-shift control supplied the base translation used here.
The obstruction below also proves the relevant finite-weight restriction
directly, so it does not depend on an unproved general existence claim.
No special paraboloid-chart hypothesis is used.

## 2. The actual sliced ring and a complete coordinate change

Start in the actual polynomial coordinates \((a,x,z,c)\), with

\[
B=\mathbb C[a,x,z,c],\qquad
E=(1+a^2)\partial_x+a\partial_z.
\tag{1}
\]

The derivation fixes \(a,c\) and lowers total degree in \(x,z\), so it
is locally nilpotent. Define actual polynomials

\[
u=x-az,\qquad b=ax-(1+a^2)z.
\tag{2}
\]

Their entire polynomial inverse, fixing \(a,c\), is

\[
x=(1+a^2)u-ab,\qquad z=au-b.
\tag{3}
\]

Substituting (2) into (3) gives back \(x,z\), and substituting (3) into
(2) gives back \(u,b\). Also \(Eu=1\) and \(Eb=0\). Consequently

\[
B=\mathbb C[a,b,c,u]=A[u],\qquad
A=\ker E=\mathbb C[a,b,c],\qquad E=\partial_u.
\tag{4}
\]

These are whole polynomial identities, with no localization or root
extension. They establish the polynomial invariant ring in this control
rather than assuming it in a proposed general theorem.

Use the following explicitly fixed polynomials in \(a\):

\[
\begin{aligned}
h&=a(1-a^2),&
f&=a(1-a^2)^2,\\
\ell&=-2a^4+7a^2-1,&
j&=-2a^2(a^2-2)(a^2-4),&
k&=1+a^2.
\end{aligned}
\tag{5}
\]

The letters in (5) denote coefficient polynomials, not new ambient
coordinates or an invariant-field reparametrization. Set

\[
H=f u^2+(\ell b+1)u,
\tag{6}
\]

where (2) makes \(H\) an actual polynomial in \(a,x,z\). The coordinate
frame to be tested is

\[
X=x,\qquad Y=a+x,\qquad Z=z,\qquad W=c+H.
\tag{7}
\]

The first three rows form an invertible linear change in \(a,x,z\),
and the last adds a polynomial in those unchanged variables to \(c\).
For the complete inverse, define successively

\[
\begin{aligned}
a_*&=Y-X,&u_*&=X-a_*Z,&
b_*&=a_*X-(1+a_*^2)Z,\\
c_*&=W-f(a_*)u_*^2-(\ell(a_*)b_*+1)u_*.
\end{aligned}
\tag{8}
\]

Then \((a,b,c,u)=(a_*,b_*,c_*,u_*)\). To recover the original
\((a,x,z,c)\), one can simply take \((a_*,X,Z,c_*)\); equivalently
apply (3) to \(a_*,b_*,u_*\). In one composition, (7)--(8) first recover
\(a\), then \(u,b\), then \(c\). In the reverse composition, (3)
recovers \(X,Z\), the relation \(Y=a_*+X\) recovers \(Y\), and (6)
recovers \(W\). Thus both whole inverse orders are polynomial.

## 3. Exact positive degrees and the entire Euler field

In the genuine slice presentation (4), the complete first three rows are

\[
X=(1+a^2)u-ab,\qquad
Y=a+(1+a^2)u-ab,\qquad Z=au-b.
\tag{9}
\]

Their coefficients of \(u\) are nonzero polynomials in \(A\), even
though they may vanish on particular fibers. The fourth row is exactly
\(W=c+f u^2+(\ell b+1)u\), with \(f\ne0\). Hence the actual degrees are

\[
(d_X,d_Y,d_Z,d_W)=(1,1,1,2).
\tag{10}
\]

No specialization at a zero of a leader is used to assign these degrees.
Let the actual weighted Euler derivation be

\[
D=X\partial_X+Y\partial_Y+Z\partial_Z+2W\partial_W.
\tag{11}
\]

Since \(X,Y,Z\) linearly span \(a,x,z\), this field restricts to the
ordinary Euler field \(a\partial_a+x\partial_x+z\partial_z\) on
\(\mathbb C[a,x,z]\). The last coefficient is determined by the full
equation \(D(c+H)=2(c+H)\).

Two elementary polynomial identities explain the cancellation needed
to calculate it:

\[
h\ell=2a^2f-af',\qquad
j=-a(\ell'+2f),
\tag{12}
\]

where primes denote ordinary differentiation in \(a\). Both identities
follow by expanding the polynomials in (5); no division by \(h\) or
other coefficient is needed. On \(a,b,u\), direct differentiation of
(2) gives

\[
D(a)=a,\qquad
D(b)=(1+a^2)b+hu,\qquad
D(u)=(1-a^2)u+ab.
\tag{13}
\]

Applying these whole coefficients to (6), the coefficient of \(u^2\)
in \(D(H)\) is \(af'+2(1-a^2)f+h\ell=2f\), by (12).
The coefficient of \(u\) is
\(\{a\ell'+2\ell+2af\}b+(1-a^2)\), and its constant coefficient
is \(ab(\ell b+1)\). Thus the entire fourth coefficient is

\[
D(c)=2c-ab(\ell b+1)+(jb+k)u.
\tag{14}
\]

Equations (13)--(14), not just their leading parts, satisfy all four
Euler eigen-equations for (7). Since (11) is the Euler derivation in an
actual polynomial coordinate frame, it is locally finite and defines
the connected positive grading with weights (10).

For a polynomial derivation on \(A[u]\), with the actual generators
\(a,b,c\) of \(A\), the whole-ring shift is the maximum of the degrees
of its three horizontal coefficients and the degree of its \(u\)
coefficient minus one. The Leibniz rule proves the upper bound on every
polynomial, and the corresponding generator attains every nonzero
candidate. By (13)--(14), this shift is exactly

\[
\delta=1.
\tag{15}
\]

It is attained already on \(b\), since \(h\ne0\). The vertical
coefficient has degree one, so its shift contribution is only zero.

## 4. The genuinely recovered derivation is primitive and nonsliced

Taking the whole coefficient of \(u\) on \(A\) gives

\[
N=h\partial_b+(jb+k)\partial_c,
\qquad N(a)=0.
\tag{16}
\]

The complete commutators are

\[
[E,D]=N+(1-a^2)E,\qquad [E,[E,D]]=0.
\tag{17}
\]

Thus corrected recovery with the actual supplied slice \(u\), as in577,
subtracts \([E,D](u)E=(1-a^2)E\) and gives exactly (16), extended to
kill \(u\). In particular the direction is not chosen independently of
the Euler field.

This is a nonzero LND on \(A\). It fixes \(a\), takes \(b\) to the
polynomial \(h(a)\), and takes \(c\) to a polynomial linear in \(b\).
Explicitly \(N^2(c)=jh\), \(N^3(c)=0\), and \(N^2(b)=0\).
These finite identities on generators prove local nilpotence on the
whole polynomial ring.

There is no nonconstant common factor in its coefficients. Any common
irreducible factor must divide \(h=a(1-a)(1+a)\). But

\[
(jb+k)|_{a=0}=1,\qquad
(jb+k)|_{a=1}=(jb+k)|_{a=-1}=2-6b.
\tag{18}
\]

None is the zero polynomial in \(b,c\). Hence
\(\gcd(h,jb+k)=1\) in \(A=\mathbb C[a,b,c]\), so \(N\) is already
primitive. Changing polynomial coordinates on \(A\) cannot create a
common polynomial factor of all images that was absent from the ideal
generated by these generator images. A nonzero complex rescaling does
not affect the following obstruction.

At \(a=1,b=1/3\), both nonzero components in (16) vanish. More precisely

\[
N(A)\subseteq\mathfrak p=(a-1,\ b-1/3)\subset A,
\tag{19}
\]

because both generator images lie in that proper ideal. The image of
every polynomial has the same property by the Leibniz rule. Thus no
polynomial \(s\in A\) can satisfy \(N(s)=1\). Primitive normalization
does not remove this failure, since there is no factor to divide out.
This proves failure of the second proposed test.

## 5. No homogeneous slice for the original derivation exists

The fixed line gives the shortest proof. Any slice for the same \(E\)
is \(v=u+q\), with \(q\in A\). If \(Dv=\lambda v\), the entire
commutator identity (17) gives
\(\lambda=[E,D](v)=N(q)+1-a^2\). Evaluate at
\(a=1,b=1/3\), where \(N\) vanishes on every element of \(A\) by (19).
It follows that \(\lambda=0\). But a nonconstant eigenfunction for a
positive Euler grading has a positive integer eigenvalue; \(v\) is
nonconstant because \(Ev=1\). This contradiction proves that no
homogeneous slice exists.

The same argument gives a general first-shift necessary condition,
without assuming a polynomial invariant ring: at every complex point
\(p\) of \(\operatorname{Spec}A\) where \(N\) vanishes, an eigen-slice
weight must equal \(b_1(p)\), where
\([E,D]=N+b_1E\). Indeed \(v-u\in A\) and the same commutator equation
applies. The value at such a point is unchanged when the supplied slice
is shifted, since \(b_1\) changes by an \(N\)-image. In this control its
value zero rules out every positive eigenweight. We do not claim that
slice constantization with the scalar zero is impossible.

For an independent check retaining all homogeneous candidates, let
\(o\) be the origin of the actual frame (7).
The inverse (8) shows it is also \(a=x=z=c=0\). If \(Ev=1\) and
\(Dv=\lambda v\), positivity makes \(\lambda\) a positive integer and
\(v\) a source-weight-\(\lambda\) polynomial. At \(o\),

\[
1=Ev(o)=\sum_{T\in\{X,Y,Z,W\}}E(T)(o)\,
                      \frac{\partial v}{\partial T}(o).
\tag{20}
\]

Therefore \(v\) has a nonzero linear source-coordinate term, whose
weight equals \(\lambda\). The only weights of the actual coordinates
are one and two. Hence \(\lambda\) must be one or two, exactly as in
the finite test of582. This argument excludes all higher weights.

For weight one, \(v\) is a complex linear form in \(X,Y,Z\), equivalently
in \(a,x,z\). It has form \(v=\alpha x+\beta z+\gamma a\), and

\[
Ev=\alpha(1+a^2)+\beta a.
\tag{21}
\]

Equality to one would force both \(\alpha=1\) and \(\alpha=0\) by its
constant and \(a^2\) coefficients. There is no weight-one slice.

For weight two, the entire source space consists of a multiple of
\(W\) plus a quadratic form in \(X,Y,Z\). Since their linear span is
\(a,x,z\), every candidate is

\[
v=\alpha W+Q_2(a,x,z),
\qquad \alpha\in\mathbb C,
\quad Q_2\text{ an ordinary homogeneous quadratic form}.
\tag{22}
\]

There are no other monomials at this source weight. The complete
derivative of (6), converted back using (2), is

\[
E(H)=2fu+\ell b+1
 =1+(a+3a^3)x+(1-8a^2-a^4)z.
\tag{23}
\]

Write the arbitrary quadratic form as
\(Q_2=q_0a^2+q_1ax+q_2az+q_3x^2+q_4xz+q_5z^2\).
Its entire derivative is

\[
E(Q_2)=q_1a(1+a^2)+q_2a^2
 +\{2q_3(1+a^2)+q_4a\}x
 +\{q_4(1+a^2)+2q_5a\}z.
\tag{24}
\]

Since \(E(c)=0\), equations (22)--(24) give
\(Ev=\alpha E(H)+E(Q_2)\). Its constant coefficient is \(\alpha\),
so \(Ev=1\) requires \(\alpha=1\). Its coefficient of the distinct
monomial \(a^3x\) is \(3\alpha\), because (24) has no such term.
The same identity would therefore require \(\alpha=0\), a contradiction.
All six coefficients of the quadratic form have been retained. There
is no weight-two slice either.

Together with the exhaustive weight restriction from (20), this proves
that no homogeneous \(E\)-slice exists for the actual Euler derivation
(11). This is failure of the first proposed test in the same frame
where Section 4 proves failure of the second.

## 6. Scope, genuine escape boundaries, and verification

The control establishes the simultaneous failure at exact shift one
of homogeneous-slice availability and sliceness of the primitive
recovered derivation. It does not say that a polynomial invariant ring
cannot be recognized. Here the full inverse (8), followed by (2)--(3),
already exhibits \(A=\mathbb C[a,b,c]\). The original coordinate \(a\)
is also an invariant actual coordinate, though it is not one of the
all-positive displayed coordinates. No restriction on using that
information or other actual coordinate changes is proved.

The displayed frame is not offered as globally minimizing any proposed
complexity. Nor is this a fixed-slice replica-chain obstruction: no
classification of its replicas, plateau moves, or recovered directions
after such moves has been established here. In particular this source
does not combine the two failed immediate tests into an obstruction to
every hybrid or iterative strategy. It refutes only the stated universal
disjunction in a single actual first-shift frame.

Fresh unsaved algebra reconstructed both complete inverse compositions,
the exact positive degrees, all four entire Euler eigen-equations, both
commutators, the polynomial identities (12), the gcd and proper-zero
conditions, and the complete weight-two coefficient obstruction.
These computations support the displayed proofs; the universal
exclusion of candidate weights uses (20), not a sample search.
No saved checker was executed, imported, or compiled. No canonical
record or previous source was edited. This bounded working proof makes
no claim of novelty, general coordinate entry, or completed cancellation.
