# Exact acceleration bounds on the full speed scheme

The rank-one quadratic branch now has a uniform scheme-theoretic bound:
the fourth power of the acceleration belongs to the ideal of the three
linear-coordinate velocities. The acceleration itself belongs to that
ideal whenever the ideal is principal. For the general nonprincipal
case, a precise primitive-divergence condition remains unproved.

These are intermediate results for an explicitly restricted class of
actions. They neither recognize all actions in that class nor solve
the unrestricted complex-threefold cancellation question. No historical
novelty or human expert verification is claimed.

## 1. The unchanged problem and the restricted hypotheses

The working interpretation of Luo's email remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The correction, dimension and field have not been confirmed by Luo.
This investigation does not treat an intermediate lemma as a substitute
for (1). The retained all-nice working theorem does not supply a nice
frame for an arbitrary action.

The current branch assumes actual polynomial coordinates and an
original global slice:
\[
B=\mathbb C[x_1,x_2,x_3,z],\quad E\in\operatorname{LND}(B),
\quad E(s)=1,\quad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{2}
\]
Write a_i=Ex_i, b=Ez, I=(a_1,a_2,a_3)B and
B_0=C[x_1,x_2,x_3]. The term rank-one refers here to the sole
possibly nonzero coordinate acceleration. It is not an assertion
about the usual rank of a derivation or an arbitrary coordinate frame.

## 2. The whole ideal, not just its zero set

The original slice makes b a unit modulo I. Invariance of each a_i
then makes I stable under the original partial_z. Extracting polynomial
coefficients by differentiation proves I=(I cap B_0)[z], without a
reducedness assumption. In the same actual quotient, the rescaled
derivative b inverse E kills B_0 and takes z to one. This proves the
polynomial-cylinder and embedded-kernel statements directly.

If I is nonzero, divide its generators by their full coefficient gcd
g, writing a_i=g f_i and J=(f_1,f_2,f_3)B. Factorial closure and UFD
divisibility prove g is invariant and independent of z; J is extended
from B_0 as well. With d_f=sum_i partial_{x_i}f_i, the exact result is
\[
q\in gB,\qquad
q\in I\ \Longleftrightarrow\ d_f\in J.
\tag{3}
\]
The proof retains every factor multiplicity in g. It does not replace
gcd one by a multivariable Bezout identity. Principal I has J=B and
therefore q in I. For I=0 the slice already gives constant b and q=0.
The full derivation is in the
[divisorial note](rank-one-acceleration-divisorial-ideal-pass82.md).

The [speed-quotient note](rank-one-speed-quotient-pass82.md) further
identifies B/I=R[z]=R[s] with the same embedded invariant ring R. In
these quotient rings, z can be a quadratic polynomial in s with a
nonzero nilpotent coefficient. The explicit finite Catalan inverse
shows why the domain assertion that an LND kills every unit cannot
be used after passing to a nonreduced quotient.

## 3. The ambient determinant imposes a uniform exponent

The nilpotent quotient examples by themselves allow all nilpotence
orders. The original polynomial action imposes more. The independent-time
flow is (x_i+t a_i,z+t b+t squared q/2), with determinant one.
Both partial_z a_i and partial_z q belong to I. Reducing the full
Jacobian determinant, while retaining its arbitrary bottom row, gives
\[
1=(1+t d)\det(\operatorname{Id}_3+tL),\qquad
d=\overline{\partial_zb},\quad
L=(\overline{\partial_{x_j}a_i}),
\qquad q^4\in I.
\tag{4}
\]
Indeed the three determinant coefficients must be -d,d squared,-d cubed;
the remaining coefficient forces d to the fourth power to vanish.
The unit relation bar(q)=bar(b)d gives the conclusion. No zero divisor
is cancelled in this coefficient argument.

The [ambient proof](rank-one-ambient-nilpotence-bound-pass82.md)
establishes the general n-variable version q to the nth power in I
and nilpotence of the full velocity Jacobian modulo I. It does not
claim that Jacobian is nilpotent in B. Nor does it establish sharpness
among actual actions.

The abstract quotient examples with acceleration of nilpotence order
at least five cannot be the full speed quotients of (2). Orders two,
three and four are not excluded by (4), and no ambient realization of
a nonzero residual acceleration has been constructed. Membership of
q itself in I remains a separate question, not a consequence of its
fourth power belonging to I.

## 4. Source and experimental boundaries

The [primary-source check](nonreduced-divergence-source-boundary-pass82.md)
examines the relative-plane theorem in Berson, van den Essen and
Maubach's 1999 report. In the current quotient, relative zero divergence
would itself be equivalent to q in I. That theorem therefore supplies
no unconditional shortcut; ambient and quotient-relative divergences
must not be identified. The report and extracted text are checksummed.

The bounded actual-coordinate search found no q outside I. Its
classified initial replay tested 140 proper nonprincipal cases over
24 distinct ideal representations. The only broader batch tested
eleven such cases over seven representations. These sets can overlap,
and neither was an exhaustion. The
[search record](rank-one-speed-search-scope-pass82.md) corrects the
initial gcd-screen label and records the exact scripts, bounds and
replay commands. Search candidates contribute zero unittest methods.

The [standalone controls](rank-one-speed-controls-pass82.md) have four
exact methods. The [canonical run](verification-pass82-working.json)
passed all four in one suite, with 0.287 seconds of unittest time and
0.501625 seconds of monotonic wall time. Three tracked inputs stayed
unchanged; the complete output is retained. Actual polynomial inverses,
quotient-only controls and formal matrix identities have separate
scopes. None is a formal proof of a universally quantified theorem.

## 5. The next mathematical gap

The next attack must either force the primitive divergence into J,
construct a genuine action with q outside I, or find a recognition
argument that does not require this membership. Any proposed example
must satisfy the original LND, slice and coordinate-generation
hypotheses, not just a nilpotent quotient or a determinant identity.

Even an affirmative answer to q in I would not by itself supply a
simultaneous polynomial coordinate change or recognize every action
in (2). The frozen pass81 example still excludes changes fixing the
three good coordinates pointwise. Arbitrary quadratic-time actions
and unrestricted cancellation remain further obligations.

The [audit](proof-audits-pass82-working.md) and
[checkpoint](checkpoint-pass82-working.json) separate written AI
proof reviews, exact finite computations, source reads and integrity
checks. No new full regression is claimed. The last full75 record
remains 146 suites and 1047 methods, and the central historical registry
remains 544 claims. No external contact, posting or submission occurred.
