# The Zariski and etale gap for a specified KR retraction problem

Date: September 18, 2026. Private working proof. Novelty: UNKNOWN.

Two exact statements delimit a proposed use of the actual-cylinder
retraction. For KR-type hypersurfaces, no retraction on any Zariski
neighborhood of the whole hypersurface can preserve z^p+t^q. Yet
compatible retractions preserving that polynomial exist to every
finite order. For the Russell cubic, the specified formal system
algebraizes on an explicit etale neighborhood but is not rational
over the ambient function field.

This excludes the PRESCRIBED preservation condition, not unrestricted
retractions. A separate actual-affine-space example below shows why
failure of one formal system to algebraize cannot decide cancellation.
No solution or counterexample to cancellation is claimed.

## 1. The necessary retraction problem

Work over C. For m,p,q>=2, put

    B=C[x,y,z,t],    P=z^p+t^q,
    f=x+x^m*y+P,    A=B/(f),    X=Spec(A).

The hypersurface is smooth and integral. In fact f_y=x^m, while f_x=1
on x=0; primitiveness and linearity in y give irreducibility of f.
No coprimality of p,q is needed for the arguments below.

Any regular affine-space retract presentation i:X -> AN, r:AN -> X
would give a retraction for this standard embedding X -> A4. Extend
the N coordinate functions of i from X to A4 and compose with r.
In particular an actual isomorphism X x A1=A4 supplies such a
standard-embedding retraction. Its converse is NOT asserted.

A whole retraction is equivalently a tuple

    r_x=x+f*a, r_y=y+f*b, r_z=z+f*c, r_t=t+f*d,
    f(r_x,r_y,r_z,r_t)=0,                            (1)

with a,b,c,d in B. The following obstruction holds even if rational
denominators regular on a neighborhood of all of X are allowed.

## 2. No P-preserving Zariski-neighborhood retraction

There is no Zariski open U with X contained in U contained in A4
and regular retraction r:U -> X for which

    r_z^p+r_t^q=P                                    (2)

as functions on U. In particular, r cannot fix both z and t.

First, A has only constant units. Indeed A_x=C[x,x^(-1),z,t]. Every
unit of A is therefore c*x^n in this localization. The element x is
a nonunit of A because A/(x)=C[y,z,t]/(P) is nonzero. Neither x nor
its inverse can occur to a nonzero power in a unit of A, so n=0.

Suppose U and r exist. There is a principal open D(h) with
X contained in D(h) contained in U and h=1 modulo f. To construct it,
let J be the ideal of the closed complement of U. Since that complement
is disjoint from X, J+(f)=B. Choose h in J with h=1 modulo f. Restrict
r to D(h). If h is factored in the UFD B, every irreducible factor
h_j restricts to a unit of A, since their product restricts to one.
Thus each restriction h_j|X is a nonzero complex constant.

The target equation and (2) give

    r_x*(1+r_x^(m-1)*r_y)=-P.

Hence r_x is a unit of B[h^(-1),P^(-1)]. Units of this localized UFD
are products of nonzero constants and integral powers of irreducible
factors of hP. Restricting them to X_P removes the h-factors as
constants; all remaining factors depend only on z,t. It follows that

    r_x|X_P belongs to C[z,t,P^(-1)]^*.

On the other hand,

    A_P=C[z,t,P^(-1)][x,x^(-1)],                     (3)

because the relation makes x invertible and determines y. The
retraction identity requires r_x|X_P=x, the independent Laurent
variable in (3). This is impossible. The proof permits reducible P,
so it also covers noncoprime p,q.

This argument assumes the exact equality (2). A retraction only gives
r_z^p+r_t^q=P modulo f, which is strictly less information.

## 3. Compatible solutions to all finite orders

Define an ordinary polynomial derivation, not an LND, by

    nu=(1-m*x^(m-1)*y)*partial_x
       +m^2*x^(m-2)*y^2*partial_y.

It kills z,t and satisfies the exact identity nu(f)=1. For N>=1 set

    pi_N(g)=sum_(j=0)^(N-1) (-f)^j*nu^j(g)/j! mod f^N.  (4)

Leibniz's formula and the binomial coefficients show multiplicativity
modulo f^N. Also

    nu^j(f*g)=f*nu^j(g)+j*nu^(j-1)(g),

where the second summand is omitted for j=0. Inserting this formula
in (4) makes the two sums cancel, leaving only a multiple of f^N.
Thus pi_N factors through A and gives an algebra section

    A -> B/(f^N)

of reduction to A. These sections are compatible in N, and all fix
z,t. They define a formal retraction pi_hat into the f-adic completion.
Thus a contradiction to existence cannot follow from mere solvability
at some finite f-adic order. A bound imposing global polynomial
termination would be additional information.

The derivation nu is not locally nilpotent: nu(y) is a nonzero
multiple of y, which an LND on a characteristic-zero domain cannot
do. The formal Taylor formula is valid without local nilpotence;
one must not silently replace it by a finite polynomial action.

## 4. Explicit etale algebraization for the cubic

Now specialize to (m,p,q)=(2,2,3). Then

    nu=(1-2xy)*partial_x+4y^2*partial_y,
    nu^n(y)=4^n*n!*y^(n+1),
    pi_hat(y)=y/(1+4fy).                             (5)

