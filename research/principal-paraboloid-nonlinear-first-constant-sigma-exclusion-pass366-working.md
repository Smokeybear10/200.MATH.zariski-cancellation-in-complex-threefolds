# A nonlinear first potential excludes constant sigma

Working exclusion: in the full actual principal chart264, suppose
k=s and n_ss is nonzero. Then sigma cannot belong to the exact
coefficient field L. The sliced third level first gives a genuine
affine polynomial parameter. Two coefficients of the full actual
determinant leave a Riccati alternative. One branch has proportional
Jacobian columns; the other makes an actual coordinate polynomial a
square in the fraction field, which is impossible.

This proof does not apply the full surface-gradient unit statement to
a sliced factorization. It does not assume rationality of L or promote
a coefficient-field change to an original coordinate change.

## 1. Exact actual inputs and the sliced quadratic

Retain the complete actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), with
the full scalar retained in
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\quad O=L[v]=L[y,\sigma,\theta],\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The selected N is the leading part of the literal Z-partial. It kills
a0,t,s. The coefficient partials extend uniquely to L, commute, and
initially fix v. Assume, for this proof,
\[
k=s,\qquad e:=n_{ss}\ne0,\qquad p:=\sigma\in L.
\tag{2}
\]
The first two potentials are the literal ones
\[
\begin{aligned}
z&=2ty+p^2+\theta+n,\\
w&=\ell-2py-n_t p-n_s\theta,\\
Y&=y+pX+tX^2,\\
Z&=z+(2tp+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
Here n,ell belong to L and can be arbitrary algebraic coefficient
functions subject to the actual chart. Put x=y+n_t/2-n_s p.
Completing the square in264's third level gives
\[
x^2+\frac e2\theta^2+D\theta+E_0=0,
\qquad D=n_{ts}p-n_s^2-\ell_s,\quad E_0\in L.
\tag{4}
\]
The constant E0 includes the third level; it is not presumed zero.

Over an algebraic closure of L, complete the square in theta and
factor the left side as a product of two affine functions of x and
theta plus a constant. If that constant were nonzero, the product
would be a nonzero constant in the polynomial ring in v, so both
factors would be constant. Then x and theta, hence y, would be
constant, contrary to O=L[v]. Thus the completed level is zero and
one linear factor vanishes identically.

In particular theta is nonconstant and y is affine in theta. The
slope lies in L: it is the ratio of their leading v-coefficients.
The constant term likewise lies in L. Therefore
\[
y=q\theta+r,\qquad q,r\in L,\qquad q^2=-e/2\ne0,
\qquad O=L[\theta],\quad \tau_0:=N\theta\in L^*.
\tag{5}
\]
The equality O=L[theta] implies that theta is affine in the original
v. No square root has been adjoined to the retained coefficient field.
Only a temporary coefficient extension was used to justify (5).

Use V=theta as the polynomial parameter. Coefficient derivatives now
fix V, agree with the old partials on L, and still commute. The
triangular parameter change gives the exact full calibration
\[
J_{t,s,V}(X)=-a_0^4/\tau_0\in L^*.
\tag{6}
\]
This is independent of both V and X. The coefficient of V in the
sliced third relation is
\[
\ell_s=2qr+q n_t-2q n_s p+n_{ts}p-n_s^2.
\tag{7}
\]
Neither (4) nor (7) asserts that the full H_P vanishes on the line.

## 2. The full scalar splits into two exact alternatives

Insert y=qV+r into the full map (3). Its vector of V coefficients is
\[
\mathcal V=(q,\ 2tq+1,\ X-2pq-n_s).
\tag{8}
\]
Because the rows are affine in V, the V-squared coefficient of the
determinant is det(V_t,V_s,V), with these three vectors as columns.
Using n_ss=-2q^2, its X coefficient is
\[
[XV^2]J=-2q q_s.
\tag{9}
\]
The scalar (6) and q nonzero imply q_s=0. Once this is substituted,
the remaining coefficient is exactly
\[
[V^2]J=2q(p_s-q)(q_t-2q^2)=0.
\tag{10}
\]
These are coefficients of the complete literal determinant, not
coefficients of a determinant formed only from intercepts.

Let F=ker_L(partial_s). It is finite over C(t), and its t-derivative
has constant field C. Thus q belongs to F. Exact integration in s
now gives
\[
n=-q^2s^2+B(t)s+f(t),\qquad B,f\in F.
\tag{11}
\]
For example B=n_s+2q^2s has zero s-derivative, and then the displayed
remainder defining f does too. This is not a rational-function ansatz.
Since L is a field, (10) leaves p_s=q or q_t=2q^2, including their
possible intersection.

## 3. The p_s=q alternative has dependent columns

Suppose p_s=q. There is a(t) in F with p=qs+a. Put
\[
C=B+2qa=2pq+n_s\in F.
\tag{12}
\]
Expand the XV coefficient of the full determinant using (7),(11)
and q_s=0. The result is
\[
[XV]J=2q\{qB+2a q^2-r_s\}.
\tag{13}
\]
Its vanishing forces r_s=qC. This makes the determinant vanish by a
short exact column identity. Indeed, differentiation of (3) at fixed
t,V,X gives
\[
\begin{aligned}
Y_s&=q(X+C),\\
Z_s&=(2tq+1)(X+C),\\
W_s&=(X-C)(X+C),
\end{aligned}
\qquad
\begin{aligned}
Y_V&=q,\\ Z_V&=2tq+1,\\ W_V&=X-C.
\end{aligned}
\tag{14}
\]
For the last s-derivative use (7): its constant term is
-2p r_s-2q n_s p-n_s^2=-C^2, while the V terms cancel because
n_ss=-2q^2. Hence the s-column is (X+C) times the V-column. This
contradicts (6). No condition on q_t, B, or a was imposed or divided by.

We have therefore proved
\[
p_s\ne q,\qquad q_t=2q^2.
\tag{15}
\]

## 4. The remaining reciprocal slope has an actual normalization

Since q belongs to F and is nonzero, differentiation of -1/(2q)
gives one. The constants of the exact t-derivative on F are C, so
\[
q=-\frac1{2(t-\tau)},\qquad \tau\in\mathbb C.
\tag{16}
\]
Normalize tau by the actual polynomial automorphism
\[
X_1=X,\quad Y_1=Y-\tau X^2,\quad
Z_1=Z-2\tau Y+\tau^2X^2,\quad W_1=W.
\tag{17}
\]
Its inverse replaces tau by -tau. It has Jacobian one and preserves
X^2Z-Y^2 exactly. The new data are t1=t-tau, s1=s, p1=p, theta1=theta,
y1=y, and k1=s1; n1 is n expressed in t1,s1. The literal Z1-partial
is exactly the old Z-partial, so the selected N and L are unchanged.
Both the coefficient and actual bad-slot determinants are one, and
(6) is retained. The actual intercept returns are rebuilt in this
polynomial frame. We now drop subscripts and have
\[
q=-1/(2t),\qquad n=-s^2/(4t^2)+B(t)s+f(t).
\tag{18}
\]
No translation by an arbitrary element of F has been used.

Define the coefficient-field function xi=2tp+s. By (15),
xi_s=2t(p_s-q) is nonzero. Thus t,xi are algebraically independent,
L is finite over C(t,xi), and the exact partials in these new
parameters commute. They restrict on F to its original derivative
in t and zero derivative in xi. The change is only in the coefficient
field. In particular xi is not declared an actual polynomial coordinate.

In this frame Z has zero V coefficient. Write
\[
\begin{aligned}
z&=2tr+p^2+n\in L,\qquad Z=z+\xi X+t^2X^2,\\
Y&=-V/(2t)+r+pX+tX^2,\qquad p=(\xi-s)/(2t).
\end{aligned}
\tag{19}
\]
Eliminating V through the actual Y in (3) gives
\[
W=I(t,\xi,X)-F_0(t,\xi,X)Y,\qquad I\in L[X],
\qquad F_0=2tX+\xi/t-2tB.
\tag{20}
\]
Indeed the V coefficient of W is X+p/t-n_s=X+xi/(2t^2)-B,
and V=-2tY+2tr+(xi-s)X+2t^2X^2. This proves (20) without
assuming any formula for ell, r, or the lower coefficients of I.

The exact successive parameter factors are xi_s and Y_V=-1/(2t).
Consequently the full Jacobian in (t,xi,Y), holding actual X fixed, is
\[
J_{t,\xi,Y}(X)=\frac{2t a_0^4}{\tau_0\xi_s}\in L^*.
\tag{21}
\]
In particular it is independent of Y and X. Although Y is now used
as a field parameter, it remains the same original coordinate.

## 5. The Y coefficient forces an impossible original-coordinate square

The determinant of the rows Y,Z,I-F0Y in the variables (t,xi,Y) is
\[
Z_t I_\xi-Z_\xi I_t+
Y\{Z_\xi(F_0)_t-Z_t(F_0)_\xi\}.
\tag{22}
\]
Its Y coefficient vanishes by (21). Put
C0=xi/t^2+2B+2tB'. From (19),(20) that coefficient is precisely
\[
(2z_\xi-C_0)X-C_0z_\xi-z_t/t.
\tag{23}
\]
Since actual X is transcendental over K, its two coefficients vanish:
\[
z_\xi=\frac\xi{2t^2}+B+tB',\qquad
z_t=-2t z_\xi^2.
\tag{24}
\]
Differentiate the first equality in t and the second in xi. Their
compatibility is
\[
tB''+4B'+2B/t=0,\qquad (t^2B)''=0.
\tag{25}
\]
This identity is in the exact field F. Its derivative constants are
C, so exact integration gives B=b1/t+b2/t^2 with b1,b2 complex.
Equation (24) then yields
\[
z=\frac{(\xi-2b_2)^2}{4t^2}+z_0,\qquad z_0\in\mathbb C.
\tag{26}
\]
For precision, subtract the displayed square from z: both its t and
xi derivatives are zero. The joint constants in the finite extension
L/C(t,xi) are C. This proves the assertion about z0 without assuming
L=C(t,xi) or integrating in a presumed rational field.

Substituting (26) in the full original Z expression (19) gives
\[
\boxed{Z-2b_2X-z_0=
\left(tX+\frac{\xi-2b_2}{2t}\right)^2
\quad\text{in }\operatorname{Frac}\mathcal B.}
\tag{27}
\]
The left side is an irreducible coordinate polynomial of the actual
UFD C[X,Y,Z,W]. Its valuation at its own prime factor is one, whereas
the valuation of every square in the fraction field is even. This
is impossible. Equivalently, normality would put the square root in
the polynomial ring, whose degree in the actual variable Z cannot
then square to degree one.

Thus the remaining alternative (15) is also impossible, proving
\[
\boxed{\ k=s,\ n_{ss}\ne0\quad\Longrightarrow\quad\sigma\notin L\ }
\tag{28}
\]
under the full actual hypotheses (1). The conclusion is an exclusion
of this constant-sigma branch, not recognition of all n_ss nonzero.

## 6. Scope, prior boundaries, and verification

The related constant-sigma note
[350](principal-paraboloid-moving-first-slope-constant-sigma-exclusion-pass350-working.md)
treats n_ss=0 with n_ts nonzero; it does not supply the present case.
The present proof does not assume reducibility of the full third
surface. It uses a factorization only after setting sigma to its
coefficient value, then returns to the full literal determinant.
In particular a surviving full H_P is never discarded. The fourth
potential's unit-minor theorem is not needed for this exclusion.

The complete264,296,350 sources were freshly read. Independent
unsaved calculations 5a25a0 and95ed36 reconstructed the initial
full-J coefficients and the column-dependence branch. Calculation
9da00d checked the literal elimination (19),(20), the coefficient
(23), both mixed derivatives, and the full-X square identity.
These exact controls supplement the written field and polynomial-ring
arguments; they do not establish them by finite sampling.

No saved checker was executed, imported, compiled, or rerun by this
author. No earlier note or canonical index was edited. No unrestricted
cancellation, historical novelty, external expert review, or
proof-assistant certification is claimed.
