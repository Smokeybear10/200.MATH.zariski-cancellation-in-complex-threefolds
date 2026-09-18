# Cuspidal residues are the repeated smooth-support boundary

Assuming the second-image obstruction has already vanished, the
repeated-plinth case has a more precise residual form than arbitrary
one-branch quadratic covers. Contractibility excludes every extra
even-multiplicity root away from the branch value. Each residue is
an odd power of one linear polynomial.

This is a conditional reduction, not removal of the second-image
obstruction. Higher image-ideal principality supplies no further test
after the global quadratic equation exists. The known Russell cubic
satisfies that entire package and is still nonpolynomial; its cylinder
is not asserted to be affine four-space.

## 1. Exact hypotheses and the global equation gate

Retain the actual degree-two independent-defect setup of
[pass 46](second-image-gluing-pass46.md), with
\[
A[s_*]\simeq\mathbb C^{[4]},\qquad
C=\ker D\simeq\mathbb C^{[2]},\qquad
\operatorname{pl}(D)=pC,\qquad Dr=p,
\]
where \(D\) is primitive. Assume the reduced support of \(p\)
is smooth and \(p\) is nonconstant. Its components are disjoint
affine lines by the established
[monodromy theorem](quadratic-monodromy-pass46.md).
The parallel-line argument from
[pass 47](smooth-plinth-recognition-pass47.md), using the published
Suzuki–Abhyankar–Moh theorem, works independently of multiplicities.
It gives coordinates \(u,v\) of the actual invariant plane with
\[
p=P(u)=\prod_{i=1}^k(u-a_i)^{n_i},\qquad
n_i\ge1,\quad a_i\ne a_j\ (i\ne j).
\tag{1}
\]
A nonzero constant factor has been absorbed into a presentation
variable. This does not make \(u\) an ambient coordinate.

Make the additional assumption
\[
J=C,\qquad I_2=pJ.
\tag{2}
\]
The exact second-image criterion, followed by completing the square,
then gives the whole ring
\[
A=\mathbb C[u,v,r,Y]/(P(u)Y-r^2-d(u,v)),\qquad
Dr=P,\quad DY=2r.
\tag{3}
\]
The actual minimal slice may have been translated by an invariant.
Without (2), (3) is not available, and none of the arguments below
silently treats the degree-two conic subalgebra as the whole ring.

Put
\[
d_i(v)=d(a_i,v),\qquad
C_i=\operatorname{Spec}\mathbb C[v,r]/(r^2+d_i(v)).
\]
Factorial closure in the UFD \(A\) makes \(u-a_i\) prime in
\(A\), so \(C_i\) is an integral reduced curve. Its generic
quadratic residue field is nontrivial. The one-branch monodromy
statement implies
\[
d_i(v)=c_i(v-b_i)h_i(v)^2,\qquad
c_i\in\mathbb C^*,\quad h_i\in\mathbb C[v]\setminus\{0\}.
\tag{4}
\]
Indeed the polynomial has exactly one root of odd multiplicity;
all other roots have even multiplicity. This is the square-class
conclusion in the actual coordinate \(v\), not just a parameter on
a different normalization.

## 2. The actual zero-fiber topology excludes the extra even roots

Let \(X=\operatorname{Spec}A\). Smoothness and contractibility follow
from its polynomial cylinder. Over the complement of the roots in
(1), equation (3) gives the actual open chart
\[
U=(\mathbb A^1\setminus\{a_1,\ldots,a_k\})\times\mathbb A^2.
\]
Its closed complement, with its actual underlying topology, is
\[
Z=\coprod_i C_i\times\mathbb A^1_Y.
\tag{5}
\]
The curves \(C_i\) can be singular. No generic smooth fiber is
substituted for them.

Use compactly supported cohomology with rational coefficients.
Poincare duality gives \(H_c^3(X)=0\), while Kunneth gives
\(H_c^4(U)=0\). The closed/open exact sequence therefore gives
\[
0=H_c^3(X)\longrightarrow
H_c^3(Z)\longrightarrow H_c^4(U)=0.
\]
The affine-line factor in (5) shifts degree by two, so
\[
\boxed{\quad H_c^1(C_i;\mathbb Q)=0\quad\text{for every }i.\quad}
\tag{6}
\]
This is the same compact-cohomology mechanism already recorded in
[the multiple-root note](multiple-root-linear-pass.md). Here it is
applied to the actual singular zero-fiber curves, whose special
quadratic normalization can be analyzed exactly. It does not claim
that an arbitrary acyclic singular plane curve is an embedded line.

