# A uniform lower bound on the shift of a Vénéreau slice derivation

Date: 2026-09-17. Private working proof; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

## 1. Statement

Let B=C[x,y,z,u], A=C[x,y,z], E=partial_u, and, for an integer n>=1,
put

\[
v_n=y+x^n\bigl(xz+y(yu+z^2)\bigr)=a_nu+b_n,
\qquad a_n=x^ny^2,\quad b_n=y+x^{n+1}z+x^nyz^2.
\]

For every locally nilpotent derivation D of B satisfying D(v_n)=1,
its exact u-degree shift satisfies

\[
\delta(D):=\max\{\deg_uDx,\deg_uDy,\deg_uDz,\deg_uDu-1\}\ge2.
\tag{1}
\]

The degree of zero is minus infinity. This statement is conditional
on existence of D and makes no coordinate-status assertion for v_1.
For n>=3 existence is supplied by the whole polynomial completion
in Section 4 below. In that range, every coordinate completion of v_n
has a coordinate partial whose shift is at least 2, and one explicit
completion has shift 10. The minimum is not determined here.

This strengthens the positive-shift obstruction of
[615](venereau-coordinate-positive-shift-obstruction-pass615-working.md)
by excluding shift one, uniformly in n. The ambient E is already a
translation. No obstruction to changing the specified coordinate v_n,
and no counterexample to cancellation, is asserted.

## 2. Filtration facts, including the boundary shifts

The generator maximum in (1) is the exact finite shift because of
the Leibniz rule on the actual polynomial ring A[u]. If delta<0,
D kills A and Du belongs to A. The equation D(v_n)=1 would give
a_n Du=1, impossible since a_n is a nonunit. Thus delta>=0.

For a nonnegative shift, the full leading derivation on A[eta] is
a nonzero homogeneous locally nilpotent derivation. This follows
directly by lifting a homogeneous element and comparing its successive
nonzero leading derivatives with those of D. Since its value at eta
is divisible by eta, that value is zero: a nonzero element of a
characteristic-zero domain cannot divide its nonzero derivative under
an LND. The leading derivation therefore has the form eta^delta N,
where N is a nonzero LND on A, and deg_u Du<=delta.

In D(a_nu+b_n)=1, the coefficient of u^(delta+1) is N(a_n),
so N(a_n)=0. Factorial closure of the kernel of N gives

\[
Nx=Ny=0.
\tag{2}
\]

These arguments are the filtration argument of
[614](nonunit-speed-coordinate-induced-action-pass614-working.md),
but here they require only D(v_n)=1 and local nilpotence, not that
D is a coordinate partial.

If delta=0, then D=N+beta partial_u with beta in A. Equations
D(v_n)=1 and (2) give

\[
1=N(b_n)+a_n\beta
 =x^n\bigl((x+2yz)N(z)+y^2\beta\bigr),
\]

which is impossible. It remains to exclude delta=1.

## 3. Shift one gives incompatible residue equations

Assume delta=1. By (2), the degree-one terms of Dx and Dy vanish.
By the preceding bound on Du, write the entire derivation components as

\[
Dx=X,\qquad Dy=Y_0,\qquad Dz=Z_0+ug,\qquad
Du=\beta_0+u\beta_1,
\tag{3}
\]

with X,Y_0,Z_0,g,beta_0,beta_1 in A. These are exact expressions,
not truncated expansions. Comparing the coefficient of u in D(v_n)=1
gives

\[
n x^{n-1}y^2X+2x^nyY_0+x^ny^2\beta_1
 +x^n(x+2yz)g=0.
\tag{4}
\]

Divide by x^(n-1) in the polynomial domain, and reduce modulo x.
Since n is nonzero and C[y,z] is a domain, this implies x divides X.
But Dx=X, so x divides Dx. Local nilpotence forces

\[
Dx=0.
\tag{5}
\]

For clarity, the fact used here follows from additivity of LND degree:
if Dx=xq were nonzero, then deg_Dx-1=deg_Dx+deg_Dq, impossible.
It is applied to the entire Dx, not only to one leading coefficient.

After (5), equation (4), divided by x^n, becomes

\[
2yY_0+y^2\beta_1+(x+2yz)g=0.
\tag{6}
\]

Modulo y this says xg=0 in C[x,z], so g=yh for some h in A.
Divide (6) by y to obtain

\[
2Y_0+y\beta_1+(x+2yz)h=0.
\tag{7}
\]

Evaluating at x=y=0 yields Y_0(0,0,z)=0. On the other hand,
evaluate the entire equation D(v_n)=1 at x=y=0. By (5), the Dx
contribution is zero. The Dy coefficient is one and the Dz and Du
coefficients are zero. Hence Y_0(0,0,z)=1. This contradiction
excludes delta=1 and proves (1) for every n>=1.

## 4. Actual completions for n>=3

Use the polynomial LND K, its invariants V,W, and its complete flow
F_tau from [615, Section 2](venereau-coordinate-positive-shift-obstruction-pass615-working.md).
Since Kx=0, replacing the scalar parameter tau by x^(n-3) for n>=3
is the genuine finite exponential of the LND x^(n-3)K. Its inverse
is obtained by replacing that same invariant parameter by its negative.
The first nontrivial flow component is

\[
Y=y+x^{n-3}x^3V=v_n.
\]

Thus (x,v_n,Z,U) is an actual polynomial coordinate system for every
n>=3, including along x=0. No localization is used to assert this.

Because the parameter depends only on x, differentiating its inverse
at fixed x,Z,U makes no derivative of tau appear. The exact u-degrees
of the coordinate partial's values on y,z,u are still 8,10,10.
Their respective leading coefficients are

\[
x^{5n-6}y^{14},\qquad
x^{5n-9}y^{18},\qquad
-x^{5n-9}y^{16}(x+2yz).
\]

These follow from the full arbitrary-tau inverse in615: before
substitution the leaders are tau^5 times x^9y^14, x^6y^18,
and -x^6y^16(x+2yz), respectively. They are nonzero polynomials
for every n>=3. Consequently this completion has exact shift 10.
This upper bound is an example, not a claim of optimality.

The coordinate status of the classical Vénéreau family is prior work;
see the primary references already identified in615. The result at
issue in this note is the lower-bound argument, whose novelty has not
been audited. This note supplies no new coordinate-status theorem.

## 5. Verification boundary

Fresh unsaved symbolic checks reconstructed the complete coefficient
of u in D(v_n), both divisibility reductions, and both final residue
evaluations for n=1,...,8. The displayed identities prove the uniform
argument; those finite checks do not substitute for it. The entire
arbitrary-parameter flow and inverse used in Section 4 were separately
checked during the independent saved-source review of615.

No saved checker was executed, imported, or compiled. Author review
and independent saved-source review remain separate gates. There is
no human expert review, Lean certification, or public novelty claim.
