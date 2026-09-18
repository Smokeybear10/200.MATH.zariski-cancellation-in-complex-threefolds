# Exact filtration for a reduced monic two-stage presentation

Private working proof, September 17, 2026. This is an algebraic consequence
of a specified presentation, not recognition of polynomial three-space.
General cancellation remains UNSOLVED. Novelty is UNKNOWN. The
adapted-basis method is standard and already used in this archive.

## 1. Statement, including the boundary cases

Let A be a domain containing Q, let 0 != f belong to A, and let n,m>=1.
Take a monic G(T) in A[T] of degree n and K(T,Y) in A[T,Y] such that

    deg_T K < n,    deg_Y K < m.                         (1)

The zero polynomial is allowed. Define the full quotient

    R=A[T,Y,Z]/(fY-G(T), fZ-Y^m-K(T,Y)).                 (2)

Write r,y,z for the images of its three presentation variables.
There is an injective map R -> A_f[T] given by

    r=T, y=G(T)/f, z=(y^m+K(T,y))/f.                    (3)

In particular R is a domain and R_f=A_f[r]. The derivation
D=f^2 partial_r on that localization preserves R, is locally
nilpotent there, and has actual kernel A on R. An A-basis is

    b_N=r^i y^j z^k,
    N=i+nj+nm k, 0<=i<n, 0<=j<m, k>=0.                (4)

For every N>=0 it satisfies

    deg_D b_N=N,
    D^N b_N=N! f^e_N,
    e_N=2N-floor(N/n)-floor(N/(nm)).                    (5)

Consequently, with F_N=ker(D^(N+1)) and I_0=A,

    F_N = direct_sum_(0<=j<=N) A b_j,
    I_N = D^N(R) intersect A = D^N(F_N) = f^e_N A.     (6)

For N=1 the exact plinth is

    f^2 A   if n>=2;
    f A     if n=1 and m>=2;
    A       if n=m=1.                                  (7)

Thus, when f is a nonunit, exact plinth f^2 A is equivalent to
n>=2 in this class. It does not imply m>=2. That latter inequality
is a separate necessary condition for a rank-three polynomial input,
via the one-generator criterion in631 and the published application
retained in621. The statement here does not assume R polynomial,
f prime, A factorial, or a normal exceptional curve.

## 2. A direct basis proof, without a hidden saturation

Give T,Y,Z positive weights 1,n,nm. Order monomials by weighted
degree, with lexicographic tie-breaking T>Y>Z. Both rewrite rules

    T^n -> fY-(G(T)-T^n),
    Y^m -> fZ-K(T,Y)                                   (8)

strictly decrease this order. The equal-weight terms fY and fZ
decrease the tie-breaker. Every monomial of G-T^n has weight below n.
Every monomial T^iY^j of K has weight at most

    (n-1)+n(m-1)=nm-1.

Because the order is well-founded and compatible with multiplication,
repeated rewriting terminates. It writes every polynomial class as
an A-linear combination of exactly the monomials in (4).

The substitution (3) annihilates both relations, hence defines a map
from the quotient. The polynomial y in A_f[T] has degree n and
leading coefficient f^(-1). The term y^m has degree nm; the degree
bound just proved puts K(T,y) strictly below nm. Thus z has degree
nm and leading coefficient f^(-(m+1)). The image of b_N has
degree N and leading coefficient

    f^(-j-(m+1)k).                                    (9)

The mixed-radix expression for each N in (4) is unique. The nonzero
images of the proposed basis therefore have distinct degrees over
the domain A_f, so they are A-linearly independent. Generation and
this independence prove simultaneously that (4) is a basis and
that (3) is injective. No confluence assertion, division by f in
the unlocalized quotient, or substitution of a saturated ideal
is needed. This also proves R_f=A_f[r].

The same conclusion can be phrased using the two monic leading
monomials T^n,Y^m and their coprime product criterion. The direct
generation/independence proof above does not require that terminology.

## 3. Whole derivation and the all-degree calculation

Differentiate (3) with D=f^2 partial_r. The exact formulas are

    Dr=f^2,
    Dy=f G'(r),
    Dz=f K_T(r,y)+G'(r)(m y^(m-1)+K_Y(r,y)).           (10)

All three belong to R. Thus D preserves R; local nilpotence follows
by restriction from polynomial differentiation on A_f[r]. Its
derivation degree on R is exactly the ordinary r-degree under (3).

For b_N, the top derivative is N! f^(2N) times (9). Since

    floor(N/n)=j+mk,    floor(N/(nm))=k,

this is exactly (5). The exponent e_N is nonnegative, including
n=m=1, because each floor is at most N. There is no reliance on
finitely many tested degrees.

An arbitrary nonzero element h of R has a unique finite expansion
h=sum a_j b_j. Its highest nonzero index is its derivation degree:
the highest term cannot cancel against a smaller r-degree. This
proves the filtration statement in (6) and ker(D)=A b_0=A.

