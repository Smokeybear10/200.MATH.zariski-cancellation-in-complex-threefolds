# Cancellation research: iterated coordinates and a sharp relative obstruction

Private research continuation, September 12, 2026 local time, continuing
into September 13 UTC.

The corrected complex-threefold cancellation problem is still unsolved:
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\stackrel{?}{\Longrightarrow}\quad X\simeq\mathbb A^3.
\]
The professor has not confirmed this interpretation of the dimensional
typo in the original email. No general proof or counterexample is supplied
here. The results below are restricted working proofs, with internal
reconstructions and exact finite controls. Novelty and human expert
review remain outstanding.

## 1. What this pass changes

The positive coordinate construction now survives an additional
additive local-slice construction, including a genuine rank-three
branch. A finite-chain version also holds under stated hypotheses.
This is a wider class than the single construction treated in
[pass 18](deep-pass-18.md), not a classification of all possible
cancellation factors.

A separate all-base theorem identifies exactly when a principal
modification can preserve the original invariant subring, when the
reduced plinth is connected. It must be constant modulo the full
plinth, including multiplicities. The proof allows every relative
isomorphism, rather than only the canonical rescaling.

Two further deductions locate the unresolved global issue more
precisely. The modification preserves every higher image ideal and
the associated graded algebra, but an original polynomial coordinate
can lose its affine-plane fibers. On the geometric branch, the nodal
candidate now imposes strong restrictions on the actual exceptional
surfaces, not merely on an abstract intermediate curve.

The distinction matters: an isomorphism fixing a selected invariant
subring is stronger than an arbitrary polynomial isomorphism. We have
positive polynomial examples where the former is impossible.

## 2. Exact setup for the all-base statements

Let \(R=\mathbb C[x,y,z]\), let \(D\ne0\) be a primitive locally
nilpotent derivation, and write
\[
C=\ker D,\qquad D(R)\cap C=pC,\qquad Dr=p.
\tag{1}
\]
Thus \(r\) is a minimal local slice. The standard three-variable
kernel and plinth results give \(C\cong\mathbb C^{[2]}\) and a
principal plinth ideal.[^1] For \(0\ne V\in C\) satisfying
\((p,V)C=C\), put
\[
M=R[r/V]=R[w]/(Vw-r).
\tag{2}
\]
The [two-way construction](research/arbitrary-invariant-kernel-pass18.md)
already establishes
\[
M[s]\cong\mathbb C^{[4]},\qquad M_V=R_V,\qquad M_p=C_p[w].
\tag{3}
\]
It does not establish \(M\cong\mathbb C^{[3]}\).
Stable polynomiality makes \(M\) a UFD with constant units; it is
smooth and topologically contractible. These assertions do not use
the cancellation conjecture.

On \(M\), the induced primitive derivation is
\[
\Delta|_R=VD,\qquad \Delta(w)=p,\qquad \ker\Delta=C.
\tag{4}
\]
Its exact plinth remains \(pC\), by localization on the two charts.

## 3. Every higher image ideal survives

For every \(j\ge0\), define \(I_j(D)=D^j(R)\cap C\). The
[complete localization proof](research/global-modification-bridge-pass19.md)
gives
\[
I_j(D)=I_j(\Delta),\qquad
\operatorname{gr}_D R\cong_C\operatorname{gr}_{\Delta}M.
\tag{5}
\]
No principality assumption on the higher ideals is needed.

Here is the whole mechanism. Formation of \(D^j(R)\cap C\)
commutes with localization at an invariant. On the \(V\)-chart,
\(\Delta^j=V^jD^j\), where \(V\) is a unit. On the \(p\)-chart,
both image ideals are the unit ideal, using \(r^j\) and \(w^j\).
The two comaximal opens therefore give equality of the ideals
globally. The normalized leading derivative \(D^j/j!\) identifies
the \(j\)-th graded piece with \(I_j(D)\), compatibly with
multiplication.

This is an all-degree proof, not an extrapolation from the checker.
It also exposes a limitation: even all these leading-term data need
not recover the filtered algebra over the specified \(C\). The
relative counterexamples below have the same graded data. A separate
nonrelative recognition theorem could conceivably exploit (5), but
none is proved here.

## 4. Relative classification with every plinth multiplicity

The full proof is
[Relative isomorphisms of local-slice modifications](research/relative-modification-classification-pass19.md).
Its main statement is:

