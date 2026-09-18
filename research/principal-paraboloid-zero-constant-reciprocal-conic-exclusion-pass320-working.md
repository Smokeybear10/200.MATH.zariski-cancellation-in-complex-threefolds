# The zero-constant reciprocal conic is excluded by an actual primitive derivation

Working theorem: the actual reciprocal conic sector of316 and318
cannot have
\[
m=\frac{c}{t-\tau},\qquad c\in\mathbb C^*,\quad\tau\in\mathbb C .
\tag{1}
\]
Thus the remaining conic coupling \(m=d+c/(t-\tau)\) must have
\(d\ne0\), under those full actual hypotheses.

The argument takes the content of an auxiliary derivation in the
original polynomial ring before localizing. This order is essential:
an arbitrary normalization over \(\mathbb C(X)\) could introduce a
pole at the moving divisor used below. No coefficient-field coordinate
is promoted to an original coordinate.

## 1. Retained actual inputs and the three exact derivatives

Retain the complete hypotheses and conclusions of
[316](principal-paraboloid-conic-factor-unit-scalar-rigidity-pass316-working.md)
and [318](principal-paraboloid-conic-original-slice-speed-pass318-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
\mathcal F=\ker_L\partial_s,\quad
[\mathcal F:\mathbb C(t)]<\infty,\quad
\mathcal F^{\partial_t}=\mathbb C,\quad L=\mathcal F(s),\\
\operatorname{Frac}\mathcal B=\mathcal F(X,s,\sigma),\qquad
\mathcal F[\mathcal B]=\mathcal F[X,s,\sigma],\qquad
a=EX,\ h=N\sigma\in\mathcal F^* .
\end{gathered}
\tag{2}
\]
The selected N is an actual locally nilpotent derivation of A.
Its extension to \(A[u]\) kills u and commutes with E.

Write
\(\omega=ah\in\mathcal F^*\), and retain the actual auxiliary
derivation318:
\[
\mathscr P=aN-(NX)E,\qquad
\mathscr PX=0,\quad [E,\mathscr P]=0,\qquad
\mathscr P=\omega\partial_\sigma
   \text{ on }\mathcal F[X,s,\sigma].
\tag{3}
\]
It is locally nilpotent on the original ring, not only on the
coefficient-field polynomial ring.

Assume (1), put \(T=t-\tau\), and denote \(b_P\) of316 by
\(\rho\). Then \(b_V=0\), and the precise formulas318 give
\[
\begin{gathered}
\mathscr PY=\omega(X-\rho),\qquad
\mathscr P^2Y=0,\\
\mathscr P^2Z=6\omega^2,\qquad \mathscr P^3Z=0,\\
\mathscr P^3W=\frac{12\omega^3}{c},\qquad
\mathscr P^4W=0 .
\end{gathered}
\tag{4}
\]
The coefficient 6 comes from \([\sigma^2]Z=3\), and 12/c
from \([\sigma^3]W=2/c\). These hold for the full original
generators, including their X-dependent terms.

The P-coefficient of the restricted-gradient identity316 gives
\[
\rho_s=0,\qquad
\rho_t=-\frac{4T\mathcal C}{c}\ne0,\qquad
\mathcal C\in\mathcal F^* .
\tag{5}
\]
Thus \(\rho\in\mathcal F\setminus\mathbb C\), and in particular
rho is transcendental over \(\mathbb C\).

## 2. Take the original-ring content before passing to \(\mathbb C(X)\)

Let g be a greatest common divisor in the UFD \(\mathcal B\) of the
four components of \(\mathscr P\). Write
\[
\mathscr P X_i=g f_i,\quad X_i\in\{X,Y,Z,W\},\qquad
\gcd(f_X,f_Y,f_Z,f_W)=1 .
\tag{6}
\]
The coefficient ideal
\(I=\mathscr P(\mathcal B)\mathcal B=g(f_X,f_Y,f_Z,f_W)\)
need not be principal. No equality \(I=(g)\) is asserted.

For each \(\Delta\in\{E,\mathscr P\}\), commutation implies
\(\Delta(I)\subseteq I\). Therefore
\[
g\mid(\Delta g)f_i\qquad\text{for every }i .
\]
For each irreducible factor of g, at least one normalized component
has valuation zero, by (6). Comparing valuations proves
\(g\mid\Delta g\). Local nilpotence then forces
\[
Eg=0,\qquad\mathscr Pg=0 .
\tag{7}
\]
Indeed a nonzero derivative has LND degree one less than g,
whereas a nonzero multiple of g has degree at least that of g.

