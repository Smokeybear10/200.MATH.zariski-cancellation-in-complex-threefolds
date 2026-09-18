# Equal higher degrees with a nonzero leading W row are impossible

Working conditional exclusion. Retain the FULL actual264 chart,
the genuine levels and unit-gradient conditions of296, and the
universal multiplier identities in Sections1--3 of494. Suppose

\[
 \sigma=P,\quad m=k_s\ne0,\quad m_s=0,\quad
 \deg_Py=\deg_P\theta=d\ge3,\quad
 y=rP^d+\cdots,\quad\theta=aP^d+\cdots,\quad
 \omega=-\frac{2r+m_ta}{m}\ne0.
\tag{1}
\]

Then these hypotheses are inconsistent. This excludes the entire
specified branch, including its cubic and quartic possibilities.
It does not exclude the complementary zero-leading-row branch,
unequal degrees, nonzero m_s, or nonlinear sigma. In particular it
does not supply a reduction of general cancellation data to264.

## 1. Actual inputs and the retained reduction

The underlying actual ring is B=C[X,Y,Z,W]=A[u_glob], with
E=partial_(u_glob), the actual time profile (1,2,2,2), and ENTIRE
original initial kernel (mathsf X^2 mathsf Z-mathsf Y^2). Retain
the literal selected derivation N=[u_glob^4]partial_Z|A, its
coefficient field L=Frac(ker_A N), and every return from264.
In particular L is finite over C(t,s), its commuting coefficient
partials fix P, and

\[
 \begin{gathered}
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\qquad
 L[y,z_{\rm int},w]=L[P],\qquad L[X,Y,Z,W]=L[X,P],\\
 Y=y+PX+tX^2,\qquad
 Z=z_{\rm int}+(2tP+k)X+t^2X^2,\qquad
 W=w+\theta X+sX^2,\\
 z_{\rm int}=2ty+P^2+k_tP+m\theta+n,\\
 mw=\ell-(2P+k_t)y-\frac{k_{tt}}2P^2-pP\theta-n_tP-n_s\theta,
 \qquad p=m_t,\\
 J=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
      =-a_0^4/\rho\in L^*,\qquad a_0=EX,\quad NP=\rho\in L^*.
 \end{gathered}
\tag{2}
\]

Here z_int is the LITERAL Z intercept, not z_int-2ty.
Neither t nor s is asserted to be an ambient coordinate. The
scalar J may depend on t,s. The original global slice need not
equal X/a_0. Lower coefficient functions and the potentials
remain unrestricted unless a stated consequence constrains them.

The complete necessary reduction in
[522](principal-paraboloid-equal-higher-degree-univariate-coupling-reduction-pass522-working.md)
applies to exactly (1). It proves

\[
 C:=\frac{2tr+ma}{r}\in\mathbb C,\qquad
 q:=\frac ra=\frac{m}{C-2t},\qquad
 u:=2q+p\ne0,\qquad
 y=q\theta+R(P),\quad\deg R\le2,\quad d\in\{3,4\}.
\tag{3}
\]

Its proof includes the zero literal Z leader C=0 and p=0.
It uses the actual polynomial three-ring, the full source-initial
kernel, a complete cofactor bound, invariant growth, and the
genuine unit gradient. No recognition theorem or arbitrary
coefficient-field normal form is substituted for those inputs.
This note uses (3) as a retained dependency, then excludes both
remaining degrees using only the complete rows and the all-X
polynomial-ring return in (2).

## 2. A licensed complex normalization

Since C is complex, the following is an actual polynomial
automorphism of the original ring:

\[
 X_*=X,\qquad Y_*=Y-\frac C2X^2,\qquad
 Z_*=Z-CY+\frac{C^2}4X^2,\qquad W_*=W.
\tag{4}
\]

Its inverse is X=X_*, W=W_*,
Y=Y_*+CX_*^2/2 and Z=Z_*+CY_*+C^2X_*^2/4.
Its determinant is one. Moreover

\[
 X_*^2Z_*-Y_*^2=X^2Z-Y^2,\qquad
 t_*=t-C/2,\quad s_*=s,\quad P_*=P.
\tag{5}
\]

The weighted automorphism in (4) therefore preserves the ENTIRE
initial-kernel statement. The leading coefficients in the time
profile stay nonzero: t_* is transcendental over C, and s is
unchanged. The literal partial partial_(Z_*) equals partial_Z,
so the selected N, a_0 and rho are unchanged. The coefficient
parameter shift also has determinant one, preserving J.

The first and second potential formulas keep k,m,n,ell,theta
unchanged as functions reexpressed in t_*,s. The intercepts
transform by y_*=y, z_(int,*)=z_int-Cy, w_*=w. This is a
COMPLEX linear change on the literal intercepts, so BOTH the
strong C-field return and the L-polynomial return survive.
The all-X return survives the actual polynomial automorphism.

