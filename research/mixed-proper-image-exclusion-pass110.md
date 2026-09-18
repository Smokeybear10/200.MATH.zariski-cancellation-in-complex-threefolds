# Exclusion of the proper second-image mixed sector

The remaining proper second-image ideal cannot occur in the supplied
collapsed mixed quadratic sector with nonzero speed normal. A divided
quartic produces a finite submodule of index ideal (b), rather than a
basis. Its derivatives lie in a small base ideal. Adjugate multiplication
and flat contraction then force an impossible divisibility relation.

This argument allows singular and nonreduced conic-constant divisors.
It does not use a smooth parameter, normalization of that divisor, or
an iteration of maximal-ideal orders. Combined with the full-image107
and unit-ideal108 exclusions, it excludes this whole mixed sector.
It is not a proof of arbitrary complex-threefold cancellation.

## 1. The precise actual inputs

Let (R,m) be the regular local invariant surface in the supplied
collapsed mixed multiplicity-(2,1) quadratic frame with L(m) nonzero.
It is a local UFD containing C. Let A_R be its faithfully flat domain,
N its R-linear locally nilpotent derivation with full kernel R, and
F_j=ker N^(j+1). Retain the actual generic polynomial line and finite
freeness of F_j of rank j+1. The proper case has the following data:
\[
\begin{gathered}
F_1=R\{1,r\},\quad F_2=R\{1,G,H\},\quad F_4\simeq R^5,\\
r=aG+bH,\quad Nr=P\ne0,\quad
NG=\epsilon br+h,\quad NH=-\epsilon ar+B_2,\\
P=ah+bB_2,\quad Q=\epsilon r^2-2B_2G+2hH\in R,
\quad\epsilon\in R^*,\\
a,b,h\in\mathfrak m\setminus\{0\},\quad
\gcd(a,b)=\gcd(h,b)=1,\quad H\in\mathfrak mA_R,\\
a^2,B_2,Q\in\mathfrak m(h)+\mathfrak m(ab)+\mathfrak m^2(b^2).
\end{gathered}
\tag{1}
\]
Here h is B1 in the preceding notes. These are the sharp proper-case
inputs108, not assumptions made about an arbitrary polynomial cylinder.[^sharp]
The whole fiber and its actual action provide an element c in F4 with
\[
\begin{gathered}
A_R/\mathfrak mA_R=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\\
\overline{Nc}=\lambda(G-G^2)+\rho G^2\ne0,
\qquad\lambda,\rho\in\mathbb C^*.
\end{gathered}
\tag{2}
\]
Only the nonzero whole residue of Nc is needed in the main contraction.
There is no assumption that it is a unit on the entire mixed fiber.

One more substantive input is the exact actual divisor filtration107.
At each height-one prime, the degree-one constant case has a slice;
the degree-two constant case has the alternating DVR basis. Thus the
generic coefficient determinant of any R-basis of F4 in the powers of
r has valuation -4 ord(P) at every height-one prime.[^divisor]
Section 3 explains the particular determinant consequence used here.

## 2. A divided quartic without a shear

Choose representations supplied by (1):
\[
\begin{gathered}
a^2=hu_0+abv_0+b^2w_0,\quad
B_2=h\beta+ab\tau+b^2\delta,\quad
Q=h\zeta+ab\xi+b^2q,\\
u_0,v_0,\beta,\tau,\zeta,\xi\in\mathfrak m,
\qquad w_0,\delta,q\in\mathfrak m^2,\\
A_0=\epsilon u_0G^2-2\beta G+2H-\zeta,\\
A_1=a(\epsilon v_0G^2+2\epsilon GH-2\tau G-\xi)
 +b(\epsilon w_0G^2+\epsilon H^2-2\delta G-q),\\
hA_0+bA_1=0.
\end{gathered}
\tag{3}
\]
The last equality is the expanded original conic. Since h and b are
coprime in a UFD, b is a nonzerodivisor modulo h. Flatness preserves
this injection in A_R/hA_R. Reduction of (3) therefore puts A1 in
hA_R. There is an actual element
\[
\boxed{\quad W=A_1/h=-A_0/b\in F_4.\quad}
\tag{4}
\]
The first division is justified before using the second expression:
write A1=hW and cancel nonzero h in (3). The element belongs to F4
because N^5(A1)=0 and h is a nonzero invariant in the domain A_R.
No inverse of a polynomial in G or H is used.

