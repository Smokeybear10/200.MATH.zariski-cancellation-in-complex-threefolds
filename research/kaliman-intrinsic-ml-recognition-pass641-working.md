# A supplied commuting pair reduces recognition to intrinsic ML

Private source-dependent working proof, September 18, 2026. With
an actual cylinder A[u]=C^[4] and a supplied independent commuting
pair of LNDs, Kaliman's published theorem gives an exact dichotomy.
Either A=C[f,t,s] for the pair's common invariant f, or ML(A)=C[f]
and every intrinsic LND fixes every critical point of f.

This is an application of a published recognition and invariant
theorem, not a new proof of that theorem. Neither existence of the
supplied pair nor descent of ML-triviality from A[u] to A is proved.
General cancellation remains UNSOLVED, and novelty is UNKNOWN.

## 1. The actual input and open cylinder

Let A be an affine complex domain with a supplied isomorphism
A[u] to C^[4]. Put X=Spec(A). Suppose P,Q are nonzero commuting
LNDs of A, independent over Frac(A). The retained intrinsic plane
quotient theorem and simultaneous kernel argument give

    ker P=C[f,g],       ker Q=C[f,h],
    ker P intersect ker Q=C[f],
    P(h)=p(f),         Q(g)=q(f),
    p,q nonzero polynomials.                         (1)

The exact simultaneous argument is in
[635, Section 1](fiberwise-free-direction-gluing-pass635-working.md):
Q restricts nontrivially to the actual plane ker P, and Rentschler
supplies f,g. Applying the same theorem to P on ker Q gives the
same common generator up to an affine-linear change. Independence
excludes a zero restriction. Alternatively, (1) can be retained
explicitly as input. Neither action need be primitive for this note.

The cylinder makes X smooth and contractible, A factorial, and
A*=C*. Contractibility follows from the homotopy equivalence
X x C to X and the given isomorphism X x C to C^4. In particular

    H_3(X;Z)=0,          e(X)=1.                     (2)

Let Sigma be the finite set of roots of p and U=A1\Sigma. The
local slice h/p for P gives an INCLUDED algebra equality

    A_p=C[f,p^(-1),g,h],
    Z:=Spec(A_p)=U x A2,                            (3)

with f equal to the projection to U. This is an actual open
affine-plane cylinder, not just a rational parametrization or an
affine-plane form over C(f). If p is a unit, (3) already gives the
desired coordinate presentation and Sigma is empty.

Both LND kernels are factorially closed in A, so C[f] is too.
Every f-c is therefore irreducible in the UFD A and hence prime.
It is a nonunit because A*=C*. Thus each fiber

    X_c=Spec(A/(f-c))                               (4)

is a nonempty integral surface. The components of X\Z are exactly
the surfaces (4) for c in Sigma. None is presumed normal, smooth
or factorial.

## 2. The precise published inputs

