# Mixed-fiber rigidity and the remaining recognition problem

In the actual collapsed mixed sector with L(m) nonzero, every function
of N-degree at most two is constant along the reduced components, and
even its nilpotent coefficient is independent of the component parameter.
Thus a hidden degree-two parameter cannot resolve this mixed sector.
The finite translation kernels also have an exact formal description.
Separately, the local conic has no section over its specified base, so
a particular published patching theorem is definitively unavailable.

These are conditional advances in the supplied quadratic frame. They
do not solve the working complex-threefold cancellation question
\[
A[u]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\]
The professor has not confirmed that this is the intended correction
of the emailed statement. There is still no reduction from an arbitrary
sliced action to the special coordinate assumptions below. The relative
cubic branch also remains separate.

## 1. The actual mixed sector has no hidden quadratic parameter

In the retained frame, B=C[x1,x2,x3,z]=A[u], E=partial u,
E squared of each xi is zero, E squared of z is a nonzero constant
q0, and u=Ez/q0. The canonical Jacobian LND N on A has full kernel
S=C[s1,s2], with S into A faithfully flat and generic fiber a
polynomial line. The actual degree modules F_n=ker N^(n+1) are
locally free of rank n+1.

For a collapsed mixed (2,1) fiber with L(m) nonzero, the whole
fiber and its induced action are
\[
A/\mathfrak mA=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\qquad
\bar N=(\lambda(G-G^2)+\rho G^2)\partial_c,
\quad\lambda\rho\ne0.
\]
The [complete mixed-module proof](mixed-degree-module-artin-image-pass104.md)
shows that im(F2 into A/mA) is contained in D. A function in F2
with a nonconstant reduced value on the double would have a nonzero
nilpotent derivative there. The general cyclic lemma103 would then
force the entire fiber to be a single double line, contradicting
the companion. A nonconstant value on the simple component would
produce four independent images of the rank-three module F2.

Those arguments first make both reduced values constant. A remaining
nonconstant nilpotent coefficient would give three independent residues
on the double, hence an actual basis of F2. The conic identity and
flat first-coefficient argument102, now applied to this arbitrary
function, contradict its actual weighted leading derivative. This
works with either first normal action. The full nonreduced residue,
not merely its reduction, is therefore independent of c.

There are exactly two possible residue spaces:
\[
\operatorname{im}F_2=\mathbb C\,1+\mathbb C\,G
\quad\text{or}\quad
\operatorname{im}F_2=\mathcal D.
\]
In the latter case the module fiber embeds, N maps F2 into mF2,
and the proof improves the base orders to N squared of F2 in m
squared, N squared of the centered normal F in m cubed, and
N to the fourth of the specified generator c in m cubed. This
does not require the first normal action to be nonzero. The
two-dimensional alternative does not inherit those stronger bounds.

This changes the next mathematical task. Looking for a degree-two
component parameter in this actual mixed sector is now ruled out by
the working proof. A cubic-generation argument must use a higher
degree function or genuinely different information. In particular,
G in F2 and c in F4 imply only Gc in F6; the rank of F4 cannot
be used with a proposed basis containing Gc without a new premise.
No mixed-fiber exclusion follows from this restriction alone.

## 2. The finite translation kernels are a transverse surface

At the collapsed whole-double or mixed fibers covered by103,
the projected original partial D has slice
r=z-q0 u squared/2 and induces an LND on every A/(mA)^k.
Write C_k for the kernel of that finite action. The new
[transverse-surface proof](adic-transverse-surface-pass104.md) identifies
these rings with
\[
C_k\simeq A/(r,(\mathfrak mA)^k).
\]
Thus they are finite neighborhoods of the single actual surface
Spec A/(r). This surface is smooth: Dr=1 forces the differential
of r to be nonzero at every point of r=0.

The original flat inclusion gives all the base-adic graded layers.
Multiplication by r is injective on those layers, so taking the
slice preserves their exact lengths. If d is the length of the
Artin fiber, then
\[
\dim_{\mathbb C} C_k=d\binom{k+1}{2},\qquad d=2\text{ or }3.
\]
The actual powers 1,G,...,G^(d-1) in the surface quotient give a
free basis over S/m^k by Nakayama and this length equality.
Compatible bases identify the completed kernel with a monogenic
finite free algebra of degree d over the completed base.

The base embedding must be specified. In the invariant ring C_k,
an element s of S acts through its finite slice projection P_k(s),
not necessarily through its original value in A/(mA)^k. With this
corrected embedding, smoothness gives formal coordinates in which
the double part is the simple ramified cover
\[
\mathbb C[[\Delta,t]]\longrightarrow\mathbb C[[Y,t]],
\qquad\Delta\longmapsto Y^2.
\]
The mixed case adds a second factor equal to the base itself.
The factorization uses the simple root of the degree-three
polynomial and formal lifting. The regular-completion and
formal-parameter facts used here are standard, not proposed as
new structure theorems.[^formal]

An exact intrinsic control shows why the embedding qualification
matters. In C[x,y,r], let f=H(y)-x^e r, with H=y squared or
y squared times (y-1), and let D=partial r. Then (x,f)=(x,H),
so all finite translation kernels are explicit. Nevertheless
P_k(f)=H(y), and f-P_k(f)=-x^e r is nonzero whenever k>e.
Even a genuine global translation on a polynomial threefold
need not fix the original chosen base at higher orders.

