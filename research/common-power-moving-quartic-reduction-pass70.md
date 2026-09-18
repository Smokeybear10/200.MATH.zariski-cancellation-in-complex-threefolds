# Rational recognition and the remaining localized symmetry in a moving quartic

In the dependent common-power moving quartic, the constant-top
companion calculations can be repeated after invariant division.
Their two nonconstant residual-pair cases are recognized by the
original rational two-direction theorem, without a polynomial
curve parameter or an assumed invariant denominator for the
correction. A collinear constant first pair is recognized too.

The remaining constant-pair case gives a three-direction symmetry
that is an actual LND of the invariant localization. Its original
slice proves that the inverted factor is fixed. This still does
not justify the global coordinate-section endpoint of the
constant-top proof. The precise surviving localization is
recorded below.

## 1. Actual common-power input

Let
\[
B=k[x_1,x_2,X,Y],\quad k=\mathbb C,\quad
E\in\operatorname{LND}(B),\quad Es_*=1,\quad A=\ker E.
\]
The actual coordinate partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Write \(W_i=[E,T_i]\) and
\(V_i=\operatorname{ad}_E^2T_i\) for the bad indices.
Retain the dependent decomposition and nonzero-commutator branch
\[
V_X=aD,\quad V_Y=bD,\quad
[E,D]=0,\quad a,b\in\ker E\cap\ker D,
\]
\[
D\text{ primitive and locally nilpotent},\quad
a,b\text{ have no nonzero complex constant relation}.
\]
The common-power highest data are normalized by actual constant
changes in the good and bad pairs to
\[
E^4x=cg^4,\quad E^5x=0,\quad c=e_1,\quad
E^3(X,Y)=(g^3,0),\quad
g\in(\ker E\cap\ker D)\setminus k.
\tag{2}
\]
Write \(z=E^3x\), \(Dz=c\theta\), and
\(\rho=a z_X+b z_Y=g^4r\), with \(r\ne0\).
The inherited dependent highest-vector calculation gives
\[
a=gr,\qquad \operatorname{rank}(E,D)=2,\qquad E\theta=0.
\tag{3}
\]
No assertion \(D\theta=0\) is required. The common-power assumption
(2) concerns both highest layers, not merely the fourth iterate.
The separate [finite-root theorem](dependent-algebraic-root-top-pass70.md)
supplies this common-power input in the remaining dependent moving
quartic. The present deduction begins with the actual polynomial
\(g\), not a root in an unproved coordinate extension.

Put \(\delta=E/g\) on \(B_g\). The actual next bad-column
coefficient and direct rescaling give
\[
W_i g=-\frac{a_i\theta}{2g^3},\qquad
\widetilde V_i=\operatorname{ad}_\delta^2T_i
=\frac{a_i}{g^2}\left(D-\frac{\theta}{g^4}E\right),
\quad (a_X,a_Y)=(a,b).
\tag{4}
\]
Thus the normalized defects have rank one, their line is
independent of \(\delta\), and \(\widetilde V_X\ne0\).
The highest good and bad identities retain all the normalized
adjoint bounds. In particular \(\delta^4x=c\) and
\(\delta^3(X,Y)=(1,0)\).
Coordinate partials are not asserted to be LNDs on \(B_g\).

## 2. The first full image and a rational two-direction field

For the remainder of this note set
\[
h_j=\delta^jx,\quad P=h_1,\quad J=\operatorname{Jac}P,\quad
\mathcal D=\widetilde V_X,\quad
\widetilde V_Y=\eta\mathcal D,\quad \eta=b/a,
\]
\[
d=\mathcal D(x),\quad \ell=(0,0,1,\eta),\quad
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}.
\]
Here \(\eta\) is rational, \(\delta\eta=0\), and the ordinary
partial derivatives are still those of the original coordinates.
The divided flow and its conjugated partials give inverse
polynomial matrices over \(\operatorname{Frac}(B)[t]\).
Consequently the full constant-quartic companion identities hold:
\[
M^4=0,\quad \operatorname{Jordan}(M)=(4,1),\quad
\operatorname{rank}M^3=1,\quad \operatorname{rank}M^2=2,
\]
\[
(M^j)_{\rm UL}=\operatorname{Jac}h_j/j!,\qquad
j!M^j|_{\rm base}
=\binom{\operatorname{Jac}h_j}
 {j\ell\operatorname{Jac}h_{j-1}}\quad(j\ge1).
\tag{5}
\]
These are pointwise field-matrix identities. They do not
differentiate \(\ell\). The block descent uses only \(d,\ell\ne0\).
It is the same algebra as
[the constant-quartic proof, Sections 1--2](dependent-constant-quartic-closure-pass68.md),
not an application of that proof's global theorem to \(B_g\).

