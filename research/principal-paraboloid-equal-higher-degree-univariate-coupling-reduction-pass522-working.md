# Equal higher intrinsic degrees with univariate coupling

Working bounded necessary reduction: retain the FULL actual chart264,
the genuine levels and unit gradients of296, and the universal
multiplier of494. Suppose sigma is an affine intrinsic parameter P,
m=k_s is nonzero with m_s=0, and

\[
 \deg_Py=\deg_P\theta=N_\theta\ge3,\qquad
 y=rP^{N_\theta}+\cdots,\quad
 \theta=aP^{N_\theta}+\cdots,\quad a,r\in L^*,
 \qquad \omega:=-\frac{2r+m_ta}{m}\ne0.
\tag{1}
\]

Then N_theta is three or four. More precisely, the proof produces
q in the exact s-constant field, a polynomial R of degree at most
two, and a NONZERO polynomial A_theta such that

\[
 y=q\theta+R,\qquad
 N_\theta+\deg_P A_\theta\le4.
\tag{2}
\]

This neither excludes nor recognizes the remaining degrees three
and four. The hypotheses (1), including equal degrees and omega
nonzero, are not consequences asserted for all higher-degree
curves. No reduction of arbitrary cancellation data to this actual
chart or to affine sigma is claimed.

## 1. Full actual hypotheses and notation

Retain every actual hypothesis and both returns of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine formal H,Q and evaluated unit-gradient/minor conditions of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and Sections1--3 of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md).
In particular,

\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
 E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the ENTIRE original initial kernel},\\
 0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
 L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\qquad O=L[P],\quad P=\sigma,\quad NP=\rho\in L^*,\\
 \operatorname{Frac}A=L(P),\qquad
 L[X,Y,Z,W]=L[X,P],\qquad L[y,P,\theta]=L[P].
 \end{gathered}
\tag{3}
\]

The integer N_theta is never the selected derivation N or the
first potential n. The original global slice need not equal X/a_0.
The exact commuting coefficient partials on L hold P fixed.
Their joint constant field is C, and
F_0=ker(partial_s|L) is finite over C(t), not assumed equal to C(t).
All lower coefficients and moving levels remain arbitrary.

Put p=m_t, so p belongs to F_0 but MAY BE ZERO. The literal rows are

\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-\mathcal F(P,\theta),\\
 \mathcal F(P,V)&=\frac{k_{tt}}2P^2+pPV+n_tP+n_sV,\\
 J:=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
   &=-a_0^4/\rho\in L^*.
 \end{aligned}
\tag{4}
\]

In particular J is independent of P and X; it is not assumed to
have zero t or s derivative. We use only the retained genuine
levels, never an independently chosen quartic relation.

## 2. The actual positive-degree three-ring argument

Define the coefficient ratio

\[
 C_{\rm lead}:=\frac{2tr+ma}{r}\in L.
\tag{5}
\]

We prove that this ratio is complex. If its numerator vanishes,
C_lead=0 is already complex and the argument in this section is
unnecessary. Thus no positive-weight theorem is applied to a
degree-dropped Z. Suppose, for contradiction, that C_lead is
noncomplex. Since C is algebraically closed, it is transcendental
over C. It is also transcendental over K=C(X): X is transcendental
over L, so clearing denominators in any proposed K-relation and
comparing its coefficients in X would make C_lead algebraic over C.

Under this contradiction hypothesis the literal rows (4) have
EXACT positive degrees and leaders

\[
 (d_Y,d_Z,d_W)=(N_\theta,N_\theta,N_\theta+1),\qquad
 (Y_{N_\theta},Z_{N_\theta},W_{N_\theta+1})
   =(r,\,2tr+ma,\,\omega).
\tag{6}
\]

For Z, N_theta>=3 makes the explicit P^2 term lower. For W,
the only contributions in degree N_theta+1 are -2Py/m and
-pP*theta/m. This uses neither p nonzero nor an assumption about
the lower W coefficients.

