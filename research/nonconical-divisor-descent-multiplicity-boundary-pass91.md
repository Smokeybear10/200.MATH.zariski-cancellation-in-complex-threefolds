# Divisor descent and a precise multiplicity boundary

The actual noncollapse theorem gives exact descent across a base
divisor whenever the entire smaller-ring fiber is a domain.
It does not give that domain hypothesis. A modified presentation of
the retained Weitzenbock example separates this missing premise
from factoriality, a primitive commuting LND, the universal pencil,
and even an actual quadratic coordinate on a polynomial cylinder.

## 1. Exact descent when the whole smaller-ring fiber is integral

Let V be a DVR with uniformizer p, fraction field K, and residue
field k. Suppose \(R_0\subset A_0\) are V-domains satisfying
\[
\begin{gathered}
(R_0)_K=(A_0)_K,\qquad A_0/pA_0\text{ is a nonzero domain},\\
R_0/pR_0\text{ is a finitely generated one-dimensional k-domain},\\
\operatorname{trdeg}_k
\operatorname{im}(R_0/pR_0\longrightarrow A_0/pA_0)=1.
\end{gathered}
\tag{1}
\]
The kernel of the displayed fiber map is prime. If it were
nonzero, the image of the one-dimensional finitely generated
k-domain would have dimension zero, contrary to its stated
transcendence degree. Thus the map is injective, or equivalently
\(pA_0\cap R_0=pR_0\).

For any \(a\in A_0\), generic equality supplies
\(p^na=r\in R_0\) for some \(n\ge0\); denominators in V are
units times powers of p. If \(n>0\), then
\(r\in pA_0\cap R_0=pR_0\), so \(r=pr_1\) with \(r_1\in R_0\).
Cancellation in the domain gives \(p^{n-1}a=r_1\). Iterating,
\[
\boxed{\quad R_0=A_0.\quad}
\tag{2}
\]
No finiteness of \(R_0\to A_0\) or normality assertion was used.

In the actual nonconical setting take \(V=S_{(p)}\),
\(R_0=R_V\), and \(A_0=A_V\). Generic equality comes from
[quadratic-potential90](nonconical-quadratic-potential-pass90.md);
the domain property of the A-fiber and noncollapse of the image
come from [cyclic-fiber90](nonconical-cyclic-fiber-omission-pass90.md).
Thus only the full \(R_V/pR_V\) domain premise in (1) is extra.

For a primitive graph presentation
\(R_V=V[Y,Z]/(aZ-P(Y))\), this extra premise holds if a is a
unit, and also if \(p\mid a\) and \(\overline P\) is irreducible
over k. In the latter case the full fiber is
\((k[Y]/(\overline P))[Z]\).
It fails when only one factor is selected or a repeated factor
is removed. The image of that fiber in A is not a substitute
for the full fiber in (1).

## 2. A polynomial threefold with a different two-generator presentation

Use the retained Weitzenbock quotient, but change its relative
generators:
\[
\begin{gathered}
A=\mathbb C[p,y,z],\qquad
S=\mathbb C[p,\eta]\subset A,\qquad \eta=pz-y^2,\\
N=p\,\partial_y+2y\,\partial_z,\qquad
R=S[Y_0,Z_0]\subset A,\qquad Y_0=py,\quad Z_0=z,\\
R\simeq S[Y,Z]/(p^3Z-Y^2-p^2\eta),\qquad
A=R[y],\qquad A_p=R_p .
\end{gathered}
\tag{3}
\]
The displayed relation is primitive and irreducible: over
\(\operatorname{Frac}(S)\) it is linear in Z, and its coefficient
content in \(S[Y]\) is one. It is the exact kernel, as is also
seen after inverting p, when \(y=Y/p\).
Moreover y is integral over R through
\(y^2=pz-\eta\). Hence A is the finite normalization of R:
it is normal, integral over R, and has the same fraction field.

The ring A is a polynomial UFD with constant units, and p is
prime in A. The derivation N is locally nilpotent and primitive;
its nonzero coefficients p and \(2y\) have gcd one.
Its kernel is exactly S. For example,
\(A_p=S_p[y]\), with \(Ny=p\). Thus the kernel there is \(S_p\);
the intersection \(A\cap S_p=S\) follows by clearing powers
of p and using the injective reduction
\(\mathbb C[\eta]\to A/pA,\ \eta\mapsto-y^2\).

