# All-fiber acyclicity and the remaining torsion question

This bounded primary-source check did not locate a theorem asserting that
every polynomial \(G:\mathbb C^3\to\mathbb C\) with all fibers smooth
and rationally acyclic is a coordinate, or that its general fiber must
be integrally acyclic. This is a coverage statement, not a claim that
either assertion is open or false.

One proposed shortcut is definitely false, even in degree four: a
smooth general fiber of an arbitrary polynomial on \(\mathbb C^3\)
need not have torsion-free \(H_1\). An explicit primary counterexample
is given below. It does not satisfy the stronger all-fiber acyclicity
hypothesis.

## 1. What the pure slice form actually supplies

Suppose

\[
F=xu^n+G(x,y,z),\qquad n\ge2,
\]

is a stable coordinate. Each \(X_\lambda=\{F=\lambda\}\) is smooth
and contractible. For every prime \(p\mid n\), the action multiplying
\(u\) by a primitive \(p\)-th root preserves \(X_\lambda\), and its
fixed set is exactly

\[
Y_\lambda=\{u=0,G=\lambda\}\simeq G^{-1}(\lambda).
\]

Smith theory gives mod-\(p\) acyclicity of this fixed set. The
ordinary-cohomology statement used here is in [Peter Symonds, *Smith
Theory for algebraic varieties*, Section 4, Corollary 4.3 and the
following remark](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf).
Smoothness follows directly as well: at \(u=0\), the differential of
\(F\) is the differential of \(G\).

