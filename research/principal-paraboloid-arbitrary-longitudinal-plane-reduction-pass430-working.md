# A plane reduction with arbitrary longitudinal coupling

Working necessary reduction: in the full actual264 chart, assume
\[
k=s+f,\qquad f\in\mathbb F:=\ker_L\partial_s,
\qquad n_s=0,\qquad e:=\ell_s\ne0.
\tag{1}
\]
There is no bound on f''' or n'''. The complete third and fourth
potentials give the WHOLE polynomial-plane return O=L[y,sigma],
and a plane polynomial Phi of total degree at most six, constant
on the actual line, whose evaluated gradient generates O.
All level derivatives are retained.

This note supplies the literal primitive and exact plane reduction.
It makes no original-coordinate conclusion from the plane parameter,
does not solve the remaining scalar conditions, and asserts no
realization of arbitrary formal data. A weighted leading form is
recorded for separate geometric analysis, not used here to claim
recognition or an exhaustive exclusion.

## 1. Full actual input

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad[L:\mathbb C(t,s)]<\infty,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
J_{t,s,v}(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
                         =-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The equality with the three projected functions uses m=k_s=1.
The original slice, actual localization, selected coordinate partial,
both returns, genuine levels and full calibration remain assumptions.
All coefficient partials commute, extend exactly to L and fix v.
Their joint constant field is C. The field F in(1) is finite over
C(t), but is not assumed equal to C(t). Since n_s=0, n also lies
in F. A prime on f or n denotes the exact t-derivative.

The complete literal rows and first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n'\sigma.
\end{aligned}
\tag{3}
\]
In particular ell can depend on both coefficient parameters even
though f and n do not. Neither e nor its derivatives are assumed
constant. No actual change of X,Y,Z,W is made in this note.

## 2. Complete third and fourth potentials

