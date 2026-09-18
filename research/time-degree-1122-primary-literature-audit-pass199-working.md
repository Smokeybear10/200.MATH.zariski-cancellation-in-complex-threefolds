# Bounded primary-literature applicability audit for the 1122 branches

Date: 2026-09-15. Status: a limited source audit, not a novelty search or
mathematical certification. This note is separate from the pass198 packet.

Result: none of the statements checked below proves recognition from
the supplied time profile \((1,1,2,2)\) and full initial kernel
\((Z^2-X^3Y)\) alone. There are strong published endpoints after an
actual invariant coordinate or a polynomial three-ring has been
established. Those extra hypotheses are precisely what cannot be
silently inferred from the generic coefficient field.

## Search boundary and degree terminology

Six search queries were used, without external outreach:

1. locally nilpotent derivation four variables "D^3" "D^2" cancellation slice
2. locally nilpotent derivations "quasi-nice" four variables slice
3. locally nilpotent derivation "1,1,2,2"
4. "locally nilpotent" "four variables" "degree two"
5. "locally nilpotent" "slice" "quadratic" "four"
6. "nice derivations" "Wang" "D2"

The exact results, definitions and relevant proof passages below were
opened in primary papers. Search snippets and unrelated repositories
were not treated as theorem evidence. This was not a full-text search
of the mathematical literature. In particular, absence of a matching
result from these queries does not establish novelty.

The profile means \(E^2X=E^2Y=0\), \(E^3Z=E^3W=0\), with the preceding
derivatives nonzero. It does not bound ordinary coefficient degree.
For example, in independent \(s,t,z,w\), the actual coordinates
\[
X=s,\quad Y=t+s,\quad Z=z+s^2p(t),\quad W=w+s^2
\]
have exact profile1122 for \(E=\partial_s\) and any nonzero polynomial
\(p\). Their inverse is
\[
s=X,\quad t=Y-X,\quad z=Z-X^2p(Y-X),\quad w=W-X^2.
\]
Thus \(E(Z)=2Xp(Y-X)\) can have arbitrarily large ordinary degree.
This example only separates the degree notions; it is not asserted
to have the special initial kernel under investigation.

## 1. An invariant coordinate is a sufficient extra hypothesis

