# Universal reconstruction and the missing center-lifting theorem

The finite reconstruction results checked here do not reduce every primitive
three-variable LND to the coordinate constructions of pass 20. There
is, however, an exact all-input reduction to a finite thickened-center
problem. A plausible automatic lifting statement for those finite jets
is false, even for a primitive derivation with connected plinth. The
failure concerns the specified lift, not polynomiality of its kernel.

This bounded pass records the exact algebra and primary-source scope.
It establishes neither novelty nor general cancellation. In particular,
it does not turn an arbitrary four-variable slice into an invariant
extension. The two global obligations remain distinct.

## 1. The precise target

Let
\[
R=\mathbb C[x_1,x_2,x_3],\quad
0\ne D\in\operatorname{LND}(R)\text{ primitive},\quad
C=\ker D\cong\mathbb C^{[2]},
\]
\[
D(R)\cap C=pC,\qquad Dr=p,\qquad
0\ne V\in C,\qquad(p,V)C=C.
\tag{1}
\]
The ring to recognize is
\[
M=R[r/V].
\tag{2}
\]
The [two-way modification reduction](arbitrary-invariant-kernel-pass18.md)
already proves \(M^{[1]}\cong\mathbb C^{[4]}\), and the
[global bridge note](global-modification-bridge-pass19.md) proves
preservation of every higher image ideal under \(D\mapsto VD\).
Neither assertion gives an absolute polynomial presentation of \(M\).

If the reduced plinth is connected, the earlier plinth-unit argument
gives \(V=c+p_{\mathrm{red}}Q\), with \(c\ne0\). Scaling \(V\)
by \(c^{-1}\) does not change (2), so the finite-jet question can
assume \(V\equiv1\pmod{p_{\mathrm{red}}}\). The proof below does
not otherwise require connectedness. If \(p\) is a unit or \(V\)
is constant, the polynomial conclusion is already elementary.

## 2. An actual universal finite-center lemma

The following proof uses only a local slice, finite generation, and
the polynomial invariant ring in (1). It does not assume a free
degree-module basis, an invariant ambient coordinate, a particular
local-slice equation, or a kernel-graph path.

**Lemma.** Put \(S=C[T]\). For some integer \(N\ge1\), there is
an ideal \(I\subset S\), containing \(p^N\), such that
\[
R\cong_C S[I/p^N].
\tag{3}
\]
Let \(\theta:S\to S\) fix \(C\) and send \(T\) to \(VT\),
and put \(J=\theta(I)S\). Then
\[
M\cong_C S[J/p^N].
\tag{4}
\]
Moreover \(\theta\) induces an automorphism of \(S/(p^N)\),
and
\[
J/(p^N)=\overline\theta\bigl(I/(p^N)\bigr).
\tag{5}
\]
If \(V\equiv1\pmod{p_{\mathrm{red}}}\), that automorphism is
the identity after reducing the coefficient ring. Both ideals are
stable under \(p\partial_T\).

**Proof.** Identify \(S\) with \(C[r]\subset R\) using
\(T\mapsto r\). The local-slice theorem gives
\(R_p=C_p[r]\). Choose \(N\) large enough that
\(p^Nx_i\in C[r]\) for all three original coordinates, and set
\[
I=p^NR\cap C[r].
\tag{6}
\]
This is a finitely generated ideal because \(S\) is Noetherian.
Every \(i/p^N\), with \(i\in I\), belongs to \(R\), and
these fractions include \(x_1,x_2,x_3\). This proves (3), with
no saturation omitted.

For (4), embed the second copy of \(S\) in \(M\) by
\(T\mapsto w=r/V\). For each \(F(T)\in I\),
\[
\frac{\theta F(w)}{p^N}=\frac{F(Vw)}{p^N}
 =\frac{F(r)}{p^N}\in R.
\]
The resulting overring contains \(w\) and every original \(x_i\);
it is therefore exactly \(R[w]\). Injectivity follows from the
transcendence of \(w\) over \(C\), and gives (4).

