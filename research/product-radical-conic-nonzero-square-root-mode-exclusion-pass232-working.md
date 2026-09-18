# Product-radical conic: exclusion of the nonzero square-root mode

This is a bounded actual-frame exclusion, not a construction or a general
cancellation theorem. In the conic left by pass227, the branch with a nonzero
cubic projected \(w\) has a precise algebraic square-root mode. The nonzero
mode is impossible: three coefficients of the complete calibrated Jacobian
put the return root at the conic vertex, contradicting pass231. The zero mode
is carried by an actual interchange of \(X,Y\) to the separate branch in
which \(w\) has degree at most two. That remaining branch is not excluded here.

## 1. Actual hypotheses and exact differential field

Assume the actual hypotheses of the universal pass184 chart and the supplied
full initial kernel used in pass227:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl(\mathbb C[X,Y,Z,W]\longrightarrow A[T]\bigr)
=(Z^2-XYW),\\
(X,Y,Z,W)\longmapsto(aT,bT,e_0T^2,h_0T^2).
\end{gathered}                                                    \tag{1}
\]
In the last two lines the displayed homomorphism is the initial map, not the
identity map on the original polynomial ring.

The actual selected \(N=[u^3]\partial_Z|_A\) gives the exact chart
\[
\begin{gathered}
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2,\quad q^2=t\rho,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad W=w+\theta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a^3\in L^* .
\end{gathered}                                                    \tag{2}
\]
Here \(t,\rho\) are algebraically independent and \(L/\mathbb C(t,\rho)\)
is finite. The determinant keeps \(X\) fixed. These are actual chart and
whole-line return statements, not consequences of a formal leading relation.

Work in the nonzero-return conic remaining in
[pass227](rank-one-product-radical-sextic-pruning-pass227-working.md). Put
\[
s=q/t,\qquad \rho=s^2t,\qquad q=st,\qquad
\xi=\rho y-t\theta,\qquad \deg_v\xi=1,\quad\deg_vy=2 .
\tag{3}
\]
Thus \(L/\mathbb C(t,s)\) is finite, and \(\xi_v\in L^*\). From now on
subscripts \(t,s\) mean differentiation in these new exact coefficient
coordinates. In particular the old derivatives are
\(\partial_t^{\rm old}=\partial_t-s\partial_s/(2t)\) and
\(\partial_\rho^{\rm old}=\partial_s/(2st)\). Their extensions to \(L\)
are unique and commute. An element killed by the new \(\partial_t\) is
not presumed rational in \(s\), much less complex.

The full first and second potentials, expressed in these coordinates, give
\[
\begin{aligned}
Y={}&y+tX,\\
W={}&w+(s^2y-\xi/t)X+s^2tX^2,\\
Z={}&\frac{w}{2s}+k_ty-\frac{\xi^2}{8s^3t^3}
       -\frac{k_s\xi}{2st^2}+n
       +\left(sy-\frac{\xi}{2st}+k\right)X+stX^2,\\
R={}&\frac{\xi+2s^2t k_s}{4s^3t^2},\qquad
J_{\xi}:=\det\frac{\partial(Y,Z,W)}{\partial(t,s,\xi)}
       =-\frac{2st\,a^3}{\xi_v}\in L^* .
\end{aligned}                                                     \tag{4}
\]
The Jacobian equality uses the full determinant in (2), not just its
specialization at \(X=0\). Its value is independent of \(X,\xi\).

## 2. The complete leading-mode reduction

The third potential has numerator of degree at most four in the affine
parameter \(\xi\), and its coefficient of \(w\) is the linear polynomial
\(R\). Hence \(\deg_\xi w\leq3\). Write
\[
y=A_*\xi^2+A_1\xi+A_0,\qquad
w=D_*\xi^3+D_2\xi^2+D_1\xi+D_0,\qquad A_*\ne0 .
\tag{5}
\]
All coefficients belong to \(L\). In this section and the main exclusion
assume \(D_*\ne0\).

The coefficient of \(\xi^4\) in the third potential is
\[
\frac{D_*}{4s^3t^2}+\frac{A_*}{8s^3t^4}
 +\frac{A_*^2 k_{tt}}2=0,
\qquad
D_*=-\frac{A_*}{2t^2}-2s^3t^2A_*^2 k_{tt}.
\tag{6}
\]
For direct verification of this coefficient, its homogeneous cubic
\(q\)-part is
\(y\xi^2/(8s^3t^4)-\xi^3/(16s^5t^5)\), and the highest radial quadratic
\(k\)-part is \(k_{tt}y^2/2\).

