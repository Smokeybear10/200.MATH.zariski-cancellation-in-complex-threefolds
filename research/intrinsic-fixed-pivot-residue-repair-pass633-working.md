# Fixed-pivot residue repair for two commuting intrinsic actions

Private source-dependent working proof, September 17, 2026. This is a
conditional reduction on the actual unknown stably polynomial threefold.
It does not assert that its lifting condition always holds. General
cancellation remains UNSOLVED; novelty is UNKNOWN.

## 1. Input and the exact remaining condition

Let A be an affine complex domain with A[u] isomorphic to C^[4].
Suppose P,Q are commuting nonzero locally nilpotent derivations of A,
independent over Frac(A), and P is primitive: no nonunit divides all
of its values in the UFD A. The cylinder gives this factoriality.
The actual quotient-plane theorem retained in
[the intrinsic quotient note](intrinsic-quotient-surface-pass.md)
gives ker(N)=C^[2] for every nonzero LND N on A. The full plinth
principality proof in [27](intrinsic-plinth-boundary-pass27.md)
also applies on this actual A, not on a presumed polynomial three-ring.

There are actual plane coordinates f,g with

    S=ker(P)=C[f,g],
    Q|_S=q(f) partial_g,  q in C[f] nonzero,
    ker(P) intersect ker(Q)=C[f].                       (1)

Write pl(P)=p(f)S with p nonzero. The polynomial dependence of p
on f is proved below. If p is a unit, P already has a slice and
A=C^[3], so the unsolved case has p nonconstant.

For each F=f-c dividing q, both derivations descend to the domain
A/FA. On its fraction field there is a unique ratio kappa with

    Qbar=kappa Pbar,   Pbar!=0.                        (2)

The precise division criterion is

    kappa belongs to C[gbar]
      iff there exists H in S such that
      W=(Q-H P)/F maps A into A.                       (3)

Whenever (3) holds, W is a globally defined LND, it commutes with P,
is independent of P, and

    W(g)=q/F.                                         (4)

The lift in (3) is automatic when p(c)!=0. Thus all potentially
stalled roots lie over the pivot's plinth. At roots of p,
automatic lifting is FALSE even for primitive nonsliced commuting
actions on actual C^[3], as Section 7 proves. Invariance under
Pbar does not place the ratio in C[gbar] or even in C(gbar).

## 2. Actual plane coordinates and a polynomial plinth

Commutation makes Q preserve S. Its restriction is nonzero.
Indeed if Q killed S, then on a local-slice chart A_d=S_d[r]
it would be an S_d-linear LND, hence a multiple of partial_r.
That would make P and Q dependent over Frac(A), contrary to
the input. Here d is a nonzero local-slice value of P.

Rentschler's theorem on the ACTUAL plane S identifies that
restriction as q(f) partial_g in a coordinate system f,g. This
proves (1) without assuming an ambient coordinate in A or A[u].

The accepted plinth theorem provides a generator p in S and a
whole s in A with P(s)=p. Commutation implies

    Q(p)=P(Q(s)) belongs to pl(P)=pS.

For an LND of a characteristic-zero domain, divisibility of a
nonzero h into its derivative forces that derivative to vanish.
One direct proof uses derivation degree: if D(h)=h b!=0, then
deg_D(Dh)=deg_D(h)-1 whereas deg_D(hb)>=deg_D(h), a contradiction.
It follows that Q(p)=0, so p belongs to C[f], as stated.

On the pivot's local-slice chart put r=s/p. We have the actual
polynomial presentation and the full formulas

    A_p=C[f,p^(-1),g,r],
    P=partial_r,
    Q=q(f) partial_g+h(f,g) partial_r,
    h belongs to C[f,p^(-1),g].                        (5)

To see the last assertion, P(Qr)=Q(Pr)=0, so Qr=h is in S_p.
The formulas do not require a global slice for P.

## 3. Residual dependence and the exact polynomial-lift test

The common kernel C[f] is factorially closed in A, as an
intersection of kernels. Therefore F=f-c is irreducible in A;
since A is a UFD, it is prime. Also

    S intersect FA=FS.                                (6)