The rank-one first image gives
\[
h_3=c\sigma+e,\quad
\sigma\in B_g,\quad e\in k^4,\quad e_B=(1,0),\quad
\delta\sigma=1.
\tag{6}
\]
The constants follow by applying all four ordinary partials,
whose common constant field is \(k\).
Put
\[
(h_2)_B=e_B\sigma+(F,G),\qquad
s_0=F+\eta G,\qquad
\beta=\frac{\sigma-2s_0}{3},\qquad S=T_e+\beta T_c.
\]
Then the full lower row and velocity give
\[
\delta F=\delta G=0,\quad dF+\eta\,dG=0,\quad
Jc=\frac32d,\quad
Je=\frac c3+\left(s_0-\frac{\sigma}{2}\right)d.
\tag{7}
\]
In the one-form identity, \(d\) denotes ordinary differential,
not the column \(d=\mathcal D(x)\).
These equations imply
\[
[\delta,S]=0,\quad \delta\beta=\frac13,\quad
S\sigma=SF=SG=0,\quad S(P_B)=0.
\tag{8}
\]
For example, commutation applied to \(h_3\) and \(h_2\) gives
\(Sh_3=\delta^3(Sx)=0\) and \(Sh_2=\delta^2(Sx)=0\).
The bad components then give \(SF=SG=0\).
No local nilpotence or denominator invariance of \(S\) is assumed.

## 3. Recognition unless the first pair is constant and transverse

If \(G\notin k\), Lie differentiation of the full one-form in
(7), using (8), gives
\[
0=d(SF)+(S\eta)dG+\eta\,d(SG)=(S\eta)dG.
\]
Thus \(S\eta=0\) and \(S\beta=0\). If \(G=0\), (7) gives
\(F\in k\), so again \(S\beta=0\).
The constant directions \(c,e\) are independent because their
bad projections are \(0,(1,0)\). Complete them to an actual
constant coordinate frame with \(T_c=\partial_\xi\) and
\(T_e=\partial_\zeta\).
The original \(E,s_*,g\), the actual good \(\partial_\xi\), and
\(S=\partial_\zeta+\beta\partial_\xi\) then satisfy the
[rational two-direction recognition theorem](rational-two-direction-recognition-pass69.md)
with \(\kappa=1/3\). Therefore
\[
\boxed{G\notin k\ \text{or}\ G=0
\quad\Longrightarrow\quad A\simeq k^{[3]}.}
\tag{9}
\]
That theorem supplies original commutation using the original
slice, and treats its two rational coefficient alternatives
without assuming that every rational nice field is an LND.

If \(G\in k^*\), (7) forces \(F\in k\). Hence the only remaining
first pair has the form
\[
(F,G)=\mu=(\mu_1,\mu_2)\in k^2,\qquad \mu_2\ne0.
\tag{10}
\]
Equivalently \(e_B,\mu\) are linearly independent.
This is the exact constant-transverse alternative, not an
unproved constancy assumption about a residual pair.

## 4. The second full image and another recognition alternative

Under (10), set \(s_0=\mu_1+\eta\mu_2\).
The two vectors
\[
v=\binom{c}{3},\qquad
w=\binom{e}{2s_0-\sigma}
\]
span \(\operatorname{im}M^2\): they come from the first image
and the velocity column, and their upper components are
independent. Full base-column comparison then gives actual
localized functions and a constant vector
\[
h_2=c\tau+e\sigma+v_0,\qquad
\tau\in B_g,\quad v_0\in k^4,\quad (v_0)_B=\mu,\quad
\delta\tau=\sigma,
\]
\[
\ell J=\frac32\,d\tau+
       \left(s_0-\frac{\sigma}{2}\right)d\sigma.
\tag{11}
\]
An actual component of \(h_2-e\sigma\), divided by a nonzero
constant component of \(c\), defines \(\tau\).
The other components have zero ordinary gradient, so give
\(v_0\). No arbitrary rational one-form has been integrated.

Define
\[
u_0=\tau-\frac{\sigma^2}{2},\qquad
Z_B=P_B-e_B\left(\frac{3\tau}{2}-\frac{\sigma^2}{4}\right)
             -\mu\sigma.
\tag{12}
\]
The lower row of (11), with those actual differentials subtracted,
gives
\[
\delta u_0=\delta Z_B=0,\qquad
dZ_1+\eta\,dZ_2=0.
\tag{13}
\]
Also (8) and \(Sh_2=0\) give \(S\tau=Su_0=0\), and then
\(SZ_B=0\).
If \(Z_B\) is nonconstant, \(Z_2\) is nonconstant by (13).
Lie differentiation now gives \((S\eta)dZ_2=0\), so
\(S\eta=S\beta=0\). The same original rational theorem proves
\[
\boxed{Z_B\notin k^2\quad\Longrightarrow\quad A\simeq k^{[3]}.}
\tag{14}
\]
No polynomial-curve factorization is needed for (9) or (14).
The denominator argument in the constant-top proof is replaced
by an exact application of the newer original-ring rational
recognition theorem.

## 5. Constant second pair: exact three-direction identities

