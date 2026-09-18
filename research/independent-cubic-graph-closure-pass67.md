# An actual coordinate slice in the independent constant-top cubic case

The independent constant-top cubic normal form is recognized.
Its two good coordinates lie on an actual polynomial graph over
\(k(t,f)\). Three coefficients of the true good-partial determinant
force a triangular ambient coordinate to be a slice of the original
action. No bad-projection hypothesis or Jacobian-conjecture implication
is used.

This theorem concerns the supplied coordinate frame with constant
third flow derivative. It does not recognize a moving cubic top or
produce a frame for an arbitrary sliced action.

## 1. Actual normal form and retained hypotheses

Work over \(k=\mathbb C\), with the actual polynomial coordinates
\[
B=k[Q_1,Q_2,X,Y]=A[s_*],\qquad
E\in\operatorname{LND}_k(B),\qquad Es_*=1,\qquad A=\ker E.
\]
The first two actual partials \(T_1,T_2\) have second \(E\)-adjoint
zero; the bad partials \(T_X,T_Y\) have third \(E\)-adjoint zero.
The defects \(V_3,V_4\) are independent.

The complete [constant-top normal-form theorem](constant-top-cubic-pass65.md)
reduces the cases not already recognized to
\[
E^3(Q_1,Q_2,X,Y)^t=e_1,\qquad
E^2(Q_1,Q_2,X,Y)^t=(f-F(t),U(t),1,0)^t,
\tag{1}
\]
\[
EX=f,\qquad EY=G(t),\qquad Ef=1,\qquad Et=0,
\tag{2}
\]
\[
\ker(V_3,V_4)=k[t,f],\qquad
\ker(E,V_3,V_4)=k[t].
\tag{3}
\]
Here \(t,f\) are algebraically independent actual polynomials.
Both \(U,G\in k[t]\) are nonconstant.
The original coordinate changes establishing this form are only
constant changes within the good and bad pairs.

Write \(P=E(Q_1,Q_2,X,Y)^t\) and \(J=\operatorname{Jac}P\).
The [good-field identity](constant-top-cubic-good-fields-pass66.md)
gives
\[
V_3=Je_1=-W_1,\qquad
U'W_2+F'V_3+G'V_4=0,\qquad W_i=[E,T_i].
\tag{4}
\]
Primes in this note denote one-variable differentiation in \(t\).
All derivations extend to the actual fraction field by the quotient
rule. Local nilpotence is not presumed after inverting a moving
slice polynomial.

The rational joint kernels in (3) are exactly \(k(t,f)\) and \(k(t)\).
Indeed, if a reduced fraction \(p/q\) is killed by any LND of \(B\),
then \(p\mid Dp\) and \(q\mid Dq\). The LND degree argument forces
\(Dp=Dq=0\). Applying this to each relevant field proves the stated
rational-kernel equalities from (3).

## 2. Exact good velocities

For compactness define rational functions of \(t\)
\[
a=\frac{F'}{2G'},\qquad C=\frac{U'}{2G'},\qquad
d=aG-F,\qquad b=U-CG.
\tag{5}
\]
The denominators are nonzero because \(G\) is nonconstant.
Define actual \(E\)-invariant polynomials
\[
x=X-\frac{f^2}{2},\qquad y=Y-Gf.
\tag{6}
\]
These symbols \(x,y\) are auxiliary invariant polynomials, not
a replacement ambient coordinate pair.

