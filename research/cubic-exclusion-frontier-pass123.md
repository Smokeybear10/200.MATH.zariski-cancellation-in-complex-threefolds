# Exclusion of the supplied exact cubic branch

The exact cubic relative branch is excluded under the actual
original-coordinate and invariant-plane hypotheses90. The null axis
was excluded in122. The remaining non-null axis is now excluded by
a scalar-potential pole bound and two elementary polynomial arguments.
There is no surviving cubic scalar type in that supplied framework.

This is not the general cancellation theorem. The original cylinder
presentation has not been shown to provide the special coordinate
frame used in the argument. The professor's intended field and
dimension also remain unconfirmed. The working target is still the
corrected complex-threefold question A[u]=C^[4] implies A=C^[3].

## 1. Exact scope of the conditional theorem

Retain the actual construction in
[quadratic potential90](nonconical-quadratic-potential-pass90.md)
and [relative degree90](nonconical-cubic-relation-pass90.md).
It starts with actual polynomial coordinates of B=C[x1,x2,x3,z],
a sliced locally nilpotent derivation E, Eu=1, Ex_i=b_i in S,
Ez=qu for a nonzero complex q, and an actual full invariant plane
S=C[s,t]. The moving-frame determinant det[b,b_s,b_t] is nonzero.
The two actual relative generators satisfy
A_K=K[v]=K[y1,y2], where K=Frac(S), and the original-coordinate
volume is a base-field unit. No relative-parameter denominator is
inverted to obtain that unit.

Under these hypotheses, the irreducible plane relation of y1,y2
cannot have total degree three. This is a claim about the supplied
actual generators and full volume identities, not every abstract
affine cubic curve or arbitrary sliced polynomial derivation.

The retained120 reductions put any surviving exact cubic into a
constant-axis normal form. The
[null-axis theorem122](cubic-null-axis-exclusion-pass122.md)
excludes a null axis. The non-null
[constant-coordinate equivalence122](cubic-nonnull-reciprocal-equivalence-pass122.md)
turns the reciprocal scalar type into a cubic scalar. It remains
to exclude the polynomial data g,P,Y with
g squared-D(P/Y)Y squared=1 and D an exact complex cubic.

## 2. The potential gives the missing divisibility

The [potential calculation123](cubic-nonnull-potential-pole-pass123.md)
returns the normalized conic formulas to the h,Y frame, h=P/Y.
It proves, with lambda a nonzero complex constant and a,c in the
possibly larger first-integral field L,

\[
\Psi_0=\lambda g/Y+c,\qquad
z+\frac q2x^tQ(h)x+qC_0x_1
 =\lambda g/Y+c-qa'x_2-q(a-ha')x_3.
\]

The constancy of lambda follows from the actual lower-volume
equations. It is not a normalization of the generic Jacobian.
The normalized derivative fixes the conic variable w, not Y;
the calculation explicitly accounts for this distinction.

The [pole-bound proof](cubic-nonnull-pole-bound-pass123.md)
uses this original-coordinate identity. Along a divisor p of Y
where h has a pole, the leading quadratic coefficient has order
three times the pole order of h. If that exceeds the pole order
of g/Y, reduction gives a nonzero polynomial over C in the residue
of the original coordinate x3. That residue must be constant.
Then p divides x3 minus a constant, and original-coordinate
irreducibility contradicts Ep=0 and Ex3=Y nonzero.

The resulting all-primes statement is

\[
2\nu_p(Y)\le3\nu_p(P)\quad(p\mid Y),\qquad
Y^2\mid P^3,\qquad Y\mid(g^2-1).
\]

The finite-place and derivative estimates retain L=C(H) without
assuming L=C(h). At the equality boundary the reciprocal residue
can survive, so the pole argument alone is not the final exclusion.

## 3. Two polynomial arguments finish the non-null case

If D has a triple root, shift that root to zero by a constant
change P to P-rY. Reduced fractions and Y squared dividing P
cubed then give P=A0 B0 squared C and Y=B0 cubed C, with
A0,B0 coprime. The norm becomes

\[
g^2-1=d_3(A_0B_0)^3C^2.
\]

Every irreducible factor has multiplicity at least two. But a
nonconstant polynomial g cannot have both fibers g=1 and g=-1
made entirely of repeated components. The product of each factor
to one less than its multiplicity would divide every partial
derivative of g while having degree at least deg(g). A nonzero
partial derivative has smaller degree. The
[triple-root proof](cubic-nonnull-triple-root-exclusion-pass123.md)
writes out this contradiction, including preservation of the
divisibility under the constant shift.

If D has two or three distinct roots, the
[nontriple proof](cubic-nonnull-nontriple-exclusion-pass123.md)
uses an independent degree comparison. Write j=Jac(P,Y).
Common factors of P,Y show Y divides j with full multiplicity.
The norm and Euler identity give g Omega=j, with Omega polynomial.
Since g and Y are coprime, gY divides j. Thus nonzero j would imply
deg(g) at most deg(P)-2. The cubic norm gives the opposite bound:
deg(g) at least deg(P), after at most one constant shift of P
to remove a proportional leading form. A cubic without a triple
root has lowest nonzero coefficient index at most two, which
closes the last degree case.

