# The sixth scalar coefficient makes the reciprocal slope affine

Working necessary reduction: retain the complete actual nonzero-E
normal form of376. The next coefficient of the literal scalar
Jacobian gives
\[
\left(\frac1{tH}\right)''=0,\qquad
\left(\frac{G_0'}{t^2H^2}\right)'=0.
\]
Consequently H=1/[t(c1+c2t)] with complex c1,c2 not both zero,
and G0 is a quotient of complex affine polynomials with denominator
c1+c2t. No assumption that the exact field F is rational is used.

This note does not combine these equations with the separately
investigated lower fourth-potential alternatives. It constructs
no ambient coordinate and proves neither realization nor recognition.

## 1. Exact retained chart and the data used

Retain every actual hypothesis and necessary identity of the fully
read held source
[376](principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad
E_{\rm slice}=\partial_u,\qquad
\deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
a_0=E_{\rm slice}X\ne0,\qquad N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\qquad
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\qquad Nr=\rho\in L^*,\\
K=L(r)=\mathbb C(y,z,w),\qquad
F=\ker_L\partial_s,\qquad [F:\mathbb C(t)]<\infty,\qquad L=F(s).
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. Primes mean the t-derivative
on F, whose constants are exactly C. The parameter s is transcendental
over F. The intrinsic remainder r is transcendental over L; it is
not an actual coordinate of the original four-ring.

The actual normalization in369 has already arranged k=s and
n=-s^2/(4t^2)+f. In the remaining intrinsic pair(2,3),376 gives
\[
\begin{gathered}
f,l,G_0,H,g,E\in F,\qquad
g=f''/2\ne0,\quad E=g'/3+g/t\ne0,\quad H\ne0,\\
E=d\,t^3H^4,\qquad d\in\mathbb C^*,\\
\sigma=A r^2+B r+e,\qquad
A=-\frac{4E}{g^2H}\ne0,\qquad
B=\beta s+\beta_0,\\
\beta=-\frac{2tH'+4H}{t^2gH},\qquad
\beta_0=-\frac{2G_0'}{tgH},\qquad
e=e_0+e_1s+e_2s^2,\quad e_i\in F.
\end{gathered}
\tag{2}
\]
The coefficient E is not the slice derivation. The complete
coefficient potential is
\[
\ell=-\frac{s^3}{4t^4}-\frac{Hs^2}{4t^2}
       +\frac{(f-tf'-G_0)s}{2t^2}+l.
\tag{3}
\]
We use the precise e1,e2 identities of376, not just their membership
in F:
\[
\begin{aligned}
e_1&=-\frac{4EG_0't+2Egt^2-2G_0'g-G_0''gt}{4Egt^3},\\
e_2&=\frac{-8EHt-4EH't^2+6Hg+6H'gt+H''gt^2}{8Egt^4}.
\end{aligned}
\tag{4}
\]
The value of e0 does not enter the new coefficient. The scalar
calculation below holds with arbitrary e0 in F, so it makes no
additional assumption about l or its derivatives.

Set
\[
C=\ell_s+\frac{s^2}{4t^4},\qquad
\Lambda=\frac{2sC}{t}+\ell_t,\qquad
G=Hs+G_0.
\tag{5}
\]
The literal third-level parametrization and intercepts are
\[
\begin{aligned}
\theta&=\frac tr\left\{
 g(\sigma^2-e^2)-\Lambda(\sigma-e)
 +\frac{2sr\sigma}{t^2}+r^2-2tCr\right\},\\
y&=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
       -\frac{n_t}{2}-tC,\\
z&=\left(\sigma+\frac{s}{2t}\right)^2+2tr+G,\\
w&=\ell-2\sigma y-n_t\sigma+\frac{s\theta}{2t^2}.
\end{aligned}
\tag{6}
\]
The numerator defining theta is divisible by r. Thus all four
expressions are polynomials in the independent r, including at zero.
Their determinant at actual X=0 is the exact nonzero scalar
\[
J_0=\det\frac{\partial(y,z,w)}{\partial(t,s,r)}
       =-a_0^4/\rho\in L^*.
\tag{7}
\]
The derivatives here fix r, before any substitution of its value.
Only independence of r is used below. We do not need the stronger
assertion that the scalar is also independent of s.

## 2. A finite coefficient ledger for the literal determinant

The new calculation uses the full intercept rows(6), not the
highest homogeneous terms of an unspecified parametrization.
Here is a finite expansion ledger which also fixes every sign.

Write p2=A, p1=B, p0=e, so sigma=sum p_i r^i.
The coefficients theta_i of theta=sum theta_i r^i are
\[
\begin{aligned}
\theta_3&=tgA^2,\\
\theta_2&=2tgAB+2sA/t,\\
\theta_1&=tg(B^2+2Ae)-t\Lambda A+2sB/t+t,\\
\theta_0&=2tgBe-t\Lambda B+2se/t-2t^2C.
\end{aligned}
\tag{8}
\]
Use zero for every coefficient outside its indicated range. Put
q_i=p_i+(s/(2t))delta_(i0). If y_i,z_i,w_i are the polynomial
coefficients of the three rows, they are exactly
\[
\begin{aligned}
y_i&=\delta_{i1}-\frac{\theta_i}{2t}
       +\frac{s p_i}{2t^2}
       -\left(\frac{n_t}{2}+tC\right)\delta_{i0},\\
z_i&=\sum_{j+k=i}q_jq_k+2t\delta_{i1}
                      +(Hs+G_0)\delta_{i0},\\
w_i&=\ell\delta_{i0}-2\sum_{j+k=i}p_jy_k
                         -n_t p_i+\frac{s\theta_i}{2t^2}.
\end{aligned}
\tag{9}
\]
The ranges are i=0,...,3 for y, i=0,...,4 for z, and i=0,...,5
for w. These formulas include the moving e and every lower
coefficient of the literal second potential.

For example the sixth determinant coefficient is the finite sum
\[
\begin{aligned}
[r^6]J_0=\sum_{i+j+k=7}\big[
 &(y_i)_t\{k(z_j)_s w_k-jz_j(w_k)_s\}\\
 &-(y_i)_s\{k(z_j)_t w_k-jz_j(w_k)_t\}\\
 &+iy_i\{(z_j)_t(w_k)_s-(z_j)_s(w_k)_t\}\big].
\end{aligned}
\tag{10}
\]
This is ordinary expansion of the determinant with columns t,s,r;
the factors i,j,k come from differentiating r powers. In particular
it is not differentiation of a moving evaluation point.

Substitute(2)--(5) into(8)--(10). In differentiating the field
coefficients, use exactly
\[
g'=3E-\frac{3g}{t},\qquad
E'=E\left(\frac3t+4\frac{H'}H\right),\qquad f''=2g.
\tag{11}
\]
These follow from the retained identities, and introduce no new
ODE. Expanding the finite sum gives the complete coefficient
\[
\boxed{
[r^6]J_0=
\frac{448E^4}{H^5g^7t^3}
\left(s\,T_H+t\,T_G\right),
}
\tag{12}
\]
where
\[
\begin{aligned}
T_H&=t^2HH''-2t^2(H')^2-2tHH'-2H^2,\\
T_G&=tHG_0''-2(H+tH')G_0'.
\end{aligned}
\tag{13}
\]
In particular the coefficient is affine in s. Its s^4,s^3,s^2
coefficients vanish identically. No f,l,e0 or derivative of e0
remains. The coefficient e enters the unreduced sixth coefficient
only through e_s; inserting e_s=e1+2e2*s gives(12).

For a separate reconstruction, one can start with arbitrary
A(t), B(t,s), e(t,s), ell(t,s), and f(t), form the same rows,
and compute(10) before making any of the substitutions(2)--(5).
That general raw coefficient gives the same(12) after substitution.
Thus neither the polynomial form of a determinant coefficient
nor the cancellation of its higher s powers is presumed.

## 3. Exact integration of the new slope equation

Calibration(7) forces(12) to vanish. Its prefactor is nonzero
because E,H,g,t are nonzero. Both T_H and T_G belong to F.
Since s is transcendental over F, the two coefficients vanish
separately:
\[
T_H=0,\qquad T_G=0.
\tag{14}
\]
No independence of the scalar from s, beyond its independence
of the intrinsic r, was used.

A direct differentiation gives
\[
\left(\frac1{tH}\right)''
   =-\frac{T_H}{t^3H^3}.
\tag{15}
\]
Thus 1/(tH) has zero second t-derivative in the exact field F.
Its first derivative is a complex constant, and subtracting
that constant times t leaves another complex constant. Therefore
\[
\boxed{
H=\frac1{t(c_1+c_2t)},\qquad
c_1,c_2\in\mathbb C,\qquad (c_1,c_2)\ne(0,0).
}
\tag{16}
\]
The denominator c1+c2*t is a nonzero element of F, even if it
has zeros at individual curve points. No inversion at a selected
fiber or ambient localization is being performed.

The inherited E equation then becomes
\[
E=\frac{d}{t(c_1+c_2t)^4},\qquad d\in\mathbb C^*.
\tag{17}
\]
This does not assert a formula for g beyond its retained differential
equation in(11). In particular it has not used either lower-Q
alternative from the separate investigation377.

## 4. The companion equation and its zero boundary

Directly,
\[
\left(\frac{G_0'}{t^2H^2}\right)'
 =\frac{T_G}{t^3H^3}.
\tag{18}
\]
The vanishing of T_G therefore gives
\[
G_0'=c_3 t^2H^2=\frac{c_3}{(c_1+c_2t)^2},
\qquad c_3\in\mathbb C.
\tag{19}
\]
No division by G0' was used, so c3=0 and constant G0 are included.

This integrates exactly inside F. If c2 is nonzero, subtract
-c3/[c2(c1+c2*t)] from G0; the difference has zero derivative
and is complex. If c2=0, then c1 is nonzero and subtracting
(c3/c1^2)*t has the same effect. Equivalently, both cases can
be recorded as
\[
\boxed{
G_0=\frac{u_1t+u_0}{c_1+c_2t},\qquad u_0,u_1\in\mathbb C .
}
\tag{20}
\]
Its derivative is (u1*c1-u0*c2)/(c1+c2*t)^2, so(19) imposes
c3=u1*c1-u0*c2. These formulas allow either c1 or c2 to vanish,
provided they do not both vanish.

## 5. Scope and verification boundary

Equations(16),(17),(20) are new necessary restrictions within the
exact actual nonzero-E family of376. The remaining functions,
including the one-variable coefficient l, are still constrained
by the lower fourth-potential and scalar equations. This note does
not assume F=C(t), construct an ambient polynomial coordinate,
or combine the scalar equation with either lower-Q mode.

The final376 source was revalidated and read through EOF in98e70c.
Fresh unsaved b4e62d, completed on its original handle2138 in77ed0d,
formed the full rows over a formal derivative field satisfying(11)
and reconstructed the entire coefficient(12). Separately36ce2c,
completed on its original handle46090 in523cf1, first computed the
general raw sixth coefficient with arbitrary coefficient functions.
A new reduction d29550, completed on its original handle63322 in
f7ac58, substituted the exact376 identities into that raw expression
and verified zero residual against(12).

These exact expansions supplement the displayed finite ledger and
the written exact-field integration. No saved checker was executed,
imported or compiled, no held source or canonical index was edited,
and no unrestricted cancellation, novelty, human-expert review or
proof-assistant certification is claimed.
