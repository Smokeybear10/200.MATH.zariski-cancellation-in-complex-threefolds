# Excluding the nonresonant affine profile by the minor and scalar identities

Working exclusion: under the entire actual264 moving-slope chart,
the normalized quadric profile (deg p,deg x,deg q)=(1,1,1) is
impossible when f''' is not 6nu'. The case f'''=0 is included.

The proof uses the complete genuine fourth potential and the exact
constant-scalar identity of296. In a graph parameter, the full minor
ideal has one generator. Its high coefficients and a differentiated
coefficient of the fourth potential force the coefficient that the
nonzero scalar requires to be nonzero to vanish. No coefficient-field
coordinate is promoted to an original complex coordinate.

## 1. Entire actual input and notation

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\\
Nv=1,\quad O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here u is the original polynomial slice. It is not replaced by X/a0,
and the definition of the selected N is not changed.

Use the exact coefficient partials on L. They commute, have joint
constants C, and initially fix v. Put F=ker_L(partial_s), finite
over C(t) but not assumed rational. Assume the hypotheses of
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md):
\[
k=s+f,\qquad n=\nu s+n_0,\qquad f,\nu,n_0\in F,\qquad
b=\nu'\ne0.
\tag{2}
\]
Primes on elements of F are their exact t-derivatives. Define
\[
\kappa=\frac{f'''}{6b}\in F,\qquad \kappa\ne1.
\tag{3}
\]
No zero or nonzero assumption on kappa is added until the two cases
are separated.

The polynomial quadric change of
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md)
is made only over L. Suppose its degrees are (1,1,1). Its p differs
from sigma by a coefficient in L, so P=sigma is an affine intrinsic
parameter and O=L[P]. The P^2 coefficient of its polynomial T2
is kappa, including when that coefficient is zero. Thus
\[
\begin{gathered}
y=aP+c,\qquad \theta=-\kappa P^2+B P+D,\\
A_1=f''-2\nu,\qquad E_0=\ell_s+\nu^2,\qquad
\lambda=a+A_1/2\ne0,\qquad
r=c+(n_t-\nu f')/2.
\end{gathered}
\tag{4}
\]
Initially a,c,B,D,lambda,r lie in L. The centered function of441 is
x=lambda P+r; its degree one proves lambda is nonzero.

Changing the parameter from v to P has triangular chain determinant
P_v=NP in L*. Hence the ORIGINAL calibrated determinant becomes
\[
\mathcal J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
            =-\frac{a_0^4}{NP}\in L^*.
\tag{5}
\]
From now on coefficient derivatives hold P fixed. Their action on
L, including on the moving levels, is unchanged. This is not an
ambient polynomial coordinate change.

## 2. The full minor has one generator in the graph parameter

Use the complete genuine H,Q and their levels from438:
\[
H(y,P,\theta)=h_0\in L,\qquad Q(y,P,\theta)=q_0\in L.
\tag{6}
\]
The two moving derivatives h0_t,h0_s are retained in Q. By296,
the three evaluated two-by-two gradient minors generate O.

All formal gradients below are evaluated after differentiation.
The third-potential normal gradients and the highest fourth-gradient
coefficients are
\[
H_U=2\lambda P+2r,\qquad H_V=bP-E_0,
\tag{7}
\]
\[
\begin{aligned}
Q_U={}&2b(\kappa-1)P^2+U_1P+U_0,\\
U_1={}&f''a+n_{tt}+2\ell_s-bf'+bB,\\
U_0={}&f''c+bD+f'\ell_s-\ell_t,\\
Q_V={}&d_2P^2+V_1P+V_0,\\
d_2={}&b'/2+\kappa\ell_{ss},\\
V_1={}&ba-\nu b-\ell_{ts}-\ell_{ss}B,\\
V_0={}&bc+\nu\ell_s-h_{0,s}-\ell_{ss}D .
\end{aligned}
\tag{8}
\]
These are the full evaluated gradients from438(8). In particular
their constant terms are not silently set to zero.

Differentiating(6) in P gives
\[
H_P=-aH_U-\theta_P H_V,\qquad
Q_P=-aQ_U-\theta_P Q_V,\qquad \theta_P=-2\kappa P+B.
\tag{9}
\]
Define the polynomial
\[
\mathcal W=H_UQ_V-H_VQ_U\in L[P].
\tag{10}
\]
The other two minors are -theta_P*mathcal W and -a*mathcal W.
Since their ideal is O=L[P], one has
\[
\boxed{\mathcal W\in L^*.}
\tag{11}
\]
This uses the full minor ideal, not a choice of one nonzero minor.

There is also an exact link to the entire scalar, not merely its
nonvanishing. The identity296(21), specialized to m=k_s=1, is
\[
H_V\mathcal J=-\det(R_H,R_Q,dy),\quad
R_H=H_U\,dP+H_P\,dt+H_V\,ds,\quad
R_Q=Q_U\,dP+Q_P\,dt+Q_V\,ds.
\tag{12}
\]
It remains valid after the moving affine parameter change because
both sides acquire the same Jacobian factor 1/(NP). Equations(9)
give
\[
R_H=H_U(dP-a\,dt)+H_V(ds-\theta_P\,dt)
\]
and the analogous expression for RQ. With
dy=y_t*dt+y_s*ds+a*dP, direct three-by-three expansion therefore gives
\[
\boxed{(bP-E_0)\mathcal J
       =\mathcal W\{y_t+a^2+\theta_P y_s\}.}
\tag{13}
\]
No evaluated H-gradient component has been divided out. The level
derivatives in the genuine Q are exactly those required for(12).

## 3. The high coefficients put lambda in the exact field F

Substituting(4) into the COMPLETE Q of438 gives
\[
[P^4]Q=\frac{b\kappa'-b'\kappa-2\kappa^2\ell_{ss}}4,
\tag{14}
\]
\[
[P^3]Q=Bd_2+2ab(\kappa-1)-\frac{bf''}{2}
               +b\kappa\nu+\kappa\ell_{ts}+\frac{n_{ttt}}6.
\tag{15}
\]
Here f''''=6(b'kappa+b*kappa') was used, not a constancy assumption
on kappa. As Q evaluates to its level q0 in L, both coefficients
vanish. The cubic coefficient of(10), using(7),(8),(11), is
\[
\boxed{\lambda(b'+2\kappa\ell_{ss})=2b^2(\kappa-1).}
\tag{16}
\]

If kappa=0, this gives b' nonzero and
lambda=-2b^2/b' in F*. If kappa is nonzero, put w=ell_ss.
Equation(14) gives
\[
w=\frac{b\kappa'-b'\kappa}{2\kappa^2}\in F.
\tag{17}
\]
Equation(16) then reduces to lambda*kappa'=2b*kappa*(kappa-1).
Since b,lambda,kappa,kappa-1 are all nonzero in this case, it also
proves kappa' is nonzero. Thus
\[
\lambda=\frac{2b\kappa(\kappa-1)}{\kappa'}\in F^*.
\tag{18}
\]
In BOTH cases lambda and a=lambda-(f''-2nu)/2 belong to F.
Consequently a_s=0. The coefficient of P in(13) now is
\[
\boxed{b\mathcal J=\mathcal W(a'-2\kappa c_s).}
\tag{19}
\]
By b,mathcal J,mathcal W nonzero, it follows that
\[
a'-2\kappa c_s\ne0.
\tag{20}
\]
We will contradict this without assuming that c is rational or
polynomial in s.

For use in each case, the P^2 coefficient of the centered third
relation gives
\[
\lambda^2+bB+\frac{n_{tt}-\nu f''}{2}
            -\frac{(f''-2\nu)^2}{4}+\kappa E_0=0.
\tag{21}
\]
Its exact s derivative, since lambda is now in F, is
\[
B_s=-\frac{d_2}{b},\qquad r_s=c_s+b/2,\qquad (E_0)_s=\ell_{ss}.
\tag{22}
\]

## 4. The zero-kappa case

Let kappa=0. Then f'''=0 and(16),(22) give
\[
b'\ne0,\qquad \lambda=-2b^2/b',\qquad B_s=-b'/(2b).
\tag{23}
\]
Differentiate the identically zero coefficient(15) in s. All its
terms other than B*d2 and n_ttt/6 have zero s derivative, since
a,nu,b,f'' lie in F and kappa=0. Remembering
(n_ttt)_s=b'', this yields
\[
0=-\frac{(b')^2}{4b}+\frac{b''}{6},
\qquad 2bb''=3(b')^2.
\tag{24}
\]
No condition on ell_ss was imposed or needed here.

Now a=lambda-f''/2+nu and f'''=0, so direct differentiation gives
\[
a'=\lambda'+b
   =-3b+\frac{2b^2b''}{(b')^2}
   =\frac{b\{2bb''-3(b')^2\}}{(b')^2}=0.
\tag{25}
\]
Every denominator here was proved nonzero in(23). Equation(25)
contradicts(20) when kappa=0. No integration in a rational ansatz
or actual normalization is needed.

## 5. The nonzero-kappa case

Now kappa, kappa-1 and kappa' are all nonzero, by(3),(18).
Retain w from(17). Then
\[
d_2=\frac{b\kappa'}{2\kappa}
   =\frac{b^2(\kappa-1)}{\lambda}\ne0,\qquad
B_s=-\frac{\kappa'}{2\kappa}.
\tag{26}
\]
Differentiate the identically zero coefficient(15) in s. This is
differentiation in the exact field L, NOT extraction of an undefined
s coefficient. As d2,w,a,lambda lie in F and
ell_tss=w', the result is
\[
0=-\frac{d_2^2}{b}+\kappa w'+\frac{b''}{6}
 =\kappa w'+\frac{b''}{6}-\frac{b(\kappa')^2}{4\kappa^2}.
\tag{27}
\]
Substitute(17), differentiating it in t with every moving term retained.
Equivalently,
\[
\boxed{\Omega:=12b'\kappa\kappa'+6b\kappa\kappa''
                   -15b(\kappa')^2-4b''\kappa^2=0.}
\tag{28}
\]

The quadratic coefficient of the polynomial mathcal W is also zero.
From(7),(8), this exact equation is
\[
0=2\lambda V_1+2r d_2-bU_1+2b(\kappa-1)E_0.
\tag{29}
\]
Differentiate(29) in s, still without assuming c is polynomial.
Use(22), V1_s=-w'-w*B_s, and
U1_s=b'+2w+b*B_s. The result simplifies to
\[
0=2d_2c_s+4bw(\kappa-1)-2\lambda w'
                              +\frac{2\lambda w d_2}{b}.
\tag{30}
\]
Since d2 is nonzero, (26) turns this into
\[
c_s=\frac{\lambda^2w'}{b^2(\kappa-1)}-\frac{3\lambda w}{b}.
\tag{31}
\]
The only divisions are by the already nonzero b,lambda,kappa-1
and d2. In particular no hypothesis on c_s is inserted.

The final elimination is an exact rational identity. Differentiate
(18) and (17), and use a'=lambda'-b(3kappa-1):
\[
\begin{aligned}
\lambda'&=\frac{2b'\kappa(\kappa-1)}{\kappa'}
          +2b(2\kappa-1)
          -\frac{2b\kappa(\kappa-1)\kappa''}{(\kappa')^2},\\
w'&=\frac{b'\kappa'}{\kappa^2}
        +\frac{b\kappa''}{2\kappa^2}
        -\frac{b(\kappa')^2}{\kappa^3}
        -\frac{b''}{2\kappa}.
\end{aligned}
\tag{32}
\]
Substitution of(31),(32), before imposing Omega=0, gives
\[
\boxed{a'-2\kappa c_s=-\frac{\kappa-1}{(\kappa')^2}\Omega.}
\tag{33}
\]
Thus (28) contradicts(20). This excludes the second case and proves
the nonresonant affine-profile exclusion.

## 6. Exact scope and verification

Every use of the scalar in this proof is an identity or consequence
of the full original determinant. In particular(13) is transported
from296 with the entire affine-parameter chain factor; it is not a
claim about a selected formal coefficient system realizing an actual
chart. The proof retains the original slice X=a0*u+x0 and the original
selected N. It does not set x0=0 or place X/a0 in the original ring.

The field F remains exact and finite over C(t). The argument requires
neither its rationality, a square root of kappa, nor an integration
of the differential equation(28). Kappa=0, the possible initial
kappa'=0, and all denominators are explicitly treated. Kappa=1 is
outside the stated scope and is handled separately by447.

The complete296 source was freshly read through EOF before this
derivation;438 and441 were fully read in the current workstream.
Fresh unsaved d4f061 rebuilt (14),(15),(16) from the complete438
primitive with arbitrary formal jets. Fresh b40bc9 retained generic
literal row derivatives as an additional consistency check.
Fresh633e6c independently reconstructed the differentiated equation
(29), the conversion (27)--(28), the zero-kappa derivative gate,
and the exact determinant wedge in(13). Fresh8d4f74 verified the
precise rational identity(33) and both identities in the zero-kappa
case, with every residual zero. These checks supplement the written
graph-unit, parameter-calibration and exact-field arguments.

No saved checker was executed, imported, compiled or rerun. No earlier
proof or canonical index was edited. No remaining profile is recognized
or realized, and no unrestricted cancellation, arbitrary-entry, novelty
or formal-certification assertion is made.
