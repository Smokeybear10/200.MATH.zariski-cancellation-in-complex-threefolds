# A sextic reduction for the t-independent rank-two initial kernel

Status: bounded working necessary restrictions, not recognition of the
remaining rank-two frame. The actual chart with \(q=1/\rho\) has a
nonzero sextic eliminant whose highest homogeneous part is a pure sixth
power. Its nonconstant projected degrees satisfy
\(\deg_v y>\deg_v\vartheta\), unlike the affine pair recognized in211.
The zero and constant centers are recognized by retained results.
A new asymmetric cone argument excludes the repeated-quadratic center.
The nonconstant squarefree centers remain open here.

## 1. Exact actual hypotheses and a nonunit speed

Assume a supplied actual frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\\
a=EX\ne0,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(as,bs,e_0s^2,h_0s^2).
\end{gathered}
\tag{1}
\]
Here \(s\) is an independent indeterminate, the four capital letters
are polynomial coordinates, and the displayed ideal is the full
initial kernel, not one vanishing relation.

Use the original pivot \(\partial_Z\). The freshly read
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
and [classification206](weight-four-t-independent-leading-kernel-classification-pass206-working.md)
give
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=1/\rho,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+\rho^{-1}X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad J_0=-a^3\in L^*.
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their commuting
partials extend uniquely to the finite separable field \(L\), then
fix \(v\). No rationality of \(L\) is assumed.

The speed \(a\) cannot be a unit of \(B\), or of \(A\). Indeed a unit
of \(B\) is complex, while the initial relation gives
\(e_0h_0=a^4\). If \(a\in\mathbb C^*\), both \(e_0,h_0\) are complex
units. Then
\(\mathsf Z-(e_0/a^2)\mathsf X^2\) is a nonzero weight-two initial
relation, contradicting (1). This is a constraint on this supplied
coordinate \(X\), not on every possible degree-one coordinate.

The branches \(R=0\) and \(\vartheta\in L\) are already recognized by
[zero-return205](weight-four-t-independent-zero-r-recognition-pass205-working.md)
and [constant-second210](weight-four-constant-second-projection-recognition-pass210-working.md).
The remaining arguments assume
\[
R\ne0,\qquad \vartheta\notin L.
\tag{3}
\]
Neither assumption makes \(R\) a unit in the line ring.

## 2. All specialized potentials and the eliminant

