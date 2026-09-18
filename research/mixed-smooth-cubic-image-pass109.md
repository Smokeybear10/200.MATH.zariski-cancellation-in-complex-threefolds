# The smooth second-image ideal must have length at least two

In the actual smooth-a mixed branch retained in108, the invisible
second-degree basis element H belongs to mF3, not only to mF4.
This makes the third derivative-image ideal nonprincipal. The two
products rG and rH then give a residue-rank obstruction: the second
residual ideal is strictly contained in the third. In particular the
k=1 subcase is excluded. This does not exclude every smooth-a fiber
or produce the original coordinate frame from cancellation input.

The separate [smooth-a determinant proof109](mixed-smooth-quartic-determinant-exclusion-pass109.md)
now excludes this entire conditional sector. Its broader
[smooth-B1 extension109](mixed-smooth-B1-exclusion-pass109.md)
also excludes a first-order B1 without assuming a first-order a.
The six-equation argument below is retained as an independent
structural route to the narrower k=1 exclusion, not as an additional
remaining branch or an input to either determinant proof.

## 1. Exact inputs and normalization

Work over the regular local invariant surface R=S_m, with maximal
ideal m, in the supplied collapsed mixed quadratic sector with
nonzero speed normal. Use the smooth-a normalization of108. Thus
A_R is a flat domain, N is its actual locally nilpotent derivation
with full kernel R, and F_j=ker N^(j+1) is free of rank j+1.
The whole fiber is D[c], where D=C[G]/(G²(G−1)). The relevant
frozen conclusions are
\[
\begin{gathered}
F_2=R\{1,G,H\},\qquad F_1=R\{1,r\},\qquad
r=aG+bH,\qquad Nr=P\ne0,\\
NG=\epsilon br+a,\qquad NH=-\epsilon ar+B_2,
\qquad \epsilon\in R^*,\qquad
a\in\mathfrak m\setminus\mathfrak m^2,\\
J_2=(a,b)\subset\mathfrak m,\qquad \gcd(a,b)=1,
\qquad k=\operatorname{length}_R R/J_2,\\
F_4=R\{1,G,G^2,c,U\},\qquad
\bar H=\bar U=\bar r=0,\qquad W_3=D,\\
N^4(G^2)=6\epsilon^2b^2P^2,\quad
N^4c=LP^2,\quad N^4U=6\epsilon^3aP^2,\\
J_4=(a,L)=(a,t^n),\quad I_4=P^2J_4,
\quad b^2\in\mathfrak mJ_4,\quad 1\le n<2k,\\
2H=\zeta+2\beta G-\epsilon aG^2-2\epsilon bGH-b^2U,
\qquad \beta,\zeta\in\mathfrak m.
\end{gathered}
\tag{1}
\]
Here t is a complementary regular parameter. Bars refer to the
entire nonreduced fiber. W3 is the actual image of F3 there,
not its internal module fiber. All these data are retained from
the actual construction and residue proof108.[^inputs]

## 2. An exact cubic basis

Scale two actual fourth-degree elements by invariant units:
X=U/(6epsilon³) and Z=G²/(6epsilon²). Since b² belongs to
m(a,L), choose sigma,tau in m with b²=a sigma+L tau. Define
\[
\begin{gathered}
Z=G^2/(6\epsilon^2),\qquad X=U/(6\epsilon^3),\qquad
b^2=a\sigma+L\tau,\quad \sigma,\tau\in\mathfrak m,\\
T=Z-\sigma X-\tau c,\qquad V=LX-ac,\\
\boxed{\qquad F_3=R\{1,G,T,V\}.\qquad}
\end{gathered}
\tag{2}
\]
Indeed the N4 row on the last three coordinates Z,c,X is
P²(b²,L,a). After subtracting a multiple of T, a row-kernel
vector is supported on c,X and satisfies Lq+as=0. Since a
and L are coprime, its exact syzygy module is R(-a,L), which
is precisely the vector V. This proves both spanning and
independence over R, not merely over its fraction field.

The whole residues of 1,G,T are independent: T reduces to
G²/(6epsilon(m)²). V has zero whole residue. Thus the whole
residue map from F3/mF3 has kernel exactly the line C[V].

## 3. H has zero internal cubic class

