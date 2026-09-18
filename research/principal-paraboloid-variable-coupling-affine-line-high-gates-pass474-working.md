# Variable coupling on an affine projected line: high gates and a zero-direction family

Working result: in the full actual principal chart264, restrict to a
birational projected line with nonconstant sigma and variable coupling
\(m=k_s\notin\mathbb C\). The genuine third and fourth potentials give
the zero-safe differential system (16) below. Its highest constant
scalar coefficient is redundant, including every zero branch.

When the directional derivative \(\beta=m_t+\mu m_s\) vanishes, the
system integrates to the exact coefficient family (25). This is a
necessary coefficient reduction, not an exclusion or a realization.
The lower potentials, lower scalar coefficients and original return
conditions are not solved by this note.

## 1. Actual entry and the intrinsic parameter

Retain the complete actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the two genuine levels of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the birational projected-line hypothesis of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the entire initial kernel},\qquad
a_0=EX\ne0,\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
K=L(v)=\mathbb C(y,z,w_{\rm int}),\quad L[y,z,w_{\rm int}]=O.
\end{gathered}
\tag{1}
\]
The coefficient partials commute, have joint constant field
\(\mathbb C\), and the literal selected partial and original slice
are retained. The current frontier additionally has irreducible
\(H-h_0\) over \(L\); the calculations below do not use that
irreducibility and do not transfer a reducible-surface endpoint.

