# A quadratic hodograph normal form for variable transverse coupling

Working result: in the actual reducible-surface projected-line sector,
assume \(m_s\ne0\), where \(m=k_s\). Then there are complex
polynomials h,l,d of degree at most two, with h nonzero, such that
\[
2h(t)\bigl(s-d(t)\bigr)=\bigl(k+l(t)\bigr)^2.
\tag{1}
\]
This follows from the complete cubic part of the factorization,
without choosing which surface factor vanishes and without dividing
by \(\sigma_v\) or \(m_t\).

An explicit actual polynomial reframe, with polynomial inverse,
then puts the coefficient relation in the form
\[
k^2=2h(t)s,\qquad
m=\frac{h(t)}k,\qquad
m_s=-\frac{h(t)^2}{k^3}\ne0.
\tag{2}
\]
The full initial kernel, selected derivation, two exact returns,
scalar calibration, affine intrinsic degrees and reducible surface
are retained. The note does not recognize or exclude this remaining
sector. In particular no field-valued hodograph is itself declared
to be an ambient coordinate.

## 1. Exact retained scope and the two possible line directions

Retain the complete actual chart264, the fourth potential and raw
determinant identities of the fully read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the reducible-surface and affine-line results of the fully read
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md)
and [309](principal-paraboloid-reducible-line-affine-generators-pass309-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\qquad a=EX\ne0,\\
[L:\mathbb C(t,s)]<\infty,\qquad
O=L[v]=L[\sigma,\theta],\qquad K=\mathbb C(y,z,w)=L(v),\\
y,\sigma,\theta\text{ affine in }v,\qquad
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{gathered}
\tag{3}
\]
The coefficient partials commute, fix v and have joint constants
exactly \(\mathbb C\). The literal Z-partial has selected shift four
and leading derivation N. Assume \(m_s\ne0\) throughout.

Let \(H_0=H-h_0=U^2+A_1U+A_0\). Its reducibility gives two
polynomial factor coefficients with sum A1 and product A0. Here
\[
(A_1)_2=-\frac{2P(m_tP+m_sV)}m,\qquad \deg A_0\le3.
\tag{4}
\]
Since \(m_s\ne0\), (4) is nonzero and its two displayed linear
factors are distinct. Exactly one surface factor coefficient is
quadratic and the other has degree at most one. Indeed both
quadratic would make their product have degree four.
These are degree statements, not a choice of the selected factor.

If \(\alpha=y_v,\beta=\sigma_v,\gamma=\theta_v\), the unit factor
difference makes \(H_U^{\rm ev}\) constant in v. Its quadratic
coefficient gives
\[
\beta(m_t\beta+m_s\gamma)=0.
\tag{5}
\]
Whole return ensures \((\beta,\gamma)\ne(0,0)\). Thus either
\(\beta=0,\gamma\ne0\), or \(\beta\ne0\) and
\(\gamma/\beta=-m_t/m_s\). We keep both alternatives. All arguments
until the final normal form are independent of this choice.

## 2. The entire raw cubic part has two necessary divisors

Use the literal formal Taylor polynomials of264 and296. Set
\[
F_2=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2,\qquad
\Lambda=m_tP+m_sV.
\]
From the raw formula
\[
A_0=F_V(\ell-F)/m+H_3(k)+H_2(n)-\ell_tP-\ell_sV-h_0
\]
the entire degree-three part is
\[
(A_0)_3=H_3(k;P,V)-\frac{\Lambda F_2}{m}.
\tag{6}
\]
The arbitrary lower coefficients n,ell,h0 do not occur in (6).

Since the cubic part of the product of the two factor coefficients
is their quadratic part times the affine factor's linear part,
(4) divides (6). This remains true if the affine factor is constant
or zero: the cubic part is then zero. In particular both P and
Lambda divide (6).

The coefficient of \(V^3\), which must vanish by P-divisibility, is
\[
0=[V^3](A_0)_3=\frac{m_{ss}}6-\frac{m_s^2}{2m},
\qquad mm_{ss}-3m_s^2=0.
\tag{7}
\]
Because \(m_s\ne0\), Lambda-divisibility can be tested at
\(V=-m_tP/m_s\). The second term of (6) vanishes there, giving
\[
k_{ttt}-3k_{tts}\frac{m_t}{m_s}
 +3k_{tss}\frac{m_t^2}{m_s^2}
 -k_{sss}\frac{m_t^3}{m_s^3}=0.
\tag{8}
\]
No condition that \(m_t\ne0\) has been imposed.

## 3. An exact coefficient hodograph, not an actual reframe

