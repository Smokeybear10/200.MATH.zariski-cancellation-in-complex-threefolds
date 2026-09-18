# Nonlinear reduction for invariant-coefficient extension rows

There is an all-degree polynomial-conjugacy classification for
\[
E=A(g)D_0+B(g)\partial_t,
\qquad D_0(r)=g\ne0,\qquad D_0(g)=0,
\tag{1}
\]
when both coefficients are polynomials in the same local-slice
derivative \(g\). The conjugacies mix the original three-variable base
with \(t\), and do not assume that any given slice is affine in \(t\).
Every nonzero derivation in this class on \(\mathbb C^{[4]}\) has an
abstract polynomial three-ring kernel, whether or not it has a slice.
The slice criterion is also exact.

A stronger variable-time flow construction applies over the whole
invariant ring, without an elementary-matrix factorization. Write
\(C=\ker D_0\). If \(A,B\in C\) and \(B\equiv1\pmod{gC}\), then
\(AD_0+B\partial_t\) has a slice exactly when \((A,B)C=C\), and in
that case an explicit polynomial automorphism conjugates it to a
coordinate partial. Section 6 proves this statement, including
nonreduced quotients in its necessary direction.

An arbitrary added coefficient is covered when an actual polynomial
shear puts it in this class. That is a sufficient algebraic criterion,
not an assertion that every slice extension admits such a shear. The
fixed Freudenburg all-coefficient theorem in
[arbitrary-coefficients-pass.md](arbitrary-coefficients-pass.md) is a
different result and is not reproved here.

## 1. The exact normal forms

Let \(R=\mathbb C[x_1,x_2,x_3]\), let \(0\ne D_0\in\operatorname{LND}(R)\),
and choose \(r\in R\) with
\[
g=D_0(r)\ne0,\qquad D_0(g)=0.
\]
For now assume \(g\notin\mathbb C\). Let \(A(u),B(u)\in\mathbb C[u]\)
be not both zero, and define (1) on \(S=R[t]\), extending \(D_0\) by
\(D_0(t)=0\). Let
\[
h=\gcd(A,B)\text{ monic},\qquad a=A/h,\quad b=B/h.
\]
Then there is a polynomial automorphism \(\Phi\) of \(S\), fixing
\(g\), such that
\[
\Phi E\Phi^{-1}=
\begin{cases}
h(g)b(0)\partial_t,&b(0)\ne0,\\
h(g)a(0)D_0,&b(0)=0.
\end{cases}
\tag{2}
\]
In the second case \(a(0)\ne0\), since \(a,b\) are coprime.
Here the zero in \(a(0),b(0)\) is the value of the formal one-variable
polynomial at zero. No assumption that \(g\) is an ambient coordinate
is made.

Consequently:

- \(\ker E\cong\mathbb C^{[3]}\) in both branches.
- \(E\) has a slice exactly when
  \[
  h=1\quad\text{and}\quad
  \bigl(b(0)\ne0\ \text{or }D_0\text{ has a slice}\bigr).
  \tag{3}
  \]
- If \(D_0\) has rank three, it has no slice, and (3) becomes
  \[
  E\text{ has a slice}\quad\Longleftrightarrow\quad
  \gcd(A,B)=1\ \text{and }B(0)\ne0.
  \tag{4}
  \]

The conjugacy construction itself works over any characteristic-zero
domain in which \(g\) is transcendental over the ground field. The
necessity of removing a nonconstant \(h(g)\) for a slice uses the
polynomial-ring unit condition. It must not be extended to a
localization where such a factor could be invertible.

## 2. Two allowed row operations are actual automorphisms

For \(H,K\in\mathbb C[u]\), define
\[
U_H=\exp\bigl(tH(g)D_0\bigr),\qquad
L_K=\exp\bigl(rK(g)\partial_t\bigr).
\tag{5}
\]
Both exponentials are polynomial automorphisms with inverses obtained
by negating the exponent. The first exponent is an invariant replica
of the extension of \(D_0\), since \(D_0(tH(g))=0\). The second is
a shear, since \(\partial_t(rK(g))=0\). Both fix \(g\).

