# An actual quintic correction and the fifth image

In the reduced zero-first-jet sector, the fifth image is
\[
I_5=p^3R,
\qquad
F_5=F_4\oplus RY
\]
for an explicitly constructed actual quintic element \(Y\).
The construction does not extrapolate the earlier image pattern.
It uses the full polynomial reduction of \(rt\) in the known
\(F_4\) basis, followed by regular-sequence division in the
actual flat algebra.

The calculation also settles the tempting obstruction inherited
from degree four: multiplying its unit cubic relation by \(r\)
removes the unit coefficient modulo \(\mathfrak mF_4\). It cannot
be reused to force a nonprincipal fifth image.

## 1. Exact hypotheses and established generators

Keep the actual reduced zero-first-jet setup of
[the fourth-image theorem](fourth-image-boundary-pass52.md):
\[
R=C_{\mathfrak m},\qquad \mathfrak n=\mathfrak mR=(a,b),
\qquad \mathcal A=A\otimes_C R,\qquad L=\operatorname{Frac}R,
\]
\[
JR=\mathfrak n,\qquad B_1,B_2\in\mathfrak n^2.
\tag{1}
\]
The actual \(\mathcal A\) is a faithfully flat domain over the
regular local surface ring \(R\), and \(D\) is its primitive
intrinsic LND. Set \(F_i=\ker D^{i+1}\) and \(I_i=D^i(F_i)\).

The known coefficients and identities are
\[
B_1=a^2c+ab d+b^2e,\quad
B_2=a^2f+ab g+b^2h,\quad
Q=a^2q_1+abq_2+b^2q_3,
\]
\[
r=az+bw,\quad Dr=p=aB_1+bB_2,\quad\epsilon\in R^*,
\]
\[
Dz=\epsilon br+B_1,\qquad Dw=-\epsilon ar+B_2,
\qquad
\epsilon r^2-2B_2z+2B_1w-Q=0.
\tag{2}
\]
All displayed coefficients in \(R\) are killed by \(D\).

Use the coherent cubic \(t\) and actual quartics \(U,V\) from
pass 52. Their full module and derivative identities are
\[
F_2=R\oplus Rz\oplus Rw,\qquad
F_3=F_2\oplus Rt,\qquad D^3t=3\epsilon^2p^2,
\]
\[
F_4=F_2\oplus RU\oplus RV,\qquad
D^4U=6\epsilon^3ap^2,\quad
D^4V=6\epsilon^3bp^2,
\tag{3}
\]
\[
aU=\epsilon w^2-2hz+2ew-q_3,\qquad
bV=\epsilon z^2-2fz+2cw-q_1,
\]
\[
t=-\frac{bU-aV}{2}-gz+dw-\frac{q_2}{2}.
\tag{4}
\]
Membership of \(U,V,t\) in the actual ring is already proved.
The conic by itself would not permit the divisions in (4).

## 2. The first image bound does not decide the answer

The products \(rU,rV,zt,wt\) are actual elements of \(F_5\).
The product rule gives
\[
D^5(rU)=30\epsilon^3ap^3,\qquad
D^5(rV)=30\epsilon^3bp^3,
\]
\[
D^5(zt)=30\epsilon^3bp^3,\qquad
D^5(wt)=-30\epsilon^3ap^3.
\tag{5}
\]
For example, only the term
\(\binom52D^2z\,D^3t\) survives in \(D^5(zt)\).

The full quadratic divisor models give
\[
I_5R_{(\pi)}=p^3R_{(\pi)}
\]
at each height-one base prime. In normalized local coordinates
\(D\rho=p\), \(D\upsilon=2\rho\),
\(p\upsilon=\rho^2-\eta\), the basis through degree five is
\[
1,\rho,\upsilon,\rho\upsilon,\upsilon^2,\rho\upsilon^2,
\qquad
D^5(\rho\upsilon^2)=120p^3.
\]
At primes where \(p\) is a unit, the polynomial-line basis gives
the same ideal. UFD contraction and (5) therefore give
\[
p^3\mathfrak n\subset I_5\subset p^3R.
\tag{6}
\]
There are initially two possibilities, not an automatic odd-image
rule. The next computation distinguishes them.

## 3. The complete \(rt\) reduction in the actual \(F_4\) basis

