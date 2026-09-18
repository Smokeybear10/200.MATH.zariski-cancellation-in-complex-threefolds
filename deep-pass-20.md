# Nonunit local-slice multipliers and cancellation boundaries

The coordinate construction extends beyond additive local-slice changes.
For the polynomial-curve bases below, every invariant slice extension
after multiplication by a power of the invariant \(f\) has a polynomial
three-variable kernel. An explicit coefficient condition also gives the
same conclusion for every nonzero multiplier \(a(f)\). The case
\(a=f-1,\ Q=h\) admits a complete coefficient classification.

These are restricted working theorems with written inverses. They do
not settle
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
The characteristic-zero problem is part of the established cancellation
literature; results in positive characteristic do not answer (1).[^1]
No general reduction of its arbitrary cancellation factor to the
families treated here is supplied. Novelty, proof-assistant verification,
and human expert review are not established.

## 1. Setup and scope of the coordinate theorem

A locally nilpotent derivation, or LND, is a derivation for which each
polynomial is killed by a sufficiently high iterate. A slice is a
polynomial \(\sigma\) with \(E\sigma=1\). In characteristic zero a
slice gives \(R[t]=(\ker E)[\sigma]\), but that equality alone does
not prove that \(\ker E\) is a polynomial ring.

Fix a monic \(F\in\mathbb C[Y]\) of degree \(d\ge2\), an integer
\(n\ge1\), and \(P\in\mathbb C[x,f]\) with \(P(x,0)\)
nonconstant. In \(R=\mathbb C[x,y,z]\), define
\[
\begin{split}
f&=xz-F(y),&
r&=xP(x,f)+yf^n,\\
G(T,S)&=S^dF(T/S),&
K_n(f,T)&=G(T,f^n)+f^{nd+1},\\
xh&=K_n(f,r).
\end{split}
\tag{2}
\]
The expression \(h\) is polynomial. The preceding
[base construction](research/polynomial-curve-lift-pass18.md)
establishes the primitive LND \(D_1=-\operatorname{Jac}(f,h,\cdot)\),
its kernel \(\mathbb C[f,h]\), and \(D_1r=f^nh\).

For \(0\ne a(f)\in\mathbb C[f]\) and \(Q\in\mathbb C[f,h]\), put
\[
\begin{split}
R_*&=ar+hQ,\\
\Phi_a(f,T)&=G(T,af^n)+a^df^{nd+1},\\
k&=\Phi_a(f,R_*)/h
 =a^dx+Q\,\Delta_G(R_*,ar;af^n),\\
D&=\operatorname{Jac}(f,k,\cdot),\qquad DR_*=af^nk.
\end{split}
\tag{3}
\]
Here \(\Delta_G(U,V;S)=(G(U,S)-G(V,S))/(U-V)\) is a
polynomial divided difference. The construction and fixed-frame
local-slice replacement principle are Freudenburg's established
machinery, also recalled by Dasgupta and Gaifullin.[^2]

The proved scope is as follows. “Invariant extension” means
\(E=AD+B\partial_t\), with the indicated coefficient ring.

| Multiplier and parameter | Coefficients covered | Conclusion |
| --- | --- | --- |
| \(a=f^e,\ e\ge1\), arbitrary \(Q\) | Every \(A,B\in\ker D\) for which \(E\) has a slice | \(\ker E\simeq\mathbb C^{[3]}\), with polynomial coordinates and inverse |
| Arbitrary \(a\ne0\), arbitrary \(Q\) | \(A,B\in\mathbb C[f,k]\), \((A,B)=1\), \(B=1+q_a(f)kJ\), where \(q_a\) is the squarefree product of factors of \(af\) | Same constructive conclusion; sufficient conditions only |
| \(a=f-1,\ Q=h\) | Every invariant slice extension | Same conclusion; exact coefficient criterion below |
| Arbitrary \(a,Q\), every possible invariant coefficient | Not classified | No assertion |

The [complete coordinate proof](research/nonunit-local-slice-pass20.md)
includes independent-variable inverse formulas. Its coefficient
necessity statements use the earlier
[source-dependent affine-replacement argument](research/general-invariant-affine-pass17.md).
The constructive sufficient statements do not require that necessity
argument.

