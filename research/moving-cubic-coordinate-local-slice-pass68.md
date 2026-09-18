# An actual coordinate local slice in a moving cubic branch

In the independent moving-top cubic branch whose original action and
two defects have joint rank three, the constant-top graph calculation
survives invariant localization in a precise form. It produces either
an original invariant coordinate or an original polynomial coordinate
\(S\) satisfying \(ES=g\), where \(g\) is the invariant top factor.
The latter is a coordinate local slice, not a slice of the original
action when \(g\) is nonconstant.

This note does not infer global recognition from that local slice.
It does not call a polynomial-four-ring theorem on \(B_g\), assert
that the localized coordinate partials are LNDs, or preserve the
rank of a defect pair without checking it.

## 1. Original hypotheses and the exact divided action

Let \(k=\mathbb C\) and
\[
B=k[Q_1,Q_2,X,Y]=A[s_*],\qquad E\in\operatorname{LND}_k(B),
\qquad Es_*=1,\qquad A=\ker E.
\]
The genuine coordinate partials satisfy
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2),\qquad
\operatorname{ad}_E^3T_j=0\quad(j=X,Y).
\tag{1}
\]
Put \(W_i=[E,T_i]\), \(V_j=[E,W_j]\). Retain independent
\(V_X,V_Y\), exact original flow degree three, and the nonzero
power-law alternative of the
[full top-line theorem](two-quadratic-top-line-pass42.md):
\[
E^3x=cg^3,\qquad L_0E^2x=\lambda g^2,\qquad
g\in\ker E\setminus k,\qquad c\ne0,\quad\lambda\ne0.
\tag{2}
\]
Here \(c\) is a constant good vector, \(\lambda\) is a constant
bad two-vector, and \(L_0\) selects the bad coordinates.
Assume additionally
\[
\operatorname{rank}_{\operatorname{Frac}B}(E,V_X,V_Y)=3.
\tag{3}
\]
Only constant changes within the good and bad pairs are used to
normalize \(c=e_1\) and \(\lambda=(1,0)^t\).

On the actual invariant localization \(B_g\), set
\[
\delta=E/g.
\]
This is an LND of \(B_g\). The exact rescaling formulas are
\[
[\delta,T_i]=g^{-1}W_i+g^{-2}(T_i g)E,
\qquad
\widetilde V_j:=\operatorname{ad}_\delta^2T_j
 =g^{-2}V_j+2g^{-3}(W_jg)E.
\tag{4}
\]
The original highest identities give \(W_i g=0\) for good
\(i\), and \(V_jg=0\) for bad \(j\). Consequently the divided
action retains the adjoint bounds (1), and
\[
\delta^3x=e_1,\qquad \delta^2X=1,\quad \delta^2Y=0.
\tag{5}
\]
The exact rank formula in pass42 gives
\[
\operatorname{rank}(\widetilde V_X,\widetilde V_Y)=2,
\quad
\langle\delta,\widetilde V_X,\widetilde V_Y\rangle
=\langle E,V_X,V_Y\rangle.
\tag{6}
\]
This is where (3) is used. At original joint rank two the normalized
defect pair has rank one, and the following graph argument does not
apply.

The original \(V_X,V_Y\) are polynomial LNDs. No such claim about
the divided defects is needed below. Nor is local nilpotence of
the original partials on \(B_g\) assumed.

## 2. Recover the exact rational kernels without a localization shortcut

The original common ring
\[
C_0=B\cap\ker E\cap\ker V_X\cap\ker V_Y
\]
contains \(g\). The rank-three distribution in (3) bounds its
transcendence degree by one. It is integrally closed in its fraction
field: an element integral over it lies in normal \(B\), and all
three defining derivations kill that fraction field.
The polynomial-curve theorem therefore gives an actual \(t\in B\)
with
\[
C_0=k[t],\qquad g=g_0(t),\qquad B\cap k(t)=k[t].
\tag{7}
\]
The exact source is de Bondt, Corollary 3.2 and Lemma 3.3; neither
finite generation of \(C_0\) nor an ambient-coordinate claim about
\(t\) is added.[^curve]

The rational common kernel is exactly \(k(t)\). Indeed, for a
reduced fraction \(p/q\in\operatorname{Frac}B\) killed by an
original LND \(D\), the equality \((Dp)q=pDq\) makes \(p\mid Dp\)
and \(q\mid Dq\). The LND degree argument gives \(Dp=Dq=0\).
Apply this to the three original LNDs, then use (7).
By (6), the same rational common kernel belongs to
\(\delta,\widetilde V_X,\widetilde V_Y\).

