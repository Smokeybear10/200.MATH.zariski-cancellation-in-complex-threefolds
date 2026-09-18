# Exact projection of an approximate coordinate frame need not complete it

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

For an actual polynomial cylinder, projecting three members of an
ambient coordinate frame onto the invariants and adjoining the supplied
slice is an automorphism exactly when a particular coordinate partial
of that slice is a nonzero constant. There is an explicit inverse when
the test succeeds. Arbitrarily high finite-order agreement with a
translation does not force this test to succeed.

This is a criterion and an obstruction to one proposed completion
procedure. It supplies no successful frame for an arbitrary cylinder,
no new recognized kernel, and no solution of complex-threefold
cancellation. The degree argument is already present in654 Section2.
Internal AI reviews and symbolic checks are not formal verification,
human expert review, or a historical novelty audit.

## 1. Hypotheses and statement

Let B=C[z1,z2,z3,z4], let E be a locally nilpotent derivation, and
let s in B satisfy E(s)=1. Put A=ker E. We use the actual cylinder
identity B=A[s] and its finite Taylor retraction

    rho(f)=sum_{j>=0} (-s)^j E^j(f)/j!.

Thus rho is an algebra homomorphism, rho fixes A, rho(s)=0,
ker(rho)=sB, and rho induces B/(s) isomorphic to A.

Let F=(X1,X2,X3,U) be an ACTUAL polynomial coordinate frame on B,
with polynomial inverse, and let D=partial_U in this frame. Set

    H=(rho(X1),rho(X2),rho(X3),s),
    c_F=det JF in C*.

All Jacobians here are taken in the same original z-coordinates.
Then

    det JH = c_F rho(Ds).                              (1)

The following four conditions are equivalent:

1. H is a polynomial automorphism.
2. det JH is a nonzero constant.
3. rho(Ds) is a nonzero constant.
4. Ds is a nonzero constant.

No commutation relation between E and D is assumed. The implication
from2 to1 is special to this setup and is proved below, not taken
from the Jacobian conjecture. A constant-Jacobian F without a supplied
polynomial inverse does not meet the hypotheses.

## 2. The determinant identity

Write Omega=dz1 wedge dz2 wedge dz3 wedge dz4. The polynomial flow
exp(tE) is an automorphism over C[t], with inverse exp(-tE).
Its Jacobian determinant is therefore a unit in C[t,z], hence a
nonzero constant; at t=0 it is one. Consequently E preserves Omega.

The form

    alpha=d(rho X1) wedge d(rho X2) wedge d(rho X3) wedge ds
         =(det JH) Omega

is also E-invariant: E(rho Xi)=0 and the Lie derivative of ds is
d(Es)=d1=0. Since E preserves Omega, this gives E(det JH)=0.
In particular det JH belongs to A and rho(det JH)=det JH.

The finite Taylor formula gives

    rho Xi = Xi-s E(Xi)+s^2 K_i

for some K_i in B. In the module of differentials modulo s,

    d(rho Xi) = dXi-E(Xi) ds mod s.

Wedging the three formulas with ds kills their correction terms.
In the genuine F-coordinates, the coefficient of dU in ds is Ds.
It follows that

    alpha = c_F (Ds) Omega mod s.

Thus det JH-c_F Ds lies in sB. Applying rho and using the
invariance of det JH proves (1).

## 3. Why the unit condition gives a whole polynomial inverse

An automorphism has nonzero constant Jacobian, proving1 implies2.
Equation (1) proves2 equivalent to3. Condition4 implies3 because
rho fixes constants.

Suppose3 holds, and write rho(Ds)=c in C*. Then

    Ds-c=sQ                                             (2)

for some Q in B. Use degree in U in the actual presentation
B=C[X1,X2,X3][U]. The degree r=deg_U(s) is positive, since
otherwise Ds=0 contradicts rho(Ds)=c. The left side of (2)
has U-degree at most r-1, while a nonzero right side has degree
r+deg_U(Q)>=r. Hence Q=0, and Ds=c. This is precisely the
degree-lowering argument used for a coordinate partial in654.
It gives

    s=cU+h(X1,X2,X3)                                   (3)

for a polynomial h. In particular B/(s)=C[X1,X2,X3]. The quotient
isomorphism induced by rho now gives algebraically independent
generators A=C[rho X1,rho X2,rho X3]. Since the ACTUAL product
B=A[s] was supplied, H is a polynomial automorphism.

