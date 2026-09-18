# A dense all-degree chart and its formal Taylor peeling

An actual sliced fourfold with three affine-in-time coordinates and
rank-two speeds with dense homogeneous cone admits the two-parameter
chart below. A formal Taylor embedding through its finite algebraic
coefficient field separates every coefficient of the last coordinate.
The two projected good coordinates together generate the whole generic
intrinsic line.

This is a bounded chart theorem, not global recognition. The coefficient
field still has transcendence degree two. The strictly negative Laurent
tail has derivative one and cannot be discarded as an invariant remainder.

## 1. Actual hypotheses and the intrinsic leading derivation

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
P(s,t,b)\ne0\ \text{for every nonzero homogeneous }P\in\mathbb C[S,T,B_0].
\end{gathered}
\tag{1}
\]
The displayed generators of \(B\) are actual polynomial coordinates.
The slice \(u\) is not assumed to be an ambient coordinate.
There is no bound on the finite integer \(m=\deg_E W\ge0\).

Let \(T=\partial_W\), holding \(X,Y,Z\) fixed.
The actual volume and cofactor theorem132 proves exact \(u\)-degree
shift two, without a last-coordinate degree assumption.[^1]
Combining that bound with the leading-LND construction125 gives
\[
T(A)\subset A[u]_{\le2},\qquad T(u)\in A[u]_{\le2},\qquad
N=[u^2]T|_A\in\operatorname{LND}(A)\setminus\{0\},\qquad
N(s)=N(t)=N(b)=0 .
\tag{2}
\]
Here \([u^2]\) extracts the coefficient of \(u^2\).
The actual Laurent rescaling of the LND \(T\), followed by
specialization, gives the nonzero homogeneous LND with value
\(u^2N(f)\) on \(A\) and zero on \(u\). Its iterates prove local
nilpotence of \(N\). The coefficient of \(u^3\) in the three
identities \(T(X)=T(Y)=T(Z)=0\) proves speed annihilation.[^2]
No local nilpotence is inferred by dividing an arbitrary vector field,
and no invariance of all the lower coefficients of \(W\) is assumed.

Set \(S_0=\ker_A N\), \(L=\operatorname{Frac}S_0\), and
\(F=\operatorname{Frac}A\). An intrinsic local slice gives
\(F=L(v_0)\), so \(\operatorname{trdeg}_{\mathbb C}L=2\).
The field \(L\) is finite over \(\mathbb C(s,t,b)\).
Indeed \(F\) is finitely generated, since \(A\simeq B/(u)\), and
therefore is finite over \(\mathbb C(s,t,b)(v_0)\).
Linear independence over the speed field is preserved when its
transcendental \(v_0\) is adjoined, proving the claimed finiteness.

## 2. Speed ratios and actual fixed-\(X\) localization

Every speed is nonzero by density. Define
\[
\tau=t/s,\qquad \rho=b/s,\qquad
\tau,\rho\text{ algebraically independent over }\mathbb C,\qquad
L/\mathbb C(\tau,\rho)\text{ finite and separable}.
\tag{3}
\]
A nonzero polynomial relation between the ratios could be homogenized
using \(s\), contradicting (1). The speed field has the same
transcendence degree as \(\mathbb C(\tau,\rho)\); thus \(s\) is
algebraic over that field, proving (3).
Extend the two coefficient partials uniquely through this finite
separable extension. They commute.

The LND \(E/s\) on \(B_s\) has slice \(X\). Its finite Taylor
projection gives
\[
\begin{gathered}
B_s=A_s[X],\qquad
A_s=\mathbb C[y,z,w_0]_{s_0(y,z,w_0)},\qquad s=s_0(y,z,w_0),\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=\mathcal W(X)=\sum_{j=0}^{m}w_jX^j,\qquad
w_j\in A_s,\quad w_m\ne0 .
\end{gathered}
\tag{4}
\]
Here \(w_0\) is the Taylor projection of \(W\), and the equality
of \(X\)-degree and \(E\)-degree uses \(E=s\partial_X\).