**Relative theorem.** Under (1)-(2), if \(p\) is nonunit and its
reduced support in \(\operatorname{Spec}C\) is connected, then
\[
R\cong_C M
\quad\Longleftrightarrow\quad
V-c\in pC\ \text{for some }c\in\mathbb C^*.
\tag{6}
\]
For unit \(p\), both rings are polynomial lines over \(C\), so
relative polynomiality is immediate.

### The multiplicity argument

At a prime factor \(f\mid p\), the residue of \(r\) is algebraic
but not rational over \(\operatorname{Frac}(C/(f))\). Algebraicity
comes from the nonzero induced derivation on the residue surface.
Rationality would allow \(ar-b=fu\) with \(f\nmid a\), whence
\(Du=ap/f\). Minimality of \(Dr=p\) would force \(f\mid a\), a
contradiction. This also gives valuation independence:
\[
v_f(qr+b)=\min(v_f(q),v_f(b))
\quad(q,b\in C_V,\ (q,b)\ne(0,0)).
\tag{7}
\]

The finite affine criterion proved in the same note is useful on its
own. Suppose \(\lambda\in C_V^*\), \(b\in C_V\), and
\(\lambda\equiv1\pmod{\sqrt{pC_V}}\). The generic-line map
\(r\mapsto\lambda r+b\) extends even as an endomorphism of \(R_V\)
if and only if
\[
\lambda-1\in pC_V,\qquad b\in pC_V.
\tag{8}
\]
In the positive case its inverse also extends.

For necessity, residue iteration first forces \(b=0\bmod f\).
One then replaces the geometric sum of iterates by a finite binomial
polynomial with error above the required valuation. A Vandermonde
matrix at distinct nonnegative integers has unit determinant in the
local DVR. Thus integrality of all evaluated iterates forces
integrality of its coefficients. The linear coefficient would have
a pole unless (8) contains the full power of \(f\) dividing \(p\).
Equation (7) prevents a multiplier-shift cancellation from hiding it.

### Why this controls every relative isomorphism

Transporting \(D\) through an arbitrary \(C\)-isomorphism \(R\to M\)
gives another primitive derivation with the same kernel. On the generic
line it is a scalar multiple of \(\Delta\). Primitivity and the
constant units of \(M\) make that scalar complex and nonzero.
Consequently the proposed map must have
\[
r\longmapsto a\,r/V+b,\qquad a\in\mathbb C^*,\quad b\in C.
\tag{9}
\]
Residue iteration makes each component residue of \(V\) a nonzero
constant and \(a/V\) a root of unity there. Applying (8) to a common
finite power yields the necessary condition
\[
V^N-a^N\in pC\quad\text{for some }N\ge1.
\tag{10}
\]
On connected support the constants agree. Factoring
\(V^N-c^N\) then gives \(p\mid V-c\), with all multiplicities.
This necessity proof is algebraic; it does not require the separate
geometric theorem concerning units on plinth components.

For sufficiency, if \(V=c+pH\), the finite independent-time flow
\[
\phi(a)=\sum_{j\ge0}\frac{(-Hw)^j}{j!}D^j(a)
\]
sends \(r\) to \(cw\). The inverse sends \(w\) to \(r/c\) and,
on \(R\), evaluates the flow at \(Hr/c\). Both maps are polynomial;
their compositions are checked on the generic line and hence globally.
These are evaluated finite flows, not an assertion that a
noninvariant multiple of \(D\) is locally nilpotent.

The kernel-fixing affine framework has a predecessor in Kuroda's
primary announcement.[^2] The pure-translation automorphism subcase
of (8) also follows from Stampfli's kernel-fixing centralizer lemma;
his proof already uses interpolation of iterates and differentiation.[^7]
The present proof checks nontrivial near-identity multipliers,
endomorphisms, localized modifications and full multiplicities
explicitly. Priority for the resulting theorem remains unestablished.

### Disconnected support is a real boundary

