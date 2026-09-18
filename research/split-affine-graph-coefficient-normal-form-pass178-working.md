# Coefficient normal forms for a nonlinear graph in the actual split chart

**Status: working coefficient reduction, with a quadratic-graph recognition subcase.**

Under the actual split hypotheses175--177, suppose the affine first
projection \(y\) has a graph \(\vartheta=P(y)\) of degree at least two.
The literal eliminant is then a scalar multiple of this graph relation.
Actual constant translations of the good coordinates normalize
\(k_\rho=0\) and \(n_\rho=d\in\mathbb C^*\). The resulting coefficient
equations recognize the degree-two graph by an explicit polynomial
shear. For graph degrees three and four they force an exact coefficient
field return, but do not yet give an original-ring recognition.

The scalar determinant is kept with its true parameter-change factor.
A proposed rational-cube shortcut omitting that factor is not used.

## 1. Actual hypotheses and exact coefficient field

Retain the full actual split setup and conclusions of
[chart175](split-cubic-generic-chart-pass175-working.md),
[the selected-component note176](split-cubic-simple-selected-component-pass176-working.md),
and [the affine-projection conclusion177](split-quadratic-projection-exclusion-pass177-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\quad
a=EX\ne0,\quad N=[u^3](\partial_Z|_A),\\
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
t=EY/a,\quad \rho=(E^2W/2)/a^2,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
y=\gamma v+\eta,\quad \gamma\in L^*,\quad\eta\in L,\quad
\vartheta=P(y),\quad 2\le\deg P\le4 .
\end{gathered}
\tag{1}
\]
The initial ideal is the full kernel. The independent ratios make
the field extension finite separable. All coefficient derivatives
on \(L\) are the unique commuting extensions of
\(\partial_t,\partial_\rho\). Initially they extend to \(L[v]\)
fixing \(v\).

Put \(K=\ker_L\partial_\rho\). Then \(K\) is finite algebraic
over \(\mathbb C(t)\), \(\rho\) is transcendental over \(K\), and
the joint constant field of the two coefficient partials is
\(\mathbb C\). Here are the elementary field facts used.
Differentiating the monic minimal polynomial of an element killed
by \(\partial_\rho\) gives a lower-degree relation, so its
coefficients in \(\mathbb C(t,\rho)\) are killed by that derivative
and belong to \(\mathbb C(t)\). The finite extension
\(L/\mathbb C(t,\rho)\) bounds the resulting extension
\(K(\rho)/\mathbb C(t,\rho)\), so \(K/\mathbb C(t)\) is finite.
An element algebraic over \(K\) is killed by \(\partial_\rho\);
this proves that \(\rho\), whose derivative is one, is transcendental.
Applying the same minimal-polynomial argument to both derivatives
makes a joint constant algebraic over \(\mathbb C\), hence complex.
No rationality of \(K\) is assumed.

In formal variables \(U,V\), write
\[
\begin{gathered}
r=k_\rho,\quad
f=H_2(k;U,V)+H_1(n;U,V),\quad
g_3=H_3(k;U,V)+H_2(n;U,V),\\
\mathcal H=(r-U)(g_3-\ell_tU-\ell_\rho V-m)+f_V(\ell-f),\\
G=V-P(U),\quad \mathcal H=GQ,\quad
Q(y,\vartheta)\in L^*,\quad \deg\mathcal H\le4 .
\end{gathered}
\tag{2}
\]
These are the literal chart potentials and eliminant, not a
generic relation substituted for them. The directional Taylor
polynomial is
\(H_j(c;U,V)=\sum_{i=0}^j c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).

## 2. The nonlinear graph has a pure eliminant

If \(\deg P=3\) or \(4\), total degree in (2) and the unit
evaluation of \(Q\) give \(\mathcal H=cG\), \(c\in L^*\).
If \(\deg P=2\), the same unit evaluation gives
\(Q-c\in(G)\) with \(\deg Q\le2\), so
\[
\mathcal H=cG+\lambda G^2,\qquad c\in L^*,\quad \lambda\in L .
\tag{3}
\]
Thus in every case \(\deg_V\mathcal H\le2\). The literal
cubic coefficient, before any coefficient-field change, is
\[
[V^3]\mathcal H=\frac{r-U}{6}\,k_{\rho\rho\rho}
                         -\frac{r_\rho^2}{2}.
\tag{4}
\]
Its coefficient of \(U\) and then its constant coefficient
give \(r_\rho=0\). The literal quadratic coefficient now reduces
to \((r-U)n_{\rho\rho}/2\). Comparing it to the constant
\(\lambda=[V^2](cG+\lambda G^2)\) gives
\[
r\in K,\quad n_{\rho\rho}=0,\quad \lambda=0,\quad
\mathcal H=cG,\quad
k=r\rho+k_0,\quad n=s\rho+n_0,\qquad k_0,s,n_0\in K .
\tag{5}
\]
For degrees three and four the comparison simply uses
\([V^2](cG)=0\). The integrations in (5) subtract explicit
primitives of constants for \(\partial_\rho\), not arbitrary
antiderivatives.

