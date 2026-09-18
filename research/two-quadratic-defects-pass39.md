# Two quadratic defects at the next height boundary

This note treats a genuine new profile beyond the saved height-nine
recognition theorem: two ambient partials have adjoint height at most
one, and two at most two. With two independent quadratic defect fields,
the inverse-flow Jacobian has a six-dimensional nilpotent linearization.
Its highest coefficient has Jacobian rank at most one in flow degrees
at least three,
but at flow degree two it necessarily has Jacobian rank two.

An explicit sliced polynomial cylinder realizes that latter case with
the exact profile (1,1,2,2). Its highest coefficient vector does not
define an LND, even though its coefficients generate the unit ideal.
Thus the earlier rank-one highest-coefficient recognition strategy
cannot be extended to this whole profile by asserting the same rank
bound or by normalizing the highest vector.

This is an obstruction to a proposed proof mechanism, not a
counterexample to cancellation. The displayed example has an explicit
polynomial quotient. No general height-ten recognition theorem is
proved here.

## 1. Actual frame and defect assumptions

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\ne0\) be an LND, and put
\(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2 T_i=0\ (i=1,2),\qquad
\operatorname{ad}_E^3 T_i=0\ (i=3,4).
\tag{1}
\]
Write \(P=E(x)\), \(J=\operatorname{Jac}P\), \(h_r=E^r(x)\), and
\[
V_i=\operatorname{ad}_E^2T_i\quad(i=3,4),\qquad
\mathcal V=[\,V_3(x)\mid V_4(x)\,],\qquad
L_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix}.
\tag{2}
\]
The extra assumption for this note is
\(\operatorname{rank}_{\operatorname{Frac}B}\mathcal V=2\).
All matrix ranks and Jordan arguments below are over that fraction field.
The constant selector \(L_0\) is not a derivation or a quotient ring.

The highest coefficients in the actual conjugated partials are LNDs.
Repeated application of \(\operatorname{ad}E\) to their zero brackets
shows that
\[
E,\ [E,T_1],\ [E,T_2],\ V_3,\ V_4
\tag{3}
\]
are mutually commuting LNDs, with zero allowed except where
independence was explicitly required. This assertion does not include
the middle coefficients \([E,T_3]\) and \([E,T_4]\).

## 2. The six-dimensional linearization

Let \(F_t=\exp(tE)x\). The coefficient matrix of the four conjugated
partials is
\[
C(t)=I-tJ+\frac{t^2}{2}\mathcal V L_0,\qquad
\operatorname{Jac}(F_t)C(t)=I,\qquad \det C(t)=1.
\tag{4}
\]
Indeed the good columns are \(T_i+t[E,T_i]\), and the other columns
add \(t^2V_i/2\). Applying them to the actual coordinates \(F_t\)
gives the inverse-Jacobian identity. The determinant of a polynomial
flow is one: it is a unit in \(\mathbb C[x,t]\) and specializes to
one at t=0.

Define
\[
\mathcal M=
\begin{pmatrix}
J&-\mathcal V/2\\
L_0&0
\end{pmatrix}.
\tag{5}
\]
Schur elimination over \(\operatorname{Frac}B(t)\) gives
\(\det(I-t\mathcal M)=\det C(t)=1\). Therefore
\[
\mathcal M^6=0,\qquad
(\mathcal M^r)_{\rm upper\ left}=
\frac{1}{r!}\operatorname{Jac}h_r \quad(r\ge1).
\tag{6}
\]
The second identity follows by comparing the upper-left block of
\((I-t\mathcal M)^{-1}\), which is \(C(t)^{-1}\), with the
Jacobian of the actual polynomial flow. It does not assume that
an arbitrary matrix satisfying the determinant identity comes from
an LND.

In particular \(\operatorname{Jac}h_6=0\), so \(h_6\) is constant
and \(h_7=0\). Every actual flow in this class has time degree at
most six. This is not an ordinary coefficient-degree bound.

## 3. A rank-preserving block lemma

