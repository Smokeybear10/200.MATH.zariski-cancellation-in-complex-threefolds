# The independent zero-motion high-top branch is recognized

The independent-defect power-law branch with zero motion in its actual
highest constant direction has an invariant ambient coordinate. The
remaining rank-two case is resolved by the two good derivatives of the
top parameter. If they generate a surface field, the common invariant
ring descends to an actual three-variable ring. If they generate only a
curve field, an invariant coordinate follows either directly from a
good partial or from the published theorem on invariants in an actual
two-variable subring.

The binary invariant theorem is an established external input, not a
new assertion about stable invariants. The result does not treat
nonzero parameter motion, constant highest vectors, or the entire
two-quadratic profile.

## 1. Original hypotheses and the polynomial fields used

Retain the actual independent high-top hypotheses of
[the full companion proof](two-quadratic-top-line-pass42.md).
Thus \(B=\mathbb C[x_1,x_2,x_3,x_4]\), the LND \(E\) has
an original polynomial slice, and \(T_i=\partial_{x_i}\) satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad\operatorname{ad}_E^3T_3=
\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Put \(W_i=[E,T_i]\) and \(V_i=[E,W_i]\). The fields
\(V_3,V_4\) are independent. In the nonzero preceding-bad
alternative the actual full-companion reduction gives
\[
E^mx=cg^m,\quad
(E^{m-1}x)_{\rm bad}=\lambda g^{m-1},\quad
3\le m\le5,
\tag{2}
\]
where \(g\in\ker E\setminus\mathbb C\), \(c\ne0\) is a
constant good vector, and \(\lambda\ne0\) is a constant bad
two-vector. Assume
\[
T_cg=0,\qquad T_c=\sum c_iT_i.
\tag{3}
\]
Set \(\alpha=(m-1)/2\),
\[
T_\lambda=\lambda_3T_3+\lambda_4T_4,\quad
V=\lambda_3V_3+\lambda_4V_4\ne0,
\quad U=[E,T_c].
\]
The exact inherited denominator and next-column identities are
\[
gU=-\alpha V,\quad
[E,U]=[E,V]=0,
\quad Eg=Ug=Vg=0,
\tag{4}
\]
and, choosing \(j\) with \(c_j\ne0\),
\[
\tau=(E^{m-1}x)_j/c_j,\qquad
E\tau=g^m,\qquad V\tau=0.
\tag{5}
\]
These are proved in the
[actual global normalizer construction](quadratic-heisenberg-repair-pass43.md).
Both \(U\) and \(V\) are global polynomial LNDs: \(U\)
is the good leading coefficient, and \(V\) is the highest
coefficient of an actual conjugated bad coordinate partial.
Equation (4) is a polynomial identity. It does not assert that an
arbitrary rational multiple of an LND is polynomial.

**Theorem.** Under (1)--(3), \(E\) fixes an actual ambient
coordinate and \(\ker E\simeq\mathbb C^{[3]}\).

The zero preceding-bad alternative is already recognized in the
full companion proof. The theorem here addresses the nonzero
alternative (2).

## 2. All required rank alternatives

The actual highest-column identities give
\[
V_3g=V_4g=W_1g=W_2g=0.
\tag{6}
\]
The good tops are LNDs, and they commute with \(E\). The
coefficients of degrees four and three in the commutation of actual
conjugated partials give, respectively,
\[
[V_3,V_4]=0,\qquad [W_i,V_j]=0
\quad(i=1,2;\ j=3,4).
\tag{7}
\]
If \(E,V_3,V_4\) have rank three, they are commuting global
LNDs fixing \(g\), which is omitted by the actual direction
\(T_c\). The already proved
[omitted-coordinate criterion](commuting-coordinate-descent-pass43.md)
recognizes the original kernel.

Otherwise their rank is two. Equation (5) shows that \(E,V\)
are independent: a rational multiple of \(E\) killing \(\tau\)
would be zero. Thus they span the same distribution as
\(V_3,V_4\). If either good top lies outside that plane, the
triple \(E,V,W_i\) is independent and commuting by (7), and
the same criterion applies.

It remains only to consider
\[
\operatorname{span}_{\operatorname{Frac}B}
\{E,V_3,V_4,W_1,W_2\}
=\operatorname{span}_{\operatorname{Frac}B}\{E,V\},
\quad\text{of dimension two}.
\tag{8}
\]
No additional assumption on the rank of a normalizer \(Y\) is
needed for the following argument. In particular, it includes the
previously remaining case where that normalizer also has rank two.

