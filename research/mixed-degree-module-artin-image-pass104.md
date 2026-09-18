# Every degree-two residue is Artin-valued on the actual mixed fiber

At an actual collapsed mixed (2,1) fiber with nonzero speed normal,
every element killed by N cubed has parameter-independent residue on
the whole nonreduced fiber. This extends the result for the specified
slice difference h in102 to the entire degree-two module.

Its residue space has dimension either two or three. In the
three-dimensional case, the degree-module map is injective on the
fiber, and its zero N-action yields stronger base-order bounds with
either first normal action. These conclusions do not exclude the
mixed fiber or supply a cubic presentation of the full algebra.

## 1. Actual mixed-fiber hypotheses

Retain the actual nonconical quadratic frame, the canonical
\(u=Ez/q_0\), and the whole-fiber hypotheses of
[actions100](quadratic-whole-fiber-actions-pass100.md) and
[rigidity102](quadratic-degree-module-fiber-rigidity-pass102.md).
In particular
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\quad E=\partial_u,
\quad E^2x_i=0,\quad E^2z=q_0\in\mathbb C^*,\\
N\in\operatorname{LND}(A)\setminus\{0\},\quad
S=\ker N=\mathbb C[s_1,s_2],\quad S\longrightarrow A
\text{ faithfully flat},\quad A_K=K[v],\\
\mathfrak m\subset S\text{ closed},\quad L(\mathfrak m)\ne0,
\quad A/\mathfrak mA=\mathcal D[c],\quad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\\
e_1=G^2,\quad e_2=1-G^2,\quad \epsilon=G-G^2,\quad
\bar N=(\lambda\epsilon+\rho e_1)\partial_c,
\quad\lambda,\rho\in\mathbb C^*,\\
F_n=\ker(N^{n+1}:A\longrightarrow A),\quad
G,h,\mathbf a\in F_2,\quad c\in F_4.
\end{gathered}
\tag{1}
\]
Here K is the fraction field of S. G is the actual centered second good normal, not a newly
chosen Artin generator; \(\mathbf a=x_{\rm tr}-u\mathbf b\)
is the centered original good column. In the double factor,
G is epsilon and epsilon squared is zero; in the simple factor,
G is one and epsilon is zero. Thus the two factors of the
whole fiber are \(\mathbb C[c,\epsilon]/(\epsilon^2)\) and
\(\mathbb C[c]\).

The exact fiber algebra, derivation, constant coefficients and
original normal chart are substantive actual inputs from99--102.
They are not consequences of faithful flatness alone. All original
coordinates in the retained construction have polynomial inverses.
We do not replace them by a proposed coordinate tuple.

Let R=S_m and \(\mathfrak r=\mathfrak mR\). The elementary theorem102
makes each \((F_n)_R\) free of rank n+1. In particular the image of
F2 in the whole fiber has complex dimension at most three. The
image of its localization is the same vector space, because every
base denominator outside m reduces to a nonzero complex scalar.

## 2. A degree-two element is constant on both reduced components

