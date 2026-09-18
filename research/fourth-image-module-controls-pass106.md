# Free degree modules can have a nonprincipal fourth image

This intrinsic finitely generated algebra control shows that freeness of the
degree modules, their exact derivative sequence, constant reduced
third-degree values, and their multiplication do not by themselves
make the fourth derivative image principal. The control has a genuine
locally nilpotent derivation and generic polynomial line. It fails
the actual mixed-frame hypotheses at a plainly identified point:
its closed fiber is a fat plane, not a flat curve, and the induced
derivation on that entire fiber is zero.

It therefore does not contradict the actual restrictions in
[nonprincipal106](mixed-fourth-image-nonprincipal-pass106.md) or
[the full-Artin refinement](mixed-full-artin-two-generator-pass106.md).

## 1. An actual algebra and derivation

Let R be the two-dimensional regular local ring at the origin
of the affine (a,b)-plane, let K be its fraction field, and let z
be transcendental over K. Inside K[z] put
\[
\begin{gathered}
R=\mathbb C[a,b]_{(a,b)},\qquad
u=z^4/a,\qquad v=(z^3-z^4)/b,\qquad
B=R[z,u,v],\\
N=ab\,\partial_z,\qquad
Nz=ab,\quad Nu=4bz^3,\quad Nv=3az^2-4az^3.
\end{gathered}
\tag{1}
\]
These formulas show that N preserves B. Its restriction is locally
nilpotent, since every element is a polynomial in z over K.
The generic algebra is B_K=K[z]. Moreover ker(N|B)=R:
the generic kernel is K, while evaluating z,u,v at zero maps
B to R and takes any generic constant in B to itself.

There is an exact presentation
\[
B=
R[Z,U,V]/(aU-Z^4,\ bV-Z^3+Z^4),
\qquad
B/(a,b)B=\mathbb C[Z,U,V]/(Z^3).
\tag{2}
\]
Here is an injectivity proof for the first assertion, rather than
only a check of its two displayed relations. In the regular UFD
R[Z,U,V], the polynomial aU-Z^4 is prime: it is primitive and
linear in U over the fraction field of R[Z,V]. The second
polynomial is nonzero in that domain. The two polynomials are
therefore a regular sequence, and their quotient is a complete
intersection with no embedded associated primes; all its minimal
primes have height two.

No height-two prime above the two relations can contain a. Such
a prime contains Z and then either b or V, so it contains
(a,Z,b) or (a,Z,V), of height three. Likewise, a prime containing
b contains Z or Z-1. In the former case it contains a or U,
giving height at least three. In the latter it contains
(b,Z-1,aU-1), again of height three. Thus ab is in no associated
prime and is a nonzerodivisor on the quotient. After inverting ab
the proposed presentation is exactly R_ab[Z]. The map into K[z]
is consequently injective before localization as well.

The second equality in (2) follows by reducing the two relations:
Z^4=0 and Z^3-Z^4=0 are equivalent to Z^3=0.
This closed fiber has dimension two, whereas the generic fiber
has dimension one and B has dimension three. In particular the
map from the regular two-dimensional base is not flat at this
fiber. A direct regular-sequence witness avoids relying only on
dimension: b(vz)=au(1-z), while vz has nonzero image in
C[Z,U,V]/(Z^3). Thus b is a zerodivisor on B/aB, contradicting
preservation of the regular base sequence (a,b) by a flat module.
Also all three derivatives in (1) lie in (a,b)B, so the
induced derivation on the whole closed fiber is zero. These
explicit failures exclude the actual faithfully flat, primitive
mixed-fiber setting.

## 2. Exact low-degree modules, not just sample elements

Write F_j=ker(N^{j+1}|B). Since ab is nonzero in K, F_j consists
exactly of the elements of B having z-degree at most j.

The two principal patches give especially simple descriptions:
\[
\begin{aligned}
B_a&=R_a[z,v]
 =R_a[V,Z]/(Z^4-Z^3+bV),&
(F_4)_a&=R_a\{1,z,z^2,z^3,v\},\\
B_b&=R_b[z,u]
 =R_b[U,Z]/(Z^4-aU),&
(F_4)_b&=R_b\{1,z,z^2,z^3,u\}.
\end{aligned}
\tag{3}
\]
For example, the first monic presentation makes B_a free over
R_a[v] with basis 1,z,z^2,z^3. Under its embedding into K[z],
the monomials z^i v^j for 0<=i<4 have distinct degrees i+4j.
Thus no cancellation can lower the highest such degree. Degree
at most four leaves exactly the five terms displayed in (3).
The other patch has the identical monic-basis argument.
These arguments apply to arbitrary elements, not merely to a
finite polynomial ansatz. Derivative kernels commute with the
invariant localizations used here.

