# The entire quintic algebra has zero closed-fiber velocity

In the actual reduced zero-first-jet sector,
\[
\boxed{D(F_5)\subseteq\mathfrak nF_4.}
\tag{1}
\]
Consequently the induced derivation on the whole, possibly
nonreduced, closed fiber kills the image of \(R[F_5]\).
The assertion concerns this image, not the entire actual fiber
ring. It neither proves generation by \(F_5\) nor excludes
the existence of the obstruction point.

This strengthens the single coherent coefficient check in the
[quintic construction](quintic-correction-pass53.md), without
changing that frozen proof or its two-method checker.

## 1. Actual hypotheses and the coefficient-order rule

Use the full actual hypotheses and coherent elements of the
quintic construction:
\[
R=C_{\mathfrak m},\quad \mathfrak n=(a,b),\quad
\mathcal A=A\otimes_C R,\quad
JR=\mathfrak n,\quad B_1,B_2\in\mathfrak n^2.
\]
Here \(R\) is a regular local surface ring and \(\mathcal A\)
is the actual faithfully flat domain. All coefficients below
are in \(R=\ker(D|_{\mathcal A})\).
Write
\[
\begin{aligned}
B_1&=a^2c+ab d+b^2e,\\
B_2&=a^2f+ab g+b^2h,\\
Q&=a^2q_1+abq_2+b^2q_3,
\end{aligned}
\qquad
r=az+bw,\quad p=aB_1+bB_2.
\]
The actual identities are
\[
Dr=p,\qquad Dz=\epsilon br+B_1,\qquad
Dw=-\epsilon ar+B_2,
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0,\qquad
\epsilon\in R^*.
\tag{2}
\]
In particular \(r\in\mathfrak nF_2\) and \(p\in\mathfrak n^3\).

The proved free modules are
\[
\begin{aligned}
F_2&=R\oplus Rz\oplus Rw,\\
F_3&=F_2\oplus Rt,\\
F_4&=F_2\oplus RU\oplus RV,\\
F_5&=F_4\oplus RY.
\end{aligned}
\tag{3}
\]
For \(x=a\) or \(b\),
\[
(\mathfrak n^2:x)=\mathfrak n.
\tag{4}
\]
Indeed the degree-one initial form of \(x\) is nonzero in
\(\operatorname{gr}_{\mathfrak n}R=
(R/\mathfrak n)[\bar a,\bar b]\).
Multiplication by it cannot put a nonzero constant initial
form into degree at least two. Equivalently a coefficient
not in \(\mathfrak n\) is a unit and its product with \(x\)
has order one.

Thus, for any of the actual free modules \(F_i\),
\[
xv\in\mathfrak n^2F_i,\quad v\in F_i
\quad\Longrightarrow\quad v\in\mathfrak nF_i.
\tag{5}
\]
This is coefficientwise in a proved module basis. It makes
no freeness or flatness assertion about the generated algebra.

## 2. The quadratic and cubic velocities have order two

Equation (2) immediately yields
\[
Dz,Dw\in\mathfrak n^2F_2.
\tag{6}
\]
To retain the exact order of \(Dt\), put
\[
c_0=ac+bd,\quad d_0=be,\quad
e_0=af+bg,\quad f_0=bh.
\]
All four belong to \(\mathfrak n\), and
\(B_1=ac_0+bd_0,\ B_2=ae_0+bf_0\).
The coherent cubic equation is
\[
bt=\epsilon rz-2e_0z+2c_0w-aq_1-bq_2.
\tag{7}
\]
Differentiating (7), and replacing \(\epsilon r^2\) using
the conic in (2), gives
\[
\begin{split}
Dt={}&\epsilon Q
 +\epsilon\bigl[a(e_0+2d_0)+3bf_0\bigr]z\\
&-\epsilon\bigl[3ac_0+b(d_0+2e_0)\bigr]w
 +2(c_0f_0-d_0e_0).
\end{split}
\tag{8}
\]
For example, before cancelling \(b\), the coefficient of
\(\epsilon z\) is
\[
p+2bB_2+a(-ac_0+bd_0-2be_0)
=b\bigl[a(e_0+2d_0)+3bf_0\bigr].
\]
Every coefficient in (8) belongs to \(\mathfrak n^2\).
Therefore
\[
\boxed{D(F_3)\subseteq\mathfrak n^2F_2.}
\tag{9}
\]
This explicit formula is stronger than merely bounding \(Dt\)
by its \(D\)-degree.

