# Excluding the zero-transverse-coupling cubic lower-degree sector

Working bounded theorem: retain the FULL actual264/296/535 chart,
with noncomplex coupling m, intrinsic sigma of degree two, theta
of degree three, and y of degree at most three. Then m_s cannot
vanish identically. The proof includes zero or lower-degree y,
both pair-curve components, and a possibly zero fourth coefficient
of the actual W row.

This is an exclusion within the supplied actual chart. It is not
an entry theorem, recognition of another sector, rationality of a
coefficient field, or unrestricted cancellation. No actual coordinate
transformation is used after the initial finite intrinsic
reparameterization, which is not an ambient coordinate change.

## 1. Full actual data and the exact coefficient field

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u_{\rm glob}],
\qquad E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,
\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_{\mathcal A},
\qquad Na_0=Nt=Ns=0,\qquad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,
\qquad [L:\mathbb C(t,s)]<\infty,
\qquad L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\qquad L[y,z_{\rm int},w]=L[v].
\end{gathered}
\tag{1}
\]
Here z_int is the literal Z-intercept. Both returns, the original
slice, the selected literal partial, and the genuine moving H and
Q levels remain required.

Use the finite intrinsic normalization spelled out in
[553, Section 1](principal-paraboloid-quadratic-sigma-higher-theta-degree-bound-pass553-working.md).
If the original quadratic sigma has leading coefficient rho squared,
adjoin rho to L and put x=rho(v-v0), where v0 is its center. Write
\[
\begin{gathered}
L'=L(\rho),\quad \sigma=x^2+c,\quad
\theta=ax^3+bx^2+dx+e,\quad a\ne0,\\
y=qx^3+y_2x^2+y_1x+y_0,\qquad
Nx=\rho\in(L')^*,\\
J_{t,s,x}(Y,Z,W)=-a_0^4/\rho\in(L')^*,
\qquad \kappa=\kappa_v/\rho^2\in(L')^*.
\end{gathered}
\tag{2}
\]
All four y coefficients are initially allowed to vanish. The
coefficient partials are the exact commuting extensions of those
on C(t,s), extended to fix x. Moving-center and moving-scale terms
are therefore retained. Source535's two multiplier expressions
scale by rho to the power minus two, so their identities still hold
at the critical point x=0. No division by sigma_x is used.

Suppose, for contradiction,
\[
m=k_s\notin\mathbb C,\qquad h=m_s=0,
\qquad p=m_t\ne0.
\tag{3}
\]
The last nonvanishing follows because the common constants of the
two exact partials in L' are C. Put F0=ker(partial_s on L'). It is
finite over C(t), not assumed equal to C(t). Thus m,p and all their
t derivatives belong to F0. An element killed by both partials is
complex. These are exact finite-field constant statements, not
choices of rational parametrizations.

Write k_j=partial_t to the j of k, and write n for the second
coefficient potential. The full rows and second potential are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_1\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_1)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=k_2P^2/2+pPV+n_tP+n_sV.
\end{aligned}
\tag{4}
\]
All coefficients n,ell and their genuine derivatives are retained.
In particular k_{1,s}=p, k_{2,s}=p_t, k_{3,s}=p_{tt}.

## 2. Full formal polynomial and the first coefficient equations

With U,P,V independent, set
\[
\begin{aligned}
\mathfrak w&=\{\ell-(2P+k_1)U-\mathcal F(P,V)\}/m,\\
H&=U^2+\mathcal F_PU+\mathcal F_V\mathfrak w
 +k_3P^3/6+p_tP^2V/2+n_{tt}P^2/2+n_{ts}PV
 +n_{ss}V^2/2-\ell_tP-\ell_sV,\\
H(y,\sigma,\theta)&=h_0\in L',\qquad
f=H_U^{\rm ev},\quad g=H_V^{\rm ev}.
\end{aligned}
\tag{5}
\]
Formal derivatives are taken BEFORE evaluation. In particular
\[
g=py+n_{ss}\theta+(p_t/2-p^2/m)\sigma^2
 +(n_{ts}-2pn_s/m)\sigma-\ell_s-n_s^2/m.
\tag{6}
\]
Both f and g have degree at most four in x.

