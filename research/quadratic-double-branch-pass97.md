# A varying double component forces a singular split branch

In a quadratic fiber with multiplicities (2,1), its double component
must contribute to both points of the split normalized cover. The
same conclusion holds for one selected component of a (2,2) fiber.
If the selected component's first
normal action is nonzero, that base branch has a prescribed tangent
and even multiplicity. In particular it cannot be smooth. The argument
uses the complete local equations, not just their leading polynomial.

This local argument alone does not exclude these profiles, handle a
component with zero first normal action, or recognize the threefold.
The separate [finite source-balance proof97](quadratic-saturated-source-balance-pass97.md)
now excludes (2,2) without that normal-action hypothesis. The argument
here remains relevant to the surviving (2,1) profile. An exact formal
example below shows why its singular tangent case cannot be discarded
by the local two-label argument alone.

## 1. The actual component and the distinguished tangent

Retain the actual quadratic frame and the conclusions of
[the96 checkpoint](checkpoint-pass96-working.json). In a (2,1) or
(2,2) fiber all fixed components are collapsed, smooth, disjoint
affine lines. The [supported lattice97](quadratic-supported-lattice-pass97.md)
distinguishes a double component C whose column at the split branch
is (1,1). For (2,2) its other essential entry, at the fully ramified
branch, is one. For (2,1) there is no such ramified branch: the
simple column is (1,0) up to ordering, and the full-basis determinant
forces the double column to be (1,1). Any extra degree-one rows are
forced by their multiplicities and do not affect this calculation.

Assume the first normal action of the canonical N is nonzero at the
generic point of this C. The [weighted conormal theorem94](nonconical-weighted-conormal-rigidity-pass94.md)
and [polynomial column classification94](nonconical-conormal-column-classification-pass94.md)
give the two column spans {1,c} and {c-c0,(c-c0)^k}. The second has a
rank-zero point. The everywhere rank bound95 excludes it, so constant
changes of the base and the two original good normal coordinates give
actual centered functions F,G and base parameters x,z with
\[
\begin{gathered}
A/\mathfrak q=\mathbb C[\bar c],\qquad
\mathfrak q=(F,G),\qquad N^3F=N^3G=0,\\
x\equiv F,\qquad z\equiv cF\pmod{\mathfrak q^2},\qquad
L=\mathbb C(c)\subset O=A_{\mathfrak q},\qquad
\widehat O=L[[x,y]],\quad y=G.
\end{gathered}
\tag{1}
\]
The symbols x,z here are coordinates of the invariant base plane.
They are not the original bad coordinate. The actual c is the affine
parameter on C; the residue identification in (1) fixes its coefficient
field in the completion. This field is not N-invariant.

