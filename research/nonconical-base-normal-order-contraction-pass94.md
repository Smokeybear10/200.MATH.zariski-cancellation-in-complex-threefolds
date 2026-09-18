# Base order equals normal order at a varying rank-one component

At a collapsed rank-one fixed component with nonzero first normal
action, every power of its normal ideal contracts to the corresponding
power of the closed base ideal. The actual affine good direction
constructed in93 consequently has a nonzero E-speed in the square
of the base ideal. This strengthens normal-order vanishing to a
statement inside the specified invariant plane.

It neither makes the direction invariant nor excludes the component.
The contraction statement itself does not require multiplicity two.

## 1. Actual local data

Retain the supplied nonconical quadratic frame, its exact primitive
Jacobian field N, and a collapsed generically rank-one fixed component
as in [conormal93](nonconical-collapsed-conormal-layer-pass93.md).
Write
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]\subset A,\qquad B=A[u]
 =\mathbb C[x_1,x_2,x_3,z],\qquad E=\partial_u,\\
\mathfrak q\subset A,\qquad
\mathfrak qB=\mathfrak P=(X,Y),\qquad
A/\mathfrak q=\mathbb C[\bar c],\\
O=A_{\mathfrak q},\qquad \mathfrak n=\mathfrak qO,\qquad
L=\kappa(\mathfrak q)=\mathbb C(\bar c),\qquad
\mathfrak m=\mathfrak q\cap S .
\end{gathered}
\tag{1}
\]
The point \(\mathfrak m\) is closed. X and Y are the actual
affine-linear good normal coordinates, and u is the canonical
slice \(Ez/q\), with \(q=E^2z\in\mathbb C^*\). The actual field
\(\mathbb C(c)\subset O\) identifies with L under reduction.

After a constant affine change of the two base coordinates, put
\(x=s_1-s_1(\mathfrak m)\) and
\(f=s_2-s_2(\mathfrak m)\), with dx nonzero generically.
The rank-one construction of
[curvilinear93](nonconical-curvilinear-fiber-action-pass93.md)
supplies a second regular parameter y and
\[
\begin{gathered}
f\equiv\alpha(c)x\pmod{\mathfrak n^2},\qquad
\operatorname{gr}_{\mathfrak n}O=L[\xi,\eta],\\
Nx=0,\qquad
Ny\equiv-\epsilon_0\alpha'(c)x\pmod{\mathfrak n^2},
\qquad \epsilon_0\in L^*,\\
\text{the first normal action is nonzero}
\quad\Longleftrightarrow\quad
\alpha'(c)\ne0
\quad\Longleftrightarrow\quad
\alpha(c)\notin\mathbb C .
\end{gathered}
\tag{2}
\]
Assume this nonzero-action case. It is the varying projective
column case of the quotient conormal matrix, not a statement
about the original E-velocity Jacobian rank. The first normal
action means the induced endomorphism of
\(\mathfrak n/\mathfrak n^2\); it differs from the action on
the whole Artinian fiber.

## 2. Exact contraction of every power

Let \(g\in S\) be nonzero and let k be its order at the closed
point \(\mathfrak m\). Its Taylor expansion in the two affine
base parameters starts with a nonzero homogeneous polynomial
\(G_k\in\mathbb C[U,V]\) of degree k. Substitution of (2) gives
the degree-k normal initial form
\[
\operatorname{in}_{\mathfrak n}(g)
=G_k(1,\alpha(c))\,\xi^k\ne0 .
\qquad
\operatorname{ord}_{\mathfrak n}(g)
=\operatorname{ord}_{\mathfrak m}(g).
\tag{3}
\]
Indeed \(G_k(1,T)\) is a nonzero polynomial: dehomogenizing a
nonzero homogeneous binary polynomial at U=1 cannot kill it.
A nonconstant rational function \(\alpha(c)\) is transcendental
over \(\mathbb C\), so its substitution cannot kill that
polynomial either. All later Taylor terms have normal order
at least k+1. This also handles k=0.

