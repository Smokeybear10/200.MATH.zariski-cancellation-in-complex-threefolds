# Exact speed-ideal structure in the rank-one acceleration case

The good-speed ideal is extended from the actual three-coordinate
subring, including its nonreduced structure. The acceleration belongs
to its divisorial hull. In particular it belongs to the speed ideal
whenever that ideal is principal. In general, membership in the full
ideal is equivalent to one explicit divergence condition on the
primitive speed row; that condition is not proved automatic here.

This is a bounded original-action deduction, not recognition of every
quadratic-time action or a claim of historical novelty. All files through
pass81 remain unchanged.

## 1. Original hypotheses and notation

Let
\[
B=\mathbb C[x_1,x_2,x_3,z],\quad
E\in\operatorname{LND}_{\mathbb C}(B),\quad Es_*=1,
\quad E^2x_i=0\ (1\le i\le3),\quad E^2z=q,\quad Eq=0.
\tag{1}
\]
Write R=C[x_1,x_2,x_3], let T be the original partial derivative
with respect to z, and put
\[
a_i=Ex_i,\qquad b=Ez,\qquad
E=\sum_{i=1}^3a_i\partial_{x_i}+bT,\qquad
I=(a_1,a_2,a_3)B.
\tag{2}
\]
No a_i is assumed to belong to R. They are E-invariant by (1).
The original slice gives the exact identity
1=sum_i a_i (s_*)_{x_i}+b T(s_*). In particular b is a unit
modulo I, with inverse the class of T(s_*).

If I=0, that identity makes b a unit of B, hence a nonzero complex
constant. Then E=bT, q=0, and the kernel is already R. We henceforth
assume I is nonzero; the unit-ideal case is allowed.

The [pass81 shear boundary](rank-one-acceleration-shear-boundary-pass81.md)
proves q in radical(I) and gives an actual sliced example with
q not in I squared. The present result keeps the full ideal, rather
than replacing it by its radical or by a coefficient gcd.

## 2. The whole speed ideal is extended from R

For each i, invariance of a_i gives
\[
0=E(a_i)=\sum_j a_j\partial_{x_j}a_i+bT(a_i).
\]
Since b is a unit modulo I, T(a_i) lies in I. The derivation rule
then shows T(I) is contained in I. Consequently
\[
T(I)\subseteq I,\qquad I=(I\cap R)B.
\tag{3}
\]
Here is an elementary proof of the second assertion with no reducedness
premise. If f in I has z-degree n and leading coefficient f_n in R,
then T^n f=n! f_n lies in I. Characteristic zero gives f_n in I cap R.
Subtract f_n z^n and induct on degree. Every coefficient of every
element of I thus belongs to I cap R. The reverse inclusion is immediate.

In particular B/I is the actual polynomial line
(R/(I cap R))[z]. Its base may be nonreduced. The assertion does not
identify that base with a polynomial ring or a smooth variety.

## 3. Dividing the coefficient gcd preserves the required invariances

Choose a coefficient gcd g of the three a_i in the original polynomial
UFD B and write
\[
a_i=g f_i,\qquad \gcd(f_1,f_2,f_3)=1,\qquad
J=(f_1,f_2,f_3)B,\qquad I=gJ.
\tag{4}
\]
Zeros among the entries are allowed. The gcd statement is not a
Bezout assertion that J=B.

We first have E(g)=E(f_i)=0. Indeed, a nonzero entry factors as
g f_i and lies in ker E, which is factorially closed in the domain B.
For completeness, E-degree is additive on products of nonzero elements
in a characteristic-zero domain with an LND. Thus E-degree zero of a
product forces degree zero of each factor. Applying the same argument
to every nonzero entry proves the assertion.

Equation (3) implies g divides T(a_i)=T(g)f_i+gT(f_i), hence g
divides T(g)f_i for every i. Since the f_i have no common irreducible
factor, prime multiplicities in the UFD give g divides T(g). This
argument does not replace gcd one by a multivariable Bezout identity.
If T(g) were nonzero its z-degree would be smaller than that of g,
contradicting that divisibility. Therefore
\[
T(g)=0,\qquad g\in R,\qquad E(g)=E(f_i)=0,\qquad
\sum_i f_i\partial_{x_i}g=0.
\tag{5}
\]
The last equality is E(g)=0 after cancelling the nonzero g in B.

