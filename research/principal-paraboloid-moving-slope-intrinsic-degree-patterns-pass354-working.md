# A degree-three bound for sigma in the moving-slope sector

Working necessary result: retain every actual hypothesis of264 and assume
k=s, n_ss=0, n_ts nonzero. Then sigma is nonconstant and has intrinsic
polynomial degree at most three. After the exact quadric centering below,
only six nonconstant degree patterns and one constant boundary remain.
Equal degrees greater than two are impossible, independently of the
earlier degree-six bound.

These are restrictions on one supplied chart. They do not classify the
coefficient functions, prove original-ring recognition, or show that
arbitrary cancellation candidates enter this chart. No remaining pattern
is asserted to occur in an actual globally sliced polynomial ring.

## 1. Inputs and exact normalized support

Retain the complete actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), the fourth
potential and unit-gradient conclusions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the scoped reductions of
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md)
and [350](principal-paraboloid-moving-first-slope-constant-sigma-exclusion-pass350-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=L(v)=\mathbb C(y,z,w),\quad O=L[y,\sigma,\theta],
\quad J(X)=-a_0^4\in L^*,\quad a_0=EX.
\end{gathered}
\tag{1}
\]
The selected N comes from the literal Z-partial as in264. All coefficient
derivatives are the retained commuting extensions to L. Write
\[
k=s,\qquad n=B(t)s+f(t),\qquad
B,f\in F:=\ker_L\partial_s,\qquad b=B'\ne0.
\tag{2}
\]
The field F is finite over C(t); no rationality assumption is added.

Use349's notation
\[
\begin{gathered}
A_2=n_{tt}/2-B^2,\quad C=\ell_s+B^2,\quad T=\ell_t,
\quad \bar h=h-B\ell+n_t^2/4,\\
x=y+n_t/2-B\sigma,\qquad p=\sigma-C/b,\\
q=\theta+(A_2/b)\sigma+A_2C/b^2-T/b,\qquad
d=\bar h-A_2C^2/b^2+TC/b.
\end{gathered}
\tag{3}
\]
This is an invertible affine change over L, not an original coordinate
change. By349 and350,
\[
x^2+bpq=d,\qquad O=L[x,p,q],\qquad p\notin L,
\qquad \max(\deg_vx,\deg_vp,\deg_vq)\le6.
\tag{4}
\]
The last bound follows from349's birational sextic argument. The older
general bound twelve is already in299 and is not a new result here.

