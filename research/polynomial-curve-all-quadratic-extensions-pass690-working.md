# Every quadratic sliced extension of the polynomial-curve family

## 1. Statement and limits

Work over C. Let m>=2, n>=1, let P(Y)=sum_{i=0}^m p_i Y^i
be monic of degree m, and let F(X,Z) belong to C[X,Z] with
F(X,0) nonconstant. In R=C[x,y,z], put

    f=xz-P(y), S(x,f)=xF(x,f), rho=S(x,f)+y f^n,
    N(f,rho)=f^(nm+1)+sum_{i=0}^m p_i rho^i f^(n(m-i)),
    g=N(f,rho)/x, H=Jac(f,g,.), C0=C[f,g], B=R[t].       (1)

The Jacobian uses the ordered gradients of f,g, and the argument.
The apparent quotient defining g is polynomial, as proved below.

**Family theorem.** For EVERY a,b in C0 minus zero and EVERY w in R
with H(w)=a^2 b, the derivation and its supplied slice

    E=H+(1+abw)partial_t, v=at-w^2/2,
    u=t-bwv+(ab^2/2)v^2                                (2)

have polynomial coordinates on B: ker E is a polynomial three-ring,
and this particular u is a coordinate of the actual polynomial
four-ring B. There is no degree restriction on a,b,w,P, or F beyond
the displayed assumptions. The case n=1 is included.

The proof gives a finite pole correction and proves that the corrected
map AND its inverse are whole polynomial maps. It uses an exact
description of all local slices to reduce (2) to that construction.
It does not assume that the original exponential in688 is polynomial.

This is a family result, not a solution of arbitrary rank-three
quadratic extensions or of complex-threefold cancellation. No reduction
of arbitrary sliced LNDs on C^[4] to (1)-(2) has been proved. Mathematical
priority is UNKNOWN; internal AI checking is not human expert review
or formal proof certification.

The monomial P(Y)=Y^m base is the published Dasgupta--Gaifullin
Theorem5.7 family. General local-slice construction is established
machinery, not a contribution here.[^1] The arbitrary monic base,
its exact kernel and local slices were already retained in18.[^2]
The specified a=f,w=rho monomial subfamily was recognized in595.[^3]
The canonical P(Y)=Y^2,F(X,Z)=X^2 subfamily was already covered more
broadly by23, for every added coefficient in C[f,g,rho].[^4]
Thus the scope added relative to these retained notes is the uniform
all-quadratic-data conclusion across (1), not a new base construction
or a claim that each special case was previously unrecognized.

## 2. Exact base algebra, kernel, and all local slices

Taylor expansion gives the whole expression

    g=z f^(nm)+sum_{j=1}^m P^(j)(y)/j!
                       *x^(j-1) F(x,f)^j f^(n(m-j)).    (3)

The polynomial f is prime, since xz-P(y) is primitive and linear
in z with coprime coefficients. In particular f does not divide x.
Modulo f, set

    s=xF(x,0), G0=s^m/x=x^(m-1)F(x,0)^m.

Then rho=s and g=G0. Both s and G0 are nonconstant. The elements
f,g are algebraically independent: in a nonzero relation divide out
the common maximal power of f and reduce modulo f to obtain an
impossible nonzero polynomial in G0(x).

There is an exact presentation

    R_f=C[f,f^(-1),g,x,rho]/(xg-N(f,rho)).               (4)

Its inverse recovers y=(rho-xF(x,f))/f^n and

    z={g+sum_{i=1}^m sum_{j=1}^i p_i(-1)^j binom(i,j)
             *rho^(i-j)x^(j-1)F(x,f)^j f^(n(m-i))}/f^(nm).

Substitution proves both compositions. Alternatively injectivity
follows after inverting x; the primitive linear relation in g makes
the presented domain x-torsion-free. No x inverse is used in the
displayed recovery of z.

