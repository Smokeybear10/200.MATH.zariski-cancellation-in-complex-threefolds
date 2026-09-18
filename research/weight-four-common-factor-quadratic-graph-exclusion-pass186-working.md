# A quadratic graph is impossible for the common-factor quartic

**Status: working exclusion under the supplied actual chart and unit-cofactor hypotheses.**

For the full initial relation \(X^2Z+XYW-Y^4\), an affine first
projection cannot have a quadratic second projection. Literal
coefficient comparison first forces a nonzero complex constant
\(\lambda\). After an actual constant translation, the second
potential would have the nonzero coefficient \(-\lambda^3/4\)
at \(\rho^2y\). Its required independence of \(y\) is impossible.

This excludes one branch, without treating the exact coefficient
field as rational or declaring a generic parameter an original
coordinate. No new external classification theorem is used.

## 1. Actual inputs and the polynomial graph

Retain the hypotheses and conclusions of the
[universal chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h_0=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\mapsto(a\tau,b\tau,e\tau^2,h_0\tau^2),\\
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\end{gathered}
\tag{1}
\]
The coordinates are actual, the slice is global, and the kernel in
(1) is the entire initial ideal. For the selected derivation
\(N=[u^3](\partial_Z|_A)\), the exact field and parameter satisfy
\[
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
t=b/a,\quad \rho=h_0/a^2,\quad q=e/a^2=-t\rho+t^4,\quad
[L:\mathbb C(t,\rho)]<\infty.
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on \(L\).
The actual projections are
\(Y=y+tX,\ Z=z+\sigma X+qX^2,\ W=w+\vartheta X+\rho X^2\).

Assume the affine branch
\[
y=\gamma v+\eta,\quad \gamma\in L^*,\qquad
\vartheta=P(y),\quad P(U)=p_2U^2+p_1U+p_0,\quad p_2\in L^*.
\tag{3}
\]
Thus \(L[y]=L[v]\), and \(y\) is transcendental over \(L\).
The required unit-cofactor conclusion is separately supplied by
[selected-component184](weight-four-bad-linear-selected-component-pass184-working.md),
after its whole-plane input. Define divided coefficient Taylor
forms \(H_j\) as in chart184, and set
\[
\begin{gathered}
R=k_\rho-U,\quad
S=4tU^3+H_2(k;U,V)+H_1(n;U,V),\\
A_1=S_V=H_1(k_\rho;U,V)+n_\rho,\quad
T=U^4+H_3(k;U,V)+H_2(n;U,V),\\
\mathcal H=R(T-\ell_tU-\ell_\rho V-m)+A_1(\ell-S),\\
R(y)w+S(y,\vartheta)=\ell,\qquad
A_1(y,\vartheta)w+T(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,
\quad k,n,\ell,m\in L .
\end{gathered}
\tag{4}
\]
The exact total degree of \(\mathcal H\) is five and its top part
is \(-U^5\). For \(G=V-P(U)\), the unit evaluated cofactor gives
\[
\mathcal H=cG+G^2L_1(U,V),\qquad c\in L^*,\qquad \deg L_1=1.
\tag{5}
\]
Indeed \(G\) generates the whole evaluation ideal and
\(\mathcal H/G-c\) belongs to \((G)\). Degree five forces the
last degree assertion. No assertion that the cofactor polynomial
itself is constant has been made.

## 2. The cubic and quadratic coefficients in V

The top part in (5) forces
\(L_1=-U/p_2^2+d_0\), with no \(V\) term.
The literal coefficient
\[
[V^3]\mathcal H
 =\frac{k_\rho-U}{6}k_{\rho\rho\rho}
  -\frac{k_{\rho\rho}^2}{2}
\tag{6}
\]
must therefore vanish. Comparing its \(U\) coefficient and then
its constant coefficient gives \(k_{\rho\rho\rho}=k_{\rho\rho}=0\).

Put \(K=\ker_L\partial_\rho\). This field is finite over
\(\mathbb C(t)\), stable under \(\partial_t\), with
\(\partial_t\)-constants exactly \(\mathbb C\).
For the algebraicity assertion, differentiate a monic minimal
polynomial of an element of \(K\) over \(\mathbb C(t,\rho)\);
minimality forces its coefficients into \(\mathbb C(t)\).
Finite independent sets in \(K/\mathbb C(t)\) stay independent
after adjoining the transcendental \(\rho\), bounding the degree
by that in (2). The same argument for a joint constant, and
algebraic closedness of \(\mathbb C\), prove the constant assertion.
Also \(\rho\) is transcendental over \(K\): a separable algebraic
equation over \(K\), differentiated by \(\partial_\rho\), would
contradict \(\partial_\rho\rho=1\).

Subtracting an explicit primitive gives \(k=r\rho+k_0\), with
\(r,k_0\in K\). Write primes for \(\partial_t\) on \(K\).
The quadratic \(V\) coefficient of (4) is now
\((r-U)n_{\rho\rho}/2\). Comparing it with (5) yields
\[
h:=n_{\rho\rho}\ne0,\qquad hp_2^2=2,\qquad
\mathcal H=cG+\frac h2(r-U)G^2.
\tag{7}
\]
The letter \(h\) here is not the original leading coefficient \(h_0\).

The literal coefficient of \(V\) is
\[
[V]\mathcal H
 =(r-U)\{r''U^2/2+n_{t\rho}U-\ell_\rho\}
                 -(r'U+n_\rho)^2.
\tag{8}
\]
The coefficients of \(U^3,U^2\), compared with
\(c-h(r-U)P(U)\), give
\[
r''=-2hp_2,\qquad
p_2=-\frac4{r''},\quad h=\frac{(r'')^2}{8}\in K^*,\qquad
hp_1=-n_{t\rho}-(r')^2.
\tag{9}
\]
The nonzero assertions follow from (7). Explicit primitive
subtraction now gives
\(n=h\rho^2/2+s\rho+n_0\), with \(s,n_0\in K\).

At \(V=0\), the coefficient of \(U^4\) in (4) is
\(r-k_{ttt}/6-4tr'\). In (7) it is \(r-hp_2p_1\);
the term \(-cP\) has degree only two. Thus
\[
\frac{k_{ttt}}6+4tr'=hp_2p_1.
\tag{10}
\]
The coefficient of \(\rho\) on the left is \(r'''/6\).
On the right it is
\[
-p_2h'=\frac{4h'}{r''}=r''',
\]
using (9). Transcendence of \(\rho/K\) therefore forces
\(r'''=0\). The exact constant field, followed by the constant
part of (10), gives
\[
\begin{gathered}
r=\frac{\lambda}2t^2+\mu t+\nu,\quad
\lambda\in\mathbb C^*,\quad\mu,\nu\in\mathbb C,\quad
h=\frac{\lambda^2}{8},\quad p_2=-\frac4\lambda,\\
s'=\frac{\lambda}{24}k_0'''-\mu r',\qquad
s=\frac{\lambda}{24}k_0''-\mu r+s_0,\quad s_0\in\mathbb C.
\end{gathered}
\tag{11}
\]
Only finite explicit polynomial primitives were subtracted.

## 3. Normalize by actual constant translations

Apply
\[
\widetilde X=X+\mu,\quad \widetilde Y=Y-\nu,\quad
\widetilde Z=Z,\quad \widetilde W=W .
\tag{12}
\]
This is an original polynomial automorphism, with inverse constant
translation. The exact time degrees and full initial ideal are
unchanged. The pivot \(\partial_Z\), intrinsic \(N\), field \(L\),
and ratios \(t,\rho,q\) are unchanged as well.
Put \(r_1=\mu t+\nu\). Direct chart substitution gives
\[
\widetilde y=y-r_1,\qquad
\widetilde\vartheta=\vartheta-2\mu\rho,\qquad
\widetilde k=k+q_t r_1+2\mu\rho q_\rho-2\mu q
             =k-r_1\rho+4r_1t^3-2\mu t^4 .
\tag{13}
\]
For the \(k\) formula one substitutes
\(\widetilde\sigma=\sigma-2\mu q\) into
\(\widetilde\sigma=q_t\widetilde y+
q_\rho\widetilde\vartheta+\widetilde k\).
Thus \(\widetilde k_\rho=\lambda t^2/2\).
The new projected graph is still quadratic with nonzero leading
coefficient, and \(\widetilde y\) is still affine in \(v\).

Reapply (4)--(11) in this actual translated frame. This derives the
new integrated coefficients from the actual potentials, without
assuming a formula for how \(n,\ell,m\) transform.
Dropping tildes, the resulting normalization is
\[
\begin{gathered}
r=\lambda t^2/2,\quad h=\lambda^2/8,\quad
k=r\rho+k_0,\quad n=h\rho^2/2+s\rho+n_0,\\
s=\lambda k_0''/24+s_0,\quad k_0,n_0\in K,\quad s_0\in\mathbb C,\\
p_2=-4/\lambda,\qquad
p_1=-k_0'''/(3\lambda)-8t^2\in K .
\end{gathered}
\tag{14}
\]
No rationality of \(K\) or coefficient-field coordinate change of
the original fourfold has been used.

## 4. The graph's constant coefficient has a forced rho derivative

The coefficients of \(U\) and \(1\) in (8), using (9), give
\[
\ell_\rho=hp_0+r(r')^2+2r'n_\rho,\qquad
c=-(n_\rho+rr')^2 .
\tag{15}
\]
In particular \(D:=n_\rho+rr'\ne0\), since \(c\in L^*\).
Substitute \(P(U)\) into \(S(U,V)\).
Its cubic term is \(4t+r'p_2=0\), and its quadratic coefficient is
\[
\alpha=\frac{k_0''}3-\frac{tk_0'''}3
              -8\lambda t^3-\frac{4s_0}{\lambda}\in K .
\tag{16}
\]
Its linear coefficient is
\(r'p_0-(r')^2\rho+sp_1+n_0'\); its constant coefficient is
\((h\rho+s)p_0\).
Since \((r-y)w+S(y,P(y))=\ell\) and \(w\in L[y]\),
coefficient comparison gives
\[
\begin{gathered}
w=\alpha y+B,\qquad
B=r\alpha+r'p_0-(r')^2\rho+sp_1+n_0',\\
\ell=rB+(h\rho+s)p_0.
\end{gathered}
\tag{17}
\]
This includes the possibility \(\alpha=0\); no division by it occurs.
Differentiate the last equality in \(\rho\), holding coefficient
partials fixed as throughout:
\[
\ell_\rho=hp_0+(h\rho+s+rr')p_{0,\rho}-r(r')^2.
\]
Together with (15) this yields
\(D p_{0,\rho}=2r'D\). Cancelling the certified nonzero field
element \(D\), then subtracting an explicit primitive, proves
\[
p_0=2\lambda t\rho+P_0,\quad P_0\in K,\qquad
B=\lambda^2t^2\rho+B_0,\quad B_0\in K .
\tag{18}
\]
This is not a claim that \(D\) is a unit of the original ring.

## 5. A coefficient of the second potential cannot vanish

The coefficients \(k,n,\ell\) now lie in \(K[\rho]\), and the
graph and \(w\) lie in \(K[\rho][U]\). Also \(y\) is
transcendental over \(L\). Write
\(\overline P(U)=p_2U^2+p_1U+P_0\).
Equations (14), (17), and (18) give
\[
\begin{gathered}
P(U)=2\lambda t\rho+\overline P(U),\qquad
w(U)=\alpha U+\lambda^2t^2\rho+B_0,\\
A_1(U,P(U))=\lambda tU+h\rho+s,\\
[\rho^2]\ell=2h\lambda t=\lambda^3t/4,\qquad
[\rho^2]\ell_t=\lambda^3/4 .
\end{gathered}
\tag{19}
\]
Here and below brackets are coefficients in a polynomial ring,
justified by the transcendence of \(\rho/K\).
The literal fourth Taylor polynomial specializes to
\[
T=U^4+\frac{k_0'''}6U^3+\frac{\lambda}2U^2V
       +\frac{s''\rho+n_0''}{2}U^2+s'UV+\frac h2V^2 .
\tag{20}
\]

Consider the second potential as a polynomial in \(U\):
\[
\mathcal M(U)=
A_1(U,P(U))w(U)+T(U,P(U))-\ell_tU-\ell_\rho P(U).
\tag{21}
\]
Equation (4) requires \(\mathcal M(U)=m\) in \(L[U]\).
Its coefficient of \(U\) must therefore be zero, irrespective of
whether \(m\) is polynomial in \(\rho\).

In the first product of (21), a term of degree two in \(\rho\)
can only be the product \(h\rho\cdot\lambda^2t^2\rho\);
it has no \(U\) factor. In (20), the only term capable of degree
two in \(\rho\) after substitution is \(hP(U)^2/2\), whose
\(\rho^2\) coefficient likewise has no \(U\) factor.
Finally \(\ell_\rho\) has degree at most one in \(\rho\), and
the \(\rho\) coefficient of \(P(U)\) is independent of \(U\);
their product's \(\rho^2\) coefficient has no \(U\) factor.
The only contribution to \([\rho^2U]\mathcal M\) is consequently
\[
[\rho^2U]\mathcal M=-[\rho^2]\ell_t
                 =-\frac{\lambda^3}{4}\ne0 .
\tag{22}
\]
This contradicts the required zero \(U\) coefficient. A quadratic
graph in (3) is impossible.

## Scope and verification

The proof imports the actual chart and the full unit-cofactor
argument184, not merely a numerical eliminant or birational
projection. Its translation is an actual complex polynomial
automorphism; all subsequent coefficient fields remain exact.
Neither constant-\(y\) exclusion nor high-graph recognition185
is an input. The latter's translation mechanism was independently
reconstructed in (12)--(13).

The final contradiction does not require an additional determinant
normalization, a solution for \(k_0,n_0,P_0\), or an invariant
ambient coordinate. It uses only a necessary coefficient of the
second potential. Finite symbolic controls can check the arithmetic,
not supply the field or actual-chart hypotheses.

This is a restricted working proof, not unrestricted cancellation,
an arbitrary-entry theorem, historical novelty clearance, human
expert review, or proof-assistant certification. No earlier frozen
source, public posting, submission, or external contact is changed.
