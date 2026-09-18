# A forced cubic element and a first-jet rank exclusion

At a reduced second-image obstruction point, faithful flatness forces
an actual element of derivation degree three into the ring. It makes
the third image ideal principal even though the second image ideal
is not. The two first-order derivative coefficients cannot be
independent: otherwise the cubic algebra is the whole ring and its
closed fiber contradicts the pointwise plinth criterion.

The cubic construction also works at a possibly nonreduced
obstruction point under the stronger coefficient premise specified
below. No unrestricted generation by degree-three elements is asserted.

## 1. Actual local hypotheses

Use the established actual setting of the
[second-image bundle note](second-image-vector-bundle-pass47.md)
and the [flat-conic gate](flat-conic-topology-gate-pass47.md).
At an obstruction point put
\[
R=C_{\mathfrak m},\quad \mathfrak n=\mathfrak mR,\quad
\mathcal A=A\otimes_C R,\quad L=\operatorname{Frac}R.
\tag{1}
\]
The ring \(R\) is a regular local surface ring over \(\mathbb C\).
The actual \(\mathcal A\) is faithfully flat over \(R\), is a
domain, and has its embedded height-one intersection property.
The original polynomial cylinder supplies the pointwise plinth
criterion; it is not replaced by a weaker abstract conic model.

Write \(F_i=\ker(D^{i+1}|_{\mathcal A})\). The actual local data are
\[
F_2=R\oplus Rz\oplus Rw,\quad r=az+bw,\quad
JR=(a,b),\quad \gcd(a,b)=1,
\tag{2}
\]
\[
Dr=p,\quad Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,
\quad p=aB_1+bB_2,\quad\epsilon\in R^*,
\tag{3}
\]
\[
\epsilon r^2-2B_2z+2B_1w=Q\in R.
\tag{4}
\]
The pair \(a,b\) is a regular sequence, since its ideal is
\(\mathfrak n\)-primary and its generators are coprime.
The flat-conic theorem proves
\(a,b,B_1,B_2,Q\in\mathfrak n\), but does not in general
put \(B_1,B_2\) in \(J\).

For Sections 2–5 assume additionally
\[
B_1,B_2\in(a,b).
\tag{5}
\]
This is automatic at every reduced obstruction point, where
\(JR=\mathfrak n\). It is an extra premise when the local
obstruction scheme is nonreduced. Equation (4), followed by
faithful-flat contraction, then gives \(Q\in(a,b)\).

Choose invariant coefficients in \(R\) such that
\[
B_1=ac+bd,\qquad B_2=ae+bf,\qquad Q=aq+bh.
\tag{6}
\]
Every coefficient in this display is killed by \(D\).

## 2. Regular-sequence division supplies an actual cubic element

Define elements of the actual ring
\[
G=\epsilon rz-2ez+2cw-q,
\qquad H=\epsilon rw-2fz+2dw-h.
\tag{7}
\]
Equations (2), (4), (6) give \(aG+bH=0\). Since flatness
preserves the regular sequence \(a,b\), reduction modulo \(b\)
and cancellation of \(a\) give \(G\in b\mathcal A\).
Write \(G=bt\). Cancellation of \(b\) then gives
\[
\boxed{\quad G=bt,\qquad H=-at,\qquad t\in\mathcal A.\quad}
\tag{8}
\]
This is division inside the actual ring, not just in its fraction
field. It is the new polynomial element forced by faithful flatness.

Both \(G,H\) have derivation degree at most three: \(r\) has
degree one and \(z,w\) have degree at most two. Since \(b\)
is invariant and nonzero, (8) implies \(D^4t=0\). Moreover
\[
D^3G=\epsilon D^3(rz)
     =3\epsilon pD^2z
     =3\epsilon^2bp^2.
\]
Consequently
\[
D^3t=3\epsilon^2p^2\ne0.
\tag{9}
\]

Each full quadratic divisor model has third image \(p^2R_{(\pi)}\),
with local units absorbed. One can check this on its basis
\(1,T,Y,TY\), where \(DT=p\), \(DY=2T\) and
\(pY=T^2-\eta\): the third derivative of \(TY\) is \(6p^2\).
Thus every member of \(D^3(F_3)\subset R\) is divisible by
\(p^2\) at every height-one prime of \(R\). The UFD
intersection contracts this to \(D^3(F_3)\subset p^2R\).
Together with (9), this proves
\[
\boxed{\quad I_3R=p^2R,\qquad F_3=F_2\oplus Rt.\quad}
\tag{10}
\]
For the splitting, subtract the appropriate invariant multiple of
\(t\) from any member of \(F_3\), using (9); the remainder is
in \(F_2\). The sum is direct because \(D^3t\ne0\).

## 3. The new derivative and its closed-fiber constant

Differentiate \(bt=G\) and use (2)–(6). Direct cancellation,
followed by eliminating \(r^2\) through (4), gives
\[
\begin{split}
Dt={}&\epsilon Q
 +\epsilon\bigl(a(e+2d)+3bf\bigr)z\\
 &+\epsilon\bigl(-3ac-b(d+2e)\bigr)w
 +2(cf-de).
\end{split}
\tag{11}
\]
For example the cancellation can be done first in \(bDt=DG\),
then in the domain \(\mathcal A\); it does not invert \(b\)
in the conclusion. In particular
\[
\overline{Dt}=2\overline{cf-de}
\quad\text{in }\mathcal A/\mathfrak n\mathcal A.
\tag{12}
\]
The residue determinant is independent of the decompositions in
(6). Two representations of an element of \((a,b)\) differ
by a multiple of the syzygy \((b,-a)\), so their coefficient
vectors agree modulo \(\mathfrak n\). Equivalently, it is the
determinant of the two classes of \(B_1,B_2\) in the basis
\(a,b\) of \(J/\mathfrak nJ\).

