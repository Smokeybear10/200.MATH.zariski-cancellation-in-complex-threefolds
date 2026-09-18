# The actual split quartic has a unit selected cofactor

**Status: working consequence of the complete actual projection proof175.**

The first potential's two return coefficients cannot vanish together
on the generic line. Consequently the selected component of the
quartic eliminant has no intersection there with an extra component.
Its evaluated cofactor is a unit. If the projected \(y\) is
nonconstant, the center polynomial is linear or squarefree quadratic,
and \(y\) has parameter degree at most two.

These statements do not make the entire eliminant irreducible:
another component may be disjoint from the actual selected curve.
No original-ring recognition or cancellation conclusion is claimed.

## 1. Exact hypotheses and the identities used

Assume the full actual split hypotheses of
[chart175](split-cubic-generic-chart-pass175-working.md):
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\tag{1}
\]
The weighted ideal is the full initial kernel, not one relation.
Use its nonzero selected LND \(N=[u^3](\partial_Z|_A)\),
exact field \(L=\operatorname{Frac}(\ker_A N)\), and
\(A_L=L[v]\), \(Nv=1\). The independent ratios \(t,\rho\)
give the commuting coefficient partials on the finite separable
extension \(L/\mathbb C(t,\rho)\), extended to fix \(v\).

