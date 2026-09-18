# The constant-top cubic branch has an exact two-variable common kernel

The independent-defect, constant-top cubic branch admits a stronger
actual normal form than the previously retained companion rank bound.
After constant changes within the two good and two bad coordinate
pairs, either an existing recognition criterion applies, or there are
actual polynomials \(t,f\) and one-variable polynomials \(F,U,G\) with
\[
Ef=1,\qquad Et=0,\qquad
\ker V_3\cap\ker V_4=\mathbb C[t,f],
\]
\[
E^2x=(f-F(t),U(t),1,0)^{\mathsf t},\qquad
Ex_3=f,\qquad Ex_4=G(t).
\]
Here \(U\) and \(G\) are nonconstant. The parameter \(t\) generates
the exact common kernel of the three independent commuting LNDs
\(E,V_3,V_4\).

This is a reduction and a recognition subcase, not a closure of the
whole constant-top cubic sector. Neither \(t\) nor the new slice
\(f\) is asserted to be an ambient coordinate. In particular the
displayed two-variable kernel is not asserted to be an ambient
coordinate plane.

## 1. Actual hypotheses and the cubic companion boundary

Let
\[
B=k[x_1,x_2,x_3,x_4],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad E(s_*)=1,
\]
and let \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2),\qquad
\operatorname{ad}_E^3T_i=0\quad(i=3,4).
\tag{1}
\]
Write
\[
P=Ex,\quad J=\operatorname{Jac}P,\quad h_j=E^jx,\quad
W_i=[E,T_i],\quad V_i=[E,W_i]\quad(i=3,4),
\]
\[
\mathcal V=[V_3(x)\mid V_4(x)],\qquad
L_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix}.
\]
Retain
\[
\operatorname{rank}_{\operatorname{Frac}B}\mathcal V=2,\qquad
h_3=c\in k^4\setminus\{0\},\qquad h_4=0.
\tag{2}
\]
Thus the original flow degree is exactly three and its highest
vector is nonzero and constant.

