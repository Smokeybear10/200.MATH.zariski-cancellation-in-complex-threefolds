# Image-ideal freeness does not yet supply the missing global equation

The sources checked on 13 September 2026 do not provide an applicable
principality theorem for the second image of the unknown stably
polynomial threefold. Their positive conclusions either require an
actual relative polynomial ring or assume the freeness property.
This is a theorem-applicability conclusion, not a claim that a bounded
search certifies the absence of every possible theorem.

## 1. The ring to which a theorem would have to apply

Keep the exact hypotheses of
[the second-image criterion](second-image-gluing-pass46.md):
\[
A[s_*]\simeq\mathbb C^{[4]},\qquad
C=\ker D\simeq\mathbb C^{[2]},\qquad
Dr=p,\qquad I_2(D)=D^2(A)\cap C=pJ.
\]
The action is primitive, the inclusion is faithfully flat, and the
full quadratic models hold at every invariant prime divisor. These
give \(p\in J\) and \(J_{(\pi)}=C_{(\pi)}\) for every prime
element \(\pi\), but not \(J=C\). In this situation principality
of \(I_2(D)\) is equivalent to \(J=C\), hence to the global
quadratic presentation for the actual minimal slice. That presentation
would still not, by itself, identify \(A\) with \(\mathbb C^{[3]}\).

## 2. Current primary statements and their gates

### Dasgupta–Lahiri, latest v6

