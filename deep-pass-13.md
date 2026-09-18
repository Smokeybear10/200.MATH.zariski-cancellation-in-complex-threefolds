# Mixed commutators and rational denominator descent

The mixed four-variable problem closes under the slice hypothesis.
Constant highest coefficients and nonzero coefficient-curve corrections
give invariant coordinates. The remaining power-law cases close by an
explicit quadratic shear or by rational denominator descent to a
polynomial two-variable action.

This is a restricted recognition result, not a solution of complex
threefold cancellation. No argument makes an arbitrary slice derivation
satisfy these mixed commutator conditions. The proved slice-filtration
threshold increases from eight to nine; no universal threshold or
decreasing coordinate operation is known from this argument.

## 1. Question and exact scope

The working cancellation question is
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]
The corrected complex-threefold interpretation of the supplied
conjecture has not been confirmed by its proposer. All assertions here
are over \(\mathbb C\); neither the dimensional typo in the original
statement nor positive-characteristic counterexamples settle this
working question.

Write \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be a nonzero locally
nilpotent derivation, and put \(T_i=\partial_{x_i}\). The hypothesis is
\[
\operatorname{ad}_E^2(T_i)=0\quad(i=1,2,3),\qquad
\operatorname{ad}_E^3(T_4)=0.
\tag{1}
\]
Here \(\operatorname{ad}_E(T)=[E,T]=ET-TE\). In the cancellation
application \(E\) has a slice \(s_*\), meaning \(E(s_*)=1\), and
\(B=(\ker E)[s_*]\).

The all-double-bracket theorem in
[the preceding report](deep-pass-12.md) already gives an invariant
ambient coordinate when the fourth double bracket also vanishes.
An *ambient coordinate* is a polynomial that belongs to a polynomial
coordinate system of \(B\), not merely a nonconstant invariant.
Once such a coordinate exists, regularity of \(\ker E\) makes that
kernel a polynomial three-ring by the regular-kernel theorem of
Bhatwadekar, Gupta and Lokhande.[^1] The slice hypothesis supplies
regularity by descent from \(B=(\ker E)[s_*]\).

**Mixed slice theorem.** If \(E\) has a slice and satisfies (1), then
\(\ker E\cong\mathbb C^{[3]}\), and its kernel contains an ambient
polynomial coordinate.

The proof first gives the following **restricted reduction**, which
does not use a slice to produce its residual form. Either an ambient
coordinate
annihilated by \(E\) has been obtained, or the displayed frame satisfies
\[
E^{m+1}x=0,\qquad E^m x=c\,g^m,\qquad
E^{m-1}x_4=\lambda g^{m-1},\qquad m\in\{3,4\},
\tag{2}
\]
where \(c\in\mathbb C^4\setminus\{0\}\), \(c_4=0\),
\(\lambda\in\mathbb C^*\), and \(g\) is a nonconstant polynomial
annihilated by \(E\). The vector \(x\) denotes the four displayed
coordinates. Formula (2) describes highest coefficients only. It is
not a normal form for the entire derivation.

Section 8 eliminates (2) using the slice. In particular, (1) together
with \(E^3x=0\) suffices for coordinate recognition even without that
final slice argument.
The quantity \(m\) is degree in the flow parameter \(t\), not ordinary
polynomial degree in the \(x_i\).

## 2. Recognition tools

Three established inputs are used precisely.

First, the three-variable single-partial lemma says that an LND \(D\)
of \(\mathbb C[u,v,w]\) with
\([D,[D,\partial_u]]=0\) fixes an ambient coordinate. Its complete
written reconstruction is in
[the single-partial audit](research/height-seven-audit.md).
The field \(W=[D,\partial_u]\) is locally nilpotent because it is the
highest coefficient of the conjugated LND
\(\partial_u+tW\). If \(D,W\) are independent over the fraction field,
the commuting-pair theorem provides a common invariant coordinate.[^2]
If dependent, primitive coefficient normalization makes the coefficients
independent of \(u\), and planar triangularization provides the
coordinate. The argument includes \(W=0\) and \(D=0\).

Second, a rank-one polynomial quasi-translation has a particularly
strong linear normal form. In suitable linear coordinates its nonzero,
complex-linearly independent coefficients depend only on the
coordinates corresponding to its zero components. Its image spans
at most three dimensions in four variables.[^3] A quasi-translation
field \(U\) here means \(U^2(x_i)=0\) for every generator. That property
will be proved for the auxiliary field to which the theorem is applied.

