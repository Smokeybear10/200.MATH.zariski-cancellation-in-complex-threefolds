# A primitive fixed point obstructs the larger triangular pencil

Allowing a constant-in-B term in the triangular candidate does not
produce a primitive fixed-point control with a simultaneous nice frame.
More precisely, for
\[
E=\partial_s,\qquad
T=\partial_A+s f(A)\partial_B+s\bigl(g(A)B+k(A)\bigr)\partial_C
\quad\text{on }R=\mathbb C[A,B,C,s],
\tag{1}
\]
suppose a polynomial coordinate frame makes T a coordinate partial
and E nice. If Q=[T,E] is nonzero, the primitive part of its restriction
to ker E is fixed-point-free.

This conclusion is only for (1). It does not prove freeness for every
nice sliced action with a good partial. Unlike the
[smaller pencil classification](triangular-nice-pencil-classification-pass76.md),
it does not assert an iff criterion for compatible frames or claim
that g must be a constant multiple of f when k is present. The old
origin two-jet test alone does not give that assertion.

## 1. Actual derivations, primitive division and zero cases

Both E and T are actual triangular LNDs with respective slices s
and A. Their derived field is
\[
Q=[T,E]=-d,\qquad
d=f(A)\partial_B+\bigl(g(A)B+k(A)\bigr)\partial_C,
\qquad [E,Q]=0.
\tag{2}
\]
Thus the double-adjoint bound always holds. The intrinsic ring is
the actual polynomial ring ker E=C[A,B,C], and Qs=0. Dividing d
instead of -d changes the primitive field only by a constant.

If f=0 and d is nonzero, it has just one nonzero coordinate
coefficient, g(A)B+k(A). Its primitive part is partial_C and has
slice C. If f=g=k=0, Q is zero and there is no nonzero primitive
direction to consider. We may therefore assume f is nonzero.

In this case the gcd of the nonzero coordinate coefficients of d
is, up to a complex unit,
\[
h=\gcd(f,g,k)\in\mathbb C[A],\qquad
D=(f/h)\partial_B+\bigl((g/h)B+k/h\bigr)\partial_C.
\tag{3}
\]
Indeed every divisor common to f(A) and g(A)B+k(A) factors in
C[A], and its multiplicity in the second polynomial is the minimum
of its multiplicities in g and k. This proves (3) with all repeated
factors retained. D is a triangular LND, and h is invariant under d.

If g=0, the two coefficients f/h and k/h are coprime univariate
polynomials. A polynomial Bezout combination of B and C is then
a D-slice, so there is no fixed point. The argument below handles
every remaining putative fixed point, without assuming h is a unit.

## 2. The forced orders at a primitive fixed point

Assume for contradiction that D has a fixed point (A0,B0,C0).
At A0 we have (f/h)(A0)=0 and
\((g/h)(A0)B0+(k/h)(A0)=0\).
It is essential that (g/h)(A0) is nonzero. Otherwise all three
polynomials f/h, g/h and k/h would vanish at A0, contrary to their
gcd being one.

Translate A0 and B0 to zero by an actual constant coordinate
change. This replaces k by k+B0 g and preserves its gcd with f,g.
Writing r=ord_0 h, there is an integer m>=1 such that
\[
\operatorname{ord}_0 f=r+m,\qquad
\operatorname{ord}_0 g=r,\qquad
\operatorname{ord}_0 k\ge r+1.
\tag{4}
\]
The order of a zero polynomial is understood as infinity.
The third inequality follows after the B-translation, because the
new k/h vanishes at zero. No division by g in the actual ring is
used. C0 plays no role because the coefficients do not depend on C.

Choose polynomial antiderivatives, all with zero value at zero,
\(F'=f\), \(G'=g\), \(K'=k\), and \(H'=Gf\). Define
\[
a=A,\qquad b=B-sF(A),\qquad
c=C-sG(A)B-sK(A)+s^2H(A),
\tag{5}
\]
retaining s. Their actual polynomial inverse is
\[
A=a,\qquad B=b+sF(a),\qquad
C=c+sG(a)b+sK(a)+s^2\bigl(G(a)F(a)-H(a)\bigr).
\tag{6}
\]
In either substitution order the C-correction cancels as
-sGB-sK+s^2H+sG(B-sF)+sK+s^2(GF-H)=0,
or as its reverse-order counterpart. A and B cancel directly.
Thus these are two-sided polynomial inverses. Direct application
of T gives Ta=1 and Ts=Tb=Tc=0, so
ker T=C[s,b,c] in this actual frame.

Put M=2H-GF and L=-Gb-K+sM. The exact transported field is
\[
E=\partial_s-F(a)\partial_b+L(a,s,b)\partial_c,
\qquad E^2c=2H(a),\qquad Ea=0.
\tag{7}
\]
In particular K changes the first derivative of c, not this second
derivative. Its contribution to a general E^2R cannot be omitted.

Set ell=r+1 and n=ell+m, so n>ell>=1. Equation (4) implies that
there are nonzero complex constants alpha,beta with
\[
\begin{aligned}
F&=\alpha a^n+O(a^{n+1}),&
G&=\beta a^\ell+O(a^{\ell+1}),&
K&=O(a^{\ell+1}),\\
H&=\frac{n}{n+\ell}\alpha\beta a^{n+\ell}
     +O(a^{n+\ell+1}),&
M&=\frac{n-\ell}{n+\ell}\alpha\beta a^{n+\ell}
     +O(a^{n+\ell+1}).
\end{aligned}
\tag{8}
\]
These are ordinary polynomial vanishing-order statements at a=0.
In particular F,H,M are all nonzero; both displayed leading
coefficients for H and M are retained. The factor n-ell in M
is positive and cannot be discarded.

