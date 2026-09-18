# Exact field obstructions for both reciprocal two-root families

Status: bounded working exclusion. Under the supplied actual global-slice
exact1122 frame with entire initial kernel
\(Z^2-X^2Y(X-Y)\), neither reciprocal family \(f=cq/t\) nor
\(f=cq/(t-1)\) can occur. The actual normalization202 is an explicit
input. Both of its remaining square alternatives contradict exact
projected field return. This is not a claim about arbitrary entry,
the separate family \(f=cq\), or unrestricted cancellation.

## 1. Actual normalized input and short projected formulas

Use the [actual reciprocal-pair normalization202](weight-four-two-root-reciprocal-actual-normalization-pass202-working.md).
Its involution and constant scaling reduce either family to
\(f=q/t\), with all actual fields, the selected partial, generic
alternatives, exact1122 profile and full initial kernel preserved.
Write
\[
\begin{gathered}
r=t/q,\quad \omega=1+r^2,\quad
t=r^2/\omega,\quad q=r/\omega,\quad q^2=t(1-t),\\
R=r,\quad \nu=-r\omega,\quad
k=r\rho,\quad n=-r\omega\rho^2/2,\quad
\ell=-r\omega^2\rho^3/2+rg,\qquad g\in K.
\end{gathered}
\tag{1}
\]
Here \(K\) is a finite extension of \(\mathbb C(r)\) with exact
derivative constants \(\mathbb C\), not assumed equal to
\(\mathbb C(r)\). The coefficient field \(L\) is finite over
\(K(\rho)\), with \(\ker_L\partial_\rho=K\).
The actual projected entries satisfy
\[
L[y,z,w]=L[y,\vartheta]=L[v],\qquad
\mathbb C(y,z,w)=L(v),\qquad
J_{t,\rho,v}=-a_E^3\in L^*,\quad a_E=EX .
\tag{2}
\]
In particular \(y,z,w\) are algebraically independent over
\(\mathbb C\). Neither (2) nor any original coordinate inverse is
inferred from a formal scalar determinant.

Primes below mean \(\partial_r\). The coefficient derivative in the
original potentials is \(\partial_t=\omega^2\partial_r/(2r)\).
The completed square has
\[
\begin{gathered}
\mathcal H=\frac{R\nu}{2}(V-P(U))^2+B_1U+B_0,\qquad
P(U)=p_2U^2+p_1U+p_0,\\
p_2=\frac{(r^2-3)\omega^2}{8r^4},\qquad
p_1=-\frac{\rho(r^2-1)\omega}{2r^2},\qquad
p_0=\frac{\omega\rho^2}{2},\qquad
B_1=-\frac{r\omega^2}{2}g'.
\end{gathered}
\tag{3}
\]
All these expressions follow by coefficient comparison before
evaluating \(U,V\). In particular the remaining \(g\) does not enter
\(P\), since it is \(\rho\)-constant.

Put
\[
\zeta=\vartheta-P(y),\qquad \xi=R\zeta,\qquad
h=C\rho+\varepsilon y,\quad C=\frac\omega r,\quad
\varepsilon=-\frac{\omega^2}{2r^3}.
\tag{4}
\]
The two literal projected potentials reduce to
\[
\boxed{\quad z=\xi+hy,\qquad w=hz-\frac12h^2y+g.\quad}
\tag{5}
\]
For a direct reconstruction, substitute
\(\vartheta=P(y)+\xi/r\) into
\(z=q_{tt}y^2/2+k_ty+R\vartheta+n\) and
\(Rw=\ell-S(y,\vartheta)\), where
\(S=dU^3+k_{tt}U^2/2+R_tUV+n_tU+n_\rho V\),
\(d=q_{ttt}/6\). The coefficients of each monomial in
\(y,\rho,\xi\) yield (5). No branch-specific constant has been
discarded.

## 2. The graph alternative has an impossible quadratic field degree

