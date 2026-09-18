# The complete centered eliminant for q = rho squared minus a cubic or quartic

This note gives the full polynomial eliminant for the two actual pivots
\(q=\rho^2-g(t)\), where \(g=t^3\) or \(g=t^4\). It retains every
lower-potential coefficient. The center polynomial is necessarily cubic,
and the leading sextics are respectively \(U^6\) and
\(4U^4(4t^2U^2-V^2)\). The centering is a change of formal plane
variables over the exact coefficient field, not an ambient coordinate map.

The actual nonzero-return branch also retains the finite-module and
conductor statements of the radical chart. None of these statements
identifies the projected plane ring with its normalization or gives an
original invariant coordinate.

## 1. Actual hypotheses and coefficient conventions

For \(d\in\{3,4\}\), suppose an actual globally sliced polynomial
four-ring has the entire supplied initial kernel
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=\mathscr A[u],\qquad
E=\partial_u,\qquad \mathscr A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0\tau,b_0\tau,e_0\tau^2,h_0\tau^2)\bigr)
 =(\mathsf X^2\mathsf Z-\mathsf W^2+
                       \mathsf X^{4-d}\mathsf Y^d).
\end{gathered}                                                    \tag{1}
\]
Here \(\tau\) is independent and the displayed generators are actual
polynomial coordinates. No minimality or entry assertion is assumed.

