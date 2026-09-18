# The quadratic degree bound controls the second normal layer of a double fiber

For a collapsed, generically rank-one fixed component of whole-fiber
multiplicity two, the degree-two identities on the centered generators
force a constant quotient conormal direction. This removes the
zero-transverse-speed-derivative exception in the first-layer argument
for double fibers. It does not handle higher multiplicities or exclude
the double fiber itself.

## 1. The actual hypotheses

Retain the quadratic actual frame and the notation of
[conormal-layer93](nonconical-collapsed-conormal-layer-pass93.md).
In particular the fixed component has
\(A/\mathfrak q=\mathbb C[\bar c]\), its cylinder is
\(\mathfrak P=\mathfrak qB=(X,Y)\), and its ideal has the
exact invariant centered generators
\[
F=X-uEX,\qquad G=Y-uEY,\qquad
\mathfrak q=(F,G)A,\qquad N^3F=N^3G=0.
\tag{1}
\]
Assume additionally that its generic whole-fiber multiplicity is
\(\mu=2\). Set \(O=A_{\mathfrak q}\),
\(\mathfrak n=\mathfrak qO\), and \(L=\mathbb C(\bar c)\).
The actual subfield \(\mathbb C(c)\subset O\) maps isomorphically
to L. It is not an N-invariant coefficient field.

Choose a constant base-coordinate change so
\(x=s_1-s_1(m)\) has nonzero differential at the generic point.
Choose a second actual regular parameter y. The construction in
[curvilinear-action93](nonconical-curvilinear-fiber-action-pass93.md)
gives a basis \(dx,dy,dc\) of the local differential module and
its dual derivations. In the following expansions the coefficients
are rational functions of c, viewed in the actual subfield above.
The associated-graded ring is \(L[x,y]\), so these expansions
through order two are unique. No global coordinate system x,y,c
on A is asserted.

Put \(f=s_2-s_2(m)\). Rank one and the multiplicity-two hypothesis
give
\[
\begin{gathered}
f\equiv \alpha(c)x+a_{20}(c)x^2+a_{11}(c)xy+a_{02}(c)y^2
                  \pmod{\mathfrak n^3},\qquad a_{02}\ne0,\\
N=\epsilon(f_y\partial_c-f_c\partial_y),\qquad
\epsilon\in O^*,\qquad Nx=0,\\
Ny\equiv\gamma x\pmod{\mathfrak n^2},\qquad
Nc\equiv\delta x+\lambda y\pmod{\mathfrak n^2},\\
\gamma=-\epsilon_0\alpha',\qquad
\lambda=2\epsilon_0a_{02}\ne0,
\qquad \epsilon_0=\epsilon\bmod\mathfrak n .
\end{gathered}
\tag{2}
\]
Here a prime is ordinary differentiation in c. The nonzero
coefficient \(a_{02}\) follows because the image of f in the
DVR O/(x) has order exactly two. Partial differentiation in y
lowers normal order by at most one; partial differentiation in c
preserves normal order. Thus (2) follows from the actual local
Jacobian expression, not an assumed formal normal form for N.

## 2. A third-derivative identity modulo the cube of the normal ideal

Write the independent normal generators as
\[
F\equiv a(c)x+b(c)y,
\qquad G\equiv d(c)x+e(c)y
                  \pmod{\mathfrak n^2},\qquad ae-bd\ne0.
\tag{3}
\]
N preserves \(\mathfrak n\) and induces the degree-preserving
operator \(\gamma x\partial_y\) on its associated-graded ring.
Its action on coefficients has positive normal order. Consequently
the third power vanishes on \(\mathfrak n^2/\mathfrak n^3\):
three y-derivatives kill every homogeneous quadratic.

For any rational coefficient b(c), the ordinary chain rule and
(2) give
\[
N^2y\in\mathfrak n^2,\qquad
N^2b\equiv b'\lambda\gamma x\pmod{\mathfrak n^2},
\qquad N^3b\in\mathfrak n^2.
\tag{4}
\]
Indeed \(N^2c\equiv\lambda\gamma x\pmod{\mathfrak n^2}\),
whereas \(N^3c\in\mathfrak n^2\). Differentiating coefficients
produces an additional factor in \(\mathfrak n\); Nx is exactly
zero. These facts also show \(N^3(ax)\in\mathfrak n^3\).

