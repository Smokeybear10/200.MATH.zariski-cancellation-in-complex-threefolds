# All higher image ideals for the canonical rank-three derivation

For the canonical Freudenburg derivation used in this project, every
higher image ideal is principal. With the notation below, the exact formula is
\[
\boxed{J_n=\Delta^n(R)\cap C
=f^{\,n-\lfloor n/5\rfloor}g^{\,\lceil n/2\rceil}C
\quad(n\ge0).}
\tag{1}
\]
Here \(J_0=C\). This is a reconstruction of an already computed
rank-three example, not a general proof of the Freeness Conjecture.
There is no nonprincipal image ideal or hidden origin-supported
associated-prime obstruction in this example.

## 1. Existing work and exact source identification

The authoritative existing
[full coefficient classifier](full_coefficient_classifier.py)
decides membership in \(\Delta(R)\) by ordinary homogeneous linear
algebra. Its slice classification concerns the fixed family
\(\Delta+a\partial_t\), including noninvariant \(a\), and is
proved in [arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md).
That completed coefficient-slice work is not repeated here. Its
degree shift is ordinary degree four, not the derivation degree used
in the present note.

Let
\[
\begin{aligned}
R&=\mathbb C[x,y,z],& f&=xz-y^2,\\
g&=zf^2+2x^2yf+x^5,& r&=-x^3-fy,\\
S&=x^2y+fz,& \Delta&=\operatorname{Jac}(f,g,\cdot),
\qquad C=\ker\Delta=\mathbb C[f,g].
\end{aligned}
\]
The polynomial identities are
\[
\Delta r=fg,\quad \Delta x=2fr,\quad
\Delta y=-g-6x^2r,\quad \Delta z=2xf^2-10xyr,
\quad r^2+f^3=xg,\quad fS=rx^2+g.
\tag{2}
\]