For independent formal variables \(U,V\), let
\(H_j(c)=\sum_{i=0}^j c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
Universal184 supplies \(k,n,\ell,m\in L\). Define
\[
\begin{aligned}
f&=\rho^{-3}V^2+k_tU+k_\rho V+n,
&\mathcal R&=2\rho^{-3}V+k_\rho,\\
S&=-\rho^{-4}V^3+\tfrac12 k_{tt}U^2+k_{t\rho}UV
       +\tfrac12 k_{\rho\rho}V^2+n_tU+n_\rho V,
&T&=\ell-S,\\
c&=-3\rho^{-4}V^2+k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Q&=\rho^{-5}V^4+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m .
\end{aligned}
\tag{4}
\]
All coefficient derivatives keep \(U,V\) fixed. In particular
\(c=f_\rho=S_V\). The exact projected identities are
\[
\begin{gathered}
\sigma=-\rho^{-2}\vartheta+k,\qquad
z=-\rho^{-2}w+f(y,\vartheta),\\
Rw=T(y,\vartheta),\qquad
\rho^{-3}w^2+c(y,\vartheta)w+Q(y,\vartheta)=0,\qquad
R=\mathcal R(y,\vartheta).
\end{gathered}
\tag{5}
\]
Eliminating \(w\) without division in the line ring gives
\[
\mathcal H=\rho^{-3}T^2+\mathcal R cT+\mathcal R^2Q,\qquad
\mathcal H(y,\vartheta)=0.
\tag{6}
\]
Every lower term of this polynomial is specified in (4).

The top homogeneous contributions to (6) have coefficients
\((1,-6,4)\rho^{-11}V^6\), respectively. Consequently
\[
\begin{gathered}
\deg\mathcal H=6,\qquad \mathcal H_6=-\rho^{-11}V^6,\qquad
\deg_U\mathcal H\le4,\qquad [U^4]\mathcal H=\frac{k_{tt}^2}{4\rho^3},\\
k_{tt}=0\quad\Longrightarrow\quad\deg_U\mathcal H\le2.
\end{gathered}
\tag{7}
\]
For the last implication, the derivatives \(k_{ttt},k_{tt\rho}\)
also vanish. The sextic is nonzero independently of all lower data.
The missing third and fourth rho derivatives in the radical chart
cannot be dropped in this rank-two chart.

## 3. Actual gradients, conductor and component multiplicity

Use evaluated quantities
\[
\begin{gathered}
B_1=S_U(y,\vartheta),\qquad
C_1=2\rho^{-3}w+c(y,\vartheta),\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\quad i=t,\rho,\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
J_0=[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw]_{dt\wedge d\rho\wedge dv}.
\end{gathered}
\tag{8}
\]
In \(\Lambda_i\), differentiate formal coefficients before evaluation.
In particular \(\mathcal R_\rho=-6\rho^{-4}V+k_{\rho\rho}\);
it is not merely \(k_{\rho\rho}\).

Let \(\mathcal K(U,V,W_0)=\rho^{-3}W_0^2+cW_0+Q\).
The evaluated gradients of the two polynomial potentials are
\[
\begin{gathered}
(\mathcal RW_0+S-\ell)_{U,V,W_0}=(B_1,C_1,R),\\
\mathcal K_{U,V,W_0}=(-\Lambda_t,-\Lambda_\rho,C_1),\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho).
\end{gathered}
\tag{9}
\]
For example \(c_U=\mathcal R_t\), \(c_V=\mathcal R_\rho\),
\(Q_U=S_t-\ell_t\), and \(Q_V=S_\rho-\ell_\rho\).
Alternatively differentiate
\(\mathcal H=\mathcal R^2\mathcal K(U,V,T/\mathcal R)\);
the factor \(\mathcal K\) vanishes after evaluation.

The wedge expansion in (8), with both signs retained, gives
\[
\begin{gathered}
R^3J_0=D_U\mathcal H_U(y,\vartheta)+D_V\mathcal H_V(y,\vartheta),\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v.
\end{gathered}
\tag{10}
\]
This is the same algebraic wedge identity as206, now using the new
coefficients (8), not copied radical potentials.

Put \(C=L[y,\vartheta]\) and \(O=L[v]\). The second identity in (5)
and the actual whole-line return show \(O=C[w]\).
The quadratic in (5) has unit leading coefficient in \(L\), so
\[
O=C+Cw,\quad \operatorname{Frac}C=L(v),\quad C_R=O_R,\quad RO\subset C.
\tag{11}
\]
Here \(1,w\) are module generators, not a free basis. The fraction
field and localization equalities use \(w=T/R\).
Thus \(O\) is finite over \(C\) and is its normalization.

Let \(G\) generate the height-one evaluation kernel
\(L[U,V]\to O\). It divides \(\mathcal H\).
Equation (10) shows that the factor is simple. Writing
\(\mathcal H=GQ_1\), it also proves
\[
0\ne Q_1(y,\vartheta)\mid R^3\quad\hbox{in }L[v].
\tag{12}
\]
No assertion that \(Q_1(y,\vartheta)\) is a unit follows.

## 4. Strict ordering of the projected degrees