The quotient map \(S\to A\) is faithfully flat. Its closed fibers
are defined by \(p=\alpha\), \(\alpha z-y^2=\beta\).
For \(\alpha\ne0\) they are lines; for \(\alpha=0\) they are
two lines or a doubled line, always nonempty and purely
one-dimensional. The smooth source and regular two-dimensional
base give flatness by the retained miracle-flatness argument.
These quotient facts are the ones explicitly checked in
[intrinsic-quotient](intrinsic-quotient-surface-pass.md), not a
new claim that all fibers are reduced.

Set \(c=y\) and \(h=0\). The universal generator pencil holds
exactly and the tensor difference of h is zero:
\[
A[\tau]=R[\tau,c+\tau h]=R[\tau,y],\qquad
h\otimes1-1\otimes h=0\text{ in }A\otimes_R A.
\tag{4}
\]
This is an algebra-only instance of those pencil identities;
it does not identify R with a completed original good-coordinate
ring.

## 3. The whole divisor fibers exhibit the missing premise

Take \(V=S_{(p)}\) and \(k=\mathbb C(\eta)\). The two whole
fibers, and the image of the smaller one, are
\[
\begin{gathered}
R_V/pR_V=k[Y,Z]/(Y^2),\\
A_V/pA_V=
\bigl(k[y]/(y^2+\eta)\bigr)[z]=k'[z],
\qquad [k':k]=2,\\
Y\longmapsto0,\quad Z\longmapsto z,\qquad
\operatorname{im}(R_V/pR_V\to A_V/pA_V)=k[z].
\end{gathered}
\tag{5}
\]
The polynomial \(y^2+\eta\) is irreducible over k: a square in
\(\mathbb C(\eta)\) cannot have odd valuation at \(\eta=0\).
Thus the whole A-fiber is a domain and the image of R has
transcendence degree one, just as in the actual noncollapse
conclusion. Nevertheless the full R-fiber is nonreduced.
The element \(\overline y\) is not in \(k[z]\), so \(y\notin R_V\)
and \(A_V\ne R_V\).

The induced N on (5) sends z to the nonzero field element
\(2\overline y\), so it is a nonzero translation on \(k'[z]\).
It therefore also satisfies the precise whole-divisor conclusion
of the primitive-LND argument, including its allowance of a
nontrivial finite constant field.

## 4. An actual quadratic coordinate does not supply the missing frame

On the genuine polynomial cylinder \(B=A[u]\) take
\(E=\partial_u\). Then E and N commute. The tuple
\((u,p,z,w)\), where \(w=y+u^2\), is a polynomial coordinate
system with the explicit inverse \(y=w-u^2\).
In these original coordinates E has coefficients
\((1,0,0,2u)\), so the first three coordinates have zero second
E-derivative and \(E^2w=2\).

This is not the actual nonconical highest-field setup. Its good
speed row is constant, and its nonzero highest adjoint is a
multiple of \(\partial_w\), whose intrinsic kernel is
\(\mathbb C[p,z]\), not the chosen S in (3).
Nor does substituting the chosen generator py into the good
tuple repair the issue:
\[
\det
\frac{\partial(u,py,z,y+u^2)}{\partial(u,p,y,z)}
=-y\notin B^* .
\tag{6}
\]
This candidate tuple is not a polynomial coordinate system.
The determinant is a rejection test, not an inverse inferred
from a constant Jacobian.

Thus the control retains a polynomial A and cylinder, an actual
quadratic coordinate, a primitive commuting LND with plane
kernel, faithful flatness, the exact generator pencil, and
whole-divisor noncollapse. It does not retain the indispensable
identification of that LND, plane and two-generator ring with
the original nonconical highest-adjoint reconstruction.
It is not a counterexample to the remaining actual-frame
recognition problem.

General supplied the DVR descent argument and the changed
Weitzenbock presentation; Root requested this bounded saved
control. The underlying Weitzenbock quotient is retained
earlier work, not a new family or novelty claim. No new
external theorem is added. All pass90 and earlier files are
unchanged.

The separate
[one-method exact checker](nonconical_multiplicity_boundary_checks_pass91.py)
checks this presentation, the nonreduced fiber relation and
translation unit, both genuine coordinate inverse orders,
the commuting fields, and the failed candidate determinant.
It does not numerically prove (1)--(2), faithful flatness,
normalization, or an original nonconical-frame realization.
The author read the saved proof and checker through EOF.
The first checker run passed its one method in 0.026 seconds
with exit zero (execution chunk 63d239); this is not a full
regression run or a formal proof certificate.
