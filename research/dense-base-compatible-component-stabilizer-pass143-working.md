# Base-compatible components and the coefficient stabilizer

For an active first-tail component with no enlarged algebraic constant
field, two initial speed-ratio identities force the formal slice
derivation to agree with the transported normalized source action.
The proof compares the two calibrated Jacobians at the initial
hyperplane, then uses the actual source inverse and a finite-order
coefficient automorphism.

These components are in bijection with the automorphisms of the
coefficient field that fix the speed-ratio field and every peeling
coefficient, including the first evaluated negative coefficient.
This is a conditional reduction. Neither the constant-field premise
nor triviality of that stabilizer is established for every component.
No first-tail primitivity or cancellation theorem is claimed.

## 1. Exact actual-source and component premises

Use the actual dense chart139 and the component construction141.[^1]
In particular, the source has
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
s=EX\ne0,\qquad D=E/s,\\
F=\operatorname{Frac}A=\mathbb C(y,z,w_0)=L(v),\qquad
L[y,z]=L[v],\\
K=\mathbb C(\tau,\rho),\qquad L/K\text{ finite separable},\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
D=\partial_X\text{ on }F(X),\\
F(X)=\mathbb C(X,Y,Z,W),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}=1 .
\end{gathered}
\tag{1}
\]
Here \(E^2X=E^2Y=E^2Z=0\), and
\(\tau=EY/s,\ \rho=EZ/s\) are algebraically independent over
\(\mathbb C\), as supplied by the dense speed cone.
The determinant fixes \(X\); the coefficient partials fix \(v\).
Its normalization, including its value at \(X=0\), is the actual
selected-cofactor calibration. The field-generation equality is
supplied by the actual polynomial coordinates and inverse. It is not
an inference from the determinant.

Write \(H_d(f;U,V)\) for the homogeneous Taylor polynomial of order
\(d\) using the commuting partials on \(L/K\). The exact data are
\[
\begin{gathered}
f_0,\ldots,f_m,f_{-1}\in L,\qquad f_m\ne0,\qquad m\ge0,\\
\Omega=\sum_{j=0}^{m}H_j(f_j),\qquad w_0=\Omega(y,z),\\
\Phi=-\sum_{j=0}^{m}H_{j+1}(f_j)-f_{-1}\ne0,\qquad
\Psi=-\sum_{j=0}^{m}H_{j+2}(f_j)-H_1(f_{-1}),\\
\ker\bigl(L[U,V]\longrightarrow L[v]\bigr)=(g),\qquad
g\text{ irreducible},\quad g\mid\Phi,\quad
\Psi(y,z)=v+c,\quad c\in L .
\end{gathered}
\tag{2}
\]
Here \(U,V\) are independent variables, and all factors are taken
over exactly \(L\).

Let \(h\) be an irreducible factor of \(\Phi\). As in141, set
\[
\begin{gathered}
R_h=L[U,V]/(h),\qquad F_h=\operatorname{Frac}R_h,\qquad
y_h=\overline U,\quad z_h=\overline V,\\
v_h=\Psi(y_h,z_h),\qquad
w_{0h}=\Omega(y_h,z_h),\\
h\text{ active}:\quad v_h\text{ is transcendental over }L .
\end{gathered}
\tag{3}
\]
Activity supplies the three extended coefficient derivations, the
polynomial \(W_h(X)\), and the cofactor derivation \(T_h\), with
\[
Y_h=y_h+\tau X,\qquad Z_h=z_h+\rho X,\qquad
T_h(X,Y_h,Z_h,W_h)=(0,0,0,1).
\]
It also supplies the relative Jacobian one and, at \(X=0\), the
source-substitution embedding142:[^2]
\[
\begin{gathered}
\sigma_h:F=\mathbb C(y,z,w_0)\hookrightarrow F_h,\qquad
(y,z,w_0)\longmapsto(y_h,z_h,w_{0h}),\\
\det\frac{\partial(y_h,z_h,w_{0h})}
              {\partial(\tau,\rho,v_h)}=1 .
\end{gathered}
\tag{4}
\]
The values \(\sigma_h(\tau)\) and \(\sigma_h(\rho)\) mean rational
source substitution, not the preassigned coefficient values.

For the rest of the forward argument assume
\[
L\text{ is relatively algebraically closed in }F_h,\qquad
\sigma_h(\tau)=\tau,\qquad \sigma_h(\rho)=\rho .
\tag{5}
\]
The first assumption says that the algebraic constant field has not
enlarged. Equivalently, \(\ker(\partial_{v_h}:F_h\to F_h)=L\).
Indeed a constant transcendental over \(L\) would make \(F_h\)
algebraic over a field on which that derivation vanishes, contradicting
\(\partial_{v_h}v_h=1\). Conversely an element algebraic over \(L\)
is killed by that derivation in characteristic zero.

## 2. Coefficient automorphism and the initial calibration

