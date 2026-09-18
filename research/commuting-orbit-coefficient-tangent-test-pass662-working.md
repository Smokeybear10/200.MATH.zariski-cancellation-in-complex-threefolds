# Whole-orbit recovery has an exact vertical-degree cutoff

Date: September 18, 2026.
Status: complete working proof; corrected version internally reviewed.

For an actual cylinder B=A[u], leading extraction alone need not recover
an additive action moving a specified point of Spec A. This note gives
an exact finite test inside a different, explicitly certified family:
the linear span of a commuting conjugation orbit of an ambient LND.
The first coefficient that can descend is determined exactly by the
degree of T(u) under the intrinsic LND. At its smooth threefold fixed
point, a vertical degree of at least two excludes the entire span.

These are consequences of finite conjugation, commuting LNDs and the
tangent representation of Ga. They do not prove that a successful
family exists for every polynomial cylinder. Cancellation remains
UNSOLVED and originality is UNKNOWN. No expert review or formal
verification is claimed.

## 1. Setup and the actual descent obligation

Let k be a characteristic-zero field, let A be a finitely generated
k-domain, and put B=A[u], E=partial_u. Let L be an LND of A, extended
to B by L(u)=0, and let T be an LND of B. We allow L=0; it gives only
the degree-zero special case below. No polynomiality of A is assumed.

For a k-rational point p of Spec A, write m for its maximal ideal.
If T restricted to A has the finite expansion

    T|A = sum_j u^j D_j,

then

    T(m B) subset m B  iff  D_j(m) subset m for every j.       (1)

This follows by reducing each T(a), a in m, in B/m B=k[u].
It is enough to check generators of m. A hypothesis that every
intrinsic LND fixes p controls the highest intrinsic coefficient,
but does not by itself control all lower D_j. Assume m is nonzero,
as it is in the threefold application. If every ordinary
coordinate partial of B=k[X_1,...,X_n] preserved m B, there would
be a contradiction: a nonzero polynomial of minimal total degree
in this proper ideal would have all its partial derivatives zero.
In characteristic zero that polynomial is a nonzero constant.
The missing step is ideal preservation, not ambient transitivity.

The generic fraction-field span theorem in
[33](cross-frame-saturation-pass33.md) does not establish (1).
Its division by a nonzero function need not be valid at p.

## 2. A finite certificate for a commuting conjugation family

Set

    C_j = (ad L)^j(T)/j!,
    T_t = exp(t L) T exp(-t L) = sum_{j=0}^N t^j C_j.          (2)

Here t is an independent scalar parameter, not the cylinder variable.
There is a finite N: on finitely many generators, both exponentials
and their compositions have finite polynomial coefficients. The
direct adjoint proof is retained in
[26, Section 1](moving-plane-lie-pass26.md). Take N to be the last
nonzero coefficient when T is nonzero.

The following conditions are equivalent:

1. [T,(ad L)^j T]=0 for j=1,...,N.
2. [T_s,T_t]=0 for all s,t in k.
3. [C_i,C_j]=0 for all i,j=0,...,N.

Indeed, condition 1 says [T,T_t]=0 coefficientwise. Conjugating gives

    [T_s,T_t] = exp(s ad L) [T,T_{t-s}].                     (3)

Thus 1 implies 2. Expanding in the two independent parameters and
using that k is infinite gives 2 implies 3. The reverse implications
are immediate by expansion. All bracket tests are finite equalities
of derivations, hence can be checked on algebra generators.

Under these conditions, EVERY constant linear combination of the C_j
is an LND. To prove this, choose N+1 distinct scalar times. Vandermonde
interpolation expresses each C_j, and therefore each such combination,
as a constant linear combination of the commuting LNDs at those times.
A finite sum of commuting LNDs is locally nilpotent: for a given
element, the multinomial expansion of a sufficiently high iterate
has a vanishing factor in each term. Commutativity lets that factor
act first. This proves nilpotence; coefficient extraction alone would
not do so.

This is a sufficient operation class, not a claim that arbitrary
conjugate LNDs commute or that arbitrary sums of LNDs are LNDs.