With \([P,Q]=PQ-QP\), the exact conjugation identities are
\[
U_H D_0U_H^{-1}=D_0,\qquad
U_H\partial_tU_H^{-1}=\partial_t-H(g)D_0,
\]
\[
L_KD_0L_K^{-1}=D_0-gK(g)\partial_t,\qquad
L_K\partial_tL_K^{-1}=\partial_t.
\tag{6}
\]
For example,
\([tH(g)D_0,\partial_t]=-H(g)D_0\) and
\([rK(g)\partial_t,D_0]=-gK(g)\partial_t\); the next commutators
vanish. Thus (6) is exact, not a first-order approximation.

On the coefficient pair, these maps implement
\[
(A,B)\stackrel{U_H}{\longmapsto}(A-HB,B),\qquad
(A,B)\stackrel{L_K}{\longmapsto}(A,B-uKA).
\tag{7}
\]
The factor \(u\) in the second move is essential: it comes from
\(D_0(r)=g\). An arbitrary lower elementary operation is not being
assumed available.

Every step uses the same original derivation \(D_0\) and polynomial
\(r\). Although a previous automorphism may move \(r\), the resulting
derivation is again a pair in the fixed span of \(D_0,\partial_t\),
so (6) can be applied anew. There is no untracked moving-base term.

## 3. The Euclidean descent terminates in every degree

First suppose \(\gcd(A,B)=1\) and \(B(0)\ne0\). If \(B\) is
constant, the upper move with \(H=A/B\) immediately gives \((0,B)\).
Otherwise divide in the one-variable polynomial ring:
\[
A=HB+A_1,\qquad \deg A_1<\deg B.
\]
The upper move gives \((A_1,B)\). The remainder \(A_1\) is nonzero:
otherwise a nonconstant \(B\) would divide \(A\), contrary to
coprimality. Now divide once more:
\[
B=(uA_1)K+B_1,\qquad
\deg B_1<\deg(uA_1)=\deg A_1+1.
\]
The lower move gives \((A_1,B_1)\), and
\[
\deg B_1\le\deg A_1<\deg B,\qquad B_1(0)=B(0)\ne0.
\tag{8}
\]
The elementary moves preserve the gcd. Thus every complete cycle
strictly decreases the nonnegative integer \(\deg B\), while
preserving its nonzero value at zero. The process terminates at
\((0,B(0))\), after a final upper move if needed. All quotients are
polynomials; no denominator in \(g\) is introduced.

If instead \(B(0)=0\), write \(B=uC\). Coprimality gives
\(\gcd(C,A)=1\) and \(A(0)\ne0\). Apply the preceding algorithm to
the auxiliary pair \((C,A)\). Its upper operation
\(C\mapsto C-HA\) is the original lower move
\(B\mapsto B-uHA\). Its lower operation
\(A\mapsto A-uKC\) is the original upper move
\(A\mapsto A-KB\). Thus the same algorithm ends at
\((C,A)=(0,A(0))\), equivalently
\[
(A,B)=(A(0),0).
\tag{9}
\]
This also handles \(B=0\), when \(C=0\) and primitive \(A\) is
already a nonzero constant.

For a general pair \((A,B)=h(a,b)\), perform the appropriate
algorithm on the coprime pair \((a,b)\). The same row operations act
on \((A,B)\), and every automorphism fixes \(h(g)\). This proves (2).

## 4. Kernel and slice conclusions, including the degenerate branches

