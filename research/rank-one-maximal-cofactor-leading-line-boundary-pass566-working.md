# Maximal rank-one cofactors give a common leading line, not entry

**Status: bounded necessary restriction and an actual equality control.**

In an actual all-positive sliced complex four-ring with initial rank
one and total degree S greater than four, every coordinate partial
attaining the rank-one cofactor upper bound has its leading field
on the same line over the invariant fraction field. If there is an
attaining partial, there are at least two. The other, nonattaining
leading fields are not asserted to lie on that line.

This is compatible with the entire actual coordinate identities.
An explicit translation frame of degrees (2,2,2,2) attains all four
bounds, with exact shifts (3,3,3,3). The total-degree-four boundary
instead admits leading rank three and is treated separately.
These controls are not globally degree-minimal. No coordinate-entry,
recognition, novelty or cancellation conclusion is claimed.

## 1. Actual hypotheses and the attaining subset

Retain the all-positive actual setup of
[158](arbitrary-positive-weight-initial-bound-pass158-working.md)
and
[562](rank-sensitive-cofactors-and-rank-one-semigroup-boundary-pass562-working.md):
\[
\begin{gathered}
B=\mathbb C[X_1,X_2,X_3,X_4]=A[u],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\quad Eu=1,\quad A=\ker E,\\
K=\operatorname{Frac}A,\qquad
d_i=\deg_E X_i\ge1,\quad S=\sum_i d_i,\\
X_i=c_i u^{d_i}+b_i u^{d_i-1}+\text{terms of smaller degree},
\qquad c_i\in A\setminus\{0\},\quad b_i\in A,\\
\operatorname{trdeg}_{\mathbb C}
 \mathbb C[c_1\eta^{d_1},\ldots,c_4\eta^{d_4}]=1.
\end{gathered}
\tag{1}
\]
Here eta is independent and b_i may vanish. When d_i=1, b_i is
the constant term. The slice u is not assumed to be an ambient
coordinate. No polynomial presentation of A is assumed.

For the ACTUAL partials T_i=partial_{X_i}, use the exact shifts
and leading fields proved in158, together with the rank-one bound
of562:
\[
\begin{gathered}
0\le k_i\le L_i:=S-d_i-3,\qquad
0\ne N_i=[u^{k_i}]T_i|_A\in\operatorname{LND}(A),\\
\deg_uT_i(u)\le k_i,\qquad
\deg_E T_i(f)\le\deg_E f+k_i\quad(T_i(f)\ne0),\\
N_i(c_j)=0\quad\text{for every }i,j,\qquad
\mathcal J=\{i:k_i=L_i\}.
\end{gathered}
\tag{2}
\]
The exact horizontal shift is the maximum degree of T_i(a) over
nonzero images of a in A. In particular its leading field is
nonzero, not merely an upper-bound symbol. Every L_i is nonnegative
because the other three degrees are positive. Unless Section6 says
otherwise, assume S>4.

The assertion to be proved is conditional on mathcal J being
nonempty. If it is empty, this source draws no leading-line
conclusion. It does not assume all four partials attain the bound.

## 2. Full normalized rows and the determinant coefficient

Choose a separating transcendence basis xi1,xi2,xi3 of K/C, and
extend its partials through the finite separable field extension.
The actual-volume argument of158 gives
\[
M=\frac{\partial(X_1,X_2,X_3,X_4)}
        {\partial(\xi_1,\xi_2,\xi_3,u)},\qquad
\det M=J_0\in K^*,\qquad
\widetilde M=M\operatorname{diag}(1,1,1,u),\quad
\det\widetilde M=uJ_0.
\tag{3}
\]
The independence of J0 from u follows from the actual flow of E,
not from a formal matrix ansatz. These field derivatives need not
preserve A.

The top row vectors of the rescaled matrix have rank one by (1)
and the characteristic-zero differential-rank calculation in562.
Their last components d_i*c_i are nonzero. Set gamma_i=d_i*c_i.
There is a common row v in K to the fourth, with last component
one, for which
\[
\begin{aligned}
\gamma_i^{-1}\widetilde M_i
 &=u^{d_i}v+u^{d_i-1}z_i+\text{degree at most }d_i-2,\\
v&=\frac{(\partial_{\xi_1}c_i,\partial_{\xi_2}c_i,
                \partial_{\xi_3}c_i,d_i c_i)}{\gamma_i},\\
z_i&=\frac{(\partial_{\xi_1}b_i,\partial_{\xi_2}b_i,
                \partial_{\xi_3}b_i,(d_i-1)b_i)}{\gamma_i}.
\end{aligned}
\tag{4}
\]
The expression for v is independent of i. A negative remainder
degree means that the remainder is zero. Dividing rows by gamma_i
is a field calculation, not an actual coordinate transformation.
No weighted root or rationality assumption on K is used.