Write \(d=\deg_v y\), \(e=\deg_v\vartheta>0\), and \(g=\deg G\).
For clarity, the degree of a constant or zero first entry causes
no problem in the following maximum.
The finite birational parametrization gives
\[
g=\max(d,e),\qquad \deg_U G=e.
\tag{13}
\]
Here is an exact-field verification. A polynomial \(p(v)\) of degree
\(j>0\) gives \([L(v):L(p)]=j\): \(p(T)-Z_0\) is irreducible,
being primitive and linear in \(Z_0\), and Gauss's lemma applies.
Use this for \(p=\vartheta\), and then for \(p=s_0y+\vartheta\)
over the purely transcendental field \(L(s_0)\).
The irreducible relation \(G(U,Z_0-s_0U)\) has U-degree \(g\),
because \(G_g(1,-s_0)\ne0\). Birationality identifies both extensions.

Since the top of \(\mathcal H\) is a pure power of \(V\), its
factor \(G\) has \(G_g=\gamma V^g\), with \(\gamma\in L^*\).
Thus \(\deg_U G<g\). Combining this with (7) and (13) gives
\[
1\le e<d\le6,\qquad e\le4,\qquad
k_{tt}=0\ \Longrightarrow\ e\le2.
\tag{14}
\]
This proves that \(y\) is nonconstant; it is not assumed.
In particular the affine-pair input of211, \(d=e=1\), is impossible
in the present branch.

There is one further elementary leading restriction:
\[
k_{tt}\ne0\quad\Longrightarrow\quad d\le2e.
\tag{15}
\]
If \(d>2e\), the U-fourth term in (7), after evaluation, has
degree \(4d\). All other terms have smaller degree. To check this
without an unstated Newton polygon, the U-third coefficient has
V-degree at most two; the U-second coefficient has V-degree at
most three; the U-first coefficient has V-degree at most four;
and the U-zero coefficient has V-degree at most six.
Their degrees are at most \(3d+2e,2d+3e,d+4e,6e<4d\).
The U-fourth term cannot cancel, a contradiction.

If \(d,e>1\) are coprime, the conductor gives
\[
(d-1)(e-1)\le e.
\tag{16}
\]
For completeness, multiplication by \(\vartheta\) on the free
\(L[y]\)-module \(O\) has a monic characteristic polynomial of
degree \(d\), which is its minimal polynomial by birationality.
Hence \(C=\bigoplus_{j=0}^{d-1}L[y]\vartheta^j\).
The leading degrees of the summands are distinct modulo \(d\).
The degree semigroup of \(C\) is therefore \(\langle d,e\rangle\),
whose largest missing integer is \(de-d-e\).
But \(Rv^j\in C\) has degree \(e+j\) for every \(j\ge0\), proving
(16). The elementary residue-class proof is also fully written in
[conductor206](radical-projection-conductor-cubic-reduction-pass206-working.md).

Consequently the only possible pairs left by these bounds are
\[
(d,e)=(d,1)\ (2\le d\le6),\quad
(3,2),(4,2),(6,2),(6,3),(6,4).
\tag{17}
\]
This is a necessary list, not a realization classification.
For \(e=1,d>2\), or for \((d,e)=(6,2)\), equation (15) also forces
\(k_{tt}=0\).

## 5. Centers and a new asymmetric cone lemma

Set
\[
V_c=-\rho^3k_\rho/2,\qquad p(U)=S(U,V_c)-\ell,\qquad
S-\ell=p(U)-\mathcal R D(U,V),\qquad \deg D\le2 .
\tag{18}
\]
Polynomial division supplies \(D\) over \(L\), and \(\deg p\le2\).
The degree of \(D\) is now two, not the radical chart's bound one.
The exact identities are
\[
R\{w-D(y,\vartheta)\}+p(y)=0,\qquad
\mathcal H(U,V_c)=\rho^{-3}p(U)^2.
\tag{19}
\]
If \(p\in L^*\), the first equation makes \(R\) a unit of \(O\),
contrary to (3). If \(p=0\), it makes \(w=D(y,\vartheta)\).
The first potential then has
\(B_1=-R D_U\), \(C_1=-R D_V\), after evaluation.
Equation (8) makes \(J_0\) divisible by \(R\) in \(O\); again \(R\)
is a unit. Thus both centers force constant \(\vartheta\), already
recognized by210. They cannot occur under (3).

