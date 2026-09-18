# Actual field return forces the zero-r coefficient curve

**Status: working proof under the explicit coefficient-normal-form inputs below.**

In the nonzero-s, zero-r actual cusp branch, the coefficient normal
form173 and the original polynomial inverse force the remaining
line-pencil coefficient to be complex. The projected coordinates
then admit a triangular polynomial change over \(\mathbb C\),
and the exact coefficient-constant field is \(K=\mathbb C(R_{00})\).

This is a field-forcing statement. Its projected coordinate change
is not asserted to be a coordinate change in the original four-ring.
In particular, the proof does not divide by the selected speed in
that ring or assume that this speed is a unit.

## 1. Actual hypotheses and the normal-form inputs

Retain the full actual hypotheses of
[cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md):
\(B=A[u]=\mathbb C[X,Y,Z,W]\), \(E=\partial_u\), exact time
degrees \((1,1,2,2)\), and full weighted initial kernel
\((\mathsf X\mathsf Z-\mathsf Y^3)\). Use the selected
\(N=[u^3](\partial_Z|_A)\), the exact coefficient field
\(L=\operatorname{Frac}(\ker_A N)\), and its commuting coefficient
partials with respect to \(t=EY/EX\) and rho. The speed \(EX\)
is nonzero, not necessarily a unit.

Assume \(r=k_\rho=0\), \(s=n_\rho\ne0\). The
[zero-r reduction160](cusp-zero-r-generic-graph-pass160-working.md)
gives \(y\) as an affine parameter of the whole generic line.
In particular,
\[
\begin{gathered}
K:=\ker_L\partial_\rho,\qquad [K:\mathbb C(t)]<\infty,
\qquad\ker_K\partial_t=\mathbb C,\\
k\in K,\qquad h=k''/2,\qquad
\operatorname{Frac}A=\mathbb C(y,z,w)=L(y),\qquad
z=n+3ty^2+k'y,\qquad w=R(y).
\end{gathered}
\tag{1}
\]
A prime denotes the coefficient derivative on \(K\). The element
\(y\) is transcendental over \(L\), and \(n\) is transcendental
over \(K\), since \(\partial_\rho n\ne0\).

The statements about \(K\) use the exact finite separable field
\(L/\mathbb C(t,\rho)\). For completeness, differentiating the
monic minimal polynomial of a rho-constant element shows that its
coefficients lie in \(\mathbb C(t)\). This gives algebraicity;
independence remains after adjoining the transcendental rho, so
the finite degree of \(L\) bounds that of \(K\). Applying both
derivatives shows that their common constants are algebraic over
\(\mathbb C\), hence equal to \(\mathbb C\). This does not yet
identify \(K\) with a rational function field.