Define the following polynomials in the invariant coefficients:
\[
\begin{split}
N_0={}&a(2cq_3-fq_2)
 +b\bigl(2dq_3-(e+g)q_2+2hq_1\bigr),\\
N_z={}&a(4ch-2fg)
 +b\bigl(4dh-2eg+4fh-2g^2+\epsilon q_3\bigr),\\
N_w={}&-a(4ce-2df+\epsilon q_1)
 -b\bigl(4ch+2de-2dg+\epsilon q_2\bigr),\\
N_U={}&2a^2c+2ab d+ab f+b^2(e+g),\\
N_V={}&a^2f+ab(e+g)+2b^2h.
\end{split}
\tag{7}
\]
Then the exact actual-ring identity is
\[
\boxed{
\epsilon rt=N_0+N_zz+N_ww+N_UU+N_VV.
}
\tag{8}
\]
In particular all coefficients on the right lie in
\(\mathfrak n\), and the last two lie in \(\mathfrak n^2\).
Since \(\epsilon\) is a unit and (3) is an actual free basis,
\[
\boxed{rt\in\mathfrak nF_4.}
\tag{9}
\]

Here is a direct all-coefficient certificate for (8).
In the rational polynomial ring before imposing the conic, put
\[
\mathcal F=\epsilon r^2-2B_2z+2B_1w-Q,
\]
define \(U,V\) by their two fractions in (4), and define \(t\)
by the last formula of (4). Direct expansion gives
\[
rt-\frac{N_0+N_zz+N_ww+N_UU+N_VV}{\epsilon}
=
\mathcal F\,
 \frac{a\epsilon z-2af-2be-b\epsilon w-2bg}
      {2ab\epsilon}.
\tag{10}
\]
Multiplying by \(2ab\epsilon\), then evaluating in the actual
domain where \(\mathcal F=0\), proves (8) by cancellation.
There is no generic-to-global coefficient assumption: the five
numerators in (7) are polynomial and \(\epsilon^{-1}\in R\).

For an explicit split of (9), take
\[
\begin{split}
R_a=\epsilon^{-1}\bigl[&
 2cq_3-fq_2+(4ch-2fg)z
 -(4ce-2df+\epsilon q_1)w\\
 &+(2ac+2bd+bf)U+(af+b(e+g))V\bigr],\\
R_b=\epsilon^{-1}\bigl[&
 2dq_3-(e+g)q_2+2hq_1\\
 &+(4dh-2eg+4fh-2g^2+\epsilon q_3)z\\
 &-(4ch+2de-2dg+\epsilon q_2)w
 +b(e+g)U+2bhV\bigr].
\end{split}
\tag{11}
\]
Both belong to \(F_4\), and (8) reads
\[
rt=aR_a+bR_b.
\tag{12}
\]

The coefficient reduction was first obtained by comparing the
five coefficients in the generic polynomial coordinate \(r\).
An independent reconstruction expanded (10) directly in the
ambient rational polynomial ring. Equation (10) is the written
certificate that replaces reliance on either computation.

## 4. Faithful flatness supplies the actual quintic element

Equation (12) yields an actual relation
\[
a(zt-R_a)+b(wt-R_b)=0.
\tag{13}
\]
The base parameters \(a,b\) remain a regular sequence in
\(\mathcal A\). Reducing (13) modulo \(a\) first gives
\(wt-R_b\in a\mathcal A\); cancellation in the domain then
supplies one element \(Y\in\mathcal A\) with
\[
\boxed{
zt-R_a=bY,\qquad wt-R_b=-aY.
}
\tag{14}
\]
This is division in the actual ring, not in a conic or quartic
subalgebra presumed flat.

Because \(R_a,R_b\in F_4\), equation (5) gives
\[
bD^5Y=30\epsilon^3bp^3,\qquad bD^6Y=0.
\]
Cancelling \(b\ne0\) proves
\[
\boxed{Y\in F_5,\qquad D^5Y=30\epsilon^3p^3\ne0.}
\tag{15}
\]
Combining (15) with the full divisor upper bound (6) gives
\[
\boxed{I_5=p^3R,\qquad F_5=F_4\oplus RY.}
\tag{16}
\]
For the direct sum, subtract a suitable invariant multiple of
\(Y\) from any element of \(F_5\) to make its fifth derivative
zero. Directness follows from the nonzero derivative in (15).

A different split \(rt=aR_a'+bR_b'\) with \(R_a',R_b'\in F_4\)
changes \(Y\) only by \(F_4\). Indeed \(F_4\) is free over \(R\);
the kernel of its parameter row \((a,b)\) is the syzygy
\((b,-a)F_4\). Thus
\(R_a'-R_a=bH,\ R_b'-R_b=-aH\) for some \(H\in F_4\), and
the resulting quintic is \(Y-H\).

