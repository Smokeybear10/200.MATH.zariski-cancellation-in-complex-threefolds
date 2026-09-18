# Height nine: mixed commutators and the remaining frame problem

Historical checkpoint: the gaps recorded below are closed under the
slice hypothesis by [the completed pass-thirteen argument](../deep-pass-13.md).
The identities and negative controls here remain part of that proof.

The pattern \((1,1,1,2)\) is not closed by this pass. There are exact
commutator and flow identities, and several proved closing subcases,
including the case where the displayed derivation is nice. The remaining
step is not supplied by an ordinary polynomial-degree bound or by
assuming independence of the leading fields.

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=K[s],\qquad E(s)=1,
\]
and put \(T_i=\partial_{x_i}\). The height-nine assumptions imply
\[
\operatorname{ad}_E^2(T_i)=0\quad(i\le3),
\qquad \operatorname{ad}_E^3(T_4)=0.
\tag{1}
\]
For the genuine pattern, the respective last nonzero brackets do not
vanish. The three-dimensional constant space
\(G=\operatorname{span}_{\mathbb C}\{T_1,T_2,T_3\}\) consists of
directions satisfying the double-bracket identity.

## 1. The certified commuting LNDs

Define
\[
W_i=[E,T_i]\quad(1\le i\le4),\qquad V=[E,W_4].
\]
Conjugation by the flow gives
\[
\exp(tE)T_i\exp(-tE)=T_i+tW_i\quad(i\le3),
\]
\[
\exp(tE)T_4\exp(-tE)=T_4+tW_4+\frac{t^2}{2}V.
\tag{2}
\]
Each conjugate is an LND on \(B[t]\), fixing \(t\). Its highest
coefficient is an LND, by taking the highest power of \(t\) in its
iterates. Therefore \(W_1,W_2,W_3,V\) are LNDs, with zero allowed.
This argument does not certify the middle coefficient \(W_4\).

Applying powers of \(\operatorname{ad}_E\) to \([T_i,T_j]=0\) gives
\[
[E,W_i]=[E,V]=0,\quad [W_i,W_j]=[W_i,V]=0
\qquad(i,j\le3).
\tag{3}
\]
The mixed identities, including their factors and signs, are
\[
[T_i,W_4]=[T_4,W_i],
\qquad [T_i,V]+2[W_i,W_4]=0\quad(i\le3).
\tag{4}
\]
In particular \([T_i,V]\) commutes with \(E\), by Jacobi and (3).
It is not automatically an LND. The same caution applies to
\([W_4,V]\), although that bracket also commutes with \(E\).

Thus \(E,W_1,W_2,W_3,V\) are a certified commuting family. Their
generic rank need not be four; the controls below have rank two.

## 2. A rank-one defect in the Riccati equation

Let \(P=(E(x_i))_i\), \(J=\operatorname{Jac}P\), and \(v=(V(x_i))_i\).
All coefficient vectors are columns. With \(e_4^{\mathsf T}=(0,0,0,1)\),
put \(R=v e_4^{\mathsf T}\). Then (1) gives
\[
E(J)=J^2-R,\qquad E(v)=Jv.
\tag{5}
\]
The first three columns satisfy the old Riccati identity, but the fourth
has the defect \(-v\). The second equation says \([E,V]=0\); it does
not say that the individual coefficients of \(V\) are \(E\)-invariant.

Unlike the all-double-bracket case, (5) does not directly give
\(E^r(J)=r!J^{r+1}\). No nilpotence assertion for \(J\) is made here.
For example, the first coefficient of the determinant identity below
gives \(\operatorname{tr}J=0\), and its quadratic coefficient gives
\[
v_4=\operatorname{tr}(J^2),
\]
not a vanishing statement for either side.

Let \(F_t=\exp(tE)x\). The coefficient matrix of the conjugated partials
in (2) is
\[
C(t)=I-tJ+\frac{t^2}{2}R.
\tag{6}
\]
Applying those partials to \(F_t\) shows, with the indicated column
convention,
\[
\operatorname{Jac}(F_t)C(t)=I,
\qquad C(t)=\operatorname{Jac}(F_t)^{-1}.
\tag{7}
\]
Since the polynomial flow has Jacobian determinant one,
\(\det C(t)=1\), and \(\operatorname{Jac}(F_t)=\operatorname{adj}C(t)\).

