# An actual quadratic coordinate: relative-source and modification gates

The checked primary statements do not recognize the unknown invariant
threefold merely because one ambient coordinate is quadratic in its
supplied slice. The closest cancellation theorem genuinely permits an
unknown coefficient algebra, but requires a relative polynomial ring
in three variables, not the four-variable ring here. Residual-coordinate
theorems have a different obstruction: this quadratic polynomial is not
even a coordinate over the fraction field of its coefficient algebra.

This is a bounded statement-level audit, not a claim that no applicable
theorem exists, and not a novelty claim. The exact modification below
also distinguishes the quadratic cover from its affine modification; it
does not recognize either base as affine space.

## 1. Actual input and the two meanings of coordinate

Use the notation of the [centered-return proof](rank-one-centered-return-quotient-pass85.md).
The arguments here need only a sliced locally nilpotent derivation
\(E\) of an actual polynomial four-ring and one actual coordinate
\(z\) satisfying \(E^3z=0\), \(E^2z\ne0\). No time-degree bound
on the other three coordinates is used. Write

\[
 B=A[s]=\mathbb C[x_1,x_2,x_3,z],\qquad Es=1,\qquad
 z=w+\frac g2(hs^2+2vs),\qquad
 0\ne g,h\in A,\quad v,w\in A,\quad \gcd_A(h,v)=1.
 \tag{1}
\]

Here \(A=\ker E\) is a smooth factorial affine domain of dimension
three, \(A[s]\simeq\mathbb C^{[4]}\), and \(A^*=\mathbb C^*\).
The element \(z\) is a coordinate over \(\mathbb C\), with the displayed
three actual companions. No identification \(A\simeq\mathbb C^{[3]}\)
is assumed. To obtain the normalization directly in this broader
setting, put \(q=E^2z\), \(b=Ez\), and \(g=\gcd_B(q,b)\).
Factorial closure of \(A\) in \(B\) gives \(g,h=q/g\in A\);
then \(v=b/g-hs\in A\), \(\gcd_A(h,v)=1\), and integration in
\(A[s]\) gives (1).

For \(K=\operatorname{Frac}A\), the nonzero quadratic leading
coefficient in (1) gives

\[
 K[s]\ne K[z],\qquad [K(s):K(z)]=2,
 \qquad z\text{ is not a residual coordinate of }A[s]\text{ over }A.
 \tag{2}
\]

Indeed, division by the quadratic polynomial expressing \(z\) makes
\(K[s]\) free with basis \(1,s\) over \(K[z]\). Equivalently a polynomial
in \(z\) of positive degree has even \(s\)-degree. The residual-coordinate
condition already fails at the zero prime of \(A\).

