# All additive actions lift on the two-stage special fiber

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This note removes the unproved action-lifting premise in677 for its specific
threefold. It does not classify all lifted actions or prove polynomiality
of the original cylinder. The new reduction concerns the special fiber,
not every global action on the fourfold in676.

## 1. Statement and notation

Set

    C0=C[V,b,S,T]/(V²T+b³S+V), X=Spec(C0),
    I=(V,b), P=V(I), z=VT, j=1+VT,
    Ctilde=C[p,q,v,w,T]/(q³w-p³vT-1).

Give Ctilde the integer grading

    deg(p,q,v,w,T)=(1,-1,-3,3,0).

As proved in677, its degree-zero subring is C0, with

    b=pq, V=p³v, S=-vw, T=T.                              (1)

Here the grading is genuinely the divisor-class grading: Pic(X)=Z[P],
and Ctilde is the direct sum of the sections of O_X(nP), n in Z. Every
additive-group action on X lifts uniquely to Ctilde preserving this grading.
Equivalently, restriction gives a bijection

    {degree-zero LNDs of Ctilde} -> {LNDs of C0}.           (2)

Under (2), preservation of I is equivalent to the lifted LND killing p.
Whether EVERY degree-zero LND kills p remains UNPROVED.

A second result excludes a particular construction, not all actions:

    If D is an LND of C0 and D(H) is contained in H,
    where H=C[b,VT,-ST], then D=0.                        (3)

Thus a base-preserving factorization lift cannot give the desired action.

## 2. Divisors, units, and the Picard group

The ring C0 is a smooth domain. Primitivity and linearity in S prove
integrality. The partial derivatives with respect to S and T are b³,V²;
if both vanish, V=b=0, where the V-derivative is 1.

The divisor b=0 is reduced and has exactly two disjoint components:

    P=(b,V), with coordinate ring C[S,T],
    E=(b,1+VT), with coordinate ring C[V,V^(-1),S].

Indeed C0/bC0=C[V,S,T]/(V(1+VT)), and the two factors are comaximal.
Both components occur with multiplicity one. On the j-chart,
V=-b³S/j and P has ideal (b). On the z-chart V and T are units, P is
absent, and E is locally b=0. Consequently

    div(b)=P+E.                                          (4)

Localizing at b gives C0_b=C[b,b^(-1),V,T], a UFD whose units are exactly
c*b^n, c in C*, n in Z. A unit of C0 must have order zero at both P and E,
so C0*=C*.

Here is the divisor-class localization calculation in full. Every Weil
divisor becomes principal after restriction to X_b, since that chart is
factorial. Subtracting that principal divisor leaves an integer combination
of P and E. A relation between these two divisors must be the divisor of
a rational function having no zero or pole on X_b. In a Laurent polynomial
UFD such a function is a unit c*b^n, and its divisor is n(P+E). Hence

    Cl(X)=(Z[P]+Z[E])/(Z([P]+[E]))=Z[P].                 (5)

