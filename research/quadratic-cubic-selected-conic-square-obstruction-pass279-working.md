# A square obstruction for the selected conic in the quadratic-cubic chart

The nonconstant-first selected conic is impossible when the quartic top
of the actual whole-plane equation263 is nonzero. The proof uses the
conic's constant discriminant, its calibrated scalar determinant, and
strong actual field return. Explicit complex polynomial corrections
then give a square whose degree in an actual coordinate is one.

This is a conditional exclusion of this selected component. It does
not assert arbitrary entry or recognition of every exact1123 frame.
In particular the affine discriminant parameter of270 is not used:
the completed-square expression here is constant on the generic line.

## 1. Actual hypotheses and the conic-specific coefficient entry

Retain the actual chart and evaluated-unit cofactor proved in
[258](two-affine-quadratic-cubic-frontier-pass258-working.md) and
[263](two-affine-quadratic-cubic-whole-plane-cofactor-pass263-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad K=\operatorname{Frac}A,\\
\deg_E(X,Y,Z,W)=(1,1,2,3),\quad
\operatorname{ht}I_{\rm initial}=2,\quad
\operatorname{shift}(\partial_Z)=3,\\
K=L(v)=\mathbb C(y,z,w),\quad L[y,\psi]=L[v],\quad
[L:\mathbb C(t,\lambda)]<\infty,\quad Nv=1.
\end{gathered}
\tag{1}
\]
Here the initial ideal is the full initial kernel, the selected partial
is literal, and \(L=\operatorname{Frac}\ker_A N\). The commuting
coefficient partials initially fix \(v\). The strong equality
\(K=\mathbb C(y,z,w)\), supplied by the actual chart, is part of (1).
It is not inferred merely from whole-line generation over \(L\).

Assume \(m=k_\lambda\ne0\), \(q'''\ne0\), and that the selected
irreducible relation \(G\) has degree two with nonconstant \(y\).
The reduction263 gives \(m_\lambda=0\). Put
\(F=\ker_L\partial_\lambda\). Then \(F\) is finite over
\(\mathbb C(t)\), its extended \(t\)-derivative has constants exactly
\(\mathbb C\), and
\[
q,r,m,k_0\in F,\qquad k=m\lambda+k_0,\qquad
\mathcal H_4=a_4U^4\ne0,\qquad
a_4=\frac{q''''-mr''''-4q'''m'/m}{24}\in F^*.
\tag{2}
\]
Primes denote that extended derivative on \(F\); coefficient
subscripts denote partials holding the displayed formal variables fixed.
Exact integration below takes place in the finite field \(L\), not in
an assumed rational field. For example a derivative-zero remainder
belongs to \(F\) by its definition.

