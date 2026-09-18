# A polynomial divisibility gate for dependent high-flow defects

With one primitive defect direction, the high-flow companion matrix has
dimension five, but its last row is no longer constant. The full image
line still forces a constant direction for a nonconstant highest flow
vector. Primitivity then clears a denominator in its commutator with
the original action. The remaining differential identity contains an
extra derivative of the defect multipliers, so the earlier common-power
conclusion cannot simply be copied.

This is a restricted reduction, not a recognition theorem for the
entire dependent-defect sector. The zero-commutator branch is recognized;
the nonzero polynomial multiplier remains an explicit obligation.

## 1. Actual hypotheses and the weighted companion

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND
with a polynomial slice, and let \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad \operatorname{ad}_E^3T_3=
\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Suppose the two nonzero quadratic defects have fraction-field rank one.
The [primitive decomposition](dependent-quadratic-defects-pass42.md)
gives
\[
V_3=aD,\quad V_4=bD,\qquad
D\text{ primitive and locally nilpotent},\qquad
a,b\in\ker E\cap\ker D,\quad [E,D]=0.
\tag{2}
\]
If \(a,b\) have a nontrivial complex constant relation, the earlier
constant-frame reduction already recognizes the original sliced action.
Assume below that they are complex-linearly independent. In particular
both are nonzero. Primitivity in (2) means polynomial coefficient gcd
one, not a unit coefficient ideal.

Put
\[
P=Ex,\quad J=\operatorname{Jac}P,\quad d=D(x),\quad
\ell=(0,0,a,b),\qquad
M=\begin{pmatrix}J&-d/2\\\ell&0\end{pmatrix}.
\tag{3}
\]
The actual conjugated partials have coefficient matrix
\[
C(t)=I-tJ+\frac{t^2}{2}d\ell,
\quad C(t)^{-1}=\operatorname{Jac}(\exp(tE)x),
\quad \det C(t)=1.
\tag{4}
\]
Schur elimination gives \(\det(I-tM)=1\). Thus, over
\(K=\operatorname{Frac}B\),
\[
M^5=0,\qquad
(M^j)_{\rm UL}=\frac{\operatorname{Jac}(E^jx)}{j!}.
\tag{5}
\]
No derivative of \(\ell\) is used in this pointwise matrix
identity. Because \(d\ne0\) and \(\ell\ne0\), neither
kernel of \(M\) contains a nonzero vector supported only on
its one-dimensional auxiliary coordinate. Consequently the same
rank-preserving block argument as in
[the full-image proof](two-quadratic-top-line-pass42.md) applies:
if \(MN=NM=0\), the upper-left block and \(N\) have the
same rank.

In particular \(E^5x\) is constant and \(E^6x=0\).
This is a flow-time bound, not a bound on polynomial coefficient degree.

## 2. The nonconstant highest vector has a good constant direction

Let \(m\) be the last nonzero coordinate iterate, put
\(h=E^mx\), \(z=E^{m-1}x\), and suppose \(m\ge3\)
and \(h\) is nonconstant. Then \(m\in\{3,4\}\).
Block descent gives \(M^{m+1}=0\) and \(M^m\ne0\).
There is one Jordan block of size \(m+1\); all others have
total size \(4-m<m\). Therefore
\[
\ker M\cap\operatorname{im}M^{m-1}
=\operatorname{im}M^m
\quad\text{is one-dimensional}.
\tag{6}
\]
Set \(\rho=\ell z\). The actual velocity and base-column
identities are
\[
M^{m-1}\binom{P}{0}
=\frac1{(m-1)!}\binom{h}{(m-1)\rho},
\qquad
(M^m)_{\text{base columns}}
=\frac1{m!}\binom{\operatorname{Jac}h}{m\ell\operatorname{Jac}z}.
\tag{7}
\]
The lower row is \(m\ell\operatorname{Jac}z\), not
\(m\operatorname{Jac}(\ell z)\).

