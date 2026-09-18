# Rank-sensitive adjoint bounds from an actual three-good frame

## 1. Statement and scope

Suppose \(n\ge2\) and the displayed generators are actual polynomial
coordinates:
\[
 \begin{gathered}
 B=\mathbb C[x_1,\ldots,x_{n-1},z]=A[u],\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\qquad A=\ker E,\quad E(u)=1,\\
 E^2x_i=0,\qquad a_i=Ex_i,\qquad
 r=\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,\ldots,a_{n-1}],
 \qquad T=\partial_z .
 \end{gathered}
 \tag{1}
\]
There is no degree assumption on \(z\) in the first conclusion:
\[
 \boxed{\operatorname{ad}_E^{\,r+1}T=0.}
 \qquad
 \text{If }E^3z=0,\quad
 \boxed{\operatorname{ad}_E^{\,n}T_j=0
 \text{ for every original coordinate partial }T_j.}
 \tag{2}
\]
For the second conclusion, the case where all the \(a_i\) vanish is
recognized directly below; in that case all original partials commute
with \(E\), so the stated bound also holds.

In dimension four, the first bound and the common-kernel theorem125
give a bad-partial adjoint degree at most two. The second bound gives
degree at most three for each other partial even when the acceleration
is nonconstant. These are degrees of conjugated coordinate partials,
not degrees of the original coordinates under \(E\).

This supplies bounds within the supplied class. It does not supply
three good coordinates for an arbitrary sliced action, or recognize
every action in this class. All files through pass125 remain unchanged.

## 2. The conjugation orientation and the exact cofactor column

Let \(\phi_t=\exp(tE)\), acting on \(B[t]\) and fixing \(t\), and let
\(F_t=(\phi_tx_1,\ldots,\phi_tx_{n-1},\phi_tz)\).
It is an actual polynomial automorphism over \(\mathbb C[t]\), with
inverse \(F_{-t}\). Its Jacobian determinant with respect to the original
coordinates is a unit of \(B[t]\), hence a complex constant, and its
value at \(t=0\) is one.

Use the bracket convention \([E,T]=ET-TE\). For
\(C_t=\phi_tT\phi_{-t}\), one has \(C_t(F_{t,j})=\delta_{jn}\).
Consequently, writing derivation coefficients as columns,
\[
 \begin{gathered}
 \operatorname{Jac}(F_t)\,C_t(x)=e_n,\qquad
 C_t(x)=\operatorname{Jac}(F_t)^{-1}e_n
          =\operatorname{adj}(\operatorname{Jac}(F_t))e_n,\\
 C_t=\sum_{k\ge0}\frac{t^k}{k!}\operatorname{ad}_E^kT,\qquad
 dF_{t,i}=dx_i+t\,da_i\quad(1\le i<n).
 \end{gathered}
 \tag{3}
\]
The sum is finite: conjugation is a polynomial derivation on \(B[t]\).
Alternatively the coefficient identities follow by differentiating
the conjugation in \(t\). There is no substitution of \(F_{-t}\)
in place of \(F_t\) in the inverse-Jacobian column in (3).

Entry \(j,n\) of the adjugate is the signed minor obtained by deleting
row \(n\) and column \(j\). In particular, every component of this
column uses only the first \(n-1\) rows of the Jacobian. The possibly
high-degree last coordinate \(\phi_tz\) is absent.

## 3. Alternating multilinearity supplies the rank-sensitive bound

Over \(K=\operatorname{Frac}B\), characteristic zero identifies the
rank of the differentials \(da_i\) with \(r\). This follows by taking
a separating transcendence basis of the speed field and extending
it to one of \(K\); algebraic field extensions are separable.

In the exterior expansion
\[
 \bigwedge_{i=1}^{n-1}(dx_i+t\,da_i)
   =\sum_{I\subseteq\{1,\ldots,n-1\}}
       t^{|I|}\,
       \bigwedge_{i=1}^{n-1}
       \begin{cases}da_i,&i\in I,\\ dx_i,&i\notin I,\end{cases}
 \qquad [t^k](\cdot)=0\quad(k>r),
 \tag{4}
\]
the order of the factors is always the original increasing order.
Every term of degree \(k>r\) contains \(k\) linearly dependent speed
differentials, so it vanishes. Coordinates of this exterior form are
exactly the signed minors in (3). Vanishing over \(K\) is vanishing
in \(B\), since \(B\) is a domain. Thus the column has degree at
most \(r\), proving the first assertion in (2).

