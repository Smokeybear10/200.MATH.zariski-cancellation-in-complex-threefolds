# Two-power coordinate descent and the remaining cancellation gap

A complete working argument now settles stable-coordinate descent for
\[
F=A(x,y)u^n+B(x,y)z^q+C(x,y),
\qquad A,B\ne0,\quad n,q\ge1.
\]
There is no upper degree bound. If both exponents exceed one, the
argument gives an exact classification: stability holds precisely when
base coordinates \(a,b\) can be chosen so that
\[
C=b,\qquad A=r(a),\qquad B=p(a)
\]
for nonzero univariate polynomials \(r,p\), including constants.
In that form, retaining \(a,u,z\) and replacing \(b\) by \(F\)
is an invertible polynomial change of coordinates.

The all-linear boundary \(n=q=1\) is already covered by the
published KVZ Theorem 3.24. It is included here by attribution,
not presented as a new result.[^10]

This is a restricted family theorem, not a solution of
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\]
No argument reduces an arbitrary example of this cancellation
problem to the displayed family. The mathematical deductions have
written proofs and separate model reconstructions, but no human
expert review or proof-assistant verification. Their novelty is
not established.

## 1. Definitions and connection to cancellation

A coordinate of \(\mathbb C[x_1,\ldots,x_N]\) is a polynomial that
can serve as one member of a polynomial coordinate system. The
change of coordinates must have a polynomial inverse. A stable
coordinate becomes a coordinate after adjoining finitely many
independent variables. Every level hypersurface of a stable
coordinate becomes affine space after taking a product with
affine space. In particular its underlying topological space is
contractible, and its equation has no critical point.

An original locally nilpotent derivation with slice \(F\) gives
\(\mathbb C[x,y,u,z]=K[F]\), where \(K\) is its kernel. The slice
is a stable coordinate: a second copy of the slice variable
identifies \(K[t]\) with a four-variable polynomial ring.
If \(F\) is an ordinary coordinate, then \(K\), identified with
the quotient by \(F\), is a three-variable polynomial ring.
Thus the family theorem really does answer cancellation for
original slices having its specified presentation.

The crucial qualifier is “having its specified presentation.”
The slice theorem by itself does not produce that form. Nor
does a lower degree in one variable give a reduction of the total
degree. Both distinctions remain necessary in any attempted
extension.

## 2. General binomial fibers: rational homology suffices

The central auxiliary statement is the following.

**Binomial-fiber theorem.** Let
\[
G=f(x,y)v^d+g(x,y),\qquad f\ne0,\quad d\ge1.
\]
If a general fiber is smooth and rationally acyclic, then \(G\)
is a coordinate. A base automorphism makes \(f\) univariate.
For \(d\ge2\), the stronger conclusion is
\[
f=p(a),\qquad g=b,\qquad \mathbb C[x,y]=\mathbb C[a,b].
\]

“General” means over a nonempty Zariski open subset of the
parameter line, not one arbitrarily selected smooth fiber.
“Rationally acyclic” includes connectedness and the vanishing
of every positive rational homology group.

The source inputs are the rational-acyclic affine-modification
lemmas and rectification criterion in Kaliman and Zaidenberg,
Section 7. They constrain the coefficient divisor and, for
\(d>1\), the Euler characteristic of the plane level curve.[^1]
The additional argument is to choose a level avoiding singular
points of the reduced coefficient divisor and critical values
of the plane restrictions. At that level the intersections are
transverse.

This genericity eliminates the exceptional tangency that can
occur at a special rational homology plane. The coefficient
components become disjoint embedded affine lines. Rectifying one
makes all the others parallel, because an invertible function
on an affine line is constant. Their multiplicities remain in
the univariate polynomial \(p\).

For \(d>1\), the general plane fiber of \(g\) has Euler
characteristic one. Its monodromy is transitive on connected
components, since the total space above the regular-value open
set is connected. If there are \(r\) components with common
Euler characteristic \(e\), then \(re=1\), forcing one affine
line. A graph argument then makes \(g\) a companion to the
coefficient coordinate. Constant \(f\) or \(g\) is handled
separately.

The complete proof is in
[General rationally acyclic binomial fibers](research/generic-rational-binomial-pass.md).
It does not preserve an arbitrarily designated original
coordinate. For \(d=1\), it does not assert that \(g\) is
itself a plane coordinate.

## 3. The root-specialization obstruction

A second lemma extracts information that separate fixed-surface
tests do not capture.

Suppose
\[
L=p(a)v^d+R(a,b,w)
\]
is stable, with \(p\ne0\) univariate and \(d\ge1\).
Then, at every root \(\alpha\) of \(p\),
\(R(\alpha,b,w)\) must be a plane coordinate.

