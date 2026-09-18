# Zero-top height-nine branches and the power-law residual

Subsequent closure: the residual described here is eliminated under the
slice hypothesis by the [quadratic shear](height-nine-power-law-pass.md)
and [rational-rescale proof](height-nine-rational-rescale-pass.md).
The intermediate reductions below remain valid; their open-case
language records the point reached before those final arguments.

This pass concerns the mixed commutator hypotheses in
[height-nine-first-pass.md](height-nine-first-pass.md), with
\(E^5x=0\) and \(E^4x_4=0\). It closes every constant highest-iterate
branch and every nonzero coefficient-curve correction described below.
The remaining nonconstant branch has a precise power-law form. That form
can occur for a primitive slice derivation with a genuine height-nine
frame. No general coordinate-recognition proof for that form is given.

Write \(P=E(x)\), \(J=\operatorname{Jac}P\), \(V=[E,[E,T_4]]\),
\(v=V(x)\), and \(h_r=E^r(x)\). The first three constant partials are
good: \(\operatorname{ad}_E^2T_i=0\). Their span is \(G\). The case
\(V=0\) is already covered by the height-eight theorem, so assume
\(v\ne0\) throughout the reductions below.

Let \(m\) be the highest flow degree, so \(h=h_m\ne0\) and
\(h_{m+1}=0\). The nice case \(m=1\) is already closed. Thus here
\(m\in\{2,3,4\}\). Put
\[
l=(h_{m-1})_4.
\]

## 1. Companion-matrix rank descent

The inverse flow Jacobian is
\[
C(t)=I-tJ+\frac{t^2}{2}ve_4^{\mathsf T},\qquad \det C(t)=1.
\]
Introduce the five-by-five matrix
\[
M=\begin{pmatrix}J&-v/2\\e_4^{\mathsf T}&0\end{pmatrix}.
\]
Block elimination gives
\(\det(I-tM)=\det C(t)=1\), so \(M^5=0\) over the fraction field.
The upper-left block of \((I-tM)^{-1}\) is \(C(t)^{-1}\). Consequently
\[
(M^r)_{\mathrm{upper\ left}}
=\frac1{r!}\operatorname{Jac}h_r.
\tag{1}
\]

Here is the needed descent principle. Suppose \(M^{r+1}=0\),
\(\operatorname{rank}M^r\le1\), and the upper-left four-by-four block
of \(M^r\) is zero. If \(M^r\ne0\), write it as an outer product
\(ab^{\mathsf T}\). The vanishing block forces either the first four
entries of \(a\) or those of \(b\) to vanish. The relations
\(MM^r=M^rM=0\) would then require respectively
\[
Me_5=(-v/2,0)=0
\quad\text{or}\quad e_5^{\mathsf T}M=(e_4^{\mathsf T},0)=0,
\]
both impossible. Hence \(M^r=0\).

A nilpotent five-by-five matrix has \(\operatorname{rank}M^4\le1\).
If \(h_4=0\), equation (1) and the principle give \(M^4=0\).
Its Jordan blocks then have size at most four, so
\(\operatorname{rank}M^3\le1\). If also \(h_3=0\), the principle
gives \(M^3=0\), and the possible blocks of sizes at most three in
dimension five give \(\operatorname{rank}M^2\le1\).
Thus in all three possible highest degrees,
\[
\operatorname{rank}\operatorname{Jac}h\le1.
\tag{2}
\]
The same argument applies when the relevant \(h_r\) is constant,
because only its zero Jacobian is used.

## 2. Uniform highest-coefficient identities

Since \(P(F_t)\) has degree \(m-1\), the coefficient of \(t^{m+1}\)
in \(C(t)P(F_t)=P\) is
\(v(h)_4/[2(m-1)!]\). Therefore
\[
(h)_4=0,\qquad E(l)=0.
\tag{3}
\]
Fourth components are written with parentheses to distinguish them from
iterate indices.

The coefficients of \(t^m\) in the same identity and of \(t^{m+1}\)
in \(C(t)\operatorname{Jac}(F_t)=I\) give
\[
Jh=\frac{m-1}{2}l v,
\qquad
J\operatorname{Jac}h=\frac m2v\operatorname{Jac}l.
\tag{4}
\]
The factorial factors follow from
\(P(F_t)=\sum_{r=0}^{m-1}t^rh_{r+1}/r!\).

