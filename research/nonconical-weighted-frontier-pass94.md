# Weighted conormal rigidity and saturated cubic fibers

The unrestricted complex-threefold cancellation question remains
unsolved in this investigation. Within the supplied nonconical
constant-acceleration frame, a weighted argument now extends the
quadratic conormal restriction to every whole-fiber multiplicity.
The varying-column sector has only two polynomial column shapes.
At multiplicity two, its possible rank drop forces a noncollapsed
fixed companion. In the cubic branch, saturated multiplicity gives
actual finite base change and affine-line reduced components.

These are restricted working deductions with separate AI
reconstructions. They have not received human expert review,
formal verification or historical novelty clearance.

## Question and exact scope

The working interpretation of the professor's message is
\(A[s]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
Neither this correction nor the choice of field and dimension
has been confirmed by the professor. The literal conclusion
\(X\simeq\mathbb A^1\) cannot be correct for arbitrary r, since
the displayed cylinder isomorphism forces \(\dim X=r\).

The present arguments retain the stronger, specified frame of
[the previous synthesis](nonconical-second-normal-frontier-pass93.md).
In the original polynomial four-ring \(B=A[u]\), the locally
nilpotent derivation E has three good affine coordinates with
zero second derivative and a fourth coordinate z with
\(E^2z=q\in\mathbb C^*\). The retained cyclic-Jacobian hypotheses
produce the actual invariant plane \(S=\mathbb C[s_1,s_2]\),
the primitive Jacobian derivation N on A with kernel S, and the
faithfully flat relative presentation \(A=S[A_1,A_2,c]\).
Generically \(A_{\operatorname{Frac}S}=K[v]\), with relative
degree d at most three. The nonconical degree-two and degree-three
branches are the subject here.

No theorem puts an arbitrary sliced action into this frame.
The local arguments below do not remove that separate obligation.
Even recognition of every case of the specified frame remains open.

## Quadratic components at every multiplicity

Assume d=2 and a fixed fiber component is collapsed, meaning both
relative generators have constant residues, and generically has
quotient differential of rank one. Its actual cylinder is an
original affine plane \(\mathfrak qB=\mathfrak P=(X,Y)\).
The centered functions \(F=X-uEX\), \(G=Y-uEY\) generate
\(\mathfrak q\), and the degree identities give \(N^3F=N^3G=0\).
The residue ring is \(\mathbb C[\bar c]\).

At its generic point choose a base parameter x, a second normal
parameter y, and the actual coefficient field \(\mathbb C(c)\).
If the whole-fiber multiplicity is \(\mu\ge2\), the second
base parameter has leading expression
\(f_*=\alpha(c)x+a(c)y^\mu\), with \(a\ne0\), for weights
\(w(x)=\mu,w(y)=1\). This filtration is derived from the actual
fiber equation, not imposed on the full algebra.

The [weighted proof](nonconical-weighted-conormal-rigidity-pass94.md)
constructs the completed local coordinates compatibly with the
given coefficient field. Its commutative-algebra input is the
coefficient-compatible case of Stacks Lemma 10.160.10.[^completion]
The leading operator is
\(D_*=(\gamma x+\rho y^\mu)\partial_y+
\lambda y^{\mu-1}\partial_c\), with
\(\gamma=-\epsilon_0\alpha'\), \(\rho=-\epsilon_0a'\) and
\(\lambda=\mu\epsilon_0a\ne0\).

For weight-one parts by and ey of the actual centers, the
coefficient of \(x^2y^{\mu-2}\) in their third derivatives gives
\[
\begin{gathered}
[x^2y^{\mu-2}]D_*^3(by)
=b(\mu-1)\gamma(\lambda\gamma'+\mu\gamma\rho)
 +(\mu^2-1)b'\lambda\gamma^2,\\
\gamma\ne0\ \Longrightarrow\ eb'-be'=0,\\
\boxed{\ C(c)=\ell(c)\rho_0\quad\text{or}\quad C(c)=\ell_0\rho(c)\ },
\end{gathered}
\tag{1}
\]
where C is the quotient conormal matrix and the indicated row
or column is constant. The alternative \(\gamma=0\) makes
\(\alpha\) constant directly. The nonzero scalar \(\mu^2-1\)
is available for every \(\mu\ge2\). This replaces the ordinary
normal-order coefficient that vanished beyond double fibers.

Returning through the actual polynomial plane gives a nonzero
constant good normal \(L_0\) with
\(EL_0\in\mathfrak P^2\) and
\(N(L_0-uEL_0)\in\mathfrak q^2\).
Neither derivative is asserted to be zero.

## Polynomial column shapes and the double-component boundary

In the nonzero first-normal-action sector, the constant-row
conclusion writes the base first terms as \(\ell(c)F\), with
two linearly independent polynomial entries of \(\ell\).
The exact identity \(N^3G=0\) gives two further leading
coefficient equations. The original global volume then turns
their rational relation into a polynomial Wronskian condition.
The [complete classification](nonconical-conormal-column-classification-pass94.md)
is
\[
\begin{gathered}
\operatorname{Wr}(\ell_1,\ell_2)
\in\operatorname{span}_{\mathbb C}\{\ell_1,\ell_2\}\setminus\{0\},\\
\boxed{\quad
\operatorname{span}\{\ell_1,\ell_2\}
=\operatorname{span}\{1,c\}
\quad\text{or}\quad
\operatorname{span}\{t,t^k\},\quad t=c-c_0,\ k\ge2 .
\quad}
\end{gathered}
\tag{2}
\]
The polynomial lemma follows by choosing unequal degrees m>n:
the Wronskian degree is m+n-1, so n is at most one. The resulting
first-order polynomial equation gives exactly the displayed spans.
No a priori coprimality of the entries is assumed.

The first shape has quotient rank one everywhere on the component.
The second has one rank-zero point. For a double component, the
fixed scheme is generically reduced along that component. Its retained pure
Cohen--Macaulay structure implies that a rank-zero point must lie
on a second fixed component. The quadratic total multiplicity
bound forces exactly a (2,2) fiber.

The companion cannot also be collapsed: the original cylinders
of two collapsed components over one base point are distinct
parallel affine planes and cannot intersect. Thus the power-column
case at multiplicity two forces a noncollapsed fixed companion.
This necessary configuration is not an exclusion or a construction.
Generic fixed-scheme reducedness has not been established for
higher multiplicities.

## Base-order contraction

In the same varying-column sector, \(\alpha(c)\) is a nonconstant
rational function. The first normal form of a base function of
order k is \(G_k(1,\alpha(c))x^k\), which is nonzero because
\(\alpha(c)\) is transcendental over \(\mathbb C\).
The [contraction proof](nonconical-base-normal-order-contraction-pass94.md)
therefore gives, for every r at least one,
\[
\begin{gathered}
S\cap(\mathfrak qA_{\mathfrak q})^r
=S\cap\mathfrak q^r=S\cap\mathfrak P^r=\mathfrak m^r,\\
0\ne EL_0\in\mathfrak m^2,\qquad
N^2(L_0-uEL_0)\in\mathfrak m^2 .
\end{gathered}
\tag{3}
\]
The nonzero speed follows from the retained common-invariant
exclusion for E and the original last-coordinate partial
derivation. The second intrinsic derivative belongs to S by
the actual quadratic degree bound. This is stronger order
information, not a common invariant.

The control \(D=p\partial_y-2y\partial_c\) and \(a_0=p+y^2\)
has \(Da_0=2py\ne0\), \(D^2a_0=2p^2\) and \(D^3a_0=0\).
It shows why second-order membership and small derivation degree
do not by themselves prove invariance. It is not an actual
nonconical-frame example.

## Saturated cubic fibers

Now assume d=3 and the sum of the generic multiplicities of all
components over one closed base point m is six. An admissible U
is a complex linear combination of \(A_1,A_2,c\) that is
nonconstant on every reduced component. With
\(T=(S[U])_{mS[U]}\), the
[saturated base-change proof](nonconical-saturated-base-change-pass94.md)
strengthens the previous finite semilocal normalization:
\[
\begin{gathered}
A\otimes_{S[U]}T=O',\qquad O'\simeq T^6
\text{ as a module},\\
A/\mathfrak q_i=\mathbb C[\tau_i],\qquad
\bar A_{1,i},\bar A_{2,i},\bar c_i
\in\mathbb C+\mathbb C\tau_i,\\
A/mA\simeq\mathbb C[U]^6\text{ as a module},\\
\text{at a rank-zero component:}\quad
\mathfrak q_iA_{\mathfrak q_i}
=(A_1-a_1,A_2-a_2)A_{\mathfrak q_i}.
\end{gathered}
\tag{4}
\]
The last two generators are a regular system of parameters at
that generic point. In reducible cases the further localization
at the selected component is essential.

The proof uses saturation for every admissible projection.
Generic projections of field degree one force a common pole
divisor of degree one, so the reduced components are actual
relative affine lines. Integral localization gives the exact
base change. Finally the whole fiber is finite and torsion-free
over the projection line, hence free, retaining its nilpotents.

These are module statements, not product decompositions of
algebras. The lines need not be disjoint in general. The scoped
multiplicity-one corollary in the same proof shows that such a
component is disjoint from every other component, since its
induced additive action is a nontrivial translation. Thus the
profiles (5,1) and (4,1,1) have pairwise disjoint reduced lines.
Their images in the intermediate exceptional curve need not be
distinct; its normalization has not been separated by this argument.

The actual local parameters do not prove that the known cleared
quadratic and cubic relations generate the full presentation.
Even a length-six transverse complete intersection need not
have the homogeneous form suggested by its numerical length.
No saturated cubic profile has been excluded here.

## Verification and next mathematical question

The [targeted exact capture](verification-pass94-working.json)
passes one symbolic test method with multiplicity subtests 2,3,4.
It checks the leading coefficient, Wronskian cancellation,
strict higher-weight perturbations, and the next two operator
coefficients. A wrong scalar is detected by specialization.
The all-multiplicity conclusion comes from the written proof,
not extrapolation from these three subtests.

The [proof audit](proof-audits-pass94-working.md) records separate
AI reconstructions and the source-reading limits. The
[checkpoint](checkpoint-pass94-working.json) records immutable
artifact identities. Neither model agreement nor matching
hashes constitutes expert or formal mathematical verification.

The next local question is whether the actual original frame
rules out the required noncollapsed companion, or forces a
stronger exact identity than its weighted initial form. On
saturated cubic fibers, the new regular parameters must be
combined with the actual Jacobian and generator relations,
not an assumed homogeneous presentation.

The independent arbitrary-frame reduction remains missing.
Recent related recognition papers concern specified linear
hypersurfaces or singular varieties; their recorded scope
does not automatically cover the smooth unknown threefold
here.[^linear][^singular] This source check supplies no new
universal bridge or claim of novelty.

## Sources

[^completion]: The Stacks Project,
    [Lemma 10.160.10, tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S),
    part (2). Complete displayed statement and proof checked
    September 14, 2026. Used only for the given-field
    power-series description of a complete regular local ring.

[^linear]: Parnashree Ghosh, Neena Gupta and Ananya Pal,
    [On the family of affine threefolds \(a(x)y=F(x,z,t)\)](https://arxiv.org/abs/2403.17397),
    arXiv:2403.17397v2, August 3, 2024. The current abstract and
    version record were checked; no fresh complete proof audit
    of the published version is asserted.

[^singular]: Buddhadev Hajra and Mohit Upmanyu,
    [Generalized Zariski cancellation for Brieskorn--Pham varieties](https://arxiv.org/abs/2606.26890),
    arXiv:2606.26890v1, June 25, 2026. Current abstract and
    version record checked. Its stated singular-variety scope
    is not a theorem about arbitrary smooth affine-space factors.
