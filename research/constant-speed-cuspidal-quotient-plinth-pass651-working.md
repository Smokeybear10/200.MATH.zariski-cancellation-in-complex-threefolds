# A constant-speed quotient and its full plinth

This note computes the entire invariant ring and plinth of one changed
action on the known second-kind Koras--Russell control625. It then
restricts auxiliary actions by published surface and plane-curve
theorems. The control has no established polynomial cylinder here.
These calculations do not solve cancellation. Novelty is UNKNOWN.
The subsequent [full classification652](cuspidal-quotient-full-lnd-classification-pass652-working.md)
closes the auxiliary-action branch left open by Section5 below.

## 1. Algebra, action, and statements

Work over the complex numbers. Put
\[
C=\mathbb C[a,b],\quad p=b^2-a^3,\quad c=p^2,
\quad R=C[s,t]/(ct-s^5+b),\quad B=R[u].
\]
Control625 establishes the properties of this known nonpolynomial
threefold. We only need the displayed presentation for the calculations
below. Define the locally nilpotent derivation
\[
La=Lb=0,\qquad Ls=c,\quad Lt=5s^4,\quad Lu=b.
\tag{1}
\]
It is the sum of the commuting LNDs D and b*partial_u. In particular
its exponential fixes a,b, sends u to u+bT and s to s+cT, and sends
\[
t\longmapsto t+\sum_{j=1}^5\binom5j s^{5-j}c^{j-1}T^j.
\]
The full result is
\[
K:=\ker_B L=\mathbb C[a,b,v,w]/(cw-v^5+b^6),
\qquad \operatorname{pl}(L):=L(B)\cap K=(b,c,v^4)K,
\tag{2}
\]
where the actual elements of B are
\[
\begin{split}
v={}&bs-cu,\\
w={}&b^5t-5b^4s^4u+10b^3s^3cu^2-10b^2s^2c^2u^3
       +5bsc^3u^4-c^4u^5.
\end{split}
\tag{3}
\]
For every LND epsilon of K, there is also the implication
\[
\varepsilon(h)=0\text{ for some }h\in C\setminus\mathbb C
\quad\Longrightarrow\quad\varepsilon(a)=\varepsilon(b)=0.
\tag{4}
\]
This does not assume that epsilon preserves C as a subring. It does
not handle actions with ker(epsilon) intersect C equal to the constants.

## 2. Entire kernel, including the exceptional divisor

Both B and the candidate algebra
S=C[v,w]/(cw-v^5+b^6) are domains: their defining equations are
primitive linear polynomials in t and w, respectively, over UFDs,
and are irreducible over the corresponding fraction fields.
The monic s^5 and v^5 expressions give the respective free C-bases
\[
\{s^it^ju^k:0\le i<5,\ j,k\ge0\},
\qquad \{v^iw^j:0\le i<5,\ j\ge0\}.
\tag{5}
\]
Expansion in B gives cw=v^5-b^6 and Lv=Lw=0. After inverting b,
the slice u/b and the change exp(-uD/b) give
\[
s\longmapsto v/b,\quad t\longmapsto w/b^5,
\qquad B_b=S_b[u],\quad L=b\partial_u.
\]
Thus the map S to B is injective after inverting b and hence injective,
and S_b=K_b. This is an equality of localized algebras, not just fields.

Modulo b the map is
\[
S/bS=\mathbb C[a,v,w]/(a^6w-v^5)
\longrightarrow B/bB=\mathbb C[a,s,t,u]/(a^6t-s^5),
\]
with v=-a^6u and w=-a^{24}u^5. The subring C[a,u] embeds in B/bB,
by the monic equation in s. The basis v^i w^j for 0<=i<5 maps to
nonzero powers of a times distinct powers u^{i+5j}. Its images are
linearly independent over C[a], proving residue injectivity.
Consequently S intersect bB=bS. If an element of K is represented
as q/b^N with q in S and N minimal, N>0 would imply q in bS,
a contradiction. Therefore S=K, proving the first assertion of (2).

## 3. Entire plinth, not only exhibited generators

