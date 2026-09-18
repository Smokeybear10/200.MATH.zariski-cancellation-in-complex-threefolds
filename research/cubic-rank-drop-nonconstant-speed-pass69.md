# Recognition in the cubic rank-drop branch with nonconstant residual speed

In the independent moving cubic branch of original joint rank two,
division by the invariant top factor leaves one normalized defect
direction. Its constant-top companion still gives an affine
acceleration layer, without treating the localization as a polynomial
four-ring. When the normalized transverse speed is nonconstant, the
full ordinary differential relation forces a rational two-direction
symmetry to be nice. The separate rational-symmetry recognition
theorem then recognizes the original sliced kernel.

Two elementary boundary cases are recognized as well. The nonzero
constant normalized transverse speed is deliberately left outside
the conclusion proved here.

## 1. Original frame and exact rank drop

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}(B),\qquad Es_*=1,\qquad A=\ker E.
\]
These four generators are actual polynomial coordinates. Their
partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\]
Write \(V_i=\operatorname{ad}_E^2T_i\) for \(i=X,Y\).
Retain
\[
\operatorname{rank}(V_X,V_Y)=2,\qquad
\operatorname{rank}(E,V_X,V_Y)=2,\qquad
E^3x=e_1g^3,\quad L_0E^2x=(1,0)^tg^2,
\]
\[
g\in\ker E\setminus k,\qquad E^4x=0.
\tag{1}
\]
The constant pairwise changes giving this normalization are the
actual ones in [pass42](two-quadratic-top-line-pass42.md),
Sections 1 and 5. The alternative with zero preceding bad vector
was already recognized there and is not part of (1).

Put \(\delta=E/g\) on the actual invariant localization \(B_g\).
It is an LND there. The exact formulas are
\[
\widetilde V_i=\operatorname{ad}_\delta^2T_i
=g^{-2}V_i+2g^{-3}([E,T_i]g)E,\qquad i=X,Y.
\tag{2}
\]
The highest original good and bad identities retain all the
normalized adjoint bounds. The exact rank formula gives
\[
\operatorname{rank}(\widetilde V_X,\widetilde V_Y)=1,\qquad
\langle\delta,\widetilde V_X,\widetilde V_Y\rangle
=\langle E,V_X,V_Y\rangle,
\]
\[
\delta^3x=e_1,\qquad \delta^2X=1,\qquad \delta^2Y=0.
\tag{3}
\]
The surviving defect line is independent of the \(\delta\)-line.
No local nilpotence of a coordinate partial on \(B_g\) is assumed.

The calculations below need the normalized defects as commuting
rational fields, not a primitive polynomial decomposition of them.
Choose a nonzero one as \(D\); write
\(\widetilde V_X=aD,\widetilde V_Y=bD\) over \(K=\operatorname{Frac}B\).
The normalized adjoint bounds imply
\[
[\delta,D]=0,\qquad \delta a=\delta b=0.
\tag{4}
\]
One coefficient can be chosen to be one. Neither coefficient is
asserted to be an actual polynomial.

## 2. A rational companion gives an actual localized affine layer

Write
\[
P=\delta x,\quad J=\operatorname{Jac}P,\quad d=D(x),\quad
\ell=(0,0,a,b),\quad
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}.
\]
All matrices here are over \(K\). The actual divided flow and
conjugated partials give inverse polynomial matrices in the time
variable:
\[
\mathcal C(z)=I-zJ+\frac{z^2}{2}d\ell,\qquad
\mathcal C(z)^{-1}
=I+zJ+\frac{z^2}{2}\operatorname{Jac}(\delta^2x).
\]
Their determinants are units of \(K[z]\), with value one at zero.
Schur elimination and comparison of upper blocks therefore give
\[
M^5=0,\qquad (M^j)_{\rm UL}
=\frac{\operatorname{Jac}(\delta^jx)}{j!}.
\tag{5}
\]
No polynomial-ring recognition theorem has been applied to \(B_g\).

