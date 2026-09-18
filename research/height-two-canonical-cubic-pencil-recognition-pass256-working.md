# Recognition of the canonical height-two cubic graph by a curve pencil

In the actual shift-two chart250, suppose the first projection is
affine on the whole generic line and the chart has
\(q=t^3\), \(k_\lambda=0\), and \(n_\lambda=\nu\in\mathbb C^*\).
Then the original polynomial ring has an explicit invariant
coordinate, and its globally sliced kernel is \(\mathbb C^{[3]}\).
The constant \(\nu\) is retained throughout; it is not set equal to one.

This is a conditional endpoint for that canonical chart. It does not
itself normalize other shift-two charts, recognize every height-two
entry, or supply an arbitrary-coordinate entry theorem. The curve
parameter used in the proof is not promoted to an ambient coordinate.

## 1. Actual hypotheses and coefficient-field conventions

Use the fully read
[shift-two chart250](height-two-shift-two-cubic-chart-pass250-working.md).
In particular, assume an actual frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad a=EX\ne0,\qquad K=\operatorname{Frac}A.
\end{gathered}                                                     \tag{1}
\]
The full weighted initial kernel has height two, the two good
initials are complex-linearly independent, and the selected literal
quadratic-slot partial has exact shift two, as in250.
Its intrinsic derivation supplies the exact fields and generic line
\[
L\subset K,\qquad [L:\mathbb C(t,\lambda)]<\infty,\qquad
K=L(v),\qquad Nv=1,
\quad L[y,z,w]=L[v],\quad K=\mathbb C(y,z,w).                       \tag{2}
\]
The last equality is the actual fixed-\(X\) field return, not merely
the equality after adjoining \(L\).

Assume that the actual coordinate expansions in this chart are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(3t^2y+k)X+t^3X^2,\\
W&=w+(\rho' y+\lambda)X+\rho X^2,
\end{aligned}
\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}=-a^2\in L^* .     \tag{3}
\]
Here \(q=t^3\), \(\rho_\lambda=k_\lambda=0\), and
\(y=\alpha v+\beta\) with \(\alpha\in L^*\), \(\beta\in L\).
The two coefficient partials on \(L\) are the commuting extensions
of the partials on \(\mathbb C(t,\lambda)\), and they initially
fix \(v\). Primes denote the extended \(t\)-derivative on elements
annihilated by \(\partial_\lambda\).

Set \(F=\ker_L\partial_\lambda\). Then
\[
[F:\mathbb C(t)]<\infty,\qquad
\lambda\text{ is transcendental over }F,\qquad
\ker_F(d/dt)=\mathbb C.                                          \tag{4}
\]
Here is an elementary exact-field justification. For an element of
\(F\), differentiate its monic minimal polynomial over
\(\mathbb C(t,\lambda)\). The resulting lower-degree polynomial
vanishes at that element, so every coefficient derivative is zero.
The coefficients therefore belong to \(\mathbb C(t)\).
Thus \(F\) is algebraic over \(\mathbb C(t)\), and \(\lambda\)
is transcendental over \(F\). Adjoining \(\lambda\) preserves
degrees of finite subextensions of \(F/\mathbb C(t)\); those degrees
are bounded by \([L:\mathbb C(t,\lambda)]\). This proves finiteness.
Commutativity of the partials makes \(F\) stable under the prime
derivative. The same monic-polynomial argument over \(\mathbb C(t)\)
shows that a prime-constant is algebraic over \(\mathbb C\), hence
belongs to \(\mathbb C\). No equality \(F=\mathbb C(t)\) is assumed.

The first and second potentials of250, with \(k_\lambda=0\), are
\[
\begin{aligned}
z&=3t y^2+k'y+n,\qquad n_\lambda=\nu\in\mathbb C^*,\\
\nu w&=\ell-y^3+\frac{\nu\rho''-k''}{2}y^2-n_t y,
\end{aligned}                                                     \tag{5}
\]
where \(n,\ell\in L\). These identities are retained inputs from
the actual chart. The nonzero constant \(\nu\) is an additional
canonical-branch hypothesis of this note.