We use two elementary localization facts. First,
\[
B_b\cap B_c=B\quad\text{inside }\operatorname{Frac}(B).
\tag{6}
\]
Indeed B is free over C by (5), and the relatively prime elements
b,c in the UFD C have C_b intersect C_c=C. Compare each coefficient
in (5). The union of the two localization charts need not be all
of Spec B; (6) proves the needed extension across its complement.

Second, for every q in K,
\[
\frac{q}{bc}\in K_b+K_c\quad\Longleftrightarrow\quad q\in(b,c)K.
\tag{7}
\]
For the forward implication write q/(bc)=alpha/b^N+beta/c^M,
with alpha,beta in K and N,M>=1. Clearing denominators gives
\[
q b^{N-1}c^{M-1}=\alpha c^M+\beta b^N.
\]
The free C-basis (5) and gcd(b,c)=1 show that multiplication by b
is injective modulo c^M. Cancelling b^{N-1} modulo c^M gives
q c^{M-1}-beta b in c^M K. Write this difference as gamma c^M.
Modulo b, cancel c^{M-1}, which is a nonzerodivisor, to obtain
q-gamma c in bK. The converse follows immediately by separating
q=b alpha+c beta. This proof uses no normality assumption on K.

For h in K, local primitives on the two charts are hu/b and hs/c.
Their difference is -hv/(bc). All other primitives differ from
these by elements of K_b and K_c. By (6), compatible local primitives
are exactly whole elements of B. It follows that
\[
h\in\operatorname{pl}(L)
\iff hv/(bc)\in K_b+K_c
\iff hv\in(b,c)K.
\tag{8}
\]
Finally
\[
K/(b,c)K=\mathbb C[a,v,w]/(a^6,v^5).
\]
In its free basis 1,v,...,v^4 over C[a,w]/(a^6), the annihilator
of v is exactly (v^4). Thus (b,c)K:v=(b,c,v^4)K, proving the
second assertion of (2), including necessity for every primitive.

An explicit whole primitive for the extra generator is
\[
r=b^4t-4b^3s^4u+6b^2cs^3u^2-4bc^2s^2u^3+c^3su^4.
\]
Direct calculation gives
\[
Lr=v^4,\qquad r=(v^4u+w)/b=(v^4s-b^5)/c.
\tag{9}
\]
Together with Lu=b and Ls=c this verifies the sufficiency generators
independently of the gluing argument.

## 4. Quotient geometry and a necessary action constraint

For F=p^2w-v^5+b^6, its four partial derivatives are
\[
F_a=-6a^2pw,\quad F_b=4bpw+6b^5,
\quad F_v=-5v^4,\quad F_w=p^2.
\]
Their common zero set on the hypersurface is exactly the line
Lambda={a=b=v=0}, with coordinate w. Hence K is normal: it is
a hypersurface domain, therefore Cohen--Macaulay, and its singular
locus has codimension two, giving the conditions S2 and R1.

The quotient map Spec B to Spec K is NOT surjective on complex
points. A point over a=b=0 has s^5=0 and thus s=0. Equations (3)
then give v=w=0. In particular Lambda minus its origin is missed.
No quotient-surjectivity or smooth-quotient argument may be used.

Every additive action on Spec K fixes Lambda pointwise. The line
is intrinsically the singular locus. The hypersurface multiplicity
at its origin is five; at each w=w0!=0 it is four, since the lowest
term is w0*b^4. Thus its origin is the unique point on that line
of multiplicity five and is fixed by every automorphism. The
restriction of an additive action to this affine line has a fixed
point and must be trivial. This constraint is not a computation
of the full Makar-Limanov invariant.

## 5. Auxiliary actions fixing a base function

First suppose epsilon fixes a plane coordinate h, so C=C[h,x].
The cusp polynomial p is irreducible and is not a plane coordinate,
because its zero curve is singular. If p were in C[h], its
irreducibility over C would force p=lambda(h-mu), a contradiction.
Thus p has positive x-degree. Localizing at C[h] minus zero gives
\[
K\otimes_{\mathbb C[h]}\mathbb C(h)
=\mathbb C(h)[x,v,w]/(p(h,x)^2w-v^5+b(h,x)^6).
\]
Rescale w by the square of the leading x-coefficient of p to make
p^2 monic. Its x-degree is at least two; the right-hand polynomial
is monic of v-degree five. Saha's Theorem3.5 applies over the field
C(h): every nonzero localized LND fixes x.[^saha]
A nonzero derivation cannot become zero on this localization of a
domain. Therefore epsilon fixes h,x, and hence fixes a,b.

