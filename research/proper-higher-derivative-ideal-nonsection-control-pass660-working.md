# A proper higher-derivative ideal can pass without a graph section

Date: September 18, 2026. Private working control. Novelty: UNKNOWN.

The necessary ideal test659 can pass with a PROPER NONZERO ideal even
though no polynomial slice shift and no constant linear ambient frame
achieves a unit projected normal. This happens on an explicitly
rectified polynomial cylinder, uniformly in the family below. Taking
q=b makes the ideal radical as well. Thus retaining the full ideal,
although necessary in659's control, does not make the test sufficient.

This concerns a specified section-lifting and frame-repair route. It
does not obstruct cancellation, the existence of intrinsic LNDs, or
recognition by unrestricted nonlinear coordinates.

## 1. Exact family and whole inverse

Let k be a field of characteristic zero. Let q in k[b] be nonconstant
and let F in k[x] have degree at least two. Starting with the whole
coordinates (a,b,c,u), set
\[
x=a+q(b)u,\qquad y=b,\qquad
z=c+q(b)u^2,\qquad t=u+F(x).
\tag{1}
\]
These are polynomial coordinates, with the entire inverse
\[
u=t-F(x),\qquad b=y,\qquad
a=x-q(y)\bigl(t-F(x)\bigr),\qquad
c=z-q(y)\bigl(t-F(x)\bigr)^2.
\tag{2}
\]
Substitution in either direction recovers each of the four variables.
Consequently, on B=k[x,y,z,t]=k[a,b,c,u], the derivation
\[
E=q(y)\partial_x+2q(y)\bigl(t-F(x)\bigr)\partial_z
  +\bigl(1+q(y)F'(x)\bigr)\partial_t
\tag{3}
\]
is exactly partial_u. In particular it is a whole LND with slice u,
and its kernel is A=k[a,b,c]. No local-coordinate or formal argument
is used to establish this action.

Every polynomial slice of this same E is u_h=u+h(a,b,c), with h in A.
The associated invariant retraction rho_h substitutes u=-h and fixes A.
Constant affine translations of an ambient frame have no effect on
the projected normal or projected partials.

## 2. The full higher-derivative ideal is proper and the test passes

The coordinate derivatives are
\[
Ex=q,\quad Ey=0,\quad Ez=2qu,\quad Et=1+qF'(x),
\]
\[
E^2x=E^2y=0,\quad E^2z=2q,\quad E^3z=0,\qquad
E^j t=q^jF^{(j)}(x)\quad(j\ge2).
\tag{4}
\]
Here q means the same invariant q(y)=q(b). Since 2 is invertible,
the FULL ideal from659 is exactly
\[
J=(E^jX_i:j\ge2)B=qB,\qquad I=J\cap A=qA.
\tag{5}
\]
It is nonzero and proper because q is nonconstant. The contraction
identity follows immediately from B=A[u] and q in A. It permits
repeated or reducible q and needs no normality argument.

The ambient necessary test659 passes: take lambda_t=1 and every
other coefficient zero, since
\[
Et-1=qF'(x)\in J.
\tag{6}
\]
Equivalently the normal residues modulo I are (0,0,0,1). Thus this
is not the vacuous J=B case. In particular q=b gives a proper nonzero
RADICAL ideal J=(y), while (6) still holds.

## 3. No polynomial shift and linear frame has even a unit normal

At an arbitrary shifted slice u_h=0, the exact normal is
\[
e^h=\bigl(q,0,-2qh,1+qF'(a-qh)\bigr).
\tag{7}
\]
If some constant linear ambient frame had a unit omitted normal,
rescaling its first row would give constants lambda with lambda e^h=1.
Reducing that equality modulo q forces lambda_t=1. Indeed q is a
nonconstant polynomial in b, so k embeds into A/qA. Cancelling the
nonzero q then gives the necessary equation
\[
\lambda_x+F'(a-qh)-2\lambda_z h=0.
\tag{8}
\]
The unused lambda_y is arbitrary and cannot affect this equation.
We now rule out (8) for every polynomial h and all constants.

### 3.1 Quadratic F

Write F'(T)=alpha T+beta with alpha in k* and beta in k. Equation (8)
would imply
\[
\bigl(\alpha q+2\lambda_z\bigr)h
  =\alpha a+\beta+\lambda_x.
\tag{9}
\]
The coefficient alpha q+2lambda_z is nonconstant in b for every
lambda_z. Reduce (9) modulo that polynomial. The coefficient alpha
of the independent variable a remains a nonzero scalar, so its
right side cannot vanish. This is a contradiction, whether or not
the polynomial defining this quotient has repeated factors.

### 3.2 Degree F at least three

Put m=deg F'>=2 and compare degrees in a over the domain k[b,c].
If h is independent of a, then a-qh has a-degree one, and the term
F'(a-qh) in (8) has degree m, while the other terms have degree zero.
If h has a-degree d>=2, then a-qh has degree d and F'(a-qh) has
degree md>d, again impossible in (8).

It remains to consider h=h_1(b,c)a+h_0(b,c), with h_1 nonzero.
The coefficient 1-qh_1 is nonzero, because the nonconstant q cannot
be a unit in k[b,c]. Hence a-qh has degree one and F'(a-qh) has
degree m>=2, whereas the other terms in (8) have degree at most one.
This is the final contradiction.

Thus no polynomial h and no constant lambda solve the unit-normal
equation. This rules out ALL constant linear ambient frames after
ALL polynomial slice shifts, before even imposing complementary
commutation. In particular the stronger certificate656 cannot
succeed through those operations. The classification concerns the
slice retractions of the supplied E, not all principal retractions.

## 4. What the extra elementary shear changes

The family658 has x=a+qu, y=b, t=u+F(x), with the fourth coordinate
c unchanged. For nonlinear F its higher-derivative ideal is contained
in (q^2). Its no-unit-normal obstruction was already visible modulo
that higher-order ideal: a constant normal equal to one modulo q^2
would force lambda_t=1 and then F'(a)+lambda_x=0 modulo q, which is
impossible by its nonconstant a-dependence.

The present frame changes only the fourth coordinate to z=c+qu^2.
This is an actual elementary polynomial shear because q and u are
polynomials in the unchanged coordinates x,y,t. It introduces the
acceleration E^2z=2q, making the full ideal exactly (q), and thereby
makes659's necessary test pass. Nevertheless Section3 proves that
the required polynomial graph section still does not exist for any
constant normal direction. This is the precise additional boundary.

There is also no contradiction with nonlinear recognition: the whole
inverse (2) restores the already known adapted coordinates (a,b,c,u).
The embedded invariant ring has been polynomial throughout.

## 5. A formal and localized graph does exist in the smallest control

Specialize q=b and F=x^2. For eta in k* take the constant direction
ell=t+eta z. In the product coordinates,
\[
E\ell-1=2b\bigl(a+(b+\eta)u\bigr).
\tag{10}
\]
The graph u=-h is therefore a section after the localization
A -> A[(b+eta)^{-1}], with
\[
h=\frac{a}{b+\eta}
 =\frac a\eta\sum_{j\ge0}\left(-\frac b\eta\right)^j
 \quad\text{in }\varprojlim_N A/(b^N)=k[a,c][[b]].
\tag{11}
\]
The denominator is a unit in the b-adic completion because eta is
nonzero. These formulas give compatible graph sections at every
finite b-adic order, as well as a regular graph over D(b+eta).
But h is not in A: b+eta does not divide a. Section3 proves more
strongly that changing the constant direction cannot produce any
global polynomial graph section either.

Only the unit-normal graph condition is asserted in this paragraph.
No commuting projected frame, algebraic additive action on a formal
quotient, or general formal-algebraization theorem is inferred from
(11). The distinction here is between a local or formal section and
a global polynomial one.

## 6. Antecedents and verification scope

The base curvature control is from22. The uniform family without the
extra fourth-coordinate shear is classified in658. Note659 supplies
the necessary higher-derivative quotient test and explicitly does not
claim sufficiency. Its normalizer correspondence also applies, so
the present no-unit-normal result excludes frame changes preserving
the supplied embedded A, as well as the slice/linear operations above.
It does not exclude arbitrary nonlinear changes moving A as a
subalgebra of the fixed ambient ring.

The full source124 was reread: its acceleration ideal is the unit
ideal, so it does not supply the proper-ideal control here. Targeted
archive searches found no identical construction or uniform statement.
This is a bounded collision check, not a novelty clearance. The
family is not claimed as a new class of varieties or as a cancellation
counterexample.

The whole inverse, every derivative in (4), both all-degree cases of
(8), and the formal identity (10)--(11) were reconstructed directly.
Root, Geometry, and Jet read the complete held source. Both separate
reviewers reported CLEAN. Fresh unsaved exact calculations independently
checked whole inverse orders, symbolic normal formulas, the ideals,
and the printed formal/localized control. The uniform conclusions
are established by the written proof, not those finite calculations.
Reviewed hashes and full-read evidence are recorded in the ledger.
No saved checker was executed, imported, compiled, or modified.
AI review is not human expert or proof-assistant certification.
General cancellation remains UNSOLVED and novelty UNKNOWN.
