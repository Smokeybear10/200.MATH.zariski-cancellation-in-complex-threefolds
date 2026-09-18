# Quadratic slices: exact literature scope and a relative obstruction

The proposed use of the residual-variable theorem needs an additional
relative hypothesis. An actual quartic coordinate of the exact form
\(xu^2+Bu+C\) need not be a residual \(x\)-variable. The counterexample
below rules out deriving that condition from stability or an original
slice alone.

The bounded primary-source search did not locate a theorem asserting
that every slice of total degree at most four in \(\mathbb C^{[4]}\)
is a coordinate. This is a coverage statement, not evidence of novelty
or a conclusive statement about the current literature.

## 1. The exact KVZ theorem

[Kaliman, Vénéreau and Zaidenberg, *Simple birational extensions of the
polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/pdf/math/0104204),
Theorem 4.27, printed pp. 46–47, says that

\[
 p=f(x,y,z)u^n+g(x,y,z),\qquad n\ge2,
\]

is a coordinate over \(\mathbb C[x]\) if every specialization
\(p(\gamma,y,z,u)\), \(\gamma\in\mathbb C\), is a coordinate in
\(\mathbb C[y,z,u]\). The conclusion is relative polynomial
coordinatehood, not merely polynomiality of one quotient. The theorem
has no total-degree bound. It does not include an arbitrary intermediate
term \(Bu\).

Its proof first obtains simultaneous rectification of each specialized
pair \((f_\gamma,g_\gamma)\), then rectifies \(g\) over
\(\mathbb C[x]\). A polynomial interpolation argument puts the other
coefficient in the form

\[
 f=\Phi(x,a(x)y+zQ(x,z)).
\]

