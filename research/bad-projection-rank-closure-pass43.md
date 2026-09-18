# Rank-one bad projection cannot retain independent speeds

The remaining common-factor alternative of the
[determinant-field reduction](bad-projection-determinant-pass43.md)
is incompatible with the original degree-two action. Thus, in the
independent-defect degree-two case with a slice, the bad projection
has the same rank as the bad-speed Jacobian. Rank-one bad projection
is recognized; every still-unrecognized independent-speed instance
has rank-two bad projection.

This uses the full original polynomial action, not a slice on the
auxiliary kernel. It does not recognize the rank-two projection
residual or assert that the middle fields are locally nilpotent.

## 1. Exact original-ring data

Retain the assumptions and notation of
[the degree-two proof](two-quadratic-degree-two-pass42.md).
Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be the original
sliced LND, and put
\[
h=E^2x\ne0,\qquad H=h\cdot\partial_x,\qquad
f=Ex_3,\quad g=Ex_4,\qquad
\mathcal V=[V_3(x)\mid V_4(x)].
\tag{1}
\]
Here \(\mathcal V\) has rank two. Let \(\mathcal P\) be its
two-dimensional fraction-field span, and \(C\) the common kernel
of the leading restrictions on \(A=\ker E\).
The inherited global identities are
\[
h_3=h_4=0,\quad f,g,h_1,h_2\in C,\quad
\mathcal P=\ker_{\operatorname{Frac}B}\operatorname{Jac}h,
\quad E\in\mathcal P,
\tag{2}
\]
and
\[
\mathcal L:=[E,H]=-\frac12(fV_3+gV_4),\qquad
[E,\mathcal L]=0.
\tag{3}
\]
In particular \(\mathcal L\) annihilates every element of \(C\).
The inclusion \(h_i\in C\) follows from the actual conjugated-column
identities \(Eh_i=V_3h_i=V_4h_i=0\), not just from \(Eh_i=0\).

Suppose, for contradiction, that
\[
\operatorname{rank}(L_0\mathcal V)=1,\qquad
\operatorname{rank}\operatorname{Jac}(f,g)=2.
\tag{4}
\]
The determinant proof and exact two-quasi classification already
give polynomial elements \(v,j\in B\) such that
\[
C=\mathbb C[v,j],\quad
j=q(v)x_3-p(v)x_4,\quad
f=d(v,j)p(v),\quad g=d(v,j)q(v),
\tag{5}
\]
with
\[
0\ne d,\qquad p'q-pq'\ne0.
\tag{6}
\]
These statements hold in the original ring. No claim that \(v\)
is an ambient coordinate is used. The first classification
alternative, a constant linear invariant in \(x_3,x_4\), is
already incompatible with the second rank in (4).

## 2. The highest field annihilates the common invariant plane

For every \(b\in C\), (3) gives
\[
E(Hb)=H(Eb)+[E,H]b=0.
\tag{7}
\]
Thus \(H(v)\) and \(H(j)\) are polynomial invariants of the
original \(E\). This does not by itself assert that \(H\)
preserves \(C\).

Since \(Hx_3=Hx_4=0\), differentiate the actual identity for \(j\):
\[
H(j)=(q'(v)x_3-p'(v)x_4)H(v).
\tag{8}
\]
Apply \(E\), using (7) and \(Ev=0\). One obtains
\[
0=(q'f-p'g)H(v)=d(q'p-p'q)H(v).
\tag{9}
\]
The coefficient is nonzero by (6). The original ring is a domain,
so \(H(v)=0\). Equation (8) gives \(H(j)=0\). Consequently
\[
H|_C=0,\qquad H(h_i)=0\quad\text{for every }i.
\tag{10}
\]
In particular \(H\) is a nonzero polynomial nice LND.
Only its nonzero polynomial coefficient vector and (10) are
needed for the remaining proportionality argument.

## 3. Proportionality and the polynomial Riccati obstruction

By (10), \(h=H(x)\) lies in \(\ker\operatorname{Jac}h=\mathcal P\).
It is nonzero by (1), and lies in the good-coordinate plane
\[
G=\{(z_1,z_2,0,0)^{\mathsf t}\}.
\]
The rank-one assumption on \(L_0\mathcal P\) implies
\[
\dim(\mathcal P\cap G)=1,\qquad
\mathcal P\cap G=(\operatorname{Frac}B)h.
\tag{11}
\]
Also \(\mathcal L\in\mathcal P\) by (3). It has zero bad
components: for \(i=3,4\),
\[
\mathcal L(x_i)=E(Hx_i)-H(Ex_i)=0,
\]
because \(Hx_i=0\) and \(f,g\in C\).
There is therefore a rational coefficient \(a\) with
\[
[E,H]=aH.
\tag{12}
\]

