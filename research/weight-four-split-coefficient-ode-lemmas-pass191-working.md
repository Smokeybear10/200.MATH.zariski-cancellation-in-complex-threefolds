# Two coefficient lemmas for the next split quartic form

Status: working standalone algebraic-function lemmas for a prospective
application. This note does not prove that every actual split-form
chart reaches the coefficient equations below. It is not recognition
of that form or a solution to cancellation. It is outside the190 packet.

The remaining one-dimensional split coefficient form is
\(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4\).
On the selected coefficient chart its leading ratio is
\[
q(t)=-t^3-t^{-1},\qquad d(t)=q'''(t)/6=t^{-4}-1.
\tag{1}
\]
The next zero-R investigation will have to derive its own projection
and coefficient-cover reductions. The following two lemmas address
equations that occur in the analogous cover calculation. Their
proofs do not assume that the coefficient field is rational.

Throughout, \(K/\mathbb C(t)\) is a finite field extension, equipped
with the unique extension of \(d/dt\). Its constants are
\(\mathbb C\). All primes below mean this exact derivative.

## 1. Every algebraic solution of the linear-slope equation is proportional to t

**Lemma.** For \(d=t^{-4}-1\), an element \(b\in K\) satisfies
\[
10d b''+5d'b'+d''b=0
\tag{2}
\]
if and only if \(b=\lambda t\), with \(\lambda\in\mathbb C\).

The converse follows by substitution, since \(5d'+td''=0\).
For the forward implication put \(f=b/t\) and \(j=f'\).
Using \(d'=-4t^{-5}\) and \(d''=20t^{-6}\), the entire left side
of (2), after substituting \(b=tf\), is
\[
10dt f''-20f'.
\]
Thus
\[
dt j'=2j.
\tag{3}
\]
If \(j=0\), the constant field proves the result.
Otherwise
\[
\frac{j'}j=\frac{2t^3}{1-t^4},\qquad
\big(j^2(1-t^4)\big)'=0.
\tag{4}
\]
Let \(v^2=1-t^4\) in a finite algebraic extension \(K'\) of \(K\).
Since the constants of \(K'\) are still \(\mathbb C\), (4) gives
\[
jv=\mu\in\mathbb C^*,\qquad df=\mu\,\frac{dt}{v}.
\tag{5}
\]

Consider the nonsingular projective curve with function field
\(\mathbb C(t,v)\). The differential \(\omega=dt/v\) is nonzero
and regular everywhere, as can be checked directly:

- At a finite point where \(v\ne0\), \(t\) is an unramified
  local parameter, and \(dt/v\) is regular.
- At a root \(\xi\) of \(1-t^4\), one has \(\xi\ne0\), and \(v\)
  is a local parameter. Differentiating the equation gives
  \(dt/v=-dv/(2t^3)\), again regular.
- At infinity put \(s=1/t\) and \(V=v/t^2\). Then
  \(V^2=s^4-1\), so \(V(0)=\pm i\) is a unit, and
  \(dt/v=-ds/V\) is regular at both points.

The projective curve of \(K'\) maps finitely to that curve.
The pullback of a regular differential is regular; in local
parameters its order changes from \(m\ge0\) to
\(em+(e-1)\ge0\), since the characteristic is zero. The pullback
of \(\omega\) is nonzero, because the field extension is separable.
Thus (5) makes \(df\) a nonzero regular differential on the
projective curve of \(K'\).

This is impossible for a rational function \(f\). If \(f\) has a
pole of order \(m>0\), its differential has a pole of order \(m+1\)
in characteristic zero. If it has no poles, it is a global regular
function on a projective integral complex curve, hence is constant.
In either case its differential cannot be nonzero and everywhere
regular. Therefore \(j=0\), proving the lemma.

This argument excludes an algebraic primitive of the nonzero regular
differential. It does not rely on a guessed list of elementary
solutions or on numerical integration.

## 2. A quadratic-cover coefficient creates a pole of order at least nine

**Lemma.** Suppose \(a\in K^*\) satisfies
\[
2da'+ad'=0,\qquad
\gamma=\frac{a'''}{18d}.
\tag{6}
\]
Then \(\gamma\) is nonconstant and
\[
[K:\mathbb C(\gamma)]\ge9.
\tag{7}
\]

