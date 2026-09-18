# The zero cubic gate excludes the sigma-dominant pair (2,3)

Working exclusion: retain the full actual385 chart and387, assume
(deg theta,deg sigma)=(2,3), and put
Ecal=e_s/6-e^2/(2nu), where nu=n_s and e=n_ss.
The branch Ecal=0 is impossible. The proof uses the complete fourth
potential, including derivatives of its evaluated level, and one
coefficient of the literal scalar determinant.

The remaining Ecal nonzero branch is not addressed. No rationality
of the exact coefficient field or original-coordinate status of an
intrinsic parameter is assumed. No earlier source is changed.

## 1. Actual entry, normalization and the literal parametrization

Retain all actual hypotheses of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
and the accepted compatibility conclusion of
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md).
Thus k=s, L is finite over C(t,s), its exact coefficient partials
commute, and O=L[v]=L[y,sigma,theta] is the entire intrinsic line.
The original ring is C[X,Y,Z,W]=A0[u], with a global slice, exact
time profile(1,2,2,2), full initial ideal(X^2Z-Y^2), and selected
literal leading derivation N=[u^4]partial_Z on A0. It kills L and
a0=EX, Nv=1, and the literal determinant is -a0^4 in L*.
The strong return K=C(y,z,w)=L(v) also remains in force.

By387, n=gamma*t+f with gamma complex and f_t=0. The actual change
X*=X, Y*=Y+gamma/2, Z*=Z, W*=W has polynomial inverse subtracting
gamma/2. It gives y*=y+gamma/2, n*=n-gamma*t=f and ell*=ell,
with t,s,sigma,theta,z,w unchanged. Its leading map and full initial
ideal are unchanged, the literal Z-partial is identical, both
intercept returns are preserved by a complex translation, and the
full determinant and parameter calibration are unchanged. These
are the same direct actual gates written in390 Section1.
Drop stars and put
\[
\mathcal S=\ker_L\partial_t,\qquad
n=f\in\mathcal S,\quad \nu=n_s\ne0,\quad e=n_{ss}\ne0,
\qquad p=\ell_t,\quad C=\ell_s+\nu^2.
\tag{1}
\]
We do not assume S=C(s) or L=S(t). The joint constants of the
two coefficient derivatives on L are C. Commutation makes S stable
under partial_s, and t is transcendental over S.

Assume (deg theta,deg sigma)=(2,3). The remainder of385 is now
r=y+p/(2nu), and its intrinsic degree is one. Consequently
\[
O=L[r],\qquad \rho=Nr\in L^*,\qquad
J_{t,s,r}(X)=-a_0^4/\rho\in L^*.
\tag{2}
\]
The exact coefficient partials extend fixing r. Their restriction
to L, hence their action on every evaluated level, is unchanged.
Write
\[
\theta=ar^2+br+c,\qquad a\in L^*,\quad b,c\in L,
\qquad y=r-\frac p{2\nu}.
\tag{3}
\]
Here b means the linear coefficient of theta, not n_ts, which is zero.

The complete third potential gives
\[
\begin{aligned}
\sigma={}&\frac{ea^2}{4\nu}r^3+\frac{eab}{2\nu}r^2
 +\left(\frac1{2\nu}+\frac{e(b^2+2ac)}{4\nu}
                         -\frac{Ca}{2\nu}\right)r\\
&-\frac p{2\nu^2}+\frac{ebc}{2\nu}-\frac{Cb}{2\nu},\\
h_0={}&\frac{p^2}{4\nu^2}+\nu\ell+\frac e2c^2-Cc.
\end{aligned}
\tag{4}
\]
Indeed the third level after the shift to r is
r^2-2nu*r*sigma-(p/nu)r+e*theta^2/2-C*theta+
p^2/(4nu^2)+nu*ell-h0. Its constant coefficient gives h0 in(4),
and division of the remaining polynomial by 2nu*r gives sigma.

## 2. The high genuine-Q coefficients and the zero gate

