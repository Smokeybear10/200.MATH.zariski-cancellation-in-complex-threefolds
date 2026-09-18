# The leading-image class obstructing slice descent

A minimal high-degree slice gauge produces a nonzero class in a
specific fractional ideal quotient. The ideal in the denominator is
the intrinsic image ideal, and the annihilating ideal is generated
by the two original bad speeds. These two ideals must not be
identified with the maximal ideal without an additional hypothesis.

In the extra sector where the original speeds form parameters at a
reduced zero-first-jet obstruction, the already established cubic,
quartic and quintic modules also exclude minimal gauge degrees
three, four and five. This uses their existing exact relations,
not a computation of the sixth filtration layer.

## 1. Actual setting and leading-coefficient ideals

Retain the actual degree-two generic graph and slice-gauge setup of
[pass54](profile-generation-gap-pass54.md). Let
\[
R=C_{\mathfrak m},\quad L=\operatorname{Frac}R,\quad
\mathcal A=A_R,\quad\mathcal B=B_R=\mathcal A[s_*],
\]
\[
\mathcal B_L=L[x_3,x_4],\quad
\mathcal A_L=L[j],\quad j=gx_3-fx_4,
\quad Ex_3=f,\quad Ex_4=g.
\tag{1}
\]
Here \(f,g\in R\) are the original nonzero bad speeds, and
\(D\) is the intrinsic primitive LND with kernel \(R\).
Put
\[
\mu=Dj\in R\setminus\{0\},\qquad
F_n=\ker D^{n+1}\subset\mathcal A,\qquad
I_n=D^n(F_n)\subset R.
\tag{2}
\]
Over \(L[j]\), \(D=\mu\partial_j\). For \(n\ge1\) define the
fractional leading-coefficient ideal
\[
M_n=\frac{I_n}{n!\mu^n}\subset L.
\tag{3}
\]
Thus \(\lambda\in M_n\) exactly when some element of \(F_n\)
has coefficient \(\lambda\) at \(j^n\). This includes
\(\lambda=0\); no choice of generators of \(F_n\) is required.
The image ideal \(I_n\) is a nonzero finitely generated ideal of
the Noetherian ring \(R\).

Choose an affine generic \(E\)-slice \(\sigma_0\).
Every actual slice has the form
\[
s=\sigma_0+H(j),\qquad H\in H_*+\mathcal A.
\tag{4}
\]
Choose a slice for which \(n=\deg_jH\) is minimal among all actual
slices, and suppose \(n\ge2\). This minimum exists whenever all
gauges have positive degree, since their degrees are integers.
Write \(\lambda\ne0\) for the leading coefficient of \(H\), and put
\[
\mathfrak h=(f,g)R.
\]
For a fractional ideal \(M\subset L\), use the notation
\[
(M:\mathfrak h)=\{\xi\in L:\mathfrak h\xi\subset M\}.
\]

## 2. The exact necessary colon class

The two actual bad-coordinate projections
\[
X_0=x_3-fs,\qquad Y_0=x_4-gs
\tag{5}
\]
belong to \(\mathcal A\). In \((j,\sigma_0)\), each bad coordinate
is affine-linear. Since \(n\ge2\), their degree-\(n\) coefficients
are exactly \(-f\lambda,-g\lambda\). Consequently
\[
f\lambda,g\lambda\in M_n.
\]
If \(\lambda\in M_n\), choose \(u\in F_n\) with that leading
coefficient. The actual slice \(s-u\) has a gauge of degree
strictly smaller than \(n\), a contradiction. Hence
\[
\boxed{\quad
0\ne[\lambda]\in (M_n:\mathfrak h)/M_n.
\quad}
\tag{6}
\]
This is a necessary condition on a minimal slice. It is not a
converse construction of a slice from a class in the quotient.

For a principal fractional ideal \(M_n=cR\), let
\(d=\gcd(f,g)\) in the local UFD \(R\). Valuation comparison gives
\[
(cR:(f,g))=\frac{c}{d}R.
\tag{7}
\]
Indeed, \(\xi/c\) can have a denominator at a prime only to the
minimum of the two valuations of \(f,g\). In particular,
\[
\gcd(f,g)=1,\quad M_n\text{ principal}
\quad\Longrightarrow\quad
n\text{ cannot be a minimal gauge degree }\ge2.
\tag{8}
\]
This implication remains valid if the speeds generate a proper
height-two ideal; a Bezout identity is not needed.

If the original speeds generate \(\mathfrak mR\), multiply (6)
by \(n!\mu^n\), and set
\[
\kappa=n!\mu^n\lambda.
\]
Then \(f\kappa,g\kappa\in I_n\subset R\). Since the two parameters
have no common prime factor, \(\kappa\in R\). Thus (6) becomes
the actual nonzero socle class
\[
\boxed{\quad
0\ne[\kappa]\in (I_n:\mathfrak mR)/I_n
       =\operatorname{Soc}(R/I_n).
\quad}
\tag{9}
\]
For a general bad-speed ideal, (6), not the socle formula (9),
is the applicable statement.

## 3. Coprime speeds are not an inherited universal premise

The [acceleration extension in pass45](acceleration-divisor-extension-pass45.md)
explicitly retains
\[
d=\gcd(f,g),\qquad f_0=f/d,\qquad g_0=g/d,
\qquad j_0=g_0x_3-f_0x_4\in A.
\]
It does not prove \(d=1\). Normalizing the invariant coordinate
from \(j\) to \(j_0\) rescales the ideals in (3), but does not
divide the actual action \(E\) or replace its bad speeds by
\(f_0,g_0\). Therefore it does not remove the ideal
\(\mathfrak h=(f,g)\) from (6).

