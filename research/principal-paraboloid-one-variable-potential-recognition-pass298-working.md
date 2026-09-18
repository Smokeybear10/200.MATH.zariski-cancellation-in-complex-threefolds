# A one-variable potential in the nonzero-coupling paraboloid chart

Working result: the actual chart264 is recognized under the additional
conditions \(k=s\), \(n=0\), and \(\ell_s=0\). No affine or
rational ansatz for \(\ell\) is imposed. When the first intercept
is nonconstant on the generic line, its nonlinear potential is
excluded by the full scalar determinant and strong actual field
return. The remaining affine potential is the actual sector297.

This does not normalize arbitrary nonzero coupling. The condition
\(\ell_s=0\), like \(k=s,n=0\), is a genuine additional hypothesis.
All new parameters below belong to exact coefficient fields; none
is promoted to an original polynomial coordinate.

## 1. Actual hypotheses and a fourth potential in this sector

Retain the entire actual entry of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and its projection clarification
[290](principal-paraboloid-nonzero-coupling-projection-pass290-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\qquad a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad K=\operatorname{Frac}A=L(v),
\quad Nv=1,\\
K=\mathbb C(y,z,w),\qquad L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here \(N\) is the exact shift-four part of the literal Z-partial.
The coefficient partials initially fix \(v\). Assume
\[
k=s,\qquad n=0,\qquad \ell_s=0.
\tag{2}
\]
Put \(F=\ker_L\partial_s\). This field is finite over
\(\mathbb C(t)\), and its exact t-derivative has constants
\(\mathbb C\). Indeed a constant in the finite function field
is algebraic over the base constant field, which is algebraically
closed. In particular \(\ell\in F\). Write
\(A_1=\ell_t\in F\); this notation is unrelated to the sliced
kernel \(A\) and the speed \(a_0\).

The literal potentials and the full fixed-X map are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta,& w&=\ell-2\sigma y,
&h&=y^2-A_1\sigma\in L,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]
In particular \(L[y,\sigma,\theta]=L[v]\). We do not yet
assert a two-generator plane return.

