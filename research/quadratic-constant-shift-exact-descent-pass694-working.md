# Exact invariant-constant repair and full-thickness descent

## 1. Scope and statement

Let R=C[x,y,z], let D0 be a primitive nonzero LND, let C0=ker D0,
and let D=lambda D0 with lambda in C0 minus zero. Suppose a,b
belong to C0 minus zero and w in R satisfies Dw=a^2 b. Set

    B=R[t], E=D+(1+abw)partial_t,
    v=at-w^2/2, u=t-bwv+(ab^2/2)v^2,
    d=a/gcd(a,lambda) in C0, up to a scalar.

For each candidate invariant constant c in C0, consider the
specified localized automorphism

    W_c=at-w^2/2+c,
    L=D/a+bw partial_t, N_c=-W_c L,
    Phi_c=exp(N_c) on B_a.                            (1)

**Exact criterion.** The following are equivalent for this c:

    Phi_c(B) subset B;
    Phi_c is a whole automorphism of B;
    d divides w^2/2-c in R.                           (2)

Thus SOME invariant constant repair exists if and only if the
class of w^2/2 in R/(d) lies in the embedded image of C0/(d).
If it exists, the set of successful c is one coset modulo dC0.

**Height-one descent.** Write d=unit*product pi_i^(q_i) in C0.
Such a global c exists if and only if, for EACH i, there exists
c_i in O_i=(C0)_(pi_i) with

    w^2/2-c_i belongs to pi_i^(q_i) R tensor_(C0) O_i. (3)

These are full-thickness congruences, not tests only modulo pi_i.
The c_i need not be selected as restrictions of one prechosen
constant; the proof constructs existence of a common global c.
There is no additional closed-point obstruction for this particular
fixed-square descent problem.

This classifies only the family (1). Failure does not imply u
is noncoordinate. The explicit controls below have whole coordinate
u even though EVERY c in (1) fails. General cancellation is still
UNSOLVED and mathematical priority UNKNOWN.

## 2. Local nilpotence, interpolation, and exact globality

On B_a, L is an LND, Lw=ab, Lt=bw, L^2t=ab^2, L^3t=0.
Also LW_c=0, since c is invariant. Thus N_c is an LND and (1)
is a genuine localized automorphism. Its coefficients are

    N_c|R=[-t+(w^2/2-c)/a]D,
    N_c(t)=-bwW_c.                                    (4)

The t coefficient is whole. Primitivity of D0 implies that its
coordinate coefficients have gcd1. Hence (4) preserves B exactly
when a divides lambda*(w^2/2-c), equivalently when the third
condition in (2) holds. The gcd and divisibility can be taken in
C0 for a,lambda because C0 is factorially closed in the UFD R;
no additional common prime factors appear in R.

If N_c preserves B, local nilpotence descends from B_a, and
exp(+/-N_c) are mutually inverse whole maps. Conversely suppose
only Phi_c(B) subset B. For each original generator h, the finite
polynomial exp(T N_c)(h) has its values at all nonnegative integers
in B, since exp(j N_c)=Phi_c^j. A rational Vandermonde inverse
at finitely many integers recovers every coefficient in B. In
particular N_c(h) is whole. This proves all implications in (2)
without assuming an inverse in the starting hypothesis.

As in691, E=aL+partial_t, EW_c=a, and [E,L]=0. It follows that

    E Phi_c=Phi_c partial_t,
    s_c=Phi_c(t)=t-bwW_c+(ab^2/2)W_c^2.                (5)

When (2) holds, the kernel is Phi_c(R), a polynomial three-ring.
The supplied u also satisfies Eu=1, so u-s_c lies in that kernel
and u is a whole coordinate by an invariant triangular shear.
No equality s_c=u is assumed when c is nonzero.

For primitive D itself, the positive criterion has an elementary
form too: (w^2/2-c)/a is whole and E sends t-(w^2/2-c)/a to1.
The replica statement in (2) allows cancellation by lambda and
need not have this same whole primitive in R.

## 3. Full-thickness local constants DO descend globally