The embedding \(\sigma_h\) fixes \(K\). Its image of any element of
\(L\) is algebraic over \(K\), hence algebraic over \(L\) inside \(F_h\).
By (5) it lies in \(L\). Since the image has the same finite degree
over \(K\), it equals \(L\). Consequently
\[
\begin{gathered}
\gamma:=\sigma_h|_L\in\operatorname{Aut}_K(L),\qquad
\gamma\text{ has finite order},\\
\sigma_h(F)=F_h,\qquad
\widetilde v=\sigma_h(v),\qquad
F_h=L(\widetilde v),\qquad R_h=L[\widetilde v].
\end{gathered}
\tag{6}
\]
For the last equality, transport \(L[y,z]=L[v]\) through
\(\sigma_h\), using \(\sigma_h(L)=L\).
The automorphism \(\gamma\) commutes with the two coefficient
partials on \(L\), by uniqueness of extension through a finite
separable field extension.

Transport the source coefficient partials to \(F_h\) using
\(\sigma_h\). They fix \(\widetilde v\) rather than \(v_h\).
Transporting the \(X=0\) instance of (1) gives
\[
\det\frac{\partial(y_h,z_h,w_{0h})}
              {\partial(\tau,\rho,\widetilde v)}=1 .
\]
This has exactly the same initial triple as (4).
The chain-rule determinant for changing
\((\tau,\rho,\widetilde v)\) to \((\tau,\rho,v_h)\) is
\(\partial_{v_h}\widetilde v\). Therefore
\[
\partial_{v_h}\widetilde v=1,\qquad
\widetilde v=v_h+c_h,\quad c_h\in L,\qquad
R_h=L[v_h].
\tag{7}
\]
In particular the unit slope is proved from the two initial
determinants. It is not assumed from activity or from the fact
that both elements are generic parameters.

## 3. Compare the last coordinate with the actual transported flow

Extend \(\sigma_h\) to \(F(X)\) by fixing \(X\), and let
\(W^*(X)=\sigma_h(W(X))\). The two initial speed identities in
(5) give the same transported goods \(Y_h,Z_h\).
The source polynomial formula and actual inverse give
\[
\begin{gathered}
W^*\in F_h[X],\qquad W^*(0)=w_{0h},\\
F_h(X)=\mathbb C(X,Y_h,Z_h,W^*),\\
W^*=\left(\sum_{j=0}^{m}X^j
                  \Theta_h(\gamma f_j)\right)_{\ge0},\qquad
W_h=\left(\sum_{j=0}^{m}X^j
                  \Theta_h(f_j)\right)_{\ge0}.
\end{gathered}
\tag{8}
\]
The Taylor identity uses the commutation of \(\gamma\) with the
coefficient partials, and the same \(y_h,z_h\) in each series.
No polynomial independence of coefficients in \(L\) is being assumed.

Transporting the whole determinant in (1) gives determinant one
with respect to \((\tau,\rho,\widetilde v)\). By (7), changing
to the component partials preserves that determinant. Thus the
same cross-product derivation \(T_h\) satisfies \(T_hW^*=1\).

On the generated field in (8), \(T_h\) is therefore the ordinary
last-coordinate partial. Its constant field is
\(\mathbb C(X,Y_h,Z_h)\). Since also \(T_hW_h=1\), the difference
\(Q=W_h-W^*\) belongs to this rational good-coordinate field.

If \(Q\ne0\), let \(j\) be the largest index with
\(f_j-\gamma f_j\ne0\). Formula (8) makes its leading \(X\)
coefficient exactly \(f_j-\gamma f_j\).
On the other hand, for any nonzero rational function
\(P(X,Y_h,Z_h)/R(X,Y_h,Z_h)\) with complex polynomial \(P,R\),
its leading \(X\) coefficient belongs to \(K\).
To see this, substitute
\(Y_h=y_h+\tau X,\ Z_h=z_h+\rho X\).
The leading terms are
\(P_d(1,\tau,\rho)X^d\) and \(R_e(1,\tau,\rho)X^e\).
They are nonzero because \(\tau,\rho\) are algebraically
independent, and their ratio belongs to \(K\).

It follows that \(f_j-\gamma f_j\in K\setminus\{0\}\).
If \(\gamma\) has order \(r\), summing its \(r\) translates gives
\[
0=f_j-\gamma^r f_j=r(f_j-\gamma f_j),
\]
which is impossible in characteristic zero. Hence
\[
W_h=W^*,\qquad
\gamma f_j=f_j\quad(0\le j\le m).
\tag{9}
\]
The argument includes \(m=0\), without division by a time degree.

The source identity \(g(y,z)=0\), transported through \(\sigma_h\),
shows that \(h\) is associated to \(\gamma g\). Thus \(h\) divides
both \(\Phi\) and \(\gamma\Phi\). By (9) their difference is the
scalar \(\gamma f_{-1}-f_{-1}\). A nonconstant polynomial cannot
divide a nonzero scalar, so \(\gamma f_{-1}=f_{-1}\).

