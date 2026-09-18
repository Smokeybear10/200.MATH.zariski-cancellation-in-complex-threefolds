# Finite Euler graphs: recognition and the higher-flow input boundary

The proof in [pass64](actual-quadratic-graph-cancellation-pass64.md)
works for arbitrary finite graph degree. This records that exact
scope and its input boundary; it is not a new pole argument or
a derivation of such a graph from higher-flow adjoint bounds.

## 1. Exact finite-degree recognition statement

Let \(k=\mathbb C\), \(B=k[Q_1,Q_2,X,Y]\) with these four
elements actual polynomial coordinates, and let \(E\) be an
LND of \(B\) with an actual slice. Suppose:

- \(C=k[a,b]\subseteq\ker E\), \(L=k(a,b)\),
  \(B\cap L=C\), and \(B\otimes_C L=L[X,Y]\).
- \(f=EX,\ g=EY\in C\) are algebraically independent.
- With the extended field partials and
  \(\mathscr H=f\partial_f+g\partial_g\), one has
  \(Q=\ell+S(X,Y)\), where \(\ell\in L^2\),
  \(S\in L[X,Y]^2\) has zero constant term and every coefficient
  of \(S\) is killed by \(\mathscr H\).
- The full determinant \(\det Q_{(f,g)}\) lies in \(L^*\),
  with \(X,Y\) held fixed.

Then \(\ker E\simeq k^{[3]}\). More precisely either
\(B=C[X,Y]\), or an element of \(C\) is an actual ambient coordinate.
There is no bound on the finite polynomial support of \(S\).

Here is the complete reduction to the already proved mechanism.
The nonzero derivation \(\mathscr H\) has a transcendence-degree-one
constant field because it fixes \(g/f\). The classical rationality
input in pass64 gives \(\ker_L\mathscr H=k(r)\) in the unchanged
field. Thus \(S\in k(r)[X,Y]^2\).
The full determinant aligns all coefficient derivatives with
\(\mathscr H\ell\).

If \(S_r\ne0\), the proof gives
\[
Q_2=\rho(r)Q_1+D(r;X,Y)+I(r),\qquad
D_r=-\rho_rS_1.
\]
Actual coordinate-field generation forces degree one in \(r\).
The coefficientwise pole maximum over the finite support forces
\(\rho\) to be constant, exactly as in pass64, Section 4.
Then \(D\in k[X,Y]\), and
\[
I=Q_2-\rho Q_1-D(X,Y)\in B\cap L=C
\]
is an actual coordinate by its displayed triangular inverse.
The same original \(E\) and slice meet the Dedekind theorem
over \(k[I]\), so its kernel is \(k[I]^{[2]}\).
If \(S_r=0\), actualness gives \(\ell\in C^2\) and \(B=C[X,Y]\).
The slice gives \(u_0f+v_0g=1\) in \(C\); the exact inverse
\[
X=f\sigma+v_0j,\quad Y=g\sigma-u_0j,\qquad
\sigma=u_0X+v_0Y,\quad j=gX-fY
\]
gives \(\ker E=C[j]\).
All external source gates are exactly those explicitly retained
in pass64. No additional source theorem or numerical suite is used.

## 2. Why larger graph degree does not supply the live higher-flow inputs

The invariant-speed premise already implies
\[
E^2X=E^2Y=0.
\]
In the independent nonconstant high-top branch with nonzero
preceding bad vector, [pass42](two-quadratic-top-line-pass42.md)
instead proves, for the original bad pair,
\[
E^{m-1}(x_3,x_4)=\lambda g^{m-1}\ne0,\qquad m\ge3.
\]
Thus \(E^2(x_3,x_4)\ne0\). The unchanged original pair fails
the invariant-speed premise, irrespective of allowed graph degree.
An invariant rescaling \(E/g\) does not repair this vanishing
condition: its second iterate is \(g^{-2}E^2\) on \(B_g\).

In the dependent high-top nonzero-multiplier branch,
[pass43](dependent-defect-top-line-pass43.md) gives
\[
(0,0,a,b)E^{m-1}x=qr\ne0.
\]
The same invariant-speed obstruction holds for its unchanged bad pair.
In the independent constant-top cubic normal form of
[the pass65 reduction](constant-top-cubic-pass65.md),
\(E(Ex_3)=1\), so its identified two-variable defect kernel
is not a base pointwise killed by \(E\), as required by the theorem above.

The preceding-layer two-rings in pass44 likewise do not supply
an ambient coordinate pair or an invariant-plane presentation.
Recognition by an omitted good direction is a different, already
proved route. A replacement pair could potentially meet the
finite-graph hypotheses, but it would require an actual coordinate
inverse, invariant speeds, a proved generic polynomial two-ring,
Euler-invariant graph coefficients and the full determinant.
None of those missing gates is supplied merely by increasing
the permissible graph degree.

Accordingly this extension alone closes no additional recorded
higher-flow branch. It makes no universal-frame, exhaustive
branch-classification, human-review or formal-verification claim.
