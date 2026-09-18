# An actual three-ring endpoint for a constant-sigma reducible line

Working theorem: in the actual nonzero-coupling chart264, suppose the
surface level is reducible, sigma is constant along the generic line,
and \(m_s=0\), where \(m=k_s\ne0\). Then the sliced kernel is a
polynomial three-ring.

The factorization forces complex coefficients in the literal auxiliary
derivation. Explicit polynomial reframes make its kernel an actual
three-variable polynomial ring preserved by the original derivation.
The endpoint still requires a primitive restriction and two stated
published theorems. No slice of the auxiliary or restricted derivation
is assumed.

## 1. Full actual entry and factor-unit hypotheses

Retain the complete actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), the
two-gradient minor-unit conclusion of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the reducible-surface return of
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad a=EX\ne0,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
0\ne N\in\operatorname{LND}(A),\quad Na=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
K=\operatorname{Frac}A=L(v),\quad Nv=1,\quad
L[y,z,w]=L[y,\sigma,\theta]=L[v],\quad K=\mathbb C(y,z,w),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{gathered}
\tag{1}
\]
Here N is the leading coefficient of the literal Z-partial with exact
shift four. Its annihilation of a is part of264's actual selected-partial
argument. The coefficient partials commute on L and have joint constants
exactly \(\mathbb C\).

Assume the additional branch conditions
\[
m=k_s\ne0,\qquad m_s=0,\qquad \sigma\in L,\qquad
H_0:=H-h_0\text{ is reducible}.
\tag{2}
\]
The projected-line condition follows from302's stronger return:
\[
L[\sigma,\theta]=L[v].
\tag{3}
\]
Indeed sigma is in L, so theta is affine nonconstant in v and
\(N\theta\in L^*\). The projected equation is \(P-\sigma\).
This does not make theta an original-ring coordinate.

For independent formal U,P,V, monicity and the factor-unit statement give
\[
\begin{aligned}
H_0&=U^2+A_1U+A_0=(U+B_1)(U+B_2),\\
B_1+B_2&=A_1,\quad B_1B_2=A_0,\quad
\deg B_i\le2,\quad \deg A_0\le3,\\
y&=-B_1(\sigma,\theta),\qquad
(B_2-B_1)(\sigma,\theta)=\epsilon\in L^*.
\end{aligned}
\tag{4}
\]
Only the selected factor is relabeled. Its companion's evaluated value
divides every component of the first gradient, so the two-gradient
minor-unit property makes that value a unit of \(L[v]\). In particular
\(H_U(y,\sigma,\theta)=\epsilon\).

## 2. The square root is formally independent of V

Put \(p=m_t\). Under \(m_s=0\), the literal coefficients are
\[
\begin{aligned}
\mathfrak F&=k_{tt}P^2/2+pPV+n_tP+n_sV,\\
A_1&=-\frac{2p}{m}P^2+pV+
\left(k_{tt}-\frac{k_tp+2n_s}{m}\right)P+n_t-\frac{k_tn_s}{m},\\
A_0&=\frac{(pP+n_s)(\ell-\mathfrak F)}m
       +H_3(k)+H_2(n)-\ell_tP-\ell_sV-h_0.
\end{aligned}
\tag{5}
\]
The Taylor polynomials retain their factorial denominators. No lower
coefficient of n, ell or h0 is specialized.

At least one of \(B_1,B_2\) has degree at most one: two nonzero quadratic
factors would have product of degree four over the domain \(L[P,V]\).
Thus the quadratic part of \(\Psi:=B_2-B_1\) is, up to sign, that of A1,
or is zero. By(5),
\[
\Psi=\lambda_2P^2+\lambda_1P+\lambda_VV+\lambda_0,\qquad \lambda_i\in L.
\tag{6}
\]
This includes \(p=0\) and the zero-factor cases. Evaluation at sigma in L
and the affine nonconstant theta forces \(\lambda_V=0\), since
\(\Psi(\sigma,\theta)=\epsilon\in L^*\). Therefore
\[
\boxed{\Delta=A_1^2-4A_0=\Psi^2\in L[P].}
\tag{7}
\]
This is formal V-independence, not differentiation at a moving point.

## 3. Three discriminant coefficients give complex slopes