Quotienting \(B_s=A_s[X]\) by \(X\) identifies \(A_s\) with
\(\mathbb C[Y,Z,W]_{s(0,Y,Z,W)}\).
It is nonzero, so \(s_0(Y,Z,W)=s(0,Y,Z,W)\ne0\).
This proves the algebraic independence of \(y,z,w_0\) before
localization and their presentation in (4).
Projecting the invariant \(s\) proves its formula there.

Both (4) and its Taylor inverse are maps of actual localized polynomial
rings. Their Jacobian determinants are inverse units.
After pullback to \(\mathbb C[y,z,w_0]_{s_0}[X]\), a unit is
independent of \(X\); evaluation at \(X=0\) gives determinant one.
This derives the Jacobian from the actual inverse, not the inverse
from a Jacobian condition.[^3]

Write \(X=b_X+su\), with \(b_X\in A\).
Re-expanding (2), including the quotient rule, yields
\[
N'=[X^2]T|_{A_s}=N/s^2,\qquad
N'\in\operatorname{LND}(A_s)\setminus\{0\},\qquad
A_L=L[v]=L[y,z,w_0],\qquad N'v=1 .
\tag{5}
\]
The LND assertion uses only localization at the invariant \(s\) and
multiplication by the invariant unit \(s^{-2}\).
The localized \(T\) is not declared locally nilpotent.
Choose \(a\in A\) with \(Na=h\ne0\), \(Nh=0\), and set \(v=s^2a/h\).
The local-slice theorem gives \(A_L=L[a/h]=L[v]\).
Since \(s_0=s\in L^*\), the denominator in (4) disappears on this
generic fiber. It is the entire affine line, not an open subset.
In particular \(y,z,w_j\in L[v]\).
Extend the coefficient partials to fix \(v\), so \(N'=\partial_v\).

## 3. The relative determinant is exactly one

Initially all coefficient derivatives hold \(v\) fixed.
The Jacobian \(J(X)\) of \((Y,Z,W)\) with respect to
\((\tau,\rho,v)\), holding \(X\) fixed, is independent of \(X\)
by the actual Jacobian identity above. Write \(J(X)=J_0\in F^*\).
The matrix and the selected cofactor are
\[
\begin{gathered}
\begin{pmatrix}
y_\tau+X&y_\rho&y_v\\
z_\tau&z_\rho+X&z_v\\
\mathcal W_\tau&\mathcal W_\rho&\mathcal W_v
\end{pmatrix},\\
T(v)=\frac{X^2+(y_\tau+z_\rho)X+y_\tau z_\rho-y_\rho z_\tau}{J_0},
\qquad [X^2]T(v)=N'v=1,\qquad J_0=1 .
\end{gathered}
\tag{6}
\]
Thus the normalization follows from the intrinsic slice \(v\);
it is not imposed on an arbitrary rational volume form.

Put
\[
\begin{gathered}
h=y_\tau+z_\rho,\qquad M=y_\tau z_\rho-y_\rho z_\tau,\\
C_\tau=y_\rho z_v-y_vz_\rho,\qquad
C_\rho=y_vz_\tau-y_\tau z_v,\\
T(\tau)=C_\tau-Xy_v,\qquad T(\rho)=C_\rho-Xz_v,\qquad
T(v)=X^2+hX+M,\\
1=(X^2+hX+M)\mathcal W_v+
(C_\tau-Xy_v)\mathcal W_\tau+(C_\rho-Xz_v)\mathcal W_\rho .
\end{gathered}
\tag{7}
\]
In particular the \(Xz_v\) term in \(T(\rho)\) has a minus sign.
The cofactors use \(T(X)=T(Y)=T(Z)=0\), \(T(W)=1\), without
restricting the degree of the last row.

## 4. The first three top coefficients

Give \(w_j\) value zero outside \(0\le j\le m\).
For every \(k\ge0\), coefficient comparison in (7) gives
\[
\begin{aligned}
(w_{k-2})_v+h(w_{k-1})_v+M(w_k)_v
-y_v(w_{k-1})_\tau-z_v(w_{k-1})_\rho
+C_\tau(w_k)_\tau+C_\rho(w_k)_\rho
=\begin{cases}1&k=0,\\0&k>0.\end{cases}
\end{aligned}
\tag{8}
\]
At \(k=m+2\), this says \(w_m=f_m\in L\).
For \(m\ge1\), the next equation integrates to
\(w_{m-1}=y(f_m)_\tau+z(f_m)_\rho+f_{m-1}\), with \(f_{m-1}\in L\).
For \(m\ge2\), the third equation gives
\[
\begin{aligned}
w_{m-2}={}&\tfrac12y^2(f_m)_{\tau\tau}
+yz(f_m)_{\tau\rho}+\tfrac12z^2(f_m)_{\rho\rho}\\
&+y(f_{m-1})_\tau+z(f_{m-1})_\rho+f_{m-2},
\qquad f_{m-2}\in L .
\end{aligned}
\tag{9}
\]
No division by \(y_v\) or \(z_v\) is used.
On substituting the formula for \(w_{m-1}\), the first-derivative
chain terms cancel using exactly \(h,C_\tau,C_\rho\) in (7).
What remains is the \(v\)-derivative of the expression in (9).

For \(m=1\), subsequent positive-degree equations are compatibility
conditions, not formulas for negative-index coefficients.
For \(m=0\), the top equation still yields \(w_0\in L\), followed
by the \(X\) and constant equations in (8).
The constant equation always has right side one.
The uniform formal argument below includes both small-degree cases.

## 5. The continuous Laurent derivation and algebraic Taylor embedding

Let \(\varepsilon=X^{-1}\) and use the natural expansion embedding
\(F(X)\subset F((\varepsilon))\).
The degree bound on \(T(F)\), obtained by the quotient rule from
(2), together with \(T(X)=0\), gives
\[
\begin{gathered}
T|_F=D_0+XD_1+X^2\partial_v,\\
T\left(\sum_{n\ge n_0}a_n\varepsilon^n\right)
=\sum_{n\ge n_0}
\left(D_0a_n\,\varepsilon^n+
D_1a_n\,\varepsilon^{n-1}+
\partial_va_n\,\varepsilon^{n-2}\right).
\end{gathered}
\tag{10}
\]
Coefficient comparison in the Leibniz identity shows that \(D_0,D_1\)
are derivations of \(F\).
Each coefficient in the right side is a finite sum, and the operator
lowers the \(\varepsilon\)-valuation by at most two.
It therefore defines a continuous derivation of the Laurent field,
agreeing with the actual \(T\) on \(F(X)\) and fixing \(\varepsilon\).
Local nilpotence of this extension is neither asserted nor needed.

Commuting coefficient partials define a Taylor homomorphism
\(L\to L[[h_1,h_2]]\).
Substitute \(h_1=y\varepsilon\), \(h_2=z\varepsilon\).
Only finitely many monomials contribute to each power of \(\varepsilon\),
so this is a well-defined homomorphism into \(F[[\varepsilon]]\).
It gives
\[
\begin{gathered}
\Theta:L\hookrightarrow F((\varepsilon)),\qquad
\Theta(f)=\sum_{a,b\ge0}
\frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}
y^az^b\varepsilon^{a+b},\\
\Theta(\tau)=\tau+y/X=Y/X,\qquad
\Theta(\rho)=\rho+z/X=Z/X,\qquad T\Theta(f)=0\quad(f\in L).
\end{gathered}
\tag{11}
\]
The commuting-derivative Leibniz formula proves multiplicativity
before substitution. The constant term is \(f\), so the map is
injective and each nonzero image is a unit of \(F[[\varepsilon]]\).
The elements \(y,z\) need not lie in \(L\); their membership in \(F\)
suffices for the substitution homomorphism.