The coefficient of X in the determinant in (1), after (3), is
\[
-A_1y_v-(A_1'\sigma+h_t)\sigma_v-h_s\theta_v.
\tag{4}
\]
The prime means the exact t-derivative on \(F\), whereas
\(h_t,h_s\) in this display are the original coefficient partials.
For a direct reconstruction, subtract \(2t\) times the first
differential row from the second. The three rows become
\[
dy+X\,d\sigma+X^2dt,\quad
2\sigma\,d\sigma+d\theta+2y\,dt+X(2\sigma dt+ds),\quad
d\ell-2\sigma dy-2y\,d\sigma+X\,d\theta+X^2ds.
\]
Expand their determinant and substitute
\(2y\,dy-A_1d\sigma=A_1'\sigma dt+dh\).
This gives exactly (4), including its sign.
Its vanishing integrates in the polynomial line variable:
\[
\boxed{-A_1y-\frac{A_1'}2\sigma^2-h_t\sigma-h_s\theta=j,
\qquad j\in L.}
\tag{5}
\]
Thus (5) is a consequence of the remaining full scalar coefficient,
not merely of the first three potentials.

If \(A_1=0\), exact constants give \(\ell\in\mathbb C\).
The constant-potential obstruction in the completely read
[297](principal-paraboloid-nagata-degree-lowering-pass297-working.md)
applies: \(Y^2+X(W-\ell-XZ)=y^2\) is an original polynomial
of exact Z-degree one. Normality would make \(y\) a polynomial,
contradicting the parity of the degree of its square. Henceforth
\(A_1\ne0\).

## 2. A constant first intercept gives an actual preserved three-ring

Suppose \(y\in L\). Equation (3) gives \(\sigma\in L\) and
\(w\in L\). The whole-line return therefore gives
\(L[\theta]=L[v]\), with \(N\theta\in L^*\).

Extend \(N\) to \(\mathcal B=A[u]\) by \(Nu=0\), and use the
actual derivation
\[
\mathcal P=a_0N-(NX)E.
\tag{6}
\]
It fixes X, commutes with E, and is locally nilpotent: on
\(\mathcal B_{a_0}=A_{a_0}[X]\) it acts as \(a_0N\) at
fixed X. Here \(Na_0=0\), and its restriction preserves the
original ring. Formula (3) gives
\[
\mathcal PX=\mathcal PY=0,\qquad
\mathcal PZ=\tau,\qquad \mathcal PW=X\tau,
\qquad \tau=a_0N\theta\ne0.
\tag{7}
\]
Make only the actual polynomial shear
\[
T_0=W-XZ,\qquad W=T_0+XZ.
\tag{8}
\]
In the coordinate frame \((X,Y,Z,T_0)\), (7) says
\(\mathcal P=\tau\partial_Z\). Since the ring is a domain,
\[
S:=\ker_{\mathcal B}\mathcal P=\mathbb C[X,Y,T_0],
\qquad E(S)\subset S.
\tag{9}
\]
No assertion that \(\tau\) is an original-ring unit is needed.

For completeness, restrict E to S and divide its three coefficients
by their gcd \(\Delta\). Local nilpotence implies
\(E\Delta=0\): the gcd property gives
\(\Delta\mid E\Delta\), and the additive degree of an LND
rules out a nonzero divisible derivative. Thus the quotient
derivation is irreducible and still has X as a nonfixed coordinate
with square-zero second derivative.
[Dasgupta--Gupta, Theorem 4.8, restating Daigle](https://arxiv.org/html/1701.03635v1)
gives an actual invariant coordinate of S. It remains a coordinate
of \(\mathcal B=S[Z]\). The kernel A is regular and affine
because \(\mathcal B=A[u]\), so
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
recognizes \(A\cong\mathbb C^{[3]}\).

This argument applies even if \(\ell''\ne0\). We therefore do
not claim that all frames under (2) have affine \(\ell\).

## 3. Nonconstant first intercept and exact reparameterization

Suppose \(y\notin L\). If \(h_s=0\), equations (3),(5)
would give the nonzero polynomial identity
\[
-A_1y-\frac{A_1'}{2A_1^2}(y^2-h)^2
-\frac{h_t}{A_1}(y^2-h)-j=0.
\]
Its odd coefficient is \(-A_1y\), so it cannot vanish as a
formal polynomial in y. A nonconstant element of \(L[v]\) is
transcendental over L, a contradiction. Hence \(h_s\ne0\).
Equations (3),(5) then express \(\sigma,\theta\) polynomially
in y over L, and the whole-line return gives
\[
L[y]=L[v],\qquad y_v\in L^*.
\tag{10}
\]

Use \(\rho=h\) as a coefficient parameter, and write
\[
s=H(t,\rho),\qquad H_\rho=1/h_s\ne0,
\qquad T=H_\rho j.
\tag{11}
\]
The new coefficient partials are
\(\partial_\rho=H_\rho\partial_s\) and
\(\partial_t^{\rm new}=\partial_t^{\rm old}+H_t\partial_s\).
They commute on the finite extension \(L/\mathbb C(t,\rho)\).
Their \(\partial_\rho\)-constant field is exactly the same F,
and their t-derivative restricts to the old derivative on F.
Initially they fix v; using the affine y in (10) as the line
parameter then gives a second triangular parameter change.

For an independent formal line variable U, put
\[
P=\frac{U^2-\rho}{A_1}.
\]
The complete intercept formulas in these coordinates are
\[
\boxed{
\begin{aligned}
\sigma&=P,\\
\theta&=H_tP-H_\rho\left(A_1U+\frac{A_1'}2P^2\right)-T,\\
z&=\left(1-\frac{A_1'H_\rho}{2}\right)P^2
            +H_tP+(2t-A_1H_\rho)U-T,\\
w&=\ell-2UP.
\end{aligned}}
\tag{12}
\]
The term \(H_tP\) uses \(h_t^{\rm old}=-H_t/H_\rho\).
All t-derivatives in (12) now hold \(\rho,U\) fixed.
These formulas make no rationality assertion about \(L/F(\rho)\).

The intercept determinant, with U finally evaluated at y, satisfies
\[
\mathcal J=\det\frac{\partial(y,z,w)}{\partial(t,\rho,y)}
=-\frac{a_0^4H_\rho}{y_v}\in L^*.
\tag{13}
\]
The coefficient-field and affine line changes contribute precisely
\(H_\rho/y_v\). Their moving t- and rho-coefficients do not
alter this triangular Jacobian factor. In particular \(\mathcal J\)
is independent of the formal U.

## 4. The scalar ledger when the potential is nonlinear

Assume \(A_1'\ne0\). Since the first row of the intercept map
in (13) is U itself, its literal determinant is simply
\[
\mathcal J=z_t w_\rho-z_\rho w_t.
\tag{14}
\]
All the following coefficient identities are obtained from (12),(14),
retaining H and T as arbitrary elements of L until each stated gate.
The coefficient of \(U^7\) is
\[
[U^7]\mathcal J=\frac{(A_1')^2H_{\rho\rho}}{A_1^4}.
\tag{15}
\]
Thus \(H_{\rho\rho}=0\). Exact integration in the field L,
with \(\ker\partial_\rho=F\), gives
\(H=b\rho+c\), \(b,c\in F\), \(b\ne0\).
For example \(b=H_\rho\in F\) and
\(c=H-\rho H_\rho\in F\), so no rational ansatz is used.

Set
\[
V_0=bA_1''+3A_1'b',\qquad
D_0=H_{tt}+A_1'T_\rho .
\]
After this first gate, the remaining needed literal coefficients are
\[
\begin{aligned}
[U^5]\mathcal J&=-V_0/A_1^3,\\
[U^3]\mathcal J&=2(\rho V_0+A_1D_0)/A_1^3,\\
[U^2]\mathcal J&=-3\bigl((A_1b)'-2\bigr)/A_1,\\
[U]\mathcal J&=-(\rho^2V_0+2\rho A_1D_0
                              +2A_1^2T_t)/A_1^3,\\
[1]\mathcal J&=\rho\bigl((A_1b)'-2\bigr)/A_1
                                       +A_1T_\rho+H_t.
\end{aligned}
\tag{16}
\]
The coefficients of \(U^6,U^4\) vanish after
\(H_{\rho\rho}=0\). These displays include all coefficients
needed to reconstruct the successive deductions:
\[
V_0=0,\qquad (A_1b)'=2,\qquad
H_{tt}+A_1'T_\rho=0,\qquad T_t=0.
\tag{17}
\]

The third equation expresses \(T_\rho\) as a polynomial of
degree at most one in rho with coefficients in F. Subtraction
and exact integration show \(T\in F[\rho]\) of degree at most
two. Its vanishing t-derivative then makes all these coefficients
complex. Write
\[
T=\frac{\alpha}{2}\rho^2+\beta\rho+\gamma,
\qquad \alpha,\beta,\gamma\in\mathbb C.
\tag{18}
\]
The third identity in (17) gives
\(b''=-\alpha A_1'\), \(c''=-\beta A_1'\).
Consequently \(b'+\alpha A_1\) and \(c'+\beta A_1\) are
complex constants. Differentiate \((A_1b)'=2\), and subtract
the result from \(V_0=0\); this gives
\(A_1'(b'+\alpha A_1)=0\). Since \(A_1'\ne0\),
\[
\boxed{
b'=-\alpha A_1,\quad c'=-\beta A_1+\delta,\quad
A_1b=2t+\varepsilon,\qquad
\delta,\varepsilon\in\mathbb C,\quad\mathcal J=\delta\ne0.}
\tag{19}
\]
Nonzero calibration, not a rationality assumption, gives
\(\delta\in\mathbb C^*\).

## 5. Strong field return excludes every nonlinear case

The identities just proved simplify the full z in (12) to
\[
\boxed{z=\delta P-\frac{\alpha}{2}y^4
                   -\beta y^2-\varepsilon y-\gamma,
\qquad w=\ell-2yP.}
\tag{20}
\]
For an explicit check, \(A_1'b=2+\alpha A_1^2\), so the
quadratic P-coefficient in (12) is \(-\alpha A_1^2/2\).
The terms with \(A_1P+\rho\) then combine using
\(A_1P+\rho=y^2\), giving (20) including its constants.

Since \(\delta\ne0\), these equations have the polynomial
intercept inverse
\[
P=\frac{z+\alpha y^4/2+\beta y^2+\varepsilon y+\gamma}{\delta},
\qquad \ell=w+2yP.
\tag{21}
\]
Both inclusions, using the strong actual return in (1), give
\[
\boxed{K=\mathbb C(y,z,w)=\mathbb C(y,P,\ell).}
\tag{22}
\]
These three generators are algebraically independent over
\(\mathbb C\), since \(\operatorname{trdeg}_{\mathbb C}K=3\).
This is a statement about the actual invariant fraction field,
not a claim that the intercept inverse is an ambient automorphism.

If \(\alpha=0\), (19) makes \(b\in\mathbb C^*\), and
\(A_1=(2t+\varepsilon)/b\). Exact integration gives
\[
\ell=\frac{(t+\varepsilon/2)^2}{b}+\ell_0,
\qquad \ell_0\in\mathbb C.
\tag{23}
\]
The polynomial \((T+\varepsilon/2)^2-b(\ell-\ell_0)\)
is irreducible of degree two over \(\mathbb C(\ell)\): its
right-hand side has a simple zero and so is not a rational square.
It remains irreducible after adjoining the independent y and P.
Equation (23) contradicts \(t\in K\) and (22).

If \(\alpha\ne0\), integrate (19) to get
\[
b=-\alpha(\ell-\ell_0),\qquad
b^2+2\alpha(t+\varepsilon/2)^2=D,
\qquad \ell_0,D\in\mathbb C.
\tag{24}
\]
For the second integral, its derivative is
\(2bb'+4\alpha(t+\varepsilon/2)=0\) by (19).
Moreover \(D\ne0\). If it were zero, the algebraic closure of
\(\mathbb C\) and the domain property would make b a constant
multiple of \(t+\varepsilon/2\); then
\(A_1=(2t+\varepsilon)/b\) would be constant, contrary to
\(A_1'\ne0\).

Eliminating b in (24) gives
\[
2\alpha(t+\varepsilon/2)^2
=D-\alpha^2(\ell-\ell_0)^2.
\tag{25}
\]
The right-hand side has two distinct simple zeros as a polynomial
in the transcendental \(\ell\), because \(D\alpha\ne0\).
It is not a square in \(\mathbb C(\ell)\), even after dividing
by the nonzero complex scalar \(2\alpha\). Thus (25) is again
an irreducible quadratic for t over \(\mathbb C(\ell)\), and
remains irreducible over \(\mathbb C(\ell)(y,P)=K\).
This contradicts \(t\in K\).

Both possibilities for \(\alpha\) are excluded. Therefore in
the nonconstant-y branch one must have \(A_1'=0\).

## 6. Endpoint and exact scope

Since \(A_1\in F\) and F has constant field \(\mathbb C\),
\(A_1'=0\) gives
\(\ell=\lambda t+\mu\), \(\lambda\in\mathbb C^*\),
\(\mu\in\mathbb C\). The completely read actual map297 then
provides an explicit polynomial coordinate frame with three
square-zero second derivatives. Its recognition conclusion is
subject to the retained three-good theorem156 and its stated
dependencies. In the constant-y branch, Section2 instead gives
the direct actual three-ring and invariant-coordinate endpoint.
Consequently
\[
\boxed{k=s,\ n=0,\ \ell_s=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}}
\tag{26}
\]
under every actual hypothesis in (1).

This result does not prove that \(k\) can be made affine, that
\(n\) can be removed, or that \(\ell_s\) must vanish in an
arbitrary coupled chart. The separate \(\ell_s\ne0\) sector
and the general nonzero-coupling problem remain open here.
It asserts no realized example or unrestricted cancellation.

The entire direct sources264,290 and297 were read through EOF.
Fresh unsaved algebra reconstructed the scalar coefficients
(15),(16), and the full intercept simplification and inverse
(20),(21). These finite identities do not certify the exact-field
or actual-ring arguments, which are supplied above. The primary
three-variable and regular-kernel theorems were freshly inspected.
No saved checker was executed, imported, or compiled; no retained
proof was edited and no novelty claim is made.
