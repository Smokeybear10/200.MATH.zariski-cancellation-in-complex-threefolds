# A last-stage denominator forces cylindrical prime fibers

Status: proved elementary presentation obstruction, with published
examples as controls. September 17, 2026. Novelty is not asserted;
general cancellation and the modification-recognition problem remain
unsolved. All rings in this note are over k, the complex numbers.

## 1. Exact global hypothesis

Let R=k^[3], let D be a nonzero locally nilpotent derivation, and
let A=ker(D). Suppose there is an actual A-algebra presentation

    R = A[T0,...,TN]/(a_i T_i-G_i(T0,...,T_(i-1)) : 1<=i<=N),

where N>=1 and each a_i is a nonzero element of A. No extra
saturation of the displayed ideal is allowed in this hypothesis.
Let pi be an irreducible element of A dividing the LAST a_N.

**Proposition.** There is an integral affine curve S over k with

    Spec(R/pi R) = S x A^1.

In particular this prime hypersurface has no isolated singular
point. The earlier a_i need not be divisible by pi.

## 2. Proof

Factorial closure of the kernel says that any factors in R of
an invariant are invariant. Since R and A have the same units
k*, irreducibility of pi in A makes it irreducible in R. The
polynomial ring R is a UFD, so pi is prime in R.

Reduce the exact presentation modulo pi. None of the first N-1
relations contains T_N. In the last relation its coefficient a_N
vanishes, leaving -G_N, which also does not contain T_N. Therefore

    R/pi R = B[T_N],

where B is the quotient of (A/pi)[T0,...,T_(N-1)] by the reduced
first N-1 relations and G_N. Since R/pi R is a domain, B is a
domain. It is a finitely generated k-algebra, and dimension gives
dim B+1=dim(R/pi R)=2. Thus S=Spec B is an integral affine curve.

Over k, the singular locus of S x A^1 is Sing(S) x A^1. One can
check this using regular local rings under polynomial extension,
or the Jacobian criterion. An integral affine curve over k is
generically smooth and has finitely many singular points. The
product is consequently either smooth or has singular locus a
nonempty finite union of affine lines. It has no isolated singular
point. This proves the proposition.

The proof fails for a merely localized presentation: a removed
point of Spec R may be exactly the singular point in question.
It also fails if the displayed equations must be saturated. Extra
relations introduced by saturation can involve T_N modulo pi.

## 3. Consequence for the two-stage proposal

The proposed global model

    R = A[r,y,z]/(f y-G(r), f z-H(r,y))

is a special case. Every prime pi dividing f must cut out a curve
cylinder in R, not a surface with an isolated singularity. This
condition is independent of whether D is primitive or r minimal.

For the published Dasgupta--Gaifullin family, write

    F=xz-y^m,  m>=2,
    pl(D)=(F^n h),  n>=1.

The invariant F is a coordinate of the invariant plane and is
prime in R. The surface R/FR has a single singular point: its
gradient is (z,-m*y^(m-1),x), which vanishes exactly at the origin.
Hence F cannot divide the last coefficient of any exact global
triangular presentation of the kind in Section 1 for these inputs.

Thus extending the local description over F=0 to the whole ring
with last denominator divisible by F is impossible, including for
the n=2 examples in the first-nonreduced-plinth investigation.
There is no need to assume that D(r) is a square for this exclusion.
If one additionally proposes D(r)=f^2, the plinth divides f^2 and
forces F to divide f, giving the same contradiction. This does
not contradict localized Masuda presentations: those may remove
the origin. Dividing D by another plinth factor after localization
does not automatically define a derivation on the original ring.

The family, rank-three assertion, and minimal local slice giving
the stated plinth are published in
[Dasgupta--Gaifullin, Theorem 5.7 and proof](https://arxiv.org/html/2306.00510v2#S5).
The isolated-singularity argument here is a direct calculation.

## 4. A genuine two-stage control is not automatically one stage

The following exact example is the PUBLISHED derivation in
[Dasgupta--Gaifullin, Example 4.15](https://arxiv.org/html/2306.00510v2#S4).
It is a control, not a new example. Put R=k[x,y,z] and

    r=xz-y^2,  s=r^2-xy,
    D(x)=0, D(y)=2xr, D(z)=x+4ry.

Direct calculation gives D(r)=x^2 and D(s)=0. Also D^3(y)=0
and D^5(z)=0, so D is locally nilpotent on the entire polynomial
ring. Its coefficients have gcd 1, so it is primitive.

The exact kernel is A=k[x,s]. Indeed,

    R_x=k[x,x^(-1),s,r],  D=x^2 partial_r.

The natural map A/xA -> R/xR sends s to y^4 and is injective.
Thus xR intersect A=xA; successive cancellation of x gives
A_x intersect R=A, proving the kernel assertion.

There is the global two-stage presentation

    R = k[x,s,r,y,z]/(xy-r^2+s, xz-r-y^2).

It is exact because the two equations eliminate s and r,
respectively, leaving the polynomial coordinates x,y,z. Its
plinth is exactly (x^2): a generator must divide D(r)=x^2.
Principality here is the standard polynomial-three-ring plinth
theorem, also recorded as DG Theorem 2.10.
If the generator were x or 1, a suitable local slice would imply
r modulo x belongs to the image k[y^4] of A/xA. This is impossible
because r modulo x is -y^2.

Nevertheless NO w in R gives R=A[r,w]. If it did, reduction
modulo x would give k[y,z]=k[y^2,wbar]. Localizing the nonzero
elements of k[y^2] yields

    k(y)[z] = k(y^2)[wbar].

The right side has transcendence degree one over k(y^2), so wbar
would be transcendental. In a rational function field in one
variable the ground field is relatively algebraically closed.
But the left side contains y, which has degree two over k(y^2).
This contradiction proves the assertion. Thus even a rank-at-most-
two input can genuinely need more than one extra generator over
its fixed kernel and local slice. The converse of621 is false.

## 5. What this changes, and what it does not

The standard rank-three controls exclude promoting the localized
one/two-stage descriptions to exact global presentations of the
same simple kind. A successful global approach must retain the
omitted locus and permit more general centers, relations, or
changes of action. Iterating KVZ is not licensed when the
intermediate threefold has not been proved polynomial.

A cylindrical prime divisor alone need not be a coordinate
divisor: X^2-Y^3 defines a cusp cylinder, and XY-1 defines
G_m x A^1 in k[X,Y,Z]. These boundary examples do not satisfy
the full primitive-plinth setup and prove no negative result
about that setup. No general rank bound for all two-stage
presentations is established here.

The whole control identities, primitivity and nilpotence on
generators were freshly checked by root in0189da. The cylinder
proof is algebraic, not inferred from a finite experiment. The
primary DG source was read in turn5184view0. No frozen checker
was run, imported or compiled. A separate saved-source review
is required before canonical acceptance. No human expert or
formal-proof certification has occurred.