A smooth affine complex surface has a finite CW model of real
dimension at most two, as used explicitly in [Kaliman and Zaidenberg,
*Affine modifications and affine hypersurfaces with a very transitive
automorphism group*, proof of Lemma 7.1](https://arxiv.org/pdf/math/9801076).
Thus \(H_2(Y_\lambda;\mathbb Z)\) is free and higher homology
vanishes. The universal coefficient theorem now gives the precise
remaining possibility:

\[
H_0(Y_\lambda;\mathbb Z)=\mathbb Z,\quad
H_2(Y_\lambda;\mathbb Z)=0,\quad
H_1(Y_\lambda;\mathbb Z)=T_\lambda,
\]

where \(T_\lambda\) is finite and its order is relatively prime to
\(n\). In particular every fiber is rationally acyclic. This
calculation does not show \(T_\lambda=0\), and it says nothing by
itself about a possibly nonabelian fundamental group.

## 2. General fibers can have first-homology torsion

[Dimca and Némethi, *On the monodromy of complex polynomials*, Example
4.1, printed page 8](https://arxiv.org/pdf/math/9912072) give the
homogeneous quartic

\[
q=x^2y^2+y^2z^2+x^2z^2-2xyz(x+y+z).
\]

Its general fiber \(M=q^{-1}(1)\) satisfies

\[
\pi_1(M)=H_1(M;\mathbb Z)=\mathbb Z/3.
\]

The paper proves that the monodromy acts nontrivially on this group,
so it acts by \(-1\). It also identifies \(M\) as a fourfold cover
of the complement of the three-cuspidal quartic in \(\mathbb P^2\).

The following checks separate this example from the target. Euler's
homogeneous identity makes all nonzero fibers smooth, and scaling
identifies them. The projective quartic is rational with three
unibranch cusps, so it has Euler characteristic \(2\). Therefore

\[
\chi(M)=4\bigl(\chi(\mathbb P^2)-2\bigr)=4,
\qquad H_2(M;\mathbb Z)=\mathbb Z^3.
\]

Here the last equality uses the surface CW model and the stated
\(H_1\). Thus even the general fibers are not rationally acyclic;
in particular they are not mod-\(2\) acyclic. The zero fiber is
singular. The example decisively disproves general-fiber
torsion-freeness at the relevant degree, but does not refute the
all-fiber assertion under investigation.

For arbitrary torsion primes, [Cohen, Denham and Suciu, *Torsion in
Milnor fiber homology*, Theorems 1 and 2](https://arxiv.org/pdf/math/0302143)
give higher-degree homogeneous polynomials on \(\mathbb C^3\).
For instance
\(f_2=x^2y(x^2-y^2)^3(x^2-z^2)^2(y^2-z^2)\) has degree
\(15\), and \(H_1(f_2^{-1}(1);\mathbb Z)=
\mathbb Z^7\oplus(\mathbb Z/2)^2\). These examples likewise do
not satisfy the all-fiber hypotheses.

## 3. The relevant positive topology theorem needs an extra hypothesis

[Alexandru Dimca and András Némethi, *Hypersurface Complements,
Alexander Modules and Monodromy*, Definition 2.6 and Proposition
2.7](https://arxiv.org/pdf/math/0201291) prove a bouquet-of-spheres
conclusion for a polynomial
\(f:\mathbb C^{r+1}\to\mathbb C\) that is *homotopically good*.
Their condition is that, for every atypical value \(b\), the pair
\((T_b,F_{\rm gen})\) is \(r\)-connected, where \(T_b\) is the
inverse image of a sufficiently small disk about \(b\).
Then the general fiber has the homotopy type of a bouquet of
\(r\)-spheres.

For \(r=2\), rational acyclicity plus this conclusion would indeed
give integral acyclicity and contractibility of the general fiber.
The paper lists isolated singularities in affine space and at infinity
as a sufficient setting. Smoothness in affine space alone does not
verify its condition at infinity.

The same paper's Remark 2.8 has a different use of the word generic:
it concerns removing a generic hyperplane from a fixed projective
hypersurface. It does not assert torsion-freeness for the general level
of an arbitrary affine polynomial with its given hyperplane at
infinity. The example in Section 2 makes the distinction decisive.

No implication from all fibers being smooth and rationally acyclic to
the required connectedness of these tube pairs was established here.

[Dimca and Némethi, Corollary B](https://arxiv.org/pdf/math/9912072),
in homological degree one, also supplies a conditional route: when
the general fiber is connected and all fibers are irreducible,
trivial integral \(H_1\)-monodromy at infinity forces
\(H_1(F_{\rm gen};\mathbb Z)=0\). The all-fiber rational
condition has not been shown here to force that monodromy to be
trivial.

## 4. Exact algebraic scope and compatible examples

### Affine-plane fibers are a stronger input

[Shulim Kaliman, *Polynomials with general C2-fibers are variables.
I*](https://arxiv.org/abs/math/9912058) proves that a polynomial on
\(\mathbb C^3\) whose general fibers are isomorphic to
\(\mathbb A^2\) is a variable. Rational or integral acyclicity is
not the theorem's fiber hypothesis.

Integral acyclicity of a smooth irreducible surface given by
\(a(x,y)z^m+b(x,y)=0\) does imply rectifiability by [Kaliman and
Zaidenberg, Theorem 7.2](https://arxiv.org/pdf/math/9801076).
This is an additional equation-shape hypothesis, not a theorem for
arbitrary \(G\).

### One rationally acyclic fiber, even with all fibers smooth, is insufficient

[Kaliman and Zaidenberg, Example 7.1](https://arxiv.org/pdf/math/9801076)
compute for \(g=x^2z-x-y^2\) that \(g^{-1}(0)\) is rationally
acyclic with \(H_1\simeq\mathbb Z/2\).

Here is a direct check of why this does not address the all-fiber
question. The gradient never vanishes, since \(g_z=x^2\) forces
\(x=0\), where \(g_x=-1\). For a nonzero level \(\lambda\), the
part with \(x\ne0\) is \(\mathbb C^*\times\mathbb C\), while
\(x=0\) consists of two affine lines given by
\(y^2=-\lambda\). Additivity gives

\[
\chi(g^{-1}(\lambda))=2\quad(\lambda\ne0),
\]

so these other fibers are not rationally acyclic. The all-fiber
condition really excludes this example, despite global smoothness.

### Even a contractible general fiber alone does not imply coordinatehood

[Kaliman and Makar-Limanov, *AK-invariant of affine domains*, Section
10](https://www.math.miami.edu/~kaliman/library/KM-L.miyanishi.pdf)
discuss the contractible hypersurfaces of logarithmic Kodaira
dimension one defined by \(P_{m,a,b}\), and explicitly observe that
the zero fiber of \(P_{1,a,b}\) is a general fiber. For example,

\[
P(x,y,z)=\frac{(zy+1)^2-(zx+1)^3+z}{z}
=zy^2+2y-z^2x^3-3zx^2-3x+1
\]

is their \(m=1,a=3,b=2\) case. It has a contractible general
fiber, yet it is not a coordinate. One can verify the latter without
any surface classification: its gradient vanishes on
\(x=y=-1/z\), \(z\ne0\), and this critical curve lies in
\(P^{-1}(1)\). This is a degree-five example, and again it does
not have all fibers smooth.

### Higher-dimensional all-fiber analogues do fail

[Tammo tom Dieck, *Hyperbolic modifications and acyclic affine
foliations*, Theorem A](https://www.uni-math.gwdg.de/tammo/preprints/hyperbol.pdf)
constructs, for every ambient dimension \(r\ge4\), nonsingular
polynomials on \(\mathbb C^r\) all of whose fibers are
diffeomorphic to Euclidean space but some of whose fibers are
algebraically exotic. Its dimension restriction excludes
\(G:\mathbb C^3\to\mathbb C\). It rules out importing an
unrestricted-dimensional version of the desired implication.

## 5. Bounded next target and coverage limit

The exact unresolved step in this pass is

\[
\text{all fibers smooth and rationally acyclic}
\quad\stackrel{?}{\Longrightarrow}\quad
H_1(G^{-1}(\lambda);\mathbb Z)=0
\text{ for general }\lambda.
\]

A useful next check is whether the actual degree-four \(G\), or its
specific leading-form strata, forces homotopical goodness or another
integral vanishing-cycle condition at infinity. That would target the
missing torsion statement, without assuming generic hypersurface
homology is always torsion-free. Even successful integral descent
would still need an appropriate algebraic theorem or equation-shape
argument to turn the surface into \(\mathbb A^2\).

For the original pure expression, absolute coordinatehood of \(G\)
would also not by itself establish the relative identity
\(\mathbb C[x,y,z]=\mathbb C[x,G,t]\). This separate distinction
from the existing pure-form note remains in force.

The search checked the displayed original papers and exact searches
for smooth, acyclic or rationally acyclic polynomial fibers, including
all-fiber and general-fiber formulations. No database-exhaustive or
historical-priority claim is made. No AI-generated repository was
used as mathematical evidence. The note establishes the counterexample
to the unrestricted torsion-free shortcut and records valid conditional
routes; it does not settle the exact all-fiber implication.
