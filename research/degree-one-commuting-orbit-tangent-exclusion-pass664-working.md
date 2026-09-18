# Degree-one vertical speed cannot recover a tangent in a commuting orbit

Date: September 18, 2026.
Status: complete private working proof, two full-source internal reviews passed.

In the smooth-threefold setting of [662](commuting-orbit-coefficient-tangent-test-pass662-working.md),
the apparent degree-one recovery regime is impossible. The proof uses
the entire fixed cylinder line, not just one orbit through one point.
Its saturation by the commuting coefficient flows is dominant whenever
the proposed recovered tangent is nonzero. This prevents a nonzero
global vertical derivative from disappearing only on the chosen orbit.

The result concerns the certified commuting conjugation span below.
It does not produce such a span for an arbitrary cylinder or exclude
recovery by other operations. General cancellation remains UNSOLVED;
novelty is UNKNOWN. No expert or formal certification is claimed.

## 1. Precise hypotheses and conclusion

Let k be a characteristic-zero field and A a finitely generated
k-domain of dimension three. Let p be a smooth k-rational point of
Spec A. Put B=A[u] and E=partial_u. Let L be an LND of A fixing p,
extended to B by L(u)=0. Let T be an LND of B, and write

    C_j=(ad L)^j(T)/j!,
    T_t=exp(tL) T exp(-tL)=sum_{j=0}^N t^j C_j.             (1)

The sum is finite on algebra generators. Assume that its coefficient
derivations commute pairwise. Equivalently, the whole conjugates T_s,T_t
commute for all scalar s,t, or

    [T,(ad L)^j T]=0 for 1<=j<=N.                           (2)

For completeness, conjugation gives
[T_s,T_t]=exp(s ad L)[T,T_(t-s)]. Coefficient comparison proves these
equivalences. Interpolation at N+1 distinct scalar times expresses
each C_j, and every constant combination of them, as a sum of commuting
LNDs. Thus all these combinations are LNDs. This supplies the complete
polynomial flows used below; no nilpotence of an arbitrary bracket is
being assumed.

Let z_0=(p,0), let M=dL_p on T_p Spec A, and let v be the horizontal
component of T(z_0). The main assertion is

    deg_L T(u)=1  implies  M^2 v=0.                        (3)

Here degree one means h=T(u) is nonzero, Lh is nonzero, and L^2h=0.
No polynomial presentation of A is required. In particular (3) applies
when the supplied cylinder happens to be k^[4].

## 2. The whole fixed line and the adjoint values

Because L kills u, every point z_s=(p,s) on the actual cylinder line
is fixed by L. Its differential there is diag(M,0), independent of s.
For any regular vector field H,

    [L,H](z_s)=-dL_(z_s)(H(z_s)).

Thus, with v(s) the horizontal component of T(z_s),

    C_j(z_s)_horizontal=(-M)^j v(s)/j!,
    C_j(z_s)_vertical=0 for j>=1.                          (4)

The sign corresponds to the pullback conjugation convention in (1).
Since L preserves the maximal ideal of p and is locally nilpotent,
its operator on the three-dimensional space m_p/m_p^2 is nilpotent.
Dualizing gives M^3=0. Consequently

    C_j(z_s)=0 for every j>=3 and every s.                 (5)

These equalities also hold as identities on the line over k: evaluation
on that line is the homomorphism rho_p:B->k[s] sending A to its value
at p and u to s. Equation (5) says rho_p C_j=0. The infinitude of k,
or the same differential calculation over k[s], justifies the identity.

The use of the full line is essential. Merely knowing that an invariant
function vanishes on one three-dimensional orbit in a fourfold would
not imply its global vanishing.

## 3. A dominant saturation map kills all higher adjoints globally

Assume for this section that M^2v is nonzero. Define the polynomial map

    Phi:A^4_k -> Spec B,
    Phi(t_0,t_1,t_2,s)
      = exp(t_0 C_0+t_1 C_1+t_2 C_2)(z_s),                (6)

