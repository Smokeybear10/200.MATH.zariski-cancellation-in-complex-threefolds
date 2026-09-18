# A DG leading line survives every single mixed slice shear

Date: September 18, 2026.

For the specific polynomial DG base below, every single elementary
change of one flow coordinate by an arbitrary polynomial in the slice
and the other two flow coordinates retains the same primitive intrinsic
top in every nonzero constant coordinate direction. This includes
shears that do not preserve the line of the flow-coordinate slice
derivation. The proof has no bound on the shear polynomial's degree.

This is a method obstruction on a known polynomial three-ring, not an
advance proving entry for an unknown cancellation factor. It covers
coordinate permutations and a final constant linear frame change, not
arbitrary preceding nonlinear changes or sequences of mixed shears.
General cancellation remains UNSOLVED; novelty is not asserted.

## 1. Whole derivation, local proof of nilpotence, and flow frame

Work over \(\mathbb C\). On \(A=\mathbb C[x,y,z]\), put
\[
 f=xz-y^2,\qquad r=x^3+yf,\qquad
 g=zf^2+2x^2yf+x^5,
\]
\[
 D=-2fr\partial_x+(6x^2r-g)\partial_y
       +(2xf^2+10xyr)\partial_z.
 \tag{1}
\]
These are the full coefficients, not a leading truncation. Direct
differentiation gives
\[
 D=\operatorname{Jac}(f,g,\cdot),\quad Df=Dg=0,\quad
 Dr=-fg,\quad xg=f^3+r^2.
 \tag{2}
\]
The following equality is an exact localization of the actual ring:
\[
 A_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r],\qquad
 x=\frac{f^3+r^2}{g},\quad y=\frac{r-x^3}{f},\quad
 z=\frac{g-2x^2r+x^5}{f^2}.
 \tag{3}
\]
Indeed these formulas recover all three generators; the last one is
the definition of \(g\) after substituting \(yf=r-x^3\).
In particular \(f,g,r\) are algebraically independent, since they
generate the three-dimensional fraction field. On (3),
\(D=-fg\partial_r\), so it is locally nilpotent there. Its polynomial
coefficients in (1) preserve \(A\), and injectivity into this localization
proves local nilpotence on \(A\) itself.

The derivation is primitive. The polynomial \(f\) is prime and does
not divide \(r\). Modulo \(f\), one has \(r=x^3\), \(g=x^5\), and
\(Dy=5x^5\ne0\). Any common prime divisor of \(Dx,Dy\) therefore
cannot divide \(f\); it would divide both \(r,g\), hence \(f^3\) by
(2), a contradiction. The identification of this retained example as
rank three with non-fence plinth is recorded in
[34, Section 4](intrinsic-rank-pass34.md). That classification is not
needed for the coefficient proof below.

On \(B=A[u]\), let \(E=\partial_u\), \(V=E+D\), and set
\[
 c_x=\exp(-uD)x,\quad c_y=\exp(-uD)y,\quad
 c_z=\exp(-uD)z,\quad U=u.
 \tag{4}
\]
This is a whole polynomial coordinate system. Explicitly, if
\(\Phi_i(t;X)=\sum_{j\ge0}t^jD^j(x_i)(X)/j!\) is the finite flow
polynomial, its inverse is \(x_i=\Phi_i(U;c_x,c_y,c_z)\), \(u=U\).
Both orders are the opposite finite flows with the independent variable
\(u\) held fixed. Write
\(T_i=\partial_{c_i}\) for the three partials holding \(U\) fixed.
The fourth partial is \(\partial_U=V\).

For a derivation moving \(A\), its horizontal degree means the largest
power of \(u\) in its values on \(x,y,z\). Its intrinsic top is the
coefficient derivation on \(A\) at that power. The coordinate partials
and their nonzero constant combinations below are whole LNDs, so their
intrinsic tops are LNDs by
the inherited extraction lemma in
[643, Section 1](primitive-leading-fixed-locus-frame-obstruction-pass643-working.md).

## 2. Reconstructing all exact degrees and tops

