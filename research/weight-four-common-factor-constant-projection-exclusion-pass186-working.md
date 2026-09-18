# Constant projection is impossible for the common-factor quartic

**Status: working exclusion under the supplied actual full initial kernel.**

In an actual sliced frame of time degrees \((1,1,2,2)\) with full
weighted initial relation \(X^2Z+XYW-Y^4\), the selected projected
\(y\) cannot lie in the coefficient field \(L\). The added quartic
term changes the literal determinant but not the coefficients that
force a commuting polynomial derivation. Wang's two-coordinate
theorem then supplies an invariant whose time-leading coefficient
cannot vanish.

This is an exclusion of the constant-projection branch. It does not
assume the whole-plane theorem, a unit selected cofactor, a rational
coefficient field, or recognition of any remaining graph branch.

## 1. Actual hypotheses and the projected parameter

Retain the actual setup of
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\tau,b\tau,e\tau^2,h\tau^2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\end{gathered}
\tag{1}
\]
The four displayed generators are original polynomial coordinates,
and the displayed ideal is the entire weighted initial kernel.
The auxiliary \(\tau\) is the initial-form variable, not the ratio
\(t\) below.

The occurring \(Z\)-pivot and the retained exact-shift result give
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad N\in\operatorname{LND}(A),\\
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad a\in L^*,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2=-t\rho+t^4,\qquad
[L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{2}
\]
In particular \(t,\rho\) are algebraically independent. The
coefficient partials on \(\mathbb C(t,\rho)\) extend uniquely and
commute on \(L\), and initially fix \(v\).

The actual chart, its first identities, and its calibration are
\[
\begin{gathered}
Y=y+tX,\qquad Z=z+\sigma X+(-t\rho+t^4)X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
\sigma=(-\rho+4t^3)y-t\vartheta+k,\\
z=-tw+6t^2y^2+k_t^{\rm old}y+
                    (k_\rho^{\rm old}-y)\vartheta+n,\qquad k,n\in L,\\
y,z,w,\sigma,\vartheta\in L[v],\quad L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a^3\in L^* .
\end{gathered}
\tag{3}
\]
The determinant holds \(X\) fixed. On this actual localized chart,
\(E=a\partial_X\), fixing \(L[v]\).

Suppose \(y\in L\). Then \(y_\rho^{\rm old}\ne0\). Otherwise
the first row of the determinant in (3) is
\((X+y_t^{\rm old},0,0)\), so the nonzero scalar determinant has
a positive-degree polynomial factor in \(X\). This is impossible.
It follows by separability that \(y\) is transcendental over
\(\mathbb C(t)\), and hence
\[
t,y\text{ are algebraically independent},\qquad
[L:\mathbb C(t,y)]<\infty .
\tag{4}
\]
The last extension is finite because \(L\) is finitely generated
of transcendence degree two.

Section 5 of universal-chart184 applies to \(q=-t\rho+t^4\) and gives
\(R=k_\rho^{\rm old}-y\ne0\). In the present branch \(R\in L^*\).
The first potential is
\[
Rw+4ty^3+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)=\ell,\qquad \ell\in L,
\tag{5}
\]
where
\(H_j(c;U,V)=\sum_{i=0}^j c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\)
uses the old coefficient partials. At fixed \(y\in L\), (5)
makes \(w\) polynomial in \(\vartheta\) of degree at most two.
Equation (3) does the same for \(z\). Since \(\vartheta\in L[v]\)
and \(L[y,z,w]=L[v]\), this proves
\[
L[\vartheta]=L[v],\qquad
w=\alpha\vartheta^2+\beta\vartheta+g,\quad \alpha,\beta,g\in L,\qquad
\vartheta_v\in L^* .
\tag{6}
\]
Thus \(\vartheta\) is a whole-line affine parameter, not an assumed
original coordinate.

## 2. The new quartic term in the determinant

Use the commuting partials \(t,y\) on the finite separable extension
in (4), and extend them to fix \(\vartheta,X\).
Their joint constant field is \(\mathbb C\): differentiating the
monic minimal polynomial of a joint constant over \(\mathbb C(t,y)\)
forces every coefficient derivative to vanish by minimality.
Those coefficients lie in \(\mathbb C\), and algebraic closedness
then gives the assertion.

The exact change-of-parameter determinant is
\[
\det\frac{\partial(t,y,\vartheta)}{\partial(t,\rho,v)}
 =y_\rho^{\rm old}\vartheta_v\in L^*.
\tag{7}
\]
Consequently the determinant in the new parameters is still in
\(L^*\), independent of both \(X\) and \(\vartheta\). Its value
need not be an original-ring unit.

