# Parallel planes have different actual Jacobian normal orders

This is a bounded pass99 working proof, separate from the frozen
pass98 files. In the nonzero-normal (2,1) configuration, the actual
velocity Jacobian has a uniform triangular form along both component
planes. On the simple plane, two successive transverse coefficients
are nonzero complex constants. On the fixed double plane their
product is identically zero.

The trace also forces fourth-order spatial divisibility after
restricting one original coordinate to zero. That divisibility is
not whole normal-square membership: the simple component has a
nonzero linear term in the discarded coordinate. Thus this
calculation does not exclude the configuration.

## 1. The actual parallel-plane setting

Retain all hypotheses and conclusions of
[companion-collapse98](quadratic-normal-companion-collapse-pass98.md).
In particular the double component is fixed pointwise by the
canonical N, the simple component has multiplicity one, and
\(L_0=L(\mathfrak m)\ne0\). Use the actual constant affine
good-coordinate change constructed there:
\[
\begin{gathered}
B=\mathbb C[\ell,Y,W,z]=A[u],\qquad
\mathfrak P_2=(\ell,Y),\qquad \mathfrak P_1=(\ell,Y-1),\\
E\ell=r(s)\in\mathfrak m^2\setminus\{0\},\qquad
EY=\sigma(s),\qquad EW=\phi(s),\qquad Ez=qu,\\
r(\mathfrak m)=\sigma(\mathfrak m)=0,\qquad
\phi(\mathfrak m)=1,\qquad
u|_{\mathfrak P_i}=W+\delta_i,\quad \delta_i\in\mathbb C.
\end{gathered}
\tag{1}
\]
The coordinate ell is specifically \(L_0\cdot x_{\rm tr}-\kappa_0\),
without an additional scalar rescaling. N below always denotes
the original canonical field, not a newly normalized Jacobian
derivation in the new coordinate order.

Let J be the velocity Jacobian in the coordinate order
\((\ell,Y,W,z)\). The constant affine change conjugates the
original Jacobian by its constant derivative matrix. Hence the
actual identities \(J^4=0\), \(\operatorname{tr}J=0\), and
\(JP=qe_z\) remain valid, where \(P=(r,\sigma,\phi,qu)^t\).

## 2. The exact trace restriction and its spatial divisibility

On either plane every derivative of r vanishes. Indeed r belongs
to the square of the base maximal ideal, and that ideal vanishes
on both planes; the chain rule therefore makes dr zero there.
The restrictions of sigma and phi are respectively zero and one,
so their W and z partials vanish there. Also \(u_W=1\) and
\(u_z=0\) on either plane by (1).

The trace identity consequently reduces to \(\sigma_Y=0\) on
each plane. In the actual polynomial quotient by ell, both the
value and first Y derivative of sigma vanish at Y=0 and Y=1.
Polynomial division over \(\mathbb C[W,z]\) proves
\[
\boxed{\quad
\sigma|_{\ell=0}\in
Y^2(Y-1)^2\mathbb C[Y,W,z].
\quad}
\tag{2}
\]
The two squared factors are comaximal, so this is divisibility
by their product, not just by each separately. It is only an
identity after restriction to ell=0. No spatial degree bound
on sigma has been assumed.

## 3. The full matrix and the retained canonical cubic identity

Define polynomial coefficients on the plane \(\mathfrak P_i\) by
\(a_i=\sigma_\ell\), \(b_i=\phi_\ell\),
\(\gamma_i=\phi_Y\), \(d_i=u_\ell\), and \(e_i=u_Y\),
where each partial is taken before restriction. Then
\[
\begin{gathered}
J|_{\mathfrak P_i}=
\begin{pmatrix}
0&0&0&0\\
a_i&0&0&0\\
b_i&\gamma_i&0&0\\
qd_i&qe_i&q&0
\end{pmatrix},\\
J^3|_{\mathfrak P_i}=q a_i\gamma_i\,e_z e_\ell^t.
\end{gathered}
\tag{3}
\]
All entries belong to \(\mathbb C[W,z]\). Multiplication of the
displayed matrix proves its cubic formula directly.

