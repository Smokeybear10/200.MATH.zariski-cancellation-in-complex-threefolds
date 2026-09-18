# A quadric reduction and eight degree profiles outside one moving-slope resonance

Working necessary result: under the entire actual264 chart, assume
k=s+f, n=nu*s+n0 with f,nu,n0 in ker(partial_s), and b=nu' nonzero.
A polynomial change of the three intrinsic generators puts the third
level on a quadric. The genuine fourth level has degree at most four
in these new generators. Their intrinsic degrees are at most eight.
Outside the coefficient relation f'''=6b, only eight nonconstant
degree profiles and one constant boundary survive.

These are restrictions on a supplied chart, not a recognition theorem
or an assertion that any surviving profile occurs. The exceptional
coefficient relation is not excluded. A polynomial change over the
coefficient field is not declared an original complex coordinate change.

## 1. Actual assumptions and exact input

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
the globally sliced polynomial four-ring B=C[X,Y,Z,W]=A[u], E=partial_u,
the exact E-degree profile (1,2,2,2), and the ENTIRE weighted initial
kernel (mathsf X^2 mathsf Z-mathsf Y^2). The nonzero selected derivation
N=[u^4]partial_Z|A, a0=EX, and the exact coefficient localization give
\[
\begin{gathered}
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient partials commute, initially fix v, and have joint
constant field C. Put F=ker_L(partial_s), finite over C(t) but not
assumed rational. Throughout assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F,\qquad b=\nu'\ne0.
\tag{2}
\]
Primes on elements of F mean their exact t-derivatives. No derivative
restriction on ell, h, n0, or f is added until explicitly stated.

Use the complete genuine H,Q and their levels h,q0 from
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md).
Its Section2 reconstructs the full corrected fourth potential of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular
\[
H(y,\sigma,\theta)=h,\quad Q(y,\sigma,\theta)=q_0,
\quad h,q_0\in L,
\tag{3}
\]
and the evaluated two-by-two gradient minors generate O. This unit
ideal is an actual scalar consequence, not an assumed smoothness of
any two-coordinate projection. The direct result
[440](principal-paraboloid-arbitrary-longitudinal-moving-first-slope-constant-sigma-exclusion-pass440-working.md)
also gives sigma not in L under exactly these assumptions.

## 2. A polynomial quadric change without a nonunit denominator

Define coefficients in L by
\[
A=f''-2\nu,\qquad B=n_t-\nu f',\qquad E_0=\ell_s+\nu^2.
\tag{4}
\]
For independent formal variables U,P,V, put x=U+(AP+B)/2. The full
third polynomial becomes
\[
H-h=x^2+(bP-E_0)V+R_3(P),
\tag{5}
\]
where the exact polynomial, including its moving level, is
\[
\begin{aligned}
R_3(P)={}&\frac{f'''}6P^3
 +\left(\frac{n_{tt}-\nu f''}{2}-\frac{A^2}{4}\right)P^2\\
&+\left(-\nu n_t-\ell_t-\frac{AB}{2}\right)P
 +\nu\ell-h-\frac{B^2}{4}.
\end{aligned}
\tag{6}
\]
Divide in the polynomial ring L[P], by a polynomial with nonzero
leading coefficient b. This defines unique T2 in L[P], deg T2<=2,
and rho in L with
\[
R_3(P)=(bP-E_0)T_2(P)+\rho,\qquad
\rho=R_3(E_0/b).
\tag{7}
\]
For clarity, this is polynomial division before evaluation. It does
not invert the possibly nonunit b*sigma-E0 in O.

Make the triangular polynomial change
\[
p=P-E_0/b,\qquad q=V+T_2(P),\qquad x=U+(AP+B)/2,
\qquad d=-\rho.
\tag{8}
\]
The inverse is P=p+E0/b, U=x-(AP+B)/2, V=q-T2(P). Both directions
are polynomial over L and the formal Jacobian determinant is one.
After evaluation, reuse x,p,q for the resulting elements of O. Then
\[
\boxed{x^2+bpq=d,\qquad O=L[x,p,q],\qquad p\notin L.}
\tag{9}
\]
This change is intrinsic only. Coefficient differentiation cannot
silently treat x,p,q as the original fixed v. No such differentiation
will be used in the degree argument.

## 3. The complete support of the transformed fourth equation

Let tau denote substitution by the inverse in(8). Define the FULL
polynomial
\[
\Phi(x,p,q)=\tau\left(Q-q_0-\frac{f''}{2}(H-h)\right).
\tag{10}
\]
Together with438's displayed Q, (6)--(10) define every coefficient
of Phi, including all derivatives of h and the level q0. There is
no discarded lower polynomial. Its support is
\[
\begin{aligned}
\Phi={}&\alpha p^2x+b xq+u_1px
 +\delta p^4+\kappa p^3+\epsilon p^2q-\frac{\ell_{ss}}2q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00},
