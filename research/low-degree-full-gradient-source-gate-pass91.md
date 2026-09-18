# The full-gradient criterion and the zero-level limitation

The relative degree bound supplies a genuine generic coordinate, so
Bhatwadekar--Dutta's polynomial-coordinate criterion has an exact
application target. Its missing premise is a unit gradient in the full
two-variable polynomial ring. The unit gradient on the actual zero
hypersurface proved in pass90 is weaker. This note records the criterion
and a precise control, not an application closing the remaining case.

## 1. Actual input and the generic-coordinate gate

Retain the original nonconical frame and the complete conclusions of
[quadratic-potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md) and
[open-free90](nonconical-open-free-derivation-pass90.md). In particular,
\[
\begin{gathered}
S=\mathbb C[s_1,s_2],\quad S^\circ=S[1/\Omega],\quad
K=\operatorname{Frac}S,\quad \Omega\ne0,\\
\mathscr P=S^\circ[Y,Z],\qquad
A_\Omega=\mathscr P/(F),\qquad 1\le\deg_{Y,Z}F\le3,\\
A_K=K[v]=K[y,z],\qquad
(F_Y,F_Z)A_\Omega=A_\Omega.
\end{gathered}
\tag{1}
\]
Here F is an irreducible generator of the actual presentation kernel.
The formal variables Y,Z are independent; their images y,z in the
quotient are not. The original four-variable polynomial cylinder and
the inclusion \(A=S[A_1,A_2,c]\) remain part of the inherited problem.
They do not identify \(\mathscr P\) with that cylinder as an S-algebra.

The elementary final argument of cubic-relation90 gives a K-linear
form L in Y,Z whose image generates \(A_K\). Complete L to a
linear coordinate pair L,M over K. There is \(P(T)\in K[T]\)
with \(\overline M=P(\overline L)\). The quotient map is therefore
the graph map, with kernel \((M-P(L))\). Since F generates the same
prime ideal, some \(a\in K^*\) satisfies
\[
F=a(M-P(L)),\qquad K[Y,Z]=K[L,M]=K[L,F].
\tag{2}
\]
Thus F is a generic coordinate of \(\mathscr P\), not merely a
polynomial with quotient \(K[v]\). This proof uses the actual
low-degree embedding result, and does not invoke an unproved
extension of a birational parametrization.

## 2. The exact original primary theorem

Bhatwadekar--Dutta, Proposition 4.4, assumes a Noetherian domain
containing a characteristic-zero field and a generic variable in its
two-variable polynomial ring. Comaximal partial derivatives imply
that this variable is a coordinate.[^bd]
The converse follows by differentiating a polynomial coordinate
inverse. Applied with the UFD \(S^\circ\), the exact criterion is
\[
\begin{gathered}
(F_Y,F_Z)\mathscr P=\mathscr P
\quad\Longleftrightarrow\quad
\mathscr P=S^\circ[F,G]\text{ for some }G\in\mathscr P,\\
(F_Y,F_Z)\mathscr P=\mathscr P
\quad\Longrightarrow\quad A_\Omega=S^\circ[\overline G].
\end{gathered}
\tag{3}
\]
The base meets every ring hypothesis. It is the first ideal equality
that has not been proved. In contrast, the last equality in (1) says
only \((F,F_Y,F_Z)\mathscr P=\mathscr P\).

Babu--Das Theorem 1.1 restates this criterion explicitly, including
the generic-coordinate premise. Their broader retract/fibration
results keep the base ring fixed; the absolute cylinder
\(A[u]\simeq_{\mathbb C}\mathbb C^{[4]}\) is not the relative
polynomial presentation over \(S^\circ\) required by those results.[^babu]
Even (3) would recognize only the principal open, not automatically A.

## 3. An actual formal-ring LND, with a different fixed ideal

