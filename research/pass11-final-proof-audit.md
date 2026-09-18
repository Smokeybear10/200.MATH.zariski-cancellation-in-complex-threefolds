# Final proof-scope audit of structural pass eleven

This is a bounded independent audit of
[deep-pass-11.md](../deep-pass-11.md) and
[height-seven-audit.md](height-seven-audit.md), concentrating on the
single-partial lemma, intrinsic quotient flatness, and the primitive
flow-twisted control. No mathematical error was found in those arguments.
Their conclusions depend on the cited classification theorems. This is
not formal verification, human peer review, or a claim of novelty.

## 1. Single-partial lemma and its height consequence

The implication
\[
D\in\operatorname{LND}(\mathbb C[x,y,z]),\qquad
[D,[D,\partial_x]]=0
\quad\Longrightarrow\quad
\ker D\text{ contains an ambient coordinate}
\]
is justified by the supplied proof, including the dependent case.

Put \(W=[D,\partial_x]\). The assertion that \(W\) is locally nilpotent
uses the exact conjugation identity on \(R[t]\), not a false general rule
about brackets of LNDs. All derivations kill \(t\), so the coefficient of
\(t^N\) in \((\partial_x+tW)^Nf\) is precisely \(W^Nf\). Local
nilpotence of the conjugate therefore proves local nilpotence of \(W\).

For independent \(D,W\), the ambient-coordinate conclusion is exactly
the applicable three-variable commuting-LND theorem. In particular,
[Maubach, Theorem 3.6](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf)
does not require both derivations to be irreducible. The distinct-kernel
formulation used in the main report is equivalent here: LNDs with the same
kernel become proportional after passing to its fraction field and a
local slice.

For dependent \(D,W\), dividing the coefficient vector of \(D\) by its
gcd is legitimate. The relation \(g\mid D(g)\) and local nilpotence imply
\(D(g)=0\), so the primitive derivation is again locally nilpotent with
the same kernel. Its coefficient ratios lie in \(\mathbb C(y,z)\).
The denominator argument in the height note correctly proves that a
primitive proportional vector can be chosen in \(\mathbb C[y,z]^3\),
and that the remaining scalar is a complex unit. It uses valuations at
irreducible polynomials. It does not confuse coefficient gcd one with
generation of the unit ideal.

The primitive derivation consequently preserves the coordinate plane
\(\mathbb C[y,z]\). Rentschler gives an invariant plane coordinate unless
the restriction is zero, which is even easier. This coordinate is ambient
in the three-variable ring, as required.

For the application, \(q_0=0\) makes the three-variable kernel of the
first coordinate partial \(E\)-stable. The second partial, of degree one,
has coefficients at most linear in \(s\) on both \(K\) and \(s\), so its
double commutator with \(E\) vanishes on all of \(K[s]\). The lemma thus
produces an ambient invariant coordinate, not just an abstract invariant
generator. Regularity of \(K\), which follows from \(K[s]\cong\mathbb C^{[4]}\),
supplies the additional hypothesis in
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1).
The conclusions for \((0,1,*,*)\), height at most seven, and the surviving
height-eight and height-nine patterns follow.

## 2. Affine-plane quotient and faithful flatness

The affine-three-plane restriction of the cylinder projection is used
only to establish dominance. Choosing a tangent complement to its kernel
gives full differential rank at one point; this does not assume a section,
surjectivity of the restriction, or birationality.

For every nonzero intrinsic LND, this domination verifies the extra
hypothesis in
[Kaliman and Saveliev, Corollary 2.8(2)](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf).
Their Lemma 2.1 supplies surjectivity and nonempty curve fibers. Thus the
base is \(\mathbb A^2\). The flatness deduction does not follow merely
from that identification: it also uses those fiber dimensions.

At a closed point of a fiber, the regular source local ring has dimension
three and the regular base local ring has dimension two. The two fiber
equations have height two, and their quotient has local dimension one.
This is exactly the Cohen--Macaulay dimension identity required by
[miracle flatness, Stacks Tag 00R4](https://stacks.math.columbia.edu/tag/00R4).
The flat locus is open and contains every closed point, hence is the whole
finite-type complex variety. Together with surjectivity, this gives
faithful flatness.

No reducedness or connectedness of every fiber is asserted or needed.
The example \(d=x\partial_y+2y\partial_z\) genuinely has disconnected
and nonreduced special fibers. Its no-retraction obstruction concerns the
actual invariant inclusion: reduction of \(xZ-Y^2=v\) modulo \(x\)
requires a polynomial square of odd degree. This is an arbitrary-degree
argument, independently of any finite regression tests.

## 3. Primitive flow-twisted control

For \(\alpha=\exp(s\delta)\), the transformed partial in the fourth
coordinate is \(E-\delta\), with the displayed sign. Each other transformed
partial kills \(s\) and satisfies
\(\partial_sT_i=[\delta,T_i]\). Therefore its nonzero highest coefficient
is both an LND and a commuting partner of \(\delta\).

[Dasgupta and Gaifullin, Theorem 4.5(i)](https://arxiv.org/pdf/2306.00510)
applies to an irreducible rank-three LND on the three-variable polynomial
ring. It gives equality of kernels for each nonzero commuting LND, hence
fraction-field proportionality. The report correctly upgrades
\(f_i\delta\) to a polynomial multiple using coefficient gcd one and
prime valuations. Commutation then gives \(\delta(f_i)=0\). Dividing by
the coefficient gcd leaves a scalar multiple of \(\delta\).

The fixed origin of Freudenburg's displayed derivation consequently
persists for every primitive leading field. Rank three is a sourced
property of that derivation, not a consequence of the coefficient test.
Also, a conjugation degree at most one for any of the first three
partials would trigger the single-partial lemma and contradict rank
three. Their degrees are at least two; the fourth degree is zero, so
this selected frame has height at least ten.

This is a valid obstruction to primitive-leading-field simplification.
It is not an obstruction to all frame changes: the inverse flow restores
an adapted frame on this already polynomial kernel.

## 4. Exact remaining scope

The audit finds no mathematical correction necessary in the three target
arguments. The residual issue is global, not a missing verification of
the displayed identities: no free intrinsic action, qualifying low-height
frame, universal decreasing move, or finite upper height bound has been
constructed for an arbitrary stably polynomial threefold algebra.

The height-eight full-rank commuting-action argument is conditional.
Its Riccati identities do not establish that full rank occurs, and a
new formula for a slice of \(E\) would not establish that the slice is an
ambient coordinate. Both notes retain these distinctions.

The parent report records 253 passing tests in nineteen suites. This audit
does not independently rerun or certify that aggregate count. Finite exact
checks support their stated polynomial controls; they do not verify the
topological or classification inputs and do not close cancellation.
