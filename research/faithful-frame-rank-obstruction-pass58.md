# A whole quadratic-generator repair family fails the actual frame equations

The faithful minimum-three control cannot acquire the required
actual-frame compatibility merely by an invertible change of its two
good generators and regular quadratic additions in the fixed bad
pair. The full good-column identities would force that change matrix
to have determinant divisible by \(a^2\), contradicting invertibility.

There is also a direct actual Jacobian and adjoint check. A simple
addition repairs the earlier pointwise rank defect and makes the two
accelerations independent, but the corresponding true local good
partial has nonzero second adjoint. Thus repairing one Jacobian value
does not repair the full frame condition.

## 1. The actual ring and the repair family

Retain the complete faithful control of
[pass57](faithful-quadratic-slice-boundary-pass57.md):
\[
R=\mathbb C[a,v]_{(a,v-1)},\quad L=\mathbb C(a,v),\qquad
\mathcal B=R[t,z,s]/(t^2-v-az),\quad E=\partial_s.
\tag{1}
\]
This is an invariant localization of the actual polynomial ring
\(\mathbb C[a,t,z,s]\), with \(v=t^2-az\). Define
\[
w=as+tz,\quad q=ts+z^2,\quad X=w,\quad Y=vw+t,
\quad T=Y-vX=t.
\tag{2}
\]
The actual ring is \(R[X,Y,z,q]\). Generically,
\[
z=\frac{T^2-v}{a},\qquad
q=\frac{XT}{a}-\frac{v(T^2-v)}{a^2},\qquad
EX=a,\quad EY=av.
\tag{3}
\]
Only \(v\), not \(a\), is a unit in \(R\).

Consider the entire explicit family
\[
\binom{Q_1}{Q_2}
=M(a,v)\binom{z}{q}+\binom{P_1(X,Y)}{P_2(X,Y)},
\qquad M\in\operatorname{GL}_2(R),\quad
P_i\in R[X,Y]_{\le2}.
\tag{4}
\]
Every such list still generates \(\mathcal B\) over \(R\):
subtract the known \(P_i\) and apply \(M^{-1}\) to recover
\(z,q\). Its good generators remain generically quadratic and
have time degree at most two. This includes arbitrary regular
base-dependent coefficients in \(M\) and in the quadratic additions.
It does not identify these generators with ambient coordinates.

## 2. The necessary actual good-column identities

Write \(f=a\), \(g=av\). These are algebraically independent and
generate the field \(L\). If a list in (4), with the fixed bad
pair \((X,Y)\), realized the complete independent-defect degree-two
frame of [the generic bad-pair theorem](generic-bad-pair-pass44.md),
its accelerations \(h_i=E^2Q_i\) would satisfy
\[
(f\partial_f+g\partial_g)h_i=2h_i,
\qquad
(Q_i)_2=\frac14
\begin{pmatrix}X&Y\end{pmatrix}
\operatorname{Hess}_{f,g}(h_i)
\binom{X}{Y}.
\tag{5}
\]
Here \((Q_i)_2\) is the homogeneous quadratic part over \(L\).
These are equations (9) and (14) of that proof. Their derivation
uses the true good coordinate partials and their adjoint bounds
to make the Schur complement independent of flow time. They are
not consequences of generic quadraticity alone.

The common field in this application cannot enlarge \(L\)
algebraically inside \(L(X,Y)\): the latter is a purely
transcendental extension, in which \(L\) is relatively algebraically
closed. Thus the displayed base derivatives have the same exact
meaning for a hypothetical full-frame realization with these speeds.

In the variables \((X,T)\), write the coefficient of \(X^2\)
in \(P_i\) as \(c_i(a,v)\in R\). Since \(ET=0\),
\(EX=a\), \(E^2z=E^2q=0\), one has
\[
h_i=2a^2c_i(a,v).
\tag{6}
\]
The Euler operator in (5) is \(a\partial_a\), with \(v\)
fixed. Its first equation therefore forces \(\partial_a c_i=0\).
Consequently
\[
c_i\in\mathbb C(v)\cap R
=\mathbb C[v]_{(v-1)}.
\tag{7}
\]
The equality follows by cancelling a rational function of \(v\)
and checking its valuation at \(v-1\). Differentiation in \(v\)
preserves this ring.

For any such \(c=c(v)\), direct differentiation gives
\[
\frac14(X,Y)\operatorname{Hess}_{f,g}
\bigl(2f^2c(g/f)\bigr)\binom{X}{Y}
=cX^2+c'XT+\frac{c''}{2}T^2.
\tag{8}
\]
All three coefficients belong to \(R\). In particular the actual
frame identities would make each quadratic coefficient regular at
the divisor \(a\).

## 3. Exact pole cancellation forces a nonunit determinant