Only the fourth column of \(C(t)\) can be quadratic in \(t\); the other
columns are linear. Every cofactor therefore has degree at most four.
Consequently
\[
E^5(x_i)\in\mathbb C,\qquad E^6(x_i)=0\quad(1\le i\le4).
\tag{8}
\]
This is a bound of five on flow time-degree, not on ordinary total degree.

There is a useful directional improvement. Entry \((4,j)\) of the
inverse matrix is the cofactor deleting row \(j\) and column four.
Only linear columns remain, so the fourth row of the inverse has degree
at most three. Hence
\[
k:=E^4(x_4)\in\mathbb C,
\qquad E^5(x_4)=0.
\tag{9}
\]
If \(c=E^5(x)\in\mathbb C^4\), then \(c_4=0\), so the constant
derivation \(T_c=c\cdot\partial\) belongs to \(G\).

There is also a rank bound for the fourth iterate. Write \(J_i\) for
column \(i\) of \(J\), and set
\[
L=(-J_1,-J_2,-J_3,v/2).
\]
Its determinant is the coefficient of \(t^5\) in \(\det C(t)=1\),
so \(\det L=0\). The weighted leading cofactor computation gives
\[
[t^4]\operatorname{adj}C(t)
=\operatorname{diag}(1,1,1,0)\operatorname{adj}L.
\]
Indeed, inverse row \(i\le3\) deletes a linear column and can have
degree four; inverse row four deletes the quadratic column and has
degree at most three. A singular four-by-four matrix has adjugate of
rank at most one, over the fraction field. Comparing with the flow
Jacobian in (7) therefore proves
\[
\operatorname{rank}\operatorname{Jac}(E^4x)\le1.
\tag{9a}
\]

## 3. The highest constants and the fourth-column defect

The flow identity
\[
C(t)P(F_t)=P(x)
\]
follows from (7) and \(P(F_t)=\operatorname{Jac}(F_t)P(x)\).
Since
\(P(F_t)=\sum_{r=0}^4 t^r E^{r+1}(x)/r!\), its coefficient of
\(t^5\), together with (9), yields
\[
Jc=2k v,
\qquad [E,T_c]=-2kV.
\tag{10}
\]

This proves a closing subcase: if \(k=0\) and \(c\ne0\), then
\(T_c\) is a nonzero constant translation commuting with \(E\).
Section 4 explains why that suffices. If \(k\ne0\) but \(c=0\),
equation (10) forces \(V=0\), also a closed subcase.

In the remaining case \(k\ne0\), \(c\ne0\), equation (10) does not
make \(T_c\) commute with \(E\). A nonzero highest constant vector
must not be treated as a commuting translation without this check.

For later use put \(h_r=E^r(x)\). The coefficient of \(t^4\) in
\(C(t)P(F_t)=P(x)\), and that of \(t^5\) in
\(C(t)\operatorname{Jac}(F_t)=I\), respectively give
\[
Jh_4=\frac c4+\frac32v(h_3)_4,
\qquad
J\operatorname{Jac}h_4=2v\operatorname{Jac}((h_3)_4).
\tag{10a}
\]
Here the second Jacobian on the right is a row vector.

When \(k\ne0\) and \(V\ne0\), (10) forces \(c\ne0\).
Equations (9a) and \(E(h_4)=c\) imply that the image closure of
\(h_4\) is an irreducible curve stable under translation by \(c\).
It contains an affine line through each image point, and hence is one
affine line. Thus \(h_4=ca+d\) for a polynomial \(a\), a constant
vector \(d\), and \(E(a)=1\). Substitution in (10a), followed by
\(Jc=2kv\), shows
\(\operatorname{Jac}((h_3)_4-ka)=0\). Consequently
\[
h_4=cs_0+d',\qquad s_0=(h_3)_4/k,\qquad
d'\in\mathbb C^4,\quad d'_4=k.
\tag{10b}
\]
This identifies an affine-line image and a polynomial slice. It does
not prove that the slice \(s_0\) is an ambient coordinate.

## 4. Proved closing subcases

If \(V=0\), all four double brackets vanish, so the theorem in
[height-eight-algebra-pass.md](height-eight-algebra-pass.md) applies.

