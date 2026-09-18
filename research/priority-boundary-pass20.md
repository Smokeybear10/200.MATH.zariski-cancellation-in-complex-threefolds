# Priority boundary: the weighted lifts reduce to standard modifications

Private bounded audit, 2026-09-13. There is a further exact prior-work
reduction beyond the cylinder comparison: the weighted-overring extension
is a composition of two applications of Kaliman--Zaidenberg's universal
property. This note proves the required second, nonreduced center
identification. Thus neither the cylinder matrix nor the abstract lifting
principle should be presented as new. The remaining project-specific
work is construction of compatible curve-center jets, their extra
normal-displacement precision, and the stated kernel/plinth calculations.
Priority for that combined statement is unresolved.

The [cylinder comparison](cylinder-comparison-pass20.md) and the full
[nonunit construction](nonunit-local-slice-pass20.md), including its
coefficient-explicit CRT continuation, were read. This note is a
source-and-implication audit, not a new audit of every CRT calculation.
It does not claim that unrestricted cancellation is solved.

## 1. Exact existing lifting statements

Kaliman--Zaidenberg Proposition 2.1 treats affine triples
\((A,I,q)\), \((A_1,I_1,q_1)\). A homomorphism \(\mu:A\to A_1\)
with \(\mu(I)\subset I_1\) and \(\mu(q)=u q_1\), \(u\) a unit,
extends uniquely to their affine modifications. If the algebra and ideal
maps are surjective, so is the extension. Corollary 2.2 states the
automorphism version: preservation of the full ideal and of the
denominator up to a unit gives a unique lifted automorphism.[^1]

These statements use the actual ideals, including their nonreduced
structure. Preservation of the reduced support is not their algebraic
hypothesis. Corollary 2.3 similarly lifts an LND when it kills the
denominator and preserves the ideal.[^1] None of these statements
constructs the necessary change of center. That is the obligation
checked in Sections 2--4 below.

## 2. The physical weighted overring is a two-stage modification

Use the notation of the cylinder comparison:
\[
\mathscr A_0=\frac{\mathbb C[f,x,h,r]}{(xh-K(f,r))},
\quad K(f,r)=G(r,f^n)+f^{nd+1},
\]
\[
a_P=r-xP(x,f),\qquad
b_P=h-P(x,f)\Delta_G(r,r-xP(x,f);f^n),
\]
\[
xb_P=G(a_P,f^n)+f^{nd+1},\qquad
\mathscr R_P=\mathscr A_0[a_P/f^n,b_P/f^{nd}].
\tag{1}
\]
Here \(F\) is monic of degree \(d\ge2\),
\(G(R,S)=S^dF(R/S)\), and \(n\ge1\).

First use the entire curve-center ideal
\[
J_P=(f^n,a_P,b_P),\qquad
\mathscr B_P=\mathscr A_0[J_P/f^n].
\tag{2}
\]
This first modification adjoins *both* \(a_P/f^n\) and
\(b_P/f^n\), not just the first fraction of (1). Set
\(y=a_P/f^n\), \(H=b_P/f^n\), and \(m=n(d-1)\). Then
\[
\mathscr B_P\cong
\frac{\mathbb C[f,x,y,H]}{(xH-f^m(F(y)+f))}.
\tag{3}
\]
Indeed the relation follows by dividing (1) by \(f^n\).
Conversely \(r=xP+f^ny\) and \(h=f^nH+P\Delta_G\) recover
the old generators. The displayed hypersurface is a domain: its
equation is primitive linear in \(H\), with coprime coefficient
\(x\) and constant term \(f^m(F(y)+f)\). Localization at \(f\)
verifies the two inverse presentations, hence injectivity before
localization as well.

The second modification is
\[
L_P=(f^m,H)\subset\mathscr B_P,
\qquad \mathscr B_P[L_P/f^m]
 =\mathscr B_P[H/f^m]=\mathscr R_P.
\tag{4}
\]
The identity \(H/f^m=b_P/f^{nd}\) proves the last equality.
All statements remain true after adjoining the cylinder variable.

## 3. The nonreduced second center is canonically preserved

The exact saturation identity is
\[
L_P=(f^m):x^\infty
 :=\{b\in\mathscr B_P:\ x^jb\in(f^m)
             \text{ for some }j\ge0\}.
\tag{5}
\]
To prove it, reduce (3) modulo \(f^m\):
\[
\mathscr B_P/(f^m)
 =\frac{(\mathbb C[f]/(f^m))[x,y,H]}{(xH)}.
\]
Localization at \(x\) kills \(H\). Conversely, after quotienting
by \(H\), \(x\) is a nonzerodivisor in a polynomial ring,
even though its coefficient ring contains nilpotents. The kernel of
this localization is therefore exactly \((H)\). Its inverse image
in \(\mathscr B_P\) is (5).

