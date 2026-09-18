# Quartic theta is impossible with transverse coupling

In the FULL actual principal chart264, with affine nonconstant
intrinsic sigma, the following hypotheses are inconsistent:
\[
 P=\sigma,\qquad m=k_s\ne0,\qquad h=m_s\ne0,\qquad
 \deg_P\theta=4.
\tag{1}
\]
The retained degree bound521 gives deg y<=4, including constant
and zero y. A complete all-X resultant argument rules out a
quartic y. The full H level, scalar multiplier and unit tangent
minor then exclude every remaining degree.

The exceptional resultant root is treated explicitly. A positive
resultant degree alone would NOT prove the exclusion. No condition
on m_tt, unheld classification, or plane-embedding theorem is used.

## 1. Full actual hypotheses and complete identities

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and evaluated unit-minor conclusions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the degree-unrestricted Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,
\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
 E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\quad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the FULL initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
 L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
 A\otimes_{\ker N}L=L[P],\\
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\quad
 L[y,z_{\rm int},w]=L[P],\quad L[X,Y,Z,W]=L[X,P].
 \end{gathered}
\tag{2}
\]
Here z_int is the literal original Z-intercept. Coefficient
partials are the exact commuting extensions from C(t,s),
extended to fix P. No rationality of L is assumed. The original
slice need not equal X/a0. For the all-X license, localization
of B=A[u_glob] at nonzero elements of ker N gives
L[P][u_glob]=L[P][X], since a0 is inverted and x0 lies in A.
This is also L[X,Y,Z,W].

Put p=m_t. The complete literal rows are
\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-k_{tt}P^2/2-pP\theta-h\theta^2/2-n_tP-n_s\theta,\\
 J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
 \end{aligned}
\tag{3}
\]
Every moving lower coefficient and level is retained. The accepted
[521](principal-paraboloid-higher-slope-intercept-degree-bound-pass521-working.md)
gives deg_P y<=4 under (1), with no exception for y=0.

For later use, recall the entire off-level formal decomposition
from521. With U,P,V independent, put
\[
 B=pP+n_s,\qquad F_0=k_{tt}P^2/2+n_tP,\qquad \gamma_P=2P+k_t.
\]
Then
\[
 H-h_0=U^2+(C_1+C_2V)U+C_3V^3+C_4V^2+C_5V+C_6,
\tag{4}
\]
where
\[
 \begin{aligned}
 C_1&=k_{tt}P+n_t-\gamma_P B/m,& C_2&=p-\gamma_P h/m,\\
 C_3&=h_s/6-h^2/(2m),&
 C_4&=h_tP/2+n_{ss}/2-3hB/(2m),\\
 C_5&=m_{tt}P^2/2+n_{ts}P-\ell_s+(h\ell-B^2-hF_0)/m,\\
 C_6&=k_{ttt}P^3/6+n_{tt}P^2/2-\ell_tP-h_0+B(\ell-F_0)/m.
 \end{aligned}
\tag{5}
\]
Their P degrees are at most 2,1,0,1,2,3. Evaluation gives
H(y,P,theta)-h0=0. Formal differentiation BEFORE evaluation gives
\[
 f=2y+C_1+C_2\theta,\qquad
 g=C_2y+3C_3\theta^2+2C_4\theta+C_5.
\tag{6}
\]
The complete universal identities from494 are
\[
 \begin{aligned}
 \nu&=(pP+n_s+h\theta)/m,\quad
 \beta_f=(2y+k_{tt}P+p\theta+n_t)/m,\quad D_f=(2P+k_t)/m,\\
 \mathcal A&=y_t+\theta_Py_s+y_P^2=\kappa g,\\
 \mathcal B_1&=\theta_t+\theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P=-\kappa f,
       \qquad \kappa\in L^*,\\
 \mathcal W&=(\theta_P+D_f)g^2+(y_P-\theta_s-\nu)fg-y_sf^2\in L^*,
       \qquad (f,g)L[P]=L[P].
 \end{aligned}
\tag{7}
\]
No conic-specific assertion of494 is used.

## 2. A complete all-X odd-part certificate