Choose \(\gamma_i\in\mathbb C^*\) with
\(\gamma_i^2=-c_i\). The normalization in (4) is
\[
\nu_i:\mathbb A^1_w\longrightarrow C_i,\qquad
v=b_i+w^2,\quad r=\gamma_i w\,h_i(b_i+w^2).
\tag{7}
\]
It is finite because \(w\) is integral over the image. It is
birational because \(w=r/(\gamma_i h_i(v))\) in the function
field. Thus its normal source is the normalization.

At \(v=b_i\), (7) has one preimage. At a root of \(h_i\)
different from \(b_i\), it has exactly two distinct preimages
which are identified by (7). At every other point it has one
preimage. Repeated multiplicity of a root of \(h_i\) changes
the local singularity, but not this two-preimage count.

For completeness, a finite normalization of this complex curve
has the exact constant-sheaf sequence
\[
0\longrightarrow\mathbb Q_{C_i}
\longrightarrow(\nu_i)_*\mathbb Q_{\mathbb A^1}
\longrightarrow
\bigoplus_{q\in C_i}\mathbb Q_q^{\,b(q)-1}
\longrightarrow0,
\tag{8}
\]
where \(b(q)\) is the number of normalization preimages and only
the finitely many nonzero summands are included. At a singular
point the map on stalks is the diagonal inclusion into one
constant copy for each analytic branch. A sufficiently small
normalized neighborhood is a union of disks, so the higher
direct images vanish. Properness of the finite map permits
compact supports to be pushed forward.

Both connected affine curves are noncompact, and
\(H_c^1(\mathbb A^1)=0\). The compactly supported exact sequence
of (8) yields
\[
\dim_{\mathbb Q}H_c^1(C_i)
=\sum_q(b(q)-1)
=\#\{v\ne b_i:h_i(v)=0\}.
\tag{9}
\]
Equations (6) and (9) force all roots of \(h_i\) to equal
\(b_i\). Absorbing its nonzero leading coefficient into \(c_i\)
gives the promised normal form
\[
\boxed{\quad
d_i(v)=c_i(v-b_i)^{2k_i+1},\qquad k_i\ge0.
\quad}
\tag{10}
\]
The two integers \(n_i\) and \(2k_i+1\) describe different
features: the full plinth multiplicity and the cusp exponent of
the residue curve. No equality between them is asserted.

## 3. Smoothness locates every genuinely cuspidal residue