using the point-action convention whose pullback is

    Theta(b)=rho_p exp(t_0 C_0+t_1 C_1+t_2 C_2)(b).

The derivations commute and are LNDs, so these exponentials are finite
on every b in B. The differential of Phi at the parameter origin has
columns C_0(z_0), C_1(z_0), C_2(z_0), E(z_0). Their horizontal parts are

    v,  -Mv,  M^2v/2,  0.                                (7)

The first three are independent: applying M^2 and then M to a linear
relation proves this successively, using M^3=0 and M^2v!=0. The fourth
column has vertical component one. Hence the differential has rank four.

This proves dominance without presuming that the individual orbits
fill an open set. To see it algebraically, choose four local parameters
at the smooth k-point z_0 represented by elements of B. Their pullbacks
have a nonzero four-by-four Jacobian at the parameter origin, so they
are algebraically independent in characteristic zero. The image of
Theta therefore has transcendence degree four. Since B is an affine
domain of dimension four, a nonzero prime kernel would lower that
dimension. Thus Theta is injective.

For j>=3, commutativity and (5) give, on every b in B,

    Theta(C_j b)
      =rho_p C_j exp(t_0 C_0+t_1 C_1+t_2 C_2)(b)=0.

Injectivity now proves

    C_j=0 globally for j>=3.                              (8)

This is stronger than their original pointwise vanishing. In the present
situation C_2 is nonzero by (7), so the actual global order is N=2.
The conclusion (8) uses M^2v!=0 and the commuting-orbit hypothesis;
there is no universal global order bound for arbitrary L,T.

## 4. The degree-one contradiction

Continue under M^2v!=0 and suppose h=T(u) has L-degree one. Since Lu=0,

    C_1(u)=Lh!=0,   C_2(u)=L^2h/2=0.                     (9)

Let F=Theta(u) in k[t_0,t_1,t_2,s]. Equation (9) and commutativity imply
that F is independent of t_2. By (8), the exact conjugation rules are

    exp(r ad L)C_0=C_0+rC_1+r^2C_2,
    exp(r ad L)C_1=C_1+2rC_2,
    exp(r ad L)C_2=C_2.                                  (10)

The symbol r here is another independent parameter. Since rho_p L=0
and Lu=0, conjugating the exponential in (6) does not change its evaluated
value on u. With the positive signs dictated by (1), this gives

    F(t_0,t_1,t_2,s)
      =F(t_0,t_1+r t_0,t_2+2r t_1+r^2 t_0,s).             (11)

Differentiate in r at zero. Because F_(t_2)=0, equation (11) reduces to

    t_0 F_(t_1)=0.

The parameter ring is a domain, so F_(t_1)=0. On the other hand,
commutativity gives F_(t_1)=Theta(C_1u). Injectivity of Theta therefore
forces C_1u=0, contradicting (9). This proves (3).

No degree of a restricted function was identified with its global
degree. The contradiction explicitly uses the dominant saturation of
all z_s to pass from a pullback identity to a global identity in B.

## 5. The resulting complete test inside the certified span

The linear-independence simplification in corrected662 is elementary.
If h!=0 and e=deg_L h, then

    h, Lh, ..., L^e h are linearly independent over k.

Apply L^e to a relation to kill all but its first coefficient, then
apply L^(e-1) to the remaining relation, and continue. Therefore, for
W=sum_j c_j C_j,

    W(u)=0  iff  c_0=...=c_e=0.                           (12)

For h=0 put e=-1, so (12) imposes no restrictions. Every W is LND by
Section 1. It preserves the ideal (u) if and only if it kills u: the
LND divisibility rule u|W(u) forces W(u)=0. Thus (12) covers every
quotient-preserving combination in this span, not merely selected ones.

Its quotient on B/(u)=A has tangent value

    sum_{j>e} c_j (-M)^j v/j! .                            (13)

