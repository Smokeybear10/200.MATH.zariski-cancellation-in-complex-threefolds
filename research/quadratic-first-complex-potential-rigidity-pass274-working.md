# Complex-coefficient potentials after the quadratic-first reduction

The full-potential result273 gives a useful coefficient-field normal form.
After an explicitly invertible change of the formal coefficient parameter,
the quadratic potential has complex coefficients. Its cubic primitive has
complex coefficients as well, except for one nonconstant element of the
invariant curve field.

This is not an ambient coordinate change or a recognition theorem.

## 1. Exact retained inputs

Retain all actual hypotheses and conclusions of
[the full-potential reduction273](quadratic-first-full-potential-discriminant-reduction-pass273-working.md),
whose complete saved source was read. In particular \(F/\mathbb C(t)\)
is finite, the constants of its extended prime derivative are exactly
\(\mathbb C\), and
\[
\begin{gathered}
L=F(\lambda),\qquad K=L(x)=F(y,x),\\
x^2=dy+\alpha\lambda+\beta,\qquad
d,\alpha\in F^*,\quad\beta\in F,\\
e=1/m,\quad h=m/N_2,\qquad m,N_2\in F^*.
\end{gathered}
\tag{1}
\]
The notation \(N_2\) is the coefficient of the quadratic polynomial
\(n=N_2\lambda^2/2+n_1\lambda+n_0\), not the intrinsic derivation.

With \(U\) a formal variable, the actual intercepts satisfy
\[
\begin{gathered}
z=hx+P_z(y),\qquad w=A(y)z+B_0(y),\\
A(U)=e'U-(N_2\lambda+n_1)e^2,\\
P_z\in F[U,\lambda],\quad \deg_{\rm total}P_z\le2,\qquad
B_0\in F[U,\lambda],\quad \deg_{\rm total}B_0\le3.
\end{gathered}
\tag{2}
\]
These total-degree bounds follow from the precise coefficient bounds
in270 and273. They are not bounds on the ambient coordinate degrees.