Coefficient extraction from the conjugated partials also gives
\[
E(h)=E(l)=0,\quad W_i(h)=W_i(l)=0\ (i\le3),
\quad V(h)=V(l)=0.
\tag{5}
\]
For \(h\), use degrees \(m+1\) and \(m+2\) in the good and bad
conjugated fields applied to \(F_t(x)\). For \(l\), use degrees \(m\)
and \(m+1\) applied to \(F_t(x_4)\), whose degree is at most \(m-1\).

## 3. A constant highest iterate closes

Suppose \(h=c\in\mathbb C^4\setminus\{0\}\). Equation (4) and
\(v\ne0\) make \(l=r\) constant. Also \(c_4=0\).
If \(r=0\), the constant field \(A=c\cdot\partial\) commutes with
\(E\), which closes by the surviving good direction on its coordinate
three-ring. If \(m=2\) and \(r\ne0\), \(E(x_4)=r\) is already a
coordinate slice.

It remains to take \(m\ge3\), \(r\ne0\). Since \(\operatorname{Jac}h_m=0\),
the companion argument gives \(\operatorname{rank}\operatorname{Jac}h_{m-1}\le1\).
But \(E(h_{m-1})=c\ne0\), so its image closure is an irreducible curve
stable under translation by \(c\), hence an affine line. Thus
\[
h_{m-1}=c a+d,\qquad E(a)=1,
\]
for a polynomial \(a\) and a constant vector \(d\).

Put \(q=(h_{m-2})_4\). Further coefficient comparisons give
\[
Jh_{m-1}=\frac{c}{m-1}+\frac{m-2}{2}qv,
\quad J\operatorname{Jac}h_{m-1}=\frac{m-1}{2}v\operatorname{Jac}q.
\]
Together with \(Jc=(m-1)rv/2\), these imply
\(q-ra\in\mathbb C\). Absorb that constant in \(d\), writing
\[
h_{m-1}=cs+d,\quad s=q/r,\quad E(s)=1,
\quad d_4=r,
\quad Jd=\frac{c}{m-1}-\frac r2sv.
\tag{6}
\]
With constant fields \(A=c\cdot\partial\) and \(B_0=d\cdot\partial\),
the field
\[
D_0=(m-1)B_0+sA
\]
commutes with \(E\), has \(D_0(x_4)=(m-1)r\), and kills \(s\).
The last assertion follows from
\(s=E^{m-2}(x_4)/r\) and \(m\ge3\).

