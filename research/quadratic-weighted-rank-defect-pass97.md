# Every total-three quadratic fiber has an exact projection-rank defect

In any quadratic fiber of total multiplicity three, every admissible
complex linear combination U of the actual relative generators
A_1,A_2,c has generic degree four but whole closed-fiber degree
three. Its flat semilocal base change is not finite. Thus the
finite-normalization balance that excluded total four cannot be
reapplied by simply assuming finiteness in this remaining case.

There is nevertheless new geometry: all three relative generators
restrict affinely to every reduced component. In the surviving
(2,1) case, a constant affine combination of A_1,A_2 separates
the two reduced components. This is not an invariant ambient
coordinate or a recognition theorem.

## 1. Weighted saturation and the exact gcd identity

Retain the actual quotient and source hypotheses of
[source-balance97](quadratic-saturated-source-balance-pass97.md).
For an actual f in A nonconstant on every component of a closed
fiber, put
\[
\begin{gathered}
n=\deg_v f=[\operatorname{Frac}A:K(f)],\qquad
d_i=[\kappa(\mathfrak q_i):\mathbb C(\bar f_i)],\\
\sum_i\mu_i d_i\le n,\qquad
T_f=(S[f])_{\mathfrak mS[f]},\qquad
L_f=\mathbb C(f).
\end{gathered}
\tag{1}
\]
The reduced components are entire affine lines by96, so d_i is
the positive polynomial degree of the residue of f on that line.
The projection bound and local flatness proof92 apply to any such
actual f, not just to a linear combination of the chosen generators.

If equality holds in (1), the retained equality-in-flat-rank and
integral-localization arguments make the entire base change
D_f finite free of rank n over T_f. Its component residue fields
now have degrees d_i over L_f; they need not all equal L_f.
The prime-divisor field tower and label-survival proof in balance97
remain unchanged. For a normalized divisor branch over C_i, its
residue degree over L_f is d_i times its residue degree over
kappa(q_i). Equivalently a generic complex f-value cuts C_i at
d_i general points, each carrying the same actual Thom column.
Thus the correct weighted source balance is
\[
\begin{gathered}
\sum_i d_i(v_i)_a=n/N_j
\quad\text{for each normalized source point }a\text{ over branch }j,\\
N_j\mid n,\qquad
\boxed{\quad
\gcd_i d_i=\gcd_j(n/N_j),\qquad
n=\operatorname{lcm}_j(N_j)\,\gcd_i d_i .
\quad}
\end{gathered}
\tag{2}
\]
Here the same finite-normalization argument counts all branches;
it does not discard the residue extensions or assume normalization
commutes with a special fiber.

To prove the gcd equality, let g be the gcd of the balanced row
values n/N_j. The weighted vector v=sum_i d_i v_i is divisible
by g in the ambient integer group. Since g divides n, its quotient
still has diagonal image under the weighted ramification map and
belongs to the full supported lattice. The actual basis property
therefore forces g to divide every d_i. Conversely any common
divisor of the d_i divides every coordinate of v, hence divides g.
Finally gcd_j(n/N_j)=n/lcm_j(N_j). This proves (2), not merely
one divisibility. It is explicitly conditional on saturation.

## 2. No admissible function saturates a total-three fiber

Assume the whole fiber has total multiplicity three. Each normalized
cover degree is one or two, so their lcm is at most two. There is
at least one exceptional branch, since a total-three fiber cannot
lie in the product complement. No choice of a fully retained
exceptional curve is needed.

Suppose any admissible actual f saturated (1), and put
g=gcd_i(d_i). Equation (2) would give n at most 2g. On the other
hand n=sum_i(mu_i d_i) is at least 3g. This contradiction proves
\[
\boxed{\quad
\sum_i\mu_i d_i<n
\quad\text{for every actual }f\in A
\text{ nonconstant on every component.}\quad}
\tag{3}
\]
No bound on the generic degree of f is needed for this strict
inequality. The proof rules out weighted saturation, not the
fiber itself. Its finite-normalization argument is used only
under the contrary saturation hypothesis.

## 3. Exact defect for the actual linear projections

Now take any complex linear combination U of A_1,A_2,c that
is nonconstant on every component. Such combinations exist,
since finitely many proper linear subspaces are to be avoided.
Its generic degree is at most four. Since every d_i is positive,
(3) forces
\[
\begin{gathered}
\boxed{\quad
\deg_v U=4,\qquad d_i=1\text{ for every }i,\qquad
\deg_v U-\sum_i\mu_i d_i=1.
\quad}\\
\deg_v c=4.
\end{gathered}
\tag{4}
\]
Indeed sum_i(mu_i d_i) is at least three; its strict upper bound
is an integer at most four. This leaves only the displayed values.
Both good generators have generic degree at most two. Thus (4)
forces the coefficient of c in every admissible U to be nonzero,
and forces the degree of c itself to be four.