Write theta=aP⁴+bP³+lower terms, with a!=0, and allow y to
have any degree at most four. For an auxiliary lambda, put
P=lambda+xi, z=xi² and decompose
\[
 \theta(\lambda+\xi)=E(\lambda,z)+\xi O(\lambda,z),\qquad
 y(\lambda+\xi)=E_y(\lambda,z)+\xi O_y(\lambda,z).
\tag{8}
\]
Odd means the coefficient of xi. Set k1=k_t, k2=k_tt,
gamma0=2lambda+k1, and
\[
 \begin{aligned}
 F&=mO+\gamma_0,\\
 G&=(mp-h\gamma_0)E+2mE_y+mk_2\lambda+mn_t
                         -(p\lambda+n_s)\gamma_0.
 \end{aligned}
\tag{9}
\]
Expansion of ALL terms in (3) gives
\[
 \begin{aligned}
 \operatorname{odd}Y&=O_y+X,\\
 \operatorname{odd}Z&=2t(O_y+X)+F,\\
 m\operatorname{odd}(mW)
   &=m^2O(X+O_y)-(mO_y+p\lambda+n_s+hE)F-G.
 \end{aligned}
\tag{10}
\]
The X² terms are even in xi. The last identity retains the full
theta-squared and lower-potential contributions.

There can be no finite common zero (lambda0,z0) of F,G over an
algebraic closure M of L. Indeed, choose the CONSTANT value
X0=-O_y(lambda0,z0), only after finding such a zero. At fixed
lambda0,X0, all three original odd coefficients vanish at z0.
Every specialized generator therefore lies in the proper ring
\[
 M[z]\mathbin{\oplus}\xi(z-z_0)M[z]\ \subsetneq\ M[\xi].
\tag{11}
\]
The product of two odd terms belongs to the unrestricted even
part, so this is a ring; it misses xi. The base-changed all-X
return evaluated at X0 instead requires M[P]=M[xi]. This
contradiction includes z0=0. It is a coefficient-field
specialization, not an actual noncomplex ambient fiber claim.

## 3. Every exceptional-root case

Center the quartic using an existing coefficient-field translation:
\[
 \chi=-b/(4a),\quad Q=P-\chi,\quad
 \theta=aQ^4+cQ^2+dQ+e,\quad
 y=r_4Q^4+RQ^3+VQ^2+W_1Q+J.
\tag{12}
\]
The coefficients in (12) are renamed centered coefficients.
This is only a polynomial substitution over L. No actual map or
constancy of chi under coefficient derivatives is asserted.

For this algebra put lambda=chi+u and gamma=k1+2chi. Define
\[
 \begin{aligned}
 B_0&=md+\gamma,\quad B_1=2mc+2,\quad Q_0=mp-h\gamma,\\
 C_0&=aQ_0+2mr_4,\quad L_1=6mR-2hc,\quad M_0=Q_0c+2mV,\\
 K_1&=Q_0d-2he+2mW_1+mk_2-p\gamma-2(p\chi+n_s),\\
 K_0&=Q_0e+2mJ+mk_2\chi+mn_t-(p\chi+n_s)\gamma.
 \end{aligned}
\tag{13}
\]
These are odd-polynomial coefficients, not new chart potentials.
The ENTIRE pair (9) becomes
\[
 \begin{aligned}
 F={}&A(u)z+B(u),\qquad A(u)=4ma u,\quad
 B(u)=B_0+B_1u+4ma u^3,\\
 G={}&(C_0-2ha u)z^2
       +(-12ha u^3+6C_0u^2+L_1u+M_0)z\\
 &-2ha u^5+C_0u^4+(2mR-2hc)u^3
                    +(M_0-2hd-2p)u^2+K_1u+K_0.
 \end{aligned}
\tag{14}
\]
Writing G=G2*z²+G1*z+G0, its linear-quadratic resultant is
\[
 \mathcal R(u)=A^2G_0-ABG_1+B^2G_2,\qquad
 \deg_u\mathcal R=7,\qquad [u^7]\mathcal R=128m^2ha^3\ne0.
\tag{15}
\]
For u!=0, F is genuinely linear in z. A root of R there gives
a finite common root by substitution into G, even if G has
lost degree. Section2 forbids every such root. Therefore
\[
 \mathcal R(u)=128m^2ha^3u^7.
\tag{16}
\]
This alone does NOT license a finite common root at u=0.

