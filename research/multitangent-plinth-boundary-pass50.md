# The multi-tangent trace bound and its triple-point boundary

The normalized-cover trace argument gives a stronger ideal-membership
condition at a plinth point with at least two distinct tangent directions:
\(p\in\mathfrak m^2J\). It does not exclude higher ordinary multiple
points. An explicit cubic conic satisfies the extracted trace and
quadratic-cover conditions at an ordinary triple point, while failing
the flatness and prime-pullback hypotheses of the actual cylinder.

This separates a proved necessary condition on the actual quotient
from a weaker control showing the limit of the trace argument alone.

## 1. Actual hypothesis and branchwise trace input

Use the exact local setup of
[the nodal exclusion](nodal-plinth-obstruction-pass49.md), at a closed
second-image obstruction point \(q\). Write
\[
R=C_{\mathfrak m_q},\quad\mathfrak n=\mathfrak m_qR,
\quad\mathcal A=A\otimes_C R,
\quad A[s_*]\simeq\mathbb C^{[4]}.
\tag{1}
\]
The actual degree-two frame has supplied every quadratic residue field.
The local bundle and conic equations are
\[
F_2=R\oplus Rz\oplus Rw,
\quad r=az+bw,\quad JR=(a,b),\quad\gcd(a,b)=1,
\tag{2}
\]
\[
Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,
\quad Dr=p=aB_1+bB_2,
\tag{3}
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0,
\quad\epsilon\in R^*,
\quad a,b,B_1,B_2,Q\in\mathfrak n.
\tag{4}
\]
Neither \(J=\mathfrak n\) nor \(B_1,B_2\in J\) is assumed.

The [normalized-cover theorem](normalized-cover-surjectivity-pass49.md)
and the actual primitive-element gate give the following exact input.
At a point \(\xi\) of the normalization of a plinth component above
\(q\), if \(b\) is not identically zero on that component, then
\[
\operatorname{ord}_\xi(B_1)
\geq\operatorname{ord}_\xi(b)+1.
\tag{5}
\]
If \(b\) is identically zero there, coprimality and (3) make
\(B_1\) identically zero. The companion assertion interchanges
\(a,B_2\) with \(b,B_1\).

For clarity, (5) came from the exact quadratic minimal polynomial
of the actual residue of \(r\), not an arbitrary conic relation.
Since \(r\) vanishes on the full fiber and every normalized cover
point is reached, it is regular and zero at all those points.
Its trace lies in the maximal ideal of the normalized base DVR.
The trace equals \(-2B_1/(\epsilon b)\), or
\(2B_2/(\epsilon a)\) in the companion formula. These are the
complete hypotheses behind (5).

## 2. Distinct tangent directions force \(p\in\mathfrak n^2J\)

Let a normalized branch have multiplicity \(e_\xi\) at \(q\).
In regular parameters \(u,v\) of the plane and a uniformizer \(t\)
on that branch, its leading parametrization is
\[
(u,v)=t^{e_\xi}(\alpha,\beta)+
\text{terms of higher order},\qquad (\alpha,\beta)\ne(0,0).
\tag{6}
\]
The vector \((\alpha,\beta)\) spans its tangent direction. Every
function in \(\mathfrak n\) has order at least \(e_\xi\) on
the branch, unless it vanishes identically there.

Apply (5). It gives order at least \(e_\xi+1\) for \(B_1\),
or identically zero. If its linear part were nonzero on the tangent
vector in (6), its order would instead be exactly \(e_\xi\):
terms from \(\mathfrak n^2\) have order at least \(2e_\xi\).
Thus its linear part annihilates that tangent direction. The same
holds for \(B_2\). This reasoning permits a singular individual
branch; it does not require each branch to be smooth.

If the reduced plinth support has at least two distinct tangent
directions at \(q\), both linear parts vanish. Hence
\[
\boxed{\quad B_1,B_2\in\mathfrak n^2,
\qquad p\in\mathfrak n^2JR.\quad}
\tag{7}
\]
This strengthens the earlier \(p\in\mathfrak nJR\). Define the
order of a nonzero ideal by the least order of one of its nonzero
members. If \(m=\operatorname{ord}_{\mathfrak n}(p)\), then
\[
\operatorname{ord}_{\mathfrak n}(J)\leq m-2.
\tag{8}
\]
At an ordinary node \(m=2\), (8) contradicts the properness of
\(J\), recovering pass 49. At an ordinary triple point it only
forces \(J\) to contain an element with nonzero linear part.
It does not force \(J=R\) or \(J=\mathfrak n\).

## 3. An exact ordinary-triple conic control

The following ring is deliberately a weaker model. Put
\[
R_0=\mathbb C[a,b],\qquad p=b^3-a^3,
\qquad r=az+bw,
\tag{9}
\]
\[
B_1=-a^2,\quad B_2=b^2,\quad \epsilon=1,
\quad Q=-ab+a^3,
\]
and define
\[
H=R_0[z,w]/
\bigl(r^2-2b^2z-2a^2w+ab-a^3\bigr).
\tag{10}
\]
The full polynomial \(p\) is reduced and has three distinct
linear components through the origin. Its origin is an ordinary
triple point. The coefficient data satisfy (3)–(4), including
\(B_1,B_2\in(a,b)^2\) and \(p\in(a,b)^3\).

