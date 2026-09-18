# A cubic whole-plane chart for a height-two pivot of shift two

In an actual globally sliced exact1122 frame with height-two initial
kernel, a quadratic-slot partial of exact shift two gives a generic
line whose two projected coordinates generate the entire line ring.
After a coefficient-field shear they satisfy a nonzero plane equation
of total degree at most three. This bound does not require a bound
on generators of the original height-two initial ideal.

The construction is a new actual-chart reduction, not original-ring
recognition. It does not apply to the remaining pair of selected
shifts \((1,1)\). Its generic coordinate changes are not asserted
to be polynomial coordinate changes of the original four-ring.

## 1. Actual assumptions and the selected intrinsic derivation

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
I=\ker\{(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
       \mapsto(a\tau,b\tau,e\tau^2,h\tau^2)\},\qquad\operatorname{ht}I=2 .
\end{gathered}                                                     \tag{1}
\]
The parameter \(\tau\) is independent, and \(a,b\) are not
proportional over \(\mathbb C\). The named capital letters are
actual polynomial coordinates.

Suppose that the actual partial \(T_Z=\partial_Z\), holding
\(X,Y,W\) fixed, has exact all-ring \(E\)-degree shift two.
If instead the other partial has this shift, first interchange
the two actual quadratic slots and rebuild everything below.
The [initial-bound157](two-linear-two-quadratic-initial-bound-pass157-working.md)
construction supplies
\[
0\ne N=[u^2](T_Z|_A)\in\operatorname{LND}(A),\qquad
N(a)=N(b)=N(e)=N(h)=0,\qquad \deg_u T_Z(u)\le2 .                    \tag{2}
\]
Set
\[
K=\operatorname{Frac}A,\qquad
t=b/a,\quad q=e/a^2,\quad \rho=h/a^2,\qquad C_0=\mathbb C(t,q,\rho).
\]
The elementary ratio-field argument in
[height-one synthesis248](full-height-one-exact1122-recognition-pass248-working.md),
Section 5, gives
\[
\operatorname{trdeg}_{\mathbb C}C_0=1,\qquad
[C_0:\mathbb C(t)]<\infty .                                      \tag{3}
\]
That argument uses only the height-two hypothesis and the independent
good initials, not recognition of height one.
Primes on \(q,\rho\) denote the unique extension of \(d/dt\) to
this finite separable field.

## 2. The actual fixed-X projection and its determinant

The localization \(B_a=A_a[X]\) follows because \(E/a\) has slice
\(X\). Let \(y,z,w\) be the finite Taylor projections of \(Y,Z,W\)
at \(X=0\). The actual coordinate expansions are
\[
Y=y+tX,\qquad
Z=z+\sigma X+qX^2,\qquad
W=w+\theta X+\rho X^2 .                                         \tag{4}
\]
All five projected coefficients \(y,z,w,\sigma,\theta\) belong
to \(A_a\).
Quotienting the two descriptions of \(B_a\) by \(X\) gives
\[
A_a=\mathbb C[y,z,w]_{a_0},\qquad
a=a_0(y,z,w),\qquad K=\mathbb C(y,z,w).                            \tag{5}
\]
Here \(a_0\) is the nonzero specialization of the original
polynomial \(a\) at \(X=0\).

The coordinate map (4), on this localization with \(X\) fixed,
has a polynomial inverse over the same localized algebra.
Its Jacobian in the projected variables is a unit of \(A_a[X]\).
Such a unit is independent of \(X\), and its value at \(X=0\)
is one. Thus this determinant is identically one.

Choose a separating transcendence basis \(t,r,s\) of \(K/\mathbb C\).
The unique extensions of its three partials commute. The partials
in \(r,s\) annihilate \(C_0\), while the \(t\)-partial restricts
to the prime derivation in (3). The chain rule therefore gives
\[
J(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,r,s)}
=J_0:=\det\frac{\partial(y,z,w)}{\partial(t,r,s)}\in K^*.           \tag{6}
\]
This is the actual inverse's determinant identity, not an imposed
formal Jacobian ansatz.

## 3. A second invariant coefficient is forced by the top cofactors

