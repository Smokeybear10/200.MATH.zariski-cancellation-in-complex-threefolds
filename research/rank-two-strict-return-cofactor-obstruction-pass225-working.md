# The evaluated return cofactor cannot attain its cubic bound

Status: working actual-chart obstruction. The evaluated cofactor loses
at least one order relative to \(R^3\) at every geometric root of the
return polynomial \(R\). In particular it cannot be a scalar multiple
of \(R^3\) when \(R\) is nonconstant.

This excludes the saturated cubic projected component. Combined with
the retained zero-return, line and degree-two exclusions, it makes the
supplied full quartic sector with root partition \(3+1\) empty.
No arbitrary initial-frame entry or unrestricted cancellation claim
is made.

The argument uses the full actual gradients and calibrated wedge,
not a classification of cusps or a lift of coefficient-field
coordinates. Earlier224 remains a correct, weaker necessary condition;
no earlier source is altered.

## 1. Exact actual inputs

Assume the actual globally sliced frame of
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
Here \(T\) is independent, \(F_4\) is a nonzero complex homogeneous
binary quartic, and the displayed ideal is the entire initial kernel.
The original capital letters are polynomial coordinates.

The exact universal chart supplies a field \(L\), a line parameter
\(v\), and
\[
\begin{gathered}
[L:\mathbb C(t,\rho)]<\infty,\qquad
q=F_4(1,t)/\rho,\qquad \mathcal O=L[v],\\
y,\vartheta,z,w\in\mathcal O,\qquad L[y,z,w]=\mathcal O,\qquad
J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their coefficient
partials extend to \(L\) and hold \(v\) fixed.
Assume \(R\ne0\). The actual plane ring
\(\mathcal C=L[y,\vartheta]\) is finite and birational in
\(\mathcal O\), and its evaluation kernel in \(L[U,V]\) has an
irreducible generator \(G\).

For precise notation, retain the universal formal polynomials
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\qquad \mathcal R=f_V,\qquad
R=\mathcal R(y,\vartheta),\\
S=H_3(q)+H_2(k)+H_1(n),\qquad T_0=\ell_0-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-(\ell_0)_tU-(\ell_0)_\rho V-m_0,\\
\mathcal H=(q_{\rho\rho}/2)T_0^2+
                         \mathcal R f_\rho T_0+\mathcal R^2Q .
\end{gathered}
\tag{3}
\]
Here \(k,n,\ell_0,m_0\in L\), and \(H_i\) are the coefficient
Taylor polynomials of universal184. All formal derivatives are
taken before evaluation at \(U=y,V=\vartheta\).

The complete universal cofactor derivation in
[saturated-pair222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md)
gives
\[
\mathcal H=GQ_1,\qquad
0\ne q_1=Q_1(y,\vartheta)\mid R^3\quad\hbox{in }L[v].
\tag{4}
\]
In particular \(G\) occurs simply in \(\mathcal H\); no repeated
selected component has been retained. Put
\[
W_0=R^3/q_1\in L[v]\setminus\{0\}.
\tag{5}
\]
This quotient is not the original coordinate \(W\) or its
projection \(w\).

## 2. Retaining both differentiated identities

Define the actual evaluated coefficients
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
\Lambda_i=(\ell_0)_i-S_i(y,\vartheta)
                        -\mathcal R_i(y,\vartheta)w,\quad i=t,\rho,\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\\
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v .
\end{gathered}
\tag{6}
\]
The coefficient partials in \(\Lambda_i\) precede evaluation;
the subscripts on \(y,\vartheta,w\) in \(D_U,D_V\) are derivatives
of the actual polynomials in \(L[v]\).

The full universal identities, with their mixed-\(q\) terms
retained, are
\[
\begin{gathered}
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\\
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\\
Rw_v=-B_1y_v-C_1\vartheta_v,\\
R^3J_0=D_U\mathcal H_U(y,\vartheta)+
                         D_V\mathcal H_V(y,\vartheta).
\end{gathered}
\tag{7}
\]
These are polynomial identities in \(L[v]\).
The third is the \(dv\) coefficient of the third-potential
differential identity, not a differentiation of a moving root.
The last follows from the calibrated wedge in the actual chart;
its \(J_0\) is a nonzero scalar, not a free formal parameter.

Evaluating the derivative of \(\mathcal H=GQ_1\) gives
\(\mathcal H_i(y,\vartheta)=q_1G_i(y,\vartheta)\) for \(i=U,V\).
Substitute this and (5) into the last equality of (7), and cancel
the nonzero polynomial \(q_1\) in the domain \(L[v]\):
\[
W_0J_0=D_UG_U(y,\vartheta)+D_VG_V(y,\vartheta).
\tag{8}
\]
Multiplying the \(V\)-gradient identity by \(W_0\), using
\(W_0q_1=R^3\), and cancelling the nonzero polynomial \(R\)
instead gives the second polynomial identity
\[
W_0(C_1^2+R\Lambda_\rho)=-R^2G_V(y,\vartheta).
\tag{9}
\]
Neither cancellation asserts that \(R\) or \(q_1\) is an
original-ring unit.

## 3. Every root of \(R\) is a root of \(W_0\)

