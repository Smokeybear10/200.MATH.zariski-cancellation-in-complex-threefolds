# The fourth image remains nonprincipal at a reduced zero-jet obstruction

The fourth-image alternative from pass 51 has a definite answer:
at a reduced actual obstruction with \(B_1,B_2\in\mathfrak n^2\),
\[
I_4=p^2\mathfrak n,
\qquad
F_4=R\oplus Rz\oplus Rw\oplus RT_a\oplus RT_b.
\]
In particular this holds at every actual second-image obstruction
lying at an ordinary triple point of the full primitive plinth.
It is not a statement about arbitrary reduced obstruction points
whose first derivative jets have rank one.

The proof uses an exact relation between the two actual quartic
corrections. Its coefficient on the cubic generator is a unit.
That excludes a principal fourth image without assuming a free
fourth filtration module or generation of the full algebra.

## 1. Full actual hypotheses

Use the actual local setup and quartic elements of
[the triple-point quartic note](triple-point-quartic-corrections-pass51.md).
Thus
\[
R=C_{\mathfrak m},\quad \mathfrak n=\mathfrak mR=(a,b),
\quad \mathcal A=A\otimes_C R,\quad L=\operatorname{Frac}R.
\tag{1}
\]
The ring \(C\simeq\mathbb C^{[2]}\) is the actual primitive
intrinsic LND kernel, \(A[s_*]\simeq\mathbb C^{[4]}\), and
\(\mathcal A\) is a faithfully flat domain over the regular
local surface ring \(R\). The parameters \(a,b\) generate the
proper local second-image ideal \(JR=\mathfrak n\).

Write \(F_i=\ker D^{i+1}\) and \(I_i=D^i(F_i)\subset R\).
The actual identities are
\[
F_2=R\oplus Rz\oplus Rw,\quad r=az+bw,\quad Dr=p,
\tag{2}
\]
\[
Dz=\epsilon br+B_1,\qquad Dw=-\epsilon ar+B_2,
\qquad p=aB_1+bB_2,\qquad \epsilon\in R^*,
\tag{3}
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0.
\tag{4}
\]
All coefficients in \(R\) are killed by \(D\). In addition
to reducedness of \(J\), assume explicitly
\[
B_1,B_2\in\mathfrak n^2.
\tag{5}
\]
Faithful-flat contraction in (4) gives \(Q\in\mathfrak n^2\).
The actual multi-tangent theorem supplies (5) when the reduced
plinth support has two distinct tangent directions. Pass 51
proves that an ordinary triple of the full \(p\), at a second-image
obstruction point, also forces \(JR=\mathfrak n\). Thus all these
hypotheses hold at such an obstruction point.

The previously established full quadratic divisor models and
actual regular-sequence divisions supply
\[
I_3=p^2R,\qquad F_3=F_2\oplus Rt,\qquad
D^3t=3\epsilon^2p^2,
\tag{6}
\]
and \(p^2\mathfrak n\subset I_4\subset p^2R\).
We reconstruct the relevant generators with coherent coefficient
choices below. No slice on the intrinsic derivation \(D\) is assumed.

## 2. A coherent choice of the cubic and quartic elements

Choose invariant coefficients in \(R\) with
\[
\begin{split}
B_1&=a^2c+ab d+b^2e,\\
B_2&=a^2f+ab g+b^2h,\\
Q&=a^2q_1+abq_2+b^2q_3.
\end{split}
\tag{7}
\]
Such expressions exist by (5). There is no assertion that these
nine coefficients vanish at the closed point.

Choose the cubic construction using
\[
B_1=a(ac+bd)+b(be),\quad
B_2=a(af+bg)+b(bh),\quad
Q=a(aq_1+bq_2)+b(bq_3).
\]
The actual regular-sequence construction gives
\[
\begin{split}
bt&=\epsilon rz-2(af+bg)z+2(ac+bd)w-(aq_1+bq_2),\\
-at&=\epsilon rw-2bhz+2bew-bq_3.
\end{split}
\tag{8}
\]
For this choice, (6) still holds: the invariant changes of
coefficient representation only select a particular cubic generator.

The two quartic constructions give actual elements \(T_a,T_b\)
with
\[
aT_a=\epsilon w^2-2hz+2ew-q_3,\qquad
bT_b=\epsilon z^2-2fz+2cw-q_1,
\tag{9}
\]
\[
D^4T_a=6\epsilon^3ap^2,\qquad
D^4T_b=6\epsilon^3bp^2,\qquad D^5T_a=D^5T_b=0.
\tag{10}
\]
Their membership in \(\mathcal A\) is the proved flatness
conclusion from pass 51, not an inference from the two fractions
in (9). The conic alone would not justify these divisions.

## 3. The exact syzygy and the exclusion of a unit fourth image

