# The zero-direction variable-coupling affine-line branch is empty

Working theorem: retain the full actual chart264 and the birational
projected-line hypothesis of325. If sigma is nonconstant and
\(m=k_s\notin\mathbb C\), then
\[
\boxed{\beta=m_t+\mu m_s\ne0.}
\tag{1}
\]
Here \(y=\lambda\sigma+r_{\rm old}\) and
\(\theta=\mu\sigma+h\) are the affine intrinsic data. The proof
excludes the entire beta-zero family of474 by the original nonzero
scalar. It does not exclude beta nonzero, constant sigma, nonlinear
projected curves, or arbitrary chart entry.

## 1. Actual entry and the exact beta-zero coefficient field

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and scalar of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the affine reduction of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_0],\qquad E=\partial_{u_0},\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
X=a_0u_0+x_0,\quad x_0\in A,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
0\ne\mathscr N=[u_0^4]\partial_Z|_A\in\operatorname{LND}(A),\quad
\mathscr Na_0=\mathscr Nt=\mathscr Ns=0,\quad
L=\operatorname{Frac}\ker_A\mathscr N,\\
[L:\mathbb C(t,s)]<\infty,\qquad
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w_{\rm int}],\quad
\mathscr Nv_0=1,\\
\operatorname{Frac}A=L(v_0)=\mathbb C(y,z,w_{\rm int}).
\end{gathered}
\tag{2}
\]
The original slice, literal selected partial, both returns and
joint coefficient constant field \(\mathbb C\) are retained.
The birational projected-line assumption and nonconstant sigma give
\[
P=\sigma,\quad O=L[P],\quad\mathscr NP=\rho\in L^*,\qquad
y=\lambda P+r_{\rm old},\quad \theta=\mu P+h,\quad
w_{\rm int}=\omega P^2+w_1P+w_0.
\tag{3}
\]
The calibrated determinant is
\(J_{t,s,P}(X)=-a_0^4/\rho\), not the determinant with speed
artificially set to one.

