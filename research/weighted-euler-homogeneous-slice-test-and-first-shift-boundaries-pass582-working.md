# A finite homogeneous-slice recognition test and the first-shift boundary

## 1. Actual hypotheses and bounded conclusions

Let

\[
B=\mathbb C[X_1,\ldots,X_n]=A[u],\qquad
E=\partial_u,\quad Eu=1,\quad A=\ker E,\qquad
d_i=\deg_E X_i>0,
\qquad D=\sum_i d_iX_i\partial_{X_i}.
\tag{1}
\]

The displayed \(X_i\) are actual polynomial coordinates. The supplied
slice \(u\) is an actual polynomial, but is not assumed to be an ambient
coordinate or a \(D\)-eigenfunction. Polynomiality of \(A\) is not an
input. Let \(\delta=\deg_E D\) be the exact whole-ring shift.

There is an exact finite linear test, in the original coordinates, for
the existence of any \(D\)-homogeneous slice \(v\), that is,

\[
Ev=1,\qquad Dv=\lambda v\quad(\lambda\in\mathbb C).
\tag{2}
\]

Success implies that \(A\) is a polynomial \((n-1)\)-ring and supplies
an actual coordinate completion with a slice. The finite test and this
recognition implication do not require \(\delta=1\).

For \(\delta=1\), retained 576 and 577 give an exact slice-adjustment
system. A complete actual first-shift control below proves that this
system need not have a solution: it has no homogeneous slice for its
displayed Euler field, and no invariant slice adjustment can even make
the slice coefficient constant. Separately, local finiteness and the
positive Euler grading do not
force the coefficient of the supplied slice in \(D(u)\) to be constant,
a unit, or invariant under the recovered derivation. An explicit actual
first-shift family below disproves all three tempting restrictions.

The new first-shift countercontrol has a known polynomial invariant ring,
and its recovered derivation becomes sliced after primitive division.
It refutes guaranteed homogeneous-slice availability, not general
first-shift recognition or recognition by other means. The retained565
control separately shows an empty test at shift 12. No general
plateau-escape theorem or arbitrary cancellation conclusion is proved.
No novelty is claimed.

The directly used contracts are the complete actual control565,
the Euler and commutator statements576--577, and the actual control578.
The current579 and581 were also read completely to distinguish an
eigen-slice test from fixed-direction replica tests. In particular the
one-step obstruction in581 has an already visible homogeneous slice;
it is not a counterexample to testing (2) first.

## 2. Only finitely many homogeneous weights can contain a slice

Let \(o\) be the origin \(X_1=\cdots=X_n=0\) of the actual coordinate
frame. It is the unique fixed point of the positive Euler action.
Write \(B_\lambda\) for the space of polynomials homogeneous of source
weight \(\lambda\) for the positive weights \(d_i\). Define

\[
\Lambda=\{d_i:E(X_i)(o)\ne0\}.
\tag{3}
\]

This is a finite, nonempty set of positive integers. Nonemptiness follows
by evaluating \(Eu=1\) at \(o\): if all \(E(X_i)(o)\) vanished, so would
\(Eu(o)\).

Suppose (2) holds. Since \(Ev=1\), \(v\) is nonconstant. The actual
positive Euler decomposition of \(B\) shows that its scalar eigenvalue
\(\lambda\) is a positive integer and \(v\in B_\lambda\). Moreover

\[
1=Ev(o)=\sum_i E(X_i)(o)
                   \frac{\partial v}{\partial X_i}(o).
\tag{4}
\]

A derivative \(\partial v/\partial X_i(o)\) can be nonzero only if the
linear monomial \(X_i\) occurs in \(v\). Homogeneity then requires
\(\lambda=d_i\). At least one term in (4) is nonzero, so

\[
\lambda\in\Lambda\subseteq\{d_1,\ldots,d_n\},
\qquad \lambda\le\max_i d_i.
\tag{5}
\]

The argument uses the tangent vector of the actual derivation at the
actual Euler origin. It does not assert that \(u\) or an invariant
coefficient is an ambient coordinate.

For every \(\lambda\in\Lambda\), enumerate the finitely many source
monomials

\[
\mathcal M_\lambda=
\{X^\alpha:\alpha\in\mathbb Z_{\ge0}^n,
                      \ \sum_i d_i\alpha_i=\lambda\}.
\tag{6}
\]

They are a basis of \(B_\lambda\). Put
\(v=\sum_{M\in\mathcal M_\lambda}t_M M\), with scalar unknowns \(t_M\).
The polynomial identity