## 3. An exact quotient-and-tangent test in this span

Assume the equivalent conditions of Section 2. For c=(c_0,...,c_N), set

    W_c = sum_j c_j C_j,
    F(c) = sum_j c_j L^j(T(u))/j! in B.                     (4)

Since L(u)=0, the commutator formula gives C_j(u)=L^j(T(u))/j!.
Consequently the following conditions are equivalent:

    W_c descends through B/(u),
    W_c(u) belongs to u B,
    W_c(u)=0,
    F(c)=0.                                                (5)

The middle implication uses local nilpotence, already proved in
Section 2: if a nonzero element f divides W_c(f), the LND degree
identity forces W_c(f)=0. Thus no candidates preserving (u) are
missed by demanding that its generator be killed exactly.

For c in ker F, the quotient action is an intrinsic LND of
B/(u)=A. This does NOT assert that W_c preserves the embedded copy
of A in B or commutes with E. Quotient descent is sufficient here.

Let z=(p,0). Define V(c)=W_c(z) in T_z Spec B. Because W_c(u)=0,
this value is tangent to the section u=0. Its identification with
T_p Spec A is precisely the value of the descended derivation.
Therefore

    some c yields an intrinsic LND nonzero at p
    iff ker F is not contained in ker V.                    (6)

Both maps have finite-dimensional domain. After choosing bases for
their finite-dimensional image spaces, (6) is equivalent to

    rank of the vertically stacked matrix (F; V) > rank F. (7)

This is a complete test WITHIN THIS CERTIFIED SPAN only.

For the actual polynomial-cylinder input B=k[X_1,...,X_n], construct
the F matrix by expanding the finitely many polynomials C_j(u) in
ambient monomials. Construct V by evaluating C_j(X_i) at z. Its n
rows suffice: after (5), a nonzero ambient tangent value is exactly
a nonzero tangent value on the section. Unknown intrinsic polynomial
coordinates are not needed. Over an exact computable coefficient
field and with exact point coordinates, these are finite bracket,
polynomial-coefficient and linear-algebra operations. This statement
does not prescribe approximate arithmetic for arbitrary complex data.

### 3.1. In one orbit, the vertical kernel is an explicit tail

There is a stronger simplification special to (2). Put h=T(u). If h
is nonzero, let e=deg_L h; otherwise put e=-1. For nonzero h, the
polynomials h,Lh,...,L^e h are linearly independent over k. Indeed,
applying L^e to a constant relation first forces the coefficient of
h to vanish. Applying L^(e-1) then forces the coefficient of Lh
to vanish, and continuing proves the assertion. Factorials do not
change independence in characteristic zero. Thus e<=N and

    ker F = {c : c_0=...=c_e=0}.                            (7a)

When h=0, the condition is empty. In particular, higher coefficients
do not cancel lower vertical values in this single-orbit span. Every
descending combination is a combination of the individually
u-killing coefficients C_(e+1),...,C_N. The matrix formulation above
remains correct, but here rank F=e+1 and its kernel is already known.
This statement concerns constant coefficients, not coefficients in A
or combinations assembled from several different conjugation orbits.

## 4. The pointwise bound on adjoint order

Suppose p is smooth and L fixes p. Put M=dL_p on T_p Spec A, and
let v be the horizontal component of T(z) in the actual product
decomposition at z. Then

    C_j(z)_horizontal = (-M)^j v/j!,                       (8)
    C_j(z)_vertical = 0 for j>=1.

To verify (8), the extension of L vanishes at z and its differential
is the block matrix diag(M,0). For any regular vector field H,

    [L,H](z) = -dL_z(H(z)).

Iterating this equality proves (8). This uses the pullback convention
for conjugation in (2); the minus sign is consequential.

The Ga action fixes p, so it induces an algebraic representation on
T_p Spec A. Its differential M is nilpotent. One elementary proof
uses local nilpotence on the finite-dimensional invariant space
m/m^2, then dualizes. If dim A=d and p is smooth, M^d=0. Hence

    C_j(z)=0 for every j>=d, provided d>=1.                 (9)