Temporarily take \(r=k\) as a coefficient variable and write
\(s=\mathscr H(t,r)\). Since \(k_s=m\ne0\), t,r are independent
and L is finite over \(\mathbb C(t,r)\). The new commuting
coefficient partials are
\[
\partial_{t,\mathrm{new}}
 =\partial_{t,\mathrm{old}}-\frac{k_t}{m}\partial_{s,\mathrm{old}},
\qquad
\partial_r=\frac1m\partial_{s,\mathrm{old}}.
\tag{9}
\]
They are the unique extensions from the rational base to L.
Let \(\mathcal F=\ker_L\partial_r\), finite over \(\mathbb C(t)\).
On \(\mathcal F\) the new t-partial equals the old one, and its
constants are exactly \(\mathbb C\). Primes below denote this
extended t-partial, not a rationality assumption on \(\mathcal F\).

The inverse derivative identities are
\[
m=\frac1{\mathscr H_r},\qquad
k_t=-\frac{\mathscr H_t}{\mathscr H_r},\qquad
\partial_{s,\mathrm{old}}=\frac1{\mathscr H_r}\partial_r.
\tag{10}
\]
Consequently
\[
mm_{ss}-3m_s^2=-\frac{\mathscr H_{rrr}}{\mathscr H_r^5}.
\tag{11}
\]
Equation (7) gives \(\mathscr H_{rrr}=0\), so exact integration in
r gives
\[
\mathscr H(t,r)=\frac{A(t)}2r^2+B(t)r+C(t),
\qquad A,B,C\in\mathcal F.
\tag{12}
\]
Here \(\mathscr H_r\ne0\), and \(m_s\ne0\) implies \(A\ne0\)
by \(m_s=-A/\mathscr H_r^3\).

## 4. The second cubic divisor makes three coefficients complex quadratics

