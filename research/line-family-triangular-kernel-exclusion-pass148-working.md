# A triangular residue-extension kernel cannot support a dense line family

Consider an actual line-family frame with last coordinate equal to the
chosen slice. If its three speeds belong to the triangular coefficient
subring below in the original good-intercept coordinates, nilpotence
of their Jacobian forces all speeds to depend on one variable. Thus
this construction cannot realize a rank-two dense selected intrinsic
derivation with that kernel.

The conclusion concerns a specified embedding of the kernel in the
intercept polynomial ring. It does not rule out arbitrary nonlinear
conjugate embeddings or frames with a different last coordinate.

## 1. The polynomial-map statement

Let \(p,y,z\) be independent variables over \(\mathbb C\). Choose
\(a\in\mathbb C[p]\) nonconstant and \(P\in\mathbb C[y]\) with
\(d=\deg P\ge2\), and set
\[
q=a(p)z-P(y),\qquad
H=(f(p,q),g(p,q),h(p,q))^t,\qquad
f,g,h\in\mathbb C[p,q].
\tag{1}
\]
The elements \(p,q\) are algebraically independent. In particular,
partials with subscripts \(p,q\) below are derivatives in that
polynomial coefficient ring, not original-coordinate derivatives.

**Proposition.** The original Jacobian
\(J=\operatorname{Jac}_{p,y,z}H\) is nilpotent if and only if
\[
H=(c,g_0(p),h_0(p))^t,
\qquad c\in\mathbb C,\quad g_0,h_0\in\mathbb C[p].
\tag{2}
\]
In particular its speed field has transcendence degree at most one.