Since \((p,V)=1\), \(V\) is a unit modulo \(p^N\). If
\(VW\equiv1\pmod{p^N}\), the inverse of
\(\overline\theta\) sends \(T\) to \(WT\). Equation (5)
now follows directly from extension of ideals and surjectivity of
\(\overline\theta\). Its reduced identity follows from the
stated congruence on \(V\).

Finally, \(p\partial_T\) is the restriction of \(D\) under
the first embedding. It preserves (6). On \(S\),
\[
(p\partial_T)\theta=V\theta(p\partial_T),
\]
so it also preserves \(J\). Under the second embedding it is
the restriction of \(VD\). This proves the lemma.

This supplies a finite global presentation, not just formal charts.
The remaining step is not existence of a finite denominator bound.
It is recognition of the transformed modification (4).

## 3. The tempting universal jet-lifting repair is false

An attractive attempted continuation of the lemma would be:

> An automorphism of \(S/(p^N)\) arising in (5), and equal to
> the identity on the reduced divisor, lifts to a polynomial
> automorphism of \(S\) preserving \((p^N)\).

Such a lift would transport \(I\) exactly to \(J\), because
both contain \(p^N\). The established affine-modification lifting
property would then identify (3) and (4). The proposed continuation
is false under precisely these hypotheses.

Take
\[
R=\mathbb C[x,y,z],\qquad
D=x^2\partial_y+2y\partial_z,\qquad
h=x^2z-y^2.
\tag{7}
\]
This derivation is triangular and primitive. Its kernel is
\(C=\mathbb C[x,h]\), its minimal local slice is \(r=y\), and
its plinth is \(p=x^2\). Here is a direct minimality check.
After inverting \(x\),
\(R_x=\mathbb C[x^{\pm1},h][y]\). Every degree-at-most-one
element has form \(a(x,h)y+b(x,h)\). If its coefficients had
a pole at \(x=0\), clearing a smallest denominator and reducing
modulo \(x\) would yield a nontrivial identity
\[
A(-y^2)y+B(-y^2)=0.
\]
Its odd and even parts vanish separately, a contradiction. Hence
\(\ker D^2=C\oplus Cy\), which proves the plinth assertion.
The same no-poles argument in degree zero verifies the kernel.

Choose \(V=1+x\). Then \((x^2,1+x)=1\), with explicit
identity \(x^2+(1-x)(1+x)=1\). The reduced plinth is the
connected line \(x=0\), and \(V\equiv1\pmod x\). With
\(S=\mathbb C[x,h,T]\), one may use
\[
N=1,\qquad I=(x^2,h+T^2),\qquad
J=(x^2,h+(1+x)^2T^2).
\tag{8}
\]
The finite quotient automorphism is
\[
\overline\theta(x)=x,\quad
\overline\theta(h)=h,\quad
\overline\theta(T)=(1+x)T\quad\text{in }S/(x^2).
\tag{9}
\]

Suppose that \(\Phi\in\operatorname{Aut}_{\mathbb C}(S)\)
preserves \((x^2)\) and induces (9). Since \(S\) is a UFD,
\(\Phi(x)=cx\) for \(c\in\mathbb C^*\). Reduction modulo
\(x^2\) forces \(c=1\). Consequently
\[
\Phi(h)=h+x^2H,\qquad
\Phi(T)=(1+x)T+x^2L
\]
for polynomials \(H,L\). Since \(\Phi(x)=x\), its Jacobian
determinant reduces modulo \(x^2\) to the two-by-two determinant
in variables \(h,T\), namely \(1+x\). But a polynomial
automorphism has nonzero constant Jacobian. No constant is
congruent to \(1+x\pmod{x^2}\). This is a contradiction.

This does **not** obstruct transporting just the ideals by a
different map. Indeed the triangular automorphism
\[
x\mapsto x,\quad T\mapsto T,\quad
h\mapsto h+((1+x)^2-1)T^2
\tag{10}
\]
transports \(I\) to \(J\) exactly. Correspondingly
\(M=\mathbb C[x,w,z]\) is polynomial. Equation (10) changes
the invariant-plane embedding and does not induce the prescribed
jet (9). Thus a valid universal repair must control the center
without insisting on lifting that exact coefficient-fixing jet.