The literal \(Z\) pivot of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
supplies
\[
\begin{gathered}
0\ne N=[u^3]\partial_Z|_{\mathscr A}\in\operatorname{LND}(\mathscr A),\qquad
L=\operatorname{Frac}(\ker_{\mathscr A}N),\qquad
\mathscr A_L=L[v],\quad Nv=1,\\
t=b_0/a_0,\qquad \rho=h_0/a_0^2,\qquad q=e_0/a_0^2
       =\rho^2-g(t),\qquad g(t)=t^d,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad W=w+\theta X+\rho X^2,\\
y,z,w,\sigma,\theta\in L[v],\qquad
L[y,z,w]=L[v],\qquad J(X)=J_0=-a_0^3\in L^*.
\end{gathered}                                                    \tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their commuting
partials extend uniquely to the finite separable field \(L\), and fix
\(v\). In particular \(t\ne0\) in this field. No rationality of \(L\)
or original-ring regularity of its elements is assumed.

Formal \(U,V\) are independent of the coefficient derivatives. Write
\(g_j=d^jg/dt^j\). Thus the relevant Taylor terms are
\[
H_2(q)=V^2-\frac{g_2}2U^2,\qquad
H_3(q)=-\frac{g_3}6U^3,\qquad
H_4(q)=-\frac{g_4}{24}U^4,\qquad q_{\rho\rho}=2.
\tag{3}
\]
All lower coefficients below are retained as \(k,n,\ell,m\in L\).
When an identity is used in the actual chart, their jets are commuting
partial derivatives of those elements. They are not independently
chosen coordinate functions or additional original-ring coordinates.

## 2. Raw potentials and the undivided eliminant

The four integrated identities specialize to
\[
\begin{gathered}
\sigma=-g_1y+2\rho\theta+k,\qquad
z=2\rho w+f(y,\theta),\\
f(U,V)=V^2-\frac{g_2}2U^2+k_tU+k_\rho V+n,\qquad
\mathcal R=f_V=2V+k_\rho,\\
S(U,V)=-\frac{g_3}6U^3+\frac{k_{tt}}2U^2+k_{t\rho}UV
       +\frac{k_{\rho\rho}}2V^2+n_tU+n_\rho V,\\
\beta(U,V)=f_\rho=S_V=k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Rw+S(y,\theta)=\ell,\qquad
w^2+\beta(y,\theta)w+Q(y,\theta)=0,\qquad R=\mathcal R(y,\theta),
\end{gathered}                                                    \tag{4}
\]
where the complete last polynomial is
\[
\begin{aligned}
Q(U,V)={}&-\frac{g_4}{24}U^4+\frac{k_{ttt}}6U^3
 +\frac{k_{tt\rho}}2U^2V+\frac{k_{t\rho\rho}}2UV^2
 +\frac{k_{\rho\rho\rho}}6V^3\\
&+\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2
 -\ell_tU-\ell_\rho V-m.
\end{aligned}                                                    \tag{5}
\]
In particular \(\beta\) is a coefficient \(\rho\)-derivative of \(f\),
not its formal \(V\)-derivative.

Set \(T=\ell-S\). Multiplying the last equation of (4) by \(R^2\)
and substituting \(Rw=T(y,\theta)\) gives the polynomial identity
\[
\boxed{\mathcal H=T^2+\mathcal R\beta T+\mathcal R^2Q,
\qquad \mathcal H(y,\theta)=0.}
\tag{6}
\]
No division by the evaluated return coefficient is used in (6). It
holds also in the identically zero-return branch. The monic \(w^2\)
term is retained throughout.

## 3. Exact center, with every lower coefficient

Use the abbreviations
\[
\begin{gathered}
\kappa=k_\rho,\qquad c=k_{\rho\rho},\qquad
\eta=V+\kappa/2,\qquad \mathcal R=2\eta,\\
B(U)=k_{t\rho}U+n_\rho-\kappa c/2,\qquad
p(U)=S(U,-\kappa/2)-\ell.
\end{gathered}                                                    \tag{7}
\]
The shift fixes \(U\), and the derivative convention remains the
original one before making this substitution. Its coefficients depend
on \(t,\rho\); it is not legitimate to treat the shifted formal
variable as fixed under the old coefficient partials without a chain
rule.

Direct substitution gives
\[
\boxed{p(U)=-\frac{g_3}6U^3+\frac{k_{tt}}2U^2
       +\left(n_t-\frac{\kappa k_{t\rho}}2\right)U
       +\frac{\kappa^2c}{8}-\frac{\kappa n_\rho}{2}-\ell.}
\tag{8}
\]
For \(g=t^3\), its leading coefficient is \(-1\); for \(g=t^4\),
it is \(-4t\ne0\). Thus \(p\) has degree exactly three in both
models, regardless of the lower potentials.

The full division and derivative identities are
\[
\begin{gathered}
S-\ell=p+B\eta+\frac c2\eta^2
          =p+\frac{\mathcal R B}{2}+\frac{c\mathcal R^2}{8},
\qquad \beta=B+c\eta,\\
D(U,V)=-\frac B2-\frac{c\mathcal R}{8}
       =-\frac{k_{t\rho}}2U-\frac{n_\rho}2
                         -\frac c4V+\frac{c\kappa}{8},\\
S-\ell=p-\mathcal R D,\qquad
R\{w-D(y,\theta)\}=-p(y),\qquad \deg D\le1.
\end{gathered}                                                    \tag{9}
\]
These formulas are exact over \(L\). In particular the cubic term
changes the center but not the affine degree of the division quotient.

Expand the complete last potential, not only its homogeneous part:
\[
Q(U,\eta-\kappa/2)=Q_0(U)+Q_1(U)\eta+Q_2(U)\eta^2+Q_3\eta^3,
\tag{10}
\]
where
\[
\begin{aligned}
Q_0={}&-\frac{g_4}{24}U^4+\frac{k_{ttt}}6U^3
 +\left(\frac{n_{tt}}2-\frac{\kappa k_{tt\rho}}4\right)U^2\\
&+\left(\frac{\kappa^2k_{t\rho\rho}}8
              -\frac{\kappa n_{t\rho}}2-\ell_t\right)U
 -\frac{\kappa^3k_{\rho\rho\rho}}{48}
 +\frac{\kappa^2n_{\rho\rho}}8+\frac{\kappa\ell_\rho}2-m,\\
Q_1={}&\frac{k_{tt\rho}}2U^2
 +\left(n_{t\rho}-\frac{\kappa k_{t\rho\rho}}2\right)U
 +\frac{\kappa^2k_{\rho\rho\rho}}8
              -\frac{\kappa n_{\rho\rho}}2-\ell_\rho,\\
Q_2={}&\frac{k_{t\rho\rho}U+n_{\rho\rho}}2
                              -\frac{\kappa k_{\rho\rho\rho}}4,
\qquad Q_3=\frac{k_{\rho\rho\rho}}6.
\end{aligned}                                                    \tag{11}
\]
Consequently the complete centered eliminant is
\[
\boxed{\begin{aligned}
\mathcal H(U,\eta-\kappa/2)={}&p^2
 +\eta^2(4Q_0-B^2-cp)
 +\eta^3(4Q_1-2cB)\\
&+\eta^4(4Q_2-3c^2/4)+4Q_3\eta^5.
\end{aligned}}                                                  \tag{12}
\]
There is no coefficient of \(\eta\). In particular
\(\mathcal H(U,-\kappa/2)=p(U)^2\), with no missing scalar factor.

For a direct proof of (12), use (9) to write
\(T=-p-B\eta-c\eta^2/2\), \(\mathcal R=2\eta\), and
\(\beta=B+c\eta\). Then
\[
\begin{aligned}
T^2+\mathcal R\beta T
 &=\left(T+\eta\beta\right)^2-\eta^2\beta^2\\
 &=p^2-(cp+B^2)\eta^2-2cB\eta^3-\frac{3c^2}{4}\eta^4.
\end{aligned}                                                    \tag{13}
\]
Adding \(4\eta^2Q(U,\eta-\kappa/2)\) and using (10) proves every
coefficient in (12). Equations (8) and (11) are ordinary polynomial
substitutions into (4) and (5), so the calculation does not require
integrating a coefficient equation or discarding any lower jet.

## 4. The complete degree-five and degree-six parts

The highest total-degree terms can also be read directly in the
unshifted variables. They are
\[
\boxed{\mathcal H_6=
\frac{g_3^2}{36}U^6-\frac{g_4}{6}U^4V^2,}
\tag{14}
\]
and
\[
\boxed{\begin{aligned}
\mathcal H_5=\frac16\bigl\{
&-\kappa g_4U^4V-g_3k_{tt}U^5
 +(c g_3+4k_{ttt})U^3V^2\\
&+12k_{tt\rho}U^2V^3+12k_{t\rho\rho}UV^4
 +4k_{\rho\rho\rho}V^5\bigr\}.
\end{aligned}}                                                  \tag{15}
\]
To check the top part without the centered formula, only the square
of the cubic term of \(T\) and the product of \((2V)^2\) with the
quartic term of \(Q\) contribute degree six. For degree five, include
the cubic/quadratic cross term of \(T^2\), the leading term of
\(\mathcal R\beta T\), \((2V)^2H_3(k)\), and the degree-one part
\(4\kappa V\) of \(\mathcal R^2\) times \(-g_4U^4/24\).
The \(g_3k_{t\rho}U^4V\) contributions cancel. The remaining
terms give exactly (15).

For the two models this specializes to
\[
\begin{array}{c|c|c}
g&\mathcal H_6&[U^3]p\\ \hline
t^3&U^6&-1\\
t^4&4U^4(4t^2U^2-V^2)&-4t.
\end{array}
\qquad
\begin{gathered}
\deg\mathcal H=6,\qquad \deg_U\mathcal H=6,\qquad
\deg_V\mathcal H\le5,\\
[U^6]\mathcal H=g_3^2/36,\qquad
[V^5]\mathcal H=2k_{\rho\rho\rho}/3.
\end{gathered}                                                    \tag{16}
\]
The top is nonzero in the exact field even when some or all lower
jets vanish. These are degree statements about the full eliminant,
not an assertion that the selected plane component is the eliminant.

## 5. What transfers to the actual nonzero-return branch

Assume only in this section that \(R\ne0\) in \(L[v]\). Define
\(C=L[y,\theta]\) and \(O=L[v]\). The actual whole-line equality
in (2) and the expression for \(z\) in (4) give
\[
\boxed{O=C[w]=C+Cw,\qquad \operatorname{Frac}C=L(v),\qquad
RO\subset C,\qquad C_R=O_R.}
\tag{17}
\]
Indeed \(z=2\rho w+f(y,\theta)\) puts the generators of \(O\)
in \(C[w]\). The monic last equation of (4) reduces every power
of \(w\) to a \(C\)-linear combination of \(1,w\). These need
not be a free basis. The first equation for \(w\) gives \(Rw\in C\),
so it gives both the fraction-field equality and the conductor
inclusion. Localizing that equation at \(R\) gives the last equality.
The ring \(O\) is therefore the normalization of \(C\) in their
common fraction field, not necessarily equal to \(C\).

Over an algebraic closure of \(L\), every point above \(R=0\) has
\(\theta=-\kappa/2\) and \(p(y)=0\), by (9). There are at most
three possible values of \(y\). For each value, the monic quadratic
in (4) has at most two values of \(w\). The triple
\((y,\theta,w)\) generates \(L[v]\), so two distinct parameter
points cannot give the same triple. Hence
\[
\#\{v\in\overline L:R(v)=0\}\le6.
\tag{18}
\]
This bounds distinct points only, not their multiplicities.

The finite-return argument is the one in
[radical206](weight-four-radical-nonzero-r-eliminant-pass206-working.md).
Its old center had degree at most two. Here the center has degree
exactly three, so neither its repeated-quadratic cone argument nor
its four-point bound can simply be reused. The conductor calculations
in [the companion206](radical-projection-conductor-cubic-reduction-pass206-working.md)
remain available only with their particular degree hypotheses checked
again; their previous small-degree conclusion is not asserted here.

## 6. Scope and verification boundary

The identities (3)--(16) are polynomial algebra over the coefficient
field and remain valid before any nonzero-return assumption. Section5
uses the actual whole-line input and assumes \(R\ne0\). It does not
assume a simple selected component, a unit cofactor, or plane normality.

The identically zero-return and constant-first-projection endpoints
are separate tasks. This note does not exclude or recognize either
model, classify the cubic center, prove an ambient coordinate, or
transfer the older quadratic-center lemma to a cubic. In particular
\(\eta\), \(D\), and every coefficient in \(L\) remain formal or
projected objects unless a separate original-ring argument says more.

The full universal184 source and both relevant206 sources were read
before this derivation. An independent unsaved symbolic reconstruction
with arbitrary lower jets verified the full centered identity, every
\(Q_j\), and the homogeneous parts (14)--(15). The written algebra
above supplies the identities; the symbolic comparison is supplementary.
No saved checker was executed, imported, or compiled, and no earlier
source, index, or packet was edited. This is not a claim about arbitrary
entry, unrestricted cancellation, historical novelty, or human review.
