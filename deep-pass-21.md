# Noninvariant slice extensions and cancellation reductions

The unrestricted implication
\[
X\times_{\mathbb C}\mathbb A^1\cong\mathbb A^4
\quad\Longrightarrow\quad X\cong\mathbb A^3
\tag{1}
\]
is not proved here. The main result is an explicit family that invalidates
two proposed shortcuts toward it. These examples have primitive rank-three
base derivations and polynomial kernels, but no slice affine in the
original added variable and no invariant added coefficient obtainable
while preserving the original three-variable subring.

A second result gives an exact finite presentation for every principal
modification in the invariant-extension reduction. The denominator bound
exists universally; an attempted automatic lifting of the prescribed
thickened-divisor automorphism does not. An explicit counterexample
separates failure of that lift from failure of polynomiality.

The geometric investigation computes the conductor module, Picard group,
and stable cotangent class of a previously constructed nodal surface.
All of these proposed obstruction tests fail to exclude its embedding.
No embedding, ambient quotient, or cancellation counterexample results.
The statements below are working mathematical proofs with separate
reconstructions and exact algebraic controls, not human peer review or
proof-assistant verification. Mathematical priority remains unestablished.

## 1. The primitive noninvariant family

Write \(R=\mathbb C[x,y,z]\). For \(n\ge2\), set
\[
\begin{split}
f&=xz-y^2,\\
r&=x^3+yf^n,\\
h&=zf^{2n}+2x^2yf^n+x^5,\qquad
D=-\operatorname{Jac}(f,h,\cdot).
\end{split}
\tag{2}
\]
This is the quadratic, \(P=x^2\), specialization of the published
local-slice family. It has primitive rank three, invariant ring
\(C=\mathbb C[f,h]\), and full plinth ideal \(f^nhC\).[^1]
The sign convention in (2) gives
\[
xh=r^2+f^{2n+1},\qquad Dr=f^nh,\qquad Dx=2f^nr.
\tag{3}
\]

Choose
\[
q=f^\ell J(f,h),\qquad
\lceil n/2\rceil\le\ell<n,\qquad J(0,h)\ne0,
\quad E=D+(1+qr)\partial_t.
\tag{4}
\]
The condition on \(J(0,h)\) means that it is a nonzero polynomial,
not that it is a unit or nonzero at every complex point.
The derivation \(E\) is locally nilpotent because it restricts to
\(D\) on \(R\) and satisfies \(E^3t=0\).

**Theorem.** For every choice in (4):

- \(E\) has an explicit slice of \(t\)-degree two, and no slice of
  \(t\)-degree zero or one.
- No polynomial automorphism preserving \(R\) as a subalgebra makes
  the added coefficient invariant under the transported base derivation.
- Nevertheless there are explicit polynomial coordinates
  \(X,Y,Z,\sigma\) of \(R[t]\) with \(E=\partial_\sigma\).
  In particular, \(\ker E=\mathbb C[X,Y,Z]\).

Thus the theorem is an obstruction to a specified reduction method,
not a counterexample to (1). Its complete derivation is also available
in the [standalone proof](research/primitive-noninvariant-bridge-pass21.md).

### 1.1. A polynomial transformation before imposing a surface equation

Work over a domain containing \(\mathbb Q\), fix \(h\), and let
the invariant coefficients \(a,q,c\) satisfy \(a\ne0\), \(ac=q^2\).
For the derivation
\[
\mathcal E=2ar\partial_x+ah\partial_r+(1+qr)\partial_t,
\]
put
\[
L=qx/2-at,\qquad \rho=r+hL,\qquad X=x+L(r+\rho),
\tag{5}
\]
\[
\sigma=t-qrt-\frac{q^2xh}{2}t+\frac{ahq}{2}t^2
       +\frac c2xr+\frac{cq}{8}x^2h.
\tag{6}
\]
Direct differentiation gives \(\mathcal EX=\mathcal E\rho=0\)
and \(\mathcal E\sigma=1\). The quadratic identity is preserved:
\(Xh-\rho^2=xh-r^2\).