Before imposing \(m_{tt}=0\), expansion of(5) gives
\[
\begin{aligned}
[V^2]\Delta&=p^2-2n_{ss},\\
[P^2V]\Delta&=-2m_{tt},\\
[PV]\Delta&=2pk_{tt}-\frac{2k_tp^2}{m}+\frac{4pn_s}{m}-4n_{ts}.
\end{aligned}
\tag{8}
\]
For example the P-squared-V contributions are \(-4p^2/m\) from
\(A_1^2\) and \(-4(m_{tt}/2-p^2/m)\) from \(-4A_0\).
All three entries vanish by(7). Exact joint constants then give
\[
\boxed{m=ct+d,\quad c,d\in\mathbb C,\quad(c,d)\ne(0,0),
\qquad n_{ss}=c^2/2.}
\tag{9}
\]
Explicitly \(c=m_t\) and \(d=m-tm_t\) are killed by both coefficient
partials. No rational parametrization of L is assumed.

Define
\[
\eta=\frac{c k_t/2-n_s}{m}\in L.
\tag{10}
\]
The exact derivatives satisfy
\[
\eta_s=\frac{c^2/2-n_{ss}}m=0,\qquad
4m\eta_t=[PV]\Delta=0.
\tag{11}
\]
Thus \(\eta\in\mathbb C\). No division by c or p was used, so \(c=0\)
is still included. After(9), A1 has V-coefficient c, and its remaining
part evaluated at \(P=\sigma\) belongs to L. The unit
\(H_U^{\rm ev}=2y+A_1(\sigma,\theta)\) therefore gives
\[
\boxed{j:=y+c\theta/2\in L.}
\tag{12}
\]
The centered surface's transverse coefficient would consequently be
zero here. The actual derivation below avoids needing that extra
coefficient calculation.

## 4. The genuine auxiliary derivation and its complete actual row

Extend N from A to \(\mathcal B=A[u]\) by \(Nu=0\), and put
\[
\mathcal P=aN-(NX)E.
\tag{13}
\]
This is an actual polynomial derivation, and it fixes X. Moreover
\([E,N]=0\), \(Ea=0\), and \(E(NX)=N(EX)=Na=0\), so
\([E,\mathcal P]=0\). On \(\mathcal B_a=A_a[X]\), it kills X and
acts as aN on \(A_a\). Because \(Na=0\), it is locally nilpotent
there and hence on the stable subring \(\mathcal B\).

The literal first and second potentials and full map are
\[
\begin{aligned}
z&=2ty+\sigma^2+k_t\sigma+m\theta+n,\\
w&=-D_0y-\lambda_0\theta+w_0,\quad
D_0=(2\sigma+k_t)/m,\quad
\lambda_0=(c\sigma+n_s)/m,\quad w_0\in L,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\qquad W=w+\theta X+sX^2.
\end{aligned}
\tag{14}
\]
Set \(\tau=aN\theta\in L^*\). By(12), \(Ny=-cN\theta/2\), while N
kills sigma and every displayed coefficient in L. Applying(13) to
the whole actual map, including its X terms, gives
\[
\boxed{\mathcal PX=0,\quad \mathcal PY=-c\tau/2,\quad
\mathcal PZ=d\tau,\quad \mathcal PW=(X+\eta)\tau.}
\tag{15}
\]
The last entry uses \(cD_0/2-\lambda_0=\eta\). At least one of the
Y and Z entries is nonzero. Tau is not assumed to be an ambient unit
and is never inverted there. In particular Y is not called fixed
when \(c\ne0\).

## 5. Two actual reframes and the preserved three-ring

If \(c\ne0\), take
\[
U_0=Z+2dY/c,\qquad V_0=W+2(X+\eta)Y/c.
\tag{16}
\]
Then the actual frame and its inverse are
\[
\mathcal B=\mathbb C[X,U_0,V_0,Y],\qquad
Z=U_0-2dY/c,\quad W=V_0-2(X+\eta)Y/c.
\tag{17}
\]
Both compositions cancel term by term. Equation(15) gives
\(\mathcal PU_0=\mathcal PV_0=0\) and
\(\mathcal PY=-c\tau/2\ne0\).

If \(c=0\), then \(d\in\mathbb C^*\). Instead take
\[
U_0=Y,\qquad V_0=W-(X+\eta)Z/d,\qquad
\mathcal B=\mathbb C[X,U_0,V_0,Z].
\tag{18}
\]
Its inverse is \(Y=U_0\), \(W=V_0+(X+\eta)Z/d\), fixing X,Z.
Both compositions are polynomial over \(\mathbb C\).
Here \(\mathcal PU_0=\mathcal PV_0=0\) and
\(\mathcal PZ=d\tau\ne0\). This inverse contains no division by c.

