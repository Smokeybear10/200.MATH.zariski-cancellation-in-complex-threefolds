# A variable second slope contradicts the actual intercept field return

Working exclusion: retain the full actual principal chart264 with
k=s and n_s=0. In333's plane chart r=ell, suppose ell_s is nonzero,
ell_ss=0, and s=c(t)r+d(t). The branch c' nonzero is impossible.
The proof uses the full nonzero scalar and the strong complex intercept
field return. It does not assume the exact coefficient field is rational
or make any coefficient function an original polynomial coordinate.

This note addresses only the variable-c branch. It does not prove the
complementary c'=0 case or compose a recognition theorem for the whole
one-variable first-potential family.

## 1. Full actual assumptions and derivative conventions

Retain the complete actual chart
[264](principal-one-affine-paraboloid-chart-pass264-working.md), the
unit-gradient-minor conclusion296, and the plane reduction of the
fully read
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\qquad a_0=EX\ne0,\\
N=[u^4]\partial_Z|_A\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad [L:\mathbb C(t,s)]<\infty,\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\quad
L[y,z,w]=L[y,\sigma,\theta]=L[v],\\
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s)X+t^2X^2,\quad
W=w+\theta X+sX^2,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The nonzero N is the chosen literal-partial leader. Its coefficient
field contains a0,t,s. All original coefficient partials commute and
fix v. The determinant holds at fixed actual X, not merely at X=0.

Assume k=s and n=f in F=ker_L(partial_s). This exact field is finite
over C(t), and its t-derivative has constants exactly C. Put
\[
p=f'/2,\qquad g=f''/2=p',\qquad x=y+p.
\tag{2}
\]
Primes mean the exact derivative on F. Nothing here assumes F=C(t).
For this bounded exclusion assume
\[
\ell_s\ne0,\quad\ell_{ss}=0,\qquad
r=\ell,\quad s=H(t,r)=c(t)r+d(t),\quad c\in\mathbb F^*,
\quad d\in\mathbb F,\quad c'\ne0.
\tag{3}
\]
The form of H follows by exact integration of H_rr=0 in L. In the
new coefficient variables, partial_r=H_r partial_s, and the new
t-partial is the old t-partial plus H_t partial_s. These commute;
their r-constant field is still F, and their t-derivative on F is
unchanged. The field L is finite over F(r), with r transcendental
over F. All subsequent t,r partials use these new variables.

Write the centered third-level coefficient as
\(\mathcal L=H_r(h+p^2)\), as in333. The exact plane presentation and
first potentials are
\[
\begin{aligned}
\theta&=c(x^2+g\sigma^2)+(c'r+d')\sigma-\mathcal L,
& O&=L[x,\sigma]=L[v],\\
z&=2tx+\sigma^2+\theta+f-tf',
& w&=r-2\sigma x.
\end{aligned}
\tag{4}
\]
This is polynomial generation over L only. The centering x=y+p is
not claimed to be an original coordinate change.

## 2. The cubic top forces a constant first function

The full plane primitive333, specialized only by H_rr=0, is
\[
\begin{aligned}
\Phi(U,P)={}&c'P U^2+
 \left(gc'+\frac{cg'}3\right)P^3
 +\frac{c''r+d''}{2}P^2\\
&+2(1+gc)UP+(c'r+d')U
 -\mathcal L_r(U^2+gP^2)-\mathcal L_tP,\\
\Phi(x,\sigma)&=q_1\in L.
\end{aligned}
\tag{5}
\]
For the full irreducible plane equation G of O=L[x,sigma], the
evaluated-gradient unit implies the exact identity
\[
\Phi-q_1=\eta G+G^2R,\qquad
\eta\in L^*,\quad R\in L[U,P].
\tag{6}
\]
The degree of G is max(deg_v x,deg_v sigma), and its highest
homogeneous part is a power of one linear form. These are the
retained whole-polynomial-line facts of333, not assumptions that
Phi itself is irreducible.

