# Affine acceleration in the dependent constant-top cubic case

The dependent-defect cubic boundary has a simpler preceding layer than
the independent-defect cubic boundary. Its entire acceleration vector
is affine in one actual polynomial slice. After subtracting that slice
from the two bad velocities, the residual velocities lie on a
polynomial curve whose tangent direction cannot be constant.

This is a normal-form reduction, not a recognition theorem for the
whole cubic case. In particular, an actual polynomial slice is not
asserted to be an ambient coordinate.

## 1. Hypotheses and notation

Let
\[
B=k[x_1,x_2,X,Y]=A[s_*],\qquad k=\mathbb C,\qquad
E(s_*)=1,\qquad A=\ker E.
\]
Assume \(E\in\operatorname{LND}_k(B)\).
Write \(x=(x_1,x_2,X,Y)^t\), \(P=Ex\), \(J=\operatorname{Jac}P\),
and \(T_i=\partial_{x_i}\), with \(x_3=X,x_4=Y\).
Assume the actual adjoint bounds
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
The two defects have rank one and no complex constant relation:
\[
V_3=aD,\qquad V_4=bD,\qquad
D\text{ a primitive polynomial LND},\qquad
[E,D]=0,\qquad a,b\in\ker E\cap\ker D.
\tag{2}
\]
Here \(a,b\ne0\). The primitive decomposition is the one proved in
[pass42](dependent-quadratic-defects-pass42.md).
Suppose specifically that
\[
E^3x=c\in k^4\setminus\{0\},\qquad E^4x=0.
\tag{3}
\]
The highest-column theorem in
[pass65](dependent-low-flow-pass65.md#2-two-full-highest-identities-kill-the-bad-top)
gives \(c_3=c_4=0\). Thus \(T_c=c_1T_1+c_2T_2\) is a genuine nonzero
constant good partial.

Put \(h_2=E^2x\), \(d=D(x)\), \(\ell=(0,0,a,b)\), and
\(f=EX,g=EY\). All ranks below are over \(\operatorname{Frac}B\).

## 2. The five-dimensional companion has a rank-one square

Use the actual weighted companion
\[
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix},\qquad
\mathcal C(t)=I-tJ+t^2d\ell/2.
\tag{4}
\]
The inverse-Jacobian identity gives
\[
\det(I-tM)=1,\qquad M^5=0,\qquad
(M^j)_{\mathrm{UL}}=\frac{\operatorname{Jac}(E^jx)}{j!}.
\tag{5}
\]
These are pointwise matrix identities. No ordinary derivative of
\(\ell\) has been discarded.

For completeness, the rank-preserving block argument applies because
\(d\ne0\) and \(\ell\ne0\). Neither the right nor the left kernel of
\(M\) contains a nonzero vector supported only on the last coordinate.
If \(MN=NM=0\), deleting the last column and then the last row of
\(N\) preserves its rank: the row restriction and column projection
are injective on the relevant kernels. Hence
\(\operatorname{rank}N=\operatorname{rank}N_{\mathrm{UL}}\).

Starting with \(M^5=0\), the zero upper-left block of \(M^4\)
therefore gives \(M^4=0\). Since \(E^3x=c\) is constant, the zero
upper-left block of \(M^3\) next gives \(M^3=0\). The same block lemma
then identifies the rank of \(M^2\) with the rank of
\(\operatorname{Jac}h_2\).

The actual velocity identity gives
\[
M^2\binom P0=\binom{c/2}{\ell h_2}\ne0.
\tag{6}
\]
For example, its top row follows from the quadratic coefficient of
\(\mathcal C(t)P(\exp(tE)x)=P\):
\(Jh_2-d(\ell P)/2=c/2\).
A cubic-zero matrix of size five has at most one Jordan block of
size three. Since (6) is nonzero, this proves
\[
\operatorname{rank}M^2
=\operatorname{rank}\operatorname{Jac}h_2=1.
\tag{7}
\]
The possible Jordan types are \((3,2)\) and \((3,1,1)\).
Neither one is selected without further hypotheses.

## 3. The complete acceleration is affine in an actual slice

Since \((\operatorname{Jac}h_2)P=c\), equation (7) says that the
image of \(\operatorname{Jac}h_2\) is precisely the field line \(kc\),
where the line is understood over \(\operatorname{Frac}B\).
Choose \(j\in\{1,2\}\) with \(c_j\ne0\), and set
\(\sigma=(h_2)_j/c_j\). Every ordinary partial kills
\(h_2-c\sigma\). The constants of all four ordinary partials are \(k\).
Consequently, for one fixed vector \(e\in k^4\),
\[
h_2=c\sigma+e,\qquad e_j=0,\qquad E\sigma=1.
\tag{8}
\]
This is an equality in the original polynomial ring. It does not use
a rational or formal extension.

In particular, write \(e_B=(e_3,e_4)\). Then
\[
Ef=e_3,\qquad Eg=e_4,\qquad
\rho:=\ell h_2=ae_3+be_4.
\tag{9}
\]
The bad accelerations are complex constants, whereas the good
accelerations need not be constant.