Renaming the new variables, (3) now reads

\[
 q=-\frac{m}{2t},\qquad u=p-\frac mt\ne0,\qquad
 y=-\frac{m}{2t}\theta+R,\qquad
 R=d_2P^2+d_1P+d_0.
\tag{6}
\]

The symbols d_2,d_1,d_0 are arbitrary members of L; d_2 may
vanish. Division by t is legitimate in L because t is
transcendental over C. No actual finite fiber t=0 is deleted to
make an ambient recognition claim; all remaining arguments take
place in the already licensed coefficient ring of (2).

## 3. Simultaneous odd parts of the complete rows

Abbreviate k_1=k_t, k_2=k_tt and set D=2td_2+1. We NEVER
divide by D. In the coefficient-field extension L(lambda), put

\[
 X_\lambda=-\frac Dt\lambda-d_1-\frac{k_1}{2t},\qquad
 P=\lambda+\xi,\qquad z=\xi^2.
\tag{7}
\]

Here lambda is an indeterminate. This substitution is an
auxiliary base change and specialization, not an ambient
automorphism or a claim that X_lambda is a complex constant.

Write the unique even/odd decomposition

\[
 \theta(\lambda+\xi)=E(\lambda,z)+\xi O(\lambda,z),
 \qquad E,O\in L[\lambda,z].
\tag{8}
\]

By the odd part of a polynomial in xi we mean its coefficient
of xi in L[z] direct-sum xi L[z]. Define

\[
 \begin{aligned}
 F(\lambda,z)&=mO+2\lambda+k_1,\\
 c_\lambda&=-(2md_2+p)\lambda-md_1-n_s,\\
 L_{\rm low}(\lambda,z)&=2d_2z+6d_2\lambda^2
             +(4d_1+2k_1d_2+k_2)\lambda+k_1d_1+2d_0+n_t,\\
 g(\lambda,z)&=c_\lambda O-uE-L_{\rm low},\\
 G(\lambda,z)&=c_\lambda(2\lambda+k_1)+muE+mL_{\rm low}.
 \end{aligned}
\tag{9}
\]

Evaluate the COMPLETE original rows of (2) at (7). Their odd
parts are exactly

\[
 \operatorname{odd}(Y)=-\frac{F}{2t},\qquad
 \operatorname{odd}(Z)=0,\qquad
 \operatorname{odd}(mW)=g,
 \qquad G=c_\lambda F-mg.
\tag{10}
\]

For clarity, the full Z polynomial after (6) is
2tR+P^2+k_1P+n+(2tP+k)X+t^2X^2. Its xi coefficient is
2Dlambda+2td_1+k_1+2tX_lambda=0. This remains true if D=0,
when its P degree drops. The Y odd part is
qO+2d_2lambda+d_1+X_lambda=-(mO+2lambda+k_1)/(2t).

The full W calculation can be checked before splitting:

\[
 mW=[mX-(2P+k_1)q-pP-n_s]\theta
       +\ell-(2P+k_1)R-\frac{k_2}2P^2-n_tP+msX^2.
\tag{11}
\]

At (7), the bracket equals c_lambda-u xi. Its contribution to
the odd part is c_lambda O-uE. The remaining odd part is
-L_low. In particular no lower potential term, X-dependent
term, or coefficient of R was dropped to obtain (10).

## 4. Both residual degrees force a common odd-part root

Take the resultant Res_z(F,G) with its conventional ordering
(F,G). The following calculations are in L[lambda], without
requiring any nonleading coefficient to be nonzero.

### 4.1. Cubic theta

For theta=aP^3+bP^2+cP+e, with a nonzero,

\[
 \begin{aligned}
 O&=a(z+3\lambda^2)+2b\lambda+c,\\
 E&=a(\lambda^3+3\lambda z)+b(\lambda^2+z)+c\lambda+e.
 \end{aligned}
\tag{12}
\]

F is linear in z with constant nonzero leader ma, and G has
degree at most one in z. Direct use of the resultant for two
linear polynomials, with its constant-polynomial specialization,
gives

\[
 \deg_\lambda\operatorname{Res}_z(F,G)=3,\qquad
 [\lambda^3]\operatorname{Res}_z(F,G)=-8m^2ua^2\ne0.
\tag{13}
\]

For an explicit leading check, F_0 has lambda leader 3ma and
degree two. G_1 has lambda leader 3mua and degree one;
G_0 has lambda leader mua and degree three. Therefore
F_1G_0-F_0G_1 has degree three with leader
m^2ua^2-9m^2ua^2. Lower terms in (9) cannot reach that degree.
At every specialization of lambda, F retains its nonzero
z coefficient ma. A zero of this resultant therefore gives a
finite common root of F and G, even if G drops degree.