The inverse, in independent variables \(X,h,\rho,\sigma\), is
\[
\begin{split}
L'&=a\sigma-qX/2,\qquad r=\rho+hL',\\
x&=X+L'(r+\rho),\\
t&=\sigma+\frac q2\sigma(r+\rho)-\frac c4X(r+\rho).
\end{split}
\tag{7}
\]
Both compositions are identities. These formulas are polynomial,
not merely rational maps defined where \(a\) or \(h\) is invertible.
Requiring a rational coefficient domain is important: characteristic
zero alone does not put the displayed halves and eighths in the ring.

In (4), take \(a=f^n\) and \(c=f^{2\ell-n}J^2\). The inequality
\(2\ell\ge n\) makes \(c\) polynomial, so (6) is a slice on the
actual four-variable ring. Its quadratic coefficient \(f^nhq/2\)
is nonzero. In particular \(E^2t=f^nhq\ne0\), so the original
added coefficient is genuinely noninvariant.

### 1.2. The exact second image gives both obstructions

The needed image ideal can be reconstructed directly:
\[
\ker D^3=C\oplus Cr\oplus Cx,\qquad
D^2(R)\cap C=f^{2n}hC.
\tag{8}
\]
After inverting \(f\), the monic surface presentation has free
coefficient-module basis \(x^jr^\epsilon\), \(\epsilon=0,1\).
Their distinct derivation degrees are \(2j+\epsilon\), so degree at
most two is spanned by \(1,r,x\).

There are no hidden coefficient poles at \(f=0\). A highest pole,
after clearing its denominator, would give a nontrivial relation
\[
A(x^5)+B(x^5)x^3+C_1(x^5)x=0.
\tag{9}
\]
The exponents of the three summands are respectively \(0,3,1\)
modulo five, so they cannot cancel. This proves the first equality
in (8); the second follows from \(D^2x=2f^{2n}h\).
This argument proves the full image ideal, not merely its behavior
on a finite collection of monomials.

For arbitrary \(q\in C\), (8) gives the exact criterion
\[
1+qr\in C+D(R)\quad\Longleftrightarrow\quad f^n\mid q.
\tag{10}
\]
For necessity, apply \(D\) and cancel \(f^nh\). For sufficiency,
use the polynomial primitive \(qx/(2f^n)\).
The coefficient in (4) fails this criterion because \(\ell<n\).

An \(R\)-automorphism of \(R[t]\) sends \(t\) to \(ut+H\),
where \(u\in\mathbb C^*\), \(H\in R\). Its new coefficient is
\(u(1+qr)+DH\), so (10) excludes making it invariant. Allowing an
automorphism of \(R\) itself does not change this obstruction:
it transports \(C\) and \(D(R)\) isomorphically. Here \(C+D(R)\)
is an additive subspace, not an assertion that \(D(R)\) is an ideal.

Now suppose \(At+v\) were a slice. Coefficient comparison gives
\(A\in C\) and \(Dv+A(1+qr)=1\). Applying \(D\) and using (8)
forces \(f^{n-\ell}\mid A\). At the fixed origin of \(D\), however,
the same slice equation gives \(A(0)=1\), a contradiction.
Consequently the minimum \(t\)-degree of a slice is exactly two.
The previously proved affine-replacement result required an invariant
added coefficient; dropping that hypothesis is invalid.

### 1.3. Lifting the transformation to the physical polynomial ring

The surface-cylinder automorphism (5)-(7) alone is insufficient:
its surface generators are not independent ambient coordinates
of \(R\). The remaining proof must clear the original modification
denominators in both directions.

Modulo \(f^n\), the transformation is independent of \(t\) and has
\[
h\mapsto h,\qquad r\mapsto r+qxh/2,\qquad x\mapsto x+qxr.
\tag{11}
\]
It preserves the vertex ideal and is the identity modulo \(f\).
On the old curve \((x,h,r)=(u,u^5,u^3)\), it induces
\[
X=u+q(f,u^5)u^4,\qquad
\rho=u^3+\tfrac12q(f,u^5)u^6.
\]
Both \(q^2\) and \(q\,q_h\) vanish modulo \(f^n\), so first-order
substitution is exact in that quotient.

