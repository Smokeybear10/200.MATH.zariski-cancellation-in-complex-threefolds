# A proper radical projection cannot have cubic second generator

Status: working exclusion under the supplied actual radical-chart
hypotheses. If the projected plane ring is proper, its original second
generator has degree two, not three. The proof uses the exact center
fiber and evaluated cofactor, followed by the actual gradient identities.
In the last remaining degree pair, an explicit polynomial normalization
is essential before the scalar-determinant contradiction.

This does not exclude proper projected planes. The actual node and cusp
examples207 have second degree two. No whole-plane recognition, entry
theorem, minimum-profile theorem, or unrestricted cancellation is claimed.

## 1. Exact inputs and the putative cubic branch

Retain the full actual hypotheses of
[eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad a=EX\ne0,\quad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
L/\mathbb C(t,\rho)\text{ finite},\quad A_L=L[v],\quad Nv=1,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
O=L[v],\quad C=L[y,\vartheta]\subsetneq O,\quad
R=2\vartheta+k_\rho\ne0,\quad J_0=-a^3\in L^*.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and extend those on
\(\mathbb C(t,\rho)\). The selected partial is the actual
\(\partial_Z\) in these bad-swapped radical coordinates.
No rationality of \(L\) is assumed.

For independent formal variables \(U,V\), use the following portions
of the fully specified potentials from eliminant206:
\[
\begin{gathered}
\mathcal R=2V+k_\rho,\qquad
S=\frac{k_{tt}}2U^2+k_{t\rho}UV+\frac{k_{\rho\rho}}2V^2
       +n_tU+n_\rho V,\qquad b_0=S_V,\\
T=\ell-S,\qquad
\mathcal K=W_0^2+b_0W_0+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal P=\mathcal R W_0+S-\ell,\qquad
\mathcal P(y,\vartheta,w)=\mathcal K(y,\vartheta,w)=0,\\
z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n.
\end{gathered}
\tag{2}
\]
Here \(H_j\) denotes the divided Taylor polynomial of degree \(j\)
in \(U,V\); all its derivatives are coefficient derivatives.
The nonzero eliminant and its simple selected factor satisfy
\[
\begin{gathered}
\mathcal H=T^2+\mathcal R b_0T+
\mathcal R^2\{H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m\}=GQ,\\
\ker(L[U,V]\longrightarrow O)=(G),\quad
0\ne Q(y,\vartheta)\mid R^3,\quad \deg\mathcal H\le5,\\
V_c=-k_\rho/2,\qquad p(U)=S(U,V_c)-\ell,\qquad
\mathcal H(U,V_c)=p(U)^2.
\end{gathered}
\tag{3}
\]
Properness makes \(p\) nonconstant and squarefree. The evaluated
gradients, formed before evaluation, give
\[
\begin{gathered}
B_1=S_U(y,\vartheta),\quad C_1=2w+b_0(y,\vartheta),\quad
\Lambda_\rho=\ell_\rho-S_\rho(y,\vartheta)-k_{\rho\rho}w,\\
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\qquad
B_1y_x+C_1\vartheta_x+Rw_x=0,\\
R(x_0)=0\ \Longrightarrow\ B_1(x_0)=p'(y(x_0))\ne0.
\end{gathered}
\tag{4}
\]
The middle identity holds for any affine parameter over \(L\).
In particular no division by \(R\) is made at one of its roots.

The fully read [conductor reduction206](radical-projection-conductor-cubic-reduction-pass206-working.md)
and [local refinement208](radical-proper-projection-degree-refinement-pass208-working.md)
give
\[
C=L[x^2,x^3+c x],\quad O=L[x],\quad x=v+\lambda,\quad
c,\lambda\in L,\quad \mathfrak c=(x^2+c)O,\quad
2\le\deg_v\vartheta\le3.
\tag{5}
\]
Suppose for contradiction that \(e=\deg_v\vartheta=3\).
Then \(d=\deg_vy\in\{2,3\}\), \(\deg G=\deg_U G=3\),
\(\deg Q\le2\), and \(k_{tt}\ne0\).
The center \(p\) has two distinct roots \(y_c,y_s\in L\).
The conductor divisor maps to \((y_c,V_c)\). There is exactly
one further root \(s\in L\) of \(R\), simple and away from
the conductor, mapping to \((y_s,V_c)\).
For a cusp the conductor root has order exactly two; for a node
all three roots of \(R\) are simple. These multiplicity statements
are the actual local-potential conclusions of refinement208.

## 2. The exact center fiber fixes the cofactor support

Normalize \(G\) to be monic in \(U\). This is possible over
\(L[V]\), not merely over \(L(V)\). Indeed \(O\) is a free
\(L[\vartheta]\)-module with basis \(1,x,x^2\). Reduction by
the cubic expression for \(\vartheta\) proves spanning, and the
distinct leading degrees modulo three prove independence.
Multiplication by \(y\) therefore has a monic characteristic
polynomial of degree three with coefficients in \(L[\vartheta]\).
Its minimal polynomial also has degree three, since
\(L(y,\vartheta)=L(x)\). Thus the characteristic polynomial
is exactly the monic irreducible equation \(G\).

Specialize this multiplication endomorphism at \(V=V_c\).
The resulting algebra is \(L[x]/(R)\), up to the harmless
factor two in \(\vartheta-V_c=R/2\). After algebraic closure,
the conductor contributes length two with \(y\)-value \(y_c\):
either one length-two cusp point or two distinct node points.
The remaining point is simple, with value \(y_s\).
The characteristic polynomial is consequently
\[
G(U,V_c)=(U-y_c)^2(U-y_s),\qquad
p(U)=\kappa(U-y_c)(U-y_s),\qquad
Q(U,V_c)=\kappa^2(U-y_s),\quad \kappa=k_{tt}/2\ne0.
\tag{6}
\]
This equality descends to the exact field \(L\). It does not use
an assumed squarefree specialization of the plane equation.

In particular \(Q(y,\vartheta)\) is nonzero at the conductor
parameters and zero at \(x=s\). Its divisibility by \(R^3\)
from (3) now gives, in \(L[x]\),
\[
Q(y,\vartheta)=\eta(x-s)^r,\qquad
\eta\in L^*,\qquad 1\le r\le3.
\tag{7}
\]
There are no other roots, including after algebraic closure.
The upper bound uses that the extra root of \(R\) is simple.

## 3. Cusp exclusion and the two possible node powers

If \(c=0\), the extra root satisfies \(s\ne0\).
An element of \(L[x^2,x^3]\) has zero coefficient of \(x\).
The coefficients of \(x\) in \((x-s)^r\), for \(r=1,2,3\),
are respectively \(1,-2s,3s^2\), all nonzero. Equation (7)
is impossible. Thus the putative cubic branch is not cuspidal.

Suppose \(c\ne0\). The exact odd-part criterion is
\[
A(x^2)+xB(x^2)\in C
\quad\Longleftrightarrow\quad B(-c)=0.
\tag{8}
\]
It follows from
\(C=L[x^2]\oplus x(x^2+c)L[x^2]\). Applied to (7), it
excludes \(r=1\), gives \(s=0\) when \(r=2\), and gives
\(c=3s^2\) when \(r=3\).

Retain the exact node notation and constraints proved in
refinement208:
\[
\begin{gathered}
y=y_0+A_2x^2+A_3x(x^2+c),\qquad
R=(x^2+c)(r_1x+r_0),\qquad r_1\ne0,\\
\vartheta=(R-k_\rho)/2,\quad A_2r_1-A_3r_0\ne0,\quad
A_2r_0+cA_3r_1=0,\quad A_2\ne0,\\
s=-r_0/r_1=cA_3/A_2,\qquad s^2+c\ne0.
\end{gathered}
\tag{9}
\]
The relation in the second line comes from the opposite values
of \(C_1\) at the two node parameters, which are the two roots
of the same monic fourth potential in \(w\).
Thus \(r=2\) gives \(A_3=0,d=2\).
If \(r=3\), then \(s\ne0\), \(A_3\ne0,d=3\), and
\(A_2=3sA_3\).

There is also a useful formal, rather than merely evaluated,
consequence. The determinant condition in (9) gives
\(\operatorname{span}_L\{1,y,\vartheta\}
=\operatorname{span}_L\{1,x^2,x^3+cx\}\).
The evaluated cofactor (7) has degree at most three, so it lies
in this span. Subtract the corresponding affine-linear formal
polynomial from \(Q\). The difference has total degree at most
two and lies in the kernel \((G)\), whose generator has degree
three. Therefore
\[
Q\text{ is affine linear},\qquad
\deg\mathcal H=4,\qquad H_3(k)=0.
\tag{10}
\]
It is nonconstant because its evaluation has positive degree.
The last conclusion uses the exact top term
\(\mathcal H_5=4V^2H_3(k)\).

## 4. The cubic node power contradicts the actual gradient

Assume \(r=3\). Differentiate \(\mathcal H=GQ\) formally
in \(V\) and evaluate. Because \(G(y,\vartheta)=0\),
\[
\mathcal H_V(y,\vartheta)=Q(y,\vartheta)G_V(y,\vartheta),
\qquad \operatorname{ord}_{x=s}\mathcal H_V(y,\vartheta)\ge3.
\tag{11}
\]
The same assertion is harmless if the evaluated derivative is
identically zero. The root of \(R\) at \(s\) is simple.
Consequently (4) implies \(C_1(s)=0\). The third-potential
derivative in (4), evaluated at \(s\), then gives
\(y_x(s)=0\), because \(B_1(s)=p'(y_s)\ne0\).
But (9) and \(c=3s^2,A_2=3sA_3\) give
\[
y_x(s)=2A_2s+A_3(3s^2+c)=12s^2A_3\ne0.
\tag{12}
\]
This contradiction excludes the cubic node power.

An independent top-coefficient check is consistent with this
gradient argument. Set \(m_0=r_1/(2A_3)\ne0\). Then
\(y=Y_0+A_3(x+s)^3\) and
\[
(x-s)^3=-\frac12(x+s)^3+\frac{3R}{2r_1}+4s^3.
\tag{13}
\]
Thus the top of the linear cofactor is proportional to
\(V-m_0U/3\), whereas the top of the cubic plane equation is
proportional to \((V-m_0U)^3\). For the latter assertion, cancel
the cubic leading terms in \(\vartheta-m_0y\); its quadratic
coefficient is nonzero by (9), and the resulting quadratic/cubic
parametrization has its cubic top equal to the cube of that
quadratic coordinate. The \(U^3V\) coefficient in their product
is a nonzero multiple of \(-2m_0^3\). In contrast, (10) and the
exact identity
\(\mathcal H_4=H_2(k)^2-2V H_1(k_\rho)H_2(k)+4V^2H_2(n)\)
make that coefficient zero: its first two contributions are
\(k_{tt}k_{t\rho}\) and \(-k_{tt}k_{t\rho}\).
This is a cross-check, not an additional hypothesis in (11)--(12).

## 5. Normalizing the remaining quadratic node in the actual ring

Only \(r=2,d=2,e=3\) remains. Equation (10) says that every
third partial of \(k\) vanishes. The joint constants of the
two coefficient partials in \(L\) are \(\mathbb C\): the
differentials \(dt,d\rho\) form a basis of
\(\Omega_{L/\mathbb C}\), and the kernel of the differential in
a finitely generated characteristic-zero field is algebraic over
the base field. Since \(\mathbb C\) is algebraically closed,
successive subtraction of quadratic and linear primitives gives
\[
k=\kappa t^2+A t\rho+\frac B2\rho^2+C_0t+D_0\rho+F_0,
\qquad \kappa,A,B,C_0,D_0,F_0\in\mathbb C,\quad\kappa\ne0.
\tag{14}
\]
The following actual elementary changes remove every term except
\(\kappa t^2\). They are the lower-time changes used in
[quartic-first208](radical-quartic-first-projection-unit-speed-pass208-working.md),
here with a retained nonzero \(t^2\) coefficient.

First set \(X'=X+s_0\), with \(s_0=-B/4\), leaving the other
coordinates fixed. Comparing full chart expansions gives
\(y'=y-s_0t\), \(\vartheta'=\vartheta-2s_0\rho\),
\(\sigma'=\sigma-2s_0\rho^2\), and
\(k'=k+2s_0\rho^2\). Next, in those coordinates, set
\(W'=W+(A/2)Y+(D_0/2)X\). This changes \(k\) by
\(-At\rho-D_0\rho\). Finally set
\(Z'=Z-C_0Y-F_0X\), removing the remaining linear terms.
Each inverse is the opposite elementary translation or addition.

Only lower-time-degree terms are added, so the exact profile and
full initial map remain unchanged. Every inverse keeps old
\(X,Y,W\) independent of new \(Z\) and gives old \(Z\) as
new \(Z\) plus a polynomial in \(X,Y\). Thus the literal
\(\partial_Z\), selected \(N\), exact field \(L\), ratios
\(t,\rho\), and speed \(a\) remain unchanged. The projected
generators change only by elements of \(L\); their degrees
\((2,3)\) and proper ring are preserved. Relabel the new actual
coordinates, so that \(k=\kappa t^2\).

Repeat the already proved cofactor argument in this normalized
actual chart. Since \(r=2\), one has
\(Q\propto U-y_s\). Indeed (9) gives \(s=0\) and
\(y-y_s=A_2x^2\), so (7) evaluates to a scalar multiple of
\(y-y_s\), and the degree-less-than-three kernel argument
makes this a formal identity. The cubic plane equation has top
proportional to \(U^3\): solve \(x^2=(y-y_s)/A_2\) and use
\(\vartheta-V_c=(r_1/2)x(x^2+c)\) to obtain its literal cubic
relation. Thus \(\mathcal H_4\) is proportional to \(U^4\).
Its exact value in this chart is
\[
\mathcal H_4=\kappa^2U^4+2n_{tt}U^2V^2
                 +4n_{t\rho}UV^3+2n_{\rho\rho}V^4.
\tag{15}
\]
Therefore all second partials of \(n\) vanish, and the same
joint-constant argument gives
\(n=\alpha t+\beta\rho+\gamma\), with
\(\alpha,\beta,\gamma\in\mathbb C\).

## 6. The scalar determinant excludes the quadratic node

Now \(V_c=0\), \(p(U)=\kappa U^2+\alpha U-\ell\), and
the literal eliminant is
\[
\mathcal H=p(U)^2-
V^2\{4\ell_tU+4\ell_\rho V+\beta^2+4m\}.
\tag{16}
\]
The formal factor \(U-y_s\) and \(p(y_s)=0\) imply
\[
\ell_\rho=0,\qquad
\beta^2+4m+4\ell_ty_s=0,\qquad \ell_t\ne0.
\tag{17}
\]
For the last assertion, otherwise (16) would be \(p(U)^2\),
which cannot have the simple irreducible cubic factor \(G\).
Differentiate the simple-root identity \(p(y_s)=0\) in
\(\rho\). Since \(p_\rho=-\ell_\rho=0\) and
\(p'(y_s)\ne0\), one has \((y_s)_\rho=0\).

The fourth potential and then the third become
\[
x_1=w+\beta/2,\qquad x_1^2=\ell_t(y-y_s),\qquad
2\vartheta x_1+p(y)=0.
\tag{18}
\]
Because \(\deg_vy=2\) and \(\ell_t\ne0\), \(x_1\) is an
affine nonconstant parameter, with \((x_1)_v\in L^*\).
Use \(t,\rho,x_1\) as differential coordinates, extending
coefficient partials by fixing \(x_1\). The identity
\(y=y_s+x_1^2/\ell_t\), together with (17), gives
\(y_\rho=0\). Differentiating the final identity of (18) at
fixed \(x_1\) then gives \(2x_1\vartheta_\rho=0\), hence
\(\vartheta_\rho=0\). This second derivative gate is needed;
it cannot be dropped from the determinant calculation.

The second potential in (2) is now
\(z=2\rho w+\vartheta^2+2\kappa t y+
\alpha t+\beta\rho+\gamma\). Consequently
\(w_t=w_\rho=0\), \(w_{x_1}=1\), and
\(z_\rho=2w+\beta=2x_1\). The actual calibration gives
\[
0\ne J_{x_1}=-\frac{a^3}{(x_1)_v}\in L^*,\qquad
J_{x_1}=\det\frac{\partial(y,z,w)}{\partial(t,\rho,x_1)}
       =2x_1y_t.
\tag{19}
\]
The right side is divisible by \(x_1\) in \(L[x_1]\), while
the left side is a nonzero scalar. This is the final contradiction.

## 7. Conclusion and limits

The cusp and both node possibilities with second degree three
have been excluded. Combining this with refinement208 gives
\[
\boxed{C\subsetneq O\quad\Longrightarrow\quad
\deg_v\vartheta=2.}
\tag{20}
\]
The possible proper first degrees are then three and four; equal
quadratic degrees cannot generate a proper birational plane ring,
as proved in conductor206. The separate unit-speed arguments for
these first degrees are not reproduced or assumed here.

All uses of roots and finite fibers were made over the exact field
or its explicitly identified algebraic closure. The actual coordinate
normalization in Section5 has complex coefficients and polynomial
inverses. No normality of the projected plane, rationality of \(L\),
or ambient-coordinate status of \(x,x_1\) was assumed. Proper
degree-two projections remain compatible with the actual examples207.
The whole-plane branch and other initial-kernel sectors are untouched.

The cited eliminant, conductor reduction, local refinement and
quartic-first normalization sources were fully reread before this
note. No saved checker was executed, imported or compiled, and no
earlier source or index was edited. This working proof is not human
expert certification, proof-assistant verification, or historical
novelty clearance.