The actual companion identities from
[pass39, Sections 2--4](two-quadratic-defects-pass39.md) are
\[
\mathcal M=
\begin{pmatrix}J&-\mathcal V/2\\L_0&0\end{pmatrix},
\qquad \mathcal M^6=0,\qquad
(\mathcal M^j)_{\mathrm{UL}}=\frac{\operatorname{Jac}h_j}{j!}.
\tag{3}
\]
The rank-preserving block lemma there applies because \(\mathcal V\)
is injective and \(L_0\) is surjective. Apply it successively to
\(\mathcal M^5,\mathcal M^4,\mathcal M^3\): their upper-left blocks
vanish, so
\[
\mathcal M^3=0.
\]
The same source proves \(\operatorname{rank}\mathcal M\ge4\).
A six-dimensional nilpotent matrix of cube zero has rank at most
four, with equality only for Jordan type \((3,3)\). Consequently
\[
\operatorname{rank}\mathcal M^2
=\operatorname{rank}\operatorname{Jac}h_2=2.
\tag{4}
\]
This is precisely the two-longest-block boundary not covered by
the \(m\ge4\) affine-layer conclusion in
[pass42, Section 6](two-quadratic-top-line-pass42.md#6-a-separate-constant-top-full-row-refinement).

Put \(\ell=L_0h_2\). The actual top identities give
\[
L_0c=0,\qquad
Jc=\mathcal V\ell,\qquad
0=\frac32\mathcal V\operatorname{Jac}\ell.
\tag{5}
\]
Injectivity of \(\mathcal V\) makes \(\ell\) a complex constant
two-vector. Make a constant invertible change only in the good
coordinate pair to arrange \(c=(1,0,0,0)^{\mathsf t}\). Then
\[
h_2=(\sigma,u,\ell_3,\ell_4)^{\mathsf t},
\qquad E\sigma=1,\qquad Eu=0.
\tag{6}
\]
Equation (4) says that \(d\sigma,du\) are independent. In particular
\(u\) is nonconstant. This produces an actual slice \(\sigma\),
but it does not make \(\sigma\) a polynomial coordinate.

## 2. Which fields annihilate the preceding layer

The original conjugated partials have coefficient matrix
\[
C(z)=I-zJ+\frac{z^2}{2}\mathcal V L_0,
\]
and the actual flow satisfies
\[
\operatorname{Jac}(\exp(zE)x)\,C(z)=I.
\tag{7}
\]
The flow Jacobian is \(I+zJ+z^2\operatorname{Jac}h_2/2\),
since \(h_3\) is constant.

For a good column, the coefficient of \(z^3\) in (7) gives
\(W_i(h_2)=0\). For a bad column, the coefficients of \(z^4\)
and \(z^3\), respectively, give
\[
V_j(h_2)=0,\qquad
V_j(P)=-W_j(h_2)\quad(j=3,4).
\tag{8}
\]
Since the last two components of \(h_2\) are constant, the
second equality also proves
\[
V_j(P_3)=V_j(P_4)=0.
\tag{9}
\]
Thus both defect fields kill \(\sigma,u\), and both good tops
kill \(\sigma,u\). These statements concern the actual fields;
they do not declare the middle bad fields \(W_3,W_4\) to be LNDs.

The highest-coefficient argument in pass39 proves that
\(E,W_1,W_2,V_3,V_4\) are commuting LNDs. Since
\(V_3,V_4\) have rank two and kill \(\sigma\), whereas \(E\sigma=1\),
\[
\operatorname{rank}(E,V_3,V_4)=3.
\tag{10}
\]

## 3. The entire joint kernel is a polynomial curve

Define the actual subring
\[
R_1=\ker E\cap\ker V_3\cap\ker V_4\subseteq B.
\]
It contains the nonconstant \(u\). Its fraction field has
transcendence degree at most one: independent differentials of
joint invariants annihilate the three-dimensional distribution
in (10), and the differential space over \(\operatorname{Frac}B\)
has dimension four. Characteristic zero identifies this differential
rank with transcendence degree. Therefore
\[
\operatorname{trdeg}_k\operatorname{Frac}R_1=1.
\]

The ring \(R_1\) is integrally closed in its fraction field.
Indeed an element integral over it is integral over \(B\), hence
belongs to the normal ring \(B\). Every derivation defining \(R_1\)
annihilates its fraction field, so that element belongs to \(R_1\).

The polynomial curve theorem, de Bondt Corollary 3.2 and Lemma 3.3,
now applies to this actual subalgebra of the polynomial four-ring,
without a finite-generation premise.[^curve] It gives an actual
nonconstant \(t\in B\) such that
\[
R_1=k[t],\qquad
B\cap k(t)=k[t],\qquad Et=V_3t=V_4t=0.
\tag{11}
\]
In particular \(u=U(t)\) for a nonconstant \(U\in k[T]\).
Since \(W_1u=W_2u=0\), characteristic zero and the domain property
give \(W_1t=W_2t=0\) as well.

Every \(t-\alpha\) is irreducible in \(B\): a nontrivial factorization
would, by factorial closure of the three LND kernels, be a
factorization inside \(k[t]\). This statement does not identify
the fibers as polynomial three-rings.

## 4. The entire defect kernel and the speed normal form

Let
\[
R_2=\ker V_3\cap\ker V_4\subseteq B.
\]
Commutation makes \(R_2\) stable under \(E\), and (8) puts the
actual slice \(\sigma\) in \(R_2\). Applying the slice identity
inside this ring, with no quotient or field extension, gives
\[
R_2=R_1[\sigma]=k[t,\sigma].
\tag{12}
\]
For completeness, if \(b\in R_2\) has \(E\)-degree \(n\),
then \(E^nb\in R_1\). Subtract
\((E^nb)\sigma^n/n!\) and induct on \(n\). This proves generation;
algebraic independence follows by applying powers of \(E\)
to a hypothetical polynomial relation.

Equation (9) places the actual bad speeds in \(R_2\).
Since \(EP_j=\ell_j\), (12) gives polynomials \(L_3,L_4\in k[T]\)
with
\[
P_3=\ell_3\sigma+L_3(t),\qquad
P_4=\ell_4\sigma+L_4(t).
\tag{13}
\]

If \(\ell=0\), equation (5) makes \(Jc=0\). Thus the actual
constant good partial \(T_c\) commutes with \(E\).
The complementary good partial and original slice satisfy
the already proved
[one-good-output-partial recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial).
Its original source gates are retained; no slice is transferred
to a different derivation. This branch has polynomial kernel.

Otherwise a constant invertible change within the bad coordinate
pair arranges \(\ell=(1,0)^{\mathsf t}\). Set \(f=P_3\).
Replacing \(\sigma\) by \(f=\sigma+L_3(t)\) in (12), and writing
\(F=L_3,\ G=L_4\), gives the exact remaining form
\[
\boxed{
\begin{aligned}
&\ker V_3\cap\ker V_4=k[t,f],\qquad Ef=1,\quad Et=0,\\
&E^2x=(f-F(t),U(t),1,0)^{\mathsf t},\\
&Ex_3=f,\qquad Ex_4=G(t).
\end{aligned}}
\tag{14}
\]
All changes made to the original four coordinates so far are
complex constant changes preserving the two good and two bad
subspaces. The replacement of \(\sigma\) by \(f\) is a change of
generators of the proved kernel (12), not a new ambient frame.

If \(G\) is constant, \(x_4\) is either a fixed ambient coordinate
or an ambient coordinate with nonzero constant \(E\)-derivative.
Derksen--van den Essen--van Rossum Corollary 4.5 recognizes both
cases using the original slice.[^recognition]
Thus an instance not already recognized in this reduction has
both \(U\) and \(G\) nonconstant.

## 5. A recognition test in any constant ambient direction

Suppose some nonzero actual constant direction \(T\) satisfies
\[
Tt=0.
\tag{15}
\]
The fields \(E,V_3,V_4\) are commuting LNDs, have rank three,
and have joint kernel \(k[t]\). Therefore the complete
[omitted-coordinate commuting criterion](commuting-coordinate-descent-pass43.md)
applies. It proves that their common kernel is generated by an
ambient coordinate, and recognizes the original kernel as \(k^{[3]}\).

This invocation retains the criterion's precise source steps:
Maubach's joint-kernel and full-dimensional commuting-action
statements, complex surface cancellation, and the coordinate
theorem on an actual three-ring after the omitted direction.
It does not assert the general four-variable commuting derivations
conjecture.

Unlike the test involving only two good directions, (15) permits
any constant direction in the actual four-ring. Hence an instance
still unrecognized after these criteria must satisfy
\[
T_1t,\ T_2t,\ T_3t,\ T_4t
\quad\hbox{complex-linearly independent}.
\tag{16}
\]
This is linear independence over \(k\), not over the fraction
field and not algebraic independence.

## 6. The remaining obligation

Equations (11)--(14) identify actual polynomial subrings and
actual speeds. They do not establish
\[
B=k[t,f]^{[2]},\qquad
B=k[t]^{[3]},\qquad
\text{or that }t\text{ is an ambient coordinate}.
\]
The base \(k[t,f]\) is killed by the two defects but is not killed
by \(E\): its restriction is \(\partial_f\).
It therefore cannot simply be substituted for the invariant base
of the degree-two graph theorem in pass64.

The lower good velocities \(Ex_1,Ex_2\), the actual inclusion of
\(k[t,f]\) in \(B\), and the genuine coordinate inverse remain
to be controlled when \(G\) is nonconstant and (16) holds.
The existence of the slice \(f\), or the polynomial description
of the common kernel, does not solve that obligation.

This note deduplicates the constant-top companion bounds in
passes39/42 and the recognition criterion in pass43. The additional
cubic statement is the exact full-kernel and speed reduction
(11)--(14), together with its stated application of the existing
criterion. It does not assert that the residual alternatives are
realized or that the whole supplied profile is recognized.

## Source and verification scope

The actual-flow coefficient and companion inputs were reread in full
in the cited pass39/42 notes. The curve source statement and its
presented proof were reread directly in the retained primary text.
The commuting-coordinate and one-good-partial results are used as
previously audited theorems with their linked source obligations,
not as freshly proved classification results here.

This is a symbolic all-instance deduction under (1)--(2).
No numerical suite, scratch computation count, registry change,
or external submission is attached to it. Frozen earlier notes
and shared metadata were not edited.

[^curve]: M. de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 and Lemma 3.3, PDF pp. 20--21, with their proof following Theorem 3.1. The corollary applies to any transcendence-degree-one subalgebra of a polynomial ring and identifies its integral closure; normality of the actual joint kernel supplies equality here. [Retained primary text](../tmp/pdfs/bondt-1501.06046v4.txt).

[^recognition]: H. Derksen, A. van den Essen and P. van Rossum, [*The Cancellation Problem in Dimension Four*](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), Nijmegen Report 0022, Theorem 4.4 and Corollary 4.5, printed pp. 8--9. The selected complete statements and proofs were directly read for the preceding pass64 audit. Corollary 4.5 permits \(E(x_4)\in k[x_4]\), in particular a complex constant; its fixed-coordinate case uses the supplied slice over the actual Dedekind base \(k[x_4]\).