## 4. Exact derivation comparison and finite stabilizer

For clarity, the transported source derivation refers to the
actual target-generator embedding
\[
\iota_h:\mathbb C(X,Y,Z,W)\hookrightarrow F_h(X),\qquad
(X,Y,Z,W)\longmapsto(X,Y_h,Z_h,W_h).
\]
For every active component this embedding exists by the relative
Jacobian. The field extension is finite separable, so its transported
\(E/s\) extends uniquely to \(F_h(X)\).
Under (5), equation (9) identifies \(\iota_h\) with the isomorphism
\(\sigma_h:F(X)\to F_h(X)\) fixing \(X\).
Since the source \(E/s\) fixes \(F\), its transport is exactly
\(\partial_X\) fixing \(F_h\).

Conversely, suppose the transported \(E/s\) equals this formal
\(\partial_X\). Its values on \(Y_h,Z_h\), specialized at \(X=0\),
give \(\sigma_h(\tau)=\tau\) and \(\sigma_h(\rho)=\rho\).
The specialization is legitimate: every nonzero rational source
denominator in the projected triple has nonzero image under (4).
Thus, among active components with algebraic constant field exactly
\(L\), the two initial speed identities are equivalent to equality
of the normalized derivations.

Define the finite group
\[
\mathcal G=
\left\{\gamma\in\operatorname{Aut}_K(L):
 \gamma f_j=f_j\ (0\le j\le m),\quad
 \gamma f_{-1}=f_{-1}\right\}.
\tag{10}
\]
There is a bijection from \(\mathcal G\) to the active components
satisfying (5), given by \(\gamma\mapsto\gamma g\), with factors
understood up to \(L^*\).
The forward construction above assigns such a component its
automorphism \(\sigma_h|_L\), and shows \(h\sim\gamma g\).

For the converse, take \(\gamma\in\mathcal G\).
It commutes with coefficient partials, so
\(\gamma\Omega=\Omega,\ \gamma\Phi=\Phi,\ \gamma\Psi=\Psi\).
The conjugate \(h=\gamma g\) is a factor of \(\Phi\), and
semilinear transport of the actual curve gives
\(R_h=L[\widetilde v]\).
The identity \(\Psi(y,z)=v+c\) transports to
\(v_h=\widetilde v+\gamma c\), proving activity and constant field
\(L\). The same transport sends the source triple to
\((y_h,z_h,w_{0h})\); by the uniqueness of rational substitution,
it is \(\sigma_h\). Hence its restriction to \(L\) is \(\gamma\),
and it fixes the two base parameters. This proves surjectivity.
If two automorphisms gave the same component, the uniquely defined
source substitution on that component would restrict to both,
so they would be equal. This proves injectivity.

The identity element corresponds to the actual factor \(g\).
In particular, if
\(L=K(f_0,\ldots,f_m,f_{-1})\), then \(\mathcal G\) is trivial
and this component subset consists only of \(g\).
That field-generation premise has not been proved in general.
Triviality of the stabilizer can also hold without that equality.

## 5. Boundaries

This result does not show that every active component has constant
field \(L\), or that every component fixes the two initial speed
ratios. Nor does equality of the normalized derivations by itself
force the chosen primitive coefficient element to be fixed.
The full coefficient-fixing criterion142 remains stronger for
selecting the actual \(L\)-component.[^3]

The target ring
\(\mathbb C[X,Y_h,Z_h,W_h]\) already carries the genuine last-slot
LND \(T_h\) for any active component. Polynomiality or local
nilpotence on that target ring alone is therefore not the new
input here. The proof uses the source inverse, its calibrated
initial triple, the exact constant field, and finite-order
coefficient comparison. It constructs no new actual extra-factor
example and makes no global cancellation or novelty claim.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 2--6. Actual projected source field, normalized inverse
   and determinant, and the polynomial Taylor expression.
2. [Formal persistence on a first-tail component141](dense-tail-component-persistence-pass141-working.md),
   Sections 1--4. Active-component field, Taylor operator, cofactor
   derivation and relative determinant one.
3. [Coefficient compatibility selects the actual first-tail component142](dense-tail-coefficient-compatibility-pass142-working.md),
   Sections 1--3. The exact rational source substitution and the
   separate primitive-element compatibility criterion.

The finite-order, calibration and rational-leading-coefficient
arguments above are proved directly. No additional external
classification theorem is used.

[^1]: Sources 1--2. The actual source inverse is an independent
    premise beyond formal relative Jacobian one.
[^2]: Sources 2--3. Algebraic independence at \(X=0\) supplies
    the rational substitution with every source denominator nonzero.
[^3]: Source 3. Fixing the full coefficient field is distinct
    from fixing its two separating base parameters.
