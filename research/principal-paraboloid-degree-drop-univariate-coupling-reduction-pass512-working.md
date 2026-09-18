# A necessary system at the quadratic-projection degree drop

Working result: retain the FULL actual principal chart264 and its
genuine third and fourth potentials. Suppose sigma is an intrinsic
affine parameter, the coupling satisfies \(m_s=0\), \(m\notin\mathbb C\),
and the quadratic theta coefficient obeys \(1+ma=0\).
This is the degree-drop boundary excluded from327's quadratic-parity
hypothesis.

The full actual assumptions force a quadratic-or-lower y, an exact
one-variable leading coefficient, two differential necessary equations,
and a separating transverse coefficient. Two possible zero branches
are excluded: the remaining linear projection coefficient and the
quadratic coefficient of the evaluated H_U cannot vanish.
The proof retains a zero quadratic coefficient of y.

These are necessary reductions, not an exclusion of this entire
boundary, a converse realization, an ambient coordinate change, or
an unrestricted cancellation result.

## 1. Actual entry, exact fields and the degree-drop hypothesis

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), the
genuine levels and unit-gradient-minor conclusions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the universal affine-sigma part of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w),\qquad
L[y,z_0,w]=O.
\end{gathered}
\tag{1}
\]
Here z_0 is the original Z intercept. All coefficient partials are
the commuting extensions from C(t,s); their joint constants are C.
The original slice, literal selected partial, full initial kernel and
both actual returns remain required.

Assume precisely
\[
\deg_v\sigma=1,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
m=k_s\ne0,\quad m_s=0,\quad m\notin\mathbb C,
\qquad \theta=-\frac{P^2}{m}+bP+c.
\tag{2}
\]
Thus \(O=L[P]\), and the coefficient partials are extended to fix P.
Put
\[
F_0=\ker_L\partial_s,\qquad
p=m'\ne0,\quad q=m'',\quad k=ms+f(t),\qquad m,f\in F_0.
\tag{3}
\]
Primes mean the exact t derivative on F_0, not a derivative after
an unspecified change of parameters. The nonzero p follows from
the joint-constant field. As in494, F_0 is finite over C(t) and its
t-derivative constants are exactly C. Neither F_0=C(t) nor L=F_0(s)
is assumed. The expression f=k-ms is an existing s-constant.

At fixed actual X the literal rows and scalar are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-F(P,\theta),\\
F(P,V)&=\frac{k_{tt}}2P^2+pPV+n_tP+n_sV,\\
J(X,P)&=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
       =-\frac{a_0^4}{\rho}\in L^*.
\end{aligned}
\tag{4}
\]
All n,ell,b,c and the coefficients of y are initially retained in L.
The scalar may depend on the coefficient parameters; it is independent
of X and P. In particular it is not set to a complex constant.

Localizing the actual equality \(\mathcal B_{a_0}=A_{a_0}[X]\)
at the coefficient constants gives the whole all-X return
\[
L[X,Y,Z,W]=L[X,P].
\tag{5}
\]
It remains true after extending L and specializing X to any element
of the extension field. Such a specialization is a polynomial-ring
test of (5), not evaluation of the original ambient coordinates at
a noncomplex point with a claimed actual fiber.

## 2. A degree bound without the quadratic-parity hypothesis

Use the genuine monic third polynomial
\[
\begin{aligned}
G(U,P,V)&=\frac{\ell-(2P+k_t)U-F(P,V)}m,\\
H(U,P,V)&=U^2+F_PU+F_VG+\frac{k_{ttt}}6P^3+\frac q2P^2V\\
&\hspace{12mm}+\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
-\ell_tP-\ell_sV,\\
H(y,P,\theta)&=h_0\in L.
\end{aligned}
\tag{6}
\]
After substituting theta from (2), the coefficient of U in H has
P-degree at most two, and the U-free term has P-degree at most four.
For example F_V=pP+n_s has degree one and the U-free part of
F(P,theta) has degree at most three. If y had degree d>2, its square
would have degree 2d, strictly larger than both d+2 and 4. The monic
level in (6) therefore proves
\[
y=eP^2+lP+r,\qquad e,l,r\in L,
\tag{7}
\]
where e is allowed to be zero.

