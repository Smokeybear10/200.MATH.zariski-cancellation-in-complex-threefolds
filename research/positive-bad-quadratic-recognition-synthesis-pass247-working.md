# Recognition for the supplied positive-rank quadratic weight-four sector

Under the actual globally sliced exact1122 hypotheses below, a full
principal weight-four initial kernel with nonzero quadratic part in
the two degree-two variables forces \(A\simeq\mathbb C^{[3]}\).
The new part of this synthesis closes the two repeated-root residual
models in the rank-one classification. The rank-two conclusion and
the surviving rank-one recognition cases are retained working inputs.

This is a restricted working theorem. There is no argument here that
an arbitrary cancellation instance admits the required coordinate
frame or initial kernel. The unrestricted complex-threefold
cancellation conjecture remains unsolved.

## 1. Exact statement and all frame assumptions

Let the named capital letters be actual polynomial coordinates, and
assume
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2 .
\end{gathered}                                                     \tag{1}
\]
Define the full weighted leading map by
\[
\begin{gathered}
\Theta:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow A[T],\\
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(aT,bT,eT^2,hT^2),\qquad \ker\Theta=(F),
\end{gathered}                                                     \tag{2}
\]
where \(T\) is independent. Require \(F\) to be irreducible and
homogeneous of weight four for weights \((1,1,2,2)\).
Write
\[
F=Q_2(\mathsf Z,\mathsf W)
 +P_2(\mathsf X,\mathsf Y)\mathsf Z
 +S_2(\mathsf X,\mathsf Y)\mathsf W
 +H_4(\mathsf X,\mathsf Y),\qquad \operatorname{rank}Q_2>0 .
\tag{3}
\]
The forms \(P_2,S_2,H_4\) may be zero. The rank is that of the
constant symmetric matrix of the binary quadratic \(Q_2\);
it is one or two.

**Working theorem.** Under (1)--(3),
\[
\boxed{A\simeq\mathbb C^{[3]}.}                                   \tag{4}
\]

The equality of the entire kernel in (2) is essential. One leading
relation does not give this theorem. The formal equation \(F=0\)
is not being asserted as an equation among the original polynomial
coordinates or as an invariant polynomial. No minimum among all
coordinate degree profiles is assumed or deduced.

## 2. The two residual repeated-root models cannot occur

First isolate the new exclusion used in the rank-one composition:
neither of the full initial kernels
\[
(Z^2-X^2W-XY^3),\qquad (Z^2-X^2W-Y^4)
\tag{5}
\]
can occur in an actual frame satisfying (1)--(2).
Here, as in the cited normal-form sources, the letters in a
displayed initial polynomial stand for its formal leading variables.

The actual exchange of the two quadratic slots in
[rebuilt237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md)
puts the two kernels into
\[
(X^2Z-W^2+XY^3),\qquad (X^2Z-W^2+Y^4).
\tag{6}
\]
Each literal new \(Z\) pivot is rebuilt from its actual frame.
The resulting exact coefficient field \(L\), nonzero selected
derivation \(N\), and generic line \(A_L=L[v]\) need not equal
their pre-exchange versions. The rebuilt leading ratio is
\(q=\rho^2-t^3\) or \(q=\rho^2-t^4\), respectively.

In both charts,237 excludes \(R=0\) and constant \(y\).
For zero return it uses a nonzero cubic coefficient followed by
the monic quadratic equation for \(w\). For a constant first
projection it constructs an actual auxiliary locally nilpotent
derivation, divides its original-ring gcd, and reaches an
original-ring unit contradiction. No coefficient-field unit is
silently promoted to an original-ring unit.

The [complete centered calculation239](radical-minus-polynomial-centered-eliminant-pass239-working.md)
retains every lower potential. In particular its center polynomial
has degree exactly three, and its full eliminant has no term
linear in the centered second formal variable. These statements
are stronger than its leading homogeneous form alone.

For the quartic chart, the local cofactor-order theorem in
[238](repeated-root-return-excess-order-bound-pass238-working.md)
excludes every projected degree except the quadratic graph
\((\deg_vy,\deg_v\theta)=(1,2)\).
The graph proof
[241](repeated-root-quartic-conic-exclusion-pass241-working.md)
then gives \(D_t=D/t\) and \(D_t=D/(6t)\) for \(D\ne0\).
Since \(t\ne0\) and the characteristic is zero, this excludes
the second kernel in (5).

For the cubic chart,
[frontier240](cubic-repeated-root-projection-frontier-pass240-working.md)
first reduces every nonconstant-return possibility to seven
degree pairs. The following separate written proofs exhaust them.

| Degree pair \((\deg_vy,\deg_v\theta)\) | Exclusion and essential final step |
| --- | --- |
| \((1,2)\) | [242](repeated-root-cubic-conic-exclusion-pass242-working.md): the correctly transformed scalar determinant is either nonconstant or zero. |
| \((1,3)\) | [244](repeated-root-cubic-graph-square-obstruction-pass244-working.md): explicit actual affine changes force a polynomial square of odd degree in an original coordinate. |
| \((2,3)\) | [245](cubic-repeated-root-two-three-conductor-exclusion-pass245-working.md): the exact parity conductor and whole-line module force an impossible order at the quadratic vertex. |
| \((2,4),(2,5)\) | [240](cubic-repeated-root-projection-frontier-pass240-working.md): exact norm/cofactor identities and the actual root-order test contradict the vertex multiplicity. |
| \((3,6)\) | [243](cubic-repeated-root-three-six-trace-exclusion-pass243-working.md): the monic cubic minimum has a nonzero linear coefficient, contradicting the complete centered identity. |
| \((4,6)\) | [246](cubic-repeated-root-four-six-conductor-trace-exclusion-pass246-working.md): the exact conductor bounds the polynomial form at infinity, whose third trace coefficient cannot vanish. |

