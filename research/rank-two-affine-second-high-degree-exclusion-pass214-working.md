# An affine second projection excludes higher first degrees in the rank-two chart

Status: bounded working exclusion. Under the actual rank-two exact1122
hypotheses, a linear center with affine second projection has first
projected degree two. The alternatives three and four are impossible.
The proof sharpens the evaluated-cofactor bound using the scalar
determinant, then uses coefficients in the unmodified actual chart.
It does not recognize the remaining original ring or solve unrestricted
complex-threefold cancellation.

## 1. Actual inputs and the affine parameter

Retain the full actual hypotheses of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md)
and the monic specialization in
[center pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\qquad
F=\mathbb C(t,\rho)\subset L,\quad [L:F]<\infty,\quad q=1/\rho,\\
O=L[v],\quad Nv=1,\quad L[y,\vartheta,w]=O,\quad
J_0=-a^3\in L^*,\quad a=EX,\\
\mathcal H=GQ_1,\quad \mathcal H(y,\vartheta)=0,\quad
\mathcal H_6=-\rho^{-11}V^6,\quad \deg\mathcal H=6 .
\end{gathered}
\tag{1}
\]
The four original generators are polynomial coordinates and the
displayed initial ideal is the entire kernel. The coefficient field,
potentials, and scalar determinant come from the actual selected
partial, not from a freely chosen polynomial parametrization.
All coefficient derivatives refer to the commuting extensions of
the partials on the algebraically independent \(t,\rho\).

Assume \(\deg_v\vartheta=1\). Then \(\vartheta=a_1v+a_0\) with
\(a_1\in L^*\), and \(O=L[\vartheta]\). Write
\[
y=P(\vartheta),\quad w=W(\vartheta),\qquad P,W\in L[V],
\qquad G(U,V)=U-P(V).
\tag{2}
\]
This is a change of parameter in a polynomial ring over \(L\),
not an ambient coordinate change over \(\mathbb C\).
Use \(t,\rho,V=\vartheta\) as differential variables in this chart.
The calibrated determinant becomes \(J=J_0/a_1\in L^*\), since
\(dt\wedge d\rho\wedge d\vartheta=a_1\,dt\wedge d\rho\wedge dv\).
Partial derivatives of \(P,W\) below keep the independent \(V\)
fixed. This convention includes their coefficient dependence.

## 2. The strengthened evaluated-cofactor bound