Third, if the fraction field of a subalgebra of a polynomial ring has
transcendence degree one, a polynomial parameter \(a\) generates that
field and contains the subalgebra in \(\mathbb C[a]\). This is the
exact polynomial factorization statement in de Bondt's Corollary 3.2.[^4]
It says nothing about whether \(a\) is an ambient coordinate.

One useful consequence of the first input is the following. If a
nonzero constant translation \(A\) commutes with \(E\), then its kernel
is an actual coordinate three-ring preserved by \(E\). The good
constant space
\[
G=\operatorname{span}_{\mathbb C}(T_1,T_2,T_3)
\]
contains a direction independent of \(A\). That direction restricts
to a nonzero constant partial on this three-ring, retains its good
double-bracket identity, and gives recognition by the single-partial
lemma. Constancy and actual commutation are both essential.

## 3. Flow and companion matrix

Put \(P=E(x)\), \(J=\operatorname{Jac}P\),
\(W_i=[E,T_i]\), and \(V=[E,W_4]\), with coefficient column \(v=V(x)\).
The case \(v=0\) is already closed, so assume \(v\ne0\).

Conjugation gives \(T_i+tW_i\) for \(i\le3\), and
\(T_4+tW_4+t^2V/2\) for the last partial. For
\(F_t=\exp(tE)x\), the coefficient matrix of these fields is
\[
C(t)=I-tJ+\frac{t^2}{2}ve_4^{\mathsf T},\qquad
\operatorname{Jac}(F_t)C(t)=I,\qquad \det C(t)=1.
\tag{3}
\]
Both multiplication orders of the inverse identity are valid. In
particular,
\[
E(J)=J^2-ve_4^{\mathsf T},\qquad E(v)=Jv.
\tag{4}
\]
The rank-one defect in (4) must not be discarded.

Only one column of \(C(t)\) is quadratic in \(t\). Cofactors therefore
give degree at most four for its inverse, and degree at most three for
the fourth row. Consequently
\[
E^5x\in\mathbb C^4,\quad E^6x=0,\quad
E^4x_4\in\mathbb C,\quad E^5x_4=0.
\tag{5}
\]
The earlier weighted-cofactor proof is in
[the initial mixed-frame note](research/height-nine-first-pass.md).

A five-by-five companion matrix makes the rank argument uniform:
\[
M=\begin{pmatrix}J&-v/2\\e_4^{\mathsf T}&0\end{pmatrix}.
\tag{6}
\]
Block elimination gives \(\det(I-tM)=\det C(t)=1\), hence \(M^5=0\).
The upper-left block of \((I-tM)^{-1}\) is \(C(t)^{-1}\). Writing
\(h_r=E^r x\), coefficient comparison gives
\[
(M^r)_{\rm upper\ left}=\frac{\operatorname{Jac}h_r}{r!}.
\tag{7}
\]

Here is the descent step. Suppose \(M^{r+1}=0\),
\(\operatorname{rank}M^r\le1\), and the upper-left block of \(M^r\)
vanishes. If \(M^r\ne0\), express it as an outer product \(ab^{\mathsf T}\).
The vanishing block forces either the first four entries of \(a\)
or those of \(b\) to vanish. Since \(MM^r=M^rM=0\), this would force
respectively \(Me_5=0\) or \(e_5^{\mathsf T}M=0\). Neither is possible:
these are \((-v/2,0)^{\mathsf T}\) and \((e_4^{\mathsf T},0)\).
Therefore \(M^r=0\).

A nilpotent matrix of size five has rank at most one in its fourth
power. If \(\operatorname{Jac}h_4=0\), descent makes \(M^4=0\);
its third power then has rank at most one. If also
\(\operatorname{Jac}h_3=0\), descent gives \(M^3=0\), whose second
power has rank at most one in dimension five. Thus every nonconstant
highest iterate \(h=h_m\) in the remaining possibilities \(m=2,3,4\)
has
\[
\operatorname{rank}\operatorname{Jac}h=1.
\tag{8}
\]
The argument uses zero Jacobians, so it applies to constant iterates
as well as zero iterates when descending.

## 4. Uniform highest-coefficient identities

Let \(m\) be the greatest index with \(h_m\ne0\), and set
\(h=h_m\), \(l=(h_{m-1})_4\). The nice case \(m=1\) closes directly:
niceness gives \(JP=0\) and \(E(J)=-J^2\); comparison with the three
good columns makes \(J^2=w e_4^{\mathsf T}\). Then \(wP_4=0\), so
either all four double brackets vanish or \(x_4\) is invariant.
This is the proved nice subcase in the initial mixed-frame note.

