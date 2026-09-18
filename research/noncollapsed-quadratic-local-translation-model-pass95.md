# A surviving quadratic generator gives an exact local Weitzenbock model

A noncollapsed fixed component in the actual quadratic frame has
whole-fiber multiplicity two. Its two good relative generators
have a reduced affine-line image; the whole reduced component is
an open subset of that line. If its first normal N-action is
nonzero, a surviving actual good generator supplies an exact
local differential model, not just a weighted initial operator.

The resulting normal parameters and base parameters are actual
polynomial functions. The assertion is local at the generic
component. It does not identify the original polynomial frame
with a chosen abstract Weitzenbock action or recognize A.

## 1. The actual component and the surviving generator

Retain the nonconical quadratic frame of
[frontier94](nonconical-weighted-frontier-pass94.md):
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]\subset A,\qquad
A=S[A_1,A_2,c],\qquad A_K=K[w],\quad K=\operatorname{Frac}S,\\
B=A[u]=\mathbb C^{[4]},\qquad
\ker(N|_A)=S,\qquad \deg_w A_i\le2,\qquad N^3A_i=0 .
\end{gathered}
\tag{1}
\]
Here N is the specified primitive canonical Jacobian LND, not
an arbitrary derivation with that kernel. The quotient is
faithfully flat, A is smooth, and the two degree statements are
the retained actual generic-degree conclusions.

Let \(\mathfrak q\) be the prime of a fixed component over a
closed base point \(\mathfrak m\). Assume it is noncollapsed:
some complex linear combination U of \(A_1,A_2\) has
nonconstant residue. The component-degree bound in
[closed-fiber92](nonconical-closed-fiber-multiplicity-pass92.md)
gives
\[
\begin{gathered}
\mu[\kappa(\mathfrak q):\mathbb C(\bar U)]
\le\deg_wU\le2,\qquad \mu\ge2,\\
\boxed{\quad
\mu=2,\quad \kappa(\mathfrak q)=\mathbb C(\bar U),
\quad \deg_wU=2,\quad N^3U=0,\quad N^2U\ne0 .
\quad}
\end{gathered}
\tag{2}
\]
The same field-degree conclusion holds for every nonconstant
complex linear combination of the two good generators.
The lower bound on the multiplicity uses that this is a fixed
component of the actual primitive field. The nonzero second
derivative follows because \(N|_{A_K}\) is a nonzero constant
multiple of \(\partial_w\).

## 2. The reduced good image is a line

If U already spans the linear space of \(A_1,A_2\), the good-image
conclusion below is immediate. Otherwise choose a second constant
linear combination V so U,V span that space. Since the component field is
\(\mathbb C(\bar U)\), write
\(\bar V=P(\bar U)/Q(\bar U)\) in reduced form.

For a generic nonzero complex number t, the reduced quotient for
\(\bar U+t\bar V\) is
\((\bar UQ(\bar U)+tP(\bar U))/Q(\bar U)\). Its numerator and
denominator are coprime. Apart from at most one leading-coefficient
cancellation, the function-field degree is
\(\max(\deg Q+1,\deg P)\). The elementary degree formula is
proved by the irreducibility argument in
[saturated-base-change94, Section 3](nonconical-saturated-base-change-pass94.md).
Equation (2) makes that degree one. Therefore Q is constant
and P has degree at most one.

Consequently both reduced good generators are affine-linear
functions of \(\bar U\). Writing the residue of the third
generator as \(a(\bar U)/b(\bar U)\) in coprime form gives
\[
\boxed{\quad
\mathbb C[\bar A_1,\bar A_2]=\mathbb C[\bar U],\qquad
A/\mathfrak q
=\mathbb C[\bar U,\bar c]
=\mathbb C[\bar U,1/b(\bar U)] .
\quad}
\tag{3}
\]
Indeed a Bezout identity for a,b expresses \(1/b\) in the
middle ring; the other inclusion is immediate. The convention
b=1 includes a polynomial third residue. Thus the component
is a smooth open affine line. It need not be the entire line
from this argument alone. In a saturated total-four fiber the
separate all-projection argument can impose more; that is not
being assumed here.

## 3. First normal action and exact actual parameters

Put \(O=A_{\mathfrak q}\), \(\mathfrak n=\mathfrak qO\).
The actual field \(\mathbb C(U)\subset O\) maps isomorphically
to its residue field by (2). Since the canonical Jacobian N
vanishes on the reduced component, the quotient differential
has rank at most one there. Generic quotient rank zero would
give multiplicity at least four by closed-fiber92, so the
generic quotient rank is one.