## 3. The two good derivatives lie in the common invariant ring

Let
\[
C=\ker E\cap\ker V.
\tag{9}
\]
The original slice writes \(B=A[s]\), \(A=\ker E\).
Independence in (5) makes \(V|_A\) nonzero. Its local-slice
theorem therefore gives \(\operatorname{trdeg}\operatorname{Frac}C=2\).
A polynomial-coordinate presentation of \(C\) is not assumed.
Every good \(W_i\) kills \(C\), by (8).

For \(i=1,2\), the degree-one coefficient in the commutation
of the actual conjugated \(T_c,T_i\) is
\[
[T_c,W_i]+[U,T_i]=0.
\tag{10}
\]
Apply it to \(g\). Equations (3),(6) make the first term zero;
the second is \(U(T_i g)\). By (4), this implies
\(V(T_i g)=0\). Also \(E(T_i g)=W_i g=0\). Hence
\[
F=\mathbb C[g,T_1g,T_2g]\subseteq C.
\tag{11}
\]
The nonconstant \(g\) makes its transcendence degree one or two.
Moreover \(T_c\) kills all of \(F\), because it commutes with
the actual good partials and kills \(g\).

Only the two good derivatives occur in (11). The bad middle fields
need not kill \(g\), so their corresponding ordinary derivatives
are not silently included in the invariant algebra.

## 4. Surface-field case: actual three-ring descent

Suppose \(\operatorname{trdeg}F=2\). Then
\(\operatorname{Frac}C\) is algebraic over
\(\operatorname{Frac}F\). Since \(T_c\) kills the latter,
characteristic zero gives
\[
T_c(C)=0.
\tag{12}
\]
Choose actual linear good coordinates with
\[
B=R_0[a],\quad R_0=\mathbb C[b,y,z],\quad
T_c=\partial_a,\quad S=\partial_b.
\tag{13}
\]
Here \(y,z\) are the actual bad coordinates. Equation (12)
puts \(C\) in \(R_0\). For \(f\in C\), the remaining
good top kills \(f\), so \(E(Sf)=0\); also
\(T_c(Sf)=S(T_cf)=0\). Consequently \(U(Sf)=0\).
The exact proportionality in (4), with \(g\ne0\), gives
\(V(Sf)=0\). Thus
\[
S(C)\subseteq C.
\tag{14}
\]
This verifies the missing descent condition using actual partials
and the polynomial relation \(gU=-\alpha V\).

