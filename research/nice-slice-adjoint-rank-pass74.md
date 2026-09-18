# Nice sliced actions have Jacobian cube zero

For a nice locally nilpotent derivation on the actual complex
polynomial four-ring, an original polynomial slice forces the
Jacobian of its velocity to have cube zero and rank at most two.
The proof uses the already proved highest-vertical-adjoint exclusion.
It does not assume a generic rank or a supplied two-quadratic frame.

This closes the spatially quadratic nice-slice subfamily using
a published triangularization theorem. For arbitrary coefficient
degree it leaves a genuine coordinate-selection boundary. A known
nice sliced action has exactly one constant good direction, so
the new rank cap does not automatically yield the recognized
two-good-direction frame by a constant linear coordinate change.

## 1. Actual inverse flow and every partial adjoint

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\quad
E=\sum_iP_i\partial_{x_i}\in\operatorname{LND}(B),\quad
E(s_*)=1,\quad E^2x_i=0.
\tag{1}
\]
Write \(P=(P_i)^t\), \(J=(\partial_jP_i)\), and
\(T_i=\partial_{x_i}\). Niceness says \(EP=JP=0\), so
the actual flow and inverse are
\[
\Phi_t(x)=x+tP(x),\qquad \Phi_{-t}(x)=x-tP(x).
\tag{2}
\]
The determinant of the Jacobian of this automorphism of
\(B[t]\) is a unit, hence a complex constant; its value at
\(t=0\) is one. Thus \(\det(I+tJ)=1\), and Cayley-Hamilton
over \(B\) gives \(J^4=0\). Differentiating \(JP=0\)
componentwise gives
\[
E(J)=-J^2.
\tag{3}
\]
The sign in (3) differs from the positive Riccati identity in
the [double-commutator theorem](height-eight-algebra-pass.md).
The two hypotheses must not be identified.

For a coefficient column \(v\), the bracket \([E,v\cdot\partial]\)
has coefficient column \(Ev-Jv\). Equation (3) implies
\(E(J^r)=-rJ^{r+1}\); induction therefore gives
\[
(\operatorname{ad}_E^rT_i)(x)
=(-1)^r r!J^re_i\quad(0\le r\le4).
\tag{4}
\]
In particular every fourth adjoint is zero. Equivalently, the
matrix of the actual conjugated partial columns is
\[
\exp(tE)(T_1,\ldots,T_4)\exp(-tE)
\ \longleftrightarrow\
(I+tJ)^{-1}=I-tJ+t^2J^2-t^3J^3.
\tag{5}
\]
For a direct chain-rule check, differentiating
\(P(\Phi_t(x))=P(x)\) gives
\(J(\Phi_t)(I+tJ)=J\). The conjugated columns are
\(I-tJ(\Phi_t)\), which is precisely (5).
No rationally changed coordinate partial is substituted for
an actual \(T_i\) in this argument.

## 2. The slice excludes the sole four-block

We use the [highest vertical exclusion](vertical-top-exclusion-pass69.md):
if \(E,T\) are actual LNDs of a characteristic-zero domain,
\(E\) has a slice, and for \(n\ge1\)
\[
\operatorname{ad}_E^{n+1}T=0,\qquad
\operatorname{ad}_E^nT=hE\quad
(h\in\operatorname{Frac}B),
\]
then the highest adjoint is zero. Here is the essential proof
gate, independently reconstructed from the complete saved note.
The original slice gives \(B=A[s_*]\), \(A=\ker E\).
Evaluating the highest adjoint on \(s_*\) makes \(h\) an
actual element of \(A\). The action of \(T\) on \(A\) has
slice degree at most \(n-1\), while \(T(s_*)\) has degree
at most \(n\). For the Laurent automorphism
\(\Psi(s_*)=s_*/z\), the actual LND
\(z^{n-1}\Psi T\Psi^{-1}\) preserves \(A[s_*,z]\).
Its quotient at \(z=0\) is an LND taking \(s_*\) to
\(b_ns_*^n\), where \(n!b_n=h\). Self-divisibility of a
nonzero element's derivative under an LND forces that derivative
to vanish. Hence \(b_n=h=0\), including when \(n=1\).
Restriction and quotient follow an actual Laurent-ring LND;
no unsupported pointwise specialization or polynomial-kernel
classification is used.

Now take ranks over \(K=\operatorname{Frac}B\). Since the
slice makes \(E\ne0\), \(P\ne0\). If \(J^3\ne0\),
the nilpotent four-by-four matrix has the unique partition
\((4)\). Consequently
\[
\dim_K\ker J=1,\qquad \ker J=KP,
\qquad \operatorname{im}J^3\subseteq KP.
\tag{6}
\]
Some column of \(J^3\) is nonzero. Equation (4) makes the
corresponding highest third adjoint a nonzero rational multiple
of \(E\), while its fourth adjoint vanishes. Apply the vertical
exclusion to that original coordinate partial. This contradicts
its nonzero third adjoint. We obtain
\[
\boxed{J^3=0,\qquad\operatorname{rank}_KJ\le2.}
\tag{7}
\]
The rank conclusion follows by listing the remaining nilpotent
partitions of four: \((3,1),(2,2),(2,1,1),(1,1,1,1)\).
Equation (7) holds in every actual frame in which (1) is nice;
it is not an assertion that every sliced action has a nice frame.

