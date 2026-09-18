# A one-parameter normal form for the dependent preceding layer

The nonconstant high-flow dependent-defect branch has a smaller
preceding invariant layer than its variable companion row initially
suggests. That layer lies in an actual polynomial parameter algebra.
Its weighted differential equation then has two exhaustive forms:
a common-power bad layer, or a rotating layer with an exact principal
multiplier ideal. A divisibility test also restricts motion of the
parameter under the actual good constant partial.

These are statements about the supplied polynomial frame. They do not
make the parameter an ambient coordinate, make the primitive defect
direction nice, or recognize the whole dependent-defect sector.

## 1. Original action and inherited identities

Retain the hypotheses of
[the dependent high-top proof](dependent-defect-top-line-pass43.md).
Thus \(B=\mathbb C[x_1,x_2,x_3,x_4]\), \(E\) is an LND with an
original polynomial slice, and the actual partials have the bounds
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_3=
\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
The two nonzero quadratic defects have rank one, with primitive
polynomial LND \(D\) and multipliers
\[
V_3=aD,\quad V_4=bD,\quad [E,D]=0,
\qquad a,b\in\ker E\cap\ker D.
\tag{2}
\]
Assume \(a,b\) have no nonzero complex constant relation. In particular
both are nonzero. Put \(J=\operatorname{Jac}(Ex)\) and
\(\ell=(0,0,a,b)\). The actual five-dimensional companion is
\[
M=\begin{pmatrix}J&-D(x)/2\\\ell&0\end{pmatrix},\qquad
(M^j)_{\rm UL}=\operatorname{Jac}(E^jx)/j!.
\tag{3}
\]

Suppose the last nonzero iterate is nonconstant and has order at least
three. The established full-image calculation gives
\[
m\in\{3,4\},\quad z=E^{m-1}x,\quad
E^mx=cq,\quad c\in\mathbb C^4\setminus\{0\},\quad c_3=c_4=0,
\tag{4}
\]
where \(q\) is nonconstant. Its Jordan partition is \((4,1)\) for
\(m=3\), or \((5)\) for \(m=4\). The further exact identities are
\[
Dz=ct,\quad Eq=Dq=0,\quad
\rho=\ell z=qr,\quad r\in\ker E\cap\ker D,\quad
[E,T_c]=-\frac{m-1}{2}rD,
\tag{5}
\]
and
\[
m q\,\ell\,dz=(m-1)\rho\,dq,
\qquad T_cq=\frac{m(m-1)}2rt.
\tag{6}
\]
Here \(t\in B\), \(T_c=\sum c_iT_i\), and \(d\) denotes ordinary
polynomial differential. All repeated factors in \(q\mid\rho\)
are included. The trace identity in (6) uses the complete auxiliary
column, not only the upper-left block.

Assume from now on \(r\ne0\). The zero case is already recognized.
The original slice and the trace calculation also prove that \(E,D\)
are fraction-field independent. No slice of \(D\) is assumed.

## 2. The preceding invariant layer has exactly one parameter

Choose \(j\) with \(c_j\ne0\), and set
\[
\tau=z_j/c_j,\qquad k=z-c\tau.
\tag{7}
\]
Then \(E\tau=q\), \(D\tau=t\), \(Ek=Dk=0\), and \(k_j=0\).
In particular \(k_3=z_3\) and \(k_4=z_4\).

For either partition in (4),
\(\operatorname{rank}M^{m-1}=2\). The row space of \(M^m\) is
contained in that of \(M^{m-1}\). Stacking these two matrices and
restricting to their four base columns therefore gives rank at most
two. The top rows contain \(\operatorname{Jac}z\) and
\(\operatorname{Jac}(cq)\), with nonzero constant factorial factors.
It follows that
\[
\operatorname{rank}\operatorname{Jac}(z,q)\le2.
\tag{8}
\]
The forms \(d\tau,dq\) are independent: the first evaluates to the
nonzero \(q\) on \(E\), the second evaluates to zero, and \(dq\ne0\).
Hence the rank in (8) is exactly two. The forms \(dk_i,dq\) lie in
this two-dimensional space and all annihilate \(E\). Its annihilator
of \(E\) is one-dimensional. Thus
\[
\operatorname{rank}\operatorname{Jac}(k,q)=1.
\tag{9}
\]
This proof retains the auxiliary rows until after the row-space
comparison. It does not replace a variable weighted row by the
Jacobian of its product.

