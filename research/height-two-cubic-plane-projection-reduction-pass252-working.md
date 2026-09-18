# Cubic-plane reduction and two recognition gates for a height-two shift-two chart

Under the actual hypotheses of250, a nonzero quadratic coefficient
in the second projected variable forces complex quadratic leading
ratios and hence three-good recognition. A constant first projection
also gives original-ring recognition, through a primitive commuting
derivation and a separate three-variable theorem.

Every branch not recognized here has an affine first projection and
a graph of degree at most three over the exact coefficient field.
Its remaining bad-linear slope is complex and can be removed by an
actual linear shear. This is not recognition of every height-two frame.

## 1. Retained actual input and notation

Read the complete [shift-two chart250](height-two-shift-two-cubic-chart-pass250-working.md).
Its hypotheses include an actual polynomial frame
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),
\tag{1}
\]
with height-two full initial kernel, nonproportional good speeds
\(a=EX,b=EY\), and exact selected shift two for the literal
\(\partial_Z\). The choice of this pivot is part of the input.
An exchange of the bad slots requires the rebuilt chart in250.

The input supplies
\[
\begin{gathered}
N=[u^2](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad A_{\ker_A N\setminus\{0\}}=L[v],
\qquad Nv=1,\\
t=b/a,\quad q=(E^2Z/2)/a^2,\quad
\rho=(E^2W/2)/a^2,\quad
C_0=\mathbb C(t,q,\rho),\quad [C_0:\mathbb C(t)]<\infty,\\
[L:\mathbb C(t,\lambda)]<\infty,\qquad
a,t,q,\rho,\lambda\in L,\qquad a\ne0 .
\end{gathered}
\tag{2}
\]
Here \(t,\lambda\) are algebraically independent. Their partials
extend uniquely to \(L\), commute, and fix \(v\). The
\(\lambda\)-partial kills \(C_0\). A prime on \(q,\rho\) denotes
the extended \(t\)-derivative. In particular these functions are
not assumed rational in \(t\).

For \(k,n,\ell\in L\), put
\[
m=k_\lambda,\quad d=\rho'',\quad
f(U)=\frac{q''-dm}{2}U^2+k_tU+n,\quad
\zeta=w-\frac d2y^2 .
\]
The actual map and its returned plane ring are
\[
\begin{gathered}
Y=y+tX,\quad
Z=z+(q'y+k)X+qX^2,\quad
W=w+(\rho'y+\lambda)X+\rho X^2,\\
z=mw+f(y),\qquad L[y,w]=L[y,\zeta]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}
   =-a^2\in L^*\quad\hbox{for every }X .
\end{gathered}
\tag{3}
\]
The shear defining \(\zeta\) is initially only over \(L\).
Neither \(\zeta\) nor \(v\) is declared an original coordinate.

## 2. The exact cubic has a unit evaluated gradient

For reference, the raw row operations in250 leave the rows
\[
dy+Xdt,\qquad B_1dt+C_1d\lambda,\qquad
dw+X(dy\,dt+d\lambda),
\quad
B_1=m_tw+f_t(y),\quad C_1=m_\lambda w+f_\lambda(y).
\tag{4}
\]
The product \(dy\,dt\) in the last row means \(d\cdot y\cdot dt\);
the first \(dy\) in (4) denotes the differential of \(y\).
All coefficient derivatives of \(f\) hold \(U\) fixed.
The positive determinant coefficient is
\((B_1-dyC_1)y_v+C_1w_v=0\).
Its exact integrability uses
\(f_{\lambda U}=m_t-dU m_\lambda\), not an extra hypothesis.

Writing
\[
\mathcal D=q'''-\rho'''m,
\]
the complete depressed cubic from250 is
\[
\mathcal H(U,V)=
\frac{m_\lambda}{2}V^2+(m_tU+n_\lambda)V
 +\frac{\mathcal D}{6}U^3+\frac{k_{tt}}2U^2+n_tU-\ell,
\qquad \mathcal H(y,\zeta)=0,\qquad \mathcal H\ne0 .
\tag{5}
\]
There is a useful stronger identification of its gradient:
\[
\boxed{\mathcal H_U(y,\zeta)=B_1,\qquad
       \mathcal H_V(y,\zeta)=C_1.}
\tag{6}
\]
Indeed \(f_t=(\mathcal D-dm_t)U^2/2+k_{tt}U+n_t\), and
\(f_\lambda=-dm_\lambda U^2/2+m_tU+n_\lambda\).
Substitute \(w=\zeta+dy^2/2\) into (4). The quadratic terms
cancel in both identities (6).

The constant determinant coefficient is
\[
\left[dy\wedge(B_1dt+C_1d\lambda)\wedge dw\right]
 _{dt\wedge d\lambda\wedge dv}=-a^2 .
\tag{7}
\]
At a common geometric zero of \(B_1,C_1\) in the parameter \(v\),
the already-formed middle row in (7) vanishes. Its right side
does not vanish. Thus
\[
(B_1,C_1)L[v]=L[v].
\tag{8}
\]
The evaluation of a formed coefficient identity does not require
differentiating a moving geometric root.

Let \(\Phi\) generate the full prime kernel of
\(L[U,V]\to L[v]\), \((U,V)\mapsto(y,\zeta)\).
Factor \(\mathcal H=\Phi^r Q\), with \(\Phi\nmid Q\).
If \(r\ge2\), both evaluated gradients are zero, contradicting (8).
If \(Q(y,\zeta)\) had a geometric zero, the two gradients would
again vanish there. Consequently
\[
\mathcal H=\Phi Q,\qquad Q(y,\zeta)\in L^* .
\tag{9}
\]
This is an evaluated-unit statement. It does not initially make
\(Q\) constant as a formal polynomial.

We will also use
\[
\deg\Phi=\max(\deg_v y,\deg_v\zeta)\le3.
\tag{10}
\]
Here and below a constant entry has degree zero. To prove the
equality, adjoin an indeterminate \(s\) and set \(\omega=sy+\zeta\).
Its degree in \(v\) is the maximum on the right. The polynomial-map
degree formula gives
\([L(s)(v):L(s)(\omega)]=\deg_v\omega\).
On the other hand, \(\Phi(U,\omega-sU)\) remains irreducible
over \(L(s,\omega)\), and has \(U\)-degree \(\deg\Phi\), since its
leading coefficient is \(\Phi_{\deg\Phi}(1,-s)\ne0\).
The equality \(L(y,\zeta)=L(v)\) identifies these two extensions.
This proves (10), including the case of a constant first entry.
The polynomial-map degree formula itself follows from irreducibility
of \(p(V)-T\) in \(L[V,T]\) and Gauss's lemma.

As another consequence of (9), if \(\deg\Phi\ge2\), then \(Q\)
is actually constant: its degree is at most one, while
\(Q-Q(y,\zeta)\) belongs to \((\Phi)\).

## 3. A genuine cubic with a nonzero square coefficient is impossible

Suppose that
\[
m_\lambda\ne0,\qquad \mathcal D\ne0 .
\tag{11}
\]
Then \(\mathcal H\) has total degree three with leading form
\(\mathcal D U^3/6\), and its \(V^2\) coefficient is the nonzero
field scalar \(m_\lambda/2\).
It is irreducible even over an algebraic closure \(\overline L\).
In fact a reducible cubic has a linear factor. Its leading form
must divide \(U^3\), so it is a multiple of \(U-c\).
But \(\mathcal H(c,V)\) cannot vanish identically because its
\(V^2\) coefficient is nonzero. This rules out every such factor.
In particular \(\mathcal H\) is a scalar multiple of \(\Phi\),
and (10) gives maximum parameter degree three.

Let \(r=\deg_v y\) and \(s=\deg_v\zeta\).
The first degree is positive: constant \(y\) would leave a
nonzero quadratic polynomial in the nonconstant \(\zeta\).
If \(r=3\), the \(U^3\) term has parameter degree nine and
cannot cancel any other term. If \(r=1\), then \(s=3\) by (10),
and the \(V^2\) term has degree six with no possible cancellation.
The only remaining balance is
\[
(\deg_vy,\deg_v\zeta)=(2,3).
\tag{12}
\]

This pair cannot generate the entire polynomial line ring.
Translate \(v\) over \(\overline L\) to write \(y=\alpha x^2+\beta\),
\(\alpha\ne0\). Subtract a linear polynomial in \(y\) and a constant
from \(\zeta\), leaving
\(\zeta_1=x(c x^2+e)\), with \(c\ne0\).
These changes preserve the equality of generated rings.
If \(e\ne0\), the two opposite nonzero roots of \(cx^2+e\)
have the same \(y,\zeta_1\), contradicting the polynomial inverse
that expresses \(x\) in them. If \(e=0\), both entries have zero
derivative at \(x=0\). Differentiating that same inverse gives
\(1=0\). This also contradicts whole-plane return.
Base extension is legitimate because the polynomial inverse
already exists over \(L\).

Therefore (11) is impossible. This uses neither an assumed
irreducibility of a general eliminant nor a classification theorem
for arbitrary plane embeddings.

## 4. The nonzero square coefficient gives actual recognition

If \(m_\lambda\ne0\), Section 3 forces
\(\mathcal D=0\). Differentiate this identity with respect to
\(\lambda\); the derivative kills \(q,\rho\). It gives
\(-\rho'''m_\lambda=0\). Hence
\[
q'''=\rho'''=0 .
\tag{13}
\]
The derivative constants of the finite field \(C_0/\mathbb C(t)\)
are exactly \(\mathbb C\). For example, differentiate a monic
minimum polynomial of a derivative-constant element. Minimality
forces every coefficient derivative to vanish; its coefficients
are then complex, and algebraic closedness finishes the assertion.
Integrating (13) by successive subtraction therefore gives
\[
q=c_2t^2+c_1t+c_0,\qquad
\rho=d_2t^2+d_1t+d_0,\qquad c_i,d_i\in\mathbb C .
\tag{14}
\]

This is an original-ring gate, not just a generic field conclusion:
the actual shear
\[
Z_*=Z-c_2Y^2-c_1XY-c_0X^2,\qquad
Z=Z_*+c_2Y^2+c_1XY+c_0X^2
\tag{15}
\]
fixes \(X,Y,W\), verifies both inverse orders, and cancels the
quadratic time coefficient of \(Z\).
Thus \(E^2X=E^2Y=E^2Z_*=0\). The retained
[three-good recognition156](three-good-all-degree-recognition-pass156-working.md)
applies, with no bound on the remaining slot required.
It proves \(A\simeq\mathbb C^{[3]}\).

## 5. A nonconstant first projection is an affine graph

Consider the remaining case \(m_\lambda=0\), and assume \(y\notin L\).
Set
\[
A_1(U)=m_tU+n_\lambda,\qquad
B_0(U)=\frac{\mathcal D}{6}U^3+\frac{k_{tt}}2U^2+n_tU-\ell .
\]
Then (5) is \(A_1(U)V+B_0(U)\).
If \(A_1=0\), its evaluation at nonconstant \(y\) would force
the nonzero polynomial \(\mathcal H\) to vanish identically.
Thus \(A_1\ne0\).

If \(A_1\) is nonconstant, it has one root \(c\in L\).
Over \(\overline L\), the polynomial \(y-c\) has a root.
Evaluating \(A_1(y)\zeta+B_0(y)=0\) at that root proves
\(B_0(c)=0\). Thus \(A_1\mid B_0\) in \(L[U]\).
The same divisibility is automatic when \(A_1\) is constant.
Since \(A_1(y)\ne0\) as a polynomial in the transcendental \(y\),
\[
\zeta=P(y),\qquad P=-B_0/A_1\in L[U],\qquad
\deg P\le3,\qquad L[y]=L[v].
\tag{16}
\]
The final equality forces \(y=\gamma v+\eta\), with
\(\gamma\in L^*\), by polynomial degrees.

The full determinant supplies a further coefficient gate.
As a formal polynomial
\(\mathcal H=A_1(U)(V-P(U))\); on the actual graph, (6) gives
\[
B_1=-A_1(y)P'(y),\qquad C_1=A_1(y).
\]
A nonconstant \(A_1\) would have a root along the affine \(y\),
violating (8). Consequently
\[
m_\lambda=m_t=0,\qquad m\in\mathbb C,\qquad
n_\lambda\ne0,\qquad
P(U)=-\frac{\mathcal D U^3/6+k_{tt}U^2/2+n_tU-\ell}{n_\lambda}.
\tag{17}
\]
Joint constants in \(L\) are complex by the same monic-minimum-polynomial
argument, now differentiated in both \(t,\lambda\).
There is no claim that \(n_\lambda\) is an original-ring unit.

## 6. Constant first projection gives original-ring recognition

Now suppose \(y\in L\), without first imposing \(m_\lambda=0\).
Equation (3) makes \(\zeta\), and hence \(w\), affine with nonzero
slope in \(v\). The same is true of \(z=mw+f(y)\), except that
its slope may vanish. The coefficients
\(\sigma=q'y+k,\theta=\rho'y+\lambda\) belong to \(L\).

Extend \(N\) to \(B=A[u]\) by \(Nu=0\), and set
\[
P_0=aN-N(X)E .
\tag{18}
\]
This is an actual derivation of \(B\): \(a,N(X)\in A\).
It kills \(X\) and \(L\), and, in the containing ring \(L[X,v]\),
it equals \(a\partial_v\) with \(X\) fixed.
It therefore preserves \(B\), is locally nilpotent, and is nonzero.
It commutes with \(E\), since \(N\) does and its two displayed
coefficients are \(E\)-invariant.
The constant-\(y\) formulas give
\[
P_0X=P_0Y=0,\qquad
P_0^2Z=P_0^2W=0,\qquad P_0Z,P_0W\in B\cap L\subset A .
\tag{19}
\]
At least one of the last two entries is nonzero.

Let \(\Delta\) be their gcd in the original UFD \(B\).
Both entries belong to \(\ker P_0\), so factorial closure of an
LND kernel gives \(P_0\Delta=0\). They also belong to \(\ker E\),
so the same argument gives \(E\Delta=0\).
These assertions include the case when one entry is zero,
by using the other nonzero entry.
The derivation \(D=P_0/\Delta\) is a well-defined primitive
\(\mathbb C[X,Y]\)-derivation of \(B\), with
\[
D\Delta=0,\qquad [E,D]=0,\qquad
D\in\operatorname{LND}(B),\qquad D^2Z=D^2W=0 .
\]
Local nilpotence follows from
\(P_0^j(b)=\Delta^jD^j(b)\), not from an unjustified localization.

The exact [Dasgupta--Gupta Lemma 2.3(ii)](https://arxiv.org/html/1701.03635v1)
applies over the UFD \(\mathbb C[X,Y]\). Thus
\(p=DZ,q_1=DW\) belong to \(\mathbb C[X,Y]\).
They also belong to \(A\), because \(P_0Z,P_0W,\Delta\) are
\(E\)-invariant. But
\(\mathbb C[X,Y]\cap A=\mathbb C\): the top homogeneous part of
any nonconstant polynomial in \(X,Y\) has nonzero leading
evaluation, by independence of \(a\tau,b\tau\).
Therefore \(p,q_1\in\mathbb C\), not both zero.

Choose \(\alpha,\beta\in\mathbb C\) with \(\alpha p+\beta q_1=1\).
The actual linear change
\[
J=q_1Z-pW,\quad S=\alpha Z+\beta W,\qquad
Z=\beta J+pS,\quad W=-\alpha J+q_1S
\tag{20}
\]
has both displayed inverse orders. It gives
\(DS=1,DJ=0\), and
\(\ker_B D=\mathbb C[X,Y,J]\), an actual polynomial three-ring.
The coordinate \(J\) is not thereby asserted \(E\)-invariant.

The identity \([E,D]=0\) makes \(E\) restrict to a nonzero LND
\(\overline E\) of this three-ring. It satisfies
\(\overline E X=a\ne0,\overline E^2X=0\).
Let \(g\) be the gcd of its three coordinate images.
It divides the nonzero invariant \(a\), so factorial closure
gives \(\overline E g=0\).
Thus \(\delta=\overline E/g\) is an irreducible LND with
\(\delta X\ne0,\delta^2X=0\) and the same kernel as \(\overline E\).

[Daigle's theorem, as stated in Dasgupta--Gupta Theorem 4.8](https://arxiv.org/html/1701.03635v1),
now supplies an invariant coordinate \(I\) of
\(\mathbb C[X,Y,J]\). Since \(B=\mathbb C[X,Y,J][S]\), it is an
actual coordinate of \(B\), and \(EI=0\).
This separate step is essential; \(D\)-invariance of \(J\) alone
would not give it.
Finally \(A\simeq B/(u)\) is regular because \(Eu=1\).
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies to the nonzero \(\mathbb C[I]\)-linear LND \(E\), and yields
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.
\tag{21}
\]
The three exact published statements were freshly read for this
application; their historical proofs are retained inputs.

## 7. The precise surviving actual normalization

The only branch not recognized above satisfies (16)--(17).
Its complex constant \(m\) permits the actual linear shear
\[
Z_*=Z-mW,\quad W_*=W,\qquad
Z=Z_*+mW_*,\quad W=W_* .
\tag{22}
\]
If \(q-m\rho=0\), the new \(Z_*\) has time degree at most one,
and156 again recognizes the kernel. Otherwise the exact1122
profile is retained. The literal new partial
\(\partial_{Z_*}=\partial_Z\), so its shift, \(N\), \(L\), \(v\),
and \(\lambda=\theta-\rho'y\) are unchanged.
The new coefficients satisfy
\[
q_*=q-m\rho,\qquad k_*=k-m\lambda,\qquad
(k_*)_\lambda=0,\qquad
z_*=\frac{q_*''}{2}y^2+(k_*)_t y+n .
\tag{23}
\]
These statements follow by substituting (22) into the entire
actual map (3), not only into its leading terms.
The two good slots and \(W_*\) are unchanged, and the invertible
weighted linear change transports the height-two initial ideal.

Thus any still-unrecognized shift-two case can be studied with
\(m=0,k_\lambda=0,n_\lambda\ne0\), affine \(y\), and the graph
(17) of degree at most three. The remaining scalar equations
and original-ring coordinate return have not been solved here.
The separate shift pair \((1,1)\), arbitrary entry, and higher
time profiles are outside this reduction.

## Verification boundary

The complete250 and the retained three-good156 statement were
read before this argument. An independent unsaved symbolic
calculation reconstructs the raw \(X^2\) coefficient, reduced
determinant, primitive, centered cubic and both gradients.
Those finite identities do not prove field return, the plane-curve
argument, primitive descent, or the published recognition inputs.
No saved checker was executed, imported or compiled, no earlier
source was edited, and no verification packet or index was changed.
This is a restricted working proof, not human expert review,
proof-assistant certification, novelty clearance, or a solution
of unrestricted cancellation.
