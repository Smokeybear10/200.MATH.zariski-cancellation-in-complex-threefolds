# Quadratic recognition for the entire polynomial-curve kernel class

## 1. Statement and dependency

Retain every hypothesis and definition (1) of the complete
[polynomial-curve proof690](polynomial-curve-all-quadratic-extensions-pass690-working.md):
R=C[x,y,z], H=Jac(f,g,.), C0=C[f,g], Hrho=-g f^n, and B=R[t].
In particular P is monic of degree m>=2, n>=1, and F(X,0) is
nonconstant. This note depends on the whole base presentation and
pole-repair calculation proved there, not on numerical tests.

**Theorem.** Let D be ANY nonzero locally nilpotent derivation of R
whose kernel is the specified embedded subalgebra C0. For every
a,b in C0 minus zero and w in R satisfying Dw=a^2 b, set

    E=D+(1+abw)partial_t, v=at-w^2/2,
    u=t-bwv+(ab^2/2)v^2.                               (1)

Then E has whole polynomial coordinates on B, ker E is C^[3],
and this PARTICULAR u is a coordinate of B. Thus the quadratic
quotient R[Q]/(w+Q+abQ^2/2) is C^[3] as well, by688's whole
quotient maps, repeated in690 Section7.

The quantifier over D covers all invariant replicas of H, with
arbitrary multiplicities and factors, not merely constant multiples.
It does not cover every embedded kernel of an LND on C^[3], much
less every sliced LND on C^[4]. General complex-threefold cancellation
remains UNSOLVED and novelty UNKNOWN. In particular the primitive
base result690 did not itself silently include these replicas.

## 2. Exactly which derivations share C0

First H is primitive: its three coefficient polynomials have no
nonconstant common divisor. An irreducible common divisor must
divide Hrho=-g f^n. Kernels of LNDs are factorially closed; since
f,g are prime variables in C0, they are prime in R. Thus the only
possible common prime factors are f and g.

Using the notation S=xF(x,f), s=S(x,0), G0=s^m/x from690,

    Hy=-g+S_x N_rho,
    Hy mod f=-G0+m s^(m-1)s'.                          (2)

If d=deg_x s>=2 and c is its leading coefficient, the last
polynomial has degree md-1 and leading coefficient (md-1)c^m,
which is nonzero. Hence f does not divide every coefficient.
In the exact f-localized chart of690, reduction modulo g gives

    R_f/(g)=C[f,f^(-1),x,rho]/(N(f,rho)).

The polynomial N_rho has degree m-1 in rho and is nonzero modulo
the monic degree-m polynomial N. Since Hx=-f^n N_rho, g does not
divide every coefficient either. This proves primitivity.

Let K=Frac(C0). The local-slice chart gives
K tensor_(C0) R=K[rho]. A nonzero D with kernel C0 extends to a
K-LND of K[rho], necessarily c partial_rho for some c in K minus
zero. For completeness a polynomial coefficient of positive degree
cannot give a nonzero LND in one variable: iterated differentiation
of rho never terminates, by degree and its nonzero leading coefficient.
Thus D=qH for q in K minus zero. Write q as a reduced fraction
in the UFD R. Its denominator divides all three coefficients of H,
since D preserves R. Primitivity forces q into R. Finally Hq=0,
so q belongs to C0. Conversely every nonzero invariant replica
lambda H is an LND with the same kernel. Consequently

    {D nonzero LND of R:ker D=C0}={lambda H:0!=lambda in C0}. (3)

The factorial-closure fact used above also has a short degree proof:
for a nonzero LND on a domain of characteristic zero, derivation
degrees of nonzero products add, so degree zero of a product forces
degree zero of both factors.

## 3. Remove the invariant constant before clearing poles

Write D=lambda H, with lambda in C0 minus zero. Since D^2=lambda^2 H^2,
the all-local-slices module from690 still gives

    w=h rho+k, h,k in C0, h!=0,
    a^2 b=-lambda h g f^n.                             (4)

Use a modified quadratic expression

    W=a t-h^2 rho^2/2-hk rho=v+k^2/2,
    L=lambda H/a+bw partial_t, N0=-W L.                (5)