Consequently the completed action still gives a restricted-series
ring, not an ordinary polynomial ring over its completed kernel.
The coefficients may tend to zero while their r-degrees grow
without bound. The formal transverse description does not
algebraize the action, identify the original base embedding,
or make A polynomial.

## 3. The local conic cannot supply a section over its base

In the distinct noncollapsed double sector,103 proves
\[
A\otimes_S S_{\mathfrak m}
\simeq R[U,V]/(V^2-2pU+\eta),\qquad R=S_{\mathfrak m}.
\]
Smoothness at every point of the double line requires
d eta minus 2t dp to be nonzero in the base cotangent space
for every complex t. A putative R-section sends U to a and
V to b. The relation forces b into the maximal ideal and
d eta=2a(m)dp, contradicting that requirement.

The [complete no-section proof](cyclic-conic-retraction-obstruction-pass104.md)
also rules out a section after completion or a local etale
base change. A relative polynomial stabilization over R is
impossible because its special fiber would retain a nonzero
nilpotent. None of this contradicts the given absolute cylinder
isomorphism A[u]=C^[4], which does not preserve the chosen base.

This is a precise reason the retraction theorem of Das and
Dutta cannot finish this local case. Their Theorem 3.9 retains
a retraction hypothesis; the alternative geometrically integral
height-one fiber criterion also fails here. Along every local
factor of p the conic has a nonsplit quadratic constant-field
extension, not a geometrically integral line.[^patching]
The paper was already in the research record. The new result
is the proved failure of those premises at this actual conic.

The specified eta is also not a candidate ambient coordinate.
Differentiating eta=2pU-V squared shows that eta has a critical
point at U=V=0 over m. In the higher-order branch, where p
belongs to m squared, every affine combination of p and eta
is critical along the double line. A different invariant
coordinate remains possible. The retained polynomial family
p=x^e already shows that absolute polynomiality does not remove
these obstructions to the specified quotient presentation.

## 4. A quartic-looking family does have a hidden quadratic parameter

This control belongs to the whole-double situation, not the mixed
sector where Section 1 excludes such a parameter. In A0=C[x,y,c], put
\[
f=y^2+xy^4+x^m c,\qquad
N=-x^m\partial_y+(2y+4xy^3)\partial_c,\qquad m\ge1.
\]
The [all-m Catalan proof](quadratic-catalan-hidden-parameter-pass104.md)
constructs the polynomial
\[
U=\frac{y^2-P_m(x,f)}{x^m},\qquad
P_m(x,f)=\sum_{j=0}^{m-1}(-1)^j C_jx^jf^{j+1},
\]
where C_j are Catalan integers. Polynomiality follows from
uniqueness of the solution of Z+xZ squared=f modulo x^m;
it is not assumed from the rational formula.

This U has NU=-2y, N squared U=2x^m and whole-fiber residue
-c. It gives A0=S[y,U] with an exact monic conic relation and
ker N cubed=S+Sy+SU. In contrast, the specified c has N-degree
four. Thus the apparent quartic term can hide a genuine quadratic
relative parameter. For m>=2 the triple (x,y,U) has nonconstant
Jacobian determinant and is not an ambient coordinate system.
The relative presentation keeps f and does not assert otherwise.

The family is already polynomial. It tests a proposed obstruction
and supplies an exact construction; it is not a realization of
the original four-coordinate E-frame or a general hidden-parameter
existence theorem.

## 5. Verification and next proof obligations

The [recorded verification](verification-pass104-working.json) passes
four suites with six methods: three new finite controls and three
retained dependency checks from102/103. The new controls cover
Catalan instances m=1,...,5, transverse quotient bases and lengths
through k=6, the corrected-base distinction, and finite ramified
parameter expansions. They do not prove the universal geometric
arguments. Those have separate written reconstructions by AI
reviewers, not human expert review or Lean certification.

~~~sh
/opt/anaconda3/bin/python -m unittest -v \
  research.quadratic_catalan_checks_pass104 \
  research.adic_transverse_surface_checks_pass104 \
  research.quadratic_degree_module_checks_pass102 \
  research.projected_derivation_thickening_checks_pass103
~~~

The next bounded mixed-fiber task is to determine the degree-three
module and its multiplication with F2, with the two residue-rank
alternatives kept separate. A cubic algebra presentation would
need an actual generating argument, not a rank count alone.
In the whole-double sector, a hidden-parameter construction must
still be transferred from intrinsic examples to the actual frame
if that route is pursued. The unrestricted entry problem and
the original global recognition step remain necessary for the
full cancellation goal.

No expert outreach, submission, public posting, novelty claim,
or new automation has been made. The full conjecture is unsolved.

## Sources

[^formal]: The Stacks Project Authors, [Lemma 10.160.10](https://stacks.math.columbia.edu/tag/0C0S),
    [Section 15.44](https://stacks.math.columbia.edu/tag/07NU), and
    [Section 10.153](https://stacks.math.columbia.edu/tag/04GE).
    The complete transverse proof specifies the statements used
    and separates them from its direct finite-module argument.

[^patching]: Prosenjit Das and Amartya K. Dutta,
    [*On codimension-one A1-fibration with retraction*](https://arxiv.org/pdf/1302.5223v1),
    arXiv:1302.5223v1, Theorem 3.9, Corollary 3.10 and Theorem 1.1.
    The complete conic note states the exact read scope and
    identifies the missing hypotheses without applying the theorem.
