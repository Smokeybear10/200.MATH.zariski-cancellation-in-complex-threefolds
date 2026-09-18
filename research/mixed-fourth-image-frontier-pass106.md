# The fourth derivative image and the remaining point defect

The actual mixed-fiber argument now forces a nonprincipal fourth
derivative-image ideal. It needs two or three generators. In the
branch with a full second-degree Artin image, the third image is
principal, the fourth image has exactly two generators, and the
two are linked by a proper complete-intersection ideal at the
closed base point. This strengthens the restrictions on a possible
mixed fiber without excluding it.

The working question remains complex-threefold cancellation:
A[u] isomorphic to a polynomial ring in four variables should
imply A isomorphic to a polynomial ring in three variables.
The full question is unsolved here. These results assume the
supplied original three-good-coordinate quadratic frame, a
collapsed mixed fiber and nonzero speed normal. No reduction of
an arbitrary sliced action to that setting has been established.
Professor Luo has not confirmed this interpretation of the email.

## 1. The actual modules and why this is a new obstruction

Let R=S_m be the local ring of the invariant plane at the chosen
closed point, and n its maximal ideal. Let N be the actual
primitive locally nilpotent derivation. Set M_j=ker N^(j+1)
after localizing the base, and I_j=N^j(M_j), an ideal of R.
Each M_j is free of rank j+1. Its image W_j in the whole
algebra fiber need not have that dimension.

The retained mixed fiber is D[c], with
D=C[G]/(G²(G−1)). It is the disjoint union of a doubled line
and a simple line, including the nilpotent structure. The
derivation on it is (lambda epsilon+rho e1) partial_c, where
epsilon=G−G², e1=G² and both constants are nonzero. The
previous result gives W_2 contained in D, dim W_2 equal to
two or three, dim W_3 at most three, and constant reduced
values for every third-degree element.

Freeness of the two adjacent degree modules gives an exact
sequence from M_3 to M_4 to I_4. It does not make I_4 free.
The [new nonprincipality proof](mixed-fourth-image-nonprincipal-pass106.md)
shows that I_4 cannot be principal in this actual setting.
That identifies a genuine obstruction to splitting the degree
filtration, instead of assuming that a free quotient exists.

## 2. Every admissible fourth-degree parameter has a boundary

An element U of M_4 is called admissible when it is nonconstant
on both reduced component lines. The actual strict weighted
degree inequality97 forces its generic degree to be four and
both component degrees to be one. This applies to localized
elements after clearing an invariant denominator outside m.

The nilpotent term does not spoil the parameter change. On the
double factor, write Ubar=a c+b+epsilon beta(c), with a nonzero.
Putting t=(Ubar−b)/a gives the exact inverse
c=t−epsilon beta(t)/a. Thus the entire closed fiber is free
of rank three over C[Ubar], not just generically finite after
discarding nilpotents.

The [generalized boundary proof](mixed-admissible-quartic-boundary-pass106.md)
checks quasi-finiteness on every stratum of the local projection
base T_U. Its finite normal closure is free of rank four, and
the actual affine open omits exactly one reduced closed point.
The omitted completed local factor is the completed base itself.
Its nonempty boundary has divisors over invariant base curves.
Some such curve has constant-field degree one, and U specializes
there to a polynomial of degree three.

This uses the precise normalization form of Zariski's Main
Theorem and finite integral closure, followed by normal-surface
Cohen--Macaulayness and miracle flatness.[^normalization]
The affine-open complement theorem supplies divisorial purity.[^boundary]
No quasi-finite map is silently promoted to a finite map.

There is a uniform additional consequence. On each invariant
curve whose constant-field extension has degree two, every
element of M_4 specializes to degree at most two. It follows
that N³(M_4) is contained in the corresponding prime of the
actual algebra. In particular the invariant ideals I_3 and
I_4 are contained in that base prime.

## 3. Why a principal fourth image is impossible

Suppose I_4=(g). Choose U with N⁴U=g and write N⁴c=gh.
For a general complex number alpha, U+alpha c is admissible
and 1+alpha h is a unit of R. Thus the fourth derivative of
this admissible parameter still generates I_4.

Its own normalization boundary supplies an invariant divisor p
with constant-field degree one and parameter degree three.
The fourth derivative therefore vanishes modulo p. But over
the base DVR at p the actual derivation has a unit slice:
subtract and divide a local slice by p until its derivative
is a unit. The residue constants lift precisely because the
constant-field extension here has degree one. The fourth
derivative of the fourth power of that slice, divided by 24,
is one. The localized ideal I_4 is both proper and the unit
ideal, a contradiction.

The exact module sequence then bounds the minimal generator
count by two or three. If dim W_3=3 it is exactly two.
Removing the gcd of the generators writes I_4=dJ with J
proper and n-primary. All divisor factors of d lie on the
degree-two constant-cover curves. The residual ideal J
disappears upon every height-one localization, but not at
the closed point. This is why divisorial information alone
does not finish the argument.

## 4. The full Artin branch has stronger compatibility equations

