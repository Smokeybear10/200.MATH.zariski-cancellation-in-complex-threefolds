# Acceleration units extend the quadratic divisor classification

The full divisor classification also applies when both bad-coordinate
speeds vanish modulo an invariant prime, provided one good-coordinate
acceleration remains nonzero. The acceleration supplies an actual
localized slice that is affine-linear in the generic bad pair. Its
projection retains the degree-two generator bound needed for the
elementary DVR argument.

A separate normalization sharpens the primitive plinth bound to
\(p\mid\Delta\) globally, including at common-speed primes. Neither
statement proves global polynomiality or removes every exceptional
divisor.

## 1. Original hypotheses and the enlarged local criterion

Retain precisely the degree-two, independent-defect, rank-two bad
projection hypotheses of
[the generic bad-pair proof](generic-bad-pair-pass44.md) and
[the full divisor classification](quadratic-divisor-classification-pass45.md).
In particular,
\[
B=A[s_*]=\mathbb C[x_1,x_2,x_3,x_4],\qquad E(s_*)=1,
\qquad C\simeq\mathbb C^{[2]},\quad L=\operatorname{Frac}C,
\]
\[
f=Ex_3,\quad g=Ex_4,\quad h_i=E^2x_i\ (i=1,2),
\qquad f,g,h_1,h_2\in C,
\tag{1}
\]
and
\[
B_L=L[x_3,x_4],\qquad
x_i=\mathcal Q_i(x_3,x_4),\quad
\mathcal Q_i\in L[X_3,X_4],\quad\deg\mathcal Q_i\le2.
\tag{2}
\]
The two speeds are algebraically independent, in particular nonzero.
The inclusion \(C\subset A\) is factorially closed and faithfully
flat, and \(A\) is a UFD. These are inherited original-cylinder
consequences.

Fix an irreducible \(\pi\in C\), put
\(R=C_{(\pi)}\), and let \(\kappa=R/\pi R\).
Assume
\[
(f,g,h_1,h_2)R=R.
\tag{3}
\]

**Theorem.** The full intrinsic localized quotient \(A_R\) is either
\(R[t]\), or
\[
A_R\simeq R[T,Z]/(\pi^n Z-T^2+\eta),\qquad
1\le n\le v_\pi(\Delta),\quad
\eta\in R^*,\quad\bar\eta\notin\kappa^{*2}.
\tag{4}
\]
For a primitive intrinsic LND with kernel \(C\), the quadratic
alternative has exact local plinth \(\pi^nR\) and full residue
invariant-field degree two. The polynomial alternative has plinth
\(R\) and residue degree one.

If either speed is a unit, the preceding classification already
applies. The new case is \(f,g\in\pi R\) and some \(h_i\in R^*\).

## 2. An actual acceleration slice has an affine-linear generic inverse

Choose a good index \(i\) with \(h_i\in R^*\). Then
\[
\sigma=\frac{Ex_i}{h_i}\in B_R,\qquad E\sigma=1.
\tag{5}
\]
This uses the actual polynomial value \(Ex_i\); it does not assume
that a rational candidate lies in the localized ring. Since \(E\)
kills \(L\), equations (1)--(2) give
\[
Ex_i=f\,\partial_{X_3}\mathcal Q_i+
g\,\partial_{X_4}\mathcal Q_i.
\]
Consequently there are \(a,b,c\in L\) such that
\[
\sigma=ax_3+bx_4+c,\qquad af+bg=1.
\tag{6}
\]

Let \(d=\gcd(f,g)\) in \(C\), set \(f_0=f/d\),
\(g_0=g/d\), and define the actual polynomial invariant
\[
j_0=g_0x_3-f_0x_4\in A.
\tag{7}
\]
Its generic ring is \(A_L=L[j_0]\), since it differs from the
previous generic coordinate \(gx_3-fx_4\) by the nonzero scalar
\(d\in L\). The determinant of the coefficient matrix for
\((\sigma-c,j_0)\) is \(-1/d\), not an assumed unit of \(R\).
Over \(L\) its exact inverse is
\[
x_3=f(\sigma-c)+dbj_0,\qquad
x_4=g(\sigma-c)-daj_0.
\tag{8}
\]
Only this generic inverse is needed. No ambient polynomial
coordinate assertion is made for \(\sigma,j_0\).

## 3. Slice projection gives the entire degree-two algebra

