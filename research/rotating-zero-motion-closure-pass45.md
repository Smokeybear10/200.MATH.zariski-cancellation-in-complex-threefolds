# The dependent zero-motion branch has an invariant coordinate

The remaining rank-two good-top case is recognized when the actual
highest constant direction kills the preceding curve parameter. The
mixed coordinate-column identities put the parameter's whole ordinary
gradient in the common invariant ring. Either that gradient algebra is
a curve, giving an invariant linear coordinate, or it forces descent
to an actual three-variable ring with a kernel-preserving coordinate
partial. Primitive leading-coefficient division then reduces the latter
case to the established affine-plane theorem.

This closes the zero-motion branch specified below, not every dependent
defect, every supplied two-quadratic frame, or unrestricted cancellation.
No realization of the previously unresolved high-flow branch is required
or asserted by this conditional theorem.

## 1. Precise original hypotheses and conclusion

Retain the actual hypotheses of
[the preceding-curve normal form](dependent-preceding-curve-pass44.md).
Thus \(B=\mathbb C[x_1,x_2,x_3,x_4]\), the LND \(E\) has an
original polynomial slice, and \(T_i=\partial_{x_i}\) satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_3=
\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Write \(W_i=[E,T_i]\), \(V_i=[E,W_i]\). The dependent
quadratic defects have the primitive form
\[
V_3=aD,\quad V_4=bD,\quad [E,D]=0,
\qquad a,b\in\ker E\cap\ker D,
\tag{2}
\]
with \(D\) a nonzero polynomial LND and \(a,b\) complex-linearly
independent. The nonconstant highest vector and preceding layer give
\[
E^mx=cq,\quad z=E^{m-1}x,\quad q=Q(u),\quad \deg Q>0,
\quad m\in\{3,4\},\quad c_3=c_4=0,
\tag{3}
\]
where \(u\in B\setminus\mathbb C\), \(Eu=Du=0\), and
\[
Dz=ct,\qquad
[E,T_c]=-\alpha rD,\quad
\alpha=(m-1)/2,\quad
T_c=\sum_i c_iT_i\ne0,
\quad r\in\ker E\cap\ker D\setminus\{0\}.
\tag{4}
\]
The original-slice argument already proves that \(E,D\) are
fraction-field independent. Assume
\[
T_cu=0.
\tag{5}
\]

**Theorem.** Under (1)--(5), \(E\) fixes an actual ambient
polynomial coordinate and \(\ker E\simeq\mathbb C^{[3]}\).

The earlier [good-top theorem](dependent-good-top-recognition-pass44.md)
already proves this when \(E,D,W_1,W_2\) have joint rank three.
All these fields kill \(u\), so the only other possible joint rank
is two. The rest of the proof treats precisely that case. Although
the rotating alternative motivated it, the proof uses only (1)--(5)
and therefore also applies to the common-power alternative with
\(T_cu=0\).

## 2. Every ordinary derivative of the parameter is jointly invariant

Put \(C=\ker E\cap\ker D\). The original slice writes
\(B=A[s]\), \(A=\ker E\). Independence makes \(D|_A\)
nonzero, and its local-slice theorem gives
\(\operatorname{trdeg}_{\mathbb C}\operatorname{Frac}C=2\).
This argument needs no polynomial-coordinate presentation of \(C\).

