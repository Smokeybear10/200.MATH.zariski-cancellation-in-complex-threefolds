# A residue obstruction to ambient additive-action lifts

For the unchanged conductor surface, nonzero translation speed on
its singular lines strongly constrains any extension to an additive
action on affine three-space. Under any hypothetical hypersurface
embedding, an extendable action of nonzero conductor speed must
have an odd polynomial multiplier in the fixed normalization
coordinate u. In particular, the actual action
\((u+u^4-1)\delta_0\) cannot have such an extension.

This is an obstruction to extending a specified action. It is not
an obstruction to the surface embedding itself: embeddings need
not extend all additive actions. No embedding, ambient realization,
cancellation solution, novelty or formal verification is asserted.

## 1. Fixed data and statement

Keep
\[
B_0=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\quad
A(u)=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3,\qquad
\delta_0u=0,\quad\delta_0y=A,\quad\delta_0z=2y-1.
\tag{1}
\]
The three pairs of conductor lines have root labels
\((1,i),(1,-i),(-1,i)\), with the same split-line labels and
scaled line parameters as in the preceding proofs.

The established full classification is
\[
\operatorname{LND}(R)=M\delta_0,\qquad
M=\mathbb C u+d\mathbb C[u],\qquad
\ker(p\delta_0)=T=\mathbb C+d\mathbb C[u]\quad(p\ne0).
\tag{2}
\]
Write \(p=cu+dq(u)\). Its action on each singular line has constant
speed c. The normalization's six conductor lines are exactly
u in \(\{1,-1,i,-i\}\), all points of R away from those lines
are smooth, and every element of T takes one common value at
the four root labels. These statements are inherited from the
[full-action classification](all-noninvariant-surface-pass30.md).

The trivial dualizing module of R has the fixed rational generator
\[
\Omega_R=\frac{du\wedge dy}{A(u)d}.
\tag{3}
\]
The alternate expression using dz extends across A=0.
The scaled gluing makes the two residues opposite at every paired
line, so (3) is also a generator at the double crossings.
Furthermore \(R^*=B_0^*=\mathbb C^*\).
The [original dualizing calculation](nodal-conductor-pass20.md)
and its unchanged rescaling give these facts.[^residue]

**Theorem.** Suppose
\(R\simeq W/(F)\), \(W=\mathbb C[X,Y,Z]\), and an LND E of W
induces \(D=p(u)\delta_0\) with c nonzero. Then:

1. The image S of \(\ker E\) in R is exactly
   \[
   S=\mathbb C+d\mathbb C[u^2].
   \tag{4}
   \]
   Its fraction field is \(\mathbb C(u^2)\), and its plane
   quotient curve has one ordinary node and no other singularities.
2. If E is primitive, then \(p=\kappa u\) for a nonzero constant
   \(\kappa\).
3. For arbitrary E, \(p=uH(u^2)\), where
   \(H(u^2)\in\mathbb C+d\mathbb C[u^2]\) and its common value
   at the conductor is nonzero. In particular p is odd.

The word primitive means that the three ambient polynomial
coefficients have no common nonunit factor.

## 2. The ambient Jacobian normalization

Miyanishi's kernel theorem gives
\(\ker E=\mathbb C[f,g]\).[^kernel]
The principal-ideal property of LNDs gives E(F)=0, since
E preserves the prime ideal (F). Thus
\(F=P(f,g)\) for an irreducible plane polynomial P.
Factorial closure also shows that
\[
S=\mathbb C[f,g]/(P)\hookrightarrow R.
\tag{5}
\]
Indeed, if an invariant belongs to FW, division by the invariant
F leaves another invariant.

For completeness, the Jacobian derivation
\(J=\operatorname{Jac}(f,g,\cdot)\) is primitive, and
\[
E=h(f,g)J,\qquad h\in\mathbb C[f,g]\setminus\{0\}.
\tag{6}
\]
Here is a direct proof that keeps the content issue explicit.
Both fields span the same one-dimensional direction over
\(\operatorname{Frac}W\). Every ambient LND has divergence zero:
the polynomial automorphisms of its additive action have
Jacobian determinant one. Since E kills f and g, the volume
identity \(\iota_J(dX\wedge dY\wedge dZ)=df\wedge dg\)
implies \([E,J]=0\).

Let j be the gcd of J's coefficients, and write J=jH with H
primitive as a polynomial field. The coefficient equations of
\([E,J]=0\) imply \(j\mid E(j)H_i\) for all i. Their gcd is
one, so \(j\mid E(j)\), and the LND principal-ideal property
gives E(j)=0. Thus j belongs to \(\mathbb C[f,g]\).