The [Dutta--Lahiri definitions](https://arxiv.org/pdf/1908.03549)
2.2--2.4 explicitly keep the chosen base ring fixed. Their Theorem 3.6
makes an already residual coordinate stably coordinate over that same
base; it does not reverse this implication from absolute coordinatehood.
Their Theorem 3.2 treats \(aW+P\) over a one-dimensional affine base,
assuming that \(P\bmod a\) is already a coordinate. Neither prerequisite
is supplied by (1).[^dl]

The fixed polynomial ring in the centered-return proof is \(A[T]\),
where \(T=hs^2+2vs\). In that ring \(z=w+gT/2\) is an \(A\)-coordinate
if and only if \(g\in A^*\). Even though \(A[T]\) is abstractly a
polynomial four-ring, this is not a cancellation argument for \(A\).
Also, finiteness of \(B\) over \(A[T]\) and finiteness over \(A[z]\)
are different questions; no theorem is applied by interchanging these
two subrings.

## 2. Global centering and the closest cancellation statement

Completing the square in (1) gives

\[
 s'=s+\frac vh,\qquad
 z=\frac{gh}{2}(s')^2+w-\frac{gv^2}{2h}.
 \tag{3}
\]

This is an \(A\)-polynomial change of the slice exactly when \(h\mid v\),
which, by their coprimality, is equivalent to \(h\in A^*\). Every
\(A\)-automorphism of \(A[s]\) is affine in \(s\), and the coefficient of
its linear term in (1) vanishes only with this same center, up to the
unit rescaling of \(s'\). Thus a nonunit \(h\) cannot be removed merely
by choosing a different slice differing from \(s\) by an element of
\(A\). A nonlinear change involving unknown coordinates of \(A\) is not
being excluded.

Das's actual Theorem 3.4, in its characteristic-zero specialization,
has the following input and conclusion. Let \(R\supset\mathbb Q\) be
a Noetherian domain, \(C\) an \(R\)-algebra, and \(a,b\in C\). Then

\[
 C[t]=R[bt^n-a]^{[2]}=R^{[3]},\quad n\ge2
 \quad\Longrightarrow\quad
 C=R[a]^{[1]}=R^{[2]}.
 \tag{4}
\]

The theorem also supplies \(C[t]=R[bt^n-a,t]^{[1]}\).
This is stronger in its coefficient-algebra scope than a theorem which
starts with \(C=R^{[2]}\), but its relative dimension is essential.[^das]

Even when (3) is global, (1) gives
\(A[s']=\mathbb C[z]^{[3]}\), not the hypothesis
\(A[s']=\mathbb C[z]^{[2]}\) of (4). Choosing a nonconstant invariant
\(u\in A\) and declaring \(R=\mathbb C[u]\) does not repair this:
one would have to prove \(B=\mathbb C[u,z]^{[2]}\) as that relative
algebra. Such a \(u\) would already be an actual invariant ambient
coordinate. The source does not construct this missing base.

Theorem 3.1 in the same paper, generalizing Wright, instead starts with
a normal affine coefficient domain \(C\) and an actual plane quotient
\(C[t]/(bt^n-a)=k^{[2]}\). Our actual quotients by \(z-\lambda\) are
three-dimensional polynomial rings, not planes. Theorems concerning
these different dimensions cannot be applied by renaming the unknown
coefficient algebra.

## 3. The exact quadratic cover and its affine modification

Fix \(\lambda\in\mathbb C\) and set \(R=A_h\). Since \(z\) is an
actual coordinate, \(C_\lambda=B/(z-\lambda)\simeq\mathbb C^{[3]}\).
The map \(A\to C_\lambda\) is injective: a nonzero multiple of
\(z-\lambda\in A[s]\) has positive \(s\)-degree and cannot lie in
\(A\). In particular \(g,h\) remain nonzero after passing to this ring.

With \(y=hs+v\), define \(L_\lambda=2h(w-\lambda)-gv^2\in A\).
Then the actual localized fiber is

\[
 (C_\lambda)_h
   =R[y]/(gy^2+L_\lambda),\qquad
 \mathcal S_\lambda=R[Y]/(Y^2+gL_\lambda),\qquad Y=gy.
 \tag{5}
\]

The first ring is a domain. Its generic quadratic polynomial is
irreducible over \(K\): localization embeds this domain into a
nonzero \(K\)-algebra, and the quotient of \(K[y]\) by that quadratic
is again a domain. Consequently the monic presentation of
\(\mathcal S_\lambda\) embeds it in \((C_\lambda)_h\).
It is a domain finite free of rank two over \(R\), and both rings
in (5) have the same fraction field.

The inclusion is exactly the affine modification

\[
 (C_\lambda)_h
  =\mathcal S_\lambda[Y/g]
  =\mathcal S_\lambda[(g,Y)/g].
 \tag{6}
\]

This uses the subalgebra-of-the-fraction-field definition in
Kaliman--Zaidenberg Proposition 1.1(b). It is an actual modification
of the cover \(\mathcal S_\lambda\), not a birational modification of
\(R\), since the field extension over \(K\) has degree two.[^kz]

The full ideal matters. If \(U\) is a new indeterminate, the correct
presentation can be written

\[
 \mathcal S_\lambda[Y/g]
   =\mathcal S_\lambda[U]/\big((gU-Y):g^\infty\big).
 \tag{7}
\]

To verify it, invert \(g\), substitute \(U=Y/g\), and contract the
resulting kernel. The unsaturated equations would, after eliminating
\(Y\), give \(g(gU^2+L_\lambda)=0\), not just
\(gU^2+L_\lambda=0\). Thus the unrestricted assertion that a modification
has only its displayed unsaturated equations is unavailable. The
primeness qualification in the source's Proposition 1.1(c) addresses
exactly this issue.

Nor is (6) automatically a normalization. At any point of
\(\operatorname{Spec}R\) with \(g=0\) and \(L_\lambda\ne0\), the cover
in (5) has the nonempty fiber \(Y^2=0\), but the modified ring has empty
fiber \(L_\lambda=0\). A finite integral normalization cannot remove
such points. This is a conditional boundary test, not an assertion
that every action has a point of this kind. The modification framework
does not transfer the known localized polynomial-ring structure of
\((C_\lambda)_h\) back to \(R\) without another theorem or geometric
argument.

## 4. Deduplication and the precise remaining source gap

The older [quadratic-slice literature audit](quadratic-slice-literature.md)
already separates absolute from residual coordinates, including an
explicit absolute coordinate whose specializations at a prescribed
base variable all fail to be coordinates. Its KVZ Theorem 4.27 gate
still requires a pure-power expression over an actual polynomial
three-ring and residual coordinatehood for a specified base variable.
The current \(A\) is not known to be such a ring. This pass freshly
checked the displayed primary statement, but does not claim a new
complete read of its proof or a new counterexample.[^kvz]

Likewise, the [relative hypersurface gates](relative-hypersurface-source-gates-pass79.md)
and [quadratic modification audit](quadratic-relative-modification-source-pass79.md)
concern an additional actual plane base \(S\simeq\mathbb C^{[2]}\),
relative affine-line fibers, or univariate denominator presentations.
The inclusions \(A\subset C_\lambda\) in (5) instead have generic
relative dimension zero. No such plane base or affine-line fibration
has been constructed from (1).

The unresolved source gate is therefore specific: one needs a theorem
which uses the actual absolute coordinate \(z\in A[s]\simeq\mathbb C^{[4]}\),
with the stated quadratic form, without presupposing an invariant
ambient coordinate, a relative polynomial three-ring, or residual
coordinatehood over an already identified base. None of the selected
primary statements supplies that implication. This bounded result does
not settle the mathematical implication itself.

No checker or full regression was run for this note. No external
contact was made, and no file from pass85 or earlier was changed.

[^dl]: A. K. Dutta and A. Lahiri, [*On Residual and Stable Coordinates*](https://arxiv.org/pdf/1908.03549), arXiv:1908.03549v1, 9 August 2019; [published DOI](https://doi.org/10.1016/j.jpaa.2021.106707). Freshly read Definitions 2.2--2.4, the complete displayed statement and proof of Theorem 3.2, and the statements of Theorems 3.4 and 3.6. The definitions on printed p. 2 were also visually checked. Original proofs of the quoted Maubach, Bhatwadekar--Dutta, and Kahoui--Ouali inputs were not freshly read.

[^das]: P. Das, [*On cancellation of variables of the form \(bT^n-a\) over affine normal domains*](https://arxiv.org/pdf/2002.02129), arXiv:2002.02129v1, 6 February 2020. Freshly read the complete displayed statement and proof of Theorem 3.4 on printed p. 7 and visually verified that page; Theorem 3.1 and Proposition 3.2 statements were also checked. The broader proof dependencies and Wright's original proof were not newly audited in full. The exact Theorem 3.4 allows the characteristic-zero Noetherian domain stated in (4), not only the normal base advertised in the abstract.

[^kz]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), arXiv:math/9801076v2, 27 February 1998; [published DOI](https://doi.org/10.1007/BF01236662). Freshly read Definition 1.1, Proposition 1.1 including its displayed proof, and the statement of Theorem 1.1. Printed p. 5 was visually checked. No fresh full proof of the topology or surface-recognition theorems is claimed. Equations (5)--(7) are the explicit algebraic application here, not a recognition conclusion attributed to this source.

[^kvz]: S. Kaliman, S. Vénéreau and M. Zaidenberg, [*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/pdf/math/0104204), arXiv:math/0104204v2, Theorem 4.27, printed p. 46. Its exact residual-variable premise was freshly checked; the earlier full-proof analysis remains attributed to the linked retained literature note.