Substitute(3) into349's centered fourth polynomial. Its complete support
has the form
\[
\begin{aligned}
0=\Phi(x,p,q)={}&-2bp^2x+\frac{b'}2p^2q+\kappa p^3
 +b xq+(A_2-2C)xp-\frac{\ell_{ss}}2q^2\\
&+\rho_{11}pq+\rho_{20}p^2+\rho_{10}p+\rho_{01}q+\rho_{00},
\end{aligned}
\tag{5}
\]
where every rho belongs to L and
\[
\kappa=\frac{n_{ttt}}6-2Bb-\frac{A_2b'}{2b},\qquad
\rho_{11}=\frac{A_2\ell_{ss}+Cb'}b-\ell_{ts}.
\tag{6}
\]
No omitted term has x-degree positive. In particular the coefficients
of p^2x and xq are the nonzero scalars -2b and b. The lower coefficients
need not be known for the degree arguments. For an explicit check of
the substitution, its p^2 coefficient is
\[
\rho_{20}=\frac{-A_2^2\ell_{ss}+4A_2Bb^2-4A_2Cb'
 +2A_2b\ell_{ts}-8BCb^2+Cb n_{ttt}+Tb b'-b^2\ell_{tt}}{2b^2}.
\tag{7}
\]
These are coefficient-field identities, obtained before any intrinsic
leading coefficient is compared.

## 2. The constant boundary and degree balance

If q=0, the first identity of(4) makes x a constant in L. Whole return
then says O=L[p], so deg_v p=1. The unit surface-gradient ideal from296
also gives x nonzero: otherwise its entries (2x,bq,bp) would generate
the proper ideal (p). Thus d=x^2 is a nonzero square in L.

Assume henceforth q is nonzero. Then x is nonconstant. Otherwise pq
would belong to L, which is impossible for nonconstant p and nonzero
polynomial q. Put
\[
a=\deg_v p\ge1,\quad c=\deg_v x\ge1,
\quad e=\deg_v q\ge0.
\tag{8}
\]
The two positive-degree terms in the quadric must cancel at their top,
so
\[
2c=a+e,\qquad a,c,e\le6.
\tag{9}
\]
For(5), the relevant degrees are
\[
\begin{array}{c|ccccc}
\text{term}&p^3&p^2x&p^2q&xq&q^2\\\hline
\text{degree}&3a&2a+c&2a+e&c+e&2e.
\end{array}
\tag{10}
\]
The other terms have degrees at most max(2a,a+e,a+c). A term whose
coefficient vanishes is removed before comparing the remaining terms.
The coefficients of p^2x and xq cannot be removed this way.

## 3. Unequal-degree patterns

If e<a, then c<a. The p^3 term has uniquely highest degree unless
kappa=0. After imposing that necessary vanishing, p^2x has uniquely
highest degree, a contradiction. This includes nonzero constant q.

Suppose a<e<2a. Then a<c<e. The p^2q term is uniquely highest unless
b'=0. After that vanishing, p^2x is strictly above every term except
possibly q^2. If 2e>2a+c, the q^2 coefficient must vanish first and
p^2x again becomes uniquely highest. If 2e<2a+c there is an immediate
contradiction. Thus
\[
2e=2a+c,\qquad e=5a/3,\quad c=4a/3,
\quad b'=0,\quad \ell_{ss}\ne0.
\tag{11}
\]
The integer degrees and bound six leave only (a,c,e)=(3,4,5).

If e=2a, then c=3a/2. Integrality makes a even, and the bound six
leaves (a,c,e)=(2,3,4). No vanishing of b' or ell_ss is asserted for
this tied-leading-term case.

If e>2a, the q^2 term is uniquely highest until ell_ss=0 is imposed.
Compare the remaining p^2q and xq terms. For 2a<e<3a, the former is
uniquely highest, forcing b'=0, after which xq is uniquely highest.
For e>3a, xq is uniquely highest immediately. Both intervals are
therefore impossible. Only
\[
e=3a,\quad c=2a,\quad \ell_{ss}=0,\quad b'\ne0
\tag{12}
\]
can survive, giving (1,2,3) or (2,4,6). Here the leading coefficients
obey lc_v(x)=-(b'/(2b))lc_v(p)^2. This is not a claim that x itself
equals that quadratic polynomial in p.

## 4. Equal degrees are at most two

Assume a=c=e and put lambda=lc_v(x)/lc_v(p), an element of L*.
The quadric's leading terms give lc_v(q)=-(lambda^2/b)lc_v(p).
Use the invertible L-linear shear
\[
x_1=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}b x-\frac{\lambda^2}b p.
\tag{13}
\]
It preserves both the quadric and the whole ring:
\[
x_1^2+bpq_1=d,\qquad O=L[x_1,p,q_1],\qquad\deg_v x_1<a.
\tag{14}
\]
If q1=0, then x1 belongs to L and whole return forces a=1. Otherwise
x1 is nonconstant and, with c1=deg_v x1 and e1=deg_v q1, one has
\[
2c_1=a+e_1,\qquad 0\le e_1<c_1<a.
\tag{15}
\]

Substitute x=x1+lambda p and q=q1-2lambda x1/b-lambda^2 p/b in(5).
Reduce any x1^2 term by(14). All such terms came from the degree-two
part of(5), so their reduction stays of total degree at most two.
The complete cubic part becomes
\[
Kp^2x_1+\frac{b'}2p^2q_1+\Gamma p^3,
\quad K=-2b-\frac{b'\lambda}b,
\quad\Gamma=\kappa-2b\lambda-\frac{b'\lambda^2}{2b}.
\tag{16}
\]
By(15), p^3 has uniquely highest intrinsic degree, so Gamma=0.
Next p^2x1 has uniquely highest degree unless K=0. Since b is nonzero,
this forces
\[
b'\ne0,\qquad \lambda=-\frac{2b^2}{b'},\qquad
\kappa=-\frac{2b^3}{b'}.
\tag{17}
\]
If e1>0, p^2q1 now has degree 2a+e1>2a, while the remaining
total-degree-two polynomial has intrinsic degree at most 2a.
Its nonzero coefficient b'/2 gives a contradiction. Therefore q1
is a nonzero constant. The quadric expresses p as a polynomial in
x1, so O=L[x1]. Consequently c1=1, and(15) gives a=2.

This proves that equal degrees a=c=e greater than one must be exactly
(2,2,2), and then(17) is necessary. The proof used no initial degree
bound. The case (1,1,1) is left open here, including the possibility
q1=0.

## 5. Exact conclusion and what it does not decide

In the q nonzero branch the exhaustive necessary list is
\[
\boxed{(\deg_vp,\deg_vx,\deg_vq)\in
\{(1,1,1),(2,2,2),(2,3,4),(3,4,5),(1,2,3),(2,4,6)\}.}
\tag{18}
\]
The only other boundary has q=0, x a nonzero constant, and deg_v p=1.
Since p differs from sigma by an element of L,
\[
\boxed{1\le\deg_v\sigma\le3.}
\tag{19}
\]
In particular degree three requires the pattern(3,4,5), b'=0 and
ell_ss nonzero. Degree two with all normalized degrees equal requires
the resonance(17). The centered square/parity restrictions in351 can
be imposed in addition, but are not needed for(18),(19).

Only integer degree patterns are finite here. Their coefficients still
lie in an arbitrary exact finite extension of C(t,s), and must satisfy
the whole fourth level, full nonzero scalar calibration, strong complex
field return, and original-ring descent. This is not a finite numerical
search, a polynomial ansatz for those coefficient functions, or a
recognition theorem. The unrestricted cancellation conjecture is unsolved.

Root completely read264,296,349,350 and the earlier299 degree proof.
Fresh unsaved symbolic calculations f0d5aa and39b8be verified the full
normalized support, the quadric shear, and the transformed cubic modulo
the monic quadric. A separate agent independently reconstructed the
support and checked every degree comparison and boundary before this
writeup; review of this saved text is recorded separately. The proof
above is the degree argument, not a numerical enumeration. No saved
checker was executed, imported, compiled or rerun for this note, and
no human-expert, formal-proof, publication or novelty claim is made.