Let \(\Phi\) be the surface-cylinder isomorphism in the weighted
lemma. The two finite curve identities give the full ideal equality
\[
\Phi(J_{\widetilde P}\mathscr A_0[t])
 =J_P\mathscr A_0[t],
\qquad \Phi(f)=f.
\tag{6}
\]
Kaliman--Zaidenberg Proposition 2.1, applied in both directions,
therefore gives
\(\Phi_1:\mathscr B_{\widetilde P}[t]\simeq\mathscr B_P[t]\).

Now \(\Phi_1(x)\equiv x\pmod f\). Modulo \(f^m\), the
elements \(\Phi_1(x)\) and \(x\) differ by a nilpotent.
They thus define identical principal open subsets, and localizing
at either has the same kernel. Explicitly, if one is invertible,
the other is that unit times \(1+\) a nilpotent, hence is
invertible too. Using (5),
\[
\Phi_1(L_{\widetilde P})
 =(f^m):\Phi_1(x)^\infty
 =(f^m):x^\infty=L_P.
\tag{7}
\]
This is equality of the full thickened ideals, not just their radicals.
A second application of Proposition 2.1 in both directions now gives
\[
\mathscr R_{\widetilde P}[t]\simeq\mathscr R_P[t].
\tag{8}
\]

Consequently the extra weighted-overring lemma in the cylinder
comparison is a direct consequence of the established modification
lifting theorem, once its curve-center equality and identity reduction
are supplied. The Taylor/prime-factor proof there is a valid explicit
verification, but it is not a new general lifting principle.

## 4. The Q correction has the same exact two-stage form

The construction can also be applied before the old \(P\)-curve
correction. Allow the coefficient-explicit nonunit setup from pass 20:
\[
0\ne a(f)\in\mathbb C[f],\qquad
\Theta(f,T)=G(T,af^n)+a^df^{nd+1},
\]
\[
\mathscr T=\frac{\mathbb C[f,h,k,R_*]}{(hk-\Theta(f,R_*))}.
\]
If \(a\) is a nonzero constant, both modifications below are
identity operations and no \(a\)-adic center correction is needed.
For the nontrivial case assume \(a\) is nonconstant.
Define
\[
c_Q=R_*-hQ(f,h),\qquad
d_Q=k-Q(f,h)\Delta_G(R_*,R_*-hQ(f,h);af^n).
\tag{9}
\]
Then
\[
hd_Q=\Theta(f,c_Q).
\tag{10}
\]
The old surface is exactly
\[
\mathscr T[c_Q/a,d_Q/a^d]
 \cong\frac{\mathbb C[f,h,r,x]}{(hx-K_n(f,r))}.
\tag{11}
\]
This follows from \(r=c_Q/a\), \(x=d_Q/a^d\), and
\(\Theta(f,ar)=a^dK_n(f,r)\).

First modify along \((a,c_Q,d_Q)\) with denominator \(a\).
The intermediate ring has presentation
\[
\frac{\mathbb C[f,h,r,W]}{(hW-a^{d-1}K_n(f,r))},
\qquad W=d_Q/a.
\tag{12}
\]
Then modify along
\[
(a^{d-1},W)=(a^{d-1}):h^\infty
\tag{13}
\]
with denominator \(a^{d-1}\). The proof of (13) is the proof
of (5), over \(\mathbb C[f]/(a^{d-1})\). It does not require
\(a\) to be prime or squarefree. The resulting ring is (11).
The presentations are domains because their equations are primitive
linear in \(W\) or \(x\), and the relevant constant terms are
nonzero polynomials independent of \(h\).

Modulo \(a\), the first center is the cone curve
\[
(h,k,R_*)=(H,H^{d-1}Q(f,H)^d,HQ(f,H)).
\tag{14}
\]
The nonunit proof's finite \(Q\)-reparametrization is exactly
the construction of a \(\widetilde Q\) for which the known
surface-cylinder map transports these full ideals in both directions.
Thus Proposition 2.1 gives the first lift. The coefficient condition
\(B\equiv1\pmod{\operatorname{rad}(a)}\) makes the image of
\(h\) congruent to \(h\) modulo \(\operatorname{rad}(a)\).
That difference is nilpotent modulo \(a^{d-1}\). Formula (13)
therefore transports the second center exactly as in (7), giving
the second lift.

