# Independent audit of the double-binomial family

The proposed implication is valid for the stated family. Let

\[
F=A(x,y)u^n+B(x,y)z^q+C(x,y),\qquad
0\ne A,B\in\mathbb C[x,y],\quad n,q\ge2.
\]

Then the following conditions are equivalent:

1. \(F\) is a stable coordinate.
2. \(F\) is a coordinate of \(\mathbb C[x,y,u,z]\).
3. There are base coordinates \((a,b)\) of \(\mathbb C[x,y]\)
   and nonzero univariate polynomials \(r,p\) such that
   \(C=b\), \(A=r(a)\), and \(B=p(a)\).

The substantive direction uses the general-level binomial theorem
proved in [the companion audit](generic-rational-binomial-pass.md),
Smith theory, finite-quotient rational cohomology, and a root-by-root
Gysin calculation. No assertion about arbitrary polynomial slices is
needed or established. This is a deduction from the cited inputs, not
a novelty claim.

## 1. The two fixed sets give compatible base coordinates

If \(F\) is stable, every fiber \(X_\lambda=\{F=\lambda\}\)
is smooth and contractible. Indeed, its product with some affine
space is an affine space.

For a prime divisor \(\ell\) of \(n\), let \(\mu_\ell\)
multiply \(u\) and fix the other variables. Its fixed set on
\(X_\lambda\) is

\[
Y^B_\lambda=\{B(x,y)z^q+C(x,y)=\lambda\}.
\]

Smith theory makes this fixed set mod-\(\ell\) acyclic, hence
rationally acyclic. It is smooth: at \(u=0\), the differential
of \(F\) is the differential of the displayed three-variable
polynomial, since \(n\ge2\). The same argument interchanging
\(u,z\) makes every fiber of \(A(x,y)u^n+C(x,y)\) smooth and
rationally acyclic. The ordinary-cohomology Smith statement used here
is recorded in Symonds, Section 4, Corollary 4.3 and its following
remark.[^smith]

