# A smooth factorial control with a nonprincipal second image ideal

A primitive locally nilpotent derivation on a smooth factorial
threefold can have a faithfully flat polynomial kernel, principal full
plinth and free second degree module, but a nonprincipal second image
ideal. This example has an explicit image ideal in every degree.
Its closed fiber also shows why scheme structure cannot be discarded
in a scalar-residue test.

The example is not contractible and is not stably polynomial. It is
a control against deductions from weaker intrinsic hypotheses, not a
counterexample to cancellation or to a theorem using an actual
polynomial four-cylinder.

## 1. The algebra and its genuine additive action

Put \(C=\mathbb C[u,v]\), and define
\[
A=C[z,w]/\bigl((uz+vw)^2+2w-v\bigr),\qquad r=uz+vw.
\tag{1}
\]
Define
\[
Du=Dv=0,\qquad Dz=1+vr,\qquad Dw=-ur.
\tag{2}
\]
Then \(Dr=u\), so the defining relation has derivative
\(2ur-2ur=0\). Moreover
\[
D^2z=uv,\quad D^2w=-u^2,\qquad D^3z=D^3w=0.
\tag{3}
\]
Leibniz expansion on the generators proves local nilpotence on all
of \(A\). Its actual flow is
\[
z\mapsto z+t(1+vr)+uvt^2/2,\qquad
w\mapsto w-urt-u^2t^2/2,
\tag{4}
\]
fixing \(u,v\) and taking \(r\) to \(r+ut\). The inverse has time
\(-t\).

Eliminating \(w\) gives the exact alternative presentation
\[
A=C[r,z]/(2uz-vr^2-2r+v^2),\qquad w=(v-r^2)/2.
\tag{5}
\]
Conversely \(r=uz+vw\) recovers (1); the maps are inverse modulo
the displayed relations. Inverting \(u\) gives
\[
A_u=\mathbb C[u,u^{-1},v,r],\qquad
z=(vr^2+2r-v^2)/(2u),\qquad D=u\partial_r.
\tag{6}
\]

## 2. Smoothness, factoriality and the exact kernel

Let \(F(v,r)=vr^2+2r-v^2\). The polynomial
\(-F=v^2-r^2v-2r\) is monic quadratic in \(v\), with discriminant
\[
\Delta(r)=r^4+8r=r(r^3+8).
\tag{7}
\]
It has four simple roots and is not a square in \(\mathbb C(r)\).
Gauss's lemma makes \(F\) irreducible. Thus \(u\) is prime in \(A\),
with
\[
A/uA=(\mathbb C[v,r]/(F))[z].
\tag{8}
\]
The relation in (5) is itself primitive and linear in \(z\) over
\(\mathbb C[u,v,r]\), so is prime and gives a domain. Since (6)
is a UFD and \(u\) is prime, Nagata's criterion makes \(A\) a
UFD.[^nagata]

The curve \(F=0\) is smooth. Its critical equations imply
\(vr=-1\) and \(r^2=2v\), hence \(v^3=1/2\); the equation
\(F=0\) would instead give \(v^3=-1\). A singular point of (5)
would have \(u=z=0\) and be singular on this curve. Thus \(A\)
is smooth. Also \(A^*=\mathbb C^*\): a unit maps in (6) to a
constant times \(u^k\), and primality of \(u\) excludes \(k\ne0\)
for a unit in \(A\).

The kernel of \(D\) lies in \(\mathbb C[u,u^{-1},v]\), by (6).
A member with a minimal positive \(u\)-pole cannot belong to \(A\):
its numerator would reduce to a nonzero polynomial in \(v\)
vanishing in (8), impossible since \(F\) has positive \(r\)-degree.
Consequently
\[
\ker D=C.
\tag{9}
\]
The derivation is primitive. Its values on the generators in (5)
include \(u\) and \(1+vr\), whose gcd in \(A\) is one because
\(1+vr\) is nonzero modulo the prime \(u\). This is a gcd
statement, not a unit image-ideal statement.

## 3. Direct faithful flatness over the kernel

The defining polynomial
\(G=2uz-vr^2-2r+v^2\in C[r,z]\) has unit coefficient \(-2\)
on \(r\). Multiplication by \(G\) is injective on \(M[r,z]\)
for every \(C\)-module \(M\).

Here is the elementary primitive-polynomial argument. In one variable,
suppose a polynomial \(f\) with unit coefficient ideal annihilates a
nonzero module polynomial \(h\), and choose such an \(h\) of least
degree. Multiplying \(h\) by the leading coefficient of \(f\)
gives an annihilated polynomial of smaller degree, so is zero.
Descending through the product coefficients now shows successively
that every coefficient of \(f\) kills all of \(h\). Their unit
ideal would kill \(h\), a contradiction. In several variables,
a sufficiently separated Kronecker substitution turns a proposed
finite annihilating product into a one-variable product, without
merging relevant monomials or changing the coefficient ideal.

