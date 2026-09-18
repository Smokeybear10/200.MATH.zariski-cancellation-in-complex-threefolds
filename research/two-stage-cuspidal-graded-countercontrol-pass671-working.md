# A genuine two-stage cuspidal control with polynomial graded data

General cancellation remains UNSOLVED and novelty UNKNOWN. This note proves
that the complete image ideals and associated graded algebra of a supplied
action do not recognize affine three-space, even for a smooth factorial
contractible threefold with smooth reduced plinth support and two genuinely
nonlinear modification stages. It does not establish a polynomial cylinder
for the negative control, and therefore does not disprove cancellation.

## 1. The pair of rings and the exact conclusion

Work over k=C. Fix integers n,m,q>=2 with gcd(q,n*m)=1. Put C=k[a,b] and

    R=C[r,y,z]/(a*y-r^n-b^q-a, a*z-y^m+r).                  (1)
    P=C[r,y,z]/(a*y-r^n+b,     a*z-y^m+r).                  (2)

On each ring define the derivation D by

    Da=Db=0, Dr=a^2, Dy=n*a*r^(n-1),
    Dz=m*n*y^(m-1)*r^(n-1)-a.                              (3)

The minus sign in Dz is essential. Both actions are primitive locally
nilpotent derivations with kernel C and FULL plinth a^2*C. If
I_N=D^N(R) intersect C, and likewise for P, then for every N>=0,

    I_N=a^(2*N-floor(N/n)-floor(N/(n*m)))*C.                 (4)

The D-degree filtrations have the same graded C-algebra, with the same
induced degree-minus-one derivation:

    gr_D R = gr_D P
      = C[rho,upsilon,zeta]/(rho^n-a*upsilon,
                             upsilon^m-a*zeta),            (5)
    weights(rho,upsilon,zeta)=(1,n,n*m).

Nevertheless P=k[a,y,z], while R is not a polynomial three-ring. In fact
Spec R is smooth and factorial, is diffeomorphic to R^6, and has
Makar-Limanov invariant ML(R)=k[a]. The topology and nontriviality step
uses the published theorem precisely identified in Section5.

The comparison identifies the abstract base rings k[a,b] and the displayed
graded generators. It does not identify the filtered rings, their entire
derivation modules, or their cylinders.

## 2. Exact quotients, the basis, and image ideals

Substitute into C[a^(-1)][r]:

    y=(r^n+b^q+a)/a, z=(y^m-r)/a                           (6)

for R, and replace the first numerator by r^n-b for P. In the raw quotient,
the replacements r^n -> a*y-b^q-a and y^m -> a*z+r show that

    E_N=r^i*y^j*z^h,  0<=i<n, 0<=j<m, h>=0,
    N=i+n*j+n*m*h                                         (7)

span over C. For P use its corresponding first replacement. Termination
follows from weighted degree followed by lexicographic order r>y>z:
every replacement strictly reduces this order. The leading r-coefficient
of (7) under (6) is

    a^(-j-(m+1)*h),                                       (8)

and its r-degree is N. Every nonnegative integer has one mixed-radix
expression in (7). Thus distinct spanning monomials have distinct r-degrees
and are C-linearly independent in the localization. This proves the raw
quotients inject there, proves they are domains without hidden a-torsion,
and proves (7) is a basis of each ENTIRE ring. In particular

    R_a=P_a=k[a,a^(-1),b,r].                               (9)

Direct differentiation of both defining relations gives zero under (3).
In (9), D=a^2*partial_r. It is locally nilpotent on the whole ring because
every element has finite r-degree. By distinctness of the degrees in (7),
the D-degree of a nonzero C-linear combination is its largest basis index.
Hence ker D=C, and

    D^N E_N=N!*a^(2*N-j-(m+1)*h).                          (10)

Here floor(N/n)=j+m*h and floor(N/(n*m))=h. An element whose Nth derivative
is invariant has D-degree at most N; its Nth derivative is exactly the top
C-coefficient times (10). This proves (4) in every degree. Factorials are
units in k. Taking N=1 proves the full plinth is a^2*C.

The leading homogeneous relations are those in (5). The same reduction and
degree-distinct basis prove that they generate the full homogeneous relation
ideal, not just an ideal contained in it. The induced graded derivation is

    Dbar(rho)=a^2,
    Dbar(upsilon)=n*a*rho^(n-1),
    Dbar(zeta)=m*n*upsilon^(m-1)*rho^(n-1).                 (11)

Thus the entire graded algebra and action agree, not just the Hilbert ranks
or a finite list of image ideals. The finite criterion of670 passes in both
examples, with no closed-point image-ideal defect.

