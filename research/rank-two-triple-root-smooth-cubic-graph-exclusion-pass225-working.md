# A triple-root quartic cannot have a smooth projected cubic graph

Status: bounded working exclusion for the remaining supplied actual
triple-root quartic charts. In either selected pair direction, an affine
transverse projection makes the cubic return squarefree. All its roots
would then be critical points of a cubic first projection, which is
impossible. No coefficient-field coordinate is lifted to the original
polynomial ring.

The proof also identifies the exact projected normal-form distinction:
after the retained geometric injectivity theorem, a cubic projection is
either an affine transverse graph or an ordinary cusp over the exact
coefficient field. This note excludes the former only. It supplies no
cusp exclusion, arbitrary-entry theorem or unrestricted cancellation
claim.

## 1. Supplied actual inputs and the cubic root gate

Assume an actual globally sliced frame with the entire initial kernel
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
a=EX,\ b=EY,\ e_0=E^2Z/2,\ h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)),\\
F_4=c\,l^3m,\qquad c\in\mathbb C^*,\quad
l,m\text{ independent complex linear forms}.
\end{gathered}
\tag{1}
\]
The symbols X,Y,Z,W are actual polynomial coordinates and T is
independent. Use the literal selected Z pivot and universal184 chart,
with its exact finite coefficient field and selected parameter:
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=F_4(1,t)/\rho,
\quad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\quad L[y,z,w]=L[v].
\end{gathered}
\tag{2}
\]
The ratios t,rho are algebraically independent. All coefficient
partials are the exact extensions on L; N fixes L. No rationality of
L or original-ring unit speed is assumed.

The complete
[cubic frontier223](rank-two-triple-root-cubic-frontier-pass223-working.md)
reduces (1), if realizable, to a selected projected cubic. Its leading
pair factor has multiplicity exactly three. The universal cofactor222
and saturated-cubic224 conclusions are
\[
\begin{gathered}
\mathcal C=L[y,\vartheta]\subset\mathcal O=L[v],\quad
\operatorname{Frac}\mathcal C=L(v),\quad R\mathcal O\subset\mathcal C,\\
\mathcal H=\Gamma Q_1,\quad
\deg\Gamma=\max(\deg_vy,\deg_v\vartheta)=3,\\
\deg_vR=3,\quad Q_1(y,\vartheta)=\gamma R^3,
\quad \gamma\in L^*,\quad \deg_vy=3,\\
R=q_{t\rho}y+q_{\rho\rho}\vartheta+k_\rho,
\qquad k\in L.
\end{gathered}
\tag{3}
\]
These are polynomial identities over L, not coordinate descent claims.
In particular C need not be normal.

For clarity, the local consequence used below is stronger than merely
having at most two normalization points over a singularity. The exact
universal gradients and calibrated determinant give
\[
\begin{gathered}
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\qquad
C_1^2+R\Lambda_\rho=-\gamma R^2\Gamma_V(y,\vartheta),\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
\left[dy\wedge(Rd\vartheta+B_1dt+C_1d\rho)\wedge dw\right]
=J_0\in L^*.
\end{gathered}
\tag{4}
\]
The last coefficient is relative to dt wedge d-rho wedge dv. Over an
algebraic closure Omega of L, evaluate these established polynomial
identities at any root r of R. The first line forces C1(r)=0. The
nonzero determinant forces B1(r) nonzero, since otherwise its middle
row vanishes. The dv coefficient of the second line then yields
\[
R(r)=0\quad\Longrightarrow\quad y_v(r)=0.
\tag{5}
\]
No derivative of a moving root is taken in this argument. The complete
proof and its field-extension details are in
[saturated cubic224](rank-two-saturated-cubic-fiber-injectivity-pass224-working.md).
That note also proves geometric injectivity of v mapping to
(y(v),vartheta(v)).

## 2. Actual root-form normalization and coefficient-field normal form

There are two selected pair types in (1): l,l and l,m. Normalize the
first by the actual constant linear change X*=l(X,Y), Y*=m(X,Y), and
the second by X*=m(X,Y), Y*=l(X,Y). In either case set Z*=Z/c and
keep W fixed. These maps have actual polynomial inverses: the good
pair uses the inverse complex two-by-two matrix and Z=cZ*.

Both good degrees remain one because t is transcendental. The full
initial ideal transforms by these polynomial automorphisms. The good
change leaves the literal Z partial unchanged, and the constant Z
rescaling multiplies it and the selected N by c. Thus L is unchanged
and the selected parameter may be rescaled by 1/c. No preservation
of the old return R or auxiliary derivation is claimed; all chart
quantities are rebuilt after the actual change.

