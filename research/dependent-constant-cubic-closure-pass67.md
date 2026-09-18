# Recognition of the dependent constant-top cubic sector

The residual dependent constant-top cubic case from pass66 is
recognized. The full velocity equations supply a rational correction
supported on two genuine constant coordinate directions. Commutation
with the original action forces the correction to fix both its
coefficient and its denominator. It is therefore an actual localized
nice LND, and the existing one-good-output recognition lemma applies.

This closes the dependent-defect, constant-top, flow-degree-three
sector under the supplied adjoint frame. It neither asserts that
this sector is empty nor proves a frame-existence theorem for arbitrary
sliced actions.

## 1. Exact actual hypotheses and the frozen reduction

Let
\[
B=k[x_1,x_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad E(s_*)=1,\qquad A=\ker E.
\]
All four displayed generators are actual polynomial coordinates.
With their partials \(T_1,T_2,T_3,T_4\), assume
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2),\qquad
\operatorname{ad}_E^3T_j=0\quad(j=3,4).
\tag{1}
\]
Retain dependent defects with no nonzero complex constant relation:
\[
V_3=aD,\qquad V_4=bD,\qquad
0\ne D\in\operatorname{LND}_k(B),\qquad [E,D]=0,
\]
\[
a,b\in\ker E\cap\ker D,\qquad a,b\ne0,
\qquad E^3x=c\in k^4\setminus\{0\},\qquad E^4x=0.
\tag{2}
\]
Here \(D\) is the actual primitive defect derivation of pass42.
The proof below uses its established actualness and commutation,
not a slice on \(D\).

Write \(P=Ex\), \(J=\operatorname{Jac}P\), \(d=D(x)\),
\(\ell=(0,0,a,b)\), and \(h_2=E^2x\).
The complete
[dependent cubic reduction](dependent-constant-cubic-pass66.md)
gives
\[
c_3=c_4=0,\qquad
h_2=c\sigma+e,\qquad c,e\in k^4,\qquad
\sigma\in B,\qquad E\sigma=1.
\tag{3}
\]
In particular \(T_c=\sum c_iT_i\) is a nonzero actual constant
good partial. Put \(e_B=(e_3,e_4)\). The same reduction gives
\[
EX=e_3\sigma+F,\qquad EY=e_4\sigma+G,\qquad
EF=EG=0,\qquad a\,dF+b\,dG=0.
\tag{4}
\]
The differentials in (4) are ordinary ambient differentials.

For a nonconstant residual pair, the polynomial-curve theorem used
and audited in pass66 supplies an actual polynomial \(u\in B\)
and univariate polynomials \(p,q\in k[U]\) such that
\[
F=p(u),\qquad G=q(u),\qquad Eu=Du=0,\qquad
a p'(u)+b q'(u)=0.
\tag{5}
\]
Both derivatives are nonzero, and their ratio is nonconstant.
Neither \(\sigma\) nor \(u\) is assumed to be an ambient coordinate.

The remaining input needed from the full matrix and velocity
equations is
\[
\rho:=ae_3+be_4,\qquad
Jc=\rho d,\qquad
Jh_2-\frac{\ell P}{2}d=\frac c2.
\tag{6}
\]
These equations retain the full auxiliary row. In particular,
they are stronger than a rank-one statement about
\(\operatorname{Jac}h_2\) alone.

## 2. Previously recognized endpoints