For beta=2x put nu=(p sigma+n_s)/m,
D_f=(2sigma+k1)/m, and B_f=(2y+k2sigma+p theta+n_t)/m.
The complete identities of535 are
\[
\begin{aligned}
\mathcal A_\beta&=4x^2y_t+2x\theta_xy_s+y_x^2
                           -2xc_ty_x-c_sy_x\theta_x=\kappa g,\\
\mathcal B_\beta&=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
                  +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2
                  =-\kappa f.
\end{aligned}
\tag{7}
\]
Denote by A_j and B_j the x-j coefficients of the two residuals
in (7), and by H_j the x-j coefficient of H(y,sigma,theta)-h0.
Their degree-six coefficients first give 6a a_s=6a q_s=0.
Thus a,q belong to F0, including the possibility q=0 at this stage.
The full next coefficients are
\[
\begin{aligned}
A_5&=4q_t+6a(y_2)_s=0,\\
B_5&=4a_t+6ab_s+10(2q+ap)/m=0,\\
H_7&=-2pq/m+a(p_t/2-p^2/m)=0,\\
H_6&=q^2+paq-2py_2/m+a^2n_{ss}/2
                  +b(p_t/2-p^2/m)+k_3/6-pk_2/(2m)=0.
\end{aligned}
\tag{8}
\]
These are coefficients of (5)--(7) with every lower term present.
The moving level h0 contributes to none of these positive powers.

## 3. The full pair-unit condition and its two possible degrees

The actual localization and both returns in (1) imply
L'[X,Y,Z,W]=L'[X,x], as in
[555](principal-paraboloid-cubic-pair-unit-and-longitudinal-exclusion-pass555-working.md).
For independent x1,x2 put u=x1+x2,z=x1*x2. Here u is a pair sum,
not the global slice. Define
\[
\begin{aligned}
S_\sigma&=u^2-2z+2c,\\
S_\theta&=a(u^3-3uz)+b(u^2-2z)+du+2e,\\
S_y&=q(u^3-3uz)+y_2(u^2-2z)+y_1u+2y_0,\\
\mathcal E&=S_y+k_2S_\sigma/2+pS_\theta/2+n_t
 -\frac{S_\sigma+k_1}{m}(pS_\sigma/2+n_s),\\
D&=2u+ma,\qquad
N(u)=u^3+ma u^2+(2c+k_1+mb)u+md.
\end{aligned}
\tag{9}
\]
Write E=E0+E1 z+E2 z squared. Direct expansion gives
\[
\begin{aligned}
E_2&=-2p/m\ne0,\\
E_1&=-3qu-2y_2-k_2-p(3au+2b)/2
                      +(2pu^2+4pc+pk_1+2n_s)/m,\\
\mathcal U&=E_0D^2+E_1DN+E_2N^2,\\
\deg_u\mathcal U&\le5,\qquad
[u^5]\mathcal U=-ap-2q,\qquad
[u^4]\mathcal U=-ma(3ap+5q).
\end{aligned}
\tag{10}
\]
The displayed E in (9) defines its entire constant coefficient E0,
so U is the complete numerator, not a leading approximation.

Here is the exact return license for its use. Polynomial divided
differences of the three rows in (4) generate the unit ideal, by
dividing the polynomial inverse for x. No x1-x2 is inverted, so
diagonal pairs are included. On u nonzero eliminate X using the
Y difference. The Z difference is N-Dz, and the W difference is
a unit multiple of E modulo N-Dz. The pair lift
\[
L'[u,u^{-1},z][x_1]/(x_1^2-ux_1+z)
\tag{11}
\]
is finite free and faithful of rank two. Thus E must be a unit in
L'[u,u inverse,z]/(N-Dz), not merely nonzero at its generic point.