Take the remainder of
\[
\widetilde P(X,f)=X^2-\frac52q(f,X^5)X^5\pmod{f^n}.
\tag{12}
\]
The two curve identities are \(\rho=X\widetilde P\) and
\(h=X\widetilde P^2\). The inverse parameter is
\(u=X-q(f,X^5)X^4\). These are universal parameter identities,
so they remain valid after passage to the physical ring.

Define
\[
Y=\frac{\rho-X\widetilde P}{f^n},\qquad
Z=\frac{h-2\widetilde P Yf^n-X\widetilde P^2}{f^{2n}}.
\tag{13}
\]
The first curve identity makes \(Y\) polynomial. Multiplying the
second numerator by \(X\) gives \(f^{2n}(Y^2+f)\). Since
\(f=xz-y^2\) is prime and \(X\equiv x\pmod f\), repeated prime
cancellation makes \(Z\) polynomial, and \(f=XZ-Y^2\).

For the inverse, start with independent \(X,Y,Z,\sigma\). Set
\[
f=XZ-Y^2,\quad
\rho=X\widetilde P+Yf^n,\quad
h=Zf^{2n}+2\widetilde P Yf^n+X\widetilde P^2,
\]
and apply (7). The inverse curve identity clears
\(y=(r-x^3)/f^n\), and the same prime-cancellation argument clears
the original \(z\). The maps are inverse after inverting \(f\);
both are polynomial maps between domains, so they are inverse globally.
All three coordinates \(X,Y,Z\) are invariant, proving the theorem.

The denominator-lifting principle is established affine-modification
machinery, not a new general construction. The
[two-stage comparison](research/priority-boundary-pass20.md) supplies
its full center-ideal hypotheses and reduction to Kaliman-Zaidenberg
Proposition 2.1.[^2] The specific curve compatibility and the family-level
consequence require their own priority assessment.

## 2. What an arbitrary slice frame still requires

Let \(B=\mathbb C^{[4]}=A[s]\), \(E(s)=1\), and \(A=\ker E\).
The statements that \(A\) is a polynomial three-ring, that \(s\)
is a coordinate, and that \(A\) contains an ambient coordinate are
equivalent. The last implication uses the published regular-kernel
recognition theorem for a four-variable LND fixing a coordinate.[^3]
That theorem does not produce the invariant coordinate.

There is a weaker exact structural reformulation. If \(B=R[w]\)
and \(E(R)\subset R\), local nilpotence forces
\[
E=D+b\partial_w,\qquad b\in R,\qquad [E,\partial_w]=0.
\tag{14}
\]
This restriction/extension principle is established prior work.[^1][^4]
A direct proof, including characteristic-zero domains that do not
contain \(\mathbb Q\), appears in the
[frame note](research/arbitrary-slice-frame-pass21.md).
Thus an \(E\)-stable coordinate three-ring exists exactly when
a genuine coordinate partial commuting with \(E\) exists.

Finding that partial and making \(b\) invariant are different
requirements. The latter, in a fixed \(R\), is exactly
\(b\in\ker D+D(R)\). The theorem in Section 1 disproves its
automatic validity even for a primitive rank-three base with a slice.
An abstract polynomial subalgebra also does not suffice:
\(\mathbb C[a^2,b,c]\subset\mathbb C[a,b,c,s]\) is polynomial
but has no one-variable polynomial complement.

Even linear-frame extraction is too strong. Begin with coordinates
\((a,b,c,s)\), and put
\[
u=a+s^2,\quad v=b+u^2,\quad w=c+v^2,\quad z=s+w^2.
\tag{15}
\]
The inverse is obtained in reverse order. The translation
\(\partial_s\), in these coordinates, becomes
\[
E=2s\partial_u+4us\partial_v+8uvs\partial_w
 +(1+16uvws)\partial_z,\qquad s=z-w^2.
\tag{16}
\]
It has an explicit polynomial kernel and a quadratic slice.