The third-derivative product rule, with (3)--(4), therefore yields
\[
\begin{aligned}
0=N^3F&\equiv bN^3y+3b'\lambda\gamma^2x^2
                      \pmod{\mathfrak n^3},\\
0=N^3G&\equiv eN^3y+3e'\lambda\gamma^2x^2
                      \pmod{\mathfrak n^3}.
\end{aligned}
\tag{5}
\]
For example the term \(3(Nb)(N^2y)\) has order at least three;
the only new order-two term is \(3(N^2b)(Ny)\). The remainder
of F or G in \(\mathfrak n^2\) contributes nothing modulo
\(\mathfrak n^3\) after three applications of N. No classification
of Artinian algebras or higher-degree filtration is used.

## 3. The conormal dichotomy

If \(\gamma\ne0\), eliminate \(N^3y\) from (5). The class
of \(x^2\) is nonzero in the regular associated-graded ring,
and the characteristic is zero, giving
\[
be'-eb'=0.
\tag{6}
\]
At least one of b,e is nonzero by (3). Their ratio, when defined,
is a rational function of c with zero derivative and is therefore
constant in \(\mathbb C\). This includes the cases where one is
zero. Hence the line spanned by \((b,e)^t\) is constant.

Let C(c) be the polynomial first coefficient matrix of the two
base parameters in F,G, which is the same C as in the original
plane coordinates by the identity CM=0 in conormal-layer93.
The vector \((b,e)^t\) spans its kernel: the quotient first
terms in x,y are \((x,\alpha(c)x)^t\). Thus C has a constant
kernel and hence a constant row direction. If instead \(\gamma=0\),
(2) gives \(\alpha'=0\), so \(\alpha\in\mathbb C\), and C
has the constant column direction \((1,\alpha)^t\). In summary,
\[
\boxed{\quad
\mu=2:\quad
\gamma\ne0\Longrightarrow C=\ell(c)\rho_0,
\qquad
\gamma=0\Longrightarrow C=\ell_0\rho(c),
\quad}
\tag{7}
\]
where the indicated constant row \(\rho_0\) or column \(\ell_0\)
is nonzero. These are polynomial identities on the entire
component, since C has polynomial entries and the generic rational
identities hold in its function field. The constant base change
used to choose x does not change either constancy assertion.

In the constant-row case choose the original affine-linear good
normal coordinate \(L_0=\rho_0(X,Y)^t\). Since M=B0C and CM=0,
\(\rho_0M=0\), so \(EL_0\in\mathfrak P^2\). In the
constant-column case every centered generator has N-image in
\(\mathfrak q^2\), and the existing first-layer argument supplies
a constant good direction whose E-speed is in \(\mathfrak P^2\).
The local determinant proof in conormal-layer93, valid at every
component point, consequently gives in both cases
\[
\boxed{\quad
L_0\in\mathfrak P\text{ nonzero and affine-linear good},\quad
EL_0\in\mathfrak P^2,\quad
N(L_0-uEL_0)\in\mathfrak q^2,\quad
N^3(L_0-uEL_0)=0 .
\quad}
\tag{8}
\]
The conclusion now includes B0=0. There is also a direct
local-to-global ideal justification: \(\mathfrak P^2=(X,Y)^2\)
is \(\mathfrak P\)-primary in the original polynomial ring,
and \(\mathfrak q^2=\mathfrak P^2\cap A\) because B=A[u].
Its contraction is therefore \(\mathfrak q\)-primary. Membership
after localization at \(\mathfrak q\) consequently suffices
here. This uses the actual linear-plane property, not a general
claim that generic ideal membership always globalizes.

## 4. What remains open

For multiplicity greater than two, \(a_{02}=0\) and the crucial
coefficient \(\lambda\) in (2) can vanish. Equations (5)--(6)
then do not force a constant direction. The extension to those
multiplicities is not proved.

Even in multiplicity two, second-order vanishing of N on a centered
generator is not invariance. The intrinsic control
\(D=p\partial_y-2y\partial_c\), \(f_0=p+y^2\), has
\(Df_0=2py\ne0\), \(Df_0\in(p,y)^2\), and \(D^3f_0=0\).
Thus (8) is an additional exact frame restriction, not exclusion,
a common invariant coordinate, or recognition.

The proof depends on the actual global degree identities (1),
not merely an arbitrary first-jet matrix. Its third-derivative
identity is also checked symbolically in the
[companion control file](double_fiber_normal_order_checks_pass93.py).
That check does not verify the local geometric hypotheses
or the unrestricted cancellation conjecture. No historical novelty,
human review, or formal proof certification is claimed.
