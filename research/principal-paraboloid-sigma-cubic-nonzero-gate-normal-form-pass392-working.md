# A polynomial coefficient normal form for the nonzero cubic gate

Working necessary reduction in the supplied actual principal chart:
in the strict sigma-dominant profile (deg theta,deg sigma)=(2,3),
the nonzero gate Ecal=n_sss/6-n_ss^2/(2n_s) forces all three intrinsic
generators to be polynomials in t and an affine line parameter over
the exact field S=ker_L partial_t. The strong complex field return
then gives L=S(t). A further scalar coefficient gives Ecal/F^4 in C*.

This note does not exclude this branch or recognize an original
coordinate. In particular coefficient-field polynomial expressions
are not promoted to original polynomial coordinates. The later
polynomial-ring return or degree-divisibility argument is not used.

## 1. Complete actual entry and the permitted normalization

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the strict-degree reduction and compatibility conclusion of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
and [387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_{A_0}\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv=1,\quad O=L[v],\\
K=\operatorname{Frac}A_0=L(v)=\mathbb C(y,z,w),\quad
O=L[y,z,w]=L[y,\sigma,\theta],\quad k=s.
\end{gathered}
\tag{1}
\]
The selected partial is the literal actual Z-partial, and the
coefficient partials on L are the unique commuting extensions of
partial_t,partial_s on C(t,s). The present profile is specifically
deg theta=2, deg sigma=3. No conclusion about another profile is
assumed here.

Source387 gives n=gamma*t+f, with gamma complex, f_t=0, and f_ss
nonzero. The actual translation Y*=Y+gamma/2, fixing X,Z,W, has a
complex polynomial inverse, preserves the full initial kernel and
the selected N, and replaces the intercept by y*=y+gamma/2.
Its first two potentials become
z=2t*y*+sigma^2+theta+f and w=ell-2sigma*y*-f_s*theta.
Thus n*=f and ell*=ell, while k=s, calibration, whole return and
strong return are preserved. Drop stars after this actual operation.
Write
\[
\mathcal S=\ker_L\partial_t,\qquad
n=f\in\mathcal S,\qquad \nu=f_s,\qquad e=f_{ss}\ne0.
\tag{2}
\]
In particular nu is nonzero, nu_s=e, and nu_t=e_t=0.
Commutation makes S stable under partial_s. Its partial_s constants
are exactly C, the joint constants of L.

For clarity, S is finite over C(s), but need not equal C(s).
Indeed the monic minimal polynomial over C(t,s) of any t-constant
element has t-constant coefficients, by differentiation and minimality,
so those coefficients lie in C(s). The degrees of all finite
subextensions of S/C(s) are bounded by [L:C(t,s)]; the primitive
element theorem then gives finiteness. Also t is transcendental
over S, by differentiation of a putative separable minimal polynomial.
We do not yet identify L with S(t).

## 2. The affine intrinsic parameter and the complete levels

Put p=ell_t and C=ell_s+nu^2. In385's remainder, after (2),
Delta=-nu and j=-p/(2nu). Its degree is 2*deg theta-deg sigma=1.
Consequently
\[
r=y+\frac p{2\nu},\qquad O=L[r],\qquad
\rho=Nr\in L^*,\qquad y=r-\frac p{2\nu}.
\tag{3}
\]
The equality O=L[r] follows because r is affine nonconstant in the
original v, not from a new plane-curve assumption. Write
\[
\theta=a r^2+b r+c,\qquad a\in L^*,\quad b,c\in L.
\tag{4}
\]
The letters a,b here are intrinsic coefficients, not the actual
leader a0 or n_ts, which is zero after (2).

The literal full rows and scalar are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+\theta+f+(2t\sigma+s)X+t^2X^2,\\
W&=\ell-2\sigma y-\nu\theta+\theta X+sX^2,\\
\mathcal J(X)&=\det\frac{\partial(Y,Z,W)}{\partial(t,s,r)}
             =-\frac{a_0^4}{\rho}\in L^*.
\end{aligned}
\tag{5}
\]
The coefficient derivatives in this determinant hold r fixed.
On L they remain the same exact coefficient partials. The factor
rho in (5) accounts for the moving intrinsic parameter, so the
calibration is not incorrectly retained as -a0^4.

For independent formal U,P,V, the complete normalized third and
fourth polynomials specialized from385 are
\[
H=U^2-2\nu PU+\frac e2V^2-pP-CV+\nu\ell,
\qquad H(y,\sigma,\theta)=h_0\in L,
\tag{6}
\]
\[
\begin{aligned}
Q={}&[2(C-\nu^2)P-2ePV-p]U+\frac{e_s}{6}V^3
       -\frac{p_t}{2}P^2-p_sPV-\frac{C_s}{2}V^2\\
 &-(h_0)_tP+[e\ell+\nu(C-\nu^2)-(h_0)_s]V,
\qquad Q(y,\sigma,\theta)=q_0\in L.
\end{aligned}
\tag{7}
\]
The level derivatives in (7) are retained. Formal gradients are
taken before evaluation, and no coefficient derivative is replaced
by differentiation of a moving root.

