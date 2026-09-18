# Global recognition after an invariant local-slice modification

Private bounded pass 19, 2026-09-13 UTC. The new deduction here preserves
the entire derivation-degree associated graded algebra. It does not
recognize the modified ring as a polynomial ring. A concrete example
also disproves preservation of an arbitrary original affine-plane
fibration. The literature check below records exact sufficient
hypotheses, not an absence-based novelty claim. No expert review or Lean
verification is asserted.

## 1. Setup and the global question

Let
\[
R=\mathbb C^{[3]},\qquad 0\ne D\in\operatorname{LND}(R)
\text{ primitive},\qquad C=\ker D,
\]
\[
P_D=D(R)\cap C=pC,\qquad Dr=p,\qquad
0\ne V\in C,\qquad (p,V)C=C.
\]
The known three-variable kernel and plinth results give
\(C\cong\mathbb C^{[2]}\); the chosen \(r\) is a minimal local
slice. Set
\[
M=R[r/V],\qquad w=r/V.
\tag{1}
\]
The [exact pass-18 reduction](arbitrary-invariant-kernel-pass18.md)
proves
\[
M\cong R[w]/(Vw-r),\qquad M^{[1]}\cong\mathbb C^{[4]},
\tag{2}
\]
and the two charts
\[
M_V=R_V,\qquad R_p=C_p[r],\qquad M_p=C_p[w].
\tag{3}
\]
These are principal opens covering the invariant plane and their
inverse images. Consequently \(M\) is smooth. Stable polynomiality
also gives that \(M\) is a UFD, \(M^*=\mathbb C^*\), and the
underlying complex variety is contractible. For the last assertion,
\(\operatorname{Spec}M\) is a deformation retract of its product
with the contractible complex line, which is isomorphic to
\(\mathbb C^4\).

The question remains whether \(M\cong\mathbb C^{[3]}\) for every
input (1). It is essential that such an isomorphism may move the
embedded invariant plane. The
[pass-17 relative examples](danielewski-relative-pass17.md) already
give polynomial modifications not isomorphic to \(R\) over \(C\).
The observations below do not reinstate that false relative conclusion.

## 2. Every higher image ideal is preserved

### Proposition

The fraction-field derivation
\[
\Delta=VD
\]
restricts to a primitive locally nilpotent derivation of \(M\), with
\[
\Delta(w)=p,\qquad \ker_M\Delta=C,
\qquad P_\Delta=pC.
\tag{4}
\]
For every integer \(j\ge0\), its higher image ideals satisfy
\[
I_j(\Delta):=\Delta^j(M)\cap C
 =D^j(R)\cap C=:I_j(D).
\tag{5}
\]
In particular, for the derivation-degree filtrations,
\[
\operatorname{gr}_{D}(R)
 \cong_C\operatorname{gr}_{\Delta}(M)
\tag{6}
\]
as graded \(C\)-algebras. No assertion that the ideals \(I_j\)
are principal, and no Freeness hypothesis, is required.

### Proof

For \(a\in R\), \(\Delta(a)=V D(a)\in R\), whereas
\(\Delta(w)=p\). Thus the derivation preserves the generators of
\(M\). Since \(V\) is invariant,
\(\Delta^j(a)=V^jD^j(a)\), and \(\Delta^2(w)=0\).
Every generator is locally nilpotent, hence so is the derivation on
the finitely generated algebra.

On the two charts in (3), its kernels are respectively \(C_V\)
and \(C_p\), since on the latter chart
\(\Delta=p\partial_w\). Their intersection in
\(\operatorname{Frac}C\) is \(C\). Indeed, coprime \(p,V\)
cannot both clear a pole at any prime of the UFD \(C\). This proves
the kernel assertion.

Primitivity is local on this cover in the present UFD situation. On
the \(V\)-chart, \(VD\) is primitive because \(V\) is a unit
and \(D\) is primitive. On the \(p\)-chart, it takes the unit
value \(p\) on \(w\). More explicitly, a common divisor of all
values in \(M\) divides \(p=\Delta(w)\); it is a unit on each
of the two covering charts, and therefore a unit of \(M\).

Each \(I_j\) is an ideal of \(C\), because the derivation kills
coefficients in \(C\). Formation of this ideal commutes with
localization at a nonzero invariant element \(s\):
\[
(D^jR\cap C)_s=D^j(R_s)\cap C_s.
\tag{7}
\]
For the nontrivial inclusion, express an element of the right-hand
side as both \(c/s^e\) and \(D^j(a)/s^k\), with \(c\in C\)
and \(a\in R\). Clearing the two invariant denominators produces
a power of \(s\) times the element in
\(D^jR\cap C\). The same argument applies to \(\Delta\).

