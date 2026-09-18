# Recognition when the full primitive plinth divisor is reduced and smooth

In the actual degree-two independent-defect residual, a squarefree
primitive plinth with smooth zero scheme forces the intrinsic
threefold to be affine three-space. The proof first removes the
second-image obstruction, then gives explicit polynomial generators
for the resulting quadratic hypersurface.

The hypothesis concerns the full plinth polynomial, not merely its
reduced support. It does not settle singular, intersecting or
nonreduced plinth divisors.

## 1. Exact inputs and statement

Keep the actual setting of the
[second-image criterion](second-image-gluing-pass46.md):
\[
A[s_*]\simeq\mathbb C^{[4]},\qquad
C=\ker D\simeq\mathbb C^{[2]},\qquad
\operatorname{pl}(D)=pC,\qquad Dr=p,
\tag{1}
\]
where \(D\ne0\) is primitive. The actual inclusion \(C\subset A\)
is faithfully flat and factorially closed. The degree-two
independent-defect hypotheses have supplied every quadratic divisor
model and the image ideal \(I_2=pJ\). In particular, this note
does not assert that an arbitrary sliced action has this setup.

The following established inputs are used.

- The [flat-conic/topology gate](flat-conic-topology-gate-pass47.md)
  puts \(\operatorname{Supp}(C/J)\) in the singular locus of the
  full plane divisor \(p=0\).
- If \(J=C\), the actual minimal slice extends to the global
  quadratic presentation proved in the second-image criterion.
- The [intrinsic monodromy theorem](quadratic-monodromy-pass46.md)
  makes the normalization of every retained plinth component an
  affine line. The degree-two cover of that normalization is a
  degree-two polynomial map from another affine line. Its quadratic
  function-field extension therefore has exactly one finite odd
  valuation, as well as the odd valuation at infinity.

**Theorem.** Under these actual hypotheses, if \(p\) is squarefree
and \(V(p)\subset\operatorname{Spec}C\) is smooth, then
\(A\simeq\mathbb C^{[3]}\).

If \(p\) is a unit, a constant multiple of \(r\) is a slice
of \(D\), and the slice theorem directly gives \(A=C^{[1]}\).
Henceforth \(p\) is nonconstant.

## 2. The invariant plinth lines are parallel in a plane coordinate system

The singular locus in the first input is empty, so \(J=C\).
Consequently
\[
A=C[r,Y],\qquad pY=r^2+ar+b,\qquad a,b\in C,
\tag{2}
\]
with the displayed equation the exact presentation, not just a
relation in a larger algebra. Replacing \(r\) by \(r+a/2\)
gives, with the new variable again denoted by \(r\),
\[
A=C[r,Y]/(pY-r^2-d),\qquad d=b-a^2/4\in C.
\tag{3}
\]
Here and below this quotient notation uses polynomial indeterminates
on the presentation side.

Because \(V(p)\) is smooth and reduced, its irreducible components
are disjoint smooth curves. Each equals its normalization, so the
third input identifies it with \(\mathbb A^1\). The
Suzuki–Abhyankar–Moh embedding theorem gives coordinates
\(u,v\) of the actual invariant plane for which one component
is \(u=0\). Its exact complex-field statement is directly given
in Vistoli's primary new proof.[^ams]

On another component, the function \(u\) never vanishes, so it
is a unit of that component's ring \(\mathbb C[t]\). It is
therefore a nonzero constant \(a_i\). The component is a
one-dimensional closed irreducible subset of the line \(u=a_i\),
and hence is that entire line. Distinct components have distinct
constants. Absorb the constant unit of \(p\) into \(Y\); then
\[
C=\mathbb C[u,v],\qquad
p=P(u)=\prod_{i=1}^k(u-a_i),\qquad
A=\mathbb C[u,v,r,Y]/(P(u)Y-r^2-d(u,v)).
\tag{4}
\]
No assertion that \(u\) is an ambient coordinate of the original
four-variable polynomial ring has been used.

## 3. Smoothness removes square factors from each residue polynomial