If j were nonconstant, choose a prime invariant Q dividing it.
Factorial closure makes Q prime in W. Choose an invariant a whose
residue on \(\mathbb C[f,g]/(Q)\) is nonconstant. Its residue
in W/(Q) remains nonconstant. In characteristic zero, at the
generic smooth point of the irreducible hypersurface Q=0,
dQ is nonzero and da has nonzero tangential restriction.
Consequently \(dQ\wedge da\) is nonzero there. But Q and a
are polynomials in f,g, so this wedge is a polynomial multiple
of \(df\wedge dg\), whose coefficients are all divisible by Q.
This is a contradiction. Therefore J is primitive.

The rational coefficient in E=hJ is now polynomial by the gcd
property. Since both divergences vanish, J(h)=0, so h is invariant.
The kernels of E and J agree, and
\(E^n(a)=h^nJ^n(a)\). Thus J is itself an LND.
This proves (6), including that primitive E has constant h.

## 3. The base curve has exactly one ordinary node

The image S lies in T. Some element of S is a nonconstant
polynomial in u, since (5) has dimension one. It follows that
\(\mathbb C[u]\) is finite over S: u satisfies the monic equation
obtained from any such polynomial. Its integral closure inside
\(\operatorname{Frac}S\) is a subring of \(\mathbb C[u]\).

By Lüroth's theorem the normalization of S is a smooth affine
rational curve. It has no nonconstant unit, since it embeds in
\(\mathbb C[u]\). A smooth affine rational curve with this property
is the affine line. Thus its normalized coordinate can be chosen as
a polynomial \(\phi(u)\), and
\[
\widetilde S=\mathbb C[t],\quad t=\phi(u),\quad
[\mathbb C(u):\operatorname{Frac}S]=\deg\phi.
\tag{7}
\]
The map from the u-line to this t-line is finite and surjective.

The map Spec R to Spec S is surjective as well. This follows by
factoring the surjective map from Spec B_0: the map B_0 to the
u-line has nonempty fibers at every u, and the u-line maps finitely
and surjectively to Spec S.

Every singular point of the plane curve \(\Gamma=\operatorname{Spec}S\)
pulls back to singular points of F=0, because the chain rule gives
\(\nabla F=P_f\nabla f+P_g\nabla g\). Every singular point of R
lies on its conductor, and all the conductor lines have the same
image q in Gamma. Surjectivity therefore implies that Gamma has
no singular point other than possibly q.

Reduce (6) modulo F. Because D has nonzero conductor speed,
the common value \(h(q)\) is nonzero, and the restriction of J
has nonzero conductor speed too. At every conductor point its
ambient coefficients do not all vanish. Hence the differential
of (f,g) has rank two there.

It follows that f-f(q), g-g(q) are part of a regular parameter
system at each such ambient point. Since the actual surface has
an ordinary double crossing there, P has a quadratic initial part
of rank two at q. Thus q is an ordinary plane node, not a cusp,
tacnode, higher multiple point or smooth point.

Let a and b be the two distinct normalization points over q.
Every root of \(\phi(u)-a\) or \(\phi(u)-b\) maps to q and hence
to the surface's singular locus. Conversely every conductor
root maps to one of them. Therefore
\[
\{u:\phi(u)=a\text{ or }\phi(u)=b\}=\{1,-1,i,-i\}.
\tag{8}
\]

## 4. Residues force a quadratic cover

First take E primitive, so h in (6) is a nonzero constant.
The hypersurface adjunction generator
\(\Omega=\operatorname{Res}(dX\wedge dY\wedge dZ/F)\)
is a constant multiple of (3), because \(R^*=\mathbb C^*\).

The plane adjunction differential is
\(\gamma=dg/P_f=-df/P_g\) on the smooth locus of Gamma.
It generates its dualizing module. The identity
\[
df\wedge dg=dF\wedge\gamma
\tag{9}
\]
and contraction with E show, up to a nonzero constant, that
\[
\frac{p(u)}{d}\,du=\phi^*\gamma.
\tag{10}
\]
This identity is in rational differentials on the normalization;
it does not assert that the singular surface's dualizing
contraction is a Kähler one-form everywhere.

At the two branches of the ordinary node, gamma has nonzero
opposite residues \(\rho,-\rho\). Pullback by a finite map
multiplies a residue by the positive integer ramification index.
On the left side of (10), the four residues are, up to the same
overall constant,
\[
\operatorname{Res}_{u=r}\frac p d\,du
=\frac{c}{4r^2}
=
\begin{cases}
c/4,&r=1,-1,\\
-c/4,&r=i,-i.
\end{cases}
\tag{11}
\]
A single base branch cannot receive both signs: that would
require positive ramification indices of opposite sign.
The equal residues also force equal indices within each pair.

