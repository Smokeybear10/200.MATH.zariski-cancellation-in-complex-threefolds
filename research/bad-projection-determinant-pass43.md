# A determinant field and a rank-one bad-projection reduction

The independent-defect degree-two residual admits a genuine polynomial
locally nilpotent determinant field fixing an actual bad coordinate.
If its bad projection has rank one, the field fixes both bad coordinates
and has a polynomial three-ring as its kernel. The original action
restricts to a two-quasi derivation there, without inheriting a slice.

This closes the rank-one bad-projection branch when the two bad speeds
are relatively prime. An instance with algebraically independent speeds
left in that branch has an exact common-factor normal form, including
the full multiplicity of the common factor. It is a reduction of the
supplied frame problem, not a recognition theorem for every residual.

This is an intermediate reduction. The later same-pass
[rank-closure proof](bad-projection-rank-closure-pass43.md) excludes
the independent-speed rank-one common-factor alternative left here,
and proves equality of the bad-projection and bad-speed Jacobian
ranks under the original assumptions. The determinant construction
and its preliminary normal form below remain unchanged.

## 1. Original assumptions and a distinction of ranks

Retain all original assumptions of
[the degree-two reduction](two-quadratic-degree-two-pass42.md).
In particular \(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(E\) is a sliced
LND, \(E^3x=0\), the good columns have vanishing second adjoint, and
the two bad quadratic tops \(V_3,V_4\) are independent.
Write
\[
A=\ker E,\qquad E(s)=1,\qquad
f=Ex_3,\quad g=Ex_4,\qquad
\mathcal V=[V_3(x)\mid V_4(x)].
\tag{1}
\]
The inherited proof establishes the following global facts:

- \(f,g\) belong to the kernel of every displayed leading field;
- \(E,V_3,V_4\) commute, are LNDs, and have joint generic rank two;
- their nonzero restrictions to \(A\) have rank one and the same kernel.

Let \(C\) be that last common kernel and \(F=\operatorname{Frac}C\).
The letter \(F\) here denotes a field, not the vector of bad speeds.
For the primary remaining case \(f,g\) are algebraically independent,
so both are nonzero. The construction below only needs \(f\ne0\).

The rank of
\[
L_0\mathcal V=
\begin{pmatrix}
V_3x_3&V_4x_3\\
V_3x_4&V_4x_4
\end{pmatrix}
\tag{2}
\]
is not the rank of \(\operatorname{Jac}(f,g)\).
The inherited image inclusion puts \((f,g)^{\mathsf t}\) in the
image of (2), so (2) has rank at least one here. We do not assume
that its rank is two just because the speeds are independent.

## 2. A simultaneous translation chart over the common invariant field

Choose a nonzero restriction \(D=V_3|_A\), swapping the labels if
necessary. A local slice of \(D\), divided by its nonzero invariant
derivative, gives
\[
A\otimes_C F=F[r],\qquad B\otimes_C F=F[r,s],
\qquad E=\partial_s,\quad V_3r=1.
\tag{3}
\]
This is the usual local-slice theorem, applied only after inverting
nonzero elements of its actual kernel. No polynomiality of \(A\),
finite generation of \(C\), or global slice of \(D\) is assumed.

All the fields kill \(F\). Since they commute with \(E\), and their
restrictions to \(F[r]\) are LNDs, write
\[
V_3=\partial_r+a_3(r)\partial_s,\qquad
V_4=b_4\partial_r+a_4(r)\partial_s,
\quad b_4\in F,\quad a_i\in F[r].
\tag{4}
\]
Commutation gives \(a_4'=b_4a_3'\). Let \(Q'=a_3\) and
\(\tau=s-Q(r)\). Polynomial integration is legitimate over the
characteristic-zero field \(F\), and has the polynomial inverse
\(s=\tau+Q(r)\). Then
\[
E=\partial_\tau,\quad
V_3=\partial_r,\quad
V_4=b_4\partial_r+c_4\partial_\tau,\qquad
0\ne c_4\in F.
\tag{5}
\]
The final nonvanishing follows from independence of \(V_3,V_4\).
These are coordinates on the localized ring only.

## 3. The determinant combination is globally an LND

Define on the original polynomial ring
\[
K=(V_4x_3)V_3-(V_3x_3)V_4.
\tag{6}
\]
All its coefficients are polynomial. Since \(Ex_3=f\in C\),
in (5) there is \(q(r)\in F[r]\) with
\[
x_3=f\tau+q(r).
\]
Substituting in (6) gives the exact expression
\[
K=c_4\bigl(f\partial_r-q'(r)\partial_\tau\bigr).
\tag{7}
\]
This is a nonzero triangular LND over \(F\): after the invertible
shear \(\theta=\tau+q(r)/f\), it is \(c_4f\partial_r\).
For every original \(b\in B\), a finite iterate of the polynomial
derivation (6) therefore vanishes in the injective localization
\(B\hookrightarrow F[r,\tau]\), and hence in \(B\).
Thus (6) is a genuine global LND, not a rational field being
silently treated as an action on \(B\).

Moreover,
\[
[E,K]=0,\qquad Kx_3=0,\qquad
Kx_4=-\det(L_0\mathcal V).
\tag{8}
\]
For commutation use \(E(V_ix_3)=V_if=0\).
In particular \(K|_A\ne0\), since it is \(c_4f\partial_r\)
on the localization of \(A\).
It has the same intrinsic kernel \(C\) as the leading fields.
This construction does not produce a second intrinsic direction.
Its additional information is the actual ambient coordinate it fixes.

## 4. Rank-one projection gives an actual polynomial auxiliary kernel

Suppose now
\[
\operatorname{rank}(L_0\mathcal V)=1.
\tag{9}
\]
Then \(Kx_3=Kx_4=0\). Consequently (6) is a nonzero
\(\mathbb C[x_3,x_4]\)-LND of
\[
B=\mathbb C[x_3,x_4][x_1,x_2],
\]
an actual relative polynomial plane.
The UFD planar-kernel theorem gives
\[
R:=\ker K=\mathbb C[x_3,x_4,z]
\tag{10}
\]
for some \(z\in B\).[^planar]
This application uses the original coordinate pair \(x_3,x_4\);
it does not replace them by abstract invariant generators.

Because of (8), \(L=E|_R\) is a nonzero LND of this genuine
polynomial three-ring, with
\[
L^2x_3=L^2x_4=0.
\tag{11}
\]
It is not asserted that \(L\) has a slice or is primitive.
In fact a nonprimitive \(L\) is exactly what the remaining
independent-speed possibility requires below.

## 5. Exact two-quasi classification and the common factor

Divide the polynomial coefficient gcd of \(L\) in \(R\), writing
\[
L=dL_0,\qquad L_0\text{ a primitive LND of }R,\qquad
0\ne d\in\ker L_0.
\tag{12}
\]
This is the standard invariant-gcd reduction for an LND on a UFD.
Since \(L_0d=0\), (11) implies \(L_0^2x_3=L_0^2x_4=0\).
Wang's two-quasi classification has two alternatives.[^wang]

In its first alternative, \(L_0\) kills a nonzero constant linear
form in \(x_3,x_4\). The same form is killed by \(E\) and is an
actual ambient coordinate of \(B\). The original slice makes \(A\)
regular, so the fixed-coordinate regular-kernel theorem recognizes
\(A=\mathbb C^{[3]}\).[^regular]

In the second alternative there is a coordinate system
\[
R=\mathbb C[v,x_3,x_4],\quad L_0v=0,\quad
L_0x_3=p(v),\quad L_0x_4=q(v),\qquad
\gcd_{\mathbb C[v]}(p,q)=1.
\tag{13}
\]
Primitivity gives the stated gcd. Choose
\(\alpha p+\beta q=1\) in \(\mathbb C[v]\), and set
\[
j=q(v)x_3-p(v)x_4,\qquad
t=\alpha(v)x_3+\beta(v)x_4.
\tag{14}
\]
The polynomial inverse is
\[
x_3=p(v)t+\beta(v)j,\qquad
x_4=q(v)t-\alpha(v)j.
\tag{15}
\]
Thus \(L_0=\partial_t\) in \(R=\mathbb C[v,j,t]\), and
\[
C=\ker E\cap\ker K=\mathbb C[v,j],\qquad
d\in\mathbb C[v,j],\qquad
f=d(v,j)p(v),\quad g=d(v,j)q(v).
\tag{16}
\]
The first equality with the original \(C\) follows also by
localization: \(E,K\) span the same generic plane as \(V_3,V_4\).
Both kernels contract from that common invariant field.

In particular
\[
\gcd_B(f,g)=d\quad\text{up to a nonzero constant}.
\tag{17}
\]
There are no suppressed prime powers. One can prove (17) directly:
\(d\) divides both speeds, while the Bezout identity in (13)
expresses \(d=\alpha(v)f+\beta(v)g\). This also avoids any
unstated transfer of irreducibility between the two rings.

If \(f,g\) are algebraically independent, then necessarily
\[
p'q-pq'\ne0,\qquad \partial_jd\ne0.
\tag{18}
\]
Indeed their Jacobian in the actual generators \(v,j\) of \(C\) is
\[
\det\operatorname{Jac}_{v,j}(f,g)
=d\,(\partial_jd)\,(p'q-pq').
\tag{19}
\]
In characteristic zero, vanishing of this determinant for two
polynomials in a polynomial plane is equivalent to algebraic
dependence. Alternatively, if either factor in (18) vanishes,
the speeds have a constant ratio or both lie in \(\mathbb C[v]\).
Hence an independent-speed instance left here has a common
factor that varies in the second invariant \(j\), not merely
some unspecified nonconstant gcd.

## 6. A closed subcase and the exact remaining hypothesis

Under (9), if \(f,g\) are relatively prime in \(B\), then the
second alternative has \(d\in\mathbb C^*\). Its two speeds are
functions of \(v\), so their Jacobian has rank at most one.
The inherited original-frame image criterion recognizes
\(A=\mathbb C^{[3]}\) in that case.
The first Wang alternative was already recognized. Therefore
\[
\operatorname{rank}(L_0\mathcal V)=1,\quad \gcd_B(f,g)=1
\quad\Longrightarrow\quad \ker E=\mathbb C^{[3]}.
\tag{20}
\]

The general independent-speed residual is not closed.
It can still have rank two in (2), or rank one together with
the exact data (16)--(18). In the latter case, \(v\) is a
coordinate of \(R\), not a proved coordinate of \(B\).
The original slice was never transferred to \(L=d\partial_t\);
when \(d\) is nonunit, that restricted derivation has no slice.
Regularity of \(\ker E\) does not itself make \(\ker K\) a
polynomially split factor of \(B\).

The determinant construction is a controlled polynomial combination
of leading fields, so it is consistent with the pass-42 obstruction:
it retains the same one intrinsic direction. Its useful new
property is an actual bad-coordinate kernel, with both bad
coordinates retained precisely under (9).
No auxiliary coordinate is promoted to an ambient one without
the explicit original-frame gate.

## Exact finite controls

The standalone
[four-method checker](bad_projection_determinant_checks_pass43.py)
imports only `unittest` and SymPy. Its first run passed all four
methods in 0.566 seconds, with no failed assertions.
It reconstructs simultaneous straightening and the finite determinant
flow, recomputes the determinant field in the inherited actual
independent-defect example, checks a separate actual coordinate-pair
model for the rank-one determinant identity, and verifies the
two-quasi inverse with a repeated common factor.

Only the second method uses an actual independent-defect frame.
The rank-one coordinate-pair model and the repeated-factor restricted
normal form are not asserted to realize an unresolved original
residual. These checks do not prove the two classification inputs or
replace the generic localization argument.

## Source scope

All generic straightening and polynomial descent in (3)--(8)
are proved here from the local-slice theorem and commutation.
The planar-kernel and two-quasi inputs below are existing results,
not new classifications. Their exact statements were directly
reread in the cited publicly available research article; that
article explicitly attributes them to Daigle--Freudenburg and
Wang. This bounded pass did not retrieve and read the complete
original 1998 and 2005 papers, and does not claim otherwise.
No novelty, expert review, proof-assistant verification, or general
cancellation solution is asserted.

[^planar]: Daigle--Freudenburg, *Locally Nilpotent Derivations over a UFD and an Application to Rank Two Locally Nilpotent Derivations of k[X1,...,Xn]*, [Journal of Algebra 204 (1998), 353--371](https://www.sciencedirect.com/science/article/pii/S0021869398974658), Theorem 2.4; exact statement reproduced as Theorem 2.2, PDF p. 3, in Dasgupta--Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1). For a UFD \(S\) containing \(\mathbb Q\), a nonzero \(S\)-LND on \(S[X,Y]\) has kernel \(S[z]\). No fixed-point-free or slice hypothesis is imposed.

[^wang]: Wang, *Homogenization of locally nilpotent derivations and an application to k[X,Y,Z]*, Journal of Pure and Applied Algebra 196 (2005), 323--337, Theorem 4.7 and Remark 5; the complete two alternatives are reproduced as Theorem 4.1, PDF p. 9, in [Dasgupta--Gupta](https://arxiv.org/pdf/1701.03635v1). The field has characteristic zero and the three-variable derivation must be primitive. Equation (12) establishes that hypothesis before the theorem is applied.

[^regular]: Bhatwadekar--Gupta--Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. This is applied only to the original \(E\), with regular original kernel supplied by its slice and an actual invariant ambient coordinate.