We use the established three-variable facts C0 is a polynomial
two-ring and R is faithfully flat over C0.[^1] In particular

    I R intersect C0=I for every ideal I of C0.         (6)

If d is a unit, (2) is automatic and there are no local tests.
Suppose d is a nonunit. The total quotient ring of S=C0/(d)
is the product of its Artin local rings at the minimal primes,

    Q(S)=product_i O_i/(pi_i^(q_i)).                   (7)

For this elementary principal hypersurface statement, the only
associated primes are the pi_i, and localizing away from their
union gives a zero-dimensional Noetherian ring. Its finitely many
local factors are exactly the displayed rings, retaining q_i.

Assume (3). The tuple of local constants defines an element of
Q(S). Represent it as c0/s, with c0,s in C0 and s a nonzerodivisor
modulo d. Thus s has no prime factor pi_i in common with d.
Every pi_i is prime in R, by factorial closure. The local tests
and the chosen representation imply that

    s*w^2/2-c0 belongs to dR.                         (8)

Indeed after localization at C0 minus (pi_i), this difference is
divisible by pi_i^(q_i). A cleared invariant denominator is not
divisible by pi_i in R, so this divisibility holds already in R.
Taking all i gives (8) in the UFD R.

Now c0 belongs to (d,s)R intersect C0. By (6), write
c0=d c1+s c2 with c1,c2 in C0. Substituting in (8) gives

    s*(w^2/2-c2) belongs to dR.

Since s and d have no common prime factor in R, d divides
w^2/2-c2. This is the desired global constant. The reverse
implication follows simply by localization.

Finally dR intersect C0=dC0, again by (6), so any two successful
constants differ by an element of dC0, and every such difference
preserves the condition. This proves the stated coset assertion.

No claim that the ideals (d,s) and C0 are equal was used: having
no common prime factors is not comaximality in a polynomial plane.
Faithful-flat contraction is exactly the step that handles those
possible intersection points.

## 4. Exact local residue and quadratic-model tests

Choose a minimal local slice D0rho=p generating its full principal
plinth. Then w=h rho+k with h,k in C0, h!=0, and

    a^2 b=lambda h p.

Fix a prime pi dividing d, put O=(C0)_(pi), q=v_pi(d), and let
H=v_pi(h), K=v_pi(k), with K=infinity if k=0. Write bars for
reduction modulo pi in R_O.

If 1,rhobar,rhobar^2 are linearly independent over
kappa=Frac(C0/(pi)), then (3) is equivalent to

    q<=min(2H,H+K).                                  (9)

Indeed the valuation of any quadratic expression in rho is the
minimum of its three coefficient valuations: divide by that power
of pi and use the displayed residual independence. Apply this to
h^2 rho^2/2+hk rho+(k^2/2-c). The two nonconstant coefficient
valuations give necessity, and c=k^2/2 gives sufficiency. In
particular when h is a unit, no positive q can pass this test.

For a nonbase algebraic residue wbar, the condition wbar^2 in
kappa requires degree2 AND trace(wbar)=0. Merely knowing degree2
is insufficient. If the residue is transcendental, its square
cannot be in kappa either.

A full-thickness quadratic test is available under the stronger
ACTUAL presentation hypothesis

    R_O=O[rho,Z], pi^P Z=rho^2+alpha rho+beta,
    alpha,beta in O, P=v_pi(p),                       (10)

with the displayed monic relation defining the ring. Then

    w^2/2=h^2 pi^P Z/2
             +(hk-alpha h^2/2)rho+(k^2-beta h^2)/2.

The normal form has basis1,rho over O[Z]. Admissibility makes
2H+P>=q: if A=v_pi(a), L0=v_pi(lambda), then q=A-L0>0 and
2A<=L0+H+P implies 2q+L0<=H+P. Consequently (3) is exactly

    hk-alpha h^2/2 belongs to pi^q O.                 (11)

One can choose c=(k^2-beta h^2)/2 locally. Condition (10) is not
inferred merely from a quadratic intermediate residue field.
The retained tower examples622/670 show why that inference fails.

## 5. Whole controls rejecting reduced-only and degree-only tests