Set

\[
 \mathcal R=K[Y,Z,W]=K^{[3]},\qquad F=L(X).
\tag{7}
\]

This is an ACTUAL polynomial three-ring because X is an actual
coordinate. It injects into F[P], and its fraction field is F(P):
indeed Frac(B)=L(P)(u_glob)=L(P)(X), using (3) and a_0!=0.
Also F is finite separable over K(t,s).

Extend N to B=A[u_glob] by Nu_glob=0 and define

\[
 \Delta=a_0N-(NX)E.
\tag{8}
\]

It preserves the actual ring, fixes X and kills L. On L[X,P] it
equals g_0*partial_P, with g_0=a_0*rho in L*. Thus its restriction
to R is a nonzero K-LND, and its degree filtration is P degree.
Local nilpotence follows from this polynomial overring; it is
not inferred merely because (8) is a difference of derivations.

Write A_D=ker_R Delta. This ring contains two algebraically
independent polynomial invariants over K. Explicitly, if
d=N_theta, then b_D=Delta^dY=d!*g_0^d*r is a nonzero invariant
in R and
v_D=Delta^{d-1}Y/b_D in R_(b_D) satisfies Delta(v_D)=1.
For f in R_(b_D), the finite sum
pi(f)=sum_j (-v_D)^j*Delta^j(f)/j! is killed by Delta.
The finite identity f=sum_i v_D^i*pi(Delta^i(f))/i! therefore gives
R_(b_D)=(A_D)_(b_D)[v_D]. Taking fraction fields yields

\[
 \operatorname{trdeg}_K A_D=2.
\tag{9}
\]

No global slice or finite generation of A_D is used.

### 2.1. The entire coordinate-initial kernel

Use fresh source variables and an independent initial parameter eta:

\[
 \begin{aligned}
 \phi:K[\mathsf Y,\mathsf Z,\mathsf W]&\longrightarrow F[\eta],\\
 (\mathsf Y,\mathsf Z,\mathsf W)&\longmapsto
 (r\eta^d,\,(2tr+ma)\eta^d,\,\omega\eta^{d+1}),\\
 \operatorname{wt}(\mathsf Y,\mathsf Z,\mathsf W)&=(d,d,d+1),
 \qquad d=N_\theta\ge3.
 \end{aligned}
\tag{10}
\]

Using derivative-normalized Delta leaders only rescales eta by
g_0, so (10) does not discard the original speed. The first two
images are algebraically independent over K. Their fraction field
contains their ratio C_lead, transcendental over K, and
r*eta^d is transcendental over F.

There is a nonzero relation among all three images. Choose a
nonconstant invariant from (9), and express it uniquely as a
polynomial in the actual Y,Z,W over K. Its source weighted degree
is positive because all three weights in (10) are positive.
Its evaluated P degree is zero, so its highest weighted component
maps to zero under phi. This supplies a nonzero relation without
any assumption that all three leaders already lie in F_0.

The image therefore has transcendence degree exactly two. The
ENTIRE kernel is a height-one prime in a polynomial UFD:

\[
 \ker\phi=(H_{\rm in}),\qquad
 H_{\rm in}\text{ irreducible and weighted homogeneous},\qquad
 D=\operatorname{wt}H_{\rm in}>0.
\tag{11}
\]

The kernel is graded; decomposing a generator into weight pieces,
each of which is divisible by that generator, shows it has a single
weight. Since the first two images are independent, H_in involves
mathsf W. Characteristic zero and irreducibility then imply
(H_in)_W is nonzero modulo H_in.

This is a three-variable source-initial kernel. It is neither the
original four-variable initial kernel in (3) nor an asserted
presentation of the entire associated graded ring of R.

### 2.2. An all-ring cofactor bound

