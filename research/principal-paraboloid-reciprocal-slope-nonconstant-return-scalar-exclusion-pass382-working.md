# A highest scalar coefficient excludes the reciprocal nonconstant-return boundary

Working exclusion: in the complete actual nonzero-E family of376,
suppose the scalar reduction378 has H=b/t^2 with b complex nonzero,
and G0' is nonzero. The coefficient-plane change
eta=sigma+s/(2t) is then invertible over F. In the parameters
(t,eta,r), the highest part of the literal intercept determinant
has a nonzero r-seventh coefficient. This contradicts379's
coefficient-field-valued scalar calibration.

The proof retains the arbitrary remaining coefficient l in the
exact finite field F. It uses no Abhyankar--Moh theorem and
does not promote the coefficient-plane change to an actual
automorphism of the original four-ring.

## 1. Precise actual entry and the reciprocal boundary

Retain every actual hypothesis and conclusion of
[376](principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md),
together with the independently scoped scalar consequences of
[378](principal-paraboloid-quadratic-cubic-sixth-scalar-gate-pass378-working.md)
and the original-ring consequences of
[379](principal-paraboloid-quadratic-cubic-polynomial-return-speeds-pass379-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad
E_{\rm slice}=\partial_u,\qquad
\deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
N=[u^4]\partial_Z|_{A_0},\qquad a_0=E_{\rm slice}X\ne0,\\
F=\ker_L\partial_s,\qquad [F:\mathbb C(t)]<\infty,\qquad
L=F(s),\qquad K=F(s,r)=\mathbb C(y,z,w),\\
F[\mathcal B]=F[X,s,r],\qquad F[A_0]=F[s,r],\qquad
a_0,\rho:=Nr\in F^*,\\
J_{t,s,r}(X)=
\det\frac{\partial(Y,Z,W)}{\partial(t,s,r)}
=-a_0^4/\rho\in F^*.
\end{gathered}
\tag{1}
\]
The scalar is independent of s,r,X; this is the substantive
original-slice and polynomial-return conclusion of379, not an
assumption drawn from a rational parametrization. The exact
t-derivative on F has constants C. Neither F=C(t) nor any
original-coordinate property of s or r is assumed.

The intrinsic pair is (deg_r sigma,deg_r theta)=(2,3), k=s,
and the actual normalization has n=-s^2/(4t^2)+f.
Consider specifically the c1=0 boundary of378:
\[
H=\frac b{t^2},\qquad b\in\mathbb C^*,\qquad G_0'\ne0.
\tag{2}
\]
This note does not address its complement or the G0'=0 case.

By376, E=d t^3H^4, with d complex nonzero. Put D=d b^4.
The exact identities E=g'/3+g/t and f''=2g integrate in F to
\[
\begin{gathered}
E=\frac D{t^5},\qquad
g=\frac{g_0}{t^3}-\frac{3D}{t^4}=\frac M{t^4},\qquad
M=g_0t-3D,\\
f=\frac{g_0}{t}-\frac D{t^2}+f_1t+f_0,\qquad
D\in\mathbb C^*,\quad g_0,f_1,f_0\in\mathbb C.
\end{gathered}
\tag{3}
\]
Indeed (t^3g)'=3D/t^2; subtraction of its displayed primitive
leaves a complex constant. The second integration subtracts the
displayed primitive of f'' and leaves a complex affine function.
The element M is nonzero, since g is nonzero. The case g0=0
is retained throughout.

The companion equation of378 similarly gives
\[
G_0'=\frac{\lambda b^2}{t^2},\qquad
G_0=G_{00}-\frac{\lambda b^2}{t},\qquad
\lambda\in\mathbb C^*,\quad G_{00}\in\mathbb C.
\tag{4}
\]
Nonzero lambda is precisely the present G0' nonzero assumption.
All integrations use the exact constant field, not rationality
of F.

## 2. The remaining plane coefficients