Explicitly, for X*=alpha X+beta Y, Y*=gamma X+delta Y, put
d=alpha delta-beta gamma, l0=alpha+beta t, m0=gamma+delta t. The
invertible projected linear change is
\[
\begin{gathered}
t_*=m_0/l_0,\quad \rho_*=\rho/l_0^2,\quad
y_*=d y/l_0,\quad
\vartheta_*=\vartheta/l_0-2\rho\beta y/l_0^2,\\
y_*-(t_*/\rho_*)\vartheta_*
=-\{l_0m_0\vartheta-\rho(\beta m_0+\delta l_0)y\}/(\rho l_0).
\end{gathered}
\tag{6}
\]
It preserves the generated projected ring and its degrees up to this
invertible L-linear presentation. The pair-factor identity220 therefore
gives, after dropping stars, these precise alternatives:
\[
\begin{array}{c|c|c|c}
\text{selected pair}&F_4&q&\text{transverse projection }\xi\\ \hline
l,l&X^3Y&t/\rho&\vartheta\\
l,m&XY^3&t^3/\rho&y-(t/\rho)\vartheta
\end{array}
\qquad \deg_v\xi<3.
\tag{7}
\]
In the first row take eta=y; in the second take eta=vartheta.
In each case deg eta=3, and L[xi,eta]=C. If xi were constant, then
Frac C=L(eta) would have index three in L(v), contrary to (3).
Consequently deg xi is either one or two.

If deg xi=1, L[xi]=L[v] and eta is cubic in xi. This is the smooth
projected graph case addressed below. Neither xi nor eta is declared
to be an original polynomial coordinate.

For completeness, geometric injectivity gives an elementary exact-L
description of the other possibility. If deg xi=2, completing the
square without extracting any root gives an affine parameter x over L
and constants A,B3 in L* with
\[
\xi=Ax^2+c_0,\qquad
\eta=B_3x^3+B_2x^2+B_1x+B_0.
\tag{8}
\]
Subtract the even part from eta and scale by B3. Thus
C=L[x squared,x cubed+b x], with b=B1/B3 in L. If b is nonzero,
choose a nonzero root alpha of x squared+b over Omega. The distinct
points alpha,-alpha have equal values of both generators, contradicting
injectivity224. Hence b=0 and
\[
\mathcal C=L[x^2,x^3]\quad\text{when }\deg_v\xi=2.
\tag{9}
\]
This is the ordinary cusp, not a smooth graph: its maximal ideal
(x squared,x cubed) has a two-dimensional cotangent space although
the ring has dimension one. Thus geometric smoothness really forces
deg xi=1. No general plane-embedding theorem is used for this step.

## 3. The repeated-root graph is impossible

In the first row of (7), assume theta is affine nonconstant in v.
The actual return in (3) is exactly
\[
R=-y/\rho^2+2t\vartheta/\rho^3+k_\rho,
\qquad R_v=-y_v/\rho^2+2t\vartheta_v/\rho^3.
\tag{10}
\]
At any geometric root r of R, (5) gives y_v(r)=0. Therefore
R_v(r)=2t theta_v/rho cubed is nonzero, because t,rho and the affine
coefficient theta_v are nonzero elements of L. Every root of R is
simple. But R has degree three, so over Omega it has three distinct
roots, all zeros of y_v by (5). The latter polynomial has degree two
since y has degree three. This is impossible.

## 4. The distinct-root graph is impossible

In the second row put h=t/rho and assume xi=y-h theta is affine
nonconstant. Then theta is cubic in xi and y=h theta+xi has degree
three. Differentiating only in v, so that h is fixed, gives
\[
\begin{gathered}
R=-3h^2y+2h^3\vartheta+k_\rho
  =-3h^2\xi-h^3\vartheta+k_\rho,\\
y_v=h\vartheta_v+\xi_v,\qquad
R_v=-3h^2\xi_v-h^3\vartheta_v.
\end{gathered}
\tag{11}
\]
At a root r of R, (5) implies h theta_v(r)=-xi_v. Thus
\[
R_v(r)=-2h^2\xi_v\ne0.
\tag{12}
\]
Again R is a squarefree cubic with three distinct roots, all critical
points of the cubic y, contradicting the quadratic degree of y_v.
The calculation uses neither a complex value of h nor an ambient
interpretation of xi.

## 5. Bounded conclusion

Neither pair direction of the supplied triple-root frame can have an
affine transverse projection. By Section2 and injectivity224, the only
projected cubic possibility left by these arguments is the ordinary
cuspidal ring over L, with transverse parameter degree two. This note
does not exclude that cusp or assume that such an actual frame exists.

The conclusion is about the supplied exact1122 frame with full kernel
(1). It is not a general assertion about polynomial cubic parametrizations,
arbitrary initial ideals, minimum time profiles or cancellation.
All original-ring changes used in the proof were the explicit complex
linear root-form changes and constant bad-coordinate scaling. All other
changes were declared coefficient-field calculations only.

The complete final223 frontier and224 injectivity sources were freshly
read before use. Both return derivatives and the root-count obstruction
were reconstructed directly from the universal return. No saved checker
was executed, imported or compiled, and no earlier source, index or
verification packet was changed. These are written working proofs, not
expert review, proof-assistant certification or historical novelty claims.
