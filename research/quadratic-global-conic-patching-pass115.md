# Global patching from the first two derivative images

Equality of the first two derivative-image ideals at every closed base
point is enough to patch the actual local conics into one global conic.
The argument uses finite degree modules, a principal ideal in the
invariant plane, and intersection of coefficient rings at height one.
It does not recognize the resulting threefold as affine three-space.

## 1. Exact algebraic hypotheses

Let S=C[s,t], K=Frac(S), and let A be a faithfully flat S-domain with
a nonzero locally nilpotent S-derivation N. Assume

\[
\begin{gathered}
\ker(N|_A)=S,\qquad A\otimes_S K=K[v],\\
F_j=\ker(N^{j+1}|_A),\qquad I_j=N^j(F_j)\subseteq S,\\
F_j\text{ is finite locally free of rank }j+1,\\
A_{\mathfrak p}=S_{\mathfrak p}[(F_2)_{\mathfrak p}]
\quad\text{for every height-one }\mathfrak p\subset S,\\
(I_2)_{\mathfrak m}=(I_1)_{\mathfrak m}
\quad\text{for every maximal }\mathfrak m\subset S.
\end{gathered}
\tag{1}
\]

All localizations here invert elements of S, not arbitrary elements of A.
Kernels therefore commute with these localizations. The finite-module
statement is the direct flatness argument in
[degree-module102, Section 2](quadratic-degree-module-fiber-rigidity-pass102.md).
The height-one generation is the actual divisor conclusion of
[divisor107, Sections 1--5](quadratic-constant-divisor-filtration-pass107.md)
together with the degree-one slice case recorded in
[all-normal111, Section 1](quadratic-all-normal-mixed-exclusion-pass111.md).
The final line of (1) is a substantive hypothesis, not a consequence of
equality at height one alone.

## 2. One global quadratic parameter

The section 1 of F1 is nonzero in every module fiber. If it belonged to
m(F1)_m, its image in A_m/mA_m would be zero, contrary to faithful
flatness. Thus 1 is a locally unimodular section of F1. The quotient
F1/S is locally free of rank one, and N identifies it with the ideal I1.
In particular I1 is a nonzero invertible ideal.

An invertible ideal of the UFD S is principal. Concretely, choose P
having exactly the height-one valuations of I1. The quotient fractional
ideal P^(-1)I1 has valuation zero at every height-one prime. An invertible
ideal is the intersection of these localizations, so it is S. Thus
I1=PS with P nonzero. This assertion uses an actual ideal, not a choice
of a global basis for every degree module.

For U in F2, NU lies in F1, so I2 is contained in I1. The finite quotient
I1/I2 vanishes at every maximal ideal by (1), and hence is zero. Choose
an actual U in F2 with N squared U=P, and put r=NU. Then

\[
\begin{gathered}
I_1=I_2=PS,\qquad Nr=P,\qquad NU=r,\\
F_1=S\oplus Sr,\qquad F_2=S\oplus Sr\oplus SU,\\
\eta=2PU-r^2\in S.
\end{gathered}
\tag{2}
\]

To verify the bases, subtract the appropriate S-multiple of r from an
element of F1, or of U from an element of F2, using its first or second
derivative respectively. The remainder has smaller degree. Independence
follows by applying N squared, then N, and then using A as a domain.
The formula for eta is invariant by direct differentiation and the
kernel hypothesis in (1).

## 3. The conic subalgebra and height-one coefficient intersection

There is an S-algebra homomorphism to A with image C=S[U,r]:

\[
\mathcal C=S[\mathsf U,\mathsf r]/
  (\mathsf r^2-2P\mathsf U+\eta)
\longrightarrow A,\qquad
(\mathsf U,\mathsf r)\longmapsto(U,r).
\tag{3}
\]

The source is free over S[mathsf U] with basis 1,mathsf r, since the
relation is monic in mathsf r. It is therefore S-torsion-free. Over K,
P is a unit and the relation eliminates mathsf U; the map becomes the
isomorphism K[mathsf r] to K[r]=K[v]. Its kernel before localization is
S-torsion, so is zero. In particular C has the S-basis

\[
\{U^i:i\ge0\}\ \cup\ \{rU^i:i\ge0\}.
\tag{4}
\]