Now let any nonconstant h in C be epsilon-invariant and suppose
that epsilon moves a or b. There are only finitely many critical
values of h:A2 to A1. To see this, its critical locus has finitely
many irreducible components; on each positive-dimensional component
the restricted differential dh is zero, so h is constant in
characteristic zero. Zero-dimensional components contribute only
finitely many further values.

Choose a complex closed point of Spec K where a moving derivative
is nonzero and h avoids these critical values. Such a point exists:
the product of that nonzero derivative with the finitely many
nonzero factors h-lambda is nonzero in the finite-type domain K.
The polynomial additive orbit projects nonconstantly to the plane
and lies in a smooth irreducible component Gamma of the fiber of h.

A nonconstant map A1 to a smooth affine curve Gamma forces Gamma
to be A1. Indeed it extends to a nonconstant, hence surjective, map
P1 to the smooth projective completion of Gamma. The completion
has genus zero. Every omitted point has a nonempty preimage contained
in the single source point at infinity. There is at most one omitted
point and, because Gamma is affine and positive-dimensional, at
least one. This proves the assertion over C.

Abhyankar--Moh--Suzuki now makes an irreducible equation g of Gamma
a plane coordinate.[^ams] Since g divides h-h(Gamma), factorial
closure of the LND kernel in the domain K gives epsilon(g)=0.
The coordinate case just proved forces epsilon(a)=epsilon(b)=0,
contradicting the chosen derivative. This proves (4). It does not
require a connected generic fiber, a field-form argument, or that
epsilon maps C into C.

## 6. Scope and verification

The extra plinth generator v^4 is a genuine additional candidate
for a plinth-compatible auxiliary lift. Formula (4) closes routes
fixing a nonconstant base polynomial, not routes fixing v alone or
an arbitrary mixed element of (b,c,v^4)K. The complete auxiliary
action classification was a separate obligation at this stage.
It is now supplied by652, which shows every auxiliary LND fixes
the base. This does not produce a polynomial cylinder for R or
prove the main cancellation assertion.

Root's fresh unsaved check d9ba5b verified all of (3) and (9), the
whole flow relation, preservation of v,w, the primitive flow identity,
the residue relation, and the exact Jacobian. General's separate
4ffcf0 and Jet's corrected3f94d4 support the same identities.
Jet's earlier6a0ea2 stopped at a structural-expression comparison
and is not recorded as a pass. The uniform full-kernel and full-plinth
proofs are the basis and denominator arguments, not finite tests.

General and Jet independently reconstructed (2) and (4); Geometry
independently checked all hypotheses of the surface theorem for
every plane coordinate. Those message reviews precede saved-source
review. Subsequently General and Jet read all247 saved lines at
SHA256 ae27fa20d6b415ded76b2b37b788dfd099a576c08c52ecd5d46e40882b376de0
and reported CLEAN (complete EOF4d6c15 and2067a7). Jet's separate
freshc2bc3c checked the printed whole identities. Geometry additionally
read the complete source inda3b56 and confirmed the dependency for652.
Root's full saved-source read was7129f2. Only this provenance and the
link to the subsequent stronger classification changed after review.
Status: internally checked within the stated scope.
No saved checker was executed, imported, compiled, or edited.
AI reviews are not human expert review or formal certification.

[^saha]: Debojyoti Saha, [On Generalised Danielewski Surfaces over fields of arbitrary characteristic, Theorem3.5 and Corollary3.6](https://arxiv.org/html/2506.01457v1#S3). The actual field, monicity, and degree hypotheses and complete Section3 proof were directly read. This is an application of an existing theorem, not a new surface classification.

[^ams]: Karol Palka, [A new proof of the theorems of Lin--Zaidenberg and Abhyankar--Moh--Suzuki, Theorem B](https://arxiv.org/html/1405.5391v2). The exact complex-plane embedding statement was directly read. This classical theorem is imported, not reproved by the present note.
