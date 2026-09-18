# Actual recognition of the normalized f=q quadratic-projection branch

Status: bounded working proof, pending independent saved-source review.
In the actual \(Z^2-X^3Y\) configuration, the normalized \(f=q\)
quadratic-projection branch has a polynomial inverse to four translation
coordinates. Its kernel is therefore a polynomial three-ring directly.
The same formulas give explicit actual examples, so this branch is
not excluded. This note is separate from the pass196 packet.

## 1. Actual normalized input and the remaining square alternative

Retain the actual hypotheses and exact fields of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
and [nonzero-R195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
q^2=t,\qquad a_E=EX\in L^*,\\
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\quad Nv=1,\\
K=\ker_L\partial_\rho,\quad [K:\mathbb C(q)]<\infty,\qquad
\ker_K\partial_q=\mathbb C,\\
Y=y+q^2X,\qquad
Z=z+\left(\frac{y}{2q}+k\right)X+qX^2,\qquad
W=w+\vartheta X+\rho X^2,\\
L[y,\vartheta]=L[v],\qquad L[y,z,w]=L[v],\qquad
\mathbb C(y,z,w)=L(v),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a_E^3\in L^*.
\end{gathered}
\tag{1}
\]
The determinant holds for every \(X\). The ideal displayed here is
the full initial kernel. The two ratios \(t,\rho\) are independent.
All entries \(y,z,w\) are the projected entries from an actual polynomial
frame, not freely chosen coefficient functions.

Assume the actual normalization
\[
R=q^{-1},\qquad
k=\frac{\rho}{q},\qquad n=-\frac{\rho^2}{2q^3},\qquad
\ell=-\frac{\rho^3}{2q^5}+l,\quad l\in K,\qquad f=1/R=q .
\tag{2}
\]
For the monomial family \(f=\beta_0q\), \(\beta_0\in\mathbb C^*\),
the original polynomial changes leading to the first three identities
are the explicit maps in
[actual normalization196](weight-four-square-root-monomial-actual-normalization-pass196-working.md).
The formula for \(\ell\) follows from the bare normalized coefficient
equations, before imposing \(B_1=0\) or \(B_1\ne0\).
Their actual inverses and preservation of the exact profile and entire
initial ideal are inputs of that normalization lemma.
Here we treat only the quadratic-projection alternative \(B_1\ne0\).
We do not assert that the other reciprocal families admit (2).

In this note a subscript \(q\) or a dot differentiates \(q\), holding
\(\rho\) fixed and extending to the exact algebraic fields.
The old derivative is \(\partial_t=(2q)^{-1}\partial_q\).
The symbols \(q\) and the projected \(z\) are not assumed to belong
to the original polynomial ring. That fact will follow from the inverse.

## 2. Literal projected formulas and the completed-square coefficient

Put \(g=ql\in K\), and introduce the generic-line polynomial
\[
P(U)=\frac{(U+2\rho)^2}{8q^2},\qquad
\zeta=\vartheta-P(y).
\tag{3}
\]
The second and third universal potentials respectively give
\[
z=\frac{\zeta}{q},\qquad
w=\frac{(y/2+\rho)\zeta}{q^2}+g .
\tag{4}
\]
For example
\(z=q^{-1}\vartheta-(y+2\rho)^2/(8q^3)\).
For the third potential, its cubic polynomial is
\[
S(U,V)=\frac{(U+2\rho)^3-8\rho^3}{16q^5}
                -\frac{(U+2\rho)V}{2q^3};
\]
substitution in \(Rw+S(y,\vartheta)=\ell\) gives (4).