For \(m\ge2\), the highest coefficient in
\(C(t)P(F_t)=P\) gives \((h)_4=0\), since \(v\ne0\). Comparing the
next coefficients in that identity and in
\(C(t)\operatorname{Jac}(F_t)=I\) gives
\[
E(l)=0,\qquad
Jh=\frac{m-1}{2}lv,\qquad
J\operatorname{Jac}h=\frac m2v\operatorname{Jac}l.
\tag{9}
\]
These factors include the factorials in the exponential flow.

The highest coefficients of the conjugated partials acting on
\(F_t(x)\), and then on \(F_t(x_4)\), also give
\[
E(h)=W_i(h)=V(h)=0,\qquad
E(l)=W_i(l)=V(l)=0\quad(i\le3).
\tag{10}
\]
This does not imply \(W_4(h)=0\). In fact \(W_4\) need not be locally
nilpotent at all.

## 5. Constant highest coefficients

Suppose \(h=c\) is a nonzero constant vector. Equation (9) forces
\(l=r\in\mathbb C\), and \(c_4=0\). If \(r=0\), \(Jc=0\), so the
constant translation \(A=c\cdot\partial\) commutes with \(E\).
The recognition consequence from Section 2 applies.

If \(m=2\) and \(r\ne0\), \(E(x_4)=r\), so \(x_4/r\) is an ambient
coordinate slice. The kernel is isomorphic to \(B/(x_4)\), which is
a polynomial three-ring; together with that slice, kernel coordinates
are ambient coordinates.

For \(m\ge3\), \(r\ne0\), companion descent gives
\(\operatorname{rank}\operatorname{Jac}h_{m-1}\le1\).
Its image closure is a curve stable under translation by \(c\), because
\(E(h_{m-1})=c\). It contains a full affine line through each image
point and hence is one affine line. Thus \(h_{m-1}=ca+d\), with
\(a\in B\), \(E(a)=1\), and \(d\) constant.

Put \(q=(h_{m-2})_4\). Further coefficient comparisons, using that
\(\operatorname{Jac}h_m=0\), give
\[
Jh_{m-1}=\frac{c}{m-1}+\frac{m-2}{2}qv,\qquad
J\operatorname{Jac}h_{m-1}=\frac{m-1}{2}v\operatorname{Jac}q.
\]
Together with \(Jc=(m-1)rv/2\), these imply \(q-ra\in\mathbb C\).
Absorbing that constant into \(d\), define \(s=q/r\); then
\[
h_{m-1}=cs+d,\quad E(s)=1,\quad d_4=r,\quad
Jd=\frac c{m-1}-\frac r2sv.
\tag{11}
\]
The constant fields \(A=c\cdot\partial\) and \(B_0=d\cdot\partial\)
are independent. Equations (9) and (11) show that
\[
D_0=(m-1)B_0+sA,\qquad [E,D_0]=0,\qquad D_0(x_4)=(m-1)r.
\tag{12}
\]
Since \(s=E^{m-2}(x_4)/r\) and \(m-2>0\), actual commutation gives
\(D_0(s)=0\). This uses commutation of iterates, not the false premise
that \(E^{m-2}\) is itself a derivation.