For \(d>1\), quotient a level hypersurface by the cyclic action
on \(v\), writing \(W=v^d\). The quotient has equation
\[
p(a)W+R(a,b,w)=\lambda.
\]
Its rational cohomology is the invariant part of the cohomology
upstairs, so it is rationally acyclic.[^2] It is also smooth:
any critical point downstairs lifts, by choosing a \(d\)-th
root of \(W\), to a critical point of \(L\). This is a check
for this equation, not a general assertion that finite
quotients preserve smoothness.

Away from the \(k\) distinct roots of \(p\), the quotient is
\((\mathbb C\setminus\{\alpha_1,\ldots,\alpha_k\})\times\mathbb A^2\).
Above a root it is a plane level curve times \(\mathbb A^1\).
The rational Gysin sequence forces the residue map from the
\(k\) root circles to the connected components of those closed
strata to be an isomorphism.

Each root circle has residue one on each component above its
own root and zero elsewhere. This remains true for repeated
roots: the selected plane level equation is reduced, so the
divisor defined by \(a-\alpha_i\) has order one. An isomorphism
therefore requires exactly one component above each root.
The next part of the same sequence kills its first homology.
The curve is an affine line, which proves the lemma by
plane-line rectification.

Empty strata, disconnected strata, and root multiplicities
are addressed explicitly in
[Two-power coordinate descent, Section 2](research/double-binomial-pass.md).
The lemma is necessary for a general pure-power expression.
No converse is claimed for arbitrary \(R\) and \(d>1\).

## 4. Why the two coefficient directions must coincide

Assume \(n,q\ge2\) and \(F\) is stable. Choose a prime divisor
of \(n\) and act on \(u\). Smith theory makes the fixed surface
\[
B(x,y)z^q+C(x,y)=\lambda
\]
acyclic with prime-field coefficients.[^3] Smoothness and a
finite CW model imply rational acyclicity. The binomial-fiber
theorem gives \(C=b\) and \(B=p(a)\) in base coordinates.

Repeating the argument using the action on \(z\) gives
\(A=r(c)\), where \(c\) is another companion to the same
coordinate \(b=C\). Automorphisms of the one-variable ring
over \(\mathbb C[b]\) have affine form, so
\[
c=\kappa a+h(b),\qquad \kappa\ne0.
\]
If either \(r\) or \(p\) is constant, the required common
coordinate is already available.

Otherwise select a root \(\alpha\) of \(p\). The
root-specialization lemma makes
\[
b+r(\kappa\alpha+h(b))u^n
\]
a plane coordinate. But \(b+k(b)u^n\) is a plane coordinate
only when \(k\) is constant. Indeed, any root \(\beta\) of a
nonconstant \(k\) gives the nontrivial factorization
\[
b+k(b)u^n-\beta
=(b-\beta)\left(1+\frac{k(b)}{b-\beta}u^n\right).
\]
A coordinate minus a constant cannot factor this way.

Thus \(r(\kappa\alpha+h(b))\) is constant. Since \(r\) is
nonconstant, degree of composition forces \(h\) to be constant.
Both coefficients depend on the same base coordinate, as
claimed. Conversely, that common-coordinate form gives the
explicit triangular inverse written at the start.

When exactly one exponent equals one, the fixed-surface
argument still makes the coefficient of that linear variable
univariate after a base change. The root lemma and Maubach's
univariate-coefficient criterion finish coordinate descent,
including repeated roots.[^4] This branch does not require
\(C\) to be a plane coordinate.

The complete proof and independent reconstruction are
[the family theorem](research/double-binomial-pass.md) and
[its audit](research/double-binomial-independent-audit.md).

## 5. A quartic showing that compatibility is essential

Consider
\[
F_0=b+(a+b)^2u^2+a^2z^2.
\]
Both fixed-surface polynomials are coordinates, but in
different base directions. The polynomial also has no critical
point. Its derivatives satisfy the exact identity
\[
1=(F_0)_b\bigl(2-(F_0)_b\bigr)+2u^3(F_0)_u.
\]

Nevertheless \(F_0\) is not stable. At \(a=0\), the root
remainder \(b+b^2u^2\) fails the plane-coordinate criterion.
There is also a direct numerical topological obstruction:
for every \(\lambda\ne0\),
\[
\chi\bigl(F_0^{-1}(\lambda)\bigr)=-3.
\]
To see this, take the quotient by \(z\mapsto-z\). Its closed
curve at \(a=0\), parameterized by \(v=bu\), is
\[
b=\lambda-v^2,\qquad u=\frac{v}{\lambda-v^2},
\]
an affine line with two points removed. The quotient has Euler
characteristic \(-1\), while its branch surface is an affine
plane. The double-cover formula gives \(2(-1)-1=-3\).

