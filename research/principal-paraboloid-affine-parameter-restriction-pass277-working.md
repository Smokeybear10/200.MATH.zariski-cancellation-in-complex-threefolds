# The old parameter is affine in the new parameter

In the actual nonconstant-intercept branch271, the full calibrated
Jacobian forces \(H_{nn}=0\), strengthening275's third-derivative
restriction. Thus the old parameter has the exact form
\(H=h_1(t)n+h_0(t)\), with coefficients in the retained finite
curve field and \(h_1\ne0\). This is a coefficient restriction,
not recognition of the whole branch.

## 1. Retained actual hypotheses and the degree input

Retain every actual hypothesis and exact field construction of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md):
the sliced complex polynomial four-ring, exact time degrees1222,
full initial kernel \((X^2Z-Y^2)\), selected literal Z-partial of
shift four, and \(k_s=0,n_s\ne0\). Its exact reparameterization gives
\[
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad H_n\ne0,\quad k\in F,
\quad L[y,\sigma]=L[v].
\tag{1}
\]
The commuting coefficient partials fix \(v\). The prime derivative
on \(F\) has constants exactly \(\mathbb C\); \(n\) is
transcendental over \(F\). All formal coefficient derivatives below
hold \(U,P\) fixed before any moving-line substitution.

Use the formal polynomials from271:
\[
\begin{aligned}
\gamma&=2P+k',& B_1&=2U+k''P,\\
\mathscr A&=(2P+k')U+k''P^2/2,
&\mathscr C&=U^2+k''PU+k'''P^3/6,\\
\mathscr W&=\omega+H_{nn}\mathscr A^2/2
 -(H_{nt}P+T_n)\mathscr A-H_n\mathscr C
 +H_tU+H_{tt}P^2/2+T_tP,\\
Q_U&=\gamma\mathscr W_n-\mathscr W_P,
&Q_P&=B_1\mathscr W_n-\mathscr W_t.
\end{aligned}
\tag{2}
\]
Here \(T,\omega\in L\). The polynomial \(Q\) is the normalized
primitive proved in271, not an independently chosen relation.
For the irreducible selected plane relation \(G\), that note gives
\[
Q-q_0=\eta G+G^2R,\quad \eta\in L^*,\qquad
G_g=c_0\Lambda^g,\quad
g=\max(\deg_vy,\deg_v\sigma),
\tag{3}
\]
where \(\Lambda\) is a nonzero linear form and \(c_0\in L^*\).
If \(\deg Q>g\), (3) implies that \(\Lambda^{2g}\) divides the
top homogeneous part of \(Q\). Multiplicities may be checked after
algebraic closure; no change of the actual coefficient field is made.

The completely read
[canonical-line theorem275](principal-paraboloid-canonical-line-recognition-pass275-working.md),
composed with the completely read actual normalization272, proves
\(H_{nnn}=0\) throughout this branch. Exact integration in (1) gives
\[
H=\frac{a}{2}n^2+b n+c,\qquad a,b,c\in F.
\tag{4}
\]
The symbol \(a\) here is \(H_{nn}\), not the slice speed \(EX\).
We write the latter as \(\rho\) below. Our task is to prove \(a=0\).
Two retained boundary statements will be used explicitly:

* By272 Section2, \(\sigma\in L\) forces \(H_{nn}=0\).
* By275, the actual canonical line \(k=0,y\in L\) forces
  \(H_{nn}=0\), independently of its recognition conclusion.

## 2. The fifth-degree term makes a a complex constant

Substitute (4) in (2) and integrate the homogeneous gradients.
The top degree-six part vanishes and the degree-five part is
\[
\boxed{
Q_5=-\frac{P^3(k''P+4U)}{24}
       \bigl(2a k'''P+3a'(k''P+4U)\bigr).
}
\tag{5}
\]
This formula can be verified by differentiating it in \(U,P\)
and matching the complete degree-four parts of (2).

