# One common centralizer field gives an intrinsic polynomial translation

Date: September 18, 2026. Private conditional theorem. Novelty: UNKNOWN.

For a principal polynomial retraction over C, every nonzero intrinsic
derivation commuting with ALL the raw projected coordinate partials is
locally nilpotent and has a slice. Local nilpotence need not be an input.
The special projection identities are essential; arbitrary polynomial
gauges of a tangent frame are not covered.

This is conditional on finding a nonzero common centralizer. Section 5
shows that the common centralizer can be ZERO even on an actual polynomial
cylinder. No existence theorem for an unknown cancellation input follows.

## 1. Hypotheses and the projection identities

Let n>=1, B=C[z_0,...,z_n], and let rho:B -> A subset B be a
C-algebra retraction with nonzero principal kernel (s). Thus A is a
domain, A=B/(s) abstractly, and s is a nonzero nonunit. A product
presentation B=A[s] is NOT assumed. Define

    r_i=rho(z_i), q_i=(z_i-r_i)/s, e_i=rho(q_i),
    h_i=rho(partial_i s), D_i=rho partial_i|A.

The identities and module presentation from
[654](commuting-projected-partials-retraction-recognition-pass654-working.md)
are

    sum_i h_i e_i=1,
    D_j(r_i)=delta_ji-h_j e_i,
    Der_C(A)=(sum_i A D_i),
    ker(A^(n+1) -> Der_C(A))=Ae.

For completeness, Taylor-expand s at z=r+s q, cancel s, and apply
rho to get the first identity. Differentiating z_i=r_i+s q_i gives
the second. The polynomial chain rule applied to V composed with rho
gives V=sum_i V(r_i)D_i for any V in Der_C(A). Applying a relation
to all r_i then identifies its coefficients as a multiple of e.

The first identity makes the gradient of s unimodular on B/(s),
so A is a smooth affine domain of dimension n. Its cotangent module
is the finite projective module A^(n+1)/Ah. Also A*=C*, since a
unit and its inverse stay units in B.

**Theorem.** If 0!=X in Der_C(A) satisfies [X,D_i]=0 for every i,
then X is locally nilpotent and there exists v in A with X(v)=1.
Consequently A=(ker X)[v], by the slice theorem.

## 2. Commutation confines the coefficient functions to one curve

Set b_i=X(r_i). Since X commutes with each D_j, differentiating the
relation sum_i e_i D_i=0 gives X(e)=lambda e for some lambda in A.
Applying X to the displayed formula for D_j(r_i) now gives

    D_j(b_i)=-e_i(X(h_j)+lambda h_j).                 (1)

Over K=Frac(A), the D_j span Der_C(K). Thus the matrix in (1)
has rank at most one and the differentials of the b_i span dimension
at most one. In characteristic zero this bounds the transcendence
degree of C[b_0,...,b_n] by one.

If every b_i is constant, some b_i is a nonzero constant because X
is nonzero and the r_i generate A. Then X^2(r_i)=0 for every i,
so X is locally nilpotent, and r_i/b_i is a slice for any nonzero b_i.

Otherwise the transcendence degree is exactly one. The polynomial
curve-factorization theorem supplies a nonconstant f in B and
polynomials P_i in C[T] such that

    b_i=P_i(f),   f in Frac(C[b_0,...,b_n]).          (2)

