# The split nonzero-R chart reduces to quartic or quadratic alternatives

Status: working reduction for the supplied actual split-quartic frame.
Constant projection is excluded. The quartic leading coefficient cannot
vanish. Three geometric alternatives remain, and only the pure-quartic
alternative is forced to have reciprocal-affine R by this note.
The two quadratic alternatives are not excluded.

## 1. Hypotheses and the multiplier obstruction

Retain the actual frame and all field/projection hypotheses (1)--(2)
of [split zero-R192](weight-four-split-zero-r-coordinate-recognition-pass192-working.md),
but replace its branch condition by \(R=k_\rho\ne0\). Thus

\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X\mathsf Y\mathsf Z+\mathsf X^4+\mathsf Y^4),
\qquad q=-t^3-t^{-1}.
\tag{1}
\]

In particular the selected actual LND \(N\), the exact finite field
\(L/\mathbb C(t,\rho)\), the entire generic-line ring
\(L[y,z,w]=L[v]\), the equality \(\mathbb C(y,z,w)=L(v)\),
and the full \(X\)-independent determinant are supplied by
[universal184](weight-four-universal-chart-potentials-pass184-working.md).
The ratios \(t,\rho\) are independent, \(Nv=1\), and the speed
\(\mathfrak a=EX\in L^*\) is not declared an original-ring unit.

Here is the elementary replacement for the two literal \(t^4\)
comparisons in the earlier constant-projection argument. If
\(l(t)=a+bt\in\mathbb C[t]\setminus\{0\}\) has degree at most one, then

\[
l(t)q(t)=-bt^4-at^3-b-a/t
\quad\hbox{is not a polynomial of degree at most three.}
\tag{2}
\]

If \(a\ne0\), its nonzero pole at zero prevents polynomiality.
If \(a=0\), then \(b\ne0\) and the degree is four.
For a nonzero constant multiplier it is not a polynomial of any degree.
No algebraic coefficient-field extension changes this rational identity.

## 2. Constant y is excluded in the original ring

Suppose \(y\in L\). Reconstruct Sections 1--4 of
[constant projection188](weight-four-absent-variable-constant-projection-exclusion-pass188-working.md)
with general \(q(t)\). The ingredients before its two leading-degree
comparisons do not require \(q=t^4\); the following reconstruction
identifies the only coefficients that change.

The potentials and whole-line equality give

\[
z=R\vartheta+A_0,\qquad
w=\alpha\vartheta^2+\beta\vartheta+g,\qquad
L[\vartheta]=L[v],\qquad N\vartheta=\gamma\in L^*.
\tag{3}
\]