If \(e_B=0\), then \(\rho=0\), so (6) gives
\([E,T_c]=-Jc=0\).
A complementary constant good direction remains available.
The already proved
[one-good-output recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
applies with this commuting constant partial and denominator one.
Thus \(A\simeq k^{[3]}\).

Suppose \(e_B\ne0\) and \(F,G\) are both constant.
Then
\[
L=e_4X-e_3Y
\]
is a nonzero actual linear coordinate, with constant derivative
\(EL=e_4F-e_3G\).
If this derivative is nonzero, a scalar multiple of \(L\) is an
ambient coordinate slice and the slice theorem gives
\(A\simeq B/(L)\simeq k^{[3]}\).
If it is zero, \(L\) is an actual invariant coordinate. The established
invariant-coordinate regular-kernel endpoint applies:
\(A\) is regular because \(B=A[s_*]\) is regular.
This is the endpoint already retained in pass66.

It remains to handle
\[
e_B\ne0,\qquad (F,G)\ \text{nonconstant}.
\tag{7}
\]
Since \(a,b\) have no complex constant relation, (7) implies
\(\rho\ne0\).

## 3. The correction has a one-variable invariant denominator

In the remainder of the proof use (5), and put
\[
s_0=ap(u)+bq(u),\qquad
\Delta(U)=e_3q'(U)-e_4p'(U),\qquad
N_0(U)=p(U)q'(U)-q(U)p'(U).
\tag{8}
\]
The relation in (5) gives the exact identities
\[
\rho q'=a\Delta,\qquad
\rho p'=-b\Delta,\qquad
s_0\Delta=\rho N_0,
\tag{9}
\]
where every univariate polynomial is evaluated at \(u\).
For the last identity, the difference is
\((e_3q-e_4p)(ap'+bq')\).

Because \(a,\rho,q'\) are nonzero, (9) forces
\(\Delta(u)\ne0\). Thus the rational function
\[
\lambda(U)=\frac{N_0(U)}{\Delta(U)}
\]
is defined and
\[
\frac{s_0}{\rho}=\lambda(u),\qquad
\beta=\frac{\sigma-\lambda(u)}2\in B_{\Delta(u)},\qquad
E\beta=\frac12.
\tag{10}
\]
Set \(g_0=\Delta(u)\).
It is an actual nonzero polynomial and \(Eg_0=0\).

No coprimality of \(p'\) and \(q'\) is assumed. No common factor
of \(\Delta\), no multiplicity in \(g_0\), and no factor of
\(\rho\) is silently discarded. The equality in (10) is first
proved in \(\operatorname{Frac}B\); its displayed formula then
places \(\beta\) in the indicated invariant localization.
The denominator \(\rho\), which may have unrelated factors,
is not inverted.

## 4. A rational two-direction correction commutes with the original action

Let \(T_e=\sum e_iT_i\), and write \(W_c=[E,T_c]\),
\(W_e=[E,T_e]\). Since \(\ell P=\rho\sigma+s_0\), substituting
(3) into (6) gives
\[
Je=\frac c2+\frac{s_0-\rho\sigma}{2}\,d.
\]
Consequently
\[
W_c=-\rho D,\qquad
W_e=-\frac12T_c+\beta\rho D.
\tag{11}
\]
The signs in (11) use \([E,T_v](x)=-Jv\) for a genuine constant
direction \(v\).

Define the actual derivation of \(B_{g_0}\)
\[
S=T_e+\beta T_c.
\tag{12}
\]
The original derivation \(E\) extends as an LND to this localization,
since \(Eg_0=0\). Equations (10)--(11) give
\[
[E,S]=W_e+(E\beta)T_c+\beta W_c=0,\qquad
Sx=e+\beta c.
\tag{13}
\]
At this stage (12) is only a derivation. Local nilpotence has
not been inferred from the rational correction or commutation.

For comparison, the middle-field correction
\(W_e+T_c/2=\beta\rho D\) is a replica of the existing defect.
It supplies no new generic direction. The useful field in this
proof is instead (12), which retains the two actual constant
directions.

## 5. Commutation forces niceness and preserves the denominator

Commutation in (13) can be applied to the original acceleration
vector. Since \(E^2\beta=0\),
\[
S(h_2)=E^2(Sx)=E^2(e+\beta c)=0.
\]
On the other hand (3) gives \(S(h_2)=c\,S\sigma\).
As \(c\ne0\), this proves
\[
S\sigma=0.
\tag{14}
\]

The bad components of \(c\) vanish. Therefore
\(S(X,Y)=e_B\), a complex constant pair. Applying commutation
once gives
\[
S(EX,EY)=E(SX,SY)=0.
\]
Use (4)--(5) and (14):
\[
(p'(u),q'(u))\,Su=0.
\]
At least one derivative is nonzero, so cancellation in the domain
gives
\[
Su=0,\qquad S\beta=0,\qquad Sg_0=0.
\tag{15}
\]
In particular
\[
S^2x_i=0\quad(1\le i\le4).
\tag{16}
\]

These identities establish actual local nilpotence on \(B_{g_0}\).
The derivation kills \(g_0^{-1}\), and every original polynomial
generator has \(S\)-degree at most one. The Leibniz rule gives a
finite nilpotence bound for each element of the localized ring.
Thus
\[
S\in\operatorname{LND}_k(B_{g_0}),\qquad
[E,S]=0,\qquad g_0 S(B)\subset B.
\tag{17}
\]
The last assertion follows directly from
\(g_0\beta=(g_0\sigma-N_0(u))/2\).
The proof did not assume that a commuting rational field is an LND.

## 6. The actual one-good-output recognition gate is met

The two constant vectors \(c,e\) are independent: \(c\) is nonzero
and has zero bad components, whereas \(e_B\ne0\).
Complete them to a complex constant basis of the ambient vector
space. The dual constant linear coordinate change gives actual
polynomial coordinates \((z_1,z_2,A_0,B_0)\) with
\[
T_c=\partial_{A_0},\qquad T_e=\partial_{B_0}.
\]
In these coordinates
\[
S=\partial_{B_0}+\beta\,\partial_{A_0},\qquad
S^2A_0=0.
\tag{18}
\]
All other coordinate functions in this display are fixed by \(S\).

Only the actual partial \(\partial_{A_0}=T_c\) must remain good.
It does: \(c\) was supported in the original good plane, so
\(\operatorname{ad}_E^2T_c=0\) follows from (1).
There is no assertion that every old adjoint bound is preserved
by this larger constant frame change.

Equations (17)--(18), the original slice \(E(s_*)=1\), and this
single good partial are exactly the hypotheses of the
[one-good-output recognition lemma, pass41 Section 1](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial).
That proved lemma recognizes the original kernel:
\[
\boxed{A=\ker E\simeq k^{[3]}.}
\tag{19}
\]

For clarity, its source mechanism does not promote an auxiliary
coordinate or slice. Its genuine localized nice flow first makes
\(\beta\) a rational function of the two fixed actual coordinates.
A reduced denominator then yields a primitive polynomial nice
field and an exact kernel presentation over that actual plane.
The surviving good partial descends. The already audited commuting
LND, planar LND, relative cancellation, and actual invariant-coordinate
recognition results complete the argument using the original
sliced kernel. None is applied here to a merely generic coordinate
system or to an assumed slice on \(D\).

Together with Section 2 this handles every alternative in the
frozen dependent constant-top cubic reduction.

## 7. Proof and source scope

This argument reuses the complete pass66 affine-acceleration and
residual-curve theorem, including its inherited de Bondt
polynomial-curve input. The complete frozen note was reread before
this deduction. The complete proof of the pass41 one-good-output
lemma was also reread, and its precise hypotheses were checked
in Sections 5--6. This is an application of that established
recognition gate, not a new classification theorem claimed without
its source dependencies.

The original slice is unchanged throughout. The new field is
localized only at the explicit original invariant \(g_0\), which
it is proved to annihilate. Neither \(\sigma\) nor \(u\) is asserted
to be an ambient coordinate. Recognition follows from the actual
two-output nice symmetry and surviving good partial.

Root and Jet independently reconstructed the correction, all
denominator identities, and the local-nilpotence and coordinate
gates before this note was saved. A later complete-file audit is
separate from those outline reconstructions.
No new numerical suite or shared metadata edit is attached to this
written all-instance deduction. Frozen pass66 files are unchanged.

The theorem concerns the dependent-defect constant-top cubic sector
with the supplied frame. It does not address higher flow degrees
or nonconstant highest vectors, certify historical novelty, or
solve unrestricted complex-threefold cancellation.