For independent formal U,P,V, the genuine fourth polynomial is
\[
\begin{aligned}
Q={}&(2\ell_sP-2ePV-p)U+\frac{e_s}{6}V^3
 -\frac{\ell_{tt}}2P^2-\ell_{ts}PV\\
&-\frac{\ell_{ss}+2\nu e}{2}V^2-(h_0)_tP
 +(e\ell+\nu\ell_s-(h_0)_s)V.
\end{aligned}
\tag{5}
\]
Its evaluation at(y,sigma,theta) belongs to L. In(5), both derivatives
of h0 are the full derivatives of(4), including c_t and c_s.
Set
\[
\mathcal E=\frac{e_s}{6}-\frac{e^2}{2\nu},\qquad
\mathcal J=\frac{pe}{\nu}-\ell_{ts}.
\tag{6}
\]
Direct substitution of(3),(4) in the complete(5) gives
\[
\begin{aligned}
[r^6]Q&=a^3\left(\mathcal E-
                     \frac{ae^2\ell_{tt}}{32\nu^2}\right),\\
[r^5]Q\big|_{[r^6]Q=0}
 &=a^2\left(-\mathcal E b+\frac{\mathcal J ea}{4\nu}\right).
\end{aligned}
\tag{7}
\]
The second equality means substitution of
ell_tt=32nu^2*Ecal/(a e^2), whose denominators are all nonzero.

Assume from now on that Ecal=0. The two coefficients in(7) imply
ell_tt=0 and Jcal=0. Since nu_t=0, the two derivatives of p/nu
then vanish. There is a complex constant c0, allowed to be zero,
such that
\[
e_s=3e^2/\nu,\qquad p=c_0\nu,\qquad
\ell=c_0t\nu+L_0,\quad c_0\in\mathbb C,\quad L_0\in\mathcal S.
\tag{8}
\]
No division by p or c0 has occurred. The next coefficient is
\[
[r^4]Q=\frac a{2\nu}
 \big[a(3e\ell_s-\nu\ell_{ss})-2e\big]=0.
\tag{9}
\]
Here the coefficient of t in 3e*ell_s-nu*ell_ss is
c0*(3e^2-nu*e_s)=0. Hence
\[
a=\frac{2e}{3e(L_0)_s-\nu(L_0)_{ss}}\in\mathcal S^*.
\tag{10}
\]
Its denominator is nonzero by(9), a nonzero and e nonzero.

## 3. Centered rows and every lower positive Q coefficient

Put
\[
H_0=\frac{(L_0)_s+\nu^2}{e}\in\mathcal S,
\qquad d=c-\frac Ce=c-c_0t-H_0.
\tag{11}
\]
Using(8)--(10) gives the exact derivative
(H0)_s=-nu-2/(a nu). Define coefficient elements
Z0=H0+f and W0=L0-nu*H0. They belong to S and satisfy
\[
(Z_0)_s=-\frac2{a\nu},\qquad (W_0)_s=\frac2a.
\tag{12}
\]
The full intercept rows, with P denoting the actual intrinsic sigma,
are now
\[
\begin{aligned}
y={}&r-c_0/2,\\
P=\sigma={}&\frac{a^2er^3+2aber^2+(2ade+b^2e+2)r
                                  +2bde-2c_0}{4\nu},\\
\theta={}&ar^2+br+d+c_0t+H_0,\\
z={}&P^2+ar^2+br+d+2tr+Z_0,\\
w={}&W_0-\nu(ar^2+br+d)+(c_0-2r)P.
\end{aligned}
\tag{13}
\]
At this stage b,d can be arbitrary elements of L subject to the
remaining equations. They have not been made t-constant.

The complete lower coefficients of(5) can be recorded compactly.
Define
\[
\begin{aligned}
F_3={}&a^2ed d_t-4ac_0-4b,\\
F_2={}&a^2bd d_te^2+2a^2d^2e^2+2a^2dd_se\nu
       -2abc_0e-2ade+2a\nu^2-2b^2e,\\
F_1={}&2a^2dd_te+ab^2d_te+4abde+4abd_s\nu
       -4ac_0+2ad_t-8b.
\end{aligned}
\tag{14}
\]
Then, after the established high gates,
\[
[r^3]Q=-\frac e{4\nu}F_3,\qquad
[r^2]Q=-\frac1{2a\nu}F_2,\qquad
[r]Q=-\frac{de}{4a\nu}F_1.
\tag{15}
\]
These expressions include all h0 derivatives; they are not the
coefficients of an arbitrary cubic through the parametrized line.

First d is nonzero. If d=0 as a field element, F3=0 gives b=-ac0,
and the second expression in(15) is exactly -nu, a contradiction.
Thus F1,F2,F3 all vanish, and division by d is now allowed.
Let
\[
M=ac_0+b,\qquad
R_0=M(aed+2)-ab\nu^2.
\tag{16}
\]
The following exact elimination identity retains every zero branch:
\[
F_1-\frac{2b}{ade}F_2
 -\frac{2ade-b^2e+2}{ade}F_3=\frac4{ade}R_0.
\tag{17}
\]
Consequently the necessary lower-Q equations give
\[
\boxed{d\ne0,\qquad M=\frac{a^2e}{4}d d_t,
\qquad M(aed+2)=ab\nu^2.}
\tag{18}
\]

