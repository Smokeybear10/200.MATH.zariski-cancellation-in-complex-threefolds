# A rank-three non-affine extension and its affine-frame boundary

## 1. What is established

This source gives a sliced extension of a primary-sourced irreducible
rank-three LND of \(\mathbb C^{[3]}\) with two precise properties.
First, no slice is affine in the selected extension variable \(t\),
even though a positive grading makes the two components commute and
be homogeneous. Second, no positive affine-linear coordinate frame
has an actual \(E\)-degree-weighted Euler field of shift at most one.
Among those affine-linear frames the minimum Euler shift is exactly
two, and a displayed actual frame attains it.

The positive grading giving commuting components has weights
\((1,1,1,8)\), not the actual \(E\)-degrees. This distinction is
essential. The example therefore belongs to the general-positive-
grading common-kernel setting of589, but it is not an example in
the actual first-shift setting of587 merely by using those weights.
Nonlinear polynomial coordinate changes are not classified here.

The explicit slice below is not proved to be an ambient coordinate,
and the kernel of the extended derivation is not proved polynomial
or nonpolynomial. A polynomial inverse on a proper local-slice
subring is not promoted to an automorphism of the whole fourfold.
No cancellation or novelty claim is made.

## 2. Exact primary rank-three input and complete polynomials

Let \(R=\mathbb C[x,y,z]\), and put
\[
 f=xz-y^2,\qquad r=x^5+yf^2,\qquad
 g=zf^4+2x^4yf^2+x^9,\qquad xg=f^5+r^2,
 \qquad H=\operatorname{Jac}(f,g,\cdot).
\tag{1}
\]
The Jacobian convention is the determinant whose successive rows
are the gradients of \(f,g\), and the argument.
This is precisely the family member \(E(2,2,F)\),
\(F(t_1,t_2)=t_1^4\), in
[Dasgupta--Gaifullin, Theorem 5.7, version 2](https://arxiv.org/html/2306.00510v2).
The family construction, the full proof of that theorem, and the
local-slice statement in Theorem 2.17 were read. They give
\[
 H\text{ irreducible and locally nilpotent},\qquad
 \operatorname{rank}H=3,\qquad
 S:=\ker H=\mathbb C[f,g],\qquad Hr=-gf^2.
\tag{2}
\]
The parameters satisfy the stated conditions \(m\ge2,n\ge1\)
and \(F(t_1,0)\notin\mathbb C\). The kernel conclusion uses
Theorem 2.17(c) and the irreducibility proved in the family theorem.
These are explicitly retained primary results, not an inference from
the absence of a particular triangular form or a new proof of the
external rank theorem.

The complete field in (1) has components
\[
 \begin{aligned}
 Hx&=-2rf^2,\\
 Hy&=-g+10x^4r,\\
 Hz&=18x^8y+2x^6z^3+12x^5y^2z^2-30x^4y^4z+16x^3y^6.
 \end{aligned}
\tag{3}
\]
In particular it has ordinary homogeneous derivation degree eight;
\(f,r,g\) have ordinary degrees two, five and nine. Direct
calculation verifies \(Hf=Hg=0\), the last identity of (2), and
every polynomial identity in (1) and (3).

Set \(B=R[t]\) and define
\[
 \psi=-fgr,\qquad J=f^3g^2,\qquad
 E=H+(1+\psi)\partial_t,\qquad L=\partial_t.
\tag{4}
\]
Here \(H\psi=J\ne0\) and \(HJ=0\). The extension is an LND:
it restricts to the LND \(H\) on \(R\), and
\(Et=1+\psi,E^2t=J,E^3t=0\). Local nilpotence on all
four generators proves local nilpotence on \(B\).

## 3. A polynomial slice, with a subring-only inverse

The following general identity explains the slice. Suppose a
derivation on a domain kills \(a,b\) and sends \(r\) to
\(a^2b\). On adjoining \(t\), give it the value
\(1+abr\) on \(t\). Then set
\[
 v=at-r^2/2,\qquad q=abv-r,
 \qquad u=t-brv+\frac{ab^2}{2}v^2.
\tag{5}
\]
Entire differentiation, without division by \(a\), gives
\[
 Ev=a,\qquad Eq=0,\qquad Eu=1,
 \qquad au=v+q^2/2,
 \qquad \partial_tu=1+abq.
\tag{6}
\]
For example \(Ev=a(1+abr)-r(a^2b)=a\);
the two nonconstant contributions to \(Eu\) cancel after
\(Er=a^2b\) and \(Ev=a\) are inserted.

Apply (5) with \(a=f,b=-g\). All of its expressions are actual
polynomials in \(R[t]\), and they prove that (4) has a slice.
Thus, for \(A=\ker E\), the slice theorem gives \(B=A[u]\).
No polynomial presentation of \(A\) follows from that statement
alone.

There is an exact inverse on the smaller ring \(S[r,t]\):
\[
 v'=au-q^2/2,\qquad
 r=abv'-q,\qquad
 t=u-bqv'+\frac{ab^2}{2}(v')^2.
\tag{7}
\]
The formulas (5) and (7) compose to the identity in both orders.
They fix \(S\), and the determinant for the two displayed variables
is \(-1\). The element \(r\) is transcendental over
\(\operatorname{Frac}S\), since \(Hr\ne0\), so \(S[r,t]\)
really is a polynomial extension of \(S\). However it is not the
whole ring \(R[t]\) merely because both rings have the same
transcendence degree. In fact \(S[r]=R\) would make \(f,g,r\)
actual coordinates and contradict \(\operatorname{rank}H=3\),
so this subring is proper. Formula (7) is not claimed to provide inverse
images of \(x,y,z\) in the whole ring. This is the precise limit
of the subring calculation.

