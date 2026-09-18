# Full-potential reduction of the quadratic-first discriminant

In the genuine quadratic-first quartic component of263, the complete
potential coefficients strengthen270: the linear discriminant coefficient
is independent of \(\lambda\), and its constant coefficient is affine in
\(\lambda\) with nonzero slope. The formerly possible cubic denominator
in \(\lambda\) therefore disappears.

This is a conditional field and polynomial-presentation reduction.
It does not identify the line parameter as an actual ambient coordinate
and does not yet recognize this branch.

## 1. Actual hypotheses and retained conclusions

Retain all actual hypotheses of
[the complete quadratic-first reduction270](quadratic-cubic-quadratic-first-field-boundary-pass270-working.md),
whose full source was read before this argument. In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad K=\operatorname{Frac}A,\\
\deg_E(X,Y,Z,W)=(1,1,2,3),\quad
\operatorname{ht}I_{\rm initial}=2,\quad
\operatorname{shift}(\partial_Z)=3,\\
L=\operatorname{Frac}\ker_A N,\quad Nv=1,\quad K=L(v),\quad
K=\mathbb C(y,z,w),\quad L[y,\psi]=L[v].
\end{gathered}
\tag{1}
\]
Here \(I_{\rm initial}\) is the full initial kernel and \(N\) is the
intrinsic locally nilpotent derivation. Its notation is distinct from
the coefficient \(N_2\) below. The selected plane relation is a genuine
degree-four component with
\(\deg_v y=2,\deg_v\psi=4\), and \(q'''\ne0\).

Set \(F=\ker_L\partial_\lambda\). The retained exact-field argument gives
\([F:\mathbb C(t)]<\infty\), with \(\mathbb C\) as the constants of its
extended \(t\)-derivative. We use primes for that derivative on \(F\).
The established coefficient restrictions are
\[
\begin{gathered}
m,q,r,k_0,N_2,n_1,n_0\in F,\qquad mN_2\ne0,\\
k=m\lambda+k_0,\qquad
n=N_2\lambda^2/2+n_1\lambda+n_0,\qquad
\nu=n_\lambda=N_2\lambda+n_1,\\
\ell\in F[\lambda],\qquad\deg_\lambda\ell\le3.
\end{gathered}
\tag{2}
\]
The coefficient partials commute. In polynomial formulas they hold the
displayed formal variable \(U\) fixed.

For completeness, the actual coordinate expansions are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3.
\end{aligned}
\tag{3}
\]
Their fixed-\(X\) determinant in \((t,\lambda,v)\) is
\(-a^3\in L^*\), where \(a=EX\).

The exact discriminant from270 has the form
\[
\begin{gathered}
\mathscr D(U)=(MU^2+b_1U+b_0)^2-2N_2C_4(U)=dU+c,\\
M=m''/2-(m')^2/m\in F^*,\qquad
d\in F[\lambda]_{\le3}\setminus\{0\},\quad
c\in F[\lambda]_{\le4},\\
x=N_2\psi+My^2+b_1y+b_0,\qquad
x^2=dy+c,\qquad L[x]=L[v],\qquad L=F(\lambda).
\end{gathered}
\tag{4}
\]
In particular \(x_v\in L^*\). The exact field equality in (4) is a
conclusion of270, not a rationality assumption made here.

## 2. Reconstructing the full coefficient identities

Write \(C_4(U)=\sum_{j=0}^4c_jU^j\), and retain the literal
coefficient table from258:
\[
\begin{aligned}
b_1&=\nu_t-2\nu m'/m,&
b_0&=-\ell_\lambda-\nu^2/m,\\
c_4&=(q''''-mr''''-4q'''m'/m)/24,\\
c_3&=(mk_{ttt}-3k_{tt}m'-\nu q''')/(6m),\\
c_2&=n_{tt}/2-k_{tt}\nu/(2m)-n_tm'/m,\\
c_1&=\ell m'/m-\ell_t-\nu n_t/m.
\end{aligned}
\tag{5}
\]
The value of \(c_0\) will not enter the generic identities in this
section. In particular we do not infer any unproved differential
restriction from a specially chosen constant coefficient.

