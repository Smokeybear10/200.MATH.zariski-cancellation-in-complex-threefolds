# Full gradient and connected low-degree fibers

In the actual localized nonconical frame, the full formal gradient
is a unit ideal exactly when every closed fiber over the invariant
plane is connected. If a closed fiber is disconnected, its defining
polynomial is a squarefree product of two or three parallel affine
linear factors. This is a classification of the remaining localized
obstruction, not a proof that such fibers cannot occur in the actual
frame.

## 1. The actual smooth and free input

Retain the complete original-coordinate hypotheses and conclusions of
[quadratic-potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md) and
[open-free90](nonconical-open-free-derivation-pass90.md). Write
\[
\begin{gathered}
S=\mathbb C[s_1,s_2],\qquad S^\circ=S[1/\Omega],\qquad
\Omega\ne0,\qquad \mathscr P=S^\circ[Y,Z],\\
A^\circ=A_\Omega=\mathscr P/(F),\qquad
1\le\deg_{Y,Z}F\le3,\\
(F_Y,F_Z)A^\circ=A^\circ,\qquad
0\ne D\in\operatorname{LND}_{S^\circ}(A^\circ),\qquad
D(A^\circ)A^\circ=A^\circ .
\end{gathered}
\tag{1}
\]
The morphism \(\operatorname{Spec}A^\circ\to\operatorname{Spec}S^\circ\)
is faithfully flat and smooth with nonempty purely one-dimensional
fibers. The freeness in (1) is the actual unit image ideal obtained
from the original-coordinate conormal determinant. It is not inferred
from the generic action or assumed for an arbitrary plane equation.

For a closed point \(m\in\operatorname{Spec}S^\circ\), let
\(F_m\in\mathbb C[Y,Z]\) be the coefficient specialization.
The fiber algebra is exactly \(C_m=\mathbb C[Y,Z]/(F_m)\).
The nonempty curve-fiber statement excludes both a nonzero constant
\(F_m\) and \(F_m=0\). Its degree can drop from that of F.

## 2. Each fiber component is an embedded polynomial line

The smooth affine curve \(\operatorname{Spec}C_m\) is reduced.
Its irreducible components are disjoint: a point lying on two of
them would have a local ring with two minimal primes, whereas a
regular local ring is a domain. There are finitely many components,
so their coordinate rings \(C_{m,j}\) give a product decomposition.

Since D kills the base, it induces an LND on \(C_m\). A derivation
kills every idempotent: from \(e^2=e\) one gets
\((1-2e)D(e)=0\), and \((1-2e)^2=1\). Thus it acts separately
on each factor. The unit image ideal in (1) descends to each factor,
so every resulting derivation is nonzero.

For completeness, a nonzero LND \(\partial\) on a finitely generated
one-dimensional complex domain C has kernel \(\mathbb C\). The
local-slice theorem makes its invariant fraction field have
transcendence degree zero; any element of C algebraic over the
algebraically closed field \(\mathbb C\) is constant. If f has
positive \(\partial\)-degree n, then
\(\partial^n f\in\mathbb C^*\), and
\(v=\partial^{n-1}f/\partial^n f\) is an actual slice. The finite
slice expansion then gives \(C=\mathbb C[v]\). Consequently
\[
C_m\simeq\prod_{j=1}^{r_m}\mathbb C[v_j],\qquad
F_m=a_m\prod_{j=1}^{r_m} f_j,\qquad
a_m\in\mathbb C^*,\qquad
\sum_j\deg f_j=\deg F_m\le3 .
\tag{2}
\]
Here the \(f_j\) are distinct irreducible polynomials and
\(\mathbb C[Y,Z]/(f_j)\simeq\mathbb C[v_j]\). The absence of
repeated factors follows from smoothness, not from discarding the
nilradical of a general quotient fiber.

The elementary low-degree embedding argument in cubic-relation90,
Section 5, applies separately to each component. In detail, the
degrees of the two coordinate polynomials in \(v_j\) have maximum
\(\deg f_j\), by generic line intersection and the actual polynomial
inverse. Subtracting proportional leading terms leaves a degree-one
coordinate unless the degree pair is (2,3). The latter normalizes to
\(v^2,v(av^2+b)\): when \(b=0\) it has a common critical point,
and when \(b\ne0\) it identifies the two distinct points with
\(v^2=-b/a\). Both contradict polynomial recovery of v.
Thus there are linear coordinates \(L_j,M_j\) over \(\mathbb C\)
and a polynomial \(P_j\) such that
\[
f_j=c_j\bigl(M_j-P_j(L_j)\bigr),\qquad c_j\in\mathbb C^*.
\tag{3}
\]
This uses the degree-at-most-three embedding argument, not a
general unproved promotion of an abstract line quotient to an
ambient coordinate.

