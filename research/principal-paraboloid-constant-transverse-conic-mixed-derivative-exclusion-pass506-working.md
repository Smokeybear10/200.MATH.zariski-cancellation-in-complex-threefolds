# Mixed derivatives exclude the constant transverse conic family

Working exclusion: under the FULL actual264/296/327 transverse-conic
hypotheses of498 and500, with affine nonconstant sigma, quadratic
theta, quadratic \(S=\sigma^2+k_t\sigma+m\theta\), and \(m_s\ne0\),
the coefficient \(\gamma=m_s/m^3\) cannot belong to \(\mathbb C^*\).

The proof uses504's licensed actual normal form, then only three
positive-degree coefficients of the ENTIRE scalar. They require
incompatible mixed coefficient derivatives. This excludes the whole
constant-gamma alternative, not just a further polynomial ansatz.
It does not exclude500's inverse-square alternative, the \(m_s=0\)
sector, the degree-drop boundary, or arbitrary cancellation data.

## 1. Full retained input and the exact coefficient basis

Retain every assumption of
[504](principal-paraboloid-constant-transverse-conic-cubic-time-normal-form-pass504-working.md),
including its complete actual264/296/327/498/500/501 inputs.
In particular the ACTUAL ring and global slice are
\[
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0.
\tag{1}
\]
The entire initial kernel, exact E-profile(1,2,2,2), literal selected
nonzero N, both actual returns and genuine moving H,Q levels remain
required. Put \(L=\operatorname{Frac}\ker_A N\), finite over C(t,s),
and use the intrinsic parameter \(P=\sigma\), with \(NP=\rho\in L^*\).
The original calibration is
\[
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{2}
\]
All coefficient derivatives are exact and commute, with joint constants C.

504 provides actual complex polynomial maps with complete inverses,
so that without changing the validity of these assumptions,
\[
\begin{gathered}
m^{-2}=\beta t^3/6-2s,\quad k=-1/m,\quad m_s=m^3,\quad
\beta\in\mathbb C^*,\\
d=ma,\quad d\ne0,\quad d+1\ne0,\quad
d_s=m^3\kappa\ne0,\quad\kappa\in L^*,\\
y=-\beta/(24d),\qquad
\theta=\frac d mP^2+\frac{\beta t^2}{4}P+c,\qquad
n=Dm,\quad D=D_1t+D_0,\quad D_0,D_1\in\mathbb C.
\end{gathered}
\tag{3}
\]
Its beta-zero boundary was excluded by an actual saturated fiber,
not discarded by division. No restriction on c or the remaining
lower potential ell is added here.

Because \(d_s\ne0\), (t,d) is a separating coefficient basis.
The exact operators are
\[
\partial_d|_t=d_s^{-1}\partial_s,\qquad
\partial_t|_d=\partial_t|_s-\frac{d_t|_s}{d_s}\partial_s.
\tag{4}
\]
They commute. Subscripts t,d henceforth mean THESE operators.
They extend to fix formal P and actual X. The full scalar becomes
\[
\mathcal J=\det\frac{\partial(Y,Z,W)}{\partial(t,d,P)}
=-\frac{a_0^4}{\rho d_s}
=-\frac{a_0^4}{\rho\kappa m^3}\in L^*.
\tag{5}
\]
It has no X or P dependence. Its value is not assumed complex or
constant in the coefficient directions.

## 2. Complete literal rows, with every lower function retained

Define EXISTING coefficient-field elements
\[
u=1/m,\qquad q=m(c+D),\qquad
F=u\ell-\frac{\beta^2t^2}{96d}-\frac{q^2}{2}
                                      +\frac{D^2}{2u^2}.
\tag{6}
\]
The symbol F here is a coefficient function, not the formal
second-potential polynomial used in264. It is the intrinsic
constant term of \(w_{\rm int}\), equivalently the X-constant,
P-constant coefficient of W. These definitions make no ambient
coordinate assertion; in particular q need not be nonzero.

The COMPLETE original rows in the normalized actual frame are
\[
\begin{aligned}
Y={}&XP-\frac{\beta}{24d}+tX^2,\\
Z={}&(d+1)P^2+2tXP-\frac{\beta t}{12d}
                                 +q-uX+t^2X^2,\\
W={}&-\frac{d^2}{2}P^4+
       \left(\frac{\beta t}{4}-dq+duX\right)P^2\\
 &+\left(-D_1+\frac{\beta u}{12d}
                             +\frac{\beta t^2X}{4}\right)P
       +F+(qu-D)X+\left(\frac{\beta t^3}{12}-\frac{u^2}{2}\right)X^2 .
\end{aligned}
\tag{7}
\]
There is no cubic-P term. To reconstruct the constant row, use
\(c=qu-D\), \(s=\beta t^3/12-u^2/2\), \(n_s=Dm^3\) and
\(k_t|_s=-\beta t^2m/4\) in the full second potential
\[
mw_{\rm int}=\ell-(2P+k_t)y-
 \left(k_{tt}P^2/2+m_tP\theta+m_s\theta^2/2+n_tP+n_s\theta\right).
\tag{8}
\]
At P=0 it gives precisely (6), including the term
\(-\beta^2t^2/(96d)\). The positive-P terms are the full
coefficients504(19) after its final actual reframe.
Thus no c,ell, lower intercept or its moving derivative was frozen.

