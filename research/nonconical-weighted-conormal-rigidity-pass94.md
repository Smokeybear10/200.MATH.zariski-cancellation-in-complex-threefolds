# Weighted conormal rigidity beyond double fibers

For a collapsed, generically rank-one fixed component in the actual
quadratic frame, the constant conormal row-or-column conclusion
holds at every whole-fiber multiplicity. The double-fiber proof93
used ordinary normal order. Weighting the first base parameter by
the fiber multiplicity recovers the decisive coefficient when
that ordinary-order coefficient vanishes.

The filtration used below is constructed from the actual local
fiber equation. It is not an additional hypothesis on the full
algebra or the older filtration from pass54. The conclusion remains
second-order vanishing, not invariance or recognition.

## 1. Actual centered generators and local coordinates

Retain the quadratic nonconical frame and a collapsed, generically
rank-one fixed component from
[conormal-layer93](nonconical-collapsed-conormal-layer-pass93.md).
Write \(\mathfrak q\subset A\) for its prime. The actual cylinder
and invariant centers satisfy
\[
\begin{gathered}
B=A[u]=\mathbb C[X,Y,W,z],\qquad
\mathfrak qB=\mathfrak P=(X,Y),\qquad A/\mathfrak q=\mathbb C[\bar c],\\
F=X-uEX,\quad G=Y-uEY,\qquad
\mathfrak q=(F,G)A,\qquad N^3F=N^3G=0.
\end{gathered}
\tag{1}
\]
The coordinates X,Y,W are affine-linear combinations of the original
three good coordinates. In particular their second E-derivatives
vanish. The ideal equality and the N-degree bounds are inherited
actual statements, not assumptions about a freely chosen Jacobian
field.

Put \(O=A_{\mathfrak q}\), \(\mathfrak n=\mathfrak qO\) and
\(L=\mathbb C(c)\subset O\). Every nonzero polynomial in c is
outside \(\mathfrak q\), and this actual subfield maps isomorphically
onto the residue field \(\mathbb C(\bar c)\). Choose a constant
linear change of base coordinates such that
\(x=s_1-s_1(m)\) has nonzero ambient differential at the generic
point. Choose a second regular parameter y and put
\(f=s_2-s_2(m)\). As in
[curvilinear-action93](nonconical-curvilinear-fiber-action-pass93.md),
\[
\begin{gathered}
dx,dy,dc\text{ form a basis of }\Omega_{O/\mathbb C},\qquad
N=\epsilon(f_y\partial_c-f_c\partial_y),\quad \epsilon\in O^*,\\
Nx=0,\qquad
\mu=\operatorname{length}_O O/(x,f)\ge2,\qquad
f\bmod x=a(c)y^\mu+\text{higher powers of }y,\quad a\ne0.
\end{gathered}
\tag{2}
\]
The coefficients in the last expansion are taken after completion.
The dual derivations in (2) are actual O-derivations before completion.
The coefficient field L is not N-invariant.

The given coefficient field and parameters identify
\(\widehat O=L[[x,y]]\). Here is the precise gate: the continuous
map from this power-series ring, sending its variables to the actual
parameters, is surjective by successive approximation. The regular
associated-graded ring is \(L[x,y]\), so the least nonzero ordinary
homogeneous term of a series cannot map to zero. This also proves
injectivity. It is the coefficient-compatible power-series
description in Stacks 0C0S(2), not an arbitrary new coefficient
field choice.[^complete]

## 2. A weight forced by the fiber equation

Assign weight \(\mu\) to x, weight one to y and weight zero to
L. Write \(\mathcal F_{\ge j}\) for the series whose monomials
have weight at least j. Positive weights make this filtration
equivalent to the maximal-ideal topology. Coefficient differentiation
by c preserves weight. The three actual dual derivations extend
continuously to the completion and become the corresponding
series derivations.