In either case put \(S=\mathbb C[X,U_0,V_0]\), and let R denote the
remaining actual coordinate, Y in(17) or Z in(18). Then
\(\mathcal B=S[R]\), \(\mathcal P\) fixes S, and
\(\mathcal PR=q\ne0\). For \(b\in S[R]\),
\(\mathcal Pb=q\,\partial_Rb\). Since this is a characteristic-zero
domain,
\[
\boxed{\ker_{\mathcal B}\mathcal P=S=\mathbb C[X,U_0,V_0].}
\tag{19}
\]
This does not require q to be a unit or \(\mathcal P\) to have a slice.
Commutation with E gives \(E(S)\subset S\).

## 6. Primitive restriction, actual invariant coordinate, and global slice

The restriction \(E_0=E|_S\) is a nonzero locally nilpotent derivation,
because the actual coordinate X satisfies
\[
E_0X=a\ne0,\qquad E_0^2X=0.
\tag{20}
\]
In particular a now belongs to S. The restriction need not be
irreducible or admit a slice.

Let g be the gcd in S of its three coordinate coefficients. It is
nonzero and divides a. Since \(E_0a=0\), additivity of locally nilpotent
degree on \(a=g(a/g)\) gives \(E_0g=0\). Hence
\[
D=g^{-1}E_0:S\longrightarrow S
\text{ is irreducible and locally nilpotent},\qquad
DX\ne0,\quad D^2X=0.
\tag{21}
\]
Polynomiality follows from the gcd, and nilpotence follows from
\(D^nb=E_0^nb/g^n\). These values lie in S because D already preserves S.
The kernels of D and \(E_0\) agree.

Use Daigle's theorem as restated in
[Dasgupta--Gupta Theorem4.8](https://arxiv.org/html/1701.03635v1):
an irreducible LND on a polynomial three-ring over a characteristic-zero
field, with a genuine coordinate of nonzero first derivative and zero
second derivative, admits an invariant coordinate in that ring. The
statement retains the given degree-one coordinate in a coordinate
system. Applied to(21), it supplies Q,R1 in S such that
\[
S=\mathbb C[Q,X,R_1],\qquad DQ=0.
\tag{22}
\]
Then \(EQ=E_0Q=gDQ=0\). Since \(\mathcal B=S[R]\) is an actual
polynomial decomposition, Q extends to an actual coordinate of the
original four-ring, not just of its fraction field.

The global slice is used for the original E. It gives
\(A\simeq\mathcal B/(u)\), so A is affine. The equality \(Eu=1\)
makes the hypersurface \(u=0\) smooth: the coefficients of E pair with
the coordinate gradient of u to give 1. Thus A is regular.
The exact hypotheses of
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
now hold for the nonzero E on \(\mathbb C[Q,X,R_1,R]\), fixing Q,
with regular kernel. They give
\[
\boxed{A=\mathbb C[Q]^{[2]}\cong\mathbb C^{[3]}.}
\tag{23}
\]
No slice of \(\mathcal P,E_0\), or D was required or inferred.

## 7. Scope and verification boundary

The conclusion concerns only the actual reducible-surface branch with
\(\sigma_v=0,m_s=0\) and full input(1). Reducibility supplies the whole
projected return, so theta is affine nonconstant and the projected
equation is a line. Neither irreducible surfaces nor the remaining
\(m_s\ne0\) cases are addressed.

No normalization of arbitrary k or n was made. Coefficient-field
expressions were used to obtain the complex constants(9)--(11); the
actual reframes divide only by nonzero complex c or d. The original
a, tau, and primitive gcd are never declared ambient units. The
preserved-ring and primitive-restriction arguments are separate and
both are needed for the endpoint.

The complete actual264 source was freshly reread. The exact302 factor
return and296 gradient-unit input are retained working dependencies.
Both published endpoint statements were freshly read with their precise
irreducibility, coordinate, nonzero and regularity conditions.
Fresh unsaved symbolic expansion reconstructed(8), (11), the complete
actual row(15), and the displayed inverse maps. These checks supplement
the field and original-ring proof gates. No saved checker was executed,
imported, compiled or rerun, and no retained source was changed.
There is no actual-existence, unrestricted cancellation, historical
novelty, human-expert or proof-assistant certification claim.
