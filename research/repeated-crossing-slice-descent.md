# Slice descent for every monomial crossing coefficient

Let \(r,s\geq1\) and \(H\in\mathbb C[x,y,z]\), with no degree bound.
Then
\[
\boxed{
F=x^r y^s u+H(x,y,z),\quad
D(F)=1\text{ for an LND }D\text{ of }\mathbb C[x,y,z,u]
\quad\Longrightarrow\quad F\text{ is a coordinate}.
}
\tag{1}
\]
The constant-axis branch closes through the geometry of each individual
fiber. It does not require proving that every stable coordinate in this
family is an ordinary coordinate. In particular, the argument does not
assume that a specified stable Vénéreau polynomial has an LND slice
structure on the original four-variable ring.

The key fiber statement is stronger than the consequence needed for
(1): every polynomial in either constant-axis residue normal
form below has all its fibers isomorphic to affine three-space, without
any stable-coordinate or slice hypothesis. The last step from this fiber
statement to (1) uses the original slice hypothesis essentially.
This fiber statement is a special case of the prior residual-plane
theorem of Kaliman, Vénéreau, and Zaidenberg, described below. It is not
a new residual-plane descent claim.

## 1. The constant-axis fiber theorem

Fix integers \(r,s,k\geq1\), scalars \(a,c\in\mathbb C^*\), and arbitrary
polynomials \(B\in\mathbb C[x]\), \(R\in\mathbb C[x,y,z]\). Put
\[
F=x^r y^s u+ay+cx^kz+B(x)+xyR(x,y,z).
\tag{2}
\]
For every \(\lambda\in\mathbb C\), define
\[
A_\lambda=\mathbb C[x,y,z,u]/(F-\lambda).
\]
Then
\[
\boxed{A_\lambda\cong\mathbb C[x]^{[2]}}
\tag{3}
\]
as a \(\mathbb C[x]\)-algebra. In particular,
\(\operatorname{Spec}A_\lambda\cong\mathbb A^3\).

For the other orientation,
\[
F=x^r y^s u+ax+cy^kz+C(y)+xyR(x,y,z),
\tag{4}
\]
the conclusion is \(A_\lambda\cong\mathbb C[y]^{[2]}\). It follows by
exchanging \(x,y\) in the proof and exchanging the coefficient exponents
\(r,s\). No equality of those exponents is required.

### Polynomial coordinates after inverting the base variable

Work first in
\[
S=\mathbb C[x,x^{-1},y],\qquad p=x^r y^s,\qquad n=xy,
\]
and write
\[
q(z)=cx^kz+ay+B(x)+nR(x,y,z),\qquad F=pu+q(z).
\]
The coefficient \(cx^k\) is a unit of \(S\). Also
\((n^s)\subseteq(p)\) in \(S\), since \(x\) is invertible.

The finite-inverse construction from
[the repeated-crossing proof, Section 1](repeated-crossing-pass.md)
applies over this ring. Explicitly, define
\[
I_0(T)=\frac{T-ay-B(x)}{cx^k},\qquad
I_{j+1}(T)=
\frac{T-ay-B(x)-xyR(x,y,I_j(T))}{cx^k},
\]
and take \(I=I_{s-1}\). When \(s=1\), use just \(I_0\).
Successive errors gain a factor \(xy\), giving both congruences
\[
q(I(T))\equiv T\pmod p,
\qquad I(q(z))\equiv z\pmod p.
\tag{5}
\]
These statements hold over \(S\), without passing to an algebraic closure
of \(\mathbb C(x)\). All denominators are powers of the already inverted
variable \(x\), times nonzero scalars.

The polynomial
\[
V=\frac{z-I(F)}p\in S[z,u]
\]
is a coordinate companion to \(F\). The inverse formulas are
\[
z=I(T)+pV,\qquad
u=\frac{T-q(I(T)+pV)}p.
\]
Both quotients are polynomial by (5), and substitution verifies both
compositions. Thus
\[
\mathbb C[x,x^{-1},y,z,u]
=\mathbb C[x,x^{-1},y,F,V],
\]
and hence
\[
A_\lambda[1/x]\cong\mathbb C[x,x^{-1}][y,V].
\tag{6}
\]
This proves all closed fibers over nonzero \(x\), as well as the generic
fiber over \(\mathbb C(x)\), are polynomial planes. It gives the entire
punctured-base trivialization at once; no deduction from closed points
to the generic point is needed.

