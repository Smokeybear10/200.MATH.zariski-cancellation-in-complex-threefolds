# Exact controls for the full six-dimensional transfer

The separate [standalone checker](higher_joint_rank_checks_pass73.py)
contains three bounded exact methods accompanying the
[higher joint-rank recognition argument](independent-higher-joint-rank-closure-pass73.md).
It retains both defect columns and both auxiliary rows. Its formal
companion tables are not asserted to arise from an actual polynomial
action. The displayed coordinate maps, in contrast, are genuine
polynomial automorphisms over the indicated constant field.

## 1. Jordan partitions and full image subtraction

The first method enumerates all eleven partitions of six. Among
partitions with largest part four or five, it checks the stated
nilpotence and ranks of the highest powers. The largest-part-four
possibilities are \((4,2)\) and \((4,1,1)\); both give the
two image ranks used in the proof. The additional actual companion
rank bound \(\operatorname{rank}M\ge4\) excludes the latter.
For largest part five, the partition is \((5,1)\), whose square
has rank three. These are exact finite linear-algebra checks,
not realizations of companion matrices by polynomial actions.

The independent formal image calculation uses
\(\ell=(1,0)^t\), \(\mu=(\mu_1,\mu_2)^t\), and
\(\mu_2\ne0\). For both \(m=4,5\), it subtracts the
full six-entry vectors to recover
\[
v=(c,(m-1)\ell)^t,\qquad
w_1=(e,(m-2)\mu-\sigma\ell)^t.
\]
It checks the two-row differential identity for the next bad pair
separately in \(\sigma\) and \(\tau\). For \(m=5\), it
also subtracts the third full vector with upper direction \(v_0\).
The nonzero upper minor \(\mu_2\) verifies the three columns'
independence, and the actual constant dual row for \(w\) kills
their upper projections. Membership in the actual companion image,
and constancy from all four ordinary partials, remain written proofs.

## 2. Cancellation with two separate defect directions

The second method works in a free coefficient module with separate
directions \(c,e,\mathcal D\ell,\mathcal D\mu\).
The two defect directions are linearly independent in this control;
they are never replaced by one common line. For each \(m=4,5\)
it verifies the full velocity identity defining \(Jv_0\), then
checks the vanishing of every coefficient of
\[
-Jv_0-\beta Je-\gamma Jc
 +(\delta\beta)e+(\delta\gamma)c.
\]
Here \(\delta\) on the coefficient formulas differentiates
\(\sigma\) and fixes \(u_0\). It also checks the distinct
quartic and quintic derivative values producing
\(Su_0=1/3\) and \(Su_0=0\), respectively, and their stated
second coordinate iterates. These are formal coefficient identities.
They do not establish local nilpotence on a localization or the
original-slice unit argument, which the written proof supplies.

## 3. Actual coordinate maps and polynomial numerators

The third method first forms the genuine constant dual coordinates
for the basis \((c,e,v_0,c_2)\). Both inverse orders, the formulas
\(z=Y/\mu_2\), \(b=X-\mu_1Y/\mu_2\), and retention of
the original good directions are checked.

It then verifies both inverse orders, both inverse Jacobian orders,
and determinant one for the actual shears
\[
a=a_0-z^2/12+(\nu_2/3)b\quad(m=4),\qquad
a=a_0-(\nu_2/2)b\quad(m=5).
\]
Their transported bad partials have the respective coefficients
\(-\nu_2/3\) and \(+\nu_2/2\) on the retained good partial.
The raw rational symmetry coefficients are stipulated formal inputs,
not an action reconstructed from these automorphisms.

For the quartic, substituting the actual-layer formulas verifies
\[
N=g\widehat\beta=(Ez-2\nu_2g)/2,\qquad
U=3g\kappa=Eb-g(z/2+2\nu_1+\nu_2^2/2),
\]
together with the normalized coefficient rates and the original
\(EN,EU\) chain. For the quintic, the analogous substitutions
verify the displayed polynomial numerators \(n=g^2\beta\),
\(Q=g^4\kappa\), and their original derivative chain.
Polynomiality in an actual application follows from those actual
velocity inputs in the written proof, not from a finite test.

## Verification and review scope

The first completed three-method version passed in **0.094 seconds**,
exit zero. Only `unittest` and SymPy are imported. No research module,
solver, prior checker, or classification implementation is imported.
The complete saved checker and this note received author EOF
self-review. Independent reviews and reruns are separate events and
must not be inferred from that author review.

The author also completed a separate independent EOF reconstruction
of all 26 equations of the transfer proof, including its exact
predecessor hypotheses. That written-proof audit is not established
by this suite and is not a fresh audit of every historical source
paper. No full-frame example, unrestricted cancellation theorem,
universal frame, proof-assistant certificate, new full regression,
checkpoint, or shared metadata change is asserted here.
Frozen pass72 and earlier artifacts are unchanged.
