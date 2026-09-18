# Structure of every degree-one horizontal in the fixed canonical model

Every degree-one horizontal in the unchanged canonical polynomial model
has a common polynomial local slice with the vertical pencil. Over
\(\mathbb C(x)\), the entire pencil is simultaneously triangular in
actual polynomial coordinates. The two generating actions consequently
belong to a finite-dimensional nilpotent Lie algebra consisting entirely
of locally nilpotent derivations.

There is also an exact boundary restriction: modulo \(x\), every such
horizontal is triangular and moves \(w\) at constant speed. Neither
result assumes global preservation of the old triangular subalgebra.
They do not construct a polynomial repair path for every primitive top.
A generic coordinate need not have a global polynomial companion.

## 1. Model, normalization, and the uniform slice

Keep the fixed canonical model
\[
B=\mathbb C[x,\lambda,w,z],\qquad
\Delta=x^2\partial_w+2(1+\lambda x)^2w\partial_z.
\tag{1}
\]
Let \(\delta\) be an LND of \(B\) with
\(\delta x=0,\delta\lambda=1\). The supplied-coordinate construction in
[pass 30](horizontal-gauge-pass30.md) gives an actual polynomial
isomorphism
\[
\theta:B\longrightarrow\mathbb C[x,\lambda,b,c],\qquad
\theta\delta\theta^{-1}=\partial_\lambda,\qquad
\theta\equiv\operatorname{id}\pmod\lambda.
\tag{2}
\]
The residue convention is \(w=b,z=c\) at \(\lambda=0\).
Its relative Jacobian is one: an actual polynomial inverse makes
the Jacobian a complex constant unit, and normalization fixes that unit.

Suppose the relative degree is one. Then
\[
\mathcal D_\lambda=\theta\Delta\theta^{-1}
 =D_0+\lambda D_1,\qquad
D_0=x^2\partial_b+2b\partial_c,\qquad D_1\ne0.
\tag{3}
\]
Both coefficients fix \(x\). The leading coefficient \(D_1\) is an
LND. On a polynomial independent of \(\lambda\), the highest
coefficient of \(\mathcal D_\lambda^j\) is \(D_1^j\), and local
nilpotence of the actual conjugate eventually kills it.

Put
\[
K=\mathbb C(x),\qquad u=b/x^2,\qquad v=x^2c-b^2.
\tag{4}
\]
These are actual coordinates of \(K[b,c]\), with inverse
\(b=x^2u,\ c=v/x^2+x^2u^2\), and relative Jacobian one.
Here \(D_0=\partial_u\). The element \(\theta(w)/x^2\) is a
polynomial slice for \(\mathcal D_\lambda\) over \(K[\lambda]\).
Consequently its two plane coefficients generate the unit ideal
in \(K[\lambda,u,v]\). Separate scalar-specialization statements
would not replace this uniform premise.

## 2. A uniformly free linear pencil has a common slice

**Pencil lemma.** Let \(K\) be a characteristic-zero field,
\(T\ne0\) an LND of \(K[u,v]\), and
\(T_\lambda=\partial_u+\lambda T\).
If the coefficients of \(T_\lambda\) generate the unit ideal, then
there are \(Q\in K[v]\), \(F=u+Q(v)\), and nonzero \(g\in K[F]\)
such that, in actual coordinates \(F,v\),
\[
T_\lambda=\partial_F-\lambda g(F)\partial_v.
\tag{5}
\]
In particular \(F\) is a common, \(\lambda\)-independent slice.

The planar additive-action theorem gives an actual coordinate \(F_0\)
with kernel \(K[F_0]\). In a companion coordinate an LND fixing
\(F_0\) has coefficient in \(K[F_0]\). Thus, with the convention
\(J_G=G_v\partial_u-G_u\partial_v\),
\[
T=g_0(F_0)J_{F_0}.
\]
A nonzero constant Jacobian is absorbed into \(g_0\). The cited
theorem is valid over \(K\), not only over algebraically closed
fields.[^plane]

