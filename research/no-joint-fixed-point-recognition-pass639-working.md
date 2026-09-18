# No joint fixed point gives intrinsic recognition

Private working proof, September 18, 2026. Let an actual affine
complex threefold algebra A satisfy A[u] isomorphic to C^[4].
If A has two primitive, commuting, generically independent locally
nilpotent derivations with no common fixed point, then their common
invariant f is a coordinate and A=C[f,t,s].

The proof uses the intrinsic Jacobian normalization in
[637](intrinsic-primitive-jacobian-normalization-pass637-working.md)
and established acyclic-threefold recognition. It does not select a
free member of the original action module or a fixed-pivot centralizer.
Existence of the required pair on every stably polynomial A is NOT
proved. General cancellation remains UNSOLVED; novelty is UNKNOWN.

## 1. Exact hypotheses and conclusion

Let A be a finitely generated complex domain with a supplied
isomorphism A[u] to C^[4]. Set X=Spec(A). Suppose that

    P,Q are nonzero primitive LNDs of A,
    [P,Q]=0, and P,Q are independent over Frac(A).     (1)

Primitivity means that no nonunit divides every value of the
derivation. It is not the assertion that its fixed locus is empty.
Assume additionally that the simultaneous fixed locus is empty:

    Fix(P) intersect Fix(Q) = empty.                  (2)

The actual quotient result in
[the intrinsic quotient note](intrinsic-quotient-surface-pass.md)
and the simultaneous kernel argument in
[635, Section 1](fiberwise-free-direction-gluing-pass635-working.md)
give elements f,g,h of A such that

    ker P=C[f,g],       ker Q=C[f,h],
    ker P intersect ker Q=C[f],
    P(h)=p(f),         Q(g)=q(f),
    0 != p,q in C[f].                                (3)

These are coordinates of the two actual kernel planes. No element
of (3) is initially assumed to be an ambient coordinate of A.
Equivalently, one may retain (3) explicitly among the hypotheses;
the proof below only uses the displayed actual inclusions.

The conclusion is the existence of t,s in A with

    A=C[f,t,s],       A[u]=C[f,t,s,u].                (4)

In particular f itself, not just an unspecified function on X, is
a coordinate. The proof is an existence and recognition argument;
it does not provide an algorithm for constructing t,s.

## 2. The cylinder supplies the ambient hypotheses

Smoothness and factoriality descend through a polynomial extension.
Thus A is a smooth three-dimensional UFD, and A*=C*. Moreover
X(C) times C is isomorphic to C^4. The zero section is a deformation
retract of this product, so X(C) is contractible. In particular,

    H_i(X(C),Z)=0 for every i>0.                     (5)

All acyclicity statements here use integral singular homology.
There is no inference that a hypersurface of X is contractible,
factorial or smooth merely because X has these properties.

The differential decomposition for A[u], restricted at u=0, gives
Omega^1_A direct_sum A free of rank four. Consequently Omega^3_A
is free of rank one. Choose its generator omega. Contraction with
omega identifies Der_C(A) with Omega^2_A, including on every tangent
space. A polynomial coordinate frame on A is not used for this step.

## 3. Joint fixed points contain the critical locus

The complete primitive-Jacobian argument of 637 applies to each
action in (1), using the SAME volume form omega. It gives constants
c,d in C* such that

    i_P omega = c df wedge dg,
    i_Q omega = d df wedge dh.                       (6)

This is the substantive algebraic dependency. Its proof excludes
divisorial Jacobian factors by a conormal-sequence argument at the
generic points of invariant prime divisors. It does not assume
closed quotient fibers are smooth. The proportionality constants
are units because both the given action and its intrinsic Jacobian
field are primitive in the smooth tangent module.

At any closed point x in X with df(x)=0, both right sides of (6)
vanish. Since omega(x) is nonzero, contraction is an isomorphism,
and therefore P(x)=Q(x)=0. Thus

    Crit(f) subset Fix(P) intersect Fix(Q).           (7)