The actual expansions and calibration are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,\\
\psi&=\theta-r''y^2/2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}=-a^3\in L^*,
\quad a=EX.
\end{aligned}
\tag{3}
\]
The unit-cofactor identity is \(\mathcal H=\eta G+G^2R_0\), with
\(\eta\in L^*\). Degree four forces \(R_0\in L^*\).
The pure leading form of a birational polynomial plane parametrization
and (2) give \(\deg_v y=1\), \(\deg_v\psi=2\).
Thus normalize \(G=V-P_2(U)\), with \(\deg P_2=2\). Comparing
the coefficient of \(V^2\) in the literal equation gives
\[
\begin{gathered}
\mathcal H=\frac{N_2}{2}(V-P_2(U))^2+\eta(V-P_2(U)),
\qquad N_2=n_{\lambda\lambda}\ne0,\\
\mathcal H=\frac{N_2}{2}V^2+\mathcal B(U)V+C_4(U),\qquad
\mathcal B(U)=MU^2+b_1U+b_0,\\
M=m''/2-(m')^2/m,\qquad
M^2=2N_2a_4,\qquad
\Delta(U):=\mathcal B(U)^2-2N_2C_4(U)=\eta^2.
\end{gathered}
\tag{4}
\]
In particular \(M,N_2\in F^*\), before any integration of \(n\).
The first two comparisons are \(M=-N_2[U^2]P_2\) and
\(a_4=N_2([U^2]P_2)^2/2\).

Write \(\nu=n_\lambda\) and \(C_4=\sum c_jU^j\). The literal ledger is
\[
\begin{aligned}
n&=N_2\lambda^2/2+n_1\lambda+n_0,\quad n_1,n_0\in F,\\
b_1&=\nu_t-2\nu m'/m,& b_0&=-\ell_\lambda-\nu^2/m,\\
c_4&=a_4,&
c_3&=(mk_{ttt}-3k_{tt}m'-\nu q''')/(6m),\\
c_2&=n_{tt}/2-k_{tt}\nu/(2m)-n_tm'/m,\\
c_1&=\ell m'/m-\ell_t-\nu n_t/m.
\end{aligned}
\tag{5}
\]
The first line follows by two integrations with exact kernel \(F\).
The vanishing \(U^2\) coefficient of \(\Delta\) gives
\[
\ell_\lambda=
\frac{b_1^2-2M\nu^2/m-2N_2c_2}{2M}\in F[\lambda]_{\le2},
\qquad \ell\in F[\lambda]_{\le3}.
\tag{6}
\]
The last assertion includes its integration constant in \(F\).
No equality \(L=F(\lambda)\) has been assumed or needed.

## 2. Complete potential identities and the constant discriminant scalar

Define the element \(\chi\), which is constant on \(v\), by
\[
\chi=N_2\psi+\mathcal B(y)=\eta\in L^*,\qquad
e=1/m,\quad h=m/N_2.
\tag{7}
\]
In particular \(\chi\) is not the affine line parameter of270.
The two literal potentials are
\[
\begin{aligned}
f(U)&=(q''-r''m)U^2/2+k_tU+n,\\
P_{\rm old}(U)&=(q'''-mr'''-3r''m')U^3/6
 +(k_{tt}-r''\nu)U^2/2+n_tU,\\
z&=m\theta+f(y),\qquad
mw=\ell-(m'y+\nu)\theta-P_{\rm old}(y).
\end{aligned}
\tag{8}
\]
Consequently, as polynomials in a formal \(U\), put
\[
\begin{aligned}
P_z(U)&=(q''/2-hM)U^2+(k_t-hb_1)U+n-hb_0,\\
A_w(U)&=e'U-\nu e^2,\\
B_w(U)&=e\ell-A_w(U)f(U)-eP_{\rm old}(U),\\
z&=h\chi+P_z(y),\qquad w=A_w(y)z+B_w(y).
\end{aligned}
\tag{9}
\]
Here \(P_z\in F[U,\lambda]_{\le2}\) and
\(B_w\in F[U,\lambda]_{\le3}\), with total degree understood.

The generic identities reconstructed in273 also follow directly from
(5),(8),(9), without that source's quartic-component specialization:
\[
\begin{gathered}
(B_w)_\lambda=N_2e^2P_z,\qquad
(A_w)_t=-e^2(2MU+b_1),\\
T_0:=(A_w)_tP_z+(B_w)_t=rac{e}{2N_2}\Delta_U=0,\\
e(P_z)_t+h(A_w)_t(P_z)_\lambda=0.
\end{gathered}
\tag{10}
\]
For completeness, the four coefficients of \(B_w\), in descending
degree, are
\[
\begin{aligned}
[U^3]B_w&=(r'''-eq'''-3e'q'')/6,\\
[U^2]B_w&=-e'k_t-ek_{tt}/2+\nu e^2q''/2,\\
[U]B_w&=-e'n+\nu e^2k_t-en_t,\\
[1]B_w&=e\ell+\nu e^2n.
\end{aligned}
\tag{11}
\]
Their \(\lambda\)-derivatives give the first equality in (10).
Also \(e''=-2e^2M\) and \((\nu e^2)_t=e^2b_1\).
If \(D_j=[U^j]\Delta\), their \(t\)-derivatives give the four
coefficients of \(T_0\) as
\(2eD_4/N_2,3eD_3/(2N_2),eD_2/N_2,eD_1/(2N_2)\).
They all vanish by (4). Finally differentiate \(T_0=0\) in
\(\lambda\), use the first equality in (10), and multiply by \(h\)
to obtain the last equality. Thus all mixed terms are retained.

Since \(y_v\in L^*\), use \(y\) itself as line parameter, with
the coefficient partials now holding it fixed. Chain rule in (3) gives
\[
J=z_tw_\lambda-z_\lambda w_t=-a^3/y_v\in L^*.
\tag{12}
\]
The moving affine change from \(v\) contributes exactly \(y_v\)
to the determinant; its other derivatives do not change that factor.
The identities (9),(10) give
\[
\begin{aligned}
w_\lambda&=A_wz_\lambda-e\chi,\qquad
w_t=A_wz_t+h(A_w)_t\chi,\\
J&=-\chi\{eh'\chi+eh\chi_t+h^2(A_w)_t\chi_\lambda\}.
\end{aligned}
\tag{13}
\]
In obtaining the second line, the last identity in (10) cancels
exactly the two terms involving derivatives of \(P_z\).
The coefficient of \(y\) in (13) is
\(2Me^2h^2\chi\chi_\lambda\). Since (12) is independent of \(y\),
\[
\chi\in F^*,\qquad s:=h\chi\in F^*,\qquad
J=-e\chi s'\ne0,
\quad\text{hence }s'\ne0.
\tag{14}
\]

## 3. Exact complex potential and strong field return

Change only the formal coefficient variable by
\[
\zeta=N_2e^2\lambda+b-e'U,\qquad b=n_1e^2.
\tag{15}
\]
This has a polynomial inverse over \(F\), since \(N_2e^2\in F^*\).
The derivation holding \(U,\zeta\) fixed is
\(D=\partial_t-(2MU+b_1)\partial_\lambda/N_2\).
The last identity in (10) gives \(DP_z=0\). Its exact constants,
coefficient by coefficient in \(F[U,\zeta]\), are complex. Also
\(DB_w=T_0=0\), while \((B_w)_\zeta=P_z\). Therefore
\[
\begin{gathered}
Q\in\mathbb C[U,\zeta]_{\le2},\quad
\Pi\in\mathbb C[U,\zeta]_{\le3},\quad\Pi_\zeta=Q,\\
z=s+Q(y,\zeta),\qquad w=\Pi(y,\zeta)-\zeta z,
\quad\zeta=N_2e^2\lambda+b-e'y\in K.
\end{gathered}
\tag{16}
\]
There is no nonconstant integration term \(T(t)\) here: \(T_0=0\),
and any complex constant has already been included in \(\Pi\).

Consider the formal polynomial
\(W_0-\Pi(U,V)+VZ_0\). It is irreducible in
\(\mathbb C[U,Z_0,W_0,V]\), being monic linear in \(W_0\).
If \(\deg_V\Pi\ge2\), it remains primitive and irreducible as a
polynomial of that degree over \(\mathbb C(U,Z_0,W_0)\).
But (1) identifies this coefficient field with \(K\) under
\((U,Z_0,W_0)=(y,z,w)\), and \(\zeta\in K\) would be a root.
This is impossible. Thus
\[
\begin{gathered}
Q(U,V)=Q_0(U)=q_2U^2+q_1U+q_0,\\
\Pi(U,V)=Q_0(U)V+g(U),\quad
g(U)=g_3U^3+g_2U^2+g_1U+g_0,\\
z=s+Q_0(y),\qquad w=g(y)-s\zeta,
\qquad q_i,g_i\in\mathbb C.
\end{gathered}
\tag{17}
\]
The degree-one case includes \(Q_0=0\). This argument uses actual
field return, not an assertion that \(\zeta\) is an ambient coordinate.

## 4. Complex coefficients of the actual polynomial corrections

Put \(j=1/(N_2e^3)\in F^*\). The linear coefficient of \(P_z\)
has \(\lambda\)-derivative
\(3m'-mN_2'/N_2=j'/(je)\). Its vanishing by (17) gives
\(j=j_0\in\mathbb C^*\). Next compare the quadratic coefficient,
and the linear coefficient at \(\lambda=0\), of \(P_z=Q_0\):
\[
\begin{gathered}
q''+j_0e''=2q_2,\qquad k_0'-j_0b'=q_1,\\
q+j_0e=q_2t^2+c_1t+c_0,\qquad
k_0-j_0b-q_1t=c_2,\quad c_0,c_1,c_2\in\mathbb C.
\end{gathered}
\tag{18}
\]
These integrations are in \(F\), with exact constants \(\mathbb C\).
Define
\[
R=r+j_0e^2/2,\qquad
\Lambda=-j_0eb,\qquad C=e(q_0-n_0)+j_0b^2/2.
\tag{19}
\]
Compare (11) with
\(B_w=Q_0(U)(N_2e^2\lambda+b-e'U)+g(U)\).
The cubic coefficient, and the quadratic and linear coefficients at
\(\lambda=0\), respectively give
\[
\begin{aligned}
(r'''-eq'''-3e'q'')/6&=g_3-q_2e',\\
-e'k_0'-ek_0''/2+bq''/2&=g_2+q_2b-q_1e',\\
-e'n_0+bk_0'-en_0'&=g_1+q_1b-q_0e'.
\end{aligned}
\tag{20}
\]
Substituting (18) proves \(R'''=6g_3\), \(\Lambda''=2g_2\),
and \(C'=g_1\). For the first use
\(q'''=-j_0e'''\), \(q''=2q_2-j_0e''\); for the second use
\(k_0'=q_1+j_0b'\), \(k_0''=j_0b''\).
Thus
\[
R=g_3t^3+r_2t^2+r_1t+r_0,\quad
\Lambda=g_2t^2+s_1t+s_0,\quad C=g_1t+\kappa,
\tag{21}
\]
where every new constant is complex. No normalization of an arbitrary
function in \(F\) has been used.

## 5. Full actual transport and the square contradiction

Define actual complex polynomial coordinates retaining \(X,Y\):
\[
\begin{aligned}
V&=Z-Q_0(Y)-c_1XY-c_2X-c_0X^2,\\
\overline W&=W-g(Y)-r_2XY^2-r_1X^2Y-r_0X^3
                         -s_1XY-s_0X^2-\kappa X.
\end{aligned}
\tag{22}
\]
The inverse adds the displayed polynomials in \(X,Y\) to \(V\)
and \(\overline W\), respectively. Both substitution orders are
therefore the identity, and \(B=\mathbb C[X,Y,V,\overline W]\).

Only for a field calculation put \(S=\zeta-eX\). The full actual
identities, including all powers of \(X\), are
\[
V=s+j_0XS,\qquad
\overline W=-sS-j_0XS^2/2.
\tag{23}
\]
To verify them solve (15) for
\(\lambda=j_0e(\zeta-b+e'y)\). Substituting (18) in the raw
\(Z\) of (3) gives the coefficients of \(V\) as
\(s,j_0\zeta,-j_0e\), in degrees zero, one, and two in \(X\).
For the last coordinate, use \(\theta=e(z-f(y))\) from (8).
The complete difference between raw \(W\) and the proposed second
expression in (23) is
\[
g(y)+\{R''y^2/2+\Lambda'y+C\}X+(R'y+\Lambda)X^2+RX^3.
\tag{24}
\]
Indeed its linear coefficient is initially
\(e(Q_0(y)-f(y))+j_0\zeta^2/2\).
Its \(\lambda^2\) terms cancel because
\(j_0(N_2e^2)^2=eN_2\), and its \(\lambda\) terms cancel because
\(j_0N_2e^2=1/e\) and \(n_1=b/e^2\).
The remaining coefficients are \(R''/2,\Lambda',C\).
The quadratic coefficient is
\(r'y+\lambda-j_0e\zeta=R'y+\Lambda\), and the cubic one is \(R\).
Finally (21) and Taylor expansion of \(g(y+tX)=g(Y)\) turn (24)
into exactly the correction in (22). This proves (23) in the original
coordinate field, rather than only on the intercept slice.

Taking the preserved quadratic expression in (23) gives
\[
V^2+2j_0X\overline W=s^2\in B.
\tag{25}
\]
The element \(s\) belongs to \(F\subset K\subset\operatorname{Frac}B\)
and satisfies a monic polynomial with coefficients in \(B\).
Since the polynomial ring \(B\) is integrally closed, \(s\in B\).
But in the actual polynomial coordinates (22), the left side of (25)
has degree exactly one in \(\overline W\), because
\(2j_0X\ne0\). A nonzero square in
\(\mathbb C[X,Y,V][\overline W]\) has even degree in \(\overline W\).
This contradiction excludes the supplied selected conic.

## 6. Scope and verification

The conclusion is nonrealizability of the nonconstant-first conic
under (1),(2), not a generic plane-curve or field-rationality assertion.
The actual normality step is used only after explicit complex
triangular changes with explicit inverses. Neither \(\chi\), \(\zeta\),
nor \(S\) was promoted to an ambient coordinate.

The proof separately rebuilds the conic-specific coefficient entry and
the scalar determinant. Only generic polynomial identities from273 and
the literal transport calculation of276 are reused, with all required
specializations displayed above. The quartic branch's affine parameter,
nonzero discriminant slope, and equality \(L=F(\lambda)\) are not inputs.
An independent peer reconstructed this argument at formula level before
the source was saved; a complete saved-source review is separate.
No earlier source was modified and no saved checker was executed,
imported, or compiled. No historical novelty or unrestricted result is
claimed.