Put
\[
\sigma=\delta X\in B_g,\qquad\delta\sigma=1.
\]
The highest coefficients of the actual divided inverse-Jacobian
identity give
\[
\widetilde V_j(\delta^2x)=0,\qquad
\widetilde V_j(\delta X)=\widetilde V_j(\delta Y)=0.
\tag{8}
\]
In particular the two divided defects kill \(\sigma\). They
commute with \(\delta\) by its adjoint bounds.

Here is an elementary rational-kernel argument that does not
assert those two fields are LNDs. Let \(F=\operatorname{Frac}B\)
and \(K_0=\operatorname{Frac}(\ker(\delta|B_g))\).
The actual slice identity gives \(F=K_0(\sigma)\). Each divided
defect preserves \(K_0\) and kills \(\sigma\).
For an invariant reduced fraction \(P(\sigma)/Q(\sigma)\),
with coefficients in \(K_0\) and monic \(Q\), coprimality gives
\[
D P=cP,\qquad D Q=cQ.
\]
Monicity forces \(c=0\). Thus every coefficient of \(P,Q\) is
invariant. Applying this to both fields and using their common
kernel with \(\delta\) proves
\[
F\cap\ker\widetilde V_X\cap\ker\widetilde V_Y=k(t,\sigma).
\tag{9}
\]

Equations (5),(8) now give rational one-variable functions
\(F_0,U,G\in k(t)\) such that
\[
\delta^2x=(\sigma-F_0(t),U(t),1,0)^t,\qquad
\delta X=\sigma,\quad \delta Y=G(t).
\tag{10}
\]
The symbols \(t,\sigma\) are not asserted to be an ambient
coordinate pair.

## 3. The algebraic constant-top gates still hold

Let \(J=\operatorname{Jac}(\delta x)\). All entries are in \(B_g\).
The divided flow and the actual conjugated partial matrix are
inverse matrices over \(\operatorname{Frac}B[z]\):
\[
\left(I+zJ+\frac{z^2}{2}\operatorname{Jac}(\delta^2x)\right)
\left(I-zJ+\frac{z^2}{2}\widetilde{\mathcal V}L_0\right)=I.
\]
Their reverse product is also \(I\). The companion identities and
the rank-preserving block lemma therefore work over the fraction
field exactly as in the
[constant cubic reduction](constant-top-cubic-pass65.md).
No ring-polynomiality or local nilpotence of a coordinate partial
is used in that matrix argument.

In particular the six-dimensional companion has cube zero and
rank at least four, so its type is \((3,3)\). Hence
\[
\operatorname{rank}\operatorname{Jac}(\delta^2x)=2,
\qquad U'\ne0.
\tag{11}
\]
The reverse-product cubic coefficient and (10) give
\[
Je_1=\widetilde V_X(x),\qquad
U'[\delta,T_2]+F_0'\widetilde V_X+G'\widetilde V_Y=0.
\tag{12}
\]