The iterate formula follows by induction. Let

    D=1+4fy,
    S=B[s,1/(s*(s+1))]/(s^2-D).

The map Spec(S) -> A4 is etale: the derivative of the defining monic
equation in s is 2s, a unit. Over X one has s^2=1. Inverting s+1
removes the other branch, leaving s=1 and S/(f)=A. Thus this is an
etale neighborhood of the ENTIRE X with a distinguished copy of X.

Define regular functions in S by

    X'=s*(x-2f/(s+1)),    Y'=y/s^2,
    Z'=z,                 T'=t.                     (6)

No division by y is used in these definitions. To check the equation,
in the function field put alpha=1+2xy. Then

    X'=(alpha*s-s^2)/(2y),
    X'+X'^2*Y'=(alpha^2-s^2)/(4y)=-P.

The equality holds in S itself because (6) is regular and S is a
domain. The latter follows also from the nonsquare check below.
Consequently (6) defines a retraction Spec(S) -> X, restricting to
the identity on the distinguished branch f=0,s=1.

To verify that it algebraizes the SPECIFIED formal system (4), use an
independent formal time h and its root s_h=1 modulo h with
s_h^2=1-4hy. The unique formal solution of the flow equations is

    X_h=s_h*(x+2h/(s_h+1)),    Y_h=y/s_h^2,
    Z_h=z,                   T_h=t.

Differentiation gives dY_h/dh=4Y_h^2 and
dX_h/dh=1-2X_h*Y_h, with initial values x,y. Uniqueness follows
coefficient by coefficient in characteristic zero, so these are
exp(h*nu) applied to the coordinates as formal power series.
Substituting h=-f recovers (4) and (6), with s=1 modulo f.
No assertion that arbitrary formal maps algebraize has been used.

This formal retraction is genuinely nonrational over Frac(B).
Viewed over C(x,y,z), the polynomial D has degree three in t, with
nonzero leading coefficient 4y. Its pole order at t=infinity is odd,
so D is not a square in Frac(B). Thus s is not in Frac(B), and the
coefficient alpha/(2y) of s in the expression for X' is nonzero.
If X' were rational over B, that expression would recover s as a
rational function, a contradiction.

In particular this specified formal system cannot agree to all orders
with a retraction on a Zariski neighborhood. This also follows from
Section2, since the system fixes P. The etale cover and its retraction
are not a retraction of A4 itself and not a polynomial-cylinder
presentation.

## 5. Why this does not decide the unrestricted problem

Even a coordinate hypersurface can have a nonrational formal Taylor
retraction. Take f0=x in C[x,y,z,t] and

    nu0=partial_x+y^3*partial_y.

It satisfies nu0(f0)=1. Its formal flow on y is
y/(1-2h*y^2)^(1/2), so the same Taylor construction gives

    pi0_hat(y)=y/(1+2x*y^2)^(1/2).                   (7)

This is not rational: 1+2x*y^2 has odd degree in x over C(y,z,t).
Nevertheless the hyperplane x=0 has the global polynomial retraction
(x,y,z,t) -> (0,y,z,t). Failure of the chosen normal derivation or
of its associated formal retraction therefore cannot exclude a
different global retraction.

For the KR-type examples, Section2 adds a true all-degree obstruction
to the preservation of P, but no reason is proved why an unrestricted
retraction must preserve P. Any successful construction or exclusion
must handle mixing of those coordinates. The actual cylinder still
contains more structure than a mere abstract retract.

## 6. Verification and scope

General independently established the all-parameter unit argument,
the compatible formal sections, and the Zariski-neighborhood
strengthening. Jet independently checked the cubic case and the
explicit etale equation. General reconstructed the nonsquare argument
and the flow matching; root checked the entire etale target equation
by fresh exact reduction in13241b, and the transverse-derivation
identity on four exponent controls in87df56. Jet's separate whole
equation check2c9fce passed. Finite checks supplement the displayed
uniform proofs and are not a substitute for them.

The retraction and low-degree projection results retained in38 and74
were checked for overlap and stronger hypotheses. The intrinsic-LND
kernel recognition theorem does not apply to an arbitrary retraction
just because its kernel is principal. General formal-versus-global
obstructions were already known in the investigation; no historical
novelty is inferred from this particular calculation.

General and Jet each read all229 saved lines through EOF at SHA256
74e2452a03e879aa7b9347ea5a2c3e6060fc5614e32b6df502fabceb2fd9212c
and reported CLEAN. General's full read930010 and final hash/count
e45407, and Jet's full read43e9a4 and final hashc8fc26, cover every
section including the hyperplane comparator. Jet's fresh9b5f62 also
checked the all-m transverse identity, whole cubic flow equations,
initial conditions and comparator flow. Root reread the entire source
in cf0c91 and revalidated the incoming hash in817c1d. This paragraph
records those completed reviews without changing the mathematics.

No saved checker was executed, imported, compiled or edited. These
are separate AI-assisted reviews, not expert review or a formal
proof-assistant certificate. General cancellation remains UNSOLVED;
novelty remains UNKNOWN.
