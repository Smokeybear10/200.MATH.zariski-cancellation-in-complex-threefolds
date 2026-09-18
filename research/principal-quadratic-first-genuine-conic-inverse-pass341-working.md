# An actual polynomial inverse for the genuine quadratic-plane branch

Under the full actual principal-chart hypotheses264, suppose k=s and
n=g t^2 with g a nonzero complex constant. In the flattened quadratic
plane of333, the branch b nonzero with a nonzero residual linear
coefficient rho is recognized. When kappa is nonzero, the proof gives
explicit polynomial generators of the original invariant ring. When
kappa is zero, an actual cubic shear enters the retained1122 theorem.

These are conditional working results. This note does not prove entry
into the supplied chart or normalize arbitrary k,n. It does not assume
that coefficient-field parameters are original polynomial coordinates.

## 1. Retained actual hypotheses and the selected quadratic equation

Retain all hypotheses and returns of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), as used in
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\\
L=\operatorname{Frac}\ker_{A_0}N,\quad K=\operatorname{Frac}A_0=L(v),
\quad Nv=1,\quad [L:\mathbb C(t,s)]<\infty,\\
K=\mathbb C(y,z,w),\quad L[y,\sigma,\theta]=L[v],\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
In particular the initial ideal is the entire kernel, N is the selected
leading part of the literal Z-partial, and all intercepts and coefficient
functions belong to K and are killed by E. No arbitrary formal map is
substituted for this actual input.

Assume k=s, n=g t^2, g in C*, and ell_s nonzero, ell_ss=0.
By333, with r=ell, the exact coefficient field has
\[
\begin{gathered}
s=cr+d(t),\qquad \mathcal L=b(t)r+e(t),\qquad c\in\mathbb C^*,\\
b,d,e\in\mathbb F:=\ker_L\partial_r,\qquad
[\mathbb F:\mathbb C(t)]<\infty,\qquad
\ker_{\mathbb F}\partial_t=\mathbb C,\\
g b^2-\frac{d''}{2}b-(1+gc)^2=0.
\end{gathered}
\tag{2}
\]
The derivations here use independent coefficient parameters t,r.
The finite field F is not presumed rational. In this note b is nonzero.
Put
\[
\kappa=1+gc,\quad h=\kappa/b,\quad j=d',\quad
U=x-h\sigma,\quad x=y+gt,\quad
\rho=hj-b'r-e'.
\tag{3}
\]
The complete plane level from333 is
\[
-bU^2+jU+\rho\sigma=q,\qquad q\in L,
\qquad j'=2gb-2\kappa^2/b.
\tag{4}
\]
We first assume rho nonzero. Solving gives
\[
P:=\sigma=\frac{q+bU^2-jU}{\rho},\qquad x=U+hP,
\qquad L[x,\sigma]=L[U]=L[v].
\tag{5}
\]
Thus U is affine in v, with U_v in L*. The full determinant in the
parameters t,r,U is a nonzero element of L independent of both X and U:
\[
J=\det\frac{\partial(Y,Z,W)}{\partial(t,r,U)}
   =-a_0^4c/U_v\in L^*.
\tag{6}
\]
This follows from the actual calibration in(1), not from a formal
constant-Jacobian assumption on unrelated polynomials.

## 2. Scalar rigidity forces b to be complex

