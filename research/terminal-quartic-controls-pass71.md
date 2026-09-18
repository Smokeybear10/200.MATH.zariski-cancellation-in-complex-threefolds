# Exact controls for the terminal quartic reduction and endpoint

The separate [standalone checker](terminal_quartic_recognition_checks_pass71.py)
contains three bounded exact methods. It accompanies the written
[parabolic reduction](terminal-quartic-parabolic-form-pass71.md),
[speed-proportionality lemma](nice-chain-speed-proportionality-pass71.md),
and [terminal recognition endpoint](terminal-quartic-recognition-pass71.md).
It does not establish those theorems by computation.

## 1. The one-power polynomial derivation

The first method uses the polynomial coefficient ring
\[
\mathbb Q[\nu_1,\nu_2,a,b,z,w,g,N,U,V,p].
\]
Here \(g,N,U,V,p\) are independent additional indeterminates.
Consequently this is not an example of the original polynomial
four-ring, and it does not realize the original adjoint profile.

The formal original-velocity table is
\[
E(a,b,z,w)=
\left(V+\frac{gb}{3},\ U+g\left(\frac z2+c_0\right),
2N+2\nu_2g,\ p\right),\qquad
c_0=2\nu_1+\frac{\nu_2^2}{2},
\]
\[
E(g,N,U,V,p)=\left(0,\frac{g^2}{2},gN,\frac{gU}{3},0\right).
\]
The second table is
\[
T(a,b,z,w)=\left(\frac U3,N,g,0\right),\qquad
T(g,N,U,V,p)=0.
\]
The checker differentiates these tables to verify \([E,T]=0\),
\(T^2\) of every generator, and the polynomial recovery of
\(N,U,V\) from the displayed original velocities.
It also verifies \(T=gS\) in the fraction field, the normalized
coefficient derivatives, the two cleared common invariants, and
the exact \(g^2\)-divisibility expansion of their cusp expression.
The polynomial quotient is checked to be killed by both fields.

This method separately tests both inverse orders of the actual
four-coordinate shear
\[
a=a_0-z^2/12+\nu_2b/3,
\]
its Jacobian and inverse-Jacobian identities, and the transported
partials. In particular the two good coordinate partials remain
unchanged. This is an actual polynomial automorphism calculation;
it does not turn the larger coefficient model into a full-frame
four-dimensional action.

## 2. The weighted highest coefficient

The second method substitutes the finite flows of \(w,N,U,g\)
into \(A(w)U+B(w)N+C(w)g\). It extracts the coefficient of
\(t^d\), where
\[
d=\max\{\deg A+2,\deg B+1,\deg C\},
\]
omitting zero polynomials. Eight selected cases cover weighted
degrees zero and one, zero coefficient polynomials, a three-way
tie, and each possible unique highest summand.

The coefficient is compared with the stated starred-coefficient
formula and its normalization by \(gp^{d-2}\). The latter is
performed in a rational function field, including \(d<2\).
The input expressions are not asserted to be zero relations.
The finite cases check extraction and normalization identities;
they do not exhaust all polynomial degrees or prove that the
linear relation exists.

## 3. Both actual endpoint shears

The third method checks both inverse orders, unit Jacobians,
and transported partials for each branch of the endpoint.
For \(f=w/(2\lambda)\), the first branch uses
\[
h=\alpha u+\gamma-u^2,\quad \beta=f+u,\quad
L=(2f+\alpha)/3,\quad R=(-f^2-\alpha f+\gamma)/3,
\]
and the actual coordinate map
\[
(a,b,z,w)\longmapsto(a-Lb-Rz,\ b-fz,\ z,w).
\]
It checks that the formal field has new outputs \((0,u,1,0)\),
that \(\partial_{b'}=\partial_b+L\partial_a\), and that
\(EL=g/3\), \(E^2L=0\). Substituting the written hypothesis
\(gW_a=-3V_b/2\) into the adjoint product rule verifies the
exact new-good-partial cancellation.

The second branch uses \(\beta=f+u_0\), with \(u_0\) constant,
and \(P=w^2/(12\lambda^2)+u_0w/(3\lambda)\). Its actual shear
\((a,b,z,w)\mapsto(a-Pz,b-\beta z,z,w)\) has formal field
outputs \((\chi,0,1,0)\), while
\(\partial_{a'}=\partial_a\). The derivative identity
\(\lambda P'=\beta/3\) is checked exactly.

Only \(\lambda\) is inverted in these coordinate maps, and it
is a nonzero constant. The quantities \(u\) and \(\chi\) are
formal invariant coefficients in the output calculations, not
asserted polynomial functions realizing a full original action.
The written proof supplies their actual rational membership and
all hypotheses of the separate rational two-direction theorem.

## Verification and source boundary

The first complete three-method run passed in **0.154 seconds**,
exit zero. An earlier two-method development run passed in
0.101 seconds; it is not another suite or additional methods.
Only `unittest` and SymPy are imported. No project solver or
classification procedure is imported.

The checker author independently reconstructed all three written
pass71 notes through EOF and reread the complete retained rational
two-direction argument before finishing these controls. Those
proof reviews are separate from author self-review of this note
and its checker. The source theorem used in the endpoint was read
as Dasgupta--Gupta's explicit statement of Wang's result; no fresh
read of Wang's inaccessible original proof is claimed.

These are exact symbolic controls, not a proof certificate,
human expert review, full-frame construction, exhaustive search,
or fresh full regression. No frozen file or shared metadata was
changed. Independent review and later runs, if any, must be
recorded separately after they occur.
