# Coordinate-frame minimization for a slice filtration

Let \(B=K[s]\simeq\mathbb C^{[4]}\), with \(E=\partial_s\).
Changing the ambient polynomial coordinate frame repairs the existing
rank-one controls by explicit elementary automorphisms. It does not
presently give a general rank-repair theorem.

There is a precise integer height to minimize. The later
[height-eight theorem](height-eight-algebra-pass.md) now closes every
frame of height at most eight, so a hypothetical nonpolynomial kernel
has minimum height at least nine. The height-seven proof below remains
valid as a weaker historical checkpoint. The missing step is an actual
height-decreasing coordinate change, not the existence of a minimum.

A stronger positive-ring control also survives primitive normalization:
a frame twisted by the flow of Freudenburg's irreducible rank-three LND
has all primitive leading directions equal, up to nonzero constants,
to that same rank-three LND. They retain its fixed point. This does not
obstruct all frames, since the inverse flow untwists the frame.

## 1. A well-defined height, and what its minimum would mean

For a polynomial coordinate frame \(x=(x_1,\ldots,x_4)\), put
\(T_i=\partial_{x_i}\) and let \(q_i\) be its derivation degree for
the \(s\)-degree filtration:

\[
q_i=\sup_{0\ne f\in B}\{\deg_s(T_i f)-\deg_s f\}.
\]

The supremum is finite and attained on a finite generating set of
\(K\), together with \(s\). Always \(q_i\ge-1\). The filtration is
intrinsic to \(E\): \(\deg_s f\) is the LND degree of \(f\) for \(E\).
Replacing the slice by \(s+h\), \(h\in K\), does not change it.

The associated-graded LND argument gives the following dichotomy,
as proved in [intrinsic-actions-pass.md](intrinsic-actions-pass.md).
If \(q_i=-1\), then \(T_i=fE\) for \(f\in K\). A coordinate
partial has a slice, so \(f\) is a unit, hence a nonzero constant.
Thus \(K=\ker T_i\simeq\mathbb C^{[3]}\). Otherwise \(q_i\ge0\)
and

\[
\widehat T_i=s^{q_i}\delta_i,\qquad
0\ne\delta_i\in\operatorname{LND}(K).
\tag{1}
\]

The top term on \(s\) vanishes because an LND cannot send a nonzero
element to a nonzero multiple of itself. In particular
\(\deg_sT_i(s)\le q_i\), not \(q_i+1\).
Homogenization of LNDs is discussed in
[Alhajjar, Sections 1.2 and 3](https://arxiv.org/pdf/1501.00445).

Define

\[
H(x)=\sum_{i=1}^4(q_i+1),\qquad
H_{\min}(E)=\min_{\text{all polynomial coordinate frames }x}H(x).
\tag{2}
\]

At most one independent coordinate partial can have degree \(-1\):
all such partials are constant multiples of \(E\). Hence \(H(x)\ge3\),
and the integer minimum in (2) exists. It is unchanged by conjugating
the cylinder decomposition by an automorphism of \(B\).

If \(K=\mathbb C[a,b,c]\), the adapted frame \((a,b,c,s)\) has
degrees \((0,0,0,-1)\), so \(H_{\min}=3\). Conversely \(H=3\)
requires a degree-\(-1\) partial and therefore a polynomial kernel.
Thus

\[
H_{\min}(E)=3\quad\Longleftrightarrow\quad K\simeq\mathbb C^{[3]}.
\tag{3}
\]

Equation (3) is a characterization, not a proof that the minimum is
three. Well-ordering supplies a minimizer but gives no operation that
decreases its height.

## 2. The stronger low-height closure

If \(q_i=0\), then \(T_i(K)\subseteq K\) and \(T_i(s)\in K\).
Consequently

\[
[T_i,E]=0.
\tag{4}
\]

Suppose two coordinate partials, say \(T_1,T_2\), have degree zero.
Their common kernel is the coordinate-plane algebra

\[
R=\ker T_1\cap\ker T_2=\mathbb C[x_3,x_4].
\]

Commutation (4) makes \(R\) stable under \(E\). Its restriction is
an LND. If this restriction is zero, \(x_3\) is an ambient coordinate
in \(\ker E\). Otherwise Rentschler's theorem supplies a coordinate
\(p\) of \(R\) with \(E(p)=0\); it remains a coordinate in \(B\).
The exact planar triangularization statement is recalled in
[Dasgupta--Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).

The kernel \(K\) is regular, since the polynomial extension \(K[s]\)
is regular. An LND on a four-variable polynomial ring fixing an
ambient coordinate and having regular kernel has polynomial kernel
over that coordinate ring, by
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1).
Its nonzero-derivation hypothesis holds because \(E(s)=1\).
Thus two degree-zero coordinate partials already imply
\(K\simeq\mathbb C^{[3]}\).

