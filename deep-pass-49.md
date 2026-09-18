# Normalized covers, nodal obstructions, and actual frame generation

The remaining quadratic branch has fewer possible obstruction points.
Every normalized exceptional-cover point is reached by the actual
exceptional surface. This gives a trace argument excluding ordinary
nodes of the full plinth, without assuming the second-image obstruction
scheme reduced. Independently, the supplied coordinate frame forces
generation in intrinsic degree at most two off a simultaneous zero locus.

These are conditional results, not a solution of complex-threefold
cancellation. The working interpretation is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The pasted email has a dimensional inconsistency, and this corrected
interpretation has not been confirmed by the professor. An arbitrary
cylinder is not known here to admit the restricted frame used below.

## 1. Hypotheses and separation of the two arguments

For the normalized-cover result, let \(A\) be the domain in (1)
and let \(D\ne0\) be a primitive locally nilpotent derivation with
\[
C=\ker D\simeq\mathbb C^{[2]},\qquad
X=\operatorname{Spec}A,\quad S=\operatorname{Spec}C.
\tag{2}
\]
The cylinder supplies smoothness, factoriality, and contractibility
of \(X\). The previously established intrinsic quotient construction
supplies the actual exceptional factorization and product complement.
These inputs do not assume that \(A\) is already polynomial.

The nodal application uses the narrower, actual independent-defect
degree-two setting. In that setting the full residue invariant field
over each retained primitive plinth component has degree two.
The frame-generation argument additionally uses the original four
coordinate generators and the inherited generic quadratic graph.
The hypotheses must not be interchanged.

The complete supporting arguments are the
[normalized-cover note](research/normalized-cover-surjectivity-pass49.md),
[node note](research/nodal-plinth-obstruction-pass49.md), and
[frame note](research/frame-filtration-generation-pass49.md).

## 2. Surjectivity after normalization

Write the actual exceptional factorization as
\[
E\xrightarrow{\kappa} Z\xrightarrow{\theta}\Gamma,
\qquad E=\pi^{-1}(\Gamma)_{\mathrm{red}}.
\tag{3}
\]
Here \(\Gamma\) is the retained reduced plinth support, \(\theta\)
is finite, and \(\kappa\) is surjective. Away from finitely many
base values the exceptional surface is a product of the intermediate
curve with an affine line. The complementary morphism is also a
product. These are the relevant published geometric inputs.[^1]

The components have finite normalizations, and dominance from each
normal surface component gives a morphism
\[
\kappa^\nu:E^\nu\longrightarrow Z^\nu.
\tag{4}
\]
Existence is the normal-source factorization property. It does not
itself prove that this morphism is surjective.[^2]

Choose a finite \(F\subset\Gamma\) containing all exceptional values
and a specified point \(q\). Stars denote deletion of \(F\) or its
preimage, and hats denote deletion of the whole exceptional divisor.
The actual homology diagram has exact rows
\[
\begin{array}{ccccc}
H_3(X^*)&\longrightarrow&H_1(Z^*)&\longrightarrow&H_2(\widehat X)\\
\downarrow&&\downarrow\theta_*&&\downarrow\cong\\
H_3(S^*)&\longrightarrow&H_1(\Gamma^*)&\longrightarrow&H_2(\widehat S).
\end{array}
\tag{5}
\]
All coefficients are rational. The reduced pullback divisors identify
the middle map with ordinary curve pushforward. Thus a cycle whose
pushforward is a lower boundary is itself an upper boundary.

Let \(L=\pi^{-1}(F)\). The vanishings \(H_4(X)=H_3(X)=0\),
excision, and the naturality of the Thom maps imply that upper
boundaries are represented in an arbitrarily small neighborhood
of the entire \(L\). This whole-fiber support statement, not
normalization alone, is decisive.

Suppose a normalized point \(\zeta_0\) above \(q\) were unreached.
Take disjoint disks about all normalized points above \(F\), and
keep only disks about reached points. Their inverse image in \(E^\nu\)
contains the whole preimage of \(L\). Finite normalization is proper
in the complex topology, so
\[
E\setminus\nu_E\bigl(E^\nu\setminus
(\kappa^\nu)^{-1}(\text{reached disks})\bigr)
\tag{6}
\]
is an open neighborhood of the whole \(L\). No compactness of \(L\)
is used. The support statement now confines upper boundary cycles
to peripheral loops about reached points.

