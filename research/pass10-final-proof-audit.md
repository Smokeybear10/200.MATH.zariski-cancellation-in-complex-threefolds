# Final adversarial audit of the binomial arguments

No theorem-level correction was found in the current versions of
[the general binomial note](generic-rational-binomial-pass.md) and
[the double-binomial note](double-binomial-pass.md). The sign-off is
limited to their stated hypotheses and conclusions. In particular,
the three potentially fragile steps below have the necessary
justifications; none requires replacing rational acyclicity by
integral acyclicity.

This is a mathematical source-and-proof audit, not independent human
review or proof-assistant verification. The main files were not
modified.

## 1. Exponent one gives a univariate coefficient, not a coordinate pair

For \(G=f(x,y)z+g(x,y)\), assume its general fiber is smooth and
rationally acyclic. The coefficient-only conclusion is valid:
there is a plane coordinate \(a\) with \(f=p(a)\).

The essential hypotheses of KZ Lemma 7.5(b) are met at the selected
level. The fiber is connected by rational acyclicity and smooth,
hence irreducible. Its equation is reduced because the level is
regular. The choice of level excludes any common component of
\(V(f)\) and \(V(g-\lambda)\), so the two polynomials are
coprime. Constants are treated separately in the main note.

For nonconstant \(f,g\), the reduced curve
\(D=V(f)_{\mathrm{red}}\) has only finitely many singular points.
On each component where \(g\) is nonconstant, its differential on
the smooth locus is not identically zero in characteristic zero.
Its zero set there is finite. Thus the excluded singular values,
critical values, and values of constant restrictions form a finite
set, which can be avoided together with the bifurcation values.

KZ Lemma 7.5(b) then supplies disjoint simply connected coefficient
components that are smooth outside the level curve. The chosen
level avoids every singular point of \(D\), so the components
are smooth everywhere. A smooth connected affine complex curve
with trivial fundamental group is \(\mathbb A^1\). This does
not silently apply the smooth-curve conclusion to a cusp.

Rectify the first such component to \(a=0\). On any other
component, \(a\) is nowhere zero and hence a constant, since
the units of \(\mathbb C[t]\) are nonzero constants. The
component is a closed irreducible curve contained in a line
\(a=\alpha\), so it is that entire line. Distinct components
give distinct \(\alpha\). Their irreducible defining
polynomials are associated to \(a-\alpha\), and unique
factorization retains all original multiplicities in \(f=p(a)\).

Separately, KZ Lemma 7.6(b) and Proposition 7.1 apply to the
transverse selected fiber and rectify it in \(\mathbb A^3\).
Its reduced prime equation then makes \(G\) a coordinate.
These statements were checked against the primary text; they do not
use the additional integral-homology hypotheses in other clauses
of Lemma 7.5.[^kz]

The main note correctly does not claim that \((f,g)=(p(a),b)\)
when the exponent is one. Its example \(xz+y+xy^2\) verifies
why that stronger conclusion would be false.

## 2. Euler characteristic one needs the generic-component argument

A disconnected smooth affine curve can have Euler characteristic
one. Euler characteristic alone is therefore insufficient. The
binomial note supplies the missing input correctly.

For nonconstant \(g:\mathbb C^2\to\mathbb C\), remove a
finite set containing its bifurcation values. Over the remaining
connected base \(S\), the map is a locally trivial fibration.
Its total space \(g^{-1}(S)\) is a nonempty Zariski open subset
of \(\mathbb C^2\), hence analytically path connected. The
standard finite bifurcation-set statement is explicitly recalled
by Dimca--Némethi, Section 2.1.[^dn]

For a locally trivial fibration over a connected base, the connected
components of the total space correspond to the monodromy orbits
on the components of a fiber. Therefore the present monodromy is
transitive on those components. Monodromy gives homeomorphisms
between them, so all have the same integer Euler characteristic
\(e\). If there are \(r\) components and total Euler
characteristic one, then

\[
re=1,\qquad r\ge1,\quad e\in\mathbb Z.
\]

It follows that \(r=e=1\). The generic curve is connected and
smooth, so its Euler characteristic one makes it an affine line.
The argument uses neither a claim that \(g\) is already
primitive nor integral acyclicity of the three-variable binomial
fiber. It also explains why the parameter must be generic for
\(g\), as the main note explicitly arranges.

The subsequent simultaneous-coordinate argument for exponent
greater than one is also sound. After coefficient components are
parallelized, \(h=g-\lambda\) remains a plane coordinate.
Its restriction to the line \(a=0\) has exactly one simple
zero, so that restriction is affine-linear. In coordinates
\((h,w)\), the line is a polynomial graph \(w=r(h)\).
Its equation \(a\) is associated to \(w-r(h)\), proving
that \((a,h)\) is a coordinate pair. This establishes a common
base pair, not merely two unrelated rectifications.

## 3. Repeated roots and empty strata in the Gysin argument

Consider the quotient level

\[
X_\lambda=\{p(a)W+R(a,b,w)=\lambda\},
\]

and let \(\alpha_1,\ldots,\alpha_k\) be the distinct roots
of \(p\). Stability upstairs makes this quotient smooth and
rationally acyclic. Smoothness is not being inferred from a general
finite-quotient theorem: a critical point downstairs lifts through
\(W=v^d\) to a critical point upstairs. Rational cohomology of
a finite quotient equals the invariant rational cohomology of the
source, including at fixed points.[^quotient]

Choose a level regular for every nonconstant
\(R_i=R(\alpha_i,b,w)\), and different from the values of
constant \(R_i\). The open set is

