# Intrinsic rank one and the geometric generic-fiber obstruction

The full hypothesis
\[
A[s]\simeq\mathbb C^{[4]}
\tag{1}
\]
still does not yield a proved exclusion of intrinsic generic LND rank
one in this investigation. A specific proposed route does have a
complete outcome: slicing the invariant plane and applying the
factorial-surface theorem requires **geometric** factoriality, which
is not forced by (1), even after allowing every coordinate of that
plane. An exact class-group formula measures the failure.

This is a bounded proof and gap report. It does not prove
\(\operatorname{ML}(A)=\mathbb C\), rank at least two, cancellation,
or any claim of novelty. The divisor calculation uses standard
local-slice and divisor-localization mechanisms.

## 1. What intrinsic rank one would mean

The generic LND rank is
\[
\rho(A)=\dim_{\operatorname{Frac}A}
 \operatorname{span}_{\operatorname{Frac}A}\operatorname{LND}(A).
\]
Under (1), earlier proofs give a nonzero intrinsic LND, smoothness,
factoriality, constant units, and, for every nonzero LND \(D\),
\[
C=\ker D\simeq\mathbb C^{[2]},\qquad
A\text{ faithfully flat over }C.
\tag{2}
\]
For a primitive \(D\), the full plinth is \(pC\), with a minimal
local slice \(r\) satisfying
\[
Dr=p,\qquad A_p=C_p[r].
\tag{3}
\]
These are the established [intrinsic quotient and plinth conclusions](intrinsic-plinth-boundary-pass27.md),
not additional assumptions that \(A\) is polynomial.

If \(\rho(A)=1\), all nonzero intrinsic LNDs have the same kernel:
they are rational multiples of any one of them. Primitive UFD
saturation then gives
\[
\operatorname{LND}(A)=CD,\qquad \operatorname{ML}(A)=C.
\tag{4}
\]
This is the standard semi-rigid situation. Alhajjar's Propositions
3.2–3.3 give the same-kernel and unique-primitive formulation under
the stated ACC/HCF hypotheses, satisfied here.[^semi]

The [already-proved fence construction](fence-centralizer-sector-pass26.md)
shows that \(p\in\mathbb C[a]\) for a coordinate \(a\) of \(C\)
produces a second independent commuting LND by clearing denominators
of \(\partial_b\) on \(C_p[r]\). A unit \(p\) supplies a slice
and already closes cancellation. Consequently a rank-one candidate
must have nonunit, non-fence full plinth. This restriction is inherited
from pass 26, not presented as a new exclusion.

## 2. An exact geometric generic-surface class group

The calculation below applies to any smooth affine complex UFD of
dimension three with a primitive LND satisfying (2)–(3). Fix an
arbitrary coordinate pair \(C=\mathbb C[a,b]\). Write
\[
p=c\prod_i f_i^{n_i},\qquad c\in\mathbb C^*,
\]
where the \(f_i\) are pairwise nonassociate prime elements of \(C\).
Let \(I_a\) be the indices for which \(a\) is nonconstant on
\(\Gamma_i=V(f_i)\). Precisely these factors are nonunits in
\(\mathbb C(a)[b]\). Put
\[
K=\mathbb C(a),\quad \overline K=\overline{\mathbb C(a)},\quad
R_a=A\otimes_{\mathbb C[a]}\overline K,
\]
\[
F_i=\operatorname{Frac}(C/f_iC),\quad
E_i=\operatorname{Frac}\ker(\overline D:A/f_iA\to A/f_iA),
\]
\[
d_i=[F_i:K]=\deg_b f_i,\qquad e_i=[E_i:F_i].
\tag{5}
\]
The degree in (5) is taken after viewing \(f_i\) over \(K\);
vertical factors are omitted. The inherited primitive boundary
criterion gives \(e_i>1\) for every plinth factor.[^boundary]

**Proposition.** The geometric generic surface is a regular integral
affine surface, and
\[
\operatorname{Cl}(R_a)
\simeq\bigoplus_{i\in I_a}\mathbb Z^{\,d_i(e_i-1)}.
\tag{6}
\]
The isomorphism is not asserted to be canonical. Plinth exponents
\(n_i\) do not enter this group: the relevant individual prime
fibers become reduced after the indicated generic base change.

