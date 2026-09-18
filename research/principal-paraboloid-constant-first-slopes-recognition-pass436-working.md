# Recognition with constant coupling and first-potential slopes

Working synthesis, retaining the recognition dependencies stated below:
under EVERY actual hypothesis of264, the conditions
\[
k_s=m\in\mathbb C^*,\qquad n_s=\nu\in\mathbb C
\tag{1}
\]
imply that the original sliced kernel is isomorphic to C^[3].
There is no restriction on k_ttt, n_ttt or ell_s. The value nu=0
is included. This extends the transverse relation in429 by removing
its additional condition m ell_s+nu^2=0.

The new composition uses an actual complex polynomial normalization,
the complete430 plane reduction, the necessary exclusions431/433,
the discriminant alternatives434, and the all-X collisions435/437.
The surviving constant-sigma case admits a direct polynomial entry
in an actual three-coordinate frame, so266 recognizes it without
using307's double-projection chain. The zero-k_ttt branch instead
uses348 and346. The inherited recognition results are retained with
their stated dependencies, not recursively certified here.

## 1. Complete actual input and derivative conventions

Retain the full supplied principal chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad Na_0=Nt=Ns=0,\\
Nv=1,\qquad O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
J_{t,s,v}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{2}
\]
Here L[A] denotes the specified actual coefficient localization.
In addition to the displayed consequences, every original slice,
localization, selected-partial and genuine-potential hypothesis of264
remains in force. Formal potential identities alone are not substitutes.

The coefficient partials commute, fix v, and have joint constants C.
The exact field F=ker_L partial_s is finite over C(t); it is not
identified with the rational field. Its t-derivative has constants C.
The literal rows are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{3}
\]
All subsequent coefficient-field manipulations are distinguished from
actual changes of these original coordinates.

## 2. Actual removal of the constant first-potential slope

First fix X,Y,Z and replace W by W1=mW. Its inverse divides only
by the nonzero complex number m. Set s1=ms. Then k_s1=1 and
n_s1=B:=nu/m is complex. Exact subtraction gives
\[
k=s_1+f,\qquad n=Bs_1+g,\qquad f,g\in\mathbb F,
\tag{4}
\]
with no restriction on ell. Write primes for the exact t-derivative
on F. For the next formulas rename this scaled W1,s1 as W,s.
The full first two potentials are
\[
\begin{aligned}
z&=2ty+\sigma^2+f'\sigma+\theta+Bs+g,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-g'\sigma-B\theta.
\end{aligned}
\tag{5}
\]