Tensor the free resolution
\[
0\longrightarrow C[r,z]\xrightarrow{\,G\,}C[r,z]
\longrightarrow A\longrightarrow0
\]
with an arbitrary \(C\)-module. The injectivity above gives
\(\operatorname{Tor}_1^C(A,M)=0\) for every \(M\); thus \(A\)
is \(C\)-flat. Every base-prime fiber is nonzero, since its relation
remains nonconstant with \(r\)-coefficient \(-2\). Flatness is
therefore faithful.

A closed fiber at \((u_0,v_0)\) is a line if \(u_0\ne0\), and
is again a line if \(u_0=v_0=0\). Otherwise it is a degree-two
\(r\)-algebra tensored with a polynomial \(z\)-line, possibly
nonreduced but always nonempty and purely one-dimensional.
No free basis of the entire \(C\)-module \(A\) is inferred.

## 4. The entire actual degree filtration

Use the conventions
\[
\mathcal F_n=\ker D^{n+1},\qquad
I_n=D^n(\mathcal F_n)\subset C\qquad(n\ge0).
\tag{10}
\]
Give \(r,z\) weights \(1,2\) over the degree-zero ring \(C\),
and let \(G_n\) be the induced quotient filtration. Initial forms
multiply in \(C[r,z]\), so the initial ideal of the principal
defining ideal is generated by \(2uz-vr^2\). Hence
\[
\operatorname{gr}_G A=C[R,Z]/(2uZ-vR^2).
\tag{11}
\]
The relation in (11) is primitive and linear in \(Z\), hence
prime. This graded ring is a domain; in particular \(u\) is a
nonzero divisor of degree zero.

Multiplication by \(u^k\) therefore does not lower the degree of
a nonzero element of \(A\). Equivalently, \(G\) is \(u\)-saturated.
After inverting \(u\), (6) identifies the quotient filtration
with ordinary \(r\)-degree, also the \(D=u\partial_r\) degree.
Injectivity into \(A_u\) and this saturation give
\[
\boxed{\quad
\mathcal F_n=G_n=\sum_{i+2j\le n} C\,r^iz^j.
\quad}
\tag{12}
\]
This is a module equality in the actual algebra, not merely a
generic spanning statement.

For \(i+2j=n\), the highest \(r\)-coefficient of \(r^iz^j\)
is \((v/(2u))^j\), so its \(n\)-th derivative is
\(n!u^{n-j}v^j/2^j\). Lower-weight monomials have zero \(n\)-th
derivative. Nonzero complex factors are units; (12) gives the exact
all-degree image formula
\[
\boxed{\quad
I_n=\sum_{j=0}^{\lfloor n/2\rfloor}Cu^{n-j}v^j
    =u^{\lceil n/2\rceil}(u,v)^{\lfloor n/2\rfloor}.
\quad}
\tag{13}
\]

## 5. Free low-degree modules and the nonprincipal image

Equation (12) gives \(\mathcal F_1=C\oplus Cr\), so
\[
\operatorname{pl}(D)=I_1=uC,\qquad Dr=u.
\tag{14}
\]
This is the full plinth. For degree two, (12) gives
\(C+Cr+Cr^2+Cz\). Since \(r=uz+vw\) and \(r^2=v-2w\),
\[
\mathcal F_2=C\oplus Cz\oplus Cw.
\tag{15}
\]
Independence follows from (6): relative to \(1,r,r^2\), the
coefficient matrix of \(1,z,w\) has determinant \(-1/(2u)\).
Thus \(\mathcal F_2\) is free of rank three, but
\[
\boxed{\quad I_2=(uv,-u^2)=u(u,v).\quad}
\tag{16}
\]
This is not principal: its gcd is \(u\), while it is a proper
subideal of \(uC\).

The inclusion \(\mathcal F_1\subset\mathcal F_2\) sends \(r\)
to the vector \((0,u,v)\) in (15), and
\[
0\longrightarrow\mathcal F_1\longrightarrow\mathcal F_2
\xrightarrow{\,D^2\,}u(u,v)\longrightarrow0.
\tag{17}
\]
At the origin the two nonconstant entries vanish. Free modules
in this filtration do not imply locally free image ideals.
Every \(I_n\) with \(n\ge2\) is nonprincipal. Its extra defect
beyond its height-one gcd is supported only at \((u,v)\);
all height-one localizations are principal.

## 6. Closed fibers and the scheme-theoretic distinction

