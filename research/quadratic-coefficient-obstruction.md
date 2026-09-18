# The smooth rank-three quadratic coefficient obstruction

Let \(v=(x,y,z)\), let \(P(v)\) be a quadratic polynomial with nondegenerate quadratic part, and suppose its completed-square constant is nonzero. Equivalently,

\[
 D=\{P=0\}\subset\mathbb A^3_{\mathbb C}
\]

is a smooth affine quadric surface. For every polynomial \(H\in\mathbb C[x,y,z]\), the polynomial

\[
 F(v,u)=P(v)u+H(v)
\]

is neither a stable coordinate nor a slice of a locally nilpotent derivation on \(\mathbb C[x,y,z,u]\). There is no degree bound on \(H\).

More precisely, for generic \(\lambda\in\mathbb C\), its fiber \(X_\lambda=\{F=\lambda\}\) satisfies

\[
 \boxed{\mathbb Q\hookrightarrow H_c^3(X_\lambda;\mathbb Q).}
 \tag{1}
\]

The following proof is an independent cohomological reconstruction, with no claim of novelty. It does not use or settle a general cancellation theorem.

## 1. The open subset does not depend on the remaining coefficient

On \(P(v)\ne0\), the equation of the fiber determines

\[
 u=\frac{\lambda-H(v)}{P(v)}.
\]

Therefore the projection to \(v\) is an algebraic isomorphism

\[
 U_\lambda:=X_\lambda\cap\{P\ne0\}
 \simeq\mathbb A^3\setminus D.
 \tag{2}
\]

The closed complement, with its reduced topological support, is

\[
 Z_\lambda=X_\lambda\setminus U_\lambda
 =C_\lambda\times\mathbb A^1_u,
 \qquad C_\lambda=\{P=0,H=\lambda\}.
 \tag{3}
\]

If \(H|_D\) is constant, choose \(\lambda\) different from that constant. Then \(C_\lambda\) is empty, and the open set is the entire fiber.

Otherwise \(H|_D\) is a nonconstant morphism from the smooth irreducible surface \(D\) to \(\mathbb A^1\). For generic \(\lambda\), its fiber \(C_\lambda\) is a smooth affine curve, possibly with several components. One can justify the finite exclusion directly: the critical locus has finitely many irreducible components, and in characteristic zero the function is constant on each positive-dimensional component of its critical locus. Its critical values are therefore finite. No irreducibility of \(C_\lambda\) is assumed.

Each connected component of a smooth affine curve is noncompact. Consequently,

\[
 H_c^0(C_\lambda;\mathbb Q)=0,
 \qquad H_c^2(Z_\lambda;\mathbb Q)=0,
 \tag{4}
\]

where the second equality is the compact-support Künneth shift by two for \(\mathbb A^1\). The same vanishing holds when the curve is empty.

## 2. The quadric has a nonzero compactly supported group in degree two

After an affine change of the three variables, the surface \(D\) has equation

\[
 XY+Z^2=a,\qquad a\ne0.
\]

Its smooth projective closure \(Q\subset\mathbb P^3\) has equation

\[
 XY+Z^2=aT^2.
\]

Writing \(A=\sqrt aT+Z\), \(B=\sqrt aT-Z\) gives \(XY=AB\), the Segre quadric. Thus \(Q\simeq\mathbb P^1\times\mathbb P^1\). Its boundary \(E=Q\cap\{T=0\}\) is a smooth conic of bidegree \((1,1)\), isomorphic to \(\mathbb P^1\).

The compact-support sequence for \(D=Q\setminus E\) contains

\[
 0=H^1(E)
 \longrightarrow H_c^2(D)
 \longrightarrow H^2(Q)=\mathbb Q^2
 \longrightarrow H^2(E)=\mathbb Q.
\]

The last map is \((a,b)\mapsto a+b\), because each ruling class has degree one on the boundary. Its kernel is one-dimensional, so

\[
 H_c^2(D;\mathbb Q)\simeq\mathbb Q.
 \tag{5}
\]

Next, the sequence for \(D\subset\mathbb A^3\) gives

\[
 H_c^2(\mathbb A^3)=0
 \longrightarrow H_c^2(D)
 \longrightarrow H_c^3(\mathbb A^3\setminus D)
 \longrightarrow H_c^3(\mathbb A^3)=0.
\]

Thus (2) and (5) imply \(H_c^3(U_\lambda;\mathbb Q)\simeq\mathbb Q\).

## 3. The closed curve stratum cannot remove this class

The sequence for \(Z_\lambda\subset X_\lambda\) includes

\[
 H_c^2(Z_\lambda)
 \longrightarrow H_c^3(U_\lambda)
 \longrightarrow H_c^3(X_\lambda).
\]

The first group vanishes by (4). Therefore the last arrow is injective, proving (1). In particular, no assumptions on the genus or number of components of the generic curve are needed.

If \(F\) became a coordinate after adjoining \(N\) independent variables, every fiber would satisfy

\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}.
\]

Compact-support Künneth would then make \(H_c^i(X_\lambda;\mathbb Q)\) vanish for \(i\ne6\), contradicting (1). A slice is a one-stable coordinate by the slice theorem, so it is excluded too.

The mechanism is more general than this particular quadric computation: a nonzero \(H_c^2(D)\) in the coefficient divisor injects into the generic threefold fiber whenever the closed curve stratum has \(H_c^0=0\). The smooth affine quadric supplies the required nonzero group explicitly.

## 4. The rank-three cone is also excluded, by an integral argument

If the completed-square constant is zero, the coefficient divisor is a quadric cone. The rational group (5) vanishes, so the preceding rational argument does not apply. The integral obstruction is nevertheless decisive; its full proof is in [the quadric-cone appendix](quadric-cone-obstruction.md).

An independent check of its degree shifts is as follows. The cone is homeomorphic to \(\mathbb C^2/\{\pm1\}\), hence is the open real cone on \(\mathbb{RP}^3\). Its one-point compactification is the suspension of \(\mathbb{RP}^3\), giving

\[
 H_c^2(D;\mathbb Z)=0,
 \qquad H_c^3(D;\mathbb Z)=\mathbb Z/2.
\]

Thus \(H_c^3(U;\mathbb Z)=0\) and \(H_c^4(U;\mathbb Z)=\mathbb Z/2\). Choose a generic value away from the value of \(H\) at the vertex. The curve \(C_\lambda\) is smooth or empty, so \(H_c^3(Z_\lambda;\mathbb Z)=H_c^1(C_\lambda;\mathbb Z)\) is free abelian. Stability would make \(H_c^3(X_\lambda)\) and \(H_c^4(X_\lambda)\) vanish, forcing an isomorphism

\[
 H_c^1(C_\lambda;\mathbb Z)\simeq\mathbb Z/2
\]

in the closed-open exact sequence, a contradiction. Both adjacent vanishing groups are necessary here; a map from a free group onto torsion alone would not be contradictory.

Combining the two cases excludes every rank-three quadratic coefficient \(P\), for every \(H\), from being a stable coordinate or an LND slice in the displayed four-variable form.

## Scope

The conclusion concerns the polynomial map \(P(v)u+H(v)\) and its generic fibers. It neither proves that all remaining slice polynomials admit such a presentation nor settles an abstract cylinder isomorphism for a single exceptional fiber. The proof consists of explicit compactifications and standard cohomological exact sequences; it is not a proof-assistant certificate.