Choose linear coordinates \((a,b,z_1,z_2)\) with
\(A=\partial_a\), \(B_0=\partial_b\), \(b=x_4/r\). Then
\[
(m-1)s_b+s s_a=0.
\tag{13}
\]
For a polynomial \(s\), degree in \(a\) excludes degree at least two:
the degrees of \(s s_a\) and \(s_b\) cannot match. Degree one would
give \((m-1)r_1'(b)+r_1(b)^2=0\) for a nonzero polynomial
coefficient \(r_1\), impossible by degree in \(b\). Consequently
\(s_a=s_b=0\).

The polynomial shear \(q_0=a-bs/(m-1)\), with inverse
\(a=q_0+bs/(m-1)\), now gives
\[
D_0=(m-1)\partial_b,\quad A=\partial_{q_0},\quad
\ker D_0=\mathbb C[q_0,z_1,z_2].
\tag{14}
\]
This is an actual coordinate three-ring preserved by \(E\). The good
direction \(A\in G\) survives as a partial there, so the single-partial
lemma closes the case.

In particular this covers \(m=5\), including the formerly unresolved
case \(E^4x_4\ne0\). The specialized derivation with constants
\(k=E^4x_4\), \(c=E^5x\) is written in
[the nonzero-top proof](research/height-nine-nonzero-top-pass.md).
No assumption \([A,V]=0\) is used.

## 6. A commuting correction for the coefficient curve

Suppose \(h\) is nonconstant. By (8) and (9), the joint map \((h,l)\)
has image dimension one: a nonzero component of \(v\) shows that
\(\operatorname{Jac}l\) lies in the row span of
\(\operatorname{Jac}h\). Polynomial curve factorization supplies
\[
h=H(a),\qquad l=L(a),\qquad
\mathbb C(h,l)=\mathbb C(a),\qquad a\in B.
\tag{15}
\]
At least one component of \(H\) is nonconstant. The chain rule and
(10) give \(E(a)=W_i(a)=V(a)=0\).

Define
\[
u(a)=(m-1)L(a)H'(a)-mL'(a)H(a),\qquad
U=u(a)\cdot\partial.
\tag{16}
\]
Equation (9) gives \(Ju=0\). Since \(E(u)=0\), this proves
\([E,U]=0\). Commutation then gives
\[
U(h)=U(E^m x)=E^m(Ux)=E^m(u(a))=0.
\]
The nonconstant component of \(H\) forces \(U(a)=0\). Hence
\(U(u(a))=0\): when nonzero, \(U\) is a nice LND with coefficient
Jacobian rank at most one. This argument does not assert that
\(h\cdot\partial\) is a nice LND.

Every nonzero \(u\) gives recognition. If constant, it is a constant
commuting translation. Otherwise apply the rank-one quasi-translation
normal form from Section 2. If its image spans a line, write \(u=f c\);
then \(Ju=0\) gives \(Jc=0\). If its image spans three dimensions,
its nonconstant coefficients depend on one linear coordinate, which
\(E(u)=0\) makes invariant.

The image-span-two case needs a further coordinate argument.
In simultaneous linear coordinates write
\[
U=f(z_1,z_2)\partial_{z_3}+g_0(z_1,z_2)\partial_{z_4}.
\]
Factor the coefficient curve again, now *inside*
\(\mathbb C[z_1,z_2]\). This gives a plane polynomial \(b\), with
\(f,g_0\in\mathbb C[b]\) and \(E(b)=0\). It does not assume that
the parameter \(a\) from (15) already belonged to this plane.

Divide the coefficients by their univariate gcd, obtaining coprime
\(p(b),q(b)\), and choose \(\alpha p+\beta q=1\) in \(\mathbb C[b]\).
The field \(U_0=p\partial_{z_3}+q\partial_{z_4}\) still commutes with
\(E\), because the divided factor is \(E\)-invariant. Set
\[
v_0=qz_3-pz_4,\qquad \rho=\alpha z_3+\beta z_4.
\tag{17}
\]
The inverse is \(z_3=p\rho+\beta v_0\),
\(z_4=q\rho-\alpha v_0\). Thus \(U_0=\partial_\rho\) and its kernel
\(\mathbb C[z_1,z_2,v_0]\) is an \(E\)-stable coordinate three-ring.

The three-dimensional good constant space \(G\) meets the
two-dimensional output plane in a nonzero constant direction
\(T=\gamma\partial_{z_3}+\delta\partial_{z_4}\). It commutes with
\(U_0\), and restricts to
\[
(\gamma q-\delta p)\partial_{v_0}.
\tag{18}
\]
The coefficient is nonzero because the two original output
coefficients were complex-linearly independent. It is \(E\)-invariant,
so its factor cancels from the restricted double-bracket equation.
The restriction of \(E\) therefore satisfies the single-partial lemma.
This proves recognition also in image-span two.

The only unit-ideal assertion here concerns coprime polynomials in one
variable. Coprime multivariable coefficients need not generate a unit
ideal. Nor was \(J\operatorname{Jac}u=0\) assumed.

## 7. Power-law exception and its quadratic elimination

If \(L=0\), (9) gives \(Jh=J\operatorname{Jac}h=0\). The same
commutation argument makes \(h\cdot\partial\) a rank-one nice LND,
so it closes as above. Thus a residual case has \(L\ne0\) and \(u=0\).

The equations
\((m-1)LH_i'=mL'H_i\) make the nonzero component ratios constant.
At each root they give
\((m-1)\operatorname{ord}H_i=m\operatorname{ord}L\).
Because \(m\) and \(m-1\) are coprime, factorization over \(\mathbb C\)
gives
\[
H=c\,g^m,\qquad L=\lambda g^{m-1},
\quad c\ne0,\ c_4=0,\ \lambda\ne0.
\tag{19}
\]
Here \(g\) is a nonconstant polynomial in the parameter, hence in
\(B\), and \(E(g)=0\). Consecutive powers generate \(\mathbb C(g)\),
so this is the exact same coefficient function field as (15).
Again, \(g\) need not be an ambient coordinate.

For \(m=2\), the power law can be removed completely. Put
\(A=c\cdot\partial\) and define
\[
y=x-\frac{c}{2\lambda^2}x_4^2.
\tag{20}
\]
Since \(c_4=0\), \(y_4=x_4\), and the polynomial inverse is
\(x=y+c y_4^2/(2\lambda^2)\). As \(E(x_4)=\lambda g\) and
\(E(g)=0\), \(E^2(x_4^2)=2\lambda^2 g^2\). Hence \(E^2y=0\).
The first three partials are unchanged. This already places \(E\)
under the proved nice-subcase criterion.

There is a stronger direct check. The new fourth partial is
\[
T'_4=T_4+\frac{x_4}{\lambda^2}A.
\]
Equation (9) says \(gJc=\lambda v/2\); using \(A\in G\) gives
\[
\operatorname{ad}_E^2(T'_4)
=V+\frac{2g}{\lambda}[E,A]
=V-\frac{2g}{\lambda}Jc=0.
\tag{21}
\]
The cancellation is a polynomial identity, even on \(g=0\).
Thus (20) gives an actual all-double-bracket coordinate frame.
This proves the \(m=2\) elimination in Section 1 and leaves only
\(m=3,4\) in (2).

## 8. Rational descent closes the higher power-law cases

Assume (2), now with the slice hypothesis, and put \(r=m-1\).
Since \(E(g)=0\), the derivation \(\delta=E/g\) is locally nilpotent
on \(B_g\), and
\[
\delta^m x=c,\qquad \delta^{m-1}x_4=\lambda.
\tag{22}
\]
The original constant partials extend to \(B_g\), but need not be
locally nilpotent there. No local-nilpotence claim about those
partials or their conjugate coefficients is used in this step.

Direct commutator expansion gives
\[
[\delta,T_i]=\frac{W_i}{g}+\frac{T_i(g)}{g}\delta.
\]
For \(i\le3\), \(E(T_i g)=W_i(g)=0\), so
\(\operatorname{ad}_\delta^2T_i=0\). For the last partial,
\[
\widetilde V:=\operatorname{ad}_\delta^2T_4
=\frac{V}{g^2}+\frac{2E(T_4g)}{g^2}\delta,\qquad
[\delta,\widetilde V]=0.
\tag{23}
\]
The last identity uses \(V(g)=0\) and \(E^2(T_4g)=V(g)=0\).
Thus the algebraic mixed-bracket identities survive rescaling.

The rational flow has determinant-one Jacobian: its divergence is
\(\operatorname{div}(E/g)=0\), because \(\operatorname{div}E=0\)
and \(E(g)=0\). Therefore the inverse-Jacobian and companion
arguments apply over the fraction field exactly as in Sections 3–5.
This is a repetition of matrix identities, not an application of a
polynomial coordinate theorem to \(B_g\).

If \(\widetilde V=0\), the highest constant identity gives
\(J_\delta c=0\). Thus \(A=c\cdot\partial\) commutes with \(\delta\),
and \([A,E]=(A(g)/g)E\). A slice makes the coefficients of \(E\)
generate the unit ideal, so this rational multiplier is polynomial.
Hence \(g\mid A(g)\). For a locally nilpotent derivation \(L\),
\(f\mid L(f)\) implies \(L(f)=0\), by its additive degree function.
Applying this to the constant partial \(A\) gives \(A(g)=0\).
Then \(A\) commutes with \(E\), and Section 2 closes the case.

Suppose \(\widetilde V\ne0\). Companion descent gives
\(\operatorname{rank}\operatorname{Jac}(\delta^{m-1}x)\le1\).
The map \(\delta^{m-1}x\) is regular on \(\operatorname{Spec}B_g\).
Its image closure is an irreducible curve, and each \(\delta\)-orbit
maps to a full affine line parallel to \(c\). It is therefore a line.
The normalized coefficient identities from Section 5 give
\[
\delta^{m-1}x=c\sigma+d,\quad d\in\mathbb C^4,\ d_4=\lambda,
\quad
\sigma=\frac{E^{m-2}x_4}{\lambda g^{m-2}},\quad E(\sigma)=g.
\tag{24}
\]
With \(A=c\cdot\partial\) and \(B_0=d\cdot\partial\), they also give
\[
D_0=rB_0+\sigma A,\quad [\delta,D_0]=0,\quad D_0(\sigma)=0.
\tag{25}
\]
As before, the last equality follows by commuting with the iterate
defining \(\sigma\), since \(D_0(x_4)=r\lambda\) is constant.

Choose linear coordinates \((a,b,z_1,z_2)\) with \(A=\partial_a\),
\(B_0=\partial_b\), \(x_4=\lambda b\), and put
\(R=\mathbb C[z_1,z_2]\). Equation (25) is the rational Burgers
equation \(r\sigma_b+\sigma\sigma_a=0\). Express
\(\sigma=N/D\) in lowest terms in \(R[a,b]\). Formula (24) ensures
\[
D\mid g^{m-2}.
\tag{26}
\]
Clearing denominators in Burgers gives
\[
rD(N_bD-ND_b)+N(N_aD-ND_a)=0.
\]
Reduction modulo \(D\) gives \(D\mid D_a\), hence \(D_a=0\) by
degree in \(a\). After division by \(D\), reduction modulo \(N\)
gives \(N\mid N_b\), hence \(N_b=0\). The remaining equation is
\(N_a=rD_b\), so
\[
N=\alpha a+\beta,\qquad D=\frac{\alpha}{r}b+\gamma,
\qquad \alpha,\beta,\gamma\in R.
\tag{27}
\]
Neither a polynomial Burgers conclusion nor a polynomial inverse
has been assumed for this rational function.

Also \(E(\sigma)=g\in B\) gives \(D\mid E(D)\); local nilpotence
then gives \(E(D)=0\) and \(E(N)=gD\). Define the polynomial field
\[
Z=D D_0=N\partial_a+rD\partial_b.
\]
Since \(\delta(D)=0\), \([\delta,Z]=0\), and consequently
\[
[Z,E]=\frac{Z(g)}gE.
\tag{28}
\]
The slice again makes \(Z(g)/g\) polynomial.

If \(\alpha\ne0\), let \(n=\deg_{a,b}g\). Equation (26) and the
nonconstant affine factor \(D\) imply \(n\ge1\). The field \(Z\)
does not increase \((a,b)\)-degree. Thus \(Z(g)/g\in R\), and
comparison of highest homogeneous terms gives \(Z(g)=n\alpha g\).
Applying \(E\) and using (28) gives \(E(\alpha)=0\).

Localize at \(\alpha\), and use the polynomial coordinates over
\(R_\alpha\)
\(a'=a+\beta/\alpha\), \(b'=b+r\gamma/\alpha\).
Then \(Z=\alpha\mathcal H\), with
\(\mathcal H=a'\partial_{a'}+b'\partial_{b'}\), and
\[
[\mathcal H,E]=nE,\qquad n\ge1.
\tag{29}
\]
The images \(E(z_i)\) are homogeneous of degree \(n\) in \(a',b'\),
and \(E(a'),E(b')\) have degree \(n+1\). Also \(E(\alpha^{-1})=0\).
It follows that \(E(B_\alpha)\) is contained in the proper ideal
\((a',b')\). This contradicts the surviving identity \(E(s_*)=1\).
Therefore \(\alpha=0\).