The constant fields are independent because \(c_4=0\) and \(d_4=r\ne0\).
Choose linear coordinates with \(A=\partial_a\), \(B_0=\partial_b\),
and \(x_4=rb\). Then
\[
(m-1)s_b+s s_a=0.
\]
Degree in \(a\) excludes degree at least two. Degree one would give
\((m-1)r_1'(b)+r_1(b)^2=0\) for a nonzero polynomial leading
coefficient, impossible by degree in \(b\). Hence \(s_a=s_b=0\).
The shear \(a\mapsto a-bs/(m-1)\) makes \(D_0\) a coordinate partial
and retains \(A\) as a coordinate partial on its kernel. Since
\(c_4=0\), \(A\in G\) and is good. The three-variable single-partial
lemma and regular-kernel recognition close this case.

## 4. Nonconstant highest iterate: one polynomial parameter

Assume \(h\) is nonconstant. Its Jacobian has rank one. In (4), any
nonzero component of \(v\) shows that \(\operatorname{Jac}l\) lies in
the row span of \(\operatorname{Jac}h\). Thus the simultaneous
coefficient map \((h,l)\) has image dimension one.

[De Bondt, Corollary 3.2](https://arxiv.org/pdf/1501.06046) supplies a
polynomial parameter \(a\in B\) for its function field and shows that
all its polynomial components belong to \(\mathbb C[a]\). Write
\[
h=H(a),\qquad l=L(a),\qquad H\in\mathbb C[a]^4,\ L\in\mathbb C[a].
\]
At least one component of \(H\) is nonconstant. Equation (5) then gives
\(E(a)=W_i(a)=V(a)=0\), by the chain rule and the domain property.
No coordinate property of \(a\) is assumed.

Define the polynomial vector
\[
u(a)=(m-1)L(a)H'(a)-mL'(a)H(a).
\tag{7}
\]
Equation (4) gives \(Ju=0\). Since \(E(a)=0\), the polynomial field
\(U=u(a)\cdot\partial\) commutes with \(E\). Therefore
\[
U(h)=U(E^m x)=E^m(Ux)=E^m(u(a))=0.
\]
The nonconstant component of \(H\) forces \(U(a)=0\). Consequently
\(U(u(a))=0\): if nonzero, \(U\) is a nice LND of coefficient-Jacobian
rank at most one. This proves its quasi-translation property rather than
assuming that property for the original highest vector \(h\).

## 5. Every nonzero correction \(u\) closes

A nonzero constant \(u\) gives a constant commuting translation.
Otherwise apply the rank-one quasi-translation normal form in
[de Bondt, Theorem 5.5](https://arxiv.org/pdf/1501.05168).
The image-span-one case gives a constant commuting direction after
cancelling a scalar factor in \(Ju=0\). In image-span three, the
coefficients depend on one linear coordinate, and \(E(u)=0\) fixes
that coordinate.

For image-span two, use simultaneous linear coordinates with
\[
U=f(z_1,z_2)\partial_{z_3}+g(z_1,z_2)\partial_{z_4}.
\]
Reapply the polynomial-parameter result inside \(\mathbb C[z_1,z_2]\),
obtaining a parameter \(b\) in that plane. This is important: the
earlier parameter \(a\) is not presumed to lie there. The coefficients
are \(f(b),g(b)\), and \(E(b)=0\).

Divide by their univariate gcd. The resulting coefficients \(p(b),q(b)\)
are coprime in \(\mathbb C[b]\), so choose \(\alpha p+\beta q=1\).
The primitive field \(U_0=p\partial_{z_3}+q\partial_{z_4}\) still
commutes with \(E\). The change
\[
v_0=qz_3-pz_4,\qquad \rho=\alpha z_3+\beta z_4
\]
is a polynomial coordinate change over \(\mathbb C[z_1,z_2]\), with
inverse \(z_3=p\rho+\beta v_0\), \(z_4=q\rho-\alpha v_0\).
Thus \(\ker U_0=\mathbb C[z_1,z_2,v_0]\) is a coordinate three-ring
preserved by \(E\).

The three-dimensional good constant space \(G\) intersects the
two-dimensional output plane in a nonzero constant direction
\(T=\gamma\partial_{z_3}+\delta\partial_{z_4}\). It commutes with
\(U_0\), and its restriction to the coordinate three-ring is
\[
(\gamma q-\delta p)\partial_{v_0}.
\]
This coefficient is nonzero: the original two coefficient functions
were complex-linearly independent, so \(p/q\) is nonconstant.
Also \(E\) kills the coefficient. The restricted double-bracket equation
therefore permits cancellation of this polynomial factor and gives the
single-partial hypothesis for \(\partial_{v_0}\). This closes the case.

In particular, this step never assumes \(J\operatorname{Jac}u=0\).
The unit-ideal assertion concerns two coprime univariate polynomials,
not arbitrary coprime multivariable coefficients.

## 6. Exact remaining power-law exception

If \(L=0\), equations (4) give \(Jh=J\operatorname{Jac}h=0\).
Then \(h\cdot\partial\) commutes with \(E\) and kills \(h\), by
\(H(E^m x)=E^m(Hx)\). The previously proved rank-one closure applies.
Thus a residual nonconstant case has \(L\ne0\) and \(u=0\).

The equations
\((m-1)LH_i'=mL'H_i\) make all nonzero component ratios constant.
At every root, they also imply
\((m-1)\operatorname{ord}H_i=m\operatorname{ord}L\).
Since \(m\) and \(m-1\) are coprime, unique factorization gives
\[
h=c\,g^m,\qquad l=\lambda g^{m-1},
\quad 0\ne c\in\mathbb C^4,\quad c_4=0,\quad\lambda\in\mathbb C^*.
\tag{8}
\]
Here \(g\) is a nonconstant polynomial invariant. The normalizing
parameter can be chosen to be \(g\): its consecutive powers generate
\(\mathbb C(g)\), the same coefficient field. This is an exact residual
normal form for the highest coefficients, not a normal form for all of
\(E\).

For \(A=c\cdot\partial\), equation (4) further gives
\[
v=\frac{2g}{(m-1)\lambda}Jc.
\]
Thus \(V\) has a factor \(g\). This does not prove that \(E\) has a
common coefficient factor, or that a primitive intrinsic action is free.
Section 8 shows that \(E\) can have the unit derivative ideal even in
this exception. A proof for the residual case must recognize its kernel,
not exclude the power-law form solely by primitivity.

## 7. A non-slice control realizes the exception

In physical coordinates \((a,b,c,d)\), take
\[
D=\partial_a+a\partial_b+(b+a^2/2)\partial_c
+(c+ab+a^3/6)\partial_d,
\]
\[
f=d-ac-b^2/2+a^2b/2-a^4/24,\qquad E=fD.
\]
Direct differentiation gives \(D(f)=0\). The partials in \(a,b,d\)
are good, while
\(\operatorname{ad}_E^2(\partial_c)=2E\ne0\) and its next bracket
vanishes. Thus order the displayed variables as \((a,b,d,c)\).
Then
\[
l=E^3(c)=2f^3,\qquad h=E^4(x)=6f^4\partial_d
\]
in vector-field notation, and \(E^5x=E^4(c)=0\). Nevertheless
\[
(6f^4\partial_d)(6f^4)=144f^7\ne0.
\]
The highest vector does not define a quasi-translation. Its correction
in (7) is identically zero.

Every coefficient of \(E\) is divisible by \(f\), and its first
coefficient equals \(f\), so its derivative ideal is exactly \((f)\).
It has no slice. This control therefore does not contradict the
cancellation premise. It proves why neither the highest-vector
quasi-translation property nor constancy of \(l\) follows merely from
the mixed commutator and top-degree identities.

The control was independently verified in
[mixed_height_checks.py](mixed_height_checks.py). Finite identities
support this example, not a general exclusion of (8).

## 8. A primitive slice control also realizes the exception

In physical coordinates \((a,d,z,w)\), put
\[
g=d-a^2/2,\qquad E=g(\partial_a+a\partial_d)+\partial_z.
\]
Then \(E(g)=0\), \(E(z)=1\), and
\[
E^2(x)=g^2e_d,\qquad E^3(x)=0.
\]
The partials \(\partial_d,\partial_z,\partial_w\) are good, whereas
\[
\operatorname{ad}_E^2(\partial_a)
=2g(\partial_a+a\partial_d)\ne0,
\qquad \operatorname{ad}_E^3(\partial_a)=0.
\]
Use the displayed coordinate frame
\[
(x_1,x_2,x_3,x_4)=(d-z-w,z,w,a).
\]
Its good partials are
\(\partial_d,\partial_d+\partial_z,\partial_d+\partial_w\), and
its bad partial is \(\partial_a\). All four filtration degrees are
exactly \((1,1,1,2)\) for the slice \(z\). Here \(m=2\), \(l=g\),
and \(h=g^2e_d\), so the correction (7) vanishes identically.
Nevertheless \(h\cdot\partial\) is not nice, since
\[
(g^2\partial_d)(g^2)=2g^3\ne0.
\]

This time the derivative ideal of \(E\) is the unit ideal. The kernel
is explicitly polynomial: with \(u=a-zg\),
\[
\ker E=\mathbb C[g,u,w],\qquad
a=u+zg,\qquad d=g+(u+zg)^2/2.
\]
Thus the example is not a cancellation counterexample. It is a decisive
control against excluding the power-law branch by common coefficient
factors or against assuming that its highest vector is a quasi-translation.
Its identities and exact height-nine profile were independently checked
in an inline SymPy calculation.

The overall height-nine problem remains unclosed in the power-law branch
identified above within this zero-top analysis. The branch is nonempty
even under the slice premise; a general recognition argument is still
needed.
