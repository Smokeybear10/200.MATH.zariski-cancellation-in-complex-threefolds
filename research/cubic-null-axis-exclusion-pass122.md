# The null constant axis is excluded in the actual cubic framework

The exact cubic branch cannot have a null constant ambient axis under
the full original-coordinate hypotheses retained in90. The reciprocal
scalar alternative was excluded in121. The cubic scalar alternative
now contradicts the irreducibility of an original affine-linear
coordinate, using a global reconstruction identity and a finite-place
residue argument.

This excludes one entire axis alternative in the supplied framework.
It does not exclude the non-null axis, establish entry from an arbitrary
polynomial cylinder, or prove the general cancellation conjecture.

## 1. Actual hypotheses and the scalar reduction

Retain [potential90](nonconical-quadratic-potential-pass90.md),
[cubic relation90](nonconical-cubic-relation-pass90.md), and the
[constant-axis restriction120](cubic-nondegenerate-conic-axis-pass120.md).
The ambient ring is B=C[x1,x2,x3,z]=A[u], with the four displayed
elements actual polynomial coordinates, E=partial_u, and the
intrinsic full kernel S=ker(N|A)=C[s,t]. The speed b belongs to S
cubed, its moving-frame determinant is nonzero, and the relative
curve has exact degree three with actual generic generation K[v],
where K=Frac(S).

Suppose the chosen constant ambient axis is null. The constant
coordinate change of [normal forms121](cubic-axis-scalar-normal-forms-pass121.md)
preserves the fact that x1,x2,x3,z are original polynomial
coordinates. The [null scalar theorem121](cubic-null-axis-scalar-constraint-pass121.md)
and [reciprocal exclusion121](cubic-null-axis-polynomial-speed-pass121.md)
leave only

\[
\begin{gathered}
b=(g,P,Y)^t\in S^3,\quad Y\ne0,\quad h=P/Y,\quad
2gY+D(h)Y^2=-1,\\
D(h)=a_3h^3+a_2h^2+a_1h+a_0,
\quad a_i\in\mathbb C,\quad a_3\ne0,\\
L/\mathbb C(h)\text{ finite},\quad
\rho=aY+B_0/Y,\quad a\in L,\quad B_0\in\mathbb C,\\
x_{\rm tr}=b(u+\rho)+b_hv+b_YR,\qquad v,R\in A_K .
\end{gathered}
\tag{1}
\]

The derivations in the last line are the commuting rational base
derivatives already constructed in121. Neither h nor Y is assumed
to be a polynomial coordinate. In particular L is not replaced by
C(h), and v is not assumed to be a global N-normalized slice.

## 2. A relative element and one coefficient are global

The [global reconstruction lemma122](cubic-null-global-reconstruction-pass122.md)
proves the exact polynomial identities

\[
\begin{gathered}
2R=2Y^2x_1+(3a_3P^2+2a_2PY+a_1Y^2)x_2\\
\hspace{18mm}+(3+4gY+a_2P^2+2a_1PY+3a_0Y^2)x_3,
\qquad R\in A,\\
F_0:=aY^2=x_3-Yu-R-B_0\in S,\\
K_0:=P^3/Y=\frac{-1-2gY-a_2P^2-a_1PY-a_0Y^2}{a_3}\in S.
\end{gathered}
\tag{2}
\]

For completeness, solving the three rows of (1) first gives
2R=2Y squared x1+D'Y squared x2+[1+(D-hD')Y squared]x3.
The speed identity eliminates P cubed/Y from the last coefficient
and gives (2). Since its coefficients are in S and its coordinates
are original, R is polynomial; its already known E-invariance then
puts it in A. The element F0 lies both in A and in K. It is killed
by N, and the full N-kernel in A is S. This proves the contraction
in (2), which would be unjustified for a coefficient-only model.

## 3. Every speed divisor gives a constant coordinate residue

Y is not a nonzero complex constant. Otherwise the speed identity
would make g a polynomial in P, forcing the speed's two base
derivatives to be dependent and its determinant to vanish. Choose
an irreducible polynomial p dividing Y in S. Equation (2) implies
p divides P, and then gives

\[
\overline{K_0}=-1/a_3,\qquad
\nu_p(Y)=3\nu_p(P)>0,\qquad
\nu_p(h)=-2\nu_p(P)<0,\qquad
\frac{a}{h^3}=\frac{F_0}{K_0}\in L\cap S_{(p)} .
\tag{3}
\]

The finite-place lemma in the reconstruction note proves that the
last element has complex residue. Here is the entire field argument:
choose a nonzero polynomial relation over C(h), divide all its
coefficients by one of minimum p-valuation, and reduce. Rational
functions of h regular at this pole have complex residues. At least
one normalized coefficient is one, so the reduction is a nonzero
polynomial over C satisfied by the element's residue. Since C is
algebraically closed, that residue is complex. This is also consistent
with the standard finiteness of residue fields in finite extensions
of discrete valuation fields.[^1]

Multiplying by the nonzero complex residue of K0 gives F0 congruent
to a constant c0 modulo pS. This is an assertion in S/(p), not just
after localization, because S/(p) injects into its fraction field.
Reduce the first two identities of (2) in the original ambient ring:

\[
2\overline R=3\overline{x_3},\qquad
\overline{x_3}-\overline R=c_0+B_0,\qquad
\overline{x_3}=-2(c_0+B_0)\in\mathbb C .
\tag{4}
\]

No coefficient of a generic relative Jacobian was required to be a
complex constant. The argument uses only the exact global row and
the coefficient-field residue at a pole of h.

## 4. Original-coordinate irreducibility is decisive

Put c=-2(c0+B0). Equation (4) says p divides x3-c in B. The
polynomial x3-c is irreducible in B because x3 is one of its
original polynomial coordinates. The nonconstant p is a nonunit
in B, whose only units are C*. Therefore p and x3-c are associates:

\[
x_3-c=\lambda p,\quad\lambda\in\mathbb C^*,\qquad
E(x_3-c)=Y\ne0,\qquad E(\lambda p)=0 .
\tag{5}
\]

The last equality uses p in S, which E kills. This is a contradiction.
It is a global polynomial argument; the nonzero polynomial Y is not
set to zero before applying E in (5).

Thus the null cubic scalar is excluded. Together with the null
reciprocal exclusion121, this rules out the entire null-axis
alternative under the stated actual cubic hypotheses. If an actual
frame offered more than one constant axis and any one were null,
that selected axis would give the same contradiction.

## 5. Scope and verification

The proof needs actual original-coordinate generation and the full
invariant-kernel contraction. The polynomial null speed control121
did not supply those hypotheses and is not a counterexample. It now
serves as a concrete family that cannot extend to the supplied actual
exact cubic frame. The same conclusion was not available from its
speed identities alone.

The separate reconstruction checker verifies the finite row and
denominator-elimination identities. The finite-place lemma and
the coordinate-prime contradiction above are written arguments,
not assertions inferred from tests. Independent AI reconstruction
is not human expert review, formal proof checking or novelty clearance.
The non-null alternative and arbitrary-frame entry remain unresolved.
Files through121 remain unchanged.

## Sources

[^1]: The Stacks Project, [Lemma 15.113.2, tag 09E5](https://stacks.math.columbia.edu/tag/09E5),
    finiteness of the residue-field extension for a finite extension
    of discrete valuation fields. The elementary normalized-polynomial
    proof above is included so this application does not depend on
    an unexpanded residue-field assertion. This source is not a
    cancellation theorem or a novelty claim for the null-axis argument.