In the notation of376,
\[
\sigma=A r^2+B r+e,\qquad e=e_0+e_1s+e_2s^2.
\]
Substitute(2)--(4) into its coefficient formulas. They give
\[
\begin{gathered}
\beta=e_2=0,\qquad
A=-\frac{4D t^5}{bM^2},\qquad
B=-\frac{2\lambda b t^3}{M},\\
e_1=-\frac{\lambda b^2}{M}-\frac1{2t},\qquad
q:=e_0\in F,\qquad
k:=-\frac{\lambda b^2}{M}\in F^*.
\end{gathered}
\tag{5}
\]
Here B is the linear-in-r coefficient of sigma. The letter k
in(5) is a newly named coefficient-plane slope, not the normalized
first potential k=s; only within the formulas below does it have
this meaning. In particular
\[
\sigma=A r^2+B r+q+\left(k-\frac1{2t}\right)s.
\tag{6}
\]
The proof will work with arbitrary q in F. It does not use the
explicit remaining formula for e0 in terms of l.

The second coefficient potential remains
\[
\ell=-\frac{s^3}{4t^4}-\frac{Hs^2}{4t^2}
       +\frac{(f-tf'-G_0)s}{2t^2}+l,\qquad l\in F.
\tag{7}
\]
With C=ell_s+s^2/(4t^4), Lambda=2sC/t+ell_t, direct
differentiation, using H'=-2H/t and(4), gives
\[
\Lambda=\left(-\frac gt+\frac{kg}{2}\right)s+l'.
\tag{8}
\]
For example its quadratic-in-s coefficient is
-(2H+tH')/(4t^3)=0, and its linear coefficient is
-g/t-G0'/(2t^2)=-g/t+kg/2.
No derivative of l has been set to zero.

## 3. An invertible coefficient-plane change and its scalar factor

Define solely in the field-adjoined polynomial plane
\[
\eta=\sigma+\frac{s}{2t}=A r^2+B r+q+ks.
\tag{9}
\]
Since k belongs to F*, it has the polynomial inverse
\[
s=\frac{\eta-r(Ar+B)-q}{k}.
\tag{10}
\]
Thus F[s,r]=F[eta,r], and eta,r are algebraically independent
over F. The coefficients may depend on t. This is not an actual
polynomial automorphism over C and eta is not asserted to be
an original coordinate.

The complete change of parameters (t,s,r) to (t,eta,r) has
Jacobian k. Consequently, with every derivative holding the
displayed independent variables fixed, the chain rule gives
\[
\widehat J_0:=
\det\frac{\partial(y,z,w)}{\partial(t,\eta,r)}
=\frac1k\,J_{t,s,r}(0)
=-\frac{a_0^4}{k\rho}\in F^*.
\tag{11}
\]
The t-dependence of(9) contributes off-diagonal entries but does
not change this triangular determinant. The F-valued assertion
in(11) uses379 essentially. Without it, an old scalar in F(s)
could acquire eta,r dependence after(10).

## 4. Exact compact intercepts with arbitrary l and q

Put K_r=Ar+B and define only as an expression
\(\mathcal Y=y+f'/2\).
The literal third-level parametrization of376, after(8), gives
\[
\boxed{
\begin{aligned}
\mathcal Y
 &=\frac r2
   -K_r\left\{\frac g4(3\eta-rK_r+q)-\frac{l'}2\right\}
   -\frac{s\eta}{2t^2},\\
z&=\eta^2+2tr+Hs+G_0,\\
w&=-2\eta\mathcal Y+\frac{sr}{t}
                       +\frac{Hs^2}{4t^2}+l .
\end{aligned}}
\tag{12}
\]
In(12), substitute s from(10) when using eta,r as parameters.

Here is an algebraic derivation retaining the literal potentials.
Since sigma-e=rK_r, the third relation is
\[
\theta=tK_r\{g(\sigma+e)-\Lambda\}
               +2s\sigma/t+tr-2t^2C.
\]
Insert this into
y=r-theta/(2t)+s sigma/(2t^2)-n_t/2-tC.
Use n_t=s^2/(2t^3)+f' and
sigma=eta-s/(2t). Also
\[
g(\sigma+e)-\Lambda
 =\frac g2(3\eta-rK_r+q)-l'
\]
by(8)--(10). This gives the first row of(12).
The second is the retained exact square presentation of372/376.
For the third, eliminate theta from the literal second potential
w=ell-2sigma*y-n_t*sigma+s theta/(2t^2).
The identity
ell-s ell_s-s^3/(2t^4)=Hs^2/(4t^2)+l
then gives precisely the displayed expression.
These are identities of full polynomials, not just leading forms.

## 5. A nonzero seventh-degree determinant coefficient

View the intercepts in F[eta,r], with ordinary total degree in
eta,r. Equations(10),(12) give exact degrees three, two and four
for y,z,w. Their highest parts are
\[
\begin{aligned}
y_3&=a r^3+b_1r^2\eta,\\
z_2&=c r^2+\eta^2,\\
w_4&=d_1r^4-2a r^3\eta-2b_1r^2\eta^2,
\end{aligned}
\tag{13}
\]
where
\[
\begin{aligned}
a&=\frac{gA^2}{4}=\frac{4D^2t^6}{b^2M^3},&
b_1&=\frac{A}{2kt^2}=\frac{2Dt^3}{\lambda b^3M},\\
c&=-\frac{HA}{k}=-\frac{4Dt^3}{\lambda b^2M},&
d_1&=\frac{HA^2}{4t^2k^2}
       =\frac{4D^2t^6}{\lambda^2b^5M^2}.
\end{aligned}
\tag{14}
\]
All four are nonzero. The subtraction of f'/2 from mathcal Y
has degree zero, so it does not alter y3.

The t-derivative preserves degree in eta,r, while the other two
columns each lower that degree by one. Therefore the total-degree
seven part of the determinant in(11) is obtained entirely from
(13). No lower-degree part of any row can contribute to it.
At eta=0, the three leading derivative rows are
\[
\begin{pmatrix}
a'r^3&b_1r^2&3ar^2\\
c'r^2&0&2cr\\
d_1'r^4&-2ar^3&4d_1r^3
\end{pmatrix}.
\tag{15}
\]
Their determinant gives
\[
[r^7\eta^0]\widehat J_0
=4ac\,a'-(4b_1d_1+6a^2)c'+2b_1c\,d_1'.
\tag{16}
\]
For a short exact simplification, M'=g0 and(14) give
\[
\frac{a'}a=\frac6t-\frac{3g_0}{M},\quad
\frac{c'}c=\frac3t-\frac{g_0}{M},\quad
\frac{d_1'}{d_1}=\frac6t-\frac{2g_0}{M}.
\tag{17}
\]
The b1*d1 terms in(16) cancel. Its remaining value is
6a^2c(1/t-g0/M)=-18D a^2c/(tM). Hence
\[
\boxed{
[r^7\eta^0]\widehat J_0
=\frac{1152D^6t^{14}}{b^6\lambda M^8}\ne0.
}
\tag{18}
\]
This contradicts the constant-in-eta,r calibration(11).

Every denominator in(18) is already nonzero: b,D,lambda are
nonzero complex constants, t is transcendental over C, and M
is nonzero because g is nonzero. The argument includes g0=0
and all possible values and derivatives of l,q.

## 6. Scope and evidence

Thus the complete actual376 boundary H=b/t^2, G0' nonzero
cannot occur. The G0'=0 case and the complementary reciprocal
slope family are outside this note. No assumption that l or F
is rational was needed, and no coordinate was obtained by
promoting(9) to the original ring.

The final376 source was fully revalidated during378. The complete
379 source was freshly read through EOF in6858a8 before using its
F-valued scalar. Its polynomial-ring and speed conclusion is an
essential retained input, not inferred here from field equality.

Fresh unsaved compact-row expansion fff56f completed on its
original handle61520 in73beb1 and found(18). A separate
reconstruction6ce15a verified all three full identities(12)
directly from the literal third and second potentials, then
independently computed the leading-form determinant(15)--(18).
The earlier large expression attempt ce19b5 was interrupted on
its original handle44213 in0c3b02 with exit130 before producing
any result; nothing is inferred from it.

The displayed algebraic derivation and highest-degree argument
are the proof, not a finite-sample or symbolic-certification
claim. No saved checker was executed, imported or compiled,
no held source or canonical index was edited, and no unrestricted
cancellation, novelty, human-expert or proof-assistant
certification claim is made.