Consequently, for every positive integer r,
\[
\boxed{\qquad
S\cap\mathfrak n^r
=S\cap\mathfrak q^r
=S\cap\mathfrak P^r
=\mathfrak m^r .
\qquad}
\tag{4}
\]
The first equality with \(\mathfrak m^r\) follows from (3).
For the other intersections, the inclusion from
\(\mathfrak m^r\) follows from \(\mathfrak m\subset\mathfrak q\).
The reverse inclusion follows by localizing at \(\mathfrak q\).
For the intersection with B, use
\(\mathfrak P^r=\mathfrak q^rB\) and the polynomial-extension
contraction \(\mathfrak q^rB\cap A=\mathfrak q^r\).
No reducedness of a thickened fiber, coefficient-field embedding
into the base, or flatness for an additional subring is assumed.
The proof only uses the actual local normal initial form.

## 3. Original E-speed and a second intrinsic derivative

The first-layer proof93 gives a nonzero affine-linear good normal
coordinate \(L_0\in\mathfrak P\) with
\(EL_0\in\mathfrak P^2\). Its speed belongs to S, since it is a
constant combination of the three good speeds. Equation (4)
therefore gives
\[
\begin{gathered}
\boxed{\ 0\ne EL_0\in\mathfrak m^2S\ },\qquad
a_0=L_0-uEL_0\in\mathfrak q,\qquad N^3a_0=0,\\
Na_0\in\mathfrak q^2
\quad\Longrightarrow\quad
N^2a_0\in\mathfrak m^2S .
\end{gathered}
\tag{5}
\]
The speed is nonzero by the exact
[cyclic common-invariant omission90](nonconical-cyclic-fiber-omission-pass90.md).
Otherwise the nonconstant good affine coordinate \(L_0\) would
be killed by both E and the original \(\partial_z\), contrary
to that theorem. Thus the stronger order condition is not being
obtained by setting the speed to zero.

The implication in the last line retains its stated additional
premise. N preserves \(\mathfrak q\) because this is a fixed
component, and hence preserves its square. Therefore \(N^2a_0\)
belongs to \(\mathfrak q^2\) if \(Na_0\) does. The quadratic
degree identity makes \(N^2a_0\in\ker(N|_A)=S\).
Apply (4) with r=2. In multiplicity two the premise is already
supplied, for a suitable \(L_0\), by
[double-fiber93](nonconical-double-fiber-normal-order-pass93.md).
The first-layer rank conditions in93 supply other cases.
The implication itself does not assume an unproved extension
of those normal-order conclusions.

The subsequently saved
[weighted conormal theorem94](nonconical-weighted-conormal-rigidity-pass94.md)
now supplies a suitable \(L_0\) with \(Na_0\in\mathfrak q^2\)
at every multiplicity \(\mu\ge2\) in this actual collapsed
rank-one setting. Thus the premise in (5) is available throughout
the nonzero first-normal-action sector considered here. This
forward consequence uses that separate proof; it does not
change the conditional argument above or assert \(Na_0=0\).

The exact identity \(N^3a_0=0\) comes from the generic quadratic
degree bound on centered good coordinates, not from a new
filtration hypothesis. The proof of (3)--(4) works at every
whole-fiber multiplicity where (2) has nonzero first normal action.

## 4. Boundaries

If \(\alpha\) is constant, the argument in (3) fails precisely
because a nonzero homogeneous polynomial can vanish at
\((1,\alpha)\). No all-power contraction theorem is claimed
for that sector.

Second base order does not make the centered generator invariant.
In the retained intrinsic polynomial comparison
\(D=p\partial_y-2y\partial_c\), with invariant plane
\(S_0=\mathbb C[p,pc+y^2]\), take \(a_0=p+y^2\).
At its fixed component \((p,y)\), the base ideal is
\(\mathfrak m_0=(p,pc+y^2)\). Directly,
\(Da_0=2py\ne0\), \(D^2a_0=2p^2\in
\mathfrak m_0^2\setminus\mathfrak m_0^3\), and \(D^3a_0=0\).
This controls the last implication in (5) and its order;
it is not an original nonconical-frame realization or a
counterexample to any stronger use of E.

The new assertion is the all-power contraction (4) and its
actual-speed consequence (5). It gives neither a common invariant
coordinate nor a contradiction at the fixed component. No
pass54 full filtration, numerical method, new external theorem,
historical novelty, or general cancellation result is asserted.
Pass93 and earlier files are unchanged.