The preliminary seven-pair list uses the pure leading form,
birationality, the exact conductor inclusion and the cubic center.
It does not assume the projected plane is normal.
The last row of the table proves the conductor formula by trace
duality, controls all four formal branches, and uses an exact
polynomial-part basis. It is not a numerical search over parametrizations.
Every pair is therefore excluded, proving the first kernel's
impossibility as well. This proves the exclusion (5).

## 3. Rank-one quadratic part

Use the precise finite-frontier statement of
[234](rank-one-bad-quadratic-four-model-frontier-pass234-working.md).
Under (1)--(2) with \(\operatorname{rank}Q_2=1\), it proves that
either \(A\simeq\mathbb C^{[3]}\) already by a retained recognition
theorem, or an actual homogeneous change of coordinates gives one
of the four full kernels
\[
\begin{gathered}
Z^2-XYW-X^4,\qquad Z^2-XYW-X^4-Y^4,\\
Z^2-X^2W-XY^3,\qquad Z^2-X^2W-Y^4 .
\end{gathered}                                                     \tag{7}
\]
The first two are excluded by
[236](rank-one-distinct-root-residue-exclusion-pass236-working.md),
and Section2 excludes the last two. Consequently only the
recognized alternative of234 can occur, proving (4) at rank one.

For clarity, the recognized alternative in234 is not empty by
definition or a claim inferred from generic rationality.
It explicitly invokes the retained recognition statements for
the absent-\(W\) case
[203](weight-four-absent-w-rank-one-recognition-synthesis-pass203-working.md)
and the pure radical case
[211](radical-initial-kernel-recognition-synthesis-pass211-working.md).
The zero-residue distinct-root model \(Z^2-XYW\) was separately
excluded by the complete product-radical chain ending in
[233](product-radical-conic-final-exclusion-pass233-working.md).
This note does not re-prove the historical dependencies of those
working theorems, invent a new realization, or expand their hypotheses.

The normalization in234 uses complex linear changes of the
degree-one slots, complex linear changes of the degree-two slots,
and quadratic translations of the latter. Their inverses are
polynomial. Each new coordinate is a nonzero homogeneous formal
polynomial of weight one or two. It cannot lie in \((F)\), whose
nonzero homogeneous terms have weight at least four. Therefore
its leading evaluation is nonzero, and its exact \(E\)-degree
does not drop. The invertible graded change transports the
entire kernel in (2).
Whenever a selected chart is used after a normalization, that
chart is rebuilt. The proof does not transfer an old return
condition through an unverified generic-field change.

## 4. Rank-two quadratic part

For \(\operatorname{rank}Q_2=2\), the complete retained recognition
statement is
[226](nondegenerate-bad-quadratic-recognition-synthesis-pass226-working.md).
Its assumptions are exactly (1)--(3) with that rank.
Actual homogeneous coordinate changes put the surviving full
initial kernel into \((ZW-X^4)\), and its retained fourth-power
recognition theorem gives \(A\simeq\mathbb C^{[3]}\).
The other binary-quartic root patterns were excluded there.
This proves (4) at rank two, and finishes the stated theorem.

The original-ring recognition in203,211,226 is supplied by their
explicit invariant-coordinate constructions and their cited
published regular-kernel endpoint. It is not a consequence of
the rationality of a projected curve or its normalization alone.
Those are retained theorem inputs to this composition, not newly
counted reconstructions of every earlier source.

## 5. What has and has not been achieved

The two residual models (5) are now excluded under the actual
supplied frame hypotheses. Composing that result with234 and226
recognizes the entire positive-quadratic-rank sector (1)--(3).
This is a theorem about a restricted hypothesis class, not a proof
that every sliced action lies in that class.

In particular, this result does not cover quadratic rank zero,
nonprincipal initial kernels, other leading weights or degree
profiles, or arbitrary coordinate entry. Some such cases have
separate retained partial results; none is silently included here.
The next bounded investigation can audit the zero-quadratic-rank
four-form classification184 and its existing branch results, while
the unrestricted entry gap remains explicit.

The new proofs237--246 and the exact statements of234,203,211,226
were read completely before this composition. A saved-source
review of a synthesis is not a new recursive verification of
every historical dependency. Complete review records, file hashes
and the sole canonical finite-check executions belong in the ledger.
Passing those algebra checks is not a machine-checked proof of
the whole theorem.

There is no human expert review, proof-assistant certification or
historical novelty clearance. No new nonempty family of examples,
publication-ready theorem or solution to unrestricted cancellation
is claimed. No external contact, public posting or submission has
occurred or is authorized by this note. The full research goal
remains active and unsolved.
