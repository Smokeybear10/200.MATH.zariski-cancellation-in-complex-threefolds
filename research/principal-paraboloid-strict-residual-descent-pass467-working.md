# Strict residual descent forces quadratic sigma

Working necessary result: retain the full actual264 hypotheses with
\(k=s+f\), \(f_s=0\), \(n_{ss}f'''\ne0\). In the strict branch
of460/461, suppose \(a=\deg_v\sigma>1\). Then
\[
\boxed{a=2,\qquad \deg_v y=\deg_v\theta=4.}
\tag{1}
\]
The proof starts from the exact half-degree remainder of465 and
descends once more using the entire polynomial \(zW\). It works
without an a priori upper degree bound. It does not exclude the
quadratic case itself or settle the balanced branch.

All changes of intrinsic generators below are over the exact
coefficient field. None is promoted to an original complex polynomial
coordinate change.

## 1. Entire actual input and the retained strict equations

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and the arbitrary-n formulas of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\quad\hbox{is the entire weighted initial kernel},\\
X=a_0u+x_0,\quad a_0\in L^*,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\quad
O=L[A]=L[v]=L[y,\sigma,\theta].
\end{gathered}
\tag{2}
\]
Both actual returns, the full calibrated scalar, localization and
selected-partial conditions remain retained. In particular the original
slice is not assumed to equal \(X/a_0\). The exact coefficient
partials commute and have joint constants \(\mathbb C\). Assume
\[
k=s+f,\quad f\in\ker_L\partial_s,\quad
e=n_{ss}\ne0,\quad f'''\ne0,\quad
a=\deg_v\sigma>1
\tag{3}
\]
and the strict alternative \(2\deg_v y>3a\).

The complete held source
[465](principal-paraboloid-strict-degree-parity-refinement-pass465-working.md)
is the necessary input, together with its
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md)
and
[461](principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md)
dependencies. It supplies intrinsic polynomials \(P,z,q,S\) and
coefficient units \(\eta,\lambda\in L^*\) with
\[
\begin{gathered}
P=\sigma,\qquad a=2c,\quad c\in\mathbb Z_{>0},\qquad
\deg_vP=\deg_vz=2c,\quad \deg_vS=c,\\
z=\lambda P+S,\qquad \deg_vq=4c,\qquad
O=L[P,z,q],\qquad
\deg_v y=\deg_v\theta=2a,\\
\mathcal H=z^2+2\eta zq+T(P)=0,\\
T(P)=2\eta\lambda P^3+t_2P^2+t_1P+t_0,\qquad
B(P)=-2\eta\lambda^2P+B_0,\qquad
D(P)=d_0+4\eta^2P .
\end{gathered}
\tag{4}
\]
Here \(z=x-\eta q\) is the shear variable of461, not the original
\(Z\)-intercept. The coefficient elements \(B_0,d_0,t_i\) are the
genuine ones from that construction; they may be zero.