\[
U\cong(\mathbb C\setminus\{\alpha_1,\ldots,\alpha_k\})
\times\mathbb C^2,
\]

while the closed set consists of the disjoint smooth divisors
\(E_i=\{R_i=\lambda\}\times\mathbb C_W\), allowing
empty \(E_i\) initially.

At a point of a nonempty \(E_i\), one of
\(\partial_b R_i,\partial_w R_i\) is nonzero. The implicit
function theorem then makes \(a-\alpha_i\) a transverse local
coordinate on \(X_\lambda\). Its divisor order is exactly one,
regardless of the order of the root in \(p\). Equivalently, its
Cartier quotient is the reduced ring

\[
\mathbb C[b,w,W]/(R_i-\lambda).
\]

This is the required multiplicity check. The residue must not be
multiplied by the exponent of \(a-\alpha_i\) in \(p\).

Ordinary rational Gysin gives an isomorphism

\[
\mathbb Q^k=H^1(U)\xrightarrow{\operatorname{res}}
\bigoplus_i H^0(E_i)
\]

because \(H^1(X_\lambda)=H^2(X_\lambda)=0\). With the
positive winding classes of \(a-\alpha_i\) as basis, column
\(i\) has entry one on every component over \(\alpha_i\)
and zero on every other component.

An empty \(E_i\) gives a zero column and contradicts
injectivity. Multiple components over one root give a target block
of dimension greater than one but an image of dimension one,
contradicting surjectivity. Thus every root contributes exactly one
connected component. This is stronger than an equality of total
Betti numbers and covers the constant-restriction case.

The next segment

\[
0=H^2(U)\longrightarrow\bigoplus_i H^1(E_i)
\longrightarrow H^3(X_\lambda)=0
\]

makes every curve \(\{R_i=\lambda\}\) an affine line. Its
reduced irreducible equation is rectifiable in \(\mathbb A^2\),
so \(R_i\) itself is a plane coordinate. There is no possible
higher power of the rectified equation at the chosen regular level.

## 4. Closing algebra and exponent-one descent

The double-binomial compatibility step has no remaining algebraic
ambiguity. Two base companions of the same coordinate differ by
\(c=\kappa a+h(b)\), with \(\kappa\ne0\) constant. If
the coefficient polynomials are both nonconstant, a root
specialization makes \(b+k(b)u^n\) a plane coordinate. A root
\(\beta\) of nonconstant \(k\) would factor its
\(\beta\)-fiber as

\[
(b-\beta)\left(1+\frac{k(b)}{b-\beta}u^n\right),
\]

with two nonunit factors. Thus \(k\) is constant. Degree of
composition forces \(h\) constant, giving the common coefficient
direction. Constant-coefficient branches are handled separately
and correctly.

When exactly one exponent is one, only coefficient rectification
is used. The resulting polynomial is linear in one variable with
univariate coefficient, and every root restriction is a plane
coordinate by the preceding Gysin calculation. Maubach Theorem 4.5
gives precisely the needed coordinate completion over the
univariate base and explicitly allows arbitrary root
multiplicities.[^maubach] No unproved higher-dimensional cancellation
case is imported through that sufficient direction.

## 5. Exact scope of the sign-off

The verified conclusions are those already stated in the main notes:

- A general smooth rationally acyclic fiber of
  \(fz^q+g\), with \(0\ne f\in\mathbb C[x,y]\) and
  \(q\ge1\), forces absolute coordinatehood and a univariate
  coefficient after a base automorphism. The simultaneous base form
  is asserted only for \(q\ge2\).
- Stability implies coordinatehood for
  \(Au^n+Bz^q+C\), with nonzero \(A,B\in\mathbb C[x,y]\)
  and positive exponents not both one. The common-base
  classification is asserted only when both exponents are at least
  two.

A single specially chosen rationally acyclic fiber is not substituted
for a general fiber. A base automorphism is not claimed to preserve
an independently specified original coordinate. No implication for
arbitrary \(xu^2+G(x,y,z)\), the all-linear double-binomial case,
or arbitrary polynomial slices is added.

For the stated original-slice corollary, the slice decomposition
\(\mathbb C^{[4]}=K[F]\) makes \(F\) a coordinate after one
extra variable: exchange \(F\) and that variable in
\(K[F,t]\). After the proved coordinate descent,
\(K\cong\mathbb C^{[4]}/(F)\cong\mathbb C^{[3]}\).
This verifies the corollary without identifying the original
derivation with a coordinate partial derivative in advance.

Finite symbolic controls do not verify Smith theory, Gysin theory,
monodromy transitivity, or the cited rectification results. The
sign-off rests on the checked mathematical inputs and the explicit
arguments above, with no generic-slice reduction supplied.

## Sources checked

[^kz]: Shulim Kaliman and Mikhail Zaidenberg,
[*Affine modifications and affine hypersurfaces with a very
transitive automorphism group*](https://arxiv.org/pdf/math/9801076v2),
Lemmas 7.4--7.6 and Proposition 7.1.

[^dn]: Alexandru Dimca and András Némethi,
[*On the monodromy of complex polynomials*](https://arxiv.org/html/math/9912072),
Section 2.1.

[^quotient]: Carlos Florentino and Jaime Silva,
[*Hodge-Deligne polynomials of character varieties of free abelian
groups*](https://arxiv.org/pdf/1711.07909), Section 4.2, equation (5)
and Proposition 4.3. The source includes nonfree finite actions.

[^maubach]: Stefan Maubach,
[*The commuting derivations conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf),
Theorem 4.5 and Corollary 4.2.
