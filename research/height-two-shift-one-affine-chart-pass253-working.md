# The affine generic-line chart when both selected shifts are one

Status: exact-field reduction for an actual globally sliced
E-time \((1,1,2,2)\) frame with full initial kernel of height two
and both literal quadratic-slot partials of exact shift one.
The projected first coordinate is an affine parameter on the
intrinsic generic line. Its actual determinant gives two differential
identities over the coefficient field.

A nonlinear dependence on the second coefficient parameter gives
an actual weight-two initial relation and the retained three-good
recognition endpoint. Otherwise all displayed coefficients reduce
to a finite algebraic curve field over \(\mathbb C(t)\).
That remaining reduction is not claimed here to be an original-ring
coordinate construction.

## 1. Actual entry and fixed-X projection

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\qquad K=\operatorname{Frac}A,\\
t=b/a\notin\mathbb C,\qquad q=e/a^2,\qquad \rho=h/a^2 .
\end{gathered}
\tag{1}
\]
The full kernel of the weighted initial map
\((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\mapsto(a\tau,b\tau,e\tau^2,h\tau^2)\), with independent \(\tau\),
has height two. Thus
\[
C_0=\mathbb C(t,q,\rho),\qquad [C_0:\mathbb C(t)]<\infty .
\tag{2}
\]
Indeed the initial fraction field is
\(\mathbb C(a\tau,t,q,\rho)\), of transcendence degree two;
\(a\tau\) is transcendental over \(K\), so the ratio field has
transcendence degree one. Since \(t\) is nonconstant and the field
is finitely generated, (2) follows.

Let \(T_Z=\partial_Z,T_W=\partial_W\) be the literal actual
partials. Their exact shifts are assumed to be
\(k_Z=k_W=1\). The intrinsic construction of
[157](two-linear-two-quadratic-initial-bound-pass157-working.md)
gives nonzero LNDs
\[
N_Z=[u]T_Z|_A,\qquad N_W=[u]T_W|_A,\qquad
N_i(a)=N_i(b)=N_i(e)=N_i(h)=0,\qquad \deg_uT_i(u)\le1 .
\tag{3}
\]
The shift-zero branch and the general selected-wedge rank statement
are treated separately in
[249](height-two-selected-partial-wedge-rank-pass249-working.md).

The actual localization \(B_a=A_a[X]\) follows from the slice
\(X\) for \(E/a\). Taylor projection at \(X=0\) gives
\[
Y=y+tX,\qquad
Z=z+\sigma X+qX^2,\qquad W=w+\theta X+\rho X^2 ,
\tag{4}
\]
where \(y,z,w,\sigma,\theta\in A_a\).
Quotienting by \(X\) gives
\[
A_a=\mathbb C[y,z,w]_{a_0},\qquad a=a_0(y,z,w),\qquad
K=\mathbb C(y,z,w).
\tag{5}
\]
Here \(a_0\) is the nonzero specialization of the actual polynomial
\(a\) at \(X=0\). These are the localization and quotient-ring
gates reconstructed in the fully read
[250 chart](height-two-shift-two-cubic-chart-pass250-working.md);
they do not require shift two.

Choose a separating transcendence basis \(t,r,s\) of \(K/\mathbb C\).
Its extended partials commute, and the \(r,s\) partials kill \(C_0\).
The actual invariant-volume identity is
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,r,s)}
=J_0\in K^*,
\tag{6}
\]
independent of \(X\). This follows either from the localized actual
inverse in (5), or from the invariant original volume and
\(X=x_0+au\), as in249. No formal constant-Jacobian ansatz is added.

## 2. Both first residual coefficients lie on the ratio curve

Primes denote the unique extension of \(d/dt\) to \(C_0\).
Define
\[
S=\sigma-q'y,\qquad H=\theta-\rho'y .
\tag{7}
\]
The degree-two horizontal cofactors of \(T_Z\) in the basis
\((t,r,s)\) are
\[
[X^2](T_Z(t),T_Z(r),T_Z(s))
  =J_0^{-1}(0,H_s,-H_r).
\]
For \(T_W\) they are \(J_0^{-1}(0,-S_s,S_r)\).
Both vanish because the exact shifts are one. Therefore
\[
S_r=S_s=H_r=H_s=0 .
\tag{8}
\]
In characteristic zero, (8) implies \(dS\wedge dt=dH\wedge dt=0\)
and hence each of \(S,H\) is algebraic over \(\mathbb C(t)\).
This is a differential algebraic-dependence statement in \(K\),
not rationality of those coefficients.
Consequently
\[
F_0=\mathbb C(t,q,\rho,S,H)
\quad\text{is finite separable over }\mathbb C(t).
\tag{9}
\]
Primes now denote the unique extension to \(F_0\). Its elements
are still annihilated by the \(r,s\) partials.

