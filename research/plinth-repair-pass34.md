# A degree-preserving repair and an exact obstruction to the usual gauge path

The extra plinth divisors constructed in pass 33 can be removed by a
genuine polynomial gauge while keeping the fixed canonical action and
degree one at every parameter value. However, the standard operation
that rescales the slice parameter inside a supplied coordinate gauge
has an exact obstruction: it stays at degree one only in a vertical
shear sector whose primitive top already has a slice.

For the entire pass-33 family, that standard scaling path has degree
five at every intermediate nonzero parameter, although both endpoints
have degree one. A different path really does repair the plinth.
Thus the choice of path matters; the supplied gauge alone does not
give a degree-preserving deformation by parameter scaling.

The repair path is not generally a single additive-group flow on the
four-variable ring. It becomes such a coordinate flow after adjoining
its path parameter. This distinction is proved below, not suppressed.
There is no claim that every degree-one horizontal admits the special
normal form used in the repair, or that any construction descends to
an unknown stable-polynomial threefold.

## 1. Fixed model and conventions

Let
\[
B=\mathbb C[x,\lambda,w,z],\quad v=1+\lambda x,\quad
\Delta w=x^2,\quad \Delta z=2v^2w,\quad
\Delta x=\Delta\lambda=0.
\tag{1}
\]
This is the unchanged canonical local-slice model with input
\(D=x^2\partial_y+2y\partial_z\), full input plinth \(x^2\ker D\),
and multiplier \(d=x\).
For
\[
\mathcal H_x=\{\delta\in\operatorname{LND}(B):
                         \delta x=0,\ \delta\lambda=1\},
\]
the largest nonzero adjoint order \(q(\delta)\) has global minimum
one, by the full-class argument in
[pass 31](minimal-horizontal-pass31.md).

Write \(A=\mathbb C[x,\lambda,b,c]\), and
\(J_G=G_c\partial_b-G_b\partial_c\).
For \(p(x)\) with \(p(0)=1\), define
\[
h=x^2c-b^2,\qquad F_p=p b+x^2h^2,
\]
\[
H_p=h-2\lambda xpF_p^2,\qquad
W_p=b+4\lambda x^3hF_p^2-4\lambda^2x^4pF_p^4,
\]
\[
Z_p=(H_p+v^2W_p^2)/x^2.
\tag{2}
\]
The actual isomorphism
\[
\theta_p:B\longrightarrow A,\qquad
\theta_p(w)=W_p,\quad \theta_p(z)=Z_p
\tag{3}
\]
fixes \(x,\lambda\). Its explicitly polynomial inverse, including
the \(x^2\)-divisibility in both directions, is proved in
[pass 33](minimum-top-structure-pass33.md), Sections 2--3.
No inverse of \(p\) is used.

The horizontal and its relative vertical pencil are
\[
\delta_p=\theta_p^{-1}\partial_\lambda\theta_p,\qquad
\theta_p\Delta\theta_p^{-1}
 =D_0-4\lambda xpF_pL_p,
\]
\[
D_0=x^2\partial_b+2b\partial_c,\qquad
L_p=J_{F_p}.
\tag{4}
\]
The primitive \(L_p\) has exact kernel and plinth
\[
\ker L_p=\mathbb C[x,F_p],\qquad
\operatorname{pl}(L_p)=p\,\mathbb C[x,F_p],
\tag{5}
\]
and fixed coefficient ideal \((p,h)\). These all-degree statements,
including repeated roots, were proved by pole contraction in pass 33.
Here \(p\) denotes the chosen top plinth, not the fixed input plinth.

## 2. An actual degree-one repair bridge

Fix \(p\) as above and introduce an independent parameter \(t\). Put
\[
p_t=1+(1-t)(p-1)=p+t(1-p).
\tag{6}
\]
The identity \(p_t(0)=1\) holds over \(\mathbb C[t]\). All formulas
in (2)--(3) and their inverses are polynomial over this parameter ring:
the proof of divisibility uses only that identity and polynomial
operations, not inversion of any function of \(t\).

Consequently
\[
G_t=\theta_{p_t}^{-1}\theta_p
\tag{7}
\]
is an actual automorphism of \(B[t]\) fixing \(x,\lambda,t\).
Its inverse is \(\theta_p^{-1}\theta_{p_t}\). It specializes to the
identity at \(t=0\), and
\[
G_t\delta_pG_t^{-1}=\delta_{p_t}.
\tag{8}
\]
This equation specifies the direction of conjugation; the maps in
(3) are homomorphisms from the physical ring to the quotient frame.