### 2.1 Regularity, integrality, and the exceptional fibers

The ordinary generic surface \(A_K=A\otimes_{\mathbb C[a]}K\)
is a localization of the regular UFD \(A\). It is regular and a
UFD. Since \(K\) is perfect, it is geometrically regular; thus
\(R_a\) is regular.[^regular]

The inclusion \(A_K\hookrightarrow (A_K)_p\) remains injective
after the flat field extension \(K\subset\overline K\). Equation
(3) gives
\[
(R_a)_p=\overline K[b,p^{-1},r],
\tag{7}
\]
which is a domain. Therefore \(R_a\) itself is a domain. This
also rules out extra components supported entirely in \(p=0\).

Factorial closure makes each \(f_i\) prime in \(A\), and
primitivity makes the induced \(\overline D\) nonzero on
\(A/f_iA\). For \(i\in I_a\), localize this ring at
\(\mathbb C[a]\setminus\{0\}\). The result \(T_i\) is a
one-dimensional affine \(K\)-domain with a nonzero LND.
Its invariant ring is algebraic over \(K\), hence is a field:
the minimal polynomial of any nonzero algebraic element supplies
its inverse. Localization of kernels identifies this field with
\(E_i\). It is a finite extension of \(K\), of degree \(d_ie_i\).
The local-slice theorem now has an invertible derivative and gives
\[
T_i=E_i[t_i].
\tag{8}
\]

All these finite extensions are separable, since the characteristic
is zero. Therefore base change to \(\overline K\) splits (8) into
\(d_ie_i\) disjoint reduced affine lines. The polynomial \(f_i\)
has \(d_i\) distinct roots \(\alpha\) over \(\overline K\),
one for each embedding of \(F_i\). Each embedding has exactly
\(e_i\) extensions to \(E_i\). Accordingly
\[
R_a/(b-\alpha)R_a\simeq\prod_{j=1}^{e_i}\overline K[t_{ij}].
\tag{9}
\]
Distinct horizontal prime factors have disjoint root sets, since
they remain coprime over \(K[b]\). Vertical factors become units.
Thus (9) lists every prime divisor removed in (7), with multiplicity
one in the divisor of \(b-\alpha\).

### 2.2 Generators and all integral relations

The localized ring in (7) is a UFD. Restricting Weil divisors to it
shows that \(\operatorname{Cl}(R_a)\) is generated by the boundary
lines \(D_{\alpha,j}\) from (9). This is the ordinary divisor
localization argument, reconstructed from the principal-divisor
presentation.[^divisors]

There are no hidden relations. If a divisor supported on these
lines is principal, its defining rational function has zero divisor
on (7), so is a unit of that polynomial localization. All such units
are exactly
\[
\overline K^*\prod_\alpha(b-\alpha)^{\mathbb Z}.
\tag{10}
\]
Consequently the complete relation list is
\[
\operatorname{div}(b-\alpha)
=D_{\alpha,1}+\cdots+D_{\alpha,e_i}.
\tag{11}
\]
Each relation has coefficient one and uses its own disjoint block
of generators. The resulting quotient is free of rank \(e_i-1\)
per root. Summing over the \(d_i\) roots proves (6), including
the absence of torsion. This is an all-degree argument, not a
bounded equation search.

## 3. The exact generic-factoriality gate

Since every \(e_i>1\), equation (6) gives
\[
R_a\text{ is factorial}
\quad\Longleftrightarrow\quad I_a=\varnothing
\quad\Longleftrightarrow\quad p\in\mathbb C[a].
\tag{12}
\]
The last equivalence follows because a prime polynomial whose
curve has constant \(a\) must be associated with \(a-\lambda\).
Conversely, if \(p\in\mathbb C[a]\), it is a unit over \(K\),
and (3) gives \(A_K=K[b,r]\) directly.

Thus selecting a geometrically factorial generic surface by changing
coordinates **inside this invariant plane** does not bypass the
non-fence case. Its existence is exactly the fence condition already
handled by the commuting-direction construction.

