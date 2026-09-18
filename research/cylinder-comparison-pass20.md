# Exact cylinder overlap and the remaining weighted-overring lift

Private bounded pass 20, 2026-09-13. This comparison replaces a vague
method resemblance by an exact reduction. The final surface-cylinder
map in pass 19 is a Blanc--Poloni--Van Santen cylinder map, followed
by an elementary ideal-preserving modification. The extra extension
to the physical polynomial ring is a separate, explicitly proved
weighted-overring lemma below. A direct hypersurface presentation
using the jet parameter \(f\) is impossible. These conclusions do
not establish novelty, rule out all alternative published reductions,
or solve cancellation.

The complete [pass-19 construction](iterated-local-slice-bridge-pass19.md)
and [prior boundary audit](literature-boundary-pass19.md) were read.
The targeted primary lemma and proof, Moser-Jauslin--Poloni Section 4,
and their Proposition 5.2.1 and proof were read directly.

## 1. What the published cylinder lemma supplies

Blanc--Poloni--Van Santen, Lemma 3.1, uses
\(S=\mathbb k[x_0,\ldots,x_s]\), hypersurfaces
\(x_0^ny=P(z)\), \(x_0^ny=Q(z)\), and polynomials
\(a,b\in S[z]\). Its assumptions are
\[
a\circ b\equiv b\circ a\equiv z\pmod{x_0^m},
\]
\[
Q(a(z)+x_0^mw)\in(x_0^n,P(z)),\qquad
P(b(z)+x_0^mw)\in(x_0^n,Q(z)).
\tag{1}
\]
The cylinder map has new coordinates
\[
z'=a(z)+x_0^mw,\qquad
y'=Q(z')/x_0^n,\qquad
w'=(z-b(z'))/x_0^m.
\tag{2}
\]
Interchanging \((P,a)\) with \((Q,b)\) gives its inverse. The
proof verifies regularity by (1) and computes both compositions.
The paper explicitly credits Moser-Jauslin--Poloni as the inspiration
for these formulas.[^1]

We apply the lemma below to integral hypersurfaces, so every displayed
fraction has its unambiguous meaning in the corresponding localization.

## 2. A literal global specialization gives the last-slice matrix

Retain the pass-19 notation
\[
K(f,z)=G(z,f^n)+f^{nd+1},\qquad
\mathscr A=\frac{\mathbb C[f,k,h,r_*]}{(kh-K(f,r_*))},
\tag{3}
\]
where \(G(R,S)=S^dF(R/S)\), with \(F\) monic of degree
\(d\ge2\). This is the actual global abstract surface family,
not only its localization at \(f\). The polynomial in (3) is
primitive linear in \(h\), since \(k\) and the nonzero monic
polynomial \(K(f,r_*)\) are coprime. Hence \(\mathscr A\) is
a domain.

Write the invariant coefficients as \(A,B\in\mathbb C[f,k]\),
normalize \(B=1+fkJ\), and choose \(U,V\) with
\[
Af^nkU+BV=1.
\tag{4}
\]
Assume \(A\ne0\) for the modification description; the case
\(A=0\) makes \(B\) a unit and is elementary. Put \(g=Af^n\).
Take the following exact inputs to the published lemma:
\[
S=\mathbb C[k,f],\quad x_0=k,\quad m_{m BPV}=n_{m BPV}=1,
\quad P_{m BPV}=Q_{m BPV}=K(f,z),
\]
\[
a(z)=Bz,\qquad b(z)=Vz.
\tag{5}
\]
Both required approximate-inverse differences equal
\[
z-a(b(z))=z-b(a(z))=(1-BV)z=gkUz\in kS[z].
\tag{6}
\]
Moreover \(B\equiv V\equiv1\pmod{k}\), the latter from (4).
Consequently both ideal inclusions are explicit:
\[
K(f,Bz+kw)-K(f,z)\in kS[z,w],
\]
\[
K(f,Vz+kw)-K(f,z)\in kS[z,w].
\tag{7}
\]
Thus (1) is satisfied without any hypothesis on simple roots of
\(K\). Formula (2) gives the global cylinder isomorphism
\[
\rho=Br_*+kw,\qquad
\widehat h=K(f,\rho)/k,\qquad
\omega=gUr_*-Vw.
\tag{8}
\]
Its inverse satisfies
\[
r_*=V\rho+k\omega,\qquad w=gU\rho-B\omega.
\tag{9}
\]
The formulas for \(h,\widehat h\) are regular by (7).

