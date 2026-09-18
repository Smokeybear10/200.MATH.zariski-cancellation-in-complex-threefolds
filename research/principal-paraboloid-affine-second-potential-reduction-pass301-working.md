# Plane entry and an affine-second-potential endpoint

Working result: in the actual principal chart264 with \(k=s,n=0\)
and \(\ell_s\ne0\), the last unused scalar coefficient gives a
genuine plane-line presentation and a quartic primitive. If additionally
\(\ell_{ss}=0\), an explicit polynomial automorphism lowers a bad
coordinate to time degree at most one, and the kernel is recognized.
The remaining sector has \(\ell_{ss}\ne0\) and selected plane
degree two or four, with the degree pairs recorded in Section6.

No argument here puts arbitrary nonzero coupling into \(k=s,n=0\).
The completed one-variable-potential sector298 is separate: it assumes
\(\ell_s=0\), whereas this note assumes \(\ell_s\ne0\).

## 1. Actual entry and exact plane return

Retain all actual hypotheses, full initial kernel and selected-partial
data of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md)
and [296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a_0=EX\ne0,\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad K=\operatorname{Frac}A=L(v),\quad Nv=1,\\
K=\mathbb C(y,z,w),\quad L[y,z,w]=L[v],\quad
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Coefficient partials extend exactly and initially fix v. Impose
\[
k=s,\qquad n=0,\qquad b_0:=\ell_s\ne0,
\qquad a_1:=\ell_t.
\tag{2}
\]
The literal formulas are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta,&w&=\ell-2\sigma y,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
The third and fourth formal potentials specialize to
\[
\begin{aligned}
\mathcal H&=U^2-a_1P-b_0V,&
\mathcal H(y,\sigma,\theta)&=h\in L,\\
\mathcal Q&=(-a_1+2b_0P)U-H_2(\ell;P,V)-h_tP-h_sV,&
\mathcal Q(y,\sigma,\theta)&=j\in L.
\end{aligned}
\tag{4}
\]
All derivatives in this display are the old coefficient partials.
The fourth potential follows directly from296's corrected gradient:
here \(F=0,m=1\), so its correction coefficient \(F_V/m\) is
zero. It also follows by differentiating the second line of (4)
along v and using the complete X-coefficient of the raw map.

Since \(b_0\ne0\), the first line solves
\(\theta=(y^2-a_1\sigma-h)/b_0\) polynomially over L. Thus
\[
\boxed{O=L[v]=L[y,\sigma].}
\tag{5}
\]
This is an actual generic polynomial-ring equality, not just an
equality of function fields.

The plane polynomial obtained by substituting
\(V=(U^2-a_1P-h)/b_0\) into \(\mathcal Q-j\) has an evaluated
gradient generating O. Indeed \(\mathcal H_V=-b_0\in L^*\),
and its two substituted derivatives are, up to this unit, the
\((U,V)\) and \((P,V)\) minors of the gradients of
\(\mathcal H,\mathcal Q\). The remaining minor is their
linear combination. The minor-unit conclusion of296 therefore
gives the asserted plane-gradient unit.

## 2. Coefficient parameter and the quartic primitive

Use \(r=\ell\) as a coefficient parameter, and write
\[
s=H(t,r),\qquad H_r=1/\ell_s\ne0,
\qquad \mathcal L=H_rh.
\tag{6}
\]
The new coefficient partials commute on the finite extension
\(L/\mathbb C(t,r)\). Put \(F=\ker_L\partial_r\); it is
finite over \(\mathbb C(t)\), with t-constant field \(\mathbb C\).
These statements concern exact algebraic fields, not a rational
ansatz for L. The literal intercepts become
\[
\boxed{
\theta=H_ry^2+H_t\sigma-\mathcal L,\quad
z=\sigma^2+H_t\sigma+H_ry^2+2ty-\mathcal L,\quad
w=r-2\sigma y.}
\tag{7}
\]

Multiply the substituted fourth potential by \(H_r\) and subtract
its formal constant term. The resulting plane polynomial is
\[
\boxed{
Q(U,P)=\frac{H_{rr}}2U^4+H_{tr}U^2P+\frac{H_{tt}}2P^2
       +2UP+H_tU-\mathcal L_rU^2-\mathcal L_tP,
\qquad Q(y,\sigma)=q_0\in L.}
\tag{8}
\]
Its evaluated gradient is still a unit ideal. To verify this
coefficient transformation explicitly, use
\[
\partial_t^{\rm old}=\partial_t-(H_t/H_r)\partial_r,
\quad\partial_s^{\rm old}=H_r^{-1}\partial_r,
\quad a_1=-H_t/H_r,\quad b_0=H_r^{-1},\quad h=\mathcal L/H_r
\]
in (4). The fourth-, third- and second-degree coefficients after
substitution are respectively
\(H_{rr}/2,H_{tr},H_{tt}/2,2,-\mathcal L_r\), and the linear
ones are \(H_t,-\mathcal L_t\), as in (8).

Let G be the full irreducible plane equation of (5). The gradient
unit implies the exact selected-factor identity
\[
\boxed{Q-q_0=\eta G+G^2R,\qquad \eta\in L^*,\ R\in L[U,P].}
\tag{9}
\]
In fact write \(Q-q_0=GJ\). Its evaluated gradient is divisible
by \(J(y,\sigma)\), which must be a unit \(\eta\); then
\(J-\eta\) belongs to the full ideal \((G)\).
No irreducibility of Q is assumed.

We will use two elementary plane-line facts. For a polynomial
plane presentation \(L[y,\sigma]=L[v]\), its full plane degree
is \(\max(\deg_vy,\deg_v\sigma)\). A generic linear projection
proves this by the field-degree tower, as in299. Its highest
homogeneous form is a power of one linear form. Indeed the
homogenized parametrization extends to a morphism from
\(\mathbb P^1_L\) onto the projective plane closure; only its
single point at infinity maps to the line at infinity. This
forces one point there, and its leading coefficient vector is
L-rational. These statements do not turn a coefficient-field
change into an ambient one.

## 3. The first plane function cannot be constant

Suppose \(y\in L\). Equation (4) then makes theta affine in sigma,
and (5) gives \(L[\sigma]=L[v]\), with \(N\sigma\in L^*\).
Use the actual LND \(\mathcal P=a_0N-(NX)E\), as in298, and
put \(\tau=a_0N\sigma\in L^*\). Its two nonzero-slot formulas are
\[
\boxed{
\mathcal PZ=\tau(2\sigma-a_1/b_0+2tX),\qquad
\mathcal PW=\tau(-2y-(a_1/b_0)X),\qquad
\mathcal PX=\mathcal PY=0.}
\tag{10}
\]
In particular \(\mathcal P^2W=0\),
\(\mathcal P^2Z=2\tau^2\ne0\), and \(\mathcal P^3Z=0\).

Divide the two coefficients of \(\mathcal P\) by their gcd
\(\Delta\) in \(\mathcal B\), giving an irreducible relative
LND D over \(S=\mathbb C[X,Y]\). Both \(\mathcal P\Delta=0\)
and \(E\Delta=0\) hold. For the first, gcd divisibility and LND
degree apply to \(\mathcal P\). For the second use
\([E,\mathcal P]=0\): if \(\mathcal Px_i=\Delta g_i\) with
gcd one, then \(\Delta\mid(E\Delta)g_i\) for each generator,
so \(\Delta\mid E\Delta\), and local nilpotence gives zero.
It follows that \(\Delta\in L^*\) and \(\delta=\tau/\Delta\in L^*\).
The literal iterates are
\[
D^2W=0,\qquad D^3Z=0,\qquad D^2Z=2\delta^2\ne0.
\tag{11}
\]

[Dasgupta--Gupta, Lemma 2.3(i)](https://arxiv.org/html/1701.03635v1)
over the UFD S gives \(DW\in S\) and \(DZ\in S[W]\).
One cannot have \(DW=0\), since then \(D^2Z=0\). Thus
\(D^3Z=0\) forces \(DZ=A_2W+B_2\), with \(A_2,B_2\in S\),
and \(D^2Z=A_2DW\in S\cap\ker E\).
This intersection is \(\mathbb C\): a nonconstant polynomial
in the actual X,Y has positive E-degree, because their leading
ratio t is transcendental and the weights are one and two.
Hence \(A_2DW=2\delta^2\in\mathbb C^*\), so
\(DW\in\mathbb C^*\) and \(\delta\in\mathbb C^*\).

Apply E to the second expression of (10) after division by Delta.
It gives \(-\delta(a_1/b_0)a_0=0\), hence \(a_1=0\).
Now \(DW=-2\delta y\in\mathbb C^*\) makes \(y\in\mathbb C\).
This contradicts the strong return \(K=\mathbb C(y,z,w)\) of
transcendence degree three. Thus
\[
\boxed{y\notin L.}
\tag{12}
\]
This proof retains the actual factor \(-a_1/b_0\) in (10);
it is not silently replaced by a complex nonzero slope.

## 4. Vanishing second s-derivative forces a quadratic coefficient

Assume \(\ell_{ss}=0\), equivalently \(H_{rr}=0\).
If \(H_{tr}\ne0\), the plane primitive (8) has exact cubic
top \(H_{tr}U^2P\). Identity (9) then excludes selected degree
two or three: degree two would force R=0 and total degree two,
while degree three would make the top a pure cube. For degree
one, its top squared must divide \(U^2P\), so its top is
proportional to U and y is constant. This contradicts (12).
Consequently \(H_{tr}=0\). Exact constants give
\[
H=c r+f(t),\qquad c\in\mathbb C^*,\quad f\in F.
\tag{13}
\]

Now Q is a quadratic with fixed mixed coefficient 2:
\[
Q=\frac{f''}2P^2+2UP-\mathcal L_rU^2+f'U-\mathcal L_tP.
\tag{14}
\]
Its selected equation has degree one or two. In both cases (9)
and the pure-leading-form property force its quadratic part to
be a square of a linear form. Its determinant therefore vanishes:
\[
f''\mathcal L_r=-2.
\]
In particular \(f''\ne0\), and exact integration gives
\[
\mathcal L=b(t)r+d(t),\qquad b,d\in F,\quad b\ne0,
\qquad f''=-2/b.
\tag{15}
\]
Define
\[
l=b'r+d',\qquad \mathcal D=f'-bl,\qquad x=\sigma-by.
\]
Completion of (14) yields
\[
Q=-x^2/b-lx+\mathcal D y=q_0.
\tag{16}
\]

If the selected component is a line, its top is the line x=0.
Thus x is a coefficient-field constant, while y is nonconstant
by (12). Equation (16) forces \(\mathcal D=0\). Since
\(\mathcal D=f'-bb'r-bd'\), independence of r over F gives
\(b'=0\).

If the selected component is a conic, \(\mathcal D\ne0\).
Otherwise x would be constant by (16), giving a line. The whole
plane return then gives an affine line parameter x and
\[
\boxed{
y=\frac{x^2/b+lx+q_0}{\mathcal D},\qquad
\sigma=by+x,\qquad x_v\in L^*.}
\tag{17}
\]
The precise scalar after the two parameter changes is
\[
J_x=\det\frac{\partial(y,z,w)}{\partial(t,r,x)}
        =-a_0^4c/x_v\in L^*.
\tag{18}
\]
All t,r derivatives below hold x fixed, not the old moving v.

Here is a short complete reconstruction of its highest coefficient.
The literal intercepts in (7) are
\[
z=\sigma^2+f'\sigma+cy^2+2ty-br-d,\qquad
w=r-2\sigma y.
\]
Subtracting a multiple of the y-row and adding b times the w-row
uses
\[
z+bw=(c-b^2)y^2+(bf'+2t)y+x^2+f'x-d.
\]
Keeping the coefficient derivative \(b'w\,dt\), and using
\(f''=-2/b\), gives exactly
\[
\boxed{
J_x=-(2x+f')y_t-2y(2x/b+l)y_r
             +\{b'(2x+f')y-2x/b-l\}y_x.}
\tag{19}
\]
For verification, the modified z-row modulo dy is
\((2x+f')dx+\{b'(2x+f')y-2x/b-l\}dt\),
and the w-row modulo dy is \(dr-2b'y^2dt-2y\,dx\).
Their wedge gives (19) with the displayed orientation.

Set \(A_x=x^2/b+lx+q_0\), \(T_x=2x/b+l\), and
\(R_x=2x+f'\). Differentiating (17), using
\(\mathcal D_r=-bb'\), makes the numerator of (19) over
\(\mathcal D^3\) equal to
\[
\begin{aligned}
&-R_x\{(A_x)_t\mathcal D-\mathcal D_tA_x\}\mathcal D
-2A_xT_x\{(b'x+(q_0)_r)\mathcal D+bb'A_x\}\\
&\hspace{18mm}+b'R_xA_xT_x\mathcal D-T_x^2\mathcal D^2.
\end{aligned}
\tag{20}
\]
Every term except \(-2bb'A_x^2T_x\) has x-degree at most four.
Thus
\[
[x^5]J_x=-\frac{4b'}{b^2\mathcal D^3}.
\tag{21}
\]
The calibrated scalar (18) is independent of x, so \(b'=0\).
This deduction leaves the lower coefficients and \(q_0\) arbitrary;
none is needed for the following actual endpoint.

In both selected-component cases, b is complex nonzero. Equation
(15) therefore gives the exact integration
\[
\boxed{f(t)=f_2t^2+f_1t+f_0,\qquad f_i\in\mathbb C,
\qquad f_2=-1/b\ne0.}
\tag{22}
\]

## 5. An explicit original-ring degree reduction

The first two literal potentials alone give the full identity
\[
\mathcal R:=Y^2+X(W-XZ)=y^2+rX.
\tag{23}
\]
This polynomial is not declared to be an ambient coordinate.
Using the complex constant c of (13), make the actual map
\[
Z_1=Z-c\mathcal R,\qquad W_1=W-cX\mathcal R,
\qquad X_1=X,\quad Y_1=Y.
\tag{24}
\]
It preserves \(\mathcal R\), because
\(Y^2+XW_1-X^2Z_1=\mathcal R\). Its polynomial inverse is
\(Z=Z_1+c\mathcal R_1,W=W_1+cX\mathcal R_1\), with
\(\mathcal R_1=Y^2+XW_1-X^2Z_1\). The preserved identity
checks both inverse orders.

Since \(\mathcal R\) has time degree at most one, Z_1 still
has exact degree two and leader ratio \(t^2\). The coefficient
of \(X^2\) in W_1 is \(s-cr=f(t)\). Use (22) to make the
second actual triangular change
\[
W_2=W_1-f_2Z_1-f_1Y-f_0X^2,
\qquad W_1=W_2+f_2Z_1+f_1Y+f_0X^2.
\tag{25}
\]
Its quadratic time coefficient vanishes. Thus
\((X,W_2,Y,Z_1)\) is an actual polynomial coordinate frame,
with degrees \((1,\le1,2,2)\). If W_2 is invariant, the
regular-kernel theorem applies directly. Otherwise the completely
read supplied-frame recognition theorem
[257](full-exact1122-recognition-synthesis-pass257-working.md)
applies, subject to its retained working dependencies. We obtain
\[
\boxed{k=s,\ n=0,\ \ell_s\ne0,\ \ell_{ss}=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{26}
\]
There is no requirement that the old full initial kernel or selected
partial survive (24),(25). The endpoint257 accepts every actual
exact1122 frame. All old selected-chart identities are used before
the reframe, and both reframes have explicit polynomial inverses.

## 6. The genuine remaining quartic sector

When \(\ell_{ss}\ne0\), equivalently \(H_{rr}\ne0\), (8)
has exact quartic top proportional to \(U^4\). By (9), a selected
degree-three component is impossible: its square cofactor must
vanish, contradicting total degree four. A selected line would
have its top squared dividing \(U^4\), so y would be constant,
excluded by (12). Thus only selected degrees two and four remain.
The pure top forces
\(\deg_v y<\deg_v\sigma=\deg G\).

For completeness, a whole polynomial-plane presentation cannot
have the pair \((\deg y,\deg\sigma)=(3,4)\). The polynomial
\(\sigma\) is integral over \(L[y]\), and its degree-three
minimal polynomial over \(L(y)\) is monic with coefficients in
the integrally closed ring \(L[y]\). Therefore
\(L[y,\sigma]\) is spanned over \(L[y]\) by
\(1,\sigma,\sigma^2\). The leading degrees of nonzero terms
\(p_i(y)\sigma^i\) are \(3\deg p_i+4i\), with different
residues modulo three, so they cannot cancel. This module cannot
contain v, a polynomial of degree one. It contradicts (5).
Consequently the remaining pairs are precisely restricted to
\[
\boxed{(\deg_v y,\deg_v\sigma)\in\{(1,2),(1,4),(2,4)\},
\qquad \ell_{ss}\ne0.}
\tag{27}
\]
This is a necessary list, not existence or recognition of any of
its members. All their coefficient functions still lie in the
exact finite field L and must satisfy the complete scalar.

The direct sources264,290,296,298 and257 were read in full. Fresh
unsaved algebra reconstructed the coefficient transformation (8),
the scalar row (19), its exact numerator and fifth coefficient,
and preservation/inverses of (24). An abandoned slower raw expansion
was interrupted before completion; no result is inferred from it.
No saved checker was executed, imported or compiled. No retained
source was edited. There is no arbitrary k or n normalization,
unrestricted cancellation, existence or novelty claim.
