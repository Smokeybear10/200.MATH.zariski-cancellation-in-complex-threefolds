# Low-degree graph recognition in the actual split chart

**Status: complete working derivation, pending review of this saved source.**

In the actual split setup175--177, a graph of degree at most one
has an explicit original polynomial reframe with all four coordinates
affine in the slice parameter, followed by an invariant coordinate.
The regular-kernel invariant-coordinate theorem recognizes the kernel.
A constant graph is in fact impossible.

The argument uses the selected cofactor's nonzero constant value on
the line. It does not assume that the literal eliminant is a scalar
multiple of the linear graph relation. No rationality of the coefficient
field, global unit speed, or descent of a projected coordinate is used.

## 1. Actual inputs and exact coefficient derivatives

Retain the full actual hypotheses of
[chart175](split-cubic-generic-chart-pass175-working.md), the
[selected-component result176](split-cubic-simple-selected-component-pass176-working.md),
and the
[affine first-projection conclusion177](split-quadratic-projection-exclusion-pass177-working.md).
Write the ambient ring as \(\mathscr B\), to distinguish it from
coefficient functions below:
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\\
a=EX\ne0,\quad b=EY,\quad
t=b/a,\quad \rho=(E^2W/2)/a^2,\\
N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
y=\gamma v+\eta,\quad \gamma\in L^*,\quad \eta\in L,\quad
\vartheta=\beta y+\chi,\quad \beta,\chi\in L .
\end{gathered}
\tag{1}
\]
The initial ideal is the full kernel. The graph assumption allows
\(\beta=0\), including the zero graph; no such case is discarded
at the outset.

The unique extensions of \(\partial_t,\partial_\rho\) to \(L\)
commute. Put \(K=\ker_L\partial_\rho\).
Their joint constant field is exactly \(\mathbb C\). Indeed if a
joint constant has monic minimal polynomial over
\(\mathbb C(t,\rho)\), differentiating that equation gives a
lower-degree relation unless each coefficient is killed by both
partials. Those coefficients are complex, and \(\mathbb C\) is
algebraically closed. All integrations below subtract explicitly
displayed primitives and then use this joint-constant assertion.
They do not assume \(K=\mathbb C(t)\).

We use the same derivatives on \(L\), extended to \(L[y]\) fixing
\(y\), when comparing coefficients. This is allowed because \(y\)
is transcendental over \(L\). It is not a replacement of the
original normalized \(v\)-derivative in any determinant formula.

The actual projection supplies
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X-t\rho X^2,\quad
W=w+\vartheta X+\rho X^2,\\
\sigma=-t\vartheta-\rho y+k,\qquad
z+tw=k_t y+(r-y)\vartheta+n,\quad r=k_\rho,\\
\mathbb C(y,z,w)=L(y),\qquad y,z,w,\vartheta\in L[y].
\end{gathered}
\tag{2}
\]
In particular the equality over \(\mathbb C\) in the last line is
an actual field-return condition, not merely the generic equality
after adjoining \(L\).

