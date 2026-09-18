# Pass67: completed proof reconstructions and verification scope

This working record distinguishes author self-review, independent
full-file review, outline reconstruction, and finite computation.
All named reviewers are AI agents. This is not a proof-assistant
certificate or a human referee report.

The two new closure proofs recognize the dependent and independent
constant-top cubic sectors under the supplied actual coordinate
frame. Together with the frozen low-flow theorem and the previously
recognized constant defect relations, they cover constant \(E^3x\),
including zero. They do not supply a frame for every sliced action
or cover every nonconstant cubic top.

## 1. Completed full-file reviews

Root is the parent agent and independent graph proof's author.
General is general_affine17, the dependent proof's author.
Jet is jet_checker17, the actual control and checker author.
Geometry is geometry_audit17.

| Saved artifact | Author self-review | Completed independent full-file reviews reported |
| --- | --- | --- |
| [Dependent cubic closure](dependent-constant-cubic-closure-pass67.md), 19 equations | General | Jet, Geometry, Root |
| [Independent graph closure](independent-cubic-graph-closure-pass67.md), 23 equations | Root | Jet, General, Geometry |
| [Actual nonomission control](constant-cubic-nonomission-control-pass67.md), 15 equations | Jet | General, Root |
| [Actual control checker](constant_cubic_nonomission_checks_pass67.py), two methods | Jet | General, Root |
| [Formal graph checker](constant_cubic_graph_checks_pass67.py), one method | Jet | General, Geometry, Root |

These rows concern the complete saved mathematical text, not merely
earlier message outlines. General explicitly confirmed that its
complete reread of its own dependent note is author self-review,
not an independent audit. Geometry directly confirmed complete
EOF reads of both proofs and the formal graph checker. Geometry
explicitly did not claim an independent read or run of the other
new checker. No unreported Geometry review of the actual control
is inserted here.

Root initially requested that its independent full-file reviews
remain pending. It subsequently explicitly confirmed complete
EOF reads and reconstructions of both saved proofs, the full
actual control, both checker files, and the complete inherited
pass41 note. The table records that later confirmation.
Root's own saved-file reconstruction of its graph proof remains
author review, not a separate independent reviewer.

## 2. Dependent cubic reconstruction

Jet independently reread the complete frozen pass66 dependent
reduction and the complete pass41 one-good-output proof before
reconstructing the new saved closure through EOF. Root subsequently
confirmed the complete saved-proof reconstruction and full
pass41 reread. Geometry directly confirmed a full clean audit.

The checked gates include:

- Exhaustion of the frozen alternatives, including zero
  bad-acceleration and constant residual-curve endpoints.
- The exact identities involving
  \(\Delta=e_3q'-e_4p'\), \(\rho=ae_3+be_4\), and
  \(pq'-qp'\). All multiplicities of \(\Delta\) are retained;
  neither a coprime multiplier pair nor inversion of \(\rho\)
  is presumed.
- The sign in
  \(\beta=(\sigma-(pq'-qp')/\Delta)/2\), \(E\beta=1/2\),
  and \([E,T_e+\beta T_c]=0\).
- The deductions \(S\sigma=Su=0\), and only then
  \(S\beta=S\Delta(u)=0\). Actions on the actual coordinate
  generators and the fixed denominator establish a genuine
  localized LND. Commutation alone does not do this.
- Constant coordinate completion of the independent directions
  \(c,e\), with the actual good partial \(T_c\) retained.
  The one-good-output lemma is applied to its actual localized
  nice symmetry and the original slice, not to an assumed
  generic coordinate system.

The completed independent reviews reported no mathematical
correction. Earlier message reconstructions before the file was
saved were separate preliminary checks. There is no new
standalone finite suite for this written all-instance deduction.

## 3. Independent graph reconstruction

Jet's complete review reconstructed every displayed equation and
the actualness gates in the saved root proof. General and Geometry
directly confirmed their own complete clean reviews. Root
subsequently confirmed its full saved-file reconstruction.

The principal gates checked were:

1. Exact rational joint kernels follow from the previously proved
   actual polynomial kernels and the reduced-fraction argument
   for LNDs on the actual UFD.
2. Actual good-field identities determine the velocities.
   Integration of their joint-invariant potentials then gives
   the rational-coefficient polynomial graphs in the original
   bad coordinates \(X,Y\).
3. Actual coordinate generation proves
   \(B\otimes_{\mathbb C[t,f]}\mathbb C(t,f)
   =\mathbb C(t,f)[X,Y]\). Algebraic independence over this
   field follows at this stage, not earlier.
4. The true partials supply a polynomial inverse to the graph's
   good-coordinate derivative matrix. Its determinant is a field
   unit for this reason, not by a Jacobian-conjecture assertion.
5. The \(X^2\), \(XY\), and \(X\) determinant coefficients give
   the successive constant restrictions. The last restriction
   produces an actual coordinate slice.
6. The alternative \(l_0=0\) makes the entire second
   base-derivative row zero. For \(l_0\ne0\), the explicit
   triangular coordinate inverse and the ordinary slice theorem
   identify the original kernel with a polynomial three-ring.

The final opening clarification \(A=\ker E\) was read and is
notation only. No mathematical correction was requested.
The formal checker verifies selected coefficient identities,
not the universal generation, rational-kernel, or coordinate
arguments above. No new external classification endpoint is
needed after the explicit coordinate slice is constructed.

## 4. Actual control and limitations

The control starts with \(E=\partial_s\) on
\(\mathbb C[t,y,z,s]\) and an explicit two-sided polynomial
coordinate inverse for every nonconstant polynomial \(G(t)\).
It has exact adjoint heights \((1,1,2,2)\), constant cubic top,
generically independent defects, and an explicitly polynomial
original kernel.

Its written kernel and coefficient calculations show that all
four ordinary derivatives of the curve parameter are
complex-linearly independent. One actual good partial fails to
preserve the common two-variable kernel, but a unique constant
good line preserves it. A constant recombination makes both
named good partials individually fail without eliminating
that line.

This refutes automatic omitted-direction and every-good-partial
preservation claims. It does not refute the existence of some
preserving good direction, realize an unresolved original
kernel, or constitute a cancellation counterexample.

General's independent EOF review reconstructed both inverse
orders, all columns, the kernel, gradient independence, and
the unique preserving line. Root subsequently confirmed its
complete note and checker read. Neither requested a correction.

## 5. Exact computations actually reported

There are two new mathematical suites with three new test
methods. Repeating a run does not add methods.

| Checker | Jet first run | General independent run | Geometry independent run | Root independent run |
| --- | --- | --- | --- | --- |
| Actual nonomission, two methods | 0.084 s | 0.082 s | Not claimed | 0.080 s |
| Formal graph, one method | 0.203 s | 0.205 s | 0.196 s | 0.198 s |

Every reported run in this table passed with exit zero. Times
are the reported unittest durations, not new estimates.

The actual-control suite checks identities with symbolic \(G(t)\)
and two inverse compositions for a specified nonconstant
polynomial \(G\). It checks all four columns, exact adjoint
bounds, and the gradient and preservation identities.

The formal graph suite checks arbitrary-function rational graph
algebra: the three determinant coefficients, both reductions
of \(Q_2\), the coordinate-slice numerator, and the entire-zero-row
alternative. Passing these identities does not assert that a
formal graph realizes an action. The actualness proof is
reviewed separately.

Both new checkers import only unittest and SymPy. Scratch algebra,
review reruns, runner-validation diagnostics, and packet
consistency checks are not additional mathematical methods.

## 6. Regression runner, actual capture, and count boundaries

The read-only [pass67 runner](run_regression_pass67.py) takes the
actual command list from the captured
[pass66 regression](verification-pass66-working.json).
Jet read the complete frozen pass66 runner and directly compared
all 130 captured commands with full60's list plus that runner's
four named additions. The comparison was exact. The parsed
command list has no duplicates.