Use precisely the conclusions of
[the coefficient normal form173](cusp-zero-r-coefficient-normal-form-pass173-working.md).
To avoid confusing its quadratic coefficient with \(EX\), call
it \(a_2\). To avoid confusing a scalar with a derivation, call
its remaining scalar \(d_*\). The inputs used here are
\[
\begin{gathered}
\rho=a_2n^2+bn+c,\qquad a_2\in\mathbb C,\quad b,c\in K,
\qquad q:=1/s=2a_2n+b\ne0,\\
q\ell=-\frac{2a_2h'}3n^2+M_1n+M_0,
\qquad M_1,M_0\in K,\\
a_2h''=0,\qquad b''=-\frac{4a_2}3hh',\\
M_1'=-\frac{b'h'}3-\frac{bh''}{12},\qquad
M_1''=\frac{4a_2}9h(h')^2,\\
\gamma=\frac{a_2(h')^2}{9},\qquad
d_* =\frac{c'''}6-\frac{h'M_1}3-hM_1',\qquad
M_0''=2hd_* .
\end{gathered}
\tag{2}
\]
The possibility \(a_2=0\) is included. We do not infer \(h''=0\)
in that case. The second equation for \(M_1\) in (2) is an
explicit normal-form input, not an unjustified derivative consequence
of the first equation after dividing by \(a_2\).

Here is the polynomial form of the same inputs. For an independent
variable \(U\), put
\[
\begin{gathered}
F(U)=U^3+hU^2,\qquad N_0(U)=3tU^2+k'U,\\
Q(U)=\frac{2a_2h'}3U^3+\frac{2a_2hh'}3U^2+M_1'U+d_*,\\
C_0(U)=a_2F(U)^2-b'UF(U)-\frac{bh'}3U^3
 +\frac{c''}2U^2+M_0'U-M_1F(U)+R_{00},\\
R(U)=\gamma n^2+Q(U)n+C_0(U),\qquad R_{00}\in K .
\end{gathered}
\tag{3}
\]
Thus every coefficient in \(z,w\), viewed as polynomials in
\(y,n\), belongs to \(K\).

Let \(D_n=q\partial_\rho\), so that \(D_n n=1\), and let
\(\nabla_t\) be the coefficient derivation extending the prime
on \(K\) and fixing \(n\). In the finite separable extension
these are the partials in \((t,n)\). They commute and fix the
formal variable \(U\). The remaining actual determinant identity
from the normal form says
\[
\mathcal D R(U)\in L^*,\qquad
\mathcal D:=\nabla_t-F_U(U)D_n .
\tag{4}
\]
In particular it is a scalar polynomial in \(U\). This is the
full constant-determinant constraint, not merely its highest terms.
The derivation \(\mathcal D\) is used over the field and polynomial
ring in \(U\); it is not asserted to be an original-ring LND.

The normal-form proof supplies (2)--(4). The new argument below
uses actual field equality in (1) to constrain those coefficients.

## 2. Exact field return and a polynomial line pencil

From (1) and (3),
\[
L(y)=\mathbb C(y,z,w)\subset K(n)(y)\subset L(y).
\]
Both inclusions are equalities. Intersecting with \(L\) proves
\[
L=K(n),\qquad
\mathbb C(y,z,w)=K(y)(z).
\tag{5}
\]
For the intersection, if \(F_0\subset L\) is a field and \(y\)
is transcendental over \(L\), then \(F_0(y)\cap L=F_0\).
Express an element of the intersection as a quotient of polynomials
in \(y\) over \(F_0\), cross-multiply, and compare any nonzero
denominator coefficient. Apply this with \(F_0=K(n)\).
The second equality in (5) also uses \(z=n+N_0(y)\), so \(z\)
is transcendental over \(K(y)\). No equality in (5) follows from
a nonzero Jacobian alone.

Substitute \(n=z-N_0(y)\) in (3). It gives
\[
\begin{gathered}
w-\gamma z^2=f(y)z+g(y),\\
f(U)=Q(U)-2\gamma N_0(U)=F_3U^3+F_2U^2+F_1U+d_*,\\
F_3=\frac{2a_2h'}3,\qquad
F_2=\frac{2a_2hh'}3-6\gamma t,\qquad
F_1=M_1'-2\gamma k',\\
g(U)=C_0(U)-Q(U)N_0(U)+\gamma N_0(U)^2\in K[U].
\end{gathered}
\tag{6}
\]
The identities (2) imply
\[
\gamma,F_3,F_2,F_1\in\mathbb C .
\tag{7}
\]
Indeed \(\gamma'=2a_2h'h''/9=0\) and \(F_3'=0\).
For \(F_2\), its derivative is
\(2a_2((h')^2+hh'')/3-6\gamma=0\).
Finally \(F_1'=M_1''-2\gamma k''=0\) since \(k''=2h\).
The constants assertion uses the proved constant field of \(K\).

## 3. The exact pencil-degree consequence

Suppose for contradiction that \(d_*\notin\mathbb C\).
Set \(k_b=\mathbb C(y)\) and \(M=K(y)\). Then \(M/k_b\)
has transcendence degree one, and (6)--(7) make \(f(y)\)
transcendental over \(k_b\). The element \(z\) is transcendental
over \(M\). Write \(w_1=w-\gamma z^2\). Because \(\gamma\)
is complex, (5) becomes
\[
w_1=f(y)z+g(y),\qquad
k_b(z,w_1)=M(z),\qquad M=k_b(f(y),g(y)).
\tag{8}
\]
The final equality needs proof. The intermediate fields
\(k_b(z,w_1)\subset k_b(f(y),g(y))(z)\subset M(z)\) are equal
by the middle equality. Intersect with \(M\) and use the same
indeterminate-field intersection argument as in Section 2.

The elementary pencil lemma166 now implies
\(g(y)\in k_b+k_b f(y)=k_b+k_b d_*\).
Its short algebraic proof is recalled to specify the exact degree
being used. Let \(\mathcal R(S,T)\) generate the full prime
relation ideal of \((f(y),g(y))\) over \(k_b\), and put
\(d=\deg\mathcal R\), the total degree. Adjoining a variable
\(z\) preserves irreducibility. The polynomial change
\(T\mapsto w_1-zS\) preserves it too. Its leading coefficient
as a polynomial in \(S\) is
\(\mathcal R_d(1,-z)\ne0\); its \(S\)-degree is exactly \(d\).
Gauss's lemma therefore gives
\([M(z):k_b(z,w_1)]=d\). Here \(z,w_1\) are independent over
\(k_b\), since any putative relation's leading part would give
a nonzero polynomial vanishing at the transcendental \(f(y)\).
Equation (8) makes \(d=1\), and the resulting linear relation
solves for \(g(y)\) as an affine expression in \(f(y)\).

Since \(g\in K[U]\), this implies coefficientwise
\[
[U^j]g(U)\in\mathbb C+\mathbb C d_*
\quad\text{for every }j .
\tag{9}
\]
To justify the coefficient return, take a complex basis for the
finite-dimensional span of \(1,d_*\) and all coefficients of
\(g\), beginning with \(1,d_*\). It stays independent over
\(\mathbb C(y)\): clear polynomial denominators and compare powers
of the transcendental \(y\). Comparison in that basis proves
(9). Rationality of \(K\) was not assumed.

## 4. Two coefficients rule out a nonconstant d-star

The coefficient of \(U\) in (6) is
\[
g_1:=[U]g=M_0'-d_*k',\qquad g_1'=-d_*'k'.
\tag{10}
\]
The derivative formula uses exactly \(M_0''=2hd_*\) and
\(k''=2h\). By (9), write \(g_1=u_1+v_1d_*\), with
\(u_1,v_1\in\mathbb C\). The assumed nonconstancy of \(d_*\)
gives \(d_*'\ne0\), so differentiation of (10) forces
\(k'=-v_1\in\mathbb C\). Hence \(h=0\).

Now \(h'=h''=0\), \(\gamma=F_3=F_2=0\), and the first
equation for \(M_1'\) in (2) gives \(F_1=M_1'=0\).
Also \(d_*=c'''/6\). Equation (6) therefore simplifies enough
to identify a second coefficient:
\[
g_2:=[U^2]g=\frac{c''}2-3td_*,\qquad
g_2'=-3t d_*'.
\tag{11}
\]
In fact \(g=a_2U^6-b'U^4-M_1U^3+g_2U^2+g_1U+R_{00}\)
in this subcase. Writing \(g_2=u_2+v_2d_*\) by (9) and
differentiating (11) would give \(t=-v_2/3\in\mathbb C\),
contrary to the actual independent ratio \(t\).
Thus the supposition was impossible, and
\[
d_*\in\mathbb C,\qquad f\in\mathbb C[U].
\tag{12}
\]
Both coefficient comparisons concern \([U]g\) and \([U^2]g\),
not derivatives of \(g\) with respect to \(U\).

## 5. The coefficient curve and projected coordinate

Evaluate the scalar identity (4) at \(U=0\). Since
\(F_U(0)=0\), \(R(0)=\gamma n^2+d_*n+R_{00}\), and
\(\gamma,d_*\) are complex, it gives
\(\mathcal D R=R_{00}'\in K^*\).
On the other hand, \(\mathcal D\) fixes \(U\) and
\(z_0:=n+N_0(U)\): indeed \(\nabla_t N_0=3U^2+k''U=F_U\)
and \(D_nz_0=1\). Apply it to the identity
\(R(U)=\gamma z_0^2+f(U)z_0+g(U)\). Equations (7) and (12)
show that only the coefficients of \(g\) contribute. Therefore
\[
g'(U)=R_{00}',\qquad
g(U)=G(U)+R_{00},\quad G\in\mathbb C[U],\quad G(0)=0 .
\tag{13}
\]
The last normalization follows directly from (6), where
\(C_0(0)=R_{00}\) and \(N_0(0)=0\). The ordinary degree
of \(G\) is at most six.

Consequently the projected polynomial ring has the explicit
triangular coordinate change and inverse
\[
R_{00}=w-\gamma z^2-f(y)z-G(y),\qquad
w=R_{00}+\gamma z^2+f(y)z+G(y),\qquad
\mathbb C[y,z,w]=\mathbb C[y,z,R_{00}].
\tag{14}
\]
Both identities have complex coefficients, and substitution in
either direction fixes the three independent projected variables.
The nonzero derivative \(R_{00}'\) shows that \(R_{00}\) is
not complex.

Finally, actual field return and (5) give
\(\mathbb C(R_{00})(y,z)=K(y,z)\). The variables \(y,z\)
are algebraically independent over \(K\). Intersecting with
\(K\), by the two-variable version of the same elementary
intersection argument, proves
\[
K=\mathbb C(R_{00}),\qquad L=\mathbb C(R_{00})(n).
\tag{15}
\]
This rationality is a conclusion, not an input to the pencil proof.

## Scope and dependencies

The new field argument retains the complete coefficient-normal-form
identities173. It neither obtains them by assuming \(K=\mathbb C(t)\)
nor integrates unspecified algebraic coefficient functions. The only
pencil input is the elementary degree lemma, reproduced above from
[the actual field-return proof166](cusp-quartic-actual-field-recognition-pass166-working.md),
Sections 3--4. No new external theorem is invoked here.

Although (14) is an actual polynomial identity in the projected
three-ring, those projected coordinates originate in the localization
at \(EX\). It proves \(R_{00}\in A_{EX}\cap L\), not that
\(R_{00}\) is a polynomial coordinate of the original four-ring.
The integral coordinate construction and its recognition endpoint
are separate obligations. The square-root coefficient cover in
the actual boundary171 is compatible with (15).

No171 or earlier source or checker is changed. This note makes no
claim of unrestricted cancellation, historical novelty, human expert
certification, proof-assistant verification, or a recursive audit of
all earlier results. Finite symbolic controls do not replace the
exact field and polynomial arguments written here.
