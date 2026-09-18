# The quartic-x, quadratic-sigma pattern is impossible

Working exclusion: under the full actual moving-slope chart of349,
the normalized intrinsic degree pattern (deg p,deg x,deg q)=(2,4,6)
cannot occur. The proof uses an exact even/odd decomposition over L,
the whole three-generator ring return, and the corrected fourth
potential. It needs no projective genus formula or ambient change.

## 1. The retained actual input

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
the globally sliced polynomial four-ring, exact1222 degrees, full initial
kernel X^2Z-Y^2, literal selected Z-partial, whole generic-line return,
strong complex-field return and nonzero all-X determinant. Assume
\[
k=s,\qquad n=B(t)s+f(t),\qquad B,f\in\ker_L\partial_s,
\qquad b=B'\ne0.
\tag{1}
\]
Use the exact affine quadric coordinates of
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md):
\[
O=L[v]=L[x,p,q],\qquad x^2+bpq=d\in L,
\quad p=\sigma-(\ell_s+B^2)/b.
\tag{2}
\]
They are functions over the exact coefficient field, not original
coordinates in the polynomial four-ring.

Suppose for contradiction that
\[
(\deg_vp,\deg_vx,\deg_vq)=(2,4,6).
\tag{3}
\]
The already proved leading-degree comparison in
[354](principal-paraboloid-moving-slope-intrinsic-degree-patterns-pass354-working.md)
then gives
\[
\ell_{ss}=0,\qquad b'\ne0,
\qquad \operatorname{lc}_v(x)
 =-\frac{b'}{2b}\operatorname{lc}_v(p)^2.
\tag{4}
\]
The corrected fourth level, with rho coefficients in L, is
\[
\begin{aligned}
0=\Phi={}&-2bp^2x+\frac{b'}2p^2q+\kappa p^3
 +bxq+(A_2-2C)xp\\
&+\rho_{11}pq+\rho_{20}p^2+\rho_{10}p+\rho_{01}q+\rho_{00},
\end{aligned}
\tag{5}
\]
where A2=n_tt/2-B^2 and C=ell_s+B^2. In particular the q^2 term
has vanished by(4), not by an extra assumption.

## 2. Exact quadratic centering without a square-root extension

An affine translation of v over L completes the square in p. Denote
the translated parameter by w and write
\[
p=\alpha(w^2-\delta),\qquad
\alpha\in L^*,\quad\delta\in L.
\tag{6}
\]
Only division by the leading coefficient and by two is required.
No square root of alpha or delta is adjoined. Since deg x=4, there
is a unique decomposition
\[
x=E(p)+wF(p),\qquad
E,F\in L[p],\quad \deg E=2,\quad \deg F\le1.
\tag{7}
\]
The top coefficient of E is
\[
e_2=-\frac{b'}{2b}\ne0
\tag{8}
\]
by(4). As L[p]-modules one has the direct sum
\[
L[w]=L[p]\oplus wL[p],\qquad w^2=p/\alpha+\delta.
\tag{9}
\]
The same independence holds over L(p): w has a quadratic minimal
polynomial there, since a linear polynomial in p is not a square
in L(p), as seen at its simple zero.

The polynomial F is nonzero. If it vanished, x would belong to L[p],
and the quadric would put q=(d-E(p)^2)/(bp) in L(p). Since q is
also in L[w], its unique decomposition(9) would have zero odd part,
so q would belong to L[p]. This contradicts L[x,p,q]=L[w], because
deg_w p=2. This argument does not assume that q has no apparent
denominator before the quadric is evaluated.

## 3. The fourth level has a nonzero odd coefficient

Put u=p/alpha+delta. The quadric gives an equality in L(p)[w]:
\[
q=q_{\rm even}+wq_{\rm odd},\qquad
q_{\rm even}=\frac{d-E^2-uF^2}{bp},\qquad
q_{\rm odd}=-\frac{2EF}{bp}.
\tag{10}
\]
These rational expressions are used only to compute the already
polynomial identity(5). Neither p nor any other nonconstant function
is declared invertible in O.

Substitute(7),(10) into(5) and reduce w^2 to u. The coefficient of w
is exactly F(p)N(p)/p, where
\[
\begin{aligned}
N(p)={}&d-3E(p)^2-uF(p)^2-\frac{b'}b p^2E(p)-2bp^3\\
&+(A_2-2C)p^2-\frac{2\rho_{11}}b pE(p)
 -\frac{2\rho_{01}}b E(p).
\end{aligned}
\tag{11}
\]
For clarity, the bxq term contributes
F(d-3E^2-uF^2)/p. The b'p^2q/2 term contributes
-(b'/b)pEF. Terms independent of x and q contribute no odd part.
Thus no coefficient-level derivative or moving-parameter derivative
is involved in(11).

Because deg E=2 and deg F<=1, the only degree-four contributions to N
are -3E^2 and -(b'/b)p^2E. Their sum has coefficient
\[
\operatorname{lc}_p N=-3e_2^2-\frac{b'}b e_2
 =-\frac{(b')^2}{4b^2}\ne0.
\tag{12}
\]
Consequently N is nonzero. Since F is nonzero and L(p) is a field,
F N/p is nonzero. But the quadratic independence in(9) forces the
odd coefficient of the zero identity(5) to vanish. This contradiction
excludes(3).

## 4. Scope and checks

The conclusion excludes a degree pattern, not the entire moving-slope
sector. It covers both d=0 and d nonzero, all possible lower coefficients
of E and F, and both constant and linear nonzero F. There is no case
omitted by dividing by a lower coefficient or by adjoining a coefficient
square root. It does not recognize the remaining affine or quadratic
intrinsic presentations, or establish arbitrary actual chart entry.

Fresh unsaved algebra e3ed90 verified the complete rational odd-part
identity(11) with arbitrary coefficients of E and F, and the top(12).
The earlier independent specializations7107c6 and6424f2 respectively
checked constant and linear odd parts. Those calculations verify stated
identities, not the whole-return argument or cancellation. Root read the
full input349 and354; a separate source audit is recorded only after
completion. No saved checker was executed, imported, compiled or rerun
for this note. No novelty, external review or formal-proof claim is made.
