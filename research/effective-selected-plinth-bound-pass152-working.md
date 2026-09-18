# An effective plinth bound from the speed determinant and minimal bad degree

For an actual dense three-good frame, the primitive selected action
has a global derivative value bounded explicitly by the speed
determinant and the minimum last-coordinate time degree under
fixed-good polynomial shears. If that minimum is \(\mu\), then
\(\Omega^{2(\mu+1)}\) belongs to the primitive plinth ideal.

More precisely, its generator divides
\((\Omega\operatorname{rad}\Omega)^{\mu+1}\).
This controls multiplicities as well as the support already confined
to \(\Omega=0\) in pass 151. It does not make a nonconstant derivative
value a slice or rule out a full divisor constant extension there.

## 1. Actual hypotheses and inherited algebraic inputs

Assume the actual dense setting of passes 139 and 151:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
E^2X=E^2Y=E^2Z=0,\\
\mathbf a=(EX,EY,EZ)^t,\qquad
\operatorname{trdeg}_{\mathbb C}\mathbb C(\mathbf a)=2,\qquad
H(\mathbf a)\ne0
\quad\text{for every nonzero homogeneous }H,\\
T=\partial_W,\qquad N=[u^2]T|_A\ne0,\qquad
S=\ker_A N=\mathbb C[P,Q],\qquad L=\operatorname{Frac}S,\\
\Omega=\det[\mathbf a,\mathbf a_P,\mathbf a_Q]\in S\setminus\{0\},
\qquad
\mathcal D=\operatorname{Jac}_{X,Y,Z,W}(P,Q,u,\,\cdot\,).
\end{gathered}
\tag{1}
\]
The polynomial \(H\) in the density condition has three independent
formal variables and complex coefficients. The displayed four
generators of \(B\) are actual polynomial coordinates. The slice
\(u\) is not presumed an ambient coordinate.

The retained intrinsic quotient input makes \(A\) a UFD and
\(S\to A\) faithfully flat. The invariant ring is factorially
closed. The actual speed gcd theorem gives
\(\gcd_S(a_1,a_2,a_3)=1\), so at every height-one prime of \(S\)
at least one good speed survives. The all-degree proof in pass 151
gives \(N=\Omega\mathcal D\), with \(\mathcal D|_A\) a primitive
nonzero LND of kernel \(S\), and a slice on \(A_\Omega\).
These are explicit inherited hypotheses and conclusions, not
consequences of a formal speed tuple.[^1]

The principal-plinth argument in pass 27 applies to this actual inclusion:
\[
\begin{gathered}
\mathfrak p_{\mathcal D}:=\mathcal D(A)\cap S=\alpha S,\qquad
0\ne\alpha\in S,\\
\mu=\min_{C\in\mathbb C[X,Y,Z]}\deg_E(W+C)\in\mathbb Z_{\ge0}.
\end{gathered}
\tag{2}
\]
Here \(\alpha\) is determined up to a complex unit. The set defining
\(\mu\) is nonempty and consists of nonnegative integers, because
\(W+C\) remains an actual coordinate with \(T(W+C)=1\).
Only the existence of this attained minimum and the invariance
under these shears will be needed.[^2]

## 2. A coefficient-derivative word has a controlled pole

Fix an irreducible \(p\in S\) dividing \(\Omega\), and write
\(V_p=S_{(p)}\), a DVR with uniformizer \(p\). Put
\(e=\operatorname{ord}_p\Omega>0\) and
\(A_{V_p}=A\otimes_S V_p\).
Choose a good speed \(s\notin(p)\), reorder the other two as
\(t,b\), and use the actual fixed-first-good chart with ratios
\(\tau=t/s,\rho=b/s\). Reordering affects only the sign of the
following determinant:
\[
\det\frac{\partial(\tau,\rho)}{\partial(P,Q)}
=\pm\frac{\Omega}{s^3},\qquad
\partial_\tau,\partial_\rho
\in p^{-e}\bigl(V_p\partial_P+V_p\partial_Q\bigr).
\tag{3}
\]
Indeed the two ordinary derivatives of each ratio lie in \(V_p\),
and the determinant of their matrix has valuation \(e\).
Its inverse therefore has entries in \(p^{-e}V_p\).
These inverse-matrix derivations are the coefficient partials on
\(L\) from pass 139. No equality of \(L\) with
\(\mathbb C(\tau,\rho)\), and no unramified extension assertion,
is used.