## 3. Smoothness, factoriality, primitivity, and genuine stages

Eliminating r from (1) gives

    R=k[a,b,y,z]/(F),
    F=a*(y-1)-(y^m-a*z)^n-b^q,
    r=y^m-a*z.                                            (12)

The exact exceptional fiber is

    R/aR=k[b,y,z]/(y^(n*m)+b^q).                           (13)

The coprimality assumption makes this binomial irreducible. Thus a is
prime. Since (9) is a UFD, the prime-element form of Nagata's criterion
makes R a UFD. Also R*=k*: any unit becomes c*a^d in R_a, and primality
and noninvertibility of a rule out d!=0 for a unit of R.

Off a=0, (9) proves smoothness. On a=0 use

    F_a=y-1+n*z*r^(n-1),
    F_b=-q*b^(q-1),
    F_y=a-m*n*y^(m-1)*r^(n-1),
    F_z=n*a*r^(n-1).                                      (14)

At a possible singular point F_b=0 forces b=0, and (13) then forces y=0
and r=0. But F_a=-1 there. Thus the entire threefold is smooth, including
the line over the cusp. This does not claim smoothness of the intermediate
first modification: it has a singular point (a,b,r,y)=(0,0,0,1).

A common nonunit divisor of all D-images would divide Dr=a^2, so would
have a as a prime divisor. However

    Dz mod a = m*n*y^(n*m-1) != 0 in R/aR.                 (15)

Therefore D is primitive. The positive control P is visibly polynomial:
eliminate r=y^m-a*z and then b=r^n-a*y. These substitutions give mutually
inverse maps P=k[a,y,z]. Its reduction modulo a is k[y,z], and (15) proves
primitivity there as well. The reduced plinth support a=0 in Spec C is
smooth in both cases; its multiplicity in the full plinth is two.

Both stages are genuinely nonlinear at the generic point of a=0. With
kappa=k(b), the negative control has successive constant fields

    kappa subset kappa(rbar) subset kappa(ybar),
    rbar^n=-b^q, ybar^m=rbar,                              (16)

of degrees n and m. Indeed ybar^(n*m)=-b^q is irreducible over k(b) by
coprimality, and rbar=ybar^m. The positive control has rbar^n=b and the
same respective degrees n and m. These are the tower degrees in670.

There is no w with R=C[r,w], and the same is true for P. To see this, reduce
modulo a and localize the invariant coefficients to the field kappa(rbar).
The actual ring becomes L[zbar], with [L:kappa(rbar)]=m>1, where
L=kappa(ybar). A presentation by one generator would make it
kappa(rbar)[wbar]. Its transcendence degree forces wbar transcendental;
but a one-variable polynomial ring has no larger algebraic constant field.
This contradicts the copy of L. Replacing r by c*r+h(C), c in k*, does
not change C[r]. This excludes one extra generator over the supplied C[r],
not a single affine modification with a multi-generator center.

## 4. Whole polynomial flow

For a flow parameter tau, put

    U_tau=sum_(j=1)^n binom(n,j)*a^(2*j-2)*r^(n-j)*tau^j.

The exponential of D is the following polynomial formula, with a,b fixed:

    r_tau=r+a^2*tau,
    y_tau=y+a*U_tau,
    z_tau=z+sum_(ell=1)^m binom(m,ell)*a^(ell-1)
                         *y^(m-ell)*U_tau^ell-a*tau.        (17)

All exponents are nonnegative. Binomial expansion proves both relations
are preserved, for both R and P. On the injective localization (9), this
is translation in r; hence composition adds parameters and the inverse
has parameter -tau on the WHOLE rings. No division by a is being silently
performed on the exceptional fiber.

## 5. Nonnormal boundary, topology, and the exact ML invariant

Let X=Spec R and E=V(a). The cusp b^q+y^(n*m)=0 has normalization

    y=t^q, b=xi*t^(n*m), xi^q=-1.

Coprimality makes this normalization finite and bijective. In the complex
topology it is a homeomorphism, since the finite map is proper. Thus
E is homeomorphic to C^2. It is not normal: t is integral and rational over
k[t^q,t^(n*m)] but does not belong to that subring. Its singular locus is
the entire line b=y=0 in E. In particular E is not factorial.

Set U=X\E. Equation (9) gives U=C* times C^2. With integral coefficients,

    H_c^3(U)=H_c^3(E)=0.

The compact-support exact sequence gives H_c^3(X)=0. Smoothness and
Poincare duality for the oriented real six-manifold X give H_3(X;Z)=0.

