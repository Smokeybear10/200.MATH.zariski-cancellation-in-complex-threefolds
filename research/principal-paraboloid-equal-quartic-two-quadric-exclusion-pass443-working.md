# The equal-quartic resonance profile is impossible

Working necessary exclusion: under EVERY actual264 hypothesis and the
moving-slope assumptions k=s+f, n=nu*s+n0, nu' nonzero, the resonance
f'''=6nu' cannot have the equal degree profile (4,4,4) in441's quadric
generators. This removes one entry from442's necessary list. It does
not recognize or realize any remaining profile.

The main algebraic lemma concerns three polynomials of degrees (4,3,2)
on a quadric. Either they fail to generate the polynomial line, or that
quadric is their only quadratic relation. A second quadratic relation
with the genuine independent-gradient condition is therefore impossible.

## 1. Exact lemma over the coefficient field

Let L be a characteristic-zero field, let b in L* and d in L, and let
p,x,q in L[v] satisfy
\[
x^2+bpq=d,\qquad L[p,x,q]=L[v],\qquad
(\deg_vp,\deg_vx,\deg_vq)=(4,3,2).
\tag{1}
\]
Suppose a polynomial Phi of total degree at most two vanishes at
(x,p,q). Then Phi is a scalar multiple of the formal polynomial
H=X^2+bPQ-d. In particular H and Phi cannot have evaluated gradient
minors generating L[v].

First translate the intrinsic parameter to center the quadratic q,
and divide q by its nonzero leading coefficient. Absorb that scalar
into b. We may write q=v^2+c, with c in L. Neither operation changes
whole generation or the degree triple. No algebraic closure is needed.

If the v^2 coefficient of x is lambda, use the invertible linear
quadric shear
\[
x_1=x-\lambda q,\qquad
p_1=p+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}q.
\tag{2}
\]
It preserves x1^2+b*p1*q=d, the degrees (4,3,2), and whole
generation. A formal relation of degree at most two remains such a
relation. Drop the subscripts. Now
\[
q=v^2+c,\qquad x=a v^3+C v+r_0=a qv+r_1v+r_0,
\qquad a\ne0,\quad r_1=C-ac.
\tag{3}
\]
Since p is polynomial, q divides x^2-d. Its exact remainder is
\[
2r_1r_0v+r_0^2-cr_1^2-d.
\tag{4}
\]
Thus r1*r0=0.

If r0=0, then x=v*(a*v^2+C) is odd, and p=(d-x^2)/(bq)
is an even polynomial. Consequently
\[
L[p,x,q]=L[v^2,v(av^2+C)]
 =L[v^2]\mathbin{\oplus}v(av^2+C)L[v^2].
\tag{5}
\]
This ring does not contain v: equality of the odd parts would require
(a*z+C)*F(z)=1 in L[z], impossible because a is nonzero. This
contradicts whole generation, including the case r1=0 as well.

Therefore r0 is nonzero, r1=0 and d=r0^2. The exact polynomials are
\[
q=v^2+c,\qquad x=a qv+r_0,\qquad
p=-\frac{a^2qv^2+2ar_0v}{b}.
\tag{6}
\]
Consider any polynomial relation of total degree at most two. Its
coefficient of P^2 is zero because that is the only monomial with
intrinsic degree eight. Next the coefficient of PX is zero because
it alone has degree seven. The degree-six terms X^2 and PQ cancel
only in the ratio supplied by H. Subtract the appropriate scalar
multiple of H, removing both terms. Then XQ is uniquely of degree
five and its coefficient is zero.

The remaining possible relation is a linear combination of
Q^2,P,X,Q,1. The coefficient of X is zero by its nonzero v^3
coefficient: Q^2 and Q are even, and P in(6) has only even terms
and its displayed v term. The coefficient of P is then zero by
its nonzero v coefficient -2*a*r0/b. Successively the coefficients
of Q^2,Q,1 vanish. Hence the original relation was precisely a
scalar multiple of H. This proves the lemma.

All changes made here are affine in the formal generators, except
an affine reparametrization of v. They preserve quadraticity and
the ideal of evaluated gradient minors. A scalar multiple of H
has gradient proportional to that of H, so every minor is zero.

## 2. Applying the lemma to the actual equal-quartic branch

Retain the entire actual264 chart, including its original sliced
polynomial four-ring, full weighted initial kernel, exact (1,2,2,2)
profile, selected derivation, exact coefficient localization, both
polynomial returns and calibrated scalar. In addition assume the
moving-slope hypotheses of
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md):
\[
k=s+f,\quad n=\nu s+n_0,\quad
f,\nu,n_0\in\ker_L\partial_s,\quad b=\nu'\ne0.
\tag{7}
\]
Its polynomial intrinsic change gives
\[
O=L[v]=L[x,p,q],\quad x^2+bpq=d,\quad p\notin L.
\tag{8}
\]
The genuine full fourth polynomial Phi has support441(11) and
an evaluated gradient-minor unit with the quadric. Assume the
resonance alpha=f'''/3-2b=0 and, for contradiction,
\[
\deg_vp=\deg_vx=\deg_vq=4.
\tag{9}
\]
The p^4 term is uniquely highest, forcing delta=0. At resonance
epsilon=-2delta, so the p^2q term also vanishes. The only remaining
cubic term is kappa*p^3, again uniquely highest, so kappa=0.
The FULL Phi therefore has total degree at most two. This is not
a replacement by selected low-degree terms. It is the same
genuine potential and its minor-unit ideal is retained.