The generic graph also gives a useful exact interpretation of (3).
Define on the genuine ring \(\mathscr P\)
\[
\mathcal D_F=F_Z\partial_Y-F_Y\partial_Z,\qquad
\mathcal D_F(F)=0,\qquad
\mathcal D_F(\mathscr P)\mathscr P=(F_Y,F_Z)\mathscr P.
\tag{4}
\]
Over K, equation (2) gives \(\mathcal D_F(L)=a\det\operatorname{Jac}(L,M)
\in K^*\). Thus \(\mathcal D_F\) is a constant translation derivation
in the coordinates F,L over K. It preserves \(\mathscr P\) by its
displayed polynomial coefficients, and local nilpotence descends from
\(K[Y,Z]\) by injectivity. Hence (4) is an actual
\(S^\circ\)-LND on the formal polynomial ring.

Its induced field on \(\mathscr P/(F)\) is fixed-point-free by (1).
This does not make (4) fixed-point-free on all of \(\mathscr P\).
No identification of its full invariant ring with \(S^\circ[F]\)
is required for this argument or asserted without a further gate.

## 4. The critical locus can miss the entire zero level

The localized Weitzenbock control from
[source-scope90, Section 5](homogeneous-speed-recognition-source-scope-pass90.md)
distinguishes the two ideals in their exact rings. With independent
base variables \(x,\eta\), put
\[
\begin{gathered}
S'=\mathbb C[x,\eta,\eta^{-1}],\qquad
\mathscr P'=S'[Y,Z],\qquad F'=xZ-Y^2-\eta,\\
(F'_Y,F'_Z)\mathscr P'=(Y,x)\mathscr P'\ne\mathscr P',\qquad
F'\bmod(x,Y)=-\eta\in S'^*,\\
(F',F'_Y,F'_Z)\mathscr P'=\mathscr P',\qquad
\mathscr P'/(F')\simeq\mathbb C[x,Y,Z,1/(xZ-Y^2)].
\end{gathered}
\tag{5}
\]
It is generically a coordinate because x is invertible in
\(\operatorname{Frac}S'\). Its formal critical locus \(x=Y=0\)
is nonempty, with critical value \(-\eta\ne0\), but its zero
hypersurface has a unit relative gradient. The latter is smooth,
factorial and faithfully flat over \(S'\), and its induced LND
\(x\partial_Y+2Y\partial_Z\) is fixed-point-free, as already
verified in pass90. It is not a relative polynomial line: the
generic x-divisor fiber has the nontrivial constant extension
\(\mathbb C(\eta)(\sqrt{-\eta})\).

This is a quadratic example, so the degree-at-most-three bound does
not remove the full-gradient obstruction. It is not supplied with the
special original nonconical frame or its remaining coefficient
identities. Whether those identities exclude critical points away from
the zero level is a separate mathematical question.

## 5. Reading and stopping scope

The retained pass79 and pass86 relative-source notes and the pass90
source scope were reread for deduplication. The additional source
input here is the full-polynomial-ring gradient criterion, rather
than another invocation of an unproved retraction or geometric-fiber
condition. The proof of the generic-coordinate gate and the formal
LND in Sections 1 and 3 are written out above.

No low-degree classification is applied without its hypotheses.
No new recognition, exhaustive literature conclusion, numerical run,
or modification of pass90 or earlier artifacts is claimed.

[^bd]: S. M. Bhatwadekar and A. K. Dutta,
    [*Kernel of locally nilpotent R-derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf),
    *Transactions of the AMS* 349 (1997), 3303--3319,
    Proposition 4.4, printed p.3314. The section-wide hypotheses,
    generic/residual definitions, and complete displayed proposition
    and proof were freshly read in the original repository PDF's text.
    Its invoked Russell--Sathaye criterion, residual-coordinate theorem
    and other deeper dependencies were not fully re-audited. The
    attempted visual fetch failed; no successful visual verification
    of that page is claimed.

[^babu]: Janaki Raman Babu and Prosenjit Das,
    [*A criterion to determine residual coordinates of A2-fibrations*, v4](https://arxiv.org/pdf/2212.03488v4),
    [version record](https://arxiv.org/abs/2212.03488).
    The record identifies v4, 14 February 2023. Freshly read Theorem 1.1,
    the fixed-base definitions and complete displayed proof of
    Proposition 3.1. The latter supplies a broader criterion, but is
    not applied to the unknown cylinder here. No whole-paper or
    deeper-dependency audit is claimed.