At \((u,v)=(0,0)\), the actual fiber is \(\mathbb C[z]\), with
\(w=r=0\) and \(\bar Dz=1\). The minimal local slice becomes
scalar even though the closed-fiber action is nonzero and sliced.
This agrees with the proper ideal \(I_2/u=(u,v)\) there.

At \((u,v)=(0,-1)\), set \(\epsilon=r-1\). The actual fiber is
\[
\mathbb C[z,\epsilon]/(\epsilon^2),\qquad
\bar r=1+\epsilon,\qquad \bar Dz=-\epsilon.
\tag{18}
\]
The element \(\epsilon\) is nonzero. Thus \(r\) is not scalar
in the scheme-theoretic fiber, although it is scalar on its reduction.
Here \(I_2/u\) is locally the unit ideal because \(v\) is a unit.
Discarding nilpotents would give the wrong scalar test.

The fixed locus of \(D\) consists of three disjoint reduced
lines: its equations give \(u=0\), \(v^3=-1\), \(r=-1/v\),
with \(z\) arbitrary. In particular \(D\) is not fixed-point free.

For the divisor model, invert \(v\) and put
\[
T=r+1/v,\qquad Z_0=2z/v,\qquad \eta=(1+v^3)/v^2.
\]
The exact equation and action are
\[
uZ_0=T^2-\eta,\qquad DT=u,\qquad DZ_0=2T.
\tag{19}
\]
This is the standard quadratic DVR model at the generic prime
\((u)\). Its residue square class is \(1+v^3\), not a single
linear factor. These coordinates invert \(v\) and are not global
coordinates at \((u,v)\).

## 7. The obstruction to a polynomial cylinder

Let \(\Sigma=\{F(v,r)=0\}\). Its projection to the \(r\)-line is
a finite double cover with four simple branch points, by (7).
Additivity and multiplicativity of compactly supported Euler
characteristic give[^euler]
\[
\chi_c(\Sigma)=2(1-4)+4=-2.
\tag{20}
\]
The open chart (6) is \(\mathbb C^*\times\mathbb A^2\), of
Euler characteristic zero; its complement is
\(\Sigma\times\mathbb A^1\). Consequently
\[
\chi_c(\operatorname{Spec}A)=-2.
\tag{21}
\]
For this smooth complex threefold, Poincare duality equates ordinary
and compactly supported Euler characteristics. It is not contractible.
Multiplying by affine space leaves (21) unchanged, whereas every
complex affine space has Euler characteristic one. Therefore
\[
A^{[N]}\not\simeq\mathbb C^{[N+3]}\qquad(N\ge0).
\tag{22}
\]
Stable polynomiality is false here, not merely unproved.

## 8. Scope and verification boundary

This actual algebra has smooth factorial total space, constant units,
a primitive LND, a faithfully flat polynomial kernel, principal full
plinth, free \(\mathcal F_1,\mathcal F_2\), and standard quadratic
generic-divisor presentation. These properties do not force principal
image ideals, and a nonzero closed-fiber action does not force the
minimal local slice to remain nonscalar.

The algebra fails the topological and polynomial-cylinder hypotheses
of the original problem. It does not realize an unresolved actual
coordinate-partial frame on \(\mathbb C^4\). The all-degree filtration
is proved through (11)--(13), not extrapolated from finite tests.
The flatness argument is supplied in full, and the Euler computation
uses the actual branched cover and open/closed decomposition.
No historical novelty or proof-assistant verification is claimed.

The standalone checker
[second_image_countercontrol_checks_pass47.py](second_image_countercontrol_checks_pass47.py)
passed all five methods on its first run in 0.209 seconds, with exit
zero. It reconstructs both presentation maps, the actual action and
flow inverse, bounded image degrees zero through eight, the free
second-module basis and nonreduced fiber, and the localized divisor
coordinates and fixed scheme. These finite controls do not replace
the universal filtration, flatness, factoriality or topology proofs.

[^nagata]: Stacks Project, [Lemma 10.120.7, Nagata's criterion for factoriality](https://stacks.math.columbia.edu/tag/0AFU). The full statement and proof were directly read. Here the ring is Noetherian, the localization is (6), and the single inverted element is prime by (7)--(8).

[^euler]: S. Cappell, L. Maxim and J. Shaneson, [Euler Characteristics of Algebraic Varieties](https://people.math.wisc.edu/~lmaxim/Euler.pdf), *Communications on Pure and Applied Mathematics* 61 (2008), 409–421, Section 2, printed page 410. This page was directly read for closed/open additivity, multiplicativity for locally trivial fibrations, and the Poincare-duality comparison. It supplies the standard Euler-characteristic mechanism, not the construction of this example.
