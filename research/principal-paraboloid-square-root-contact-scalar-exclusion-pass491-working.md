# The normalized square-root contact family has no calibrated scalar

Working result: the normalized necessary family supplied by490 is
incompatible with the full original scalar. Its zero exceptional factor
makes the literal Z differential divisible by a nonconstant intrinsic
linear polynomial. In the complementary case, two scalar coefficients
force a separating coefficient parameter to have constant cube.
This excludes only the actual branch reduced in489 and490; no recognition
or general cancellation claim is made.

## 1. Retained actual hypotheses and the precise normalized input

Retain every actual264 hypothesis, the genuine296 levels and minor units,
and the nonconstant-sigma birational projected-line entry of325, in the
form of474. In particular the original polynomial four-ring, global
slice, entire initial kernel, literal selected partial, both original-ring
returns and full nonzero calibrated scalar remain hypotheses. As usual,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
[L:\mathbb C(t,s)]<\infty,\qquad P=\sigma,\quad O=L[P],
\quad NP=\rho\in L^*,\\
y=\lambda P+r_{\rm old},\qquad \theta=\mu P+h_{\rm old},\qquad
w_{\rm int}=\omega P^2+b_{\rm old}P+c_{\rm old},\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
The original intercept \(x_0\) is not removed, and a0 is not assumed to
be a unit of the actual ring. The coefficient partials commute, with
joint constants exactly \(\mathbb C\). Intrinsic P is not the original
slice or an asserted ambient coordinate.

The branch under consideration retains variable \(m=k_s\), noncomplex
lambda and omega, nonzero \(\beta=\mathcal Dm\), and the noncomplex
contact parameter with \(\mathcal D\tau\ne0\). The held
[489](principal-paraboloid-transverse-contact-square-root-reduction-pass489-working.md)
reduces its high equations to an exact square-root family. The actual
normalization and further necessary scalar integrations of
[490](principal-paraboloid-transverse-contact-universal-normalization-pass490-working.md)
give, in the resulting actual frame,
\[
\begin{gathered}
s=r^2/2,\qquad k=tr,\qquad
\omega=w^2/2,\qquad \lambda=w/2,\qquad \mu=-rw,\\
\mathcal D=\partial_t|_r-w\partial_r|_t,\qquad
\mathcal Dw\ne0,\qquad r,w\in L^*.
\end{gathered}
\tag{2}
\]
Here r and w are existing coefficient-field elements, not adjoined roots
or ambient coordinates. The actual normalization is part of the490
input, not a field-valued coordinate substitution asserted in this note.
The complete490 source was read at SHA
8ebfd323d2fceb4f7486d02f68f6d9559dbfa921aacff3deff6ece5ff495f32a.
Its Section6 reapplies the high integrations in the normalized actual
frame with new constants; no old-frame constants are silently reused.

Set \(v=r+tw\). In the exact \((t,r)\) basis,
\[
\det\frac{\partial(w,v)}{\partial(t,r)}
=w_t(1+tw_r)-w_r(w+tw_t)=\mathcal Dw\ne0.
\tag{3}
\]
Thus \((w,v)\) is a separating basis of L, which is finite over
\(\mathbb C(w,v)\). Its exact extended partials commute. Write
\[
F_v=\ker_L\partial_w.
\]
Then \(F_v/\mathbb C(v)\) is finite, its v derivative has constants
exactly \(\mathbb C\), and w is transcendental over \(F_v\). These facts
also follow directly by differentiating minimal polynomials over the
rational two-variable field; the degrees of finite constant
subextensions are bounded by the degree of L. No equality
\(F_v=\mathbb C(v)\) or \(L=F_v(w)\) is assumed. In particular v is
nonzero and transcendental over \(\mathbb C\).

