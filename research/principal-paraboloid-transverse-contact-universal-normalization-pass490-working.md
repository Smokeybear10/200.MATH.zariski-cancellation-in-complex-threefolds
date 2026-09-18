# Transverse contact: high scalar gates and actual universal normalization

Working necessary reduction: retain the full actual square-root
family of489. Its complete literal scalar forces \(h_0=0\),
and hence \(c_1\ne0\). Licensed actual complex polynomial maps
then give the universal coefficient family
\[
\boxed{\quad
s=r^2/2,\qquad k=tr,\qquad
\lambda=w/2,\quad \omega=w^2/2,\quad \mu=-rw.
\quad}
\tag{1}
\]
The existing coefficient elements r and w are not promoted to
ambient coordinates. Their remaining condition
\(\mathcal Dw=w_t-w w_r\ne0\) is retained. This note proves
the high scalar reduction and actual normalization only; it does
not exclude or realize the remaining normalized family.

## 1. Retained actual input and a licensed coefficient basis

Retain every actual264, genuine296 and birational projected-line325
hypothesis carried by474 and the fully read
[489](principal-paraboloid-transverse-contact-square-root-reduction-pass489-working.md).
In particular the original polynomial four-ring, global slice
with \(X=a_0u_{\rm glob}+x_0\), full initial kernel, selected
literal partial, both returns and nonzero original scalar remain
required. Write \(P=\sigma\), \(NP=\rho\in L^*\),
\(O=L[P]\), and \(y=\lambda P+r_{\rm old}\),
\(\theta=\mu P+h_{\rm int}\).

Use489's already normalized actual frame. To distinguish its
complex constants from the coupling k, write
\(h=h_0,\ \kappa=c_1,\ d=c_0,\ \ell=\lambda_0\).
Before imposing any new scalar gate,
\[
\begin{gathered}
s=r^2/2,\quad \omega=w^2/2,\quad \mu=-rw,\qquad
\lambda=hw^2/4+\kappa w/2+\ell,\\
k=-hr^2/2+(\kappa t+d)r-2\ell t^2+Ct+E,\\
h,\kappa,d,\ell,C,E\in\mathbb C,\qquad
(h,\kappa)\ne(0,0),\quad(\kappa,d)\ne(0,0).
\end{gathered}
\tag{2}
\]
The exact coefficient basis \((t,r)\) satisfies
\[
[L:\mathbb C(t,r)]<\infty,\qquad
\partial_s=r^{-1}\partial_r|_t,\qquad
\mathcal D=\partial_t|_r-w\partial_r|_t,\qquad
r,w,\mathcal Dw\ne0.
\tag{3}
\]
Here t derivatives in \((t,r)\) also equal the original fixed-s
t derivative, since \(s=r^2/2\). The variable coupling and
nonzero beta remain hypotheses, with
\(\beta=(\kappa r+(\kappa t+d)w)/r^2\ne0\).

Put
\[
v=r+tw=\tau w.
\tag{4}
\]
The original contact parameter tau is noncomplex, so v is nonzero.
More importantly,
\[
\det\frac{\partial(w,v)}{\partial(t,r)}
                         =w_t-w w_r=\mathcal Dw\ne0.
\tag{5}
\]
Thus \((w,v)\) is a separating coefficient basis. Its commuting
extended partials define exact finite fields
\[
F_w=\ker_L\partial_v,\qquad F_v=\ker_L\partial_w,
\qquad [F_w:\mathbb C(w)]<\infty,\quad [F_v:\mathbb C(v)]<\infty.
\tag{6}
\]
For example, differentiating a constant's monic minimal polynomial
over \(\mathbb C(w,v)\) forces its coefficients into the corresponding
one-variable rational field. Finite constant subextensions have
uniformly bounded degree, and hence their union is finite. The
other derivative on each field has constants exactly C. Neither
field, nor L, is asserted to be rational. Also w is transcendental
over \(F_v\), and v over \(F_w\), by separability and their
nonzero coordinate derivatives.

