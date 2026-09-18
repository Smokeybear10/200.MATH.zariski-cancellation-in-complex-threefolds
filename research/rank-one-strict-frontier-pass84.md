# Strict acceleration containment and the remaining local obstruction

The supplied polynomial slice imposes more than ordinary integral
dependence on the acceleration. Its rational return identity gives an
explicit power in a strictly higher power of the full speed ideal.
Separately, any possible nonzero square class is confined to finitely
many embedded critical points in the three-variable speed scheme.

These are restricted working deductions, not a solution of complex
threefold cancellation. They neither produce a nice frame for an
arbitrary sliced action nor recognize every action in the restricted
class. No historical novelty or human expert validation is asserted.

## 1. Exact scope and notation

The original question is still the unconfirmed corrected interpretation
A[s] isomorphic to C^[4] implies A isomorphic to C^[3]. The present
deductions assume additional structure in actual polynomial coordinates:
\[
B=\mathbb C[x_1,x_2,x_3,z],\quad E\in\operatorname{LND}(B),
\quad E(s)=1,\quad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Write a_i=E(x_i), b=E(z), I=(a_1,a_2,a_3)B. The three a_i are the
good-coordinate speeds; q is the remaining acceleration. The supplied
slice is the original polynomial s, not a local analytic flow parameter.

The expressions q squared in I and q in I squared have different
meanings. The former kills the square of the class of q in B/I.
The latter expresses q as sums of products of two good speeds.
The actual pass81 example with I=(a squared), q=a cubed satisfies
the first statement and violates the second.

The preserved [pass83 proof](rank-one-return-frontier-pass83.md) gives
q integral over I, q cubed in I, and no isolated points of the
specialized good-speed zero set. It does not discard nilpotents.

## 2. The original slice strengthens the return identity

For nonzero q and proper I, return along the actual flow to the
same original z coordinate. At time -2b/q the rational map is
rho=(x-2ba/q,z). It keeps a and q fixed, changes b to -b, and changes
the actual slice by -2b/q. The last identity is the new input.

Let D be the degree of s in the three good variables, treating z
as a coefficient. Frozen Taylor derivatives H_k are formed by
contracting the kth good-coordinate derivative of s with k copies
of a. Hence H_k lies in I^k. Derivatives do not act on a. The slice
identity forces D>=2 and gives
\[
Uq^{D-1}=\sum_{k=2}^D
\frac{(-2b)^{k-1}}{k!}H_kq^{D-k},
\qquad U=1-H_1=b\partial_zs\equiv1\pmod I.
\tag{2}
\]
After localization at U this is monic of degree m=D-1, with its
jth coefficient in the ideal power I^(j+1), rather than merely I^j.
Repeated monic reduction of q^(m squared) yields coefficient order
at least m squared plus one in every terminal term. Since U is a
unit modulo every power of I, localization contracts exactly and
\[
\boxed{q^{(D-1)^2}\in I^{(D-1)^2+1}.}
\qquad D=2\Longrightarrow q\in I^2.
\tag{3}
\]
The [complete strict-slice proof](rank-one-strict-slice-certificate-pass84.md)
checks the exponent estimate and the descent. This argument works
directly in B; replacing q by a congruent representative modulo I
would not justify a strict power statement.

The property in (3) is called inner integral closure in established
commutative algebra terminology.[^inner] The proof here is elementary
and does not import a closure equivalence theorem or Briancon--Skoda
for this step. It also gives v(q)>v(I) for any valuation nonnegative
on B with v(I)>0. If g is the gcd of the good speeds, every irreducible
factor dividing g occurs in q at least one additional time. The
actual I=(a squared), q=a cubed example attains that additional-copy
bound. The exponent in (3) is an explicit upper bound, not asserted
optimal for the supplied slice.

## 3. Where a square defect can remain

Use the exact extension I=J[z], where
R=C[x_1,x_2,x_3], J=(f_1,f_2,f_3), f_i=a_i(x,0), and q_0=q(x,0).
The cyclic square-defect module is M=R times the class of q_0 squared
inside R/J. It vanishes exactly when q squared belongs to I.

At a prime of R of height at most two, a minimal reduction of the
localized ideal has at most two generators. The two-generator
Briancon--Skoda inclusion makes M vanish there. At a closed point
where some f_i has a nonzero linear term, use that generator as a
regular-parameter auxiliary ideal in the original source theorem.
This also gives square membership. Consequently
\[
\operatorname{Supp}M\subseteq
\{\mathfrak m\in\operatorname{Ass}(R/J):
\mathfrak m\text{ is embedded and maximal},
\operatorname{Jac}(f)(\mathfrak m)=0,
\ell(JR_{\mathfrak m})=3\}.
\tag{4}
\]
This set is finite. The displayed Jacobian condition means the entire
matrix is zero, not just its determinant. The analytic spread condition
is a local ideal condition, not a dimension estimate inferred from
the underlying zero set. In B the corresponding possible supports
are z-lines; finiteness refers to the three-variable specialization.

Thus the absence of embedded maximal associated primes implies
q squared in I. More generally, at a closed speed zero with linear
rank r=rank Jac(f), r=0,1,2 gives q_0^(3-r) in the local ideal.
Rank two in particular gives first-power membership. Rank three is
excluded by the absence of isolated zeros. The
[complete local proof](rank-one-square-embedded-support-pass84.md)
specifies each published hypothesis and gives a separate elementary
rank-two argument. It does not prove that the actual speed ideal
has no embedded critical points.

## 4. Exact controls against invalid upgrades

Strict power containment does not itself imply square membership,
even with no isolated components. In C[x,y,z], take
I=(x^10,xy^9,xz^9) and h=x^4y^4z^4. Then h^9 belongs to I^10 but
h squared is not in I. The radical is (x) and the square-defect
annihilator is (x squared,y,z), giving an embedded length-two defect
at the origin. Its full Jacobian matrix vanishes there and its
analytic spread is three.

These data fail an actual-action identity: h is not congruent to
-b_0 div(f) modulo I for any admissible unit b_0. A second strict
ideal example satisfies that trace relation but fails the next
quotient determinant coefficient. The
[ideal-boundary proof](embedded-square-ideal-boundary-pass84.md)
records both failures. Neither is an action counterexample.

The actual return also has Jacobian determinant minus one, both in
the full four variables and in the three good variables with z fixed.
The [variable-time determinant proof](rank-one-return-jacobian-pass84.md)
derives this from the original flow. A retained actual example has a
genuine pole despite that determinant, so the condition does not supply
a polynomial inverse or remove the remaining membership obstruction.

The [two-method actual checker](strict_slice_checks_pass84.py) verifies
the whole-z return identities, both coordinate-inverse orders, the
transported derivations, slice equations, and strict Taylor certificates
for two genuine actions. Their supplied good-variable slice degrees
are two and five. A separate
[one-method ideal checker](embedded_square_controls_pass84.py) verifies
the preceding ideal-only controls and the identities they fail.
These finite examples do not verify the general monic-reduction lemma.

## 5. Remaining obligation

First-power membership or an actual counterexample remains the central
question in this restricted branch. The inner-integrality and support
conditions now rule out additional candidate data, but the ideal-only
examples show exactly why those conditions cannot substitute for the
remaining original-action identities. Even first-power membership
would still require a coordinate-reduction or recognition argument.

The unrestricted goal remains unchanged. The
[verification capture](verification-pass84-working.json),
[proof audit](proof-audits-pass84-working.md), and
[checkpoint](checkpoint-pass84-working.json) separate the working
deductions from finite checks, source inputs, and unresolved claims.
No expert contact, public posting, submission or novelty claim has
been made.

[^inner]: Neil Epstein and Melvin Hochster, [*Continuous Closure, Axes
    Closure, and Natural Closure*](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/08/CnClTAMS.pdf),
    definition preceding Theorem 5.4 and Theorem 5.4(3), printed
    pp. 20--21. This citation identifies the established terminology,
    not the novelty of the actual-action deduction.