This is a counterexample to a proposed proof shortcut, not to
cancellation. It prevents replacing the compatibility step
with smoothness plus coordinatehood of the two fixed surfaces.

There is a separate boundary control when one exponent is one:
\[
a^2z+(1+ab)u^2+b+ab^2
\]
is a coordinate by the root criterion, but
\(b+ab^2\) is not a plane coordinate. Therefore the stronger
base classification cannot be extended unchanged to that case.

For the remaining boundary \(n=q=1\), the published two-linear
theorem directly turns an irreducible smooth integrally acyclic
zero hypersurface into a coordinate. Stability supplies those
hypotheses. This closes the boundary without assuming that
every affine-three-space fibration is algebraically trivial.[^10]
The [two-linear source comparison](research/two-linear-literature-audit.md)
records the exact theorem.

## 6. Low-degree surface fibers

The binomial-fiber theorem also completes this deduction:
if \(G\in\mathbb C[x,y,z]\) has degree at most three and
general smooth rationally acyclic fiber, then \(G\) is a
coordinate. This is an absolute coordinate statement, not
a relative one preserving a specified variable.

For degree \(d\ge3\), a smooth fiber of Euler characteristic
one forces
\[
J(G_d)\cap V(G_{d-1})\ne\varnothing
\quad\text{in }\mathbb P^2.
\]
Otherwise its projective closure is a smooth degree-\(d\)
surface, whose boundary is a reduced plane curve. The
Euler and polar-degree formulas give
\[
\chi\ge1+(d-1)^2(d-2)>1,
\]
a contradiction.[^5][^6] An independent derivation bounds
the boundary Euler characteristic by \(d+1\), using
normalization and its connected incidence graph.

A point in that intersection supplies a linear direction
in which \(G\) has degree at most \(d-2\). For a cubic,
this makes it linear in one variable, so the binomial
result applies. Quadratics are handled by rank: without
a nonzero linear term on the radical, their generic
Euler characteristics are \(2,0,2\) in ranks one, two,
and three, respectively.

For quartics the output is only
\[
G=A(x,y)u^2+B(x,y)u+C(x,y),
\quad \deg A\le2,\ \deg B\le3,\ \deg C\le4.
\]
The intermediate term is not removed by a general
polynomial square completion. This is a reduction, not
a quartic classification. See
[Low-degree surface fibers](research/low-degree-surface-fibers.md).

## 7. What the remaining topological methods do establish

For a critical-point-free \(G:\mathbb C^3\to\mathbb C\)
with reduced leading homogeneous form, the singularities
at infinity are fiberwise isolated. If its general
fiber is rationally acyclic, the Siersma–Tibăr formulas
make it a bouquet of zero two-spheres, hence contractible.
Their description of atypical values gives no
bifurcations, so every fiber is contractible.[^7]
This eliminates finite homology torsion in that branch.

It does not identify an arbitrary contractible fiber
algebraically with \(\mathbb A^2\). The reduced-leading
hypothesis is also essential to this particular
deduction: replacing a nonreduced leading polynomial
by its reduced support changes its Jacobian locus.

The original Siersma–Tibăr author preprint explicitly asks
whether isolated singularity behavior at infinity together
with \(\mu=\lambda=0\) forces coordinatehood.[^12]
This locates the historical distinction between the
topological theorem and the desired algebraic conclusion.
It does not establish the present open status of that
question or of its narrower FISI case. See the
[exact source comparison](research/fisi-coordinate-gap-audit.md).

Without that hypothesis, the integral vanishing-cycle
analysis gives more constraints but no contradiction.
Writing \(A=H_1(Y;\mathbb Z)\) for the finite homology
of a general fiber, \(A_i\) for special fibers, and
\(m_i\) for monodromy, the source exact sequence and
the previously proved order formula yield
\[
A=\bigoplus_iV_i,\qquad
\operatorname{im}(m_i-1)=V_i,\qquad
A_i\simeq\ker(m_i-1).
\]
These are a deduction using the star decomposition and
exact sequence of Dimca and Némethi.[^8] Nonzero formal
finite-group models satisfy the resulting conditions,
including the change-of-coefficient constraints.
They have not been realized by a polynomial map.

The original slice supplies a product with a family of
finite cyclic actions. A separate formal conjugacy
argument makes that family constant after completion
at each parameter value. Formal conjugacy does not
give global transport on a noncompact affine fiber:
the series \(z/(1-\tau z)\) is formally invertible but
has a pole somewhere on every nonzero parameter fiber.
Averaging a complete slice field can likewise destroy
completeness. Thus these constructions do not prove
constancy of the fixed-surface homology.

