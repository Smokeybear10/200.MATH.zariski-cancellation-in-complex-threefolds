# Cubic acceleration bound from the actual return map

The rank-one quadratic branch now has a stronger working result:
the acceleration is integral over the full good-speed ideal, and its
third power belongs to that ideal. The proof constructs an explicit
monic equation, not an inference from a finite search. The good-speed
zero set has no isolated points.

The acceleration itself is not proved to belong to the ideal in every
case. No general square-power bound, coordinate reduction, arbitrary
rank-one recognition, or unrestricted cancellation proof is claimed.
These are AI-audited working deductions, not expert-reviewed or
historically certified novel results.

## 1. The unchanged original-action hypotheses

The underlying goal remains the unconfirmed corrected complex-threefold
cancellation implication A[s]=C^[4] implies A=C^[3]. Luo has not
confirmed the correction, dimension or field. The current theorem
assumes the restricted actual polynomial action
\[
B=\mathbb C[x_1,x_2,x_3,z],\quad E\in\operatorname{LND}(B),
\quad E(s)=1,\quad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Set a_i=Ex_i, b=Ez and I=(a_1,a_2,a_3)B. The frozen pass82 proofs
give I=I_0[z], where R=C[x_1,x_2,x_3], I_0=(f_1,f_2,f_3)R and
f_i=a_i(x,0). Write b_0=b(x,0), q_0=q(x,0). Then b_0 is a unit
modulo I_0 and q-q_0 belongs to I. All of these are statements about
the full ideal, including nilpotents.

Unit and zero ideals are treated separately in the detailed proof.
If q_0=0, first-power membership already follows. Assume q_0 is
nonzero for the return-map construction.

## 2. An identity not visible in a quotient matrix

Start the actual flow on z=0. Its fourth coordinate is
t b_0+t squared q_0/2, whose second root is -2b_0/q_0. Substitution
in the original polynomial identities gives a rational return map
\[
\rho=x-2b_0f/q_0,\qquad
f(\rho)=f,\quad q_0(\rho)=q_0,\quad b_0(\rho)=-b_0,
\qquad \rho^2=\operatorname{id}.
\tag{2}
\]
No polynomial inverse or extension across its denominator is asserted.
The sign change is an exact consequence of E(b)=q and E(q)=0.
In particular a nonzero constant b_0 is impossible when q_0 is
nonzero. A formal determinant identity alone does not impose this.

## 3. Explicit integral dependence and the cube

Let D be the ordinary total degree of b_0. It is positive in the
nonzero-q_0 case. Taylor-expand b_0 at x with the direction f held
fixed. Denote its kth frozen directional derivative by H_k. It is
a sum of products of k entries of f with kth partial derivatives
of b_0, so H_k belongs to I_0 to the kth power. The return sign in
(2) gives
\[
q_0^D+\sum_{k=1}^D
\frac{(-1)^k(2b_0)^{k-1}}{k!}
H_k q_0^{D-k}=0,
\qquad H_k\in I_0^k.
\tag{3}
\]
This is a monic ideal-integrality equation in the original polynomial
ring. Derivatives in H_k do not act on f. A separate valuation
argument reconstructs the same conclusion but is not required for
the explicit proof.

The elementary power property of integral dependence and
Lipman--Sathaye's Briancon--Skoda theorem, applied to the actual
three-generated ideal in the regular three-ring, now give
\[
q_0\in\overline{I_0},\quad q_0^3\in I_0,
\qquad q\in\overline I,\quad q^3\in I.
\tag{4}
\]
The [full return-map proof](rank-one-return-map-integral-closure-pass83.md)
checks the Rees/Veronese power step and every theorem hypothesis.
It also proves the section-dependent bound q to the Dth power in I:
degree one gives q in I and degree at most two gives q squared in I.
No such low-degree section is assumed to exist in every action.

Integral closure is genuinely weaker than membership. For example,
xy is integral over (x squared,y squared) but is not in that ideal.
This elementary ideal is a limitation of the inference, not an
actual speed-ideal counterexample.

## 4. Isolated good-speed zeros are excluded

The original flow determinant identifies the cubic acceleration
modulo I_0 with -b_0 cubed times the Jacobian determinant of f.
At an isolated zero of three functions in three variables, the
characteristic-zero Jacobian/socle theorem makes that determinant
nonzero in the local quotient. Since b_0 is a quotient unit, that
would contradict (4).

The [socle note](rank-one-cubic-acceleration-socle-pass83.md) proves
the stronger independent characterization: the annihilator of the
cubic class is the intersection of the maximal ideals of the isolated
points. Combining it with the return proof makes that set empty.
Embedded points on positive-dimensional components are not excluded.

Consequently, the earlier fourth-power upper bound is not sharp for
the actual four-variable class. A formal integrable three-variable
Jacobian can nevertheless satisfy all the old quotient identities
with a nonzero cubic class. The new return identity explains why
that local jet does not lift to an actual action in this class.

## 5. Independent controls and source limits

The [three-method checker](rank_one_return_checks_pass83.py) checks
an actual two-speed polynomial coordinate frame, its rational return,
and its nontrivial frozen Taylor equation. It separately checks a
three-polynomial isolated jet and the nonconstant determinant of its
failed lift, then distinguishes integral closure from membership.
These controls are not a finite verification of a universal theorem.

The [controls note](rank-one-return-controls-pass83.md) records exact
scope. The [targeted capture](verification-pass83-working.json) and
[audit](proof-audits-pass83-working.md) record runs and independent
proof reviews. No search is part of this pass. No fresh full regression
is claimed; the retained full75 record remains 146 suites and 1047
methods, and the historical registry remains 544 claims.

The [primary-source record](primary-source-scope-pass83.md) identifies
the exact algebraic Briancon--Skoda and field-valued socle inputs,
the inspected pages, and the limits of fresh source reconstruction.
The deep-research and PDF workflows were used to verify those premises,
including integral-closure bars missing from some extracted text.
The [checkpoint](checkpoint-pass83-working.json) keeps future work
separate from this result. No outreach, public posting or submission
occurred.

## 6. Remaining mathematical obligation

The next target is still first-power membership or a genuine actual
counterexample, followed by a valid coordinate-reduction or recognition
argument. The return map is not proved regular near every speed zero.
Nor is the speed ideal proved integrally closed or free of embedded
components. Even solving those restricted questions would not supply
a nice frame for an arbitrary cylinder action. The unrestricted
cancellation goal remains open and active.