No assertion about the ordinary polynomial degree of the \(a_i\)
or about the polynomiality of their coordinate algebra is used.

## 4. The exact intrinsic shift and its degree-zero endpoint

Assume some \(a_i\ne0\). The
[common intrinsic-speed theorem125](three-good-intrinsic-speed-quotient-pass125.md),
Sections 2--5, proves that \(T(A)\ne0\) and that its exact
\(u\)-filtration shift \(d\) is nonnegative. More precisely,
\[
 \begin{gathered}
 T(A)\subseteq A[u]_{\le d},\qquad
 T(u)\in A[u]_{\le d},\qquad
 N(f)=[u^d]T(f)\quad(f\in A),\\
 0\ne N\in\operatorname{LND}(A),\quad N(a_i)=0,\qquad
 \deg_t(\exp(tE)T\exp(-tE))=d\le r\le n-2 .
 \end{gathered}
 \tag{5}
\]
For completeness, the equality of degrees is exact, not just an
upper bound. On \(A\), conjugation replaces \(u\) in \(T(f)\) by
\(u+t\). On \(u\), it replaces \(u\) in \(T(u)\) by \(u+t\).
Some \(f\in A\) has nonzero coefficient \(N(f)\), so the conjugation
has degree exactly \(d\). The bound \(r\le n-2\) is the invariant-field
dimension consequence of the nonzero intrinsic \(N\).

The top commutator divided by \(d!\) restricts to \(N\) on \(A\),
but it can send \(u\) to \([u^d]T(u)\ne0\). It is not silently
identified with the extension of \(N\) that kills \(u\).

Now let \(n=4\). If \(d=0\), (5) gives \([E,T]=0\).
Hence \(T(a_i)=T(Ex_i)=0\), so each \(a_i\) belongs to the
actual polynomial three-ring
\(R=\mathbb C[x_1,x_2,x_3]\).
The restriction \(E|_R\) is a nonzero LND and is nice on these three
generators. The exact retained
[three-variable linear-invariant theorem](nice-linear-invariant-source-pass71.md)
therefore gives constants \(\lambda_i\), not all zero, with
\(E(\sum_i\lambda_ix_i)=0\).
That linear form is an ambient polynomial coordinate of \(B\).
Since \(A\) is regular, the retained Bhatwadekar--Gupta--Lokhande
recognition gate in
[coordinate-frame minimization, Section 2](coordinate-frame-minimization-pass.md)
gives \(A\simeq\mathbb C^{[3]}\).
No slice for the restriction \(E|_R\) is assumed.

If all speeds vanish, then \(E=E(z)\partial_z\). The given slice
satisfies \(E(z)\partial_zu=1\), so \(E(z)\in\mathbb C^*\).
The kernel is the good-coordinate ring directly.
If the speed rank is zero and some speed is nonzero, that speed is a
nonzero complex constant and the corresponding good coordinate is
an actual coordinate slice, again giving recognition.

Thus any as-yet unrecognized four-dimensional instance in (1) has
either \(r=1,d=1\), or \(r=2,d=1\) or \(2\).
This is a restriction on the selected bad partial, with no degree
bound on \(z\).

## 5. A quadratic last coordinate bounds every column

Suppose now \(E^3z=0\), and write \(c=Ez\), \(q=E^2z\in A\).
The all-zero-speed case was settled above; assume some speed is nonzero.
If \(q\ne0\), it is twice the leading \(u\)-coefficient of \(z\).
The same intrinsic \(N\) in125 kills that coefficient. If \(q=0\),
it is of course already in \(\ker N\). Thus
\[
 \begin{gathered}
 \operatorname{rank}_K d(a_1,\ldots,a_{n-1},q)\le n-2,\\
 dF_{t,n}=dz+t\,dc+\frac{t^2}{2}\,dq,\qquad
 \deg_t\operatorname{adj}(\operatorname{Jac}(F_t))\le n-1 .
 \end{gathered}
 \tag{6}
\]
Only the transcendence-degree bound for \(\ker N\) is needed here.
The source-dependent identification of the fourfold intrinsic
quotient with a polynomial plane, and its faithful flatness, are
not required for this rank inequality.

