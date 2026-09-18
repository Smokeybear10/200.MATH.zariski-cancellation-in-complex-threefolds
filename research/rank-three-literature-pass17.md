# Rank-three image ideals and the pointwise plinth question

The concrete positive lead is already published: Freudenburg proves the
freeness property in every degree for the rank-three \((2,5)\) derivation used
in this project. Dasgupta–Gaifullin give a broader rank-three family with an
explicit plinth, but their family theorem does not establish principal higher
image ideals. The recent sources inspected here do not supply the requested
general rank-three or pointwise-fiber implication. This is a bounded access
and statement audit through September 12, 2026, not an absence-based claim
that either implication is open or new.

## 1. A known all-degree rank-three case

[Freudenburg, *Canonical factorization of the quotient morphism for an affine
Ga-variety*, Sections 8.2.2, 8.2.7–8.2.8](https://arxiv.org/pdf/1602.08786),
*Transformation Groups* **24** (2019), 355–377,
[DOI 10.1007/s00031-018-9472-y](https://doi.org/10.1007/s00031-018-9472-y).
The full primary PDF was read at Theorem 8.3, Proposition 8.4, Corollary 8.5,
and their proofs.

For a characteristic-zero field, put
\[
T=k[x,y,z],\quad f=xz-y^2,\quad
g=zf^2+2x^2yf+x^5,\quad r=x^3+yf,\quad s=x^2y+zf,
\]
and \(D=\operatorname{Jac}(f,g,\cdot)\), \(C=\ker D=k[f,g]\).
This is the rank-three \((2,5)\) derivation. With
\(\mathcal F_j=\ker D^{j+1}\), the source proves
\[
T=\bigoplus_{m\ge0}\mathcal F_9z^m,
\qquad
\mathcal F_9=
C\{1,r,x,xr,x^2,s,y,xs,xy,x^2s\}.
\]
The listed basis elements have successive \(D\)-degrees \(0,\ldots,9\),
and \(\deg_Dz=10\). Thus this is an adapted basis in every degree, not merely
a calculation up to degree ten. In particular, all
\(I_j=D^j\mathcal F_j\) are principal. The source also computes
\[
\operatorname{Gr}_D(T)=
C[fgt,f^2gt^2,f^4g^3t^5,f^5g^3t^6,f^8g^5t^{10}].
\]
The project's convention replaces \(r\) by \(-r\); it does not change these
ideals. These all-degree conclusions must be credited as known.

An elementary transfer, separate from the cited calculation, is
\(I_j(aD)=a^jI_j(D)\) for \(0\ne a\in C\). Hence invariant replicas and
automorphic conjugates inherit principal higher image ideals. This does not
cover arbitrary local-slice constructions.

## 2. The closest broader family: exact plinth, not all images

[Dasgupta–Gaifullin, *On locally nilpotent derivations of polynomial algebra
in three variables*, Theorem 5.7 and proof](https://www.mathnet.ru/eng/sm10094),
*Sbornik: Mathematics* **216**(4) (2025), 456–484,
DOI 10.4213/sm10094e. The published full HTML and
[arXiv:2306.00510v2](https://arxiv.org/html/2306.00510v2) were read.

Let \(m\ge2\), \(n\ge1\), and \(F\in k[t_1,t_2]\) with
\(F(t_1,0)\notin k\). Define
\[
f=xz-y^m,\quad r=xF(x,f)+yf^n,\quad
h=\frac{f^{mn+1}+r^m}{x},\quad E=\operatorname{Jac}(f,h,\cdot).
\]
The theorem proves rank three. Its proof establishes irreducibility,
\(\ker E=k[f,h]\), and minimality of the local slice \(r\). Consequently
\[
E(r)=-hf^n,\qquad \operatorname{pl}(E)=f^nh\,k[f,h].
\]
The positive bound on \(n\) is explicit in arXiv; the published HTML omits
that inequality in its displayed theorem. No all-degree image-ideal or
freeness assertion is made in this family theorem. Propositions 5.3–5.4
instead characterize irreducible rank three by a plinth generator that is
not univariate in any coordinate of the kernel.

### Elementary consequence for the matrix-lift premise

For \(n=1\), \(C/(fh)\) is the reduced union of two coordinate axes, and
\((C/(fh))^*=k^*\): a unit restricts to constants on each affine line, and
those constants agree at the intersection. Therefore an affine-slice
condition making \(B\) a unit modulo \(fh\) gives
\(B\equiv c\pmod{fh}\), \(c\in k^*\). This is the scalar-congruence
premise of the project's matrix lift, after normalization.

For \(n>1\), the reduced support remains the same connected pair of axes,
but \(C/(f^nh)\) is nonreduced. For example, \(1+fh\) is a unit there
because \((fh)^n=0\), yet it is not congruent to a scalar modulo \(f^nh\).
Thus connected reduced support alone does not remove the thickening issue.
Nor does reducedness and connectedness of an arbitrary curve imply constant
units, as \(\mathbb G_m\) illustrates.

This observation concerns an already established affine-slice condition.
The source's plinth formula alone does not prove that every extension slice
has an affine replacement for this entire family.

## 3. Recent freeness sources: exact scope

[Dasgupta–Lahiri, arXiv:2302.13787v6](https://arxiv.org/html/2302.13787v6),
July 24, 2026, studies irreducible nice and quasi-nice relative derivations.
Its introduction still presents all higher image ideals on \(k^{[3]}\) as
the Freeness Conjecture, and attributes the PID-relative \(R^{[2]}\), hence
rank-at-most-two, result to Ben Khaddah–El Kahoui–Ouali. Theorem 5.9 gives
explicit generators under its quasi-nice hypotheses, with an additional
leading-coefficient condition for its all-degree formula. It is not an
arbitrary rank-three theorem. The original rank-two source-access boundary
is recorded in [the pass16 note](rank-two-image-ideals-pass16.md).

[El Kahoui–Labtaini–Ouali, *The Freeness Property for Locally Nilpotent
Derivations of Factorial Domains*](https://link.springer.com/article/10.1007/s00031-026-09969-9),
published May 15, 2026, DOI 10.1007/s00031-026-09969-9, assumes an affine
factorial characteristic-zero domain, an irreducible LND, an affine kernel,
the freeness property, and a prime-power-generated plinth. Its conclusion
identifies the differential algebra with a generalized Danielewski model.
Freeness is a premise, not its conclusion. Only the primary abstract and
bibliography were accessible; the full theorem was subscription-only.

The primary record of
[Daigle, arXiv:2009.14800](https://arxiv.org/abs/2009.14800) explicitly
withdraws the purported all-ranks proof for an error. Its retained abstract
must not be used as evidence of a resolution.

## 4. Pointwise fibers: what the current theorem actually says

[Masuda, *Faithfully flat quotient morphisms by Ga-actions on factorial
affine varieties*](https://arxiv.org/html/2512.06687v1), arXiv v1,
December 7, 2025, published in *Journal of Algebra* **691** (2026), 577–596,
[DOI 10.1016/j.jalgebra.2025.11.020](https://doi.org/10.1016/j.jalgebra.2025.11.020).
Proposition 2.5, its remark, and Theorem 3.5 were read in full.

For a factorial affine complex variety, irreducible LND, affine kernel,
and faithfully flat quotient \(\pi\), the remark proves
\[
\overline{\{y:\pi^*(y)\not\cong\mathbb A^1\}}
=V(\operatorname{pl}(D)).
\]
This is a closure equality. It does not itself exclude an exceptional
reduced \(\mathbb A^1\) fiber inside the plinth support.

Theorem 3.5 gives a global criterion: the quotient is a trivial line bundle
exactly when there is a principal divisor outside which every closed fiber
is \(\mathbb A^1\), and, for each prime divisor component \(V(f_i)\),
\[
\operatorname{Spec}\ker\overline D_i\longrightarrow
\operatorname{Spec}(C/f_iC)
\]
is birational. Here \(\overline D_i\) is induced on \(T/f_iT\).
Birationality along every relevant divisor is stronger than having one
reduced free-orbit fiber. This theorem supplies a precise additional premise,
not the desired pointwise implication.

## 5. Bounded coverage

The search followed the current freeness references, Freudenburg's
all-degree calculation, the closest published rank-three family, and
Masuda's latest fiber criterion. Queries included rank-three higher image
ideals, Freeness Conjecture updates, and reduced single-orbit fibers in the
plinth locus. No paid access or author contact was used. The known
\((2,5)\) adapted basis is the directly applicable positive result; the
source statements inspected in this literature note do not by themselves
certify general rank-three freeness or the pointwise bridge.

## 6. Later pointwise deduction and another current boundary

The separate [peripheral-cycle proof](pointwise-plinth-pass17.md) and
[independent audit](pointwise-plinth-audit-pass17.md) now supply a working
pointwise deduction using Kaliman's actual global homology diagram.
This changes the status of the research argument, not the wording of
Masuda's closure-only theorem above. The exact distinction remains relevant.

A further primary source was read: Kirill Shakhmatov,
[Cylinders and the zero locus of the plinth ideal](https://arxiv.org/html/2605.00138v1),
arXiv:2605.00138v1, April 30, 2026, Theorem 2.6, Corollaries 2.7-2.8,
and the examples in Section 3. Its criterion identifies invariant
principal open cylinders by powers of their defining functions belonging
to the plinth ideal. This characterizes an existing equivariant product
neighborhood; it does not assert that one smooth quotient fiber supplies
such a neighborhood. The theorem is therefore consistent with, but not
a replacement for, the additional pointwise proof.

No novelty conclusion is drawn from these bounded searches. Unreviewed
public research repositories returned by search were not used as proof
sources or evidence that cancellation has been resolved.