Direct Jacobian calculation gives

    Hf=Hg=0, Hrho=-g f^n, Hx=-f^n N_rho.               (5)

For the signs, Jac(f,rho,x)=-x f^n. Inverting g in (4) gives
R_fg=C[f^(+/-1),g^(+/-1),rho], on which H=-g f^n partial_rho.
This licenses local nilpotence on R, since H preserves R and every
element is killed by an iterate in that localization.

As N is monic of degree m in rho, (4) is free over C[f^(+/-1),g]
with basis x^j rho^i, j>=0, 0<=i<m. In R_fg the H-degree of this
basis element is mj+i. These degrees are all distinct, so highest
degrees cannot cancel. Thus

    ker(H|R_f)=C[f^(+/-1),g],
    ker(H^2|R_f)=C[f^(+/-1),g] + C[f^(+/-1),g]rho.      (6)

Let d=deg_x s>=2. Then deg_x G0=md-1>d, so
s does not belong to C(G0): otherwise the field degree md-1
would divide d. To contract the second module in (6) to R, clear
the least common f denominator in h(f,g)rho+k(f,g). If this
denominator has positive exponent, reduction modulo f gives

    h0(G0)s+k0(G0)=0

with at least one of h0,k0 nonzero. If h0 is zero, nonconstancy
of G0 is a contradiction; otherwise s would belong to C(G0).
The same argument contracts the first ring. Consequently

    ker H=C0, ker H^2=C0 direct-sum C0 rho,
    H(R) intersect C0=g f^n C0.                        (7)

In particular EVERY w in (2) is h rho+k for h,k in C0, h nonzero.
No invariants-under-specialization assertion was used in this proof.

## 3. Higher-pole construction

Fix integers e>=1 and 2e<=n, and arbitrary gamma,beta,kappa in C0,
including zero coefficients. Put

    J=gamma rho^2/2+beta rho+kappa, V=f^e t-J,
    E=H+[1-g f^(n-e)(gamma rho+beta)]partial_t,
    L=H/f^e-g f^(n-2e)(gamma rho+beta)partial_t.          (8)

In this section E denotes (8), before the reduction from (2).
It is an LND on B, since its t coefficient has H-degree at most one.
On B_f, L is an LND, LV=0, and

    E=f^e L+partial_t, EV=f^e, [E,L]=0,
    Lrho=-g f^(n-e), L^2t=gamma g^2 f^(2n-3e), L^3t=0.

Therefore Phi=exp(-VL) is a licensed automorphism of B_f. It fixes
f,g and satisfies

    rho'=Phi(rho)=rho+g f^(n-e)V,
    s_star=Phi(t)=t+g f^(n-2e)(gamma rho+beta)V
                       +(gamma g^2/2)f^(2n-3e)V^2.     (9)

All exponents in s_star are nonnegative. The commutator
[E,-VL]=-f^e L commutes with -VL, so the finite exponential identity
gives E Phi=Phi partial_t. In particular E(s_star)=1. This direct
intertwining, rather than just the existence of a slice, will later
identify the kernel coordinates.

Expanding xg=N(f,rho) gives a whole first coordinate

    X=Phi(x)=x+sum_{i=1}^m sum_{j=1}^i
       p_i binom(i,j)rho^(i-j)g^(j-1)
       *f^(n(m-i)+j(n-e))V^j.                          (10)

Every cancellation of g has already occurred in (10). No locus
g=0 is removed. Write q=n-e>=e; then X-x belongs to f^q B.

The remaining potentially polar image is

    Phi(y)=y+{g f^q V-[S(X,f)-S(x,f)]}/f^n.            (11)

## 4. Exact pole correction and full constant term

All f-adic calculations can be made in
B_x=C[x,x^(-1),f,y,t], with f an independent polynomial variable.
For a whole polynomial, divisibility by f^j there descends to B,
because f is prime and does not divide x. We use this descent only
after exhibiting a numerator in B, not for an arbitrary rational
function.