Inside the actual fraction field in (2), the two derivations are
\(a\partial_X\) and \(\omega\partial_\sigma\), with nonzero
coefficient-field scalars. Their common constant field is
\(\mathcal F(s)\). Since \(g\in\mathcal B\subseteq
\mathcal F[X,s,\sigma]\), (7) gives
\[
g\in\mathcal F[s].
\]
But g divides \(\mathscr PY=\omega(X-\rho)\) in that polynomial
ring. Its coefficient of X is \(\omega\in\mathcal F^*\); hence
\[
g\in\mathcal F^* .
\tag{8}
\]
This excludes an X-dependent moving factor from the original content.

Define
\[
D=\mathscr P/g,\qquad \kappa=\omega/g\in\mathcal F^* .
\tag{9}
\]
It is an irreducible locally nilpotent derivation of \(\mathcal B\):
its components are polynomial and have gcd one; (7) gives local
nilpotence by \(D^n b=g^{-n}\mathscr P^n b\).
It fixes X. Localize the invariant ring \(\mathbb C[X]\) to
\(k=\mathbb C(X)\). The derivation remains irreducible and locally
nilpotent on
\[
\mathcal B_k=k[Y,Z,W].
\]
Irreducibility follows by UFD localization, or by clearing denominators
and Gauss's lemma: a nonunit common factor after localization would
lift to a common irreducible factor of the normalized original
components. No additional content is chosen over k.

The exact normalized derivatives are
\[
DY=\kappa(X-\rho),\quad D^2Y=0,\qquad
D^2Z=6\kappa^2,\quad D^3Z=0,\qquad
D^3W=12\kappa^3/c,\quad D^4W=0 .
\tag{10}
\]

## 3. A field-relative triangularization, with Y retained

