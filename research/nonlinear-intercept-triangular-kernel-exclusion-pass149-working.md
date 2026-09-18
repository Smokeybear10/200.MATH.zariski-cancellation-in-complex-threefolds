# A nonlinear intercept shear still excludes the triangular residue kernel

The triangular residue-extension kernel remains incompatible with a
dense last-coordinate-slice line family after the explicit nonlinear
intercept placement below. Nilpotence of the original speed Jacobian
forces its first two speeds to be constants and its third to depend
on one invariant variable.

This extends the fixed-intercept obstruction148 to one nonlinear
placement. It does not cover arbitrary nonlinear changes of the
intercepts or a triangular polynomial depending on both base and
line variables.

## 1. A polynomial-map classification in the original coordinates

Let \(x,y,z\) be independent complex variables. Choose
\(R,Q\in\mathbb C[x]\) and \(a\in\mathbb C[p]\) with
\(\deg R\ge2\), \(\deg Q\ge2\), and \(a\) nonconstant.
Define
\[
p=y-R(x),\qquad q=a(p)z-Q(x),\qquad
V=(f(p,q),g(p,q),h(p,q))^t,
\quad f,g,h\in\mathbb C[p,q].
\tag{1}
\]
The pair \(p,q\) is algebraically independent. All subscripts
\(p,q\) below are coefficient derivatives holding the other
coefficient variable fixed. Primes on \(R,Q,a\) are their ordinary
one-variable derivatives.

**Proposition.** The original Jacobian
\(J=\operatorname{Jac}_{x,y,z}V\) is nilpotent if and only if
\[
V=(c_1,c_2,h_0(p))^t,
\qquad c_1,c_2\in\mathbb C,\quad h_0\in\mathbb C[p].
\tag{2}
\]
In particular the field of these three speeds has transcendence
degree at most one.

The proof computes the original Jacobian, without transporting a
nilpotence assertion through a nonlinear coordinate change. Factor
it as
\[
\begin{gathered}
J=AB,\qquad
A=\begin{pmatrix}f_p&f_q\\g_p&g_q\\h_p&h_q\end{pmatrix},
\qquad
B=\begin{pmatrix}
-R'&1&0\\
-a'zR'-Q'&a'z&a
\end{pmatrix},\\
L_1=-R'f_p+g_p,\qquad L_2=-R'f_q+g_q,\\
BA=\begin{pmatrix}
L_1&L_2\\
a'zL_1-Q'f_p+ah_p&a'zL_2-Q'f_q+ah_q
\end{pmatrix}.
\end{gathered}
\tag{3}
\]
Nilpotence of \(AB\) implies nilpotence of \(BA\), by
\((BA)^{n+1}=B(AB)^nA\). Thus the trace and determinant of
the two-by-two matrix vanish.

