# Cubic rank loss and the actual normalization boundary

The actual collapsed mixed quadratic sector with nonzero speed normal
has a further restriction: the rank-four degree-three module has
whole-fiber image of dimension at most three, and every degree-three
function is constant on both reduced components. The argument uses
an actual normalization boundary and a polynomial slice over a
one-dimensional local base. A dimension count on nilpotent coefficients
alone would not prove it.

This is a conditional result inside the supplied three-good-coordinate
frame. It neither excludes the mixed fiber nor reduces an arbitrary
sliced action to that frame. The working complex-threefold cancellation
question remains unsolved, and Professor Luo has not confirmed that
this is the intended interpretation of the original email.

## 1. The setting and the precise new conclusion

The actual data include a smooth affine threefold ring A with
A[u] a polynomial ring in four original coordinates, a sliced derivation
E, and its associated primitive locally nilpotent derivation N on A.
The invariant ring is S=C[s1,s2], the inclusion S into A is faithfully
flat, and the generic fiber is K[v], where K is the fraction field of S.
The specified relative generators have N-degrees at most two, two and
four. These requirements are not consequences of a formal local model.

At the closed base point m under consideration, the whole fiber is
D[c], with D=C[G]/(G²(G−1)). It contains a double line and a disjoint
simple line. Put epsilon=G−G² and e1=G². The actual fiber derivation is
(lambda epsilon+rho e1) partial_c, with both constants nonzero.
The speed normal L(m) is assumed nonzero throughout the mixed claims.

Write Fj=ker N^(j+1), R=S_m and Wj for the image of Fj in the whole
fiber. The modules (Fj)_R are free of rank j+1. The previous result104
put W2 inside the constant Artin algebra D, with dimension two or three.
The [new rank-defect proof](mixed-cubic-rank-defect-pass105.md) gives
dim W3 at most three and zero reduced slopes for every element of F3.
In particular, if W2=D, then W3=D as well. The alternative W2 of
dimension two can still leave an additional nilpotent coefficient
direction in W3; no argument silently removes that possibility.

Here “degree” means degree under N, equivalently generic v-degree.
It does not mean total degree in a displayed ambient coordinate system.
“Whole fiber” includes nilpotents. The conclusion is stronger than a
statement about values at complex points, but weaker than identifying
the whole algebra or proving that the fiber cannot occur.

## 2. Why the cubic module alone was insufficient

The [degree-three image proof](mixed-third-degree-image-pass105.md)
first writes every F3 residue as
(a1 c+a0+epsilon beta(c), b1 c+b0) on the two factors. This follows
because NU lies in F2 and has constant Artin residue.

The any-function strict weighted inequality97 says that an actual
function nonconstant on both components has generic degree strictly
greater than the sum of its component degrees weighted by two and one.
Both nonzero slopes for an F3 element would require 3<deg U<=3.
Consequently all F3 reduced slope vectors lie in one common coordinate
axis, or vanish. If W2 has dimension two, either nonzero slope would
produce a third independent F2 residue, so all slopes already vanish.

This also excludes any element U, of any degree, for which A_R is
finite over R[U]. Such finiteness would force U nonconstant on both
lines. Localizing the projection at the generic parameter over m gives
a finite algebra over a regular local surface. Its actual regular local
targets make it flat, hence free. Its generic and special ranks would
then agree, contradicting strict97. This argument does not confuse a
finite map with a map having finite fibers.

Weighted differentiation bounds the possible nilpotent coefficient
beta. Importantly, the elementary full-rank, zero-slope argument allows
the four-dimensional space D+C epsilon c. Epsilon is independent of
1 and G. Discarding that fourth direction would be an incorrect proof
of rank loss. The next two sections supply the additional argument
that actually excludes full rank in this setting.

## 3. The selected c-projection has a concrete boundary

The [normalization proof](mixed-c-parameter-normalization-boundary-pass105.md)
uses T=(S[c])_(mS[c]) and B=A tensor_(S[c]) T. The ring T is regular
local of dimension two, with residue field C(c). The generic degree
is four, while the whole closed fiber of B has length three.

The proof first checks quasi-finiteness on every stratum, not only on
the closed fiber. Generic integrality provides finiteness after
inverting a nonzero base element. Each remaining height-one prime is
an invariant base prime p. Since Nc is nonzero on the whole closed
fiber, it is nonzero modulo p as well. On the whole generic p-divisor,
the actual derivation is a nonzero translation on k'_p[w]. Thus c is
nonconstant in w and its projection has finite fiber.

