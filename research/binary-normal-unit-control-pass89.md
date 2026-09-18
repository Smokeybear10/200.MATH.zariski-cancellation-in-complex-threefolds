# Removing the ramification factor before substituting a unit binary pair

This exact parameter-only control illustrates the normal-row step in
the [conical-normal lemma](constant-acceleration-conical-normal-pass89.md).
Its raw derivative cross product has a nonconstant common factor.
After removing that factor, substitution of a unit binary pair gives
a polynomial normal with an explicit Bezout row. No original
four-coordinate additive action is constructed.

## 1. A primitive cubic tuple with a nonprimitive derivative cross product

Take the homogeneous primitive binary tuple
\[
H=(\xi^3,\xi^2\eta,\eta^3)^t,\qquad
H_\xi\times H_\eta
 =3\xi\,(2\eta^3,-3\xi\eta^2,\xi^3)^t,
\qquad N_0=(2\eta^3,-3\xi\eta^2,\xi^3)^t.
\tag{1}
\]
The raw cross product has gcd xi up to a nonzero constant.
The entries of N_0 have gcd one and a common degree three.
Its first and last entries already show that it has no common
zero away from the origin. Direct calculation gives
N_0 dot H=N_0 dot H_xi=N_0 dot H_eta=0.

On the polynomial plane S=C[s,t] put
\[
p=s,\qquad r=st-1,\qquad tp-r=1,\qquad
b=H(p,r),\qquad N=N_0(p,r).
\tag{2}
\]
Thus (p,r) is a unit pair. It is also algebraically independent:
the Jacobian determinant of (p,r) in (s,t) is s, a nonzero
polynomial. The map is not asserted to be a plane automorphism;
its Jacobian drops rank on s=0.

## 2. Explicit unit rows and exact rank

The fifth power of the unit identity in (2) gives polynomial
coefficients
\[
U=t^5p^2-5t^4pr+10t^3r^2,\qquad
V=-10t^2p^2+5tpr-r^2,\qquad
Up^3+Vr^3=(tp-r)^5=1.
\tag{3}
\]
Consequently the row (U,0,V) has scalar product one with b,
and (V/2,0,U) has scalar product one with N. These are explicit
unit-ideal assertions, not just gcd computations.

The actual parameter derivatives in S satisfy
\[
b_s\times b_t=3s^2N,\qquad
\det[b,b_s,b_t]=0,\qquad
\det\begin{pmatrix}(b_1)_s&(b_1)_t\\
                         (b_2)_s&(b_2)_t\end{pmatrix}=3s^5\ne0.
\tag{4}
\]
Thus the speed map has generic rank two and satisfies the
conical determinant condition. The two factors of s in the raw
cross product have separate sources: the binary common factor xi
in (1) becomes s, and the Jacobian of the substitution contributes
another s. Its gcd in C[s,t] is s squared up to a nonzero constant,
so its entries do not generate the unit ideal. They all vanish on
s=0, whereas N specializes there to (-2,0,0), which is nonzero.
Dividing by the raw common factor therefore matters even though
the speed row itself is a unit row.

Equations (1)--(4) concern an explicitly given map of polynomial
parameter rings. They do not manufacture E, an original coordinate
frame, an intrinsic LND, or a cancellation example. They also do
not prove the arbitrary binary decomposition theorem. The general
normal argument in the linked proof still uses its stated source
and all its original-action hypotheses.

## 3. Exact control and review scope

The standalone
[one-method checker](binary_normal_unit_checks_pass89.py)
uses only unittest and SymPy. It verifies both cross products and
their gcd factors, the generic-rank minor, both explicit unit rows,
normal annihilation, and the specialization at s=0. These finite
identities support the illustrative control, not a universal
action or theorem certification.

Root proposed the cubic binary tuple and the substituted unit pair.
Jet independently derived the cross factors and Bezout rows.
Jet also fully read the linked eight-equation conical-normal proof
through EOF and reconstructed it cleanly. For its source gate,
the retained de Bondt Theorem 2.7 displayed statement and proof
were freshly read, including the used parts (i)--(v). This does
not claim a new audit of every preceding Luroth or homogeneous-gcd
dependency, nor a complete paper audit. No pass88 or older file
is changed. The author's actual one-method run passed in
0.147 seconds, exit zero, with full output in tool chunk dd1bae.
The entire saved proof and checker were then read through EOF,
with no correction. Final hashes are reported separately; this
control adds no runner or full regression.
