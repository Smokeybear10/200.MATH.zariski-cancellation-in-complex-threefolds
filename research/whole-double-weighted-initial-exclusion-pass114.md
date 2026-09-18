# Equal-weight coprime initial forms are excluded

In the actual proper whole-double branch, the two distinguished coefficients
a and b cannot have equal weighted order and coprime weighted initial forms
in any formal base coordinates with positive integer weights. This is a
criterion on the actual coefficients satisfying the retained identities,
not permission to replace them by arbitrary generators of their ideal.

The argument forces coprime initial factors of P and lifts them completely.
It does not assume that every m-primary ideal admits the stated weights,
cover unequal weighted orders, or finish the proper whole-double problem.

## 1. Precise coefficient hypotheses

Work over the completed regular local base R=C[[x,y]], with maximal ideal
m. The actual restrictions from
[product-index112](whole-double-product-index-pass112.md) and the
[analytic-prime input113](whole-double-ramified-completion-descent-pass113.md)
include

\[
\begin{gathered}
a,b\in\mathfrak m\setminus\{0\},\quad
J=(a,b)\text{ is }\mathfrak m\text{-primary},\quad h\ne0,\\
b^2=s h+a^2u+abv\quad(s,u,v\in R),\\
B_2\in\mathfrak m(h)+\mathfrak m(a^2)
          +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
P=ah+bB_2=w p^e\ne0,\quad
w\in R^*,\quad p\text{ prime in }R,\quad e\ge1.
\end{gathered}
\tag{1}
\]

The actual setup has h in m squared, although the argument below only needs
h to be a nonzero nonunit. The fact that p remains prime after completion
is substantive: it follows from the supported integral whole-fiber argument
and finite normalization113, not from algebraic irreducibility alone.

Suppose there are positive integers alpha,beta with

\[
\operatorname{wt}x=\alpha,\quad\operatorname{wt}y=\beta,
\quad\operatorname{wt}(a)=\operatorname{wt}(b)=d>0,
\qquad A=\operatorname{in}(a),\quad B=\operatorname{in}(b),
\qquad\gcd(A,B)=1\text{ in }\mathbb C[x,y].
\tag{2}
\]

All initial forms in this note refer to these weights. Positive weights
make the filtration separated and equivalent to the m-adic filtration.
Every nonzero series has a nonzero polynomial initial form, and weighted
orders of products add because the associated graded polynomial ring is
a domain. Put delta=min(alpha,beta), the least positive weight of m.

## 2. The coefficient identity supplies the correct leading factors

In (1), a squared and ab have weight 2d, as does b squared. The weight-2d
part of b squared-a squared u-abv is
B squared-A squared u(0)-ABv(0). It is nonzero: otherwise A would divide
B squared, contradicting coprimality in (2). Therefore s is nonzero and
s h has weight exactly 2d. Set q=wt(h), S=in(s), and H=in(h). Then

\[
\begin{gathered}
0<q\le2d,\qquad \operatorname{wt}(s)=2d-q,\\
S H=B^2-A^2u(0)-ABv(0),\qquad \gcd(A,H)=1,\\
\operatorname{wt}(B_2)\ge q+\delta,\qquad
\operatorname{wt}(P)=d+q,\qquad \operatorname{in}(P)=A H.
\end{gathered}
\tag{3}
\]

For the second coprimality assertion, any irreducible polynomial dividing
both A and H would, by the displayed identity, divide B squared and hence
B. No coprimality of S and A is needed.

The sharp bound for B2 in (1) has four summands of weights at least
q+delta, 2d+delta, 2d+delta, and 2d+2delta. Because q is at most 2d,
their minimum is at least q+delta. Thus bB2 has weight strictly larger
than d+q, and cannot cancel the leading term of ah. This verifies the
leading product in (3), rather than inferring it from coprimality alone.
If B2 is zero, its weighted order is interpreted as infinity.

## 3. The weighted initial-factor ideal contains every later error

Here is the graded calculation used for lifting. Let T=C[x,y] with the
given positive grading, and let A,H be the coprime homogeneous polynomials
of degrees d,q in (3). Their common zero scheme is zero dimensional:
otherwise an irreducible curve in the plane would supply a common prime
polynomial factor. Positive homogeneity then puts its support at the
origin. Equivalently T/(A,H) is a finite-dimensional graded C-vector space.

