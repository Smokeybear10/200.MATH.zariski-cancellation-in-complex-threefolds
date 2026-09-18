# An all-parameter resultant obstruction when sigma is affine

Working necessary result: under the complete actual264 moving-slope
hypotheses of441, if sigma is an affine intrinsic parameter, the
centered generator x cannot have intrinsic degree at least two.
In particular the degree profile (deg p,deg x,deg q)=(1,2,3)
is impossible BOTH at and away from f'''=6nu'.

The obstruction uses the original all-X polynomial-ring return and
the quadric relation. It does not require the finite degree bound,
the genuine fourth equation, or additional differential compatibility.
The proof includes repeated points. It is not an exclusion of the
remaining affine profile (1,1,1), an original-ring recognition, or a
solution of unrestricted cancellation.

## 1. A polynomial lemma with an exact resultant

Let K be a characteristic-zero field. Let x(V),z(V) belong to K[V],
with
\[
\deg x=n\ge2,\qquad \deg z=2n-1,\qquad
\operatorname{lc}(x)=a\ne0,\quad
\operatorname{lc}(z)=c\ne0.
\tag{1}
\]
For a scalar T over an extension field M/K, define
\[
f_T(V)=x(V)+TV,\qquad g(V)=z(V),\qquad
h_T(V)=2Vx(V)+TV^2.
\tag{2}
\]
Then there is an algebraic extension M/K and T in M such that
\[
M[f_T,g,h_T]\ne M[V].
\tag{3}
\]
It suffices to work in an algebraic closure of K. Define two
polynomials, before specializing either variable,
\[
F(U,V)=x(U)+x(V),\qquad
G(U,V)=\frac{z(U)-z(V)}{U-V}.
\tag{4}
\]
The second expression is the polynomial divided difference, including
its value z'(V) on U=V. Put m=2n-2. As polynomials in U, their
degrees are n,m and their leading coefficients are the nonzero
CONSTANTS a,c. Their top total-degree forms are
\[
F_n=a(U^n+V^n),\qquad
G_m=c\sum_{j=0}^{m}U^{m-j}V^j.
\tag{5}
\]
Let R(V)=Res_U(F,G). The following exact highest term is useful:
\[
\boxed{\deg_V R=nm,\qquad
\operatorname{lc}_V R=a^m c^n\ne0.}
\tag{6}
\]

Here is a direct verification, including the absence of cancellation.
Set U=VW, first with V invertible. The scaling identities for the
resultant give
\[
V^{-nm}R(V)=
\operatorname{Res}_W\bigl(V^{-n}F(VW,V),
                         V^{-m}G(VW,V)\bigr).
\tag{7}
\]
Both arguments on the right are polynomials in W and V^{-1}.
Consequently R has degree at most nm in V. Its coefficient at
degree nm is the right side evaluated at V^{-1}=0, namely
\[
\operatorname{Res}_W
\left(a(W^n+1),c\sum_{j=0}^{2n-2}W^j\right).
\tag{8}
\]
If w^n=-1, then w is nonzero and w is not one. Since w^{2n}=1,
\[
\sum_{j=0}^{2n-2}w^j
=\frac{w^{2n-1}-1}{w-1}=-\frac1w.
\]
The product of all n roots of W^n+1 is (-1)^n. The root-product
formula for (8) therefore gives a^m*c^n exactly, proving (6).
Equivalently, the top forms in (5) have no common projective
point at infinity; no generic-coefficient assumption was used.

Because nm>0, R has a root v in an algebraic closure. The leading
U-coefficients a,c remain nonzero at that value of V. Thus the
specialized resultant zero gives an actual finite u with
\[
x(u)+x(v)=0,\qquad G(u,v)=0.
\tag{9}
\]
There is no lost leading coefficient or root at infinity in this
specialization. The two elements u,v are algebraic over K.

If u and v are distinct, choose
\[
T=-\frac{x(u)-x(v)}{u-v}.
\tag{10}
\]
Then f_T(u)=f_T(v) and g(u)=g(v). The exact third divided difference is
\[
\frac{h_T(u)-h_T(v)}{u-v}
=x(u)+x(v)+(u+v)
 \left(\frac{x(u)-x(v)}{u-v}+T\right)=0.
\tag{11}
\]
So every polynomial in the three outputs has equal values at u,v,
whereas V does not. They cannot generate M[V].

If u=v, equations (9) instead give x(v)=0 and z'(v)=0.
Choose T=-x'(v). All three output derivatives vanish:
\[
f_T'(v)=0,\qquad g'(v)=0,\qquad
h_T'(v)=2x(v)+2v(x'(v)+T)=0.
\tag{12}
\]
Every polynomial in the outputs then has derivative zero there,
whereas V has derivative one. This again proves (3).
This diagonal argument is essential: no nonzero-discriminant
assumption can replace it.

## 2. The complete actual hypotheses and the relevant ring return

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
the actual polynomial ring B=C[X,Y,Z,W]=A[u], its global slice
E=partial_u, exact E-degrees (1,2,2,2), the ENTIRE weighted initial
kernel mathsf X^2*mathsf Z-mathsf Y^2, the literal selected nonzero
derivation N, coefficient localization, both original return statements
and the nonzero calibrated full scalar. As in
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md),
also assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F=\ker_L\partial_s,\qquad b=\nu'\ne0.
\tag{13}
\]
Here L is the exact selected-derivation coefficient field and
O=L[v]. The field L is finite over C(t,s), and F is finite over C(t).
Neither field is assumed rational. No resonance condition is added.

The intrinsic polynomial change in441 gives
\[
\begin{gathered}
x=y+\frac{(f''-2\nu)\sigma+n_t-\nu f'}2,\qquad
p=\sigma-E_0/b,\qquad q=\theta+T_2(\sigma),\\
E_0=\ell_s+\nu^2,\qquad \deg T_2\le2,\\
x^2+bpq=d,\qquad O=L[x,p,q],\qquad p\notin L.
\end{gathered}
\tag{14}
\]
All changes in (14) are only over L. They are not asserted to be
automorphisms of the original complex four-ring.

Use the exact centered function from
[439, Section4](principal-paraboloid-moving-slope-centered-collision-boundary-pass439-working.md):
\[
\zeta=\theta+\sigma^2+f'\sigma
     =q-T_2(\sigma)+\sigma^2+f'\sigma.
\tag{15}
\]
The original slice and the two-sided polynomial transformation of
the literal rows in439 establish the following identity, including
arbitrary scalar extensions and ALL parameter values:
\[
M[x+T\sigma,\ \zeta,\ 2\sigma x+T\sigma^2]=M[v]
\quad\text{for every field extension }M/L\text{ and }T\in M.
\tag{16}
\]
This is a whole-polynomial-ring statement, not just a function-field
identity or generation for generic T. The distinction licenses the
specialization used below.

## 3. Consequence when the original sigma is affine

Suppose deg_v sigma=1. Then V=sigma is an affine change of the
intrinsic parameter, and M[V]=M[v] after every field extension.
Write the evaluated x as a polynomial x(V).

Assume for a contradiction that its degree is n>=2. In (14),
p=V-E0/b is monic linear, and x^2-d has degree 2n. Hence
\[
\deg_V q=2n-1,\qquad
\operatorname{lc}_V q=-\frac{\operatorname{lc}_V(x)^2}{b}\ne0.
\tag{17}
\]
Equation (15) changes q only by a polynomial of degree at most two.
Since 2n-1>=3, it follows that
\[
\deg_V\zeta=2n-1,\qquad
\operatorname{lc}_V\zeta=-\frac{\operatorname{lc}_V(x)^2}{b}.
\tag{18}
\]
Apply Section1 with K=L and z=zeta. It supplies algebraic u,v,T
for which the three outputs fail to generate M[V], contrary to
(16). Therefore
\[
\boxed{\deg_v\sigma=1\quad\Longrightarrow\quad\deg_v x\le1,}
\tag{19}
\]
where the zero polynomial is included in the conclusion.
No degree upper bound on a hypothetical n was needed.

In the positive-degree frontier of441 and442, p and sigma have
the same degree. In particular (deg p,deg x,deg q)=(1,2,3)
is excluded in BOTH resonance and nonresonance. The result does
not by itself exclude the positive profile (1,1,1) or constant
x. The separate zero-q exclusion445 uses additional scalar and
original-ring arguments, not this resultant lemma.

## 4. Direct reconstruction for the excluded (1,2,3) profile

For a smaller explicit check, take
\[
x(V)=AV^2+BV+C,\quad
\zeta(V)=K_3V^3+K_2V^2+K_1V+K_0,
\quad A K_3\ne0.
\]
Write S=u+v and Pi=u*v. Conditions (9) become
\[
A(S^2-2\Pi)+BS+2C=0,\qquad
K_3(S^2-\Pi)+K_2S+K_1=0.
\tag{20}
\]
Eliminating Pi gives the genuine quadratic
\[
\frac{K_3}{2}S^2+
\left(K_2-\frac{K_3B}{2A}\right)S+
K_1-\frac{K_3C}{A}=0.
\tag{21}
\]
Choose one root S, set Pi=(S^2+(B/A)S+2C/A)/2, and take the
two roots of V^2-SV+Pi. They supply the distinct or repeated pair
already treated. This proof is exact over an algebraic closure;
it does not sample parameter values or assume simple roots.

## 5. Verification and scope

Root read the current264 and439 through EOF, and the complete441.
Fresh unsaved ebd32d checked the symmetric elimination (20),(21)
and the exact divided-difference identity (11), with zero residuals.
It separately verified (6) for several nonhomogeneous test
polynomials with n=2,...,6, and the homogeneous resultant for
n=2,...,8. Those finite checks only test the formulas; the
all-n statement is proved by (7),(8), not by enumeration.
An independent AI review reconstructed the scaling identity,
the exact leading coefficient, specialization with unchanged
U-degrees, and both collision endpoints before this draft.
The saved-source review and held hash belong in the ledger.

The coefficients may move in L, but this proof never differentiates
them: every polynomial computation fixes that field. No moving
parameter derivative has been dropped from a scalar calculation.
No finite projection is declared normal, and no coefficient-field
generator is promoted to an original complex coordinate.

No saved checker was executed, imported, compiled or rerun.
No unrestricted cancellation, arbitrary chart entry, actual model
existence, historical novelty, expert review or formal certification
is claimed.