Make the actual complex polynomial map
\[
X_*=X+B,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W+2BZ.
\tag{6}
\]
Its inverse is X=X*-B, W=W*-2BZ*, with Y,Z fixed. Expanding at
fixed X* gives the complete coefficient transport
\[
\begin{aligned}
t_*&=t,&s_*&=s+2Bt^2,&k_*&=s_*+f,\\
y_*&=y-B\sigma+B^2t,&\sigma_*&=\sigma-2Bt,\\
z_*&=z-B(2t\sigma+s+f)+B^2t^2,\\
\theta_*&=\theta+4Bt\sigma+2Bf-4B^2t^2,\\
w_*&=w+2Bz-B\theta-4B^2t\sigma-B^2s-2B^2f+2B^3t^2.
\end{aligned}
\tag{7}
\]
The starred partials are partial_s*=partial_s and
partial_t*=partial_t-4Bt partial_s. They restrict to the same exact
t-derivative on F. The transported potentials are
\[
\boxed{n_*=g-B^2t^2+2Bt f'-3Bf\in\mathbb F,}
\tag{8}
\]
\[
\boxed{\ell_*=
\ell+B^2s+2Bg-2Bt g'+2B^3t^2
-2B^2t^2f''+3B^2t f'-2B^2f.}
\tag{9}
\]
These satisfy exactly
\[
\begin{aligned}
z_*&=2ty_*+\sigma_*^2+f'\sigma_*+\theta_*+n_*,\\
w_*&=\ell_*-(2\sigma_*+f')y_*
                     -\frac{f''}{2}\sigma_*^2-(n_*)_{t_*}\sigma_*.
\end{aligned}
\tag{10}
\]
In particular (n*)_s*=0. No assumption on ell_s was used.
The generic potential transport in429 Sections1--3 proves these
identities before its extra transverse condition is imposed.

In ORIGINAL coordinates the combined map, inverse and parameter
change are
\[
\begin{aligned}
X_*&=X+B,&Y_*&=Y,&Z_*&=Z,&W_*&=mW+2BZ,\\
X&=X_*-B,&Y&=Y_*,&Z&=Z_*,&W&=(W_*-2BZ_*)/m,\\
t_*&=t,&s_*&=ms+2Bt^2,&f&=k-ms.
\end{aligned}
\tag{11}
\]
All inverse denominators are nonzero complex constants. In these
original parameters,
\[
(\ell_*)_{s_*}=\frac{\ell_s}{m}+B^2
               =\frac{m\ell_s+\nu^2}{m^2}.
\tag{12}
\]
This need not vanish, or initially be complex. The proof below
allows every value of this derivative.

The actual licenses in429 do not depend on its special relation
ell_s=-B^2. The weighted leading map fixes X,Y,Z and takes W to
mW+2BZ. It is invertible and preserves the full initial ideal.
The leading ratio ms+2Bt^2 is nonzero and algebraically independent
of t, so the exact four time degrees are preserved. EX*=a0.

The literal selected partial is
\[
\partial_{Z_*}=\partial_Z-(2B/m)\partial_W.
\tag{13}
\]
The old W-partial has horizontal shift at most three by264's
omitted-leading-triple bound; the old Z-partial has exact shift four.
Therefore N*=N. The exact field L and the chosen Nv=1 are unchanged.
The map of (y,sigma,theta) in(7) is invertible affine over L and
preserves the whole O-return. For the stronger complex return use
the actual quotient separately: B_a0=A_a0[X*], and evaluation at
X*=0 in the actual starred frame gives K=C(y*,z*,w*) and the usual
N-constant localization. Neither return is inferred from an arbitrary
field-valued coordinate change.

Finally, the row determinant in(11) at fixed X* is m, while the
parameter determinant from(t,s,v) to(t*,s*,v) is also m. Hence
\[
J_*(X_*)=J(X_*-B)=-a_0^4.
\tag{14}
\]
The original E, its global slice and its kernel A have not changed.
Thus every actual264 hypothesis survives. Renaming the starred
chart, it suffices to recognize
\[
\boxed{k=s+f,\qquad f,n\in\mathbb F,\qquad n_s=0,}
\tag{15}
\]
with ell arbitrary. Since the exact t-derivative on F was unchanged,
f''' is the original k_ttt. No bound on it was introduced.

## 3. The zero longitudinal third derivative

If f'''=0, the ORIGINAL hypotheses in(1) give
k_ttt=0 and n_ss=n_ts=0. The actual normalization theorem
[348](principal-paraboloid-constant-coupling-general-first-normalization-pass348-working.md)
therefore applies directly. It produces a full actual chart with
k*=s* and (n*)_s*=0, with no restriction on the transformed ell.
Its endpoint is precisely
[346](principal-one-variable-first-potential-recognition-pass346-working.md).
Consequently A is C^[3], with346's retained recognition dependencies.

This branch does NOT cite337 alone:337 additionally requires
ell_s=0. Nor does this branch need422's broader n_ss analysis.
The finite-field first potential in346 may remain nonrational;
no n_ttt bound is used in348 or here.

## 4. Nonlinear time coupling with zero second slope

Suppose now f''' is nonzero in the normalized chart(15), and put
e=ell_s. If e=0, the completely read result
[427](principal-paraboloid-arbitrary-longitudinal-coupling-recognition-pass427-working.md)
applies: k_s=1 and n_s=ell_s=0, with arbitrary f. It recognizes A.

In its nonlinear-time branch427 proves y,sigma belong to L, then
constructs the global auxiliary LND from the original slice. Its
literal row fixes the actual polynomial three-ring
C[X,Y,W-XZ]. The primitive restriction and actual preslice permit
Daigle's theorem, followed by the Bhatwadekar--Gupta--Lokhande
invariant-coordinate criterion. These actual hypotheses, rather
than a generic line parameter alone, supply that endpoint.
427's published-theorem and retained-input qualifications continue
to apply. In particular no assertion that EX is a unit of A is made.

## 5. Nonzero second slope reduces to constant sigma

It remains that f'''e is nonzero. The complete430 reduction retains
the genuine third and fourth levels and the full minor-unit identity.
Then
[431](principal-paraboloid-nonlinear-time-weighted-plane-exclusion-pass431-working.md)
forces ell_ss=0, and
[433](principal-paraboloid-variable-second-slope-exclusion-pass433-working.md)
forces ell_ts=0. Joint exact constants imply
\[
e\in\mathbb C^*,\qquad \ell=es+\ell_0,\quad\ell_0\in\mathbb F.
\tag{16}
\]
431 retains its primary polynomial-plane degree-divisibility input;
433 uses the all-X polynomial return and an elementary degree(2,3)
collision. These hypotheses hold in the actual normalized chart.

For clarity, the crucial all-X license is
\[
L[\mathcal B]=L[A][u]=L[v,u]=L[v,X]=L[X,Y,Z,W],
\tag{17}
\]
since X=a0 u+x0 with x0 in A and a0 in L*. After any coefficient
field extension, it remains a polynomial-ring identity, and every
specialization X=c gives the whole polynomial line. It does not
assert that X-c is an original complex coordinate.

Let h in L be the genuine third level. The plane primitive of430,
under(16), has the exact form
\[
\Phi(U,P)-q=\mathcal A U^2+B(P)U+C(P),\qquad
\mathcal A=f''/2-h_s/e,\qquad [P^2]B=f'''/2\ne0,
\tag{18}
\]
and its evaluated gradient generates O=L[y,sigma]. The complete
discriminant classification
[434](principal-paraboloid-constant-second-slope-discriminant-reduction-pass434-working.md)
retains all moving levels. If Acal=0, it forces sigma in L. If
Acal is nonzero, it gives exactly two possible intrinsic profiles:
\[
(\deg_v\sigma,\deg_vy)=(1,2)\quad\text{or}\quad(2,4).
\tag{19}
\]
The first is excluded by
[435](principal-paraboloid-affine-sigma-nonlinear-time-exclusion-pass435-working.md).
For the second,434 gives a generator x of O with
\[
\sigma=a x^2+b,\qquad
y=\gamma\sigma^2+\beta\sigma+\delta+\kappa x,
\qquad a\gamma\kappa\ne0.
\tag{20}
\]
This is exactly the coefficient-field input of
[437](principal-paraboloid-quadratic-sigma-collision-exclusion-pass437-working.md),
which excludes it by(17). Both collision arguments handle distinct
points and repeated roots, the latter by a common derivative-zero
contradiction. Neither promotes x to an ambient coordinate.

The alternatives are exhaustive, including Acal=0 and the nonzero
constant-discriminant boundary in434. We conclude in this branch
that sigma belongs to L.

## 6. Direct actual polynomial entry in the constant-sigma case

With sigma in L,430 gives O=L[y,sigma]=L[y], so y is an affine
nonconstant polynomial parameter of the actual localized line.
The coefficient of U^2 in Phi must vanish. The zero-Acal part of434
then gives, using its full coefficient ledger,
\[
\sigma=p=-b_1/f'''\in\mathbb F,\qquad
b_1=n''+2e-(f'')^2/2,\qquad
h=e f''s/2+h_*,\quad h_*\in\mathbb F.
\tag{21}
\]
Indeed Phi(U,p)=q forces B(p)=0, and the unit normal derivative
forces B'(p)=0, giving p=-b1/f'''. The identity Acal=0 gives
h_s=e f''/2, and exact subtraction gives the last formula.
Neither step assumes L=F(s).

The complete third relation now reads
\[
\theta=\frac{y^2+(f''p+n')y+(f'''/6)p^3
                 +(n''/2)p^2-\ell_0'p-h_*}{e}-\frac{f''}{2}s.
\tag{22}
\]
Every coefficient other than s,y in this expression belongs to F.
In particular the moving third-level term has been retained.

Use the ACTUAL complex polynomial coordinate frame
\[
U=Y,\qquad V=W-XZ,\qquad
\mathcal B=\mathbb C[X,U,V,Z],\qquad W=V+XZ.
\tag{23}
\]
This triangular map and its inverse involve no element of L as an
ambient coefficient. Define the coefficient polynomials
\[
\begin{aligned}
D(X)&=2p+f'+2tX,\\
R(X)&=\ell_0-\frac{f''}{2}p^2-n'p
 -X(p^2+f'p+n)-(2tp+f)X^2-t^2X^3
 \quad\in\mathbb F[X].
\end{aligned}
\tag{24}
\]
The complete literal rows and the first two potentials give
\[
\boxed{U=y+pX+tX^2,\qquad V=e s-D(X)y+R(X).}
\tag{25}
\]
For the second identity, the theta terms cancel in W-XZ. Its sX^2
terms cancel as well, leaving the displayed polynomial; no division
by X or by a polynomial in the actual coordinates occurs.
Consequently
\[
y=U-pX-tX^2,\qquad
s=\frac{V+D(X)y-R(X)}e\quad\in\mathbb F[X,U,V].
\tag{26}
\]
Only the nonzero coefficient e is divided out. Substitution in(22)
puts theta in the same polynomial ring, and hence the literal row
\[
Z=2ty+p^2+f'p+\theta+n+(2tp+s+f)X+t^2X^2
\tag{27}
\]
proves the actual polynomial-entry statement
\[
\boxed{Z\in\mathbb F[X,U,V].}
\tag{28}
\]
This is stronger than rational membership or a generic-line return.
The three variables X,U,V are actual coordinates of the frame(23),
and F is a finitely generated transcendence-degree-one subfield
of Frac A. Thus all hypotheses of the curve-field polynomial-entry
criterion
[266](curve-field-polynomial-entry-criterion-pass266-working.md)
are satisfied, with its fourth coordinate relabeled Z.

That criterion supplies a polynomial P0 in C[X,U,V] for which
Q=Z-P0 is an actual coordinate and EQ=0. Its curve-pencil argument
uses the nonsingular projective model and degree-of-a-function
identities, identified in
[Stacks 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
[0AYZ](https://stacks.math.columbia.edu/tag/0AYZ) and
[02NY](https://stacks.math.columbia.edu/tag/02NY).
The retained proof of266, including its polynomial rather than
rational entry requirement, is the recognition input here.

Finally A is regular by descent from the polynomial extension
A[u]=B, and E is nonzero because Eu=1. In the actual coordinate
frame C[Q,X,U,V], E fixes Q. These are precisely the hypotheses of
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1):
the kernel of a nonzero characteristic-zero LND fixing an ambient
coordinate is a polynomial ring over that coordinate when the
kernel is regular. It follows that A=C[Q]^[2], hence A is C^[3].
The invariant-coordinate and regularity conditions are both used.

For comparison only, (22) also makes theta exact degree two in y,
so [L(v):Frac L[sigma,theta]]=2. This agrees with the already
recognized constant-sigma case307. It is not the different condition
deg_v sigma=2. The present endpoint does not invoke307,303 or295:
(21)--(28) give the necessary actual entry directly. This is a
shorter proof of that existing constant-sigma case, not new coverage
for it. Together with Sections3--5 it proves the implication(1).

## 7. Dependency and verification boundary

The actual normalization uses only the generic algebraic transport
and actual licenses in429 Sections1--3, not429's special recognition
hypothesis. The zero-f''' endpoint is348 followed by346. The e=0
endpoint is427. The e nonzero endpoint is430,431,433--435 and437 followed
by the explicit actual entry(21)--(28) and the retained266 criterion.
These are distinct branches, not a replacement of original-ring
recognition by formal plane classification.

The complete current sources307,303,295,290 and266 were read for
the projection-pedigree audit. The full430/431 and427/429 sources
were independently read for the current continuation. Before this
synthesis,346 and348 were freshly read through61873d and5fcf82;
433,434,435,437 through9e59f3,c67edf,9a8a00,ab89cf; and429 again
through ec2996. Their exact current hashes were revalidated.
After Root proposed the shorter entry,266 was fully reread through
0f5595. The primary BGL theorem and the three stated Stacks inputs
were freshly inspected in turn4650view0--3 and turn4651view0--3.
The writing guide was read through EOF in41c9bc before authoring.

Fresh unsaved321e7c reconstructs all three complete transported
rows and both potentials in(7)--(10), with arbitrary ell and all
required longitudinal jets. Every residual is zero. Fresh d07c38
independently reconstructs437's original-row divided differences
and their diagonal derivatives; d96b15 reconstructs435's complete
quadratic eliminant. Fresh0f5595 reconstructs the entire literal
V identity, both polynomial solves and the complete theta/Z entry,
with zero residuals. The degree-eight root lemma was independently
checked with all multiplicity cases. These finite computations
supplement, and do not replace, the ring and field arguments.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical index was edited. The recognition
inputs346,427 and266 are explicitly retained; this is not a full
recursive audit of their historical dependencies, expert review,
proof-assistant certification or novelty clearance.

Nothing here proves constant k_s or n_s for an arbitrary chart,
allows k_s=0, or supplies an actual principal1222 frame for an
arbitrary globally sliced polynomial ring. Accordingly this is
not an unrestricted cancellation theorem or an arbitrary-entry
result. No actual realization of the remaining formal data is
asserted and no external submission or contact is made.
