# Recognition of the constant-sigma variable-coupling projected line

Working theorem: retain EVERY actual hypothesis of264. Suppose the
projected plane curve is a line, its function-field projection has
degree one, sigma belongs to the exact coefficient field L, and
\(m=k_s\notin\mathbb C\). Then
\[
\boxed{m_s=m_{tt}=0,\qquad
m=at+d\quad(a\in\mathbb C^*,\ d\in\mathbb C),\qquad
A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
This closes the remaining \(m_{tt}\ne0\) alternative in475 by
using a published theorem on nice derivations over a field. It
does not assert arbitrary entry into264, recognize nonlinear
projected curves, or solve unrestricted cancellation.

## 1. Actual input and the three simultaneous degree-one velocities

Retain the full actual chart264 and the complete reduction
[475](principal-paraboloid-constant-sigma-variable-coupling-reduction-pass475-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad Na_0=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
\operatorname{Frac}A=L(v),\quad Nv=1,\quad
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
\operatorname{Frac}A=\mathbb C(y,z,w).
\end{gathered}
\tag{2}
\]
All exact-field and strong-return assumptions are preserved. The
two coefficient partials commute and have joint constants C.
The projected-line hypothesis gives the affine parameter
\(V=\theta\), with \(N\theta\in L^*\), and475 proves
\[
m_s=0,\quad m_t\ne0,\qquad y=-m_tV/2+r,\quad r\in L.
\tag{3}
\]
Write \(p=\sigma\in L\). The actual rows from475 become
\[
\begin{aligned}
Y&=-\frac{m_t}{2}V+r+pX+tX^2,\\
Z&=(m-tm_t)V+2tr+p^2+k_tp+n+(2tp+k)X+t^2X^2,\\
W&=(X+\upsilon)V+w_0+sX^2,\\
\upsilon&=-\frac{(2p+k_t)(-m_t/2)+m_tp+n_s}{m}\in L.
\end{aligned}
\tag{4}
\]
There is no assumption that upsilon is complex. The old global
slice u is not renamed or replaced by any coefficient function.

Extend N to \(A[u]\) by \(Nu=0\), and retain475's actual LND
\[
\Delta=a_0N-(NX)E.
\tag{5}
\]
It fixes X, commutes with E, kills L in the fraction field, and
is locally nilpotent on the original ring. Indeed it is the
derivation \(a_0N\) at fixed X on \(\mathcal B_{a_0}=A_{a_0}[X]\),
and it preserves the original ring. Put
\(\tau_0=a_0N\theta\in L^*\). Equations(4) give
\[
\Delta Y=-\frac{m_t}{2}\tau_0,\qquad
\Delta Z=(m-tm_t)\tau_0,\qquad
\Delta W=(X+\upsilon)\tau_0.
\tag{6}
\]
All three displayed velocities are killed by Delta. Thus
\(\Delta^2Y=\Delta^2Z=\Delta^2W=0\).
This conclusion uses all three actual coordinates at once,
not only the two-coordinate Riccati subcase of475.

## 2. A published linear invariant over the fixed-coordinate field

Localize the ACTUAL ring at \(\mathbb C[X]\setminus\{0\}\).
Since Delta fixes X, it extends as a nonzero LND to
\[
\mathscr K[Y,Z,W],\qquad \mathscr K=\mathbb C(X).
\tag{7}
\]
It remains locally nilpotent because all inverted elements are
Delta-invariant. The localization is a polynomial THREE-ring
over the characteristic-zero field \(\mathscr K\), and all its
three displayed variables have Delta-degree at most one by(6).

Theorem3.1(i) of
[Dasgupta--Gupta, Nice derivations over principal ideal domains](https://arxiv.org/html/1701.03635v1),
stating Wang's result, supplies a nonzero linear invariant in the
three variables for any such nonzero nice LND over a field.
The irreducibility condition stated separately in part(iii)
is not a hypothesis of part(i). It follows that there are
\(A_1,B_1,C_1\in\mathbb C(X)\), not all zero, such that
\[
-\frac{A_1(X)}2m_t+B_1(X)(m-tm_t)
                 +C_1(X)(X+\upsilon)=0.
\tag{8}
\]
Here only the nonzero fraction-field scalar \(\tau_0\) was
canceled. The resulting linear invariant is NOT being promoted
to an original complex polynomial coordinate.

The element X is transcendental over L: it is affine with nonzero
coefficient in the original global slice over \(\operatorname{Frac}A\).
Thus(8) is an identity in the rational function field \(L(X)\).
In particular formal differentiation in X fixing ALL of L is
valid, independently of the original coefficient partials.

## 3. Either coefficient case forces m to be affine

First suppose \(C_1=0\). Choose a complex number \(x_*\) that
is not a pole of \(A_1,B_1\) and does not kill both. This is
possible because one rational function is nonzero and C is
infinite. Evaluation of(8) gives constants \(\alpha,\beta\in\mathbb C\),
not both zero, with
\[
\alpha m_t+\beta(m-tm_t)=0.
\tag{9}
\]
This evaluates only the independent rational-function variable X;
it does not specialize t, s, L, or any actual fiber.

Now suppose \(C_1\ne0\). Divide(8) by it and rearrange to
\[
X+\upsilon=a(X)m_t+b(X)(m-tm_t),\qquad a,b\in\mathbb C(X).
\tag{10}
\]
Formal differentiation in X fixing L gives
\[
1=a'(X)m_t+b'(X)(m-tm_t).
\tag{11}
\]
Choose \(x_*\in\mathbb C\) away from the finitely many poles
of these two rational derivatives. Evaluation gives
\[
\alpha m_t+\beta(m-tm_t)=1,\qquad \alpha,\beta\in\mathbb C.
\tag{12}
\]
The constants cannot both vanish, since their combination is one.

Apply the ORIGINAL partial \(\partial_t\), at fixed s, to(9)
or(12). In either case,
\[
(\alpha-\beta t)m_{tt}=0.
\tag{13}
\]
Since t is transcendental over C and the constant pair is
nontrivial, \(\alpha-\beta t\ne0\). Therefore \(m_{tt}=0\).
Together with(3), joint constants give
\(m_t=a\in\mathbb C^*\) and \(m-at=d\in\mathbb C\).
No rationality of \(\ker_L\partial_s\) or L was used.

## 4. The retained actual-coordinate recognition applies

The hypotheses of475 Section8 are now satisfied, so its proof
constructs actual coordinates for the kernel of Delta and then
an actual E-invariant coordinate. More explicitly it first
forces \(\upsilon=\upsilon_0\in\mathbb C\) and uses
\[
U_0=Z+2dY/a,\qquad
V_0=W+2(X+\upsilon_0)Y/a.
\tag{14}
\]
The ring \(\ker_{\mathcal B}\Delta=\mathbb C[X,U_0,V_0]\)
is an actual polynomial three-ring, stable under E, in which
X is a genuine nonzero degree-one coordinate for E. Primitive
division followed by Daigle's theorem, stated as
[Dasgupta--Gupta Theorem4.8](https://arxiv.org/html/1701.03635v1),
gives an E-invariant coordinate of this ring and hence of
\(\mathcal B\). The original slice makes A affine and regular;
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
then gives \(A\simeq\mathbb C^{[3]}\).
The exact hypotheses and polynomial inverses for this endpoint
are written in475, not supplied merely by the field localization(7).

## 5. Dependencies, checks, and remaining scope

The complete held475 source was read through EOF before this
proof, including all its exceptional-column and zero-slope cases.
Its conclusions \(m_s=0\) and \(\lambda=-m_t/2\) are essential
inputs, not new assumptions added to the theorem. The primary
statements of the three published endpoints were inspected directly.
The new use of Theorem3.1(i) is only over the field C(X), not over
the PID C[X]; no local result is itself called a global coordinate.

Fresh unsaved root calculation809003 verifies the full velocity
row(6), its three squared-derivation identities and(13). The
specialization, field and published-theorem steps are the written
proof above, not consequences of symbolic tests. Separate AI
outline audits and final source reviews are recorded in the ledger.

This recognizes the constant-sigma, birational projected-line
variable-coupling branch within the full supplied chart264. It
does not cover nonconstant sigma, nonlinear projected curves,
other initial kernels or general entry. The earlier264/325
dependencies remain retained rather than recursively recertified.
No saved checker was executed, imported, compiled or rerun.
No historical novelty, human-expert review, Lean certification,
public submission or unrestricted cancellation is claimed.
