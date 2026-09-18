# The constant-first line with nonconstant parameter slope is impossible

Working result: the nonconstant complex-affine slope mode of288 cannot
have its line coefficient independent of \(t\). More precisely, in
that note's nonzero-\(\ell\) branch, \(b'\ne0\) and
\(r=a'/\ell=0\) are incompatible with the actual field return.
This excludes this supplied branch; it does not assert existence or
recognize the separate \(r\ne0\) mode.

The proof uses a literal constant translation of \(X\), then the raw
potentials of271. Its endpoint is an exact degree-three field
contradiction. No coefficient-field parameter is promoted to an
ambient coordinate, and no rationality assumption on the finite
curve field is used.

## 1. Exact entry and the meaning of r

Retain the actual hypotheses of the completely read
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md),
[277](principal-paraboloid-affine-parameter-restriction-pass277-working.md),
and the nonzero-\(\ell\) reduction in the completely read
[288](principal-paraboloid-projected-line-polynomial-reduction-pass288-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},
\quad \operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\quad
Nv=1,\quad L[y,\sigma]=L[v],\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad \ker(\partial_t|_F)=\mathbb C .
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and initially fix \(v\).
The full initial relation is not an identity between the actual
coordinates. Put \(a_0=EX\ne0\) for the slice speed.