One may factor u to the d_i from each row in K((u inverse)).
Subtract the first normalized row from the other three. The exact
coefficient at total degree S-3 of the determinant, after division
by the product of the gamma_i, is
\[
v\wedge(z_2-z_1)\wedge(z_3-z_1)\wedge(z_4-z_1).
\tag{5}
\]
Equivalently, expand the complete polynomial rows. A term with two
top rows vanishes because they are proportional. Terms with no
top row have degree at most S-4. Thus only one top row and three
first-lower rows contribute to (5); no omitted lower coefficient
can contribute at that degree.

Since S>4, the exponent S-3 is greater than one. Equation (3)
therefore makes (5) zero. In the quotient K^4/Kv, put
\[
V_1=\operatorname{span}_K
 \{\overline{z_2-z_1},\overline{z_3-z_1},
                  \overline{z_4-z_1}\},\qquad \dim_K V_1\le2.
\tag{6}
\]
This conclusion concerns first-lower differential rows. It is not
an assumption about ranks of the N_i.

## 3. Maximal three-cofactors lie on one line

For any three indices i,j,k in their chosen order, the degree
d_i+d_j+d_k-2 coefficient of their normalized three-row wedge is
\[
v\wedge(z_j-z_i)\wedge(z_k-z_i).
\tag{7}
\]
The same expansion justifies (7): its only possible contributors
are one top row and two first-lower rows. The unnormalized wedge
has the additional nonzero factor gamma_i*gamma_j*gamma_k.

Fix an omitted index ell and put R_ell=S-d_ell. A horizontal
cofactor of M uses the other three rows and contains the last
column. Its rescaled counterpart is u times that cofactor.
Thus a nonzero coefficient at degree L_ell=R_ell-3 in a horizontal
entry of T_ell is exactly a nonzero corresponding component at
degree R_ell-2 in (7), multiplied by the three retained gamma
factors, divided by J0 and with its cofactor sign.
The field chain rule identifies this with the coefficient N_ell
on K. Nonvanishing on K is equivalent to nonvanishing on some
element of A: otherwise the quotient rule would kill all of K.

Consequently, if mathcal J is nonempty, at least one wedge (7)
is nonzero. This forces dim V1=2. Hence
\[
\mathcal W=\operatorname{span}_K
 \{v,z_2-z_1,z_3-z_1,z_4-z_1\}
 \quad\text{has dimension three}.
\tag{8}
\]
Every wedge (7) belongs to the one-dimensional space Lambda^3 W.
Their cofactor dual vectors are therefore proportional over K.

The component deleting the last column deserves a separate check.
That cofactor contains only horizontal columns, so rescaling does
not change its numerator. A nonzero degree R_ell-2 coefficient
would give T_ell(u) that degree. But
\[
\deg_u T_\ell(u)\le k_\ell\le R_\ell-3.
\tag{9}
\]
Thus this component of every maximal wedge is zero. In particular
the common nonzero cofactor dual direction in (8) is horizontal;
its horizontal projection is not zero. It follows that
\[
\boxed{\dim_K\operatorname{span}_K\{N_i:i\in\mathcal J\}=1
                 \quad\text{if }\mathcal J\ne\varnothing.}
\tag{10}
\]
Here derivations are extended to K. For a nonattaining index all
horizontal components of its wedge (7) vanish, and (9) kills its
remaining component, so that particular maximal wedge is zero.
Its actual nonzero N_i comes from LOWER coefficients. No assertion
places that lower field on the line in (10).

## 4. Whole commutation and E recombination

The whole actual identities impose further exact restrictions.
For f in A, the coefficient at u to the k_i+k_j in
[T_i,T_j](f)=0 is
\[
[N_i,N_j](f)=0.
\tag{11}
\]
Indeed, horizontal lower coefficients contribute lower degree.
When a partial differentiates a power of u, (2) makes the degree
at most k_i+k_j-1. This also covers k_i=k_j=0, where the relevant
power derivative is zero. Thus all four leading fields commute,
whether or not they attain the upper bounds.