The full map, with all intrinsic expressions retained, is
\[
\begin{aligned}
\theta&=c(x^2+gP^2)+jP-br-e,&s&=cr+d,\\
y&=x-gt,&z&=P^2+\theta+2tx-gt^2,&w&=r-2Px,\\
Y&=y+PX+tX^2,\\
Z&=z+(2tP+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{7}
\]
At X=0 perform determinant-preserving row operations. Starting with
(dy,dz,dw), set A=dy, C=dw+2Pdy, and
B=dz-(2t+2cx)dy+bC. Their exact forms are
\[
\mathsf A=dx-g\,dt,\quad
\mathsf B=(j-2bU)dP+(2\kappa U+\rho-hj)dt,\quad
\mathsf C=dr-2x\,dP-2gP\,dt.
\tag{8}
\]
Write delta=j-2bU and C0=2kappa U+rho-hj only in this paragraph.
The determinant of these three rows is
\[
J=C_0-2C_0P_rx+C_0P_Uh+2gPP_r\delta
   -PP_U\delta h'+P_t\delta+P_U\delta g,
\tag{9}
\]
where
\[
P_U=(2bU-j)/\rho,\quad
P_r=q_r/\rho+Pb'/\rho,\quad
P_t=(q_t+b'U^2-j'U)/\rho-P\rho_t/\rho,
\quad h'=-\kappa b'/b^2.
\tag{10}
\]
Here rho_r=-b'. Exact expansion gives
\[
[U^5](\rho^3b^2J)=-4b^3b'(b^2g+\kappa^2).
\tag{11}
\]
Because J is independent of U, this vanishes. If b' were nonzero,
then b^2g+kappa^2=0; differentiating would give 2gbb'=0, a
contradiction. Consequently b'=0 and b is a nonzero complex constant.
This proof also covers kappa=0.

## 3. The nonzero-kappa branch has complex polynomial coefficients

Suppose kappa nonzero. Since b is now constant, rho=hj-e' lies in F.
After b'=0, the next coefficients of(9) are
\[
[U^3](\rho^2J)=2\{b^2\rho_t-2(b^2g+\kappa^2)q_r\}.
\tag{12}
\]
After this cubic coefficient is set to zero, the quadratic coefficient
is -6 rho kappa q_r. Hence q_r=0 and rho_t=0. Thus q belongs to F,
rho is a nonzero complex constant, and h is a complex constant.
The linear coefficient then gives
\[
q'=(g-h^2)j+2\rho h.
\tag{13}
\]
Exact constants of F, not an assumed rational parametrization, give
\[
\begin{aligned}
\lambda&=g-h^2,\\
d&=b\lambda t^2+j_0t+d_0,\\
e&=hd-\rho t+e_0,\\
q&=\lambda d+2\rho ht+q_0,
\qquad j_0,d_0,e_0,q_0\in\mathbb C.
\end{aligned}
\tag{14}
\]
The constant coefficient of(9) becomes J=rho. Neither lambda nor
g+h^2 is divided out. In particular both resonances are included.

## 4. Explicit inverse in the original polynomial ring

Initially as elements of K define
\[
V=U-\lambda t-j_0/(2b),\qquad
C=\lambda d_0+q_0-j_0^2/(4b),\qquad L_X=X+h.
\tag{15}
\]
The intrinsic formulas simplify exactly to
\[
P=(b/\rho)V^2+2ht+C/\rho,\quad
x=V+\lambda t+j_0/(2b)+hP.
\tag{16}
\]
All coefficients in(14)--(16) are complex. Set
\[
F=L_Xt+(b/\rho)V^2+C/\rho,\quad
\widehat Y=Y-j_0/(2b)=V+L_XF,\quad
N_0=t-(b/\rho)(2VF+L_XF^2).
\tag{17}
\]
The two-variable map (V,t) to (Yhat,N0) is a polynomial
automorphism over C[X]. Its full inverse is
\[
F=L_XN_0+(b/\rho)\widehat Y^2+C/\rho,\quad
V=\widehat Y-L_XF,\quad
t=N_0+(b/\rho)(2\widehat YF-L_XF^2).
\tag{18}
\]
Substitution proves both orders; no division by L_X occurs.

To recover N0 using only original coordinates, make the actual linear
change over C[X]
\[
S=W-XZ,\qquad \widetilde Z=Z-(cX-b)S.
\tag{19}
\]
Its inverse is Z=Ztilde+(cX-b)S and W=S+XZ, so its determinant
is a complex unit. Direct substitution into the full map(7) gives
\[
\begin{aligned}
S&=r-2x(P+tX)-X(P+tX)^2+gt^2X,\\
\widetilde Z&=\rho N_0+cY^2+d_0(X-h)-e_0.
\end{aligned}
\tag{20}
\]
In particular the complete original-ring inverse is obtained in order:

1. Compute S,Ztilde by(19), and
   N0=(Ztilde-cY^2-d0(X-h)+e0)/rho.
2. Compute Yhat and then F,V,t by(18).
3. Compute P,x by(16), and
   r=S+2x(P+tX)+X(P+tX)^2-gt^2X.

Only the nonzero complex constants b and rho are inverted. Every
computed expression belongs to B. Conversely(7),(14),(16) express all
original coordinates polynomially in X,t,r,V. Therefore
\[
\boxed{B=\mathbb C[X,t,r,V],\qquad A_0=\mathbb C[t,r,V].}
\tag{21}
\]
Indeed t,r are algebraically independent, V is affine nonconstant in
the independent intrinsic variable v, and X is transcendental over K.
They are thus four polynomial coordinates, not merely generators with
unknown relations. E fixes t,r,V and sends X to the nonzero invariant
a0. On this polynomial ring its kernel is exactly C[t,r,V].
This is an explicit inverse argument, not an invocation of the
Jacobian conjecture or a promotion of generic coordinates by fiat.

## 5. The zero-kappa branch: an actual lower-degree frame

Suppose kappa=0. For the rho nonzero branch, Section2 already gives
b in C*. The same conclusion also holds in the separate rho=0
branch: differentiating rho=hj-b'r-e'=0 in r gives b'=0.
Now c=-1/g, h=0, and(2) integrates to
\[
d=d_2t^2+d_1t+d_0,\qquad d_2=gb\in\mathbb C^*,
\qquad d_1,d_0\in\mathbb C.
\tag{22}
\]
Use the actual coordinates supplied by
[332](principal-paraboloid-quadratic-affine-first-potential-transfer-pass332-working.md):
\[
T=Y^2+XW-X^2Z+gZ,\qquad S_1=XZ-W,
\quad Z=(T-Y^2+XS_1)/g,\quad W=XZ-S_1.
\tag{23}
\]
They satisfy E^2T=0, with its X-linear coefficient
ell+gs=r+g(cr+d)=gd. The X-cubic coefficient of S1 is t^2.
The actual shear
\[
S_2=S_1-\frac{X^2T}{gd_2}
              +\frac{d_1}{d_2}XY+\frac{d_0}{d_2}X^3
\tag{24}
\]
has a polynomial inverse fixing X,T,Y. Its cubic coefficient is
t^2-d/d2+(d1/d2)t+d0/d2=0. Thus
\[
\deg_E(X,T,Y,S_2)=(1,1,2,\text{at most }2).
\tag{25}
\]
The second degree is exactly one because d2 is nonzero and t is
transcendental. If the last degree is two, the retained actual-frame
working theorem[257](full-exact1122-recognition-synthesis-pass257-working.md)
applies. If it is at most one, the retained
[156](three-good-all-degree-recognition-pass156-working.md) applies.
Both give A0=C^[3], with all their stated working proof dependencies.
No height or selected-shift hypothesis is silently added to257.

## 6. Scope and verification boundary

The genuine conic rho nonzero is now recognized for every kappa,
under(1)--(4). The additional rho=0,kappa=0 line case is also
recognized by Section5. The rho=0,kappa nonzero case is not proved
here. The b=0 case belongs to339, not to a division by b in this note.
The ell_ss nonzero case belongs to340, and ell_s=0 to337.

The nonzero-kappa conclusion(21) uses the supplied actual chart and
333's plane reduction but no earlier kernel-recognition endpoint.
Section5 expressly depends on156/257 and does not recursively
recertify their full proof chains. The complete264,333,332,156,257
sources were read for the hypotheses used here.

Fresh unsaved exact computations reconstruct(8)--(13), the full-X
Jacobian after(14), and(17)--(20), with every displayed constant
retained. Separate saved-source review and any finite test execution
are recorded in the ledger. These are not a human expert review,
proof-assistant certificate, novelty clearance, or a solution of
unrestricted complex-threefold cancellation.
