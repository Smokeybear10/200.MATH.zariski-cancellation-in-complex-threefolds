# No affine first projection for the coprime bad-linear quartic

**Status: working exclusion of the affine-y branch under the actual chart hypotheses.**

For a supplied actual E-time \((1,1,2,2)\) frame with full
initial kernel \((X^2Z+Y^2W)\), the projected entry \(y\)
cannot be affine and nonconstant in the normalized generic parameter.
Graphs of degree at least three contradict the quintic leading form.
A quadratic graph would force an irrational Euler exponent for an
algebraic coefficient. Graphs of degree one and zero are excluded
separately, with the constant graph requiring a second use of the
unit evaluated cofactor.

Together with the separately proved constant-or-affine gate184,
this leaves \(y\in L\). That remaining branch is not excluded or
recognized in this note. No generic parameter is treated as an
original coordinate, and no determinant factor is discarded.

## 1. Exact actual and selected-component inputs

Retain the supplied hypotheses
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\qquad Eu=1,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,h_0\eta^2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z+\mathsf Y^2\mathsf W),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h_0=E^2W/2.
\end{gathered}
\tag{1}
\]
The ideal is the full initial kernel, not one relation, and the
four displayed original generators are actual polynomial coordinates.
Use the exact field and parameter of
[the universal chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\qquad \rho=h_0/a^2,\qquad q=e/a^2=-t^2\rho,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad t,\rho\text{ algebraically independent}.
\end{gathered}
\tag{2}
\]
The two coefficient partials extend uniquely and commute on \(L\).
All derivatives below are those coefficient partials, before any
substitution of projected entries. Put \(K=\ker_L\partial_\rho\);
it is not assumed rational.

The whole-plane proof and selected-component proof184, both read as
complete saved sources, give
\[
\begin{gathered}
L[y,\vartheta]=L[v],\qquad
\mathcal H=GQ\in L[U,V],\qquad
Q(y,\vartheta)=\omega\in L^*,\\
\ker\{L[U,V]\to L[v],\ (U,V)\mapsto(y,\vartheta)\}=(G),\\
\deg\mathcal H=5,\qquad
\mathcal H_5=-U^4V,\qquad \deg_V\mathcal H\le3,\\
y\in L\quad\hbox{or}\quad y=\gamma v+\eta_0,
\qquad\gamma\in L^*,\quad\eta_0\in L.
\end{gathered}
\tag{3}
\]
Here \(\mathcal H_5\) is the ordinary total-degree-five part.
The coefficient \(\omega\) is the value of the cofactor on the
selected line. The polynomial \(Q(U,V)\) is not assumed constant.

Suppose for contradiction that the second alternative in (3) holds.
Then \(L[y]=L[v]\), so \(\vartheta=P(y)\) for \(P\in L[U]\).
Polynomial division in \(V\) proves that we may choose
\[
G=V-P(U),\qquad \deg P\le5,
\qquad \mathcal H=\omega G+G^2T,\quad T\in L[U,V].
\tag{4}
\]
Indeed the kernel is exactly \((V-P(U))\), and
\(Q-\omega\) belongs to that kernel. Rescaling the original
generator \(G\) only rescales the nonzero \(\omega\).
The degree bound follows from \(G\mid\mathcal H\).
The possibility \(P=0\) is included among the constant graphs.

## 2. The exact literal coefficients needed below