Combining (7a) and (8), recovery within the certified span is exactly

    M^(e+1) v is nonzero.                                  (9a)

If this vector is nonzero, C_(e+1) itself descends and moves p. If it
is zero, every later power is zero, so no descending combination can
move p. The formula also handles e=-1: T itself kills u and recovery
is exactly v nonzero. If e=N, the identically zero C_(N+1) and (8)
ensure that (9a) fails; there is no missing endpoint condition.

For a smooth threefold the exact conditional tests are:

| Vertical value h=T(u) | Test for recovery in this span |
| --- | --- |
| h=0 | v is nonzero |
| h nonzero and deg_L h=0 | Mv is nonzero |
| deg_L h=1 | M^2v is nonzero |
| deg_L h>=2 | Recovery is impossible |

These are equivalences under the commuting-orbit hypothesis, not
claims that every row is realizable for arbitrary input data. The
last row is an obstruction to the ENTIRE span, not just its highest
coefficient. No coefficient of order at least three can assist
tangent recovery, and no lower vertical values can be canceled by
the later coefficients within this span.

There is a useful separate statement without the commutativity
hypothesis: the highest nonzero C_N is always an LND. For each
generator g, exp(-tL)g has finitely many coefficients, each killed
by a sufficiently high common power of T. Conjugation therefore
gives T_t^r(g)=0 identically for some r. Its highest parameter
coefficient is C_N^r(g), so this also vanishes. Thus if C_N(u)=0
and C_N(z) is nonzero, this highest coefficient alone gives the
desired quotient action. By (9), that route cannot move p when
N>=3 in the smooth-threefold fixed-point setting.

No bound here is imposed on the global adjoint order N. The bound
concerns its value at this particular fixed point.

## 5. Exact control: cancel before extracting the u-top

On A=k[a,b,c], take p=(0,0,0), and set

    L=a partial_b,
    T=partial_a + u a partial_b on A[u].

The whole polynomial coordinates

    (a, b-u a^2/2, c, u)

have inverse (A,B,C,U) -> (A,B+U A^2/2,C,U), and T is their
first coordinate partial. Thus its nilpotence has an actual inverse
certificate. Direct computation gives

    [L,T]=-partial_b,  [L,[L,T]]=0,  [T,[L,T]]=0,
    T_t=T-t partial_b.

All T_t commute. Each has the same u-leading intrinsic coefficient
a partial_b, which vanishes at p. But the whole-family difference
T_t-T_0=-t partial_b is a certified LND killing u and nonzero at p
for t nonzero. The test (7) detects this.

This separates interpolation BEFORE u-top extraction from
interpolation AFTER it. The latter only combines the vanishing
top coefficients. The example does not satisfy the hypothesis
that EVERY intrinsic LND fixes p: partial_b visibly does not.
It is not a counterexample to that stronger hypothesis, and its
known polynomial base is not a cancellation result.

### 5.1. Full tangent span can still have no descending combination

Take instead

    L=a partial_b+b partial_c,
    T=partial_a+c partial_u,
    p=(0,0,0).

Here T is the first partial in the whole coordinates
(a,b,c,u-ac), with inverse (A,B,C,U)->(A,B,C,U+AC). Its orbit
coefficients are

    C_0=partial_a+c partial_u,
    C_1=-partial_b+b partial_u,
    C_2=(partial_c+a partial_u)/2,
    C_j=0 for j>=3.

All three commute, as direct differentiation verifies. Their values
at z=(p,0) span the three-dimensional tangent space to u=0. But their
values on u are c,b,a/2, which are linearly independent polynomials.
Thus NO nonzero combination descends through (u). This is the e=2
boundary of (9a), not a failure of the commutation certificate.
It shows why pointwise tangency cannot replace polynomial ideal
preservation. Again the base is known affine space.

## 6. Why simply subtracting a top is still invalid

Suppose an ambient LND has

    T|A=sum_{j=0}^q u^j D_j,   T(u)=sum_{j=0}^q u^j h_j,
    q>0, D_q nonzero, h_q nonzero.