Put
\[
S=\sigma-q'y,\qquad H=\theta-\rho'y .                            \tag{7}
\]
Expanding the \(X^3\) coefficient in (6) gives
\[
S_rH_s-S_sH_r=0.                                                \tag{8}
\]
For example, the terms before grouping are
\(\sigma_r\theta_s-\sigma_s\theta_r
-q'(y_r\theta_s-y_s\theta_r)
+\rho'(y_r\sigma_s-y_s\sigma_r)\).
There is no higher coefficient affecting (8).

Cofactors for the literal partial \(T_Z\) give
\[
[X^2]T_Z(t)=0,\qquad
[X^2]T_Z(r)=H_s/J_0,\qquad
[X^2]T_Z(s)=-H_r/J_0 .                                         \tag{9}
\]
The restriction to \(K\) has degree two in \(u\), and replacing
\(u\) by \((X-x_0)/a\), where \(X=x_0+au\), changes its leading
coefficient by \(a^{-2}\). Consequently
\[
N=\frac{a^2}{J_0}(H_s\partial_r-H_r\partial_s)
\quad\hbox{on }K,\qquad N(t)=N(H)=N(S)=0 .                       \tag{10}
\]
The last equality follows from (8). Since \(N\ne0\), at least
one of \(H_r,H_s\) is nonzero. Thus \(t,H\) are algebraically
independent.

Let
\[
L=\operatorname{Frac}(\ker_A N)=\ker_K N .
\]
The local-slice theorem gives \(A_{\ker_A N\setminus\{0\}}=L[v]\),
with \(Nv=1\), and \(K=L(v)\).
Set \(\lambda=H\). Equations (10) place the independent pair
\(t,\lambda\) in \(L\), and
\[
[L:\mathbb C(t,\lambda)]<\infty .                               \tag{11}
\]
For completeness, \(t,\lambda,v\) are a transcendence basis of
the finitely generated field \(K\), so \(K\) is finite over
\(\mathbb C(t,\lambda,v)\). Adjoining the transcendental \(v\)
preserves the degree of the algebraic extension
\(L/\mathbb C(t,\lambda)\), which proves its finiteness.

The two partials of \(\mathbb C(t,\lambda)\) extend uniquely to
\(L\), commute, and are extended to \(L[v]\) fixing \(v\).
Their \(\lambda\)-partial annihilates \(q,\rho\).
By (7),(10), for some \(k\in L\),
\[
\sigma=q'y+k,\qquad \theta=\rho'y+\lambda .                      \tag{12}
\]
There has been no replacement of \(L\) by \(C_0\) or by a
presumed rational coefficient field.

Since \(a\in\ker_A N\setminus\{0\}\), (5) now implies
\[
y,z,w,\sigma,\theta\in L[v],\qquad L[y,z,w]=L[v] .                 \tag{13}
\]
In the new variables \(t,\lambda,v\), the coefficient of \(X^2\)
in the cofactor for \(T_Z(v)\) is \(-1/J\), by (12).
Its coefficient must also be \(a^{-2}\), by \(Nv=1\).
Thus the exact calibration is
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}
 =-a^2\in L^* .                                                 \tag{14}
\]
In particular \(a\) is a coefficient-field unit, not necessarily
a unit of the original polynomial ring.

## 4. The first integral gives the entire projected plane ring

Write \(d=\rho''\) and \(m=k_\lambda\).
For total differentials over \(\mathbb C\) with \(X\) fixed,
subtract \(q'X\,dY\) and \(\rho'X\,dY\) from the last two
coordinate rows in (4). The resulting three rows are
\[
\begin{aligned}
dY&=dy+X\,dt,\\
dZ_{\rm red}&=dz+X\{(q''y+k_t)\,dt+m\,d\lambda\},\\
dW_{\rm red}&=dw+X\{d\,y\,dt+d\lambda\}.
\end{aligned}                                                   \tag{15}
\]
These row operations preserve the determinant.
The coefficient of \(X^2\), with orientation
\(dt\wedge d\lambda\wedge dv\), is
\[
-z_v+m w_v+\{(q''-dm)y+k_t\}y_v .
\]
It vanishes by (14). Integration in the polynomial variable \(v\)
therefore gives \(n\in L\) such that
\[
z=mw+f(y),\qquad
f(U)=\frac{q''-dm}{2}U^2+k_tU+n .                               \tag{16}
\]
This does not divide by \(y_v\). It includes constant \(y\).
Equations (13),(16) prove
\[
\boxed{L[y,w]=L[v].}                                             \tag{17}
\]
Thus the projected plane image itself is the entire affine line;
only saying that its normalization is a line would be weaker.