Suppose \(Z_B=\nu\in k^2\). Write
\[
\nu=\nu_1e_B+\nu_2\mu,\qquad \nu_1,\nu_2\in k.
\]
The remaining velocity coefficient, with the full variable row
retained, is
\[
Jv_0=\frac{c\sigma}{6}+\frac e2
 -\frac{3u_0}{4}d-\frac{\sigma s_0}{2}d
 +\frac{\nu_1+\nu_2s_0}{2}d.
\tag{15}
\]
Define in the actual localization
\[
\beta_3=\frac{\sigma-\nu_2}{2},\qquad
\gamma_3=\frac{\sigma^2}{6}-\frac{\nu_2\sigma}{6}
             +\frac{u_0}{2}-\frac{\nu_1}{3},\qquad
S_3=T_{v_0}+\beta_3T_e+\gamma_3T_c.
\tag{16}
\]
The same direct coefficient calculation as in the constant-top
proof now takes place in \(B_g\), and gives
\[
[\delta,S_3]=0,\quad S_3\sigma=0,\quad
S_3u_0=\frac13,\quad
S_3\beta_3=0,\quad S_3\gamma_3=\frac16,
\]
\[
S_3^2x=\frac c6,\qquad S_3^3x=0.
\tag{17}
\]
For clarity, the first two derivative conclusions come from
commutation on \(h_3=c\sigma+e\) and
\(h_2=c\tau+e\sigma+v_0\). One has
\(\delta^2\gamma_3=1/3\), so \(S_3\tau=1/3\), and hence
\(S_3u_0=1/3\).
The sign and scalar equations (15)--(17) are algebraic;
they do not assert global polynomiality of the coefficients.

## 6. What the original slice does and does not descend

The original-slice unit argument works for this bounded coordinate
flow as well as for a nice field. In the formal rational
power-series ring, (17) makes
\(\exp(tS_3)f\) a polynomial in \(t\) for every \(f\in B\),
by the Leibniz rule. In particular this holds for \(g,s_*\).
Commutation with \(\delta\) gives
\[
\delta\bigl(\exp(tS_3)s_*\bigr)
=\exp(tS_3)(\delta s_*)
=\exp(tS_3)(1/g).
\]
The left side is a polynomial in \(t\), and multiplication by
the polynomial \(\exp(tS_3)g\) gives one.
Units of a polynomial ring over a domain are constant in \(t\).
Therefore
\[
S_3g=0,\qquad [E,S_3]=0,\qquad
S_3\in\operatorname{LND}(B_g).
\tag{18}
\]
For the last statement, (17) kills high iterates of each original
polynomial generator, while \(S_3(g^{-1})=0\).
There is an integer \(N\ge0\) for which
\(g^NS_3(B)\subset B\). Its restriction is an original
polynomial LND commuting with \(E\), by the invariant-replica
and preserved-subring arguments.

The constant vectors \(c,e,v_0\) are independent because their
bad projections are \(0,e_B,\mu\). Thus an actual linear
coordinate \(z_0\), dual to \(v_0\) and killed by \(T_c,T_e\),
satisfies
\[
S_3z_0=1,\quad S_3\sigma=0,\quad
E\sigma=g,\quad E(\sigma/g)=1.
\tag{19}
\]
However the justified coordinate-section identity is only
\[
\ker(S_3|_{B_g})
\simeq B_g/(z_0)
\simeq \bigl(B/(z_0)\bigr)_{\overline g}
\simeq k^{[3]}_{\overline g}.
\tag{20}
\]
Here \(\overline g\ne0\), as follows from the actual slice
decomposition \(B_g=(\ker S_3)[z_0]\) and \(S_3g=0\).
It is not assumed to be a unit or a coordinate of the unlocalized
polynomial three-ring.
Moreover the global replica sends \(z_0\) to \(g^N\), not
necessarily to one.

Consequently (18)--(20) do not meet the global polynomial
three-ring premise of the coordinate-section recognition lemma
used in pass68. This note does not assert recognition in this
terminal alternative or that the original invariant localization
is itself a polynomial ring.

One actual shear makes the remaining distinction particularly
explicit. Complete the constant directions to coordinates
\((a_0,b_0,z_0,w_0)\) with
\(T_c=\partial_{a_0}\), \(T_e=\partial_{b_0}\), and
\(T_{v_0}=\partial_{z_0}\).
Put \(a'_0=a_0-z_0^2/12\), fixing the other coordinates.
The good \(T_c\) is unchanged, and
\[
S_3=\partial_{z_0}+\beta_3\partial_{b_0}
       +(\gamma_3-z_0/6)\partial_{a'_0},\qquad
S_3^2(a'_0,b_0,z_0,w_0)=0.
\tag{21}
\]
This is a rational nice field with three constant output
directions. The two rational coefficients are fixed by \(S_3\),
but no relation reducing them to one coefficient is supplied.
The two-direction theorem from pass69 therefore does not
automatically recognize this terminal case.

## Dependencies and verification boundary

The common-power input and primitive decomposition are the exact
ones already specified in the dependent highest-vector and
preceding-layer notes. The first and second full-image calculations,
including the variable auxiliary row, have been reconstructed
from the constant-quartic proof. Only their algebraic field
identities transfer automatically.

The recognition deductions (9),(14) instead use the complete
original-slice rational two-direction theorem from pass69.
The bounded-flow unit argument in Section 6 is written in full.
No new curve theorem, finite test, regression, metadata integration,
historical novelty conclusion, human expert review, or formal
verification is asserted. This note is separate from the pass69
checkpoint.