The highest coefficients of \(C(t)E(\exp(tE)x)=P\) give
\[
\ell h=0,\qquad Jh=\frac{m-1}{2}\rho d.
\tag{8}
\]
They show that the first vector in (7) is nonzero and killed by
\(M\), hence spans the line in (6). Every differential column
of \(h\) is consequently proportional to \(h\). All ordinary
partials kill every rational ratio of its nonzero components. Their
common constant field is \(\mathbb C\), so
\[
h=cq,\qquad 0\ne c\in\mathbb C^4,\qquad
q\in\ker E\setminus\mathbb C.
\tag{9}
\]
Equation \(\ell h=0\) says \(a c_3+b c_4=0\).
Complex-linear independence of \(a,b\) therefore forces
\(c_3=c_4=0\). The constant direction
\(T_c=c_1T_1+c_2T_2\) is genuinely good in the original frame.

## 3. Primitivity removes a commutator denominator

The top bad-column coefficients give \(D h=0\), so \(Dq=0\).
Write \(W_i=[E,T_i]\). The next coefficients give
\[
V_i z=-\frac2m W_i h=-\frac2m c\,W_iq
\quad(i=3,4).
\tag{10}
\]
Since one multiplier in (2) is nonzero, this puts \(Dz\) in
the field line \(Kc\). It is actually \(ct\) for some
\(t\in B\), by choosing a nonzero constant component of \(c\).
Thus \(D\rho=(D\ell)z+\ell Dz=0\), since \(D\ell=0\)
and \(\ell c=0\). Also \(E\rho=\ell h=0\).

Now (8)--(9) give the polynomial vector identity
\[
q Jc=\frac{m-1}{2}\rho d.
\tag{11}
\]
For every irreducible \(\pi\) dividing \(q\), some component
of the primitive vector \(d\) is not divisible by \(\pi\).
Taking the valuation of that component in (11) proves
\(v_\pi(\rho)\ge v_\pi(q)\). Hence
\[
q\mid\rho\text{ in }B,\qquad r:=\rho/q\in\ker E\cap\ker D,
\qquad [E,T_c]=-\frac{m-1}{2}rD.
\tag{12}
\]
This is a polynomial commutator formula, with all repeated factors
retained. It does not require the coefficients of \(D\) to generate
the unit ideal.