If mathcal J is nonempty, choose j0 in it and N=N_j0. Equation
(10) gives nonzero lambda_i in K with N_i=lambda_i*N for i in
mathcal J, taking lambda_j0=1. Equation (11) then gives
\[
N(\lambda_i)=0,\qquad \lambda_i\in(K^N)^*,
\quad K^N:=\{q\in K:Nq=0\}.
\tag{12}
\]
This is invariance of rational coefficients in the exact field.
It does not make them complex or make a quotient coordinate.

Because the T_i are the complete actual coordinate partials,
there is an identity of derivations on the WHOLE ring
\[
E=\sum_{i=1}^4 E(X_i)T_i.
\tag{13}
\]
Apply it to A, on which E is zero. For an attaining i the largest
possible degree of E(X_i)T_i|A is d_i-1+k_i=S-4, with coefficient
d_i*c_i*N_i. A nonattaining i contributes degree at most S-5.
Thus comparison of the exact degree S-4 coefficient proves
\[
\boxed{\sum_{i\in\mathcal J}d_ic_iN_i=0.}
\tag{14}
\]
Every displayed d_i*c_i is nonzero and every N_i is nonzero.
In particular
\[
\boxed{\mathcal J=\varnothing\quad\text{or}\quad|\mathcal J|\ge2.}
\tag{15}
\]
For nonempty mathcal J, (12),(14) also give the relation
sum_{i in J} d_i*c_i*lambda_i=0 in K^N, because N kills every
c_i by (2). Relations (10),(12),(14) are compatible with each
other; they are not a contradiction to an actual sliced frame.

## 5. An actual all-maximal degree-(2,2,2,2) control

Start with B=C[a,b,c,u] and E=partial_u. Set
\[
A_1=a+u^2,\qquad C_1=c+au,\qquad B_1=b+cu,
\tag{16}
\]
and take the supplied coordinates
\[
X_1=A_1,\quad X_2=A_1+B_1,\quad X_3=A_1+C_1,
\quad X_4=A_1+B_1+C_1+u.
\tag{17}
\]
Their complete polynomial inverse is
\[
\begin{aligned}
u&=X_4-X_2-X_3+X_1,\\
a&=X_1-u^2,\\
c&=X_3-X_1-au,\\
b&=X_2-X_1-cu.
\end{aligned}
\tag{18}
\]
Each right side uses only preceding recovered quantities.
Substituting (17) into (18) recovers a,b,c,u. Conversely, (18)
gives A1=X1, B1=X2-X1 and C1=X3-X1, and recovers X4 from its
first equation. Thus both inverse orders are polynomial identities.
The original-coordinate Jacobian determinant is one.

All four degrees are two, with c_i=1. The entire initial kernel is
(mathsf X2-mathsf X1, mathsf X3-mathsf X1, mathsf X4-mathsf X1):
the quotient is C[mathsf X1], and its map to C[eta squared] is
injective. Hence the initial rank is exactly one and S=8.

Differentiating the full inverse gives the following complete
actual partial table, in the original a,b,c,u variables:

| Partial | T_i(a) | T_i(b) | T_i(c) | T_i(u) |
| --- | --- | --- | --- | --- |
| T1 | 1-2u | au-c-2u^3+u^2+u-1 | -a+2u^2-u-1 | 1 |
| T2 | 2u | -au+c+2u^3+1 | a-2u^2 | -1 |
| T3 | 2u | -au+c+2u^3-u | a-2u^2+1 | -1 |
| T4 | -2u | au-c-2u^3 | -a+2u^2 | 1 |

The maximum horizontal degree is three in every row and is attained
on b. The derivation rule bounds every image of C[a,b,c] by three.
The last column has degree zero, so the rule on its polynomial
extension in u gives the exact all-ring shifts as well. Therefore
\[
\begin{gathered}
(d_1,d_2,d_3,d_4)=(2,2,2,2),\qquad
(k_1,k_2,k_3,k_4)=(3,3,3,3),\\
k_i=S-d_i-3\quad\text{for all }i,\qquad
(N_1,N_2,N_3,N_4)=(-2,2,2,-2)\partial_b.
\end{gathered}
\tag{19}
\]
The table satisfies every T_i(X_j)=delta_ij, every commutator
[T_i,T_j]=0 and the entire identity (13). In particular
sum_i d_i*c_i*N_i=2*(-2+2+2-2)*partial_b=0.
The first-lower coefficients of (17) are 0,c,a,a+c+1. Their
normalized difference rows modulo the common top row have rank
two, exactly as in (6)--(8).

