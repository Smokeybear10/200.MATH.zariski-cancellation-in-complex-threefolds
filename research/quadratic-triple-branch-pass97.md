# A varying triple-component conormal forces a special base tangent

In an actual quadratic fiber of profile (3,1), suppose the collapsed
triple component has nonzero first normal N-action. The essential
split degree-two base branch must then have a distinguished vertical
tangent and multiplicity divisible by three. In particular it cannot
be smooth.

This local argument alone does not exclude the profile. In its surviving case there are
three arithmetic transverse branches, and two can carry one source
label while the third carries the other. An exact formal control below
realizes that assignment. Counting source normalization points as if
they were transverse branches would give a false exclusion.

Current status: the independent
[saturated source-balance theorem97](quadratic-saturated-source-balance-pass97.md)
excludes the actual (3,1) configuration without a first-normal-action
hypothesis. The local argument below is retained as a conditional
diagnostic. Its exact control still distinguishes formal descent and
formal invariance from rationality on the actual exceptional surface;
it is not an actual (3,1) frame.

## 1. Actual local form, including the constant cubic coefficient

Retain the supplied actual nonconical quadratic frame of
[checkpoint96](checkpoint-pass96-working.json). Let \(\mathfrak q\)
be its multiplicity-three component over the closed base point b.
By compatibility96 it is collapsed; its reduced ring is
\(\mathbb C[\bar c]\), and its actual centered normal generators
F,G have \(N^3F=N^3G=0\).

Assume that the first normal action is nonzero generically.
The [weighted theorem94](nonconical-weighted-conormal-rigidity-pass94.md)
and [polynomial-column theorem94](nonconical-conormal-column-classification-pass94.md)
give a constant
normal row and a polynomial conormal column whose span is
\(\{1,c\}\) or \(\{t,t^k\}\), after constant changes. The second
case has a common zero and hence a quotient-rank-zero point.
Everywhere rank95 excludes it at multiplicity three too.
We may therefore choose centered base coordinates x,z and
the actual normal complement y=G so that
\[
\begin{gathered}
L=\mathbb C(c)\subset O=A_{\mathfrak q},\qquad
\widehat O=L[[x,y]],\qquad
x\equiv F,\quad z\equiv cF\pmod{\mathfrak q^2},\\
z=f(x,y),\qquad
f=cx+a(c)y^3+f_{>3},\qquad a(c)\ne0,\\
\operatorname{wt}(x)=3,\quad \operatorname{wt}(y)=1,\qquad
D_*=(\gamma x+\rho y^3)\partial_y+\lambda y^2\partial_c,\\
\epsilon_0=\nu\in\mathbb C^*,\quad
\gamma=-\nu,\quad \rho=-\nu a',\quad \lambda=3\nu a .
\end{gathered}
\tag{1}
\]
The coefficient field is the specified actual \(\mathbb C(c)\);
it is not N-invariant. Its compatibility with completion and
the strict weight increase of every omitted Hamiltonian term
are precisely the proved weighted94 statements. The constant
\(\nu\) comes from the original volume along the entire component.

