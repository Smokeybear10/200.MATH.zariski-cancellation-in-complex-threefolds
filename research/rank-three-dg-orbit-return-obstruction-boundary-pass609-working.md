# A DG orbit-return obstruction and its degree boundary

Date: 2026-09-17

Status: bounded working proof, pending independent saved-source review.
The particular coefficient in Section 5 is not asserted to give a sliced
or an unsliced extension. No cancellation or novelty claim is made.

## 1. Statement and exact scope

Work over C and put R=C[x,y,z]. Fix the explicit homogeneous DG base

\[
f=xz-y^2,\qquad r=x^3+yf,\qquad
g=zf^2+2x^2yf+x^5=\frac{f^3+r^2}{x},\qquad
H=\operatorname{Jac}(f,g,\cdot).
\tag{1}
\]

The quotient expression for g is only an identity: the displayed
expanded expression defines a whole polynomial. This note uses direct
identities for this base, not an imported classification or rank theorem.
For a nonzero ordinary-homogeneous psi of degree ell>=1 consider

\[
E=H+(1+\psi)\partial_t\quad\text{on }B=R[t].
\tag{2}
\]

We prove an exact necessary return-degree condition for E to have a
polynomial slice. We then show that this condition does not impose the
desired full H-degree bound, even for ell=5. More precisely, the return
map below has a homogeneous degree-five element Q with return zero and
deg_H Q=17, whereas the critical degree at ell=5 is 9.

This is a limitation of the specified return test. It is not a
counterexample to a necessary degree bound under the additional
assumption that E is sliced. Sliceness of the extension defined by Q
is not determined here.

## 2. Whole base identities and a generic orbit

The Jacobian definition gives the following entire polynomial identities:

\[
Hf=Hg=0,\qquad Hr=-fg,\qquad Hx=-2fr,
\qquad Hy=6x^2r-g,
\]
\[
Hz=2x(5x^3y+x^2z^2+3xy^2z-4y^4).
\tag{3}
\]

For example, the formula for Hy follows by applying H to
r=x^3+yf and using Hr=-fg. All coefficients of H are homogeneous
of ordinary degree five, so its derivation degree is d=4.

There is a useful exact localization, with both f and g inverted:

\[
x=\frac{f^3+r^2}{g},\qquad
y=\frac{r-x^3}{f},\qquad
z=\frac{g-2x^2r+x^5}{f^2},
\]
\[
R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r],\qquad
H=-fg\partial_r.
\tag{4}
\]

The third expression follows from g=zf^2+2x^2r-x^5. The formulas
show that x,y,z belong to the ring on the right; the opposite inclusion
is immediate. In particular f,g,r are algebraically independent, since
the displayed equality has transcendence degree three. Differentiating
in r kills every polynomial in this ring after sufficiently many steps.
Consequently H is an LND on the original polynomial ring as well.

The leading r-terms in (4) give

\[
\deg_H(x,y,z)=(2,6,10),\qquad N=10.
\tag{5}
\]

For example their respective leading r-coefficients are
g^(-1), -f^(-1)g^(-3), and f^(-2)g^(-5), all nonzero. The triangular
extension E in (2) is also an LND: on t its iterates after the first
are successive H-derivatives of psi.

Take independent parameters v,w, initially invertible, and begin a
base orbit at (0,v,w). Its invariant and local-slice values are

\[
f=-v^2,\qquad g=wv^4,\qquad r=-v^3.
\tag{6}
\]

Write lambda=v/w and let u=r/v^3 be the varying orbit parameter.
Set A=u^2-1. Substituting (6) and r=v^3u in (4) gives the whole orbit

\[
\begin{aligned}
x(u)&=wX_\lambda(u),&X_\lambda&=\lambda^2 A,\\
y(u)&=wY_\lambda(u),&Y_\lambda&=-\lambda u+\lambda^4 A^3,\\
z(u)&=wZ_\lambda(u),&Z_\lambda&=1-2\lambda^3uA^2+\lambda^6A^5.
\end{aligned}
\tag{7}
\]

