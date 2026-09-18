# The remaining supplied radical chart has an affine projected pair

Status: working restricted frontier synthesis, not recognition of the
remaining branch. The exact supplied radical chart is either recognized
by the retained and new branch theorems, or has two nonconstant affine
projected generators. This removes the nonlinear whole-plane branches.
The affine pair is still a generic statement, not an ambient coordinate.

## 1. Actual setup and precise conclusion

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad a=EX\ne0,\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2).
\end{gathered}
\tag{1}
\]
The displayed ideal is the full initial kernel. Use the literal
selected partial \(\partial_Z\) and the actual universal chart184:
\[
\begin{gathered}
N=[u^3](\partial_Z|_A),\quad L=\operatorname{Frac}\ker_A N,\quad
A_L=L[v],\quad Nv=1,\quad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
C=L[y,\vartheta]\subseteq O=L[v],\qquad R=2\vartheta+k_\rho .
\end{gathered}
\tag{2}
\]
All coefficient derivatives below act on the exact field \(L\);
no rationality or polynomial regularity of its elements is assumed.

The combined conclusion is the following alternative:
\[
\boxed{A\simeq\mathbb C^{[3]}
\quad\text{or}\quad
R\ne0,\ C=O,\ \deg_vy=\deg_v\vartheta=1,\quad
\deg_vw\le1,\ \deg_vz=2.}
\tag{3}
\]
The second alternative is a necessary remaining form, not a
counterexample or an assertion that \(A\) is not polynomial.
The two alternatives need not be disjoint.

## 2. Exhaustive branch coverage

If \(R=0\), the actual
[zero-return recognition205](weight-four-t-independent-zero-r-recognition-pass205-working.md)
applies with \(q=\rho^2\). Hence \(A\simeq\mathbb C^{[3]}\).
Suppose \(R\ne0\).
If \(C\subsetneq O\), the complete
[proper-plane synthesis209](radical-proper-plane-unit-speed-synthesis-pass209-working.md)
gives actual unit speed and the polynomial kernel.
It remains to consider \(C=O\).

If \(\vartheta\in L\), the
[constant-second-projection theorem210](weight-four-constant-second-projection-recognition-pass210-working.md)
proves recognition. Its hypotheses \(q_t=0\), \(q_{\rho\rho}\ne0\)
hold here because \(q=\rho^2\).
Thus restrict to \(\vartheta\notin L\).

Use the exact center of eliminant206:
\[
\begin{gathered}
V_c=-k_\rho/2,\quad
p(U)=S(U,V_c)-\ell,\qquad
S=\tfrac12k_{tt}U^2+k_{t\rho}UV+\tfrac12k_{\rho\rho}V^2+n_tU+n_\rho V,\\
\deg p\le2,\qquad
S-\ell=p(U)-(2V+k_\rho)D(U,V),\quad \deg D\le1,\\
R\{w-D(y,\vartheta)\}+p(y)=0 .
\end{gathered}
\tag{4}
\]
There are four exhaustive possibilities over the characteristic-zero
field \(L\).

- If \(p=0\), the
  [zero-center argument210](radical-zero-and-repeated-center-reduction-pass210-working.md)
  makes the calibrated determinant divisible by \(R\). Since the
  determinant is an \(L\)-unit, \(R\) is a line-ring unit and
  \(\vartheta\in L\), already recognized.
- If \(p\in L^*\), (4) makes \(R\) a unit of \(L[v]\), again
  forcing \(\vartheta\in L\). This elementary gate is in206.
- If \(p\) is a nonzero repeated quadratic, the
  [repeated-center exclusion210](radical-zero-and-repeated-center-reduction-pass210-working.md)
  proves it impossible. Its final contradiction is an irreducible
  original polynomial forced to be a square in \(\operatorname{Frac}B\).