On the \(V\)-chart, (7) and \(\Delta^j=V^jD^j\) give
\[
I_j(\Delta)_V=V^jI_j(D)_V=I_j(D)_V.
\]
On the \(p\)-chart both ideals are the full ring \(C_p\):
\[
D^j(r^j)=j!p^j,\qquad \Delta^j(w^j)=j!p^j,
\]
which is a unit there. Equality of the ideals on the two comaximal
principal opens proves (5). Taking \(j=1\) also proves the plinth
assertion in (4).

Finally put \(F_j(D)=\ker D^{j+1}\), with \(F_{-1}=0\).
The normalized leading derivative
\[
F_j(D)/F_{j-1}(D)\longrightarrow C,
\qquad [a]\longmapsto D^j(a)/j!
\]
is injective and has image \(I_j(D)\). If \(D^j(a)\) is
invariant, then \(a\in F_j(D)\), so surjectivity onto that
ideal is immediate; the nonzero factorial does not change an ideal
over \(\mathbb C\). Leibniz's formula shows that these maps
respect graded multiplication. Therefore
\[
\operatorname{gr}_D(R)
 \cong \bigoplus_{j\ge0}I_j(D)T^j
 =\bigoplus_{j\ge0}I_j(\Delta)T^j
 \cong\operatorname{gr}_\Delta(M).
\]
This proves the proposition.

### What it does not prove

The equality in (6) only retains leading terms. It does not identify
the extension data of the filtered algebras, much less produce three
global polynomial generators. Combining this proposition with the
already-proved relative examples gives a concrete failure of the
implication
\[
\text{same graded algebra over }C
 \ \Longrightarrow\ \text{same filtered algebra over }C.
\]
It remains possible that a separate, nonrelative recognition theorem
could exploit these data. No such theorem is proved here.

## 3. An original coordinate can lose its affine-plane fibers

The following example lies in the solved
[polynomial-curve family](polynomial-curve-lift-pass18.md). Choose
\[
f=xz-y^2,\qquad r=x^2+yf^2,\qquad
h=(r^2+f^5)/x,
\]
\[
D=-\operatorname{Jac}(f,h,\cdot),\qquad
p=f^2h,\qquad V=1+fh.
\tag{8}
\]
Here \(h=zf^4+2xyf^2+x^3\) is polynomial. The family theorem
establishes that \(D\) is primitive, with kernel
\(\mathbb C[f,h]\) and minimal derivative \(Dr=f^2h\).
The identity
\[
p h+(1-fh)V=1
\tag{9}
\]
also verifies the required comaximality. In particular,
\(D+(1-fh)\partial_t\) has slice \(hr+Vt\), and its kernel
is \(M=R[r/V]\). The finite-jet family theorem proves that
this \(M\) is abstractly \(\mathbb C^{[3]}\).

The original \(x\) is a coordinate of \(R\) and an element of
\(M\), but \(M/(x)\) is not an affine plane. At \(x=0\),
\[
f=-y^2,\qquad r=y^5,\qquad h=y^8z,
\qquad V=1-y^{10}z.
\]
The exact presentation (2) therefore gives
\[
M/(x)=\frac{\mathbb C[y,z,w]}
 {((1-y^{10}z)w-y^5)}.
\tag{10}
\]
Set \(J=1-y^{10}z\). In (10),
\[
1=J+y^{10}z=J(1+y^5zw).
\]
Consequently
\[
M/(x)\cong\mathbb C[y,z,J^{-1}],\qquad w=y^5/J.
\tag{11}
\]
The nonconstant unit \(J\) rules out an isomorphism with
\(\mathbb C^{[2]}\). This disproves the proposed general
preservation of an original coordinate's affine-plane fibration.
It does not disprove the existence of a different fibration.

Indeed this example supplies a positive control: the known coordinate
construction replaces \(x\) by
\[
X=\frac{w^2+f^5}{h}=x-fw(w+r)\in M.
\tag{12}
\]
The equality follows from \(r=Vw\). Under the slice quotient,
the family's invariant \((1-fh)r-pt\) becomes \(w\), so
(12) is exactly its proved first polynomial coordinate. Thus
\(M=\mathbb C[X,Y,Z]\) for the accompanying coordinates in
that theorem. The successful fibration here is nonlinear in the
original data. No arbitrary-\(D\) analogue of (12) has been
constructed.

The polynomiality of \(h\), all four reductions modulo \(x\),
and the two identities used in (9) and (11) were also checked by exact
SymPy expansion using `/opt/anaconda3/bin/python`. These finite
identities are a computational check of this example, not verification
of a universal recognition theorem.