### The remaining base fiber and flatness

At \(x=0\), the defining equation is
\[
ay+B(0)-\lambda=0.
\]
Since \(a\ne0\), it eliminates \(y\) and gives
\[
A_\lambda/xA_\lambda\cong\mathbb C[z,u].
\tag{7}
\]
This holds for every \(\lambda\), including \(\lambda=B(0)\), and is
a scheme-theoretic polynomial ring, not merely a reduced support.

For flatness, regard \(F-\lambda\) as a polynomial in \(u\) over the UFD
\(\mathbb C[x,y,z]\). Its coefficients are relatively prime. The only
possible irreducible common factors with \(x^ry^s\) would be \(x\) or
\(y\), but its constant coefficient has restrictions
\[
ay+B(0)-\lambda\ne0\quad\text{at }x=0,
\]
and
\[
cx^kz+B(x)-\lambda\ne0\quad\text{at }y=0.
\]
These are inequalities between polynomials, not claims that they have
no zeros. Therefore \(F-\lambda\) is primitive and linear in \(u\), so
Gauss's lemma makes it irreducible. The quotient \(A_\lambda\) is a
domain.

The natural map \(\mathbb C[x]\to A_\lambda\) is injective, as can also
be seen after the localization (6). Consequently \(A_\lambda\) is
torsion free as a \(\mathbb C[x]\)-module, and hence flat because
\(\mathbb C[x]\) is a PID. It is finitely presented by its displayed
hypersurface presentation.

Together, (6)--(7) show that \(A_\lambda\) is an
\(\mathbb A^2\)-fibration over \(\mathbb C[x]\): it is of finite type and
flat, and its fiber at every prime, including the generic prime, is a
polynomial ring in two variables over the residue field.

### The exact classical closing theorem

The input is the following established consequence of Sathaye and
Bass--Connell--Wright:

> If \(R\) is a PID containing \(\mathbb Q\), and \(A\) is a finite-type
> flat \(R\)-algebra whose fiber over each prime \(\mathfrak p\) is
> \(k(\mathfrak p)^{[2]}\), then \(A\cong R^{[2]}\) over \(R\).

Sathaye supplies the DVR case. Localization at maximal ideals followed
by Bass--Connell--Wright globalization reduces the PID case to a finite
projective module, which is free over a PID. This combined consequence
is stated explicitly in Babu and Das, in the discussion following
Problem 4.6; their Section 1 gives precisely the fibration definition
used here.[^fibration]

Apply this theorem with \(R=\mathbb C[x]\) and \(A=A_\lambda\). Every
hypothesis was established above, proving (3). The theorem is a statement
about an affine-plane fibration over a one-dimensional base. No
triviality assertion over \(\mathbb C[x,F]\), a two-dimensional base,
is being used.

### A direct prior theorem gives the same conclusion

Kaliman, Vénéreau, and Zaidenberg call \(p\) a residual \(x\)-plane when
each specialization at a complex value of \(x\) has a two-variable
polynomial quotient. Their Theorem 4.23 applies to every residual
\(x\)-plane of the form
\(p=f(x,y)u+g(x,y,z)\). It gives
\[
\mathbb C[x,y,z,u]/(p-\ell(x))\cong\mathbb C[x]^{[2]}
\qquad\text{for every }\ell\in\mathbb C[x].
\]
The polynomial-valued version is explicit in their definition 4.19 and
the concluding paragraph of proof 4.26.[^kvz]

For (2), the localization construction and the specialization at zero
verify these residual-plane hypotheses directly. Thus this published
result is an alternative closure of Section 1. Its statement is more
general than the monomial family considered here. In particular, the
affine-space fiber conclusion does not constitute a new theorem about
Vénéreau examples. The local inverse and flatness argument above remain
a separate verification that the classical fibration route applies.

## 2. From an original LND slice to a coordinate

Let
\[
T=\mathbb C[x,y,z,u],\qquad F=x^r y^s u+H(x,y,z),
\]
and assume an LND \(D:T\to T\) satisfies \(D(F)=1\). Set \(K=\ker D\).
The slice theorem gives
\[
T=K[F].
\tag{8}
\]
In particular, \(F\) is a one-stable coordinate: after adjoining a new
indeterminate \(W\), the ring \(K[W]\) is abstractly isomorphic to
\(K[F]=T\), so \(T[W]=K[W][F]\) is a polynomial algebra with \(F\)
as a coordinate. The slice theorem and the exact meaning of its original
ring hypothesis are also recorded in the same accessible source.[^slice]