## 2. The scalar determinant gives a generic polynomial pencil

Equation (4) first gives
\[
n=\nu\lambda+n_0,\qquad n_0\in F.                                \tag{6}
\]
Change only the coefficient-field parameter from \(v\) to \(y\).
Its derivative is \(y_v=\alpha\in L^*\). The full chain rule,
including the moving \(t,\lambda\) derivatives of \(y\), gives
\[
J_y:=\det\frac{\partial(y,z,w)}{\partial(t,\lambda,y)}
       =-\frac{a^2}{y_v}\in L^*.                                 \tag{7}
\]
The partials in the determinant on the left hold the new parameter
\(y\) fixed. On coefficient elements of \(L\) they retain the
same values as before. In particular \(J_y\) is independent of
\(y\), although it need not be a complex constant.

Computing this determinant directly from (5),(6) gives
\[
J_y=(3y^2+k''y+n_0')\frac{\ell_\lambda}{\nu}
       -\ell_t-\frac{\nu\rho'''-k'''}2y^2+n_0''y .                \tag{8}
\]
For example, the first row is \((0,0,1)\), while
\(z_\lambda=\nu\). Thus the sign and the factor \(\nu\)
in (8) are fixed by the literal determinant, not a rescaling.
Its quadratic and linear coefficients imply
\[
\begin{gathered}
\mu:=\frac{\ell_\lambda}{\nu}
      =\frac{\nu\rho'''-k'''}6\in F,\qquad
\ell=\nu\mu\lambda+\ell_0,\quad\ell_0\in F,\\
n_0''=-\mu k'' .
\end{gathered}                                                     \tag{9}
\]
This convention uses \(\mu=\ell_\lambda/\nu\), not
\(\mu=\ell_\lambda\).

Define three coefficient functions in \(F\) by
\[
A_2=\frac{\nu\rho''-k''}{2}-3t\mu,\qquad
A_1=-n_0'-\mu k',\qquad A_0=\ell_0-\mu n_0 .                     \tag{10}
\]
Eliminating \(\lambda\) with
\(\nu\lambda=z-3ty^2-k'y-n_0\), including its factor \(\nu\),
rewrites the second potential as
\[
\boxed{\nu w=\mu z-y^3+A_2y^2+A_1y+A_0.}                         \tag{11}
\]
The coefficient derivatives satisfy
\[
A_2'=-3t\mu',\qquad A_1'=-k'\mu'.                               \tag{12}
\]
Both are direct consequences of (9), without assuming rationality
of any coefficient function.

The actual field return in (2) is decisive here. Equation (11)
gives one field inclusion, and \(F\subset L\subset K\) gives the
other:
\[
K=\mathbb C(y,z,w)=F(y,z).
\quad\text{Consequently}\quad
F(y,z)=\mathbb C(y,z)(\mu z+A_2y^2+A_1y+A_0).                     \tag{13}
\]
Also \(y,z\) are algebraically independent over \(F\): the
left side has transcendence degree three over \(\mathbb C\),
while \(F\) has transcendence degree one. Equivalently, (5),(6)
identify \(F(y,z)=F(y,\lambda)\), with the two parameters
independent over \(F\).

## 3. A self-contained generic-pencil pole argument

We use the following exact curve fact. For a nonconstant function
\(f\) on a nonsingular projective curve \(\Gamma/k\),
\[
\deg\operatorname{Pole}(f)=[k(\Gamma):k(f)].                      \tag{14}
\]
A one-variable function field has such a projective model by
[Stacks, Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1).
The pole divisor is the pullback of \(\infty\) under the associated
morphism to \(\mathbb P^1\). Its degree is (14) by the
[pullback-degree formula, tag 0AYZ](https://stacks.math.columbia.edu/tag/0AYZ)
and the
[function-field definition of degree, tag 02NY](https://stacks.math.columbia.edu/tag/02NY).
These statements were freshly read in their primary forms.

Here is the precise pencil consequence, proved independently.
Let \(F/\mathbb C\) be a one-variable function field and let
\(Y_0,Z_0\) be independent over \(F\). Suppose
\[
F(Y_0,Z_0)=\mathbb C(Y_0,Z_0)(f),\qquad
f=f_1Z_0+f_2Y_0^2+f_3Y_0+f_0,\quad f_i\in F.                    \tag{15}
\]
Then there is a parameter \(\gamma\) with
\(F=\mathbb C(\gamma)\) such that every \(f_i\) lies in
\(\mathbb C+\mathbb C\gamma\). Any nonconstant coefficient
can itself be chosen as \(\gamma\).

To see this, let \(\Gamma/\mathbb C\) be the nonsingular projective
curve of \(F\). Every closed point is complex-rational. Take the
maximum polar divisor of the four coefficients:
\[
D=\sum_{P\in\Gamma}d_PP,\qquad
d_P=\max\{0,-\operatorname{ord}_P f_0,
                -\operatorname{ord}_P f_1,
                -\operatorname{ord}_P f_2,
                -\operatorname{ord}_P f_3\}.                    \tag{16}
\]
Base change to \(\Omega=\mathbb C(Y_0,Z_0)\). The curve remains
integral and nonsingular, with function field \(F(Y_0,Z_0)\).
Every original point \(P\) gives an \(\Omega\)-rational point,
with the same local uniformizer. At a point with \(d_P>0\), the
coefficient of that uniformizer to the power \(-d_P\) in \(f\)
is
\[
c_1Z_0+c_2Y_0^2+c_3Y_0+c_0,\qquad c_i\in\mathbb C,
\quad (c_0,c_1,c_2,c_3)\ne0.                                    \tag{17}
\]
It cannot vanish because the four displayed monomials are
complex-linearly independent. There are no poles elsewhere,
since all four coefficients are regular off the support of \(D\).
Thus the pole divisor of \(f\) on the base-changed curve is
exactly \(D_\Omega\).

The function in (15) is nonconstant over \(\Omega\), and its
function-field degree is one. Equation (14) therefore implies
\(\deg D=1\). Hence \(D\) consists of one complex point with
multiplicity one. At least one coefficient is nonconstant;
otherwise (15) would generate only \(\Omega\). Any nonconstant
coefficient \(\gamma\) has that single simple pole, and another
application of (14) over \(\mathbb C\) gives
\(F=\mathbb C(\gamma)\). Every other coefficient has at most
the same simple pole. As a rational function of \(\gamma\),
it has no finite pole and at most a simple pole at infinity,
so it is affine in \(\gamma\). This proves the assertion.

No numerical specialization of \(Y_0,Z_0\) is used. Such a
specialization could cancel (17). No rationality of \(F\) is
assumed before the pole computation.

## 4. The coefficient functions needed for the ambient map are constant

Apply Section 3 to (13). If \(\mu\notin\mathbb C\), it may be
chosen as the curve parameter, so
\(A_2=c\mu+d\) for some \(c,d\in\mathbb C\).
By (4), \(\mu'\ne0\). The first identity in (12) would give
\[
c\mu'=-3t\mu',\qquad t=-c/3\in\mathbb C,
\]
contrary to the supplied transcendental coefficient parameter.
Therefore
\[
\boxed{\mu,A_2,A_1\in\mathbb C.}                                 \tag{18}
\]
Indeed the last two constants follow from (12),(4).
The remaining coefficient \(A_0\) is not claimed constant.

The identities (9),(10) now integrate exactly over \(F\):
\[
\begin{aligned}
\nu\rho'-k'-3\mu t^2&=2A_2t+c_1,\\
-\mu k-n_0&=A_1t+c_2,\\
\nu\rho-k-\mu t^3&=A_2t^2+c_1t+c_3,
\end{aligned}
\qquad c_1,c_2,c_3\in\mathbb C.                                  \tag{19}
\]
For example, differentiation of the first equality has zero
residual by (10); the second follows from the definition of
\(A_1\); the third integrates the first. Each integration
constant is complex by (4), not by a rational ansatz.
The scalar (8) also reduces to \(J_y=-A_0'\ne0\), so the
remaining coefficient genuinely carries the curve parameter.

## 5. The original invariant coordinate and both inverse orders

All coefficients in the following polynomial are now complex:
\[
\boxed{
I=\nu W-\mu Z-XZ+Y^3-A_2Y^2-A_1Y
          -c_1XY-c_2X-c_3X^2\in B.}                              \tag{20}
\]
Substitute the actual expansions (3), not a generic ambient
coordinate change. The coefficient of \(X^0\) is \(A_0\) by
(11). The coefficients of \(X^3,X^2,X\), respectively, are
\[
\begin{aligned}
&0,\\
&\nu\rho-\mu t^3-k-A_2t^2-c_1t-c_3,\\
&(\nu\rho'-k'-3\mu t^2-2A_2t-c_1)y
               -\mu k-n_0-A_1t-c_2 .
\end{aligned}                                                     \tag{21}
\]
They vanish by (19). In the last line the cancellation uses
\(\nu\lambda=z-3ty^2-k'y-n_0\), not the formula with \(\nu\)
omitted. Thus \(I=A_0\in F\subset\operatorname{Frac}A\), and
\(EI=0\) since \(I\) is also an element of the original ring.

Retaining \(X,Y,Z\), the map replacing \(W\) by \(I\) has the
explicit polynomial inverse
\[
W=\frac{I+\mu Z+XZ-Y^3+A_2Y^2+A_1Y
                    +c_1XY+c_2X+c_3X^2}{\nu}.                   \tag{22}
\]
Substitution of (20) into (22) returns \(W\). Substitution of
(22) into (20) returns \(I\), and the three retained coordinates
are unchanged in both compositions. Division is only by the
proved complex unit \(\nu\). Therefore
\(B=\mathbb C[I,X,Y,Z]\) is an actual polynomial coordinate
presentation with \(EI=0\).

The kernel \(A\) is regular: it is a finitely generated algebra
because \(A=B/(u)\), and regularity descends from the polynomial
extension \(A[u]=B\). Equivalently, the actual slice has
\(Eu=1\), so its zero hypersurface is nonsingular.
Apply
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1),
freshly read with its exact hypotheses: a nonzero characteristic-zero
LND on a four-variable polynomial ring, fixing one actual coordinate,
has a two-variable polynomial kernel over that coordinate when the
kernel is regular. With that fixed coordinate equal to \(I\),
\[
\boxed{A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.}                 \tag{23}
\]

## 6. Scope and provenance

The complete250 chart was read before using its potentials,
calibration and actual projected field return. The proof above
retains a general nonzero complex \(\nu\), proves its own
finite-field and generic-pencil steps, and constructs both orders
of the actual polynomial inverse. The same pole lemma appears
independently in the separate shift-one endpoint254, whose complete
source was also read. Neither argument treats a coefficient-field
parameter as an original polynomial coordinate.

This source does not prove the normalization hypotheses
\(q=t^3\), \(k_\lambda=0\), \(n_\lambda\in\mathbb C^*\), or
the affine first projection for every shift-two chart. Any use of
a separate normalization proof must check its actual coordinate
transport and rebuild the selected chart before applying this
conditional endpoint. The shift-one pair is outside this note.

Independent unsaved algebra checks confirm the fixed-\(y\)
determinant and the full general-\(\nu\) identity (20),(21);
finite symbolic checks do not establish the curve-field argument
or the published recognition theorem.
No earlier source or frozen packet was edited. No saved checker
was executed, imported or compiled. No human expert review,
proof-assistant certification, historical novelty, arbitrary-entry
theorem or unrestricted cancellation solution is claimed.