The word geometrically cannot be dropped. Every ordinary generic
surface \(A_K\) above is already a UFD by localization. A theorem
for factorial surfaces over an algebraically closed field cannot be
applied over \(K=\mathbb C(a)\) without the extra hypothesis.
Sai Krishna's Corollary 2.10 explicitly retains geometric factoriality
over an arbitrary field; Theorem 2.9 has an algebraically closed
base field.[^surfaces]

## 4. An actual polynomial-cylinder countercontrol, for every plane coordinate

Use the classical rank-three local-slice action on the already
polynomial ring \(A_0=\mathbb C[x,y,z]\):
\[
f=xz-y^2,\qquad r=x^3+yf,
\]
\[
h=zf^2+2x^2yf+x^5,\qquad
D=\operatorname{Jac}(f,h,\cdot).
\tag{13}
\]
The known exact input is
\[
\ker D=\mathbb C[f,h],\qquad
Dr=-fh,\qquad \operatorname{pl}(D)=fh\mathbb C[f,h].
\tag{14}
\]
Changing the sign of a plinth generator is immaterial. These are
the inherited Freudenburg example and full degree-module calculation,
not a newly constructed rank-three action.[^canonical]

For completeness, the boundary fields can be seen without a
numerical fiber count. Modulo \(f\), the function field is
\(\mathbb C(x,y)\), \(h=x^5\), \(Dx=0\), and
\(Dy=5x^5\). Hence its invariant field is \(\mathbb C(x)\),
of degree five over \(\mathbb C(h)\). Modulo \(h\), use
\[
xh=r^2+f^3,\quad y=(r-x^3)/f,\quad z=(f+y^2)/x.
\]
The function field is \(\mathbb C(f,r)(x)\), with
\(r^2=-f^3\) and \(Dx=-2fr\ne0\). Its invariant field is
\(\mathbb C(f,r)\), of degree two over \(\mathbb C(f)\).
Thus
\[
e_f=5,\qquad e_h=2.
\tag{15}
\]

For every coordinate \(a\) of \(\mathbb C[f,h]\), at least one
of \(V(f)\), \(V(h)\) is horizontal over \(a\). Indeed, if both
were vertical, their intersection would force their constant
\(a\)-values to be equal, say \(c\). Then \(fh\mid a-c\),
contradicting primality of the coordinate polynomial \(a-c\).
Equations (6) and (15) therefore prove
\[
\operatorname{Cl}\!\left(A_0\otimes_{\mathbb C[a]}
                 \overline{\mathbb C(a)}\right)\ne0
\quad\text{for every coordinate }a\text{ of }\mathbb C[f,h].
\tag{16}
\]

There is also an unbounded exact family of class groups in this
single fixed polynomial example. For \(a=f+h^N\), \(N\ge1\),
the pair \((a,h)\) is a coordinate pair of the invariant plane.
The two horizontal degrees are \(d_f=N\), \(d_h=1\). Hence
\[
\operatorname{Cl}\!\left(A_0\otimes_{\mathbb C[f+h^N]}
            \overline{\mathbb C(f+h^N)}\right)
\simeq\mathbb Z^{4N+1}.
\tag{17}
\]
In particular \(a=f+h\) gives \(\mathbb Z^5\).

This is a countercontrol with the **full** polynomial-cylinder
hypothesis: \(A_0[s]=\mathbb C^{[4]}\) by an explicit identity.
It disproves automatic existence of a favorable coordinate in a
specified intrinsic invariant plane, including all nonlinear
coordinate changes of that plane. It is not a rank-one example:
the full intrinsic LND rank of \(A_0\) is three. Thus it does not
disprove the still-open claim that a genuine rank-one candidate
under (1) is impossible.

## 5. Exact remaining quantifier and source boundary

Rank one would make the invariant plane unique by (4), and the
existing fence argument would make its plinth non-fence. Formula
(6) then forces nonzero geometric generic class groups for every
coordinate of that plane. The missing step is not another
factorial-surface theorem: one would have to use **uniqueness of
the entire intrinsic LND direction**, together with (1), to exclude
this non-fence situation or construct an action moving the plane.
The polynomial example (13) shows why (1) alone, applied to one
chosen LND, cannot do that through generic factoriality.