Let \(K=\operatorname{Frac}B\), and split \(K^6=K^4\oplus K^2\).
The right and left kernels of \(\mathcal M\) contain no nonzero
vector or row supported on the auxiliary \(K^2\):
\[
\mathcal M(0,z)=(-\mathcal V z/2,0),\qquad
(0,z^{\mathsf t})\mathcal M=(z^{\mathsf t}L_0,0).
\tag{7}
\]
This uses the rank-two assumption on \(\mathcal V\) and the
independence of the two rows of \(L_0\).

**Block lemma.** If a six-by-six matrix N satisfies
\(\mathcal M N=N\mathcal M=0\), then its upper-left four-by-four
block has exactly the same rank as N.

To prove it, projection onto the first four coordinates is injective
on \(\ker\mathcal M\), by (7). It is therefore injective on
\(\operatorname{im}N\). Also every row of N lies in the left
kernel of \(\mathcal M\). Restricting those rows to the first
four entries is injective, again by (7). Thus deleting the last
two columns of N preserves rank, and projecting the resulting
image onto the first four rows preserves rank. Their composition
is exactly its upper-left block.

In particular, if \(\mathcal M^{r+1}=0\), then
\[
\operatorname{rank}(\mathcal M^r)_{\rm upper\ left}
=\operatorname{rank}\mathcal M^r.
\tag{8}
\]
This is stronger than a rank-one outer-product argument.

## 4. The exact highest-coefficient dichotomy

Let m be the highest index with \(h_m\ne0\). Since all later
Jacobian blocks vanish, repeated application of (8), starting
with \(\mathcal M^6=0\), gives
\(\mathcal M^{m+1}=0\) whenever m is at most five.
Consequently (6) and (8) identify the rank of \(\operatorname{Jac}h_m\)
with the rank of \(\mathcal M^m\).

For m at least three, a nilpotent six-by-six matrix with blocks
of size at most m+1 has at most one block of size m+1. It follows
that
\[
m\ge3\quad\Longrightarrow\quad
\operatorname{rank}\operatorname{Jac}h_m\le1.
\tag{9}
\]
The case m=6 has zero Jacobian directly.

For m=2, the same descent gives \(\mathcal M^3=0\).
Independently, \(\operatorname{rank}\mathcal M\ge4\): its
restriction to the auxiliary plane has rank two and zero bottom
coordinates, and two base vectors can have independent bottom
coordinates through \(L_0\).
A square matrix of size six with cube zero has rank at most four.
Equality forces exactly two Jordan blocks of size three. Hence
\[
m=2\quad\Longrightarrow\quad
\mathcal M\text{ has Jordan type }(3,3),\qquad
\operatorname{rank}\operatorname{Jac}h_2=2.
\tag{10}
\]
The rank-two conclusion uses the block lemma, not just the rank
of the full six-dimensional matrix.

The case m=1 is impossible under the rank-two defect assumption.
It would give \(\mathcal M^2=0\), hence rank at most three,
contradicting rank at least four.

For later use there are exact top-coefficient identities. Define
\(\ell=L_0h_{m-1}\). Comparing the highest powers in
\(C(t)P(F_t)=P\) and \(C(t)\operatorname{Jac}(F_t)=I\) gives
\[
L_0h_m=0,\qquad E(\ell)=0,\qquad
Jh_m=\frac{m-1}{2}\mathcal V\ell,\qquad
J\operatorname{Jac}h_m=
\frac m2\mathcal V\operatorname{Jac}\ell.
\tag{11}
\]
The first identity uses injectivity of \(\mathcal V\).
These equations do not assert that \(h_m\cdot\partial_x\)
is locally nilpotent or that its coefficients are coordinates.

## 5. A genuine sliced realization of the rank-two residual

