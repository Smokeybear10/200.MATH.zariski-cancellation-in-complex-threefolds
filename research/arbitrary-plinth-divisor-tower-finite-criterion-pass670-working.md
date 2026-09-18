# Arbitrary plinth multiplicities: exact divisor towers and a finite image test

General cancellation remains UNSOLVED and novelty UNKNOWN. This proof extends
the divisor calculation and finite exact test of668 to arbitrary multiplicities.
It does not prove that the test passes, or recognize an arbitrary threefold as
affine space when it does. The local tower is consistent with established PID
classification; no priority is claimed for the elementary reconstruction.

## 1. Full hypotheses and result

Let k=C, A a finite-type factorial k-domain of dimension three, D a primitive
nonzero locally nilpotent derivation, and suppose

    C=ker D=k[a,b],      pl(D)=pC,      Dr=p,
    p=product_i f_i^e_i,       e_i>=1.                            (1)

Scalar units are suppressed. The f_i are distinct prime elements of C and r
is the supplied minimal local slice. A polynomial cylinder is NOT assumed.
If p is a unit, the slice theorem already settles all the statements below
with no boundary primes. We therefore take p nonconstant.

For O_i=C_(f_i), kappa_i=Frac(C/f_i), R_i=A tensor_C O_i, write

    R_i/f_i R_i=L_i[t],        d_i=[L_i:kappa_i].                 (2)

Primitivity and factoriality imply (2), with L_i a finite separable field
extension. This is the elementary residual-curve argument in668, Section2.
No smoothness of the entire exceptional surface A/f_i A is asserted.

There are integers, with repetitions permitted,

    2<=d_(i,1) | d_(i,2) | ... | d_(i,e_i)=d_i,                 (3)

and exact embedded triangular models for R_i retaining r. For every N>=0,
put I_N=D^N(A) intersect C, I_0=C. Then

    h_N=product_i f_i^( e_i*N - sum_(j=1)^e_i floor(N/d_(i,j)) ),
    I_N**=h_N C,       I_N=h_N J_N,                             (4)

where J_N is an actual ideal of C with unit localization at every height-one
prime. One finite closed set of Spec C supports every C/J_N simultaneously.

Let M=lcm(d_1,...,d_s). Then the exact finite criterion is

    every I_N is principal  iff  J_0=J_1=...=J_M=C.              (5)

Repeated d_(i,j) in (4) MUST be counted with multiplicity. M is determined
by the terminal residual-field degrees, not by discarding repeated terms
from the valuation formula. Equations (4)--(5) are all-degree statements,
not interpolation from finite numerical checks.

## 2. Construction at one divisor

Suppress i. Write f=f_i, e=e_i, O=C_(f), kappa=Frac(C/f), K=Frac(C),
R=A tensor_C O, and p=f^e beta with beta in O*. The residual ring is
T=R/fR=L[t], with nonzero induced derivation delta and ker delta=L.

Set y_0=r, d_0=1 and L_0=kappa. We construct y_1,...,y_e in R.
At stage j, let L_(j-1)=kappa[y_0bar,...,y_(j-2)bar]. The variables already
listed are algebraic invariants, so this subalgebra is a finite field.
The next residue y_(j-1)bar is also invariant for j<=e. Let n_j be its
minimal-polynomial degree over L_(j-1), and set

    L_j=L_(j-1)[y_(j-1)bar],       d_j=d_(j-1)*n_j.

The minimal polynomial is separable. Express its coefficients in the
kappa-basis consisting of reduced monomials in earlier residues, and lift
their scalar coefficients to O. This gives a polynomial

    G_j(Y_0,...,Y_(j-1))=Y_(j-1)^n_j + lower terms,
    deg_(Y_h) of each lower term < n_(h+1) for all h<j.          (6)

There is no denominator problem in this coefficient lift: a finite algebraic
subalgebra of a field over kappa is already a field, and the iterated monic
minimal polynomials give exactly the stated mixed-radix vector-space basis.
Set

    y_j=G_j(y_0,...,y_(j-1))/f in R.                            (7)

Membership follows from the actual vanishing of G_j in T, not formal division
in an abstract presentation. The claim that all required residues are
invariant, used in the induction, follows next.

### 2.1. Each stage lowers the derivative valuation by exactly one