The standard cylinder degree bound is deg_u T(u)<=q;
[23](leading-derivation-pass23.md) supplies its proof. Although
u^q D_q is an LND, S=T-u^q D_q is NOT an LND. If S moves A,
its horizontal degree is at most q-1 while deg_u S(u)=q,
contradicting that bound. If S kills A, it is an A-linear field
on A[u] with a positive-degree nonzero coefficient on partial_u,
which is also not locally nilpotent.

Subtracting u^q(D_q+h_q E) removes both top coefficients, but
this subtractand is itself not an LND: it sends u to the nonzero
multiple u^q h_q of u. The difference might or might not be an
LND; the subtraction alone does not certify it.

For the retained whole coordinate pair

    x=u+a^2, y=a+x^2,

the x-partial is

    T=-2(u+a^2) partial_a + (1+4a(u+a^2)) partial_u.

Its top stripping gives

    S=-2a^2 partial_a + (1+4a^3+4au) partial_u,
    S^n(a)=(-2)^n n! a^(n+1), n>=1.

The same control shows that Section 2's commutation premise is not
automatic. With L=-2 partial_a, the bracket [T,[L,T]] has
components -32(a^2+u) and 64a^3+64au-8 on a,u respectively.

## 7. Evidence, provenance and remaining task

The core mechanisms are standard or already retained in23,26,33:
finite adjoints, highest-coefficient nilpotence, interpolation,
commuting LND sums, and quotient descent. The contribution of this
pass is an explicit finite selection test that keeps nilpotence,
quotient compatibility and point values separate. It is not a
novelty determination or a general recognition theorem.

Root's fresh unsaved calculation82c23f checked both inverse
compositions in Section 5, coordinate-partial identities, the
two-parameter commuting-family identity, and its nonzero recovered
tangent with unchanged vanishing top. A later assertion in that
same run failed because SymPy's percent operator represented
4*a*u modulo u as u*Mod(4*a,1), not a polynomial remainder.
Fresh ee73de used polynomial division instead, and checked the
eight exact recurrence residuals and the nonzero bracket in
Section 6. These finite checks support the explicit controls,
not the universal propositions, whose proofs are written above.
No saved checker was executed, imported, edited or compiled.

Two full internal AI reviews initially checked the first version and
requested the nonzero-m qualifier in Section 1. Both then verified
that correction. Root subsequently found the stronger argument in
Section 3.1, which also exposed a false explanatory sentence in the
first draft: higher coefficients cannot cancel lower vertical values
in this single orbit. Both reviewers independently reconstructed
the correction. Agreement in the earlier reviews did not certify
that sentence. The original matrix criterion was valid and now
simplifies to (9a).

Fresh bafbd2 verified the entire inverse, all commuting coefficients,
rank-three tangent span and zero descent kernel in Section 5.1.
It also checked the positive degree-zero control T=partial_a+a*partial_u
with the same L. A proposed degree-one control T=partial_a+b*partial_u
failed the required commutation check. That is a failed candidate,
not evidence that the degree-one row is attainable or that the
criterion is false. No such positive degree-one example is claimed.

Fresh1ca771 rechecked the exact vertical kernels of those three
controls and diagnosed the degree-one rejection as the nonzero
bracket 2*partial_u. It completed successfully. The universal cutoff
is proved by the chain-independence argument, not those examples.

The revised 363-line source at SHA256
614838938e503cdc71e81885e7875e07af937f885777cc202b2f2a1cb3f56b08
was read through EOF by root in5c353a, Geometry in d0e60d/badb04,
and General in47e73e/17388e. Both separate reviewers reported
the corrected complete mathematical source CLEAN. This final
addition records review and calculation provenance only. Internal
AI review is not human expert review or formal certification.

For a hypothetical point fixed by every intrinsic LND, every
certified vector in ker F must have zero value. To exclude such
a point, it remains necessary to construct a pair L,T for which
the finite bracket certificates hold and (9a) is nonzero, or to
supply a different valid descent method. Neither existence has
been proved. Even excluding common fixed points would not by
itself supply the independent commuting pair required by639.
The full cancellation goal is unchanged and remains unresolved.