## 4. No slice affine in the selected t

Suppose \(\alpha t+\beta\), with \(\alpha,\beta\in R\),
were an \(E\)-slice. The full coefficient equations would be
\[
 H\alpha=0,\qquad H\beta+\alpha(1-fgr)=1.
\tag{8}
\]
By (2), \(\alpha\in\mathbb C[f,g]\). In ordinary homogeneous
degree zero, the second equation forces \(\alpha_0=1\), since
\(H\) raises degree by eight and kills constants. In degree
sixteen it forces
\[
 H(\beta_8)+\alpha_{16}-fgr=0,
 \qquad \alpha_{16}=c f^8\quad(c\in\mathbb C).
\tag{9}
\]
The second assertion follows from \(\deg f=2,\deg g=9\):
\(2i+9j=16\) with nonnegative integers has only \((i,j)=(8,0)\).
No homogeneity of the entire proposed \(\alpha\) or \(\beta\)
has been assumed.

Here is an exact coefficient obstruction to (9). On homogeneous
degree-sixteen polynomials define
\[
 \begin{aligned}
 \Lambda(P)={}&243[y^{15}z]P+32[xy^{13}z^2]P
       +19[x^4y^{12}]P\\
       &+4[x^5y^{10}z]P+3[x^9y^7]P.
 \end{aligned}
\tag{10}
\]
Using the entire field (3), its exact values are
\[
 \Lambda(H(x^iy^jz^k))=0\quad(i+j+k=8),
 \qquad \Lambda(f^8)=0,\qquad \Lambda(fgr)=-30.
\tag{11}
\]
There are forty-five monomials in the first assertion, spanning all
of \(R_8\). One finite way to verify it is to insert (3) in
\(i x^{i-1}y^jz^k Hx+jx^iy^{j-1}z^k Hy+
kx^iy^jz^{k-1}Hz\) and take the five specified coefficients.
Thus (11) is a complete linear functional certificate on \(R_8\),
not a search over a selection of proposed slices.
Applying it to (9) is a contradiction.

There is therefore no affine-in-\(t\) slice at all, including the
constant-in-\(t\) case. In particular no \(Q\in R\) has
\(E(t-Q)\in\mathbb C^*\). The slice (5) has exact \(t\)-degree
two, with nonzero coefficient \(a^3b^2/2=f^3g^2/2\). Its minimum
\(t\)-degree is exactly two. This is a rank-three version of the
same-frame obstruction in591; it is not a proof concerning the
extended kernel's polynomiality.