Differentiate bW=-A0 and substitute the first two representations
in (3). The exact result is
\[
\boxed{\quad
NW=-2\epsilon^2u_0Gr+2\epsilon\beta r
 +2\epsilon\bigl((av_0+bw_0)G+aH\bigr)
 -2a\tau-2b\delta.
\quad}
\tag{5}
\]
Indeed, the initially divided expression contains
2epsilon(a r-hu0G)/b. Using r=aG+bH and
a squared-hu0=abv0+b squared w0 gives the middle term in (5).
This identity needs no membership of a/b in R/(h).

## 3. An index-b submodule, not a putative basis

In the generic line K[r], N=P partial_r. Integration gives
G=g2 r squared+g1 r+g0, where g2=epsilon b/(2P), g1=h/P,
and the integration constant g0 is arbitrary.
For five polynomials let Delta be their coefficient
determinant in 1,r,r squared,r cubed,r to the fourth. Then
\[
\begin{aligned}
\Delta(1,G,G^2,GH,W)
 &=-\frac{2}{b^3}\Delta(1,G,G^2,rG,r)\\
 &=-\frac{2}{b^3}\left(\frac{\epsilon b}{2P}\right)^4
 =-\frac{\epsilon^4b}{8P^4}.
\end{aligned}
\tag{6}
\]
For the first equality, W is -2H/b modulo 1,G,G squared,
GH is rG/b modulo G squared, and H is r/b modulo G. For the
second equality reorder the last determinant to
(1,r,G,rG,G squared). That permutation has even sign, and the
consecutive leading coefficients are 1,1,g2,g2,g2 squared.
All integration constants remain arbitrary.

Fix an actual R-basis E of F4. At a degree-one constant divisor,
P is a unit and the powers of r form a basis, so Delta(E) has
valuation zero. At a quadratic constant divisor, put e=ord(P).
The actual basis is 1,r0,t,r0t,t squared, with a monic relation
p^e t=r0 squared+alpha r0+eta. The global r and local r0 differ
by a unit-affine change because their derivatives both generate
the first-image ideal. Their degree-four determinants therefore
have the same valuation, namely -4e. These are all the actual
divisor types in the supplied quadratic frame.

Let C be the coefficient matrix of the five actual elements in
(6) relative to E. Its entries belong to R and its determinant has
exactly the valuations of b at every height-one prime. Since R is
a UFD, det(C)=v b for a unit v in R. The adjugate identity now gives
\[
M=R\{1,G,G^2,GH,W\}\subseteq F_4,
\qquad \boxed{\quad bF_4\subseteq M.\quad}
\tag{7}
\]
This is not a claim that M=F4 or that F4/M is isomorphic to R/(b).
Only annihilation by b is used. Divisorwise comparison is applied
to a scalar determinant of a finite matrix of actual elements.

## 4. Derivatives contract to an impossible base ideal

Define the base ideal J=(h)+m(a)+m squared(b). We claim
N(M) is contained in J A_R. The relevant identities are
\[
\begin{gathered}
NG=h+\epsilon abG+\epsilon b^2H,\\
N(G^2)=2hG+2\epsilon abG^2+2\epsilon b^2GH,\\
N(GH)=-\epsilon a^2G^2+\epsilon b^2H^2+hH+B_2G,\\
\boxed{\quad N(M)\subseteq JA_R,\qquad bNc\in JA_R.\quad}
\end{gathered}
\tag{8}
\]
For the first two identities use ab in m(a), H in mA_R,
and b squared H in m squared(b)A_R. In the third, a squared
is in m(a), b squared H squared is in m squared(b)A_R,
hH is in (h)A_R, and the sharp representation puts B2 in J.
For (5), expand r=aG+bH. Terms containing u0 a, beta a,
a v0, aH and a tau belong to m(a)A_R; terms containing
u0 bH, beta bH, b w0 and b delta belong to m squared(b)A_R.
Thus NW also belongs to J A_R. Since N kills R, these checks
on the five generators prove the containment for all M. The
last assertion of (8) uses bc in M from (7), not c in M.