We need a new bound for the repeated center. The retained
[cone184](vertex-free-quintic-cone-projection-pass184-working.md)
only gives a symmetric degree bound five, so it cannot simply be
invoked at degree six.

**Asymmetric cone lemma.** Over a characteristic-zero field \(F\),
suppose \(P,Q,S_0\in F[v]\) satisfy
\[
P\ne0,\quad PS_0=Q^2,\quad F[P,Q,S_0]=F[v],\quad
(P,Q,S_0)F[v]=F[v],\quad \deg P\le4.
\tag{20}
\]
Then \(F[P,Q]=F[v]\). There is no bound on \(\deg Q\).

Here is a complete proof, including the low-degree cases.
Extend scalars to an algebraic closure \(K\). Equality descends
because \(K\otimes_F(F[v]/F[P,Q])=0\) implies the original
vector-space quotient is zero. If \(Q=0\), then \(S_0=0\);
the unit condition makes \(P\) constant, contradicting generation.
All three entries are therefore nonzero.

The unit condition makes \(P,S_0\) coprime. Factorization and the
cone equation give \(P=a_1^2,Q=a_1b_1,S_0=b_1^2\), after absorbing
nonzero scalar squares, with \(\gcd(a_1,b_1)=1\).
Put \(m_1=\deg a_1\le2\), \(n_1=\deg b_1\).
The three squares and product generate \(K[v]\).
Two distinct parameter values where both \(a_1,b_1\) change sign
would contradict this generation.

If \(m_1=0\), the nonzero constant \(a_1\) directly gives
\(K[P,Q]=K[b_1]=K[v]\).
If \(m_1=1\), use \(x=a_1\) as affine parameter and write
\(b_1=B(x^2)+xC(x^2)\), with \(B(0)\ne0\).
If \(B\) were nonconstant, one of its roots \(s\ne0\) would give
opposite nonzero points \(x_0,-x_0\), \(x_0^2=s\), where both
entries change sign. Thus \(B=b_0\in K^*\), and
\(x=(Q-PC(P))/b_0\in K[P,Q]\).
There is no bound on \(n_1\) needed in this case.

It remains to rule out \(m_1=2\).
If \(n_1=0\), the triple generates \(K[a_1]\), not \(K[v]\).
If \(n_1=1\), use \(x=b_1\); write
\(a_1=A x^2+B x+C\), with \(AC\ne0\) by degree and coprimality.
Choose \(x_0^2=-C/A\ne0\). Both entries change sign at
\(x_0,-x_0\), a contradiction.
If \(n_1=2\), subtract a scalar multiple of \(a_1\) from \(b_1\)
to reduce its degree to at most one. This preserves coprimality
and the triple ring because the new product and square are
\(Q-\lambda P\) and \(S_0-2\lambda Q+\lambda^2P\).
The preceding cases apply.

For every remaining degree, normalize \(a_1=x^2+c_0\) by a constant
rescaling and an affine parameter change. The substitutions
\[
\begin{gathered}
b_1'=b_1-a_1 H(a_1^2),\qquad
Q'=Q-PH(P),\\
S_0'=S_0-2QH(P)+PH(P)^2,\qquad H\in K[T],
\end{gathered}
\]
preserve coprimality, the full triple ring and the plane ring
\(K[P,Q]\). Their inverse formulas replace \(H\) by \(-H\).
If the highest degree \(n_1\) is congruent to two modulo four,
choose a monomial \(H\) to cancel it. Repeating strictly decreases
the degree and terminates. A constant remainder cannot generate
\(K[v]\); a zero remainder contradicts coprimality.
Thus it remains to consider a positive degree \(n_1\not\equiv2\pmod4\).

