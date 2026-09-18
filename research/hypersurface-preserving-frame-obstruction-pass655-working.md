# Hypersurface-preserving frames cannot bypass the linear-complement test

September 18, 2026. Private working proof. Novelty: UNKNOWN.

For an actual sliced polynomial cylinder, a frame change preserving
the zero-slice hypersurface can make every projected partial commute
if and only if the original slice polynomial already has a constant
directional derivative equal to one. The frame change may be nonlinear
and may act nontrivially on the hypersurface. Requiring it to fix that
hypersurface pointwise does not change the existence criterion.

The constant-normal version remains necessary for formal frame changes.
This is an obstruction to a specified recognition procedure, not a
proof that every slice has the required linear complement. The formal
nonalgebraization principle and the example used below are retained
work, not claimed as new results.

## 1. Setup and polynomial equivalence

Work over a characteristic-zero field k. Fix
\[
B=k[X_0,\ldots,X_n]=A[u],\qquad n\ge1,\qquad
E=\partial_u,\qquad A=\ker E.
\tag{1}
\]
The equality B=A[u] is an actual polynomial product, not a formal or
birational presentation. Let rho:B to A be evaluation at u=0. Then
ker(rho)=(u), A is finitely generated, and A*=k*, since a unit of A
is a unit of B.

For sigma in Aut_k(B), the new ambient frame is Y_i=sigma(X_i).
Its coordinate partials are sigma*partial_i*sigma^(-1). The
[polynomial-frame criterion654](commuting-projected-partials-retraction-recognition-pass654-working.md)
applied to this frame says that all projected partials on A commute
if and only if
\[
e_i^\sigma=\rho(EY_i)\in k\quad\hbox{for every }i.
\tag{2}
\]
Indeed (Y_i-rho(Y_i))/u has residue rho(EY_i) in the actual product.
Only this saved polynomial-frame criterion is imported here.

The following conditions are equivalent:

1. Some polynomial automorphism sigma with sigma((u))=(u) satisfies (2).
2. Some polynomial automorphism sigma fixing u and inducing identity
   on B/(u) satisfies (2).
3. Some constant translation T=sum v_i partial_i satisfies T(u)=1.

In particular the equivalent conditions recognize A as k^[n]. They
do not assert that such a translation or successful frame always exists.

For necessity, let sigma((u))=(u). Since B*=k*,
\[
\sigma(u)=c u\quad(c\in k^*),\qquad
\ker(\rho\sigma)=(u).
\tag{3}
\]
Suppose (2) holds and put T=sum e_i^sigma partial_i. The polynomial
chain rule applied to u(Y)=sigma(u) gives
\[
\rho\bigl((Tu)(Y)\bigr)=\rho\bigl(E(u(Y))\bigr)=c.
\tag{4}
\]
Consequently Tu-c belongs to (u), say Tu=c+uQ with Q in B.
The derivation T is a constant LND. It cannot kill u, since u is
a nonunit and c is nonzero. Put d=deg_T(u)>=1. If Q were nonzero,
the right side would have T-degree d+deg_T(Q)>=d, whereas the left
side has degree d-1. Hence Q=0. Replacing T by c^(-1)T proves3.

For sufficiency, choose linear coordinates Z_1,...,Z_n,t with
T=partial_t. Then
\[
u=t+F(Z),\qquad B=k[Z,u],\qquad A=k[\rho Z].
\tag{5}
\]
The last equality and algebraic independence follow by applying
the isomorphism B/(u) to A. Because the actual product (1) is given,
the assignments
\[
\sigma(Z_j)=\rho Z_j,\qquad \sigma(u)=u
\tag{6}
\]
define a whole polynomial automorphism: both (Z,u) and (rho Z,u)
are coordinate systems of B. It induces identity modulo u. Moreover
E sigma(Z_j)=0 and E sigma(t)=1, since sigma(t)=u-F(rho Z).
Each X_i is a constant linear combination of Z,t, so every E sigma(X_i)
is constant. This proves2, and2 implies1 immediately.