## 3. All T-invariant nice polynomials, without a degree bound

Let R0(s,b,c) be any polynomial in ker T and assume E^2R0=0.
Use subscripts for its partial derivatives. The complete product
and chain rule calculation from (7) is
\[
E^2R_0=R_{0,ss}-2F R_{0,sb}+2L R_{0,sc}
 +F^2R_{0,bb}-2FL R_{0,bc}+L^2R_{0,cc}+2H R_{0,c}.
\tag{9}
\]
This is a polynomial identity in the independent variable a over
C[s,b,c]. At order zero it gives R0,ss=0. At order ell, the only
remaining contribution is -2 beta b R0,sc, so R0,sc=0 as well.
Consequently R0=s v(b)+W(b,c) for polynomials v,W.

First suppose n is not 2ell. If n<2ell, the coefficient of a^n
now forces R0,sb=0, and the coefficient of a^(2ell) then forces
R0,cc=0. If n>2ell, the same two conclusions follow in the opposite
order. The decisive coefficients are respectively
-2 alpha R0,sb and beta^2 b^2 R0,cc. Other terms cannot enter
either comparison: the F L and H terms begin at n+ell, and F^2
begins at 2n, both strictly above max(n,2ell). Previously killed
derivatives also remove their higher-order contributions.

In the resonant case n=2ell, the coefficient of a^(2ell) instead
gives
\[
-2\alpha v'(b)+\beta^2b^2 W_{cc}(b,c)=0.
\tag{10}
\]
Since the first term is independent of c, polynomiality forces
Wcc to be a polynomial of b alone. Therefore
\[
R_0=s v(b)+\frac12p(b)c^2+q(b)c+u(b),
\qquad 2\alpha v'(b)=\beta^2b^2p(b).
\tag{11}
\]
Take the coefficient of c in the a^(3ell) coefficient of (9).
The F^2 term starts only at 4ell. The K contribution in F L
starts above 3ell because ord K>=ell+1. The L^2 term acts on
Wcc=p(b), hence contributes no c. The only surviving terms with
c are the leading F G and H terms. Using (8), their sum is
\[
2\alpha\beta\left(b p'(b)+\frac23p(b)\right)=0.
\tag{12}
\]
For a polynomial p, every b^j coefficient here is multiplied by
j+2/3, which is nonzero in characteristic zero. Thus p=0 and,
by (11), v'=0. This proves R0,cc=R0,sb=0 also in the resonant
case. No coefficient of K has been silently set to zero.

In every case R0 now has the form R0=lambda s+q(b)c+u(b), with
lambda complex. Substitute this into the full identity (9):
\[
0=F^2\bigl(q''(b)c+u''(b)\bigr)
 +2F\bigl(Gb+K-sM\bigr)q'(b)+2Hq(b).
\tag{13}
\]
Its coefficient of s is -2FM q'. Since F and M are nonzero,
q'=0. Hence q is constant, and (13) reduces to
F^2u''+2Hq=0. The leading order of H is n+ell, strictly below
2n, the order of F^2. Therefore q=0. Now u''=0. Conversely s
and b have zero second E-derivative. We have obtained the exact
all-polynomial identity
\[
\ker T\cap\ker E^2
=\mathbb C\oplus\mathbb Cs\oplus\mathbb Cb
\quad\text{under the putative primitive-fixed-point hypothesis}.
\tag{14}
\]

## 4. Contradiction with every compatible coordinate frame

In any coordinate frame making T a coordinate partial, the other
three coordinates generate ker T=C[s,b,c]. If E is nice in that
same frame, all three belong to (14), and therefore generate an
algebra contained in C[s,b]. This has transcendence degree at most
two, not three. The contradiction does not depend on choosing a
as the T-slice: every other T-slice is a plus an element of ker T,
and the same three invariant generators would still be required.

Thus a primitive fixed point as in Section 2 cannot exist under
the simultaneous-frame premise. Over C, the Nullstellensatz gives
the precise ideal conclusion
\[
\bigl(D(\mathbb C[A,B,C])\bigr)=\mathbb C[A,B,C].
\tag{15}
\]
Equivalently, the wedge ideal of E and Q becomes the unit ideal
after dividing by its exact gcd as in
[the primitive quotient criterion](primitive-good-quotient-scope-pass75.md).
No unsupported inference from primitivity alone is used.

## 5. Boundary and verification record

The added k term weakens the old single-point two-jet test: at
s=b=c=0 the first velocity is (1,-F,-K), so its Hessian terms
include K, FK and K^2. This proof instead uses a hypothetical
primitive fixed point to normalize the orders (4), and compares
the full coefficient identity (9), including its resonant case.
It does not reassert constant proportionality of f and g or a
classification of all compatible frames in the larger family.

The zero cases in Section 1 have explicit primitive slices. In
the general case the conclusion proved here is fixed-point-freeness
and (15); no separate global coordinate-slice classification is
asserted. The whole construction still begins with the already
recognized E=partial_s. It does not provide a new cancellation
case or settle the arbitrary nice/good-partial target.

Inline exact SymPy controls checked the full identity (9) and its
first two decisive coefficients for (ell,n)=(1,2),(1,3),(3,4),
representing resonance and both nonresonant orderings. The resonant
c coefficient was additionally checked in the (1,2) case.
These finite calculations are not a proof
of the all-order argument or a full-frame counterexample. No new
standalone checker, numerical method or full regression was added.
The complete saved proof was author-read through EOF. Frozen
passes through75 and shared metadata remain unchanged.