## 3. Three exact scalar coefficients

Let \(J_{ij}=[X^iP^j]\mathcal J\). Each coefficient with
\((i,j)\ne(0,0)\) vanishes by (5). Direct expansion of the ENTIRE
three-row determinant (7), keeping arbitrary first derivatives
of u,q,F, gives
\[
\begin{aligned}
J_{03}&=\frac{\beta}{144d^2}
                   (2\beta d+3\beta-12d q_t),\\
J_{21}&=-\frac{96d^2F_d-\beta^2t^2+96d^2q q_d}{48d},\\
J_{12}&=-\frac{24dF_t-\beta^2t+4\beta d q_d-6\beta q+24dq q_t}{24d}.
\end{aligned}
\tag{9}
\]
All u terms, their first derivatives and the complex constants
D0,D1 cancel from these three coefficients. No equation on those
terms has been imposed to obtain (9).

Since beta,d are nonzero, \(J_{03}=0\) gives
\[
q_t=\frac{\beta}{6}+\frac{\beta}{4d}.
\tag{10}
\]
Put the EXISTING element \(G=F+q^2/2\in L\).
The other two vanishing coefficients give exactly
\[
G_d=\frac{\beta^2t^2}{96d^2},\qquad
G_t=\frac{\beta^2t}{24d}-\frac{\beta q_d}{6}
                                      +\frac{\beta q}{4d}.
\tag{11}
\]
No integration, rationality assumption, or division by q,u,F or
their derivatives is used.

## 4. Exact commutation is impossible

The two coefficient derivatives in (4) commute. Differentiating
(10) in d yields \(q_{dt}=-\beta/(4d^2)\). Differentiate the
second identity in (11) in t at fixed d:
\[
\begin{aligned}
G_{tt}
 &=\frac{\beta^2}{24d}
       -\frac{\beta}{6}\left(-\frac{\beta}{4d^2}\right)
       +\frac{\beta}{4d}\left(\frac{\beta}{6}+\frac{\beta}{4d}\right)\\
 &=\frac{\beta^2}{12d}+\frac{5\beta^2}{48d^2}.
\end{aligned}
\tag{12}
\]
On the other hand, the first identity in (11) gives
\((G_d)_{tt}=\beta^2/(48d^2)\). Therefore the COMPLETE mixed
derivative difference is
\[
0=(G_{tt})_d-(G_d)_{tt}
 =-\frac{5\beta^2(d+2)}{48d^3}.
\tag{13}
\]
Characteristic zero and beta,d nonzero force d=-2. This contradicts
\(d_s=m^3\kappa\ne0\), or simply the fact that d is a member of
the separating basis with \(\partial_d d=1\).

This argument differentiates identities obtained from coefficients
already known to vanish. It never differentiates the unknown
coefficient-field value of the calibrated scalar and sets that
derivative to zero. No zero derivative of u, q or F is assumed.

Every normalized family504 is impossible. Since its normalization
was by genuine complex polynomial automorphisms with both returns
and the nonzero scalar retained, the original full constant-gamma
sector is impossible as well. In combination with
[500](principal-paraboloid-transverse-conic-initial-rigidity-pass500-working.md),
every surviving transverse conic must consequently have
\(\gamma=C/(t-\tau)^2\), with C nonzero complex and tau complex.

## 5. Independent verification and exact boundary

Root fresh788089 builds all three full rows (7) with independent
u_t,u_d,q_t,q_d,F_t,F_d and expands the complete determinant.
It gives all three coefficients (9). Fresh109655 verifies the
whole compatibility difference (13), including its sign and factor.

General fully read held504 through EOF42639d+1d9cab at
SHA13192b25ad19a55cbf714e007d64d9d2d44dcae8e511f728431f22efea46dff6.
Its independent fresh ed93f0 reconstructs every row from the
literal first and second potentials, including the definition (6),
and separately checks the three ungated determinant coefficients.
Fresh c815dc independently verifies (11),(12) and the entire
mixed difference (13). All corresponding residuals are zero.
A complete saved-source review is recorded separately in the ledger.

The conclusion excludes the constant-gamma alternative only under
the FULL actual affine-sigma, quadratic-theta, quadratic-S,
nonzero-transverse-coupling hypotheses. It does not provide arbitrary
chart entry, an inverse-square-branch exclusion, a result for the
delta-zero boundary, or general cancellation. No historical novelty,
human expert review or proof-assistant certification is claimed.
All saved checkers remain frozen; none was executed, imported,
compiled or rerun. No earlier mathematical source was edited.