Let T be the actual partial derivative partial_W of R, holding
K,Y,Z fixed. It extends to Frac(R)=F(P). Invert the COMPLETE
Jacobian in (4). Cofactors using the Y,Z rows show

\[
 T(t),T(s)\in F[P]_{\le 2d-1},\qquad
 T(P)\in F[P]_{\le 2d}.
\tag{12}
\]

Division by the nonzero J introduces no P denominator. For every
coefficient c in F, separability of F/K(t,s) gives
T(c)=c_t*T(t)+c_s*T(s). This is the equality of derivations into
F(P), even though T need not preserve F. Applying the product rule
to an arbitrary polynomial in F[P] therefore gives

\[
 \deg_P T(f)\le\deg_P f+2d-1\quad(T(f)\ne0).
\tag{13}
\]

In particular this holds on ALL of R. Since T preserves R,
iteration gives deg_P T^j(f)<=deg_P f+j(2d-1) whenever nonzero.
No coefficient-field parameter has been declared an actual
coordinate, and no stronger bound on T(P) is needed.

### 2.3. Derivative multiplicity and quadratic invariant growth

Let f be any nonconstant polynomial invariant and Q its unique
source polynomial. Write its weighted top, of weight M>0, as

\[
 Q_M=H_{\rm in}^{\,\ell}G,\qquad
 \ell\ge1,\quad H_{\rm in}\nmid G,\quad \ell D\le M.
\tag{14}
\]

The exact source derivative residue is
partial_W^ell(H_in^ell G)=ell!*G*((H_in)_W)^ell modulo H_in,
which is nonzero in the quotient domain. Its weight is M-(d+1)ell.
Every lower weight of Q differentiates to a smaller weight or zero.
By the FULL kernel statement (11), the remaining top evaluates
nontrivially, so the exact degree is

\[
 \deg_P T^\ell(f)=M-(d+1)\ell.
\tag{15}
\]

The iterated bound (13) and deg_P f=0 imply

\[
 \ell D\le M\le 3d\ell.
\tag{16}
\]

Thus D<=3d. Equality is impossible. Indeed, if D=3d, then every
nonconstant invariant has M=3d*ell and G in (14) has weight zero,
hence belongs to K. Let (A_D)_M be the vector space of invariants
of source weighted degree at most M. Each nonzero positive
filtered quotient is at most the one-dimensional span of a power
of H_in, and it can occur only at multiples of 3d. Consequently
dim_K(A_D)_M<=floor(M/(3d))+1.

By (9) choose two algebraically independent invariants f_1,f_2.
If c_D is the sum of their positive source weights, their
(j+1)^2 monomials f_1^i*f_2^k with 0<=i,k<=j are linearly
independent and all belong to (A_D)_(c_D*j). This quadratic lower
growth contradicts the linear upper bound. Therefore

\[
 D\le3d-1.
\tag{17}
\]

For weights (d,d,d+1), however, any homogeneous relation involving
mathsf W must have at least two distinct W-exponent blocks.
A single block W^j*G(Y,Z) has nonzero image because the first
two images are independent. If j_1<j_2 occur at the same weight,
then d divides (d+1)(j_2-j_1), hence d divides j_2-j_1.
Thus j_2>=d and D>=(d+1)j_2>=d(d+1).
For every d>=3 this exceeds 3d-1, contradicting (17).

This completes the standalone argument and proves

\[
 C_{\rm lead}\in\mathbb C.
\tag{18}
\]

The zero Z-leader case was already handled before (6). Positivity
was needed only under the noncomplex-ratio contradiction hypothesis.
No claim about zero-weight filtrations is made.

## 3. The leading coefficient and s-derivative gates

Since t is transcendental over C, C_lead-2t is nonzero. Define

\[
 q=\frac ra=\frac{m}{C_{\rm lead}-2t}\in F_0^*,\qquad
 u_q=2q+p\ne0.
\tag{19}
\]