Set
\[
\xi=z-\frac{q''}{2}y^2-S'y,\qquad
\zeta=w-\frac{\rho''}{2}y^2-H'y .
\tag{10}
\]
These are elements of \(K\). To compute the new top coefficient,
first subtract \(q'X\,dY,\rho'X\,dY\) from the last two rows of
the fixed-X differential matrix of (4). Next subtract
\((q''y+S')dY,(\rho''y+H')dY\), respectively.
The resulting three rows, with unchanged determinant, are
\[
dy+Xdt,\qquad d\xi+A(y)dt,\qquad d\zeta+B(y)dt,
\quad
A(U)=\frac{q'''}2U^2+S''U,\quad
B(U)=\frac{\rho'''}2U^2+H''U .
\tag{11}
\]
Thus the coefficient of \(X\) in (6) is
\[
\xi_r\zeta_s-\xi_s\zeta_r=0 .
\tag{12}
\]
The \(X\)-cofactor for \(T_Z\) is the Hamiltonian row of \(\zeta\).
Since \([u]T_Z=a[X]T_Z\) on \(K\), this gives
\[
N:=N_Z=\frac{a}{J_0}
       (\zeta_s\partial_r-\zeta_r\partial_s),\qquad
N(t)=N(\zeta)=N(\xi)=0 .
\tag{13}
\]
The final equality uses (12). Nonzero exact shift one implies
\((\zeta_r,\zeta_s)\ne(0,0)\), so \(t,\zeta\) are algebraically
independent.

## 3. Exact coefficient field and the entire generic line

Put \(L=\operatorname{Frac}(\ker_A N)=\ker_K N\).
The local-slice theorem gives
\[
A_{\ker_A N\setminus\{0\}}=L[v],\qquad Nv=1,\qquad K=L(v).
\tag{14}
\]
The equality of the two constant fields follows from this same
localization. Since \(N(t)=0\), it annihilates every element of
\(F_0\), by separability of (9).
Set
\[
\lambda=\zeta\in L,\qquad \xi=n\in L .
\]
Then \(t,\lambda\) are independent and
\([L:\mathbb C(t,\lambda)]<\infty\). For the finiteness, \(K\) is
finite over \(\mathbb C(t,\lambda,v)\), and adjoining the independent
transcendental \(v\) preserves the degree of the algebraic extension
\(L/\mathbb C(t,\lambda)\).
The two coordinate partials extend uniquely and commute on \(L\).
Its \(\lambda\)-partial kills \(F_0\); its \(t\)-partial agrees there
with the prime in (9).

As \(a\) is a nonzero invariant of \(N\), (5),(14) imply
\(L[y,z,w]=L[v]\). Equation (10) now gives
\[
z=n+\frac{q''}{2}y^2+S'y,\qquad
w=\lambda+\frac{\rho''}{2}y^2+H'y,\qquad
\boxed{L[y]=L[v].}
\tag{15}
\]
In particular \(y=\alpha v+\beta\) for \(\alpha\in L^*,\beta\in L\):
the degrees in an identity \(v=P(y)\) multiply, forcing
\(\deg_v y=1\). Hence \(Ny=\alpha\in L^*\).
No affine change in the original four-ring has been made.

## 4. Full scalar determinant and its calibration

Use the separating basis \(t,\lambda,y\) of \(K/\mathbb C\).
The actual coordinate formulas are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=n+\frac{q''}{2}y^2+S'y+(q'y+S)X+qX^2,\\
W&=\lambda+\frac{\rho''}{2}y^2+H'y+(\rho'y+H)X+\rho X^2.
\end{aligned}
\tag{16}
\]
In this basis (11) becomes
\[
dy+Xdt,\qquad
\left(n_t+\frac{q'''}2y^2+S''y\right)dt+n_\lambda d\lambda,\qquad
\left(\frac{\rho'''}2y^2+H''y\right)dt+d\lambda .
\]
With orientation \(dt\wedge d\lambda\wedge dy\), its determinant is
\[
J=n_t+
  \frac{q'''-n_\lambda\rho'''}2y^2+
  (S''-n_\lambda H'')y .
\tag{17}
\]
This is the whole determinant, not only selected high coefficients.

