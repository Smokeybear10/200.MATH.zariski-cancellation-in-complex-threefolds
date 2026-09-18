# Polynomial coefficient reduction for the remaining paraboloid lines

This note treats selected projected lines in the actual branch271 after
the affine-parameter theorem277. It does not assume the nonlinear
component restrictions of280. The complete gradient and scalar equations
force a complex affine parameter slope and remove the finite extension
of the coefficient field. Two subbranches admit actual degree-lowering
maps. Two explicitly stated coefficient modes remain unresolved here.

## 1. Actual entry and exact fields

Retain all actual hypotheses of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and the proved conclusion of
[277](principal-paraboloid-affine-parameter-restriction-pass277-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
\text{full initial kernel }(X^2Z-Y^2),\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad \ker(\partial_t|_F)=\mathbb C,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\quad
L[y,\sigma]=L[v],\quad Nv=1,\\
H=b(t)n+c(t),\qquad b\in F^*,\quad c,k\in F.
\end{gathered}
\tag{1}
\]
The full initial relation is not an equation between the actual
coordinates. The exact coefficient partials commute and initially fix
\(v\). Primes on elements of \(F\) denote their t-derivatives.
The parameter \(n\) is transcendental over \(F\).

Assume the selected full plane relation is a line and that
\(\sigma\notin L\). The constant-second branch is treated separately
in278. Since the plane pair generates the whole polynomial line, there
are \(a,d\in L\) with
\[
G=U-aP-d,\quad y=a\sigma+d,\quad L[\sigma]=L[v],
\quad \sigma_v\in L^*.
\tag{2}
\]
The letters \(a,d\) in (2) are the projected slope and intercept.
They do not denote the nonzero slice speed \(a_0=EX\).

The actual expansions and calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,
&z&=2ty+\sigma^2+k'\sigma+n,\\
W&=w+\theta X+HX^2,
&\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}&=-a_0^4b\in L^*.
\end{aligned}
\tag{3}
\]
Every later field equality uses the actual return in (1), not merely
whole-line generation over \(L\).

## 2. Raw potentials, selected cofactor and moving-line scalar