The DVR order in (2) excludes every pure-y term of degree below
\(\mu\). All terms containing x, other than its linear term,
have weight strictly greater than \(\mu\). Consequently
\[
\begin{gathered}
f=\alpha(c)x+a(c)y^\mu+f_{>\mu},\qquad
\epsilon=\epsilon_0(c)+\epsilon_{>0},\qquad \epsilon_0a\ne0,\\
N(\mathcal F_{\ge j})\subset\mathcal F_{\ge j+\mu-1},\\
D_*=\bigl(\gamma x+\rho y^\mu\bigr)\partial_y
          +\lambda y^{\mu-1}\partial_c,\qquad
\gamma=-\epsilon_0\alpha',\quad
\rho=-\epsilon_0a',\quad \lambda=\mu\epsilon_0a\ne0 .
\end{gathered}
\tag{3}
\]
D_* is the operator induced by N on this weighted associated
graded ring. A prime denotes differentiation in c. Indeed
\(\partial_y\) lowers weight by at most one, while
\(\partial_c\) preserves it. The terms omitted from each
coefficient in (3) strictly increase the indicated weight shift.
For example a term proportional to x in \(Nc\) has weight
\(\mu\), not the leading weight \(\mu-1\).

Thus successive leading operators compose: for
\(H\in\mathcal F_{\ge j}\), the component of weight
\(j+3(\mu-1)\) in \(N^3 H\) is \(D_*^3\) applied to
the weight-j component of H. This assertion needs neither local
nilpotence on the completed ring nor a separate finite-degree
description of all of A.

Write the independent first normal terms of the actual centers as
\[
F\equiv p(c)x+b(c)y,\qquad
G\equiv r(c)x+e(c)y\pmod{\mathfrak n^2},\qquad pe-br\ne0.
\qquad
D_*^3(by)=D_*^3(ey)=0.
\tag{4}
\]
Since \(\mu\ge2\), the weight-one components are precisely by
and ey. Every remaining term, including the displayed x terms,
has weight at least two. The last equalities follow from (1)
and (3). If b or e is zero, the corresponding equality is simply
zero; at least one is nonzero by the determinant condition.

## 3. The coefficient that survives at every multiplicity