No nonzero constant vector field commutes with (16). The \(u\)
component of the commutator first forces its \(w,z\) coefficients
to vanish; the \(v\) and \(w\) components then force the other two
coefficients to vanish. By (14), no three-ring generated by three
independent affine-linear forms can be stable under \(E\).
The nonlinear frame (15) still works, so this is not an obstruction
to every coordinate frame.

Replacing commutation by preservation of the slice foliation does
not enlarge the class of locally nilpotent candidates. For an LND
\(T\) on \(A[s]\), the conditions
\[
T(A)\subset A,\qquad [T,E]\in BE,\qquad [T,E]=0
\]
are equivalent by (14). An arbitrary intrinsic additive action
therefore cannot be called a coordinate partial without proving
the missing coordinate assertion.

## 3. The universal finite-center presentation

Suppose now that the invariant-extension reduction has genuinely
been reached. Let \(D\ne0\) be primitive on \(R=\mathbb C^{[3]}\),
write \(C=\ker D\), and choose a minimal local slice \(Dr=p\).
For \(0\ne V\in C\) with \((p,V)C=C\), the ring to recognize is
\[
M=R[r/V].
\tag{17}
\]
The earlier [two-way reduction](research/arbitrary-invariant-kernel-pass18.md)
identifies these rings precisely with the relevant invariant
affine-slice kernels. The present statement does not identify
every cancellation factor with such a ring.

**Finite-center lemma.** There are \(N\ge1\) and
\(I\subset S=C[T]\), with \(p^N\in I\), such that
\[
R\cong_C S[I/p^N],\qquad
M\cong_C S[\theta(I)S/p^N],\qquad
\theta(T)=VT,\quad \theta|_C=\mathrm{id}.
\tag{18}
\]
The map \(\theta\) is an automorphism modulo \(p^N\).
If \(V\equiv1\pmod{p_{\mathrm{red}}}\), its reduction on the
reduced coefficient divisor is the identity.

Indeed, \(R_p=C_p[r]\). Choose one exponent \(N\) clearing the
denominators of the three original coordinates and set
\(I=p^NR\cap C[r]\). The fractions \(I/p^N\) all lie in \(R\)
and include its three generators. In the second presentation,
evaluate \(T\) at \(w=r/V\): the transformed fraction
\(\theta(F)(w)/p^N\) is exactly \(F(r)/p^N\).
Together with \(w\), these fractions generate \(M\).

Comaximality makes \(V\) a unit modulo \(p^N\), proving the
quotient automorphism assertion. The ideals are stable under
\(p\partial_T\), since
\((p\partial_T)\theta=V\theta(p\partial_T)\).
No module-freeness or invariant ambient coordinate assumption was
introduced. Here finite means finitely many ideal generators and
a bounded thickening, not a finite-dimensional complex vector space.

### 3.1. The prescribed jet need not lift

Consider
\[
D=x^2\partial_y+2y\partial_z,\quad
h=x^2z-y^2,\quad C=\mathbb C[x,h],\quad p=x^2,\quad V=1+x.
\]
This base is primitive, its plinth is exactly \(x^2C\), and its
reduced plinth is connected. With \(N=1\),
\[
I=(x^2,h+T^2),\qquad
J=(x^2,h+(1+x)^2T^2).
\tag{19}
\]
The first ideal is the actual contraction \(x^2R\cap C[y]\),
not an artificial larger center.

The quotient automorphism fixes \(x,h\) and sends
\(T\) to \((1+x)T\) modulo \(x^2\). Suppose a polynomial
automorphism preserving \((x^2)\) induced that exact map.
Unique factorization forces its image of \(x\) to be \(x\), so
the other images have the forms
\[
h+x^2H,\qquad (1+x)T+x^2L.
\]
Its Jacobian determinant is \(1+x\pmod{x^2}\), which cannot be
a nonzero constant. Such an automorphism does not exist.

Nevertheless the triangular automorphism
\[
x\mapsto x,\quad T\mapsto T,\quad
h\mapsto h+\big((1+x)^2-1\big)T^2
\tag{20}
\]
carries \(I\) to \(J\) exactly. Moreover \(y=(1+x)w\) gives
\(M=\mathbb C[x,w,z]\). Thus insisting on the exact
coefficient-fixing quotient map loses a valid alternative center
transport. A universal repair must address the full centers without
silently assuming that this particular jet lifts.