The actual identity \(N^3G=0\) gives \(D_*^3y=0\). The coefficient
of \(x^2y\) in this cube is
\(2\gamma(\lambda\gamma'+3\gamma\rho)\).
Since \(\gamma\) is a nonzero constant, \(\rho=0\), so \(a'=0\).
Thus the full, not truncated, local equation has the form
\[
\boxed{\quad
f(x,y)=cx+a y^3+R(x,y),\qquad
a\in\mathbb C^*,\qquad
R\in(x^2,xy,y^4)L[[x,y]] .
\quad}
\tag{2}
\]
Only its indicated leading part is prescribed. No full-ring
identity \(N^2G=0\), polynomial coordinate change, or local
nilpotence on \(\widehat O\) follows from this step.

## 2. A normalized complex base branch

Take any one reduced unibranch germ of the exceptional base
curve at b. Use its actual normalization parameter t:
\[
\begin{gathered}
x=x(t),\quad z=z(t)\in t\mathbb C[[t]],\qquad
m=\min\{\operatorname{ord}_t x(t),\operatorname{ord}_t z(t)\},\\
x(t)=x_0t^m+\text{higher terms},\qquad
z(t)=z_0t^m+\text{higher terms},\qquad (x_0,z_0)\ne(0,0),\\
\Phi(t,y)=f(x(t),y)-z(t),\qquad R_t=L[[t]] .
\end{gathered}
\tag{3}
\]
The branch multiplicity is m. Either displayed leading
coefficient may be zero. Its tangent is nonvertical when
\(x_0\ne0\), and is the distinguished line x=0 when \(x_0=0\).
All coefficients \(x_0,z_0\) are complex constants; they are
not allowed to depend on the component parameter c.

Equation (2) implies
\(\Phi\bmod t^m=f(0,y)=y^3u_0(y)\), where \(u_0(0)=a\).
Also \(\Phi(t,0)\) has order exactly m, with leading
coefficient \(cx_0-z_0\ne0\) in L. Formal preparation gives
\[
\begin{gathered}
\Phi(t,y)=U(t,y)P(t,y),\qquad U(0,0)=a,\quad U\in R_t[[y]]^*,\\
P=y^3+A_2(t)y^2+A_1(t)y+A_0(t),\\
A_1,A_2\in t^mR_t,\qquad
A_0=\frac{cx_0-z_0}{a}t^m+O(t^{m+1}) .
\end{gathered}
\tag{4}
\]
Here is a direct preparation argument sufficient for these
coefficient claims. Start modulo t with \(U=u_0(y)\), \(P=y^3\).
At each t-adic order divide the remaining error by \(u_0(y)\)
and split the resulting series uniquely into a polynomial of
y-degree below three plus a multiple of \(y^3\). Correct P
by the first part and U by \(u_0\) times the second. The
cross-error has higher t-adic order. Completeness gives the
displayed factorization. There are no corrections before
order m. Evaluating at y=0 determines the leading coefficient
of \(A_0\) because \(U(0,0)=a\).
This retains every higher term of the original f.

## 3. Nonvertical branches give an irreducible cubic over the actual field

Any root of the monic cubic P in \(L((t))\) belongs to \(L[[t]]\),
since that DVR is integrally closed. It has positive valuation:
the reduction of P is \(y^3\). Comparing valuations in (4)
shows that a root of valuation r must satisfy \(3r=m\).
If \(3r<m\), its cube is the unique lowest term; if \(3r>m\),
the constant coefficient is the unique lowest term.

If three does not divide m, no such Laurent-series root exists.
If \(m=3k\), write a possible root as \(y=t^k b(t)\). The
leading coefficient equation is
\[
b(0)^3=\frac{z_0-cx_0}{a}.
\tag{5}
\]
When \(x_0\ne0\), the right side has a simple zero as a rational
function of c, and is not a cube in \(\mathbb C(c)\). Thus
there is again no root. A reducible cubic over a field has
a linear factor, so P is irreducible over \(L((t))\).

Its finite algebra \(R_t[y]/(P)\) is a domain. The integral
closure of a complete DVR in a finite field extension is a
local DVR.[^hensel] Consequently its normalization has one
arithmetic branch. This means one branch over L, before
extending L to an algebraic closure. Such an extension can
split its residue field; those geometric conjugates must not
be relabeled independently.

## 4. Why these are the branches relevant to the actual source labels

The normalization of the complex base branch is finite and
birational. After the completed extension of its constants to L, it is
\(L[[t]]\). The finite local map in (2) has rank three:
apply the same preparation construction to \(f(x,y)-z\)
over \(L[[x,z]]\). Restricting this map to the base branch
and then pulling back its normalization gives exactly the
finite free \(R_t\)-algebra in (4).

The normalization pullback is birational away from t=0,
where the conductor of the base-branch normalization is
invertible. The finite free pullback has no t-torsion.
It has the same horizontal total fraction algebra as the
unnormalized pullback. Their horizontal normalizations are
therefore the same. A conductor-supported vertical artifact
is not an additional exceptional branch counted by the
positive Thom column.

The actual factorization \(E\to Z\to\Gamma\) induces the
corresponding map on these horizontal branches. After
normalizing one of them, its dominant map to a source-curve
component lifts to that component's normalization: elements
integral over the source ring are integral in the normalized
branch field and belong to its integrally closed valuation
ring. Completion of the finite normalized curve cover over
the chosen base branch has factors indexed by its normalized
source points. A local normalized arithmetic branch chooses
just one such factor, and hence one source label.

Those labels are actual complex points of the source
normalization. They are fixed under every automorphism over
L of an algebraic closure of L. If an arithmetic branch
splits geometrically, all its conjugates therefore retain
its one label. In particular the unique arithmetic branch
of Section 3 cannot supply positive entries at two different
normalized source points. This is the required label gate;
it does not identify the number of source points with the
number of geometric transverse branches.

## 5. Consequence for the essential split branch of a (3,1) fiber

The exact supported columns in
[supported-lattice97](quadratic-supported-lattice-pass97.md)
give an essential split degree-two base branch. Its two
normalized source points have ramification indices one,
and the triple component's column there is \((2,1)^t\),
up to ordering. Both labels must occur.

Section 3 excludes a nonvertical tangent. The same valuation
argument excludes \(3\nmid m\) even for a vertical tangent.
Therefore
\[
\boxed{\quad
\mu=3,\ \text{first normal action nonzero},\ (3,1)\text{ fiber}
\quad\Longrightarrow\quad
x_0=0,\qquad 3\mid m
\quad}
\tag{6}
\]
for its essential split base branch, in the normalized base
coordinates of (1). This necessary condition concerns the
actual distinguished direction. A further constant base
change does not erase the condition by choosing a convenient
projection parameter.

In the surviving case, write \(m=3k\). Then \(z_0/a\) is a
nonzero complex cube. Substituting \(y=t^kY\) and dividing
P by \(t^{3k}\) gives a monic cubic over \(R_t\), whose
reduction is \(Y^3-z_0/a\). Its three roots are simple and
belong to L. Successive coefficient lifting gives three
distinct roots in \(L[[t]]\), so the original P splits
completely. There are exactly three arithmetic normalized
branches, each of degree one over the base normalization.
Their source labels can group as two at one point and
one at the other. Condition (6) is thus not an exclusion.

## 6. An exact intrinsic and formal control of the surviving assignment

On the literal polynomial ring take
\[
\begin{gathered}
A_0=\mathbb C[x,y,c],\qquad
N_0=x\partial_y-3y^2\partial_c,\qquad z=cx+y^3,\\
\ker N_0=\mathbb C[x,z],\qquad
A_0/(x,z)=\mathbb C[y,c]/(y^3),\\
x=t^4,\quad z=t^3,\qquad
y^3=t^3(1-ct).
\end{gathered}
\tag{7}
\]
This triangular field is an actual primitive polynomial LND.
Its kernel follows by the x-local slice and contraction,
since \(z\bmod x=y^3\) is transcendental over \(\mathbb C\).
The component has multiplicity three, varying column
\((1,c)^t\), and \(N_0^3x=N_0^3y=0\).
The base branch \(x^3=z^4\) is unibranch, with vertical
tangent and multiplicity three.

In \(L[[t]]\), choose the uniquely specified series
\(\vartheta=(1-ct)^{1/3}\) and \(s=(1+t)^{1/2}\) with
constant term one. Put \(Y=y/\vartheta\). The pullback of the
base normalization now has equation \(Y^3=t^3\). In its nonnormal
finite ring itself, not just in the normalization, set
\[
H=\frac{s}{3}(t^2-2tY-2Y^2),\qquad
H^2=t^4(1+t)\quad\bmod(Y^3-t^3).
\tag{8}
\]
To check the identity without series expansion, the difference
\((t^2-2tY-2Y^2)^2-9t^4\) is divisible by \(Y^3-t^3\);
then use \(s^2=1+t\).
At \(Y=t\), H has value \(-t^2s\). At the other two
cube-root branches, it has value \(+t^2s\).

The finite complex curve \(H^2=t^4(1+t)\) has normalization
\(t=w^2-1,\ H=t^2w\). Its two normalized points over t=0
are \(w=-1\) and \(w=1\), glued at the single singular
point of the curve. Equation (8) gives an exact morphism
from the base-normalized formal pullback to the completed source
curve. It assigns one branch to the first label and two
to the second, all with normalized parameter degree one.
Thus the two positive label entries are \((1,2)^t\),
equivalent to the required ordering in Section 5.

There is a stronger formal control which does descend to the
unnormalized cusp pullback. Put
\(B_0=L[[t^3,t^4]]\), let \(R_0\) be that unnormalized
completed pullback, and let \(D_0=R_0\otimes_{B_0}L[[t]]\).
Here \(R_0=B_0[y]/(y^3-z+cx)\) is finite free of rank
three over \(B_0\), so the map \(R_0\to D_0\) is injective.
The normalization \(L[[t]]\) is generated by \(1,t,t^2\)
over \(B_0\). Also \(t^6,t^7,t^8=(z^2,xz,x^2)\) belong
to \(B_0\). Hence \(t^6L[[t]]\subset B_0\), and tensoring
these explicit expressions gives \(t^6D_0\subset R_0\).
It follows that
\[
\begin{gathered}
K=t^6H\in R_0,\qquad
K^2=t^{16}(1+t)=x^4+x^2z^3,\\
Z_0=\operatorname{Spec}
\frac{\mathbb C[x,z,K]}{(x^3-z^4,\ K^2-x^4-x^2z^3)},\\
x=(w^2-1)^4,\qquad z=(w^2-1)^3,\qquad
K=(w^2-1)^8w .
\end{gathered}
\tag{9}
\]
The target curve is a domain: its monic K-equation is
irreducible over \(\mathbb C(t)\), since \(1+t\) is not a
rational square. The displayed polynomial normalization
has the same fraction field; w is integral and
\(\mathbb C[w]\) is normal. Its two points w=1,-1 map to
the same origin. The formal map to its completion gives
the same two-to-one grouping as before. Thus failure of
formal descent is not an obstruction left by this control.

Even formal invariance holds. The extension of \(N_0\)
fixes t and s, while differentiating the defining equation
of \(\vartheta\) gives
\[
\begin{gathered}
N_0\vartheta=t\,y^2/\vartheta^2=tY^2,\qquad
N_0Y=(t^4-tY^3)/\vartheta=0,\\
N_0H=N_0K=0,\qquad
\operatorname{Frac}(E_0)=\mathbb C(t,y),\quad
c=(t^3-y^3)/t^4,\quad
N_0|_{\operatorname{Frac}(E_0)}=t^4\partial_y,\\
\ker(N_0|_{\operatorname{Frac}(E_0)})=\mathbb C(t).
\end{gathered}
\tag{10}
\]
Here \(E_0\) is the actual exceptional surface over the
cusp for this intrinsic quotient. The displayed rational
parametrization gives its function field. In particular,
after using z=cx+y^3, the equation \(z^4=x^3\) is
irreducible over \(\mathbb C(x,y)\), by the x-adic valuation
and coprimality of four and three. Also t=x/z in that field.
Equation (10) follows either by differentiation or from
the same rational parametrization.

The formally invariant K is not a rational function on
\(E_0\). Otherwise (10) would place it in \(\mathbb C(t)\),
contradicting \(K^2=t^{16}(1+t)\), whose right side has
odd valuation at t=-1. This proves, rather than merely
leaves open, its failure to be a global regular invariant.
Formal invariance and conductor descent have not supplied
an actual algebraic exceptional-surface factorization.

This is still only an intrinsic action and a formal
curve-map control. The degree-two target has not been
identified with the actual intermediate quotient curve of
\(N_0\). In fact the actual divisor x=0 for this intrinsic
quotient has algebraic constant-field degree three over
\(\mathbb C(z)\), since z=y^3 there. It violates the
all-divisor degree-two gate of the studied original frame.
No original four-coordinate inverse or actual (3,1) action
is asserted.

## 7. Scope and verification

The nonzero first normal action, actual degree-two identities
and original volume are used to obtain the constant a in (2).
The completed calculation retains all higher terms. The
irreducibility argument is over the specified field
\(\mathbb C(c)\), not after silently choosing algebraic
coefficient functions. The normalization argument preserves
the distinction between arithmetic branches, geometric
branches, and complex source labels.

The first-normal-action-zero sector is outside this theorem.
The vertical singular case remains possible at this local
level. Neither whole-profile exclusion, freeness, recognition,
nor an arbitrary-frame reduction is proved.

The retained weighted and column proofs94, current fiber
restrictions96 and supported source-column proof97 were
read for these applications. Their prior primary-source
dependencies are not freshly reconstructed here.
The preparation and root arguments above are elementary
coefficient constructions, not a citation to a numerical
Newton-polygon test. The [companion finite checker](quadratic_triple_branch_checks_pass97.py) tests
only the displayed polynomial LND and formal label-control
identities; it does not prove the universal branch or
original-frame statements.

The first assertion-bearing author run of
`/opt/anaconda3/bin/python research/quadratic_triple_branch_checks_pass97.py`
passed one method in 0.038 seconds, exit zero, with full output
in tool chunk `7058f2`. It imports only unittest and SymPy.
An earlier malformed add-file patch was rejected before creating
either file; it was corrected before this first execution.
No numerical assertion failed, and no frozen file was edited.
The final conductor-descent and formal-invariance version
passed the same one method in 0.044 seconds, exit zero,
with full output in tool chunk `3806fa`. This is a
later version of that method, not an additional test count.

[^hensel]: The Stacks Project,
    [Remark 15.116.1, tag 09EM](https://stacks.math.columbia.edu/tag/09EM),
    especially (1), (4) and (7), and
    [Lemma 10.153.4, tag 04GH](https://stacks.math.columbia.edu/tag/04GH).
    Both complete displayed passages, including their given
    arguments, were freshly read on September 14, 2026.
    They give the finite local DVR normalization in the
    finite separable extension of a complete DVR used here.
    Deeper cited normalization and henselian-equivalence
    proofs were not freshly reread.