Equation (1) integrates with respect to the actual slice \(f\):
\[
P_1=\frac{f^2}{2}-Ff+A_0,\qquad
P_2=Uf+C_0,\qquad A_0,C_0\in\ker E.
\]
The good quadratic flow coefficients say
\[
W_iP=-\frac12T_i(E^2Q),\qquad i=1,2.
\tag{7}
\]
Here \(Q=(Q_1,Q_2,X,Y)^t\).
Combining (4),(7), and the bad components of
\(W_iQ=-T_iP\), proves, for each \(V\in\{V_3,V_4\}\),
\[
VP_1=\frac12VX-a\,VY,\qquad VP_2=C\,VY.
\tag{8}
\]
For example \(V_3X=T_1f\) and \(V_3Y=G'T_1t\); the
second good field supplies the independent remaining equation.
No determinant of the bad projections has been assumed nonzero.

Since \(Vt=Vf=0\), equation (8) shows that
\(A_0-x/2+ay\) and \(C_0-Cy\) are killed by both defects
and by \(E\). The rational joint-kernel assertion gives
\(k,l\in k(t)\) such that
\[
A_0=x/2-ay+k,\qquad C_0=Cy+l.
\]
Equivalently, the actual velocities satisfy
\[
P_1=X/2+f^2/4+df-aY+k,\qquad
P_2=CY+bf+l.
\tag{9}
\]
Rational coefficients in this identity are not asserted individually
polynomial. The complete left sides remain the actual polynomial
velocities.

## 3. The good-coordinate graph is obtained before generation

The relation (4) also expresses both defects as rational combinations
of the first two columns of \(J\):
\[
V_3=Je_1,\qquad
V_4=\frac{U'}{G'}Je_2-\frac{F'}{G'}Je_1.
\]
The actual good partials fix \(X,Y\). Applying their chain rules
to the rational expressions (9), then taking these combinations,
gives, for \(V=V_3,V_4\) and \(i=1,2\),
\[
VQ_i=(P_i)_t\,\frac{VY}{G'}+(P_i)_f\,VX.
\tag{10}
\]
The partial derivatives on the right treat \(X,Y,t,f\) as the
displayed arguments of the rational formulas (9).
This chain-rule use is legitimate before those four arguments
are proved independent: it is the differentiation of a rational
expression at its actual polynomial inputs.

Integrating (1)--(2) once more with the slice \(f\), put
\[
B_1=Q_1-f^3/6+Ff^2/2-A_0f,\qquad
B_2=Q_2-Uf^2/2-C_0f.
\]
Both polynomials are \(E\)-invariant.
Using (9) in (10), and substituting \(Y=y+Gf\), gives
\[
VB_1=d\,Vx+\frac{-a'y+k'}{G'}\,Vy,\qquad
VB_2=b\,Vx+\frac{C'y+l'}{G'}\,Vy.
\tag{11}
\]
The cancellation in the first formula uses
\(d'-a'G=-F'/2\); the second uses \(C'G+b'=U'/2\).

Subtract the explicit potentials on the right of (11).
Their differences are killed by \(V_3,V_4,E\), so (3) gives
\(m,n\in k(t)\). The resulting exact graph is
\[
\begin{aligned}
Q_1={}&f^3/6-Ff^2/2+(x/2-ay+k)f\\
 &+dx-\frac{a'}{2G'}y^2+\frac{k'}{G'}y+m,\\
Q_2={}&Uf^2/2+(Cy+l)f\\
 &+bx+\frac{C'}{2G'}y^2+\frac{l'}{G'}y+n.
\end{aligned}
\tag{12}
\]
This is an equality in \(\operatorname{Frac}B\).
It was derived through actual joint-kernel equalities, not by
assuming that the bad coordinates are a generic coordinate pair.

## 4. Actual generation supplies the determinant gate

Set \(K=k(t,f)\). Localize the actual inclusion \(k[t,f]\subset B\).
Equation (12) lies in \(K[X,Y]\), and the four original coordinates
generate the localized ring. Therefore
\[
B\otimes_{k[t,f]}K
=K[Q_1,Q_2,X,Y]
=K[X,Y].
\tag{13}
\]
The left side has transcendence degree two over \(K\).
Consequently \(X,Y\) are algebraically independent over \(K\).
In particular \(t,f,X,Y\) are now a genuine rational coordinate
system for \(\operatorname{Frac}B\).

Let \(\Phi_1,\Phi_2\in K[X,Y]\) be the graph expressions (12), and
differentiate at fixed \(X,Y\):
\[
\mathcal K=\frac{\partial(\Phi_1,\Phi_2)}{\partial(t,f)},\qquad
\mathcal T=
\begin{pmatrix}T_1t&T_2t\\T_1f&T_2f\end{pmatrix}.
\]
All entries of \(\mathcal K\) lie in \(K[X,Y]\).
The actual polynomials \(T_it,T_if\) lie there as well by (13).
Since \(T_iQ_j=\delta_{ij}\) and \(T_iX=T_iY=0\),
\[
\mathcal K\mathcal T=I,\qquad
\det\mathcal K\in K[X,Y]^*=K^*.
\tag{14}
\]
This is an actual polynomial inverse matrix, not a use of the
Jacobian conjecture. It requires the preceding generation equality.

## 5. Three determinant coefficients yield a coordinate slice

In (12), the coefficient of \(X\) in \(\Phi_1\) is \(f/2+d(t)\),
and the coefficient of \(X\) in \(\Phi_2\) is \(b(t)\).
Neither graph has an \(X^2\) or \(XY\) term.
Thus the \(X^2\) coefficient of (14)'s determinant is
\[
[X^2]\det\mathcal K=-b'/2=0.
\tag{15}
\]
Hence \(b=b_0\in k\).
The equation \(U-GU'/(2G')=b_0\) gives
\(((U-b_0)/G^2)'=0\), and therefore
\[
U=b_0+\kappa G^2,\qquad C=\kappa G,\qquad
\kappa\in k^*.
\tag{16}
\]
The nonzero value of \(\kappa\) follows from nonconstancy of \(U\).

Substituting (16) into \(\Phi_2\) cancels all mixed \(fY\)
and quadratic \(f\) terms:
\[
\Phi_2=b_0X+\frac{\kappa}{2}Y^2+LY+(l-GL)f+n,
\qquad L=\frac{l'}{G'}.
\tag{17}
\]
Now \((\Phi_1)_f\) has \(X\) coefficient \(1/2\), while
\((\Phi_2)_t\) has \(Y\) coefficient \(L'\).
No other product in the determinant contributes an \(XY\) term,
so
\[
[XY]\det\mathcal K=-L'/2=0.
\tag{18}
\]
It follows that \(L=a_2\in k\) and \(l=a_2G+l_0\), with
\(l_0\in k\). Thus
\[
\Phi_2=b_0X+\kappa Y^2/2+a_2Y+l_0f+n(t).
\tag{19}
\]

There is one further useful coefficient. The determinant is now
\(l_0(\Phi_1)_t-n'(\Phi_1)_f\). Its \(X\) coefficient gives
\[
l_0d'-n'/2=0,\qquad n=2l_0d+n_0,\qquad n_0\in k.
\tag{20}
\]
If \(l_0=0\), then \(n'=0\), so the entire second row of
\(\mathcal K\) vanishes, contradicting (14).
Consequently \(l_0\ne0\).

Define the actual polynomial
\[
S=\frac{Q_2-b_0X-\kappa Y^2/2-a_2Y-n_0}{l_0}.
\tag{21}
\]
The triangular inverse
\(Q_2=l_0S+b_0X+\kappa Y^2/2+a_2Y+n_0\)
shows that \((Q_1,S,X,Y)\) are genuine ambient coordinates.
Equations (19)--(20) give
\[
S=f+2d(t),\qquad ES=1.
\tag{22}
\]
Thus the polynomial originally represented by the rational
expression \(f+2d(t)\) is an actual ambient coordinate slice.
No claim that \(d(t)\) was polynomial was needed beforehand.

The slice theorem now gives
\[
A=\ker E\simeq B/(S)\simeq k[Q_1,X,Y]\simeq k^{[3]}.
\tag{23}
\]
The first isomorphism is the usual evaluation in \(B=A[S]\).
The second uses the explicit triangular ambient coordinate change
(21). It is not cancellation of an unknown polynomial factor.

## 6. Scope and proof dependencies

This recognizes the complete independent-defect constant-top cubic
sector after the earlier normal-form alternatives. Constant \(G\),
zero preceding bad vector, and the other already recognized
alternatives remain covered by their earlier proofs.
The new remaining branch has an actual coordinate slice directly;
it does not need a fixed-coordinate regular-kernel theorem at
its final step.

The generic graph and determinant use the actual inclusion of
\(k[t,f]\), both rational joint-kernel equalities, and the genuine
coordinate partials. A formal graph with no actual generation
would not justify (13)--(14). Conversely, a nonzero bad-projection
determinant was not inserted as an extra hypothesis.

The [pass65 normal form](constant-top-cubic-pass65.md) retains its
stated polynomial-curve and prior recognition source obligations.
The [pass66 good-field refinement](constant-top-cubic-good-fields-pass66.md)
supplies the full inverse-Jacobian identity used in (4).
The new integrations, determinant coefficients and triangular
coordinate construction are written explicitly above.

No full two-quadratic-profile theorem, moving-top recognition,
universal frame-existence theorem, historical novelty certification,
human expert review, external contact, or proof-assistant verification
is claimed. The unrestricted cancellation question remains separate.