In particular, the principal image ideals proved in the earlier
filtration work cannot automatically be used with (8) at every
actual point. When a common speed divisor remains, even a
principal \(M_n\) has the larger colon in (7).
This is a precise denominator obstruction, not a proof that
any such class is realized by an actual slice.

The use of intrinsic image ideals is the same established
image-ideal route discussed in
[the pass47 source audit](image-ideal-source-scope-pass47.md).
No general principality or freeness theorem is added here.

## 4. Extra parameter-speed sector: the quartic syzygy excludes degree four

For the remainder impose both the actual reduced zero-first-jet
conditions and the additional bad-speed condition
\[
JR=\mathfrak mR,\qquad B_1,B_2\in(\mathfrak mR)^2,
\qquad \boxed{(f,g)R=\mathfrak mR.}
\tag{10}
\]
The boxed condition is not supplied by the original generic
rank-two speed assumption.

It is legitimate here to choose the conic parameters
\[
a=f,\qquad b=g.
\tag{11}
\]
To check this against the actual module rather than rename
unrelated symbols, start with a basis
\(F_2=R\oplus Rz_0\oplus Rw_0\), and
\(r=a_0z_0+b_0w_0\), where \((a_0,b_0)=JR\).
Both \((a_0,b_0)\) and \((f,g)\) are minimal generating pairs
of the same maximal ideal. A coefficient matrix expressing
the second pair in terms of the first has invertible reduction
modulo \(\mathfrak mR\), hence is an element of
\(\operatorname{GL}_2(R)\).
If
\[
\binom a b=M\binom{a_0}{b_0},
\qquad
\binom z w=M^{-{\mathsf t}}\binom{z_0}{w_0},
\tag{12}
\]
then \(r=az+bw\) and this is still a basis of the actual \(F_2\).
The alternating coefficient in
\(Dz=\epsilon br+B_1,\ Dw=-\epsilon ar+B_2\)
is multiplied by the unit \(1/\det M\).
The \(B\)-column is multiplied by \(M^{-{\mathsf t}}\),
so its zero-first-jet condition is preserved.
These are invariant coefficient changes; \(D\) differentiates
none of the matrix entries.

Apply the already proved cubic, quartic and quintic formulas
in this actual parameter basis:
\[
I_3=p^2R,\qquad I_4=p^2(a,b)R,\qquad I_5=p^3R,
\tag{13}
\]
\[
F_3=F_2\oplus Rt,\qquad
F_4=F_2\oplus RU\oplus RV,
\tag{14}
\]
\[
D^4U=6\epsilon^3ap^2,\qquad
D^4V=6\epsilon^3bp^2,\qquad
bU-aV=-2t+\eta,\quad \eta\in F_2.
\tag{15}
\]
Here \(Dr=p\) is the full primitive plinth generator, and
\(\epsilon\in R^*\). The sources are the
[cubic construction in pass48](third-image-cubic-gate-pass48.md),
[quartic boundary in pass52](fourth-image-boundary-pass52.md),
and [quintic construction in pass53](quintic-correction-pass53.md).
Equations (13)--(15) concern those entire actual filtration modules.

Suppose a minimal gauge has degree four. Its normalized leading
value from (9) satisfies
\[
\kappa\in(p^2(a,b):(a,b))\setminus p^2(a,b)
       =p^2R\setminus p^2(a,b).
\tag{16}
\]
For the equality, first use the coprime parameters to cancel
the principal factor \(p^2\); then
\(((a,b):(a,b))=R\).
Consequently
\[
c=-\frac{\kappa}{6\epsilon^3p^2}\in R^*.
\]
The two actual projections in (5) satisfy
\[
X_0=cU+\alpha,\qquad Y_0=cV+\beta,
\qquad \alpha,\beta\in F_3,
\tag{17}
\]
by their fourth derivatives. But their determinant is the
actual degree-one invariant
\[
j=bX_0-aY_0\in F_1.
\]
Using (15)--(17) gives
\[
j=-2ct+c\eta+b\alpha-a\beta.
\tag{18}
\]
The coefficient of \(t\) in the last two terms belongs to
\((a,b)\), whereas \(-2c\) is a unit. This contradicts
the direct sum \(F_3=F_2\oplus Rt\) and \(j\in F_1\subset F_2\).
Thus degree four is impossible as well.

## 5. What the conditional conclusion does and does not say

In the sector (10), the actual quartic algebra obstruction
\(R[F_4]\ne\mathcal A\) already excludes every gauge of degree
at most two. Principal \(I_3,I_5\) and (8) exclude minimal
degrees three and five. Section 4 excludes degree four.
Therefore
\[
\boxed{\quad
\min_{Es=1}\deg_j(s-\sigma_0)\ge6
\quad\text{under the extra hypotheses (10).}
\quad}
\tag{19}
\]
The exact generic quadratic-graph degree comparison then gives
maximum intrinsic degree at least twelve in every projected
original four-generator list.

Neither conclusion proves that an obstruction point satisfying
(10) exists. Nor does either exclude higher-degree gauges,
prove any upper bound, describe \(F_6\), or identify the minimum
degree of an arbitrary intrinsic generating set with that of
a single projected list.

The general result is (6). It isolates the leading-image class
whose lifting would lower a slice. The additional syzygy shows
that even a nonzero colon class need not satisfy the lower
compatibilities imposed by the two actual bad projections.
Quadratic generation has not been used to assume that an
invariant leading coefficient automatically lifts.

The [separate weak quadratic control](quadratic-slice-selection-boundary-pass55.md)
has minimum gauge three and an empty closed fiber. It is not
an instance of (10) or of the actual image ideals in (13).
The present argument neither repairs its missing fiber nor
uses it as an actual-cylinder counterexample.

No new finite suite is required for this deduction: the written
argument uses the previously verified filtration identities.
No frozen file, registry or regression count is changed.