By (2), the single element Nc has nonzero residue in the flat
module A_R/mA_R. The residue-basis purity lemma therefore gives
R Nc intersect J A_R = J Nc. Since A_R is a domain and Nc is
nonzero, (8) implies b in J.[^purity] Equivalently, for some
d in R, v in m and w in m squared, b=hd+va+wb. Absorbing
the unit 1-w proves
\[
\boxed{\quad b\in(h)+\mathfrak m(a).\quad}
\tag{9}
\]
There is also a geometric check of this contraction which avoids
purity of a finite piece. At a closed point of the simple component
of the fiber, Nc has nonzero value rho. It is a unit in the
corresponding localization of A_R. That localization is flat and
local over R, hence faithfully flat. Dividing bNc in JA_R there
and contracting J again gives b in J. This alternative uses the
simple-component unit in (2), not a unit on the whole fiber.

Work now in the local quotient C=R/(h), with maximal ideal n.
It need not be reduced or normal. Equation (9) gives b=a v in C
for some v in n. The sharp first membership in (1) consequently
implies a squared in n squared(a squared). By Nakayama applied
to the cyclic ideal (a squared) of C, this ideal is zero. Thus
h divides a squared in R.

Equivalently, write b=hd+av in R with v in m, substitute in the
first representation in (3), and reduce modulo h. The resulting
identity is (1-vv0-v squared w0)a squared=0 modulo h. Its
parenthesis is a unit, proving the same divisibility directly.

On the other hand, any common prime factor of a and h would
divide b by (9), contrary to gcd(a,b)=1. Therefore a and h are
coprime. A nonzero nonunit h in a UFD cannot divide a squared
while being coprime to a. This contradiction proves the exclusion.

## 5. Scope, checks and remaining obligations

The contradiction needs no smoothness of a, b or h, no reducedness
of R/(h), no equality of component speeds, no fourth-image
nonprincipality, and no statement that F4 generates A_R as an
algebra. The maximal-ideal order bounds109 are not inputs.
The determinant index, rather than an unjustified basis assertion,
is the important difference from the smooth proof.

The [finite controls110](mixed_singular_coefficient_checks_pass110.py)
check polynomial identities and generic determinants. Their
[coefficient-only singular example](mixed-singular-coefficient-controls-pass110.md)
satisfies the sharp coefficient constraints but fails the new
necessary ideal contraction. It is not an actual mixed frame and
does not contradict this theorem. Finite computation does not
prove flatness, actual division, all-divisor classification, or
the existence of the stated original frame.

Together with [full-Artin exclusion107](mixed-full-artin-quartic-exclusion-pass107.md)
and [unit-ideal exclusion108](mixed-unit-second-image-exclusion-pass108.md),
this excludes the collapsed mixed quadratic fiber with L(m) nonzero
under the retained actual-frame hypotheses. Whole-double fibers,
zero speed normal, the relative cubic branch, global recognition,
and entry from an arbitrary sliced action remain unproved.
Separate AI reconstructions are not human expert review, formal
verification, or evidence of novelty. No public claim is made.

[^sharp]: [Sharp proper second-image restrictions108](mixed-proper-second-image-jets-pass108.md), Sections 1–3. The whole-fiber action is recorded in [actions100](quadratic-whole-fiber-actions-pass100.md) and the [pure quartic row108](mixed-pure-quartic-row-pass108.md). These are conditional actual-frame deductions, not consequences asserted for arbitrary cancellation input.

[^divisor]: [Exact quadratic divisor filtration107](quadratic-constant-divisor-filtration-pass107.md), Sections 2–5; [degree-one divisor slice105](mixed-cubic-rank-defect-pass105.md), Section 2; and [divisor91](nonconical-residue-degree-bound-pass91.md), including the supplied noncollapse hypotheses. The particular scalar determinant comparison is also written in [smooth-B1 exclusion109](mixed-smooth-B1-exclusion-pass109.md), Section 4.

[^purity]: [Residue-basis purity107](residue-basis-purity-pass107.md), with its complete finite-free colimit proof, based on the Stacks Project's [Lazard theorem, 058G](https://stacks.math.columbia.edu/tag/058G) and [finite factorization construction, 058C](https://stacks.math.columbia.edu/tag/058C). The contraction here uses only the one-element instance, not purity of F2, F3 or F4.