For completeness, intersect these two explicitly computed
lattices. If w=sum_{i=0}^4 p_i z^i lies in F_4, its coefficients
satisfy
\[
\begin{gathered}
p_0,p_1,p_2\in R_a\cap R_b=R,\qquad
p_3\in R_b,\quad ap_4\in R_b,\\
p_3+p_4\in R_a,\quad bp_4\in R_a,\\
p_4=g/(ab),\quad p_3=\beta/b,\quad
g=b\alpha-a\beta
\quad\text{for some }g,\alpha,\beta\in R.
\end{gathered}
\tag{4}
\]
The last line uses only height-one valuations in the UFD R.
The two conditions on p_4 bound its a- and b-poles by one and
exclude all other poles. The condition on p_3 first excludes
every pole except b. Since p_3+p_4 is regular at b, its b-pole
also has order at most one. Finally regularity at b of
(a beta+g)/(ab) says that b divides a beta+g. This proves the
last line and w=p_0+p_1z+p_2z^2+alpha u+beta v.
The reverse inclusion follows directly from (1). These five
elements are K-linearly independent: z^3 only occurs in v
among the last two, and z^4 occurs in u. Therefore
\[
\begin{gathered}
F_4=R\{1,z,z^2,u,v\},\qquad
F_3=R\{1,z,z^2,z^3\},\\
F_2=R\{1,z,z^2\},\qquad F_1=R\{1,z\},\qquad F_0=R,\\
z^3=au+bv,\qquad
F_3\hookrightarrow F_4:
\begin{pmatrix}
1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&a\\0&0&0&b
\end{pmatrix}.
\end{gathered}
\tag{5}
\]
Indeed cancellation of the z^4 coefficient in alpha u+beta v
means b alpha=a beta. Coprimality gives alpha=a delta,
beta=b delta, producing precisely delta z^3.
The assertions for the lower modules then follow immediately.
Reduction of the displayed inclusion has rank three, not four.
Every F_3 element has constant image on the reduced closed
fiber C[U,V], since Z becomes zero there.

## 3. Nonprincipality survives the multiplication gates

Put I_j=N^jF_j. Direct differentiation of the exact bases gives
\[
\begin{gathered}
I_1=abR,\quad I_2=2a^2b^2R,\quad
I_3=6a^3b^3R,\quad
I_4=24a^3b^3(a,b),\\
0\longrightarrow F_3\longrightarrow F_4
 \xrightarrow{\,N^4\,}I_4\longrightarrow0.
\end{gathered}
\tag{6}
\]
The last ideal is not principal: cancelling its nonzero common
factor would make the maximal ideal (a,b) principal in the
regular local ring of dimension two. Thus a free rank-five
module modulo the specified free rank-four submodule need not
be a free rank-one module.

The multiplication restrictions are genuine ring restrictions
here. In particular F_i F_j is contained in F_{i+j}, and
z^4=au, z^3=au+bv verify the potentially relevant products
through degree four explicitly. The matrix compatibility in
the actual full-Artin note also holds in this control:
\[
\begin{gathered}
t=z^3,\quad \theta=4,\quad P=0,\quad Q=3az^2,\quad
g=N^3t=6a^3b^3,\\
t=au+bv,\quad Nu=\theta bt+P,\quad Nv=-\theta at+Q,\\
g=aN^2P+bN^2Q,\qquad
I_4=\theta g(a,b),\qquad g\in(a,b)I_2,\\
I_2^2\subseteq I_4,\qquad I_1I_3\subseteq I_4,\qquad
I_1\subseteq\theta(a,b).
\end{gathered}
\tag{7}
\]
No multiplication obstruction follows from these identities
alone. This conclusion does not assert that every abstract
Hilbert--Burch matrix is realized by an LND algebra, nor that
this particular algebra satisfies the remaining actual-frame
hypotheses. Here both the ring realization and its specific
failures are explicit.

## 4. Finite checks and their scope

The standalone
[checker](fourth_image_module_checks_pass106.py) has two methods.
The first checks the displayed rational embeddings, derivatives,
matrix identities, ideal generators, and low-degree products.
It also checks the presentation's special-fiber ideal by exact
Groebner reduction. Those finite checks do not prove the
arbitrary-element lattice intersection, presentation injectivity,
flatness failure, or universal actual geometry.

The second method independently checks polynomial changes of
parameter on a dual-number line and on a simple line, the finite
algebraic calculation used in
[admissible-boundary106](mixed-admissible-quartic-boundary-pass106.md).
It tests both inverse orders with several nilpotent coefficient
polynomials. It does not test Zariski's Main Theorem, normalization
finiteness, affine-boundary purity, or the all-parameter theorem.

The first assertion-bearing author run used
`/opt/anaconda3/bin/python research/fourth_image_module_checks_pass106.py`.
Both methods passed in 0.367 unittest seconds, exit zero
(chunk 295df5; process wall time 0.954592542 seconds).

All arguments above are elementary algebra apart from the
standard complete-intersection unmixedness used explicitly in
the presentation proof. Root freshly read the complete displayed
[Stacks Section 10.103](https://stacks.math.columbia.edu/tag/00N2),
including its Cohen--Macaulay quotient and no-embedded-prime gates,
to check that standard step. This is Root's source-read scope,
not a fresh primary-source proof read by this note's author.
No full regression is claimed. No file through105 is changed.
