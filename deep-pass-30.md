# Coordinate frames, compatible gauges and all surface symmetries

The corrected complex threefold cancellation problem remains unresolved:
\[
A[s]\simeq\mathbb C^{[4]}
\quad\stackrel{?}{\Longrightarrow}\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Here \(A\) is a finitely generated complex domain and \(s\) is an
indeterminate over \(A\). This interpretation corrects the dimension
mismatch in the supplied conjecture; the field and correction have not
been confirmed by the professor. No conclusion below is a solution of (1).

There is a complete classification for the fixed nonnormal surface
constructed in the preceding notes: all its additive actions and all its
automorphisms are now determined. The classification makes the previous
invariant-generator obstruction independent of the chosen action.
It also exhibits an invertible module of additive velocities of exact
order four, with no common fixed point although every individual
nonzero additive action has fixed points.

Two other results delimit the proposed general methods. Finite Lie
closure with a prescribed translation frame is not automatic, even for
an explicit coordinate derivation with polynomial kernel. Normalizing a
horizontal derivation can also require changing the other derivation in
the pair. Neither a change of frame nor an isolated gauge theorem
provides the missing universal existence argument.

## 1. Scope of the finite-closure criterion

The preceding [recognition theorem](research/levi-bridge-pass29.md)
shows that an LND on complex affine space is polynomially
triangularizable if its Lie closure with all partials of an actual
polynomial coordinate frame is finite-dimensional. In dimension four,
a slice then yields a polynomial three-variable kernel. This is a
sufficient criterion using published geometric results, not an automatic
property of arbitrary sliced actions.

For positive integers \(m,n\), consider the actual coordinates
\[
u=x+y^m,\qquad s=y+u^n,
\qquad
y=s-u^n,\quad x=u-(s-u^n)^m.
\tag{2}
\]
The derivation \(\delta u=1,\delta s=0\) has an explicit slice and
kernel \(\mathbb C[s]\). In the original coordinates,
\[
\delta=
\bigl(1+mn y^{m-1}(x+y^m)^{n-1}\bigr)\partial_x
-n(x+y^m)^{n-1}\partial_y.
\tag{3}
\]
The exact closure \(\operatorname{Lie}_{\mathbb C}
\langle\delta,\partial_x,\partial_y\rangle\) has the following types.

| Parameters | Exact result |
| --- | --- |
| \(m=1\) | Nilpotent of dimension \(n+1\) and class \(n\) |
| \(n=1\) | Nilpotent of dimension \(m+1\) and class \(m\) |
| \(m=n=2\) | Five-dimensional perfect algebra \(\mathfrak{sl}_2\ltimes\mathbb C^2\) |
| \(m,n\ge2,\ m+n>4\) | Infinite-dimensional |

The proof uses intermediate coordinates \(u,v=y\). Put
\(P=\partial_u,Q=\partial_v\). Repeated bracketing extracts
\(P,Q,u^{n-1}Q,v^{m-1}P\) from the three original generators.
For a Hamiltonian \(f\), put \(V_f=f_uQ-f_vP\) and use
\([V_f,V_g]=V_{\{f,g\}}\), where
\(\{f,g\}=f_ug_v-f_vg_u\).

For the remaining cases assume \(m,n\ge2\). Starting with \(h_0=u^n\), the Lie words
\(h_{r+1}=\{u^n,\{v^m,h_r\}\}\) satisfy
\[
h_r=c_r u^{n+r(n-2)}v^{r(m-2)},\qquad
c_{r+1}=-nm\bigl(n+r(n-2)\bigr)
              \bigl(r(m-2)+m-1\bigr)c_r.
\tag{4}
\]
Here \(c_0=1\), and none of the coefficients vanish in characteristic
zero. The coefficient degree of \(V_{h_r}\) is
\(n-1+r(m+n-4)\). Strictly increasing degrees prove infinitely
many independent fields for the last row. This is an all-depth proof,
not a numerical extrapolation.

Adding two passive coordinates gives the same obstruction on
\(\mathbb A^4\), although the kernel is explicitly
\(\mathbb C[s,z_1,z_2]\). Every invertible affine-linear replacement
of the prescribed frame has the same space of translation fields
and hence the same infinite closure. The nonlinear frame
\((u,s,z_1,z_2)\) instead has abelian four-dimensional closure.

The finite/infinite boundary itself is covered by the published
directed-cycle criterion for homogeneous LND generators. It is not
a new finite-dimensionality theorem.[^1] The complete elementary
[proof and boundary analysis](research/finite-closure-frame-obstruction-pass30.md)
makes the precise fixed-frame failure explicit. It does not establish
or disprove the existence of a successful nonlinear frame for an
unknown cylinder in (1).

## 2. Normalizing one action is not normalizing a pair

The exact canonical model is
\[
B=\mathbb C[x,\lambda,w,z],\qquad v=1+\lambda x,\qquad
\Delta=x^2\partial_w+2v^2w\partial_z.
\tag{5}
\]
Consider all LNDs \(\delta\) satisfying \(\delta x=0\) and
\(\delta\lambda=1\), without requiring that they fix
\(F=2xz-w^2\).

Every such \(\delta\) has a unique normalized polynomial gauge
fixing \(x,\lambda\) and equal to the identity modulo \(\lambda\).
It is constructed by the finite slice projection
\[
\rho(f)=\sum_{j\ge0}\frac{(-\lambda)^j}{j!}\delta^j f,
\qquad
U=\rho(w),\quad V=\rho(z).
\tag{6}
\]
The sums terminate by local nilpotence. The map \(\rho\) is
multiplicative, kills \(\lambda\), and has invariant image. Because
\(\lambda\) is already part of the stipulated ambient coordinate
frame, \(\rho(f)=f(0,x,U,V)\). Reduction modulo \(\lambda\)
proves independence of \(U,V\), and the identity
\[
f=\sum_{j\ge0}\frac{\lambda^j}{j!}\rho(\delta^j f)
\tag{7}
\]
supplies the complete polynomial inverse. Thus the new coordinates
are \(x,\lambda,U,V\), with \(\delta=\partial_\lambda\).

This reconstruction cannot be applied to an unknown slice in (1)
by calling it an ambient coordinate. The required presentation
containing that slice would already settle the missing quotient
recognition. The distinction is an input hypothesis, not notation.

There is a separate obstruction when the gauge must normalize
\(\mathbb C^*\Delta\). Modulo \(x\), the vertical action is
\(2w\partial_z\). Any such gauge \(\phi\), fixing \(x,\lambda\),
necessarily has residue
\[
\bar\phi(w)=aw,\qquad
\bar\phi(z)=\gamma a z+P(\lambda,w),
\quad a,\gamma\in\mathbb C^*.
\tag{8}
\]
Indeed its action on the kernel first gives \(aw+b(\lambda)\);
the normalizer equation on \(z\) forces divisibility by \(w\),
hence \(b=0\). As a result, the property
\(\delta w\in xB\) is invariant under every such normalizing gauge.

Every horizontal fixing \(F\) has this property, whereas
\(\delta_1=\partial_\lambda+\partial_w\) does not. Thus this
actual sliced action cannot be brought into the previous
\(F\)-fixing family by any gauge preserving the vertical action
up to a nonzero scalar. Its unrestricted gauge \(w\mapsto
w-\lambda\) works, but transforms the vertical \(z\)-coefficient
to \(2v^2(w+\lambda)\), outside the fixed pair in (5).

An independent formulation uses the actual fixed ideal
\[
J_\Delta=(\Delta(B))=(x^2,w),\qquad
\sqrt{J_\Delta}=(x,w).
\tag{9}
\]
Normalizers preserve this ideal and its radical. Tangency to its
reduced zero locus is therefore a conjugacy invariant.
The \(F\)-fixing family is tangent; \(\delta_1\) is not.
The [complete gauge proof](research/horizontal-gauge-pass30.md)
includes the inverse algorithm and its exact input limits.

## 3. Cylinder homogeneity does not automatically descend

A different exact control addresses attempts to transfer a
transitive group action from a cylinder to its chosen quotient.
For an arbitrary complex affine domain \(A\), the centralizer
of \(\partial_s\) in \(\operatorname{Aut}(A[s])\) consists of
\[
\phi|_A=\sigma\in\operatorname{Aut}(A),\qquad
\phi(s)=s+h,\quad h\in A.
\tag{10}
\]
Its large subgroup of vertical shifts provides no directions
on \(\operatorname{Spec}(A)\). A commuting derivation is
\(D+h\partial_s\), and it is locally nilpotent exactly when
its restriction \(D\) is locally nilpotent on \(A\).

For \(n\ge2\), let \(X_n=\{x^nz=y^2-1\}\). The classical
doubled-line torsor construction gives
\(X_n\times\mathbb A^1\simeq X_1\times\mathbb A^1\).[^2]
The surface \(X_1\) is the conjugacy class of
\(\operatorname{diag}(1,-1)\) in the trace-zero matrices of
determinant \(-1\). Hence its cylinder, and therefore the
cylinder of \(X_n\), is homogeneous under an algebraic group
isomorphic to \(\mathrm{SL}_2\times\mathbb G_a\).

Nevertheless every automorphism of \(X_n\) preserves its two-line
fiber \(x=0\), by the complete published automorphism theorem.[^3]
The normalizer of the chosen cylinder translation therefore
preserves that fiber times the added line, and cannot be transitive.
In particular, homogeneity upstairs does not imply a transitive
normalizer or a homogeneous base.

This control is not a counterexample to affine-space cancellation:
\(H_2(X_n,\mathbb Z)=\mathbb Z\), from the two affine-plane
charts and their \(\mathbb C^*\times\mathbb C\) overlap.
The surfaces and their cylinders are not contractible or affine
spaces. The [full symmetry-descent note](research/intrinsic-symmetry-pass30.md)
records this boundary and distinguishes normalization of the
chosen additive subgroup from mere containment in a group.

## 4. All symmetries of the fixed conductor surface

The fixed surface is obtained from
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),
\qquad d=u^4-1
\tag{11}
\]
by the unchanged scaled pinch of six lines into three pairs.
Write \(a(u)=(u-1)(u-i)\). The pairs are
\[
((1,0),(i,0)),\quad ((1,1),(-i,*)),\quad
((-1,*),(i,1)).
\tag{12}
\]
A split branch \((r,\epsilon)\) has shared parameter
\(t=z/[r(2\epsilon-1)]\); an ordinary branch has
\(t=y/[r a(r)]\). Let \(R\) denote the resulting affine domain.
Its normalization is \(B_0\) and its conductor is \(dB_0\).