Now \(N,D\in R\). If \(D\) is constant, \(\sigma\in R\),
and \(D_0=r\partial_b+\sigma\partial_a\) is a polynomial nice LND.
The same multiplier argument in (28), followed by locally nilpotent
divisibility, gives \(D_0(g)=0\). Hence \([E,D_0]=0\).
The shear \(a\mapsto a-b\sigma/r\) retains \(A\) as a good partial,
so the single-partial three-ring argument closes this case.

If \(D\) is nonconstant, \(N,D\) are algebraically independent:
\(E(D)=0\), while \(E(N)=gD\ne0\), so \(N\) cannot be algebraic
over \(\mathbb C(D)\) in characteristic zero. Solving the two
Jacobian equations
\(\delta(D)=0\), \(\delta(N)=D\) therefore shows
\(\delta(z_1),\delta(z_2)\in\operatorname{Frac}R\).
Write them as reduced fractions in \(R\). Their denominators divide
\(g\) in \(B=R[a,b]\), because \(g\delta(z_i)=E(z_i)\) is polynomial
and coprimality in \(R\) persists in \(R[a,b]\).

Let \(h\in R\) be the least common multiple of these denominators.
Then \(h\mid g\), so \(E(h)=0\) by factorial closure of an LND
kernel. Consequently
\[
\Delta=h\delta|_R
\tag{30}
\]
is a polynomial derivation of \(R\), and
\(\Delta^j(z_i)=h^j\delta^j(z_i)\) eventually vanishes.
Thus \(\Delta\) is a nonzero plane LND; indeed
\(\Delta(N)=hD\ne0\). Planar triangularization supplies a coordinate
\(p\) of \(R\) with \(\Delta(p)=0\), hence \(E(p)=0\).[^5]
This is an ambient coordinate of \(B\). Regular-kernel recognition
finishes both remaining power-law cases and the mixed slice theorem.