On B_a, L is an LND: its base is an invariant multiple of H and
Lw=ab, Lt=bw, L^2t=ab^2, L^3t=0. Also LW=0. Thus N0 is an
LND on B_a and Phi=exp(N0) is an automorphism there. One has

    E=aL+partial_t, EW=a, [E,L]=0,
    [E,N0]=-aL, [N0,-aL]=0.

Therefore E Phi=Phi partial_t. In particular

    s_star=Phi(t)=t-bwW+(ab^2/2)W^2                    (6)

is WHOLE and E(s_star)=1. Removing the invariant constant in (5)
does not claim W=v. It keeps the intertwining and eliminates an
unneeded polar constant. The supplied u will be recovered later.

The base part and t part of N0 are

    N0|R=[-lambda t+(lambda h/a)(h rho^2/2+k rho)]H,
    N0(t)=-bwW.                                       (7)

The second expression is already whole. All possible poles of the
first coefficient outside f disappear by the next exact valuation.

## 4. Prime-factor reduction, including repeated factors of lambda

Write

    lambda=f^L0 lambda0, h=f^ell h0, a=f^j A0,
    L0,ell,j>=0, f dividing none of lambda0,h0,A0.

For each irreducible pi!=f dividing A0 with multiplicity A>=1,
equation (4) gives

    2A<=v_pi(lambda)+v_pi(h)+v_pi(g)
        <=v_pi(lambda)+v_pi(h)+1.

Hence v_pi(lambda h)>=2A-1>=A, so A0 divides lambda0 h0 in C0.
Define the POLYNOMIAL and the integer

    d0=lambda0 h0/A0 in C0,
    e=j-L0-ell, lambda h/a=f^(-e)d0.                  (8)

If e<=0, (7) is a whole derivation on B. Its local nilpotence
descends from B_a by injectivity of localization. Both exp(N0)
and exp(-N0) are therefore whole automorphisms, and the intertwining
already proves the theorem's polynomial-kernel conclusion.

Suppose henceforth e>0. The f-valuation of (4) gives

    2j<=L0+ell+n, so 2e+L0+ell<=n.                    (9)

In particular 2e<=n and j>0. Formula (7) proves that N0 preserves
B_f. Its local nilpotence there follows by comparison in B_af with
the already licensed LND on B_a, since f is invariant. We do NOT
need L itself to preserve B_f. Thus Phi is an automorphism of B_f.

Put

    gamma=d0 h, beta=d0 k, J=gamma rho^2/2+beta rho,
    Vhat=f^e lambda t-J=(f^e lambda/a)W.                (10)

These expressions are whole except that the final equality is read
in the common fraction ring. Its coefficient f^e lambda/a is
invariant, so N0(Vhat)=0. Equations (5),(7) give exactly

    Phi(rho)=rho+g f^(n-e)Vhat.                       (11)

No higher terms in that image are omitted. Phi fixes f,g.

## 5. The repaired map, its residue, and its whole inverse

Let q=n-e>=e. Formula (10) of690 now gives the whole Phi(x)=X
with V replaced by Vhat. In particular X=x modulo f and
X-x belongs to f^q B. The formula for Phi(y) is likewise (11)
of690 with that replacement.

For precision the entire changed finite-part calculation is as
follows. Use S,G,M,T from690 (12) and set

    J_star=d0(f,G)[h(f,G)S^2/2+k(f,G)S],
    C=rem_(f^e)(-J_star T), K_res=(-J_star T-C)/f^e,
    V0=-J_star(x,0), d1=m s^(m-1)V0,
    d2=binom(m,2)s^(m-2)G0 V0^2.

Let epsilon=1 for n=2e and zero otherwise. In B_x the full expansion
modulo f^(n+1) is

    X-x=f^q M[f^e lambda(f,G)t-J_star]+epsilon f^n d2.

The substitution lambda(f,g) by lambda(f,G) is legitimate because
their difference belongs to f^n B_x; after its multiplier f^(q+e)
its contribution is above order n. The same reasoning applies to
gamma,beta. All Taylor-order inequalities in690 remain unchanged.

Define delta0=x partial_y+P'(y)partial_z and

    Gamma=exp[-C(x,f)/(x f^e)delta0], Psi=Phi Gamma.