Use \(H_j\) for the divided coefficient Taylor polynomials of184.
The source formulas specialize to
\[
\begin{gathered}
f=-\rho U^2-2tUV+k_tU+k_\rho V+n,\qquad
\mathcal R=k_\rho-2tU,\\
S=-U^2V+H_2(k;U,V)+H_1(n;U,V),\qquad
g_4=H_3(k;U,V)+H_2(n;U,V),\\
\mathcal H=\mathcal R(g_4-\ell_tU-\ell_\rho V-m)
                  +S_V(\ell-S),\qquad k,n,\ell,m\in L.
\end{gathered}
\tag{5}
\]
In particular \(S_V=f_\rho\). For transparent coefficient
extraction, put
\[
\begin{gathered}
r=k_\rho,\qquad h=k_{\rho\rho},\qquad
A(U)=-U^2+k_{t\rho}U+n_\rho,\qquad
D(U)=\frac{k_{tt}}2U^2+n_tU,\\
S=D(U)+A(U)V+\frac h2V^2,\qquad S_V=A(U)+hV,\\
[V^3]g_4=\frac{k_{\rho\rho\rho}}6,\qquad
[V^2]g_4=\frac{h_tU+n_{\rho\rho}}2.
\end{gathered}
\tag{6}
\]
The symbol \(h\) here is an integrated coefficient derivative,
not the original leading coefficient \(h_0\) in (1).
Multiplication in (5) gives the two exact identities
\[
\begin{aligned}
[V^3]\mathcal H
 &=\frac{r-2tU}{6}k_{\rho\rho\rho}-\frac{h^2}{2},\\
[V^2]\mathcal H
 &=\frac{r-2tU}{2}(h_tU+n_{\rho\rho})
                  -\frac{3h}{2}A(U),\\
[U^2V^2]\mathcal H&=-t h_t+\frac32h.
\end{aligned}
\tag{7}
\]
For example the second product in (5) is
\((A+hV)(\ell-D-AV-hV^2/2)\). Its cubic coefficient is
\(-h^2/2\), and its quadratic coefficient is \(-3hA/2\).
No derivative of \(n\) or lower coefficient is silently set to zero.

## 3. Degrees at least three contradict the top quintic

Suppose \(d=\deg P\ge3\). Then \(\deg G=d\), and any nonzero
\(G^2T\) has degree at least \(2d\ge6\). Its top degree cannot
cancel against \(\omega G\), which has degree \(d\).
Since \(\deg\mathcal H=5\), (4) forces \(T=0\).
Thus \(\mathcal H=\omega G\); its top is a nonzero multiple
of \(U^d\). It cannot equal \(-U^4V\).
This excludes every \(d\ge3\), including degree five.

## 4. A quadratic graph forces an irrational Euler exponent

Suppose
\(P=p_2U^2+p_1U+p_0\), with \(p_2\in L^*\).
Now \(\deg G=2\). Equation (4) and degree five force
\(T\) to have degree one. Write
\(T=s_UU+s_VV+s_0\). Comparing degree-five parts gives
\[
\mathcal H=\omega G+G^2(s_VV+s_0),\qquad
s_U=0,\qquad s_Vp_2^2=-1.
\tag{8}
\]
In particular \(s_V\ne0\).
The coefficient of \(V^3\) on the right is exactly \(s_V\).
Comparing with the first identity of (7), first in degree one
in \(U\) and then in degree zero, gives
\[
k_{\rho\rho\rho}=0,\qquad
h\in K^*,\qquad s_V=-\frac{h^2}{2},\qquad
(hp_2)^2=2.
\tag{9}
\]
The first conclusion uses \(t\ne0\), which follows from its
transcendence. The nonzero conclusion for \(h\) follows from
\(s_V\ne0\). Since the field contains \(\mathbb C\), the last
identity gives \(\delta:=hp_2\in\{\sqrt2,-\sqrt2\}\subset\mathbb C\).
This is not extraction of a new coefficient-field root.

The \(V^2\) coefficient on the right of (8) is
\(s_0-2s_VP\). Its \(U^2\) coefficient is
\(-2s_Vp_2=h^2p_2\). The final identity of (7) therefore yields
\[
-t h_t+\frac32h=h^2p_2,
\qquad \frac{t h_t}{h}=\frac32-\delta.
\tag{10}
\]

