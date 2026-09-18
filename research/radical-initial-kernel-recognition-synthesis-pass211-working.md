# Recognition for a supplied radical initial-kernel frame

Status: working restricted recognition theorem. The last affine
projected-pair case now has an original-ring proof. Combined with the
retained branch reductions, it recognizes every globally sliced action
with the exact radical frame stated below.

This does not prove that an arbitrary cancellation instance admits
such a frame. It does not solve the full cancellation conjecture.

## 1. The theorem and every frame assumption

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad \deg_E(X,Y,Z,W)=(1,1,2,2).
\tag{1}
\]
The four capital letters are actual polynomial coordinates of \(B\).
Put \(a=EX,\ b=EY,\ e=E^2Z/2,\ h=E^2W/2\).
Assume the entire leading evaluation kernel is
\[
\ker\!\left(
\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow A[s]
\right)=(\mathsf X^2\mathsf Z-\mathsf W^2),
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(as,bs,es^2,hs^2).
\tag{2}
\]
Here \(s\) is an independent indeterminate.
A single identity \(a^2e=h^2\) is not a substitute for (2).
There is no assumption that \(a\) is constant or invertible.

**Working theorem.** Under (1)--(2),
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{3}
\]
In particular the original action fixes an ambient polynomial
coordinate. The conclusion is an original-ring isomorphism, not an
isomorphism only after extending a coefficient field or inverting a
polynomial.

## 2. The retained reduction is exhaustive

Use the literal selected partial \(\partial_Z\).
The actual construction in universal184 and eliminant206 gives
\[
\begin{gathered}
N=[u^3](\partial_Z|_A),\quad L=\operatorname{Frac}\ker_A N,\quad
A_L=L[v],\quad Nv=1,\quad [L:\mathbb C(t,\rho)]<\infty,\\
t=b/a,\quad \rho=h/a^2,\quad
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+(2\rho\vartheta+k)X+\rho^2X^2 .
\end{gathered}
\tag{4}
\]
The chart is derived from the actual ring. In particular its calibrated
determinant and field return are not formal assumptions chosen to
make a polynomial parametrization work.

The [complete frontier synthesis210](radical-affine-pair-frontier-synthesis-pass210-working.md)
proves that (1)--(2) imply either (3) already, or
\[
R=2\vartheta+k_\rho\ne0,\quad
L[y,\vartheta]=L[v],\quad
\deg_vy=\deg_v\vartheta=1,\quad
\deg_vw\le1,\quad \deg_vz=2 .
\tag{5}
\]
Its coverage includes the identically zero return coefficient, proper
projected planes, constant second projection and every center
polynomial of degree at most two. Thus (5) is the entire remaining
case within the supplied frame, not a selected favorable branch.

## 3. Recognition of the remaining affine pair

The [affine-pair recognition211](radical-affine-pair-coordinate-recognition-pass211-working.md)
applies exactly to (4)--(5). Write
\(y=\mu\vartheta+\nu\) and \(w=\lambda\vartheta+\omega\) over \(L\).
Its auxiliary derivation is the actual
\(P=aN-(NX)E\), and primitive division preserves commutation with \(E\).
The square identity for its second \(Z\)-derivative returns the
needed coefficient to the original polynomial ring.

For \(\mu\in\mathbb C^*\), an actual elementary shear makes the
primitive auxiliary derivation nice. A PID-linear invariant and
weighted leading-degree comparison force an actual coefficient to
be a nonzero complex constant. An explicit auxiliary slice and
polynomial three-variable kernel result. The known three-variable
triangularization theorem then supplies an invariant coordinate of
the original four-ring; the regular-kernel theorem concludes (3).
Weighted leading comparison does not assume that the speed \(a\)
is algebraically independent from other coefficient-field elements.

For \(\mu\notin\mathbb C\), the exact generic classification yields
a linear relation between the slopes. That linear exception is
retained rather than discarded. Actual elementary normalizations
put its candidate invariant into a polynomial expression with
transcendental specialization at every \(X=c\).
Polynomial-in-that-invariant denominators contract to the original
subring. Reduction at \(X=0\) gives an odd/even polynomial identity,
forcing \(X\) to divide a nonzero E-invariant coefficient.
Factorial closure contradicts \(EX\ne0\).
The independently written
[fiber-obstruction lemma211](radical-wang-second-case-fiber-obstruction-pass211-working.md)
isolates this final argument and its exact actualness prerequisites.

These two slope cases exhaust (5), proving (3).
The [actual node and cusp examples207](radical-nodal-cuspidal-actual-frame-pass207-working.md)
remain compatible with the theorem, so this is recognition rather
than a claim that the supplied radical frame never occurs.

## 4. Verification and the unresolved global problem

The exact imported inputs are Wang's alternatives and Daigle's
three-variable result as stated in
[Dasgupta--Gupta](https://arxiv.org/pdf/1701.03635v1), together with
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1).
Their hypotheses are checked in the affine-pair proof.
An unconditional PID recognition claim is not inferred from the
generic classification.

The retained210 reductions have a frozen written-review and finite
algebra packet. The new211 recognition, fiber lemma and this synthesis
are separate working sources. Complete saved-source reviews and any
new finite checker must be recorded separately; no finite computation
proves the imported theorems or the universal descent arguments.

The unrestricted target still requires recognition outside this
initial kernel and an entry argument from arbitrary globally sliced
actions. Neither is proved here. There is no human expert review,
proof-assistant verification, novelty clearance, public posting,
submission or external contact. The full goal remains active and
unsolved.
