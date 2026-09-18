# Fiber invariant opens and the bounded-slice obstruction

At a simultaneous speed-and-acceleration zero, the actual sliced
action supplies two degree-two invariant principal opens covering
the entire scheme-theoretic fiber. They do not, by themselves,
produce a new bounded polynomial slice. A bounded slice on either
nonempty open already descends to the original local ring.

There are two additional exact boundaries. In the genuine
degree-two case, projection of the four original coordinates into
\(F_3\) is equivalent to projection into \(F_2\), for a single
chosen slice. Adjoining a square root of a degree-two invariant
does produce normalized slices on invariant étale opens, but
those slices can have infinite intrinsic derivative degree.
None of these statements proves generation by \(F_3\) using a
different generating set.

## 1. Actual frame and local notation

Use the full supplied independent degree-two frame of
[pass 49](frame-filtration-generation-pass49.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad
Es_*=1,\qquad A=\ker E,
\]
\[
C=\ker D\simeq\mathbb C^{[2]},\qquad
L=\operatorname{Frac}C,\qquad A_L=L[j],
\qquad B_L=L[x_3,x_4].
\tag{1}
\]
Here \(D\) is the actual primitive intrinsic LND. Its generic
restriction is a nonzero \(L\)-multiple of \(\partial_j\).
The supplied actual generic graph is
\[
Ex_3=f,\quad Ex_4=g,\quad E^2x_i=h_i\quad(i=1,2),
\]
\[
f,g,h_1,h_2\in C,\qquad
x_i=\mathcal Q_i(x_3,x_4),\quad
\mathcal Q_i\in L[X_3,X_4],\quad\deg\mathcal Q_i\le2.
\tag{2}
\]
The bad speeds \(f,g\) are algebraically independent. For the
degree threshold in Section 4 we explicitly require genuine flow
degree two, so at least one \(h_i\) is nonzero.

Fix a closed point
\[
\mathfrak m\supset(f,g,h_1,h_2),\qquad
R=C_{\mathfrak m},\qquad
A_0=A_R,\qquad B_0=B_R=A_0[s_*].
\tag{3}
\]
Write \(\overline A=A_0/\mathfrak mA_0\) and
\(\overline B=\overline A[s_*]\). No reducedness or smoothness
of this fiber is assumed. The actual \(A_0\) is a UFD, as follows
from the polynomial-cylinder hypothesis and invariant localization.
Let
\[
F_n(A_0)=\ker(D^{n+1}:A_0\longrightarrow A_0).
\]

## 2. The two actual \(F_2\) opens cover the whole fiber

Put \(P_i=Ex_i\) for \(i=1,2\), and define
\[
I_i=P_i^2-2h_ix_i,\qquad
I_{12}=P_1P_2-h_2x_1-h_1x_2.
\tag{4}
\]
Direct differentiation gives \(E I_i=E I_{12}=0\).
The generic graph makes each \(P_i\) affine-linear in the bad
coordinates. Therefore all three invariants in (4) have generic
\(j\)-degree at most two, and are actual elements of \(F_2(A_0)\).

The residues \(p_i=\overline{P_i}\) are \(E\)-invariant in
\(\overline B\), because \(h_i\in\mathfrak m\). The actual slice
identity, written in the original coordinates, gives
\[
1=\sum_{\nu=1}^4
       \frac{\partial s_*}{\partial x_\nu}E x_\nu.
\]
Modulo \(\mathfrak m\), the two bad terms vanish. Evaluation at
\(s_*=0\) in \(\overline B=\overline A[s_*]\) now gives
\[
(p_1,p_2)\overline A=\overline A.
\tag{5}
\]
This evaluation is legitimate for the entire nonreduced fiber.

Moreover,
\[
\overline I_1=p_1^2,\qquad
\overline I_{12}=p_1p_2,\qquad
\overline I_2=p_2^2,
\]
so
\[
(\overline I_1,\overline I_2)\overline A=\overline A.
\tag{6}
\]
For example, cube an identity \(\alpha p_1+\beta p_2=1\)
and group its four terms by \(p_1^2\) and \(p_2^2\).
Thus the two principal opens \(D(\overline I_i)\) cover the
whole actual fiber, not merely its reduced closed points.
An empty member of the cover is simply discarded.

These are opens in the intrinsic threefold. Their denominators
lie in \(F_2(A_0)\), not necessarily in \(R=\ker D\).
Although \(E\) remains locally nilpotent after these localizations,
\(D\) need not do so.

## 3. Polynomial finite-degree elements cannot acquire moving denominators

We use the following elementary denominator lemma.

