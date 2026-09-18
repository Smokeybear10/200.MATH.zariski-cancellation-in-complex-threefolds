# Three quadratic adjoint bounds in an actual three-variable frame

A locally nilpotent derivation of the complex polynomial three-ring
fixes an actual coordinate if its third iterated adjoint kills every
partial of one polynomial coordinate frame. No slice is assumed on
this three-variable derivation. This recognizes the remaining
four-variable profile with one commuting column and three quadratic
columns, provided the original four-variable action has a slice.

The result concerns a supplied actual frame. It does not produce such
a frame for an arbitrary cancellation candidate. The proof uses
established commuting-LND and nice-derivation theorems; no novelty,
expert review, formal verification, or general cancellation solution
is claimed.

## 1. Prior scope and exact statement

The earlier [commuting-column audit](commuting-coordinate-partial-pass.md)
does not recognize an arbitrary sliced extension
\(D+a\partial_t\) of a rank-three base derivation. In particular,
an original slice cannot simply be transferred to \(D\), and its
coefficient need not have the form \(c+D(H)\).

The [single-partial lemma](height-seven-audit.md#2-a-single-partial-lemma-in-three-variables)
already recognizes a three-variable LND when one actual partial has
vanishing second iterated adjoint. That is a different hypothesis
from the three third-adjoint bounds used here. The argument below
either invokes that earlier criterion or obtains a suitable commuting
nice action directly.

**Theorem.** Let \(R=\mathbb C[y_1,y_2,y_3]\), and let
\(D\in\operatorname{LND}(R)\). Put \(T_i=\partial_{y_i}\).
If
\[
\operatorname{ad}_D^3T_i=0\qquad(i=1,2,3),
\tag{1}
\]
then \(\ker D\) contains an actual coordinate of \(R\).
For nonzero \(D\), this says \(\operatorname{rank}D\le2\).

The case \(D=0\) is immediate. Assume \(D\ne0\) for the proof.
Write \(K=\operatorname{Frac}R\), \(y=(y_1,y_2,y_3)^{\mathsf t}\),
and
\[
v=Dy,\quad J=\operatorname{Jac}v,\quad
W_i=[D,T_i],\quad U_i=[D,[D,T_i]].
\tag{2}
\]
All matrix calculations below take place over \(K[t]\), but
the final vector fields used for recognition are polynomial on \(R\).
No rational rescaling of \(D\) is made.

## 2. Independent quadratic tops already give a coordinate

Extend derivations to \(R[t]\) by killing \(t\). The actual
conjugate of the coordinate partial is
\[
\exp(tD)T_i\exp(-tD)=T_i+tW_i+\frac{t^2}{2}U_i.
\tag{3}
\]
It is an LND of \(R[t]\). For a fixed \(f\in R\), take an
iterate of (3) that kills \(f\). Its highest coefficient in
\(t\) is the corresponding iterate of \(U_i/2\). Thus
each \(U_i\) is an LND. Also \([D,U_i]=0\) by (1).

If any \(U_i\) is independent of \(D\) over \(K\), the
commuting-LND theorem gives a coordinate generating their common
kernel.[^commuting] This proves the conclusion in that case.
Otherwise there are \(h_i\in K\) with
\[
U_i=h_iD,
\qquad D(h_i)=0.
\tag{4}
\]
The zero tops are included by \(h_i=0\). The coefficients
\(h_i\) need not be polynomial; their rationality causes no
localization or divisibility assumption in what follows.

Put \(h=(h_1,h_2,h_3)^{\mathsf t}\). The column matrix of
the \(U_i\) is the rank-at-most-one polynomial matrix
\[
S=vh^{\mathsf t}.
\tag{5}
\]

## 3. The rank-one adjugate update bounds the actual flow degree

Let \(F_t=\exp(tD)y\). Its Jacobian has determinant one:
the polynomial flow is an automorphism of \(R[t]\), and its
Jacobian is a unit specializing to one at \(t=0\).
The matrix of (3) is exactly its inverse Jacobian. Since
the coefficients of \(W_i\) are the columns of \(-J\),
\[
C(t):=(\operatorname{Jac}F_t)^{-1}
=I-tJ+\frac{t^2}{2}vh^{\mathsf t},
\qquad \det C(t)=1.
\tag{6}
\]
Consequently \(\operatorname{Jac}F_t=\operatorname{adj}C(t)\).

For any square matrix \(A\) and vectors \(v,h\), one has
the polynomial identity
\[
\operatorname{adj}(A+qvh^{\mathsf t})v
=\operatorname{adj}(A)v.
\tag{7}
\]
For an invertible generic \(A\), the determinant lemma and
rank-one inverse formula prove (7) by cancellation of the common
factor \(1+q h^{\mathsf t}A^{-1}v\). Since both sides are
polynomial in the matrix entries, this proves (7) identically,
including singular specializations. Here \(A=I-tJ\) is already
invertible over \(K(t)\), so only this generic-field calculation
is needed.

Apply (7) to (6). Differentiation of the actual flow gives
\[
\frac{dF_t}{dt}
=D(F_t)=(\operatorname{Jac}F_t)v
=\operatorname{adj}(I-tJ)v.
\tag{8}
\]
The right side has degree at most two in \(t\), because
\(I-tJ\) is a three-by-three matrix. Therefore
\[
D^4y=0.
\tag{9}
\]
This bound is obtained only after the independent-top cases have
been separated. It is not asserted for every derivation satisfying
(1) by this calculation alone.

## 4. The last nonzero iterate has Jacobian rank at most one

Let \(m\ge1\) be the largest integer with \(D^my\ne0\),
and put \(H=D^my\). By (9), \(m\le3\). If \(m=1\),
then \(D^2y=0\), so the nice-derivation theorem supplies a
nonzero invariant linear form.[^nice] Assume \(m=2\) or \(3\).

The coefficient of \(t^m\) in \(\operatorname{Jac}F_t\)
is \(\operatorname{Jac}H/m!\). Since
\(\det\operatorname{Jac}F_t=1\), (6) also says
\(\operatorname{adj}(\operatorname{Jac}F_t)=C(t)\), a
matrix of degree at most two. The coefficient of \(t^{2m}\)
on the left is
\[
\frac{1}{(m!)^2}\operatorname{adj}(\operatorname{Jac}H).
\]
Because \(2m>2\), it vanishes. A three-by-three matrix has
zero adjugate exactly when its rank is at most one. Thus
\[
\operatorname{rank}_K\operatorname{Jac}H\le1.
\tag{10}
\]
This includes the possibility that \(H\) is a nonzero constant
vector. No factorization through a polynomial curve parameter
has been assumed.

Define the polynomial vector field \(T_H=H\cdot\partial\).
Since \(DH=0\), (4) gives
\[
[D,[D,T_H]]=(h^{\mathsf t}H)D.
\tag{11}
\]
On the other hand \(C(t)F'_t=v\). Its coefficients of
degrees \(m+1\) and \(m\), respectively, give
\[
h^{\mathsf t}H=0,
\qquad
JH=\frac{m-1}{2}(h^{\mathsf t}D^{m-1}y)v.
\tag{12}
\]
These identities retain both Taylor factors. Put
\[
\kappa=-\frac{m-1}{2}h^{\mathsf t}D^{m-1}y\in K.
\]
Then
\[
[D,T_H]=\kappa D,
\qquad D\kappa=0.
\tag{13}
\]
The second assertion follows from (11)--(12) and \(D\ne0\).
It is a field identity, not a claim that \(\kappa\) is polynomial.

Because \(D\kappa=0\), ordinary operator commutation gives
\([D^m,T_H]=m\kappa D^m\). Applying it to \(y\), and
using \(D^m(T_Hy)=D^mH=0\), yields
\[
T_HH=-m\kappa H.
\tag{14}
\]

## 5. Two final cases, both global

### Zero multiplier

If \(\kappa=0\), equations (13)--(14) say
\[
[D,T_H]=0,
\qquad T_H^2y=0.
\]
The field \(T_H\) is a nonzero polynomial nice LND on \(R\).
If it is independent of \(D\) over \(K\), apply the
commuting-LND coordinate theorem. If they are dependent,
their kernels are equal. The nice-derivation theorem supplies
an actual invariant linear form for \(T_H\), hence for \(D\).
Both assertions concern polynomial fields on the original ring.

### Nonzero multiplier

Suppose \(\kappa\ne0\). Equation (14) becomes
\[
(\operatorname{Jac}H)H=-m\kappa H\ne0.
\tag{15}
\]
Thus \(H\) belongs to the image of \(\operatorname{Jac}H\).
By (10), that image is exactly \(KH\). Every column of
\(\operatorname{Jac}H\) is proportional to \(H\).
Choose a nonzero component \(H_j\). It follows that every
ordinary partial derivative of each ratio \(H_i/H_j\) is zero.
The common constants of the ordinary partials on
\(\mathbb C(y_1,y_2,y_3)\) are \(\mathbb C\). Therefore
\[
H=Fc,
\qquad 0\ne F\in R,
\quad c\in\mathbb C^3\setminus\{0\}.
\tag{16}
\]
Here one may take \(F=H_j\); no root extraction or denominator
clearing of a curve parameter is involved.

Equation (12) now gives \(h^{\mathsf t}c=0\). Hence the
nonzero constant partial \(T_c=c\cdot\partial\) satisfies
\[
[D,[D,T_c]]=\sum_i c_iU_i
=(h^{\mathsf t}c)D=0.
\tag{17}
\]
After an actual complex linear coordinate change, \(T_c\) is
a coordinate partial. The earlier single-partial lemma applies
and supplies a coordinate of \(R\) killed by \(D\).
This proves the theorem in all cases.

For completeness, that lemma does not assume a slice: its first
commutator is a commuting LND by actual conjugation. An independent
pair uses Maubach. In the dependent case, dividing the original
coefficient vector by its polynomial gcd makes its entries independent
of the selected coordinate; the restricted planar LND then uses
Rentschler. The full denominator proof remains in the linked earlier
audit, and these are established recognition inputs, not a new
unrestricted rank theorem.

## 6. Application to one commuting column in four variables

Let \(B=\mathbb C[t,y_1,y_2,y_3]\), and let \(E\) be an
LND with a polynomial slice. Suppose the actual partials satisfy
\[
[E,\partial_t]=0,
\qquad \operatorname{ad}_E^3\partial_{y_i}=0
\quad(i=1,2,3).
\tag{18}
\]
Commutation makes every coefficient of \(E\) independent of
\(t\). Therefore, on this actual presentation,
\[
E=D+a(y)\partial_t,
\qquad D\in\operatorname{LND}(\mathbb C[y_1,y_2,y_3]),
\quad a\in\mathbb C[y_1,y_2,y_3].
\tag{19}
\]
Restriction of the other adjoint equations gives (1) for \(D\).

If \(D=0\), the slice identity forces \(a\) to be a unit:
every value of \(E=a\partial_t\) belongs to \(aB\), and
one such value is one. Thus \(a\in\mathbb C^*\), and the
kernel is the original polynomial three-ring.

If \(D\ne0\), the theorem supplies an actual coordinate
\(p\) of \(\mathbb C[y_1,y_2,y_3]\) killed by \(D\).
It remains an ambient coordinate of \(B\) and is killed by
\(E\), regardless of the coefficient \(a\). The original
slice gives \(B=(\ker E)[s_*]\), so \(\ker E\) is regular.
The regular-kernel theorem yields
\[
\ker E=\mathbb C[p]^{[2]}\simeq\mathbb C^{[3]}.
\tag{20}
\]
No slice on \(D\), no affine-in-\(t\) replacement slice,
and no gauge expression for \(a\) is required.[^regular]

Thus the supplied profile \((0,2,2,2)\) is recognized. The
argument says nothing about automatic existence of that profile
on an arbitrary polynomial cylinder. The distinct two-quadratic
profile remains a separate problem unless independently closed.

## 7. Actual profile control and finite verification

The hypotheses do not require the base derivation to have a slice.
For an actual example, take
\[
N=\begin{pmatrix}-1&-3&-1\\1&1&1\\0&2&0\end{pmatrix},
\quad D(y)=Ny,\quad E=D+\partial_t.
\tag{21}
\]
Here \(N^3=0\), every column of \(N^2\) is nonzero, and
\(D\) vanishes at the origin. Thus \(D\) has no slice,
whereas \(Et=1\). The actual adjoint heights are exactly
\((0,2,2,2)\) in the order \((\partial_t,\partial_{y_1},
\partial_{y_2},\partial_{y_3})\). The coordinate inverse pair
\[
k=\left(I-tN+\frac{t^2}{2}N^2\right)y,
\quad s=t,
\qquad
y=\left(I+sN+\frac{s^2}{2}N^2\right)k,
\quad t=s
\tag{22}
\]
also proves the exact shifted slice-filtration profile: the
transformed three base partials have degree two in \(s\),
and the transformed \(\partial_t\) has degree zero.
This is a genuine polynomial example within the recognized family,
not an example of a nonpolynomial cancellation candidate.

The standalone
[three_variable_quadratic_frame_checks_pass42.py](three_variable_quadratic_frame_checks_pass42.py)
imports only `unittest` and `sympy`. Its six methods check the
generic adjugate update, both highest-flow coefficients, the
highest adjugate-minor coefficient, (21)--(22) and all four actual
partial profiles, a cubic-flow zero-quadratic-top example, and the
necessity of the augmented-image condition in the projective step.
The first run passed all six methods in 0.426 seconds, with no
assertion failure. Formal matrix and projective controls are
separated from the actual derivation examples.

The geometry investigator independently read the complete proof,
including the zero-derivation and constant-top boundaries, and
reported a clean reconstruction. The Maubach, Wang, Rentschler and
regular-kernel statements cited below were directly reread from
their retained primary sources in this pass. The finite checks
do not machine-prove those theorems or the universal reduction.

## Primary source gates

[^commuting]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 3.6 and its proof, with Proposition 3.5, PDF pp. 4-5. It recognizes the joint kernel of two commuting polynomially independent LNDs of the actual complex polynomial three-ring. The equivalent distinct-kernel statement is Proposition 2.14 of Dasgupta and Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), PDF p. 7.

[^nice]: Wang's three-variable nice-derivation theorem, stated with attribution as Theorem 3.1(i) in Dasgupta and Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), PDF p. 5. It requires a nonzero polynomial LND killing every coordinate under its second iterate. It supplies a nonzero invariant linear form; no slice or irreducibility premise is needed for this part. The earlier single-partial lemma also uses Rentschler's actual-plane theorem, stated as Theorem 2.7 in Dasgupta and Gaifullin, PDF p. 6.

[^regular]: Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and its proof, PDF p. 11. Its hypotheses are a nonzero LND fixing an actual ambient coordinate and a regular original kernel. Both are proved before the application in Section 6.