Indeed if a=Fb belongs to S, then 0=P(a)=F P(b), and hence b
belongs to S. This proves (6). In particular C[g]=S/FS injects
into A/FA, so gbar remains transcendental over C.

Primitivity makes Pbar nonzero: otherwise every value of P
would lie in FA. When F divides q, both Pbar and Qbar kill gbar.
The fraction field of A/FA has transcendence degree two over C,
and hence one over C(gbar). In characteristic zero its derivations
over C(gbar) form a one-dimensional vector space over Frac(A/FA).
This proves (2), allowing kappa=0 if Qbar=0. Commutation further
gives Pbar(kappa)=0. It does not put kappa in C[gbar].

For H in S the numerator Q-H P takes every value into FA if and
only if its residual derivation is zero. By (2) and Pbar!=0,
this holds if and only if kappa=Hbar. The image of S in A/FA
is exactly C[gbar]. This proves both directions of (3), including
necessity. If a lift exists, H may be chosen as a polynomial in
g alone. No rational lift or lift on a smaller open set suffices.

## 4. Why the repaired whole derivation is locally nilpotent

For any H in S, the numerator L=Q-H P on the chart (5) is

    L=q(f) partial_g+(h(f,g)-H(f,g)) partial_r.         (7)

It is triangular over C[f,p^(-1)] and therefore locally nilpotent.
For example, give g weight one and r weight larger than the
g-degree of h-H; L strictly lowers positive weight. Restricting
back to A proves local nilpotence of L on A.

If (3) holds, define W(a)=L(a)/F for a in A. These values belong
to A and satisfy the derivation rule because L does and F is a
nonzero invariant. In the fraction field,

    W^j(a)=L^j(a)/F^j,

since L(F)=0. Thus W is locally nilpotent on A. This is a whole
derivation proof, not an inference from a locally nilpotent
associated graded action. Finally P(H)=P(F)=0 and [P,Q]=0 give
[P,W]=0, while (4) follows from P(g)=0. Since q/F!=0, W is
independent of P and has the same common kernel C[f].

If p(c)!=0, the chart (5) contains the whole F-fiber:

    A/FA=C[gbar,rbar],
    Pbar=partial_rbar,
    Qbar=h(c,gbar) partial_rbar.

The denominator p evaluates to a nonzero complex scalar, so
h(c,gbar) is a polynomial in gbar. Taking H=h(c,g) proves the
automatic lift assertion. This argument makes no statement about
fibers where p(c)=0.

## 5. Finite termination if all required lifts succeed

Keep P, f and g fixed. After a successful repair replace Q by W.
All assumptions needed for (1)--(4) remain valid, and its new
q-polynomial is q/F. Its degree has dropped by one, counting
multiplicity. Thus successive successful repairs terminate in
at most deg(q) steps at an action Q_* with

    Q_*(g)=a in C*,  [P,Q_*]=0.                        (8)

The normalized action Q_*/a has the whole slice g, so the slice
theorem gives

    A=(ker Q_*)[g].                                   (9)

The intrinsic quotient theorem applies again and makes ker Q_*
an actual polynomial plane. P restricts to a nonzero LND on that
plane: if it vanished there, it would vanish on (9), since Pg=0.
Its kernel there is exactly C[f], by preservation of the common
kernel through every step. Rentschler's theorem therefore supplies
h_* with ker Q_*=C[f,h_*]. Consequently

    A=C[f,h_*,g],  A[u]=C[f,h_*,g,u].                  (10)

This is a genuine coordinate conclusion under the stated successful
lift premises. It does not assume the original u was an ambient
coordinate. Already constant q requires no repairs. Failed lifting
for a selected pair is not evidence that A is nonpolynomial; another
pair or a different method may still recognize A.

## 6. Existing successful control and deduplication

The elementary polynomial control already retained in
[561](saturated-commuting-leading-family-fiber-obstruction-pass561-working.md)
has A=C[a,b,c], P=partial_b and Q=c partial_b+a partial_c.
Then f=a, g=c, q=a, and modulo a the ratio is kappa=cbar.
The whole lift H=c gives

    (Q-cP)/a=partial_c.

