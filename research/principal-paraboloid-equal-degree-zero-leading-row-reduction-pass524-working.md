# Equal higher degrees with a vanishing leading third row

Working result: retain the FULL actual principal chart264, nonzero
coupling m with m_s=0, and affine nonconstant intrinsic sigma=P.
Suppose theta and y have the same degree D>=3, with leaders a,r,
and the potential third row has vanishing degree-(D+1) coefficient
\(\omega=-(2r+m_ta)/m=0\).

Put p=m_t and R=y+p theta/2. A specific nonzero polynomial T of
degree at most two is defined below. The necessary degree triples
reduce to

| deg theta | deg R | deg T |
| --- | --- | --- |
| 3 | at most 1, including R=0 | 0 |
| 3 | 2 | 1 |
| 4 | 2 | 0 |

In every case m_tt=0 and p is a nonzero complex constant. This
is only a necessary reduction. None of the three remaining cases
is asserted to occur, to be recognized, or to satisfy the unused
lower equations automatically.

## 1. Full actual entry and the specified branch

Retain every actual hypothesis of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and unit gradient-minor conclusions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the universal identities in Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular
\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
 E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the FULL initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\quad
 L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\quad m=k_s\ne0,\quad m_s=0,\\
 \deg_v\sigma=1,\quad P=\sigma,\quad NP=\rho\in L^*,\quad
 O=L[P]=L[y,\sigma,\theta],\\
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w).
 \end{gathered}
\tag{1}
\]
Here z_int is the literal original Z-intercept Z at X=0, not its
corrected difference with 2ty. Both actual returns, the original
global slice, and the selected literal partial are retained.
The original slice is not assumed to be X/a_0.

The exact commuting coefficient partials on L extend those on
C(t,s) and fix P after this intrinsic reparameterization. The
literal rows and potentials are
\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-\mathcal F(P,\theta),\\
 \mathcal F(P,V)&=k_{tt}P^2/2+pPV+n_tP+n_sV,\qquad p=m_t,\\
 J_{t,s,P}(Y,Z,W)&=-a_0^4/\rho\in L^*.
 \end{aligned}
\tag{2}
\]
The symbols n and ell in this display are the retained potentials
in L; D below is the intrinsic degree, not a potential.

Add precisely
\[
 \theta=aP^D+\cdots,\quad y=rP^D+\cdots,\quad
 D\ge3,\quad a,r\in L^*,\qquad
 \omega=-\frac{2r+pa}{m}=0.
\tag{3}
\]
The expression omega is the degree-(D+1) coefficient of w in
(2), and also of the literal W. Thus
\[
 p\ne0,\qquad r=-pa/2,\qquad
 R:=y+(p/2)\theta\in L[P],\quad \deg R<D
\tag{4}
\]
when R is nonzero. In particular the m_t=0 branch is not silently
discarded: it is incompatible with (3) and r!=0. No actual
ambient coordinate is changed in defining R.

## 2. The retained full scalar and minor identities

Let H be the genuine formal third polynomial from264 and296:
\[
 \begin{aligned}
 G&=(\ell-(2P+k_t)U-\mathcal F(P,V))/m,\\
 H&=U^2+\mathcal F_PU+\mathcal F_VG
        +H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV,\\
 H(y,P,\theta)&=h_0\in L.
 \end{aligned}
\tag{5}
\]
All formal derivatives in U,P,V are taken before evaluation. Put
\[
 \begin{aligned}
 f&=H_U(y,P,\theta),\quad g=H_V(y,P,\theta),\quad
 D_f=(2P+k_t)/m,\\
 \nu&=(pP+n_s)/m,\quad
 \beta_f=(2y+k_{tt}P+p\theta+n_t)/m,\\
 \mathcal A&=y_t+\theta_Py_s+y_P^2,\\
 \mathcal B_1&=\theta_t+
              \theta_P(y_P+\theta_s+\nu)+\beta_f+D_fy_P.
 \end{aligned}
\tag{6}
\]
The universal494 argument, not its separate conic application,
gives
\[
 \begin{gathered}
 (f,g)L[P]=L[P],\qquad
 \mathcal A=\kappa g,\quad \mathcal B_1=-\kappa f,
 \quad \kappa\in L^*,\\
 \mathcal W=(\theta_P+D_f)g^2
       +(y_P-\theta_s-\nu)fg-y_sf^2\in L^*.
 \end{gathered}
\tag{7}
\]
These are complete polynomial identities from the full scalar,
including its nonzero constant-X coefficient. No coefficient of
a possibly moving scalar in L is set to zero except positive
powers of P, which cannot occur in an element of L.