Bhatwadekar, Gupta and Lokhande, *Some K-theoretic properties of the
kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\)*,
Theorem 3.5, states the following mathematical implication:
\[
\operatorname{char}k=0,\quad
0\ne D\in\operatorname{LND}_{k[T]}(k[T,X,Y,Z]),\quad
A=\ker D\text{ regular}
\quad\Longrightarrow\quad A=k[T]^{[2]}.
\]
[Primary statement and proof](https://arxiv.org/html/1501.01438v1).

For the sliced problem, regularity follows from
\(A\simeq B/(u)\) and \(Eu=1\): the gradient of \(u\) cannot vanish.
The missing hypothesis is an **ambient polynomial coordinate**
\(T\) with \(DT=0\), not merely a nonconstant element of the kernel,
an algebraic coefficient \(q\), or a generic-line parameter.
Thus the theorem applies after pass197's actual inverse has established
invariant coordinates, but does not replace that inverse or imply
pass198's impossibility statements.

## 2. Nice and two-good theorems have narrower coordinate hypotheses

Dasgupta and Gupta, *Nice derivations over principal ideal domains*,
Corollary 3.8, assumes characteristic zero, irreducible \(D\) on
\(k[X_1,X_2,X_3,X_4]\), and
\[
DX_1=0,\qquad D^2X_2=D^2X_3=D^2X_4=0;
\]
its conclusion is \(\ker D\simeq k^{[3]}\).
[Primary PDF, printed pp.7 and9](https://arxiv.org/pdf/1701.03635v1).

The same paper's Theorem 4.1 states Wang's classification for
irreducible nonzero \(D\) on **\(k[X,Y,Z]\)** with \(D^2X=D^2Y=0\).
Either a linear change \((L_1,L_2)\) of \((X,Y)\) gives
\(DL_1=0,\ DL_2\in k[L_1],\ DZ\in k[L_1,L_2]\), or an invariant
coordinate \(V\) satisfies \(k[X,Y,Z]=k[V,X,Y]\) and
\(DX,DY\in k[V]\).

Neither hypothesis is supplied by1122 on four generators.
Applying the three-variable theorem to an unknown kernel as though
it were already a polynomial three-ring would be circular.
The paper credits Wang, *Homogenization of locally nilpotent
derivations and an application to \(k[X,Y,Z]\)* (2005),
Theorem4.7/Remark5. The present audit read the precise primary
restatement, not Wang's original full article.

## 3. The recent image-ideal paper does not remove the invariant base

Dasgupta and Lahiri, *On image ideals of nice and quasi-nice
derivations on \(R[X_1,X_2]\)*, arXiv2302.13787, version6 dated
24 July2026, Theorem4.1:
\[
R\text{ a UFD},\quad B=R[X_1,X_2],\quad
D\in\operatorname{LND}_R(B)\text{ irreducible},\quad
D^2X_1=D^2X_2=0
\quad\Longrightarrow\quad
I_j=(DX_1,DX_2)^j\ker D.
\]
The ambient standing hypotheses include characteristic zero and
the specified affine base.
[Primary PDF, definitions and theorem](https://arxiv.org/pdf/2302.13787v6).

Theorem5.9 instead requires a PID base and prescribed triangular
form \(DX_1=\prod p_i^{r_i}\in R,\ DX_2=-f'(X_1)\), with additional
divisibility hypotheses for its higher-image-ideal formula.
These are image-ideal results over an already annihilated base.
Our two good coordinates are not annihilated, so taking
\(R=\mathbb C[X,Y]\) is invalid. A slice already makes every
\(I_j\) the unit ideal, as the paper observes; that fact alone
does not identify an unknown three-dimensional kernel.

## 4. Recent commuting-derivation classification also has a dimension gate

Dasgupta and Gaifullin, *On locally nilpotent derivations of polynomial
algebra in three variables*, Sbornik Mathematics216(4),2025:
Theorem4.5(i) says an irreducible LND of rank3 on \(k^{[3]}\) has
no nonzero commuting LND with a different kernel. Parts(ii)--(iii) describe
commuting derivations in ranks2 and1.
[Primary full text and theorem](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=sm&paperid=10094&option_lang=eng).

Its Corollary3.18 extends a construction to \(k^{[n]}\), but assumes
\(D(x_3)=\cdots=D(x_n)=0\) in an actual coordinate system.
It constructs a chain of irreducible commuting-derived LNDs with
coefficients over the invariant polynomial base.
It does not derive those fixed coordinates from two generators of
time degree1. The selected derivation on an as-yet unrecognized
kernel cannot be inserted into the three-variable theorem until
that kernel is known to be \(k^{[3]}\).

## Bounded conclusion

The checked statements do not subsume the supplied197 normalized
quadratic-projection recognition or198 reciprocal exclusions from
their starting hypotheses. The Bhatwadekar--Gupta--Lokhande endpoint
would give recognition once197's invariant-coordinate gate is proved,
but cannot give the reciprocal branch's nonexistence conclusion.

No checked theorem is stated in terms of the specific full initial
ideal \((Z^2-X^3Y)\), or the coefficient-field families \(f=\beta q\)
and \(f=\beta/q\). This is a report about these inspected statements,
not a claim that no other paper treats those cases.
No source, checker, proof assumption, or packet from198 or earlier
was changed. No checker was executed, imported, or compiled.

Source-read evidence for this audit: primary BGL3.5 at
turn4272view4; nice/two-good statements at turn4272view3 and
turn4273view1; image-ideal hypotheses at turn4274view2--5;
2025 commuting/rank statements at turn4277view0--2.
These identifiers record this audit's retrieval only.