Both \(\partial_P\) and \(\partial_Q\) preserve \(V_p\): writing
an element as a quotient with denominator outside \((p)\), its
derivative still has denominator outside \((p)\). Thus, for either
\(\delta=\partial_\tau\) or \(\partial_\rho\),
\[
\begin{gathered}
\delta(V_p)\subset p^{-e}V_p,\qquad
\delta(p^{-A}V_p)\subset p^{-(A+e+1)}V_p\quad(A\ge1),\\
M_e(d)=d(e+1)-1\quad(d\ge1),\qquad
\delta_d\cdots\delta_1(V_p)\subset p^{-M_e(d)}V_p
\quad(\delta_i\in\{\partial_\tau,\partial_\rho\}).
\end{gathered}
\tag{4}
\]
The second inclusion follows by differentiating \(p^{-A}f\)
and using \(\delta p\in p^{-e}V_p\). The first derivative of a
regular coefficient costs at most \(e=M_e(1)\), not \(e+1\).
Each later derivative increases the pole bound by at most \(e+1\).
Since \(e>0\), induction proves the last inclusion. This is a
bound for every ordered word, not just for repeated derivatives
in one direction. It already accounts for derivatives of the
inverse-matrix coefficients.

## 3. Descending peeling and the corrected second tail

For now let \(m=\deg_E W\) for any one of the actual fixed-good
frames. In the selected chart write
\(W=\sum_{j=0}^m w_jX^j\), renaming the selected first good
coordinate \(X\) in this section. Its speed \(s\) is a unit in
\(V_p\), so \(y,z,w_j\in A_{V_p}\) and this is also its
\(X\)-degree.

For independent formal \(U,V\), let
\[
\begin{gathered}
H_d(f;U,V)=\sum_{i+j=d}
\frac{\partial_\tau^i\partial_\rho^j f}{i!j!}\,U^iV^j,\qquad
f_j=w_j-\sum_{k=j+1}^m H_{k-j}(f_k;y,z)\in L,\\
f_m\in V_p,\qquad
f_j\in p^{-M_e(m-j)}V_p\quad(0\le j<m).
\end{gathered}
\tag{5}
\]
The recurrence and membership in \(L\) are the canonical peeling
identities from pass 139. To prove the bounds, first note
\(A_{V_p}\cap L=V_p\): clearing an invariant denominator reduces
this to \(A\cap L=S=\ker_A N\).
Consequently \(f_m=w_m\in V_p\).

Suppose the higher coefficients have already been bounded. An
order-\((k-j)\) derivative of \(f_k\), for \(k<m\), has pole
at most
\(M_e(m-k)+(k-j)(e+1)=M_e(m-j)\), by the second inclusion
in (4). For \(k=m\), the word bound in (4) gives the same result.
Factorials are complex units. Evaluation at the integral pair
\(y,z\) therefore puts the entire difference in
\(p^{-M_e(m-j)}A_{V_p}\). Since it lies in \(L\), the same
intersection argument puts it in \(p^{-M_e(m-j)}V_p\).
This proves (5) without requiring the lower \(w_j\) to be
invariant.

Use the signed first and corrected second negative coefficients:
\[
\begin{gathered}
f_{-1}=-\sum_{j=0}^m H_{j+1}(f_j;y,z)\in L,\qquad
f_{-1}\in p^{-M_e(m+1)}V_p,\\
\Psi(U,V)=-\sum_{j=0}^m H_{j+2}(f_j;U,V)
-H_1(f_{-1};U,V)
\in p^{-M_e(m+2)}V_p[U,V],\\
N'=\frac{N}{s^2},\qquad N'\bigl(\Psi(y,z)\bigr)=1 .
\end{gathered}
\tag{6}
\]
The first bound follows from (5) and (4), with total derivative
index \(m+1\); evaluation is integral and the result lies in
\(L\). Each term in the second line has the total pole bound
\(M_e(m+2)\). The last assertion is the exact tail identity from pass 139:
one subtracts \(X^{-1}\Theta(f_{-1})\) before taking the
\(X^{-2}\) coefficient. The negative correction in (6) is
essential.[^3]
When \(m=0\), the lower-coefficient range in (5) is empty; the
two estimates in (6) still follow from the first and second
derivatives of the regular \(f_0\).

## 4. Clearing the local primitive slice

Set \(K=M_e(m+2)\). Since \(N=\Omega\mathcal D\), the rational
slice and its cleared value satisfy
\[
\begin{gathered}
r_p=\frac{\Omega}{s^2}\Psi(y,z),\qquad
\mathcal D r_p=1,\qquad
r_p\in p^{-(K-e)}A_{V_p},\\
K-e=(m+1)(e+1),\qquad
b_p=p^{(m+1)(e+1)}r_p\in A_{V_p},\qquad
\mathcal D b_p=p^{(m+1)(e+1)} .
\end{gathered}
\tag{7}
\]
All identities take place in the fraction field before the
explicit denominator clearance. Multiplication by \(\Omega/s^2\)
improves the bound by exactly its valuation \(e\); no inverse
of \(p\) has been silently admitted into \(A_{V_p}\).