Let u_star=-ma/2 and delta=N(u_star). Both m and a are nonzero,
so u_star is nonzero. If delta=0, the full vertical component
u=u_star remains in the pair curve. Its restriction E(u_star,z)
would have to be a nonzero constant, contradicting E2 nonzero.
If delta is nonzero, the exact pair ring is
L'[u,u inverse,D inverse]. Its units give U=lambda*u^i*D^j,
with lambda nonzero and i,j nonnegative. But
U(u_star)=E2 delta squared is nonzero, so j=0. Therefore
\[
\delta\ne0,\qquad \mathcal U=\lambda u^i,
\qquad \lambda\in(L')^*,\quad 0\le i\le5.
\tag{12}
\]
Equations (10),(12) leave exactly two alternatives:
\[
\begin{array}{c|c|c|c}
 &q&i&\mathcal U\\ \hline
\mathrm I&-3ap/5&5&(ap/5)u^5\\
\mathrm {II}&-ap/2&4&-(ma^2p/2)u^4.
\end{array}
\tag{13}
\]
Indeed a nonzero fifth coefficient forces the fourth to vanish;
a zero fifth coefficient makes the displayed fourth nonzero.
In particular q is now nonzero. All originally lower-degree and
zero y cases have been excluded by this same argument, not omitted.
Equation H7 in (8) gives p_t=-2p squared/(5m) in I and p_t=0 in II.

The boundary u=0 is also retained. There the sigma difference
is zero and theta's divided difference is d-az. If y1-qz also
vanished at z=d/a, every literal row difference, including W by
(4), would vanish. The same monic pair lift before localizing u
contradicts the polynomial inverse. Consequently
\[
ay_1-dq\ne0.
\tag{14}
\]
This condition includes diagonal pairs and will discard one sign
in alternative II.

## 4. A pair derivative formula and exclusion of alternative I

Put K0=2c+k1+mb and epsilon=delta/(m cubed*a cubed). The identity
for delta is equivalent to
\[
d=aK_0/2+m^2a^3(\epsilon-1/8).
\tag{15}
\]
Evaluating (12),(13) at u_star gives
epsilon squared=1/320 in I and 1/64 in II. Thus epsilon is an
existing nonzero complex constant, not an adjoined root or a
function whose derivatives may be chosen independently.

Since E2 is constant in u, differentiation of the complete U gives
\[
\begin{aligned}
\mathcal U'(u_*)&=2E_1(u_*)\delta+2E_2\delta N'(u_*),\\
E_1(u_*)&=E_2\{i\delta/(2u_*)-N'(u_*)\},\qquad
N'(u_*)=K_0-m^2a^2/4.
\end{aligned}
\tag{16}
\]
The second line uses U'/U=i/u_star. This is differentiation in the
independent pair variable u followed by evaluation, not coefficient
differentiation at a moving root. With alpha=q/(ap), substitution
of E1 from (10) yields the exact formula
\[
y_2=\frac{n_s}{m}-\frac{k_2}{2}-\frac{pk_1}{2m}
 -\frac{3pb}{2}+a^2mp\{3\alpha/4+7/8-i\epsilon\}.
\tag{17}
\]
No lower coefficient of the pair polynomial was set to zero to
obtain this equality.

In I, alpha=-3/5 and the final bracket is 17/40-5epsilon.
Put A0=a_t/a in F0. Equations (8) give
\[
(y_2)_s=\frac{2pA_0}{5}-\frac{4p^2}{25m},\qquad
b_s=-\frac{2A_0}{3}+\frac{p}{3m},\qquad
p_t=-\frac{2p^2}{5m},\quad p_{tt}=\frac{18p^3}{25m^2}.
\tag{18}
\]
Differentiate (17) by the genuine s partial. Its last term is
s-constant, and k_{1,s}=p,k_{2,s}=p_t. Therefore
\[
n_{ss}=m(y_2)_s+mp_t/2+p^2/2+(3mp/2)b_s\in F_0.
\tag{19}
\]
In particular n_sss=0. This conclusion is an exact derivative
identity, not an assumption on the form of the potential n.

Now differentiate the ENTIRE H6 in (8). Its terms involving
q,a,p,n_ss are s-constant. Using (18),(19), the result is
\[
\begin{aligned}
0=(H_6)_s
 &=-2p(y_2)_s/m+b_s(p_t/2-p^2/m)
                                  +p_{tt}/6-pp_t/(2m)\\
 &=\frac{6p^3}{25m^2}\ne0.
\end{aligned}
\tag{20}
\]
The A0 terms cancel. Both epsilon signs and arbitrary a_t are
retained. This contradiction excludes I.

## 5. Alternative II and the discarded pair sign

Here q=-ap/2 and p_t=0. Since also p_s=0, p belongs to C*,
and m=pt+mu with mu in C. We will not use m as an ambient
coordinate. Initially a is only in F0*, not assumed complex.

Now epsilon is either +1/8 or -1/8. Formula (17) and the next
coefficient U3=0 give
\[
\begin{aligned}
y_2&=n_s/m-k_2/2-pk_1/(2m)-3pb/2
                                      +a^2mp(1/2-4\epsilon),\\
y_1&=ap\{-K_0/4+a^2m^2(5/16-5\epsilon/2)\}.
\end{aligned}
\tag{21}
\]
For epsilon=+1/8, equations (15),(21) give d=aK0/2 and
y1=-apK0/4=dq/a, contradicting (14). The minus sign remains.

For that sign put J0=2c+k1 and K0=J0+mb, and put C0=n_t+2y0.
The complete surviving pair equations are
\[
\begin{aligned}
d&=aK_0/2-a^3m^2/4,\\
y_1&=ap(-K_0/4+5a^2m^2/8),\\
n_s&=my_2+mk_2/2+pk_1/2+3mpb/2-a^2m^2p,\\
C_0&=J_0(y_2+pb/2)+k_1k_2/2-pe-3a^4m^3p/8
                                      +a^2bm^2p-b^2mp/2.
\end{aligned}
\tag{22}
\]
The third line is (21), the first two are (15),(21), and U2=0
gives the fourth. After the third line has been imposed, the
coefficients determining y1 and C0 have nonzero constant
coefficients 4. Substituting all of (22) into the ENTIRE numerator
gives exactly U=-(ma squared*p/2)u to the fourth, including its
u1 and u0 coefficients. Thus no unexamined lower pair equation
is being substituted for the displayed necessary implications.
The retained u=0 guard is ay1-dq=a to the fourth*m squared*p/2,
which is nonzero.

Equations A5,B5 and the s derivative of the third line of (22) give
\[
b_s=-2a_t/(3a),\qquad
(y_2)_s=pa_t/(3a),\qquad
n_{ss}=p^2/2-2mpa_t/(3a).
\tag{23}
\]
Define T=4y2+2pb+k2. Then T_s=0. The genuine W row (4) has
degree at most four, with
\[
w_4=[x^4]W=-T/(2m)\in F_0.
\tag{24}
\]
Its fifth coefficient vanishes because 2q+pa=0. The terms theta X
and sX squared have no contribution to w4. In particular w4 is
independent of the actual X.

## 6. The actual ring forces w4 to be complex

Work over K= C(X) in the ACTUAL polynomial ring R=K[Y,Z,W].
Extend N from A by killing the original global slice, and set
Delta=a0 N-(NX)E. This derivation preserves the actual four-ring,
kills X, and is nonzero and locally nilpotent: in
B localized at a0=A localized at a0[X] it acts as a0 N on A
and kills X. Thus it restricts to a nonzero K-LND of R. In the
coefficient extension L'(X)[x] it is a0 rho partial_x and kills
L'(X). Its polynomial kernel contains a nonconstant element over K,
indeed has transcendence degree two by the local-slice argument.

Suppose w4 is not complex. It is then nonzero. The exact intrinsic
degrees of Y,Z,W are (3,4,4), with initial forms
\[
q\eta^3,\qquad \eta^4,\qquad w_4\eta^4.
\tag{25}
\]
Since w4 is noncomplex and X is independent, the last two are
algebraically independent over K. All three lie in F0(X)[eta],
whose transcendence degree over K is two. Their FULL initial
kernel is consequently a height-one homogeneous prime generated
by an irreducible weighted-homogeneous polynomial P0, for weights
(3,4,4). It must involve the first source variable.

In a fixed weighted degree, the exponent of that variable is
fixed modulo four. If only one exponent occurred, P0 would factor
as its power times a polynomial in the other two variables. This
is inconsistent with irreducibility and their independence; the
first initial form is itself nonzero. Hence at least two distinct
exponents occur, differing by at least four, and
\[
\operatorname{wt}(P_0)\ge12.
\tag{26}
\]

On the other hand the literal actual partial partial_Y has
intrinsic degree shift at most seven on EVERY element of R.
To see this, uniquely extend that derivation to the finite
coefficient overfield L'(X)(x). Inverting the full differential
matrix in (t,s,x), the t and s cofactors from the Z,W rows have
degree at most 4+4-1=7, and the x cofactor has degree at most
eight. The denominator is the full coefficient-only nonzero
scalar from (2). Coefficient partials do not raise polynomial
x degree, and partial_x lowers it by one. This proves the
all-ring bound. It does not identify the coefficient overfield
with Frac(R) when the finite extension is proper.

Choose f0 in ker_R(Delta) outside K. Its actual x degree is zero.
Let Q be the top weighted part of its UNIQUE source polynomial
in Y,Z,W, of weight M>0. Then Q=P0 to the ell times Q0, with
ell positive and P0 not dividing Q0. As P0 involves the first
variable, its first partial is nonzero modulo P0 in characteristic
zero. The ell-th first partial of Q is therefore nonzero modulo
the FULL initial kernel. Thus
\[
\deg_x(\partial_Y^\ell f_0)=M-3\ell\le7\ell,
\qquad M\ge\ell\operatorname{wt}(P_0).
\tag{27}
\]
The first equality also uses that every lower-weight source term
stays lower after the same differentiation. Equations (26),(27)
would give 12ell<=10ell. This contradiction proves w4 belongs
to C. The argument was applied only when w4 was noncomplex;
the case w4=0 is retained without assigning W a false degree.

## 7. Full mixed derivatives exclude the remaining complex case

Set tau=T/m=-2w4 in C, possibly zero. Before assuming a_t=0,
differentiate the actual pair coefficients in (22):
d_s=a(2c_s+p+mb_s)/2 and (y1)_s=-(p/2)d_s. In addition,
4(y2)_s+2pb_s=0 by (23). These genuine identities are imposed
before combining A4 and B4; their lower-coefficient terms cannot
be discarded independently. Substitution of (22),(23) and these
derivatives in the full coefficients (5)--(7) gives
\[
H_6=\{k_3-3pT/m-2pma a_t\}/6=0,\qquad
A_4+(p/2)B_4=4(y_2)_t+2pb_t+2pT/m=0.
\tag{28}
\]
In particular T_t=k3-2pT/m. Differentiating T=tau*m gives
T_t=tau*p. Equations (28) force k3=3p tau and a_t=0.
Since a_s was already zero, a belongs to C*. No actual frame
change is inferred from the complex status of a,p,tau.

We now have b_s=(y2)_s=0 and n_ss=p squared/2. The complete H5
coefficient reduces to
\[
n_{ts}=py_2+3bp^2/2+k_2p.
\tag{29}
\]
Differentiate the third line of (22) with respect to t, using
the genuine potential derivatives k_{1,t}=k2,k_{2,t}=k3 and
m_t=p. Compare with (29). This gives
(y2)_t+k3/2+3pb_t/2-2a squared*p squared=0. Combining it with
T_t=tau*p and k3=3p tau yields
\[
b_t=2a^2p-\tau,\qquad
(y_2)_t=-a^2p^2,\qquad
n_{tts}=2a^2p^3+3p^2\tau/2.
\tag{30}
\]
The last equality differentiates (29), not an independently
chosen n jet. All optional zeros of tau,b,y2 are retained.

Finally substitute the ENTIRE pair expressions (22) into the
ENTIRE formal H in (5), using (29), k3=3p tau, and
k2=tau*m-2pb-4y2. Its degree-four coefficient is
\[
\begin{aligned}
8H_4={}&-24y_2^2-24y_2bp+12y_2m\tau
 +3a^4m^2p^2+4a^2m^2p\tau-2b^2p^2\\
 &+2bmp\tau-6k_1p\tau-2m^2\tau^2+4n_{tt}.
\end{aligned}
\tag{31}
\]
In this complete coefficient all c,e,ell and their possible lower
contributions have canceled; they were not assumed constant or
set to zero. No integration or rationality assumption on n is used.
Every term on the right except k1 and n_tt is s-constant. The
genuine identities k_{1,s}=p and (30) therefore give
\[
0=(H_4)_s
=\{-6p^2\tau+4(2a^2p^3+3p^2\tau/2)\}/8
=a^2p^3\ne0.
\tag{32}
\]
This excludes II and proves the bounded theorem.

## 8. Verification and precise scope

The full264,296,535,553 and555 sources were read through EOF
before authoring. The finite intrinsic normalization and the
generic pair-unit lemma are their direct retained contracts;
no conclusion from an excess-degree or nonzero-h branch is
imported. The actual initial-ring argument in Section 6 is proved
here with its cofactor bound, full prime, and multiplicity step.

Fresh unsaved a98daf reconstructed the ENTIRE formal H, its
formal derivatives before evaluation, and the full A/B expressions
with unrestricted lower coefficients. It checked all four equations
(8) and the endpoint (20). Fresh ef01c5 reconstructed the ENTIRE
pair E and numerator U, both coefficients in (10), both epsilon
equations and the complete derivative identity (16),(17).
Fresh 0dc478 checked the whole pair substitution (22), including
the remaining coefficients after solving for C0.

Fresh c6972f retained moving a and checked both complete identities
(28) and the full H5. Fresh 3bc970 reconstructed the entire H
coefficient and its genuine derivative in (31),(32); ee5abc gave
the printed simplified form. Independently, fresh 1e19b8 completed
in25854c substituted the derived exact t/s derivatives into the
full formal polynomial, leaving c(t,s),e(t,s),ell(t,s) and an
arbitrary n remainder N0(t) present. It found H6=H5=0 and
partial_s H4=a squared*p cubed. These symbolic reconstructions
supplement the exact ring and derivative proofs, not finite samples.

All divisions are by licensed nonzero coefficients m,p,a,delta,
u_star or nonzero integers. The discarded epsilon sign is removed
by the full u=0 polynomial-return guard. Zero q and lower y degree
are excluded by (13); zero w4 and tau remain within the proof.
No square root is descended to the original coefficient field,
and no coefficient-field expression is promoted to an actual
coordinate. The result does not cover nonzero h, arbitrary theta
degree, an arbitrary sliced frame, or a cancellation-entry problem.

No saved checker was executed, imported, compiled or rerun. No
canonical record or earlier source was edited. This author-held
proof requires separate complete saved-source review. No novelty,
realization, recognition, or general cancellation claim is made.