## 3. The quartic velocities have order one

The actual quartic equations are
\[
aU=\epsilon w^2-2hz+2ew-q_3,\qquad
bV=\epsilon z^2-2fz+2cw-q_1.
\tag{10}
\]
The coherent cubic equations also give
\[
rz,rw\in\mathfrak nF_3.
\tag{11}
\]
For example,
\[
\epsilon rw=-at+2bhz-2bew+bq_3.
\]
Differentiate the first equation in (10):
\[
aDU=-2\epsilon^2a(rw)+2\epsilon B_2w
     -2hDz+2eDw.
\tag{12}
\]
Its right side lies in \(\mathfrak n^2F_3\), by (6)
and (11). Since \(DU\in F_3\), rule (5) gives
\(DU\in\mathfrak nF_3\).
The other equation similarly yields
\[
bDV=2\epsilon^2b(rz)+2\epsilon B_1z
     -2fDz+2cDw\in\mathfrak n^2F_3.
\]
Consequently
\[
\boxed{D(F_4)\subseteq\mathfrak nF_3.}
\tag{13}
\]
These are divisions in free filtration modules of the actual
ring, not in the nonflat quartic subalgebra.

## 4. The new quintic also has zero residue

The explicit split in the quintic construction has
\[
rt=aR_a+bR_b,\qquad rt\in\mathfrak nF_4,
\]
\[
bY=zt-R_a,\qquad -aY=wt-R_b.
\tag{14}
\]
In that particular \(R_a\), the coefficients of \(1,z,w\)
belong to \(R\), while the coefficients of \(U,V\) belong
to \(\mathfrak n\). Thus (6) and (12)--(13) imply
\[
DR_a\in\mathfrak n^2F_3\subseteq\mathfrak n^2F_4.
\tag{15}
\]
There is an important degree distinction in differentiating
\(zt\). The product \(Dz\cdot t\) must not simply be treated
as a product of two \(F_2\) elements. Instead the proved
\(rt\) reduction gives
\[
D(zt)=\epsilon b(rt)+B_1t+zDt
       \in\mathfrak n^2F_4.
\tag{16}
\]
For the last term use (9) and \(F_2F_2\subseteq F_4\).
The first term uses \(rt\in\mathfrak nF_4\), and the middle
term uses \(B_1\in\mathfrak n^2,\ t\in F_4\).

Equations (14)--(16) prove
\[
bDY=D(zt-R_a)\in\mathfrak n^2F_4.
\]
But \(DY\in F_4\) is already known from \(Y\in F_5\).
The free-basis coefficient rule (5) therefore gives
\[
DY\in\mathfrak nF_4.
\tag{17}
\]
Combining (17) with (13) and the actual direct sum in (3)
proves (1). Replacing \(Y\) by another normalized choice
changes it by \(F_4\); equation (13) shows that the residue
statement is independent of that choice.

## 5. Whole-fiber scope and the remaining algebra gate

Since \(D\) kills \(R\), it induces a derivation
\(\bar D\) on
\(\bar{\mathcal A}=\mathcal A/\mathfrak n\mathcal A\).
Equation (1) and the Leibniz rule give
\[
\bar D\bigl(\operatorname{image}
  (R[F_5]\longrightarrow\bar{\mathcal A})\bigr)=0.
\tag{18}
\]
No passage to the reduced fiber is involved. In particular the
image of the entire quintic algebra cannot contain a
\(\bar D\)-slice on this nonzero fiber.

If \(\bar D\ne0\) on the actual whole fiber, (18) would
immediately prove \(R[F_5]\ne\mathcal A\). The present
argument does not establish that nonvanishing. Conversely,
if \(R[F_5]=\mathcal A\), it would force \(\bar D=0\).
This conditional statement is not a contradiction supplied
by primitivity alone.

The [separate saturation gate](quintic-saturation-gate-pass53.md)
identifies actual equality with regularity of \((a,b)\) on
the full generated algebra. The finite module freeness in
(3) does not settle that regularity. Nor does this note
identify the closed fiber of \(R[F_5]\) with the actual
closed fiber, or construct an actual obstruction point.

All new assertions are written coefficient-order arguments.
No additional numeric suite or computational verification
of the universal flatness and division hypotheses is claimed.
Files from pass 52 and earlier, and the frozen quintic
construction and checker, are unchanged.