Contractibility does not remove the rank-one issue by itself.
Petitjean's primary paper describes smooth contractible Koras–Russell
threefolds of the second kind with invariant ring \(\mathbb C[x,z]\)
and every LND an invariant replica of one primitive derivation.[^second]
No assertion that their cylinders are polynomial is made here.
They are a distinct rank-one warning, not the familiar first-kind
rank-two example and not a counterexample to (1).

No new independent intrinsic LND, universal rank bound, or termination
procedure has been obtained. The proof above closes a precisely
specified generic-factoriality inference and supplies an exact
all-degree class-group formula. The literature use is confined to
the hypotheses stated below; absent search matches supply no
priority evidence.

## 6. Independent finite controls

The standalone [exact checker](intrinsic_rank_checks_pass34.py) imports
only `unittest` and SymPy. Its five methods reconstruct the canonical
Jacobian and local-slice identities, both rational boundary charts,
the integral block-relation bases, and finite members of the nonlinear
coordinate family. The first run passed all five methods in 0.095 s:

```sh
/opt/anaconda3/bin/python research/intrinsic_rank_checks_pass34.py
```

These controls do not prove the geometric class-group theorem or the
quantifier over all coordinates. Those claims rest on the written
divisor proof, which received two independent full-file algebraic
audits. No expert or Lean verification is claimed.

## Primary inputs

[^semi]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Propositions 3.2–3.3 and their full proofs, PDF pp. 6–7, directly read. The hypotheses are finite characteristic-zero transcendence degree for the setting, ACC on principal ideals, and an HCF invariant ring for uniqueness. These mechanisms are inherited, not a cylinder invariance theorem.

[^boundary]: The exact intrinsic support proof is in [pass 27](intrinsic-plinth-boundary-pass27.md). Direct primary comparison: Kayo Masuda, [*Faithfully flat quotient morphisms by Ga-actions on factorial affine varieties*](https://arxiv.org/pdf/2512.06687), Remark after Proposition 2.5, p. 5; Section 3 hypotheses and Lemma 3.1(2)–(3), pp. 6–8; Theorem 3.5 proof and following Remark (1), pp. 11–12. Those passages were directly read. They treat factorial affine domains, primitive LNDs, affine kernels and faithful flatness; the theorem proof explicitly gives the strict boundary invariant-field degree. Pass 27 supplies the elementary minimal-local-slice proof without normality of \(A/f_iA\).

[^regular]: [Stacks Project, Lemma 33.12.2, Tag 038U](https://stacks.math.columbia.edu/tag/038U), statement and proof directly read. The criterion tests finite purely inseparable extensions; over the perfect field \(\mathbb C(a)\), regularity therefore implies geometric regularity.

[^divisors]: [Stacks Project, Section 31.27, Tag 0BE0](https://stacks.math.columbia.edu/tag/0BE0), Definitions 31.27.2–31.27.7 and the principal-divisor exact complex, directly read. The generator-and-relation calculation above reconstructs the usual divisor-localization argument in this normal affine setting; it is not quoted as a new class-group theorem.

[^surfaces]: Sai Krishna, [*An algebraic characterization of the affine three space in arbitrary characteristic*](https://arxiv.org/pdf/2308.05424), Theorem 2.9, Corollary 2.10 and Remark 2.11, PDF p. 5, directly read. These are recalled source statements, not new proofs in that paper. Only their exact distinction between algebraically closed and arbitrary coefficient fields is used; none recognizes all stably polynomial threefolds.

[^canonical]: Gene Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), Section 4.1, and [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Sections 8.2.1–8.2.2, especially the kernel, images and degree modules. These primary passages were read. The latter gives the full first degree module \(\ker D^2=C+Cr\), hence the full plinth in (14).

[^second]: Charlie Petitjean, [*Automorphism groups of Koras–Russell threefolds of the second kind*](https://arxiv.org/pdf/1507.06087), Introduction and Section 2, PDF pp. 1–4, directly read. The family is \(x+y(x^d+z^{\alpha_2})^\ell+t^{\alpha_3}=0\), with \(d\ge2\), \(\ell\ge1\), \(2\le\alpha_2\le\alpha_3\), and the two stated coprimality conditions. Only its smooth contractibility and explicit rank-one action classification are used.