### 4.2. Quartic theta

For theta=aP^4+bP^3+cP^2+eP+h, with a nonzero,

\[
 \begin{aligned}
 O&=4a\lambda z+4a\lambda^3+b(z+3\lambda^2)+2c\lambda+e,\\
 E&=a(z^2+6\lambda^2z+\lambda^4)
       +b(3\lambda z+\lambda^3)+c(z+\lambda^2)+e\lambda+h.
 \end{aligned}
\tag{14}
\]

Now F has degree at most one in z and G has degree exactly
two, with constant nonzero z^2 leader mua. Writing
F=F_1z+F_0 and G=G_2z^2+G_1z+G_0, the resultant is
G_2F_0^2-G_1F_0F_1+G_0F_1^2. Consequently

\[
 \deg_\lambda\operatorname{Res}_z(F,G)=6,\qquad
 [\lambda^6]\operatorname{Res}_z(F,G)=-64m^3ua^3\ne0.
\tag{15}
\]

Indeed the relevant lambda leaders of F_0,F_1,G_2,G_1,G_0
are 4ma,4ma,mua,6mua,mua, at degrees three, one, zero,
two and four. The three degree-six contributions are
(16-96+16)m^3ua^3.

This also handles specialization at F_1=0. If F_0 remains
nonzero there, the resultant is G_2F_0^2, which is nonzero.
Thus a resultant zero with F_1=0 forces F_0=0 too. Then F
is the zero polynomial and G is still a quadratic with
nonzero leading coefficient, so a finite common root exists
over an algebraic closure. No root at infinity is being
misrepresented as a finite common root.

## 5. Contradiction to the all-X polynomial-ring return

Let M be an algebraic closure of L. In either degree (13) or
(15), the resultant is a nonconstant polynomial with nonzero
leading coefficient. It has a root lambda_0 in M. By Section4
there is z_0 in M such that

\[
 F(\lambda_0,z_0)=G(\lambda_0,z_0)=g(\lambda_0,z_0)=0.
\tag{16}
\]

The last equality uses (10) and m nonzero. The ideal
I=(F(lambda_0,z),g(lambda_0,z)) in M[z] is proper, since
evaluation at z_0 annihilates it.

The return L[X,Y,Z,W]=L[X,P] in (2) survives scalar extension
to M and passage to the quotient X=X_(lambda_0). Translating
P=lambda_0+xi in that quotient gives the actual polynomial
generation equality

\[
 M[Y_0(\xi),Z_0(\xi),W_0(\xi)]=M[\xi].
\tag{17}
\]

On the other hand (10) puts every generator on the left in

\[
 \mathcal S=M[z]\mathbin{\oplus}\xi I\ \subset\ M[\xi],
 \qquad z=\xi^2.
\tag{18}
\]

This is a subring: even terms multiply as usual, even times
odd preserves I, and the product of two odd terms lies in
zI^2, hence in the unrestricted even summand M[z]. It is
proper because the unique even/odd decomposition of xi has
odd coefficient one, and 1 is not in I. Thus (18) excludes
xi from the left side of (17), a contradiction.

The argument includes z_0=0. In that case it detects the
failure to recover the linear term, rather than requiring
two distinct opposite points. It also includes D=0, all
lower-coefficient cancellations, and every degree drop of F
or G allowed by Section4. Only the original all-X return is
used; no unproved plane-coordinate theorem is invoked.

## 6. Verification and scope

Root read the entire held522 source in619262+2fc67e at SHA
530c3fd4ec901f0f19b3b378ecac49746baa75a1ffb6917ab3b4962dd8fa3968.
Fresh inline calculation89f3de, completedacf92d, reconstructed
both inverse orders in (4), the exact initial-relation identity,
the ambient determinant and selected partial, then all three
COMPLETE row odd parts and both full resultants with arbitrary
lower coefficients. Every asserted residual was zero. It also
substituted D=0 directly without dividing by D.

The earlier separate General outline checkcfb509 reconstructed
the same complete identities and checked the finite-root and
proper-subring steps. A complete saved-source review is a
separate gate after this author hold. These symbolic checks
supplement the field, specialization and parity arguments;
they are not proof-assistant certification or expert review.

This excludes exactly (1), conditional on the retained actual
sources and522. It does not prove arbitrary chart entry, force
m_s=0, force equal degrees, or treat omega=0. The general
cancellation problem remains unsolved, and the intended field
and dimension of Luo's original email remain unconfirmed.
No novelty assertion, public submission or external contact
is made. No saved checker was executed, imported or compiled.
