# A pure quartic row in the remaining mixed branch

The remaining two-dimensional second-degree image admits an
explicit fourth-degree basis containing 1,G,G squared and the
specified quartic c. The intersection of its pure rank-four
piece with F3 is controlled by one exact gcd relation. This
gives coefficient restrictions and a one-way speed constraint,
not an exclusion of the remaining mixed fiber.

## 1. Actual hypotheses and the pure pieces

Work in the actual collapsed mixed quadratic sector with L(m)
nonzero, over R=S_m. Retain the flat domain A_R, full kernel R,
generic polynomial line, and finite free modules
F_j=ker(N^(j+1)) of rank j+1. The preceding results give
\[
\begin{gathered}
A_R/\mathfrak mA_R=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\\
\epsilon_f=G-G^2,\quad e_1=G^2,\qquad
\bar N=(\lambda\epsilon_f+\rho e_1)\partial_c,\qquad
\lambda,\rho\in\mathbb C^*,\\
\mathcal W_2=\mathbb C1+\mathbb CG,\qquad
\mathcal W_1=\mathbb C,\qquad
\dim\mathcal W_3\le3,\qquad \deg_N c=4.
\end{gathered}
\tag{1}
\]
Every F3 element has constant values on both reduced component
lines. Here G is the specified actual separator element in F2,
not a generic coordinate introduced after localization.[^actual]

Since G has nonconstant whole residue, W1=C implies G is not
in F1. Thus d=N squared of G is a nonzero invariant and G has
degree exactly two. The characteristic-zero Leibniz rule gives
N fourth of G squared equal to 6d squared. The residues 1,G,G
squared are independent: G has minimal polynomial G squared
times (G-1), of degree three, in the whole Artin algebra.
The variable c is independent of that entire Artin algebra.
Consequently
\[
\begin{gathered}
E=R\{1,G,G^2\},\qquad
E_c=R\{1,G,G^2,c\},\\
E\text{ and }E_c\text{ are pure in }A_R,\\
F_4=R\{1,G,G^2,c,H_4\}
\quad\text{for some actual }H_4\in F_4.
\end{gathered}
\tag{2}
\]
The purity assertion is the all-ideal residue-basis lemma107.
The basis extension uses independent classes in the finite
free module F4/mF4, which follow from independent whole
residues. E is not F2: its element G squared has degree four.
No independence of the fifth whole residue is asserted.

## 2. The exact image row and a cubic cancellation

Put d=N^2G, k=N^4c and l=N^4H4. These are elements of R,
with d and k nonzero. In the basis (2),
\[
\begin{gathered}
N^4|_{F_4}=(0,0,6d^2,k,l),\qquad
I_4=(6d^2,k,l),\\
F_3/R\{1,G\}\simeq
\ker\bigl(R^3\xrightarrow{(6d^2,k,l)}I_4\bigr)
\simeq R^2 .
\end{gathered}
\tag{3}
\]
For the last freeness, the independent residues of 1,G split
their span off the free rank-four F3. Thus (3) is an exact
module description, not an assumption that a rank-one ideal
is free. The row need not be a minimal generating row.

Take a greatest common divisor g0 of 6d squared and k in the
UFD R, and write
\[
\begin{gathered}
A_0=6d^2/g_0,\qquad B_0=k/g_0,\qquad
\gcd(A_0,B_0)=1,\qquad
V_3=B_0G^2-A_0c\in F_3,\\
\boxed{\quad F_3\cap E_c=R\{1,G,V_3\}.\quad}
\end{gathered}
\tag{4}
\]
Indeed the last two coordinates of an element of E_c lie in
the kernel of the row (6d squared,k) precisely when they
are a multiple of (B0,-A0). Coprimality proves that exact
syzygy statement over R. V3 is independent of 1,G because
A0 is nonzero and (2) is a basis of E_c. Its degree is at
most three; exact degree three is not assumed.

On the double reduced line G is zero, while on the simple
line G is one. Hence V3 has slope -A0(m) in c on both
lines. The actual zero-slope theorem for every F3 element
therefore forces A0 into m. If B0 is a unit, V3 reduces
to a nonzero scalar times G squared and supplies the third
Artin direction. Also N c belongs to F3 and has residue
lambda G+(rho-lambda)G squared. We have proved
\[
\begin{gathered}
A_0\in\mathfrak m,\\
B_0\in R^*\ \Longrightarrow\ \mathcal W_3=\mathcal D,\qquad
\rho\ne\lambda\ \Longrightarrow\ \mathcal W_3=\mathcal D,\\
\dim\mathcal W_3=2\ \Longrightarrow\
B_0\in\mathfrak m,\quad \rho=\lambda,\quad
(A_0,B_0)\text{ is a proper }\mathfrak m\text{-primary
complete intersection}.
\end{gathered}
\tag{5}
\]
For the ideal assertion both entries are nonzero, coprime
nonunits in the regular local surface R. They form a regular
sequence and their ideal has radical m. None of the displayed
implications is reversed. In particular equal speeds do not
force W3 to have dimension two.

