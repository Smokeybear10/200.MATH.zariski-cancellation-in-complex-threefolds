# Affine sigma with an arbitrary first potential: a necessary degree reduction

Working result: retain the complete actual264 chart, assume k=s+f,
f_s=0, n_ss nonzero and f''' nonzero, and suppose sigma has intrinsic
degree one. Then the centered first generator x has degree two and
zeta=theta+sigma^2+f' sigma has degree one. In particular zeta is
nonconstant.

This is a necessary reduction conditional on affine sigma. It does
not force sigma to be affine, exclude the resulting degree pattern,
recognize the original invariant ring, or realize an arbitrary
coefficient-field parametrization. The main additional ingredient is
an elementary all-parameter collision lemma proved below.

## 1. Actual input and the two exact inherited licenses

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and the
specialization in
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md).
In particular the original polynomial ring and slice satisfy
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
X=a_0u+x_0,\quad a_0\in L^*,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[A]=L[v_0]=L[y,\sigma,\theta],\quad Nv_0=1,\\
\operatorname{Frac}A=L(v_0)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v_0)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The displayed initial ideal is the entire weighted initial kernel.
All additional actual264 conditions remain part of the input; (1)
does not replace that input by a formal tuple of polynomials.

The exact coefficient partials on L commute and have joint constants
C. Put F=ker_L(partial_s), finite over C(t), and assume
\[
k=s+f,\quad f\in F,\quad n,\ell\in L,\qquad
e=n_{ss}\ne0,\quad f'''\ne0,\quad \deg_{v_0}\sigma=1.
\tag{2}
\]
Primes on f are exact t-derivatives. Write
\[
a=n_t,\quad \nu=n_s,\quad c=n_{tt},\quad b=n_{ts},\quad
E_0=\ell_s+\nu^2,\quad A_1=f''-2\nu,\quad B_1=a-\nu f'.
\tag{3}
\]
There is no assumption b nonzero, n_ss constant, or L=C(t,s).