At fixed X, put \(\xi=P+t(X-\lambda)\). The complete original centered
rows and the normalized high integrations from490 are exactly
\[
\boxed{\begin{aligned}
Y&=(X+w/2)\xi+R,\\
Z&=\xi^2+v\xi+g(v),\\
W&=\frac{w^2}{2}\xi^2+(b-wvX)\xi+c+HX+\frac{v^2}{2}X^2,
\end{aligned}}
\tag{4}
\]
where
\[
\begin{aligned}
g(v)&=v^2/4+\alpha v/2-b_c/v+g_c,\\
b&=2wR-\alpha w^2/2-2q_cw+a_c,\\
H&=-2vR+\alpha wv/2+2q_cv+b_cw/v+t_c,\\
&\alpha,a_c,b_c,t_c,q_c,g_c\in\mathbb C,\qquad R,c\in L.
\end{aligned}
\tag{5}
\]
All six complex constants may be zero individually. All derivatives of
the lower functions R and c are retained. Their actual origin from the
potentials and affine intercepts is not replaced by free constant jets;
the identities below are necessary for every such origin.
For the exact notation match, \((a_c,b_c,t_c,q_c,g_c)\) denotes
490's new-frame \((A_-,B_-,T_0,Q_0,g_0)\). In that frame its equations
(20),(21) give \(R=b/(2w)+\alpha w/4-a_c/(2w)+q_c\);
solving for b and substituting in \(H=vL_0\) gives exactly (5).

The original slice and polynomial-line return imply that X and xi are
algebraically independent over L. The shift from P to xi has parameter
Jacobian one at fixed X. Equations (1)--(3) therefore give the precise
calibration
\[
\mathcal J:=J_{w,v,\xi}(X)
   =-\frac{r a_0^4}{\rho\,\mathcal Dw}\in L^*.
\tag{6}
\]
It is independent of X and xi, but may depend on both coefficient
parameters. No constant coefficient of the determinant will be
artificially set to zero.

## 2. The full raw determinant and its zero-safe first gate

Use primes for the exact v derivative on \(F_v\). The derivative matrix
of the full literal rows (4), with columns \((w,v,\xi)\), is
\[
\begin{pmatrix}
\xi/2+R_w&R_v&X+w/2\\
0&\xi+g'&2\xi+v\\
w\xi^2+(b_w-vX)\xi+c_w+H_wX&
(b_v-wX)\xi+c_v+H_vX+vX^2&
w^2\xi+b-wvX
\end{pmatrix}.
\tag{7}
\]
In particular the \(vX^2\) term in its third row is retained. Define
\[
\jmath=\frac{\alpha}{4}+\frac{b_c}{2v^2}\in F_v,
\qquad g'=v/2+2\jmath,\qquad
\jmath'=-b_c/v^3.
\tag{8}
\]
Substitute only the full b and H formulas in (5) into (7).
The entire coefficient of \(X^2\xi^0\) is
\[
[X^2]\mathcal J
   =4v\jmath\left(R_w-\frac v4-\jmath\right).
\tag{9}
\]
This identity includes arbitrary \(R_w,R_v,c_w,c_v\). It is a scalar
coefficient identity, not a new potential relation or a highest-degree
formal model. We split \(\jmath=0\) before dividing it.

## 3. The zero factor contradicts the scalar unit directly

If \(\jmath=0\), then \(\alpha v^2+2b_c=0\). Since v is
transcendental over \(\mathbb C\), both \(\alpha\) and \(b_c\) are zero.
Thus the literal Z row in (4) is
\[
Z=(\xi+v/2)^2+g_c.
\tag{10}
\]
Its entire derivative row in (7) equals
\[
(\xi+v/2)(0,1,2).
\tag{11}
\]
Consequently the whole determinant is divisible by \(\xi+v/2\) in
\(L[X,\xi]\). This nonconstant intrinsic polynomial cannot divide the
nonzero element of L in (6). This already excludes the zero-jmath
case with all lower functions R and c unrestricted. Equivalently the
determinant vanishes after the purely algebraic substitution
\(\xi=-v/2\); this is not an actual coordinate change or an assertion
about an original slice.

## 4. The nonzero factor and the complete next two coefficients