This sufficiency uses B=A[u]. It must not be transplanted to an
arbitrary principal retraction:654 Section5 and648 retain examples
with polynomial abstract image but without this supplied-image product.

## 2. The exact first-jet constraint

Write r_i=rho(X_i), e_i=rho(EX_i), and h_i=rho(partial_i u).
The chain rule for E(u)=1 gives h dot e=1. If a polynomial
automorphism induces identity modulo u, write
\[
\sigma(X_i)=X_i+u k_i,\qquad \kappa_i=\rho(k_i).
\]
Then
\[
e^\sigma=e+\kappa,\qquad h\mathbin{\cdot}\kappa=c-1
\quad\hbox{when }\sigma(u)=cu.
\tag{7}
\]
The second equality follows by expanding sigma(u)=u(X+uk) modulo
u^2 and dividing by u. Thus, for sigma(u)=u, the change is tangential:
h dot kappa=0. For general c it is e^sigma-c e that is tangential.
Preserving the hypersurface pointwise does not require c=1.

These are constraints on first jets, not a polynomial lifting theorem.
For example, in standard coordinates B=k[a,b,c,u], suppose a polynomial
automorphism fixes u, induces identity modulo u, and has
\[
\sigma(a_j)=a_j+uV_j(a,b,c)+O(u^2),\qquad (a_1,a_2,a_3)=(a,b,c).
\]
Its Jacobian determinant is a nonzero constant, equal to one modulo u.
The last row is (0,0,0,1), so expansion gives
\[
1=\det J\sigma=1+u\sum_j\partial_{a_j}V_j\pmod {u^2}.
\tag{8}
\]
Therefore div(V)=0 is necessary. It is not claimed sufficient.

## 3. Precisely what extends formally

Let Bhat be the u-adic completion A[[u]], with evaluation rhohat
at u=0. The derivation E=partial_u extends continuously: it lowers
u-adic order by at most one. Consider a continuous k-algebra
automorphism sigma of Bhat with sigma((u))=(u). It need not preserve
B, fix u, or induce identity on the zero fiber. We claim only:
\[
\widehat\rho(E\sigma(X_i))\in k\ \hbox{for all }i
\quad\Longrightarrow\quad
\text{a constant translation }T\text{ on }B\text{ has }T(u)=1.
\tag{9}
\]
This is a constant-normal statement. We do not silently identify a
formal frame with a polynomial frame or apply654 to formal partials.

To prove (9), write sigma(u)=uU for a unit U in Bhat. Its residue
c=rhohat(U) lies in A*=k*. If alpha is the induced automorphism of
A=Bhat/(u), then for b in B,
\[
\widehat\rho(\sigma(b))=\alpha(\rho(b)),\qquad
\ker\bigl((\widehat\rho\sigma)|_B\bigr)=(u)B.
\tag{10}
\]
Set v_i=rhohat(E sigma(X_i)) and T=sum v_i partial_i. The finite
polynomial expression for u in the X_i and the continuous chain rule
give rhohat(sigma(Tu))=rhohat(E(uU))=c. Equation (10) yields
Tu-c in uB, not merely uBhat. The same T-degree argument used above
gives Tu=c, proving (9) after rescaling. Higher coefficients of U
are unrestricted and play no role. Conversely condition3 of Section1
already supplies a polynomial automorphism, so it also supplies a
formal one with this constant-normal property.

There is nevertheless considerable formal first-jet freedom. For
any V in Der_k(A), extend V to Bhat by V(u)=0. Then
\[
\tau=\exp(uV),\qquad \tau^{-1}=\exp(-uV)
\tag{11}
\]
are well-defined continuous automorphisms: uV raises u-adic order,
and each coefficient of either series is a finite sum. They fix u,
induce identity modulo u, and change e_i to e_i+V(r_i).
Every kappa with h dot kappa=0 arises this way at first order. Indeed
the assignments X_i to kappa_i define a k-derivation B to A through
rho; the condition makes it vanish on u and hence on (u), so it
descends to a derivation V of A with V(r_i)=kappa_i.