The coefficient calculation is entirely within the polynomial
ring \(L[x,y]\). For any \(b=b(c)\), put
\[
\begin{gathered}
A_b=b\gamma,\qquad B_b=b\rho+b'\lambda,\\
D_*(by)=A_bx+B_by^\mu,\\
D_*^2(by)=C_bxy^{\mu-1}+D_by^{2\mu-1},\\
C_b=\lambda A_b'+\mu\gamma B_b,\qquad
D_b=\lambda B_b'+\mu\rho B_b .
\end{gathered}
\tag{5}
\]
Only the first summand on the third line can contribute to
\(x^2y^{\mu-2}\) after one more derivative. Therefore
\[
\begin{aligned}
[x^2y^{\mu-2}]D_*^3(by)
&=(\mu-1)\gamma C_b\\
&=b(\mu-1)\gamma(\lambda\gamma'+\mu\gamma\rho)
  +(\mu^2-1)b'\lambda\gamma^2 .
\end{aligned}
\tag{6}
\]
The monomial is valid for every \(\mu\ge2\), including
\(\mu=2\). Multiply this identity for b by e, subtract the
identity for e multiplied by b, and use (4). If \(\gamma\ne0\),
then \(\lambda\ne0\) and the characteristic-zero scalar
\(\mu^2-1\ne0\), giving
\[
eb'-be'=0.
\tag{7}
\]
When b and e are both nonzero, their ratio is a rational
function of c with derivative zero, hence a complex constant.
When exactly one vanishes, their line is already a constant
coordinate line. The excluded case b=e=0 would contradict (4).

## 4. Return to the actual polynomial component

Let \(C(c)\) be the polynomial first coefficient matrix of the
two base parameters in F,G from conormal-layer93. In the local
parameters x,y those first terms are \((x,\alpha(c)x)^t\).
The column \((b,e)^t\) spans the kernel of C. If
\(\gamma\ne0\), (7) therefore makes this kernel a constant
line, so C has a constant row direction.

If \(\gamma=0\), (3) gives \(\alpha'=0\), hence
\(\alpha\in\mathbb C\). The image line of C is then the
constant line \((1,\alpha)^t\). We obtain
\[
\boxed{\quad
\mu\ge2:\qquad
C=\ell(c)\rho_0
\quad\text{or}\quad C=\ell_0\rho(c),
\quad}
\tag{8}
\]
with the indicated nonzero row or column constant. These are
polynomial identities on the entire component: a fixed nonzero
constant entry recovers the other factor from the polynomial
entries of C. The initial constant base change preserves both
constancy assertions.

The first-layer identities \(M=B_0C\), \(CM=0\) and the local
Jacobian calculation of conormal-layer93 now give, exactly as
in the final double-fiber proof93,
\[
\boxed{\quad
\exists L_0\in\mathfrak P\text{ nonzero affine-linear good normal}:
\quad EL_0\in\mathfrak P^2,\quad
N(L_0-uEL_0)\in\mathfrak q^2,\quad
N^3(L_0-uEL_0)=0.
\quad}
\tag{9}
\]
There is no hypothesis on the rank of the constant matrix B_0.
In the constant-row case choose \(L_0=\rho_0(X,Y)^t\).
In the constant-column case every centered generator has
N-image in \(\mathfrak q^2\), and the first-layer argument
supplies the E-speed condition.

The global ideal membership can also be checked by primary
contraction: \((X,Y)^2\) is \(\mathfrak P\)-primary in the
original polynomial ring, and
\(\mathfrak q^2=(X,Y)^2\cap A\) since \(B=A[u]\).
Thus membership at the generic prime suffices in this actual
linear-plane setting. Nothing asserts that generic membership
in an arbitrary ideal would suffice.

## 5. Scope, deduplication, and controls

For \(\mu=2\), the scalar \(\mu^2-1\) is three and (6)
recovers the previously audited product-rule coefficient.
For higher multiplicities the ordinary first normal coefficient
used there vanishes, but the weighted monomial in (6) survives.
The ordinary-order boundary in the frozen pass93 proof is not
being silently reinterpreted.

The algebraic calculation works for every integer \(\mu\ge2\).
Actual quadratic-frame multiplicities also obey the independent
total bound and topology of pass92; this note constructs none
of those fibers. It does not extend to uncollapsed components,
generic quotient rank zero, or arbitrary chosen generators with
no actual degree-two identities.

Second-order vanishing remains weaker than invariance. The
retained intrinsic control \(D=p\partial_y-2y\partial_c\),
\(f_0=p+y^2\), still has \(Df_0=2py\ne0\),
\(Df_0\in(p,y)^2\), and \(D^3f_0=0\). Thus (9) does not
provide a common invariant coordinate or exclude the component.

The [standalone checker](weighted_conormal_checks_pass94.py)
has one method with multiplicity subtests \(\mu=2,3,4\).
It checks the weighted coefficient, Wronskian cancellation,
strict higher-weight perturbations and the two successive
coefficients of \(D_*^3y\). A deliberately incorrect scalar
is rejected by an exact specialization. These are formal
operator controls, separate from the all-multiplicity written
derivation (5)--(7) and the actual local hypotheses.

The first author execution of
`/opt/anaconda3/bin/python research/weighted_conormal_checks_pass94.py`
passed its one method in 0.587 seconds, exit zero, with complete
output retained as chunk `45f5db`. No assertion failed in that
execution. The checker imports only unittest and SymPy; it does
not import the solver, earlier checkers or proof scripts.
No old full-filtration hypothesis, action realization, universal
recognition, frozen-file change, or historical novelty claim
is added.

[^complete]: The Stacks Project,
    [Lemma 10.160.10(2), tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S).
    Its complete displayed statement and proof were freshly read.
    The given-field compatibility is essential. The argument here
    also describes the graded approximation directly using the
    retained regular-local associated-graded theorem; it does not
    claim a fresh proof of every Cohen-structure dependency.
