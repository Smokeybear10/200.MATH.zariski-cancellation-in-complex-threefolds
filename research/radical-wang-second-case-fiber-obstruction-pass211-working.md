# A fiber-contraction obstruction to the remaining Wang second case

Status: working original-ring obstruction. This note isolates the
denominator and parity argument used in the proposed affine-pair
recognition. It proves the stated conditional obstruction, not that an
arbitrary cancellation problem has been reduced to its hypotheses.

## 1. A polynomial subring with no hidden X-denominators

Let
\[
B=\mathbb C[X,Y,Z,W],\qquad
F=X^2Z-W^2+2dXY,\quad d\in\mathbb C .
\tag{1}
\]
The four displayed generators are actual independent polynomial
coordinates. Then
\[
\boxed{\mathbb C(X)[F]\cap B=\mathbb C[X,F].}
\tag{2}
\]
The intersection is taken in \(\operatorname{Frac}B\).
This is a polynomial-in-\(F\) assertion, not an assertion about all
rational functions in \(X,F\).

First \(X,F\) are algebraically independent, since \(F\) has positive
degree in \(Z\) over \(\mathbb C(X,Y,W)\).
For each \(c\in\mathbb C\), the specialization
\[
F_c=c^2Z-W^2+2dcY
\tag{3}
\]
is transcendental over \(\mathbb C\) in \(B/(X-c)\).
For \(c\ne0\) it has nonzero coefficient \(c^2\) of \(Z\);
for \(c=0\) it is \(-W^2\).
Consequently the map
\(\mathbb C[T]\longrightarrow B/(X-c)\), \(T\mapsto F_c\),
is injective.

Take \(b\in\mathbb C(X)[F]\cap B\). It has an expression
\(b=H(X,F)/q(X)\), with \(H\in\mathbb C[X,T]\) and nonzero
\(q\in\mathbb C[X]\).
If \(X-c\) divides \(q\), reducing \(q(X)b=H(X,F)\) modulo \(X-c\)
gives \(H(c,F_c)=0\).
Injectivity forces the polynomial \(H(c,T)\) to vanish, so
\(X-c\) divides \(H\) in \(\mathbb C[X,T]\).
Cancel the common factor before evaluation.
Every nonconstant factor of \(q\) is linear over \(\mathbb C\);
repeating, including multiplicities, removes the whole denominator.
Thus \(b\in\mathbb C[X,F]\). The reverse inclusion is immediate.
This proves (2) at every fiber, including the nonsmooth fiber at zero.

## 2. The actual derivation obstruction

Suppose \(E\) is a locally nilpotent derivation of \(B\) with
\(EX\ne0\), and \(D\) is a polynomial derivation of \(B\) satisfying
\[
DX=DF=0,\qquad DW=X\tau,\qquad
0\ne\tau\in B\cap\ker E,\qquad
DY,\ DW\in\mathbb C(X)[F].
\tag{4}
\]
No slice or local nilpotence for \(D\) is needed in this lemma.
These hypotheses are impossible.

Put \(b=DY\in B\).
Since \(\tau=DW/X\) lies both in \(B\) and in \(\mathbb C(X)[F]\),
equation (2) gives
\[
b=B_0(X,F),\qquad \tau=T_0(X,F),
\qquad B_0,T_0\in\mathbb C[X,T].
\tag{5}
\]
Differentiate the actual polynomial \(F\) using (4), and cancel
the nonzero polynomial \(X\) in the domain \(B\). The result is
\[
X\,DZ=2\tau W-2d b .
\tag{6}
\]
Modulo \(X\), one has \(F=-W^2\); hence
\[
T_0(0,-W^2)W=d\,B_0(0,-W^2)
\quad\text{in }\mathbb C[Y,Z,W].
\tag{7}
\]
The left side is odd in \(W\) and the right side is even.
Subtract the identity with \(W\) replaced by \(-W\).
Characteristic zero and the domain property give
\(T_0(0,-W^2)=0\).
The substitution \(\mathbb C[T]\to\mathbb C[W]\),
\(T\mapsto-W^2\), is injective, so \(T_0(0,T)=0\).
Therefore \(X\mid T_0(X,T)\), and (5) implies \(X\mid\tau\) in \(B\).

The kernel of an LND on a characteristic-zero domain is factorially
closed. For completeness, LND degree is additive on a nonzero product:
the highest surviving derivative is the product of the two highest
derivatives times a nonzero binomial coefficient. Since
\(\tau=X(\tau/X)\ne0\) has E-degree zero, \(X\) has E-degree zero.
This contradicts \(EX\ne0\), proving the obstruction.

## 3. Exact intended application and its remaining prerequisite

For a normalized actual affine-pair chart, the intended primitive
auxiliary derivation has
\[
DY=b,\quad DW=X\tau,\quad DF=0,\qquad
V=F/X^2+q_0(X),\quad q_0\in\mathbb C(X).
\tag{8}
\]
If the generic Wang second case gives
\(DY,DW\in\mathbb C(X)[V]\), its coefficient ring is exactly
\(\mathbb C(X)[F]\), as required in (4).
Actual regularity and E-invariance of \(\tau\), and the actual
coordinate normalizations leading to (8), must be proved before
using this lemma. They do not follow from a generic field description.

In that application, a common scalar \(\tau\) initially in
\(\operatorname{Frac}B\) can be returned to \(B\) if the exact
identity \(D^2Z=2\tau^2\in B\) is available: \(\tau\) is integral
over the normal polynomial ring. Its E-invariance still needs the
commuting-action and primitive-division argument.
This is a sufficient route to a hypothesis, not an assumption that
every generic derivation has polynomial coefficients.

The proof above is elementary and independent of the source of the
Wang classification. Its use in a complete recognition theorem is
separate. The denominator contraction and parity argument have
independent AI outline reconstructions; saved-source review and
finite formula checks are not human expert or formal certification.
No unrestricted cancellation, arbitrary entry, or novelty is claimed.