The crucial point is that the plane action in (30) is polynomial on
the original plane, not merely rational or defined away from \(g=0\).
Its denominator is removed by an invariant factor whose divisibility
has been established in the ambient UFD.

## 9. Exact controls and excluded shortcuts

A primitive slice derivation can genuinely have power-law highest
coefficients before the shear. In coordinates \((a,d,z,w)\), take
\[
g=d-a^2/2,\qquad E=g(\partial_a+a\partial_d)+\partial_z.
\tag{31}
\]
Then \(E(g)=0\), \(E(z)=1\), \(E^2x=g^2e_d\), and \(E^3x=0\).
The partials in \(d,z,w\) are good; the double bracket of
\(\partial_a\) is \(2g(\partial_a+a\partial_d)\), whose next bracket
vanishes. The frame \((d-z-w,z,w,a)\) has exactly the filtration
degrees \((1,1,1,2)\). The derivative ideal is the unit ideal, yet
\((g^2\partial_d)(g^2)=2g^3\ne0\). The highest coefficient field
is not nice.

Its kernel is explicitly
\(\mathbb C[g,u,w]\), where \(u=a-zg\). The inverse equations are
\(a=u+zg\), \(d=g+(u+zg)^2/2\). This is a positive recognition
example and a counterexample to excluding the power-law branch by
primitivity. It is not a cancellation counterexample.

