# Double-cover weight-four frontier after the pass195 proofs

Status: bounded working synthesis. For the supplied full initial kernel
\(Z^2-X^3Y\), the zero-\(R\) branch is recognized in the original
polynomial ring. In the nonzero-\(R\) branch, two differential gates have
a complete surviving coefficient list, not a complete actual-frame
classification. For the second double-cover form below, only the
nonzero-\(R\) reduction to square alternatives is supplied here.
Neither full double-cover configuration is settled.

## 1. Exact hypotheses and distinct leading ratios

Retain an actual globally sliced frame
\[
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\mathcal A=\ker E,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2).
\tag{1}
\]
The full weighted initial kernel, not merely a relation among leaders,
is one of
\[
\begin{aligned}
(F_1)&=(\mathsf Z^2-\mathsf X^3\mathsf Y),
& q^2&=t,\\
(F_2)&=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
& q^2&=t(1-t).
\end{aligned}
\tag{2}
\]
Both are positive-rank cases for the quadratic part in the bad slots
\(\mathsf Z,\mathsf W\). They are not in the zero-bad-quadratic-part
stratum recognized by the frozen194 synthesis.

The [universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
uses the occurring \(Z\) pivot and gives commuting coefficient partials,
the independent ratios \(t,\rho\), and exact fields
\(L/\mathbb C(t,\rho)\) and
\(K=\ker_L\partial_\rho\), with \(K/\mathbb C(t)\) finite and derivative
constants \(\mathbb C\). Here
\(q=(E^2Z/2)/(EX)^2\in K\), and \(R=k_\rho\).
The projected entries satisfy the whole-line and field-return equalities
\(L[y,z,w]=L[v]\) and \(\mathbb C(y,z,w)=L(v)\).
The original determinant is nonzero and independent of \(X\).

Neither \(K=\mathbb C(t)\), an original-ring unit speed, nor an original
coordinate equal to \(q\) is assumed. The square-root notation refers to
the given algebraic coefficient element. Its sign is not an analytic
branch choice.

## 2. The zero-R branch of the first form is recognized

For \(F_1\) and \(R=0\), the
[zero-R proof195](weight-four-double-root-zero-r-coordinate-recognition-pass195-working.md)
first excludes constant projected \(y\) through an actual commuting
derivation and Wang's two-coordinate theorem. The remaining whole-line
identity makes \(y\) affine in the generic parameter, retaining \(Ny\).

The general coefficient cover has
\(\rho=a n^2+b n+c\), with \(a,b,c\in K\), and the literal scalar
recurrence puts every projected entry in \(K[n,y]\).
Actual field return proves \(L=K(n)\), rather than assuming it.
If \(a\ne0\), the coefficient of \(z^3\) in \(w\) has a pole of order
at least three on the coefficient curve; the exact field equality
requires degree one. Thus \(a=0\).
The full algebraic solution of the remaining slope equation is
\(b=Aq+B t^{7/4}\). Its \(B\ne0\) term makes the coefficient of \(z^2\)
have pole order at least five, giving the same contradiction.
Consequently \(b=\lambda q\), with \(\lambda\in\mathbb C^*\).

The residual polynomial subtraction is
\(w-\lambda z^2/2=(\alpha y+D)z+G(y)+g_0\).
The exact linear-pencil argument and
\(g_2'=-q''D'/2\) force \(D\in\mathbb C\), then
\(G\in\mathbb C[y]\) and \(K=\mathbb C(g_0)\).
These are coefficient-field conclusions until the following original
polynomial construction is made:
\[
\begin{aligned}
I&=W-\frac{\lambda}{2}Z^2
       -(\alpha Y+\beta X+D)Z-Q_0(X,Y)=g_0,\\
W&=I+\frac{\lambda}{2}Z^2
       +(\alpha Y+\beta X+D)Z+Q_0(X,Y),
\qquad Q_0\in\mathbb C[X,Y].
\end{aligned}
\tag{3}
\]
All displayed scalars are complex. Both maps fix \(X,Y,Z\).
The proof computes the original coefficient of \(n\) after the square
subtraction and uses the exact transverse derivation to transport
the correction into \(\mathbb C[X,Y]\).
Thus both compositions in (3) are polynomial inverses in \(B\), with
no division by \(q\), a coordinate, or the speed.

The polynomial \(I\) is \(E\)-invariant. The global slice gives a regular
kernel, so the exact published
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
yields \(\mathcal A=\mathbb C[I]^{[2]}\).
This conclusion concerns \(F_1,R=0\), not every case in (2).

## 3. An algebraic leading ratio rules out the pure-quartic branch

The [nonzero-R reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
proves a more general statement before specializing to (2).
In a pure-quartic actual branch with \(q\in K\), the coefficient gates
give \(R=1/\chi\), \(\chi=\alpha t+\beta\) with complex constants,
and \(n_\rho=cR^2\). Set \(d=q'''/6\).
The literal scalar determinant then supplies
\[
D=\frac{\chi d'}4+\alpha d\ne0,\qquad
T=At+B\ne0,\qquad
(DT^5)'=0,\qquad D\in\mathbb C(t)^*.
\tag{4}
\]
The affine-parameter factor and the coefficient-variable change are
retained when deriving (4); no field equality \(L=K(h)\) is needed.

Subtract the normalized trace of \(q\) over \(\mathbb C(t)\).
Derivation commutes with trace, so the difference \(\widetilde q\)
satisfies
\(\chi\widetilde q''''+4\alpha\widetilde q'''=0\).
Its explicit primitives belong to \(\mathbb C(t)\): a cubic polynomial
when \(\alpha=0\), or a multiple of \(1/\chi\) plus a quadratic polynomial
when \(\alpha\ne0\). Therefore the pure-quartic branch forces
\(q\in\mathbb C(t)\).

In each case (2), the defining rational square has an odd-order zero
at \(t=0\), so \(q\notin\mathbb C(t)\).
The same nonrationality forbids every nonzero polynomial multiplier
of \(q\) from becoming rational. This supplies the exact obstruction
in the actual constant-projection argument.
The general-\(q\) coefficient rigidity, the nonzero curvature at a
hypothetically vanishing quartic top, and the whole-plane/cofactor
argument then leave only the two square-completion alternatives.
The pure-quartic alternative is excluded for both forms (2).

## 4. Complete two-gate classification for q-squared equals t

For \(F_1,R\ne0\), put \(f=1/R\), \(d=1/(16q^5)\), and
\(D_f=d'f/4+df'\). In either surviving square alternative,
the necessary coefficient equations and scalar-Jacobian condition are
the first differential equation and \(J_3=0\) of
[classification195](weight-four-square-root-two-gate-classification-pass195-working.md),
with nonzero gates \(f f''D_f\ne0\).

That note rewrites the first equation in logarithmic derivative
coordinates and factors the second one modulo the first.
No rationality of \(K\) or power-law ansatz is used.
The two resulting Euler equations are integrated using the exact
constant field, and substitution back into the first equation removes
the inadmissible mixed family. The complete result is
\[
f=a t+bq\quad(a\in\mathbb C,\ b\in\mathbb C^*),
\qquad\text{or}\qquad
f=b/q\quad(b\in\mathbb C^*).
\tag{5}
\]
Every element of this list satisfies both differential gates and all
their stated nonzero conditions.
It follows that the vanishing-gate exclusion194 for
\(d=t^{-4}-1\) cannot be transferred to \(d=1/(16q^5)\).

The classification makes the displayed coefficients \(R,\nu,p_2,p\)
rational in \(q\); it does not prove \(K=\mathbb C(q)\).
It is a classification of necessary differential equations, not of
actual polynomial frames or all their lower potentials.

## 5. What remains in the actual configurations

For either form (2), every remaining nonzero-\(R\) branch has a completed
square eliminant
\[
\mathcal H=A_2(V-P_2(U))^2+B_1U+B_0,\qquad
A_2\ne0,\quad \deg P_2=2.
\tag{6}
\]
The quadratic-graph case has \(B_1=0\); the quadratic-projection case
has \(B_1\ne0\). The distinction is not removed by completing the square.

| Supplied full kernel and branch | Result recorded here |
| --- | --- |
| \(F_1,\ R=0\) | Original invariant coordinate and polynomial kernel. |
| \(F_1,\ R\ne0\) | Only the two actual square alternatives can remain; their reciprocal coefficient must satisfy (5). Realization, exclusion or recognition is unresolved. |
| \(F_2,\ R\ne0\) | Only the two square alternatives can remain. The classification (5) does not apply to its different \(d\). |
| \(F_2,\ R=0\) | Not treated by the zero-R proof in this packet. |

For the classified \(F_1\) families, a next bounded task is to enforce
the lower potentials, all scalar-Jacobian coefficients, actual whole-line
and field-return constraints, and original-ring descent.
A formal potential system is not automatically an actual globally
sliced frame. Conversely, the surviving necessary equations alone
do not exclude such a frame.

The full positive bad quadratic rank stratum is not recognized here.
Height-two kernels, higher minimum profiles, arbitrary coordinate entry,
and unrestricted corrected cancellation also remain open.
There is no minimum-profile or entry theorem.

This synthesis composes written proofs with exact stated hypotheses.
The separately recorded finite controls verify only their algebraic
identities; they do not prove field return, pole-degree arguments,
Euler completeness or the published endpoint.
No checker was executed, imported or compiled for this synthesis.
The frozen194 packet and all earlier sources remain unchanged.
This is not human expert review, formal certification, historical
novelty clearance, external contact, public submission, or completion
of the general goal.