A second closing condition is stronger: one degree-zero partial and
one degree-one partial suffice, regardless of the remaining degrees.
The needed three-variable statement is the following single-partial
lemma, independently audited in
[height-seven-audit.md](height-seven-audit.md).

**Single-partial lemma.** Let \(D\) be an LND of
\(R=\mathbb C[y_1,y_2,y_3]\). If
\(\operatorname{ad}_D^2(\partial_{y_1})=0\), then \(D\) fixes an
ambient coordinate of \(R\).

For a proof, the case \(D=0\) is immediate. Otherwise set
\(W=[D,\partial_{y_1}]\). The conjugate
\[
\exp(tD)\partial_{y_1}\exp(-tD)=\partial_{y_1}+tW
\]
is an LND of \(R[t]\), fixing \(t\). For any \(f\in R\), the
coefficient of \(t^m\) in its \(m\)-th iterate on \(f\) is
\(W^m(f)\). Local nilpotence therefore makes \(W\) an LND, and the
hypothesis says \([D,W]=0\).

If \(D,W\) are independent over \(\operatorname{Frac}R\), they have
distinct kernels. Their common kernel contains an ambient coordinate
by [Dasgupta--Gaifullin, Proposition 2.14](https://arxiv.org/pdf/2306.00510).
It remains to handle the dependent case, including \(W=0\).
Write \(D=gD_0\), where \(g\) is the gcd of its polynomial
coefficients and \(D_0=\sum a_j\partial_{y_j}\) has coefficient gcd
one. Since \(g\mid D(g)\), the LND divisibility property gives
\(D(g)=0\); hence \(D_0\) is also an LND and has the same kernel.
Dependence gives
\(\partial_{y_1}a_j=h a_j\) for one rational function \(h\).
The denominator of \(h\) divides every \(a_j\), so \(h\in R\).
A nonzero polynomial cannot divide its nonzero partial derivative
with respect to \(y_1\), by degree. Thus \(h=0\), and every
\(a_j\) is independent of \(y_1\). Now \(D_0\) preserves the
polynomial plane \(\mathbb C[y_2,y_3]\). A zero restriction fixes
\(y_2\); a nonzero restriction fixes a plane coordinate by Rentschler.
Either coordinate is ambient in \(R\) and lies in \(\ker D\).
No irreducibility hypothesis on \(D\) is needed.

To apply the lemma, suppose \(q_1=0\) and \(q_2=1\).
Commutation (4) makes the polynomial three-ring
\(R=\ker T_1=\mathbb C[x_2,x_3,x_4]\) stable under \(E\).
Both \(T_2\) and \(E\) preserve \(R\). The degree-one bounds give
\(\deg_s T_2(f)\le1\) for \(f\in K\) and
\(\deg_s T_2(s)\le1\), so
\(\operatorname{ad}_E^2(T_2)=0\) on the generators \(K,s\), and
therefore on \(B\). Restriction to \(R\) invokes the lemma for
\(D=E|_R\). Its invariant coordinate is also ambient in \(B\).
Regularity of \(K\) and Bhatwadekar--Gupta--Lokhande again finish.

If there is no degree-\(-1\) partial and \(H\le7\), then
\(\sum q_i\le3\). There are either at least two degree-zero
partials, or the sorted pattern is \((0,1,1,1)\). Thus

\[
H(x)\le7\quad\Longrightarrow\quad K\simeq\mathbb C^{[3]},
\qquad
K\not\simeq\mathbb C^{[3]}\quad\Longrightarrow\quad H_{\min}(E)\ge8.
\tag{5}
\]

More precisely, a hypothetical nonpolynomial kernel permits neither
two degree-zero partials nor a pair of degrees zero and one. A frame
containing a degree-zero partial must consequently have its other
three degrees at least two, and hence height at least ten. The only
remaining sorted patterns at this checkpoint were respectively
\((1,1,1,1)\) and \((1,1,1,2)\). The first is now closed by the
[height-eight theorem](height-eight-algebra-pass.md); the second
remains outside the proved result.

The single-partial hypothesis is not interchangeable with
\(D^3(y_j)=0\). For example,
\[
D=\partial_a+a\partial_b+(b+a^2/2)\partial_c
\]
satisfies \(\operatorname{ad}_D^2(\partial_i)=0\) for all three
coordinate partials, but \(D^3(c)=2\). Its only invariant affine-linear
polynomials are constants, whereas \(b-a^2/2\) is an invariant
polynomial coordinate. Thus the closure neither asserts cubic
nilpotence on the original generators nor an invariant linear form.

The intrinsic leading rank can nevertheless be one at height six.
The frame
\[
(a,b,c+(a+b)s,s)
\]
has degrees \((1,1,0,0)\) and leading intrinsic directions
\[
-\partial_c,\ -\partial_c,\ \partial_c,\ -(a+b)\partial_c.
\]
Therefore the closure in (5) is stronger than merely counting
independent leading directions.

## 3. Rank three across all frames is another equivalent endpoint

The derivations \(\delta_i\) in (1) commute. If three are independent
over \(\operatorname{Frac}K\), their flows give a three-dimensional
orbit of \(\mathbb G_a^3\) on \(\operatorname{Spec}K\). It is open
and, by closedness of unipotent-group orbits on affine varieties,
closed. Irreducibility makes it the whole threefold. Its stabilizer
is trivial, so \(K\simeq\mathbb C^{[3]}\).
The closed-orbit theorem is recalled in
[Arzhantsev, Introduction](https://arxiv.org/html/2102.11330v1).

Conversely, if \(K=\mathbb C[a,b,c]\), the frame
\((a+s,b,c,a-s)\) has four degree-zero partials whose leading
intrinsic directions span rank three. Therefore

\[
\text{some frame has intrinsic leading rank three}
\quad\Longleftrightarrow\quad K\simeq\mathbb C^{[3]}.
\tag{6}
\]

No universal rank-two frame theorem is established here. A weaker
useful count is that \(m_0\) degree-zero partials have intrinsic
rank at least \(m_0-1\): restriction of independent derivations to
\(K\) loses at most the one-dimensional vertical direction.
That count is not substituted for the stronger two-partial argument
in Section 2.

## 4. Which row cancellations are actual elementary frame changes?

An elementary coordinate change has the form
\[
y_j=x_j+P(x_1,\ldots,\widehat{x_j},\ldots,x_4),\qquad
y_i=x_i\quad(i\ne j).
\]
Its coordinate partials are exactly
\[
U_j=T_j,\qquad U_i=T_i-(T_iP)T_j\quad(i\ne j).
\tag{7}
\]

Thus the coefficients of a proposed row cancellation cannot be
chosen independently. If \(h_i=T_iP\), they satisfy
\[
T_jh_i=0,\qquad T_ih_k=T_kh_i\quad(i,k\ne j).
\tag{8}
\]
Conversely these polynomial conditions allow integration to such a
\(P\), up to a constant, in the three coordinates other than \(x_j\).
This is the elementary polynomial closed-one-form calculation in
characteristic zero.

A concrete sufficient certificate for strict height descent is:
choose \(j,P\) as above so that for every nonzero \(T_iP\),
\[
\deg_s(T_iP)+q_j\le q_i,
\]
and at least one highest symbol cancels in (7). Then no partial
degree increases and at least one decreases, hence \(H(y)<H(x)\).

Generic dependence of the \(\delta_i\) only gives coefficients in
\(\operatorname{Frac}K\). It does not give polynomial coefficients
with (8), or a simultaneous degree bound for all modified partials.
Clearing denominators is not an invertible coordinate operation.
Even polynomial row cancellations can fail to preserve local
nilpotence, as Section 6 shows.

Minimizing over all frames also differs from minimizing over a
chosen elementary orbit. No assertion that elementary changes
generate every automorphism of \(\mathbb C^{[4]}\) is used.

## 5. Exact elementary repairs of the existing controls

Each listed replacement is made in the current coordinates. All
other coordinates are retained. Let \(r=a-sb\) in the third example.

| Initial frame | Elementary replacements | Heights | Intrinsic ranks |
| --- | --- | --- | --- |
| \((a-(b+a^2s)-(c+bs)-s,\ b+a^2s,\ c+bs,\ s)\) | \(x_1\leftarrow x_1+x_2+x_3+x_4\); \(x_3\leftarrow x_3-x_2x_4+x_1^2x_4^2\); \(x_2\leftarrow x_2-x_1^2x_4\) | \(12,8,5,3\) | \(1,1,2,3\) |
| \((a+s^2,\ b+as,\ c+bs,\ s+(a+s^2)^2)\) | \(x_4\leftarrow x_4-x_1^2\); \(x_1\leftarrow x_1-x_4^2\); \(x_3\leftarrow x_3-x_2x_4+x_1x_4^2\); \(x_2\leftarrow x_2-x_1x_4\) | \(13,10,8,5,3\) | \(1,1,1,2,3\) |
| \((a-csr,\ b-cr,\ c,\ s)\) | \(x_1\leftarrow x_1-x_4x_2\); \(x_2\leftarrow x_2+x_3x_1\); \(x_1\leftarrow x_1+x_4x_2\) | \(11,8,5,3\) | \(1,1,2,3\) |

Every sequence ends at \((a,b,c,s)\). The maximum total degrees
of the elementary substitutions are respectively four, three, and
two. These are finite exact repairs on rings whose polynomial
structure was already specified. They do not prove the existence
of analogous repairs on an unknown \(K\).

## 6. A degree-lowering row cancellation that is not an LND

For the second frame in Section 5, use its first and fourth
coordinate partials from
[verify_global_filtration.py](../verify_global_filtration.py).
They have degrees five and three, with top symbols
\(4s^5\partial_c\) and \(-2s^3\partial_c\). The polynomial
combination

\[
W=T_1+2s^2T_4
\]

cancels degree five and has degree three. However, it preserves
\(\mathbb C[a,s]\) and restricts there to

\[
W(a)=1+4as,\qquad W(s)=-2a.
\]

For the ordinary total-degree filtration on \(\mathbb C[a,s]\),
the highest derivation is \(4as\partial_a\). Its iterates satisfy
\[
(4as\partial_a)^n(a)=(4s)^n a\ne0.
\]
It is not locally nilpotent. Since a highest derivation of an LND
would be locally nilpotent, neither the restriction nor \(W\) is
an LND. Also \([W,T_4]=-4sT_4\ne0\).

This invalid row cancellation is not a counterexample to the
existence of some valid decreasing frame change. It shows why
lowering a row's filtration degree does not itself certify one.

## 7. A flow-twisted frame with a primitive rank-three LND

Here rank three for one LND means that its kernel contains no
ambient coordinate of the three-variable polynomial ring. This is
different from the generic rank of a collection of vector fields.

Take \(K=\mathbb C[a,b,c]\) and an irreducible rank-three LND
\(\delta\). Extend it to kill \(s\), and put
\[
\alpha=\exp(s\delta)\in\operatorname{Aut}(K[s]),\qquad
X_i=\alpha(a_i)\ (a_1=a,a_2=b,a_3=c),\quad X_4=s.
\]
The flow is polynomial and has inverse \(\exp(-s\delta)\). Its
coordinate partials are
\[
T_i=\alpha\partial_{a_i}\alpha^{-1}\quad(i\le3),
\qquad T_4=E-\delta.
\tag{9}
\]

Expand \(T_i=\sum_{j=0}^{N_i}s^jD_{ij}\). This sum is finite
because (9) is a polynomial derivation. Differentiating in \(s\)
gives \(\partial_sT_i=[\delta,T_i]\), so
\[
[\delta,D_{iN_i}]=0.
\]
The highest coefficient is a nonzero LND on \(K\) by (1).

For an irreducible rank-three LND on \(\mathbb C^{[3]}\), every
nonzero commuting LND has the same kernel. This is exactly
[Dasgupta--Gaifullin, Theorem 4.5(i); equivalence is defined in
Definition 2.3](https://arxiv.org/pdf/2306.00510).
It yields \(D_{iN_i}=f_i\delta\) with
\(f_i\in\operatorname{Frac}K\). Irreducibility of \(\delta\)
means its three polynomial coefficients have gcd one. Since the
coefficients of \(D_{iN_i}\) are polynomial, the denominator of
each \(f_i\) divides all three coefficients of \(\delta\), hence
is a unit. Thus \(f_i\in K\); commutation implies
\(\delta(f_i)=0\).

The fourth top direction is \(-\delta\). Consequently all four
leading intrinsic fields have generic rank one, and dividing the
polynomial coefficient gcd of each leaves a nonzero constant
multiple of \(\delta\).

Each \(N_i\) for \(i\le3\) is at least two. If \(N_i\le1\),
the flow-conjugation expansion (9) would give
\(\operatorname{ad}_{\delta}^2(\partial_{a_i})=0\); the
single-partial lemma would contradict rank three. Thus this frame
has only one degree-zero partial, \(T_4\), and height at least ten.
Its minimum over all frames nevertheless remains three.

For the concrete Freudenburg example, take
\[
f=ac-b^2,\qquad g=cf^2+2a^2bf+a^5,\qquad
\delta=\operatorname{Jac}(f,g,\cdot).
\]
Its rank-three property and local-slice construction are treated
in [Dasgupta--Gaifullin, Section 5](https://arxiv.org/pdf/2306.00510).
Direct symbolic calculation verifies that its coefficient gcd is
one and that all coefficients vanish at the origin. Every primitive
leading field above therefore retains that fixed point and cannot
have a slice.

This is stronger than the earlier common top \(2a\partial_c\),
whose primitive normalization is a translation. It still concerns
one selected frame on \(K=\mathbb C^{[3]}\). The polynomial
automorphism \(\alpha^{-1}\) recovers an adapted frame. No bounded
elementary factorization or height-decreasing factorization of this
inverse is asserted.

## 8. Exact remaining statement

A sufficient missing descent lemma would say: whenever no known
closing condition holds, some polynomial coordinate change strictly
decreases \(H\). In view of (5), iteration would terminate in a
closing frame. Neither the rank-one relations nor the existence of
the minimum proves this statement.

The tests establish finite repairs and explicit failures of
uncertified row cancellation. The flow-twisted example additionally
rules out automatic repair by primitive normalization. They do not
show that all frames can remain rank one on any nonpolynomial
cancellation kernel, or establish a universal rank-two frame.

## 9. Reproducible checks and source scope

The independent helper [frame_height_checks.py](frame_height_checks.py)
imports SymPy and the Python standard library, not the project's
research modules. Run

    /opt/anaconda3/bin/python research/frame_height_checks.py

All sixteen tests passed. They check the elementary repair sequences,
their Jacobians and coordinate-partial pairings, commutators,
height/rank profiles, the degree-zero commutation controls, the
invalid degree-lowering combination, and the coefficient gcd and
fixed point of the Freudenburg derivation. Six additional controls
check double commutators, the distinction from cubic nilpotence on
generators, a reducible dependent-commutator example, and an explicit
height-seven frame. They do not numerically
certify the universal height bound, the centralizer theorem, or
Freudenburg's rank-three theorem.

The geometric closures used above were checked in their exact
primary-source scope: Rentschler is used on a polynomial plane,
Bhatwadekar--Gupta--Lokhande is used only after finding an ambient
coordinate invariant and proving regularity of the kernel, and
Dasgupta--Gaifullin's commuting-pair result is used only on a
polynomial three-ring, while its rank-three centralizer theorem is
used with an irreducible rank-three LND on the explicitly polynomial
ring \(\mathbb C[a,b,c]\). None of these three-variable conclusions
is transferred to an unidentified stably polynomial kernel.
