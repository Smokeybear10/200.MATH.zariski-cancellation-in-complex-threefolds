# Fixed-fiber multiplicity and the remaining recognition problem

The restricted investigation now bounds the total multiplicity of
every closed quotient fiber, not just its individual components.
This rules out every generically rank-zero component in the
quadratic branch. In the cubic branch, it leaves a short list of
possible multiplicity profiles. A collapsed component also has a
rigid embedding: its cylinder is an actual affine plane in the
original four coordinates.

The full cancellation problem is not solved. These deductions
require a special original-coordinate frame whose existence has
not been established for an arbitrary cancellation instance.
Even within that frame, rank-one fixed components and several
cubic configurations remain unresolved.

## 1. The full question and the restricted setting

The working interpretation of Luo's email remains
\[
A[s]\simeq_{\mathbb C}\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq_{\mathbb C}\mathbb C^{[3]}.
\tag{1}
\]
The intended correction, field and dimension have not been
confirmed by Luo. The literal conclusion that X is an affine
line is dimensionally incorrect for general r. Equation (1)
is the full working target, not a theorem established here.

The current branch has an actual locally nilpotent derivation E
in original polynomial coordinates, with
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,
\quad E^2x_i=0,\quad E^2z=q\in\mathbb C^*,\quad u=Ez/q,\\
S=\mathbb C[s_1,s_2]\subset A,\qquad
R=S[A_1,A_2],\quad A=R[c],\quad A_K=K[v],\quad K=\operatorname{Frac}S,\\
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0,
\quad b=(Ex_1,Ex_2,Ex_3)^t\in S^3,\\
N(f)=\det\frac{\partial(s_1,s_2,u,f)}{\partial(x_1,x_2,x_3,z)},
\quad\ker(N|_A)=S,\quad N\text{ primitive},\quad d\in\{2,3\}.
\end{gathered}
\tag{2}
\]
The plane, completion and N are those constructed from the
actual frame, not freely chosen commuting actions. The parameter d
is the degree of the irreducible relative equation of R and the
maximum generic v-degree of its two generators. The degree-one
branch was recognized in pass91. The constant nonzero Omega branch
was recognized in pass90.

The cylinder makes A smooth, factorial and contractible. The
retained quotient theorem gives a faithfully flat map to the
invariant plane with nonempty pure curve fibers. The exact
Jacobian field is free away from Omega=0; its remaining fixed
set maps to finitely many closed base points. These are the
starting conclusions of the [pass91 synthesis](nonconical-exceptional-fiber-frontier-pass91.md).

## 2. The fixed scheme is a curve, including its nilpotents

The [fixed-scheme proof](nonconical-fixed-scheme-structure-pass92.md)
identifies the local value ideal of N with the two-by-two minors
of the two quotient differential rows. Primitivity prevents a
common height-one factor. A direct fraction-field syzygy argument,
followed by height-one denominator descent, gives an exact free
resolution. The depth lemma then shows that the fixed scheme,
if nonempty, is pure one-dimensional and Cohen--Macaulay.[^depth]

There are no isolated fixed components or embedded point
components. Every reduced fixed component is an entire component
of a closed quotient fiber. At a point where the quotient
differential has rank one, its fixed ideal is a two-generator
local complete intersection. None of this removes the fixed
curve or makes it reduced.

For a fixed component with generic prime \(\mathfrak q\), put
\(\mu=\operatorname{length}_{A_{\mathfrak q}}
(A_{\mathfrak q}/mA_{\mathfrak q})\). The primitive-fiber theorem54
gives \(\mu\ge2\): the action is nonzero on this whole Artinian
fiber although it is zero on the reduced fixed curve. This is
why a calculation only on ordinary points would lose essential
information.

## 3. A degree bound for the total fiber

The actual volume identities give \(\deg_v c\le2d\), in
addition to \(\deg_v A_i\le d\). For any individual component,
choose a generator U with nonconstant residue. The local map
\((S[U])_{mS[U]}\to A_{\mathfrak q}\) is flat by miracle
flatness. Its generic field extension has degree \(\deg_v U\).
Lifting a basis of its Artinian closed fiber and taking the
least-order initial form of a hypothetical relation proves that
these lifts are generically independent. This does not require
the local extension to be finite.[^flat]

The [total-fiber proof](nonconical-total-fiber-multiplicity-pass92.md)
chooses one complex linear combination U of \(A_1,A_2,c\)
which is nonconstant on every component. It then makes the
same argument over the semilocalization at all their generic
primes. Target-local flatness and the Artinian product
decomposition give
\[
\boxed{\qquad
\sum_i\mu_i[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)]
\le\deg_v U\le2d,
\qquad\sum_i\mu_i\le2d.
\qquad}
\tag{3}
\]
This sum includes nonfixed components as well as fixed ones.
If a particular component has a nonconstant \(\bar A_i\),
its individual multiplicity is at most d. If both quotient
differentials vanish generically in the ambient cotangent
space, the two fiber parameters lie in the square of the
maximal ideal of a regular local surface. Two such parameters
cannot give a quotient of length three, so that component has
multiplicity at least four. Both relative generators must then
be constant on it, and its reduced ring is \(\mathbb C[\bar c]\).

## 4. A genuine exclusion, with its remaining cases