The cofactor numerator for \(T_Z(y)\) in (16) is exactly \(-X\).
As \(J\) is independent of \(X\), comparison of its \(X\)-coefficient
with the exact intrinsic coefficient in (3) gives
\[
Ny=-a/J,\qquad
\boxed{J=-a/(Ny)\in L^*.}
\tag{18}
\]
This proves its coefficient-field scalar property before comparing
coefficients in (17). Since \(y\) is transcendental over \(L\),
\[
\boxed{
n_t=-a/(Ny)\ne0,\qquad
q'''=n_\lambda\rho''',\qquad S''=n_\lambda H'' .
}
\tag{19}
\]
The corresponding cofactor numerator for \(T_W(y)\) is
\(Xn_\lambda\). Its leading cofactor field is therefore
\(N_W=-n_\lambda N_Z\), consistent with249.
In particular \(n_\lambda\ne0\), since \(k_W=1\) is exact.
The units in these formulas are units of \(L\), not assertions
about the units of \(B\).

## 5. The nonlinear coefficient branch and the remaining curve field

Differentiate the first identity in (19) involving third derivatives
with respect to \(\lambda\). Since \(q,\rho\in F_0\), this gives
\(n_{\lambda\lambda}\rho'''=0\).
If \(n_{\lambda\lambda}\ne0\), then
\[
q'''=\rho'''=0 .
\tag{20}
\]
An element \(f\) of the finite field \(F_0/\mathbb C(t)\) with
\(f'=0\) is algebraic over \(\mathbb C\) and therefore complex:
use \(df=0\) in its one-dimensional differential space.
Successively applying this to the derivatives and differences of
\(q,\rho\) proves that both are complex polynomials in \(t\) of
degree at most two.

For example write \(q=q_2t^2+q_1t+q_0\), \(q_i\in\mathbb C\).
Then \(e=q_2b^2+q_1ab+q_0a^2\), and the actual shear
\[
Z_1=Z-(q_2Y^2+q_1XY+q_0X^2),\qquad
Z=Z_1+(q_2Y^2+q_1XY+q_0X^2)
\tag{21}
\]
has both polynomial inverse orders and satisfies \(E^2Z_1=0\).
It preserves the two original good coordinates.
Thus the explicitly retained three-good theorem156 recognizes
\(A\simeq\mathbb C^{[3]}\) in this branch, with the same mathematical
and source dependencies as that working theorem.

In the other branch put
\[
m=n_\lambda,\qquad n_0=n-m\lambda .
\]
If \(n_{\lambda\lambda}=0\), both \(m,n_0\) are killed by
\(\partial_\lambda\). Their differentials are multiples of \(dt\),
so they are algebraic over \(\mathbb C(t)\).
Thus, after adjoining these finitely many elements,
\[
\begin{gathered}
F=\mathbb C(t,q,\rho,S,H,m,n_0),\qquad
[F:\mathbb C(t)]<\infty,\qquad m\ne0,\\
n=m\lambda+n_0,\qquad
q'''=m\rho''',\qquad S''=mH'',\qquad
m'\lambda+n_0'\ne0 .
\end{gathered}
\tag{22}
\]
The prime is the unique extended \(t\)-derivative on \(F\).
This does not identify \(t\) with a rational parameter of \(F\),
or make any element of \(F\) an original-ring coefficient unit.

## 6. Scope and evidence

The conclusion is an exact affine generic-line chart and its scalar
constraints. This source does not recognize the remaining case (22)
or assert that a coefficient-field shear descends to an ambient
polynomial automorphism.

The complete selected-partial input157, wedge-rank note249,
shift-two chart250 and three-good synthesis156 were read.
Only the projection and determinant mechanism of250 is used here;
its shift-two hypothesis is not imported into the present entry.
The whole-ring return, exact separating fields, shift-one cofactors,
and determinant calibration have been reconstructed.

An independent unsaved symbolic expansion of the literal map (16)
has zero residual against (17) and gives cofactor numerators
\(-X\) and \(Xn_\lambda\). It is a finite algebra control, not a
proof of the exact-field or original-ring gates.
No saved checker was executed, imported or compiled. No previous
source, index, or frozen packet was edited. No arbitrary-entry
recognition or unrestricted cancellation conclusion is claimed.
