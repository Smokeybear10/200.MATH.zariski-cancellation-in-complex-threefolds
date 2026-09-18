# Scalar slice filters cannot universally lower orbit degree

A fixed scalar Taylor filter that preserves polynomial coordinate frames
for every sliced action of bounded orbit degree must act on those frames
as a nonzero dilation of the slice. Such a dilation preserves orbit
degree. This rules out a full class of universal degree-lowering formulas,
not the existence of a problem-specific coordinate change.

The proof uses a two-variable polynomial automorphism extended by two
unchanged variables. Its invariant ring is already a polynomial ring.
Nothing here is a counterexample to cancellation, and no historical
novelty is asserted.

## 1. The precise universal claim

Fix an integer d at least two and complex constants c_0,...,c_d with
c_0=1. For an actual polynomial four-ring B with locally nilpotent
derivation E and supplied slice s, define the linear operator
\[
\mathcal T(f)=\sum_{j=0}^{d}c_j s^j E^j(f).
\tag{1}
\]
Here E(s)=1. The condition under consideration is that, for every
polynomial coordinate frame x_1,...,x_4 satisfying E^{d+1}(x_i)=0,
the four elements T(x_i) are again a polynomial coordinate frame.
The same constants are used for every action, slice and input frame.
They may depend on the chosen bound d.

**Theorem.** This universal coordinate-preservation condition holds
if and only if there is k in C* such that
\[
c_j=\frac{(k-1)^j}{j!}\qquad(0\le j\le d).
\tag{2}
\]
In that case, writing B=A[s] with A=ker E, the images of the input
coordinates are exactly their images under the automorphism fixing A
and sending s to ks. Every nonconstant-in-s input coordinate has
the same E-degree before and after this operation.

The finite operator (1) need not equal that automorphism on elements
of E-degree greater than d. Only the specified input generators and
the degree-at-most-d subspace are identified with the dilation.

## 2. One actual frame forces every coefficient

Work in B=C[a,s,b,c] with E=partial_s. Take the polynomial frame
\[
x_1=s+a^2,\qquad x_2=a+x_1^d,\qquad x_3=b,\quad x_4=c.
\tag{3}
\]
Its inverse is a=x_2-x_1^d, s=x_1-(x_2-x_1^d)^2, b=x_3,
c=x_4. Thus this is an actual polynomial automorphism, not merely
a map with a nonzero Jacobian. Its two-by-two determinant in the
ordered variables (a,s) is -1. The E-degrees are 1,d,0,0, so the
frame meets the required bound and contains a genuinely degree-d
coordinate.

For 0<=n<=d, define the weight multipliers
\[
r_n=\sum_{j=0}^{n}c_j\frac{n!}{(n-j)!},\qquad
r_0=1,\qquad k=r_1=1+c_1.
\tag{4}
\]
The operator sends h s^n to r_n h s^n whenever h is in A.
With independent symbols u and s, put
\[
G_d(u,s)=\sum_{n=0}^{d}\binom dn r_n u^{d-n}s^n.
\tag{5}
\]
The images of (3) are therefore
y_1=a^2+ks, y_2=a+G_d(a^2,s), y_3=b, y_4=c.
Direct differentiation, without assuming they generate B, gives
\[
\det\frac{\partial(y_1,y_2)}{\partial(a,s)}
=-k+2a\bigl((G_d)_s-k(G_d)_u\bigr)(a^2,s).
\tag{6}
\]

If this frame is a polynomial coordinate system, its determinant
must be a nonzero complex constant, by the chain rule with its
polynomial inverse. At a=0 equation (6) takes the value -k, so
k is nonzero and that is the constant determinant everywhere.
The second term in (6) must consequently vanish. The substitution
C[u,s] -> C[a,s], u -> a^2, is injective: distinct monomials
u^i s^j map to distinct monomials a^{2i}s^j. Since C[a,s] is a
domain, this proves (G_d)_s=k(G_d)_u.

For 0<=n<d, the coefficient of u^{d-n-1}s^n in this last identity is
\[
d\binom{d-1}{n}\bigl(r_{n+1}-k r_n\bigr)=0.
\tag{7}
\]
Characteristic zero now gives r_n=k^n for every 0<=n<=d.
The coefficient system (4) is triangular in c_0,...,c_d with
nonzero diagonal n!. It has a unique solution. The binomial identity
k^n=sum_j binom(n,j)(k-1)^j shows that solution is precisely (2).
This proves necessity from the single actual frame (3).

## 3. Sufficiency and the failure of degree lowering

The slice presentation B=A[s] is part of the hypothesis, not a
claim that A is a polynomial three-ring. If (2) holds, then for any
f=sum_{n=0}^{d}a_n s^n with a_n in A, equations (1) and (4) give
\[
\mathcal T(f)=\sum_{n=0}^{d}a_n k^n s^n=f(ks).
\tag{8}
\]
The substitution fixing A and sending s to ks is an automorphism
of B, with inverse s -> k^{-1}s. It therefore sends every original
coordinate frame of the specified degree bound to a coordinate
frame. If a_n is the nonzero leading coefficient, then a_n k^n
is nonzero, proving that its E-degree is unchanged.

Equivalently, the image formula comes from the actual independent-time
flow exp(tE) by substituting t=(k-1)s after forming that flow. It
must not be confused with exponentiating the variable-coefficient
derivation (k-1)sE. The latter is not the finite Taylor operation
in (1).

In particular, no choice of constants in (1) can both preserve all
such polynomial frames and uniformly remove their degree-d terms.
Uniform removal would require r_d=0, whereas coordinate preservation
has forced \(r_d=k^d\ne0\).

## 4. Relation to the quadratic reduction and the main problem

For d=2, write \(c_1=\lambda\) and \(c_2=\mu\). The theorem says
that the only universal possibilities are \(\mu=\lambda^2/2\) and
\(\lambda\ne-1\). Their quadratic weight is \((1+\lambda)^2\),
necessarily nonzero.
The [quadratic filter analysis](quadratic-flow-filter-obstruction-pass81.md)
records the minimal explicit determinant obstruction and its own
finite checker.

The earlier [projection calculation](quadratic-slice-projection-pass74.md)
already distinguishes a slice retraction's four generators from a
polynomial coordinate system. It also shows why ordinary projection
degree is different from orbit degree. The present obstruction is
about universal scalar modifications of the coordinate generators,
not about ordinary spatial degree or invariant-ring generation.

The [nice-action working theorem](nice-slice-recognition-pass80.md)
requires a polynomial frame whose generators have E-degree at most
one. The argument above rules out obtaining that frame uniformly
from all bounded-degree frames by (1). It does not rule out nonlinear,
frame-dependent changes, invariant-dependent coefficients, a useful
change of supplied slice, or a recognition argument that never
constructs a nice frame. Those remain distinct obligations in the
general cancellation problem.

The full argument is elementary and written above. A finite symbolic
check of selected d values is only a check of examples; it cannot
replace the coefficient proof for arbitrary d. Independent proof
review and exact test records are recorded separately in the pass81
audit. This is private working mathematics, not human-reviewed or
formally verified mathematics.