Assume the projected curve is a line, its function-field projection
has degree one, and sigma is nonconstant. By325 all three intrinsic
functions are affine. Consequently \(P=\sigma\) is a polynomial
parameter of \(O\), and
\[
y=\lambda P+r,\qquad \theta=\mu P+h,\qquad
\lambda,\mu,r,h\in L,\qquad NP=\rho\in L^*.
\tag{2}
\]
Both slopes may vanish. Hereafter coefficient derivatives on \(O\)
fix \(P\). They agree with the original derivatives on \(L\), but
need not fix the former parameter \(v\). The exact chain rule gives
\[
J_P(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
=-\frac{a_0^4}{\rho}\in L^*.
\tag{3}
\]
This is not the assertion \(NP=1\), and \(P\) is not the original
slice. In particular \(X=a_0u+x_0\), with its original intercept,
has not been replaced by \(a_0u\).

## 2. The complete potentials used for the high coefficients

For formal independent variables \(U,P,V\), set
\[
\begin{aligned}
\mathcal F&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
g&=\frac{\ell-(2P+k_t)U-\mathcal F}{m},\qquad m=k_s\ne0,\\
H&=U^2+\mathcal F_PU+\mathcal F_Vg
 +H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV.
\end{aligned}
\tag{4}
\]
Here \(H_j(a;P,V)=\sum_{i=0}^j
a_{t^{j-i}s^i}P^{j-i}V^i/((j-i)!i!)\). The actual level is
\(H(y,P,\theta)=h_0\in L\). The entire corrected fourth potential
has formal gradients
\[
\begin{aligned}
Q_U&=H_P-\frac{2P+k_t}{m}H_V+\frac{\mathcal F_V}{m}H_U,\\
Q_P&=H_t-h_{0,t}-\frac{2U+\mathcal F_P}{m}H_V
                       +\frac{\mathcal F_V}{m}H_P,\\
Q_V&=H_s-h_{0,s},\qquad Q(y,P,\theta)=q_0\in L.
\end{aligned}
\tag{5}
\]
The formal coefficient partials in (5) hold \(U,P,V\) fixed.
Both moving levels are retained; in particular \(h_{0,t},h_{0,s}\)
are not set to zero. The constant level \(q_0\) does not affect
positive intrinsic coefficients. These are296's full gradients,
not an arbitrary quartic chosen to contain the line.

For a directly reconstructible complete primitive, the same gradients
are obtained from
\[
\begin{aligned}
\widehat Q={}&\frac{k_{tt}}2U^2+
 (\partial_PH_3(k)+\partial_PH_2(n)-\ell_t)U\\
&+(m_tU+H_2(m)+H_1(n_s)-\ell_s)g+\frac{m_s}{2}g^2\\
&+H_4(k)+H_3(n)-H_2(\ell)-h_{0,t}P-h_{0,s}V.
\end{aligned}
\tag{5a}
\]
Every Taylor form in (5a) has the arguments \((P,V)\). Its value
at the formal origin is
\(-\ell_s\ell/m+m_s\ell^2/(2m^2)\in L\); subtracting that value
normalizes \(Q(0,0,0)=0\) and only shifts its coefficient level.
Thus the term \(g^2\), all arbitrary \(n,\ell\) derivatives and
both derivatives of the moving third level remain present.

Define frozen directional Taylor sums
\[
\begin{aligned}
\mathcal K_j&=\sum_{i=0}^j\binom ji\mu^i k_{t^{j-i}s^i}
                         &&(j=2,3,4),\\
\beta&=m_t+\mu m_s,\qquad
\mathcal M_2=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\\
\mathcal M_3&=m_{ttt}+3\mu m_{tts}+3\mu^2m_{tss}+\mu^3m_{sss},\qquad
\mathcal N_1=m_{ts}+\mu m_{ss}.
\end{aligned}
\tag{6}
\]
The powers of \(\mu\) in (6) are held fixed in these sums.
They are not powers of the actual derivation
\(\mathcal D=\partial_t+\mu\partial_s\).

The exact quadratic coefficient of the intercept \(w_{\rm int}\)
and two auxiliary coefficients are
\[
\omega=-\frac{2\lambda+\mathcal K_2/2}{m},\qquad
B_2=\frac{\mathcal M_2}{2}+m_s\omega,\qquad
C_3=\omega\mathcal N_1+\frac{\mathcal M_3}{6}.
\tag{7}
\]
In fact the complete intercept is
\[
\begin{aligned}
w_{\rm int}&=\omega P^2+w_1P+w_0,\\
w_1&=-\frac{2r+k_t\lambda+\beta h+n_t+n_s\mu}{m},\\
w_0&=\frac{\ell-k_tr-m_sh^2/2-n_sh}{m}.
\end{aligned}
\tag{8}
\]
No division by \(\lambda,\mu,\beta,\omega\), or \(B_2\) occurs.

## 3. The two levels and their primitive minor

Substitution in the full formulas (4),(5) gives
\[
H_3^{\rm ev}:=[P^3]H_{\rm ev}
 =\beta\omega+\frac{\mathcal K_3}{6}=0,\qquad
Q_4^{\rm ev}:=[P^4]Q_{\rm ev}
 =\frac{\mathcal K_4}{24}
   +\frac{\omega\mathcal M_2}{2}
   +\frac{m_s\omega^2}{2}=0.
\tag{9}
\]
For the second equality, the homogeneous quartic of \(Q\) is
one quarter of \(UQ_U+PQ_P+VQ_V\)'s homogeneous quartic.
Thus (5) gives this coefficient without discarding any lower
terms of the genuine potential. Direct expansion also gives
the following complete leading-gradient ledger:
\[
\begin{array}{c|c}
\text{coefficient}&\text{value}\\ \hline
[P^2](H_U)_{\rm ev}&-2\beta/m\\
[P^2](H_V)_{\rm ev}&B_2-\beta^2/m\\
[P^3](Q_U)_{\rm ev}&-2B_2/m\\
[P^3](Q_V)_{\rm ev}&C_3-\beta B_2/m.
\end{array}
\tag{10}
\]
It follows that
\[
[P^5](H_UQ_V-H_VQ_U)_{\rm ev}
=\frac2m(B_2^2-\beta C_3).
\tag{11}
\]
There is an exact unit justification for setting this coefficient
to zero. Differentiating both levels in \(P\) gives
\(H_P=-\lambda H_U-\mu H_V\) and
\(Q_P=-\lambda Q_U-\mu Q_V\) after evaluation.
Hence all three evaluated minors are multiples, by coefficients
in \(L\), of \((H_UQ_V-H_VQ_U)_{\rm ev}\).
Their ideal is the unit ideal by296, so that polynomial itself
is a nonzero element of \(L\). Therefore
\[
\boxed{B_2^2=\beta C_3.}
\tag{12}
\]
This argument uses the derivative \(P_P=1\) of the intrinsic
parameter. It does not remove the speed \(\rho\) from (3).

## 4. Exact one-forms, with zero branches retained

Write \(\kappa=\mathcal D\mu\), and use \(d\) for the
coefficient differential in \(t,s\). Frozen sums and actual
derivatives satisfy
\[
\begin{gathered}
\mathcal D\mathcal K_2=\mathcal K_3+2\beta\kappa,\qquad
\mathcal D\mathcal K_3=\mathcal K_4+3\mathcal M_2\kappa,\\
(\mathcal K_2)_s=\mathcal M_2+2\beta\mu_s,\qquad
(\mathcal K_3)_s=\mathcal M_3+3\mathcal M_2\mu_s,\qquad
\beta_s=\mathcal N_1+m_s\mu_s.
\end{gathered}
\tag{13}
\]
Differentiating (7), and then using the first level in (9), gives
\[
\begin{aligned}
m\mathcal D\omega+2\mathcal D\lambda
                  +\beta(\kappa-2\omega)&=0,\\
m\omega_s+2\lambda_s+\beta\mu_s+B_2&=0.
\end{aligned}
\tag{14}
\]
For example the first left side before imposing the level is
\(-3H_3^{\rm ev}\). Applying \(\mathcal D\) to that level
and subtracting four times \(Q_4^{\rm ev}\) gives the first
identity below. Its s derivative gives the second:
\[
\begin{aligned}
\beta\mathcal D\omega+B_2(\kappa-2\omega)&=0,\\
\beta\omega_s+B_2\mu_s+C_3&=0.
\end{aligned}
\tag{15}
\]
Equivalently the full zero-safe high system is
\[
\boxed{\begin{aligned}
2d\lambda+m\,d\omega+
 \beta(d\mu-2\omega\,dt)+B_2(ds-\mu\,dt)&=0,\\
\beta\,d\omega+B_2(d\mu-2\omega\,dt)
                         +C_3(ds-\mu\,dt)&=0,\\
B_2^2&=\beta C_3.
\end{aligned}}
\tag{16}
\]
Multiplying the first form by \(B_2\) and subtracting \(\beta\)
times the second proves, without division,
\[
2B_2\,d\lambda=(\beta^2-mB_2)\,d\omega.
\tag{17}
\]

## 5. The highest constant scalar is redundant

This redundancy is checked in the original literal rows, including
every moving coefficient. After subtracting \(2t\) times the
Y differential row from the Z row, their exact matrix at fixed X is
\[
\begin{pmatrix}
\lambda_tP+r_t+X^2&\lambda_sP+r_s&\lambda+X\\
(j+2X)P+d_0+k_tX&b_0P+e_0+mX&2P+k_t+m\mu\\
\omega_tP^2+(w_{1,t}+\mu_tX)P+w_{0,t}+h_tX&
\omega_sP^2+(w_{1,s}+\mu_sX)P+w_{0,s}+h_sX+X^2&
2\omega P+w_1+\mu X
\end{pmatrix},
\tag{18}
\]
where
\[
\begin{aligned}
j&=m\mu_t+2\lambda+k_{tt}+m_t\mu,&b_0&=m\mu_s+\beta,\\
d_0&=mh_t+2r+m_th+n_t,&e_0&=mh_s+m_sh+n_s.
\end{aligned}
\]
Its \(X^0P^4\) coefficient is exactly
\[
[X^0P^4]J_P=2(\lambda_s\omega_t-\lambda_t\omega_s).
\tag{19}
\]
It vanishes already from (16). If \(B_2\ne0\), use (17).
If \(B_2=0,\beta\ne0\), (12) gives \(C_3=0\), and the
second form in (16) gives \(d\omega=0\). If
\(B_2=\beta=0\), the first form gives
\(2d\lambda+m\,d\omega=0\), which again makes the wedge
zero. These cases include zero or constant \(\lambda,\omega\).
Thus (19) is not an extra independent obstruction. The lower
coefficients of the full nonzero scalar (3) remain required.

## 6. Integrating the beta-zero branch in its exact field

Assume \(\beta=0\). Because \(m\notin\mathbb C\), this forces
\(m_s\ne0\): otherwise \(m_t=0\) too. Equation (12) forces
\(B_2=0\), without any division. Also
\[
0=\mathcal D\beta=\mathcal M_2+m_s\mathcal D\mu,
\qquad B_2=0
\quad\Longrightarrow\quad \mathcal D\mu=2\omega.
\tag{20}
\]
The first form in (16) is now the entire two-component identity
\(2d\lambda+m\,d\omega=0\). Its exterior derivative gives
\(dm\wedge d\omega=0\). Since \(\mathcal Dm=0\) and
\(m_s\ne0\), evaluation on \((\mathcal D,\partial_s)\)
forces \(\mathcal D\omega=0\), and then
\(\mathcal D\lambda=0\).

The pair \((t,m)\) is a separating coefficient basis: its
Jacobian against \((t,s)\) is \(m_s\ne0\), so it is
algebraically independent and \(L/\mathbb C(t,m)\) is finite.
The exact coefficient derivations in this basis are
\[
\dot{\ }=\partial_t|_m=\mathcal D,
\qquad {}'=\partial_m|_t=m_s^{-1}\partial_s,
\qquad \mathscr F=\ker_L\mathcal D.
\tag{21}
\]
They commute by uniqueness of extensions through a finite
separable field extension. The field \(\mathscr F\) is a finite
extension of \(\mathbb C(m)\), not necessarily equal to it.
Indeed differentiating the monic minimal polynomial over
\(\mathbb C(t,m)\) of a \(\mathcal D\)-constant shows that
all its coefficients have zero t derivative. Thus every such
constant is algebraic over \(\mathbb C(m)\). Finite subextensions
have degrees bounded by \([L:\mathbb C(t,m)]\), because t
is transcendental over this algebraic constant extension; this
bounds the degree of their union as well. Finally the prime
constants in \(\mathscr F\) are exactly \(\mathbb C\).

We have obtained
\[
\lambda,\omega\in\mathscr F,\qquad
2\lambda'+m\omega'=0,\qquad \dot\mu=2\omega.
\tag{22}
\]
For a complete integration define the coefficient Legendre
expression \(\mathcal L=k-ms\). Because \(k_s=m\),
\[
\dot{\mathcal L}=k_t,\qquad \mathcal L'=-s,
\qquad
\ddot{\mathcal L}=k_{tt}+\mu m_t
 =\mathcal K_2=-4\lambda-2m\omega.
\tag{23}
\]
The middle equality for \(\mathcal K_2\) uses \(\beta=0\),
not an identification of frozen and actual directional powers.
Integrating twice by subtracting an explicit quadratic, the
remainders have zero dot derivative. Therefore there are
\(C_1,C_0\in\mathscr F\) with
\[
\mathcal L=-(2\lambda+m\omega)t^2+C_1t+C_0.
\tag{24}
\]
Differentiate in m, use (22), then recover \(k=\mathcal L+ms\)
and \(\mu=\dot s\). The resulting necessary family is
\[
\boxed{\begin{aligned}
s&=\omega t^2-C_1't-C_0',\\
\mu&=2\omega t-C_1',\\
k&=-2\lambda t^2+(C_1-mC_1')t+C_0-mC_0',\\
\lambda,\omega,C_1,C_0&\in\mathscr F,\qquad
2\lambda'+m\omega'=0,\\
\partial_m s&=\omega't^2-C_1''t-C_0''\ne0.
\end{aligned}}
\tag{25}
\]
The final nonzero condition is essential: it equals \(1/m_s\).
No antiderivative outside the exact field was chosen. The constants
\(C_1,C_0\) in (24) are existing elements of its exact dot-constant
field. Since m is nonzero and the joint constants are complex,
\[
\lambda\in\mathbb C\quad\Longleftrightarrow\quad
\omega\in\mathbb C.
\tag{26}
\]
In particular \(\lambda=0\) or \(\omega=0\) is permitted;
neither was divided out in the derivation.

## 7. Forward checks and the unresolved actual conditions

Formula (25), with its nonzero basis derivative, reconstructs
\(k_s=m\), \(\beta=0\), \(B_2=0\), and
\(\mathcal K_2=-4\lambda-2m\omega\).
The actual derivative identities (13) give
\(\mathcal K_3=0\), \(\mathcal M_2=-2m_s\omega\), and
\(\mathcal K_4=12m_s\omega^2\). These verify both high
levels (9); (22) verifies the complete high one-form system.
Such forward identities do not construct actual coordinates or
verify the lower coefficients of (4),(5),(18).

This note proves only necessary restrictions within the specified
nonconstant-sigma affine projected-line branch. It does not solve
the remaining constraints on \(n,\ell,r,h\), the two levels,
the lower nonzero scalar, or the original polynomial and strong
field returns. It does not cover constant sigma, claim that
\(\beta\) must vanish, identify \(L=\mathscr F(t)\), or promote
the coefficient basis \((t,m)\) to an actual complex polynomial
coordinate change. No recognition conclusion follows here.

The full296 and325 sources were reread before authoring; full264
was retained with its actual calibration. Fresh unsaved algebra
reconstructed all three gradients from a full polynomial primitive,
the two level leaders, all four entries of (10), the complete
coefficient (11), the literal scalar (19), and the forward family
identities. The written derivations supply the zero-case and exact
field arguments. No saved checker was executed, imported, compiled
or rerun. No earlier source or canonical file was edited.