## 4. Full lower rows constrain the residual velocities

The base columns of \(M^2\) are
\[
(M^2)_{\mathrm{base\ columns}}
=\binom{\operatorname{Jac}h_2/2}{\ell J}.
\]
Their image is the same rank-one line as the nonzero vector in (6).
Using (8), comparison of their top rows first fixes the scalar
multipliers, and comparison of their bottom rows then yields
\[
\ell J=\rho\,d\sigma.
\tag{10}
\]
The symbol \(d\sigma\) here is the ordinary differential row.
It is not the derivation coefficient vector \(d=D(x)\).

Define the actual polynomials
\[
F=f-e_3\sigma,\qquad G=g-e_4\sigma.
\tag{11}
\]
Equations (9)--(10) become
\[
EF=EG=0,\qquad a\,dF+b\,dG=0.
\tag{12}
\]
In particular, \(F,G\) are algebraically dependent. If their
differentials were independent, the nonzero pair \(a,b\) could not
satisfy (12).

There is also an exact leading-field invariance statement. For
\(i=1,2\), the good cubic coefficient of
\((T_i+tW_i)(\exp(tE)x)\) gives \(W_i h_2=0\), hence
\(W_i\sigma=0\). Its bad quadratic components give \(W_i f=W_i g=0\),
because \(e_3,e_4\) are constant. For \(j=3,4\), the bad quartic
coefficient gives \(V_jh_2=0\); the bad cubic components give
\(V_jf=V_jg=0\). Dividing a nonzero multiplier proves
\[
D\sigma=DF=DG=0,\qquad
W_i\sigma=W_iF=W_iG=0\quad(i=1,2).
\tag{13}
\]
No restriction of the original slice to \(\ker D\) is presumed;
(13) is proved from the actual coefficients.

If at least one of \(F,G\) is nonconstant, polynomial curve
factorization applied to \(k[F,G]\) supplies an actual polynomial
\(u\in B\) and univariate polynomials \(p,q\in k[U]\) such that[^curve]
\[
F=p(u),\qquad G=q(u),\qquad
Eu=Du=W_1u=W_2u=0.
\tag{14}
\]
The invariance follows by differentiating whichever nonconstant
polynomial in (14) is available. Equation (12) gives
\[
a\,p'(u)+b\,q'(u)=0.
\tag{15}
\]
Both derivatives are nonzero. Otherwise (15), \(a,b\ne0\), and
nonconstancy of the pair would contradict each other.
Moreover \(p'/q'\) is nonconstant: a constant ratio in (15) would
be a forbidden complex constant relation between \(a,b\).
This is a condition on the residual curve's tangent direction,
not on the projective direction of the original velocities
\(e_B\sigma+(p(u),q(u))\).

## 5. Recognition endpoints and exact remaining scope

If \(e_B=0\), then \(\rho=0\). Applying \(M\) to (6) gives
\(Jc=\rho d=0\). Therefore
\[
[E,T_c]=0.
\tag{16}
\]
There remains a complementary actual good partial. The
[one-good-output recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
applies with constant denominator one and rational coefficient zero.
It recognizes the original kernel \(A\simeq k^{[3]}\).

If \(F,G\) are both constant and \(e_B\ne0\), the nonzero linear
coordinate \(L=e_4X-e_3Y\) has constant derivative
\(EL=e_4F-e_3G\). A zero derivative gives an actual invariant
coordinate and the inherited regular-kernel theorem. A nonzero
derivative makes a scalar multiple of \(L\) an ambient coordinate
slice. In the latter case the slice theorem identifies
\(A\simeq B/(L)\simeq k^{[3]}\). Thus this alternative is also
recognized.

After these endpoints, any still-unrecognized instance in this
dependent constant-top cubic sector must have \(e_B\ne0\) and the
nonconstant residual curve (14)--(15). The polynomial \(\rho\)
is then nonzero, since a zero value in (9) would be a constant
relation between the defects.

No proof here makes \(\sigma\) or \(u\) an ambient coordinate.
The note does not recognize that residual sector, assert its
realizability, or change the universal frame-existence obligation.
It does not address the separate independent-defect cubic normal form.

## Sources and verification scope

The matrix construction and block argument are inherited from
[the weighted companion proof](dependent-defect-top-line-pass43.md#1-actual-hypotheses-and-the-weighted-companion)
and are reconstructed in Sections 2--4. The constant bad top is the
full highest-column result of pass65. The recognition endpoints retain
the complete source obligations of the linked one-good-output lemma
and invariant-coordinate theorem.

[^curve]: Michiel de Bondt,
[*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4),
Corollary 3.2 and Lemma 3.3, PDF pp. 20--21. The finite polynomial
subalgebra here has transcendence degree one. Its parameter is a
polynomial of the original ring, not a claimed ambient coordinate.

This is a written conditional derivation. Finite symbolic checks and
independent AI reviews, when recorded separately, do not replace a
formal proof or human expert review. No historical novelty, public
submission, external contact, or general cancellation solution is claimed.