## 4. A unit determinant makes the cubic presentation exact and flat

Suppose \(cf-de\in R^*\). Set \(S=R[Z,W,T]\), interpret
\(r=aZ+bW\) in (7), and put
\[
I=(bT-G,\ aT+H)\subset S.
\tag{13}
\]
There is a surjection \(S/I\to K=R[z,w,t]\subset\mathcal A\).
We verify its kernel, rather than assuming these two relations are
a presentation.

At every height-one prime of the base, one of \(a,b\) is a
unit. Eliminate \(T\) using the corresponding equation in
(13). The remaining equation is exactly the conic (4), because
\(aG+bH\) is that conic polynomial. The previously proved
height-one equality of the conic ring therefore gives
\[
(S/I)_{(\pi)}=K_{(\pi)}=\mathcal A_{(\pi)}.
\tag{14}
\]
The same generic calculation gives \((S/I)_L=L[r]\), a domain.

No minimal prime over \(I\) can contract to a height-one base
prime: after that localization (14) is a domain in which the
base prime remains nonzero. Nor can one contract to \(\mathfrak n\).
Indeed the two equations modulo \(\mathfrak n\) are
\[
2\bar e Z-2\bar c W+\bar q=0,
\qquad -2\bar f Z+2\bar d W-\bar h=0.
\tag{15}
\]
Their coefficient determinant is a nonzero constant. Hence
\(I+\mathfrak nS\) has height four in \(S\), whereas a
minimal prime of a two-generated ideal has height at most two.
All minimal primes consequently contract to zero, and the generic
domain gives a unique one, of height two.

The ring \(S\) is regular. The two generators of \(I\)
form a regular sequence: in the UFD \(S\), height two excludes
a common prime factor. Thus \(S/I\) is Cohen–Macaulay and has
no embedded primes. It is reduced at its unique minimal prime
by its generic localization. These facts make it a domain and
prove the exact presentation \(K=S/I\). The standard
regular-sequence and associated-prime facts used here are recorded
in Stacks [02JN](https://stacks.math.columbia.edu/tag/02JN) and
[0BUS](https://stacks.math.columbia.edu/tag/0BUS).

Equation (15) now gives the full closed fiber
\[
K/\mathfrak nK\simeq\mathbb C[T].
\tag{16}
\]
At a prime of this fiber, its ambient inverse image in \(S\)
has height four or five, according as the fiber prime is generic
or closed. Quotienting the regular sequence of length two gives
\(\dim K_{\mathfrak q}=2+\dim(K_{\mathfrak q}/\mathfrak nK_{\mathfrak q})\).
The base local ring is regular and the total local ring is
Cohen–Macaulay, so miracle flatness applies. Its exact statement
and full proof were directly read in
[Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4).
At the other base primes, flatness already follows from (14).
Therefore \(K\) is flat over \(R\).

The elementary flat-module height-one intersection from the
[flat-conic note, Section 2](flat-conic-topology-gate-pass47.md)
now applies to \(K\). Since \(K\subset\mathcal A\) and
they agree in (14), it forces
\[
K=\mathcal A.
\tag{17}
\]
This is a proved generation statement only under the unit
determinant premise, not a general Hartogs assertion for subalgebras.

## 5. The actual topological exclusion and exact remaining boundary

Equations (12), (16), (17) give a full reduced affine-line
quotient fiber with nonzero constant induced derivation. The
[intrinsic pointwise plinth criterion](intrinsic-pointwise-plinth-pass47.md)
puts it outside the primitive plinth support. But
\(p=aB_1+bB_2\in\mathfrak n\). This contradiction proves
\[
\boxed{\quad cf-de\in\mathfrak n,\qquad
D(F_3)\subset\mathfrak nF_3.\quad}
\tag{18}
\]
The second assertion follows from (11), the earlier
\(D(F_2)\subset\mathfrak nF_2\), and (10).

In particular, at every reduced obstruction point \(J=\mathfrak n\),
the third image is principal and the first-jet matrix of
\(B_1,B_2\) in regular parameters \(a,b\) has rank at most
one. More generally Sections 2–5 apply whenever \(B_1,B_2\in J\);
the forbidden unit determinant is equivalent by Nakayama to
\((B_1,B_2)=J\). Without this coefficient premise at a nonreduced
point, the construction has not supplied the same cubic element.

When the determinant is not a unit, the special fiber of the
two-equation candidate may have dimension at least two. The
minimal-prime and flatness arguments above no longer apply; no
equality \(R[z,w,t]=\mathcal A\) is asserted. Nor does
\(D(F_3)\subset\mathfrak nF_3\) say that \(D\) vanishes on
the entire closed fiber: higher degree elements may still move.
These are the remaining dependencies, not an exclusion of all
second-image basepoints or a cancellation theorem. All pass-47
files remain unchanged; no journal or historical novelty claim
is attached to this bounded deduction.

## Finite verification boundary

The standalone [three-method checker](third_image_cubic_gate_checks_pass48.py)
tests the exact cubic derivatives and relation preservation,
generic elimination and the unit-determinant closed equations,
and rank-deficient and missing-coefficient negative controls.
These formal coefficient models are not asserted to satisfy the
actual polynomial-cylinder and divisor-cover hypotheses.

The completed run passed all three methods in 0.114 seconds,
exit zero. The initial run had one harness error: a Groebner basis
inferred over the integers was asked to reduce rational coefficients.
Selecting its exact rational coefficient field fixed the harness;
no mathematical formula or assertion was changed. Only `unittest`
and SymPy are imported. No finite test verifies the regular-sequence,
flatness or topological arguments for all inputs.
