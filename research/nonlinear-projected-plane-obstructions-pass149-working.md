# Two nonlinear projected placements that cannot complete an actual dense chart

The two elementary changes of projected coordinates considered here do
not produce a dense three-good frame with the standard triangular
coefficient embedding \(q=pz-t^2\). The first has one exceptional
quadratic case without a generic critical point, but that case has a
critical point on the surviving divisor \(p=0\). The second either
fails whole generic-line generation or has a generic critical point.
Neither conclusion is an actual counterexample to cancellation.

## 1. Rings, placement, and necessary conditions

Put
\[
A_0=\mathbb C[p,t,z],\qquad q=pz-t^2,\qquad
S=\mathbb C[p,q],\qquad K=\mathbb C(p,q).
\tag{1}
\]
Let \(h\in S\setminus\{0\}\), and work in
\(A_h=A_0[h^{-1}]\). We consider \(f,g\in S[h^{-1}]\) with
\(J=f_pg_q-f_qg_p\ne0\). Thus \(f,g\) may be rational functions
of \(p,q\); the chosen invariant localization contains their
denominators. Their indicated partials hold the other coefficient
variable fixed.

For projected intercepts \(y_0,z_0\), form
\(Y=y_0+Xf,\ Z=z_0+Xg\). A necessary condition for completion
by an actual last coordinate \(W\in A_h[X]\) is that the two
relative differential rows of \(Y,Z\), with \(X\) fixed, have
unit minor ideal in \(A_h[X]\). Indeed an actual polynomial
inverse supplies a third row making their determinant a unit.
We use this necessity only, never its converse.[^1]

In the actual dense chart under consideration, the coefficient
embedding additionally gives
\[
A_h\otimes_S K=K[t],\qquad K[y_0,z_0]=K[t].
\tag{2}
\]
The second equality is the retained whole generic-line theorem139,
not an assumption that either intercept alone is linear.[^2]
The first follows directly from (1) by
\(z=(q+t^2)/p\). A failure of (2) excludes this actual chart,
without making a general claim about pairs that do not satisfy it.

The two placements below are themselves genuine polynomial
coordinate changes of the intercept ring:
\((p,t,z)\mapsto(p,t+R(z),z)\) has inverse
\((p,y_0,z_0)\mapsto(p,y_0-R(z_0),z_0)\);
\((p,t,z)\mapsto(p+R(t),z,t)\) has inverse
\((y_0,z_0,w_0)\mapsto(y_0-R(w_0),w_0,z_0)\).
Both inverse orders are immediate. This does not make the
four-variable shifted pair into an actual frame.

## 2. The placement \((t+R(z),z)\)

Let \(R\in\mathbb C[z]\) have degree at least two. Assume
\(h(0,q)\ne0\), so the generic divisor \(p=0\) is not removed.
Set \(y_0=t+R(z),z_0=z\). This pair already satisfies (2), since
\(t=y_0-R(z_0)\). We prove that no completion has unit Jacobian.

Work over \(K\), substituting \(z=(q+t^2)/p\), and put
\[
B=p+2tR'(z),\qquad
\Delta=B g_q-2t f_q,\qquad
F=z\Delta+B g_p-2t f_p.
\tag{3}
\]
These are polynomials in \(t\) over \(K\). Absolute differentials
over \(\mathbb C\), arranged in columns \((p,q,t)\), give
\[
\begin{pmatrix}
-R'z/p+Xf_p&R'/p+Xf_q&1+2tR'/p\\
-z/p+Xg_p&1/p+Xg_q&2t/p
\end{pmatrix}.
\tag{4}
\]
Here \(dp,dq\) are not set to zero. The rational coordinate
change from \((p,t,z)\) to \((p,q,t)\) has determinant \(-p\),
which is nonzero over the generic coefficient field. Thus
rank-drop in (4) is rank-drop of the original rows.

