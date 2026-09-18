# The split quartic zero-R branch has an original invariant coordinate

Status: working recognition proof for a supplied actual frame and the
additional branch condition \(k_\rho=0\). The full initial kernel is

\[
(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4).
\]

The proof constructs an invariant coordinate of the original polynomial
four-ring. It does not identify a generic rational parameter with such a
coordinate. The nonzero-R branch, other initial forms, arbitrary entry,
and unrestricted cancellation are not settled here.

## 1. Actual hypotheses and specialized potentials

Assume the full actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md):

\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,
\qquad \mathcal A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4),\\
\mathfrak a=EX,\quad \mathfrak b=EY,\quad
\mathfrak e=E^2Z/2,\quad \mathfrak h=E^2W/2.
\end{gathered}
\tag{1}
\]

The displayed ideal is the full weighted initial kernel for weights
\((1,1,2,2)\), not merely a vanishing relation. The occurring \(Z\)-pivot
gives the exact selected derivation and coefficient field

\[
\begin{gathered}
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\quad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\quad
\mathcal A_L=L[v],\quad Nv=1,\quad \mathfrak a\in L^*,\\
t=\mathfrak b/\mathfrak a,\quad
\rho=\mathfrak h/\mathfrak a^2,\quad
q=\mathfrak e/\mathfrak a^2=-t^3-t^{-1},\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-\mathfrak a^3.
\end{gathered}
\tag{2}
\]

The last determinant holds with \(X\) fixed and is independent of \(X\).
The variables \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on \(L\), initially fixing \(v\).
On the localized chart, \(E=\mathfrak a\partial_X\) fixes \(L[v]\).
No original-ring unit assumption on \(\mathfrak a\) is made.

Assume \(R=k_\rho=0\), and put

\[
K=\ker_L\partial_\rho,\qquad k\in K,\qquad
Q=q''/2=-3t-t^{-3},\qquad
d=q'''/6=t^{-4}-1,\qquad h=k''/2.
\tag{3}
\]

Here \(K/\mathbb C(t)\) is finite, its derivative constants are
\(\mathbb C\), and \(K\) is stable under \(\partial_t\).
For clarity, the usual minimal-polynomial proof applies over the exact
field: differentiating the monic minimal polynomial of an element killed
by \(\partial_\rho\) forces its coefficients into \(\mathbb C(t)\).
Finite independent sets remain independent after adjoining the
transcendental \(\rho\), which bounds the degree. The same argument for
the derivative on this one-variable algebraic function field gives the
stated constants. Rationality of \(K\) is not assumed.

The universal potentials specialize, without any division by \(R\), to

\[
\begin{gathered}
\sigma=q'y+k,\qquad z=Qy^2+k'y+n,\\
d y^3+h y^2+n_t y+n_\rho\vartheta=\ell,\\
n_\rho w+\mathcal V(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,\\
\mathcal V(U,V)=\frac{d'}4U^4+\frac{h'}3U^3
 +\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2,
\qquad n,\ell,m\in L.
\end{gathered}
\tag{4}
\]

Subscripts in (4) are the old coefficient partials fixing \(\rho\) or
\(t\), before evaluation. In particular \(d\ne0\) and \(Q'=3d\ne0\).

## 2. Constant projection is impossible; the remaining parameter is affine

The generalization explicitly proved at the end of
[zero-R187](weight-four-absent-variable-zero-r-reduction-pass187-working.md)
applies to \(q_\rho=0,q'''\ne0\). The needed argument is recalled to
make its dependence on the actual chart precise.

If \(y\in L\), then \(z,\sigma\in L\) and (2) makes \(w\) an affine
parameter over \(L\). Also \(y_\rho\ne0\), since otherwise the first
Jacobian row is \((X+y_t,0,0)\), contrary to its nonzero scalar
determinant. Substitution of (4) gives exactly

