# Exclusion of the linear rank-two center with quadratic second projection

Status: bounded working exclusion under the actual supplied rank-two
exact1122 hypotheses. A linear center cannot have second projected
degree two. The evaluated cofactor first forces the degree-six case;
two further coefficient identities and actual complex-coefficient
shears then force an impossible algebraic Euler exponent.
This is not a theorem about arbitrary supplied frames or unrestricted
complex-threefold cancellation.

## 1. Actual hypotheses and exact-field conventions

Retain the actual hypotheses of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\qquad
N=[u^3](\partial_Z|_A)\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\quad
[L:\mathbb C(t,\rho)]<\infty,\quad q=1/\rho,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+\rho^{-1}X^2 .
\end{gathered}
\tag{1}
\]
The initial ideal is the full kernel, not merely a vanishing
relation. The ratios \(t,\rho\) are algebraically independent.
Their commuting coefficient partials extend uniquely to the finite
separable field \(L\), and keep the line parameter \(v\) fixed.
No rationality of \(L\) is assumed.

Use the exact potentials of212, with independent formal \(U,V\):
\[
\begin{aligned}
\mathcal R&=2\rho^{-3}V+k_\rho,\\
S&=-\rho^{-4}V^3+\tfrac12k_{tt}U^2+k_{t\rho}UV
       +\tfrac12k_{\rho\rho}V^2+n_tU+n_\rho V,\\
T&=\ell-S,\qquad
c=-3\rho^{-4}V^2+k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Q&=\rho^{-5}V^4+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H&=\rho^{-3}T^2+\mathcal R cT+\mathcal R^2Q .
\end{aligned}
\tag{2}
\]
Here \(H_j(b)=\sum_{i=0}^j b_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
All coefficient derivatives in (2) keep \(U,V\) fixed.
The actual identities include \(Rw=T(y,\vartheta)\) and
\(\mathcal H(y,\vartheta)=0\), where
\(R=2\rho^{-3}\vartheta+k_\rho\).

Assume the linear-center, quadratic-second branch:
\[
\begin{gathered}
\deg_v\vartheta=2,\quad V_c=-\rho^3 k_\rho/2,\\
p(U)=S(U,V_c)-\ell=B(U-U_0),\qquad B\in L^*,\quad U_0\in L .
\end{gathered}
\tag{3}
\]
In particular \(k_{tt}=0\). The actual determinant and field return
proved in212 give, for the irreducible evaluation relation \(G\),
\[
\begin{gathered}
\mathcal H=GQ_1,\qquad
0\ne Q_1(y,\vartheta)\mid R^3\quad\hbox{in }L[v],\\
\deg\mathcal H=6,\quad\mathcal H_6=-\rho^{-11}V^6,\quad
\deg_U\mathcal H\le2,\quad \deg G=d=\deg_vy .
\end{gathered}
\tag{4}
\]
The factor is simple. We use precisely this actual cofactor result,
not a cofactor assumption on a freely parametrized plane curve.

Two elementary field facts will be used below. If \(b\in L\) has
\(b_t=0\), differentiate its monic minimal polynomial over
\(\mathbb C(t,\rho)\). The resulting polynomial in \(b\) has smaller
degree, so all differentiated coefficients vanish. Those coefficients
therefore lie in \(\mathbb C(\rho)\), and \(b\) is algebraic over
\(\mathbb C(\rho)\). Applying the same argument with both partials
shows that their joint constant field in \(L\) is \(\mathbb C\).
These facts do not identify either one-partial constant field with a
rational function field.

## 2. The explicit monic plane relation

The complete
[linear-center ring description213](rank-two-linear-center-quadratic-projection-pass213-working.md)
gives, over the exact field \(L\),
\[
\begin{gathered}
x=v-v_0,\qquad \vartheta=A_2x^2+c_0,\qquad A_2\in L^*,\\
y=U_0-\frac{R}{B}\{P(\vartheta)+b_1x\},\qquad
P\in L[V],\quad b_1\in L^* .
\end{gathered}
\tag{5}
\]
These are identities of projected polynomials, not ambient coordinate
changes. In particular no square root of \(A_2\) is required.
Put
\[
J(V)=U_0-\frac{\mathcal R(V)}B P(V),\qquad
\epsilon=\frac{b_1^2}{B^2A_2}\in L^* .
\tag{6}
\]
We may and do choose the selected monic relation to be
\[
G(U,V)=(U-J(V))^2-\epsilon\mathcal R(V)^2(V-c_0).
\tag{7}
\]
Indeed (5) makes it vanish. It is irreducible over \(L(V)\), since
\(\epsilon(V-c_0)\) has odd valuation at \(V=c_0\) and is not a
square. Its monic U-degree is two, so Gauss's lemma and the
height-one evaluation kernel prove the claim.

The degree bound \(d\le6\) and (5) give \(\deg P\le2\).
Consequently \(\deg J\le3\), the U-linear coefficient of \(G\)
has V-degree at most three, and its discriminant in U is the
degree-three polynomial \(4\epsilon\mathcal R^2(V-c_0)\).
These statements hold for both the node and the cusp of213.

## 3. Cofactor support forces degree six

Write
\[
j=k_\rho,\quad K=k_{t\rho},\quad N_0=n_t,\qquad
B=N_0-\tfrac12\rho^3jK,\qquad
\delta=2n_{tt}-\rho^3K^2 .
\tag{8}
\]
The displayed value of \(B\) is exactly the center slope in (3).
Taking the U-quadratic coefficient directly in (2) gives
\[
\begin{aligned}
A(V):=[U^2]\mathcal H
 &=\rho^{-3}(KV+N_0)^2
       -\mathcal R K(KV+N_0)+\tfrac12n_{tt}\mathcal R^2\\
 &=\rho^{-3}B^2+\tfrac14\delta\mathcal R^2 .
\end{aligned}
\tag{9}
\]
Since both \(\mathcal H\) and the monic \(G\) have U-degree two,
their quotient is in \(L[V]\), and comparison of U-quadratic
coefficients identifies \(Q_1=A(V)\) exactly.

At \(V=V_c\), \(A(V_c)=\rho^{-3}B^2\ne0\).
Thus \(A(V)\) is coprime to the linear polynomial \(\mathcal R(V)\)
in \(L[V]\). A Bezout identity remains a Bezout identity after
evaluating at \(V=\vartheta\). Hence \(A(\vartheta)\) is coprime
to \(R\) in \(L[v]\). But (4) says \(A(\vartheta)\mid R^3\).
It follows that \(A(\vartheta)\in L^*\), and the nonconstant
\(\vartheta\) forces \(A(V)\) itself to be constant.
Therefore
\[
\delta=0,\qquad B_t=0,\qquad
\mathcal H=\rho^{-3}B^2G,\qquad d=6,\qquad \deg J=3 .
\tag{10}
\]
Here \(B_t=n_{tt}-\rho^3K^2/2\), using \(k_{tt}=0\).
This already excludes the degree-three and degree-four alternatives
in213 without solving any differential equation.

## 4. A high coefficient and actual lower-time normalization

For transparency, put
\[
\begin{gathered}
\phi=-\rho^{-4}V^3+\tfrac12k_{\rho\rho}V^2+n_\rho V,\quad
T_0=\ell-\phi,\quad
c_0^*=-3\rho^{-4}V^2+k_{\rho\rho}V+n_\rho,\\
A_0=KV+N_0 .
\end{gathered}
\tag{11}
\]
Since \(k_{tt}=0\), expansion of (2) gives the entire U-linear
coefficient, before any parameter-dependent evaluation:
\[
[U]\mathcal H=(-2\rho^{-3}A_0+\mathcal RK)T_0
 -\mathcal R c_0^*A_0
 +\mathcal R^2\{\tfrac12K_\rho V^2+n_{t\rho}V-\ell_t\}.
\tag{12}
\]
In view of (8), the first parenthesis is \(-2\rho^{-3}B\).
Taking the V-fourth coefficient in (12), while retaining every
coefficient derivative, yields
\[
[UV^4]\mathcal H=2\rho^{-7}(3K+\rho K_\rho)=0 .
\tag{13}
\]
The vanishing follows from (7) and (10), not from a guessed normal
form for the lower potentials. Thus \((\rho^3K)_\rho=0\).
Also \(K_t=0\), so joint constants give \(\rho^3K=c\in\mathbb C\).
Integrating once inside \(L\), again using joint constants, gives
\[
k_t=c_*-\frac{c}{2\rho^2},\qquad c,c_*\in\mathbb C .
\tag{14}
\]
For example \(\partial_\rho(k_t+c/(2\rho^2))=0\) and its
t-partial is zero, which proves the assertion without a rational
ansatz.

Now make only the following actual polynomial coordinate changes:
\[
X'=X,\qquad Y'=Y,\qquad
W'=W+\tfrac c2Y,\qquad Z'=Z-c_*Y .
\tag{15}
\]
Their inverse is
\(X=X',Y=Y',W=W'-cY'/2,Z=Z'+c_*Y'\), so both inverse
orders are literal identity substitutions. Their coefficients are
complex constants. The added terms have E-degree one, so the exact
1122 profile and all four leading coefficients are unchanged.
In particular the full initial kernel in (1) remains unchanged.
Also \(\partial_{Z'}=\partial_Z\) as original derivations: the other
three new coordinates are fixed by \(\partial_Z\), and its value
on \(Z'\) is one. Thus \(N,L,t,\rho,a=EX\), and the coefficient
partials are all unchanged. This is not a descent of an arbitrary
\(L\)-coordinate change.

Here is the exact center-slope check. For the intermediate change
\(W'=W+\alpha Y+\beta X\), with \(\alpha,\beta\in\mathbb C\),
write \(b(t)=\alpha t+\beta\). Substitution in the first two
potentials gives
\[
\begin{gathered}
\vartheta'=\vartheta+b(t),\quad w'=w+\alpha y,\quad
k'=k+\rho^{-2}b(t),\quad
n'=n-k_\rho b(t)+\rho^{-3}b(t)^2,\\
k'_{t\rho}=K-2\alpha\rho^{-3},\quad
k'_\rho=j-2\rho^{-3}b(t),\\
n'_t-\tfrac12\rho^3 k'_\rho k'_{t\rho}
 =n_t-\tfrac12\rho^3jK=B .
\end{gathered}
\tag{16}
\]
The change \(Z'=Z-c_*Y\) then sends \(k'\) to \(k'-c_*t\)
and does not change \(n'\), so it also preserves \(B\).
Taking \(\alpha=c/2,\beta=0\) in (16) and using (14) makes
the final \(k_t\) vanish.

The actual chart can be rebuilt with these new coordinates, with
the same exact hypotheses. The first projected entry is unchanged,
and the second changes by a scalar of \(L\); thus \(d=6,e=2\)
remain unchanged. The center is still linear with the same nonzero
slope \(B\), since \(k_{tt}=0\) remains true. Reapply (5)--(10)
to this actual chart and relabel its potentials. We now have
\[
k_t=K=0,\qquad n_t=B,\qquad n_{tt}=B_t=0,
\qquad \mathcal H=\rho^{-3}B^2G .
\tag{17}
\]
No formula for the newly chosen \(\ell,m\) is assumed.

## 5. The discriminant forces a forbidden algebraic exponent

With (17), the full coefficient formula (12) specializes to
\[
[U]\mathcal H=-2\rho^{-3}B(\ell-\phi)
 -\mathcal R c_0^*B
 +\mathcal R^2(B_\rho V-\ell_t).
\tag{18}
\]
Its V-cubic coefficient, together with two retained coefficients,
is
\[
[UV^3]\mathcal H=4\rho^{-7}(B+\rho B_\rho),\qquad
[U^2]\mathcal H=\rho^{-3}B^2,\qquad
[V^6]\mathcal H=-\rho^{-11} .
\tag{19}
\]
For the first equality, the leading cubic coefficient in
\(2\rho^{-3}\phi-\mathcal R c_0^*\) is \(4\rho^{-7}\),
and that in \(\mathcal R^2B_\rho V\) is \(4\rho^{-6}B_\rho\).
Terms involving \(\ell_t\) have V-degree at most two.

Equation (7) has degree-three discriminant and \(\deg J=3\).
Consequently the degree-six coefficient in its constant term is
the square of the cubic coefficient of \(J\). Multiplying by
the nonzero scalar in (17) gives the exact identity
\[
([UV^3]\mathcal H)^2
 =4[U^2]\mathcal H\,[V^6]\mathcal H .
\tag{20}
\]
Substitute (19) and divide only by nonzero elements of \(L\):
\[
4\left(1+\frac{\rho B_\rho}{B}\right)^2=-1,
\qquad
\rho B_\rho=\lambda B,\qquad
\lambda=-1+\tfrac i2\ \hbox{or}\ -1-\tfrac i2 .
\tag{21}
\]
The field is a domain containing \(\mathbb C\), so the two possible
roots in (21) are precisely those displayed constants.

By \(B_t=0\) and the exact-field fact proved after (4), the nonzero
\(B\) is algebraic over \(F=\mathbb C(\rho)\).
Let \(M=F(B)\), of finite degree \(m\), and let
\(b_0=\operatorname{Norm}_{M/F}(B)\in F^*\).
Each of the \(m\) conjugates of \(B\) satisfies the same Euler
equation, because the extension of \(\partial_\rho\) is unique
in characteristic zero. Differentiating their product therefore
gives
\[
\rho\frac{b_0'}{b_0}=m\lambda .
\tag{22}
\]
This norm argument can equivalently be read from the nonzero
constant term of the monic minimal polynomial of \(B\).
Write \(b_0=\rho^j h(\rho)\) at zero, where \(j\in\mathbb Z\)
and \(h\) is a rational function regular and nonzero there.
The value at zero of the left side of (22) is \(j\).
Thus \(m\lambda=j\), so \(\lambda\in\mathbb Q\).
Both values in (21) are nonreal, a contradiction.

## 6. Bounded conclusion and verification scope

There is no actual frame satisfying (1) whose center is linear and
whose second projected degree is two. This simultaneously eliminates
the three pairs \((3,2),(4,2),(6,2)\) in that center branch.
The first two disappear by the evaluated cofactor support alone;
the last uses the full coefficient identities and actual shears.
No claim is made here about linear centers with affine second
projection, quadratic centers, other initial ideals, arbitrary
entry, or unrestricted cancellation.

The complete212 and213 sources were reread before this proof.
One fresh unsaved symbolic calculation checked (9) under \(\delta=0\),
(13), the first coefficient in (19), and the center-slope identity
in (16). Those finite identities do not prove the field-return,
cofactor, irreducibility, or algebraic-function arguments.
No saved checker was executed, imported or compiled. No earlier
source, checkpoint, index or packet was changed.
