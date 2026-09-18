# Invariant extensions of triangular derivations admit affine slices

For the full family
\[
D=x^m\partial_y+P(x,y)\partial_z
\quad\text{on }R=\mathbb C[x,y,z],\qquad m\ge1,
\tag{1}
\]
with arbitrary \(P\in\mathbb C[x,y]\), there is no example of an
invariant-coefficient extension which has a slice but has no slice
affine in the extension variable. Precisely, if
\[
C=\ker D,\qquad A,B\in C,\qquad
E=AD+B\partial_t\quad\text{on }R[t],
\tag{2}
\]
then
\[
E\text{ has a slice}
\quad\Longleftrightarrow\quad
E\text{ has a slice affine in }t
\quad\Longleftrightarrow\quad
A P_D+BC=C,
\tag{3}
\]
where \(P_D=D(R)\cap C\) is the plinth ideal. This is an
all-degree structural statement, not a conclusion from a coefficient
scan. It asserts existence of an affine replacement, not that every
given slice is affine.

Section 7 extends the result from \(x^m\) to every nonzero
\(p(x)\in\mathbb C[x]\), with an explicit description of the
reduced plinth support. Thus the no-go result holds for the full
triangular family \(p(x)\partial_y+P(x,y)\partial_z\).

The proof below gives explicit criteria for all boundary cases of
\(P(0,y)\), including common factors of the two coefficients of
\(D\). Its key step is a discrete-valuation-ring test on a component
of \(B=0\). It does not prove (3) for arbitrary rank-three base
derivations, or supply a general affine-slice-to-coordinate theorem.

## 1. The primitive nonlinear-residue case

First assume
\[
\deg_yP(0,y)\ge1.
\tag{4}
\]
Choose \(Q\in\mathbb C[x,y]\) with \(Q_y=P\) and
\(Q(x,0)=0\), and put
\[
F=x^m z-Q(x,y),\qquad d=\deg_yQ(0,y)\ge2.
\tag{5}
\]
Then
\[
C=\mathbb C[x,F],\qquad
R\simeq C[y,z]/(x^m z-Q(x,y)-F).
\tag{6}
\]
Here is an elementary verification of the kernel assertion. After
inverting \(x\), the variables \(x,F,y\) give
\(R_x=\mathbb C[x,x^{-1},F,y]\), with
\(D=x^m\partial_y\). Thus its kernel is
\(\mathbb C[x,x^{-1},F]\). If a polynomial invariant in \(R\)
required a denominator \(x^n\), choose such a presentation with
minimal positive \(n\). Reduction modulo \(x\) of its numerator
would give
\(h(0,-Q(0,y))=0\). Since \(Q(0,y)\) is nonconstant,
\(h(0,F)=0\), so \(x\) divides the numerator already in
\(\mathbb C[x,F]\), a contradiction.

The quotient map \(\operatorname{Spec}R\to\operatorname{Spec}C\)
is surjective on complex points. At \(x=\alpha\ne0\) one solves
for \(z\); at \(x=0,F=\nu\), the equation
\(Q(0,y)+\nu=0\) has a root. Consequently a slice for (2)
forces
\[
(A,B)C=C.
\tag{7}
\]
Indeed, a common zero of \(A,B\) would lift to a point of
\(\operatorname{Spec}R\), and all coefficients of \(E\) would
vanish there. Nullstellensatz then gives (7).

The stronger necessary condition is
\[
B(0,F)\in\mathbb C^*.
\tag{8}
\]
Sections 2 and 3 prove this without imposing smoothness, transverse
intersection, or reducedness on the plane curve \(B=0\).

## 2. The DVR obstruction

Let \(V\) be a discrete valuation ring containing \(\mathbb C\),
with uniformizer \(\pi\), fraction field \(L\), and residue field
\(\mathbb C\). Suppose \(C\to V\) maps \(x\) to a nonzero
element of \(\pi V\) and \(F\) to an element whose residue is
\(\nu\in\mathbb C\). Form
\[
T=R\otimes_CV
=V[y,z]/(x^m z-Q(x,y)-F).
\tag{9}
\]
The induced derivation \(D_V\) kills \(V\), sends \(y\) to
\(x^m\), and sends \(z\) to \(P(x,y)\).