[arXiv:2302.13787v6](https://arxiv.org/html/2302.13787v6), dated
24 July 2026, still states all-image principality for LNDs of
\(k^{[3]}\) as the Freeness Conjecture. Its document title is
*On image ideals of nice and quasi-nice derivations on
\(R[X_1,X_2]\)*; the abstract-page title retains the older wording.
For an irreducible \(R\)-LND on an actual \(R[X_1,X_2]\), with
\(R\) a characteristic-zero affine UFD, Theorem 4.1 assumes
\(D^2X_1=D^2X_2=0\) and gives
\(I_j=(DX_1,DX_2)^j\ker D\). Corollary 4.2 includes
nonprincipal ideals.

Theorem 5.2 instead assumes a non-fixed-point-free, strictly
1-quasi-nice action, \(DX_1=b\) irreducible in \(R\), and
\(DX_2=-f'(X_1)\). If
\(d=\max\{i:b\nmid f_i\}\), its formula specializes to
\[
I_2=\begin{cases}b(b,f_2)\ker D,&d=2,\\
b^2\ker D,&d>2.\end{cases}
\]
Theorem 5.9 requires a PID and the displayed relative triangular
coordinates; its higher-image formula additionally requires every
prime factor of \(DX_1\) to avoid the leading coefficient of \(f\).
The relevant theorem statements and proofs were read directly.

The application fails before these formulas: no global relative
polynomial-plane coordinates on the unknown \(A\) have been supplied.
The generic bad-coordinate chart and full DVR quadratic neighborhoods
are not the hypothesis \(A=R[X_1,X_2]\). Reading v6 updates the
source status of pass 46's explicitly versioned v3 citation; it does
not change that older proof's logical scope.

### Ben Khaddah–El Kahoui–Ouali, published PID result

[*The freeness property for locally nilpotent derivations of
\(R^{[2]}\)*](https://link.springer.com/article/10.1007/s00031-022-09705-z),
*Transformation Groups* 28 (2023), 35–60, was published online
5 March 2022. For a PID \(R\) containing \(\mathbb Q\) and a
nonzero relative LND on the actual polynomial plane \(R^{[2]}\),
the published abstract asserts an adapted derivation-degree basis
over the kernel. It explicitly gives actual rank-at-most-two
\(k^{[3]}\) actions as a consequence. The current publisher
abstract was directly read. The full original theorem is
subscription-only in the checked route; its numbering as
Theorem 4.1 and all-image formulation are also recorded explicitly
by Dasgupta–Lahiri. No inaccessible proof is claimed as read.

An invariant plane \(C\) inside \(A\) is not an invariant
coordinate in an already known three-variable polynomial ring.
Neither \(C\) nor its two-dimensional closed-point local ring is
a PID. Applying this result directly to \(A\) would insert exactly
the missing global coordinate structure.

### El Kahoui–Labtaini–Ouali, published factorial-domain result

[*The Freeness Property for Locally Nilpotent Derivations of
Factorial Domains*](https://link.springer.com/article/10.1007/s00031-026-09969-9),
published 15 May 2026, starts with an affine factorial domain over
a characteristic-zero field, an irreducible LND, an affine kernel,
a prime-power-generated plinth, and the freeness property. Its
announced conclusion is a differential-algebra identification with
a generalized Danielewski variety. The publisher's complete abstract
and reference list were read; the full article is subscription-only
in the checked route.

This is not a theorem deriving freeness from factoriality. Even if
the plinth here had only one prime factor, using that statement to
prove \(I_2\) principal would assume its missing freeness premise.

### Withdrawn all-ranks claim

The current [Daigle arXiv:2009.14800 record](https://arxiv.org/abs/2009.14800)
explicitly marks v2, dated 14 May 2021, withdrawn because of an error
in the main proof. Its retained abstract still announces the full
three-variable Freeness Conjecture. That announcement is not used
as a valid theorem here.

## 3. Two exact algebraic applicability checks

First, an adapted basis is stronger information than unspecified
module freeness. For any domain and nonzero characteristic-zero LND,
put \(F_n=\ker D^{n+1}\). The exact sequences
\[
0\longrightarrow F_{n-1}\longrightarrow F_n
\xrightarrow{D^n} I_n\longrightarrow0
\]
show that principality of every \(I_n\) constructs, inductively,
a basis \(e_n\) with \(\deg_D e_n=n\). Conversely such a basis
generates \(I_n\) by \(D^n e_n\). A statement only that a larger
module is free cannot silently be substituted: even a quotient of
two finite free modules can be the nonprincipal ideal \((U,V)\).

Second, extend \(D\) to \(\widetilde D\) on \(B=A[s_*]\)
by \(\widetilde D(s_*)=0\). Coefficientwise comparison proves
\[
\ker\widetilde D=C[s_*],\qquad
I_n(\widetilde D)=I_n(D)C[s_*].
\tag{1}
\]
If the extended ideal were principal, evaluation at \(s_*=0\)
would make \(I_n(D)\) principal. Thus an applicable theorem about
this particular four-variable action would suffice. But its ambient
ring being abstractly polynomial does not establish a relative
presentation over the original cylinder variable. In particular,
\(B=\mathbb C[s_*]^{[3]}\) as a
\(\mathbb C[s_*]\)-algebra would already yield
\(A=B/(s_*)\simeq\mathbb C^{[3]}\).
Also the original sliced action \(\partial_{s_*}\) is different
from \(\widetilde D\); its slice does not trivialize the latter's
image ideals.

## 4. The stronger geometric source has a different exact conclusion

In [Kaliman's final 2004 author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Lemma 2.2 constructs \(E\xrightarrow{\kappa}Z
\xrightarrow{\theta}\Gamma\) with \(\kappa\) surjective,
\(\theta\) quasi-finite, and a dense cylinder over \(Z\).
Here \(Z\) is the image in a proper compactification's Stein
factorization, not by definition the full residue invariant spectrum.
Proposition 3.2(i) proves this \(\theta\) finite when
\(H_3(X)=0\) and \(X^*\) is smooth, within the inherited
factorial affine threefold setup. These hypotheses follow from
the original cylinder. The statement and complete finiteness proof
were reread directly.

Finiteness alone does not make a chosen generic primitive element
nonconstant in a full closed fiber. The elementary finite cover
\(\mathbb C[v]\subset\mathbb C[w]\), \(v=w^2\), has generic
primitive element \(r=w^3\), yet \(r=0\) in
\(\mathbb C[w]/(w^2)\). This is only a curve-level control, not
an actual minimal slice of the target threefold. It isolates the
extra minimal-slice/ambient-regularity argument still needed to
deduce the non-scalar closed-fiber condition of
[the pass-47 criterion](second-image-closed-fiber-pass47.md).

The bounded source search therefore leaves a precise obligation:
prove \(J=C\), or equivalently rule out the actual minimal slice
becoming scalar in a full closed quotient fiber, using a hypothesis
not supplied by the relative polynomial-ring freeness theorems.
No new computational suite, frozen-file edit, or general cancellation
claim is attached to this source audit.