Before (3), the first surviving power test was M^(e+1)v!=0. There is
no omitted order restriction: a nonzero such tangent forces the
corresponding C_(e+1) to exist. Equation (3) now excludes the e=1 case,
while M^3=0 already excludes every e>=2 case. Consequently the exact
success classification is

    h=0:              success iff v!=0;
    h!=0 and Lh=0:    success iff Mv!=0;
    Lh!=0:            no nonzero tangent is recovered.     (14)

In the first successful case T itself descends. In the second C_1
descends and is already nonzero at p. Quotient descent need not preserve
the original embedded A or commute with E; local nilpotence descends
through the stable ideal (u).

This is a classification of the specified constant coefficient span,
not of all possible intrinsic LNDs or all nonlinear ambient repairs.
If every intrinsic LND fixes p, neither successful condition in (14)
can occur. No argument here constructs L,T meeting one of them.

## 6. Whole-coordinate controls and the commutation boundary

The following controls use A=k[a,b,c], p=0, L=a partial_b+b partial_c,
and E=partial_u. Put T=partial_a+hE. For h=a,b,c respectively, T is
the first coordinate partial in

    (a,b,c,u-H),  H=a^2/2, ab, ac respectively.

The inverse simply replaces u by the last coordinate plus H. Thus all
three T are actual coordinate LNDs, with no inference from their jets.
Their nonzero adjoint coefficients are

| h | C_1 | C_2 | Commuting orbit? |
|---|---|---|---|
| a | -partial_b | partial_c/2 | yes |
| b | -partial_b+aE | partial_c/2 | no: [T,C_1]=2E |
| c | -partial_b+bE | (partial_c+aE)/2 | yes |

All C_3 are zero. Also v=partial_a, Mv=partial_b and M^2v=partial_c.
The first row realizes the invariant-speed success in (14). The last
has vertical degree two and no nonzero quotient-preserving combination.
The middle row shows why the commuting-orbit premise cannot be dropped:
its highest coefficient C_2 does descend and move p, but the orbit
fails the exact bracket certificate.

For the first and last rows the pullbacks in (6) are respectively

    F=s+t_0^2/2,
    F=s+(t_0 t_2-t_1^2)/2.

Both satisfy (11). The last depends on t_2, exactly as C_2u=a/2 requires.
It therefore supplies no contradiction to Section 4.

## 7. Evidence and scope

The finite conjugation, commuting-LND and tangent mechanisms are retained
in662 and its cited predecessors. This proof adds the fixed-line
dominance argument, which resolves the previously unclassified degree-one
regime. Jet derived the saturation and invariant pullback argument;
root independently reconstructed it and observed that dominance first
makes every higher C_j vanish globally. General independently challenged
the fixed-line, higher-coefficient and dominance steps before this source
was held. These are AI-assisted internal checks, not human peer review.

Fresh unsaved exact calculation066cbe checked the full coordinate inverses
and partials in Section 6, every adjoint and bracket there, the tangent
signs and rank-four determinant, the parameter shear in (10)--(11), and
both displayed invariant pullbacks. The universal proof is Sections 2--4,
not an extrapolation from those controls. No saved checker was executed,
imported, compiled or edited, and no canonical file was changed.

The proof neither supplies a successful commuting conjugation orbit for
an arbitrary actual polynomial cylinder nor establishes the broader
cancellation claim.

## 8. Completed internal saved-source review

The complete held proof had SHA256
dab0de5d731e951a4f5def22cc3282b563f649321865771557f5671c00b27d55,
252 lines/10,862 bytes. Root read its full source in47b71f. Geometry
read through EOF in6f9d58 and rechecked its hash ind96e77. General
read through EOF in832527 and rechecked the source in3b77ba.
Both separate reviews were CLEAN. No mathematical edits were requested.
Only the status and review-provenance text changed afterward.

Root's independent fresh unsaved d3d618 passed both whole commuting
control pullbacks and their parameter invariance, the rank-four
Jacobian determinants, and the exact rejection bracket 2*partial_u
for the degree-one attempted control. General's independent fresh
3b77ba reconstructed the three adjoint/bracket controls and both
pullbacks as well. These checks do not replace the general proof.
