# A second-image basepoint lies on the singular full plinth divisor

In the actual degree-two residual, the finite obstruction cannot occur
at a smooth point of the full primitive plinth divisor. This uses the
topology inherited from the polynomial cylinder, not faithful flatness
alone. More precisely, at an obstruction point the plinth belongs to
the product of the maximal ideal with the local obstruction ideal.

## 1. Exact local hypotheses

Use the complete hypotheses of the
[second-image bundle theorem](second-image-vector-bundle-pass47.md).
At a closed point of the invariant plane, put
\[
R=C_{\mathfrak m},\qquad \mathfrak n=\mathfrak mR,
\qquad \mathcal A=A\otimes_C R.
\tag{1}
\]
Suppose \(JR\ne R\). The proved local basis gives
\[
(F_2)_R=R\oplus Rz\oplus Rw,\quad r=az+bw,
\quad JR=(a,b),\quad a,b\in\mathfrak n,
\tag{2}
\]
\[
Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,
\quad p=aB_1+bB_2,\quad \epsilon\in R^*.
\tag{3}
\]
Here the harmless invariant translation of the actual minimal slice
has already been made. The exact conic subalgebra is
\[
H=R[z,w]\simeq R[Z,W]/(F),
\quad F=\epsilon(aZ+bW)^2-2B_2Z+2B_1W-Q,
\quad Q\in R.
\tag{4}
\]
It agrees with \(\mathcal A\) at every height-one prime of \(R\).
The ring \(\mathcal A\), but not automatically \(H\), is
faithfully flat over \(R\).

The additional geometric input is the
[intrinsic pointwise plinth criterion](intrinsic-pointwise-plinth-pass47.md):
in the actual smooth contractible threefold, a full reduced single
affine-line quotient fiber with nonzero induced translation is outside
the primitive plinth support. That note verifies the extension of the
earlier peripheral-cycle proof to the unknown cylinder factor.

## 2. Two elementary flatness facts

First, if the coefficients of a polynomial \(f\in R[X_1,\ldots,X_d]\)
generate the unit ideal, multiplication by \(f\) is injective on
\(M[X_1,\ldots,X_d]\) for every \(R\)-module \(M\).
Here is a direct argument rather than a monic-polynomial assumption.
For one variable, choose a nonzero annihilated polynomial \(g\)
of minimum degree. The highest coefficient of \(f\) kills the
highest coefficient of \(g\); multiplying \(g\) by that coefficient
therefore gives an annihilated polynomial of smaller degree, hence
zero. Remove that term of \(f\) and descend through its coefficients.
Each kills \(g\), contradicting their unit ideal. For several variables,
a sufficiently separated Kronecker substitution into one variable
preserves the coefficients of \(f\) and the nonzero polynomial \(g\),
and reduces to that argument.

Tensor the free resolution given by multiplication by \(f\).
The preceding injectivity for every \(M\) proves
\[
R[X_1,\ldots,X_d]/(f)\text{ is flat over }R.
\tag{5}
\]
Unit ideal of coefficients is stronger than absence of a common
irreducible factor. These two meanings of primitive must not be
interchanged in a two-dimensional local ring.

Second, if \(R\) is a UFD and \(M\) is a flat \(R\)-module,
then, inside \(M\otimes_R L\),
\[
M=\bigcap_{\operatorname{ht}\mathfrak q=1}M_{\mathfrak q},
\qquad L=\operatorname{Frac}R.
\tag{6}
\]
To prove this, write an element on the right as \(h/c\).
For every prime power \(\pi^e\) dividing \(c\), membership at
\((\pi)\) gives some \(s\notin(\pi)\) with
\(sh\in\pi^eM\). Multiplication by \(s\) is injective on
\(R/\pi^eR\), and flatness preserves the injection, so
\(h\in\pi^eM\). Flatness also preserves finite intersections
of ideals after tensoring their defining short exact sequences.
The intersection of these prime-power ideals in a UFD is \(cR\).
Thus \(h\in cM\), which proves (6). Flatness already makes
\(M\) torsion free, so the generic embedding used here is valid.

