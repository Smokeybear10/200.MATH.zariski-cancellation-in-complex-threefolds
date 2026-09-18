# A necessary degree-drop ODE and two conditional coefficient families

Working bounded reduction: in the FULL actual degree-drop sector512,
retain the nonzero quadratic coefficient of y supplied by515 and
assume also that the original W row has nonzero cubic intrinsic
coefficient. Two existing dimensionless coefficient functions satisfy
the necessary first-order system below. If the first is constant,
or if the pair lies on one specified invariant curve, the coefficient
functions admit the explicit root-free descriptions proved here.

These two cases are NOT asserted to exhaust the system's trajectories.
Neither family is asserted to satisfy the lower genuine levels, the
full nonzero scalar, the actual polynomial-ring returns, or actual
chart existence. No exclusion, converse, recognition or unrestricted
cancellation theorem is claimed.

## 1. Actual entry and the exact one-variable coefficient field

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and unit minors of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
the unrestricted unit multiplier of
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md),
and the complete degree-drop reduction
[512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md).
Thus the original slice and actual ring are
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,
\qquad L=\operatorname{Frac}\ker_A N,
\qquad [L:\mathbb C(t,s)]<\infty,\\
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\quad
Na_0=Nt=Ns=0,\\
\operatorname{Frac}A=L(P)=\mathbb C(y,z_0,w_{\rm int}),\qquad
L[y,z_0,w_{\rm int}]=O,\qquad
L[X,Y,Z,W]=L[X,P],\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
The original selected partial, both actual returns, and full scalar
remain required. In particular the scalar is not replaced by a
nonzero formal leading coefficient.

The exact coefficient partials commute and have joint constants C.
Put \(F_0=\ker_L\partial_s\), a finite extension of C(t) whose
exact t-derivative constants are C. Neither F0 nor L is assumed
rational. A prime means that exact t derivative, not a derivative
after an unlicensed change of parameters.

The present sector is
\[
\begin{gathered}
m=k_s\ne0,\quad m_s=0,\quad m\notin\mathbb C,\quad
p=m'\ne0,\quad q=m'',\\
\theta=-P^2/m+bP+c,\qquad
y=eP^2+lP+r,\qquad e\in F_0,\qquad e\ne0,\\
g_3=[P^3]w_{\rm int}=(p-2me)/m^2\ne0.
\end{gathered}
\tag{2}
\]
Here y has degree at most two by512's direct monic argument, not
327's quadratic-level parity. The necessary exclusion of e=0 is
the separately accepted
[515](principal-paraboloid-degree-drop-zero-quadratic-exclusion-pass515-working.md).
The condition g3 nonzero is an ADDITIONAL restriction of this note;
the g3 zero branch is not settled by the ODE analysis below.

By512 the quadratic H_U coefficient is nonzero:
\[
F_2=2e-3p/m\ne0.
\tag{3}
\]
No assumption that q, a later normalized variable, or its derivative
is nonzero is added.

## 2. The complete retained necessary equations and their reduction

The two genuine high equations proved from the full scalar and
minor in512 are
\[
\begin{aligned}
\mathcal E={}&-12m^3e^3+30m^2pe^2-6m^3ee'
       +9m^2qe-18mp^2e+9m^2pe'\\
 &\hspace{13mm}+m^2m'''-6mpq+6p^3=0,\\
\mathcal T={}&-4e^3m^2+2e^2mp-2ee'm^2-emq+2ep^2+3e'mp=0.
\end{aligned}
\tag{4}
\]
The second equation uses the already proved F2 nonzero in (3).
These equations retain the exact coefficient derivatives. They are
necessary consequences only, not a replacement for the other actual
conditions in (1).

Define EXISTING elements of F0 and an exact rescaled derivation by
\[
h=me/p,\qquad u=\dot h,\qquad
w=mq/p^2,\qquad \zeta=m^2m'''/p^3,\qquad
\dot{\ }=\frac mp\frac d{dt}.
\tag{5}
\]
The letter w here is the normalized second derivative, not the
original intercept w_int in (1). The dot derivation has the same
constant field C as the prime derivative because m/p is nonzero.
There is no introduction of a logarithm of m or a new independent
ambient coordinate.