Suppose for contradiction that \(\beta=0\). The fully read
[474, Section6](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md)
proves \(m_s\ne0\) and supplies the exact separating basis
\[
\dot{\ }=\partial_t|_m=\partial_t|_s+\mu\partial_s|_t,
\qquad {}'=\partial_m|_t=m_s^{-1}\partial_s|_t,
\qquad F=\ker_L\dot{\ }.
\tag{4}
\]
These partials commute, \(F/\mathbb C(m)\) is finite, and the
prime constants of F are exactly \(\mathbb C\). The resulting
family is
\[
\begin{aligned}
s&=\omega t^2-C_1't-C_0',&
\mu&=2\omega t-C_1',\\
k&=-2\lambda t^2+(C_1-mC_1')t+C_0-mC_0',&
2\lambda'+m\omega'&=0,\\
\lambda,\omega,C_1,C_0&\in F,&s'&\ne0.
\end{aligned}
\tag{5}
\]
No equality \(F=\mathbb C(m)\) or \(L=F(t)\) is used.

If \(\omega'=0\), then \(\omega\in\mathbb C\), and(5)
also gives \(\lambda\in\mathbb C\). The fully read actual
complex-slope exclusion
[477](principal-paraboloid-variable-coupling-complex-slope-exclusion-pass477-working.md)
excludes that case, including zero slopes. We therefore assume
\[
\upsilon:=\omega'\ne0.
\tag{6}
\]
The symbol \(\upsilon\) is a coefficient derivative, not a slice.

## 2. A complete intrinsic shift and the forced n family

Define existing coefficient functions
\[
\mathsf A=C_1-mC_1',\quad M=-C_1',\quad
\phi=C_0-mC_0',\quad \chi=-C_0'.
\]
They belong to F and satisfy
\[
\mathsf A'=mM',\qquad \phi'=m\chi',\qquad
C_1=\mathsf A-mM,\qquad C_1'=-M.
\tag{7}
\]
Make only the intrinsic, X-dependent parameter change
\[
\xi=P+t(X-\lambda),\qquad r=r_{\rm old}+\lambda^2t.
\tag{8}
\]
This is not an ambient coordinate map. The complete literal rows are
\[
\begin{aligned}
Y&=(X+\lambda)\xi+r,\\
Z&=\xi^2+\mathsf A\xi+G+\phi X,\\
W&=\omega\xi^2+b\xi+c+HX+MX\xi+\chi X^2,
\end{aligned}
\tag{9}
\]
where, with no intercept derivative discarded,
\[
\begin{aligned}
G&=2tr_{\rm old}+mh+n+\lambda t\mathsf A-\lambda^2t^2,\\
b&=w_1+2\omega\lambda t,\qquad
c=w_0+\lambda t w_1+\omega\lambda^2t^2,\\
H&=h-tw_1+M\lambda t.
\end{aligned}
\tag{10}
\]
In particular these are the original Y,Z,W, not newly chosen
polynomials with similar leading terms. The original slice makes
X transcendental over \(L(P)\), and(8) is an invertible polynomial
change over \(L[X]\). Thus X and xi are algebraically independent
over L. At fixed X the parameter
Jacobian from \((t,s,P)\) to \((t,m,\xi)\) is \(m_s\), so
\[
J_{t,m,\xi}(X)=-\frac{a_0^4}{\rho m_s}\in L^*.
\tag{11}
\]
The coefficient of \(\xi^3\) in the full determinant of(9) is
\(-\upsilon(2\dot r+m\dot b)\). The intercept identity474(8) gives
\[
w_1=-\frac{2r_{\rm old}+k_t\lambda+\dot n}{m},\qquad
k_t=-(4\lambda+2m\omega)t+C_1,
\]
where this \(k_t\) is the original fixed-s derivative. Therefore
\[
b=-\frac{2r}{m}
-\frac{\dot n-(6\lambda^2+4m\omega\lambda)t+\lambda C_1}{m}.
\tag{12}
\]
By(6), the cubic scalar coefficient forces
\[
\ddot n=6\lambda^2+4m\omega\lambda,\qquad
n=(3\lambda^2+2m\omega\lambda)t^2+N_1t+N,\quad N_1,N\in F.
\tag{13}
\]
Here N is a coefficient function, distinct from the selected
derivation \(\mathscr N\) in(2). This integration subtracts the
displayed quadratic from the existing
n, then subtracts its remaining linear term. It introduces no
antiderivative outside L. Equations(10),(12),(13) give the exact
identities
\[
b=B-\frac{2r}{m},\qquad H=\frac{G-N}{m},\qquad
B=-\frac{\lambda C_1+N_1}{m}\in F.
\tag{14}
\]
For example, before(13), \(G-mH=n-t\dot n+
(3\lambda^2+2m\omega\lambda)t^2\); after(13) it equals N.

## 3. The zero intercept-speed branch and the exact new basis

Put \(L_0=\lambda+m\omega\). First suppose \(\dot r=0\),
without changing coefficient basis. In the full determinant of(9),
using(14), the \(\xi^2\) coefficient and(6) give
\[
\dot c=L_0\dot G/m.
\]
If \(\dot G=0\), then \(\dot c=0\), and the entire first
column of the derivative matrix is zero. This contradicts(11).
Otherwise its \(X^2\) coefficient becomes
\[
-\frac{\dot G}{m^2}
\bigl(G-N+mN'+m^2\chi'L_0\bigr)=0.
\tag{15}
\]
It forces G to belong to F, again contradicting \(\dot G\ne0\).
Thus
\[
\dot r\ne0.
\tag{16}
\]
Now \((r,m)\) is a separating coefficient basis, since its
Jacobian against \((t,m)\) is \(\dot r\). On L the new
partial \(\partial_r|_m\) equals \(\dot{\ }/\dot r\).
Its kernel is still F. The new \(\partial_m|_r\) agrees with
the prime derivative on F, and the two new partials commute.
Hereafter subscripts r,m refer to this new basis; a prime still
denotes the unambiguous derivative on F. In particular
\[
J:=J_{r,m,\xi}(X)=-\frac{a_0^4}{\rho m_s\dot r}\in L^*.
\tag{17}
\]
It is independent of X and xi, but it is not presumed independent
of r. The variables r and m are algebraically independent, and
\(L/\mathbb C(r,m)\) is finite.

We will use that F is relatively algebraically closed in L.
Indeed if an element z of L is algebraic over F, differentiate
its monic minimal polynomial with \(\partial_r\). Its coefficients
are killed, and separability gives \(\partial_r z=0\). Hence
\(z\in\ker_L\partial_r=F\). This proves the needed assertion;
it is not an assumption that the full extension is rational.

## 4. The complete six-coefficient determinant

The exact matrix of(9) in the new basis is
\[
\begin{pmatrix}
1&-m\upsilon\xi/2&X+\lambda\\
G_r&mM'\xi+G_m+m\chi'X&2\xi+\mathsf A\\
-2\xi/m+c_r+G_rX/m&
\upsilon\xi^2+b_m\xi+c_m+H_mX+M'X\xi+\chi'X^2&
2\omega\xi+b+MX
\end{pmatrix}.
\tag{18}
\]
All derivatives of b and H here are the derivatives of(14).
For a compact complete ledger put
\[
\begin{aligned}
v&=G_r,& z&=G_m,&
K_1&=mM-\mathsf A-mc_r,\\
Q_1&=\lambda v-\mathsf A,& T_1&=b-\lambda c_r,&
E_1&=B'+2r/m^2,\qquad H_1=G-N+mN'.
\end{aligned}
\]
Expansion of(18) has exactly the following possible support:
\[
\begin{array}{c|l}
X^2&\chi'K_1-vH_1/m^2\\
X\xi&v((mM-\mathsf A)\upsilon/2+E_1)
       +M'K_1+2H_1/m^2+2\chi'L_0\\
\xi^2&\upsilon(L_0v-mc_r)+2M'L_0-2E_1\\
X&-Q_1H_1/m^2+zK_1/m+v c_m+\chi'mT_1\\
\xi&Q_1E_1+m\upsilon(bv-\mathsf A c_r)/2
       +mM'T_1+2zL_0/m-2c_m\\
1&Q_1c_m+T_1z.
\end{array}
\tag{19}
\]
The five positive-monomial rows vanish. The final row must be
nonzero by(17). Thus the ledger includes, rather than omits, the
scalar whose eventual vanishing will be the contradiction.

The \(\xi^2\) row integrates exactly in r:
\[
c=\frac{L_0G}{m}
 +\frac{2(M'L_0-B')r}{m\upsilon}
 -\frac{2r^2}{m^3\upsilon}+K,\qquad K\in F.
\tag{20}
\]
Subtracting the right side from c gives an existing r-constant;
this does not presume that c was rational in r.

## 5. The high scalar forces an affine G, with its zero slope retained

Use the \(\xi^2\) row of(19) to solve for \(E_1\), and then
the \(X\xi\) row to solve for \(H_1\). Substitution in the
\(X^2\) row gives the exact factorization
\[
0=\frac14\bigl(\upsilon v^2+2M'v+4\chi'\bigr)
                 \bigl(K_1+L_0v\bigr).
\tag{21}
\]
The second factor, using(20), is
\[
K_1+L_0v
=-C_1-\frac{2(M'L_0-B')}{\upsilon}
             +\frac{4r}{m^2\upsilon}\ne0.
\tag{22}
\]
It is nonzero because its r derivative is
\(4/(m^2\upsilon)\ne0\). The first factor therefore vanishes.
It is a nonzero quadratic polynomial in v over F, so v is
algebraic over F. The relative algebraic-closedness proof in
Section3 gives
\[
v\in F,\qquad G=vr+g,\quad g\in F.
\tag{23}
\]
Now the r coefficient of the \(X^2\) row is
\((4\chi'/\upsilon-v^2)/m^2\). Together with(21) this gives
\(4\chi'=\upsilon v^2\) and
\(v(\upsilon v+M')=0\).
If \(v\ne0\), this proves \(M'=-\upsilon v\).
If \(v=0\), then \(\chi'=0\), and the \(X\xi\) row has
r coefficient \(4M'/(m^2\upsilon)\), which forces \(M'=0\).
Thus uniformly, without dividing by v,
\[
M'=-\upsilon v,\qquad \chi'=\frac{\upsilon v^2}{4}.
\tag{24}
\]
The constant part of the same \(X\xi\) equation is exactly
\[
g=N-mN'
 +\frac{m^2v}{4}
    \bigl(\upsilon vL_0+2B'-\upsilon C_1\bigr).
\tag{25}
\]
These statements include \(v=0\), when \(g=N-mN'\).

## 6. Lower coefficients force complex integration constants

At this point all coefficients in(9) are polynomials in r over F:
use(20),(23),(25). Coefficient comparisons in r are now licensed,
since r is transcendental over F. This was not assumed before
those equations were proved.

Substitute(20),(23)--(25) into the complete matrix(18), still
retaining the derivatives \(\upsilon',v',B'',N'',K'\).
Its indicated lower coefficients are
\[
[r^2\xi]J=-\frac{4(m\upsilon'+3\upsilon)}{m^4\upsilon^2},
\qquad
\left.[r^2X]J\right|_{m\upsilon'+3\upsilon=0}
=\frac{4v'}{m^3\upsilon}.
\tag{26}
\]
Both vanish by(17). Consequently
\[
\upsilon=\frac{a}{m^3},\quad a\in\mathbb C^*,\qquad
v\in\mathbb C.
\tag{27}
\]
For the first assertion, the existing element \(m^3\upsilon\)
has zero prime derivative and lies in F. The second uses the
same constant field. The nonzero a follows from(6).

Integrating (5),(7),(24) by explicit subtraction gives
\[
\begin{aligned}
\lambda&=\lambda_0+\frac{a}{2m},&
\omega&=\omega_0-\frac{a}{2m^2},\\
M&=M_0+\frac{av}{2m^2},&
\mathsf A&=A_0+\frac{av}{m},\\
\chi&=\chi_0-\frac{av^2}{8m^2},&
\phi&=\phi_0-\frac{av^2}{4m},
\end{aligned}
\tag{28}
\]
where all six displayed subscript-zero constants are complex.
They may vanish. In particular \(C_1=\mathsf A-mM\) continues
to satisfy \(C_1'=-M\).

After(27),(28), the remaining \(r\xi\) coefficient is
\[
[r\xi]J=
\frac{4}{m^2\upsilon}
       \bigl(mB''+2B'-\upsilon v\lambda_0\bigr).
\tag{29}
\]
It therefore vanishes precisely when the bracket vanishes.
Integrating this equation inside F gives
\[
B=B_0-\frac{B_1}{m}+
           \frac{av\lambda_0}{2m^2},\qquad B_0,B_1\in\mathbb C.
\tag{30}
\]
Indeed \((m^2B')'=av\lambda_0/m^2\), so
\(m^2B'+av\lambda_0/m=B_1\) is a complex constant, followed
by the explicit second subtraction. No division by v or
\(\lambda_0\) is used.

## 7. A full final determinant identity, not just selected coefficients

Keep N and K as arbitrary elements of F. Keep(20),(23),(25)
as the definitions of c,G,g, and use(27),(28),(30). Set
\[
\begin{aligned}
\mathcal R_N&=N''-\frac{av(4A_0m+3av)}{8m^4},\\
K_*&=\frac{av(A_0\omega_0-B_0+M_0\lambda_0
                         -\lambda_0v\omega_0)}{4m^2}
       -\frac{a\lambda_0^2v^2}{4m^3}
       +\frac{\lambda_0(N-mN')}{m^2},\\
\mathcal R_K&=K'-K_*,\\
Z_1&=A_0-mM_0-\frac{2mB_1}{a}
       +\frac{av}{2m}-2mv\omega_0-\frac{4mr}{a}.
\end{aligned}
\tag{31}
\]
Both residuals \(\mathcal R_N,\mathcal R_K\) belong to F.
Direct substitution in the
entire literal matrix(18), or all six rows of(19), gives the
polynomial identity
\[
\boxed{
J=\mathcal R_N\bigl(Z_1X-L_0Q_1-mT_1\bigr)
  +\mathcal R_K\bigl(vX-2\xi+Q_1\bigr).
}
\tag{32}
\]
Here \(Q_1=\lambda v-\mathsf A\) and
\(T_1=b-\lambda c_r\) are exactly their earlier definitions.
Identity(32) retains both the constant scalar and every moving
coefficient derivative of N and K. It is an identity before
either residual is set to zero.

The xi coefficient of the nonzero scalar must vanish, so
\(\mathcal R_K=0\). The X coefficient then says
\(\mathcal R_NZ_1=0\). But
\((Z_1)_r=-4m/a\ne0\), hence \(Z_1\ne0\) and
\(\mathcal R_N=0\). Equation(32) now gives \(J=0\),
contradicting(17).

This final contradiction includes v zero. It does not require
integrating N or K, declaring them rational functions, setting
their moving derivatives to zero, or comparing an undefined
coefficient in a non-polynomial field element.

## 8. Scope and verification

The beta-zero branch with \(\omega'=0\) is excluded by the
actual complex-slope theorem477. Sections2--7 exclude its
complement \(\omega'\ne0\). These cases prove(1) under the
stated actual birational projected-line entry. The result is an
exclusion, not recognition or construction of an actual frame.
No claim is made about beta nonzero or unrestricted cancellation.

The complete held474 and477 sources and the writing guide were
read before authoring. The original264/296/325 licenses and
calibration are retained, not replaced by a formal polynomial
family. Fresh unsaved reconstruction7e7aef verifies the initial
cubic gate and the complete six-coefficient ledger. Reconstruction
f8a061 verifies the factorization(21), 24b5dc checks the full lower
coefficient gates before integration, and d12d05 checks the final
constraints with arbitrary N,K retained. Fresh851736 reconstructs
the complete literal determinant and verifies the entire identity
(32). Written exact-field arguments above justify the coefficient
comparisons, integrations and every zero branch.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. This working note
does not claim formal certification, human expert verification,
historical novelty or a solution beyond its explicit hypotheses.