These are full polynomials in u, not truncated orbit expansions. At
u=-1 and u=1 the points are respectively (0,v,w) and (0,-v,w).
Since Hr=-fg=wv^6, the actual time parameter tau satisfies

\[
\frac{du}{d\tau}=wv^3,\qquad
d\tau=\frac{du}{wv^3},\qquad
\tau_{-1\to1}=\frac{2}{wv^3}.
\tag{8}
\]

Equivalently, each of the three polynomials in (7), differentiated
with respect to u and multiplied by wv^3, equals the corresponding
whole H coefficient evaluated on (7).

There is no loss of generic orbit degree in this parametrization.
The map from C(f,g) to C(v,w) in (6) is injective and finite: v^2=-f
and w=g/f^2, with v,w independent. Over this finite coefficient
extension, r=v^3u is an invertible linear scaling of the independent
variable r. Thus for every nonzero homogeneous psi,

\[
\deg_H\psi
=\deg_u\psi\bigl(wX_\lambda,wY_\lambda,wZ_\lambda\bigr)
=\deg_u\psi\bigl(X_\lambda,Y_\lambda,Z_\lambda\bigr).
\tag{9}
\]

In the last expression the coefficient field is C(lambda); ordinary
homogeneity has removed the nonzero factor w^ell. This is a dominant
generic-invariant specialization, not evaluation on a single special
orbit or a finite collection of numerical orbits.

## 3. The entire return polynomial

Define the linear map on the ordinary homogeneous piece R_ell by

\[
P_\psi(\lambda)=\int_{-1}^{1}
 \psi\bigl(X_\lambda(u),Y_\lambda(u),Z_\lambda(u)\bigr)\,du
\ \in\mathbb C[\lambda].
\tag{10}
\]

This integral means evaluation of a polynomial antiderivative. It
involves neither convergence nor a chosen analytic orbit. If the
integrand is sum c_ij lambda^i u^j, its exact value is
sum over even j of 2c_ij lambda^i/(j+1).

Start the entire E-orbit at (0,v,w,0). Its t-displacement at the second
base endpoint, using ordinary homogeneity and (8), is exactly

\[
\Delta t=\frac{2+w^\ell P_\psi(v/w)}{wv^3}.
\tag{11}
\]

Every lower coefficient of psi contributes to (10)--(11). A high
u-degree term can integrate to zero, so the degree of P is not
identified with deg_H psi.

## 4. A formal endpoint obstruction

Suppose P=P_psi is nonzero of degree K>ell. Write
P(lambda)=sum from j=0 to K of p_j lambda^j, with p_K nonzero.
Introduce a formal parameter s and substitute

\[
w=s^K,\qquad v=s^{K-\ell}V(s).
\tag{12}
\]

The entire numerator of (11) then vanishes precisely when

\[
2+p_KV(s)^K+
\sum_{j<K}p_j s^{\ell(K-j)}V(s)^j=0.
\tag{13}
\]

Choose a nonzero complex V0 satisfying 2+p_K V0^K=0. Its derivative
in this equation is K p_K V0^(K-1), which is nonzero. Formal
coefficient recursion therefore gives V(s) in C[[s]] with V(0)=V0
and (13) identically zero. This is an actual formal solution, not just
a leading-order cancellation.

Both entire endpoint arcs

\[
(0,s^{K-\ell}V(s),s^K,0),\qquad
(0,-s^{K-\ell}V(s),s^K,0)
\tag{14}
\]

belong to C[[s]]^4. The t-coordinate returns to zero by (11)--(13),
whereas their actual flow time is

\[
\tau=2s^{-(4K-3\ell)}V(s)^{-3}.
\tag{15}
\]