Both \(d\) and \(\ell\) are nonzero. The usual two-sided
rank-preserving block lemma therefore applies over \(K\).
First \(M^4\), then \(M^3\), has zero upper block and is killed
on both sides by \(M\); hence
\[
M^3=0.
\]
The full velocity identity has
\[
M^2\binom P0=\binom{e_1/2}{\ell\,\delta^2x}\ne0.
\]
A five-dimensional cube-zero matrix has at most one block of
size three. Thus \(M^2\), and its upper block, have rank one:
\[
\operatorname{rank}\operatorname{Jac}(\delta^2x)=1.
\tag{6}
\]

Its image contains
\(e_1=(\operatorname{Jac}(\delta^2x))P\).
Set \(\sigma=(\delta^2x)_1\in B_g\). Every remaining component
of \(\delta^2x-e_1\sigma\) is killed by every ordinary actual
partial, so is a complex constant. Consequently
\[
\delta^2x=c\sigma+e,\qquad c=e_1,\quad
e\in k^4,\quad e_B=(1,0),\qquad \delta\sigma=1.
\tag{7}
\]
Here \(e_B\) denotes the two bad components. The constants really
belong to \(k\), because the constants of all four rational
coordinate derivatives on \(K\) are \(k\). No coordinate
assertion about \(\sigma\) is made.

The same full image and velocity coefficients give
\[
\ell\operatorname{Jac}P=(\ell e)\,d\sigma,\qquad
Jc=(\ell e)d,\qquad
J(c\sigma+e)-\frac{\ell P}{2}d=\frac c2.
\tag{8}
\]
The lower row is \(\ell\operatorname{Jac}P\), not
\(d(\ell P)\). The variable multipliers have not been
differentiated.

## 3. A zero first normalized defect is already recognized

Suppose \(\widetilde V_X=0\). Choose \(D=\widetilde V_Y\),
so \(a=0,b=1\), and \(\ell e=0\) by (7).
Equation (8) gives
\[
[\delta,T_c]=-Jc=0.
\]
The actual constant partial \(T_c\) has square zero on all
polynomial coordinates. The original-slice unit argument applies:
the formal exponentials of \(g\) and \(1/g=\delta s_*\) under
\(T_c\) are polynomials in time and multiply to one. Therefore
\[
T_cg=0,\qquad [E,T_c]=0.
\tag{9}
\]
A complementary actual good direction remains available.
The complete one-good-output lemma with denominator one gives
an original invariant coordinate and \(A\simeq k^{[3]}\).

This argument does not infer local nilpotence of \(T_c\) on
\(B_g\) before proving that it fixes the inverted element.

## 4. The full residual differential identity

Assume now \(\widetilde V_X\ne0\).
Choose
\[
D=\widetilde V_X,\qquad
\widetilde V_Y=rD,\qquad r\in K,\qquad \delta r=0.
\]
Thus \(a=1,b=r,\ell e=1\).
Define the actual localized functions
\[
F=\delta X-\sigma,\qquad G=\delta Y.
\]
They satisfy
\[
\delta F=\delta G=0,\qquad
\delta X=\sigma+F,\quad \delta Y=G,\qquad
dF+r\,dG=0.
\tag{10}
\]
The last equality is the first identity of (8), as an equality
of full ordinary rational one-forms on the original fraction
field. It is stronger than a relation involving only
\(\delta\)-derivatives.

Set
\[
\beta=\frac{\sigma-F-rG}{2},\qquad
S=T_e+\beta T_c.
\tag{11}
\]
The coefficient need not belong to \(B_g\); it is an element
of the original fraction field. Equations (8),(10) give
\[
Je=\frac c2+\frac{F+rG-\sigma}{2}d,
\]
\[
[\delta,T_c]=-D,\qquad
[\delta,T_e]=-\frac12T_c+\beta D,\qquad
\delta\beta=\frac12,\qquad [\delta,S]=0.
\tag{12}
\]
No claim that \(S\) is locally nilpotent has entered these
calculations.