Seeking opposite values at \(x_1,x_2\), put
\(\sigma_0=x_1+x_2\), \(\pi_0=x_1x_2\).
The equation \(a_1(x_1)+a_1(x_2)=0\) gives
\(\pi_0=(\sigma_0^2+2c_0)/2\).
The power sums \(s_j=x_1^j+x_2^j\) are polynomials in \(\sigma_0\):
\(s_0=2,s_1=\sigma_0\), and
\(s_j=\sigma_0s_{j-1}-\pi_0s_{j-2}\).
Their coefficient of \(\sigma_0^j\) is
\(((1+i)/2)^j+((1-i)/2)^j\).
It is zero exactly when \(i^j=-1\), that is, \(j\equiv2\pmod4\).
The polynomial \(b_1(x_1)+b_1(x_2)\) therefore has positive degree
\(n_1\) in \(\sigma_0\), and has a root in \(K\).
For such a root take \(x_1,x_2\) as the roots of
\(T^2-\sigma_0T+\pi_0\).
They cannot coincide, since a coincident point would make both
\(a_1,b_1\) zero. Their three cone values agree, contradicting
generation. This handles all degrees.

For the first new finite case, and the cubic case used in184, write
\[
b_1=A_4x^4+A_3x^3+A_2x^2+A_1x+A_0.
\tag{21}
\]
Either \(A_4\ne0\), or \(A_4=0,A_3\ne0\).
The two sign-change equations explicitly become
\[
\begin{gathered}
\pi_0=(\sigma_0^2+2c_0)/2,\\
-\tfrac12A_4\sigma_0^4-\tfrac12A_3\sigma_0^3
 -2A_4c_0\sigma_0^2+(A_1-3A_3c_0)\sigma_0
 +2A_4c_0^2-2A_2c_0+2A_0=0 .
\end{gathered}
\tag{22}
\]
The nonzero quartic or cubic coefficient exhibits the same
contradiction directly in these low degrees.
This completes the asymmetric lemma and its exact-field descent.
The degree-six countercontrol in184 has \(\deg P=6\), and does
not contradict this stronger bound on the first cone coordinate.

## 6. Exclusion of the repeated-quadratic center

Suppose \(p=\kappa(U-U_0)^2\), with \(\kappa\in L^*\).
Its repeated root \(U_0\) belongs to \(L\).
Set
\[
P=R,\qquad Q_c=y-U_0,\qquad
S_c=-\{w-D(y,\vartheta)\}/\kappa .
\tag{23}
\]
Then \(PS_c=Q_c^2\), and the triple generates \(O\).
Indeed \(P\) recovers \(\vartheta\), \(Q_c\) recovers \(y\), and
\(S_c\) recovers \(w\).
At a common zero of the triple, the first potential has gradients
\[
B_1=-R D_U+2\kappa(y-U_0),\qquad
C_1=2\rho^{-3}(w-D)-R D_V,\qquad
(\mathcal R W_0+S-\ell)_{W_0}=R.
\tag{24}
\]
They all vanish, contradicting the actual scalar determinant (8).
Thus the triple is vertex-free over an algebraic closure.
Its degrees satisfy \(\deg P=e\le4\), \(\deg Q_c=d\le6\).
The new lemma, with all hypotheses now checked, proves \(C=O\)
in this conditional center branch.

Every root of \(R\) has \(y=U_0,\vartheta=V_c\).
The vertex exclusion makes \(w-D\ne0\) there, so (19) gives
\(\operatorname{ord}R=2\operatorname{ord}(y-U_0)\).
Because \(v\) is a polynomial in \(y,\vartheta\), their derivatives
cannot both vanish at a point. The displayed orders make
\(\vartheta_v=0\), so \(y_v\ne0\), and each root of \(R\) has
multiplicity exactly two.
There is only one distinct root: two roots would have identical
\((y,\vartheta)\), contradicting that these generate \(O\).
Consequently \(e=2\). The unique root lies in \(L\), by
separability or by the linear coefficient of the quadratic \(R\).

