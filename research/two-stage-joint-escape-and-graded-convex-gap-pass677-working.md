# Joint-motion constraints on the two-stage escape problem

Date: September 18, 2026.

Complex-threefold cancellation remains UNSOLVED and novelty UNKNOWN.
This pass strengthens the action-construction gate in676 and checks two
proposed shortcuts. It proves neither polynomiality of the candidate cylinder
nor invariance of the critical plane under all its additive actions.

## 1. Special fiber and exact statement

The unit chart from676 has ring

    Q=C[A,A^(-1),V,b,S,T]/(V²T+b³S+AV+A(A-1)).

Every LND of Q kills the unit A. Its induced derivation on the fiber A=1
is an LND of

    C0=C[V,b,S,T]/(F), F=V²T+b³S+V.                       (1)

The critical plane P in Spec C0 has prime ideal I=(V,b).
C0 is a domain: F is primitive and linear in S over C[V,b,T]. It is smooth:
vanishing of F_S=b³ and F_T=V² forces b=V=0, where F_V=1.

For every LND D of C0,

    D(T)=0 implies D(b)=0,
    D(S)=0 implies D(V)=0.                               (2)

Either premise implies that D preserves I. Therefore a chart LND whose
action moves a point out of the critical plane must move BOTH S and T on
the special fiber. Moving them only by multiples of A-1 does not suffice.
This strengthens676's exclusion of the common kernel of A,S,T. It does not
prove that joint S,T-motion is impossible. Global actions moving A need not
remain LNDs on Q and are outside this chart restriction.

## 2. Proof by complex specialization, without a field-extension assumption

