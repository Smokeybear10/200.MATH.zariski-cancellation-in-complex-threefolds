# The quadratic construction preserves the entire inherited plinth

## 1. Exact statement

Let R=C[x,y,z], let D be a nonzero locally nilpotent derivation,
and put C0=ker D. Choose a minimal local slice rho with

    D rho=P, pl_R(D)=P C0, P!=0.

The standard three-variable kernel and plinth theorems give
C0 isomorphic to C^[2] and the displayed principal plinth.[^1]
No primitivity or squarefreeness is assumed. Take a,b in C0
minus zero and w in R with Dw=a^2 b. Set

    c=ab, B=R[t], E=D+(1+cw)partial_t, K=ker E.

Use the whole slice and quadratic quotient from688:

    v=at-w^2/2, u=t-bwv+(ab^2/2)v^2,
    K isomorphic to A=R[Q]/(w+Q+cQ^2/2), K[u]=B.

The inherited action on K is delta=-partial_t restricted to K;
on A it is delta|R=(1+cQ)D, delta Q=-a^2b. Its kernel is
the SAME embedded C0, as proved in688. Then

    pl_K(delta)=P C0=pl_R(D).                         (1)

This is equality with every prime multiplicity retained, not just
equality of support or of fixed schemes. It holds even when
polynomiality of K is not known. If D has invariant content gamma,
the inherited action has exactly the same content gamma, and its
primitive normalization also has unchanged full plinth.

Thus iterating this construction along its inherited action does
not lower plinth multiplicities or create a new invariant kernel.
The result rules out this proposed progress measure. It is not
a recognition theorem for K and does not settle cancellation.
General cancellation is UNSOLVED; novelty is UNKNOWN.

## 2. The original first degree module and its local saturation

Every element f with D^2 f=0 satisfies Df=qP for q in C0;
then f-q rho belongs to C0. Hence

    ker D^2=C0 direct-sum C0 rho.

In particular write w=h rho+k, h,k in C0, h!=0, so

    hP=a^2 b.                                       (2)

For a prime pi in C0 dividing P, let O=(C0)_(pi) and
kappa=Frac(C0/(pi)). The element pi is prime in R because
C0 is factorially closed in the UFD R. Thus R_O/(pi) is a
domain containing kappa.

The elements 1 and rhobar are linearly independent over kappa.
Otherwise rhobar belongs to kappa. Lift this scalar to k in O;
then rho-k=pi f for f in R_O. Applying D gives Df=P/pi.
But the full plinth localizes to P O, a contradiction.

Here localization of the full plinth needs no extra theorem:
if D(r/s) belongs to O, with r in R and s in C0 outside(pi),
then D^2 r=0. Thus Dr belongs to P C0, and D(r/s) belongs
to P O. The opposite inclusion is immediate. This argument
also covers primes coming only from a nonprimitive multiplier.

## 3. An explicit minimal slice for the inherited action

Define elements of R and K respectively by

    J=(1+ck)rho+(ch/2)rho^2,
    S=J-Pt.                                         (3)

Direct differentiation gives

    DJ=P(1+ck+ch rho)=P(1+cw), E S=0, delta S=P.

Consequently P C0 is contained in pl_K(delta).

Conversely, let z belong to pl_K(delta) and choose F in K
with delta F=z. Since z belongs to ker delta=C0 and delta
is -partial_t on K, F=f0-zt for f0 in R. The equation EF=0
is exactly

    D f0=z(1+cw).                                   (4)

Over L=Frac(C0), the local-slice theorem gives R tensor L=L[rho].
Integrating (4) there, or subtracting the known derivative DJ,
gives

    f0=(z/P)J+beta, beta in L.                       (5)

Fix any prime pi dividing P. Equation (2) implies pi divides
c=ab: if neither a nor b were divisible by pi, its right side
would be a unit at pi whereas hP would not be. Therefore

    Jbar=rhobar in R_O/(pi).

If the smaller pi-valuation of z/P and beta were negative,
multiply (5) by the smallest positive power of pi that makes
both coefficients integral. Its left side reduces to zero,
whereas its right side reduces to a nonzero kappa-linear
combination of 1 and rhobar. Section2 excludes this. Thus
z/P belongs to O for every prime pi dividing P. Since z and P
belong to the UFD C0, P divides z globally. This proves (1).

It also proves the complete first degree module of delta:

    ker_K delta^2=C0 direct-sum C0 S.                (6)

