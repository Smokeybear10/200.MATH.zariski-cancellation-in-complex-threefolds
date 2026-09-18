# An all-parameter collision excludes the degree profile (2,4,6)

Working exclusion: in the complete actual264 moving-slope chart of441,
the intrinsic quadric profile (deg p,deg x,deg q)=(2,4,6) is impossible,
both at and away from the resonance f'''=6nu'. The proof uses the
quadric, whole-line generation, its gradient unit, and the actual
all-X polynomial-ring return. It does not use selected terms of the
fourth potential in place of that return.

Two exact normal forms remain after an odd-module argument. For each,
a symmetric-pair resultant has a root whose sum is NONZERO. This is
the necessary guard against pairs with the same quadratic p value.
Distinct and repeated points are both included. No remaining profile
is realized or recognized by this argument.

## 1. Complete actual input and the abstract obstruction

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
the original polynomial four-ring B=C[X,Y,Z,W]=A[u], its global slice
E=partial_u, exact time degrees(1,2,2,2), the ENTIRE weighted initial
kernel mathsf X^2*mathsf Z-mathsf Y^2, the literal selected nonzero
derivation N, exact coefficient localization, both original returns,
and the nonzero calibrated full scalar. Assume the moving-slope
hypotheses of
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md):
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F=\ker_L\partial_s,\qquad b=\nu'\ne0.
\tag{1}
\]
Here L is finite over C(t,s), and F is finite over C(t). Neither is
assumed rational. No resonance condition is imposed.

The exact polynomial intrinsic change of441 gives
\[
\begin{gathered}
O=L[v]=L[x,p,q],\qquad x^2+bpq=d\in L,\\
p=\sigma-E_0/b,\qquad E_0=\ell_s+\nu^2,\qquad
q=\theta+T_2(\sigma),\qquad \deg T_2\le2,\\
x=y+\{(f''-2\nu)\sigma+n_t-\nu f'\}/2.
\end{gathered}
\tag{2}
\]
The evaluated quadric gradient generates a unit ideal in O, because
its minors with the genuine fourth gradient do. In particular
\[
(2x,bq,bp)\,O=O.
\tag{3}
\]

The complete row transformation in
[439, Section4](principal-paraboloid-moving-slope-centered-collision-boundary-pass439-working.md)
uses
\[
\zeta=\theta+\sigma^2+f'\sigma
      =q-T_2(\sigma)+\sigma^2+f'\sigma.
\]
It gives whole polynomial-ring generation for EVERY scalar extension
and EVERY parameter value, not merely a generic field equality.
Translating sigma=p+E0/b changes its third generator by twice E0/b
times the first and a constant. Thus the same return is
\[
M[x+Tp,\ \zeta,\ 2px+Tp^2]=M[v]
\quad\text{for every field extension }M/L,\ T\in M.
\tag{4}
\]
This license comes from the original slice: L[B]=O[X], since
X=a0*u+x0 with a0 in L* and x0 in A, followed by439's two-sided
L[X]-polynomial row transformation and specialization. It is not
an assertion that the intrinsic changes are ambient complex
coordinate changes.

We prove that (2)--(4) cannot hold when
\[
\deg_vp=2,\qquad \deg_vx=4,\qquad \deg_vq=6.
\tag{5}
\]
Only the first two degrees are needed after the quadric is imposed.
By the formula for zeta, it differs from q by a polynomial in p
of degree at most two.

## 2. Centering p and exhausting the polynomial remainder

Translate v over L to remove the linear term of the quadratic p.
Write the old p as alpha*(v^2+c), with alpha in L*. Replace p by
p/alpha and b by alpha*b. The quadric is unchanged in form.
Equation(4) is unchanged after replacing T by alpha*T and dividing
its third generator by alpha. The quadratic correction in zeta
remains arbitrary. After these operations, reuse the symbols:
\[
p=v^2+c,\qquad
\zeta=q-d_2p^2-d_1p-d_0,\qquad c,d_2,d_1,d_0\in L.
\tag{6}
\]
No square root or extension of L was needed for this normalization.
The coefficient d2 is allowed to vanish; in particular no step
excludes the resonance by assuming d2 nonzero.

Divide x by the monic p and write the full quotient and remainder:
\[
x=p(Ap+D+Bv)+rv+h,\qquad A\in L^*,\quad B,D,r,h\in L.
\tag{7}
\]
Here h is a remainder coefficient, not the third-potential level.
Polynomiality of q=(d-x^2)/(bp) forces
\[
rh=0,\qquad d=h^2-cr^2,\qquad
q=-\frac{p(Ap+D+Bv)^2+2(Ap+D+Bv)(rv+h)+r^2}{b}.
\tag{8}
\]
These identities include all remainder constants.

If r=h=0, then x,p,q are all multiples of the nonconstant p.
Their evaluated quadric gradient in(3) is contained in the proper
ideal (p), a contradiction. Thus exactly one of r,h is nonzero.

Suppose h=0 and r is nonzero. The even parts of x and q belong
to L[p], while their odd parts are respectively
v*(Bp+r) and -2*(Ap+D)*v*(Bp+r)/b. Consequently
\[
L[p,x,q]=L[p,v(Bp+r)]
=L[p]\mathbin{\oplus}v(Bp+r)L[p].
\tag{9}
\]
The square of the odd generator is in L[p] because v^2=p-c.
Whole generation L[p,x,q]=L[v] forces Bp+r to be a unit of L[p]:
compare the odd component of an expression for v. Hence B=0.

Suppose instead r=0 and h is nonzero. If B=0, all three generators
would belong to the proper subring L[v^2], contradicting whole
generation. Therefore B is nonzero.

The two exhaustive necessary forms are thus
\[
\begin{array}{ll}
\mathrm{I}:&
x=p(Ap+D)+rv,\quad
q=-\{p(Ap+D)^2+2rv(Ap+D)+r^2\}/b,\quad Ar\ne0;\\[1mm]
\mathrm{II}:&
x=p(Ap+D+Bv)+h,\quad
q=-\{p(Ap+D+Bv)^2+2h(Ap+D+Bv)\}/b,\quad ABh\ne0.
\end{array}
\tag{10}
\]
They remain coefficient-field descriptions, not proposed actual
models. In both, zeta has the arbitrary correction in(6).

## 3. Exact symmetric equations, with all lower coefficients retained

For a potential pair u,v, use the independent symmetric symbols
\[
S=u+v,\qquad z=p(u)+p(v),\qquad
\Pi=uv=\frac{S^2+2c-z}{2}.
\]
Then
\[
\mathcal P=p(u)p(v)=\frac{(S^2-z)^2}{4}+cS^2.
\tag{11}
\]
The symbol z here is a symmetric variable, NOT the original
intercept z of264. Define polynomials in L[S,z] by
\[
\mathcal F=x(u)+x(v),\qquad
\mathcal G=-b\,\frac{\zeta(u)-\zeta(v)}{u-v}.
\tag{12}
\]
The divided difference means its polynomial value, including the
derivative on the diagonal. Put j=b*d2 and k=b*d1. The unused
constant d0 cancels from the divided difference, not from zeta.

For Type I, direct substitution of(10) gives the ENTIRE polynomials
\[
\begin{aligned}
\mathcal F_{\rm I}
 &=A(z^2-2\mathcal P)+Dz+rS,\\
\mathcal G_{\rm I}
 &=S\{A^2(z^2-\mathcal P)+(2AD+j)z+D^2+k\}\\
 &\hspace{8mm}+r\{A(S^2+z)+2D\}.
\end{aligned}
\tag{13}
\]
For Type II, define the polynomial divided difference of v*p(v)^2:
\[
\mathcal V_5
=\frac{-S^4-4cS^2+4S^2z+z^2}{4}.
\]
The complete pair is
\[
\begin{aligned}
\mathcal F_{\rm II}
 &=A(z^2-2\mathcal P)+Dz+2h
      +\frac{BS}{2}(-S^2+3z-4c),\\
\mathcal G_{\rm II}
 &=S\{A^2(z^2-\mathcal P)+(2AD+B^2+j)z
                 +D^2-B^2c+2hA+k\}\\
 &\hspace{8mm}+2B\{A\mathcal V_5+D(S^2+z)/2+h\}.
\end{aligned}
\tag{14}
\]
In both cases the coefficient of z^2 in F is the nonzero CONSTANT
A/2. This fact will protect finite specialization even if the
z-degree of G falls at a particular value of S.

## 4. Two exact high coefficients of the resultant

Let
\[
\mathcal R(S)=\operatorname{Res}_z(\mathcal F,\mathcal G).
\]
We will prove, without a numerical parameter choice,
\[
\begin{array}{lll}
\mathrm{I}:&
[S^{10}]\mathcal R=A^6/16,&[S^7]\mathcal R=3A^5r/8\ne0;\\
\mathrm{II}:&
[S^{10}]\mathcal R=A^6/16,&[S^9]\mathcal R=3A^5B/8\ne0.
\end{array}
\tag{15}
\]
In particular both resultants have degree exactly ten and are not
monomials in S.

Here is a small exact computation establishing these coefficients.
Set z=S^2Z with S invertible, and put epsilon=1/S. Both polynomials
have z-degree two over L(S), so the resultant scaling identity gives
\[
S^{-10}\mathcal R(S)
=\operatorname{Res}_Z
 \bigl(S^{-4}\mathcal F(S,S^2Z),
       S^{-5}\mathcal G(S,S^2Z)\bigr).
\tag{16}
\]
Both entries on the right are polynomials in epsilon and Z. Their
constant terms are the same in the two types:
\[
f_0=\frac A2(Z^2+2Z-1),\qquad
g_0=\frac{A^2}{4}(3Z^2+2Z-1).
\tag{17}
\]

For transparency, the quadratic resultant used here is
\[
\begin{aligned}
&\operatorname{Res}_Z(a_2Z^2+a_1Z+a_0,\ b_2Z^2+b_1Z+b_0)\\
&\qquad=(a_2b_0-a_0b_2)^2
       -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
\end{aligned}
\tag{18}
\]
This is the determinant of the quadratic Sylvester matrix. It is
a polynomial identity, including when a leading coefficient
specializes to zero.

For Type I the two arguments in(16) are exactly
\[
\begin{aligned}
f_0&+\epsilon^2(DZ-2Ac)+\epsilon^3r,\\
g_0&+\epsilon^2\{-A^2c+(2AD+j)Z\}
 +\epsilon^3rA(1+Z)+\epsilon^4(D^2+k)+2rD\epsilon^5.
\end{aligned}
\tag{19}
\]
There is no epsilon term, so the coefficient of epsilon^3 in the
resultant depends only on the two displayed epsilon^3 perturbations.
Using(18) with a formal perturbation parameter t gives
\[
\begin{aligned}
\operatorname{Res}_Z(f_0,g_0)&=A^6/16,\\
[t]\operatorname{Res}_Z(f_0+tr,\ g_0+trA(1+Z))&=3A^5r/8.
\end{aligned}
\tag{20}
\]
There can be no contribution of order three made from order-two
terms when no order-one term is present.

For Type II it is enough to retain the constant and linear terms
in epsilon. They are
\[
f_0+\epsilon\,\frac B2(-1+3Z)+O(\epsilon^2),\qquad
g_0+\epsilon\,\frac{AB}{2}(-1+4Z+Z^2)+O(\epsilon^2).
\tag{21}
\]
Equation(18) gives
\[
[t]\operatorname{Res}_Z
 \left(f_0+t\,\frac B2(-1+3Z),
       g_0+t\,\frac{AB}{2}(-1+4Z+Z^2)\right)
=3A^5B/8.
\tag{22}
\]
Equations(16),(20),(22) prove all of(15). These formal perturbation
coefficients are not derivatives in the exact coefficient field.
No assumption about moving coefficient derivatives is made.

## 5. A nonzero pair sum and the two collision endpoints

Work now over an algebraic closure M of L. If every root of R were
zero, its nonzero degree-ten leading coefficient would make it a
constant multiple of S^10. The nonzero S^7 or S^9 coefficient in
(15) rules that out. Therefore there is a root
\[
S_0\in M^*,\qquad \mathcal R(S_0)=0.
\tag{23}
\]
At this value, F remains quadratic in z with leading coefficient
A/2. Consequently the resultant zero gives a finite z0 in M
with F(S0,z0)=G(S0,z0)=0. This remains true if G drops degree
or becomes zero: the root-product formula using the two finite
roots of F still applies, since its leading coefficient is a unit.
No unchanged-degree assumption for G is being used.

Set Pi0=(S0^2+2c-z0)/2, and take the two roots u,v of
V^2-S0*V+Pi0. Then p(u)+p(v)=z0 and the exact identities
(11)--(14) give
\[
x(u)+x(v)=0,\qquad
\frac{\zeta(u)-\zeta(v)}{u-v}=0.
\tag{24}
\]
The second equation again means polynomial divided difference.

If u and v are distinct, then
p(u)-p(v)=(u-v)S0 is nonzero. Choose
\[
T=-\frac{x(u)-x(v)}{p(u)-p(v)}.
\tag{25}
\]
The first and second generators in(4) take equal values at u,v.
The third divided difference, with denominator u-v, is
\[
S_0\{x(u)+x(v)\}
 +z_0\left\{\frac{x(u)-x(v)}{u-v}+TS_0\right\}=0.
\tag{26}
\]
Thus all three generators have the same values at two distinct
points and cannot generate M[v].

If the pair is repeated, write u=v=w. Then S0=2w is nonzero,
so p'(w)=2w is nonzero. Equations(24) give x(w)=0 and zeta'(w)=0.
Choose T=-x'(w)/p'(w). The derivatives of the first two generators
in(4) vanish, and the third derivative is
\[
2p'(w)x(w)+2p(w)\{x'(w)+Tp'(w)\}=0.
\tag{27}
\]
Every polynomial in the outputs has derivative zero at w, whereas
the intrinsic variable has derivative one. Whole generation fails
in this case as well.

Both endpoints contradict the exact all-parameter return(4).
The nonzero S0 construction is indispensable: the excluded pairs
with p(u)=p(v), and the diagonal at p'=0, were never used.

## 6. Consequence and verification boundary

All alternatives from the exact polynomial division(7),(8) have
been exhausted. It follows that, under the full supplied actual
chart and(1),
\[
\boxed{(\deg_vp,\deg_vx,\deg_vq)\ne(2,4,6).}
\tag{28}
\]
This removes the named profile in both441's nonresonant and442's
resonant necessary lists. It does not require d2 nonzero, a
nonzero centered level d, a rational coefficient field, or a
classification of all abstract polynomial embeddings of the line.

The actual input is precisely439's all-parameter polynomial return
and441's quadric, whole generation, and unit evaluated gradient.
Those sources were read completely in this review sequence. The
resultant proof here is distinct from the affine-sigma argument446:
the quadratic sigma requires the explicit nonzero-sum guard in(23).
No original complex coordinate is changed in this proof, and no
field equality is substituted for polynomial-ring generation.

Fresh unsaved054470 and477be6 expanded the complete resultants
with all displayed coefficient symbols arbitrary. Independent
unsaved9cec6c rebuilt both complete sum/divided-difference pairs
from(10) and(6), and checked(17),(20),(22), all with zero residuals
for the identities. The proof of the high coefficients is the
written quadratic determinant formula, not numerical sampling.
The writing guide was read fully before authoring.

No saved checker was executed, imported, compiled or rerun. No
earlier proof source or canonical ledger was edited. No remaining
profile is realized or recognized, and no unrestricted cancellation,
historical novelty, expert review or formal certification is claimed.