After exchanging a,b if necessary, (8) therefore gives
\[
\phi(u)-a=A(u^2-1)^\ell,\qquad
\phi(u)-b=A(u^2+1)^\ell
\tag{12}
\]
for a nonzero constant A and a positive integer ell.
The exponent is the same on both sides because both polynomials
have degree deg phi. Their leading coefficient is also the same.
Subtracting the identities gives a nonzero constant; for ell>1
their difference has leading nonconstant coefficient
\(-2\ell A\,u^{2\ell-2}\). Thus ell=1 and
\[
\phi(u)=A u^2+B,\qquad \widetilde S=\mathbb C[u^2].
\tag{13}
\]

This residue argument applies to the primitive J in (6) also
when the original E is not primitive, since h(q) is nonzero.
Hence (13) holds in both cases.

## 5. The curve ring and primitive multiplier are exact

Put t=u^2 and \(d=t^2-1\). The plane curve Gamma is smooth
away from its one ordinary node, whose two normalization points
are t=1 and t=-1. Its coordinate ring is consequently exactly
\[
S=\{r(t)\in\mathbb C[t]:r(1)=r(-1)\}
 =\mathbb C+(t^2-1)\mathbb C[t].
\tag{14}
\]
To justify the equality without assuming a chosen plane equation,
the right ring is finite over S and equal to it away from q.
At q the normalization of an ordinary node is the pair of
formal smooth branches, and its completed ring consists of
pairs having equal constant term. This is also the completed
ring on the right of (14). Faithful flatness of completion
annihilates the finite quotient, proving equality.

The ring in (14) has the explicit presentation
\[
\mathbb C[d,v]/(v^2-d^2(d+1)),\qquad v=dt,
\tag{15}
\]
with adjunction generator \(dd/(2v)=dt/d\).
Every other global dualizing generator is a constant multiple:
the only units are constants. Substituting \(t=u^2\) into (10)
now forces
\[
p(u)=\kappa u
\tag{16}
\]
for primitive E, with kappa nonzero.

For general E=h(f,g)J, the primitive J restriction has the form
(16), while h restricts to an element of S. Therefore
\(p=uH(u^2)\), with H in (14) and H(q) nonzero. This proves
all parts of the theorem.

## 6. An actual action with no ambient additive extension

The polynomial
\[
p=u+d=u+u^4-1
\tag{17}
\]
belongs to M and has c=1. It therefore defines an actual LND
of the fixed R, with nonzero translation speed on all three
singular lines. It is not odd:
\(p(u)+p(-u)=2d\ne0\).
The theorem excludes its extension to an LND of W in every
hypothetical hypersurface presentation.

This is stronger than showing that one chosen derivation lift
is not locally nilpotent. Every ambient LND lift of this action
is excluded, conditional on the presentation. The pass-31 proof
still supplies an exact F-preserving polynomial derivation lift
and additive actions on every finite F-adic thickening for it.

There is no contradiction: uniform ambient nilpotence was never
proved by those infinitesimal statements. Nor does the present
result exclude a hypersurface embedding or an ambient extension
of the different action u delta_0. That action, its degree-two
base and its nodal invariant subring remain compatible with
the necessary conditions derived here.

## Sources and verification scope

The full polynomial-kernel theorem is the cited inherited
three-variable classification input. The content/Jacobian proof,
finite normalized curve argument, residue partition and degree
calculation are written above. Exact finite controls cannot
replace those universal geometric arguments.

The standalone [ambient_residue_checks_pass32.py](ambient_residue_checks_pass32.py)
imports only unittest and SymPy. Its six finite methods check the
actual multiplier and conductor speeds, a primitive ambient Jacobian
and its invariant replicas, the residue partition, the cover-power
identity, the exact nodal ring and dualizing pullback, and the
nonzero-speed boundary of the theorem. The targeted run passed all
six methods in 0.135 seconds. Two separate AI reconstructions of
the complete geometric argument found no correction; neither is
human expert review or proof-assistant verification.

```
/opt/anaconda3/bin/python research/ambient_residue_checks_pass32.py
```

[^kernel]: D. Daigle and S. Kaliman, [*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), Proposition 1.4 and proof, printed pp. 536-537, recording Miyanishi's kernel theorem; Theorem 1.5 also gives the known faithfully flat quotient. Only the kernel theorem is essential to the argument above.

[^residue]: J. Kollár, [*Semi Log Canonical Pairs*, author chapter](https://web.math.princeton.edu/~kollar/book/chap3.pdf), paragraph 8 and Proposition 9, for the opposite-residue dualizing description at ordinary double crossings. The actual generator and gluing constants are proved in the linked original surface note. Local completion is faithfully flat by [Stacks Project, Lemma 10.97.3](https://stacks.math.columbia.edu/tag/00MC).