Set
\[
x=y+\frac{A_1\sigma+B_1}{2},\qquad
\zeta=\theta+\sigma^2+f'\sigma.
\tag{4}
\]
The complete third relation in458 is
\[
\begin{aligned}
H(U,P,V)={}&U^2+(A_1P+B_1)U+\frac{f'''}6P^3
 +\frac{c-\nu f''}{2}P^2-(\nu a+\ell_t)P+\nu\ell\\
&+(bP-E_0)V+\frac e2V^2,
\qquad H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{5}
\]
Its exact arbitrary-n terms, including eV^2/2, are retained.

The second license is the all-parameter polynomial-ring return from
458, Section 8:
\[
M[x+T\sigma,\ \zeta,\ 2\sigma x+T\sigma^2]=M[v_0]
\quad\text{for every field extension }M/L\text{ and every }T\in M.
\tag{6}
\]
For clarity, this comes from the ORIGINAL slice, which gives
L[B]=O[u]=O[X]=L[X,v0], followed by an invertible polynomial row
change over L[X] and specialization of X. It is not inferred from
the intercept return alone, and it has no generic-value restriction.
The row change and both inverse orders are written in458(30)--(32).
No assumption n_ss=0 is used in that license.

Since sigma is affine with nonzero leading coefficient, put v=sigma.
Then L[v]=L[v0], and this change preserves every intrinsic degree.
It is only a change of polynomial parameter over L. We do not make
an original complex coordinate change or transport the calibrated
coefficient derivatives as if the parameter were fixed. No such
derivative is used below. Equations(5),(6) now hold with sigma=v.

## 2. The completed cubic permits only degrees two or three

Define
\[
q=\theta+\frac{bv-E_0}{e}.
\tag{7}
\]
Completing the two squares in(5) gives the exact identity
\[
x^2+\frac e2q^2+R_3(v)=0,
\tag{8}
\]
where the entire polynomial on the coefficient side is
\[
\begin{aligned}
R_3(P)={}&\frac{f'''}6P^3+\frac{c-\nu f''}{2}P^2
 -(\nu a+\ell_t)P+\nu\ell-h\\
&-\frac{(A_1P+B_1)^2}{4}-\frac{(bP-E_0)^2}{2e}.
\end{aligned}
\tag{9}
\]
Its degree is exactly three and its leading coefficient is f'''/6.
Neither square subtracted in(9) can affect that coefficient.

Extend scalars to an algebraic closure M of L and choose rho in M
with rho^2=-e/2. Here rho is nonzero. Equation(8) factors as
\[
(x+\rho q)(x-\rho q)=-R_3(v).
\tag{10}
\]
Both factors are nonzero because R3 is nonzero. Their degrees add to
three. Their ordered degree pair is therefore one of (0,3), (1,2),
(2,1), (3,0); a nonzero constant factor is allowed. The two degrees
are always different, so neither their half-sum x nor their scaled
difference q can lose the highest term. Consequently
\[
\deg_vx=\deg_vq\in\{2,3\}.
\tag{11}
\]
Degrees are unchanged by this field extension. Also
\[
\zeta=q+v^2+(f'-b/e)v+E_0/e.
\tag{12}
\]
Thus degree three in(11) would give deg(zeta)=3, while degree two
gives deg(zeta) at most two. The possible quadratic cancellation
in(12) must be retained.

## 3. An equal-degree all-parameter collision lemma

Let K be any field of characteristic zero. Suppose x,zeta belong to
K[v] and the return
\[
M[x+Tv,\zeta,2vx+Tv^2]=M[v]
\quad\text{for every extension }M/K\text{ and }T\in M
\tag{13}
\]
holds. Then it is impossible that
\[
\deg x=\deg\zeta=n\ge2.
\tag{14}
\]
Here both degrees refer to the same polynomial parameter v.

To prove this, write a=lc(x) and c=lc(zeta), both nonzero. In two
independent variables U,V form
\[
F(U,V)=x(U)+x(V),\qquad
G(U,V)=\frac{\zeta(U)-\zeta(V)}{U-V}\in K[U,V],
\qquad \mathcal R(V)=\operatorname{Res}_U(F,G).
\tag{15}
\]
The quotient defining G is a polynomial, including on the diagonal.
The U-degrees of F,G are n and n-1, with leading coefficients a,c
that do not depend on V. We claim
\[
\deg_V\mathcal R=n(n-1),\qquad
\operatorname{lc}_V\mathcal R=(2a)^{n-1}c^n\ne0.
\tag{16}
\]

Here is an all-n proof that also accounts for every lower coefficient.
Substitute U=Vz. The polynomials V^(-n)F(Vz,V) and
V^(-(n-1))G(Vz,V) have coefficients polynomial in V^(-1), with
constant terms respectively
\[
a(z^n+1),\qquad c\sum_{j=0}^{n-1}z^j.
\tag{17}
\]
The change of polynomial variable multiplies the resultant by
V^(n(n-1)); scaling the two polynomials as displayed divides their
resultant by V^(2n(n-1)). It follows that V^(-n(n-1))*R(V)
is a polynomial in V^(-1), whose constant coefficient is the
resultant of(17).

For completeness, let rho run through the n roots of z^n+1 over an
algebraic closure. None equals one, and
\[
\sum_{j=0}^{n-1}\rho^j=-\frac2{\rho-1},\qquad
\prod_{\rho^n=-1}(\rho-1)=(-1)^n2.
\tag{18}
\]
Their product therefore equals 2^(n-1). Multiplying by a^(n-1)c^n
proves(16). This also proves that lower terms cannot cancel the
claimed leading coefficient.

Let M be an algebraic closure of K. The nonconstant polynomial R has
a root v2 in M. Because the two U-leading coefficients in(15) remain
the nonzero constants a,c at every specialization, the vanishing
resultant gives a FINITE common root v1 in M of F(U,v2),G(U,v2).
There is no root-at-infinity alternative caused by a degree drop.

First suppose v1 and v2 are distinct. Put
\[
T=-\frac{x(v_1)-x(v_2)}{v_1-v_2}.
\tag{19}
\]
Then x+Tv has the same value at the two points; G=0 gives the same
value of zeta, and F=0 gives x(v1)+x(v2)=0. The exact third-output
difference is
\[
\begin{aligned}
&2v_1x(v_1)-2v_2x(v_2)+T(v_1^2-v_2^2)\\
&=(v_1+v_2)\{x(v_1)-x(v_2)+T(v_1-v_2)\}
 +(v_1-v_2)\{x(v_1)+x(v_2)\}=0.
\end{aligned}
\tag{20}
\]
All three generators in(13) take equal values at distinct points.
They cannot generate M[v], because v itself separates those points.

Now suppose v1=v2=w. The two equations become
\[
x(w)=0,\qquad \zeta'(w)=0.
\tag{21}
\]
Choose T=-x'(w). All three generators in(13) then have zero
v-derivative at w: for the third one the derivative is
2x(w)+2w(x'(w)+T)=0. If v were a polynomial in these generators,
the chain rule would force its derivative 1 to vanish at w. This is
again impossible. Thus(14) contradicts(13), proving the lemma with
both the distinct-point and repeated-root boundaries included.

## 4. Application and the constant-zeta boundary

Apply the lemma to the exact return(6). If the common degree in(11)
were three, (12) would give deg(x)=deg(zeta)=3, impossible. Hence
deg(x)=deg(q)=2. If zeta had degree two, the lemma with n=2 would
again give a contradiction. It follows that
\[
\deg_vx=2,\qquad \zeta\in L[v]\text{ has degree at most one}.
\tag{22}
\]

Suppose zeta is constant. In(6) take T=0 and M=L. It would give
\[
L[x,2vx]=L[v],\qquad \deg x=2,\quad \deg(2vx)=3.
\tag{23}
\]
Here is the complete elementary obstruction for this quadratic/cubic
pair. Translate v to a parameter w over L to remove the linear term
of x. Scaling and subtracting its constant then give L[x]=L[w^2].
Write the cubic 2vx in w and subtract its even part, which belongs
to L[w^2]. Its remaining odd part is w(Aw^2+B) with A nonzero.
The square of this odd polynomial is in L[w^2], so the entire
generated ring is exactly
\[
L[w^2,\ w(Aw^2+B)]
=L[w^2]\mathbin{\oplus}w(Aw^2+B)L[w^2].
\tag{24}
\]
Its odd part cannot contain w, since Aw^2+B is a nonunit of L[w^2].
This includes B=0 and requires no square root of the leading
quadratic coefficient. Thus(23) is impossible.

Combining this with(22) proves the stated necessary reduction:
\[
\boxed{\deg_{v_0}\sigma=1\quad\Longrightarrow\quad
\deg_{v_0}x=2,\qquad
\deg_{v_0}(\theta+\sigma^2+f'\sigma)=1.}
\tag{25}
\]
In the parameter v=sigma it can be written
x=A v^2+Bv+C and zeta=Dv+E with A,D in L* and B,C,E in L.
This description is only intrinsic. In particular D being a unit
of L does not make zeta an original ambient coordinate over C.

## 5. Verification and dependency boundary

The current458 source was read completely before using its complete
third relation and original all-parameter return. Its arbitrary-n
formula and return are retained with their entire actual264 pedigree;
this is not a recursive certification of that pedigree.

Fresh unsaved032b34 reconstructs(8),(9) from the full(5), with zero
residual, and confirms the exact cubic leading coefficient f'''/6.
It independently checks(20) and the diagonal third derivative in(21).
For n=2,3, symbolic resultants with arbitrary lower coefficients have
exact degree n(n-1) and the leading coefficient(16). Homogeneous
controls for n=2 through8 match(18). These controls supplement the
written all-n proof; they do not replace it.

No fourth-potential coefficient gate, unheld degree classification,
or coefficient-field rationality is used. The result does not exclude
affine sigma, assert that sigma is always affine, or recognize A.
Every scalar extension and parameter change above is explicitly over
the coefficient field and is not promoted to an actual polynomial
automorphism over C.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited, and no unrestricted cancellation,
historical novelty or formal-certification claim is made.
