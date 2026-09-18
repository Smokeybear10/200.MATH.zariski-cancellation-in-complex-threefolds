# Independent audit of the dense three-good chain obstruction

The arbitrary-length differential-field obstruction in156 survives
the reconstruction below. Its critical-fiber argument gives a strict
degree contradiction with every coefficient derivative retained.
The exact-field extraction meets that lemma's fixed-axis hypotheses
under the stated139/145/153 inputs.

A sharp boundary matters: a length-two formal chart can satisfy both
coefficient-gradient identities, whole generic-line return and a
Jacobian equal to one while failing actual rational-field return by
degree two. Section 5 gives such a chart explicitly. It is not an
actual sliced four-ring or a polynomial Keller counterexample.
It demonstrates why a weaker formal argument would be unsound.

This is a bounded mathematical audit of a vulnerable part of156,
not recursive certification of the entire three-good theorem or257.
No retained source is changed.

## 1. Exact sublemma being challenged

Let \(F\) be a characteristic-zero field with derivation \(\delta\),
extended to fix independent formal \(U,V\).
For \(n\ge3\), choose \(A_i\in F[T]\) of degrees \(d_i\ge2\), and set
\[
\begin{gathered}
P_0=U,\quad P_1=V-A_1(U),\quad
P_i=P_{i-2}-A_i(P_{i-1})\quad(2\le i\le n-1),\\
\Phi=A_n(P_{n-1})+\lambda P_{n-2}+\nu,\qquad
\lambda\in F^*,\quad \nu\in F .
\end{gathered}
\tag{1}
\]
The assertion is that no \(\alpha\in F^*,\beta,c\in F\) satisfy
\[
\delta\Phi=\partial_U(\alpha P_{n-1}+\beta+c\Phi).
\tag{2}
\]
Every coefficient of every \(A_i,\lambda,\nu,\alpha,c\) may vary.
Put \(\nabla=\delta-c\partial_U\), \(Q_i=\nabla P_i\), and write
\(\dot A_i\) for coefficient differentiation at fixed argument.
Then
\[
\begin{gathered}
Q_0=-c,\quad Q_1=B(U),\quad
B(T)=cA_1'(T)-\dot A_1(T),\quad \deg B\le r:=d_1,\\
Q_i=Q_{i-2}-\dot A_i(P_{i-1})-A_i'(P_{i-1})Q_{i-1},\qquad
\nabla\Phi=\alpha(P_{n-1})_U .
\end{gathered}
\tag{3}
\]
The first issue is to prove \(\deg B\le r-1\). Without this
improvement, the final critical-fiber degree gap is not established.

## 2. Reconstructing the first leading-coefficient gate