As in690, C is divisible by x^(m-1), so Gamma is a licensed
automorphism of B_f fixing t. The repaired Y=Psi(y) is whole with

    Y=y+A(x,t) mod f,
    A=lambda(0,G0)t T(x,0)+K_res(x,0)
      -epsilon*[s'd2+s''d1^2/2+C_x(x,0)d1].            (12)

Every term is divisible by x. No unit condition on lambda(0,G0)
is needed. There are no extra lambda derivatives in (12): lambda
enters the order-n time term before the Taylor substitution for S,
and its higher f-adic errors are strictly above that order.

Crucially the t image has coefficient ONE in its residue, not
lambda(0,G0). Since j>0, abar=0 modulo f. Use bars on coefficients
in C0 to mean evaluation at (f,g)=(0,G0), and write

    wbar=hbar*s+kbar,
    Wbar=-hbar^2*s^2/2-hbar*kbar*s,
    s_star=t+P0(x) mod f, P0=-bbar*wbar*Wbar.           (13)

Both wbar,Wbar are independent of t, and the last term of (6)
vanishes modulo f. This proves the stated unit coefficient even
when lambda has repeated factors or vanishes along f.

The proof of whole Z=Psi(z) from XZ=f+P(Y) is unchanged. The
residual map on B/(f) is therefore the whole automorphism

    x->x, t->t+P0(x), y->y+A(x,t),
    z->z+[P(y+A(x,t))-P(y)]/x.

Its inverse is exactly (19)'s inverse in690: replace t by t-P0(x),
then subtract A(x,t-P0(x)) from y and the matching divided
difference from z. The x-divisibility makes both maps whole.
Injectivity modulo f and the least-denominator argument in690
then make the localized inverse of Psi whole as well.

Since Gamma commutes with partial_t, E Psi=Psi partial_t. Thus
B=C[X,Y,Z,s_star] and ker E=C[X,Y,Z] in the e>0 branch too.

## 6. Supplied coordinate, boundary cases, and scope

Directly from Dw=a^2b, the identities in688 give Eu=1 for (1).
In either branch, u-s_star belongs to the now-polynomial kernel.
The shear s_star->u therefore completes u to whole coordinates.
This is not a claim that (6) equals u or that the discarded constant
k^2/2 has a polynomial primitive divided by a.

When n=1, (9) excludes e>0, so the whole-exponential branch handles
every replica. When n=2e, (9) forces L0=ell=0; the full epsilon
terms of (12) still remain and have not been discarded. Factors
of lambda away from f, including repeated factors of g and unrelated
plane curves, were all included in the prime argument in Section4.

The dependency on the particular embedded kernel C0 is essential
to the current proof. Neither (3) nor the residue calculation
classifies other embedded polynomial two-kernels in C^[3]. The
remaining task is a general recognition or reduction argument for
those kernels, or for the arbitrary polynomial-cylinder hypothesis.
The theorem does not fill that gap. No public novelty claim,
submission, or expert contact is made by recording this result.

## Verification provenance

The complete 244-line source was held at SHA256
e1b919f64efe8fa54f68bf69a8c70c0c58d99c9ea6e9a73515960fe438e0a7d6.
Root read all lines through EOF in39c045. Separate complete AI
reconstructions returned CLEAN: General9114ec, final hash06fef2;
Jet7cf16b, final hash361d54; Geometry61abb4, final hash1388d1.
No source correction was requested. This appendix alone was added
after those reviews.

Fresh exact scratch checks include Jet e18443 with a=f^2g and
g not dividing lambda, exercising the L-versus-N localization
distinction. Jet ab7199 independently checked n=3, lambda=f,
h=k=1,a=f^2,b=-g, for which the Y residue has no time term but
the time residue has a nonzero shift despite n>2e. Root0bdb68
checked that time identity, then encountered a failed scratch
assertion caused by extracting a coefficient from an unexpanded
SymPy product. The corrected independent calculation cbed20 gave
all polar coefficients zero and exact finite part A=x^4(5x^2+7)
for P=y^2+y+1,F=x+f. The failed scratch assertion is not counted
as a passing test or concealed as a theorem defect.

No saved checker was executed, imported, compiled or edited. No
human expert review, proof-assistant certification, or novelty
clearance follows from these internal checks.
