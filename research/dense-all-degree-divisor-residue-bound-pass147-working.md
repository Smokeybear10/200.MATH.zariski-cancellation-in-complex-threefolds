# A global divisor-residue bound for dense three-good frames

Every height-one fiber of the intrinsic quotient is an affine line
over a finite extension of its coefficient residue field. In the
actual dense three-good setting, that extension has degree at most
the minimum last-coordinate time degree plus one. More precisely,
its degree times the residual degree of any surviving projected good
coordinate is bounded by that coordinate's generic degree.

This extends the scope of the retained constant-acceleration bound91.
The curve-LND and valuation arguments are the same elementary
mechanisms; the additional ingredients are all-degree good-coordinate
noncollapse, a permissible good-coordinate selection at every divisor,
and the exact fixed-good degree formula145. No triviality of every
residue extension or cancellation conclusion is asserted.

## 1. Actual hypotheses and the base-ring dependency

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\\
H(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }
H\in\mathbb C[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
The four displayed generators are actual polynomial coordinates.
There is no bound on \(m=\deg_E W\).
The selected actual partial \(T=\partial_W\) holds all three goods
fixed. The retained cofactor and leading-LND results give
\[
\begin{gathered}
N=[u^2]T|_A\in\operatorname{LND}_{\mathbb C}(A)\setminus\{0\},
\qquad N(a_i)=0,\\
S=\ker_A N,\qquad L=\operatorname{Frac}S,\qquad
\operatorname{Frac}A=L(v),\qquad A_L=L[v],\\
\mu=\min_{P\in\mathbb C[x_1,x_2,x_3]}\deg_E(W+P).
\end{gathered}
\tag{2}
\]
Here \(A_L\) localizes by the nonzero elements of \(S\).[^1]

An additional inherited geometric theorem is used in this note:
\(S\simeq\mathbb C^{[2]}\). It applies to every nonzero intrinsic
LND on an affine domain with cylinder \(A[u]\simeq\mathbb C^{[4]}\),
without a time-degree assumption. The cylinder makes
\(\operatorname{Spec}A\) smooth and contractible, and its projection
from \(\mathbb A^4\) restricts to a dominant morphism from a suitable
linear \(\mathbb A^3\). Kaliman--Saveliev's quotient theorem then
gives the affine plane. The retained intrinsic-quotient proof and its
foundational audit spell out this application.[^2]

Thus \(S\) is a Noetherian UFD of dimension two. In particular,
for every irreducible \(p\in S\), the ring \(D=S_{(p)}\) is a
DVR and \(k=\operatorname{Frac}(S/(p))\) has transcendence degree
one over \(\mathbb C\). These facts are not inferred merely from
the field description in (2). The same inherited theorem gives
faithful flatness, but the fiber-dimension argument below does not
need that further conclusion.

## 2. Prime fibers and a nonzero residual LND

The ring \(A\) is an affine UFD with units \(\mathbb C^*\).
Indeed it is a quotient of its affine cylinder by \((u)\), and an
irreducible element of \(A\) stays irreducible in \(A[u]\) by
degree in \(u\). It is therefore prime in the polynomial UFD
\(A[u]\), and hence in \(A\).

Factorial closure of \(S=\ker N\) in \(A\) implies that an
irreducible \(p\in S\) remains irreducible, and thus prime, in
\(A\). Also \(pA\cap S=pS\): if \(f=pa\in S\), then
\(0=Nf=pNa\), so \(a\in S\). Consequently
\[
C_p=A_D/pA_D
\quad\text{is a nonzero finitely generated }k\text{-domain}.
\tag{3}
\]
Finite generation follows from any finite set of complex algebra
generators of \(A\); it also generates \(A\) over \(S\).

Choose such generators \(b_1,\ldots,b_r\), and let \(e\) be the
minimum of the finite \(p\)-adic orders of their nonzero values
\(N(b_i)\). Then
\[
N_p=p^{-e}N\in\operatorname{LND}(A),\qquad
N_p(p)=0,\qquad
\overline{N_p}\in\operatorname{LND}_k(C_p)\setminus\{0\}.
\tag{4}
\]
Divisibility of all generator values makes \(N_p\) preserve
\(A\); since \(Np=0\), its iterates satisfy
\(N^j=p^{ej}N_p^j\). This proves local nilpotence. A generator
with order exactly \(e\) has nonzero reduced derivative, which
remains nonzero after the coefficient localization. No global
primitivity assumption on the original \(N\) is needed.

Here is an elementary dimension check. If two elements of \(C_p\)
were algebraically independent over \(k\), lift them to \(A_D\).
Their lifts are dependent over \(L\), since \(\operatorname{Frac}A\)
has transcendence degree one over \(L\). Multiplying a nonzero
polynomial dependence by a power of the DVR uniformizer makes all
its coefficients belong to \(D\), with at least one a unit.
Reduction gives a nonzero polynomial dependence over \(k\), a
contradiction. Thus \(\operatorname{trdeg}_k C_p\le1\).
The nonzero derivation in (4) rules out degree zero in characteristic
zero, so the degree is exactly one.

The standard local-slice argument is especially strong for this
curve. The kernel of \(\overline{N_p}\) has transcendence degree
zero over \(k\); every nonzero element of that kernel is algebraic
over \(k\), and its inverse is a polynomial in itself. Hence the
kernel is a field \(\ell_p\). A nonzero local-slice derivative
is already a unit, so the local-slice expansion gives
\[
C_p=\ell_p[\xi],\qquad
\overline{N_p}(\xi)=1,\qquad [\ell_p:k]<\infty.
\tag{5}
\]
The extension is finite because evaluation at \(\xi=0\) realizes
\(\ell_p\) as a finitely generated field algebra over \(k\).
It is the full algebraic-constant field of \(\operatorname{Frac}C_p\).
This does not assume geometric integrality.

## 3. A valid good-coordinate selection at every divisor

The actual slice makes \(E\) fixed-point-free. The dense divisor
exclusion134 therefore gives \(\gcd_B(a_1,a_2,a_3)=1\).[^3]
Since \(p\) is prime in \(B=A[u]\), some \(a_i\) is not
divisible by \(p\). Permute the good coordinates so that this
coordinate is called \(X\), and put
\(s=EX\notin(p)\), \(t=EY\), \(b=EZ\).

This permutation changes neither the actual partial \(T\), nor
\(N=[u^2]T|_A\), nor its kernel \(S\). It also leaves
\(\mathbb C[x_1,x_2,x_3]\) and the fixed-good minimum \(\mu\)
unchanged. The dense chart139 now supplies
\[
\begin{gathered}
B_D=A_D[X],\qquad
Y=y+\tau X,\quad Z=z+\rho X,\qquad
\tau=t/s,\ \rho=b/s\in D,\quad y,z\in A_D,\\
L[y,z]=L[v],\qquad
d:=\deg g=\max\{\deg_v y,\deg_v z\}=\mu+1 .
\end{gathered}
\tag{6}
\]
The generic parameter \(v\) can be renormalized for this selected
speed; its change is affine over \(L\), which preserves polynomial
degrees. The last equality is the exact degree consequence145 in
this permuted chart, with the same \(\mu\).[^4]

At least one of \(\bar y,\bar z\) is transcendental over \(k\).
Indeed, the divisor restriction134 says that
\((p)B\cap\mathbb C[X,Y,Z]=0\).[^3] The injection of the good
ring remains injective on localizing by \(S\setminus(p)\).
If both projected values were algebraic over \(k\), the images
of all three goods in \(C_p[X]\) would lie in
\(k(\bar y,\bar z)(X)\), whose transcendence degree over
\(\mathbb C\) is only two. That contradicts the injection of
the polynomial good ring of transcendence degree three.
This is the all-degree noncollapse argument; no assertion that the
good speeds are independent modulo \(p\) is made.

## 4. Restriction of the divisor valuation

Fix either \(U=y\) or \(U=z\) whose image \(\bar U\) is
transcendental over \(k\), and put \(n=\deg_v U\ge1\).
Then \([\operatorname{Frac}A:L(U)]=n\).
Let \(V_p=A_{pA}\) be the DVR at the prime divisor \(pA\),
with valuation \(\nu(p)=1\). Its residue field is
\(\operatorname{Frac}C_p\). Its restriction to \(L\) is the
ordinary valuation of \(D\), by \(p^jA\cap S=p^jS\).

For a nonzero polynomial \(Q(T)=\sum q_iT^i\in L[T]\), scale
its coefficients by a power of \(p\) until their smallest
valuation is zero. The reduced polynomial is nonzero over \(k\)
and cannot vanish at \(\bar U\). Thus
\[
\nu(Q(U))=\min_i\nu(q_i),\qquad
\kappa\bigl(V_p\cap L(U)\bigr)=k(\bar U).
\tag{7}
\]
The residue-field equality follows by applying the same calculation
to quotients of polynomials. In particular \(p\) is a uniformizer
for the restricted valuation as well.

Lift any finite set of elements of \(\operatorname{Frac}C_p\)
linearly independent over \(k(\bar U)\) to elements of \(V_p\)
with nonzero residues. These lifts are linearly independent over
\(L(U)\): scale any proposed dependence to make its coefficient
valuations nonnegative with one zero, and then reduce using (7).
The resulting residue dependence would be nontrivial. Since the
field extension over \(L(U)\) has degree \(n\), this proves
\[
\boxed{\quad
[\ell_p:k]\,\deg_\xi\bar U
=[\operatorname{Frac}C_p:k(\bar U)]
\le \deg_v U\le d=\mu+1 .
\quad}
\tag{8}
\]
For the equality, use the tower
\(k(\bar U)\subset\ell_p(\bar U)\subset\ell_p(\xi)\).
The first degree is \([\ell_p:k]\), because \(\bar U\) is
transcendental over \(\ell_p\); the second is the degree of the
nonconstant polynomial \(\bar U\in\ell_p[\xi]\).
This is the elementary residue-independence proof already used91.[^5]

The prime \(p\) was arbitrary. Thus \([\ell_p:k]\le\mu+1\)
holds at every height-one prime of \(S\), including divisors
removed by the initially chosen selected-speed localization.
The good-coordinate choice is allowed to depend on \(p\).
Since \(\ell_p/k\) is separable, extension to an algebraic closure
of \(k\) makes this full divisor fiber exactly \([\ell_p:k]\)
disjoint affine lines, and therefore at most \(\mu+1\) such lines.

## 5. A surviving generic linear coordinate gives local recognition

If one of the surviving projected goods satisfies \(\deg_v U=1\),
equation (8) implies
\[
\ell_p=k,\qquad C_p=k[\bar U],\qquad A_D=D[U].
\tag{9}
\]
For the final equality, \(A_L=L[U]\). Write any \(f\in A_D\)
as a polynomial in \(U\) with coefficients in \(L\). If a
coefficient had a pole at \(p\), multiplication by the smallest
positive power of \(p\) clearing those poles would give a
polynomial with primitive coefficients in \(D\), but with value
zero modulo \(pA_D\). Its nonzero reduction cannot vanish at
the transcendental \(\bar U\). All coefficients therefore lie
in \(D\), proving \(A_D=D[U]\).

This statement concerns a specified surviving coordinate, not a
claim that such a coordinate has generic degree one at every prime.
When \(\mu=0\), the existence from Section 3 and (6) do supply
one at each prime, so the local conclusion includes that boundary.
There is no exception requiring the original bad degree to be positive.

## 6. Scope of the generalization

The bound91 imposed constant acceleration, a low generic degree,
a primitive global field, and a separate low-degree noncollapse
theorem. Here the intrinsic field is the actual leading \(N\) of
an arbitrary-degree dense chart. Division by its local prime content
handles vanishing along a divisor;134 handles noncollapse and the
choice of a nonvanishing speed. The valuation estimate itself is not
a new theorem.

Already139 gives the upper bound by \(\deg g\), and139 together
with141 bounds it by \(\mu+1\);145 identifies these last two
quantities exactly. The affine-plane quotient theorem is an explicit
additional dependency in this divisor argument, although139 and145
did not need it for their generic-field proofs.

Nothing here proves \(\ell_p=k\) at all primes when \(\mu>0\),
identifies a projected-good subring with the full invariant overring,
or removes every coefficient denominator. The full fibers considered
are \(A_D/pA_D\), not the possibly split fibers of a smaller
plane presentation. Global polynomial descent, arbitrary coordinate
entry, and the unrestricted cancellation target remain outside the
conclusion.

## Sources

1. [Dense all-degree Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--2 and 7. The actual selected leading LND, invariant
   localization, and whole generic line; its sources132 and125
   supply the all-degree cofactor and leading-LND construction.
2. [Intrinsic additive quotients are affine planes](intrinsic-quotient-surface-pass.md),
   Sections 1--3, and [the foundational quotient audit51](intrinsic-quotient-foundation-audit-pass51.md),
   Sections 1--3. Their primary input is Shulim Kaliman and Nikolai
   Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
   Lemma 2.1 and Corollary 2.8(2). The statement applies to the
   unknown affine threefold through its polynomial cylinder, not
   through an assumed identification with \(\mathbb A^3\).
3. [Dense good speeds have no common invariant divisor134](dense-good-speed-divisor-exclusion-pass134.md),
   Sections 2--3. Both the gcd result and good-ring injection have
   no last-coordinate degree bound.
4. [The generic embedded-line degree139](dense-generic-embedded-line-pass139-working.md),
   Section 3; [fixed-good shear minimum141](dense-shear-minimal-tail-pass141-working.md),
   Sections 2--4; and [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Section 9. Their exact combination is used in (6).
5. [The relative degree bounds every generic divisor residue extension91](nonconical-residue-degree-bound-pass91.md),
   Sections 2--5. The curve-LND argument, elementary valuation
   inequality, and conditional local recognition are reproduced
   here in the broader actual setting.

No new external classification theorem, numerical verification,
historical novelty determination, or proof-assistant verification is
claimed. The indicated retained proofs remain explicit dependencies.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4.
[^5]: Source 5.
