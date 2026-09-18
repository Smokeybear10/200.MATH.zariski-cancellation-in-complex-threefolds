# Finite reconstruction of the canonical rescaling obstruction

The canonical rescaling criterion in
[the radical-modification note](radical-modification-attack-pass18.md)
survives a separate reconstruction. The proof below uses only finite
polynomials and a Vandermonde matrix. It removes completion and formal
logarithms from the necessity argument, without weakening its scope.
It is not a proof that the modified ring is nonpolynomial.

## 1. Hypotheses and local data

Let \(R=\mathbb C^{[3]}\), let \(D\ne0\) be primitive and locally
nilpotent, let \(C=\ker D\), and choose a minimal local slice
\(Dr=p\), so \(P_D=pC\). Let \(V\ne0\), assume
\((p,V)C=C\), and let
\(\lambda\in C_V^*\) be 1 modulo the radical of \(pC_V\).
Suppose the \(C_{pV}\)-automorphism
\(r\mapsto\lambda r\) of \(R_{pV}=C_{pV}[r]\) maps
\(R_V\) into itself.

Fix a prime factor \(f\) of \(p\), with multiplicity \(n\).
It is prime in \(R\) by factorial closure. In the DVR
\(O=R_{(f)}\), write \(v=v_f\). Minimality gives
\(v(r)=0\), since \(f\mid r\) would imply
\(p/f=D(r/f)\in pC\). Primitivity supplies a coordinate
\(a\) with \(v(Da)=0\). All nonzero rational numbers are
units of \(O\).

Assume \(q=\lambda-1\ne0\), and suppose
\(k=v(q)<n\). The radical hypothesis gives \(k\ge1\).
Let \(d\ge1\) be the \(D\)-degree of \(a\), and put
\(N=nd\).

## 2. Replace the infinite series by one polynomial

Use the polynomial
\[
c(T)=\sum_{\ell=1}^N\binom{T}{\ell}q^\ell\in O[T].
\tag{1}
\]
For every nonnegative integer \(m\), the ordinary finite binomial
theorem gives
\[
c(m)-(\lambda^m-1)\in f^{N+1}O.
\tag{2}
\]
If \(m\le N\), the equality is exact. Otherwise, every omitted
term has a factor \(q^{N+1}\), of valuation at least \(N+1\).
There is no analytic or infinite-series evaluation here.

Define the finite polynomial over \(\operatorname{Frac}(O)\)
\[
H(T)=\sum_{j=0}^d
\frac{r^jD^j(a)}{j!p^j}\,c(T)^j.
\tag{3}
\]
On the local-slice ring, the \(m\)-th rescaling iterate evaluates
the same expression with \(c(m)\) replaced by \(\lambda^m-1\).
The coefficient of that power has valuation at least \(-nj\).
By (2), the difference of the two evaluations is integral: a
difference of \(j\)-th powers has the same \(f^{N+1}\)
factor, and \(N+1-nj\ge1\). Every rescaling iterate is
integral by the assumed endomorphism property. Hence
\(H(m)\in O\) for every nonnegative integer \(m\).

Evaluate \(H\) at the integers \(0,1,\ldots,\deg H\).
Their Vandermonde determinant is a nonzero integer, so its inverse
matrix has entries in \(O\). All coefficients of \(H\)
are therefore in \(O\). This inference uses finitely many exact
evaluations, not an assumption about pointwise limits.

But \(c(0)=0\), and
\[
c'(0)=\sum_{\ell=1}^N
\frac{(-1)^{\ell-1}}{\ell}q^\ell
\]
has valuation exactly \(k\): the first term has that valuation
and every later term has strictly larger valuation. Thus
\[
H'(0)=\frac{rDa}{p}c'(0),\qquad v(H'(0))=k-n<0,
\tag{4}
\]
contradicting integrality of the coefficients. This proves that
\(v_f(\lambda-1)\ge v_f(p)\) at every plinth factor.

## 3. Conclusion and boundary

Unique factorization in \(C_V\) now gives
\(\lambda-1\in pC_V\). Conversely that divisibility makes
the finite flow with time \(((\lambda-1)/p)r\) polynomial
over \(R_V\); the corresponding formula for \(\lambda^{-1}\)
is its inverse. Thus endomorphism extendability, automorphism
extendability and full-plinth congruence are equivalent under the
radical-congruence hypothesis.

The argument depends on primitivity, minimality, preservation of
the original invariant ring, and the specified pure rescaling of
the local slice. It does not rule out another relative isomorphism
with an affine shift, or an abstract coordinate change that moves
the invariant-plane embedding. Those are different statements.

The accompanying
[exact controls](rescaling_curve_controls_pass18.py)
check the finite binomial derivative, Vandermonde determinants,
the explicit pole obstruction, and the separate nodal-curve
counterexample. They do not prove the all-parameter valuation argument;
that argument is the finite reconstruction above.