For 0<=j<=e, induction gives

    Dy_j in f^(e-j) R,
    f^(j-e) Dy_j mod f
      = beta_bar * product_(h=1)^j (G_h)_(Y_(h-1))(ybar) != 0.  (8)

For j=0 the product is empty and this is Dr=f^e beta. Differentiate (7).
In f^(-1) sum_(h<j) (G_j)_(Y_h) Dy_h, only h=j-1 can contribute modulo
f after removing f^(e-j); earlier h have at least one additional factor of f.
The surviving derivative is nonzero by separability. For j<e, (8) says y_jbar
is invariant, so the next minimal polynomial exists. At j=e, it instead says
delta(y_ebar) is a nonzero element of L_e. Consequently y_ebar is
transcendental over L_e in T.

The first degree n_1 is at least two. If rbar belonged to kappa, a lift c in O
would give (r-c)/f in R and D((r-c)/f)=f^(e-1) beta. This contradicts the
localized full plinth f^e O. Localization of the plinth is valid because all
denominators are invariant. Later n_j may equal one.

## 3. Exact quotient, mixed-radix basis and whole-ring saturation

For 1<=j<=e form the raw quotient

    H_j=O[Y_0,...,Y_j]/(fY_h-G_h : 1<=h<=j).                   (9)

It evaluates into R using (7). Give Y_h weight d_h. Every lower monomial in
G_h has weight at most

    sum_(q=0)^(h-1) (n_(q+1)-1)*d_q = d_h-1.                 (10)

Order monomials by weight, then lexicographically with earlier variables
larger. Replacing Y_(h-1)^n_h by fY_h minus lower terms strictly decreases
this well-founded order. Thus H_j is spanned over O by

    y_0^a_0 ... y_j^a_j,
    0<=a_h<n_(h+1) for h<j,       a_j>=0.                     (11)

Inside R_f=K[r], y_h is a polynomial of degree d_h and leading coefficient
f^(-b_h), where

    b_0=0,       b_h=n_h*b_(h-1)+1
                   =sum_(q=1)^h d_h/d_q.                    (12)

Equation (10) prevents cancellation of its leading term. The monomials in
(11) have distinct r-degrees, one for each nonnegative integer. Their images
are therefore O-linearly independent. This proves both that (11) is a basis
and that (9) has no extra kernel or hidden f-torsion.

At the final stage, reduction of the exact quotient gives

    H_e/fH_e=L_e[Y_e].                                      (13)

Its map to R/fR is injective: it is injective on the constructed field L_e,
and (8) makes y_ebar transcendental over that field. Hence

    H_e intersect fR=fH_e,       (H_e)_f=K[r]=R_f.

For z in R, the least N with f^N z in H_e is zero by this saturation equality.
Therefore R=H_e. Comparing the invariant fields of (13) with ker delta=L
also proves L_e=L, and hence d_e=[L:kappa].

This gives e unit-denominator stages, not a claim that e is the minimal number
of additional generators. If some n_j=1, variables can be eliminated and some
degrees repeat. It does not give a global model over the two-dimensional C.

## 4. Exact image valuations and the global finite gate

For the unique basis monomial E_N in (11) of degree N, its denominator exponent
in the leading coefficient is

    sum_(h=0)^e a_h*b_h = sum_(j=1)^e floor(N/d_j).             (14)

This follows by substituting (12); the mixed-radix expression shows
floor(N/d_j)=sum_(h=j)^e a_h*d_h/d_j. Since D=f^e beta partial_r,

    D^N E_N = N! beta^N f^(eN-sum_j floor(N/d_j)).             (15)

Every element of R is a unique finite O-linear combination of these basis
monomials. Its largest nonzero basis index equals its derivation degree,
because distinct degrees cannot cancel. Consequently

    (ker D^(N+1)) tensor_C O = direct sum_(q=0)^N O E_q,
    I_N O = f^(eN-sum_j floor(N/d_j)) O.                     (16)

All factorials and beta are units. At primes not dividing p, the local-slice
identity makes I_N a unit ideal. The height-one intersection in the UFD C
now proves (4). In particular J_N has support only at closed points.