Since \(e=hp/m\), exact differentiation gives
\[
e'=\frac{p^2}{m^2}\{u+h(w-1)\}.
\tag{6}
\]
The full identities after substitution into (4) are
\[
\begin{aligned}
\widehat T:=\frac{m\mathcal T}{p^3}
 &=(3-2h)u-4h^3-2h^2w+4h^2+2hw-h,\\
\frac{\mathcal E}{p^3}
 &=3\widehat T+24h^2+12hw-24h-6w+\zeta+6.
\end{aligned}
\tag{7}
\]
Every derivative term in (4) is included in these equalities.

Now put
\[
v=2h-1\in F_0.
\tag{8}
\]
This v is a coefficient function, not the original intrinsic slice
parameter used to obtain P. The exact nonzero factors in (2),(3)
give
\[
g_3=-pv/m^2\ne0,\qquad
e=p(v+1)/(2m)\ne0,\qquad
F_2=p(v-2)/m\ne0.
\tag{9}
\]
Thus \(v\ne0,-1,2\) as elements of the coefficient field.
These statements do not remove places at which a nonzero function
has a zero or pole.

Because \(3-2h=2-v\ne0\), the first equality in (7) solves
for dot h. The second then gives \(\zeta=-6v(v+w)\).
Direct differentiation of w also gives
\(\dot w=w+\zeta-2w^2\). Consequently
\[
\boxed{
\dot v=\frac{(v+1)\{v^2+(v-1)w\}}{2-v},\qquad
\dot w=-2w^2+(1-6v)w-6v^2.
}
\tag{10}
\]
The derivation additionally satisfies \(\dot m=m\) and
\(\dot p=wp\). These are identities, not extra equations
imposed on a putative actual realization.

## 3. Conditional family I: v is constant

Assume now \(\dot v=0\). The exact constant-field statement
implies \(v=v_0\in\mathbb C\). In addition to the exclusions
in (9), v0 cannot be one: the numerator of the first equation
in (10) would then be two. Therefore that equation gives
\[
w=-\frac{v_0^2}{v_0-1}\in\mathbb C.
\tag{11}
\]
Its dot derivative is zero. Substitution in the second equation
of (10) gives the exact factorization
\[
0=-\frac{v_0^2(2v_0^2-5v_0+5)}{(v_0-1)^2}.
\tag{12}
\]
The factors already checked nonzero may now be removed. Hence
\[
2v_0^2-5v_0+5=0,\qquad w=-5/2.
\tag{13}
\]
Both complex roots are retained. In particular no real-coefficient
restriction has been introduced. The value v0 is an existing
coefficient constant satisfying (13), not a newly adjoined root.

