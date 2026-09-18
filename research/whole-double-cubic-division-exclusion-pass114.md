# Cubic division excludes the proper whole-double coefficient system

The actual proper-image whole-double branch is incompatible with the
coefficient identities112 and the single analytically prime support113.
A homogeneous cubic has a simple root over the completed base. Polynomial
division produces two nonunit factors of P whose joint ideal contains the
square of the m-primary residual ideal. They cannot both be powers of the
same prime.

This excludes the specified proper residual second-image alternative. It
does not give an original constant-acceleration frame for an arbitrary
cancellation input, recognize the global threefold, or prove cancellation.

## 1. Exact actual inputs, and the algebraic statement they supply

Let R be the completed regular local complex base surface, with maximal
ideal m. In particular R is a complete local UFD and a domain. The actual
identities from
[product-index112](whole-double-product-index-pass112.md) and the
[analytic-prime conclusion113](whole-double-ramified-completion-descent-pass113.md)
give

\[
\begin{gathered}
J=(a,b)\text{ is }\mathfrak m\text{-primary},\quad
a,b\in\mathfrak m\setminus\{0\},\quad h\in\mathfrak m,\\
b^2=s h+a^2u+abv,\qquad s,u,v\in R,\\
B_2\in\mathfrak m(h)+\mathfrak m(a^2)
       +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
P=ah+bB_2=w p^e\ne0,\qquad
w\in R^*,\quad p\text{ prime in }R,\quad e\ge1.
\end{gathered}
\tag{1}
\]

The actual branch has the stronger h in m squared, but only h in m is
needed below. Completion preserves J being m-primary. The assertion that
p is prime here uses the separately proved analytic irreducibility; it is
not inferred just from the original base equation being irreducible.

The coefficient bound can be simplified without changing generators.
The relation for b squared gives m squared(b squared) contained in
m squared(h)+m squared(aJ). Hence B2 belongs to m(h)+m(aJ). Choose

\[
\begin{gathered}
B_2=h\eta+a\zeta,\qquad \eta\in\mathfrak m,
\quad\zeta\in\mathfrak mJ,\\
\zeta=az+bt,\qquad z,t\in\mathfrak m,\\
P=(a+b\eta)h+ab(az+bt).
\end{gathered}
\tag{2}
\]

These are ideal-membership choices in R. They do not assert a polynomial
coordinate change or a presentation of the actual algebra from arbitrary
coefficient data. From this point onward, the proof is a contradiction
among (1)--(2) in the coefficient ring itself.

## 2. A simple root of the homogeneous cubic

Use an independent polynomial variable T and define

\[
\begin{gathered}
F(T)=(T+\eta)(1-T^2u-Tv)+sT^2z+sTt,\\
F(0)\in\mathfrak m,\qquad F'(0)\equiv1\pmod{\mathfrak m},\\
\rho\in\mathfrak m,\quad F(\rho)=0,\qquad
D=1-\rho^2u-\rho v\in R^*,\quad E=F'(\rho)\in R^*.
\end{gathered}
\tag{3}
\]

The first two properties follow because eta,z,t belong to m. The simple
root at zero modulo m lifts in the complete ring R. Explicitly, start at
zero and repeatedly subtract the error divided by the derivative. The
derivative remains a unit, the error order at least doubles, and the
successive approximations converge to rho. This does not require F to be
monic. The displayed unit properties of D and E follow by reduction
modulo m. No bound on the residues of s,u,v is imposed.

Monic division by T-rho gives Q(T) in R[T] of degree at most two with
F(T)=(T-rho)Q(T). Introduce independent homogeneous variables A,B and put
Q2(A,B)=B squared Q(A/B), which is an actual homogeneous polynomial of
degree two. Similarly B cubed F(A/B) is a homogeneous cubic. Thus

\[
\begin{gathered}
B^3F(A/B)=(A-\rho B)Q_2(A,B),\qquad
Q_2(\rho,1)=E,\\
sP=(a-\rho b)Q_2(a,b),\qquad L=a-\rho b\in\mathfrak m.
\end{gathered}
\tag{4}
\]

