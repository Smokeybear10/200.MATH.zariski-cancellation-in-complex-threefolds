# Conditional recognition of the split pure-quartic reciprocal branch

Status: working recognition proof under the additional coefficient and
projection hypotheses explicitly stated below. It constructs an invariant
coordinate of the original polynomial four-ring. It does not establish
that every nonzero-R split chart satisfies those hypotheses.

In particular, the square-completion alternatives are outside this note.
No affine-solution conclusion from the absent-variable differential
equation189 is imported into the split case.

## 1. The supplied actual chart and the conditional branch

Assume the actual globally sliced setup of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):

\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\quad
\mathcal A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4),\\
a_E=EX,\quad t=EY/a_E,\quad
\rho=(E^2W/2)/a_E^2,\quad q=(E^2Z/2)/a_E^2=-t^3-t^{-1}.
\end{gathered}
\tag{1}
\]

The four displayed generators are actual polynomial coordinates and the
displayed ideal is the full weighted initial kernel, with weights
\((1,1,2,2)\). The occurring \(Z\)-pivot gives

\[
\begin{gathered}
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\quad
\mathcal A_L=L[v],\quad Nv=1,\quad a_E\in L^*,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a_E^3.
\end{gathered}
\tag{2}
\]

The determinant holds at fixed \(X\) and is independent of \(X\).
The ratios \(t,\rho\) are independent, their coefficient partials
extend uniquely and commute on \(L\), and initially fix \(v\).
The field \(K\) and its constant assertion follow by the usual monic
minimal-polynomial differentiation over the finite separable field in
(2). No rationality of \(K\) is assumed. The original action on the
localized chart is \(E=a_E\partial_X\), fixing \(L(v)\).

The following are additional branch hypotheses, not conclusions of this
note's use of the full split initial relation:

\[
\begin{gathered}
R=k_\rho=r\ne0,\quad R_\rho=0,\quad
\chi=\alpha t+\beta,\quad r=\chi^{-1},\quad
\alpha,\beta\in\mathbb C,\quad(\alpha,\beta)\ne(0,0),\\
k=r\rho+k_0,\quad n=c r^2\rho+n_0,\qquad
c\in\mathbb C,\quad k_0,n_0\in K,\\
y=\Gamma v+\eta,\quad \Gamma=Ny\in L^*,\quad \eta\in L,\qquad
\vartheta=P(y),\quad P\in L[U],\quad \deg P=4.
\end{gathered}
\tag{3}
\]

Thus the projected plane is a quartic graph in the original selected
axes. The pure eliminant property is also visible directly from these
coefficient hypotheses in Section 2. It is not inferred from a
generic plane-curve degree alone. Any theorem deriving (3) for an
additional class of actual charts is a separate input.

Changing the line parameter from \(v\) to \(y\) gives exactly

\[
\mathbb C(y,z,w)=L(y),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
 =-\frac{a_E^3}{\Gamma}\in L^*.
\tag{4}
\]

All coefficient partials below initially fix this independent \(y\).
The factor \(\Gamma\) is retained; no generic parameter change is
asserted to be an original-ring automorphism.

## 2. General-q elimination with all coefficient derivatives retained

Put \(Q=q''/2\), \(d=q'''/6\). For the literal split ratio,
\[
Q=-3t-t^{-3},\qquad d=t^{-4}-1,\qquad Q'=3d.
\tag{5}
\]

The universal equations, using \(r'=-\alpha r^2\), are

\[
\begin{gathered}
z=Qy^2+k_t y+r\vartheta+n,\qquad
rw+\mathcal S(y,\vartheta)=\ell,\\
(r'y+c r^2)w+\mathcal V(y,\vartheta)
 -\ell_t y-\ell_\rho\vartheta=m,\\
\mathcal S(U,V)=dU^3+\frac{k_{tt}}2U^2+r'UV+n_tU+c r^2V,\\
\mathcal V(U,V)=\frac{d'}4U^4+\frac{k_{ttt}}6U^3
 +\frac{r''}2U^2V+\frac{n_{tt}}2U^2+(c r^2)'UV,
\qquad \ell,m\in L.
\end{gathered}
\tag{6}
\]

Here coefficient \(t\)-partials still fix \(\rho\). In particular
\(k_{ttt}\) is not replaced by \(k_0'''\) before the \(\rho\) terms
are canceled.