Let \(\Omega\) be an algebraic closure of \(L\), and let
\(r\in\Omega\) satisfy \(R(r)=0\). Suppose \(W_0(r)\ne0\).
Evaluation of (9) gives \(C_1(r)=0\).
Then the definitions in (6) imply
\[
D_U(r)=0,\qquad D_V(r)=-B_1(r)y_v(r).
\tag{10}
\]
The third equality of (7) at this point gives
\(B_1(r)y_v(r)=0\). Hence \(D_V(r)=0\) as well.
Evaluating (8) now yields
\(W_0(r)J_0=0\), contrary to \(W_0(r)\ne0\) and \(J_0\in L^*\).
Therefore
\[
R(r)=0\quad\Longrightarrow\quad W_0(r)=0
\qquad (r\in\Omega).
\tag{11}
\]

This proof does not require a simple root, a nonzero value of
\(B_1(r)\), smoothness of the plane curve, injectivity of its
normalization, or any assumed degree of \(y\).
Every derivative is taken in the original polynomial identities
before scalar extension and point evaluation. No coefficient
partial is applied to the algebraic point \(r\).

Let \(\operatorname{rad}R\) denote the monic squarefree part of
the nonzero polynomial \(R\), with \(\operatorname{rad}R=1\)
when \(R\) is constant. Characteristic zero and (11) imply
\(\operatorname{rad}R\mid W_0\) in \(\Omega[v]\), and also in
\(L[v]\): monic polynomial division over \(L\) leaves a remainder
that is zero after extension to \(\Omega\).
Thus the strict cofactor bound is
\[
\boxed{
\operatorname{rad}R\mid R^3/q_1,\qquad
q_1\mid\frac{R^3}{\operatorname{rad}R}
\quad\hbox{in }L[v].}
\tag{12}
\]
In particular, when \(R\) is nonconstant,
\[
\deg_vq_1\le3\deg_vR-\deg_v\operatorname{rad}R
 <3\deg_vR .
\tag{13}
\]
The special case \(q_1=cR^3\), \(c\in L^*\), is consequently
impossible for nonconstant \(R\).

## 4. Saturated cubics are excluded

Suppose the selected component has total degree \(g=3\), and
its pure leading line occurs with multiplicity \(m=3\) in the
leading sextic.
The exact degree argument222, recalled independently in
[fiber224](rank-two-saturated-cubic-fiber-injectivity-pass224-working.md),
gives
\[
\deg_vq_1=9,\qquad
\deg_vR=3,\qquad q_1=cR^3,\quad c\in L^* .
\tag{14}
\]
For clarity, the cofactor has total degree three and its top
homogeneous part contains none of the selected leading factor.
Its value on the nonzero degree-three leading vector of
\((y,\vartheta)\) is therefore nonzero, giving degree nine.
The universal return is affine in the projected pair, so its
degree is at most three. Divisibility (4) forces the remaining
equalities in (14).

Now (13) would give \(9\le8\), a contradiction.
Thus no actual saturated cubic component \(g=m=3\) occurs.
This excludes both singular and smooth possibilities at once;
no separate cusp normal form is required.

## 5. Consequence for root partition \(3+1\)

For a supplied full initial kernel with
\(F_4=c\,l^3m\), where \(l,m\) are independent complex root
forms, the retained
[cubic frontier223](rank-two-triple-root-cubic-frontier-pass223-working.md)
already proves that any actual frame would have a saturated
cubic component. Its composition is precise:

- the nonsquare zero-return theorem221 excludes \(R=0\);
- the actual line proof223 excludes both pair-line directions;
- the degree-two cofactor comparison223 excludes conics;
- the two distinct leading pair factors each have multiplicity
  three, so the only remaining component has \(g=m=3\).

Section4 excludes that last case. Consequently
\[
\boxed{\text{No supplied actual globally sliced exact1122 frame
with full initial kernel }ZW-c\,l^3m\text{ exists}.}
\tag{15}
\]
This is restricted nonrealizability, not an arbitrary-entry theorem
or unrestricted complex-threefold cancellation. It does not assert
that all polynomial leading data with that one equation are
inconsistent, or that a relation alone is the entire initial ideal.

The new proof logically strengthens the earlier nodal-fiber224
condition and any separately established smooth-cubic restriction.
Those sources are left unchanged. No generic-field coordinate
operation has been asserted to be a polynomial automorphism of
the original ring.

## 6. Verification and boundaries

The complete universal-cofactor222 and cubic-frontier223 sources
were freshly read before this composition, and their exact hashes
were checked after the final TeX-only correction to222.
The underlying gradient and wedge identities were independently
reconstructed. In a fresh unsaved symbolic calculation, the raw
wedge remainder before imposing the third-potential derivative
factored by \(B_1y_v+C_1\vartheta_v+Rw_v\), and vanished after
that exact relation was imposed.

The root and squarefree-divisor arguments are written proofs, not
finite-test conclusions. No saved checker was executed, imported
or compiled, and no previous source, index or packet was edited.
No human expert review, proof-assistant certification, historical
novelty clearance, external submission, or unrestricted solution
is asserted.