The count is 126 historical full60 suites and 1,000 methods,
plus four previously captured working61--66 suites and eight
methods, plus two new pass67 suites and three methods.
The full67 set therefore has 132 suites and 1,011 methods.

Every inherited command string is preserved. Output distinguishes
cumulative working additions, 6 suites and 11 methods, from
current pass67 additions, 2 suites and 3 methods. A mismatch with
a suite's expected method count is a failure even if its process
exits successfully.

Successful inherited output is omitted from JSON only after
hashing its full captured combined stdout/stderr text. Failed
and current-pass output remains in full; launch errors are
reported separately. The runner writes no verification,
checkpoint, registry, or frozen packet.

Jet's bounded code audit checked syntax, all 132 script paths,
the exact inherited list, and new AST method counts. Mocked
process results checked compaction and hashes, output retention,
failed exits, missing summaries, count mismatches, and launch
errors. Mocked aggregation gave 132/1,011, 6/11, and 2/3.
These diagnostics did not launch mathematical suites and are
not a captured regression. General subsequently confirmed a
complete clean read-only code audit, without executing the
runner or any suite.

Root then ran the full command set and saved the complete
[actual full67 capture](verification-pass67-working.json).
The recorded interval is September 14, 2026,
01:00:54.530456 through 01:02:30.132767 UTC. Root reports the
execution session exited zero with untruncated tool output.
All 132 suites and 1,011 methods passed.

Jet independently inspected every one of the 132 saved records.
All inherited 130 commands and method counts agree exactly with
pass66. Every exit status, pass flag, method-count match, summary,
and timing field is consistent. Both retained new outputs hash
to their recorded SHA-256 values. The 130 omitted successful
outputs cannot be reconstructed from their hashes; their full
text hashing is the reviewed runner's behavior, not a new
independent reproduction of those omitted streams.

The two new suites in this full run took 0.159 s for two methods
and 0.406 s for one method. These are distinct run timings,
not additional methods beyond the targeted runs in Section 5.
The capture is 98,259 bytes with SHA-256
f3a00db1f0d024f2257ca4721250d4a5cb72fb13d71f717731f504e7c49aac0b.
Jet did not rerun the full command set or write the capture.
Root retains responsibility for the final integrity capture
and checkpoint.

The first integrity run encountered a link-parser false positive:
the TeX expression \([E,T_v](x)\) was read as a Markdown link to
a file named x. Root changed the parser to exclude complete
TeX inline/display regions and fenced code before checking
prose links. Jet independently read this delta and checked
that it removes the math/code false links while retaining
ordinary Markdown links. This was an integrity-parser defect,
not a mathematical assertion or test-method failure.
Root reports the subsequent actual integrity run passed at
01:07:41.968560 UTC on September 14, with ten current artifacts,
27 local link paths and one explicitly deferred future
checkpoint link. The final hash capture follows this audit
update; repeated integrity runs add no mathematical methods.

## 7. Sources and larger-goal boundaries

The dependent endpoint applies the inherited one-good-output
lemma. Jet and Root fully reread its local written proof;
General also reports complete inherited pass41 and pass66
reads. This does not claim a fresh complete read of every
original classification paper cited by those notes.

The independent endpoint constructs an actual ambient coordinate
slice and uses the slice theorem. Its earlier normal-form and
polynomial-curve dependencies remain explicitly inherited.
Finite determinant calculations do not verify those sources.

Jet read the [constant-top synthesis](constant-cubic-closure-pass67.md)
through EOF. Its mathematical scope agrees with the two proofs
and frozen low-flow theorem: constant \(E^3x\), not merely
\(E^4x=0\); a supplied actual frame, not a universal frame.
Jet flagged that its review summary must distinguish General's
author self-review from independent reviews of that same note.
Root applied that wording correction, and Jet read the revised
paragraph. No mathematical conclusion changed.

No human expert review, formal verification, statement-level
historical novelty certification, external communication, or
submission is recorded. No central claim-registry or experiment
manifest integration is performed here. Nonconstant-top and
higher-flow sectors and the separate universal frame-existence
problem remain outside the completed conclusion.