## 5. The degree-four obstruction does not propagate

The previous unit relation was
\[
bU-aV=-2t-2gz+2dw-q_2.
\]
After multiplication by \(r\), its right side lies in
\(\mathfrak nF_4\). In addition to (9), the coherent cubic
equations give
\[
rz=\epsilon^{-1}
 \bigl(bt+2(af+bg)z-2(ac+bd)w+aq_1+bq_2\bigr)
 \in\mathfrak nF_3,
\]
\[
rw=\epsilon^{-1}
 \bigl(-at+2bhz-2bew+bq_3\bigr)
 \in\mathfrak nF_3.
\]
Also \(r\in\mathfrak nF_2\). Therefore
\[
\boxed{
b(rU)-a(rV)
=r(-2t-2gz+2dw-q_2)\in\mathfrak nF_4.
}
\tag{17}
\]
The unit coefficient used to exclude a principal \(I_4\) has
genuinely disappeared at the next stage. Equations (8)--(17),
rather than an observed pattern, explain why \(I_5\) is principal.

## 6. Exact limits

This result requires the reduced zero-first-jet hypotheses in
(1). It does not cover a general reduced rank-one-jet obstruction
or every nonreduced obstruction ideal.

The actual \(F_5\) module is now explicitly free of rank six,
but its algebra has not been identified with \(\mathcal A\).
In particular no equality \(R[F_5]=\mathcal A\), no formula for
the closed fiber of \(R[F_5]\), and no assertion that \(Y\)
lies outside the algebra \(R[F_4]\) is made here. The known
quartic surface-fiber obstruction cannot simply be extrapolated
to the quintic algebra.

No assertion is made about all later odd images. The original
polynomial-cylinder and full divisor hypotheses remain in force;
no actual unresolved-frame obstruction point is constructed.
Every file from pass 52 and earlier remains frozen.

## 7. Bounded verification

The standalone [two-method checker](quintic_correction_checks_pass53.py)
passed its first complete run in 1.007 seconds, with process exit zero.
It independently expands the full conic-residual certificate, the
parameter-ideal orders and the explicit split, then checks the fifth
derivatives and normalized local quadratic basis with exact arithmetic.
It imports only unittest and SymPy and does not import another solver.

These finite algebra checks do not verify faithful flatness,
regular-sequence division in the actual algebra, the full divisor
classification, or existence of an actual obstruction point. Those
steps remain the quantified written proof above and its inherited
actual-cylinder hypotheses.

## 8. A bounded closed-fiber velocity check

For the coherent specialization
\[
\epsilon=1,\qquad B_1=a^2,\quad B_2=b^2,\quad Q=0
\]
the preceding formulas become
\[
U=\frac{w^2-2z}{a},\qquad
V=\frac{z^2+2w}{b},\qquad
t=-\frac{bU-aV}{2},
\]
\[
R_a=4z+2aU,\qquad R_b=-4w+2bV,\qquad
Y=\frac{zt-R_a}{b}.
\]
Here the fractions denote the same actual elements supplied by
flatness if this coefficient specialization occurs in the actual
setup. The displayed coefficient data alone do not construct such
an occurrence or a polynomial-cylinder frame.

In this specialization the exact answer is
\[
\boxed{DY=14az-14bw+5a^2U+5b^2V\in\mathfrak nF_4.}
\tag{18}
\]
Indeed, before imposing the conic
\(\mathcal F=r^2-2b^2z+2a^2w\), direct differentiation with
\(Dz=br+a^2,\ Dw=-ar+b^2\) gives
\[
DY-(14az-14bw+5a^2U+5b^2V)
=\mathcal F\,\frac{a^2+3abz-b^2w}{2ab^2}.
\tag{19}
\]
Multiplication and cancellation in the actual domain proves (18).

Consequently the residue of \(DY\) is zero on the whole closed
fiber, with any nilpotents retained. No reducedness or assumed
values of the residues of \(z,w,U,V\) are needed. In particular
this requested coefficient check does not produce a nonzero
constant velocity, a closed-fiber slice, or a pointwise-plinth
contradiction.

Equation (19) was independently expanded by two agents as a
bounded diagnostic after the two-method suite was frozen. It
does not add a test method or purport to verify an actual
coefficient-model realization.