## 3. The normalized proper-second-image row

Here are more explicit coefficients when the second-image
ideal J2 is proper. Choose F2=R{1,G,H2} with H2 having zero
whole residue, and shift a first-degree basis element so that
F1=R{1,r}, r=aG+bH2 and r has zero whole residue. Then
a belongs to m. The elementary conic computation gives
\[
\begin{gathered}
P=Nr\ne0,\qquad \gcd(a,b)=1,\qquad
NG=\epsilon b r+B_1,\quad NH_2=-\epsilon a r+B_2,\\
I_2=\epsilon P(a,b),\qquad
d=N^2G=\epsilon bP,\qquad \epsilon\in R^*,\\
J_2=(a,b)\subseteq\mathfrak m,\qquad
k=P^2L,\qquad l=P^2M,\qquad L,M\in R,\\
I_4=P^2J_4,\qquad
\boxed{\quad J_4=(6\epsilon^2b^2,L,M),\quad
\gcd(P,L)=1.\quad}
\end{gathered}
\tag{6}
\]
The assertions in (6) use different gates, which must be kept
separate. Torsion freeness of F2/F1 gives gcd(a,b)=1.
At every height-one base prime the exact divisor filtration107
gives equal valuations for I2 and I1. Thus epsilon has no
prime factor and is a unit, independently of full W2=D.
The actual proper-J2 premise puts both a and b in m.

All height-one valuations of I4 are twice those of I1=(P).
This proves divisibility by P squared and the stated J4 row.
The selected c has *exactly* that valuation at every quadratic
constant divisor through m, by the additional actual boundary
gate in normal-form107. At degree-one constant divisors P
is a unit. Thus L has no common prime divisor with P.
The exact valuation of this selected element is an extra
input; generic quartic degree alone does not prove it.[^divisor]

The actual nonprincipality theorem106 makes J4 proper after
removing its common divisor, so L,M belong to m and J4 is
m-primary with two or three minimal generators. No minimality
of the three displayed row entries is asserted. Also P belongs
to m because r has zero whole residue and N preserves the
fiber ideal. Since P and L are nonzero coprime nonunits,
(P,L) is another m-primary parameter ideal.

Equivalently, in (4) one may take
g0=P squared times D, where D=gcd(6epsilon squared b squared,L).
Then A0=6epsilon squared b squared/D and B0=L/D.
The conditions (5) apply to this exact normalized pair.
They do not imply that J2, J4, (P,L), or (A0,B0) is reduced.

For comparison only, if J2 were the unit ideal, a in m would
make b a unit. Then d squared would be a unit multiple of
P squared. The selected-c valuation gate would make A0 a
unit, contradicting (5). This is an alternative unit-branch
observation. The separate
[unit-second-image proof108](mixed-unit-second-image-exclusion-pass108.md) gives a
stronger whole-algebra route without using the selected-c
boundary condition; that independent proof is not an input
to (2)--(5).

## 4. Verification and limits

The companion
[checker](mixed_pure_quartic_checks_pass108.py) checks finite
row/syzygy and mixed-Artin coefficient identities in its first
method. Its second method checks the general-epsilon sharp
conic rearrangement from
[proper-image jets108](mixed-proper-second-image-jets-pass108.md)
and the exact rational quartic derivative and rearrangement
from [smooth-generator108](mixed-smooth-generator-quartic-pass108.md).
The latter proof, not the rational computation, establishes
that the divided quartic is an element of the actual algebra.
These two methods do not prove purity, divisor classification,
the all-element intersection (4), or existence of an actual
original frame.

The author command was
`/opt/anaconda3/bin/python research/mixed_pure_quartic_checks_pass108.py`.
Its first assertion-bearing run passed both methods in 0.259
unittest seconds, exit zero, output chunk f598dd. The command
tool reported 1.372963 seconds of wall time. A coefficient
transcription in the unused draft expansion of H squared was
corrected during the complete code read before that run. No
failed test, additional method, or broader regression is hidden
in this two-method count. The saved six-equation proof and full
checker were read through EOF before execution.

This note does not identify E with F2, make the whole F4
residue map injective, conclude that J4 is principal, or
exclude the proper-J2 branch. Its exact missing-residue
information is the rank-two row kernel (3) and the
at-most-cubic cancellation (4). All files through107 remain
unchanged.

[^actual]: [Final mixed branch107](mixed-full-artin-exclusion-frontier-pass107.md); [third-degree rank defect105](mixed-cubic-rank-defect-pass105.md), including zero reduced slopes; [mixed third-degree image105](mixed-third-degree-image-pass105.md); and [degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md). The purity input is [residue-basis purity107](residue-basis-purity-pass107.md).

[^divisor]: [Exact actual DVR filtration107](quadratic-constant-divisor-filtration-pass107.md), all-degree ideal formula; [selected-c gate107](quadratic-divisor-normal-form-gates-pass107.md), Section 6; [degree-one DVR slice105](mixed-cubic-rank-defect-pass105.md); and [actual fourth-image nonprincipality106](mixed-fourth-image-nonprincipal-pass106.md).
