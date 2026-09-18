# Cubic rank-zero fibers constrain the leading quadratic pencil

At a collapsed rank-zero component of multiplicity five or six,
the independent-quadratic sector has a precise leading model.
After constant changes of the two base equations and a polynomial
normal-frame change over the component line, the quadratic initials
are P squared and P times Q. The induced polynomial LND is a
nonzero constant times P squared times the derivative in c.
The normal-frame matrix and its inverse have c-degree at most three.

This is a statement on the actual normal associated-graded ring.
It neither conjugates the full derivation on A nor excludes the
fiber. Proportional quadratic initials have a separate boundary
described below.

## 1. An actual polynomial leading derivation

Retain the actual cubic nonconical frame, a generically rank-zero
closed-fiber component with prime \(\mathfrak q\), and its
[collapsed plane92](nonconical-collapsed-component-plane-pass92.md).
Use the original affine-linear good normal coordinates X,Y and
their invariant centers F,G. The retained generic degree bound
on centered good coordinates and on c gives
\[
\begin{gathered}
\mathfrak qB=(X,Y),\qquad B=A[u],\qquad
F=X-uEX,\quad G=Y-uEY,\quad \mathfrak q=(F,G)A,\\
A/\mathfrak q=\mathbb C[\bar c],\qquad
\operatorname{gr}_{\mathfrak q}A
 =\mathbb C[c,\xi,\eta],\qquad
\deg\xi=\deg\eta=1,\quad\deg c=0,\\
N^4F=N^4G=0,\qquad N^7c=0 .
\end{gathered}
\tag{1}
\]
The symbols \(\xi,\eta\) are the normal classes of F,G, not new
coordinates of A. The ideal is an actual regular sequence, so
its associated-graded ring has the displayed form. The original
linear-plane ideal also makes every \(\mathfrak q^j\) primary:
it is the contraction of \((X,Y)^j\) from the polynomial
extension B. Thus the normal-order statements below, computed
at the generic component, contract back to the actual ideals.

Put \(f=s_1-s_1(m)\), \(g=s_2-s_2(m)\). Rank zero gives
\(f,g\in\mathfrak q^2\). Let \(\phi,\psi\) be their degree-two
normal classes, permitting a zero class. Their coefficients lie
in \(\mathbb C[c]\), not just \(\mathbb C(c)\).

The canonical Jacobian field N is defined using the original
volume and the actual base functions. Along the whole component,
\(dF,dG,dc\) are a differential basis. The ratio of their wedge
to the induced threefold volume is a polynomial in c without
zeros on the affine component line, hence a nonzero complex
constant \(\nu\). This is the same actual volume gate proved
in [column-classification94](nonconical-conormal-column-classification-pass94.md),
and does not require rank one. The local Jacobian calculation gives
\[
\begin{gathered}
N(\mathfrak q^j)\subset\mathfrak q^{j+2}\quad(j\ge0),\\
D=\nu\operatorname{Jac}_{\xi,\eta,c}(\phi,\psi,-),\qquad
D\phi=D\psi=0,\\
D^4\xi=D^4\eta=0,\qquad D^7c=0 .
\end{gathered}
\tag{2}
\]
For the order assertion, derivatives in a normal parameter lower
order by at most one, whereas differentiation in the actual
coefficient parameter c preserves it. Consequently NF,NG have
order at least three and Nc has order at least two. The unit
factor contributes only its constant normal class \(\nu\) to D.
Leibniz and primary contraction give the stated filtration shift.
Leading operators compose, so the degree identities in (1) give
the last line of (2).

In particular D is a polynomial LND on \(\mathbb C[c,\xi,\eta]\):
it is nilpotent on these three algebra generators, and the
Leibniz rule then proves local nilpotence on their polynomial
ring. This is not local nilpotence on \(\mathbb C(c)\) or on a
completed local ring. The operator has normal degree two and
can differentiate its coefficient parameter c.

## 2. The independent quadratic sector and the multiplicity gate

Write \(L=\mathbb C(c)\) and assume for now that \(\phi,\psi\)
are linearly independent over L. For homogeneous binary forms
of the same positive degree, zero binary Jacobian would make
their ratio have zero derivative on the projective coordinate,
hence be constant over L. Therefore
\[
D c=\nu\operatorname{Jac}_{\xi,\eta}(\phi,\psi)\ne0,
\qquad
\phi,\psi\text{ are algebraically independent over }L.
\tag{3}
\]
Suppose the actual generic whole-fiber length is \(\mu>4\),
so in the retained cubic list it is five or six. Then \(\phi\)
and \(\psi\) have a common linear factor over L.

Here is the exact length argument. Complete
\(A_{\mathfrak q}\) using its given coefficient field L.
If the two quadratic initials were coprime, their only leading
syzygies would be multiples of \((\psi,-\phi)\). Any leading
cancellation in a combination of f,g can thus be removed by
subtracting the corresponding multiple of \((g,-f)\), raising
the coefficient order. Iterating to any fixed order shows that
the initial ideal of \((f,g)\) is \((\phi,\psi)\). The graded
quotient of two coprime binary quadratics has Hilbert series
\((1+t)^2\), so its length is four. This contradicts \(\mu>4\).
The common factor has degree one because the quadratics are
L-linearly independent. No assertion about generators of a
cleared relative presentation is used here.

