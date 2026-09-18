# Cubic exclusion and a degenerate conic endpoint in the paraboloid chart

In the actual nonlinear branch271 after280, a selected irreducible
plane component of degree three is impossible. If the whole-plane
polynomial has degree two and its \(U^2\) coefficient vanishes, an
explicit complex polynomial shear lowers the last actual coordinate
to time degree one. The retained exact1122 theorem then recognizes
the original kernel.

This is a bounded result. The degree-two selected component with a
nonzero \(U^2\) coefficient, and the degree-two selected component of
a degree-four whole-plane polynomial, are not settled here.

## 1. Retained actual entry and the complete polynomial

Retain the complete hypotheses and field construction of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and the nonlinear reduction
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md).
In particular,
\[
\begin{gathered}
B_{\rm amb}=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
\text{full weighted initial kernel }(X^2Z-Y^2),\qquad
\operatorname{shift}(\partial_Z)=4,\qquad k_s=0,\quad n_s\ne0,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\qquad
L[y,\sigma]=L[v],\qquad Nv=1,\\
F=\ker_L\partial_n,\qquad [F:\mathbb C(t)]<\infty,\qquad
[L:F(n)]<\infty,\qquad \ker_F\partial_t=\mathbb C.
\end{gathered}
\tag{1}
\]
These are exact fields obtained from the actual chart, not selected
finite extensions. The coefficient partials commute and initially
fix \(v\). The element \(n\) is transcendental over \(F\).

The conclusion of280 is
\[
H=hn+c,\qquad T=pn+q,\qquad
h\in\mathbb C^*,\quad c,k,p,q\in F.
\tag{2}
\]
Let \(G\in L[U,P]\) be the irreducible generator of the full
evaluation ideal of \((y,\sigma)\), and put \(g=\deg G\).
The retained whole-line and scalar gates give
\[
g=\max(\deg_v y,\deg_v\sigma),\qquad
G_g=\gamma\Lambda^g,\qquad
Q-q_0=\eta G+G^2R,\quad \gamma,\eta\in L^*,\quad q_0\in L.
\tag{3}
\]
Here \(\Lambda\) is a nonzero linear form. No irreducibility of
\(Q-q_0\) is assumed.

For clarity, the complete coefficient table used below is
\[
\begin{aligned}
Q={}&B U^2+(C_2P^2+C_1P+C_0)U
             +D_4P^4+D_3P^3+D_2P^2+D_1P,\\
B={}&hk''/2+p,& C_2={}&hk'''/2+2p',\\
C_1={}&pk''-c''+k'p'+2\omega_n,
&C_0={}&-np'+k'\omega_n-q',\\
D_4={}&hk''''/24,
&D_3={}&(pk'''-c'''+3k''p')/6,\\
D_2={}&-np''/2+k''\omega_n/2-q''/2,
&D_1={}&-\omega_t,\qquad \omega\in L.
\end{aligned}
\tag{4}
\]
The letter \(B\) in (4) is a coefficient in \(F\), not the ambient
ring \(B_{\rm amb}\). All coefficient derivatives in (4) are taken
before evaluating the formal variables.

The actual fixed-\(X\) map and scalar calibration remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k'\sigma+n+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+(hn+c)X^2,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}
  &=-a^4h\in L^*,\qquad a=EX.
\end{aligned}
\tag{5}
\]
The polynomial formulas for \(w,\theta\) are the literal potentials
of271, not freely chosen plane parametrizations.

## 2. A whole-line degree pair \((3,2)\) is impossible

We will use one elementary consequence of whole-line generation.
Suppose \(\deg_v\sigma=2\) and \(\deg_v y=3\). Translate the
polynomial parameter over \(L\) to write
\(\sigma=\alpha x^2+\beta\), with \(\alpha\in L^*\).
The unique even-odd decomposition is
\[
y=P_1(\sigma)+x B_1(x^2),\qquad \deg B_1=1.
\tag{6}
\]
The odd module of \(L[\sigma,y]\) is exactly
\(xB_1(x^2)L[x^2]\): its even generator gives all \(L[x^2]\),
and every product of two odd factors is even.
Equality \(L[\sigma,y]=L[x]\) would therefore force
\(B_1\) to be a unit of \(L[x^2]\), contradicting its degree.
This argument works over the exact field \(L\); it does not
require algebraic closure or an ambient coordinate change.

We also use the standard degree identity in this exact situation:
for nonconstant \(\sigma\),
\(\deg_U G=[L(v):L(\sigma)]=\deg_v\sigma\).
It follows by viewing the irreducible relation over \(L(P)\) and
using \(L(y,\sigma)=L(v)\), which is supplied by (1).

## 3. A selected cubic reduces to a canonical cubic graph

