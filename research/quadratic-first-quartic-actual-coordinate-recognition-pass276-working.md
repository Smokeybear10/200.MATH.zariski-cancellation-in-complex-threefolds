# Actual coordinate recognition for the quadratic-first quartic component

The genuine quadratic-first quartic component left by263 is recognized.
The coefficient-field reductions273 and274 first give a quadratic
complex-coefficient potential. Strong actual field return forces it to
be linear in its second argument. The full literal coordinate expansion
then supplies complex polynomial corrections and an explicit polynomial
automorphism producing two invariant ambient coordinates.

The result is restricted to this selected quartic component. It does
not assert arbitrary entry, recognition of lower-degree components,
or recognition of every exact1123 frame.

## 1. Actual inputs and the coefficient-field normal form

Retain all actual hypotheses of
[270](quadratic-cubic-quadratic-first-field-boundary-pass270-working.md),
[273](quadratic-first-full-potential-discriminant-reduction-pass273-working.md)
and [274](quadratic-first-complex-potential-rigidity-pass274-working.md).
In particular
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\\
\operatorname{ht}I_{\rm initial}=2,\quad
\operatorname{shift}(\partial_Z)=3,\quad
K=\mathbb C(y,z,w)=L(v),\quad L[y,\psi]=L[v],\\
q'''\ne0,\quad m=k_\lambda\ne0,\quad
\deg G=4,\quad\deg_v y=2,\quad\deg_v\psi=4.
\end{gathered}
\tag{1}
\]
The initial ideal is the full weighted initial kernel, and \(G\)
is the selected irreducible projected relation. The auxiliary
polynomial \(\mathcal H\) was not presumed irreducible: the
evaluated-unit cofactor gives \(\mathcal H=\eta_0G\) in this
degree-four branch. The symbol \(\eta_0\) is not used below.

Use the exact fields and coefficients established in273:
\[
\begin{gathered}
[F:\mathbb C(t)]<\infty,\qquad L=F(\lambda),\qquad K=F(y,x),\\
\ker(\partial_t|_F)=\mathbb C,\quad
e=1/m,\quad h=m/N_2,\quad m,N_2\in F^*,\\
x^2=dy+\alpha\lambda+\beta,\qquad
d,\alpha\in F^*,\quad\beta\in F,\\
k=m\lambda+k_0,\qquad
n=N_2\lambda^2/2+n_1\lambda+n_0,
\quad k_0,n_1,n_0\in F.
\end{gathered}
\tag{2}
\]
Primes mean the unique extended \(t\)-derivative on \(F\).
The original coefficient partials fix \(t\) or \(\lambda\) as
appropriate. Both variables \(y,x\) are algebraically independent
over \(F\). No coefficient-field element has yet been declared
an ambient coordinate.

The literal actual chart, with \(a=EX\), is
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}&=-a^3\in L^*.
\end{aligned}
\tag{3}
\]
Here \(q,r\in F\), \(x\) is affine in \(v\), and the first
potential is
\[
z=m\theta+f(y),\qquad
f(U)=(q''-r''m)U^2/2+k_tU+n.
\tag{4}
\]

Put \(b=n_1e^2\), \(g_*=N_2e^2\), and define only in the field
\[
\zeta=g_*\lambda+b-e'y,\qquad \eta=hx.
\tag{5}
\]
The result274 supplies polynomials \(Q,\Pi\) and an element \(T\):
\[
\begin{gathered}
Q\in\mathbb C[U,V],\quad\deg Q\le2,\qquad
\Pi\in\mathbb C[U,V],\quad\deg\Pi\le3,\quad\Pi_V=Q,\\
z=\eta+Q(y,\zeta),\qquad
w=\Pi(y,\zeta)-\zeta z+T,\qquad
T\in F,\quad T'=\frac{ed}{2N_2}\ne0.
\end{gathered}
\tag{6}
\]
It also retains the complete coefficient identities used below.

## 2. Scalar calibration and a primitive polynomial relation

Equations (2),(5) express the square of \(\eta\) as
\[
\eta^2=A_1y+B_1\zeta+C_1,\qquad
B_1=\frac{h^2\alpha}{g_*}\in F^*,\quad
A_1=h^2d+B_1e',\quad C_1=h^2\beta-B_1b.
\tag{7}
\]
Here subscripts label coefficients, not derivatives.
For the next calculation hold \(y\) fixed. Since
\(y=(x^2-\alpha\lambda-\beta)/d\), the change
\((t,\lambda,x)\mapsto(t,y,x)\) has determinant \(-\alpha/d\).
The exact scalar from273 is
\(\det\partial(y,z,w)/\partial(t,\lambda,x)=-\alpha/(2N_2^2)\).
Taking account of the first row in the new ordering gives
\[
z_tw_x-z_xw_t=-\frac{d}{2N_2^2}\in F^*.
\tag{8}
\]
In particular this determinant is independent of \(x\).

From (7),
\(\zeta=(h^2x^2-A_1y-C_1)/B_1\).
Differentiate the two evaluated expressions in (6) at fixed \(y\).
The equality \(\Pi_V=Q\) gives the exact cancellation
\[
z_tw_x-z_xw_t
=-T'h-\frac{h^2x}{B_1}
 \{A_1'y+B_1'\zeta+C_1'+2T'Q_V(y,\zeta)\}.
\tag{9}
\]
For instance \(w_t=-\eta\zeta_t-\zeta z_t+T'\) and
\(w_x=-\eta\zeta_x-\zeta z_x\), which directly yield (9).
The bracket is even in \(x\). Its multiplied term is odd,
whereas (8) is constant in \(x\). Thus the bracket vanishes.
Because \(y,\zeta\) are algebraically independent over \(F\),
write \(Q_V=q_{11}U+2q_{02}V+q_{01}\) and compare coefficients:
\[
A_1'=-2q_{11}T',\qquad
B_1'=-4q_{02}T',\qquad C_1'=-2q_{01}T'.
\tag{10}
\]
Exact constants in \(F\) therefore give complex constants
\(A_0,B_0,C_0\) such that
\[
\eta^2=A_0y+B_0\zeta+C_0-2TQ_V(y,\zeta).
\tag{11}
\]

We now prove \(q_{02}=0\). Suppose instead that it is nonzero.
Eliminate \(T=w+\zeta z-\Pi(y,\zeta)\) from (11). In formal
variables \(U,Z_0,W_0,V\), the resulting polynomial is
\[
\mathcal R=(Z_0-Q(U,V))^2
 +2\{W_0+VZ_0-\Pi(U,V)\}Q_V(U,V)
 -(A_0U+B_0V+C_0).
\tag{12}
\]
As a polynomial in \(W_0\) over the UFD \(\mathbb C[U,Z_0,V]\),
its coefficient and constant term are relatively prime.
Indeed every common divisor would divide \(Q_V\), and reduction
modulo such a divisor leaves
\((Z_0-Q)^2-(A_0U+B_0V+C_0)\), whose \(Z_0^2\) coefficient is one.
Thus (12) is primitive and linear in \(W_0\), hence irreducible.
It remains irreducible over \(\mathbb C(U,Z_0,W_0)\) as a
polynomial in \(V\), by Gauss's lemma. Its leading coefficient is
\[
[V^4]\mathcal R=-q_{02}^2/3\ne0.
\tag{13}
\]
But \(K=\mathbb C(y,z,w)\), with \(y,z,w\) algebraically
independent over \(\mathbb C\), and \(\zeta\in K\) is a root
of this irreducible degree-four polynomial. That is impossible.
This uses the strong actual field return, not whole-line generation
over a larger coefficient field.

Consequently there are complex polynomials
\[
\begin{gathered}
Q_0(U)=q_2U^2+q_1U+q_0,\qquad L_0(U)=l_1U+l_0,\\
g_0(U)=g_3U^3+g_2U^2+g_1U+g_0^*,\\
Q(U,V)=Q_0(U)+L_0(U)V,\qquad
\Pi(U,V)=Q_0(U)V+L_0(U)V^2/2+g_0(U).
\end{gathered}
\tag{14}
\]
This includes \(Q_V=0\). No division by \(L_0\) will be used.
Equation (10) now makes \(B_1=B_0\in\mathbb C^*\), since
the coefficient in (7) is nonzero. The evaluated form becomes
\[
\begin{aligned}
z&=\eta+Q_0(y)+L_0(y)\zeta,\\
w&=T-\zeta\eta-L_0(y)\zeta^2/2+g_0(y),\\
\eta^2&=(A_0-2l_1T)y+B_0\zeta+C_0-2l_0T.
\end{aligned}
\tag{15}
\]

## 3. Exact integrations giving complex correction coefficients

All integrations in this section take place in \(F\), whose
prime constants are exactly \(\mathbb C\). Put
\[
j=\frac1{N_2e^3}\in F^*,\qquad b=n_1e^2.
\tag{16}
\]
The quadratic polynomial \(P_z\) of273 has coefficients
\[
[U^2]P_z=q''/2+e''/(2N_2e^3),\qquad
\partial_\lambda[U]P_z=3m'-mN_2'/N_2.
\]
Compare these with \(Q_0(U)+L_0(U)(g_*\lambda+b-e'U)\).
The second comparison first gives \(j'=l_1\), and the first gives
\(q''+je''+2l_1e'=2q_2\). The constant-in-\(\lambda\)
part of the linear coefficient gives the third identity below:
\[
\begin{gathered}
j=l_1t+l_2,\qquad
q+je=q_2t^2+c_1t+c_0,\\
k_0-jb+l_0e-q_1t=c_2,
\qquad l_2,c_1,c_0,c_2\in\mathbb C.
\end{gathered}
\tag{17}
\]
For the last comparison explicitly,
\([U]P_z|_{\lambda=0}=k_0'-jb'\), while the other side is
\(q_1+l_1b-l_0e'\). Their equality is exactly the derivative
of the third expression in (17).

Define three further elements of \(F\):
\[
R=r+je^2/2,\qquad
\Lambda=l_0e^2/2-jeb,\qquad
C=e(q_0-n_0)+jb^2/2.
\tag{18}
\]
To determine them one must retain the cubic integration constant
\(g_0(U)\) in (14). The full273 polynomial \(B_{\rm old}(U)\)
satisfies
\(B_{\rm old}=\Pi(U,g_*\lambda+b-e'U)+T\).
Its cubic coefficient, and its quadratic and linear coefficients
at \(\lambda=0\), give respectively
\[
\begin{aligned}
\frac{r'''-eq'''-3e'q''}{6}
 &=g_3-q_2e'+l_1(e')^2/2,\\
-e'k_0'-ek_0''/2+bq''/2
 &=g_2+q_2b-q_1e'+l_0(e')^2/2-l_1be',\\
-e'n_0+bk_0'-en_0'
 &=g_1+q_1b-q_0e'+l_1b^2/2-l_0be'.
\end{aligned}
\tag{19}
\]
These are literal coefficient comparisons, not choices of a
special coefficient curve. Substitution of (17) into the three
lines of (19) gives
\[
R'''=6g_3,\qquad \Lambda''=2g_2,\qquad C'=g_1.
\tag{20}
\]
For example the cubic comparison uses
\(q'''=-je'''-3l_1e''\) and
\(q''=2q_2-je''-2l_1e'\); its left side after moving the
nonconstant terms is \((r+je^2/2)'''/6\).
For the quadratic comparison use
\(k_0'=q_1+l_1b-l_0e'+jb'\) and
\(k_0''=2l_1b'-l_0e''+jb''\).
The linear comparison becomes directly
\(\{e(q_0-n_0)+jb^2/2\}'=g_1\).
Thus all constants in the following expressions are complex:
\[
\begin{aligned}
R&=g_3t^3+r_2t^2+r_1t+r_0,\\
\Lambda&=g_2t^2+s_1t+s_0,\qquad
C=g_1t+\kappa.
\end{aligned}
\tag{21}
\]

One more integration is needed for the quadratic form.
By (7),(15),
\(h^2d+B_0e'=A_0-2l_1T\).
The equality \(T'=ed/(2N_2)\) in (6) implies
\(h^2d=2jT'\). Since \(j'=l_1\), exact constants give
\[
2jT+B_0e-A_0t=c_3,\qquad c_3\in\mathbb C.
\tag{22}
\]

## 4. Full literal transport to actual complex polynomial shears

Define the following polynomials in the original ring:
\[
\begin{aligned}
\mathcal L&=l_1Y+l_0+l_2X\in\mathbb C[X,Y],\\
V&=Z-Q_0(Y)-c_1XY-c_2X-c_0X^2,\\
\overline W&=W-g_0(Y)-r_2XY^2-r_1X^2Y-r_0X^3
                       -s_1XY-s_0X^2-\kappa X.
\end{aligned}
\tag{23}
\]
These are actual complex-coefficient triangular changes with
\(X,Y\) retained. Their inverses add the displayed polynomials.
There are no coefficient-field denominators in (23).

For this calculation only put \(S=\zeta-eX\) in the function
field. We prove the full, not merely intercept, identities
\[
\boxed{V=\eta+\mathcal LS,\qquad
\overline W=T-S\eta-\mathcal LS^2/2.}
\tag{24}
\]
First note \(\mathcal L=L_0(y)+jX\), because \(Y=y+tX\).
Solving (5) gives
\(\lambda=je(\zeta-b+e'y)\).
Substitute this and (17) in the literal expression for \(Z\)
in (3). After subtracting (23), its coefficients of \(1,X,X^2\)
are
\[
\eta+L_0(y)\zeta,\qquad
j\zeta-eL_0(y),\qquad -je.
\tag{25}
\]
These are exactly the coefficients of
\(\eta+(L_0(y)+jX)(\zeta-eX)\).

For the last coordinate, use \(\theta=e(z-f(y))\) from (4).
Subtract \(T-S\eta-(L_0(y)+jX)S^2/2\) from the raw \(W\).
The complete difference is
\[
g_0(y)+\{R''y^2/2+\Lambda'y+C\}X
          +(R'y+\Lambda)X^2+RX^3.
\tag{26}
\]
Here is the parameter cancellation in its linear coefficient.
Before simplification this coefficient is
\(e(Q_0(y)-f(y))+j\zeta^2/2\).
Writing \(\zeta=g_*\lambda+b-e'y\), its \(\lambda^2\)
terms cancel because \(jg_*^2=eN_2\); its \(\lambda\)
terms cancel because \(jg_*=1/e\) and \(n_1=b/e^2\).
The remaining quadratic, linear and constant coefficients in
\(y\) are respectively \(R''/2,\Lambda',C\), by (17),(18).
The quadratic-in-\(X\) coefficient is
\[
r'y+\lambda-je\zeta+L_0(y)e^2/2
       =R'y+\Lambda,
\]
and the cubic one is \(r+je^2/2=R\). This proves (26).

Finally substitute (21) into (26). Taylor expansion of the
complex cubic \(g_0(y+tX)=g_0(Y)\) leaves exactly
\[
r_2XY^2+r_1X^2Y+r_0X^3+s_1XY+s_0X^2+\kappa X.
\]
This is the correction in (23), proving the second identity
in (24). No field-dependent coordinate change has been used.

## 5. A polynomial parameter and both actual inverse orders

Combine the last line of (15) with (22). Since
\(\mathcal L=L_0(y)+jX\) and \(Y=y+tX\), the result is
\[
\eta^2+2\mathcal LT
   =A_0Y+B_0S+C_0+c_3X.
\tag{27}
\]
The identities (24) also preserve the same quadratic form:
\(V^2+2\mathcal L\overline W=\eta^2+2\mathcal LT\).
Because \(B_0\in\mathbb C^*\), the following is an actual
polynomial, not just the old field parameter:
\[
S_*=\frac{V^2+2\mathcal L\overline W-A_0Y-c_3X-C_0}{B_0}
              \in B,\qquad S_*=S.
\tag{28}
\]
Define actual polynomials
\[
\boxed{I=V-\mathcal LS_*,\qquad
J=\overline W+S_*V-\mathcal LS_*^2/2.}
\tag{29}
\]
The letters \(I,J\) here denote new ambient coordinates,
not an initial ideal or a Jacobian.
Their explicit inverse over \(\mathbb C[X,Y]\) is
\[
\begin{aligned}
S^*&=\frac{I^2+2\mathcal LJ-A_0Y-c_3X-C_0}{B_0},\\
V&=I+\mathcal LS^*,\qquad
\overline W=J-S^*I-\mathcal L(S^*)^2/2.
\end{aligned}
\tag{30}
\]
Indeed (29) gives
\(I^2+2\mathcal LJ=V^2+2\mathcal L\overline W\), so
\(S^*=S_*\), and (30) immediately returns \(V,\overline W\).
Conversely (30) preserves the same form, so (28) returns
\(S_* = S^*\), and substitution into (29) returns \(I,J\).
This verifies both inverse orders. Division by \(\mathcal L\)
is never used, so its zeros and even \(\mathcal L=0\) cause
no exceptional case.

Composing with the triangular inverses of (23) gives an explicit
polynomial automorphism of the original four-ring, retaining
\(X,Y\). Equations (24),(28),(29) identify its new coordinates:
\[
\boxed{I=\eta=hx\in K,\qquad J=T\in F\subset K,
\qquad B=\mathbb C[X,Y,I,J].}
\tag{31}
\]
Since \(I,J\) are actual polynomials and \(E\) annihilates
\(K=\operatorname{Frac}A\), they both belong to \(A\).
Thus the passage from invariant field elements to ambient
coordinates has been proved by the actual inverse, not presumed.

## 6. Recognition and scope

The original derivation is nonzero and fixes the actual coordinate
\(J\). Its kernel \(A\) is regular: regularity descends from
the polynomial extension \(A[u]=B\).
The freshly checked primary
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
therefore applies to this actual coordinate frame and gives
\[
A=\mathbb C[J]^{[2]}\simeq\mathbb C^{[3]}.
\tag{32}
\]
Only this published endpoint is used; the polynomial corrections
and inverses above are explicit.

Together with267 this recognizes the two genuine degree-four
whole-plane shapes under the actual263 hypotheses. Lower-degree
selected components, smaller selected shifts, other initial-kernel
cases and arbitrary entry are separate questions. No conclusion
about all exact1123 frames or unrestricted cancellation is made.

## 7. Verification record

The complete saved273 and274 sources were independently read,
including the exact-field and scalar-calibration gates. The
primary theorem used in Section6 was freshly checked in full.
Unsaved symbolic calculations reconstructed (9), the coefficient
in (13), the preserved quadratic form and both intercept inverse
orders. A separate unrestricted literal substitution, retaining
the full \(X\)-dependent map and arbitrary \(e(t)\), verified all
four coefficients of both identities in (24). All residuals were
zero. An independent peer also rebuilt the full \(V\) and
\(\overline W\) transport before this source was finalized.

Those finite calculations do not replace the irreducibility,
constant-field integrations, actual inverse proof or recognition
theorem. No retained source was edited and no saved checker
was executed, imported or compiled. No historical novelty,
human expert certification or unrestricted result is claimed.
