# A fixed good base direction removes one coefficient variable

A rational two-output symmetry whose coefficient lies in its
actual fixed coordinate plane has an additional restriction
when one fixed base partial is good and its first adjoint
lies in the other output's nonzero second-adjoint line.
Under these precise conditions, the coefficient is independent
of that fixed good coordinate.

The result below is a rational derivation identity. It does not
assert local nilpotence, a global slice, or recognition of an
original kernel.

## 1. Exact hypotheses

Let
\[
B=k[a,w,b,z],\qquad k=\mathbb C,\qquad K=\operatorname{Frac}B,
\qquad \delta\in\operatorname{Der}_k(K).
\]
The four generators are actual polynomial coordinates; their
ordinary partials extend to \(K\). Suppose
\[
v\in k(a,w),\qquad
S=\partial_z+v\partial_b,\qquad
[\delta,S]=0,\qquad \delta v=c\in k.
\tag{1}
\]
In particular \(S\) fixes the actual base coordinates \(a,w\).
Define
\[
D'=\operatorname{ad}_\delta^2\partial_b.
\]
Assume, as identities in \(\operatorname{Der}_k(K)\), that
\[
D'\ne0,\qquad
\operatorname{ad}_\delta^2\partial_a=0,\qquad
[\delta,\partial_a]=qD'
\quad\text{for some }q\in K.
\tag{2}
\]
Here “good” means the displayed second-adjoint identity.
No polynomiality or local nilpotence of \(\delta,D',S\)
on a localization is presumed. The coefficient \(q\) may
be rational.

**Lemma.** Under (1)--(2),
\[
\boxed{v\in k(w).}
\tag{3}
\]
The scalar \(c\) is allowed to be zero.

## 2. The full adjoint calculation

Since \(v\in k(a,w)\), one has \(\partial_bv=0\).
Also \(\partial_b(\delta v)=0\) and \(\delta^2v=0\),
because \(\delta v=c\in k\). Thus the full second-adjoint
formula gives
\[
D'v
=\delta^2(\partial_bv)-2\delta(\partial_b\delta v)
  +\partial_b(\delta^2v)=0.
\]
Put \(r=\partial_av\). Using (2), not differentiating
the coefficient \(q\), yields
\[
\delta r=\partial_a(\delta v)+[\delta,\partial_a]v
         =qD'v=0.
\tag{4}
\]

All four actual coordinate partials commute, so
\([\partial_a,S]=r\partial_b\).
The adjoint action \(\operatorname{ad}_\delta\) is a
derivation of the Lie bracket. Since \([\delta,S]=0\),
applying it twice gives
\[
\operatorname{ad}_\delta^2[\partial_a,S]
=[\operatorname{ad}_\delta^2\partial_a,S]=0.
\]
On the other hand, the coefficient product rule and (4) give
\[
\begin{aligned}
\operatorname{ad}_\delta^2(r\partial_b)
&=(\delta^2r)\partial_b+
  2(\delta r)[\delta,\partial_b]+rD'\\
&=rD'.
\end{aligned}
\tag{5}
\]
Consequently \(rD'=0\). A nonzero derivation of the field
\(K\) cannot be annihilated by a nonzero field scalar.
The hypothesis \(D'\ne0\) therefore implies
\(\partial_av=r=0\).

The constants of ordinary \(a\)-differentiation on
\(k(w)(a)\) are \(k(w)\). Explicitly, write a nonzero \(v\)
as a reduced quotient of polynomials in \(a\) over \(k(w)\).
The zero derivative makes each numerator and denominator
divide its own derivative. Degree in \(a\) then makes both
derivatives zero, and characteristic zero makes both
polynomials constant in \(a\). The case \(v=0\) is immediate.
This proves (3).

## 3. Scope

Only the actual commuting coordinate partials, rational
coefficient dependence in \(k(a,w)\), and the exact bracket
identities are used. In particular \(D'\) need not be a
polynomial LND, and no assertion about \(\delta q\) is
required.

The nonzero second-adjoint premise is essential to the scalar
cancellation in (5). The lemma alone does not decide whether
\(v\) is constant or polynomial in \(w\). Such conclusions
would require additional information about \(\delta w\).
Any original-kernel recognition endpoint is a separate
application with its own actual-coordinate and slice hypotheses.

The calculation is supplied in full and uses no new external
theorem, numerical suite, regression claim, or frozen-file
change.
