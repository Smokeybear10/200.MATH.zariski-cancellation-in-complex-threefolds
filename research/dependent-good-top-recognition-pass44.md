# Commuting good tops recognize a rank-three dependent branch

In the rotating dependent high-top branch, the two good leading fields
commute with the primitive defect direction and fix all reduced
multipliers. When the actual good constant direction kills the curve
parameter, a rank-three span of these actions recognizes the original
kernel. The remaining case within that zero-motion branch has rank
exactly two.

## 1. Actual hypotheses

Use all assumptions of
[the dependent preceding-curve proof](dependent-preceding-curve-pass44.md).
In particular \(B=\mathbb C[x_1,x_2,x_3,x_4]\), the original LND
\(E\) has a polynomial slice, and \(T_i=\partial_{x_i}\) are
actual coordinate partials. For \(i=1,2\), put
\(W_i=[E,T_i]\); then \([E,W_i]=0\).
The nonconstant highest vector has order \(m\in\{3,4\}\) and
\[
E^mx=cq,\qquad c\ne0,\quad c_3=c_4=0,
\qquad q=Q(u),\quad \deg Q>0.
\tag{1}
\]
The two quadratic defects are \(aD,bD\), where \(D\) is a
primitive polynomial LND commuting with \(E\). In the nonzero
commutator branch,
\[
W_c:=[E,T_c]= -\alpha rD,\qquad
\alpha=(m-1)/2,\quad r\ne0,\quad Er=Dr=0.
\tag{2}
\]
Here \(T_c=c_1T_1+c_2T_2\) is a nonzero actual constant partial.
The original-slice argument has already proved that \(E,D\) are
fraction-field independent.

In the rotating alternative, the actual polynomial parameter and
exact multiplier form are
\[
Eu=Du=0,\qquad
a=H_1Q_1(u)a_0(u),\quad b=H_1Q_1(u)b_0(u),\quad
r=H_1R_1(u),
\tag{3}
\]
where \(H_1\ne0\), \(R_1\ne0\), and the other factors are the
univariate polynomials constructed in that proof. No ambient-coordinate
status of \(u\) is assumed.

## 2. Primitivity makes the good tops commute with the defect

Each \(W_i\) is an actual polynomial LND, possibly zero. This
can be checked without localizing any ordinary partial at a moving
coefficient. For an external invariant parameter \(\varepsilon\),
\[
\varepsilon\exp(\operatorname{ad}_{E/\varepsilon})T_i
=\varepsilon T_i+W_i.
\tag{4}
\]
The left side is an LND on \(B[\varepsilon,\varepsilon^{-1}]\):
it is an invariant multiple of an actual conjugated coordinate
partial. The right side preserves \(B[\varepsilon]\) and kills
\(\varepsilon\). Restriction and specialization at zero give
local nilpotence of \(W_i\) on \(B\).

The conjugated good partials \(T_i+tW_i\) commute. Their
quadratic coefficient gives \([W_1,W_2]=0\). Since
\(W_c=c_1W_1+c_2W_2\), (2) yields
\[
[W_i,rD]=0,\qquad
[W_i,D]=-\frac{W_i(r)}rD\quad(i=1,2).
\tag{5}
\]
The left side of the second identity is polynomial. Primitivity
of the coefficient vector of \(D\) therefore makes the rational
coefficient \(W_i(r)/r\) polynomial: a denominator in reduced
form would divide every coefficient of \(D\). Thus
\(r\mid W_i(r)\) in \(B\).

The LND divisibility lemma now gives \(W_i(r)=0\). Indeed a
nonzero derivative lowers LND degree by one, whereas multiplication
by a nonzero polynomial cannot do so. Hence
\[
[W_i,D]=0,\qquad W_i(r)=0\quad(i=1,2).
\tag{6}
\]
This argument uses polynomial coefficient gcd one, not a unit
coefficient ideal for \(D\).

There is a separate exact invariance argument for \(u\). Apply
\(T_i+tW_i\) to the actual flow \(\exp(tE)x\). The result is
the constant coordinate vector. The coefficient of \(t^{m+1}\)
is \(W_i(cq)/m!\), so \(W_iq=0\). Since
\(q=Q(u)\) and \(Q'(u)\ne0\),
\[
W_i(u)=0.
\tag{7}
\]
In the rotating form (3), equations (6)--(7) then give
\[
W_i(H_1)=W_i(a)=W_i(b)=0.
\tag{8}
\]
Thus \(E,D,W_1,W_2\) are pairwise commuting global LNDs, all
fixing the nonconstant polynomial \(u\). The zero good fields
cause no exception to these identities.

## 3. Recognition and the exact remaining rank

Suppose in addition that \(T_cu=0\). If
\[
\operatorname{rank}(E,D,W_i)=3
\quad\text{for either }i\in\{1,2\},
\tag{9}
\]
the three indicated fields are independent commuting global LNDs
on the actual complex four-ring. They fix a nonconstant polynomial
\(u\) omitted by the nonzero constant direction \(T_c\).
The [omitted-coordinate criterion](commuting-coordinate-descent-pass43.md)
therefore gives an invariant ambient coordinate and
\[
\ker E\simeq\mathbb C^{[3]}.
\tag{10}
\]
The criterion uses the established common-kernel and full-dimensional
commuting-action theorems, complex surface cancellation, and the
three-variable general-plane-fiber theorem. It is not an application
of the unresolved threefold cancellation statement. The final
fixed-coordinate kernel step uses regularity supplied by the original
slice of \(E\). No slice is transferred to \(D\) or to a good top.

Because \(E,D\) already have rank two, condition (9) is equivalent
to \(\operatorname{rank}(E,D,W_1,W_2)=3\). Their joint rank is
at most three since they all kill the nonconstant \(u\).
Thus only joint rank two remains within the \(T_cu=0\) branch.

In particular the preceding motion obstruction gives the explicit
conditional recognition
\[
R_1\nmid Q',\quad
\operatorname{rank}(E,D,W_1,W_2)=3
\quad\Longrightarrow\quad \ker E\simeq\mathbb C^{[3]}.
\tag{11}
\]
The nondivisibility here is in \(\mathbb C[U]\) and retains all
multiplicities. The case \(R_1\mid Q'\) is not excluded, and
\(T_cu\ne0\) is not ruled out by the commutation proof.
No claim that the rank-three condition is automatic is made.

## Verification boundary

This is a written deduction from actual conjugated-column identities,
primitive polynomial coefficients, and the already source-audited
coordinate criterion. It adds no numerical methods or claimed
realization of the nonzero-\(r\) branch. Independent reconstruction
is not human expert review or proof-assistant verification.
The complete supplied profile and unrestricted cancellation question
remain unresolved.