In (3), the substitution defining (4) is simply
\(r\mapsto r+fgu\), with \(f,g\) fixed. Consequently
\[
\begin{array}{c|ccc}
 &c_x&c_y&c_z\\ \hline
 \deg_u&2&6&10\\
 \operatorname{lc}_u&f^2g&-f^5g^3&f^8g^5
\end{array}
\qquad
 \ell_x=f^2g,\quad\ell_y=-f^5g^3,\quad\ell_z=f^8g^5.
 \tag{5}
\]
Here and below leading coefficients are elements of the original
fraction field, and the final top derivations will be polynomial.
Let \(R_c=r+fgu\). Since \(f(c)=f\), \(g(c)=g\), and \(r(c)=R_c\),
the whole partials obey
\[
 T_i f=f_i(c),\qquad T_i g=g_i(c),\qquad
 T_i r=r_i(c)-u\bigl(gf_i(c)+fg_i(c)\bigr).
 \tag{6}
\]
Subscripts on \(f,g,r\) denote their original coordinate derivatives.
For a short reconstruction of every leading calculation, use
\[
 (f_x,f_y,f_z)(c)=(c_z,-2c_y,c_x),\quad
 (r_x,r_y,r_z)(c)=(3c_x^2+c_yc_z,\ f-2c_y^2,\ c_xc_y),
\]
\[
\begin{aligned}
 g_x(c)&=\frac{3f^2c_z+2R_c(3c_x^2+c_yc_z)-g}{c_x},\\
 g_y(c)&=\frac{-6f^2c_y+2R_c(f-2c_y^2)}{c_x},\\
 g_z(c)&=3f^2+2R_cc_y.
\end{aligned}
 \tag{7}
\]
The first two identities follow by differentiating \(xg=f^3+r^2\).
Their fraction-field use is only a calculation of actual polynomial
partials; it does not replace the whole frame by a rational one.
Equations (5)--(7) give the table
\[
\begin{array}{c|ccc|c|c}
 i&\deg T_if&\deg T_ig&\deg T_ir&
 \operatorname{lc}(T_ig)&\operatorname{lc}(T_ir)\\ \hline
 x&10&15&16&-2f^{12}g^8&f^{13}g^8\\
 y&6&11&12&-4f^9g^6&2f^{10}g^6\\
 z&2&7&8&-2f^6g^4&f^7g^4
\end{array}.
 \tag{8}
\]
For example the three leading coefficients of \(r_i(c)\) are
\(-f^{13}g^8,-2f^{10}g^6,-f^7g^4\). Subtracting \(ufg_i(c)\)
changes them to the last column of (8); the \(ugf_i(c)\) terms have
strictly lower degrees. This verifies rather than assumes the possible
leading cancellations in (6).

The highest coefficient in each row kills \(f,g\), while
\(\partial_r=-D/(fg)\). Since \(f,g,r\) generate the fraction field,
(8) therefore proves the exact horizontal degrees and intrinsic tops
\[
\begin{array}{c|c|c}
 &q_i&\operatorname{top}(T_i)=t_iD\\ \hline
 T_x&16&-f^{12}g^7D\\
 T_y&12&-2f^9g^5D\\
 T_z&8&-f^6g^3D
\end{array},\qquad \operatorname{top}(V)=D,\quad q_V=0.
 \tag{9}
\]
The nonzero top on the fraction field also ensures that the horizontal
degree cannot drop when measured on the original generators.

## 3. Every polynomial single shear, including all constant directions

Choose any permutation \((i,j,k)\) of \((x,y,z)\) and any
\(P\in\mathbb C[U,c_j,c_k]\). The new coordinates are
\[
 v_i=c_i+P(U,c_j,c_k),\quad v_j=c_j,\quad v_k=c_k,\quad U=u.
 \tag{10}
\]
The inverse subtracts \(P\), then uses the inverse in (4). Its complete
coordinate partials are
\[
 S_i=T_i,\quad S_j=T_j-P_jT_i,\quad S_k=T_k-P_kT_i,
 \quad S_U=V-P_UT_i.
 \tag{11}
\]
The derivatives of \(P\) hold its other displayed variables fixed.
Thus every constant direction in this frame has the exact form
\[
 L=a_jT_j+a_kT_k+a_UV+Q(U,c_j,c_k)T_i,
 \quad Q=a_i-a_jP_j-a_kP_k-a_UP_U.
 \tag{12}
\]

Put \((n_x,n_y,n_z)=(2,6,10)\) and give \(U,c_x,c_y,c_z\) weights
\(1,2,6,10\). The exponent vectors
in \(f,g\) of \(\ell_x,\ell_y,\ell_z\) are
\((2,1),(5,3),(8,5)\); the determinants for their three pairs are
\(1,2,1\). Hence, for any remaining pair, substitution
\[
 U\mapsto u,\qquad c_j\mapsto\ell_j u^{n_j},\qquad
 c_k\mapsto\ell_k u^{n_k}
 \tag{13}
\]
is injective on the polynomial algebra in these three variables.
Indeed equality of the two \(f,g\) exponents first forces equality of
the exponents of \(c_j,c_k\), then equality of the \(u\) exponents.
Therefore a nonzero \(Q\) has exact substituted degree equal to its
weighted degree and a nonzero leading coefficient in
\(\mathbb C[\ell_j,\ell_k]\). There is no hidden cancellation inside
an arbitrary high-degree shear polynomial.

