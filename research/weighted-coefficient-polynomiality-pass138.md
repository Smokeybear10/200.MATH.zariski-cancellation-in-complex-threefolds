# Weighted coefficient polynomiality for a differential operator

A polynomial in two formal variables satisfying the differential
condition below has polynomial coefficients in \(\kappa\). Its original
\((2,1)\)-weighted degree bounds its ordinary total degree after
\(\kappa\) is counted as a third polynomial variable.

This is a differential-field lemma. It does not assume that the field
is rational, that a finite algebraic extension has been trivialized,
or that formal differential data come from polynomial coordinates.
Its potential geometric application requires a separately proved
actual chart.

## 1. Statement and field assumptions

Let \(L\) be a field of characteristic zero equipped with commuting
derivations \(\partial_\tau,\partial_\kappa\). Suppose
\[
\kappa\in L,\qquad
\partial_\kappa\kappa=1,\qquad \partial_\tau\kappa=0,\qquad
K=\ker(\partial_\kappa|_L),\qquad r\in K^* .
\tag{1}
\]
Commutation makes \(K\) stable under \(\partial_\tau\).
The element \(\kappa\) is transcendental over \(K\): differentiating
a monic minimal polynomial of positive degree would give a nonzero
polynomial of smaller degree vanishing at \(\kappa\).
Thus \(K[\kappa]\) really is a polynomial ring.

Extend the two coefficient derivations to \(L[X,y]\) by fixing the
independent formal variables \(X,y\). Let \(\partial_y\) fix \(L\)
and \(X\). Define
\[
\mathcal L=X\partial_y-\partial_\tau+r y\partial_\kappa,
\qquad
\operatorname{wt}X=2,\quad \operatorname{wt}y=1.
\quad
\mathcal L W\in L
\ \Longrightarrow\
W\in K[\kappa,X,y],\qquad
\deg_{\kappa,X,y}W\le \operatorname{wt}_{X,y}W
\tag{2}
\]
for every nonzero \(W\in L[X,y]\). All coefficients in \(L\) initially
have weight zero. The zero polynomial satisfies the polynomiality
conclusion separately.

Neither \(\partial_\tau r=0\) nor the existence of an element named
\(\tau\) with prescribed derivatives is required. In particular,
the notation \(\partial_\tau\) does not add an unstated coordinate
hypothesis. No finite-generation or algebraicity assumption on
\(L/K(\kappa)\) is used.

## 2. Polynomial primitives inside the exact field

We use the following elementary fact. If \(f\in L\) and
\(\partial_\kappa f=\sum_{j=0}^d a_j\kappa^j\) with \(a_j\in K\),
then
\[
f-\sum_{j=0}^d\frac{a_j}{j+1}\kappa^{j+1}\in K.
\tag{3}
\]
The derivative of the displayed difference is zero, so it belongs
to the exact kernel defining \(K\). Characteristic zero permits all
the divisions. If \(\partial_\kappa f=0\), simply \(f\in K\).
Hence a polynomial derivative forces a polynomial element, without
assuming a primitive exists in an unspecified extension.

Furthermore \(\partial_\tau\) maps \(K[\kappa]\) into itself and
does not increase its \(\kappa\)-degree: it differentiates the
coefficients in \(K\) and fixes \(\kappa\).
This is the only use of the second derivation's compatibility with
the constant field in the descent.

## 3. The triangular coefficient equations

Let \(n=\operatorname{wt}_{X,y}W\). Write its homogeneous pieces as
\[
\begin{gathered}
W=\sum_{N=0}^n W_N,\qquad
W_N=\sum_{i=0}^{\lfloor N/2\rfloor}
c_{N,i}X^i y^{N-2i},\qquad c_{N,i}\in L,\\
\delta_0=X\partial_y+r y\partial_\kappa,\qquad
\delta_0W_N=\partial_\tau W_{N+1}\quad(0\le N\le n),
\qquad W_{n+1}=0 .
\end{gathered}
\tag{4}
\]
The operator \(\delta_0\) raises weight by one, while
\(\partial_\tau\) preserves it. Thus the second line is precisely
the positive-weight part of \(\mathcal LW\in L\).
The remaining weight-zero equation is
\(-\partial_\tau W_0=\mathcal LW\); no assumption about the
initial right-hand side's membership in \(K\) is made.

Put \(c_{N,-1}=0\), and regard an index outside the displayed range
of a homogeneous piece as zero. For
\(0\le i\le\lfloor N/2\rfloor\), compare the coefficient of
\(X^i y^{N+1-2i}\) in (4):
\[
r\,\partial_\kappa c_{N,i}
+ (N-2i+2)c_{N,i-1}
=\partial_\tau c_{N+1,i}.
\quad
N=2m+1\ \Longrightarrow\
c_{N,m}=\partial_\tau c_{N+1,m+1}.
\tag{5}
\]
The second equality is the additional coefficient of \(X^{m+1}\)
when \(N\) is odd. It is a compatibility equation, not a missing
primitive step. If \(N\) is even, there is no additional coefficient:
the last monomial of \(W_N\) has no \(y\) to differentiate.