There is an independent exact expression from
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md):
in the original coordinates,
\(J_{\rm old}^3=qN(x_{\rm old})(L,0)\).
Let K be the constant three-by-three derivative matrix of the
good-coordinate change. Its first row is L_0. Conjugating the
last identity transforms its column to
\(N(\ell,Y,W,z)^t\) and its row to \((L K^{-1},0)\).
On either plane the latter row is exactly \(1,0,0,0\), because
L specializes to L_0 and \(L_0K^{-1}=e_\ell^t\). Thus
\[
\boxed{\quad
a_i\gamma_i=N(z)|_{\mathfrak P_i}.
\quad}
\tag{4}
\]
This keeps the original canonical normalization of N throughout.
If one instead defined a new determinant field in the changed
coordinate order, its determinant factor would have to be kept.

## 4. Units on the simple plane, zero product on the double

The connected additive action preserves every reduced component
of its invariant fiber. Indeed it acts on the finite set of
irreducible components, and the image of a connected group in
that discrete set is one point. Therefore N descends to each
component and to its cylinder. It kills u.

Both components are collapsed, so their rings are \(\mathbb C[c_i]\)
and their original good coordinates have no dependence on c_i.
The retained primitive whole-fiber theorem54 is nonzero at the
generic scheme of each component. At the multiplicity-one
component that local scheme is reduced. Consequently N is
nonzero on its reduced line. A nonzero LND of \(\mathbb C[c_1]\)
is a nonzero constant translation. Since z has coefficient one
on c_1 in the reconstruction98, its value is the same nonzero
constant. On the fixed double component, by contrast, N is zero
on the reduced ring. Hence (4) gives
\[
\begin{gathered}
N(z)|_{\mathfrak P_1}=\nu\in\mathbb C^*,\qquad
a_1\gamma_1=\nu,\qquad a_1,\gamma_1\in\mathbb C^*,\\
a_2\gamma_2=0\text{ in }\mathbb C[W,z],
\qquad a_2=0\text{ identically or }\gamma_2=0\text{ identically}.
\end{gathered}
\tag{5}
\]
The unit conclusions use the polynomial coordinate ring of the
entire plane, whose only units are complex constants. The last
alternative uses that this ring is a domain, not a pointwise
choice between two vanishing factors.

In particular \(J^3\) is nonzero at every point of the simple
plane, while it is zero on the double plane. The simple plane
therefore has the regular nilpotent Jordan type of size four.
This is compatible with the global nilpotence identity.

More importantly, (5) fixes the exact failed normal-order step:
\[
\boxed{\quad
EY\equiv a_1\ell\pmod{\mathfrak P_1^2},\qquad
a_1\in\mathbb C^*,\qquad EY\notin\mathfrak P_1^2.
\quad}
\tag{6}
\]
The value is zero on the plane, its Y derivative is zero, and
the transverse ell derivative is a_1. Taylor expansion in the
actual normal coordinates \(\ell,Y-1\) proves (6). Thus (2)
cannot be promoted to a second normal order on the simple plane.
Discarding ell has discarded precisely its nonzero linear term.

The ordinary spatial divisibility (2) also does not contradict
the low group-parameter degree \(E^2Y=0\). The actual inverse
family in equation (5) of
[source-scope90](homogeneous-speed-recognition-source-scope-pass90.md)
already has arbitrary nonconstant polynomial f among its good
speeds, with \(E^2x_i=0\), \(E^2z=2\), and
\(\Omega=f'\ne0\). Its displayed polynomial inverse shows that
unbounded spatial degree is possible in this same broad frame
class. That retained family is recognized by an original slice
coordinate and does not realize the exceptional planes here.
It is only a boundary to the proposed spatial-degree argument.

## Scope and evidence

Root proposed the trace and restricted-divisibility test. Geometry
derived the full specialized matrix, used the exact canonical
cubic identity to obtain the product, and isolated the missing
ell term. Jet independently derived the simple-plane transverse
unit from its base-conormal matrix. General independently checked
the matrix, normalization, product, and normal-order outline.
The retained whole-scheme nonvanishing proof54 was reread through
EOF here; no new original socle or topology proof was read.

This note adds no numerical method and no original-frame
realization. It proves the displayed necessary distinction, not
an exclusion, global invariant coordinate, or recognition result.
No formula from the restriction to either plane is promoted to
a global normal form. All files through98 are unchanged.
