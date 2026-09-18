# The dependent common-power moving cubic is recognized

The common-power cubic alternative of the dependent-defect reduction
also has one normalized defect direction. Original defect independence
was not needed for the rational companion and symmetry arguments of
pass69 once that normalized rank was established. Rechecking that
rank gives recognition of this particular dependent moving branch.

The polynomial-curve reduction itself is not new here: the stronger
joint preceding-layer statement was already proved in
[pass44, Section 2](dependent-preceding-curve-pass44.md). The result
below transfers the completed pass69 recognition argument to its
common-power cubic alternative. It does not treat the rotating
alternative or moving flow degree four.

## 1. Actual hypotheses and exact scope

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}(B),\qquad E(s_*)=1,\qquad A=\ker E.
\]
These are actual polynomial coordinates, with partials satisfying
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Suppose the original quadratic defects are dependent:
\[
V_X=aD,\qquad V_Y=bD,\qquad
D\in\operatorname{LND}(B)\text{ primitive},\qquad
[E,D]=0,\qquad a,b\in\ker E\cap\ker D.
\tag{2}
\]
A complex constant relation between the defects already supplies a
third good partial and the mixed recognition theorem. Retain the
branch with no such relation. In particular both multipliers are
nonzero.

The [full dependent highest-vector reduction](dependent-defect-top-line-pass43.md)
gives, in the moving cubic case,
\[
z=E^2x,\qquad E^3x=cq,\qquad E^4x=0,\qquad
c\in k^4\setminus\{0\},\quad c_X=c_Y=0,\quad
q\in(\ker E\cap\ker D)\setminus k,
\]
\[
Dz=c\theta,\qquad
\rho=a z_X+b z_Y=qr,\qquad
r\in\ker E\cap\ker D,\qquad [E,T_c]=-rD.
\tag{3}
\]
Here \(\theta\in B\), with \(E\theta=0\); no assertion
\(D\theta=0\) is needed. If \(r=0\), the actual good constant
partial \(T_c\) commutes with \(E\), and that branch is already
recognized. Assume \(r\ne0\). The same original-slice reduction
proves that \(E,D\) are fraction-field independent.

Assume precisely the common-power alternative of
[pass44, equations (14)--(15)](dependent-preceding-curve-pass44.md):
\[
q=g^3,\qquad (z_X,z_Y)^t=\lambda g^2,\qquad
0\ne\lambda\in k^2,\qquad
g\in(\ker E\cap\ker D)\setminus k.
\tag{4}
\]
In particular this does not assume merely that \(q\) happens to
be a cube while leaving the preceding bad pair arbitrary.

Constant changes within the good and bad coordinate pairs put
\(c=e_1\) and \(\lambda=(1,0)^t\), preserving (1), the original
slice, and the actual polynomial coordinate ring. Thus
\[
E^3x=e_1g^3,\qquad E^2X=g^2,\qquad E^2Y=0.
\tag{5}
\]
Notation (2)--(3) is retained after these changes. In particular
\(\rho=ag^2=g^3r\), so \(a=gr\ne0\).

**Theorem.** Under these hypotheses,
\[
\boxed{A\simeq k^{[3]}.}
\tag{6}
\]

## 2. The normalized rank is one without original defect independence

Put \(W_i=[E,T_i]\) and \(\delta=E/g\) on the actual invariant
localization \(B_g\). Because \(Eg=Dg=0\), both \(\delta,D\)
are commuting LNDs there. No coordinate partial is presumed
locally nilpotent on that localization.

The original next bad-column coefficient, including its scalar
factor, is
\[
V_i z=-\frac23W_i(E^3x)=-2e_1g^2W_i g.
\]
Writing \(a_X=a,a_Y=b\), equation (3) gives
\[
W_i g=-\frac{a_i\theta}{2g^2},\qquad
\widetilde V_i:=\operatorname{ad}_\delta^2T_i
=g^{-2}V_i+2g^{-3}(W_i g)E
=\frac{a_i}{g^2}\left(D-\frac{\theta}{g^3}E\right).
\tag{7}
\]
The derivatives \(W_i g\) are actual polynomials, although their
displayed quotients initially belong to the fraction field.
No denominator has been silently cleared to a unit.

Since \(E,D\) are independent and \(a\ne0\), the two normalized
defects have rank exactly one. Their line is independent of
\(\delta\). Thus
\[
\operatorname{rank}(\widetilde V_X,\widetilde V_Y)=1,\qquad
\operatorname{rank}(\delta,\widetilde V_X)=2.
\tag{8}
\]
This is the step that replaces original defect independence in
the pass69 rank-drop proof.