## 5. Actual degrees and the two different Euler fields

The actual \(H\)-degrees of \(x,y,z\) are \((2,10,18)\).
For a direct verification, work over the coefficient field
\(K=\mathbb C(f,g)\). In \(K[r]\) the identities (1) give
\[
 x=(f^5+r^2)/g,\qquad
 y=(r-x^5)/f^2,\qquad
 z=(g-2x^4yf^2-x^9)/f^4.
\tag{12}
\]
All three lie in this polynomial ring, and
\(H=-gf^2\partial_r\) there. Their degrees are two, ten and
eighteen: the last numerator has leading contribution
\(2x^9-x^9=x^9\). These field calculations compute degrees only;
they are not ambient coordinate changes. Since \(E|_R=H\),
and \(E^2t=J\ne0,E^3t=0\), the degrees of \((x,y,z,t)\)
are \((2,10,18,2)\).

An actual positive frame attaining a particularly simple Euler field
is
\[
 (X_1,X_2,X_3,X_4)=(x+z,y+z,z,t),
 \qquad d=(18,18,18,2).
\tag{13}
\]
Its entire inverse is
\(x=X_1-X_3,y=X_2-X_3,z=X_3,t=X_4\).
Write \(Z=x\partial_x+y\partial_y+z\partial_z\) and
\(V=\psi\partial_t\). Its actual Euler field and exact brackets
are
\[
 \begin{gathered}
 D_*=18Z+2t\partial_t,\qquad E=L+H+V,\\
 [D_*,L]=-2L,\qquad [D_*,H]=144H,
 \qquad [D_*,V]=286V,\\
 \operatorname{ad}_E^2(D_*)=-142J\partial_t\ne0,
 \qquad \operatorname{ad}_E^3(D_*)=0.
 \end{gathered}
\tag{14}
\]
Here \([H,V]=J\partial_t\), and \(L\) commutes with both.
The bracket convention is \([P,Q]=PQ-QP\).

These equations give exact whole-ring Euler shift two. In \(A[u]\),
the last equation bounds the \(u\)-degrees of \(D_*(A)\) and
\(D_*(u)\) by two. The nonzero terminal field
\(-142J\partial_t\) is not a multiple of \(E\) over
\(\operatorname{Frac}B\), since \(H\ne0\). It cannot vanish
on all of \(A\), since a derivation of \(A[u]\) vanishing on
\(A\) is a multiple of \(E=\partial_u\). Thus some element
of \(A\) has image under \(D_*\) of \(u\)-degree two, proving
the claimed exact shift.

By contrast the separately weighted positive Euler field
\[
 G=Z+8t\partial_t
\tag{15}
\]
makes \(P=H+V\) homogeneous of weight eight and \(L\) homogeneous
of weight minus eight. These two LNDs commute. The sum \(P\) is
locally nilpotent by its restriction to \(H\) and its finite
iterates on \(t\). One has
\[
 [E,G]=8L-8P=16L-8E,
 \qquad \operatorname{ad}_E^2G=0.
\tag{16}
\]
Its exact \(E\)-filtration shift is one, by the same argument
with a nonparallel terminal field. Thus the general positive-grading
commuting hypothesis of589 is met. However \(G\) is not the Euler
field weighted by the actual degrees of its displayed coordinates,
which are those in (12)--(13), not \((1,1,1,8)\).

## 6. Complete affine-linear double-commutator classification

We now prove a stronger obstruction than failure of (13) alone.
For every affine-linear polynomial derivation \(\mathcal T\) of
\(\mathbb C[x,y,z,t]\),
\[
 \operatorname{ad}_E^2\mathcal T=0
 \quad\Longleftrightarrow\quad
 \mathcal T=kG+d\partial_t\quad\text{for }k,d\in\mathbb C.
\tag{17}
\]
This includes all twenty coefficients of an affine-linear vector
field, without a diagonal or semisimple assumption.