Here omega=-a*u_q/m, so the last assertion is exactly the
retained nonzero hypothesis in (1). This does not require p!=0.

For completeness the universal polynomials needed from494 are

\[
 \begin{aligned}
 f&=H_U(y,P,\theta),\qquad g=H_V(y,P,\theta),\\
 \nu&=(pP+n_s)/m,\quad
 \beta_f=(2y+\mathcal F_P(P,\theta))/m,\quad D_f=(2P+k_t)/m,\\
 \mathcal A&=y_t+\theta_Py_s+y_P^2,\\
 \mathcal B_1&=\theta_t+\theta_P(y_P+\theta_s+\nu)
                         +\beta_f+D_fy_P,\\
 \mathcal A&=\kappa g,\qquad \mathcal B_1=-\kappa f,\qquad
 \kappa\in L^*.
 \end{aligned}
\tag{20}
\]

For m_s=0, f has degree at most N_theta. In B1, the sole possible
term in degree 2N_theta-1 is theta_P*theta_s, with coefficient
N_theta*a*a_s. Indeed theta_P*y_P has degree 2N_theta-2,
theta_P*nu and all the remaining terms have degree at most
N_theta. Since 2N_theta-1>N_theta, (20) gives

\[
 a_s=0,\qquad r_s=(qa)_s=0.
\tag{21}
\]

The full monic H level in the next section has coefficient
r^2+par+n_ss*a^2/2 in degree 2N_theta. All summands other than
y^2+p*theta*y+(n_ss/2)*theta^2 have degree at most
N_theta+2<2N_theta. Dividing by a^2 gives

\[
 n_{ss}=-2q(q+p).
\tag{22}
\]

No s-constant condition is imposed on lower coefficients of y or
theta, or on either potential.

## 4. The complete off-level monic decomposition

With U,P,V independent, let H_0=H-h_0 be the genuine third
level polynomial. The exact formal expression from264, with
m_s=0 and hence m_ss=m_ts=0, is

\[
 \begin{aligned}
 H_0={}&U^2+\mathcal F_P U+
   \frac{\mathcal F_V}{m}\bigl(\ell-(2P+k_t)U-\mathcal F\bigr)
   +\frac{k_{ttt}}6P^3+\frac{m_{tt}}2P^2V\\
 &+\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
   -\ell_tP-\ell_sV-h_0.
 \end{aligned}
\tag{23}
\]

Define the COMPLETE coefficient polynomials

\[
 \begin{aligned}
 L_2(P)&=k_{tt}P+n_t-\frac{(2P+k_t)(pP+n_s)}m,\\
 M_2(P)&=\frac{m_{tt}}2P^2+n_{ts}P-\ell_s
                         -\frac{(pP+n_s)^2}{m},\\
 N_3(P)&=\frac{(pP+n_s)(\ell-k_{tt}P^2/2-n_tP)}m
               +\frac{k_{ttt}}6P^3+\frac{n_{tt}}2P^2-\ell_tP-h_0.
 \end{aligned}
\tag{24}
\]

Their degrees are at most two, two and three respectively, including
when some or all leading coefficients vanish. Expanding (23)
BEFORE evaluating U,V gives

\[
 H_0=U^2+pUV+L_2U+\frac{n_{ss}}2V^2+M_2V+N_3.
\tag{25}
\]

This retains every lower coefficient and moving level. In particular
no formal derivative is replaced by a derivative of H_0 evaluated
on its zero set.

Set

\[
 R(P)=y-q\theta,\qquad \deg_PR<N_\theta,\qquad
 A_\theta(P)=u_qR+qL_2+M_2.
\tag{26}
\]

The zero R and constant R cases are allowed. Using (22), the
complete formal shear and its actual evaluation give

\[
 \begin{aligned}
 H_0(qV+R,P,V)&=A_\theta(P)V+R^2+L_2R+N_3,\\
 0&=A_\theta(P)\theta+R^2+L_2R+N_3.
 \end{aligned}
\tag{27}
\]