The unchanged function field is \(\mathbb C(p,q)(x)\), using
\(y=p+R(x)\) and \(z=(q+Q(x))/a(p)\). Write
\(\alpha=a'/a\in\mathbb C(p)^*\). The trace equation becomes
\[
-R'f_p+g_p+
\alpha(q+Q)(-R'f_q+g_q)-Q'f_q+ah_q=0.
\tag{4}
\]
Its unique possible term of degree
\(\deg R-1+\deg Q\) in \(x\) is
\(-\alpha R'Qf_q\). This degree is strictly larger than the
degrees of \(R'\), \(Q\), and \(Q'\), because
\(\deg R-1\ge1\) and \(\deg Q\ge2\). Its coefficient must
vanish, and \(\alpha\ne0\), so \(f_q=0\).

The remaining trace is
\(-R'f_p+\alpha Qg_q+(g_p+\alpha qg_q+ah_q)=0\).
If \(1,R',Q\) are linearly independent over \(\mathbb C\),
they remain independent over \(\mathbb C(p,q)\). Hence
\(f_p=g_q=0\).

If those three polynomials are dependent, both \(R'\) and \(Q\)
are nonconstant, so necessarily
\[
R'=cQ+d_0\quad(c\in\mathbb C^*,\ d_0\in\mathbb C),
\qquad g_q=(c/\alpha)f_p,
\qquad
\det(BA)=ah_q(-R'f_p+g_p)+Q'f_pg_q-ah_pg_q.
\tag{5}
\]
The determinant formula follows directly from (3) after \(f_q=0\);
the terms involving \(a'z\) cancel. Substitute \(R'=cQ+d_0\)
in that determinant. The polynomials \(1,Q,Q'\) are linearly
independent over \(\mathbb C(p,q)\), since their degrees are
\(0,\deg Q,\deg Q-1\), all distinct. Its \(Q'\)-coefficient
therefore gives \(f_pg_q=0\). By (5), this is
\((c/\alpha)f_p^2=0\), so again \(f_p=g_q=0\).

In both cases, \(f_q=f_p=g_q=0\). Equation (4) reduces to
\(g_p+ah_q=0\). The reverse product in (3) now has
upper-right entry zero and diagonal entries \(g_p,-g_p\).
Its determinant is \(-g_p^2\), so \(g_p=h_q=0\).
This proves (2). Conversely, the original Jacobian of (2) has
only its third row possibly nonzero, namely
\((-R'h_0',h_0',0)\). Its square is zero. This proves the
converse as well.

## 2. Consequence for an actual line-family frame

Suppose
\[
\begin{gathered}
B=A[u]=\mathbb C[X_1,X_2,X_3,W],\qquad E=\partial_u,
\qquad W=u,\qquad E^2X_i=0,\\
(X_1,X_2,X_3)=(x,y,z)+uV(x,y,z).
\end{gathered}
\tag{6}
\]
Here \(x,y,z\) are the actual good intercepts at \(u=0\).
They are polynomial coordinates of \(A\), since reduction of
the displayed coordinate ring by \((W)\) is \(A\).
The map \(((x,y,z),u)\mapsto((x,y,z)+uV,u)\) has an actual
polynomial inverse. Its determinant \(\det(I+uJ)\) is therefore
a polynomial unit, and its value at \(u=0\) is 1. It follows
that \(J^3=0\), exactly as in the retained line-family
reduction148.[^1]

Let \(T=\partial_W\) hold all three goods fixed. Differentiation
of the actual inverse gives
\(T(x,y,z)^t=-V+uJV-u^2J^2V\), and therefore
\(N=[u^2]T|_A=-(J^2V)\cdot\partial_{x,y,z}\).
For a rank-two dense good-speed cone, this selected \(N\) is
a nonzero LND annihilating the three speeds.[^2]

If its kernel is the subring \(\mathbb C[p,q]\) embedded as
in (1), all speeds satisfy the proposition, contradicting rank
two. The same exclusion only needs their membership in that
subring; equality with the full kernel is not necessary.

The surviving case (2) does give an actual polynomial frame. Its
inverse is
\[
\begin{gathered}
u=W,\qquad x=X_1-c_1W,\qquad y=X_2-c_2W,\\
p=X_2-c_2W-R(X_1-c_1W),\qquad
z=X_3-Wh_0(p).
\end{gathered}
\tag{7}
\]
Substitution in either order returns every coordinate. Its speed
rank is at most one and \(N=0\), because \(J^2=0\). It is
not a dense rank-two example obtained by satisfying a relative
determinant condition alone.

## 3. The excluded kernel really has full residue extensions

The polynomial change \((x,y,z)\mapsto(p,x,z)\), with
inverse \(y=p+R(x)\), identifies the ordinary LND
\[
\delta=a(p)(\partial_x+R'(x)\partial_y)+Q'(x)\partial_z
\]
with \(a(p)\partial_x+Q'(x)\partial_z\) in those changed
coordinates. Its kernel is \(S=\mathbb C[p,q]\): after
inverting \(a\), the ring is \(S[a^{-1}][x]\); at each
root \(p_0\) of \(a\), the specialization
\(q=-Q(x)\) is transcendental over \(\mathbb C\), so the
coefficient-divisibility argument148 contracts the localized
kernel back to \(S\).[^1]

Writing \(k=\mathbb C(q)\), its full divisor fiber is
\[
A_{S\setminus(p-p_0)}/(p-p_0)
\simeq k[x,z]/(Q(x)+q)=\ell[z],
\qquad
\ell=k[x]/(Q(x)+q),\quad [\ell:k]=\deg Q.
\tag{8}
\]
The polynomial \(Q(x)+q\) is irreducible over \(\mathbb C(q)\),
by its primitive linear presentation in \(q\). This is the full
fiber of the ordinary triangular model, not a split fiber of a
smaller projected plane ring.[^3] Repeated roots of \(a\) cause
no change to this calculation.

The nonlinear change in this section is used to compute the kernel
and its fibers. The nilpotence proof in Section 1 instead used the
original \((x,y,z)\)-Jacobian throughout. It did not assume that
nilpotence is preserved by a nonlinear change of the intercepts.

## 4. The remaining placement restriction

The hypotheses here require the simultaneous expressions
\(p=y-R(x)\) and \(q=a(p)z-Q(x)\) in the actual intercepts.
They cover this one nonlinear first-coordinate shear of a standard
triangular quotient. No reduction of all projected or intercept
placements to this form is asserted.

In particular, this proof keeps \(Q\) independent of \(p\).
For a general \(\mathcal Q(p,x)\), the original trace acquires
additional \(\mathcal Q_p\)-terms, and the two ordinary-degree
comparisons used above no longer constitute a proof. The
base-dependent extension148 in a different intercept placement
cannot simply be transported through the nonlinear change here.
No conclusion for that larger family is claimed.

The last coordinate is also required to equal the slice \(u\).
The result neither constructs a nontrivial residue extension for
an actual selected dense frame nor proves all such extensions
trivial. General nonlinear placements, global descent, arbitrary
coordinate entry, and unrestricted cancellation remain outside
this conclusion.

## Sources

1. [A triangular residue-extension kernel cannot support a dense
   line family148](line-family-triangular-kernel-exclusion-pass148-working.md),
   Sections 1--3 and 5. The original-intercept inverse reduction,
   selected-partial formula, and ordinary triangular-kernel
   contraction. Section 4 of that note concerns a different
   base-dependent placement and is not used to infer the present
   nonlinear-intercept statement.
2. [A dense all-degree chart and its formal Taylor
   peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Section 1, equation (2). Nonzero selected leading LND and
   annihilation of the actual good speeds.
3. [A global divisor-residue bound for dense three-good
   frames147](dense-all-degree-divisor-residue-bound-pass147-working.md),
   Sections 2--6. The full-fiber residue-extension question and
   its distinction from a projected-order degeneration.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.

