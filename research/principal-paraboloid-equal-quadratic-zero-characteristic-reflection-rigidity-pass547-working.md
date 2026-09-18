# Reflection rigidity in the zero-characteristic equal-quadratic branch

Working necessary reduction: retain the FULL actual chart264/296/535,
with noncomplex \(m=k_s\ne0\) and both intrinsic slopes quadratic.
Use the centered coefficient notation of545, but write a for its
quadratic y coefficient to distinguish it from the actual kernel ring
A. In the remaining branch
\[
q:=m_t+\mu m_s=0,\qquad a\notin\mathbb C,
\]
the full scalar and the actual initial-relation bound force
\[
\boxed{a=\frac{\alpha}{m}+\beta,\qquad
       \chi=\frac{2\alpha}{m^2}+\delta,\qquad
       \alpha\in\mathbb C^*,\quad\beta,\delta\in\mathbb C.}
\tag{1}
\]
The proof does not assume a rational coefficient field. It supplies
only a necessary family. No exclusion, recognition, actual
degree-lowering change, or general chart-entry claim is made for
this remaining branch.

## 1. Actual input and exact coefficient conventions

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and [535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A\in\operatorname{LND}(A),
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The symbol \(z_{\rm int}\) means the literal original Z-intercept.
Both returns, the selected literal partial, original global slice and
full genuine gradient-unit hypotheses remain required.

The finite intrinsic affine normalization from
[545, Sections 1--2](principal-paraboloid-equal-quadratic-nonzero-characteristic-exclusion-pass545-working.md)
gives
\[
\sigma=x^2+c,\qquad \theta=\mu x^2+d x+e,
\qquad y=a x^2+b x+r,
\quad \mu\ne0,\quad d\ne0.
\tag{3}
\]
Here \(x=\rho(v-v_0)\), \(\rho^2\in L^*\), and coefficients
may lie in \(L'=L(\rho)\). The functions a and mu lie in the
original L, since they are original leading-coefficient ratios.
The degree bound on y in545 precedes its q-nonzero hypothesis.
The d-zero boundary is the retained double-cover case303 and forces
m complex, contrary to the present assumptions.

Coefficient partials now fix x. The scalar is
\(J_{t,s,x}=-a_0^4/\rho\), and \(Nx=\rho\), not necessarily one.
The primitive-cross and multiplier covariance is
\(\tau_x=\rho\tau_v\), \(\kappa_x=\kappa_v/\rho^2\in L^*\).
We use \(\kappa=\kappa_x\). No actual coordinate change or extension
of the actual kernel ring is inferred from adjoining rho.

Set
\[
\begin{gathered}
p=m_t,\quad h=m_s,\quad q=p+h\mu=0,\quad
\Phi=k_{tt}+2p\mu+h\mu^2,\quad
\chi=(4a+\Phi)/m,\\
\mathcal D=\partial_t+\mu\partial_s.
\end{gathered}
\tag{4}
\]
We assume \(a\notin\mathbb C\). Since m is noncomplex, q zero
implies \(h\ne0\): otherwise both exact partials of m would vanish.
Neither \(b=0\) nor any of the three surviving Laurent alternatives
is assumed.

## 2. Full scalar pedigree for the characteristic constants

For clarity the complete rows and formal H behind the required high
coefficients are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-F(\sigma,\theta),\\
F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2+n_tP+n_sV,\\
H(U,P,V)&=U^2+F_PU+
 \frac{F_V}{m}\{\ell-(2P+k_t)U-F\}\\
&\quad+k_{ttt}P^3/6+p_tP^2V/2+h_tPV^2/2+h_sV^3/6\\
&\quad+n_{tt}P^2/2+n_{ts}PV+n_{ss}V^2/2-\ell_tP-\ell_sV,
\qquad H(y,\sigma,\theta)=h_0\in L.
\end{aligned}
\tag{5}
\]
The evaluations \(f=H_U^{\rm ev}\), \(g=H_V^{\rm ev}\) use
formal differentiation before substitution. With \(\eta=\sigma_x\),
\(D_f=(2\sigma+k_t)/m\), \(\nu=F_V^{\rm ev}/m\), and
\(B_f=(2y+F_P^{\rm ev})/m\), the complete535 expressions are
\[
\begin{aligned}
\mathcal A_\eta={}&\eta^2y_t+\eta\theta_xy_s+y_x^2
                 -\eta\sigma_ty_x-\sigma_sy_x\theta_x,\\
\mathcal B_\eta={}&\eta^2(\theta_t+B_f)+D_f\eta y_x+y_x\theta_x
             +\eta(\theta_s+\nu-\sigma_t)\theta_x-\sigma_s\theta_x^2,\\
\mathcal A_\eta={}&\kappa g,\qquad \mathcal B_\eta=-\kappa f.
\end{aligned}
\tag{6}
\]
In particular no coprimality of f,g at \(\eta=0\) is used.

Put
\(M_2=p_t+2\mu h_t+\mu^2h_s\) and
\(K_3=k_{ttt}+3\mu p_t+3\mu^2h_t+\mu^3h_s\).
The unrestricted high ledger in545, specialized only at q zero,
is
\[
\begin{aligned}
[x^6]H^{\rm ev}&=K_3/6,&
[x^5]H^{\rm ev}&=d(M_2-h\chi)/2,\\
[x^4]g&=(M_2-h\chi)/2,&
[x^4]\mathcal A_\eta&=4\mathcal Da,\\
[x^4](\mathcal B_\eta+\kappa f)&=4(\mathcal D\mu+\chi).
\end{aligned}
\tag{7}
\]
These identities do not require \(b=-qd/2\); the omitted unrestricted
term of H's fifth coefficient has a factor q. Since \(d\ne0\),
the genuine level and (6) give
\[
K_3=0,\quad M_2=h\chi,\qquad
\mathcal Dm=0,\quad \mathcal Da=0,\quad
\mathcal D\mu=-\chi,\quad \mathcal D\chi=0.
\tag{8}
\]
For the last identity, differentiate \(m\chi=4a+\Phi\) and use
\(\mathcal D\Phi=K_3+2q\mathcal D\mu=0\). This is a full-potential
consequence, not an independent ansatz for the coefficients.

## 3. Exact characteristic field and the derivative relation

Because \(h\ne0\), the coefficient pair \((t,m)\) is a separating
transcendence basis. L is finite over \(\mathbb C(t,m)\), and
\(\mathcal D\) is its unique extension of \(\partial_t|_m\).
Let \(F_0=\ker_L\mathcal D\). Then \(F_0\) is finite algebraic over
\(\mathbb C(m)\), not necessarily equal to that rational field.
For example, differentiating the monic minimal polynomial of any
\(\mathcal D\)-constant over \(\mathbb C(t,m)\) shows that its
coefficients are in \(\mathbb C(m)\); the relative algebraic closure
in a finite function-field extension is finite. The commuting
\(\partial_m|_t\) preserves \(F_0\), and its constants there are C.

Equations (8) imply exact integrations by subtraction:
\[
\begin{aligned}
\mu&=-\chi t+\mu_0,\\
s&=-\chi t^2/2+\mu_0t+s_0,\\
k&=-2a t^2+K_1t+K_0,
\qquad a,\chi,\mu_0,s_0,K_1,K_0\in F_0.
\end{aligned}
\tag{9}
\]
Indeed \(\mathcal Ds=\mu\). Also
\[
\mathcal D^2k
=\mathcal D(k_t+\mu m)
=k_{tt}+\mu p-m\chi
=\Phi-m\chi=-4a,
\]
using q zero. Thus neither integration assumes rationality or a
primitive for an arbitrary function.

The original equation \(k_s=m\), in the exact \((t,m)\) basis, is
\(k_m=m s_m\). Compare powers of t in (9), which is legitimate
because t is transcendental over \(F_0\). It gives
\[
\boxed{4a_m=m\chi_m,}\qquad
(K_1)_m=m(\mu_0)_m,\qquad (K_0)_m=m(s_0)_m.
\tag{10}
\]
In particular \(a\notin\mathbb C\) implies \(a_m\ne0\), then
\(\chi_m\ne0\). Hence chi is nonzero and noncomplex. This treats
the otherwise possible zero value of chi before any division by it.

## 4. The actual initial kernel has a relation of weight at most eight

The fourth intrinsic coefficient of the complete w in (5) is
\(-\chi/2\). Its cubic coefficient is \(-2b/m\), but will not
affect this argument. Thus the actual intrinsic profile is exactly
\((2,4,4)\), with initials
\[
Y_h=(X+a)T^2,\qquad Z_h=T^4,\qquad W_h=-\chi T^4/2.
\tag{11}
\]
Here T is an independent grading symbol. All three degrees are
positive; no actual ambient variable is being replaced by m or x.

For completeness, the actual LND is
\[
\Delta=a_0N-(NX)E
\quad\hbox{on}\quad R=\mathbb C(X)[Y,Z,W].
\tag{12}
\]
Extend N to the original \(A[u_{\rm glob}]\) by \(Nu_{\rm glob}=0\).
The displayed derivation preserves the actual polynomial ring, fixes
X, and on \(A_{a_0}[X]\) acts as \(a_0N\) with X fixed. It is
therefore a nonzero LND. A local slice gives
\(\operatorname{trdeg}_{\mathbb C(X)}\ker_R\Delta=2\), so a
nonconstant actual polynomial invariant exists. The fraction field
of R is the ORIGINAL \(L(v)(X)\). In the finite extension
\(L'(X)(x)\), \(\Delta=a_0\rho\partial_x\), so an actual invariant
has intrinsic degree zero. The two fraction fields are not identified.

The Y and W initials are algebraically independent over \(K=\mathbb C(X)\).
To check this explicitly, their degree-zero ratio is
\[
Y_h^2/W_h=-2(X+a)^2/\chi.
\]
Its m derivative is nonzero: after clearing its nonzero denominator,
the coefficient of \(X^2\) is a nonzero multiple of \(\chi_m\).
An element algebraic over K would be killed by this coefficient
derivation in characteristic zero. Thus that ratio is transcendental
over K; together with the independent grading symbol it gives the
claimed independence.

A nonconstant actual invariant supplies a nonzero relation by taking
its positive-weight top part. Consequently the FULL initial kernel
has height one and is generated by an irreducible weighted-homogeneous
polynomial \(\mathscr H\in K[Y,Z,W]\). The Y/W independence proves
that \(\mathscr H\) depends on Z.

Use the ACTUAL coordinate partial \(\partial_Z\), holding X,Y,W
fixed, and extend it uniquely through the finite separable coefficient
extension. The full scalar in \((t,s,x)\) is \(-a_0^4/\rho\in(L')^*\).
The two other rows have intrinsic degrees two and four. Cramer's
rule therefore gives t,s coefficients of intrinsic degree at most
five and an x coefficient of degree at most six. This extended partial
increases the intrinsic degree of any polynomial by at most five.

Let an actual invariant have highest weighted part
\(\mathscr H^\ell G\), of weight M, where \(\ell\ge1\) and
\(\mathscr H\nmid G\). Characteristic zero and Z dependence give
\(\mathscr H_Z\notin(\mathscr H)\). After \(\ell\) coordinate
partials, the highest part modulo \(\mathscr H\) is
\(\ell!\mathscr H_Z^\ell G\ne0\). Therefore its exact intrinsic
degree is \(M-4\ell\). Starting from intrinsic degree zero, the
cofactor bound gives \(M-4\ell\le5\ell\). Hence
\[
\operatorname{wt}\mathscr H\le9,
\qquad\hbox{and thus}\qquad
\boxed{\operatorname{wt}\mathscr H\le8}
\tag{13}
\]
because all weights \((2,4,4)\) are even. No strict invariant-growth
refinement, global Delta slice, or assumed rational coefficient field
is used in this bound.

## 5. The reflection argument over the original complex constants

In a homogeneous polynomial of weights \((2,4,4)\), all Y exponents
have the same parity. An odd parity would factor out Y, contradicting
irreducibility of \(\mathscr H\) unless it were a scalar times Y,
which cannot vanish on (11). Thus it is a polynomial in \(Y^2,Z,W\).
After dividing the weights by four, (13) makes it homogeneous of
ordinary degree at most two in these three entries. Dehomogenize at
the nonzero initial Z and absorb the factor \(-1/2\) of W. There is
a nonzero polynomial
\[
P_X(S,T)\in\mathbb C(X)[S,T],\qquad
\deg_{S,T}P_X\le2,\qquad P_X((X+a)^2,\chi)=0.
\tag{14}
\]
Its total degree bound, including its T-squared coefficient, will be
important. The notation \(P_X\) permits rational coefficients in X.

Since \(a,\chi\in F_0\), they are algebraically dependent over C.
Let \(F(S,T)\in\mathbb C[S,T]\) generate their height-one prime
relation ideal, with F irreducible. Both \(\deg_SF\) and
\(\deg_TF\) are positive: a relation in only one variable would make
a or chi complex. Extension to the purely transcendental field K
preserves irreducibility and the full relation ideal. Thus
\[
F(S,T)\mid P_X((X+S)^2,T)\quad\hbox{in }K[S,T].
\tag{15}
\]
Reflection \(S\mapsto-2X-S\) fixes the right side. Therefore
\(F(-2X-S,T)\) also divides it, and this reflected polynomial is
irreducible over K.

These two factors are distinct. To see this without any rationality
assumption on a, write
\(F=f_j(T)S^j+f_{j-1}(T)S^{j-1}+\cdots\), with \(j>0\).
If reflection made an associate, comparison of leading S coefficients
would fix the associate factor as \((-1)^j\). The next coefficient
would then give
\(jXf_j(T)=f_{j-1}(T)\), impossible for the independent X.
They are consequently coprime and their product divides the pullback
in (15).

The latter has T degree at most two and S degree at most four. Thus
\[
\deg_TF=1,\qquad \deg_SF\le2.
\tag{16}
\]
Write \(F=u(S)T+v(S)\). The product of the two factors has T degree
two, so any remaining quotient has T degree zero. On the other hand
the T-squared coefficient of \(P_X((X+S)^2,T)\) is a nonzero element
of K independent of S: total degree at most two in (14) leaves no
S factor multiplying T squared. Consequently
\[
u(S)u(-2X-S)\cdot\text{(remaining quotient)}\in K^*.
\]
All entries are polynomials in S. Each must be constant in S.
In particular u is a nonzero complex constant. Together with (16),
this proves
\[
\chi=c_2a^2+c_1a+c_0,\qquad c_0,c_1,c_2\in\mathbb C.
\tag{17}
\]
Neither a rational parametrization nor a rationality assumption on
\(F_0\) entered the reflection proof.

## 6. Differential rigidity and what remains

Substitute (17) into (10) and cancel \(a_m\ne0\). This yields
\[
4=m(2c_2a+c_1).
\tag{18}
\]
If \(c_2=0\), then \(c_1=0\) makes (18) impossible, while
\(c_1\ne0\) would make m complex. Both alternatives are excluded.
Thus \(c_2\ne0\), and
\[
a=\frac{2}{c_2m}-\frac{c_1}{2c_2},\qquad
\chi=\frac{4}{c_2m^2}+c_0-\frac{c_1^2}{4c_2}.
\tag{19}
\]
Set \(\alpha=2/c_2\), \(\beta=-c_1/(2c_2)\), and
\(\delta=c_0-c_1^2/(4c_2)\). This is precisely (1). The constants
beta and delta may vanish. No value of the other coefficients in
(3),(9), and no zero or nonzero value of b, was divided away.

This is a genuine necessary reduction, not a contradiction. The
abstract reflected relation has the explicit conic form
\[
P_X(S,T)=\{T-c_2S-(c_2X^2-c_1X+c_0)\}^2
                       -(2c_2X-c_1)^2S.
\tag{20}
\]
Its pullback at \(S=(X+a)^2,T=\chi\) vanishes under (17), so the
small-weight support itself is compatible with the remaining family.
That polynomial compatibility is not an actual264 realization.
The functions \(\mu_0,s_0,K_1,K_0\) in (9) still belong to the
exact finite field \(F_0\); the present argument does not make that
whole field rational or remove any roots by an ambient localization.

## 7. Verification and scope

The full545 source was author-read through EOF and independently
saved-reviewed before this task. Its unrestricted high ledger is
reprinted here and specialized only after retaining its q factors.
Fresh unsaved b4ab6f reconstructed the complete formal H and both
full535 polynomials, including every high coefficient used in (7).
Fresh 3536f2 checks the entire reflected product behind (20), the
derivative identity in (18)--(19), and the complete coefficient
comparison \(k_m-ms_m\); every residual is zero. The exact-field,
actual-LND, cofactor/multiplicity, prime relation and reflection
arguments are the written proofs above.

This note requires noncomplex m and noncomplex quadratic y coefficient
a inside the q-zero equal-quadratic sector. It does not address the
complex-a sector, assert a full nonlinear-sigma exclusion, identify a
new actual coordinate, or prove arbitrary chart entry or cancellation.
Earlier recognition ancestors are not recursively recertified.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited. No novelty, external certification
or independent saved-source acceptance is claimed by this author note.