Suppose first B0=0. Then F(0,z) is identically zero. Absence of
a finite common root requires G(0,z) to be a nonzero constant:
\[
 C_0=M_0=0,\qquad K_0\ne0.
\tag{17}
\]
If G(0,z) were nonconstant or zero, Section2 would already give
a contradiction. Under (17), F=u(4ma z+B1+4ma u²). The
resultant has exact u-order two, with coefficient (4ma)²K0!=0.
Equivalently, factor u² from (15) and evaluate its remaining
factor at zero. This contradicts (16). Hence
\[
 B_0\ne0.
\tag{18}
\]
Now R(0)=B0²C0, so (16) first forces C0=0. After precisely
this substitution, the full resultant has coefficients
\[
 [u^4]\mathcal R=-32a^2mQ_0,\qquad
 [u^5]\mathcal R=64a^2m(-Rm^2+chm+h).
\tag{19}
\]
Thus (16) gives
\[
 Q_0=0,\qquad r_4=0,\qquad
 R=\frac h m\left(c+\frac1m\right).
\tag{20}
\]
The conclusion r4=0 uses C0=aQ0+2mr4=0. No lower coefficient
has been divided by. The final residue relation in (20) is an
additional checked necessity, but is not needed below.

This proves deg_P y<=3. From here onward we return to the
ORIGINAL P and its original fixed-P coefficient derivatives.
The translation (12) is never differentiated while being
mistakenly held fixed.

## 4. The full H level rules out every degree below three

Since deg y<=3, the degree-twelve term in (4) is uniquely
C3*theta³. After its removal, the degree-nine term is uniquely
the linear part of C4 times theta². Consequently
\[
 h_s=3h^2/m,\qquad h_t=3hp/m,\qquad
 C_3=0,\quad \deg_P C_4\le0.
\tag{21}
\]
There is no condition on m_tt.

Suppose deg y<=2. The degree-eight coefficient then forces the
constant C4=0. The complete level becomes
\[
 y^2+C_1y+C_6+g\theta=0,\qquad g=C_2y+C_5.
\tag{22}
\]
If y has exact degree two with leader v2, g has exact degree
three and leader -2h*v2/m. Then g*theta has degree seven,
whereas every other term in (22) has degree at most four.
This is impossible.

If y has degree at most one, including zero, the other terms
in (22) have degree at most three. The quartic theta forces
g=0. But f=2y+C1+C2*theta has exact degree five with
leader -2ha/m!=0. This contradicts (f,g)=L[P] from (7).
No zero-gradient component was divided away.

Hence, in the original P notation, write
\[
 \theta=aP^4+bP^3+cP^2+dP+e,\qquad
 y=rP^3+vP^2+w_1P+j,\qquad a,r\in L^*.
\tag{23}
\]
These are the original coefficients, not the centered lower
coefficients of (12). The degree-eight H coefficient gives
\[
 C_4=\frac{2hr}{ma},\qquad
 \deg_Pf=5,\quad [P^5]f=-\frac{2ha}{m},\qquad
 \deg_Pg=4,\quad [P^4]g=\frac{2hr}{m}.
\tag{24}
\]
All stated leaders are nonzero.

## 5. Complete scalar and minor coefficients

In the original coefficient basis, set
\[
 K_\theta=y_P+\theta_s+\nu.
\tag{25}
\]
The full B1 identity has degree at most five. Its degree-seven
coefficient and then its degree-six coefficient give
\[
 [P^7]\mathcal B_1=4a(a_s+ha/m)=0,\qquad
 [P^6]\mathcal B_1=4a(b_s+hb/m)=0
       \quad\hbox{after the first gate}.
\tag{26}
\]
Therefore K_theta has degree at most two. Write
k2bar=[P²]K_theta, allowing k2bar=0 without division.
The full degree-five B1 equation is
\[
 4a\bar k_2=\kappa\frac{2ha}{m},\qquad
 \bar k_2=\frac{\kappa h}{2m}.
\tag{27}
\]
Terms theta_t and beta_f have degree at most four; D_f*y_P
has degree at most three, so no discarded term contributes.

