# Where the actual fiber can meet the quartic model

The actual fiber avoids every point where an individual vertical component
of the quartic model is Cartier. In particular its image lies in the
singular locus of that model. When the finite quadratic residue algebra
is exactly \(\mathbb C\), two explicit affine equations hold in the
entire actual fiber ring, not merely on its reduction. A nonzero
determinant then makes the image of the entire \(F_4\)-generated algebra
equal to the constants on that fiber.

This does not exclude the obstruction point. A flat polynomial overring
can contract its line fiber to exactly such a singular point. The control
below has the same quartic equations but not the required full image
ideals or filtration, so it is not a realization of the unresolved frame.

## 1. Exact inputs and a Cartier-avoidance lemma

Retain the hypotheses and the exact presentation of
[the quartic fiber theorem](quartic-fiber-gate-pass52.md). Thus
\(R=C_{\mathfrak m}\) is a regular local surface ring with residue
field \(k=\mathbb C\), \(\mathfrak n=(a,b)\), and
\(\mathcal A=A\otimes_C R\) is a faithfully flat domain. Its closed
fiber is a nonempty curve. In addition to the actual frame setup, the
quartic theorem assumes
\[
JR=\mathfrak n,\qquad B_1,B_2\in\mathfrak n^2.
\tag{1}
\]
Write
\[
K=K_4=R[F_4]=R[z,w,U,V]\subset\mathcal A.
\]
The previously proved presentation is
\[
K=R[Z,W,U,V]/(F_1,F_2,F_3),
\quad
\begin{cases}
F_1=bV-Q_{aa},\\
F_2=aV+bU+Q_{ab},\\
F_3=aU-Q_{bb}.
\end{cases}
\tag{2}
\]
Here the three \(Q\)'s belong to \(R[Z,W]\). This is a domain
complete intersection of dimension three, and
\[
K/\mathfrak nK=S_0[U,V],\qquad
S_0=k[Z,W]/(\bar Q_{aa},\bar Q_{ab},\bar Q_{bb}),
\quad 1\le\dim_k S_0\le3.
\tag{3}
\]
In particular each reduced irreducible component of the vertical fiber
has height one in \(K\). This also follows directly in the regular
ambient ring: its vertical component has height four and the defining
complete intersection has height three.

**Cartier-avoidance lemma.** More generally, suppose \(R\) is a regular
local surface, \(\mathcal A\) a flat domain over \(R\), and
\(K\subset\mathcal A\) an \(R\)-subalgebra domain. Let \(y\) be a
point over \(\mathfrak n\), and suppose there is a prime
\(P\subseteq y\), containing \(\mathfrak nK\), such that
\(PK_y=(\tau)\). Then no point of \(\operatorname{Spec}\mathcal A\)
maps to \(y\).