The complete identities, with partials initially fixing \(U,\lambda\),
are
\[
\begin{aligned}
(B_0)_\lambda&=N_2e^2P_z,\\
A_t&=-e^2(2MU+b_1),\\
A_tP_z+(B_0)_t&=\frac{ed}{2N_2},\\
e(P_z)_t+hA_t(P_z)_\lambda&=0,
\end{aligned}
\qquad M=m''/2-(m')^2/m\ne0.
\tag{3}
\]
Every identity in (3) comes from273 with its actual scalar calibration.
No individual polynomial coefficient is being specialized here.

## 2. An exact formal parameter change

Set \(g=N_2e^2\in F^*\) and define
\[
\zeta=g\lambda+n_1e^2-e'U=-A(U).
\tag{4}
\]
Keeping \(U\) fixed gives the exact inverse
\[
\lambda=\frac{\zeta-n_1e^2+e'U}{g}.
\qquad F[U,\lambda]=F[U,\zeta].
\tag{5}
\]
Thus (4) is a polynomial automorphism over the coefficient field \(F\).
It is affine in the two formal variables and preserves total-degree
bounds. It is not asserted to be an automorphism of the original
complex polynomial four-ring.

On \(F[U,\lambda]\), the \(t\)-derivative that fixes \(U,\zeta\) is
\[
\mathcal D
=\partial_t-\frac{\zeta_t}{g}\partial_\lambda
=\partial_t-\frac{2MU+b_1}{N_2}\partial_\lambda.
\tag{6}
\]
Indeed \(\zeta_t=-A_t=e^2(2MU+b_1)\), while
\(\zeta_\lambda=g\). Equation (6) restricts to the given prime
derivative on \(F\), kills \(U,\zeta\), and therefore is exactly the
coefficientwise derivative in the polynomial ring \(F[U,\zeta]\).
This identifies the held variables explicitly, rather than silently
continuing the old fixed-\(\lambda\) convention.

The last identity in (3), using \(h/e=m^2/N_2\), gives
\[
\mathcal D P_z
=(P_z)_t-\frac{2MU+b_1}{N_2}(P_z)_\lambda=0.
\tag{7}
\]
Express \(P_z\) in the algebraically independent variables \(U,\zeta\).
Their monomials are linearly independent over \(F\), so (7) says that
each coefficient has zero prime derivative. The exact constant-field
statement now proves
\[
\boxed{P_z(U,\lambda)=Q(U,\zeta),\qquad
Q\in\mathbb C[U,\zeta],\quad\deg_{\rm total}Q\le2.}
\tag{8}
\]
No assumption \(F=\mathbb C(t)\) is needed for this coefficient argument.

## 3. The cubic potential and its full integration constant

Rewrite \(B_0\) in \(F[U,\zeta]\), and denote the rewritten polynomial
by \(\widehat B\). Since \(\partial_\zeta=g^{-1}\partial_\lambda\)
with \(t,U\) fixed, the first identity in (3) gives
\[
\widehat B_\zeta=Q(U,\zeta).
\tag{9}
\]
The other derivative, now fixing \(U,\zeta\), is
\[
\begin{aligned}
\mathcal D B_0
&=(B_0)_t-\frac{2MU+b_1}{N_2}(B_0)_\lambda\\
&=(B_0)_t-e^2(2MU+b_1)P_z
 =(B_0)_t+A_tP_z
 =\frac{ed}{2N_2}\in F^*.
\end{aligned}
\tag{10}
\]

For a direct treatment of every integration constant, let
\[
G_0(U,\zeta)=\int_0^\zeta Q(U,s)\,ds
\in\mathbb C[U,\zeta].
\]
This is formal polynomial integration in characteristic zero, and
\(\deg_{\rm total}G_0\le3\). Equation (9) says
\(\widehat B-G_0=R(U)\in F[U]\), of degree at most three.
By (10), \(R_t(U)=ed/(2N_2)\) is independent of \(U\).
Consequently every positive-\(U\)-degree coefficient of \(R\) is
complex. Its constant coefficient may vary in \(F\).

Write \(R(U)=R_0(U)+T\), where
\(R_0\in\mathbb C[U]\) has zero constant coefficient and \(T\in F\).
With \(G=G_0+R_0\), this proves
\[
\boxed{
\widehat B=G(U,\zeta)+T,\quad
G\in\mathbb C[U,\zeta],\quad
\deg_{\rm total}G\le3,\quad
G_\zeta=Q,\quad T'=\frac{ed}{2N_2}\ne0.
}
\tag{11}
\]
In particular the polynomial \(R_0(U)\), the integration constant
with respect to \(\zeta\), has not been discarded.

## 4. Evaluated normal form and precise boundary

Evaluate (4) at the actual intercept \(U=y\), still only in the
function field \(K\). Equations (2),(8),(11) give
\[
\boxed{
\zeta=N_2e^2\lambda+n_1e^2-e'y\in K,\qquad
z=hx+Q(y,\zeta),\qquad
w=-\zeta z+G(y,\zeta)+T.
}
\tag{12}
\]
Here \(Q,G\) have complex coefficients, but \(h,T\) belong to the
curve field \(F\). Also \(T\notin\mathbb C\), since \(T'\ne0\).
In particular \(F/\mathbb C(T)\) is finite: \(T\) is nonconstant
in the finitely generated one-variable function field \(F/\mathbb C\).
Nothing here proves \(F=\mathbb C(T)\).

For clarity, \(\zeta\) is algebraically independent from \(y\) over
\(F\). The identities in (1),(4) express \(x^2\) as an affine
polynomial in \(y,\zeta\) with nonzero \(\zeta\)-coefficient.
Since \(K=F(y,x)\) has transcendence degree two over \(F\), the
subfield \(F(y,\zeta)\), over which \(x\) is algebraic, also has
transcendence degree two. This is an evaluated field statement,
not an ambient coordinate assertion.

The distinctions remain essential:
\(x,\zeta\in K=\operatorname{Frac}A\) need not belong to \(A\);
(5) is over \(F\), not over \(\mathbb C\); and (12) alone gives
no polynomial inverse for the original four coordinates.
In particular this note does not assert recognition of the
quadratic-first quartic component.

## 5. Verification

The complete saved273 source was read, and the changes of held variables
in (6),(9),(10) were reconstructed directly. The proof uses exact
coefficient comparison and the retained constant-field theorem.
It does not infer polynomiality from finitely many parameter values.
No saved checker was executed, imported, or compiled, and no earlier
source was edited. No unrestricted entry, cancellation, or novelty
claim is made.