Any nonzero constant translation commuting with \(E\) also suffices.
After a linear coordinate change it is a coordinate partial, whose
kernel is a polynomial three-ring preserved by \(E\). There is a
direction in \(G\) independent of that translation. It descends to a
nonzero constant coordinate direction on this three-ring and still
satisfies the double-bracket identity. The three-variable lemma in
[height-seven-audit.md](height-seven-audit.md) gives an invariant ambient
coordinate. This applies, for example, when \(V\) is a nonzero constant
field, or when a known constant linear combination of the commuting
fields is a nonzero constant field.

If the family \(E,W_1,W_2,W_3,V\) has generic rank four, its additive
group action has an open orbit. The orbit is also closed because
unipotent orbits on affine varieties are closed. Thus it is transitive;
the quotient of the acting vector group by its stabilizer identifies
\(B\) with a polynomial ring in which \(E\) is a translation. This is
the same full-rank criterion used in
[height-seven-audit.md, Section 5](height-seven-audit.md).

There is a separate useful algebraic subcase. Suppose \(E\) is nice in
the displayed frame, meaning
\[
E^2(x_i)=0\quad\text{for every }i.
\]
Then \(JP=0\), and differentiating this identity gives
\(E(J)=-J^2\). Comparing its first three columns with (5) gives
\[
J^2=w e_4^{\mathsf T}
\]
for a polynomial column \(w\). Multiplication by \(P\) gives
\[
0=J^2P=wP_4.
\]
If \(w=0\), then \(E(J)=J^2=0\), so all four double brackets vanish.
If \(w\ne0\), the domain property gives \(P_4=E(x_4)=0\), an invariant
ambient coordinate. Therefore the nice subcase closes. This argument
does not need the fourth triple-bracket assumption.

A further higher-iterate subcase closes when
\[
c=E^5(x)=0,\qquad E^3(x_4)=0,\qquad h=E^4(x)\ne0.
\tag{10c}
\]
Then \(k=0\), \(E(h)=0\), and (9a), (10a) give
\[
\operatorname{rank}\operatorname{Jac}h\le1,\qquad
Jh=0,\qquad J\operatorname{Jac}h=0.
\]
Set \(H=h\cdot\partial\). First,
\([E,H]=E(h)-Jh=0\). Commutation then gives, componentwise,
\[
H(h)=H(E^4x)=E^4(Hx)=E^4h=0.
\]
Thus \(H\) is a nice LND. This argument uses commutation of the
derivations \(E,H\); it does not treat the operator \(E^4\) as a
derivation.