Let \(b\in B\setminus\{0\}\) be the gcd of the nonzero
components of \(h\), and put \(H_0=H/b\).
Every component of \(h\) is killed by \(E\). Factorial closure
of \(\ker E\) gives \(Eb=0\), including every prime power in
the gcd. Thus
\[
[E,H_0]=aH_0,\qquad [E,[E,H_0]]=0.
\tag{13}
\]
The coefficient \(a\) is polynomial. The left side of the first
identity is a polynomial field. A denominator of the reduced
fraction \(a\) would divide every coefficient of \(H_0\);
their gcd is one.

Expanding the second commutator gives
\[
E(a)+a^2=0.
\tag{14}
\]
If \(a\ne0\), the Leibniz rule gives by induction
\[
E^n(a)=(-1)^n n!a^{n+1}\ne0\qquad(n\ge1),
\]
contradicting local nilpotence of the original \(E\).
Therefore \(a=0\). Polynomiality was proved before applying
local nilpotence; no rational rescaling of \(E\) was used.

Equations (12) and (3) now imply
\[
fV_3+gV_4=0.
\tag{15}
\]
Independence of the two fields forces \(f=g=0\), contradicting
(4). This excludes the proposed common-factor residual at
every multiplicity and every \(j\)-degree.

## 4. Exact remaining rank and the middle fields

The original image identities give
\[
(f,g)^{\mathsf t}\in\operatorname{im}(L_0\mathcal V)
\subseteq\operatorname{im}\operatorname{Jac}(f,g).
\tag{16}
\]
More precisely \(L_0\mathcal V=2\operatorname{Jac}(f,g)
J_{\{3,4\}}\), so its rank is at most that of the bad-speed
Jacobian. For Jacobian rank zero, (16) gives \(f=g=0\)
and the displayed matrix identity gives projection rank zero.
For Jacobian rank one, the speed vector is nonzero, so (16)
makes projection rank exactly one.
For Jacobian rank two, (16) rules out projection rank zero
and the proof above rules out one. Hence
\[
\operatorname{rank}(L_0\mathcal V)
=\operatorname{rank}\operatorname{Jac}(f,g).
\tag{17}
\]
Thus rank-one bad projection is fully recognized by the
original invariant-linear-coordinate criterion.

For completeness, in every remaining independent-speed case
the two genuine slice-corrected middle fields
\[
N_i=W_i-sV_i-(W_i(s)-sV_i(s))E,\qquad i=3,4,
\tag{18}
\]
centralize \(E\) and kill its chosen original slice \(s\).
They restrict to polynomial derivations of \(A\).
The actual conjugated-column comparison gives
\[
N_i(f,g)^{\mathsf t}=W_i(f,g)^{\mathsf t}
=-\frac12L_0V_i(x).
\tag{19}
\]
By (17), these two column vectors are independent.
Together with a nonzero intrinsic leading field, which kills
\(f,g\), they give three generically independent intrinsic
polynomial derivations.

This is a full generic derivation span, not a locally nilpotent
or commuting frame. It gives neither an intrinsic slice nor
local nilpotence of (18). The rank-two-projection problem
still requires admissible corrections, another action, or an
actual coordinate change. The frozen leading-module obstruction
remains unchanged.

## Verification and attribution

This deduction uses the source-audited determinant construction
and the exact Daigle--Freudenburg/Wang alternatives in the linked
note. No new classification theorem is invoked.
The new exclusion is the original-ring calculation (7)--(15),
including the invariant-gcd and polynomial-coefficient gates.
No rank-one-projection residual with independent speeds is
claimed to exist, and no numerical example proves its exclusion.
The separate [three-method checker](bad_projection_rank_closure_checks_pass43.py)
imports only `unittest` and SymPy. Its first run passed in 0.213 seconds,
with no failed assertions. It checks the Wronskian differentiation,
polynomial Riccati iterates against the rational and moving-gcd
countercontrols, and the actual rank-two-projection boundary where
the highest field and its commutator are not proportional.
Independent AI reconstruction is not expert review or formal
proof. No novelty or general cancellation claim is made.
