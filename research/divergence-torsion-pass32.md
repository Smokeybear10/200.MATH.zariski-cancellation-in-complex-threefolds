# Four residual divergence classes for the fixed conductor surface

The divergence obstruction for every additive action of the fixed surface
reduces, in any hypothetical hypersurface presentation, to four classes.
An infinite-dimensional subspace of actions has explicit divergence-free,
exactly equation-preserving polynomial lifts. This is a reduction of the
global obstruction, not a proof that any of the four residual classes
vanishes or is nonzero.

There is also no pointwise formal obstruction: the divergence quotient
vanishes in the completed ambient local ring at every point of the
hypothetical zero hypersurface. These local primitives do not prove a
global polynomial primitive. A separate exact example below shows why
one cannot patch that conclusion by treating the divergence image as an
ideal.

## 1. Unchanged premises and the obstruction being studied

Retain the actual normalization and gluing of
[pass 30](all-noninvariant-surface-pass30.md):
\[
B=\mathbb C[u,y,z]/(A z-y(y-1)),\quad A=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B\times_{\mathbb C[t]^6}\mathbb C[t]^3,
\quad T=\mathbb C+d\mathbb C[u],\quad
M=\mathbb C u+d\mathbb C[u].
\tag{1}
\]
The three paired root values are \((1,i),(1,-i),(-1,i)\), with
the same split-branch labels and scaled parameters as in that note.
Every LND is
\[
D_p=p(u)\delta_0,
\quad p\in M,\quad
\delta_0(u)=0,\quad\delta_0(y)=A,\quad\delta_0(z)=2y-1.
\tag{2}
\]

Assume only conditionally that \(R=W/(F)\) with
\(W=\mathbb C[X,Y,Z]\). The equation is irreducible, since
\(R\) is a domain. The [pass-31 lifting theorem](hypersurface-lifting-pass31.md)
gives an exact polynomial lift \(E_0(F)=0\) of every \(D_p\).
The action fixes the dualizing generator, so
\(\operatorname{div}E_0=Fh\). Its lift-independent obstruction is
\[
\theta_F(D_p)=[h]\in\mathcal C_F[F],\qquad
\mathcal C_F=W/\operatorname{div}\{V:V(F)=0\}.
\tag{3}
\]
It vanishes exactly when \(D_p\) has an exact, divergence-free
polynomial lift. The quotient is a complex vector space and a
\(\mathbb C[F]\)-module, not generally a \(W\)-module.
The map \(p\mapsto\theta_F(D_p)\) is complex-linear: add or
scale exact lifts and their divergence coefficients.

The full [finite-thickening criterion](finite-thickening-algebraization-pass31.md)
has been read. Exact preservation already implies local nilpotence on
every \(W/(F^N)\). None of the arguments below supplies the uniform
nilpotence bounds required for an ambient LND.

## 2. Every invariant Hamiltonian has a good polynomial lift

The established dualizing generator of \(R\), viewed as a rational
two-form on the normalization, is
\[
\omega_R=\frac{du\wedge dy}{A d}.
\tag{4}
\]
This is the normalized version of the opposite-residue construction in
[pass 20, Section 6](nodal-conductor-pass20.md). In particular the poles
on the normalization do not mean it fails to be a regular generator of
the surface dualizing module. Direct contraction gives
\[
\iota_{D_p}\omega_R=-\frac{p(u)}{d(u)}\,du.
\tag{5}
\]

Let \(G\in T\), and choose any polynomial lift \(\widetilde G\in W\).
For the ambient volume form \(\mathrm{vol}\), define the polynomial
Hamiltonian vector field \(K_G\) by
\[
\iota_{K_G}\mathrm{vol}=dF\wedge d\widetilde G.
\tag{6}
\]
It satisfies
\[
K_G(F)=0,\qquad \operatorname{div}K_G=0.
\tag{7}
\]
The first identity follows by wedging (6) with \(dF\), and the
second by applying the exterior derivative. These are polynomial
identities, with no hypothesis about the gradient being a regular
sequence.

