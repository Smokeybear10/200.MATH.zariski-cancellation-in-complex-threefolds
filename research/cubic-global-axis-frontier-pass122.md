# Global axis restrictions in the supplied cubic framework

The null constant-axis alternative is excluded under the full actual
original-coordinate hypotheses90. A non-null reciprocal scalar is
equivalent, by a constant change of the original good coordinates, to
a non-null cubic scalar. The remaining supplied type is therefore
non-null cubic, with new restrictions on its polynomial speed divisors.
It is not excluded: a polynomial unimodular speed control survives those
restrictions without supplying an actual frame.

These are conditional results inside the supplied exact cubic framework.
Entry from an arbitrary polynomial cylinder and the general corrected
complex-threefold cancellation problem remain unresolved.

## 1. The null axis cannot occur

The [global reconstruction lemma](cubic-null-global-reconstruction-pass122.md)
starts with the actual null cubic data
b=(g,P,Y), h=P/Y, D=a3 h^3+a2 h^2+a1 h+a0, and
rho=aY+B0/Y. The relative graph element R has the exact polynomial row

\[
2R=2Y^2x_1+(3a_3P^2+2a_2PY+a_1Y^2)x_2
 +(3+4gY+a_2P^2+2a_1PY+3a_0Y^2)x_3.
\]

Thus R belongs to the actual kernel A. The third original coordinate
then gives F0=aY^2 in A intersect K=S. These memberships use the full
invariant kernel and original polynomial coordinates, not just a
rational inverse or a formal coefficient identity.

For any irreducible p dividing the nonconstant Y, the norm relation
forces p to divide P and makes K0=P^3/Y a polynomial with residue
-1/a3. The element a/h^3=F0/K0 is regular at the corresponding pole
of h. Every regular element of the finite field extension L/C(h)
has complex residue at that place. This is proved directly by reducing
a normalized polynomial relation; no equality L=C(h) is assumed.

The polynomial row reduces to 2R=3x3, while the third coordinate gives
x3-R=F0+B0. Hence x3 has complex-constant residue modulo p. The
[null-axis exclusion](cubic-null-axis-exclusion-pass122.md) finishes:
p divides an original affine-linear coordinate x3-c, so irreducibility
makes them associates. Applying E contradicts Ep=0 and Ex3=Y nonzero.
Together with the null reciprocal exclusion121, this eliminates the
entire null-axis alternative in the stated actual framework.

No growth estimate for derivatives of a, complex-constant relative
Jacobian, or global normalization N(v)=1 is needed. The polynomial null
speed control121 remains a valid coefficient control, but cannot extend
to a frame with these actual original-coordinate hypotheses.

## 2. A non-null reciprocal scalar is a cubic in changed coordinates

The [constant-coordinate equivalence](cubic-nonnull-reciprocal-equivalence-pass122.md)
treats D=a2 h^2+a1 h+a0+c/(lambda h+mu), with c lambda nonzero.
The actual linear change
x2_new=x3, x3_new=lambda x2+mu x3 has a polynomial inverse.
It sends h to xi=1/(lambda h+mu) and D to xi^2 D,
an exact cubic polynomial in xi with leading coefficient c.

This does not assert that the rational change of h is an automorphism
of the invariant plane. The constant ambient change preserves the
original inverse, potential and relative degree. The possible proper
finite extension L/C(h) is retained. For a general constant change of
determinant Lambda, the oriented intrinsic Jacobian derivation becomes
N/Lambda; its kernel, degree filtration and primitivity are unchanged.
Thus reciprocal and cubic are not separate surviving non-null types
modulo these allowed original-coordinate changes.

## 3. The remaining non-null cubic has restricted speed divisors

The [non-null divisor proof](cubic-nonnull-divisor-restriction-pass122.md)
uses the h,Y connection to obtain rho=C0 g+aY, with C0 complex
and a in L. Explicit differential first integrals establish this form
without an unproved integration in a finite field extension. It then
constructs a polynomial row for R and again contracts aY^2 to S.

For every irreducible p dividing Y, the actual conclusion is

\[
0<v_p(Y)<3v_p(P),\qquad p\mid(g^2-1).
\]

The weak inequality comes from P^3=Y K0. Equality would make K0 a
unit at p. The finite-place residue argument would then yield a
constant residue for x3 after cancellation of the nonzero factor
g^2-1 in B/pB, contradicting original-coordinate irreducibility.
That cancellation is justified: S is factorially closed in the
polynomial ambient ring, so p stays prime and pB intersect S=pS.

Consequently g is nonconstant and at least one of g-1 and g+1 is
reducible, counting repeated nonconstant factors. If both were
irreducible, Y would lie in C[g] and the cubic norm equation would
make P algebraic over C(g), contradicting the nonzero moving-frame
determinant. In particular g cannot be an actual coordinate of S.
The radical divisibility above does not assert Y divides g^2-1
with its full multiplicities.

The proof also supplies a surviving speed control. Put H=st and
U=H^2+2, and take
b=(H^2+1,st^2U,st^4U^2), h=1/(t^2U), D=h^3.
Its norm identity, unit row 1=g^2-sP and nonzero determinant
Omega=4st^5U^2 hold. The orders of (Y,P) along its prime supports
are (1,1), (4,2), and (2,1), so every strict bound holds. No actual
potential or original polynomial-coordinate inverse is assigned.
The two older non-null controls121 fail the new radical restriction.

## 4. Verification and the remaining obligation

The [canonical capture122](verification-pass122-working.json) records
six suites and eight successful methods: four new and four retained.
All six input hashes stayed unchanged. The measured subprocess elapsed
time is 2.6984937922097743 seconds; unittest reports 2.333 seconds.
The complete output hash and exact command are stored in the capture.

The new methods cover the [null polynomial row](cubic_null_reconstruction_checks_pass122.py),
the [constant metric congruence](cubic_nonnull_reciprocal_checks_pass122.py),
and the [non-null reconstruction and speed control](cubic_nonnull_reconstruction_checks_pass122.py).
They do not certify invariant-kernel contraction, finite-place field
arguments, prime cancellation, an actual frame or cancellation.
Full saved-file mathematical and code reconstructions found no defect
in their stated scopes. They are independent AI reviews, not human
expert review, formal verification or novelty clearance.

The user-status rerun a6c9c2 repeated eight tests and reread the proof.
It was verification progress only, not a new theorem or discovery.
The canonical run e33429 supersedes that run for this package; the
runs are not additive test coverage. This pass's mathematical gains
are the separately proved exclusions, equivalence and divisor bounds.

The next obligation is the full original-coordinate realization or
exclusion of the remaining non-null cubic type. Coefficient controls
alone do not settle it. Even a complete supplied-cubic exclusion would
leave arbitrary-frame entry and the unconfirmed intended statement.
The [checkpoint122](checkpoint-pass122-working.json) records the frozen
artifact versions and exact evidence scopes. Files through121 remain
unchanged; README and the research ledger remain live indexes.
