# Constant formal factor difference is impossible in the actual chart

In the actual nonzero-coupling chart264, suppose the cubic surface
level is reducible. Its two monic factors cannot differ by a nonzero
formal constant in the coefficient field. This excludes the special
case that302 reduced to an affine projected line.

The proof combines two independently checked working arguments.
It does not exclude reducible surfaces with nonconstant factor
difference, even when their selected projected image is a line.

## 1. Actual normalization, not just a discriminant substitution

Retain the exact actual hypotheses of
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md),
including the sliced original ring, full initial kernel, selected
literal partial, exact coefficient field, and calibrated Jacobian.
Suppose

\[
H-h_0=(U+A)(U+B),\qquad B-A=\eta\in L^*.
\tag{1}
\]

The nonzero condition is necessary: both factors cannot vanish on
the selected line, since the evaluated first gradient is a unit ideal.
The degree-four discriminant coefficient forces \(m_t=m_s=0\).
Then the cubic coefficient gives
\(k=ms+\kappa t^2/2+bt+d\), with complex constants and m nonzero.

Sections3 and4 of302 supply an actual polynomial reframe
\(W_*=mW+\kappa Z/2+bY+dX^2\), its polynomial inverse, and the
exact transformed surface level. Their formal-level transport keeps
arbitrary n until it is constrained by the new discriminant.
Consequently, after this justified reframe and dropping the stars,

\[
k=s,\qquad n=\nu s+\nu^2t^2+b_1t+c_2,\qquad
\ell=-\nu^2s+\ell_0,
\quad \nu,b_1,c_2,\ell_0\in\mathbb C.
\tag{2}
\]

This is precisely302(17). The result requires its actual transport
argument. A change of coefficient variables alone would not suffice.

## 2. The full polynomial identity contradicts normality

The invariant-family identity in
[303, Section4](principal-paraboloid-double-cover-line-obstruction-pass303-working.md)
holds without any projection assumption. Apply it with
\(\alpha=2\nu^2\), \(\beta=b_1\), \(\delta=c_2\). Set

\[
Y_0=Y+b_1/2,\quad Z_0=Z-c_2,\quad W_0=W-\ell_0,
\quad V_0=W_0-(X-\nu)Z_0.
\]

These are actual complex shifts and a triangular polynomial shear;
\(X,Y_0,Z_0,V_0\) are independent polynomial coordinates of
\(\mathcal B\). The full-X identity303(16),(17) becomes

\[
Y_0^2+(X+\nu)V_0
  =(y+b_1/2+\nu^2t-\nu\sigma)^2.
\tag{3}
\]

The right-hand square root belongs to \(K\subset\operatorname{Frac}
\mathcal B\). Equation (3) is monic in that square root, making
it integral over the normal polynomial ring \(\mathcal B\).
Hence it would be a polynomial in the four independent coordinates
above. But the left side of (3) has exact degree one in V0, whereas
every nonzero polynomial square has even V0-degree. Contradiction.

Thus no actual frame with (1) exists. This exclusion uses the explicit
identity and normality only; it does not require the published
regular-kernel recognition theorem used for the nondegenerate part
of303's family lemma.

## 3. Boundary

The finite checks for302 reconstruct its arbitrary-n normalization
and surface-level transport. The checks for303 reconstruct the full
invariant and odd-degree degeneration. No new numerical test can
substitute for the normality and actual-coordinate argument above.

This is a scoped exclusion, not a counterexample to cancellation or
a proof of unrestricted cancellation. Other factor differences,
irreducible cubic levels, other initial kernels, and arbitrary
coordinate entry remain outside this argument. No historical novelty,
human-expert review, or formal proof-assistant verification is claimed.