For independent \(U,V\), retain the literal potentials
\[
\begin{gathered}
f=\frac{k_{tt}}2U^2+r_tUV+\frac{r_\rho}2V^2+n_tU+n_\rho V,\qquad
g_3=H_3(k;U,V)+H_2(n;U,V),\\
(r-y)w+f(y,\vartheta)=\ell,\qquad
f_V(y,\vartheta)w+g_3(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,\\
\mathcal H=(r-U)(g_3-\ell_tU-\ell_\rho V-m)+f_V(\ell-f),
\qquad \ell,m\in L .
\end{gathered}
\tag{3}
\]
Here \(H_j\) is the divided directional Taylor polynomial of175.

## 2. Only evaluated cofactor information is needed

Let \(G=V-\beta U-\chi\). The retained results give
\(\mathcal H=GQ\), with \(Q(y,\vartheta)\in L^*\).
Since \(y\) is transcendental over \(L\), for some \(\lambda\in L^*\)
this says exactly
\[
Q(U,\beta U+\chi)=\lambda,\qquad
\mathcal H_V(U,\beta U+\chi)=\lambda,\qquad
\mathcal H_U(U,\beta U+\chi)=-\beta\lambda .
\tag{4}
\]
There may still be higher powers of \(G\) in \(\mathcal H\).
Nothing below sets them to zero.

The first potential, whose right side has degree at most two in
\(y\), forces \(w=hy+j\) with \(h,j\in L\).
Its coefficients give
\[
\begin{gathered}
h=\frac{k_{tt}+2\beta r_t+\beta^2r_\rho}{2},\qquad
T=r_t+\beta r_\rho,\qquad \epsilon=r_\rho\chi+n_\rho,\\
j=rh+T\chi+n_t+\beta n_\rho,\qquad
\ell=rj+\frac{r_\rho}2\chi^2+n_\rho\chi .
\end{gathered}
\tag{5}
\]
These formulas also cover \(h=0\) or constant \(w\).

For the rest of the coefficient calculation put
\[
\begin{gathered}
R=r-U,\quad F=f_V(U,\beta U+\chi)=TU+\epsilon,\quad
d_0=rT+\epsilon,\quad F=d_0-TR,\\
B_1=f_U(U,\beta U+\chi)-(hU+j)=-\beta F-Rh,\\
\mathcal C_i=f_i(U,\beta U+\chi)+r_i(hU+j)-\ell_i
             \quad(i=t,\rho).
\end{gathered}
\tag{6}
\]
The unit ideal \((r-y,f_V(y,\vartheta))=L[y]\) from176 implies
\(d_0\ne0\): otherwise both generators vanish at \(y=r\).

Differentiate the first potential as a polynomial identity, holding
\(U\) fixed. The evaluated-gradient identities175 then read
\[
\begin{gathered}
\mathcal C_i=-R(h_iU+j_i)-F(\beta_iU+\chi_i),\\
\mathcal H_V|_G=R\mathcal C_\rho-F^2
             =-R^2(h_\rho U+j_\rho)
              -RF(\beta_\rho U+\chi_\rho)-F^2,\\
\mathcal H_U|_G+\beta\mathcal H_V|_G
=R\{-R((Dh)U+Dj)-F((D\beta)U+D\chi-h)\}=0,\\
D=\partial_t+\beta\partial_\rho .
\end{gathered}
\tag{7}
\]
The notation \(|_G\) means substitution \(V=\beta U+\chi\);
\(D\) here acts on coefficients and fixes \(U\).
All identities are in \(L[U]\). No localization at \(R\) is made.

Comparing cubic coefficients in the second and third lines of (7)
with (4) gives, respectively,
\[
h_\rho=T\beta_\rho,\qquad Dh=T\,D\beta,\qquad
h_t=T\beta_t .
\tag{8}
\]
For the third line, its inner braces have quadratic coefficient
\(Dh-TD\beta\); multiplying by the nonzero linear \(R\)
proves the assertion. Thus (8) is the exact identity
\(dh=T\,d\beta\) for the two coefficient directions.

## 3. The remaining gradient coefficients

Use (8) in the second line of (7), and compare the coefficients
after replacing \(U\) by \(r-R\). The result is
\[
\lambda=-d_0^2,\qquad
\chi_\rho=2T-r\beta_\rho,\qquad
j_\rho=\epsilon\beta_\rho+T^2 .
\tag{9}
\]
For completeness, put \(A_0=r\beta_\rho+\chi_\rho\).
The constant term in \(R\) is \(-d_0^2\); its linear term is
\(d_0(2T-A_0)\).
Once that term vanishes, the quadratic term is
\(-rT\beta_\rho-j_\rho+d_0\beta_\rho+T^2\).
These are precisely (9), because \(d_0\ne0\).

Put \(\mathcal W=D\beta=\beta_t+\beta\beta_\rho\).
Using (8), the inner identity in the third line of (7) reduces to
\[
d_0\mathcal W U+F(D\chi-h)+R\,Dj=0 .
\]
Its two coefficients and \(d_0\ne0\) give
\[
D\chi=h-r\mathcal W,\qquad Dj=\epsilon\mathcal W,
\qquad
\chi_t=h-2\beta T-r\beta_t,\qquad
j_t=\epsilon\beta_t-\beta T^2 .
\tag{10}
\]
For instance, the constant coefficient first gives
\(Dj=-\epsilon(D\chi-h)/r\) when \(r\ne0\), but that division
is unnecessary: elimination of the two coefficients gives
\(d_0(D\chi-h+r\mathcal W)=0\) directly.
Thus (10) holds also when \(r=0\).

Commuting the two derivatives of \(\chi\) in (9)--(10), and
using (8), gives
\[
2DT+r_\rho\mathcal W=0 .
\]
On the other hand, differentiate the formula for \(h\) in (5)
with respect to \(\rho\), and use \(h_\rho=T\beta_\rho\):
\[
r_{tt}+2\beta r_{t\rho}+\beta^2r_{\rho\rho}=0,\qquad
DT=r_\rho\mathcal W .
\]
Consequently
\[
3r_\rho\mathcal W=0 .
\tag{11}
\]

## 4. Actual field return rules out the zero direction

Suppose \(\mathcal W=0\).
Extend \(D=\partial_t+\beta\partial_\rho\) from \(L\) to \(L(y)\)
fixing \(y\). Equations (8) and (10) give
\[
D\beta=Dh=Dj=0,\qquad D\vartheta=h,\qquad Dw=0,\qquad Dr=T .
\tag{12}
\]
Also \(Dk_t=k_{tt}+\beta r_t=2h-\beta T\).
Applying \(D\) to the actual identity for \(z\) in (2) therefore gives
\[
\begin{aligned}
Dz
&=(2h-\beta T)y+T(\beta y+\chi)+(r-y)h+Dn-w\\
&=T\chi+rh+Dn-j=0 ,
\end{aligned}
\tag{13}
\]
by (5). Thus \(D\) annihilates all of \(y,z,w\).
The actual equality \(\mathbb C(y,z,w)=L(y)\) forces \(D=0\)
on \(L(y)\), whereas \(Dt=1\).
This contradiction proves
\[
\mathcal W\ne0,\qquad r_\rho=0 .
\tag{14}
\]
In particular \(\beta=0\), or more generally a complex-constant
slope \(\beta\), is impossible. This is a conclusion, not an
extra graph hypothesis. The proof uses the full field return;
a formal low graph with the same first potentials need not satisfy it.

## 5. Exact complex constants and the remaining n coefficients

Equations (11) and (14) now give \(r_{tt}=0\).
The joint constant field, followed by (8)--(10), gives complex
constants \(\mu,\nu,h_0,c_0\) such that
\[
r=\mu t+\nu,\quad T=\mu,\quad h=\mu\beta+h_0,\quad
\chi+r\beta=2\mu\rho+h_0t+c_0 .
\tag{15}
\]
Indeed the last expression minus its right side has both partials
zero. Since \(k_\rho=r\), write \(k=r\rho+k_0\) with \(k_0\in K\).
The formula for \(h\) gives \(k_0''=2h_0\), hence
\[
k_0=h_0t^2+k_1t+k_{00},\qquad k_1,k_{00}\in\mathbb C .
\tag{16}
\]

Put \(s=n_\rho\), so \(\epsilon=s\).
Differentiate the formula for \(j\) in (5) in the rho direction
and compare it with (9); this gives
\[
s_t+\beta s_\rho=-\mu^2 .
\]
The mixed derivatives of \(j_t=s\beta_t-\beta\mu^2\) and
\(j_\rho=s\beta_\rho+\mu^2\) give
\[
s_\rho\beta_t-(s_t+\mu^2)\beta_\rho
=s_\rho(\beta_t+\beta\beta_\rho)=0 .
\]
Using (14) and then explicit integration yields
\[
s_\rho=0,\qquad s=-\mu^2t+s_0,\quad s_0\in\mathbb C,\qquad
d:=r\mu+s=\mu\nu+s_0\in\mathbb C^*,\quad \lambda=-d^2 .
\tag{17}
\]
Nonvanishing of \(d\) follows from (9), not from a global-unit
assumption about the original speed.

Write \(n=s\rho+n_0\), \(n_0\in K\).
Both partials of \(j-s\beta-\mu^2\rho\) vanish, so let this
complex constant be \(j_0\). Substitution into (5) and (15) gives
\[
\begin{gathered}
n_0'=j_0-h_0(r+\mu t)-\mu c_0,\qquad n_0''=-2\mu h_0,\\
n_0=-\mu h_0t^2+n_1t+n_{00},\qquad n_1,n_{00}\in\mathbb C .
\end{gathered}
\tag{18}
\]
Every coefficient integration in (15)--(18) subtracts a complex
polynomial and uses both coefficient derivatives. It is valid
over the original finite algebraic field \(L\).

## 6. Actual translations put k and n in polynomial form

Perform the original coordinate translation
\[
\widetilde X=X+\mu,\qquad \widetilde Y=Y-\nu,\qquad
\widetilde Z=Z,\qquad\widetilde W=W .
\tag{19}
\]
Both inverse orders are immediate by subtracting \(\mu\) and
adding \(\nu\). It preserves the speeds, the full leading kernel,
the selected \(\partial_Z\), and therefore \(N,L,t,\rho\).

For clarity the exact chart substitutions are
\[
\begin{gathered}
\widetilde y=y-r,\quad
\widetilde\vartheta=\vartheta-2\mu\rho,\quad
\widetilde w=w-\mu\vartheta+\mu^2\rho,\\
\widetilde\sigma=\sigma+2\mu t\rho,\qquad
\widetilde z=z-\mu\sigma-\mu^2t\rho .
\end{gathered}
\tag{20}
\]
They follow by replacing \(X\) with \(\widetilde X-\mu\)
in (2) and its chart. Substitution into the two integrated
identities in (2) gives
\[
\begin{gathered}
\widetilde k=k-r\rho=k_0,\qquad \widetilde r=0,\\
\widetilde n=n-\mu k+r k_t+\mu r\rho
=d\rho+\widetilde n_0,\qquad
\widetilde n_0=n_0-\mu k_0+r k_0',\\
\widetilde n_0''=-2\mu h_0-2\mu h_0+4\mu h_0=0 .
\end{gathered}
\tag{21}
\]
In explicit constants,
\(\widetilde n_0=(n_1+2\nu h_0)t+
n_{00}-\mu k_{00}+\nu k_1\).
This rechecks the same actual translation formulas used in178;
the nonlinear purity argument of that note is not imported.

Drop tildes. We have complex constants \(A_0,B_0,C_0,D_0,F_0\)
and \(d\ne0\) with
\[
r=0,\qquad k=A_0t^2+B_0t+C_0,\qquad
n=d\rho+D_0t+F_0 .
\tag{22}
\]
No condition on the transformed second potential \(m\) is needed.

## 7. A polynomial good-coordinate shear and recognition

In these normalized actual coordinates put \(H_{\rm sp}=XZ+YW\)
and define
\[
F_{\rm good}=C_0X^2+B_0XY+A_0Y^2+F_0X+D_0Y,\qquad
P_0=\frac{F_{\rm good}-H_{\rm sp}}d\in\mathbb C[X,Y,H_{\rm sp}] .
\tag{23}
\]
In the actual localized chart, holding all invariants fixed and
using \(Y=y+tX\), the literal identity175 gives
\[
H_{\rm sp}=yw+(k_t y+n)X+kX^2,\qquad
\partial_XF_{\rm good}=2kX+k_ty+D_0t+F_0 .
\]
It follows that
\[
\partial_XP_0=-\rho,\qquad EP_0=-a\rho,\qquad E^2P_0=0 .
\tag{24}
\]
These are identities in \(\mathscr B_a\); because \(P_0\) is an
original polynomial and \(\mathscr B\) is a domain, the resulting
identities for polynomial derivatives hold in \(\mathscr B\).
The element \(a\rho\) need not have been known polynomial before
this calculation.

Now make the actual polynomial transformation
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z-YP_0,\quad W_1=W+XP_0 .
\tag{25}
\]
It preserves \(XZ+YW=X_1Z_1+Y_1W_1\), hence preserves the
polynomial expression \(P_0(X,Y,H_{\rm sp})\).
Its inverse is
\[
X=X_1,\quad Y=Y_1,\quad
Z=Z_1+Y_1P_0(X_1,Y_1,X_1Z_1+Y_1W_1),\quad
W=W_1-X_1P_0(X_1,Y_1,X_1Z_1+Y_1W_1).
\]
Preservation of \(H_{\rm sp}\) verifies both compositions exactly.
No coefficient field element is used in this inverse.