For exponent at least two, the companion binomial theorem supplies
the simultaneous form \((f,g)=(p(a),b)\), not just absolute
coordinatehood of \(fz^q+g\). Applying it twice gives base
coordinate pairs \((a,b)\) and \((a',b)\) with

\[
b=C,\qquad B=p(a),\qquad A=r(a').
\tag{1}
\]

The constant-coefficient cases are included in that theorem. In
particular, even if both \(A\) and \(B\) are constants, \(C\)
is a plane coordinate. A constant \(C\) would also contradict
smoothness directly at \(u=z=0\).

An automorphism of the one-variable polynomial algebra
\(\mathbb C[b][a]\) over \(\mathbb C[b]\) is affine in \(a\).
Its leading coefficient is a unit of \(\mathbb C[b]\), hence a
nonzero constant. Therefore

\[
a'=\kappa a+h(b),\qquad
\kappa\in\mathbb C^*,\quad h\in\mathbb C[b].
\tag{2}
\]

If \(p\) is constant, use the coordinates \((a',b)\): both
coefficients are then functions of \(a'\). If \(r\) is constant,
use \((a,b)\). These cases already give condition 3. Assume from
now on that \(p,r\) are nonconstant.

### Audit of the binomial input

The relevant primary statement is KZ Lemma 7.5 under rational, not
integral, acyclicity. It gives the simply connected components of
\(V(f)_{\mathrm{red}}\) and the Euler characteristic of
\(V(g-\lambda)\). At a general level, transversality makes those
components smooth. The generic components of the \(g\)-fiber have
equal Euler characteristic by transitive monodromy; total Euler
characteristic one therefore forces one affine line. These facts
give the simultaneous base-coordinate form in (1). The use of a
general level, and the distinction between \(q=1\) and \(q>1\),
are essential. KZ Lemmas 7.4--7.6 and Proposition 7.1 were checked
in the original text.[^kz]

## 2. The cyclic quotient is smooth and rationally acyclic

In the coordinates (1)--(2), put

\[
R(a,b,u)=b+r(\kappa a+h(b))u^n,
\qquad J(a,b,u,W)=p(a)W+R(a,b,u).
\tag{3}
\]

The quotient of \(X_\lambda\) by the action \(z\mapsto\zeta z\)
of \(\mu_q\) is exactly \(Z_\lambda=\{J=\lambda\}\), with
\(W=z^q\). In characteristic zero, taking invariants commutes with
the quotient by this invariant equation. More explicitly, if an
invariant polynomial is a multiple of \(F-\lambda\), its quotient
is invariant because the polynomial ring is a domain. Thus the
invariant ring is

\[
\mathbb C[a,b,u,W]/(p(a)W+R(a,b,u)-\lambda).
\]

There is no need to infer smoothness from a general assertion about
finite quotients. If \(J\) had a critical point \((a,b,u,W)\),
choose any \(z\) with \(z^q=W\). The equality

\[
F=J(a,b,u,z^q)
\]

and the chain rule would make the lifted point critical for \(F\).
Consequently every \(Z_\lambda\) is smooth.

A finite-group quotient of a complex algebraic variety has rational
cohomology equal to the invariant rational cohomology of the source.
One may see this using an equivariant triangulation, or by proper
base change for the finite quotient map and exactness of the
invariant functor over \(\mathbb Q\). This assertion allows fixed
points. Hence

\[
H^*(Z_\lambda;\mathbb Q)
\cong H^*(X_\lambda;\mathbb Q)^{\mu_q}
\cong H^*(\mathrm{point};\mathbb Q).
\tag{4}
\]

Only rational acyclicity of the quotient is used. Integral
acyclicity and contractibility of a finite quotient are not assumed.
KZ's proof of Lemma 7.4(a) uses the same finite-quotient rational
acyclicity principle in the three-variable binomial case.[^kz]

## 3. The residue matrix forces one affine line at every root

The following lemma is useful independently. Let

\[
J=p(a)W+R(a,b,u),\qquad 0\ne p\in\mathbb C[a].
\]

Assume a general fiber \(Z_\lambda\) is smooth and rationally
acyclic. For every root \(\alpha\) of \(p\), the polynomial
\(R_\alpha(b,u)=R(\alpha,b,u)\) is a plane coordinate.

To prove this, write \(\alpha_1,\ldots,\alpha_d\) for the
distinct roots. Choose \(\lambda\) outside the finite union of
the exceptional sets of the nonconstant \(R_{\alpha_i}\), and
different from the values of the constant ones. The latter contribute
empty strata for this choice. On the complement of these root strata,
the equation uniquely solves for \(W\), giving

\[
U=Z_\lambda\setminus\{p(a)=0\}
\cong (\mathbb C\setminus\{\alpha_1,\ldots,\alpha_d\})
\times\mathbb C^2.
\tag{5}
\]

For a nonempty root stratum, set

\[
E_i=\{a=\alpha_i\}\cap Z_\lambda
=C_i\times\mathbb C_W,
\qquad C_i=\{R_{\alpha_i}(b,u)=\lambda\}.
\]

The \(C_i\) are smooth curves, possibly disconnected before using
acyclicity. The nonempty \(E_i\) are disjoint smooth divisors. The
function \(a-\alpha_i\) vanishes to order exactly one on each
component of \(E_i\): at a point of \(E_i\), one of the
\(b,u\) derivatives of \(R_{\alpha_i}\) is nonzero, so the
implicit function theorem makes \(a\) a local coordinate on
\(Z_\lambda\). This remains true for repeated roots of \(p\).

The ordinary rational Gysin sequence gives

\[
0=H^1(Z_\lambda)\longrightarrow H^1(U)
\xrightarrow{\operatorname{res}}H^0(E)
\longrightarrow H^2(Z_\lambda)=0,
\tag{6}
\]

and

\[
H^2(U)=0\longrightarrow H^1(E)
\longrightarrow H^3(Z_\lambda)=0,
\tag{7}
\]

where \(E=\coprod_i E_i\). Let \(\omega_i\) be the
normalized winding class of \(a-\alpha_i\), a basis of
\(H^1(U;\mathbb Q)=\mathbb Q^d\). If \(C_i\) has
\(c_i\) components, its block of the residue matrix is

\[
\operatorname{res}(\omega_j)|_{E_i}
=\begin{cases}(1,\ldots,1)\in\mathbb Q^{c_i},&i=j,\\
0,&i\ne j.
\end{cases}
\tag{8}
\]

This explicit matrix matters. An empty root stratum would give a
zero column and violate injectivity in (6); two or more components
over a root would violate surjectivity. Thus every \(c_i=1\).
Equation (7) then gives \(H^1(C_i;\mathbb Q)=0\) individually.
Each \(C_i\) is a connected smooth affine curve, so it is
\(\mathbb A^1\).

Plane-line rectification makes \(R_{\alpha_i}\) a coordinate:
the chosen fiber is reduced and irreducible, so its defining
polynomial becomes a nonzero constant times a coordinate minus a
constant, not a higher power. This proves the lemma.

The proof neither estimates only total Betti numbers nor assumes in
advance that every root has a nonempty connected stratum. Equation
(8) supplies those conclusions, with the required multiplicity check.

## 4. The root restriction removes the incompatible shear

Choose a root \(\alpha\) of the nonconstant polynomial \(p\).
The lemma applied to (3)--(4) makes

\[
L(b,u)=b+d(b)u^n,\qquad
d(b)=r(\kappa\alpha+h(b)),
\tag{9}
\]

a plane coordinate. Such a polynomial can be a coordinate only if
\(d\) is constant.

Indeed, suppose \(d\) is nonconstant and let \(\beta\) be a
root. Choose \(\lambda\) outside the finite root set of \(d\).
On the affine-line fiber \(L=\lambda\), the function
\(b-\beta\) has no zero, because \(b=\beta\) would give
\(L=\beta\ne\lambda\). It is therefore a unit in the
coordinate ring of \(\mathbb A^1\), hence a constant. Thus
\(b=\gamma\) is constant on the whole fiber. If \(d(\gamma)=0\),
the equation gives \(\lambda=\gamma\), contradicting the chosen
level. If \(d(\gamma)\ne0\), the equation leaves only finitely
many values of \(u\), contradicting that the fiber is an affine
line. This proves that \(d\) is constant. The converse is immediate,
and the same elementary criterion works for every positive exponent.

There is also a shorter algebraic check at the level \(\beta\):

\[
L-\beta=(b-\beta)
\left(1+\frac{d(b)}{b-\beta}u^n\right).
\]

Both factors are nonunits when \(d\) is nonconstant, whereas a
coordinate minus a constant is irreducible. The quotient displayed
here is a polynomial because \(d(\beta)=0\).

Since \(r\) is nonconstant, constancy of
\(r(\kappa\alpha+h(b))\) implies constancy of \(h\): a
composition of two nonconstant polynomials has positive degree.
Therefore \(A\) and \(B\) are both polynomials in \(a\), and
condition 3 follows. Finally,

\[
(a,b,u,z)\longmapsto
(a,b+r(a)u^n+p(a)z^q,u,z)
\]

is a triangular automorphism with inverse obtained by subtracting
the two summands. This proves condition 3 implies condition 2; the
remaining implication is immediate.

## 5. A quartic negative control for separate fixed-plane tests

The polynomial

\[
F_0=b+(a+b)^2u^2+a^2z^2
\tag{10}
\]

is critical-point-free. Its \(u\) derivative is
\(2(a+b)^2u\); whenever this vanishes, either \(u=0\) or
\(a+b=0\), and in either case its \(b\) derivative is one.
Both fixed-set polynomials are coordinates:

\[
F_0|_{u=0}=b+a^2z^2,
\qquad F_0|_{z=0}=b+c^2u^2,\quad c=a+b.
\]

Consequently both fixed sets in every fiber are affine planes.
Nevertheless \(F_0\) is not stable. Its cyclic quotient is

\[
J_0=a^2W+b+(a+b)^2u^2.
\]

At \(a=0\), the curve on a nonzero level is
\(C_\lambda=\{b+b^2u^2=\lambda\}\). Put \(v=bu\).
Then

\[
b=\lambda-v^2,\qquad u=\frac{v}{\lambda-v^2},
\]

so \(C_\lambda\cong\mathbb A^1\setminus
\{\sqrt\lambda,-\sqrt\lambda\}\) and
\(\chi(C_\lambda)=-1\). The \(a\ne0\) stratum of the
\(J_0\)-fiber is \(\mathbb C^*\times\mathbb C^2\), of
Euler characteristic zero, and its \(a=0\) stratum is
\(C_\lambda\times\mathbb C\). Hence
\(\chi(J_0^{-1}(\lambda))=-1\).

The double cover from the \(F_0\)-fiber is branched along the
affine plane \(\{z=0,F_0=\lambda\}\). Additivity and
multiplicativity on the unramified complement give

\[
\chi(F_0^{-1}(\lambda))
=2\chi(J_0^{-1}(\lambda))-1=-3
\qquad(\lambda\ne0).
\tag{11}
\]

Thus the two fixed-plane conditions and submersivity do not by
themselves imply stability or coordinatehood. The additional quotient
acyclicity used in (4) is a real hypothesis, not a consequence of
those separate tests.

## 6. Exponent-one scope

If one exponent is one and the other is at least two, stable
coordinatehood still follows from the established univariate linear
coefficient theorem. For example, when \(q=1\), the fixed
\(u=0\) polynomial \(Bz+C\) has general rationally acyclic
fibers. The exponent-one binomial argument makes
\(B=p(a)\) after a base automorphism, although it need not make
\(C\) a plane coordinate. The original \(F\) then has a
univariate coefficient of its linear variable \(z\), so the
[univariate criterion](multiple-root-linear-pass.md) applies.

The stronger simultaneous form in condition 3 does not extend to
this exponent-one branch. For example,

\[
u^2+xz+y+xy^2
\]

is a coordinate, by first replacing \(z\) with \(z+y^2\).
But \(C=y+xy^2\) is not a plane coordinate: a nonzero fiber is
\(\mathbb C^*\), parametrized by \(y\ne0\) and
\(x=(\lambda-y)/y^2\).

The equivalence in the opening statement therefore retains exactly
the hypothesis \(n,q\ge2\). None of these arguments reduces an
arbitrary four-variable slice to the displayed separated-power form.

## Sources

[^smith]: Peter Symonds, [*Smith Theory for algebraic
varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf),
Section 4, Corollary 4.3 and the following remark. This is the
ordinary-cohomology fixed-point input, not a claim that fixed sets
are contractible.

[^kz]: Shulim Kaliman and Mikhail Zaidenberg, [*Affine modifications
and affine hypersurfaces with a very transitive automorphism
group*](https://arxiv.org/pdf/math/9801076v2), Lemmas 7.4--7.6 and
Proposition 7.1. The application to a general rationally acyclic
binomial fiber, including constants, is proved separately in
[the binomial note](generic-rational-binomial-pass.md).
