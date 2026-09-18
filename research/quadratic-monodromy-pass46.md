# The quadratic residue cover has one finite normalized branch value

The classified quadratic divisor models from pass 45 have an additional
global restriction. Their quadratic residue extension cannot be an
arbitrary extension of a rational function field. In a polynomial
parameter on the normalization of the base component, its square class
has exactly one finite odd valuation.

This is an application of published quotient geometry to the actual
unknown threefold. It neither excludes the quadratic models nor
identifies their global gluing.

The same conclusion applies to any intrinsic residue field of degree
two, even before a full DVR presentation of its neighborhood is known.
Section 3.1 states this distinction explicitly.
Combined with [the all-prime degree proof](quadratic-residue-degree-pass46.md),
it applies to every primitive plinth component of a still-unrecognized
quotient in the actual degree-two independent-defect frame.

## 1. Hypotheses and the exact conclusion

Retain the original cylinder
\[
B=A[s_*]\simeq\mathbb C^{[4]}
\]
and a nonzero intrinsic LND \(D\) on \(A\) whose kernel is the
already established ring \(C\simeq\mathbb C^{[2]}\).
In particular, \(X=\operatorname{Spec}A\) is a smooth factorial
contractible affine threefold. These properties concern \(A\), not
an assumed polynomial presentation of \(A\). For clarity, finite
generation follows by applying the retraction \(s_*\mapsto0\)
to polynomial generators of \(B\); smoothness descends from the
product \(X\times\mathbb A^1\), and factoriality descends from
the polynomial extension \(A[s_*]\). On complex points, projection
\(X\times\mathbb C\to X\) is a homotopy equivalence. Since
the former is \(\mathbb C^4\), \(X\) is contractible and
\(H_2(X)=H_3(X)=0\).

Let \(\pi\in C\) be irreducible. Set
\[
R=C_{(\pi)},\qquad K=\operatorname{Frac}(C/\pi C).
\]
Suppose the full intrinsic local ring, not merely a subalgebra of
bad-coordinate images, has the classified quadratic presentation
\[
A_R\simeq R[T,Z]/(\pi^nZ-T^2+\eta),\qquad
n\geq1,\quad \eta\in R^*,\quad \bar\eta\notin K^{*2}.
\tag{1}
\]
This includes every quadratic alternative justified in
[the divisor classification](quadratic-divisor-classification-pass45.md)
and [its acceleration extension](acceleration-divisor-extension-pass45.md).

Then the normalization of \(\Gamma_0=V(\pi)\) is
\(\mathbb A^1_u\), and there are \(b\in\mathbb C\) and
\(q(u)\in\mathbb C(u)^*\) such that, in \(K=\mathbb C(u)\),
\[
\boxed{\bar\eta=(u-b)q(u)^2.}
\tag{2}
\]
Equivalently, the normalization of the actual intermediate quotient
curve over \(\Gamma_0\) is \(\mathbb A^1_w\), with map
\[
u=w^2+b
\tag{3}
\]
after scaling and translating \(w\). Thus (3) has one finite
normalized branch value and ramification at infinity.
The parameter \(u\) is on the normalization; it need not belong
to \(C/\pi C\) and is not asserted to be a coordinate of \(C\).

## 2. The primary-source gate applies before cancellation