For every scalar \(\tau\in\mathbb C\), equation (4) with \(p_\tau\)
has nonzero coefficient of \(\lambda\) and no higher coefficient.
Therefore
\[
q(\delta_{p_\tau})=1\quad\hbox{for every }\tau,\qquad
\operatorname{pl}(L_{p_1})=(1).
\tag{9}
\]
This is a genuine degree-preserving repair of a supplied member of
the family. At the endpoint \(p_1=1\), the explicit coordinates
\((F_1,S_1)\) from pass 33, equation (33), make
\(L_1=-\partial_{S_1}\).

More generally any two normalized \(p,r\) can be connected by replacing
(6) with \((1-t)p+tr\). The coordinate transition maps obey the exact
groupoid identity
\[
(\theta_s^{-1}\theta_r)(\theta_r^{-1}\theta_p)
 =\theta_s^{-1}\theta_p.
\tag{10}
\]
This is an identity of actual polynomial maps, not an inference from
their Jacobians.

There is no gradual decrease of degree in the particular path (6).
If \(p\) is nonconstant, then
\[
\deg_xp_\tau=\deg_xp\quad(\tau\ne1),\qquad
\deg_xp_1=0.
\tag{11}
\]
The drop is at the endpoint. For example, when \(p=1-x\), the
fixed fiber is \(x=1/(1-\tau)\) for \(\tau\ne1\), and disappears
from the affine \(x\)-line at \(\tau=1\).
Equation (11) is not a well-founded sequence of local decreases or
a complexity bound for finding repairs outside this family.

## 3. Why this path is not generally a single four-variable flow

The family \(G_t\) is regular with polynomial inverse, but the
additive law \(G_{t+u}=G_tG_u\) does not hold when \(p\ne1\).
This can be checked in the first \(\lambda\)-jet, without a large
expansion of the full maps.

Use independent auxiliary variables \(b,h\). Let
\[
A_p=4x^3h(p b+x^2h^2)^2.
\]
The forward map in (2) sends \(b\) to
\(b+\lambda A_p+O(\lambda^2)\); its inverse has the negative
first coefficient. Hence the first coefficient of the \(w\)-image
under (7), with \(r=p_t\), is
\[
A_p-A_r
=4x^3h\left[(p b+x^2h^2)^2
                 -(r b+x^2h^2)^2\right].
\tag{12}
\]
The coefficient of \(t^2\) in (12) is
\[
-4x^3h(1-p)^2b^2,
\tag{13}
\]
which is nonzero for \(p\ne1\). On the physical ring at
\(\lambda=0\), substitute \(b=w\) and \(h=x^2z-w^2\);
the polynomial remains nonzero.

Every \(G_t\) is the identity modulo \(\lambda\). An additive group
law for such maps would imply that their first \(\lambda\)
coefficients are additive polynomials in \(t\), hence linear in
characteristic zero. Equation (13) contradicts that consequence.
This disproves the additive law for this particular path; it does
not exclude a different single-flow repair.

There is nonetheless an exact additional-parameter lift. On \(B[t]\)
define
\[
\mathcal D=\theta_{p_t}^{-1}\partial_\lambda\theta_{p_t},
\qquad
\mathcal T=\theta_{p_t}^{-1}\partial_t\theta_{p_t}.
\tag{14}
\]
Both are actual coordinate LNDs, since \(\theta_{p_t}\) is an actual
polynomial isomorphism over the full parameter ring. They satisfy
\[
[\mathcal T,\mathcal D]=0,\quad
\mathcal T(t)=1,\quad\mathcal T(\lambda)=0,\quad
\mathcal D(t)=0,\quad\mathcal D(\lambda)=1.
\tag{15}
\]
Thus the additive flow of \(\mathcal T\) identifies the fiber
horizontals along the path. This is a flow on the five-variable
ring \(B[t]\), not an intrinsic LND on an unknown threefold or an
asserted one-parameter subgroup of \(\operatorname{Aut}(B)\).

## 4. Marked canonical normalizers cannot perform the repair

Suppose \(\gamma\) is an actual automorphism of \(B\) satisfying
\[
\gamma x=x,\quad\gamma\lambda=\lambda,\quad
\gamma\Delta\gamma^{-1}=a\Delta\quad(a\in\mathbb C^*),
\qquad
\gamma\delta_p\gamma^{-1}=\delta_r.
\tag{16}
\]
Then necessarily
\[
p=r.
\tag{17}
\]

