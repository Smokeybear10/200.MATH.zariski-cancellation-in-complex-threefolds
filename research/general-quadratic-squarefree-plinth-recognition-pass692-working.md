# General quadratic recognition with a squarefree plinth

## 1. Statement independent of the polynomial-curve model

Let R=C[x,y,z], let D0 be a nonzero locally nilpotent derivation,
and put C0=ker D0. The three-variable kernel and plinth theorems
give C0 isomorphic to C^[2] and a nonzero generator p of the
principal ideal D0(R) intersect C0. Choose rho in R with D0rho=p.
These precise structural facts are recorded as Theorems2.8 and2.10
in the inspected primary source.[^1]

Let lambda,a,b be nonzero elements of C0, D=lambda D0, and suppose
that w belongs to R and Dw=a^2 b. On B=R[t] set

    E=D+(1+abw)partial_t, v=at-w^2/2,
    u=t-bwv+(ab^2/2)v^2.                               (1)

Write w=h rho+k with h,k in C0, as justified below.

**Divisibility criterion.** If a divides lambda*h in C0, there is
a whole polynomial automorphism Phi of B with E Phi=Phi partial_t.
In particular ker E is C^[3], and the specific u in (1) is a
coordinate of B.

**Squarefree consequence.** If p is squarefree up to a nonzero
constant, EVERY admissible datum lambda,a,b,w satisfies this
criterion. The conclusion holds without assuming smoothness or
connectedness of V(p), an invariant ambient coordinate, or the
polynomial-curve presentation of690. A unit p is included.

More generally the proof gives a uniform bound for the only
possible poles of its modified exponential generator: a pole
along an irreducible pi of C0 has order at most floor(v_pi(p)/2).
This is a bound, not a claim that every such pole actually survives.

The conclusion concerns the displayed quadratic extensions only.
It does not classify arbitrary slice extensions, recognize every
stably polynomial three-ring, or prove cancellation. General
cancellation remains UNSOLVED, and mathematical priority is UNKNOWN.

## 2. All local slices and the modified generator

Since lambda is invariant and nonzero, Dw=a^2 b implies D0^2w=0.
Thus D0w belongs to D0(R) intersect C0=pC0. Write D0w=hp. Then

    h in C0 minus zero, k=w-h rho in C0,
    w=h rho+k, a^2 b=lambda h p.                       (2)

This proves the required decomposition with no choice of coordinates
for the embedded invariant ring.

On B_a define

    W=a t-h^2 rho^2/2-hk rho=v+k^2/2,
    L=D/a+bw partial_t, N=-W L.                        (3)

The restriction of L to R_a is an invariant multiple of D0 and
is locally nilpotent. Also Lw=ab, Lt=bw, L^2t=ab^2, L^3t=0,
so L is locally nilpotent on B_a. One has LW=0, hence N is an
LND there. Its coefficients are exactly

    N|R=[-lambda t+(lambda h/a)(h rho^2/2+k rho)]D0,
    Nt=-bwW.                                         (4)

When a divides lambda*h, both expressions are whole. Then N
restricts to an LND of B: nilpotence of each polynomial follows
from the injective localization B to B_a. Therefore

    Phi=exp(N), Phi^(-1)=exp(-N)

are mutually inverse WHOLE automorphisms. These are finite sums
on each generator, not formal power series or local-only maps.

## 3. Direct rectification and the supplied slice

On B_a, E=aL+partial_t, EW=a and [E,L]=0. Consequently

    [E,N]=-aL, [N,-aL]=0,
    E Phi=Phi(E-aL)=Phi partial_t.                    (5)

All identities restrict to B when the criterion holds. In particular

    s_star=Phi(t)=t-bwW+(ab^2/2)W^2,
    B=C[Phi(x),Phi(y),Phi(z),s_star],
    ker E=C[Phi(x),Phi(y),Phi(z)].                     (6)

The given u need not equal s_star. The exact identities

    Ev=a, q=abv-w, Eq=0, v+q^2/2=au