Use independent formal variables U,P,V over L. The third potential
specializes exactly to
\[
\boxed{H=U^2+(f''P+n')U+\frac{f'''}6P^3
              +\frac{n''}{2}P^2-\ell_tP-eV,}
\quad H(y,\sigma,\theta)=h_0\in L.
\tag{4}
\]
The level h0 is NOT presumed s-constant. The complete fourth
primitive normalized by Q(0,0,0)=0 is
\[
\boxed{\begin{aligned}
Q={}&\frac{f''}{2}U^2
 +\left\{\frac{f'''}2P^2+(n''+2e)P+f'e-\ell_t\right\}U\\
 &+\frac{f''''}{24}P^4+\frac{n'''}6P^3
          +\frac{f''e-\ell_{tt}}2P^2
          -\ell_{ts}PV-\frac{\ell_{ss}}2V^2\\
 &+(n'e-h_{0,t})P-h_{0,s}V,
\end{aligned}}
\qquad Q(y,\sigma,\theta)=q_0\in L.
\tag{5}
\]
The coefficients h0_t,h0_s are the actual derivatives of the third
level. Dropping either gives a different formal differential identity.
The new level q0 is another exact element of L, not a complex constant.

Here is a direct derivation from the completely read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
Its notation has m=1, lambda=F_V/m=0, D=2P+f',
F=f''P^2/2+n'P, and beta=2U+f''P+n'. The corrected gradient
components therefore become
\[
\begin{aligned}
Q_U&=H_P-(2P+f')H_V,\\
Q_P&=H_t-h_{0,t}-(2U+f''P+n')H_V,\\
Q_V&=H_s-h_{0,s}.
\end{aligned}
\tag{6}
\]
All coefficient derivatives on the right hold U,P,V fixed.
Since H_V=-e, differentiation of(5) gives respectively
\[
\begin{aligned}
Q_U={}&f''U+\frac{f'''}2P^2+(n''+2e)P+f'e-\ell_t,\\
Q_P={}&\{f'''P+n''+2e\}U+\frac{f''''}{6}P^3
 +\frac{n'''}2P^2+(f''e-\ell_{tt})P
                         -\ell_{ts}V+n'e-h_{0,t},\\
Q_V={}&-\ell_{ts}P-\ell_{ss}V-h_{0,s}.
\end{aligned}
\tag{7}
\]
These are precisely(6). Normalization at the origin fixes the
primitive.296 then identifies its evaluated v-derivative with the
linear coefficient of the full scalar after using H=h0, and hence
gives the level q0 in(5). Thus(5) is not a guessed polynomial
relation or an integration that ignores moving coefficient levels.

## 3. Exact graph elimination and whole plane return

Define polynomials over L by
\[
\begin{aligned}
S(U,P)&=U^2+(f''P+n')U+\frac{f'''}6P^3
               +\frac{n''}{2}P^2-\ell_tP-h_0,\\
T(U,P)&=S(U,P)/e.
\end{aligned}
\tag{8}
\]
The division by e is legitimate in the coefficient FIELD L because
e is nonzero. It is not asserted to be a unit of A or an allowed
ambient-coordinate denominator. Equation(4) is exactly
\[
\boxed{\theta=T(y,\sigma),\qquad
O=L[y,\sigma,\theta]=L[y,\sigma].}
\tag{9}
\]
The corresponding intercepts in this plane presentation are
\[
z=2ty+\sigma^2+f'\sigma+T(y,\sigma)+n,
\quad
w=\ell-(2\sigma+f')y-f''\sigma^2/2-n'\sigma.
\tag{10}
\]
They remain the original chart intercepts; this does not express
the ambient ring as a polynomial ring in coefficient-field variables.

Let Q0(U,P):=Q(U,P,0), and define the full plane primitive
\[
\boxed{\begin{aligned}
\Phi(U,P)&:=Q(U,P,T(U,P))\\
 &=Q_0(U,P)-\frac{\ell_{ts}P+h_{0,s}}e S(U,P)
                  -\frac{\ell_{ss}}{2e^2}S(U,P)^2.
\end{aligned}}
\qquad\Phi(y,\sigma)=q_0.
\tag{11}
\]
This compact expression keeps every coefficient of(5), including
both level derivatives. Since deg S is at most three, it gives
\[
\deg\Phi\le6.
\tag{12}
\]
No denominator depends on U,P. Consequently Phi is a polynomial
over L even when the exact field L is not rational.

## 4. Evaluated gradient unit and the exact selected cofactor

The unit ideal of evaluated gradient minors in296 is essential
here. Put
\[
M_{UP}=H_UQ_P-H_PQ_U,\quad
M_{UV}=H_UQ_V-H_VQ_U,\quad
M_{PV}=H_PQ_V-H_VQ_P.
\tag{13}
\]
Their evaluations at(y,sigma,theta) generate O under the full actual
scalar(2). Formal differentiation of the graph, at fixed coefficients,
uses T_U=H_U/e and T_P=H_P/e. Hence on V=T(U,P),
\[
\boxed{\Phi_U=M_{UV}/e,\qquad \Phi_P=M_{PV}/e,
\qquad M_{UP}=H_U\Phi_P-H_P\Phi_U.}
\tag{14}
\]
The nonzero coefficient e is a unit of O=L[v]. Equations(13),(14)
therefore identify the two ideals after evaluation and prove
\[
\boxed{(\Phi_U(y,\sigma),\Phi_P(y,\sigma))O=O.}
\tag{15}
\]
In particular Phi is not a constant polynomial and Phi-q0 is a
nonzero plane relation. The single component H_V=-e already makes
the first gradient nonzero, but this alone would NOT imply(15);
the full two-gradient minor conclusion is used.

For precision, the evaluation map L[U,P] onto O in(9) has a
height-one prime kernel generated by an irreducible polynomial G.
Write Phi-q0=G C1. On the actual line its gradient is
C1(y,sigma) times the evaluated gradient of G. From(15),
C1(y,sigma) must be a unit of O, hence some eta in L*. Thus
C1-eta belongs to the same kernel and
\[
\boxed{\Phi-q_0=\eta G+G^2R,
\qquad\eta\in L^*,\quad R\in L[U,P].}
\tag{16}
\]
This proves in particular that the selected plane component occurs
with multiplicity one. It does not assert that Phi-q0 is irreducible
or that other components cannot be present. No plane coordinate
over C is inferred from the exact polynomial-line isomorphism.

## 5. Total and weighted leading terms

For total degree, if f''' and ell_ss are both nonzero, the unique
degree-six term of(11) is
\[
\boxed{\operatorname{in}_{\rm total}\Phi
 =-\frac{\ell_{ss}(f''')^2}{72e^2}P^6.}
\tag{17}
\]
If ell_ss=0, formula(11) has total degree at most four. If f'''=0,
S has total degree at most two and the same bound four holds; when
ell_ss is nonzero in that case the U^4 coefficient is
-ell_ss/(2e^2), so its total degree is exactly four. These assertions
keep the zero boundaries rather than dividing f''' or ell_ss away.

There is a sharper weighted statement for the genuinely new
f'''ell_ss nonzero subcase. Assign weight three to U and weight two
to P, and put
\[
\mathcal C(U,P)=U^2+\frac{f'''}6P^3.
\tag{18}
\]
The weighted top of S is Ccal of weight six. All terms of
Q0-(ell_ts P+h0_s)S/e have weight at most eight: the largest are
the P^4 term and the product P S. Thus
\[
\boxed{\operatorname{in}_{(3,2)}\Phi
       =-\frac{\ell_{ss}}{2e^2}\mathcal C^2,
       \qquad\operatorname{wt}\Phi=12.}
\tag{19}
\]
This exact top, not just the total P^6 term, is available for further
analysis. For example Ccal is irreducible in L[U,P] when f''' is
nonzero: over L(P), the element -(f'''/6)P^3 is not a square because
its P-adic valuation is odd, and Gauss's lemma applies. From G dividing
Phi-q0 it follows that
\[
\operatorname{in}_{(3,2)}G=\kappa\mathcal C^j,
\quad\kappa\in L^*,\quad j\in\{1,2\},
\quad \deg_U G=2j,\quad\deg_P G=3j.
\tag{20}
\]
The weighted initial product is multiplicative, and a nonconstant G
has positive weight, so j=0 cannot occur. No smooth-projective-curve,
root-counting or polynomial-embedding degree theorem is applied in
this note to turn(20) into an exclusion.

