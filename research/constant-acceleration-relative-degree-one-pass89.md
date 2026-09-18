# The actual last-partial commutator forces generic degree one

In the remaining rank-one-speed and rank-two conical branches,
the two relative generators do more than give a finite generic
extension: their first generator is a coordinate on the generic
intrinsic line. An assumed critical point would force the actual
last-partial commutator into an impossible nonzero vertical vector.
This proof does not require global descent of the slice difference
or an assertion that its companion generator has zero derivative.

## 1. The actual common-kernel and two-generator hypotheses

Retain the actual constructions in the
[conical-normal proof](constant-acceleration-conical-normal-pass89.md)
or the [curve-speed proof](constant-acceleration-curve-speed-pass89.md).
Write
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad Eu=1,\quad
Ex_{\rm tr}=b\in S^3,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\ker(W|A)=\mathbb C[s_1,s_2],\qquad
A=S[Y,c],\qquad h=u-\sigma\in A\cap\operatorname{Frac}(S[Y]),\\
x_{\rm tr}=b(u-h)+VY+U_0c_0,\qquad
z=c+\frac q2(u^2-h^2),\qquad b,V,U_0\in S^3,\quad c_0\in S.
\end{gathered}
\tag{1}
\]
Here W is the original intrinsic highest-adjoint LND and kills u.
The slice sigma and the reconstruction in (1) are actual polynomial
identities. They are not a proposed ambient matrix automorphism.

Let P=(b_1,b_2,b_3,qu) transposed and J its Jacobian in the four
original coordinates. In the nontrivial remaining branches the
original T=partial_z has good second adjoint, and
\[
Q=[E,T]\ne0,\qquad Q\in\operatorname{LND}(B),\qquad
Q(u)=0,\qquad \ker(Q|A)=S,\qquad
Q(x_1,x_2,x_3,z)^t=-Je_4,\qquad JQ(x)=0.
\tag{2}
\]
These are the exact conclusions of conical-good-direction88 and
curve-speed89, including their common-highest-line arguments.
The final identity follows from J squared e_4=0. If Q is zero,
the predecessor stable-good-coordinate recognition branch applies;
that case is not part of the degree-one argument below. No claim
that T preserves S is assumed.

If Y is algebraic over Frac(S), the actual W kills it by
minimal-polynomial differentiation, hence Y belongs to S and
A=S[c] is already polynomial. Assume from now on that Y is
transcendental over K=Frac(S).

## 2. The generic line and polynomial slice difference

A local slice for W yields A_K=K[v]. Here and below subscripts K
mean localization at the nonzero elements of S. Since Q kills S,
it extends as an actual LND to this localization. Its restriction
to A_K is nonzero, because Q kills u and B=A[u]. A nonzero LND
of K[v] is a nonzero constant multiple of partial_v. Therefore
\[
A_K=K[v]=K[Y,c],\qquad
Q|_{A_K}=\lambda\partial_v,\quad\lambda\in K^*,\qquad
h=H(Y)\quad\text{for some }H\in K[T].
\tag{3}
\]
For completeness, if Qv were a nonconstant polynomial in v,
additivity of LND degree on products would contradict the drop
in LND degree from v to Qv. This proves the stated constant
coefficient without a coordinate choice for T.

The last claim of (3) uses only the generic integrality argument
in the [pole-support proof](constant-acceleration-pole-support-pass89.md).
The nonconstant polynomial Y in K[v] makes v integral over K[Y],
by dividing its polynomial equation by its leading coefficient.
Hence h in K[v] is integral over K[Y]. It also belongs to K(Y)
by (1). Normality of the polynomial ring K[Y] gives h in K[Y].
No global integrality of A over S[Y] or global membership of h
in S[Y] is required.

## 3. A critical point contradicts the original Jacobian identities

Suppose Y has degree at least two as a polynomial in v. Its
derivative has a root v_0 over an algebraic closure of K, since
the characteristic is zero. The generation equality in (3)
gives a polynomial G in K[T,C] with v=G(Y,c). Differentiate
this identity first, then specialize v to v_0. It gives
\[
Y'(v_0)=0,\qquad
1=G_T(Y(v_0),c(v_0))Y'(v_0)
  +G_C(Y(v_0),c(v_0))c'(v_0),\qquad c'(v_0)\ne0.
\tag{4}
\]
This does not assume c prime vanishes. It proves the opposite
at the proposed critical point. No differentiation of the
algebraic element v_0 itself is performed.

By h=H(Y), one has h prime at v_0 zero. Differentiate the
actual reconstruction (1) in v, fixing K and u, and then use (3).
At v_0 the original coefficient column of Q becomes
\[
Q(x)\big|_{v_0}=(0,0,0,\lambda c'(v_0))^t
                =\mu e_4,\qquad \mu\in\overline K^*.
\tag{5}
\]
All matrices and coefficients in (2), when expressed in the
actual ring K[v,u], may be specialized at this point. There is
no v-dependent denominator in these expressions. Applying the
last identity of (2) to (5) gives mu times J e_4 at v_0 equal
to zero. Since mu is nonzero, J e_4 at v_0 is zero. The other
identity Q(x)=-J e_4 then makes (5) zero, a contradiction.

Thus Y prime has no root over the algebraic closure of K.
Since Y is nonconstant and characteristic zero, its degree is one:
\[
\deg_vY=1,\qquad A_K=K[Y],\qquad
\operatorname{Frac}(A)=\operatorname{Frac}(S[Y]).
\tag{6}
\]
In particular the kernel is generically the polynomial line in
the actual first relative generator, in both stated branches.
This is stronger than an unspecified finite generic extension.

The argument does not make every divisor fiber a polynomial
line, put h globally in S[Y], prove that A=S[Y], or give a
global slice for Q. Those are separate remaining ring and fiber
questions. The original-coordinate identities (2) are essential;
an arbitrary commuting LND on an abstract relative curve does
not supply them.

Jet identified the critical-point obstruction from the actual
original-coordinate coefficient column. Root supplied the
generation identity v=G(Y,c) to prove the needed nonvanishing
without a coordinate-volume calculation. The generic integrality
input and exact two-generator hypotheses are retained from the
linked written proofs. This six-equation note introduces no new
primary classification theorem, checker, or numerical method,
and changes no pass88 or older file.