Let O' be the semilocal ring of A at all component generic
points, viewed over T_U. The same local regularity and associated
graded proof used92 gives
\[
\begin{gathered}
O'\text{ is flat over }T_U,\qquad
\dim_{K(U)}(O'\otimes_{T_U}K(U))=4,\\
\dim_{\mathbb C(U)}O'/\mathfrak mO'=3,\qquad
\boxed{\quad O'\text{ is not a finite }T_U\text{-module}.\quad}
\end{gathered}
\tag{5}
\]
If it were finite, flatness over the local ring T_U would make
it free of its generic rank four, contradicting the residue
dimension three. The entire indicated base change D_U is not
finite either: if finite over T_U, all its maximal ideals would
lie over the closed point and would be precisely the listed
component points. Its semilocalization would then already be
D_U=O', contradicting (5).

This is an exact failure of the finite-module hypothesis, not
merely an absent proof of it. The one-unit rank difference does
not by itself identify a missing geometric point or a canonical
compactification branch.

## 4. Relative straight lines and a separator in the (2,1) case

Write the residues of A_1,A_2,c on each C_i=A1_(t_i) as polynomials.
The degree of a generic linear combination is the maximum of
their degrees: cancellation of the highest coefficient imposes
a proper linear condition. One can avoid that condition and
the nonadmissible combinations simultaneously. Equation (4)
therefore gives, on every component,
\[
\bar A_1=\alpha_{1i}t_i+\beta_{1i},\qquad
\bar A_2=\alpha_{2i}t_i+\beta_{2i},\qquad
\bar c=\gamma_i t_i+\delta_i
\quad\text{on }C_i.
\tag{6}
\]
At least one slope is nonzero, since these residues generate
the component ring. Thus its actual relative image in the
three coordinates (A_1,A_2,c) is an affine line, not a nonlinear
polynomial embedding of an abstract affine line.

Now specialize to profile (2,1), calling the double component C_2
and the simple component C_1. The double component is collapsed
by96 and has a vertical relative line: its A_i are a constant
point p in the relative good plane, while c
is its parameter. If the simple component's good projection
is a line through p, its full relative line would meet this
vertical line. If that projection is the point p itself,
the two full lines would coincide. Both are impossible:
the actual generating presentation embeds the reduced fiber
in the relative three-space, and its components are disjoint.
Hence the simple good projection is a line avoiding p or
a different point. A constant affine linear form on that
plane consequently yields an actual function
\[
F=\lambda_0+\lambda_1A_1+\lambda_2A_2\in A,
\qquad F|_{C_2}=0,\qquad F|_{C_1}=1,
\qquad \deg_vF\le2.
\tag{7}
\]
This separates reduced components only. It is not constant
on the whole nonreduced thickening by assertion, is not
admissible for (1), and is not claimed to be an original
affine coordinate or a coordinate of A.

There is also an important original-coordinate limit. If
C_1 is noncollapsed, the component-degree bound applied to
the actual h gives only deg(h restricted to C_1) at most two,
not one. In constant affine good coordinates sigma,t,L_0
on its cylinder, the reconstruction can therefore have graph
z=bar c(t)+q sigma^2/2+q sigma H(t), with H quadratic.
This is a genuine triangular graph, possibly cubic, not an
affine-linear plane. If C_1 is collapsed, the earlier
collapsed-good-plane description applies instead. Neither
case supplies global action recognition.

## 5. A precise flat rank-defect control

The missing finite-module conclusion is a real algebraic
phenomenon even for regular local rings. Set
\[
\begin{gathered}
T_0=\mathbb C[x,z]_{(x,z)},\qquad
x=t^2(t-1)(t-2),\\
O_0=\mathbb C[t,z]_{\mathbb C[t,z]\setminus((t,z)\cup(t-1,z))},\\
\operatorname{rank}_{T_0}O_0=4,\qquad
O_0/(x,z)O_0\simeq\mathbb C[t]/(t^2)\times\mathbb C,\qquad
\dim_{\mathbb C}O_0/(x,z)O_0=3.
\end{gathered}
\tag{8}
\]
The polynomial t-equation is monic of degree four, so
C[t,z] is free of rank four over C[x,z]. The displayed
further localization is flat, regular and a domain. It
retains the double point t=0 and the simple point t=1,
while removing t=2. The residue calculation follows by
the Chinese remainder theorem. Its flat generic rank
four and residue dimension three prove it nonfinite over
T_0 exactly as in (5).

This is a semilocal algebra control, not an actual quotient
frame or a counterexample satisfying the source hypotheses.
In particular x does not remain prime in its polynomial
target. It demonstrates why flatness, regularity and finite
generic degree cannot replace the equality needed for
finite-module descent.

## Scope and provenance

The weighted row balance is the finite-normalization proof97
with all component residue degrees retained. Geometry, Root
and General independently reconstructed this extension and
the strict inequality. General supplied the exact gcd
equality refinement; Root noted the reduced-component
separation consequence and the extension to every total-three
fiber. No new primary-source theorem or numerical method is
used in the proof. The separate [arithmetic checker](quadratic_source_balance_checks_pass97.py)
tests finite degree tables, not these geometric conclusions.
The normalization and supported
homology dependencies are exactly those already recorded in
balance97 and96.

The result strengthens the geometry and identifies the exact
lost-rank gate for all total-three fibers, including (2,1).
It does not exclude (2,1), prove freeness, recognize A,
or reduce arbitrary sliced actions
to this frame. All files through96 are unchanged.