Differentiating the literal map (4), retaining all lower coefficients,
gives the following two coefficients of its complete determinant:
\[
\begin{aligned}
[\xi^7]J_\xi
 &={D_*(2A_*D_{*,t}-3D_*A_{*,t})\over2s^2},\\
[X\xi^5]J_\xi
 &={1\over2s^2t^4}\bigl(
 8s^3t^4A_*^3k_{tt}-3t^4D_*^2-2t^3A_*D_{*,t}
 +4t^3D_*A_{*,t}\\
 &\hspace{37mm}+2t^2A_*D_*+tA_*A_{*,t}+3A_*^2\bigr).
\end{aligned}                                                     \tag{7}
\]
Both vanish by scalar calibration. Substituting (6) and then the first
equation of (7) into the second yields
\[
(t^2D_*+A_*)(tA_{*,t}-3t^2D_*+A_*)=0 .
\tag{8}
\]
This is a field product identity, so it gives the stated two alternatives
without an assumption about zeros of coefficient functions.

Define
\[
\alpha=\frac{A_*^3}{D_*^2},\qquad
\zeta=\frac{A_*}{D_*},\qquad \eta=\zeta+t^2 .
\tag{9}
\]
Equation (7) gives \(\alpha_t=0\) and
\(A_{*,t}/A_*=-2\zeta_t/\zeta\). If the first factor in (8) vanishes,
\(\zeta=-t^2\). Otherwise its second factor gives
\(2t\zeta_t-\zeta=-3t^2\). The first alternative satisfies the same
differential equation. Consequently
\[
2t\eta_t=\eta,\qquad
\gamma:=\eta^2/t,\quad\gamma_t=0,\qquad
A_*=\frac{\alpha}{(\eta-t^2)^2},\quad
D_*=\frac{\alpha}{(\eta-t^2)^3}.
\tag{10}
\]
Here \(\alpha\ne0\), and \(\zeta=\eta-t^2\ne0\) by (9). Substitution in
(6) and exact integration give
\[
k_{tt}=\frac{1-\gamma/t^3}{4s^3\alpha},\qquad
k=\frac{t^2-\gamma/t}{8s^3\alpha}+\beta t+\delta,\qquad
\alpha_t=\gamma_t=\beta_t=\delta_t=0 .
\tag{11}
\]
This integration is complete in the actual finite field: after subtracting
the displayed primitive, a function with second \(t\)-derivative zero
equals \(\beta t+\delta\), as follows by taking its first derivative and
then subtracting that derivative times \(t\). No rationality assertion
about the four integration coefficients is used.

For the remainder of the exclusion assume \(\eta\ne0\), equivalently
\(\gamma\ne0\). Then
\(\eta_t=\eta/(2t)\) and \(\eta_s=\eta\gamma_s/(2\gamma)\).

## 3. Exact-field centering and the full polynomial columns

Center the quadratic \(y\) only in the coefficient-field polynomial ring:
\[
\xi=\zeta x+H,\quad H=-A_1/(2A_*),\qquad
y=\alpha x^2+C,\quad
w=\alpha x^3+\mathcal E x^2+\mathcal F x+\mathcal G,\qquad
J:=\det\frac{\partial(Y,Z,W)}{\partial(t,s,x)}
=-\frac{2st\,a^3\zeta}{\xi_v}\in L^* .
\tag{12}
\]
Indeed \(A_*\zeta^2=D_*\zeta^3=\alpha\). The change of parameter in (12)
is not asserted to be an ambient polynomial automorphism. Its
\(t,s\)-dependent terms do not change the determinant except for its
factor \(\zeta\), by the full triangular chain rule.