There are now two cases.

If \(H(0,0,z)\) is nonconstant, the complete nonconstant-axis theorem in
[the repeated-crossing proof](repeated-crossing-pass.md) already gives
an ordinary coordinate, for all exponents \(r,s\).

If \(H(0,0,z)=b\) is constant, the stable-coordinate consequence of (8)
allows the necessary-residue theorem in that proof to be applied. It
gives exactly one of the forms (2) or (4), with \(B(0)=b\) or
\(C(0)=b\). That theorem uses integral topology, including the residue
map on the generic punctured-line stratum. It has no restriction on
the mixed remainder or its degree.

Section 1 now gives
\[
T/(F-\lambda)\cong\mathbb C^{[3]}
\qquad\text{for every }\lambda\in\mathbb C.
\tag{9}
\]
On the other hand, (8) identifies this quotient with the actual kernel:
\[
K[F]/(F-\lambda)\cong K.
\tag{10}
\]
Hence \(K\cong\mathbb C^{[3]}\). Choosing three polynomial generators
\(k_1,k_2,k_3\) of \(K\) in (8) yields
\[
T=\mathbb C[k_1,k_2,k_3,F],
\]
which proves (1). Only one value of \(\lambda\) would suffice for this
last argument; the fiber theorem proves all of them.

No invariance assumption \(D(x)=0\) or \(D(y)=0\) was made. The base
coordinate in the fiber theorem belongs to the quotient ring, and need
not coincide with its representative in the kernel under (10).

## 3. Audit of the distinction that makes the argument close

All hypotheses of the classical fibration theorem are present: finite
presentation is explicit; domain and flatness are established; the
special fiber is scheme-theoretically a plane; and the generic fiber
has a direct coordinate construction over its actual ground field.
Unequal multiplicities and arbitrary-degree mixed terms do not change
any of these checks.

The conclusion for a polynomial merely known to be stable is, in the
constant-axis branch, that all its fibers are affine three-spaces.
This note does not promote those separate fiber isomorphisms to a
coordinate of the original four-variable ring. That promotion in
Section 2 uses the original LND slice decomposition (8).

For example,
\[
v=xy^2u+y+x^2z+xyz^2
\]
is included in (2), so this argument proves
\(\mathbb C[x,y,z,u]/(v-\lambda)\cong\mathbb C[x]^{[2]}\) for every
\(\lambda\). If an LND on this same four-variable ring with
\(D(v)=1\) is supplied, (8)--(10) prove \(v\) is a coordinate.
Stabilizing first and producing a slice on the enlarged ring would
not supply that hypothesis. No claim about the current embedding status
of this example is needed for theorem (1).

The full cancellation problem is still outside the conclusion unless
one has independently shown that the given slice admits the displayed
monomial-coefficient presentation. Within that presentation, the
original slice problem is settled for every \(r,s\geq1\), including
\(xy^2u+H\) of total degree four. These are reconstructions using
classical inputs, with no originality assertion or human expert
review claim.

## Sources

[^fibration]: Janaki Raman Babu and Prosenjit Das,
[*Structure of \(\mathbb A^2\)-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/html/2001.07632v5),
Section 1, Theorem 2.2, and the paragraph following Problem 4.6. This
accessible primary paper explicitly records the combined PID consequence
used above. It cites A. Sathaye,
[*Polynomial Ring in Two Variables Over a D.V.R.: A Criterion*](https://doi.org/10.1007/BF01388536),
*Inventiones Mathematicae* **74** (1983), 159--168, and H. Bass,
E. H. Connell, D. L. Wright,
[*Locally Polynomial Algebras Are Symmetric Algebras*](https://doi.org/10.1007/BF01403135),
*Inventiones Mathematicae* **38** (1976/77), 279--299. The statement was
checked in Babu--Das; the original publisher texts were not retrieved
in this pass.

[^slice]: Babu and Das, [Section 1](https://arxiv.org/html/2001.07632v5),
recalls the slice theorem over rings containing \(\mathbb Q\).

[^kvz]: Shulim Kaliman, Stéphane Vénéreau, and Mikhail Zaidenberg,
[*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/html/math/0104204v2),
definition 4.19, Theorem 4.23, and proof 4.26. The exact hypotheses and
the \(\mathbb C[x]\)-algebra conclusion were checked in the primary text.