A positive control shows that the freedom in c can genuinely help.
For any j>=1 take D=x^(2j)partial_y+2y partial_z,
g=x^(2j)z-y^2, a=x^j,b=1,w=y. The fixed choice c=0 fails,
but c=-g/2 gives w^2/2-c=x^(2j)z/2, divisible by a. Thus
s=t-x^j z/2 is a whole coordinate slice. This does not claim
that all failures of the sufficient criterion692 can be repaired.

For a negative control take D=x^2 partial_y+2y partial_z, with
g=x^2z-y^2, C0=C[x,g], a=x,b=1,w=y+1. The residue ybar over
C(g) has degree2, but (ybar+1)^2=-g+2ybar+1 is not in C(g).
Thus no invariant c gives a whole Phi_c, despite the quadratic
residue degree. The missing condition is trace cancellation.

More strongly take

    D=x^4 partial_y+(2y+x)partial_z,
    g=x^4 z-y^2-xy, C0=C[x,g], a=x^2,b=1,w=y.          (12)

The reduced test passes: y^2=-g modulo x. But no invariant c
works modulo x^2. Any candidate must have, modulo x^2,
c=-g/2+x c1(g). Then

    y^2-2c=-x[y+2c1(-y^2)] mod x^2,

which cannot vanish, since 1,y are independent over C(y^2).
The same contradiction allows c1 rational over the residue field,
so even the height-one thickness-two test fails. This is not a
failure caused only by a closed intersection point.

For exact kernel and plinth in (12), center Y=y+x/2 and
G=g-x^2/4=x^4z-Y^2. Then D=x^4 partial_Y+2Y partial_z.
Invariant localization and independence of1,Y modulo x give
ker D=C[x,G]=C[x,g] and ker D^2=C0 direct-sum C0 Y;
the full plinth is therefore x^4 C0. The first control has the
identical argument with x^2 in place of x^4. Both fields are
primitive because their displayed coefficients have gcd1.

In BOTH controls u is nevertheless a whole coordinate. Since
b=1 and a is a polynomial in x, set q0=av-w and use coordinates
(x,q0,z,u). Their polynomial inverse is

    V'=a U-Q^2/2, w=aV'-Q,
    t=U-QV'+a(V')^2/2,

with y=w-1 in the first control and y=w in the second. This
completes the positive check without an external recognition
theorem. Failure of (1) excludes only the entire invariant-
constant-shift exponential family, not every coordinate completion.

## 6. Research consequence

The local-to-global assertion in Section3 concerns one fixed
element w^2/2 and constants in an embedded faithfully flat base.
It does not supply old-invariant DVR rectifications, which693
shows may be impossible even for globally solved examples. Nor
does it remove point defects from unrelated image-module or
simultaneous generator-selection problems.

The constant-shift search can now be decided by exact generic-
divisor tests with the full multiplicities. When it fails, a
successful completion must leave this exponential family. The
remaining general construction, and the reduction from arbitrary
A[s]=C^[4], are not supplied by this criterion.

[^1]: N. Dasgupta and S. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables, primary version2](https://arxiv.org/html/2306.00510v2), Theorems2.8 and2.10(i), recalling the polynomial kernel and faithful flatness. The proof uses the whole faithfully flat inclusion, not flatness on only a principal open. The interpolation mechanism is retained from688; the current statement permits all invariant constants and retains nonreduced congruences.

## 7. Completed internal reconstruction

The mathematical source held for review had251 lines and SHA256
ae8aac6c37101a01d9a50f3874c3106e94d1b7bf3ec830f9da96b2f72601bd18.
Root read the full held source inac7e2d and again ind19867.
Three independent full-source AI reviews reported CLEAN:
General325222/9bae98, Jet b03e20/aaa3c8, and Geometrybc84b7.
Fresh unsaved root7ee0ca checked both universal coordinate inverses,
the thickness-two obstruction, its centering identity, and the
positive elementary-slice controls for j=1 through5. Full-thickness
descent rests on the written faithful-flat contraction proof, not
those finite calculations. Only this provenance was appended after
the reviews. No saved checker was executed, imported, compiled or
edited. These reviews are not human expert review, formal
verification, or confirmation of novelty.