Corollary 1.30 handles the remaining dilation of \(y\). In the displayed
definition of \(P\) near the end of printed p. 46, the manuscript writes
\(\Phi(x,y')u+z\). The argument requires \(u^n\) there; this is a
harmless missing exponent, since the triangular-coordinate argument
works with \(\Phi(x,y')u^n+z\).

For

\[
 F=xu^2+Bu+C,
\]

the triangular change \(v=u+B/(2x)\) belongs to the polynomial
automorphism group over \(\mathbb C[x,y,z]\) when \(x\mid B\).
It then gives

\[
 F=xv^2+\left(C-\frac{B^2}{4x}\right).
 \tag{1}
\]

Without \(x\mid B\), this is only a localized change. It does not
put \(F\) under Theorem 4.27 globally. Even with (1), the residual
condition must still be established.

## 2. A quartic coordinate which fails every residual specialization

Consider

\[
 F=xu^2+yu+x+z^4,\qquad
 D=\partial_x-u\partial_y.
 \tag{2}
\]

This has total degree four, and

\[
 D(F)=(u^2+1)-u^2=1.
\]

The derivation is locally nilpotent: it fixes \(u,z\) and lowers total
degree in \(x,y\). More explicitly, put \(w=y+xu\). Then

\[
 F=x+uw+z^4,
\]

and the inverse of the coordinate system \((F,w,u,z)\) is

\[
 x=F-uw-z^4,\qquad y=w-u(F-uw-z^4).
\]

Nevertheless, for every \(\gamma\in\mathbb C\),

\[
 F_\gamma=\gamma+u(y+\gamma u)+z^4
\]

has a critical point at \(u=y=z=0\). It is not a coordinate in
\(\mathbb C[y,z,u]\). Removing \(z^4\) gives the same phenomenon
in total degree three; its level \(\gamma\) is reducible.

This is an independently checked algebraic counterexample to

\[
 \text{absolute coordinate, stable coordinate, or original slice}
 \Longrightarrow \text{residual variable for the specified }x.
\]

It is not a counterexample to the proposed degree-four slice theorem.
It also does not settle whether a smaller pure-power subclass with
coefficient exactly \(x\) satisfies additional implications.

## 3. Relative hypotheses which really are sufficient

Here are valid ways to establish residual \(x\)-coordinatehood.

* If an automorphism completing \(F\) after stabilization fixes \(x\),
  specialize that automorphism and its inverse at each \(x=\gamma\).
  Every \(F_\gamma\) is then a stable coordinate in three variables.
* More generally, suppose a locally nilpotent derivation on
  \(\mathbb C[x,y,z,u,w_1,\ldots,w_N]\) satisfies
  \(D(x)=0\) and \(D(F)=1\). It descends at every \(x=\gamma\)
  to a slice derivation. The slice decomposition makes
  \(F_\gamma\) a stable coordinate, with one further auxiliary
  variable if necessary.

In both cases, stable-coordinate descent in three complex variables
gives ordinary coordinatehood of each specialization. This finite-
stabilization statement is [Shpilrain and Yu, *Affine varieties with
equivalent cylinders*, Proposition 1.1(c) and its proof](https://arxiv.org/html/math/0110324).
If the global expression also has the pure-power shape, KVZ applies.

For an original slice, the stronger condition \(D(x)=0\) already
provides another route for arbitrary \(F\). With
\(K=\ker D\), the slice decomposition is over \(\mathbb C[x]\),
and

\[
 K\simeq\mathbb C[x,y,z,u]/(F).
\]

Its fibers over \(x\) are affine planes by three-variable slice
cancellation; the generic fiber is an affine plane by the same
characteristic-zero cancellation theorem over \(\mathbb C(x)\).
Flatness follows from torsion-freeness over the PID. The
Sathaye and Bass–Connell–Wright affine-plane-fibration result gives
\(K\simeq\mathbb C[x]^{[2]}\), hence a coordinate completion over
\(\mathbb C[x]\). The relevant relative cancellation and fibration
scope is explicitly recorded in [Das, *On cancellation of variables of
the form \(bT^n-a\) over affine normal domains*, Introduction](https://arxiv.org/pdf/2002.02129).
This route does not require a degree bound. Finding such an invariant
ambient coordinate is additional work, not a consequence of low degree
of the slice.

## 4. The stronger surface theorem behind KVZ

[Kaliman and Zaidenberg, *Affine modifications and affine hypersurfaces
with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076),
Theorem 7.2, printed pp. 28–29, concerns an irreducible smooth surface

\[
 X=\{f(y,z)v^n+g(y,z)=0\}\subset\mathbb A^3_{\mathbb C},
 \qquad n\ge1.
\]

It proves equivalence of integral acyclicity, the conditions
\(\chi(X)=1\) and \(H_1(X;\mathbb Z)=0\), isomorphism to
\(\mathbb A^2\), and rectifiability. For \(n>1\), these are also
equivalent to simultaneous rectification of \((f,g)\) to
\((q(y),z)\). Rational acyclicity is insufficient: their Example 7.1
has \(H_1=\mathbb Z/2\).

Consequently, in the pure-power family, it suffices to prove that every
fixed-\(x\) zero surface is smooth, irreducible, and integrally acyclic.
The original slice hypothesis gives information about the threefolds
\(F^{-1}(\lambda)\), not automatically about those surface sections.
Example (2) shows why this distinction cannot be omitted.

A useful positive application concerns the monic branch
\(H=s^2+G(v_1,v_2,v_3)\). If \(H\) is stable and the completed
remainder \(G\) is itself binomial in one remaining variable,
the general-fiber integral acyclicity established in
[the monic-branch note](quartic-quadratic-variable-pass.md) combines
with this surface theorem to prove \(G\), and hence \(H\), is a
coordinate. Only a smooth general fiber of \(G\) is needed.
The integral acyclicity input is the sum case of
[Némethi, *Generalized local and global Sebastiani-Thom type theorems*,
Theorem G1 and Example 3.4(a)](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf).
This is a deduction from published results, not a new literature claim.

## 5. Wright, relative cancellation, and the dimension mismatch

Wright's original paper is *Cancellation of variables of the form
\(bT^n-a\)*, *Journal of Algebra* **52** (1978), 94–100.
Its exact theorem is reproduced in [Das, Theorem 1.4](https://arxiv.org/pdf/2002.02129):
for an affine normal domain \(A\) over an algebraically closed field,
\(b\ne0\), and \(n\ge2\) prime to positive characteristic,

\[
 A[T]/(bT^n-a)\simeq k^{[2]}
\]

forces \(A\simeq k^{[2]}\) and coordinatehood of the defining
equation. The original Wright text was identified but not independently
read in this pass; the stronger complex-surface theorem above was read
directly.

Das's own Theorem 3.4 works over a Noetherian normal domain \(R\)
containing a field. If \(a,b\in A\) and

\[
 A[T]=R[bT^n-a]^{[2]},
\]

then \(A=R[a]^{[1]}\), under the same exponent restriction. This
requires a known relative polynomial presentation. It does not infer it
from absolute stability.

There are two scope barriers here. In our target, the unknown quotient
has dimension three, whereas Wright's polynomial quotient is an affine
plane. Also, in \(S=K[F]\), the indeterminate \(T\) would be the
slice \(F\). A low-degree expression of \(F\) in the ambient
variable \(u\) does not give an ambient coordinate expressed as
\(bF^n-a\) with coefficients in \(K\).

[Russell, *Simple Galois extensions of two-dimensional affine rational
domains*](https://www.numdam.org/item/CM_1979__38_3_253_0.pdf),
Introduction and Theorem 2.4, broadens the simple-extension mechanism
to suitable Galois extensions inside a polynomial plane. It retains the
two-dimensional setting and hypotheses on the base domain. It is not
a classification of stably polynomial threefold double covers.

## 6. What the quadratic double-cover model loses at the boundary

For \(X_\lambda=\{xu^2+Bu+C=\lambda\}\), put

\[
 v=2xu+B,\qquad \Delta_\lambda=B^2-4x(C-\lambda).
\]

After inverting \(x\), there is an exact presentation

\[
 \mathbb C[X_\lambda][1/x]
 \simeq
 \frac{\mathbb C[x,x^{-1},y,z,v]}{(v^2-\Delta_\lambda)}.
 \tag{3}
\]

This is not generally a global isomorphism. The involution suggested by
(3) sends \(u\) to \(-u-B/x\), which need not be polynomial.
The original boundary has equation

\[
 B(0,y,z)u+C(0,y,z)=\lambda,
\]

while the naive square model at \(x=0\) has
\(v^2=B(0,y,z)^2\). Reconstructing the original chart additionally
uses \(v-B=2xu\). Thus the boundary modification cannot be ignored
when applying cyclic-cover or fixed-point arguments.

For a constant nonzero leading coefficient the involution is global
after completing the square, but completion can raise total degree
from four to six when \(\deg B=3\). Smith theory controls fixed-set
mod-2 cohomology, not polynomiality of the fixed surface; the existing
monic-branch note also supplies an explicit failure of averaging to
preserve local nilpotence.

As another control, the Russell polynomial
\(x^2u+x+y^2+z^3\) has a smooth contractible zero threefold which is
not \(\mathbb A^3\); this example is discussed in the KVZ
Introduction. All its fibers are smooth, but a nonzero fiber has Euler
characteristic \(-1\): its \(x\ne0\) part contributes zero, and its
\(x=0\) part is \(\{y^2+z^3=\lambda\}\times\mathbb A^1\).
It is therefore not a stable coordinate. This blocks weakening the
global assumption to smoothness and one contractible fiber; it does
not contradict any slice result.

## 7. Coverage and the next decisive checks

The source search used combinations of slice, quartic, degree four,
degree at most four, low degree, stable coordinate, quadratic
cancellation, residual variable, double cover, hyperelliptic polynomial,
and polynomial-ring retract, together with the names of the relevant
authors. The resulting original papers directly checked were KVZ,
Kaliman–Zaidenberg, Das, and Russell; Sathaye's *On linear planes* was
also located in an author-hosted copy. Search hits from AI research
repositories and unrelated automated theorem sites were not used.

No matching global degree-four slice theorem was found. The search was
not an exhaustive MathSciNet or zbMATH audit, and did not examine every
monograph chapter or non-English thesis. The result should therefore
remain a working theorem or target with unresolved priority until a
broader bibliographic check is completed.

The most useful bounded follow-ups are to test for an invariant ambient
coordinate under the given slice derivation, to classify the gluing data
at \(x=0\) in (3), and to identify which completed monic remainders
fall under the binomial surface criterion. A proof that merely recycles
global stability into residual coordinatehood for the displayed \(x\)
cannot work because of (2).
