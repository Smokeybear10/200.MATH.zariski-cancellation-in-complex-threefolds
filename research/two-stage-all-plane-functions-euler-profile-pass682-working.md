# An exact fiber profile excludes every function in the selected plane

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
For the test cylinder from671, no nonconstant element of the entire
subalgebra H=C[x,b] can be a global coordinate or a slice of any locally
nilpotent derivation. This is an arbitrary-polynomial result, not a degree
bound or a restriction to coordinate changes of H.

An explicit retract plane inside ordinary affine four-space has the same
no-coordinate and no-slice property. Thus the exclusion does not prove
nonpolynomiality of the test cylinder or solve cancellation.

## 1. The exact whole presentation and topological convention

Use681's presentation

    B=C[a,b,x,K,S]/(a²S+a(1+x+x²K)+x⁴+b³),
    H=C[x,b], P=x⁴+b³.                                  (1)

It gives, without any generic-fiber assumption,

    B_a=H[a,a^(-1),K],
    B/(a)=(H/(P))[K,S].                                 (2)

The first isomorphism eliminates S with denominator a². The second
simply sets a=0 in the defining relation. In particular H embeds in B.
All statements below use these exact whole strata.

For a complex algebraic variety Z, write chi_c(Z) for its compactly
supported Euler characteristic with rational coefficients. It is additive
under a closed subset and its open complement, and multiplicative for
products. These facts follow from the compact-support cohomology exact
sequence and the Kunneth formula. Also

    chi_c(A^n)=1, chi_c(C*)=0.                           (3)

Euler characteristic concerns the underlying complex topological space.
Nilpotent scheme structure contributes no extra points or multiplicity.
An isomorphism with affine three-space would therefore force chi_c=1,
whether or not we already know a proposed fiber is smooth or reduced.

## 2. The complete scalar-fiber profile for every f in H

Let f be ANY polynomial in H and put

    g(t)=f(t³,-t⁴),
    Z_lambda=V_Spec(B)(f-lambda).                        (4)

THEOREM. For every complex scalar lambda,

    chi_c(Z_lambda)=chi_c({t in C : g(t)=lambda}).        (5)

In particular, if g is nonconstant, this is the number of DISTINCT
roots of g(t)-lambda. If g is constant gamma, it is 1 at lambda=gamma
and 0 at every other lambda.

Proof. The open and closed pieces of Z_lambda from (2) are exactly

    Z_lambda intersect D(a)
      = V_A2(f-lambda) times C* times A1;
    Z_lambda intersect V(a)
      = V_A2(P,f-lambda) times A2.                       (6)

The open piece has Euler characteristic zero, even when the plane fiber
is reducible, singular, or empty. The closed piece contributes precisely
chi_c(V_A2(P,f-lambda)).

The cusp P=0 is parametrized by

    nu:C -> V(P), t -> (t³,-t⁴).                        (7)

This is a bijection on complex points. Off its origin the inverse is
t=-b/x; if x=0 on the cusp then b=0 and t=0. Its coordinate extension
is finite, since t is integral over C[t³,t⁴], and it is the normalization.
Equivalently, it is a proper continuous bijection, hence a homeomorphism.
Restriction identifies the topological fiber of f on the cusp with the
right side of (5). This proves (5), including repeated scheme roots.

One can avoid the homeomorphism fact in the Euler calculation itself.
For nonconstant g, both fibers are finite sets in bijection. For constant
g=gamma, the cusp fiber is empty off gamma and is the entire cusp at
gamma. The cusp is the disjoint union of its origin and a copy of C*,
so has Euler characteristic 1. This gives all cases directly.

The polynomial g lies in C[t³,t⁴]. Every nonconstant such polynomial
has degree at least 3; cancellation among terms cannot create a power
of t absent from that subalgebra. Consequently the GENERIC value in (5)
is either 0 or an integer d>=3, never 1. In the nonconstant case the
exceptional scalars are among the finitely many critical values of g.

## 3. Global coordinates and all LND slices in H are excluded

If f were a global coordinate on B, every scalar fiber would be affine
three-space and have Euler characteristic 1. Equation (5) contradicts
this for every nonconstant f in H. This includes arbitrary nonlinear
polynomials in x,b, not just x, b, linear combinations, or coordinates
obtained by an automorphism of H.

The same stratification without f gives

    chi_c(Spec B)=0+chi_c(V(P) times A2)=1.              (8)

Suppose a global locally nilpotent derivation delta had delta(f)=1.
The slice theorem gives B=(ker delta)[f]. Thus Spec B is a product of
Spec(ker delta) with A1, and every scalar fiber of f is Spec(ker delta).
By (8) and multiplicativity each fiber must have Euler characteristic1,
again contradicting the generic profile (5). The kernel here is finitely
generated, since it is isomorphic to B/(f), so the Euler characteristic
is defined in the stated category.

Therefore no nonconstant element of H is a slice of ANY global LND.
Equivalently, for f in H and any LND delta of B, delta(f) can be a
constant only if that constant is zero: rescale delta otherwise.
This does NOT assert that every LND kills H, or that every LND preserves
H. Values delta(f) that are nonconstant remain entirely possible.

For exact examples, f=x and f=b give generic Euler characteristics 3
and 4, recovering the individual exclusions of681. For f=x+b,
g=t³-t⁴, the value is 4 except at lambda=0 and lambda=27/256, where
the distinct-root counts are respectively 2 and 3. For f=P, g=0, the
value is 0 at every nonzero lambda and 1 at zero. A fiber having value1
is NOT asserted to be affine three-space.

## 4. An actual polynomial ambient ring has a retract with the same exclusion

Let B'=C[X,Y,Z,T], an ordinary polynomial four-ring, and put

    p=X+X²Y, q=Z+Z²T, H'=C[p,q].                        (9)