The [completed projection proof175](split-projection-exceptional-cone-pass175-working.md)
now supplies the whole ring, not merely its fraction field:
\[
O=L[v]=L[y,\vartheta],\qquad R=r-y\ne0,\qquad r=k_\rho\in L .
\tag{2}
\]
Use the polynomials from chart175 and
[the quartic proof175](split-cubic-projected-quartic-bound-pass175-working.md):
\[
\begin{gathered}
f=H_2(k;U,V)+H_1(n;U,V),\quad
g_3=H_3(k;U,V)+H_2(n;U,V),\\
\mathcal P=(r-U)W_0+f-\ell,\quad
\Psi=f_VW_0+g_3-\ell_tU-\ell_\rho V,\quad
\mathcal P(y,\vartheta,w)=0,\quad \Psi(y,\vartheta,w)=m .
\end{gathered}
\tag{3}
\]
Write the evaluated coefficients as
\[
\begin{gathered}
F=f_V(y,\vartheta),\qquad B_1=f_U(y,\vartheta)-w,\\
C_i=f_i(y,\vartheta)+r_iw-\ell_i\quad(i=t,\rho).
\end{gathered}
\]
Their coefficient derivatives hold the formal variables fixed.
The two formal gradients and actual determinant are
\[
\begin{gathered}
(\mathcal P_U,\mathcal P_V,\mathcal P_{W_0})|=(B_1,F,R),\\
(\Psi_U,\Psi_V,\Psi_{W_0})|=(C_t,C_\rho,F),\\
\left[
dy\wedge(R\,d\vartheta+B_1dt+F\,d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}=-a^3\in L^* .
\end{gathered}
\tag{4}
\]

## 2. A common zero contradicts the whole plane embedding

Suppose \(R\) and \(F\) have a common zero \(v_*\) over
an algebraic closure of \(L\). At this point \(y=r\). For
\[
q(V)=f(r,V)-\ell\in L[V]
\]
the first potential gives \(q(\vartheta(v_*))=0\), and
\[
q'(\vartheta)=F+r_tR
\tag{5}
\]
gives \(q'(\vartheta(v_*))=0\).
Since \(\deg q\le2\), either \(q=0\) identically or
\[
q(V)=\kappa(V-\vartheta_0)^2,\qquad
\kappa=r_\rho/2\in L^*,\qquad \vartheta_0\in L .
\tag{6}
\]
The repeated quadratic root lies in \(L\) itself.

For the zero polynomial, division by \(U-r\) gives
\(f-\ell=(U-r)D(U,V)\), with \(\deg D\le1\).
Because \(R\ne0\), the first potential implies
\(w=D(y,\vartheta)\) in \(O\).
At \(v_*\), this makes
\(B_1=-\{w-D(y,\vartheta)\}-R D_U=0\).
Together with \(R=F=0\), it makes the middle row of (4)
zero at \(v_*\), contradicting its nonzero right side.

Consider instead (6). At \(v_*\), (4) forces
\[
B_1(v_*)\ne0 .
\tag{7}
\]
Differentiate the two evaluated potentials with respect to
the genuine parameter \(v\), keeping \(L\) fixed:
\[
B_1 y_v+F\vartheta_v+R w_v=0,\qquad
C_t y_v+C_\rho\vartheta_v+F w_v=0 .
\tag{8}
\]
Evaluation of the first identity gives \(y_v(v_*)=0\).

The center equality \(\ell=f(r,\vartheta_0)\) is an
identity in the exact field \(L\), and
\(f_V(r,\vartheta_0)=q'(\vartheta_0)=0\).
Differentiate this identity in the coefficient direction \(\rho\):
\[
\ell_\rho=f_\rho(r,\vartheta_0)
              +f_U(r,\vartheta_0)r_\rho .
\tag{9}
\]
The term involving \((\vartheta_0)_\rho\) is zero for
the stated reason, not because the moving center is held fixed.
It follows that at \(v_*\)
\[
C_\rho=r_\rho\{w-f_U(r,\vartheta_0)\}
       =-r_\rho B_1\ne0 .
\tag{10}
\]
The nonzero assertion uses (6), (7), and characteristic zero.
The second equation in (8) now forces
\(\vartheta_v(v_*)=0\).

But (2) gives a polynomial \(T(U,V)\in L[U,V]\)
with \(T(y,\vartheta)=v\). Its parameter derivative is
\[
T_U(y,\vartheta)y_v+T_V(y,\vartheta)\vartheta_v=1 .
\tag{11}
\]
The two zero derivatives at \(v_*\) contradict this identity.
Every evaluation above is made after the polynomial or
coefficient-field identity has been formed. No derivative of
the possibly moving point \(v_*\) is used.

Both possibilities for \(q\) are impossible. Thus \(R,F\)
have no common zero over an algebraic closure, equivalently
\[
(R,F)L[v]=L[v].
\tag{12}
\]
This is the claimed whole-line unit ideal.

## 3. Consequences for the eliminant and its center

Let \(G\) be the irreducible generator of the plane evaluation
kernel. The calibrated quartic proof175 gives
\[
\mathcal H=GQ,\quad G\nmid Q,\quad
Q(y,\vartheta)\ne0,\quad Q(y,\vartheta)\mid R^2 ,
\tag{13}
\]
and every zero of \(Q(y,\vartheta)\) lies over \(R=F=0\).
Equation (12) excludes such a zero. A nonconstant polynomial
in \(L[v]\) has a root after algebraic closure, so
\[
Q(y,\vartheta)\in L^* .
\tag{14}
\]
In particular there is \(c\in L^*\) with \(Q-c\in(G)\).
Therefore \((G,Q)=L[U,V]\), including when \(Q\) is a
nonconstant polynomial defining disjoint extra components.
Neither \(Q\in L^*\) in the two-variable ring nor
irreducibility of \(\mathcal H\) follows from (14).

If \(y\notin L\), the nonconstant \(R=r-y\) has a root
over an algebraic closure. An identically zero center has
\(q'=0\), and (5) would give \(F=0\) at that root.
A repeated center (6) makes the first potential force
\(\vartheta=\vartheta_0\) there, so again \(F=0\) by (5).
Both contradict (12). Hence
\[
y\notin L\quad\Longrightarrow\quad
\deg q\in\{1,2\}\ \text{and}\ \gcd(q,q')=1 .
\tag{15}
\]
To exclude a nonzero constant center, use the division identity
\(f-\ell=q+(U-r)D\) in the first potential:
\(q(\vartheta)=R\{D(y,\vartheta)-w\}\).
Both factors on the right are polynomials in \(L[v]\), and
the first is nonconstant. Their product cannot be a nonzero
constant. This excludes degree zero without assuming that
\(q\) has degree two; a linear center is still possible.

## 4. A nonconstant projected y has degree at most two

Suppose \(y\notin L\). Let \(v_*\) be any root of
\(R=r-y\) over an algebraic closure of \(L\).
Equation (12) gives \(F(v_*)\ne0\).
The first identity of (8) becomes
\[
B_1(v_*)y_v(v_*)+F(v_*)\vartheta_v(v_*)=0 .
\tag{16}
\]
If \(y_v(v_*)=0\), it would also give
\(\vartheta_v(v_*)=0\), contradicting (11).
Thus every root of \(R\) is simple.

Two distinct roots of \(R\) cannot have the same value of
\(\vartheta\): their values of both plane coordinates would
then agree, and the polynomial inverse \(T\) in (11) would
make the parameters agree. At every such root the first
potential gives \(q(\vartheta)=0\).
There are therefore at most \(\deg q\) roots of \(R\).
Since all its roots are simple, this proves
\[
1\le\deg_v y=\deg_v R\le\deg q\le2 .
\tag{17}
\]
In particular a linear center forces \(y\) to be an affine
parameter. If \(y\) is quadratic, the center is squarefree
quadratic and its two roots are matched bijectively with the
two parameter points over \(y=r\).
This argument uses polynomial generation for both separation
and the derivative identity. Birationality alone would not
justify either step.

Combining (17) with the independent
[constant-projection exclusion176](split-constant-projection-exclusion-pass176-working.md)
gives \(\deg_v y\in\{1,2\}\) for the actual split chart.
That exclusion does not depend on this note, so there is no
circular use of the nonconstant hypothesis.

## Scope and proof boundary

The new step uses whole plane generation only at (11), where
equality of fraction fields would not suffice. The center
derivative in (9) keeps the exact coefficient field and moving
root contribution explicit. These are written proof steps,
not conclusions from finite numerical or symbolic tests.

This result closes the possible finite cofactor intersection
left open in175 and bounds the first projected degree by two.
It does not prove an original polynomial
coordinate, classify every surviving degree-four plane curve,
or recognize the split-cubic invariant ring. Other initial
profiles and unrestricted cancellation remain open.
The saved175 sources were fully read before this argument.
There is no new external theorem, checker execution, frozen
artifact edit, human expert review, novelty clearance or
proof-assistant certification associated with this note.