To prove this, factor the original Jacobian, in the stated coordinate
order, as
\[
J=AB,\qquad
A=\begin{pmatrix}f_p&f_q\\g_p&g_q\\h_p&h_q\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0&0\\a'z&-P'&a\end{pmatrix},
\qquad
BA=\begin{pmatrix}
f_p&f_q\\
a'zf_p-P'g_p+ah_p&a'zf_q-P'g_q+ah_q
\end{pmatrix}.
\tag{3}
\]
If \(AB\) is nilpotent, so is \(BA\), since
\((BA)^{n+1}=B(AB)^nA\). Its trace and determinant therefore
vanish. Work in the unchanged function field, written as
\(\mathbb C(p,q)(y)\), by substituting
\(z=(q+P(y))/a(p)\). The trace identity is
\[
f_p+\frac{a'}a(q+P(y))f_q-P'(y)g_q+ah_q=0.
\tag{4}
\]
Its coefficient of \(y^d\) is the nonzero leading coefficient of
\(P\), times \((a'/a)f_q\). Characteristic zero and the
nonconstancy of \(a\) imply \(a'/a\ne0\), so \(f_q=0\).
The coefficient of \(y^{d-1}\) then forces \(g_q=0\), because
\(d-1\ge1\). The remaining trace equation is
\(f_p+ah_q=0\).

With \(f_q=g_q=0\), the two diagonal entries of \(BA\) are
\(f_p\) and \(ah_q=-f_p\), and its upper-right entry is zero.
Consequently \(\det(BA)=-f_p^2\). Vanishing of the determinant
gives \(f_p=0\), and then \(h_q=0\). This is exactly (2).
Conversely, the Jacobian of (2) has only its first column possibly
nonzero and has zero first row. Its square is zero, proving the
converse.

All field substitutions above are coefficient calculations. No
coordinate change is used to infer nilpotence of a different
Jacobian.

## 2. Application to an actual last-coordinate slice

Suppose
\[
B=A[u]=\mathbb C[X_1,X_2,X_3,W],\qquad
E=\partial_u,\quad W=u,\quad E^2X_i=0.
\tag{5}
\]
These are actual polynomial coordinates. Reducing modulo \(u=W\)
shows that the intercepts \(x_i=X_i|_{u=0}\) are independent
polynomial generators of \(A\). In these particular coordinates,
\(X_i=x_i+uH_i(x)\). The map
\((x,u)\mapsto(x+uH(x),u)\) is an actual polynomial
automorphism, with an actual polynomial inverse.[^1]

Its determinant is \(\det(I+uJ)\). A polynomial automorphism
has a nonzero constant Jacobian determinant; at \(u=0\) this
one is 1. Hence \(\det(I+uJ)=1\). Comparison of the three
characteristic coefficients, followed by Cayley--Hamilton over
\(\mathbb C[x]\), gives \(J^3=0\).

For completeness, the actual partial \(T=\partial_W\), holding
the three \(X_i\) fixed, satisfies
\[
T(u)=1,\qquad
T(x)=-(I+uJ)^{-1}H=-H+uJH-u^2J^2H,
\qquad
N=[u^2]T|_A=-(J^2H)\mathbin{\cdot}\partial_x.
\tag{6}
\]
This follows by differentiating \(x+uH(x)\) under the actual
partial and using \((I+uJ)^{-1}=I-uJ+u^2J^2\).
It does not infer a polynomial inverse from nilpotence alone.

If the speeds have rank two and dense homogeneous cone, the retained
selected-cofactor result says that this \(N\) is a nonzero LND
annihilating all three speeds.[^2] Suppose its kernel, in the
intercept coordinates \((x_1,x_2,x_3)=(p,y,z)\), is
\(\mathbb C[p,a(p)z-P(y)]\), with the hypotheses of Section 1.
Then all three speeds have the form (1). The proposition contradicts
their rank two. More generally, the same exclusion holds if all
speeds merely belong to that displayed subring.

There is no failure of invertibility hidden in the surviving case
(2). It gives the actual triangular inverse
\[
u=W,\qquad
p=X_1-cW,\qquad
y=X_2-Wg_0(X_1-cW),\qquad
z=X_3-Wh_0(X_1-cW).
\tag{7}
\]
Substitution in either order returns each of the four variables.
Its selected \(N\) is zero because \(J^2=0\), and its speed
field has rank at most one. Thus it lies outside the target dense
rank-two setting for explicit reasons.

## 3. Why this is a residue-extension model

The ordinary triangular LND
\(\delta=a(p)\partial_y+P'(y)\partial_z\) kills \(p,q\).
After inverting \(a\), its kernel is
\(\mathbb C[p,a^{-1},q]\), since the ring is
\(\mathbb C[p,a^{-1},q,y]\) and \(\delta=a\partial_y\).
Its kernel before localization is exactly \(S=\mathbb C[p,q]\).
Indeed, at any root \(\alpha\) of \(a\), reduction sends
\(q\) to \(-P(y)\), a transcendental element over \(\mathbb C\).
Thus a polynomial \(F(p,q)\) becomes divisible by \(p-\alpha\)
in \(\mathbb C[p,y,z]\) only if all its \(q\)-coefficients
are divisible by \(p-\alpha\). Repeatedly removing such factors
clears every possible denominator in \(a\).

At the height-one prime \((p-\alpha)\subset S\), put
\(k=\mathbb C(q)\). The full divisor fiber of this abstract
triangular model is
\[
\mathbb C[p,y,z]_{S\setminus(p-\alpha)}
 /(p-\alpha)
\simeq k[y,z]/(P(y)+q)
=\ell[z],\qquad
\ell=k[y]/(P(y)+q),\quad [\ell:k]=d.
\tag{8}
\]
Here \(P(Y)+q\) is irreducible over \(\mathbb C(q)\): it is
irreducible in \(\mathbb C[q,Y]\), being monic linear in \(q\),
and is primitive over \(\mathbb C[q]\). Its degree in \(Y\)
is \(d\). This applies at every root of \(a\), with no
simple-root hypothesis on \(a\).

Thus the abstract kernel does exhibit the nontrivial full residue
constants sought in the divisor bound147.[^3] The proposition proves
that this particular embedding cannot be the selected kernel of a
dense line family (5). It does not mistake a split fiber of a smaller
projected ring for the full fiber in (8).

## 4. Extension to a base-dependent triangular equation

The same polynomial-map classification holds in a larger family.
Replace (1) by
\[
\begin{gathered}
q=a(p)z-\mathcal H(p,y),\qquad
\mathcal H\in\mathbb C[p,y],\qquad
H=(f(p,q),g(p,q),h(p,q))^t,\\
a(p_0)=0,\qquad
P_0(y)=\mathcal H(p_0,y),\qquad d=\deg P_0\ge2 .
\end{gathered}
\tag{9}
\]
As before, \(a\) is a nonconstant polynomial and \(f,g,h\) are
polynomials in \(p,q\). There is no bound on the generic degree
of \(\mathcal H\) in \(y\).

The factorization (3) now has second row of \(B\) equal to
\((a'z-\mathcal H_p,-\mathcal H_y,a)\). Nilpotence of the
original Jacobian still forces the reverse product to have trace
zero. Substituting \(z=(q+\mathcal H)/a\) and multiplying the
trace by \(a\) gives
\[
a f_p+I_0 f_q-a\mathcal H_y g_q+a^2h_q=0,
\qquad
I_0=a'(q+\mathcal H)-a\mathcal H_p.
\tag{10}
\]
The first and last terms are constant in \(y\).

Put \(\pi=p-p_0\), and write \(a=\pi^e b(\pi)\), with
\(e\ge1\) and \(b_0=b(0)\ne0\). Expansion at this divisor gives
\(I_0=e b_0(q+P_0)\pi^{e-1}+O(\pi^e)\) and
\(\mathcal H_y=P_0'+O(\pi)\). The derivative
\(\mathcal H_p\) is polynomial, so its contribution begins at
order at least \(e\).

If \(f_q\ne0\), let \(n\) be its order in \(\pi\) and let
\(c(q)\ne0\) be its leading coefficient. The first nonzero
\(y\)-nonconstant coefficient of \(I_0f_q\) occurs at order
\(n+e-1\); its full leading coefficient is
\(e b_0(q+P_0)c(q)\), of degree \(d\) in \(y\).
If \(g_q\ne0\), define its order \(m\) and leading coefficient
\(c_1(q)\ne0\) similarly. The term
\(-a\mathcal H_y g_q\) first occurs at order \(m+e\), with
coefficient \(-b_0P_0'c_1(q)\), of positive degree \(d-1\).

If just one of these two derivatives is nonzero, its nonconstant
coefficient cannot be canceled in (10). If both are nonzero and
their displayed orders differ, the earlier nonconstant coefficient
cannot be canceled. If the orders agree, their degrees \(d\)
and \(d-1\) differ, again preventing cancellation. Consequently
\(f_q=g_q=0\).

Equation (10) reduces to \(f_p+ah_q=0\). The reverse product
then has upper-right entry zero and diagonal entries \(f_p,-f_p\),
so its determinant is \(-f_p^2\). Exactly as in Section 1,
\(f_p=h_q=0\), proving (2). Its converse and the actual inverse
(7) are unchanged. The actual line-family exclusion in Section 2
therefore also holds whenever its three speeds belong to the
subring in (9), in the original intercept coordinates.

This extension includes base-dependent polynomial shears of the
third triangular coordinate: adding a multiple of \(a(p)\) to
\(\mathcal H\) does not change \(P_0\). It makes no assertion
that \(\mathbb C[p,q]\) is automatically the full kernel for
every \(a,\mathcal H\). At other roots of \(a\), a constant
specialization can enlarge that kernel. The application only
requires the stated membership of the three speeds.

## 5. Exact scope

The normalization to intercept coordinates in Section 2 is forced
by the actual frame. An arbitrary nonlinear automorphism of
\(A\) can put a derivation or its kernel into a different form,
but it also changes the expressions of the three intercepts. One
cannot then retain both the identity-intercept form
\(x+uH(x)\) and the newly chosen kernel embedding without an
additional argument. The proposition concerns their simultaneous
placement, not abstract isomorphism of kernels or conjugacy of LNDs.

The hypotheses \(W=u\) and \(a\) nonconstant are retained in
the applications. The nonlinear polynomial is \(P\) in Sections
1--3, or the specified specialization \(P_0\) in Section 4.
No assertion about arbitrary last-degree
frames, all nonlinear conjugates, or triviality of every full
divisor residue extension is made. The obstruction uses the actual
inverse only to obtain a necessary nilpotent-Jacobian condition;
the matrix and coefficient argument itself is elementary.

## Sources

1. [A line-family construction criterion and an elementary-shear
   obstruction75](nice-good-direction-construction-boundary-pass75.md),
   Section 1. The actual inverse and nilpotent-Jacobian reduction are
   reproduced here for the last-coordinate slice convention.
2. [A dense all-degree chart and its formal Taylor
   peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Section 1, equation (2). Only the nonzero selected leading LND
   and its annihilation of the speeds are used in the application.
3. [A global divisor-residue bound for dense three-good
   frames147](dense-all-degree-divisor-residue-bound-pass147-working.md),
   Sections 2--6. The distinction between a full divisor residue
   extension and a projected-order fiber, and the unresolved
   actual-realization question motivating (8).

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