Use the first two literal potentials
\[
\begin{aligned}
f(U)&=(q''-r''m)U^2/2+k_tU+n,\\
P_{\rm old}(U)&=(q'''-mr'''-3r''m')U^3/6
 +(k_{tt}-r''\nu)U^2/2+n_tU,\\
z&=m\theta+f(y),\qquad
mw=\ell-(m'y+\nu)\theta-P_{\rm old}(y),\qquad
\theta=\psi+r''y^2/2.
\end{aligned}
\tag{6}
\]
Put \(e=1/m\), \(h=m/N_2\), and define
\[
\begin{aligned}
P_z(U)&=pU^2+u_1U+v_0,\\
p&=q''/2-hM,\qquad
u_1=k_t-hb_1,\qquad v_0=n-hb_0,\\
A(U)&=e'U-\nu e^2,\qquad
B_0(U)=e\ell-A(U)f(U)-eP_{\rm old}(U).
\end{aligned}
\tag{7}
\]
Then the actual intercepts satisfy
\[
z=hx+P_z(y),\qquad w=A(y)z+B_0(y).
\tag{8}
\]
All coefficients of \(P_z,A,B_0\) belong to \(F[\lambda]\).
Moreover \(p\in F\), \(u_1\) is affine in \(\lambda\), and \(v_0\)
has degree at most two in \(\lambda\).

The following identities use the entire raw ledger, not just polynomial
degree bounds:
\[
\boxed{
V_0:=(B_0)_\lambda-N_2e^2P_z=0,\qquad
A_t=-e^2(2MU+b_1).
}
\tag{9}
\]
For direct verification, the coefficients of \(B_0\), from highest to
lowest degree in \(U\), are
\[
\begin{aligned}
[U^3]B_0&=(r'''-eq'''-3e'q'')/6,\\
[U^2]B_0&=-e'k_t-ek_{tt}/2+\nu e^2q''/2,\\
[U]B_0&=-e'n+\nu e^2k_t-en_t,\\
[1]B_0&=e\ell+\nu e^2n.
\end{aligned}
\tag{10}
\]
Differentiating these four expressions in \(\lambda\), and using
(5),(7), gives respectively the four coefficients of \(N_2e^2P_z\).
Also \(e''=-2e^2M\) and
\((-\nu e^2)_t=-e^2b_1\), proving the second identity in (9).

There is a second complete identity:
\[
\boxed{
T_0:=A_tP_z+(B_0)_t
          =\frac{e}{2N_2}\mathscr D_U(U).
}
\tag{11}
\]
To check it without assuming the discriminant has already become linear,
write \(D_j=[U^j]\mathscr D\). The four coefficients of its left side are
\[
\begin{aligned}
[U^3]T_0&=\frac{2e}{N_2}(M^2-2N_2c_4)
                         =\frac{2e}{N_2}D_4,\\
[U^2]T_0&=\frac{3e}{N_2}(Mb_1-N_2c_3)
                         =\frac{3e}{2N_2}D_3,\\
[U]T_0&=\frac{e}{N_2}(b_1^2+2Mb_0-2N_2c_2)
                         =\frac{e}{N_2}D_2,\\
[1]T_0&=\frac{e}{2N_2}(2b_1b_0-2N_2c_1)
                         =\frac{e}{2N_2}D_1.
\end{aligned}
\tag{12}
\]
These follow by differentiating (10) in \(t\) and substituting (5).
For example the first uses
\([U^3](B_0)_t=-4ec_4-e''q''/2\).
Thus no coefficient of degree two or three in \(T_0\) has been discarded.
In the actual selected branch (4), (11) specializes to
\[
T_0=\frac{ed}{2N_2}.
\tag{13}
\]

## 3. Odd scalar coefficients remove parameter dependence from \(d\)

Because \(x\) is affine in \(v\), the actual scalar calibration is
\[
\mathfrak J=
\det\frac{\partial(y,z,w)}{\partial(t,\lambda,x)}
=-a^3/x_v\in L^*.
\tag{14}
\]
It is independent of \(x\). In (14) the coefficient partials hold \(x\)
fixed. To compute it one may temporarily hold \(y\) fixed, so that
\(x_t=(d_ty+c_t)/(2x)\) and
\(x_\lambda=(d_\lambda y+c_\lambda)/(2x)\).
This rational calculation gives the complete odd and even parts
after reduction by \(x^2=dy+c\):
\[
\begin{aligned}
\mathfrak J_{\rm odd}&=\frac{2x}{d}\mathcal O(y),\\
\mathcal O(U)&=
 -(P_z)_\lambda T_0
 +\frac{h^2e^2}{2}(2MU+b_1)(d_\lambda U+c_\lambda)\\
&\hspace{12mm}
 -\frac{eh}{2}(d_tU+c_t)-eh'(dU+c),\\
\mathfrak J_{\rm even}&=
 -\frac{2}{d}\{e(P_z)_t+hA_t(P_z)_\lambda\}(dy+c)
 -\frac{hT_0}{d}(d_\lambda y+c_\lambda).
\end{aligned}
\tag{15}
\]
For verification, start with
\(\mathfrak J=(2x/d)\{z_t(A_\lambda z+(B_0)_\lambda)
-z_\lambda(A_tz+(B_0)_t)\}\), substitute (8), and use
\(A_\lambda z+(B_0)_\lambda=-ex\) from (9).
No presumed vanishing of either parity part is used in this expansion.

Since \(\mathfrak J\) is independent of \(x\), its odd part vanishes.
The substitution \(U=(x^2-c)/d\) is injective on \(L[U]\), so
\(\mathcal O(U)=0\). By (7), \((P_z)_\lambda\) has degree at most
one in \(U\); by (13), \(T_0\) has degree zero. Hence
\[
0=[U^2]\mathcal O=\frac{M}{N_2^2}d_\lambda.
\qquad
\boxed{d\in F^*.}
\tag{16}
\]
Here nonvanishing uses \(M\ne0\) and the nonzero discriminant slope
already established in (4).

The linear coefficient, now with \(d_\lambda=0\), is
\[
0=-\frac{ed}{2N_2}(u_1)_\lambda
  -\frac{d'}{2N_2}-\frac{h'}{hN_2}d
  +\frac{M}{N_2^2}c_\lambda.
\tag{17}
\]
Since \((u_1)_\lambda=3m'-mN_2'/N_2\in F\), this proves
\[
c_\lambda=\frac{N_2}{2M}
 \left\{d'+\left(5m'/m-3N_2'/N_2\right)d\right\}\in F.
\tag{18}
\]
The exact kernel of \(\partial_\lambda\) in \(L\) is \(F\).
Subtracting the displayed primitive therefore gives
\(c=\alpha\lambda+\beta\), with \(\alpha,\beta\in F\).
This argument does not yet assert \(\alpha\ne0\).

## 4. The even scalar forces a nonzero affine slope

Differentiate the first identity in (9) in \(t\), and differentiate
the definition of \(T_0\) in \(\lambda\). The mixed partials commute;
the derivative of \(A_\lambda=-N_2e^2\) cancels the corresponding
coefficient derivative. Consequently
\[
(T_0)_\lambda=A_t(P_z)_\lambda+N_2e^2(P_z)_t.
\tag{19}
\]
But \(T_0=ed/(2N_2)\in F\) by (16), so its left side is zero.
Multiplying by \(h\), and using \(N_2e^2h=e\), gives
\(e(P_z)_t+hA_t(P_z)_\lambda=0\).
The complete even part in (15) therefore collapses to
\[
\boxed{
\mathfrak J=-\frac{hT_0}{d}c_\lambda
           =-\frac{\alpha}{2N_2^2}.
}
\tag{20}
\]
Its nonzero value in (14) proves \(\alpha\in F^*\).
In particular no case with zero affine slope has been lost.

## 5. Exact polynomial presentation and the boundary

The final conclusions are
\[
\boxed{
D_1=d\in F^*,\qquad
D_0=\alpha\lambda+\beta,\quad \alpha\in F^*,\ \beta\in F,\qquad
L=F(\lambda).
}
\tag{21}
\]
They imply the two exact polynomial identities
\[
y=\frac{x^2-\alpha\lambda-\beta}{d},\qquad
\lambda=\frac{x^2-dy-\beta}{\alpha},\qquad
F[\lambda,x]=F[y,x],\qquad K=F(y,x).
\tag{22}
\]
All the divisions in (22) are now by nonzero elements of \(F\),
not by a polynomial of positive \(\lambda\)-degree.
As a polynomial in \(\lambda\) over \(F(U)\),
\(D_0+D_1U=\alpha\lambda+\beta+dU\) has degree exactly one
and no repeated root. Thus the prospective quartic dependence on
\(\lambda\) has collapsed rather than acquired a repeated-root factor.

The retained potentials also give
\(y,z,w,\psi,\theta\in F[\lambda,x]=F[y,x]\).
These are polynomial presentations after coefficient-field extension.
They do not show \(x\in B\), do not make \(F\) an ambient coordinate
ring, and do not identify \(F[y,z,w]\) with \(F[y,x]\).
In particular neither actual coordinate recognition nor the hypothesis
of the one-parameter polynomial-entry criterion266 follows merely
by naming this polynomial pair.

## 6. Verification and scope

The complete270 source and the relevant full-potential formulas of258
and263 were read. The generic identities (9),(11) were independently
reconstructed before specializing the discriminant. An unsaved
arbitrary-function calculation checked their complete coefficient
expressions and the exact quadratic odd coefficient; every residual
was zero. The scalar parity and mixed-partial arguments are written
above, not inferred from a grid of coefficient values.

The result applies only under the actual genuine quadratic-first quartic
hypotheses (1)--(4). It does not handle lower-degree selected components,
arbitrary chart entry, or unrestricted cancellation. No retained source
or checker was executed, imported, compiled, or edited. No claim of
novelty or independent human certification is made.