## 3. A unit derivative coefficient would give the whole affine-line fiber

Suppose one of \(B_1,B_2\) is a unit of the local ring \(R\).
Its associated linear coefficient in (4) is a unit. Therefore the
coefficients of \(F\) generate the unit ideal and (5) makes
\(H\) flat. By (6), its embedded height-one intersection is \(H\).
Since \(H\subset\mathcal A\) and they agree at every such
localization, every member of \(\mathcal A\) belongs to \(H\).
Consequently
\[
\mathcal A=H.
\tag{7}
\]
This is the missing generation argument in this case. It does not
apply flatness of \(\mathcal A\) to its subalgebra without proof.

Reducing (4) modulo \(\mathfrak n\), the quadratic coefficients
vanish by (2). The remaining nonconstant linear relation gives
\[
\mathcal A/\mathfrak n\mathcal A
\simeq\mathbb C[Z,W]/(-2\bar B_2Z+2\bar B_1W-\bar Q)
\simeq\mathbb C^{[1]}.
\tag{8}
\]
This is the full scheme-theoretic fiber, not its reduction alone.
The induced derivation sends \(Z,W\) to
\(\bar B_1,\bar B_2\), respectively. It is a nonzero tangent
translation on the line. The intrinsic pointwise criterion now says
that \(p\notin\mathfrak m\), whereas (2)--(3) give
\(p\in\mathfrak n\). This is a contradiction.

Thus every actual second-image basepoint satisfies
\[
B_1,B_2\in\mathfrak n,
\qquad p\in\mathfrak n\,JR\subseteq\mathfrak n^2.
\tag{9}
\]
In particular the point is singular on the hypersurface defined by
the full polynomial \(p\). In plane coordinates \(U,V\),
\[
\operatorname{Supp}(C/J)
\subseteq V(p,\partial_U p,\partial_V p).
\tag{10}
\]
Equation (9) is stronger than this set-theoretic containment. No
global containment of \((p,\partial_U p,\partial_V p)\) in \(J\)
is asserted.

## 4. The remaining conic degeneration

The constant \(Q\) in (4) belongs to \(\mathfrak n\).
Indeed (2), (9) and the actual equality defining \(Q\) put it
in \(\mathfrak n\mathcal A\); faithful-flat contraction puts
it in \(\mathfrak n\). Hence the conic subalgebra has
\[
H/\mathfrak nH\simeq\mathbb C[Z,W],
\qquad D((F_2)_R)\subseteq\mathfrak n(F_2)_R.
\tag{11}
\]
This is not a contradiction to the one-dimensional full quotient
fiber. The map from this two-variable polynomial ring into
\(\mathcal A/\mathfrak n\mathcal A\) need not be injective
or surjective. Higher degree elements of \(\mathcal A\) may
change the fiber. Showing that they cannot do so requires another
argument using the actual frame or global topology.

In particular, if \(p\) is squarefree and its zero scheme is smooth,
the right side of (10) is empty, and \(J=C\). This proves the
global quadratic presentation in that case. Recognition of such
a presentation as a polynomial ring is treated separately; it is
not a consequence of (10) alone.

The full polynomial matters: \(p=U^n\), \(n>1\), is singular
along its entire zero set even though its reduced support is a
smooth line. Neither (9) nor (10) excludes those points.

## Attribution and limits

The conic data and vector-bundle section are inherited from the
linked new algebraic lemma. The topological input is the explicit
scope extension of the existing peripheral-cycle argument, ultimately
based on Kaliman's published quotient geometry. Equations (5)--(6)
are elementary module arguments written in full. The conclusion
removes smooth points of the full plinth divisor, not all points of
the obstruction, not the remaining moving-frame branches, and not
the unrestricted cancellation conjecture. No historical novelty,
human review or proof-assistant verification is asserted.