By (2), df vanishes nowhere. The smoothness criterion for a
morphism from a smooth complex variety to the smooth curve A1
then proves that f:X->A1 is smooth. In particular every nonempty
scheme fiber is a smooth surface. It is not necessary first to
assume normality of these fibers and then analyze their singular
points under the group action.

The same normalization also gives q=-(d/c)p. This equalization is
not needed for the recognition proof: the local slice P(h)=p(f)
alone supplies the open chart below. Neither p nor q is asserted
to be a constant polynomial.

## 4. Every fiber is integral and the open chart is trivial

The intersection of two factorially closed subrings is factorially
closed, so C[f] is factorially closed in A. For each alpha in C,
the polynomial f-alpha is irreducible in C[f] and remains irreducible
in A. Because A is a UFD, it is prime. It is not a unit since
A*=C* and f is nonconstant. Therefore

    X_alpha=Spec(A/(f-alpha)A)
    is nonempty and integral for every alpha in C.  (8)

Together with Section 3, each X_alpha is a smooth, irreducible
affine surface. The domain A is torsion-free as a C[f]-module,
and C[f] is a PID. Hence f is flat. Its nonempty closed fibers and
its generic fiber make it surjective, so it is faithfully flat.
This also follows from the already established surjective smooth
morphism, but the module argument records flatness separately.

Since P(h)=p(f) is a nonzero invariant, h is an actual local slice.
The local-slice theorem yields the equality of included algebras

    A_p=(ker P)_p[h]=C[f,p(f)^(-1),g,h].             (9)

Here g,h are algebraically independent over C[f,p^(-1)]. Let
Sigma be the finite set of complex roots of p. Equation (9) says
that f over A1 minus Sigma is a trivial affine-plane bundle.
If p is a nonzero constant, (9) already proves (4) with t=g,s=h.
There is then no exceptional-fiber argument to perform.

Assume now that Sigma is nonempty. Its fibers satisfy (8) and are
smooth by (7). None of these facts says that g,h are coordinates
on an exceptional fiber. The original quotient actions can still
have nontrivial boundary invariant extensions there.

## 5. Precise geometric inputs and their application