There is also a nonslice degree-four control. In \((a,b,c,d)\), let
\[
D=\partial_a+a\partial_b+(b+a^2/2)\partial_c
 +(c+ab+a^3/6)\partial_d,
\quad f=d-ac-b^2/2+a^2b/2-a^4/24.
\]
For \(E=fD\), \(D(f)=0\), the good partials are those in \(a,b,d\),
and the bad one is that in \(c\). Here
\(E^3(c)=2f^3\), \(E^4x=6f^4e_d\), and \(E^5x=0\).
The highest vector again fails niceness. All coefficients of \(E\)
are divisible by \(f\), so this example has no slice. The two
controls distinguish the highest-coefficient structure from the
separate slice hypothesis.

Finally,
\(E=-d(a+bd)\partial_a+(a+bd)\partial_b+\partial_c\)
is a genuine mixed slice control whose middle field is
\[
W_4=(a+2bd)\partial_a-b\partial_b.
\]
Every positive iterate of \(W_4\) on \(b\) is \((-1)^n b\), so
\(W_4\) is not locally nilpotent. Only the highest conjugate
coefficients were certified as LNDs.

All 282 test methods in twenty-one suites passed. The new independent
[mixed-height checker](research/mixed_height_checks.py) contains
twenty-two methods and imports no research modules. It checks the
positive and negative controls, inverse Jacobian orientations,
filtration degrees, polynomial and rational Burgers identities,
denominator clearing, positive-weight fixed loci, and the \(m=2\)
reduction. A genuine primitive cubic-time slice control checks the
nonzero rescaled defect and the actual coordinate three-ring.
[The verification log](verification-pass-13.json) records the actual
commands, observed counts, exit codes, and times.

These finite algebraic checks do not formally prove the general
classification theorems or every step of the written argument.
[The separate full restricted-proof audit](research/height-nine-pass13-independent-audit.md)
checks the initial reduction through the quadratic shear.
[The separate rational-rescaling audit](research/height-nine-rational-rescale-independent-audit.md)
checks the final higher-degree closure, including the vanishing-defect
and constant-denominator cases. Both found no gap in their stated
arguments. These are model reconstructions, not human expert review
or proof-assistant verification.

## 10. Scope of the completed theorem and remaining work

For (2), equation (9) gives
\[
v=\frac{2g}{(m-1)\lambda}Jc.
\tag{32}
\]
Thus \(V\) has a polynomial factor \(g\). This does not prove that
\(E\) has that factor. The primitive example (31) disproves that
inference in degree two.