The following are polynomials in x,f:

    G=S^m/x, M=mS^(m-1), T=G-M S_x,
    J_star=gamma(f,G)S^2/2+beta(f,G)S+kappa(f,G),
    C=rem_(f^e)(-J_star T),
    K_res=(-J_star T-C)/f^e.                            (12)

The remainder means the unique polynomial of f-degree less than e.
Since S is divisible by x, G,M,T are divisible by x^(m-1).
Thus C,K_res belong to x^(m-1)C[x,f], including when kappa has a
nonzero constant. In particular C/x is a polynomial.

In B_x, rho-S, g-G, and J-J_star belong to f^n B_x. Terms in
(10) with i<m begin at order n+q, and terms with j>=3 have order
at least 3q>=n+1. Let epsilon be 1 if n=2e and 0 otherwise, and put

    V0=-J_star(x,0), d1=m s^(m-1)V0,
    d2=binom(m,2)s^(m-2)G0 V0^2.                       (13)

The full expansion needed, including the boundary n=2e, is

    X-x = f^q M(f^e t-J_star)+epsilon f^n d2
                                              mod f^(n+1). (14)

The j=2 term can survive to order n only when 2q=n. In Taylor
expanding S(X,f), the quadratic term similarly survives only in
that case. Higher powers have order at least n+1. Substitution
in (11) yields the complete constant-term congruence

    Phi(y)-C(x,f)/f^e
      = y+t T(x,0)+K_res(x,0)
        -epsilon*(s' d2+s'' d1^2/2)             mod f.  (15)

This expression is whole: before division by f^n in (11), the
polar part is -f^q J_star T; its difference from f^q C is divisible
by f^n, by (12). The remaining Taylor terms also have that
divisibility. This is first a calculation in B_x and then a whole
divisibility statement in B by the prime-factor argument above.

Define the triangular LND delta0=x partial_y+P'(y)partial_z,
which fixes x,f,t, and define on B_f

    Gamma=exp[-C(x,f)/(x f^e) delta0], Psi=Phi Gamma.

The coefficient is in the kernel of delta0, so this is a licensed
automorphism, with Gamma(y)=y-C(x,f)/f^e and Gamma(t)=t.
Thus

    Y=Psi(y)=Phi(y)-C(X,f)/f^e                         (16)

is whole too: C(X,f)-C(x,f) is divisible by f^q, hence by f^e.
Its constant contribution after division is epsilon*C_x(x,0)d1.
Combining (15)-(16) gives

    Y=y+A(x,t) mod f,
    A(x,t)=t T(x,0)+K_res(x,0)
       -epsilon*(s' d2+s'' d1^2/2+C_x(x,0)d1).          (17)

Every term in A is divisible by x. Indeed T,K_res,C contain
x^(m-1), d1 contains x^(m-1), d2 contains x^(2m-3), and C_x
contains x^(m-2). These bounds suffice even for m=2, n=2e, and
arbitrary constant terms in gamma,beta,kappa and P. No coefficient
has been assumed nonzero in order to divide by it.

The fourth image (9) has residue

    s_star=t+P0(x) mod f,
    P0=epsilon*G0[gamma(0,G0)s+beta(0,G0)]V0.           (18)

The final term in (9) has order 2n-3e>=e>=1 and does not affect
(18). Equations (14)-(18) retain every term that can survive at
the stated orders; they are not a truncation assumption on F or P.

## 5. Whole fourth coordinate, inverse descent, and rectification

We have whole images X,Y,s_star and Psi(f)=f. Set Z=Psi(z) in B_f.
The identity

    XZ=f+P(Y)

shows that Z is whole, because f is prime and X=x modulo f is
not divisible by f. More explicitly, if Z=p/f^k is reduced with
k>0, this identity would force f to divide Xp, a contradiction.
Thus Psi is an injective whole endomorphism of B.

Its reduction modulo f agrees with the following whole polynomial
automorphism of B, which fixes f:

    x |-> x,
    t |-> t+P0(x),
    y |-> y+A(x,t),
    z |-> z+[P(y+A(x,t))-P(y)]/x.                      (19)

The quotient by x is polynomial, since x divides A. An inverse
sends t to t-P0(x), y to y-A(x,t-P0(x)), and z to

    z+[P(y-A(x,t-P0(x)))-P(y)]/x.

Both inverse orders follow by substitution. To verify the z residue
of Psi agrees with (19), reduce XZ=f+P(Y) modulo f and cancel x
in the domain B/(f). Thus the induced map on B/(f) is injective.

For any original generator h of B, the localized inverse writes
Psi^(-1)(h)=p/f^k, where p is in B and k>=0 is minimal. If k>0,
then Psi(p)=f^k h, so injectivity modulo f forces p into (f),
contradicting minimality. Hence k=0 for all generators and the
localized inverse is whole. This proves Psi is an automorphism
of B, not just a localized map or a formal automorphism.

Gamma is independent of t and commutes with partial_t. Therefore
the intertwining from Section3 gives

    E Psi=Psi partial_t,
    B=C[X,Y,Z,s_star], ker E=C[X,Y,Z].                 (20)

The pole-repair conclusion holds for every e,gamma,beta,kappa in
Section3, with no further condition. The correction Gamma need
not fix g; preserving f alone is enough. This is why the argument
does not contradict the old-invariant-plane obstruction in689.

## 6. Reduction of EVERY admissible quadratic datum

Return to (2). Equation (7) gives w=h rho+k with h,k in C0,
h nonzero, and

    a^2 b=-h g f^n.                                   (21)

In the polynomial ring C0=C[f,g], write a=f^j A0 with j>=0 and
f not dividing A0. Let pi be any irreducible divisor of A0 and
let s=v_pi(A0)>=1. Since pi is not f and g is a prime variable,
(21) gives

    2s<=v_pi(h)+v_pi(g)<=v_pi(h)+1.

Thus v_pi(h)>=s and A0 divides h. Write

    h=A0 f^ell h0, f not dividing h0, ell>=0,
    e=j-ell, gamma=A0 f^ell h0^2, beta=h0 k.            (22)

Then ab=-g f^(n-e)h0 and the original E is EXACTLY

    H+[1-g f^(n-e)(gamma rho+beta)]partial_t.           (23)

The f-valuation of (21) gives 2j<=ell+n. If e>0, it follows
that 2e+ell<=n, in particular 2e<=n. Apply Sections3-5 with
these gamma,beta and kappa=0. This proves a whole rectification
of the original E and polynomiality of its kernel.

If e<=0 instead, the whole polynomial

    J0=f^(-e)(gamma rho^2/2+beta rho)

satisfies Et=1+HJ0. The triangular coordinate s=t-J0 obeys
Es=1 and changes E to H+partial_s. The finite automorphism
exp(-sH) in R[s] fixes s and intertwines H+partial_s with
partial_s, giving polynomial kernel coordinates in this branch
as well. For n=1 the branch e>0 cannot occur, so all data there
are handled by this elementary case.

It remains to identify the supplied u, rather than only the new
coordinate slice s_star (or s). Direct calculation from (2) gives

    Ev=a, q0=abv-w, Eq0=0, v+q0^2/2=au, Eu=1.         (24)

Once (20), or its elementary counterpart, is established, u-s_star
belongs to the polynomial kernel. Thus replacing s_star by u is
a triangular shear in those coordinates. The same argument uses
u-s in the elementary branch. Hence the particular u of (2) is
a whole coordinate, proving the theorem.

There is an important distinction here. The exponential constructed
with kappa=0 need NOT be the original quadratic exponential of688.
To match its constant term formally would require
kappa=k^2/(2A0 f^ell), which need not be polynomial. We do not make
that substitution. Rectifying E first and then using (24) avoids
that inadmissible denominator entirely.

## 7. Consequence and the still-missing general step

The whole quotient identification already proved in688 now gives,
for all data in (1)-(2),

    R[Q]/(w+Q+abQ^2/2) is isomorphic to C^[3].          (25)

For completeness, that identification sends Q to q0 modulo u and
has inverse fixing R and sending t to bQ^3/2+ab^2Q^4/8. The identities
q0=Q,u=0 on substitution and

    t-bq0^3/2-ab^2q0^4/8
      =(1-abq0-a^2b^2q0^2/2)u+(a^3b^2/2)u^2

check both orders. The finite slice projection identifies ker E
with B/(u). Thus (25) is not an inference from a local chart.
It does not separately assert that the defining equation in R[Q]
is itself an ambient coordinate.

The construction relies on several concrete features not supplied
for an arbitrary rank-three LND: the monic chart (4), the complete
degree-one module (7), the triangular field delta0 fixing f, and
the x-divisible residue (17) giving a whole residual inverse.
Neither an arbitrary presentation A[s]=C^[4] nor an arbitrary
rank-three quadratic extension has been shown to provide these.
The general cancellation goal therefore remains UNSOLVED. Repeating
tests inside this now-recognized class cannot supply that reduction.

## Sources and retained comparisons

[^1]: N. Dasgupta and S. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables, primary version2](https://arxiv.org/html/2306.00510v2), Theorem2.17 for established local-slice machinery and Theorem5.7 for the displayed monomial family. The direct proof here does not rely on the source's typographical error in its displayed derivative of y.

[^2]: [Polynomial-curve lift18](polynomial-curve-lift-pass18.md), Sections1-3, and its [statement-level literature audit](polynomial-curve-literature-pass18.md). The field sign there is the negative of H here. Exact kernel and local-slice proofs are repeated in Section2 for a self-contained dependency.

[^3]: [Pole-repair recognition595](rank-three-family-pole-repair-recognition-pass595-working.md), for P(Y)=Y^m, a=f, w=rho, n>=2. The present proof retains its residue and whole-inverse method, allowing higher poles and arbitrary invariant quadratic coefficients.

[^4]: [Polynomial local-slice coefficients23](polynomial-local-slice-coefficients-pass23.md), for P(Y)=Y^2,F(X,Z)=X^2. Its sign convention can be changed by t->-t and scaling the derivation; no new conclusion for that entire canonical coefficient family is claimed here.

## Verification provenance

The 380-line mathematical source was held unchanged at SHA256
45df52ac57ed94d7bc829c27d12f6a8c792178ffcb3d69779635100a033aa87d.
Root read every line through EOF in c0ca98. Three separate AI agents
then reconstructed that entire source and returned CLEAN, without
corrections: General0ab815/f4c980 with final hash b28e9d;
Jet47b853 with final hash8c8955; Geometry0103ff/b2d481 with final
hash8a0890. These reviews included the full inverse, all-data reduction,
boundary cases, and the distinction from general cancellation.

Fresh unsaved exact checks included root416337 for
(m,n,e)=(2,4,2),(2,5,2),(3,2,1), Jet73aee4 for (2,4,2), and
Jet702cba for (3,4,2), with nonzero constant terms and the complete
finite-part correction. Root52bca0 additionally checked universal
slice/commutator identities and a datum whose exponential-matching
kappa is nonpolynomial but whose two coordinate slices have invariant
difference. Finite samples support, but do not replace, the proof.
Two naive full-composition scratch expansions were stopped without
results and replaced by bounded exact f-adic arithmetic; neither
interrupted computation is counted as passing evidence.

No saved checker was executed, imported, compiled or edited. Only
this provenance section was appended after the complete-source reviews.
No human peer review, proof-assistant certification, or novelty clearance
is asserted. The theorem is for H in (1), not implicitly for every
invariant replica lambda*H.
