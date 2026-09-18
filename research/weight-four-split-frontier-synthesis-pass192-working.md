# Split zero-R recognition, actual absent-variable examples, and a failed ODE extension

Status: grouped191--192 working results. The actual split-quartic
zero-R branch has an original invariant coordinate. Two different
actual frames realize the earlier absent-variable branches.
A nonaffine rational solution prevents importing the earlier ODE
exclusion into the split nonzero-R case.
Unrestricted cancellation and arbitrary coordinate entry remain unsolved.

## 1. Exact scope of the new recognition

Assume an actual globally sliced frame

\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4).
\tag{1}
\]

The initial ideal is the entire weighted initial kernel, not one
relation among leading coefficients. The
[split zero-R proof192](weight-four-split-zero-r-coordinate-recognition-pass192-working.md)
uses the actual chart of184, with
\(q=-t^3-t^{-1}\), and additionally assumes \(R=k_\rho=0\).
It constructs

\[
I=W-(\lambda XY+\beta X+\alpha Y+D)Z-Q_0(X,Y)=g_0,\qquad
Q_0\in\mathbb C[X,Y],\quad
\lambda\in\mathbb C^*,\quad \alpha,\beta,D\in\mathbb C.
\tag{2}
\]

The right side belongs to the exact invariant coefficient field;
the left side belongs to the original polynomial ring.
The displayed shear has inverse
\(W=I+(\lambda XY+\beta X+\alpha Y+D)Z+Q_0(X,Y)\)
while \(X,Y,Z\) remain fixed. Thus \(I\) is an actual invariant
ambient coordinate, not merely a rational parameter.

Since the global slice makes \(A\cong B/(u)\) regular, the hypotheses
of [Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
are met. Its published conclusion gives \(A=\mathbb C[I]^{[2]}\).
The proof supplies its coordinate and regularity hypotheses
before applying that theorem.

## 2. Why the coefficient lemmas now apply

The [standalone lemmas191](weight-four-split-coefficient-ode-lemmas-pass191-working.md)
were initially conditional. The zero-R192 argument supplies their
actual geometric and field hypotheses.

Constant projected \(y\) is excluded using an actual commuting
derivation and the two-coordinate theorem. The remaining cubic
potential makes \(y\) affine on the entire generic line.
The full scalar determinant, with the factor \(Ny\) retained,
forces an exact coefficient cover

\[
\rho=an^2+bn+c,\qquad
2da'+ad'=0,\qquad d=t^{-4}-1.
\tag{3}
\]

The unrestricted coefficient integral is rederived with \(d'\)
retained. Actual field return proves \(L=K(n)\), where
\(K/\mathbb C(t)\) is finite but not assumed rational.
If \(a\ne0\), the coefficient \(a'''/(18d)\) has a pole of order
at least nine. Its occurrence as the leading coefficient of a
polynomial in the independent projected \(z\) contradicts the
degree-one field return. Thus \(a=0\).

The remaining linear-cover equation is

\[
10db''+5d'b'+d''b=0,\qquad b=\lambda t.
\tag{4}
\]

The assertion covers algebraic solutions in the exact field,
not just rational-function guesses. A nonproportional solution
would give an algebraic primitive of the nonzero regular
differential \(dt/\sqrt{1-t^4}\), impossible on a projective curve.

The residual scalar equations leave a slope \(D\in K\).
They do not by themselves force \(D\) constant.
The exact linear-pencil lemma and
\(g_2'=-(q''/2)D'\) do.
Finally the \(n\)-coefficient in the original \(W\) is exactly
\(\lambda XY+\beta X+\alpha Y+D\).
Subtracting that polynomial times \(Z\) removes \(n\);
transport through \(y=Y-tX\) makes the remaining correction's
coefficients complex. This is the original-ring step behind (2).

## 3. A negative result for the nonzero-R proof route

The [split ODE counterexample192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md)
derives the square-completion equation before specializing \(q\).
For \(f=1/R\), \(D_f=d'f/4+df'\), its necessary equation is

\[
20D_f f'''-3d(f'')^2-12f''D_f'=0,\qquad
f,f'',D_f\ne0.
\tag{5}
\]

Unlike the earlier equation for \(q=t^4\), this equation has the
nonaffine rational solution \(f=t^5+3t\) when \(d=t^{-4}-1\).
Here \(f''=20t^3\) and \(D_f=1-5t^4\), so the divisions used
in deriving (5) are legitimate in the coefficient field.

This disproves the proposed affine-only extension, not the
earlier lemma with its actual hypotheses. It does not realize
a polynomial frame, solve the full coefficient system, or
produce a counterexample to cancellation.
The extra potentials, scalar determinant, field return and
original inverse still need analysis.
The zero-R recognition does not depend on this failed extension.

## 4. Actual examples for the earlier, different initial form

The [two actual frames191](weight-four-absent-variable-two-actual-frames-pass191-working.md)
independently realize \(R=0\) and \(R=1\) for
\(\mathsf X^2\mathsf Z-\mathsf Y^4\), not the split form (1).
Both start with a polynomial ring carrying \(E=\partial_x\),
supply explicit target coordinates and two-sided polynomial
inverses, and have invariant coordinates

\[
I_0=W-X^2Z+Y^4=t,\qquad
I_1=(1+X^2)Z-XW-Y^4=t.
\tag{6}
\]

Their literal original \(\partial_Z\) operators have top selected
derivations \(\partial_y\) and \(-\partial_y\), respectively.
The second example therefore checks that \(Ny\) need not equal one:
here \(Ny=-1\), although it is a nonzero field unit.

The full initial maps have fraction field
\(\mathbb C(\xi,t,s)\), hence height-one kernel, and the primitive
irreducible relation \(X^2Z-Y^4\) generates it.
This proves actual nonvacuity, not just a formal leading identity.
Neither example establishes a minimal time profile: their invariant
coordinates already permit a different frame with a time-zero slot.

## 5. Verification evidence and its limits

Three saved-source suites have each been executed exactly once:

* actual frames191: three methods, 0.115 seconds, OK, exit zero;
* split coefficient192: three methods, 0.947 seconds, OK, exit zero;
* split zero-R192: three methods, 0.355 seconds, OK, exit zero.

The coefficient suite initially yielded an execution handle;
the terminal result came from polling that same handle, not
restarting it. The other two runs were initially terminal.
Complete source reads preceded the runs, and separate AI reviews
checked the supporting calculations and their stated boundaries.

The controls cover inverse identities, literal partials, coefficient
recurrences, the rational ODE counterexample and transport in an
explicit symbolic Laurent fixture. That fixture is not asserted
to be a globally sliced polynomial frame.
Finite controls do not prove exact field return, projective-curve
arguments, the published recognition theorem or all retained inputs.
These results remain working proofs without human expert review,
proof-assistant certification or historical novelty clearance.

The [verification192](verification-pass192-working.json) and
[checkpoint192](checkpoint-pass192-working.json) capture this group
separately from frozen190. Subsequent193 investigations are not
included in this synthesis's recognition claim or test counts.

The preceding check-in was status communication, not a new
mathematical result. The continued investigation adds the new
recognition and negative-result evidence rather than treating
repetition as progress.
No external contact, submission, public posting or new automation
is authorized by this packet or has been performed for it.
