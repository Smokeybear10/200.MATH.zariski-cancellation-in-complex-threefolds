# A stronger cofactor bound and an actual swap for the mixed quadratic graph

Status: working necessary reduction for a supplied actual frame. The
quadratic projected graph is not excluded or recognized here. The result
does not put arbitrary cancellation instances into these hypotheses.

## 1. Actual hypotheses and the remaining graph

Use the complete actual setup of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
with
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(ZW-X^2Y^2).
\tag{1}
\]
The initial kernel is the entire weighted evaluation ideal, not just a
vanishing leading equation. Use the literal pivot \(\partial_Z\) and its
selected actual derivation \(N\). Write
\[
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\quad
h=t/\rho,\quad q=t^2/\rho,\quad
\xi=y-h\vartheta .
\tag{2}
\]
The field \(L\) is finite over \(\mathbb C(t,\rho)\), the two partials
extend uniquely, and \(t,\rho\) are algebraically independent. Coefficients
below belong to this exact field, not necessarily its rational subfield.
The expression \(\xi\) is a polynomial in \(v\), not asserted to be an
ambient polynomial coordinate.

Assume the remaining quadratic-graph branch:
\[
\deg_v\xi=1,\qquad
\vartheta=P(\xi),\qquad
P(T)=\alpha T^2+\alpha_1T+\alpha_0,\quad\alpha\in L^* .
\tag{3}
\]
Thus \(O=L[v]=L[\xi]\) and \(y=\xi+hP(\xi)\). The return polynomial is
\[
\mathcal R(T)=-\frac{2h}{\rho}T+k_\rho,\qquad
R=\mathcal R(\xi)\ne0,\qquad \deg_vR=1 .
\tag{4}
\]
The complete nonzero-return projection reduction in
[mixed projection217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
supplies either a plane line or (3). This note only studies (3).

## 2. The evaluated cofactor divides the square of the return polynomial

In the original formal variables \(U,V\), put
\[
S=g_3-\ell,\quad T_0=-S,\quad
C_0=f_\rho,\quad Q_0=g_4-\ell_tU-\ell_\rho V-m,\qquad
\mathcal H=\frac{h^2}{\rho}S^2-f_VC_0S+f_V^2Q_0 .
\tag{5}
\]
These are the literal universal potentials, including all coefficient
derivatives before evaluation. Let
\(\widetilde{\mathcal H}(T,V)=\mathcal H(T+hV,V)\).
Its selected irreducible factor is \(V-P(T)\). Write
\[
q_1=\widetilde{\mathcal H}_V(\xi,P(\xi)).
\tag{6}
\]
The full calibrated determinant and both potentials give the universal
identities below. Subscripts on \(y,\vartheta,w\) are total partials at
fixed \(v\), and \(J_0=-a^3\in L^*\):
\[
\begin{gathered}
R^3J_0=D_U\mathcal H_U(y,\vartheta)
             +D_V\mathcal H_V(y,\vartheta),\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v,\\
B_1y_v+C_1\vartheta_v+Rw_v=0 .
\end{gathered}
\tag{7}
\]
Here \(B_1=f_t(y,\vartheta)+q_{t\rho}w\) and
\(C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w\).
In particular the \(q_{t\rho}w\) term has not been dropped.
Equation (7), reconstructed in mixed projection217, implies that the
selected factor is simple and \(q_1\ne0\).

Put \(p=P'(\xi)\). The kernel gradient and its chain rule give
\[
\mathcal H_U(y,\vartheta)=-p q_1,\qquad
\mathcal H_V(y,\vartheta)=(1+hp)q_1,\qquad
y_v=(1+hp)\xi_v,\quad \vartheta_v=p\xi_v .
\tag{8}
\]
As \(\xi_v\in L^*\), the last identity in (7) says
\(B_1(1+hp)+C_1p=-Rw_v/\xi_v\).
Consequently the coefficient multiplying \(q_1\) in (7) has an
additional factor \(R\):
\[
\begin{gathered}
-pD_U+(1+hp)D_V=R K_0,\\
K_0=-p(y_v\vartheta_\rho-y_\rho\vartheta_v)
 +(1+hp)(y_t\vartheta_v-y_v\vartheta_t)
 +(1+hp)w_v,\\
R^2J_0=K_0q_1,\qquad
0\ne q_1\mid R^2,\qquad \deg_vq_1\le2 .
\end{gathered}
\tag{9}
\]
Everything in this identity lies in \(L[v]\). It neither differentiates
the field-dependent change as though \(h\) were constant over
\(\mathbb C\), nor requires \(h\) or \(\xi_v\) to be regular in \(B\).

## 3. The two possible radial leading branches

Define the derivation \(\mathcal D=h\partial_t+\partial_\rho\) on \(L\).
It satisfies \(\mathcal D h=0\) and \(\mathcal D\rho=1\). Let
\[
K=\mathcal D^2k/2,\qquad D_3=\mathcal D^3k .
\tag{10}
\]
Because \(\mathcal D h=0\), powers of \(\mathcal D\) give the ordinary
binomial coefficient combinations of the two commuting partials.
For example \(\mathcal D^2k=h^2k_{tt}+2hk_{t\rho}+k_{\rho\rho}\).

Assign weights \(1,2\) to \(T,V\). The transformed polynomials in (5)
have the following maximal weighted parts:
\[
\begin{aligned}
S_{[4]}&=K V^2-\rho^{-2}T^2V,&
(f_V)_{[1]}&=-2hT/\rho,\\
(C_0)_{[3]}&=2hTV/\rho^2,&
(Q_0)_{[6]}&=T^2V^2/\rho^3+(D_3/6)V^3 .
\end{aligned}
\tag{11}
\]
No omitted term has larger weight. One can check this directly from
\(H_2(q)=T^2/\rho\), \(H_3(q)=-VT^2/\rho^2\), and
\(H_4(q)=V^2T^2/\rho^3\), after substituting \(U=T+hV\).
The coefficient derivatives defining \(C_0\) are still taken at fixed
original \(U,V\), before this substitution.
Thus the complete weight-eight part is
\[
\widetilde{\mathcal H}_{[8]}
=\frac{h^2}{\rho}V^2
 \left\{K^2V^2+
 \left(\frac{2K}{\rho^2}+\frac{2D_3}{3\rho}\right)T^2V
 +\frac{T^4}{\rho^4}\right\}.
\tag{12}
\]

Set \(B_0=2K/\rho^2+2D_3/(3\rho)\).
The coefficient of \(\xi^8\) in
\(\widetilde{\mathcal H}(\xi,P(\xi))=0\), and that of \(\xi^6\)
in (6), using (9), imply respectively
\[
K^2\alpha^2+B_0\alpha+\rho^{-4}=0,\qquad
2K^2\alpha+B_0=0 .
\tag{13}
\]
For the second equality, differentiating (12) and then using the first
equality removes its multiple of the vanishing quadratic factor.
Every lower-weight term gives a strictly lower degree, so neither
coefficient comparison has an unexamined cancellation.
If \(K=0\), the two equalities are inconsistent. Otherwise they give
\[
\begin{array}{c|c|c}
 &D_3&\alpha\\ \hline
\mathrm{I}&0&-1/(K\rho^2)\\
\mathrm{II}&-6K/\rho&1/(K\rho^2).
\end{array}
\tag{14}
\]
This is a necessary two-case reduction, not a classification of all
solutions of the lower potentials. It does not assert that the
\(\mathcal D\)-constant field is \(\mathbb C\).

## 4. An actual good-coordinate swap removes cubic projected intercepts

Since \(Rw=-S(\xi+hP(\xi),P(\xi))\), the third potential and
(11)--(14) show
\[
\begin{array}{c|c}
\mathrm{I}&
w=(K h\rho^3)^{-1}\xi^3+\text{terms of degree at most two}\\
\mathrm{II}&\deg_vw\le2 .
\end{array}
\tag{15}
\]
In case II the degree-four numerator cancels; in case I its coefficient
is \(2/(K\rho^4)\), and division by the leading coefficient
\(-2h/\rho\) of \(R\), with the minus sign in \(Rw=-S\), gives (15).
The second potential is exactly
\[
z=-h^2w+\xi^2/\rho+k_t\xi+(hk_t+k_\rho)\vartheta+n .
\tag{16}
\]
It follows that \(z\) also has degree at most two in case II.

In case I perform the actual polynomial automorphism
\[
X'=Y,\quad Y'=X,\quad Z'=Z,\quad W'=W ,
\tag{17}
\]
whose inverse is the same interchange. This preserves exact time
degrees and the full initial ideal \(ZW-X^2Y^2\). It also preserves
the literal pivot \(\partial_Z\), hence its selected \(N\) and \(L\).
The original slice \(u\) is unchanged; no field-dependent ambient
linear combination is made.

The new ratios and intercepts, obtained by solving
\(X=(X'-y)/t\), satisfy
\[
\begin{gathered}
t'=1/t,\quad \rho'=\rho/t^2,\quad q'=q/t^2=t'^2/\rho',
\quad h'=t'/\rho'=h,\\
y'=-y/t,\qquad
\vartheta'=-\vartheta/t-2\xi/(ht),\qquad \xi'=\xi/t,\\
w'=w+\xi\vartheta/t+\rho\xi^2/t^2,\\
z'=-h^2w'+\xi^2/\rho+(k_t-k/t)\xi
             +(hk_t+k_\rho-k/\rho)\vartheta+n .
\end{gathered}
\tag{18}
\]
The cubic coefficient of \(w'\) is
\((K h\rho^3)^{-1}+\alpha/t=0\) in case I.
Thus \(y',z',w'\) all have degree at most two in the unchanged \(v\).
The second projection remains quadratic and \(\xi'\) remains affine.
The new third-potential coefficient \(k'\) and the new return coefficient
are not claimed to equal the old ones.

Under either the identity in case II or (17) in case I, therefore,
the actual selected chart has all three projected intercepts of
degree at most two. The corresponding actual commuting auxiliary
derivation \(\mathcal P=aN-(NX)E\), rebuilt using the chosen first
coordinate, satisfies
\[
\mathcal P X=0,\qquad
\mathcal P^3Y=\mathcal P^3Z=\mathcal P^3W=0 .
\tag{19}
\]
Here \(N\) extends to \(B=A[u]\) by \(Nu=0\).
Its commutation with \(E\), invariance of \(a\), and triangular action
on \(u\) make the displayed \(\mathcal P\) an actual polynomial LND.
On the localized chart it is \(a\partial_v\) at fixed \(X\).
The first potential \(\sigma=2hy-h^2\vartheta+k\) also has degree
at most two in the chosen chart. Together with the intercept bounds
and the quadratic second projection, this proves the iterate bound
for the actual coordinates, including their coefficients of \(X\).
The bound (19) is not the square-zero hypothesis of the nice-derivation
theorem. It provides no ambient invariant coordinate or cancellation
recognition by itself.

## 5. Verification boundary

The complete universal184 source was freshly read before this derivation.
The full-q gradient and cofactor identities are supplied by the separate
mixed projection217 proof and reconstructed in (7)--(9) for this graph.
Fresh inline algebra6cb46c checked the displayed weight-eight polynomial,
its graph derivative and both scalar branches. That computation is
not a proof of the actual-chart, field, factor-simplicity or LND claims.
No saved checker has been run in authoring this note. Peer review and
any later canonical finite suite are separate evidence.

The plane-line branch, the zero-return branch, the lower-potential
conditions after (19), arbitrary coordinate entry and unrestricted
cancellation are outside this note's conclusion. No historical novelty,
human review, formal verification, public posting or submission is claimed.