The ordinary top relation and (24) give
\[
\begin{gathered}
E^2Z/2=-ab\rho,\qquad E^2W/2=a^2\rho,\\
E^2(YP_0)/2=b\,EP_0=-ab\rho,\qquad
E^2(XP_0)/2=a\,EP_0=-a^2\rho,\\
E^2X_1=E^2Y_1=E^2Z_1=E^2W_1=0 .
\end{gathered}
\tag{26}
\]
All four entries are actual polynomial coordinates, and the given
global slice is unchanged. There is also a direct invariant coordinate,
so the final recognition need not invoke the general three-good theorem.

Indeed (15), (17)--(18), and the substitutions (20) give, after
normalization,
\[
\vartheta=\beta y+h_0t+c_0,\qquad
w=h_0y+d\beta+D_0,\qquad
\ell=d(h_0t+c_0).
\tag{27}
\]
Here \(A_0=h_0\) in (22), and \(c_0\) is the same complex constant
as in (15). To verify the middle identity directly before dropping
tildes, its constant term is
\(d\beta+h_0\nu+j_0-\mu c_0=d\beta+D_0\),
because (18) gives
\(D_0=n_1+2\nu h_0=j_0+\nu h_0-\mu c_0\).
The last identity of (27) is the first potential in (3).

At \(X=0\), (23) and (27) give
\(P_0|_{X=0}=-\beta y=\ell/d-\vartheta\).
Together with \(\partial_XP_0=-\rho\) this yields
\[
W_1=w+(h_0t+c_0)X,\qquad
I=W_1-h_0Y_1-c_0X_1=d\beta+D_0,\qquad EI=0 .
\tag{28}
\]
The invariance calculation takes place in the actual localization
and therefore holds in the original domain. The change from
\((X_1,Y_1,Z_1,W_1)\) to \((X_1,Y_1,Z_1,I)\) is an actual
linear shear, with inverse \(W_1=I+h_0Y_1+c_0X_1\).
Composing it with the two-sided inverse of (25) gives the full
original-ring coordinate inverse. In particular (28) is not an
assertion that the coefficient \(\beta\) was originally a coordinate.