## 3. Homogeneous generators of the leading kernel

The quotient-plane theorem applies to the nonzero polynomial LND
D on the actual polynomial three-ring in (2). Thus
\(H=\ker D\simeq\mathbb C^{[2]}\). One precise published input
is Kaliman--Saveliev Corollary 2.8(2): its threefold here is
literally affine three-space, so smoothness, contractibility and
domination by a curve times an affine plane are immediate.[^kernel]
No free-action assertion is needed.

Since D is homogeneous and Dc is nonzero, H inherits the normal
grading and its degree-zero part is exactly \(\mathbb C\).
The positive-degree ideal is therefore a maximal ideal of the
polynomial plane H. Choose homogeneous elements P,Q giving a
basis of its two-dimensional cotangent space. Induction on
positive degree, or graded Nakayama, shows that they generate
the whole graded algebra. Algebraic independence follows from
its dimension. The two independent degree-two invariants in
(3) restrict their positive weights to
\[
H=\mathbb C[P,Q],\qquad
(\deg P,\deg Q)\in\{(1,1),(1,2),(2,2)\},
\tag{4}
\]
after interchanging P,Q if necessary.

The pair (2,2) is impossible. Normal negation
\((\xi,\eta,c)\mapsto(-\xi,-\eta,c)\) would fix H pointwise
and commute with D. On the generic translation field
\(\operatorname{Frac}(H)(t)\), with Dt=1, any such automorphism
sends t to t plus an element of \(\operatorname{Frac}H\).
Its order two makes that element zero in characteristic zero.
It would then be the identity on the whole fraction field,
contrary to its nontrivial action on \(\xi\). The generic
translation field is the usual local-slice construction for
the genuine polynomial LND D.

## 4. A common factor rules out weights one and two

If the weights were (1,2), the independent degree-two pair would
span \(\mathbb C P^2+\mathbb C Q\). A constant base change
would put \(\phi,\psi\) into P squared and Q. Their common
factor over L would then force P to divide Q in \(L[\xi,\eta]\).

The normal-linear polynomial P is primitive over \(\mathbb C[c]\).
Indeed any nonconstant factor depending only on c would itself
be killed by D, by factorial closure of an LND kernel. That
contradicts Dc being nonzero. Gauss's lemma now descends the
divisibility to \(\mathbb C[c,\xi,\eta]\). Write Q=PV there.
Then DV=0, and V is homogeneous of degree one. In the grading
(1,2), this means V is a complex multiple of P, contradicting
the independence of the kernel generators. Hence
\[
\mu>4,\ \phi,\psi\text{ L-independent}
\quad\Longrightarrow\quad H=\mathbb C[P,Q],
\qquad \deg P=\deg Q=1.
\tag{5}
\]
Both P and Q are linear in the two normal variables with
polynomial coefficients in c. Their coefficient matrix is
invertible over L: otherwise Q/P would belong to L; its
D-invariance and Dc nonzero would make that ratio complex
constant, again contradicting independence.

Now \(\phi,\psi\) are binary quadratic forms in P,Q with
complex coefficients. Their common factor over L is therefore
already a common complex linear factor in P,Q. Replacing the
homogeneous kernel basis and making a constant invertible change
of the two base equations gives
\[
\phi=P^2,\qquad\psi=PQ,\qquad
\binom P Q=M(c)\binom\xi\eta,
\qquad M\in\operatorname{Mat}_2(\mathbb C[c]),\quad
\det M\ne0.
\tag{6}
\]
For this displayed normal form, a constant determinant factor
from the change of base equations is absorbed in the scalar
of the Jacobian field below.

## 5. The leading normal frame is polynomial and degree bounded

Set \(D_0=\operatorname{Jac}(P,Q,-)\). The chain rule in (6)
and (2) gives D as a nonzero constant times \(P^2D_0\).
The multiplier is D0-invariant. Since D is locally nilpotent,
the identity \(D^j a=(\kappa P^2)^jD_0^j a\) in a domain
proves that D0 is locally nilpotent as well. But D0 preserves
\(\mathbb C[c]\), with \(D_0c=\det M(c)\). A nonzero LND
on this polynomial one-ring has a nonzero constant coefficient.
Consequently
\[
\boxed{\quad
M\in\operatorname{GL}_2(\mathbb C[c]),\qquad
D=\beta P^2\partial_c\text{ in the coordinates }P,Q,c,
\qquad\beta\in\mathbb C^*.
\quad}
\tag{7}
\]
The derivative here holds P,Q fixed. It does not hold the
original normal variables fixed. In these polynomial leading
coordinates, (2) also implies
\[
\boxed{\quad
\deg_c M\le3,\qquad \deg_c M^{-1}\le3,
\qquad D^2c=0.
\quad}
\tag{8}
\]
Indeed \((\xi,\eta)^t=M^{-1}(c)(P,Q)^t\). The fourth
D-derivative is \(\beta^4P^8\) times the fourth c-derivative
of this column. Independence of P,Q and characteristic zero
force all entries of the inverse matrix to have degree at most
three. A two-by-two matrix of constant nonzero determinant has
inverse given by its linear cofactors, so the same bound holds
for M. The assertion about c follows directly from (7).