### 3.2. Published reconstruction does not supply polynomial descent

The modified-commuting construction of Dasgupta-Gaifullin starts
with invariant ambient coordinates and covers rank at most two.
A primitive rank-three derivation has no nonequivalent commuting
LND, by their characterization.[^1] This limits that method;
it does not prohibit noncommuting changes of local slices.

Freudenburg's degree reconstruction is finite over a Noetherian
kernel, but its intermediate rings need not be polynomial.[^5]
In his explicit rank-three example the second positive-degree ring is
\[
\mathbb C[F,G,T,X]/(XG-F^3-T^2).
\tag{21}
\]
Its gradient vanishes at the origin, where the tangent dimension
is four rather than three. A polynomial-ring induction cannot pass
through this singular stage without another recognition theorem.

The [full source-scope note](research/universal-bridge-pass21.md)
also distinguishes connected blocks in a kernel graph from global
connectivity, and suspension flexibility from polynomial recognition.
Neither is used as a missing universal theorem here. The residual
problem is compatible center recognition, not existence of a finite
denominator bound.

## 4. Global tests for the nodal surface

The following calculations concern an actual affine surface, not
only a proposed incidence diagram. Fix \(a_0^4=3\), put
\(w_1=a_0,w_2=-a_0,w_3=ia_0,w_4=-ia_0\), and set
\[
d=w^4-3,\quad A_0=(w-w_1)(w-w_3),\qquad
B_0=\mathbb C[w,y,z]/(A_0z-y(y-1)).
\]
The normalization \(B_0\) is smooth. Its six lines over \(d=0\)
are paired as
\((L_{10},L_{30})\), \((L_{11},L_4)\), and \((L_2,L_{31})\).
In \(L_{j\epsilon}\), \(j\) records the root and \(\epsilon\)
records \(y=0,1\).

The pairwise gluing uses \(t=z/[w_j(2\epsilon-1)]\) on a split
line and \(t=y/[w_jA_0(w_j)]\) on an unsplit line. Write
\[
D_0=B_0/dB_0\cong\mathbb C[t]^6,\quad
C_0=\mathbb C[t]^3,\quad
R_0=B_0\times_{D_0}C_0,
\tag{22}
\]
where \(C_0\) maps pairwise diagonally.
The [construction proof](research/nodal-conductor-pass20.md) gives
an integral finite-type surface, conductor \(I=dB_0\), local
double normal crossings, and trivial dualizing sheaf.

### 4.1. Module generators and the Picard group

The distinct values of \(w\) on every paired pair give
\[
B_0=R_0+R_0w,\qquad I=(d,dw)R_0,\qquad B_0/R_0\cong R_0/I.
\tag{23}
\]
For any pair of residues \(b_i(t),b_j(t)\), solve
\(b_i=c_0+w_ic_1\), \(b_j=c_0+w_jc_1\).
The determinant \(w_j-w_i\) is a nonzero constant, so the solutions
are polynomial. Lifting \(c_0,c_1\) through \(R_0\to C_0\)
proves the first equality; the same residue calculation proves
the last isomorphism.

Localizing \(B_0\) at \(A_0\) gives a factorial ring. The four
removed split lines generate \(\operatorname{Cl}(B_0)\), with exactly
the two relations given by the two complete split fibers.
Consequently \(B_0^*=\mathbb C^*\) and
\(\operatorname{Pic}(B_0)\cong\mathbb Z^2\).
The Units-Pic sequence for (22) then gives[^6]
\[
0\longrightarrow(\mathbb C^*)^3
\longrightarrow\operatorname{Pic}(R_0)
\longrightarrow\mathbb Z^2\longrightarrow0.
\tag{24}
\]
This splits as an abstract abelian-group sequence, not canonically.
No statement about a Picard scheme is intended. Nonzero Picard
group alone cannot exclude a hypersurface embedding: the smooth
normalization above is itself a hypersurface with nonzero Picard group.