Suppose \(a'\ne0\). Then \(a\ne0\) and (5) is nonzero. If
\(a k'''\ne0\), its three linear factors are distinct, with
multiplicities \(3,1,1\). The pure-top condition in (3) gives
\(g\le3<5\), and the doubled multiplicity condition gives
\(g=1\) and \(\Lambda=P\). Thus \(\sigma\in L\), contradicting
the first boundary statement after (4).

The remaining possibility is \(k'''=0\). Formula (5) then has
factor multiplicities \(3,2\), so again \(g=1\). Its direction is
either \(P\) or \(4U+k''P\). The first has just been excluded.
In the second case the exact integration of \(k'''=0\) gives a
complex quadratic \(k\). The actual affine transformation in272
Sections3--4 makes \(k_*=0,y_*\in L\). The new parameter differs
from \(n\) by a complex polynomial in \(t\), so \(H_{n_*n_*}=a\).
The canonical-line restriction275 contradicts \(a\ne0\).
Consequently
\[
\boxed{a'=0,\qquad a\in\mathbb C.}
\tag{6}
\]
This argument does not assert that arbitrary projected plane changes
are ambient coordinate changes; it uses only the specific actual
map already proved in272.

## 3. A nonzero a would force k to be a complex quadratic

Assume for contradiction that \(a\in\mathbb C^*\). If \(k'''\ne0\),
(5) becomes
\[
Q_5=-a k'''P^4(k''P+4U)/12.
\tag{7}
\]
The pure-top bound first gives \(g\le4<5\); the doubled
multiplicities in (3) then give \(g\le2\), with pure top \(P^g\).
For \(g=1\), \(\sigma\in L\), already impossible.

For \(g=2\), irreducibility and the pure top \(P^2\) give the exact
form, after multiplication by a unit,
\[
G=U-rP^2-sP-C,\qquad r\in L^*,\quad s,C\in L.
\tag{8}
\]
Indeed its U-coefficient must be nonzero: otherwise \(G\) would
be a polynomial in \(P\) only, whose root \(\sigma\in L[v]\)
would be constant and would provide a linear factor over \(L\).
Equation (3) makes
\(Q_U(rP^2+sP+C,P)=\eta\). But the raw formula (2), with (4)
and constant \(a\), gives
\[
[P^5]Q_U(rP^2+sP+C,P)=-6ar^2\ne0.
\tag{9}
\]
The identity is independent of derivatives of \(r,s,C\), since
formal derivatives precede substitution. This is a contradiction.
Hence \(k'''=0\), so
\[
k=\kappa t^2/2+\alpha t+\beta,
\qquad \kappa,\alpha,\beta\in\mathbb C.
\tag{10}
\]

We may now set \(k=0\) by the actual affine map from272, even
without its old projected-line hypothesis. To make this usage explicit,
put \(d=\kappa/4\) and use
\[
X_*=X-d,\quad Y_*=Y+\alpha X_*/2,\quad
Z_*=Z-\beta X_*,\quad W_*=W.
\tag{11}
\]
The inverse is \(X=X_*+d,Y=Y_*-\alpha X_*/2,
Z=Z_*+\beta X_*,W=W_*\). Literal substitution, for arbitrary
old \(y,\sigma\), gives
\[
\begin{aligned}
y_*&=y+d\sigma+td^2,& \sigma_*&=\sigma+2dt+\alpha/2,\\
k_*&=0,&n_*&=n-3d^2t^2-\alpha dt+\beta d-\alpha^2/4.
\end{aligned}
\tag{12}
\]
All leaders, the full initial kernel, the literal selected partial,
the exact field \(L\), and actual chart returns are retained as in272.
In particular \(\partial_{n_*}=\partial_n\) and \(H_{n_*n_*}=a\).
After renaming the new chart, (4) still holds with the same complex
nonzero \(a\) and possibly different \(b,c\in F\), but now \(k=0\).

## 4. The fourth-degree term forces a projected line

With \(k=0\), the full potential is particularly short:
\[
\mathscr W=
\omega+2aU^2P^2-2UP(b'P+T_n)
 -(an+b)U^2+(b'n+c')U
 +(b''n+c'')P^2/2+T_tP.
\tag{13}
\]
The fifth-degree part is zero and the nonzero fourth-degree part is
\[
\boxed{Q_4=UP\bigl(b''P^2-2T_{nn}UP-2aU^2\bigr).}
\tag{14}
\]
No linear factor in (14) has multiplicity greater than three: the
two displayed factors \(U,P\) are distinct, and the remaining
quadratic is not divisible by \(P\), since \(a\ne0\).
The pure-top and doubled-multiplicity arguments in (3) therefore
give \(g\le3<4\) and then \(g=1\).

If \(\sigma\in L\), we already have a contradiction. Otherwise
\(L[\sigma]=L[v]\), and the line is
\[
G=U-sP-C,\quad y=s\sigma+C,\qquad s,C\in L,
\quad Q_U(sP+C,P)=\eta,\quad Q_P(sP+C,P)=-s\eta.
\tag{15}
\]
If \(s=0\), this is275's actual canonical line, contradicting
\(a\ne0\). Hence assume \(s\ne0\).

The cubic P-coefficients of the last two identities in (15), from
(13), are respectively
\[
b''-4T_{nn}s-6as^2=0,\qquad
-2as^3-4T_{nn}s^2+3b''s=0.
\tag{16}
\]
They give
\[
T_{nn}=-2as,\qquad b''=-2as^2.
\tag{17}
\]
Differentiating the second equality in \(n\), and using \(as\ne0\),
shows \(s_n=0\), so \(s\in F\). Exact integration of the first
equality in the field with constants (1) gives
\[
T=-as n^2+p n+q,\qquad p,q\in F.
\tag{18}
\]

## 5. Lower coefficients contradict the nonzero actual determinant

The quadratic P-coefficients in (15) now give
\[
\begin{aligned}
0&=-2(2an s'+2aCs-3sb'-p'),\\
0&=-\tfrac12(12an ss'-8aCs^2-6s^2b'-8sp'+c''').
\end{aligned}
\tag{19}
\]
The first implies
\[
C=-n s'/s+3b'/(2a)+p'/(2as).
\tag{20}
\]
Substitute in the second. Up to its nonzero scalar factor, the result is
\[
20an ss'-18s^2b'-12sp'+c'''=0.
\tag{21}
\]
All coefficients lie in \(F\), and \(n\) is transcendental over
\(F\). Its n-coefficient, with \(as\ne0\), forces \(s'=0\).
Thus \(s\in\mathbb C^*\) and \(C\in F\). In particular (20) gives
\[
p'=2asC-3sb'.
\tag{22}
\]

The linear P-coefficient of \(Q_U(sP+C,P)\) gives
\[
\omega_n=an s^2+3aC^2-3Cb'-ps+c''/2.
\tag{23}
\]
Using this, the linear P-coefficient of \(Q_P(sP+C,P)\) is
\[
n(4as^3-p'')+8aC^2s+4Cp'-2ps^2-q''=0.
\tag{24}
\]
Again all coefficients other than \(n\) lie in \(F\), so
\(p''=4as^3\). Differentiate (22) and use (17):
\[
4as^3=2asC'-3sb''=2asC'+6as^3,
\qquad C'=-s^2.
\tag{25}
\]

It remains essential to use the actual scalar determinant, rather
than treating the formal gradients alone as a contradiction. From271,
with \(k=0\),
\[
\begin{aligned}
-\rho^4H_n&=Q_U(y,\sigma)D_U+Q_P(y,\sigma)D_P\in L^*,\\
D_U&=(2y y_n-y_t)\sigma_v+(\sigma_t-2y\sigma_n)y_v,\\
D_P&=(1+2\sigma\sigma_n)y_v-2\sigma y_n\sigma_v.
\end{aligned}
\tag{26}
\]
Since \(y=s\sigma+C(t)\), with complex constant \(s\), these
expressions reduce exactly to
\[
D_U=-C'\sigma_v,\qquad D_P=s\sigma_v.
\tag{27}
\]
Equations (15),(25)--(27) now give
\[
0\ne-\rho^4H_n=-\eta(C'+s^2)\sigma_v=0,
\tag{28}
\]
the required contradiction. Therefore \(a\ne0\) was impossible.

## 6. Exact conclusion and remaining scope

Throughout the actual branch271 we have proved
\[
\boxed{H_{nn}=0,\qquad H=h_1n+h_0,
\qquad h_1,h_0\in F,\quad h_1\ne0.}
\tag{29}
\]
The integration is exact because \(F=\ker_L\partial_n\), and
\(h_1\ne0\) follows from the original reparameterization condition
\(H_n\ne0\). No inference \(L=F(n)\) is made: a finite extension
of that field has not been removed by the displayed affine identity.
Nor are \(h_1,h_0\) shown to be complex, or \(k\) shown to be
quadratic when \(a=0\). The polynomial potentials, their actual
field return, and remaining scalar identity must still be used to
settle that remaining family.

This note is not full recognition of271, the supplied exact1222
profile, or unrestricted cancellation. It composes precisely stated
working lemmas, not a formal verification of their historical chain.
No novelty or human expert certification is asserted.

Root completely read271,272 and275 before writing this source.
Fresh unsaved symbolic expansions reconstructed the homogeneous
parts (5),(14), both full gradients, the parabola coefficient (9),
and the complete line coefficient lists behind (16),(19),(23),(24).
The field integrations and actual-coordinate distinctions are proved
above, not inferred from those finite computations.