The following established results are used from
[Masuda, arXiv:2512.06687v1](https://arxiv.org/html/2512.06687v1).

- Proposition 2.6: a faithfully flat map from a smooth acyclic
  n-fold, n>=3, to A1, trivial with fiber A^(n-1) off finitely many
  points, has acyclic exceptional fibers if those fibers are smooth
  and irreducible.
- Its introduction explicitly records the Fujita consequence that
  a smooth acyclic affine variety is factorial and has only constant
  units, citing Fujita, 1.18--1.20.
- Theorem 4.1: a smooth acyclic affine threefold with an affine-plane
  fibration over A1 and factorial closed fibers is affine three-space,
  with the specified base function as a coordinate.

The complete statements and proofs of Proposition 2.6 and Theorem
4.1 were read directly. The former uses compact-support cohomology
and duality. The latter credits the earlier Miyanishi--Kaliman
recognition theorem. Here its affine-plane-fibration terminology
allows exceptional fibers not already known to be planes.

Sections 2--4 verify every hypothesis of Proposition 2.6 with n=3.
Consequently the exceptional surfaces X_alpha are acyclic. They
are smooth and affine, so the stated Fujita result makes them
factorial. The other fibers are planes by (9). Theorem 4.1 now
applies and gives precisely (4).

Thus the logical order is

    no joint fixed point -> df nowhere zero
    -> smooth integral fibers -> acyclic fibers
    -> factorial fibers -> A=C[f,t,s].              (10)

No step in this chain substitutes normality for factoriality.
No acyclicity of a singular exceptional fiber is asserted.

For provenance, Fujita's original is *On the topology of
non-complete algebraic surfaces*, Journal of the Faculty of Science,
University of Tokyo, Section IA 29 (1982), 503--566, available in
the [official repository record](https://repository.dl.itc.u-tokyo.ac.jp/records/39576).
That repository returned an access error during this audit. Its
original items 1.18--1.20 were therefore not independently read here.
The exact factoriality implication used above is the one expressly
stated and invoked in Masuda's primary text, not a claim of a fresh
proof or direct inspection of the unavailable original.

## 6. Relation to the retained recognition and selection boundaries

[27, Section 5](intrinsic-plinth-boundary-pass27.md) already retained
the factorial-exceptional-fiber recognition endpoint, with its exact
Masuda dependency. This note supplies those factorial fibers under
the additional no-joint-fixed-point hypothesis through (6)--(10).
It does not introduce a new affine-three-space recognition theorem
or claim priority for the topological ingredients.

The conclusion is compatible with the negative action-selection
controls in [634](saturated-pencil-no-free-direction-pass634-working.md)
and [636](fixed-pivot-shear-obstruction-pass636-working.md). An actual
polynomial threefold can admit the required pair while the whole
C[f]-module generated by that pair contains no free member, or
while the entire LND centralizer of a chosen pivot contains no
free member. This proof never asserts otherwise. Once (4) is
established, a free action such as partial_t exists, but it need
not lie in either prescribed class.

Similarly, this note does not prove that the joint image algebra
C[bar g,bar h] on a bad fiber is its full residual invariant line.
It does not apply an embedded-line degree theorem before such an
embedding has been justified. A global C[f]-plane chart is obtained
as the conclusion (4), not used to prove the unknown A polynomial.

There is an exact limitation on changing a given pair. Write

    I(P,Q)=(P(a),Q(a) : a in A) subset A.             (11)

For M in GL_2(A), let (P',Q')^T=M(P,Q)^T. Each new value is an
A-linear combination of old values, and the inverse matrix gives
the reverse inclusion. Hence

    I(P',Q')=I(P,Q).                                 (12)

In particular all swaps and unimodular shears preserve the joint
fixed scheme. This remains an obstruction even when a particular
change also preserves local nilpotence and commutation. Those
action properties are not claimed for arbitrary matrices M.

Division by a common coefficient of one field is not unimodular
and can change (11). For example, the 637 control has

    P=x partial_y+2y partial_z,
    g=xz-y^2,     Q=gP+x partial_z.

The pair has the joint fixed line x=y=0, while
(Q-gP)/x=partial_z is a slice derivation. Thus (12) does not rule
out procedures involving a justified primitive division.

No construction here removes common fixed points from an arbitrary
commuting pair. In fact, the assertion that EVERY A with A[u]=C^[4]
admits a pair satisfying (1)--(2) would, by this theorem, imply
the three-dimensional cancellation statement. Conversely, if all
such A were polynomial, two coordinate partials would supply such
a pair. Thus this universal existence assertion is equivalent to
that cancellation statement and is NOT established here. The proved
entry is recognition once the specified pair exists.

The primitive hypothesis remains explicit; no unproved assertion
about simultaneous primitive normalization is needed.

## 7. Dependency and verification boundary

The full saved 637 proof was read before this note was written,
at SHA256 a5b7bdfb8b4015850c609f1fc6e5d0347c1fa15edf4d9f61c2f4469648b70d42.
The actual quotient note and the retained Section 5 of 27 were
also read through EOF. The primary input is identified precisely
in Section 5, including the distinction between a directly read
proof and Fujita's result as stated in Masuda.

This is a conditional recognition result on the actual unknown
threefold, not a recognition inferred from a hypothetical polynomial
presentation. No saved checker was executed, imported or compiled.
Independent full saved-source review is required before acceptance.
No human expert review, formal proof certification, public contact,
universal termination, cancellation completion or novelty claim is
asserted.