Write \(f_H=H_U^{\rm ev}\), \(g_H=H_V^{\rm ev}\), with evaluation
at (y,P,theta). Both have P-degree at most two. The universal494
identities, including the genuine fourth potential, give
\[
\begin{gathered}
\mathcal A=y_t+\theta_Py_s+y_P^2=\kappa g_H,\\
\mathcal B_1=\theta_t+
\theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P=-\kappa f_H,
\qquad\kappa\in L^*,\\
\nu=\frac{pP+n_s}{m},\quad
\beta_f=\frac{2y+F_P(P,\theta)}m,\quad D_f=\frac{2P+k_t}{m},\\
\mathcal W=(\theta_P+D_f)g_H^2+
(y_P-\theta_s-\nu)f_Hg_H-y_sf_H^2\in L^*,\qquad
J=\kappa\mathcal W.
\end{gathered}
\tag{8}
\]
The last equality is the complete scalar identity after the level
and multiplier equations. Neither f_H nor g_H is assumed nonzero
before applying494. Its proof covers both zero-gradient-component
cases. The moving level term has already been retained in deriving
the displayed W; no additional \(f_Hh_{0,s}\) term occurs.

The P^3 coefficient of A is \(-2e_s/m\). The right side of its
equation in (8) has degree at most two. Consequently
\[
e_s=0,\qquad e\in F_0.
\tag{9}
\]
This argument does not divide by e. It uses no parity statement
from327: in the present case \(P^2+k_tP+m\theta\) has degree at
most one, not the exact degree two required there.

## 3. The complete necessary high-coefficient system

The P^4 coefficient of the actual H level is
\[
[P^4]H^{\rm ev}
=\frac{n_{ss}+2m^2e^2-6mpe+2p^2-mq}{2m^2}.
\]
Thus, defining N_2 in F_0, exact integration by subtraction gives
\[
N_2=-2m^2e^2+6mpe-2p^2+mq,\qquad
n=\frac{N_2}{2}s^2+n_1s+n_0,
\quad n_1,n_0\in F_0.
\tag{10}
\]
No primitive in a rational function field is being postulated.
For instance n_1=n_s-N_2s and then n_0=n-N_2s^2/2-n_1s
are the existing s-constants.