The plinth commutes with this invariant localization.
If \(r=a/t\in A_{V_p}\), with \(a\in A\) and
\(t\in S\setminus(p)\), has
\(\mathcal D r\in V_p\), then
\(\mathcal D a=t\,\mathcal D r\in A\cap L=S\).
Thus \(\mathcal D a\) belongs to the global plinth.
The opposite inclusion follows by localizing a global preimage.
Using (2) and (7) gives
\[
\bigl(\mathcal D(A_{V_p})\cap V_p\bigr)
=\mathfrak p_{\mathcal D}V_p=\alpha V_p,\qquad
\operatorname{ord}_p\alpha\le(m+1)(e+1).
\tag{8}
\]
This localization argument is about the first-image plinth.
It asserts no corresponding equality or principality for higher
image ideals.

## 5. Minimizing the bad degree and taking a global product

Replace \(W\) by \(W+C(X,Y,Z)\), with \(C\) realizing the
minimum \(\mu\) in (2). This is an actual elementary coordinate
change, with polynomial inverse \(W=\widetilde W-C\).
The original \(T\) still kills all three goods and takes value
one on \(\widetilde W\), so it is exactly the new selected
partial. Hence \(N,S,\mathbf a,\Omega,\mathcal D\), and the
chosen \(P,Q,u\) are all unchanged. Apply (8) with \(m=\mu\).
This uses only fixed-good shear invariance, not arbitrary good
coordinate changes or the first-tail primitivity theorem in pass 145.

For a prime \(p\nmid\Omega\), the slice on \(A_\Omega\) from pass 151
gives \(\operatorname{ord}_p\alpha=0\). Factor
\(\Omega=c\prod_i p_i^{e_i}\), with \(c\in\mathbb C^*\) and
distinct irreducibles \(p_i\). Define
\(\operatorname{rad}\Omega=\prod_i p_i\), up to a complex unit;
it is 1 if \(\Omega\) is constant. The UFD \(S\) and all the
local inequalities now give
\[
\begin{gathered}
\operatorname{ord}_{p_i}\alpha\le(\mu+1)(e_i+1),\qquad
\boxed{\ \alpha\mid
(\Omega\operatorname{rad}\Omega)^{\mu+1}\ },\\
(\Omega\operatorname{rad}\Omega)^{\mu+1}
\in\mathcal D(A)\cap S,\qquad
\boxed{\ \Omega^{2(\mu+1)}\in\mathcal D(A)\cap S\ } .
\end{gathered}
\tag{9}
\]
For the last assertion use \(e_i+1\le2e_i\).
Membership gives an actual polynomial preimage in \(A\):
choose \(a_\alpha\in A\) with \(\mathcal D a_\alpha=\alpha\)
from the definition of the principal plinth and multiply it
by the corresponding quotient in \(S\).
If \(\Omega\) is a complex unit, the same statement gives a
slice, consistently with pass 151.

## 6. Scope of the effective value

The conclusion bounds the vanishing exponents of the primitive
plinth by the selected content orders and the fixed-good minimum.
It does not identify those exponents, claim that the estimate is
sharp for actual frames, or bound the original-coordinate degree
of a preimage. The proof is a finite algebraic derivative and
valuation argument, not a numerical search or a test certificate.

In particular a nonconstant \(\Omega^{2(\mu+1)}\) is a derivative
value, not a slice value of 1. Nontrivial full divisor constant
extensions on \(\Omega=0\) remain possible within the current
unresolved hypotheses; this note proves neither their existence
in an actual frame nor their exclusion. The separate arbitrary
three-good coordinate-entry problem also remains untouched.
No frozen file, runtime result, or earlier theorem is changed.

## Sources

1. [The primitive Jacobian factor and its off-determinant slice151](dense-all-degree-primitive-jacobian-factor-pass151-working.md),
   Sections 1--6. Actual quotient and speed-gcd inputs, exact
   \(N=\Omega\mathcal D\), primitive action, ratio determinant,
   and the slice on \(A_\Omega\). Its full proof was independently
   reread; the cited external quotient theorems were not newly audited.
2. [Fixed-good shear invariance and minimal degree141](dense-shear-minimal-tail-pass141-working.md),
   Sections 1--2 and 4. Actual elementary inverse, unchanged
   selected partial and intrinsic data, and the attained minimum.
   No later first-tail factor theorem is required here.
3. [Actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 2 and 4--6, and [the signed negative coefficients139](dense-negative-tail-relations-pass139-working.md),
   Sections 1--3. Polynomial membership before localization,
   canonical recurrence, and the corrected second-tail slice.
4. [Intrinsic principal plinth27](intrinsic-plinth-boundary-pass27.md),
   Sections 1--3. The faithful-flat UFD hypotheses and the
   first-image gcd proof of principality were reread completely.
   This is retained published input, not a new principality claim.

[^1]: Source 1 and its explicit retained quotient and speed-gcd dependencies.
[^2]: Sources 2 and 4.
[^3]: Source 3.