The ring \(T\) is a domain. In the UFD \(V[y]\), the two
coefficients of the linear polynomial in \(z\) in (9) are
coprime: every nonunit divisor of \(x^m\) is a power of \(\pi\),
whereas \(Q(x,y)+F\) reduces to the nonconstant polynomial
\(Q(0,y)+\nu\). The linear polynomial is primitive and
irreducible over the fraction field of \(V[y]\), hence prime in
\(V[y,z]\) by Gauss's lemma.

Its generic fiber and special fiber are
\[
T_L=L[y],\qquad
T/\pi T=\mathbb C[y,z]/(Q(0,y)+\nu).
\tag{10}
\]
In particular the special fiber is nonzero, so \(\pi\) is not a
unit in \(T\). The generic derivation is
\(x^m\partial_y\), with kernel \(L\). Therefore
\[
\ker D_V=T\cap L=V.
\tag{11}
\]
To justify the last equality, an element of \(L\setminus V\)
has the form \(u\pi^{-n}\), \(u\in V^*\), \(n>0\).
If it belonged to \(T\), then multiplying by
\(u^{-1}\pi^{n-1}\) would put \(\pi^{-1}\) in \(T\),
contradicting the nonzero special fiber. This is the explicit
no-pole argument; invariant formation under arbitrary base change
is not being assumed.

The derivation \(D_V\) cannot have a slice. Such a slice would
give \(T=(\ker D_V)[s]=V[s]\), whose special fiber is
\(\mathbb C[s]\). But the polynomial in (10) has degree
\(d\ge2\). If it has at least two distinct roots, its quotient
has nontrivial idempotents. If it has one distinct root, that root
has multiplicity at least two and its quotient has a nonzero
nilpotent. Neither ring is \(\mathbb C[s]\).

Only the ordinary characteristic-zero slice theorem is used here.
It follows directly by induction on derivation degree: subtract
the appropriate invariant multiple of the highest power of a
slice. No cancellation theorem for surfaces or threefolds is used.

## 3. Why an invariant coefficient cannot meet the bad line

Suppose \(E\) has a slice and (8) fails. If
\(B(0,F)=0\) identically, then \(x\) divides \(B\). Choose
a root \(y_0\) of the nonconstant polynomial \(P(0,y)\).
At every point \(x=0,y=y_0\), both coefficients of \(D\)
and the coefficient \(B\) vanish. Thus \(E\) has a fixed
point, impossible for a derivation with a slice.

