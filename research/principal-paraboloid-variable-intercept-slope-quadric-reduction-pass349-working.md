# Variable intercept slope: an irreducible quadric and birational projection

Working result: retain the full actual chart264, and assume
\(k=s\), \(n_{ss}=0\), and \(n_{ts}\ne0\). The third relation is an
absolutely irreducible quadratic surface, and the fourth potential has
exact total degree three. The projection to \((\sigma,\theta)\) is
birational, not of degree two. Its implicit degree and all three
intrinsic polynomial degrees are at most six.

The note gives the complete specialized gradients, centered potentials,
and an exact denominator/conductor boundary. It does not prove that the
projected plane ring is normal or equal to the whole polynomial line.
It makes no actual coordinate change by the nonconstant function
\(B(t)\), and supplies no recognition conclusion for this branch.

## 1. Full actual hypotheses and exact coefficient fields

Retain the full hypotheses, literal selected partial, and actual returns
of [264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
a=EX\ne0,\quad L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\\
O=A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The coefficient partials \(\partial_t,\partial_s\) commute, extend
uniquely to \(L\), and fix the original \(v\). The actual expansions are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{aligned}
\tag{2}
\]
Here the extra assumptions are exactly
\[
k=s,\qquad n_{ss}=0,\qquad n_{ts}\ne0.
\tag{3}
\]
Put \(F=\ker_L\partial_s\). This is a finite extension of
\(\mathbb C(t)\): an element killed by \(\partial_s\) has a monic
minimal polynomial over \(\mathbb C(t,s)\) whose differentiated
coefficients vanish, and hence is algebraic over \(\mathbb C(t)\).
Conversely, algebraic elements over \(\mathbb C(t)\) are killed by
\(\partial_s\). Finiteness follows inside the finitely generated field
\(L\). The constants of \(\partial_t\) on \(F\) are \(\mathbb C\).
Thus exact integration of (3), inside \(L\), gives
\[
n=B(t)s+f(t),\qquad B,f\in F,\qquad b:=B'\ne0.
\tag{4}
\]
Primes denote \(\partial_t\) on \(F\). No rationality of \(F\) or
\(L\) is assumed. Write \(u_1=n_t\) below; this is not the original
slice \(u\).

The first two literal potentials are
\[
z=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-u_1\sigma-B\theta,\qquad \ell\in L.
\tag{5}
\]
They give the genuine three-generator return
\(O=L[y,\sigma,\theta]\), as in264. They do not yet give a
two-generator return.

## 2. The full third relation and fourth gradient

Use independent formal variables \(U,P,V\), and put
\(g=\ell-2PU-u_1P-BV\). Direct specialization of264 gives
\[
\begin{aligned}
H={}&U^2+(u_1-2BP)U+\frac{n_{tt}}2P^2+bPV\\
 &-(\ell_t+Bu_1)P-(\ell_s+B^2)V+B\ell,
\qquad H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{6}
\]
In particular this is a quadratic, not a general cubic surface.
All coefficient partials in what follows hold \(U,P,V\) fixed.