Put \(d_i(v)=d(a_i,v)\). Suppose \(d_i\) has a repeated root
\(v_0\), or is identically zero. Since \(P'(a_i)\ne0\), the
point
\[
u=a_i,\quad v=v_0,\quad r=0,\quad
Y=\frac{d_u(a_i,v_0)}{P'(a_i)}
\tag{5}
\]
lies on the hypersurface (4) and annihilates all four partial
derivatives of its equation. In the identically zero case any
\(v_0\) works. This contradicts smoothness of \(A\), which
is inherited from the polynomial cylinder. Thus every \(d_i\)
is a nonzero squarefree polynomial.

At the generic point of \(u=a_i\), the full residue ring of
(4) is
\[
\mathbb C(v)[r,Y]/(r^2+d_i(v)).
\tag{6}
\]
Its constant field is the actual nontrivial degree-two extension
\(\mathbb C(v)(\sqrt{-d_i(v)})\). The coordinate \(v\) is
a coordinate on the retained affine line. The monodromy input
says this extension has exactly one finite odd valuation. Every
root of the squarefree polynomial \(d_i\) contributes one, and
a nonzero constant would make the extension trivial over
\(\mathbb C(v)\). Consequently
\[
d_i(v)=A_i v+B_i,\qquad A_i\in\mathbb C^*,\quad B_i\in\mathbb C.
\tag{7}
\]
This argument uses the full residue field and its retained cover,
not a choice of a rational square root or an unproved extension
of generic coordinates across the divisor.

## 4. An explicit global polynomial inverse

Interpolate polynomials \(A_0(u),B_0(u)\) with values
\(A_i,B_i\) at the distinct \(a_i\). The Chinese remainder
theorem, applied coefficientwise in \(v\), gives
\[
d(u,v)=A_0(u)v+B_0(u)+P(u)h(u,v).
\tag{8}
\]
Set \(Y'=Y-h(u,v)\). Equation (4) becomes
\[
P Y'=r^2+A_0v+B_0.
\tag{9}
\]
All \(A_i\) are nonzero, so \(\gcd(P,A_0)=1\) in
\(\mathbb C[u]\). Choose \(\alpha,\beta\in\mathbb C[u]\)
with \(\alpha P+\beta A_0=1\), and define
\[
W=P Y'-A_0v,\qquad Z=\beta Y'+\alpha v.
\tag{10}
\]
This is a determinant-one linear change over \(\mathbb C[u]\),
with exact inverse
\[
Y'=\alpha W+A_0Z,\qquad v=-\beta W+PZ.
\tag{11}
\]
The only defining equation is now \(W=r^2+B_0(u)\).
Eliminating \(W\) proves
\[
\boxed{\quad A=\mathbb C[u,r,Z].\quad}
\tag{12}
\]
Conversely (11), \(W=r^2+B_0\), and \(Y=Y'+h(u,v)\)
recover every original generator polynomially. This verifies the
algebraic recognition, rather than only birationality or an
isomorphism after inverting \(P\).

## 5. Scope, source access and finite controls

The algebra in Sections 3–4 also proves a useful conditional
statement: a smooth global hypersurface of the form (4), with
squarefree \(P\) and the stated nontrivial one-branch quadratic
residue covers, is polynomial. The original-cylinder hypotheses
are used to obtain that global presentation and its cover geometry.

Smooth reduced support alone is insufficient for this proof when
the full plinth has repeated factors. Then the flat-conic critical
locus need not be empty and the division by \(P'(a_i)\) in
(5) is unavailable. No conclusion is asserted for those cases,
for intersecting components or for the unrestricted cancellation
problem. No historical novelty or formal verification is claimed.

The companion [exact checker](smooth_plinth_recognition_checks_pass47.py)
is limited to finite CRT reconstruction, determinant-one changes
and both inverse directions modulo the equation, plus repeated-root
singularity and repeated-plinth boundary controls. It does not test
the universal embedding or monodromy theorems.
The first complete run passed all three methods in 0.861 seconds,
with exit status zero and no failed assertions. The checker imports
only `unittest` and SymPy and uses exact arithmetic.

[^ams]: Angelo Vistoli, *On the minimal normal compactification of a
    polynomial in two variables*, [arXiv:math/9904035v3](https://arxiv.org/pdf/math/9904035v3),
    2 August 1999, page 2: the complex Suzuki–Abhyankar–Moh theorem
    and its proof; supporting Theorem 1 and its complete proof are
    on pages 2–4. These passages and the full paper were directly
    read. The original Abhyankar–Moh 1975 article and Suzuki 1974
    article receive the historical credit; their original full
    texts were not accessed in this bounded check.