## 2. The entire literal centered matrix

At fixed formal X set
\[
\xi=P+t(X-\lambda),\qquad R=r_{\rm old}+\lambda^2t,\qquad
A=(hw+\kappa)v-dw+C,\quad \phi=-hv^2/2+dv+E.
\tag{7}
\]
Expanding (2) after \(r=v-tw\) gives
\(k=-2\lambda t^2+At+\phi\). Direct differentiation in (3)
also gives \(\mathcal Dk=A-4\lambda t\); no claim that A or
lambda is killed by \(\mathcal D\) is needed. The literal rows
are exactly
\[
\begin{aligned}
Y&=(X+\lambda)\xi+R,\\
Z&=\xi^2+A\xi+G+\phi X,\\
W&=\tfrac12w^2\xi^2+(b-wvX)\xi+c+HX+\tfrac12v^2X^2.
\end{aligned}
\tag{8}
\]
The lower coefficients in (8) are existing elements of L. To
record the full original-to-centered transport, if
\(w_{\rm int}=\omega P^2+w_1P+w_0^{\rm int}\), then
\[
\begin{aligned}
G&=2tr_{\rm old}+mh_{\rm int}+n+\lambda tA-\lambda^2t^2,\\
b&=w_1+2\omega\lambda t,\qquad
c=w_0^{\rm int}+\lambda t w_1+\omega\lambda^2t^2,\\
H&=h_{\rm int}-tw_1-wv\lambda t.
\end{aligned}
\tag{9}
\]
In particular the \(v^2X^2/2\) term is retained throughout.

Let \(J=J_{w,v,\xi}\). Since the shift from P to xi has
Jacobian one, its correct calibration is
\[
J=-\frac{r a_0^4}{\rho\mathcal Dw}\in L^*.
\tag{10}
\]
The factor r is in the numerator: \(J_{t,r,P}=rJ_{t,s,P}\),
and (5) then divides by \(\mathcal Dw\). This scalar can
depend on w,v. Only coefficients of positive X or xi powers
are set to zero below.

The determinant used is the FULL derivative matrix of (8):
\[
\begin{pmatrix}
\lambda_w\xi+R_w&R_v&X+\lambda\\
(hv-d)\xi+G_w&(hw+\kappa)\xi+G_v+(d-hv)X&2\xi+A\\
w\xi^2+(b_w-vX)\xi+c_w+H_wX&
(b_v-wX)\xi+c_v+H_vX+vX^2&w^2\xi+b-wvX
\end{pmatrix}.
\tag{11}
\]
Here \(\lambda_w=(hw+\kappa)/2\). All lower coefficients
and their derivatives remain arbitrary until forced otherwise.

## 3. Two scalar coefficients force h to vanish

The xi-cubed coefficient of (11) integrates exactly to
\[
R=\frac{hw+\kappa}{2w}b
       -\frac{(hw+\kappa)(hw^2-4\ell)}8v+Q,
\qquad Q\in F_w.
\tag{12}
\]
This requires only \(w\ne0\). The X-cubed coefficient is
\(vG_w-(d-hv)H_w\). Put \(L_0=H/v\), using \(v\ne0\).
Its vanishing then gives
\[
H=vL_0,\qquad G=(d-hv)L_0+g,\qquad g\in F_v.
\tag{13}
\]
No nonzero assumption on \(L_0\) or either of its derivatives
has been made.

Introduce only coefficient-field expressions
\[
\begin{gathered}
F_0=L_0+b/w,\qquad T=(dw+\kappa v)F_0,\\
D_0=\frac C2(hw+\kappa)+2Q_w\in F_w,\qquad
N_0=\frac34h^2w^2-h\ell-\frac12\kappa^2.
\end{gathered}
\tag{14}
\]
The factor \(dw+\kappa v\) is nonzero by (2) and the
separating basis, including when either d or kappa is zero.
After only (12),(13), the exact raw coefficients of the full
matrix (11) are
\[
\begin{aligned}
[X^2\xi]J&=-T_w+vg_v-vD_0+v^2N_0,\\
[X\xi^2]J&=-T_v+wD_0-wg_v-vwN_0.
\end{aligned}
\tag{15}
\]
These are individual coefficients, not approximate top-degree
relations or combinations with an omitted scalar term.