In characteristic zero, (9) says that the polynomial algebra
\(\mathbb C[k_1,k_2,k_3,k_4,q]\) has transcendence degree one.
The polynomial curve-factorization theorem supplies an element
\(u\in B\setminus\mathbb C\) such that
\[
q=Q(u),\qquad k=K(u),\qquad Q,K_i\in\mathbb C[U],
\qquad \deg Q>0.
\tag{10}
\]
More precisely, its fraction field is \(\mathbb C(u)\) and its
normalization inside that field is \(\mathbb C[u]\).[^curve]
This is an actual polynomial parameter in the original ring, not a
formal variable substituted without an existence theorem. From
\(Eq=Dq=0\) and \(Q'(u)\ne0\),
\[
Eu=Du=0.
\tag{11}
\]
No claim that \(u\) is a coordinate follows from this factorization.

## 3. Exhaustive weighted-curve alternatives

Define two univariate polynomials
\[
A_i=mQK_i'-(m-1)Q'K_i\quad(i=3,4).
\tag{12}
\]
Since \(\ell c=0\), the first identity in (6) becomes
\[
a A_3(u)+b A_4(u)=0.
\tag{13}
\]
Also \(aK_3(u)+bK_4(u)=q r\ne0\).

### The common-power alternative

Suppose \(A_3=A_4=0\). At least one \(K_i\) is nonzero, by
\(qr\ne0\). For each such component, (12) says
\(mQK_i'=(m-1)Q'K_i\). Comparing orders at every complex root gives
\(m\,\operatorname{ord}K_i=(m-1)\operatorname{ord}Q\).
There are no other roots of \(K_i\). Since \(m,m-1\) are coprime,
every multiplicity of \(Q\) is divisible by \(m\). Absorbing a
nonzero complex constant into an \(m\)-th root, obtain
\[
g=G(u)\in B\setminus\mathbb C,\qquad
q=g^m,\qquad
(z_3,z_4)^{\mathsf t}=\lambda g^{m-1},
\tag{14}
\]
for a nonzero constant vector \(\lambda=(\lambda_3,\lambda_4)\).
Zero components of \(\lambda\) are allowed. Equation (5) then gives
the exact polynomial divisibility
\[
\lambda_3a+\lambda_4b=gr.
\tag{15}
\]
This conclusion concerns the bad part of the preceding layer. It
does not assert that every component of \(K\) belongs to
\(\mathbb C[G]\), or that \(a,b\) have a constant relation.

### The rotating alternative and its full denominator ideal

If the pair in (12) is not zero, both components are nonzero. Otherwise
(13) would force \(a=0\) or \(b=0\). Their projective ratio is not
constant, since that would give a forbidden constant relation between
\(a,b\). Put
\[
\Delta=\gcd(A_3,A_4),\qquad
a_0=-A_4/\Delta,\quad b_0=A_3/\Delta,
\qquad \gcd(a_0,b_0)=1
\tag{16}
\]
in \(\mathbb C[U]\), taking \(\Delta\) monic. Equation (13) says
\(a b_0(u)=b a_0(u)\). Univariate Bezout coefficients for \(a_0,b_0\)
produce a polynomial \(H\in\ker E\cap\ker D\) such that
\[
a=H a_0(u),\qquad b=H b_0(u).
\tag{17}
\]
For example, if \(Aa_0+Bb_0=1\), take \(H=A(u)a+B(u)b\).
No factorial closure of \(\mathbb C[u]\) or coordinate hypothesis
on \(u\) is needed.

Define
\[
R=a_0K_3+b_0K_4
=\frac{mQ}{\Delta}(K_3'K_4-K_4'K_3)\ne0.
\tag{18}
\]
Thus the preceding bad vector really rotates projectively:
\(K_3'K_4-K_4'K_3\ne0\). Let
\[
e=\gcd(Q,R),\qquad Q_1=Q/e,\quad R_1=R/e.
\tag{19}
\]
The relation \(r=H R_1(u)/Q_1(u)\) is polynomial on the original
ring. Bezout for the coprime pair \(Q_1,R_1\) forces
\(H=Q_1(u)H_1\) with \(H_1\in\ker E\cap\ker D\). Explicitly,
if \(AQ_1+BR_1=1\), take \(H_1=A(u)H+B(u)r\).
Consequently the all-degree normal form is
\[
\boxed{\quad
a=H_1Q_1(u)a_0(u),\qquad
b=H_1Q_1(u)b_0(u),\qquad
r=H_1R_1(u).
\quad}
\tag{20}
\]
All multiplicities in the potential denominator are retained.
Moreover the multiplier ideal is exactly
\[
(a,b,r)=H_1B.
\tag{21}
\]
Indeed the univariate weights \(Q_1a_0,Q_1b_0,R_1\) generate the
unit ideal by two explicit Bezout identities. This principal-ideal
statement is proved, not inferred from a coefficient gcd. The
coefficients of the primitive direction \(D\) itself need not
generate the unit ideal.

## 4. A necessary divisibility test for motion of the parameter

In the rotating alternative, the trace identity (6) becomes
\[
Q'(u)T_cu=\frac{m(m-1)}2 H_1R_1(u)t.
\tag{22}
\]
If \(R_1\) does not divide \(Q'\) in \(\mathbb C[U]\), set
\(R_2=R_1/\gcd(R_1,Q')\). This is nonconstant. Bezout applied to
the reduced pair in (22) implies \(R_2(u)\mid T_cu\).
Therefore \(R_2(u)\) divides its own derivative under the actual
constant-partial LND \(T_c\). The LND divisibility lemma forces
\(T_cR_2(u)=0\), and characteristic zero gives \(T_cu=0\).
Since \(r\ne0\), (22) then also gives \(t=0\). Hence
\[
R_1\nmid Q'\quad\Longrightarrow\quad
T_cu=0,\quad Dz=0.
\tag{23}
\]
Equivalently, parameter motion \(T_cu\ne0\) requires the complete
univariate divisibility \(R_1\mid Q'\), not just support containment.
The converse is not asserted. Even when \(T_cu=0\), (5) has a
nonzero commutator; a new commuting constant partial has not been
produced.

## 5. Transfer of the global repair in the common-power alternative

The common-power alternative admits a precise transfer of the
[global normalizer and repair](quadratic-heisenberg-repair-pass43.md).
Let \(\alpha=(m-1)/2\),
\[
T_\lambda=\lambda_3T_3+\lambda_4T_4,\quad
W=[E,T_\lambda],\quad V=[E,W]=grD\ne0.
\tag{24}
\]
The actual partials \(T_c,T_\lambda\) commute and are independent,
and their inherited adjoint bounds are still two and three.
Equations (5), (14)--(15) give
\(g[E,T_c]=-\alpha V\). The next bad-column identity and the trace
identity give, respectively,
\[
Wg=-\frac{rt}{2g^{m-2}},\qquad
g^{m-1}T_cg=\alpha rt,
\quad\text{hence}\quad
Wg=-\frac{gT_cg}{m-1}.
\tag{25}
\]
These are identities in \(\operatorname{Frac}B\) whose stated
derivatives are polynomial. Also \(Vg=0\).

Suppose \(T_cg=0\). Then \(Wg=0\) and, since \(r\ne0\), \(t=0\).
The actual Laurent conjugation used in the linked proof applies to
\(gT_c+2\alpha vT_\lambda\), with external invariant parameter \(v\).
It proves that
\[
Y=gT_c+2\alpha W
\tag{26}
\]
is a global polynomial LND with
\([E,Y]=\alpha V\) and \([Y,V]=[E,V]=0\). This argument needs
\(V\ne0\), established in (24), not independence of the original
two defects.

For the actual \(\tau\) in (7), now \(E\tau=g^m\) and
\(V\tau=grt=0\). Thus the compatible local slice and centralizer
lemma give the global polynomial LND
\[
\mathcal R=g^mY-\alpha\tau V-(Y\tau)E,
\qquad [E,\mathcal R]=[V,\mathcal R]=0,
\qquad \mathcal Rg=0.
\tag{27}
\]
Every localization in this construction inverts the common invariant
\(g\); the explicit replica is polynomial before it is restricted
back to \(B\).

If \(\operatorname{rank}(E,Y,D)=3\), the commuting triple
\(E,V,\mathcal R\) has rank three. It fixes the nonconstant \(g\)
omitting the actual constant direction \(T_c\). The
[commuting coordinate-descent criterion](commuting-coordinate-descent-pass43.md)
therefore recognizes an invariant ambient coordinate and
\(\ker E=\mathbb C^{[3]}\). Its surface cancellation and
three-variable general-fiber inputs are the established theorems
specified in that proof.

If \(T_cg\) is a nonzero complex constant, \(g\) itself is already
a triangular ambient coordinate, since \(T_c\) is an actual constant
partial. That branch is recognized as well. No conclusion is asserted
for nonconstant \(T_cg\), or for the remaining rank-two case of
(26)--(27). The rotating alternative has not been converted into
this common-power repair.

## Verification and source scope

The new rank and weighted-curve arguments use the actual companion
identities, not arbitrary nilpotent matrices as polynomial actions.
The curve-factorization input is applied only after (9) proves its
transcendence-degree hypothesis. Its parameter need not be a
coordinate. The transferred repair invokes the already audited
global polynomial construction, with every formerly relevant
nonvanishing and slice condition rechecked in (24)--(27).

The standalone [five-method checker](dependent_preceding_curve_checks_pass44.py)
imports only `unittest` and SymPy. Its first run passed all five methods
in 0.537 seconds. It checks the new stacked-row ranks in an actual cubic
frame, both permitted formal Jordan partitions, repeated-factor rotating
data with explicit ideal certificates, common-power data with variable
multipliers, and the surviving pole in a failed parameter-motion test.
The actual cubic model has \(r=0\); the separate nonzero-\(r\) curve
data are explicitly formal controls rather than original actions.
No full original action in the unresolved
rotating or nonzero-\(r\) branch is asserted to have been constructed.
Neither (20) nor (23) is sufficient for realizability. The supplied
two-quadratic configuration and arbitrary complex threefold
cancellation remain unresolved. No novelty, expert review or formal
proof-assistant verification is claimed.

[^curve]: Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 and its proof, and Lemma 3.3, PDF pp. 20--21. The exact statement applies to a transcendence-degree-one subalgebra of a polynomial ring over a field and places its normalization in a polynomial parameter algebra inside that original ring. The theorem and proof were directly reread; no ambient-coordinate conclusion is included in that input.