The inherited full trace identity is
\[
T_cq=\frac{m(m-1)}2rt.
\tag{6}
\]
Equations (3),(5) force \(t=0\). The next bad-column identity
\[
V_i z=-\frac2m c\,W_iq\quad(i=3,4)
\tag{7}
\]
therefore gives \(W_3q=W_4q=0\). The highest good-column
identity already gives \(W_1q=W_2q=0\). Since
\(Q'(u)\ne0\), all four \(W_i\) kill \(u\).

Conjugation preserves the commutation of the actual partials.
The coefficient of the first power of the external flow parameter in
the commutator of the conjugated \(T_c\) and \(T_i\) is
\[
[T_c,W_i]+[W_c,T_i]=0,
\qquad W_c=[E,T_c]=-\alpha rD.
\tag{8}
\]
Apply (8) to \(u\). The first term is zero by (5) and
\(W_i u=0\); the second is \(-\alpha rD(T_i u)\).
Hence \(D(T_i u)=0\). Also
\(E(T_i u)=W_i u=0\). Thus the actual polynomial algebra
\[
F=\mathbb C[u,T_1u,T_2u,T_3u,T_4u]
\quad\text{satisfies}\quad F\subseteq C.
\tag{9}
\]
Its transcendence degree is one or two. In addition, the actual
constant partial \(T_c\) kills all of \(F\), since it commutes
with every \(T_i\) and kills \(u\).

The mixed identity is essential here. Merely knowing that the
parameter and its defect multipliers are invariant would not put the
whole gradient in \(C\).

## 3. A one-dimensional gradient algebra gives a linear coordinate

Suppose \(\operatorname{trdeg}F=1\). Apply polynomial curve
factorization to the actual subalgebra in (9). There is
\(v\in B\setminus\mathbb C\) with
\[
\operatorname{Frac}F=\mathbb C(v),\qquad
B\cap\mathbb C(v)=\mathbb C[v],\qquad
u=P(v),\quad T_i u=P_i(v)
\tag{10}
\]
for univariate polynomials, with \(\deg P>0\).[^curve]
Differentiating gives
\[
T_i v=\frac{P_i(v)}{P'(v)}\in
B\cap\mathbb C(v)=\mathbb C[v].
\tag{11}
\]
Since each \(T_i\) is an actual LND, its restriction to the
stable one-variable ring \(\mathbb C[v]\) is an LND. A polynomial
derivation \(H(v)\partial_v\) is locally nilpotent only when
\(H\) is constant: for positive degree its nonzero iterates on
\(v\) retain a nonzero leading term. Consequently all four
ordinary derivatives of \(v\) are complex constants.

Thus \(v\) is a nonconstant affine-linear polynomial, hence an
actual ambient coordinate. The equality \(u=P(v)\) and
\(Eu=0\) give \(Ev=0\). This proves the required invariant
coordinate in the one-dimensional case. It does not require the
original \(u\) itself to be a coordinate.

## 4. A two-dimensional gradient algebra descends the other good partial

Suppose \(\operatorname{trdeg}F=2\). Since \(F\subseteq C\)
and both fraction fields have transcendence degree two,
\(\operatorname{Frac}C\) is algebraic over \(\operatorname{Frac}F\).
The derivation \(T_c\) kills the latter field. Characteristic zero
and the minimal-polynomial derivative show that it kills every
algebraic element of the former. Hence
\[
T_c(C)=0.
\tag{12}
\]
This conclusion did not presume that \(C\) was contained in a
three-variable coordinate ring.

Make an actual constant linear change in the good plane. Write
\[
B=R_0[a],\quad R_0=\mathbb C[b,y,z],\quad
T_c=\partial_a,\quad S=\partial_b,
\tag{13}
\]
where \(S\) is the other good constant partial, and \(y,z\)
are the original bad coordinates. Equation (12) now gives
\(C\subset R_0\). Its good top \(W_S=[E,S]\) lies in
the fraction-field span of \(E,D\), by the remaining rank-two
assumption. Thus \(W_S\) kills \(C\).

For \(f\in C\), it follows that
\[
E(Sf)=W_Sf=0,\qquad T_c(Sf)=S(T_cf)=0.
\]
Apply (4) to \(Sf\). Both terms of \([E,T_c](Sf)\) are
zero, so \(rD(Sf)=0\). Consequently
\[
S(C)\subseteq C.
\tag{14}
\]
This is an actual polynomial invariant-ring descent. It uses neither
a rational replacement for \(S\) nor a Jacobian-only coordinate map.

## 5. Extraction on the actual three-ring

The horizontal part of \(E\) with respect to (13) is nonzero.
Otherwise \(E\) is fraction-field parallel to \(T_c\), and
\([E,T_c]\) is parallel to \(E\), contradicting (4) and
independence of \(E,D\).

Let \(d\ge0\) be the largest \(a\)-degree of the coefficients
of \(E(b),E(y),E(z)\), and let \(k=\deg_a E(a)\), allowing
\(k=-\infty\). Give \(a\) weight one and \(R_0\) weight zero.
The highest weighted derivation of an LND is an LND: the initial
form of each sufficiently high iterate is zero, and an earlier drop
of degree already kills the corresponding graded iterate.

If \(k\ge d+1\), this highest derivation has a nonzero value
\(\beta a^k\) on \(a\), with \(\beta\in R_0\setminus\{0\}\).
That value is divisible by \(a\). This is impossible for an LND,
by the divisibility lemma. Thus \(k\le d\), and the actual
highest weighted derivation is
\[
\overline E=a^d L,\qquad
0\ne L\in\operatorname{Der}_{\mathbb C}(R_0),\quad La=0.
\tag{15}
\]
Local nilpotence descends to \(L\), since
\((a^dL)^Nf=a^{dN}L^Nf\). No inversion of a variable has occurred.

Every element of \(C\subset R_0\) is killed by every coefficient
of the polynomial-in-\(a\) identity \(Ef=0\). Hence
\(C\subseteq\ker_{R_0}L\). Both fields have transcendence
degree two. Each member of \(\ker L\) is therefore algebraic
over \(\operatorname{Frac}C\); because \(E,D\) kill that
field, they kill the member as well. We obtain the exact equality
\[
\ker_{R_0}L=C.
\tag{16}
\]
The equality is not inferred from a generic isomorphism of surfaces.

Divide the polynomial coefficient gcd of \(L\) in \(R_0\),
writing \(L=hL_0\). The LND divisibility lemma applied to
\(Lh=hL_0h\) gives \(Lh=0\). Thus \(L_0h=0\), and
\(L^Nf=h^NL_0^Nf\) proves that \(L_0\) is an LND, with
primitive coefficient vector and the same kernel \(C\).

## 6. Kernel-preserving coordinate translation makes the primitive field commute

By (14), \(\Phi_t=\exp(tS)\) is an actual automorphism of
\(R_0[t]\) preserving \(C[t]\) setwise. Here \(t\) is an
external parameter, killed by every derivation. Therefore
\(L_0\) and \(\Phi_tL_0\Phi_t^{-1}\) have the same kernel
\(C[t]\). Two such nonzero LNDs are rationally proportional:
after localizing the common kernel, their fraction field has
transcendence degree one and their derivations are parallel.

Both coefficient vectors are primitive in the actual UFD
\(R_0[t]\). The translated vector remains primitive because an
automorphism and its invertible Jacobian matrix preserve the
coefficient ideal up to that automorphism. Write their rational ratio
in reduced form. Its denominator divides every coefficient of
\(L_0\), and its numerator divides every coefficient of the
conjugate. Both are units. The ratio consequently belongs to
\(R_0[t]^*=\mathbb C^*\), and evaluation at \(t=0\) makes
it one. Differentiation gives
\[
[S,L_0]=0.
\tag{17}
\]
This is the same primitive equal-kernel saturation mechanism used
in the earlier normalizer proofs, now applied on the actual
three-ring. No gcd-one-to-Bezout implication is used.

Since \(S=\partial_b\), every coefficient of \(L_0\) is
independent of \(b\). Its restriction to the actual plane
\(\mathbb C[y,z]\) is an LND. If that restriction is zero,
both \(y,z\) already belong to \(C\). Otherwise the established
plane invariant-coordinate theorem supplies a coordinate
\(v\) of \(\mathbb C[y,z]\) killed by \(L_0\).[^plane]
In either case, (16) gives an actual ambient coordinate in
\(C\subseteq\ker E\).

## 7. Original kernel and the exact scope of the closure

In each branch an invariant ambient coordinate is proved before
using the fixed-coordinate kernel theorem. The original slice makes
\(\ker E\) regular. Bhatwadekar--Gupta--Lokhande's Theorem 3.5
therefore applies and gives \(\ker E\simeq\mathbb C^{[3]}\).[^regular]
This uses the original sliced action, not a slice transferred to
\(D\), \(L\), or \(L_0\).

Together with the previously closed rank-three good-top case, this
recognizes the entire nonzero-\(r\), nonconstant-highest branch
satisfying \(T_cu=0\). In the rotating normal form, the all-degree
condition \(R_1\nmid Q'\) implies \(T_cu=0\), so that
conditional arithmetic branch is now recognized without an extra
rank premise. The surviving possibility \(T_cu\ne0\), which
requires \(R_1\mid Q'\), is not excluded by this proof.

No new universal frame, full-profile recognition, arbitrary
cancellation conclusion, historical novelty, human expert review or
proof-assistant verification is claimed. The actual coordinate
requirements occur in (8), (11), (13) and (17); arbitrary commuting
derivations would not suffice at those steps.

## Sources and verification boundary

The mixed-column, gradient and descent arguments are proved above.
The weighted leading-LND step and primitive equal-kernel argument
are likewise supplied in full. The separate
[four-method checker](rotating_zero_motion_checks_pass45.py) imports
only `unittest` and SymPy. It checks actual mixed-column and gradient
identities, two-sided coordinate inverses and horizontal extraction,
primitive conjugation versus a nonprimitive replica, and a deliberately
non-LND vertical leading term. All four methods passed in 0.249 seconds.
The first run caught a test that compared gcd representatives literally
instead of up to a nonzero constant; monic comparison corrected that
assertion without changing a field or proof formula. These finite
mechanism controls cannot certify existence of a full high-flow
nonzero-\(r\) frame.

[^curve]: Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 with its complete proof and Lemma 3.3, PDF pp. 20--21. These passages were directly reread. The input is applied to the proved transcendence-degree-one actual algebra in (9), including its precise intersection statement.

[^plane]: Shigeru Kuroda, [*The automorphism theorem and additive group actions on the affine plane*](https://arxiv.org/pdf/1604.04070v1), Theorem 1.1 and complete proof, PDF pp. 1--3. The primary note credits the characteristic-zero invariant-coordinate theorem to Rentschler. It is used only on the actual polynomial two-ring after (17).

[^regular]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and proof, PDF p. 11; the preceding local regular-kernel argument is Proposition 3.3. These passages were directly reread. The theorem is used only after an invariant actual coordinate has been obtained.