## 4. Primary recognition theorems and the actual missing bridge

### 4.1 A global target not restricted to the old invariant plane

Kaliman and Zaidenberg state Miyanishi's characterization for a smooth
contractible complex affine threefold: it is affine three-space if
there exists a regular function with a trivial affine-plane family
over a nonempty open subset of the line and every fiber is reduced,
irreducible, and factorial.[^1] This gives a concrete sufficient target:
find \(q\in M\), with no requirement \(q\in C\) or \(q\in R\),
and prove
\[
M_a\cong_{\mathbb C[q]_a}\mathbb C[q]_a^{[2]}
\quad\text{for some }0\ne a\in\mathbb C[q],
\qquad M/(q-c)\text{ is a UFD domain for every }c\in\mathbb C.
\tag{13}
\]
The preliminary smoothness and contractibility assumptions already
hold by Section 1. Neither the existence of \(q\) nor the fiber
conditions in (13) follow from (3) or (6).

An alternative version, explicitly stated as Theorem 2.6 by
Dubouloz, Pauli and Østvær with credit to Kaliman and Zaidenberg,
requires general affine-plane fibers and at most isolated
singularities in every closed fiber.[^2] This too allows \(q\)
outside the invariant plane. It remains a conditional bridge, not
a newly supplied \(q\).

For the specific original \(x\) in Section 3, even the general
fibers cannot all be affine planes: \(M\) is already known to be
affine three-space, and Kaliman's theorem, restated as Theorem 2.4
in the same source, would then force its closed fibers to be planes,
contrary to (11).[^2] Thus checking only a few favorable fibers of
an original coordinate would be insufficient.

### 4.2 A modification theorem whose conclusion is weaker

Theorem 2.7 of Dubouloz, Pauli and Østvær gives preservation of
topological contractibility for a regular-sequence modification,
subject to precise divisor-support, reduced-pullback, manifold, and
center homotopy-equivalence hypotheses.[^2] Its conclusion is
contractibility, not polynomiality. Here contractibility is already
known from (2); applying that theorem would not finish the bridge.

### 4.3 Additional additive actions and relative translation theorems

Gurjar, Koras, Miyanishi and Russell's Theorem 1.1 concerns a smooth
factorial threefold with constant units and two independent additive
actions. Its conclusion identifies the quotient surface, with affine
plane quotient in the simply connected case. It does not identify
the total threefold. Their Theorem 3.1 makes a fixed-point-free action
on complex affine four-space a translation when it fixes a polynomial
variable.[^3] The first result would not upgrade our already known
quotient \(\operatorname{Spec}C=\mathbb A^2\) to a polynomial
\(M\); the second still requires an ambient invariant coordinate,
which the arbitrary rank-three input does not supply.

The earlier [pass-18 statement audit](arbitrary-invariant-kernel-pass18.md)
also records the ambient-coordinate hypotheses in the relevant
Kaliman--Vénéreau--Zaidenberg and linear-hyperplane results. This
bounded pass has not identified an exact theorem that removes those
hypotheses for every ring (1). That is a report of checked scope,
not evidence of novelty or a claim that no such literature exists.

## 5. Bounded outcome

The all-base deduction (5)--(6) is available for subsequent arguments.
The concrete failed implication is preservation of an original
coordinate's plane fibers. The mathematically precise outstanding
lemma is construction of a regular function \(q\in M\) satisfying
one of the global recognition criteria in Section 4.1, or an independent
nonrelative polynomial-recognition theorem for (1). Local charts,
formal agreement, and matching associated graded algebras do not
establish that lemma. Full cancellation has not been solved.

## Sources

[^1]: S. Kaliman and M. Zaidenberg, *Miyanishi's characterization of the
    affine 3-space does not hold in higher dimensions*, Annales de
    l'Institut Fourier **50** (2000), 1649--1669. Introduction,
    pp. 1649--1650, including its explicit hypotheses and attribution.
    [Primary journal PDF](https://www.numdam.org/item/10.5802/aif.1803.pdf).

[^2]: A. Dubouloz, S. Pauli and P. A. Østvær,
    *A1-contractibility of affine modifications*, International Journal
    of Mathematics **30** (2019), 1950069. Theorems 2.4, 2.6 and 2.7
    in the [primary author preprint](https://arxiv.org/pdf/1805.08959).
    The relevant statements and their attributions were read directly.

[^3]: R. V. Gurjar, M. Koras, M. Miyanishi and P. Russell,
    *Affine threefolds admitting Ga-actions*, Theorems 1.1 and 3.1.
    [Primary author preprint, version 1](https://arxiv.org/pdf/1502.01849v1).
    The theorem statements, rather than just the abstract, were read.