The finite peripheral loops are independent. Each normalized
component is affine, so its smooth compactification has at least
one additional puncture at infinity. The sole total-puncture
relation therefore gives no relation among the finite loops alone.

A small sphere at \(q\) maps to the sum of its normalized base-branch
loops. Choose one cover loop above each branch, including the loop
at \(\zeta_0\), and weight it by the reciprocal ramification index.
Its pushforward is that sphere boundary. By (5) it is an upper
boundary, although its unreached-loop coefficient is nonzero.
This contradiction proves
\[
\boxed{\kappa^\nu\text{ is surjective componentwise}.}
\tag{7}
\]
The proof does not require a reduced, smooth, irreducible or
affine-line special fiber.

## 3. The full exceptional invariant ring is finite

For one exceptional component, put
\[
B_i=\mathcal O(\Gamma_i),\qquad
T_i=\mathcal O(E_i)^{D_i},\qquad
N_i=\mathcal O(Z_i^\nu).
\tag{8}
\]
The induced \(D_i\) is nonzero by primitivity and factoriality.
The product chart identifies its rational invariant field with
\(\mathbb C(Z_i)\).

An element of \(T_i\) is therefore rational on \(Z_i^\nu\) and
regular after pullback to \(E_i^\nu\). A pole of order \(n>0\)
at a point with local parameter \(t\) would give \(t^nf=u\)
with \(u\) a unit. Surjectivity (7) gives a point above it.
Pullback would put a unit in that point's maximal ideal, a contradiction.

It follows that
\[
B_i\subseteq T_i\subseteq N_i.
\tag{9}
\]
Finiteness of normalization over the base curve makes \(N_i\)
a finite \(B_i\)-module.[^3] Since \(B_i\) is Noetherian,
\(T_i\) is finite too. Localization on the dense product chart
gives its invariant curve ring; passing to fraction fields gives
\(\operatorname{Frac}T_i=\mathbb C(Z_i)\). Thus \(N_i\) is also
the integral closure of \(T_i\).

This does not identify \(Z_i\) with \(\operatorname{Spec}T_i\).
They can be different finite nonnormal models with the same
normalization. A useful consequence is that an actual invariant
vanishing on the whole fiber vanishes at every normalized cover
point above every normalized base branch.

## 4. An ordinary node cannot support the second-image obstruction

Use the intrinsic filtration \(F_n=\ker D^{n+1}\), full plinth
\(\operatorname{pl}(D)=D(A)\cap C=pC\), and second image
\(I_2=D^2(F_2)=pJ\). Here nonzero numerical scalar factors do
not affect image ideals. In local displays, \(J\) denotes its
extension to the displayed local base ring.

Now assume the actual quadratic setup. At an alleged obstruction
point let \(R=C_{\mathfrak m}\), \(\mathfrak n=\mathfrak mR\),
and \(\mathcal A=A\otimes_C R\). The previously proved bundle
and conic results give
\[
F_2=R\oplus Rz\oplus Rw,\quad r=az+bw,\quad J=(a,b),
\quad \gcd(a,b)=1,
\tag{10}
\]
\[
Dr=p,\quad Dz=\epsilon br+B_1,\quad
Dw=-\epsilon ar+B_2,\quad p=aB_1+bB_2,
\tag{11}
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0,\qquad \epsilon\in R^*.
\tag{12}
\]
All \(a,b,B_1,B_2,Q\) belong to \(\mathfrak n\).
In particular \(r\in\mathfrak n\mathcal A\).
There is no extra premise \(B_1,B_2\in J\).

On a normalized branch \(\xi\) of a plinth component, let
\(R_\xi\) be the base DVR and \(T_\xi\) its integral closure
in the actual degree-two invariant field. It is finite free
of rank two. Its maximal ideals correspond to the cover points
over \(\xi\).[^4] By (7) and the vanishing of \(r\) on the whole fiber,
\[
r\in\operatorname{rad}(\mathfrak m_\xi T_\xi).
\tag{13}
\]
Multiplication by \(r\) is nilpotent on the residue algebra,
even if that algebra is nonreduced. Its trace therefore gives
\[
\operatorname{Tr}(r)\in\mathfrak m_\xi.
\tag{14}
\]