Otherwise \(B(0,F)\) is a nonconstant polynomial and has a root
\(\nu\). Choose an irreducible factor \(b\) of \(B\) with
\(b(0,\nu)=0\). Since \(x\) does not divide \(B\), the
curve \(\Gamma=\operatorname{Spec}C/(b)\) is not the line
\(x=0\). Normalize \(\Gamma\) and choose a point above
\((0,\nu)\). Its local ring \(V\) is a DVR with residue field
\(\mathbb C\), and the image of \(x\) is nonzero but nonunit.
These normalization facts follow from the standard curve results
in [Stacks, Tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R)
and [Tag 0C3P](https://stacks.math.columbia.edu/tag/0C3P).

Base-changing the equation \(ES=1\) along \(C\to V\) preserves
it. Because \(B\) maps to zero, the resulting derivation on
\(T[t]\) is \(\overline A D_V\). Evaluate its slice equation
at \(t=0\), obtaining
\[
\overline A D_V(S_0)=1.
\]
Since \(\overline A\in V\) is invariant,
\(D_V(\overline A S_0)=1\). This contradicts Section 2.

This argument treats a singular curve \(b=0\), tangent contact
with \(x=0\), and repeated factors of \(B\) without change.
One passes to a single reduced component solely to obtain a DVR;
the original slice equation remains valid after that base change.

We have proved (8). Combining it with (7), the element \(x\)
is a unit modulo \(B\), hence so is \(x^m\). Therefore
\[
(Ax^m,B)C=C.
\tag{12}
\]
Choose \(U,V\in C\) with \(Ax^mU+BV=1\). Then
\[
s=Uy+Vt,\qquad E(s)=1.
\tag{13}
\]
This supplies the required affine slice. Conversely (7) and (8)
imply (12), so they are an exact slice criterion in the case (4).

For orientation, the reduced plinth support in this case is exactly
the line \(x=0\):
\[
\sqrt{P_D}=(x).
\tag{14}
\]
We have \(x^m=Dy\in P_D\). If \(p\in P_D\) did not vanish
identically modulo \(x\), choose \(\nu\) with
\(p(0,\nu)\ne0\). Localizing at \(p\) gives a slice and hence
\(R_p=C_p[s]\). Its fiber at \((0,\nu)\) would be an affine
line, contradicting the same special fiber in (10). Thus
\(P_D\subseteq(x)\), proving (14). No equality of plinth
multiplicities is needed.

## 4. Constant residue and common-factor boundary cases

Now let \(P\) in (1) be arbitrary. Put
\[
e=\min\{m,\operatorname{ord}_xP\},\qquad
n=m-e,\qquad P_1=P/x^e,
\]
using \(\operatorname{ord}_x0=+\infty\), and write
\[
D=x^e\delta,\qquad
\delta=x^n\partial_y+P_1(x,y)\partial_z.
\tag{15}
\]
These are invariant replicas, so \(\ker D=\ker\delta\).

### 4.1. The case \(n=0\)

Here \(\delta y=1\). If \(Q_{1,y}=P_1\), then
\(F=z-Q_1(x,y)\) gives
\(R=\mathbb C[x,F,y]\), \(C=\mathbb C[x,F]\), and
\(D=x^e\partial_y\). Thus
\[
P_D=x^eC,\qquad
E\text{ has a slice}\Longleftrightarrow(Ax^e,B)C=C.
\tag{16}
\]
Necessity follows by evaluating a slice equation at \(y=t=0\);
sufficiency is a Bezout combination of \(y,t\). This includes
\(P=0\).

### 4.2. The case \(n>0\) and \(P_1(0,y)=c\in\mathbb C^*\)

There is an explicit polynomial \(\delta\)-slice. Choose
\(Q_{1,y}=P_1\), \(Q_1(x,0)=0\), and write
\[
Q_1(x,y)=cy+xH(x,y),\qquad F=x^n z-Q_1(x,y).
\]
As in (6), \(C=\mathbb C[x,F]\). Define polynomials in
\(\mathbb C[x,F]\) recursively by
\[
I_0=-F/c,\qquad
I_{j+1}=-F/c-(x/c)H(x,I_j).
\tag{17}
\]
After \(n-1\) updates, \(I=I_{n-1}\) satisfies
\(I(x,F)-y\in x^nR\). Indeed the initial difference is in
\(xR\), and each update improves its order by one, up to the
error \(x^nz/c\). The polynomial
\[
w=(y-I(x,F))/x^n\in R
\tag{18}
\]
therefore satisfies \(\delta w=1\). Hence \(R=C[w]\),
\(D=x^e\partial_w\), and (16) again holds, with \(w\) in
place of \(y\). This proof avoids invoking a general theorem
about free actions on three-space.

### 4.3. The case \(n>0\) and \(P_1(0,y)\) nonconstant

The polynomial \(P_1(0,y)\) cannot be identically zero, by the
choice of \(e\). Apply Sections 1-3 to \(\delta\), with
coefficient \(A'=Ax^e\) and exponent \(n\). Here the invariant
coordinate is \(F=x^nz-Q_1(x,y)\), where
\(Q_{1,y}=P_1\) and \(Q_1(x,0)=0\). A slice forces
\(B(0,F)\in\mathbb C^*\), and the resulting Bezout identity is
\[
A'x^nU+BV=Ax^mU+BV=1.
\]
Thus (13) remains an affine slice for the original \(E\).
Equivalently, in this case the exact criterion is
\[
(A,B)C=C\quad\text{and}\quad B(0,F)\in\mathbb C^*.
\tag{19}
\]
The reduced plinth support remains \((x)\), since
\(P_D=x^eP_\delta\) and \(\sqrt{P_\delta}=(x)\).

These three cases exhaust (1) for every \(m\ge1\) and every
\(P\), without a degree bound. The case \(m=0\), if added,
is immediately Section 4.1 with \(e=0\).

## 5. Affine-slice equivalence and exact scope

For any nonzero base derivation and invariant coefficients with
\(A\ne0\), a slice \(r+ht\) affine in \(t\) has
\(Dh=0\), and then \(ADr+Bh=1\) implies \(D^2r=0\).
Thus it is equivalent to \(AP_D+BC=C\). The converse is the
same Bezout identity. Sections 1-4 establish the missing
arbitrary-slice-to-affine-slice implication for (1), proving (3).

If \(A=0\), a slice forces \(B\) to be a nonzero constant,
and \(t/B\) is an affine slice; this also satisfies (3). If
\(B=0\), a slice forces \(A\) to be a unit and \(D\) to
have a slice, by evaluating at \(t=0\). If \(A=B=0\), both
sides of (3) are false. These statements use the polynomial-base
unit condition and are not transferred to arbitrary localizations.

The proof supplies the exact hypothesis of an affine-slice lifting
argument. It does not silently identify an affine slice with a
coordinate. In the nonlinear-residue branch, (8) yields a nonzero
scalar modulo \(x\), not necessarily modulo the full local-slice
value \(x^m\). More generally, the rank-one control in
[quotient-slice-boundary-pass15.md](quotient-slice-boundary-pass15.md)
shows that plinth unimodularity does not force a scalar congruence
modulo a chosen local-slice value. No such extra implication is
used here.

The DVR argument uses the explicit primitive linear-in-\(z\)
presentation and its special fiber. It has not been replaced by a
theorem asserting that invariants commute with arbitrary base change.
No claim is made that arbitrary rank-three LNDs admit this triangular
presentation, or that the remaining global cancellation problem is
settled.

Since (1) fixes the ambient coordinate \(x\), polynomial-kernel
closure under an \(E\)-slice is already in the earlier
[invariant-coordinate scope](commuting-coordinate-partial-pass.md).
The content established here is the stronger affine replacement
and plinth-unit-ideal criterion in the specified original frame.

## 6. Exact controls

Thirteen inline exact checks with `/opt/anaconda3/bin/python` and
SymPy passed in 0.125 seconds. They included the following distinct
mechanisms.

For \(D=x^3\partial_y+(2y+xy^2)\partial_z\), put
\(F=x^3z-y^2-xy^3/3\). Taking
\(A=x^2\), \(B=1+xF\), and
\(M=\sum_{j=0}^4(-xF)^j\) gives
\[
s=-F^5y+Mt,\qquad (AD+B\partial_t)s=1.
\]
This checks a nonconstant \(A\), a higher-power local slice, and
an invariant \(B\) which is scalar modulo \(x\) but not modulo
\(x^3\).

For \(\delta=x^3\partial_y+(1+2xy)\partial_z\), the two
updates in (17) give a polynomial quotient (18) with
\(\delta w=1\). The additional replica control
\(D=x^2\delta\), \(B=1+xF\) has the affine slice
\(F^2w+(1-xF)t\).

The negative controls used
\(D=x\partial_y+2y\partial_z\), \(F=xz-y^2\).
The choice \(B=F-1\) is fixed-point-free but has the split
special fiber \(\mathbb C[y,z]/(y^2+1)\), so has no slice.
The singular curve \(B=F^2-x^3=0\), normalized by
\(x=\tau^2,F=\tau^3\), gives the special relation
\(\tau^2z-y^2-\tau^3\), reducing to \(-y^2\). The checks
confirmed its derivation invariance and a genuinely nonzero
nilpotent class in the special fiber.

These are algebraic controls of the displayed formulas. The
normalization, no-pole argument, and all-degree conclusion are
proved in Sections 1-5, not inferred from these finite checks.

## 7. Arbitrary univariate leading coefficient

Let
\[
D=p(x)\partial_y+P(x,y)\partial_z,
\qquad 0\ne p\in\mathbb C[x],\quad P\in\mathbb C[x,y],
\tag{20}
\]
and keep \(E=AD+B\partial_t\), \(A,B\in C=\ker D\).
Then the equivalences (3) hold without change.

There is a more explicit criterion. Let \(h\in\mathbb C[x]\)
be the monic greatest common divisor of \(p\) and all the
coefficients of \(P\), viewed as a polynomial in \(y\). For
\(P=0\), take \(h\) to be the monic associate of \(p\).
Write
\[
p=ha,\qquad P=hP_1,\qquad
D=h\delta,\qquad
\delta=a(x)\partial_y+P_1(x,y)\partial_z.
\tag{21}
\]
Choose \(Q_y=P_1\), \(Q(x,0)=0\), and set
\[
F=a(x)z-Q(x,y),\qquad C=\mathbb C[x,F].
\tag{22}
\]
Define the finite set
\[
\Sigma=
\{\alpha:h(\alpha)=0\}
\ \cup\
\{\alpha:a(\alpha)=0,\ \deg_yP_1(\alpha,y)\ge1\}.
\tag{23}
\]
At a root of \(a\), the polynomial \(P_1(\alpha,y)\) is
never zero identically, by the gcd choice. Thus the roots of
\(a\) excluded from the second set in (23) have nonzero
constant residue.

The exact criterion is
\[
E\text{ has a slice}
\quad\Longleftrightarrow\quad
(A,B)C=C\quad\text{and}\quad
B(\alpha,F)\in\mathbb C^*
\text{ for every }\alpha\in\Sigma.
\tag{24}
\]
When \(\Sigma\) is empty, the second condition is vacuous.
The proof also shows
\[
\sqrt{P_D}
=\left(\prod_{\alpha\in\Sigma}(x-\alpha)\right)C,
\tag{25}
\]
with the empty product equal to 1. No assertion about the
multiplicities of these factors in \(P_D\) is required.

### 7.1. The invariant ring and surjectivity

Since \(h\ne0\), the kernels of \(D\) and \(\delta\)
are equal. On inverting \(a\), the ring is
\(\mathbb C[x,1/a,F,y]\) and \(\delta=a\partial_y\).
For every root \(\alpha\) of \(a\), the polynomial
\(Q(\alpha,y)\) is nonconstant. The same denominator argument
as in Section 1, now removing one factor \(x-\alpha\) at a
time, proves (22). If \(a\) is a nonzero constant, (22)
follows immediately by solving for \(z\).

The map \(\operatorname{Spec}R\to\operatorname{Spec}C\)
is again surjective on complex points: when \(a(\alpha)\ne0\)
one solves for \(z\), and when \(a(\alpha)=0\) one solves
the nonconstant polynomial equation \(Q(\alpha,y)+\nu=0\).
Therefore an \(E\)-slice forces \((A,B)C=C\), by the
fixed-point argument from Section 1.

### 7.2. Good roots have a global local-slice witness

Let \(\alpha\) be a root of \(a\) with multiplicity \(n\),
and suppose \(P_1(\alpha,y)=c\in\mathbb C^*\). Write
\[
a=(x-\alpha)^n u(x),\qquad u(\alpha)\ne0,
\qquad
Q(x,y)=cy+(x-\alpha)H(x,y).
\]
Use the finite recursion
\[
I_0=-F/c,\qquad
I_{j+1}=-F/c-((x-\alpha)/c)H(x,I_j),
\qquad I=I_{n-1}.
\tag{26}
\]
Exactly as in Section 4.2,
\(y-I(x,F)\in(x-\alpha)^nR\). Hence
\[
r_\alpha=\frac{y-I(x,F)}{(x-\alpha)^n}\in R,
\qquad \delta r_\alpha=u(x).
\tag{27}
\]
The quotient in (27) is already a polynomial in the original
ring. In particular the other roots contribute only the polynomial
\(u\), which is nonzero at \(\alpha\); no untracked inverse
of another root factor has been introduced. Equivalently,
\(r_\alpha/u\) is a slice after localizing at \(u\), and
(27) explicitly clears that denominator.

Thus \(u\in P_\delta\) and the plinth ideal does not vanish
at any point of the line \(x=\alpha\).

### 7.3. The plinth support is exactly the bad vertical lines

Since \(\delta y=a\), the zero set of \(P_\delta\) is
contained in the union of lines over roots of \(a\). Section
7.2 excludes every root with nonzero constant residue. At a
remaining root \(\alpha\), \(Q(\alpha,y)\) has degree at
least two. If some \(p_0\in P_\delta\) were nonzero at
\((\alpha,\nu)\), localization at \(p_0\) would give a slice
and make the fiber at that point an affine line. Its actual ring is
\[
\mathbb C[y,z]/(Q(\alpha,y)+\nu),
\]
which is disconnected or nonreduced. Therefore the entire line
\(x=\alpha\) belongs to the plinth zero set.

Finally,
\[
P_D=hP_\delta.
\tag{28}
\]
Indeed, if \(D r=h\delta r\) is invariant, applying
\(\delta\) and cancelling the nonzero invariant \(h\)
shows \(\delta^2r=0\); the converse is immediate. Equation
(28) adds exactly the lines over roots of \(h\). These
observations prove (25), including the case of an empty zero set.

### 7.4. A slice forces the added coefficient to avoid each line

At a root \(\alpha\) of \(h\), the derivation \(D\)
vanishes on the whole plane \(x=\alpha\). Surjectivity in
Section 7.1 implies that a zero of \(B(\alpha,F)\) would
give an \(E\)-fixed point. Thus \(B(\alpha,F)\) is a
nonzero constant.

Now let \(\alpha\) be a root of \(a\) with nonconstant
\(P_1(\alpha,y)\). If \(B(\alpha,F)\) is identically
zero, choose a root of \(P_1(\alpha,y)\); at the resulting
point, both \(D\) and \(B\partial_t\) vanish.

If instead \(B(\alpha,F)\) has a zero \(\nu\) without
being identically zero, select an irreducible component of
\(B=0\) through \((\alpha,\nu)\), normalize it, and take
the DVR at a point above \((\alpha,\nu)\). The function
\(x-\alpha\) is nonzero but nonunit there, and all other
root factors of \(a\) are units. The base-change ring is
\[
T=V[y,z]/(a(x)z-Q(x,y)-F).
\tag{29}
\]
The proof in Section 2 applies verbatim: the relation is primitive
linear in \(z\), its generic fiber is \(L[y]\), and its
special fiber is the degree-at-least-two ring in Section 7.3.
The no-pole argument gives \(\ker\delta_V=V\), and this
derivation has no slice.

But an \(E\)-slice base-changes, after \(B\) becomes zero,
to a slice for \(\overline A\,\overline h\,\delta_V\)
on \(T[t]\). Evaluation at \(t=0\), followed by multiplying
by the invariant \(\overline A\,\overline h\), gives a
\(\delta_V\)-slice. This contradiction proves the required
condition on \(B\) for every line in (23).

### 7.5. The global affine slice

The preceding steps show that an \(E\)-slice forces both
\((A,B)C=C\) and \((P_D,B)C=C\). Conversely, the conditions
on the right side of (24), together with (25) and
Nullstellensatz in \(C=\mathbb C[x,F]\), give these same two
unit-ideal statements.

Choose
\[
AU+BV=1,\qquad p_0+BW=1,\qquad p_0\in P_D.
\]
Multiplying the identities gives
\[
1=AUp_0+B(AUW+Vp_0+BVW).
\tag{30}
\]
Since \(Up_0\in P_D\), choose \(r\in R\) with
\(Dr=Up_0\). Then
\[
s=r+(AUW+Vp_0+BVW)t
\]
is an affine slice for \(E\). This proves (24) and (3) for
every nonzero \(p(x)\), including constant \(p\) and \(P=0\).

The global step is an ideal calculation using actual polynomial
local-slice witnesses. It does not assume that a scalar congruence
holds modulo the whole plinth generator, or that arbitrary invariant
rings satisfy a local-to-global slice principle.

### 7.6. A control with different root types

Take
\[
h=x+1,\quad a=x^2(x-1)^3,\quad
D=ha\partial_y+h(1+xy)\partial_z,
\qquad F=az-y-xy^2/2.
\]
The root \(x=0\) is good, the root \(x=1\) has nonlinear
residue, and \(x=-1\) comes from the common factor. Formula
(26) at \(x=0\) gives
\[
I=-F-xF^2/2,\qquad r=(y-I)/x^2\in R,
\qquad Dr=g=(x+1)(x-1)^3.
\]
Since \(g(0)=-1\), the polynomial \(V=(g+1)/x\) belongs
to \(\mathbb C[x]\). The extension \(E=D+x\partial_t\)
has the affine slice
\[
s=-r+Vt,\qquad Es=-g+xV=1.
\]
Its added coefficient takes different nonzero values on the two
bad lines, so this example is not based on a single scalar
congruence modulo their product.

Eight further inline exact checks passed in 0.067 seconds. They
verified polynomial divisibility for \(r\) and \(V\), the
invariant \(F\), the local-slice derivative, the Bezout and slice
identities, the split quadratic residue at \(x=1,F=0\), and
the vanishing of the base vector field at \(x=-1\). They do
not replace the arbitrary-degree argument in Sections 7.1-7.5.