Proceed downward in \(N\), beginning with \(N=n\). At a fixed
weight proceed upward in \(i\). The right side of the first
equation in (5) is polynomial in \(\kappa\) once \(W_{N+1}\)
has polynomial coefficients. The preceding coefficient
\(c_{N,i-1}\) is polynomial by the inner induction, starting from
zero at \(i=0\). Since \(r^{-1}\in K\), this proves that
\(\partial_\kappa c_{N,i}\) is polynomial in \(\kappa\).
Equation (3) then proves \(c_{N,i}\in K[\kappa]\).

For the initial weight, \(W_{n+1}=0\), so this same reasoning
starts with \(\partial_\kappa c_{n,0}=0\).
The induction also includes \(N=0\): its equation is
\(r\partial_\kappa c_{0,0}=\partial_\tau c_{1,0}\).
Thus neither the constant piece nor an odd endpoint is omitted.
The actual coefficients already satisfy the extra equation in (5);
the proof does not assert that arbitrary choices of integration
constants satisfy it.

This proves the polynomiality assertion in (2).

## 4. The ordinary degree bound

More precisely, the same two inductions give
\[
\deg_\kappa c_{N,i}\le n-N+i,\qquad
0\le N\le n,\quad 0\le i\le\lfloor N/2\rfloor.
\tag{6}
\]
Zero coefficients may be omitted from degree statements.
At \(N=n\), the first coefficient belongs to \(K\). Each subsequent
primitive adds at most one to the preceding coefficient's degree,
so \(\deg_\kappa c_{n,i}\le i\).

For \(N<n\), the first term on the right after solving (5) for
\(\partial_\kappa c_{N,i}\) has degree at most
\(n-N-1+i\). The previous coefficient in that equation has the
same bound by the inner induction. Taking a polynomial primitive
adds at most one; its arbitrary constant in \(K\) does not violate
the nonnegative bound \(n-N+i\). This proves (6), even when
\(r\) varies under \(\partial_\tau\).

A monomial \(\kappa^jX^iy^{N-2i}\) in \(W_N\) therefore has
ordinary degree
\(j+i+N-2i=j+N-i\le n\), proving the second conclusion in (2).

There is also an endpoint restriction: the highest nonzero weight
\(n\) is even. If \(n=2m+1\), the last equation in (5) gives
\(c_{n,m}=0\), since \(W_{n+1}=0\). Substituting this into the
preceding coefficient equation forces \(c_{n,m-1}=0\), and
continuing backward forces every coefficient of \(W_n\) to vanish.
This contradicts the definition of \(n\). This observation is not
needed for the polynomiality or degree proof.

## 5. Conditional chart consequence and limits

Suppose a separate actual-chart argument supplies
\[
\begin{gathered}
W(X,y)=\sum_{j=0}^{\ell}w_j(y)X^j,\qquad
w_j\in L[y],\qquad \deg_y w_j\le2(\ell-j),\\
\bigl(X\partial_y-\partial_\tau+r y\partial_\kappa\bigr)W\in L.
\quad\text{Then}\quad
W\in K[\kappa,X,y],\qquad \deg_{\kappa,X,y}W\le2\ell .
\end{gathered}
\tag{7}
\]
Indeed its original weighted degree is at most \(2\ell\), so (2)
applies. If that chart also expresses \(\kappa,y\) as affine-linear
polynomials in actual good coordinates over \(K\), substitution
preserves this ordinary degree bound. A monic expression for an
actual bad coordinate over \(K\) can then follow.

This lemma does not establish any of those geometric premises.
In particular, it does not prove that \(K\) has transcendence
degree one over \(\mathbb C\), that it lies in an actual invariant
field, or that the monic-field relation descends to a complex
polynomial coordinate. Those are distinct requirements.
The quadratic calculation136 and its speed-based extension137
provide earlier instances of this separation.[^1][^2]

The nonzero coefficient \(r\) is essential to this statement.
For example, in \(L=\mathbb Q(\kappa)\), with
\(\partial_\kappa=d/d\kappa\), \(\partial_\tau=0\), and \(r=0\),
the polynomial \(W=\kappa^{-1}\in L[X,y]\) satisfies
\(\mathcal LW=0\) but does not belong to \(\mathbb Q[\kappa,X,y]\).
The theorem makes no claim for that omitted hypothesis.

## Sources

1. [Polynomial coefficients over a one-variable field in the conical mismatch branch](conical-mismatch-coefficient-polynomiality-pass136.md),
   Sections 2--5. Earlier exact-constant-field and polynomial-primitive
   arguments in the quadratic chart.
2. [A speed-based tangent chart for nonlinear conical frames](universal-conical-tangent-reduction-pass137.md),
   Sections 4--5. The quadratic differential operator after the
   actual tangent and whole-line reductions.

The proof above is complete as a differential-field statement and
requires no additional external theorem. No historical novelty
claim or realization theorem is inferred from it.

[^1]: [Coefficient-polynomiality136](conical-mismatch-coefficient-polynomiality-pass136.md), Sections 2--5.
[^2]: [Universal conical137](universal-conical-tangent-reduction-pass137.md), Sections 4--5.

