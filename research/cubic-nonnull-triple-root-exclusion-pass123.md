# A triple root of the non-null cubic scalar is impossible

The strengthened divisibility Y squared divides P cubed excludes
every non-null cubic scalar with a triple root. This is a polynomial
algebra consequence: no additional volume coefficient, rational
first-integral generator, or normal-ratio coordinate assumption is
needed after that divisibility has been proved.

The argument is separate from the unresolved cases in which the
cubic has two or three distinct roots. It remains conditional on
the supplied actual framework when applied to cancellation.

## 1. The polynomial statement needed from the actual framework

Retain the actual non-null cubic setting and the conclusion of
[the pole-bound theorem123](cubic-nonnull-pole-bound-pass123.md).
The polynomial data needed here are precisely

\[
\begin{gathered}
S=\mathbb C[s,t],\qquad g,P,Y\in S,\qquad Y\ne0,\qquad
h=P/Y\notin\mathbb C,\qquad Y^2\mid P^3,\\
g^2-D(h)Y^2=1,\qquad
\det[(g,P,Y)^t,(g,P,Y)^t_s,(g,P,Y)^t_t]\ne0 .
\end{gathered}
\tag{1}
\]

Suppose for contradiction that the exact cubic has a triple root.
Write D(h)=d3(h-r) cubed, where d3 is a nonzero complex constant
and r is complex. The shift P0=P-rY is a constant linear change
of the second and third speed entries. In the actual frame it is
the genuine original-coordinate change x2 to x2-rx3 with its
explicit inverse x2 to x2+rx3, fixing the other coordinates.

There is also a direct algebraic check that the bound persists.
At every irreducible factor of Y, twice its multiplicity in Y is
at most three times its multiplicity in P. This implies its
multiplicity in Y is at most twice its multiplicity in P. Hence

\[
\begin{gathered}
Y\mid P^2,\qquad P_0=P-rY,\qquad
Y^2\mid P_0^3,\\
P_0^3=P^3-3rP^2Y+3r^2PY^2-r^3Y^3,\\
g^2-1=d_3 P_0^3/Y,\qquad P_0\ne0 .
\end{gathered}
\tag{2}
\]

The last nonvanishing follows from h nonconstant. Thus no invocation
of a newly established divisibility theorem after changing coordinates
is necessary.

## 2. Reduced fractions determine the entire common factor

Choose coprime nonzero polynomials A0,B0 with P0/Y=A0/B0.
The letters A0,B0 here are just numerator and denominator in S,
not the actual invariant or ambient ring. Unique factorization
first gives P0=A0T and Y=B0T for one nonzero T in S. The bound
in (2) says B0 squared divides A0 cubed T. Coprimality therefore
forces B0 squared to divide T. For some nonzero C in S,

\[
\gcd(A_0,B_0)=1,\qquad
P_0=A_0 B_0^2 C,\qquad
Y=B_0^3 C,\qquad
g^2-1=d_3(A_0B_0)^3 C^2 .
\tag{3}
\]

All equalities are polynomial identities, including multiplicities.
No assumption that A0,B0 or C are coordinates or irreducible
polynomials has been made.

The polynomial g is nonconstant. Indeed g=1 or g=-1 contradicts
the nonzero right side of (3). If g were any other constant, that
right side would be a nonzero constant. The only units of S are
complex constants, so A0,B0,C would all be constants. Then P0,Y
and P would be constants as well, contrary to the nonzero determinant
in (1).

Every irreducible factor of the nonconstant polynomial g squared
minus one has multiplicity at least two: its exponent on the right
of (3) is three times a nonnegative integer plus twice another.
In symbols,

\[
g^2-1=c_*\prod_i p_i^{m_i},\qquad
c_*\in\mathbb C^*,\quad p_i\text{ distinct irreducibles},\qquad
m_i=3\nu_{p_i}(A_0B_0)+2\nu_{p_i}(C)\ge2 .
\tag{4}
\]

## 3. Two fibers cannot both have only repeated components

Here is the elementary derivative lemma used to contradict (4).
For any nonconstant polynomial f over C, in any finite number of
variables, the polynomial f squared minus one has at least one
irreducible factor of multiplicity one.

To prove this, suppose every multiplicity m_i in its factorization
is at least two, and put R0 equal to the product of p_i to powers
m_i-1. Differentiating f squared minus one shows p_i to power
m_i-1 divides 2f times each partial derivative of f. No p_i divides
f, since it divides f squared minus one. Unique factorization
therefore gives

\[
R_0:=\prod_i p_i^{m_i-1}\ \mid\ \partial_j f
\quad\text{for every }j,\qquad
\deg R_0
 =\sum_i(m_i-1)\deg p_i
 \ge\frac12\sum_i m_i\deg p_i
 =\deg f .
\tag{5}
\]

In characteristic zero at least one partial derivative of the
nonconstant f is nonzero. Its total degree is at most deg(f)-1,
contradicting its divisibility by R0. This proves the lemma.
It is a direct polynomial argument and does not appeal to an
unexpanded polynomial abc or fibration theorem.

Apply the lemma to g. It contradicts (4), completing the exclusion
of a triple root of D.

## 4. Consequence and scope

In the supplied actual cubic framework, constant reciprocal
equivalence122 first permits a cubic polynomial D. The present
argument says that this cubic must have at least two distinct
complex roots. It does not exclude the double-root or squarefree
cases, and it does not show that every remaining coefficient
tuple is realizable.

The result uses only (1) after the actual pole-bound theorem.
In particular it does not need the additional vertical-divisor
restriction, the further differential relation between the two
potential coefficients, or a unit-row hypothesis. Any polynomial
speed control with D equal to a nonzero constant times a shifted
cube and nonzero speed determinant must fail the strengthened
bound somewhere, regardless of its other coefficient identities.

No new checker or external source is required for the all-polynomial
derivative lemma. The proof is not a global original-coordinate
recognition theorem or a solution of the unrestricted cancellation
problem. Files through122 remain unchanged.

