# A sextic plane reduction in the nonconstant-intercept paraboloid branch

Status: a genuine two-generator polynomial-line reduction for the branch
\(k_s=0,\ n_s\ne0\) of the actual principal exact1222 chart264.
Replacing the coefficient parameter \(s\) by \(n\), the \(X^2\)
Jacobian coefficient expresses \(w\) polynomially in \(y,\sigma\).
The remaining \(X\)-coefficient integrates to a nonconstant degree-at-most-six
plane relation, and the nonzero constant coefficient makes its
evaluated gradient ideal the unit ideal.

A further consequence is that if the third \(n\)-derivative of the old
parameter \(s\) is nonzero, then the projected plane curve is a line.
This is not an actual coordinate-recognition endpoint for that line
or for the entire branch. No existing source or checker is changed,
and no saved checker is executed, imported, or compiled.

## 1. Actual entry and exact reparameterization

Retain every actual hypothesis of the fully read
[principal paraboloid chart264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),
\quad \text{full initial kernel }(X^2Z-Y^2).
\tag{1}
\]
The relation in (1) is the full weighted initial relation, not an
identity between the original coordinates. Put \(a=EX\),
\(t=(E^2Y/2)/a^2\), and \(s=(E^2W/2)/a^2\).
The two ratios \(t,s\) are algebraically independent.

The literal \(Z\)-partial has exact horizontal shift four and intrinsic
nonzero LND \(N\) on \(A\), with
\[
Na=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\quad
A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad K=\operatorname{Frac}A=L(v).
\tag{2}
\]
The actual fixed-\(X\) expressions, returns, and calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
K&=\mathbb C(y,z,w),\qquad L[y,z,w]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a^4\in L^* .
\end{aligned}
\tag{3}
\]
All projected coefficients lie in \(L[v]\); \(k,n,\ell\in L\) are
the first and second potential coefficients of264.

Assume
\[
k_s=0,\qquad \nu:=n_s\ne0.
\tag{4}
\]
For the moment the subscripts \(t,s\) are the old coefficient
derivations, which fix \(v\). Let
\(F=\ker_L\partial_s\).
Then \(F/\mathbb C(t)\) is finite, \(k\in F\), and the old
\(t\)-derivative preserves \(F\).

For clarity, the finite-field argument is included. If an element
of \(L\) is killed by \(\partial_s\), differentiating its monic
minimal polynomial over \(\mathbb C(t,s)\) gives a polynomial
of smaller degree vanishing at that element. It must be zero.
The original coefficients therefore belong to \(\mathbb C(t)\).
Thus \(F\) is algebraic over \(\mathbb C(t)\), and is finite because
the relative algebraic closure of \(\mathbb C(t)\) in the finitely
generated field \(K\) is finite. Commutation gives preservation by
\(\partial_t\). The same minimal-polynomial argument shows that the
constants of the induced \(t\)-derivative on \(F\) are \(\mathbb C\).
We do not assume \(F=\mathbb C(t)\).

The condition \(n_s\ne0\) implies that \(n\) is transcendental over
\(F\): a separable algebraic element over \(F\) would be killed by
\(\partial_s\). Hence \(t,n\) form a transcendence basis of \(L\),
and \(L/\mathbb C(t,n)\), as well as \(L/F(n)\), is finite.
Define the new coefficient derivations by
\[
\partial_n=\nu^{-1}\partial_s,\qquad
\partial_t=\partial_t^{\,o}
 -\frac{\partial_t^{\,o}n}{\nu}\partial_s.
\tag{5}
\]
Here \(\partial_t^{\,o}\) denotes the old \(t\)-derivative.
These are the unique extensions of the partials on
\(\mathbb C(t,n)\); they commute by separability. They still fix \(v\),
and
\[
\ker_L\partial_n=F.
\tag{6}
\]
On \(F\), the new \(t\)-derivative equals the old one. Primes on
\(k\) below denote this derivative.

Write the old parameter and a rescaled potential level as
\[
H=s\in L,\qquad T=H_n\ell,\qquad H_n=\nu^{-1}\ne0.
\tag{7}
\]
The old derivative of \(n\) is \(\partial_t^{\,o}n=-H_t/H_n\).
Only a coefficient-field parameter has changed. Neither \(N\),
the actual coordinates, nor the polynomial variable \(v\) has changed.
The determinant transforms by the exact chain rule to
\[
\mathcal J(X):=
\det\frac{\partial(Y,Z,W)}{\partial(t,n,v)}
=-a^4H_n\in L^*.
\tag{8}
\]
In particular it is independent of \(X,v\). The factor \(H_n\)
must not be replaced by a complex unit.