Write \(A=g_0(F_0)(F_0)_u\) and \(C=g_0(F_0)(F_0)_v\).
The premise gives
\[
(\lambda A,1+\lambda C)=K[\lambda,u,v].
\tag{6}
\]
Modulo \(A\), the polynomial \(1+\lambda C\) must be a unit.
Reduction modulo every prime ideal shows that \(C\) is nilpotent
in this quotient, so
\[
C^N\in(A)
\tag{7}
\]
for some \(N\). If \((F_0)_u=0\), then \(A=0,C\ne0\), which
contradicts (6) in the domain \(K[u,v]\). Thus \((F_0)_u\ne0\).

The actual coordinate property implies
\(\gcd((F_0)_u,(F_0)_v)=1\). Equation (7) forces every irreducible
factor of \((F_0)_u\) to divide \(g_0(F_0)\). In the presentation
\(K[u,v]=K[F_0,V_0]\), irreducible polynomials in \(F_0\) remain
prime. Hence \((F_0)_u\in K[F_0]\), up to a constant unit.

If \(d=\deg_uF_0\ge1\), characteristic zero gives
\(\deg_u(F_0)_u=d-1\). A nonconstant polynomial in \(F_0\) would
instead have \(u\)-degree at least \(d\). Therefore
\((F_0)_u=a\in K^*\), and \(F_0=au+Q_0(v)\).
Rescaling gives (5).