**Lemma.** Let \(A_0\) be the UFD in (1)--(3), and let
\(0\ne I\in A_0\). Let \(c\) be the product of the distinct
\(D\)-invariant prime factors of \(I\), with the empty product
equal to one. Then
\[
A_0[I^{-1}]\cap L[j]=A_0[c^{-1}],
\tag{7}
\]
inside \(\operatorname{Frac}A\). Equivalently, the elements of
\(A_0[I^{-1}]\) killed by some power of \(D\) are exactly
\(A_0[c^{-1}]\). In each finite degree,
\[
\ker(D^{n+1}:A_0[I^{-1}]\longrightarrow A_0[I^{-1}])
       =F_n(A_0)[c^{-1}].
\tag{8}
\]
The left side uses the extended derivation; it does not assert
local nilpotence on the whole localization.

To prove (7), write a fraction in reduced UFD form. A prime
\(q\in A_0\) becomes a unit in \((A_0)_L=L[j]\) exactly when
it divides a nonzero element of \(R\). Such a factor is
\(D\)-invariant: if \(qa\in\ker D\), additivity of the LND
degree forces both \(Dq=0\) and \(Da=0\). Conversely a nonzero
invariant \(q\) belongs to \(R\) and is inverted over \(L\).
Every other prime remains prime and nonunit in \(L[j]\), so
cannot survive in the reduced denominator of a polynomial there.
This proves (7), with all multiplicities allowed.

On \(L(j)\), a rational function killed by a power of the
nonzero constant multiple of \(\partial_j\) is a polynomial
in \(j\). A finite pole would persist under repeated differentiation.
This proves the finite-degree formulation, and invariant
localization gives (8).

If \(D(\overline I)\) meets the actual closed fiber, no invariant
prime factor of \(I\) can be a nonunit of \(R\). Indeed, such a
factor belongs to \(\mathfrak mR\), which would give
\(\overline I=0\). Consequently (7)--(8) reduce to
\[
A_0[I^{-1}]\cap L[j]=A_0,\qquad
\ker D^{n+1}\text{ on }A_0[I^{-1}]=F_n(A_0).
\tag{9}
\]

Here and below \(D(\overline I)\) denotes a principal open,
not application of the derivation to \(\overline I\).

**Bounded-slice descent.** Suppose this fiber open is nonempty,
and let \(\sigma\in B_0[I^{-1}]\) be an actual \(E\)-slice.
If its four original-coordinate projections
\(\rho_\sigma(x_\nu)\) are killed by powers of the extended
intrinsic \(D\), then \(\sigma\) belongs to \(B_0\).

Indeed,
\[
\sigma=s_*+b,\qquad b\in A_0[I^{-1}].
\]
The two projections of \(x_3\), along \(s_*\) and \(\sigma\),
differ by
\[
\rho_{s_*}(x_3)-\rho_\sigma(x_3)=fb.
\tag{10}
\]
The first term belongs to \(A_0\), hence has finite \(D\)-degree;
the second has finite degree by assumption. Since \(Df=0\)
and \(f\ne0\), the same holds for \(b\). Equation (9) gives
\(b\in A_0\), proving descent. Its projected elements and their
degree bounds descend unchanged.

Thus no nonempty \(F_2\) fiber open in (6) supplies a new
bounded polynomial gauge that was unavailable over the original
local ring.

## 4. A single \(F_3\)-bounded projected list is already \(F_2\)-bounded

Choose any affine generic slice \(\sigma_0\) over \(L\),
for example \(x_3/f\), and keep \(j=gx_3-fx_4\).
Every actual slice of \(B_0\) has the unique generic form
\[
\sigma=\sigma_0+H(j),\qquad H\in L[j].
\tag{11}
\]
The generic graph gives
\[
x_i=\frac{h_i}{2}\sigma_0^2+
       A_i(j)\sigma_0+B_i(j),\qquad
\deg A_i\le1,\quad\deg B_i\le2.
\]
Projection along (11) is therefore
\[
\rho_\sigma(x_i)=
       \frac{h_i}{2}H^2-A_iH+B_i.
\tag{12}
\]
If \(N=\deg H\ge2\) and \(h_i\ne0\), its degree is exactly
\(2N\). The other terms have degrees at most \(N+1\) and two,
strictly smaller than \(2N\). Both bad projected coordinates
have degree at most \(N\), and a nonzero bad speed gives exact
degree \(N\).

It follows that
\[
\boxed{
\begin{array}{c}
\rho_\sigma(x_\nu)\in F_3(A_0)\text{ for all }\nu\\
\Longleftrightarrow\ \sigma\text{ is affine-linear over }L
                        \text{ in }x_3,x_4\\
\Longleftrightarrow\
\rho_\sigma(x_\nu)\in F_2(A_0)\text{ for all }\nu .
\end{array}}
\tag{13}
\]
The convention for constant or zero \(H\) causes no exception.
The same statement holds for slices on the nonempty fiber opens
in (6), because Section 3 first descends them.

