# Independent audit of separable sums with a binomial remainder

The proposed equivalence is valid over \(\mathbb C\). Let
\[
F(s,x,y,z)=h(s)+G(x,y,z),\qquad
G=f(x,y)z^q+g(x,y),
\]
with \(\deg h=N\geq2\), \(q\geq1\), and \(f\ne0\). Then
\[
\boxed{
F\text{ is stable}\quad\Longleftrightarrow\quad
G\text{ is a coordinate of }\mathbb C[x,y,z]
\quad\Longleftrightarrow\quad
F\text{ is a coordinate of }\mathbb C[s,x,y,z].
}
\tag{1}
\]
Here “stable” means a stable coordinate after finitely many polynomial
variables are adjoined. An original LND slice is therefore included.
There is no degree bound on \(f\), \(g\), or \(h\), beyond \(N\geq2\).

The audit found no gap in the main implication. The points requiring
explicit treatment are integral homology, potentially disconnected
general fibers, passage from a rectified surface to its defining
polynomial, and the constant cases omitted from the proof of the
surface theorem. They are addressed below. This is a deduction from
published theorems, without an originality claim.

## 1. The global join theorem has the required scope

For arbitrary complex polynomial maps in disjoint sets of variables,
Némethi's global sum theorem identifies the general fiber of their sum
up to homotopy with the join of their general fibers. A direct primary
statement is Theorem 2.4 of *Global Sebastiani--Thom theorem for polynomial
maps*; Corollary 2.5 records the resulting homology formula and explicitly
allows disconnected fibers.[^global]

The separately cited Compositio paper also supplies the result: in
Theorem G1 take the outer polynomial \(p(c,d)=c+d\). Example 3.4(a)
explicitly verifies its hypotheses and gives the join. There is no
additional tameness or isolated-critical-point requirement in this
sum case.[^generalized]

Let \(Y\) be a general fiber of \(G\). Since \(f\ne0\) and \(q\geq1\),
the polynomial \(G\) is nonconstant and \(Y\) is nonempty. A general
fiber of \(h\) is a discrete space \(D_N\) consisting of \(N\) points.
Thus a general fiber \(X\) of \(F\) satisfies
\[
X\simeq D_N*Y.
\tag{2}
\]
These are general fibers; no conclusion about an exceptional fiber
of either summand is being imported from the join theorem.

## 2. Integral join homology includes connectedness and torsion

For every nonempty space \(Y\) having the homotopy type of a CW complex,
the integral join formula with \(D_N\) gives
\[
\widetilde H_{j+1}(D_N*Y;\mathbb Z)
\cong
\widetilde H_j(Y;\mathbb Z)^{\oplus(N-1)}
\qquad(j\geq0).
\tag{3}
\]
One can calculate this using augmented chains: the reduced chains of
the discrete set have homology \(\mathbb Z^{N-1}\) concentrated in
degree zero, and the join suspends the tensor product. The tensor factor
is free, so the integral Künneth calculation has no Tor terms. This
argument requires neither connectedness nor torsion-free homology of
\(Y\). Smooth affine fibers have the needed CW homotopy type.

If \(F\) is stable, then \(X\times\mathbb A^m\cong\mathbb A^{m+3}\)
for some \(m\), so \(X\) is contractible. Combining (2)--(3), and using
\(N-1\geq1\), gives
\[
\widetilde H_j(Y;\mathbb Z)=0\qquad(j\geq0).
\tag{4}
\]
In degree zero this says \(Y\) is connected. In positive degrees it
annihilates torsion as well as free homology. There is no replacement
of rational acyclicity by integral acyclicity in this step.

Contractibility of the join alone would not imply contractibility of
\(Y\). Only (4), the weaker assertion actually needed by the surface
theorem, is concluded.

## 3. Smoothness, irreducibility, and the defining equation

A stable coordinate has no critical point on its original affine
space: if all its original partial derivatives vanished at a point,
then its differential would also vanish after adding variables,
contradicting its being a coordinate there.