If \(Q\ne0\), then \(QT_i\) has degree at least eight, so its top
cannot cancel against \(a_UV\). The unchanged \(T_j,T_k\) have
distinct degrees. A tie between \(QT_i\) and an unchanged partial
of greater or equal degree would require the following leading
coefficient of \(Q\):
\[
\begin{array}{c|c|c|c}
 i&\text{unchanged partial}&\text{required ratio}&
 \text{exponents in the remaining pair}\\ \hline
 y&T_x&t_x/t_y=f^3g^2/2&(\ell_x,\ell_z):(-1/2,1/2)\\
 z&T_x&t_x/t_z=f^6g^4&(\ell_x,\ell_y):(-2,2)\\
 z&T_y&t_y/t_z=2f^3g^2&(\ell_x,\ell_y):(-1,1)
\end{array}.
 \tag{14}
\]
None is a nonnegative integral pair. Distinct monomials in
\(\ell_j,\ell_k\) have distinct \(f,g\) exponents, so a polynomial
sum cannot produce a missing monomial either. When \(i=x\), its
degree already exceeds the other two, and no tie is possible.
Nonzero constants multiplying the ratios do not affect this argument.

It follows that every nonzero constant direction in (12) has a nonzero
intrinsic top in \(\mathbb C[f,g]D\). If \(Q=0\), the distinct degrees
of the remaining nonzero terms give the same conclusion. The only
case with no such term is the zero direction itself. Since \(D\) is
primitive, removing the polynomial gcd from any of these tops gives
\(D\) up to a scalar. Thus the extracted generic span is exactly one
after every (10) and every final invertible constant linear frame change.

## 4. Two shear orders: exact formulas, not an extended obstruction

For any polynomial-base LND, the following whole formulas apply in
its flow frame \((c_1,c_2,c_3,U=u)\). They specify what would have to
be analyzed for a longer operation sequence.

First perform (10) with target 1, then set \(W=U+H(v)\), where
\(H\in\mathbb C[v_1,v_2,v_3]\). With the fields \(S\) from (11),
the final partials and inverse are
\[
 R_i=S_i-H_i(v)S_U,\quad R_W=S_U;\qquad
 U=W-H(v),\quad c_1=v_1-P(U,v_2,v_3),\quad c_j=v_j\ (j=2,3).
 \tag{15}
\]
Conversely, first set \(W=U+H(c)\), giving
\(B_i=T_i-H_i(c)V\), \(B_W=V\), and then replace
\(c_1\) by \(v_1=c_1+P(W,c_2,c_3)\). The result is
\[
 R_1=B_1,\quad R_j=B_j-P_j(W,c_2,c_3)B_1\ (j=2,3),
 \quad R_W=V-P_W(W,c_2,c_3)B_1,
\]
\[
 c_1=v_1-P(W,v_2,v_3),\quad c_j=v_j\ (j=2,3),
 \quad U=W-H(c).
 \tag{16}
\]
In both cases the last inverse step is the original finite flow.
These actual inverse pairs certify local nilpotence of every partial.
The single-shear proof does not establish the same top-line conclusion
for arbitrary \(H\) in either order. Products in (15), or replacement
of \(U\) by \(u+H(c)\) in (16), introduce leading-cancellation questions
not covered by (13)--(14). No claim about their existence or absence is
being made here.

## 5. Deduplication, checks, and status

The whole base is retained in [611](rank-three-dg-degree-five-joint-return-reduction-pass611-working.md).
[26](fence-centralizer-sector-pass26.md) already gives the non-fence
commuting-LND centralizer obstruction. [643](primitive-leading-fixed-locus-frame-obstruction-pass643-working.md)
already realizes arbitrary primitive tops in whole polynomial frames,
with individual-replica and vertical-shift closures.
[33](cross-frame-saturation-pass33.md) treats the span across all frames;
[649](simultaneous-replica-and-whole-frame-descent-gates-pass649-working.md)
separates coordinate replacement from valid height descent.
The single-shear gate in [75](nice-good-direction-construction-boundary-pass75.md)
concerns preservation of niceness for a different action.
The additional bounded calculation here is (5)--(14), not a general
centralizer, rank, frame-selection, or cancellation theorem.

Fresh unsaved exact algebra verified all coefficients in (1), (2),
the primitive gcd, and the complete parameter expressions (6)--(8).
The universal quantifier on \(P\) is proved by the injective initial
substitution and the three impossible ratios, not by a finite search.
Two preliminary scratch invocations stopped at a missing SymPy import;
the later independent-runtime calculations completed successfully.
No saved checker was executed, imported, or compiled. The author did
not change canonical files while constructing this note.

The complete held source, 282 lines/11422 bytes, had SHA256
b9a70c9679239c6836c07a33103f1343e6c3143ab04ac6df144bd122de2a6795.
Root read it through EOF in651631 and independently checked all
degree/leader tables and forbidden ratios in fresh unsaved8ae0a7.
Geometry read the complete source in87ba6e/d35976, verified hash1bee51,
and reconstructed all arguments CLEAN. Jet read the complete source
in9b13e8/c45d1a, verified hashcec4d9, and reported CLEAN after fresh
independent algebra d2b7cc. Jet's preliminary scratch comparison
afa121 failed on differently factored symbolic expressions;450770
found zero polynomial differences and the corrected complete check
passed. These checks support the formulas, while the universal
single-shear claim rests on the written initial-substitution proof.
This final addition records provenance only. These are internal AI
reviews of a private working proof, not expert or formal certification.