\[
\sum_{M\in\mathcal M_\lambda}t_M E(M)=1
\tag{7}
\]

is a finite affine-linear system over \(\mathbb C\), obtained by
comparing coefficients in the actual coordinates. Equations (3)--(7)
prove both directions of the exact test: some system (7) is consistent
if and only if a homogeneous slice exists.

No generators of \(A\), no kernel presentation, and no unbounded search
over weights are needed. The statement is an exact finite algebraic
criterion, not an implemented solver. Effective execution requires
exactly specified effective coefficients; arbitrary complex input is
not silently converted into an effective number field.

## 3. Why a successful test recognizes the invariant ring

Let \(v\) satisfy (2). Since \(Ev=Eu=1\), we have
\(q=v-u\in A\). Hence \(B=A[v]\), and evaluation at \(v=0\) gives

\[
B/(v)\simeq A.
\tag{8}
\]

This is the slice presentation, not a prior assertion that \(v\) is one
of the actual polynomial coordinates.

There is an explicit coordinate completion. Equation (4) supplies a
nonzero linear term of \(v\) of weight \(\lambda\). A monomial of total
weight \(\lambda\) cannot involve a variable of larger weight, and a
monomial involving a variable of weight exactly \(\lambda\) must be
that variable alone. Thus the complete homogeneous polynomial has form

\[
v=\sum_{d_i=\lambda}c_iX_i+
       P\bigl(X_j:d_j<\lambda\bigr),
\qquad c_i\in\mathbb C,\quad\text{some }c_i\ne0.
\tag{9}
\]

Choose \(i\) with \(c_i\ne0\). The actual replacement of \(X_i\) by
\(v\), fixing all other coordinates, has the whole polynomial inverse

\[
X_i=c_i^{-1}\left(v-\sum_{\substack{j\ne i\\d_j=\lambda}}c_jX_j
                        -P(X_j:d_j<\lambda)\right).
\tag{10}
\]

The right side uses no \(X_i\) in its polynomial part. Hence \(v\) is
now proved to be an ambient coordinate. In particular the residue
classes of the other \(n-1\) coordinates freely generate \(B/(v)\).
Transport those classes to \(A\) by the actual slice Taylor map
\(\pi_v(f)=\sum_{r\ge0}(-v)^rE^r(f)/r!\). It has kernel \((v)\)
and image \(A\), as follows directly from \(B=A[v]\). If \(g_j\) are
the Taylor images of those remaining coordinates, (8) gives

\[
B=\mathbb C[g_1,\ldots,g_{n-1},v]
 =\mathbb C[g_1,\ldots,g_{n-1},u].
\tag{11}
\]

These are actual invariant coordinate completions, now proved rather
than assumed. Equivalently, one could use the connected positive grading
and smooth homogeneous vertex of \(B/(v)\), as in576. The explicit
inverse (10) makes that longer recognition argument unnecessary here.
The grading transported to \(A\) from the quotient need not be the
restriction of \(D\) to the original subring \(A\). In particular this
proof does not insert the generally false premise \(D(A)\subseteq A\)
at positive shift.

The special condition \(D(u)=u\) is an immediate successful instance of
the test. More generally any scalar eigen-slice works, with its positive
weight from (5). If one instead finds
\(Dv=\lambda v+\gamma\) with scalar \(\gamma\) and \(Ev=1\), then
\(\lambda\ne0\): a positive Euler derivation cannot take a polynomial
to a nonzero constant, and its kernel consists of constants. Replacing
\(v\) by \(v+\gamma/\lambda\) reduces to (2). This does not enlarge the
recognition hypothesis.

## 4. Exact first-shift coefficients and slice adjustment

Now assume \(\delta=1\). The complete coefficient statement of576--577,
including the vanishing vertical leading term, gives

\[
D|_A=M+uN,\qquad D(u)=b_1u+b_0,
\qquad M\in\operatorname{Der}_{\mathbb C}(A),
\quad 0\ne N\in\operatorname{LND}(A),
\quad b_0,b_1\in A.
\tag{12}
\]

The extension of \(N\) killing the displayed slice satisfies
\([E,D]=N+b_1E\), and \(\operatorname{ad}_E^2D=0\). All coefficients
are genuine elements of \(A\). The constant term \(M\) need not be a
locally finite derivation by itself.

Every other slice for the same \(E\) is uniquely \(v=u+q\), \(q\in A\).
Directly expanding the whole derivation gives

