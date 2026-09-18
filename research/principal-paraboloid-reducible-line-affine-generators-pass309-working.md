# Every intrinsic generator is affine in the reducible projected-line case

Retain the actual reducible-surface hypotheses of
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md),
and suppose its projected equation G has degree one. Then

\[
\boxed{\max(\deg_v y,\deg_v\sigma,\deg_v\theta)\le1.}
\tag{1}
\]

This improves302's general degree-two bound in this case. It does
not require the formal factor difference to be constant, which is
excluded in the actual chart by308.

## Proof

The exact factor and return statements302 give

\[
H-h_0=(U+A)(U+B),\quad A,B\in L[P,V],\quad
\deg A,\deg B\le2,\quad\deg(AB)\le3,
\]

\[
O=L[v]=L[\sigma,\theta],\qquad
\max(\deg_v\sigma,\deg_v\theta)=\deg G=1.
\tag{2}
\]

Relabel so \(U+A\) vanishes on the actual curve. The other
evaluated factor is a unit because it divides every component
of the evaluated first gradient. Thus

\[
y=-A(\sigma,\theta),\qquad
B(\sigma,\theta)-A(\sigma,\theta)=\eta\in L^*.
\tag{3}
\]

At least one of A and B has degree at most one. If both were
nonzero quadratic polynomials, their product over the domain
\(L[P,V]\) would have degree four, contradicting (2)'s surface
degree bound. If one is zero, the assertion is immediate.

The evaluation of this affine factor at the two affine functions
in (2) has v-degree at most one. Equation (3) shows that the other
factor's evaluation differs from it by a coefficient-field constant,
so it also has degree at most one. In particular y is affine.
This proves (1), regardless of which formal factor has higher degree.

## Scope

The statement is about polynomial degrees over the exact field L.
It does not say that y, sigma or theta is an ambient coordinate,
and does not convert an auxiliary derivation into a globally sliced
one. No bound on the coefficient functions in t,s is supplied.

The projected-line recognition problem remains open here. The
argument uses only the fully read302 factor-unit and whole-return
statements and the degree of a product in a polynomial domain.
No separate finite checker, historical novelty, expert review or
formal proof-assistant certification is asserted.