We use Daigle's triangularization theorem as stated in
[Dasgupta--Gupta, Theorem4.8](https://arxiv.org/html/1701.03635v1).
For an irreducible locally nilpotent derivation of a polynomial
three-ring over a characteristic-zero field, an actual coordinate
Y with \(DY\ne0,\ D^2Y=0\) can be retained in a triangular
coordinate system. The theorem is applied only over the field k,
not over \(\mathbb C[X]\).

All its hypotheses have been checked in Section2. It gives
coordinates U,Y,V of \(\mathcal B_k\) such that
\[
\mathcal B_k=k[U,Y,V],\qquad
DU=0,\quad DY=f(U)\in k[U],\quad DV=j(U,Y)\in k[U,Y].
\tag{11}
\]
These are not claimed to be original complex polynomial coordinates.

The polynomial f is nonconstant. If
\(\kappa(X-\rho)\in\mathbb C(X)\), the intersection
\(\mathcal F[X]\cap\mathbb C(X)=\mathbb C[X]\) and coefficient
comparison in the independent X would give
\(\kappa,\kappa\rho\in\mathbb C\). Since \(\kappa\ne0\), this
contradicts (5).

We next determine precisely which coefficient field (11) uses.
Since \(f(U)=\kappa(X-\rho)\in\mathcal F(X)\), U is algebraic
over \(\mathcal F(X)\). The latter is relatively algebraically
closed in the purely transcendental extension
\(\mathcal F(X)(s,\sigma)=\operatorname{Frac}\mathcal B\).
Thus \(U\in\mathcal F(X)\).

Conversely \(\mathcal F(X)\) is a finitely generated field of
transcendence degree one over k. Since f(U) is nonconstant over k,
it is finite over \(k(f(U))\), and hence algebraic over k(U).
But k(U) is relatively algebraically closed in
\(k(U)(Y,V)=\operatorname{Frac}\mathcal B\), by (11). Therefore
\[
\mathcal F(X)=k(U).
\tag{12}
\]
This is an exact subfield equality, not a descent of the coordinate U.

Furthermore (10) and polynomial-coordinate independence in (11)
give
\[
\kappa^2\in\mathcal B_k\cap k(U)=k[U].
\]
As \(k[U]\) is integrally closed and \(\kappa\in k(U)\), the monic
equation with this square coefficient proves
\[
\kappa\in k[U].
\tag{13}
\]
The control of its moving zeros below uses the stronger previously
proved membership \(\kappa\in\mathcal F^*\), not just (13).

## 4. The moving zero is necessarily a finite U-place

On \(\mathcal F(X)\), take the discrete valuation v associated
with the linear irreducible polynomial \(X-\rho\) in
\(\mathcal F[X]\). It satisfies
\[
v(\kappa)=0,\qquad v(f(U))=v(\kappa(X-\rho))=1 .
\tag{14}
\]
It is trivial on \(k=\mathbb C(X)\). Indeed every nonzero complex
polynomial q has \(q(\rho)\ne0\), because rho is transcendental
over \(\mathbb C\); hence neither the numerator nor denominator
of a nonzero element of k vanishes at \(X=\rho\).

Use the exact equality (12). If \(v(U)<0\), the distinct powers
of U in the nonconstant polynomial \(f(U)\in k[U]\) have
distinct valuations, and their coefficients have valuation zero.
Its leading term would give
\[
v(f(U))=\deg(f)\,v(U)<0,
\]
contradicting (14). Thus U is finite at this place. Its residue
\(u_0\) satisfies
\[
f(u_0)=0,\qquad \kappa(u_0)\ne0 .
\tag{15}
\]
The first assertion also shows \(u_0\) is algebraic over k;
the second follows from (13),(14). Embed the residue field into
an algebraic closure \(\Omega\) of k. Such an embedding exists:
the residue field of \(v_{X-\rho}\) is \(\mathcal F\), with
\(k\) embedded by \(X\mapsto\rho\), and
\([\mathcal F:\mathbb C(\rho)]<\infty\).

This proves the required finite-place assertion without assuming
that a generic zero stays away from a coordinate-dependent infinity.
Had one chosen an arbitrary k-content instead of (6), the resulting
kappa could have had a pole at this same moving place, invalidating
(14). The original-ring argument (8) is what rules that out.

## 5. The specialized original generators have impossible degrees two and three

Extend scalars in (11) to \(\Omega\), and quotient by the D-stable
ideal \((U-u_0)\). Both the original and triangular coordinate
presentations give
\[
\Omega[Y,\overline Z,\overline W]=\Omega[Y,V].
\tag{16}
\]
Here Y is still an independent polynomial coordinate. The induced
derivation kills Y and is
\[
\overline D=j(u_0,Y)\partial_V .
\]
It is nonzero: by (10),(15), its second derivative on \(\overline Z\)
is \(6\kappa(u_0)^2\ne0\). The same relations give
\[
\overline D^2\overline Z\ne0,\quad
\overline D^3\overline Z=0,\qquad
\overline D^3\overline W\ne0,\quad
\overline D^4\overline W=0 .
\tag{17}
\]
Reduction commutes with the derivation because U and the scalar
\(u_0\) are fixed.

Localize (16) over Y, putting \(K_0=\Omega(Y)\). Now
\(j(u_0,Y)\in K_0^*\), so the D-degree of a polynomial in V is
its ordinary V-degree. Thus (16),(17) require
\[
K_0[\overline Z,\overline W]=K_0[V],\qquad
\deg_V\overline Z=2,\quad\deg_V\overline W=3 .
\tag{18}
\]

For completeness, (18) is impossible by an elementary argument in
characteristic zero. Translate V to a new variable xi to remove the
linear term of the quadratic. Subtract its constant and divide by
its leading coefficient, making the first generator \(\xi^2\).
Subtract a multiple of that generator and a constant from the cubic.
Its remaining form is \(\xi(A\xi^2+B)\), with \(A\ne0\).
Consequently the ring generated by the two polynomials has parity
decomposition
\[
K_0[\xi^2,\xi(A\xi^2+B)]
 =K_0[\xi^2]\oplus \xi(A\xi^2+B)K_0[\xi^2].
\tag{19}
\]
To check this equality, the square of the odd generator is already
in \(K_0[\xi^2]\); its even and odd parts therefore have precisely
the displayed form. It cannot contain xi, because
\(A\xi^2+B\) is a nonunit in \(K_0[\xi^2]\).
This contradicts (18), proving the theorem.

## 6. Scope and independent checks

The excluded sector is exactly the \(d=0\) part of the actual
reciprocal conic family in316/318. No equality
\(\mathcal F=\mathbb C(t)\), original coordinate U, invariant
coordinate of A, or unrestricted cancellation conclusion is used.
The \(d\ne0\) conic family is not treated here.

The full318 source was read before this argument. The stated
triangularization theorem was freshly checked in its primary
research source, Theorem4.8 and its citation to Daigle's
*Triangular Derivations of \(k[X,Y,Z]\)*, JPAA214(2010),1173--1180.
It requires irreducibility over the field and the retained
coordinate Y; it requires no slice of D.

The original-content, field-intersection, finite-valuation and
special-fiber steps are mathematical arguments, not finite numerical
controls. No saved checker was executed, imported, compiled or rerun.
No earlier proof, index or packet was edited. No historical novelty,
external expert certification or proof-assistant verification is claimed.