An actual affine generic slice makes the projected original
generators generate \(A_0\), so it implies \(A_0=R[F_2(A_0)]\).
At an actual second-image basepoint \(J\subset\mathfrak m\),
the conic presentation and topology coefficient vanishing from
[pass 47](flat-conic-topology-gate-pass47.md) would then give
the two-dimensional fiber \(\mathbb C[Z,W]\), contradicting
the actual one-dimensional quotient fiber. Consequently, at any
such basepoint, no slice with the property in (13) exists,
even on the nonempty fiber opens (6).

This is a conditional obstruction, not an assertion that such
basepoints occur in an unresolved actual frame. It also does not
exclude generation of \(A_0\) by \(F_3(A_0)\) using a different
set of elements unrelated to a single projected original list.

## 5. What the square-root construction actually gives

For one good coordinate write \(X=x_i\), \(P=EX\), \(H=E^2X\),
and \(I=P^2-2HX\). After inverting \(I\), adjoining
\(\kappa^2=I\) is finite étale. Extend \(E\) by \(E\kappa=0\).
Using the already supplied slice,
\[
P=Hs_*+a,\qquad
X=\frac H2s_*^2+a s_*+b,\qquad
a,b\in A_0,\qquad I=a^2-2Hb.
\tag{14}
\]
On the invariant open \(a+\kappa\ne0\) of this extension,
\[
\sigma=s_*+\frac{2b}{a+\kappa},\qquad
E\sigma=1,\qquad H\sigma=P-\kappa.
\tag{15}
\]
There is no division-by-\(H\) assertion in the definition of
\(\sigma\). The opposite sign gives a slice on \(a-\kappa\ne0\).
These two invariant opens cover the étale extension because
\(\kappa\) is a unit. Thus these are actual slices of the
localized extended algebras.

In contrast, directly inverting \(P+\kappa\) is not an
\(E\)-invariant localization when \(H\ne0\), since
\(E(P+\kappa)=H\). The formula \(2X/(P+\kappa)\) alone does
not justify the polynomial slice theorem there.

More importantly, the intrinsic derivation must now be extended
by
\[
D\kappa=\frac{DI}{2\kappa}.
\tag{16}
\]
It need not be locally nilpotent, or even finite on \(\kappa\).
Section 3 does not apply to this algebraic extension of \(L[j]\).
Equations (14)--(15) therefore supply no uniform intrinsic
degree bound and no descent to the original coefficient field.

A genuine lower-profile polynomial-cylinder control isolates
this failure. In \(\mathbb C[u,v,a,s]\), take
\[
E=\partial_s,\qquad D=\partial_a,\qquad
X=a+s+\frac u2s^2,\qquad
(x_1,x_2,x_3,x_4)=(X,s,u,v).
\tag{17}
\]
The inverse is polynomial:
\(a=x_1-x_2-x_3x_2^2/2\), \(s=x_2\), \(u=x_3\), \(v=x_4\).
The actual partials have adjoint heights \((0,1,2,0)\).
Here
\[
P=1+us,\quad H=u,\quad I=1-2ua,\quad
\sigma=s+\frac{2a}{1+\kappa},\quad \kappa^2=1-2ua.
\tag{18}
\]
On \(1+\kappa\ne0\), this is the actual slice (15). In the
generic field it is \(s+(1-\kappa)/u\). For every \(n\ge1\),
\[
D^n\kappa=(-2u)^n
   \left(\frac12\right)
   \left(\frac12-1\right)\cdots
   \left(\frac12-n+1\right)\kappa^{1-2n}\ne0.
\tag{19}
\]
Thus this normalized slice and its projected original coordinate
\(x_2=s\) have infinite intrinsic derivative degree.
The control is not the unresolved independent \((1,1,2,2)\)
profile; it already has the original coordinate slice \(s\).
It tests exactly the unsupported implication from an étale
normalized slice to a bounded intrinsic one.

## 6. Exact remaining obligation

The fiber cover (6) is genuine, and its polynomial
finite-degree descent is exact. To obtain a bounded polynomial
repair one must still produce an actual slice before or after
descent satisfying the affine condition in (13). Constructing
étale slices as in (15) does not meet that condition.

Alternatively, one can try to generate the whole local ring by
\(F_3\) through a different intrinsic generating set. The present
argument neither proves nor disproves that assertion. The
[cubic image result](third-image-cubic-gate-pass48.md) may only be
applied to the whole actual fiber after such a generation theorem
is proved. No frozen proof, checker, or metadata is altered here.

The standalone
[fiber_invariant_opens_checks_pass50.py](fiber_invariant_opens_checks_pass50.py)
contains one exact lower-profile control. Its first complete run passed
in 0.297 seconds, exit zero. It checks both polynomial inverse orders,
the actual partial identities and adjoint heights, the normalized
étale slice, and the nonzero derivative recurrence through order seven.
The all-degree recurrence is proved in (19); finite checks do not prove
the general denominator lemma, the covering assertion, or a theorem
about the unresolved full frame. Only unittest and SymPy are imported.