The last equation says \(mq=-5p^2/2\). It gives two exact
integrals inside F0:
\[
c_*:=m^5p^2\in\mathbb C^*,\qquad
T:=\frac{2m}{7p},\qquad T'=1.
\tag{14}
\]
Indeed \((m^5p^2)'=m^4p(5p^2+2mq)=0\), and
\(T'=(2/7)(1-w)=1\). Thus \(T=t-\tau\) for some
\(\tau\in\mathbb C\). No primitive or algebraic root is
postulated. Multiplying the two existing identities in (14) gives
the necessary family
\[
\boxed{
\begin{gathered}
m^7=c_7(t-\tau)^2,\qquad
c_7=49c_*/4\in\mathbb C^*,\quad \tau\in\mathbb C,\\
p=\frac{2m}{7(t-\tau)},\qquad
e=\frac{v_0+1}{7(t-\tau)},\qquad
2v_0^2-5v_0+5=0.
\end{gathered}}
\tag{15}
\]
The existing m, possibly algebraic and not rational in t, satisfies
this relation. No choice of a seventh-root function or enlargement
of F0 is made. Also \(t-\tau\ne0\) as a field element, since
its derivative is one. Neither F0=C(t,m) nor any converse actual
realization follows from (15).

## 4. Conditional family II: w+2v vanishes

The entire system (10) satisfies the polynomial-rational identity
\[
\dot{(w+2v)}=(w+2v)
          \frac{4v^2+2vw-5v-4w}{2-v}.
\tag{16}
\]
Thus w+2v=0 is an invariant curve of this necessary coefficient
system. This calculation does not show that an arbitrary solution
lies on that curve.

Assume now exactly \(w+2v=0\). Equation (10) reduces to
\[
\dot v=v(v+1),\qquad w=-2v.
\tag{17}
\]
The exclusions v=0 and v=-1 from (9) show that v is nonconstant
in this conditional family. In particular it is not a missed
constant-v case of Section3.

Using \(\dot m=m\), form the EXISTING nonzero quotient
\[
C:=\frac{v}{m(v+1)}\in\mathbb C^*.
\tag{18}
\]
Its dot derivative is zero by (17), and its nonzero numerator and
denominator have already been justified. Solving this algebraic
identity gives
\[
v=\frac{Cm}{1-Cm},\qquad
w=-\frac{2Cm}{1-Cm},\qquad
1-Cm=\frac1{v+1}\ne0.
\tag{19}
\]
Since \(\dot p=wp\), direct differentiation gives the second
existing nonzero constant
\[
K:=\frac{p}{(1-Cm)^2}\in\mathbb C^*.
\tag{20}
\]
This K is unrelated to the genuine scalar multiplier kappa.
Neither C nor K is allowed to be zero, for the reasons just given.
No division by q, w, or a coefficient derivative was used.

The prime derivative of \((1-Cm)^{-1}\) is CK. Therefore
\[
\frac1{1-Cm}=CK(t-\tau),\qquad \tau\in\mathbb C.
\tag{21}
\]
This is again exact subtraction in F0, not an assumption of
rationality. Equations (19)--(21) give the necessary family
\[
\boxed{
\begin{aligned}
m&=\frac1C-\frac1{C^2K(t-\tau)},\\
v&=CK(t-\tau)-1,\qquad w=-2\{CK(t-\tau)-1\},\\
p&=\frac1{C^2K(t-\tau)^2},\\
e&=\frac{CK}{2\{CK(t-\tau)-1\}}
   =\frac1{2\{t-\tau-1/(CK)\}},\\
C,K&\in\mathbb C^*,\qquad \tau\in\mathbb C.
\end{aligned}}
\tag{22}
\]
Here the particular functions m,e are rational in t as a conclusion
of this conditional calculation. F0 and all other coefficient
functions are not asserted rational. The nonzero field denominators
in (22) follow from (9),(18)--(21). No places are deleted, and no
time translation in these field formulas is asserted to be an
actual ambient coordinate map.

## 5. Zero boundaries and what remains to be tested

The derivation of (10) divides only by m,p and v-2, already nonzero
under the stated actual sector. It does not divide by q, w, dot v,
or dot w. Section3 treats dot v=0 directly, and excludes v0=1
before dividing by v0-1. Section4 assumes the specified curve and
uses only the justified nonzero v,v+1,m,p and their resulting
nonzero constants. The forbidden identically constant values
v=0,-1,2 belong to other branches identified respectively by
g3=0, e=0 and F2=0. This note does not silently discard any
additional zero case.

Both conditional families still have the full lower coefficient
functions b,c,l,r,n,ell, their exact derivatives and the genuine
levels to satisfy. In particular the full scalar in (1) must be
nonzero and independent of X,P, not just compatible with (4).
The original actual-ring and whole-return assumptions must also
hold. Verifying only the two ODEs cannot establish these conditions.

The two cases proved here do not classify other trajectories of
(10), nor show that every actual solution falls into either case.
There is no claim that a formal choice of constants in (15) or
(22) supplies a polynomial four-ring or an actual chart.

## 6. Verification and retained dependencies

The complete held512 source was read through EOF. The complete
accepted515 source was also read through EOF before this note,
at SHA cd6b2f7e78c4607e4a781ce5b6b158a3b8efc75a8c92c948a052ab0947404a4c.
Their results are retained inputs, not recursively certified here.
Only515's exclusion of e=0 is used; its separate classification
argument is not reapplied in the present generic branch.

Fresh unsaved1953d9 reconstructed the entire normalized E/T
identities (7), both vector-field components (10), the complete
constant-v factor (12), the invariant-curve factor (16), and
the displayed fractional-linear substitution. All residuals were
zero. Fresh ee11cc independently checked both exact constants
(18),(20), the constant-v time derivative, and substitution of
(22) into the ENTIRE original equations (4), with zero residuals.
Root's independent2e9c07,368417 and9d5dd1 agree on the ODE and
constant-v calculations.

These finite algebra checks supplement the written exact-field
integrations, nonzero-factor arguments and boundary distinctions.
No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical record was edited. No broader ODE
classification, actual realization or cancellation claim is made.

