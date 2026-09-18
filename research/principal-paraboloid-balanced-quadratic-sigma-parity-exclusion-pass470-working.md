# The balanced quadratic-sigma profile is excluded by parity

Working scoped exclusion: retain EVERY actual hypothesis of264,
and assume
\[
k=s+f,\qquad f_s=0,\qquad e=n_{ss}\ne0,\qquad f'''\ne0.
\tag{1}
\]
Then the balanced intrinsic profile
\[
\boxed{\deg\sigma=2,\qquad \deg y=\deg\theta=3}
\tag{2}
\]
cannot occur. The proof uses the complete centered third and fourth
relations of460, whole polynomial-line generation, and the primitive
tangent minor. It requires no strict-branch result from465--467
and no rationality assumption on the exact coefficient field.

## 1. Full actual input and the entire centered relations

Retain the globally sliced original polynomial ring
\(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\), the exact E-degrees
\((1,2,2,2)\), and the ENTIRE weighted initial kernel
\(\mathsf X^2\mathsf Z-\mathsf Y^2\) from
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
The literal selected nonzero N, exact coefficient field L,
original localization, both ring and fraction-field returns,
and full calibrated scalar remain required.
The original slice satisfies \(X=a_0u+x_0\), \(x_0\in A\);
it is not replaced by \(X/a_0\).

Use the complete arbitrary-n reduction
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md)
and the centered support and tangent-minor result
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md).
Their exact coefficient partials commute and have joint constants
\(\mathbb C\). No assertion \(L=\mathbb C(t,s)\), or
\(\ker_L\partial_s=\mathbb C(t)\), is made.

In460's notation, set
\[
\begin{gathered}
\nu=n_s,\qquad b=n_{ts},\qquad C_0=\ell_s+\nu^2,\qquad P=\sigma,\\
x=y+\frac{(f''-2\nu)P+n_t-\nu f'}2,\qquad
q=\theta+\frac{bP-C_0}{e}.
\end{gathered}
\tag{3}
\]
This is invertible affine centering over L, not an actual complex
ambient coordinate map. Under(2),460 gives
\[
O=L[v_0]=L[x,P,q],\qquad
\deg_{v_0}P=2,\quad \deg_{v_0}x=\deg_{v_0}q=3,\qquad e_s=0.
\tag{4}
\]
The corrections in(3) have intrinsic degree at most two, so they
do not change the cubic degrees of y and theta.

The ENTIRE third and fourth levels are
\[
\mathcal H=x^2+\frac e2q^2+T(P)=0,\qquad
\deg_PT=3,\qquad [P^3]T=f'''/6\ne0,
\tag{5}
\]
\[
\Phi=x\{T'(P)+D(P)q\}+K_0(P)+J_2(P)q+E_1(P)q^2=0,
\tag{6}
\]
where
\[
\begin{gathered}
D(P)=d_0-2eP,\qquad d_0=b-ef',\\
E_1(P)=\frac{e_t}{2}P+c_0,\qquad
c_0=-\frac{ef''}{4}-e\nu-\frac{\ell_{ss}}2,\\
\deg J_2\le2,\qquad
K_0(P)=\frac{f''''}{24}P^4+K_3(P),\quad \deg K_3\le3.
\end{gathered}
\tag{7}
\]
The prime on T is the formal P-derivative. All coefficients and
levels are the exact ones in460(8)--(12). In particular no lower
term of K0, J2, or T is omitted. They are not new freely chosen
relations replacing the genuine fourth potential.

The evaluated gradient minors of \(\mathcal H,\Phi\) generate O.
Whole generation differentiates to a polynomial combination of
\((x_{v_0},P_{v_0},q_{v_0})\) equal to one. The primitive tangent
argument of460 therefore supplies \(\psi\in L^*\) such that
\[
\begin{aligned}
W&:=\mathcal H_x\Phi_q-\mathcal H_q\Phi_x\\
 &=2Dx^2-eDq^2+2xJ_2+4E_1xq-eqT'
 =-\psi P_{v_0}.
\end{aligned}
\tag{8}
\]
The sign is minus the middle component in formal order \((x,P,q)\).
This uses the genuine unit ideal, not just generic independence
of the two gradients. The intrinsic derivative fixes L.

## 2. Affine parameter normalization and the common-root boundary

Extend L to an algebraic closure M. All polynomial identities,
whole generation, and the minor-unit condition extend to
\(M[v_0]\). An affine parameter change
\(v=\alpha_0v_0+\beta_0\), \(\alpha_0\in M^*\), makes
\[
P=v^2+p_0,\qquad p_0\in M.
\tag{9}
\]
This is only an intrinsic scalar extension and parameter change.
It does not normalize a coefficient-field derivative, the original
slice, or an actual ambient coordinate.

The chain rule in(8) gives
\[
W=-\widetilde\psi P_v=-2\widetilde\psi v,\qquad
\widetilde\psi=\alpha_0\psi\in M^*.
\tag{10}
\]
Thus the even part of W is zero. No assumption \(Nv=1\) is made
for this new affine parameter.

The degree-three polynomials x and q have unique decompositions
\[
x=X_{\rm e}(P)+vF(P),\qquad
q=Q_{\rm e}(P)+vG(P),
\tag{11}
\]
where
\[
\deg X_{\rm e},\deg Q_{\rm e}\le1,\qquad
\deg F=\deg G=1.
\tag{12}
\]
Here zero even parts are allowed. The exact degree-one assertions
for F and G follow from the nonzero cubic leaders of x and q.

We claim \(\gcd(F,G)=1\) in \(M[P]\). Otherwise the two linear
polynomials have a common root \(r\in M\).
If \(r\ne p_0\), choose \(v_\pm=\pm\sqrt{r-p_0}\). They are
distinct. At these two points P has the same value r, while
\[
x(v_\pm)=X_{\rm e}(r),\qquad q(v_\pm)=Q_{\rm e}(r).
\]
This contradicts \(M[x,P,q]=M[v]\): a polynomial expression for v
in the three generators would have equal values at distinct points.

If \(r=p_0\), the pair has coalesced at \(v=0\).
Direct differentiation of(9),(11) gives
\[
P_v(0)=0,\qquad x_v(0)=F(p_0)=0,\qquad
q_v(0)=G(p_0)=0.
\]
Differentiating a polynomial expression for v in x,P,q would
give \(1=0\) there. Hence this boundary is impossible as well.
This proves
\[
\boxed{\gcd(F,G)=1.}
\tag{13}
\]
Both the distinct-point and derivative-zero arguments use whole
polynomial-ring generation, not just equality of fraction fields.

## 3. The entire third relation determines both even parts

The decomposition \(M[v]=M[P]\oplus vM[P]\), with
\(v^2=P-p_0\), separates the odd part of(5):
\[
X_{\rm e}F+\frac e2Q_{\rm e}G=0.
\tag{14}
\]
Because F and G are coprime, G divides \(X_{\rm e}\).
The degree bound in(12) gives a coefficient \(\tau\in M\) with
\[
X_{\rm e}=\tau G,\qquad
Q_{\rm e}=-\frac{2\tau}{e}F.
\tag{15}
\]
The value \(\tau=0\) is included. In deriving the second equality,
one cancels the nonzero polynomial G in a domain; it is not
declared a unit. The only coefficient division is by \(e\ne0\).
There is no claim that tau is complex or defines a time translation.

Thus the complete parametrization at this stage is
\[
x=\tau G+vF,\qquad
q=-\frac{2\tau}{e}F+vG.
\tag{16}
\]
Its even third relation gives, without a root or square-free
assumption on T,
\[
T(P)=-
\left(P-p_0+\frac{2\tau^2}{e}\right)
\left(F(P)^2+\frac e2G(P)^2\right).
\tag{17}
\]
The inherited exact cubic degree of T remains imposed.
The contradiction below does not divide either factor of(17).

## 4. Full odd fourth relation and full even minor

Let
\[
\mathcal E(P)=
F T'+\tau D\left(G^2-\frac{2F^2}{e}\right)
       +J_2G-\frac{4\tau E_1}{e}FG.
\tag{18}
\]
Substitution of(16) into the ENTIRE relation(6) gives
\[
\Phi_{\rm odd}=v\,\mathcal E(P).
\tag{19}
\]
Indeed the odd part of xq is
\(\tau v(G^2-2F^2/e)\), and the odd part of q squared is
\(-4\tau vFG/e\). The whole K0 is even. Since \(\Phi=0\)
and the ring is a domain, the polynomial injection
\(M[P]\hookrightarrow M[v]\) gives
\[
\mathcal E(P)=0.
\tag{20}
\]
This is cancellation in a polynomial identity, not inversion of v.

For clarity, the even part of the COMPLETE minor(8) is
\[
\begin{aligned}
W_{\rm even}={}&
2D\{\tau^2G^2+(P-p_0)F^2\}\\
&-eD\{4\tau^2F^2/e^2+(P-p_0)G^2\}
       +2\tau GJ_2\\
&+4E_1\{-2\tau^2FG/e+(P-p_0)FG\}
       +2\tau F T'.
\end{aligned}
\tag{21}
\]
Subtracting \(2\tau\mathcal E\) yields the exact identity
\[
\boxed{
W_{\rm even}-2\tau\mathcal E
=(P-p_0)\{D(2F^2-eG^2)+4E_1FG\}.}
\tag{22}
\]
No leading-degree truncation is used in(18)--(22).

By(10),(20), the left side of(22) is zero.
The polynomial \(P-p_0\) is nonzero, including when \(p_0=0\).
Consequently
\[
D(P)\{2F(P)^2-eG(P)^2\}+4E_1(P)F(P)G(P)=0
\tag{23}
\]
identically in \(M[P]\).

Let \(r_F,r_G\) be the respective roots of F and G.
Both exist, and they are distinct by their exact linear degrees
and(13). Evaluation of(23) gives
\[
-eD(r_F)G(r_F)^2=0,\qquad
2D(r_G)F(r_G)^2=0.
\tag{24}
\]
The omitted factors are nonzero: \(e\ne0\),
\(G(r_F)\ne0\), and \(F(r_G)\ne0\).
Thus D vanishes at two distinct points.
But \(D=d_0-2eP\) is a degree-one polynomial with nonzero slope.
This is impossible, proving(2).

## 5. Boundaries and verification scope

The argument includes \(\tau=0\), either zero even part in(11),
all zero lower coefficients in the genuine levels, and \(p_0=0\).
A common root of F and G at \(p_0\) is explicitly handled by
the derivative-zero argument, not silently discarded as a repeated
pair. The polynomial T may have repeated roots. No factor of T,
no F or G, and no evaluated nonconstant polynomial is inverted
in the polynomial ring.

The full held460 was freshly reread through116cbe+c866b8 at SHA
1f501703fd4da19b986d13bcb14d492d959459e62135a071b0a564f0efc16878.
The writing guide was completely reread through c866b8+51e873.
Fresh unsaved981cc1 independently reconstructed the full third
relation(17), the whole odd fourth identity(19), the complete
even-minor identity(22), and both evaluations(24), with every
lower coefficient free. Every residual was zero.
Root's separate fresh c30edd reconstruction also checked the
complete identities. The written whole-ring and coprimality
arguments, not those coefficient controls, handle the common-root
and derivative boundaries.

This proof requires only the indicated full460 consequences of
the actual264/296/458 chart. It does not depend on465,466,467,
an all-parameter collision lemma, the strict Riccati integration,
or a finite degree enumeration. Earlier recognition dependencies
are not recursively re-certified here.

Only the balanced profile(2) is excluded. No higher balanced
profile, actual realization, original coordinate recovery, or
general cancellation statement follows from this note alone.
No saved checker was executed, imported, compiled, or rerun.
No earlier source or canonical index was edited, and no historical
novelty, external expert review, or formal certification is claimed.