Write \(\omega_F\) for the adjunction generator determined by
\(\mathrm{vol}=dF\wedge\widetilde\omega_F\) on the smooth locus.
Then \(\iota_{\overline K_G}\omega_F=-dG\). Both
\(\omega_F\) and (4) generate \(\omega_R\), so
\(\omega_F=\lambda\omega_R\) for some \(\lambda\in\mathbb C^*\):
the multiplier is a unit of \(R\), and \(R^*=\mathbb C^*\).
Consequently (5) shows that
\[
\lambda K_G\bmod F=D_{dG'}.
\tag{8}
\]
One may check equality on the function field, where the two-form is
nondegenerate; equality of derivations of the domain then follows.
Thus
\[
\theta_F(D_{dG'})=0\qquad(G\in T).
\tag{9}
\]
The constant \(\lambda\) affects the explicit normalization of the
lift, but not its existence, divergence, or the kernel subspace in (9).

This is exactly the intrinsic Hamiltonian subspace of the classified
actions. Indeed if \(\iota_{D_p}\omega_R=-dG\) for some
\(G\in R\), equation (5) and the generic coordinates \((u,y)\)
force \(\partial G/\partial y=0\). In characteristic zero this gives
\(G\in\mathbb C(u)\), and \(R\cap\mathbb C(u)=T\). Hence
\(p=dG'\). This converse does not say that every divergence-free
ambient lift must be Hamiltonian with an invariant polynomial potential.

## 3. The remaining source of the obstruction is four-dimensional

Let
\[
T'=\{G':G\in T\}\subset\mathbb C[u]
\tag{10}
\]
denote a complex vector subspace, not an ideal. Every polynomial has a
unique expression
\[
q=G'+a_0+a_1u+a_2u^2,
\qquad G\in d\mathbb C[u],\quad a_0,a_1,a_2\in\mathbb C.
\tag{11}
\]
For existence, eliminate each leading term of degree \(m\ge3\)
using
\[
\frac{d}{du}(d u^{m-3})=(m+1)u^m-(m-3)u^{m-4}.
\tag{12}
\]
The second term is absent when \(m=3\). This decreases degree and
terminates. For uniqueness, a nonzero derivative of an element of
\(d\mathbb C[u]\) has degree at least three; the derivative map is
injective on that subspace.

Every \(p\in M\) has a unique expression \(p=cu+dq\): reduce
modulo \(d\) to see uniqueness of \(c\), then divide in the
domain. Equations (9)-(11) prove
\[
M/(dT')
=\operatorname{span}_{\mathbb C}\{[u],[d],[du],[du^2]\},
\quad \dim_{\mathbb C}M/(dT')=4.
\tag{13}
\]
Here square brackets mean vector-space classes, not subalgebras.
For every hypothetical embedding the exact formula is
\[
\theta_F(D_p)
=c\,\theta_F(D_u)
 +a_0\theta_F(D_d)+a_1\theta_F(D_{du})
 +a_2\theta_F(D_{du^2}).
\tag{14}
\]
In particular the image of the action obstruction has dimension at most
four. This does not bound the dimension of the whole module
\(\mathcal C_F[F]\), assert independence of the four displayed
classes, or prove their values are presentation-independent.

## 4. Exact residue and primitive-difference coordinates

The four-dimensional quotient can be detected on the fixed surface
without knowing \(F\). For \(p=cu+dq\), the one-form (5) has
residue
\[
\operatorname{Res}_{u=r}\left(-\frac{p}{d}\,du\right)
=-\frac{c}{4r^2}\qquad(r^4=1).
\tag{15}
\]
The residues cancel in all three actual pairs. Thus \(c\) is
the separate logarithmic coordinate of the quotient.

Choose any polynomial primitive \(Q'=q\), and set
\[
\Pi(q)=\bigl(Q(i)-Q(1),\ Q(-i)-Q(1),\ Q(i)-Q(-1)\bigr).
\tag{16}
\]
This is independent of the additive constant. The pair graph is
connected, so \(\Pi(q)=0\) exactly when the four values of \(Q\)
agree, which is exactly \(Q\in T\), or \(q\in T'\).
On the basis \(1,u,u^2\) the matrix of (16) is
\[
\begin{pmatrix}
-1+i&-1&(-1-i)/3\\
-1-i&-1&(-1+i)/3\\
1+i&-1&(1-i)/3
\end{pmatrix},
\qquad\det=-8i/3\ne0.
\tag{17}
\]
Thus the residue coefficient and these three primitive differences
give exact coordinates on (13). They are coordinates on a source
quotient, not a computation of the target classes (3).

Nonzero residues alone cannot obstruct a good lift. For the actual
nodal cylinder
\[
R_2=\mathbb C[X,Y,Z]/(Y^2-X^2(X+1)),
\quad X=v^2-1,\quad Y=v(v^2-1),
\tag{18}
\]
the adjunction generator is
\(dv\wedge dZ/(v^2-1)\). Its contraction with the ambient
divergence-free LND \(\partial_Z\) has residues \(-1/2,1/2\)
at \(v=1,-1\). This is a control against a residue-only inference,
not a replacement model for the four-branch surface.

## 5. All local formal divergence quotients on the zero surface vanish

There is a general formal lemma. In
\(\widehat W=\mathbb C[[\xi,\eta,t]]\), suppose either
\(F=\xi\) or \(F=\xi\eta\), and let the ambient volume be
\(v\,d\xi\wedge d\eta\wedge dt\), where \(v\) is a unit.
For any formal \(h\), choose its formal antiderivative in \(t\):
\[
k=v^{-1}\int vh\,dt,\qquad V=k\partial_t.
\tag{19}
\]
Then \(V(F)=0\) and \(\operatorname{div}_{\mathrm{vol}}V=h\).
Formal integration is legitimate in characteristic zero, term by term;
no convergence or polynomial conclusion is asserted.

At every point of a hypothetical presentation of \(R\), the ambient
completed pair has one of these two forms. At a smooth point \(F\)
is a parameter. At a conductor point it initially has form
\(v_0\xi\eta\); replacing \(\eta\) by \(v_0\eta\) is a
formal coordinate change and makes the equation exactly \(\xi\eta\).
The transformed original volume has a unit coefficient, as allowed in
(19). Hence every \(h\) in (3) admits a local formal correction.
All \(\theta_F(D_p)\) map to zero in these completed divergence
quotients.

This conclusion matches, but does not require, the analytic
normal-crossing computation of Barlet and Saito. Their
\(A_f^\bullet=\ker(df\wedge)\) has top cohomology equal to the
local analogue of (3), and their Proposition 2.2 proves freeness in
the normal-crossing case.[^bs] In three variables with at most two
crossing factors, their displayed complex also has an unused coordinate
derivative, whose local integration makes the top quotient zero.

Neither the local analytic statement nor (19) is a theorem about the
global polynomial quotient. The differential is not linear over the
ambient structure sheaf. Faithful flatness of local completion, useful
for ideals in pass 31, does not turn a differential-image quotient
into an ideal-membership problem.

## 6. A global calculation exposing the failed patching shortcut

Take \(W_0=\mathbb C[x,y,z]\) and \(F_0=xyz-1\). Its zero
hypersurface is smooth. Every tangent polynomial field has the form
\[
V=a(x\partial_x-z\partial_z)+b(y\partial_y-z\partial_z),
\qquad a,b\in W_0.
\tag{20}
\]
Indeed from \(V(x)yz+V(y)xz+V(z)xy=0\), reducing modulo each
coordinate gives \(x\mid V(x),y\mid V(y),z\mid V(z)\).
Dividing by \(xyz\) then gives the two-generator formula.
Its divergence is
\[
(x\partial_x-z\partial_z)a+(y\partial_y-z\partial_z)b.
\tag{21}
\]
On a monomial \(x^iy^jz^k\) the two coefficients are \(i-k\)
and \(j-k\). Thus every nondiagonal monomial is in the image,
and no diagonal monomial occurs in any image. Consequently
\[
\mathcal C_{F_0}\cong\mathbb C[xyz]
\tag{22}
\]
as a vector space and a free rank-one \(\mathbb C[F_0]\)-module.
At every point of \(F_0=0\), however, the completed divergence
quotient is zero by (19).

This proves that local formal vanishing does not imply global vanishing
of this type of differential quotient, even with an ambient polynomial
ring and a smooth irreducible zero hypersurface. The example has no
\(F_0\)-torsion, so it does not refute a stronger, still unproved
claim that the particular torsion classes (3) must vanish for our
surface. That distinction is essential.

## 7. Precise remaining question

The infinite-dimensional search has reduced to determining the four
classes in (14), for arbitrary hypothetical \(F\), or proving a
structural theorem annihilating those particular global torsion classes.
Their local formal images, their residue cancellation, and their
dualizing invariance are already compatible with zero. None currently
forces zero or nonzero in the polynomial quotient.

The analytic literature explicitly treats nonisolated critical loci;
it must not be replaced here by the isolated-singularity Koszul
exactness shortcut. In particular the normal-crossing local result
does not supply the missing algebraic global comparison. No assumption
of properness, tameness at infinity, or a globally rectifiable equation
has been introduced.

Even a nonzero class for one action would exclude that action's
divergence-free ambient lift, not the hypersurface embedding. Vanishing
of all four would still not produce an ambient LND: the uniform
nilpotence gap of pass 31 remains. The three-versus-four generator
question and unrestricted cancellation remain open; no novelty or
formal-verification claim is made.

## Independent finite controls

The standalone [divergence_torsion_checks_pass32.py](divergence_torsion_checks_pass32.py)
imports only unittest and SymPy. It checks exact derivative reduction,
primitive-difference coordinates, the original three residue pairs,
Hamiltonian/gauge identities, the genuine nodal-cylinder residue
control, the local integration formula, and the diagonal-monomial
quotient calculation. These are seven finite methods. The universal
statements rely on the written proofs, not the tested degree range.
The targeted run passed all seven methods in 0.623 seconds.

```
/opt/anaconda3/bin/python research/divergence_torsion_checks_pass32.py
```

## Primary-source scope

[^bs]: Daniel Barlet and Morihiko Saito, [*Brieskorn Modules and Gauss-Manin Systems for Non-isolated Hypersurface Singularities*](https://arxiv.org/pdf/math/0411406), version 2. Sections 2.1 and 2.2, including the complete normal-crossing proof, and Remarks 3.6-3.7 were directly read in this pass. The notation uses the kernel complex itself, not only the larger quotient by \(df\wedge d\Omega^1\). These are local analytic statements; no global polynomial torsion-freeness theorem is attributed to them. Their torsion discussion prevents an unsupported extension of isolated-singularity formulas. The finite-dimensional Hamiltonian reduction (8)-(17) and global control (20)-(22) have the elementary proofs above.
