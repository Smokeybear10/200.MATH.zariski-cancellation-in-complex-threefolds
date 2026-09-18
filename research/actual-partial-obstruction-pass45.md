# A genuine coordinate partial can retain compatibility torsion

The condition \(U=[E,T_c]\), with \(T_c\) an actual constant
coordinate partial and \([E,U]=0\), does not by itself remove the
height-one obstruction from the preceding pass. The example below
even belongs to the supplied two-quadratic adjoint bounds. Its
obstructed partial is not the highest-flow constant direction, and
it fails the particular second-direction normalization needed in the
remaining power-law branch. Those distinctions are proved explicitly.

## 1. Two actual polynomial coordinate systems

Start in \(B=\mathbb C[x,y,z,s]\), and put
\[
E=\partial_s+x\partial_y+2y\partial_z,
\qquad t=s+yz.
\tag{1}
\]
The physical coordinates are \((x,y,z,t)\); their polynomial inverse
is \(s=t-yz\). In those physical coordinates,
\[
E=x\partial_y+2y\partial_z+(1+xz+2y^2)\partial_t.
\tag{2}
\]
It is a sliced LND, since in (1) it is triangular and \(E(s)=1\).
Take the genuine physical constant partial
\[
T_c=\partial_z\big|_{x,y,t}
=\partial_z\big|_{x,y,s}-y\partial_s.
\tag{3}
\]
Then
\[
U=[E,T_c]=-x\partial_s=-x\partial_t,
\qquad [E,U]=0.
\tag{4}
\]
In particular this is not an arbitrary polynomial derivation being
called a constant partial. Equation (3) is exactly the coordinate
change of the physical partial in (2).

Set
\[
g=x,\qquad Y=xy\partial_s=xy\partial_t.
\tag{5}
\]
Both \(U\) and \(Y\) are actual invariant replicas of
\(\partial_s\), so they are LNDs. Directly,
\[
[E,Y]=-gU,\qquad [Y,U]=0,
\quad Eg=Ug=Yg=T_cg=0.
\tag{6}
\]
Over \(\operatorname{Frac}B\), the pair \(E,U\) has rank two
and \(Y=-yU\), so the triple has rank two. Also \(g\) is a
nonconstant polynomial invariant, not a formal parameter or a unit.

## 2. Exact intrinsic action and its obstruction

The original slice frame is polynomial as well. Define
\[
\eta=y-xs,\qquad \zeta=z-2ys+xs^2.
\tag{7}
\]
Then \(E\eta=E\zeta=0\), and the inverse is
\[
y=\eta+xs,\qquad z=\zeta+2\eta s+xs^2.
\tag{8}
\]
Consequently
\[
A=\ker E=\mathbb C[x,\eta,\zeta],
\quad U(s)=-x,
\quad D:=U|_A=xD_0,
\quad D_0=x\partial_\eta+2\eta\partial_\zeta.
\tag{9}
\]
The intrinsic action is not primitive: its coefficient gcd is
\(x\), and \(D_0\) is primitive. Let
\[
v=x\zeta-\eta^2=xz-y^2,
\qquad R=\ker D=\ker D_0=\mathbb C[x,v].
\tag{10}
\]
For completeness, after inverting \(x\), the kernel statement is
immediate from \(A_x=\mathbb C[x,x^{-1},v,\eta]\). A putative
minimal negative power of \(x\) in an invariant would reduce to
a nonzero polynomial in \(-\eta^2\) modulo \(x\), contradicting
regularity. Thus no denominator survives.

The exact plinth of \(D_0\) is \(xR\). The inclusion
\(xR\subset D_0(A)\cap R\) follows from \(D_0\eta=x\).
If \(D_0h=a\in R\), then \(xh-a\eta\in R\).
Reduction modulo \(x\) separates even and odd polynomials in
\(\eta\), forcing \(a(0,v)=0\). Hence \(x\mid a\) in
\(R\), proving the reverse inclusion. Multiplication by the
invariant \(x\) gives the full plinth \(D(A)\cap R=x^2R\).