The earlier integral ramification argument applies to the unknown
threefold because the cylinder supplies its exact smoothness and
homology hypotheses. The source applicability was already recorded
in pass46, not discovered anew here. On a fully retained
exceptional curve, the actual divisor constant-field degrees from
pass91 are at most d. For a whole irreducible reduced fiber,
the integral support lattice forces its multiplicity to be the
product of pairwise coprime retained branch degrees. The
[ramification note](nonconical-irreducible-fiber-ramification-pass92.md)
reconstructs this argument and checks its source scope.[^kaliman]

In degree two, a generically rank-zero component has multiplicity
four by the local bound. It exhausts the total bound (3), so
there can be no other component. But the irreducible-fiber
ramification calculation permits only multiplicity two. This
contradiction proves the quadratic exclusion below.
\[
\begin{array}{c|l}
d&\text{remaining generically rank-zero possibilities}\\ \hline
2&\text{none}\\
3&\mu=6\text{ alone; or }\mu=5\text{ with one multiplicity-one component;}\\
 &\mu=4\text{ with other components of total multiplicity one or two.}
\end{array}
\tag{4}
\]
There is at most one generically rank-zero component in each
cubic fiber. In the multiplicity-six case, the retained branches
have degrees two and three and belong to distinct components of
the exceptional base curve. These conditions do not prove that
any listed configuration exists, or that either branch is smooth.

Generic rank is important. Equation (4) does not exclude an
isolated rank drop on a generically rank-one fixed curve. It also
does not eliminate rank-one fixed curves, which remain a principal
obstacle even in relative degree two.

## 5. The actual embedding of a collapsed component

When \(\bar A_1,\bar A_2\) are constant on a component, the
universal generator pencil says that \(h\otimes1-1\otimes h\)
is nilpotent in \(A\otimes_R A\). Evaluate this tensor ring
on two copies of its reduced component \(\mathbb C[\bar c]\).
The target is the domain \(\mathbb C[c_1,c_2]\), so
\(\bar h(c_1)=\bar h(c_2)\) and \(\bar h\) is constant.

Substituting into the original coordinate reconstruction shows
that the cylinder of the component is exactly an affine plane.
The [plane proof](nonconical-collapsed-component-plane-pass92.md)
constructs affine-linear good coordinates X,Y,W with
\[
\begin{gathered}
\mathfrak qB=(X,Y),\qquad B/\mathfrak qB=\mathbb C[W,z],
\qquad \bar E=\partial_W+qW\partial_z,
\qquad\bar T=\partial_z,\quad T=\partial_z\text{ originally};\\
\text{at generic quotient rank zero:}\quad
mB\subset(X,Y)^2,\quad
\operatorname{rank}(J\bmod(X,Y))=1,\quad J^2\equiv0\bmod(X,Y),
\end{gathered}
\tag{5}
\]
where J is the original velocity Jacobian. The rank-one assertion
holds everywhere on that plane, following from the generic
rank-zero assumption for the quotient map. These are different
matrices and different rank statements.

The plane is stable under both E and T, and their commutator
vanishes on its quotient. Stability of this codimension-two ideal
does not furnish a common invariant function or a stable principal
divisor. It therefore does not contradict the already proved
absence of a nonconstant common rational invariant.

## 6. Verification and the next mathematical work

The [exact control](fixed-scheme-artin-controls-pass92.md) checks
Artinian complete intersections of lengths four, five and six,
and distinguishes whole-fiber multiplicity from fixed-scheme
thickness in a triangular polynomial family. Both unittest
methods pass in the [recorded capture](verification-pass92-working.json).
They verify those finite algebra calculations, not the universal
flatness, topology or recognition arguments. The written proofs
received separate AI reconstructions, whose scopes are recorded
in the [proof audit](proof-audits-pass92-working.md).

The next bounded mathematical tasks are to exploit the exact
plane constraint and total-length bound against the remaining
cubic profiles, and to analyze rank-one fixed components in
degree two. The old quintic-generation obstruction54 has extra
filtration and zero-first-jet hypotheses; the new plane condition
does not by itself supply those hypotheses. The formal first-jet
Jordan checks likewise have not produced an actual inverse frame.

Separately, a proof for an arbitrary sliced action must still
construct an admissible frame or use another route entirely.
The general target (1) remains active and unproved. Human expert
review, formal proof verification and historical novelty checks
remain outstanding. No submission, public claim or external
contact has been made. The [checkpoint](checkpoint-pass92-working.json)
preserves this restricted progress without redefining the goal.

[^depth]: The Stacks Project, [00LX](https://stacks.math.columbia.edu/tag/00LX),
    [00LK](https://stacks.math.columbia.edu/tag/00LK) and
    [00NQ](https://stacks.math.columbia.edu/tag/00NQ). Exact local
    resolution and scope are in fixed-scheme92.

[^flat]: The Stacks Project, [00R4](https://stacks.math.columbia.edu/tag/00R4),
    [00NN](https://stacks.math.columbia.edu/tag/00NN) and
    [00HT(7)](https://stacks.math.columbia.edu/tag/00HT).
    The local and semilocal applications are proved in the linked
    multiplicity notes, including all contraction and residue-field checks.

[^kaliman]: Shulim Kaliman,
    [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
    final author version, Notation 2.3, Proposition 3.2 and Theorem 5.2(i).
    The source supplies the retained quotient construction. The
    integer-lattice and total-length combination is a separate
    written derivation, not a quoted cancellation theorem.
