# The full divisor quotient is a line or a quadratic model

At every invariant prime where at least one bad-coordinate speed
remains nonzero, the full localized slice quotient has an exact
classification. It is either a polynomial line over the discrete
valuation ring, or a quadratic model
\[
R[T,Z]/(\pi^nZ-T^2+\eta),\qquad
n\ge1,\quad \eta\in R^*,\quad
\overline\eta\notin\kappa^{*2}.
\tag{1}
\]
Here \(R=C_{(\pi)}\) and \(\kappa=\operatorname{Frac}(C/\pi C)\).
The second possibility has a quadratic constant-field extension in
its special fiber. It is not excluded by this note.

This classifies the entire localized quotient, not only the
bad-image subring from pass 44. The additional step is an exact
generation argument using the actual linear bad-coordinate slice.
No new classification theorem is invoked.

## 1. Retained original hypotheses

Keep the original degree-two, independent-defect, rank-two bad
projection assumptions of
[the generic graph](generic-bad-pair-pass44.md) and
[its denominator proof](quadratic-graph-denominators-pass44.md).
In particular,
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\quad
A=\ker E,\quad E(s_*)=1,
\]
\[
C\simeq\mathbb C^{[2]},\quad L=\operatorname{Frac}C,\quad
f=Ex_3,\quad g=Ex_4,\quad f,g\in C,
\tag{2}
\]
and the actual good generators are quadratic polynomials in the
bad pair over \(L\):
\[
x_i=\mathcal Q_i(x_3,x_4),\qquad
\mathcal Q_i\in L[X_3,X_4],\quad \deg\mathcal Q_i\le2
\quad(i=1,2).
\tag{3}
\]
The common invariant inclusion \(C\subset A\) is faithfully flat.
Both \(A\) and \(B\) are UFDs, and \(C\) is factorially closed
in them. These are inherited cylinder consequences, not conclusions
drawn from an assumed polynomial presentation of \(A\).

Fix an irreducible \(\pi\in C\) and assume
\[
(f,g)C_{(\pi)}=C_{(\pi)}.
\tag{4}
\]
Equivalently, the reduced speeds are not both zero. Put
\(R=C_{(\pi)}\), \(\kappa=R/\pi R\), and
\(A_R=A\otimes_C R\), \(B_R=B\otimes_C R\).
The field of fractions of \(R\) is \(L\).

No hypothesis that \(\pi\) is a genuine graph pole is needed for
the classification. Away from \(\Delta\), the earlier proof already
gives the polynomial-line alternative.

## 2. The actual slice reduces the generators to quadratic fractions

Suppose first that \(f\in R^*\); the other case is symmetric.
The actual element
\[
\sigma=x_3/f\in B_R
\]
satisfies \(E\sigma=1\). With
\(j=gx_3-fx_4\), the exact inverse is
\[
x_3=f\sigma,\qquad x_4=g\sigma-j/f.
\tag{5}
\]
Thus \(B_R=A_R[\sigma]\), by the slice theorem on this original
localized ring. Apply the slice projection \(\sigma\mapsto0\).
The projection is an \(R\)-algebra homomorphism, so original
generation of \(B_R\) by its four actual coordinates implies
\[
A_R=R[j,q_1(j),q_2(j)]\subset L[j],
\qquad q_i(J)=\mathcal Q_i(0,-J/f),\quad\deg q_i\le2.
\tag{6}
\]
For \(g\in R^*\), use the analogous projection at \(x_4/g\).

Also
\[
A_R\cap L=R.
\tag{7}
\]
Indeed \(A\cap L=C\); localization at \(C\setminus(\pi)\)
preserves this contraction. The element \(j\) is transcendental
over \(L\), as proved by the full generic bad-pair theorem.

The prime \(\pi\) remains prime in \(A\): factorial closure
forces any factorization in the UFD \(A\) to occur already in
\(C\). Therefore \(A_R/\pi A_R\) is a domain. It is nonzero
by faithful flatness.

## 3. Elementary DVR elimination gives two generators

