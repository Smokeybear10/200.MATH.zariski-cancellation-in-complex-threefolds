# The selected Su threefold cell is affine three-space

## 1. Result and precise scope

Work over an algebraically closed field \(k\) of characteristic zero. Fix the very generic regular semisimple monodromies in Su's setup

\[
(g,k_{\mathrm{punct}},n,\boldsymbol\mu)
=(0,6,2,((1,1)^6)).
\]

Choose all five Bruhat indices \(w_i=s_1\), and the chronological walk

\[
(p_0,\ldots,p_{10})=(1,s,s,s,1,s,1,s,1,s,1)
\tag{1}
\]

of \(\beta=\sigma_1^{10}\). The affine threefold attached to **this selected index** in Su's Theorem 2.10 is isomorphic to \(\mathbb A^3_k\). We reconstruct its actual four-dimensional affine prequotient, its actual additive action, and an explicit polynomial quotient below. This is a computation of a specified published candidate, not a general cancellation theorem or a novelty claim.

The source identification is essential: the conclusion does not follow merely from finding a convenient action on a matrix model with the right dimension. The relevant equivariance and removal of extra factors are checked in Section 2.

## 2. Identification with the actual character-variety cell

The primary source read is Tao Su, *Cell decomposition and dual boundary complexes of character varieties*, [arXiv:2307.16657v4](https://arxiv.org/pdf/2307.16657v4). The exact inputs are Definition 1.12, Definition 1.14, Proposition 1.16, equations (2.1.3), (2.2.5), (2.3.6)--(2.3.8), Lemma 2.5 including its proof, and the construction of \(A_{\boldsymbol\mu}(\mathbf w,p)\) in the proof of Theorem 2.10, manuscript pages 10--11, 13--18, and 21--23. Appendix A, Lemma A.1, provides the normalized coordinate recursion used below. Remark 2.12 supplies the context of the 80 proposed candidates, not their polynomiality.

Write

\[
H(z)=\begin{pmatrix}1&z\\0&1\end{pmatrix},\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
B(z)=SH(z)=\begin{pmatrix}0&1\\1&z\end{pmatrix}.
\tag{2}
\]

This is precisely Su's braid-matrix convention. Chronological multiplication is
\(P_j=B(\epsilon_j)\cdots B(\epsilon_1)\), not the reversed product.

For \(GL_2\), \(U_S^+=U\cap S^{-1}US=\{1\}\). Thus every extra factor \(U_{w_i}^+\cap N_i\) in (2.3.7) is trivial for our five chosen indices. There are no handle factors because \(g=0\). Consequently Su's canonical projection is an isomorphism

\[
M_B''(\mathbf w,p)\simeq\widetilde X_p(\sigma_1^{10}).
\tag{3}
\]

Crucially, Lemma 2.5(a) states that this projection is \(B\)-equivariant for **the action in Definition 1.14**. Its proof, equation (2.3.11), identifies the action by the original conjugation and puncture formulas. Hence the braid action computed in Section 4 is the action on this actual character-variety cell.

Let the fixed monodromies be \(C_i=\operatorname{diag}(c_{i,1},c_{i,2})\). Equations (2.1.3) and (2.2.5), with \(g=0\), give the fixed diagonal matrix

\[
D^0=D_1=\left(\prod_{i=1}^{5}C_i^S\right)C_6
=\operatorname{diag}(\kappa,\kappa^{-1}),\qquad
\kappa=c_{6,1}\prod_{i=1}^{5}c_{i,2}\in k^*.
\tag{4}
\]

The determinant-one assertion uses the generic monodromy determinant condition. No eigenvalue is replaced by a freely chosen matrix parameter. Very genericity in particular excludes \(\kappa=1\), although the explicit algebra below would remain valid for any nonzero \(\kappa\).

The source's defining equation (2.3.6) is
\(u^0D^0P_{10}=I\), with \(u^0\in U\). It is equivalent to fixing the diagonal monodromy of \(P_{10}\) to \((D^0)^{-1}\); the upper-unipotent factor \(u^0\) is then uniquely determined. It does not impose an additional equation on an affine up-coordinate.

## 3. Four actual affine coordinates and both coordinate maps

The walk has

\[
U_p=\{1,5,7,9\},\quad S_p=\{2,3\},\quad D_p=\{4,6,8,10\}.
\]

Use Su's normalized coordinates

\[
a=\epsilon'_1,\quad b=\epsilon'_5,\quad
c=\epsilon'_7,\quad d=\epsilon'_9,\qquad
r=\epsilon'_2\ne0,\quad z=\epsilon'_3\ne0.
\]

Here \(z\) is a stay-coordinate, not the permutation \(s\) in (1). Define \(q=-z/r\). The raw braid coordinates are

\[
\begin{aligned}
\epsilon_1&=a,&\epsilon_2&=r,&
\epsilon_3&=-\frac1r-\frac z{r^2},&
\epsilon_4&=\frac{r^2}{z},\\
\epsilon_5&=\frac{z^2}{r^2}
\left(b-a-\frac1z-\frac1r\right),&
\epsilon_6&=0,&
\epsilon_7&=\frac{z^2}{r^2}(c-b),\\
\epsilon_8&=0,&
\epsilon_9&=\frac{z^2}{r^2}(d-c),&
\epsilon_{10}&=0.
\end{aligned}
\tag{5}
\]

All denominators are invertible stay-coordinates. These are regular maps on the specified torus-times-affine cell, not rational maps restricted to an unspecified dense open subset.

Here is an independent derivation from the actual Bruhat recursion. For
\(P=\left(\begin{smallmatrix}A&B_0\\ C&D\end{smallmatrix}\right)\) with \(C\ne0\),

\[
P=H(A/C)S\operatorname{diag}(C,-\det(P)/C)H(D/C).
\tag{6}
\]

In rank two, the up formula (A.0.3) applied to an upper-triangular previous product \(P\) is
\(\epsilon'_j=(P_{22}/P_{11})\epsilon_j+P_{12}/P_{11}\).
For a stay, (6) and (A.0.5) give
\(\epsilon'_j=-C^2(\epsilon_j+A/C)/\det(P)\).
Thus the first two stays give
\(r=\epsilon_2\) and \(z=-r(1+r\epsilon_3)\), and the next down-step forces \(\epsilon_4=r^2/z\). After this down-step the product is upper triangular. Applying the up formula and the subsequent forced down-step three times gives exactly (5).

For completeness, the inverse formulas on the walk stratum are

\[
\begin{aligned}
r&=\epsilon_2,&z&=-r(1+r\epsilon_3),&a&=\epsilon_1,\\
b&=a+\frac1r+\frac1z+\frac{r^2}{z^2}\epsilon_5,&
c&=b+\frac{r^2}{z^2}\epsilon_7,&
d&=c+\frac{r^2}{z^2}\epsilon_9.
\end{aligned}
\tag{7}
\]

The lower-left entries of the successive products are
\(1,r,q,0,q,0,q,0,q,0\). Therefore (5) has exactly the prescribed Bruhat walk, including every nonvanishing condition. Conversely those conditions and the four down-steps force the relations in (5). Direct multiplication gives

\[
P_{10}=\operatorname{diag}(-z/r,-r/z)H(d)
=\operatorname{diag}(q,q^{-1})H(d).
\tag{8}
\]

Equations (4) and (8) impose precisely

\[
q=\kappa^{-1},\qquad z=-\kappa^{-1}r.
\tag{9}
\]

Thus \(\widetilde X_p\simeq\mathbb G_m\times\mathbb A^4\), with coordinates \((r;a,b,c,d)\). Moreover \(D^0P_{10}=H(d)\), so the eliminated source variable is explicitly \(u^0=H(-d)\).

The source affine factor is obtained by choosing a point of this torus. We choose \(r=1\), which forces \(z=-\kappa^{-1}\). This produces the actual four-dimensional affine prequotient with polynomial ring \(k[a,b,c,d]\). Any other nonzero fixed value of \(r\) gives the same computation.

## 4. Actual additive action, slice, and quotient

Let \(u=H(t)\in U\). Definition 1.14 pushes \(u^{-1}\) through the braid diagram beginning at its chronological first crossing. The exact elementary identity is

\[
B(\epsilon_1)H(-t)=B(\epsilon_1-t).
\tag{10}
\]

This equality uses only addition of adjacent handleslides in the very same crossing diagram. There is no residual upper-triangular factor. The later raw braid coordinates therefore remain unchanged:

\[
\epsilon_1\longmapsto\epsilon_1-t,
\qquad\epsilon_j\longmapsto\epsilon_j\quad(2\le j\le10).
\tag{11}
\]

By (7), the induced action in the actual normalized coordinates is

\[
t\cdot(r;a,b,c,d)=(r;a-t,b-t,c-t,d-t).
\tag{12}
\]

In particular the torus section \(r=1\) is invariant. Its action derivation, using the convention \(D(f)=\left.\frac d{dt}f(t\cdot x)\right|_{t=0}\), is

\[
D=-\partial_a-\partial_b-\partial_c-\partial_d.
\tag{13}
\]

Set

\[
\tau=-a,\qquad X=b-a,\qquad Y=c-a,\qquad Z=d-a.
\tag{14}
\]

Then \(D\tau=1\) and \(DX=DY=DZ=0\). These are polynomial coordinates: the explicit inverse is

\[
a=-\tau,\quad b=X-\tau,\quad c=Y-\tau,\quad d=Z-\tau.
\tag{15}
\]

Consequently

\[
k[a,b,c,d]=k[X,Y,Z,\tau],\qquad
\ker D=k[X,Y,Z],\qquad
\mathbb A^4/U\simeq\mathbb A^3.
\tag{16}
\]

This identifies the geometric quotient used to define Su's \(A_{\boldsymbol\mu}(\mathbf w,p)\), not merely a subring of its invariant ring. In the coordinates (14), its fibers are exactly the additive orbits and the quotient map is ordinary projection.

## 5. The residual torus quotient and the selected cell itself

For \(t_0=\operatorname{diag}(t_1,t_2)\), put \(\rho=t_1/t_2\). Su's Proposition 1.16(1)(b) gives

\[
(r,z)\longmapsto(\rho^{-1}r,\rho^{-1}z),\qquad
(a,b,c,d)\longmapsto(\rho a,\rho b,\rho c,\rho d).
\tag{17}
\]

Indeed each up-step has previous permutation \(1\), and each stay has previous permutation \(s\). Hence \(PT\) acts freely and transitively on the torus coordinate \(r\). Taking \(\rho=r\) normalizes it to \(1\) and gives invariant functions on the complete \(PB\)-quotient

\[
r(b-a),\qquad r(c-a),\qquad r(d-a).
\tag{18}
\]

After first taking \(U\)-invariants the ring is
\(k[r,r^{-1},X,Y,Z]\), with weights \((-1,1,1,1)\). Its weight-zero subring is exactly \(k[rX,rY,rZ]\): every weight-zero Laurent monomial has its power of \(r\) equal to its total degree in \(X,Y,Z\). This also gives a direct algebraic check of the full quotient.

Thus both the selected affine factor and, since its residual torus exponent is zero, the selected character-variety cell satisfy

\[
A_{\boldsymbol\mu}(\mathbf w,p)
\simeq\mathcal M_{\boldsymbol\mu}(\mathbf w,p)
\simeq\mathbb A^3_k.
\tag{19}
\]

## 6. Evidence and limits

The broad rank-two cancellation conclusion is already explicitly stated in Mellit's [published Section 1.4, page 160](https://link.springer.com/content/pdf/10.1007/s10240-025-00158-0.pdf), also present in his 2019 preprint. The [bounded literature comparison](literature-scope-pass37.md) records this inherited credit. The present contribution to this research ledger is the checked reconstruction of the specified Su coordinates and action.

The calculation uses Su's actual diagram normalization and equivariance theorem. The coordinate reconstruction, exact matrices, and quotient maps have also been independently reconstructed by the root agent and the jet-checking agent. The standalone [exact checker](su_cell_checks_pass37.py), written independently by the jet-checking agent, was fully read and independently run: **8 methods passed in 0.202 seconds**. It reconstructs Appendix A parameters from actual prefix matrices, checks both coordinate maps, the monodromy restriction, the actual additive and torus actions, and the quotient maps. Such controls do not replace the source-identification proof above.

This selected-index calculation removes this index from consideration as a nontrivial cancellation candidate. The separately audited [rank-two coordinate-slice argument](su-geometry-audit-pass37.md) extends the method to the other 79 indices while retaining their extra affine factors. Neither result decides higher-rank groups, all of Su's cells, arbitrary sliced actions on \(\mathbb A^4\), or the original characteristic-zero three-dimensional cancellation problem. No priority claim, public announcement, outreach, or submission is made. The proof has not been expert-reviewed or formalized in Lean.