An even earlier shortcut fails in the same example. The canonical
rank-one restriction is \(x^2\partial_T\) on \(S\). Its
primitive normalization \(\partial_T\) does not extend to
\(R\), because
\[
\partial_T\left((h+T^2)/x^2\right)=2T/x^2\notin R.
\tag{11}
\]
Normalizing the smaller-ring derivation discards essential extension
data. Rank one on a proper polynomial subalgebra is not a rank-one
coordinate reduction on the original ring.

## 4. What actual finite-generation and descent theorems supply

### The recent rank construction has an invariant-coordinate hypothesis

Dasgupta--Gaifullin's 2025 Corollary 3.18 starts with a primitive
LND killing the specified ambient coordinates \(x_3,\ldots,x_n\).
Its finite modified-commuting chain keeps them fixed. In three
variables its hypothesis is rank at most two. Their Lemma 5.1
does give \(C[r]\subset R\) for every LND, but not equality.
Theorem 4.5(i) says that a primitive rank-three LND has no
nonequivalent commuting LND.[^1]

Thus the theorem does not furnish a first nonequivalent commuting
step out of a rank-three derivation. That is an actual obstruction
to the proposed commuting method, not evidence against noncommuting
local-slice constructions. Equation (11) separately blocks importing
the primitive rank-one classification from the smaller ring.

### Canonical degree reconstruction exists, but its rings need not be polynomial

Freudenburg's degree-module algorithm terminates over a Noetherian
kernel. His finite degree resolution uses the subalgebras
\(R_i=\mathbb C[\ker D^{i+1}]\). Its geometric birational steps
are equivariant affine modifications. These are statements on varying
ambient rings, not coordinate changes in a fixed polynomial ring.[^2]

The source itself gives a decisive control. For its primitive
rank-three \((2,5)\) example, write
\[
f=xz-y^2,\quad g=zf^2+2x^2yf+x^5,\quad r=x^3+yf.
\]
The plinth is \((fg)\), so its reduced support is connected.
Its first two positive-degree rings are
\[
R_1=\mathbb C[f,g,r],\qquad
R_2=\mathbb C[f,g,r,x]
 \cong\frac{\mathbb C[F,G,T,X]}{(XG-F^3-T^2)}.
\tag{12}
\]
These presentations and \(R_2\)'s place in the resolution are
computed in Section 8.2.3 of the primary paper.[^2]

Independently, the gradient of \(XG-F^3-T^2\) is
\((-3F^2,X,-2T,G)\). It vanishes at the origin. This is a
three-dimensional domain whose maximal ideal there has cotangent
dimension four, so \(R_2\) is not a polynomial three-ring.
In particular, even primitive rank three and connected plinth do
not make every intermediate stage polynomial. An induction using
only the already-proved polynomial-ambient family theorem cannot
cross this stage without an additional theorem.

### Kernel-graph blocks are not a universal path theorem

Daigle's generalized graph must also be distinguished from the
original Freudenburg graph. His 2004 introduction explicitly gives
inclusion of the latter's edges into the former and does not identify
the edge sets. Theorem 5.1 decomposes the nonisolated part into
connected blocks associated to Danielewski generic surfaces. Distinct
blocks meet in at most one vertex; this does not prove that all
blocks meet one another, or exclude isolated vertices.[^3]

Daigle's homogeneous Theorem 4.5 proves connectivity under a fixed
positive grading of positive type. Paragraph 4.4.4 gives degree
descent after an invariant homogeneous ambient coordinate has been
supplied. The introduction states a broader positive-grading result
whose type-zero part is assigned to subsequent work. None of these
statements removes the grading hypothesis for arbitrary \(D\).[^4]

Even an arbitrary kernel-graph path, if separately established,
would require another argument here: each edge would have to
transport the extension problem's full centers and coefficient
conditions. The pass-20 proof establishes this for its explicit
controlled operations, not for every edge in either graph.

### A 2026 local-slice result has a different endpoint

Isaev's July 2026 preprint proves orbit and flexibility statements
for suspensions \(uv^k=f\) over a flexible variety, with \(f\)
a local slice; its Section 4 specifies the additional exceptional
set. This is not a kernel-graph generation or polynomial-recognition
theorem. Moreover \(Vw=r\) has an old base coefficient \(V\),
not an additional independent suspension variable.[^5]