Use primes for \(\partial_t\) on \(K\). The coefficient of \(V\)
in the literal eliminant is
\[
[V]\mathcal H
=(r-U)\left(\frac{r''}{2}U^2+s'U-\ell_\rho\right)
                         -(r'U+s)^2=c .
\tag{6}
\]
Successively comparing the coefficients of \(U^3,U^2,U\)
and the constant term proves
\[
r''=0,\quad s'=-(r')^2,\quad
\ell_\rho=2r's+r(r')^2,\quad c=-(rr'+s)^2 .
\tag{7}
\]
The exact joint constant field gives
\[
\begin{gathered}
r=\mu t+\nu,\quad s=-\mu^2t+s_0,\quad
d:=\mu\nu+s_0\in\mathbb C^*,\quad c=-d^2,\\
\mu,\nu,s_0\in\mathbb C,\qquad
\ell=(2\mu d-\mu^2r)\rho+\ell_0,\quad \ell_0\in K .
\end{gathered}
\tag{8}
\]
The nonzero condition on \(d\) follows from \(c\ne0\).
Neither \(\mu\) nor \(\nu\) is required to be nonzero.

## 3. The normalization is an actual constant translation

Perform the original polynomial coordinate change
\[
\widetilde X=X+\mu,\qquad
\widetilde Y=Y-\nu,\qquad
\widetilde Z=Z,\qquad \widetilde W=W .
\tag{9}
\]
Its inverse subtracts \(\mu\) from \(\widetilde X\) and adds
\(\nu\) to \(\widetilde Y\), fixing the other two coordinates.
It preserves the speeds, the exact time profile, the full initial
kernel, and the selected original \(\partial_Z\). Thus \(a,N,L,t,\rho\)
and the normalized parameter \(v\) are unchanged.

Expand the same original polynomials in \(\widetilde X\).
The actual projected entries become
\[
\begin{gathered}
\widetilde y=y-r,\quad
\widetilde\vartheta=\vartheta-2\mu\rho,\quad
\widetilde w=w-\mu\vartheta+\mu^2\rho,\\
\widetilde\sigma=\sigma+2\mu t\rho,\quad
\widetilde z=z-\mu\sigma-\mu^2t\rho .
\end{gathered}
\tag{10}
\]
These identities and their inverse substitutions follow directly
from \(X=\widetilde X-\mu\) in the original chart. In particular
\(\widetilde\vartheta\) is still a graph of degree \(\deg P\) in
\(\widetilde y\). The first two integrated coefficients are exactly
\[
\begin{gathered}
\widetilde k=k-r\rho=k_0,\qquad \widetilde r=0,\\
\widetilde n=n-\mu k+r k_t+\mu r\rho
   =d\rho+\widetilde n_0,\qquad
\widetilde n_0=n_0-\mu k_0+r k_0' .
\end{gathered}
\tag{11}
\]
For example, the first formula follows by substituting (10) in
\(\sigma=-t\vartheta-\rho y+k\). The second follows from
\(z+tw=k_ty+(r-y)\vartheta+n\); here
\(\widetilde r-\widetilde y=r-y\), so no generic denominator
was introduced.

The first potential gives a useful additional exact formula:
\[
\widetilde\ell
=\ell_0-r n_0'-\frac{r^2}{2}k_0''\in K .
\tag{12}
\]
Indeed in the old variables
\(f=k_0''y^2/2+(\mu y+s)\vartheta+(n_0'-\mu^2\rho)y\).
Insert (10)--(11) into
\((-\widetilde y)\widetilde w+
\widetilde k_{tt}\widetilde y^2/2+
d\widetilde\vartheta+\widetilde n_{0,t}\widetilde y\).
The theta terms match the old ones; the remainder is
\(\ell+(\mu^2r-2\mu d)\rho-rn_0'-r^2k_0''/2\),
which is (12).

Coefficient partials on \(L\) have not changed: \(t,\rho,v\)
are unchanged. If one instead uses \(y\) or \(\widetilde y\)
as the whole-line parameter, the extensions satisfy
\[
\partial_t|_{\widetilde y}
=\partial_t|_y+\mu\partial_y,\qquad
\partial_\rho|_{\widetilde y}=\partial_\rho|_y,\qquad
\partial_{\widetilde y}=\partial_y .
\tag{13}
\]
This is the chain rule for \(y=\widetilde y+r(t)\).
It is not a change of the coefficient derivatives on \(L\).

Drop tildes from now on, and call the new coefficient in \(K\)
again \(n_0\), the new first potential again \(\ell\), and the
new second potential \(m\in L\). The latter is defined by the
retained actual chart after (9); no formula for transforming an
arbitrary old \(m\) is needed. The normalized data are
\[
r=0,\qquad k\in K,\qquad n=d\rho+n_0,\quad n_0,\ell\in K,\quad
d\in\mathbb C^* .
\tag{14}
\]

## 4. Normalized potentials and the correctly calibrated determinant

The two literal potentials now read
\[
-yw+\frac{k''}{2}y^2+n_0'y+d\vartheta=\ell,\qquad
dw+\frac{k'''}6y^3+\frac{n_0''}2y^2-\ell'y=m .
\tag{15}
\]
Thus
\[
\begin{aligned}
w={}&\frac md-\frac{k'''}{6d}y^3
                  -\frac{n_0''}{2d}y^2+\frac{\ell'}d y,\\
\vartheta={}&-\frac{k'''}{6d^2}y^4
             -\frac{n_0''}{2d^2}y^3
 +\left(\frac{\ell'}{d^2}-\frac{k''}{2d}\right)y^2
 +\left(\frac m{d^2}-\frac{n_0'}d\right)y+\frac\ell d,\\
z={}&k'y-y\vartheta+d\rho+n_0-tw .
\end{aligned}
\tag{16}
\]
All coefficient derivatives still act on the exact field \(L\).
The scalar \(d\) in this display is not the unnormalized ordinary
quadratic coefficient \(E^2W/2\).

Since \(y=\gamma v+\eta\), using \(y\) in place of \(v\) changes
the calibrated determinant by the nonzero factor \(\gamma=Ny\):
\[
\mathcal J_y(X)
=\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
=-\frac{a^3}{\gamma}\in L^*,\qquad \gamma=Ny\in L^* .
\tag{17}
\]
The two coefficient directions here hold \(y\) fixed. Explicitly
\(\partial_i|_y=\partial_i|_v-(y_i|_v/\gamma)\partial_v\)
for \(i=t,\rho\), and \(\partial_y=\gamma^{-1}\partial_v\).
These derivations restrict to the original derivatives on \(L\).
Translation (9) leaves \(\gamma\) unchanged. In particular neither
\(\gamma=1\) nor a global unit speed is assumed.

Set \(A_1=m_\rho\). At \(X=0\), the first Jacobian row is
\((0,0,1)\), so
\(\mathcal J_y=z_tw_\rho-z_\rho w_t\).
Using (15) to cancel the terms involving \(y^2w_t\) gives
\[
\begin{aligned}
\mathcal J_y={}&-m_t+\frac{A_1}{d}\left(n_0'-\frac md\right)\\
&+\left[-\ell''+\frac{A_1}{d}
                    \left(k''-\frac{2\ell'}d\right)\right]y\\
&+\frac12\left[n_0'''+\frac{3A_1}{d^2}n_0''\right]y^2
 +\frac16\left[k''''+\frac{4A_1}{d^2}k'''\right]y^3 .
\end{aligned}
\tag{18}
\]
For a direct reconstruction, use \(w_\rho=A_1/d\),
\(\vartheta_\rho=A_1y/d^2\), and
\(z=k'y-y\vartheta+d\rho+n_0-tw\).
The two terms involving \(t w_t w_\rho\) cancel as well.
Since (17) is independent of \(y\), (18) proves
\[
\begin{gathered}
k''''+\frac{4A_1}{d^2}k'''=0,\qquad
n_0'''+\frac{3A_1}{d^2}n_0''=0,\\
\ell''=\frac{A_1}{d}\left(k''-\frac{2\ell'}d\right),\qquad
-m_t+\frac{A_1}{d}\left(n_0'-\frac md\right)
=-\frac{a^3}{\gamma}\ne0 .
\end{gathered}
\tag{19}
\]
Only the actual determinant and literal potentials were used.

## 5. What the degree-three and degree-four branches force

If \(\deg P\ge3\), at least one of \(k'''\), \(n_0''\) is
nonzero by (16). The first or second equation of (19) then gives
\(A_1\in K\). Subtracting its explicit rho primitive gives
\[
m=A_1\rho+B_0,\qquad A_1,B_0\in K,\qquad L=K(\rho).
\tag{20}
\]
Here is the last, actual field-return step. Formula (16) puts all
of \(z,w,\vartheta\) in \(K(\rho)[y]\). The original inverse175,
also valid after the actual translations, gives
\(\mathbb C(y,z,w)=L(y)\). Therefore
\[
L(y)=\mathbb C(y,z,w)\subseteq K(\rho)(y)\subseteq L(y).
\]
Intersecting with \(L\) gives \(L=K(\rho)\); the elementary
intersection \(L\cap K(\rho)(y)=K(\rho)\) follows by coefficient
comparison in a rational expression in the transcendental \(y\).
This does not make \(K\) rational over \(\mathbb C\).

The remaining scalar equation is
\[
-\left(A_1'+\frac{A_1^2}{d^2}\right)\rho
-B_0'+\frac{A_1}{d}\left(n_0'-\frac{B_0}d\right)
=-\frac{a^3}{\gamma}.
\tag{21}
\]
It does not prove \(A_1'+A_1^2/d^2=0\).
Although \(a\in K(\rho)\), the denominator \(\gamma=Ny\)
also belongs to \(K(\rho)^*\) and is not normalized to one.
Thus the right side is not known to be a rational cube up to
a constant. Omitting \(\gamma\) would produce an invalid
rational-cube degree argument. No reciprocal-linear formula
for \(A_1\), exclusion of \(A_1=0\), or degree-three/four
recognition is inferred here.

## 6. The degree-two graph has an actual good-coordinate reframe

If \(\deg P=2\), equation (16) forces
\(k'''=n_0''=0\). Exact joint constants, by subtracting successive
explicit primitives, give complex constants \(A_0,B_1,C_0,D_0,F_0\)
such that
\[
k=A_0t^2+B_1t+C_0,\qquad n_0=D_0t+F_0 .
\tag{22}
\]
No constraint on the possibly algebraic \(m\) is needed below.
Let \(H=XZ+YW\) in the normalized actual coordinates and put
\[
F_{\rm good}=C_0X^2+B_1XY+A_0Y^2+F_0X+D_0Y,\qquad
P_0=\frac{F_{\rm good}-H}{d}\in\mathbb C[X,Y,H].
\tag{23}
\]
The literal split identity175 and \(Y=y+tX\) give
\[
H=yw+(k'y+d\rho+n_0)X+kX^2,\qquad
\partial_X F_{\rm good}=2kX+k'y+n_0 .
\]
Here \(\partial_X\) fixes all of \(L[y]\). Consequently
\[
\partial_X P_0=-\rho,\qquad EP_0=-a\rho,\qquad E^2P_0=0 .
\tag{24}
\]
This is an affine-in-time correction, not an invariant one.

The polynomial derivation
\(\Delta=Y\partial_Z-X\partial_W\) kills \(X,Y,H\), and
therefore \(P_0\). The actual polynomial automorphism
\(\exp(-P_0\Delta)\) is explicitly
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z-YP_0,\quad W_1=W+XP_0 .
\tag{25}
\]
It preserves \(H=X_1Z_1+Y_1W_1\). Its inverse adds
\(Y_1P_0(X_1,Y_1,H)\) to \(Z_1\) and subtracts
\(X_1P_0(X_1,Y_1,H)\) from \(W_1\). Preservation of \(H\)
verifies both inverse orders, without a generic-coordinate descent.

Writing \(b=EY=at\), the ordinary quadratic coefficients give
\[
\frac{E^2Z}{2}=-ab\rho,\qquad
\frac{E^2W}{2}=a^2\rho,\qquad
\frac{E^2(YP_0)}2=b\,EP_0=-ab\rho,\qquad
\frac{E^2(XP_0)}2=a\,EP_0=-a^2\rho .
\tag{26}
\]
Hence \(E^2X_1=E^2Y_1=E^2Z_1=E^2W_1=0\).
These are actual coordinates, with the same global slice.
The retained
[three-good recognition156](three-good-all-degree-recognition-pass156-working.md)
therefore gives \(A\simeq\mathbb C^{[3]}\) in this subcase.
This endpoint explicitly inherits that working theorem's sources;
it is not a new recursive audit of them.

## Scope

The actual graph degree-two branch is recognized by (23)--(26).
For graph degree three or four, only the coefficient equations
and exact field return (19)--(21) are established here.
The graph of degree at most one is outside this note's assumption,
as are other initial configurations and unrestricted entry.

The normalization is an original constant coordinate translation;
the final quadratic-graph reframe is an explicit polynomial
automorphism. In contrast, the generic parameter change in (17)
is allowed to have a nonconstant coefficient factor. Keeping
these two operations distinct is essential.

The relevant saved175--177 sources and the retained156 synthesis
were read before authoring. No checker was executed or imported,
and no earlier source, packet, or live index was changed.
These working deductions are not a novelty claim, a human expert
certification, a proof-assistant verification, or a proof of
unrestricted cancellation.