Equation (6) gives \(a^2d=\kappa\in\mathbb C^*\).
Choose a point of the projective curve of \(K\) above any root
\(\xi\) of \(1-t^4\). The map to the \(t\)-line is finite and
surjective, so such a point exists. Let \(e\) be the order of
\(t-\xi\) at that point. Since \(d\) has a simple zero at \(\xi\),
\[
\operatorname{ord}(d)=e,\qquad
\operatorname{ord}(a)=-e/2.
\tag{8}
\]
In particular \(e\) is a positive even integer.

In a completed local field, choose a uniformizer so that
\(t-\xi=s^e\). This is possible by extracting an \(e\)-th root
of a unit in characteristic zero with residue field \(\mathbb C\).
The equation \(a^2d=\kappa\) gives a nonzero leading term
\(A(t-\xi)^{-1/2}\). Its third \(t\)-derivative has nonzero
leading coefficient
\[
A(-1/2)(-3/2)(-5/2)
\]
and exponent \(-7/2\). Division by the simple zero of \(d\)
therefore yields
\[
\operatorname{ord}(\gamma)=-9e/2\le-9.
\tag{9}
\]
Consequently \(\gamma\) is nonconstant. The degree of its pole
divisor is at least nine, so the degree of the associated
function-field extension is at least nine. This proves (7).
No assumption \(K=\mathbb C(\gamma)\) has been made.

The projective model and morphism facts used here are supplied by
[Stacks Theorem 53.2.6](https://stacks.math.columbia.edu/tag/0BY1).
Pole degree equals the degree of the map to the projective line by
[Stacks Lemma 33.44.11](https://stacks.math.columbia.edu/tag/0AYZ),
applied to the point at infinity; the function-field definition is
[Stacks Definition 29.52.8](https://stacks.math.columbia.edu/tag/02NY).
The local pole-order calculation (8)--(9) is explicit above.

## 3. A precise conditional consequence for an actual-field-return attempt

Let \(y,z\) be independent over \(K\), and suppose an attempted
quadratic-cover reduction produces
\[
w=\gamma z^3+\sum_{i=0}^2 c_i(y)z^i,\qquad c_i(y)\in K[y],
\qquad K(y,z)=\mathbb C(y,z,w),
\tag{10}
\]
with \(\gamma\) as in (6). This is impossible.

Indeed, at a pole of \(\gamma\), the valuation of the polynomial
in \(z\) is the minimum of the coefficient valuations, after
extending the constants by \(y,z\). The independent monomials in
\(z\) prevent cancellation of the leading residues. Thus the pole
divisor of \(w\), viewed on the coefficient curve over
\(\mathbb C(y,z)\), contains that of \(\gamma\).
Its degree is at least nine, whereas the field equality in (10)
would make its degree one.
This is the polynomial-pencil degree argument used in
[cover-collapse189](weight-four-absent-zero-r-cover-collapse-pass189-working.md),
now with a local pole obstruction instead of a rational-coordinate
valuation contradiction.

If a separate actual-chart proof supplies (2) for a nonzero
linear-cover slope, the first lemma makes that slope
\(\lambda t\), with \(\lambda\in\mathbb C^*\).
It does not make the slope constant. That distinction matters:
in an original-coordinate lift, a contribution
\(\lambda tX^2+\lambda yX\) combines into \(\lambda XY\) because
\(Y=y+tX\). It must not be discarded as a failed constant-slope case.

Remaining work: derive the whole-line graph alternatives and
coefficient-cover equations for the actual split form, including
constant projection and the nonzero-R branch. Neither lemma
supplies those missing hypotheses. No split-form coordinate
recognition, full cancellation result, formal verification,
expert review, or novelty claim is made here.