The full genuine minor after the forced vanishings in465 is
\[
W=2B(P)z+2\eta B(P)q-2\eta zT'(P)+2D(P)z^2,
\qquad
W=-\psi P',\quad \psi\in L^*,\qquad
\deg_vW=2c-1 .
\tag{5}
\]
The derivative of \(T\) is formal in \(P\); the derivative \(P'\)
in the tangent identity is intrinsic in \(v\), fixing \(L\).
The exact degree in (5) uses whole generation and the evaluated
gradient-minor unit, not merely a nonzero minor.

## 2. The complete polynomial to which descent applies

Multiply (5) by \(z\) and use the third equation in (4). The full
identity is
\[
K:=zW=B(P)z^2-B(P)T(P)-2\eta z^2T'(P)+2D(P)z^3,
\qquad \deg_vK=4c-1 .
\tag{6}
\]
Before imposing \(\mathcal H=0\), the difference between \(zW\)
and the displayed polynomial is exactly \(B(P)\mathcal H\).
Thus no lower level or remainder has been deleted.

The following coefficient notation records every term of465(29),(30):
\[
\begin{aligned}
M&=12\eta^2\lambda\ne0,\qquad D_1=8\eta^2\ne0,\\
k_3&=-2\lambda\{\eta B_0-d_0\lambda^2+
                            \eta\lambda^3+\eta\lambda t_2\},\\
\alpha_2&=B_0(\lambda^2-t_2),\\
\beta_2&=6d_0\lambda^2-4\eta\lambda^3-8\eta\lambda t_2,\\
\alpha_1&=2\eta\lambda^2t_0-B_0t_1,\qquad
\beta_1=2B_0\lambda-4\eta\lambda t_1,\\
\gamma_1&=6d_0\lambda-2\eta\lambda^2-4\eta t_2,\\
\gamma_0&=B_0-2\eta t_1,\qquad \alpha_0=-B_0t_0.
\end{aligned}
\tag{7}
\]
In particular \(M\) here denotes a coefficient unit, not a field
extension. The exact polynomial is
\[
\boxed{
\begin{aligned}
K(P,S)={}&k_3P^3+(MS^2+\beta_2S+\alpha_2)P^2\\
 &+(D_1S^3+\gamma_1S^2+\beta_1S+\alpha_1)P\\
 &+2d_0S^3+\gamma_0S^2+\alpha_0 .
\end{aligned}}
\tag{8}
\]
Equations (6)--(8) are evaluated identities in \(O\). We do not
assume that \(P,S\) are algebraically independent.

## 3. The first residual has degree at most c

The two possible degree-\(6c\) terms of (8) are \(k_3P^3\) and
\(MP^2S^2\). Every other term has degree at most \(5c\), whereas
(6) has exact degree \(4c-1\). Since the second term has nonzero
leading coefficient, \(k_3\) cannot vanish. Define
\[
\delta=\frac{k_3}{M}\in L^*,\qquad U=S^2+\delta P.
\tag{9}
\]
The cancellation of the degree-\(6c\) coefficients proves
\(\deg_vU<2c\), allowing \(U=0\).
For later reconstruction, the definition of \(\delta\) and (7)
is exactly equivalent to
\[
\boxed{B_0=\frac{d_0\lambda^2}{\eta}
              -\lambda^3-\lambda t_2-6\eta\delta .}
\tag{10}
\]
This relation is retained in every subsequent substitution.

Grouping the two leading terms of (8) gives the entire identity
\[
\begin{aligned}
K={}&MP^2U+\beta_2P^2S+D_1PS^3+\alpha_2P^2\\
 &+(\gamma_1S^2+\beta_1S+\alpha_1)P
      +2d_0S^3+\gamma_0S^2+\alpha_0 .
\end{aligned}
\tag{11}
\]
If \(U\) were nonconstant of degree greater than \(c\), the first
term would have degree \(4c+\deg_vU>5c\). Every other term in
(11) has degree at most \(5c\), so that leading term could not
cancel. This contradicts (6). Consequently
\[
\deg_vU\le c\quad\hbox{or }U=0.
\tag{12}
\]
This includes both the zero and constant cases; neither is
discarded by a leading-coefficient division.

## 4. Exact second subtraction and the degree-four remainder

The following complete decomposition isolates all higher terms.
Let
\[
\mu=\frac{D_1\delta-\beta_2}{M}
 =\frac{-3d_0\lambda^2+4\delta\eta^2+
                   2\eta\lambda^3+4\eta\lambda t_2}
        {6\eta^2\lambda},
\qquad V=U-\mu S.
\tag{13}
\]
There is no assumption \(\mu\ne0\).
Substitute \(P=(U-S^2)/\delta\) into (11). The exact polynomial
identity in independent symbols \(S,U\) is
\[
\boxed{
K\!\left(\frac{U-S^2}{\delta},S\right)
   =\frac{M}{\delta^2}S^4(U-\mu S)+\mathcal R_4(S,U),}
\tag{14}
\]
where the ENTIRE lower polynomial is
\[
\begin{aligned}
\mathcal R_4(S,U)={}&
 \frac{M}{\delta^2}(U^3-2S^2U^2)
 +\frac{\beta_2}{\delta^2}(SU^2-2S^3U)
 +\frac{D_1}{\delta}S^3U\\
&+\frac{\alpha_2}{\delta^2}(U-S^2)^2\\
&+\frac{\alpha_1+\beta_1S+\gamma_1S^2}{\delta}(U-S^2)
  +\gamma_0S^2+2d_0S^3+\alpha_0 .
\end{aligned}
\tag{15}
\]
Every monomial of \(\mathcal R_4\) has ordinary total degree at
most four in \(S,U\). This is a displayed identity with all lower
coefficients, not a truncation modulo unspecified terms.

By (12), evaluation of \(\mathcal R_4(S,U)\) has intrinsic degree
at most \(4c\), unless it is zero. If \(\deg_vU=c\), the
degree-\(5c\) coefficient in (14) must cancel, so
\(\operatorname{lc}_vU=\mu\,\operatorname{lc}_vS\).
If \(\deg_vU<c\), including constant or zero \(U\), the same
comparison forces \(\mu=0\). Indeed otherwise the only term of
degree \(5c\) would be \(-M\mu S^5/\delta^2\).
It follows in every case that
\[
\boxed{\deg_vV<c\quad\hbox{or }V=0.}
\tag{16}
\]
In the first case above \(\mu\) is automatically nonzero, but it
was not divided by; the second case explicitly retains \(\mu=0\).

Replacing \(U\) by \(\mu S+V\) in (14) now gives
\[
\boxed{
K\!\left(\frac{\mu S+V-S^2}{\delta},S\right)
 =\frac{M}{\delta^2}S^4V+\widetilde{\mathcal R}_4(S,V),
\qquad
\widetilde{\mathcal R}_4=\mathcal R_4(S,\mu S+V).}
\tag{17}
\]
The lower polynomial still has ordinary total degree at most four.
For a complete support check, the possible exponent pairs \((i,j)\)
of its full right side are contained in
\[
\begin{gathered}
(4,1),(4,0),(3,1),(3,0),(2,2),(2,1),(2,0),\\
(1,2),(1,1),(1,0),(0,3),(0,2),(0,1),(0,0).
\end{gathered}
\tag{18}
\]
Here \((i,j)\) denotes \(S^iV^j\). The coefficient at \((4,1)\)
is exactly \(M/\delta^2=12\eta^2\lambda/\delta^2\ne0\).
Every other listed pair has \(i+j\le4\); any of their coefficients
may vanish. Formula (15) specifies every one of them.

Suppose now that \(V\) has positive degree \(h<c\).
The first term of (17) has degree \(4c+h>4c\), with nonzero
leading coefficient. Every monomial of
\(\widetilde{\mathcal R}_4(S,V)\) has degree at most \(4c\),
because both input degrees are at most \(c\) and its total degree
is at most four. Thus the leading term cannot cancel. This
contradicts the exact degree \(4c-1\) in (6).
We have proved
\[
\boxed{V=v_0\in L.}
\tag{19}
\]
The symbol \(v_0\) in (19) is a coefficient constant, not the
original intrinsic variable \(v\). It may be zero.

## 5. Whole polynomial generation forces c=1

From (9),(13),(19),
\[
P=\frac{\mu S+v_0-S^2}{\delta}\in L[S],
\qquad z=\lambda P+S\in L[S].
\tag{20}
\]
Since \(z\ne0\), the third level in (4) gives
\[
q=-\frac{z^2+T(P)}{2\eta z}\in L(S).
\tag{21}
\]
This division is a statement in the fraction field only.
The evaluated polynomial \(z\) is not declared a unit of \(O\).

To recover the polynomial statement, use the elementary intersection
\[
L(S)\cap L[v]=L[S]\qquad(S\in L[v]\hbox{ nonconstant}).
\tag{22}
\]
Here is its full proof. Write an element of the intersection as
\(A_*(S)/B_*(S)\), with \(A_*,B_*\in L[T]\) coprime.
The Euclidean algorithm supplies \(I_*A_*+J_*B_*=1\).
Since \(B_*(S)\) divides \(A_*(S)\) in \(L[v]\), it then divides
one. Hence \(B_*(S)\) is a polynomial unit. Because \(S\) has
positive degree, this forces \(B_*\) to be constant. This proves
(22) without assuming that any unrelated projected ring is normal.

Apply (22) to (21). Then \(q\in L[S]\). Together with (20) and
the whole return in (4), this gives
\[
O=L[P,z,q]\subseteq L[S]\subseteq O,\qquad
\boxed{O=L[S]=L[v].}
\tag{23}
\]
The second inclusion uses \(S=z-\lambda P\in O\).
Write \(v\) as a polynomial in \(S\). That polynomial is nonconstant,
so its intrinsic degree is \(c\) times its positive polynomial degree.
It equals the degree one of \(v\). Therefore \(c=1\), and
\(a=2c=2\). Equation (4) now gives \(\deg_v y=\deg_v\theta=4\),
which proves (1).

## 6. Scope and verification

This proof consumes the complete half-degree normal form465, not
a speculative replacement for it. That held source was read through
EOF before this note was written. The complete461 source had also
been freshly read for the genuine minor and strict-degree reduction.
Their full264/296/458/460 dependencies remain retained rather than
recursively re-certified here.

Fresh unsaved971249 first rebuilt the residual substitution and the
full support (18). Fresh6ef110 independently reconstructed the
identity \(zW-K=B(P)\mathcal H\), every coefficient of (8), the
relation (10), the nonzero \(S^4V\) coefficient and the complete
support again. Fresh eea675 checked the exact decomposition
(14),(15), including its ordinary total-degree bound four.
All displayed identity residuals were zero. The general degree
comparisons in Sections 3--4, not finite samples of \(c\), are the
proof of the descent.

All zero lower-coefficient cases, \(U=0\), constant \(U\), \(\mu=0\),
\(V=0\), and constant nonzero \(V\) have been retained. The only
new scalar divisions are by the nonzero \(\eta,\lambda,M,\delta\).
The fraction-field step (21) is followed by the separate polynomial
intersection proof before whole-ring generation is used.

The result is \(a=2\) for the strict branch with \(a>1\), not exclusion
of that final quadratic case. It does not invoke a pending
quadratic-case proof, the bound twelve, or any balanced-case claim.
In particular it proves no original coordinate recovery or
recognition theorem. No actual realization is asserted.

No saved checker was executed, imported, compiled, or rerun.
Only this newly assigned source was written; no earlier source
or canonical index was edited. No unrestricted cancellation,
historical novelty, external expert review, or formal certification
is claimed.