In a fixed invariant frame the derivative requirement itself excludes
an unqualified multiplier \(a(f,h)\): if
\(D_1(ar+b)=h\,q(f)\ne0\), then \(af^n=q(f)\), so
\(a\in\mathbb C[f]\setminus\{0\}\).
Changing invariant generators is a separate operation not classified here.

## 2. Exact plinth calculation and an essential exception

The plinth ideal is \(D(R)\cap\ker D\). Its full multiplicity
matters when deciding whether a displayed local slice is minimal.

First take \(a=f^e\) and \(q(H)=Q(0,H)\ne0\). Write
\[
N=n+e,\quad H_0=x^{d-1}P(x,0)^d,\quad
\kappa(H)=H^{d-1}q(H)^d,\quad \tau(H)=Hq(H).
\tag{4}
\]
Modulo \(f\), the new invariants satisfy
\(k=\kappa(H_0)\) and \(R_*=\tau(H_0)\).
After inverting \(f\), the surface chart is
\[
R_f=
\mathbb C[f^{\pm1},h,k,R_*]/(hk-K_N(f,R_*)).
\tag{5}
\]
The monic chart and the nonconstant residue of \(k\) give
\(\ker D=\mathbb C[f,k]\). The exact derivative
\(DR_*=f^Nk\) limits any common coefficient factor to \(f\) or
\(k\). A degree-\((d-1)\) derivative of the monic relation excludes
\(k\), and \(Dy\bmod f=x\,d\kappa(H_0(x))/dx\ne0\) excludes
\(f\). Thus \(D\) is primitive.

Except when \(d=2\) and \(q\) is constant,
\(\deg\kappa>\deg\tau\). Hence \(1,\tau(H)\) are linearly
independent over \(\mathbb C(\kappa(H))\). Applying this to the
degree-one chart rules out canceled coefficient poles and gives
\[
\ker D^2=\mathbb C[f,k]\oplus\mathbb C[f,k]R_*,
\qquad \operatorname{plinth}(D)=(f^{n+e}k).
\tag{6}
\]

For \(d=2,\ q=c\ne0\), the true answer is smaller:
\[
\operatorname{plinth}(D)=(f^nk).
\tag{7}
\]
Indeed, writing \(F(Y)=Y^2+\ell Y+c_0\), one has
\(k=a^2x+2arQ+hQ^2+\ell af^nQ\).
A finite inverse to \(h\mapsto hQ^2\) modulo \(f^e\) supplies
\(\psi(f,k)\) such that \(u=(R_*-\psi)/a\) is polynomial
and \(Du=f^nk\). Its residue is \(-r_0+w(H_0)\);
the same degree test proves minimality. If \(Q=c\) is actually
constant, \(k/c^2\) is exactly the old base invariant after
\(P\mapsto P+a/c\). This is a direct control, not a numerical guess.

