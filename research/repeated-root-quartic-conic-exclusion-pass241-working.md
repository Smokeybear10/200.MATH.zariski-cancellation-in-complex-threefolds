# Excluding the quadratic graph in the rebuilt quartic repeated-root chart

The remaining quadratic graph in the actual chart \(q=\rho^2-t^4\)
cannot occur. Its cofactor condition forces a double-graph expression
for the complete eliminant. The centered coefficients then give two
incompatible differential identities for the same nonzero element of
the exact coefficient field.

Together with the rebuilt-chart exclusions in pass237 and the
higher-degree reduction in pass238, this excludes a globally sliced
exact1122 frame whose entire supplied initial kernel is
\((Z_{\rm old}^2-X^2W_{\rm old}-Y^4)\). This is a restricted
nonrealizability statement, not an arbitrary-frame entry theorem or
an unrestricted cancellation result.

## 1. Actual chart and the remaining branch

Start with the actual hypotheses and reconstruction of
[pass237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md).
The actual interchange \(Z=W_{\rm old},W=Z_{\rm old}\) is made first.
The literal new \(Z\) pivot is then rebuilt, rather than transporting
the old selected derivation or coefficient field. In this rebuilt
frame, assume
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=\mathscr A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0\tau,b_0\tau,e_0\tau^2,h_0\tau^2)\bigr)
       =(\mathsf X^2\mathsf Z-\mathsf W^2+\mathsf Y^4),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2 .
\end{gathered}                                                    \tag{1}
\]
Here \(\tau\) is an independent indeterminate, and (1) specifies the
full kernel, not just a relation among the leading coefficients.