For completeness, the entire actual map \(Q=(Y,Z,W)\), with \(X\) fixed,
is \(Q=\sum_{i=0}^3Q_i x^i\), where
\[
\begin{aligned}
Q_3={}&(0,\alpha/(2s),\alpha),\\
Q_2={}&\left(\alpha,\,
 \frac{\mathcal E}{2s}+\alpha k_t-\frac{\zeta^2}{8s^3t^3}
       +s\alpha X,\,
 \mathcal E+s^2\alpha X\right),\\
Q_1={}&\left(0,\,
 \frac{\mathcal F}{2s}-\frac{\zeta H}{4s^3t^3}
       -\frac{k_s\zeta}{2st^2}-\frac{\zeta X}{2st},\,
 \mathcal F-\frac{\zeta X}{t}\right),\\
Q_0={}&\left(C+tX,\,
 \frac{\mathcal G}{2s}+k_tC-\frac{H^2}{8s^3t^3}
       -\frac{k_sH}{2st^2}+n
       +\left(sC-\frac{H}{2st}+k\right)X+stX^2,\right.\\
 &\hspace{47mm}\left.
 \mathcal G+\left(s^2C-\frac{H}{t}\right)X+s^2tX^2\right).
\end{aligned}                                                     \tag{13}
\]
Thus all lower intercepts \(H,C,\mathcal E,\mathcal F,\mathcal G,n\)
are retained. For each \(r\), the explicit coefficient rule is
\[
[x^r]J=
\sum_{\substack{0\le i,j\le3,\ 1\le k\le3\\i+j+k-1=r}}
k\det\bigl((Q_i)_t,(Q_j)_s,Q_k\bigr).
\tag{14}
\]
The following identities can therefore be checked by these finite
three-column determinants and (10), rather than by a specialization of
the lower coefficients.

## 4. Three calibrated coefficients force the forbidden vertex

The first coefficient is
\[
[x^6]J=
\frac{\alpha(8st^2\alpha\mathcal E_t-t^2\alpha_s+\eta\alpha_s)}
     {8s^3t^2}.
\tag{15}
\]
For example, its nonzero column contributions reduce to
\(2\det((Q_2)_t,(Q_3)_s,Q_2)
+3\det((Q_2)_t,(Q_2)_s,Q_3)\).
Since (15) vanishes, its complete exact-field integral is
\[
\mathcal E=\frac{\alpha_s}{8s\alpha}
               \left(t+\frac{2\eta}{t}\right)+\varepsilon,
\qquad \varepsilon_t=0 .
\tag{16}
\]

Next, \([X^2x^2]J=3N_{22}/(8s^4t^3\alpha)\), with
\[
\begin{aligned}
N_{22}={}&8s^4t^4\alpha^2\beta_s+8s^4t\eta\alpha^2\delta_s
-4s^2t^4\mathcal E\alpha+4s^2t^2\eta\mathcal E\alpha
+4s^2\eta H\alpha^2\\
&-2st^5\alpha_s+st^3\eta\alpha_s+st^2\alpha\gamma_s
-st^2\gamma\alpha_s-2s\eta\alpha\gamma_s
+2s\eta\gamma\alpha_s-5t^5\alpha+5\eta\alpha\gamma .
\end{aligned}                                                     \tag{17}
\]
Its coefficient of \(H\) is nonzero. Substituting (16) and solving gives
\[
\begin{aligned}
H=-\frac1{8s^2\eta\alpha^2}\bigl(&
16s^4t^4\alpha^2\beta_s+16s^4t\eta\alpha^2\delta_s
-8s^2t^4\alpha\varepsilon+8s^2t^2\eta\alpha\varepsilon\\
&-5st^5\alpha_s+st^3\eta\alpha_s
+2st^2\alpha\gamma_s-4s\eta\alpha\gamma_s
+4s\eta\gamma\alpha_s-10t^5\alpha+10\eta\alpha\gamma
\bigr).
\end{aligned}                                                     \tag{18}
\]

Finally \([Xx^4]J=N_{14}/(8s^4t^4)\), where the uneliminated numerator is
\[
\begin{aligned}
N_{14}={}&24s^4t^4\alpha^2\beta_s+24s^4t\eta\alpha^2\delta_s
+8s^2t^5\alpha\mathcal E_t-12s^2t^4\mathcal E\alpha
-8s^2t^3\eta\alpha\mathcal E_t+4s^2t^2\eta\mathcal E\alpha\\
&-8s^2t\eta\alpha^2H_t+20s^2\eta H\alpha^2
-7st^5\alpha_s+4st^3\eta\alpha_s+2st^2\alpha\gamma_s
-2st^2\gamma\alpha_s\\
&-5s\eta\alpha\gamma_s+5s\eta\gamma\alpha_s
-15t^5\alpha+15\eta\alpha\gamma .
\end{aligned}                                                     \tag{19}
\]
Using (16), (18), and their full \(t\)-derivatives in (19) gives
\[
\begin{aligned}
[Xx^4]J=\frac5{16s^4t^4}\bigl\{&
t^4(16s^4\alpha^2\beta_s-8s^2\alpha\varepsilon)
-7t^5(s\alpha_s+2\alpha)\\
&+\eta(2s\alpha\gamma_s-2s\gamma\alpha_s-4\alpha\gamma)
\bigr\}.
\end{aligned}                                                     \tag{20}
\]
In particular \(H_t\) has not been set to zero when eliminating \(H\).