There is one additional compatibility requirement if \(a\) vanishes
at \(f=0\). If \(e=\operatorname{ord}_f(a)>0\), the
\(Q\)-curve equality merely modulo \(f^e\) gives polynomial
division by \(a\), but does not by itself specify the old cone
map modulo \(f\). The extra \(f^{e+1}\) calculation in pass 20
retains the first normal displacement \(ar\) and proves that this
old-cone map is the identity modulo \(f\). If \(e=0\), the
separate congruence \(\widetilde Q\equiv Q\pmod f\) gives
that identity. Its cylinder-variable independence and vertex
preservation are then checked in the project proof. Those conditions
permit the further \(P\)-center transport and the two lifts in
Sections 2--3.

Thus the known lifting theorem does apply to the completed nonunit
construction. It does not remove the need to prove these particular
center correspondences or their extra order of precision.

## 5. Freudenburg's iteration results: exact scope

Freudenburg's Section 2, Proposition 2, permits a replacement local
slice when it generates the same localized polynomial algebra over
the invariant ring after inverting nonzero polynomials in one invariant.
Theorem 2 then constructs the new Jacobian LND using the irreducible
minimal relation. The following paragraph explicitly discusses changing
the slice and interchanging invariant roles for further iteration.
Section 4.2 proves its Fibonacci-type rank-three examples. Section 5
proves that the component of the basic kernel contains all rank-two
kernels and asks whether the whole graph is connected.[^2]

For the present replacement \(R_*=a(f)r+hQ(f,h)\), the factor
\(a(f)\) is invertible in that localized coefficient field and the
shift is invariant. Hence it satisfies the localized-coordinate
condition. When using the construction theorem, its irreducible
minimal relation must still be selected: a displayed relation with
removable common factors cannot be substituted without that check.
The raw Jacobian's possible replica factor and its primitive plinth
are separate issues.

These results identify the old derivation-construction machinery.
Their inspected statements do not assert that every invariant slice
extension of these new derivations is a coordinate translation on
four-space, and their graph question is not a theorem producing all
rank-three derivations by the project's controlled words. No current
status of that wider graph question is inferred from a 1997 paper.

## 6. Exact implication status and next action

| Claim under comparison | Status established in this audit |
| --- | --- |
| Last-slice surface-cylinder matrix | Already reduced exactly to BPV in the companion comparison. |
| Lifting an isomorphism once full center ideals match | Direct Kaliman--Zaidenberg Proposition 2.1. |
| Higher-weight second center in the P lift | Exact saturation identity (5), transported by (7); no new lifting theorem needed. |
| Higher-weight second center in the Q lift | The same calculation (12)--(13), valid for nonsquarefree a. |
| Existence of the specific corrected Q and P centers | Verified in the project by finite inverse curve jets, extra normal-displacement precision, and CRT. No inspected primary statement has been shown to supply this exact combined assertion automatically. |
| Minimal plinth and all-slice coverage | Separate explicit project calculations, including the quadratic exception and coefficient-only boundary. Not conclusions of the lifting propositions. |

The remaining priority question is now narrower: whether an existing
theorem already supplies these uniform center correspondences and the
resulting extension classification for the stated local-slice families.
This audit has not proved such an implication or established its
absence. A mentor packet should present the result, if retained, as
an explicit family-level application of established cylinder and
affine-modification machinery, with novelty unestablished. Repeating
the abstract universal-property proof would not resolve that question.

No literature inference here upgrades the result to expert-reviewed,
formally verified, or a solution of general cancellation.

## Sources and reading record

[^1]: S. Kaliman and M. Zaidenberg, *Affine modifications and affine
    hypersurfaces with a very transitive automorphism group*,
    Transformation Groups **4** (1999), 53--95. The complete
    Proposition 2.1 and proof, Corollaries 2.2 and 2.3, and the
    surrounding definitions were read in the
    [primary author preprint](https://arxiv.org/pdf/math/9801076),
    Section 2, printed pp. 7--10 of that version. The two-stage
    saturation calculations above are the explicit application here.

[^2]: G. Freudenburg, *Local slice constructions in k[X,Y,Z]*,
    Osaka Journal of Mathematics **34** (1997), 757--767.
    Section 2, Proposition 2 and Theorem 2 with the post-theorem
    iteration discussion; Sections 4.2 and 5.
    [Primary journal scan](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf).
    The scan's displayed formulas have imperfect text extraction;
    no claim depends on inferring an unread formula from OCR.
