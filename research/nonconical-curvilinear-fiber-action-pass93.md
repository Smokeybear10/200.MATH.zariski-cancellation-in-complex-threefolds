# The exact action on a generically rank-one fixed fiber

At a generically rank-one fixed component in the actual nonconical
frame, the transverse whole fiber is curvilinear. The canonical
Jacobian derivation sends its Artinian ring into the socle, kills its
maximal ideal, and has square zero there. Its first action on the
normal space of the reduced component need not vanish.

These are local restrictions, not a new recognition theorem. They
neither exclude rank-one fixed components nor apply automatically to
the rank-zero components left in the cubic multiplicity list.

## 1. The actual ring and the generic rank hypothesis

Retain the actual primitive Jacobian field N, smooth threefold A,
invariant plane S, and faithful-flat quotient from
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md) and
[fixed-scheme92](nonconical-fixed-scheme-structure-pass92.md).
Let m be a closed point of S and let \(\mathfrak q\) be the generic
prime of a reduced fixed component of its fiber. Thus
\[
\begin{gathered}
O=A_{\mathfrak q},\qquad \mathfrak n=\mathfrak qO,\qquad
L=\kappa(\mathfrak q),\qquad \dim O=2,\\
J=mO,\qquad T=O/J,\qquad
\mu=\operatorname{length}_O T\ge2,\\
\operatorname{rank}_L(ds_1,ds_2)
\text{ in }\Omega_{A/\mathbb C}\otimes_A L=1.
\end{gathered}
\tag{1}
\]
The last rank is in the ambient cotangent module, not the
automatically zero images in the differentials of L. The inequality
uses the retained componentwise primitive-fiber theorem54. The new
argument below also proves nonvanishing directly in this rank-one
case.

After an invertible constant linear change of the two base
coordinates, take \(x=s_1-s_1(m)\) with nonzero differential modulo
\(\mathfrak n\), and put \(f=s_2-s_2(m)\). Then \(J=(x,f)\).
Choose an actual \(t\in A\) whose residue in L is transcendental
over \(\mathbb C\). Every nonzero polynomial in t is outside
\(\mathfrak q\), so \(K=\mathbb C(t)\subset O\), and L is finite
separable over K.

As in [primitive-fiber54, Section 3](primitive-fiber-nonvanishing-pass54.md),
O is essentially smooth over K. The conormal map to its separable
residue field identifies \(\mathfrak n/\mathfrak n^2\) with
\(\Omega_{O/K}\otimes_O L\). Thus x can be completed by a parameter
\(y\in\mathfrak n\) such that \(dx,dy\) form an O-basis of
\(\Omega_{O/K}\). The three differentials \(dx,dy,dt\) form a
basis of \(\Omega_{O/\mathbb C}\).

Write \(\partial_x,\partial_y,\partial_t\) for its dual
derivations. These preserve the actual ring O and are defined by
that differential basis; they are not partial derivatives in an
assumed global polynomial coordinate system. In particular
\(\partial_t x=\partial_t y=0\). No coefficient field in a
completion is being assumed in this construction.

## 2. The whole Artinian action

The local unit-factor calculation in fixed-scheme92 retains the
original fourth differential du and gives, after choosing orientation,
\[
N|_O=\epsilon\bigl(f_y\partial_t-f_t\partial_y\bigr),
\qquad \epsilon\in O^*,\qquad Nx=0.
\tag{2}
\]
N preserves \(\mathfrak q\) because the component is fixed; hence it
extends as a derivation to O. This does not assert that localization
at arbitrary noninvariant denominators preserves local nilpotence.
The formula and the following quotient identities are sufficient.

The ring \(D=O/(x)\) is a regular local ring of dimension one,
with parameter \(\bar y\). Since J is primary to \(\mathfrak n\),
\[
\bar f=a\bar y^\mu\quad\text{in }D,\qquad a\in D^*,
\qquad
f_t\in J,\qquad
f_y\bmod J=(\mu a+\bar y\,\partial_y a)\bar y^{\mu-1}\bmod(\bar f).
\tag{3}
\]
The exponent is \(\mu\) because length in this DVR equals its
parameter order. Both \(\partial_t\) and \(\partial_y\) descend to
D. The first fixes \(\bar y\), so
\(\partial_t\bar f=(\partial_t a)\bar y^\mu\), which proves
\(f_t\in J\). The second identity is the ordinary product rule
in D. Its parenthesized coefficient is a unit, since the
characteristic is zero. Thus \(N(t)\) is a nonzero generator of
the one-dimensional L-socle of T.

