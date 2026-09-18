# A base-dependent triangular equation cannot support rank-two line-family speeds

The nonlinear-intercept obstruction149 extends to every polynomial
triangular equation, with arbitrary dependence on its base variable.
A polynomial speed row in that coefficient subring, with nilpotent
original Jacobian, cannot have transcendence degree two.

The argument first uses the determinant to restrict the triangular
equation. Ordinary-degree comparisons in the trace finish its
nonresonant branch; a quadratic resonance is excluded by polynomial
coefficient membership. It does not classify all surviving rank-one
speed rows.

## 1. Polynomial-map hypotheses

Let \(x,y,z\) be independent variables over \(\mathbb C\). Fix
\(R\in\mathbb C[x]\), \(a\in\mathbb C[p]\), and
\(\mathcal H\in\mathbb C[p,x]\), with
\[
\begin{gathered}
n=\deg R\ge2,\qquad a\text{ nonconstant},\\
p=y-R(x),\qquad q=a(p)z-\mathcal H(p,x),\\
V=(f(p,q),g(p,q),h(p,q))^t,\qquad f,g,h\in\mathbb C[p,q].
\end{gathered}
\tag{1}
\]
The pair \(p,q\) is algebraically independent, and the unchanged
function field is \(\mathbb C(p,q)(x)\). Write \(K=\mathbb C(p,q)\).
All coefficient subscripts \(p,q\) hold the other coefficient
variable fixed. The subscripts on \(\mathcal H\) instead refer to
its displayed independent variables \(p,x\).

**Theorem.** If \(J=\operatorname{Jac}_{x,y,z}V\) is nilpotent,
then \(\operatorname{trdeg}_{\mathbb C}\mathbb C(f,g,h)\le1\).

In particular no polynomial speed row of rank two satisfies these
hypotheses. The claimed conclusion is only this rank bound, not the
stronger explicit rank-one classification obtained149 when the
triangular polynomial is independent of \(p\).[^1]

## 2. The original determinant restricts the triangular equation