For completeness, the actual three-ring recognition mechanism is
the one fully proved in
[Sections 5--6 of the dependent zero-motion proof](rotating-zero-motion-closure-pass45.md#5-extraction-on-the-actual-three-ring).
Its hypotheses now hold with \(V\) replacing \(D\).
The horizontal part of \(E\) relative to \(a\) is nonzero:
otherwise \([E,T_c]\) would be parallel to \(E\), contradicting
(4)--(5). The highest \(a\)-weighted LND has form \(a^dL\)
for a nonzero polynomial LND \(L\) on \(R_0\). A nonzero
vertical top is excluded because its value on \(a\) is divisible
by \(a\), impossible for an LND.

Coefficient comparison in \(Ef=0\) gives \(C\subseteq\ker L\).
Both fields have transcendence degree two; algebraicity and the
joint-kernel definition give the exact equality \(\ker L=C\).
Divide \(L\) to a primitive polynomial LND \(L_0\).
The actual translations generated by \(S\) preserve \(C\)
by (14). Their conjugates of \(L_0\) have the same kernel
and are primitive over \(R_0[t]\); the reduced rational ratio
is a unit of that ring, hence a complex constant and one at zero.
Therefore \([S,L_0]=0\).

The restriction of \(L_0\) to the actual plane \(\mathbb C[y,z]\)
is consequently an LND. If zero, both bad coordinates belong to
\(C\); if nonzero, the established plane invariant-coordinate
theorem supplies a coordinate in \(C\).[^plane]
In either case \(E\) fixes an actual ambient coordinate.

## 5. Curve-field case: a good coordinate or a binary invariant

Suppose \(\operatorname{trdeg}F=1\). The polynomial curve
theorem supplies \(v\in B\setminus\mathbb C\) such that
\[
\operatorname{Frac}F=\mathbb C(v),\quad
B\cap\mathbb C(v)=\mathbb C[v],\quad
g=P(v),\quad T_i g=P_i(v)\ (i=1,2),
\tag{15}
\]
where the displayed polynomials are univariate and \(\deg P>0\).[^curve]
For either good partial,
\[
T_i v=P_i(v)/P'(v)\in B\cap\mathbb C(v)=\mathbb C[v].
\]
Its actual local nilpotence makes this derivative a complex constant.
Also \(Ev=Vv=T_cv=0\), by differentiating \(g=P(v)\).

In the actual good frame (13), write \(Sv=\kappa\in\mathbb C\).
If \(\kappa\ne0\), then
\[
v=\kappa b+H(y,z),\qquad
b=(v-H(y,z))/\kappa.
\tag{16}
\]
This is an actual triangular coordinate with a polynomial inverse,
and it is killed by \(E\).

If \(\kappa=0\), both actual good partials kill \(v\).
Thus
\[
v,g\in\mathbb C[y,z],\qquad
g\notin\mathbb C,\qquad Eg=0.
\tag{17}
\]
Apply the published binary-invariant theorem: an LND on a polynomial
ring over a characteristic-zero field that fixes a nonconstant
polynomial in an actual two-variable subring either kills both plane
variables or fixes a coordinate of that plane.[^binary]
It does not require \(E\) to preserve the plane subring.
Both conclusions in the theorem therefore give an actual ambient
coordinate in \(\ker E\).

No generic affine-line form, stable-coordinate descent, or geometric
fiber recognition is inferred at (17). The precise established
binary-invariant theorem is the gate used here.

## 6. Conclusion and limits

Every rank and gradient-field case above yields an actual invariant
ambient coordinate. The original slice makes \(\ker E\) regular.
The fixed-coordinate regular-kernel theorem then gives
\(\ker E\simeq\mathbb C^{[3]}\).[^regular]

This closes the nonconstant independent power-law high-top branch
with \(T_cg=0\), including the earlier two rank-two conditions.
It does not assert \(T_cg=0\) automatically. The nonconstant
motion branch and the separate constant-highest and low-flow cases
are not recognized by this argument. The two good actual partials,
not arbitrary rational generators of the same distribution, are
essential in (10), (13)--(16).

## Sources and finite verification boundary

The mixed-column deduction and both field-dimension alternatives
are written above. The earlier exact three-ring proof is used only
after (12)--(14) verify its actual-coordinate hypotheses.
The separate [three-method checker](independent_zero_motion_checks_pass45.py)
imports only `unittest` and SymPy. All three methods passed in
0.131 seconds. It checks an actual good-gradient surface-field
control with the polynomial replica relation, an actual triangular
good-coordinate case, and a binary invariant for an action that
does not preserve the plane. Every displayed coordinate change has
both inverse compositions checked. The first run compared one
expanded polynomial to its identical factored form literally;
expanding that expected expression corrected the assertion without
changing the formula or action. No full nonconstant high-flow
realization is asserted by these mechanism controls.
No historical novelty, human expert review,
proof-assistant verification, or unrestricted cancellation conclusion
is claimed.

[^curve]: Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2, complete proof and Lemma 3.3, PDF pp. 20--21. These passages were directly reread and are applied only after the actual algebra (11) has transcendence degree one.

[^plane]: Shigeru Kuroda, [*The automorphism theorem and additive group actions on the affine plane*](https://arxiv.org/pdf/1604.04070v1), Theorem 1.1 and complete proof, PDF pp. 1--3, directly reread. The characteristic-zero theorem is credited there to Rentschler.

[^binary]: Shigeru Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313v2), Proposition 3.2 and the following discussion, PDF p. 8, directly read. It explicitly states the exact binary-subring theorem for a characteristic-zero LND on any larger polynomial ring, credits Daigle--Freudenburg via Freudenburg's book, Theorem 5.37 and Corollary 5.40, and cites Gene Freudenburg, [*A note on the kernel of a locally nilpotent derivation*](https://doi.org/10.1090/S0002-9939-96-03003-1), *Proceedings of the AMS* 124 (1996), 27--29. The original 1996 publisher PDF was not retrieved in this audit; its proof is not represented as freshly reconstructed. The directly read Kuroda proposition supplies the theorem with its precise hypotheses.

[^regular]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Proposition 3.3 and Theorem 3.5 with their proofs, PDF pp. 10--11, directly reread. Applied only to the original sliced action after obtaining an invariant ambient coordinate.