The old \(y_\rho\) is nonzero, or the first row of the full determinant
would be \((X+y_t,0,0)\), making the determinant divisible by a
nonconstant polynomial in \(X\). Use the commuting coefficient
partials for \(L/\mathbb C(t,y)\), fixing \(X,\vartheta\).
Their joint constants are \(\mathbb C\).
In the literal determinant of188, replace \(4t^3\) by \(q'\).
This changes only the term \(X^2(K_{0,y}-q')\) in its braces.
The coefficients of \(\vartheta^2\) and \(X\vartheta^2\) are unchanged.
They give
\(R\alpha_t-2\alpha R_t=R\alpha_y-2\alpha R_y=0\), hence
\(\alpha=cR^2\), \(c\in\mathbb C\).

Extend the actual \(N\) to \(A[u]\) fixing \(u\), and set
\(\mathscr P=\mathfrak aN-(NX)E\).
It is an actual LND fixing \(X,Y\): on \(B_{\mathfrak a}=A_{\mathfrak a}[X]\)
it fixes \(X\) and acts as \(\mathfrak aN\) on coefficients.
It commutes with \(E\).
Primitive division by its coefficient gcd gives an irreducible
LND \(D\) with

\[
DX=DY=0,\quad DZ\ne0,\quad D^2Z=0,\quad
D^3W=0,\quad D^2W/(DZ)^2=2c,\quad [E,D]=0,
\quad D(EX)=D(EY)=D(E^2Z)=D(E^2W)=0.
\tag{4}
\]

For clarity, primitive division here has an actual-ring proof.
If \(\mathscr P=\Delta D\), LND degree applied to
\(\mathscr P\Delta=\Delta D\Delta\) makes \(D\Delta=0\);
then \(\mathscr P^j=\Delta^jD^j\) on elements.
Commutation gives
\((E\Delta)D+\Delta[E,D]=0\).
Primitivity implies \(\Delta\mid E\Delta\), prime by prime in \(B\).
The same LND-degree argument makes \(E\Delta=0\), so \([E,D]=0\).
Thus no generic partial was substituted for an actual derivation.

[Dasgupta--Gupta, Lemma 2.3(i)](https://arxiv.org/pdf/1701.03635v1)
over the UFD \(\mathbb C[X,Y]\) gives
\(DZ=B_0(X,Y)\ne0\) and \(DW\in\mathbb C[X,Y,Z]\).
Equation (4) then yields

\[
DW=2cB_0Z+C_0(X,Y),\qquad
E^2B_0=E^2(DW)=0,\qquad \deg B_0\le1.
\tag{5}
\]

A polynomial in \(X,Y\) has ordinary degree equal to its E-degree:
its top part gives the nonzero value
\(\mathfrak a^j H_j(1,t)\), since \(t\) is transcendental.
If \(c\ne0\) and \(j=\deg B_0\in\{0,1\}\), equation (5) would
force \(C_0\) to have degree \(j+2\) and
\(2cB_{0,j}(1,t)q+C_{0,j+2}(1,t)=0\).
For \(j=0\), (2)'s constant case excludes this.
For \(j=1\), (2) excludes the degree-at-most-three right side.
Thus \(c=0\), and \(C_0\) is affine or zero.
Primitivity now says \(\gcd(B_0,C_0)=1\).

The actual invariant three-ring of \(D\) is

\[
\ker_BD=\mathbb C[X,Y,F],\qquad F=B_0W-C_0Z.
\tag{6}
\]

Here is the needed descent, not an assumed generic equality.
If \(B_0,C_0\) generate the unit ideal, their affine form gives
complex \(\lambda,\mu\) with \(\lambda B_0+\mu C_0=1\).
Then \(T=\lambda Z+\mu W\) has the two-sided inverse
\(Z=B_0T-\mu F,\ W=C_0T+\lambda F\), and \(D=\partial_T\).
Otherwise their linear parts are independent; a dependent affine
pair would have a common factor or a nonzero constant combination.
They form affine coordinates of \(\mathbb C[X,Y]\).
Localizing at \(B_0\) gives kernel \(\mathbb C[X,Y]_{B_0}[F]\).
Modulo \(B_0\), \(F\mapsto-\overline C_0Z\) is injective on
\((\mathbb C[X,Y]/(B_0))[F]\).
A least denominator-power argument gives (6).

The restriction of \(E\) to (6) is a nonzero LND with \(E^2X=E^2Y=0\).
After primitive division, Wang's two-coordinate theorem,
[Dasgupta--Gupta, Theorem 4.1](https://arxiv.org/pdf/1701.03635v1),
either gives an invariant nonzero complex linear form in \(X,Y\),
which contradicts transcendental \(t=EY/EX\), or an invariant
\(\xi=c_0F+H(X,Y)\), \(c_0\in\mathbb C^*\).
For the second alternative:

* If \(B_0\) is nonconstant, the degree-three leading coefficient of
  \(F\) contains the nonzero term \(B_{0,1}(1,t)\rho\); independence
  of \(t,\rho\) prevents cancellation by a cubic \(H\).
* If \(B_0\) is constant and \(C_0\) is nonconstant, the degree-three
  coefficient is \(-C_{0,1}(1,t)q\), which (2) prevents a cubic \(H\)
  from canceling.
* If both are constant, the degree-two coefficient
  \(B_0\rho-C_0q\) has nonzero \(\rho\) coefficient.

These cases exhaust the affine pair, including \(C_0=0\).
Therefore \(y\notin L\).

## 3. The rho derivative and the nonvanishing quartic top

The statement of [nonzero-R rigidity188](weight-four-absent-variable-nonzero-r-rigidity-pass188-working.md)
already treats general \(q_\rho=0,q'''\ne0\), not merely \(q=t^4\).
It applies now and gives \(R_\rho=0\).
Set \(K=\ker_L\partial_\rho\), so \(K/\mathbb C(t)\) is finite,
its derivative constants are \(\mathbb C\), and
\(k=R\rho+k_0\), with \(R\in K^*, k_0\in K\).

Use the eliminant \(\mathcal H\) defined in (2) of
[split counterexample192](weight-four-split-nonzero-r-ode-counterexample-pass192-working.md).
The general actual determinant proof in188 gives

\[
L[y,\vartheta]=L[v],\qquad
0\ne\mathcal H=\omega G+G^2D_0,\qquad
\omega\in L^*,\quad D_0\in L[U,V],
\tag{7}
\]

where \(G\) generates the entire plane kernel. Its top form over
\(\overline L\) is a power of one linear form, because the actual
polynomial parametrization has only one point at infinity.
Put \(d=q'''/6=t^{-4}-1,\ e=d'/4=-t^{-5}\).
The top coefficients are

\[
C_4=eR-dR',\qquad
\Delta=RR''/2-(R')^2,\qquad
\mathcal H_4=C_4U^4,\qquad
[U^2V]\mathcal H=\Delta,\quad \deg_V\mathcal H\le2.
\tag{8}
\]

If \(C_4=0\), then \(R'/R=d'/(4d)\). Differentiation gives

\[
\Delta=\frac{R^2(4dd''-5(d')^2)}{32d^2}
       =-\frac{5R^2}{2t^6d^2}\ne0,
\qquad 4dd''-5(d')^2=-80t^{-6}.
\tag{9}
\]

These identities hold over the exact algebraic \(K\); no rational
solution assumption is involved.
Then \(\mathcal H\) has degree three, with top
\(U^2(C_3U+\Delta V)\), having two distinct linear factors.
If \(\deg G=3\), this contradicts its one-point-at-infinity property.
If \(\deg G=2\), the degree-one cofactor and (7) force a constant
cofactor, contradicting degree three.
If \(\deg G=1\), (7) forces the square of its leading linear form
to divide the cubic top. That form must be \(U\), hence \(y\in L\),
already excluded. Thus

\[
C_4\ne0,\qquad \deg\mathcal H=4,\qquad
\mathcal H_4=C_4U^4.
\tag{10}
\]

## 4. Exactly three remaining geometric alternatives

The degree argument of Section 4 of
[quartic reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md)
now applies to (7),(10) without using its later specialized ODE.
For completeness, \(\deg_vy=\deg_VG\le2\):
the ring equality makes \(G\) the minimal relation of
\(\vartheta\) over \(L(y)\), and a degree-m polynomial \(y(v)\)
gives field degree m over \(L(y)\).
A linear \(G\) would force constant \(y\), and degree three would
force a constant cofactor in (7), contradicting degree four.

If \(y\) is affine, then \(\vartheta=P(y)\), and \(\deg P=2\) or 4.
Degree four makes the cofactor constant; degree two permits exactly
the nonzero constant square term in (7).
If \(y\) is quadratic, translating \(v\) writes
\(y=a_0v_0^2+b_0\), and
\(\vartheta=P(y)+v_0Q(y)\).
Over \(\overline L\), a root of \(Q\) away from \(b_0\) would identify
two line parameters, and a root at \(b_0\) would make both derivatives
vanish. Either contradicts the polynomial inverse.
Thus \(Q\) is a nonzero constant in \(L\).
The V-degree-two bound excludes \(G^2D_0\).
Consequently the alternatives are exactly

\[
\begin{array}{ll}
\text{pure quartic:}&
 \mathcal H=\omega(V-P_4(U)),\quad \deg P_4=4,\quad y\text{ affine};\\
\text{quadratic graph:}&
 \mathcal H=\omega(V-P_2(U))+A_2(V-P_2(U))^2,\quad
 \deg P_2=2,\quad y\text{ affine};\\
\text{quadratic projection:}&
 \mathcal H=A_2((V-P_2(U))^2-a_2U-b_2),\quad
 \deg P_2=2,\quad \deg_v y=2,
\end{array}
\tag{11}
\]

where \(\omega,A_2,a_2\) are nonzero in the alternatives where
they occur. In the last line \(b_2\in L\) is unrestricted.
Every parameter change in this classification is over \(L\);
it is not an original polynomial-coordinate change.

Only in the pure-quartic alternative does coefficient comparison
give

\[
n_{\rho\rho}=0,\qquad RR''/2-(R')^2=0,\qquad
Rn_{t\rho}-2R'n_\rho=0,\qquad
R=\frac1{\alpha t+\beta},\quad
n=cR^2\rho+n_0,\quad
\alpha,\beta,c\in\mathbb C,\quad n_0\in K.
\tag{12}
\]

Here \((\alpha,\beta)\ne(0,0)\). The middle differential equation
is \((1/R)''=0\); the last says \((n_\rho/R^2)'=0\).
The constants follow in the exact field \(K\).
This supplies the reciprocal gates for a separate pure-quartic
recognition argument, not for either quadratic alternative.

The two quadratic alternatives have the common completed-square
form in192 and therefore its necessary differential equation.
That equation has the nonaffine rational solution \(f=t^5+3t\).
Accordingly no affine-only lemma from the absent-variable case
has been used to discard them. The remaining equations, actual
cofactor and original-ring return still need analysis.

## Scope

This note excludes constant projection and a vanishing quartic
top for the supplied actual split nonzero-R frame, then records
an exhaustive three-case reduction. It does not recognize the
quadratic branches, prove arbitrary coordinate entry, or solve
unrestricted cancellation.
The primary two-variable and two-coordinate theorem statements
were read directly for this application; their published conclusions
are retained, not re-proved here.
No claim of historical novelty, human expert review, proof-assistant
verification, external contact or public submission is made.
No earlier artifact was edited and no checker was run for this note.

