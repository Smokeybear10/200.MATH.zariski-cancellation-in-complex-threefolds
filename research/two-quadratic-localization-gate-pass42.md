# A denominator gate for the constant-top commuting corrector

The normalized commuting corrector suggested by the common-power top
has a computable action on the inverted polynomial. Unless that action
vanishes, neither local nilpotence on the localization nor a global
locally nilpotent power-clearing replica is possible. This is an exact
additional gate, not a proof that the gate fails for an actual residual.

## 1. Retained actual-frame hypotheses

Use the nonzero-\(\ell\) alternative of
[the top-line reduction](two-quadratic-top-line-pass42.md). Thus
\(B=\mathbb C[x_1,x_2,x_3,x_4]\), the original LND \(E\) has
a polynomial slice \(s_*\), and its two quadratic defects are
independent. For \(3\le m\le5\), the actual highest data are
\[
E^mx=cg^m,\qquad L_0E^{m-1}x=\lambda g^{m-1},
\quad Eg=0,\quad g\notin\mathbb C,
\tag{1}
\]
where \(c\ne0\) is a constant vector supported in the two good
directions and \(0\ne\lambda\in\mathbb C^2\). Let
\[
T_c=\sum c_i\partial_{x_i},\qquad
T_\lambda=\lambda_1\partial_{x_3}+\lambda_2\partial_{x_4},
\qquad \delta=E/g\text{ on }B_g.
\]
The original and normalized bad combinations are
\[
W_\lambda=[E,T_\lambda],\quad
V_\lambda=[E,W_\lambda],\quad
\widetilde V_\lambda=[\delta,[\delta,T_\lambda]].
\]
The exact rank dichotomy does not remove the localization in this setup.

## 2. The corrector moves the inverted polynomial by half a constant derivative

Write \(J_E=\operatorname{Jac}(Ex)\) and
\(J_\delta=\operatorname{Jac}(\delta x)\). The original and
normalized top coefficient identities give
\[
gJ_Ec=\frac{m-1}{2}V_\lambda(x),\qquad
J_\delta c=\frac{m-1}{2}\widetilde V_\lambda(x).
\tag{2}
\]
These particular identities do not require the normalized defect pair
to remain independent. Put \(k=T_cg\). The exact derivative and
rescaling formulas are
\[
J_\delta c=g^{-1}J_Ec-g^{-2}kE(x),
\quad
\widetilde V_\lambda
=g^{-2}V_\lambda+2g^{-3}(W_\lambda g)E.
\tag{3}
\]
Substitute (3) into (2), cancel the common first term, and use
\(E\ne0\). This yields
\[
W_\lambda g=-\frac{gk}{m-1}.
\tag{4}
\]

Consider the derivation of \(B_g\)
\[
Z=T_c+\frac{m-1}{2}[\delta,T_\lambda].
\tag{5}
\]
Equation (2) gives \([\delta,Z]=0\). However
\([\delta,T_\lambda]g=g^{-1}W_\lambda g\), so (4) gives the
stronger bookkeeping identities
\[
Zg=\frac k2,\qquad
[E,Z]=-\frac{k}{2g}E.
\tag{6}
\]
In particular, centralizing \(\delta\) does not automatically
centralize the original \(E\).

The good-column top identity gives \([E,T_c]g=0\), so \(Ek=0\).
Thus the obstruction \(k\) is a polynomial invariant of the original
action, not a formal coefficient with an unproved invariance property.

## 3. Necessary global and localized conditions

Each of the following implies \(k=0\).

1. \(Z\) is locally nilpotent on \(B_g\). An LND kills every
   unit, whereas \(g\) is a unit there and \(Zg=k/2\).
2. For some integer \(N\ge1\), \(g^NZ\) is a polynomial LND
   of \(B\). Its value on \(g\) is \(g^Nk/2\), divisible by
   \(g\). In a characteristic-zero domain, local nilpotence and
   \(g\mid Dg\) imply \(Dg=0\).
3. \(Z\) itself is a polynomial derivation of \(B\), without
   assuming local nilpotence. Apply the second equality of (6) to
   the original slice: \(E(Zs_*)=-k/(2g)\in B\). Hence
   \(g\mid k=T_cg\). Since the actual constant partial \(T_c\)
   is an LND, the same divisibility criterion gives \(k=0\).

For the divisibility criterion, use the degree of a nonzero polynomial
under an LND: if \(Dg=ag\ne0\), then
\(\deg_D(Dg)=\deg_Dg-1\), whereas
\(\deg_D(ag)=\deg_Da+\deg_Dg\), a contradiction.

An explicit polynomial clearing is always available:
\[
g^2Z=g^2T_c+\frac{m-1}{2}
 \bigl(gW_\lambda+(T_\lambda g)E\bigr).
\tag{7}
\]
It is not thereby an LND. If \(k=0\), it kills \(g\) and
commutes with \(E\); local nilpotence or niceness remains a separate
obligation. If a local LND proof for \(Z\) is eventually obtained,
then \(Zg=0\) makes this replica locally nilpotent on \(B_g\),
and its polynomial restriction descends to an LND of \(B\).
No local quotient coordinates are inferred to extend across \(g=0\).

## 4. A small recognition branch and the remaining gap

If \(k=T_cg\) is a nonzero complex constant, \(g\) is itself an
ambient coordinate. Indeed, choose linear coordinates with
\(T_c=\partial_b\); then \(g=kb+q\), with \(q\) independent
of \(b\), and this has a polynomial triangular inverse. Since
\(Eg=0\), the original-slice regular-kernel criterion recognizes
\(\ker E\simeq\mathbb C^{[3]}\).
The recognition input is
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/pdf/1501.01438v1),
whose invariant-coordinate and original-kernel regularity hypotheses
are both established here.

An instance left after this observation has \(k=0\) or \(k\)
nonconstant. In the latter case (6) definitively
rejects this particular local-LND corrector and all its locally
nilpotent power-clearing replicas. In the former case those rejection
arguments vanish, but do not prove the needed integrability.

This note does not construct a high-degree example with \(k\ne0\),
prove \(k=0\) from the full frame, make an arbitrary invariant
polynomial an ambient coordinate, or solve the remaining original
cylinder problem. All deductions use the unchanged original slice;
no slice or coordinate theorem is transferred from \(B_g\) to \(B\).
