# A quadratic cofactor excludes two cubic profiles

Working necessary exclusion: in the supplied full actual264 moving-slope
chart at f'''=6nu', neither (3,2,1) nor (3,3,3) can be the degree triple
(deg p,deg x,deg q) of441's quadric generators. Together with443 this
leaves eight necessary positive-degree resonance profiles and the
separately constrained zero-q boundary. No remaining case is recognized.

## 1. The complete quadratic-relation space at degrees (3,2,1)

Let L be a characteristic-zero field, b in L*, and suppose p,x,q in
L[v] satisfy
\[
x^2+bpq=d\in L,\qquad
(\deg_vp,\deg_vx,\deg_vq)=(3,2,1).
\tag{1}
\]
Since q is affine, use q itself as the intrinsic parameter. Write
\[
x=a q^2+Bq+c,\qquad a\ne0.
\tag{2}
\]
Polynomiality of p=(d-x^2)/(bq) forces d=c^2, and hence
\[
p=-\frac{(aq+B)(x+c)}b.
\tag{3}
\]
These are exact coefficient-field identities; no ambient coordinate
change is asserted.

For independent formal variables X,P,Q define
\[
\begin{aligned}
H&=X^2+bPQ-c^2,\\
F&=X-aQ^2-BQ-c,\\
G&=bP+(aQ+B)(X+c).
\end{aligned}
\tag{4}
\]
All three vanish at (x,p,q), and the formal identity
\[
\boxed{H=(X+c)F+QG}
\tag{5}
\]
holds before evaluation.

Every polynomial of total degree at most two vanishing on this curve
is in the constant-coefficient span of H,F,G over L. Indeed its P^2
coefficient is zero by the unique intrinsic degree six, and its PX
coefficient is zero by degree five. The terms X^2 and PQ of degree
four can be removed together by a scalar multiple of H. The remaining
degree-three terms XQ and P can then be removed by a scalar multiple
of G. Likewise a multiple of F removes the degree-two terms Q^2 and
X. What remains is affine in Q and must be zero because q is
transcendental. This proves the full span claim, including all lower
coefficients and the case c=0.

## 2. Every second quadric has a forbidden common gradient factor

Suppose Phi is such a quadratic relation. Write
\[
\Phi=\lambda F+\mu G+\kappa H,
\qquad \lambda,\mu,\kappa\in L.
\tag{6}
\]
All gradients in this section are formal X,P,Q gradients, evaluated
after differentiation. Equation(5), with F=G=0 on the curve, gives
\[
\nabla H=(x+c)\nabla F+q\nabla G.
\]
Taking the exterior product with the evaluated gradient of(6) yields
\[
\boxed{
\nabla H\wedge\nabla\Phi
 =\chi\,\nabla F\wedge\nabla G,
\qquad \chi=\mu(x+c)-\lambda q.}
\tag{7}
\]
If the three components on the left generated the unit ideal of
L[q], their common factor chi would be a unit, a nonzero element
of L. But(2) gives
\[
\chi=a\mu q^2+(B\mu-\lambda)q+2c\mu.
\tag{8}
\]
Constancy first forces mu=0 because a is nonzero, and then lambda=0.
The resulting chi is zero, not a unit. Thus NO quadratic Phi can
have unit evaluated gradient minors with H for this degree triple.
No assumption that the F,G gradient minors themselves form a unit
ideal was needed: the common factor alone is enough.

## 3. The two actual applications

Retain EVERY actual264 hypothesis, including the sliced polynomial
four-ring, full weighted initial kernel, exact (1,2,2,2) degree
profile, literal selected derivation, exact coefficient localization,
both returns and nonzero calibrated full scalar. Assume, as in
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md),
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in\ker_L\partial_s,\qquad b=\nu'\ne0,
\qquad f'''=6b.
\tag{9}
\]
The exact polynomial intrinsic change gives
\[
O=L[v]=L[x,p,q],\quad x^2+bpq=d,\quad p\notin L,
\tag{10}
\]
and the genuine full fourth polynomial Phi has unit evaluated
gradient minors with this quadric. Its support and coefficient
relations are the complete ones of441 and
[442](principal-paraboloid-moving-slope-resonance-degree-profiles-pass442-working.md).
In particular epsilon=-2delta at resonance. Coefficients remain
in the exact field L, not an assumed rational function field.

For the profile (3,2,1), the lower-degree argument442, Section4,
forces delta=epsilon=kappa=c20=u1=c11=0. The ENTIRE fourth level
is consequently quadratic:
\[
\Phi=bxq+F_2q^2+c_{10}p+c_{01}q+c_{00}.
\tag{11}
\]
It retains the genuine gradient-minor unit. Sections1--2 contradict
that unit, so this profile is excluded.

For (3,3,3), the uniquely highest p^4 term forces delta=0 and hence
epsilon=0. The remaining cubic term kappa*p^3 is uniquely highest,
so kappa=0. Again the FULL Phi is quadratic. Set
lambda=lc_v(x)/lc_v(p) and make the invertible linear quadric shear
\[
x_1=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p.
\tag{12}
\]
It preserves whole generation, the quadric, quadraticity of Phi,
and the unit ideal of its gradient minors. The degree of x1 is
less than three. If q1=0, x1 is constant and whole generation
would force p affine, contradicting deg p=3. Otherwise x1 is
nonconstant. Its degrees obey 2*deg(x1)=3+deg(q1), with
0<=deg(q1)<deg(x1)<3. The only possibility is deg(x1)=2,
deg(q1)=1. This is exactly the degree triple of Sections1--2,
so its genuine second quadric is impossible as well.

## 4. Remaining frontier and verification boundary

After this result and the equal-quartic exclusion
[443](principal-paraboloid-equal-quartic-two-quadric-exclusion-pass443-working.md),
the necessary positive-degree resonance list is
\[
\boxed{
(1,1,1),(2,2,2),(4,5,6),(3,4,5),
(2,3,4),(4,6,8),(1,2,3),(2,4,6).}
\tag{13}
\]
The exact q=0 boundary442(14),(16) is still unresolved. The
nonresonant eight-profile list441(21) is unchanged, and442 excludes
q=0 outside resonance. The original degree bounds
1<=deg(sigma)<=4, deg(y)<=6, deg(theta)<=8 remain in force.
These are restrictions, not assertions of realization or recognition.

Root read441,442,443 fully before this argument. An independent
reconstruction58f7c4 checked(3)--(8), including all wedge components
and c=0. It also obtained a nonzero seven-monomial evaluation minor
-a^12/b^5, agreeing with the complete quadratic-span argument.
The written coefficient comparison and unit-factor proof above
are the proof; numerical sampling is not used.

No saved checker was executed, imported, compiled or rerun. No
earlier proof source was edited. There is no claim of original-ring
recognition, arbitrary chart entry, unrestricted cancellation,
historical novelty, expert review or formal certification.