Here is the finite algebra behind the classification. Let
\(S=R[j,q_1(j),q_2(j)]\subset L[j]\), with \(\deg q_i\le2\),
\(S\cap L=R\), and \(j\) transcendental.

If there are two degree-two generators, choose one, called \(z\),
whose leading coefficient has the smaller valuation.
Subtract an \(R\)-multiple of \(z\) from the other generator
to remove its quadratic term. The remaining generator has degree
at most one. If only one quadratic generator existed, call it \(z\)
directly. Constant generators belong to \(R\) by contraction.

Among the remaining nonconstant linear generators, including
\(j\), choose \(t\) with the smallest leading-coefficient valuation.
Any other linear generator is \(a t+b\) with \(a\in R\).
Since \(b\in S\cap L\), it belongs to \(R\).
Consequently
\[
S=R[t]\quad\hbox{or}\quad S=R[t,z],
\qquad z\in L[t],\quad\deg_tz=2.
\tag{8}
\]
All changes use actual elements of the ring. In particular, a
linear rational expression is not adjoined merely because it lies
in the generic field.

If the coefficients of \(z\) already belong to \(R\), (8) again
gives \(S=R[t]\). Otherwise choose the smallest \(n\ge1\) such that
\[
P(t):=\pi^n z\in R[t].
\tag{9}
\]
At least one coefficient of \(P\) is a unit of \(R\), and
\(\deg P\le2\). The presentation is exact:
\[
S\simeq R[T,Z]/(\pi^nZ-P(T)).
\tag{10}
\]
To check saturation, the polynomial in (10) is primitive in the
UFD \(R[T][Z]\), since \(\gcd(\pi^n,P)=1\).
It is irreducible over \(L(T)[Z]\), hence irreducible and prime
in \(R[T,Z]\). Its domain quotient injects into its localization
at \(\pi\), where \(Z=P(T)/\pi^n\).
Thus no extra component or hidden \(\pi\)-torsion is retained.

Since \(S/\pi S\) is a nonzero domain, (10) gives
\[
S/\pi S=\kappa[T,Z]/(\overline P(T)),
\]
with \(\overline P\) irreducible and nonconstant.
It has degree one or two. A nonzero constant would give the
zero ring; reducibility or a repeated factor would contradict
the domain property.

## 4. Linear reduction gives an actual polynomial line

Suppose \(\deg\overline P=1\).
Its unique residue root lifts to an element \(t_0\in R\) satisfying
\[
P(t_0)\in\pi^nR.
\tag{11}
\]
Only finitely many elementary corrections are needed:
given a root modulo \(\pi^k\), add a multiple of \(\pi^k\)
to cancel the next residue, using the unit derivative.
This constructs (11) modulo \(\pi^n\) in \(R\) itself.
It assumes neither completeness nor Henselianity.

After replacing \(t\) by \(T=t-t_0\), the relation is
\[
\pi^n(z-c)=bT+aT^2,\qquad
c\in R,\quad b\in R^*,\quad a\in\pi R.
\tag{12}
\]
The finite polynomial
\[
L(T)=b^{-1}\sum_{k=0}^{n-1}(-aT/b)^k
\]
satisfies
\[
(b+aT)L(T)=1+\pi^nK(T)
\quad\hbox{for some }K(T)\in R[T].
\]
Thus the rational candidate is actually in the ring:
\[
w:=T/\pi^n=(z-c)L(T)-TK(T)\in S.
\tag{13}
\]
Conversely
\[
t=t_0+\pi^n w,\qquad
z=c+bw+a\pi^n w^2\in R[w].
\tag{14}
\]
Equations (13)--(14) prove \(S=R[w]\) as an actual equality
of rings. They do not use formal power series or an inverse
function assertion.

The case \(n=0\), or no quadratic generator, was already
polynomial in Section 3.

## 5. The quadratic alternative and the full special fiber