## 6. Proportional quadratic initials have a separate boundary

Suppose instead that the two nonzero quadratic initials are
L-proportional. Write \(\phi=J\), \(\psi=r(c)J\), where J is
a homogeneous binary quadratic over L. The leading field is
\[
D c=0,\qquad
D=\nu r'(c)J\bigl(J_\eta\partial_\xi-J_\xi\partial_\eta\bigr).
\tag{9}
\]
If r is constant, this degree-two operator is zero and supplies
no condition; the same is true if one quadratic initial is zero.
If r is nonconstant, D remains nonzero and is L-linear. Its
local nilpotence extends after adjoining algebraic scalars to L.
A binary quadratic with two distinct linear factors becomes a
nonzero multiple of ab in linear coordinates. Its Hamiltonian
field is a nonzero multiple of \(a\partial_a-b\partial_b\).
Multiplication by the invariant ab cannot make its repeated
action on a vanish. This contradicts local nilpotence.

Thus J has a double linear factor. That line is defined over L:
a rank-one binary quadratic over a characteristic-zero field
has the form \(d(c)\ell^2\), with \(\ell\) L-linear. Formula
(9) then has a constant L-linear direction and coefficient
proportional to \(\ell^3\). It follows that
\[
\boxed{\quad
r\notin\mathbb C\quad\Longrightarrow\quad
J=d(c)\ell^2,\qquad D^2\xi=D^2\eta=0,
\qquad Dc=0.
\quad}
\tag{10}
\]
This kills c only for this particular leading operator. It
does not assert Nc=0 for the original derivation.

## 7. Exact controls and remaining scope

The bound in (8) is attainable for polynomial leading fields.
For example, take
\[
P=\xi,\qquad Q=\eta+c^3\xi,\qquad
D=\xi^2\partial_c-3c^2\xi^3\partial_\eta,
\qquad D^3\eta=-6\xi^7\ne0,\quad D^4\eta=0.
\tag{11}
\]
This is (7) with \(\beta=1\). It is a genuine polynomial LND
on the associated-graded three-ring, not an original inverse
frame or a construction of the exceptional fiber.

The shared initial pencil also does not determine the whole
fiber length or its higher-order equations. Over L the examples
\[
\operatorname{length}\frac{L[[x,y]]}{(x^2+y^3,xy)}=5,
\qquad
\operatorname{length}\frac{L[[x,y]]}{(x^2,xy+y^3)}=6
\tag{12}
\]
have the same independent quadratic pencil \((x^2,xy)\).
The bases are respectively \(1,x,y,y^2,y^3\) and
\(1,x,y,y^2,y^3,y^4\). These are Artinian controls only.
No compatible full original LND, kernel S, or coordinate
generation is being inferred from them.

The proof retains coefficient differentiation throughout and
never assumes that the known cleared equations generate the
full local ideal. The shared-factor conclusion uses the actual
length, while the polynomial leading model uses the actual
degree identities and the source-backed kernel-plane theorem.
If the degree-two operator is zero, higher normal terms remain
uncontrolled by this argument. Even in (7), the higher normal
terms of N need not share the displayed translation form.

The [standalone finite checker](cubic_quadratic_pencil_checks_pass95.py)
has one method. It verifies both polynomial normal-frame inverse
orders, the Jacobian multiplier, the sharp degree-three example,
and the failure of the fourth-derivative constraint for the
degree-four variant. Exact Groebner reduction checks both Artin
bases and their ideal-power ranks, retaining the nonhomogeneous
relations. None of these finite controls verifies the general
leading-kernel theorem or asserts an original-action lift.

The complete retained collapsed-plane92, saturated-base-change94
and intrinsic-quotient-surface proofs were reread for these gates.
The first assertion-bearing author run used
`/opt/anaconda3/bin/python` and passed the one method in 0.038
seconds, exit zero, with full output in chunk a3698e. Before
that run, the default Python dependency probe and one bundled
Python launch lacked SymPy and stopped at import; no assertion
was executed or failed in those two attempts. No frozen edit,
action realization, unrestricted recognition or historical
novelty claim is added.

[^kernel]: Shulim Kaliman and Nikolai Saveliev,
    [*C+-actions on contractible threefolds*, final author PDF](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
    Corollary 2.8(2). The full displayed statement and proof of
    Corollary 2.8 and the selected complete proof of Theorem 2.7
    were freshly read in the primary text in pass95. The deeper
    cited topology and surface-classification proofs were not
    freshly reread. This application needs only the quotient-plane
    conclusion for the polynomial three-ring, not freeness or
    a new proof of Miyanishi's original theorem.