The source used here is Poloni, *Classification(s) of Danielewski
hypersurfaces*, arXiv:0912.3241, Definition2.2 and Theorem3.1, printedpp2--3.
For C[x,y,z]/(x^n y-P(x,z)), n>=2 and deg P(0,z)>=2, it gives ML=C[x].
The definition allows repeated roots of P(0,z). We use it over C only,
not over an unverified arbitrary coefficient field.
[Primary definition and theorem](https://arxiv.org/pdf/0912.3241).

If D(T)=0, then for every c in C*, it induces an LND on

    C0/(T-c)=C[b,V,S]/(b³S+V+cV²).

The theorem applies with x=b,n=3,z=V,P=-V-cV². Thus the image of D(b)
vanishes on this quotient, and D(b) lies in (T-c)C0 for every c!=0.
Inside the injective localization

    (C0)_b=C[b,b^(-1),V,T],

the intersection of those ideals is zero: a polynomial in T over a domain
cannot have every nonzero complex scalar as a root. Hence D(b)=0 in C0.

If D(S)=0, apply the theorem on each S=c!=0 quotient

    C0/(S-c)=C[V,b,T]/(V²T+V+cb³),

with x=V,n=2,z=b,P=-V-cb³. Its residual polynomial -cb³ has a multiple
root, which the cited theorem expressly permits. Thus D(V) belongs to
(S-c)C0 for all c!=0. Use the injective localization

    (C0)_V=C[V,V^(-1),b,S]

to conclude D(V)=0. These two localizations test polynomial identities;
no assertion that D remains locally nilpotent there is needed.

If D(b)=0, reduce D(F)=0 modulo I. Its only surviving term is D(V), so
D(V) lies in I and D preserves I. If D(V)=0, its additive action preserves
the divisor V=0. Its two irreducible components have ideals (V,b) and (V,S).
A connected additive group cannot permute this finite set nontrivially, so
it preserves each component, including I. This proves(2) and its consequence.

For a chart LND, specialize A=1 and apply this argument. If either S or T
is killed on that fiber, the ideal (A-1,V,b) is preserved in Q. This proves
the stated special-fiber joint-motion requirement.

## 3. A free action still has no slice and does not escape

The elementary action

    D1(V)=b³, D1(S)=-(2VT+1), D1(b)=D1(T)=0

is locally nilpotent, with whole polynomial flow

    V_s=V+b³s,
    S_s=S-(2VT+1)s-b³Ts²,
    b_s=b, T_s=T.                                        (3)

The inverse has parameter -s. It is nowhere zero because in C0

    1=(2VT+1)²+4Tb³S.                                    (4)

Thus its additive action is free, but it preserves P by Section2.
It has no slice. Indeed, after inverting b its kernel is C[b,b^(-1),T].
The contraction is C[b,T]: if b^(-n)g(b,T) lies in C0 with n>0 minimal,
then g(0,T)=0 in C0/bC0. The inclusion C[T] into that quotient is injective
(its component V=0 already has ring C[S,T]), so b divides g, a contradiction.

If a slice existed, the slice theorem would give C0=C[b,T][s]. However,
at b=0,T=c!=0 its fiber is

    C[V,S]/(V(1+cV)) = C[S] times C[S],

not a polynomial line. This contradiction shows that freeness of this
specific action does not provide a slice or a polynomial-coordinate frame.

## 4. An exact graded presentation, without claiming a Cox-ring lift

Consider the auxiliary domain

    Ctilde=C[p,q,v,w,T]/(q³w-p³vT-1),
    deg_Pic(p,q,v,w,T)=(1,-1,-3,3,0).                     (5)

Here Pic is just a label for the coarse integer grading, not an asserted
identification with a Picard group.

Its degree-zero subring is EXACTLY C0 under

    b=pq, V=p³v, S=-vw, T=T.                             (6)

To prove generation, take a weight-zero monomial p^i q^j v^k w^l T^h.
Remove (vw)^min(k,l). If k>=l, its remainder is a product of powers of
pq,p³v,T. If l>=k, it is a product of powers of pq,q³w,T. Use q³w=1+VT.
The relation F pulls back to -p³v(q³w-p³vT-1). For injectivity, invert b.
Then p,q are units, and Ctilde_b=C[b,b^(-1),V,T,p,p^(-1)], with only p of
nonzero Pic-degree. Its degree-zero subring equals (C0)_b. Both original
rings are domains and inject into these localizations, proving injectivity.

This construction does not invoke a Cox-ring identification, a universal
torsor, or a theorem lifting every action of C0. Those would be additional
claims and are not needed for the negative grading test below.

Use the finer Z³-grading with basis e_p,e_q,e_T and weights

    wt(p)=e_p, wt(q)=e_q, wt(T)=e_T,
    wt(v)=-3e_p-e_T, wt(w)=-3e_q.

Pic-degree is projection (d_p,d_q,d_T) -> d_p-d_q. Define

    Dplus=T³(q³ partial_v+p³T partial_w),
    Dminus=p²v²w(p³v partial_q+3q²w partial_T),
    Dzero=q²w partial_p+p²vT partial_q.                  (7)

Each preserves the defining relation. Dplus and Dminus are LNDs: each is
an invariant replica of the displayed triangular derivation. Their fine
degrees are respectively (3,3,4) and (-4,-4,-3), both of Pic-degree zero.
They fix p. Dzero has degree (-1,-1,0), also Pic-degree zero, but moves p
modulo(p), since q²w remains nonzero when q³w=1.

Dzero is NOT locally nilpotent. On C0 it induces

    Dzero(b)=1+2VT, Dzero(V)=-3b²S, Dzero(S)=Dzero(T)=0.

This is the negative of676's elliptic tangent derivation at A=1. At S=T=1
it is a nonzero derivation of the smooth genus-one curve V²+V+b³=0, which
cannot admit a nonzero LND, as proved in676.

## 5. The precise failure of the convex-degree shortcut

In the plane of Pic-zero fine degrees, write (d,e) for (d,d,e). Then

    (-1,0)=(3/7)(3,4)+(4/7)(-4,-3).                      (8)

Thus the degree carrying the p-moving tangent component lies strictly
between degrees of two legitimate p-preserving homogeneous LNDs. A linear
functional cannot strictly separate that degree from both permitted ones.
The principle that extreme homogeneous components of an LND are LNDs is
therefore insufficient for the proposed convex separation alone.

This is NOT an example of an escaping LND with those three components.
No local nilpotence of Dplus+Dzero+Dminus is claimed. Nor is a classification
of fine-homogeneous LNDs silently applied to every Pic-homogeneous LND.
Interior support and an all-action lifting premise would require additional
arguments. The explicit degree configuration blocks the suggested shortcut,
not the possibility of a more substantial graded proof.

## 6. The actual polynomial-cylinder premise remains unused by the shortcut

In this section A denotes the unknown three-ring in cancellation, not the
auxiliary unit function denoted A in the chart.

A parallel primary-source audit found no applicable theorem that supplies
normality of the cusp fiber from the actual A[u]=C^[4] hypothesis. Masuda's
Theorem4.3 requires every closed fiber of the induced map f_Y:Y->A1 on the
Ga-quotient Y to be factorial. These are not the fibers of the quotient
map pi:X->Y itself. Example4.2 discusses a Russell-cylinder instance of
this missing premise.
The cusp times A1 is not normal, hence not factorial.
[Exact theorem and example](https://arxiv.org/pdf/2512.06687).

Das--Dutta Theorem3.13 uses affine fibrations whose fibers at EVERY prime
are polynomial, not just their general fibers. The bad fiber fails that
definition. Choosing the separate cylinder variable as base instead makes
the required fiber polynomiality exactly the unknown polynomiality of A.
[Definition in Section2 and Theorem3.13](https://arxiv.org/pdf/2002.02128).

Even under an actual B=C^[4], absolute differential freeness does not repair
this: for a nonconstant function a,

    Omega_(C[a])(B)=B^4/(B*da).

At a critical point its residue-vector-space dimension is four, versus
three off the critical locus. Therefore this relative module is not locally
free there and cannot be stably free. This is a failed theorem application,
not a contradiction to B being polynomial as an ABSOLUTE C-algebra.

## 7. Verification and remaining task

General and Jet independently derived the fixed-parameter restrictions.
Root read Poloni's exact definition/theorem and the other two primary
theorem hypotheses. General independently checked the graded presentation
and all fine degrees. Root's fresh unsaved5f657e verified(3), its inverse,
(4), the graded relation, the two triangular nilpotence bounds, the descent
of Dzero, and the strict convex identity. Jet's unsavedba5e15 checked the
whole free action separately. These are exact checks supplementing proofs,
not an exhaustive classification of possible LNDs.

The complete225-line source was held at SHA256
c9931f28ec0bf42d15b463bb214f41bf484fc60af8f7ab762893f8101531859f.
General (a6725d/2018c9/ba3b80), Geometry (72cd0e/bc8037), and Jet
(f69f29/5075ac) each read it through EOF and reconstructed the arguments.
General and Geometry returned CLEAN. Jet found no algebraic defect and
requested the precise distinction between the two morphisms in Masuda's
hypothesis, now supplied in Section6. All reviews finished before that
wording clarification and this provenance update. No theorem is changed.

No saved checker was run, imported, compiled, or edited. No novelty claim,
contact, or submission is made. Human and formal verification remain absent.
The next escaping-action attempt must permit nonzero joint S,T-motion on
the special fiber, or be a global action moving A. No such action is
established here. The main cancellation objective remains active.