The integral closure C of T in Frac A is finite. The precise
normalization form of Zariski's Main Theorem identifies Spec B with
a dense affine open in Spec C. Normality in dimension two gives
Cohen--Macaulayness; the local dimension equality then gives flatness
over T. Therefore C is free of rank four. These are applications of
the cited theorems with their hypotheses checked, not new versions of
those theorems.[^normalization]

The finite closed fiber of C consists of the retained double factor,
the retained simple factor and exactly one omitted reduced point P.
The completed local algebra at that omitted point is canonically
the completion of T. This is a statement about a completed direct
factor of the finite algebra. The uncompleted local ring C_P need
not itself be finite as a T-module.

The affine open has a nonempty divisorial boundary. Every boundary
divisor lies over an invariant prime p, and all its closed points
are the single omitted point P. For such a divisor Q, the finite
module C/Q has one-dimensional closed fiber. Its unit is consequently
a module generator, so C/Q=T/pT. The completed local identification
then gives ramification index one and uniqueness of the boundary
divisor over p.

The resulting complete valuation count is 4=n_p+b_p, where n_p is
the degree of the retained generic p-divisor over k_p(c), and b_p is
one or zero according to whether a boundary divisor occurs. Since
n_p=N_p deg_w(c) and the actual constant-field degree N_p is one or
two, some boundary prime has N_p=1 and deg_w(c)=3. A prime with N_p=2
has no boundary divisor and instead deg_w(c)=2. The omitted closed
point can still lie in the closure of that retained degree-two
divisor. The statement does not remove that point from its closure.

This locates the missing projection degree more precisely than the
earlier rank-defect observation. It does not say that every special
fiber rank loss in algebraic geometry has this particular boundary.

## 4. The boundary excludes full cubic rank

At a prime with N_p=1, put V=S_(p). The whole divisor ring is k_p[w]
and the reduced derivation has kernel k_p. Choose an actual local
slice t in A_V, normalized so Nt=p^e. When e is positive, t has
constant residue. Lift that constant from V, subtract it and divide
by p in A_V. The derivative exponent drops by one. After finitely
many steps the resulting element v satisfies Nv=1.

Thus A_V=V[v], using the ordinary polynomial slice expansion and
the exact localized kernel V. In particular, the image of N^4 on
F4 localized at p is all of V, since N^4(v^4/24)=1. This does not
assume that taking a kernel commutes with reduction modulo p. It
constructs the needed slice inside the localized polynomial algebra.

Now suppose W3 had dimension four. Its slope-axis restriction makes
the residue of c independent of W3: c has nonzero slopes on both
components. The five independent residues give
F4_R=F3_R direct-sum Rc by the rank-five module and Nakayama.
Hence the fourth-derivative image ideal would be principal, generated
by N^4c.

At the boundary prime from Section 3, however, c has degree three
on the whole divisor, so N^4c belongs to p. The principal image ideal
would remain a proper ideal after localizing at p, contradicting the
explicit slice calculation. Therefore dim W3<=3.

Finally, W2 of dimension two already forces zero F3 slopes. If W2=D,
then W2 is contained in W3 and both have dimension three, so W3=D.
This proves the asserted constancy on both reduced components in
both cases. It is the combination of the boundary and slice arguments,
not an incorrectly shortened nilpotent dimension count, that closes
the full-rank alternative.

## 5. Intrinsic controls and the transverse interpretation

The [mixed quartic family](mixed-quartic-hidden-cubic-parameter-pass105.md)
has f=y²(y−1)+xy⁴+x^m c in C[x,y,c] for every m>=1. Finite monic
preparation produces an actual polynomial U of degree three and
the exact algebra A=S[y,U], with F3=S+Sy+Sy²+SU. Its residue varies
on both reduced mixed components. This is a positive construction
for that family, with full polynomial saturation proved in writing.

The distinction from the actual frame is now explicit. Its invariant
x-divisor has exact relative constant field C(y) over C(y²(y−1)),
of degree three. The actual quadratic frame permits degree at most
two. Thus this specified invariant inclusion cannot realize the
frame, regardless of its smooth polynomial ambient threefold.
It is neither a cancellation counterexample nor a construction
that bypasses the new rank-defect theorem.

