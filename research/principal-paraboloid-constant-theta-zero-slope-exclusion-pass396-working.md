# Constant theta cannot have zero affine slope

Working scoped exclusion: in the full actual264 chart with k=s and
n_ss nonzero, suppose theta belongs to the coefficient field. The
affine line presentation of386 is y=lambda*sigma+r. Then lambda
cannot be zero. Four coefficients of the literal scalar suffice.

This argument does not exclude the nonzero-slope constant-theta
case. It does not apply387's nonconstant-theta conclusion to this
boundary, and it does not normalize n to a function of s.

## 1. Full actual entry and the zero-slope assumption

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the constant-theta reduction
[386](principal-paraboloid-nonlinear-constant-theta-line-gates-pass386-working.md).
In particular B=C[X,Y,Z,W]=A0[u] has the original slice, exact time
degrees(1,2,2,2), full initial kernel(X^2Z-Y^2), and the actual selected
nonzero derivation N=[u^4]partial_Z restricted to A0. Its exact kernel
field L is finite over C(t,s), with commuting coefficient partials.
Both whole-line return and strong complex-field return are retained.
The coupling is k=s and e=n_ss is nonzero.

By386, sigma is affine nonconstant on the intrinsic line and
\[
O=L[\sigma],\quad \tau=N\sigma\in L^*,\quad
\theta=h\in L,\quad y=\lambda\sigma+r,\quad\lambda,r\in L.
\tag{1}
\]
Use P=sigma as the independent intrinsic parameter. Its moving
coefficient change is already accounted for in the actual scalar
\[
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-a_0^4/\tau\in L^*,\qquad a_0=E_{\rm slice}X\ne0.
\tag{2}
\]
All derivatives below fix P and the actual X. Their restrictions to
L are the exact original coefficient partials.

Assume for contradiction that lambda=0. The highest third-potential
gate in386 gives n_tt=0. Introduce
\[
a=n_t,\quad b=n_{ts},\quad\nu=n_s,\quad e=n_{ss}\ne0,
\quad g=2r+a.
\tag{3}
\]
Here nu is a nonzero field element, because nu_s=e is nonzero.
We have a_t=0, a_s=nu_t=b and g_t=2r_t. None of a,b,g,r,r_t,r_s
is assumed nonzero. The affine intercept formula in386, with
Delta=-nu, gives the exact coefficient identity
\[
\ell_t=bh-\nu(2r+a)=bh-\nu g.
\tag{4}
\]
This follows without dividing by lambda or b.

## 2. The full literal matrix

With y=r, the original polynomial rows are
\[
\begin{aligned}
Y&=r+PX+tX^2,\\
Z&=P^2+2tr+h+n+(2tP+s)X+t^2X^2,\\
W&=-gP+\ell-\nu h+hX+sX^2.
\end{aligned}
\tag{5}
\]
Using only(3),(4), their derivative matrix in(t,s,P) is
\[
\begin{pmatrix}
r_t+X^2&r_s&X\\
g+2tr_t+h_t+2PX+2tX^2&2tr_s+h_s+\nu+X&2P+2tX\\
-2r_tP-\nu(g+h_t)+h_tX&
\ell_s-(2r_s+b)P-eh-\nu h_s+h_sX+X^2&-g
\end{pmatrix}.
\tag{6}
\]
In particular nu_t=b has not been discarded: in the third row its
term -bh cancels exactly against the bh in ell_t. This is the
unnormalized n_tt=0 family, not just the smaller n_t-constant case.

Direct expansion of(6) gives the following four coefficients:
\[
\begin{aligned}
[P^2X^0]J&=2b r_t,\\
[PX]J&=2\nu r_t-b(g+h_t),\\
[PX^0]J&=-2\{r_t(\ell_s-eh-\nu h_s)
                         +\nu r_s(g+h_t)\},\\
[P^0X^0]J&=g\{r_s(g+h_t)-r_t(h_s+\nu)\}.
\end{aligned}
\tag{7}
\]
These identities concern the full actual determinant. In particular
the PX coefficient is not obtained from its X=0 specialization.
Calibration(2) forces the first three coefficients in(7) to vanish.

## 3. Exhaustion without discarding a zero branch

First r_t must be zero. Otherwise the first equation in(7) forces
b=0; the second then becomes 2nu*r_t=0, contradicting both assumed
r_t nonzero and established nu nonzero. This argument retains b=0
from the start and uses the field property, not a generic-value test.

With r_t=0, the third equation of(7) forces
\[
r_s(g+h_t)=0,
\tag{8}
\]
since nu is nonzero. No division by r_s or g+h_t is needed.
The constant coefficient in(7) is therefore zero. But J is independent
of X,P by(2), so that constant coefficient is its full value. This
contradicts J=-a0^4/tau nonzero.

Consequently
\[
\boxed{\text{Under every actual264 hypothesis, }k=s,\ n_{ss}\ne0,
\ \theta\in L\quad\Longrightarrow\quad\lambda\ne0.}
\tag{9}
\]
In this boundary sigma has intrinsic degree one by386, so y now
also has intrinsic degree one. The nonzero-slope differential gates
of386 become available without an illicit division by zero.

## 4. Evidence and limits

The complete386 source was freshly reread through EOF in8a3fce.
Fresh unsaved15c784 rebuilt the full matrix(6) with arbitrary
coefficient jets, expanded its literal determinant and recovered
all four coefficients(7). An earlier restricted computation451c0f
set b=a=0 and agreed, but the proof uses the general15c784 result.
The zero-branch exhaustion above is the written argument, not an
inference from sampled coefficients. Independent saved-source review
is pending until recorded in the ledger.

The proof retains every actual input but needs no additional
complex-field-return argument after386. No intrinsic parameter or
coefficient-field transformation is declared an original coordinate.
It does not treat nonzero lambda, equal-degree theta and sigma,
arbitrary coupling, arbitrary-chart entry, or unrestricted cancellation.
No saved checker was executed, imported, compiled or rerun. No prior
proof or canonical record was changed, and no novelty, human-expert
review or proof-assistant certification is claimed.