The corrected gradient construction of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
specializes to
\[
Q_U=H_P-2PH_V+BH_U,\quad
Q_P=H_t-h_t-(2U+u_1)H_V+BH_P,\quad
Q_V=H_s-h_s.
\tag{7}
\]
Keeping every mixed derivative gives the complete three components:
\[
\begin{aligned}
Q_U={}&-2bP^2+(n_{tt}+2\ell_s)P+bV-\ell_t,\\
Q_P={}&(n_{tt}-4bP+2\ell_s)U+\frac{n_{ttt}}2P^2+b'PV\\
 &-(\ell_{tt}+2bu_1)P-(\ell_{ts}+Bb)V
       +b\ell+u_1\ell_s-h_t,\\
Q_V={}&bU+\frac{b'}2P^2-(\ell_{ts}+Bb)P
       -\ell_{ss}V+B\ell_s-h_s.
\end{aligned}
\tag{8}
\]
These are the derivatives of the following primitive, normalized to
vanish at the formal origin:
\[
\begin{aligned}
Q={}&\{-2bP^2+(n_{tt}+2\ell_s)P+bV-\ell_t\}U
       +\frac{n_{ttt}}6P^3\\
 &-\frac{\ell_{tt}+2bu_1}{2}P^2
       +\frac{b'}2P^2V-(\ell_{ts}+Bb)PV-\frac{\ell_{ss}}2V^2\\
 &+(b\ell+u_1\ell_s-h_t)P+(B\ell_s-h_s)V.
\end{aligned}
\tag{9}
\]
The term \(-2bP^2U\) is nonzero, so \(\deg Q=3\) exactly.
The actual linear Jacobian coefficient gives
\(Q(y,\sigma,\theta)=q_0\in L\).

For completeness, the still-required constant calibration is the literal
determinant of the following rows in \(dt,ds,dv\):
\[
\begin{pmatrix}
dy\\
2\sigma\,d\sigma+d\theta+(2y+u_1)dt+Bds\\
-2\sigma\,dy-(2y+u_1)d\sigma-Bd\theta
 +(\ell_t-n_{tt}\sigma-b\theta)dt+(\ell_s-b\sigma)ds
\end{pmatrix},
\qquad J_0=-a^4.
\tag{10}
\]
This retains all original holding-variable conventions. Relations (6)
and (9) alone do not replace (10).

## 3. Exact centering and absolute irreducibility

Introduce only a formal affine change over \(L\):
\[
\begin{gathered}
x=U+u_1/2-BP,\quad A_2=n_{tt}/2-B^2,\quad
C_2=\ell_s+B^2,\quad T=\ell_t,\\
\bar h=h-B\ell+u_1^2/4,\qquad
\bar q=q_0-u_1T/2.
\end{gathered}
\tag{11}
\]
The corresponding evaluated function is
\(x(v)=y+u_1/2-B\sigma\). We use the same letter for the formal
variable and its evaluation when the distinction is explicit.
The centered third level is
\[
H-h=x^2+J(P,V),\qquad
J=A_2P^2-TP+(bP-C_2)V-\bar h.
\tag{12}
\]
Its homogeneous quadratic part is \(x^2+A_2P^2+bPV\), whose symmetric
matrix has determinant \(-b^2/4\ne0\). A product of two affine linear
polynomials has homogeneous quadratic rank at most two. Therefore
\(H-h\) is irreducible even over an algebraic closure of \(L\).

The centered fourth level has the exact form
\[
Q-q_0=D(P,V)x+E(P,V),\qquad
D=-2bP^2+2(A_2+C_2)P+bV-T,
\tag{13}
\]
where
\[
\begin{aligned}
E={}&\left(\frac{n_{ttt}}6-2Bb\right)P^3+\frac{b'}2P^2V
 +\left(2B(A_2+C_2)-\frac{\ell_{tt}}2\right)P^2\\
 &-\ell_{ts}PV-\frac{\ell_{ss}}2V^2
 +(-\bar h_t-2BT)P-\bar h_sV-\bar q.
\end{aligned}
\tag{14}
\]
These expressions are obtained by substituting (11) into the already
derived primitive (9), not by differentiating moving formal variables
as though they were fixed. In particular the constant subtraction in
\(\bar q\) and both derivatives of \(\bar h\) are required.

An optional further affine change over \(L\), also not ambient, is
\[
\begin{aligned}
p&=P-C_2/b,\\
q&=V+(A_2/b)P+A_2C_2/b^2-T/b,\\
d_0&=\bar h-A_2C_2^2/b^2+TC_2/b.
\end{aligned}
\quad
H-h=x^2+bpq-d_0,\quad
D=bq+(A_2-2C_2)p-2bp^2.
\tag{15}
\]
No division by an evaluated nonconstant polynomial is made in this
formal coefficient-field change.

## 4. Degree-two projection is impossible

Let \(C=L[\sigma,\theta]\subset O\). The whole-line return and (11)
give \(O=C[x]\). Since (12) is monic quadratic in \(x\),
\[
[L(v):\operatorname{Frac}C]\le2.
\tag{16}
\]
The projected field has transcendence degree one: otherwise \(\sigma\)
and \(\theta\) would be constants, and (12) would make \(x\) constant
as well. Polynomial elements of \(L[v]\) algebraic over \(L\) belong
to \(L\).

Suppose the degree in (16) is two. Then \(1,x\) are independent over
\(\operatorname{Frac}C\), so (13) forces \(D(\sigma,\theta)=0\).
Since \(b\ne0\), this means
\[
\theta=2\sigma^2-\frac{2(A_2+C_2)}b\sigma+\frac Tb,
\qquad C=L[\sigma].
\tag{17}
\]
Consequently \(\deg_v\sigma=2\). Translation of \(v\), with no
coefficient square root, writes \(\sigma=a_2\xi^2+c_0\),
\(a_2\in L^*\). Substitution of (17) into (12) gives
\(x^2=R(\sigma)\), where \(R\) has exact degree three and leading
coefficient \(-2b\). Thus \(\deg_\xi x=3\).

Write \(x=e(\xi^2)+\xi a(\xi^2)\). Its square is even, so
\(e a=0\). The cubic degree makes \(a\ne0\), hence \(e=0\) and
\(a\) has exact degree one. But then
\[
C[x]=L[\xi^2]\ \oplus\ \xi a(\xi^2)L[\xi^2]
\ne L[\xi],
\tag{18}
\]
because the nonconstant polynomial \(a\) does not divide one. This
contradicts \(O=C[x]=L[v]\). Hence the projection is birational.
This is an exclusion in the present \(B'\ne0\) specialization, stronger
than recognition of degree-two projections in the broader retained307
sector; no use of that recognition result is needed here.

Furthermore \(D(\sigma,\theta)\ne0\) in the birational case. Otherwise
(17) again gives \(C=L[\sigma]\); \(x\) is integral over this normal
ring and lies in its fraction field, so \(x\in C\). Thus \(O=C\),
\(\deg_v\sigma=1\), and the exact cubic identity \(x^2=R(\sigma)\)
is impossible. This also checks the possible identically-zero
denominator, rather than silently localizing at it.

## 5. A sextic resultant and exact intrinsic-degree bound

Eliminating \(x\) from (12),(13) gives
\[
\mathcal R(P,V)=E(P,V)^2+D(P,V)^2J(P,V),
\qquad \mathcal R(\sigma,\theta)=0.
\tag{19}
\]
It is nonzero: the absolutely irreducible monic quadratic (12) cannot
divide the nonzero polynomial (13) of \(x\)-degree one. Equivalently
their resultant over \(L(P,V)\) is nonzero. Put
\(a_3=n_{ttt}/6-2Bb\), \(b_3=b'/2\). The exact top is
\[
\mathcal R_6=P^4\{(a_3P+b_3V)^2+4b^2(A_2P^2+bPV)\}.
\tag{20}
\]
If \(b'\ne0\), its \(P^4V^2\) coefficient is \((b')^2/4\ne0\).
If \(b'=0\), its \(P^5V\) coefficient is \(4b^3\ne0\).
Thus \(\deg\mathcal R=6\) in every case.

Let \(G(P,V)\) generate the projected plane kernel. It divides
\(\mathcal R\), so \(\deg G\le6\). Birationality gives the elementary
identity
\[
\deg G=\max(\deg_v\sigma,\deg_v\theta).
\tag{21}
\]
Indeed, after adjoining an independent \(\kappa\), the generic linear
combination \(z_1=\theta+\kappa\sigma\) has polynomial degree equal to
the right side, and hence that field degree over \(L(\kappa)(z_1)\).
The irreducible polynomial \(G(P,z_1-\kappa P)\) has exact \(P\)-degree
\(\deg G\), so gives the same field degree. This argument does not
assume that \(C\) is normal.

Finally (12) implies \(\deg_v x\le\max(\deg_v\sigma,\deg_v\theta)\):
otherwise \(x^2\) would have uniquely highest degree in that relation.
Using (11) gives the proved bound
\[
\boxed{[L(v):L(\sigma,\theta)]=1,\qquad
\max(\deg_v y,\deg_v\sigma,\deg_v\theta)=\deg G\le6.}
\tag{22}
\]
The maximum equality follows since the maximum of the last two degrees
is already \(\deg G\). Constants among individual generators cause no
exception.

## 6. What the cofactor and denominator conditions do not prove

Formal affine centering preserves296's unit ideal of evaluated gradient
minors. For \(\widehat H=x^2+J\), \(\widehat Q=Dx+E\), put
\(M_{ij}=\widehat H_i\widehat Q_j-\widehat H_j\widehat Q_i\).
Then
\[
(M_{xP},M_{xV},M_{PV})O=O.
\tag{23}
\]
Write \(\mathcal R=G S_0\). Differentiating (19) and evaluating the two
levels gives the exact projected cofactor equations
\[
S_0(\sigma,\theta)G_P(\sigma,\theta)=-D(\sigma,\theta)M_{xP},
\qquad
S_0(\sigma,\theta)G_V(\sigma,\theta)=-D(\sigma,\theta)M_{xV}.
\tag{24}
\]
They do not say that \(S_0(\sigma,\theta)\), or either projected
gradient, is a unit.

Let \(D_*=D(\sigma,\theta)\ne0\). Monic reduction in (12) gives
\(O=C+Cx\), and (13) gives \(D_*x\in C\). Therefore
\[
D_*O\subset C,\qquad O_{D_*}=C_{D_*}.
\tag{25}
\]
This is a genuine conductor inclusion and a localized polynomial-ring
return. It is not the assertion \(D_*\in L^*\) or \(C=O\).
Likewise the coefficient \(b\sigma-C_2\) of \(\theta\) in (12) is
nonconstant whenever \(\sigma\) is nonconstant. Solving that equation
for \(\theta\) only gives a localized return; the possible exceptional
fibers must still be treated. The constant-\(\sigma\) case is not
silently removed here.

The remaining actual problem includes the constant calibration (10),
the strong \(\mathbb C\)-field return in (1), and descent from these
coefficient-field presentations. In particular \(X\mapsto X+B(t)\)
has not been used as an ambient polynomial automorphism.

The complete264 and296 sources were freshly read. A fresh unsaved
symbolic calculation returned zero for all three components (8), both
centered identities, (20), and the exact cubic coefficient in (17).
The field, parity, and degree arguments above are mathematical proofs,
not claims certified by those finite calculations. No saved checker
was executed, imported, compiled or rerun. No previous source, index
or packet was edited, and no novelty or unrestricted cancellation
claim is made.