For an independent check of the remaining square coefficient, the
cleared fourth-potential eliminant is
\[
\begin{aligned}
\mathcal H(U,V)
&=-\frac{(V-P(U))^2}{2q^4}
  -\frac{g_q}{2q^3}U
  +\frac{5\rho^4}{8q^8}-\frac{\rho g}{q^4}-\frac m q,\\
B_1&=-\frac{g_q}{2q^3}.
\end{aligned}
\tag{5}
\]
Here \(m\in L\) is the fourth scalar potential; \(\mathcal H(y,\vartheta)=0\).
Indeed its uncleared expression is
\((R'U+n_\rho)w+H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m\),
with \(w=(\ell-S)/R\), and (5) is this expression multiplied by \(R\).
All partials in these formulas are coefficient partials before
evaluation. In particular \(B_1\ne0\) means \(g_q\ne0\).

The quadratic-projection equation becomes
\[
y=-\frac{\zeta^2}{qg_q}+\mathcal B(q,\rho),\qquad
\mathcal B=\frac{5\rho^4}{4q^5g_q}
          -\frac{2\rho g}{qg_q}-\frac{2q^2m}{g_q}\in L .
\tag{6}
\]
Since \(\vartheta=\zeta+P(y)\), (6) and the whole-plane equality in
(1) give \(L[\zeta]=L[v]\). Therefore \(\zeta\) is affine over \(L\),
and \(\nu:=N\zeta\in L^*\).
Changing coefficient coordinates from \(t\) to \(q\), and the generic
line parameter from \(v\) to \(\zeta\), preserves the actual scalar
determinant:
\[
\det\frac{\partial(Y,Z,W)}{\partial(q,\rho,\zeta)}
  =-\frac{2q\,a_E^3}{\nu}\in L^* .
\tag{7}
\]
Although the new coefficient partials fix \(\zeta\), derivatives of
elements of \(L\) are unchanged; their extensions to \(L(\zeta)\) are
the ones used from now on. No factor \(\nu\) is replaced by one.

## 3. The projected scalar Jacobian forces g to be quadratic

At \(X=0\), use (4) with \(a=y/2+\rho\). Subtracting
\(\zeta\,dy/(2q^2)+(a/q)\,dz\) from the differential of \(w\)
gives the row \((g_q-a\zeta/q^3,\zeta/q^2,0)\).
Thus the exact determinant is
\[
J_0=\frac{y_\rho g_q}{q}
 -\frac{\zeta}{2q^4}
       \left(2q y_q+(y+2\rho)y_\rho+2\zeta y_\zeta\right).
\tag{8}
\]
Substitution of (6) leaves just the following odd coefficients and
constant term:
\[
\begin{gathered}
[\zeta^3]J_0
 =-\frac{2qg_{qq}-\mathcal B_\rho g_q-2g_q}
          {2q^5g_q^2},\\
[\zeta]J_0
 =-\frac{2q\mathcal B_q+2\rho\mathcal B_\rho
                       +\mathcal B\mathcal B_\rho}{2q^4},\qquad
[\zeta^0]J_0=\frac{\mathcal B_\rho g_q}{q}.
\end{gathered}
\tag{9}
\]
The independence of \(\zeta\) and the nonzero scalar (7) therefore give
\[
\begin{gathered}
\mathcal B=u\rho+v_0,\qquad
u=\frac{2qg_{qq}}{g_q}-2\in K^*,\quad v_0\in K,\\
2qu_q+2u+u^2=0,\qquad 2q(v_0)_q+u v_0=0.
\end{gathered}
\tag{10}
\]
The integration in \(\rho\) takes place in the original exact field:
\(\mathcal B-u\rho\) is killed by \(\partial_\rho\), so belongs to \(K\).
No rationality of \(K\) has been assumed.

Direct differentiation of the expression for \(u\) gives
\[
2qu_q+2u+u^2=\frac{4q^2g_{qqq}}{g_q}.
\tag{11}
\]
The exact constants of \(K\) now imply
\[
\begin{gathered}
g=\alpha q^2+\beta q+\gamma,\qquad
\alpha,\beta,\gamma\in\mathbb C,\quad \beta\ne0,\\
u=-\frac{2\beta}{2\alpha q+\beta},\qquad
v_0=\frac{\delta q}{2\alpha q+\beta},\quad\delta\in\mathbb C .
\end{gathered}
\tag{12}
\]
For the first assertion, subtract a quadratic polynomial after three
successive derivative-constant equations. The condition \(u\ne0\)
forces \(\beta\ne0\). The last assertion includes \(v_0=0\):
the second equation of (10) says precisely that
\(((2\alpha q+\beta)v_0/q)_q=0\).

## 4. Exact field return removes the quadratic term

Since \(\zeta=qz\), equations (6) and (12) give
\[
\begin{gathered}
(2\alpha q+\beta)y=-qz^2-2\beta\rho+\delta q,\\
\rho=\frac{q(\delta-z^2)-(2\alpha q+\beta)y}{2\beta},\\
w=\frac{z(\delta-z^2-2\alpha y)}{2\beta}
          +\alpha q^2+\beta q+\gamma .
\end{gathered}
\tag{13}
\]
In particular \(y,z\) are independent over \(K\): \(z=\zeta/q\)
is transcendental over \(L\), and the first equation is an invertible
linear change between \(\rho\) and \(y\) over \(K(z)\).
Initially \(L/K(\rho)\) can be a proper finite extension. But (1) and
(13) give the inclusions, in the same actual field,
\[
L(z)=\mathbb C(y,z,w)\ \subseteq\ K(y,z)=K(\rho,z)
                                      \ \subseteq\ L(z).
\tag{14}
\]
They are equalities. Comparing rational functions in the independent
variable \(z\) also gives \(L=K(\rho)\).

The first term in the last line of (13) is a complex polynomial in
\(y,z\). Removing it from the returned field yields
\[
K(y,z)=\mathbb C(y,z,g(q)),\qquad K=\mathbb C(g(q)).
\tag{15}
\]
The second equality follows by intersecting with \(K\), using the
independence of \(y,z\). Since \(q\in K\) and \(g(q)\in\mathbb C(q)\),
it follows that
\(\mathbb C(q)\subseteq K=\mathbb C(g(q))\subseteq\mathbb C(q)\).
If \(\alpha\ne0\), the nontrivial automorphism
\(q\mapsto-\beta/\alpha-q\) of \(\mathbb C(q)\) fixes \(g(q)\).
It contradicts \(\mathbb C(q)=\mathbb C(g(q))\).
Consequently
\[
\alpha=0,\qquad K=\mathbb C(q),\qquad
g=\beta q+\gamma,\qquad
y=-\frac{\zeta^2}{\beta q}-2\rho+\frac{\delta q}{\beta},
\quad\beta\in\mathbb C^*.
\tag{16}
\]
This is the actual-field step; the scalar equations alone allowed
the quadratic term \(\alpha q^2\).

## 5. An explicit original polynomial inverse

Set \(H_0=(\delta-z^2)/(2\beta)\). Using (4), (16), and the actual
chart in (1) gives
\[
\begin{gathered}
\rho=qH_0-y/2,\qquad
\vartheta=qz+H_0^2/2,\qquad w=H_0z+\beta q+\gamma,\\
Y=y+q^2X,\qquad Z=z+H_0X+qX^2,\\
W=H_0z+\beta q+\gamma+(qz+H_0^2/2)X
                         +(qH_0-y/2)X^2 .
\end{gathered}
\tag{17}
\]
At this point \(q,y,z\) are still merely known to be invariant
rational functions. Define the following actual polynomials in
the original ring, in the indicated order:
\[
\begin{aligned}
J&=\frac{\delta-Z^2+X^3Y+2X(W-\gamma)}{2\beta},\\
z_*&=Z-XJ,\\
q_*&=\frac{W-\gamma-z_*J-XJ^2/2+X^2Y/2}{\beta},\\
y_*&=Y-q_*^2X.
\end{aligned}
\tag{18}
\]
Only the nonzero complex constant \(\beta\) is inverted.

Substituting (17) into the first line gives \(J=H_0+qX\).
The second line then returns \(z_*=z\). Rewrite the last line of (17)
as
\[
W-\gamma=\beta q+zJ+\frac X2J^2-\frac{X^2}{2}Y.
\tag{19}
\]
The remaining inverse formulas give \(q_*=q\), \(y_*=y\).
This verifies inverse-after-forward.

For the opposite order, start with arbitrary independent \(X,Y,Z,W\)
and the polynomials (18). Direct expansion, using the definition of
\(J\), gives
\[
\delta-z_*^2=2\beta(J-q_*X).
\tag{20}
\]
Thus \(H_*=(\delta-z_*^2)/(2\beta)=J-q_*X\).
It follows successively that
\(Z=z_*+H_*X+q_*X^2\), \(Y=y_*+q_*^2X\), and, by the defining
formula for \(q_*\),
\[
W=\gamma+\beta q_*+z_*J+\frac X2J^2-\frac{X^2}{2}Y .
\]
Replacing \(J\) by \(H_*+q_*X\) and \(Y\) by \(y_*+q_*^2X\)
is exactly the forward formula (17). This proves
forward-after-inverse without dividing by \(X\).

We have proved
\[
B=\mathbb C[X,y,z,q],\qquad y,z,q\in\mathcal A.
\tag{21}
\]
In these polynomial coordinates \(E=a_E\partial_X\), where
\(a_E\in\mathbb C[y,z,q]\setminus\{0\}\).
The given global slice satisfies
\(1=Eu=a_E\,\partial_Xu\); hence \(a_E\) is a nonzero complex constant.
It follows directly that
\[
\mathcal A=\mathbb C[y,z,q]\cong\mathbb C^{[3]} .
\tag{22}
\]
No additional recognition theorem is needed for this normalized branch.
For example \(z=Z-XJ\) in (18) is the proposed invariant polynomial,
and (18) additionally recovers \(q\) and \(y\) polynomially.
It is the inverse proof, not an initial coefficient-field interpretation,
that establishes their original-ring membership.

## 6. Actual nonvacuity and the entire initial kernel

Conversely choose arbitrary complex \(\gamma,\delta\) and
\(\beta\ne0\), and take independent variables \(x,y,z,q\).
Define \(X=x\) and \(Y,Z,W\) by (17). The two inverse orders just
proved show this is a polynomial automorphism.
The derivation \(E=\partial_x\), fixing \(y,z,q\), has global slice
\(X\), and
\[
EX=1,\qquad EY=q^2,\qquad
EZ=H_0+2qX,\qquad
EW=qz+H_0^2/2+2(qH_0-y/2)X .
\tag{23}
\]
All right sides are actual polynomials through (18).
The exact time degrees are \((1,1,2,2)\), with ordinary leading
coefficients \(1,q^2,q,\rho\), where \(\rho=qH_0-y/2\ne0\).
The elements \(q,\rho\) are independent.

For an independent leading-time symbol \(\xi\), the initial map is
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto
(\xi,\ q^2\xi,\ q\xi^2,\ \rho\xi^2).
\tag{24}
\]
Its fraction field is \(\mathbb C(\xi,q,\rho)\), of transcendence
degree three: one recovers \(q=\mathsf Z/\mathsf X^2\) and
\(\rho=\mathsf W/\mathsf X^2\) in the image fraction field.
Its prime kernel therefore has height one.
The relation \(\mathsf Z^2-\mathsf X^3\mathsf Y\) is irreducible:
as a polynomial in \(\mathsf Y\), its two coefficients
\(-\mathsf X^3,\mathsf Z^2\) are coprime, and it is linear over
the fraction field of the other variables.
Gauss's lemma proves that it generates the entire initial kernel.
This is a written dimension/irreducibility proof, not a finite-check
inference from one vanishing relation.

For calibration, direct differentiation of the inverse (18) gives
\[
\begin{gathered}
\partial_Zz=1+\frac{XZ}{\beta},\qquad
\partial_Zq=-\frac J\beta+\frac{zZ}{\beta^2},\qquad
\partial_Zy=-2qX\,\partial_Zq,\\
N=[X^3](\partial_Z|_{\mathcal A})
 =\frac q\beta\,\partial_z-\frac{2q^2z}{\beta^2}\,\partial_y,\qquad
Nq=N\rho=0,\quad N\zeta=\frac{q^2}{\beta}.
\end{gathered}
\tag{25}
\]
In the actual invariant coordinates \(q,\rho,z\),
\(N=(q/\beta)\partial_z\); hence \(L=\mathbb C(q,\rho)\),
and \(v=\beta z/q\) satisfies \(Nv=1\) over \(L\).
The projected determinant in \((q,\rho,\zeta)\) is
\(-2\beta/q\), agreeing with (7), since here \(a_E=1\).
The literal normalized third potential has \(l=\beta+\gamma/q\)
and \(B_1=-\beta/(2q^3)\ne0\).
Its fourth scalar is
\(m=5\rho^4/(8q^7)-\gamma\rho/q^3-\delta/(2q)\), from (5)--(6).

The simplest example takes \(\beta=1,\gamma=\delta=0\):
\[
\begin{aligned}
X&=x,&Y&=y+q^2x,\\
Z&=z-\tfrac12z^2x+qx^2,\qquad&
W&=q-\tfrac12z^3+
       \left(qz+\tfrac18z^4\right)x
       -\tfrac12(y+qz^2)x^2 .
\end{aligned}
\tag{26}
\]
The inverse remains the polynomial formula (18) with these constants.
This is an actual quadratic-projection example, not just formal
solutions of the coefficient ODEs.

## Scope

The conclusion applies to the actual normalized monomial \(f=q\)
quadratic-projection branch, and composes with the actual monomial
normalization after its hypotheses are checked.
It does not treat the nonmonomial family \(f=at+bq\) with \(a\ne0\),
the reciprocal monomial family \(f=b/q\), the second-cover nonzero-R
branches, higher profiles, arbitrary entry, or unrestricted cancellation.
The actual normalization's graph subbranch is separate.

The saved normalization196 and nonzero-R195 sources were fully read
before this proof was saved. The projected identities, scalar Jacobian,
field intersection and both original inverse orders were independently
reconstructed here. No saved checker was executed, imported, compiled,
or changed; no196 or earlier artifact was edited.
This is a bounded working proof, not historical novelty clearance,
public submission, proof-assistant certification, or human expert review.