## 5. The irreducible gap after this pass

There are two exact possible next lemmas, neither proved here.

1. **Center recognition:** for the ideals \(I\) arising in (6),
   prove that \(S[\theta(I)/p^N]\) is polynomial whenever
   \(S[I/p^N]\cong\mathbb C^{[3]}\) and the derivation and
   comaximality hypotheses in (1) hold. One sufficient route would
   construct a denominator-preserving automorphism carrying the
   full ideals, without requiring its quotient map to be (9).
   That sufficient automorphism criterion may itself be stronger
   than necessary and is not assumed to hold universally.
2. **Graph reduction with compatibility:** construct a terminating
   path from the given primitive rank-three input to a covered
   input, together with a proof that the desired absolute kernel
   recognition transfers across every permitted edge. A theorem
   about just one of these obligations does not establish the other.

The [coordinate-frame minimization note](coordinate-frame-minimization-pass.md)
has a separate missing frame-descent lemma on four-space. A canonical
resolution of a three-variable derivation neither constructs that
frame nor identifies an arbitrary cancellation kernel with a ring
of form (2). The current source audit therefore changes the next
action from finding a finite reconstruction to proving compatible
center recognition. Finiteness is available; preservation of the
required global polynomial structure is the remaining issue.

The control calculations were independently expanded with SymPy in
`/opt/anaconda3/bin/python`: invariance and the local-slice derivative
in (7), coefficient gcd, the Bezout identity, inverse quotient scaling,
the center transport and its inverse, the constant and linear terms
of the hypothetical lift's Jacobian, and the relation, local-slice
derivative, and singular gradient in (12). These check the displayed
finite identities. They do not certify the universal lemma, the
source classification theorems, or general cancellation.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, *On locally nilpotent derivations
    of polynomial algebra in three variables*, Sbornik: Mathematics
    **216** (2025), 456--484. [Published primary record](https://www.mathnet.ru/eng/sm10094)
    and [author text](https://arxiv.org/html/2306.00510v2), Lemma 3.17,
    Corollary 3.18 with proof, Theorem 4.5(i) with proof, and Lemma 5.1.
    No numerical universal-level convention or unrestricted use of
    Remark 5.2 is needed.

[^2]: G. Freudenburg, *Canonical factorization of the quotient morphism
    for a Ga-action on an affine variety*, Transformation Groups
    **24** (2019), [DOI](https://doi.org/10.1007/s00031-018-9472-y).
    [Primary preprint](https://arxiv.org/pdf/1602.08786), Lemma 4.1,
    Theorem 4.4 and proof, Sections 5--7, and Sections 8.2.1--8.2.3.
    The singularity conclusion following (12) is the elementary
    Jacobian calculation here, not an extra assertion attributed
    to the factorization theorem.

[^3]: D. Daigle, *Locally nilpotent derivations and Danielewski surfaces*,
    Osaka Journal of Mathematics **41** (2004), 37--80.
    [Primary journal scan](https://ir.library.osaka-u.ac.jp/repo/ouka/all/7758/1606ojm.pdf),
    introduction, Theorems 4.8 and 5.1, and Section 6. These exact
    statements are not used to assert the current open status of
    every graph question posed in 2004.

[^4]: D. Daigle, *Classification of homogeneous locally nilpotent
    derivations of k[X,Y,Z]. Part I: Positive gradings of positive type*,
    Transformation Groups **12** (2007), 33--47.
    [Primary author manuscript](https://www.researchgate.net/publication/227202730_Classification_of_homogeneous_locally_nilpotent_derivations_of_kXYZ_Part_I_Positive_gradings_of_positive_type),
    introduction and Sections 4.1--4.5. The directly hosted author
    PDF did not open reliably; the complete relevant author text
    was read through this publicly accessible manuscript page.

[^5]: R. Isaev, *The flexibility of m-suspensions constructed via a
    local slice*, [primary preprint, July 2026](https://arxiv.org/pdf/2607.11678),
    Section 4, G-orbit decomposition theorem and Corollary 4.1.
    This is a scope comparison, not a reconstruction of the full
    preprint's proof or a claim of peer review.