We translate (8), keeping its direction fixed during each formal
Taylor derivative. Put \(q=-m_t/m_s\). The first derivative of
r along the old direction \((1,q)\) is
\[
r_1=\frac{q-\mathscr H_t}{\mathscr H_r}
    =-\frac{\mathscr H_{tr}}A.
\tag{13}
\]
In particular
\(\mathscr H_{tr}+A r_1=0\). Expanding
\(\mathscr H(t+\epsilon,r(\epsilon))=s+q\epsilon\) to third
order, the terms containing the second derivative of r have
coefficient \(3(\mathscr H_{tr}+Ar_1)=0\).
Since \(\mathscr H_{rrr}=0\), equation (8) is therefore equivalent to
\[
\mathscr H_{ttt}
 -\frac{3\mathscr H_{tr}\mathscr H_{ttr}}A
 +\frac{3\mathscr H_{tr}^{\,2}A'}{A^2}=0.
\tag{14}
\]
This is a polynomial identity in the independent variable r.
It is not the derivative along a moving vector field.

Complete the square in (12), purely in the coefficient field:
\[
h=\frac1A,\qquad l=\frac BA,\qquad
d=C-\frac{B^2}{2A},\qquad
\mathscr H=\frac{(r+l)^2}{2h}+d.
\tag{15}
\]
The coefficients of \(r^2,r,1\) in the left side of (14) are,
respectively,
\[
-\frac{h'''}{2h^2},\qquad
\frac{l'''}h-\frac{l h'''}{h^2},\qquad
d'''+\frac{l l'''}h-\frac{l^2h'''}{2h^2}.
\tag{16}
\]
Thus \(h'''=l'''=d'''=0\). Each is in \(\mathcal F\).
The exact constant field then gives
\[
\begin{aligned}
h&=\rho_2t^2+\rho_1t+\rho_0\ne0,\\
l&=l_2t^2+l_1t+l_0,\qquad
d=d_2t^2+d_1t+d_0,
\qquad \rho_i,l_i,d_i\in\mathbb C.
\end{aligned}
\tag{17}
\]
For example \(h''\) is killed by both old coefficient partials,
so is complex; subtracting its quadratic integral and repeating
proves the assertion. The same argument applies to l,d, without
identifying \(\mathcal F\) with \(\mathbb C(t)\).
Putting \(r=k\) back into (15) proves (1).

## 5. Actual polynomial normalization and its inverse

Only now use the complex coefficients established in (17).
Put \(c_0=l_2/2\) and define
\[
\begin{aligned}
X_*&=X+c_0,\\
Y_*&=Y-\frac{l_1}{2}X_*,\\
Z_*&=Z+l_0X_*,\\
W_*&=W-d_2Z_*-d_1Y_*-d_0X_*^2.
\end{aligned}
\tag{18}
\]
These actual polynomial coordinates have the explicit inverse
\[
\begin{aligned}
X&=X_*-c_0,\\
Y&=Y_*+\frac{l_1}{2}X_*,\\
Z&=Z_*-l_0X_*,\\
W&=W_*+d_2Z_*+d_1Y_*+d_0X_*^2.
\end{aligned}
\tag{19}
\]
Both compositions are the identity. These formulas are not
coefficient-field changes of the original coordinates.

The weighted leading map is invertible: it fixes the X,Y,Z leaders
and replaces the W leader by itself minus
\(d_2Z+d_1Y+d_0X^2\) at the initial level.
It therefore preserves the full initial ideal \((X^2Z-Y^2)\).
The actual degree profile remains1222, since t and s are independent
and \(s-d(t)\ne0\). Also \(EX_*=a\).

Direct substitution of \(X=X_*-c_0\) into the full map296 gives
\[
\begin{aligned}
t_*&=t,\qquad s_*=s-d(t),\qquad k_*=k+l(t),\\
y_*&=y-c_0\sigma+c_0^2t,\qquad
\sigma_*=\sigma-2c_0t-l_1/2,\\
\theta_*&=\theta-2c_0s
           -d_2(2t\sigma_*+k_*)-d_1\sigma_*.
\end{aligned}
\tag{20}
\]
In particular \((y,\sigma,\theta)\mapsto
(y_*,\sigma_*,\theta_*)\) is an invertible affine L-map, and its
restriction to the two projected variables is invertible affine.
All intrinsic affine degrees and the projected line are retained;
\((\sigma_*)_v=\sigma_v\), including its possible zero value.

The new coefficient partials satisfy
\[
\partial_{t,*}=\partial_t+d'(t)\partial_s,\qquad
\partial_{s,*}=\partial_s,\qquad m_*=m.
\tag{21}
\]
For an explicit check that the first potential still has a
coefficient-field constant, its transformed constant is
\[
n_*=n-c_0k-c_0^2t^2+\frac{k_tl'}2+\frac{(l')^2}4
                        +m(d_2k_*+2c_0s).
\tag{22}
\]
Substitution of (20)--(22) into
\(z_*=2ty_*+\sigma_*^2+(k_*)_{t,*}\sigma_*+m\theta_*+n_*\)
recovers the full transformed Z-intercept.

The literal new Z-partial is
\(\partial_{Z_*}=\partial_Z+d_2\partial_W\).
The old W-partial has shift at most three by the retained omitted
leading-triple criterion, whereas the old Z-partial has exact shift
four. Hence its selected coefficient N is unchanged.
In particular L and its localization O are unchanged.
The actual intercept return applies to the new polynomial frame,
giving \(K=\mathbb C(y_*,z_*,w_*)\); the affine intrinsic map in
(20) also directly preserves whole O-return.

## 6. Full scalar and formal surface-level transport

At fixed \(X_*\), the original X equals \(X_*-c_0\).
The row transformations in (18) have determinant one.
The coefficient change \((t,s)\mapsto(t,s_*)\) also has
Jacobian one. Therefore the exact full scalar is retained:
\[
J_*(X_*)=J(X_*-c_0)=-a^4.
\tag{23}
\]
This does not merely preserve a top coefficient.

For clarity, reducibility of the formal surface can also be retained.
Before imposing either surface or fourth level, the universal296
identities after the first two potentials make the raw determinant
have degree at most two in X. Translation and (18) leave that fact
unchanged. The new first potential has the coefficient constant
(22). Its next raw coefficient is the line derivative of the new
second-potential expression. Since the new cubic coefficient is zero
for arbitrary independent intrinsic jets, that expression is formally
constant in the three intrinsic variables. Thus it defines
\(\ell_*\in L\), not an intercept-dependent parameter.

The quadratic determinant coefficient is unchanged by X-translation.
It is the line derivative of H in the old variables and of H* in
the new ones. Apply this identity to arbitrary independent first
jets of y,sigma,theta, with the affine substitution (20).
All three formal derivatives of the difference vanish. Hence
\[
H_*(y_*,\sigma_*,\theta_*)-H(y,\sigma,\theta)
\]
is formally a coefficient constant; equivalently, with (20) used as
an affine substitution of independent U,P,V,
\[
(H_*-h_{0,*})(U_*,P_*,V_*)=H_0(U,P,V).
\tag{24}
\]
The new level constant is the old one plus that coefficient
constant. This is the same raw-coefficient method used in302 to
justify its arbitrary-n normalization. It uses identities before
evaluation on the actual line, so preserves the formal factorization,
not only its selected values.

Finally (1),(20),(21), after dropping stars, give (2).
Here k and h(t) are nonzero in L, and
\[
m_t=\frac{h'(t)}{2k}
\tag{25}
\]
for the new fixed-s derivative. No division by \(h'\) is made, so
the constant, linear and quadratic possibilities for h are all
retained.

## 7. Precise remaining boundary and verification scope

The two possible projected-line directions remain those in (5);
they have not been recognized or excluded. The necessary coefficient
normal form (2) is substantive, but no new generator has been
declared an ambient coordinate or an actual invariant-coordinate
criterion established. Other coefficient potentials and the full
actual return still impose further conditions.

The complete296,302 and309 sources were freshly read before this
derivation. Unsaved exact algebra reconstructed the entire raw cubic
(6), its V-cubed coefficient, the hodograph identities (11),(14),
all three coefficients (16), the full intrinsic transport (20),
the first-potential constant (22), and both inverse compositions
(18),(19). The field integrations and formal-level transport are
the written arguments, not finite-sample claims.

No saved checker was executed, imported, compiled or rerun by this
author. No retained source, index or packet was changed. There is no
unrestricted cancellation, realization, novelty or formal-verification
claim.