Indeed conjugation in (16) carries the first nonzero highest
adjoint of \(\Delta\) for \(\delta_p\) to a nonzero scalar multiple
of that for \(\delta_r\). Its restriction carries
\(\ker\delta_p\) isomorphically to \(\ker\delta_r\).
Primitivity is preserved under a polynomial isomorphism: a
principal ideal containing every derivative is transported to
such an ideal on the other side. Hence the primitive tops are
conjugate up to a constant unit.

The plinth ideals of these primitive fields are transported as
well. Since \(\gamma\) fixes \(x\), (5) implies that \(p\) and \(r\)
generate the same principal ideal in the target invariant ring.
That ring has only constant units. Therefore \(p\) and \(r\) differ
by a nonzero scalar, and \(p(0)=r(0)=1\) forces (17).

Thus distinct members of the family lie in different orbits under
the marked canonical-normalizer group (16), even though Section 2
connects them by actual degree-one polynomial gauges. In particular
the successful nontrivial repair gauges do not normalize \(\Delta\).
A mere intrinsic change of coordinates for a primitive top cannot
turn a nonunit plinth into a unit plinth either: existence of a slice
is preserved by every such conjugation.

## 5. An all-degree criterion for the standard scaling path

The following statement covers every supplied normalized
degree-one gauge, not merely the \(p\)-family.

First use the known good coordinates
\[
w=b,\qquad z=c+\lambda^2b^2.
\tag{18}
\]
They are an actual polynomial isomorphism, denoted by
\(\theta_{\rm good}:B\to A\), and give the good pencil
\[
P_\lambda=D_0+\lambda E,\qquad E=4xb\partial_c.
\tag{19}
\]

Let \(\phi\) be any actual \(\mathbb C[x,\lambda]\)-automorphism of
\(A\), normalized by \(\phi|_{\lambda=0}=\mathrm{id}\), and assume
\[
\phi^{-1}P_\lambda\phi=D_0+\lambda D_1,\qquad D_1\ne0.
\tag{20}
\]
The corresponding horizontal is
\(\phi\partial_\lambda\phi^{-1}\), with actual slice \(\lambda\).
The normalization entails no assertion that an unknown quotient
is polynomial. In this fixed canonical setting, the actual
ambient coordinate \(\lambda\) gives the supplied normalized frame
by the slice-projection argument in
[pass 30](horizontal-gauge-pass30.md).

Form the usual scaling path \(\phi_t\) by replacing \(\lambda\)
with \(t\lambda\) in the polynomial coordinate images and their
polynomial inverse. It is an actual automorphism over
\(\mathbb C[t,x,\lambda]\), and \(\phi_0=\mathrm{id}\).
Put
\[
C(\lambda)=\phi^{-1}E\phi,\qquad N=\deg_\lambda C.
\tag{21}
\]
Here the degree is the maximum degree of the two coefficient
polynomials; \(C\ne0\).
Substitution in (20) and
\(P_\lambda=P_{t\lambda}+(1-t)\lambda E\) give the exact identity
\[
\phi_t^{-1}P_\lambda\phi_t
 =D_0+t\lambda D_1+(1-t)\lambda C(t\lambda).
\tag{22}
\]

**Scaling-path criterion.** If \(N>0\), then every scalar
\(\tau\ne0,1\) has relative degree exactly \(N+1\).
If \(N=0\), the entire path has degree one.
Equivalently, the path has degree at most one at even one scalar
\(\tau\ne0,1\) if and only if \(\phi\) centralizes \(E\).

To prove the first assertion, the top coefficient in (22) is
\((1-\tau)\tau^N C_N\ne0\). Its degree \(N+1>1\) prevents any
cancellation with the first two terms.
If \(N=0\), evaluating (21) at \(\lambda=0\) gives \(C=E\), since
\(\phi\) is normalized. Conversely a centralizer has \(C=E\).
Equation (22) then has degree at most one, and the inherited
zero-degree exclusion, or the explicit normal form below, makes
it exactly one. This proves every quantifier in the criterion;
it is not a conclusion from finitely many intermediate samples.

## 6. The complete normalized centralizer and the resulting boundary

The normalized \(\mathbb C[x,\lambda]\)-automorphisms centralizing
\(E=4xb\partial_c\) are exactly
\[
\phi(b)=b,\qquad \phi(c)=c+K(x,\lambda,b),\qquad
K|_{\lambda=0}=0.
\tag{23}
\]
Indeed they preserve \(\ker E=\mathbb C[x,\lambda,b]\).
An automorphism of this one-variable polynomial ring over
\(\mathbb C[x,\lambda]\) sends \(b\) to \(ub+v_0\), with
\(u\in\mathbb C^*\). Its extension sends \(c\) to
\(ac+K\), again with \(a\in\mathbb C^*\).
Commutation, applied to \(c\), gives
\[
4xb\,a=4x(ub+v_0).
\]
Thus \(v_0=0\), \(a=u\), and normalization gives \(a=u=1\).
The converse in (23) is immediate.

