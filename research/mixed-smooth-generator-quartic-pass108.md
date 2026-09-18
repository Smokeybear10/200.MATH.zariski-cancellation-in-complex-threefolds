# A smooth second-image generator supplies an actual quartic

In the remaining proper second-image branch, suppose the coefficient
a of the surviving degree-two element has first base order one.
An exact change of the degree-two basis makes B1=a. A regular-sequence
division then produces one actual quartic and forces the normalized
fourth-image ideal to have the form (a,t^n), with a finite bound on n.
This is a conditional restriction, not an exclusion of this branch.

## 1. Hypotheses and a basis change preserving the surviving element

Use the actual local setting and notation of the
[proper-second-image proof108](mixed-proper-second-image-jets-pass108.md).
Thus R is the regular local invariant surface, with maximal ideal m;
A_R is a faithfully flat domain; N is its invariant derivation;
F_j=ker N^(j+1) is free of rank j+1; and the whole fiber is
C[G]/(G^2(G-1))[c]. In the proper case, F2 has basis 1,G,H,
with H having zero whole-fiber residue, and
\[
\begin{gathered}
r=aG+bH,\quad NG=\epsilon br+B_1,\quad
NH=-\epsilon ar+B_2,\quad Nr=P=aB_1+bB_2,\\
Q=\epsilon r^2-2B_2G+2B_1H\in R,\qquad
J_2=(a,b)\subset\mathfrak m,\quad \gcd(a,b)=1,
\quad\epsilon\in R^*.
\end{gathered}
\tag{1}
\]
Assume ord_m(a)=1. The cited proof gives A=B1 of order one,
a=A u+bv with u a unit and v in m, and
B2,Q in m(A)+m^2(b^2). Define
\[
\begin{gathered}
r'=r/u,\qquad H'=(H+vG)/u,\qquad G'=G,\\
a'=A,\quad b'=b,\quad \epsilon'=\epsilon u,
\quad B_1'=A,\quad B_2'=(B_2+vA)/u,\\
P'=P/u,\qquad Q'=Q/u.
\end{gathered}
\tag{2}
\]
All coefficients are invariant, so direct substitution in (1)
proves the same conic and derivative identities for the primed
data. For example NG'=epsilon' b' r'+a', and
NH'=-epsilon' a' r'+B2'. The basis change has unit determinant,
and H' still has zero whole residue. Also J2=(a',b') is unchanged.

Drop the primes from now on. In this normalized basis B1=a,
ord_m(a)=1, and B2,Q belong to m(a)+m^2(b^2). Choose invariant
coefficients beta,zeta in m and delta,q in m^2 such that
\[
\begin{gathered}
B_2=a\beta+b^2\delta,\qquad Q=a\zeta+b^2q,\\
P=a^2+ab\beta+b^3\delta,\qquad
\operatorname{in}_{\mathfrak m}(P)
 =\operatorname{in}_{\mathfrak m}(a)^2.
\end{gathered}
\tag{3}
\]
This change does not rescale N. It only changes its chosen
first-degree and second-degree basis elements and the corresponding
generator P of I1.

## 2. Division in the actual algebra