Set them to zero and commute the partials on T. The result is
\[
2g_v+vg_{vv}-2D_0-w(D_0)_w+v\{3N_0+w(N_0)_w\}=0.
\tag{16}
\]
Since g is killed by \(\partial_w\) and \(D_0\) by
\(\partial_v\), differentiating (16) first in v and then w
leaves exactly
\[
4(N_0)_w+w(N_0)_{ww}=\frac{15}{2}h^2w=0.
\tag{17}
\]
Therefore
\[
h=0,\qquad \kappa\ne0.
\tag{18}
\]
The second assertion uses the retained nonzero pair \((h,\kappa)\).
No division by d, h, g or Q occurred.

## 4. Exact integration of the remaining high scalar equations

Now \(N_0=-\kappa^2/2\). Equation (16) separates as
\[
vg_{vv}+2g_v-\frac32\kappa^2v
                       =2D_0+w(D_0)_w=\alpha\in\mathbb C.
\tag{19}
\]
Indeed the left expression is in \(F_v\), the right in \(F_w\),
and their equality is killed by both coordinate partials. Exact
subtraction gives complex constants
\(A_-,B_-,T_0,Q_0,g_0\), all permitted to vanish, with
\[
\begin{aligned}
D_0&=\frac\alpha2+\frac{A_-}{w^2},\\
Q&=\frac{\alpha-C\kappa}{4}w-\frac{A_-}{2w}+Q_0,\\
g&=\frac{\kappa^2v^2}{4}+\frac\alpha2v-\frac{B_-}{v}+g_0,\\
T&=A_-\frac vw+B_-\frac wv+T_0.
\end{aligned}
\tag{20}
\]
For example \((w^2D_0-\alpha w^2/2)_w=0\).
After subtracting the quadratic and linear terms from g,
equation (19) says that v squared times the remaining derivative
is constant. These yield the displayed inverse powers because
w and v are nonzero. The last line follows by substituting the
first three into (15); the remaining difference has both partials
zero. No rational form was assumed before these exact integrations.

The complete remaining high family at this stage is (12),(13),(20),
with
\[
L_0=\frac{T}{dw+\kappa v}-\frac bw,\qquad
R=\frac{\kappa b}{2w}+\frac{\kappa\ell}{2}v+Q.
\tag{21}
\]
The lower functions b,c and their unresolved scalar coefficients
are still required. No denominator in (21) is an ambient unit
assertion; it is only a nonzero element of the coefficient field.

## 5. A complete actual normalization with its inverse

After (18), the actual coupling in (2) is
\((\kappa t+d)r-2\ell t^2+Ct+E\). Since \(\kappa\ne0\), put
\[
a=d/\kappa,\qquad
\widehat C=C+4\ell a,\qquad
\widehat E=E-Ca-2\ell a^2.
\tag{22}
\]
All are complex constants. The following ACTUAL composite map is
polynomial:
\[
\begin{aligned}
X_*&=X+\ell,\\
Y_*&=Y+aX^2+\tfrac12\widehat C(X+\ell),\\
Z_*&=Z+2aY+a^2X^2-\widehat E(X+\ell),\\
W_*&=\kappa^2W.
\end{aligned}
\tag{23}
\]
Its sequential polynomial inverse, with \(x=X_*-\ell\), is
\[
\begin{aligned}
X&=x,\qquad Y=Y_*-\widehat C X_*/2-a x^2,\\
Z&=Z_*+\widehat E X_*-2aY-a^2x^2,\qquad W=W_*/\kappa^2.
\end{aligned}
\tag{24}
\]
Only the proved nonzero complex constant kappa is divided out.
For comparison with the fully read
[426](general-coupling-normalization-obstruction-pass426-working.md),
(23) is the sequence: the actual time shift
\(Y_1=Y+aX^2,Z_1=Z+2aY+a^2X^2\); the actual translation
\(X_2=X+\ell\); the linear additions
\(Y_3=Y_1+\widehat C X_2/2,Z_3=Z_1-\widehat E X_2\);
and the scaling \(W_*=\kappa^2W\).

