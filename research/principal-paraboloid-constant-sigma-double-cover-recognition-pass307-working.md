# Actual recognition of constant-sigma double covers

Working theorem: in the actual nonzero-coupling principal paraboloid
chart264, a degree-two projection with \(\sigma\in L\) has polynomial
kernel. Combined with303's nonconstant-\(\sigma\) result, this recognizes
the entire degree-two projection branch. It does not recognize the
remaining birational projection branch or arbitrary1222 frames.

The new step is polynomial entry over an invariant curve field in an
actual coordinate frame. The auxiliary locally nilpotent derivation
from303 is not assumed to have a slice. All coefficient-field parameter
changes below are distinguished from the displayed ambient automorphisms.

## 1. Actual input and the retained constant-sigma restrictions

Retain the full actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[295](principal-paraboloid-double-projection-line-reduction-pass295-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the fully read
[303](principal-paraboloid-double-cover-line-obstruction-pass303-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\qquad a=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
L[y,z,w]=L[y,\sigma,\theta]=O,\\
m=k_s\ne0,\qquad\sigma\in L,\qquad
[L(v):\operatorname{Frac}L[\sigma,\theta]]=2.
\end{gathered}
\tag{1}
\]
The selected literal \(Z\)-partial has exact intrinsic shift four.
The coefficient partials extend uniquely to \(L\), commute, and fix
\(v\); their joint constants are exactly \(\mathbb C\).
The literal coordinates and full scalar calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{aligned}
\tag{2}
\]
These hypotheses, including both returns in (1), are not replaced by
a formal parametrized surface or a nonzero determinant alone.

By303, Sections5 and6, there are complex constants \(c,d,\eta\), with
\((c,d)\ne(0,0)\), such that
\[
m=ct+d,\qquad n_{ss}=c^2/2,\qquad
\frac{c k_t/2-n_s}{m}=\eta.
\tag{3}
\]
Moreover there is \(x=v-\beta_0/2\), with \(Nx=1\), for which
\[
\theta=q_1x^2+q_0,\quad q_1\in L^*,\qquad
j:=y+c\theta/2=b_0+\tau x,\quad\tau\in L^*,\qquad O=L[j].
\tag{4}
\]
The last assertion is an exact one-variable ring equality, not an
ambient coordinate assertion.

## 2. The exact curve constant field

Put \(F=\ker_L\partial_s\). Then
\[
\mathbb C(t)\subset F\subset L\subset K,\qquad
[F:\mathbb C(t)]<\infty,
\quad F\text{ is relatively algebraically closed in }L,
\quad \partial_tF\subset F.
\tag{5}
\]
Here are the exact field arguments. If \(b\in F\), differentiate its
monic minimal polynomial over \(\mathbb C(t,s)\). Since \(b_s=0\),
the differentiated polynomial also vanishes at \(b\), but has smaller
degree. It is zero, so all coefficients belong to \(\mathbb C(t)\).
Thus every element of \(F\) is algebraic over \(\mathbb C(t)\).
Every finite subextension has degree at most
\([L:\mathbb C(t,s)]\), after adjoining the independent variable
\(s\). This uniform bound makes the full algebraic extension finite.
If an element of \(L\) is algebraic over \(F\), differentiation of
its separable minimal polynomial over \(F\) makes its \(s\)-derivative
zero. It therefore belongs to \(F\). Commutation of the two partials
proves the last inclusion in (5). The constants of \(\partial_t\) on
\(F\) are the joint constants \(\mathbb C\).