\[
J(X)=(w_v+\vartheta_vX)(n_\rho X+C_0),\qquad
C_0=y_tz_\rho-y_\rho z_t.
\tag{5}
\]

Both factors must be units in \(L[v][X]\). Thus \(n_\rho=0\),
\(\vartheta\in L\), and \(C_0\ne0\). In fact \(C_0=-\ell_\rho\),
so it would be incorrect to compare an independent \(\vartheta\)
coefficient in the second potential and conclude \(\ell_\rho=0\).

Intersecting \(\mathbb C(y,z)(w)=L(w)\) with \(L\) gives
\(L=\mathbb C(y,z)\). This uses that \(w\) is transcendental over \(L\):
clear denominators of a rational expression in \(w\) and compare a
nonzero denominator coefficient. The field derivation fixing \(L,X\)
and sending \(w\) to one is the actual original \(\partial_W\), since
it kills \(X,Y,Z\) and takes \(W\) to one. It commutes with
\(E=\mathfrak a\partial_X\). Hence \(E\) restricts to a nonzero LND
on the actual ring \(\mathbb C[X,Y,Z]\), killing \(X,Y\) after two
iterations.

Divide its coefficient gcd to obtain an irreducible LND with the same
kernel. This division preserves local nilpotence: if the gcd is
\(\Delta\), the identity \(E\Delta=\Delta D\Delta\) and additivity
of LND degree force \(E\Delta=0\), and then
\(E^j f=\Delta^jD^j f\). Wang's two-coordinate theorem applies.
Its invariant linear-form alternative contradicts the transcendence
of \(t=EY/EX\). Its other alternative gives an invariant coordinate
\(cZ+Q_*(X,Y)\), with \(c\in\mathbb C^*\), fixing \(X,Y\).
Since the time degree of a nonconstant polynomial in \(X,Y\) equals
its ordinary degree, its quadratic leading part must satisfy

\[
cq+Q_{*,2}(1,t)=0.
\tag{6}
\]