The sequence A,H is regular in T. Indeed A is nonzero, and A dividing Hf
with gcd(A,H)=1 implies A divides f. The exact homogeneous sequence is

\[
0\longrightarrow T(-d-q)
 \xrightarrow{\ z\mapsto(Hz,-Az)\ }
 T(-d)\oplus T(-q)
 \xrightarrow{\ (u,v)\mapsto Au+Hv\ }
 T\longrightarrow T/(A,H)\longrightarrow0.
\tag{4}
\]

For completeness, every syzygy Au+Hv=0 has u=Hz and v=-Az by the same
coprimality argument. Thus (4) needs no assertion about an unknown formal
factorization. Count monomials in each graded piece. The Hilbert series
of T is 1/((1-z^alpha)(1-z^beta)), and exactness gives

\[
\begin{gathered}
\sum_{j\ge0}\dim_{\mathbb C}(T/(A,H))_j\,z^j
 =\frac{(1-z^d)(1-z^q)}{(1-z^\alpha)(1-z^\beta)},\\
\deg\left(\sum_j\dim_{\mathbb C}(T/(A,H))_j z^j\right)
 =d+q-\alpha-\beta,\\
T_j\subseteq(A,H)\qquad(j>d+q-\alpha-\beta).
\end{gathered}
\tag{5}
\]

The series on the left is a nonzero polynomial by finite dimensionality.
Multiplying by the denominator and comparing highest degrees proves the
middle equality. No positivity or cancellation guess about the rational
expression is needed. In particular every homogeneous error of weight
strictly greater than d+q lies in (A,H).

## 4. Complete factor lifting

Put D=d+q, and begin with L=A and K=H as elements of R. Their product
agrees with P through weight D by (3). Suppose the current product agrees
below weight j, for some integer j>D. Its weight-j error E_j lies in
(A,H) by (5). Homogeneous components of a polynomial representation give

\[
\begin{gathered}
E_j=H U_{j-q}+A V_{j-d},\qquad
L\longmapsto L+U_{j-q},\qquad
K\longmapsto K+V_{j-d},\\
\operatorname{wt}(U_{j-q})=j-q>d,\quad
\operatorname{wt}(V_{j-d})=j-d>q,
\end{gathered}
\tag{6}
\]

where a zero correction is allowed. Existing higher-weight terms of the
two factors contribute only above weight j. The product of the new
corrections has weight 2j-D, strictly greater than j. Therefore this
improves the agreement by one integer weight. Weights with no monomials
simply have zero error. Iterating gives convergent formal factors with

\[
\begin{gathered}
P=L K,\qquad \operatorname{in}(L)=A,
\quad\operatorname{in}(K)=H,
\qquad\gcd(L,K)=1,\\
\boxed{\quad
\text{the actual proper whole-double coefficients cannot satisfy (2).}
\quad}
\end{gathered}
\tag{7}
\]

The convergence is in the weighted, hence ordinary formal, topology.
If a nonunit formal divisor divided both L and K, its positive-degree
initial form would divide both A and H, contrary to (3). This proves
the claimed coprimality of the limiting factors.

Since d and q are positive, both factors are nonunits. Their product has
at least two distinct prime divisors in the regular local UFD R. This
contradicts (1), where P is a unit times a power of the single prime p.
The individual limiting factors need not themselves be irreducible.

## 5. Limits and provenance

This criterion applies to a formal choice of base coordinates and weights
for the same coefficients a,b satisfying (1). If a new pair of ideal
generators is used instead, the asymmetric identities must first be
reconstructed for that pair, as was done in the separate
[smooth-a114 proof](whole-double-smooth-a-exclusion-pass114.md). Coprimality
of initial forms with unequal weighted orders is not covered by (2).

The proof is compatible with the separate
[square-ideal exclusion114](whole-double-square-ideal-exclusion-pass114.md),
but does not require h to belong to J squared or a reduced Artinian base.
It gives a new obstruction to surviving coefficient configurations, not
their full classification or an actual realization of any remaining one.
The arbitrary original-frame entry and general cancellation targets remain
open.

Root proposed the weighted criterion. General reconstructed the leading
identity, the exact graded sequence and the complete lifting argument.
The square-ideal114 proof was fully read before this deduction; the actual
coefficient and analytic-prime inputs remain the already identified112--113
dependencies. No new primary-source theorem, numerical method or execution
is introduced. Files through113 and the other authors' notes are unchanged.