\end{aligned}
\tag{11}
\]
where u1, all c's and kappa are exact coefficients in L determined
by(10). The three needed high coefficients are
\[
\boxed{
\begin{aligned}
\alpha&=\frac{f'''}3-2b,\\
\delta&=\frac{3b^2f''''-6bb'f'''-\ell_{ss}(f''')^2}{72b^2},\\
\epsilon&=\frac{b'}2+\frac{\ell_{ss}f'''}{6b}.
\end{aligned}}
\tag{12}
\]
The coefficient of xq is exactly b, nonzero. To check the leading
terms, T2 has P^2 coefficient f'''/(6b). In the reduced fourth
polynomial the x coefficient is bV+(f'''/2-2b)P^2 plus lower terms.
Substitution V=q-T2 gives alpha. The P^4 terms come from f''''P^4/24,
b'P^2V/2, and -ell_ss V^2/2, giving delta. Their mixed P^2q terms
give epsilon. Translation P=p+E0/b does not change these coefficients.
All other terms have exactly the support allowed in(11).
There is no term constant in p,q multiplying x. Indeed the corrected
Q_U identity from438, after the centering of U, gives the x coefficient
\[
R_3'(P)+bV-(2P+f')(bP-E_0).
\]
Here primes on R3 and T2 denote formal P-derivatives, not coefficient
t-derivatives.
Since R3' = b*T2+(bP-E0)*T2', substituting V=q-T2 makes this
\[
bq+(bP-E_0)(T_2'(P)-2P-f')
 =bq+\alpha p^2+u_1p.
\]
This also proves the support assertion for the x terms directly.

The pair (x^2+bpq-d,Phi) has evaluated gradient minors generating O.
Indeed replacing Q-q0 by Q-q0-f''(H-h)/2 leaves the gradient wedge
unchanged over L. The polynomial automorphism(8) acts on the wedge
by the second exterior power of an invertible polynomial Jacobian.
It therefore preserves the ideal generated by its components, after
evaluation as well. In particular Phi is not identically zero and
cannot share a factor with the quadric that vanishes on the line.

## 4. The intrinsic degree bound is eight

The elementary two-equation argument of
[299, Sections2--4](principal-paraboloid-generic-degree-bound-pass299-working.md)
applies with total degrees at most two and four instead of three
and four. Briefly, remove a polynomial gcd from the two equations.
The unit minors show that its evaluation is a unit, so the reduced
coprime equations still vanish on the whole line. If their degrees
are a1<=2 and a2<=4, their homogenized quotient has degree-n dimension
\[
a_1a_2n+\frac{a_1a_2(4-a_1-a_2)}2
\quad\text{for sufficiently large }n.
\tag{13}
\]
It surjects onto evaluated polynomials of total degree at most n.
If D is the greatest intrinsic degree of x,p,q, whole generation
O=L[x,p,q] gives at least D(n-C+1) independent such polynomials
for some fixed C. Divide these inequalities by n and let n grow.
Thus
\[
\boxed{\max(\deg_vx,\deg_vp,\deg_vq)\le8.}
\tag{14}
\]
Zero polynomials are ignored in this maximum. This argument works
over the exact field L and does not assert that these two equations
generate the entire curve ideal. The bound is on the new generators;
the quadratic shear in(8) is not an affine degree-preserving change
of theta. The old degree-twelve bound for the original generators
from299 remains separately available.

## 5. Nonresonant unequal-degree profiles

For the rest of this note add the explicit condition
\[
\alpha\ne0,\quad\text{equivalently } f'''\ne6b.
\tag{15}
\]
If q=0, (9) makes x constant and O=L[p], so deg_v p=1. The gradient
ideal of the quadric is a unit, and p is nonconstant, so x cannot
be zero. Thus this boundary has d=x^2 in L* and x in L*.

Assume q is nonzero. Since p is nonconstant, a constant x would
make the nonconstant product pq constant, impossible. Define
\[
a=\deg_vp\ge1,\quad c=\deg_vx\ge1,\quad e=\deg_vq\ge0.
\]
The leading terms of the quadric and(14) give
\[
2c=a+e,\qquad a,c,e\le8.
\tag{16}
\]
The potentially largest degrees in(11) are
\[
\begin{array}{c|rrrrrr}
\text{term}&p^4&p^3&p^2x&p^2q&xq&q^2\\\hline
\text{degree}&4a&3a&2a+c&2a+e&c+e&2e.
\end{array}
\tag{17}
\]
The other terms have degree at most max(a+c,2a,a+e). A coefficient
forced to vanish is removed before the next comparison.

If e<a, then c<a. First p^4 forces delta=0 and then p^3 forces
kappa=0. The nonzero alpha*p^2*x is now uniquely highest, impossible.
This also excludes nonzero constant q.