Assume \(g=3\). Since \(\deg Q\le4\), the term \(G^2R\) in (3)
must vanish. Thus \(Q-q_0=\eta G\) has degree exactly three.
Equation (4) gives \(k''''=0\), and its cubic top is
\[
Q_3=P^2(C_2U+D_3P).
\tag{7}
\]
The pure-cube condition from (3) forces \(C_2=0,D_3\ne0\).
In particular the top of \(G\) is proportional to \(P^3\).

If \(B\ne0\), the \(U\)-degree of \(G\) is two. Hence
\(\deg_v\sigma=2\), while \(\deg_v y=3\).
Section2 contradicts whole-line generation. Therefore \(B=0\).
The \(U\)-degree of \(G\) cannot be zero: a relation in
\(\sigma\) alone would make \(\sigma\) constant in \(L[v]\) and
give a linear full plane relation. It is therefore one, so
\(\sigma\) is affine and \(y\) is cubic in that parameter.
Combining \(B=0\) and \(C_2=0\) in (4) yields
\[
p=-hk''/2,\qquad k'''=0.
\tag{8}
\]
Exact integration in \(F\) gives
\(k=\kappa t^2/2+\alpha t+\beta\), with all three coefficients
complex.

Put \(d=\kappa/4\) and make the actual affine change proved in
[272](principal-paraboloid-high-derivative-line-normalization-pass272-working.md):
\[
X_*=X-d,\qquad Y_*=Y+\alpha X_*/2,\qquad
Z_*=Z-\beta X_*,\qquad W_*=W.
\tag{9}
\]
Its inverse is \(X=X_*+d,\ Y=Y_*-\alpha X_*/2,
Z=Z_*+\beta X_*,\ W=W_*\).
For arbitrary old \(y,\sigma\), its projected transformation is
\[
y_*=y+d\sigma+td^2,\quad
\sigma_*=\sigma+2dt+\alpha/2,\quad k_*=0,\quad
n_*=n-3d^2t^2-\alpha dt+\beta d-\alpha^2/4.
\tag{10}
\]
Thus the whole-line relation still has degree three, with
\(\sigma_*\) affine and \(y_*\) cubic in that parameter.
The literal selected partial, \(N,L,F\), leaders, full initial
kernel and actual return are preserved as proved in272.
The coefficient \(h\) remains the same complex constant, since
\(n_*-n\in\mathbb C[t]\). The coefficient partial in \(t\)
is rebuilt holding \(n_*,v\) fixed.

