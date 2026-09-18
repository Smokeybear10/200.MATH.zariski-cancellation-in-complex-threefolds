# An exact generic rank test, and why it does not settle divisor descent

For a polynomially embedded generic line, the two translated good
coordinates have a unit Jacobian-minor ideal exactly when one
eliminated polynomial is a nonzero coefficient-field constant.
This is a useful exact test for nonlinear constructions.

It is not a new missing condition on the retained actual frames:
their negative-tail identities139 already imply it. Nor does passing
the test give a polynomial inverse or control a removed coefficient
divisor. The nonlinear exceptional family149 makes that distinction
explicit.

## 1. Statement over the generic coefficient field

Let \(K\) be a characteristic-zero field with commuting coefficient
derivations \(\partial_r,\partial_q\). In applications it is
\(\mathbb C(r,q)\), or a finite separable extension with the uniquely
extended partials. Adjoin independent variables \(t,X\), and extend
the coefficient derivations to fix both. Let
\[
\begin{gathered}
U,V\in K[t],\qquad K[U,V]=K[t],\qquad
f,g\in K,\qquad J=f_r g_q-f_qg_r\ne0,\\
\mathcal M=
\begin{pmatrix}
U_r+Xf_r&U_q+Xf_q&U_t\\
V_r+Xg_r&V_q+Xg_q&V_t
\end{pmatrix}.
\end{gathered}
\tag{1}
\]
These are absolute coefficient derivatives taken before evaluation
at a generic-field point, not differentials relative to \(K\).
Define
\[
\begin{aligned}
A_r&=V_tU_r-U_tV_r,& A_q&=V_tU_q-U_tV_q,\\
B_r&=V_tf_r-U_tg_r,& B_q&=V_tf_q-U_tg_q,\\
\mathcal F&=A_rB_q-A_qB_r\in K[t].
\end{aligned}
\tag{2}
\]
Then the ideal of two-by-two minors of \(\mathcal M\) in
\(K[t,X]\) is the unit ideal if and only if
\[
\mathcal F\in K^* .
\tag{3}
\]
In particular an actual coordinate completion forces (3). The
converse in (3) concerns only the minor ideal, not completion.

## 2. Proof and explicit critical points

Choose \(R(U,V)\in K[U,V]\) evaluating to \(t\).
Differentiation in \(t\) gives
\(R_U(U,V)U_t+R_V(U,V)V_t=1\).
Thus \(U_t,V_t\) have no common zero over an algebraic closure of
\(K\). Since the coefficient matrix defining \(B_r,B_q\) from
\(U_t,V_t\) has determinant \(J\ne0\), neither do \(B_r,B_q\).

The minors involving the last column of (1) are
\(E_r=A_r+XB_r\) and \(E_q=A_q+XB_q\), with the column order
shown. Their identity
\[
B_qE_r-B_rE_q=\mathcal F
\tag{4}
\]
proves the unit-ideal implication when \(\mathcal F\in K^*\).

If \(\mathcal F\) is nonconstant, choose a root \(\theta\) over
\(\overline K\). If it is zero identically, choose any \(\theta\).
At least one of \(B_r(\theta),B_q(\theta)\) is nonzero.
Set \(X=-A_r(\theta)/B_r(\theta)\) when the first is nonzero;
otherwise use \(-A_q(\theta)/B_q(\theta)\).
The relation \(\mathcal F(\theta)=0\) makes both \(E_r,E_q\)
zero. Since the last column of \(\mathcal M\) is not zero there,
the two rows are proportional. All three minors vanish at this
point, so their ideal is proper. This proves (3) and provides the
critical point used to reject a proposed construction.

An evaluation over \(\overline K\) is sufficient. All nonzero
coefficient-field denominators remain invertible. It supplies no
information about a divisor that was removed on passing to \(K\).

## 3. This condition was already present in the actual Taylor identities

In the normalized139 chart take \(r=\tau,q=\rho,t=v\) and
\(f=\tau,g=\rho\). Then \(B_\tau=V_v\), \(B_\rho=-U_v\).
Let \(\Phi,\Psi\) be its first two tail polynomials. The retained
identities give
\[
\begin{gathered}
\Phi(U,V)=0,\qquad
(\Phi_U(U,V),\Phi_V(U,V))K[v]=K[v],\\
\Psi_v(U,V)=1,\qquad
(\Psi_U,\Psi_V)=(\Phi_\tau,\Phi_\rho).
\end{gathered}
\tag{5}
\]
In the middle formula, \(\Psi_v(U,V)\) denotes the derivative of
the evaluated polynomial, including its \(U,V\) dependence.
The coefficient derivatives in the final formula hold the formal
arguments fixed.