It has a pole: 4K-3ell>0 and V(s) is a unit. The finite polynomial
E-flow is defined over C((s)), so all these endpoint equalities are
legitimate even though the flow time is not integral.

If a polynomial S in B satisfied ES=1, its finite flow identity would
give S(endpoint two)-S(endpoint one)=tau. The left side belongs to
C[[s]], while (15) does not. This proves the necessary condition

\[
E\text{ sliced}\quad\Longrightarrow\quad
P_\psi=0\ \text{or}\ \deg P_\psi\le\ell.
\tag{16}
\]

The proof requires no properness theorem, external action
classification, rational parametrization of V(s), or polynomial slice
for H. It concludes nonsliceness only when the stated return-degree
hypothesis holds.

## 5. An overcritical element with identically zero return

Take ell=5 and the entire polynomial

\[
Q=-43x^3yz+4x^2y^3-13x^2z^3-13xy^2z^2+26y^4z.
\tag{17}
\]

For A=u^2-1 the exact whole substitution from (7) is

\[
\begin{aligned}
Q(X_\lambda,Y_\lambda,Z_\lambda)
={}&-39\lambda^{13}uA^8
 +9\lambda^{10}A^5(13u^2-1)\\
 &-\lambda^7uA^2(117u^2-61)
 +13\lambda^4(3u^2-1).
\end{aligned}
\tag{18}
\]

Its u-degree is 17, with leading coefficient -39lambda^13. Equation
(9) therefore gives the exact equality deg_H Q=17.

Here is a whole antiderivative certificate for the return, retaining
all four powers of lambda:

\[
\begin{aligned}
J(\lambda,u)={}&-\frac{13}{6}\lambda^{13}A^9
 +9\lambda^{10}uA^6\\
 &-\lambda^7\left(\frac{117}{8}A^4+\frac{28}{3}A^3\right)
 +13\lambda^4uA.
\end{aligned}
\]
\[
\partial_uJ=Q(X_\lambda,Y_\lambda,Z_\lambda),\qquad
J(\lambda,-1)=J(\lambda,1)=0.
\tag{19}
\]

Thus P_Q is identically zero. In this example d=4, ell=5, q=ell-d=1,
and N=10, so

\[
\deg P_Q=-\infty\le5,\qquad
\deg_H Q=17>qN-1=9.
\tag{20}
\]

Consequently the return-degree condition (16) does not imply the
critical full-degree bound on the space of homogeneous coefficients.
In particular no proof may replace the required generic orbit-degree
calculation by the degree of this single return polynomial.

For Q the numerator in (11) is simply 2, so the zero-return formal
construction in Section 4 does not apply. That observation is not a
sliceness or a nonsliceness proof for H+(1+Q)partial_t. Other endpoint
families or other equations could impose further conditions.

## 6. Verification and limits

Fresh unsaved exact algebra reconstructed the entire Jacobian H,
all invariant identities and the three differential equations for
(7). A separate full substitution checked (18), its leading term,
and the vanishing of all four integrated coefficients. Equation (19)
is an explicit independently differentiable certificate for that zero.

As supplementary finite linear-algebra evidence, the 21 degree-five
monomials were substituted into the entire polynomials (7). Taking
every coefficient of lambda^i for i>5 in the integrated result gave
a 13 by 21 matrix of rank 13, hence an eight-dimensional space with
return degree at most five. Taking every u-degree greater than nine
in the unintegrated result gave rank 15, hence a six-dimensional
space with H-degree at most nine. These counts do not replace the
explicit counterexample (17)--(20), and no claim about sliceness is
drawn from either nullspace dimension.

The formal obstruction (16) is uniform in homogeneous psi. The
failure (20) is one exact coefficient-space counterexample. Neither
asserts a classification of sliced extensions, a failure of the
degree bound under sliceness, an entry theorem for arbitrary sliced
actions on C^[4], or a cancellation conclusion.

No saved checker was executed, imported, or compiled. No canonical
file or other author's source was changed.