Since A=kappa*g has degree at most four, its degree-six and
degree-five coefficients successively give
\[
 [P^6]\mathcal A=4ar_s=0,\qquad
 [P^5]\mathcal A=4av_s=0\quad\hbox{after }r_s=0.
\tag{28}
\]
In particular y_s has degree at most one. The complete
degree-four equation is
\[
 4a(w_1)_s+9r^2=\kappa\frac{2hr}{m}=4r\bar k_2.
\tag{29}
\]
This uses (27), with no constancy assumption on kappa.

Now use the entire minor formula (7). After (26),(28), all
three terms have degree at most eleven. The coefficient is
\[
 \begin{aligned}
 [P^{11}]\mathcal W
 &=4a\left(\frac{2hr}{m}\right)^2
 +(6r-\bar k_2)\left(-\frac{2ha}{m}\right)
                       \left(\frac{2hr}{m}\right)
 -(w_1)_s\left(-\frac{2ha}{m}\right)^2\\
 &=-\frac{4h^2a}{m^2}
       \left(a(w_1)_s+2r^2-r\bar k_2\right).
 \end{aligned}
\tag{30}
\]
Indeed y_P-theta_s-nu=2y_P-K_theta, explaining its quadratic
coefficient 6r-k2bar. Equation (29) gives
a(w1)_s=r*k2bar-9r²/4. Therefore
\[
 [P^{11}]\mathcal W=\frac{ah^2r^2}{m^2}\ne0.
\tag{31}
\]
This contradicts the coefficient-field unit Wcal in (7) and
proves (1). All t derivatives and lower coefficients remain
unrestricted; no moving-center connection was omitted.

## 6. Degree-collapse control, verification and scope

The exceptional root issue is substantive. At the level of
the first two potential formulas only, take
m=s,h=1,p=k_t=k_tt=n_t=n_s=0, k=s²/2, and
\[
 \theta=(P^4+P)/s,\qquad
 y=(P^3-P^2/4+7P/4+7/8)/s^2.
\tag{32}
\]
The resultant is 128u⁷/s, but at its only root u=0 one has
F=1 and G=(7-2z)/(4s), so there is no finite common root.
This is only a coefficient control, not a solution of the H
level, scalar, unit minors or actual returns. It does not
realize an actual chart. Sections4--5 close the loophole that
a bare positive-degree resultant argument leaves open.

The full actual264 input was reread through EOF5f600e+3ce6a4;
the complete521 input through4da395+ae24db, and complete494
through88d26d+cfdb20. Only494 Sections1--3 are used; its
conic theorem is not imported. Earlier dependencies are retained,
not recursively certified by this note.

Fresh unsaved0396db reconstructed the complete original parity
rows, the W certificate (10), degree-seven resultant and leader,
and the control (32), with zero residuals. Fresh ed15ae and
corrected34e273 verified (19) and the exact order-two coefficient
in the B0=0 case. An omitted m in one diagnostic expectation
for the u5 prefactor was corrected before use; (19) is the
full checked coefficient and its zero equation was unchanged.
General's independent b6978e rebuilt the whole preliminary
certificate, exceptional-root ledger and finite-root identity.

Fresh e5031b independently rebuilt the entire original-P
H,f,g,A,B1,Wcal polynomials with unrestricted lower support.
All eight displayed coefficient residuals for (24),(26)--(30)
and the final substitution (31) were zero. A separate longer
centered reconstruction6263af, independently matched by
65e18c/767271, retained both center derivatives and gave the
same terminal coefficient; that residue-dependent route is
not needed by the shorter original-P proof written here.
All calculations retained arbitrary m_tt.

No earlier source, saved checker or canonical record was edited.
No saved checker was executed, imported, compiled or rerun.
The coefficient-field translations and specializations are not
ambient coordinate promotions. This excludes exactly the
quartic-theta sector under the supplied actual hypotheses and
h!=0. It is not arbitrary chart entry, recognition of all
sectors, unrestricted cancellation or a novelty assertion.