### 4.2. The stable cotangent class also passes

On the regular surface \(B_0\), \(SK_0\) is generated by closed-point
classes.[^7] Every point lies on a closed affine-line component
of a fiber of \(w\). The multiplication sequence on that line
makes its point class zero, and exact pushforward gives
\(SK_0(B_0)=0\).

The projective-module Milnor sequence for (22) now shows
\[
SK_0(R_0)=0,\qquad
K_0(R_0)\cong\mathbb Z\oplus\operatorname{Pic}(R_0).
\tag{25}
\]
Here is the precise diagram chase. A rank-zero, determinant-trivial
class vanishes on \(B_0\) and \(C_0\), so it comes from
\(K_1(D_0)=D_0^*\). Its determinant is the line bundle patched
by that unit. Triviality puts the unit in the image of
\(B_0^*\times C_0^*\), so its \(K_0\) boundary is zero.[^8]
No hypothesis \(SK_1(B_0)=0\) is needed.

Since \(R_0\) is a local complete intersection, its cotangent
complex is perfect of amplitude \([-1,0]\).[^9]
Its rank is two, and its determinant is the dualizing module,
which is trivial for this particular scaled gluing. Equation (25)
therefore gives
\[
[L_{R_0/\mathbb C}]=2[R_0]\quad\text{in }K_0(R_0).
\tag{26}
\]
This is the necessary class of a hypersurface in \(\mathbb A^3\).
It does not make the cotangent complex a particular free two-term
complex or supply three algebra generators.

For this surface, an embedding in \(\mathbb A^3\) is equivalent
to a triple \(g_1,g_2,g_3\in R_0\) generating \(R_0\) as a
complex algebra. Its height-one prime relation would then be
principal. Neither such a triple nor an obstruction to every
triple is constructed. Even that embedding would not yet provide
the additional ambient locally nilpotent derivation and quotient
compatibilities required by the original geometric route.

## 5. Verification and research boundary

The [exact execution record](verification-pass-21.json) accompanies
the [independent checker](research/primitive_bridge_checks_pass21.py)
and [regression runner](research/run_regression_pass21.py).
All 451 test methods across 34 suites passed in the complete execution
from September 13, 2026, 05:07:47 to 05:09:15 UTC.
The new suite has fourteen test methods. Its controls include
separate forward and inverse formulas, Jacobian-derived physical
derivations, nonconstant-invariant curve jets, inverse recomputation
of the invariant coefficient, exact residue matrices, and failed
lifting examples. It imports no project solver.

The finite matrices do not prove a rank classification or a
geometric realization. The all-parameter image and denominator
arguments are written proofs; the Picard and \(K_0\) conclusions
are source-dependent diagram arguments. Separate reconstructions
are recorded in the [audit summary](research/proof-audits-pass21.md).
Their agreement is not a substitute for a mathematician's review.

Reproduction from the project directory:

~~~sh
/opt/anaconda3/bin/python research/primitive_bridge_checks_pass21.py
/opt/anaconda3/bin/python research/run_regression_pass21.py
/opt/anaconda3/bin/python research/consistency_checks_pass21.py
~~~

The remaining universal obligations are now more specific.
An arbitrary slice action needs a justified nonlinear coordinate
frame, not just a polynomial subalgebra or an affine-linear
projection. The fixed-base coefficient shortcut is false.
Within the genuine invariant-extension reduction, transformed
full centers still need polynomial recognition; the prescribed
near-identity jet shortcut is also false.

These negative results eliminate invalid inference rules. They
do not establish that the weaker existential repairs fail.
No public novelty claim, submission, or external expert review
is justified by this report alone.

