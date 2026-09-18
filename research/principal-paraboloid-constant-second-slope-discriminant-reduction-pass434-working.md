# The constant-second-slope discriminant and its exact boundaries

Working necessary classification: retain the full actual264 chart,
the complete430 plane primitive, and
\[
k=s+f,\qquad f_s=n_s=0,\qquad f'''\ne0,
\qquad e=\ell_s\in\mathbb C^*.
\tag{1}
\]
The coefficient of U^2 in the plane primitive is
\(\mathcal A=f''/2-h_s/e\), where h is the actual third level.
If Acal is nonzero, the centered discriminant is at most linear
in P. The whole-line possibilities are exactly restricted to
\[
(\deg_v\sigma,\deg_v y)=(2,4)\quad\hbox{or}\quad(1,2).
\tag{2}
\]
This is a necessary list, not an existence assertion. The moving
third and fourth levels remain in the coefficient ledger.

The Acal=0 boundary is different: sigma is coefficient-constant
and y is an affine intrinsic parameter. It is not excluded here.
Neither part of this note supplies original-ring recognition or
solves the remaining calibrated scalar. Separate collision arguments
must retain their own all-X license and boundary checks.

## 1. Actual hypotheses and the retained plane polynomial

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad[L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\quad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{3}
\]
The original slice, selected literal partial, actual localization,
both returns and all coefficients of the scalar remain in force.
The exact coefficient partials commute and fix v, with joint
constants C. Let F=ker_L partial_s, finite over C(t). Primes denote
its exact t-derivative, not a rational-function ansatz. By(1),
\[
f,n\in\mathbb F,\qquad \ell=es+\ell_0,\quad\ell_0\in\mathbb F.
\tag{4}
\]

The completely read
[430 reduction](principal-paraboloid-arbitrary-longitudinal-plane-reduction-pass430-working.md)
supplies genuine levels h,q in L and
\[
\begin{gathered}
S(U,P)=U^2+(f''P+n')U+\frac{f'''}6P^3
              +\frac{n''}2P^2-\ell_0'P-h,\\
\theta=S(y,\sigma)/e,\quad O=L[y,\sigma],\quad
\Phi(y,\sigma)=q,\quad
(\Phi_U(y,\sigma),\Phi_P(y,\sigma))O=O.
\end{gathered}
\tag{5}
\]
The gradient ideal uses296's full minor-unit argument, not just
the fact that the third surface has V-derivative -e. Both levels
are actual coefficient functions; h_s,h_t and q are not discarded.

## 2. Complete coefficient and discriminant ledger