The actual minimal-slice argument ensures that the residue of \(r\)
is non-scalar and hence generates the quadratic field extension.
If \(b\) is nonzero on the component, eliminate \(w\) from (12).
Since \(p=0\) there, the exact minimal polynomial is
\[
r^2+\frac{2B_1}{\epsilon b}r-\frac Q\epsilon=0.
\tag{15}
\]
Thus \(B_1/b\) has positive order at \(\xi\). At a smooth
branch through the obstruction point this gives
\(\operatorname{ord}_\xi(B_1)\ge2\).
If \(b\) vanishes identically on the component, coprimality
makes \(a\) nonzero there and (11) makes \(B_1\) identically zero.
The swapped argument gives the same order bound for \(B_2\).

At an ordinary node, the two smooth branches have distinct
tangent directions. Both linear coefficient parts vanish on
both tangents. Consequently
\[
B_1,B_2\in\mathfrak n^2,\qquad
p=aB_1+bB_2\in\mathfrak n^3.
\tag{16}
\]
This contradicts the full plinth's nonzero quadratic initial form.

The proof covers nonreduced \(J\), ramified quadratic covers,
and two branches of a single irreducible nodal curve.
It does not exclude higher-multiplicity or repeated full plinths.
For reduced \(J=\mathfrak n\), combining it with the earlier
cubic determinant restriction also makes the first-jet
coefficient matrix symmetric of rank at most one.

Together with the earlier smooth-point exclusion, a reduced
full plinth with only ordinary nodes forces \(J=C\). This
supplies the whole global quadratic equation, not automatic
recognition of that equation as a polynomial three-ring.

## 5. The original frame forces low-degree generation on an open set

Retain the actual supplied independent degree-two frame
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad E(s_*)=1,
\]
\[
f=Ex_3,\quad g=Ex_4,\quad h_i=E^2x_i\in C,\quad
L=\operatorname{Frac}C.
\tag{17}
\]
The established generic-generator theorem gives
\[
B_L=L[x_3,x_4],\qquad
x_i=\mathcal Q_i(x_3,x_4),\quad \deg\mathcal Q_i\le2,
\qquad A_L=L[j],\quad j=gx_3-fx_4.
\tag{18}
\]
Intrinsic \(D\)-degree agrees with polynomial \(j\)-degree.

If one of \(f,g,h_1,h_2\) is a unit in an invariant localization
\(R\), respectively choose the actual slice
\[
\sigma=x_3/f,\quad x_4/g,\quad Ex_1/h_1,\quad Ex_2/h_2.
\tag{19}
\]
It is affine-linear over \(L\) in the bad coordinates:
\(\sigma=\alpha x_3+\beta x_4+\gamma\) with
\(\alpha f+\beta g=1\). The actual membership follows from
(19), not from assuming these three coefficients belong to \(R\).

The inverse linear system gives
\[
x_3=f(\sigma-\gamma)+\beta j,\qquad
x_4=g(\sigma-\gamma)-\alpha j.
\tag{20}
\]
Projection to \(\sigma=0\) sends the bad coordinates into \(F_1\)
and, by (18), the good coordinates into \(F_2\).
The four original coordinates generate the whole \(B_R\);
the actual slice projection is surjective. Hence
\[
A_R=R[(F_2)_R].
\tag{21}
\]
A finite principal-open cover proves the same result whenever
\((f,g,h_1,h_2)R=R\). This gluing uses individual module
elements and annihilating powers, not an unproved finite
generation assertion.

At a second-image basepoint, the exact conic (12) has a
two-dimensional plane fiber because all its coefficients vanish.
If (21) held there, it would be the whole actual quotient fiber,
whose dimension is one. Therefore
\[
\boxed{\operatorname{Supp}(C/J)\subseteq V(f,g,h_1,h_2).}
\tag{22}
\]
This is a set-theoretic support restriction. No ideal equality,
closed-fiber generation at the remaining points, or universal
frame existence follows.

