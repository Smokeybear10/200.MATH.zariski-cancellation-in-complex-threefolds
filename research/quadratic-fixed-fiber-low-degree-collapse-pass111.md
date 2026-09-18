# A fixed fiber collapses every translating good component

In the supplied actual nonconical quadratic frame, every
multiplicity-one companion of a fixed component is collapsed by
both good relative generators. No nonvanishing of the speed normal
is needed. The key is the invariant conic attached to any element
of N-degree at most two, not an extension of the nonzero-normal
volume argument.

For a collapsed fixed double component, the actual parameter c
also has a nonzero derivative on its entire double thickening:
that derivative is a constant nonzero multiple of a generator of
the square-zero ideal. This provides a low-degree element with
nonzero whole-fiber residue even when the speed normal vanishes.
It does not by itself put an original affine-linear normal in
the whole fiber ideal or make that ideal stable under the original
partial derivative.

## 1. Actual hypotheses and the invariant conic

Retain the supplied original frame and actual invariant plane of
[three-good87](constant-acceleration-three-good-frame-pass87.md),
[invariant-plane88](constant-acceleration-invariant-plane-pass88.md),
and [global-Jacobian91](nonconical-global-jacobian-field-pass91.md).
In the relative quadratic branch the actual data include
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,
\qquad u=Ez/q,\quad q=E^2z\in\mathbb C^*,\\
E^2x_i=0,\qquad S=\mathbb C[s_1,s_2]=\ker(N|_A),\qquad
A=S[A_1,A_2,c],\\
N(f)=\det\frac{\partial(s_1,s_2,u,f)}
 {\partial(x_1,x_2,x_3,z)},\qquad
F_j=\ker(N^{j+1}|_A),\qquad A_1,A_2\in F_2,\quad c\in F_4.
\end{gathered}
\tag{1}
\]
Here A is a smooth complex affine threefold, S to A is faithfully
flat with nonempty pure curve fibers, and N is the actual primitive
LND. The degree bounds are the retained generic-line bounds, not
bounds on ordinary degree in the four original coordinates.

Fix a closed base point \(\mathfrak m\) whose fiber contains an
N-fixed closed point p. For any \(U\in F_2\), define
\[
\begin{gathered}
p_U=N^2U\in S,\qquad
\eta_U=2p_UU-(NU)^2\in S,\\
p_U(p)=\eta_U(p)=0,\qquad
p_U,\eta_U\in\mathfrak m,\qquad
\boxed{\ (NU)^2=0\quad\hbox{in }A/\mathfrak mA.\ }
\end{gathered}
\tag{2}
\]
Indeed \(N\eta_U=2p_UNU-2NU\,N^2U=0\), so its membership
in S uses the exact kernel in (1). At a fixed point the value
of N on every function is zero, including its value on NU.
Thus both \(NU(p)\) and \(p_U(p)\) vanish, proving the
evaluations and then (2). This argument does not interchange
formation of a kernel with reduction modulo the base ideal.

In particular NU vanishes on every reduced component of the
fiber. Applying (2) also to U+V and using characteristic zero
gives the slightly stronger ideal statement
\[
N(F_2)N(F_2)\subseteq\mathfrak mA,
\qquad
N(F_2)\longrightarrow (A/\mathfrak mA)_{\mathrm{red}}
\text{ is zero}.
\tag{3}
\]
The elementary calculation (2) applies to any LND with the stated
kernel and a fixed point; original coordinates enter the next
step through the actual membership \(A_i\in F_2\).

## 2. Simple companions collapse, without a speed-normal hypothesis

By the componentwise nonvanishing theorem retained in
[primitive-fiber54](primitive-fiber-nonvanishing-pass54.md), a
multiplicity-one component has nonzero induced N. As reconstructed
in [quotient-rank95, Sections 1--3](quadratic-quotient-rank-everywhere-pass95.md),
its reduced coordinate ring is \(\mathbb C[t]\), with N a
nontrivial translation. Its kernel is exactly \(\mathbb C\).
Equation (3) therefore makes the restriction of every element
of F2 constant on this component. In particular
\[
\boxed{\quad
\mu_i=1\text{ in a fixed-containing fiber}
\quad\Longrightarrow\quad
\bar A_1,\bar A_2\in\mathbb C,
\qquad A/\mathfrak q_i=\mathbb C[\bar c].
\quad}
\tag{4}
\]
The last equality uses the actual generating set in (1); its
dimension makes \(\bar c\) transcendental. The restriction of
N to this ring is \(\rho\partial_c\), with
\(\rho\in\mathbb C^*\).