The narrower two-variable construction already has a definite
prior-work explanation. For \(p\mid q^2\) in a rational coefficient
domain, \(p\partial_r+(1+qr)\partial_t\) is divergence-free and
fixed-point-free, so Berson-van den Essen-Maubach supplies a slice
and polynomial kernel.[^10] With \(p=f^nh\), this covers the
stronger divisibility subfamily, not automatically the weaker
\(f^n\mid q^2\) condition used in Section 1. It also does not
identify the original rank-three physical overring with the
two-variable polynomial ring. The
[priority record](research/primitive-bridge-audit-pass21.md)
distinguishes that implication from the unresolved full-family comparison.
A [further comparison](research/priority-comparison-pass21.md) identifies
Freudenburg's 2009 sliced-derivation family as a concrete outstanding
lead. Its author's abstract treats a two-parameter polynomial base,
but supplies no example formulas.[^11] The full paper was not obtained
in this bounded comparison, so neither a collision nor a distinction
between its examples and this family is established.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, *On locally nilpotent derivations of polynomial algebra in three variables*, *Sbornik: Mathematics* 216(4) (2025), 456-484. [Published record](https://www.mathnet.ru/eng/sm10094); [author text, version 2](https://arxiv.org/html/2306.00510v2). Proposition 2.16, Corollary 3.18, Theorem 4.5(i), and Theorem 5.7, with the local-slice family immediately preceding it. The author's version predates publication.

[^2]: S. Kaliman and M. Zaidenberg, *Affine modifications and affine hypersurfaces with a very transitive automorphism group*, *Transformation Groups* 4 (1999), 53-95. [Primary text](https://arxiv.org/pdf/math/9801076), Proposition 2.1. Full ideal transport, not only reduced-support preservation, is the relevant hypothesis.

[^3]: S. M. Bhatwadekar, N. Gupta, and S. A. Lokhande, *Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*. [Primary author text](https://arxiv.org/html/1501.01438v1), Theorem 3.5 and proof. The invariant ambient coordinate is an assumption.

[^4]: G. Freudenburg, *Actions of SL2(k) on affine k-domains and fundamental pairs*. [Primary text](https://arxiv.org/pdf/2108.12021), Lemma 2.2. The coefficient in a locally nilpotent extension may be arbitrary in the base, not necessarily invariant.

[^5]: G. Freudenburg, *Canonical factorization of the quotient morphism for a Ga-action on an affine variety*, *Transformation Groups* 24 (2019). [Primary text](https://arxiv.org/pdf/1602.08786), Theorem 4.4 and Sections 8.2.1-8.2.3; [published DOI](https://doi.org/10.1007/s00031-018-9472-y). The displayed intermediate ring and its degree-resolution position are in Section 8.2.3.

[^6]: C. Weibel, *The K-book*, [Chapter I](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.I.pdf), Theorem 3.10 and proof, printed pp. 22-23. The Units-Pic sequence applies to the actual conductor square.

[^7]: Weibel, [Chapter II](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf), Theorem 8.2 and Example 8.2.2, printed pp. 76-77. Regularity is used for the normalization only.

[^8]: Weibel, [Chapter III](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf), Theorem 2.6 and proof, printed p. 15, and Example 1.3.5, printed p. 4. These are projective-module \(K\)-theory statements for a Milnor square and Euclidean polynomial rings.

[^9]: The Stacks Project, [Proposition 92.14.4](https://stacks.math.columbia.edu/tag/08SL), on the cotangent complex of a local complete intersection. The finite projective conormal module and the amplitude assertion are the inputs used.

[^10]: J. Berson, A. van den Essen, and S. Maubach, *Derivations having divergence zero on R[X,Y]*, Nijmegen Report 9918 (April 1999). [Primary author manuscript](https://www.math.ru.nl/~maubach/Papers/DerivHavingDivZero.pdf), property B(R) on printed p. 3 and Theorems 3.4 and 3.7 on printed pp. 4-5.

[^11]: G. Freudenburg, *Additive group actions associated to derivations of R[X,Y,Z] with a slice*, [author's CMS 2009 conference abstract](https://www2.cms.math.ca/Events/summer09/abs/pdf/aga-gf.pdf), one page. The related article is *Derivations of R[X,Y,Z] with a slice*, *Journal of Algebra* 322 (2009), 3078-3087, [DOI](https://doi.org/10.1016/j.jalgebra.2008.05.007). Only the abstract, not the article's full formulas, supports this scope comparison.
