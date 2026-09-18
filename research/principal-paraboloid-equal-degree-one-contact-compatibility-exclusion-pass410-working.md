# The nonconstant contact family is incompatible with the first potential

Working conditional exclusion in the supplied actual264
equal-degree-one chart. Assume the contact family of409, together
with its exact original high-H equation and beta relation. The
existence of the actual coefficient function n then forces an
impossible mixed-partial identity.

The proof retains arbitrary t in the exact coefficient field.
It neither assumes a rational coefficient-field presentation nor
promotes a field parameter to an ambient coordinate. This note
does not compose the earlier branches into a general degree-one
classification.

## 1. Complete actual input and precise conditional family

Retain every actual hypothesis of
[401](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md)
and the nonconstant contact family in
[409, Section 4](principal-paraboloid-equal-degree-one-contact-reduction-pass409-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,\qquad
a_0=EX\ne0,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the full kernel},\qquad
0\ne N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad k=s,\qquad n_{ss}\ne0,\\
O=L[P]=L[y,\sigma,\theta]=L[y,z,w],\quad P=\sigma,\quad
NP=\rho\in L^*,\\
\operatorname{Frac}A_0=L(P)=\mathbb C(y,z,w),\qquad
y=\lambda P+r,\quad\theta=\mu P+h,\quad\mu\in L^*.
\end{gathered}
\tag{1}
\]
Thus sigma and theta both have intrinsic degree one. The original
global slice, both returns, full initial kernel, literal selected
partial, genuine levels and calibrated nonzero full scalar all
remain imposed. The contradiction below uses only a necessary
subset of their coefficient equations.

The subscripts t,s refer to the original exact coefficient partials.
Put
\[
\nu=n_s,\qquad
\mathscr D=\partial_t+\mu\partial_s,\qquad
\delta=\lambda-\nu,\qquad
\beta=\mathscr D\nu=n_{ts}+\mu n_{ss}.
\]
In the conditional branch of409, delta and beta are nonzero and
\[
\xi=\lambda,\qquad A=\delta/\beta=t+q\ne0.
\tag{2}
\]
The two original necessary equations to be used are
\[
\boxed{
\begin{aligned}
n_{tt}+2\mu n_{ts}+\mu^2n_{ss}&=4\xi\nu-2\xi^2,\\
\beta&=(\xi-\nu)/A.
\end{aligned}}
\tag{3}
\]
The first is the genuine H quadratic coefficient, not a freely
chosen differential equation. The second retains the original
meaning of A, rather than treating it as an unrelated parameter.

By the contact-family hypothesis, q,xi are a separating coefficient
basis, L is finite over C(q,xi), and
\[
\boxed{
\begin{gathered}
A=t+q,\qquad
\mu=B_q-4\xi A,\qquad
s=-2\xi A^2+A B_q-B,\\
B\in\mathcal F:=\ker_L(\partial_\xi|_q),\qquad
[\,\mathcal F:\mathbb C(q)\,]<\infty.
\end{gathered}}
\tag{4}
\]
Here partial_q and partial_xi at fixed q are the unique commuting
extensions of the coordinate partials of C(q,xi). From now on,
q and xi subscripts always mean these new partials. They are not
the old t,s partials or the characteristic operator Dscript.
Their joint constants are C. The field F need not equal C(q).

No formula for t as a rational function of q,xi is assumed.
It remains an arbitrary retained element of L subject to the
displayed necessary equations. In particular its q and xi
derivatives will not be discarded.

## 2. Exact differential identities with arbitrary t

All differentials in this proof are over C in the coefficient
field L. The forms dq,dxi are a basis because q,xi are a
separating transcendence basis; the old dt,ds are a basis as well.
Thus one may change basis without imposing a rationality ansatz.

Put C=B_qq-4xi, an auxiliary field element for which no nonzero
assumption is made. Differentiating (4), using dA=dt+dq, gives
\[
\boxed{
\begin{aligned}
ds-\mu\,dt&=A C\,dq-2A^2\,d\xi,\\
d\mu&=C\,dq-4\xi\,dt-4A\,d\xi.
\end{aligned}}
\tag{5}
\]
Every derivative of t is still present through dt. For example,
the first identity follows by collecting the dA coefficient as
mu and the dq coefficient as A(B_qq-4xi).

Define an actual coefficient element
\[
\mathcal W:=\mathscr Dn=n_t+\mu\nu\in L.
\tag{6}
\]
This symbol is not the ambient W or its original intercept w.
The old Hessian symmetries give
\[
\begin{aligned}
d\mathcal W
 &=d(n_t)+\mu\,d\nu+\nu\,d\mu\\
 &=(n_{tt}+2\mu n_{ts}+\mu^2n_{ss})\,dt
        +\beta(ds-\mu\,dt)+\nu\,d\mu.
\end{aligned}
\]
Substituting (3),(5) and A*beta=xi-nu yields
\[
\boxed{
d\mathcal W
 =-2\xi^2\,dt+\xi C\,dq-2A(\xi+\nu)\,d\xi.
}
\tag{7}
\]
In particular the coefficient of dq in this identity has no
remaining nu term. This cancellation uses the exact beta relation
in (3).

## 3. Define the auxiliary functions inside L