The same argument works on \(k^{[n]}\) over any characteristic-zero
field, for \(n\ge2\). The actual inverse flow first gives \(J^n=0\).
If \(J^{n-1}\ne0\), its unique Jordan block has size \(n\),
and a highest \((n-1)\)-st adjoint of an actual partial is nonzero
and parallel to \(E\). Thus \(J^{n-1}=0\) and
\(\operatorname{rank}J\le n-2\). The dimension-one sliced
case has constant nonzero velocity and \(J=0\); the displayed
\(n-2\) bound is not applied to it. This observation is a
deduction from the same proof, not a historical novelty claim.

If \(J^2=0\), equation (4) gives the existing all-double-adjoint
recognition theorem. Otherwise the partition is \((3,1)\), so
\(\operatorname{rank}J=2\) and \(\operatorname{rank}J^2=1\).
The latter line is independent of \(E\): if it were parallel
to \(E\), a nonzero second-adjoint column would contradict the
same vertical exclusion with \(n=2\).

## 3. A source-backed quadratic-coefficient consequence

Assume additionally that \(\max_i\deg P_i\le2\), where
degree here is ordinary spatial degree, not adjoint height.
For the degree-two case, de Bondt's Theorem 3.2 states that a
quadratic polynomial map with nilpotent Jacobian of rank at most
two has Jacobian similar, by a constant matrix, to a triangular
matrix.[^rank] The affine case follows directly from constant
nilpotent-matrix triangularization. Equation (7) verifies the
rank hypothesis without a new generic assumption.

