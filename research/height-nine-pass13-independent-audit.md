# Independent audit of the pass-thirteen mixed-height reductions

The subsequent higher-degree closure has its own
[independent audit](height-nine-rational-rescale-independent-audit.md).
The scope and intermediate open-case language below are historical.

The restricted reductions in
[height-nine-zero-top-pass.md](height-nine-zero-top-pass.md) and
[height-nine-nonzero-top-pass.md](height-nine-nonzero-top-pass.md)
pass this audit. The companion-matrix descent, the nonzero correction
closure, and the stated power-law highest coefficients are justified.
The additional \(m=2\) shear below also closes that power-law case.
No proof for the remaining \(m=3,4\) power-law cases is claimed here.

## 1. Companion matrix and the rank descent

With \(R=ve_4^{\mathsf T}\), the proposed matrix satisfies
\[
I-tM=\begin{pmatrix}I-tJ&tv/2\\-te_4^{\mathsf T}&1\end{pmatrix}.
\]
Its Schur complement is exactly \(I-tJ+t^2R/2=C(t)\). Thus both
the determinant and upper-left inverse-block statements have the
correct signs and orientation. The identity \(\det(I-tM)=1\) makes
the characteristic polynomial \(X^5\), so Cayley-Hamilton gives
\(M^5=0\) over the fraction field. Expanding its inverse gives
\[
(M^r)_{1:4,1:4}=\operatorname{Jac}(E^r x)/r!.
\]

The rank-one descent principle is valid. If a nonzero rank-one matrix
\(N=ab^{\mathsf T}\) has zero upper-left four-by-four block, either
the first four entries of \(a\) vanish or the first four of \(b\)
vanish. If additionally \(MN=NM=0\), the first possibility forces
\(Me_5=0\), and the second forces \(e_5^{\mathsf T}M=0\).
Here these are impossible because \(v\ne0\) and \(e_4\ne0\).

The Jordan-block counts used afterward are also correct. In dimension
five, nilpotence indices at most five, four, and three give ranks of
\(M^4,M^3,M^2\) at most one, respectively. The descending argument
uses a zero Jacobian, so it works for constant as well as zero highest
iterates. It is not an assertion that an arbitrary rank-one block can
be discarded without the annihilation hypotheses.

## 2. Highest coefficients and the polynomial parameter

Coefficient comparison independently gives
\[
(h_m)_4=0,\qquad
Jh_m=\frac{m-1}{2}l v,\qquad
J\operatorname{Jac}h_m=\frac m2v\operatorname{Jac}l.
\]
The factors are consistent with the denominators \((m-1)!\) in
\(P(F_t)\) and \(m!\) in \(F_t\). The vanishing statements for
\(W_i(h_m),V(h_m),W_i(l),V(l)\) follow from the respective highest
coefficients of the conjugated fields, as stated in the note.

When \(h_m\) is nonconstant, its Jacobian has rank one. A nonzero
entry of \(v\) makes \(\operatorname{Jac}l\) a linear combination
of the rows of \(\operatorname{Jac}h_m\). Therefore the simultaneous
coefficient algebra really has transcendence degree one.