Put
\[
\delta_0(y)=a(u),\quad \delta_0(z)=2y-1,\quad
\delta_0(u)=0,\qquad
M=\mathbb C u+d\mathbb C[u],\quad
T=\mathbb C+d\mathbb C[u].
\tag{13}
\]
The complete classification is
\[
\operatorname{LND}(R)=\{p(u)\delta_0|_R:p\in M\},
\quad
\operatorname{Aut}_{\mathbb C}(R)=
\{\exp(p(u)\delta_0)|_R:p\in M\}.
\tag{14}
\]
Every nonzero LND has kernel \(T\), and every automorphism fixes
\(T\) pointwise.

To see the LND assertion, lift its polynomial exponential to the
normalization. The lifted action preserves the intrinsic conductor
\(dB_0\). The LND principal-ideal property forces \(D(d)=0\)
and hence \(D(u)=0\).[^4] On the generic polynomial-line fiber,
\(D=q(u)\partial_y\). Regularity at both split fibers forces
\(q=a p\) with polynomial \(p\). On each branch, the induced
speed of the shared parameter is \(p(r)/r\). The connected
three-edge graph (12) forces these speeds to agree, exactly
the condition \(p=cu+dq_1(u)\). Conversely every such coefficient
descends and is locally nilpotent.

For the automorphism assertion, the common invariant ring is
characteristic. Its normalization forces an affine action on
\(u\) preserving the four roots of \(d\), hence a rotation
\(u\mapsto\alpha u\), \(\alpha^4=1\). The reducible fibers at
\(1,i\) exclude all rotations but the identity. A generic-fiber
automorphism has \(y\mapsto b(u)y+c(u)\). Regularity at all
ordinary fibers and both components of each split fiber removes
every possible pole; applying this to the inverse makes \(b\)
a nonzero constant. The split fibers force \(b=\pm1\). The minus
choice violates the actual pairings in (12), leaving precisely
\(y\mapsto y+a p\). Its forced \(z\)-formula is the exponential
of \(p\delta_0\), with the same descent condition \(p\in M\).