If D^N(h) belongs to A, then D^(N+1)(h)=0, and conversely. Applying
D^N to the displayed filtration leaves only a_N D^N b_N. Since
N! is a unit in A, the ideal is f^e_N A. This proves both equalities
in (6), with an explicit witness b_N/N! for its generator.

Taking N=1 gives (7). In the unit-plinth boundary n=m=1 the
formulas give Dz=1 directly, since G=T+g_0 and K is a constant
in T,Y. If n=1<m, Dy=f is already a minimal local-slice value.

## 4. The associated graded algebra and exactly what is forgotten

Let gr_D(R)=direct_sum F_N/F_(N-1), with F_(-1)=0. The classes
U=in(r), V=in(y), W=in(z) have degrees 1,n,nm. The strict
lower-weight bounds in (1) give

    gr_D(R) = A[U,V,W]/(U^n-fV, V^m-fW).               (11)

For completeness, generation follows from the basis expansion.
The quotient on the right has the same spanning monomials as (4).
Their images in gr_D(R) lie in distinct degrees and each generates
a free rank-one A-module, so the map has no additional relation.

Equivalently, using D^N/N! on each graded piece embeds (11) into
A[t] with

    U=f^2 t, V=f^(2n-1)t^n, W=f^(2nm-m-1)t^(nm).       (12)

The factorial normalization makes this identification multiplicative,
by Leibniz's rule in the top derivative degree. The displayed powers
of f are nonnegative even in the boundary cases.

Neither the image-ideal formula nor (11) retains the lower
coefficients of G or K. It is therefore not a recognition theorem
for those lower-order terms. It gives no reason for the curve

    (A/f)[T,Y]/(Gbar(T), Y^m+Kbar(T,Y))

to be normal. The known nonpolynomial control625 already shows that
adapted bases and principal images in every degree cannot replace
the actual polynomial-ambient hypothesis in a normality argument.

There is an even sharper warning about using the graded ring itself.
If f is a nonunit and n>=2, the domain in (11) is ALWAYS nonnormal.
Put L=nm, E=2L-m-1, and consider the fraction

    h=U^(n-1)V^(m-1)/f.

Its degree is L-1 and its image under (12) is f^(E-1)t^(L-1).
The degree-(L-1) part of (12) is f^E A t^(L-1), so h is not in
the graded ring: membership would imply 1 belongs to fA. Yet

    h^L = f^(L-m-1) W^(L-1).

The exponent L-m-1=m(n-1)-1 is nonnegative. Thus this equation
is a monic integral equation for h over the graded ring. This
proves nonnormality even when the original ungraded R is C^[3].
It must not be confused with normality of R or of R/fR. Normality
of gr_D(R) therefore cannot serve as an additional premise for
the unresolved nonunit-square-plinth inputs of this class.

The exponent sequence does recover the two presentation degrees:

    e_N-e_(N-1)=2-1_(n divides N)-1_(nm divides N).

The first deficit from two occurs at n, and the first zero jump
occurs at nm, including m=1. This is information about the
filtration, not control of a different LND on the whole R.

## 5. Application and scope relative to earlier work

The normalization in
[631](nonlinear-two-stage-monic-normalization-pass631-working.md),
subject to its separate acceptance,
puts an exact nonlinear two-stage input on R=C^[3] with actual
A=ker(D) and Dr=f^2 into (1)--(2), preserving this A, D and r.
Subject to that normalization's geometric finiteness dependency,
the present elementary calculation then determines every higher
image ideal of the original action. It does not merely compute
the images of a different derivation on a new abstract ring.

The adapted-basis implication itself was already recorded in
[16](rank-two-image-ideals-pass16.md) and
[47](image-ideal-source-scope-pass47.md). The rank-three example
in [17](rank-three-image-pass17.md) has its own known basis and a
different two-prime formula; no general freeness conjecture is
settled here. If m=1, (5) becomes

    e_N=2N-2 floor(N/n),

the single-stage pattern represented by the n=5 control in
[625](prime-square-cuspidal-plinth-smooth-factorial-control-pass625-working.md).
Preservation of all image ideals under coprime local-slice
modification was already proved in
[19](global-modification-bridge-pass19.md) and is not recounted
as a new consequence.

El Kahoui--Labtaini--Ouali's 2026
[*Freeness Property for Locally Nilpotent Derivations of Factorial Domains*](https://link.springer.com/article/10.1007/s00031-026-09969-9)
has a directly checked publisher abstract assuming freeness,
an affine kernel and prime-power plinth, and concluding a
generalized Danielewski description. Only that abstract and its
reference list were accessible here, not the subscription proof.
It supplies context, not the proof of (5) or a claim of originality.

The remaining cancellation obligations are unchanged: no arbitrary
sliced fourfold has been put in this presentation class, and the
nonlinear n,m>=2 case has not been recognized as rank at most two.
Neither human expert review nor Lean verification has occurred.

## 6. Verification status

The all-degree proof is Sections 2--4. Fresh unsaved exact algebra
is supplementary evidence only. A complete separate review of this
saved source is required before canonical acceptance. No frozen
checker script is executed, imported or compiled by this note.