For the last assertion in (11), the actual \(T\) kills \(Y/X,Z/X\),
hence kills the image of \(\mathbb C(\tau,\rho)\).
Transport the monic minimal polynomial of \(f\in L\) over that
base through \(\Theta\), then differentiate its identity at
\(\Theta(f)\) with \(T\).
All coefficient derivatives vanish.
The polynomial derivative at \(\Theta(f)\) is nonzero: its constant
term is the original separable minimal-polynomial derivative at \(f\).
Therefore \(T\Theta(f)=0\).
This justifies the shifted-field argument even when
\(L\ne\mathbb C(\tau,\rho)\).
No analytic branch or convergence assertion occurs.

## 6. Finite peeling and the nonzero negative tail

Set \(R^{(m)}=\mathcal W\).
At stage \(m\ge j\ge0\), suppose the remainder has no powers of
\(X\) greater than \(j\) and satisfies \(TR^{(j)}=1\).
Let \(f_j=[X^j]R^{(j)}\in F\), allowing zero.
The coefficient of \(X^{j+2}\) in its derivative is
\(\partial_vf_j\), by (10).
Since \(j+2>0\), it is zero, so \(f_j\in L\).
Define
\[
\begin{gathered}
R^{(j-1)}=R^{(j)}-X^j\Theta(f_j)\quad(j=m,\ldots,0),\\
\mathcal W=
\left[\sum_{j=0}^{m}X^j\Theta(f_j)\right]_{\ge0},\qquad
R:=\mathcal W-\sum_{j=0}^{m}X^j\Theta(f_j)
\in X^{-1}F[[X^{-1}]],\qquad TR=1,\quad R\ne0 .
\end{gathered}
\tag{12}
\]
The constant term of \(\Theta(f_j)\) cancels the coefficient at \(X^j\).
Equation (11) preserves the derivative value.
This proves the downward induction, including \(j=0\).
Here \([\ ]_{\ge0}\) extracts nonnegative powers of \(X\), not of
\(\varepsilon\).