Since \(N\geq2\), choose \(s_0\in\mathbb C\) with \(h'(s_0)=0\).
If \(G\) had a critical point \(p\), then
\[
dF_{(s_0,p)}=(h'(s_0),dG_p)=0,
\]
a contradiction. Therefore \(G\) is a submersion. In particular, a
general fiber \(Y=V(G-\lambda)\) is a smooth, reduced surface. Its
connectedness from (4) makes it irreducible, since distinct irreducible
components of a smooth variety are disjoint open-and-closed components.

Kaliman and Zaidenberg's Theorem 7.2 applies to an irreducible smooth
surface
\[
V(f(x,y)z^q+g(x,y)-\lambda)\subset\mathbb A^3,
\qquad q\geq1.
\]
It equates integral acyclicity with rectifiability of the embedding,
and, for \(q>1\), also gives simultaneous rectification of
\((f,g-\lambda)\). Its statement is explicitly integral; the paper
provides a rationally acyclic counterexample to an integral-free
replacement.[^surface]

Thus (4) makes \(Y\) a rectifiable plane. Since \(G-\lambda\) defines
the smooth irreducible fiber scheme, its principal ideal is the prime
ideal of that plane. An ambient automorphism rectifying the plane
therefore takes \(G-\lambda\) to a nonzero scalar times a coordinate
function. A higher power cannot occur because the fiber equation is
reduced. It follows that \(G\) is a coordinate, not merely that its
quotient ring is an abstract polynomial ring.

The preceding invocation treats the case of nonconstant \(f\) and
\(g\). The statement of Theorem 7.2 also permits constants, but the
paragraph preceding it says those cases are easy and omits them from
the subsequent proof. The following separate checks cover them.

## 4. Constant and boundary cases

If \(q=1\) and \(f=c\ne0\) is constant, then
\(G=cz+g(x,y)\) is a coordinate directly, with \(x,y\) as companions.
This covers constant \(g\) as well.

Suppose \(q\geq2\) and \(f=c\ne0\) is constant. Under stability,
Section 3 implies that \(g\) has no critical point, since at \(z=0\)
the gradient of \(G\) is \((g_x,g_y,0)\). In particular, \(g\) is
nonconstant. Let \(C\) be a general plane curve fiber of \(g\). Apply
the same global sum theorem to
\[
G=cz^q+g(x,y).
\]
The general fiber \(Y\) is homotopy equivalent to \(D_q*C\).
Equation (4) and the integral formula (3), with \(q\) in place of
\(N\), make \(C\) integrally acyclic. It is a smooth connected affine
curve, hence an affine line. The plane-line rectification theorem makes
\(g\) a coordinate of \(\mathbb C[x,y]\). Consequently
\(G=cz^q+g\) is a coordinate by an explicit triangular shear. This
also proves the required simultaneous-pair assertion when \(f\)
is constant.

If \(g=b\) is constant and \(q\geq2\), every point with \(z=0\) is
critical for \(G\), so stability is impossible. If \(g=b\), \(q=1\),
and \(f\) is nonconstant, there is a point with \(f(x,y)=0\). At that
point and \(z=0\), all partial derivatives of \(G=fz+b\) vanish.
Stability is again impossible. Thus the only stable case with constant
\(g\) is the already handled \(q=1\), constant nonzero \(f\) case.

The lower bound \(N\geq2\) is essential to the claimed equivalence.
For \(h(s)=s\) and \(G=z^2\), the polynomial \(F=s+z^2\) is a
coordinate, while \(G\) is not. The join calculation reflects this:
joining with one point gives a contractible cone and supplies no
homology restriction on \(Y\).

## 5. The converse and the stronger statement for \(q\geq2\)

If \(G\) is a coordinate, choose companions \(U,V\) with
\(\mathbb C[x,y,z]=\mathbb C[G,U,V]\). Then
\[
\mathbb C[s,x,y,z]
=\mathbb C[s,G,U,V]
=\mathbb C[s,F,U,V],
\]
since \(G=F-h(s)\). Thus \(F\) is a coordinate. Every coordinate is
stable. Together with Sections 1--4, this proves all of (1).

For \(q\geq2\), the hypotheses of (1) are also equivalent to the
existence of an automorphism \(\alpha\) of \(\mathbb C[x,y]\), a
polynomial \(p\in\mathbb C[x]\setminus\{0\}\), and a scalar \(b\)
such that
\[
\alpha(f)=p(x),\qquad \alpha(g)=y+b.
\tag{5}
\]
For nonconstant \(f,g\), this is the simultaneous-pair conclusion of
Theorem 7.2 applied to one general fiber \(G-\lambda\), with
\(b=\lambda\). The constant case was checked separately above.
Conversely, (5) changes \(G\) into
\(p(x)z^q+y+b\), an explicit coordinate. Here \(p\) is allowed to be
a nonzero constant.

This pair conclusion should not be extended to \(q=1\). For example,
\[
G=xz+y+xy^2=x(z+y^2)+y
\]
is a coordinate, while the plane polynomial \(g=y+xy^2\) is not a
coordinate. Indeed, for \(\lambda\ne0\), its level curve has \(y\ne0\)
and \(x=(\lambda-y)/y^2\), so it is \(\mathbb C^*\), not an affine
line. Thus this example cannot have a simultaneous pair of the form
(5), even though (1) holds for every \(h\) of degree at least two.

## Audit conclusion

The main equivalence and the \(q\geq2\) pair criterion both pass the
audit. The proof uses a general fiber, its ordinary integral homology,
the global sum theorem, and a surface rectification theorem that
already matches the binomial form. It does not require every summand
fiber to be contractible, nor does it infer ordinary coordinates from
rational Euler data.

The result concerns the displayed separable-sum presentation. It
provides no reduction of an arbitrary polynomial slice to that form
and therefore does not complete the general cancellation problem.

## Sources checked

[^global]: András Némethi,
[*Global Sebastiani--Thom theorem for polynomial maps*](https://www.jstage.jst.go.jp/article/jmath1948/43/2/43_2_213/_pdf/-char/en),
*Journal of the Mathematical Society of Japan* **43** (1991), 213--218,
Theorem 2.4 and Corollary 2.5, printed p. 216. These give the general
fiber join and its homology consequences directly.

[^generalized]: András Némethi,
[*Generalized local and global Sebastiani--Thom type theorems*](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf),
*Compositio Mathematica* **80** (1991), 1--14, Theorem G1 and Example
3.4(a), printed p. 6. The sum example explicitly verifies the stated
global assumptions.

[^surface]: Shulim Kaliman and Mikhail Zaidenberg,
[*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076v2),
Theorem 7.2, printed pp. 28--29; its constant-case comment immediately
precedes the theorem. The simultaneous-pair assertion is condition
(v). Example 7.1 explains the failure with rational acyclicity alone.