The classification includes all possible discrete automorphisms,
not just a selected connected subgroup. It does not assert that
any action extends to an ambient polynomial ring.

## 5. A nontrivial velocity module and the exact remaining gap

The \(R\)-span of the classified derivations is the invertible module
\[
\mathcal V=(uR+dR)\delta_0.
\tag{15}
\]
Its Picard class has exact order four. For
\(N_k=u^kR+dR\), one has \(N_iN_j=N_{i+j}\) and \(N_4=R\).
For example,
\(u(1-d)u^3+d^2=1\) explicitly proves an inverse identity.
If \(N_k\) were principal, extension to \(B_0\) would make its
generator a unit of \(B_0\), hence a nonzero complex constant.
Then \(u^k\) would belong to \(R\), which the connected gluing
graph permits exactly when \(4\mid k\). This argument proves
nontriviality after the actual pullback, without assuming a
general injectivity theorem for Picard groups.

The two derivations \(u\delta_0,d\delta_0\) have no common fixed
point. At a conductor point the first translates the shared
parameter with speed one; off the conductor their coefficients
have no common zero and \(\delta_0\) has no zero. In contrast,
every individual nonzero coefficient \(p=cu+dq\) has zeros:
if \(c=0\), the conductor is fixed; if \(c\ne0\), a root exists
off the conductor. Thus no single additive action is free.