## 6. Exact coefficient reparametrization and unresolved obligations

If useful for subsequent coefficient work, r=ell is a separating
parameter with t because ell_s=e is nonzero. The finite field L is
also finite over C(t,r), and the exact coefficient operators are
\[
\partial_r=e^{-1}\partial_s,\qquad
\left.\partial_t\right|_r=\partial_t-(\ell_t/e)\partial_s.
\tag{21}
\]
They commute and restrict to the same exact derivative on F.
Writing s=Hcal(t,r) in L gives Hcal_r=1/e. These are coefficient
field identities only. Neither r nor Hcal is thereby an original
polynomial coordinate, and a later scalar calculation must hold
the stated parameters fixed.

All remaining lower coefficients, the actual constant scalar,
the actual localization and both returns stay in force. In particular
(9),(11),(15) are necessary consequences, not sufficient conditions
for constructing a globally sliced polynomial four-ring. Even a
classification of polynomial solutions of Phi=q0 would not by itself
give an original-ring recognition theorem.

## 7. Verification record

The full264 source was read for the current general-coupling work.
The complete296 source was freshly read through79091b+b07403 before
the derivation. Fresh unsavedc62a08 reconstructs every formal
gradient in(6),(7), both graph/minor identities, the complete compact
substitution, and the total/weighted tops. All residuals are zero.
A deliberate omission of -h0_s V leaves the nonzero formal residual
h0_s in the V-gradient, checking the level-derivative boundary.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited. The exact symbolic checks do not
replace the written whole-ring, ideal or field arguments. Independent
review, any further geometric exclusion, and any original-ring
recognition remain separate obligations. No expert verification,
proof-assistant certification, novelty clearance, global cancellation
solution or external submission is claimed.