For a column other than the last, each relevant minor has \(n-2\)
good rows and the last row. Its degree is at most \(n\) before
cancellation. Its possible degree-\(n\) term wedges \(n-2\)
differentials \(da_i\) with \(dq\). These \(n-1\) differentials lie
in a space of dimension at most \(n-2\), so the term is zero.
The last column already has degree at most \(n-2\) by (4)--(5).
Applying the conjugation calculation to every original partial
proves the second assertion in (2).

In dimension four this says exactly
\(\operatorname{ad}_E^3T=0\) and
\(\operatorname{ad}_E^4T_j=0\) for the other three partials.
The potential degree-four term is the wedge of two speed
differentials with \(dq\), not an assumed constant-acceleration term.

## 6. Comparison with the retained coordinate-partial height

For an actual partial \(T_j\), let \(\delta_j\) be its derivation
degree for the \(u\)-filtration. The retained definition is
\[
 \delta_j=\sup_{f\ne0}\bigl(\deg_uT_j(f)-\deg_uf\bigr),
 \qquad
 H=\sum_{j=1}^4(\delta_j+1).
 \tag{7}
\]
A degree-minus-one partial already recognizes the kernel. For a
nonnegative degree the leading-LND argument kills the would-be
top term on \(u\), so \(\delta_j\) equals the degree of the conjugated
partial, exactly as in Section 4.

Consequently the quadratic case supplies
\(\delta_z\le2\), \(\delta_j\le3\) for the three others. The sum
of these four degrees is at most eleven, but the height \(H\) in
(7) is at most **fifteen**, not eleven.
The complete retained
[height-ten theorem73](height-ten-closure-pass73.md)
recognizes every frame with \(H\le10\).
The older minimization note's lower threshold is historical and is
not the current all-profile endpoint.

Thus a hypothetical nonpolynomial kernel in this supplied quadratic
class would satisfy
\[
 11\le H_{\min}(E)\le H\le15.
 \qquad
 H=11\ \Longrightarrow\quad
 \text{sorted }(\delta_j)\in
 \{(0,2,2,3),(1,1,2,3),(1,2,2,2)\}.
 \tag{8}
\]
For the displayed list, two zero degrees, or a zero and a one,
are already recognized by the retained low-profile lemmas.
After excluding those and degree minus one, the list is simply the
partitions of \(\sum\delta_j=7\) subject to the present upper bounds.
It does not assert that any listed profile realizes a nonpolynomial
kernel, or that \(H_{\min}=11\). Higher displayed heights remain
possible under these bounds.

Recognition of nice frames80 and of the constant-acceleration
class123 is separate. Their additional hypotheses cannot be inferred
from the numerical bounds in (6)--(8). Neither coordinate
\(E\)-degree minimization124 nor a change of notation turns (7)
into a height-ten entry theorem.

## 7. Prior machinery and verification boundary

The inverse-flow identity and cofactor method were already used,
for example in
[generation-gap54, Section 5](profile-generation-gap-pass54.md).
The present application uses only the good rows for the selected
column and their algebraic differential rank. The
[constant-acceleration frame87](constant-acceleration-three-good-frame-pass87.md)
proved the fourfold third/fourth-adjoint bounds under constant
acceleration. Section 5 extends those bounds to variable quadratic
acceleration by125's common intrinsic invariant field.
No historical novelty claim is made.

As a direct check on orientation and on a nonsharp rank bound, the
actual family in
[the three-good checker125](three_good_controls_pass125.py)
has adapted coordinates \((a,b,c,u)\), good coordinates
\((a,b+a^2u,c+bu)\), and last coordinate \(u+(c+bu)^\ell\).
Its actual bad partial is
\(T=\partial_u-a^2\partial_b+(a^2u-b)\partial_c\).
Conjugation is exactly \(T+t\,a^2\partial_c\).
Thus \(d=1\) while the speeds \((0,a^2,b)\) have rank two, for
every positive integer \(\ell\); the algebraic inverse in125 shows
why this is an actual frame rather than a formal vector-field array.
The existing finite checker tests \(\ell=2,3,5\), not all integers.

This is a written algebraic proof. No numerical run or new primary-source
audit is claimed. The complete retained125 intrinsic proof,71
linear-invariant source gate, coordinate-partial minimization proof,
height-ten73 synthesis, and87 frame note were reread for the exact
uses above. Only the cited cofactor section54 was reread for the
deduplication comparison.
The recognition statements retain their cited working-proof and
source dependencies; these computations alone do not prove
unrestricted cancellation.