Apply Bhatwadekar--Gupta--Lokhande,
[Theorem 3.5](https://arxiv.org/html/1501.01438v1).
It states that a nonzero locally nilpotent derivation on a polynomial
four-ring over a characteristic-zero field, linear over the subring
generated by one coordinate, has kernel polynomial in two variables
over that subring if its kernel is regular. Here \(E\ne0\) because
\(Eu=1\), and it is \(\mathbb C[I]\)-linear on the actual ring
\(\mathbb C[I,X_1,Y_1,Z_1]\).
Finally \(A\simeq\mathscr B/(u)\) is regular: the equality
\(Eu=1\) expresses one as a polynomial combination of the four
partial derivatives of \(u\), so this hypersurface is smooth.
Every hypothesis of that theorem is therefore met, and
\(A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}\).

## Scope and verification boundary

This proves recognition for the graph of degree at most one under
the full actual split175--177 hypotheses. A constant graph is
excluded in (14); the remaining linear graph is recognized by
the actual transformations (19), (25), and (28).
It complements, rather than assumes, the nonlinear graph reduction178.

The exact primary Theorem 3.5 statement and its displayed proof
were freshly read for the endpoint. The full saved synthesis156
and actual translation and shear argument178 were also read,
but the direct invariant-coordinate endpoint does not require156.
This is not a new recursive certification of every historical input.
The decisive uses of actualness are the selected-cofactor input176,
the field equality in (2), and the original polynomial coordinates
and slice at the end.

No earlier source or packet was changed. No checker was run,
imported, or compiled for this note. These deductions are not a
human expert review, proof-assistant verification, novelty claim,
arbitrary-coordinate entry theorem, or proof of unrestricted
complex-threefold cancellation.