Indeed if delta F=qP, subtract qS; the difference is in C0.
The sum is direct since delta S=P is nonzero.

## 4. The quotient formula and unchanged boundary actions

In A, the inverse quotient map from688 sends

    t to t0(Q)=bQ^3/2+ab^2Q^4/8,
    w to -Q-cQ^2/2.

Substitution in (3), using h rho=w-k and hP=a^2b, yields
the useful WHOLE identity

    hS=-Q-k-ck^2/2.                                 (7)

Although solving this formally for S displays a denominator h,
S is already polynomial by (3). Equation (7) identifies precisely
why Q need not be a minimal local slice: delta Q=-hP.

For every prime pi dividing P, reduction of the defining relation
gives Q=-w, since pi divides c. Consequently the natural map

    R/(pi) --> A/(pi)

is an isomorphism. Under this isomorphism the induced derivations
also agree: delta|R=(1+cQ)D reduces to D. Hence the boundary
invariant rings and invariant-field extensions over C0/(pi)
are unchanged. This conclusion uses the quotient presentation,
not a claim that the unreduced old-DVR localizations are isomorphic.
The latter claim is explicitly false in693.

## 5. Primitive normalization cannot hide an improvement

Write D=gamma D0 with D0 primitive. The gcd gamma of the
coordinate coefficients is invariant, by the standard content
property of LNDs; thus gamma belongs to C0. Put d0=D0w, so
gamma d0=a^2b and c^2=b gamma d0. On A define

    delta0|R=(1+cQ)D0, delta0 Q=-d0.

Then delta=gamma delta0. It preserves the defining relation,
and gamma is invariant. As delta is LND and A is a domain,
delta^n f=gamma^n delta0^n f proves that delta0 is LND.

Let J0 be the ideal generated by D0(R) in R and W=1+cQ.
The fixed ideal of delta0 is (W J0,d0)A. The exact identity

    1=W(1-cQ)+b gamma Q^2 d0

shows that this ideal is J0 A. In R/J0, d0=0 and c^2=0.
The factorization at Q0=-w-cw^2/2 from688 has a unit second
factor, so A/J0 A is isomorphic to R/J0, including nilpotents.

Both R and A have dimension three. The latter is a smooth UFD
because A[u]=C^[4]; factoriality here descends from a polynomial
extension and does NOT assume A=C^[3]. Since D0 is primitive,
R/J0 has dimension at most one (or the fixed scheme is empty).
The same is true of A/J0 A, so delta0 has no divisorial common
factor. It is primitive. Thus gamma is exactly the inherited
content, up to a scalar. Finally

    pl(delta)=gamma pl(delta0), pl(D)=gamma pl(D0)

and (1) allow cancellation of gamma, giving
pl(delta0)=pl(D0) in the same embedded C0.

## 6. Remaining gap

The construction can change the total ring while retaining its
inherited kernel, primitive full plinth, and every generic boundary
action just described. These equalities do not identify the total
rings:693 supplies a globally polynomial control where even the
old height-one localizations are not isomorphic as C-algebras.

A strategy seeking simpler plinths therefore needs a genuinely
different action or another global invariant-moving operation.
This proof provides no such action and no reduction from an
arbitrary A[s]=C^[4] to the quadratic construction. It must not
be reported as the requested cancellation solution.

[^1]: N. Dasgupta and S. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables](https://arxiv.org/html/2306.00510v2), Theorems2.8 and2.10, recalling the kernel and full principal plinth theorems. The current full-plinth equality is proved directly above using these inputs and the whole construction688. It is not inferred from equality of fixed schemes.

## 7. Completed internal reconstruction

The held mathematical source had191 lines and SHA256
c1f8d28fa101622517ef3e05e9d0ea55b07f837fecc4179ef7dc73b73e1acd42.
Root read all of it in2f47de. Full-source AI reviews reported CLEAN:
General2da98d/81b6af, Geometry380b57, and Jet f86408/fb3d32.
Root and Geometry independently derived the plinth proof before
the saved note; all three reviewers subsequently reconstructed
the entire saved source, including its additional content and
boundary assertions. Fresh unsaved root490383 checked universal
derivative, quotient and nilpotent-factorization identities and
18 repeated-plinth controls. Jet fb3d32 independently checked the
universal identities. The universal theorem rests on the written
valuation and codimension arguments, not a finite search.
Only provenance was appended after these reviews. No saved
checker was executed, imported, compiled or edited. This is not
human expert review, formal certification or novelty clearance.