Put rho=h_s/e and Acal=f''/2-rho. The full primitive has the form
\[
\Phi(U,P)-q=\mathcal A U^2+B(P)U+C(P),
\quad B=b_2P^2+b_1P+b_0,\quad C=\sum_{i=0}^4c_iP^i,
\tag{6}
\]
with the complete coefficients
\[
\begin{aligned}
\rho&=h_s/e,&\mathcal A&=f''/2-\rho,\\
b_2&=f'''/2,&b_1&=n''+2e-\rho f'',
&b_0&=ef'-\ell_0'-\rho n',\\
c_4&=f''''/24,&c_3&=(n'''-\rho f''')/6,\\
c_2&=(ef''-\ell_0''-\rho n'')/2,
&c_1&=en'-h_t+\rho\ell_0',
&c_0&=\rho h-q.
\end{aligned}
\tag{7}
\]
In particular C already includes the fourth level through c0.
There is no missing additive level in the discriminant below.

For now assume Acal is nonzero and set
\[
\xi=2\mathcal A y+B(\sigma),\qquad
\Delta(P)=B(P)^2-4\mathcal A C(P)=\sum_{i=0}^4d_iP^i.
\tag{8}
\]
The polynomial coefficients are exactly
\[
\begin{aligned}
d_4&=b_2^2-4\mathcal A c_4,\\
d_3&=2b_2b_1-4\mathcal A c_3,\\
d_2&=b_1^2+2b_2b_0-4\mathcal A c_2,\\
d_1&=2b_1b_0-4\mathcal A c_1,\\
d_0&=b_0^2-4\mathcal A c_0.
\end{aligned}
\tag{9}
\]
Completion of the square is a formal coefficient-field operation,
not an ambient coordinate change. It yields
\[
\xi^2=\Delta(\sigma),\qquad
O=L[\xi,\sigma].
\tag{10}
\]
Indeed y=(xi-B(sigma))/(2Acal), whose denominator is a nonzero
coefficient field element. Formal differentiation also gives
\[
\Phi_U=2\mathcal A U+B(P),\qquad
\Delta'(P)=2B'(P)(2\mathcal A U+B(P))-4\mathcal A\Phi_P.
\tag{11}
\]
Here the primes on B,Delta are formal P-derivatives, unlike the
coefficient derivatives in(7). Hence the evaluated gradient condition
in(5) is equivalent to
\[
\boxed{(\xi,\Delta'(\sigma))O=O.}
\tag{12}
\]

## 3. Root multiplicities force a linear discriminant

First sigma cannot be in L. Otherwise O=L[y], so y is transcendental
over L. The level Phi(y,sigma)=q would force the coefficient Acal
of U^2 to vanish, contrary to the present case.

Extend scalars to an algebraic closure of L; a generating or Bezout
identity over L remains valid there. A repeated root r of Delta
would have a preimage under the nonconstant polynomial sigma(v).
At that point xi^2=Delta(sigma) gives xi=0, and Delta'(sigma)=0,
contradicting(12). Thus a nonconstant Delta must be squarefree.

If deg Delta is at least three, choose three distinct roots r_i.
For d=deg_v sigma>0, each root of sigma-r_i has even multiplicity,
because it has exactly that multiplicity in the square Delta(sigma).
Thus each of these fibers contains at most d/2 distinct points.
Its roots contribute at least d/2 to the multiplicity of the zeros
of sigma_v. The three fibers are disjoint, while the nonzero
polynomial sigma_v has degree d-1. The resulting inequality
d-1>=3d/2 is impossible. This is the elementary multiplicity
argument of427, with the exact discriminant and unit ideal(12).

Degree two is also impossible. If Delta=a(P-r1)(P-r2) has distinct
roots, put c=(r1+r2)/2 and choose a square root of a after the
same base extension. The identity(10) becomes
\[
\{\xi-\sqrt a(\sigma-c)\}
\{\xi+\sqrt a(\sigma-c)\}
             =-a(r1-r2)^2/4\ne0.
\tag{13}
\]
Both polynomial factors must be units, hence constants. Their
difference makes sigma constant, a contradiction. Repeated roots
were already handled, not omitted. Finally Delta=0 is impossible
because it would give xi=0 and a zero gradient ideal in(12).

We have proved
\[
\boxed{d_4=d_3=d_2=0,\qquad
\Delta(P)=d_1P+d_0\ne0.}
\tag{14}
\]
No polynomial plane-embedding theorem or original-ring recognition
is used in this conclusion.

## 4. Exact whole-line alternatives and their moving levels

If d1 is nonzero, then
\[
\sigma=(\xi^2-d_0)/d_1,\qquad
y=\frac{\xi-b_2\sigma^2-b_1\sigma-b_0}{2\mathcal A},
\qquad O=L[\xi].
\tag{15}
\]
Since L[xi]=L[v], xi has intrinsic degree one. Therefore sigma
has exact degree two and y has exact degree four; its quartic
coefficient is nonzero because b2=f'''/2 is nonzero. The functions
d1,d0 may move in both coefficient parameters. No square-root
choice of d0 or polynomiality over C(t,s) has been assumed.

If d1=0, equation(10) makes xi a coefficient constant eta in L*,
and d0=eta^2. Consequently
\[
y=-\frac{f'''}{4\mathcal A}\sigma^2
   -\frac{b_1}{2\mathcal A}\sigma
   +\frac{\eta-b_0}{2\mathcal A},\qquad O=L[\sigma].
\tag{16}
\]
Thus sigma has exact degree one and y exact degree two. This does
not claim eta is complex, or introduce its value as an ambient
coordinate coefficient.

The actual scalar remains available in either affine intrinsic
parameter p=xi from(15) or p=sigma from(16):
\[
N p\in L^*,\qquad
J_{t,s,p}(X)=-a_0^4/(Np)\in L^*.
\tag{17}
\]
It follows by the triangular parameter Jacobian. Future coefficient
derivatives in this scalar must hold p fixed rather than the old v.
The plane analysis does not establish that this full scalar holds
for arbitrary expressions in(15),(16).

There are additional exact coefficient restrictions in(14). Its
first equation reads
\[
\frac{(f''')^2}{4}-\frac{\mathcal A f''''}{6}=0,
\quad\boxed{f''''\ne0,\quad
\mathcal A=\frac{3(f''')^2}{2f''''}\in\mathbb F^*.}
\tag{18}
\]
Hence rho=f''/2-Acal lies in F, and exact subtraction gives
\[
h=e\rho s+h_*,\qquad h_*\in\mathbb F.
\tag{19}
\]
The remaining high equations, still with every coefficient, are
\[
\begin{aligned}
0&=f'''b_1-\frac{2\mathcal A}{3}(n'''-\rho f'''),\\
0&=b_1^2+f'''b_0-2\mathcal A(ef''-\ell_0''-\rho n'').
\end{aligned}
\tag{20}
\]
In particular b1,b0 lie in F, but the lower levels do not become
constant in s. Explicitly
\[
\begin{aligned}
d_1&=4\mathcal A e\rho' s+\delta_1,\\
\delta_1&=2b_1b_0-4\mathcal A(en'-h_*'+\rho\ell_0')\in\mathbb F,\\
d_0&=b_0^2-4\mathcal A\rho(e\rho s+h_*)+4\mathcal A q,\\
(d_0)_s&=4\mathcal A(q_s-e\rho^2).
\end{aligned}
\tag{21}
\]
The fourth level q, and therefore d0, are not presumed s-constant.

In the affine-sigma alternative d1=0, independence of s over F
forces rho'=0, so rho belongs to C, and
\[
h_*'=en'+\rho\ell_0'-b_1b_0/(2\mathcal A).
\tag{22}
\]
Writing p_c=f''-2rho=2Acal, equation(18) now says
p_c p_c''=3(p_c')^2, with p_c'=f''' nonzero. Therefore
\[
(p_c^{-2})''=0,\qquad
\boxed{p_c^{-2}=a t+b,\quad a\in\mathbb C^*,\ b\in\mathbb C.}
\tag{23}
\]
This is an allowed finite-field square-root mode, not a rationality
contradiction. Exact integration uses only that the derivative
constants of F are C. If a were zero, p_c' would vanish, so that
boundary is excluded by the stated f''' condition, not by an ansatz.

## 5. The zero-Acal boundary, without division by Acal

Suppose instead Acal=0. Then rho=f''/2 is in F and(19) holds with
this rho. The primitive is linear in U:
\[
\Phi-q=B(P)U+C(P),\qquad b_2=f'''/2\ne0,
\tag{24}
\]
with the unchanged complete ledger(7).

If sigma were nonconstant, y would be integral over L[sigma]: v
is integral over that ring by its polynomial defining equation.
The monic minimal polynomial of y over L(sigma) lies in L[P][U],
because L[P] is integrally closed. Its U-degree is
[L(v):L(sigma)]=deg_v sigma, since the whole field return is
L(y,sigma)=L(v). Equation(24) bounds this degree by one. Hence
L[sigma]=O and y is a polynomial g(sigma). Differentiation of
Phi(g(P),P)=q then makes the evaluated gradient ideal generated
by Phi_U=B(sigma) alone. It cannot be a unit, since B has exact
degree two and sigma is nonconstant. This is a contradiction.

Thus sigma=p0 is in L and O=L[y]; y is affine intrinsic. The
level requires B(p0)=0 and C(p0)=0. The first gradient component
is zero, and the other is B'(p0)y+C'(p0). Since y is nonconstant,
the unit-gradient condition forces B'(p0)=0 and C'(p0) nonzero.
The complete necessary coefficient conditions are consequently
\[
\boxed{p_0=-b_1/f'''\in\mathbb F,\qquad
b_0=b_1^2/(2f'''),\qquad C(p_0)=0.}
\tag{25}
\]
All divisions are by the explicitly nonzero f'''. In this boundary,
the normal derivative has the exact shape
\[
C'(p_0)=-\frac{e f'''}2s+c_*(t),\quad c_*\in\mathbb F,
\qquad q_s=e\rho^2-\frac{e f'''}2p_0.
\tag{26}
\]
It is automatically a nonzero element of L, because s is
transcendental over F and ef''' is nonzero. Thus the gradient
condition alone does not exclude this remaining case. The displayed
fourth-level derivative follows by differentiating C(p0)=0, using
p0_s=0 and the complete c0=rho h-q. No q derivative is suppressed.

## 6. Scope and verification

For Acal nonzero the necessary alternatives are(15),(16), with the
full coefficient conditions(18)--(23). For Acal zero the separate
constant-sigma boundary(25),(26) remains. No actual realization or
converse is claimed in any case. In particular one must not discard
the algebraic mode(23), treat the moving discriminant level as
complex constant, or turn xi into an original coordinate.

The current430 source was fully reread through df53fc, and433 through
b52289 before this analysis.433 explains why e is a complex constant
in the retained nonlinear-time sector after its earlier hypotheses;
the present proof takes(1) explicitly and does not re-prove that
exhaustion.427's elementary root-multiplicity argument was previously
read in full and is reproduced here for the exact discriminant.

Fresh unsaved672ef8 reconstructs the entire coefficient ledger(7),
all five discriminant coefficients(9), the completion and gradient
identities(10)--(12), the moving-level formula(21), the exact
integration identity behind(23), and the zero-Acal normal derivative.
All residuals are zero. The written whole-ring, root-fiber and
exact-field arguments remain necessary in addition to those checks.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited. Independent full-source review
and further all-X collision or scalar arguments are separate from
this author verification. No expert certification, unrestricted
cancellation theorem, original-coordinate entry, historical novelty,
formal proof-assistant verification or external submission is claimed.