There is one precise extra operation before (8) becomes the pass-19
matrix: adjoin \(w/g\). The ideal \((g,w)\) is transported to
\((g,\omega)\) in both directions, by (8)--(9). Since the map
fixes \(g\), it therefore lifts to the modifications adjoining
\(w/g\) and \(\omega/g\). This also follows immediately by
dividing those two explicit formulas by \(g\).

Set \(w=-gt\) and \(\omega=g\sigma\). Because the original
\(w\) is transcendental and \(g\ne0\), adjoining \(w/g\)
again gives a polynomial cylinder over \(\mathscr A\). Equations
(8)--(9) become exactly
\[
\rho=Br_*-Af^nk t,\qquad
\sigma=Ur_*+Vt,
\]
\[
r_*=V\rho+Af^nk\sigma,\qquad t=-U\rho+B\sigma.
\tag{10}
\]
No inversion of \(f\), \(A\), or \(B\) has occurred in these
global cylinder rings.

**Exact credit boundary.** The last-slice surface-cylinder map is
therefore an explicit consequence of the published lemma plus this
elementary stable-ideal modification. It should not be presented as
a new cylinder-isomorphism mechanism. This conclusion is stronger
than observing similar-looking formulas.

### Equivalent two-denominator formulation

For completeness, the same calculation can be packaged as a small
extension of (1)--(2). Let \(S\) be a domain, \(0\ne d,e\in S\),
and assume \(S[y,z]/(dy-P)\) and \(S[y,z]/(dy-Q)\) are domains
embedding in \(S_d[z]\). Suppose
\[
a\circ b\equiv b\circ a\equiv z\pmod e,
\quad Q(a(z)+ew)\in(d,P),\quad P(b(z)+ew)\in(d,Q).
\tag{11}
\]
Then
\[
z'=a(z)+ew,\quad y'=Q(z')/d,\quad w'=(z-b(z'))/e
\tag{12}
\]
and the swapped formulas are inverse cylinder maps. Indeed, the
ideal inclusions make \(y'\) regular. The congruence and the
polynomial divided difference of \(b\) make \(w'\) regular.
The two compositions recover \(z,w\), then \(y\) in the
localization at \(d\). Injectivity into that localization proves
the same equalities globally. This is the published proof with two
arbitrary nonzero denominators, not an independent new technique.

For (10), set \(d=k\), \(e=Af^nk\), \(a(z)=Bz\),
\(b(z)=Vz\), and take the free input coordinate to be \(-t\).
Equation (4) verifies the stronger congruences modulo \(e\), and
(7) verifies the two ideal inclusions. Formula (12) then gives
\(\sigma=(r_*-V\rho)/e\) directly.

As a finite control, exact SymPy expansion also checked (4), both
matrix inverse identities, both \(K\)-ideal inclusions, and the
substitution \(\omega=g\sigma\) with the nonunit coefficient
\(A=1+f^2k(1+fk)\), \(B=1+fk\), \(U=k\),
\(V=1-fk-f^4k^3\), \(K(f,z)=z^2+f^5\).
All six checks passed. They supplement the displayed symbolic proof.

## 3. The physical ring is a different overring

Return to the original global surface presentation
\[
\mathscr A_0=
\frac{\mathbb C[f,x,h,r]}{(xh-K(f,r))}.
\]
For \(P(x,f)\in\mathbb C[x,f]\), define two elements of this
ring, with no denominators:
\[
a_P=r-xP(x,f),
\]
\[
b_P=h-P(x,f)\Delta_G(r,r-xP(x,f);f^n),
\tag{13}
\]
where \(\Delta_G\) is the polynomial divided difference in its
first argument. Their exact relation is
\[
xb_P=G(a_P,f^n)+f^{nd+1}.
\tag{14}
\]
The physical ring is
\[
\mathscr R_P=\mathscr A_0[a_P/f^n,b_P/f^{nd}]
\subset(\mathscr A_0)_f.
\tag{15}
\]
Writing \(y=a_P/f^n\), \(z=b_P/f^{nd}\), (14) gives
\[
xz=F(y)+f.
\tag{16}
\]
Conversely (16), \(r=xP(x,f)+yf^n\), and the definition of
\(b_P\) recover all of \(\mathscr A_0\). These formulas give
the exact isomorphism
\[
\mathscr R_P\cong
\frac{\mathbb C[f,x,y,z]}{(xz-F(y)-f)}
\cong\mathbb C[x,y,z].
\tag{17}
\]
For example, one can check both substitutions after inverting
\(f\), then use the domain presentations. In particular \(f\)
is prime in \(\mathscr R_P\), and \(f\nmid x\).

The single modification ideal underlying (15) can be written
\[
I_P=(f^{nd},\ f^{n(d-1)}a_P,\ b_P)\subset\mathscr A_0,
\quad \mathscr R_P=\mathscr A_0[I_P/f^{nd}].
\tag{18}
\]
An automorphism of \(\mathscr A_0[t]\), even one supplied
exactly by a cylinder lemma, need not preserve these prescribed
fractions. The negative control in pass-19 Section 7 makes the
uncorrected first fraction have an actual \(f\)-pole. The
surface-cylinder conclusion alone is therefore not the physical-ring
conclusion.

There is also a concrete obstruction to stopping after the first
fraction. Direct substitution in (14) gives
\[
\mathscr A_0[a_P/f^n]
\cong\frac{\mathbb C[f,x,y,H]}
 {(xH-f^{nd}(F(y)+f))}.
\tag{19}
\]
Here \(H=b_P\), and the domain presentation is checked by
localizing at \(f\). Modulo \(f\), (19) becomes \(xH=0\),
a reducible surface. But (17) modulo \(f\) is the integral
surface \(xz=F(y)\). Even their cylinders cannot be isomorphic
over \(\mathbb C[f]\). The second fraction in (15) is not
an optional simplification.

## 4. No direct \(f\)-power hypersurface presentation of the physical ring

**Proposition.** For monic \(F\) of degree \(d\ge2\), the
\(\mathbb C[f]\)-algebra in (17) has no presentation
\[
\frac{\mathbb C[f,u,v,w]}{(f^Nv-L(f,u,w))},
\qquad N\ge1.
\tag{20}
\]

**Proof.** Its fiber at \(f=0\) is the integral surface
\(S_F=\{xz=F(y)\}\). Formula (20) would make that fiber
\(\Gamma\times\mathbb A^1\), where
\(\Gamma=\operatorname{Spec}\mathbb C[u,w]/(L(0,u,w))\).
Integrality and dimension of \(S_F\) force \(\Gamma\) to be
an integral affine curve. This excludes zero, unit, and nonreduced
degeneracies of the equation.

If \(F\) has a repeated root, the singular locus of \(S_F\)
is the nonempty finite set
\[
\{x=z=0,\quad F(y)=F'(y)=0\}.
\]
The singular locus of a curve times \(\mathbb A^1\) is either
empty or contains a line, a contradiction.

If \(F\) is squarefree, then \(S_F\) and hence \(\Gamma\)
are smooth. The locus \(x\ne0\) of \(S_F\) is
\(\mathbb C^*\times\mathbb C\), while \(x=0\) consists
of \(d\) disjoint affine lines. Additivity of compactly supported
Euler characteristic gives \(\chi_c(S_F)=d\ge2\). A smooth
connected affine curve, obtained from a compact curve of genus
\(g\) by deleting \(r\ge1\) points, has
\(\chi_c(\Gamma)=2-2g-r\le1\). Since
\(\chi_c(\mathbb A^1)=1\), this is again a contradiction.

The two cases prove the proposition. The proof was independently
crosschecked in pass 20, including the domain qualification.

Thus taking the BPV base coordinate \(x_0\) to be the jet parameter
\(f\) cannot produce the needed global physical-ring presentation.
This does **not** exclude using another base coordinate, another
cylinder presentation, or a more elaborate sequence of existing
constructions. It rules out this exact proposed direct specialization.

## 5. A precise weighted-overring extension lemma

The following abstracts the additional compatibility proved in pass 19.
It separates that issue from the already identified cylinder step.

**Lemma.** Let \(\Phi\) be a \(\mathbb C[f]\)-automorphism
of \(\mathscr A_0[t]\). Suppose that, modulo \(f^n\), its
restriction to the surface subalgebra induces an automorphism
\[
\alpha:\frac{S_n[x,h,r]}{(xh-r^d)}
 \longrightarrow\frac{S_n[x,h,r]}{(xh-r^d)},
\qquad S_n=\mathbb C[f]/(f^n),
\]
independent of the cylinder variable. Assume that \(\alpha\)
preserves the vertex ideal \((x,h,r)\) and is the identity
modulo \(f\). Then for every \(P\) there is a finite jet
\(\widetilde P\in\mathbb C[x,f]\), with
\(\widetilde P(x,0)=P(x,0)\), such that \(\Phi\) extends to
an isomorphism
\[
\mathscr R_{\widetilde P}[t]\longrightarrow\mathscr R_P[t].
\tag{21}
\]
The direction here is the direction of the map on coordinate rings.

**Proof.** On the universal \(P\)-curve in the cone, evaluate
\((x,h,r)=(u,u^{d-1}P(u,f)^d,uP(u,f))\). Vertex preservation
and the identity modulo \(f\) give
\[
\alpha(x)=uU(u,f),\quad \alpha(r)=uW(u,f),
\quad U\equiv1\pmod f.
\]
Let \(\beta(u)=uU(u,f)\). In \(S_n[u]\), \(U\) is a
unit, and \(\beta\) has a finite polynomial inverse \(j\).
For any polynomial lifts, these are the two exact approximate-inverse
congruences
\[
\beta(j(X))\equiv X\pmod{f^n},\qquad
j(\beta(u))\equiv u\pmod{f^n}.
\tag{22}
\]
Set \(\widetilde P=(W/U)\circ j\) modulo \(f^n\), and choose
its representative of degree less than \(n\) in \(f\).
The cone relation then gives
\[
\alpha(h)=\beta(u)^{d-1}
 \widetilde P(\beta(u),f)^d.
\]
Only the indeterminate \(u\) is cancelled here; it is a
nonzerodivisor in \(S_n[u]\). The inverse curve identity holds
universally as well.

This supplies explicit ideal inclusions. Define
\[
J_P=(f^n,a_P,b_P)\subset\mathscr A_0.
\tag{23}
\]
Modulo \(f^n\), this is the kernel of evaluation on the
\(P\)-curve: it also equals the ideal generated by
\(r-xP\) and \(h-x^{d-1}P^d\) in the cone. The two curve
identities give
\[
\Phi(J_{\widetilde P})\subset J_P\mathscr A_0[t],
\qquad \Phi^{-1}(J_P)\subset J_{\widetilde P}\mathscr A_0[t].
\tag{24}
\]
They are scheme-theoretic congruences over \(S_n\), not only
conditions on reduced points.

In \(\mathscr R_P[t]\), every generator of \(J_P\) is
divisible by \(f^n\). Hence
\[
y'=\Phi(a_{\widetilde P})/f^n\in\mathscr R_P[t].
\tag{25}
\]
For the higher-weight generator use the exact surface relation (14):
\[
\Phi(x)\Phi(b_{\widetilde P})
 =f^{nd}\bigl(F(y')+f\bigr).
\tag{26}
\]
Now \(f\) is prime in the polynomial UFD \(\mathscr R_P[t]\),
and \(\Phi(x)\equiv x\not\equiv0\pmod f\). Equation (26)
therefore forces
\[
z'=\Phi(b_{\widetilde P})/f^{nd}\in\mathscr R_P[t].
\tag{27}
\]
Equations (25)--(27) are precisely the extra inclusions needed for
the two fractions in (15). The argument for \(\Phi^{-1}\) is
identical, using the inverse universal curve identity and primeness
of \(f\) in \(\mathscr R_{\widetilde P}\). Both extensions are
the original inverse maps in the common \(f\)-localized rings,
so they remain inverse globally. This proves (21).

The lemma requires more than approximate inverse polynomials (22):
it uses the curve-center ideals (24), the weighted relation (26),
and the prime divisor in the larger polynomial ring. Those are the
specific additional compatibility statements. They do not follow
merely by renaming variables in the one-denominator surface-cylinder
presentation.

### Application to the additive word

Every pass-19 additive mutation is a global polynomial isomorphism
of \(\mathscr A_0\), and modulo \(f^n\) it preserves the cone
vertex. Conjugate the exact cylinder map (10) by a finite such word.
Its reduced surface map is
\(\alpha=\mu^{-1}\sigma_B\mu\), where
\[
\sigma_B(h,k,r_*)=(B^dh,k,Br_*).
\]
Because \(B\equiv1\pmod f\), this is an automorphism of the
nilpotent cone and is the identity modulo \(f\). The lemma applies.
The constructed surface coordinates are invariant for the extension,
and \(\sigma\) is its slice, so the extended polynomial map gives
the claimed polynomial kernel. This recovers pass-19 Sections 4--6
as **the published cylinder construction plus the weighted-overring
extension lemma**, with an exact proof of the second part.

The final derivation's kernel and local-slice hypotheses from pass 19
are still needed. This is not a generation theorem for arbitrary LNDs.

## 6. What Moser-Jauslin--Poloni does and does not remove

Moser-Jauslin--Poloni Theorem 4.0.1 begins with a special Danielewski
surface that is a principal bundle over the line with several origins.
It constructs its cylinder isomorphism using finite Hermite congruences
and a slice. Proposition 5.2.1 treats two classical surfaces with
simple-root defining polynomials.[^2] The abstract surface family
(3) specializes at \(f=0\) to \(kh=r_*^d\), whose cone vertex
is singular and whose \(k=0\) fiber is nonreduced. It does not
satisfy those special-surface hypotheses. On fibers \(f=a\) where
\(K(a,z)\) has simple roots, their constructions are pertinent,
but they supply no extension over this excluded degeneration or
the weighted overring (15).

Thus this source must receive credit for the cylinder/slice/congruence
method, but its displayed statements do not replace the specific
compatibility proof in Section 5. No claim excluding an alternative
global presentation or a further consequence of their work is made.

## 7. Decision for the next research pass

The exact overlap settles a meaningful part of the priority question:
do not spend another pass treating the last-slice matrix or its
surface-cylinder inverse as new. Any candidate statement or mentor
packet should isolate the weighted-overring extension criterion and
its uniform application to the controlled additive words. A further
priority audit should target that statement, especially affine
modification lift criteria with nonreduced curve centers, rather than
searching again for generic similarities to cylinder formulas.

It has not been proved that no finite sequence of other published
cylinder constructions could imply the entire result. The concrete
outcome is narrower: an exact inherited step, an impossible direct
\(f\)-presentation, and a proved extra compatibility lemma.

## Sources

[^1]: J. Blanc, P.-M. Poloni and I. Van Santen,
    *Complements of hypersurfaces in projective spaces*, Journal de
    l'École polytechnique, Mathématiques **11** (2024), 733--768,
    Lemma 3.1 and its complete proof, printed pp. 740--741.
    [Primary journal PDF](https://jep.centre-mersenne.org/item/10.5802/jep.264.pdf).

[^2]: L. Moser-Jauslin and P.-M. Poloni,
    *Isomorphisms between cylinders over Danielewski surfaces*,
    Section 4, Theorem 4.0.1, and Proposition 5.2.1 with its proof.
    [Primary author preprint](https://arxiv.org/pdf/2002.12202).