After a constant affine base change, choose
\(x=s_1-s_1(\mathfrak m)\) with nonzero differential there.
Choose a second regular parameter y and put
\(f=s_2-s_2(\mathfrak m)\). The actual local Jacobian construction
of [curvilinear93](nonconical-curvilinear-fiber-action-pass93.md)
gives a differential basis dx,dy,dU and
\[
\begin{gathered}
N=\epsilon(f_y\partial_U-f_U\partial_y),\qquad
\epsilon\in O^*,\qquad Nx=0,\\
f\equiv\alpha(U)x+a_{20}(U)x^2+a_{11}(U)xy
                  +a_{02}(U)y^2\pmod{\mathfrak n^3},
\qquad a_{02}\ne0,\\
Ny\equiv\gamma x,\qquad
NU\equiv\delta x+\lambda y\pmod{\mathfrak n^2},\qquad
\gamma=-\epsilon_0\alpha',\quad
\lambda=2\epsilon_0a_{02}\ne0 .
\end{gathered}
\tag{4}
\]
Coefficients are rational functions of the actual U, and a prime
denotes differentiation in U. The coefficient of \(y^2\) is
nonzero because \(O/(x,f)\) has length two. The original local
derivations, and not just formal symbols, give these formulas.

Assume now that the first normal action is nonzero, equivalently
\(\gamma\ne0\). Define the actual polynomial functions
\[
\begin{gathered}
r=N^2U\in S,\qquad v=NU\in A,\qquad
r,v\in\mathfrak q,\\
v\equiv\delta x+\lambda y,\qquad
r\equiv\lambda\gamma x\pmod{\mathfrak n^2},\\
\boxed{\quad
\mathfrak n=(r,v)O,\qquad dr,dv,dU
\text{ form a basis of }\Omega_{O/\mathbb C}.
\quad}
\end{gathered}
\tag{5}
\]
For the second congruence, differentiate the first congruence
for v. N preserves \(\mathfrak n\) and its square. The
derivatives of its rational coefficients belong to
\(\mathfrak n\), since NU does. Thus only \(\lambda Ny\)
contributes in \(\mathfrak n/\mathfrak n^2\).
The determinant of the two displayed normal rows is
\(\lambda^2\gamma\ne0\). Nakayama gives the regular parameter
pair, and the transcendental residue of U supplies the remaining
differential basis vector.

There is no assumption that r is an affine-linear polynomial
in the original base coordinates, or that v is an original
ambient coordinate.

## 4. Exact differential form and the base parameters

The functions just constructed have exact identities
\[
\begin{gathered}
Nr=0,\qquad Nv=r,\qquad NU=v,\\
\boxed{\quad N=r\partial_v+v\partial_U\quad\text{on }O, \quad}\\
\eta=2rU-v^2\in S\cap\mathfrak q=\mathfrak m .
\end{gathered}
\tag{6}
\]
The partial derivatives are dual to the actual basis
dr,dv,dU, so their coefficient expression determines N on O.
The assertion on \(\eta\) follows by direct differentiation and
the actual global kernel equality. It is a polynomial invariant,
not a fraction introduced to normalize the field.

The ideal \((r,\eta)O=(r,v^2)O\) has colength two because r,v
are regular parameters. It is contained in \(\mathfrak mO\),
whose colength is also two by (2). The inclusion is therefore
an equality. The map \(S_{\mathfrak m}\to O\) is local and flat,
hence faithfully flat. Contracting this equality yields
\[
\boxed{\quad
\mathfrak mS_{\mathfrak m}=(r,\eta)S_{\mathfrak m},\qquad
\mathfrak mO=(r,v^2)O .
\quad}
\tag{7}
\]
In particular r,\(\eta\) are a regular system of parameters of
the regular local base ring \(S_{\mathfrak m}\).

For precision, the coefficient-compatible completed description is
\[
\begin{gathered}
\widehat O=\mathbb C(U)[[r,v]],\qquad
\widehat{S_{\mathfrak m}}=\mathbb C[[r,\eta]],\\
\eta\longmapsto 2rU-v^2,\qquad
N=r\partial_v+v\partial_U .
\end{gathered}
\tag{8}
\]
The first description uses the specified actual coefficient
field and regular parameters, by the same graded-approximation
argument as [weighted94](nonconical-weighted-conormal-rigidity-pass94.md).
The derivations extend continuously; no local nilpotence on
these completed rings is being asserted. In particular N need
not kill the coefficient field \(\mathbb C(U)\).

## 5. What this local model does not assert

Equations (5)--(8) describe actual functions and their local
differential action, and not merely a leading weighted field.
They do not identify \(A_{\mathfrak q}\) with a polynomial local
ring over \(\mathbb C(U)\), trivialize a possible etale
neighborhood, or give an original four-variable inverse pair.
The regular parameters r,\(\eta\) on the localized base need
not generate S globally.

The first-normal-action-zero case is outside (5)--(8). Likewise
the model does not prove that the open line in (3) has no
punctures, resolve an intersection with a second component,
or exclude the noncollapsed companion required by
[column-classification94](nonconical-conormal-column-classification-pass94.md).
Those require further actual global information.

No new numerical method, arbitrary-frame reduction, full-ring
recognition, source-theorem novelty, or change to pass94 and
earlier is asserted. The new proof uses the fully retained
component-degree, local-Jacobian and coefficient-compatible
completion gates. No fresh original-source proof reading is
claimed for this note.