The previous global branch theorem excluded a three-generator
presentation containing any member of \(T\). Equation (14) now
makes that conclusion intrinsic to all nonzero additive actions.
Changing actions or applying a surface automorphism cannot avoid
it. If a hypothetical hypersurface embedding admits an ambient
LND extending a nonzero surface action, that ambient derivation
must have rank three and infinite Lie closure with the partials
of every ambient polynomial frame.

The missing implication is still substantial: an arbitrary
three-generator presentation does not presently force an
invariant ambient coordinate, nor does an action on a quotient
automatically lift to its polynomial presentation. Consequently
the surface's generator number remains between three and four.
The module in (15) is not, by itself, a proved hypersurface
obstruction. Even a resolution of that embedding question would
need the separate ambient realization and general reduction
steps before it could decide (1).

The [complete all-action proof](research/all-noninvariant-surface-pass30.md)
states these distinctions explicitly. The results give exact
restrictions on proposed proofs, not a universal cancellation
argument. No novelty, expert review or proof-assistant
certification is established.

## Sources

[^1]: Ivan Arzhantsev, Sergey Gaifullin and Viktor Lopatkin, [*On finite-dimensional homogeneous Lie algebras of derivations of polynomial rings*](https://arxiv.org/pdf/2408.05627), Theorem 3.1 and complete Section 3 proof, arXiv pp. 4-6; published in *Izvestiya: Mathematics* 89 (2025), 425-441. Their homogeneous-LND criterion credits earlier work of Arzhantsev, Liendo and Stasyuk and of Arzhantsev and Zaidenberg. The dichotomy here is a special case.

[^2]: Lucy Moser-Jauslin and Pierre-Marie Poloni, [*Isomorphisms between cylinders over Danielewski surfaces*](https://arxiv.org/pdf/2002.12202), Section 2.2, printed p. 3. The one-cylinder isomorphism follows from the two actual additive torsors over the same doubled-origin line.

[^3]: Adrien Dubouloz and Pierre-Marie Poloni, [*On a class of Danielewski surfaces in affine 3-space*](https://arxiv.org/pdf/math/0602549), Theorem 3.10, arXiv pp. 11-12; *Journal of Algebra* 321 (2009), 1797-1812. For exponent at least two every generator preserves \(x=0\); the interchange exception is confined to exponent one.

[^4]: Hubert Flenner and Mikhail Zaidenberg, [*Locally nilpotent derivations on affine surfaces with a C-star action*](https://arxiv.org/pdf/math/0403215), Proposition 1.1 and Corollary 1.2(b), printed pp. 3-4. Only the domain LND facts are used. Their normal-surface classification is not applied to the nonnormal surface \(R\).