Take \(p=x(x-1)\), \(D=p\partial_y+2y\partial_z\),
\(h=pz-y^2\), \(r=y\), and \(V=2x-1\). Then
\(V^2-1=4p\). In \(M\), put \(z'=z-4w^2\). The relation becomes
\(h=pz'-w^2\), giving a \(C=\mathbb C[x,h]\)-isomorphism even though
the two residues of \(V\) are different. Condition (10) allows this.
It is not asserted sufficient for arbitrary disconnected plinths.

## 5. A positive theorem beyond one construction step

The [complete coordinate and inverse proof](research/iterated-local-slice-bridge-pass19.md)
starts with the pass-18 data
\[
\begin{split}
&f=xz-F(y),\qquad r=xP(x,f)+yf^n,\\
&G(T,S)=S^dF(T/S),\qquad K(f,T)=G(T,f^n)+f^{nd+1},\\
&xh=K(f,r),
\end{split}
\tag{11}
\]
where \(F\) is monic of degree \(d\ge2\), \(n\ge1\), and
\(P(x,0)\) is nonconstant.

For any polynomial \(Q(f,h)\), make an actual additional local-slice
construction:
\[
r_2=r+hQ(f,h),\qquad
k=x+Q(f,h)\Delta_G(r_2,r;f^n)=K(f,r_2)/h,
\qquad D_2=\operatorname{Jac}(f,k,\cdot).
\tag{12}
\]
Here \(\Delta_G\) is the polynomial divided difference in the first
argument. The forward and reverse surface transformations are
polynomial. Their established construction machinery is prior work,
not a claimed invention here.[^1]

**One-step preservation theorem.** Every invariant slice extension
\(AD_2+B\partial_t\), with \(A,B\in\ker D_2\), has polynomial
three-variable kernel.

The proof distinguishes the boundary cases exactly. If \(Q(0,H)=0\),
the derivation has rank two and plinth \((k)\); finite reparametrization
produces a local slice of derivative \(k\), and a published
ambient-invariant-coordinate result applies. If \(Q(0,H)\ne0\),
the direct residue-degree calculation gives primitivity, rank three,
kernel \(\mathbb C[f,k]\), and exact plinth \((f^nk)\).

In the rank-three branch the slice criterion is
\[
(A,B)=\mathbb C[f,k],\qquad B=c+fkJ,\quad c\ne0.
\tag{13}
\]
Necessity retains the source-dependent affine-replacement proof
from pass 17. Sufficiency and the explicit coordinates use only
the displayed algebraic conditions.

### How the denominator repair works

Normalize \(c=1\), choose \(Af^nkU+BV=1\), and set
\(\rho=Br_2-Af^nkt\), \(\sigma=Ur_2+Vt\).
The first is invariant and \(E\sigma=1\). Form
\(\widehat h=K(f,\rho)/k\), then reverse (12) to obtain
\(\widehat r,\widehat x\). All these are polynomials; the first
division is justified by \(\rho-r_2\in kR[t]\).

The remaining issue is genuinely nonlinear. Modulo \(f^n\), the
surface is the cone \(xh=r^d\). Conjugating the final scaling by
the surface mutation gives a vertex-preserving cone automorphism
\(\alpha\) equal to the identity modulo \(f\). On the original curve
\((x,h,r)=(u,u^{d-1}P(u,f)^d,uP(u,f))\), write
\[
\alpha(x)=uU_0(u,f),\qquad
\alpha(r)=uV_0(u,f),\qquad U_0\equiv1\pmod f.
\tag{14}
\]
Over \(\mathbb C[f]/(f^n)\), \(U_0\) is a unit and
\(\beta(u)=uU_0(u,f)\) has a finite polynomial inverse \(j\).
Define
\(\widetilde P(X,f)=(V_0/U_0)(j(X,f),f)\).
The cone relation gives the entire transformed curve, including
its \(h\)-coordinate. The inverse automorphism recovers the original
curve scheme-theoretically, including all the nilpotent orders.

Consequently
\[
Y=(\widehat r-\widehat x\widetilde P(\widehat x,f))/f^n
\tag{15}
\]
is polynomial. Taylor expansion gives a polynomial \(Z\) with
\(f=\widehat x Z-F(Y)\). The higher denominator \(f^{nd}\) is
removed by this identity and the coprimality
\(\gcd(\widehat x,f)=1\), not by a separate infinite-series argument.

The inverse is constructed in independent variables
\((X,Y,Z,\sigma)\): recover \(f,\widehat r,\widehat h\), apply
the forward surface mutation, invert the slice matrix, reverse the
mutation, and use the inverse finite-curve congruence to recover
polynomial \(x,y,z,t\). Both quotient divisions are justified in
that independent polynomial ring. This produces actual global
coordinates, not only an isomorphism of formal neighborhoods.

### Negative control and finite-chain scope

For \(F(y)=y^2\), \(P=x^2\), \(n=2\), \(Q=h\), and \(B=1+fk\),
put \(k_0=x(1+x^7)^2\). The uncorrected formula fails:
\[
\widehat r-\widehat x^3
=fk_0x^3(1+15x^7)\pmod{f^2}.
\tag{16}
\]
Thus division by \(f^2\) leaves an actual pole. The repaired jet is
\[
\widetilde P(X,f)=X^2+
fX^3(1+X^7)^2(1+15X^7)\pmod{f^2}.
\tag{17}
\]
The checker reconstructs the inverse independently at orders two
and three. This failure refutes only the uncorrected formula.

The same proof works for a finite composition of these additive
surface mutations, provided the final kernel, local-slice derivative
\(f^nk\), and coefficient conditions (13) hold. Claiming that
**every** slice extension of a longer chain is covered additionally
requires checking its minimal plinth or an alternative necessity
argument. No classification of all rank-three derivations, arbitrary
changes of invariant generators, or nonunit slice multipliers is
included.

## 6. Why the original coordinate is not a global shortcut

The explicit [fiber control](research/global-modification-bridge-pass19.md)
uses
\[
f=xz-y^2,\quad r=x^2+yf^2,\quad
h=zf^4+2xyf^2+x^3,\quad p=f^2h,\quad V=1+fh.
\]
The modification is already known to be a polynomial three-ring
from pass 18. Nevertheless, its old coordinate \(x\) has zero fiber
\[
M/(x)\cong\mathbb C[y,z,(1-y^{10}z)^{-1}],
\tag{18}
\]
which is not an affine plane because it has a nonconstant unit.
The successful new first coordinate is
\(X=x-fw(w+r)=(w^2+f^5)/h\).
An arbitrary original affine-plane fibration therefore need not
survive the modification.

Primary recognition theorems give meaningful alternative targets:
find some new regular function on \(\operatorname{Spec}M\) with a
trivial affine-plane family on an open subset of the line and
reduced irreducible factorial fibers.[^3] Another version asks for
general affine-plane fibers and at most isolated singularities in
every closed fiber.[^4] The existence of such a function is the
missing assertion, not a consequence of (3) or (5).

The inspected modification theorem preserving topological
contractibility has a weaker conclusion than polynomiality.[^4]
Likewise, two independent additive actions can determine the
quotient surface without determining the total threefold. A
fixed-point-free action on four-space fixing an ambient polynomial
variable is a translation, but that variable is still a genuine
extra hypothesis.[^5]

## 7. Actual exceptional surfaces for the nodal candidate

The [surface-constraint proof](research/nodal-surface-constraints-pass19.md)
examines a hypothetical primitive quotient on \(\mathbb C^3\) whose
retained exceptional support is the two nodal fibers
\(\Gamma_\pm=V(v^2-u^3+3u\mp2)\).
It uses Kaliman's actual quotient homology diagram and its
normalization comparison, with their ambient hypotheses retained.[^6]

At an exceptional base point \(b\), let \(q_b\) count normalization
branches of the intermediate curve, and \(c_b\) count irreducible
components of the actual reduced quotient fiber. Excision in the
smooth ambient threefold and the integral diagram give
\[
c_b=q_b\ \text{at smooth base points},\qquad
c_b=q_b-1\ \text{at nodes}.
\tag{19}
\]
The node ramification indices must also have greatest common divisor
one. Additivity of compact-support Euler characteristic then forces
every exceptional fiber to be a disjoint union of unibranch curves
with affine-line normalization.

In particular the previous four-branch, degree-two intermediate
curve would require **three disjoint contractible irreducible
curves** above a node. An intersecting tree of three curves fails.
Each exceptional surface also has only
\(H_c^3\cong\mathbb Z\) and \(H_c^4\cong\mathbb Z\) nonzero,
and the entire node fiber lies in its singular locus.

These conditions do not yet contradict existence. The intermediate
one-point condition does not imply connectedness of the actual
affine fiber: the map comes from restricting a proper Stein-factor
construction, and deleting the boundary can disconnect that fiber.
Nilpotents and multiplicities remain uncontrolled. No such
exceptional surfaces or LND have been constructed here.

## 8. Verification and research status

The two new standalone checkers are:

~~~sh
/opt/anaconda3/bin/python research/global_bridge_checks_pass19.py
/opt/anaconda3/bin/python research/iterated_local_slice_checks_pass19.py
~~~

They add twelve and four methods respectively. They import no
research solver. The first checks affine iterates, finite truncation,
valuation controls, explicit relative inverses, the disconnected
positive case, the failed fiber, and bounded higher-image examples.
The second checks the surface mutation and inverse, the failed
uncorrected formula, the repaired curve in both directions, and
the rank-two branch's finite local-slice correction.

The main agent reran all suites from 03:46:50 to 03:48:07 UTC on
September 13, 2026. **All 420 methods across 31 suites passed.**
The complete execution record is
[verification-pass-19.json](verification-pass-19.json); the full
suite commands are in [README.md](README.md).
Finite identity tests do not prove the general theorems, verify the
topological source results, or constitute Lean formalization.
Separate model reconstructions are not human expert review.

Two separate reconstructions found no gap in the relative proof.
The independent iterated-coordinate audit checked the universal
nonreduced-curve cancellation, inverse specialization, both global
divisibilities, and the finite-chain scope, also finding no gap.
Its independent four-test execution is not added to the method count.

The literature boundaries are recorded both in the
[global-recognition note](research/global-modification-bridge-pass19.md)
and the [targeted statement comparison](research/literature-boundary-pass19.md).
Established local-slice machinery, kernel-automorphism frameworks,
and recognition theorems must be credited. No priority claim follows
from a missing search match.

The new comparison with Blanc, Poloni and Van Santen's Lemma 3.1
is particularly close: it constructs inverse cylinder maps from
approximate polynomial inverses and two ideal inclusions.[^8]
To derive the present lift from it, one must exhibit the required
global hypersurface presentation and verify both inclusions for the
physical overring. That comparison remains unfinished. Finite-jet
inversion alone is not a defensible novelty claim.

## 9. The remaining mathematical obligations

To use the invariant-extension route for unrestricted cancellation,
two distinct steps remain:

1. Recognize arbitrary principal modifications (2) as polynomial
   rings, allowing an isomorphism that moves the embedded invariant
   subring, or prove a sufficient classification placing them in a
   handled class.
2. Reduce an arbitrary slice derivation on \(\mathbb C^{[4]}\)
   to that invariant-extension setting, or find another unrestricted
   argument.

The next bounded construction task is to allow a nonunit
multiplicative change of local slice, \(r_*=a(f,h)r+b(f,h)\),
and determine exactly which extra denominator ideals replace the
invertible additive mutation used above. A positive extension needs
a polynomial inverse on the physical ring; failure needs an explicit
divisor or residue witness. The closed additive case should not be
rerun as if it were still an open proof gap.

On the geometric branch, progress requires an actual surface
realization or an additional obstruction compatible with (19),
not another abstract nodal-curve example.

No external contact, submission, public posting, payment, or
automation was performed. The unrestricted goal remains active
and unsolved.

## Primary sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484. Theorems 2.8, 2.10 and 2.17; Lemma 2.15(ii) and Lemma 4.3. The local-slice construction is credited there to Freudenburg. Present coordinate-preservation deductions are separately proved, not quoted as statements from this paper.

[^2]: S. Kuroda, [*The automorphism group of a UFD over the kernel of a locally nilpotent derivation*](https://www.math.okayama-u.ac.jp/~hashimoto/paper/Comm-Alg/35/jsca35kurodas.pdf), primary symposium announcement, Propositions 2.1-2.2 and Theorem 2.4. Its announced status is not silently upgraded to a complete journal proof.

[^3]: S. Kaliman and M. Zaidenberg, [*Miyanishi's characterization of the affine 3-space does not hold in higher dimensions*](https://www.numdam.org/item/10.5802/aif.1803.pdf), *Annales de l'Institut Fourier* 50 (2000), 1649-1669, introduction at 1649-1650. The three-dimensional recognition assumptions are used exactly as stated.

[^4]: A. Dubouloz, S. Pauli and P. A. Østvær, [*A1-contractibility of affine modifications*](https://arxiv.org/pdf/1805.08959), *International Journal of Mathematics* 30 (2019), 1950069, Theorems 2.4, 2.6 and 2.7. The recognition statements and their attribution, and the separate contractibility conclusion, were checked directly.

[^5]: R. V. Gurjar, M. Koras, M. Miyanishi and P. Russell, [*Affine threefolds admitting Ga-actions*](https://arxiv.org/pdf/1502.01849v1), Theorems 1.1 and 3.1. The quotient conclusion and the ambient invariant-variable premise are distinct.

[^6]: S. Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Lemmas 2.1-2.2, Proposition 3.2 and Remark 3.3. The conditional surface deduction uses the actual ambient diagram, not just a proposed finite curve map.

[^7]: I. Stampfli, [*Automorphisms of C3 commuting with a C+-action*](https://arxiv.org/pdf/1406.6246), Lemma 5.1.2 and its proof. The pure-translation overlap is known; the same interpolation method is not presented as newly invented.

[^8]: J. Blanc, P.-M. Poloni and I. Van Santen, [*Complements of hypersurfaces in projective spaces*](https://jep.centre-mersenne.org/item/10.5802/jep.264.pdf), *Journal de l'École polytechnique, Mathématiques* 11 (2024), Lemma 3.1, 740-741. The complete statement and both inverse formulas were checked directly.