Each stage is in426's licensed filtered class. The full leading
relation remains the entire initial kernel, with all exact time
degrees unchanged. Here also \(\partial_{Z_*}=\partial_Z\),
\(N_*=N\), and \(a_{0,*}=a_0\). Both original-ring returns
are obtained in the new actual coordinate frame through426's
localized quotient argument, not from a coefficient-field
parametrization. The literal parameter transports are
\[
\begin{gathered}
t_*=t+a,\quad s_*=\kappa^2s,\quad
P_*=P-2\ell t_*+\widehat C/2,\quad NP_*=\rho,\\
r_*=\kappa r,\quad w_*=\kappa w,\qquad
\lambda_* =\lambda-\ell=w_*/2,\\
\omega_* =\kappa^2\omega=w_*^2/2,\qquad
\mu_* =\kappa^2\mu=-r_*w_*,\qquad k_*=t_*r_*.
\end{gathered}
\tag{25}
\]
For the last identity, after the time shift the coupling is
\(\kappa t_*r-2\ell t_*^2+\widehat C t_*+\widehat E\).
The X translation adds \(2\ell t_*^2\), and the linear additions
subtract \(\widehat C t_*+\widehat E\). Scaling W then identifies
\(\kappa r=r_*\). Thus no coefficient-valued ambient change is
hidden in (25).

The original bad-coordinate row Jacobian of (23) is \(\kappa^2\),
and the coefficient-parameter Jacobian is the same. Consequently
the new actual scalar is still \(-a_0^4/\rho\).
The actual directional derivation is unchanged, while
\(\mathcal D_*w_*=\kappa\mathcal Dw\ne0\). Also
\[
v_*=r_*+t_*w_*=\kappa(v+aw),\qquad
\xi_* =\xi+a(X-\lambda)+\widehat C/2.
\tag{26}
\]
These last expressions are coefficient and intrinsic transports,
not additional ambient automorphisms. Their Jacobians agree with
the preserved calibration.

## 6. The normalized frontier and what has not been proved

Drop stars in the actual frame (25). Equations (1) hold, and the
centered rows (8) have the normalized constants
\[
h=d=\ell=C=E=0,\qquad \kappa=1,\qquad A=v,\quad\phi=0.
\tag{27}
\]
Sections2--4 can be repeated in this new actual frame. They give
new complex integration constants in (20); those constants are
not silently identified with their old-frame values. The still
moving lower coefficients must satisfy the complete remaining
determinant of (11), with calibration
\(-r a_0^4/(\rho\mathcal Dw)\ne0\).

This source does not set that determinant's constant coefficient
to zero, assume it is independent of the coefficient parameters,
or claim that the normalized family is impossible. It also does
not construct the lower genuine levels or establish an actual
realization. The bounded conclusion is precisely the forced
high-scalar gate (18), its exact integrations and the actual
universal normalization (23)--(27).

The complete489,474 and426 sources were read. Fresh unsaved950b22
reconstructs the full matrix coefficients. Fresh734bb5 verifies the
two raw identities (15), including the previously forced X-cubed
and xi-cubed zero coefficients. A preliminary diagnostic112645
omitted the \(v^2X^2/2\) term and is not used; all claimed identities
use the complete rows (8). Fresh0b71c6 verifies the full high
integrations (20), both orders of the actual inverse, the coupling
normalization and row Jacobian. The written proof supplies the
exact-field, separating, nonzero-factor and actual-transport gates.
No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited while authoring this note.

