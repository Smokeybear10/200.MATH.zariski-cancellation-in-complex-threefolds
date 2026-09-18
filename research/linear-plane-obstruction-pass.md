# A slice action invisible to every affine-linear coordinate plane

There is a polynomial-coordinate copy of translation on affine four-space
whose invariant ring meets every affine-linear coordinate plane only in
the constants. Thus a search confined to linear coordinate changes cannot
always find even one invariant polynomial in two coordinates. This is an
obstruction to a proposed search strategy, not to cancellation: the kernel
in this example has an explicit polynomial basis.

## Statement and coordinate inverse

Start with \(B=\mathbb C[a,b,c,s]\) and \(E=\partial_s\). Introduce
the polynomial coordinates
\[
x_1=a+s^2,\qquad x_2=b+s^3,\qquad x_3=c+s^4,\qquad
x_4=s+x_1x_2.
\tag{1}
\]
Their polynomial inverse is
\[
s=x_4-x_1x_2,\qquad a=x_1-s^2,\qquad b=x_2-s^3,\qquad
c=x_3-s^4.
\tag{2}
\]
In the displayed frame the coefficient vector of \(E\) is
\[
\bigl(2s,\ 3s^2,\ 4s^3,\ 1+2x_2s+3x_1s^2\bigr).
\tag{3}
\]
It has slice \(s\), and its kernel is exactly \(\mathbb C[a,b,c]\).

**Proposition.** For any two affine-linear forms \(U,V\) in
\(x_1,x_2,x_3,x_4\) with linearly independent linear parts,
\[
\ker E\cap\mathbb C[U,V]=\mathbb C.
\tag{4}
\]
The quantifier in (4) is over all complex coefficients, not a rational
grid or a finite set of candidate planes.

## Proof

First suppose the span of the linear parts of \(U,V\) has no
\(x_4\)-component. Then \(\mathbb C[U,V]\) is a subalgebra of
\(\mathbb C[x_1,x_2,x_3]\). For any \(f\) in that larger algebra,
\[
E(f)=2s f_{x_1}+3s^2 f_{x_2}+4s^3 f_{x_3}.
\tag{5}
\]
The elements \(x_1,x_2,x_3,s\) are polynomial coordinates, by
(1) and (2). Comparing the three distinct powers of the independent
variable \(s\) shows that \(E(f)=0\) forces all three partial
derivatives to vanish. In characteristic zero \(f\) is constant.

Otherwise, an invertible affine change of generators of the same plane
puts its basis in the form
\[
U=x_4+\alpha x_1+\beta x_2+\gamma x_3+u_0,
\qquad V=l_1x_1+l_2x_2+l_3x_3+v_0,
\tag{6}
\]
where \((l_1,l_2,l_3)\ne(0,0,0)\). On the hypersurface \(s=0\),
which is \(x_4=x_1x_2\), their restrictions are
\[
U_0=x_1x_2+\alpha x_1+\beta x_2+\gamma x_3+u_0,
\qquad V_0=l_1x_1+l_2x_2+l_3x_3+v_0.
\tag{7}
\]
They are algebraically independent. Indeed, their Jacobian has the
three two-by-two minors
\[
\begin{aligned}
M_{12}&=(x_2+\alpha)l_2-(x_1+\beta)l_1,\\
M_{13}&=(x_2+\alpha)l_3-\gamma l_1,\\
M_{23}&=(x_1+\beta)l_3-\gamma l_2.
\end{aligned}
\tag{8}
\]
If all vanished identically, the coefficients of \(x_1,x_2\) in
\(M_{12}\) would give \(l_1=l_2=0\); the coefficient of \(x_2\)
in \(M_{13}\) would give \(l_3=0\), a contradiction. The
characteristic-zero Jacobian criterion gives the asserted independence.
Equivalently, substitution \(F\mapsto F(U_0,V_0)\) is injective.

Now let \(F(U,V)\) be invariant. Formula (3) gives
\[
E(U)\equiv1\pmod{s},\qquad E(V)\equiv0\pmod{s}.
\tag{9}
\]
Reduce the chain rule
\(0=F_U(U,V)E(U)+F_V(U,V)E(V)\) modulo \(s\). It yields
\(F_U(U_0,V_0)=0\), so injectivity forces \(F_U=0\).
Thus \(F\) depends only on \(V\). But
\[
E(V)=2l_1s+3l_2s^2+4l_3s^3\ne0.
\tag{10}
\]
The domain property now forces \(F_V=0\), and \(F\) is constant.
This proves (4), including arbitrary affine constants.

## Consequences and limits

For an LND, the existence of a nonconstant invariant in an actual
coordinate plane implies the existence of an invariant coordinate of
that plane. This is the published intersection criterion, not a new
result: see Freudenburg, *Algebraic Theory of Locally Nilpotent
Derivations*, second edition, Chapter 5 Appendix, Corollary 5.43
([primary source](https://doi.org/10.1007/978-3-662-55350-3_5)).
The projective-direction formulation follows from the known
quasi-extension lemma and Rentschler's theorem, as explained in
[the source audit](global-symmetry-bridge-literature.md).

Consequently (4) also excludes finding a projectable direction
\(E(U):E(V)\) over \(\mathbb C(U,V)\) in any affine-linear plane.
It does not exclude nonlinear planes: \(\mathbb C[a,s]\) is one,
and \(a\) is an invariant ambient coordinate. The explicit inverse
(2) already solves cancellation for this example.

The field also commutes with the constant translation
\(\partial_{x_3}\), since every coefficient in (3) is independent
of \(x_3\). Even a commuting coordinate partial therefore does not
force the required plane to be affine-linear in the displayed frame.
This does not refute recognition using nonlinear coordinates.

The same argument works with any three distinct integers
\(d_1,d_2,d_3\ge2\), replacing the first three powers of \(s\)
in (1) by \(s^{d_i}\). Distinctness gives the coefficient separation
and (10), and the lower bound two gives (9). The quadratic restriction
\(x_4=x_1x_2\) and its Jacobian argument are unchanged.

No novelty claim is made for this construction. Its purpose is to
exclude a precise universal search rule. The proof is algebraic;
[the exact checker](projective_plane_checks.py) verifies the displayed
identities and the symbolic-parameter Jacobian obstruction but is not
a formal proof assistant. The separate
[reconstruction](linear-plane-obstruction-audit.md) is a model audit,
not human expert review.