The coordinate inverse is explicitly \(u=F-Q(v)\). If \(G'=g\),
a complete coordinate presentation for the pencil is
\[
\lambda,\ F,\ V=v+\lambda G(F),\qquad
v=V-\lambda G(F),\quad u=F-Q(V-\lambda G(F)).
\tag{8}
\]
Here \(T_\lambda V=0\). This is an actual two-sided inverse,
not a Jacobian-conjecture inference.

The uniform coefficient-ideal condition is essential. The pencil
\((1+\lambda)\partial_u\) is an LND, as is every scalar
specialization, but it does not have unit coefficient ideal.
Its top has invariant coordinate \(v\), with zero \(u\)-derivative,
so it fails the conclusion of this lemma.

## 3. Polynomial normal form of the primitive top

Divide the coefficients of \(D_1\) by their polynomial gcd:
\(D_1=\gamma L\), with \(L\) primitive. Then
\(\gamma\in\ker D_1\), and \(L\) is an LND. Indeed, choose a
local slice \(r\) for \(D_1\). The nonzero invariant
\(D_1r=\gamma Lr\), together with additivity of LND degree on
products, makes \(\gamma\) invariant. Division by \(\gamma\)
preserves local nilpotence after localization, and it descends
back to the polynomial ring.

The divergence of \(L\) in \(b,c\) vanishes. Its polynomial
exponential has polynomial inverse and Jacobian one; differentiate
that identity at time zero. Integrating the resulting closed
polynomial one-form over \(\mathbb C[x]\) gives a potential
\[
L=J_F=F_c\partial_b-F_b\partial_c,\qquad F\in\mathbb C[x,b,c].
\tag{9}
\]
Primitivity persists after localization to \(K[b,c]\).
Section 2 and the planar coordinate theorem therefore make
\(L_K\) a nonzero \(K\)-constant multiple of the Jacobian
derivation of the coordinate in (5). Its potential \(F\) is
affine-linear in that coordinate, up to a constant in \(K\).
It follows that
\[
F=p(x)b+Q(x,h),\qquad h=x^2c-b^2,
\tag{10}
\]
initially with \(p\in K^*\) and \(Q\in K[h]\).

There are no coefficient poles in \(x\). At \(x=\alpha\ne0\),
the residues \(b,h\) are independent coordinates, excluding
cancellation of a highest denominator pole. At \(x=0\), its
residue would have the form
\[
p_0b+Q_0(-b^2)=0.
\tag{11}
\]
The odd and even parts imply \(p_0=Q_0=0\), contrary to
the choice of a highest pole. Multiplying by the largest
power of \(x-\alpha\) treats poles of every order. Thus
\(p\in\mathbb C[x]\setminus\{0\}\) and
\(Q\in\mathbb C[x,h]\).

In particular
\[
\begin{split}
L&=x^2Q_h\,\partial_b+(2bQ_h-p)\,\partial_c,\\
Lh&=-x^2p,\qquad LF=0,\qquad D_0F=x^2p.
\end{split}
\tag{12}
\]
There is an exact kernel contraction
\[
\ker L=\mathbb C[x,F].
\tag{13}
\]
Generically the kernel is \(K[F]\). For every \(\alpha\),
\(F(\alpha,b,c)\) is nonconstant: otherwise both coefficients
in (9) would be divisible by \(x-\alpha\), violating primitivity.
Substitution of this nonconstant polynomial is injective on
\(\mathbb C[T]\), so a highest denominator pole of an element
of \(K[F]\) cannot cancel. This proves (13) without assuming
a kernel theorem for arbitrary primitive relative-plane LNDs.

It follows that \(\gamma=g(x,F)\) for a nonzero polynomial
\(g\in\mathbb C[x,F]\). The full global necessary normal form is
\[
\boxed{
\mathcal D_\lambda=D_0+\lambda g(x,F)L,\quad
F=p(x)b+Q(x,x^2c-b^2),\quad
\mathcal D_\lambda F=x^2p(x).
}
\tag{14}
\]
Consequently \(\theta^{-1}F\in\ker\delta\) in the physical ring
and \(\Delta(\theta^{-1}F)=x^2p(x)\). It is a common polynomial
local slice. We do not assert that every \(p,Q,g\) fitting (14)
comes from an actual normalized degree-one gauge.

## 4. The finite nilpotent algebra generated by the pair

Let \(a(x)=x^2p(x)\), \(m=\deg_Fg\), and
\[
V_j=a(x)^j\frac{\partial^jg}{\partial F^j}(x,F)L
\quad(0\le j\le m),\qquad V_{m+1}=0.
\tag{15}
\]
The relation \([D_0,L]=J_{D_0F}=J_{a(x)}=0\) follows from
the divergence-free Jacobian identity. Every multiplier in
(15) is invariant under \(L\). Direct calculation gives
\[
\begin{split}
[\partial_\lambda,\mathcal D_\lambda]&=V_0,\\
[\mathcal D_\lambda,V_j]&=V_{j+1},\\
[\partial_\lambda,V_j]&=0,\qquad [V_i,V_j]=0.
\end{split}
\tag{16}
\]
The complex span of
\(\partial_\lambda,\mathcal D_\lambda,V_0,\ldots,V_m\)
is exactly the Lie algebra generated by the pair. It is
finite-dimensional and nilpotent of class \(m+2\):
successive brackets reach the nonzero \(V_m\), and the next
one vanishes.

Every element of this span is an LND, not just its generators.
Over \(K\), take the actual coordinate companion to \(F\)
from Section 2. In the order \(\lambda,F,v\), a constant
linear combination in (16) is triangular, with its first two
coefficients in \(K\) and its third polynomial in
\(\lambda,F\). It is locally nilpotent over \(K\), hence
on the original polynomial ring by injectivity.

The generic rank is three. The horizontal moves \(\lambda\),
and the determinant of the remaining plane directions is
\[
\det(D_0,L)=-x^2p(x)\ne0.
\tag{17}
\]
The nonzero multiplier \(g\) does not change generic rank.
The joint rational kernel of the pair is \(\mathbb C(x)\);
the joint polynomial kernel is \(\mathbb C[x]\).

The standard finite-dimensional integration theorem for Lie
algebras generated by LNDs applies to this explicitly computed
algebra. In the all-LND case here it yields a connected unipotent
algebraic action.[^integration] This is a conclusion about the
stipulated polynomial model, not an existence theorem for such
pairs on an unknown cylinder.

## 5. Exact reduced-boundary rigidity

This part does not use the planar theorem. Write
\[
W=\theta(w),\quad Z=\theta(z),\quad
H=\theta\bigl(x^2z-(1+\lambda x)^2w^2\bigr).
\]
The Jacobian-one convention implies
\[
\mathcal D_\lambda=J_H,\qquad
\overline H=-\overline W^{\,2}\pmod x.
\tag{18}
\]
Both partial derivatives of \(\overline H\) have
\(\lambda\)-degree at most one. Since
\(\overline W|_{\lambda=0}=b\), one has
\(\overline W_b|_{\lambda=0}=1\). The two factors are nonzero,
and the polynomial ring is an integral domain. Thus
\[
\deg_\lambda\overline W+
\deg_\lambda\overline W_b
 =\deg_\lambda(\overline W\overline W_b)\le1.
\tag{19}
\]
Their leading product cannot cancel. Hence
\(\overline W=b+\lambda A(b,c)\).
The degree-two coefficients in the two derivatives of
\(-\overline W^2\) imply \(AA_b=AA_c=0\).
Either \(A=0\), or the domain property and characteristic zero
make \(A\) a complex constant.

The reduced map still has an actual inverse and Jacobian one.
Its second coordinate consequently has \(Z_c=1\), so
\[
\overline W=b+\alpha\lambda,\quad
\overline Z=c+K(\lambda,b),\quad
\alpha\in\mathbb C,\quad K(0,b)=0.
\tag{20}
\]
The two-sided inverse is
\(b=w-\alpha\lambda,\ c=z-K(\lambda,w-\alpha\lambda)\).
In physical reduced coordinates,
\[
\boxed{
\overline\delta=
\partial_\lambda+\alpha\partial_w+
K_\lambda(\lambda,w-\alpha\lambda)\partial_z.
}
\tag{21}
\]
In particular \(\delta w\bmod x\) is constant for every full-sector
degree-one minimizer.

More generally, start with the boundary replica \(f(w)\partial_z\),
where \(f\) has degree \(d\ge1\), and an actual normalized
relative coordinate change. Its potential is \(-P(W)\), \(P'=f\).
If the conjugate has degree at most one, then
\[
d\deg_\lambda W+\deg_\lambda W_b\le1.
\tag{22}
\]
The derivative \(W_b\) is nonzero because its value at
\(\lambda=0\) is one. When \(d\ge2\), (22) forces \(W=b\);
the map is \((b,c+K(\lambda,b))\), and the boundary horizontal
commutes with the replica. For \(d=1\) the constant-velocity
conclusion (20) holds. No claim is made for degree-zero replicas.

## 6. The remaining repair boundary

The generic simultaneous triangularization holds for every actual
degree-one horizontal in this fixed model, with no triangular
subalgebra assumption and no bound on the supplied gauge's degree.
Formula (14) resolves the existence of a common polynomial local
slice, but not one whose derivative is exactly \(x^2\).

It does not force \(p\) to be a unit, and does not produce a
polynomial companion to \(F\) over \(\mathbb C[x]\). The
nonsliced primitive tops in [pass 32](unrestricted-minimum-pass32.md)
and the arbitrary extra-fiber plinths in
[pass 33](minimum-top-structure-pass33.md) remain consistent with it.
The generic inverse can have poles on special fibers.

Likewise (21) is a boundary necessity theorem, not a claim that
every such residue automorphism lifts \(x\)-adically or polynomially
while satisfying the entire pencil equation. Neither it nor the
finite Lie algebra supplies a path retaining degree one to the
good horizontal. The repair path in [pass 34](plinth-repair-pass34.md)
therefore remains family-scoped.

Finally, the argument uses the actual polynomial presentation
containing \(\lambda\). It does not infer that an arbitrary
sliced polynomial in an unspecified ambient frame is a coordinate.
No general cancellation theorem or universal repair algorithm
is claimed.

## 7. Verification boundary

The separate general_q1_repair_checks_pass35.py supplies bounded
exact controls for actual coordinate inverses, common-slice
identities, coefficient-ideal obstructions, the bracket chain,
and boundary degree calculations. The universal assertions rest
on the written proof. The finite checks do not machine-verify
the published planar or integration theorems.

All seven methods passed in the author-side run in 0.212 seconds.
Independent full-file reviews and reruns passed the same seven methods
in 0.219 and 0.220 seconds. An initial run exposed two
expanded-versus-factored expression comparisons; only the expected
expression normalization was corrected, with no change to a formula.

## Sources

[^plane]: Shigeru Kuroda, [*The automorphism theorem and additive group actions on the affine plane*](https://arxiv.org/pdf/1604.04070), Theorem 1.1 and complete proof, manuscript pages 1–3. The statement covers arbitrary fields and credits the characteristic-zero theorem to Rentschler. Only this established planar invariant-coordinate theorem is imported.

[^integration]: Hanspeter Kraft and Mikhail Zaidenberg, [*Algebraically generated groups and their Lie algebras*](https://arxiv.org/pdf/2203.11356v4), Theorem 3.1.1(1), with its all-LND unipotent specialization. See the source-audited [finite-Lie bridge](levi-bridge-pass29.md). Bracket closure, nilpotence, all-member local nilpotence, and rank here are explicitly proved in Section 4; no universal existence of such an algebra is asserted.
