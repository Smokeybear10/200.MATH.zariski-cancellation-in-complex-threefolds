# Lower-rank orbit geometry at height eight

**Later closure:** [height-eight-algebra-pass.md](height-eight-algebra-pass.md),
independently audited in [pass12-full-proof-audit.md](pass12-full-proof-audit.md),
now closes the lower-rank branches under the full double-commutator
hypothesis. It does not require full group rank or freeness of the displayed
fields. The exploratory limitations below record the earlier orbit-only
approach; they are not the current boundary of the height-eight theorem.

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=K[s],\qquad E=\partial_s,
\qquad [E,[E,T_i]]=0,\quad T_i=\partial_{x_i}.
\]
Put \(W_i=[E,T_i]\). As proved in
[height-seven-audit.md](height-seven-audit.md), the \(W_i\) are LNDs,
commute with \(E\), and commute with one another. Let \(r\) be the generic
rank of \(E,W_1,\ldots,W_4\). The case \(r=4\) closes cancellation by
the transitive vector-group action. This note studies \(r=2,3\).

The rank-three case has a faithfully flat common quotient to an affine
line, with integral surface fibers and general fiber \(\mathbb A^2\).
The missing step is control of finitely many possible degenerate fibers.
Actual height-eight coordinate frames can have lower orbit rank along a
nonempty locus, so freeness of the displayed action is not automatic.
Neither lower-rank case is closed here.

## 1. Passing from ambient fields to intrinsic fields

The \(W_i\) need not kill the chosen slice. Since they commute with \(E\),
they have unique decompositions
\[
W_i=d_i+f_iE,\qquad d_i\in\operatorname{LND}(K),\quad f_i=W_i(s)\in K,
\]
where \(d_i\) is extended to kill \(s\). Restriction to \(K\) gives local
nilpotence and
\[
[d_i,d_j]=0,\qquad d_i(f_j)=d_j(f_i).
\]
Consequently the generic rank of the intrinsic collection is \(r-1\).
One must not silently identify \(W_i\) with \(d_i\) before removing its
vertical component.