\[
\begin{aligned}
D|_A&=(M-qN)+vN,\\
D(v)&=(b_1+Nq)v+
       \{b_0+Mq-(b_1+Nq)q\}.
\end{aligned}
\tag{13}
\]

Here the restriction \(N:A\to A\) is unchanged. Its extension killing
the new slice differs from the old extension by \(-N(q)E\), as in577.
The exact whole-ring filtration and \(\delta\) are independent of this
choice of slice.

Thus an adjusted eigen-slice exists with scalar eigenvalue \(\lambda\)
if and only if a genuine \(q\in A\) satisfies both equations

\[
\boxed{\quad Nq=\lambda-b_1,\qquad Mq+b_0=\lambda q.\quad}
\tag{14}
\]

The first equation alone is not sufficient. In particular constantizing
the coefficient of the slice requires the class of \(b_1\) in the
vector-space quotient \(A/N(A)\) to contain a complex constant.
This quotient is not being treated as a quotient ring; \(N(A)\) need
not be an ideal. Even after the first equation is solved, the second
equation remains an exact compatibility requirement. Section 2 tests
their simultaneous solvability without a presentation of \(A\), by
searching directly for \(v\) in the finite spaces \(B_\lambda\).

Section 6 proves that (14) can be unsolvable in an actual first-shift
frame. Failure of a particular supplied-slice coefficient to be constant
is weaker and, by itself, is not failure of the full test.

## 5. First-shift controls with nonconstant, noninvariant slice coefficient

Use the entire accepted578 frame in the known polynomial ring
\(\mathbb C[a,b,c,u]\):

\[
(X,Y,Z,W)=
\left(u,\ a+u^2,\ b+au+u^4,
 c+bu+\frac12au^2+u^6\right).
\tag{15}
\]

Its inverse successively recovers

\[
u=X,\quad a=Y-X^2,\quad b=Z-aX-X^4,
\quad c=W-bX-\frac12aX^2-X^6.
\tag{16}
\]

Both compositions are polynomial identities. The exact coordinate
degrees are \((1,2,4,6)\), and the entire Euler field is

\[
D=D_A+uE+uN,\qquad
D_A=2a\partial_a+4b\partial_b+6c\partial_c,
\qquad N=a\partial_b+b\partial_c.
\tag{17}
\]

For example its coefficients are
\(D(a)=2a\), \(D(b)=4b+au\), \(D(c)=6c+bu\), \(D(u)=u\),
and these satisfy all four exact Euler eigen-equations. Its shift is
one, attained on \(b\). The derivation \(N\) is nonzero and locally
nilpotent. Thus all the actual positive-Euler and first-shift hypotheses
hold before any change of supplied slice.

For every integer \(k\ge1\), supply instead the slice
\(v=u+b^k\). The map replacing \(u\) by \(v\) while fixing \(a,b,c\)
has inverse \(u=v-b^k\), so this is an actual polynomial slice without
localization. The actual frame and its Euler field remain fixed.
Since \(Ev=1\), it has exactly the same \(E\)-filtration and shift.
The entire coefficient identity is

\[
D(v)=\beta_1v+\beta_0,\qquad
\beta_1=1+k a b^{k-1},\qquad
\beta_0=(4k-1-kab^{k-1})b^k.
\tag{18}
\]

Every \(\beta_1\) is nonconstant and hence a nonunit. For \(k\ge2\),

\[
N(\beta_1)=k(k-1)a^2b^{k-2}\ne0.
\tag{19}
\]

The ordinary polynomial degrees of these supplied-slice coefficients
are unbounded as \(k\) grows, while the actual degree tuple, \(D\), and
\(\delta=1\) stay fixed. Local finiteness and positive grading therefore
do not force constancy, invertibility, or \(N\)-invariance of the
coefficient called \(b_1\) for an arbitrary supplied slice.

These controls do not obstruct eigen-slice adjustment. The original
\(u=v-b^k\) remains a visible homogeneous slice of weight one. Relative
to the new slice, \(M=D_A-b^kN\), and \(q=-b^k\), \(\lambda=1\)
satisfy both equations (14). They explicitly distinguish a false
restriction on the supplied slice from the still-open general
recognition question. Section 6 supplies a different control where no
eigen-slice adjustment exists at all.