The identical calculation for C0[t1,...,tr] gives the same generators and
relation, and only constant units. Its smoothness identifies its Picard
group with its divisor class group. In particular restriction at t=0 is an
isomorphism Pic(X times A1) -> Pic(X), as is the analogous restriction for
two parameters. For the standard Picard/class-group identification see
[Stacks, Lemma 31.28.7](https://stacks.math.columbia.edu/tag/02SE), together
with [regular local factoriality](https://stacks.math.columbia.edu/tag/0FJH).
We have proved the polynomial-extension assertion here rather than assuming
an unverified homotopy-invariance hypothesis.

## 3. Explicit principal multiplicative-group bundle and Cox ring

The opens X_j and X_z cover X because j-z=1. There are graded isomorphisms

    Ctilde_j=C0_j[q,q^(-1)],
    p=b/q, v=-S*q³/j, w=j/q³;                            (6)

and

    Ctilde_z=C0_z[p,p^(-1)],
    q=b/p, v=V/p³, w=-S*p³/V.                            (7)

In (6), q is a unit because q³w=j is a unit. In (7), p is a unit because
p³vT=z is a unit. The displayed formulas verify the relation and (1) in
both directions; their only denominators are declared units. These are
local trivializations of a principal Gm-bundle Spec(Ctilde) -> X.

For each integer n, send a degree-n element f to the degree-zero rational
function f/p^n. On X_j, the degree-one generator q^(-1) maps to 1/b. On
X_z, the degree-one generator p maps to 1. Since the Cartier divisor P
is b=0 on X_j and is empty on X_z, these are exactly the local generators
of O_X(P). All other degrees are tensor powers, including the negative
ones. The maps agree on the overlap and with multiplication, proving

    Ctilde = direct_sum_(n in Z) Gamma(X,O_X(nP)).         (8)

Thus the auxiliary ring is the Cox ring for the chosen generator [P] of
Pic(X), with a specified multiplicative identification, not just a ring
whose invariant subring happens to be C0.

The pulled-back ideal of P is exactly (p). In addition to the containment
(b,V)Ctilde contained in (p), use the whole-ring identity

    p=(q²w)b-pTV.                                        (9)

This follows by multiplying q³w-p³vT=1 by p. The quotient by (p) is
C[q,q^(-1),v,T], whose degree-zero part is C[S,T]; therefore
(p) intersect C0=I as well.

## 4. Every additive action lifts, without a fine-grading assumption

Let mu:Ga times X -> X be an arbitrary algebraic additive-group action,
and let L=O_X(P). On Ga times X compare mu*L with pr_X*L. Restriction at
the identity 0 gives L in both cases. Section2 shows that this restriction
is an isomorphism of Picard groups, so the two line bundles are isomorphic.

Choose an isomorphism and normalize its restriction at t=0 to the identity.
This normalization is possible because automorphisms of L are multiplication
by units of C0, hence by nonzero constants. Over Ga times Ga times X, the
two composites required by the group-action cocycle identity are isomorphisms
between the same line bundles. Their ratio is a unit of C0[s,t], hence a
constant. At s=t=0 this ratio is 1. The cocycle identity follows everywhere.

This gives an algebraic Ga-linearization of L and of every tensor power.
Taking the direct sum in (8) gives a Ga-action on Ctilde that preserves
each graded part and induces mu on degree zero. Its infinitesimal generator
is a degree-zero LND. This proves existence in (2).

For uniqueness, the normalized bundle isomorphism above is unique: two
choices differ by a constant unit on C0[t], and their identity restrictions
make that constant 1. This proves injectivity in (2). As a separate check,
a degree-zero LND vanishing on C0
extends after invariant localization to

    Frac(C0)[p,p^(-1)].

It must kill the unit p as well as the coefficient field, so it is zero.
This excludes vertical additive actions invisible on X. It is not an
alternative proof of injectivity by subtracting two LNDs, since their
difference need not be locally nilpotent.

If an action on X preserves I, its lift preserves I*Ctilde=(p), by (9).
For an LND, divisibility of D(p) by p forces D(p)=0. Conversely D(p)=0
preserves (p) and therefore its contraction I. This proves the equivalence
stated after (2).

None of this makes a degree-zero LND homogeneous for the finer Z³-grading
in677. The fine-homogeneous classification in Krasikov--Rassolov
[Theorem 2.2](https://arxiv.org/html/2605.17670v1) does not classify every
LND in (2). The interior-degree obstruction in677 still applies.

## 5. A factorization-preserving action is necessarily zero

Put h=-ST. Then

    b³h=z(z+1), z=VT.                                    (10)

The resulting map

    C[b,z,h]/(b³h-z(z+1)) -> C0

is injective. After inverting b its source is C[b,b^(-1),z], which embeds
in C[b,b^(-1),V,T] by z=VT. Both unlocalized rings are domains.
Its image is precisely H.

Suppose D is an LND of C0 preserving H. Its restriction to H is an LND.
Poloni's [Theorem 3.2](https://arxiv.org/pdf/0912.3241) applies to the
Danielewski equation with exponent 3 and residual polynomial z(z+1).
It gives, allowing alpha=0 for the zero derivation,

    D(b)=0, D(z)=alpha(b)b³,
    D(h)=alpha(b)(2z+1), alpha in C[b].                   (11)

Now reduce D(z)=T D(V)+V D(T) modulo (V,S,T). The quotient C0/(V,S,T)
is C[b]. The left side becomes zero, so alpha(b)b³=0 in C[b], and alpha=0.
Thus D kills H. Factorial closure of the LND kernel applied to the nonzero
products VT and ST forces it to kill V,T,S separately. It also kills b,
so D=0, proving (3).

Upstairs consider the factorization subring

    Dbase=C[p,q,e=vT,w] inside Ctilde.

It is isomorphic to C[p,q,e,w]/(q³w-p³e-1): injectivity can be checked
after inverting T, where v=e/T. Its degree-zero subring is H, with
z=p³e and h=ew. For generation of that invariant subring, remove powers
of ew from a weight-zero monomial p^i q^j e^k w^l. If k>=l the remainder
is generated by pq and p³e; if l>=k it is generated by pq and q³w=1+p³e.

A degree-zero LND of Ctilde preserving Dbase therefore restricts to an
LND of C0 preserving H. It vanishes on C0 by (3), then vanishes upstairs
by Section4. Thus there is NO nonzero such factorization-preserving lift.
Preservation of Dbase is an explicit additional premise, not an automatic
property of a degree-zero LND.

## 6. Exact geometry of the complement, with an extension warning

The open complement X minus P is the affine threefold

    Y={VU+b³W=1} inside A4_(V,b,U,W).                     (12)

Its map to X fixes V,b and sets T=-U, S=-VW. The equation forces V,b not
to vanish simultaneously, so the image avoids P. The inverse is U=-T,
with W=-S/V on X_V and W=(1+VT)/b³ on X_b. These expressions agree by
the equation of C0 and give both inverse compositions.

After changing a sign, (12) is the standard X_(1,3) in Dubouloz--Finston,
[*On exotic affine 3-spheres*](https://arxiv.org/pdf/1106.2900), Sections
1.2--1.3 and Theorem 2.3. Their Remark1.4 states flexibility of this family.
That conclusion is about the OPEN COMPLEMENT. It does not extend every
one of its actions across P and does not prove flexibility of X or of the
original cylinder.

For example, on Y the triangular LND

    delta(V)=b³, delta(W)=-U, delta(b)=delta(U)=0

does extend to X, but gives exactly D1 of677:

    D1(V)=b³, D1(S)=-(2VT+1), D1(b)=D1(T)=0.

It preserves P. The familiar complement action therefore supplies no new
escaping action. A different complement action would need a checked whole
extension, including local nilpotence, before it could be used here.

## 7. Verification and what remains

Root derived Sections2--4; General independently reconstructed the Picard
calculation, both bundle charts, the Cox identification, and the normalized
action-lifting proof. General derived the factorization obstruction in
Section5. Geometry supplied the complement identification in Section6.
These are internal AI reconstructions, not expert or formal verification.

Root's fresh unsaved calculation adcf3b checks both torsor charts, their
quotient maps, the complement maps and overlap, equation(10), ideal
identity(9), and the displayed lift of D1. An initial check f7ac73 stopped
because it compared an expanded polynomial with an unexpanded expression
using structural equality. Expanding their difference corrected that test;
the mathematical identity was unchanged. No saved checker was used.

The complete 263-line source was held at SHA256
6650e302c6fb45ab503f8bc5fe95998d18eed78f29ad36781657eed6dedd0096.
General read it through EOF in6da4e8/e69c93 and reread it inea25a1, with
final hash7d980f. Geometry's complete reads weref092f4/0117f5, with final
hash7ef664. Jet's complete read was212773, with final hashe4b948. All three
reconstructed the full proof and its source scopes. General requested the
Section4 clarification distinguishing uniqueness of linearization from
absence of vertical LNDs. The latter alone cannot prove injectivity by
subtraction. All reviews finished before that clarification; the valid
uniqueness argument and theorem are unchanged. Jet's independent fresh
unsaved75b7b6 also verified both charts in both directions and the whole
algebraic identities. These remain AI reviews, not formal or expert checks.

No complete all-LND classification, escaping action, or polynomial-coordinate
system has been obtained. The precise special-fiber question is now whether a degree-zero
LND of Ctilde can move p. The finer classification cannot replace this
question, and any candidate preserving Dbase is already excluded.

Even a solution of that special-fiber question would not by itself settle
the main problem. One would still need a compatible action or obstruction
for the whole fourfold, including possible actions moving the chart
function A, and a proof using the actual polynomial-cylinder hypothesis.
No novelty, contact, or publication claim is made. The main goal is active.