The source cited for its parameter has precisely the needed strength.
[De Bondt, Corollary 3.2](https://arxiv.org/pdf/1501.06046) supplies
a polynomial generator of the fraction field and places the coefficient
algebra inside the polynomial ring in that generator. Applying it first
in four variables, and later again in the actual coordinate plane, is
legitimate. The second application cannot be replaced by an unsupported
assertion that the first parameter already lies in that plane.

The correction
\[
u=(m-1)LH'-mL'H
\]
satisfies \(Ju=0\), by the two coefficient identities. Its coefficients
are \(E\)-invariant, so \(U=u\cdot\partial\) commutes with \(E\).
The computation
\(U(h_m)=U(E^m x)=E^m(Ux)=0\) is valid by commutation. It forces
\(U(a)=0\) through a nonconstant component of \(H(a)\), and hence
proves niceness of \(U\). It does not presume niceness of \(h_m\).

## 3. The image-span-two correction closes

[De Bondt, Theorem 5.5](https://arxiv.org/pdf/1501.05168) is a
nonhomogeneous rank-one quasi-translation theorem, so it applies to the
constructed \(U\). In the image-span-two case it puts both coefficient
functions in the complementary coordinate plane. The polynomial
parameter theorem then gives \(f(b),g(b)\) there, with \(E(b)=0\).

After removing their gcd in \(\mathbb C[b]\), let the coefficients be
\(p,q\), and choose \(\alpha p+\beta q=1\). The gcd is
\(E\)-invariant, so division preserves commutation with \(E\). The
matrix for the proposed two-variable change is
\[
\begin{pmatrix}q&-p\\\alpha&\beta\end{pmatrix},
\qquad\det=\beta q+\alpha p=1.
\]
The inverse displayed in the note is correct. Its coefficients lie in
the coordinate-plane ring even if \(b\) is not a coordinate of that
plane. Consequently \(\ker U_0\) is an actual coordinate three-ring,
not just an abstract polynomial algebra.

A three-dimensional constant good space intersects the constant output
plane nontrivially. For a nonzero direction
\(T=\gamma\partial_{z_3}+\delta\partial_{z_4}\) in that intersection,
the restricted coefficient is
\(r=\gamma q-\delta p\). It cannot vanish: otherwise \(p,q\), and
then \(f,g\), would be complex-linearly dependent. Also \(E(r)=0\).
Since both \(E\) and \(T\) preserve \(\ker U_0\), restriction and
the product rule give exactly
\[
0=[E,[E,r\partial_{v_0}]]
=r[E,[E,\partial_{v_0}]].
\]
Cancellation is legitimate in this domain. No unit assumption on \(r\)
is needed. This verifies the retained single-partial hypothesis without
assuming \(J\operatorname{Jac}u=0\) or a multivariable Bezout identity.

## 4. The residual power law is exact

In the nonconstant residual case, \(L\ne0\) and \(u=0\).
A nonzero constant \(L\) would force every \(H_i\) constant, so
\(L\) is nonconstant. The logarithmic derivative equations make all
nonzero component ratios of \(H\) constant. At each root they give
\[
(m-1)\operatorname{ord}H_i=m\operatorname{ord}L.
\]
The coprimality of \(m,m-1\) therefore makes the root multiplicities
of \(L\) multiples of \(m-1\), and those of each nonzero \(H_i\)
the corresponding multiples of \(m\). This proves
\[
h_m=cg^m,\qquad l=\lambda g^{m-1},
\quad c_4=0,\quad \lambda\ne0,
\]
for a nonconstant polynomial invariant \(g\). There are no missing
roots supported only in one of the two factors: their orders would
contradict the same equation. Over \(\mathbb C\), the remaining
factors are nonzero constants.

The parameter-field claim is also exact. Choose \(c_i\ne0\). Then
\(g=\lambda(h_m)_i/(c_i l)\), so the coefficient field contains
\(g\), while all the coefficients are in \(\mathbb C[g]\).
Thus the coefficient field equals \(\mathbb C(g)\). This says nothing
by itself about coordinatehood of \(g\), or about the lower iterates
of \(E\). The factor \(g\) in \(V\) is not a factor of \(E\)
without a separate argument.

## 5. Nonzero-top reduction and the additional quadratic-time shear

The nonzero-top note's key improvement is sound:
\([E,D_0]=0\), \(D_0(x_4)=4k\), and
\(s=E^3(x_4)/k\) imply \(D_0(s)=0\). The polynomial equation
\(4s_b+ss_a=0\) then forces independence of both \(a,b\) by the
stated degree comparisons. The resulting shear retains one good
partial, which suffices. No assumption about \([T_c,V]\) is used.

There is a further proved reduction when the zero-top power law has
\(m=2\). In that case
\[
E^2x=cg^2,\qquad E(x_4)=\lambda g,\qquad E(g)=0.
\]
Set
\[
y=x-\frac{c x_4^2}{2\lambda^2}.
\]
Because \(c_4=0\), this is a polynomial shear with inverse obtained
by adding the same vector expression in \(y_4\). Directly,
\(E^2y=0\). Its first three partials are unchanged, while the fourth
is
\[
T'_4=T_4+\frac{x_4}{\lambda^2}A,
\qquad A=c\cdot\partial.
\]
Using \(\operatorname{ad}_E^2A=0\), \(E^2x_4=0\), and
\(2gJc=\lambda v\), the transformed bad double bracket is
\[
\operatorname{ad}_E^2T'_4
=V-\frac{2g}{\lambda}(Jc)\cdot\partial=0.
\]
This is an actual all-double coordinate frame. It closes \(m=2\)
without assuming that \(g\) is a coordinate. The remaining power-law
degrees in this restricted audit are \(m=3,4\).

Eight inline exact SymPy assertions independently checked the Bezout
coordinate map and both inverse compositions with a noncoordinate plane
parameter, the nonunit retained coefficient, and the explicit \(m=2\)
slice control's shear, inverse, and transformed nice all-double field.
No original proof note, test suite, or registry was edited by this audit.
