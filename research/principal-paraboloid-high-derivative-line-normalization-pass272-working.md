# An actual normal form for the high-derivative projected line

In the supplied branch271, a nonzero third coefficient derivative
forces a projected line. One of its two possible directions is
impossible. The other forces the coefficient k to be a complex
quadratic and admits an explicit actual coordinate change making
k zero and the first intercept constant along the intrinsic action.

This is an actual normalization, not recognition. The remaining
canonical line still has to yield an invariant ambient coordinate.

## 1. Precise retained hypotheses and identities

Retain all actual hypotheses of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md):
the globally sliced complex polynomial four-ring, time degrees
(1,2,2,2), full initial kernel (X^2 Z-Y^2), literal Z-partial of
shift four, and branch k_s=0, n_s nonzero. Its exact coefficient
reparameterization has
\[
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
H=s\in L,\quad H_n\ne0,\quad k\in F,
\quad L[y,\sigma]=L[v],\quad Nv=1.
\tag{1}
\]
The constants of the t-derivative on F are exactly C. All
coefficient partials below hold the formal variables U,P fixed.

Use271's polynomials
\[
\begin{aligned}
\gamma&=2P+k',& B_1&=2U+k''P,\\
\mathscr A&=\gamma U+k''P^2/2,
&\mathscr C&=U^2+k''PU+k'''P^3/6,\\
\mathscr W&=\omega+H_{nn}\mathscr A^2/2
 -(H_{nt}P+T_n)\mathscr A-H_n\mathscr C
 +H_tU+H_{tt}P^2/2+T_tP,\\
Q_U&=\gamma\mathscr W_n-\mathscr W_P,
&Q_P&=B_1\mathscr W_n-\mathscr W_t.
\end{aligned}
\tag{2}
\]
Here \(T,\omega\) lie in \(L\). The actual intercept satisfies
\(w=\mathscr W(y,\sigma)\). The full nonzero scalar Jacobian gives
the selected-component identity
\[
Q-q_0=\eta G+G^2R,\qquad \eta\in L^*.
\tag{3}
\]
In particular, if G is a line, its evaluated gradient is
exactly eta times that line's constant gradient.
No derivative of a moving line coefficient is implicit in (3).

Assume for the main conclusion that
\[
H_{nnn}\ne0.
\tag{4}
\]
By271, G has degree one and its top direction is either
P or 4U+k''P. Thus either sigma lies in L or
4y+k''sigma lies in L. The projected entries are not both
constant because they generate L[v].

## 2. A constant second projection forces H to be affine in n

This section does not require (4). Suppose sigma lies in L.
Then L[y]=L[v], so y is affine and nonconstant. Choose
G=P-sigma. Equation (3) gives
\[
Q_U(y,\sigma)=0,\qquad Q_P(y,\sigma)=\eta\in L^*.
\tag{5}
\]
Since substitution U=y is injective on L[U], all positive
U-coefficients in these evaluations vanish.

Before evaluating \(P=\sigma\), the coefficient of \(U^2\) in
\(\mathscr W\) is \(H_{nn}\gamma^2/2-H_n\). Directly from (2),
\[
\begin{aligned}
[U^2]Q_U&=\gamma^3H_{nnn}/2-3\gamma H_{nn},\\
[U^3]Q_P&=\gamma^2H_{nnn}-2H_{nn}.
\end{aligned}
\tag{6}
\]
Evaluate gamma at 2sigma+k'. Both expressions vanish by (5).
Twice the first minus gamma times the second is
-4gamma H_nn. If gamma is nonzero, H_nn=0. If gamma is zero,
the second expression directly gives H_nn=0. Thus in every case
\[
\boxed{\sigma\in L\quad\Longrightarrow\quad
H_{nn}=0,\qquad H=h_1n+h_0,\quad h_i\in F,\ h_1\ne0.}
\tag{7}
\]
The integration uses the exact constants in (1); h1 is nonzero
because H_n is nonzero. In particular the constant-sigma line
is impossible under (4). Partial derivatives were taken before
evaluation at sigma; no false assumption sigma_n=0 was used.

## 3. The other line makes k a complex quadratic

Under (4), the remaining line is
\[
y=C-\frac{k''}{4}\sigma,\qquad C\in L,
\qquad L[\sigma]=L[v].
\tag{8}
\]
Choose G=4U+k''P-4C. Its U-gradient is four, so (3) makes
Q_U(C-k''P/4,P) a nonzero scalar in L.

The fourth-degree coefficient of this substituted polynomial is
\[
[P^4]\,Q_U(C-k''P/4,P)=-H_{nn}k'''/3.
\tag{9}
\]
There is a short direct way to check this coefficient. Along the
line, \(\mathscr A\) is affine in \(P\) because its two quadratic
terms cancel. The only cubic term of \(\mathscr C\) is
\(k'''P^3/6\). Therefore the cubic term of \(\mathscr W_n\)
after substitution is \(-H_{nn}k'''P^3/6\). Multiplication
by \(\gamma=2P+k'\) supplies (9). The other term \(\mathscr W_P\) has total degree
at most three before line substitution and cannot contribute
degree four. This calculation differentiates first and substitutes
the line afterwards.

Equation (9) vanishes. Condition (4) implies H_nn is nonzero
as a field element, since its n-derivative is nonzero. Hence
k'''=0. The exact t-constants of F give
\[
\boxed{k=\frac{\kappa}{2}t^2+\alpha t+\beta,
\qquad \kappa,\alpha,\beta\in\mathbb C.}
\tag{10}
\]
This conclusion includes k''=0 and does not assume F rational.

## 4. A literal complex-coefficient coordinate change

Put c=kappa/4. The following is an actual affine automorphism:
\[
\boxed{
X_*=X-c,\quad Y_*=Y+\frac{\alpha}{2}X_*,\quad
Z_*=Z-\beta X_*,\quad W_*=W.
}
\tag{11}
\]
Its polynomial inverse is
\[
X=X_*+c,\quad Y=Y_*-\frac{\alpha}{2}X_*,\quad
Z=Z_*+\beta X_*,\quad W=W_*.
\tag{12}
\]
Both compositions are the identity. Every correction has strictly
smaller E-degree than its affected coordinate, so all leading
coefficients and the full initial kernel remain unchanged.
The literal partial d/dZ_* equals the old d/dZ. Its selected
shift, intrinsic action N and exact field L are unchanged.

In the new actual chart the expansions are
\[
\begin{aligned}
Y_*&=y_*+\sigma_*X_*+tX_*^2,\\
Z_*&=z_*+2t\sigma_*X_*+t^2X_*^2,\\
W_*&=w_*+\theta_*X_*+HX_*^2,
\end{aligned}
\tag{13}
\]
where literal substitution gives
\[
\begin{aligned}
\sigma_*&=\sigma+2ct+\alpha/2,& y_*&=C+tc^2\in L,\\
z_*&=z+c(2t\sigma+k)+t^2c^2,&
w_*&=w+c\theta+c^2H,\\
\theta_*&=\theta+2cH,& k_*&=0.
\end{aligned}
\tag{14}
\]
For instance the new middle linear coefficient minus 2t times
the new first linear coefficient is
k-2ct^2-alpha t-beta=0 by (10).

The first potential becomes
\[
z_*=2ty_*+\sigma_*^2+n_*,\qquad
n_*=n-3c^2t^2-\alpha ct+\beta c-\alpha^2/4.
\tag{15}
\]
In particular n_*-n lies in C[t]. Thus (n_*)_s=n_s is nonzero,
the new derivative d/dn_* equals d/dn on L, and its exact
constant field is still F. The nonzero derivative H_nnn in (4)
survives this reparameterization.

The actual map (11) has determinant one and X=X_*+c has
coefficient derivatives zero at fixed X_*. Hence the calibrated
Jacobian -a^4 H_n is unchanged, also after n becomes n_*.
Whole-line and strong field returns are preserved by the actual
coordinate-frame argument of264, not inferred merely from a
coefficient-field substitution.

## 5. Exact remaining boundary

Under (4), the original problem in271 has been reduced by actual
complex polynomial coordinates to
\[
k=0,\qquad y\in L,\qquad L[\sigma]=L[v],\qquad
H_n\ne0,\quad H_{nnn}\ne0,
\tag{16}
\]
with every other actual principal-chart assumption retained.
The proof does not declare this canonical line impossible and does
not produce an E-invariant ambient coordinate. In particular Ny=0
does not make Y invariant: Y=y+sigma X+tX^2 still depends on X.

The constant-sigma conclusion (7) holds independently of (4).
No claim is made here about the nonlinear plane components, which
271 already places in H_nnn=0. Neither the full principal1222
sector nor unrestricted cancellation is recognized by this note.

Root fully read271 before deriving (6),(9),(11)--(15).
Fresh unsaved symbolic calculations checked the formal coefficient
identities and the literal new intercepts, with derivatives taken
before evaluation. Geometry independently reconstructed (6) and
all actual coordinate substitutions. These finite identities do not
replace the exact-field and original-ring arguments above.
No completed saved checker was rerun, imported or compiled.
No historical novelty or human expert certification is asserted.