Write \(\mathbf x=(x,y,z)^T\) and decompose those coefficients as
\[
 \mathcal T(\mathbf x)=M\mathbf x+t\mathbf v+\mathbf w,
 \qquad \mathcal T(t)=ct+\ell+d,
 \qquad \ell=\ell_xx+\ell_yy+\ell_zz.
\tag{18}
\]
Here \(M\) is a constant matrix and all other displayed coefficients
are complex. The ordinary degree-thirty-one part of the
\(\partial_t\) coefficient of \(\operatorname{ad}_E^2\mathcal T\)
is exactly \(-2\psi\,\mathbf v(\psi)\). It comes from twice
bracketing with \(V=\psi\partial_t\); no term involving \(H\)
or \(L\) has that degree. Since \(\psi\ne0\), its vanishing
implies \(\mathbf v(\psi)=0\). Three exact coefficients of this
last polynomial are
\[
 [y^{15}]\mathbf v(\psi)=v_z,\quad
 [x^7z^8]\mathbf v(\psi)=-v_y,\quad
 [y^{13}z^2]\mathbf v(\psi)=-7v_x.
\tag{19}
\]
They force \(\mathbf v=0\).

Put \(T_0=M\mathbf x+\mathbf w\) as a derivation of \(R\).
After that deduction, the entire double commutator has base and
vertical parts
\[
 \begin{aligned}
 (\operatorname{ad}_E^2\mathcal T)|_R&=[H,[H,T_0]],\\
 (\operatorname{ad}_E^2\mathcal T)(t)&=
 H^2\ell+cH\psi-2H(T_0\psi)+T_0(H\psi).
 \end{aligned}
\tag{20}
\]
There are no omitted moving coefficients in this formula. The
constant \(d\partial_t\) commutes with \(E\).

The base expression splits into ordinary polynomial component
degrees seventeen, from \(M\mathbf x\), and sixteen, from
\(\mathbf w\). The latter vanishes only if \(\mathbf w=0\).
Explicit coefficient witnesses, listing the vector component first,
are

| Component and monomial of \([H,[H,\mathbf w]]\) | Coefficient |
| --- | --- |
| \(x;\ x^8z^8\) | \(2w_z\) |
| \(y;\ x^8y^2z^6\) | \(12w_x\) |
| \(y;\ y^{14}z^2\) | \(-16w_y\) |

For the linear part, use entries \(m_{ij}\) with the first index
denoting the output component. Eight necessary coefficient equations
are obtained directly from the whole field (3):

| Component and monomial of \([H,[H,M\mathbf x]]\) | Coefficient |
| --- | --- |
| \(x;\ x^9z^8\) | \(2m_{zx}\) |
| \(z;\ x^{10}z^7\) | \(2m_{zy}\) |
| \(z;\ x^9z^8\) | \(24m_{xy}\) |
| \(z;\ x^{11}z^6\) | \(-24m_{xz}\) |
| \(x;\ x^{11}z^6\) | \(12m_{yx}-8m_{zy}\) |
| \(y;\ y^{14}z^3\) | \(8m_{xy}-16m_{yz}\) |
| \(z;\ x^{11}y^2z^4\) | \(1080(m_{xx}-m_{zz})\) |
| \(z;\ x^6y^7z^4\) | \(2400(m_{xx}-m_{yy})\) |

Thus \(M=kI\). Conversely the entire base double commutator
vanishes for \(M=kI\), since \([Z,H]=8H\). These coefficient
equations therefore describe the full solution, not only a
numerically sampled nullspace.

The vertical expression in (20) now reduces exactly to
\[
 H^2\ell+(c-8k)J.
\tag{21}
\]
Its first term has ordinary degree seventeen and the second degree
twenty-four. The former has coefficient witnesses
\[
 [y^{16}z]H^2\ell=2\ell_x,\quad
 [x^{10}z^7]H^2\ell=-10\ell_y,\quad
 [x^{11}y^2z^4]H^2\ell=24\ell_z.
\tag{22}
\]
Hence \(\ell=0\), and \(J\ne0\) gives \(c=8k\).
This proves the forward implication in (17). Its converse follows
from (16) and \([E,\partial_t]=0\).