The precise arguments are in
[the integral vanishing-cycle note](research/integral-vanishing-cycle-pass.md),
[the cyclic-family note](research/cyclic-family-rigidity-pass.md), and
[the quartic source audit](research/quartic-acyclic-fiber-literature.md).

## 8. Attribution and verification

The closest checked published statements include
Kaliman–Zaidenberg's binomial-surface theorem,
Das–Dutta's field and relative extensions of Wright's
theorem, KVZ's residual-variable result, and Das's
relative cancellation theorem.[^1][^9][^10][^11]
The relative results require an already established
polynomial quotient or coordinate property over the
specified base ring. Absolute stability in four
variables does not supply that premise.

The [statement-level audit](research/double-binomial-literature-audit.md)
records five exact comparisons. It does not establish
priority or the absence of a matching result elsewhere.

All **225 test methods across seventeen suites pass**.
The new suite contains seventeen exact checks of
coordinate inverses, derivative identities, quotient
lifting, root-residue matrices, and degree/Euler
arithmetic. Tests are finite supporting evidence, not
a verification of general topology or a formalization
of the mathematical theorems.

To reproduce the new suite from this directory, run
the executable command below. The full list of suites
and their scopes is in the README and experiment
manifest.

~~~sh
/opt/anaconda3/bin/python verify_two_power_slices.py
~~~

The remaining task is specific: either find a valid
structural reduction of an arbitrary original slice,
or prove a further family theorem without assuming
the required relative coordinates or global control
at infinity. In particular, \(xu^2+G(x,y,z)\) for an
arbitrary remainder is not settled by the present
two-power theorem. The all-linear two-term case is
covered by the published result cited above.

## Sources

[^1]: Shulim Kaliman and Mikhail Zaidenberg,
[*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076v2),
1998 preprint, Section 7, especially Lemmas 7.4–7.6,
Proposition 7.1, and Theorem 7.2.

[^2]: Carlos Florentino and Jaime Silva,
[*Hodge-Deligne polynomials of character varieties of free abelian groups*](https://arxiv.org/pdf/1711.07909),
2017 preprint, Section 4.2, equation (5) and Proposition 4.3.

[^3]: Peter Symonds,
[*Smith theory for algebraic varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf),
Algebraic & Geometric Topology 4 (2004), 121–131,
Section 4, Corollary 4.3 and Remark (1).

[^4]: Stefan Maubach,
[*The commuting derivations conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf),
author-hosted paper, Corollary 4.2 and Theorem 4.5.

[^5]: Laurentiu Maxim, Laurentiu Păunescu and Mihai Tibăr,
[*Vanishing cohomology and Betti bounds for complex projective hypersurfaces*](https://www.numdam.org/item/10.5802/aif.3486.pdf),
Annales de l'Institut Fourier 72 (2022), 1705–1731,
equations (1.3) and (3.11).

[^6]: June Huh,
[*Milnor numbers of projective hypersurfaces with isolated singularities*](https://arxiv.org/pdf/1210.2690),
2012 preprint, Section 1.1, polar-degree identity.

[^7]: Dirk Siersma and Mihai Tibăr,
[*Deformations of polynomials, boundary singularities and monodromy*](https://arxiv.org/pdf/math/0207076),
2002 preprint, Definition 2.1, equations (2.1)–(2.4),
and the equivalence following (3.1).

[^8]: Alexandru Dimca and András Némethi,
[*On the monodromy of complex polynomials*](https://arxiv.org/pdf/math/9912072v2),
Section 2.3, Lemma 2.4, Theorem 3.1, and equation (E).

[^9]: Prosenjit Das and Amartya K. Dutta,
[*Planes of the form b(X,Y)Z^n-a(X,Y) over a DVR*](https://arxiv.org/pdf/2002.02118),
2020 preprint, Theorems 4.5 and 6.2.

[^10]: Shulim Kaliman, Stéphane Vénéreau and Mikhail Zaidenberg,
[*Simple birational extensions of the polynomial ring C[3]*](https://arxiv.org/pdf/math/0104204),
2001 preprint, Theorems 3.24 and 4.27.

[^11]: Prosenjit Das,
[*On cancellation of variables of the form bT^n-a over affine normal domains*](https://arxiv.org/pdf/2002.02129),
2020 preprint, Theorem 3.4.

[^12]: Dirk Siersma and Mihai Tibăr,
[*Singularities at infinity and their vanishing cycles*](https://webspace.science.uu.nl/~siers101/inftyST.pdf),
author preprint of the Duke Mathematical Journal 80 (1995),
771–783 paper, page 10, unnumbered question between
Remark 5.7 and Corollary 5.8.