Assume for contradiction that the speed field has transcendence
degree two. Compute the original Jacobian as
\[
\begin{gathered}
J=AB,\qquad
A=\begin{pmatrix}f_p&f_q\\g_p&g_q\\h_p&h_q\end{pmatrix},\\
B=\begin{pmatrix}
-R'&1&0\\
-(a'z-\mathcal H_p)R'-\mathcal H_x&a'z-\mathcal H_p&a
\end{pmatrix},\\
L_1=g_p-R'f_p,\qquad L_2=g_q-R'f_q,\qquad
b=a'z-\mathcal H_p,\\
BA=\begin{pmatrix}
L_1&L_2\\
bL_1-\mathcal H_xf_p+ah_p&bL_2-\mathcal H_xf_q+ah_q
\end{pmatrix}.
\end{gathered}
\tag{2}
\]
The factor \(B\) is the Jacobian of \((p,q)\) in the original
\((x,y,z)\) coordinates. No nilpotence assertion is transported
through a nonlinear coordinate change.

Nilpotence of \(AB\) implies nilpotence of \(BA\), since
\((BA)^{j+1}=B(AB)^jA\). Define the three coefficient minors by
\[
\begin{gathered}
D_{fg}=f_pg_q-f_qg_p,\qquad
D_{fh}=f_ph_q-f_qh_p,\qquad
D_{gh}=g_ph_q-g_qh_p,\\
0=\det(BA)=
\mathcal H_xD_{fg}-aR'D_{fh}+aD_{gh}.
\end{gathered}
\tag{3}
\]
The terms containing \(b\) cancel directly.

At least one of these three minors is nonzero. Indeed, in
characteristic zero an algebraically independent pair among
\(f,g,h\) has independent differentials in the finite separable
extension \(K/\mathbb C(f_i,f_j)\). Its coefficient Jacobian
minor is therefore nonzero.

In fact \(D_{fg}\ne0\). Otherwise (3) would give
\(R'D_{fh}=D_{gh}\). Since \(R'\) is nonconstant in the
independent variable \(x\) and the two minors belong to \(K\),
both minors would vanish as well, a contradiction.

Solving (3) now puts \(\mathcal H_x\) in the \(K\)-span of
\(R'\) and 1. Its two coefficients actually belong to
\(\mathbb C[p]\). To see this, choose a positive-degree
coefficient of \(R'\) that is nonzero. The corresponding
coefficient of \(\mathcal H_x\) is a polynomial in \(p\), so
their quotient determines the \(R'\)-coefficient in
\(\mathbb C[p]\). Comparing constant coefficients gives the
same assertion for the remaining coefficient. Integrating in
\(x\) therefore yields
\[
\mathcal H(p,x)=\lambda_0(p)R(x)+\lambda_1(p)x+\lambda_2(p),
\qquad \lambda_i\in\mathbb C[p].
\tag{4}
\]

## 3. The nonresonant trace branch

The trace of (2) is zero. Substitute
\(z=(q+\mathcal H)/a\) and multiply by \(a\) to obtain
\[
\begin{gathered}
a(g_p-R'f_p)+I_0(g_q-R'f_q)
-a\mathcal H_xf_q+a^2h_q=0,\\
I_0=a'(q+\mathcal H)-a\mathcal H_p.
\end{gathered}
\tag{5}
\]
This identity is in \(K[x]\). Using (4), write
\[
\begin{gathered}
I_0=U(p)R(x)+W_1(p)x+W_0(p,q),\\
U=a'\lambda_0-a\lambda_0',\qquad
W_1=a'\lambda_1-a\lambda_1',\\
W_0=a'q+a'\lambda_2-a\lambda_2'.
\end{gathered}
\tag{6}
\]
First suppose \(U\ne0\).

The only term of degree \(2n-1\) in (5) that can occur is
\(-URR'f_q\). Every other term has degree at most \(n\):
the contribution from \(W_1xR'\) has degree at most \(n\),
and \(\mathcal H_x\) has degree \(n-1\) by (4).
Since \(n\ge2\), one has \(2n-1>n\).
Thus the coefficient of that degree forces \(f_q=0\).

With \(f_q=0\), equation (5) becomes
\(a g_p-aR'f_p+I_0g_q+a^2h_q=0\).
Its only possible term of degree \(n\) is \(URg_q\); all other
terms have degree at most \(n-1\) or one. It follows that
\(g_q=0\). This contradicts \(D_{fg}\ne0\).

In particular no unproved comparison of the arbitrary generic
degree of \(\mathcal H\) with its residual degree is used. The
determinant forces (4) before either trace comparison is made.

## 4. The resonant trace branch

It remains to treat \(U=0\). Characteristic zero gives
\(\lambda_0=k a\) for a constant \(k\in\mathbb C\).
Comparing the coefficients of \(R'\) and 1 in (3), then using
\(D_{fg}\ne0\), gives the following identity of coefficient
one-forms and the resulting reduced trace:
\[
\begin{gathered}
a\,dh=\lambda_1\,df+\lambda_0\,dg,\\
g_p-R'f_p+(V_1x+W)(g_q-R'f_q)=0,\\
\alpha=a'/a,\qquad V_1=\alpha\lambda_1-\lambda_1',\qquad
W=\alpha(q+\lambda_2)-\lambda_2'+\lambda_0,\qquad W_q=\alpha.
\end{gathered}
\tag{7}
\]
For completeness, the determinant comparisons are
\(aD_{fh}=\lambda_0D_{fg}\) and
\(aD_{gh}=-\lambda_1D_{fg}\). Since \(df,dg\) form a
\(K\)-basis of the coefficient differentials, these two identities
give the displayed one-form equality. Substituting its \(q\)
coefficient into (5) changes the coefficient of
\(g_q-R'f_q\) to \(I_0+a\lambda_0\), giving (7).

If \(V_1=0\), independence of 1 and \(R'\) gives
\(g_p+Wg_q=0\) and \(f_p+Wf_q=0\).
Thus the same nonzero coefficient derivation
\(\partial_p+W\partial_q\) kills both \(f\) and \(g\),
and directly \(D_{fg}=0\), a contradiction.

Suppose \(V_1\ne0\). If \(n\ge3\), the unique possible
degree-\(n\) term in (7) is \(-V_1xR'f_q\), so \(f_q=0\).
Then the unique possible term of degree \(n-1\ge2\) is
\(-R'f_p\), so \(f_p=0\). This again contradicts
\(D_{fg}\ne0\).

Finally let \(n=2\), and write \(R'=r x+s\), with
\(r\in\mathbb C^*\). Set \(\lambda=V_1/r\) and
\(\kappa=W-s\lambda\), so that \(\kappa_q=\alpha\).
Expanding (7) in powers of the independent linear polynomial
\(R'\) yields
\[
\begin{gathered}
-\lambda f_q(R')^2+
(-f_p+\lambda g_q-\kappa f_q)R'+g_p+\kappa g_q=0,\\
f_q=0,\qquad f_p=\lambda g_q,\qquad
g_p=-\kappa g_q,\\
g_q=c(p)\in\mathbb C[p]\setminus\{0\},\qquad
c'=-\alpha c,\qquad (ac)'=0.
\end{gathered}
\tag{8}
\]
Here \(f_q=0\) makes \(f\) a polynomial in \(p\).
Since \(\lambda\in\mathbb C(p)^*\), the second equality
puts \(g_q\) in \(\mathbb C(p)\), and its original polynomial
coefficient membership puts it in \(\mathbb C[p]\).
It is nonzero because \(D_{fg}\ne0\). Differentiating the third
equality with respect to \(q\) gives
\(c'=-\kappa_qc=-\alpha c\).
Consequently the nonzero polynomial \(ac\) is constant,
which is impossible because \(a\) is nonconstant. This closes
the last branch and proves the theorem for every \(\mathcal H\).

## 5. Complete rational rank-two boundary

Retain \(\deg R\ge2\), nonconstant polynomial \(a\), and
polynomial \(\mathcal H\), but now permit \(f,g,h\in K\).
There is a rank-two tuple with nilpotent original Jacobian
if and only if it has the following form:
\[
\begin{gathered}
R(x)=\tfrac r2x^2+s x+t_0,\qquad r\in\mathbb C^*,\\
\mathcal H=k a R+B_0(p)x+C_0(p),\qquad
k\in\mathbb C,\quad B_0,C_0\in\mathbb C[p],\\
D=B_0/a,\qquad D'\ne0,\qquad c\in\mathbb C^*,\\
f=f_0-\frac c rD,\qquad
g=g_0+\frac{c(q+C_0)}a-ckp-\frac{cs}rD,\\
h=h_0+kg-\frac c{2r}D^2,\qquad
f_0,g_0,h_0\in\mathbb C.
\end{gathered}
\tag{9}
\]
Necessity follows from the determinant and trace arguments in
Sections 2--4. In the final quadratic branch, rational membership
gives \(f\in\mathbb C(p)\) and \(g_q\in\mathbb C(p)\)
instead of polynomial membership. The same mixed-partial identity
still gives \((a g_q)'=0\). In that branch
\(V_1=-aD'\), \(\lambda=-aD'/r\), and
\(g_q=c/a\) for a nonzero complex constant \(c\).
Integrating \(f_p=\lambda g_q\) gives the displayed \(f\).
Next \(g_p=-\kappa g_q\), where
\(\kappa=\alpha(q+C_0)-C_0'+ka+saD'/r\),
gives the displayed \(g\). These integrations only subtract
displayed rational primitives; no arbitrary rational antiderivative
is assumed. Finally (7) says \(dh=D\,df+k\,dg\), which gives
the displayed \(h\). The joint constants of \(\partial_p\)
and \(\partial_q\) in \(K\) are \(\mathbb C\).

Conversely (9) has
\[
D_{fg}=-\frac{c^2D'}{ra}\ne0,\qquad
a\,dh=B_0\,df+ka\,dg,\qquad
\operatorname{tr}(BA)=\det(BA)=0.
\tag{10}
\]
The trace is the direct substitution in (7), and the one-form
identity gives the determinant in (3). Cayley--Hamilton for the
two-by-two matrix gives \((BA)^2=0\), hence
\((AB)^3=A(BA)^2B=0\). This proves the converse and rank two.
In particular \(g_q=c/a\) rules out polynomial coefficient
membership whenever \(a\) is nonconstant.

The distinction from ambient polynomiality is essential. In (9),
the tuple is polynomial in the original \(x,y,z\) if and only if
\(D\in\mathbb C[p]\). Necessity follows from the formula for
\(f\) and \(\mathbb C(p)\cap\mathbb C[x,y,z]=\mathbb C[p]\),
since \((p,x,z)\) is a polynomial coordinate system.
For sufficiency substitute \(q=a z-kaR-aD x-C_0\) and
\(p=y-R\): then
\(g=g_0+c(z-ky)-cD(p)(x+s/r)\), and all three speeds are
polynomial.

A concrete actual line family lies on this boundary:
\[
\begin{gathered}
p=y-\tfrac12x^2,\quad a=p,\quad
\mathcal H=p^2x,\quad q=pz-p^2x,\quad
V=(-p,q/p,-p^2/2),\\
(X_1,X_2,X_3,W)
=(x-up,\ y+u(z-px),\ z-up^2/2,\ u),\\
\widehat p=X_2-X_1^2/2-WX_3,\quad
x=X_1+W\widehat p,\quad
y=\widehat p+(X_1+W\widehat p)^2/2,\quad
z=X_3+W\widehat p^2/2,\quad u=W.
\end{gathered}
\tag{11}
\]
Substitution of the forward map gives \(\widehat p=p\)
and then recovers \(x,y,z,u\). In the reverse order the
displayed inverse gives \(y-x^2/2=\widehat p\); its first
and third forward coordinates become \(X_1,X_3\), and its
second becomes \(\widehat p+X_1^2/2+WX_3=X_2\).
Thus both polynomial inverse orders hold. The tuple is not in
\(\mathbb C[p,q]^3\), since \(q/p\notin\mathbb C[p,q]\).
It is not a counterexample to the polynomial-coefficient theorem.

For ambient polynomial tuples in (9), a linear change
\(z'=z-ky\), followed by interchanging \(x,y\), puts the
tuple in the established nilpotent-map pattern with all but the
first component in two original variables. Its quadratic
dependence and linear third-variable term overlap the normal form
of Yan and de Bondt, Theorem 2.5.[^3] This is a statement-level
source comparison, not a novelty claim for (9). The coefficient-
subring exclusion above is proved directly and does not invoke
that classification as a substitute for its determinant reduction.

## 6. Application to an actual last-coordinate-slice frame

Suppose
\[
\begin{gathered}
B=A[u]=\mathbb C[X_1,X_2,X_3,W],\qquad
E=\partial_u,\qquad W=u,\qquad E^2X_i=0,\\
(X_1,X_2,X_3)=(x,y,z)+uV(x,y,z),\\
T=\partial_W,\qquad
N=[u^2]T|_A=-(J^2V)\cdot\partial_{x,y,z}.
\end{gathered}
\tag{12}
\]
Here \(x,y,z\) are the actual good intercepts. Reducing modulo
\(W=u\) identifies \(A\) with their polynomial ring.
The actual line-family map has a polynomial inverse, so
\(\det(I+uJ)\) is a constant unit and equals 1 at \(u=0\).
Its characteristic coefficients therefore vanish, giving \(J^3=0\).
Differentiating the actual inverse gives the formula for \(N\)
in (12). These are the retained original-intercept reductions148/149,
not a converse to the Jacobian condition.[^1]

If the three speeds have rank two and dense homogeneous cone,
the selected \(N\) is a nonzero LND killing them.[^2]
If its kernel has the simultaneous embedding in (1), the three
speeds belong to the indicated coefficient subring, contrary to
the theorem. More generally, equality with the full kernel is
unnecessary: speed membership alone suffices.

The original invariant algebra \(A\) is already polynomial in
this last-coordinate-slice branch. The conclusion constrains which
selected intrinsic derivations can arise there; it is not a new
recognition of \(A\) or a cancellation theorem.

## 7. Scope

The polynomial-map theorem needs neither local nilpotence of the
speed vector field \(V\cdot\partial_{x,y,z}\) nor an actual inverse.
Nilpotence of the original Jacobian is enough for its rank-two
exclusion. In the frame application, that necessary condition is
supplied by the actual polynomial inverse.

For rational speeds \(f,g,h\in\mathbb C(p,q)\), the same
determinant reduction and every branch except the last polynomial
contradiction remain valid. In particular rank two is excluded if
\(U\ne0\), or if \(\deg R\ge3\). If there is a root \(p_0\)
of \(a\) with \(\deg_x\mathcal H(p_0,x)\ge2\), then (4)
forces \(\lambda_0(p_0)\ne0\), whereas \(U=0\) would force
\(\lambda_0=ka\). Thus that original specialization premise
still suffices to exclude rational rank-two speeds, including
multiple roots of \(a\).

Section 5 classifies the remaining rational quadratic branch.
The polynomial theorem uses membership in \(\mathbb C[p,q]\),
not merely ambient polynomiality after substitution of \(p,q\).
The actual inverse in (11) demonstrates why those hypotheses cannot
be identified.

The polynomial \(\mathcal H(p,x)\) may have arbitrary base dependence.
There is no specialization premise in the polynomial theorem.
It does not assert that
\(\mathbb C[p,q]\) is the full kernel of an ordinary triangular
LND for every such choice: collapsing specializations at other
roots may enlarge that kernel. The theorem only uses the stated
speed membership.

No classification of the remaining rank-zero or rank-one maps is
claimed. The more precise conclusion149 for \(\mathcal H=Q(x)\)
is retained as its own narrower theorem. Nor is there a reduction
of arbitrary nonlinear intercept placements to
\(p=y-R(x), q=a(p)z-\mathcal H(p,x)\), or a removal of the
hypothesis \(W=u\) in the actual-frame application.
Full divisor residue triviality, global descent, arbitrary
coordinate entry, and unrestricted cancellation remain unresolved.

## Sources

1. [Nonlinear-intercept obstruction149](nonlinear-intercept-triangular-kernel-exclusion-pass149-working.md),
   Sections 1--2, and [line-family obstruction148](line-family-triangular-kernel-exclusion-pass148-working.md),
   Sections 2 and 4--5. The original-intercept Jacobian convention,
   inverse implication, selected-partial formula, and the distinction
   between a polynomial-map condition and an actual frame.
   The determinant reduction and rank-two proof above are reproduced
   in full and do not assume the missing base-dependent step149.
2. [Dense all-degree chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Section 1, equation (2). Nonzero selected leading LND and
   annihilation of the actual good speeds. No quotient-surface
   recognition theorem is used in the polynomial-map proof.
3. D. Yan and M. de Bondt, [*The classification of some polynomial
   maps with nilpotent Jacobians*](https://arxiv.org/pdf/1710.04210v3),
   Theorem 2.5, printed page 7. The theorem concerns polynomial maps
   whose components except the first belong to two original variables,
   with zero constant term and linearly independent components.
   Only the displayed statement was independently compared here.
   Subtracting the constant tuple in the ambient polynomial branch
   of (9) gives the appropriate zero-constant-term setting; the
   third-variable term and nonconstant \(D,D^2\) give independence.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