## 6. Why an arbitrary supplied slice is not enough

A genuine coordinate example separates a useful choice of slice
from an arbitrary one. On \(\mathbb C[u,v,a,c]\), put
\[
g=uv-1,\quad E=u\partial_a+g\partial_c,\quad
x=(u+a^2/2,\ v+c^2/2,\ a,\ c).
\tag{23}
\]
The inverse coordinate change is polynomial. Its actual adjoint
profile is \((1,1,2,2)\), with independent bad determinant
\(4u^2g\). Put \(s_0=va-c\) and \(r=ga-uc\). Then
\(Es_0=1\), \(Er=0\), and \(A=\mathbb C[u,v,r]\).

For any \(N\ge2\), the actual slice \(s_N=s_0+r^N\) gives
projected original generators
\[
\left(
u+\tfrac12(r+ur^N)^2,\quad
v+\tfrac12(vr+gr^N)^2,\quad
-r-ur^N,\ -vr-gr^N
\right).
\tag{24}
\]
Their intrinsic degrees are exactly \((2N,2N,N,N)\).
Thus there is no fixed bound on this projected list for an
arbitrary supplied slice. This is not a counterexample to
bounded-degree generation of the ring: this ring is generated
by \(F_1\) already.

## 7. Verification and unresolved steps

The mathematical arguments are written proofs with inherited
published inputs and separate AI reconstructions. The
[audit record](research/proof-audits-pass49.md) distinguishes
source-dependent topology from exact identities. No human
expert or proof-assistant certification is asserted.

The standalone control is reproducible with:

~~~sh
/opt/anaconda3/bin/python research/frame_filtration_generation_checks_pass49.py
~~~

It is one method checking the actual frame and the nonlinear-slice
example at \(N=2,3,5\). It does not mechanically certify (7), (16),
or (21). The all-\(N\) degree statement follows from the displayed
nonzero leading coefficients.

The [captured full regression](verification-pass-49.json) passes
980 methods across 116 suites, including this one new method.
The [integrity checker](research/consistency_checks_pass49.py)
checks registry scope, source hashes, links and method counts;
it is not a mathematical proof verifier. Reproduce the full
checkpoint with:

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass49.py
/opt/anaconda3/bin/python research/consistency_checks_pass49.py
~~~

The obstruction support is now confined to singular full-plinth
points other than ordinary nodes, and to the simultaneous
speed/acceleration zero locus. The next proof has to use the
actual algebra at those points. Equality with a low-degree
subalgebra cannot be inferred just from agreement at height one.

After \(J=C\), global quadratic recognition still needs its own
hypotheses. The earlier repeated-component cusp obstruction and
the Russell-cubic weak-hypothesis boundary remain relevant.
The moving-frame cases and universal actual-frame reduction
also remain unresolved. No historical novelty claim follows
from the source comparison or from the number of tests.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), *Inventiones Mathematicae* 156 (2004), 163–173, Lemmas 2.1–2.2, Lemma 3.1 and Proposition 3.2, especially diagram (*) and the excision argument. The extension to the unknown actual cylinder factor is justified in the [intrinsic pointwise note](research/intrinsic-pointwise-plinth-pass47.md). The normalized-cover conclusion here is a deduction, not a theorem attributed verbatim to the source.
[^2]: The Stacks Project, [Lemma 29.55.5, tag 035Q](https://stacks.math.columbia.edu/tag/035Q), part (4), normal-source factorization through normalization. Surjectivity of the factored map requires the additional proof above.
[^3]: The Stacks Project, [Lemma 29.55.11, tag 035S](https://stacks.math.columbia.edu/tag/035S), finiteness of normalization for Nagata schemes. All varieties here are of finite type over \(\mathbb C\).
[^4]: The Stacks Project, [Lemma 33.41.2, tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R), semilocal integral closure of a reduced curve. The rank-two trace calculation additionally uses the separately proved actual quadratic invariant-field identification in the [minimal-slice note](research/minimal-quadratic-slice-pass46.md).