Normalize \(G\) to be monic of degree two in \(U\).
This is justified integrally: \(O\) is a free rank-two module over
\(L[\vartheta]\), and the characteristic polynomial of multiplication
by \(y\) equals its minimal polynomial by birationality.
Over \(\vartheta=V_c\) the fiber is \(L[x]/(x^2)\), where
\(x=v-v_0\), and \(y=U_0+b_1x\) modulo \(x^2\), \(b_1\ne0\).
Its characteristic polynomial is \((U-U_0)^2\). Hence
\[
G(U,V_c)=(U-U_0)^2,\qquad
Q_1(U,V_c)=\rho^{-3}\kappa^2(U-U_0)^2.
\tag{25}
\]
No reduced-fiber or etale assumption is used.

Both polynomials in (25) have U-degree two.
But their top total homogeneous forms multiply to
\(-\rho^{-11}V^6\), so each top form is a pure power of \(V\).
Each polynomial therefore has total degree at least three.
Their total degrees sum to six, forcing both degrees to be three.
By (13), this gives \(d=3,e=2\).

Here is an elementary contradiction to \(C=O\) in these degrees.
Over an algebraic closure, normalize the quadratic \(\vartheta\)
to \(x^2\) by scalar and constant changes and an affine parameter.
Subtract its multiple and a constant from the cubic \(y\), giving
\(A x^3+B x\), \(A\ne0\).
If \(B\ne0\), the nonzero roots of \(A x^2+B\) are opposite and
give equal values of both generators, contradicting generation.
If \(B=0\), both generator derivatives vanish at zero, also
contradicting generation of \(x\). Thus this last possibility
is impossible. The repeated-quadratic center is excluded.

## 7. Remaining gate and the primitive auxiliary derivation

Under (3), the center must consequently be nonconstant and squarefree
of degree one or two. The degree bounds (14)--(17), conductor (11),
and cofactor support (12) are necessary restrictions, not recognition.
In particular this note does not infer \(C=O\) in the remaining cases.

The actual auxiliary construction still gives
\(P=aN-(NX)E\), a nonzero polynomial LND fixing \(X\) and commuting
with \(E\). It is locally nilpotent on \(B_a=A_a[X]\), where it
restricts to \(aN\), and preserves \(B\) by its formula.
Primitive division is also available. For a gcd \(\Delta\) of its
polynomial coefficients, \(P\Delta=\Delta(P/\Delta)(\Delta)\).
LND-degree additivity forces \(P\Delta=0\).
Since \(\Delta\) divides \(PY=aNy\ne0\), which is E-invariant,
factorial closure gives \(E\Delta=0\).
Thus \(P/\Delta\) is again an actual commuting LND.

This does not supply211's quasi-nice input: by (14),
\[
\deg_PY=d>e\ge1,\qquad P^2Y\ne0.
\tag{26}
\]
Primitive division preserves these derivation degrees.
There is no established replacement pair of actual coordinates
with square-zero iterates, or generic Wang invariant of the specific
fiber-contraction form211. Neither a coefficient-field reparametrization
nor the simple existence of a commuting action supplies such a pair.
The known constant-second and zero-return recognition theorems
remain valid separate branches; no nonconstant squarefree rank-two
branch is recognized or excluded by the present note.

The retained universal, classification, radical eliminant/conductor
and cone sources were freshly read before this argument. A new
inline symbolic expansion checked (7), (19), and the opposite-point
polynomial (22); it was not a saved checker or a proof of the geometric
arguments. No saved suite was run, imported or compiled, and no
earlier source or index was edited. The full cancellation goal,
arbitrary entry, other initial kernels, and historical novelty remain
outside this working result.