Assume W_2=D. Three independent whole-fiber residues split
M_2 off both M_3 and M_4. The
[two-generator proof](mixed-full-artin-two-generator-pass106.md)
chooses complements M_3=M_2+Rt and M_4=M_2+Ru+Rv,
with direct sums in both cases, and writes
t=a u+b v+H for H in M_2. Torsion freeness and the new
nonprincipality make a,b coprime nonunits. Hence J=(a,b)
is a proper n-primary complete-intersection ideal.

The exact derivative relations are
Nu=theta b t+P and Nv=−theta a t+Q, with P,Q in M_2
and theta nonzero in R. For g=N³t they give
I_3=(g), I_4=theta gJ and g=aN²P+bN²Q in JI_2.
The coefficient H is retained in the proof and disappears
only under the correct third iterate. Theta is not assumed
to be a unit.

Since the earlier full-Artin argument gives I_2 contained in
n², the new relation gives I_3 contained in n³ and I_4
contained in n⁴. In particular N⁴c has base order at least
four. The divisor support of g is exactly the degree-two
constant-cover locus through the selected point, without
any determination of its multiplicities.

Multiplication also imposes I_2² contained in theta gJ and
I_1 contained in theta J, by the fourfold Leibniz formula.
These inequalities are compatible with a nonzero residual
ideal. Neither a fourth-order zero nor a two-generator
description is itself a contradiction.

## 5. An explicit control prevents a module-only conclusion

The [intrinsic algebra control](fourth-image-module-controls-pass106.md)
takes R=C[a,b] localized at (a,b), z transcendental, and
B=R[z,z⁴/a,(z³−z⁴)/b] inside K[z]. The locally nilpotent
derivation N=ab partial_z preserves B. Its exact degree
modules through four are free, but its fourth image is
24a³b³(a,b), which is nonprincipal. The third-degree values
on the reduced closed fiber are all constant. The matrix
and multiplication constraints in Section 4 also hold.

The whole closed fiber of this control is a fat plane,
C[Z,U,V]/(Z³), not the actual mixed curve. The derivation
vanishes on that whole fiber, and the inclusion from R is
not flat. These exact failures prevent using it as either
an actual-frame example or a counterexample to cancellation.
It does show why free modules and the displayed low-degree
product identities cannot supply the missing contradiction
without additional actual geometry.
The presentation proof explicitly uses the standard fact that
a regular-sequence quotient of a regular ring is Cohen--Macaulay
and has no embedded associated primes.[^control]

## 6. Verification and the next unresolved step

The detailed proofs distinguish the actual ring, its generic
divisors, the whole nonreduced closed fiber, and reductions of
the finite degree modules. Separate AI reconstructions check
the written arguments. They are not human expert review,
formal verification in Lean, or an assessment of novelty.
Computational checks, where recorded, test only their stated
finite algebraic controls and cannot certify the geometric
theorems or cancellation.

The [recorded targeted run](verification-pass106-working.json)
passes three suites and four methods: two new finite controls,
one retained intrinsic quartic-recovery control, and one retained
conic-matrix control. The new methods check the ring's displayed
rational identities, finite products and special-fiber reductions,
plus five dual-number parameter inverses. They do not prove the
arbitrary-element module lattice or the universal geometry.
The exact inputs, complete output and hashes are retained in the
capture, and the [checkpoint106](checkpoint-pass106-working.json)
records the proof versions and review scope.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.fourth_image_module_checks_pass106 research.mixed_quartic_cubic_checks_pass105 research.quadratic_degree_module_checks_pass102
~~~

The next substantive task is to determine whether the actual
multiplication and the degree-two divisor filtrations permit
I_4=theta gJ with g in JI_2. A precise route is to determine
the height-one valuations of I_1 through I_4 on the actual
degree-two constant extensions, then combine them with these
closed-point relations. No valuation formula has yet been
proved in this pass. The rank-two W_2 branch also remains.

The whole-double case, zero speed normal, global recognition
and the entry problem for arbitrary sliced actions are still
open. No claim of a breakthrough, submission readiness or
publication-level verification follows from these lemmas.

## Sources

The links above identify the exact private mathematical proofs.
Their retained hypotheses are recorded in the105 checkpoint
and the actual-frame papers within this project. The primary
external results used here are the following standard theorems,
consulted September 14, 2026.

[^normalization]: The Stacks Project, [finite integral closure, Lemma 10.161.8](https://stacks.math.columbia.edu/tag/032L); [normalization form of Zariski's Main Theorem, Theorem 29.57.1](https://stacks.math.columbia.edu/tag/03GT), with its [algebraic theorem 10.123.12](https://stacks.math.columbia.edu/tag/00Q9); [normal surfaces are Cohen--Macaulay, Lemma 28.12.7](https://stacks.math.columbia.edu/tag/0B3D); [miracle flatness, Lemma 10.128.1](https://stacks.math.columbia.edu/tag/00R4).
[^boundary]: The Stacks Project, [Complements of affine opens, Section 31.17, Lemmas 31.17.4--5](https://stacks.math.columbia.edu/tag/0BCQ). The separate direct regular-sequence argument agrees with [Lemma 10.104.2](https://stacks.math.columbia.edu/tag/02JN).
[^control]: The Stacks Project, [Cohen--Macaulay modules, Section 10.103, especially Lemmas 10.103.5 and 10.103.7](https://stacks.math.columbia.edu/tag/00N2). The complete displayed section was checked; its deeper depth-theory dependencies were not rebuilt.