The line and parameter slope under consideration are
\[
\begin{gathered}
y=a\sigma+d,\quad a,d\in L,\quad L[\sigma]=L[v],
\quad \sigma_v\in L^*,\\
\ell=4a+k''\ne0,\quad a\in F,\quad
r=\frac{a'}{\ell}=0,\quad d\in F,\\
H=bn+c,\quad b=\beta t+\beta_0,\quad
\beta,\beta_0\in\mathbb C,\quad \beta\ne0,\quad c,k\in F .
\end{gathered}
\tag{2}
\]
These are precisely the corresponding conclusions and extra case
condition in288. Here \(r\) means \(a'/\ell\), not the derivative
of its potential coefficient \(p\), which will occur below.

Since the derivative constants in \(F\) are complex, \(a'=0\)
makes \(a=\alpha\in\mathbb C\). The actual line scalar from288
reduces to
\[
\delta=-d'-\alpha^2\ne0.
\tag{3}
\]
We do not need288's already proved field equality \(L=F(n)\).
The relevant field equalities will be obtained again from the
rebuilt potentials and the actual return.

## 2. A literal translation makes the first intercept constant

Use the actual complex affine automorphism
\[
X_*=X+\alpha,\qquad Y_*=Y,\qquad Z_*=Z,\qquad W_*=W.
\tag{4}
\]
Its inverse is \(X=X_*-\alpha\), with the other coordinates fixed.
Both compositions are immediate polynomial identities. All leading
coefficients, exact degrees and the full initial ideal remain
unchanged. The literal \(\partial_{Z_*}\) equals \(\partial_Z\),
so its shift, intrinsic derivation \(N\) and exact field \(L\)
are unchanged.

The full old expressions are
\[
Y=y+\sigma X+tX^2,\qquad
Z=z+(2t\sigma+k)X+t^2X^2,\qquad
W=w+\theta X+HX^2,
\quad z=2ty+\sigma^2+k'\sigma+n.
\]
Substituting \(X=X_*-\alpha\) gives
\[
\begin{aligned}
y_*&=y-\alpha\sigma+\alpha^2t=d+\alpha^2t\in F,
&\sigma_*&=\sigma-2\alpha t,\\
z_*&=z-\alpha(2t\sigma+k)+\alpha^2t^2,
&k_*&=k+2\alpha t^2,\\
w_*&=w-\alpha\theta+\alpha^2H,
&\theta_*&=\theta-2\alpha H,\qquad H_*=H .
\end{aligned}
\tag{5}
\]
In particular the sign in \(k_*=k+2\alpha t^2\) is positive.
It follows from comparing the new \(Z\)-linear coefficient with
\(2t\sigma_*\); a negative sign would fail that literal comparison.

The rebuilt first potential has
\[
\begin{aligned}
z_*&=2ty_*+\sigma_*^2+k_*'\sigma_*+n_*,\\
n_*&=n+f(t),\qquad
f=-\alpha k+3\alpha^2t^2+2\alpha t k'\in F,\\
k_*''&=k''+4\alpha=\ell\ne0,\qquad
y_*'=d'+\alpha^2=-\delta\ne0 .
\end{aligned}
\tag{6}
\]
The function \(f\) need not be a complex polynomial. It is only a
coefficient-parameter shift, not part of the actual automorphism (4).
It preserves \(\partial_{n_*}=\partial_n\), hence its kernel \(F\).
The new \(t\)-partial agrees with the old one on \(F\), and
\((n_*)_s=n_s\ne0\). Also
\[
H=b n_*+(c-bf),\qquad b=\beta t+\beta_0
\tag{7}
\]
retains the same nonconstant complex-affine slope. The parameter
Jacobian is one, so the calibrated determinant remains
\(-a_0^4b\). Translation of the actual \(X\) by a complex constant
introduces no additional coefficient derivatives.

The whole-line return survives because
\(\sigma_*=\sigma-2\alpha t\) still generates \(L[v]\).
The strong return \(K=\mathbb C(y_*,z_*,w_*)\) is the actual
coordinate-frame return of271, which applies after (4).
It can also be seen directly: since \(E X_*=a_0\) and
\(E a_0=0\), localization gives
\(\mathcal B_{a_0}=A_{a_0}[X_*]\).
Quotienting by \(X_*\) identifies \(A_{a_0}\) with a localization
of the actual ring \(\mathbb C[Y_*,Z_*,W_*]\), with the three
images \(y_*,z_*,w_*\). The image of \(a_0\) is nonzero under
that identification. Taking fraction fields proves the return.

Relabel this rebuilt actual chart. From now on,
\[
y=d(t)\in F,\qquad d'\ne0,\qquad k''\ne0,\qquad
H=bn+c,\quad b=\beta t+\beta_0,\quad\beta\in\mathbb C^* .
\tag{8}
\]
Every hypothesis in (1) is retained, with these rebuilt coefficients.

## 3. The raw constant-first gradients

For independent formal \(U,P\), write the complete specialized
potentials from271:
\[
\begin{aligned}
\mathscr A&=(2P+k')U+k''P^2/2,
&\mathscr C&=U^2+k''PU+k'''P^3/6,\\
g&=T+(\beta n+c')P-b\mathscr A,\\
\mathscr W&=\omega-(\beta P+T_n)\mathscr A-b\mathscr C
 +(\beta n+c')U+c''P^2/2+T_tP,\\
Q_U&=(2P+k')\mathscr W_n-\mathscr W_P,
&Q_P&=(2U+k''P)\mathscr W_n-\mathscr W_t .
\end{aligned}
\tag{9}
\]
Here initially \(T,\omega\in L\), and
\(\theta=g(d,\sigma)\), \(w=\mathscr W(d,\sigma)\).
All formal derivatives are taken before substituting \(U=d\).
In particular \(d\) is not held constant under the exact
\(t\)-derivative when evaluated identities are later differentiated.

The full selected plane relation is \(G=U-d\). Its unit cofactor
and the actual scalar are
\[
Q_U(d,P)=\eta,\qquad Q_P(d,P)=0,\qquad \eta\in L^*,\qquad
J_\sigma=-\eta d'=-a_0^4b/\sigma_v\ne0.
\tag{10}
\]
These polynomial identities in \(P\) use that \(\sigma\) is affine
and nonconstant over \(L\). The scalar also independently proves
\(d'\ne0\), without relying on its expression in (6).

The raw cubic coefficient is
\[
[P^3]Q_U(d,P)=-k''T_{nn}.
\]
Since \(k''\ne0\), exact integration in the field with constants
\(\ker_L\partial_n=F\) gives
\[
T_{nn}=0,\qquad T=pn+q,\qquad p,q\in F.
\tag{11}
\]
The linear coefficient of \(Q_U(d,P)\), with (11), is
\[
6\beta d+p k''+p'k'-c''+2\omega_n.
\]
It vanishes, so \(\omega_n\in F\). Integrating again gives
\[
\omega=v_1n+v_0,\qquad v_1,v_0\in F.
\tag{12}
\]
No assertion \(L=F(n)\) was used in either integration.

Here is the complete positive-gradient ledger needed below,
including the constant \(Q_P\) coefficient. The displayed scalings
by two or six are harmless nonzero complex scalars. The last two
lines use the first two lines to remove their indicated terms:
\[
\begin{aligned}
0&=4p'+b k'''+3\beta k'',\\
0&=6\beta d+p k''+p'k'-c''+2v_1,\\
0&=b k''''+4\beta k''',\\
0&=p k'''+3k''p'-c''',\\
0&=-p''n+k''v_1-q'',\\
0&=-v_1'n-v_0'-3\beta d^2 .
\end{aligned}
\tag{13}
\]
The first two are \(2[P^2]Q_U=0\) and \([P]Q_U=0\).
The next two are \(6[P^3]Q_P=0\) and \(2[P^2]Q_P=0\).
Before using the first line, \([P]Q_P\) is
\(d(bk'''+3\beta k''+4p')-p''n+k''v_1-q''\).
Before using the second line, the constant \(Q_P\) coefficient is
\[
-v_1'n-v_0'+2dv_1+dp'k'+dp k''+3\beta d^2-c''d.
\]
Thus every term removed in (13) is accounted for by a previous
raw equation, not by an unproved moving-evaluation identity.

For reference, the remaining constant gradient is exactly
\[
\eta=k'v_1+(b k''+2p+2\beta k')d-p'n-q'.
\tag{14}
\]
No claim that this field element is an original-ring unit is made.

## 4. Compatibility forces a nonzero complex cubic coefficient

The parameter \(n\) is transcendental over \(F\). The last two
lines of (13), whose coefficients lie in \(F\), therefore give
\[
p''=0,\qquad q''=k''v_1,\qquad
v_1'=0,\qquad v_0'=-3\beta d^2.
\tag{15}
\]
In particular \(p'\) and \(v_1\) are complex, using the exact
derivative constants of \(F\).

Differentiate the second line of (13) in \(t\). The fourth line
and \(p''=v_1'=0\) then give
\[
0=6\beta d'+2p'k''+p k'''-c'''
 =6\beta d'-p'k''.
\tag{16}
\]
Consequently
\[
d'=\frac{p'k''}{6\beta},\qquad p'\in\mathbb C^*.
\tag{17}
\]
The last nonzero assertion follows from \(\beta\ne0\) and the
actual nonzero scalar \(d'\ne0\). It is not a discarded
zero-mode assumption.

The complete evaluated third intercept is
\[
\begin{aligned}
w={}&v_1n+v_0-(\beta\sigma+p)
       \bigl((2\sigma+k')d+k''\sigma^2/2\bigr)\\
 &-b\bigl(d^2+k''\sigma d+k'''\sigma^3/6\bigr)
       +(\beta n+c')d+c''\sigma^2/2+(p'n+q')\sigma.
\end{aligned}
\tag{18}
\]
Eliminate \(n\) using the literal first potential:
\[
n=z-2td-\sigma^2-k'\sigma .
\tag{19}
\]
Every coefficient of (18) belongs to \(F\); hence (19) makes
\(w\) a polynomial in \(\sigma\) over \(F[z]\).
Its cubic coefficient is
\[
\begin{aligned}
[\sigma^3]w
 &=-p'-\frac{\beta k''}{2}-\frac{b k'''}6\\
 &=-p'+\frac{4p'}6
 =-\frac{p'}3\ne0,
\end{aligned}
\tag{20}
\]
where the first line of (13) is the only simplification used.
There are no higher powers of \(\sigma\) in (18),(19).
Thus this polynomial has exact degree three, not merely an upper
bound obtained from leading terms of a different parameterization.

## 5. Exact field return contradicts degree three

Equations (11),(12),(18) and the first potential give
\(d,z,w\in F[n,\sigma]\).
Since \(F,n\subset L\subset K\) and \(\sigma\in K\), the actual
strong return yields both inclusions
\[
K=\mathbb C(d,z,w)\ \subset\ F(n,\sigma)\ \subset\ K.
\]
Therefore
\[
K=F(n,\sigma)=F(z,\sigma).
\tag{21}
\]
The last equality is the polynomial substitution (19), with inverse
\(z=n+2td+\sigma^2+k'\sigma\).
The pair \(n,\sigma\) is algebraically independent over \(F\):
\(n\) is transcendental over \(F\), \(L/F(n)\) is algebraic, and
\(\sigma\) is transcendental over \(L\).
It follows that \(z,\sigma\) is algebraically independent over \(F\)
as well. Taking \(N\)-constants also recovers \(L=F(n)\), although
that further equality is not needed for the contradiction.

Set \(F_0=F(z)\). By (20), \(w=g(\sigma)\) for a polynomial
\(g(T)\in F_0[T]\) of exact degree three. Since \(\sigma\) is
transcendental over \(F_0\),
\[
[F_0(\sigma):F_0(w)]=3.
\tag{22}
\]
For completeness, this degree fact needs no geometric theorem.
The polynomial \(g(T)-V\) is irreducible in \(F_0[T,V]\), since
it is primitive linear in \(V\) with a unit coefficient.
Viewed as a polynomial in \(T\) over \(F_0[V]\), it is primitive:
its leading coefficient is a nonzero element of the field \(F_0\).
Gauss's lemma makes it irreducible of degree three over \(F_0(V)\).
The transcendental substitution \(V\mapsto w\) gives (22).

But \(d\in F\), so the same actual strong return also gives
\[
K=\mathbb C(d,z,w)\ \subset\ F(z,w)\ \subset\ K.
\tag{23}
\]
This forces \(K=F(z,w)\), contradicting (21),(22).
In particular no assumption \(F=\mathbb C(d)\), no coordinate
claim about \(n,\sigma\), and no generic-pencil theorem is hidden
in this last step.

## 6. Exact conclusion and verification boundary

Under the nonzero-\(\ell\) entry of288,
\[
\boxed{b'\ne0,\quad r=a'/(4a+k'')=0
       \quad\Longrightarrow\quad\text{no such actual frame exists}.}
\tag{24}
\]
The constant-first auxiliary statement proved in Sections3--5 is
itself conditional on the literal actual271 chart with
\(b=\beta t+\beta_0\), \(\beta\ne0\), \(k''\ne0\), and \(y\in F\).
The original-ring translation in Section2 proves exactly that entry
for the stated remaining288 mode.

This note does not treat the separate \(r\ne0\) mode, the
constant-\(b\) lines, or the three-projection branch \(k_s\ne0\).
It does not establish arbitrary-coordinate entry or unrestricted
cancellation. No unpublished endpoint from another new note is
used here.

The complete retained271,277 and288 sources were read before this
derivation;272's actual normalization was also read for comparison
but is not the translation used here. Fresh unsaved algebra rebuilt
the signs in (5),(6), every raw coefficient used in (13),(14), the
compatibility (16), and the exact cubic coefficient (20).
Those finite identities do not certify the field-theoretic proof.
No saved checker was executed, imported, compiled or rerun.
No earlier note, index or packet was edited.
No novelty, human-expert or proof-assistant certification is claimed.