Set
\[
F_2=2e-\frac{3p}{m}=[P^2]f_H,\qquad
G_2=2me^2-5pe+\frac{p^2}{m}-\frac q2=[P^2]g_H.
\tag{11}
\]
The two P^2 equations in (8) are exactly
\[
l_s=\frac m2(e'+4e^2-\kappa G_2),\qquad
b_s=e-\frac pm+\frac{\kappa mF_2}{2}.
\tag{12}
\]
They remain valid when e or G_2 vanishes.

For the complete cubic H coefficient, define
\[
\begin{aligned}
E_0={}&4me^3-12pe^2+4mee'-7qe+\frac{9p^2e}{m}-6pe'
-\frac56m'''+\frac{9pq}{2m}-\frac{4p^3}{m^2},\\
C_0={}&\left(e-\frac{p}{2m}\right)f''-\frac{ep}{m}f'
+\left(-\frac{2e}{m}+\frac{2p}{m^2}\right)n_1
-\frac{n_1'}m+\frac{f'''}6.
\end{aligned}
\tag{13}
\]
Here E_0,C_0 belong to F_0. Full substitution into (6) gives
\[
[P^3]H^{\rm ev}=F_2l+G_2b+E_0s+C_0=0.
\tag{14}
\]
In particular differentiating this equation in s and using (12)
cancels kappa. The resulting exact identity is
\[
F_2l_s+G_2b_s+E_0=-\frac{5}{6m^2}\mathcal E,
\]
where the necessary differential equation is
\[
\boxed{
\begin{aligned}
\mathcal E={}&-12m^3e^3+30m^2pe^2-6m^3ee'
+9m^2qe-18mp^2e+9m^2pe'\\
&+m^2m'''-6mpq+6p^3=0.
\end{aligned}}
\tag{15}
\]

There is a second independent high equation. Because
\(\theta_P+D_f=(k_t+mb)/m\) is constant in P, the P^5
coefficient of the full W in (8), after (12), is
\[
\begin{aligned}
[P^5]\mathcal W
&=(2e-b_s-p/m)F_2G_2-l_sF_2^2\\
&=F_2\left(eG_2-\frac{mF_2}{2}(e'+4e^2)\right)
=\frac{F_2\mathcal T}{2m},
\end{aligned}
\tag{16}
\]
with
\[
\boxed{\mathcal T=-4e^3m^2+2e^2mp-2ee'm^2-emq+2ep^2+3e'mp.}
\tag{17}
\]
Thus F_2 T=0 before resolving the F_2 boundary. These calculations
retain the arbitrary lower coefficients c,r,ell and their derivatives;
their absence from these selected high equations is cancellation,
not a normalization or deletion.

## 4. The quadratic H_U coefficient cannot vanish

First F_2 and G_2 cannot both be zero. Otherwise (11) implies
\[
e=\frac{3p}{2m},\qquad q=-\frac{4p^2}{m},\qquad
e'=-\frac{15p^2}{2m^2},\qquad m'''=\frac{36p^3}{m^2}.
\tag{18}
\]
The last two equations are actual derivatives of the first two.
Substituting (18) in E gives \(\mathcal E=12p^3\ne0\),
contradicting (15).

Suppose now F_2=0, so G_2 is nonzero. Then
\[
e=\frac{3p}{2m}\ne0,\quad
G_2=-\frac q2-\frac{2p^2}{m}\ne0,\quad
b_s=\frac{p}{2m},\quad N_2=mq+\frac52p^2.
\tag{19}
\]
Put \(\epsilon=k_t+mb\), and write \(f_H=f_1P+f_0\), allowing
f_1=0. Directly from the formal H_U in (6),
\[
f_1=2l+k_{tt}+pb-\frac{2n_s+pk_t}{m}.
\tag{20}
\]
In this branch the P coefficient of \(y_P-\theta_s-\nu\) is e.
Since g_H has exact degree two and y_s has degree at most one,
the entire P^4 coefficient of W is
\[
[P^4]\mathcal W=\frac\epsilon mG_2^2+ef_1G_2=0.
\tag{21}
\]
All m,e,G_2 are s-constant. Equations (12),(19),(20) give
\[
\epsilon_s=me,\qquad (f_1)_s=-G_2(1+m\kappa).
\tag{22}
\]
For example differentiating (20) gives
\(2l_s+q+pb_s-(2N_2+p^2)/m\), which is the second expression
in (22). Differentiating (21) in s therefore yields
\[
0=-em\kappa G_2^2,
\]
an impossibility. No division by epsilon, f_1, q or a moving root
was used. We have proved
\[
\boxed{F_2\ne0,\qquad\mathcal E=0,\qquad\mathcal T=0.}
\tag{23}
\]

## 5. The remaining linear projection coefficient cannot vanish

The literal rows (4) give the exact identity
\[
Z-2tY=\epsilon P+mc+n+kX-t^2X^2,
\qquad\epsilon=k_t+mb.
\tag{24}
\]
We prove \(\epsilon\ne0\) using only the full all-X return (5).
The proof does not use an assumed actual ambient coordinate formed
from the left side of (24).

Suppose epsilon is zero. After any field extension and specialization
X=x, the Z row belongs to the algebra generated by Y and constants.
Hence (5) requires \(\overline L[Y_x,W_x]=\overline L[P]\)
for every x in an algebraic closure of L. The cubic coefficient of
the literal W row is
\[
g_3=[P^3]w=\frac{p-2me}{m^2}.
\tag{25}
\]
There are three exhaustive cases.

If e=0, choose x=-l. Then Y_x is constant, while W_x retains
the nonzero cubic coefficient p/m^2. A polynomial of degree three
cannot alone generate the polynomial ring in P, by degrees of
polynomial compositions. This contradicts (5).

If e is nonzero and g_3 is nonzero, fix any x and center the quadratic
Y_x by an affine intrinsic parameter Q, so Y_x=eQ^2+constant.
Subtract the even part of W_x using Y_x. Its remaining odd part is
\(Q(g_3Q^2+j)\) for some j in the algebraic closure. Thus the
generated algebra is contained in
\[
\overline L[Q^2]\ \oplus
Q(g_3Q^2+j)\overline L[Q^2],
\tag{26}
\]
which is a subalgebra because the square of its odd generator is
even. It does not contain Q: g_3Q^2+j is a nonunit in the even
polynomial ring. This includes j=0 and repeated or zero roots, so
no distinct-pair assumption has been hidden in the argument.

Finally let e be nonzero and g_3=0. Write the full two specialized
rows before specialization as
\[
\begin{aligned}
Y&=eP^2+(l+X)P+\text{constant in P},\\
W&=(w_2-X/m)P^2+(w_1+bX)P+\text{constant in P},
\end{aligned}
\]
with arbitrary w_2,w_1 in L. Eliminating P^2 leaves a linear
coefficient whose product with e is
\[
K(X)=e(w_1+bX)-(w_2-X/m)(l+X),\qquad [X^2]K=1/m\ne0.
\tag{27}
\]
At a root x of K over the algebraic closure, W_x is a scalar
multiple of Y_x plus a constant. The resulting algebra is generated
by one polynomial of exact degree two, again not the full line.
This argument does not require the root of K to be simple.

All three cases contradict (5). Therefore
\[
\boxed{\epsilon=k_t+mb\ne0.}
\tag{28}
\]
Conversely, at the coefficient-ring level only, (24) then explicitly
recovers P from Y,Z over L[X]. This observation does not certify
the original actual chart or any of its lower scalar equations.

## 6. An exact transverse coefficient and a bounded subcase

Because F_2 is nonzero, define the existing coefficient
\[
z=b-\left(e-\frac pm\right)s.
\tag{29}
\]
Equations (12),(14),(15) give the full expressions
\[
\begin{aligned}
b&=\left(e-\frac pm\right)s+z,\qquad
z_s=\frac{\kappa mF_2}{2}\ne0,\\
l&=\frac m2(e'+4e^2)s-\frac{G_2}{F_2}z-\frac{C_0}{F_2}.
\end{aligned}
\tag{30}
\]
Indeed (15) identifies E_0 with
\(-F_2m(e'+4e^2)/2-G_2(e-p/m)\), which gives the second
line directly from (14). The variable z in this section is a
coefficient parameter, not the original Z intercept z_0.

The nonzero z_s proves that t,z form an exact separating basis:
\[
[L:\mathbb C(t,z)]<\infty,\quad
\partial_z|_t=z_s^{-1}\partial_s|_t,\quad
\partial_t|_z=\partial_t|_s-(z_t/z_s)\partial_s|_t,
\qquad
J_{t,z,P}=-\frac{a_0^4}{\rho z_s}\ne0.
\tag{31}
\]
The constants of the new transverse partial are still exactly F_0.
There is no assertion that L=F_0(z), that z is polynomial in s,
or that z is an ambient coordinate. The original speed rho and the
parameter factor z_s must be retained in subsequent scalar work.

There is one short zero-leading-coefficient consequence. If g_3=0
in (25), then e=p/(2m), F_2=-2p/m, and its actual derivative is
\(e'=q/(2m)-p^2/(2m^2)\). Substitution in (17) gives
\[
\mathcal T=\frac{pq}{2}.
\]
Since p is nonzero, (23) forces
\[
g_3=0\quad\Longrightarrow\quad m''=0,
\qquad m=pt+d,\quad p\in\mathbb C^*,\ d\in\mathbb C.
\tag{32}
\]
This statement does not transfer327,496 or any subsequent
nonzero-delta result to the degree-drop boundary. Any such extension
must separately verify its literal entry and downstream hypotheses.

## 7. Verification and remaining scope

The complete264,296,327 and universal494 inputs were read. The
initial use of327 is solely to identify its excluded boundary, not
to import its parity or quadratic-y coefficient.
Fresh unsaved033f0f/9fc5db reconstruct the full H coefficient ledger,
both evaluated gradient leaders, the complete cubic coefficient
(14), and the W coefficient (16). Fresh17a982 checks the common
F_2,G_2 boundary and the quadratic in (27); a044e8 reconstructs
the full differentiated coefficient (21); f0c8c9 checks (32).
The independent peer reconstruction54e7df and d070ce checks the
same full H, multiplier and minor identities and the zero branches.
These are algebraic reconstructions, not replacements for the
field, whole-return or degree arguments written above.

The unresolved branch still has the full lower genuine-H and
genuine-Q equations, the complete nonzero scalar, and the original
actual ring returns to satisfy. No converse, entire conic exclusion,
ambient recognition, general chart entry or unrestricted cancellation
is claimed. All saved checkers remained frozen. None was executed,
imported, compiled or rerun. No earlier source or canonical file was
edited in authoring this note.