Expand GH in the actual F4 basis as
GH=j0+j1G+j2G²+jc c+jU U. Its whole residue is zero, because
H has zero whole residue. Independence of 1,G,G²,c therefore
puts j0,j1,j2,jc in m; no assertion about jU is needed.
The last identity in (1) shows that the c coefficient of H
in that F4 basis is exactly -epsilon b jc, and hence belongs
to m². Write H in the cubic basis (2). This gives
\[
\begin{gathered}
H=h_0+h_1G+vT+wV,\qquad h_0,h_1,v\in\mathfrak m,\\
[c]_{F_4}H=-\epsilon b j_c=-v\tau-wa\in\mathfrak m^2,\\
w\in\mathfrak m,\qquad
\boxed{\qquad H\in\mathfrak mF_3.\qquad}\\
v=-3\epsilon^3a-6\epsilon^3b j_2,
\qquad v\in\mathfrak m\setminus\mathfrak m^2.
\end{gathered}
\tag{3}
\]
The first three coefficients are in m by the independent
whole residues of 1,G,T. Since v and tau are in m, comparison
of the c coefficient gives wa in m². The first-order parameter
a then forces w into m: a unit w would leave wa of order one.
The last line compares G² coefficients in (1) and (2); it is
an additional first-order statement, not needed for membership.

This argument never contracts through the non-pure F2 or F3.
It uses the specified actual bases and coefficient comparison.

## 4. The third image has a proper residual ideal

The exact sequence F2 to F3 to I3, with last map N³, remains
right exact after reduction modulo m. By (3) the internal
image of F2 is spanned precisely by the independent classes
of 1,G. Hence
\[
\begin{gathered}
\mu_R(I_3)=4-2=2,\qquad
I_3=P^2J_3,\\
J_3\subsetneq R\text{ is an }\mathfrak m\text{-primary
two-generated complete intersection}.
\end{gathered}
\tag{4}
\]
For the normalization, at every height-one invariant prime
the exact divisor filtration gives the valuation of I3 as
twice that of I1=(P). In degree two this is formula107; in
degree one the retained slice division makes every image
ideal a unit. In the UFD R, every element of I3 is therefore
divisible by P², and J3 has no common prime divisor.[^divisors]
Multiplication by P² identifies J3 with I3 as R-modules.
The two-generator count makes J3 proper. With no height-one
support it is maximal-primary, and its two generators form
a regular sequence in the regular local surface.

## 5. Products force a strict inclusion and exclude k=1

Both rG and rH belong to F3 and have zero whole residue.
Their classes in F3/mF3 consequently lie in the single line
C[V] from (2). Apply the linear map induced by N³ from that
module fiber to I3/mI3. The characteristic-zero product rule
gives the exact identities
\[
\begin{gathered}
N^3(rG)=3P\,N^2G=3\epsilon bP^2,\qquad
N^3(rH)=3P\,N^2H=-3\epsilon aP^2,\\
J_2\subseteq J_3,\qquad
\dim_{\mathbb C}\operatorname{image}
\bigl(J_2\longrightarrow J_3/\mathfrak mJ_3\bigr)\le1.
\end{gathered}
\tag{5}
\]
The first line proves the inclusion after cancelling P².
The one-dimensional bound follows from the one-dimensional
source line, using the R-module isomorphism J3 to I3 given
by multiplication by P². It does not identify a whole-fiber
kernel with an internal derivative-image kernel.

If J2 equaled J3, its image in J3/mJ3 would have dimension
two by (4), contradicting (5). Because J3 contains the smooth
parameter a, pass to the DVR R/(a). The ideal J2 has image
(t^k), while J3 has image (t^h) for some positive integer h.
Inclusion and its strictness give
\[
\boxed{\qquad
J_3=(a,t^h),\quad 1\le h<k,
\qquad k\ge2.
\qquad}
\tag{6}
\]
Thus the actual smooth-a subcase with k=1 cannot occur.
This is a residue-product obstruction, not a comparison of
the unrelated contact orders of P with a and with L.
The higher-contact bound of108 by itself was not a contradiction.

## Scope and verification

The H membership and product argument use only the stated
smooth-a consequences of the actual frame, the finite free
degree modules, and the exact retained divisor valuations.
No new primary classification theorem, infinite completion,
or selected-c contact computation is required. The smooth
normalization, actual quartic construction and full residue
argument108, and the exact divisor proof107 were reread
through EOF before this deduction.

The stricter conclusion leaves k at least two and does not
exclude all smooth-a or higher-order proper ideals. It gives
no general original-coordinate witness or cancellation theorem.
Root independently reconstructed the rank-product argument
and the residual-ideal normalization; the coefficient proof
of H in mF3 is given explicitly here. All files through108
remain unchanged.

[^inputs]: [Smooth-generator construction108](mixed-smooth-generator-quartic-pass108.md), the exact normalized conic and actual U; [quartic residue108](mixed-smooth-quartic-residue-pass108.md), the F4 basis, W3=D and strict J4 bound; [pure quartic row108](mixed-pure-quartic-row-pass108.md), the exact row method.

[^divisors]: [Quadratic divisor filtration107](quadratic-constant-divisor-filtration-pass107.md), all-degree image formula; and [degree-one slice105](mixed-cubic-rank-defect-pass105.md). The finite free degree modules are established in [module102](quadratic-degree-module-fiber-rigidity-pass102.md).