For the present equal degrees, f has degree at most D, whereas
the degree-(2D-1) coefficient of B1 is D*a*a_s. All its other
terms have lower degree. Since 2D-1>D, (7) forces a_s=0.
Equation (4) then gives r_s=0, since p_s=0. The degree-2D
coefficient of the full H level is
\[
 r^2+par+(n_{ss}/2)a^2=0.
\]
After the three displayed formal contributions, every remaining
formal summand has evaluated degree at most D+2<2D. Consequently
\[
 a_s=r_s=0,\qquad n_{ss}=p^2/2.
\tag{8}
\]

Let F_0=ker_L(partial_s). This is a finite extension of C(t).
For example, differentiating the monic minimal polynomial of an
s-constant over C(t,s) forces all its coefficients into C(t).
Every finite collection of such constants generates an extension
of C(t) of degree at most [L:C(t,s)], since adjoining the
transcendental s preserves that degree. These uniform bounds
prove finiteness of the whole constant subfield. Its exact
t-derivative constants are C, by characteristic zero and the
joint-constant field of L. Neither F_0=C(t) nor L=F_0(s) is
assumed.

Exact subtraction in L, using (8), gives
\[
 \begin{gathered}
 k=ms+f_0,\qquad
 n=\frac{p^2}{4}s^2+n_1s+n_0,\qquad
 m,p,a,f_0,n_1,n_0\in F_0,\\
 q=m_{tt},\qquad
 \zeta=\frac{n_s-pk_t/2}{m}
       =\frac{n_1-pf_0'/2}{m}\in F_0.
 \end{gathered}
\tag{9}
\]
Primes on F_0 mean the exact original t partial at fixed s.
This is an integration already witnessed by the displayed
differences, not a rationality assumption.

## 3. The complete reduced polynomial system

Define the following polynomials in the independent intrinsic P:
\[
 \begin{aligned}
 B&=pP+n_s,\quad \gamma=2P+k_t,
       \quad F_{\rm base}=k_{tt}P^2/2+n_tP,\\
 L_2&=k_{tt}P+n_t-\gamma B/m,\\
 M_2&=qP^2/2+n_{ts}P-\ell_s-B^2/m,\\
 N_3&=k_{ttt}P^3/6+n_{tt}P^2/2-\ell_tP-h_0
                      +B(\ell-F_{\rm base})/m,\\
 T&=M_2-(p/2)L_2.
 \end{aligned}
\tag{10}
\]
In particular
\[
 \deg L_2=2,\quad [P^2]L_2=-2p/m\ne0,\quad
 \deg M_2\le2,\quad\deg N_3\le3,\quad\deg T\le2,\qquad
 [P^2]T=q/2,\quad [P]T=m\zeta'+(q/2)k_t.
\tag{11}
\]
Expanding the entire formal H, before imposing (8), gives
\(H-h_0=U^2+(pV+L_2)U+(n_{ss}/2)V^2+M_2V+N_3\).
Thus (8) and U=R-pV/2 cancel the quadratic V term exactly,
not just its leading evaluated coefficient. The full level and
evaluated gradients become
\[
 R^2+L_2R+N_3+T\theta=0,\qquad
 f=2R+L_2,\qquad g=(p/2)f+T.
\tag{12}
\]

To display the entire remaining scalar and minor system, put
\[
 \begin{aligned}
 K&=\theta_s-(p/2)\theta_P+R_P+\zeta,\\
 L_R&=R_s-(p/2)R_P+(p/2)\zeta,\\
 J_R&=(2R+k_{tt}P+n_t+\gamma R_P)/m,\qquad
 \mathcal C=\mathcal A+(p/2)\mathcal B_1.
 \end{aligned}
\tag{13}
\]
Substitution into (6),(7), retaining p_t=q, gives the exact
polynomial identities
\[
 \begin{aligned}
 \mathcal B_1&=\theta_t+\theta_PK+J_R=-\kappa f,\\
 \mathcal C&=R_t+R_P^2-(q/2)\theta+\theta_PL_R+(p/2)J_R
                       =\kappa T,\\
 \mathcal W&=-L_R f^2+
       (2R_P-K+(p/2)D_f)fT+(\theta_P+D_f)T^2\in L^*.
 \end{aligned}
\tag{14}
\]
For instance g-pf/2=T proves the multiplier in the second
line. In the third line the coefficient of f^2 is precisely
-L_R, including the term p*zeta/2. These identities retain
all lower coefficients and the moving potential derivatives.

## 4. The zero T case is impossible

Suppose T=0. Then g=pf/2, so the ideal statement in (7)
forces f to be a nonzero unit of L[P], hence f in L*.
Write f=2c, c in L*. Equation (12) gives
\[
 R=-L_2/2+c,\qquad c^2-L_2^2/4+N_3=0.
\tag{15}
\]
But the second polynomial has degree-four coefficient
-p^2/m^2, nonzero by (4), because N3 has degree at most three.
This is a contradiction. The zero-gradient alternatives were
included in the retained unit ideal, so no separate nonzero
gradient assumption is hidden here. We may henceforth put
\[
 T\ne0,\qquad \tau=\deg T\in\{0,1,2\}.
\tag{16}
\]

## 5. Excluding every residual degree greater than two

Suppose b=deg R>2 and write R=uP^b+lower terms, u in L*.
Recall b<D from (4). In the first equation of (12), R^2
has degree 2b, strictly larger than b+2 and three. The only
possible balancing term is T*theta. Therefore, with
t_tau=lc_P(T) in L*,
\[
 D+\tau=2b,\qquad u^2+a t_\tau=0.
\tag{17}
\]
This is the complete degree/parity constraint before using the
remaining scalar. In particular no division by q has occurred.

The first equation of (14) forces deg K<=1. If its degree were
at least two, theta_P K would have degree at least D+1,
uniquely exceeding theta_t, J_R and kappa f; their degrees are
at most D, b and b, respectively. This same bound on K also
holds later when deg R<=2, since D>=3.

If tau=0, then q=0 by (11), and (17) gives D=2b.
In the second equation of (14), any nonzero L_R would make
theta_P L_R have degree at least D-1, uniquely exceeding the
other terms, whose degrees are at most D-2. Thus L_R=0.
But then R_P^2 has uniquely highest degree 2b-2>b in that
equation, with nonzero coefficient b^2u^2, contradicting its
constant right side. This excludes tau=0 when b>2.

For tau=1 or2, the same equation forces
deg L_R<=tau-1. Otherwise theta_P L_R would have degree
at least D+tau-1, whereas the other terms have degree at most
D+tau-2. For tau=1 the q term is zero; for tau=2 its degree
is D and q/2=t_tau. At degree D+tau-2 the equation therefore
gives
\[
 b^2u^2-\mathbf1_{\{\tau=2\}}a t_\tau
       +Da\,[P^{\tau-1}]L_R=0,\qquad
 [P^{\tau-1}]L_R=
       \frac{b^2+\mathbf1_{\{\tau=2\}}}{D}\,t_\tau.
\tag{18}
\]
The right side kappa*T has lower degree here, since b>2.

Now use the ENTIRE third equation of (14). Its coefficient of
P^{D+2tau-1} is
\[
 \begin{aligned}
 &-4u^2[P^{\tau-1}]L_R+4bu^2t_\tau+Da t_\tau^2\\
 &\hspace{8mm}=-\frac{u^2t_\tau}{D}
       \left(\tau^2+4\mathbf1_{\{\tau=2\}}\right).
 \end{aligned}
\tag{19}
\]
Here f has exact degree b and leader 2u; the highest coefficient
of 2R_P-K+(p/2)D_f is 2bu because b-1>1. The two equalities
in (17) and (18) give the last line. It is -u^2t_tau/D for
tau=1 and -8u^2t_tau/D for tau=2, in either case nonzero.
Its positive P degree contradicts W in L*. This excludes all
b>2, including both parity possibilities in (17).

We have proved
\[
 \deg R\le2\quad\text{or }R=0.
\tag{20}
\]
This proof made no rationality or polynomial-in-s assumption on
any lower coefficient of R or T.

## 6. The exact remaining degree triples

In (12), the sum R^2+L2R+N3 now has degree at most four.
Since T and theta are nonzero, D+tau<=4. Thus
\[
 (D,\tau)\in\{(3,0),(3,1),(4,0)\},\qquad
 q=0.
\tag{21}
\]
The latter follows from [P²]T=q/2, not from a division by q.
Since p_s=0 and p_t=q=0, p is a nonzero complex constant.
Exact subtraction then gives m=pt+d_0 with d_0 in C.
We do not normalize p or d0 by an actual coordinate change.

Let u=[P²]R, allowing u=0 when R has smaller degree or is zero.
In the (3,1) and (4,0) cases, the degree-four coefficient of
(12) is
\[
 u(u-2p/m)+a t_\tau=0.
\tag{22}
\]
Consequently deg R=2 and u is neither zero nor 2p/m.
In fact u is also not p/m. To see this without assuming f
has degree two, suppose u=p/m, so deg f<=1. The second line
of (14) forces L_R to be constant for D=3 and to be zero for
D=4. The last line would then have its uniquely highest term
theta_P*T², of degree four in (3,1) or three in (4,0), with
nonzero coefficient D*a*t_tau². The other terms have strictly
smaller degree because deg K<=1. This contradicts the unit
minor. Thus in these two cases
\[
 \deg R=2,\qquad
 u\notin\{0,p/m,2p/m\}.
\tag{23}
\]

It remains to sharpen (D,tau)=(3,0). Equation (12) at P4 says
u(u-2p/m)=0. Thus f has exact degree two in both alternatives,
with leader -2p/m or 2p/m. The second line of (14) forces
L_R to be constant, since theta_P has degree two and every
other term has degree at most two. The degree-four coefficient
of the last line is then -L_R times the square of that nonzero
leader. Hence L_R=0.

Write R=uP²+vP+c_R, still allowing u=0. With L_R=0 and q=0,
the degree-two coefficient in the second line of (14) is exactly
\[
 u_t+4u^2+3pu/m=0.
\tag{24}
\]
If u=2p/m, its t derivative is -2p²/m² since p is constant,
and the left side of (24) equals 20p²/m², nonzero. Therefore
u=0. This proves deg R<=1, including R=0, in the first row of
the result table. All three rows are now justified.

## 7. Verification and remaining scope

The complete264,296 and494 sources were read before this work.
Only494's universal multiplier and gradient-unit conclusions are
used; no quadratic-theta parity statement or later conic theorem
is applied outside its scope. The exact field F0 remains finite
over C(t), not assumed rational. All comparisons are coefficients
in the intrinsic polynomial P; no unrestricted comparison of
unspecified algebraic functions as polynomials in s is made.

Fresh unsaved inline411ad8 reconstructed the full formal H and
all six identities comprising (12),(14), with arbitrary retained
lower terms. Every residual was zero. It independently checked
[P²]T=q/2 and the two terminal coefficients in (19). Fresh236b39
checked the entire degree-two coefficient (24), its value
20p²/m² in the nonzero alternative, and the exact quartic
contradiction in (15). These calculations supplement the uniform
degree arguments, rather than replace them with finite examples.
Fresh2148d0 also reconstructs the complete coefficient [P]T in
(11) and the unrestricted leading B1 coefficient used in (8),
with all residuals zero.

The potentials f0,n1,n0,ell and all lower coefficients not
explicitly constrained above remain in their exact fields. No
equation solves the entire remaining scalar system, and no
remaining row is claimed to be realized. The original coupling
m=0, non-affine sigma, unequal degrees, and nonzero omega are
outside this particular statement.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. There is no claim
of actual recognition, arbitrary chart entry, unrestricted
cancellation, novelty or external certification.