The actual universal chart supplies
\[
\begin{gathered}
0\ne N=[u^3]\partial_Z|_{\mathscr A},\quad
L=\operatorname{Frac}(\ker_{\mathscr A}N),\quad
\mathscr A_L=L[v],\quad Nv=1,\\
t=b_0/a_0,\quad \rho=h_0/a_0^2,\quad q=e_0/a_0^2=\rho^2-t^4,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\quad L[y,z,w]=L[v],\\
J(X)=J_0=-a_0^3\in L^* .
\end{gathered}                                                    \tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their commuting
partials extend uniquely to the finite separable field \(L\), and fix
\(v\). All projected entries in (2) lie in \(L[v]\). No rationality
of \(L\), original-ring regularity of its elements, or ambient
coordinate meaning for a coefficient-field parameter is assumed.

Pass237 excludes \(R=0\), where \(R=2\theta+k_\rho\), and excludes
constant \(y\). The pure-top and excess-order argument of
[pass238](repeated-root-return-excess-order-bound-pass238-working.md)
then leaves precisely
\[
\begin{gathered}
\deg_vy=1,\qquad \deg_v\theta=2,\qquad
L[y,\theta]=L[v],\\
\theta=\widehat P(y),\qquad
\widehat P\in L[U],\quad \deg\widehat P=2,\qquad
G(U,V)=V-\widehat P(U).
\end{gathered}                                                    \tag{3}
\]
In particular the evaluation kernel of \(L[U,V]\to L[v]\) is
exactly \((G)\). This conclusion is over the original exact field
\(L\), not merely its algebraic closure.

## 2. Complete lower potentials and the cofactor

Retain arbitrary lower potentials \(k,n,\ell,m\in L\). Define
\[
\begin{aligned}
S={}&-4tU^3+\frac{k_{tt}}2U^2+k_{t\rho}UV
                       +\frac{k_{\rho\rho}}2V^2+n_tU+n_\rho V,\\
\mathcal R={}&2V+k_\rho,\qquad
\beta=k_{t\rho}U+k_{\rho\rho}V+n_\rho,\qquad T=\ell-S,\\
Q={}&-U^4+\frac{k_{ttt}}6U^3+\frac{k_{tt\rho}}2U^2V
       +\frac{k_{t\rho\rho}}2UV^2+\frac{k_{\rho\rho\rho}}6V^3\\
&+\frac{n_{tt}}2U^2+n_{t\rho}UV+\frac{n_{\rho\rho}}2V^2
                                      -\ell_tU-\ell_\rho V-m,\\
\mathcal H={}&T^2+\mathcal R\beta T+\mathcal R^2Q .
\end{aligned}                                                    \tag{4}
\]
These are the actual third and fourth universal potentials and their
undivided eliminant. In particular
\[
Rw=T(y,\theta),\qquad
w^2+\beta(y,\theta)w+Q(y,\theta)=0,\qquad
\mathcal H(y,\theta)=0 .
\]
The complete formulas and the centering identity are proved in
[pass239](radical-minus-polynomial-centered-eliminant-pass239-working.md).
Their total degree is exactly six, with
\[
\mathcal H_6=16t^2U^6-4U^4V^2 .
\]
No lower potential is set to zero.

The actual cofactor argument and the local bound in pass238 give
\[
\mathcal H=GQ_1,\qquad
Q_1(y,\theta)=\eta R,\qquad \eta\in L^* .
\tag{5}
\]
For clarity, its two divisibilities are essential: since \(\deg_vy=1\),
the excess-order lemma gives \(Q_1(y,\theta)\mid R\); since \(G_V=1\),
the exact identity
\(\mathcal H_V(y,\theta)=-R(C_1^2+R\Lambda_\rho)\)
gives the reverse divisibility. Thus (5) is not inferred from
birationality alone or from a freely chosen polynomial parametrization.

## 3. Centering and the double-graph form

Put
\[
\kappa=k_\rho,\qquad c=k_{\rho\rho},\qquad
\zeta=V+\kappa/2,\qquad
P(U)=\widehat P(U)+\kappa/2=AU^2+BU+C,\quad A\in L^*,
\tag{6}
\]
and let
\(\mathcal H_c(U,\zeta)=\mathcal H(U,\zeta-\kappa/2)\).
The symbol \(\zeta\) is a formal plane variable, not the projected
coordinate \(z\) in (2). This formal shift does not change the
highest total-degree part. The evaluation kernel becomes
\((\zeta-P(U))\), and the formal return is \(2\zeta\).

After the same shift of \(Q_1\), equation (5) says that
\(Q_1-2\eta\zeta\) is in this evaluation kernel. Since
\(\deg Q_1=4\) and \(\deg(\zeta-P)=2\), there is an \(M\in L[U,\zeta]\)
of total degree at most two such that
\[
\boxed{\mathcal H_c=(\zeta-P)^2M+2\eta\zeta(\zeta-P),\qquad
M_2=\frac{16t^2U^2-4\zeta^2}{A^2}.}
\tag{7}
\]
The second assertion follows by dividing the top of \(\mathcal H_c\)
by the top \(A^2U^4\) of \((\zeta-P)^2\).
In particular there is no \(U\zeta\) term in \(M\).

The center polynomial and its exact leading terms are
\[
\begin{aligned}
p(U)&=S(U,-\kappa/2)-\ell\\
&=-4tU^3+\frac{k_{tt}}2U^2+
  \left(n_t-\frac{\kappa k_{t\rho}}2\right)U
   +\frac{\kappa^2c}{8}-\frac{\kappa n_\rho}{2}-\ell .
\end{aligned}                                                    \tag{8}
\]
The centered identity of pass239 states
\(\mathcal H_c(U,0)=p(U)^2\) and \([\zeta]\mathcal H_c=0\).
Evaluating (7) at zero therefore gives \(P^2M(U,0)=p^2\).
The UFD \(L[U]\) implies \(P\mid p\), without any squarefree
assumption on \(P\). Write
\[
p=P\,l,\qquad l=l_1U+l_0,\qquad l_1=-4t/A .
\]
Then \(M(U,0)=l^2\), and the absence of \(U\zeta\) in \(M\) gives
\[
M=l^2+m_1\zeta-\frac4{A^2}\zeta^2,\qquad m_1\in L .
\]
The coefficient of \(\zeta\) in (7) is
\(P^2m_1-2Pl^2-2\eta P\). Since it vanishes,
\[
Pm_1=2l^2+2\eta,\qquad
m_1A=2l_1^2,\qquad m_1B=4l_1l_0 .
\tag{9}
\]
Here \(l_1,m_1\ne0\), because \(t,A\ne0\). These equations give
\[
l_0=\frac{l_1B}{2A},\qquad
[U^2]p=Al_0+Bl_1=\frac32Bl_1=\frac{k_{tt}}2,
\qquad
\boxed{B=-\frac{A k_{tt}}{12t}.}
\tag{10}
\]

## 4. Six exact coefficients

Expand the full raw polynomial (4) after the formal substitution
\(V=\zeta-\kappa/2\), and compare it with (7)--(9). The required
six entries are
\[
\begin{array}{c|c|c}
\text{coefficient}&\text{raw }\mathcal H_c&
                       \text{double-graph expression}\\ \hline
[\zeta^5]&2k_{\rho\rho\rho}/3&0\\
[U\zeta^4]&2k_{t\rho\rho}&0\\
[\zeta^4]&2n_{\rho\rho}-3c^2/4-\kappa k_{\rho\rho\rho}
                                                   &-4/A^2\\
[U^2\zeta^3]&2k_{tt\rho}&8/A\\
[U\zeta^3]&4n_{t\rho}-2c k_{t\rho}-2\kappa k_{t\rho\rho}
                                                   &8B/A^2\\
[U^3\zeta^2]&2k_{ttt}/3+4ct&-8B/A
\end{array}                                                       \tag{11}
\]
The notation for an entry specifies the exact monomial, so the
\([\zeta^4]\) row has \(U\)-degree zero.
One can read the raw column directly from the centered formula
of pass239; it includes every relevant lower jet in (4).
For the model column, the \(\zeta^3\) contribution from
\(-4\zeta^2(\zeta-P)^2/A^2\) is \(8P\zeta^3/A^2\).
Consequently the \(U\zeta^3\) entry is \(8B/A^2\), not \(8B/A\).
The \(U^3\zeta^2\) entry is the coefficient of \(U^3\) in
\(-4P^2/A^2\), namely \(-8B/A\).

All original coefficient derivatives were taken before the shift in
(6). We will now differentiate equalities among elements of \(L\).
This is legitimate coefficient differentiation. We never differentiate
the centered polynomial at fixed \(\zeta\) as if the old partials
fixed that shifted variable.

## 5. Two incompatible equations for a nonzero coefficient

The first two rows of (11) imply
\[
k_{\rho\rho\rho}=k_{t\rho\rho}=0,\qquad c_t=c_\rho=0 .
\]
Set \(D=k_{tt\rho}\). The next two rows give
\[
\boxed{D=\frac4A\ne0,\qquad
D_\rho=(k_{t\rho\rho})_t=0,\qquad A_\rho=0,\qquad
n_{\rho\rho}=\frac{3c^2}{8}-\frac{D^2}{8}.}
\tag{12}
\]
These identities need no assumption that \(A\) or \(D\) is constant
in \(t\), and do not require an integration or a constant-field theorem.

The last row of (11) and (10) give
\[
B=-\frac{A k_{ttt}}{12}-\frac{Act}{2}
  =-\frac{A k_{tt}}{12t},
\qquad
k_{ttt}=\frac{k_{tt}}t-6ct .
\]
Taking the coefficient \(\rho\)-derivative, using \(c_\rho=0\),
proves
\[
\boxed{D_t=\frac Dt.}
\tag{13}
\]

The fifth row of (11), with \(k_{t\rho\rho}=0\), instead says
\[
4n_{t\rho}-2c k_{t\rho}
 =\frac{8B}{A^2}=-\frac{2k_{tt}}{3At}.
\]
Its \(\rho\)-derivative, using \(c_\rho=A_\rho=k_{t\rho\rho}=0\),
is
\[
4n_{t\rho\rho}=-\frac{2D}{3At}.
\]
But the \(t\)-derivative of the last equation in (12) gives
\(4n_{t\rho\rho}=-DD_t\), since \(c_t=0\).
As \(D\ne0\), it follows that
\[
\boxed{D_t=\frac{2}{3At}=\frac{D}{6t}.}
\tag{14}
\]
Equations (13) and (14) contradict \(D\ne0\), \(t\ne0\), and
characteristic zero. Thus the actual quadratic graph (3) is impossible.

## 6. Composition and scope

Pass237 rebuilds the chart by an actual coordinate interchange and
excludes both identically zero return and constant first projection.
Pass238 excludes the simple leading directions and the remaining
projected degrees three and four, and leaves exactly (3).
The contradiction above excludes that last branch. Therefore
\[
\boxed{\text{No globally sliced exact1122 polynomial frame has full
initial kernel }(Z_{\rm old}^2-X^2W_{\rm old}-Y^4).}
\tag{15}
\]
Equivalently the full rebuilt kernel in (1) cannot occur.
The hypotheses include the supplied actual coordinate frame and full
kernel throughout. No conclusion about arbitrary exact1122 entry,
the separate cubic-residue model, or the unrestricted cancellation
problem is contained in (15).

No coefficient-field element was lifted to an ambient coordinate or
declared an original-ring unit. The contradiction uses all lower
potentials, their commuting derivatives, and the actual cofactor
condition obtained from the calibrated determinant. A polynomial
identity imposed without those actual inputs would not suffice.

The complete sources237--239 were read before composition. The raw
centered coefficients and the graph-model coefficients were separately
reconstructed; an incorrect exploratory denominator was corrected
before this source was saved. No discarded intermediate argument is
used here. No retained source or index was edited, and no saved checker
was executed, imported, or compiled. This working proof does not assert
proof-assistant certification, historical novelty, or human expert review.