Indeed, if \(x\) mapped to \(y\), the local map
\(K_y\hookrightarrow\mathcal A_x\) would send \(\tau\) to a nonzero
nonunit. Since \(a,b\in P\), write
\[
a=\tau a',\qquad b=\tau b'
\quad\text{in }\mathcal A_x.
\]
Flatness preserves the regular sequence \(a,b\). But
\(ba'=b'a\), while \(a'\notin a\mathcal A_x\): otherwise
\(a'=ac\), and cancellation in the domain gives \(1=\tau c\).
Thus \(b\) is a zero divisor modulo \(a\), a contradiction.

This proof requires neither factoriality of \(\mathcal A_x\) nor a
dimension estimate for the actual fiber. It applies in particular if
the whole vertical ideal, its radical, or any individual reduced
vertical component through \(y\) is locally principal. In the domain
\(K_y\), the corresponding nonzero equation is a non-zero-divisor,
so this is precisely the effective Cartier condition.

Every height-one prime in a regular local ring is principal. Applying
the lemma to (2)--(3) gives the topological support restriction
\[
\operatorname{im}\bigl(
\operatorname{Spec}(\mathcal A/\mathfrak n\mathcal A)
\longrightarrow\operatorname{Spec}K\bigr)
\subseteq
\operatorname{Sing}(K)\cap V(\mathfrak nK).
\tag{4}
\]
More precisely, every vertical component through an actual image point
must be non-Cartier there. The statement (4) by itself is about points.
It does not say that the Jacobian ideal vanishes in a possibly
nonreduced actual fiber ring.

The primary algebra inputs, whose statements and proofs were directly
read for this argument, are flat preservation of regular sequences,
[Stacks 00LM](https://stacks.math.columbia.edu/tag/00LM), regular local
rings being UFDs,
[Stacks 0AG0](https://stacks.math.columbia.edu/tag/0AG0), and the local
equation characterization of effective Cartier divisors,
[Stacks 01WS](https://stacks.math.columbia.edu/tag/01WS).

## 2. The precise singular subset of each vertical plane

Fix a point \((z_0,w_0)\) in the support of \(S_0\). Define
\[
G=
\left.
\begin{pmatrix}
-\partial_Z\bar Q_{aa}&-\partial_W\bar Q_{aa}\\
 \partial_Z\bar Q_{ab}& \partial_W\bar Q_{ab}\\
-\partial_Z\bar Q_{bb}&-\partial_W\bar Q_{bb}
\end{pmatrix}
\right|_{(z_0,w_0)}.
\tag{5}
\]
For each \(Q_i\), let \(q_{i,a},q_{i,b}\) be its two linear
coefficients in \(\mathfrak n/\mathfrak n^2\) after substituting
\((z_0,w_0)\). Set
\[
\gamma_a=(-q_{aa,a},q_{ab,a},-q_{bb,a})^{\mathsf t},\quad
\gamma_b=(-q_{aa,b},q_{ab,b},-q_{bb,b})^{\mathsf t},
\]
\[
d_a=\gamma_a+(0,V,U)^{\mathsf t},\qquad
d_b=\gamma_b+(V,U,0)^{\mathsf t}.
\tag{6}
\]
This uses first jets in the regular parameter system \(a,b\), not an
assumption that every coefficient has a chosen global coordinate
derivative. On the vertical plane over \((z_0,w_0)\), the full
cotangent matrix has columns
\[
[\ d_a\mid d_b\mid G\mid 0\mid 0\ ].
\tag{7}
\]
The last two columns correspond to \(U,V\). A closed point is regular
exactly when this matrix has rank three. One can either compute the
embedding dimension in the six-dimensional regular ambient local ring
or apply the directly read regularity/cotangent criterion
[Stacks 00TS](https://stacks.math.columbia.edu/tag/00TS) on an affine
neighborhood. The local ring of \(K\) at a closed point of this plane
has dimension three.

Let \(r_G=\operatorname{rank}G\). The embedding dimension of the local
Artinian factor of \(S_0\) is \(2-r_G\).

* If \(r_G=2\), choose a nonzero left null vector
  \(\ell=(\ell_1,\ell_2,\ell_3)\) of \(G\). The singular subset is
  exactly the affine linear locus
  \[
  \ell_3U+\ell_2V+c_a=0,\qquad
  \ell_2U+\ell_1V+c_b=0,
  \quad c_a=\ell\gamma_a,
  \quad c_b=\ell\gamma_b.
  \tag{8}
  \]
  Its coefficient determinant is
  \(\ell_1\ell_3-\ell_2^2\). If this is nonzero, the locus is one
  point. Otherwise it is a line or empty: the coefficient matrix
  cannot have rank zero because \(\ell\ne0\).

* If \(r_G=1\), choose a nonzero column-image vector \(v\) of \(G\).
  The singular subset is the conic
  \[
  \det[\,v,d_a,d_b\,]=0.
  \tag{9}
  \]
  Its homogeneous quadratic part is
  \(-v_1U^2+v_2UV-v_3V^2\), which is not identically zero.
  Consequently this is a proper plane curve, possibly reducible or
  nonreduced.

* If \(r_G=0\), every point of this vertical plane is singular.
  The Cartier-avoidance argument alone then gives no smaller
  Jacobian support bound.

These are restrictions on the actual image, not equalities with that
image. With several factors of \(S_0\), the computation applies
separately to each plane. An empty singular locus on one plane does not
contradict nonemptiness of the actual fiber if it can meet another
plane.

## 3. Length one: equations in the entire actual fiber ring

Assume now \(S_0=k\), so that there is only one support point and its
scheme is reduced. Put \(\bar{\mathcal A}=\mathcal A/\mathfrak n\mathcal A\).
The actual residues satisfy
\[
\bar z=z_0,\qquad \bar w=w_0
\quad\text{in }\bar{\mathcal A},
\]
even if \(\bar{\mathcal A}\) itself is nonreduced. Choose actual
elements with
\[
z-z_0=az_a+bz_b,\qquad w-w_0=aw_a+bw_b.
\tag{10}
\]
Flatness identifies
\[
\mathfrak n\mathcal A/\mathfrak n^2\mathcal A
\simeq (\mathfrak n/\mathfrak n^2)
\otimes_k\bar{\mathcal A}
\simeq \bar{\mathcal A}^{\,2}.
\]
Expanding the three actual equations (2) to first order in
\(\mathfrak n\), and comparing the \(a,b\) coefficients, gives
\[
G\binom{\bar z_a}{\bar w_a}+d_a(\bar U,\bar V)=0,
\qquad
G\binom{\bar z_b}{\bar w_b}+d_b(\bar U,\bar V)=0.
\tag{11}
\]
Left multiplication by \(\ell\) proves that both equations (8) hold
in \(\bar{\mathcal A}\) itself. This is stronger than (4).

In particular, if
\[
\ell_1\ell_3-\ell_2^2\ne0,
\tag{12}
\]
then \(\bar U,\bar V\) are complex constants and
\[
\operatorname{im}(K/\mathfrak nK\longrightarrow\bar{\mathcal A})=k.
\tag{13}
\]
The same is true of the image of the full module \(F_4\), whose basis
is \(1,z,w,U,V\). Equation (13) does not make
\(\bar{\mathcal A}\) zero-dimensional. Its nonconstant elements must
come from higher intrinsic degrees.

If the coefficient determinant vanishes, the two equations must be
consistent because the actual fiber is nonempty. They factor the
\(k[U,V]\)-image through an affine line, possibly through a further
quotient. No reduced-line description of the whole actual fiber, or
pointwise plinth conclusion, follows from this assertion.

## 4. Exact point-contraction control in the same quartic shape

Here is a polynomial control showing why point contraction is not by
itself impossible. It deliberately drops the full filtration and
minimal-plinth premises.

Take \(R=k[a,b]_{(a,b)}\), \(p=a^3+b^3\), and
\(\mathcal A_0=R[t]\). Define
\[
r=pt,\quad
z=a^2t+\frac{bp}{2}t^2,\quad
w=b^2t-\frac{ap}{2}t^2,
\tag{14}
\]
\[
\begin{split}
U&=-2at-a^2bt^2-b^2pt^3+\frac{ap^2}{4}t^4,\\
V&= 2bt-ab^2t^2+a^2pt^3+\frac{bp^2}{4}t^4.
\end{split}
\tag{15}
\]
These obey \(az+bw=r\) and the exact equations
\[
bV=z^2+2w,\qquad
aV+bU+2zw=0,\qquad
aU=w^2-2z.
\tag{16}
\]
The abstract three-equation algebra in (16) embeds as
\(K_0=R[z,w,U,V]\subset R[t]\). For completeness, its exactness does
not require treating it as an actual obstruction: after inverting
\(a\) or \(b\), elimination leaves
\[
(aZ+bW)^2-2b^2Z+2a^2W=0.
\]
Over \(L=\operatorname{Frac}R\), the independent linear coordinates
\(r=aZ+bW\), \(j=-b^2Z+a^2W\), whose determinant is \(p\ne0\),
turn this into \(r^2+2j=0\). At each height-one base localization
one of \(a,b\) is a unit, and the conic polynomial is primitive over
that DVR, so generic irreducibility gives a domain there. The raw
closed residue ideal is
\[
(Z^2+2W,2ZW,W^2-2Z)=(Z,W).
\tag{17}
\]
Thus the same height and complete-intersection argument used in the
quartic presentation theorem excludes vertical minimal primes and
embedded primes. The abstract quotient injects into its generic ring
\(L[r]=L[t]\), proving the stated presentation of \(K_0\).

Its closed fiber is the plane \(k[U,V]\). Along that plane its
cotangent matrix is
\[
\begin{pmatrix}
0&V&0&-2&0&0\\
V&U&0&0&0&0\\
U&0&2&0&0&0
\end{pmatrix}.
\tag{18}
\]
The ideal of its three-by-three minors is \((U,V)\). Consequently
the only singular point on the plane is \(U=V=0\). All four elements
in (14)--(15) reduce to zero in \(\mathcal A_0/\mathfrak n\mathcal A_0=k[t]\),
so the entire reduced line is contracted to this point.

For \(D_0=\partial_t\), one has
\(D_0r=p\), \(D_0z=a^2+br\), and \(D_0w=b^2-ar\).
Nevertheless the full primitive plinth of \(D_0\) is the unit ideal,
not \(pR\), and its true \(F_4\) contains \(t\). The subalgebra
\(K_0\) is therefore not its full \(F_4\)-generated algebra. This
control meets the flat-overring and exact quartic-shape conditions,
not the actual obstruction's full image-ideal conditions.

## 5. Verification and the remaining obligation

An inline exact SymPy calculation verified all four identities
\(az+bw=r\) and (16), all four zero residues, matrix (18), the
minor ideal \((U,V)\), and the homogeneous conic coefficient in (9).
This was a standalone finite calculation, not a new unittest suite or
a universal proof by computation. The Cartier, conormal, and exact
presentation arguments are the written algebra above. The parallel
independent review reconstructed the support and conormal arguments
before this transcription; a full-file audit is separate.

The new positive restriction is (4), with the explicit cases (8)--(9)
and the scheme-theoretic strengthening (11)--(13). In the length-one,
nonzero-determinant sector, all actual fiber variation must first appear
outside \(F_4\). Nothing here proves that higher intrinsic generators
cannot supply it, that the fiber is a reduced translating line, or that
the full cancellation problem is settled.