The subalgebra is a polynomial plane, since specializing Y=T=0 turns
p,q into the independent variables X,Z. It is a retract of B':

    rho(X)=p, rho(Y)=0, rho(Z)=q, rho(T)=0.              (10)

These formulas fix p,q, so rho²=rho and its image is exactly H'.

The map (p,q):A4 -> A2 is smooth everywhere. Its two Jacobian rows
have disjoint variable supports. The first has entries 1+2XY and X²,
which cannot vanish together, and the second has entries 1+2ZT and Z²,
with the same property. Thus the Jacobian has rank2 at every point.
The section (p,q) -> (p,0,q,0) also proves surjectivity.

For EVERY polynomial F(p,q) and scalar lambda, write
W_lambda=V_A4(F(p,q)-lambda). There is an exact Euler profile

    chi_c(W_lambda)=1 if lambda=F(0,0), and 0 otherwise. (11)

Here is the entire stratification proof. On XZ!=0, the coordinate
change from X,Y,Z,T to X,p,Z,q has the regular inverse

    Y=(p-X)/X², T=(q-Z)/Z².

Hence this stratum of W_lambda is V_A2(F-lambda) times (C*)²,
with Euler characteristic0. On X=0,Z!=0 it is

    V_A1(F(0,q)-lambda) times A1 times C*,

where Y is free and T=(q-Z)/Z². It also contributes0, including
when F(0,q)-lambda vanishes identically. On X!=0,Z=0 the analogous
stratum is V_A1(F(p,0)-lambda) times C* times A1, again contributing0.
Finally X=Z=0 leaves p=q=0 with Y,T free. This is A2 if
lambda=F(0,0), and empty otherwise. Additivity proves (11).

Thus no nonconstant element of H' is a B'-coordinate. Since chi_c(A4)=1,
the slice argument of Section3 also shows that no such element is a
slice of any LND of B'. This conclusion does not use threefold
cancellation to identify the kernel of a hypothetical sliced LND.

The scope distinction is essential. The retract H' is NOT factorially
closed in B': p=X(1+XY) belongs to H', but X does not. Indeed if
X=Q(p,q), setting Y=T=0 forces Q(U,V)=U, contrary to X=p in B'.
An actual sliced kernel A in A[u] is factorially closed, and has
dimension3 in the main problem. This dimension2 retract is not a
counterexample satisfying those stronger hypotheses. Its retraction has
kernel (Y,T), not a principal kernel: algebraic independence of p,q
makes rho(F)=0 equivalent to F(X,0,Z,0)=0.

Equation (11) does refute the inference that a polynomial-plane retract
containing no ambient coordinate or LND slice makes its ambient ring
nonpolynomial, even if its quotient map is smooth and has a section.
That proposed global shortcut is unavailable.

The individual retract generator X+X²Y is a published example, explicitly
given by Shpilrain--Yu on p.477 of *Polynomial Retracts and the Jacobian
Conjecture*. This construction takes the product of two such known
examples; the complete all-F Euler profile is proved above rather than
ascribed to their paper. A bounded search did not locate that exact
smooth-product formulation, which is not novelty clearance.
[Primary published author copy, introduction](https://shpilrain.ccny.cuny.edu/retracts.pdf).

## 5. Evidence and remaining scope

Root derived the whole all-H Euler profile from the two strata; Geometry
and Jet independently reconstructed the argument including every special
fiber and the distinction between roots and scheme multiplicities.
Jet supplied the polynomial-ambient safeguard and checked its four strata;
root independently reconstructed its inverse maps and slice consequence.

Fresh unsaved rootf02c4c verifies the entire a-chart elimination, the
H-retraction a=1,K=0,S=-(1+x+P), the cusp parametrization and inverse,
the H' retraction, both inverse orders on the XZ-invertible stratum,
and the exact special values for f=x+b. Jet's independent freshaba2a3
checks the stratum maps and related identities. These are supplementary
algebraic checks, not numerical evidence for the all-polynomial theorem.

The complete224-line saved source was held at SHA256
65c64de17ba562422f5e53c1e353fea16a60255908035ea5a04495430eb35651.
General read every line in36ce6d/d19661 and confirmed hash266356;
Geometry read through EOF in4af03c and confirmed a417a4;
Jet read through EOF ind96fce and confirmed71a416. All three complete
reviews returned CLEAN before this provenance-only update. No mathematical
correction was requested. Root also reread the entire held source inb819e2.
Fresh rootf73ddb and Jet819a5e independently verified an exact unit
certificate for the full Jacobian-minor ideal of the smooth safeguard.
Jet additionally checked both exceptional root counts. An earlier scratch
assertion compared equal factorizations structurally; exact subtraction
resolved it. This was not a counterexample to any identity in the proof.

No novelty clearance has been obtained. The zero-Euler open-stratum mechanism already occurs in
research/cubic-linear-variable-pass.md Section1, equation(5). The divisor
localization used in681 occurs in research/intrinsic-rank-pass34.md
Section2.2. These underlying methods are not presented as new. Root
read Shpilrain--Yu's exact example and complete Theorem1.1 proof in
turn6157view0; General independently read the published source in
turn6156view0. That theorem is not needed for the explicit product proof.
No saved checker was executed, imported, compiled or edited. These reviews
are internal AI checks. No human expert review or formal
proof-assistant verification has been obtained.

The original target remains A[u]=C^[4] implies A=C^[3]. This note closes
the entire coordinate-or-slice search confined to H for one test cylinder,
while its polynomial control proves that this alone cannot recognize
the cylinder. The next global argument must use structure beyond that
selected plane, and beyond the existence of a retraction alone.