[Freudenburg, *Canonical Factorization of the Quotient Morphism for an
Affine Ga-Variety*, Sections 8.2.1, 8.2.7 and 8.2.8](https://arxiv.org/html/1602.08786v3#S8.SS2)
uses the same \(f,g,S\) and the same Jacobian derivation. His capital
\(R\) equals \(-r\), so his identity \(D(R)=-FG\) agrees exactly
with (2). Corollary 8.5 supplies an adapted basis in every derivation
degree. Section 8.2.8 gives
\[
\operatorname{Gr}_{\Delta}(R)
=C[fgT,f^2gT^2,f^4g^3T^5,f^5g^3T^6,f^8g^5T^{10}].
\tag{3}
\]
The next sections independently recover the coefficient ideals and
explicit witnesses from two presentations of the same ring.

## 2. The chart where f is invertible

The exact presentation is
\[
R_f=C_f[x,r]/(r^2-gx+f^3),
\qquad
y=-\frac{r+x^3}{f},\quad
z=\frac{g+2x^2r+x^5}{f^2}.
\tag{4}
\]
It is free over \(C_f[x]\) with basis \(1,r\). Over
\(\operatorname{Frac}(C)\), one has
\[
x=(r^2+f^3)/g,\qquad \Delta=fg\partial_r.
\]
The normal-form monomials \(x^j r^\epsilon\),
\(j\ge0\), \(\epsilon\in\{0,1\}\), have distinct
derivation degrees \(2j+\epsilon\). Their leading coefficients
as polynomials in \(r\) are \(g^{-j}\).
Consequently
\[
J_n C_f=f^n g^{\lceil n/2\rceil}C_f.
\tag{5}
\]
In particular every element of \(J_n\subset C\) is divisible by
\(g^{\lceil n/2\rceil}\).

## 3. The chart where g is invertible

The apparent quotient
\[
q=\frac{r^5+g^3}{f}
=g^2S-2r^3f^2-rf^5
\tag{6}
\]
is an actual polynomial in the original ring. It satisfies
\[
fq=r^5+g^3,\qquad \Delta q=5gr^4.
\]
There is an exact presentation
\[
R_g=C_g[r,q]/(r^5-fq+g^3).
\tag{7}
\]
For an explicit check of generation, in addition to
\(x=(r^2+f^3)/g\), the inverse expressions are
\[
y=-\frac{rq+3r^4f^2+3r^2f^5+f^8}{g^3}
\]
and
\[
z=\frac{q^2+f(5r^8+4g^3r^3)
+f^4(10r^6+2g^3r)+10r^4f^7+5r^2f^{10}+f^{13}}{g^5}.
\tag{8}
\]
All denominators in these inverse expressions are powers of \(g\).
The presentation embeds in \(\operatorname{Frac}(C)[r]\),
where its relation solves \(q=(r^5+g^3)/f\); this also verifies
that no extra relation has been imposed.

Since the relation is monic of degree five in \(r\), this ring
is free over \(C_g[q]\) with basis \(1,r,\ldots,r^4\).
The normal-form monomials \(r^i q^j\), \(0\le i<5\), have
distinct derivation degrees \(i+5j\), with leading coefficient
\(f^{-j}\) in the generic coordinate \(r\). Thus
\[
J_n C_g=f^{n-\lfloor n/5\rfloor}g^nC_g.
\tag{9}
\]
Equations (5) and (9) prove the global divisibility
\[
J_n\subseteq f^{n-\lfloor n/5\rfloor}g^{\lceil n/2\rceil}C.
\tag{10}
\]
Only invariant localizations are used: localization of an invariant
value of \(\Delta^n\) commutes with \(\Delta\), and clearing
an invariant denominator proves the converse localization identity.
Arbitrary base change of invariant rings is not assumed.

## 4. Global witnesses and residue classes modulo ten

Write \(n=10k+i\), with \(0\le i<10\). Define \(b_i\),
\(a_i\), \(d_i\) and \(\epsilon_i\) by the following table.
The sign records the leading coefficient in the generic coordinate
\(r\), using the project's sign convention.

| i | b_i | a_i | d_i | epsilon_i |
|---|---|---|---|---|
| 0 | \(1\) | 0 | 0 | 1 |
| 1 | \(r\) | 1 | 1 | 1 |
| 2 | \(x\) | 2 | 1 | 1 |
| 3 | \(rx\) | 3 | 2 | 1 |
| 4 | \(x^2\) | 4 | 2 | 1 |
| 5 | \(S\) | 4 | 3 | 1 |
| 6 | \(y\) | 5 | 3 | -1 |
| 7 | \(ry\) | 6 | 4 | -1 |
| 8 | \(xy\) | 7 | 4 | -1 |
| 9 | \(rxy\) | 8 | 5 | -1 |

Direct generic leading coefficients give
\[
\deg_\Delta(b_i z^k)=10k+i,
\qquad
\Delta^n(b_i z^k)
=\epsilon_i n!f^{8k+a_i}g^{5k+d_i}.
\tag{11}
\]
Indeed the leading coefficients of \(r,x,S,y,z\) are respectively
\(1,g^{-1},f^{-1}g^{-2},-f^{-1}g^{-3},f^{-2}g^{-5}\),
and \(\Delta=fg\partial_r\). Therefore
\[
H_n=\frac{\epsilon_i}{n!}b_i z^k
\quad\text{satisfies}\quad
\Delta^n H_n=f^{8k+a_i}g^{5k+d_i}.
\tag{12}
\]
The two exponents in (12) equal those in (10), proving (1) in
every degree. This supplies actual global witnesses at the
intersection \(f=g=0\), not merely a calculation on its complement.

For example,
\[
J_1=(fg),\quad J_2=(f^2g),\quad J_5=(f^4g^3),
\quad J_6=(f^5g^3),\quad J_{10}=(f^8g^5),
\qquad J_{n+10}=f^8g^5J_n.
\]
The relations \(ry=f^2-xS\) and
\(rxy=xf^2-x^2S\) explain the harmless triangular change
from Freudenburg's chosen basis to the table above.

## 5. Associated primes and the exact absence of a hidden obstruction

For every \(n\ge1\), put
\(a=n-\lfloor n/5\rfloor\) and \(b=\lceil n/2\rceil\).
The primary decomposition is
\[
J_n=(f^a)\cap(g^b)=(f^ag^b).
\]
Thus
\[
\operatorname{Ass}_C(C/J_n)=\{(f),(g)\}.
\tag{13}
\]
There is no embedded associated prime at \((f,g)\). This does
not follow from the two charts alone; the global witness (12) is
what excludes an additional origin-supported defect.

The same witnesses give a derivation-adapted free basis:
\[
\ker\Delta^{n+1}=\bigoplus_{j=0}^{n}C H_j,
\qquad R=\bigoplus_{j\ge0}C H_j.
\tag{14}
\]
For generation, the top value of any element of derivation degree
\(n\) is a multiple of \(\Delta^nH_n\). Subtract that
multiple of \(H_n\) and induct. Distinct derivation degrees
give independence. This is a reconstruction of the known adapted
basis for this example, not a rank-three generalization.

## 6. Consequence for all invariant coefficient pairs

Let \(A,B\in C\) and \(E=A\Delta+B\partial_t\). The
whole-component exclusion and higher-image reduction proved in
[whole-plinth-component-pass16.md](whole-plinth-component-pass16.md),
combined with (1), give
\[
\boxed{E\text{ has a slice}
\iff (Afg,B)C=C
\iff (A,B)C=C\ \text{and}\ B=c+fgQ,
\quad c\in\mathbb C^*,\ Q\in C.}
\tag{15}
\]
The units of \(C/(fg)\) explain the last equivalence. Restrict
a unit to each axis. Both restrictions are nonzero constants in
one-variable polynomial rings, and their values at the origin
are equal. Hence their common residue is a scalar \(c\ne0\),
and the difference \(B-c\) lies in
\((f)\cap(g)=(fg)\). The converse is immediate.

The condition \((A,B)C=C\) must not be replaced by
\(\gcd(A,B)=1\). For instance \(A=f-1\), \(B=1+fg\)
have no common factor and have the desired scalar residue, but
both vanish at \((f,g)=(1,-1)\). They do not satisfy (15).

Every positive case in (15) is polynomially conjugate to a
translation by the exact matrix lift in
[extension-mixing-pass15.md, Section 6](extension-mixing-pass15.md).
For explicit normalization set
\[
p=fg,\quad a=A/c,\quad b=B/c=1+p\eta,
\quad \eta=Q/c.
\]
Choose \(U,V\in C\) with
\(aU+bV=1\), and put
\[
L=-\eta U,\quad M=aU+V,\quad
W=\eta r-at,
\qquad bM+paL=1.
\]
The finite independent-time flow gives a polynomial automorphism
\[
\Phi(v)=\exp(T\Delta)(v)|_{T=W}\ (v\in R),
\qquad \Phi(t)=Lr+Mt.
\]
Its inverse is the pass15 formula with
\(W'=((M-1)/p)r+at\), which is polynomial because
\(M\equiv1\pmod p\). It satisfies
\[
\Phi^{-1}E\Phi=c\partial_t,
\qquad s=(Lr+Mt)/c,
\qquad \ker E=\Phi(R)\cong\mathbb C^{[3]}.
\tag{16}
\]
No claim that \(W\Delta\) is locally nilpotent is involved.
The inverse finite-flow identities, not a variable-time exponential
assertion, provide the automorphism certificate.

When \(A=0\), the criterion reduces to \(B\) a nonzero
constant. When \(B=0\), no slice exists because \(\Delta\)
has proper plinth ideal. The zero derivation has no slice.
This invariant-pair conclusion extends the multiplier in front of
the fixed rank-three base; it does not reclassify arbitrary
noninvariant coefficients or arbitrary rank-three base derivations.

## 7. Verification scope

The independent script `rank_three_image_checks_pass17.py` checks
the displayed chart identities, signs, witnesses, residue-class
formula and invariant-pair boundary controls. It imports no
research module. Finite tests verify formulas, not the all-degree
conclusion; Sections 2-4 prove that conclusion algebraically.

The command
`/opt/anaconda3/bin/python research/rank_three_image_checks_pass17.py`
passed all eight test methods in 0.466 seconds. The witness check
covers degrees zero through 29; the all-degree proof does not infer
its conclusion from this finite range.

This note identifies no new counterexample to affine replacement
or to the Freeness Conjecture. The canonical rank-three example
already has the required freeness property in every degree.
