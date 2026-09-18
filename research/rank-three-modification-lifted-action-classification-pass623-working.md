# Actions fixing the plinth or modification denominator are replicas

September 17, 2026. Source-dependent working theorem, with a complete
algebraic reduction below. Novelty is UNKNOWN. This does not classify
all actions on the modified threefold and does not solve cancellation.

## 1. Statement on the actual modification

Work over k=C, the complex numbers. Let R=k[x,y,z], let D be a
primitive locally nilpotent derivation of rank three, and put

    A=ker(D),  pl(D)=pA,  D(r)=p,  rho=rad(p).

Here r is a minimal local slice and rho is a squarefree generator.
Choose a NONZERO Q in A and set

    V=1+rho Q,  M=R[r/V],  w=r/V,  Delta=VD.

Then V is nonconstant and (p,V)A=A. The previously established
[modification presentation](arbitrary-invariant-kernel-pass18.md) and
[preserved-action calculation](global-modification-bridge-pass19.md) give

    M=R[W]/(VW-r),  M_V=R_V,  ker_M(Delta)=A,
    Delta(w)=p,  pl(Delta)=pA,  M^[1]=k^[4].

**Theorem.** As sets of derivations of M,

    {Theta in LND(M) : Theta(p)=0}
       = {Theta in LND(M) : Theta(V)=0}
       = {Theta in LND(M) : Theta(R) is contained in R}
       = {b Delta : b in A}.

The zero derivation is included. In particular, any nonzero action
fixing p, fixing V, or preserving the specified original polynomial
subring has kernel A. Fixing p or V does NOT initially assume that
the action preserves R. There is no plinth-multiplicity bound:
p dividing rho^2 is NOT used.

## 2. A necessary and sufficient lifting test

Put I=(V,r)R. For any k-derivation L of R, its unique extension to
Frac(R) restricts to a derivation of M if and only if

    L(V) in I and L(r) in I.                         (1)

Indeed, the extension must satisfy

    V L(w)=L(r)-w L(V).                              (2)

The exact presentation gives

    M/VM=(R/I)[w].                                  (3)

If the extension preserves M, reducing (2) modulo V shows that
the polynomial L(r)-w L(V) has both coefficients zero in R/I.
This is valid even when that coefficient ring is nonreduced.
Conversely, write

    L(r)=Va+rb,  L(V)=Vc+rd,  a,b,c,d in R.

Then the fraction-field formula becomes the polynomial expression

    L(w)=a+(b-c)w-dw^2,

so the extension preserves all generators of M. This proves (1).

If L is locally nilpotent, its extension is locally nilpotent on M
if and only if

    L(V)=0 and L(r) in I.                            (4)

For necessity, (1) implies L(V)=V(c+dw) in VM. For a locally
nilpotent derivation Theta on a characteristic-zero domain, a
nonzero f with Theta(f) in fM must satisfy Theta(f)=0: otherwise
the additive Theta-degree on products contradicts
deg_Theta(Theta(f))=deg_Theta(f)-1. Apply this with f=V.
For sufficiency, L(V)=0 extends L as an LND of R_V. Condition (1)
then preserves M, so its restriction to M is locally nilpotent.

