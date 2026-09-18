# Recognition of the selected-line quadratic-first branch

Working result: the selected-line alternative in333's nonzero-b,
complex-quadratic first-potential branch is recognized. The nonresonant
case supplies a literal polynomial LND with an E-stable actual three-ring.
The resonant case is excluded by the strong original invariant-field
return and an irreducible quadratic.

This includes the selected lines with \(\kappa=0\), without a separate
cubic shear or a three-good theorem. It does not assert arbitrary-chart
entry or address the genuine-conic alternative \(\mathcal A\ne0\).

## 1. Exact branch, flattening, and coefficient constants

Retain all actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and the
fully read reduction
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
O=L[v]=L[y,\sigma,\theta],\qquad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here N remains the actual selected shift-four part of the literal
Z-partial. All intrinsic coefficients are E-invariant. Assume
\(k=s,n=gt^2\), with \(g\in\mathbb C^*\), and the alternative
\(\ell_s\ne0,\ell_{ss}=0\) of333. Its exact notation is
\[
r=\ell,\qquad s=H=cr+d(t),\qquad
\mathcal L=b(t)r+e(t),\qquad
c\in\mathbb C^*,\quad b,d,e\in\mathbb F,
\tag{2}
\]
where \(\mathbb F=\ker_L\partial_r\) is finite over
\(\mathbb C(t)\), with exact t-derivative constants \(\mathbb C\).
These are commuting coefficient partials, not rational parameter
assumptions. In this note \(b\ne0\).

Put \(x=y+gt\), \(\kappa=1+gc\), and \(h=\kappa/b\).
The quadratic-top relation retained from333 is
\[
d''=2gb-2\kappa^2/b.
\tag{3}
\]
Its full plane primitive, after the formal L-linear substitution
\(U=x-h\sigma\), is
\[
\Phi=-bU^2+d'U+\mathcal A\sigma,
\qquad \mathcal A=hd'-b'r-e',\qquad \Phi=q\in L.
\tag{4}
\]
The coefficient derivatives are taken before the formal substitution.
The selected-line branch addressed here is precisely
\(\mathcal A=0\).