They also justify the warning about \(M\). For \(k=2\),
\(M(a)=2a\) and \(M(b)=4b-ab^2\). The highest \(b\)-degree term of
\(M^j(b)\) is \((-1)^j j!a^j b^{j+1}\), by induction using the
\(-ab^2\partial_b\) term. Thus this coefficient derivation \(M\) is not
locally finite, even though the entire actual \(D\) is a positive Euler
derivation. Local finiteness cannot simply be passed to that coefficient.

## 6. A first-shift frame with no homogeneous slice or constantization

Work first in the actual polynomial coordinates \((a,x,z,c)\), and put

\[
B=\mathbb C[a,x,z,c],\qquad
E=(1+a^2)\partial_x+a\partial_z.
\tag{20}
\]

This is a locally nilpotent derivation: it fixes \(a,c\), and lowers
total degree in \(x,z\). Define the genuine slice and invariant

\[
u=x-az,\qquad b=ax-(1+a^2)z,\qquad
x=(1+a^2)u-ab,\quad z=au-b.
\tag{21}
\]

Direct substitution in both orders verifies the last two formulas as
the whole polynomial inverse to the first two, fixing \(a,c\).
Moreover \(Eu=1\) and \(Eb=0\). Hence
\(B=\mathbb C[a,b,c,u]\), \(E=\partial_u\) in this actual presentation,
and \(A=\ker E=\mathbb C[a,b,c]\). These conclusions are verified
polynomial identities, not an assumed coordinate property of a slice.

Choose the actual all-positive coordinate frame

\[
\begin{aligned}
X&=x,&Y&=a+x,&Z&=z,&W&=c+x,\\
a&=Y-X,&c&=W-X,&u&=X-aZ,&b&=aX-(1+a^2)Z.
\end{aligned}
\tag{22}
\]

The first row is an invertible complex linear change from
\((a,x,z,c)\); the second row, followed by (21), is its complete
polynomial inverse in coefficient-slice variables. The four first
derivatives are \((1+a^2,1+a^2,a,1+a^2)\), all nonzero elements of
\(A\), and all second derivatives vanish. Thus their exact degrees
are \((1,1,1,1)\). The weighted Euler derivation is simply the standard
Euler field in \((a,x,z,c)\).

Its complete coefficients in \((a,b,c,u)\) are

\[
\begin{aligned}
D(a)&=a,&D(c)&=c,\\
D(u)&=(1-a^2)u+ab,&
D(b)&=(1+a^2)b+a(1-a^2)u.\\
N&=a(1-a^2)\partial_b,&
M&=a\partial_a+(1+a^2)b\partial_b+c\partial_c.
\end{aligned}
\tag{23}
\]

They follow either by differentiating (21) with the standard Euler
field or by checking all four equations \(D(X_i)=X_i\). They show
that the exact whole-ring shift is one, attained on \(b\). In the
notation (12), \(b_1=1-a^2\), \(b_0=ab\), and the nonzero recovered
LND is the displayed \(N\). In particular
\([E,D]=N+(1-a^2)E\) and \(\operatorname{ad}_E^2D=0\).

The source-weight-one space consists of all linear forms in
\((a,x,z,c)\). Since all coordinate weights are one, Section 2 allows
no other candidate weight. A possible homogeneous slice therefore has
form \(v=\alpha x+\beta z+\gamma a+\epsilon c\), with complex
coefficients, and

\[
Ev=\alpha(1+a^2)+\beta a.
\tag{24}
\]

Equality to one would force \(\alpha=1\) from the constant coefficient
and \(\alpha=0\) from the \(a^2\) coefficient. This is impossible.
Thus the finite homogeneous-slice test is empty at \(\delta=1\).

There is an even stronger direct failure of slice constantization.
For any \(q\in A=\mathbb C[a,b,c]\), the first equation of (14) would
require

\[
a(1-a^2)\,q_b=\lambda-1+a^2
\qquad(\lambda\in\mathbb C).
\tag{25}
\]

Evaluation at \(a=0\) gives \(\lambda=1\), whereas evaluation at
\(a=1\) gives \(\lambda=0\). Both are evaluations of whole polynomial
identities in \(\mathbb C[b,c]\). No denominator or pointwise division
is involved. Thus no slice \(u+q\) makes the coefficient of that slice
in its \(D\)-image constant, even before the second equation of (14)
is imposed.

This is not a counterexample to first-shift polynomial recognition:
\(A\) is explicitly polynomial by (21). The recovered \(N\) has the
nonconstant common factor \(a(1-a^2)\); removing it gives
\(\partial_b\), with slice \(b\). Thus this control does not refute
recognition using a primitive induced derivation, other actual
coordinate changes, or methods beyond homogeneous-slice availability.
It makes no claim about globally minimizing frames.