Start with physical coordinates \((a,b,c,d)\), and define
\[
u=b-a^2/2,\qquad v=d-c^2/2,\qquad g=uv-1,
\]
\[
E=u\partial_a+au\partial_b+g\partial_c+cg\partial_d.
\tag{12}
\]
The coordinates \((u,v,a,c)\) are polynomial, with inverse
\(b=u+a^2/2,\ d=v+c^2/2\). In them,
\[
E=u\partial_a+g\partial_c,\qquad E(u)=E(v)=0.
\]
Thus E is locally nilpotent. It has the actual slice and invariant
\[
s=va-c,\qquad r=ga-uc=us-a,\qquad E(s)=1,\quad E(r)=0.
\tag{13}
\]
The inverse presentation is
\[
a=us-r,\qquad c=gs-vr,\qquad
b=u+(us-r)^2/2,\qquad d=v+(gs-vr)^2/2.
\tag{14}
\]
These are both-sided polynomial inverses, proving
\(\ker E=\mathbb C[u,v,r]\). No cancellation theorem is
used to recognize this example.

Order the displayed ambient frame as
\((x_1,x_2,x_3,x_4)=(b,d,a,c)\). In the intermediate
coordinates \((u,v,a,c)\), its partials are
\[
T_1=\partial_u,\quad T_2=\partial_v,\quad
T_3=\partial_a-a\partial_u,\quad
T_4=\partial_c-c\partial_v.
\tag{15}
\]
Their exact adjoint heights are (1,1,2,2). The nonzero highest
commutators are
\[
[E,T_1]=-\partial_a-v\partial_c,\quad
[E,T_2]=-u\partial_c,\quad
V_3=2u(\partial_a+v\partial_c),\quad
V_4=2ug\partial_c.
\tag{16}
\]
The last two fields have generic rank two. In the ordered physical
frame the highest coefficient is
\[
h_2=(u^2,g^2,0,0)^{\mathsf t}.
\tag{17}
\]
Its Jacobian rank is two: in the independent variables u,v,
the determinant for the first two entries is \(4u^2g\ne0\).
This realizes (10) with a genuine sliced action, not a formal
matrix pencil or an arbitrary highest-vector ansatz.

The adjoint heights here also equal the shifted slice-filtration
degrees. At their highest orders the commutators in (16) act
nontrivially on the invariant r: their values are respectively
1, \(u^2\), \(-2u\), and \(-2u^2g\). Therefore the horizontal
leading coefficient reaches each stated order, and this is an
actual height-ten profile, not just an upper bound.

## 6. Why highest-vector normalization cannot close this branch

The field defined by (17), in physical coordinates, is
\[
U=u^2\partial_b+g^2\partial_d.
\]
It satisfies \(U(u)=u^2\), hence
\[
U^n(u)=n!u^{n+1}\ne0\quad(n\ge1).
\tag{18}
\]
So U is not locally nilpotent. Its coefficients even generate
the unit ideal, since \(uv-g=1\) and
\[
u^2(v^2-2v^2g)+g^2(3+2g)=1.
\tag{19}
\]
Thus passing to a primitive coefficient vector changes nothing.
The original E has a slice and a unit derivative ideal as well.

The example does not refute the existence of a better coordinate
frame; (14) supplies one explicitly. It refutes automatic
rank-one highest coefficients and automatic quasi-translation or
LND behavior of the highest vector at this next profile. A
general proof must use additional coordinate information.

## Dependencies and verification scope

The inverse-Jacobian construction extends the identities already
proved for one quadratic column in
[the completed height-nine report](../deep-pass-13.md).
The two-column rank-preserving lemma and the realized (3,3)
residual are proved above by elementary linear algebra and
explicit polynomial identities. No new external classification
is needed for these deductions.

The [independent exact checker](two_quadratic_defects_checks_pass39.py)
tests the displayed realization, coordinate inverses, defects and matrix
identities. Its six methods passed in the first run in 1.039 seconds,
and in separate reruns in 1.100 and 1.068 seconds. The complete
[separate proof audit](two-quadratic-defects-audit-pass39.md) reconstructs
the universal conditional argument. The finite tests cannot verify
universal frame existence, all
matrix quantifiers, novelty or general cancellation. The written
argument supplies those stated universal conditional deductions;
human expert review and proof-assistant verification remain absent.
