# The quadratic volume coefficient gives exact descent off the velocity divisor

In the actual nonconical three-good-coordinate setting, the original
volume identity eliminates the third relative generator after
inverting the velocity determinant. The conclusion is
\(A_\Omega=R_\Omega\), not merely equality of fraction fields or
finite normalization. It is a controlled open-set equality of actual
subalgebras, not recognition of the global kernel as a polynomial ring.

## 1. Actual centered reconstruction

Retain the complete hypotheses of
[invariant-plane88](constant-acceleration-invariant-plane-pass88.md)
and the exact normal relation of
[volume-descent88](constant-acceleration-volume-descent-pass88.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,\qquad
Eu=1,\quad Ex_{\rm tr}=b\in S^3,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\ker(W|A)=\mathbb C[s_1,s_2],\qquad Wu=0,\qquad
a=x_{\rm tr}-bu\in A^3,\quad r=z-\frac q2u^2\in A,\\
L=b_{s_1}\times b_{s_2},\qquad
\Omega=L\cdot b\ne0,\qquad L\cdot a=\kappa\in S.
\end{gathered}
\tag{1}
\]
Both derivations are actual LNDs. All four coordinates of \(B\)
are original polynomial coordinates. The nonzero \(\Omega\) implies
that the two derivatives of \(b\) have rank two.

The actual \(u\)-slice projection sends the original generators
to \(a_1,a_2,a_3,r\), fixes \(S\), and has image \(A\).
It follows that \(A=S[a_1,a_2,a_3,r]\). No ambient automorphism
is inferred from the matrix used next.

Write \(\mathcal C=[b,b_{s_1},b_{s_2}]\). Over \(S_\Omega\)
this matrix is invertible, and the first row of its inverse is
\(L/\Omega\). Thus there are actual elements \(y_1,y_2\in A_\Omega\)
such that
\[
\rho=\frac{\kappa}{\Omega}\in S_\Omega,\qquad
a=\rho b+y_1b_{s_1}+y_2b_{s_2},\qquad
A_\Omega=S_\Omega[y_1,y_2,r].
\tag{2}
\]
The last equality follows in both directions from the invertible
matrix over the already embedded \(S_\Omega\).

## 2. The exact quadratic coefficient of the original volume

Choose an intrinsic local slice only to compute derivatives:
after inverting a nonzero \(g\in S\), write
\(A_{\Omega g}=S_{\Omega g}[v]\), with \(Wv=1\).
All partial derivatives below refer to these actual localized
variables. The original coordinate differential basis gives
\[
\mathcal J=
\det\begin{pmatrix}
b&u b_{s_1}+a_{s_1}&u b_{s_2}+a_{s_2}&a_v\\
qu&r_{s_1}&r_{s_2}&r_v
\end{pmatrix}
\in B_{\Omega g}^*=S_{\Omega g}^*.
\tag{3}
\]
In particular every positive coefficient in \(u\) vanishes.
This is the actual original-coordinate determinant. Its unit
property is not inferred from a formal Jacobian or a matrix
over a fraction field.

Expansion along the bottom row gives the coefficient
\[
0=[u^2]\mathcal J
=\Omega r_v-q\bigl(
\det[b_{s_1},a_{s_2},a_v]
+\det[a_{s_1},b_{s_2},a_v]\bigr).
\tag{4}
\]
Indeed the \(r_v\) minor has quadratic term \(\Omega\);
the \(qu\) minor has a minus sign and contributes the two
displayed terms. The \(r_{s_1}\) and \(r_{s_2}\) minors have
degree at most one. This fixes the sign in (4).