## 7. A separate higher-shift frame where the finite test is empty

Take the \(n=4\) member of the completely read565 control:

\[
X_1=a+u^4,\quad X_2=b+u^5,\quad
X_3=c+u^6+u^3,\quad
X_4=u+X_2^2-X_1X_3.
\tag{26}
\]

It is a polynomial coordinate frame. Its entire inverse is

\[
U=X_4-X_2^2+X_1X_3,\qquad
u=U,\quad a=X_1-U^4,\quad b=X_2-U^5,
\quad c=X_3-U^6-U^3.
\tag{27}
\]

Both inverse orders follow by first recovering \(U=u\), then the
first three rows and finally the fourth. The actual degrees are
\((4,5,6,7)\). The Euler origin in these coordinates is also
\(a=b=c=u=0\). At that point

\[
\bigl(E(X_1),E(X_2),E(X_3),E(X_4)\bigr)(o)=(0,0,0,1).
\tag{28}
\]

Consequently (3) gives the single candidate weight \(\lambda=7\).
The source-weight-seven space is \(B_7=\mathbb C X_4\): all weights
are at least four, so a product of two positive-weight coordinates
has weight at least eight. But the whole derivative is

\[
E(X_4)=1-7u^6-6au^5+10bu^4-4cu^3-3au^2,
\tag{29}
\]

which is nonconstant. No scalar multiple has derivative one. Thus
there is no homogeneous slice for this particular actual Euler field,
even though the ring and its invariant factor are explicitly polynomial.

For the essential shift boundary, let
\(D=4X_1\partial_{X_1}+5X_2\partial_{X_2}
 +6X_3\partial_{X_3}+7X_4\partial_{X_4}\). Its complete coefficients
can be recorded without expanding large polynomials:

\[
\begin{aligned}
D(u)&=10u-3X_4,\\
D(a)&=4a+4u^4-4u^3D(u),\\
D(b)&=5b+5u^5-5u^4D(u),\\
D(c)&=6c+6u^6+6u^3-(6u^5+3u^2)D(u).
\end{aligned}
\tag{30}
\]

Since \(X_4\) has leader \(-u^7\), the coefficient degrees in
\((a,b,c,u)\) are respectively \((10,11,12,7)\). The whole-ring
shift is therefore 12. The horizontal \(c\) coefficient attains it;
the vertical contribution has shift only six. This is not a
first-shift counterexample and must not be used as one.

The frame admits the explicit nonhomogeneous elementary replacement
\(X_4\mapsto X_4-X_2^2+X_1X_3=u\). Its failure of the homogeneous
test is neither a failure of all actual reductions nor a globally
minimality assertion.

## 8. What remains and what was checked

For an arbitrary positive first-shift frame, (14) is exact and the
finite test (3)--(7) decides whether an eigen-slice exists, once its
coefficient linear systems are supplied. Section 6 disproves the claim
that some system must always be consistent at \(\delta=1\). It does not
disprove general first-shift recognition: its own invariant ring is
polynomial, and a different induced-derivation reduction is available.
General recognition and plateau-escape theorems remain unproved here.

In particular the primitive nonsliced one-step replica control581 has
the coordinate \(X=u\) of weight one, with \(D(u)=u\). The present test
already recognizes its invariant factor. Its replica obstruction does
not refute a strategy that first tests for a homogeneous slice and only
then investigates plateau moves. The same distinction applies to any
other control with a visible Euler-homogeneous slice.

Fresh unsaved algebra verified all Euler eigen-equations in (15),
the complete identities (18)--(19) and restoration equations for
\(k=1,2,3,5\), both whole inverse orders and the entire first-shift
coefficients of (20)--(23), the contradictions (24)--(25), and the
complete Euler coefficients, exact shift, and tangent-vector data of
(26). The initial 582 hold at SHA
`11f84507e8d088fea26c96f69cb0d2c85e6435eea8fbfe66a10dfd8c00bb71ca`
was withdrawn for this stronger actual first-shift control. A review
of that earlier version is not a review of this revision.
The finite-weight and recognition
arguments above are proofs, not extrapolations from those samples.
No saved checker was executed, imported, or compiled. No canonical
file or earlier source was edited. This bounded working source makes
no claim of novelty, general descent, or completion of cancellation.