For independent formal \(U,P\), put
\[
\begin{aligned}
\gamma&=2P+k',& B_1&=2U+k''P,\\
\mathscr A&=(2P+k')U+k''P^2/2,
&\mathscr C&=U^2+k''PU+k'''P^3/6,\\
g&=T+(b'n+c')P-b\mathscr A,\\
\mathscr W&=\omega-(b'P+T_n)\mathscr A-b\mathscr C
 +(b'n+c')U+(b''n+c'')P^2/2+T_tP,\\
Q_U&=\gamma\mathscr W_n-\mathscr W_P,
&Q_P&=B_1\mathscr W_n-\mathscr W_t,
\end{aligned}
\tag{4}
\]
where initially \(T,\omega\in L\),
\(\theta=g(y,\sigma)\), and \(w=\mathscr W(y,\sigma)\).
All derivatives in (4) are formal coefficient derivatives before
substitution of (2).

The unit selected-cofactor statement of271 gives
\[
Q-q_0=\eta G+G^2R,\quad \eta\in L^*,\qquad
Q_U(aP+d,P)=\eta,\quad Q_P(aP+d,P)=-a\eta.
\tag{5}
\]
Neither irreducibility of \(Q-q_0\) nor constancy of \(a,d\) is
assumed.

Change only the generic-line parameter from \(v\) to \(\sigma\).
Its derivative is \(\sigma_v\in L^*\), so the new determinant is
\(-a_0^4b/\sigma_v\in L^*\), independent of the new line parameter.
The old and new coefficient partials differ by the appropriate moving
parameter terms. Equivalently, use271's wedge identity before changing
parameter. With (5), it gives exactly
\[
\begin{aligned}
J_\sigma/\eta
&=-y_t+(2y+k''\sigma)y_n
       -a\bigl(y_\sigma-(2\sigma+k')y_n\bigr)\\
&=(4a+k'')a_n\sigma^2
 +\bigl((4a+k'')d_n+(2d+ak')a_n-a_t\bigr)\sigma\\
&\hspace{12mm}+(2d+ak')d_n-d_t-a^2\in L^*.
\end{aligned}
\tag{6}
\]
On the first line the derivatives hold the new formal \(\sigma\)
fixed. Thus \(y_t=a_t\sigma+d_t\) and \(y_n=a_n\sigma+d_n\).
There is no assertion that moving-parameter partials equal the original
ones on all of \(K\).

Write \(\ell=4a+k''\). Equation (6) implies
\[
\ell a_n=0,\quad
\ell d_n+(2d+ak')a_n-a_t=0,\quad
(2d+ak')d_n-d_t-a^2\ne0.
\tag{7}
\]

## 3. The zero-ell branch is an actual recognized branch

If \(\ell=0\), then \(a=-k''/4\in F\), hence \(a_n=0\).
The second equation of (7) gives \(a'=0\), so \(k'''=0\).
Exact integration in \(F\) gives
\[
k=\kappa t^2/2+\alpha t+\beta,\quad
\kappa,\alpha,\beta\in\mathbb C,\quad a=-\kappa/4.
\tag{8}
\]
Set \(d_*=\kappa/4\). Use the specific actual transformation proved
in [272](principal-paraboloid-high-derivative-line-normalization-pass272-working.md):
\[
X_*=X-d_*,\quad Y_*=Y+\alpha X_*/2,\quad
Z_*=Z-\beta X_*,\quad W_*=W.
\tag{9}
\]
Its inverse is obtained by adding \(d_*\) to \(X_*\), subtracting
\(\alpha X_*/2\) from \(Y_*\), and adding \(\beta X_*\) to
\(Z_*\). Literal substitution gives
\[
\begin{aligned}
y_*&=y+d_*\sigma+td_*^2=d+td_*^2\in L,\\
\sigma_*&=\sigma+2d_*t+\alpha/2,\quad k_*=0,\\
n_*&=n-3d_*^2t^2-\alpha d_*t+\beta d_*-\alpha^2/4.
\end{aligned}
\tag{10}
\]
The exact degrees, entire initial kernel, selected literal partial,
coefficient field and whole-line return are transported as in272.
Thus the actual canonical-line theorem
[275](principal-paraboloid-canonical-line-recognition-pass275-working.md)
applies. Subject to that retained working theorem,
\(A\cong\mathbb C^{[3]}\).

No coefficient-field affine transformation has been promoted to an
ambient one. The map (9) has only complex coefficients.

## 4. Nonzero ell: the two scalar coefficients kill b-double-prime

Assume henceforth \(\ell\ne0\). Equations (7) give
\[
a\in F,\quad r=\frac{a'}{\ell}\in F,\quad
d=rn+d_0,\quad d_0\in F.
\tag{11}
\]
The integration uses precisely \(F=\ker_L\partial_n\).
The nonzero scalar in (7) is now
\[
\delta=(2r^2-r')n+2rd_0+ak'r-d_0'-a^2\ne0.
\tag{12}
\]

For transparency, the following is the necessary raw lower-gradient
ledger. Put \(k_j=k^{(j)}\), temporarily \(u=T_{nn}\), and let
\(F_j=[P^j]Q_U(aP+d,P)\), \(J_j=[P^j]Q_P(aP+d,P)\).
Every positive-index coefficient is zero by (5). Expansion of (4) gives
\[
\begin{aligned}
F_3={}&b''-\ell u,\\
6J_3={}&-24a^2u-18au k_2-3u k_2^2
 +18ab''+bk_4+4b'k_3+6b''k_2,\\
2F_2={}&-8au k_1+12ab'-8du-u k_1k_2
 +4T_{tn}+bk_3+3b'k_2+b''k_1,\\
F_1={}&2aT_n-au k_1^2+abk_2+2ab'k_1-4du k_1+6db'\\
 &+T_nk_2+T_{tn}k_1-b''n-c''+2\omega_n,\\
J_1={}&-4adu k_1+6adb'+aT_nk_2+aT_{tn}k_1
 -ab''n-ac''+2a\omega_n\\
 &-4d^2u-du k_1k_2+4dT_{tn}+dbk_3+3db'k_2
 +db''k_1-T_{tt}+k_2\omega_n.
\end{aligned}
\tag{13}
\]
These are coefficients after formal differentiation, not derivatives
of moving evaluated coefficients.

The first two equations give
\[
u=\frac{b''}{\ell}\in F,\quad
T=\frac u2 n^2+pn+q,\quad p,q\in F,\qquad
bk''''+4b'k'''+3u\ell^2=0.
\tag{14}
\]
The n-coefficient and constant coefficient of \(F_2=0\), respectively,
are
\[
u'=2ru,\qquad
p'=u(ak'+2d_0)-\frac{bk'''+3\ell b'}4.
\tag{15}
\]

Solve \(F_1=0\) for \(\omega_n\) and substitute into \(J_1\).
Use (11),(14),(15), including their t-derivatives. The two highest
n-coefficients of this last polynomial are exactly
\[
\begin{aligned}
[n^2]J_1&=u(2r^2-r'),\\
[n]J_1&=2u(2rd_0+ak'r-d_0'-a^2).
\end{aligned}
\tag{16}
\]
One can reconstruct the first line before the last substitution as
\(4r^2u-r u'-u r'\). For the second, substitute the derivative of
the second equation of (15) and
\(bk''''=-4b'k'''-3u\ell^2\); the displayed expression results.
Thus (16) does not discard derivatives of \(u\) or \(p\).

If \(u\ne0\), both coefficients of \(\delta\) in (12) vanish,
contradicting its nonzero calibration. Therefore
\[
\boxed{b''=0,\quad T_{nn}=0,\quad
b=\beta_1t+\beta_0\ne0,\quad \beta_i\in\mathbb C,\quad T=pn+q.}
\tag{17}
\]
This argument is valid also when \(a=0\), \(r=0\), or \(b'=0\).
Only \(\ell\) was divided out in this branch. The nonzero scalar
was essential; the formal gradient equations alone were not used as
an obstruction.

## 5. Polynomial potentials remove the finite coefficient extension

Put \(\beta=b'\in\mathbb C\). The remaining top identity and
(15) are
\[
bk''''+4\beta k'''=0,\qquad
p'=-\frac{bk'''+3\ell\beta}{4}.
\tag{18}
\]
With (17), the equation \(F_1=0\) in (13) gives
\[
\begin{aligned}
\omega_n&=-3\beta r n+v_1,\\
v_1&=-3\beta d_0-\beta ak'-\frac{k'p'}2
 -\frac{abk''}2-ap-\frac{pk''}2+\frac{c''}2\in F,\\
\omega&=-\frac{3\beta r}{2}n^2+v_1n+v_0,\qquad v_0\in F.
\end{aligned}
\tag{19}
\]
Exact integration is again inside \(L\), using its specified kernel
\(F\); no rationality of \(L\) is assumed to obtain (19).

Equations (4),(11),(17),(19) now prove
\[
y,z,w,\theta\in F[n,\sigma],\quad
\deg_n\omega\le2,\qquad
K=F(n,\sigma),\qquad \boxed{L=F(n).}
\tag{20}
\]
Here are both field inclusions and the final intersection argument.
The literal potentials place \(\mathbb C(y,z,w)\) in
\(F(n,\sigma)\). Conversely \(F,n\subset L\subset K\) and
\(\sigma\in K\), so \(F(n,\sigma)\subset K\). Use the strong
return in (1) for equality. On \(L(\sigma)\), the derivation \(N\)
is \(\sigma_v\partial_\sigma\), with \(\sigma_v\in L^*\).
Thus an element of \(F(n,\sigma)\) is N-fixed exactly when it is
in \(F(n)\), whether or not \(\sigma_v\) was known to lie there.
Taking N-constants in the equality of fields gives (20).

This is a field and coefficient-polynomiality statement. Neither
\(n\) nor \(\sigma\) has been shown to be an ambient polynomial
coordinate, and (20) is not an equality of original polynomial rings.

There is also a useful complete form for the selected primitive.
Since (18) kills its quartic top, \(\deg Q\le3\). Its U-degree
is at most two, and direct differentiation of (4) gives
\[
[U^2]Q=3\beta P+B_0,\qquad B_0=\frac{bk''}{2}+p+\beta k'.
\]
In (5), degree at most three makes \(R\) affine, and the U-degree
bound makes it independent of U. Comparing the U-squared coefficient
therefore gives the exact identity
\[
\boxed{Q-q_0=\eta(U-aP-d)+(3\beta P+B_0)(U-aP-d)^2.}
\tag{21}
\]
This permits a reducible level polynomial. It does not replace the
full selected line relation by an unproved irreducibility assertion.

## 6. Exact coefficient modes, and a second actual recognized subbranch

If \(\beta=0\), then \(b=h\in\mathbb C^*\), and (18) gives
\(k''''=0\). Consequently
\[
k\in\mathbb C[t]_{\le3},\quad p'=-hk'''/4\in\mathbb C,\quad
p\in\mathbb C[t]_{\le1}.
\tag{22}
\]
The coefficient \([P^2]Q_P(aP+d,P)=0\), with (17) and
\(\beta=0\), gives
\[
c'''=pk'''+3k''p',\qquad c\in\mathbb C[t]_{\le4}.
\tag{23}
\]
For instance the same raw coefficient before substituting (18) is
\((8ap'+2abk'''+3k''p'+pk'''-c''')/2\);
its first two terms cancel. The polynomial conclusions in (22),(23)
follow by subtracting complex polynomial primitives in the exact field
\(F\), whose derivative constants are exactly complex.

Suppose additionally \(k'''=0\). Then \(k,c\) are complex
quadratics. Apply (9) to make \(k=0\), retaining every actual
hypothesis. The new parameter differs from the old one by a complex
quadratic in t, so \(H=hn+c\) still has complex quadratic c.
The new line either is canonical and is recognized by275, or has
nonzero \(\ell\) and the preceding argument applies again. In the
latter case its rebuilt coefficients satisfy
\[
k=0,\quad H=hn+c,\quad c=c_2t^2/2+c_1t+c_0,\quad
T=pn+q,\quad h\in\mathbb C^*,\quad p,c_i\in\mathbb C.
\tag{24}
\]
No assertion that q is complex is needed below.

Define a triangular correction in the actual polynomial ring:
\[
\boxed{W_*=W-h(X^2Z-Y^2)-c_2Z/2-c_1Y-c_0X^2.}
\tag{25}
\]
It fixes \(X,Y,Z\); adding the same displayed polynomial gives its
polynomial inverse. In the k=0 chart,
\(X^2Z-Y^2=-y^2-2y\sigma X+nX^2\).
Substitution of the complete potentials (4) yields
\[
W_*=\omega-c_2n/2+(q'-2py)\sigma+(pn+q)X.
\tag{26}
\]
The coefficients on the right belong to \(K\). If \(pn+q\ne0\),
this is an exact degree-one coordinate. The actual frame
\((X,W_*,Y,Z)\) has degrees1122, and the completely read retained
[recognition synthesis257](full-exact1122-recognition-synthesis-pass257-working.md)
applies, with no condition on its rebuilt entire initial kernel.
If \(pn+q=0\), then \(W_*\) is an invariant actual coordinate.
The slice makes \(A\) regular, and
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
applies to the nonzero LND on \(\mathbb C[W_*]^{[3]}\).
Both alternatives recognize \(A\cong\mathbb C^{[3]}\), subject
to the stated retained endpoint dependencies.

If instead \(\beta\ne0\), equation (18) says
\((b^4k''')'=0\). Thus there are complex constants and a complex
quadratic polynomial with
\[
\boxed{b=\beta t+\beta_0,\quad \beta\ne0,\qquad
k=k_2(t)+\kappa/b,\quad k_2\in\mathbb C[t]_{\le2},\quad
\kappa\in\mathbb C.}
\tag{27}
\]
Indeed \((\kappa/b)'''=-6\kappa\beta^3/b^4\), so choose
\(\kappa\) to match \(b^4k'''\) and integrate the remaining
zero third derivative. The case \(\kappa=0\) is retained.
Equation (27) is a coefficient-field form, not an actual reciprocal
change of coordinates.

## 7. Precise frontier and verification boundary

For the selected lines (2), this note proves recognition when
\(4a+k''=0\), or when \(b\in\mathbb C^*\) and \(k'''=0\).
Every other such line is reduced to all of (11),(12),(17)--(21),
with one of the following two coefficient modes:

* \(b\in\mathbb C^*\) and k is a complex cubic with nonzero
  third derivative; p is complex affine and c is complex polynomial
  of degree at most four.
* b is nonconstant complex affine and k has the exact form (27).

These alternatives are necessary forms, not asserted actual examples.
Their remaining gradient coefficients, original field return and
actual scalar are still required. In particular this note does not
recognize all projected lines or the entire branch271, and it does
not identify \(F\) with \(\mathbb C(t)\).

The new algebra was reconstructed from the literal potentials (4),
including the n-coefficients in (16) and the complete correction (26).
Unsaved symbolic calculations checked the displayed coefficient
identities; the scalar obstruction and exact-field intersections are
proved separately above. No saved checker was executed, imported or
compiled. Earlier sources, indices and packets are unchanged.
The retained sources271,272,275,277 and257 were completely read;
this is not a recursive revalidation of their older dependency chains.
There is no novelty, formal verification, human certification or
unrestricted cancellation claim.