Under the actual linear change \(x=Cy\), the new velocity is
\(C^{-1}P(Cy)\); its Jacobian is
\(C^{-1}J(Cy)C\). It is strictly triangular, because its
diagonal is nilpotent in a domain. An extreme component of this
new velocity is therefore a complex constant. If nonzero, the
corresponding normalized linear variable is an actual coordinate
slice, and the original kernel is the polynomial coordinate
hyperplane ring. If zero, the corresponding linear variable is
an invariant ambient coordinate. The existing
[slice/invariant-coordinate recognition gate](nice-route.md#three-different-ranks-and-the-first-decisive-closure)
then gives the same conclusion. In that branch one can use the
retained Dedekind-base three-variable slice theorem over
\(\mathbb C[y_1]\); no localized slice replaces \(s_*\).
Thus
\[
\deg P\le2,\quad E^2x=0,\quad E(s_*)=1
\quad\Longrightarrow\quad\ker E\simeq\mathbb C^{[3]}.
\tag{8}
\]
The old [nice-route inventory](nice-route.md) already used the
rank-at-most-two source theorem and left its rank-three candidate
unremoved. The new input here is the sliced rank cap (7), not a
new triangularization theorem. The separate
[quadratic source-scope note](quadratic-nice-source-scope-pass74.md)
provides another published route to the same subfamily and records
its own source-access limitations. Neither route supplies arbitrary
nonhomogeneous nice-action recognition.

## 4. Rank one of the top is not two constant good directions

Define the constant vector space
\[
G_2=\{v\in\mathbb C^4:J^2v=0\}.
\tag{9}
\]
If \(\dim_{\mathbb C}G_2\ge2\), choose two independent
constant directions in it and complete them to an actual linear
coordinate frame. Equations (4) and (7) give the supplied
two-quadratic profile, so [pass73 recognition](height-ten-closure-pass73.md)
applies. A one-dimensional image of \(J^2\) over \(K\)
does not imply that its kernel contains two complex constant
directions.

This failure already occurs in the previously retained de Bondt
control, not a newly constructed action:[^example]
\[
a=xz-y^2+w,\qquad
P=(1,a,a^2,-a^2x+2ay-z)^t.
\tag{10}
\]
It satisfies \(JP=0\) and \(Ex=1\). Its exact square has
\[
(J^2)_{2,*}=(-a^2,2a,-1,0),\qquad J^2e_w=0.
\tag{11}
\]
For a constant column \(v=(v_1,v_2,v_3,v_4)^t\), the second
row of \(J^2v=0\) forces
\(-v_1a^2+2v_2a-v_3=0\). The polynomial \(a\) is
transcendental over \(\mathbb C\), so the first three constants
are zero. Equation (11) gives the exact result
\[
G_2=\mathbb Ce_w.
\tag{12}
\]
The first three square columns are nonzero, the last Jacobian
column is nonzero, and the cube is zero. Hence its actual displayed
adjoint profile is \((2,2,2,1)\), with height eleven. No constant
linear coordinate change makes two directions good. This does
not claim a lower bound on its minimum over polynomial frames.

Indeed, the actual coordinates
\[
(x,a,Y,Z)=(x,a,y-xa,z-xa^2)
\tag{13}
\]
have inverse
\(y=Y+xa\), \(z=Z+xa^2\),
\(w=a-xZ+Y^2+2xaY\), and transform \(E\) into
\(\partial_x\). Thus this action is already recognized.
It is a countercontrol only to automatic constant-linear
good-direction selection, not to nonlinear recognition or
cancellation.

## 5. An actual nonslice four-block and the localization boundary

The slice hypothesis in (7) is essential. The following exact
control was supplied and checked by Root in this pass, without
a historical novelty claim. In the actual coordinates \((x,y,z,w)\),
put
\[
q=y-xz,\qquad g=w-xq,\qquad
E_0=\partial_x+z\partial_y+q\partial_w,\qquad E=gE_0.
\tag{14}
\]
Here \(E_0^2(x,y,z,w)=0\), \(E_0x=1\), and \(E_0g=0\).
Thus \(E\) is an actual nice LND, an invariant replica of
\(E_0\). Every coefficient is divisible by the nonconstant
\(g\), and the origin is a fixed point, so \(E\) has no
polynomial slice. For its velocity column \(P=g(1,z,0,q)^t\),
direct differentiation gives
\[
\operatorname{rank}J=3,\quad\operatorname{rank}J^2=2,\quad
J^3=gP e_z^t\ne0,\quad J^4=0,
\qquad \operatorname{ad}_E^3\partial_z=-6gE\ne0.
\tag{15}
\]
This realizes the exact four-block excluded in Section2, including
its vertical highest adjoint, once the original slice is dropped.

On \(B_g\) there is nevertheless a slice: \(E(x/g)=1\).
This does not allow the vertical exclusion to be applied to
\(T=\partial_z\) there. Although \(T\) is an LND on \(B\),
it is not an LND on \(B_g\), since \(Tg=x^2\ne0\)
and every LND on a characteristic-zero domain kills every unit.
An invariant localization of \(E\) therefore need not preserve
the other derivation's local nilpotence. This is an actual
localization countercontrol, not merely a rational coefficient
table or a claimed counterexample to recognition.

## 6. Exact controls, audits, and remaining scope

The [standalone checker](nice_slice_adjoint_checks_pass74.py)
has three methods and imports only `unittest` and SymPy.
The first uses (10) and the simpler actual nice sliced action
\(P=(1,z,0,y-xz)^t\). It independently computes the polynomial
flows, both inverse orders, the group law, Jacobians, all four
partial adjoints through order four, and the exact profiles
\((2,2,2,1)\) and \((1,1,2,0)\), respectively.
Another method keeps the five formal nilpotent Jordan representatives
separate from actual Jacobians, checks the exact constant-kernel
calculation (11)--(12), and verifies both coordinate inverse
orders in (13). The formal four-block is not asserted to arise
from a nice sliced action.

The added nonslice method verifies both actual flow inverse orders,
the invariant replica identity, fixed-point and nonconstant-factor
conditions, all ranks and the highest adjoint in (15), and the
localized slice and moving-unit identities. The written evaluation
and unit arguments, not finitely many probes, establish the absence
of a global slice and failure of localized local nilpotence.

The original two-method version passed in **1.126 seconds**,
exit zero. After the nonslice method was added, its first three-method
run passed in **1.594 seconds**. The final version, including the
localized-slice identities, passed **three methods in 1.577 seconds**,
exit zero. These are successive versions/runs, not eight distinct
methods. These are finite identity controls, not a computational
proof of vertical exclusion, a classification theorem, or all
nice actions. The complete vertical69 written proof was freshly
read and independently reconstructed through EOF in this task.
The source in the footnote was checked separately. Independent
reviews of this new note and checker are not inferred from an
outline review or author self-review.

For higher spatial degree, the remaining boundary here is the
nice type \((3,1)\) case with no supplied recognition coordinate
or sufficient constant good directions. No universal adapted
degree bound, full-frame reduction, new historical classification,
formal verification, or general cancellation result is asserted.
No frozen pass73-or-earlier artifact or shared metadata was changed,
and no new full regression was run for these controls.

[^rank]: Michiel de Bondt, [*Quadratic polynomial maps with Jacobian rank two*](https://arxiv.org/html/1601.00579v4), Theorem 3.2, with its complete displayed proof; [PDF](https://arxiv.org/pdf/1601.00579v4), printed pp.14--16. The theorem and its complete displayed proof were freshly read, but not every earlier lemma cited by that proof. It does not require homogeneity. This is a selected primary-source verification, not a fresh whole-paper proof audit.

[^example]: The complete actual control and its source attribution are already in [literature-scope-pass39.md](literature-scope-pass39.md), Section2, and [nice-route.md](nice-route.md). It is the fixed-fifth-coordinate specialization of de Bondt's Example1.3(b). The added use here is the exact constant-good subspace (12); no new example or novelty claim is made.
