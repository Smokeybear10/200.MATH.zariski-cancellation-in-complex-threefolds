# A linear-resultant collision excludes the resonant profile (2,3,4)

Working exclusion: in the entire actual264 moving-slope chart,
the resonant profile (deg p,deg x,deg q)=(2,3,4) cannot occur.
An exact polynomial remainder and whole-line generation force one
normal form. Two symmetric collision equations then have a linear
resultant with a nonzero root. Both distinct and repeated points
contradict the original all-parameter polynomial-ring return.

Resonance is essential to this argument: it removes the quadratic
correction between zeta and q. The corresponding nonresonant
profile is NOT excluded here. No remaining profile is recognized
and no original complex coordinate is constructed.

## 1. Entire actual hypotheses and the resonance consequence

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including the original globally sliced polynomial four-ring
B=C[X,Y,Z,W]=A[u], exact E-degrees (1,2,2,2), the ENTIRE
weighted initial kernel mathsf X^2*mathsf Z-mathsf Y^2, the
literal selected derivation N, both actual return statements,
the exact coefficient localization and the nonzero calibrated
scalar. As in
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md),
assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F=\ker_L\partial_s,\qquad b=\nu'\ne0.
\tag{1}
\]
Here L is the exact finite extension of C(t,s), and F is finite
over C(t); neither is assumed rational. Add the resonance
\[
f'''=6b.
\tag{2}
\]

The quadric transformation of441 and the actual return of
[439, Section4](principal-paraboloid-moving-slope-centered-collision-boundary-pass439-working.md)
give
\[
\begin{gathered}
L[v]=L[x,p,q],\qquad x^2+bpq=d\in L,\qquad
(2x,bp,bq)L[v]=L[v],\\
M[x+Tp,\ \zeta,\ 2px+Tp^2]=M[v]
\quad\text{for every field extension }M/L\text{ and every }T\in M.
\end{gathered}
\tag{3}
\]
The gradient unit follows from the genuine two-gradient minor unit,
not an assumed smoothness of a two-coordinate projection. For the
last line, translating sigma=p+E0/b changes439's first and third
generators only by constants and a multiple of the first generator.
The all-T identity is a whole-ring return from the original slice,
not a generic function-field equality.

In441's notation, q=theta+T2(sigma), where the P^2 coefficient
of T2 is f'''/(6b). Therefore (2) makes T2 monic quadratic.
The centered zeta=theta+sigma^2+f'*sigma consequently satisfies
\[
\zeta=q-d_1p-d_0,\qquad d_1,d_0\in L.
\tag{4}
\]
There is NO quadratic p correction in (4). This is the exact
place where the resonance will be used.

Suppose for a contradiction that
\[
(\deg_vp,\deg_vx,\deg_vq)=(2,3,4).
\tag{5}
\]
Translate the intrinsic parameter to center the quadratic p, and
divide p by its nonzero leading coefficient. Absorb that scalar
in b and reparameterize T in (3). Dividing the third output by
the same scalar retains the all-T return, and (4) remains affine
in p. We may thus reuse notation with
\[
p=v^2+c,\qquad c\in L.
\tag{6}
\]
These are changes over L, not original complex coordinate changes.

## 2. Polynomial division and whole generation force one form

Write the entire quotient and remainder when dividing x by p:
\[
x=p(Av+B)+rv+h,\qquad A\in L^*,\quad B,r,h\in L.
\tag{7}
\]
Here h is a remainder coefficient, not the third-potential level.
Polynomiality of q=(d-x^2)/(bp) gives
\[
rh=0,\qquad d=h^2-cr^2,\qquad
q=-\{p(Av+B)^2+2(Av+B)(rv+h)+r^2\}/b.
\tag{8}
\]
If r=h=0, all three functions x,p,q are multiples of the
nonconstant p. This contradicts the gradient unit in (3).

If h=0 and r is nonzero, the even parts of x,q belong to L[p].
Their odd parts are respectively v(Ap+r) and -2Bv(Ap+r)/b.
The square of the odd generator belongs to L[p], so
\[
L[p,x,q]=L[p]\mathbin{\oplus}v(Ap+r)L[p].
\tag{9}
\]
Because A is nonzero, Ap+r is a nonunit of L[p]. Comparing
odd components shows that (9) cannot contain v, contrary to
the whole generation in (3).

The sole remaining possibility has r=0 and h nonzero. Thus
\[
\boxed{
x=p(Av+B)+h,\qquad
q=-\{p(Av+B)^2+2h(Av+B)\}/b,\qquad Ah\ne0.}
\tag{10}
\]
The coefficient B and the centered quadratic constant c may vanish.
No further assumption on either is introduced.

## 3. The two complete symmetric equations

For a pair u,v introduce independent symmetric symbols
\[
S=u+v,\qquad z=p(u)+p(v),\qquad
\Pi=uv=(S^2+2c-z)/2.
\tag{11}
\]
The z in this section is NOT the original intercept z of264.
Set k=b*d1. From (4),(10) one obtains the complete polynomials
\[
\begin{aligned}
\mathcal F(S,z)&=x(u)+x(v)
 =(3AS/2+B)z-AS^3/2-2AcS+2h,\\
\mathcal G(S,z)&=-b\,\frac{\zeta(u)-\zeta(v)}{u-v}\\
 &=(A^2S+AB)z+ABS^2+(B^2-A^2c+k)S+2Ah.
\end{aligned}
\tag{12}
\]
The divided difference is a polynomial before specializing u,v,
and equals zeta'(v) on the diagonal. The constant d0 drops
out of this difference, not out of the original zeta.
The formulas use
u*p(u)+v*p(v)=S(-S^2+3z-4c)/2 and
(u*p(u)-v*p(v))/(u-v)=(S^2+z)/2.

Both polynomials are linear in z. The exact linear resultant is
\[
\begin{aligned}
\mathcal R(S)&=\operatorname{Res}_z(\mathcal F,\mathcal G)\\
 &=\frac{A^3}{2}S^4+2A^2BS^3
  +\frac A2(5B^2+A^2c+3k)S^2\\
 &\hspace{9mm}+(A^2h+B^3+A^2Bc+Bk)S.
\end{aligned}
\tag{13}
\]
This is the determinant F_z*G_const-F_const*G_z, so it remains
a polynomial identity at any specialization where a z degree drops.

The degree-four coefficient is nonzero. Moreover R cannot be a
constant multiple of S^4. Such a monomial would first force B=0
from the S^3 coefficient, then k=-A^2*c/3 from the S^2 coefficient.
Its S coefficient would then be A^2*h, which is nonzero.
Over an algebraic closure M of L, R therefore has a NONZERO root
\[
S_0\in M^*,\qquad \mathcal R(S_0)=0.
\tag{14}
\]

There is no lost finite solution at this root. The two z-leading
coefficients in (12) cannot vanish together when S is nonzero:
3AS/2+B=0 and A^2S+AB=0 would imply AS/2=0.
Thus at least one equation remains genuinely linear in z. Its
unique root satisfies the other equation by the determinant zero.
This supplies z0 in M with
\[
\mathcal F(S_0,z_0)=\mathcal G(S_0,z_0)=0.
\tag{15}
\]
This argument allows B=0 and degree-drop in either equation.

## 4. Distinct and diagonal collisions both contradict the return

Put Pi0=(S0^2+2c-z0)/2 and take the roots u,v of
V^2-S0*V+Pi0. The complete identities (11),(12) give
\[
x(u)+x(v)=0,\qquad
\frac{\zeta(u)-\zeta(v)}{u-v}=0.
\tag{16}
\]
If the roots are distinct, then p(u)-p(v)=(u-v)S0 is nonzero.
Choose T=-(x(u)-x(v))/(p(u)-p(v)). The first two outputs in
(3) have equal values at u,v. The third divided difference is
\[
S_0\{x(u)+x(v)\}
 +z_0\left\{\frac{x(u)-x(v)}{u-v}+TS_0\right\}=0.
\tag{17}
\]
Hence every polynomial in the outputs has equal values there,
whereas the intrinsic variable does not. They cannot generate M[v].

If the roots coincide at w, then p'(w)=2w=S0 is nonzero.
Equations (16) give x(w)=0 and zeta'(w)=0. Choose
T=-x'(w)/p'(w). All three output derivatives then vanish;
the third derivative is
\[
2p'(w)x(w)+2p(w)\{x'(w)+Tp'(w)\}=0.
\tag{18}
\]
Every polynomial in the outputs has derivative zero at w,
whereas v has derivative one. This also contradicts (3).
The nonzero-S construction is essential to both divisions.

Thus the resonant profile (5) is impossible. This proof does not
discard pairs with equal p values: it constructs a forbidden pair
outside that exceptional set, with the diagonal treated separately.

## 5. Scope and verification

The proof retains the whole original ring return of439, the quadric
and gradient unit of441, and the exact monic T2 consequence of442's
resonance. It does not promote a coefficient-field change to an
ambient complex automorphism or replace polynomial generation
by equality of fraction fields.

Root read current264,439 and441 completely in this workstream,
and the stated resonance transformation and coefficients in442.
Fresh unsaved eb7c9a independently reconstructed both entire
polynomials in (12) directly from (10),(4), and the full resultant
(13), with zero residuals. The final monomial test returned the
nonzero expression A^2*h. These are exact symbolic identities,
not numerical evidence for existence of a forbidden pair.
The root-existence and collision steps are the written algebraic
argument. A separate saved-source review belongs in the ledger.

No saved checker was executed, imported, compiled or rerun.
No arbitrary chart entry, nonresonant (2,3,4) exclusion, remaining
profile recognition, unrestricted cancellation, historical novelty,
external expert review or formal certification is claimed.