Use the final publication of Shulim Kaliman,
[*Polynomials with general C2-fibers are variables*](https://msp.org/pjm/2002/203-1/pjm-v203-n1-p08-s.pdf),
Pacific Journal of Mathematics 203 (2002), 161--190.
Its Main Theorem and Lemmas I--II, printed pp.162--163, apply to
a smooth affine threefold with factorial coordinate ring, constant
units, H_3=0, and an open A2-cylinder over a curve.

The two imported conclusions used here are:

- If every excluded irreducible component has at most isolated
  singularities, the threefold is A3 and the cylinder projection
  extends as a coordinate. The same conclusion holds with
  e(X)=1 and every excluded component factorial.
- If some excluded component is not factorial, Lemma II gives
  ML(X) different from C.

Here ML(A) denotes the intersection of the kernels of ALL LNDs of A.
These are intrinsic actions, not derivations of its larger cylinder.
Equations (1)--(4) verify the actual hypotheses above. No claim
about the geometry of a generic fiber is substituted for (3).

The relevant source audit included complete Sections 4--5,
printed pp.180--188. The proof endpoint uses Proposition 5.5 and
an imported result of Kaliman--Makar-Limanov [KaM-L2] about perfect
derivations. This note uses the published theorem; it does NOT
independently prove that imported result or its antecedents.

## 3. The intrinsic invariant has only two possibilities

The supplied pair immediately gives

    C subset ML(A) subset C[f].                     (5)

Suppose ML(A) contains a nonconstant F(f). For any LND E of A,
the chain rule gives

    0=E(F(f))=F'(f)E(f).                            (6)

The domain has characteristic zero and f is transcendental over C,
so F'(f)!=0. Hence E(f)=0 for every E. Consequently

    ML(A)=C   or   ML(A)=C[f].                      (7)

This elementary two-case conclusion uses (5); it is not a claim
about the possible ML invariants of arbitrary affine threefolds.
It also gives, without using any recognition theorem,

    ML(A)=C
      iff some E in LND(A) has E(f)!=0.             (8)

For the forward direction, otherwise f would belong to ML(A).
For the reverse direction, (6) prevents any nonconstant element
of C[f] from surviving the intersection (5).

## 4. Recognition and the complete conditional equivalence

Assume ML(A)=C. Lemma II's contrapositive makes EVERY component
of X\Z factorial. Together with e(X)=1, the factorial-boundary
version of the Main Theorem gives actual elements t,s in A with

    A=C[f,t,s].                                    (9)

There is a base-identification point in (9). The theorem may identify
the abstract open curve U with an open subset of A1 using a different
parameter r. It then supplies A=C[r,t,s] and C(r)=C(f), since both
parameters give the function field of the same cylinder base. Our
given f is regular on X, so

    f in A intersect C(r)=C[r].

Write f=F(r). A nonconstant polynomial F of degree greater than one
would make F(r)-c a product of nonunits over C, contradicting the
irreducibility of f-c proved in Section 1. Hence f=alpha r+beta,
alpha in C*, and (9) follows with the supplied f itself. This avoids
assuming that the theorem's initial identification of U fixes f.

Conversely, (9) makes ML(A)=C, since intersecting the kernels of
the three coordinate partials already leaves only constants.

If Crit(f) is empty, all the integral fibers (4) are smooth.
The isolated-singularity version of the same Main Theorem applies,
again giving (9). Conversely, (9) makes df everywhere nonzero.
Combining these implications with (8) proves

    A=C[f,t,s]
      iff Crit(f) is empty
      iff ML(A)=C
      iff some intrinsic LND E satisfies E(f)!=0.  (10)

All equivalences retain the supplied-pair setup of Section 1.
There is no assertion that an arbitrary polynomial function on a
threefold satisfies (10).

## 5. Normal exceptional fibers are another equivalent test

Each X_c in (4) is a Cartier hypersurface in the smooth threefold X.
Its coordinate ring is Cohen--Macaulay, hence satisfies Serre's S2
condition. For this integral surface, normality is therefore
equivalent to regularity in codimension one. Over C, that says
its singular locus is empty or zero-dimensional. A zero-dimensional
closed subset of an affine variety of finite type is finite.

Thus, if every X_c for c in Sigma is normal, all excluded components
have at most isolated singularities. Kaliman's Main Theorem gives
(9). Conversely, (9) makes every fiber an affine plane. Accordingly

    every X_c with c in Sigma is normal
      iff A=C[f,t,s].                              (11)

This is a normality TEST, not a deduction of normality from the
polynomial cylinder. The empty-Sigma case is included.

In particular, failure of (9) implies that at least one exceptional
fiber is nonnormal. Its failure of R1 supplies a positive-dimensional
singular locus. Since X is smooth, the hypersurface Jacobian
criterion identifies that locus with Crit(f) intersect X_c.
Thus the unrecognized branch cannot have only isolated critical
points across its finitely many exceptional fibers.

## 6. Every intrinsic additive action fixes the critical locus

If (9) fails, Section 4 rules out ML(A)=C. Equation (7) then gives

    ML(A)=C[f],
    E(f)=0 for every E in LND(A).                   (12)

The complete fixed-base theorem
[640](fixed-base-critical-locus-obstruction-pass640-working.md)
now applies to every intrinsic LND, not only to a chosen pencil or
centralizer. It proves

    Crit(f) subset intersection over ALL
                     E in LND(A) of Fix(E).         (13)

Recall why 640 applies: for each nonzero f-preserving E its actual
kernel is C[f,k_E]. After dividing its invariant content, the
primitive-volume identity is a nonzero constant times df wedge dk_E,
which vanishes wherever df does. Every corresponding additive flow,
and the group generated by all of them, fixes those points pointwise.

Equations (12)--(13) are conditional descriptions of a hypothetical
unrecognized branch. They do not prove that it occurs under A[u]=C^[4].
They also show why merely changing the common invariant through
intrinsic LND reselection cannot be assumed possible in that branch.

## 7. The remaining cylinder gap and provenance

The supplied independent commuting pair is an additional input:
its existence on every A with A[u]=C^[4] is NOT established here.
Even with the pair, polynomiality of A[u] gives ML(A[u])=C, not
the missing assertion ML(A)=C.

The retained [stable-invariant audit](stable-polynomial-invariants-pass32.md)
already distinguishes these implications. The published
[Koras--Russell cylinder calculation](https://arxiv.org/pdf/0807.4085)
has ML(X)=C[x] but ML(X x A1)=C. It is a warning against invariant
descent, not a claimed isomorphism X x A1=A4 or a counterexample
to the actual cylinder hypothesis of this note.

The bounded archive and primary-source search found no additional
cylinder consequence forcing the equivalent positive conditions
in (10)--(11) for every supplied pair. This reports the scope of
the checked arguments, not an absence theorem or a claim
that every possible route has been searched. A search for corrections
located no specific caveat to the cited Kaliman statements; that
search is not independent certification of the published proofs.

The recognition input is published. The invariant-intersection
deduction records its application to the retained supplied-pair
setup. No novelty or unrestricted cancellation result is claimed.
No saved checker was executed, imported or compiled, and no
canonical record was edited. Full independent saved-source review
is required before this note is accepted.