The original volume calculation in column94 makes the leading local
Jacobian unit a nonzero constant nu, because the first conormal column
entry is one. With weights two on x and one on y, write
\[
\begin{gathered}
z=f(x,y)=cx+a(c)y^2+f_{>2},\qquad a(c)\ne0,\\
D_*=\bigl(-\nu x-\nu a'(c)y^2\bigr)\partial_y
              +2\nu a(c)y\partial_c,\qquad D_*^3y=0,\\
\boxed{\quad a(c)=a\in\mathbb C^*,\qquad
f(x,y)=cx+ay^2+O(x^2,xy,y^3).\quad}
\end{gathered}
\tag{2}
\]
To check the last step directly, in the notation of column94,
gamma=-nu, rho=-nu a', lambda=2nu a. The coefficient of x^2 in
D_*^3y is gamma(lambda gamma'+2gamma rho). Since gamma is a
nonzero constant, its vanishing forces rho=0 and hence a'=0.
Constants of rational differentiation on C(c) are C. Higher weighted
terms cannot enter this coefficient. No local nilpotence of the
completed derivation is assumed.

The line x=0 in the base tangent space is distinguished by these
normalizations. Changing c affinely replaces z by an affine linear
combination of z and x, and rescales x; it does not remove this line.
The conclusion below is stated in the actual coordinates (1).

## 2. The full quadratic after normalization of a base branch

Let a complex analytic base branch through the fiber value have a
primitive normalization parameter t and parametrization
(x(t),z(t)). Set n=min(ord_t x(t),ord_t z(t)); a zero series has
infinite order. Thus n is its ordinary plane-curve multiplicity.
Write x0,z0 for the coefficients of t^n, not both zero.

After this finite base normalization, the completed transverse
pullback at the generic point of C is
\[
\begin{gathered}
L[[t,y]]/(f(x(t),y)-z(t)),\\
f(x(t),y)-z(t)=U(t,y)W(t,y),\qquad U(0,0)=a,\\
W(t,y)=y^2+B(t)y+C(t),\quad B,C\in t^nL[[t]],\\
\operatorname{ord}_t C=n,\qquad
[t^n]C=(cx_0-z_0)/a.
\end{gathered}
\tag{3}
\]
Here U is a unit. Formal Weierstrass preparation applies because
the reduction at t=0 is y^2 times a unit. The lower coefficients
are divisible by t^n: modulo t^n the original series is again y^2
times a unit, and uniqueness of preparation forces its monic
prepared polynomial to be exactly y^2 modulo t^n. Evaluating at
y=0 proves the final coefficient, including the factor a.
It is nonzero since c is transcendental over C and x0,z0 are not
both zero. Terms in x^2 have order at least 2n and the other omitted
terms do not change this computation.

Here preparation can also be constructed directly. Begin modulo t
with W=y^2 and U=f(0,y)/y^2. If a factorization has been obtained
modulo t^k, divide its next error, after dividing by U(0,y), into
y^2 q(y)+r(y), with r of degree less than two. Add t^k r to W and
t^k U(0,y)q to U. This corrects the error modulo t^(k+1).
Completeness gives the factorization. At the first t-order where
two answers differ, the same division forces both differences to
vanish, proving uniqueness. This also proves the assertion modulo
t^n without dropping any higher y-terms.

For precision, the coefficient-compatible completion (1) comes from
the retained regular-local argument94. The normalized branch pullback
uses x=x(t) and z=z(t) before eliminating x. It does not identify the
normalization of the exceptional surface with the intermediate curve.

## 3. Irreducibility and source labels

Suppose W has a root v in L((t)). Since it is monic with reduction
y^2, v has positive integral valuation. If 2 ord_t(v) is less than n,
its square is the unique lowest-valuation term in W(v). If it is
greater than n, C is the unique lowest term. Therefore
\[
2\operatorname{ord}_t(v)=n,\qquad
v_0^2=(z_0-cx_0)/a,
\tag{4}
\]
where v0 is the leading coefficient. If n is odd there is no such
root. If x0 is nonzero, the right side has a simple zero as a rational
function of c, whereas every square in C(c) has even order at each
point. There is again no root. A quadratic over a field is reducible
exactly when it has a root. Thus W is irreducible in either case.

When x0=0 and n is even, substitute y=t^(n/2)v and divide by t^n.
The resulting monic polynomial over L[[t]] has reduction
v^2-z0/a, with two distinct roots in C. Hensel lifting gives two
distinct roots in L[[t]], so there are precisely two arithmetic
branches, both of degree one over the base normalization. This uses
only completeness and simple-root lifting.[^hensel]

The word arithmetic is important. The coefficient field is C(c),
not its algebraic closure. An irreducible W gives one branch of the
normalization over that field. One way to see this is to take the
integral closure of the complete DVR L[[t]] in its finite root field.
It is finite and local; completeness is henselian and a finite domain
cannot be a nontrivial product of local rings. The same normalization
is obtained from the finite order L[[t]][y]/(W).

Finiteness in this particular characteristic-zero situation has a
short direct proof. Scale a basis of the finite separable root field
so its elements are integral over the DVR. The trace-dual of their
span is a finite free DVR-module, since the field trace pairing is
nondegenerate. Every integral element lies in that dual: its product
with each integral basis element has trace integral over the DVR and
in its fraction field, hence in the DVR. The integral closure is a
submodule of this finite module over a Noetherian ring and is finite.
The henselian finite-algebra decomposition then gives locality.
This is the standard trace-dual argument of Stacks 032L; 09E8
also records the resulting single place for a henselian DVR.[^normal]

An actual normalized source point of Z is a label on such a branch.
The morphism to Z lifts on the normalization of the transverse
pullback: the extra functions in the finite normalization of Z are
integral, and the target branch ring is normal. On completing at the
base point, distinct normalized source points are different factors
of that finite curve algebra. A map from this product to a domain
selects one factor, because its idempotents map to zero or one.
Consequently one arithmetic branch cannot contribute to two distinct
complex source-normalization labels. This assertion is weaker than
equating the number of source labels with the number of geometric
branches after extending C(c). The normalization lift is an application
of the dominant-normal-source property in Stacks 035Q(4): the branch
maps nonconstantly to a component of the curve Z.[^lift]

The distinguished double component's split column is (1,1), so both
labels must occur with positive winding. Equations (3)--(4) therefore
force
\[
\boxed{\quad
\operatorname{ord}_t x(t)>\operatorname{ord}_t z(t)=n,
\qquad n\in2\mathbb Z_{>0}.
\quad}
\tag{5}
\]
The split branch is tangent to x=0 and is singular, of multiplicity
at least two. Its two arithmetic transverse branches have degree
one and must carry the two labels separately, since each column
entry is one.

This restriction applies to the split branch of the intrinsic
degree-two exceptional locus Delta_2 defined in lattice97. No choice
of extra degree-one product-complement components changes it. The
fully ramified branch, when present, has a different column and is not subject to
this two-label argument. If the selected component has zero first
normal action, (2) is unavailable and (5) is not asserted.

## 4. An exact formal control for the surviving tangent case

On the intrinsic polynomial ring C[x,y,c], let
z=cx+y^2 and D=x partial_y-2y partial_c. This is a primitive
triangular LND, with invariant plane C[x,z]. Its origin fiber is the
double line (x,y^2); the first conormal column is (1,c). These facts
do not supply the required original four-coordinate frame or a
second fiber component.

Take the singular vertical branch (x,z)=(t^3,t^2). Its full pullback
and the following formal units satisfy
\[
\begin{gathered}
y^2=t^2(1-ct),\qquad \theta^2=1-ct,\quad s^2=1+t,
\quad \theta(0)=s(0)=1,\\
H=s\,y/\theta,\qquad
H^2=t^2(1+t).
\end{gathered}
\tag{6}
\]
The two units exist by simple-root lifting. The target finite curve
C[t,H]/(H^2-t^2(1+t)) has two normalization points over t=0,
which meet at its one singular point. On the two pullback branches
y=+t theta and y=-t theta, H equals +ts and -ts respectively.
Thus there is an exact formal two-label map with column (1,1).

There is a stronger formal descent control. The cusp base ring
C[[t^2,t^3]] contains t^2 C[[t]], since every integer at least two
belongs to the semigroup generated by two and three. Write D0 for
the base-normalized pullback in (6), and R0 for the original
unnormalized completed pullback. The finite base normalization is
birational, and the flatness checked below gives R0 embedded in D0.
The conductor inclusion gives t^2 D0 contained in R0. Equivalently the coefficients of t^2 H in
its finite basis over C(c)[[t]] all lie in C(c)[[t^2,t^3]]. Hence
\[
\begin{gathered}
K=t^2H\in R_0,\qquad K^2=t^6(1+t)=x^2+xz^2,\\
Z_0=\operatorname{Spec}
\mathbb C[x,z,K]/(x^2-z^3,\ K^2-x^2-xz^2),\\
t=w^2-1,\qquad x=t^3,\quad z=t^2,\quad K=t^3w .
\end{gathered}
\tag{7}
\]
The finite free base change is torsion-free over the cusp base:
the formal map (x,y) to (x,z=cx+y^2) is finite free of rank two.
Thus the inclusion R0 into D0 and the conductor multiplication
can also be checked by tensoring that flat map with the base
normalization. This does not infer injectivity from birationality
alone for an arbitrary tensor product.

The displayed curve Z0 is finite of degree two over the cusp.
Its quadratic is irreducible in C(t), because 1+t has a simple
zero and is not a square. It is therefore a domain. The last
line is its normalization: w is integral, and its fraction field
is recovered from t=x/z and w=K/t^3. Both w=1 and w=-1 have the
same image (0,0,0), and the cover of the base normalization is
unramified there. Multiplication by t^2 preserves the two labels.

Consequently even formal descent to the original cusp pullback
does not exclude the permitted case if the finite source curve
is allowed to vary. This is still not an algebraic map from the
entire exceptional surface, an actual Stein factorization, or
a (2,1) or (2,2) action. The intrinsic example itself has only one reduced
component in the origin fiber.

In fact the descended K is formally D-invariant but provably not
rational on that algebraic exceptional surface. Since D(t)=0,
D(y)=t^3 and D(c)=-2y, differentiating theta^2=1-ct gives
D(theta)=t y/theta. Hence, for Y=y/theta, the identity
D(Y)=(t^3-tY^2)/theta=0 holds on Y^2=t^2. The square root s
is also fixed, so D(H)=D(K)=0. These are identities for the
extended derivation, not a claim of local nilpotence on the
formal ring.

On the other hand the actual exceptional surface over this cusp
has rational function field C(t,y), with
c=(t^2-y^2)/t^3 and D=t^3 partial_y. Its rational invariant
field is exactly C(t). If K were rational, its formal invariance
would put it in C(t). But K^2=t^6(1+t) has no square root in
that field, since its order at t=-1 is odd. This contradiction
proves nonrationality. Thus neither completion nor formal
invariance supplies the actual global algebraic factorization.

## 5. Verification, dependencies, and limits

The proof uses the actual normal/volume and degree identities94,
the everywhere rank bound95, the compatibility and full lattice96,
and the new two-column classification97. Its branch arithmetic is
proved above with higher terms retained. The analogous cubic
investigation is recorded separately in
[triple-branch97](quadratic-triple-branch-pass97.md).

The [standalone checker](quadratic_double_branch_checks_pass97.py)
checks the weighted coefficient forcing a'=0, exact formal-control
relations and a finite range of perturbed quadratic valuation
examples. It does not verify the actual-frame hypotheses, all
power-series preparation, normalization functoriality, or the
universal geometric conclusion. Its execution is recorded in the
pass97 verification capture, not presumed here.

The needed preparation and finite-normalization arguments are given
above in their specific complete-DVR setting; the separable trace
pairing and the normalization lift remain standard algebraic facts.
The complete stated Stacks simple-root and completeness arguments
were read for this pass. No independent human review,
formal proof certificate, novelty clearance or general cancellation
result is claimed. All files through96 remain unchanged.

[^hensel]: The Stacks Project, [Lemma 15.11.4, 0ALJ](https://stacks.math.columbia.edu/tag/0ALJ)
    and [Lemma 10.153.3, 04GG](https://stacks.math.columbia.edu/tag/04GG).
    These supply henselian completeness, simple-root lifting and
    decomposition of finite algebras. The separate preparation and
    trace-dual arguments above are not attributed to these lemmas.

[^normal]: The Stacks Project, [Lemma 10.161.8, 032L](https://stacks.math.columbia.edu/tag/032L)
    and [Remark 15.113.6, 09E8](https://stacks.math.columbia.edu/tag/09E8).
    Their complete displayed arguments were read. The latter explicitly
    distinguishes a general semilocal normalization from the one-place
    henselian case. No claim about an algebraic closure of C(c) is used.

[^lift]: The Stacks Project, [Lemma 29.55.5(4), 035Q](https://stacks.math.columbia.edu/tag/035Q).
    The complete displayed statement and proof were read. Its dominance
    hypothesis is checked on each nonconstant branch, not assumed for
    an arbitrary map into the singular locus.