We justify the exact-field obstruction to (10) without assuming
\(K=\mathbb C(t)\). Since \(h_\rho=0\), differentiate its monic
minimal polynomial over \(\mathbb C(t,\rho)\) with respect to
\(\rho\). The result has smaller degree in \(h\), so every
coefficient derivative is zero. Rational functions killed by
\(\partial_\rho\) lie in \(\mathbb C(t)\). Thus \(h\) is
algebraic over \(\mathbb C(t)\).

Here is the needed elementary Euler lemma. If a nonzero element
\(z\) algebraic over \(\mathbb C(t)\) satisfies
\(t z_t=\alpha z\) for a constant \(\alpha\in\mathbb C\),
then \(\alpha\in\mathbb Q\).
Write its monic minimal polynomial as
\[
z^d+\sum_{i=0}^{d-1}a_i(t)z^i=0,
\qquad a_0\ne0,\quad a_i\in\mathbb C(t).
\tag{11}
\]
Apply \(t\partial_t\) and subtract \(d\alpha\) times the
original equation. Minimality makes every coefficient in the
remaining relation of degree less than \(d\) zero. In particular
\(t a_0'=d\alpha a_0\). Write the rational function
\(a_0=t^j b(t)\), where \(j\in\mathbb Z\) and \(b\) is a
unit at \(t=0\). Then
\(t a_0'/a_0=j+t b'/b\) has value \(j\) at zero.
It follows that \(d\alpha=j\), proving the lemma.
These coefficient derivatives are the unique extensions through
the finite characteristic-zero field, so they agree with those
already used in (10).

But \(3/2-\sqrt2\) and \(3/2+\sqrt2\) are not rational.
Applying the lemma to (10) is a contradiction. A quadratic graph
is impossible.

## 5. Linear and constant graphs are also impossible

If \(P=p_1U+p_0\) has degree one, then
\(G_1=V-p_1U\) divides \(\mathcal H_5=-U^4V\).
In the unique factorization ring \(L[U,V]\), this linear factor
must be associated to \(U\) or \(V\). Its coefficient of \(V\)
is one, so the first is impossible; the second forces \(p_1=0\),
contrary to degree one.

Finally let \(P=p_0\), including \(p_0=0\). In (4) the linear
polynomial \(G=V-p_0\) has top \(V\). Since \(\mathcal H\) has
degree five, \(T\ne0\) has degree three, and
\[
\mathcal H_5=V^2T_3.
\tag{12}
\]
This contradicts \(\mathcal H_5=-U^4V\), where \(V\) has exact
multiplicity one. Merely noting that \(G_1\) divides the top
quintic would not exclude this constant graph; the evaluated-unit
identity \(Q-\omega\in(G)\) is essential a second time.

All possible graph degrees in (4) have now been excluded.
The affine alternative for \(y\) in (3) is therefore impossible.
The conclusion under the supplied actual assumptions is
\[
\boxed{y\in L.}
\tag{13}
\]

## Scope and verification

The full universal-chart184 proof, the whole-plane companion
[184](weight-four-bad-linear-whole-plane-projection-pass184-working.md),
and the saved selected-component companion
[184](weight-four-bad-linear-selected-component-pass184-working.md)
were read before this derivation. In particular (3) imports the
proved evaluated-unit assertion, not just its earlier divisibility
into \(R^2\). No Abhyankar--Moh theorem, genus formula, or new
external classification result is used.

This is an exclusion of nonconstant affine \(y\), not an exclusion
of the complete initial form. The remaining \(y\in L\) branch,
other quartic forms, lower initial rank and arbitrary coordinate
entry require separate arguments. The coefficient-field Euler
lemma and every coefficient comparison are proved here. They give
no original-ring inverse or invariant coordinate.

No earlier artifact, packet or index was edited. No checker was
executed, imported or compiled. This is a bounded working proof,
not a human expert review, proof-assistant verification, historical
novelty claim, or unrestricted cancellation theorem.