Expanding the normalized conic gives the identity
\[
\begin{gathered}
aF+b^2D=0,\\
F=\epsilon aG^2+2\epsilon bGH-2\beta G+2H-\zeta,\\
D=\epsilon H^2-2\delta G-q.
\end{gathered}
\tag{4}
\]
The quotient R/(a) is a regular local ring of dimension one,
and hence a DVR. Since gcd(a,b)=1, b is nonzero in that quotient.
Thus a,b^2 is an R-regular sequence. Tensoring its injective
multiplication maps with the flat algebra A_R shows that b^2
is a nonzerodivisor on A_R/aA_R. Reducing (4) modulo a proves
D belongs to aA_R. There is consequently an actual element
\[
\boxed{\qquad U=(\epsilon H^2-2\delta G-q)/a\in A_R.\qquad}
\tag{5}
\]
This is not division by a unit and is not a completed-ring
construction. Its existence is proved by the regular sequence.
Since D belongs to F4 and a is invariant and nonzero,
a N^5U=N^5D=0 implies U belongs to F4. Further,
N^2H=-epsilon aP, so Leibniz's formula gives
\[
\begin{gathered}
N^4U=6\epsilon^3aP^2\ne0,\qquad \deg_N U=4,\\
2H=\zeta+2\beta G-\epsilon aG^2-2\epsilon bGH-b^2U,
\qquad H\in\mathfrak mF_4.
\end{gathered}
\tag{6}
\]
The second equality is (4) after cancellation of the nonzero a.
Every element displayed on its right has N-degree at most four,
and every coefficient belongs to m, proving the last membership.
It does not express H polynomially in G,U: moving the GH term
to the left introduces 1+epsilon bG, which is not known to be
a unit in A_R. Only the stated finite-module membership is used.

## 3. The fourth-image ideal over the transverse DVR

The retained exact divisor filtration gives I4=P^2 J4, with
J4 an ideal of R. The actual nonprincipality theorem106 makes
J4 proper and maximal-primary. These are separate retained
inputs, not consequences of a numerical check.[^images]
Equation (6) puts a in J4. Since N^2G=epsilon bP, the actual
element G^2 gives N^4(G^2)=6epsilon^2b^2P^2, so b^2 is in J4.

Choose a complementary regular parameter t, so m=(a,t), and
put k=length_R R/(a,b). In the DVR C=R/(a), the nonzero b
has valuation k. Every ideal of C is principal. Because J4
contains a and b^2 but is proper, its image is (t^n) for a
unique integer n with 1<=n<=2k. Taking preimages gives
\[
\boxed{\qquad
J_4=(a,t^n),\quad 1\le n\le2k,\quad
\mu_R(I_4)=\mu_R(J_4)=2,\quad
\operatorname{length}_R(R/J_4)=n.
\qquad}
\tag{7}
\]
Here t denotes a lift of the DVR uniformizer. Equality of the
preimage with (a,t^n) is literal: an element of J4 mapping to
t^n differs from t^n by a multiple of a, already in J4.
The two generators are a regular sequence and are minimal.
Multiplication by the nonzero P^2 identifies J4 and I4 as
R-modules, which proves the equality of generator numbers.

The old and new J2 and J4 differ by no substantive choice:
J2 is unchanged, and replacing P by a unit multiple does not
change the ideal I4/P^2. In particular the length bound uses
the actual residual second-image ideal, not its reduction.

## 4. Verification and remaining scope

The basis transformation, conic expansion and differentiation
are exact algebraic identities. The needed quotient/DVR facts
are the regular-parameter quotient theorem and the characterization
of one-dimensional regular local rings as DVRs.[^regular]
The existence of U uses flatness of the actual algebra, which
an abstract formal conic by itself does not supply.

This proof assumes ord_m(a)=1. It does not prove that assumption
in the remaining branch, determine n, generate the whole A_R
from G,U, or exclude a collapsed mixed fiber. It also does not
resolve the arbitrary-frame entry problem for cancellation.
Separate AI reconstructions and finite symbolic tests are not
human expert review or a formal proof of the geometric inputs.
Files through107 remain unchanged.

[^images]: [Exact divisor filtration107](quadratic-constant-divisor-filtration-pass107.md), all-degree valuations; [fourth-image nonprincipality106](mixed-fourth-image-nonprincipal-pass106.md); and [pure quartic row108](mixed-pure-quartic-row-pass108.md), the normalized image row. The latter row is not needed for the construction of U.

[^regular]: Stacks Project, [Lemma 10.106.3, tag 00NQ](https://stacks.math.columbia.edu/tag/00NQ), and [Lemma 10.119.7, tag 00PD](https://stacks.math.columbia.edu/tag/00PD). Complete displayed statements and proofs read for this deduction. The elementary ideal-preimage and flat base-change arguments are given explicitly above.