Suppose \(\deg\overline P=2\). Write
\(P=aT^2+bT+c\), with \(a\in R^*\).
After the actual changes
\[
T'=T+b/(2a),\qquad Z'=Z/a,
\]
equation (10) becomes
\[
\pi^nZ'=T'^2-\eta,\qquad
\eta=\frac{b^2}{4a^2}-\frac ca\in R.
\tag{15}
\]
Irreducibility of \(\overline P\) in characteristic zero says
\(\overline\eta\) is nonzero and nonsquare in \(\kappa\).
Thus \(\eta\) is a unit of \(R\), and
\[
A_R/\pi A_R\simeq\kappa(\sqrt{\overline\eta})[Z'].
\tag{16}
\]
This identifies the entire localized quotient fiber because
(6)--(10) establish its entire ring, not just the bad-coordinate
image. Geometrically the residue fiber splits into two lines
after extending \(\kappa\) to an algebraic closure.
No contradiction with the original hypotheses has been deduced.

## 6. Primitive intrinsic actions have exact local plinth order

Choose a primitive nonzero intrinsic LND \(D\) on \(A\) with
kernel \(C\). Such a primitive choice may be obtained by dividing
the gcd of its values on finitely many algebra generators of the
UFD \(A\). That gcd is \(D\)-invariant by the LND divisibility
lemma. No free tangent-module assertion is needed.

Primitivity means that \(D(A)\) is not contained in \(aA\)
for any nonunit \(a\in A\). In particular its reduction modulo
\(\pi\) is nonzero, and that remains true after the present
invariant localization.

If \(A_R=R[t]\), a nonzero \(R\)-LND is \(u\partial_t\)
with \(u\in R\). Primitivity forces \(u\in R^*\).
The localized plinth is \(R\), and the residue invariant field
is \(\kappa\).

In the quadratic case write the variables of (15) simply as
\(T,Z\). On \(L[T]\), any \(R\)-LND has \(D(T)=a_0\in L\).
Contraction (7) makes \(a_0\in R\), and differentiating the
relation gives
\[
D(Z)=2T a_0/\pi^n.
\]
Since \(\pi\) is prime in \(A_R\) and does not divide \(T\)
(the residue satisfies \(T^2=\overline\eta\ne0\)),
polynomiality forces \(\pi^n\mid a_0\) in \(R\).
Primitivity then gives the exact form
\[
D=u\bigl(\pi^n\partial_T+2T\partial_Z\bigr),
\qquad u\in R^*.
\tag{17}
\]

The linear-degree contraction is
\[
A_R\cap (L+LT)=R+RT.
\tag{18}
\]
For a proof, clear a smallest possible power of \(\pi\) in
\(a+bT\). A nontrivial negative valuation would reduce to a
nonzero linear relation between \(1,\overline T\) over \(\kappa\),
contrary to the quadratic irreducibility in (16).

Every local slice of \(D\) has degree one in the generic
coordinate \(T\), so (18) proves
\[
\operatorname{pl}(D|_{A_R})=\pi^nR.
\tag{19}
\]
In the actual residue ring (16), \(D\) is a nonzero constant
multiple of \(\partial_Z\) over the quadratic field.
Hence
\[
[\operatorname{Frac}\ker(\overline D):\kappa]=2.
\tag{20}
\]
In the polynomial-line alternative this degree is one.
These conclusions concern the full intrinsic residue quotient,
now justified by the additional ring-generation proof.

### 6.1. The determinant bounds the exact primitive plinth exponent

Write the full intrinsic plinth as \(\operatorname{pl}(D)=pC\),
where \(p\ne0\). Its principality is the inherited
[factorial faithfully-flat plinth theorem](intrinsic-plinth-boundary-pass27.md),
not an additional conclusion from the local models. The global
determinant fields from pass 44 restrict to LNDs of \(A\), and
\[
K_3(j)=f\Delta,\qquad K_4(j)=g\Delta.
\tag{21}
\]
On \(A_L=L[j]\), these restrictions and \(D\) are nonzero
constant multiples of \(\partial_j\). Hence
\(K_i|_A=a_iD\) for some \(a_i\in L\).

These multipliers are genuinely in \(C\). Write \(a_i\) as a
reduced fraction in the UFD \(A\). Since \(K_i\) takes every
algebra generator of \(A\) into \(A\), its denominator divides
every value of \(D\) on those generators. Primitivity forces
that denominator to be a unit. Thus \(a_i\in A\cap L=C\).
This is coefficient-gcd saturation, not a claim that a gcd-one
coefficient ideal is the unit ideal.

Consequently (21) gives actual local-slice values
\[
f\Delta=D(a_3j),\qquad g\Delta=D(a_4j).
\]
Both belong to \(pC\), so unique factorization in \(C\) yields
\[
p\mid\gcd(f,g)\,\Delta.
\tag{22}
\]
Localization of the plinth at an invariant multiplicative set
commutes with taking \(D(A)\cap\ker D\): a localized invariant
image can have its invariant denominator cleared. Therefore, at
a classified quadratic prime, (19) says \(v_\pi(p)=n\).
Since at least one speed is a unit there, (22) sharpens the
quadratic graph's raw \(\Delta^2\) denominator bound to
\[
1\le n\le v_\pi(\Delta).
\tag{23}
\]
At primes dividing both speeds, only (22) is asserted. It does
not supply the missing local classification or global gluing.

## 7. Exact remaining boundary

The classification applies at every prime \(\pi\) for which
at least one of \(f,g\) is a unit in \(C_{(\pi)}\).
It removes every linear reduced-relation branch after legitimate
changes of the intrinsic local coordinate. Such a change need
not preserve the original bad-coordinate embedding.

Two issues remain: the quadratic model (1), and primes dividing
both speeds. Neither is excluded here by the original slice,
smoothness or faithful flatness. A free action after this divisor
localization is not a global free action on the contractible
threefold, and a local coordinate is not an ambient coordinate.

The quadratic alternative need not be excluded to prove global
polynomiality. The standard polynomial three-ring already supplies
the boundary example
\[
A=\mathbb C[X,Y,Z],\qquad
D=X\partial_Y+2Y\partial_Z,\qquad
C=\mathbb C[X,H],\quad H=XZ-Y^2.
\]
At the prime \(X\) of \(C\), its exact model is
\(XZ=Y^2+H\), with \(\eta=-H\) nonsquare in
\(\mathbb C(H)\). The kernel assertion follows after inverting
\(X\) and contracting: a minimal negative \(X\)-power in an
invariant numerator would give a nonzero polynomial in \(H\)
vanishing identically at \(H=-Y^2\), which is impossible.
This is a known polynomial-ring boundary, not a realization of
the full supplied degree-two residual. The unresolved task is to
handle the global arrangement and gluing of the permitted local
models, not to treat a quadratic residue extension as evidence
that \(A\) is nonpolynomial.

The exact exponent \(n\) is retained; it is not replaced by
the reduced support. No rank-three classification on an already
polynomial three-ring is applied to the unknown \(A\).
No recognition of the entire supplied frame or of unrestricted
complex threefold cancellation is claimed.

## Attribution and verification

The inputs from the actual frame are the frozen pass-44
quadratic graph, original-generator equality, original slice
and inherited factorial faithful-flat quotient. The remainder
is the full elementary DVR elimination, finite root lifting,
Gauss-lemma saturation and residue contraction written above.
This is not an application of an unverified global
affine-modification theorem.

The standalone
[four-method checker](quadratic_divisor_checks_pass45.py), importing
only unittest and SymPy, passed the final bounded run in
0.284 seconds. It checks generator elimination with a hidden
quadratic residue field, finite root-lift and inverse identities,
unit square completion, and the residue/primitivity controls for
the standard action. An initial broader finite exponent grid also
passed; it was reduced to keep the recurring regression bounded.
No assertion failed and the number of methods remains four.
These controls do not prove the all-prime quantifier or exclude (1).
No historical novelty, human expert review or proof-assistant
verification is asserted.