For (23), direct conjugation gives
\[
\phi^{-1}P_\lambda\phi
=x^2\partial_b+
       (2b+4\lambda xb+x^2K_b)\partial_c.
\tag{24}
\]
The retained degree-one premise (20) is equivalent to
\[
K=\lambda A(x,b)+C_0(x,\lambda),\qquad C_0(x,0)=0.
\tag{25}
\]
The decomposition need not be unique in its terms independent of
\(b\), which is harmless. Its top is
\[
(4xb+x^2A_b)\partial_c.
\tag{26}
\]
It is nonzero because \(4xb\) is not divisible by \(x^2\) as a
polynomial coefficient of \(b\). Its primitive part is
\(\partial_c\), so it has a slice.

Combining Sections 5--6, the standard scaling homotopy cannot take
a supplied nonsliced primitive degree-one top toward the good
gauge while staying at degree one: every intermediate scalar
other than the two endpoints has higher degree.
This is a precise obstruction to that universally available path.
It does not obstruct the different path constructed in Section 2.

## 7. Exact barrier height for the pass-33 family

For the family (2), take
\[
\phi=\theta_{\rm good}\theta_p^{-1}.
\tag{27}
\]
It is an actual normalized gauge satisfying (20), because
\[
\phi^{-1}P_\lambda\phi=\theta_p\Delta\theta_p^{-1}.
\]
Since \(\theta_{\rm good}^{-1}(b)=w\), one has
\[
\phi^{-1}(b)=W_p.
\tag{28}
\]

All these normalized relative automorphisms have Jacobian
determinant one: their actual polynomial inverses make the
determinant a constant unit, and the normalization fixes it.
Conjugation of a Jacobian derivation therefore gives
\[
C(\lambda)=\phi^{-1}E\phi
 =J_{-2xW_p^2},
\tag{29}
\]
using \(E=J_{-2xb^2}\).
The leading \(\lambda\)-coefficient of \(W_p\) is
\(-4x^4pF_p^4\). Thus (29) has exact degree four, with
\[
C_4=J_{-32x^9p^2F_p^8}
    =-256x^9p^2F_p^7L_p\ne0.
\tag{30}
\]
Equations (22) and (30) prove
\[
q\bigl(\phi_\tau\partial_\lambda\phi_\tau^{-1}\bigr)
 =5\quad(\tau\ne0,1),
\tag{31}
\]
whereas both endpoints have degree one.
This also holds at \(p=1\): a supplied good top does not imply
that an arbitrary normalized gauge centralizes \(E\).

The explicit degree-five barrier is entirely bypassed by the
degree-one \(p_t\) path in Section 2. No degree minimization or
finite parameter search was used to find its endpoint.

## 8. Scope of the repair result

The positive operation is constructive for a supplied member of
the explicit family: read its polynomial \(p\), apply the two
known polynomial maps in (7), and the endpoint has a genuine
primitive slice. Its coordinate inverses and the nonzero degree-one
condition hold uniformly in the path parameter.

The exact general statement is instead the scaling-path criterion
(21)--(26), which applies to every supplied normalized gauge
satisfying (20). It does not classify all degree-one gauges, and
it does not identify an arbitrary such gauge with (27).
The marked normalizer obstruction is also exact, but allowing
all gauges removes that conjugacy invariant, as the positive
bridge itself demonstrates.

An endpoint gauge to a known good frame can always be written in
this already polynomial canonical model using its supplied slice
coordinates. That observation was already proved in pass 30.
What is not supplied by it is a degree-one path for every input,
a single four-variable additive flow, or a corresponding
construction when the invariant quotient is not known to have
this relative-plane presentation. Those are not asserted here.

All groupoid, conjugation, centralizer, and degree arguments above
are direct polynomial proofs. The prior replica and local-slice
mechanisms retain their attribution in the linked notes. No
novelty, expert-review, or formal proof-assistant claim is made.

The standalone [finite checker](plinth_repair_checks_pass34.py)
passed all six methods in 10.995 seconds. An earlier fully expanded
run also passed; keeping the auxiliary variable \(h=x^2c-b^2\)
independent in high-degree identities reduced redundant expansion.
No mathematical formula or assertion was changed. The finite tests
check the new parameter identities, non-additive first jet, exact
degree-five coefficient, and endpoint slice, not the universal
centralizer classification or existence of a repair outside this
explicit family.