The original highest good-column identity gives \(W_jg=0\)
for \(j=1,2\), and (2) gives \(V_i g=0\) for bad \(i\).
The direct rescaling identities therefore retain
\[
\operatorname{ad}_\delta^2T_1=\operatorname{ad}_\delta^2T_2=0,
\qquad
\operatorname{ad}_\delta^3T_X=\operatorname{ad}_\delta^3T_Y=0,
\qquad
\delta^3x=e_1,\quad \delta^2X=1,\quad\delta^2Y=0.
\tag{9}
\]
For the third adjoint the extra term is \(3g^{-4}(V_i g)E\);
for the second it is the term displayed in (7).
These identities hold on the original fraction field and on
the relevant actual invariant localization.

One may also verify actual local nilpotence of the common line.
Set \(\sigma_0=z_1/g^2\), so
\(\delta\sigma_0=1\) and \(D\sigma_0=\theta/g^2\).
The actual slice projection
\[
D-(D\sigma_0)\delta=D-\theta E/g^3
\]
is an LND on \(B_g\) by the complete
[projection lemma](projected-cubic-defects-pass69.md), Section 1.
It kills \(g,a,b\), so the two replicas in (7) are LNDs there.
This observation is not required to treat any localized coordinate
partial as an LND.

## 3. The same rational companion supplies the affine layer

Here is the part of the pass69 proof needed after the changed
rank argument. It is included to avoid applying a theorem with
an unmatched original-rank hypothesis.

Let \(\mathcal D=\widetilde V_X\), write
\(\widetilde V_Y=\eta\mathcal D\), and put
\[
P=\delta x,\qquad J=\operatorname{Jac}P,\qquad
d=\mathcal D(x),\qquad \ell=(0,0,1,\eta),\qquad
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}.
\]
The normalized adjoint identities imply
\([\delta,\mathcal D]=0\) and \(\delta\eta=0\).
The divided flow and conjugated original partials give inverse
matrices over \(\operatorname{Frac}(B)[t]\), with constant
determinant one. Their upper-block coefficients give
\[
M^5=0,\qquad
(M^j)_{\mathrm{UL}}=\frac{\operatorname{Jac}(\delta^jx)}{j!}.
\tag{10}
\]
The two-sided rank-preserving block argument first makes
\(M^4=0\), then \(M^3=0\), because the corresponding upper
blocks vanish and \(d,\ell\ne0\).
The velocity identity makes \(M^2\ne0\).
A cube-zero five-dimensional matrix has at most one block of
size three, so \(M^2\) and its upper block have rank one.

The image of \(\operatorname{Jac}(\delta^2x)\) contains
\(e_1\), because its value on \(P\) is \(\delta^3x=e_1\).
Consequently, with \(\sigma=(\delta^2x)_1\in B_g\),
\[
\delta^2x=e_1\sigma+e,\qquad
e\in k^4,\quad e_B=(1,0),\qquad\delta\sigma=1.
\tag{11}
\]
All four ordinary partials kill the remaining components, so
these are complex constants, not arbitrary invariants.

The full lower row and velocity coefficients give
\[
\ell J=d\sigma,\qquad Je_1=d,\qquad
J(e_1\sigma+e)-\frac{\ell P}{2}d=\frac{e_1}{2}.
\tag{12}
\]
In the first identity \(d\sigma\) is the ordinary differential
row. The variable row \(\ell\) has not been differentiated;
in particular it has not been replaced by \(d(\ell P)\).

Define
\[
F=\delta X-\sigma,\qquad G=\delta Y,\qquad
\beta=\frac{\sigma-F-\eta G}{2},\qquad
S=T_e+\beta T_1.
\]
The same full identities now yield
\[
\delta F=\delta G=0,\qquad dF+\eta\,dG=0,\qquad
[\delta,S]=0,\qquad \delta\beta=\frac12,\qquad
S\sigma=SF=SG=0.
\tag{13}
\]
For example
\(Je=e_1/2+(F+\eta G-\sigma)d/2\), while
\([\delta,T_1]=-\,\mathcal D\); these give the commutator
with the stated sign.
Commutation with (11) gives \(S\sigma=0\), and commutation
on \(X,Y\), whose \(S\)-images are \(1,0\), gives \(SF=SG=0\).
All these are rational identities. No denominator of \(\beta\)
has been claimed invariant.

## 4. All normalized transverse speeds are recognized