Since \(Sx=e+\beta c\) and \(\delta^2\beta=0\),
commutation applied to (7) gives \(S\sigma=0\).
Since \(S(X,Y)=e_B=(1,0)\), applying commutation once to the
bad coordinates then gives
\[
S\sigma=SF=SG=0.
\tag{13}
\]

## 5. A nonconstant normalized transverse speed recognizes the kernel

Suppose \(G\notin k\). Its full ordinary differential is nonzero.
Apply the Lie derivative by the rational derivation \(S\)
to the last equality in (10). Lie derivative commutes with
ordinary exterior differentiation on \(K\). Using (13) gives
\[
0=d(SF)+(Sr)dG+r\,d(SG)=(Sr)dG.
\]
Thus
\[
Sr=0,\qquad S\beta=0,\qquad S^2x=0.
\tag{14}
\]
No polynomial-curve parameter, algebraic dependence of \(g\)
on that parameter, or invariance of a guessed denominator is
needed for this implication.

The two complex vectors \(c,e\) are independent since their
bad projections are \(0,(1,0)\). Complete them to a complex
constant coordinate frame so that
\[
T_c=\partial_a,\qquad T_e=\partial_b,\qquad
S=\partial_b+\beta\partial_a.
\]
The actual original good bound
\(\operatorname{ad}_E^2\partial_a=0\) survives.
Equations (12),(14), the original slice, and the original
\(g\in\ker E\) meet every hypothesis of the separately proved
[rational two-direction recognition theorem](rational-two-direction-recognition-pass69.md),
with \(\kappa=1/2\). Therefore
\[
\boxed{\widetilde V_X\ne0,\ G\notin k
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.}
\tag{15}
\]

That theorem first uses the original slice to prove \(Sg=0\)
and \([E,S]=0\). It does not assume these facts from
\([\delta,S]=0\). Its classification of a rational nice
two-direction coefficient then either supplies an actual
invariant localization for a parallel field or forces \(E\)
to preserve an actual polynomial plane in the radial case.
The latter field is not falsely promoted to an LND of its
displayed localization. Both endpoints concern the original
action and slice.

## 6. Zero speed and the exact remaining branch

If \(G=0\), the original bad coordinate \(Y\) has \(EY=gG=0\).
The established original invariant-coordinate endpoint, with
the original slice and regular kernel, gives \(A\simeq k^{[3]}\).

The only case not covered by Sections 3, 5 and this zero-speed
endpoint is
\[
\widetilde V_X\ne0,\qquad G\in k^*.
\tag{16}
\]
In that case (10) forces \(dF=0\), hence \(F\in k\).
The full differential relation is now identically zero.
Its Lie derivative supplies no information about \(Sr\).
In particular the proof above does not assert \(S\beta=0\)
or apply the rational-symmetry recognition theorem in (16).

This is a precise limitation of this deduction, not a realization
of an unknown kernel. A separate analysis of the actual
constant-\((F,G)\) equations may recognize that branch.
The statement here neither closes the entire moving cubic
rank-drop case nor the supplied profile.

## Dependencies and verification scope

The exact original-to-divided rank formula and retained adjoint
bounds were reread in pass42 Section 5. The full dependent
constant-cubic proof from pass67 and the moving local-slice
proof from pass68 were also reread. Their use here is limited
to actual matrix identities and explicitly rederived rational
calculations. No original-ring recognition theorem is applied
directly to \(B_g\).

The companion argument uses rational rank-one factorization only.
It does not need the separate normalized-defect LND result,
does not assume a primitive normalized defect is polynomial on
\(B\), and does not call the localized partials LNDs.
The full rational two-direction recognition proof was read
through EOF before its application. Its complete one-good-output,
original-slice unit, plane and invariant-coordinate source
obligations remain part of the endpoint; no fresh full-paper
source audit is asserted.

All computations above are written identities. There is no new
numerical suite or method count, metadata edit, human review,
proof-assistant certificate, historical novelty claim, or
unrestricted cancellation claim. Frozen files through pass68
are unchanged.