Differentiating three times contradicts \(q'''=6d\ne0\).
The exact theorem used is Wang's result as stated in
[Dasgupta--Gupta, Theorem 4.1](https://arxiv.org/pdf/1701.03635v1),
printed page 9. Its hypotheses and both alternatives were checked
directly for this application.

Therefore \(y\notin L\). If \(s:=n_\rho\) vanished, the cubic
potential in (4), with leading coefficient \(d\ne0\), would contradict
the transcendence of \(y\) over \(L\). Thus \(s\ne0\), and

\[
\begin{aligned}
P(U)&=(\ell-dU^3-hU^2-n_tU)/s,\\
\mathcal W(U)&=
 \{m-\mathcal V(U,P(U))+\ell_tU+\ell_\rho P(U)\}/s,\\
\vartheta&=P(y),\quad w=\mathcal W(y),\qquad
L[y]=L[v],\quad \Gamma:=Ny\in L^*.
\end{aligned}
\tag{7}
\]

Indeed both other projected entries are in \(L[y]\), so the whole-line
equality in (2) forces \(y\) affine in \(v\). No plane selected-component
result for a different initial form is used here.

The remaining determinant rows give the exact polynomial identities

\[
\mathcal W_U=P_t+P_UP_\rho,\qquad
\mathcal W_t+P_U\mathcal W_\rho
 =\frac{\mathfrak a^3}{s\Gamma}\in L^*.
\tag{8}
\]

For example, the middle reduced row is
\((-sP_U(y))dt+s\,d\rho\). Its constant wedge coefficient is
\(-s\Gamma(\mathcal W_t+P_U\mathcal W_\rho)\), which proves the sign
and the retained factor \(\Gamma\) in (8).

## 3. The exact cover and the general coefficient integral

Let \(A_3=-d/s\) be the cubic coefficient of \(P\). The first identity
in (8) gives \([U^6]\mathcal W=A_3(A_3)_\rho/2\). The \(U^8\)
coefficient of the second is
\(3A_3((A_3)_\rho^2+A_3(A_3)_{\rho\rho})/2\).
It vanishes, hence \((s^{-2})_{\rho\rho}=0\).
Set \(\eta=1/s\) and \(\partial_n=\eta\partial_\rho\). Its kernel
is \(K\) and it sends \(n\) to one. Since
\(\partial_n^2\eta=\eta(\eta^2)_{\rho\rho}/2=0\), explicit primitive
subtraction gives

\[
\rho=a n^2+b n+c,\qquad \eta=2an+b\ne0,
\qquad a,b,c\in K.
\tag{9}
\]

The symbol \(a\) in (9) is a cover coefficient, not the original speed
\(\mathfrak a\). The element \(n\) is transcendental over \(K\).
Extend the derivative of \(K\) fixing \(n\), then uniquely across the
finite separable extension \(L/K(n)\); denote it by a prime or
\(\nabla\). Then

\[
\partial_\rho=\eta^{-1}\partial_n,\quad
\partial_t^{\rm old}=\nabla-\frac{\rho'}\eta\partial_n,
\quad F(U)=dU^3+hU^2,\quad M=\eta\ell,
\quad \delta=\nabla-F_U\partial_n.
\tag{10}
\]

The new partials commute and \(\ker_L\partial_n=K\). Formula (8)
becomes \(P=\rho'U-\eta F+M\), \(\mathcal W_U=\delta P\), and
\(\delta\mathcal W=\mathfrak a^3/(s\Gamma)\in L^*\).
Integration only in the polynomial variable \(U\) gives

\[
\mathcal W=aF^2-\eta'UF
 -\eta\left(\frac{d'}4U^4+\frac{h'}3U^3\right)
 +\frac{\rho''}2U^2+M'U-M_nF+W_0,
\qquad W_0\in L.
\tag{11}
\]

Differentiating (11) gives \(\delta P\); no arbitrary algebraic
coefficient primitive was adjoined. In particular the \(d'\) term
has not been omitted. For \(\mathcal W_j=[U^j]\mathcal W\), the
coefficient recurrence is

\[
[U^j]\delta\mathcal W=
\mathcal W_j'-3d\partial_n\mathcal W_{j-2}
                 -2h\partial_n\mathcal W_{j-1}.
\tag{12}
\]

The \(U^6,U^5,U^2\) equations give, respectively,

\[
\begin{gathered}
2da'+ad'=0,\qquad
\mu:=M_{nn}=\frac{ahd'}{d^2}-\frac{4ah'}{3d},\qquad
M=\frac\mu2n^2+M_1n+M_0,\quad M_1,M_0\in K,\\
3d(W_0)_n=\frac{a'''}2n^2+
 \left(\frac{b'''}2-h'\mu-3h\mu'\right)n
 +\frac{c'''}2-h'M_1-3hM_1',\\
[n^3]W_0=\gamma:=\frac{a'''}{18d},\qquad W_0\in K[n].
\end{gathered}
\tag{13}
\]

For the first two equations the raw coefficients before simplification
are \(7d(ad'+2da')/2\) and
\(12a'dh+3ad'h+4adh'+3d^2M_{nn}\). Integrating the displayed
\(\partial_n\) equations means subtracting explicit polynomials in
\(n\); the remaining kernel is exactly \(K\).
These are the general formulas of
[cover189](weight-four-absent-zero-r-cover-collapse-pass189-working.md),
now derived with \(d=t^{-4}-1\), not with \(d=4t\).

All coefficients of \(z,w\) are now in \(K[n]\). Exact actual field
return, followed by clearing a denominator in the independent \(y\),
therefore gives

\[
L(y)=\mathbb C(y,z,w)=K(n)(y),\qquad
L=K(n),\qquad \mathbb C(y,z,w)=K(y)(z).
\tag{14}
\]

The last equality uses \(n=z-Qy^2-k'y\). In particular \(y,z\) are
independent over \(K\). This step uses the actual inverse, not just
the scalar identities.

## 4. The quadratic cover vanishes and the linear slope is lambda t

If \(a\ne0\), the first equation of (13) gives \(a^2d\in\mathbb C^*\).
At a place of \(K\) above a root \(\xi\) of \(1-t^4\), put
\(e=\operatorname{ord}(t-\xi)\). Then \(e\) is positive and even,
\(a\) has leading exponent \(-1/2\) in \(t-\xi\), and
\(\gamma=a'''/(18d)\) has order \(-9e/2\le-9\).
All terms in (11) other than \(W_0\) have \(n\)-degree at most two.
Thus after shifting \(n=z-Qy^2-k'y\), \(w\) is cubic in \(z\) with
coefficient \(\gamma\) on \(z^3\).

On the coefficient curve, adjoining independent \(y,z\) does not allow
leading coefficient poles to cancel in a polynomial in \(z\). At such
a place the valuation of that polynomial is the minimum of the
coefficient valuations, because its nonzero leading residues form a
nonzero polynomial in the independent \(z\). The pole degree of \(w\)
is therefore at least nine. Its map degree over \(\mathbb C(y,z)\)
cannot equal one, contrary to (14).
This is exactly the second lemma and conditional consequence in
[split coefficient191](weight-four-split-coefficient-ode-lemmas-pass191-working.md),
whose projective-curve and pole-degree inputs are stated there.
We have now supplied its actual-field hypotheses. Hence \(a=0\).

Consequently \(\rho=bn+c\), \(b\in K^*\), \(\mu=0\), and
\(M=M_1n+M_0\). The \(U^4\) equation in (12) is

\[
10db''+5d'b'+d''b=0.
\tag{15}
\]

The first lemma of split coefficient191 applies over this exact finite
field \(K/\mathbb C(t)\), and gives

\[
b=\lambda t,\qquad \lambda\in\mathbb C^*.
\tag{16}
\]

Its exclusion of other algebraic solutions is important here. Briefly,
writing \(b=tf\) gives \(dt f''=2f'\), so a nonzero \(j=f'\)
would satisfy \(j^2(1-t^4)\in\mathbb C^*\). After adjoining
\(v^2=1-t^4\), this makes \(df\) a nonzero constant multiple of
\(dt/v\). The latter is regular everywhere on the smooth projective
curve and remains regular and nonzero under a finite separable pullback.
A differential of a rational function cannot be nonzero and everywhere
regular: a pole differentiates to a pole, and a function with no poles
on the projective curve is constant. Thus \(j=0\).
In particular (16) is not an unsupported rational-function solution
ansatz, and it does not say that \(b\) is constant.

## 5. Residual scalar identities and the exact linear pencil

With (16), the possibly nonzero coefficients in (11) are

\[
\begin{aligned}
\mathcal W_4&=-\lambda d-\lambda t d'/4=\lambda,\\
\mathcal W_3&=-\lambda h-\lambda t h'/3-dM_1,\\
\mathcal W_2&=c''/2-hM_1,\\
\mathcal W_1&=M_1'n+M_0',\qquad \mathcal W_0=W_0.
\end{aligned}
\tag{17}
\]

The coefficients \(U^3,U^2,U\) of (12) give

\[
\begin{gathered}
\lambda t h''+4\lambda h'+3d'M_1+12dM_1'=0,\\
(W_0)_n=D:=\frac{c'''}{6d}-\frac{h'M_1}{3d}
                         -\frac{hM_1'}d\in K,\\
0=M_1''n+M_0''-2hD.
\end{gathered}
\tag{18}
\]

Transcendence of \(n\) and the exact constants now prove

\[
M_1=\alpha t+\beta,\quad \alpha,\beta\in\mathbb C,
\qquad W_0=Dn+g_0,\quad g_0\in K,\quad
M_0''=2hD,\quad \delta\mathcal W=D'n+g_0'\ne0.
\tag{19}
\]

No conclusion \(D'=0\) follows from scalarity in \(U\) alone.
To obtain it, shift \(n=z-Qy^2-k'y\) and set

\[
\begin{gathered}
w=(\alpha y+D)z+G(y)+g_0,\qquad
G(U)=\lambda U^4+g_3U^3+g_2U^2+g_1U,\\
g_3=\mathcal W_3-\alpha Q,\qquad
g_2=c''/2-hM_1-\alpha k'-QD,\qquad
g_1=M_0'-k'D,\\
g_3'=0,\qquad g_2'=-QD',\qquad g_1'=-k'D'.
\end{gathered}
\tag{20}
\]

For example \(\mathcal W_3'=3d\alpha=\alpha Q'\).
The terms in \(g_2'\) besides \(-QD'\) are
\(c'''/2-h'M_1-3h\alpha-3dD=0\); those in \(g_1'\)
besides \(-k'D'\) are \(M_0''-2hD=0\).

We use the exact linear-pencil lemma proved in Section 3 of
[zero-R field190](weight-four-absent-zero-r-field-normal-form-pass190-working.md).
If \(H/F_0\) is a one-variable function field, \(z\) is independent,
\(D\in H\) is transcendental over \(F_0\), and
\(H(z)=F_0(z,Dz+v_0)\), then \(v_0\in F_0+F_0D\).
Its algebraic proof first gives \(H=F_0(D,v_0)\) by intersection.
An irreducible relation \(\mathcal R(S,T)\) for \(D,v_0\), of total
degree \(j\), becomes \(\mathcal R(S,W-zS)\). It is irreducible,
of \(S\)-degree exactly \(j\), since its leading coefficient is
\(\mathcal R_j(1,-z)\ne0\). Gauss's lemma makes the field degree
equal to \(j\). Exact field equality forces \(j=1\), which proves
the assertion. No algebraically closed assumption on \(F_0\) is used.

If \(D\notin\mathbb C\), apply this with
\(F_0=\mathbb C(y)\), \(H=K(y)\), and
\(v_0=G(y)+g_0\). Indeed (14) and \(\alpha\in\mathbb C\) give
\(H(z)=F_0(z,w-\alpha yz)\), and \(D\) is transcendental over \(F_0\).
Thus \(v_0\in\mathbb C(y)+\mathbb C(y)D\).
Each coefficient of the polynomial \(v_0\in K[y]\) lies in
\(\mathbb C+\mathbb CD\): clear a common denominator in \(\mathbb C[y]\),
then compare components in a complex basis of the finite span of the
coefficients and \(1,D\). In particular \(g_2=c_2+e_2D\) for complex
\(c_2,e_2\). Since \(D'\ne0\), (20) would force \(e_2=-Q\),
contrary to \(Q'=3d\ne0\). Therefore

\[
D,g_1,g_2,g_3\in\mathbb C,\qquad G\in\mathbb C[U],
\qquad g_0'\ne0,\qquad K=\mathbb C(g_0).
\tag{21}
\]

For the final equality, (20) gives
\(\mathbb C[y,z,w]=\mathbb C[y,z,g_0]\), whose inverse is
\(w=(\alpha y+D)z+G(y)+g_0\). Intersect its field equality with \(K\)
using independence of \(y,z\) over \(K\). This is still a projected-ring
statement, not yet an original coordinate.

## 6. Polynomial coefficient transport and the actual coordinate

The original entries, now in \(K[n,y,X]\), are

\[
\begin{aligned}
Y&=y+tX,\\
Z&=n+Qy^2+k'y+(q'y+k)X+qX^2,\\
W&=\mathcal W(y)+P(y)X+(\lambda t n+c)X^2,\\
P(U)&=(\lambda n+c')U-\lambda t F(U)
                         +(\alpha t+\beta)n+M_0.
\end{aligned}
\tag{22}
\]

The coefficient of \(n\) in \(Z\) is one. That in \(W\) is

\[
\alpha y+D+(\lambda y+\alpha t+\beta)X+\lambda tX^2
 =A_0(X,Y):=\lambda XY+\beta X+\alpha Y+D
 \in\mathbb C[X,Y].
\tag{23}
\]

Consequently \(I_*:=W-A_0Z\in B\), and
\(I_*-g_0\in K[X,y]\); all \(n\)-dependence has canceled in the
polynomial ring, not merely in its fraction field.

On \(K(n,y,X)\) consider the exact derivation

\[
\mathscr T=\nabla-X\partial_y-F_U(y)\partial_n.
\tag{24}
\]

It kills \(X,Y,Z\). For \(Z\), direct differentiation gives
\(-F_U(y)+Q'y^2+k''y=0\), since \(Q'=3d\) and \(k''=2h\).
Also \(\delta\rho=\rho'-\eta F_U=P_U\). Using (8), (10), and
(19), differentiation of the literal \(W\) in (22) gives

\[
\mathscr T W
 =\delta\mathcal W(y)
   +X(\delta P-\mathcal W_U)(y)
   +X^2(\delta\rho-P_U)(y)=g_0'.
\tag{25}
\]

Because \(A_0\in\mathbb C[X,Y]\), it is also killed by
\(\mathscr T\). Hence \(I_*-g_0\in K[X,y]\) is killed by
\(\nabla-X\partial_y\). Substitute \(y=Y-tX\). This is a polynomial
change over \(K\), and that derivation becomes coefficient
differentiation fixing \(X,Y\). Every coefficient of the resulting
polynomial is therefore in the constant field \(\mathbb C\).
There is a polynomial \(Q_0(X,Y)\in\mathbb C[X,Y]\) such that

\[
I:=W-A_0(X,Y)Z-Q_0(X,Y)=g_0\in L\subset\operatorname{Frac}\mathcal A.
\tag{26}
\]

The left side belongs to the original \(B\). Since \(E\) kills the
right side, \(I\in\mathcal A\). Moreover this is an actual polynomial
coordinate: the map fixing \(X,Y,Z\) and replacing \(W\) by \(I\)
has the polynomial inverse

\[
W=I+A_0(X,Y)Z+Q_0(X,Y).
\tag{27}
\]

Substitution in either order cancels exactly the same two summands;
both inverse compositions are the identity. No coefficient from \(K\)
or denominator occurs in this inverse.

## 7. Restricted recognition and scope

The global slice identifies \(\mathcal A\) with \(B/(u)\). Since
\(Eu=1\), the original partial derivatives of \(u\) generate the unit
ideal, so this hypersurface ring is regular. Equation (27) identifies
\(B=\mathbb C[I,X,Y,Z]\), and \(E\) is a nonzero
\(\mathbb C[I]\)-linear LND on this ring. The exact regular-kernel
statement of
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore gives

\[
\mathcal A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.
\tag{28}
\]

The theorem statement and its short proof were freshly checked; this
retains that published theorem as an input, not a recursive audit of
all its dependencies. The actual slice and original-coordinate inverse
above verify its hypotheses here.

Thus the supplied full split-quartic frame with \(k_\rho=0\) is recognized.
Constant projected \(y\) has been excluded; the remaining graph has an
actual invariant coordinate. The factor \(Ny=\Gamma\) was retained
throughout, and neither \(K=\mathbb C(t)\), a global unit speed, nor a
polynomial generic reparameterization of the original ring was assumed.
The coefficient lemmas191 now have their actual zero-R hypotheses,
but their conclusions have not been extrapolated to nonzero \(R\).

No claim is made for the nonzero-R split branch, arbitrary coordinate
entry, other unresolved normal forms, or unrestricted cancellation.
This is a working proof, not human expert or proof-assistant
certification or a historical novelty claim. No checker was executed,
imported, or compiled, and no190 or earlier source was changed.