## 7. No affine-linear actual frame has shift at most one

First recall why an actual locally finite positive Euler field of
\(E\)-filtration shift at most one satisfies
\(\operatorname{ad}_E^2D=0\). For shift zero this follows directly
from \(D(A)\subseteq A\) and \(\deg_uD(u)\le1\).
For shift one, write
\(D|_A=M_0+uN_0\) and \(D(u)=b_2u^2+b_1u+b_0\).
The nonzero top degree-one derivation on \(A[\eta]\) is locally
nilpotent: otherwise its iterates would give unbounded
\(E\)-degrees in the finite-dimensional orbit of a polynomial
under the actual Euler field. This top derivation sends \(\eta\)
to \(b_2\eta^2\), so \(b_2=0\). The elementary fact used here
is that an LND on a characteristic-zero domain cannot send a
nonzero element to a nonzero multiple of itself, as follows by
additivity of the LND degree on products. Thus the entire
double commutator vanishes. Negative shift is impossible for an
actual Euler field with all actual coordinate degrees positive,
since it sends each such coordinate to a nonzero scalar multiple
of itself.

Now let \(F_1,\ldots,F_4\) be any affine-linear polynomial
coordinate frame with \(d_i=\deg_EF_i>0\), and let
\(D_F=\sum_i d_i F_i\partial_{F_i}\). It is an affine-linear
derivation in \((x,y,z,t)\). If its shift were at most one, (17)
would give \(D_F=kG+d\partial_t\).

The linear part of this positive Euler field has eigenvalues
\(k,k,k,8k\). In particular \(k\) is a positive integer, since
the eigenvalues are the actual positive integer degrees \(d_i\).
There must be a coordinate of weight \(8k\), and its affine
eigenspace is
\[
 \mathbb C\left(t+\frac{d}{8k}\right).
\tag{23}
\]
This follows by comparing the \(x,y,z,t\) and constant
coefficients of the eigen-equation; \(k\ne0\) and \(8k\ne k\).
Every nonzero element in (23) has exact \(E\)-degree two. Hence
the actual weight assignment would require \(8k=2\), contradicting
\(k\in\mathbb Z_{>0}\). The case \(k=0\) was already excluded
by the positive eigenvalues, not silently divided out.

This proves the claimed obstruction for every positive affine-linear
frame, including translations. Frame (13) attains shift two, so the
minimum over this class is exactly two. It is not a minimum theorem
over all polynomial coordinate frames.

## 8. Exact boundary and verification record

The source supplies a rank-three non-affine-slice extension for the
general positive-grading commuting case, and a sharp obstruction to
putting this candidate into actual first shift by affine-linear
reframing. It does not answer whether a nonlinear polynomial frame
can do so, whether the explicit \(u\) is an ambient coordinate,
or whether \(\ker E\) is polynomial. The subring inverse (7) is
expressly insufficient for any of those conclusions.

The earlier extension note and591 already distinguish same-frame
gauge failure from recognition. The present base is the different
primary family member (1), not the earlier \(E(2,1,t_1^2)\).
No theorem for that fixed older base is transferred to this one.
No old non-affine-slice counterexample or external rank theorem is
being presented as a new discovery.

Fresh unsaved algebra reconstructs the whole Jacobian field, all
local-slice and universal slice identities, both subring inverse
orders, and the full commutators for both Euler fields. It checks
the functional (10) on all forty-five degree-eight basis monomials,
and all entries of the affine-classification coefficient tables.
The tables and complete formula (20) are proof certificates for
arbitrary affine coefficients, not a grid search over frames.

No saved checker was executed, imported or compiled. No canonical
file was edited, and no unfinished source was read. Final hold is
reported separately only after a complete author EOF reread and
exact hash, for further independent saved-source review.