Let lambda=lc_v(x)/lc_v(p), and make the invertible linear shear
\[
x_1=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p.
\tag{10}
\]
It preserves the quadric and whole return, while deg_v x1<4.
The transformed Phi is still quadratic and its evaluated minors
with the quadric still generate O.

If q1=0, then x1 is constant and O=L[p], contradicting deg_v p=4.
Otherwise x1 is nonconstant, and writing c1=deg_v x1, e1=deg_v q1
gives 2c1=4+e1 with 0<=e1<c1<4. The only possibilities are
(c1,e1)=(2,0) and (3,2). In the first case q1 is a nonzero
constant. The quadric expresses p in L[x1], so O=L[x1], forcing
deg_v x1=1, a contradiction. The second case is exactly the
degree triple (4,3,2) of the lemma. Its second genuine quadratic
relation contradicts the lemma's minor conclusion.

Thus
\[
\boxed{(\deg_vp,\deg_vx,\deg_vq)\ne(4,4,4)
\quad\text{at }f'''=6\nu'.}
\tag{11}
\]

## 3. Updated finite frontier and scope

Removing(4,4,4) from
[442](principal-paraboloid-moving-slope-resonance-degree-profiles-pass442-working.md)
leaves the ten necessary positive-degree resonance profiles
\[
\begin{gathered}
(3,2,1),(1,1,1),(2,2,2),(3,3,3),(4,5,6),\\
(3,4,5),(2,3,4),(4,6,8),(1,2,3),(2,4,6).
\end{gathered}
\tag{12}
\]
The separately constrained q=0 boundary remains. In the nonresonant
case the eight profiles441(21) remain necessary, while442 excludes
q=0 there. The original bounds deg(sigma)<=4, deg(y)<=6,
deg(theta)<=8 are unchanged. No remaining case is asserted to
occur or to be recognized.

Root read441 and442 completely before this application. The proof
uses the entire quadratic relation, whole line generation, and
the genuine minor ideal. It does not infer plane normality or
promote a coefficient-field change to an original coordinate.
An independent reconstruction046e10 checked the normalizing shear,
quadratic remainder, explicit branch and quadratic-relation rank;
the written coefficient argument above supplies the proof.

No saved checker was executed, imported, compiled or rerun. No
earlier source was edited for this exclusion. There is no claim of
unrestricted cancellation, arbitrary actual-frame entry, existence,
historical novelty, expert review or formal certification.
