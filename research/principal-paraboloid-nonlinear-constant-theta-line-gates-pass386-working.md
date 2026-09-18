# Constant theta forces an intrinsic line presentation

Working necessary reduction: retain the complete actual264 chart,
with k=s and n_ss nonzero. If theta belongs to the exact coefficient
field L, sigma is an affine intrinsic parameter and y is affine in
sigma. Its slope satisfies exact first differential gates obtained
from the genuine potentials and the full calibrated determinant.

This is not exclusion or recognition of this boundary. The zero
slope is retained. An intrinsic parameter over L is not asserted to
be a coordinate of the original polynomial ring.

## 1. Actual retained entry and the highest potential terms

Retain all actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the genuine full potentials of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md).
Thus B=C[X,Y,Z,W]=A0[u] with original slice derivation E_slice,
exact degrees (1,2,2,2), and full initial kernel (X^2Z-Y^2).
The selected nonzero derivation is N=[u^4]partial_Z restricted to A0.
Its exact coefficient field L is finite over C(t,s), and
\[
O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
K=L(v)=\mathbb C(y,z,w),\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\tag{1}
\]
The literal rows and first two potentials are exactly those of264
with k=s. The original-ring hypotheses, both returns and the
calibrated nonzero scalar are not replaced by a formal conic.

Assume
\[
\theta=h\in L,\qquad e=n_{ss}\ne0,
\qquad \nu=n_s,\quad b=n_{ts},\quad a=n_t.
\tag{2}
\]
Here h denotes the constant-in-v theta, not the third potential
level. That level will be denoted h0. By366, sigma is nonconstant;
put d=deg_v sigma. The monic-y quadric first gives deg_v y<=d:
otherwise its y-squared term would have uniquely greatest degree.
Define the leading ratio, allowing zero, by
\[
\lambda=\frac{[v^d]y}{[v^d]\sigma}\in L.
\tag{3}
\]
The highest terms of the complete third and fourth potentials give
\[
\lambda^2-2\nu\lambda+\frac{n_{tt}}2=0,
\qquad n_{ttt}=12b\lambda.
\tag{4}
\]
Indeed the only terms of degree 2d in the third relation are
y^2-2nu*sigma*y+(n_tt/2)*sigma^2. The only terms of degree
3d in the fourth are -2b*sigma^2*y+(n_ttt/6)*sigma^3.
Terms containing theta have smaller degree because theta is in L.
These comparisons are valid when lambda=0 as well.

Set Delta=lambda-nu. It is nonzero. To see this, if Delta=0,
(4) gives n_tt=2nu^2 and n_ttt=12b*nu. Differentiating the
first identity in t instead gives n_ttt=4nu*b. Since nu_s=e
is nonzero, nu is nonzero, so b=0. But then differentiating
n_tt=2nu^2 in s gives b_t=4nu*e, a contradiction. Thus
\[
\boxed{\Delta\ne0.}
\tag{5}
\]
Differentiating the first equality of(4) in t and using its second
equality also gives, without division by lambda,
\[
\boxed{\Delta\lambda_t+2b\lambda=0.}
\tag{6}
\]

## 2. Factor the sliced quadric over the retained field

Let U,P be independent formal variables. In the genuine third
potential substitute V=h but do not discard any other coefficient:
\[
\begin{aligned}
H_h(U,P)={}&U^2+(a-2\nu P)U+\frac{n_{tt}}2P^2
 +(bh-\ell_t-\nu a)P\\
&+\frac e2h^2-(\ell_s+\nu^2)h+\nu\ell-h_0.
\end{aligned}
\tag{7}
\]
It vanishes at(y,sigma). Define elements of L
\[
p=\frac a2+\frac{bh-\ell_t}{2\Delta},\qquad q=a-p.
\tag{8}
\]
Direct multiplication and(4) give
\[
H_h(U,P)=
(U-\lambda P+p)(U-(2\nu-\lambda)P+q)+C_0,
\quad C_0\in L.
\tag{9}
\]
This uses no coefficient-field square root or algebraic extension.
The evaluated second factor has degree d and leading coefficient
2Delta*[v^d]sigma, hence is nonconstant. Its product with the first
factor is a scalar. In the polynomial ring L[v], this forces the
product scalar to be zero and the first factor to vanish. Therefore
\[
y=\lambda\sigma+r,\qquad
r=-\frac a2+\frac{\ell_t-bh}{2\Delta}\in L.
\tag{10}
\]
Whole-ring return now gives O=L[sigma], so
\[
\boxed{\deg_v\sigma=1,\qquad
\tau:=N\sigma\in L^*,\qquad O=L[\sigma].}
\tag{11}
\]
The product argument uses the sliced polynomial identity, not a
misapplied full-surface gradient statement.

## 3. A high scalar coefficient retains both slope branches

Use P=sigma as the independent intrinsic parameter. The exact
coefficient partials now fix P and still have their original action
on L. This affine intrinsic change gives
\[
J_{t,s,P}(X)=-a_0^4/\tau\in L^*.
\tag{12}
\]
The same original literal rows become
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+2t(\lambda P+r)+h+n+(2tP+s)X+t^2X^2,\\
W&=-2\lambda P^2-(2r+n_t)P+\ell-\nu h+hX+sX^2.
\end{aligned}
\tag{13}
\]
Expand their full determinant with columns t,s,P. Its cubic-in-P
coefficient, independent of X, and its X*P^2 coefficient are
\[
\begin{aligned}
[P^3X^0]J&=-2\{(n_{tt}-2\lambda^2)\lambda_s-b\lambda_t\}
          =8\lambda\Delta\lambda_s+2b\lambda_t,\\
[P^2X]J&=-2(\Delta\lambda_t+2b\lambda).
\end{aligned}
\tag{14}
\]
The second vanishing agrees with(6), and is not an independent
additional equation. By(6), the first coefficient vanishes only if
\[
\lambda\bigl(2\Delta^2\lambda_s-b^2\bigr)=0.
\tag{15}
\]
Consequently if lambda is nonzero, necessarily
\[
\boxed{\lambda_s=\frac{b^2}{2\Delta^2},\qquad
\lambda_t=-\frac{2b\lambda}{\Delta}.}
\tag{16}
\]
No assertion is made that this system has been solved.

If lambda=0 instead, then n_tt=0 by(4). In this branch the full
coefficient [P^2 X^0]J reduces to 2b*r_t. Hence one obtains only
\[
\boxed{\lambda=0\quad\Longrightarrow\quad n_{tt}=0,
\qquad b r_t=0.}
\tag{17}
\]
The alternatives b=0 and r_t=0 are both retained. In particular
(16) cannot be applied after dividing by a zero lambda.

## 4. Evidence and remaining boundary

The original chart264 and complete potentials365 were fully reread
in2d20f9 and40df39/5b492d. The independent constant-sigma input366
was fully reread in3deca0/9a8095. The argument here needs no result
about the nonzero-E family or its coefficient field F.

Fresh unsaved10d969 rebuilt the full determinant of(13) with
independent coefficient functions, obtaining all coefficients of
P-degree at least two. Fresh ce5fcf checked that the remainder
in(9) is independent of U,P, and checked the reduction of(14)
to(15). These are exact polynomial identities, not finite sampling.
The degree and whole-return arguments are the written proofs.

The result gives a necessary intrinsic line form and differential
gates. It neither excludes this case nor descends P to an actual
coordinate of A0. The remaining scalar coefficients and the original
ring return still constrain it. No unrestricted cancellation,
novelty, human-expert or proof-assistant certification is claimed.
No saved checker was executed, imported, compiled or rerun, and no
held source or canonical index was edited.