If \(k_i>0\), the residue equation has a singular point
\(v=b_i,r=0\). At the points of \(X\) over it, the gradient
of the equation in (3) is
\[
(P'(a_i)Y-d_u(a_i,b_i),\,0,\,0,\,0)
\tag{11}
\]
in the order \(u,v,r,Y\).

If \(n_i=1\), choosing
\(Y=d_u(a_i,b_i)/P'(a_i)\) would make the total space singular.
Thus \(k_i=0\) whenever \(n_i=1\). If \(n_i\ge2\), smoothness
instead requires
\[
\boxed{\quad
k_i>0\ \Longrightarrow\
n_i\ge2\quad\text{and}\quad d_u(a_i,b_i)\ne0.
\quad}
\tag{12}
\]
The last condition is also sufficient for smoothness along that
entire cusp line. At the other points of \(u=a_i\), one of
\(r\) and \(d_i'(v)\) is nonzero.

If every \(k_i=0\), the root specialization of the defining
polynomial is \(r^2+c_i(v-b_i)\), an actual plane coordinate.
Maubach's repeated-root theorem, already precisely sourced and
used in the multiple-root note, therefore makes the defining
polynomial a coordinate over \(\mathbb C[u]\).
Consequently \(A\simeq\mathbb C^{[3]}\). This positive
sufficiency is inherited, not a new coordinate theorem.

The remaining conditional equation branch thus has at least one
cusp exponent \(2k_i+1\ge3\) on a component of full plinth
multiplicity at least two.

## 4. Once J vanishes, all higher image ideals are already principal

This is an elementary consequence of the existing monic global
basis, not an additional freeness theorem. For the action in (3),
\[
\{Y^j,rY^j:j\ge0\}
\tag{13}
\]
is a \(C\)-basis. On \(A_P=C_P[r]\), the element of (13)
with degree \(n\) is
\[
b_n=\begin{cases}
Y^{n/2},&n\text{ even},\\
rY^{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
It has \(r\)-degree \(n\) and leading coefficient
\(P^{-\lfloor n/2\rfloor}\). Distinct basis elements have
distinct degrees, so nonzero invariant coefficients cannot cancel
the highest term. Since \(D=P\partial_r\) on this chart,
\[
F_n=\bigoplus_{j=0}^n Cb_j,\qquad
D^n b_n=n!P^{\lceil n/2\rceil},\qquad
\boxed{I_n=P^{\lceil n/2\rceil}C.}
\tag{14}
\]
The generic computation determines the actual filtration because
(13) is already an actual global \(C\)-basis.

In particular, requiring principality of all higher image ideals
adds nothing to (2) in this quadratic equation branch. It cannot
exclude the cusps in (10).

## 5. The known Russell cubic satisfies the complete weaker package

The already recorded Koras–Russell cubic, after replacing its
original \(y\) by \(-Y\), is
\[
A_{\rm KR}=
\mathbb C[x,v,r,Y]/(x^2Y-r^2-x-v^3),\qquad
D=x^2\partial_r+2r\partial_Y.
\tag{15}
\]
This is the existing example from
[pass 31](contractible-symmetry-pass31.md), not a new threefold.
Its contractibility and nonpolynomiality are published inputs.[^kr]

Here are the exact filtration data relevant to the proposed
extension. The ring is smooth: at \(x\ne0\) the \(Y\)-partial
is nonzero, and at \(x=0,r=v=0\) the \(x\)-partial is \(-1\).
The other points of \(x=0\) have a nonzero \(r\)- or
\(v\)-partial. The element \(x\) is prime because
\(r^2+v^3\) is irreducible. Its localization is
\(\mathbb C[x,x^{-1},v,r]\), so Nagata's criterion gives
factoriality, as already used in the old note.

The kernel of \(D\) is exactly \(\mathbb C[x,v]\).
Localization puts it in \(\mathbb C[x,x^{-1},v]\), and a
minimal \(x\)-pole is impossible because
\(\mathbb C[v]\) injects into
\(\mathbb C[v,r,Y]/(r^2+v^3)\).
The action is primitive: its values \(x^2,2r\) have gcd one
in the UFD. The monic basis (13) makes \(A_{\rm KR}\)
faithfully free over its kernel, and (14) gives
\[
\operatorname{pl}(D)=x^2C,\qquad J=C,\qquad
F_n=\bigoplus_{j=0}^n Cb_j,\qquad
I_n=x^{2\lceil n/2\rceil}C.
\tag{16}
\]
Thus even every degree module is free and every image ideal
is principal.

The normalized residue curve has the actual map
\[
v=-w^2,\qquad r=w^3.
\tag{17}
\]
It is an affine-line normalization with a degree-two polynomial
map to the base \(v\)-line, one finite branch value, and a cusp
at that value. At the generic prime \((x)\), (15) is already
the complete quadratic DVR equation, with full exponent two
and nonsquare residue square class \(-v^3\).
It has \(n_1=2,k_1=1,d_x(0,0)=1\) in (10)--(12).

The known \(\operatorname{ML}(A_{\rm KR})=\mathbb C[x]\)
precludes \(A_{\rm KR}\simeq\mathbb C^{[3]}\).
Hence smoothness, factoriality, contractibility, faithful-flat
polynomial kernel, a smooth reduced plinth support, complete
quadratic divisor models, \(J=C\), the one-branch cover condition,
and all higher freeness conditions still do not imply recognition.

No polynomial-cylinder isomorphism for (15) is asserted or denied
here. Nor is it asserted that (15) realizes the unresolved original
coordinate-partial frame. The precise remaining tasks under the
full cylinder hypothesis are to remove \(J\) where it may still
have basepoints, and then exclude or recognize the cuspidal
thickenings in (10)--(12) using additional actual-frame information.
Topology and higher image principality alone cannot supply that step.

## Verification boundary and attribution

The compact-cohomology mechanism and repeated-root positive theorem
were already recorded in the cited earlier notes. Equations
(7)--(10) supply the additional singular quadratic-fiber calculation;
(14)--(17) give the exact conjunction on the existing Russell example.
No historical novelty, universal cylinder recognition or formal
proof verification is claimed.

The standalone
[repeated_smooth_support_checks_pass48.py](repeated_smooth_support_checks_pass48.py)
passed both methods on its first run in 0.133 seconds, with exit
zero. The finite controls reconstruct normalization maps and branch
identifications, simple-versus-repeated-plinth gradient conditions,
the actual Russell action and inverse flow, and adapted basis degrees
zero through eight. They do not verify the cohomological or published
geometric inputs, and do not test any polynomial-cylinder isomorphism.

[^kr]: Adrien Dubouloz, [The cylinder over the Koras–Russell cubic threefold has a trivial Makar-Limanov invariant](https://arxiv.org/pdf/0807.4085), Introduction, PDF page 1; *Transformation Groups* 14 (2009), 531–539. This primary introduction was directly reread for the precise example, its diffeomorphism to real six-space, its Makar-Limanov invariant and nonpolynomiality, and the distinction between its cylinder invariant and a polynomial-cylinder isomorphism. These are inherited results; the original Makar-Limanov argument is not re-proved here.
