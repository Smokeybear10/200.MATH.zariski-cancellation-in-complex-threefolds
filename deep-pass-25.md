# Pass 25: exact symmetry gates and a genuine algebraic lifting obstruction

The unrestricted complex threefold cancellation conjecture is not solved.
This pass replaces several proposed shortcuts by exact statements:
a polynomial coordinate-pair elimination criterion, a full
invariant-plane normalizer obstruction, and a one-step algebraic lifting
obstruction for the prescribed pinched surface. It also proves that
flatness over the smaller nodal base is not an obstruction.

The working target is still

\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]

This is the corrected interpretation under investigation, not a
dimension or field convention confirmed by Professor Luo.
The written proofs below and in the linked notes concern stated
subproblems. They do not provide the universal reduction needed for (1).

## 1. Exactly when a coordinate-pair row operation preserves local nilpotence

Let \(S\) be a \(\mathbb Q\)-domain,
\(B=S[u,v]\), \(T=\partial_u\), \(U=\partial_v\), and \(h\in B\).
There is an exact all-degree criterion:

\[
W=U-hT\text{ is locally nilpotent}
\quad\Longleftrightarrow\quad T(h)=0.
\tag{2}
\]

If \(T(h)=0\), integrate \(h\) in \(v\) inside \(S[v]\).
For \(F'=h\), the coordinates \(u+F(v),v\) make \(W\) a coordinate
partial. Notice that \(h\) need not be killed by \(U\).

For necessity, suppose \(m=\deg_u h>0\).
If \(m\geq2\), the \(u\)-degree of \(W^j(u)\) is
\(1+j(m-1)\), with nonzero leading coefficient obtained by multiplying
the successive positive integers \(1+i(m-1)\) and powers of the leading
coefficient of \(h\). If \(m=1\), write \(h=\alpha(v)u+\beta(v)\).
The coefficient of \(u\) in \(W^j(u)\) satisfies
\(a_{j+1}=a_j'-\alpha a_j\), \(a_0=1\).
For nonconstant \(\alpha\), its degree grows; for constant nonzero
\(\alpha\), it equals \((-\alpha)^j\). Either way it never vanishes.

The [full proof and exact control](research/commuting-leading-pass25.md)
apply this to an inherited commuting coordinate frame.
In the original coordinates \(a,b,c,s\), a forced leading-term
cancellation has coefficient \(c^2\) and produces

\[
W=\partial_s+(ca-2csb)\partial_a-cb\partial_b-c^2\partial_c.
\tag{3}
\]

It has \(W(s)=1\) and lowers the selected filtration degree, but

\[
W^j(c)=(-1)^j j!\,c^{j+1}\ne0.
\tag{4}
\]

The coefficient is invariant under the leading field but not under the
actual coordinate partial: \(T_c(c^2)=2c\).
Thus matching leading coefficients does not certify a valid additive
action. In this exact same-degree row operation the coefficient is forced,
so choosing another admissible coefficient cannot fix it.
Changing both columns or temporarily raising degree remains outside
the exclusion.

A second precise limit uses established UFD facts.[^1]
For a nonzero primitive LND \(\delta\) on a finitely generated
characteristic-zero UFD \(A\), with \(K=\operatorname{Frac}(A)\),

\[
\operatorname{Der}(A)\cap K\delta=A\delta,\qquad
\operatorname{LND}(A)\cap K\delta=(\ker\delta)\delta.
\tag{5}
\]

Here primitive means no nonunit divides all values, not that the
values generate the unit ideal. Denominators in a regular rational
multiple would divide all values and hence cancel. If \(h\delta\)
is locally nilpotent, its value on \(h\) is divisible by \(h\);
the LND divisibility lemma forces \(\delta(h)=0\).
An invariant multiple changes the plinth by that same factor.
Consequently polynomial combinations, brackets and regular rational
saturation that stay on this rational orbit line cannot manufacture
a missing primitive slice. This is not a claim that all useful LNDs
on an unknown \(A\) belong to one such line.

## 2. Allowing the invariant plane to move inside itself is still restrictive

Let \(R=\mathbb C^{[3]}\), let \(D\) be a nonzero primitive LND,
and set \(C=\ker D=\mathbb C^{[2]}\).
Choose a minimal local slice \(Dr=p\), where the full plinth is
the nonzero nonunit principal ideal \(pC\).
For \(d\in\sqrt{pC}\), put \(v=1+\lambda d\) and

\[
\mathcal B=R[\lambda,w]/(vw-r),\qquad
\mathcal A=C[\lambda],\qquad
\Delta|_R=vD,\quad \Delta(\lambda)=0,\quad \Delta(w)=p.
\tag{6}
\]

The previously established stable cylinder gives that \(\mathcal B\)
is a UFD with constant units. The two charts \(v\ne0\) and \(p\ne0\)
give \(\ker\Delta=\mathcal A\),
\(\ker\Delta^2=\mathcal A+\mathcal A w\), and full plinth
\(p\mathcal A\), with \(\Delta\) primitive.

The [normalizer proof](research/coupled-homotopy-pass25.md) establishes

\[
\begin{gathered}
\delta\in\operatorname{LND}(\mathcal B),\quad
\delta(\lambda)=1,\quad \delta(\mathcal A)\subseteq\mathcal A\\
\Longrightarrow\quad
[\delta,\Delta]=0,\quad \delta(p)=0,\quad
\delta(w)\in\mathcal A .
\end{gathered}
\tag{7}
\]

To see the key step, conjugate \(\Delta\) by the polynomial flow
of \(\delta\). The two primitive LNDs on the actual UFD
\(\mathcal B[\tau]\) have the same kernel \(\mathcal A[\tau]\).
Their ratio in its fraction field has valuation zero at every prime,
so is a unit. All units are constant, and at \(\tau=0\) the ratio
is one. Differentiation gives commutation. Applying it to \(w\)
gives \(\delta(p)\in p\mathcal A\), hence \(\delta(p)=0\);
then \(\Delta\delta(w)=0\).
The same-kernel and centralizer machinery is inherited, not a new
abstract principle.[^1]

There is a full-algebra interpretation: a \(\delta\) satisfying the
premise exists exactly when a \(\mathbb C[\lambda]\)-isomorphism
\(\mathcal B\simeq R[\lambda]\) carries \(\mathcal A\) onto
\(C[\lambda]\) setwise. Apply the slice theorem both to
\(\mathcal B\) and to \(\mathcal A\), then evaluate at \(\lambda=0\).
Conversely transport \(\partial_\lambda\).
Thus (7) tests the transport of an embedded subalgebra, not only
a list of formulas for a derivation.

### The exact non-fence extension

An effective plane divisor is a fence if its equation is a polynomial
in one plane coordinate after a polynomial change of coordinates,
equivalently if it is \(F\times\mathbb A^1\) with \(F\) finite.
For \(C=\mathbb C[u_0,v_0]\) and nonconstant \(p\in C\), we prove:

Every LND of \(C[\lambda]\) sending \(\lambda\) to one and killing
\(p\) fixes \(C\) pointwise if and only if \(\operatorname{div}(p)\)
is not a fence.

Here the published inputs are explicit. Stampfli's Proposition 3.0.3
makes the stabilizer of a non-fence an algebraic group without nontrivial
unipotent elements.[^1] Its identity component is a torus by the
standard connected algebraic-group result.[^2]
Every regular map from the entire affine line to a torus is constant,
since polynomial units are constant.

The subtlety is that the flow moves \(\lambda\). If \(\Phi_\tau\)
is the flow, freezing \(\lambda=c\) gives a family of plane
automorphisms whose inverse is
\(\Phi_{-\tau}|_{\lambda=c+\tau}\), not the specialization at \(c\).
Both maps are polynomial of uniformly bounded degree. They therefore
give a genuine regular map into the stabilizer, starting at the identity.
It is constant. Differentiation for every \(c\) proves the assertion.
For a fence, choose coordinates with \(p\in\mathbb C[u_0]\);
then \(\partial_\lambda+\partial_{v_0}\) supplies the converse.

The [complete proof](research/nonfence-plane-rigidity-pass25.md) combines
this with (7) and the prior common-residue, full-plinth criterion:

\[
\begin{gathered}
\exists\,\delta\in\operatorname{LND}(\mathcal B),\
\delta(\lambda)=1,\
\delta(\mathcal A)\subseteq\mathcal A\\
\Longleftrightarrow d\in pC,
\qquad\text{if }\operatorname{div}(p)\text{ is not a fence}.
\end{gathered}
\tag{8}
\]

For necessity the horizontal slice would identify the zero and one
fibers over \(C\); the coefficient \(1+d\) has common residue one
on every plinth component, and the relative theorem forces \(p\mid d\).
For sufficiency write \(d=pH\) and take
\(\delta(\lambda)=1\), \(\delta(w)=0\), \(\delta|_R=HwD\).
No connected-support assumption is needed.

The factor-field special case has a separate elementary proof:
if the distinct irreducible factors of \(p\) generate a field of
transcendence degree two, \(\delta(p)=0\) kills each factor and then
all of \(\operatorname{Frac}(C)\) by separability.
The non-fence result also covers irreducible curves, where that
argument has no force.

The complete affine parameter line matters.
The family \((u_0,v_0)\mapsto(\lambda u_0,\lambda^{-1}v_0)\)
preserves \(u_0v_0\) over \(\mathbb G_m\), and a formal exponential
does so formally. Neither is polynomial over all of \(\mathbb A^1\).

### The obstruction is present even in a polynomial ambient ring

For \(D=x^2\partial_y+2y\partial_z\), \(r=y\), \(p=x^2\), \(d=x\),
the family is actually \(\mathbb C[\lambda,x,w,z]\), with

\[
h=x^2z-(1+\lambda x)^2w^2,\qquad
\mathcal A=\mathbb C[\lambda,x,h].
\tag{9}
\]

There is no horizontal LND preserving \(\mathcal A\) setwise.
This stronger conclusion is proved directly because \(x^2\) is a fence.

By (7), such a derivation kills \(x\).
Over \(\mathbb C(x)\), local nilpotence forces its value on \(h\)
to be independent of \(h\), using the same all-degree recurrence
as in Section 1. Differentiating (9) and reducing modulo \(x\)
forces its values on \(h\) and \(w\) to be divisible by \(x\).
After dividing once more, the even part in \(w\) contains a
nonzero \(2w^2\) that cannot cancel. The note supplies every step.

Yet the coordinate partial \(\partial_\lambda\) does exist on
the ambient polynomial ring. It sends \(h\) outside \(\mathcal A\).
A regular commuting plane-preserving derivation is also displayed,
but its iterates on \(h\) never vanish. Thus regularity, commutation,
and value one on the parameter do not by themselves imply local nilpotence.

Finally, a residual polynomial coordinate pair cannot have both entries
in \(\mathcal A\): at \(\lambda=0\), it would make
\(R=\mathbb C[u_1,u_2]^{[1]}\) with \(u_1,u_2\in C\).
The primitive LND on that line must have unit coefficient, contradicting
its nonunit plinth. Any successful residual-pair construction must
therefore leave the old invariant subalgebra.

## 3. The prescribed surface passes flatness but fails every specified one-step lift

Use the fixed pinched surface \(R_{\rm pin}\) and its action \(\partial\)
from the [preceding surface proof](research/nodal-hypersurface-pass24.md).
The same normalization, six branches, three conductor pairs and
shared line parameters are retained. With \(d=u^4-1\),

\[
T=\ker\partial=\mathbb C+d\mathbb C[u],\quad
A_0=\mathbb C[d,v],\quad v=du^2,\quad
v^2=d^2(d+1).
\tag{10}
\]

Set \(e=du\), \(w=du^3\), and \(\mathfrak n=(d,v)\).
The full curve \(T\) and its nodal subcurve \(A_0\) must not be confused.

The [new surface proof](research/ambient-lifting-pass25.md) establishes
that \(R_{\rm pin}\) is faithfully flat over \(A_0\).
Each original conductor pair has roots whose squares are \(+1,-1\).
At a branch root \(r\), the actual formal base map is
\(u=r(1+d)^{1/4}\), \(v=r^2d\sqrt{1+d}\).
The opposite signs give a compatible, not merely abstract, isomorphism

\[
\widehat{(R_{\rm pin})_q}
 \simeq
\widehat{(A_0)_{\mathfrak n}}[[t]]
\tag{11}
\]

at every closed conductor point. Noetherian completion and power-series
flatness descend flatness to the actual local map.[^3]
Away from the node, the base local rings are DVRs or fields and the
domain extension is torsion-free. Every base fiber is nonempty,
which gives faithfulness. The earlier nonflatness over \(T\) remains
true but cannot be used as a contradiction over \(A_0\).

At the node, however,

\[
T/\mathfrak nT=\mathbb C[e,w]/(e,w)^2.
\tag{12}
\]

This algebra has dimension three and a two-dimensional square-zero
maximal ideal. Any single element generates an algebra of dimension
at most two. Therefore \(T\) is not monogenic over \(A_0\), even
locally at the node; \(T=A_0[e,w]\) proves the exact relative
generator count is two.

This supplies a genuine multiplication obstruction.
Let \(C_*=\mathbb C[D_0,V_0]\),
\(P=V_0^2-D_0^2(D_0+1)\), and \(k\geq1\). Consider any relative
one-step model

\[
W_F=C_*[\rho,Z]/(P^kZ-F(D_0,V_0,\rho)),\qquad
D_F(\rho)=P^k,\quad D_F(Z)=F_\rho,\quad D_F|_{C_*}=0.
\tag{13}
\]

Assume the restriction modulo \(P\) is an integral surface, that the
prescribed \(A_0\) injects, and that the induced derivation is nonzero.
Then it is \(K[Z]\), with
\(K=A_0[\rho]/(\overline F)\), and its derivation is
\(\overline F_\rho\partial_Z\). In characteristic zero the kernel is
exactly the monogenic algebra \(K\). It cannot be the fixed \(T\).
No monicity of \(F\) is assumed. The exclusion survives base
localization by functions nonvanishing at the node.

Unlike the previous module-only countercontrol, the first attempted
repair here is an actual algebra with an actual primitive LND:

\[
W_k=\mathbb C[D_0,V_0,\rho,Z]/
       (P^kZ-\rho^2+D_0V_0),\qquad
D(\rho)=P^k,\quad D(Z)=2\rho .
\tag{14}
\]

The note proves it is a domain, \(P\) remains prime,
\(\ker D=C_*\), and \(D\) is primitive in the common-divisor sense.
Its restriction kernel is only
\(A_0[\rho]/(\rho^2-dv)\simeq A_0[e]\).
The missing generator \(w\) cannot be repaired by renaming \(\rho\).
The invariant-lifting defect is free of rank one, rather than the
required nonfree normalization module.
Moreover the line \(D_0=V_0=\rho=0\) is singular for every \(k\),
and the node fiber is a doubled line.
So this genuine construction is not \(\mathbb A^3\) and does not
realize the prescribed surface.

For an arbitrary hypothetical ambient LND on \(W=\mathbb C^{[3]}\),
the remaining necessary condition is still

\[
(W/DW)[P]\simeq T/A_0\simeq\mathbb C[u^2]
\quad\text{as }A_0\text{-modules}.
\tag{15}
\]

Its generic rank one forces \(P\) to divide the actual plinth:
otherwise localization at the prime \((P)\) makes a local slice
a genuine slice, and integration makes \(D\) surjective there.
This does not prohibit torsion supported only at special closed points.

There is no justified reduction of arbitrary ambient LNDs to (13)
at this node. Kaliman's relevant exceptional-curve conclusion concerns
normalizations, and permits a nodal polynomial curve.[^4]
Masuda's generic normal form uses localization outside the divisor's
generic prime, which may remove the node; the cited global one-step
specialization has an additional factorial-divisor assumption.[^5]
Neither input supplies the missing node-preserving reduction.

## 4. Verification and the remaining proof obligation

The three new standalone checkers import only unittest and SymPy.
The complete regression passed 553 methods across 43 suites, including
28 new methods in three suites, from 07:41:06 to 07:42:21 UTC on
September 13, 2026. Repeated runs are not counted as additional methods.
They test exact identities, degree recurrences, incompatible parity,
formal branch signs, the square-zero fiber algebra, and the singular
quadratic attempt. The universal exclusions and flatness argument are
written proofs, not conclusions from sampling.

[Audit record](research/proof-audits-pass25.md),
[execution log](verification-pass-25.json), and
[artifact-integrity log](consistency-pass-25.json) record distinct
kinds of evidence. An independent AI reconstruction is not human
expert review. No Lean proof or other proof-assistant verification,
comprehensive priority audit, public claim or submission is asserted.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass25.py
/opt/anaconda3/bin/python research/consistency_checks_pass25.py
~~~

The useful next question is not whether another old-plane formula works:
the restrictions above already exclude whole classes without degree bounds.
A construction intended to work for every input in (6) must allow the
embedded invariant plane itself to change. The intrinsic route still
needs a sliced or otherwise sufficient
tangent action for arbitrary \(X\), not just a nonzero leading LND.
The surface route needs a genuine ambient polynomial realization beyond
(13), with the specific multiplication and defect in (15).

Scaling the already given cylinder coordinate gives a semistable
multiplicative action, but its linearization is a classical
reformulation of cancellation, not an independent shortcut.[^6]
No implication established in this pass bridges these remaining
obligations to (1).

## Sources and inherited inputs

[^1]: I. Stampfli, [*Automorphisms of C^3 Commuting with a C+-Action*](https://arxiv.org/pdf/1406.6246v2), v2 (2016), Proposition 3.0.3, Proposition 3.0.5, Lemma 4.1.1(vi)-(ix), subsection 4.2, Proposition 5.1.1 and Lemma 5.1.2. These primary passages were read directly. They supply the plane-stabilizer and established UFD/centralizer inputs, not the entire homotopy statement (8) or the explicit coordinate controls.
[^2]: J. S. Milne, [*Algebraic Groups*, corrected 2022 edition](https://www.jmilne.org/math/Books/iAG2022.pdf), Section 17b and Corollary 17.25, printed p. 360. The statement and proof were read with the connected, algebraically closed-field convention checked.
[^3]: The Stacks Project, [Lemma 10.97.2, tag 00MB](https://stacks.math.columbia.edu/tag/00MB), and [Lemma 10.97.3, tag 00MC](https://stacks.math.columbia.edu/tag/00MC). Both completion statements and proofs were read directly.
[^4]: S. Kaliman, [*Free C+-actions on C^3 are translations*, author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), Lemma 2.2, Notation 2.3, Proposition 3.2 and Theorem 5.2(i). The precise normalization scope was checked; smoothness or unibranchness of every exceptional base curve is not asserted.
[^5]: K. Masuda, [*Factorial affine Ga-varieties with principal plinth ideals*](https://arxiv.org/html/2312.05455), arXiv:2312.05455v1, Section 3, Theorems 3.8-3.9 and the paragraph preceding Corollary 3.10. The localizing element is excluded from the generic prime, not necessarily from the node's maximal ideal. The stated global one-step conclusion requires additional hypotheses that the fixed nodal base lacks.
[^6]: M. Zaidenberg, [*Exotic algebraic structures on affine spaces*](https://arxiv.org/pdf/math/9801075), v2, introductory discussion of semistable multiplicative actions and the cancellation reformulation, crediting Kambayashi-Russell and Bass-Haboush. This is historical attribution for the reformulation, not evidence that a current open problem has been solved.