Since c' is nonzero, Phi has degree exactly three. Equation(6)
excludes degree two: a nonzero G^2R would have degree at least four,
whereas R=0 would leave degree two. Degree three would force R=0
and a pure-cube top. But
\[
\Phi_3=P\left(c'U^2+\left(gc'+cg'/3\right)P^2\right)
\tag{7}
\]
cannot be a cube: if the P-squared coefficient inside parentheses
is nonzero, its three linear factors are distinct over an algebraic
closure; if it is zero, its multiplicities are two and one.

Thus G is linear, and its squared top divides (7). The only way (7)
has any squared linear factor is
\[
gc'+cg'/3=0,
\qquad G=U-\beta\quad\text{after monic normalization},
\qquad x=\beta\in L.
\tag{8}
\]
In this case the squared factor is U^2. If g were zero, the
unit-gradient calculation below still applies and the field argument
has an even simpler contradiction, treated separately in Section6.
For Sections3--5 assume g is nonzero.

The whole return in(4) now gives L[sigma]=L[v], so sigma is affine
nonconstant in v. Differentiating (6) formally in U and evaluating
on U=beta gives Phi_U(beta,sigma)=eta, a coefficient-field unit.
Its P-coefficient must vanish. The result and the P-squared and
P coefficients of Phi(beta,P) are respectively
\[
\begin{aligned}
\beta&=-\frac{1+gc}{c'}\in\mathbb F,\\
\mathcal L_r&=\frac{c''r+d''}{2g},\\
\mathcal L_t&=-\frac{(1+gc)^2}{c'}.
\end{aligned}
\tag{9}
\]
The scalar beta is therefore in the exact curve field, not just L.
No parameter root was differentiated to obtain these equations.

## 3. Exact integrations and a conserved scalar

Commuting the t,r derivatives of(9), whose last member is independent
of r, gives
\[
\left(\frac{c''}{g}\right)'=0,\qquad
\left(\frac{d''}{g}\right)'=0.
\tag{10}
\]
Coefficient comparison in the transcendental r is legitimate over F.
Exact constants therefore give complex numbers A,B such that
\[
c''=Ag,\qquad d''=Bg,\qquad
\mathcal L=\frac A4r^2+\frac B2r+e(t),\qquad e\in\mathbb F.
\tag{11}
\]
The last assertion follows by subtracting the displayed polynomial
primitive in r; its difference is killed by partial_r and lies in F.
Neither A nor B is assumed nonzero.

Equation(8) integrates inside the exact field to
\[
C:=gc^3\in\mathbb C^*,\qquad
\kappa:=(c')^2+\frac{AC}{c^2}\in\mathbb C.
\tag{12}
\]
Indeed (gc^3)'=0. Differentiating the second expression and using
c''=AC/c^3 gives zero. This is differentiation followed by the
known constant-field property, not a rational-function ansatz.

Put J=1+gc. Then J'=-2gc' is nonzero; in particular J itself is a
nonzero element of F. Differentiating beta=-J/c' exactly gives
\[
\beta'-g
 =g\left(1+\frac{AJ}{(c')^2}\right)
 =\frac{g(\kappa+A)}{(c')^2}.
\tag{13}
\]
The symbol J in this section is this coefficient function, not the
calibrated determinant. We do not divide by kappa or A separately.

## 4. The original nonzero scalar forces the quadratic coefficient

Use the independent variables t,r,P, where P=sigma, at X=0.
The intercepts from(4) become
\[
\begin{aligned}
y&=\beta-p,\\
z&=2t\beta+J P^2+(c'r+d')P+c\beta^2
           -\mathcal L+f-tf',\\
w&=r-2\beta P.
\end{aligned}
\tag{14}
\]
Here y_r=y_P=0, w_r=1, and w_P=-2beta. A direct first-row expansion
of the determinant yields
\[
\begin{aligned}
\mathcal J
 &:=\det\frac{\partial(y,z,w)}{\partial(t,r,P)}\\
 &=(\beta'-g)
 \left[-2(\beta c'+J)P+2\beta\mathcal L_r-(c'r+d')\right]\\
 &=(\beta'-g)\left[2\beta\mathcal L_r-H_t\right]\in L^*.
\end{aligned}
\tag{15}
\]
The final nonzero assertion is an actual calibration consequence.
If h=sigma_v in L*, then the parameter-change determinant is
\[
\det\frac{\partial(t,r,\sigma)}{\partial(t,s,v)}=h/c,
\qquad \mathcal J=-\frac{c a_0^4}{h}\ne0.
\tag{16}
\]
The coefficient derivatives of sigma at fixed v contribute no other
term to this triangular parameter-change determinant. No assertion
that h or a0 belongs to F is needed.

Consequently beta'-g is nonzero. Equation(13) forces
\[
\kappa+A\ne0.
\tag{17}
\]
This is exactly the nonvanishing needed below. The possibly zero
energy kappa and integration constants A,B have not been discarded.

## 5. The strong complex intercept return contradicts degree two

Equations(11),(14) put all three intercepts in F[r,P]. Since F and
r,P already lie in K, the actual strong return gives both inclusions
\[
K=\mathbb C(y,z,w)\ \subseteq\ \mathbb F(r,P)\ \subseteq\ K.
\tag{18}
\]
Thus K=F(r,P). The variables r and P are algebraically independent
over F: r is transcendental over F and P is transcendental over L.
In particular w=r-2beta P is independent of P over F and
\[
K=\mathbb F(w,P).
\tag{19}
\]
No equality L=F(r) was assumed to obtain these inclusions.

Substitute r=w+2beta P in z from(14), retaining the quadratic
polynomial L of(11). Its coefficient of P squared is
\[
\begin{aligned}
q_2&=J+2\beta c'-A\beta^2
     =-J-A\beta^2\\
    &=-\frac{J((c')^2+AJ)}{(c')^2}
     =-\frac{J(\kappa+A)}{(c')^2}\ne0.
\end{aligned}
\tag{20}
\]
Every other term has P-degree at most one or is a coefficient in
F(w). Hence z is a polynomial of degree exactly two in P over F(w).
It follows that
\[
[\mathbb F(w,P):\mathbb F(w,z)]=2.
\tag{21}
\]
For clarity, this elementary degree statement holds over any field:
for a polynomial of degree d in an independent variable P, the powers
1,P,...,P^(d-1) span over its rational function field by reduction;
their independence follows by clearing denominators and comparing
distinct leading degrees modulo d. Here d=2, and no algebraic
closedness or rationality of F is used.

But y=beta-p belongs to F. Thus the same actual return also gives
\[
K=\mathbb C(y,z,w)\subseteq\mathbb F(z,w)\subseteq K.
\tag{22}
\]
This makes the extension in(21) degree one, a contradiction. The
argument is a whole-field obstruction, not an attempt to call P,
r or a coefficient-field polynomial an original coordinate.

## 6. The zero-g boundary and exact conclusion

If g=0 in the branch(3), then g'=0. The cubic-top and unit-gradient
argument still yields G=U-beta, beta=-1/c', and L[sigma]=L[v].
The P-squared coefficient of Phi(beta,P) is now H_tt/2, forcing
c''=d''=0. Consequently c' is a nonzero complex constant, so beta
is complex. Also p'=g=0 makes p complex. Thus y=beta-p is complex,
and the first row of the X=0 intercept determinant is zero. This
contradicts the same nonzero calibration(1). No division by g is
needed in this separate boundary.

We have therefore excluded c' nonzero for every g in F, under the
full actual hypotheses(1)--(3). The conclusion does not require the
broader necessity ell_ss=0 proved separately in the fully read
[344](principal-paraboloid-complex-quadratic-family-recognition-pass344-working.md),
although it can be composed with that result when its dependencies
are retained. The branch ell_s=0 and the branch c'=0 are outside
this exclusion and are not silently omitted from a larger theorem.

Complete direct264,333 and344 sources were read before this note.
The full fourth-potential input296 is a retained completely read
working theorem, not an assertion that every upstream proof has
been recursively audited in this note. Fresh unsaved algebra rebuilt
the literal determinant(15), the coefficient(20) before substitution,
and the two reductions using(12), all with zero residuals. These
checks supplement, not replace, the exact integration and field-degree
arguments. No saved checker was executed, imported or compiled;
no earlier proof, checker, canonical ledger or index was changed.