One finite closed set works for all degrees. For each i, clear the finitely
many invariant denominators of the ENTIRE tower, and those expressing a
finite C-algebra generating set of A in it. Also invert the other plinth
factors. Their product c_i is not divisible by f_i. On D(c_i) the actual
whole-ring tower and its degree-distinct basis hold, so every J_N is a unit
there. The same is true on D(p). The complement

    Z=V(p,c_1,...,c_s)

contains no height-one point and is finite or empty. It supports every C/J_N,
without a degree-dependent choice of open cover.

Because each d_(i,j) divides M, (4) gives h_(N+M)=h_N*h_M. Leibniz's rule
in the highest nonzero degree gives

    I_N I_M subset I_(N+M),       J_N J_M subset J_(N+M).       (17)

If J_0,...,J_M are unit ideals, induction in every residue class modulo M
makes all J_N unit. The converse is immediate. An I_N is principal exactly
when J_N=C, since its height-one valuations already fix its generator up to
a unit. This proves (5). No unproved higher-image gcd property is used.

Also p^N/h_N belongs to J_N. In particular J_N=C for N smaller than every
first degree d_(i,1). These automatically verified degrees do not in general
reach the finite cutoff M.

If the test passes and actual witnesses e_j satisfy D^j e_j=j!h_j for
0<=j<=M, then e_(qM+j)=e_M^q e_j, 0<=j<M, give witnesses in every degree.
Subtracting the appropriate top coefficient inductively proves they form a
C-basis of A. Thus A is free of rank M over C[e_M], with basis e_0,...,e_(M-1).
This is a finite algebraic extension statement, not a polynomial recognition.

## 5. Scope, countercontrols and deduplication

For e=1 this is668. For e=2 the local formula is

    2N-floor(N/n)-floor(N/(nm)),        n>=2, m>=1.

The basis and formula for a SUPPLIED two-stage presentation are already in
[632](two-stage-mixed-radix-basis-and-image-ideals-pass632-working.md).
The additional licensing step here puts every actual primitive height-one
localization with plinth exponent two into that presentation, retaining r.
Sections2--3 extend the same licensing to arbitrary e.

The published polynomial two-stage example retained in
[622](global-triangular-presentation-cylinder-obstruction-pass622-working.md)
has x*y=r^n-s and x*z=r+y^m, n,m>=2. No one extra element generates it over
the supplied C[r], despite its being affine three-space. This does not exclude
a single modification with a multi-generator center. The case m=1 repeats the degree and gives
2N-2floor(N/n), as in a single relation f^2*z=G(r)+fK(r).

Neither repeated factors nor principal images decide cancellation. The known
Koras-Russell controls in625 and668 are nonpolynomial smooth factorial
contractible threefolds satisfying all their exact image equalities. No
polynomial cylinder for those controls is established in this investigation.
The actual cylinder must still enter a separate recognition argument.

Local tower existence is already supplied by Barkatou-El Kahoui's published
PID classification, Theorem3.1 and Lemma4.4, cited and scope-checked in668.
Root reread the exact theorem and General the complete relevant induction
and proof in the author-uploaded primary text. This note reconstructs the
needed local statement directly instead of applying a PID theorem to the plane C.
The finite-gate argument is exactly the periodicity mechanism of668, now with
the all-multiplicity divisor formula licensed. No novelty clearance is claimed.

## 6. Verification status

Root, General, Geometry and Jet independently reconstructed the arbitrary-e
induction. The complete 249-line source was then held at SHA256
b0a506e0084baeab4790a25aa7fbd2cd32f344a63924738b4a11eabe2790277a.
General (87cd84/fa99de), Geometry (8b3431), and Jet (797cea/666258/dc02b8)
each read the whole saved source through EOF and returned CLEAN. After every
review finished, root clarified the one-extra-generator scope above, credited
the published existence theorem more explicitly, and added this provenance.
The mathematical proofs and conclusions are unchanged.
Fresh unsaved root algebra78524e passed 182 normalized mixed-radix samples for
e=1,...,4, including repeated degrees, and exact top-derivative witnesses.
An earlier synthetic fixture9f5b7b failed because it included an unreduced
earlier variable when a radix equaled one, violating (6). The corrected fixture
restricts every lower monomial to its prescribed radix range; no theorem
hypothesis was changed. Finite checks do not prove the all-degree assertions.
Saved checker scripts were not executed, imported, compiled or edited.

AI review is not human expert review or formal certification. The general
cancellation goal remains active, with no public claim or external contact.