If a<e<2a, first p^4 forces delta=0 and p^2q forces epsilon=0.
The only possible cancellation of alpha*p^2*x is with q^2. If q^2
were strictly higher its coefficient would first have to vanish,
again leaving p^2x alone. Thus 2e=2a+c, ell_ss nonzero, and
\[
e=5a/3,\quad c=4a/3.
\]
The integer degrees and bound eight leave exactly (a,c,e)=(3,4,5).

If e=2a, then c=3a/2. Integrality and e<=8 leave (2,3,4) and
(4,6,8). The three terms of degree4a may cancel; no extra coefficient
vanishing is asserted for this case.

If e>2a, q^2 is uniquely highest until ell_ss=0 is imposed. For
2a<e<3a, p^2q is next uniquely highest unless epsilon=0. Then xq
and p^4 must have the same degree: all other terms are strictly
lower than xq, and removing a uniquely highest p^4 would leave
xq alone. Hence c+e=4a, giving (a,c,e)=(3,5,7). Here delta is
nonzero. In terms of(12), this case requires
\[
\ell_{ss}=0,\quad b'=0,\quad f''''\ne0.
\tag{18}
\]
If e=3a, then c=2a, and p^2q cancels xq only when epsilon is
nonzero. The allowed profiles are (1,2,3) and (2,4,6). In this
case ell_ss=0 and b' nonzero. If e>3a, xq is uniquely highest
after ell_ss=0, impossible.

## 6. Equal degrees are at most two

Suppose a=c=e. The p^4 term first gives delta=0. Put
lambda=lc_v(x)/lc_v(p) in L*. The quadric gives lc_v(q)=-lambda^2
lc_v(p)/b. Use the invertible LINEAR quadric shear
\[
x_1=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p.
\tag{19}
\]
Then x1^2+b*p*q1=d, O=L[x1,p,q1], and deg_v x1<a. If q1=0,
x1 is constant and whole generation gives a=1.

Otherwise x1 is nonconstant. If c1=deg_v x1 and e1=deg_v q1,
then 2c1=a+e1 and 0<=e1<c1<a. In(11), with delta=0, the entire
degree-three part after substitution is
\[
\left(\alpha-\frac{2\epsilon\lambda}{b}\right)p^2x_1
 +\epsilon p^2q_1
 +\left(\kappa+\alpha\lambda-\frac{\epsilon\lambda^2}{b}\right)p^3.
\tag{20}
\]
All other terms have total degree at most two. Any x1^2 introduced
there can be reduced by the quadric without increasing that degree.
The p^3 coefficient must vanish first, and then the p^2*x1 coefficient
must vanish. By alpha nonzero this forces epsilon nonzero. If e1>0,
epsilon*p^2*q1 has degree2a+e1>2a, greater than every remaining
term, a contradiction. Thus q1 is a nonzero constant. The quadric
expresses p as a quadratic polynomial in x1 and O=L[x1]. Whole
generation forces c1=1, hence a=2. The only equal-degree profiles
are therefore (1,1,1) and (2,2,2).

## 7. Exact conclusion and unresolved boundaries

Under(1),(2),(15), the q nonzero branch has the exhaustive necessary
list
\[
\boxed{
(\deg_vp,\deg_vx,\deg_vq)\in
\{(1,1,1),(2,2,2),(3,4,5),(2,3,4),(4,6,8),
  (3,5,7),(1,2,3),(2,4,6)\}.}
\tag{21}
\]
The separate q=0 boundary has x in L*, deg_v p=1. In particular
\[
1\le\deg_v\sigma=\deg_vp\le4
\quad\text{when }f'''\ne6\nu'.
\tag{22}
\]
The quadric reduction, support and degree-eight bound do not require
this last nonresonance. At f'''=6b, however, the p^2x coefficient
vanishes and the degree comparisons above cannot be used. For
example then delta=-(b'+2ell_ss)/4 and epsilon=-2delta; these coupled
coefficients have to be treated, not discarded as a generic case.

The surviving profiles still have exact coefficient functions in a
finite extension of C(t,s). They must obey the full fourth level,
nonzero calibrated scalar, both actual returns and original-ring
entry. A finite list of integer degrees is not a finite numerical
classification and is not a proof of cancellation. The argument
does not promote a function-field equality to a polynomial return.

Root read264,296,299,300,354,438 and440 fully before this writeup.
Fresh unsaved1323a5, completed as2bc77a, reconstructed all three
corrected gradients, the polynomial quadric substitution, the full
fourth support and coefficients(12), as well as440's nonzero-D
quadratic obstruction. Every identity residual was zero. The
degree proof is the written inequality argument, not enumeration
or numerical evidence. Separate review is recorded in the ledger.

No saved checker was executed, imported, compiled or rerun. No
original complex polynomial coordinate change, arbitrary chart
entry, actual realization, unrestricted cancellation, historical
novelty, expert review or formal certification is claimed.