Let a row of \(M\) be \((m_1,m_2)\). Its contribution from
\(m_1z+m_2q\) to the quadratic part in \((X,T)\) is
\[
\frac{m_2}{a}XT+
\frac{am_1-vm_2}{a^2}T^2.
\tag{9}
\]
The coefficients of the added polynomial \(P_i\) are already
regular. Therefore (8)--(9) require
\[
m_2\in aR,\qquad am_1-vm_2\in a^2R.
\tag{10}
\]
These are exact ideal conditions, retaining the second power of
the denominator. They are equivalent to
\[
(m_1,m_2)=(ak+vn,an)\quad\text{for some }k,n\in R.
\tag{11}
\]
If both rows satisfy them, then
\[
M=
\begin{pmatrix}k_1&n_1\\k_2&n_2\end{pmatrix}
\begin{pmatrix}a&0\\v&a\end{pmatrix},
\qquad
\det M=a^2(k_1n_2-n_1k_2).
\tag{12}
\]
This contradicts \(M\in\operatorname{GL}_2(R)\).

The row module in (11) has a direct algebraic interpretation:
\[
az=T^2-v,\qquad vz+aq=XT.
\tag{13}
\]
It is exactly the set of regular coefficient combinations of
\(z,q\) whose generic quadratic poles disappear. The necessary
frame identities force both good rows into that module, while
an invertible recovery of the two original good generators
cannot do so.

Thus no member of (4) satisfies the complete necessary frame
identities (5). In particular, no member realizes the target
independent-defect actual adjoint frame with this bad pair.
This is a fixed-family obstruction, not a classification of all
possible new bad pairs or all nonlinear generator changes.

## 4. Independent accelerations and a repaired local Jacobian

For an arbitrary constant \(c\in\mathbb C\), take the member
\[
Q_1=z+ca+X^2,\qquad Q_2=q+Y^2.
\tag{14}
\]
Now
\[
h_1=2a^2=2f^2,\qquad h_2=2a^2v^2=2g^2,
\quad
\det\frac{\partial(h_1,h_2)}{\partial(a,v)}=16a^3v\ne0.
\tag{15}
\]
Thus the accelerations have rank two. Nevertheless (5) would
require the respective quadratic parts to be just \(X^2,Y^2\).
The additional terms in (3) violate that requirement.

There is also a direct check using the actual ambient Jacobian,
without assuming any converse to the graph theorem. In original
coordinates \((a,t,z,s)\), restrict to the entire line
\(a=0,t=1,z=0\). The Jacobian of \((Q_1,Q_2,X,Y)\) is
\[
J(s)=
\begin{pmatrix}
c&0&1&0\\
2s&s+2&2&1\\
s&0&1&0\\
s&1&1&0
\end{pmatrix},\qquad \det J(s)=s-c.
\tag{16}
\]
All these points survive the invariant localization. When
\(s\ne c\), the genuine rational dual field to the first good
generator is regular near that point. Its coefficient column,
restricted to this line, is
\[
\widetilde T_1\big|_{\mathrm{line}}
=\frac1{c-s}\partial_a-\frac{s}{c-s}\partial_z.
\tag{17}
\]
Since the actual \(E\) is \(\partial_s\), its adjoints on
coefficient columns are ordinary \(s\)-derivatives. Restriction
to this line commutes with them. Hence
\[
[E,[E,\widetilde T_1]]\big|_{\mathrm{line}}
=\frac{2}{(c-s)^3}(\partial_a-c\partial_z)\ne0.
\tag{18}
\]
This is a true local dual partial, not a formal matrix column
declared to be an action. No local-nilpotence claim on a
non-invariant Jacobian open is needed for the calculation.

For \(c=1\), the point \((0,1,0,0)\) now has determinant
\(-1\), repairing the particular rank defect in pass57. Its
second good adjoint is still nonzero. For every \(c\), the
point of the same line with \(s=c\) also shows that this
particular four-function list is not globally an ambient
coordinate frame.

## 5. Verification and exact remaining boundary

The generic bad-pair proof was reread in full for the necessary
Euler and Hessian identities used here. The ring, slice, faithful
flatness, and all-slices minimum-three result are inherited from
pass57. The change (4) keeps the bad pair and its entire slice-gauge
coset fixed; it does not construct a full-frame example.

[The two-method exact checker](faithful_frame_rank_checks_pass58.py) verifies the Hessian
transformation and coefficient-module determinant certificate,
then the actual polynomial Jacobian, accelerations, and nonzero
second adjoint in (14)--(18). These are reusable symbolic identity
controls, not a proof by bounded parameter search or a realization
of the missing full frame. Both methods passed in 0.162 seconds,
exit zero. The initial harness used structural equality for two
equivalent but differently simplified expressions; those comparisons
were normalized before the successful run. No mathematical formula
changed.
An independent full proof and checker audit was clean; its separate
two-method rerun passed in 0.157 seconds, exit zero. The audit caught
one missing display-spacing backslash, which was corrected without
changing any formula.

The obstruction leaves changes of the bad pair, more general
nonlinear generator changes, and the original unrestricted
frame-selection problem open. It supplies no cancellation
counterexample or universal affine-slice theorem.