Integrating (3) in this exact field gives
\[
k=ms+f,\qquad
n=\frac{c^2}{4}s^2+\left(\frac{cf'}2-\eta m\right)s+n_0,
\qquad f,n_0\in F.
\tag{6}
\]
A prime means \(\partial_t\) on \(F\). No rational parametrization
of \(F\) has been assumed. The integration is literal: subtract
the displayed polynomial in \(s\), and the remainder is killed by
\(\partial_s\).

## 3. The centered surface and its nonzero transverse coefficient

Use formal independent variables \(U,P,V\), and define
\[
\begin{aligned}
\mathfrak F&=\frac{k_{tt}}2P^2+cPV+n_tP+n_sV,\\
\gamma&=2P+cs+f',\qquad D=\gamma/m,
\qquad \lambda=\mathfrak F_V/m,\qquad e=f''/2-c\gamma/m,\\
g&=(\ell-\gamma U-\mathfrak F)/m,\\
H&=U^2+\mathfrak F_PU+\mathfrak F_Vg+\mathcal H_3(k)
                 +\mathcal H_2(n)-\ell_tP-\ell_sV.
\end{aligned}
\tag{7}
\]
The homogeneous Taylor convention is
\(\mathcal H_r(b)=\sum_{i=0}^r
b_{t^{r-i}s^i}P^{r-i}V^i/((r-i)!i!)\).
The actual first and second potentials say
\(z=2ty+\sigma^2+k_t\sigma+m\theta+n\) and
\(w=g(y,\sigma,\theta)\). The next potential says
\(H(y,\sigma,\theta)=h_0\), with \(h_0\in L\).

Make only the formal substitution \(J=U+cV/2\). Direct expansion of
(7), with all lower derivatives retained, gives
\[
H=J^2+\mathcal A(P)J+\mathcal C V+\mathcal B(P),
\qquad
\mathcal A(P)=f''P+n_t+\eta\gamma-\frac{c\gamma^2}{2m},
\tag{8}
\]
where \(\mathcal B(P)=H(0,P,0)\) and the coefficient of \(V\) is
independent of \(P\):
\[
\mathcal C=c^2\left(\eta-\frac{f''}{4}\right)s
             -\eta^2m+\frac{c\eta f'}2-\frac{c n_0'}2-\ell_s,
\qquad \mathcal A_s=ce.
\tag{9}
\]
For example, in (8) the formal \(V^2,JV,PV\) coefficients all vanish.
The original formal \(V\)-derivative, before evaluation, is
\[
H_V=cJ+c\mathcal A(P)/2+\mathcal C.
\tag{10}
\]
It is not just \(\mathcal C\), since the substitution \(J=U+cV/2\)
must be differentiated too.

Crucially, \(\mathcal C\ne0\). Otherwise evaluating (8) at
\(P=\sigma\) would give a monic quadratic equation over \(L\)
for the nonconstant affine parameter \(j\) in (4). This is
impossible. Equivalently, the double-cover discriminant has a
nonzero linear coefficient in \(\theta\); it is not constant.

Retain the actual remainder identity from295 and296:
\[
\begin{gathered}
H-h_0=U^2+A_1U+A_0,\qquad
Q-q_0-e(H-h_0)=R(P,V)U+S(P,V),\\
R=A_{0,P}-DA_{0,V}+(\lambda-e)A_1,\\
G=P-\sigma,\qquad R\in(G^2),\quad
S\in\eta_0G+(G^2),\quad \eta_0\in L^* .
\end{gathered}
\tag{11}
\]
The square divisibility uses the unit ideal of the two-gradient
minors of the actual constant Jacobian. Differentiating (11) in
the formal \(V\)-variable gives
\(Q_V^{\rm ev}=e^{\rm ev}H_V^{\rm ev}\), because \(G_V=0\).
By296, \(Q_V=H_s-h_{0,s}\). Solve (8) for \(\theta\), using
\(\mathcal C\ne0\), and compare coefficients of \(j^2\) in this
last equality. The coefficient is \(-\mathcal C_s/\mathcal C\).
Since \(O=L[j]\), it vanishes. Consequently
\[
\ell=\frac{c^2}{2}\left(\eta-\frac{f''}{4}\right)s^2
                     +\ell_1s+\ell_0,
\qquad \ell_1,\ell_0\in F,
\qquad
\mathcal C=-\eta^2m+\frac{c\eta f'}2-\frac{c n_0'}2-\ell_1
\in F^*.
\tag{12}
\]
No derivative at a moving root has been substituted into a
formal gradient during this argument.

## 4. A moving-parameter remainder forces polynomial coefficient return

First suppose that the formal remainder \(R\) is not zero.
After (6),(12), formula (11) is independent of \(V\).
Regard \(\gamma\) as an independent formal variable and put
\[
\widehat R(\gamma)=
R\left((\gamma-cs-f')/2,V\right).
\]
The exact coefficient identity, with \(\gamma\) held fixed, is
\[
\boxed{\partial_s\widehat R=\mathcal C'-c\mathcal C/m.}
\tag{13}
\]
One expanded form of its right side is
\[
\frac{c\eta m f''-c m n_0''-2m\ell_1'
             -c^2\eta f'+c^2n_0'+2c\ell_1}{2m}.
\]
This follows directly from (7),(11),(12); it contains every derivative
of \(f,n_0,\ell_1\). In particular it is independent of \(\gamma\).
Thus \(\widehat R_\gamma\in F[\gamma]\).

Set \(\gamma_0=2\sigma+cs+f'\in L\). Equation (11) gives
\(\widehat R(\gamma_0)=\widehat R_\gamma(\gamma_0)=0\).
The second polynomial is nonzero: a nonzero polynomial with a double
root cannot be constant in characteristic zero. Hence \(\gamma_0\)
is algebraic over \(F\). Relative algebraic closedness in (5) gives
\[
\gamma_0\in F,\qquad
\sigma=-cs/2+\sigma_0,\quad \sigma_0\in F,
\qquad \mathcal C'-c\mathcal C/m=0.
\tag{14}
\]
The final identity comes by differentiating
\(\widehat R(\gamma_0)=0\) in \(s\), now knowing
\((\gamma_0)_s=0\). It also implies \(\mathcal C/m\in\mathbb C^*\),
although only its membership in \(F^*\) will be needed below.

The remaining constant coefficient of
\(Q_V^{\rm ev}=e^{\rm ev}H_V^{\rm ev}\), using
\(\mathcal A_s=ce\), gives the precise level derivative
\[
h_{0,s}=\mathcal B_s(\sigma)
       -e(\sigma)\bigl(c\mathcal A(\sigma)/2+\mathcal C\bigr).
\tag{15}
\]
Here \(\mathcal B_s\) means formal coefficient differentiation before
\(P=\sigma\). The term \(c\mathcal A/2\) must not be dropped.
All coefficients of \(\mathcal A,\mathcal B,e\) lie in \(F[s]\),
and (14) is polynomial in \(s\). Thus the right side of (15) lies
in \(F[s]\). Integrate this polynomial term by term in \(s\);
the residual constant is in \(F\). It follows that
\[
h_0\in F[s],\qquad
\theta=\frac{h_0-j^2-\mathcal A(\sigma)j-\mathcal B(\sigma)}{\mathcal C}
\in F[s,j],\qquad y=j-c\theta/2\in F[s,j].
\tag{16}
\]
The first two potentials now also give \(z,w\in F[s,j]\).
Only at this point may both field inclusions be used:
\[
K=\mathbb C(y,z,w)\subset F(s,j)\subset K,
\qquad K=F(s,j),\qquad L=F(s).
\tag{17}
\]
For the last equality, \(N\) kills \(F(s)\), and
\(Nj=\tau\ne0\), so the constants of \(N\) on \(F(s)(j)\)
are exactly \(F(s)\). This uses the actual three-generator field
return, not an assumed polynomial parametrization of \(L\).

## 5. Actual polynomial entry when c is nonzero

Continue in the branch \(R\ne0\), and assume \(c\ne0\).
Use the actual polynomial coordinates already exhibited in303:
\[
U_0=Z+\frac{2d}{c}Y,\qquad
V_0=W+\frac{2(X+\eta)}{c}Y,
\qquad \mathcal B=\mathbb C[X,Y,U_0,V_0].
\tag{18}
\]
The inverses are
\(Z=U_0-2dY/c\) and
\(W=V_0-2(X+\eta)Y/c\). Both compositions are polynomial over
\(\mathbb C\). The parameters introduced next are not claimed to
be actual polynomial coordinates.

Put
\[
\begin{aligned}
J_0&=j-\eta cs/2,\qquad D_0=(2\sigma_0+f')/m,\\
z_{00}&=\sigma_0^2+f'\sigma_0+n_0,\\
w_{00}&=(\ell_0-f''\sigma_0^2/2-n_0'\sigma_0)/m,\\
u_0(X)&=z_{00}+(2m\sigma_0/c+f)X+(t^2+2dt/c)X^2,\\
v_0(X)&=w_{00}+2\sigma_0(X+\eta)X/c
                         +2t(X+\eta)X^2/c.
\end{aligned}
\tag{19}
\]
All the coefficients in the last two polynomials are in \(F\).
Literal substitution in the full map (2), not just its intercepts,
gives
\[
\boxed{
U_0=\frac{2m}{c}J_0+u_0(X),\qquad
V_0=\left(\frac{2(X+\eta)}c-D_0\right)J_0
                         -\frac{\mathcal C}{m}s+v_0(X).}
\tag{20}
\]
For clarity, the intercept of \(w\) as an expression in \(j,\theta\)
is affine in \(s\), with slope
\((\ell_1+\eta c\sigma_0+c n_0'/2)/m\).
After the substitution \(j=J_0+\eta cs/2\), this gives exactly
the coefficient \(-\mathcal C/m\) in (20).

The two coefficient parameters can therefore be solved polynomially:
\[
\begin{aligned}
J_0&=\frac{c}{2m}(U_0-u_0(X)),\\
s&=-\frac{m}{\mathcal C}
\left[V_0-\left(\frac{2(X+\eta)}c-D_0\right)J_0-v_0(X)\right].
\end{aligned}
\tag{21}
\]
The solve determinant is \(-2\mathcal C/c\in F^*\).
There is no denominator depending on \(X,U_0,V_0\).
Equations (16),(21) and \(j=J_0+\eta cs/2\) now imply
\[
\boxed{Y=y+\sigma X+tX^2\in F[X,U_0,V_0].}
\tag{22}
\]
This is polynomial entry for an actual coordinate of the original
four-ring, not merely membership in a rational function field.

## 6. Actual polynomial entry when c is zero

If \(c=0\), then \(m=d\in\mathbb C^*\),
\(j=y\), \(\sigma=\sigma_0\in F\), and
\(\mathcal C=-\eta^2m-\ell_1\ne0\).
Use the different actual frame
\[
U_0=Y,\qquad V_0=W-\frac{X+\eta}{m}Z,
\qquad \mathcal B=\mathbb C[X,U_0,Z,V_0].
\tag{23}
\]
Its inverse is \(Y=U_0\),
\(W=V_0+(X+\eta)Z/m\), fixing \(X,Z\).
With \(D_0,z_{00},w_{00}\) defined by (19) at \(c=0\), put
\[
v_{00}(X)=w_{00}-\frac{X+\eta}{m}
\left[z_{00}+(2t\sigma_0+f)X+t^2X^2\right]\in F[X].
\]
The exact full-map identities and their polynomial solves are
\[
\begin{aligned}
U_0&=y+\sigma_0X+tX^2,\\
V_0&=-\left(D_0+\frac{2t(X+\eta)}m\right)y
                           -\frac{\mathcal C}{m}s+v_{00}(X),\\
y&=U_0-\sigma_0X-tX^2,\\
s&=-\frac{m}{\mathcal C}
\left[V_0+\left(D_0+\frac{2t(X+\eta)}m\right)y-v_{00}(X)\right].
\end{aligned}
\tag{24}
\]
Again every denominator is a nonzero element of \(F\).
Equation (16) gives \(\theta\in F[X,U_0,V_0]\), and the first
potential and (2) consequently give
\[
\boxed{Z\in F[X,U_0,V_0].}
\tag{25}
\]
This case does not specialize an inverse containing \(1/c\).

In both (22) and (25), \(F\subset\operatorname{Frac}A\) is finitely
generated of transcendence degree one by (5). The other three entries
are actual independent coordinates, as their explicitly displayed
ambient inverses prove. Thus the exact statement of the fully read
[266, Sections1--3](curve-field-polynomial-entry-criterion-pass266-working.md)
applies. It produces a triangular invariant coordinate by subtracting
a complex polynomial in those three entries from the remaining one.
Its regular-kernel endpoint gives
\[
\boxed{A\cong\mathbb C^{[3]}.}
\tag{26}
\]
The global slice supplies the affine regular kernel required there.
No slice or primitive-coordinate theorem for the auxiliary derivation
is invoked.

## 7. The zero-remainder branch uses an actual reframe

It remains to handle \(R=0\), which was not included in Section4.
Under (3),(6), the raw coefficient of \(P^3\) in (11) is
\(-4c^2/m^2\). Hence \(c=0\), \(m=d\in\mathbb C^*\), and
\(n_s=-\eta m\in\mathbb C\). The coefficient of \(P^2\)
then becomes \(f'''/2\), so exact constant-field integration gives
\[
k=ms+\kappa t^2/2+bt+d_0,\qquad
n=\nu s+f_0,\qquad
\kappa,b,d_0,\nu\in\mathbb C,\quad f_0\in F.
\tag{27}
\]
Now, and only now, make the actual295 reframe
\[
W_*=mW+\kappa Z/2+bY+d_0X^2,\qquad
W=(W_*-\kappa Z/2-bY-d_0X^2)/m.
\tag{28}
\]
For precision, its transformed data are
\[
\begin{aligned}
s_*&=k,\quad k_*=s_*,\quad m_*=1,\quad \sigma_*=\sigma,\\
\theta_*&=m\theta+(\kappa t+b)\sigma+\kappa k/2,\\
n_*&=n-\kappa k/2=\nu_*s_*+g(t),\quad
\nu_*=\nu/m-\kappa/2\in\mathbb C,\\
\ell_*&=\ell+\kappa n/2+\kappa\nu_*k/2.
\end{aligned}
\tag{29}
\]
The notation \(g(t)\) means an element killed by \(\partial_{s_*}\),
not an assumed rational function. As proved in295, Section5, the
weighted leading map preserves the full initial kernel and the exact
time degrees; \(t,s_*\) remain independent. Both intercept returns
are preserved by the actual inverse. The new literal \(Z\)-partial
is the old one minus \(\kappa/(2m)\) times the old \(W\)-partial;
the latter has shift at most three, so the shift-four leading \(N\)
and its field \(L\) are unchanged. The actual row determinant
factor \(m\) cancels the coefficient-basis factor \(m\), retaining
the calibration \(-a^4\). The projection ring is unchanged because
the displayed \(\theta_*\) change is affine invertible over \(L\).

Do not infer that the old zero remainder is unchanged. Rebuild (11)
in this actual frame. Its new expression is
\[
R_*=(g''+2(\ell_*)_{s_*})P-(\ell_*)_t.
\tag{30}
\]
It has degree at most one in \(P\), yet is divisible by
\((P-\sigma_*)^2\). Therefore it is zero. Commuting the coefficient
partials gives \(g'''=0\). Exact joint-constant integration gives,
after dropping stars,
\[
k=s,\qquad n=\nu s+\alpha t^2/2+\beta t+\delta,
\qquad \ell=-\alpha s/2+\ell_0,
\qquad \nu,\alpha,\beta,\delta,\ell_0\in\mathbb C.
\tag{31}
\]
This is precisely the entire coefficient family recognized or excluded
by303, Section4, without any nonconstant-\(\sigma\) assumption.
For completeness its actual invariant is
\[
I=(Y+\beta/2)^2+(\alpha/2-X^2)(Z-\delta)
                         +(X+\nu)(W-\ell_0).
\]
Writing \(\epsilon=\alpha/2-\nu^2\) and
\(V_1=W-\ell_0-(X-\nu)(Z-\delta)\), one has
\(I=(Y+\beta/2)^2+\epsilon(Z-\delta)+(X+\nu)V_1\).
If \(\epsilon\ne0\), this solves polynomially for \(Z-\delta\)
and is an invariant coordinate. If \(\epsilon=0\), the literal
potential substitution makes \(I\) a square in \(\operatorname{Frac}\mathcal B\);
normality makes it a polynomial square, impossible since its degree
in the actual coordinate \(V_1\) is one. Thus the possible actual
members of (31) have the same recognized endpoint (26).

## 8. Scope and verification boundary

The cases \(R\ne0\) and \(R=0\) exhaust the constant-\(\sigma\)
double-cover branch of (1). Together with the retained303 result for
\(\sigma\notin L\), this proves recognition for every degree-two
projection in the actual coupled chart264. No assertion about the
birational projection branch is included.

The polynomial-entry theorem266, including its curve-pencil and
regular-kernel inputs, was fully reread. Fresh unsaved symbolic
reconstruction checked the centered surface, the formal and moving
coefficient derivatives in (9),(13), both full-coordinate identities
(20),(24), all displayed polynomial solves, and the old-frame
zero-remainder normalization identities. These are supplementary
finite checks; the exact field, double-cover and actual-coordinate
arguments above are the proof gates.

No saved checker was executed, imported, compiled or rerun. No held
source was edited. No arbitrary1222 recognition, unrestricted
cancellation theorem, actual-existence, historical novelty or
proof-assistant certification claim is made.
