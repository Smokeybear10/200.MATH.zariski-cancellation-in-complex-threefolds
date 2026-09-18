# Quadratic repairs: whole invariant-plane normalizers and the gluing gap

## 1. Result and scope

Use the complete setup and whole quotient maps of
[688](quadratic-sliced-extension-normal-form-and-repair-gate-pass688-working.md):

    R=C[x,y,z], D in LND(R), 0!=a,b in ker D, Dr=a^2 b,
    c=ab, B=R[t], E=D+(1+cr) partial_t,
    v=at-r^2/2, q=cv-r, u=t-brv+(ab^2/2)v^2,
    A=R[Q]/(r+Q+cQ^2/2) isomorphic to B/(u).

This note proves that the natural R-to-A map gives isomorphisms on
EVERY finite thickening of a=0, compatibly, and that their complements
are separately isomorphic. It then strengthens688's obstruction:
in the m>=3 triangular controls, no automorphism sending t to u can
even PRESERVE the whole old invariant plane as a subalgebra. Pointwise
fixing is not required for this exclusion.

The controls nevertheless have u as a whole coordinate. These are
limits on a repair mechanism, not exotic affine spaces or cancellation
counterexamples. General cancellation is UNSOLVED, novelty UNKNOWN.

## 2. Every finite thickening and the formal completion

For every n>=1 the natural map is an isomorphism

    R/(a^n) --> A/(a^n).                                (1)

Proof: put T=R/(a^n). Since c=ab, c^n=0 in T. Start q0=-r and
iterate q_(j+1)=-r-c q_j^2/2 inside T. Consecutive differences gain
a factor c at each step:

    q_(j+1)-q_j=-(c/2)(q_j+q_(j-1))(q_j-q_(j-1)).

The first difference is divisible by c, so the iteration stabilizes
after finitely many steps. Its stable value q* satisfies
F(q*)=0 for F(Q)=r+Q+cQ^2/2. In T[Q],

    F(Q)=(Q-q*)[1+c(Q+q*)/2].                          (2)

The second factor is a unit because c is nilpotent. Therefore
T[Q]/(F)=T by Q mapping to q*, proving (1). This includes all
nilpotents and does not assume that a is irreducible or reduced.

The root is unique: for any roots q1,q2 in a T-algebra,

    (q1-q2)[1+c(q1+q2)/2]=0,

and the bracket is a unit. Uniqueness makes the isomorphisms (1)
compatible with reduction n+1 to n. Taking inverse limits gives
an isomorphism of the canonical a-adic completions.

If a is a unit, these quotients are the zero ring and the assertion
is vacuous; the interesting case is nonunit a.

## 3. The complement is matched by a different map

Let C0=ker D. On B_a, the genuine automorphism

    Phi=exp[-v(D/a+br partial_t)]

fixes C0 and sends t to u, as proved in688. It consequently induces
a C0-algebra isomorphism

    R_a --> A_a.                                       (3)

This is not in general the natural R-to-A map used in (1).
In particular Phi(r)=r-cv=-q, so (3) sends r to -Q, while the
natural inclusion sends r to r=-Q-cQ^2/2.

Thus (1) and (3) supply separate formal and complement matches,
not a compatible global map. The difference cannot simply be dropped
as higher order. The next section gives actual polynomial rings for
which no C0-normalizing global comparison can exist at all.

## 4. No whole repair can preserve the old invariant plane in the controls

For any integer m>=3 take

    D=x^2 partial_y+m y^(m-1) partial_z,
    a=x, b=1, r=y, g=x^2 z-y^m, C0=C[x,g].

As verified in688, ker D=C0 and (x,q,z,u) are whole polynomial
coordinates. Setting W0=-Q identifies the quotient with C[x,W0,Z],
where the embedded old invariant g is

    g=x^2 Z-(W0-xW0^2/2)^m.                            (4)

Suppose there were an automorphism theta of B with theta(t)=u
and theta(C0)=C0. It would induce an isomorphism psi:R-->A with
psi|C0=zeta an automorphism of C0. We show this is impossible.

Consider the two maps Spec R and Spec A to Spec C0. Their fibers
over (x,g) have the same compact-support Euler characteristic:

    chi_c=m on {x=0,g!=0};  chi_c=1 everywhere else.     (5)