There is no residual V^2 term. If c=deg_P R>2, then u_q!=0
forces deg A_theta=c. The first term in the second line of
(27) has exact degree N_theta+c, strictly larger than
2c,c+2 and three, since c<N_theta. This is impossible. Hence

\[
 \deg_PR\le2,
\tag{28}
\]

where the zero polynomial has degree minus infinity.

## 5. The zero coefficient is excluded by the unit gradient

Suppose A_theta is identically zero. Equation (27) then also
gives the polynomial identity R^2+L_2R+N_3=0. By the COMPLETE
formal decomposition, not merely an evaluated relation,

\[
 H_0=(U-qV-R(P))\bigl(U+(q+p)V+L_2(P)+R(P)\bigr).
\tag{29}
\]

The first factor vanishes on the actual line. The other evaluates to

\[
 B_{\rm ev}=u_q\theta+L_2+2R,
 \qquad \deg_P B_{\rm ev}=N_\theta\ge3,
\tag{30}
\]

because u_q!=0 and (28) bounds the remaining summands by two.
Taking FORMAL U,P,V derivatives in (29) before evaluation, the
evaluated gradient is exactly

\[
 \bigl((H_0)_U,(H_0)_P,(H_0)_V\bigr)_{\rm ev}
       =B_{\rm ev}\,(1,-R_P,-q).
\tag{31}
\]

Thus its generated ideal in O=L[P] is (B_ev), a nonunit ideal.
This contradicts296's retained unit H-gradient ideal. Consequently

\[
 A_\theta\ne0.
\tag{32}
\]

No factor-recognition theorem or endpoint from324 is needed.
The argument does not assume irreducibility of H_0; it uses the
actual evaluated unit-gradient condition at the proposed factor.

Now (27),(28) show that A_theta*theta is a nonzero polynomial
equal to one of degree at most four. Therefore

\[
 \boxed{N_\theta+\deg_PA_\theta\le4,\qquad
        N_\theta\in\{3,4\}.}
\tag{33}
\]

For N_theta=4, A_theta must be a nonzero constant in L; for
N_theta=3 it may have degree zero or one. Neither possibility is
discarded. R can still be zero, constant, linear or quadratic.
These are only necessary restrictions, not realizations.

## 6. Verification and scope

The current actual264, genuine296 and universal494 sources have
been fully read. The complete source519 was reread to check the
actual cofactor, local-slice and growth licenses; Section2 supplies
the entire adapted argument and does not rely on an unsaved
generic three-ring lemma. Source521 is separate context, not
needed to assume the equal-degree hypothesis in (1).

Fresh unsaved inline calculation acf195 reconstructed the entire
formal expression (23), the decomposition (25), the shear (27),
the formal factorization boundary (29), and the identities for the
full high coefficients. A separate fresh1529ea recheck during
authoring returned zero for the whole decomposition, shear and
factor residual, and for the H, B1 and literal W leading
coefficients with unrestricted lower polynomials in degrees three
through six. These finite symbolic checks supplement the uniform
degree proofs and do not replace the field, kernel or growth
arguments.

Root independently identified and checked the same gradient-unit
endpoint after the original outline. Saved-source review is a
separate step after the author hold. No prior recognition ancestry
has been recursively recertified here.

All actual returns, the literal selected partial, the original
global slice, genuine moving levels and complete nonzero scalar
remain hypotheses. The proof includes p=0, a zero Z leader, and
every lower-degree R and A_theta boundary specified above. It
makes no assertion for omega=0, unequal degrees, m_s!=0,
nonaffine sigma, other projected curves or unrestricted chart
entry. No coordinate-field parameter is promoted to an ambient
coordinate, and no new field root is taken.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. This is not a
general cancellation result, a recognition theorem, a novelty
claim or an external certification.
