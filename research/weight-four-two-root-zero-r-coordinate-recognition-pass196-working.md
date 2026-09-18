# Zero-R recognition for the supplied two-root double-cover configuration

Status: bounded working proof, pending independent saved-source review.
For the supplied actual full initial kernel
\(Z^2-X^2Y(X-Y)\), the branch \(k_\rho=0\) admits an invariant
coordinate in the original polynomial four-ring. A regular-differential
obstruction excludes the second algebraic solution of the slope equation.
Neither the leading square root nor the auxiliary curve parameters are
asserted to be original coordinates.

## 1. Actual hypotheses and the retained general zero-R identities

Assume the actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
with
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\qquad q^2=t(1-t),\qquad R=k_\rho=0.
\end{gathered}
\tag{1}
\]
The ideal in (1) is the entire weighted initial kernel. The supplied
frame and slice are actual. The occurring Z-pivot gives the nonzero
intrinsic derivation \(N=[u^3](\partial_Z|_{\mathcal A})\), the exact
coefficient fields, and the calibrated chart
\[
\begin{gathered}
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\quad Nv=1,\qquad
\mathfrak a=EX\in L^*,\\
t=EY/\mathfrak a,\qquad
\rho=(E^2W/2)/\mathfrak a^2,\qquad
q=(E^2Z/2)/\mathfrak a^2,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
Y=y+tX,\qquad Z=z+(q'y+k)X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
 =-\mathfrak a^3\in L^*.
\end{gathered}
\tag{2}
\]
The determinant is independent of \(X\). The coefficient partials
initially fix \(v\), commute, and extend the independent partials on
\(\mathbb C(t,\rho)\). Differentiating \(q^2=t(1-t)\) in \(\rho\)
puts \(q\) in \(K\). No rationality of \(K\), unit speed in \(B\), or
original-coordinate status of \(q\) is assumed.

Set \(s=1-2t\). Exact differentiation gives
\[
q'=\frac{s}{2q},\qquad q''=-\frac1{4q^3},\qquad
Q:=q''/2=-\frac1{8q^3},\qquad
d:=q'''/6=\frac{s}{16q^5},\qquad Q'=3d\ne0,\qquad h:=k''/2.
\tag{3}
\]
Here \(s\) is not \(n_\rho\). Although \(d\) has zeros on the coefficient
curve, it is a nonzero field element.

The general-q zero-R derivation in Sections 1--3 of
[zero-R192](weight-four-split-zero-r-coordinate-recognition-pass192-working.md)
uses \(q_\rho=0\) and \(q'''\ne0\) before its later split specialization.
For clarity, its actual gates and the coefficient equations used below
are recorded here.

The case \(y\in L\) is impossible. The factorized actual determinant
then forces \(n_\rho=0\), \(\vartheta\in L\), and \(w\) affine over
\(L\). Actual field return gives \(L=\mathbb C(y,z)\). The field
derivative fixing \(L,X\) and sending \(w\) to one is the original
\(\partial_W\); it commutes with \(E\). Thus \(E\) restricts to an LND
on the actual ring \(\mathbb C[X,Y,Z]\), with \(E^2X=E^2Y=0\).
Primitive division preserves the kernel, local nilpotence, and these
second-iterate vanishings. Wang's two-coordinate theorem, as stated in
[Dasgupta--Gupta Theorem 4.1](https://arxiv.org/pdf/1701.03635v1),
gives either an invariant nonzero complex linear form in \(X,Y\), or
an invariant coordinate \(cZ+H(X,Y)\), \(c\in\mathbb C^*\).
The first contradicts transcendental \(t\); the second requires
\(cq+H_2(1,t)=0\), contrary to \(q'''\ne0\).
This is the actual constant-projection argument, not a claim obtained
solely from a formal potential.

Consequently \(y\notin L\). The cubic potential gives
\(\sigma_n:=n_\rho\ne0\), and \(\vartheta,w\) are polynomials in \(y\).
The whole-line identity in (2) makes \(y\) affine in \(v\), with
\(\Gamma=Ny\in L^*\). Write \(\vartheta=P(y)\), \(w=\mathcal W(y)\).
The calibrated equations are
\[
\mathcal W_U=P_t+P_UP_\rho,\qquad
\mathcal W_t+P_U\mathcal W_\rho
 =\frac{\mathfrak a^3}{\sigma_n\Gamma}\in L^*.
\tag{4}
\]
The derivatives here are coefficient derivatives before evaluation.
Neither the speed nor the affine parameter factor has been discarded.

## 2. Polynomial cover and the field gate before any pole argument

The \(U^8\) coefficient in (4) gives
\((\sigma_n^{-2})_{\rho\rho}=0\). With
\(\eta=\sigma_n^{-1}\), \(\partial_n=\eta\partial_\rho\), exact
polynomial primitive subtraction gives
\[
\rho=a n^2+b n+c,\qquad \eta=2an+b,\qquad a,b,c\in K.
\tag{5}
\]
Here \(a\) is a cover coefficient, distinct from the speed
\(\mathfrak a\). Initially \(L/K(n)\) may be a proper finite extension,
and \(n\) is transcendental over \(K\). Let \(\nabla\), also denoted
by a prime, extend the derivative on \(K\) while fixing \(n\).
It extends uniquely across this separable algebraic extension.
Define
\[
F(U)=dU^3+hU^2,\qquad M=\eta\ell,\qquad
P(U)=\rho'U-\eta F(U)+M,\qquad
\delta=\nabla-F_U\partial_n .
\tag{6}
\]
The old partials are
\(\partial_\rho=\eta^{-1}\partial_n\) and
\(\partial_t^{\rm old}=\nabla-(\rho'/\eta)\partial_n\).
Thus (4) becomes \(\mathcal W_U=\delta P\) and
\(\delta\mathcal W=\mathfrak a^3/(\sigma_n\Gamma)\in L^*\).
Integration only in the polynomial variable \(U\) gives
\[
\mathcal W
 =aF^2-\eta'UF
 -\eta\left(\frac{d'}4U^4+\frac{h'}3U^3\right)
 +\frac{\rho''}2U^2+M'U-M_nF+W_0,\qquad W_0\in L.
\tag{7}
\]
In particular the varying-\(d\) term is retained.
For \(\mathcal W_j=[U^j]\mathcal W\), the scalar-equation recurrence is
\[
[U^j]\delta\mathcal W
 =\mathcal W_j'-3d\,\partial_n\mathcal W_{j-2}
                  -2h\,\partial_n\mathcal W_{j-1}.
\tag{8}
\]
Its top equations and \(U^2\) equation give
\[
\begin{gathered}
2da'+ad'=0,\qquad
\mu:=M_{nn}=\frac{ahd'}{d^2}-\frac{4ah'}{3d},\qquad
M=\frac{\mu}{2}n^2+M_1n+M_0,\quad M_1,M_0\in K,\\
3d(W_0)_n=\frac{a'''}2n^2+
 \left(\frac{b'''}2-h'\mu-3h\mu'\right)n+
 \frac{c'''}2-h'M_1-3hM_1',\\
W_0\in K[n],\qquad [n^3]W_0=\gamma:=\frac{a'''}{18d}.
\end{gathered}
\tag{9}
\]
The integrations use polynomial subtraction and
\(\ker_L\partial_n=K\), not an assumption \(L=K(n)\).
These are general coefficient identities, not formulas specialized
to either of the earlier rational choices of \(d\).

Now \(z=n+Qy^2+k'y\) and \(w=\mathcal W(y)\) belong to \(K[n,y]\).
The actual field equality in (2), followed by comparison in the
independent variable \(y\), gives
\[
L=K(n),\qquad
K(y)(z)=\mathbb C(y,z,w),\qquad n=z-Qy^2-k'y .
\tag{10}
\]
In particular \(y,z\) are independent over \(K\). The pole arguments
below use this actual degree-one field return, not just the scalar
equations or the polynomial nature of the projected parametrization.

## 3. The simple zero of d excludes the quadratic cover

Suppose \(a\ne0\). From (9),
\[
a^2d\in\mathbb C^*.
\tag{11}
\]
Choose a place of \(K\) above \(t=\tfrac12\), and put
\(e=\operatorname{ord}(t-\tfrac12)>0\).
At that place \(q\) is a unit, since \(q^2=\tfrac14\); hence \(d\)
has order \(e\) by (3). Equation (11) forces
\(\operatorname{ord}(a)=-e/2\), so \(e\) is even.
The local leading exponent of \(a\), in \(t-\tfrac12\), is
\(-\tfrac12\). Three derivatives have nonzero leading coefficient
\((-\tfrac12)(-\tfrac32)(-\tfrac52)\). Therefore
\[
\operatorname{ord}(\gamma)=-\frac{9e}{2}\le-9.
\tag{12}
\]
This calculation is at a place of the actual finite coefficient field.
It does not treat a ramified coefficient as a rational function of \(t\).

All terms of (7) other than \(W_0\) have \(n\)-degree at most two.
After substituting (10), \(w\) is consequently a cubic polynomial in
\(z\) with leading coefficient \(\gamma\).
Extend the chosen valuation by the independent variables \(y,z\).
The independent monomials cannot cancel its leading residue polynomial,
so \(w\) has a pole of order at least nine.
But (10) says that \(w\) generates \(K(y,z)\) over \(\mathbb C(y,z)\).
On the coefficient curve over this latter base, that function would
have map degree one, whereas its pole divisor has degree at least nine.
The pole-degree equality and finite-curve inputs are the ones stated in
[coefficient lemmas191](weight-four-split-coefficient-ode-lemmas-pass191-working.md),
including [Stacks, Lemma 33.44.11](https://stacks.math.columbia.edu/tag/0AYZ).
This contradiction proves \(a=0\).

## 4. A regular differential excludes the second algebraic slope

Now \(b\ne0\), \(\mu=0\), and \(M=M_1n+M_0\).
The \(U^4\) equation from (8) is
\[
10db''+5d'b'+d''b=0.
\tag{13}
\]
The given \(q\) is a solution, because \(d=q'''/6\) and
\[
10dq''+5d'q'+d''q=\frac{(q^2)^{(5)}}{12}=0.
\tag{14}
\]
This observation alone would not exclude a second algebraic solution.
Write \(b=q\phi\), with \(\phi\in K\). Substitution in (13) gives
\[
10dq\,\phi''+(20dq'+5d'q)\phi'=0.
\tag{15}
\]
Suppose \(j:=\phi'\ne0\). Dividing (15) by \(10dqj\) and taking an
exact derivative shows \(j^2q^4d\in\mathbb C^*\).
Since \(d=s/(16q^5)\), choose \(\mu_0\in\mathbb C^*\) such that
\(\mu_0^2=j^2s/q\), and define elements of \(K\) by
\[
r=j/\mu_0,\qquad r^2=q/s,\qquad
\zeta=1/s,\qquad \zeta^2=1+4r^4,\qquad
t=\frac{1-\zeta^{-1}}2 .
\tag{16}
\]
The symbol \(\mu_0\) is unrelated to the vanishing coefficient \(\mu\)
in (9). The relation in (16) follows from
\(4q^2+s^2=1\). It makes \(r\) nonconstant, and
\(\mathbb C(r,\zeta)\subset K\) is a finite subextension over
\(\mathbb C(t)\). No auxiliary element has to be adjoined.

In the algebraic function field (16), differentiation gives
\[
dt=\frac{4r^3}{\zeta^3}\,dr,\qquad
d\phi=\frac{4\mu_0 r^4}{\zeta^3}\,dr
 =\frac{\mu_0}{2}
   \left(\frac{dr}{\zeta}-d\left(\frac r\zeta\right)\right).
\tag{17}
\]
Here \(d\phi,dt,dr\) denote differentials; the coefficient \(d\)
from (3) is not being differentiated as an operator. Thus
\[
d\left(\frac{2\phi}{\mu_0}+\frac r\zeta\right)=\frac{dr}{\zeta}.
\tag{18}
\]

The differential on the right is nonzero and regular on the smooth
projective curve with function field \(\mathbb C(r,\zeta)\).
This can be checked without a genus calculation:

- At a finite point with \(\zeta\ne0\), the formula \(dr/\zeta\)
  is regular.
- At a finite zero of \(\zeta\), the equation
  \(\zeta^2=1+4r^4\) has a simple root in \(r\), with \(r\ne0\);
  \(dr/\zeta=d\zeta/(8r^3)\) is regular.
- At infinity use \(x=1/r\), \(z_\infty=\zeta/r^2\).
  Then \(z_\infty^2=x^4+4\), with \(z_\infty=\pm2\) at the
  two points at infinity, and \(dr/\zeta=-dx/z_\infty\) is regular.

It is nonzero because \(r\) is transcendental and the characteristic is
zero. Its pullback to the smooth projective curve of \(K\) is still
regular and nonzero: at a point of ramification index \(e\), a regular
differential of order \(m\ge0\) pulls back with order \(em+e-1\ge0\).
All finite extensions here are separable.

A rational function on a smooth projective curve cannot have a
nonzero regular differential as its exact derivative. Indeed, a pole
of order \(h>0\) makes its derivative have a pole of order \(h+1\)
in characteristic zero. If it has no poles, the function is constant.
Applying this to the left side of (18) gives a contradiction.
Therefore \(j=0\), and the exact constant field of \(K\) gives
\[
b=\lambda q,\qquad \lambda\in\mathbb C^*,\qquad
W_0=\frac{\lambda}{2}n^2+D n+g_0,\qquad D,g_0\in K.
\tag{19}
\]
The coefficient of \(n^2\) follows from
\(b'''/(12d)=\lambda/2\).
The regular-differential obstruction applies on every finite
coefficient extension, not just on the displayed quartic curve.

## 5. Residual pencil forces complex coefficients

For completeness, the remaining coefficients in (7) are
\[
\begin{gathered}
\mathcal W_4=-b'd-bd'/4,\qquad
\mathcal W_3=-b'h-bh'/3-dM_1,\\
\mathcal W_2=b''n/2+c''/2-hM_1,\qquad
\mathcal W_1=M_1'n+M_0',\\
D=\frac{c'''}{6d}-\frac{h'M_1}{3d}-\frac{hM_1'}d .
\end{gathered}
\tag{20}
\]
Using (19), the \(U^3,U\) equations give
\[
\begin{gathered}
\mathcal W_3'=3dM_1'+hb'',\qquad
M_1''=\lambda k'',\qquad M_0''=2hD,\\
M_1=\lambda k+\alpha t+\beta,\quad \alpha,\beta\in\mathbb C,
\qquad \delta\mathcal W=D'n+g_0'\ne0.
\end{gathered}
\tag{21}
\]
Subtract the complex polynomial \(\lambda z^2/2\) from \(w\), then
use \(n=z-Qy^2-k'y\). The result is
\[
\begin{gathered}
\widetilde w=w-\lambda z^2/2=(\alpha y+D)z+G(y)+g_0,\\
G(U)=g_4U^4+g_3U^3+g_2U^2+g_1U,\\
g_4=\mathcal W_4-\lambda Q^2/2
    =-\frac{\lambda}{48}(q^2)^{(4)}=0,\\
g_3=\mathcal W_3-\lambda Qk'-\alpha Q,\\
g_2=c''/2-hM_1-\lambda(k')^2/2-DQ-\alpha k',
\qquad g_1=M_0'-Dk',\\
g_3'=0,\qquad g_2'=-QD',\qquad g_1'=-k'D'.
\end{gathered}
\tag{22}
\]
The \(g_4\) identity is valid for general \(q\) before using the
quadratic polynomial \(q^2=t(1-t)\). It follows by expanding
\((q^2)^{(4)}=2qq^{(4)}+8q'q'''+6(q'')^2\).
The last row follows from (20)--(21), \(Q'=3d\), and \(k''=2h\).

If \(D\notin\mathbb C\), apply the exact linear-pencil lemma in
Section 3 of
[field normal form190](weight-four-absent-zero-r-field-normal-form-pass190-working.md)
to the field equality (10) over \(\mathbb C(y)\), with independent
parameter \(z\). Removing the complex polynomials
\(\lambda z^2/2+\alpha yz\) does not change that field.
The lemma gives \(G(y)+g_0\in\mathbb C(y)+\mathbb C(y)D\).
Clearing denominators in \(\mathbb C[y]\) and comparing a complex
basis of the finite coefficient span shows
\(g_2=u_0+u_1D\), with \(u_0,u_1\in\mathbb C\).
Since \(D'\ne0\), its derivative and (22) force \(u_1=-Q\),
contrary to \(Q'=3d\ne0\).
We have proved
\[
D\in\mathbb C,\qquad G\in\mathbb C[U],\qquad
g_0'\ne0,\qquad K=\mathbb C(g_0).
\tag{23}
\]
The nonvanishing is the scalar equation (21). The last assertion
follows from (10) and the projected polynomial inverse in (22), by
intersecting with \(K\). Up to this point, this is only a
coefficient-field and projected-coordinate conclusion.

## 6. Actual transport, polynomial inverse, and recognition

The original chart entries, now in \(K[n,y,X]\), are
\[
\begin{gathered}
Z=n+Qy^2+k'y+(q'y+k)X+qX^2,\\
W=\mathcal W(y)+P(y)X+(\lambda qn+c)X^2,\\
P(y)=(\lambda q'n+c')y-\lambda qF(y)
       +(\lambda k+\alpha t+\beta)n+M_0 .
\end{gathered}
\tag{24}
\]
The coefficient of \(n^2\) in \(W\) is \(\lambda/2\), and that
of \(n\) in \(Z\) is one. Consequently subtraction gives
\[
[n]\{W-\lambda Z^2/2\}
 =\alpha y+D+(\alpha t+\beta)X
 =\alpha Y+\beta X+D=:A_0(X,Y)\in\mathbb C[X,Y].
\tag{25}
\]
The two extra contributions vanish by
\(b-\lambda q=0\) and \(b'-\lambda q'=0\).
Thus \(I_*:=W-\lambda Z^2/2-A_0Z\) belongs to \(B\cap K[X,y]\),
with \(I_*|_{X=0}=G(y)+g_0\).

On the coefficient chart set
\(\mathscr T=\nabla-X\partial_y-F_U(y)\partial_n\).
Using \(Q'=3d\), \(k''=2h\), and \(q''=2Q\), direct differentiation
gives \(\mathscr T(X)=\mathscr T(Y)=\mathscr T(Z)=0\).
Also \(\delta\rho=P_U\) and \(\mathcal W_U=\delta P\), so
\[
\mathscr T W
 =\delta\mathcal W+
 X(\delta P-\mathcal W_U)+X^2(\delta\rho-P_U)=g_0'.
\tag{26}
\]
The complex polynomial \(A_0(X,Y)\) is killed too.
Hence \(\mathcal Q:=I_*-g_0\in K[X,y]\) satisfies
\((\nabla-X\partial_y)\mathcal Q=0\).
Substitution \(y=Y-tX\) turns this into coefficient differentiation
at fixed \(X,Y\). The exact constant field gives
\(Q_0(X,Y):=\mathcal Q(X,Y-tX)\in\mathbb C[X,Y]\).
This proves the actual invariant-coordinate formula and inverse
\[
\begin{aligned}
I&=W-\frac{\lambda}{2}Z^2
       -(\alpha Y+\beta X+D)Z-Q_0(X,Y)=g_0,\\
W&=I+\frac{\lambda}{2}Z^2
       +(\alpha Y+\beta X+D)Z+Q_0(X,Y).
\end{aligned}
\tag{27}
\]
Both maps fix \(X,Y,Z\). Each composition cancels precisely the same
three complex-coefficient polynomials, so both inverse orders hold
in the original ring, without inverting a speed or a coordinate.
Since \(g_0\in K\subset\operatorname{Frac}\mathcal A\) and \(I\in B\),
we have \(EI=0\).

The global slice makes \(\mathcal A\simeq B/(u)\) regular:
\(Eu=1\) puts one in the ideal of original partial derivatives of \(u\).
Now \(E\) is a nonzero \(\mathbb C[I]\)-linear LND of the polynomial
three-ring \(B=\mathbb C[I][X,Y,Z]\).
The exact regular-kernel statement of
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore gives
\[
\mathcal A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.
\tag{28}
\]

## Scope and dependencies

This note closes only the zero-R branch for the supplied actual
two-root full initial kernel in (1). The nonzero-R square alternatives,
other positive bad-quadratic ranks, higher profiles, arbitrary entry,
and unrestricted cancellation are not concluded here.
The coefficient-curve argument is not a claim that \(q,r,\zeta\)
are polynomial coordinates. The actual polynomial coordinate is (27).

The retained general zero-R reduction, actual field return, linear
pencil lemma, and published Wang/BGL endpoints are explicit inputs.
The new second-cover steps are the simple-zero pole bound (12), the
algebraic-slope uniqueness argument (15)--(19), and verification that
the original polynomial shear survives via (22) and (25).
No checker was authored, executed, imported, or compiled for this note,
and no195 or earlier source was edited. This is a bounded working
proof, not human expert review, proof-assistant certification, historical
novelty clearance, public submission, or a solution of the unrestricted
objective.
