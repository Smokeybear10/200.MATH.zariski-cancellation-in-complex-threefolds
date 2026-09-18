# Polynomial specialization excludes the entire reciprocal conic sector

Working theorem: no genuine conic from the retained actual reducible
principal-chart sector can occur. This includes both d=0 and d nonzero
in the affine-selected reciprocal family306. The contradiction uses a
coefficient-adjoined polynomial ring and a legitimate evaluation map,
not descent of its coordinates to the original complex polynomial ring.

## 1. A two-variable polynomial-generation lemma

Let K be any field of characteristic zero, and let x,z be independent
polynomial variables. Suppose F,G,H belong to K[x,z] and satisfy
\[
K[x,F,G,H]=K[x,z].
\tag{1}
\]
Assume that their z-expansions have the form
\[
\begin{aligned}
F&=f_2z^2+(f_1+\lambda x)z+F_0(x),\\
G&=g_2z^2+(g_1+\mu x)z+G_0(x),\\
H&=h_3z^3+\text{terms of z-degree at most two},
\end{aligned}
\tag{2}
\]
where all f_i,g_i,lambda,mu,h_3 belong to K, while F_0,G_0 belong
to K[x]. Suppose
\[
g_2h_3\ne0,\qquad r:=g_2\lambda-f_2\mu\ne0.
\tag{3}
\]
These hypotheses are impossible. The coefficient f_2 may be zero.

Indeed g_2F-f_2G has z-degree at most one, with linear coefficient
\(r x+g_2f_1-f_2g_1\). Set
\[
x_0=-\frac{g_2f_1-f_2g_1}{r}\in K.
\tag{4}
\]
Evaluation at x=x_0 is a K-algebra homomorphism from K[x,z] onto K[z].
Consequently (1) gives K[F(x_0,z),G(x_0,z),H(x_0,z)]=K[z]. But the
evaluated g_2F-f_2G is constant, and g_2 is invertible. Hence
\[
K[G(x_0,z),H(x_0,z)]=K[z],
\qquad \deg_zG(x_0,z)=2,\quad \deg_zH(x_0,z)=3.
\tag{5}
\]
The leading coefficients remain nonzero because they lie in K and
are independent of x.

For completeness, a quadratic and a cubic cannot generate K[z].
Translate z to xi to eliminate the linear term of the quadratic,
then rescale and subtract its constant, giving the first generator
xi^2. Subtract a multiple of xi^2 and a constant from the cubic.
The second generator becomes xi(A xi^2+B), where A is nonzero.
Its square belongs to K[xi^2], so the generated ring is exactly
\[
K[\xi^2]\oplus\xi(A\xi^2+B)K[\xi^2].
\tag{6}
\]
It cannot contain xi: its odd coefficient would require the nonconstant
polynomial A xi^2+B to be invertible in K[xi^2]. This proves the lemma
without a classification theorem for polynomial embeddings.

## 2. Actual chart and coefficient-adjoined ring equality

Retain the full actual chart264, the reducible genuine-conic sector302,
and the affine selection and reciprocal coupling proved in
[306](principal-paraboloid-selected-conic-factor-rigidity-pass306-working.md).
The polynomial formulas are those displayed in
[315](principal-paraboloid-conic-polynomial-coefficient-return-pass315-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
a=EX\in L^*,\quad Ea=0,\\
K=\operatorname{Frac}A=L(\sigma),\qquad L[v]=L[\sigma],
\qquad X\text{ is transcendental over }K,\\
Y=y+\sigma X+tX^2,\\
Z=z+(2t\sigma+k)X+t^2X^2,\\
W=w+\theta X+sX^2,\qquad
y,z,w,\theta\in L[\sigma].
\end{gathered}
\tag{7}
\]
The full original E-profile is (1,2,2,2), its full initial relation
is X^2Z-Y^2, and the chosen nonzero intrinsic derivation N kills a,t,s.
These actual entry assumptions are not replaced by a formal ansatz.

All elements of L and sigma are killed by E. The displayed expansions
first give \(L[\mathcal B]\subseteq L[X,\sigma]\). Conversely the
actual derivative EY belongs to the original ring, and
\[
\sigma=\frac{EY}{a}-2tX\in L[\mathcal B].
\tag{8}
\]
Therefore
\[
\boxed{L[X,Y,Z,W]=L[\mathcal B]=L[X,\sigma].}
\tag{9}
\]
Every ring here is the specified subring of the original fraction field.
Equation (9) uses that E preserves the original ring and that a is a
nonzero element of L. It does not require a to be a unit of the original
ring, prove that L is rational, or invoke318's stronger equality over F.