Since \((U_v,V_v)\) is unimodular, every polynomial syzygy of that
pair is a multiple of \((-V_v,U_v)\). Differentiating
\(\Phi(U,V)=0\) in \(v\), and then using the unit gradient ideal,
therefore gives
\((\Phi_U,\Phi_V)(U,V)=c(-V_v,U_v)\) for \(c\in K^*\).
Differentiating the same identity in \(\tau,\rho\) yields
\(\Phi_\tau(U,V)=cA_\tau\), \(\Phi_\rho(U,V)=cA_\rho\).
Consequently
\[
1=c(A_\tau U_v+A_\rho V_v),\qquad
\mathcal F=-A_\tau U_v-A_\rho V_v=-1/c\in K^* .
\tag{6}
\]
Thus the eliminated determinant is already a unit in the actual
generic chart by139. Equations (1)--(4) provide a short direct
rank-test formulation useful for construction attempts, not a
newly closed proof gap. The value \(-1/c\) may have a pole or
zero at a coefficient divisor; generic unit status is not a
divisor-unit assertion.

## 4. A precise gate for relative coordinate reductions

An absolute polynomial coordinate need not be a coordinate relative
to a chosen invariant base. For example \(r+t^2\) is an absolute
coordinate of \(\mathbb C[r,t,z]\), with inverse
\(r=(r+t^2)-t^2\). Over \(\mathbb C(r)\), however, its quotient
contains a root of \(t^2=-r\). The element \(-r\) is not a square
in \(\mathbb C(r)\), as its order at \(r=0\) is odd. The quotient
therefore has a nontrivial algebraic constant extension and is not
a polynomial line over \(\mathbb C(r)\).

Edo, van den Essen and Maubach's Proposition 3.1 proves a useful
conditional result: a polynomial with polynomial-plane quotient
that is a coordinate on one fiber of the base variable is a
coordinate over that base ring. Their stated consequence also
applies to an absolute coordinate already known to be a generic
relative coordinate. It does not supply that additional hypothesis
for our projected goods. The primary statement and its proof on
printed pages 6--7 were inspected.[^1]

Accordingly, absolute coordinate status alone does not authorize
relative plane-coordinate reductions. No decomposition theorem
for all polynomial automorphisms over the divisor ring is assumed.
This source gate is not a novelty audit.

## 5. Quotient-preserving nonlinear changes are already covered by148

There is a useful covariance corollary, requiring no relative
automorphism classification. Retain the actual dense-chart and
embedded triangular-base hypotheses of148, but allow the projected
pair specified below in place of its affine-placement assumption:
\[
S=\mathbb C[r,q]\subset C=\mathbb C[r,t,w],\qquad
q=a(r)w-H(r,t),
\tag{7}
\]
with a nonlinear specialization at a root of \(a\), and an invariant
localization meeting that divisor as in148. Suppose
\(\varphi\in\operatorname{Aut}_{\mathbb C[r]}C\) satisfies
\(\varphi(S)=S\), and the actual projected pair is
\((U,V)=(\varphi(t),\varphi(w))\).

The restricted automorphism of \(S=\mathbb C[r][q]\) fixes \(r\),
so \(\varphi(q)=bq+c(r)\), where \(b\in\mathbb C^*\) and
\(c(r)\in\mathbb C[r]\). This follows by multiplying the degrees
in \(q\) of an automorphism and its inverse; both must have degree
one, and the leading coefficient must be a unit of \(\mathbb C[r]\).
Applying \(\varphi\) to (7) therefore gives
\[
q=\frac{a(r)}b\,V-\frac{H(r,U)+c(r)}b,\qquad
C=\mathbb C[r,U,V].
\tag{8}
\]
In these coordinates the actual projected pair is affine, the
triangular coefficient has the same roots, and its specified
residual polynomial has the same nonlinear degree. The original
invariant localization is still a function of \(r,q\) and still
meets the same divisor. All hypotheses of148 hold in this new
presentation, so the actual completion is excluded.

For example, \(\delta=a(r)\partial_t+H_t(r,t)\partial_w\) is
locally nilpotent and kills \(r,q\). For any \(F\in S\),
\(\exp(F\delta)\) is a polynomial automorphism fixing them both.
All of these potentially nonlinear pair placements fall under
the corollary. Local nilpotence follows directly from
\(\delta t=a(r)\), invariance of \(a\), and the finite degree of
\(H\) in \(t\); multiplying by the invariant \(F\) preserves it.

This excludes quotient-preserving changes, not every polynomial
automorphism fixing \(r\). An automorphism can fail to normalize
the embedded \(S\). That simultaneous-placement distinction is
essential, and no general reduction to its normalizer is claimed.
The corollary records covariance of148, not a separate historical
novelty assertion.

## Sources and scope

1. [Negative tail139](dense-negative-tail-relations-pass139-working.md),
   Sections 3--4, supplies the exact statements in (5).
2. [Actual chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3 and 7, supplies generic polynomial generation
   and the actual Jacobian completion.
3. [Conditional exclusion148](triangular-residue-frame-exclusion-pass148-working.md)
   states the special affine-placement theorem this test helps extend.

The algebraic test is a necessary-condition tool, not a proof of a
Jacobian converse, polynomial inverse, divisor triviality or full
cancellation. Independent human review and historical priority
assessment remain outstanding.

[^1]: Eric Edo, Arno van den Essen and Stefan Maubach,
    [*A note on k[z]-automorphisms in two variables*](https://arxiv.org/pdf/0809.0767),
    Proposition 3.1 and the introduction's generic-coordinate consequence.