If \(h\) is constant, it supplies a nonzero constant commuting
translation. Otherwise its Jacobian rank is one, and
[de Bondt, Theorem 5.5](https://arxiv.org/pdf/1501.05168) gives the
normal form used in
[height-eight-algebra-pass.md, Section 3](height-eight-algebra-pass.md).
All three image-span cases still close here. A one-dimensional image
span gives \(h=g v\) and \(Jv=0\), so the constant-translation
argument above applies. A three-dimensional image span makes the
components polynomials in one linear coordinate; \(E(h)=0\) fixes
that coordinate. For a two-dimensional image span, the vectors \(h\)
and a suitable partial derivative of \(h\) span a constant plane over
the fraction field. The two identities \(Jh=J\operatorname{Jac}h=0\)
make \(E\) commute with both constant directions in this plane.
It therefore preserves the complementary polynomial two-ring, where
Rentschler supplies an invariant coordinate if the restriction is
nonzero. Only the constant-translation case needs a surviving good
direction; the three-dimensional space \(G\) supplies one after
quotienting by that translation.

For each invariant-coordinate closure above, regularity of \(K\)
descends from \(K[s]\), and
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
then gives \(K=\mathbb C^{[3]}\). Alternatively, if \(E(x_4)\) is a
nonzero constant, \(x_4/E(x_4)\) is already a coordinate slice and its
polynomial quotient identifies the kernel directly.

## 5. The corrected fourth field is not yet a corrected frame

Suppose \(k\ne0\), and set
\[
s_0=\frac{E^3(x_4)}{k},\qquad E(s_0)=1.
\]
Equation (10) gives the exact polynomial correction
\[
Q=T_4+\frac{s_0}{4k}T_c,
\qquad \operatorname{ad}_E^2(Q)=0.
\tag{11}
\]
Indeed \(\operatorname{ad}_E^2(s_0T_c)=2[E,T_c]=-4kV\).
Polynomiality of \(Q\) and its double-bracket identity do not certify
that it is an LND or a coordinate partial.

Applying the conjugated fields in (2) to \(F_t(x_4)\), and comparing
the highest coefficients, gives the additional relations
\[
V(s_0)=0,
\qquad T_c(s_0)=6V(E^2(x_4))=-4kW_4(s_0).
\tag{12}
\]
These do not currently prove \(T_c(s_0)=0\).
For each \(i\le3\), the coefficient of \(t^4\) in
\((T_i+tW_i)F_t(x_4)=0\) also gives
\[
W_i(s_0)=E(T_i(s_0))=0.
\tag{12a}
\]
These additional invariant coefficients do not by themselves certify
the corrected field as part of a suitable coordinate frame.

Even assuming that extra vanishing needs care. Since \(c_4=0\), one
can choose linear coordinates with \(T_c=\partial_y\) while retaining
\(u=x_4\). If \(T_c(s_0)=0\), the coefficient of \(\partial_y\) in
\(Q\) is independent of \(y\). Integrating it polynomially with respect
to \(u\) makes \(Q\) a triangular coordinate partial. However, the other
good partials satisfy
\[
[T_i,Q]=\frac{T_i(s_0)}{4k}T_c\qquad(i\le3),
\tag{13}
\]
so they need not remain a commuting frame with \(Q\). Completing the
coordinate shear changes those partials too, and their new double-bracket
identities have not been established. Thus (11) is a derivation-level
correction, not a height-eight frame certificate.

## 6. Exact controls and scope of the computation

For a middle-coefficient warning, use physical coordinates \((a,b,c,d)\)
and put \(f=a+bd\). The derivation
\[
E=-df\partial_a+f\partial_b+\partial_c
\]
is nice and has slice \(c\). Its first three coordinate partials satisfy
the double-bracket identity, and its fourth satisfies the triple-bracket
identity. But
\[
W_4=(a+2bd)\partial_a-b\partial_b
\]
is not locally nilpotent, since \(W_4(b)=-b\). Meanwhile
\[
V=2df\partial_a-2f\partial_b=-2(E-\partial_c)
\]
is a commuting LND. The linear coordinate frame \((a-c,b,c,d)\) has
degrees exactly \((1,1,1,2)\). The certified commuting family has generic
rank two, not four. This example is in the proved nice subcase because
\(E(d)=0\).

A different triangular control is
\[
E=(c+2d^3/3)\partial_b+d^2\partial_c+\partial_d.
\]
Here \(V=-2d\partial_b-2\partial_c\) is nonconstant, and
\(E^4(b)=6\), so time-degree four genuinely occurs under (1).
The linear frame \((c-a-b,a,b,d)\) has degrees \((1,1,1,2)\).
It closes directly because \(d\) is a coordinate slice; it is not
evidence that an arbitrary fourth-order slice expression is a coordinate.

An inline SymPy calculation, run with \(/opt/anaconda3/bin/python\),
passed 16 exact assertions on these two controls. It checked the
commutator relations, the defect sign in (5), \(\det C(t)=1\), the
inverse-Jacobian orientation in (7), the displayed middle and highest
coefficients, and both exact filtration-degree profiles. No new test
suite file was created. The identities involving general \(k,c\) were
proved by the coefficient comparisons above, not claimed as verified by
these controls, which have \(k=c=0\).

The separate
[height-nine-first-audit.md](height-nine-first-audit.md) independently
checks equations (5)--(13), the weighted rank bound (9a), and the
additional invariant-coefficient relation (12a).

## 7. Precise remaining branch

After these closures, a residual height-nine case must be non-nice,
have \(V\ne0\), have certified commuting rank at most three, and have
no obtained constant translation commuting with \(E\). The highest
constants split into two unclosed possibilities:

- \(k=0\) and \(c=0\), so the full flow has time-degree at most four
  and its fourth coordinate has time-degree at most three. In view of
  (10c), it must also satisfy \(E^3(x_4)\ne0\) or \(E^4(x)=0\);
- \(k\ne0\) and \(c\ne0\), with \(Jc=2kv\), where the correction
  (11) has not been promoted to an appropriate polynomial coordinate frame.
  The affine-line description (10b) supplies a slice, not a proof that
  this slice is an ambient coordinate.

These are necessary conditions for an unclosed case, not examples of
nonpolynomial kernels. The established universal height threshold remains
\(H\le8\); this note does not raise it to nine.