## 2. The second potential and a polynomial formula for \(w\)

For independent formal variables \(U,P\), define
\[
\begin{aligned}
\gamma&=2P+k',\qquad B_1=2U+k''P,\\
\mathscr A&=(2P+k')U+\frac{k''}{2}P^2,\\
\mathscr C&=U^2+k''PU+\frac{k'''}6P^3,\\
g(U,P)&=T+H_tP-H_n\mathscr A.
\end{aligned}
\tag{9}
\]
All subsequent coefficient partials hold \(U,P\) fixed. The two
potentials of264, after (5), read exactly
\[
z=2ty+\sigma^2+k'\sigma+n,\qquad \theta=g(y,\sigma).
\tag{10}
\]
Indeed the old second potential is
\((2\sigma+k')y+k''\sigma^2/2+
(\partial_t^{\,o}n)\sigma+\nu\theta=\ell\).
Multiplication by \(H_n\) gives (10).

Subtracting \(2t\) times the differential of \(Y\) from that of \(Z\),
the three literal fixed-\(X\) rows become
\[
\begin{aligned}
&dy+X\,d\sigma+X^2dt,\\
&\gamma\,d\sigma+B_1\,dt+dn+X\gamma\,dt,\\
&dw+X\,dg+X^2\,dH ,
\end{aligned}
\tag{11}
\]
where formal expressions are evaluated at \((y,\sigma)\).
In particular every coefficient derivative in \(dg,dH\) is retained.

Define the following polynomial of total degree at most four:
\[
\mathscr F=
-\frac{H_{nn}}2\mathscr A^2+
(H_{nt}P+T_n)\mathscr A+
H_n\mathscr C-H_tU-\frac{H_{tt}}2P^2-T_tP.
\tag{12}
\]
The complete coefficient of \(X^2\) in the determinant (11) is
\[
w_v+\mathscr F_U(y,\sigma)y_v+
       \mathscr F_P(y,\sigma)\sigma_v.
\tag{13}
\]
The coefficients of \(X^4\) and \(X^3\) have already vanished by
the two potentials. To check (12)--(13) without a large coefficient
table, put \(\mathscr W=\omega-\mathscr F\), where \(\omega\) is
temporarily any coefficient in \(L\). Direct differentiation gives
\[
\boxed{\mathscr W_U=g_P-\gamma g_n,\qquad
       \mathscr W_P=g_t-B_1g_n.}
\tag{14}
\]
For example \(\mathscr A_U=\gamma\),
\(\mathscr A_P=B_1\), and
\(\mathscr C_P=\mathscr A_t=k''U+k'''P^2/2\).
These identities give (14) with the full derivatives of \(H,T\).
Expanding (11) at \(X^2\) gives
\((w_v-\mathscr W_U y_v-\mathscr W_P\sigma_v)\), which is (13).

Since \(Nv=\partial_vv=1\) on \(L[v]\), (13) integrates with an
exact coefficient-field constant:
\[
\boxed{w=\mathscr W(y,\sigma)=\omega-\mathscr F(y,\sigma),
\qquad \omega\in L.}
\tag{15}
\]
No \(t,n\)-constant or rational-function assumption is imposed on
\(\omega\).

Now the whole-line return in (3) supplies both ring inclusions:
\[
L[y,\sigma]\ \subset\ L[v]=L[y,z,w]\ \subset\ L[y,\sigma].
\]
The second inclusion uses both (10) and (15). Therefore
\[
\boxed{L[y,\sigma]=L[v].}
\tag{16}
\]
This is genuinely a plane presentation, unlike the three-generator
surface relation in the nonzero-coupling part of264.
The original field return \(K=\mathbb C(y,z,w)\) is still retained;
it is not replaced by (16).

## 3. The full remaining \(X\)-coefficient has a sextic primitive

Define two formal polynomials by
\[
Q_U:=\gamma\mathscr W_n-\mathscr W_P,\qquad
Q_P:=B_1\mathscr W_n-\mathscr W_t .
\tag{17}
\]
They have total degree at most five. They are the two derivatives
of a polynomial \(Q\in L[U,P]\). Here is a direct integrability proof:
\[
\begin{aligned}
\partial_P Q_U-\partial_U Q_P
 &=\gamma\mathscr W_{Pn}-B_1\mathscr W_{Un}
       +\mathscr W_{Ut}-\mathscr W_{PP}\\
 &=0 .
\end{aligned}
\tag{18}
\]
In the first equality \(\gamma_P=(B_1)_U=2\) cancels.
For the second, substitute (14). The remaining terms cancel
because \(\gamma_t=(B_1)_P=k''\) and mixed coefficient derivatives
commute. An explicit normalization, using only termwise polynomial
integration, is
\[
Q(U,P)=
\int_0^U Q_U(\xi,P)\,d\xi+
\int_0^P Q_P(0,\pi)\,d\pi,\qquad Q(0,0)=0,\qquad \deg Q\le6.
\tag{19}
\]
This construction is within \(L[U,P]\); no integration in an
algebraic coefficient field is being assumed.

Using the literal rows (11) and substituting (14), every occurrence
of \(y_t,y_n,\sigma_t,\sigma_n\) in the coefficient of \(X\) cancels.
The result is exactly
\[
[X]\mathcal J(X)=Q_U(y,\sigma)y_v+Q_P(y,\sigma)\sigma_v.
\tag{20}
\]
It follows that
\[
Q(y,\sigma)=q_0,\qquad q_0\in L.
\tag{21}
\]
The nonzero assertion for \(Q-q_0\) will follow from the constant
coefficient, not from an unsupported generic-leading assumption.

## 4. The constant coefficient and the unit cofactor

All the subscripts on \(y,\sigma\) below use the new coefficient
basis \((t,n,v)\). Define
\[
\begin{aligned}
D_U&=(B_1y_n-y_t)\sigma_v+(\sigma_t-B_1\sigma_n)y_v,\\
D_P&=(1+\gamma\sigma_n)y_v-\gamma y_n\sigma_v.
\end{aligned}
\tag{22}
\]
The complete constant coefficient of (11) is
\[
\boxed{-a^4H_n
 =Q_U(y,\sigma)D_U+Q_P(y,\sigma)D_P.}
\tag{23}
\]
For an explicit verification, at \(X=0\) the three rows are
\(dy\), \(\gamma\,d\sigma+B_1dt+dn\), and
\(\mathscr W_Udy+\mathscr W_Pd\sigma+
 \mathscr W_tdt+\mathscr W_ndn\).
Expanding their determinant and replacing
\(\mathscr W_P=\gamma\mathscr W_n-Q_U\) and
\(\mathscr W_t=B_1\mathscr W_n-Q_P\)
cancels every term in \(\mathscr W_n\), leaving (23).
No equation in a moving root or uncalibrated volume is used.

Each entry in (22) is in \(L[v]\), since the coefficient
derivations fix \(v\). The left side of (23) is a nonzero element
of \(L\). Consequently
\[
\bigl(Q_U(y,\sigma),Q_P(y,\sigma)\bigr)L[v]=L[v].
\tag{24}
\]
In particular \(Q\) is not constant, and \(Q-q_0\) is a nonzero
polynomial relation.

Let \(G\) generate the kernel of
\(L[U,P]\longrightarrow L[v]\), \((U,P)\mapsto(y,\sigma)\).
By (16), this is a height-one prime ideal, so \(G\) is an
irreducible polynomial over the exact field \(L\).
Write \(Q-q_0=GV\). Evaluating its formal derivatives gives
\(Q_U=V(y,\sigma)G_U\) and \(Q_P=V(y,\sigma)G_P\).
Equation (24) makes \(V(y,\sigma)\) a unit of \(L[v]\), hence
a scalar \(\eta\in L^*\). Thus \(V-\eta\in(G)\), and
\[
\boxed{Q-q_0=\eta G+G^2R,\qquad \eta\in L^*,\quad R\in L[U,P].}
\tag{25}
\]
The cofactor is a unit because of the actual constant Jacobian,
not merely because the plane curve in (16) is smooth.

## 5. A nonzero third parameter derivative forces a projected line

The degree-four part of \(\mathscr W\) in (15) is
\(H_{nn}\mathscr A_2^2/2\), where
\(\mathscr A_2=P(2U+k''P/2)\).
Equations (17) then give the exact top homogeneous part
\[
\boxed{Q_6=\frac{H_{nnn}}6\mathscr A_2^3
       =\frac{H_{nnn}}{48}P^3(k''P+4U)^3.}
\tag{26}
\]
This also follows by differentiating the displayed cubic power.
It retains the coefficient derivative \(H_{nnn}\).

We give the exact-field plane-degree input used here.
For polynomials \(r(v),p(v)\) generating \(L[v]\), cancel equal
leading terms by an \(L\)-linear transformation so their degrees
are \(i<d\). This operation is only in the projected plane.
If \(r\) is constant, generation forces \(d=1\).
Otherwise \(L[v]\) is free of rank \(d\) over \(L[p]\), and
the characteristic polynomial of multiplication by \(r\) is
its minimal polynomial, since \(L(r,p)=L(v)\).
The coefficient of first-variable degree \(d-j\) has
second-variable degree at most \(\lfloor ij/d\rfloor<j\).
Indeed, temporarily over an algebraic closure of \(L\), the
\(d\) roots of \(p(v)=z^{-d}\) have leading form
\(\lambda z^{-1}\) with distinct nonzero \(\lambda\).
Coefficient recursion gives their formal expansions.
Each value of \(r\) has pole order at most \(i\), so its
\(j\)-th elementary symmetric function has pole order at most
\(ij\). It is a polynomial in \(p\), proving the bound.
The relation therefore has total degree \(d\) and pure top
equal to the first variable to the power \(d\).
Transforming back gives
\[
g:=\deg G=\max(\deg_v y,\deg_v\sigma),\qquad
G_g=c_0\Lambda^g,\quad c_0\in L^*,\qquad
0\ne\Lambda\in L[U,P]_1.
\tag{27}
\]
This is the same characteristic-polynomial argument freshly
reread in [235, Section5](rank-one-distinct-root-residue-sextic-line-reduction-pass235-working.md).
No geometric splitting assumption or ambient linear change is needed.

Now assume \(H_{nnn}\ne0\). The two lines in (26) are distinct
over \(L\), since the coefficient of \(U\) in the second is four.
As \(G\mid Q-q_0\), (26),(27) first give \(g\le3\).
But \(\deg Q=6>g\), so the term \(G^2R\) in (25) must be nonzero
and must supply the leading degree six. Consequently
\(\Lambda^{2g}\) divides (26). Both line multiplicities there
are three, hence \(2g\le3\), and \(g=1\).
Thus
\[
H_{nnn}\ne0
\quad\Longrightarrow\quad
\max(\deg_vy,\deg_v\sigma)=1.
\tag{28}
\]
More precisely the line has leading equation either \(P=0\)
or \(4U+k''P=0\). Respectively \(\sigma\in L\), or
\(4y+k''\sigma\in L\). The two projected entries cannot both
be constant because of (16).
Conversely, every nonlinear projected plane component satisfies
\(H_{nnn}=0\). Exact constant-field integration using (6) then gives
\[
H=A_2 n^2/2+A_1n+A_0,\qquad A_i\in F,
\tag{29}
\]
without asserting \(L=F(n)\) or discarding the case \(A_2\ne0\).

## 6. What this does and does not settle

The branch (4) now has an exact two-generator polynomial-line return,
a nonconstant relation of degree at most six, the full remaining
Jacobian identity (23), and the unit-cofactor structure (25).
The high-parameter-derivative branch is forced to a projected line,
and every nonlinear plane branch satisfies the exact quadratic
parameter restriction (29). These are constraints on an actual
frame, not examples of realizability.

No projected line is promoted to an actual ambient coordinate.
In particular (16),(25), and (28) do not on their own prove the
polynomial-entry hypothesis \(W\in F[X,Y,Z]\) of266.
The complete actual field return in (3) remains available for
a later descent argument; no curve-field pencil is invoked
without first proving its membership hypothesis.
Recognition in either remaining subcase is left open.

The complete264 and262 sources were read for the actual chart
and the coefficient-parameter comparison. The compact potential
and its two gradients were reconstructed from the literal
determinant in fresh unsaved algebra. Independently, a generic-jet
expansion reconstructed both (20) and (23) with zero residuals.
One optional symbolic pretty-printing call failed after all its
displayed coefficient and integrability calculations had completed;
no mathematical conclusion depends on that formatting call.
No saved checker was executed, imported, compiled, or rerun.
Earlier proof sources and frozen packets are unchanged.