Subtracting \(R'\) times the second row from the first, and then
subtracting \(2t/p\) times that new first row from the second,
shows that at \(X=-1/\Delta\) the last difference is
\((-F/(p\Delta),0,0)\). The exact polynomial identity
\[
f_qF-(f_qz+f_p)\Delta=-BJ
\tag{5}
\]
also shows that \(F,\Delta\) have no common root. In detail,
a common root would have \(B=0\). Since \(B(0)=p\), its value
of \(t\) is nonzero. Then \(\Delta=-2tf_q=0\), so \(f_q=0\).
Now \(J=f_pg_q\ne0\), whereas
\(F=-2tf_p\ne0\), a contradiction. In particular \(\Delta\)
is not identically zero: if it were, its even part \(pg_q\)
and then its odd part would force \(g_q=f_q=0\).

If \(F\) is nonconstant, choose a root in \(\overline K\).
At that root \(\Delta\ne0\), and (4) drops rank at
\(X=-1/\Delta\). This defines a field-valued point of the
localized ring, because every nonzero coefficient denominator,
including \(h\), remains nonzero. The minor ideal is therefore
proper. No specialization to a complex closed point is needed.

It remains to classify exactly when \(F\) is constant in \(t\).
Since \(z=(q+t^2)/p\) is even in \(t\), equation (3) gives
\[
F_{\rm even}=p g_p+(q+t^2)g_q,\qquad
F_{\rm odd}=2t\{R'(z)(g_p+zg_q)-f_p-zf_q\}.
\tag{6}
\]
Constancy forces \(g_q=0\). Now \(J=-f_qg_p\ne0\), and the
vanishing odd part says
\(R'(z)g_p=f_p+zf_q\). The substitution
\(K[z]\hookrightarrow K[t]\), \(z\mapsto(q+t^2)/p\), is
injective. Hence \(R'\) must have degree one, and
\[
R(z)=c z^2+d z+e,\quad
g=\alpha p+\beta,\quad
f=2c\alpha q+d\alpha p+\gamma,\quad
c\alpha\ne0.
\tag{7}
\]
Indeed the coefficient identities are
\(f_q=2c g_p,\ f_p=d g_p\).
Since \(g_q=0\), equality of mixed partials gives \(g_{pp}=0\),
so \(\alpha,\beta,\gamma\) are complex constants. Conversely,
(7) makes \(F=p\alpha\), which is nonzero over \(K\).

This exceptional family still cannot complete on the stated chart.
In the original columns \((p,t,z)\), subtract \(R'(z)\) times
the \(Z\) row from the \(Y\) row. The resulting two rows are
\[
(0,\ 1-4c\alpha tX,\ 2c\alpha pX),\qquad
(\alpha X,\ 0,\ 1).
\tag{8}
\]
Their minors are
\(-\alpha X(1-4c\alpha tX)\),
\(-2c\alpha^2pX^2\), and \(1-4c\alpha tX\).
At \(p=0,\ X=(4c\alpha t)^{-1}\), with \(t\) generic, all
vanish. The relation \(q=-t^2\) makes
\(h(0,-t^2)\ne0\), so this point survives the localization.
This finishes the first exclusion. The visible-divisor hypothesis
is used only for (7); it must not be dropped from that case.

## 3. The placement \((p+R(t),z)\)

Let \(R\in\mathbb C[t]\) be nonlinear and put
\(y_0=p+R(t),z_0=z\). First write
\(R(t)=P(t^2)+tO(t^2)\). Over \(K\), the generated algebra is
\[
K[y_0,z_0]=K[t^2,R(t)]
=K[t^2]\mathbin{\oplus}tO(t^2)K[t^2].
\tag{9}
\]
The direct-sum description holds because the square of
\(tO(t^2)\) belongs to \(K[t^2]\). Thus it equals \(K[t]\)
if and only if \(O\) is a nonzero constant. This includes the
case \(O=0\), where the odd summand vanishes and equality fails.
Consequently (2) forces
\(R(t)=ct+P(t^2)\), with \(c\in\mathbb C^*\).

Assume this necessary form. Put
\(B=R'(t)=c+tD_0(t^2)\), where \(D_0(T)=2P'(T)\), and define
\[
\Delta=pB g_q-2t f_q,\qquad
F=(zB+2t)\Delta+B(pB g_p-2t f_p).
\tag{10}
\]
The absolute differential rows in \((p,q,t)\) are
\[
\begin{pmatrix}
1+Xf_p&Xf_q&B\\
-z/p+Xg_p&1/p+Xg_q&2t/p
\end{pmatrix}.
\tag{11}
\]
If \(f_q=0\), then \(f_pg_q\ne0\). Since \(R\) is nonlinear,
\(B\) is nonconstant and has a root over \(\overline K\).
At such a root and \(X=-1/f_p\), the entire first row is zero.
Thus this case already has a generic rank-drop.

Suppose \(f_q\ne0\). We will prove that \(F\) is nonconstant.
For any common root of \(F,\Delta\), the identity
\[
f_qF-\{f_q(zB+2t)+Bf_p\}\Delta=-pB^2J
\tag{12}
\]
would force \(B=0\). But \(B(0)=c\ne0\), so \(t\ne0\) at
that root, and \(\Delta=-2tf_q\ne0\), a contradiction.
Also \(F\) at a root of \(B\) is \(-4t^2f_q\ne0\).
Hence a root of the nonconstant \(F\) has both
\(B,\Delta\ne0\). At \(X=-B/\Delta\), the row combination
\(B\,{\rm row}_2-(2t/p){\rm row}_1\) is
\((-F/(p\Delta),0,0)\), yielding rank-drop.

Here is the full nonconstancy argument, with no restriction on the
degree of \(D_0\). Set \(T=t^2\), and put
\[
A(T)=(q+T)g_q+p g_p,\qquad
C(T)=p g_q-(q+T)f_q/p-f_p.
\tag{13}
\]
Direct expansion of (10) gives
\(F=B^2A+2tBC-4Tf_q\).
If \(F\) were constant, its odd part would give
\(D_0A+C=0\), since \(c\ne0\). Substituting that identity
in its even part would give the constant polynomial
\[
c^2A-TD_0^2A-4Tf_q.
\tag{14}
\]
The following degree cases exhaust the possibilities.

* If \(\deg D_0\ge2\), the identity \(D_0A+C=0\) is
  impossible unless \(A=0\), because \(\deg C\le1\).
  But \(A=0\) implies \(g_q=g_p=0\), contrary to \(J\ne0\).
* If \(\deg D_0=1\), its quadratic coefficient in \(D_0A\)
  first forces \(g_q=0\). Then \(A=p g_p\) is a nonzero
  constant, and (14) has degree three with nonzero leading
  coefficient \(-g_pp\operatorname{lc}(D_0)^2\).
* If \(D_0=d_0\ne0\) is constant and \(g_q\ne0\), (14)
  has the nonzero quadratic coefficient \(-d_0^2g_q\).
  If instead \(g_q=0\), the coefficient of \(T\) in
  \(D_0A+C=0\) forces \(f_q=0\), contradicting \(J\ne0\).
* For completeness, if \(D_0=0\), the odd identity \(C=0\)
  gives \(f_q=0,\ f_p=pg_q\). Constancy of (14) gives
  \(g_q=0\), so again \(J=0\). This is the affine boundary,
  not needed for the stated nonlinear family.

Thus \(F\) is nonconstant. The resulting field-valued critical
point keeps every invariant denominator nonzero exactly as in
Section 2. This second exclusion does not require that \(p=0\)
survive: it uses either whole-line failure or a generic critical
point.

## 4. Scope and finite controls

Both conclusions concern the displayed simultaneous embedding
\(S=\mathbb C[p,pz-t^2]\), the specified projected coordinates,
and the rational speed ratios \(f,g\). They exclude two nonlinear
elementary projected placements, not arbitrary nonlinear changes
of all three intercept coordinates. No completed actual frame,
nontrivial actual divisor constants, or cancellation counterexample
is produced.

The companion
[exact checker](nonlinear_projection_controls_pass149.py) checks
cleared polynomial row identities, finite parity/degree controls,
and the exceptional quadratic minors. It never divides by an
unknown root value, treats a Jacobian condition as an inverse,
or numerically verifies the universal exclusion.

## Sources

1. [The triangular-residue frame exclusion148](triangular-residue-frame-exclusion-pass148-working.md),
   Sections 1--2. The actual-chart minor-ideal necessity and
   invariant-localization convention are retained here; the two
   nonlinear placements and the exceptional classification are
   proved above.
2. [The dense all-degree Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   the whole generic-line conclusion. Only \(K[y_0,z_0]=K[t]\)
   is imported in Section 3; its original proof is not re-audited
   by the finite controls.

[^1]: Source 1.
[^2]: Source 2.