If \(G\notin k\), its full ordinary differential is nonzero.
The Lie derivative of the last one-form relation in (13) gives
\[
0=d(SF)+(S\eta)dG+\eta\,d(SG)=(S\eta)dG.
\]
Thus \(S\eta=0\), and
\[
S\beta=0,\qquad S^2x=0.
\tag{14}
\]
The constant directions \(e_1,e\) are independent because
their bad projections are \(0,(1,0)\). Complete them to an
actual constant coordinate frame with
\(T_1=\partial_\xi,T_e=\partial_\zeta\).
The original good partial \(T_1\), original slice, and rational
field \(S\) meet exactly the hypotheses of the
[rational two-direction recognition theorem](rational-two-direction-recognition-pass69.md).
Its coefficient constant is \(1/2\). That theorem first derives
\(Sg=0\) from the original slice, then treats its parallel and
radial coefficient alternatives with the appropriate actual-ring
endpoint. It proves (6), without an assumption \(S\in
\operatorname{LND}(B_g)\).

If \(G=0\), the original coordinate \(Y\) satisfies \(EY=0\).
The invariant-coordinate regular-kernel endpoint, with the unchanged
original slice, gives (6).

It remains \(G\in k^*\). The ordinary relation in (13) also
makes \(F\) constant, but its value is unnecessary. The original
full highest identity is
\[
J_E(E^3x)=V_X(x)g^2,\qquad J_E=\operatorname{Jac}(Ex).
\]
Since \(E^3x=e_1g^3\) and \(W_1(x)=-J_Ee_1\), it gives
\[
gW_1=-V_X.
\tag{15}
\]
Original independence of \(V_X,V_Y\) is not used.

Make the actual complex-coefficient shear
\[
q_1=Q_1-\frac{XY}{2G}+\frac{Y^3}{12G^3},\qquad
q_2=Q_2,\qquad x_3=X,\qquad x_4=Y.
\tag{16}
\]
Its inverse changes the two added signs and fixes \(Q_2,X,Y\).
The new partials are
\[
T'_1=T_1,\quad T'_2=T_2,\quad
T'_X=T_X+\frac{Y}{2G}T_1,\qquad
T'_Y=T_Y+\left(\frac{X}{2G}-\frac{Y^2}{4G^3}\right)T_1.
\]
Using \(EY=Gg\), \(E^2X=g^2\), \(E^2Y=0\) and (15), the
exact commutator product rule gives
\[
\operatorname{ad}_E^2T'_X=V_X+gW_1=0,\qquad
\operatorname{ad}_E^3T'_Y=0.
\tag{17}
\]
For the second equality the multiplier
\(X/(2G)-Y^2/(4G^3)\) has second \(E\)-derivative zero.
The two original good partials are unchanged. Thus this is an
actual \((1,1,1,2)\)-bounded frame with the original slice.
The complete [mixed slice theorem](../deep-pass-13.md), Section 1,
proves (6). Equivalently, every calculation in the separate
[constant-speed shear proof](cubic-rank-drop-constant-speed-closure-pass69.md)
still applies after the new rank justification in Section 2.

## 5. Deduplication, denominators, and the remaining boundary

The rank inequality
\(\operatorname{rank}\operatorname{Jac}(z,q)\le2\), and the
actual polynomial curve form
\(z=c\tau+K(u),q=Q(u),Eu=Du=0\), were already proved for
both moving orders three and four in pass44. This note does
not count that reduction again. The common-power input (4)
is exactly one of its two exhaustive weighted-curve alternatives.

Only the polynomial factor \(g\) is inverted to form \(\delta\).
The rational symmetry coefficient may have other poles.
Those poles are handled by the complete rational-recognition
theorem, not by a claim that every rational nice field is
locally nilpotent on its displayed localization.
The constant-speed shear has only nonzero complex constants
as denominators and acts on the original polynomial ring.

The rotating cubic alternative does not in general have
\(q=g^3\) and \(z_B=\lambda g^2\). Dividing its action by an
arbitrary root or by \(q\) does not supply (9) or (11).
It therefore remains outside this proof. Moving order four
also remains outside this cubic transfer. Previously recognized
zero-motion, omitted-good-direction and ramification subcases
are retained; none is being reopened.

The complete pass44 curve reduction, the pass69 rational
recognition proof and both rank-drop proofs were read through
EOF for this transfer. The curve source, de Bondt Corollary 3.2
and Lemma 3.3, is inherited through pass44; their retained primary
statements and proofs were also reread. The one-good-output,
plane and original invariant-coordinate theorem dependencies
of the recognition endpoint remain necessary. No fresh full
review of every historical primary theorem proof is claimed.

This file contains a bounded written hypothesis-transfer proof.
It adds no numerical method, regression run, shared metadata
change, human expert review, formal verification or historical
novelty claim. Frozen files through pass68 and the separate
pass69 mathematical files are unchanged.