Define elements of \(L\) using the old partials:
\[
r=k_\rho^{\rm old},\quad R=r-y,\quad
A_0=6t^2y^2+k_t^{\rm old}y+n,\quad
K_0=k+(-\rho+4t^3)y.
\]
The literal chart identity is
\[
Z+tW=R\vartheta+A_0+K_0X+t^4X^2 .
\tag{8}
\]
From now on all \(t,y\) subscripts refer to the new partials.
Adding \(t\) times the last row to the middle row in the
Jacobian yields
\[
\begin{pmatrix}
X&1&0\\
R_t\vartheta+A_{0,t}-w+(K_{0,t}-\vartheta)X+(4t^3-\rho)X^2&
R_y\vartheta+A_{0,y}+K_{0,y}X&R\\
w_t+\rho_tX^2&w_y+\rho_yX^2&w_\vartheta+X
\end{pmatrix}.
\tag{9}
\]
Both \(-W\,dt\) from \(dZ+t\,dW=d(Z+tW)-W\,dt\) and
\(4t^3X^2dt\) from the last term of (8) have been included.

Direct expansion gives the following identity in \(L[X,\vartheta]\):
\[
\begin{aligned}
\mathcal J={}&(2\alpha\vartheta+\beta+X)
 \{\alpha\vartheta^2+(\beta-R_t)\vartheta+g-A_{0,t}\\
&\qquad+X[(R_y+1)\vartheta+A_{0,y}-K_{0,t}]
       +X^2(K_{0,y}+\rho-4t^3)\}\\
&+R(w_t-Xw_y+\rho_tX^2-\rho_yX^3)\in L^* .
\end{aligned}
\tag{10}
\]
In particular the \(X^2\) bracket is not the split-chart bracket.
The extra term is independent of \(\vartheta\), which is the
specific reason the following coefficient argument still works.

## 3. Coefficient rigidity over the exact field

The coefficient of \(\vartheta^3\) at \(X=0\) in (10) is
\(2\alpha^2\), so \(\alpha=0\). Its partials consequently vanish.
The coefficients of \(X^2\vartheta\), \(X\vartheta\), and
\(\vartheta\) at \(X=0\), in that order, give
\[
R_y=-1,\qquad \beta-R_t-R\beta_y=0,\qquad
\beta^2-\beta R_t+R\beta_t=0.
\tag{11}
\]
Since \(R\ne0\), the last two imply
\(\beta_t+\beta\beta_y=0\).

Put \(\mathcal K=\ker_L\partial_y\). Commutativity makes it
stable under \(\partial_t\). Since \(R=r-y\), the first
identity in (11) gives \(r\in\mathcal K\). The second gives
\(\partial_y(R\beta)=-r_t\), whence, by subtracting the explicit
primitive \(r_tR\),
\[
\beta=r_t+\frac dR,\quad d\in\mathcal K,\qquad
0=\beta_t+\beta\beta_y
  =r_{tt}+\frac{d_t}{R}+\frac{d^2}{R^3}.
\tag{12}
\]
No arbitrary antiderivative in \(\mathcal K\) is assumed.

The element \(R\) is transcendental over \(\mathcal K\).
Indeed separability of a hypothetical algebraic equation over
that field, differentiated in \(y\), would force \(R_y=0\).
Multiplication of (12) by \(R^3\) and coefficient comparison
therefore yield \(d=0\) and \(r_{tt}=0\).
Using the joint constant field from Section 2 gives
\[
r=\mu t+\nu,\quad R=\mu t+\nu-y,\quad
\beta=\mu,\quad w=\mu\vartheta+g,\qquad \mu,\nu\in\mathbb C.
\tag{13}
\]
This includes \(\mu=0\) and the case \(w\in L\).

## 4. Return to a commuting derivation on the original ring

On the chart take \(T_0=\partial_\vartheta\), fixing \(L,X\).
Equations (8) and (13) give
\[
T_0X=T_0Y=0,\qquad
T_0Z=R-t(\mu+X)=\nu-Y,\qquad T_0W=X+\mu .
\tag{14}
\]
It therefore restricts to the actual polynomial locally nilpotent
derivation
\[
T_0=(\nu-Y)\partial_Z+(X+\mu)\partial_W,\qquad [E,T_0]=0.
\tag{15}
\]
Local nilpotence holds because \(T_0\) fixes its coefficients.
Commutation follows on the chart from \(E=a\partial_X\), \(a\in L\),
then holds on the original domain. This derivation is not asserted
to be a coordinate partial.