By (2) and the height-one hypothesis, C_p=A_p at every height-one prime
p of S. Let f be any element of A. In K[r], it has a unique finite
expansion in (4) with coefficients in K. Membership in C_p forces each
of those same coefficients to lie in S_p, because (4) is also an S_p
basis of C_p. A normal domain is the intersection of its height-one
localizations inside its fraction field; for this UFD the assertion
also follows by factoring a reduced denominator. Therefore every
coefficient lies in S. This proves A=C, not just equality away from a
finite subset of the base.

We have proved the global presentation

\[
\boxed{\quad
A=S[U,r]\simeq S[\mathsf U,\mathsf r]/
  (\mathsf r^2-2P\mathsf U+\eta),\qquad
N=P\partial_r+r\partial_U.
\quad}
\tag{5}
\]

The displayed derivation is interpreted on the quotient, where it
annihilates the relation. No formal coordinate, completed invariant
ring, projective-module cancellation, or finite generation of A as an
S-module is used in this patching step.

## 4. All degree modules and closed fibers

In K[r], U=(r squared+eta)/(2P). The two basis families in (4) have
distinct degrees 2i and 2i+1. Thus cancellation between their highest
degrees is impossible, and for every j at least zero,

\[
\begin{gathered}
F_j=\bigoplus_{2i\le j}S U^i
\ \oplus\!\bigoplus_{2i+1\le j}S rU^i,\\
I_j=\frac{j!}{2^{\lfloor j/2\rfloor}}
       P^{\lceil j/2\rceil}S
    =P^{\lceil j/2\rceil}S\quad(j\ge1).
\end{gathered}
\tag{6}
\]

At a closed base point m, (5) gives exactly the following possibilities.

| Base values | Whole fiber and N-action |
| --- | --- |
| P(m) nonzero | A polynomial line in r; N is the nonzero constant translation P(m) partial_r |
| P(m)=0 and eta(m) nonzero | Two disjoint reduced lines in U, with r equal to the two nonzero roots of r squared=-eta(m); N translates them with opposite speeds |
| P(m)=eta(m)=0 | The entire double line C[U,r]/(r squared); N=r partial_U, nonzero on the whole scheme and zero on its reduction |

This classification is a consequence of the global presentation. It
cannot be used backwards to prove the last hypothesis of (1) without
the separate free-fiber argument.

## 5. Consequence in the supplied quadratic frame

In the supplied actual nonconical quadratic frame, all hypotheses in
(1) are now available. Faithful flatness, the full invariant plane and
the generic line are the retained actual quotient inputs. Module102
gives finite local freeness, and divisor107 gives generation in height
one. The [fixed-fiber theorem114](whole-double-universal-frontier-pass114.md)
proves I2=I1 at every closed fiber containing a fixed point. The
[free-fiber theorem115](free-quadratic-fiber-conic-pass115.md) proves it
at every other closed fiber. These cases exhaust the maximal ideals.
Thus (5) and (6) hold globally in that supplied frame.

This corollary is conditional on the entire stated actual-frame
dependency chain, not a new derivation of those hypotheses from an
arbitrary polynomial cylinder. The previously missing all-closed-point
step is exactly the combination of the two fiber theorems, and the
patching step is Sections 2--3 above.

## 6. Recognition is a separate problem

Even smooth contractible conics of this form need not be polynomial
three-rings. The [recognition note115](quadratic-conic-global-recognition-gates-pass115.md)
checks an explicit Russell cubic in exactly this format and the
hypotheses of published positive recognition theorems. It does not
assert that the Russell cubic has a polynomial cylinder or realizes
the supplied original frame.

The resulting conic still has to be combined with the actual original
coordinate identities to obtain a polynomial threefold. Entry of an
arbitrary sliced action into that special frame remains unproved too.
Thus (5) is not a proof of the intended cancellation conjecture.

## Sources and verification scope

The finite locally free modules and actual divisor generation are the
explicit retained local proofs cited above. The algebraic patching proof
is written in full here. The elementary UFD denominator argument suffices
for the coefficient intersection; the related general normal-domain
criterion is [Stacks Project, Lemma 10.157.6(2), tag 031T](https://stacks.math.columbia.edu/tag/031T).
Its complete displayed statement and proof were freshly read. Deeper
referenced proofs were not reconstructed; the direct UFD argument above
does not require them.

Finite symbolic identities cannot prove the all-point hypothesis in (1)
or the global isomorphism in (5). Review and execution evidence are
recorded separately. No novelty, human expert review, formal verification,
or full cancellation claim is made.