## 3. A disconnected fiber consists of parallel lines

Suppose \(r_m\ge2\). The only partition of degree at most three
that could include a nonlinear component is one quadratic component
and one line. By (3), the quadratic is a parabola parametrized by
\(L=v, M=P(v)\), with \(\deg P=2\).
Every affine line \(\alpha L+\beta M+\gamma=0\),
\((\alpha,\beta)\ne(0,0)\), meets it: substitution gives a
nonconstant quadratic if \(\beta\ne0\), or a nonconstant linear
polynomial otherwise. Such a polynomial has a complex root.
This contradicts the disjointness established above.

Hence all components are lines. Any two nonparallel complex affine
lines meet, so these lines have a common direction. There is a
nonzero linear form L, completable to linear coordinates L,M, with
\[
\boxed{\quad
r_m\in\{2,3\},\qquad
F_m=a_m P_m(L),\qquad
P_m(T)=\prod_{j=1}^{r_m}(T-\lambda_j),\quad
\lambda_i\ne\lambda_j\ (i\ne j).
\quad}
\tag{4}
\]
Conversely (4) gives precisely that disconnected smooth fiber.
The constants \(\lambda_j\) may absorb affine translations of
the parallel lines; L itself can be taken linear.

## 4. The exact formal critical scheme and the equivalence

If the fiber is connected, (2) has a single factor, and (3)
makes \(F_m\) a coordinate up to a nonzero scalar. In particular
its two partial derivatives generate \(\mathbb C[Y,Z]\).

For the disconnected form (4), the invertible linear change to
L,M instead gives the full critical scheme
\[
\begin{gathered}
\mathbb C[Y,Z]/((F_m)_Y,(F_m)_Z)
\simeq\mathbb C[L,M]/(P_m'(L)),\\
\gcd(P_m,P_m')=1,\qquad
P_m(L)\text{ is a unit in }\mathbb C[L,M]/(P_m'(L)).
\end{gathered}
\tag{5}
\]
It is nonempty, because \(\deg P_m'\ge1\). Its support is one
or two parallel lines, and it can be nonreduced in the cubic case.
For example \(P_m=T^3-1\) gives the ideal \((L^2)\), not
\((L)\). Formula (5) shows scheme-theoretically why this critical
locus misses the entire actual zero level.

The ring \(\mathscr P\) is a finitely generated complex algebra.
A proper ideal is therefore contained in a maximal ideal with complex
residue field, and its contraction to \(S^\circ\) is a closed
base point. Applying this observation to the formal gradient ideal,
then using the preceding classification, proves
\[
\boxed{\quad
(F_Y,F_Z)\mathscr P=\mathscr P
\quad\Longleftrightarrow\quad
\text{every closed fiber over }\operatorname{Spec}S^\circ
\text{ is connected}.
\quad}
\tag{6}
\]
In that event every such fiber is a single embedded polynomial line.
The generic-coordinate gate and the exact Bhatwadekar--Dutta criterion
in [source-gate91](low-degree-full-gradient-source-gate-pass91.md)
then give \(\mathscr P=S^\circ[F,G]\) and
\(A_\Omega=S^\circ[\overline G]\). Neither connectedness nor
this coordinate conclusion has been proved automatically here.
Even that localized conclusion would not remove \(\Omega=0\).

## 5. Relation to the remaining divisor problem

The separate [residue-degree theorem91](nonconical-residue-degree-bound-pass91.md)
treats whole generic divisor fibers, including divisors contained in
\(\Omega=0\), without identifying R and A there. The present proof
does not duplicate that extension. It concerns the actual smooth
two-generator presentation and free field on \(D(\Omega)\).

The quadratic localized Weitzenbock witness in source-gate91 has,
at \(x=0\) and \(\eta=\eta_0\ne0\), two distinct parallel
lines \(Y=\pm\sqrt{-\eta_0}\). It realizes exactly the alternative
in (4) among the abstract local properties. It has not been supplied
with the special original nonconical frame. No actual counterexample
to that frame, global kernel recognition, or cancellation conclusion
is asserted.

Geometry supplied the closed-fiber and critical-scheme argument.
The cited actual volume, low-degree embedding, and free-field proofs
were reread through EOF for their exact hypotheses. This note adds
no new external classification input or numerical method, and it does
not alter pass90 or earlier files.