Multiplication by a nonzero invariant does not change a derivation's
kernel. In the first branch of (2), the kernel is \(R\). In the
second, it is
\[
(\ker D_0)[t].
\]
Miyanishi's theorem gives \(\ker D_0\cong\mathbb C^{[2]}\), in the
exact form recorded in
[Freudenburg, Theorem 2.4(a)](https://arxiv.org/pdf/2108.12021).
This proves the polynomial-kernel assertion without finding an ambient
coordinate in \(\ker D_0\).

If \(h\) is nonconstant, \(h(g)\) is a nonconstant polynomial of
\(R\), hence a nonunit. Every value of either normal-form derivation
lies in \(h(g)S\), so there is no slice. If \(h=1\), the first
normal form has the slice \(t/b(0)\). The second has a slice exactly
when \(D_0\) does: if \(D_0\) kills \(t\) and
\(a(0)D_0(\sum_j s_jt^j)=1\), its constant coefficient gives
\(a(0)D_0(s_0)=1\). Conversely a \(D_0\)-slice works after scaling.
This proves (3).

The remaining edge cases are explicit:

- If \(A=0\), then \(E=B(g)\partial_t\); its kernel is \(R\), and
  it has a slice exactly when \(B\) is a nonzero constant.
- If \(B=0\), then \(E=A(g)D_0\); its kernel is
  \((\ker D_0)[t]\), and it has a slice exactly when \(A\) is a
  nonzero constant and \(D_0\) has a slice.
- If both coefficient polynomials vanish, \(E=0\), its kernel is
  the four-ring \(S\), and it has no slice. This was excluded above.
- If \(g=\lambda\in\mathbb C^*\), then \(r/\lambda\) is a
  \(D_0\)-slice. Evaluate the coefficient polynomials at \(\lambda\)
  first. If both values are zero, \(E=0\); otherwise the resulting
  constant-coefficient pair is a translation, with polynomial kernel.
  The formal gcd of \(A(u),B(u)\) is not a slice criterion in this
  constant-parameter case.

If one allows \(g=0\), the premise is no longer a local slice. The
pair again evaluates to constants: a nonzero \(B(0)\) gives a
translation by a finite flow, while \(B(0)=0\), \(A(0)\ne0\) gives
the constant replica \(A(0)D_0\). No \(D_0\)-slice follows merely
from \(D_0(r)=0\).

## 5. A useful criterion for a genuinely noninvariant added coefficient

Now begin with
\[
E=A(g)D_0+f\partial_t,
\qquad f\in R
\]
without assuming \(D_0(f)=0\). Suppose one can exhibit
\(H\in R\) and \(B(u)\in\mathbb C[u]\) such that
\[
f=B(g)+A(g)D_0(H).
\tag{10}
\]
The polynomial shear \(\Psi=\exp(H\partial_t)\) gives
\[
\Psi E\Psi^{-1}=A(g)D_0+B(g)\partial_t.
\]
Thus (2)-(4) apply verbatim. The method handles arbitrary degree in
\(H\), and \(f\) need not be invariant. In particular, it gives
explicit nonlinear recognition after a checkable primitive identity
(10), without inspecting the degree of an existing slice.

Equation (10) is a sufficient presentation to be proved for the given
input. Its existence is not inferred from the slice assumption. The
known quadratic-in-\(t\) countercontrol from the earlier pass shows
why an unrestricted assertion of that sort would need a new argument.

For the previous non-gauge family \((A,B)=(u-1,u+1)\), the complete
row trace is
\[
(u-1,u+1)\stackrel{U_1}{\longmapsto}(-2,u+1)
\stackrel{L_{-1/2}}{\longmapsto}(-2,1)
\stackrel{U_{-2}}{\longmapsto}(0,1).
\tag{11}
\]
Thus the Euclidean lemma contains the earlier base-mixing certificate
and extends it to arbitrary coprime one-parameter pairs.

## 6. A variable-time lift over the whole invariant ring

The Euclidean algorithm is not needed for the following stronger
translation criterion. In this section \(R\) can be any domain over
a field of characteristic zero, \(D_0\) is a nonzero locally
nilpotent derivation, and
\[
C=\ker D_0,\qquad D_0(r)=g\ne0,\qquad g\in C.
\]
Suppose \(A,B\in C\) and
\[
B=1+gQ,\qquad Q\in C.
\tag{12}
\]
Define \(E=AD_0+B\partial_t\) on \(R[t]\). Then the following
conditions are equivalent:

1. \(E\) has a slice.
2. \((A,B)C=C\).
3. \((gA,B)C=C\).
4. \(E\) is conjugate by a polynomial algebra automorphism of
   \(R[t]\) to \(\partial_t\).

In particular, in the original case \(R=\mathbb C^{[3]}\), this
gives \(\ker E\cong\mathbb C^{[3]}\). The construction does not
require a slice of \(D_0\), polynomial generators of \(C\), or
elementary generation of a matrix group over \(C\).

### 6.1. The certificate and the two algebra maps

Conditions 2 and 3 are equivalent because \(g\) is a unit modulo
\(B\), with inverse \(-Q\). More explicitly, if
\(AU+BV=1\), then the choices
\[
L=-QU,\qquad M=AU+V
\]
give
\[
BM+gAL=1.
\tag{13}
\]
Conversely (13) directly implies condition 2. Assume such \(L,M\in C\)
have been chosen. Reducing (13) modulo \(g\) gives \(M\equiv1\pmod g\).
In fact \(M-1=-g(QM+AL)\), so this divisibility holds in \(C\).
Set
\[
W=Qr-At,\qquad
W'=\frac{M-1}{g}r+At.
\tag{14}
\]
Both expressions are polynomials. For \(f\in R\), let
\[
\theta_T(f)=\sum_{j\ge0}\frac{T^j}{j!}D_0^j(f)\in R[T]
\]
be the finite flow with an independent parameter \(T\). Define
algebra maps on \(R[t]\) by
\[
\begin{aligned}
\Phi(f)&=\theta_T(f)\big|_{T=W},&
\Phi(t)&=Lr+Mt,\\
\Psi(f)&=\theta_T(f)\big|_{T=W'},&
\Psi(t)&=-Lr+Bt.
\end{aligned}
\tag{15}
\]
These are algebra maps because independent-time flow and polynomial
evaluation are algebra maps. In particular, (15) is not the exponential
of the derivation \(WD_0\): generally \(D_0(W)=B-1\ne0\).
No local nilpotence of \(WD_0\) is asserted or needed.

Both maps fix every element of \(C\), and their action on the
local-slice pair is
\[
\begin{pmatrix}\Phi(r)\\\Phi(t)\end{pmatrix}
=
\begin{pmatrix}B&-gA\\L&M\end{pmatrix}
\begin{pmatrix}r\\t\end{pmatrix},
\qquad
\begin{pmatrix}\Psi(r)\\\Psi(t)\end{pmatrix}
=
\begin{pmatrix}M&gA\\-L&B\end{pmatrix}
\begin{pmatrix}r\\t\end{pmatrix}.
\tag{16}
\]
The two matrices are inverse by (13). More importantly, a calculation
on the actual variable-time parameters gives
\[
\Phi(W')=-W,\qquad \Psi(W)=-W'.
\tag{17}
\]
For example, the coefficient of \(r\) in \(\Phi(W')\) is
\(((M-1)B+gAL)/g=(1-B)/g=-Q\), and its coefficient of
\(t\) is \(A\).

The independent-time group law now proves inverse identities on all
of \(R\), not merely on \(r\):
\[
\Phi\Psi(f)=\theta_{W+\Phi(W')}(f)=f,
\qquad
\Psi\Phi(f)=\theta_{W'+\Psi(W)}(f)=f.
\]
This notation means finite polynomial evaluation after using the
two independent parameters in the flow group law. The inverse
identities on \(t\) follow from (16). Thus \(\Phi\) and \(\Psi\)
are mutually inverse polynomial automorphisms.

### 6.2. Conjugation and an explicit slice

Since \(A,B,Q,L,M\) are invariant,
\[
E(W)=QgA-AB=-A.
\tag{18}
\]
Differentiating the finite independent-time flow before evaluation
therefore gives, for every \(f\in R\),
\[
E\Phi(f)
=A\,\theta_W(D_0f)+E(W)\,\theta_W(D_0f)=0.
\]
Also
\[
E\Phi(t)=LAg+MB=1.
\tag{19}
\]
Consequently
\[
\Phi^{-1}E\Phi=\partial_t,\qquad
\ker E=\Phi(R),\qquad s=\Phi(t)=Lr+Mt.
\tag{20}
\]
The conjugation orientation in (20) is the inverse of the convention
used for the row operations in (2). It follows directly from
\(E\Phi=\Phi\partial_t\).

### 6.3. Necessity, including nonreduced quotients

Suppose \(E(s)=1\) for some polynomial \(s\in R[t]\), with no
restriction on its degree in \(t\). If \(B\) is a unit of \(C\),
condition 2 is immediate. Otherwise reduce the slice equation modulo
\(B\). The ideal \(BR[t]\) is stable because \(E(B)=0\), and
the equation becomes
\[
\overline A\,\overline{D_0}(\overline s)=1
\quad\text{in }(R/BR)[t].
\tag{21}
\]
Since \(B=1+gQ\), the class of \(g\) is already a unit in
\(R/BR\). The local-slice theorem and localization therefore give
\[
R/BR\cong R_g/BR_g
\cong (C_g/BC_g)[r/g]
\cong (C/BC)[r/g].
\tag{22}
\]
Here the last isomorphism follows again from the polynomial inverse
\(-Q\) for \(g\) modulo \(B\). In particular, (22) is valid when
\(C/BC\) has nilpotents. No reducedness or unique factorization of
that quotient is used.

For completeness, the local-slice identity used here is
\(R_g=C_g[r/g]\): the element \(r/g\) has derivative 1, and
subtracting the appropriate invariant multiple of its highest power
reduces the \(D_0\)-degree of any element of \(R_g\). Induction
gives generation, while applying the highest nonzero derivative to
a proposed polynomial relation gives algebraic independence. The
invariant ring of \(R_g\) is \(C_g\), since \(g\) is invariant.

Evaluate the polynomial identity (21), under (22), at \(t=0\) and
\(r/g=0\). It yields an inverse for \(\overline A\) in \(C/BC\).
Thus \(AU+BV=1\) for some \(U,V\in C\), proving condition 2.
This argument also covers \(B=0\): then (12) forces \(g\) to be
a unit, the local slice is global, and the same evaluation proves
that \(A\) is a unit. It does not use the polynomial-ring unit
condition required for the separate gcd necessity in Section 4.

### 6.4. The two-invariant example is now explicitly resolved

Let \(\eta\in C\), with no dependence assumption on \(g\). Take
\[
A=g^2,\qquad B=1+g\eta,\qquad
M=1-g\eta+g^2\eta^2,\qquad L=-\eta^3.
\tag{23}
\]
Then \(BM+gAL=1\). Thus
\[
E=g^2D_0+(1+g\eta)\partial_t
\]
is a translation, with the explicit slice
\[
s=(1-g\eta+g^2\eta^2)t-\eta^3r
\]
and base generators given by the finite flow at
\(W=\eta r-g^2t\). This proves coordinatehood of the entire
kernel presentation through (15), not just the slice identity.

The degree descent of Section 3 still does not extend to an arbitrary
multivariable coefficient ring. The variable-time construction avoids
that issue altogether. No assertion that the matrix in (16) is a
product of elementary matrices is made.

### 6.5. Scope and noninvariant coefficients

The same theorem holds with \(B\equiv\beta\pmod{gC}\), where
\(\beta\) is a nonzero scalar: replace \(E\) by \(E/\beta\)
and its coefficient pair by \((A/\beta,B/\beta)\). It also applies
after an exhibited shear
\[
f=B+A D_0(H),\qquad A,B\in C,\quad H\in R,
\]
as in Section 5, provided the invariant remainder satisfies the
congruence and the invariant coefficient pair is unimodular.

The congruence \(B\equiv\beta\pmod{gC}\) is a real hypothesis.
The proof does not replace it by general unimodularity, does not
establish that arbitrary \(f\) has the required shear presentation,
and does not assume that an initially given slice is affine in
\(t\). It constructs a new affine slice only after the stated
coefficient conditions have been proved.

The all-degree results of this pass are the one-parameter normal
forms (2) and the invariant-ring translation criterion of Section 6,
together with their explicit polynomial maps. They supply nonlinear
base-mixing reductions for specified families. They do not classify
arbitrary rank-three base extensions or arbitrary slice LNDs on
four-space, and make no novelty claim.