This control rules out a universal strict improvement of the four
rank-one cofactor bounds from these actual identities alone.
It does NOT rule out a stronger statement under global degree
minimality: its recovered u in (18) is an actual degree-one
coordinate, and the original invariant coordinates are also
explicit. The supplied frame is not a minimum.

### A nonattaining field need not lie on that line

A second actual translation makes the attaining-subset distinction
explicit. In the same original ring, put
\[
X_1=a+u,\quad X_2=b+u,\quad X_3=c+u,
\quad X_4=u+X_1X_2.
\tag{20}
\]
The full inverse is U=X4-X1X2, u=U, a=X1-U, b=X2-U, c=X3-U.
Both substitution orders are immediate polynomial identities. The
entire partial table, allowing the displayed actual X1,X2 as
abbreviations, is

| Partial | T_i(a) | T_i(b) | T_i(c) | T_i(u) |
| --- | --- | --- | --- | --- |
| T1 | 1+X2 | X2 | X2 | -X2 |
| T2 | X1 | 1+X1 | X1 | -X1 |
| T3 | 0 | 0 | 1 | 0 |
| T4 | -1 | -1 | -1 | 1 |

Here d=(1,1,1,2), S=5, the initial coefficients are all one,
and the initial rank is one. The exact shifts are (1,1,0,0),
while the upper bounds are (1,1,1,0). Thus mathcal J={1,2,4}.
Writing D=partial_a+partial_b+partial_c, the leading fields are
\[
(N_1,N_2,N_3,N_4)=(D,D,\partial_c,-D).
\tag{21}
\]
The nonattaining N3 is not a K-multiple of D. The attaining
relation (14) is D+D-2D=0. This is another nonminimal actual
frame, not a claim about a hypothetical minimizing frame.

## 6. Why total degree four is different

If S=4, positivity forces every d_i=1. The exponent S-3 in (5)
is then one, and det(Mtilde)=uJ0 does not make its coefficient
vanish. The missing cancellation can really occur.

In C[a,b,c,u] with E=partial_u, take
\[
(X_1,X_2,X_3,X_4)=(a+u,b+u,c+u,u).
\tag{22}
\]
The inverse is u=X4, a=X1-X4, b=X2-X4, c=X3-X4. All degrees
are one, all initial coefficients are one, and the full initial
rank is one. The actual partials are
\[
\begin{aligned}
T_1&=\partial_a,&T_2&=\partial_b,&T_3&=\partial_c,\\
T_4&=\partial_u-\partial_a-\partial_b-\partial_c.
\end{aligned}
\tag{23}
\]
They all have exact horizontal shift zero, attaining
S-d_i-3=0. Their leading fields on A are
partial_a, partial_b, partial_c and -partial_a-partial_b-partial_c,
which have rank three over K. The recombination relation (14)
still holds, but the proportionality statement (10) does not.
This is the explicit reason for retaining S>4 in the theorem.

## 7. Remaining boundary and verification

For the abstract degree tuple (4,5,6,7) in562, the assigned maximal
shifts (15,14,13,12), if attained by an actual frame, would therefore
require all four leading fields to lie on the single invariant-ratio
line described above. This source neither realizes nor excludes
that maximal-shift assignment. Its degree-(2,2,2,2) control is not
silently substituted for it.

The coefficient at S-3 and the maximal three-cofactors are only
part of the whole Jacobian identity. Lower determinant coefficients,
lower terms in the coordinate-partial equations, regularity on the
actual invariant ring and an actual polynomial coordinate inverse
are still required to construct a proposed frame. Conversely,
proportional leading fields do not supply a coordinate shear or a
completion theorem. No generic differential matrix or abstract
monomial-curve embedding is promoted to actual coordinates.

The target was checked absent before creation, and the full writing
guide was read. Complete158 was freshly reread through EOF in865c5f;
562 is the author's separately held rank-sensitive proof. Fresh
unsaved8cbdcb checked both inverse orders in (17),(18), the full
partial table, all sixteen coordinate pairings, all commutators,
the entire E recombination, the Jacobian determinant and all exact
degrees and shifts. Fresh4bc826 separately checked both inverse
orders, the entire partial table, all coordinate pairings, full
E recombination and exact degrees and shifts of (20),(21).
The wedge proof and the attaining-subset
argument are supplied universally above, not inferred from that
example. Independent saved-source review is still required.

Only this source was created. No earlier source or canonical record
was edited. No saved checker was executed, imported or compiled.
There is no novelty, arbitrary coordinate-entry, degree-minimum
classification, or unrestricted cancellation claim.