Every differential of an element of O is an O-linear combination
of \(dx,dy,dt\). Formula (2) and (3) therefore imply
\[
\boxed{\quad
\bar N(T)\subset\operatorname{Soc}(T)
   =\bar y^{\mu-1}T,\qquad
\bar N(\mathfrak nT)=0,\qquad
\bar N^2=0,\qquad \bar N(t)\ne0.
\quad}
\tag{4}
\]
For the middle assertion, \(\mathfrak nT=\bar yT\);
\(\bar N(\bar y)=0\) and \(\bar y\) annihilates the socle.
For the square assertion, the image of a socle element
\(\bar y^{\mu-1}a_0\) is
\(\bar y^{\mu-1}\bar N(a_0)\), which is zero since
\(2\mu-2\ge\mu\). In particular \(\bar N\) also kills the socle.
This is a nonzero derivation of a nonreduced ring, not a nonzero
derivation of its residue field.

For precision about terminology, T is curvilinear:
noncanonically \(T\simeq L[\eta]/(\eta^\mu)\) as a K-algebra.
Indeed T is an Artinian local K-algebra with separable residue
extension L/K. A primitive element of L has separable minimal
polynomial, whose simple residue root lifts to T by the finite
Newton correction process: each correction raises the nilpotent
error order, and the derivative is a unit. This embeds L in T
over K. The powers of \(\bar y\) then give the asserted presentation.
This optional description is not needed for (3)--(4), and its
coefficient field is not asserted to be killed by \(\bar N\).

## 3. The first normal action is a different quotient

Let \(\alpha=f_x\bmod\mathfrak n\in L\), and let
\(\delta_t\) be the unique extension to L of the usual derivation
of \(K=\mathbb C(t)\). The derivation \(\partial_t\) preserves
\(\mathfrak n=(x,y)\) and induces exactly \(\delta_t\) on L.
Rank one gives
\(f\equiv\alpha x\pmod{\mathfrak n^2}\), interpreted with any
lift of \(\alpha\). Differentiating this congruence by
\(\partial_t\), which preserves \(\mathfrak n^2\), gives
\[
Nx=0,\qquad
Ny\equiv-\epsilon_0\,\delta_t(\alpha)\,x
       \pmod{\mathfrak n^2},\qquad
\epsilon_0=\epsilon\bmod\mathfrak n\in L^*.
\tag{5}
\]
Here N induces an L-linear endomorphism on
\(\mathfrak n/\mathfrak n^2\), because \(N(O)\subset\mathfrak n\).
It has square zero and rank at most one. It can have rank one
even though N kills the maximal ideal of the different quotient
T. The parameter x is zero in T but not in
\(\mathfrak n/\mathfrak n^2\).

Reuse the triangular polynomial family, with any integer
\(\mu\ge2\):
\[
\begin{gathered}
A_0=\mathbb C[x,y,t],\qquad
S_0=\mathbb C[x,f],\qquad f=xt+y^\mu,\\
D_0=\mu y^{\mu-1}\partial_t-x\partial_y,\qquad
\ker D_0=S_0,\qquad
I_0=(x,y^{\mu-1}),\\
T_0=\mathbb C(t)[y]/(y^\mu),\qquad
\bar D_0(t)=\mu y^{\mu-1},\quad
\bar D_0(y)=0,\qquad
D_0y=-x.
\end{gathered}
\tag{6}
\]
The field is triangular and locally nilpotent, and its coefficients
have gcd one. Its kernel is \(S_0\): after inverting x use the
coordinate y and invariant f, and descend by the injective
substitution \(\mathbb C[f]\to\mathbb C[y]\),
\(f\mapsto y^\mu\), canceling powers of x successively.
Its first normal action is nonzero, with \(\alpha=t\).
This is the retained triangular family with changed names and sign,
not a new construction or an actual nonconical original frame.

## 4. Exact limits and verification

The total multiplicity theorem92 gives \(\mu\le2d\le6\) in the
actual setting. If a relative good generator remains nonconstant,
the individual bound improves to \(\mu\le d\). Formula (4) holds
for every such generically rank-one fixed component regardless
of which bound applies. Neither bound makes (5) vanish.

No assertion about rank-zero Artinian complete intersections is
obtained by replacing them with this curvilinear presentation:
their maximal ideal has two generators. In particular, the cubic
profiles consisting of a rank-zero component of multiplicity four
or five and additional reduced components remain outside this
lemma. Formal first jets and the reused polynomial comparison do
not establish an actual polynomial inverse frame for them.

The complete retained rank-one Hamiltonian calculation92 and the
local-coordinate and socle argument54 were read for deduplication.
The new content here is the precise whole-fiber action (4) and its
distinction from the first normal action (5). The proof uses those
actual differential bases and elementary DVR arithmetic; it does
not claim a fresh read of the original socle-theorem proof.
No numerical method, global recognition assertion, frozen edit,
or historical novelty claim is added.