If \(G=0\), the original bad coordinate \(Y\) is \(E\)-invariant.
If \(G\in k^*\), the original coordinate \(S=Y/G\) satisfies
\(\delta S=1\) and \(ES=g\). It remains to consider \(G'\ne0\).

## 4. Replay the graph, retaining the original generators

All integrations in Sections 2--5 of the
[constant cubic graph proof](independent-cubic-graph-closure-pass67.md)
use (8)--(12), a slice of the action being integrated, and the
exact rational common kernel. These have now been established
for \(\delta\), without claiming that \(B_g\) is a polynomial
four-ring. For clarity, the resulting graph is recorded explicitly.

Define
\[
a=\frac{F_0'}{2G'},\quad C=\frac{U'}{2G'},\quad
d=aG-F_0,\quad b=U-CG,\quad
x=X-\sigma^2/2,\quad y=Y-G\sigma.
\]
The two good velocities are
\[
\delta Q_1=X/2+\sigma^2/4+d\sigma-aY+k,\qquad
\delta Q_2=CY+b\sigma+l,
\]
with \(k,l\in k(t)\). Subtracting their explicit defect
potentials gives \(m,n\in k(t)\) and
\[
\begin{aligned}
Q_1={}&\sigma^3/6-F_0\sigma^2/2+(x/2-ay+k)\sigma\\
 &+dx-\frac{a'}{2G'}y^2+\frac{k'}{G'}y+m,\\
Q_2={}&U\sigma^2/2+(Cy+l)\sigma
 +bx+\frac{C'}{2G'}y^2+\frac{l'}{G'}y+n.
\end{aligned}
\tag{13}
\]
The integration constants are justified by the rational kernel
\(k(t)\), not by a coordinate assertion about any auxiliary ring.

Set \(K=k(t,\sigma)\). Since \(g=g_0(t)\), localization of the
actual original generators and (13) give
\[
B_g\otimes_{k[t]_{g_0}[\sigma]}K
=K[Q_1,Q_2,X,Y]=K[X,Y].
\tag{14}
\]
Thus \(X,Y\) are algebraically independent over \(K\). All entries
of \(T_i t,T_i\sigma\) belong to the right side of (14), including
their original \(g\)-denominators. The true good-partial chain rule
therefore gives a polynomial inverse matrix:
\[
\mathcal K=
\frac{\partial(Q_1,Q_2)}{\partial(t,\sigma)}
\in\operatorname{Mat}_2(K[X,Y]),
\qquad \det\mathcal K\in K^*.
\tag{15}
\]
Only after the actual generation equality (14) is this determinant
condition used.

The same three coefficients as in pass67 now yield
\[
[X^2]\det\mathcal K=-b'/2,\qquad b=b_0\in k,
\qquad U=b_0+\kappa G^2,\quad\kappa\in k^*;
\]
\[
[XY]\det\mathcal K=-\tfrac12(l'/G')',\qquad
l=a_2G+l_0,\quad a_2,l_0\in k;
\]
\[
[X]\det\mathcal K=l_0d'-n'/2,\qquad
n=2l_0d+n_0,\quad n_0\in k,\quad l_0\ne0.
\tag{16}
\]
If \(l_0=0\), the last equation makes the entire second
determinant row zero, contradicting (15).
The fact that the coefficients here are rational functions rather
than polynomials of \(t\) causes no change: the constants of
differentiation on \(k(t)\) are precisely \(k\).

Consequently
\[
\boxed{
S=\frac{Q_2-b_0X-\kappa Y^2/2-a_2Y-n_0}{l_0}
 =\sigma+2d(t),\qquad ES=g.}
\tag{17}
\]
The left side of (17) proves that \(S\) is an actual polynomial
coordinate of the original \(B\). Its inverse is the displayed
triangular expression for \(Q_2\). No denominator survives in
that coordinate change. The right side computes its derivative
on \(B_g\); equality \(ES=g\) then holds in the original domain
\(B\). Also \(E^2S=0\).

## 5. What has and has not descended

The theorem established above is:
under (1)--(3), either \(Y\) is an original invariant coordinate,
or there is an original coordinate \(S\) with \(ES=g\).
The invariant-coordinate case has the existing original-slice
recognition endpoint. The second outcome is not such an endpoint.

In particular, although
\[
\delta S=1,\qquad
B_g=(\ker E)_g[S],
\tag{18}
\]
one may not replace (18) by \(B=A[S]\). When \(g\) is nonconstant,
\(ES=g\ne1\), and the supplied original slice is still \(s_*\).
The quotient \(B/(S)\simeq k^{[3]}\) is not identified with \(A\):
evaluation at \(S=0\) has not been shown to be the projection
associated to \(E\). Nor does (18) prove that \(g\), \(t\), or
any original invariant denominator is an ambient coordinate.

Thus the graph has descended farther than a conditional localized
chart: its output coordinate itself is global. Recognition of
the original kernel, or exclusion of the remaining \(ES=g\)
configuration by the full frame, remains a separate implication.
The original joint-rank-two case, where the divided defects drop
rank, is not addressed here.

## Verification and source scope

This is a written algebraic extension of the frozen pass67 graph
calculation. Its finite graph coefficients are the same ones
covered by that proof's standalone checker; no new checker,
method count, actual moving-frame realization, or global
recognition claim is added.
The pass42 rescaling/rank section, complete pass65 constant cubic
reduction, pass66 good-field proof, and complete pass67 graph proof
were read directly for this extension. The curve source below,
including the complete Corollary 3.2 and Lemma 3.3 proofs, was
directly reread in the retained primary text and checked against
the current primary HTML.

[^curve]: Michiel de Bondt, *Rational maps \(H\) for which
  \(K(tH)\) has transcendence degree 2 over \(K\)*,
  [arXiv:1501.06046v4](https://arxiv.org/html/1501.06046v4),
  Corollary 3.2 and Lemma 3.3. Applied to a normal
  transcendence-degree-one subalgebra of the actual polynomial
  ring, these identify it with a polynomial curve ring. They do
  not assert that its generator is an ambient coordinate.
