# A source-dependent counterexample to the modified-Derksen conjecture

Date: September 18, 2026.

The complex-threefold cancellation problem remains UNSOLVED. This note
concerns a DIFFERENT conjecture, stated in Section 6 of
Boldyrev--Gaifullin--Shafarevich, arXiv:2312.08421v2 (December 9, 2024).
Novelty is UNKNOWN. No public priority claim, submission, or contact is made.

## 1. Precise claim

Let

    A=C[x,y,z,t]/(x^2*y+z^2+x+t^3), Y=Spec A, B=A[u].

Then the following assertions hold simultaneously:

    HD*(B)=B,
    I=(D(f): D is an LND of A, f in A) is a proper ideal of A,
    the origin of Y is fixed by every algebraic automorphism of Y.

Here HD* is generated as a C-algebra by the kernels of locally nilpotent
derivations WITH SLICES, and I is generated as an IDEAL of the BASE A.
The ring B is the CYLINDER. These are different ambient rings.

BGS call Y type A when HD*(A[u])=A[u]. Their Conjecture 1 asserts the
equivalence of this property, I=A, and the absence of SAut(Y)-fixed points.
The assertions above contradict its type-A-to-I=A direction, as stated in
that version. The already proved sufficient direction I=A implies type A
is unaffected. So is the equivalence between I=A and absence of fixed points.
[Definition 2, Corollary 2, Section 6](https://arxiv.org/html/2312.08421v2).

## 2. Inputs and proof

The base is nonrigid: D=x^2*partial_z-2*z*partial_y is a nonzero LND of A.
Indeed D(x)=D(t)=0, D(z)=x^2, D(y)=-2z, and D kills the equation.

The origin is fixed by Aut(Y), by Dubouloz--Moser-Jauslin--Poloni,
*Automorphism groups of certain rational hypersurfaces in complex four-space*,
arXiv:1309.7363, Proposition 3.1(2), printed page 3. This is the result cited
as journal Proposition 1 in Poloni's later paper. It applies to the Russell
cubic parameters d=2,k=2,ell=3. Only algebraic automorphisms are at issue;
the adjacent remark about holomorphic automorphisms does not contradict it.
[Original proposition](https://arxiv.org/pdf/1309.7363).

For every LND D of A, exp(sD) therefore fixes the origin for all s in C.
Differentiate f(exp(sD)(0))=f(0) at s=0 to obtain D(f)(0)=0. Consequently

    I is contained in m_0=(x,y,z,t), so I is proper.        (1)

Poloni's arXiv:2609.14090v1, dated September 12, 2026, constructs four
additive actions generating a transitive group on Y times A1. We use that
theorem with attribution. Its explicit cubic construction is not our new
discovery. The all-nonconstant-h reconstruction and extension is in673.
[Cylinder transitivity theorem](https://arxiv.org/html/2609.14090v1).

For completeness, the needed conductor deduction is as follows. Put H=HD*(B).
Since partial_u has a slice, A is contained in H. The subalgebra H is preserved
by every automorphism of B, since conjugation preserves slices. It is thus
stable under every LND: interpolate the coefficients of exp(sL)(f), f in H,
at finitely many distinct complex values of s. The coefficient of s is L(f).

Extend a base LND D to kill u. For j>=0, u^j*D is an LND of B, so

    u^j*D(f) belongs to H for every f in A.

Since A is contained in H, this implies IB is contained in H. The image-ideal
step is adapted from BGS Theorem 1, not presented as a newly invented method.
The conductor

    C_H={b in B: bB is contained in H}

is a nonzero ideal of B, contains IB, and is Aut(B)-invariant. Its zero set
is a proper invariant closed subset of the irreducible cylinder. Transitivity
forces that zero set to be empty. The Nullstellensatz gives C_H=B, hence
H=B. No finite generation of H is used. Together with (1) and the fixed
origin theorem, this proves the claim in Section 1.

## 3. Source and inference boundaries

The BGS arXiv version history was checked on September 18, 2026: it lists
v1 (December 13, 2023) and v2 (December 9, 2024). The checked abstract page
has no journal-reference entry. This does not exclude a later journal
publication, correction, or discussion elsewhere.
[Checked version record](https://arxiv.org/abs/2312.08421).

This note makes a version-specific mathematical statement, not an assertion
that the conjecture has remained unknown to be false until this work. The
new cylinder-transitivity input is itself a preprint. Its formulas have
been reconstructed internally, not certified by a proof assistant or an
external expert. The explicit modified-Derksen consequence was not located
in the bounded primary-source audit; that is not novelty clearance.

No claim about BGS Conjecture 2 is made: its surrounding type-B context and
displayed notation require separate interpretation. In particular, this
example is type A, not a type-B example for that discussion.

No isomorphism B=C^[4] has been produced. A nonpolynomial base with a full
modified Derksen invariant after adjoining one variable is NOT a
cancellation counterexample. This deduction closes an invariant-based
obstruction for this candidate, but leaves the original polynomial-cylinder
recognition requirement entirely in force.

## 4. Verification status

Root directly read the exact BGS definition and conjecture, the arXiv
version history, and the original DMP proposition. Geometry independently
reconstructed the same implication from those original sources. The
conductor proof in673 has already passed three separate full-source AI
reviews. The complete 114-line source was held at SHA256
1fddacac8fc4efaf9f8e0bf8e691fbae17288907d37b983f957f4a79a80c2dac.
General (cb08b1/89381d), Geometry (e261ed/799f3e), and Jet
(7f004b/ad8b64) each read it through EOF and returned CLEAN. All reviews
finished before this provenance-only update; the mathematical body is unchanged.

The separate finite certificate in675 supplies a second algebraic derivation
of the full-invariant input without the transitivity/conductor argument.

Saved checker scripts remain frozen. There is no new numerical experiment
or computational theorem assumption in this deduction. Human expert review
and a comprehensive priority audit remain outstanding.