The exact source is
[de Bondt, Corollary 3.2 and Lemma 3.3](https://arxiv.org/pdf/1501.06046).
It supplies a polynomial parameter in the original ambient ring, not
an ambient coordinate. This is the same imported input used in
[656](three-commuting-projected-partials-unit-normal-recognition-pass656-working.md),
not a new curve-factorization assertion.

In fact f belongs to A. For any element p/q in B intersect Frac(A),
with p,q in A and q nonzero, apply rho to q(p/q)=p. This gives
rho(p/q)=p/q, proving B intersect Frac(A)=A. Apply this to (2).

Let S(T) be a gcd of the nonzero derivatives P_i'(T), and put
C_i(T)=P_i'(T)/S(T), with C_i=0 when P_i'=0. At least one
derivative is nonzero, and the tuple C_i has gcd one in C[T].
Choose j with D_j(f) nonzero. Equation (1) and the chain rule show
that

    e_i=k C_i(f) for all i, for some k in K*.

Indeed the scalar X(h_j)+lambda h_j cannot vanish for this j,
since at least one P_i'(f)D_j(f) is nonzero. Bezout for the C_i
then gives k in A. The equality sum h_i e_i=1 makes k a unit,
so k is a nonzero complex scalar.

The equation X(e)=lambda e therefore becomes

    C_i'(f)X(f)=lambda C_i(f) for every i.           (3)

If X(f)=0, (2) gives X^2(r_i)=0 for all i. Local nilpotence follows
on the entire finitely generated algebra by the iterated product rule.

If X(f) is nonzero, eliminate lambda from (3). The resulting
Wronskians C_i'C_j-C_i C_j' vanish at the transcendental element f,
and hence vanish as polynomials in T. All nonzero ratios C_i/C_j
are constant in characteristic zero. As their polynomial gcd is one,
the entire tuple C_i is constant, and therefore e is constant.

## 3. The constant-normal branch and the slice in every case

When e is constant, the argument of654 applies. Here are its decisive
steps to keep the conclusion separate from a Jacobian-conjecture claim.
The constant ambient derivation T=sum e_i partial_i is nonzero and
locally nilpotent. The identity sum h_i e_i=1 gives

    T(s)=1+sQ, Q in B.

If Q were nonzero, its right side would have T-degree at least that
of s, while the left side has degree one smaller. Thus Q=0. Choose
linear coordinates Y_1,...,Y_n,t with T=partial_t. Then
s=t+F(Y), A=C[w_1,...,w_n] with w_i=rho(Y_i), and the transformed
raw projected fields are partial_(w_i) and zero. These are constant
linear combinations of the original D_i.

An X commuting with every D_i therefore commutes with each coordinate
partial. Its coefficients in the w-frame are constants. A nonzero such
X is a constant translation, hence locally nilpotent and sliced.

It remains to supply a slice in the nonconstant-curve branch X(f)=0.
Let I=(b_0,...,b_n) be the coefficient ideal of X. It is nonzero.
For any a in A, X(a) belongs to I because the r_i generate A.
Commutation gives

    D_j(b_i)=X(D_j(r_i)) in I.

Thus I is stable under the D_j, hence under every derivation of A.
A smooth affine complex domain has no proper nonzero ideal stable
under all its derivations. A direct proof, including nonradical ideals,
is as follows. Localize at a maximal ideal containing a putative such
ideal. In this regular local ring choose a nonzero element of the
ideal of least finite positive maximal-ideal order d. Finite order
follows from Krull separation. The associated graded ring is a
polynomial ring over C. Some tangent partial derivative of the
nonzero degree-d initial form is nonzero in characteristic zero.
Smoothness lifts that tangent vector to a local derivation. Applying
it produces an element of the localized ideal of order d-1, a
contradiction. Stability localizes, and derivations localize because
the cotangent module is finite projective. Therefore I=A.

Consequently gcd(P_0,...,P_n)=1 in C[T]. Otherwise the evaluation
of a nonconstant common divisor at f would divide every b_i, hence
be a unit of A. This contradicts A*=C* and f nonconstant. Choose
Q_i in C[T] with sum Q_i P_i=1. The explicit element

    v=sum_i Q_i(f) r_i

satisfies X(v)=1, because X(f)=0. This proves the theorem in every
branch. The product assertion follows by the finite Taylor retraction
sum_j (-v)^j X^j/j!, or the usual slice theorem.

## 4. Positive controls and a necessary boundary qualification

An actual nonconstant coefficient-curve example is obtained on
B=C[a,f,c,u], A=C[a,f,c], E=partial_u by using ambient coordinates

    z0=a, z1=af+u, z2=c+af^2+2fu, z3=f.

Their whole inverse is

    a=z0, f=z3, u=z1-z0z3, c=z2-2z1z3+z0z3^2.

Projection at u=0 has

    r=(a,af,c+af^2,f), e=(0,1,2f,0),
    (D0,D1,D2,D3)=(partial_a+f^2 partial_c,
                  -2f partial_c, partial_c, partial_f).

The derivation X=partial_a commutes with all four fields. Here
b=(1,f,f^2,0), the curve parameter f is in ker X, and a is a slice.
This directly tests the nonconstant-curve, nonconstant-normal branch.

Do NOT assert X^2(r_i)=0 universally. In the constant-normal example
B=C[x,y,z,t], rho fixes x,y,z and sends t to -x^2. Its kernel is
(t+x^2), its raw fields are partial_x,partial_y,partial_z,0, and
e=(0,0,0,1). The field X=partial_x centralizes all of them and has
a slice, but X^2(r_t)=-2. The square-zero generator bound is only
part of the relevant branch of the proof.

The new criterion also applies to the c-independent family658 at
its original slice: partial_c commutes with all four projected fields.
When that family's q is nonconstant and F nonlinear,658 proves that
no slice and no constant linear frame supplies the complementary-basis
certificate656. Thus the present condition can succeed where that
certificate fails. These are already polynomial examples, not newly
recognized unknown cancellation kernels.

## 5. Existence fails for a supplied frame, even on affine three-space

Use the actual frame of702 at h=0. Two of its raw projected fields are

    D=a partial_b+b partial_c,
    V_alpha=partial_a-c^2 D.

If X commutes with all four raw fields, it commutes with these two.
Put Z=X(c). The equation [X,D]=0 implies

    X(b)=D(Z), X(a)=D^2(Z).

The c-component of [X,V_alpha]=0 then yields

    partial_a Z=-2bc Z.

No nonzero polynomial in C[a,b,c] satisfies this equation: its left
side has strictly smaller a-degree than its right side, whose nonzero
coefficient -2bc is independent of a. Hence Z=0 and X=0.
Thus the common centralizer of ALL four raw fields is zero in this
genuine polynomial-cylinder example. A nonlinear adapted frame instead
has the usual three constant translations in its common centralizer.
This negative assertion concerns the displayed slice, not every slice.

## 6. Attribution, checks, and remaining obligation

The projection matrix, exact relation module and constant-normal theorem
are from654. The polynomial-curve argument and retraction descent are
adapted from656 and the cited de Bondt result. The differential-ideal
argument is a standard smoothness fact, proved above. The new retained
conditional test concerns one field centralizing ALL raw projected
partials, not a preselected commuting basis or the centralizer of just
the supplied ambient LND. Bounded archive and primary-source comparison
did not locate an identical statement; that is not novelty clearance.

Root and General independently developed the rank-one differential
argument. General supplied the slice upgrade, separately reconstructed
by root, Jet and Geometry. Root freshly checked both inverse orders
and all projected coefficients in Section 4, and the unrestricted
differential identity underlying Section 5. The finite controls do not
replace the general proof. Complete saved-source reviews are recorded
in the ledger. No saved checker was executed, imported, compiled or edited.

The centralizer equations are linear in the unknown field, unlike
local nilpotence itself, but a nonzero polynomial solution in a useful
ambient frame has NOT been proved to exist. The countercontrol forbids
assuming existence in every supplied frame. Arbitrary nonlinear changes
still require a new construction. Corrected complex-threefold cancellation
remains UNSOLVED and novelty UNKNOWN. No expert review or proof-assistant
certification is claimed, and Luo has not confirmed the working scope.
