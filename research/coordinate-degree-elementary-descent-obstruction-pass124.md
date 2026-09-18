# Coordinate-degree elementary descent obstruction, pass 124

## 1. Result and scope

Even for the translation derivation on a polynomial fourfold, an actual
polynomial coordinate frame can admit no strictly degree-decreasing elementary
replacement while lying arbitrarily far above the global minimum of the sum
of its derivation degrees. This obstructs a specific proposed universal-entry
algorithm: repeatedly lower that sum by replacing one coordinate with itself
plus a polynomial in the other coordinates.

It does not obstruct cancellation. The examples have an explicitly polynomial
kernel and an explicitly known adapted coordinate frame. Nor does it show
that an arbitrary sequence of degree-preserving elementary changes cannot
eventually reach a descending step. That stronger assertion is not proved here.

The remaining universal-entry gap is stated in
[the pass-123 synthesis](cubic-exclusion-frontier-pass123.md) and
[the global-entry audit](global-entry-audit-pass108.md).
The degree here is the actual \(E\)-degree of an ambient polynomial, not the
horizontal-adjoint minimum in
[pass 32](unrestricted-minimum-pass32.md), and not an intrinsic quotient
degree that can be substituted for it; compare
[the degree-scope note](coordinate-slice-degree-scope-pass58.md).

## 2. Actual coordinate frames and the allowed moves

Let \(B=\mathbb C[u,v,z,w]\), \(E=\partial_u\). For a nonzero polynomial \(f\),
write \(d_E(f)\) for its degree in \(u\), with coefficients in
\(\mathbb C[v,z,w]\). Equivalently it is the largest integer \(j\) with
\(E^j f\ne0\). For an ordered polynomial coordinate frame
\(\mathcal F=(F_1,F_2,F_3,F_4)\), put
\[
 H_E(\mathcal F)=\sum_{i=1}^4 d_E(F_i),\qquad
 F_i\longmapsto cF_i+
 f(F_1,\ldots,\widehat F_i,\ldots,F_4),
 \quad c\in\mathbb C^*.
 \tag{1}
\]
The second expression defines an elementary replacement, with the other
three coordinates fixed and with \(f\) an arbitrary polynomial over
\(\mathbb C\). Every such replacement is an actual polynomial automorphism:
its inverse subtracts \(f\) and divides by the nonzero complex constant \(c\).
Permutations and nonzero constant rescalings are also allowed, but do not
change \(H_E\).

The global minimum of \(H_E\) is \(1\). Indeed, the frame
\((u,v,z,w)\) attains \(1\); a frame of height \(0\) would put all four
polynomial generators in \(\ker E\), forcing \(E=0\), a contradiction.
This is a minimum over actual frames, not an assertion that a slice of an
arbitrary polynomial-ring derivation is a coordinate.

## 3. A family with complete polynomial inverses

For every integer \(m\ge1\), define
\[
 \Delta=zu+v^2,\qquad
 X=u-2v\Delta^m-z\Delta^{2m},\qquad
 Y=v+z\Delta^m,\qquad Z=z,\qquad W=w.
 \tag{2}
\]
Expansion gives \(ZX+Y^2=\Delta\). Consequently, if
\(\Delta_*=ZX+Y^2\), the inverse expressions are
\[
 u=X+2Y\Delta_*^m-Z\Delta_*^{2m},\qquad
 v=Y-Z\Delta_*^m,\qquad z=Z,\qquad w=W.
 \tag{3}
\]
These are inverse in both orders. In one order, substitute
\(\Delta_*=\Delta\) into (3) and cancel the terms in \(\Delta^m\) and
\(\Delta^{2m}\). In the other, the values given by (3) satisfy
\(zu+v^2=\Delta_*\), so (2) cancels back to \(X,Y,Z,W\).
Thus (2) is an actual polynomial coordinate frame on the whole fourfold,
with no localization or unproved inverse.