Expand \(r=az+bw\) in the second equation of (8), and use
the first equation of (9):
\[
-at=\epsilon azw+b(aT_a).
\]
Cancel the nonzero invariant \(a\) in the actual domain. The
first equation of (8), with the second equation of (9), similarly
permits cancellation of \(b\). The two resulting identities are
\[
bT_a=-t-\epsilon zw,\qquad
aT_b=t-\epsilon zw+2gz-2dw+q_2.
\tag{11}
\]
Subtracting them cancels the degree-four product \(zw\):
\[
\boxed{\quad
bT_a-aT_b=-2t-2gz+2dw-q_2.
\quad}
\tag{12}
\]
The right side belongs to \(F_3\), and its coefficient on \(t\)
in the actual direct sum (6) is the unit \(-2\).

Suppose \(I_4=p^2R\). Since \(I_4\) is the image of the
\(R\)-linear map \(D^4:F_4\to R\), there is an actual
\(Y\in F_4\) normalized by
\[
D^4Y=6\epsilon^3p^2.
\tag{13}
\]
Equation (10) then puts \(T_a-aY\) and \(T_b-bY\) in \(F_3\).
Consequently
\[
bT_a-aT_b
=b(T_a-aY)-a(T_b-bY)\in\mathfrak nF_3.
\tag{14}
\]
But the direct sum \(F_3=F_2\oplus Rt\) makes
\(\mathfrak nF_3=\mathfrak nF_2\oplus\mathfrak nRt\).
The unit \(t\)-coefficient in (12) contradicts (14).
Combining this with the pass-51 alternative proves
\[
\boxed{\quad I_4=p^2\mathfrak n.\quad}
\tag{15}
\]
In particular there is no actual quartic element whose fourth
derivative is a unit multiple of \(p^2\) at this point.

## 4. The complete fourth filtration module

For any \(x\in F_4\), (10) and (15) allow subtraction of an
\(R\)-linear combination of \(T_a,T_b\) so that the fourth
derivative is zero. Thus
\[
F_4=F_3+RT_a+RT_b.
\]
Equation (12) solves for \(t\) using the unit \(2\), and gives
\[
F_4=F_2+RT_a+RT_b.
\tag{16}
\]
This sum is direct. Suppose
\(u+\alpha T_a+\beta T_b=0\), where \(u\in F_2\) and
\(\alpha,\beta\in R\). Apply \(D^4\) and cancel the nonzero
factor \(6\epsilon^3p^2\):
\[
a\alpha+b\beta=0.
\]
Since \(a,b\) are coprime parameters, there is a \(k\in R\)
with \(\alpha=bk\), \(\beta=-ak\). Substitution of (12)
then gives \(-2kt+u'\!=0\) for some \(u'\in F_2\).
The direct sum (6) forces \(k=0\), and then \(u=0\).
Therefore
\[
\boxed{\quad
F_4=R\oplus Rz\oplus Rw\oplus RT_a\oplus RT_b.
\quad}
\tag{17}
\]
This is a direct module computation. No assertion about reflexive
modules, an image-ideal freeness theorem, or a slice on a closed
fiber is required.

## 5. Exact limits

The previous principal third image \(I_3=p^2R\) is followed
here by the nonprincipal fourth image \(p^2\mathfrak n\).
The existence of actual quartic corrections therefore does not
make the next image principal. The direct basis (17) identifies
the entire fourth filtration module, not the full intrinsic ring.

In particular the proof alone does not show
\(\mathcal A=R[F_4]\), decide the fiber of that subalgebra,
or exclude an actual obstruction point. Those questions require
an additional algebra-presentation or generation argument. The
rank-one first-jet case at a general reduced obstruction is
outside (5), and is not resolved here.

The independently reconstructed
[quartic algebra theorem](quartic-fiber-gate-pass52.md) supplies
that separate presentation under exactly the hypotheses above.
It proves \(R[F_4]\ne\mathcal A\), with a two-dimensional
closed fiber. Thus even the complete module (17) cannot generate
the actual ring; every generating set needs intrinsic degree at
least five. That additional conclusion uses the companion proof,
not the image-ideal argument alone.

The original cylinder and its actual quadratic-divisor and
flatness consequences have not been replaced by a weak conic
example. No new unresolved-frame realization, historical novelty,
or unrestricted cancellation conclusion is claimed. All files
from passes 51 and earlier remain unchanged.

## Finite verification boundary

The standalone [two-method checker](fourth_image_boundary_checks_pass52.py)
reconstructs the coherent cubic/quartic syzygy with its exact conic
error before quotienting, checks the third derivative carrying the
unit cubic coefficient, and computes a nonzero generic determinant
for the five proposed basis elements from an independent conic
inverse. Its first complete run passed two methods in 0.209 seconds,
exit zero, with no failed assertions. Only unittest and SymPy are
imported. These controls do not verify actual flatness, the universal
image-ideal conclusion, or existence of an unresolved-cylinder example.
