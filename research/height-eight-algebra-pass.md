# The height-eight double-commutator closure

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), and let \(E\) be a locally
nilpotent derivation satisfying

\[
[E,[E,\partial_{x_i}]]=0\qquad(1\le i\le4).
\tag{1}
\]

Then \(\ker E\) contains an ambient polynomial coordinate. If in addition
\(E\) has a slice, its kernel is \(\mathbb C^{[3]}\). In particular the
remaining height-eight pattern \((1,1,1,1)\) closes. This is a bounded
commutator criterion, not a proof that every slice action admits such a
coordinate frame.

The proof combines exact differential identities, the three-variable
single-partial lemma from [height-seven-audit.md](height-seven-audit.md),
and two quasi-translation results of de Bondt. Its last step is the
cone-preserving homogenization argument developed independently in the
main pass. No classification by ordinary polynomial degree is used.

## 1. Riccati identities and the highest nonzero iterate

Write \(P=(E(x_i))_i\) as a column vector and
\(J=\operatorname{Jac}P=(\partial_jP_i)_{i,j}\). The coefficient vector
of \(W_j=[E,\partial_j]\) is minus column \(j\) of \(J\), and

\[
[E,W_j]=0\quad\Longleftrightarrow\quad E(J)=J^2.
\tag{2}
\]

Induction gives \(E^r(J)=r!J^{r+1}\). Since \(E\) is locally nilpotent
on the finitely many entries of \(J\), this matrix is nilpotent. Over
\(\operatorname{Frac}B\), a nilpotent four-by-four matrix has fourth
power zero; consequently

\[
J^4=0.
\tag{3}
\]

Put \(h_r=E^r(x)\). For every \(r\ge1\), direct induction gives

\[
h_r=(r-1)!J^{r-1}P,
\qquad
\operatorname{Jac}h_r=r!J^r.
\tag{4}
\]

For the second identity, differentiation of a vector \(v\) obeys
\(\operatorname{Jac}(Ev)=E(\operatorname{Jac}v)
+(\operatorname{Jac}v)J\). Equation (2) then proves (4), including its
factorials. In particular \(h_4\) is constant and \(h_5=0\).

If \(E=0\), every coordinate is invariant. Otherwise let
\(m\in\{1,2,3,4\}\) be maximal with \(h_m\ne0\), and set \(h=h_m\).
Equations (3) and (4) imply

\[
E(h)=0,\qquad Jh=0,\qquad J\operatorname{Jac}h=0.
\tag{5}
\]

Indeed \(Jh=h_{m+1}/m=0\), and differentiating \(h_{m+1}=0\) gives
\(J^{m+1}=0\). The derivation \(V_h=\sum h_i\partial_i\) is a
quasi-translation derivation: \((\operatorname{Jac}h)h=0\), so
\(V_h^2(x_i)=0\) for all generators. This condition itself makes
\(V_h\) locally nilpotent, since its generator images are invariant.
Also \([E,V_h]=E(h)-Jh=0\).

If \(m\ge2\), then \(\operatorname{rank}\operatorname{Jac}h\le1\).
For \(m=4\) it is zero. For \(m=3\), a nilpotent four-by-four matrix
has \(\operatorname{rank}J^3\le1\). For \(m=2\), equation (4) and
\(h_3=0\) give \(J^3=0\); its possible Jordan blocks then imply
\(\operatorname{rank}J^2\le1\). The remaining case \(m=1\) is exactly

\[
EP=JP=0,\qquad J^2=0,\qquad \operatorname{rank}J\le2.
\tag{6}
\]

The flow has time-degree at most four, and its Jacobian is

\[
\operatorname{Jac}(\exp(tE)x)
=I+tJ+t^2J^2+t^3J^3=(I-tJ)^{-1}.
\tag{7}
\]

These are time-degree statements. They place no uniform bound on the
ordinary total degree of the coefficients of \(E\).

## 2. A constant commuting translation closes

Suppose \(v\in\mathbb C^4\setminus\{0\}\) satisfies \(Jv=0\).
The constant derivation \(V=v\cdot\partial\) commutes with \(E\).
After a linear coordinate change, \(V=\partial_4\), so \(E\) preserves
the polynomial three-ring \(R=\mathbb C[x_1,x_2,x_3]\).

Identity (1) is preserved by linear coordinate changes: every new
coordinate partial is a constant linear combination of the old ones.
It restricts to \(R\). The single-partial lemma therefore supplies a
coordinate of \(R\) invariant under \(E|_R\), including the case of a
zero restriction. That coordinate is ambient in \(B\).