Use \(R=2\rho^{-3}V+k_\rho\in L[V]\), which is nonconstant.
Retain the evaluated quantities \(B_1,C_1,\Lambda_t,\Lambda_\rho\)
from212. They are defined by both full polynomial potentials, not
only by the eliminant. The first of these potentials has total
V-derivative
\[
R W'+B_1P'+C_1=0 .
\tag{3}
\]
Here primes mean ordinary derivatives in \(V\).
Put \(q_1(V)=Q_1(P(V),V)\ne0\). The simple-factor result in212
ensures this is nonzero. Since \(G_U=1\) and \(G_V=-P'\), one has
\(\mathcal H_U(P,V)=q_1\) and
\(\mathcal H_V(P,V)=-P'q_1\).
The determinant identity212, in the present coordinates, reads
\[
\begin{gathered}
R^3J=(D_U-P'D_V)q_1,\qquad
D_U=-R P_\rho+C_1P',\qquad D_V=R P_t-B_1P',\\
D_U-P'D_V=-R(P_\rho+P'P_t)+P'(C_1+B_1P')
              =-R(P_\rho+P'P_t+P'W'),\\
R^2J=-(P_\rho+P'P_t+P'W')q_1 .
\end{gathered}
\tag{4}
\]
The last line cancels only the nonzero polynomial \(R\) in a domain.
It does not invert \(R\) in \(O\). As \(J\in L^*\), this proves
\[
0\ne q_1\mid R^2\quad\hbox{in }L[V],\qquad \deg_Vq_1\le2 .
\tag{5}
\]
This improvement uses the fact that \(\vartheta_v\) is a field
unit. It has not been extended to a nonlinear second projection.
The gradients used in (4) require both exact potentials of212;
imposing only (3) on arbitrary polynomials is insufficient.

## 3. The exact linear-center coefficients

Now assume the center is linear:
\[
\begin{gathered}
V_c=-\rho^3 k_\rho/2,\qquad
p(U)=S(U,V_c)-\ell=b(U-U_0),\quad b\in L^*,\\
j=k_\rho,\quad K=k_{t\rho},\quad N_0=n_t,\qquad
b=N_0-\rho^3jK/2,\qquad
\delta=2n_{tt}-\rho^3K^2 .
\end{gathered}
\tag{6}
\]
Its U-quadratic coefficient forces \(k_{tt}=0\).
The full potentials in212 therefore give
\[
\mathcal H=A(V)U^2+D(V)U+C(V),\qquad
A(V)=\rho^{-3}b^2+\frac{\delta}{4}R^2,\qquad
\deg D\le4,\quad \deg C=6,\quad [V^6]C=-\rho^{-11}.
\tag{7}
\]
For explicit coefficient bookkeeping, set
\(\phi=-\rho^{-4}V^3+k_{\rho\rho}V^2/2+n_\rho V\) and
\(c_*=-3\rho^{-4}V^2+k_{\rho\rho}V+n_\rho\).
Direct U-linear extraction gives
\[
D=-2\rho^{-3}b(\ell-\phi)-R c_*(KV+N_0)
       +R^2\left(\frac{K_\rho}{2}V^2+n_{t\rho}V-\ell_t\right).
\tag{8}
\]
In particular, if \(D_i=[V^i]D\), then
\[
D_4=2\rho^{-7}(3K+\rho K_\rho),\qquad
D_3=4\rho^{-7}(b+\rho b_\rho)+2\rho^3jD_4 .
\tag{9}
\]
Here the second formula is in the unshifted actual chart. To check
the coefficient dependence explicitly, differentiation of (6) gives
\[
b_\rho=n_{t\rho}-\frac32\rho^2jK
                   -\frac12\rho^3k_{\rho\rho}K
                   -\frac12\rho^3jK_\rho .
\tag{10}
\]
Substituting (10) into the second formula in (9) reproduces the
V-cubic coefficient of (8). Thus when \(D_4=0\), the cubic
coefficient already has the desired center-slope form, without
normalizing \(k_t\) or making any coordinate change.

## 4. Excluding first degrees four and three

The necessary list213 leaves \(d=\deg P=2,3,4\). Suppose \(d\ge3\).
By (2) and (7),
\[
q_1=2AP+D,\qquad \deg q_1\le2 .
\tag{11}
\]
If \(\delta\ne0\), then \(\deg A=2\), so \(2AP\) has degree
\(d+2\ge5\), larger than \(\deg D\). This contradicts (11).
Consequently \(\delta=0\) and \(A=\rho^{-3}b^2\in L^*\).
Eliminating \(D=q_1-2AP\) from \(\mathcal H(P,V)=0\) yields
\[
C=AP^2-q_1P .
\tag{12}
\]
If \(d=4\), the first term has degree eight and the second at most
six, contradicting \(\deg C=6\).

It remains to exclude \(d=3\). Equation (11) gives \(D_4=0\).
Write \(p_3=[V^3]P\ne0\). Equations (11) and (12) then give
\[
D_3=-2Ap_3,\qquad [V^6]C=Ap_3^2,\qquad
D_3^2=4A[V^6]C .
\tag{13}
\]
Using (7) and (9), this becomes
\[
4(b+\rho b_\rho)^2+b^2=0,\qquad
\frac{\rho b_\rho}{b}=\lambda\in\{-1+i/2,-1-i/2\}.
\tag{14}
\]
Both alternatives are constants in \(\mathbb C\): the product of
their two distinct linear factors vanishes in the field \(L\).
No variable sign or analytic branch choice is involved.

For completeness, the finite-field obstruction is elementary.
Let \(n_0=[L:F]\) and \(M=\operatorname{Norm}_{L/F}(b)\in F^*\).
Every conjugate satisfies the same differential equation, because
extensions of the derivation through separable algebraic fields are
unique. Differentiating their product gives
\[
\frac{M_\rho}{M}=\frac{n_0\lambda}{\rho}.
\tag{15}
\]
Regard \(M\) as a rational function in \(\rho\) over \(\mathbb C(t)\).
Write \(M=\rho^jP_0/Q_0\) at zero with \(j\in\mathbb Z\) and
\(P_0,Q_0\) nonzero at zero. The coefficient of \(\rho^{-1}\)
in \(M_\rho/M\) is \(j\), an integer. Equation (15) would make it
\(n_0\lambda\), which has a nonzero imaginary part. This is
impossible. No rationality of \(L\) or descent of \(b\) to
\(\mathbb C(\rho)\) was assumed.

## 5. Remaining scope

For a linear center and affine second projection, only \((d,e)=(2,1)\)
remains. Combined with the separate
[quadratic-second exclusion214](rank-two-linear-center-quadratic-projection-exclusion-pass214-working.md),
this leaves the same single degree pair for every linear center.
The other214 proof excludes
[\((6,4)\) for the quadratic center](rank-two-quadratic-center-six-four-exclusion-pass214-working.md);
that center still has the two pairs \((2,1),(3,2)\).
No pair in these remaining lists is asserted to be realizable or
recognized.

The proof retains the scalar determinant only where it is actually
used, in the improvement (5). Its coefficient comparison is direct
in the original chart. It supplies no invariant coordinate, general
coordinate-entry theorem, or proof of unrestricted cancellation.
The complete212 and213 sources and both companion214 proofs were
read before writing. New inline arithmetic checked the coefficients
in (7) and (9); a direct determinant expansion also exposed the need
for both full potential identities in (4), as explicitly retained.
Those calculations are supporting identities, not universal
verification of the written proof. No earlier frozen file or saved
checker was modified or rerun.
