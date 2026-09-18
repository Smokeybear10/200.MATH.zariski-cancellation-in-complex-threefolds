# Quadratic sigma and affine theta force longitudinally constant coupling

Working conditional result: under the FULL actual264 hypotheses, with
\(m=k_s\ne0\), suppose the original intrinsic degrees are
\(\deg_v\sigma=2\) and \(\deg_v\theta=1\). Then
\[
\boxed{\deg_v y\le2,\qquad m_t=0.}
\tag{1}
\]
The case \(m_t=0\) remains. This note does not recognize or exclude that
case, lower the degree of sigma by an actual coordinate transformation,
or supply an entry theorem for arbitrary cancellation data.

The proof keeps the complete scalar, moving coefficient derivatives,
all-X polynomial return, and an actual locally nilpotent derivation.
The ambient shear in the longitudinal contradiction has a proved
complex coefficient. The later corollary uses only a separately
identified localized coordinate change. No coefficient-field
coordinate change is promoted to an ambient map.

## 1. Full actual inputs and an intrinsic affine parameter

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and gradient ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the denominator-free identities of
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\qquad
Na_0=Nt=Ns=0,\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
L[A]=L[v],\quad Nv=1,\quad
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\\
L[y,z_{\rm int},w]=L[v],\qquad
L[y,\sigma,\theta]=L[v],\qquad
J_{t,s,v}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{2}
\]
Here \(z_{\rm int}\) is the literal original Z-intercept. Neither
return is replaced by birationality alone. Assume throughout that
\(m=k_s\ne0,\ \deg_v\sigma=2,\ \deg_v\theta=1\).