Substitute (3),(4) in (6). Comparing its constant term and dividing
the remaining polynomial by r gives respectively
\[
h_0=\frac{p^2}{4\nu^2}+\frac e2c^2-Cc+\nu\ell
\tag{8}
\]
and the complete intrinsic cubic
\[
\begin{aligned}
\sigma={}&\frac{ea^2}{4\nu}r^3+\frac{eab}{2\nu}r^2\\
 &+\left[\frac1{2\nu}+\frac{e(b^2+2ac)}{4\nu}
                   -\frac{Ca}{2\nu}\right]r
 -\frac p{2\nu^2}+\frac{ebc}{2\nu}-\frac{Cb}{2\nu}.
\end{aligned}
\tag{9}
\]
This is polynomial division in L[r]. In particular its leading
coefficient is nonzero, consistent with deg sigma=3.

## 3. The three highest fourth-potential coefficients

Define the exact t-constant gate
\[
\mathcal E=\frac{e_s}{6}-\frac{e^2}{2\nu}\in\mathcal S,
\qquad \mathcal E\ne0.
\tag{10}
\]
The last inequality is the branch assumption of this note. The case
Ecal=0 is not divided out or treated by the conclusions below.

Insert (3),(4),(9) in the full (7), before dropping any lower terms.
The r^6 coefficient is
\[
[r^6]Q=a^3\left(\mathcal E-\frac{ae^2p_t}{32\nu^2}\right).
\tag{11}
\]
It vanishes by the level, so set
\[
F=p_t=\frac{32\nu^2\mathcal E}{ae^2}\ne0.
\tag{12}
\]
At this stage F need not yet be t-constant. After (12), the next
coefficient is
\[
[r^5]Q=\frac{a^2}{4\nu^2}
       [ae^2p-ae\nu p_s-4\mathcal E b\nu^2],
\qquad
\mathcal E b=\frac{ae}{4\nu}\left(\frac{pe}{\nu}-p_s\right).
\tag{13}
\]
After both gates, define
\[
c_*:=\frac{4C}{e}
 +\frac{3e\ell_s/\nu-\ell_{ss}}{2\mathcal E}
 -\frac{4\mathcal E\nu+e^2}{ae\nu\mathcal E}.
\tag{14}
\]
Direct collection of the r^4 coefficient gives
\[
[r^4]Q=a^2\mathcal E(c_*-c),\qquad c=c_*.
\tag{15}
\]
For instance C_s=ell_ss+2nu*e converts the raw coefficient into
(14). The h0 derivative terms in (7) have degrees at most three
and two, so they do not contribute to (11),(13),(15); they have
not been declared zero. These identities impose no condition on
the remaining lower fourth-potential coefficients.

## 4. Two high coefficients of the literal scalar

Here only X=0 is needed, as a necessary specialization of the full
nonzero scalar (5). Set P=sigma and V=theta as polynomials in r.
The following exact row operations preserve its determinant:
\[
\begin{aligned}
R_1&=dy,\\
R_2&=dZ-2t\,dy=2P\,dP+dV+2y\,dt+\nu\,ds,\\
R_3&=dW+2P\,dy+\nu R_2
       =(2\nu P-2y)dP+2\nu r\,dt+(C-eV)ds.
\end{aligned}
\tag{16}
\]
The symbol d in (16) means total differential in (t,s,r) at X=0;
the functions t and nu multiply rows, and no derivative of those
row multipliers is inserted. Equations (3),(9) retain all their
coefficient derivatives when these rows are expanded.

The r^10 and r^9 coefficients cancel identically. The next one is
\[
[r^8]\mathcal J(0)
 =-\frac{a^4a_t e(3e^2-\nu e_s)}{8\nu^2}
 =\frac{3a^4a_t e\mathcal E}{4\nu}.
\tag{17}
\]
Calibration makes it zero. All other factors are nonzero, proving
a_t=0. Thus a and the F of (12) both belong to S*.