- Otherwise \(p\) is nonconstant and squarefree, of degree one or two.
  The [squarefree reduction210](radical-squarefree-whole-plane-reduction-pass210-working.md)
  gives \(\deg_v\vartheta=1\) and \(\deg_vy\le2\).
  The [affine-second conic exclusion210](radical-affine-second-quadratic-first-exclusion-pass210-working.md)
  rules out \(\deg_vy=2\).

In the last case, \(y\) cannot be constant. The squarefree reduction
proves that at every root \(r\) of \(R\),
\(B_1(r)\), \(C_1(r)\), and \(\vartheta_v(r)\) are nonzero.
The differentiated third potential then gives
\[
B_1(r)y_v(r)=-C_1(r)\vartheta_v(r)\ne0 .
\tag{5}
\]
Since \(R\) is nonconstant, it has a root over an algebraic closure.
This proves \(\deg_vy=1\).

Now \(y,\vartheta\) are affine. The third potential
\(Rw=\ell-S(y,\vartheta)\) has a numerator of degree at most two
and a denominator of degree one. Since \(w\) is a polynomial,
\(\deg_vw\le1\).
The second potential is
\(z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n\).
Only \(\vartheta^2\) contributes a quadratic term, with nonzero
coefficient. Thus \(\deg_vz=2\), completing (3).

## 3. What the affine pair actually supplies

One may use \(h=\vartheta\) as an affine parameter over \(L\), writing
\[
y=\mu h+\nu,\quad w=\lambda h+\omega,\quad
z=h^2+(2\rho\lambda+k_t\mu+k_\rho)h+
       (2\rho\omega+k_t\nu+n),
\qquad \mu\in L^*,\quad \nu,\lambda,\omega\in L .
\tag{6}
\]
This is not an actual polynomial coordinate change over \(\mathbb C\).
The coefficient of \(h^2\) in the third potential gives the useful
necessary relation
\[
4\lambda+k_{tt}\mu^2+2k_{t\rho}\mu+k_{\rho\rho}=0 .
\tag{7}
\]
No coefficient in (6) is assumed complex.

There is also an original-ring derivation carrying the remaining
problem. Extend \(N\) to \(A[u]\) by \(Nu=0\) and put
\(P=aN-(NX)E\).
As proved in the constant-projection source, \(Na=0\),
\(NX\in A\), \(PX=0\), and \(P|_A=aN\).
It is a nonzero polynomial LND: on \(B_a=A_a[X]\) it fixes \(X\)
and restricts to the locally nilpotent \(aN\), and it preserves \(B\).
It commutes with \(E\).

Write \(b=N\vartheta\in L^*\). The actual chart now gives
\[
\begin{gathered}
PY=aNy,\quad PW=a(Nw+Xb),\quad
PZ=a(Nz+2\rho Xb),\\
P^2Y=P^2W=0,\quad P^2Z=2a^2b^2\ne0,\quad P^3Z=0,\\
[E,P]=0,\quad E(PY)=0,\quad
E(PW)=a^2b\ne0,\quad E(PZ)=2a^2\rho b .
\end{gathered}
\tag{8}
\]
Although expressed with field coefficients, these identities have
actual polynomial left sides. The \(P\)-degrees of the original
coordinates are exactly \((0,1,2,1)\).

In particular criterion205 does not yet apply: \(P\) is not nice
on \(Z\), and its \(W\)-coefficient is not \(E\)-invariant.
Squaring a derivation does not produce a derivation, so \(P^2\)
is not a replacement auxiliary LND. A new actual coordinate change,
a different auxiliary action, or another recognition argument is
needed. Generic affine parameters alone do not supply any of these.

## Scope and verification

The four new210 component notes and the retained205/206/209 inputs
give the stated restricted alternative. Their written proofs include
all center cases and both nonlinear squarefree projections.
Finite exact checks of formulas are separate from the geometric,
field and original-ring arguments.

The full cancellation goal remains active and unsolved. The residual
affine pair, other initial kernels, and entry from arbitrary globally
sliced actions remain unresolved. No human expert review, formal
verification, novelty clearance, public claim, submission or external
contact has occurred.