[Kaliman, *Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Lemma 2.2, Proposition 3.2 and Theorem 5.2(i), have hypotheses on a
factorial affine threefold with \(X\) smooth and
\(H_2(X)=H_3(X)=0\); they do not require \(X\simeq\mathbb C^3\).
They provide a product complement and a factorization
\[
X\supset E\longrightarrow Z\xrightarrow{\theta}\Gamma
\]
with \(\theta\) finite. One can retain only components whose
intermediate maps are nonbijective; their base normalizations are
affine lines. Step 2 of the proof of Proposition 3.2 gives equality
of the first Betti numbers of the total source and base normalizations.
These statements and their complete relevant proofs were directly
read in the final author PDF, including Theorem 5.2 and Remark 5.4.

Here those hypotheses follow from the original cylinder. In the
fully retained choice, the base normalization has zero first Betti
number, so the source normalization does too. Each connected source
normalization is a smooth affine curve. If its smooth projective
completion has genus \(g\) and \(r\geq1\) omitted points, then
\(b_1=2g+r-1\). Hence each is an affine line.

This is the same normalization-rank mechanism used previously for
an actual ambient \(\mathbb C^3\) in
[pass 34](integral-ramification-pass34.md). The present scope check
uses the theorem's actual general-threefold hypotheses; it is not
a new source theorem or a claim of historical novelty.

## 3. Identifying the actual cover, without guessing a residue quotient

First, \(\Gamma_0\) must remain a component of the fully retained
\(\Gamma\). If it did not, its generic point would lie in the
product-complement open set. The corresponding generic divisor
fiber would then be \(K^{[1]}\). In contrast, (1) gives its entire
ring as
\[
A_R/\pi A_R=K(\sqrt{\bar\eta})[Z],
\tag{4}
\]
whose algebraic constant field over \(K\) has degree two. These
are not isomorphic \(K\)-algebras. This argument does not assume
that every component of a plinth is already identified with the
retained divisor.

Let \(Z_0\) be the intermediate component over \(\Gamma_0\).
The surface \(E_0=V_A(\pi)\) is irreducible; equivalently here,
\(\pi\) remains prime by factorial closure in the UFD \(A\).
Consequently its dominant image in the intermediate curve is one
irreducible component. The generic cylinder in the factorization
identifies its function field as
\[
\mathbb C(E_0)=\mathbb C(Z_0)(z_0).
\tag{5}
\]
On the other hand, (4) identifies that same field as
\(K(\sqrt{\bar\eta})(Z)\). The algebraic closure of \(K\)
inside a one-variable rational function field over a finite
extension \(L/K\) is exactly \(L\): any element algebraic over
\(L\) inside \(L(Z)\) belongs to \(L\). Applying this in (5)
and (4) yields the equality inside \(\mathbb C(E_0)\)
\[
\mathbb C(Z_0)=K(\sqrt{\bar\eta}).
\tag{6}
\]
Thus the actual finite cover has degree two. This uses the full
residue ring and the actual factorization. It does not assume that
restriction of invariants surjects onto the residue invariant ring.

Normalization of the finite dominant curve map is finite. One
way to check this precisely is to take the integral closure of
\(\mathbb C[\Gamma_0]\) in (6): it contains the integral closure
of \(\mathbb C[\Gamma_0]\) in \(K\), and the same finite module
generators still generate over this larger ring. Thus the induced
map of the two affine-line normalizations is a finite polynomial
map of degree two.

### 3.1. Intrinsic residue fields and all primitive plinth components

For this subsection choose \(D\) primitive: the values of \(D\)
on a finite algebra generating set of the UFD \(A\) have gcd one.
Let \(\pi\) be any irreducible element of \(C\), not necessarily
one with presentation (1). The full residue curve
\(A_R/\pi A_R\) is a nonzero domain of transcendence degree one
over \(K\). Faithful flatness and the equidimensional quotient
give this dimension; factorial closure gives primality.
Primitivity makes its induced LND nonzero. Otherwise all generator
values would be divisible by \(\pi\) after the invariant
localization and therefore already in \(A\).

Every invariant of that residue LND is algebraic over \(K\).
Such a nonzero algebraic element is invertible in the residue
ring, by its minimal polynomial over the field \(K\). Thus its
invariant ring is a field \(F_\pi\), finite over \(K\): it is
contained in the relative algebraic closure of \(K\) inside the
finitely generated residue function field. A nonzero local-slice
value belongs to this field and is a unit, so the slice theorem
gives the entire ring
\[
A_R/\pi A_R=F_\pi[t],\qquad
e_\pi=[F_\pi:K]<\infty.
\tag{6a}
\]
This is a generic-divisor statement, not an invariant-lifting
assertion from \(C/\pi C\).

The reduced primitive plinth support is exactly the fully retained
\(\Gamma\). Here is the needed extension of the old
[coordinate-coefficient proof](whole-plinth-component-pass16.md)
to the unknown \(A\). Write \(\Gamma=V(f)\). Outside it,
\(A_f=C_f[w]\), and \(D=a\partial_w\) for some
\(a\in C_f\). A nonunit prime factor of \(a\) in \(C_f\)
would divide every \(D\)-value of a generator after localization.
Prime saturation in the UFD \(A\), with that prime coprime to
\(f\), makes it divide every such value globally. This contradicts
primitivity. Thus \(a\) is a unit. The slice \(w/a\in A_f\)
has a power of \(f\) as a denominator; clearing it gives a
plinth value not vanishing anywhere outside \(\Gamma\).

Conversely, each fully retained intermediate component has degree
greater than one. Here nonbijective implies nonbirational by the
actual Proposition 3.2 argument; no such implication is asserted
for arbitrary finite curve maps. A plinth value not vanishing
generically on that component would give a slice and a single-line
generic divisor fiber, which contradicts its cover degree.
This proves the support equality and
\[
\pi\mid\operatorname{pl}(D)\quad\Longrightarrow\quad
e_\pi>1.
\tag{6b}
\]
In (6b), divisibility of an ideal means that every element of the
plinth is divisible by \(\pi\); its principality is not needed.

For every such prime, the preceding normalization argument gives
an actual finite polynomial map
\(\mathbb A^1\to\mathbb A^1\) of degree \(e_\pi\).
In particular, if \(e_\pi=2\), equation (2) holds for any
nonsquare \(\epsilon\in K^*\) with
\(F_\pi=K(\sqrt\epsilon)\), replacing \(\bar\eta\) by
\(\epsilon\). This extension requires neither a lift of
\(\epsilon\) into a preferred presentation nor the existence
of a local equation \(\pi^nZ=T^2-\eta\).

The separate [all-prime degree proof](quadratic-residue-degree-pass46.md)
now shows that, in the actual degree-two independent-defect frame,
either \(A\simeq\mathbb C^{[3]}\) is already recognized or every
primitive plinth prime has \(e_\pi=2\). Applying the present
argument in the latter case therefore gives (3) for every such
component, including the simultaneous primes. This combination alone
is a field-cover restriction. The later
[minimal-slice lifting lemma](minimal-quadratic-slice-pass46.md)
now supplies the full quadratic DVR neighborhoods at all these
primes, without changing the cover argument here.

## 4. The square-class computation

Write this polynomial map as \(u=a w^2+c w+d\), with
\(a\ne0\). Completing the square and taking a complex square
root of \(a\) changes the source coordinate so that it is (3).
Therefore (6) is
\[
\mathbb C(u)(\sqrt{\bar\eta})
=\mathbb C(u)(\sqrt{u-b}).
\]
For nonsquares \(a_1,a_2\) in a characteristic-zero field, equal
quadratic extensions imply \(a_1/a_2\) is a square: write
\(\sqrt{a_1}=r+t\sqrt{a_2}\) and compare its square; the mixed
term gives \(rt=0\), while nonsquareness excludes \(t=0\).
This proves (2).

Consequently, on \(\mathbb A^1_u\), \(\bar\eta\) has odd
valuation at precisely \(u=b\). At all other finite points its
valuation is even. Its valuation at infinity is odd. These are
valuations in the normalized function field; zeros or poles of a
chosen non-normal-plane expression are not a substitute.

For example, a proposed normalized square class \(u(u-1)\)
cannot occur in (1) under the global hypotheses. This is stronger
than requiring the cover to be rational: its affine normalization
is \(\mathbb C^*\), not \(\mathbb A^1\). Indeed, with
\(v^2=u(u-1)\),
\[
t=2u-1+2v,\quad t^{-1}=2u-1-2v,
\quad u=(t+t^{-1}+2)/4,\quad v=(t-t^{-1})/4.
\tag{7}
\]
These mutually inverse identities identify the smooth affine
conic with \(\operatorname{Spec}\mathbb C[t,t^{-1}]\).

## 5. What this does not settle

The known polynomial example
\(D=X\partial_Y+2Y\partial_Z\) on \(\mathbb C[X,Y,Z]\)
already has normalized square class \(-H\), where
\(H=XZ-Y^2\). It satisfies (2). The larger repeated-exponent
and disconnected-support polynomial controls from passes 18 and
33 likewise remain valid. They are existing controls, not new
claims or new tests in this pass.

There is no bound here on the thickness \(n\), no proof that
\(\Gamma_0\) is a smooth embedded line, and no compatibility
theorem gluing different divisor coordinates. In particular,
the cover argument alone does not classify the simultaneous
neighborhoods from pass 45. Their local classification is now supplied
by the separate [finite minimal-slice correction](minimal-quadratic-slice-pass46.md).
Global compatibility of the resulting embedded divisor models
remains open; contractibility has not supplied a global polynomial
inverse for \(A\).

The separate published recognition gate is disappearance of all
genuine retained covers, or a fixed-point-free intrinsic action;
Kaliman's Theorem 5.2 then gives a product over the smooth quotient.
The permitted degree-two covers do not meet that gate. The broader
question is still open in this program. No withdrawn paper,
human expert review, or proof-assistant verification is used.

## Verification boundary

The source hypotheses, field identifications and degree-two
argument are written proofs. No additional numerical grid or
duplicate standalone suite is introduced for them. Identity (7)
is an exact elementary inverse and can be checked by substitution.