give Eu=1. By (5), Es_star=1 too. Thus u-s_star is in the
polynomial kernel and replacing s_star by u is a whole triangular
coordinate shear. This proves the particular-coordinate assertion.
As in688, the whole quotient maps also identify
R[Q]/(w+Q+abQ^2/2) with ker E; no extra localization is needed.

## 4. Exact valuation bound and squarefree case

Let pi be an irreducible element of the UFD C0 and write

    A=v_pi(a), L0=v_pi(lambda), H0=v_pi(h), P0=v_pi(p).

Equation (2) and b in C0 give

    2A<=L0+H0+P0.                                    (7)

If e=A-L0-H0 is positive, it follows that

    2e+L0+H0<=P0, hence e<=floor(P0/2).                (8)

This is precisely the possible pole order of lambda*h/a in (4).
Each such pi is prime in R as well: C0 is factorially closed in
the UFD R, so a factorization in R would give a factorization in
C0. Thus the bound also has its asserted meaning for the rational
coefficient on the actual polynomial ambient space. Other factors
in (4) can cancel a pole; they cannot increase its order.

When p is squarefree, P0 is zero or one for every pi, so (8)
allows no positive e. Equivalently a divides lambda*h, and
Sections2-3 apply. This proof includes all repeated factors of
lambda and all local slices, not only the selected minimal rho.

## 5. Earlier coverage and remaining obligation

The modified-generator mechanism is the one used in691; here its
whole branch is isolated without the polynomial-curve hypotheses.
The local-slice decomposition follows directly from a principal
plinth and is established algebraic machinery, not a new kernel
or plinth theorem.

The older [squarefree-plinth note18](plinth-units-pass18.md)
concerns invariant added coefficients A D0+B partial_t and uses
connectedness in its unit argument. The current coefficient
1+abw generally is not invariant. Its squarefree proof is the
different elementary divisibility argument (7)-(8); it does not
silently remove hypotheses from the older invariant-extension
statement. The later intrinsic smooth-squarefree recognition669
also imposes a different smoothness hypothesis and treats a
different intrinsic presentation. No priority claim is inferred
from these internal comparisons.

For a multiple plinth component, (8) bounds a possible pole but
does not repair it. Proofs690-691 perform that repair in one
explicit embedded-kernel class. A whole repair along arbitrary
multiple components, compatible at their intersections, remains
unproved. Even such a repair for every quadratic extension would
still require a separate reduction from the arbitrary hypothesis
A[s]=C^[4]. Neither missing step is asserted here.

[^1]: N. Dasgupta and S. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables, primary version2](https://arxiv.org/html/2306.00510v2), Theorems2.8 and2.10. They recall the known polynomial-kernel and principal-plinth results; the present proof uses only those stated consequences, not a new geometric replacement theorem.

## Verification provenance

The 150-line mathematical source was held at SHA256
cacc291dc25c162c628ec1f4157e5247568251e5d613e51889642e539e8306cc.
Root's complete EOF read was581425. Separate full-source AI reviews
returned CLEAN without correction: General73c7e1, final hashc5fec1;
Jet8ddfbd, final hash36a1e4; Geometryb8bc5b, final hash28da14.
They independently distinguished a sufficient criterion from a
necessary one, and generator poles from poles of an exponential.
The source's structural hypotheses and old-note comparisons were
also checked, including primary DG2.8/2.10 in turn6318view0 and
turn6319view0/1. Root had read those primary statements in
turn6309view1/2 before drafting.

Fresh rootbe34a0 used the actual polynomial ring with
D0=x(x-1)partial_y+2y partial_z, g=x(x-1)z-y^2,
a=g+x, lambda=a^2,h=1,k=g+1,b=x(x-1). It checked the actual
generator's nilpotence on the generators, its invariant W, and
both supplied and repaired slice identities. This exercises a
disconnected squarefree-plinth control and h not divisible by a.
The exact proof, not this finite example or integer sanity grid,
establishes the universal statement.

Only this provenance was appended after full-source reviews. No
saved checker was executed, imported, compiled or edited. Internal
AI reviews and exact tests are not human expert review, formal
proof certification, or a determination of novelty.