## 5. The second integral and the depressed cubic

Subtract \(m\) times the last row of (15) and \(f_U(y)\) times
its first row from the middle one. All its \(X\)-terms cancel.
It becomes
\[
B_1\,dt+C_1\,d\lambda,\qquad
B_1=m_t w+f_t(y),\quad C_1=m_\lambda w+f_\lambda(y),               \tag{18}
\]
where coefficient partials of \(f\) hold \(U\) fixed.
The remaining positive-degree determinant coefficient is
\[
J_1=(B_1-dyC_1)y_v+C_1w_v=0 .                                  \tag{19}
\]
Here \(dyC_1\) means the product \(d\cdot y\cdot C_1\).

The identity
\[
f_{\lambda U}=m_t-dU m_\lambda
\]
shows that (19) is an exact derivative in \(v\).
Define a polynomial in \(U\) by the explicit antiderivative
\[
P(U)=\frac{d^2m_\lambda}{8}U^4
 +\frac{q'''-\rho'''m-3dm_t}{6}U^3
 +\frac{k_{tt}-dn_\lambda}{2}U^2+n_tU .
\]
It satisfies \(P_U=f_t-dU f_\lambda\), including every lower
coefficient. Hence for some \(\ell\in L\),
\[
\frac{m_\lambda}{2}w^2+f_\lambda(y)w+P(y)=\ell .                  \tag{20}
\]
No integration in the possibly algebraic coefficient field is
required for this step.

Make only the coefficient-field shear
\[
\zeta=w-\frac{\rho''}{2}y^2 .
\]
It has an inverse over \(L\), so \(L[y,\zeta]=L[v]\).
Substituting this shear in (20) cancels the quartic and the
mixed quadratic terms. The final relation is
\[
\boxed{
\mathcal H(U,V)=
\frac{k_{\lambda\lambda}}2 V^2
 +(k_{t\lambda}U+n_\lambda)V
 +\frac{q'''-\rho'''k_\lambda}{6}U^3
 +\frac{k_{tt}}2U^2+n_tU-\ell,\qquad
\mathcal H(y,\zeta)=0 .}                                       \tag{21}
\]
It has total degree at most three.

The polynomial \(\mathcal H\) is nonzero.
If it vanished identically, (20) before the invertible shear
would be a constant formal polynomial. Its formal derivatives
would give \(C_1=0\) and \(B_1-dyC_1=0\), hence \(B_1=0\).
The constant determinant coefficient
\[
\left[dy\wedge(B_1dt+C_1d\lambda)\wedge dw\right]_
                 {dt\wedge d\lambda\wedge dv}=-a^2
\]
would then vanish, contradicting (14).

The full kernel of \(L[U,V]\to L[v]\) at \((y,\zeta)\)
is a height-one prime, generated by an irreducible factor of
\(\mathcal H\). Its quotient is exactly \(L[v]\).
The proof does not assert that \(\mathcal H\) itself is
irreducible, reduced, or the generator of that kernel.

## 6. Scope of the new reduction

The proof gives an exact-field, degree-at-most-three projected
problem whenever a height-two frame has a selected shift-two
pivot. It keeps constant first projection, repeated or extra
eliminant factors, and nonrational coefficient fields in scope.
It does not require a bounded generating set for the initial ideal.

The remaining proof obligations are to use the full scalar
determinant and actual field return, and to construct any needed
invariant coordinate in the original ring. A generic polynomial
shear in \(L[U,V]\) is not that construction.
The pair of selected shifts \((1,1)\) is a separate case.
Arbitrary coordinate entry and higher time profiles also remain open.

The actual initial-bound157 and the ratio-field argument248
were read completely. The projection, top cofactors, calibration,
two integrations and final cubic are reconstructed here.
An independent unsaved algebra reconstruction agrees with the
coefficient identities, but finite algebra does not prove the
generic-field and original-ring assertions.

No earlier source or frozen packet was edited. No saved checker
was executed, imported or compiled for this note.
No human expert review, proof-assistant certification, historical
novelty, external contact or unrestricted cancellation solution
is claimed.