Use independent coordinates \(R=P_1,H=P_2\), whose inverse is
\(U=H+A_2(R)\), \(V=R+A_1(H+A_2(R))\).
Write \(F_1(H,R)=\Phi\), \(G(H,R)=P_{n-1}\), and \(q=d_2\).
The literal chain rule gives
\[
\begin{aligned}
&(F_{1,R}-A_2'F_{1,H})B(H+A_2)
 +\dot F_1-(c+\dot A_2)F_{1,H}\\
&\hspace{10mm}
=\alpha\{G_H+(A_2'G_H-G_R)A_1'(H+A_2)\}.
\end{aligned}
\tag{4}
\]
Here \(\dot F_1\) differentiates every coefficient at fixed \(H,R\),
including the later polynomials and the coordinate substitutions.
There is no derivative of \(c\): the operator is applied once.

For \(n=3\), \(F_1=A_3(H)+\lambda R+\nu\), \(G=H\).
If \(\deg B=r\), the term \(-A_2'A_3'B(H+A_2)\) has exact
\(R\)-degree \(q(r+1)-1\), with nonzero coefficient in \(F[H]\).
The term \(\lambda B\) has degree \(qr\), the right side has
degree at most \(qr-1\), and the remaining terms have degree
at most \(q\). None can cancel the displayed top term.

For \(n\ge4\), first replace \(R\) by \(K=R-A_3(H)\).
The highest two \(K\)-coefficients of
\(F_1(H,K+A_3(H))\) lie in \(F\), with the highest nonzero.
Indeed start with \(H-A_4(K)\). In each subsequent nonlinear
composition, all lower powers of the preceding residual and the
added earlier residual lie at least two degrees below the new
top. The highest two coefficients therefore cannot acquire
\(H\)-dependence. For \(n=4\), use directly
\(A_4(K)+\lambda H+\nu\).

Consequently, setting
\(e=\prod_{i=4}^{n-1}d_i\), \(D=d_ne\), and
\(a_D=\operatorname{lc}_R F_1\), with empty product one, gives
\[
\deg_R G=e,\quad D>e,\quad a_D\in F^*,\qquad
\deg_R F_{1,H}=D-1,\quad
[R^{D-1}]F_{1,H}=-Da_DA_3'(H)\ne0 .
\tag{5}
\]
The \(H\)-derivative at fixed \(K\) has degree at most \(D-2\);
the displayed term comes from differentiating \(K=R-A_3(H)\).
This checks the moving-coordinate term explicitly.

If \(\deg B=r\) with leading coefficient \(b_r\), and
\(a_q=\operatorname{lc}A_2\), the first product in (4) has
\[
\begin{gathered}
\deg_R\{(F_{1,R}-A_2'F_{1,H})B(H+A_2)\}
 =D+q(r+1)-2,\\
[R^{D+q(r+1)-2}](\cdots)
 =Dq\,a_Da_q^{r+1}A_3'(H)b_r\ne0 .
\end{gathered}
\tag{6}
\]
All other left terms have degree at most \(D+q-1\).
The right side has degree at most \(e+qr-1\), using
\(\deg_R G_H\le e\), \(\deg_R G_R\le e-1\).
The strict differences are \(qr-1>0\) and \(D-e+q-1>0\).
Thus, for every \(n\ge3\),
\[
\boxed{\deg B\le d_1-1.}
\tag{7}
\]
Equivalently the leading coefficient of \(A_1\) is
\(\delta\)-constant. No such constancy is assumed for later \(A_i\).

## 3. A critical fiber proves the uniform contradiction

The pair \(T=P_{n-2},K_*=P_{n-1}\) is a polynomial coordinate
pair, with determinant \(\epsilon=(-1)^{n-2}\) relative to \(U,V\).
Choose a root \(k\) of \(A_n'\) in an algebraic closure of \(F\).
Restrict the already differentiated identity (3) to \(K_*=k\).
This step does not differentiate \(k\).

Backward substitution gives
\[
h_i:=\deg_T(P_i|_{K_*=k})
 =\prod_{j=i+2}^{n-1}d_j\quad(0\le i\le n-2),\qquad
M=d_1h_0\ge4 .
\tag{8}
\]
Start with \(P_{n-2}=T\). Each earlier nonlinear composition
has strictly greater degree than the added later residual.
Hence its leading coefficient cannot cancel. In particular
\(h_{n-2}=1\), \(h_{i-2}=d_i h_{i-1}\), and
\(V=P_1+A_1(P_0)\) has fiber degree \(M\).
The inverse-Jacobian formula gives
\[
(P_{n-1})_U|_{K_*=k}
 =-\epsilon\frac{d}{dT}(V|_{K_*=k}),\qquad
\deg_T((P_{n-1})_U|_{K_*=k})=M-1 .
\tag{9}
\]
Characteristic zero is essential to that last degree.

The full recurrence (3) and (7) imply
\[
\deg_T(Q_i|_{K_*=k})\le M-h_{i-1}
\quad(1\le i\le n-2).
\tag{10}
\]
For \(i=1\) this is \((d_1-1)h_0=M-h_0\).
The product term at the next step has degree at most
\((d_i-1)h_{i-1}+M-h_{i-2}=M-h_{i-1}\).
The entire coefficient derivative \(\dot A_i(P_{i-1})\)
has degree at most \(h_{i-2}\), which fits the same bound because
\(h_{i-2}+h_{i-1}<2h_0\le M\).
The term \(Q_{i-2}\) has a smaller bound; for \(i=2\) it is
the constant \(-c\). This proves (10) without dropping coefficient jets.

Since \(h_{n-3}=d_{n-1}\ge2\), the final \(Q_{n-2}\) has
degree at most \(M-2\). For \(n=3\) this is the initial \(Q_1\)
bound itself. The evaluated final identity is
\[
\dot A_n(k)+\dot\lambda T
 +\lambda Q_{n-2}|_{K_*=k}+\dot\nu
 =\alpha(P_{n-1})_U|_{K_*=k}.
\tag{11}
\]
The left side has degree at most \(M-2\), and the right side
has exact degree \(M-1\). This proves the precise lemma (1)--(2).

The root \(k\) may depend algebraically on the coefficients.
There is still no omitted \(\delta k\): (11) evaluates a
polynomial identity already formed over \(F\).
Differentiating a specialized identity would be a different operation.
The retained156 proof uses the valid order.

## 4. Auditing the actual-to-formal handoff

The actual chart139 gives \(L[y,z]=L[v]\), a literal first tail
\(\Phi\), a second tail \(\Psi\), and \(\Psi(y,z)=v+\beta_0\).
Its Taylor peeling uses the actual partial killing \(Y/X,Z/X\).
Separable algebraicity extends annihilation to all transformed
coefficients. No local nilpotence after an arbitrary localization
is required for the continuous Laurent derivation.

The first-tail theorem145 gives \(\Phi\in L^*g\), not merely
\(g\mid\Phi\), where \(g\) is the full generic kernel.
I specifically reconstructed its two vulnerable steps:

- For active factors, the common abstract Laurent field has one
  Gauss valuation. The selected actual target field has the entire
  residue field \(L(v)\). Actual invariant polynomials have valuation
  zero on every active factor, so their images are constant in \(X\).
  Residue comparison returns every element of \(L\) exactly.
  The factor must therefore be \(g\).
- For a possibly inactive factor no field embedding is presumed.
  Each actual invariant's common Laurent polynomial has no negative
  powers, because those coefficients vanish identically in the selected
  Gauss model. Polynomial substitution on the factor puts its image
  in \(L[\Psi]\). Apply this to all three actual speeds and intercepts.
  Both projected coordinates are recovered in that ring, so its
  transcendence degree is one and \(\Psi\) is transcendental.
  Every factor is therefore active.

The selected factor is simple by the evaluated-gradient unit
identity of signed-tail139. Thus the handoff discards no extra
or repeated component.

Leading-normalization153 gives \(f_m=\gamma\tau^{m+1}\),
\(\gamma\in\mathbb C^*\), and
\(\Phi_{m+1}=-\gamma U^{m+1}\).
The possible degree-\(m+2\) term of \(\Psi\) is an order-\(m+2\)
derivative of this \(f_m\), hence zero.
Thus \(\deg\Psi\le d=\deg\Phi=m+1\).
The unique infinity direction and exact implicit-degree identity
give \(0<\deg_v y<\deg_v z=d\).

For a nongraph, repeated degree reduction is over exactly \(L\).
The characteristic-zero AMS degree-divisibility statement is
explicitly over a field in the freshly checked
[Makar-Limanov primary source, printed page 1](https://arxiv.org/pdf/1212.0163v1).
Each leading-coefficient cancellation uses a ratio in \(L\),
not an extracted root, and preserves \(L[y,z]=L[v]\).
The smaller residual degree stays positive and strictly decreases
until it equals one. The final relation is
\(\lambda(P_{n-2}-B_n(P_{n-1}))\), in the original formal axes,
with every \(d_i\ge2\) and total degree \(d=\prod_i d_i\).
The final residual is affine in \(v\), so
\[
\Psi-\alpha P_{n-1}-\beta\in(\Phi),\qquad
\deg\Psi\le d,\quad\deg P_{n-1}<d
\quad\Longrightarrow\quad
\Psi=\alpha P_{n-1}+\beta+c\Phi,\quad c\in L.
\tag{12}
\]
The literal identity \(\Psi_U=\Phi_\tau\) now supplies (2).
No coefficient-dependent plane reframe has suppressed a derivative.

## 5. Sharp countercontrol: length two and a quadratic cover

Let \(\tau,\rho,v,X\) be independent over \(\mathbb C\), and set
\[
\begin{gathered}
L=\mathbb C(\tau,\rho),\qquad
y=\frac{v^2+\rho}{2\tau},\quad z=v+y^2,\\
\Phi=(V-U^2)^2-2\tau U+\rho,\qquad \Psi=V-U^2 .
\end{gathered}
\tag{13}
\]
Then \(\Phi(y,z)=0\), \(\Psi(y,z)=v\), \(L[y,z]=L[v]\), and
\(\Phi_\tau=\Psi_U=-2U\), \(\Phi_\rho=\Psi_V=1\).
This length-two chain satisfies the canonical degree bound.
Thus the formal lemma cannot be enlarged to \(n=2\).

It extends to a polynomial-in-\(X\) formal chart:
\[
\begin{gathered}
Y=y+\tau X,\quad R=v-v^2X-\tau^2X^2,\quad
Z=R+Y^2=z+\rho X,\\
W=\tau^2+\frac{v^2-R^2}{X},\qquad \deg_X W=3 .
\end{gathered}
\tag{14}
\]
The quotient is polynomial in \(X\), since \(R\equiv v\pmod X\).
For independent target variables \(X,Y,Z,W\), make the actual
polynomial change
\[
R=Z-Y^2,\quad H=XW+R^2,\quad
I=R+XH,\quad J=W-2RH-XH^2 .
\tag{15}
\]
The inverse retains \(X,Y\) and is
\[
\Delta=XJ+I^2,\qquad
R=I-X\Delta,\qquad W=J+2I\Delta-X\Delta^2,\qquad Z=R+Y^2 .
\tag{16}
\]
Both orders restore the four variables. Equivalently,
\(J=W-(I^2-R^2)/X\), whose numerator is divisible by \(X\).
The determinant is one: over the field with \(X\) inverted the
change is the composition through the fixed quantity
\(H=XW+R^2\), followed by \(I=R+XH\), and back to
\(J=(H-I^2)/X\). Their determinants multiply to one, so the
same polynomial determinant identity holds without inverting \(X\).

On the formal chart (14), the identities become
\[
H=v^2+\tau^2X,\qquad I=v,\qquad J=\tau^2,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}=1 .
\tag{17}
\]
For the last identity use (15) and compute the determinant of
\((Y,v,\tau^2)\), which equals \(2\tau Y_\rho=1\).
Nevertheless,
\[
\mathbb C(X,Y,Z,W)=\mathbb C(X,Y,v,\tau^2)
\subsetneq L(v,X)=\mathbb C(X,Y,v,\tau),\qquad
[L(v,X):\mathbb C(X,Y,Z,W)]=2 .
\tag{18}
\]
The right equality uses
\(\rho=2\tau(Y-\tau X)-v^2\).
The elements \(X,Y,v,\tau\) are independent, so the even-power
subfield has exact index two.

More explicitly, after inverting \(J\), the target ring
\(\mathbb C[X,Y,I,J,J^{-1}]\) has the finite etale degree-two
cover \(\mathbb C[X,Y,v,\tau,\tau^{-1}]\), under
\(I=v,J=\tau^2\). The derivative \(2\tau\) is invertible.
In these source coordinates, the derivation holding
\(\tau,\rho,v\) fixed and differentiating \(X\) is
\[
\widetilde E=\partial_X+\tau\partial_Y .
\tag{19}
\]
It is not invariant under the deck involution
\(\tau\mapsto-\tau\). Its value on \(Y\) is outside the target
field, so it does not descend even as a field derivation.

This is not an actual counterexample to156.
It is also not a polynomial Keller counterexample: the chart in
\(\tau,\rho,v\) uses \(1/\tau\), and the described cover inverts
\(J\). It disproves the weaker replacement of actual rational-field
return by whole-line return plus a unit generic Jacobian.
It confirms the need for a separate original-ring argument154.
One unsaved symbolic calculation checked (13)--(17);
the degree-two and descent assertions are proved above, not sampled.

## 6. Verdict and remaining audit boundary

No counterexample or missing coefficient term was found in the
arbitrary-length156 lemma or its fixed-axis extraction from the
stated139/145/153 data. Sections 2--3 give its precise uniform
degree proof. Section 5 isolates an actual-input distinction that
cannot be weakened.

The separate two-stage154 and graph-correction153 sources were
also completely read to check the boundaries of the chain split.
The former uses an actual polynomial inverse and square-order
argument, not the abstract lemma proved here. The latter constructs
an invariant actual coordinate after exact-field descent, not by
calling a generic plane parameter an ambient coordinate.
Their further retained dependencies have not all been recursively
reproved in this audit.

The complete sources read were both156 core notes,
leading-normalization153, graph-correction153, actual Taylor-chart139,
signed-tail139, embedded-degree139, common-Gauss-primitivity145,
and two-stage154. In particular this is not a new audit of every
cofactor/degeneration input125/132, every prior shear lemma141, or
the other historical three-good speed-rank cases.
The AMS degree-divisibility statement was freshly checked in the
primary source; its full historical proof remains an external input.

No saved checker was executed, imported or compiled. No retained
proof, index or packet was edited. The one new finite calculation
was unsaved and checked only the explicit countercontrol identities.
The etale-cover reformulation was independently suggested by Root
and reconstructed here.
This is not human expert review, proof-assistant certification,
historical novelty clearance, or an unrestricted cancellation proof.