The actual slice theorem gives \(B_R=A_R[\sigma]\).
Let \(\rho:B_R\to A_R\) be evaluation at \(\sigma=0\).
Equation (8) gives actual elements
\[
\ell_3=\rho(x_3)=dbj_0-fc,\qquad
\ell_4=\rho(x_4)=-daj_0-gc
\tag{9}
\]
of \(A_R\), each affine-linear in \(j_0\) over \(L\).
The projected good coordinates are
\[
q_i(j_0)=\rho(x_i)=\mathcal Q_i(\ell_3,\ell_4)
\in L[j_0],\qquad \deg q_i\le2.
\tag{10}
\]
Since the four actual coordinates generate \(B_R\) over \(R\),
their images generate the entire quotient:
\[
A_R=R[\ell_3,\ell_4,q_1,q_2]
    =R[j_0,\ell_3,\ell_4,q_1,q_2]\subset L[j_0].
\tag{11}
\]
The second equality is legitimate because
\(j_0=g_0\ell_3-f_0\ell_4\) with coefficients in \(R\).

For completeness, the same DVR elimination applies to this slightly
larger list of linear generators. Choose one of the at most two
quadratics with smallest leading-coefficient valuation and eliminate
the other quadratic term by an \(R\)-multiple. Among the remaining
finitely many nonconstant linears, including \(j_0\), choose \(t\)
with smallest leading-coefficient valuation. Every other linear
generator is \(at+b\), with \(a\in R\) and
\(b\in A_R\cap L=R\). Thus
\[
A_R=R[t]\quad\text{or}\quad A_R=R[t,z],
\qquad z\in L[t],\quad\deg_tz=2.
\tag{12}
\]
Factorial closure and faithful flatness give the same nonzero domain
special fiber as in the preceding proof. Its exact primitive
presentation, finite root lifting in the linear-residue case, and
square completion in the irreducible quadratic-residue case therefore
apply without alteration. This proves the alternatives in (4), apart
from the exponent bound proved next. The full-ring statement is a
consequence of (11), not a promotion of the bad-image subring.

## 4. Normalizing the invariant removes the common-speed factor

Let \(D\) be a primitive nonzero intrinsic LND on \(A\) with
kernel \(C\), and write its full plinth as \(pC\).
Principality is the inherited
[factorial faithfully-flat plinth result](intrinsic-plinth-boundary-pass27.md).
The global determinant fields satisfy
\[
K_3j_0=f_0\Delta,\qquad K_4j_0=g_0\Delta.
\tag{13}
\]
They restrict to \(A\) because they commute with \(E\).
As proved explicitly in Section 6.1 of the preceding classification,
\[
K_3|_A=a_3D,\qquad K_4|_A=a_4D,\qquad a_3,a_4\in C.
\]
Indeed generic proportionality on \(L[j_0]\) gives multipliers
in \(L\); reducing a multiplier as a fraction in the UFD \(A\)
forces its denominator to divide all values of the primitive \(D\)
on algebra generators. The denominator is a unit, and contraction
\(A\cap L=C\) finishes the argument.

Therefore (13) consists of genuine local-slice values:
\[
f_0\Delta=D(a_3j_0),\qquad
g_0\Delta=D(a_4j_0).
\]
Both lie in \(pC\). Since \(\gcd(f_0,g_0)=1\), unique
factorization yields the stronger global bound
\[
p\mid\Delta.
\tag{14}
\]
No Bezout identity or unit-ideal assertion for \((f_0,g_0)\)
is required. This improves the earlier valid bound
\(p\mid d\Delta\) by using an actual normalized invariant,
not by dividing a field or local slice outside its ring.

The preceding exact local plinth calculation and invariant
localization give \(n=v_\pi(p)\) in every quadratic model
obtained here. Equation (14) proves the bound in (4), including
at primes dividing both original speeds.

## 5. Exact residual divisor set and verification scope

The enlarged argument classifies every divisor prime except
possibly those dividing all of
\[
f,\quad g,\quad h_1,\quad h_2.
\tag{15}
\]
Even among these, \(p\notin\pi C\) already implies
\(A_R=R[t]\): the full primitive plinth becomes the unit ideal,
so an invariant-localized actual \(D\)-slice gives the polynomial
line by the slice theorem. Thus any unclassified divisor
degeneration is supported on the prime factors of
\[
\gcd(p,f,g,h_1,h_2),
\quad\text{a divisor of}\quad
\gcd(\Delta,f,g,h_1,h_2).
\tag{16}
\]
This support statement does not exclude those primes, assert that
the quadratic alternatives are nonpolynomial globally, or prove that
codimension-one classifications glue to \(A\simeq\mathbb C^{[3]}\).
The standard polynomial three-ring boundary in the preceding note
continues to apply.

The only classification mechanism reused is the fully written
elementary DVR proof in the preceding note, with the generator
extension justified in (9)--(12). No new literature theorem is
invoked. Its existing four-method checker tests the shared DVR
mechanisms; it is not rerun or counted as a new suite here. The
affine-linear inverse and projection in this note are exact algebraic
proof identities. No new full-frame example, human expert review,
proof-assistant verification, historical novelty or unrestricted
cancellation claim is made.