All three bracketed coefficients in (20) are killed by \(\partial_t\).
The nonzero functions \(t^4,t^5,\eta\) are eigenvectors of \(t\partial_t\)
with distinct eigenvalues \(4,5,1/2\). Applying the three Lagrange
projection polynomials in \(t\partial_t\) proves their independence over
the exact \(\partial_t\)-constant field. Hence scalar calibration forces
\[
\varepsilon=2s^2\alpha\beta_s,\qquad
s\alpha_s+2\alpha=0,\qquad \gamma_s=0 .
\tag{21}
\]
The last conclusion uses the second equality in the coefficient of
\(\eta\). It does not require these coefficient functions to have been
rational in \(s\).

Substituting (21) into (18) and using the explicit \(k\) in (11) yields
\[
H+2s^2t k_s=0,\qquad
R=\frac{\zeta x}{4s^3t^2},\qquad y_x=2\alpha x .
\tag{22}
\]
This is the decisive contradiction. The return polynomial has a simple
root at \(x=0\), which is also the critical point of \(y\).

More explicitly, the affine conic parameter in
[pass231](universal-simple-return-root-cofactor-bound-pass231-working.md)
is \(\chi=\theta-s^2y=-\xi/t\); its derivative with respect to \(x\) is
\(-\zeta/t\ne0\). Equation (22) therefore says that the quadratic
\(y=P(\chi)\) has \(P'(\chi_R)=0\) at the return root. Pass231, under the
same actual universal hypotheses and scalar calibration, proves
\(P'(\chi_R)\ne0\). This use is only an evaluation of polynomial identities
over \(L\). No differentiation of a moving root and no ambient
coefficient-field change is involved.

Thus \(D_*\ne0,\eta\ne0\) is impossible.

## 5. The zero mode is an actual reduction, not an exclusion

For \(\eta=0\), (10) gives \(A_*=\alpha/t^4\) and
\(D_*=-\alpha/t^6\). There is then an actual polynomial involution
\[
\begin{gathered}
(X^*,Y^*,Z^*,W^*)=(Y,X,Z,W),\\
t^*=1/t,\qquad s^*=s,\qquad
y^*=-y/t,\qquad \xi^*=\xi/t^3,\qquad
w^*=w+\xi y/t^2,\\
A_{2,*}=-t^5A_*,\qquad
D_{3,*}=t^7(t^2D_*+A_*)=0 .
\end{gathered}                                                     \tag{23}
\]
Both inverse orders are the identity because the original-coordinate
interchange is self-inverse. It preserves the full ideal
\((Z^2-XYW)\), the exact profile, and the literal selected partial
\(\partial_Z\); therefore \(N,L\) remain the same. Its displayed
coefficient formulas follow by solving the old \(Y=y+tX\) for \(X\)
and substituting in \(W\), not by treating the coefficient-field
centering (12) as an ambient operation. The new leading speed is
\(EX^*=b\ne0\), and the chart and scalar calibration are rebuilt.

If \(D_*=0\) from the outset, (6), (7) instead give
\(tA_{*,t}+A_*=0\), whence \(A_*=\alpha_0/t\) and
\(k=-1/(8s^3\alpha_0t)+\beta_0t+\delta_0\), with all three coefficients
killed by \(\partial_t\). These are necessary reductions only.
The present proof does not settle their remaining lower equations.

## 6. Verification and scope

The upstream coefficients were obtained from the literal map (4), with
arbitrary lower coefficients, and independently reconstructed before this
source was completed. The centered identities (15), (17), and (19) were
also reconstructed independently from the literal map, not by importing
their coefficient arrays. Reduction used \(\eta^2=\gamma t\), together
with its exact \(t,s\)-derivative rules. The antiderivative (16), the full
substitution (20), and the final offset (22) were separately checked.
These finite arithmetic checks support the displayed identities; the
exact-field integration, eigenvalue separation, actual swap, and pass231
geometric contradiction are written arguments above.

No saved checker was executed, imported, or compiled in preparing this
note. No previous proof or packet was changed. The conclusion is precisely
that every actual remaining conic can, after the optional actual swap
(23), be studied in the branch \(\deg_\xi w\le2\). It does not assert
existence, nonexistence, or coordinate recognition for that last branch.
