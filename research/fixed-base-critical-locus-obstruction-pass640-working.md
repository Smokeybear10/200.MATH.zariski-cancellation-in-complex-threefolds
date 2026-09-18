# Every action preserving the common base fixes its critical locus

Private working proof, September 18, 2026. Suppose A[u] is actually
isomorphic to C^[4], and f is the common invariant supplied by two
independent commuting LNDs on A. Every LND E of A with E(f)=0 fixes
every critical point of f. The action E need not commute with either
of the supplied actions.

The key step is that f is a coordinate of the plane ker E for every
nonzero such E. A finite denominator argument proves this from the
actual generic affine-plane fiber and the plane LND theorem. Thus
changing actions while retaining f, including justified primitive
division, cannot remove Crit(f).

This does not assert that a critical f of this kind actually exists
under the cylinder hypothesis. It neither constructs the original
pair nor proves f smooth. General cancellation remains UNSOLVED;
novelty is UNKNOWN.

## 1. Actual setup and the generic plane

Let A be a finitely generated complex domain with a supplied
isomorphism A[u] to C^[4], and put X=Spec(A). Then A is a smooth
three-dimensional UFD with A*=C*. Suppose P,Q are nonzero commuting
LNDs, independent over Frac(A), with the actual kernel data

    ker P=C[f,g],       ker Q=C[f,h],
    ker P intersect ker Q=C[f],
    P(h)=p(f),         Q(g)=q(f),
    p,q nonzero polynomials.                         (1)

The intrinsic plane-quotient theorem and the simultaneous kernel
argument in [635, Section 1](fiberwise-free-direction-gluing-pass635-working.md)
give (1) for such a pair. One may equivalently keep (1) explicitly
as input. No absence of common fixed points is assumed here.

Let K=C(f), and let S=C[f] minus {0}. The actual local-slice equality
and its further localization are

    A_p=C[f,p(f)^(-1),g,h],
    A_K:=S^(-1)A=K[g,h]=K^[2].                       (2)

In particular this is a split polynomial plane over K, not merely
a geometrically split surface or a rational function field.

We also have the exact intersection

    A intersect K = C[f]                            (3)

inside Frac(A). Indeed P and Q extend to that fraction field and
annihilate K. Every element of A intersect K therefore belongs to
both kernels in (1); the reverse inclusion is immediate. This
argument uses the actual common kernel, not a claimed retraction
onto it or an inference from generic rationality.

## 2. A denominator-clearing lemma for a plane subalgebra

We first isolate the elementary step that will be applied to ker E.
Suppose B is a complex polynomial plane containing C[f], with

    B intersect C(f)=C[f],
    S^(-1)B=K[v]                                    (4)

as included rings in a common fraction field. Then f is a coordinate
of B.

To prove this, choose actual plane generators b1,b2 with B=C[b1,b2].
Because v belongs to S^(-1)B, write

    v=b/s(f),     b in B,  0 != s(f) in C[f].        (5)

By (4), each b_i is a finite polynomial in v with coefficients in K.
Choose a nonzero h(f) divisible by s(f) and by every denominator
occurring in these two finite expressions. Then v belongs to B_h,
and each b_i belongs to C[f,h^(-1),v]. Both inclusions give

    B_h=C[f,h^(-1),v].                              (6)

This is a finite spread of an INCLUDED equality. It requires neither
a choice of a root in a larger field nor an assertion about a
closed exceptional fiber.

Let partial_v denote the C[f,h^(-1)]-derivation of (6) taking v
to 1. Its two values partial_v(b_i) lie in B_h. Choose N>=0 so that

    h^N partial_v(b_i) belongs to B,  i=1,2.         (7)

Since b1,b2 generate B, delta=h^N partial_v restricts to a derivation
of B. On K[v] it is locally nilpotent: h belongs to K, and successive
v-derivatives eventually vanish on every polynomial. Hence its
restriction to B is also locally nilpotent. It is nonzero, for if
it vanished on B it would vanish on B_h, whereas delta(v)=h^N!=0.

Finally,

    ker(delta on B)=B intersect K=C[f].             (8)

Rentschler's plane theorem says that this kernel has a coordinate
generator w of B. Thus C[w]=C[f]. Equality of these one-variable
polynomial algebras makes f=alpha w+beta for alpha in C*, beta in C:
the degrees of two inverse polynomial expressions must multiply to
one. Therefore f is a coordinate of B, proving the lemma.

## 3. Application to every f-preserving intrinsic action

Let E be ANY nonzero LND of A satisfying E(f)=0. No commutation
with P or Q is required. The
[actual intrinsic quotient theorem](intrinsic-quotient-surface-pass.md)
gives the included kernel plane B=ker E isomorphic to C^[2].

Since S consists of invariants of E, localization extends E to a
nonzero K-LND E_K on A_K=K^[2]. It remains nonzero because A embeds
in A_K. Invariance of the denominators gives

    ker E_K=S^(-1)(ker E)=S^(-1)B.                  (9)

Rentschler over the field K gives ker E_K=K[v], where v is one member
of a K-coordinate system of A_K. This is an equality over K itself,
not only over its algebraic closure. Also (3), together with f in B,
implies B intersect K=C[f]. The lemma of Section 2 now applies and
proves

    ker E=C[f,k_E] for some k_E in A.               (10)

