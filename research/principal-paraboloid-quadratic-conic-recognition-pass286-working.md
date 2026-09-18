# Recognition of the quadratic whole-plane conic with nonzero B

The remaining selected conic with a degree-two whole-plane polynomial
and nonzero \(U^2\) coefficient in the actual branch271 is recognized.
The full scalar determinant first forces both coefficients of the
completed-square discriminant into the exact curve field. When
\(p'=0\), an actual monic shear lowers the last time degree. When
\(p'\ne0\), a coefficient derivative is zero and the full actual map
satisfies the polynomial-three-ring criterion proved in285.

This treats a degree-two whole equation, not the selected conic of a
degree-four whole equation. It does not change the scope of283.

## 1. Actual entry and the quadratic coefficients

Retain every actual hypothesis of
[271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and the nonlinear reduction
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
K=\operatorname{Frac}A,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
\operatorname{shift}(\partial_Z)=4,\qquad k_s=0,\quad n_s\ne0,\\
K=\mathbb C(y,z,w)=L(v),\qquad L[y,\sigma]=L[v],\qquad Nv=1,\\
F=\ker_L\partial_n,\qquad [F:\mathbb C(t)]<\infty,\qquad
[L:F(n)]<\infty,\qquad \ker_F\partial_t=\mathbb C,\\
H=hn+c,\quad T=pn+q,\qquad h\in\mathbb C^*,\quad c,k,p,q\in F.
\end{gathered}
\tag{1}
\]
The coefficient derivations commute and initially fix \(v\).
The original parameter \(n\) is transcendental over \(F\).
The actual scalar is \(-a^4h\in L^*\), where \(a=EX\ne0\).
No rationality of \(F\) or \(L\) is assumed.

Assume the selected irreducible relation has degree two and the
whole-plane polynomial \(Q\) also has degree two. The unit cofactor
of271 then gives \(Q-q_0=\eta G\), with \(\eta\in L^*\).
Using280's complete table, write
\[
\begin{aligned}
Q&=BU^2+(bP+C_0)U+D_2P^2+D_1P,\qquad B\ne0,\\
B&=hk''/2+p,\qquad r=p',\\
b&=pk''-c''+k'r+2\omega_n,\qquad C_0=-rn+k'\omega_n-q',\\
D_2&=k''\omega_n/2-q''/2,\qquad D_1=-\omega_t .
\end{aligned}
\tag{2}
\]
Here the absence of higher-degree terms gives
\[
k''''=0,\qquad hk'''/2+2p'=0,\qquad
c'''=pk'''+3k''p',\qquad
r\in\mathbb C,\quad B'=-r,\quad p''=0.
\tag{3}
\]
In particular (2)'s expression for \(D_2\) retains every term.
The coefficient \(B\) is not the ambient ring \(\mathcal B\).

The pure-square top of the selected conic gives
\[
b^2=4BD_2.
\tag{4}
\]
Set \(A_1=pk''-c''+k'r\in F\). Equation (4) reads
\((A_1+2\omega_n)^2-2Bk''\omega_n+2Bq''=0\).
This is a nonzero polynomial over \(F\) in \(\omega_n\), with
leading coefficient four. Thus \(\omega_n\) is algebraic over \(F\).
The derivation \(\partial_n\) kills \(F\), so separability forces
\(\omega_{nn}=0\). Its exact kernel in (1) then gives
\[
\omega=v_1n+v_0,\quad v_1,v_0\in F,\qquad
C_0=-rn+u_0,\quad u_0=k'v_1-q'.
\tag{5}
\]
This argument does not differentiate a possibly multiple displayed
root without justification; use its separable minimal polynomial
over \(F\).

Several exact ledger identities follow:
\[
\begin{aligned}
b'&=-rk''+2v_1',&
q''&=k''v_1-b^2/(2B),&
u_0'&=k'v_1'+b^2/(2B),\\
d&:=2bC_0-4BD_1,&
d_n&=-2br+4Bv_1'=2B(b'+rk'')-2br .
\end{aligned}
\tag{6}
\]
No constraint on the finite-field remainder \(q_0\) has been used.

## 2. The completed square and its correct polynomial-line parameter

The \(U\)-discriminant of \(Q-q_0\) is
\[
(bP+C_0)^2-4B(D_2P^2+D_1P-q_0)=dP+f,
\qquad f=C_0^2+4Bq_0\in L.
\tag{7}
\]
Define
\[
x=2By+b\sigma+C_0,\qquad x^2=d\sigma+f.
\tag{8}
\]
The \(U\)-degree of \(G\) is two, so
\(\deg_v\sigma=[L(v):L(\sigma)]=2\).
If \(d=0\), then the polynomial \(x\in L[v]\) has constant
square and is itself constant. Equation (8) would make \(y\)
affine in \(\sigma\), contrary to \(L[y,\sigma]=L[v]\) and
\(\deg_v\sigma=2\). Hence \(d\ne0\).
It follows that \(x\) has degree one in \(v\), so
\[
L[x]=L[v],\quad x_v\in L^*,\qquad
\sigma=\frac{x^2-f}{d},\qquad
y=\frac{x-b\sigma-C_0}{2B}.
\tag{9}
\]
Only this generic-line parameter is changed. It is not declared
to be an ambient coordinate.

Coefficient partials in the next calculation hold \(x\) fixed.
The exact \(X=0\) calibration becomes
\[
J_x:=\det\frac{\partial(y,z,w)}{\partial(t,n,x)}
       =-\frac{a^4h}{x_v}\in L^*.
\tag{10}
\]
The factor \(x_v\), and no additional field scalar, is the
Jacobian of the moving affine change from \(v\) to \(x\).

## 3. The full scalar forces d and f into F

Here is a direct coefficient computation retaining both coefficient
partials. Put \(\gamma=2\sigma+k'\) and \(B_1=2y+k''\sigma\).
The literal constant-coefficient exterior identity of271 is
\[
\begin{aligned}
D_U&=(B_1y_n-y_t)\sigma_x+(\sigma_t-B_1\sigma_n)y_x,\\
D_P&=(1+\gamma\sigma_n)y_x-\gamma y_n\sigma_x,\\
J_x&=xD_U+\left(\frac{bx}{2B}-\frac d{4B}\right)D_P.
\end{aligned}
\tag{11}
\]
Indeed \(Q_U(y,\sigma)=x\), and differentiating the quadratic
polynomial before evaluating gives
\(Q_P(y,\sigma)=bx/(2B)-d/(4B)\).
The second term is not \(-d/(2B)\).

Substitute (9) in (11), and use (3),(5),(6), including
\((C_0)_n=-r\) and
\((C_0)_t=k'(b'+rk'')/2+b^2/(2B)\).
The expression is a polynomial in \(x\) of degree at most five.
Its indicated coefficients are
\[
[x^4]J_x=\frac{5d_n}{4B^2d^2},\qquad
[x^2]J_x\bigm|_{d_n=0}=\frac{3f_n}{4B^2d}.
\tag{12}
\]
The second formula uses the consequence
\(b'=-rk''+br/B\) of \(d_n=0\).
Since (10) is independent of \(x\), exactness of the constants gives
\[
d,f\in F,\qquad
b'=-rk''+br/B,\qquad v_1'=br/(2B).
\tag{13}
\]
No assertion \(L=F(n)\) was needed for this calculation.

For transparency, after these two gates the entire scalar polynomial
is
\[
\begin{aligned}
J_x={}&-\frac{S}{2B^2d^2}x^3
 +\frac{-2Bd f'+2Sf+(2b+rk')d^2}{4B^2d^2}x
 -\frac d{8B^2},\\
S={}&Bd'-rd=(Bd)'.
\end{aligned}
\tag{14}
\]
Thus the remaining positive coefficients and the constant coefficient
give
\[
(Bd)'=0,\qquad 2Bf'=(2b+rk')d,\qquad
J_x=-\frac d{8B^2}\ne0.
\tag{15}
\]
Equations (11)--(14) give a finite algebraic reconstruction of the
scalar gates, not a numerical test or a replacement for field return.

We can now prove the exact field equality. All the literal projected
coefficients lie in \(F[n,x]\), by (5),(9) and the polynomial
potentials of280. Hence
\[
K=\mathbb C(y,z,w)\ \subset\ F(n,x)\ \subset\ L(x)=K.
\]
Since \(x\) is transcendental over \(L\), intersecting
\(L\) with \(F(n)(x)\) gives \(F(n)\). Therefore
\[
\boxed{K=F(n,x),\qquad L=F(n).}
\tag{16}
\]
This is the use of strong actual field return. A nonzero scalar
determinant alone would not establish (16).

## 4. The mode r zero has an actual degree-lowering shear

Suppose \(r=0\). Equations (3) imply \(k'''=c'''=0\), so \(k,c\)
are complex quadratics. Use the actual affine normalization272 to
make \(k=0\). Explicitly, for
\(k=\kappa t^2/2+\alpha t+\beta\) and \(d_0=\kappa/4\),
\[
X_*=X-d_0,\quad Y_*=Y+\alpha X_*/2,\quad
Z_*=Z-\beta X_*,\quad W_*=W.
\tag{17}
\]
The inverse adds \(d_0\), subtracts \(\alpha X_*/2\), and adds
\(\beta X_*\) in the respective slots. The actual selected partial,
fields, leaders and full initial kernel are preserved as proved in
[272](principal-paraboloid-high-derivative-line-normalization-pass272-working.md).
The new \(n\) differs from the old one by a complex quadratic
in \(t\), so \(h\) stays complex constant and the new \(c\) is
still complex quadratic.

Rebuild the coefficient derivatives and rename the chart.
The selected relation is still a conic, and \(\sigma\) remains
quadratic in its line parameter. The new \(Q\) has degree at most
three because \(k=0\). The unit-cofactor identity excludes degree
three for a selected conic. Thus it has degree two. Its \(U\)-degree
is two, so the new \(B=p\) is nonzero; absence of the cubic term
\(2p'UP^2\) gives \(p\in\mathbb C^*\).

Write \(c=c_2t^2/2+c_1t+c_0\), with complex coefficients.
The actual monic change
\[
\widetilde W=W-h(X^2Z-Y^2)-\frac{c_2}{2}Z-c_1Y-c_0X^2
\tag{18}
\]
has the inverse that adds the displayed polynomial, fixing
\(X,Y,Z\). Both compositions are the identity.
The full literal potentials, with \(k=0,p'=0\), give
\[
\widetilde W=
\left(\omega-\frac{c_2n}{2}-2p\sigma y+q'\sigma\right)
                    +(pn+q)X.
\tag{19}
\]
All its coefficients belong to \(K\), while \(pn+q\ne0\)
because \(p\in\mathbb C^*\) and \(n\) is transcendental over \(F\).
Thus \(\widetilde W\) has exact time degree one.
The actual frame \((X,\widetilde W,Y,Z)\) has exact degrees1122,
and the retained
[theorem257](full-exact1122-recognition-synthesis-pass257-working.md)
recognizes \(A\). No new initial-kernel hypothesis is imposed.

## 5. The mode r nonzero has a constant-slope actual pencil

Suppose \(r\in\mathbb C^*\). Since \(B'=-r\), a complex
translation of \(t\) makes \(B=-tr\). This translation is actual:
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W.
\tag{20}
\]
Its inverse is \(Y=Y_*+\tau X_*^2\) and
\(Z=Z_*+2\tau Y_*+\tau^2X_*^2\), with \(X,W\) unchanged.
The polynomial \(X^2Z-Y^2\) is preserved exactly.
The new \(t\) is \(t-\tau\), while \(y,\sigma,n\) are unchanged
and \(z\) changes to \(z-2\tau y\). The literal selected partial
is unchanged. These substitutions preserve all actual chart
hypotheses and the exact fields in (1),(16).

Rename the new parameter. Exact differentiation gives
\[
B=-tr,\qquad \kappa:=hk'+2tp\in\mathbb C,
\qquad \kappa'=hk''+2p+2tr=2B+2tr=0.
\tag{21}
\]
Solving (8) for \(n\), using \(C_0=-rn+u_0\), now gives
\[
n=-2ty+N_0(x),\quad
N_0(x)=\frac{b\sigma+u_0-x}{r}\in F[x],\qquad K=F(y,x).
\tag{22}
\]
The coefficient \(-2t\) is nonzero in \(F\), so (16) proves the
last equality and the algebraic independence of \(y,x\) over \(F\).

The complete original fixed-\(X\) coefficients are those of280:
\[
\begin{aligned}
z&=2ty+\sigma^2+k'\sigma+n,\\
\theta&=pn+q+c'\sigma-h\{(2\sigma+k')y+k''\sigma^2/2\},\\
w&=v_1n+v_0-p\{(2\sigma+k')y+k''\sigma^2/2\}\\
 &\quad-h\{y^2+k''\sigma y+k'''\sigma^3/6\}
              +c'y+c''\sigma^2/2+(rn+q')\sigma .
\end{aligned}
\tag{23}
\]
Substitution of (22) gives
\[
\begin{aligned}
z&=\sigma^2+(k'+b/r)\sigma+(u_0-x)/r\in F[x],\\
w&=-hy^2+\Lambda y+\Omega(x),\qquad
\Lambda=c'-pk'-2tv_1\in F,\quad \Omega\in F[x].
\end{aligned}
\tag{24}
\]
The coefficient of \(\sigma y\) is
\(-2p-hk''-2tr=0\). This is a full polynomial identity with no
restriction on the remaining lower functions.

There is a direct coefficient descent, independent of a pencil
theorem. From the definition of \(b\) and the last equality in (13),
\[
\Lambda'=-b-2tv_1'
        =-b\left(1+\frac{tr}{B}\right)=0.
\qquad\boxed{\Lambda\in\mathbb C.}
\tag{25}
\]
This uses exact prime constants in \(F\).

Make the actual complex triangular coordinate
\[
J=W+hY^2+\kappa XY,\qquad W=J-hY^2-\kappa XY.
\tag{26}
\]
Let \(M_0=F(X,x)\). Then
\(\operatorname{Frac}\mathcal B=M_0(Y)\), with \(Y\)
transcendental over \(M_0\).
The full \(Z\) row, not only its intercept, is
\[
Z=\sigma^2+(k'+b/r+2tX)\sigma+(u_0-x)/r+kX+t^2X^2.
\tag{27}
\]
Since \(\sigma=(x^2-f)/d\), this is a polynomial in \(x\)
over \(F(X)\) of degree exactly four, with leading coefficient
\(1/d^2\ne0\).

Likewise the entire actual last coordinate has the pencil form
\[
J=\Lambda Y+\Omega_X,\qquad \Omega_X\in F[X,x].
\tag{28}
\]
Here the subscript on \(\Omega_X\) denotes dependence on \(X\).
For a direct verification at fixed \(F,X,x\), (22),(23) give
\(n_y=-2t\), \(\theta_y=-\kappa-2h\sigma\), \(H_y=-2ht\).
Together with (24), these identities give \(J_y=\Lambda\).
All expressions are polynomial in \(y\), which proves (28)
including every power of the original \(X\).

## 6. Exact field intersection and the original-ring endpoint

The complete stable source
[285](principal-paraboloid-nonzero-p-derivative-quartic-recognition-pass285-working.md)
was read before reusing its Sections5--6 argument.
Here (25) already proves the coefficient is complex, so no
generic-pencil theorem or quartic ODE family is an input.
We spell out the actual-ring application.

The map
\(J_*=J-\Lambda Y=W+hY^2+\kappa XY-\Lambda Y\)
is a complex monic triangular change with the inverse that
subtracts \(hY^2+\kappa XY-\Lambda Y\). Thus
\[
S=\mathbb C[X,Z,J_*],\qquad \mathcal B=S[Y],\qquad
\operatorname{Frac}S\subset M_0.
\tag{29}
\]
Its fraction field satisfies
\(\operatorname{Frac}S(Y)=M_0(Y)\).
For any fields \(D\subset M_0\) and a variable \(Y\)
transcendental over \(M_0\), coefficient comparison gives
\(M_0\cap D(Y)=D\). Apply this with \(D=\operatorname{Frac}S\):
\[
\boxed{\operatorname{Frac}S=M_0.}
\tag{30}
\]

All four ratios
\((EX,EZ,EJ_*,EY)/a\) belong to \(\operatorname{Frac}S\):
the derivation \(E/a\) is the \(X\)-partial with \(K\) fixed,
and \(Z,J_*\in F[X,x]\), \(EY/a=\sigma+2tX\).
Choose a primitive vector \(b_i\in S^4\) representing these
ratios and write the actual component vector as \(g(b_i)\).
Since its first component is \(a\ne0\), one has
\(g\in\operatorname{Frac}(S)[Y]\).
All products \(g b_i\) belong to \(S[Y]\). For each prime of
the UFD \(S\), some \(b_i\) is not divisible by that prime.
Hence no coefficient of \(g\) has that prime in its denominator,
so \(g\in S[Y]\).
The actual slice equation \(Eu=1\), expressed in the coordinates
\((X,Z,J_*,Y)\), now makes \(g\) divide one. Thus
\(g\in\mathbb C^*\), and
\[
EX,EZ,EJ_*,EY\in S,\qquad E(S)\subset S.
\tag{31}
\]
Only at this point has the fraction-field direction been descended
to an actual polynomial-ring derivation.

The restriction \(E_0=E|_S\) is a nonzero LND and retains
\(EX\ne0,E^2X=0\). If \(\Delta\) is the gcd of its three
coordinate values, then \(\Delta\mid E_0\Delta\).
The LND degree argument forces \(E_0\Delta=0\), so
\(D=E_0/\Delta\) is an irreducible LND with the same kernel
and \(DX\ne0,D^2X=0\).
The precise three-variable preslice theorem,
[Dasgupta--Gupta, Theorem4.8](https://arxiv.org/html/1701.03635v1),
therefore supplies an invariant actual coordinate \(I\) of \(S\).
It remains a coordinate on adjoining \(Y\).
Since \(A\) is regular and affine from \(\mathcal B=A[u]\),
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{32}
\]
No coefficient-field parameter \(x,n,t\), or arbitrary element
of \(F\), has been declared an ambient coordinate.

## 7. Scope and verification

Both possible complex values of \(r=p'\), zero and nonzero,
are covered. This completes the degree-two whole equation with
nonzero \(B\). The \(B=0\) case belongs to the separate held283.
A selected conic in a degree-four whole equation is not treated
here, and no claim about every component of271 follows alone.

Fresh unsaved exact algebra rebuilt (11) from the exterior rows,
both sequential gates in (12), the entire remaining scalar (14),
and the full actual pencil (28). All these identities retained
symbolic coefficient derivatives. The exact integration,
field-return, field-intersection, content, slice and original-ring
arguments are separate from those finite algebra checks.

No saved checker was executed, imported, compiled or rerun.
No retained source, index or packet was edited. The recognition
conclusion retains the stated working dependencies, without
recursive formal certification, novelty clearance, or an
unrestricted cancellation claim.