In particular evaluation at X equal to any element of L is legitimate
in (9). This is not an original coordinate change or an evaluation of
coefficient functions in t or s. The coefficient field L is held fixed.

## 3. Complete leading coefficients of the actual generators

Write
\[
T=t-\tau,\qquad m=d+c/T,\qquad c,d,\tau\in\mathbb C,
\quad c\ne0,\qquad p=m_t,\qquad
\delta=\frac{m m_{tt}}{2p},\qquad b_V=(p-\delta)/2.
\tag{10}
\]
The coefficient t is transcendental over the complex numbers, so T,
c+dT and the expressions stated nonzero below are nonzero elements of L.
No finite coefficient value is being removed from the actual variety.

The selected conic has
\[
\theta=\frac{\eta+(2p/m)\sigma^2+\beta\sigma+\chi}{\delta},
\qquad y=-b_P\sigma-b_V\theta-b_0,
\tag{11}
\]
with all eta,beta,chi,b_P,b_0 in L. It is unnecessary here to prove
eta_s=0 or other lower-coefficient rigidity. The first and second
literal potentials give
\[
z=2ty+\sigma^2+k_t\sigma+m\theta+n,
\qquad
w=\frac{\ell-(2\sigma+k_t)y-F(\sigma,\theta)}m,
\tag{12}
\]
where
\(F(P,V)=k_{tt}P^2/2+pPV+n_tP+n_sV\).

Extracting coefficients before any evaluation in X gives
\[
\begin{aligned}
\theta_2&=\frac{2p}{m\delta}
             =\frac{2cT}{(c+dT)^2},\\
y_2:=[\sigma^2]Y&=-b_V\theta_2
             =-\frac{dc}{(c+dT)^2},\\
z_2:=[\sigma^2]Z&=2t y_2+1+m\theta_2
             =1-\frac{2tdc}{(c+dT)^2}+\frac{2c}{c+dT},\\
w_3:=[\sigma^3]W&=-\frac{2y_2+p\theta_2}{m}
             =\frac{2c}{(c+dT)^2}.
\end{aligned}
\tag{13}
\]
The cubic formula retains both contributions from y and F in (12).
The X-dependent terms in (7) do not change these coefficients.
In particular w_3 is nonzero. Also z_2 is nonzero: it equals 3 if d=0;
otherwise its numerator, after multiplying by (c+dT)^2 and replacing
t with T+tau, has leading term d^2T^2.

Write y=y_2 sigma^2+y_1 sigma+y_0 and
z=z_2 sigma^2+z_1 sigma+z_0, with all these coefficients in L.
The linear sigma coefficients of the actual Y,Z are respectively
y_1+X and z_1+2tX. Thus the last nonvanishing condition for the lemma is
\[
r=z_2-2t y_2=1+\frac{2c}{c+dT}
              =\frac{3c+dT}{c+dT}\ne0.
\tag{14}
\]
For d=0 this equals 3. For d nonzero its numerator is a nonconstant
complex linear polynomial in the transcendental T.

## 4. Apply the generation lemma, without original-coordinate descent

Use Section1 with coefficient field L, x=X, its z-variable equal to
sigma, and (F,G,H)=(Y,Z,W). The field is characteristic zero,
(9) is the full required polynomial-ring generation, and (13),(14)
verify all nonvanishing and degree conditions, including d=0.

Equivalently, put
\[
X_0=-\frac{z_2y_1-y_2z_1}{z_2-2ty_2}\in L.
\tag{15}
\]
At X=X_0, z_2Y-y_2Z becomes constant in sigma. The specialized Z
and W still have degrees exactly two and three. Equation (9) says
they must generate L[sigma], contradicting (6).

Hence the entire actual genuine-conic sector is impossible. The proof
does not divide by d or y_2, does not require sigma to be an original
polynomial coordinate, and does not differentiate the moving X_0.

## 5. Scope and verification boundary

This excludes the conic remaining after306 and315, including the sector
excluded separately by320. The earlier scalar and generic-plane results
316 and318 remain valid conditional consequences, but are not needed
to establish the stronger contradiction here. The proof also does not
use319's rank-two-action theorem or a field-relative triangularization.

The input remains the specified actual principal chart and the previously
proved reducible-conic classification. Arbitrary-coordinate entry and
irreducible surfaces are outside this argument. No unrestricted
cancellation theorem, original-coordinate descent, historical novelty,
human expert certification or formal proof-assistant result is claimed.