Define, rather than adjoin an antiderivative,
\[
\boxed{
J=\mathcal W+2\xi^2t-\xi B_q+4\xi^2q\in L.
}
\tag{8}
\]
The letter J in this note is a coefficient function, not the
calibrated Jacobian. Differentiate its explicit definition with
(7) and B_xi=0. The dt and dq terms cancel exactly:
\[
dJ=[\,2A(\xi-\nu)+4\xi q-B_q\,]\,d\xi.
\]
Consequently
\[
\boxed{
J_q=0,\qquad
2A(\xi-\nu)=B_q-4\xi q+J_\xi.
}
\tag{9}
\]
This only puts J in the exact kernel of the q partial; it does not
assert that J is rational in xi. Commutation implies that all of
its xi derivatives are also killed by partial_q.

The definition (8) also gives
\[
\mathcal W=-2\xi^2t+\xi B_q-4\xi^2q+J.
\]
Since mu=B_q-4xi(t+q), it follows that
\[
n_t=\mathcal W-\mu\nu
       =2\xi^2t+J+\mu(\xi-\nu).
\tag{10}
\]
Now define a second actual coefficient element
\[
\boxed{M=n-\xi s-\xi^2t^2-Jt\in L.}
\tag{11}
\]
There is no assertion that a formally closed one-form has a
primitive in L. The function M already exists by (11).

Using dn=n_t*dt+nu*ds, equations (5),(9),(10), and the displayed
formula for s in (4), direct differentiation gives
\[
\boxed{
\begin{aligned}
M_q&=-\frac12(B_{qq}-4\xi)(B_q-4\xi q+J_\xi),\\
M_\xi&=-2\xi q^2+qJ_\xi+B.
\end{aligned}}
\tag{12}
\]
For a detailed cancellation, (10),(11) first give
\[
dM=-(\xi-\nu)(ds-\mu\,dt)
              -(s+2\xi t^2+tJ_\xi)\,d\xi.
\]
Its dq coefficient is the first line of (12) by (5),(9).
Its dxi coefficient is
2A^2(xi-nu)-s-2xi*t^2-t*J_xi. Substituting (4),(9) and
A=t+q reduces it to the second line of (12).
Thus all t dependence cancels without any restriction on t(q,xi).

## 4. Mixed partials are incompatible

Since M belongs to L and the new partials commute,
(M_q)_xi-(M_xi)_q=0. Equations (12), B_xi=0 and J_q=0 make this
the exact identity
\[
\boxed{
\mathcal E:=
B_q+J_\xi+2qB_{qq}-12\xi q
 -\frac12B_{qq}J_{\xi\xi}+2\xi J_{\xi\xi}=0.
}
\tag{13}
\]
It is an identity in the retained field L, not a comparison of
coefficients after assuming either constant field is rational.

Differentiate (13) once in q and once in xi. The cross derivatives
of B and J vanish in the opposite directions, giving
\[
0=\mathcal E_{q\xi}
  =-12-\frac12 B_{qqq}J_{\xi\xi\xi}.
\]
Hence
\[
\boxed{B_{qqq}J_{\xi\xi\xi}=-24.}
\tag{14}
\]
Both factors are therefore nonzero. Differentiate (14) in q.
Because J_q=0 and the partials commute,
\[
B_{qqqq}J_{\xi\xi\xi}=0,\qquad\text{so}\qquad B_{qqqq}=0.
\tag{15}
\]
On the other hand, two q derivatives of (13) give
\[
0=\mathcal E_{qq}
 =5B_{qqq}+\left(2q-\frac12J_{\xi\xi}\right)B_{qqqq}.
\tag{16}
\]
Equation (15) now forces B_qqq=0 in characteristic zero,
contradicting (14). This completes the conditional exclusion.

No branch with B_qqq=0 or J_xixixi=0 was discarded by division:
the necessary equation (14) first excludes both. No integration
to cubic polynomials, algebraic closure of a constant subfield,
or rationality of B or J is needed.

## 5. Scope and verification

The conclusion is that no coefficient family can satisfy (2)--(4)
under the retained actual entry. The obstruction concerns the
nonconstant-q contact family from409. It does not independently
establish the reductions that lead to that family or compose the
constant-q, constant-slope, Delta-zero or characteristic-zero
branches. It makes no claim about larger equal intrinsic degrees,
general coupling, arbitrary initial ideals, original-ring
recognition or unrestricted cancellation.

The original lower functions r,h,ell were never specialized.
Neither the lower scalar coefficients nor an ambient change of
coordinates was used. The contradiction already follows from
the existence of n with its two exact original relations (3)
and the contact presentation (4). This is a necessary-condition
argument, not a proposed realization of the contact coefficients.

The complete held409 source was read through EOF/hash553fe7 at
SHA e2c35e9176cc18ada59b0497bbbf2bf689479c99279db9dad1888f2e42d945ff
before this note was written. The complete401 input had been read
through EOF in d1317b+d7a30a. Fresh unsaved a978c6 retained an
arbitrary function t(q,xi) and independently checked both contact
one-forms, (7), the entire residual dM, and the closure identity
(13), all with zero residual. It also returned exactly the two
derivative expressions used in (14),(16).

Those symbolic identities support, but do not replace, the written
definitions of J,M, the exact-field derivative conventions and
the nonzero-factor argument. Independent full saved-source review
is still required. No saved checker was executed, imported,
compiled or rerun. No held earlier source or canonical index was
edited. No novelty, human-expert review, formal certification or
general cancellation claim is made.