Kaliman, *Polynomials with general C2-fibers are variables*, Pacific J.
Math.203 (2002), Lemma II, printed pp.162--163, now applies: X is smooth,
factorial, has only constant units and H_3=0, contains an actual open
C2-cylinder, and its excluded irreducible component is not factorial.
The theorem gives X diffeomorphic to R^6, X not isomorphic to C^3, and
ML(R)!=k. This imports the published lemma and its dependencies; this note
does not independently reconstruct its general ML or diffeomorphism proof.
[Primary journal text](https://msp.org/pjm/2002/203-1/pjm-v203-n1-p08-s.pdf).

For the exact invariant, define a second derivation Delta by

    Delta(a)=Delta(r)=0, Delta(b)=a^2,
    Delta(y)=q*a*b^(q-1),
    Delta(z)=m*q*y^(m-1)*b^(q-1).                          (18)

It preserves both relations. On R_a it is a^2*partial_b, hence locally
nilpotent on R, and it commutes with D. Its kernel is k[a,r]. Indeed the
localized kernel is k[a,a^(-1),r]; a negative a-denominator in an element
of R would contradict injectivity k[r] -> R/aR, where rbar=ybar^m is
transcendental over k. Iterating this denominator argument proves equality.

Therefore ML(R) is contained in ker D intersect ker Delta=k[a]. The
published nontriviality supplies a nonconstant f(a) in ML(R). For ANY LND
Theta of R, 0=Theta(f(a))=f'(a)*Theta(a), so Theta(a)=0 in characteristic
zero. Consequently

    ML(R)=k[a].                                           (19)

This is an invariant of R, not a computation of ML(R[u]). No claim of
motivic A1-contractibility or polynomiality of R[u] follows from this section.

## 6. Prior work and exact scope of the obstruction

The closest constructional antecedent located is Dubouloz--Pauli--Ostvaer,
*A1-contractibility of affine modifications*, arXiv:1805.08959v1, Eq.(1.15):

    x^n1*z=(x^n2*y+z^m)^alpha1+t^alpha2
             +x*p(x,x^n2*y+z^m,t).

Our formula (12) matches its shape under
(x,z_paper,y_paper,t)=(a,y,-z,b), alpha1=n, alpha2=q, p=1,
but with n1=n2=1. The displayed published parameter range requires BOTH
n1,n2>=2. We do not import its motivic results at excluded parameter values,
infer that R is abstractly absent from existing classifications, or claim
a new family. This is an explicit exponent-one two-stage cuspidal control
analogous to published iterated Koras-Russell constructions.
[Primary preprint, p.3](https://arxiv.org/pdf/1805.08959).

Retained48,625 and668 already contain one-stage or different-support
Koras-Russell controls with principal higher images. Retained632 proves
the mixed-radix formula for a supplied two-stage presentation. What is added
here is the exact paired control with n,m>=2, smooth reduced plinth support,
and identical ENTIRE graded C-algebra and action, including every image ideal.
The underlying variety and these deductions have not received novelty
clearance. Internal literature searches are not a proof of novelty.

This invalidates the implication from those data plus smoothness,
factoriality and ordinary contractibility to exceptional-fiber normality
or polynomial recognition. It does NOT invalidate a statement assuming an
ACTUAL polynomial cylinder. That assumption has not been established for R.
The remaining route must use more than the filtration data enumerated here.

## 7. Verification status

Before drafting, General, Geometry and Jet independently checked the proposed
family at argument level. General and Geometry also checked the source
hypotheses; Jet directly checked those during the full saved-source review.
Root reopened Kaliman pp.162--163 and the precise preprint parameter range
in this continuation. Fresh unsaved symbolic checks in the preceding research
pass verified complete flows, defining relations, the Jacobian unit ideal,
and derivative witnesses through degree12 for (n,m,q)=(2,2,3),(2,3,5),(3,2,5).
Root separately checked both commuting actions and the positive polynomial
inverse for (2,2,3). These finite tests support, but do not replace, the
all-parameter and all-degree proofs above.

The complete 272-line draft was held at SHA256
d294be3e5a4222b88dd645ff2fa9b5bc92fb300deccb0e00f3527de8425150a7.
General (819d61/f68e2b), Geometry (b5edfc/fd62ed), and Jet
(19b532/b5c212/38fd05) each read it through EOF and returned CLEAN.
All reviews finished before this provenance-only update. The mathematical
proofs and conclusions are unchanged. The separate sequel672 computes the
cylinder ML invariant without asserting a polynomial cylinder.

Saved checker scripts remain frozen and were not executed, imported, compiled
or edited. AI review is not human expert review or formal certification.
No submission or contact has been made. The complete cancellation objective
remains active.