These alternatives exhaust every exact cubic over C. Therefore
the non-null cubic is impossible. Together with the null result
and the retained lower-rank exclusions, this closes the supplied
exact cubic branch. The coefficient controls from121 and122
remain valid as coefficient identities; they fail necessary
actual-frame conditions and are not cancellation counterexamples.

There is also a standalone polynomial consequence: for any exact
cubic D and polynomials g,P,Y in C[s,t] with Y nonzero,
the norm identity together with Y squared dividing P cubed forces
det[b,b_s,b_t]=0. Assuming this determinant nonzero supplies the
nonconstant-ratio hypotheses used in the two arguments above.
This polynomial statement needs no actual four-coordinate frame.
Its historical novelty has not been assessed.

A separate [geometric proof](cubic-nonnull-log-form-obstruction-pass123.md)
excludes the nontriple scalar even without the radical divisor gate.
It explicitly resolves the projective cubic surface and its boundary,
then pulls back a logarithmic two-form to the projective plane.
The pullback would be a nonzero section of O(-2), which is impossible.
The final combined argument above uses the elementary polynomial
proof, so it does not depend on this additional geometric route.

## 4. Additional proved restrictions

Several intermediate results are retained even though the shortest
combined proof does not need them. The
[horizontal-divisor proof](cubic-nonnull-horizontal-divisor-pass123.md)
excludes a divisor of Y carrying a nonconstant finite h-residue;
it specifically excludes the122 speed control at s=0.
The polynomial dual row from the pole bound contracts aY to S.
The [coefficient-globalization proof](cubic-nonnull-coefficient-globalization-pass123.md)
then proves Ya', Pa' and Yc polynomial and makes the entire
Y-multiplied original-coordinate identity polynomial.

The lower scalar relation is also explicit:
c'+q(a'') squared/D''' is complex constant. It is an additional
necessary coefficient identity, not a premise of either final
polynomial exclusion. These results are not counted as separate
solutions of the same cubic branch.

## 5. Verification and the next obligation

The [canonical capture123](verification-pass123-working.json)
records six suites and twelve passing methods: four new and eight
retained. All six input hashes are unchanged. The measured run
took 2.9538412920664996 seconds; unittest reports 2.595 seconds.
The [new checker](cubic_nonnull_potential_checks_pass123.py)
verifies the potential and its original-coordinate identity, the
lower-volume conversion, the polynomial dual row, and the cubic
surface Jacobian identity with its full residual retained.

These finite identities do not prove the all-primes valuation
argument, the degree contradiction, the actual framework, or
cancellation. Those are written mathematical arguments with
separate AI reconstructions. No human expert review, formal proof
checking or novelty clearance has occurred.

Combining this cubic exclusion with the retained case proofs closes
the following working recognition statement:

\[
E\in\operatorname{LND}_{\mathbb C}
  (\mathbb C[x_1,x_2,x_3,z]),\qquad
E^2x_1=E^2x_2=E^2x_3=0,\quad E^2z\in\mathbb C^*
\quad\Longrightarrow\quad \ker E\simeq\mathbb C^{[3]}.
\]

The canonical slice u=Ez/q is automatic. The actual invariant-plane
construction88 puts all three speeds in a polynomial plane. The
[homogeneous-speed theorem89](constant-acceleration-relative-slice-descent-pass89.md)
covers Omega=0, including ranks zero and one and the conical case.
For Omega nonzero, the degree bound90 leaves exact degrees one,
two and three. The [linear case91](nonconical-linear-relation-recognition-pass91.md)
is recognized, the [quadratic shear117](quadratic-velocity-shear-pass117.md)
reduces degree two to the retained
[working nice-slice theorem80](nice-slice-recognition-pass80.md),
and the present argument excludes degree three.

This composition retains the source-dependent and AI-only proof
confidence of those earlier theorems; it is not a fresh independent
audit of every historical source or a published recognition theorem.
A constant linear change also covers any sliced derivation with an
actual polynomial frame whose four second derivatives are complex
constants. A zero acceleration vector uses nice80; a nonzero one
reduces to the displayed form. Nonconstant invariant accelerations,
or merely E cubed killing every generator, are not included.

The next investigation must address what is known for an arbitrary
globally sliced derivation on C^[4], and what would produce a
genuine special coordinate frame or an alternative direct kernel
recognition argument. Merely transporting partial_u through a
cylinder isomorphism does not supply that frame. The full goal
therefore remains active and unsolved.

The remaining entry statement is substantial. In fact, given the
working recognition theorem above, its universal version is equivalent
to the cancellation question. If the kernel is already C[a,b,c],
then B=C[a,b,c,u], and the genuine coordinate frame
(u,a,b,c+q*u^2/2) has exactly the required constant acceleration.
The reverse implication is the recognition theorem. Thus the new
restricted result does not make the universal entry problem a small
technical step or establish that the original conjecture is nearly
solved.

All research artifacts through122 are unchanged. No external
contact, publication, submission, paid resource or new automation
was used. The cited local proofs preserve their original scopes;
their earlier descriptions of a remaining case are historical
intermediate states, not claims that this final combined case
analysis is still unfinished.
