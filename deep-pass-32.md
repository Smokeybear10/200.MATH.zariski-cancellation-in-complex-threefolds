# Residue obstructions and failed minimum-degree selection

Private working report, September 13, 2026.

The general complex threefold cancellation conjecture is not solved.
This pass finishes a narrower conditional theorem: one actual additive
action of the fixed conductor surface cannot extend to an additive
action on affine three-space under any hypersurface presentation.
It also gives a full polynomial counterexample to the proposed rule
that every globally minimum-degree horizontal choice has a sliced
primitive top. These are distinct results on two different models.

The missing implication remains
\[
A[s]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Neither a generating triple for the surface nor a contradiction to
its existence has been obtained. The professor's intended field and
correction of the dimensional typo remain unconfirmed. No novelty,
human expert review, Lean proof, publication, or external contact is
claimed.

## 1. What changed mathematically

The [full residue proof](research/ambient-residue-obstruction-pass32.md)
forces the invariant base of every proposed nonzero-speed ambient
action to be one particular nodal curve. Its normalized covering
degree is exactly two. That constraint excludes the specified action
with multiplier \(u+u^4-1\), but allows the necessary form of the
different action \(u\delta_0\).

The [unrestricted-minimum counterexample](research/unrestricted-minimum-pass32.md)
has two-sided polynomial coordinate formulas. It has the same
canonical vertical action and the exact global minimum proved in
pass 31, but its primitive top has a fixed line and no slice.
The positive triangular-sector theorem remains correct.

The [divergence calculation](research/divergence-torsion-pass32.md)
reduces an infinite-dimensional family of obstruction classes to four
specified classes. None of those four values has been computed.
The [cross-frame criterion](research/stable-polynomial-invariants-pass32.md)
gives finite sufficient data for intrinsic Makar-Limanov triviality.
It does not prove those data exist for an arbitrary cylinder.

## 2. The surface and the conditional ambient theorem

Retain the unchanged normalization, conductor gluing, and action:
\[
B_0=\mathbb C[u,y,z]/(A_0z-y(y-1)),\quad
A_0=(u-1)(u-i),\quad d=u^4-1,\qquad
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3.
\tag{2}
\]
The three paired root labels are \((1,i),(1,-i),(-1,i)\),
with the split-line labels and scaled parameters fixed in the
[full surface description](research/all-noninvariant-surface-pass30.md).
The surface has exactly three ordinary double-crossing affine lines.
Its normalization is smooth. No hypersurface embedding is presumed
to have been constructed.

The inherited complete action classification and dualizing calculation
give
\[
\operatorname{LND}(R)=M\delta_0,\quad
M=\mathbb C u+d\mathbb C[u],\quad
\ker(p\delta_0)=T=\mathbb C+d\mathbb C[u]\quad(p\ne0),
\]
\[
\delta_0u=0,\quad\delta_0y=A_0,\quad\delta_0z=2y-1,\qquad
\Omega_R=\frac{du\wedge dy}{A_0d},\quad
\iota_{p\delta_0}\Omega_R=-\frac p d\,du.
\tag{3}
\]
For \(p=cu+dq\), the translation speed on each singular line is c.
The logarithmic expression for \(\Omega_R\) is a regular generator
of the dualizing module, not a regular two-form on the normalization.
Opposite residues at the glued branches are essential.[^1]

**Conditional theorem.** If \(R\simeq W/(F)\), \(W=\mathbb C[X,Y,Z]\),
and an ambient LND E induces \(p\delta_0\) with \(c\ne0\), then
\[
\operatorname{image}(\ker E\longrightarrow R)
=S=\mathbb C+d\mathbb C[u^2].
\tag{4}
\]
The plane curve \(\operatorname{Spec}S\) has exactly one ordinary
node. If E is primitive, then \(p=\kappa u\), with
\(\kappa\in\mathbb C^*\). In general
\[
p=uH(u^2),\qquad H(u^2)\in S,\qquad H|_{\text{conductor}}\ne0.
\tag{5}
\]
In particular p is odd. Primitive means that the ambient polynomial
coefficients have no common nonunit factor.

### Why the theorem is not a numerical extrapolation

An ambient LND preserving the principal prime ideal (F) kills F.
Miyanishi's three-variable kernel theorem gives
\(\ker E=\mathbb C[f,g]\), so \(F=P(f,g)\) for an irreducible
plane equation P.[^2] The quotient
\(\mathbb C[f,g]/(P)\) injects into R: dividing an invariant by
the invariant F preserves invariance.

The Jacobian field \(J=\operatorname{Jac}(f,g,\cdot)\) is primitive.
The full proof derives this without first assuming J is an LND.
Since E has zero divergence and kills f,g, it commutes with J.
The gcd of J's coefficients is consequently E-invariant. A prime
invariant dividing that gcd would make \(dQ\wedge da\) vanish at
the generic point of Q=0 for an invariant a nonconstant modulo Q.
Characteristic zero and the injected invariant quotient instead make
the same wedge nonzero. This contradiction removes the gcd.
It follows that \(E=h(f,g)J\) with h polynomial and invariant.
Then \(E^n=h^nJ^n\) proves local nilpotence of J.

The curve ring S is a subring of T containing a nonconstant
polynomial in u. Hence \(\mathbb C[u]\) is finite over S.
Lüroth's theorem and the absence of nonconstant units identify
its normalization as \(\mathbb C[\phi(u)]\) for a polynomial
\(\phi\). The surface maps surjectively to the curve.

Every singular curve point pulls back to singular surface points
by the chain rule for \(F=P(f,g)\). All the conductor lines have
one common image q. Nonzero conductor speed implies \(h(q)\ne0\)
and J is nonzero on the conductor. Thus (f,g) has differential
rank two there. The actual surface's ordinary double crossing
forces q to be an ordinary node. There are no other singular
curve points.

Let a,b be the two normalization points of that node. The full
preimage of \(\{a,b\}\) under \(\phi\) is exactly
\(\{1,-1,i,-i\}\). For primitive E, contraction and adjunction
identify \(p\,du/d\), up to one nonzero constant, with the pullback
of the nodal curve's dualizing generator. Its residues are
\[
\operatorname{Res}_{u=r}\frac p d\,du
=\frac{c}{4r^2}
=\begin{cases}c/4,&r=1,-1,\\-c/4,&r=i,-i.\end{cases}
\tag{6}
\]
The two base residues are nonzero and opposite. Pullback multiplies
each by a positive integer ramification index. Opposite signs
cannot lie over the same branch; equal residues in each pair
force equal ramification indices. Consequently
\[
\phi(u)-a=C(u^2-1)^\ell,\qquad
\phi(u)-b=C(u^2+1)^\ell.
\tag{7}
\]
Equal degree and leading coefficient justify the same exponent
and C. Subtraction is constant only for \(\ell=1\), since otherwise
the difference has nonzero term \(-2\ell C u^{2\ell-2}\).
Thus the normalized base is exactly \(\mathbb C[u^2]\).

A curve smooth away from one ordinary node is recovered from its
normalization by equating the two values at the node. Here this gives
S in (4). The full proof checks the equality through the finite
overring and the completed ordinary-node rings, rather than assuming
a preferred equation. With \(t=u^2\), an explicit presentation is
\[
S=\mathbb C[d,v]/(v^2-d^2(d+1)),\quad
d=t^2-1,\quad v=dt,\qquad \gamma=\frac{dt}{t^2-1}.
\tag{8}
\]
Every dualizing generator differs by a constant unit. Pulling back
\(\gamma\) gives \(2u\,du/d\), proving the primitive assertion.
The invariant factor h restricts to S, proving (5) for every replica.

### The excluded action and the remaining gap

The genuine surface action
\[
D_{\mathrm{bad}}=(u+d)\delta_0
\tag{9}
\]
has conductor speed one but its multiplier is not odd:
\(p(u)+p(-u)=2d\ne0\). Equations (4)-(5) therefore exclude every
ambient LND extension of this specified action under every proposed
hypersurface presentation.

This is a universal conditional obstruction, not an exhibited
embedding with a nonextendable action. The surface's embedding itself
is still unknown. Nor is it a proof that the divergence class of
this action is nonzero.

The [pass-31 exact-lifting theorem](research/hypersurface-lifting-pass31.md)
still supplies an F-preserving derivation lift and compatible
additive actions on all finite F-adic thickenings, conditional on
the same presentation. There is no contradiction. Those statements
never supplied ambient local nilpotence, and a hypersurface
embedding does not have to extend every surface action.

## 3. A genuine global minimizer can have a nonsliced top

Work now in a different, actual polynomial model:
\[
B=\mathbb C[x,\lambda,w,z],\quad v=1+\lambda x,\qquad
\Delta=x^2\partial_w+2v^2w\partial_z.
\tag{10}
\]
The [pass-31 proof](research/minimal-horizontal-pass31.md) establishes
that the minimum relative degree over all actual horizontal LNDs
fixing x and sending \(\lambda\) to one is exactly one.

Here are full polynomial coordinate data attaining that minimum
with the opposite slice outcome. Set
\[
a=\frac23,\quad h=1+a\lambda x,\quad
P=(1-a\lambda x)(1+a^2\lambda^2x^2),\quad
e=a^4\lambda^3x^2,\quad H_0=x^2c-b^2.
\tag{11}
\]
Then \(Ph+e\lambda x^2=1\). Define
\[
W=Pb+eH_0,\quad H=hH_0-\lambda x^2b,\quad
Z=\frac{H+v^2W^2}{x^2}.
\tag{12}
\]
The numerator is divisible by \(x^2\); before setting \(a=2/3\),
its residue is \((2-3a)\lambda x b^2\).
For physical \(I=x^2z-v^2w^2\), the inverse is
\[
b=hw-eI,\qquad
c=\frac{\lambda x^2w+PI+(hw-eI)^2}{x^2}.
\tag{13}
\]
Its numerator residue is \((3a-2)\lambda xw^2\), also zero.
The two-by-two determinant identity proves both full inverse
compositions. These are actual global polynomial coordinates, not
a Jacobian-one assertion or an inverse only after localization.

In these coordinates,
\[
\widetilde\Delta=D_0+\lambda D_1,\quad
D_0=x^2\partial_b+2b\partial_c,\quad
D_1=\frac23xL,\quad
L=x^2\partial_b+(2b+\tfrac32x)\partial_c.
\tag{14}
\]
The transported coordinate partial \(\partial_\lambda\) is a
genuine horizontal LND of relative degree one. Restrict its primitive
top L to the three-variable slice ring \(\mathbb C[x,b,c]\).
There L vanishes on the line \(x=b=0\) and cannot have a slice.
With \(b'=b+3x/4\), its exact kernel and full plinth are
\(\mathbb C[x,x^2c-(b')^2]\) and x squared times that kernel.
The all-degree kernel and plinth proof is in the full note.

This falsifies the unrestricted every-minimizer claim. The bad
horizontal is even tangent to the canonical fixed locus, so that
tangency is not a sufficient repair. It does not preserve the old
triangular subalgebra, and therefore does not contradict the
positive theorem there. Another global minimizer with sliced
primitive top is already known. Selecting a useful minimizer,
rather than an arbitrary one, remains possible in this example
and unproved for the unknown cylinder.

## 4. Only four source classes remain in the divergence calculation

In any hypothetical surface presentation, the pass-31 obstruction is
\[
\theta_F(D_p)\in\mathcal C_F[F],\qquad
\mathcal C_F=W/\operatorname{div}\{V:V(F)=0\}.
\tag{15}
\]
It vanishes exactly when an exact lift can be made divergence-free.
The quotient is a complex vector space and a \(\mathbb C[F]\)-module,
not generally a W-module.

For \(G\in T\), any polynomial lift of G gives an ambient
Hamiltonian field \(\operatorname{Jac}(F,\widetilde G,\cdot)\).
It preserves F and has zero divergence. Contraction with the fixed
dualizing generator shows that it lifts \(D_{dG'}\), after a constant
rescaling. Hence \(\theta_F\) kills \(dT'\).

Leading-term polynomial integration gives the exact vector-space
decomposition
\[
\mathbb C[u]=T'\oplus\operatorname{span}_{\mathbb C}\{1,u,u^2\},
\quad
M/(dT')=\operatorname{span}_{\mathbb C}\{[u],[d],[du],[du^2]\}.
\tag{16}
\]
The second quotient has dimension four. It is the source quotient;
the four target classes may be dependent or zero. No value of
\(\theta_F(D_{\mathrm{bad}})\) has been inferred from (9).

Every completed local divergence quotient on F=0 vanishes by
formal integration in the unused coordinate of \(F=\xi\) or
\(F=\xi\eta\). This is consistent with the local analytic
normal-crossing complex of Barlet and Saito, not a global
polynomial torsion-freeness theorem.[^3]

A separate exact control demonstrates the distinction. For
\(F_0=XYZ-1\), tangent fields are generated by
\(X\partial_X-Z\partial_Z\) and \(Y\partial_Y-Z\partial_Z\).
Divergence removes every monomial except the diagonal powers
\((XYZ)^n\), so \(\mathcal C_{F_0}\simeq\mathbb C[XYZ]\).
The completed quotients on F_0=0 vanish, while this global quotient
does not. This example is torsion-free over \(\mathbb C[F_0]\);
it does not refute a theorem restricted to the particular torsion
classes in (15).

## 5. A cross-frame intrinsic invariant certificate

Return to the full cylinder hypothesis (1), with \(E=\partial_s\).
Choose three actual coordinate LNDs \(T_i\), possibly from different
polynomial frames with verified inverses, and take their highest
nonzero adjoints:
\[
K_i=\frac{(\operatorname{ad}E)^{q_i}T_i}{q_i!},\quad
(\operatorname{ad}E)^{q_i+1}T_i=0.
\tag{17}
\]
The conjugate \(\exp(tE)T_i\exp(-tE)\) is an LND on B[t].
Its highest coefficient is K_i, and the highest coefficient of
a sufficiently high iterate proves that K_i is an LND.
It commutes with E, so it restricts to an intrinsic LND of A.
This is the inherited leading-filtration mechanism, with a direct
proof that does not declare arbitrary lower coefficients LNDs.[^4]

In any actual polynomial coordinates \(x_j\) of B,
\[
\det\bigl(E(x_j),K_1(x_j),K_2(x_j),K_3(x_j)\bigr)_{j=1}^4
\ne0\quad\Longrightarrow\quad \operatorname{ML}(A)=\mathbb C.
\tag{18}
\]
Indeed a common intrinsic invariant is killed by all four columns.
Their rational invertibility makes every ambient partial kill it,
so it is constant. Existence of such a determinant for every (1)
remains unproved. The fields need not commute, so the earlier
commuting-rank-three cancellation argument cannot be applied.

Actual polynomial controls show that every translation in an entire
affine-linear orbit of one bad frame can lose a chosen invariant
at its leading degree. Different bad frames can nevertheless
supply (18). Selecting instead the highest coefficient that moves
the chosen function can produce the non-LND
\(\partial_a+c\partial_b+b\partial_c\), even when the original
coordinate LND sends a to one.

The published inclusion \(\operatorname{ML}^*(A[s])\subseteq
\operatorname{ML}(A)\) does not give the reverse descent needed
here. The known factorial threefold characterization requires
ML triviality together with an intrinsic sliced LND. The ambient
slice s does not fulfill that extra requirement.[^5]

## 6. Verification, limits, and the next proof obligation

The four complete proof notes, independent reconstruction record,
and finite exact controls form a private review packet. The
[regression runner](research/run_regression_pass32.py) reruns the
entire preceding checkpoint and the four new suites. Repeated
targeted runs and inline calculations are not extra test methods.

The saved run from 2026-09-13 10:44:33 UTC through 10:45:56 UTC
passed all 732 methods across 65 suites: 703 prior methods and
29 new methods. The [actual verification log](verification-pass-32.json)
records every suite, command, count, exit code and elapsed time.

The proof of (4)-(5) received two independent AI reconstructions,
including the primitive Jacobian, surjective base map, residue
partition, node-ring equality, and replica quantifiers. The
minimum-degree counterexample has a separate full inverse and
kernel/plinth audit. This is not human peer review, and the
finite tests do not establish the cited classification inputs
or the universal geometric arguments. Full process and source
scope are in [the audit record](research/proof-audits-pass32.md).

The remaining positive cases are precise. On the surface route,
the necessary action \(u\delta_0\) and nodal base (4) are still
compatible with all proved restrictions; a three-generator
presentation or an obstruction to every such presentation is
missing. On the full cancellation route, a sufficient intrinsic
recognition structure must still be extracted from (1).
Neither the cross-frame determinant's existence nor a useful
unrestricted minimizer has been supplied.

The new counterexample closes the every-minimizer shortcut.
The residue theorem closes automatic extension of every
nonzero-speed action. These closed routes should not be
repackaged as conjectures in the next pass. No statement-level
priority certification or expert approval has been obtained.

## Primary sources

[^1]: János Kollár, [*Semi Log Canonical Pairs*](https://web.math.princeton.edu/~kollar/book/chap3.pdf), paragraph 8 and Proposition 9. Opposite residues describe dualizing forms at double crossings. The actual generator and gluing constants in (2)-(3) are proved in the project's [original conductor note](research/nodal-conductor-pass20.md); they are not inferred merely from a generic normal-crossing statement.

[^2]: Daniel Daigle and Shulim Kaliman, [*A Note on Locally Nilpotent Derivations and Variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), Proposition 1.4 and proof, printed pp. 536-537, recording Miyanishi's polynomial-kernel theorem. The primitive Jacobian argument used here is reconstructed explicitly in the full proof. [Stacks Project, Lemma 10.97.3](https://stacks.math.columbia.edu/tag/00MC) supplies faithful flatness for the finite node-ring comparison, not a claim about differential-image quotients.

[^3]: Daniel Barlet and Morihiko Saito, [*Brieskorn Modules and Gauss-Manin Systems for Non-isolated Hypersurface Singularities*](https://arxiv.org/pdf/math/0411406), Sections 2.1-2.2 with the full normal-crossing proof, and Remark 3.6 and Proposition 3.7. These local analytic statements are not promoted to a global polynomial torsion theorem. The formal integration and the XYZ-1 global control have elementary proofs in the linked divergence note.

[^4]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2, attributed to Daigle, and Proposition 3.4 with proof. These are inherited filtration and one-cylinder rigidity inputs. Formula (17) has an independent highest-adjoint proof in the cross-frame note.

[^5]: Nikhilesh Dasgupta and Neena Gupta, [*An algebraic characterization of the affine three space*](https://arxiv.org/pdf/1709.00169), Lemma 3.1 and proof, Lemma 4.5 and Theorem 4.6 with proofs. The exact inclusion direction and intrinsic slice assumption are retained. The inspected statements do not themselves prove (1); this is a bounded source audit, not an assertion of worldwide literature absence.