For a mixed fiber of profile (2,1), the fixed double component
is already collapsed: the no-companion theorem in
[component-compatibility96](quadratic-component-compatibility-pass96.md)
says that a noncollapsed fixed component would be the whole
reduced fiber. Equation (4) now collapses its simple companion
as well. This removes the L(m) nonzero premise specifically
from the companion-collapse conclusion of pass98.

For each collapsed component the tensor evaluation and exact
original reconstruction in
[collapsed-plane92](nonconical-collapsed-component-plane-pass92.md)
give an actual affine plane in B, with direction
\(\operatorname{span}_{\mathbb C}(b(\mathfrak m),e_z)\).
Consequently the two cylinders in the mixed case are distinct,
parallel, disjoint affine planes. A constant affine change in
the three good coordinates can write their reduced ideals as
\((X,Y)\) and \((X,Y-1)\). This does not put X in the
nonreduced ideal \(\mathfrak mB\).

## 3. The entire collapsed double factor

Now let \(\mathfrak q\) be any collapsed fixed component of
multiplicity two, whether or not it has a companion. All reduced
quadratic fiber components are disjoint, by the retained95 theorem.
The whole-fiber decomposition and actual parameter-ring argument
of its Section 4 give a factor D2 with
\(D_{2,\mathrm{red}}=\mathbb C[c]\), containing the actual
\(\mathbb C[c]\), and finite free of rank two over that subring.

The reduction map splits over \(\mathbb C[c]\). Its kernel Z
is thus a rank-one projective, and hence free, module over this
PID. Generically D2 has Artinian length two, so its nilradical
has square zero. Torsion-freeness over \(\mathbb C[c]\) then
makes \(Z^2=0\) globally. Choose a generator epsilon of Z.
The induced N preserves this factor and its nilradical. Indeed,
derivations kill idempotents, and the additive action preserves
each reduced component. We obtain
\[
\begin{gathered}
D_2=\mathbb C[c]\oplus\epsilon\mathbb C[c]
 \simeq\mathbb C[c,\epsilon]/(\epsilon^2),\\
\bar N c=g(c)\epsilon,\qquad
\bar N\epsilon=h(c)\epsilon,\qquad
\bar N^n\epsilon=h(c)^n\epsilon,\qquad h=0.
\end{gathered}
\tag{5}
\]
Fixedness of the reduction gives the first derivative formula.
The iterated formula uses \(\epsilon^2=0\); local nilpotence
on the actual quotient D2 forces h=0. No local nilpotence is
asserted after localization at an arbitrary closed point or after
completion.

## 4. The canonical Jacobian makes g a constant unit

Fix any closed point p of this double component. By the
all-point quotient-rank theorem95, a constant combination x of
the centered base parameters has \(dx(p)\ne0\). Complete it
to a constant base coordinate pair x,f. The actual restriction
of c is a parameter on the smooth reduced component. Since x
vanishes there, dx and dc are independent at p.

In \(O=A_p\), choose \(y\in\mathfrak qO\) so that
\(\mathfrak qO=(x,y)\) and \(dx,dy,dc\) form a local
differential basis. The ring \(O/(x)\) is a regular local
surface. Its remaining base equation \(\bar f\) has radical
\((\bar y)\). There is only the chosen component locally,
because the fiber components are disjoint. Factoring in this
regular local UFD, or contracting its unique height-one primary
component from the DVR, gives \(\bar f=\bar v\bar y^e\)
with \(\bar v\) a unit. The exponent is exactly the generic
fiber length, namely two. Lift the unit and the equality to O:
\[
\begin{gathered}
f=\alpha x+v y^2,\qquad v\in O^*,\qquad
\mathfrak mO=(x,y^2),\\
N|_O=\nu(f_y\partial_c-f_c\partial_y),\qquad \nu\in O^*,\\
Nc\equiv 2\nu v\,y\pmod{\mathfrak mO}.
\end{gathered}
\tag{6}
\]
The sign is absorbed into nu. The exact unit factor follows
from the retained local volume calculation in
[fixed-scheme92, Sections 1 and 3](nonconical-fixed-scheme-structure-pass92.md):
evaluate the original four-dimensional differential basis at
u=0 while retaining du. This identifies the canonical N with
a unit times the three-dimensional Jacobian in the displayed
differential basis. The partials in (6) are its dual local
derivations. They are not assumed to be global coordinates.