Formal tangential freedom therefore does not remove the constraint
that a CONSTANT target vector v satisfy h dot v=1. For a constant
translation this congruence already forces Tu=1 in B.

For a concrete failure of polynomial jet lifting, reuse the map from
[lifting-route](lifting-route.md), in renamed variables:
\[
\tau(a)=a+ua^2,\qquad \tau(b)=b,\quad\tau(c)=c,\quad\tau(u)=u.
\tag{12}
\]
It is an automorphism of Bhat and every B/(u^N). Its inverse sends
a to sum_{j>=0}(-1)^j C_j u^j a^(j+1), with C_j the Catalan numbers;
the identity g+ug^2=a determines the coefficients and both inverse
compositions. But its first tangential jet has V=a^2 partial_a and
div(V)=2a. By (8), no polynomial automorphism fixing u has even this
same first jet on a,b,c. This is stronger than just observing that
the particular series is infinite, but it is not an obstruction to
the explicit polynomial construction (6) when its hypothesis holds.

## 4. Actual controls and scope

The two controls in654 separate the conclusions. For
E=y partial_x+partial_t and u=t, the frame change
\[
\sigma(x)=x-ty,\quad\sigma(y)=y,\quad\sigma(z)=z,\quad\sigma(t)=t
\]
fixes the zero fiber pointwise and has whole inverse x to x+ty.
It changes the nonconstant normal vector (y,0,0,1) to (0,0,0,1).
Here the old constant translation partial_t already slices u.

In contrast set v=y+x^2 and u=x+v^2, with z,t unchanged. These are
actual coordinates, with x=u-v^2 and y=v-(u-v^2)^2. The actual LND
E=partial_x-2x partial_y kills v and satisfies E(u)=1. For a constant
translation T with x,y coefficients alpha,beta,
\[
T(u)=\alpha+v(4\alpha x+2\beta).
\tag{13}
\]
Algebraic independence of x,v makes T(u)=1 impossible. Sections1
and3 thus exclude every polynomial hypersurface-preserving repair,
and every formal such repair with constant normal coefficients.
The unrestricted actual frame (u,v,z,t) works; its defining
automorphism does not preserve the original ideal (u). The slice
and its zero hypersurface are fixed throughout our negative statement.

The general warning about formal algebraization is already in
[lifting-route](lifting-route.md),
[critical-plane642](critical-plane-formal-action-nonalgebraization-pass642-working.md)
and [specified-retraction647](kr-retraction-zariski-etale-gap-pass647-working.md).
The latter two concern different prescribed data and do not prove
the stabilizer equivalence above. Here the no-linear-complement
case fails at the desired first jet, before any global algebraization
question. No universal successful nonlinear frame is constructed.

The author reread654 in full and the relevant retained formal controls,
and challenged (9) allowing both a nonidentity residual automorphism
alpha and an arbitrary formal unit U. The proof handles both; replacing
U itself by a scalar would have been an unjustified restriction.
The complete 235-line source at SHA256
47912d8f65171ee6debb7aba0a9a2cbc70a3b7faa27a9013433a24a760d75deb
was read through EOF by root in7ffd27 and independently by Jet inbcddde.
Both reconstructions found no gap. Jet's fresh unsaved59acf0 checked
both whole inverse orders, positive repair, normal identities, and
both formal inverse compositions modulo u^10. Root's fresh unsaved
7a366d separately checked both formal compositions at orders3,5,8;
the nonlinear coordinate identities were checked in764d11. The
uniform formal and polynomial claims have the written proofs above,
not merely these finite controls.

Status: internally checked scoped theorem, not human expert review
or formal certification. No saved checker was run, imported, compiled
or changed. No novelty, universal recognition, or cancellation
conclusion is asserted.

Scope update: [criterion656](three-commuting-projected-partials-unit-normal-recognition-pass656-working.md)
requires only a commuting complementary basis. It succeeds on the
nonlinear control in Section4 without repairing all projected
fields. The stabilizer obstruction here concerns the stronger
all-fields/constant-normal target, not that later weaker criterion.