There is a parallel exact extension result for J. The original slice
identity makes b a unit modulo J as well, and E(f_i)=0 gives
bT(f_i)=-g sum_j f_j partial_{x_j}f_i. Thus T(J) is contained
in J. The same coefficient argument proves J=(J cap R)B. It is
still not assumed reduced or the unit ideal.

## 4. The divisorial bound and exact remaining membership test

Every polynomial LND on B has zero divergence in the actual polynomial
coordinates. One direct proof uses its original independent-time flow:
exp(tE) is an automorphism of B[t], its Jacobian determinant is a
unit of B[t], and evaluating at t=0 makes that unit one. Its linear
t coefficient is precisely div(E).

Set d=sum_i partial_{x_i}f_i. Substituting (4) and (5) into the
zero-divergence identity gives
\[
T(b)=-g d,\qquad
q=E(b)=g\left(\sum_i f_i\partial_{x_i}b-bd\right).
\tag{6}
\]
Thus q belongs to gB, the divisorial hull of I in the polynomial UFD.
This uses the full multiplicity of g, not merely its radical.

There is also an exact equivalence, not just a sufficient condition:
\[
\boxed{\ q\in I\quad\Longleftrightarrow\quad d\in J.\ }
\tag{7}
\]
Indeed I=gJ and B is a domain, so q in I is equivalent to q/g in J.
In (6) the first term inside parentheses already belongs to J, and
b is a unit modulo J by the original slice. Therefore q/g lies in
J exactly when d does.

If I is principal, its gcd generates I up to a complex unit, so J=B.
Equation (7) proves q in I. Equivalently, the general formula gives
q in gB=I directly. The zero-ideal case was handled in Section 1.
The countercontrol from pass81 has I=(a^2) and q=a^3, showing this
principal conclusion does not strengthen to q in I squared.

The proof through (7) only requires E^2x_i=0 and the original LND
slice. The additional Eq=0 in (1) is needed for the quadratic-time
interpretation and for the earlier radical-membership argument, not
for the new divisorial identity itself.

## 5. A nonreduced quotient is a genuine remaining gate

The quotient descriptions in Sections 2 and 3 cannot be silently
reduced. Over the ring C[epsilon]/(epsilon squared), the derivation
\[
\delta=(1+\epsilon z)\partial_z,\qquad
\sigma=z-\frac\epsilon2 z^2,\qquad
z=\sigma+\frac\epsilon2\sigma^2
\tag{8}
\]
has a genuine polynomial two-sided coordinate inverse and
delta(sigma)=1. It is therefore an LND. Nevertheless
\[
1+\epsilon z\text{ is a unit},\qquad
\delta^2z=\epsilon\ne0,\qquad \delta^3z=0.
\tag{9}
\]
Thus the domain rule that an LND kills every unit is false in this
nonreduced polynomial line. The original ambient B is a domain; this
control is only about arguments after passing to B/I or B/J. It is
not a lift to an actual action satisfying (1), and is not a
counterexample to q in I in that original setting.

The exact outstanding statement after this reduction is d in J for
the primitive row arising from the original action. The displayed
identities alone are not being promoted to a solution of that statement,
to a fixed-base polynomial presentation of ker E, or to recognition.
Simultaneous coordinate reduction and unrestricted cancellation remain
separate unresolved obligations.

## 6. Verification and attribution

The ideal-extension and principal-ideal arguments were reconstructed
here. Root independently supplied the extension from a principal ideal
to its general coefficient gcd, which was checked with exact prime
multiplicities; the final primitive divergence equivalence was then
derived here. These are coordinated written proofs, not independent
historical discoveries.

The note uses the original polynomial slice, ordinary coordinate
partials, UFD divisibility, E-degree, and the polynomial flow determinant.
It imports no new classification theorem and has no standalone checker,
numerical method, or full-regression claim. Independent written reviews
are separate evidence. No frozen file or shared metadata was changed.