A localization that divides by \(g\) must retain information at
\(g=0\). The polynomial Burgers step in Section 5 does not hold for
rational functions: \(s=4a/b\) satisfies \(4s_b+s s_a=0\), but
\(s_a\ne0\), and the proposed shear \(a-bs/4\) is identically zero.
Generic rational straightening is therefore insufficient. Section 8
addresses that failure directly: the nonpolynomial solutions either
produce a forbidden positive-weight fixed locus, or give a polynomial
plane LND after invariant denominator clearing.

The completed mixed-case proof still leaves the global problem of
constructing a suitable frame for an arbitrary slice. To state the
height consequence, filter \(K[s_*]\) by polynomial degree in \(s_*\).
For each coordinate partial let \(q_i\) be the least shift such that
\(T_i(F_d)\subseteq F_{d+q_i}\) for every filtration piece \(F_d\),
and put \(H=\sum_i(q_i+1)\). This is the frame-dependent height
defined in the preceding report.

If a frame has filtration height at most nine, the earlier zero/low-degree criteria
leave only the pattern \((1,1,1,2)\), which satisfies (1).
Thus the strengthened conclusion is
\[
H\le9\quad\Longrightarrow\quad \ker E\simeq\mathbb C^{[3]}.
\tag{33}
\]
A hypothetical nonpolynomial factor now has \(H_{\min}\ge10\).
There is no proved universal upper bound or decreasing frame
operation. Raising a finite threshold is not a proof that every
possible frame can be reduced to that threshold.

The rational Burgers formula itself has a published predecessor:
Saleeby's Theorem 1(ii) states the corresponding nonconstant
constant-coefficient formula.[^6] The proof here retains an elementary
UFD argument over the parameter ring \(R\), and separately proves
the action-specific denominator and fixed-locus steps.
The [post-proof overlap audit](research/mixed-commutator-postproof-literature.md)
records this attribution and the source-scope distinctions.

That bounded review did not locate an identical mixed recognition
theorem. This is not evidence of novelty or an exhaustive determination
of the literature. Nearby time-degree,
quasi-nice, triangular-action, and fibration theorems retain their own
coordinate and presentation hypotheses; the
[source-scope audit](research/mixed-flow-literature-pass.md) records
those distinctions. No novelty, publication, or solution of the
unrestricted conjecture is claimed.

## Sources

[^1]: S. M. Bhatwadekar, N. Gupta and S. A. Lokhande,
    [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\)*](https://arxiv.org/html/1501.01438v1),
    Theorem 3.5. A nonzero \(k[T]\)-LND of \(k[T,X,Y,Z]\) with
    regular kernel has kernel \(k[T]^{[2]}\).

[^2]: S. Maubach,
    [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf),
    Theorem 3.6, for the complex three-variable commuting-pair
    statement. Also reproduced, with attribution to Daigle and
    Kaliman, in N. Dasgupta and S. Gaifullin,
    [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510),
    Proposition 2.14.

[^3]: M. de Bondt,
    [*Quasi-translations and singular Hessians*](https://arxiv.org/pdf/1501.05168),
    Proposition 1.3 and Theorem 5.5. The quasi-translation hypothesis
    and rank-one coefficient Jacobian are verified before application.

[^4]: M. de Bondt,
    [*Rational maps \(H\) for which \(K(tH)\) has transcendence degree 2 over \(K\)*](https://arxiv.org/pdf/1501.06046),
    Corollary 3.2 and Lemma 3.3, PDF pp. 20–21. The polynomial
    parameter theorem is used both in \(B\) and separately in a
    coordinate plane. See the
    [exact source note](research/polynomial-curve-factorization-source.md)
    for the distinction between a function-field generator and an
    ambient coordinate.

[^5]: R. Rentschler, *Opérations du groupe additif sur le plan affine*,
    C. R. Acad. Sci. Paris, Sér. A-B 267 (1968), A384–A387.
    The exact triangularization statement used here is reproduced as
    Theorem 2.7 in N. Dasgupta and S. Gaifullin,
    [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510).
    Its Section 2 also records factorial closure and invariant
    localization for LNDs.

[^6]: E. G. Saleeby,
    [*Meromorphic solutions of generalized inviscid Burgers' equations and a family of quadratic PDEs*](https://doi.org/10.1016/j.jmaa.2014.12.046),
    Journal of Mathematical Analysis and Applications 425 (2015),
    508–519, Theorem 1(ii), p. 510. The
    [author-uploaded original article](https://www.researchgate.net/publication/270961773_Meromorphic_solutions_of_generalized_inviscid_Burgers%27_equations_and_a_family_of_quadratic_PDEs)
    was inspected. Constant solutions must be included separately;
    the project does not rely on the source's analytic proof.