The case \(m=1\) is the standard Nagata construction. Its derivation
\(\delta=-2v\partial_u+z\partial_v\) fixes \(\Delta\); more generally (2)
is \(\exp(\Delta^m\delta)\) on the first three coordinates. This attribution
is only historical: the complete inverse needed here was just verified
directly. The standard \(m=1\) formula and the exponential-inverse convention
are recorded in Maubach and Poloni, *The Nagata automorphism is shifted
linearizable*, Section 1.2, printed pages 3–4
([primary preprint](https://publications.mfo.de/bitstream/handle/mfo/1129/OWP2008_09.pdf?isAllowed=y&sequence=1)).
No theorem on wildness, stable tameness, or shifted linearizability is used.

As polynomials in \(u\), their leading terms and degrees are
\[
 \begin{aligned}
 X&=-z^{2m+1}u^{2m}+\text{terms of smaller }u\text{-degree},\\
 Y&=z^{m+1}u^m+\text{terms of smaller }u\text{-degree},\\
 (d_E X,d_E Y,d_E Z,d_E W)&=(2m,m,0,0),\qquad
 H_E(X,Y,Z,W)=3m.
 \end{aligned}
 \tag{4}
\]
The leading coefficients are nonzero polynomials. Hence these heights are
unbounded even though the global minimum is always \(1\).

## 4. No strictly decreasing elementary replacement

First consider replacing \(X\). Write the added polynomial uniquely as
\(f(Y,Z,W)=\sum_{j=0}^k a_j(Z,W)Y^j\), with \(a_k\ne0\) unless
\(f=0\). Since \(Z,W\) are \(E\)-invariant and
\(\mathbb C[z,w]\) is a domain, a nonzero term of largest \(Y\)-degree
has a nonzero leading coefficient in \(u\). Thus its \(E\)-degree is \(km\).
Different \(j\)'s have different \(E\)-degrees, so they cannot cancel
one another's top terms.

If \(k>2\), \(cX+f\) has degree \(km>2m\). If \(k<2\), it retains
degree \(2m\). If \(k=2\), lowering the degree requires
\[
 -c z^{2m+1}+a_2(z,w)z^{2m+2}=0,
 \qquad\text{equivalently}\qquad z\,a_2(z,w)=c.
 \tag{5}
\]
The last equality is impossible in \(\mathbb C[z,w]\), as evaluation
at \(z=0\) shows. Therefore an elementary replacement of \(X\) never
lowers its \(E\)-degree.

Next consider replacing \(Y\). A polynomial
\(f(X,Z,W)\) of positive \(X\)-degree \(k\) has \(E\)-degree exactly
\(2mk\), by the same leading-coefficient argument. That is strictly
larger than \(m=d_E(Y)\), and cannot cancel the leading term of \(cY\).
If its \(X\)-degree is zero, it is invariant and again cannot cancel that
term. Therefore a replacement of \(Y\) cannot lower its degree.

Finally, \(Z\) and \(W\) have degree \(0\), the smallest possible degree
of a nonzero polynomial. An elementary replacement is still a nonconstant
coordinate, so neither can be replaced by the zero polynomial or by a
nonzero constant. Their degrees cannot decrease.

Only one coordinate changes in an elementary replacement. The preceding
four cases prove that no such replacement lowers \(H_E\).
Permutations or constant rescalings before the replacement merely relabel
these cases or replace \(c\) and the polynomial coefficients by other
allowed coefficients. They do not provide a descending step.

## 5. The exact failed leading-term implication

The leading \(E\)-forms are algebraically dependent:
\[
 Z\,\operatorname{in}_E(X)
   +\operatorname{in}_E(Y)^2=0,\qquad
 ZX+Y^2=\Delta,\qquad d_E(\Delta)=1.
 \tag{6}
\]
Thus the leading cancellation itself is genuine and produces a polynomial
of lower \(E\)-degree. But it does not produce an elementary coordinate
replacement. The map
\((X,Y,Z,W)\mapsto(ZX+Y^2,Y,Z,W)\)
has Jacobian determinant \(Z\), a nonunit. If it had a polynomial inverse,
the chain rule would make this determinant a unit, which is impossible.
Equivalently, solving for \(X\) while fixing \(Y,Z,W\) requires division
by \(Z\).

For \(m=1\), the hidden invariant
\(v=Y-Z(ZX+Y^2)\) also shows why a longer plateau argument is delicate:
the elementary replacement \(W\mapsto W+v\) preserves its degree \(0\),
but the two displayed invariant slots are no longer simply obtained by
an automorphism of the old ring \(\mathbb C[Z,W]\). The one-step theorem
does not treat such sequences as if that ring remained fixed.

## 6. Consequence for the next entry argument

A well-ordering argument supplies a globally minimizing actual frame, but
does not show how a given frame reaches one by strictly decreasing elementary
moves. The examples above rule out that latter universal descent claim,
even with arbitrarily large starting height and with the entire polynomial
inverse already known.

A viable minimizing-frame argument must instead prove a property of true
global minimizers, allow and control non-decreasing intermediate moves, or
supply a different class of actual coordinate changes. Algebraic dependence
of the leading \(E\)-forms by itself does not certify an invertible change.
Nothing here proves that an arbitrary sliced derivation enters the
constant-acceleration class recognized in pass 123.

The companion [six-shear bypass](nagata-stabilized-degree-bypass-pass124.md)
does reach \((u,v,z,w)\) for every frame (2), with a temporary degree sum
\(4m\). That is an explicit upper bound for one path, not a proof that every
path needs an increase. Its finite checker supports the exact identities
without certifying the arbitrary-polynomial one-step obstruction proved here.

The proof is exact for every \(m\ge1\). Its primary-source check was confined
to the complete selected Section 1.2, visually read on printed pages 3–4;
the displayed inverse and all degree arguments above were independently
reconstructed. No broad source theorem or numerical test is a prerequisite.