For x!=0 each fiber is an affine line, with free coordinate y or
W0. At x=0,g!=0 it consists of m disjoint affine lines, indexed
by the distinct mth roots of -g. At (0,0) its underlying reduced
space is one affine line. The potentially nonreduced fiber at the
origin does not alter this topological Euler computation.

An isomorphism psi over zeta preserves (5). Therefore zeta
preserves the punctured line {x=0,g!=0}, its closure {x=0}, and
the unique missing point (0,0). Every plane automorphism with
these properties has the form

    zeta(x)=lambda x, zeta(g)=mu g+P(x),
    lambda,mu in C*, P in C[x], P(0)=0.                 (6)

Indeed preservation of the prime line ideal makes zeta(x) a
constant multiple of x. An automorphism over C[x], after undoing
that scaling, has degree one in g and unit leading coefficient
in C[x], hence a nonzero constant. Fixing the origin gives P(0)=0.

Invert x. Source and target are one-variable polynomial rings
over C0_x. A semilinear isomorphism over zeta must send

    y |--> kappa x^k W0+beta,
    kappa in C*, k in Z, beta in C0_x.                 (7)

The same two-sided saturation argument as in688 gives k=0 and
beta in C0. For clarity, a negative minimum x-order in (7) cannot
cancel: its coefficient at x=0 is a nonzero multiple of W0,
a nonzero polynomial in -W0^m, or their nonzero sum. For the
inverse the linear coefficient is a nonzero constant times x^-k,
even with zeta acting on coefficients. Applying the identical
argument in C[x,y,z] gives -k>=0. Thus both sides force k=0.

Apply psi to g=x^2z-y^m and use (4) and (6). Since lambda^2 x^2
psi(z) is divisible by x^2, so is

    (kappa W0+beta)^m-mu(W0-xW0^2/2)^m+P(x).           (8)

Reduction modulo x gives kappa^m=mu and beta=x beta1, with
beta1 in C0. This follows as in688: an mth root of mu W0^m
is a constant multiple of W0, whereas beta(0,-W0^m) has no
linear term. The coefficient of x in (8) must then vanish:

    m kappa^(m-1) W0^(m-1) beta1(0,-W0^m)
        +(mu m/2) W0^(m+1)+P'(0)=0.                  (9)

Evaluating at W0=0 forces P'(0)=0. Cancelling the nonzero
factor m kappa^(m-1) W0^(m-1) gives

    beta1(0,-W0^m)=-kappa W0^2/2,

impossible for m>=3. This proves nonexistence of theta.

The same argument directly excludes every isomorphism R-->A
which maps the embedded C0 onto the embedded C0. This is not
an exclusion of abstract isomorphisms: both rings here are C^[3].
Any repair completing u must move the old invariant plane to a
different subalgebra, not merely reparametrize that plane.

## 5. Exact implication for the research route

The formal/complement matches (1)-(3) are present for all the
quadratic data, including these controls. The controls admit no
whole invariant-plane-normalizing match. Therefore separate
matches cannot be promoted to a whole such match without a
compatibility or algebraization proof. Checking higher finite
jets of the natural inclusion cannot establish the missing step:
all finite levels already match automatically by Section2.

This does not prove that no unrestricted gluing or transverse
construction works. In the controls an unrestricted completion
already exists. For general rank-three D it remains necessary to
construct a whole completion allowed to change the old invariant
subalgebra, or supply a different valid recognition argument.
The general sliced extension is still unrecognized.

## 6. Verification and status

The proofs use nilpotent contraction, factorization, full fiber
strata, and an all-degree polynomial-isomorphism argument.
Fresh unsaved root9cfb38 checked both concrete inverse orders,
thickening identities for n=1,...,8, and first-jet identities for
m=3,...,9. These samples supplement the all-n and all-m proofs;
they do not replace them. No saved checker was run, imported,
compiled or edited. No novelty, formal-certification, expert-review,
or general-cancellation claim is made.

## 7. Complete-source internal review

Held mathematical source: 184 lines, SHA256
c859341a52bb7f7e9beb9722a87a77ddb6c1ceb3cb29dd47fb0c6657e3340255.
Root full EOF read f1cfa6. General full EOF/hash b189ff; Jet full
EOF37ba9e and final hash edbafb; Geometry full EOF e8b7c8 and
final hash e5aba7. All three returned CLEAN on the entire saved
source at its unchanged hash. Only this provenance section was
appended afterward. These are internal AI proof reconstructions,
not human peer review, formal certification, or novelty clearance.