The sufficient direction is also the standard modification-lifting
result of [Kaliman--Zaidenberg, Corollary 2.3](https://arxiv.org/pdf/math/9801076),
printed page 11. The necessity here uses the specific exact
one-fraction presentation, not a converse to that general theorem.

## 3. Fixing V forces the original kernel

Let L be a nonzero LND of R with L(V)=0. Since V-1=rho Q is
nonzero, factorial closure of ker(L) gives L(rho)=0. Every prime
factor of rho is also invariant under L, so L(p)=0.

The polynomial p is nonconstant: if it were a unit, D would have
a slice and R=A[r/p] would give rank one, contrary to rank three.
Thus A intersect ker(L) contains the nonconstant p.

Suppose ker(L) is different from A. The kernel-intersection theorem
for two LNDs of k^[3] gives elements f,g with

    A=k[f,g],  A intersect ker(L)=k[f].

Consequently p belongs to k[f]. The variable-transfer lemma says
that a variable f of A is a variable of R if a local slice has
nonzero derivative in k[f]. Apply it to D(r)=p. This would make
f an actual ambient coordinate fixed by D, contradicting rank
three. Therefore

    ker(L)=A.                                       (5)

No commutation of D and L is assumed. The source obligations are
[Dasgupta--Gaifullin, Theorem 2.13 and Lemma 2.15(ii)](https://arxiv.org/html/2306.00510v2#S2),
which record the intersection theorem and the transfer lemma
attributed there to Freudenburg and Daigle. These are imported
theorems, not newly proved results of this note.

## 4. The exact multiplier

Equivalent nonzero LNDs are proportional over the fraction field
of their common kernel, so (5) gives L=aD, a in Frac(A). Write
this fraction in lowest terms in the UFD R. Its denominator must
divide D(x), D(y), and D(z). Primitivity of D makes that denominator
a unit. Hence a belongs to R; since D(a)=0, in fact a belongs to A.

The local-slice theorem and the fact that p is a unit modulo V give

    R/VR=(A/VA)[r],  R/I=A/VA,  I intersect A=VA.      (6)

These identities include all nonreduced V. They follow by inverting
p, which does not alter either quotient, and using R_p=A_p[r].

Now (4) for L=aD requires ap in I. Equation (6) and invertibility
of p in A/VA force a in VA. Write a=Vb with b in A. Conversely,
VbD fixes V and sends r to Vbp in I, so (4) supplies the LND
extension bDelta on M.

Finally, an LND Theta of M preserving R restricts to an LND L of
R. If L=0, its extension to the common fraction field is zero,
so Theta=0. Otherwise the preceding argument applies and the
extension is unique. This proves the R-preserving equality. The
next section proves the stronger intrinsic fixing conditions.

## 5. Fixing p on M already forces preservation of R

Let Theta be a nonzero LND of M satisfying Theta(p)=0. Put

    A'=ker_M(Theta),  C=A intersect A'.

The polynomial p is nonconstant by Section 3, so trdeg_k(C)>=1.
Both A and A' have transcendence degree two. If C also had
transcendence degree two, Frac(A) would be algebraic over Frac(C).
Since Frac(C) is contained in Frac(A'), and Frac(A') is relatively
algebraically closed in Frac(M), this would put A inside A'. Two
nested LND kernels of the same transcendence degree are equal:
every element of A' is algebraic over Frac(A), and the same
relative algebraic closedness gives A'=A. Here we also use the
basic identity M intersect Frac(A)=A, and its counterpart for A'.
Consequently, if A' differs from A, then trdeg_k(C)=1.

The stable polynomiality M^[1]=k^[4] puts M in Daigle's class
C_s(k), in particular in C(k). In his notation A_i(M) denotes
intersections of LND kernels of transcendence codimension i.
Thus C belongs to A_2(M) and A belongs to A_1(M).
[Daigle, Corollary 5.5(a),(b)](https://arxiv.org/pdf/1806.10742)
then gives actual elements f,g such that

    C=k[f],  A=C[g]=k[f,g].                          (7)

The membership hypotheses are licensed by his Definition 1.2,
Definition 5.1, and Proposition 5.3.4. No commutation hypothesis,
polynomiality of M, or separately assumed finite generation of C
is needed. Corollary 5.5 follows there from Theorem 4.14.

Because p lies in C, equation (7) makes p a polynomial in the
variable f of the ORIGINAL kernel A. Apply DG Lemma 2.15(ii) to
the ORIGINAL polynomial ring R, with D(r)=p. It makes f an actual
coordinate of R, contradicting rank(D)=3. This argument does not
apply that polynomial-ring lemma to the unrecognized ring M.
It follows that A'=A.

Write K=Frac(A). The local-slice theorem gives

    (A minus {0})^(-1) M=K[w].

Both nonzero derivations are K-LNDs of this one-variable polynomial
ring, hence Theta=b Delta with b in K. The ring M is a UFD and
Delta is primitive, by the two-chart calculation cited in Section 1.
Writing b in lowest terms in M shows that its denominator divides
every value of Delta and is therefore a unit. Thus b is in M;
since it is also in K, b belongs to A. This proves

    {Theta in LND(M) : Theta(p)=0}=A Delta.           (8)

Now suppose Theta(V)=0. Since V-1=rho Q is nonzero, factorial
closure of ker(Theta) implies Theta(rho)=0 and hence Theta(p)=0.
Equation (8) applies. Conversely, each bDelta fixes both p and V
and preserves R. Together with Sections 2--4, this proves all
the equalities in the theorem, including the zero derivation.

In particular, preserving either principal ideal pM or VM is
equivalent here to fixing its generator: the LND divisibility
lemma in Section 2 applies. Any action with kernel different
from A must move both p and V and must fail to preserve R.

## 6. Two essential scope controls

Preserving the center ideal alone does NOT preserve local nilpotence.
For R=k[x,y,z], V=x, r=y, the LND L=y partial_x preserves (x,y).
Its extension to M=k[x,w,z], y=xw, satisfies

    L(x)=xw,  L(w)=-w^2,  L(z)=0,
    L^n(w)=(-1)^n n! w^(n+1) for every n>=1.

It is a derivation, but not an LND. This elementary control is for
the lifting test, not for the rank-three assumptions of Section 1.

Nor does the theorem prove that M is semi-rigid. It does not control
actions moving both p and V and failing to preserve R. In the
already recognized polynomial families, there must be independent
actions of precisely this unrestricted kind.
In fact, no action in the displayed class has a slice: M has only
scalar units and pl(Delta)=pA is proper, so no bDelta can send an
element to 1. Therefore, if polynomial coordinates on M are found,
each of their coordinate partials necessarily moves p and V and
some element of the original R outside R.

The Q=0 exception is essential. Then V=1, M=R, and every LND of
R preserves R and fixes V, not only the replicas of D. Identity
(8) alone remains true at Q=0, but the displayed full equality
does not. The theorem does not
assert that all modifications are nonpolynomial, that all their
LNDs have kernel A, or that an independent action would by itself
prove polynomiality.

## 7. Verification boundary

Root directly read DG Theorem 2.13, Lemma 2.15, the equivalence
principle and degree facts in turn5193view0, and KZ Corollary 2.3
in turn5194view1. Geometry and General separately reconstructed
the full argument and source hypotheses before this file was
written. Jet and General independently reconstructed the stronger
Section 5 argument and checked the actual Daigle hypotheses.
Root read Definition 1.2 in turn5209view0, Definition 5.1 through
Corollary 5.5 in turn5213view1/2, and Theorem 4.14 and its proof
in turn5214view1. Root rechecked DG Lemma 2.15(ii) in turn5214view0.
Their agreement is not human expert review.

Fresh unsaved root calculation87d935 checks the entire polynomial
extension formula and the countercontrol's iterates; induction
proves the all-n identity. No finite computation certifies the
universal kernel-intersection step, which rests on the stated
primary theorem. No frozen checker was run, imported or compiled.
Saved-source review is still required before canonical acceptance.

This result rules out the plinth-fixing, denominator-fixing and
R-preserving sources of independent actions on the actual M.
It does not supply the missing action that moves those data,
a coordinate system, or arbitrary four-variable entry. General
cancellation remains UNSOLVED; novelty and expert review remain
unestablished.