For completeness, here is its inverse as a point map. Let Gamma_t
denote the polynomial E-flow, with Gamma_t(q) having coordinates
(exp(tE)zi)(q). For target coordinates (Z1,Z2,Z3,S), put

    q0=F^{-1}(Z1,Z2,Z3,-h(Z1,Z2,Z3)/c),
    H^{-1}(Z1,Z2,Z3,S)=Gamma_S(q0).                     (4)

Equation (3) gives s(q0)=0. On that section rho Xi=Xi, while
rho Xi stays fixed under Gamma_S and s increases by S. Therefore
H applied to (4) is (Z1,Z2,Z3,S). Conversely Gamma_{-s(q)}(q)
lies on s=0 with Xi-values rho Xi(q), so it equals the corresponding
q0 by the actual inverse F^{-1}. Applying Gamma_{s(q)} proves
the other inverse identity. Every map in (4) is polynomial.

The proof cannot be transferred wholesale to an arbitrary principal
retraction. In particular B=A[s] and the E-invariance of the volume
form and of rho Xi are used explicitly.

## 4. Failure at every finite normal order, for one fixed translation

Take B=C[a,b,c,u], E=partial_u, s=u and I=(a,b,c), the ideal of
the entire u-axis. For each integer k>=2 define the actual frame

    F_k=(a+b^k(u+a^k), b, c, u+a^k).                   (5)

It is a composition of two polynomial shears. In target coordinates
(X,B_0,C_0,U) its inverse is

    a=X-B_0^k U,
    b=B_0,
    c=C_0,
    u=U-(X-B_0^k U)^k.                                (6)

Substituting (5) in (6), or (6) in (5), gives the identity. Its
Jacobian determinant is one. It fixes the whole u-axis pointwise,
and I=(F_{k,1},F_{k,2},F_{k,3}), since a=F_{k,1}-b^k F_{k,4}.
Moreover

    F_k-(a,b,c,u) belongs to (I^k)^4,
    E(F_{k,1})=b^k in I^k,
    E(F_{k,2})=E(F_{k,3})=0,
    E(F_{k,4})=1.                                     (7)

Thus these are actual frames satisfying the order-k orbit conditions
in698, not merely formal invertible jets. Exact projection, however,
gives

    H_k=(a+b^k a^k,b,c,u),
    det JH_k=1+k b^k a^(k-1).                         (8)

This determinant is nonconstant and even vanishes at a=1 and any
b satisfying b^k=-1/k. Consequently H_k is not an automorphism.
The coordinate partial D_k=partial_{F_{k,4}} also satisfies

    D_k(s)=1+k b^k a^(k-1),

as differentiation of (6) shows. This agrees exactly with (1).

The original action and slice have fixed complexity e=0, d=1, N=2,
independent of k. The forward degree of (5) is 2k and the inverse
degree of (6) is k(k+1). Nevertheless the STANDARD frame already
solves this cylinder at every order with degree one. The example
therefore does NOT lower-bound the minimum degree of a successful
frame and does not refute the hoped-for bound in698.

Nor do all projected generators lose their information. The fourth
projection is rho(F_{k,4})=a^k, and

    a=rho(F_{k,1})-b^k rho(F_{k,4}).

The failure concerns the specified operation of keeping the first
three projections and replacing the fourth coordinate by s.

## 5. What this settles, and what it does not

The criterion supplies an exact test and an explicit inverse for a
chosen frame. It does not show how to choose a frame with Ds in C*.
Existence of such a frame is equivalent to coordinatehood of the
specified slice: one direction is (3), and in the other direction
choose U=s. Under B=A[s], this is the original recognition problem.
The reformulation must not be mistaken for a reduction of that gap.

The all-order example rules out automatic completion of arbitrary
finite-order witnesses by this projection procedure. It leaves open
better choices of frame, nonlinear combinations of all projected
generators, and a genuinely useful global degree estimate.

This concerns projected FUNCTIONS. The criteria in654 and656 concern
projected DERIVATIONS and retain their different hypotheses. The
elementary degree argument is reused from654, not claimed as new.
The rational prescribed-jet control in696 is also different: (5)
is already a polynomial frame at every order, and the failure here
occurs in the subsequent exact projection. No historical originality
or new cancellation case is established.

Supplemental fresh unsaved symbolic checks verified both inverse
orders, det JF_k, det JH_k, D_k(s), the E-residuals, and the displayed
degrees for k=2,3,4,6 in root receipt a587cd. Independent checks used
k=2,3,5 in281d06 and k=2,3,4,5 in3cd680. These finite computations
are checks of the formulas; the all-k proof is (5)--(8). No saved
checker was executed, imported, compiled, or edited.