Rename this rebuilt chart. Reapply (3),(4), rather than assuming
that the old coefficient \(p\) is unchanged.
Now \(k=0\), so \(\deg Q\le3\), and the selected cubic gives
\(Q-q_0=\eta G\). Since \(\sigma\) is affine and \(y\) cubic,
the full relation is a graph \(U-P_3(P)\). Its \(U^2\) coefficient
vanishes and its \(U\) coefficient is a nonzero scalar in \(L\).
The complete table then gives
\[
p=0,\qquad \omega_n=c''/2,\qquad q'\ne0,\qquad c'''\ne0,
\qquad \omega=c''n/2+\omega_0,\quad \omega_0\in F.
\tag{11}
\]
For example, with \(k=p=0\), the \(UP\) coefficient is
\(2\omega_n-c''\), the \(U\) coefficient is \(-q'\),
and the cubic coefficient is \(-c'''/6\).

## 4. The canonical cubic graph contradicts the actual scalar

Its literal relation and projected coefficients are
\[
\begin{aligned}
Q&=-q'U-c'''P^3/6-q''P^2/2-(c'''n/2+\omega_0')P,\\
y&=-\frac{c'''}{6q'}\sigma^3-\frac{q''}{2q'}\sigma^2
       -\frac{c'''n/2+\omega_0'}{q'}\sigma+D,\qquad D=-q_0/q'\in L,\\
z&=2ty+\sigma^2+n,\\
w&=-hy^2+c'y+c''(\sigma^2+n)/2+q'\sigma+\omega_0.
\end{aligned}
\tag{12}
\]
No restriction on \(D_t,D_n\), or rationality of \(L\), is imposed.

Since \(\sigma\) is affine in \(v\), its derivative
\(\sigma_v\in L^*\). Changing only this polynomial-line parameter
in the \(X=0\) specialization of (5) gives
\[
J_\sigma:=\det\frac{\partial(y,z,w)}{\partial(t,n,\sigma)}
 =-\frac{a^4h}{\sigma_v}\in L^*.
\tag{13}
\]
Coefficient partials now hold \(\sigma\) fixed. The moving
parameter contributes precisely the factor \(\sigma_v\);
its other coefficient derivatives cancel in the determinant.

Set
\(\Psi=c'''(\sigma^2+n)/2+q''\sigma+\omega_0'\).
After row subtraction the exact determinant is
\[
J_\sigma=q'y_t-2q'y\,y_n+2\sigma\Psi\,y_n-\Psi y_\sigma
         =q'y_t-2q'y\,y_n+2\sigma\Psi\,y_n+\Psi^2/q'.
\tag{14}
\]
Here \(y_\sigma=-\Psi/q'\), directly from (12).
Also \(\deg_\sigma y_t\le3\) and
\(y_n=-c'''\sigma/(2q')+D_n\).
The respective degree-four contributions of the last three terms
of (14) are
\(- (c''')^2/(6q')\), \(- (c''')^2/(2q')\), and
\((c''')^2/(4q')\). Therefore
\[
[\sigma^4]J_\sigma=-\frac{5(c''')^2}{12q'}\ne0.
\tag{15}
\]
This contradicts (13). Every selected cubic in the supplied
nonlinear branch is therefore impossible.

## 5. A degree-two whole equation with B zero is recognized

Assume instead
\[
g=2,\qquad \deg Q=2,\qquad B=0.
\tag{16}
\]
The degree condition in (4) gives \(k''''=C_2=D_3=0\).
As in (8), \(B=C_2=0\) gives \(k'''=0\) and \(p=-hk''/2\).
Then \(D_3=0\) gives \(c'''=0\).
Thus \(k,c\) are complex quadratics and \(p\) is complex.

The top of \(Q\) has the form \(C_1UP+D_2P^2\).
Because \(Q-q_0=\eta G\) and its top is a pure square,
\(C_1=0,D_2\ne0\). Its \(U\) coefficient is nonzero:
otherwise a relation in \(\sigma\) alone would force
\(\sigma\in L\), and the full plane relation would be linear.
It follows that \(\sigma\) is affine and \(y\) is quadratic.

Make the same actual affine normalization (9),(10).
The new \(k\) is zero, \(c\) is still a complex quadratic,
and the selected relation is still a quadratic graph with pure
top \(P^2\). Reapplying (3),(4), the rebuilt \(Q\) cannot
have degree three: for \(g=2\), a nonzero square-cofactor term
has degree at least four, whereas a zero one makes its degree two.
Nor can it have degree four, since \(k=0\).
Thus its degree is two, and its graph form forces its new
\(U^2\) coefficient \(p\) to vanish.

Write the rebuilt complex quadratic as
\(c=c_2t^2/2+c_1t+c_0\).
The \(UP\) coefficient of the complete table now gives
\(\omega_n=c_2/2\). Consequently
\[
\omega=c_2n/2+\omega_0,\quad \omega_0\in F,\qquad
Q=-q'U-q''P^2/2-\omega_0'P,\qquad q'\ne0,\quad q''\ne0.
\tag{17}
\]
The nonzero coefficients follow from its genuine quadratic
graph form. In particular \(q\in F^*\).

Define in the actual rebuilt ring
\[
\boxed{\widetilde W=
W-h(X^2Z-Y^2)-\frac{c_2}{2}Z-c_1Y-c_0X^2.}
\tag{18}
\]
Every displayed coefficient is complex. The inverse fixes
\(X,Y,Z\) and adds the same polynomial to \(\widetilde W\).
Both substitution orders are the identity.

The literal potentials with \(k=p=0\), together with (17), give
\[
\begin{aligned}
\theta&=q+c'\sigma-2h\sigma y,\\
w&=-hy^2+c'y+c_2\sigma^2/2+q'\sigma+c_2n/2+\omega_0,\\
X^2Z-Y^2&=-y^2-2y\sigma X+nX^2,\\
\widetilde W&=\omega_0+q'\sigma+qX .
\end{aligned}
\tag{19}
\]
All coefficients of the last expression belong to \(K\), so
are killed by \(E\). Since \(q\ne0\) and \(EX=a\ne0\), the
actual coordinate \(\widetilde W\) has exact time degree one.
The actual frame \((X,\widetilde W,Y,Z)\) has exact degrees1122.
The retained working
[recognition theorem257](full-exact1122-recognition-synthesis-pass257-working.md)
therefore gives \(A\simeq\mathbb C^{[3]}\).
No condition on the new full initial ideal is added.

## 6. Exact scope and verification boundary

For a selected conic, (3) permits a whole equation of degree two
or four, but not degree three. Section5 treats only degree two
with \(B=0\). The degree-two case \(B\ne0\) and the degree-four
selected conic remain unresolved in this source.
No statement about genuine selected quartics is made here.

The complete saved271,272,280 and257 sources were read for
the retained hypotheses used above. The new scalar calculation
(14),(15) was independently rebuilt from the literal three
projected coordinates in unsaved exact algebra, keeping the
arbitrary coefficient \(D\) and both of its partial derivatives.
The degree-lowering identity (19) is a full original-coordinate
identity with an explicit monic inverse, not an intercept-only
claim or a declaration that \(\sigma\) is ambient.

No saved checker was executed, imported, compiled or rerun.
No earlier source or index was edited. This bounded note does
not establish all of271, every supplied1222 frame, or unrestricted
cancellation. It retains the working dependencies of257 and
makes no claim of recursive formal certification or historical
novelty.