For \(i,j\in\{1,2\}\), let \(\Gamma^0_{ij}\in S_\Omega\) be
the coefficient of \(b\) in the \(\mathcal C\)-expansion of
\(b_{s_i s_j}\). Mixed partial equality gives
\(\Gamma^0_{12}=\Gamma^0_{21}\).
The \(b\)-coefficient \(g_i\) of \(a_{s_i}\) and the two
determinants in (4) are
\[
\begin{gathered}
g_i=\rho_{s_i}+\Gamma^0_{i1}y_1+\Gamma^0_{i2}y_2,\qquad
a_v=(y_1)_v b_{s_1}+(y_2)_v b_{s_2},\\
\det[b_{s_1},a_{s_2},a_v]=-\Omega\,g_2(y_2)_v,\qquad
\det[a_{s_1},b_{s_2},a_v]=-\Omega\,g_1(y_1)_v .
\end{gathered}
\tag{5}
\]
For example, the first determinant has columns
\(e_2,(g_2,*,*)^t,(0,(y_1)_v,(y_2)_v)^t\) in the
\(\mathcal C\)-basis, so its sign is negative. The other is
computed in the same fixed basis. Terms involving derivatives
of the \(y_j\) contribute only along \(b_{s_1},b_{s_2}\), so
they do not enter \(g_i\).

## 3. Integrating a base-valued quadratic form

The symmetry of the two mixed coefficients makes
\[
\begin{gathered}
\Psi=\rho_{s_1}y_1+\rho_{s_2}y_2+
\frac12\Gamma^0_{11}y_1^2+
\Gamma^0_{12}y_1y_2+
\frac12\Gamma^0_{22}y_2^2\in S_\Omega[y_1,y_2],\\
\Psi_v=g_1(y_1)_v+g_2(y_2)_v,\qquad
0=r_v+q\Psi_v .
\end{gathered}
\tag{6}
\]
The last equation is (4)--(5) after division by the invertible
\(\Omega\). All coefficients of this quadratic form are in the
actual base \(S_\Omega\); they have no \(v\)-dependence.

Thus \(W(r+q\Psi)=0\) in the local calculation.
But \(r+q\Psi\) already belongs to \(A_\Omega\). The localization
map is injective, and
\(\ker(W|A_\Omega)=S_\Omega\), since \(W\Omega=0\).
The exact global-on-this-open-set conclusion is therefore
\[
r+q\Psi=\chi\in S_\Omega,\qquad
r=\chi-q\Psi\in S_\Omega[y_1,y_2],\qquad
A_\Omega=S_\Omega[y_1,y_2].
\tag{7}
\]
The auxiliary local-slice factor \(g\) is absent from (7).
No primitive division of \(W\), global slice for \(W\), or
integration through a parameter-field extension was used.

## 4. Equality with the original smaller generator ring

Return to the actual completed matrix of invariant-plane88:
\(M b=e_1\), \(Mx_{\rm tr}=(\sigma,A_1,A_2)^t\),
\(R=S[A_1,A_2]\), and \(h=u-\sigma\).
Then \(Ma=(-h,A_1,A_2)^t\).
The earlier volume identity places \(h\) in \(R_\Omega\).
Consequently \(a\in R_\Omega^3\), and the inverse
\(\mathcal C\)-matrix puts \(y_1,y_2\) in \(R_\Omega\).
Conversely (2) places \(a\) in \(S_\Omega[y_1,y_2]^3\),
so \(A_1,A_2\) belong to that ring by applying \(M\).
Together with (7), this gives
\[
\boxed{\quad
A_\Omega=R_\Omega=S_\Omega[y_1,y_2].
\quad}
\tag{8}
\]
This proves normality of \(R_\Omega\), since \(A\) is normal.
It does not claim that \(y_1,y_2\) are algebraically independent
over \(S_\Omega\): the relative transcendence degree is one.
The two-generator ring has a height-one hypersurface relation,
not a free polynomial presentation on two variables.

The equality is stronger than the finite unramified normalization
conclusion in [the preliminary local note](nonconical-unramified-normalization-pass90.md).
That note's algebra-only nodal control illustrates a limitation of
the weaker differential argument; it does not satisfy the full
actual volume identities used in (4)--(7).

The divisor \(\Omega=0\) has not been removed from the global
problem. Even if \(\Omega\) is a nonzero constant and (8) is
global, two relative generators over the invariant plane do not
alone prove \(A\simeq\mathbb C^{[3]}\). No global recognition or
new coordinate-system claim is made here.

Root proposed the quadratic coefficient and symmetric potential.
General independently reconstructed its determinant signs,
coefficient derivatives, kernel contraction and both directions
of the ring equality, then supplied this saved proof.
The relevant predecessor proofs were read through EOF; this
argument imports no new external classification theorem and adds
no numerical method. Every pass89 and earlier file is unchanged.