The [intrinsic quotient theorem](intrinsic-quotient-surface-pass.md),
derived from
[Kaliman and Saveliev, Lemma 2.1 and Corollary 2.8](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
applies to every nonzero \(d_i\): its kernel is \(\mathbb C^{[2]}\), and
its quotient is surjective and faithfully flat with curve fibers.
An intrinsic field without fixed points would close cancellation.

## 2. Total rank three: an exact common-quotient reduction

Suppose the intrinsic rank is two. Choose two of the \(d_i\), called
\(d_1,d_2\), independent over \(\operatorname{Frac}K\). Their commuting
flows define a generically free \(\mathbb G_a^2\)-action on
\(X=\operatorname{Spec}K\).

Set \(A_1=\ker d_1\cong\mathbb C^{[2]}\). The restriction of \(d_2\)
to \(A_1\) is nonzero. Otherwise both derivations kill the same
transcendence-degree-two field and are proportional on the remaining
one-dimensional rational extension, contrary to independence.
Rentschler's theorem therefore gives coordinates \(f,t\) of \(A_1\)
such that
\[
A_1=\mathbb C[f,t],\qquad d_2|_{A_1}=p(f)\partial_t,
\quad p\in\mathbb C[f]\setminus\{0\}.
\]
The plane theorem is recalled in
[Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).
In particular
\[
\ker d_1\cap\ker d_2=\mathbb C[f].
\]
Every other \(d_i\) lies in their fraction-field span and hence kills
\(f\). Thus the common intrinsic and ambient invariant rings are
\[
\bigcap_i\ker(d_i|_K)=\mathbb C[f],\qquad
\ker E\cap\bigcap_i\ker W_i=\mathbb C[f].
\]
The same argument with any nonzero \(d_i\) and an independent partner
shows that \(f\), up to a scalar affine change, is a coordinate of that
individual affine-plane kernel. This is not yet an ambient coordinate of
\(B\), or a coordinate of \(K\).

There are several unconditional geometric consequences.

1. The map \(f:X\to\mathbb A^1\) is surjective and faithfully flat. It
   factors as the faithfully flat quotient \(X\to\operatorname{Spec}A_1\)
   followed by the coordinate projection \((f,t)\mapsto f\).
2. Every \(f-\lambda\) is prime in \(K\). The common invariant ring is
   factorially closed in the UFD \(K\), and \(f-\lambda\) is irreducible
   in \(\mathbb C[f]\). It is not a unit, since \(K^*=\mathbb C^*\).
   Hence every fiber \(Y_\lambda\) is a nonempty integral surface.
3. Base change of the first quotient gives a faithfully flat map
   \(Y_\lambda\to\mathbb A^1_t\) with curve fibers. This does not make
   \(Y_\lambda\) smooth or make those curves reduced.
4. The general \(Y_\lambda\) is \(\mathbb A^2\). The precise source is
   [Derksen, van den Essen, Finston and Maubach, Theorem 2(1)](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.35.pdf).

For the fixed pair \(d_1,d_2\), if the pair has rank two at even one
point of \(Y_\lambda\), its orbit is two-dimensional and closed.
Since the fiber is irreducible of dimension two, the orbit is the entire
fiber. Its vector-group stabilizer is trivial, so the fiber is
\(\mathbb A^2\), and the pair has rank two everywhere on it. The same
paper's Theorem 3(1) shows that the alternative, rank at most one
everywhere, can occur for only finitely many \(\lambda\).

Thus the rank-drop locus for this pair is a finite union of whole
fibers. Showing it empty would suffice. It is not made empty by the
individual quotient theorem.

### A source-scope warning

The abstract of the 2011 paper states a stronger product conclusion from
one point with trivial isotropy than its actual Theorem 2 provides.
Theorem 2(1) gives general affine-space fibers; Theorem 2(2) assumes a
globally free action for the product conclusion. Its Example 2 already
distinguishes these hypotheses. This note uses the numbered theorems,
not that stronger reading of the abstract.

## 3. Total rank two: replicas over an affine-plane quotient

Suppose the intrinsic rank is one. All nonzero \(d_i\) have the same
kernel \(A\cong\mathbb C^{[2]}\). There is a primitive LND \(\delta\)
on \(K\), with this kernel, such that
\[
d_i=h_i\delta,\qquad h_i\in A.
\]
For precision, choose finitely many algebra generators of \(K\) and
divide one nonzero \(d_i\) by the gcd of its values on them. The gcd is
invariant, so the divided derivation is still locally nilpotent. Every
other \(d_i\) is fraction-field proportional to it; prime valuations of
the primitive values show that the multiplier is polynomial. Equality
of kernels and commutation make the multiplier invariant.

The common quotient is therefore the faithfully flat affine-plane
quotient of \(\delta\). Its fixed-point ideal need not be the unit
ideal. In fact the derivative ideal of the displayed collection is
\[
\left(\sum_i d_i(K)\right)K
=(h_1,\ldots,h_4)K\cdot(\delta(K))K.
\]
Neither factor is automatically a unit ideal. Even with an already
polynomial \(K\), the primitive field
\(x\partial_y+2y\partial_z\) has affine-plane faithfully flat quotient
and a nonempty fixed locus. Adjoining \(E=\partial_s\) gives the relevant
rank-two commuting orbit data. This last example alone is not asserted
to arise as the full commutator collection of a height-eight frame.

## 4. Genuine height-eight controls

These controls do satisfy the full constant-coordinate-partial premise.
They show rank drop for the displayed group on polynomial cylinders,
without claiming a nonpolynomial kernel or failure of all repairs.

Work first in \(\mathbb C[a,b,c,d]\), with constant partials \(P_a,P_b,P_c,P_d\).
Replace their basis by
\[
(T_1,T_2,T_3,T_4)
=(P_a+P_b,\ P_c+P_b,\ P_d+P_b,\ P_b).
\]
These are the coordinate partials dual to
\[
(x_1,x_2,x_3,x_4)=(a,c,d,b-a-c-d).
\]

### Rank two

Take
\[
E=P_a+(b^3+c^3)P_d,
\qquad s=a,\qquad v=d-a(b^3+c^3).
\]
Then \(K=\mathbb C[b,c,v]\), and the only nonzero original commutators
are
\[
[E,P_b]=-3b^2P_d,\qquad [E,P_c]=-3c^2P_d.
\]
They commute with \(E\) and with each other. The total generic rank is
two, but all induced intrinsic fields vanish along \(b=c=0\).
Each \([E,T_i]\) is nonzero; direct substitution in \(K[a]\) gives
\(q_i=1\) for all four transformed partials. This is a height-eight frame.

### Rank three

Take
\[
E=P_a+b^2P_c+b^2cP_d,
\qquad s=a,
\]
with polynomial invariants
\[
v=c-ab^2,
\qquad w=d-ab^2c+\frac{a^2b^4}{2}.
\]
The inverse is
\[
c=v+ab^2,\qquad d=w+ab^2v+\frac{a^2b^4}{2},
\]
so \(K=\mathbb C[b,v,w]\). The commutators are
\[
[E,P_b]=-2b(P_c+cP_d),\qquad [E,P_c]=-b^2P_d,
\qquad [E,P_a]=[E,P_d]=0.
\]
All double commutators vanish. The total generic rank is three, whereas
all the intrinsic commutators vanish on the entire divisor \(b=0\).
Their nonzero restrictions to \(K\) are
\[
d_b=-2b(\partial_v+v\partial_w),\qquad d_c=-b^2\partial_w.
\]
Again the displayed constant basis change gives \(q_i=1\) for every
\(T_i\). The common quotient is \(b\); every fiber is already an affine
plane, despite the displayed pair losing rank on the zero fiber.
Dividing coefficient factors yields free fields and repairs the action
in this example. The control does not disprove the existence of such a
repair in general.

A standalone inline SymPy calculation verified 47 exact controls for
these two families: slice and invariant identities, double commutators,
pairwise commutation, common vanishing, generic matrix ranks, invertibility
of the constant basis, and all four filtration degrees. They passed in
0.108 seconds under SymPy 1.13.3. This finite check does not prove a
classification of all frames or certify the cited geometric theorems.

## 5. The remaining constant-frame input

For the rank-three common invariant \(f\), the original commutator
identities give an extra condition not present in arbitrary commuting
actions:
\[
E(f)=0,\qquad W_i(f)=0
\quad\Longrightarrow\quad E(T_i f)=0\quad\text{for every }i.
\]
Thus every original first partial derivative of \(f\) lies in \(K\).
This is a genuine additional algebraic constraint. It has not been
converted here into an ambient-coordinate theorem, a globally free
intrinsic field, or elimination of the exceptional common-quotient fibers.

The result of this pass is therefore a lower-rank quotient reduction and
two exact height-eight degeneration controls. No conclusion that all
height-eight actions cancel, or that a counterexample exists, is drawn.