Since every term of \(hd'-e'\) belongs to \(\mathbb F\), applying
\(\partial_r\) to \(\mathcal A=0\) gives \(b'=0\). Exact constants
therefore give
\[
\begin{gathered}
b\in\mathbb C^*,\quad h\in\mathbb C,\quad \kappa=bh,\\
d=d_2t^2+d_1t+d_0,\quad d_2=b(g-h^2),\qquad
e=hd+e_0,\qquad d_i,e_0\in\mathbb C.
\end{gathered}
\tag{5}
\]
No division by h or kappa occurs. The identity \(\mathcal A=0\)
was used to integrate \(e'=hd'\) only after h was shown constant.

A nonconstant polynomial in v is transcendental over L. Since (4)
has nonzero quadratic coefficient \(-b\), its evaluated U belongs
to L. Write
\[
x=h\sigma+\zeta,\qquad \zeta\in L,
\qquad O=L[\sigma]=L[v].
\tag{6}
\]
The equality follows from the whole plane return in333. Its selected
full equation is \(U-\zeta\); the unit-cofactor identity gives
\[
\eta=d'-2b\zeta\in L^*.
\tag{7}
\]
In particular a double selected root is not allowed. The level q,
and hence zeta, is not presumed to belong to \(\mathbb F\).

## 2. Complete actual map and scalar calibration

In the exact separating coefficient variables (t,r), and with P the
affine intrinsic parameter sigma, the first three potentials give
\[
\begin{aligned}
x&=hP+\zeta,& y&=x-gt,\\
\theta&=c(x^2+gP^2)+d'P-br-hd-e_0,\\
z&=2tx-gt^2+P^2+\theta,&w&=r-2Px,\\
Y&=y+PX+tX^2,&
Z&=z+(2tP+cr+d)X+t^2X^2,\\
W&=w+\theta X+(cr+d)X^2.
\end{aligned}
\tag{8}
\]
The change from the original parameters (t,s,v) has inverse determinant
\(c/(N\sigma)\), since \(s_r=c\) and sigma is affine in v.
Consequently the complete actual determinant in this parameterization is
\[
J_{t,r,P}(X)=-\frac{a_0^4c}{N\sigma}\in L^*.
\tag{9}
\]
All moving coefficients of sigma contribute only off-diagonal terms
to this triangular parameter change. In particular (9) is independent
of both X and P.

Here is a row derivation retaining every X-coefficient. Differentials
hold X fixed. Set
\[
F=\theta_P=2chx+2cgP+d',\qquad
\mathrm d\theta=F\,\mathrm dP+2cx\,\mathrm d\zeta
 +(d''P-hd')\,\mathrm dt-b\,\mathrm dr.
\tag{10}
\]
Start with the determinant-preserving row subtraction
\(\mathsf A=\mathrm dY,\mathsf B=\mathrm dZ-2t\,\mathrm dY,
\mathsf C=\mathrm dW\). The full rows from (8) are
\[
\begin{aligned}
\mathsf A={}&(X+h)\,\mathrm dP+\mathrm d\zeta+(X^2-g)\,\mathrm dt,\\
\mathsf B={}&(2P+F)\,\mathrm dP+2cx\,\mathrm d\zeta
 +[2x+d''P-hd'+X(2P+d')]\,\mathrm dt+(cX-b)\,\mathrm dr,\\
\mathsf C={}&[-2(x+hP)+XF]\,\mathrm dP+[-2P+2cXx]\,\mathrm d\zeta\\
&+[X(d''P-hd')+X^2d']\,\mathrm dt+(1-bX+cX^2)\,\mathrm dr.
\end{aligned}
\tag{11}
\]
Use the complex identities \(bh=1+gc\) and
\(d''=2b(g-h^2)\) from (5). Direct row operations give
\[
\begin{aligned}
\mathsf C_1&=\mathsf C-X\mathsf B+2P\mathsf A
 =\mathrm dr-2x\,\mathrm dP-2(Xx+gP)\,\mathrm dt,\\
\mathsf B_2&=\mathsf B-2cx\mathsf A-(cX-b)\mathsf C_1
 =\eta\bigl(\mathrm dP+(X-h)\,\mathrm dt\bigr).
\end{aligned}
\tag{12}
\]
The transformation to \((\mathsf A,\mathsf B_2,\mathsf C_1)\)
has determinant one. For \(Q_0=\mathrm dP+(X-h)\,\mathrm dt\),
the remaining subtractions are
\[
\mathsf A-(X+h)Q_0=\mathrm d\zeta+(h^2-g)\,\mathrm dt,
\qquad
\mathsf C_1+2xQ_0
=\mathrm dr-2[(g+h^2)P+h\zeta]\,\mathrm dt.
\tag{13}
\]
Thus the entire determinant is
\[
\boxed{J_{t,r,P}(X)
=-\eta\bigl(2(g+h^2)\zeta_rP
       +\zeta_t-g+h^2+2h\zeta\zeta_r\bigr).}
\tag{14}
\]
This identity is independent of X before any remaining scalar condition
is imposed. The nonzero calibration (9) and \(\eta\ne0\) imply
\[
(g+h^2)\zeta_r=0.
\tag{15}
\]

## 3. Nonresonance gives a literal polynomial LND and an actual three-ring

Suppose \(g+h^2\ne0\). Then \(\zeta_r=0\), hence
\(\zeta\in\mathbb F\). Differentiating the complete map (8) in r
at fixed t,P,X gives
\[
\partial_r(X,Y,Z,W)=(0,0,cX-b,1-bX+cX^2).
\tag{16}
\]
The right side defines the actual polynomial LND
\[
\Delta=(cX-b)\partial_Z+(1-bX+cX^2)\partial_W
\quad\text{on }\mathcal B.
\tag{17}
\]
Its coefficients belong to \(\mathbb C[X]\), which it fixes.
The derivation of K(X) obtained by extending \(\partial_r\) and
fixing X agrees with (17) on all original generators, so it is exactly
Delta. In particular \(\Delta K\subset K\) and
\(\Delta A\subset\mathcal B\cap K=A\).

Make the actual polynomial reframe
\[
S=XZ-W,\qquad Q=Z+(cX-b)S.
\tag{18}
\]
Both inverse orders are furnished by
\[
Z=Q-(cX-b)S,\qquad
W=XQ-(cX^2-bX+1)S.
\tag{19}
\]
Thus \(\mathcal B=\mathbb C[X,Y,Q,S]\),
\(\Delta S=-1\), and \(\Delta Q=0\). Its actual kernel is
\(R=\mathbb C[X,Y,Q]\).

For completeness, an LND of \(A[u]\) preserving A commutes with
\(E=\partial_u\). Indeed its exponential and inverse preserve
\(A[z]\). The image of u under that automorphism of \(A[z][u]\)
is affine in u with a unit linear coefficient. Units of the domain
\(A[z]\) belong to \(A^*\), and specialization at z=0 makes that
coefficient one. The derivative at z=0 therefore gives
\(\Delta u\in A\), proving the asserted commutation on A and u.
This is the elementary argument fully recorded in339 Section4.
It does not assume the original E-speed is independent of r.

Consequently R is E-stable. Its restriction is a nonzero LND with
actual coordinate X of degree one. Dividing its three coefficients
by their gcd preserves local nilpotence and this degree: the gcd
divides \(EX\in\ker E\), so is invariant by factorial closure.
The resulting irreducible LND meets the exact hypotheses of
[Dasgupta--Gupta, Theorem4.8, restating Daigle](https://arxiv.org/html/1701.03635v1).
An invariant coordinate of R remains an actual coordinate after
adjoining S. The original sliced kernel is regular, so
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives \(A\cong\mathbb C^{[3]}\).

This proof never divides by h or kappa. In particular it includes
\(\kappa=0\): then h=0 and \(g+h^2=g\ne0\), so (15) still applies.
No three-good working recognition theorem is used in this branch.

## 4. Resonance contradicts the strong original field return

Now suppose \(h^2=-g\). Then \(h\ne0\) and
\(\kappa=bh\ne0\). The complex formulas (5) read
\[
b=\kappa/h,\qquad c=(1-\kappa)/h^2,
\qquad d=-2\kappa h t^2+d_1t+d_0,
\qquad e=hd+e_0.
\tag{20}
\]
No condition on \(\zeta_r\) is assumed. Define elements of K by
\[
R_1=\sigma-ht,\qquad
Z_0=z+bw-cy^2+hd_0+e_0.
\tag{21}
\]
These are intrinsic expressions, not claimed ambient coordinates.
The complete intercepts (8) give the exact identity
\[
\boxed{Z_0=\kappa R_1^2+(d_1-2by)R_1.}
\tag{22}
\]
Here is an elimination that retains every constant. With
\(x=y-h^2t\), the w identity gives
\(r=w+2(y-h^2t)\sigma\). The z and theta identities then give
\[
\begin{aligned}
z+bw-cy^2+hd_0+e_0
={}&\kappa\sigma^2+(d_1-2by-2\kappa ht)\sigma\\
&+\kappa h^2t^2+(2\kappa y-hd_1)t,
\end{aligned}
\tag{23}
\]
which is exactly (22).

The intercept change in (21) has the polynomial inverse
\(z=Z_0-bw+cy^2-hd_0-e_0\). Therefore both field inclusions in the
strong actual return give
\[
K=\mathbb C(y,z,w)=\mathbb C(y,w,Z_0).
\tag{24}
\]
The three displayed generators are algebraically independent over
\(\mathbb C\), since K has transcendence degree three.
However \(R_1\in K\) solves the quadratic
\[
\kappa T^2+(d_1-2by)T-Z_0=0.
\tag{25}
\]
Over \(\mathbb C(y,w)(Z_0)\), its discriminant is
\((d_1-2by)^2+4\kappa Z_0\). This polynomial has degree one in
the independent Z0 and has a simple zero because \(\kappa\ne0\).
Its corresponding discrete valuation is odd, so it cannot be a
rational square. In characteristic zero the quadratic (25) is therefore
irreducible over the entire field (24), contradicting \(R_1\in K\).

Thus resonance is impossible. This uses the actual strong field
return, not just the relative polynomial line over L or a nonzero
formal Jacobian. It makes no rationality assertion about \(\mathbb F\).

## 5. Conclusion and boundary

Every selected line with \(\mathcal A=0\) and b nonzero in the actual
branch (1)--(4) is now covered: \(g+h^2\ne0\) is recognized by an
actual preserved three-ring, and \(g+h^2=0\) is excluded. No existence
of frames in the recognized branch is asserted.

The b=0 case is a separate339 result. The genuine-conic branch
\(\mathcal A\ne0\) is not included in this proof. The assumptions
\(k=s,n=gt^2\) with complex nonzero g, the full principal initial
kernel, the calibrated scalar, and both actual returns are retained.
There is no normalization of arbitrary potentials or unrestricted
cancellation conclusion.

The complete direct sources264,333 and339 were read, with the exact
primary three-variable and regular-kernel statements freshly inspected
in337. Fresh unsaved algebra independently reconstructed the entire
scalar (14), the field-derivative row (16), both actual inverse orders
(19), and the complete resonant identity and intercept inverse
(22)--(24). The row proof and irreducibility argument above are the
mathematical deductions; those finite calculations do not certify
universal field or descent claims. No saved checker was executed,
imported, compiled, or rerun. No retained source or canonical index
was edited.