An \(E\)-slice killed by \(U\) must be \(s+f\), with
\(f\in A\), and must solve \(Df=x\). Its obstruction is
\([-x]\in A/D(A)\). Cancelling \(x\) in this domain yields
\[
\operatorname{Ann}_R([-x])
=\{a\in R:-a\in D_0(A)\}
=xR.
\tag{11}
\]
Thus no compatible global slice exists. The obstruction also remains
nonzero after localization at the height-one prime \((x)\) of
\(R\), where its annihilator is still the proper ideal \((x)\).
The invariant localization after inverting \(x\) does admit one:
\[
s+\eta/x=y/x,
\qquad E(y/x)=1,\quad U(y/x)=0.
\tag{12}
\]
This is precisely a nonzero, divisor-supported compatibility class,
not failure to find a polynomial primitive by a finite search.

## 3. The supplied adjoint bounds are genuine

Write \(T_x,T_y,T_z,T_t\) for the physical partials. The second
defects are
\[
\operatorname{ad}_E^2 T_x=2T_z+2yT_t,
\qquad \operatorname{ad}_E^2 T_y=-2xT_t,
\qquad \operatorname{ad}_E^2T_z=
\operatorname{ad}_E^2T_t=0.
\tag{13}
\]
Both displayed nonzero defects commute with \(E\); they are
independent over \(\operatorname{Frac}B\). Moreover
\(\operatorname{ad}_ET_z=-xT_t\) and
\(\operatorname{ad}_ET_t=0\).
The individual heights in the ordering \((z,t,x,y)\) are
therefore \((1,0,2,2)\).

A constant change of the good plane makes both good heights one:
take \(a=z-t\), \(b=t\). Then
\(\partial_a=T_z\) and \(\partial_b=T_z+T_t\).
In the actual coordinates \((a,b,x,y)\), the exact individual
heights are \((1,1,2,2)\). No nonlinear or rational frame
substitution is needed for this assertion.

The highest physical iterate is, however,
\[
E^3(x,y,z,t)=(0,0,0,6x^2),\qquad E^4(x,y,z,t)=0.
\tag{14}
\]
Its constant direction is \(T_t\), which commutes with \(E\),
not the obstructed \(T_c=T_z\). The preceding iterate has zero
bad projection: \(E^2(x,y)=(0,0)\). This is the previously
recognized zero-projection branch, not the nonzero power-law branch.
After the good-plane change, the highest direction is
\(-\partial_a+\partial_b\), whose commutator still vanishes.

There is also a direct failure of the required second-direction
identity for the selected obstructed partial. For a constant vector
\(\lambda\), (13) gives
\[
V_\lambda=2\lambda_xT_z+
  (2\lambda_xy-2\lambda_yx)T_t.
\tag{15}
\]
For any nonzero complex scalar \(\alpha\), an equality
\(gU=-\alpha V_\lambda\), with the chosen \(g=x\),
would force first \(\lambda_x=0\), and then
\(\lambda_y=-x/(2\alpha)\). This is impossible for a constant
direction. A rationally or polynomially varying replacement is not
the actual constant bad direction required by the power-law proof.

## 4. Scope and verification

This example refutes automatic compatibility from the following
conditions even when taken together: an actual sliced four-ring,
an actual constant partial with vanishing second adjoint, the supplied
two-quadratic frame bounds, a nonconstant invariant killed by that
partial, an actual rank-two Heisenberg normalizer, and a compatible
slice after inverting that invariant. It does not impose primitivity
of the induced action in (9).

The special highest-direction and normalized second-direction
conditions have not been removed from the remaining problem. The
example does not realize them and therefore does not obstruct their
possible use in a positive recognition theorem. Its original kernel
is explicitly a polynomial three-ring.

The kernel and plinth computations reconstruct the inherited
triangular calculation from the
[height-one note](heisenberg-height-one-bound-pass44.md).
All new coordinate and bracket formulas are explicit. The independent
finite suite [actual_partial_obstruction_checks_pass45.py](actual_partial_obstruction_checks_pass45.py)
checks the displayed example, not a universal classification or the
existence of an unresolved full high-top model. No novelty, external
expert review, proof-assistant verification, or unrestricted
cancellation result is claimed.

The standalone suite has four methods and passed in 0.240 seconds.
Its initial run stopped at a checker-only Python integer that lacked
SymPy's substitution method; replacing that literal by an exact SymPy
integer fixed the harness. No mathematical formula changed.
