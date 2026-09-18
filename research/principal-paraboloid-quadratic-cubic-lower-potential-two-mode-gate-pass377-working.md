# Two exact lower-potential modes in the quadratic-cubic normal form

Working necessary reduction: the complete lower fourth potential
in376 forces either 8t e2=H beta or 16t e2=H beta. The two other
coefficients at the same total degree are compatible with these
modes and supply no additional condition there. In dimensionless
coefficient functions, the alternatives become two explicit coupled
first-order differential systems. The zero-beta overlap is retained.

This note uses the genuine fourth polynomial, including the moving
third-level derivatives h_t,h_s. It does not use any new scalar
restriction beyond376, classify the differential systems, exclude a
mode, or infer an actual coordinate from a coefficient-field form.

## 1. Exact retained normal form

Retain every actual and exact-field hypothesis of the fully read
[376](principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md).
In particular the original globally sliced polynomial ring and its
full initial kernel supply the literal chart, the genuine potentials,
whole-line return, and the nonzero scalar. The coefficient fields are
\[
\begin{gathered}
F=\ker_L\partial_s,\qquad [F:\mathbb C(t)]<\infty,
\qquad L=F(s),\qquad K=F(s,r)=\mathbb C(y,z,w),\\
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\qquad
Nr=\rho\in L^*,\qquad
J_{t,s,r}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute. The constants of the
t derivative on F are C. No equality F=C(t) is assumed, and
neither s nor r is declared an original coordinate.

Use precisely the following coefficient notation from376:
\[
\begin{gathered}
g=f''/2\in F^*,\qquad
E=g'/3+g/t\in F^*,\qquad H\in F^*,\qquad
E=d t^3H^4,\quad d\in\mathbb C^*,\\
n=-\frac{s^2}{4t^2}+f,\qquad
\ell=-\frac{s^3}{4t^4}-\frac{Hs^2}{4t^2}
       +\frac{(f-tf'-G_0)s}{2t^2}+l,\qquad f,G_0,l\in F,\\
\sigma=A r^2+(\beta s+\beta_0)r+e,\qquad
e=e_2s^2+e_1s+e_0,\qquad A,\beta,\beta_0,e_i\in F,\quad A\ne0.
\end{gathered}
\tag{2}
\]
Primes mean the exact t derivative on F. In particular
\[
\begin{aligned}
A&=-\frac{4E}{g^2H},\qquad
\beta=-\frac{2tH'+4H}{t^2gH},\qquad
\beta_0=-\frac{2G_0'}{tgH},\\
e_2&=\frac{-8EHt-4EH't^2+6Hg+6H'gt+H''gt^2}{8Egt^4}.
\end{aligned}
\tag{3}
\]
The other two e coefficients remain exactly those of376. Their
values will not affect the homogeneous coefficients selected below.
Neither beta nor e2 is assumed nonzero.

## 2. The literal third level and full fourth polynomial

To make the derivative convention explicit, define
\[
\begin{gathered}
\nu=n_s=-\frac{s}{2t^2},\qquad
C=\ell_s+\frac{s^2}{4t^4},\qquad
\Lambda=\frac{2sC}{t}+\ell_t,\\
\theta=\frac tr\left\{g(\sigma^2-e^2)
 -\Lambda(\sigma-e)+\frac{2sr\sigma}{t^2}+r^2-2tCr\right\},\\
y=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
       -\frac{n_t}{2}-tC,\qquad
h=t^2C^2-\Lambda e+ge^2+\nu\ell-\frac{n_t^2}{4}.
\end{gathered}
\tag{4}
\]
The numerator defining theta is divisible by r, so this is an
identity in F[s,r] including r=0. The h in (4) is the third-level
coefficient, not the logarithmic derivative used later.

With independent formal variables U,P,V, the genuine fourth
primitive365(7) is
\[
\begin{aligned}
Q={}&[(n_{tt}+2\ell_s)P+n_{ts}V-2n_{ts}P^2
             -2n_{ss}PV-\ell_t]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
 +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2n_{ts}n_t}{2}P^2
 -(\ell_{ts}+n_sn_{ts}+n_{ss}n_t)PV
 -\frac{\ell_{ss}+2n_sn_{ss}}{2}V^2\\
&+(n_{ts}\ell+n_t\ell_s-h_t)P
 +(n_{ss}\ell+n_s\ell_s-h_s)V,
\qquad Q(y,\sigma,\theta)=q_0\in L.
\end{aligned}
\tag{5}
\]
The derivatives h_t,h_s are taken from the full expression (4).
In particular they retain the moving e coefficients. They cannot
be omitted when computing the r-cubic and lower coefficients.

All terms after evaluation lie in F[s,r]. Consequently each
positive-r coefficient must vanish as a polynomial in the
transcendental s. We examine the total-degree-six coefficients
r^3 s^3, r^2 s^4 and r s^5, within the three remaining positive
r coefficients after the high gates of376.

For an explicit expansion check, the relevant highest pieces are
\[
\begin{gathered}
\sigma_2=A r^2+\beta rs+e_2s^2,\qquad
[s^2]\Lambda=-\frac{2H+tH'}{4t^3},\\
[s^4]h=\frac{5}{16t^6}
      +\frac{(2H+tH')e_2}{4t^3}+g e_2^2.
\end{gathered}
\tag{6}
\]
Thus the terms -h_t sigma and -h_s theta in (5) do contribute
at the total degree in question. Using (4),(5), not just the
cubic homogeneous part of the formal Q, gives the following
complete coefficient ledger.

## 3. A factored lower-coefficient ledger

Set, solely as coefficient-field abbreviations,
\[
M=8t e_2-H\beta,\qquad
L_1=16t e_2-H\beta,\qquad
W_1=t e_2'+3e_2.
\tag{7}
\]
After the identities (3), the three exact coefficients are
\[
\boxed{
[r^3s^3]Q=-\frac{A^2g^2}{32t}\,M L_1.
}
\tag{8}
\]
The two lower ones, with their derivatives retained, are
\[
\begin{aligned}
[r^2s^4]Q
 &=-\frac{AgL_1}{256t^2}
      \left(-AHgL_1+16\beta gtM+32W_1\right),\\
[rs^5]Q
 &=-\frac{gL_1}{128t^2}
      \left(AgL_1(4te_2-H\beta)
                   +4\beta^2gtM+16\beta W_1\right).
\end{aligned}
\tag{9}
\]
One way to reconstruct this finite expansion is first to regard
A,beta,e2,g,g',H,H',H'',e2' as independent formal jets. Substitute
(4) into (5), extract the three monomials, and only then replace
\[
g'=-\frac{3Ag^2H}{4}-\frac{3g}{t},\qquad
H'=-\frac{H(\beta t^2g+4)}{2t},
\tag{10}
\]
and solve the last formula of (3) for H''. This produces (8),(9)
without dropping any lower coefficient derivative. No equation
obtained from a new scalar calculation is used here.

Since A,g,t are nonzero and F is a field, (8) proves the necessary
alternatives
\[
\boxed{8t e_2=H\beta\quad\text{or}\quad16t e_2=H\beta.}
\tag{11}
\]
This field-valued product implication needs no choice varying
with a geometric point. It includes their possible overlap.

## 4. Derivative compatibility and the zero-beta boundary

Directly differentiating beta in (3), and then using (3),(10),
gives the exact identity
\[
\boxed{\beta'=\frac g4
       \left(-AH\beta+16At e_2+2t\beta^2\right).}
\tag{12}
\]
This is an identity among the retained coefficients, not an
additional imposed scalar equation.

In the second mode of (11), L1=0 and both expressions in (9)
vanish immediately. In the first mode M=0, differentiation of
e2=H beta/(8t), followed by (10),(12), gives
\[
L_1=H\beta,\qquad W_1=\frac{AHgL_1}{32}.
\tag{13}
\]
Substitution into (9) makes both coefficients zero as well.
For the last coefficient, 4te2-H beta=-L1/2 and L1=H beta
make its two surviving terms cancel. No beta division is used.

Thus these next two top coefficients do not independently remove
either mode. If beta=0, either mode of (11) forces e2=0, since t
is nonzero. Conversely beta=e2=0 satisfies both modes and (12).
This overlap must be retained in any later argument.

## 5. Equivalent dimensionless necessary systems

Use the logarithmic derivative D=t partial_t on F and define
\[
\zeta=t\frac{H'}H+2,\qquad
\omega=\frac{tE}{g}\ne0.
\tag{14}
\]
These are coefficient functions, not original coordinates.
Equations (3) become
\[
\beta=-\frac{2\zeta}{t^2g},\qquad
e_2=\frac{H}{8Et^4}
          \left(D\zeta+\zeta^2+\zeta-4\omega\zeta\right).
\tag{15}
\]
The two alternatives in (11) are therefore respectively
\[
\boxed{
D\zeta=\zeta(2\omega-\zeta-1)
\quad\text{or}\quad
D\zeta=\zeta(3\omega-\zeta-1).
}
\tag{16}
\]
Independently, the already retained identity E=d t^3H^4 and
E=g'/3+g/t give
\[
\boxed{D\omega=\omega(4\zeta-1-3\omega).}
\tag{17}
\]
Indeed D log E=3+4D log H=4zeta-5, whereas
D log g=3omega-3. Subtracting these and adding D log t=1
gives (17). All denominators are the nonzero t,E,g,H from (2).
The case zeta=0, equivalent to beta=0, has not been divided out.

## 6. Scope and verification record

Equations (11),(12),(16),(17) are necessary consequences of the
full actual376 entry. The remaining lower-s coefficients of the
same three Q equations and the full scalar still constrain the
family. No sufficiency, mode exclusion, differential-system
classification, actual-coordinate recognition, or unrestricted
cancellation conclusion is claimed here.

The held376 source was reread completely and its hash revalidated
in5e39cf. Fresh unsaved2bcf22 reconstructed the entire evaluated
Q with full h_t,h_s, and extracted all three total-degree-six
coefficients with independent coefficient jets. Separate f95cb1
reduced the first one to (8). A further reduction15136d verified
(9),(12), and both zero-mode substitutions without beta division.
The dimensionless forms follow by the explicit substitutions
and logarithmic differentiation written in (14)--(17).

These exact finite identities supplement the written algebraic
arguments. No saved checker was executed, imported, compiled or
rerun by this author, and no earlier source or canonical record
was edited. No novelty, human-expert verification, or
proof-assistant certification is claimed.