After a_t=0, the next scalar coefficient is exactly
\[
[r^7]\mathcal J(0)=\frac{a^4e}{16\nu^3}
 [aF(e^2+12\nu\mathcal E)+a_s e\nu F
                                      +12\nu^2\mathcal E b_t].
\tag{18}
\]
Differentiate (13) in t, using a_t=0, to get
b_t=ae(Fe/nu-F_s)/(4nu*Ecal). Together with the logarithmic
s derivative of (12), equation (18) gives
\[
3\frac{\mathcal E_s}{\mathcal E}
 =8\frac{e_s}{e}-8\frac e\nu+4\frac{a_s}{a},
\qquad
\frac{\mathcal E_s}{\mathcal E}=4\frac{F_s}{F}.
\tag{19}
\]
All divisions are by known nonzero field elements. Since Ecal and
F are already t-constant, their quotient Ecal/F^4 has both exact
coefficient derivatives zero. Hence
\[
\boxed{\frac{\mathcal E}{F^4}=\delta\in\mathbb C^*.}
\tag{20}
\]
This uses joint constants, not a choice of a fourth root or a
rationality assumption about S.

## 5. Polynomial coefficients in t over the exact field S

Exact integration of p_t=F in L, with F_t=0, gives
\[
p=Ft+B,\qquad
\ell=\frac F2t^2+Bt+D,\qquad B,D\in\mathcal S.
\tag{21}
\]
For example B=p-Ft and D=ell-Ft^2/2-Bt have zero t derivative.
Equation (13) becomes
\[
\begin{aligned}
b&=\beta t+\beta_0,\\
\beta&=8-\frac{8\nu F_s}{eF},\qquad
\beta_0=\frac{8B}{F}-\frac{8\nu B_s}{eF}.
\end{aligned}
\tag{22}
\]
Equation (14), retaining every derivative of B,D,F, similarly gives
\[
\begin{aligned}
c&=c_2t^2+c_1t+c_0,\\
c_2&=\frac{2F_s}{e}
       +\frac{3eF_s/\nu-F_{ss}}{4\mathcal E},\\
c_1&=\frac{4B_s}{e}
       +\frac{3eB_s/\nu-B_{ss}}{2\mathcal E},\\
c_0&=\frac{4(D_s+\nu^2)}e
       +\frac{3eD_s/\nu-D_{ss}}{2\mathcal E}
       -\frac{4\mathcal E\nu+e^2}{ae\nu\mathcal E}.
\end{aligned}
\tag{23}
\]
Every displayed coefficient belongs to S. In particular (3),(4),(9)
give y,sigma,theta in S[t,r], with respective total-degree bounds
one, three and two. The literal first two potentials and full rows
of (5) then give
\[
y,z,w\in\mathcal S[t,r],\qquad
X,Y,Z,W\in\mathcal S[t,r,X].
\tag{24}
\]
The second inclusion is interpreted inside the actual function
field after adjoining S. It is not an equality of original rings,
and does not yet say that S[y,z,w]=S[t,r].

## 6. Strong field return removes the remaining algebraic extension

The actual strong return in (1), together with (24), gives both
inclusions in
\[
K=\mathbb C(y,z,w)\subseteq\mathcal S(t,r)
                       \subseteq L(r)=K.
\tag{25}
\]
Therefore K=S(t,r). The selected N kills S and t, while Nr=rho
is nonzero. For a rational function in S(t,r), its N derivative
is rho times its ordinary r derivative. Characteristic zero gives
the exact constant field S(t), irrespective of whether rho was
previously known to belong to that smaller field. As ker_K N=L,
this proves
\[
\boxed{L=\mathcal S(t),\qquad
K=\mathcal S(t,r),\qquad [\mathcal S:\mathbb C(s)]<\infty.}
\tag{26}
\]
Thus rationality in the t direction is a conclusion of the actual
strong return, not an ansatz used in the coefficient integrations.
Neither S=C(s) nor any ambient-coordinate status of s,t,r follows.

## 7. Scope and verification record

The complete264,296,385,387 sources were read through EOF before
this source was finalized. The fresh read handles were11697b,
761d74,62288e,0f3c21 respectively. The actual gamma translation,
moving-parameter determinant factor, full two potentials, and both
actual returns are explicitly retained above.

Fresh unsaved370b38 rebuilt the full (7), substituted (3),(4),(9),
and verified each coefficient in (11),(13),(15), including the full
c formula, with zero residuals. Fresh unsavedfd88a8 independently
rebuilt the literal determinant via (16), verified its vanishing
r^10,r^9 coefficients, and recovered (17),(18). The earlier
independent scalar computations076e9f/54382a and9f9b3b gave the
same coefficients and the exact logarithmic identity (19).
These are generic symbolic identities with coefficient derivatives,
not numeric sampling or a converse to the actual chart.

This note stops at the necessary polynomial normal form and field
return (26). Lower scalar and fourth-potential coefficients remain
available. No Abhyankar-Moh application, original-ring recognition,
exclusion of Ecal=0, arbitrary-chart entry or unrestricted
cancellation result is claimed. No saved checker was executed,
imported, compiled or rerun. No held source or canonical index was
edited; no novelty, human-expert review or formal certification
is asserted.