After a finite coefficient extension \(L'/L\), an affine change
\(x=\rho v+\zeta\), with \(\rho\in L'^*\), writes
\[
\sigma=x^2+c,\qquad \theta=dx+e,\qquad d\in L'^*,\quad c,e\in L'.
\tag{3}
\]
Explicitly, if \(\sigma=a v^2+bv+c_{\rm old}\), choose
\(\rho^2=a\) and \(x=\rho(v+b/(2a))\). This is only an intrinsic
parameter change. Extend the commuting coefficient derivatives to
\(L'\), and rebase their extensions to fix x. We do NOT set \(Nx=1\):
\[
Nx=\rho,\qquad J_{t,s,x}(X)=-a_0^4/\rho\in L'^*.
\tag{4}
\]
The formal potentials use only derivatives of coefficients in L, so
their definitions do not change. Their evaluated chain rules use the
new fixed-x partials.

For precision,535's two cleared expressions transform by
\[
\mathcal A_{\beta,\rm new}=\rho^{-2}\mathcal A_{\beta,\rm old},
\qquad
\mathcal B_{\beta,\rm new}=\rho^{-2}\mathcal B_{\beta,\rm old}.
\tag{5}
\]
The chain-rule terms involving the moving \(x_t,x_s\) cancel.
The tangent rescales by \(1/\rho\), so the cross-gradient multiplier
rescales as \(\tau_{\rm new}=\rho\tau_{\rm old}\), whereas J rescales
by \(1/\rho\). Thus \(\kappa_{\rm new}=\kappa_{\rm old}/\rho^2\)
is still a coefficient-field unit. Write it simply as
\(\kappa\in L'^*\).

Put
\[
p=m_t,\quad h=m_s,\quad k_j=\partial_t^j k,\qquad
F(P,V)=\frac{k_2}2P^2+pPV+\frac h2V^2+n_tP+n_sV.
\tag{6}
\]
The complete literal rows and second potential are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_1\sigma+m\theta+n
                         +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
mw=\ell-(2\sigma+k_1)y-F(\sigma,\theta).
\end{aligned}
\tag{7}
\]
All lower coefficients and their derivatives remain unrestricted.

## 2. The full multiplier gives the quadratic y bound

Set \(\beta=\sigma_x=2x\), and abbreviate
\[
\nu=\frac{p\sigma+h\theta+n_s}{m},\quad
D=\frac{2\sigma+k_1}{m},\quad
B_f=\frac{2y+k_2\sigma+p\theta+n_t}{m},\quad f=H_U^{\rm ev}.
\]
The complete535 expression is
\[
\begin{aligned}
\mathcal B_\beta={}&
\beta^2(\theta_t+B_f)+D\beta y_x+y_x\theta_x\\
&+\beta(\theta_s+\nu-\sigma_t)\theta_x-\sigma_s\theta_x^2
                         =-\kappa f,\\
f={}&2y+k_2\sigma+p\theta+n_t-(2\sigma+k_1)\nu.
\end{aligned}
\tag{8}
\]
If \(\deg_x y=D_y\ge3\), with leader \(a_y\ne0\), the two terms
\(\beta^2(2y/m)\) and \(D\beta y_x\) have combined degree
\(D_y+2\) coefficient
\[
\frac{4(D_y+2)a_y}{m}\ne0.
\tag{9}
\]
All remaining terms have degree at most
\(\max(D_y-1,4)\). Meanwhile
\(\deg f\le\max(D_y,4)\). Thus (8) is impossible.
This includes every zero-leading boundary: when y is zero or
constant there is no division by its leading coefficient.
Consequently write
\[
y=A x^2+B x+C,\qquad A,B,C\in L',
\tag{10}
\]
allowing any of these coefficients to vanish.

## 3. Exact all-X divided differences and the Laurent condition

The actual ring equality and localization in (2) imply
\[
L'[X,Y,Z,W]=L'[X,x].
\tag{11}
\]
It persists after any further coefficient extension and specialization
of X. In particular the three divided differences of Y,Z,W generate
the unit ideal in \(L'[X,x_1,x_2]\): apply a polynomial inverse for x
and divide its difference by \(x_1-x_2\). This statement includes
the diagonal \(x_1=x_2\), where divided differences become derivatives.

Put \(u=x_1+x_2\), and let brackets denote divided differences.
The divided first-potential fiber, after eliminating the Y difference,
is
\[
\mathcal F=u(\sigma_1+\sigma_2+k_1)+md.
\tag{12}
\]
Every zero of \(\mathcal F\) has \(u\ne0\). At such a pair set
\(X=-y[x_1,x_2]/u\); then both Y and Z divided differences vanish.
The exact identity from the ENTIRE W row is
\[
\begin{aligned}
mW[x_1,x_2]+\mathcal G
&+(\sigma_1+\sigma_2+k_1)\{y[x_1,x_2]+Xu\}
-X\mathcal F=0,\\
\mathcal G={}&u\left(y_1+y_2+\frac{k_2}2(\sigma_1+\sigma_2)
                         +\frac p2(\theta_1+\theta_2)+n_t\right)\\
&+d\left(\frac p2(\sigma_1+\sigma_2)
                         +\frac h2(\theta_1+\theta_2)+n_s\right).
\end{aligned}
\tag{13}
\]
Here W includes its \(\theta X+sX^2\) terms.

For any chosen \(u\ne0\), the equation \(\mathcal F=0\) is realized
over an algebraic closure by roots of
\[
z^2-uz+\frac{u^2+2c+k_1+md/u}{2}=0.
\tag{14}
\]
Repeated roots are permitted. Substitution in (13) gives
\(\mathcal G=u\,\mathcal L(u)\), where the FULL Laurent polynomial is
\[
\begin{aligned}
\mathcal L(u)={}&(B+pd/2)u\\
&-A(2c+k_1)+2C+pe+n_t-k_2k_1/2+hd^2/2\\
&+\frac{d}{u}\left(-Am+he+n_s-pk_1/2-mk_2/2\right)
-\frac{pmd^2}{2u^2}.
\end{aligned}
\tag{15}
\]
A nonzero finite root would contradict the divided-difference unit
ideal, including in the repeated-root case. The identically zero
polynomial is likewise impossible. Therefore \(\mathcal L\) is a
nonzero Laurent monomial.

If \(p=0\), exactly one of its possible \(u,1,u^{-1}\) coefficients
is nonzero; this is only a necessary condition. We now suppose
\(p\ne0\) for contradiction. The coefficient of \(u^{-2}\) is then
nonzero, so all three other coefficients vanish:
\[
\boxed{\begin{aligned}
B&=-pd/2,\\
A&=(he+n_s)/m-k_2/2-pk_1/(2m),\\
2C&=A(2c+k_1)-pe-n_t+k_2k_1/2-hd^2/2.
\end{aligned}}
\tag{16}
\]
No pair coordinate has been made an ambient coordinate, and no
moving root was substituted before coefficient differentiation.

## 4. Complete high potential and multiplier coefficients

The following comparisons use the genuine off-level formal polynomial
\[
\begin{aligned}
H(U,P,V)={}&U^2+F_PU+F_V
       \frac{\ell-(2P+k_1)U-F}{m}\\
&+\frac{k_3}6P^3+\frac{p_t}2P^2V+\frac{h_t}2PV^2
 +\frac{h_s}6V^3
 +\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
 -\ell_tP-\ell_sV.
\end{aligned}
\tag{17}
\]
Differentiate formally before evaluation. Put \(g=H_V^{\rm ev}\).
After only the substitutions (3),(10),(16), the complete coefficients
are
\[
\begin{aligned}
[x^4](\mathcal B_\beta+\kappa f)
       &=(16A+4k_2-2\kappa p)/m,\\
[x^6](H^{\rm ev}-h_0)&=k_3/6-pk_2/(2m)-2pA/m,\\
[x^5](H^{\rm ev}-h_0)&=\frac d2
                          \left(p_t-\frac{h(4A+k_2)}m\right),\\
[x^4]g&=p_t/2-h(2A+k_2/2)/m-p^2/m,\\
[x^4]\mathcal A_\beta&=4A_t,\\
[x^3](\mathcal B_\beta+\kappa f)&=4d_t-2\kappa hd/m.
\end{aligned}
\tag{18}
\]
For the fifth line one uses the full expression
\[
\mathcal A_\beta=\beta^2y_t+\beta\theta_x y_s+y_x^2
                  -\beta\sigma_t y_x-\sigma_s y_x\theta_x.
\]
All moving derivatives of c,d,e,A,B,C are retained. The last line
of (18) is not needed for the terminal contradiction, but records
the nonconstant-theta derivative rather than discarding it.

The first three vanishing coefficients give
\[
\kappa=\frac{2mk_3}{3p^2},\qquad k_3\ne0,\qquad
A=\frac{mk_3}{12p}-\frac{k_2}4,\qquad
3pp_t=hk_3.
\tag{19}
\]
The nonzero \(k_3\) follows from the actual unit \(\kappa\).
The fourth line of (18) is consequently \(-p^2/m\).
The full identity \(\mathcal A_\beta=\kappa g\) then yields
\[
A_t=-k_3/6.
\tag{20}
\]
Differentiate the expression for A in (19) at fixed s.
Since \(k_{2,t}=k_3\), comparison with (20) proves
\[
r:=k_3/p\ne0,\qquad r_t=0,\qquad
3p_t=rh,\qquad A_t=-rp/6\ne0.
\tag{21}
\]
No rationality of any coefficient field was used.

## 5. The actual locally nilpotent derivation forces r complex

Extend N to \(\mathcal B=A[u]\) by \(Nu=0\), and define
\[
\Delta=a_0N-(NX)E.
\tag{22}
\]
This is an actual nonzero locally nilpotent derivation. It fixes X,
acts on A as \(a_0N\), and satisfies
\(\Delta u=-Nx_0\); repeated derivatives of u terminate because
N is locally nilpotent and kills \(a_0\). These facts also prove
local nilpotence on every polynomial in A and u.

Localize at \(\mathbb C[X]\setminus\{0\}\):
\[
\mathbb K=\mathbb C(X),\qquad
\mathcal R=\mathbb K[Y,Z,W],\qquad
\operatorname{Frac}\mathcal R=L(X)(v).
\tag{23}
\]
The last equality follows from the actual sliced ring, not from a
generic polynomial parametrization. Delta is a nonzero LND of
this actual three-variable polynomial ring over \(\mathbb K\).
Its unique extension to the finite separable field
\(L'(X)(x)\) acts as \(a_0\rho\,\partial_x\), killing \(L'(X)\).
We do not identify the original fraction field in (23) with that
possibly larger field or identify the actual ring with \(L'(X)[x]\).

There is a nonconstant polynomial in \(\ker_{\mathcal R}\Delta\).
For example the elementary local-slice argument gives
\(\operatorname{trdeg}_{\mathbb K}\operatorname{Frac}\ker\Delta=2\):
choose a local slice with invariant nonzero derivative and invert
that derivative, obtaining a one-variable polynomial extension
of the localized kernel.

The literal W coefficients from (7),(16) are
\[
[x^4]w=-\frac{2A+k_2/2}{m}=-r/6,\qquad
[x^3]w=0,\qquad
[x^2]w=-r(2c+k_1)/6.
\tag{24}
\]
Hence the actual intrinsic profile is \((2,4,4)\), with leaders
\((X+A,1,-r/6)\). If \(r_s\ne0\), equations (21) imply that
A,r are algebraically independent over \(\mathbb C\), since
their differential determinant is \(A_t r_s\ne0\).
They remain so over the independent field \(\mathbb C(X)\).
Together with an independent leading variable T, the initials
\[
(X+A)T^2,\qquad T^4,\qquad -rT^4/6
\]
would therefore be algebraically independent over \(\mathbb K\).
But a nonconstant actual Delta-invariant has intrinsic degree zero,
so its positive-weight highest part supplies a nonzero relation
among these three initials. This is a contradiction.
Thus \(r_s=0\), and
\[
r\in\mathbb C^*.
\tag{25}
\]
Joint constants of a finite extension of \(\mathbb C(t,s)\) are
\(\mathbb C\); this follows from characteristic-zero differentials
and the algebraic closedness of \(\mathbb C\).

Differentiate \(k_3=rp\) in s. Since \(k_{3,s}=p_{tt}\) and
\(h_t=p_s\), differentiating \(3p_t=rh\) in t gives
\(rp_s=(r/3)p_s\). Thus \(p_s=h_t=0\). Differentiating
\(3p_t=rh\) in s gives \(h_s=0\). Exact subtraction now gives
\[
\begin{gathered}
h\in\mathbb C,\qquad p=rht/3+p_0,\qquad p_0\in\mathbb C,\\
A=-r^2ht^2/36-rp_0t/6+A_0,\qquad A_0\in\mathbb C.
\end{gathered}
\tag{26}
\]
For the last assertion, (19) first gives \(A_s=0\). No primitive
in a presumed rational field is being chosen. If \(h=0\), the
standing condition \(p\ne0\) implies \(p_0\ne0\).

## 6. One actual shear and its entire initial relation

Because r is now proved complex, the shear
\[
\mathcal U=W+rZ/6
\tag{27}
\]
is an actual polynomial coordinate change, with inverse
\(W=\mathcal U-rZ/6\). Its determinant is one. Only the actual
three-ring, scalar, and intrinsic degrees are needed after this
map; no additional chart-entry assertion is made.

Equations (24) give the exact intrinsic profile
\[
\deg_x(Y,Z,\mathcal U)=(2,4,2),\qquad
(Y_{\rm top},Z_{\rm top},\mathcal U_{\rm top})
  =((X+A)T^2,T^4,rt(X+A)T^2/3).
\tag{28}
\]
The first and third initials are algebraically independent over
\(\mathbb K\): their ratio recovers t, and their common degree
variable is transcendental over the coefficient field.
An actual nonconstant Delta-invariant again supplies a relation,
so the entire initial kernel is a height-one prime.

Use formal variables \(\mathsf Y,\mathsf Z,\mathsf U\) of weights
\((2,4,2)\). If \(h\ne0\), put
\[
Q_2=(X+A_0)\mathsf Y^2-(p_0/2)\mathsf Y\mathsf U
                                      -(h/4)\mathsf U^2 .
\]
Equation (26) gives the relation
\[
\mathcal H=\mathsf Y^6-\mathsf ZQ_2^2,\qquad
\operatorname{wt}\mathcal H=12.
\tag{29}
\]
It is irreducible: it is primitive and linear in \(\mathsf Z\),
and \(\gcd(\mathsf Y,Q_2)=1\) because \(h\ne0\).
Thus it generates the entire height-one initial kernel.

If \(h=0\), then \(p_0\ne0\), and the corresponding primitive
relation after cancelling \(\mathsf Y^2\) is
\[
\mathcal H=\mathsf Y^4-\mathsf Z
           ((X+A_0)\mathsf Y-p_0\mathsf U/2)^2,\qquad
\operatorname{wt}\mathcal H=8.
\tag{30}
\]
The same primitive linear-polynomial argument proves irreducibility
and equality with the entire initial kernel. No specialization of X
at a coefficient-dependent root is used.

## 7. The actual coordinate partial gives weight at most seven

In the ACTUAL ring
\(\mathcal R=\mathbb K[Y,Z,\mathcal U]\), use its coordinate partial
\(\mathscr D=\partial/\partial Z\), fixing Y and \(\mathcal U\).
Extend it uniquely across the finite separable coefficient extension.
The full horizontal determinant is still
\[
\det\frac{\partial(Y,Z,\mathcal U)}{\partial(t,s,x)}
                       =-a_0^4/\rho\in L'^* .
\tag{31}
\]
The other two rows have intrinsic degree two. Their t- and s-partials
have degree at most two, and their x-partials have degree at most one.
The inverse-Jacobian coefficients of \(\mathscr D\) therefore have
degrees at most three in the t,s directions and at most four in
the x direction. As \(\partial_x\) lowers degree by one,
\[
\deg_x\mathscr D(G)\le\deg_xG+3
\quad\text{for every }G\in L'(X)[x]\text{ with }\mathscr D(G)\ne0.
\tag{32}
\]
All denominators here are coefficient-field units, not polynomials
in x. The bound follows from the actual nonzero scalar and includes
all moving coefficient derivatives.

Choose a nonconstant \(F\in\ker_{\mathcal R}\Delta\), and let M be
its positive weighted degree. Its highest weighted part belongs
to the initial kernel. Write it as \(\mathcal H^\ell G\), where
\(\ell\ge1\) and \(\mathcal H\nmid G\).
Both (29),(30) are linear in \(\mathsf Z\), so
\(\mathcal H\nmid\mathcal H_{\mathsf Z}\). In characteristic zero,
\[
\partial_{\mathsf Z}^{\,\ell}(\mathcal H^\ell G)
 \equiv \ell!\mathcal H_{\mathsf Z}^{\,\ell}G
                            \not\equiv0\pmod{\mathcal H}.
\tag{33}
\]
Every coordinate Z derivative lowers source weight by four.
Consequently the actual intrinsic degree is EXACTLY
\(\deg_x\mathscr D^\ell F=M-4\ell\).
On the other hand \(\deg_xF=0\), since F is Delta-invariant;
iteration of (32) gives \(M-4\ell\le3\ell\).
Since \(M\ge\ell\,\operatorname{wt}\mathcal H\), this proves
\[
\operatorname{wt}\mathcal H\le7.
\tag{34}
\]
This contradicts both the weights 12 and 8 above. No stronger
filtered-growth equality argument or generic bound is needed.
The assumption \(p=m_t\ne0\) is impossible, proving (1).

## 8. A further necessary restriction in the variable-coupling remainder

The proved \(p=0\) branch has \(m_t=0\). If m is noncomplex, then
\(h=m_s\ne0\). The first line of (18) did not use division by p:
from the full formula (8), with (10) but without (16), it still gives
\(A=-k_2/4\). The complete H coefficient of \(x^6\) is then
\(k_3/6\). Hence \(k_3=0\); also \(k_{2,s}=m_{tt}=0\).
Thus \(k_2\in\mathbb C\) and A is complex.

Without any Laurent-branch choice, the full evaluated gradient and
multiplier now have
\[
[x^3]g=-2hB/m,\qquad [x^3]\mathcal A_\beta=4B_t.
\tag{35}
\]
If \(B\ne0\), the full identity gives
\(B_t=-\kappa hB/(2m)\ne0\). Since \(m_t=0,m_s=h\ne0\),
B,m are algebraically independent over \(\mathbb C\).

In the actual LOCALIZED ring over \(\mathbb K=\mathbb C(X)\),
put \(q=X-k_2/4\in\mathbb K^*\) and use the coordinate shear
\[
Z_1=Z-Y^2/q^2.
\tag{36}
\]
Its inverse is \(Z=Z_1+Y^2/q^2\). This is only a coordinate map
over \(\mathbb K\), not an asserted ambient polynomial map over
\(\mathbb C\). The full literal rows give profile \((2,3,3)\)
and leaders
\[
Y_{\rm top}=qT^2,\qquad
(Z_1)_{\rm top}=-2BT^3/q,\qquad W_{\rm top}=-2BT^3/m .
\tag{37}
\]
Their degree-zero ratios recover
\[
m=q\,(Z_1)_{\rm top}/W_{\rm top},\qquad
B^2=q^5(Z_1)_{\rm top}^2/(4Y_{\rm top}^3).
\tag{38}
\]
The two independent coefficients \(m,B^2\), together with the
independent leading variable T, make these three initials
algebraically independent over \(\mathbb K\). This contradicts
the nonconstant actual Delta-invariant exactly as in Section5.
Consequently the remaining noncomplex-m sector satisfies
\[
\boxed{B=0,\qquad k_{tt}\in\mathbb C,\qquad
             y=-(k_{tt}/4)x^2+C.}
\tag{39}
\]
This is a necessary reduction only. The two remaining Laurent
monomial possibilities have not been excluded here.

## 9. Verification and retained boundary

The entire264,296 and535 sources were read before this derivation.
Fresh unsaved7f8409 reconstructed the complete divided W identity
and Laurent expression. Fresh eda796 checked the full multiplier
degree comparisons, and5f6f81/c039ac checked the complete high
potential and multiplier coefficients with unrestricted lower jets.
Fresh93f508 reconstructed the full formal H, its evaluated gradients,
all six identities in (18), the three literal W leaders in (24),
and both initial relations; all residuals were zero. Fresh db185f
also reconstructed every literal leader in (37), including both
cancelled quartic terms; all residuals were zero.
The independent outline checks of the full Laurent identity and
the degree bound are separate from a saved-source review.

The written actual-ring, irreducibility, local-slice and derivative
arguments supply the licenses not proved by symbolic expansion.
In particular the finite extension and intrinsic affine reparameter
are not ambient normalizations. The ambient shear (27) uses the
proved complex constant r only; (36) is expressly localized.

The main result is \(m_t=0\) and \(\deg_v y\le2\) for quadratic
sigma and NONCONSTANT affine theta in the supplied chart, with
the further necessary reduction (39) when m is noncomplex.
The monomial alternatives in (15) with \(p=0\) remain constraints,
not a solved branch. Constant theta is not an additional conclusion
of this note. No nonlinear-sigma-wide exclusion, recognition,
arbitrary chart entry, unrestricted cancellation, novelty or external
certification is claimed.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical file was edited. A complete independent
saved-source review remains separate from this author verification.