In (6), differentiating alpha times x contributes a multiple
of x; differentiating v times y squared contributes
\(2vy\) modulo \((x,y^2)\). Thus Nc generates the localized
nilradical at every p. Comparing with (5) shows that g has no
zero on the complex affine c-line. It is a nonzero constant.
Consequently
\[
\boxed{\quad
\bar N|_{D_2}=\lambda\epsilon\partial_c,
\qquad\lambda\in\mathbb C^*,\qquad
Nc\in F_3\text{ has nonzero residue generating }Z.
\quad}
\tag{7}
\]
This is an all-point statement about the whole double
thickening, stronger than merely detecting the generic Artinian
action. It holds without any condition on L(m).

In the mixed case, (4)--(7) give the whole fiber, with its actual
c and N, as
\(\mathbb C[c,\epsilon]/(\epsilon^2)\times\mathbb C[c]\),
with derivative \((\lambda\epsilon\partial_c,\rho\partial_c)\).
In particular the residue of Nc is nonzero on both factors,
nilpotent on the double and a nonzero scalar on the simple.
No generator of the Artin coefficient algebra is yet asserted
to be an element of F2 or a specified original linear normal.

## 5. What zero speed normal does and does not imply

Use the actual notation of
[volume-descent88](constant-acceleration-volume-descent-pass88.md):
\(b=(Ex_1,Ex_2,Ex_3)^t\),
\(L=b_{s_1}\times b_{s_2}\), \(\Omega=L\cdot b\), and
\(L\cdot(x_{\rm tr}-ub)=\kappa\in S\).
The row b is unimodular, so \(b(\mathfrak m)\ne0\).
If \(L(\mathfrak m)=0\), then
\[
\begin{gathered}
\operatorname{rank}(db_{\mathfrak m})\le1,
\qquad \Omega(\mathfrak m)=\kappa(\mathfrak m)=0,\\
J=\operatorname{Jac}_{x_1,x_2,x_3,z}(b,qu),\qquad
J^3=q\,N(x_1,x_2,x_3,z)(L,0),\qquad
J^2e_z=\Omega\,N(x_1,x_2,x_3,z),\\
J^3\in\operatorname{Mat}_4(\mathfrak mB),\qquad
J^2e_z\in(\mathfrak mB)^4,\qquad
\operatorname{rank}J(p)\le2\quad(p\text{ on the fiber}).
\end{gathered}
\tag{8}
\]
The exact matrix identities are91. In particular the displayed
congruences hold on the nonreduced whole fiber, not just its
radical. The rank bound follows separately by factoring the
first three rows through db and adding the last row q du.
Rank of the speed map db is not rank of the quotient
differential \((ds_1,ds_2)\); the latter still has rank at
least one by95.

For a collapsed component,92 gives
\(T=\partial_z\) preserving its reduced plane ideal,
\(Tu=0\), \(Tc=1\), and \([E,T]=0\) on that reduced plane.
These statements hold without L(m) nonzero. For the two
collapsed mixed components they hold on their disjoint reduced
union. They do not imply \(T(\mathfrak mB)\subseteq\mathfrak mB\).
The proof here supplies no replacement for99's stronger
original linear equation inside the whole fiber ideal.

Thus a zero speed normal does not make the canonical N-action
on the double factor zero: (7) proves the opposite. Nor do the
vanishing highest-adjoint coefficients in (8) make N vanish;
the factor Omega is precisely what vanishes. The remaining
whole-ideal, low-degree Artin-generator and global-recognition
questions are distinct from the companion-collapse theorem.

## Scope and evidence

The main new argument is (2)--(4); the all-point canonical
double-action extension is (5)--(7). Root and Geometry
independently checked their outlines before saving. This note
uses the retained actual-frame, primitive-component,
disjointness, finite-thickening and quotient-rank statements;
it adds no primary-source theorem, numerical method or actual
example. The regular-local primary/DVR argument is the same
retained algebraic gate as99, applied locally without its
nonzero-normal input. The actual cancellation-to-frame
reduction, other fiber sectors and global recognition remain
unproved. No file through110 is changed.