## 4. One literal scalar coefficient forces b affine in t

Set actual X=0 in the full calibrated determinant(2). This is a
polynomial specialization of the literal identity, not an assertion
about the coordinate ring of a fiber. It gives
J0=det partial(y,z,w)/partial(t,s,r), still the nonzero element
-a0^4/rho of L and independent of r.

For a finite row check, set T=ar^2+br+d. Equation(13) gives
\[
\begin{aligned}
z_t&=2PP_t+T_t+2r,&z_s&=2PP_s+T_s-2/(a\nu),\\
w_t&=-\nu T_t+(c_0-2r)P_t,
&w_s&=2/a-eT-\nu T_s+(c_0-2r)P_s.
\end{aligned}
\tag{19}
\]
Since y_t=y_s=0 and y_r=1, J0=z_t*w_s-z_s*w_t.
Differentiate P in(13), retaining a_s,b_s,d_s and b_t,d_t, using
nu_s=e, e_s=3e^2/nu and a_t=e_t=nu_t=0. Expansion has degree at
most five in r, and its highest coefficient is exactly
\[
[r^5]J_0=-\frac{ae}{4\nu^2}
       (3ae b_t+8ae+8a_s\nu)=0.
\tag{20}
\]
Every coefficient other than b_t in this equation belongs to S.
Commutation gives a_s in S as well. Thus b_t belongs to S, and
exact integration inside L gives
\[
b=B_1t+B_0,\qquad B_1,B_0\in\mathcal S.
\tag{21}
\]
No rationality of b was presumed to obtain(21).

## 5. Rationality, integrality and the zero branch finish the exclusion

Suppose first that M is nonzero. The last relation of(18) then
implies the specific rationality statement
\[
d=\frac{ab\nu^2-2M}{aeM}\in\mathcal S(t).
\tag{22}
\]
On the other hand the middle relation of(18) and(21) show that
(d^2)_t=8M/(a^2e) is affine in t over S. Subtract an explicit
quadratic antiderivative; the remainder has zero t derivative.
Therefore d^2 belongs to S[t], of degree at most two.

The element d is integral over S[t] and belongs to its fraction
field by(22). Since S[t] is integrally closed, d belongs to S[t].
In fact(22) makes it constant in t. If M has degree one in t,
both its numerator and denominator have degree at most one, so
a nonzero polynomial quotient has degree at most zero. If M is
constant, then b=M-ac0 is also constant and the same conclusion
is immediate. Hence d_t=0, contradicting nonzero M in(18).

It remains to retain M=0. Since a,e,d are nonzero, the middle
equation of(18) gives d_t=0. Its last equation gives b=0 because
a and nu are nonzero. Then M=ac0+b=0 also gives c0=0.
All coefficients of P,T,Z0,W0 in(13) now belong to S. The literal
intercept t-column is consequently
\[
(y_t,z_t,w_t)=(0,2r,0).
\tag{23}
\]
Evaluating the polynomial determinant at r=0 gives J0=0, contrary
to its nonzero scalar calibration(2). This is the final contradiction,
including the possible zero value of c0 from the start.

Thus the scoped conclusion is
\[
\boxed{\text{Under the complete actual385/387 hypotheses,}
\quad(\deg\theta,\deg\sigma)=(2,3)
\quad\Longrightarrow\quad\mathcal E\ne0.}
\tag{24}
\]
The proof does not solve the nonzero-Ecal branch, treat equal degrees,
or recognize the original invariant ring.

## 6. Evidence and precise limits

The full385 source and387 were read and checked before this work.
The actual normalization and complete n_t=0 potentials were also
rebuilt in390. No original coordinate is replaced by a coefficient-
field function. In particular r, b, d and the exact constant field S
are not promoted to original polynomial coordinates or rational fields.

Fresh unsaved b2e3a1 rebuilt(7),(9) and all lower Q coefficients from
the complete(4),(5). Calculation5b1501 rebuilt the centered versions
(14),(15). Calculation72fcd1 checked the exact elimination(17), the
d=0 residual -nu, and both centered intercept identities in(13).
Calculation3493d6 independently formed the literal scalar from the
rows(19) and obtained(20). All displayed identity residuals were zero.
The exact-field, integrality and specialization arguments are written
above and are not finite-test certification.

No saved checker was executed, imported, compiled or rerun by this
author. No earlier proof, checker or canonical index was edited.
No unrestricted cancellation, novelty, human-expert verification
or proof-assistant certification is claimed.