If \(r=0\), then \(T_c\) commutes with \(E\). A constant
linear change within the original good plane retains a second good
partial. The original slice and the
[one-good-output-partial recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
then give an invariant ambient coordinate and polynomial original
kernel. This conclusion does not require a constant relation between
the two bad defects.

### A nonzero commutator forces two independent actions

The full matrix also supplies an exact trace identity. Retain the
polynomial \(t\) defined by \(Dz=ct\). Since
\((M^{m-1})_{\rm UL}=\operatorname{Jac}z/(m-1)!\), the upper-right
column of \(M^m=M^{m-1}M\) is
\(-ct/[2(m-1)!]\). Its image is the line already determined in
(7), with direction \((c,(m-1)r)^{\mathsf t}\). Thus the entire
matrix, including the auxiliary column, is
\[
M^m=\frac1{m!}
\binom{c}{(m-1)r}
\begin{pmatrix}dq&-mt/2\end{pmatrix}.
\tag{12a}
\]
Here \(dq\) is the row of the four ordinary partial derivatives.
Taking the trace of this nilpotent matrix gives
\[
T_cq=\frac{m(m-1)}2\,rt.
\tag{12b}
\]

If \(E,D\) were fraction-field dependent, then \(D=\kappa E\)
for some \(\kappa\in\mathbb C^*\). Indeed the original slice
makes the coefficient ideal of \(E\) the unit ideal, and both
\(E,D\) have polynomial coefficient gcd one. Writing the rational
ratio in reduced form and comparing prime factors on both sides
forces its numerator and denominator to be units of \(B\).
Consequently \(Dz=\kappa Ez=\kappa cq\), so \(t=\kappa q\).
Equation (12b) would make \(T_cq\) divisible by \(q\).
For an LND on a characteristic-zero domain, a polynomial dividing
its own derivative must have derivative zero: otherwise its LND
degree drops by one under differentiation but cannot drop under
multiplication by a nonzero polynomial. Apply this to the actual
constant partial \(T_c\). It gives \(T_cq=0\), and (12b) then
forces \(r=0\).

Therefore the remaining \(r\ne0\) branch necessarily has
\(\operatorname{rank}_{\operatorname{Frac}B}(E,D)=2\).
The parallel branch is already recognized by the zero-\(r\) gate.
This argument neither makes \(D\) nice nor gives it a slice, and
does not recognize the independent branch. It is an all-degree
consequence of the full matrix and original slice, not an additional
finite-test claim.

## 4. The exact variable-row remainder

Comparison of the auxiliary components in (7) gives
\[
m q\,\ell\,d z=(m-1)\rho\,dq.
\tag{13}
\]
Since \(d\rho=\ell\,dz+z_3\,da+z_4\,db\), substitution
of \(\rho=qr\) yields
\[
r\,dq+m q\,dr=m(z_3\,da+z_4\,db).
\tag{14}
\]
Here \(d\) in (13)--(14) is the ordinary polynomial
differential, not the coefficient vector \(D(x)\) from (3).
Every identity holds for each of the four actual ambient partials.

The extra right side cannot be omitted merely because \(a,b\)
are invariant under \(E\) and \(D\). Invariance under those
two fields does not make their ordinary differentials zero.
For example, formal one-variable data
\[
q=t,\quad r=1,\quad
a=(m-1)/m,\quad b=t/m,\quad z_3=t,\quad z_4=1
\tag{15}
\]
satisfy \(\rho=qr=\ell z\), (13), and (14), but
\(\rho^m/q^{m-1}=t\) is nonconstant. These are only formal
coefficient data, not a claimed realization of the frame. They show
why the differential equation by itself does not give the previous
common-power conclusion.

The nonzero-\(r\) branch, the constant highest-vector cases, and
flow degrees below three are not recognized by this note. No global
coordinate conclusion follows just from (12)--(14).

## 5. A genuine cubic boundary control

Take independent coordinates \((u,v,A,C)\), put
\(G=v^2+1\), and define
\[
E=v\partial_A+G\partial_C,\qquad
s=C-vA,\qquad R=GA-vC.
\]
The actual inverse is \(A=R+vs\), \(C=vR+Gs\), with
\(Es=1\) and \(\ker E=\mathbb C[u,v,R]\).
Set \(F=(A^3+C^3)/6\) and take the actual frame
\[
x_1=(u+F+v)/2,\quad x_2=(u+F-v)/2,
\quad x_3=A,\quad x_4=C.
\tag{16}
\]
Its polynomial inverse is
\(u=x_1+x_2-(x_3^3+x_4^3)/6\), \(v=x_1-x_2\).
The good partials pull back to \(\partial_u\pm\partial_v\),
and the other two to
\(\partial_A-A^2\partial_u/2\),
\(\partial_C-C^2\partial_u/2\).
Direct brackets give the exact profile \((1,1,2,2)\) and
\[
V_3=-v^2\partial_u,\qquad
V_4=-G^2\partial_u.
\tag{17}
\]
Their primitive common direction is the constant partial
\(D=\partial_u\); their multipliers have no constant relation.
Moreover
\[
E^3x=cq,\quad E^4x=0,\qquad
c=(1/2,1/2,0,0)^{\mathsf t},\quad q=v^3+(v^2+1)^3,
\quad \rho=r=0.
\tag{18}
\]
This nonconstant \(q\) is not a cube: it is squarefree, since a
common zero of \(q,q'\) would require \(v=1\) or \(-1\),
where \(q\) equals nine or seven. Equivalently direct polynomial
gcd calculation gives \(\gcd(q,q')=1\).

The example is in the recognized zero-\(r\) branch. It does not
realize the unresolved nonzero-\(r\) alternative. It supplies
actual inverse and flow controls, rather than an arbitrary matrix
pretending to be a polynomial action.

## Verification boundary

The general proof consists of the actual companion identities,
image-line argument, primitive valuation argument and corrected
differential identity. The independent
[five-method checker](dependent_defect_top_line_checks_pass43.py)
passed its first run in 0.297 seconds. It reconstructs the actual
two-sided inverses, exact heights, full companion velocity rows and
non-cube boundary; separate formal controls check the variable-row
remainder and primitive valuation mechanism without a unit-ideal
assumption. Finite controls test only these identities and boundary
data. They do not prove
universal frame existence, recognition of every dependent-defect
action, or general cancellation. No novelty or external expert-review
claim is made.