The literal eliminant is

\[
\begin{aligned}
\mathcal H(U,V)
={}&r\{\mathcal V(U,V)-\ell_tU-\ell_\rho V-m\}\\
&+(r'U+c r^2)\{\ell-\mathcal S(U,V)\}.
\end{aligned}
\tag{7}
\]

It vanishes at \(y,\vartheta\). Its coefficient of \(V\) is
\[
\left(\frac{rr''}2-r'^2\right)U^2
 +\{r(c r^2)'-2r'c r^2\}U-r\ell_\rho-c^2r^4
 =\omega:=-r\ell_\rho-c^2r^4.
\]
There are no higher powers of \(V\). Define

\[
\begin{gathered}
D=\frac{\chi d'}4+\alpha d=-\alpha-\beta t^{-5}\ne0,\\
F_3=\frac{\chi k_0'''}6+\frac{\alpha k_0''}2-cd,\qquad
F_2=\frac{\chi n_0''}2+\alpha n_0'-\frac{c k_0''}2,\\
F(U)=DU^4+F_3U^3+F_2U^2,\\
p(U)=p_3U^3+p_2U^2+p_1U,\\
p_3=-\chi d-\alpha Q=4\alpha t+\beta-\beta t^{-4},\\
p_2=cQ-\frac{\chi k_0''}2-\alpha k_0',\qquad
p_1=c k_0'-\chi n_0'-\alpha n_0,\qquad p_t=-F_U.
\end{gathered}
\tag{8}
\]

The \(U^4\) coefficient of \(\mathcal H\) is
\(r d'/4-r'd=r^2D\ne0\). If \(\omega=0\), its evaluation would
give a nonzero polynomial relation in the transcendental \(y\).
Thus \(\omega\ne0\). It follows that the full eliminant is
\(\mathcal H=\omega(V-P(U))\) with \(P\) quartic, not a graph
times an unspecified nonconstant cofactor.

Set

\[
h=\chi\ell+c^2r^2\rho+c n_0.
\tag{9}
\]

Eliminating \(\vartheta\) from the first two equations of (6) gives

\[
w=(\alpha y-c)z+p(y)+h,\qquad
h_\rho=\chi\ell_\rho+c^2r^2=-\omega/r^2\ne0.
\tag{10}
\]

For example the coefficient of \(y^3\) in this elimination is
\(-d/r-\alpha Q=p_3\). The \(\rho\) terms in the lower
coefficients cancel using \(r''=2\alpha^2r^3\) and
\((c r^2)'=-2\alpha c r^3\); the constant term is exactly (9).
The identity \(p_t=-F_U\) in (8) follows coefficientwise from
\(Q'=3d\) and \(\chi'=\alpha\).

The element \(h\) is transcendental over \(K\), and \(L/K(h)\)
is finite separable. Define the new exact coefficient partials by

\[
\partial_h=h_\rho^{-1}\partial_\rho,\qquad
\partial_t^{\,h}
 =\partial_t^{\,\mathrm{old}}
  -\frac{h_t^{\,\mathrm{old}}}{h_\rho}\partial_\rho.
\tag{11}
\]

They commute, and \(\ker_L\partial_h=K\). A \(t\)-subscript on
\(L\) from now on means \(\partial_t^{\,h}\); on \(K\) it is
the same prime derivative as before. We have not yet asserted
\(L=K(h)\).

The remaining potential gives the full projected expression

\[
z=r\rho_hF(y)+Qy^2+(r\rho+k_0)_t y+z_0,\qquad
z_0=n+\rho_h(-m+c r\ell)\in L.
\tag{12}
\]

To verify the change of partials in this formula, its three high
coefficients besides \(Qy^2\), computed first with old partials,
are
\[
\frac{rD}{h_\rho},\qquad
\frac{k_0'''/6+\alpha r k_0''/2-c r d}{h_\rho},\qquad
\frac{n_0''/2+\alpha r n_0'-c r k_0''/2}{h_\rho}.
\]
These are \(r\rho_hD,r\rho_hF_3,r\rho_hF_2\).
The \(y\)-coefficient is
\(k_t^{\rm old}-r h_t^{\rm old}/h_\rho=(r\rho+k_0)_t\).
The constant is the displayed \(z_0\).
Thus (12) uses literal potential coefficients, not a guessed
replacement of the \(d=4t\) formula.

At \(X=0\), the determinant of \(y,z,w\) in (4), using (10), is
\(h_\rho z_t^{\rm old}-(p_t+h_t^{\rm old})z_\rho\).
After (11) this gives the calibrated scalar identity

\[
\delta z=-\frac{a_E^3\rho_h}{\Gamma}\in L^*,\qquad
\delta=\partial_t^{\,h}+F_U(y)\partial_h.
\tag{13}
\]

Its right side is independent of \(y\), but may depend on \(h\).
It is not treated as a rational cube.

## 3. The two possible reciprocal slopes in the split form

The \(y^7\) coefficient in (13), using (12), is
\(4rD^2\rho_{hh}\). Since \(rD\ne0\), two explicit primitive
subtractions with \(\partial_h\) give

\[
\rho=\lambda h+\kappa,\quad \lambda,\kappa\in K,\quad
\lambda\ne0,\qquad T=r\lambda\in K^*,\qquad
u_0=(r\kappa+k_0)'.
\tag{14}
\]

Consequently
\[
z=TDy^4+TF_3y^3+(Q+TF_2)y^2+(T'h+u_0)y+z_0.
\]
The coefficients \(y^4,y^3,y^2,y\) of its scalar equation give

\[
\begin{gathered}
5DT'+D'T=0,\\
(z_0)_h=b:=-\frac{TF_3'+4T'F_3}{4D}\in K,\qquad
z_0=bh+g_0,\quad g_0\in K,\\
Q'+TF_2'+3T'F_2+3F_3b=0,\qquad
T''h+u_0'+2F_2b=0.
\end{gathered}
\tag{15}
\]

All terms in the last equation other than \(h\) lie in \(K\).
Thus \(T''=0\), and the exact constants imply
\(T=A t+B\) with \(A,B\in\mathbb C\), not both zero.
Substituting the split value \(D=-\alpha-\beta t^{-5}\) into
the first equation in (15) gives

\[
-5\alpha A+5\beta B t^{-6}=0,\qquad
\alpha A=0,\quad \beta B=0.
\tag{16}
\]

There are exactly two possible cases:

- \(\alpha=0,\ \beta\ne0,\ B=0,\ T=A t,\ A\ne0\);
- \(\beta=0,\ \alpha\ne0,\ A=0,\ T=B,\ B\ne0\).

In particular \(\alpha\beta\ne0\) is impossible under the conditional
actual hypotheses here. The absent-variable conclusion
\(\alpha=0\) does not transfer unchanged: the second case survives
this calculation. No rationality of \(K\) was used.

The scalar term remaining after (15) is
\[
\delta z=b'h+g_0'\ne0.
\tag{17}
\]

## 4. Exact field return makes the last slope complex

Equations (10), (12), and (14)--(15) show that every coefficient
of \(z,w\), as polynomials in \(y\), is in \(K[h]\).
Actual field return in (4) therefore gives
\[
L(y)=\mathbb C(y,z,w)\subset K(h)(y)\subset L(y).
\]
Intersecting with \(L\), using independence of \(y\) and clearing
one polynomial denominator, proves \(L=K(h)\).

Put
\[
\widetilde w=w-(\alpha y-c)z=h+p(y).
\]
The first expression is a complex polynomial change in the projected
entries. Thus \(y,\widetilde w\) are independent over \(K\), and

\[
\begin{gathered}
K(y,\widetilde w)=\mathbb C(y,\widetilde w,z),\\
z=(Ay+b)\widetilde w+g(y),\\
g(U)=TD U^4+TF_3U^3+(Q+TF_2)U^2+u_0U+g_0-(AU+b)p(U)
 \in K[U].
\end{gathered}
\tag{18}
\]

Write \(g_j=[U^j]g\). Direct differentiation, using (8),
(15), and \(T'=A\), gives

\[
\begin{gathered}
g_4=TD-Ap_3=-(\alpha B+\beta A)\in\mathbb C^*,\\
g_3'=-p_3b',\qquad g_2'=-p_2b',\qquad
g_1'=-p_1b'.
\end{gathered}
\tag{19}
\]

For example
\[
g_3'=TF_3'+4AF_3+4Db-p_3b'=-p_3b'.
\]
The analogous cancellations for \(g_2,g_1\) are exactly the last
two equations of (15). The \(g_4\) identity uses (16), and its
nonvanishing follows in each of the two cases listed above.

Suppose \(b\notin\mathbb C\). Apply the exact linear-pencil lemma
from Section 3 of
[zero-R field190](weight-four-absent-zero-r-field-normal-form-pass190-working.md)
with \(F_0=\mathbb C(y)\), \(H=K(y)\), independent parameter
\(\widetilde w\), and
\[
z-Ay\widetilde w=b\widetilde w+g(y).
\]
The equality required by that lemma is exactly (18), since
\(A\in\mathbb C\). Also \(b\) is transcendental over \(F_0\).
The lemma gives \(g(y)\in\mathbb C(y)+\mathbb C(y)b\).

For precision, its algebraic proof first obtains
\(H=F_0(b,g(y))\) by intersecting fields of rational functions in
\(\widetilde w\). An irreducible relation \(\mathcal R(S,V)\)
for these two elements, of total degree \(j\), transforms to
\(\mathcal R(S,Z-\widetilde w S)\). Its degree in \(S\) is \(j\),
with nonzero leading coefficient
\(\mathcal R_j(1,-\widetilde w)\). Polynomial substitution and
Gauss's lemma preserve irreducibility, so the field extension
degree in (18) is \(j\). It is one, and hence the relation is
linear. This proves the stated affine-span conclusion without
assuming \(F_0\) algebraically closed.

Every coefficient of \(g(y)\in K[y]\) then belongs to
\(\mathbb C+\mathbb Cb\). Indeed, clear a common denominator in
\(\mathbb C[y]\), and compare components in a complex basis of
the finite span of \(1,b\) and those coefficients.
In particular \(g_3=c_0+c_1b\) with \(c_i\in\mathbb C\).
Since \(b'\ne0\), (19) would imply \(c_1=-p_3\).
But
\[
p_3=4\alpha t+\beta-\beta t^{-4}
\]
is nonconstant in both cases of (16). This is a contradiction.
Therefore

\[
b\in\mathbb C,\qquad
g(U)=G(U)+g_0,\quad G\in\mathbb C[U],\quad G(0)=0,
\qquad g_0'\ne0,\qquad K=\mathbb C(g_0).
\tag{20}
\]

The inequality follows from (17), not from an arbitrary choice of
coefficient parameter. For the last equality, (18) now reads
\(K(y,\widetilde w)=\mathbb C(g_0)(y,\widetilde w)\).
Intersect with \(K\), again using the two independent parameters.
This is a field equality, not yet an original-coordinate assertion.

## 5. The exact h-columns are original polynomials

All actual chart entries now belong to \(K[h,X,y]\).
For instance \(\rho=\lambda h+\kappa\),
\(k=T h+r\kappa+k_0\), and the formula for \(\vartheta\)
from (6) is polynomial in \(h,y\).
The exact coefficient partial \(\partial_h\) fixes \(X,y,t\).
Using \(z_h=Ay+b\) and \(k_h=T\), it gives

\[
Z_h=Ay+b+TX=A Y+B X+b=:B_0(X,Y)\in\mathbb C[X,Y].
\tag{21}
\]

For the other bad entry, the old partial in \(k_t y\) must still
be handled correctly. Its \(h\)-derivative is
\(r'\lambda=-\alpha rT\), and \(n_h=c rT\). Thus
\[
\vartheta_h
 =\chi(Ay+b)+(\alpha y-c)T.
\]
Since \(w_h=1+(\alpha y-c)(Ay+b)\) and
\(\rho_h=\chi T\), one obtains

\[
\begin{gathered}
W_h=1+(\alpha y-c)(Ay+b)
 +\{\chi(Ay+b)+(\alpha y-c)T\}X+\chi T X^2\\
 =1+\lambda_0(X,Y)B_0(X,Y),\qquad
\lambda_0(X,Y)=\alpha Y+\beta X-c\in\mathbb C[X,Y].
\end{gathered}
\tag{22}
\]

These are derivatives of the actual coordinate expressions.
They do not identify a field derivative with an original coordinate
partial without proof. The particular polynomial dependence in
(21)--(22) is the new original-ring gate.

Define the original polynomials

\[
J=W-\lambda_0Z,\qquad I_*=Z-B_0J.
\tag{23}
\]

These are successive triangular polynomial changes over
\(\mathbb C[X,Y]\), each with determinant one in the bad variables.
Equations (21)--(22) give \(J_h=1\) and \((I_*)_h=0\).
Because \(I_*\in K[h,X,y]\), this proves \(I_*\in K[X,y]\).
At \(X=0\),
\[
J=\widetilde w,\qquad I_*=z-(Ay+b)\widetilde w=G(y)+g_0.
\]

## 6. Full determinant transport and both original inverse orders

Changing the coefficient variables in (4) from \((t,\rho,y)\)
to \((t,y,h)\) multiplies the determinant by
\(-\rho_h=-\chi T\), which is nonzero and independent of \(X\).
The two changes (23) preserve the determinant in the three rows
\((Y,Z,W)\), because their coefficients lie in \(\mathbb C[X,Y]\)
and the \(Y\)-row is unchanged. Therefore
\[
\det\frac{\partial(Y,I_*,J)}{\partial(t,y,h)}
\]
is still independent of \(X\). Since \(Y=y+tX\),
\((I_*)_h=0\), and \(J_h=1\), it is
\(X(I_*)_y-(I_*)_t\).
At \(X=0\), (20) evaluates it to \(-g_0'\). Consequently

\[
(\partial_t-X\partial_y)I_*=g_0',\qquad
\mathcal Q(X,y):=I_*-g_0\in K[X,y],\qquad
(\partial_t-X\partial_y)\mathcal Q=0.
\tag{24}
\]

This uses the entire actual determinant, not merely its scalar
value at \(X=0\). The chain factor \(-\rho_h\), the speed \(a_E\),
and the original affine-parameter factor \(\Gamma\) have not been
discarded or normalized to one.

Substitute \(y=Y-tX\). Coefficient differentiation at fixed \(X,Y\)
in (24), and the exact constant field of \(K\), show

\[
Q_0(X,Y):=\mathcal Q(X,Y-tX)\in\mathbb C[X,Y],\qquad
I=I_*-Q_0(X,Y)=g_0.
\tag{25}
\]

This is polynomial coefficient transport: polynomiality in \(X,y\)
was established before the constant-field argument.
The complete original map and inverse, fixing \(X,Y\), are

\[
\begin{aligned}
J&=W-\lambda_0Z,&
I&=Z-B_0J-Q_0(X,Y),\\
Z&=I+Q_0(X,Y)+B_0J,&
W&=J+\lambda_0\{I+Q_0(X,Y)+B_0J\}.
\end{aligned}
\tag{26}
\]

Substituting the first line in the second recovers \(Z,W\).
Substituting the second line in the first recovers \(J,I\), by
canceling \(\lambda_0Z\) and then \(B_0J+Q_0\).
Every coefficient in both directions is an original complex
polynomial in \(X,Y\). Thus \(B=\mathbb C[X,Y,I,J]\).
Moreover \(I\in B\) equals \(g_0\in K\subset\operatorname{Frac}\mathcal A\),
so \(EI=0\) in the original ring. This is an actual invariant
ambient coordinate, not only a generic rational parameter.

## 7. Published recognition endpoint and the remaining hypotheses

The slice identifies \(\mathcal A\simeq B/(u)\).
Since \(Eu=1\), the four original partial derivatives of \(u\)
generate the unit ideal, so that hypersurface ring is regular.
In the actual coordinates of (26), \(E\) is a nonzero
\(\mathbb C[I]\)-linear LND on \(\mathbb C[I,X,Y,J]\).
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore gives

\[
\mathcal A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.
\tag{27}
\]

The exact primary statement and its short proof were checked
directly. Its nonzero-derivation, invariant-coordinate, and
regular-kernel hypotheses have all been supplied above.
This uses the published theorem as an input, not a recursive
verification of its dependencies.

The conditional conclusion is recognition under (1)--(3).
The proof explicitly allows both reciprocal cases of (16).
It does not prove that every nonzero-R split chart has
\(R_\rho=0\), reciprocal-linear \(R\), the stated \(n_\rho\),
or affine \(y\) with a pure-quartic graph. In particular it does
not exclude the separate square-completion alternatives.
Any derivation of those entry gates must be cited separately.
The zero-R recognition192 has a different proof and is not an
input to this conditional result.

No earlier file was changed, and no checker was executed,
imported, or compiled. This is a restricted working proof, not
unrestricted cancellation, historical novelty clearance, human
expert certification, proof-assistant verification, or a submission.