This closes any branch in which the highest nonzero iterate \(h\) is a
constant vector. It is more than the observation that a nonzero
\(E^4(x_i)\) displays a slice, which was already assumed in the
cancellation application.

## 3. Every rank-one highest-iterate branch closes

Suppose \(\operatorname{rank}\operatorname{Jac}h=1\).
[De Bondt, Theorem 5.5](https://arxiv.org/pdf/1501.05168) gives the
following exact nonhomogeneous statement: after linear coordinates,

\[
h=(0,\ldots,0,h_{s+1},\ldots,h_4),\qquad
h_i\in\mathbb C[x_1,\ldots,x_s],
\tag{8}
\]

where \(s\ge1\), and the \(4-s\) nonzero components are linearly
independent over \(\mathbb C\). There are three cases.

If the image of \(h\) spans a line, then \(h=g v\) for a nonzero
constant vector \(v\). Equation \(Jh=0\) gives \(Jv=0\), so Section 2
applies.

If its image spans a three-dimensional space, then \(s=1\). Some
\(h_i\in\mathbb C[x_1]\) is nonconstant, since the Jacobian rank is one.
The identity \(E(h_i)=h_i'(x_1)E(x_1)=0\) implies \(E(x_1)=0\).
Thus an invariant linear coordinate is already present.

If its image spans a plane, then
\(h=(0,0,h_3(x_1,x_2),h_4(x_1,x_2))\). Linear independence gives an
index \(j\in\{1,2\}\) with

\[
h_3\partial_jh_4-h_4\partial_jh_3\ne0.
\tag{9}
\]

Otherwise \(h_3/h_4\) would be a constant rational function. Therefore
\(h\) and \(\partial_jh\) span the constant \(e_3,e_4\) plane over
\(\operatorname{Frac}B\). Equation (5) says that \(J\) kills both
vectors, so its third and fourth columns vanish identically. Hence
\(E\) preserves \(\mathbb C[x_1,x_2]\). A zero restriction fixes
\(x_1\); a nonzero restriction fixes a plane coordinate by Rentschler.
Again that coordinate is ambient in \(B\).

This proof requires neither a polynomial Luroth generator nor an
extension of the homogeneous rank-two theorem to nonhomogeneous maps.
It closes all \(m\ge2\) branches and the rank-one part of \(m=1\).

## 4. The rank-two nice branch has a conical image

It remains to treat (6) with \(\operatorname{rank}J=2\). Set
\(S=\overline{P(\mathbb A^4)}\subseteq\mathbb A^4\), an irreducible
surface. Over \(\operatorname{Frac}B\), the square-zero condition gives

\[
\operatorname{im}J=\ker J.
\]

Since \(JP=0\), there is a rational vector \(v\) with \(P=Jv\).
For every polynomial relation \(R(P)=0\), differentiation gives
\((\nabla R)(P)J=0\), hence

\[
(\mathcal E R)(P)=(\nabla R)(P)P=0,
\qquad \mathcal E=\sum_i y_i\partial_{y_i}.
\tag{10}
\]

Thus the prime relation ideal \(I(S)\) is stable under the target Euler
derivation. On a polynomial with finitely many homogeneous components,
polynomial interpolation in \(\mathcal E\) isolates each component,
because their degrees are distinct eigenvalues in characteristic zero.
Every homogeneous component of every element of \(I(S)\) therefore lies
in \(I(S)\). The ideal is homogeneous, and \(S\) is a cone.

This argument establishes a property of the image closure. It does not
claim that the actual image contains the cone vertex or every point of
each ray.

## 5. Cone-preserving homogenization closes the residual

Let \(d=\max_i\deg P_i\) and introduce a fifth variable \(t\). Define

\[
\widetilde P(x,t)=\bigl(t^dP(x/t),0\bigr).
\tag{11}
\]

This is a homogeneous polynomial vector. The quasi-translation
homogenization statement is
[de Bondt, Proposition 5.1](https://arxiv.org/pdf/1501.05168); directly,
the last component is zero and \(JP=0\) gives
\((\operatorname{Jac}\widetilde P)\widetilde P=0\).

The important rank check is exact. For \(t\ne0\), the value in (11)
lies in \(S\times\{0\}\), since \(S\) is a cone. Polynomial equations
for this closed set then imply the same containment at \(t=0\).
Conversely \(t=1\) recovers \((P(x),0)\), whose image is dense in
\(S\times\{0\}\). Consequently

\[
\overline{\widetilde P(\mathbb A^5)}=S\times\{0\},
\qquad \operatorname{rank}\operatorname{Jac}\widetilde P=2.
\tag{12}
\]

Ordinary homogenization can increase this rank; the conical image is
what prevents that increase here.

Now apply the homogeneous rank-two quasi-translation theorem
[de Bondt, Theorem 5.3, attributed to Gordan and Nother](https://arxiv.org/pdf/1501.05168).
In dimension five the linear span of the image has dimension at most
\(5-2=3\). Equation (12) makes this exactly the dimension of the linear
span of \(S\) in the original four-space. There is therefore a nonzero
constant row \(\lambda\in\mathbb C^4\) with

\[
\lambda P=0.
\]

The linear polynomial \(\lambda x\) is an invariant ambient coordinate.
This proves the claim at the start of the note. Neither primitivity of
\(P\) nor a slice was needed for this algebraic step.

## 6. Kernel recognition and the height consequence

For the cancellation application, \(E(s)=1\) and \(B=K[s]\).
The kernel \(K\) is regular by descent from its regular polynomial
extension. Once the invariant ambient coordinate \(p\) is found,
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies to the nonzero \(\mathbb C[p]\)-linear LND of
\(\mathbb C[p]^{[3]}\), giving \(K=\mathbb C[p]^{[2]}\).

The previous height criteria already closed degrees \(-1\), two degree
zeros, and a pair of degrees zero and one. The only remaining pattern
at height eight was \((1,1,1,1)\), for which the filtration bounds imply
(1). Therefore

\[
H\le8\ \Longrightarrow\ K\simeq\mathbb C^{[3]},
\qquad
K\not\simeq\mathbb C^{[3]}\ \Longrightarrow\ H_{\min}\ge9.
\tag{13}
\]

No claim is made for the height-nine pattern \((1,1,1,2)\), or for an
arbitrary slice derivation without the double-commutator condition.

## 7. Exact positive and negative controls

The triangular derivation
\[
E=\partial_a+a\partial_b+(b+a^2/2)\partial_c
 +(c+ab+a^3/6)\partial_d
\]
satisfies (1) and has \(E^4(d)=6\). It verifies that the fourth time
degree can genuinely occur; the constant commuting direction is
\(6\partial_d\).

For every integer \(N\ge1\), another control is
\[
E_N=a^N\partial_c+(a^Nb-1)\partial_d.
\]
It is nice, has square-zero Jacobian of generic rank two, and has slice
\(s=bc-d\). With \(u=(a^Nb-1)c-a^Nd\), its exact inverse presentation is
\[
c=a^Ns-u,\qquad d=(a^Nb-1)s-bu,
\qquad K=\mathbb C[a,b,u].
\]
Thus ordinary coefficient degrees are unbounded in this class. For
\(N=1\), the linear frame \((a-c,b-d,c,d)\) has all four degrees equal
to one, while \(E,W_1,\ldots,W_4\) have generic rank only two and the
intrinsic leading fields have rank one. This defeats a full-orbit-rank
shortcut even in an actual height-eight frame.

The coefficient image \((a,b)\mapsto(a,ab-1)\) misses the origin of its
plane-cone closure. Thus the cone step cannot be replaced by an assertion
that a unimodular coefficient map hits its vertex.

For a negative control, put \(f=a+bd-c^2\) and
\[
Q=(-d+2cf-bf^2,1,f,f^2).
\]
Then \(Q\cdot\partial\) is a nice LND with slice \(b\), but its
Jacobian has nonzero square. This primitive version of
[de Bondt, Example 4.3](https://arxiv.org/pdf/1501.05168) is not covered
by (1). Conversely the map
\(H=(0,a^2,a^3,3ba^2-2ca)\) has square-zero Jacobian, but
\((\operatorname{Jac}H)H=(0,0,0,a^4)\ne0\) and fails (2). It is the
ordinary-versus-strong-nilpotence control in
[de Bondt, Section 2 after Proposition 2.3](https://arxiv.org/pdf/1203.6615).
Neither square-zero Jacobian alone nor nice-with-a-slice alone substitutes
for the exact hypotheses used above.

The independent script
[height_eight_algebra_checks.py](height_eight_algebra_checks.py) uses
SymPy and the standard library, with no research-module imports. Run

    /opt/anaconda3/bin/python research/height_eight_algebra_checks.py

All seven tests passed. They verify these identities, coordinate inverses, filtration
degrees, and the explicit homogenization rank. They do not replace the
proof of the general theorem or computationally certify the cited
homogeneous quasi-translation theorem.
