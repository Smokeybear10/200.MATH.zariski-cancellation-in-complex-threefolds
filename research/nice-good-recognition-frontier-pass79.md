# Recognition of the supplied-good nice branch

The supplied-good nice branch has a complete written recognition
argument, with separate AI reconstructions of its new proofs and
their actual-coordinate hypotheses. The previous relative
hypersurface obstruction is closed within that branch. The general
complex-threefold cancellation problem is not solved.

The working interpretation remains the corrected statement
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Xiangrui Luo has not confirmed this field and dimension or the
correction of the pasted email's conclusion. No external message,
submission or public research claim has been made.

## 1. The exact advance

The [recognition theorem](nice-good-direction-recognition-pass79.md)
applies to a locally nilpotent derivation in the original polynomial four-ring with
the following additional structure:
\[
E(s_*)=1,\qquad E^2(x_i)=0\ (1\le i\le4),\qquad
\exists\,0\ne c\in\mathbb C^4:\ [E,[T_c,E]]=0,
\quad T_c=\sum_i c_i\partial_{x_i}.
\tag{2}
\]
Its conclusion is that ker E is a polynomial three-ring. Niceness
is the middle condition. The last condition supplies a constant
good direction; it is not asserted to follow from the first two.
The ordinary degrees of the coefficient polynomials are unrestricted.

The square-zero-Jacobian and linear-velocity-cone cases use the
previously recognized gates. The new proof treats the nonlinear
cone case with its one supplied good direction. It retains the
published quotient and quasi-translation inputs rather than
substituting rational or local coordinates for original ones.

## 2. Why the final coefficient is a constant

Pass78 supplied an actual invariant plane S=C[u,v] and two generators
of A over S. The new
[generation determinant](relative-quadratic-generation-pass79.md)
uses the original coordinate reconstruction to constrain the defining
relation. Over S, it is linear in Z and quadratic at most in Y.
The original good partial T=partial_w has exact regular cofactor
formulas. Together these give
\[
\begin{gathered}
A=S[Y,Z]/(aZ+bY^2+dY+e),\qquad a\in S\setminus\{0\},\\
Tu=-a\ell_v/\kappa,\quad Tv=a\ell_u/\kappa,
\quad\kappa\in\mathbb C^*,\\
T(a)=a(-a_u\ell_v+a_v\ell_u)/\kappa\in aB,\\
T(a)=0,\quad E(a)=0
\quad\Longrightarrow\quad a\in\mathbb C^*
\quad\Longrightarrow\quad A=S[Y].
\end{gathered}
\tag{3}
\]
The first implication uses the actual coordinate LND: a nonzero
polynomial cannot have a nonzero derivative divisible by itself.
The next uses the precise invariant-omission theorem for this
nonlinear supplied-good branch. Once a is a constant, the relation
eliminates Z globally. There is no denominator patching left.

The key point is that the cofactors came from the actual polynomial
coordinate generation of B. A smooth abstract quadratic hypersurface
would not supply this T or the omission theorem. The
[quadratic source control](quadratic-relative-modification-source-pass79.md)
explains that distinction using the Russell cubic without assigning
it an unproved polynomial-cylinder property.

## 3. Other proved structure in the same calculation

The [primitive-Jacobian proof](relative-jacobian-primitive-pass79.md)
shows that the primitive intrinsic field is a complex multiple of
F_Z partial_Y minus F_Y partial_Z. Its two coefficients have no
nonconstant gcd in A. The argument keeps every whole fiber,
including nilpotents. A gcd-one pair is not in general a unit ideal;
the extra constant-coefficient result in (3) is what makes this
specific primitive field have a global slice.

The [transported-partial system](relative-good-partial-equations-pass79.md)
gives all four original-coordinate equations and the exact bracket
constraints. In particular the induced derivation on the slice
section cannot preserve S in this nonlinear branch. Holding its
S-coefficients constant would invalidate the calculation.

The quadratic-generation proof also shows that Q=[T,E] has
Q cubed zero on all four original coordinates. Its second iterate
is nonzero and not parallel to its first by the retained Wronskian
theorem. These are coordinate-iterate statements in this branch,
not a claim that Q cubed is the zero operator on every polynomial.
The original unnormalized intrinsic field may still be a replica
of its primitive part.

## 4. Verification and source boundaries

The new [standalone checker](relative_quadratic_checks_pass79.py)
has four exact methods. They check formal determinant and cofactor
identities, both inverse orders of the actual retained conic,
quadratic field calculations, the non-LND self-divisibility boundary,
and the whole nonreduced-fiber distinction. The
[controls note](relative-quadratic-controls-pass79.md) states what
each method does and does not establish.

The [canonical targeted capture](verification-pass79-working.json)
passes all four methods in one suite. Its unittest runtime is
0.189 seconds; its complete output and input hashes are retained.
This is not a full79 regression. The last full record remains
146 suites and 1047 methods from75. Repeated executions do not
increase those method counts.

The [proof audit](proof-audits-pass79-working.md) distinguishes
complete written AI reconstructions, selected primary-proof reads,
finite exact checks and file-integrity evidence. The
[checkpoint](checkpoint-pass79-working.json) freezes the new packet
without rewriting earlier pass conclusions. No finite test proves
the published geometric inputs or the universal theorem statement.

The supplied-good endpoint uses de Bondt's selected invariant-omission
theorem, not a theorem giving an invariant ambient coordinate for
every nice derivation. The source-applicability notes distinguish
coordinate rank from matrix rank and a polynomial presentation over
the actual base from an abstract cylinder. A bounded search with
no exact match is not a historical novelty certification.

## 5. The remaining mathematical problem

The recognition step in the supplied-good nice branch should not be
reopened as though the coefficient a could still be nonconstant
under every retained hypothesis. Weaker intrinsic examples do not
satisfy that complete original-partial system.

The next nice-action question is whether the original global slice
excludes the apex-free velocity-cone case, or whether a different
recognition route can handle it. A constant good direction has not
been produced there. Separately, no nice coordinate frame has been
constructed for an arbitrary E obtained from (1). Both obligations
remain part of the original objective.

The [common-highest-field proof](nice-common-top-normal-identity-pass79.md)
makes a concrete start without a supplied good direction. The
second-adjoint columns have one actual polynomial LND direction;
its common quotient with E is a plane containing all four original
velocities. A four-entry normal gives a faithfully contracted
polynomial syzygy. At any common zero of that row, its lowest-order
terms span at most two dimensions. This restriction does not exclude
all such zeros or finish the no-good-direction case.

The all-profile height threshold remains ten; this packet does not
recognize every general height-eleven frame. Within a hypothetical
nonpolynomial nice frame, the new theorem would force every nonzero
constant direction to fail goodness. The original partial profile
would therefore be (2,2,2,2), of height twelve, by J cubed zero.
This conditional nice-frame bound is not an all-frame bound.

The result is a written working theorem, not a submitted paper or
a formally verified proof. Human expert review, a complete novelty
audit and any claimed proof-assistant certification remain absent.
The persistent unrestricted goal stays active.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass79.py
~~~