The repaired action has slice c. This is the exact successful
operation previously printed in561, not a newly discovered example.
Its point is that an operation using a coefficient in ker P can
leave the invariant-field-saturated span of the original pair.
Saturation within C(f)-linear combinations cannot supply this repair.

The related actual-coordinate row-operation restriction in
[25](commuting-leading-pass25.md) remains valid; here triangularity
is proved on the compatible pivot chart, not assumed for arbitrary
leading-compatible coefficients. The denominator-cleared companion
in [26](fence-centralizer-sector-pass26.md) gives an independent
commuting action but does not assert its residue-liftability.
The old cross-frame saturation results do not prove (3) automatic.
A bounded archive audit found no previous statement combining this
fixed-pivot criterion with the decreasing degree of q. That is not
a novelty audit or a claim of priority for the elementary steps.

## 7. Automatic repair fails even with two nonsliced polynomial actions

Take the actual polynomial ring A=C[x,y,z] and the triangular LNDs

    P=x partial_y+2y partial_z,
    Q=x partial_y+(2y+1) partial_z.                    (11)

Their commutator is zero on each generator. Their determinant on
y,z is x, so they are independent over Frac(A). Both are primitive,
since gcd(x,2y)=gcd(x,2y+1)=1. Their fixed lines are respectively
x=y=0 and x=0,y=-1/2; thus neither has a slice. The cylinder
condition is satisfied here, not merely a weaker factoriality test.

Put g=xz-y^2. The exact kernels and cross-speed are

    ker P=C[x,g],
    ker Q=C[x,g-y],
    Q(g)=x.                                          (12)

For the first kernel, inverting x gives A_x=C[x,x^(-1),g,y]
and P=x partial_y. If an invariant has a minimal expression
x^(-d) F(x,g) with d>0, polynomiality would give
F(0,-y^2)=0, which forces F(0,g)=0 and contradicts minimality.
The injective substitution C[g]->C[y], g->-y^2, justifies this
step. Hence the first kernel is exactly as printed. Replacing
y by y+1/2 conjugates the two triangular actions and gives the
second kernel (an added constant 1/4 does not change that ring).

Each full plinth is exactly x times its kernel. Indeed its
principal generator divides P(y)=Q(y)=x, so it is a unit or an
associate of x. A unit plinth would supply a slice, which the
displayed fixed line excludes. This uses the accepted plinth
principality theorem with its polynomial input fully satisfied.

For the fixed pivot P, (1) has f=x and q=x. On A/xA=C[y,z],

    Pbar=2y partial_z,
    Qbar=(2y+1) partial_z,
    kappa=1+1/(2y),   gbar=-y^2.                      (13)

The ratio has a pole at y=0, so it is not in C[gbar]. In fact
the involution y->-y does not fix it, so it is not in C(gbar).
There is an even more direct whole-polynomial obstruction: for
ANY polynomial H in A,

    (Q-HP)(z)=2y+1-2yH

equals 1 after setting x=y=0. It cannot be divisible by x. Thus
there is no polynomial repair in (3), even allowing coefficients
outside ker P. The degree-q procedure stops at its first root.

Nevertheless

    Q-P=partial_z                                    (14)

already has the whole slice z. This countercontrol proves that
one cannot promote the conditional criterion to a universal
fixed-pivot lifting theorem under the actual cylinder hypothesis,
even after requiring both starting actions to be primitive and
nonsliced. Changing the action pair is genuinely different from
insisting on the fixed pivot and fixed quotient coordinate g.

The first triangular action and its kernel are already in the
intrinsic quotient note. The control is a shifted pair of known
actions, not a claim to a new family or a cancellation counterexample.

## 8. Consequence for the research direction

The conditional repair theorem remains valid, including its strict
termination measure. But a universal proof that the required lift
always exists is ruled out, not merely awaiting proof. Any viable
general argument along this route must allow a change of pair,
produce a slice by a different operation, or justify an additional
selection condition not contradicted by (11)--(14). No such
unconditional selection theorem is proved here. The original
cancellation objective remains unchanged and unresolved.

No public contact, human review, or Lean certification has occurred.
A complete independent saved-source review is required before
acceptance; finite algebra checks supplement the uniform proof.