The ring \(H\) is a domain. Over \(\mathbb C(a,b)\), the two
linear functions \(r=az+bw\) and
\(j=-b^2z-a^2w\) have determinant \(p\ne0\), and the relation
is \(r^2+2j-Q\). It is irreducible there. In \(R_0[z,w]\)
the relation is primitive, since its coefficients on \(z^2,w^2\)
are the coprime elements \(a^2,b^2\). Gauss's lemma therefore
makes it prime globally.

There is a genuine LND on this ring:
\[
Da=Db=0,\qquad Dz=br-a^2,\qquad Dw=-ar+b^2.
\tag{11}
\]
Indeed \(Dr=p\), \(Dj=-pr\), so the defining relation is
preserved; moreover
\[
D^2z=bp,\qquad D^2w=-ap,\qquad D^3z=D^3w=0.
\tag{12}
\]
Leibniz expansion proves local nilpotence on every polynomial.
No polynomial-cylinder presentation or full plinth computation
for this weaker ring is claimed.

## 4. All three dominating quadratic covers satisfy the trace conditions

Fix \(\zeta\in\mathbb C\) with \(\zeta^3=1\), and take the
base component \(a=t,b=\zeta t\). Its generic conic equation is
\[
(r-\zeta^2t)^2=t^3.
\tag{13}
\]
This is irreducible over \(\mathbb C(t)\), since \(t\) is not
a rational square. Its finite birational normalization is
\[
t=s^2,\qquad r=\zeta^2s^2+s^3.
\tag{14}
\]
Finiteness follows from \(s^2=t\), and birationality from
\(s=(r-\zeta^2t)/t\) in the fraction field. Thus the actual
generic field of the dominating component is \(\mathbb C(s)\),
quadratic over \(\mathbb C(t)\). The normalized cover is
\(\mathbb A^1_s\to\mathbb A^1_t\), \(t=s^2\), with one
finite branch value. The residue of \(r\) at its sole point
over zero is zero, and
\[
\operatorname{Tr}(r)=2\zeta^2t.
\tag{15}
\]
Its trace vanishes to positive order, exactly as required by (5).

The dominating exceptional surface is explicit too. Dividing out
the vertical factor from the component pullback gives
\[
(z+\zeta w-\zeta^2)^2-t=0.
\tag{16}
\]
It is the polynomial plane \(\mathbb C[s,z]\), with
\(s=z+\zeta w-\zeta^2\). Its map to \(\mathbb A^1_s\)
is surjective. The induced derivation is
\(\zeta s^5\partial_z\), so the invariant ring of this
dominating surface is exactly \(\mathbb C[s]\). This verifies
the normalized-cover and no-missed-point features in this model,
rather than only writing down a possible field extension.

## 5. Why the model does not contradict an actual-cylinder theorem

The full component pullback in \(H\), before deleting anything,
is
\[
H/(b-\zeta a)H
\simeq\mathbb C[t,z,w]/
\bigl(t^2((z+\zeta w-\zeta^2)^2-t)\bigr).
\tag{17}
\]
It contains an extra vertical plane with multiplicity two. It is
not the prime reduced exceptional surface required in the actual
factorial quotient. Passing to the dominating component in (16)
must not be confused with this full pullback.

Likewise \(H/(a,b)H=\mathbb C[z,w]\), a plane rather than a
curve. Flatness actually fails, not merely remains unproved:
\[
H/bH\simeq\mathbb C[a,z,w]/\bigl(a^2(z^2-2w-a)\bigr).
\tag{18}
\]
The nonzero class of \(a(z^2-2w-a)\) is killed by \(a\),
so the base regular sequence \(b,a\) does not remain regular.
The total hypersurface is singular at every point of its vertical
plane, as all four derivatives of (10) vanish at \(a=b=0\).
These facts prevent it from being a smooth faithfully-flat
intrinsic factor of a polynomial cylinder.

The exact conclusion of the control is limited: conic identities,
quadratic dominating field extensions, one-branch normalized
monodromy, reached points and trace vanishing are jointly compatible
with an ordinary triple point. Those extracted conditions alone
cannot reproduce the ordinary-node contradiction in higher
multiplicity. A further argument using the actual flat algebra,
its prime exceptional pullbacks, higher corrections or the supplied
coordinate frame is still needed. No counterexample to cancellation
or to the full actual hypotheses is produced here.

The actual theorem (7) and the weaker control have separate roles.
All pass-49 files remain unchanged, and no journal, historical
novelty or formal-verification claim is made.

## Finite controls

The standalone [three-method checker](multitangent_plinth_boundary_checks_pass50.py)
checks the genuine polynomial flow on the weaker ring, all three
branch normalizations and traces using the exact relation
\(\zeta^3=1\), and the failed flatness, prime-pullback and
smoothness premises. The first complete run passed three methods
in 0.071 seconds, exit zero, with no failed assertions. Only
`unittest` and SymPy are imported. These finite identities do not
verify the actual-cylinder tangent theorem or the universal
topological input, and the example is not labeled an actual
unresolved-frame realization.