If \(Q\) has a common power of \(f\) with \(a\), let
\(s=\min(e,\operatorname{ord}_f Q)\), taking \(s=e\) for \(Q=0\).
Then \(R_*=f^sR'\), \(k=f^{ds}k'\), and \(D=f^{ds}D'\).
The reduced construction is either the preceding primitive case or
the additive construction. Its invariant factor is absorbed into \(A\).
This proves the all-\(Q\) assertion without claiming that every
unnormalized Jacobian is primitive.

Both primitive branches have reduced plinth support \(V(fk)\).
The slice-coefficient criterion is
\[
(A,B)=1,\qquad B=c+fkJ,\qquad c\in\mathbb C^*.
\tag{8}
\]
The construction below normalizes \(c=1\).

## 3. A sharp obstruction to the unchanged inverse

The old reverse formula really fails for nonunit multipliers. Take
\(a=f^e\), \(q\ne0\), and
\[
B=1+f^\ell kJ,\quad \ell\ge1,\quad J(0,K)\ne0.
\]
For \(E=D+B\partial_t\), the geometric series for \(B^{-1}\)
modulo \(f^Nk\) gives a polynomial slice. Thus the following
failure occurs in an actual slice extension.

Set
\[
\rho=BR_*-f^Nkt,\quad \widehat h=K_N(f,\rho)/k,\quad
\widehat r_{\rm old}
 =\frac{\rho-\widehat hQ(f,\widehat h)}{f^e}.
\tag{9}
\]
The [exact obstruction proof](research/nonunit-inverse-obstruction-pass20.md)
gives
\[
\widehat r_{\rm old}\in R[t]\ \Longleftrightarrow\ \ell\ge e;
\qquad
v_f(\widehat r_{\rm old})=\ell-e\quad(\ell<e).
\tag{10}
\]
For \(\ell<e\), its numerator's leading coefficient is
\[
k_0J(0,k_0)H_0\bigl((1-d)q(H_0)-dH_0q'(H_0)\bigr).
\tag{11}
\]
It is nonzero: substitution by a nonconstant polynomial is injective,
and the operator \((1-d)-dH\,d/dH\) has nonzero eigenvalue
\(1-d-dj\) on every \(H^j\). For \(\ell\ge e\), the
polynomial divided-difference formula gives the required divisibility.

This is a theorem about one unchanged formula. It is not a
nonpolynomial-kernel theorem and is not a cancellation counterexample.

## 4. Two finite corrections and the global inverse

Under (8), choose \(U,V\in\mathbb C[f,k]\) satisfying
\(Af^NkU+BV=1\). The matrix
\[
\rho=BR_*-Af^Nkt,\qquad \sigma=UR_*+Vt
\tag{12}
\]
has polynomial inverse
\(R_*=V\rho+Af^Nk\sigma,\ t=-U\rho+B\sigma\).
Moreover \(E\rho=0\) and \(E\sigma=1\).

The first repair changes \(Q\), not \(P\). Over
\(\mathbb C[f]/(f^{e+1})\), use the curve
\((h,k,R_*)=(H,H^{d-1}Q^d,HQ)\). Put
\[
b(f,H)=B(f,H^{d-1}Q^d),\quad \beta(H)=Hb^d,\quad
\widetilde Q(f,Z)=
(b^{1-d}Q)(f,\beta^{-1}(Z)).
\tag{13}
\]
All inverses here are finite polynomials in a nilpotent coefficient
ring, because \(b\equiv1\pmod f\). The order \(e+1\), not
merely \(e\), retains the normal displacement \(ar\):
\[
\rho-\widehat h\widetilde Q(f,\widehat h)
 \equiv ar\pmod{f^{e+1}}.
\tag{14}
\]
Define
\[
\widehat r=
 \frac{\rho-\widehat h\widetilde Q(f,\widehat h)}a,\qquad
\widehat x=
 \frac{k-\widetilde Q(f,\widehat h)
       \Delta_G(\rho,a\widehat r;af^n)}{a^d}.
\tag{15}
\]
The first is polynomial by (14). Multiplying the second numerator
by \(\widehat h\) gives \(a^dK_n(f,\widehat r)\).
The element \(f\) is prime in the abstract surface cylinder and
does not divide \(\widehat h\), so repeated prime cancellation
clears the full denominator \(a^d\). No unique-factorization
hypothesis on that surface is used.

The inverse is constructed on an independent copy of
\(XH=K_n(f,T)\). First set
\(\rho=aT+H\widetilde Q\) and
\(k=a^dX+\widetilde Q\Delta_G(\rho,aT;af^n)\), then use
the inverse matrix (12). The inverse curve identity from (13)
clears the first denominator, and the same prime argument clears
the second. The compositions are inverse on localization and,
since the rings are domains, globally.

The second repair changes \(P\). Modulo \(f^n\), the surface map
and its inverse are independent of the cylinder coordinate,
preserve the vertex ideal \((x,h,r)\) of \(xh=r^d\), and are
the identity modulo \(f\). On the universal original curve
\[
(x,h,r)=(u,u^{d-1}P(u,f)^d,uP(u,f)),
\]
write \(\widehat x=uU_0,\ \widehat r=uW_0\).
The finite inverse to \(u\mapsto uU_0\) produces
\(\widetilde P=(W_0/U_0)\circ(uU_0)^{-1}\).
Both curve identities are established before substituting into any
ring with nilpotents.

Consequently
\(Y=(\widehat r-\widehat x\widetilde P(\widehat x,f))/f^n\)
is polynomial. The Taylor expansion of \(F\) supplies a polynomial
\(Z\) satisfying \(f=\widehat xZ-F(Y)\).
The inverse curve identity clears the original denominators in an
independent polynomial ring as well. Thus
\[
R[t]=\mathbb C[\widehat x,Y,Z,\sigma],\qquad
E=\partial_\sigma,\qquad
\ker E=\mathbb C[\widehat x,Y,Z].
\tag{16}
\]
This is the missing global inverse assertion that formal agreement
alone would not provide.

For a concrete negative-and-positive control, take
\(F=Y^2,\ P=x^2,\ n=e=2,\ Q=h,\ B=1+fk\).
The unchanged numerator is \(-3fh^5\bmod f^2\).
The two corrections are
\[
\widetilde Q=h-3fh^4+24f^2h^7\bmod f^3,\qquad
\widetilde P=X^2+f(31X^{17}+1265X^{54})\bmod f^2.
\tag{17}
\]
The exact checker tests the displayed coefficients and independently
re-evaluates the inverse, rather than substituting a forward result
back into the same helper.

## 5. Distinct divisors and the coefficient boundary

For arbitrary \(a=c\prod_g g^{v_g}\), where \(g=f-\lambda\),
impose \(B=1+q_a kJ\) as in the table. Construct the \(Q\)-jet
modulo each \(g^{v_g}\); at \(f=0\), use one extra order if
\(f\mid a\), and otherwise impose \(\widetilde Q=Q\bmod f\).
Coefficientwise Chinese remaindering yields one polynomial
\(\widetilde Q\).

Each \(g\) is prime in
\(\mathbb C[f,x,h,r]/(xh-K_n(f,r))\):
its quotient is defined by \(xh-K_n(\lambda,r)\), with a
nonzero monic right-hand polynomial. Also \(\widehat h=h\bmod g\).
The first divisions are cleared by the curve congruences and the
second divisions prime by prime. Compositions are checked after
inverting \(af\). The old \(P\)-jet argument then applies at
\(f=0\), where \(a/f^{\operatorname{ord}_f a}\) is a unit.

The condition on \(B\) cannot be called necessary for all \(a,Q\).
The quadratic constant-\(Q\) control above has plinth \(f^nk\)
even when \(a\) vanishes elsewhere. Those additional roots do not
automatically constrain an actual slice coefficient.

For \(a=f-1,\ Q=h\), by contrast, the residue-degree tests at
both \(f=0\) and \(f=1\) give
\[
\ker D=\mathbb C[f,k],\qquad
\operatorname{plinth}(D)=((f-1)f^nk).
\tag{18}
\]
The primitive rank is three. The three plinth lines have connected
union, so their invertible polynomial residues share one constant.
The exact slice criterion is
\((A,B)=1,\ B=c+f(f-1)kJ,\ c\ne0\).
Here the first correction can be \(\widetilde Q=Q\); only the
old \(P\)-curve needs adjustment. The
[independent CRT audit](research/crt-audit-pass20.md) covers this
case and the general sufficient statement separately.

## 6. Prior work and the precise remaining calculation

The surface-cylinder matrix is an exact specialization of
Blanc, Poloni and Van Santen's Lemma 3.1, followed by adjoining
fractions for a transported ideal. It is not a new cylinder
isomorphism principle.[^3] Moser-Jauslin and Poloni provide related
explicit finite-congruence and slice constructions for special
Danielewski surfaces. Their stated simple-root hypotheses do not
directly cover the degenerate fiber \(kh=R_*^d\).[^4]
The [literal comparison](research/cylinder-comparison-pass20.md)
records the substitutions and both published inverse maps.

The physical polynomial ring has two weighted fractions. In
\(\mathscr A_0=\mathbb C[f,x,h,r]/(xh-K_n(f,r))\), set
\[
a_P=r-xP,\quad
b_P=h-P\Delta_G(r,r-xP;f^n),\quad
\mathscr R_P=\mathscr A_0[a_P/f^n,b_P/f^{nd}].
\tag{19}
\]
Then \(\mathscr R_P\simeq R\). Adjoining only the first
fraction leaves a reducible fiber \(xH=0\) at \(f=0\), so
that shortcut does not give the physical ring.

The extension through both fractions is itself a consequence of
the established universal property of affine modifications.[^5]
The [two-stage reduction](research/priority-boundary-pass20.md)
first uses the transported curve ideal
\(J_P=(f^n,a_P,b_P)\). Writing \(q=n(d-1)\), its intermediate
ring is
\[
\mathscr B_P=\mathscr A_0[J_P/f^n]
 \simeq\mathbb C[f,x,y,H]/(xH-f^q(F(y)+f)).
\tag{20}
\]
The second ideal is
\((f^q,H)=(f^q):x^\infty\).
A map sending \(x\) to \(x\bmod f\) preserves this saturation:
modulo \(f^q\), those two elements define the same principal open
set because their difference is nilpotent. A second application
of the same universal property completes the lift.

Therefore neither the cylinder matrix nor the modification-lifting
principle should be presented as a new theorem. The calculation
requiring verification here is transport of the two nonreduced curve
centers, including the extra normal-displacement order in (14).
Whether the resulting uniform family statement already occurs as a
published consequence remains unestablished.

A different direct specialization is impossible: as a
\(\mathbb C[f]\)-algebra, the physical \(R\) cannot have a
presentation \(f^Nv=L(f,u,w)\), \(N\ge1\).
Its zero fiber would be a curve times a line. If \(F\) has repeated
roots, the actual fiber \(xz=F(y)\) has a nonempty finite singular
set, unlike that product. If \(F\) is squarefree, its compact-support
Euler characteristic is \(d\ge2\), while a smooth connected affine
curve times a line has Euler characteristic at most one. This
excludes that exact presentation, not all alternative uses of
published constructions.

## 7. An actual nodal surface passes the previous local tests

A separate geometric construction shows why the remaining ambient
problem cannot be replaced by local singularity or Euler tests.
The earlier conditional quotient argument, using Kaliman's
topological results, required three disjoint contractible components
above a node with four normalization branches.[^6]

Fix \(a_0^4=3\), with distinguished values
\(w_1=a_0,w_2=-a_0,w_3=ia_0,w_4=-ia_0\). Put
\[
d_0=w^4-3,\quad A_0(w)=(w-w_1)(w-w_3),\quad
\mathcal B=\mathbb C[w,y,z]/(A_0(w)z-y(y-1)).
\tag{21}
\]
This is a smooth integral surface. The divisor \(d_0=0\) has six
disjoint affine lines, two at each split value \(w_1,w_3\) and
one at each of \(w_2,w_4\). Pair them as follows:
\((w_1,0)\) with \((w_3,0)\);
\((w_1,1)\) with \(w_4\);
and \(w_2\) with \((w_3,1)\).

On a split line use \(\tau=z/(2y-1)\); on an ordinary line use
\(\tau=y/A_0(w_j)\). Identify paired lines by \(t=\tau/w_j\).
The affine pinch is
\[
\mathcal R=\mathcal B
 \times_{\mathcal B/d_0\mathcal B}\mathbb C[t]^3,
\tag{22}
\]
where each factor is embedded diagonally on its pair.
The established affine pinching theorem supplies finite generation
and a finite normalization map.[^7] Directly, the normalization is
\(\mathcal B\) and the conductor is exactly \(d_0\mathcal B\).

The surface \(E=\operatorname{Spec}\mathcal R\) is integral.
Along its three disjoint singular lines its completed local ring is
\(\mathbb C[[\xi,\zeta,t]]/(\xi\zeta)\), so it is locally a
complete intersection and Gorenstein. Global integrality is
compatible with two branches after completion.

The actual LND
\[
\partial=w\delta,\qquad
\delta w=0,\quad \delta y=A_0(w),\quad\delta z=2y-1
\]
descends to \(\mathcal R\), because \(\partial t=1\) on
every paired line. Its invariant ring is
\[
T=\mathbb C+d_0\mathbb C[w].
\tag{23}
\]
The finite map
\(u=w^4-2,\ v=(w^4-3)w^2\)
lands on \(v^2-u^3+3u=2\), with normalized map \(w\mapsto w^2\).
It has one intermediate point over the node and four normalization
branches. Its node fiber in \(E\) is three reduced disjoint lines.

The actual closed/open cohomology connecting map is
\[
N=\begin{pmatrix}1&1&0\\0&0&1\\1&0&1\\0&1&0\end{pmatrix}.
\tag{24}
\]
Its maximal minors are \(1,-1,-1,1\). Consequently
\(H_c^3(E,\mathbb Z)=H_c^4(E,\mathbb Z)=\mathbb Z\), and the
other compact-support groups vanish. This matrix follows from
naturality under the finite normalization and its specified line
pairings, rather than from matching ranks alone.

The normalization form
\(\Omega=dw\wedge dy/(A_0(w)d_0)\)
has residues \(dt/(4w_j^2)\). Every pair has opposite residues.
The double-normal-crossing residue criterion therefore gives a
nowhere-vanishing dualizing section, so \(\omega_E\simeq\mathcal O_E\).[^8]
The scaling in the gluing coordinate is essential to this calculation.

The [full conductor proof](research/nodal-conductor-pass20.md)
therefore realizes all these conditions on one actual affine surface.
It does not embed that surface into affine three-space as the
required exceptional hypersurface, construct its disjoint partner,
or supply a global primitive quotient action with the prescribed
complement. Local models at crossings and ramification points do
not furnish those global objects.

## 8. Verification and unresolved obligations

The [execution record](verification-pass-20.json) contains all
437 passing exact test methods across 33 suites. The new suites add
11 multiplier/surface controls and six two-correction controls.
They check the old formula's pole, corrected forward and inverse
jets, distinct-divisor Chinese remaindering, derivative/primitivity
examples, integral minors, residues, and local quotient identities.

These finite controls do not certify a universal geometric theorem.
The [proof audit record](research/proof-audits-pass20.md) separates
written reconstructions from computations. Agreement between
independent model reconstructions is not human peer review, and
none of the source theorems has been formalized here in Lean.

The remaining cancellation obligations are not cosmetic:

1. Recognize polynomial kernels for general principal modifications
   outside the explicitly controlled constructions, or find a valid
   counterexample with both a cylinder isomorphism and a proof of
   nonpolynomiality.
2. Relate an arbitrary slice LND of \(\mathbb C^{[4]}\) to a
   covered invariant-extension frame. An additional solved family
   does not prove that reduction.
3. On the nodal route, resolve global ambient realizability rather
   than reusing the surface-level conditions already satisfied by (22).

The present result is a larger restricted coordinate theorem and a
more precise obstruction boundary. It is not a solution of (1).

## Sources

[^1]: N. Gupta, [*The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry*](https://arxiv.org/abs/2208.14736), ICM survey, 2022. Background and distinction between positive and zero characteristic; not evidence that an unrestricted solution has been obtained here.

[^2]: G. Freudenburg, [*Local slice constructions in k[X,Y,Z]*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), *Osaka Journal of Mathematics* 34 (1997), 757-767, Section 2, Proposition 2 and Theorem 2. Also N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484, Theorem 2.17. Construction credit, not a citation claiming the present all-extension coordinate conclusion.

[^3]: J. Blanc, P.-M. Poloni and I. Van Santen, [*Complements of hypersurfaces in projective spaces*](https://jep.centre-mersenne.org/item/10.5802/jep.264.pdf), *Journal de l'École polytechnique, Mathématiques* 11 (2024), 733-768, Lemma 3.1 and its full inverse proof, 740-741. Exact inherited cylinder step.

[^4]: L. Moser-Jauslin and P.-M. Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*](https://arxiv.org/pdf/2002.12202), 2020 author preprint, Theorem 4.0.1 and Proposition 5.2.1. Explicit congruence/slice predecessors and their simple-root scope.

[^5]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), *Transformation Groups* 4 (1999), 53-95, Proposition 2.1 and proof. Universal lifting property; the two-stage reduction and center-transport checks are detailed separately.

[^6]: S. Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final author version, Lemmas 2.1-2.2, Proposition 3.2 and Theorem 5.2. Used through the prior conditional quotient argument, not as an ambient realization theorem for (22).

[^7]: [Stacks Project, Lemma 15.5.1](https://stacks.math.columbia.edu/tag/08KG) and [Situation 37.67.1, Proposition 37.67.3](https://stacks.math.columbia.edu/tag/0ECH). Finite generation and affine pinching along a closed immersion and finite fold map.

[^8]: J. Kollár, [*Semi Log Canonical Pairs*](https://web.math.princeton.edu/~kollar/book/chap3.pdf), author chapter draft, May 31, 2010, paragraph 8, equation (8.1) and Proposition 9, 6-7. Double-normal-crossing dualizing forms and opposite-residue descent only.
