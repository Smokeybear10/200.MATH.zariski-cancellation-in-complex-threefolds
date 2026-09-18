# A relative Danielewski obstruction

For every \(b\in\mathbb C^*\) and \(n\ge2\), the two rings
\[
S_X=\mathbb C[f,q,r]/(f^nq-r^5-b^3),
\qquad
S_Y=\mathbb C[f,Q,\rho]/
\bigl(f^nQ-\rho^5-(1+bf)^5b^3\bigr)
\]
are not isomorphic as \(\mathbb C[f]\)-algebras. This follows from an exact
primary isomorphism restriction and a first-order calculation. It is a
relative obstruction, not a cancellation counterexample or a proof that a
kernel lacks an abstract polynomial presentation.

## Primary statement

P.-M. Poloni, *Classification(s) of Danielewski hypersurfaces*,
*Transformation Groups* **16** (2011), 579–597,
[DOI 10.1007/s00031-011-9146-5](https://link.springer.com/article/10.1007/s00031-011-9146-5).
The directly read primary source is
[arXiv:0912.3241v1, Corollary 3.3(1), printed page 4](https://arxiv.org/pdf/0912.3241),
with Definition 2.2, Theorem 3.2, and the corollary's proof.

For hypersurfaces \(x^{n_i}y=Q_i(x,z)\) over \(\mathbb C\), with
\(n_i\ge2\) and \(\deg Q_i(0,z)\ge2\), every isomorphism has pullbacks
\[
x\longmapsto a x,\qquad z\longmapsto\alpha z+\beta(x),
\quad a,\alpha\in\mathbb C^*,\quad\beta\in\mathbb C[x].
\]
The coefficient \(\alpha\) is a constant. This conclusion requires neither
standard form nor a simple-root hypothesis. For isomorphisms over
\(\mathbb C[x]\), one has \(a=1\). In the present application both special
polynomials are \(z^5+b^3\), so the required degree is five, and their roots
are also simple.

The source proves the restriction via the intrinsic LND kernels and
second degree modules. Consequently it concerns arbitrary algebraic
isomorphisms, not only isomorphisms that extend to the ambient affine space.

## Application: a self-contained first-order contradiction

Suppose \(\phi:S_Y\to S_X\) fixes \(f\). The primary restriction gives
\[
\phi(\rho)=\alpha r+\beta(f),\qquad\alpha\ne0.
\]
Write \(\beta(f)=\beta_0+\beta_1f\pmod{f^2}\). Since \(n\ge2\), the
relation in \(S_X/(f^2)\) is simply \(r^5=-b^3\); the variable \(q\)
remains free. The image of the defining relation of \(S_Y\) yields
\[
(\alpha r+\beta(f))^5+b^3(1+bf)^5=0
\quad\text{in }S_X/(f^2).
\]
Modulo \(f\), comparison using the basis \(1,r,r^2,r^3,r^4\) of
\(\mathbb C[r]/(r^5+b^3)\) gives
\[
\beta_0=0,\qquad\alpha^5=1.
\]
Indeed, the coefficient of \(r^4\) is \(5\alpha^4\beta_0\), and the
remaining constant term is \(b^3(1-\alpha^5)\).

The coefficient of \(f\) now gives
\[
5\alpha^4\beta_1r^4+5b^4=0
\quad\text{in }\mathbb C[r]/(r^5+b^3).
\]
The elements \(1\) and \(r^4\) are linearly independent. Thus this equality
would force \(b=0\), contrary to the premise. No such \(\phi\) exists.

The exponent restriction is sharp for these equations. When \(n=1\), the
map fixing \(f,r\) and sending
\[
Q\longmapsto q+
\frac{b^3((1+bf)^5-1)}{f}
\]
is a polynomial \(\mathbb C[f]\)-isomorphism from \(S_Y\) to \(S_X\).
For \(b=0\), the two displayed equations coincide for every \(n\).

## Exact invariant-kernel chart

The required chart can be established polynomially, including its
compatibility with specialization. Use the family and the exact chart in
[the all-image reconstruction](nonreduced-rank-three-images-pass17.md):
\[
R_h=\mathbb C[h,h^{-1},f,r,q]/(f^nq-r^5-h^3),
\qquad D_nr=f^nh,
\]
where \(R=\mathbb C[x,y,z]\). Put
\[
B=1+fh,\quad g=f^nh,\quad
U=(-1)^nh^{n-1},\quad V=\sum_{j=0}^{n-1}(-fh)^j.
\]
Then \(gU+BV=1\). For \(E=D_n+B\partial_t\), define
\[
\rho=Br-gt,\qquad s=Ur+Vt,\qquad
r=V\rho+gs,\quad t=-U\rho+Bs.
\]
This is an invertible matrix change over \(\mathbb C[f,h]\).
The following polynomial is invariant:
\[
\bar q=q-\frac{(V\rho+gs)^5-(V\rho)^5}{f^n}.
\]
The displayed quotient is polynomial because \(f^n\mid g\).
It eliminates every occurrence of \(s\) from the defining relation:
\[
f^n\bar q=V^5\rho^5+h^3.
\]
The same formulas have a polynomial inverse. Consequently
\[
R_h[t]\cong
\left(\mathbb C[h,h^{-1},f,\rho,\bar q]/
(f^n\bar q-V^5\rho^5-h^3)\right)[s],
\]
with \(E=\partial_s\). Thus the parenthesized ring is exactly
\((\ker E)_h\), not just a candidate subring.

Set
\[
W=\frac{1-(BV)^5}{f^n},\qquad
Q=B^5\bar q+W\rho^5.
\]
Again \(W\) is polynomial, since \(BV=1-gU\). The inverse is
\(\bar q=V^5Q+Wh^3\); the two defining relations verify both
compositions. This gives the exact presentation
\[
(\ker E)_h\cong
\mathbb C[h,h^{-1},f,\rho,Q]/
\bigl(f^nQ-\rho^5-B^5h^3\bigr).
\]
Specializing \(h=b\ne0\) produces precisely \(S_X\) and
\(S_Y\) above. A \(\mathbb C[f,h]\)-isomorphism between \(R\)
and \(\ker E\) would therefore produce the excluded
\(\mathbb C[f]\)-isomorphism. Hence no such relative isomorphism
exists for \(n\ge2\).

Nevertheless the [finite-jet coordinate construction](nonreduced-coordinate-lift-pass17.md)
proves that \(\ker E\) is abstractly a polynomial three-ring.
It changes the presentation of the invariant \(h\), which is exactly
what the relative obstruction requires. This is a sharp restriction on
the permissible coordinate construction, not a cancellation counterexample.