A simpler control A=C[x,z,v], S=C[x,z], N=partial_v and selected
c=xv⁴+v³−v² shows that generic degree four can specialize to degree
three along a degree-one constant-field divisor. There is no general
parity prohibition from polynomiality and local nilpotence alone.
This control has a reduced affine-line closed fiber, not the mixed
fiber or an original E-frame. Its rescaling w=xv satisfies the monic
equation w⁴+w³−xw²−cx³=0; no normality of that monic model is claimed.

Separately, the [shifted transverse-surface proof](quadratic-transverse-branch-motion-pass105.md)
identifies the branch tangent on each actual slice r=t as the line
df−a(t+q0 eta2²/2)dx, with a(c)=a0+a1c. First normal action is nonzero
exactly when these tangents vary. The retained intrinsic family
f=y²−2x^e r shows why transverse branch curves need not lie in one
fixed quotient exceptional curve. Constant tangents do not even
make their higher-order branch germs constant. This geometric
interpretation supplies no global coordinate recognition.

## 6. Verification and sources

The [canonical capture](verification-pass105-working.json) records
five suites and seven passing methods. Three methods are new: the
mixed quartic preparation for m=1 through5, the symbolic weighted
fourth/fifth derivative formulas, and the intrinsic odd-specialization
control. Four methods repeat retained finite dependency checks.
The run took 2.011593583 wall seconds and 1.695 unittest seconds.
Input hashes were unchanged before and after execution.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.mixed_quartic_cubic_checks_pass105 research.mixed_third_degree_checks_pass105 research.quadratic_catalan_checks_pass104 research.adic_transverse_surface_checks_pass104 research.quadratic_degree_module_checks_pass102
~~~

The finite checks do not verify the universal normalization argument,
slice-lifting theorem, whole-module saturation or cancellation. Those
are written arguments with separate AI reconstructions. There is no
human expert approval, formal proof-assistant certificate or novelty
clearance. The historical full75 regression is not a new run here.

The weak relative Noether normalization theorem was also checked:
it supplies a quasi-finite relative parameter map, not a finite one.
It cannot reverse the all-degree no-finiteness conclusion in Section 2.
For the selected c, the explicit all-strata proof above is stronger
than merely invoking existence of an unspecified parameter.[^weak]

[^normalization]: The Stacks Project Authors, [Theorem 29.57.1, tag 03GT](https://stacks.math.columbia.edu/tag/03GT)
    and [Theorem 10.123.12, tag 00Q9](https://stacks.math.columbia.edu/tag/00Q9);
    [Lemma 10.161.8, tag 032L](https://stacks.math.columbia.edu/tag/032L);
    [Lemma 28.12.7, tag 0B3D](https://stacks.math.columbia.edu/tag/0B3D);
    [Lemma 10.128.1, tag 00R4](https://stacks.math.columbia.edu/tag/00R4);
    [Section 31.17, tag 0BCQ](https://stacks.math.columbia.edu/tag/0BCQ).
    The displayed statements and proofs were freshly read. The deeper
    conductor and foundational dependencies were not freshly rebuilt.

[^weak]: The Stacks Project Authors, [Lemma 37.31.3, tag 0GTG](https://stacks.math.columbia.edu/tag/0GTG)
    and its parameter-power lemma [37.31.2, tag 0GTF](https://stacks.math.columbia.edu/tag/0GTF).
    Their displayed statements and proofs were read to distinguish
    quasi-finiteness from finite-module descent. No new result is
    attributed to this source audit.

## 7. Remaining proof frontier

The lower-rank cubic alternatives still need analysis. In the
rank-three F2 branch, every F3 residue is now Artin-valued, but c in
degree four still generates a nonconstant fiber parameter. In the
rank-two F2 branch, a third nilpotent residue direction remains
possible subject to the weighted bounds. Neither case gives a finite
parameter presentation, since that route is excluded at every degree.

The next bounded task is to analyze the derivative image ideals and
multiplication in these lower-rank cases using the actual boundary
prime and its polynomial local slice. Any proposed contradiction must
retain the distinction between the degree-one boundary curve and the
degree-two constant-cover curve, and between a missing divisor and a
missing closed point. The whole-double, L(m)=0, global recognition and
arbitrary-frame entry gaps remain separate and unresolved.

All frozen files through104 are preserved. The exact current proof
versions, review coverage, tests and outstanding limits belong in
[checkpoint105](checkpoint-pass105-working.json). No external contact,
public posting, submission or new automation is part of this pass.