Suppose first that \(\vartheta\in L[y]\). The ring equality (2)
then gives \(L[y]=L[v]\), so \(y\) is affine in \(v\).
The evaluated square identity (3) gives
\((R\nu/2)\zeta^2+B_1y+B_0=0\), with
\(\zeta\in L[y]\). A nonconstant square has degree at least two;
the remaining expression has degree at most one. Hence
\(\zeta\in L\) and \(B_1=0\). By (3), \(g'=0\), so
\(g=\gamma\in\mathbb C\). Initially \(\xi=r\zeta\) need only belong
to \(L\); no descent to \(K\) or nonzero assumption is made.

Let \(w_0=w-\gamma\). Equations (5) imply the field chain
\[
\mathbb C(y,z,w_0)\ \subseteq\ \mathbb C(y,h,\xi)
\ \subseteq\ L(y)=\mathbb C(y,z,w_0).
\tag{6}
\]
Thus every inclusion is equality. The common field has transcendence
degree three, so \(y,h,\xi\) are algebraically independent over
\(\mathbb C\). Replacing \(\xi\) by \(z=\xi+hy\) is an invertible
polynomial change over \(\mathbb C[y,h]\). Consequently \(h\) is
transcendental over \(F=\mathbb C(y,z)\), and (6) would give
\[
F(h)=F(w_0),\qquad w_0=zh-yh^2/2.
\tag{7}
\]
This has degree two, not one. Explicitly, for independent \(S,H\),
the polynomial \(yH^2-2zH+2S\) is prime in \(F[S,H]\), since its
quotient is \(F[H]\) after solving for \(S\). It is primitive as a
polynomial in \(H\) over \(F[S]\). Gauss's lemma gives irreducibility
of degree two over \(F(S)\). Substitution \(S=w_0\) preserves this
statement because \(w_0\) is transcendental over \(F\).
This contradicts (7). It also covers the putative \(\xi=0\)
specialization: (6) would already have incompatible transcendence degrees.

## 3. The projection alternative and the exact scalar Jacobian

Suppose now \(B_1\ne0\), equivalently \(g'\ne0\).
The square relation and (2) give \(L[\zeta]=L[v]\), hence also
\(L[\xi]=L[v]\). With \(\Gamma=N\xi\in L^*\), the quadratic
projection is
\[
y=A\xi^2+B,\qquad
A=-\frac1{r\omega g'}\in K^*,\quad B\in L,
\qquad J_{r,\rho,\xi}=-\frac{2r\,a_E^3}{\omega^2\Gamma}\in L^*.
\tag{8}
\]
The factor \(r^2\) from \(\xi=R\zeta\) is included in \(A\).
The speed \(\Gamma\) is retained rather than normalized to one.

Differentiate the literal expressions (4)--(5), allowing unrestricted
\(y=y(r,\rho,\xi)\), and take the determinant in the order
\(r,\rho,\xi\). The exact identity is
\[
J=g'y_\rho+
\xi\{(C'\rho+\varepsilon'y)y_\rho-Cy_r\}
-yg'Cy_\xi .
\tag{9}
\]
Insert (8). The cubic coefficient in \(\xi\) is
\(\varepsilon'AB_\rho-CA'-2g'CA^2\). Since
\(\varepsilon'=-\omega(r^2-3)/(2r^4)\ne0\), its vanishing gives
\[
B=a\rho+b,\quad a,b\in K,\qquad
a=\frac{2r^2(rg''+3g')}{(r^2-3)g'}.
\tag{10}
\]
Indeed it first gives \(B_\rho=a\in K\); subtraction of \(a\rho\)
leaves \(b\in\ker_L\partial_\rho=K\). This is valid in the exact
finite field. The constant coefficient of (9) is \(g'a\).
Its nonvanishing in (8) proves \(a\ne0\).

The linear coefficient of (9), separately in \(\rho\) and its
constant term, gives
\[
(C'+\varepsilon'a)a-Ca'-2g'CAa=0,\qquad
\varepsilon'ab-Cb'-2g'CAb=0.
\tag{11}
\]
Substitute the explicit \(A,a\). The first expression is exactly
\[
-\frac{2\omega}{(r^2-3)^2g'}
\{r^2(r^2-3)g'''+6r(r^2-4)g''+6(r^2-6)g'\}=0.
\tag{12}
\]
No factor that could vanish at an allowed field element was discarded.
In particular \(r^2-3\ne0\) because \(r\) is transcendental.

## 4. Complete finite-field integration, including every constant case

The three functions \(1,r^{-2},\omega r^{-3}\) solve the homogeneous
third-order equation in braces in (12). In that order their derivative
Wronskian is \(2(r^2-3)/r^8\ne0\). The leading coefficient in (12)
is nonzero. For any solution in \(K\), express its three derivative
entries in these three columns. Differentiation and the common
third-order equation make all three coefficient derivatives zero.
Thus the complete solution inside the exact field is
\[
g=\frac\alpha{r^2}+\frac{\beta\omega}{r^3}+\gamma,
\qquad \alpha,\beta,\gamma\in\mathbb C.
\tag{13}
\]
This is not a rational-function ansatz. Set
\(D=2\alpha r+\beta r^2+3\beta\). Then
\[
g'=-D/r^4,\qquad
A=\frac{r^3}{\omega D},\qquad
a=\frac{2\beta r^2}{D},\qquad b=\delta A,
\quad \delta\in\mathbb C,\quad \beta\ne0.
\tag{14}
\]
The nonzero gate \(g'\ne0\) gives \(D\ne0\), and \(a\ne0\)
then gives \(\beta\ne0\). The case \(\alpha=0\) is retained.
For the last equality in (14), direct substitution into the second
equation (11) gives \(b'=(A'/A)b\), so \((b/A)'=0\).
No division by \(b\) is used, and \(b=0\) is included.

Put \(T=g-\gamma\). Combining \(y=A\xi^2+a\rho+\delta A\)
with \(h=C\rho+\varepsilon y\) yields the exact identity
\[
\beta h=(T+\alpha)y-\frac{\xi^2+\delta}{2}.
\tag{15}
\]
For example \(\beta(C/a+\varepsilon)=T+\alpha\) and
\(\beta CA/a=1/2\), which verify both coefficients directly.
The element \(T\) is nonconstant, so \(T+\alpha\ne0\).

## 5. Actual field return forces an impossible cubic generator

Equations (5) and (15) express \(y,z,w\) rationally in \(T,h,\xi\).
Since \(T\in K\), actual field return gives
\[
\mathbb C(y,z,w)\ \subseteq\ \mathbb C(T,h,\xi)
\ \subseteq\ K(h,\xi)\ \subseteq\ L(\xi)
=\mathbb C(y,z,w).
\tag{16}
\]
All inclusions are therefore equalities. Moreover
\(K(h,\xi)=K(\rho,\xi)\): one inclusion follows from (4),(8),(10),
and the reverse follows by solving (15) for \(y\), then using
\(\rho=(h-\varepsilon y)/C\). The elements \(\rho,\xi\) are algebraically
independent over \(K\), since \(\rho\) is transcendental over \(K\)
and \(\xi\) is a generic-line parameter over \(L\).
Hence \(h,\xi\) are algebraically independent over \(K\) as well.

Intersect the middle equality in (16) with \(K\). Algebraic
independence of \(h,\xi\) implies
\(K\cap\mathbb C(T)(h,\xi)=\mathbb C(T)\), by comparing
coefficients of a rational function in the two independent variables.
Thus \(K=\mathbb C(T)\). But \(p=1/r\in K\) satisfies
\[
T=\beta p^3+\alpha p^2+\beta p,\qquad \beta\ne0.
\tag{17}
\]
The polynomial \(\beta H^3+\alpha H^2+\beta H-S\) is prime in
\(\mathbb C[S,H]\), since its quotient is \(\mathbb C[H]\).
Its leading coefficient in \(H\) is a nonzero complex number,
so Gauss's lemma gives irreducibility of degree three over
\(\mathbb C(S)\). Equation (17) therefore implies
\([\mathbb C(p):\mathbb C(T)]=3\), whereas \(p\in K=\mathbb C(T)\)
would force degree one. This contradiction excludes the projection.

## 6. Scope

The actual normalization202 applies to both \(f=cq/t\) and
\(f=cq/(t-1)\) and preserves the two alternatives. Sections2 and5
exclude both normalized alternatives. Consequently neither reciprocal
family can occur under the complete actual hypotheses used here.
The separate \(f=cq\) family and the already separate zero-R case
are not decided by this note.

The determinant calculation retains the selected speed, every finite
field integration is justified by exact derivative constants, and
the field contradictions use the actual equality (2). Scalar
Jacobian identities alone are never treated as an original inverse.
No rationality of \(K\) was assumed; its rationality in Section5
is a consequence that immediately contradicts (17).
New inline exact arithmetic checked the raw potentials, determinant,
differential residual and parameter identities. No saved checker was
executed, imported or compiled, and no202 or earlier source was edited.
This is a bounded working proof, not expert certification, formal
verification, novelty clearance or unrestricted cancellation.