The negative remainder cannot vanish because its derivative is one.
Thus the polynomial part is not the complete invariant formal series.
The tail carries remaining compatibility equations even in small-degree
or already recognized actual frames.

Comparing coefficients in (12) proves
\[
w_j=\sum_{k=j}^{m}\ \sum_{a+b=k-j}
\frac{\partial_\tau^a\partial_\rho^b f_k}{a!\,b!}\,y^az^b
\in L[y,z],\qquad
\deg_{y,z}w_j\le m-j\quad(0\le j\le m).
\tag{13}
\]
The bound means there is a polynomial expression of that degree before
imposing any algebraic relation between \(y,z\).
Their independence is not assumed.

## 7. Whole-line consequence and the remaining gap

Since \(w_0\in L[y,z]\), equations (5) and (13) imply
\[
L[v]=L[y,z,w_0]=L[y,z].
\tag{14}
\]
The pair therefore generates the whole polynomial generic line.
Neither individual generator is proved linear in \(v\);
no analogue of the conical identity \(L[v]=L[y]\) is inferred.

Substituting \(y=Y-\tau X\), \(z=Z-\rho X\) in (13) also gives
\(W\in L[X,Y,Z]\) with ordinary total degree at most \(m\).
This does not meet the earlier one-variable monic-pencil descent
hypothesis. The invariant field \(L\) has transcendence degree two,
and the three goods are themselves algebraically dependent over \(L\).
The embedded-line relation and the negative tail retain information
not captured by this polynomial expression.

No polynomial presentation for \(A\), invariant ambient coordinate,
or arbitrary three-good coordinate-entry theorem is proved here.
The construction uses the intrinsic leading LND and its local slice,
not the stronger source-dependent assertion that its kernel is an
actual affine plane.

## Sources

1. [Dense three-good speeds force exact bad-partial adjoint degree two](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5. Actual invariant volume, bounds on all coefficients,
   and nonzero degree-two horizontal coefficient, without a
   last-coordinate degree bound.
2. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. Actual Laurent leading-LND construction, annihilation
   of the speed row, and intrinsic local slice. Section 6's separate
   affine-plane quotient theorem is not invoked.
3. [An all-degree actual chart for nonlinear conical speeds](all-degree-conical-chart-pass138-working.md),
   Section 2. Actual fixed-\(X\) Taylor localization and the whole-line
   mechanism, reproduced here with the dense degree-two rescaling.
   Its conical cofactor equation is not assumed.

[^1]: [Dense cofactor132](dense-three-good-adjoint-degree-pass132.md), Sections 2--5.
[^2]: [Intrinsic leading125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^3]: [Actual chart138](all-degree-conical-chart-pass138-working.md), Section 2.