Here f is a coordinate of ker E. Equation (10) does not yet assert
that f is a coordinate of the unknown threefold A.

The exact primary field scope used twice is recorded in
[Dasgupta--Gaifullin, arXiv:2306.00510v2](https://arxiv.org/pdf/2306.00510v2),
Section 1 and Theorem 2.7. Their ground field is an arbitrary field
of characteristic zero; Theorem 2.7 gives triangularization of a
nonzero LND of k[x,y] by a k-automorphism, so its kernel is a
coordinate line over k. The statement is explicitly attributed there
to Rentschler, *Operations du groupe additif sur le plan affine*,
C. R. Acad. Sci. Paris 267 (1968), 384--387.
The directly read source here is that precise statement in the
primary Dasgupta--Gaifullin paper, not a claimed rereading of the
original 1968 proof. Both k=K and k=C are within its stated scope.

## 4. Primitive normalization and the critical locus

For completeness, primitive normalization works in the actual UFD A
without choosing polynomial coordinates on A. Choose finite algebra
generators a1,...,a_m of A. Let a be a gcd of the nonzero E(a_i).
The ideal generated by these values is the ideal generated by all
E(A), so E=aE0 for a regular primitive derivation E0 of A.

Since E(a)=aE0(a) belongs to aA, the LND divisibility lemma gives
E(a)=0. One can see that lemma directly from the additive E-degree:
if E(a)=ab!=0, then

    deg_E(a)-1=deg_E(E(a))
              =deg_E(a)+deg_E(b),

which is impossible. It follows that E0(a)=0, and induction gives

    E^j(b)=a^j E0^j(b) for b in A, j>=0.            (11)

Thus E0 is locally nilpotent and ker E0=ker E. It is nonzero and
primitive, and still kills f. In particular (10) applies to E0.

The complete intrinsic Jacobian normalization in
[637](intrinsic-primitive-jacobian-normalization-pass637-working.md)
now applies to the kernel coordinates f,k_E. For a generator omega
of Omega^3_A, there is a nonzero complex constant c_E with

    i_E0 omega = c_E df wedge d k_E.                (12)

At a critical point x of f, df(x)=0, so contraction with the
nonvanishing volume form gives E0(x)=0. Multiplication by a gives
E(x)=0. The zero derivation has this property as well. Consequently

    Crit(f) subset Fix(E)
    for EVERY E in LND(A) satisfying E(f)=0.        (13)

Every corresponding additive-group flow fixes each such point:
all positive iterates E^j(b) evaluate to zero there for every b in A,
so the exponential acts as the identity on that point. Hence the
group generated by all f-preserving additive actions fixes Crit(f)
pointwise. This is not a claim that every algebraic automorphism
over C[f] fixes each critical point rather than permuting them.

## 5. The exact fixed-base boundary

Equation (13) applies to arbitrary f-preserving LND reselection,
not only to the original pencil, its rational saturation, or a
fixed-pivot centralizer. Polynomial shears, swaps, and justified
primitive divisions do not escape this obstruction while their
resulting actions continue to kill the same f.

Thus, IF Crit(f) is nonempty, no collection of f-preserving LNDs
can have an empty joint fixed locus. This is a conditional barrier.
It neither provides an example with Crit(f) nonempty under A[u]=C^[4]
nor excludes such an example.

Conversely, if df is nowhere zero, the argument in
[639, Sections 4--5](no-joint-fixed-point-recognition-pass639-working.md)
already gives

    A=C[f,t,s].                                    (14)

Indeed the original common kernel makes f-alpha prime and nonunit
for every alpha; (2) is the actual plane-bundle chart away from
finitely many fibers. Smoothness of f then supplies smooth integral
exceptional fibers. Contractibility of X, Masuda's acyclicity
Proposition 2.6, the stated Fujita factoriality consequence, and
Masuda's Theorem 4.1 supply (14), exactly as audited in 639.
This application does not require the ORIGINAL pair to have no
common fixed point. The converse, (14) implying f smooth, is immediate.

Within the setup of Section 1 this also gives the exact equivalence

    Crit(f) is empty
      iff A=C[f,t,s]
      iff some free LND E of A satisfies E(f)=0.    (15)

Here free means that its additive action has no fixed point. The
coordinate presentation supplies E=partial_t. Conversely, (13)
forces Crit(f) to be empty whenever such a free action exists.
Thus (15) adds no existence assertion beyond its explicit conditions.

For this supplied common base, smoothness is therefore already a
recognition criterion. The unresolved task is to rule out its
critical fibers using the cylinder, or to obtain useful actions
with a DIFFERENT common invariant. Changing f-preserving actions
alone cannot move a critical point.

## 6. Provenance and review boundary

The proof uses the retained intrinsic quotient result, the full
primitive-volume argument of 637, and the established recognition
endpoint audited in 639. The generic-line spread in Section 2 is
written out to avoid assuming a theorem about exceptional fibers
or descending an affine-line form without justification.

This is not a theorem for an arbitrary polynomial f on an arbitrary
threefold: (1)--(3) are essential inputs. No global C[f]-plane chart
is presumed before the conditional conclusion (14). No hypothesis
that all intrinsic LNDs preserve f is introduced.

No saved checker was executed, imported or compiled, and no canonical
record was edited. Independent full saved-source review is required
before acceptance. No newness, human expert review, formal proof
certification, universal action-selection procedure or solution of
the cancellation problem is asserted.