The notation involving A/B only abbreviates the homogenized polynomials;
no inversion of b is used. To verify the second line, expand (2) and
replace s h by b squared-a squared u-abv using (1). Polynomial identities
over R can be evaluated at a,b even though their coefficients also belong
to R. There is no assertion that a,b are independent variables or that a
quotient coefficient ring has a section.

## 3. Removing the auxiliary factor s

Since J is m-primary in a regular local surface, a and b have no common
prime factor. In particular s is nonzero: if s were zero, (1) would make
the nonunit a divide b squared, contradicting this coprimality. Also L is
nonzero. Otherwise a=rho b would give the principal ideal J=(b), which
cannot be m-primary in dimension two.

No prime can divide both s and L. Indeed, modulo such a prime, a=rho b
and the relation (1) gives b squared D=0. Since D is a unit, that prime
would divide b, hence a, contradicting coprimality. Therefore gcd(s,L)=1
in the UFD R. Equation (4) implies L divides P. Define H=P/L in R;
it is nonzero. Cancelling the nonzero L in the domain gives

\[
\begin{gathered}
P=LH,\qquad sH=Q_2(a,b),\qquad \gcd(s,L)=1,\\
s h\equiv b^2D\pmod L,\qquad
sH\equiv b^2E\pmod L.
\end{gathered}
\tag{5}
\]

The second congruence uses the homogeneity of Q2 and a=rho b modulo L,
so Q2(a,b) is congruent to b squared Q2(rho,1). Neither congruence assumes
R/(L) is a domain. L has not been asserted prime or smooth.

## 4. Both factors are nonunits and their joint ideal is m-primary

Multiply the last two congruences in (5) by E and D respectively and
subtract. The result is s(DH-Eh) in (L). Coprimality of s and L permits
cancellation modulo L in the following precise UFD sense: every prime
power dividing L divides DH-Eh, since none divides s. Thus

\[
\begin{gathered}
DH-Eh\in(L),\qquad
H\in(h,L)\subseteq\mathfrak m,\\
b^2E\in(L,sH)\subseteq(L,H),\qquad b^2\in(L,H),\\
J=(a,b)=(L,b),\qquad J^2\subseteq(L,H),\qquad
\sqrt{(L,H)}=\mathfrak m.
\end{gathered}
\tag{6}
\]

The first containment for H uses that D is a unit. The containment for
b squared uses that E is a unit. This proves nonunit status of the
cofactor, rather than attempting to infer it merely from P=LH. The joint
ideal is proper because L,H belong to m; it is m-primary because it
contains J squared.

Both L and H are nonzero nonunits. But (1) and the UFD property make every
nonunit factor of P a unit times a positive power of p. Consequently
(L,H) would be contained in the height-one ideal (p), contradicting (6).
Therefore

\[
\boxed{\quad
\text{the actual proper residual second-image whole-double alternative
is impossible.}\quad}
\tag{7}
\]

## 5. Scope and dependence

The proof needs neither a smooth generator of J, membership h in J
squared, nor weighted coprime initial forms. It does not exchange a and b.
The earlier bounded exclusions114 are consistent special consequences;
they are not required to derive the cubic division contradiction.

The actual inputs remain indispensable. Product-index112 used the
canonical whole-double action, actual free degree modules and divisor
determinants, and pure residue contraction to obtain (1). The one-prime
support113 used the polynomial cylinder's topology, the actual generic
divisor models, and finite curve normalization. This proof does not
replace those geometric hypotheses by a claim about every sliced action.

The independently proved completed-kernel rigidity113 is not needed here:
only a scalar factorization in the completed base is used. No completion
of an R-linear kernel, formal slice descent, or recognition of the original
polynomial coordinate tuple enters the argument.

Root proposed the universal cubic. General independently supplied the
homogeneous division, removal of s, cofactor nonunit argument, and joint
ideal contradiction. Root's separate explicit-cofactor calculation is an
independent reconstruction of the same exclusion, not a second resolved
case. No new numerical method or execution is asserted here, and no file
through113 or another author's proof is modified. Independent AI review is
not human expert review, formal verification, or a novelty clearance.