Let \(p=X+\mu\), \(q_0=\nu-Y\), and
\[
F=pZ-q_0W=(X+\mu)Z+(Y-\nu)W,\qquad
\ker_B T_0=\mathbb C[p,q_0,F]=\mathbb C[X,Y,F].
\tag{16}
\]
For the unlocalized kernel assertion, \(p,q_0,F\) are algebraically
independent and, after inverting \(p\), one has
\(B_p=\mathbb C[p,q_0,F]_p[W]\) and \(T_0=p\partial_W\).
Modulo \(p\), the map
\(\mathbb C[q_0,F]\longrightarrow\mathbb C[q_0,Z,W]\),
\(F\mapsto-q_0W\), is injective by coefficient comparison.
Thus \(pB\cap\mathbb C[p,q_0,F]=p\mathbb C[p,q_0,F]\).
A least-denominator-power argument removes \(p\) from any element
of the localized kernel and proves (16).

Consequently \(E\) restricts to a nonzero LND \(D\) on the actual
polynomial three-ring \(C=\mathbb C[X,Y,F]\), with
\(DX=a\ne0\) and \(D^2X=D^2Y=0\).
Divide its coefficient gcd \(\delta\) to write \(D=\delta D_0\).
The gcd is invariant: \(D\delta=\delta D_0\delta\ne0\) would
contradict the additivity of LND degree on products and its decrease
by one on differentiation. Hence \(D\delta=D_0\delta=0\), and
\[
D^j f=\delta^jD_0^j f,\qquad
D_0\in\operatorname{LND}(C)\setminus\{0\},\quad
D_0\text{ is irreducible},\quad
D_0^2X=D_0^2Y=0,\quad \ker D_0=\ker D.
\tag{17}
\]

## 5. Wang's alternatives contradict the quartic leading relation

Apply Wang's theorem in the form of Dasgupta--Gupta Theorem 4.1
to \(D_0\) on \(C=\mathbb C[X,Y,F]\).
Its first alternative gives an invariant nonzero complex linear
form in \(X,Y\). Differentiating that form by \(E\) and dividing
by \(a\) would give a nontrivial complex linear equation for
the transcendental \(t=b/a\), which is impossible.

Its second alternative gives \(\xi\in\ker D_0\) such that
\(C=\mathbb C[X,Y,\xi]\). The two polynomial presentations over
\(\mathbb C[X,Y]\) are inverse one-variable maps. Their degrees
multiply to one and their leading coefficients are units.
It follows that
\[
\xi=cF+Q(X,Y),\qquad c\in\mathbb C^*,\quad
Q\in\mathbb C[X,Y],\qquad E\xi=0.
\tag{18}
\]
No claim that \(F\) or \(\xi\) is an ambient fourfold coordinate
is used here.

The supplied leading relation in (1) and (2) gives
\[
\deg_E F=3,\qquad [u^3]F=ae+bh
 =a^3(q+t\rho)=a^3t^4\ne0 .
\tag{19}
\]
For any nonconstant \(Q\) of ordinary degree \(j\), its top
homogeneous part \(Q_j\) has
\([u^j]Q(X,Y)=Q_j(a,b)=a^jQ_j(1,t)\ne0\).
The last inequality follows from the transcendence of \(t\)
over \(\mathbb C\). Thus \(\deg_E Q(X,Y)=j\).

Invariance in (18) first forces \(Q\) to have ordinary degree
three. Its time-leading coefficient would then require
\[
c\,t^4+Q_3(1,t)=0 .
\tag{20}
\]
The second term has degree at most three in \(t\), while \(c\ne0\).
This contradicts transcendence. Both alternatives of Wang's
theorem are excluded, so the assumed constant projection is impossible:
\[
\boxed{\,y\notin L\,}.
\tag{21}
\]

## Sources and exact scope

The actual chart, scalar calibration and nonzero-\(R\) lemma are
retained from universal-chart184. The determinant mechanism was
compared with
[the unified split exclusion176](split-constant-projection-exclusion-pass176-working.md),
but (8)--(10) above include the additional quartic term explicitly.
The split-cubic initial relation is not assumed at any point.
The common-factor selected-component184 and high-graph185 notes
were read for context, but their whole-plane, unit-cofactor and
recognition conclusions are not inputs to this exclusion.

The external classification used in Section 5 was freshly checked
in N. Dasgupta and N. Gupta,
[Nice derivations over principal ideal domains](https://arxiv.org/pdf/1701.03635v1),
Theorem 4.1, printed page 9. Its hypotheses and both alternatives
are the ones used above. This retains that theorem as an external
input, not a recursive verification of Wang's original proof.

The conclusion only excludes \(y\in L\) for the supplied actual
full initial relation \(X^2Z+XYW-Y^4\). It does not independently
classify the nonconstant projection, recognize all its graph
branches, treat other quartic forms or height-two initial kernels,
or place arbitrary sliced actions into the given time profile.
No unrestricted cancellation claim follows from this note alone.

No tests were executed, imported or compiled during this derivation,
and no185 or earlier file was changed. Written arguments and
independent AI reviews are not human expert certification or
proof-assistant verification. No historical novelty, external contact,
publication or submission claim is made.

