# Cubic theta and lower y-degree with nonzero transverse coupling

## 1. Scope and full actual inputs

Retain all the actual hypotheses of264,296 and535. This note imposes
\(\deg_x y\le3\) directly. It does not use an exclusion of the excess
degree-four case to obtain this hypothesis. The sector considered is
\[
 \deg\sigma=2,\qquad \deg\theta=3,\qquad \deg y\le3,\qquad
 h=m_s\ne0.
\tag{1}
\]
Here \(m=k_s\), so in particular \(m\ne0\) and \(m\notin\mathbf C\).
The conclusion is that this entire supplied sector is impossible.
The cases \(m_s=0\), including exact cubic \(y\), are outside the theorem.

The original data include an actual polynomial ring and global slice,
\[
 \begin{gathered}
 \mathcal B=\mathbf C[X,Y,Z,W]=\mathcal A[u_{\rm glob}],
 \qquad E u_{\rm glob}=1,\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
       \quad\hbox{is the entire initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_{\mathcal A}\ne0,\quad
 Na_0=Nt=Ns=0,\quad Nv_{\rm old}=1,\\
 L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
 [L:\mathbf C(t,s)]<\infty,\quad
 L[\mathcal A]=L[v_{\rm old}]=L[y,\sigma,\theta],\\
 \operatorname{Frac}\mathcal A=L(v_{\rm old})
       =\mathbf C(y,z_{\rm int},w),\qquad
 L[y,z_{\rm int},w]=L[v_{\rm old}].
 \end{gathered}
\tag{2}
\]
The intercept \(z_{\rm int}\) is the literal original \(Z\)-intercept.
The selected literal partial, original slice, both returns, genuine
moving levels and complete scalar equation remain required.

After the allowed finite coefficient extension \(L'\supset L\), use
the moving affine intrinsic parameter \(x=\rho v_{\rm old}+\zeta_0\),
with \(\rho\in L'^*\), to write
\[
 \sigma=x^2+c,\qquad
 \theta=ax^3+bx^2+dx+e,\qquad
 y=qx^3+y_2x^2+y_1x+y_0,\qquad a\ne0.
\tag{3}
\]
Every displayed coefficient lies in \(L'\). Both coefficient partials
are the commuting extensions fixing \(x\). Thus \(Nx=\rho\), not
necessarily one, and no square root is descended to the original field.
The polynomial \(y\) can be quadratic, linear, constant or zero; no
coefficient of it is assumed nonzero until a stated case split.
Write
\[
 p=m_t,\quad h=m_s,\quad k_1=k_t,\quad k_2=k_{tt},\quad
 F_0=\ker(\partial_s:L'\longrightarrow L').
\tag{4}
\]
The exact field \(F_0\) is finite over \(\mathbf C(t)\); it is not
assumed to equal that rational field. Its \(t\)-constant field is
\(\mathbf C\). We will also use directly the characteristic-zero fact
that an element algebraic over \(F_0\) is killed by \(\partial_s\).

## 2. Whole potentials, multiplier and polynomial return

The full actual rows and second potential are
\[
 \begin{split}
 Y&=y+\sigma X+tX^2,\\
 Z&=2ty+\sigma^2+k_1\sigma+m\theta+n
                              +(2t\sigma+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 F(P,V)&=\frac{k_2}{2}P^2+pPV+\frac h2V^2+n_tP+n_sV,\\
 G(U,P,V)&=\frac{\ell-(2P+k_1)U-F(P,V)}m,\qquad
 w=G(y,\sigma,\theta).
 \end{split}
\tag{5}
\]
The complete formal cubic relation is
\[
 \begin{split}
 H(U,P,V)={}&U^2+F_PU+F_VG
 +\frac{k_{ttt}}6P^3+\frac{p_t}2P^2V
 +\frac{h_t}2PV^2+\frac{h_s}6V^3\\
 &+\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
 -\ell_tP-\ell_sV,\qquad H(y,\sigma,\theta)=h_0\in L'.
 \end{split}
\tag{6}
\]
The level \(h_0\) is a genuine moving coefficient. Define formal
derivatives before evaluation:
\[
 \begin{gathered}
 f=H_U(y,\sigma,\theta),\qquad g=H_V(y,\sigma,\theta),\\
 D_f=\frac{2\sigma+k_1}{m},\quad
 B_f=\frac{2y+k_2\sigma+p\theta+n_t}{m},\quad
 \nu=\frac{p\sigma+h\theta+n_s}{m},\\
 A_\beta=4x^2y_t+2x\theta_x y_s+y_x^2
                         -2xc_t y_x-c_s y_x\theta_x,\\
 B_\beta=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
                  +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2.
 \end{gathered}
\tag{7}
\]
The whole denominator-free535 equations and scalar are
\[
 A_\beta=\kappa g,\qquad B_\beta=-\kappa f,\qquad
 \kappa\in L'^*,\qquad
 J_{t,s,x}(Y,Z,W)=-a_0^4/\rho\in L'^*.
\tag{8}
\]
Under the moving affine parameter change, the scalar scales by
\(\rho^{-1}\), the primitive-cross multiplier by \(\rho\), and
\(\kappa\) by \(\rho^{-2}\). No critical point \(2x=0\) or vanishing
gradient component is deleted.

The whole all-\(X\) polynomial return is also essential. Since
\(\mathcal B_{a_0}=\mathcal A_{a_0}[X]\), adjoining \(L'\) to the actual
equality and using (2) gives
\[
 L'[X,Y,Z,W]=L'[X,x].
\tag{9}
\]
This is an equality of the indicated subrings of the same overring.
It is not a replacement of the actual four-ring by a rational
coefficient-field parametrization.

## 3. The full divided-pair unit condition

We reproduce the part of555 needed here, with \(y\)'s degree-four
coefficient set to zero but every lower coefficient retained. Let
\(u=x_1+x_2\), \(z=x_1x_2\); this \(u\) is not the global slice.
For each polynomial take the polynomial divided difference
\(f^{[1]}=(f(x_1)-f(x_2))/(x_1-x_2)\), including its diagonal value.
Set
\[
 \begin{split}
 S_\sigma&=u^2-2z+2c,\\
 S_\theta&=a(u^3-3uz)+b(u^2-2z)+du+2e,\\
 S_y&=q(u^3-3uz)+y_2(u^2-2z)+y_1u+2y_0,\\
 Y_d&=q(u^2-z)+y_2u+y_1,\\
 \overline F_P&=k_2S_\sigma/2+pS_\theta/2+n_t,\qquad
 \overline F_V=pS_\sigma/2+hS_\theta/2+n_s,\\
 D(u)&=2u+ma,\quad
 N(u)=u^3+ma u^2+(2c+k_1+mb)u+md,\\
 P_{\rm pair}(u,z)&=N-Dz,\qquad
 \mathcal E(u,z)=S_y+\overline F_P
                      -\frac{S_\sigma+k_1}{m}\overline F_V.
 \end{split}
\tag{10}
\]
The exact identity from all three rows (5), before setting
\(P_{\rm pair}=0\), is
\[
 \begin{gathered}
 Y^{[1]}=Y_d+uX,\qquad
 Z^{[1]}-2tY^{[1]}=P_{\rm pair},\\
 mW^{[1]}\big|_{X=-Y_d/u}+u\mathcal E
       =-P_{\rm pair}(Y_d/u+\overline F_V/m).
 \end{gathered}
\tag{11}
\]
It is used on \(u\ne0\), without ever inverting \(x_1-x_2\).
The inverse polynomial for \(x\) from (9), applied to differences
at the same \(X\), makes
\((Y^{[1]},Z^{[1]},W^{[1]})\) the unit ideal. The ordered-pair lift
\[
 L'[u,u^{-1},z][x_1]/(x_1^2-ux_1+z),\qquad x_2=u-x_1
\tag{12}
\]
is free of rank two and faithfully flat, also at diagonal pairs.
Eliminating \(X\) in (11) therefore proves that \(\mathcal E\) is a
unit of \(L'[u,u^{-1},z]/(N-Dz)\).

Here are all coefficients of \(\mathcal E\), not just its top:
write \(S_0=u^2+2c\), \(T_0=au^3+bu^2+du+2e\),
\(v_0=3au+2b\), \(Q_0=S_0+k_1\), and
\(V_0=pS_0/2+hT_0/2+n_s\). These are temporary pair polynomials.
Then \(\mathcal E=E_0+E_1z+E_2z^2\), where
\[
 \begin{split}
 E_0={}&qu^3+y_2u^2+y_1u+2y_0
                    +k_2S_0/2+pT_0/2+n_t-Q_0V_0/m,\\
 E_1={}&-3qu-2y_2-k_2-pv_0/2
                         +\{Q_0(p+hv_0/2)+2V_0\}/m,\\
 E_2={}&-(2p+hv_0)/m.
 \end{split}
\tag{13}
\]
Put
\[
 \begin{gathered}
 u_*=-ma/2\ne0,\qquad
 \delta=N(u_*)=m\{d-a(2c+k_1)/2-mab/2+m^2a^3/8\},\\
 \mathcal U=E_0D^2+E_1DN+E_2N^2.
 \end{gathered}
\tag{14}
\]
The complete numerator has degree at most six and satisfies
\[
 \begin{split}
 \mathcal U_6&=[u^6]\mathcal U=-ha^2/2\ne0,\\
 \mathcal U_5&=-ma^3h-abh-ap-2q,\\
 \mathcal U_4&=-a(4abhm+2ach+ahk_1+3amp+5mq),\\
 \mathcal U(u_*)&=E_2(u_*)\delta^2,\qquad
 E_2(u_*)=3ha^2/2-2(p+hb)/m.
 \end{split}
\tag{15}
\]

If \(\delta\ne0\), Bezout for \(N,D\) gives the exact pair ring
\(L'[u,u^{-1},D^{-1}]\). Its units give
\[
 \mathcal U=\lambda u^{6-j}D^j,\qquad
 \lambda\in L'^*,\qquad 0\le j\le6.
\tag{16}
\]
The total exponent is six because \(\mathcal U_6\ne0\).
If \(j\ge1\), (15) also gives \(E_2(u_*)=0\).

If \(\delta=0\), retain the whole vertical component:
\[
 N=DM,\quad
 M=u^2/2+ma u/4+(2c+k_1+mb)/2-m^2a^2/8.
\tag{17}
\]
The pair ring is the fiber product of the graph \(z=M(u)\) and the
vertical line \(u=u_*\), meeting at their actual intersection.
A unit must restrict to units on both components. In particular,
\(E_2(u_*)=E_1(u_*)=0\), \(E_0(u_*)\ne0\), and the graph restriction
is a Laurent monomial. It is a polynomial, and
\(\mathcal U=D^2\mathcal E(u,M)\) has degree six, so necessarily
\(\mathcal E(u,M)=\lambda u^4\). Thus (16) holds with \(j=2\)
and \(E_2(u_*)=0\) also in this case. No vertical component has
been divided away.

The retained omitted-boundary condition from the same polynomial
return, before \(u\) is inverted, is \(ay_1-dq\ne0\). We do not
need it in the contradiction below and do not replace it by an
assumption on distinct pairs.

## 4. High whole equations collapse the pair numerator

The highest equations from (6)--(8) first give
\[
 h_s=\frac{3h^2}{m},\qquad
 a_s=-\frac{ha}{m},\qquad q_s=0,\qquad
 h_t=\frac{3hp}{m}+\frac{4hq}{ma}.
\tag{18}
\]
Here is their full support pedigree. The degree-nine coefficient
of the formal \(H\) after evaluation is
\(a^3(h_s/6-h^2/(2m))\). The degree-six coefficient of
\(B_\beta+\kappa f\) is \(6a(a_s+ha/m)\).
After the first identity, \([x^6]g=0\), so the degree-six
coefficient of \(A_\beta-\kappa g\) is \(6aq_s\).
Finally, the degree-eight coefficient of \(H\) is
\[
 \frac{a^2}{2}(h_t-3hp/m)-\frac{2haq}{m}.
\tag{19}
\]
The polynomials of degree at most two, including zero \(y\), satisfy
these same equations with \(q=0\). In particular
\[
 (ha^3)_s=0,\qquad (ma)_s=0.
\tag{20}
\]

Suppose \(j\ge1\) in (16), also including the vertical case \(j=2\).
Comparing the full degree-five coefficient with (15) gives
\[
 b=\frac{j-4}{4}ma^2-\frac ph-\frac{2q}{ah},\qquad
 E_2(u_*)=\frac{7-j}{2}ha^2+\frac{4q}{am}.
\tag{21}
\]
Since the latter expression must vanish, it follows that
\(q=-(7-j)mha^3/8\). Its genuine \(s\)-derivative, using (18)--(20),
is
\[
 0=-\frac{7-j}{8}h^2a^3,
\tag{22}
\]
which is impossible for \(1\le j\le6\). Thus the entire
\(\delta=0\) branch is excluded, and the nonvertical branch is forced
to have \(j=0\). Consequently
\[
 \delta\ne0,\qquad \mathcal U=-\frac{ha^2}{2}u^6.
\tag{23}
\]
The coefficients \(\mathcal U_5=\mathcal U_4=0\), with no lower
coefficient omitted, now give
\[
 b=-ma^2-\frac ph-\frac{2q}{ah},\qquad
 2c+k_1=4m^2a^2+\frac{mp}{h}+\frac{3mq}{ah}.
\tag{24}
\]
Differentiate these identities with the genuine
\(p_s=h_t\), \((k_1)_s=p\), and (18). The result is
\[
 b_s=ha^2,\qquad c_s=\frac{q}{2a}.
\tag{25}
\]
No assumption about \(p\) or \(q\) was used in this collapse.

## 5. Next whole equations and genuine mixed derivatives

For readability let \(H_7=[x^7](H(y,\sigma,\theta)-h_0)\),
\(\mathcal A_5=[x^5](A_\beta-\kappa g)\), and
\(\mathcal B_i=[x^i](B_\beta+\kappa f)\). After (18), their
complete relevant expressions are
\[
 \begin{split}
 H_7&=-\frac{1}{2m}
   (-4bhq+ahk_2+4ahy_2-am p_t+2ap^2+4pq),\\
 \mathcal A_5&=4q_t+6a(y_2)_s-\frac{2\kappa hq}{m},\\
 \mathcal B_5&=4a_t+6ab_s+
               \frac{6abh-2ah\kappa+10ap+20q}{m}.
 \end{split}
\tag{26}
\]
Thus \(H_7=0\) and (24)--(25) reduce the equations to
\[
 \begin{split}
 y_2&=\frac{bq}{a}-\frac{k_2}{4}
                    +\frac{mp_t}{4h}-\frac{p^2}{2h}-\frac{pq}{ah},\\
 \mathcal B_5&=4a_t+\frac{4ap+8q-2\kappa ha}{m}=0.
 \end{split}
\tag{27}
\]

The derivative of the first line is the genuine \(s\)-derivative.
In particular, use \((k_2)_s=p_t\), \(p_s=h_t\), and
\[
 \begin{split}
 (p_t)_s=(h_t)_t={}&
 \frac{3h_t p}{m}+\frac{3hp_t}{m}-\frac{3hp^2}{m^2}
 +\frac{4h_tq}{ma}+\frac{4hq_t}{ma}\\
 &-\frac{4hpq}{m^2a}-\frac{4hq a_t}{ma^2}.
 \end{split}
\tag{28}
\]
Substituting this full derivative and \(\mathcal B_5=0\) into
\(\mathcal A_5\) yields the exact expression
\[
 \mathcal A_5=\frac5m(2mq_t-\kappa hq).
 \quad\hbox{Hence}\quad
 q_t=\frac{\kappa hq}{2m},\qquad (y_2)_s=0.
\tag{29}
\]
The last equality follows by substituting the same identities into
the derivative in (27). Equation (29) is also valid for \(q=0\);
we did not divide by \(q\) to derive it.

The next entire multiplier coefficient, before using any special
value of \(d\) or its derivatives, is
\[
 \begin{split}
 \mathcal B_4={}&4b_t+6ad_s+2da_s+4bb_s-9a^2c_s+9aq\\
 &+\frac{8had+4hb^2+8pb+4k_2+16y_2-2\kappa(p+hb)}m.
 \end{split}
\tag{30}
\]
This includes all lower coefficients' possible contributions at this
degree. In particular it is extracted from the formal \(H_U\), not
from an on-level substitution differentiated afterwards.

## 6. The finite-field boundary parameter

Let
\[
 z_0=\frac{q}{mha^3},\qquad
 \xi=\frac{\delta}{m^3a^3}.
\tag{31}
\]
The symbol \(z_0\) here is a coefficient-field ratio, not a coordinate
or the pair-product variable \(z\). Equations (15), (23), and (24)
give
\[
 E_2(u_*)=\frac{ha^2}{2}(7+8z_0),\qquad
 7+8z_0\ne0,\qquad
 \xi^2=-\frac{1}{64(7+8z_0)}.
\tag{32}
\]
Indeed \(\mathcal U(u_*)\ne0\) and \(\delta\ne0\), so the first
factor cannot vanish. No additional root is adjoined to get \(\xi\):
it is the displayed element already in \(L'\).

Solving the defining formula for \(\delta\), using (24), gives
\[
 d=\left(\frac{11}{8}+\xi\right)m^2a^3+\frac{mq}{2h}.
\tag{33}
\]
All derivatives of this equation must retain the movement of
\(\xi\). In fact (18), (20), and (32) give
\[
 (z_0)_s=-\frac{hz_0}{m},\qquad
 \xi_s=\frac{4hz_0\xi}{m(7+8z_0)},\qquad
 d_s+\frac{hd}{m}=m^2a^3\xi_s-\frac q2.
\tag{34}
\]
This formula also holds at \(q=0\). Neither \(d\) nor
\(11/8+\xi\) was divided out.

## 7. The case \(q=0\), including zero y

Here \(z_0=0\), and \(\xi^2=-1/448\), so \(\xi\) is complex.
In particular (34) gives \(d_s=-hd/m\). The previous identities
specialize to
\[
 \begin{gathered}
 b=-ma^2-p/h,\quad b_s=ha^2,\quad c_s=0,\quad
 h_t=3hp/m,\\
 y_2=-k_2/4+mp_t/(4h)-p^2/(2h),\\
 b_t=-pa^2-2ma a_t-p_t/h+3p^2/(mh).
 \end{gathered}
\tag{35}
\]
The last equation is the genuine \(t\)-derivative of \(b\).
Substitution into the whole (30), retaining \(\kappa\), gives the
exact certificate
\[
 \mathcal B_4+2\kappa ha^2+2am\,\mathcal B_5=0.
\tag{36}
\]
Since both multiplier coefficients vanish, this forces
\(2\kappa ha^2=0\), contrary to \(a,h,\kappa\ne0\).
The argument applies to every degree at most two, including constant
and zero \(y\). It does not assume \(p\ne0\), \(d\ne0\), or any
nonzero lower coefficient.

## 8. The case \(q\ne0\)

Now (29) implies \(q_t\ne0\). Define the exact coefficient
\[
 \mathfrak j=\frac{\kappa ha}{q}
             =\frac{2(ma)q_t}{q^2}\in F_0^*.
\tag{37}
\]
Membership in \(F_0\) follows from \((ma)_s=q_s=0\) and the
commutation of the genuine coefficient partials. No rationality of
\(F_0\), nor descent of a square root, is involved.

Differentiate the full first equation of (24) in \(t\):
\[
 b_t=-pa^2-2ma a_t-\frac{p_t}{h}+\frac{ph_t}{h^2}
          -\frac{2q_t}{ah}
          +\frac{2q(a_t h+ah_t)}{a^2h^2}.
\tag{38}
\]
Use (18), (25), (27), (29), (34), and (38) in the entire
\(\mathcal B_4\) from (30). Its exact remaining expression is
\[
 \mathcal B_4=
 2ha^2(2z_0-1)\kappa
       +mha^4z_0\left(\frac{19}{2}
                            +\frac{24\xi}{7+8z_0}\right)=0.
\tag{39}
\]
The factor \(z_0\) is nonzero in this case. Dividing by
\(mha^4z_0\) and using (37) gives
\[
 2(2z_0-1)\mathfrak j+\frac{19}{2}
                     +\frac{24\xi}{7+8z_0}=0.
\tag{40}
\]
We have not divided by \(2z_0-1\). Solving only for the linear
appearance of \(\xi\) and using its full square equation (32)
produces the cleared polynomial identity
\[
 (7+8z_0)^3[\,4(2z_0-1)\mathfrak j+19\,]^2+36=0.
\tag{41}
\]
By (34), \((z_0)_s=-hz_0/m\ne0\). Thus \(z_0\) is transcendental
over \(F_0\): an algebraic element over the constants of this
derivation would be killed by it in characteristic zero.
But (41) is a polynomial in \(z_0\) over \(F_0\) whose leading
degree-five coefficient is \(32768\mathfrak j^2\ne0\).
This is a contradiction.

Both \(q\)-cases are impossible, completing the claimed exclusion
of the full sector (1). The vertical pair branch, the cases \(p=0\)
and \(d=0\), zero lower coefficients, and the finite coefficient
extension have all been retained.

## 9. Verification and limits

The complete direct inputs264,296,535 and555 were read before their
use. The pair proof uses the full polynomial inverse and its
faithfully flat ordered-pair lift. It never specializes an actual
coordinate at a moving coefficient-field root. The whole formal
potentials and formal gradients, not only selected leaders, are
printed in (5)--(8).

Fresh unsaved algebra independently reconstructed the whole \(H\),
\(H_U\), \(H_V\), \(A_\beta\), \(B_\beta\), and complete pair
numerator. It verified the raw gates (18)--(19), the entire
coefficients (26),(30), the genuine mixed derivative in (28), both
specializations (36),(39), the square elimination (41), and its
nonzero leading coefficient. Independent parent and peer outline
reconstructions agreed. These checks supplement the proof; they
are not an independent saved-source audit of this authored file.

No excess-degree exclusion, conic-family restriction or unproved
chart-entry reduction is used. The result concerns only the full
supplied chart with \(m_s\ne0\) and the directly imposed degree
bound on \(y\). It is not a recognition theorem for an arbitrary
nonlinear chart or an assertion of general cancellation.
No saved checker was executed, imported or compiled, no canonical
file was edited, and no novelty claim is made.