Take any U in F2 and write its whole-fiber residue as
\[
\bar U=
\bigl(a(c)+\epsilon\beta(c),\ b(c)\bigr)
\quad\text{in }
\mathbb C[c,\epsilon]/(\epsilon^2)\times\mathbb C[c].
\tag{2}
\]
If a is nonconstant, (1) gives
\(\overline{NU}=\lambda\epsilon a'(c)\ne0\) in the generic
Artinian double fiber. The general cyclic-module lemma in
[cyclic103](noncollapsed-cyclic-degree-module-pass103.md),
Section 2, applies to this actual U in ker N cubed. Its proof
does not require U to be an original good combination. It would
make the entire fiber a single dual-number affine line. That
contradicts the actual simple companion in (1). Therefore a is
constant.

Moreover N squared vanishes on every element of the double factor
in (1). Since \(N^2U\in S\), its value at m is the same scalar
on both components and must be zero. On the simple factor this
says \(\rho^2b''(c)=0\), so b is affine.

Suppose b is nonconstant. Then \(1,G,U,NU\) all belong to F2,
and their whole-fiber residues are linearly independent. Indeed,
in a putative relation, the coefficient of c on the simple
component first kills the U coefficient. The constant part on
the double then kills the coefficient of 1. Its nilpotent part
kills the coefficient of G. Finally NU is a nonzero constant
on the simple component and zero on the double, killing its
coefficient. This gives four independent images of a rank-three
module, a contradiction. Thus both a and b are constants.

## 3. The remaining nilpotent coefficient cannot depend on c

Subtract the actual element \(a+(b-a)G\) from U and call the
result W. Its residue is zero on the simple component and has
the form \(\epsilon\gamma(c)\) on the double. We prove gamma
constant, retaining either first normal action.

Assume gamma is nonconstant. The three residues
\(1,G,W\), when projected to the double, are
\(1,\epsilon,\epsilon\gamma(c)\), and are linearly independent.
The free rank-three module theorem and Nakayama therefore give
an actual basis \((F_2)_R=R\oplus RG\oplus RW\).
Its reduction map to the whole fiber is injective, and N kills
all three residues by (1). Thus N maps this module into
\(\mathfrak r(F_2)_R\).

The exact intrinsic conic construction of102 applies to this
basis without using the origin of W as a slice difference.
For completeness, extend 1 to a basis 1,r0 of the free rank-two
module F1, subtract its constant term, and write
\[
\begin{gathered}
r_0=a_0G+b_0W,\quad \gcd_R(a_0,b_0)=1,\\
NG=\theta b_0r_0+B_1,\qquad
NW=-\theta a_0r_0+B_2,\qquad
Q=\theta r_0^2-2B_2G+2B_1W\in R,\\
B_1,B_2,\theta a_0^2,\theta a_0b_0,\theta b_0^2,Q
\in\mathfrak r,\qquad
B_1,B_2,Q\in\mathfrak r^2.
\end{gathered}
\tag{3}
\]
The quotient F2/F1 embeds in R under N squared, so it is
torsion-free and gives the coprimality. Comparing coefficients
in Nr0 gives the displayed theta formulas; theta is not assumed
to be a unit. Differentiating Q gives zero. Its coefficients
are in r because the whole-fiber matrix of N is zero, and
faithful flatness contracts Q into r.

To obtain the last three square memberships, use
\(\mathfrak r A_R/\mathfrak r^2 A_R
=(\mathfrak r/\mathfrak r^2)\otimes_{\mathbb C}(A/\mathfrak mA)\).
For each first base coefficient in the conic, project to the
double. There G squared, GW and W squared vanish. Independence
of \(1,\epsilon,\epsilon\gamma(c)\) then kills each coefficient
of B1, B2 and Q. This is a first-coefficient argument in the
flat whole algebra, not a general fiber-purity premise.

Use the actual weighted normal chart from
[volume-normal99](quadratic-volume-normal-splitting-pass99.md).
It has \(\operatorname{wt}x=2\), \(\operatorname{wt}y=1\),
y=G, and constant nonzero transverse coefficient. The leading
operator is \(D_*=\gamma_0x\partial_y+\lambda_0y\partial_c\),
where \(\lambda_0\ne0\) is constant and gamma0 is a constant
that vanishes exactly for zero first normal action. The
order-one part of W is \(\gamma(c)y\). Indeed its difference
from \(\gamma(c)(G-G^2)\) belongs to the whole ideal mA,
whose elements have weight at least two in this local chart;
the extra G squared term also has weight two.

If gamma0 is nonzero, the coefficient of x squared in
\(D_*^3(\gamma(c)y)\) is
\(3\gamma_0^2\lambda_0\gamma'(c)\). The actual identity
N cubed of W equals zero forces it to vanish. Strictly higher
operator and function weights cannot cancel it. Thus gamma
would be constant, a contradiction.

If gamma0 is zero, the actual leading term of NW has weight
two and is \(\lambda_0\gamma'(c)y^2\). But (3) gives
\(NW=B_2-\theta a_0^2G-\theta a_0b_0W\) of weight at least
three: B2 is in the base square, and the other coefficients
are in the base maximal ideal. This is again a contradiction.
Therefore gamma is constant in either case.

## 4. Exact residue-space dichotomy

Combining Sections 2--3 proves
\[
\boxed{\quad
\mathcal W:=\operatorname{im}(F_2\longrightarrow A/\mathfrak mA)
\subseteq\mathcal D,\qquad
\mathcal W=\mathbb C\,1+\mathbb C\,G
\quad\text{or}\quad\mathcal W=\mathcal D.
\quad}
\tag{4}
\]
The two alternatives have dimensions two and three. Both 1 and
G lie in the image and are independent. Since D has dimension
three, these exhaust the possibilities. In particular every
actual centered good generator and h is Artin-valued, but the
statement covers all degree-two elements, not just that finite
generating list.

The larger alternative holds if and only if some degree-two
element has a nonzero coefficient of G squared in its unique
Artin representative. A nonzero such coefficient for h is one
sufficient condition; it is not asserted to be necessary.

## 5. Stronger orders in the three-dimensional alternative

Suppose \(\mathcal W=\mathcal D\). Three independent Artin
residues form an R-basis of F2, so its fiber map is injective.
As N annihilates D, we obtain
\[
\begin{gathered}
(F_2)_R\cap\mathfrak rA_R=\mathfrak r(F_2)_R,\qquad
N((F_2)_R)\subseteq\mathfrak r(F_2)_R,\\
\boxed{\quad N^2((F_2)_R)\subseteq\mathfrak r^2.\quad}\\
N^2h\in\mathfrak m^2S,\qquad
N^2\mathbf a\in(\mathfrak m^2S)^3,\qquad
N^2F\in\mathfrak m^3S.
\end{gathered}
\tag{5}
\]
For the boxed line, N kills R, so iterating the preceding
inclusion gives N squared of F2 inside r squared times F2.
It is also invariant. Contracting from A_R to R by faithful
flatness puts it in r squared. The global elements in the next
line then belong to the indicated powers of m in S, because
\(\mathfrak m^jS_{\mathfrak m}\cap S=\mathfrak m^j\): every
denominator outside m is already a unit modulo that finite
local quotient.

The final assertion uses the exact original-volume identity
\(F=(L(\mathfrak m)-L)\cdot\mathbf a+\kappa-\kappa(\mathfrak m)\).
N annihilates its base coefficients. Thus
\(N^2F=(L(\mathfrak m)-L)\cdot N^2\mathbf a\), and the first
factor has base order at least one. These order improvements
do not require the first normal action to be nonzero. That
distinguishes this conditional rank-three result from the
earlier nonzero-first-normal bounds101.

The specified degree-four generator satisfies, in the same
alternative,
\[
\boxed{\quad
N^2c\in\mathfrak r(F_2)_R,\qquad
N^3c\in\mathfrak r^2(F_2)_R,\qquad
N^4c\in\mathfrak m^3S.
\quad}
\tag{6}
\]
Indeed N squared of c belongs to F2 and vanishes on the whole
fiber by (1), so the injective reduction gives the first
membership. Apply N twice more, using (5); the last element
is invariant because N to the fifth of c is zero. The same
contraction gives its stated global base order.

## 6. The cubic-generation step remains separate

The residue theorem and these order bounds use actual original
geometry. In particular the double-residue exclusion invokes
the actual cyclic103 gate, and the nilpotent-coefficient exclusion
uses the constant transverse coefficient and original volume99.
They are not proved from flatness and module ranks alone.

Even in the rank-three alternative, no argument above supplies
a first-degree generator whose residue generates all of D, or
a third-degree element restricting to a component parameter.
The specified c is only known to belong to F4. For example,
knowing G in F2 and c in F4 puts their product in F6, not in
F4. The five-dimensional rank of F4 alone cannot turn a
proposed list involving Gc into its basis. This is a precise
missing multiplication/generation premise for an attempted
cubic normal form, not an assertion that such a form is false.

The intrinsic all-e mixed family in
[frontier103, Section 6](adic-and-cyclic-conic-frontier-pass103.md)
already has F2 equal to S0 plus S0y plus S0y squared, with
whole residue space D and a genuine mixed fiber. It has no
hidden degree-two component parameter. It remains an intrinsic
polynomial algebra, not a verified original nonconical E-frame.
That existing control prevents interpreting (4) as an exclusion
or a frame-realization claim; no new control or numerical method
is introduced here.

The sector L(m)=0 and the two-dimensional alternative in (4)
do not inherit the rank-three order statements. The proof does
not make N squared of any of these elements zero, establish a
global coordinate, or recognize A. All files through103 remain
unchanged. The argument uses the linked retained proofs; no new
primary-source theorem or external review is claimed.
