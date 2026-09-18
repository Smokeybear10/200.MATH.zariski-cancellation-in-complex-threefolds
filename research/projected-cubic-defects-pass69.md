# Normalized cubic defects are genuine locally nilpotent derivations

In the moving cubic reduction, the normalized defects are locally
nilpotent on the invariant localization. A slice projection proves
this without claiming that the localized coordinate partials are
locally nilpotent. One additional power of the invariant factor
clears the projected fields to polynomial commuting LNDs of the
original ring. Their rank can still drop, so this is a reduction,
not a recognition theorem by itself.

## 1. A slice projection lemma

Let \(R\) be a domain over a field of characteristic zero. Suppose
\(\delta,V\in\operatorname{LND}(R)\), \([\delta,V]=0\), and
\(\sigma\in R\) satisfies \(\delta\sigma=1\). Put
\[
C=\ker\delta,\qquad b=V\sigma,\qquad N=V-b\delta.
\tag{1}
\]
Commutation gives \(b\in C\) and makes \(C\) stable under \(V\).
The slice identity gives \(R=C[\sigma]\). For completeness,
one obtains generation by subtracting
\((\delta^nf)\sigma^n/n!\) from any element of \(\delta\)-degree
\(n\) and inducting; algebraic independence follows by applying
successive powers of \(\delta\).[^slice]

On this actual polynomial extension, \(N\) is exactly the LND
\(V|_C\), extended by setting \(N\sigma=0\). Therefore
\[
N\in\operatorname{LND}(R),\qquad
[\delta,N]=0,\qquad N\sigma=0.
\tag{2}
\]
If \(V_1,V_2\) commute as well, their two projections commute.
Indeed \(V_1(V_2\sigma)=V_2(V_1\sigma)\); expansion of the
bracket in (1), using \(\delta b_i=0\), gives
\([N_1,N_2]=0\). A projection may be zero, for example when
\(V=b\delta\). No generic independence is part of this lemma.

## 2. Application to the actual moving cubic frame

Let
\[
B=\mathbb C[Q_1,Q_2,X,Y],\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1,
\]
with genuine good coordinate partials of second adjoint zero and
bad coordinate partials of third adjoint zero. Put
\(W_j=[E,T_j]\), \(V_j=[E,W_j]\), \(j=X,Y\), and assume
the independent-defect moving cubic power-law alternative
\[
E^3x=e_1g^3,\qquad E^2(X,Y)=(g^2,0),\qquad
g\in\ker E\setminus\mathbb C.
\tag{3}
\]
These are the actual hypotheses and constant normalizations of
[the highest-vector reduction](two-quadratic-top-line-pass42.md).
The original top fields \(V_X,V_Y\) are polynomial LNDs,
commute with each other and \(E\), and kill \(g\).

On \(B_g\), let
\[
\delta=E/g,\qquad \sigma=\delta X=EX/g,\qquad
\delta\sigma=1.
\tag{4}
\]
The fields \(V_j\) extend as LNDs because they kill \(g\),
and they commute with \(\delta\). The exact rescaling and
inverse-Jacobian coefficient identities are
\[
\widetilde V_j=\operatorname{ad}_\delta^2T_j
=g^{-2}V_j+2g^{-3}(W_jg)E,\qquad
\widetilde V_j\sigma=0.
\tag{5}
\]
The first is the direct rescaling identity of pass42. The second
follows from the highest coefficients of the divided inverse-flow
Jacobian, as reconstructed in Section 2 of
[the moving cubic local-slice note](moving-cubic-coordinate-local-slice-pass68.md).
That coefficient calculation does not require joint rank three;
the later rational-curve and graph arguments there do.

Evaluation of (5) on \(\sigma\), using \(E\sigma=g\), yields
\[
V_j\sigma=-2W_jg,\qquad
N_j:=V_j-(V_j\sigma)\delta=g^2\widetilde V_j.
\tag{6}
\]
The slice projection lemma shows that \(N_j\) is an actual LND
on \(B_g\). It kills \(g\), since both \(V_j\) and \(\delta\)
do. Consequently its invariant replica \(g^{-2}N_j\) is an LND
there too. Thus the normalized defects themselves, not just formal
coefficient matrices, are locally nilpotent on this localization.

## 3. Polynomial descent with the correct denominator power

Define
\[
\mathcal R_j=gN_j=g^3\widetilde V_j
=gV_j+2(W_jg)E.
\tag{7}
\]
The right side is polynomial on the original \(B\). The left
side is an LND on \(B_g\), because \(N_jg=0\). Restricting it
to the preserved original subring proves
\[
\mathcal R_j\in\operatorname{LND}(B),\qquad
[E,\mathcal R_j]=[\mathcal R_X,\mathcal R_Y]=0,
\qquad \mathcal R_jg=\mathcal R_j(EX)=0.
\tag{8}
\]
The bracket with \(E\) also follows directly from (7), since
\(E(W_jg)=V_jg=0\). The other bracket follows from commuting
projections and their common invariant factor \(g\).
Finally \(EX=g\sigma\), which proves the last equality.

The one-power clearing from \(N_j\) to \(\mathcal R_j\) uses
the full coefficient identity \(V_j\sigma=-2W_jg\), whose right
side is polynomial. For a general commuting LND and an arbitrary
localized slice, the factor \(g\) alone need not clear the poles
of \(V\sigma\). The abstract projection lemma does not claim it.

## 4. Exact rank and intrinsic-action limits

All ranks here are dimensions over \(\operatorname{Frac}B\), not
coordinate ranks of individual LNDs. Multiplication by nonzero
powers of \(g\) leaves rank unchanged. The exact rank formula
of the original full highest-vector reduction gives
\[
\operatorname{rank}(\mathcal R_X,\mathcal R_Y)
=\operatorname{rank}(\widetilde V_X,\widetilde V_Y)
=\operatorname{rank}(E,V_X,V_Y)-1.
\tag{9}
\]
Thus original joint rank two gives exactly one surviving projected
direction, not two. Original joint rank three gives two. Each
nonzero projected direction is independent of \(E\), because it
kills \(\sigma\), whereas \(E\sigma=g\ne0\).

For the original kernel \(A=\ker E\), equation (7) gives
\(\mathcal R_j|_A=gV_j|_A\). These are replicas of already
available intrinsic actions; they do not supply new intrinsic
directions. Their value in the reduction is that they fix the
particular normalized slice while retaining actual local nilpotence
and an explicit polynomial descent.

No original invariant denominator, normalized slice or quotient
parameter has been made an ambient coordinate by this argument.
The original slice remains unchanged. The rational rank-drop
recognition problem is a separate step, not a consequence of
polynomial descent or of a finite example.

## Sources and verification scope

The complete pass42 highest-vector and rescaling calculation and
the selected complete pass68 coefficient argument were reread for
this deduction. The commuting slice-projection proof is given
directly above; it is also the central-commutator-zero instance of
the [Heisenberg projection](quadratic-heisenberg-repair-pass43.md),
Section 4, whose complete proof was reread. Independent reviews
and bounded symbolic controls are recorded separately. No human
review, formal proof-assistant verification, historical novelty
verdict or general cancellation solution is asserted.

[^slice]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), arXiv:2306.00510v2, December 9, 2023, Theorem 2.5. Its actual domain-and-slice statement was directly checked. The needed generation and algebraic-independence argument is reproduced in Section 1 rather than inferred from an abstract quotient identification.