Assume \(\jmath\ne0\). Both v and jmath are now nonzero, so (9) gives
\(R_w=v/4+\jmath\). Subtracting the indicated existing element gives
\[
R=(v/4+\jmath)w+f+q_c,\qquad f\in F_v.
\tag{12}
\]
No primitive is adjoined and f is not assumed rational in v.
Equations (5) become
\[
\begin{aligned}
b&=(v/2+b_c/v^2)w^2+2fw+a_c,\\
H&=-v^2w/2-2vf+t_c.
\end{aligned}
\tag{13}
\]
The complex constants \(a_c,t_c,q_c,g_c\) remain unrestricted. They
cancel from the decisive coefficients; no zero or nonzero choice for
them has been imposed.

Define the exact field expression
\[
\Gamma
=vf+4v\jmath f'
   +w\left(\frac{v^2}{4}+\frac{b_c}{v}
                         -\frac{4b_c\jmath}{v^2}\right).
\tag{14}
\]
Expansion of the full matrix (7) after (12),(13), with both derivatives
of c still arbitrary, gives
\[
[X\xi]\mathcal J=\Gamma-c_w.
\tag{15}
\]
Hence the calibrated scalar forces \(c_w=\Gamma\).
Substitute only that equation into the entire next coefficient.
One obtains exactly
\[
\boxed{\begin{aligned}
[X]\mathcal J\big|_{c_w=\Gamma}
&=-2v\jmath^2\bigl((1+4\jmath')w+4f'\bigr)\\
&=-\frac{(2b_c+\alpha v^2)^2}{8v^6}
          \bigl((v^3-4b_c)w+4f'v^3\bigr).
\end{aligned}}
\tag{16}
\]
Here \([X]\) means the coefficient of \(X\xi^0\), not the whole
coefficient of X as a polynomial in xi. This formula retains the
remaining lower derivative \(c_v\); its cancellation follows from the
full determinant, and no equation for \(c_v\) or c itself was used.
Equations (7),(12),(13),(14) supply a direct reconstruction of both
(15) and (16). For example
\(R_v=(1/4+\jmath')w+f'\), and every v derivative in the third row
is taken with w fixed. Thus no moving-parameter derivative is omitted.

Both positive-X coefficients must vanish. Since \(v\jmath^2\ne0\),
(16) implies
\[
(1+4\jmath')w+4f'=0.
\tag{17}
\]
Its coefficients lie in \(F_v\), and w is transcendental over that
field. Consequently
\[
1+4\jmath'=0,\qquad f'=0.
\tag{18}
\]
But the explicit derivative in (8) now gives \(v^3=4b_c\).
Applying the exact v derivative to this equality gives \(3v^2=0\),
contrary to \(v\ne0\) in characteristic zero. This includes \(b_c=0\);
there was no division by \(b_c\), alpha, \(v^3-4b_c\), or \(f'\).
It contradicts the scalar without solving any further coefficients.

## 5. Bounded conclusion and reconstruction evidence

The split \(\jmath=0\) or \(\jmath\ne0\) is exhaustive. Hence no
full actual normalized family (2),(4),(5) can satisfy its calibrated
scalar. Composing only with the actual normalization and necessary
high integrations of490 excludes the noncomplex-contact,
\(\mathcal D\tau\ne0\) branch of489 under its complete retained
actual affine projected-line hypotheses.

This note does not treat other projected curves, the global chart-entry
problem, or arbitrary cancellation. It does not promote r,w,v,xi or f
to ambient coordinates. The exact finite coefficient fields and
original selected-partial speed rho are retained throughout. The proof
requires only a subset of the lower scalar equations; it leaves no
actual realization in this subcase, rather than constructing one from
the high family.

Fresh unsaved reconstruction3a0bfc gives the full general square-root
centered determinant. After the normalized high input,1b29a7 and76462e
rebuild the entire lower determinant and the two decisive coefficients.
The separate exact check83c4d0 starts before the R integration and
verifies (9), the whole (15),(16), and the exact zero-jmath row factor,
with every residual zero. The complete held490 input was read inb1f629;
fresh83a452 independently verifies both its high T equations, the h0
obstruction and both partial equations of its integrated input.
Independent reconstructions9028a7,1d1b30,22b755,ee5350 and1f64c9 match
the lower gates and both zero cases. No saved checker was
executed, imported, compiled or rerun. No earlier source or canonical
file was edited.
