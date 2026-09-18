# Original-ring recognition in the absent-variable nonzero-R branch

**Status: working recognition proof for a supplied actual initial configuration.**

Assume the full actual hypotheses of the nonzero-\(R\)
[quartic-graph reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md).
This note solves its remaining coefficient gates and constructs an
invariant coordinate in the original polynomial four-ring, with an
explicit polynomial inverse. A published regular-kernel theorem then
recognizes the invariant ring. This is a restricted case, not an
unrestricted cancellation proof or an arbitrary-entry argument.

## 1. Actual input and the calibrated line parameter

Write
\[
\begin{gathered}
 B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
 \mathcal A=\ker E,\qquad
 \deg_E(X,Y,Z,W)=(1,1,2,2),\\
 \ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4),\qquad
 L=\operatorname{Frac}(\ker_{\mathcal A}N),\quad
 \mathcal A_L=L[v],\quad Nv=1,\\
 a_E=EX\in L^*,\quad t=EY/a_E,\quad
 \rho=(E^2W/2)/a_E^2,\quad [L:\mathbb C(t,\rho)]<\infty,\\
 K=\ker_L\partial_\rho,\qquad [K:\mathbb C(t)]<\infty,\qquad
 \ker_K\partial_t=\mathbb C .
\end{gathered}
\tag{1}
\]
Here \(N\) is the actual selected leading LND supplied by184.
The initial ideal is the whole kernel. It is not merely one
vanishing relation.

Assume \(R=k_\rho\ne0\) and \(y\notin L\).
Reduction189 gives constants \(\alpha,\beta,c\in\mathbb C\) and
\(k_0,n_0\in K\) such that
\[
\begin{gathered}
 \chi=\alpha t+\beta,\qquad r=R=\chi^{-1},\qquad
 (\alpha,\beta)\ne(0,0),\\
 k=r\rho+k_0,\qquad n=c r^2\rho+n_0,\qquad
 y=\Gamma v+\eta,\quad \Gamma=Ny\in L^*,\quad \eta\in L,\\
 \vartheta\in L[y],\quad \deg_y\vartheta=4,\qquad
 L[y,z,w]=L[y],\qquad \mathbb C(y,z,w)=L(y).
\end{gathered}
\tag{2}
\]
The displayed ring equality just asserts that the three projected
entries generate the entire line over \(L\).
No rationality of \(K\) is assumed.

The actual chart and its determinant are
\[
\begin{gathered}
 Y=y+tX,\qquad
 Z=z+(4t^3y+k)X+t^4X^2,\qquad
 W=w+\vartheta X+\rho X^2,\\
 \det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
     =-\frac{a_E^3}{\Gamma}\in L^* .
\end{gathered}
\tag{3}
\]
In (3), \(X\) is held fixed. The determinant is independent of \(X\).
Changing the old normalized line parameter \(v\) to \(y\)
divides the original determinant by \(\Gamma\); that factor is
retained throughout. Coefficient partials initially on \(L\)
extend to \(L[y]\) by fixing \(y\).
The original derivation acts as \(E=a_E\partial_X\), fixing
\(L(y)\).

## 2. A coefficient-field coordinate and literal elimination

Primes on \(K\) continue to mean its \(t\)-derivative.
Set
\[
\begin{gathered}
 D=5\alpha t+\beta\ne0,\\
 F_3=\frac{\chi k_0'''}6+\frac{\alpha k_0''}2-4ct,\qquad
 F_2=\frac{\chi n_0''}2+\alpha n_0'-\frac{c k_0''}2,\\
 p(U)=(-10\alpha t^2-4\beta t)U^3
       +\left(6ct^2-\frac{\chi k_0''}2-\alpha k_0'\right)U^2
       +(c k_0'-\chi n_0'-\alpha n_0)U,\\
 F(U)=D U^4+F_3U^3+F_2U^2,\qquad p_t=-F_U .
\end{gathered}
\tag{4}
\]
The nonzero \(D\) also follows from the nonvanishing quartic
coefficient in189; the affine polynomial \(D\) cannot vanish
identically when \((\alpha,\beta)\ne(0,0)\).

Define an element of the exact coefficient field by
\[
 h=\chi\ell+c^2r^2\rho+c n_0 .
\tag{5}
\]
The first potential and the formula for \(z\) imply
\[
 w=(\alpha y-c)z+p(y)+h .
\tag{6}
\]
Here the cancellation of the nonconstant \(\rho\) terms in the
coefficients of \(y^2\) and \(y\) is literal:
\(r'=-\alpha r^2\), \(r''=2\alpha^2r^3\), and
\((cr^2)'=-2\alpha cr^3\).
For example the coefficient of \(y^3\) before simplification is
\(-4t/r-6\alpha t^2\), giving the first coefficient in (4).
The constant coefficient in (6) is exactly (5), not an omitted
coefficient-field correction.

In the pure quartic-graph eliminant of189, the coefficient of
\(V\) is
\(\omega=-r\ell_\rho-c^2r^4\in L^*\).
Consequently
\[
 h_\rho=\chi\ell_\rho+c^2r^2=-\omega/r^2\ne0 .
\tag{7}
\]
In particular \(h\) is transcendental over \(K\), and \(L/K(h)\)
is finite separable. Define the new coefficient partials by
\[
 \partial_h=(h_\rho)^{-1}\partial_\rho,\qquad
 \partial_t^{\,h}=\partial_t^{\,\mathrm{old}}
      -\frac{h_t^{\,\mathrm{old}}}{h_\rho}\partial_\rho .
\tag{8}
\]
They commute, fix respectively \(t\) and \(h\), and
\(\ker_L\partial_h=K\).
Below a \(t\)-subscript on an element of \(L\) uses
\(\partial_t^{\,h}\); on \(K\) it is the same prime as before.
These are exact derivations on the given finite field, not a
premature assertion that \(L=K(h)\).

For completeness, substitution into the pure eliminant gives
the following entire projected polynomial:
\[
\begin{gathered}
 z=r\rho_h F(y)+6t^2y^2+(r\rho+k_0)_t\,y+z_0,\\
 z_0=n+\rho_h(-m+cr\ell)\in L .
\end{gathered}
\tag{9}
\]
One can check (9) coefficientwise before changing derivations.
The coefficients of \(y^4,y^3,y^2\), other than \(6t^2\),
are respectively
\[
 \frac{rD}{h_\rho},\qquad
 \frac{k_0'''/6+\alpha r k_0''/2-4ctr}{h_\rho},\qquad
 \frac{n_0''/2+\alpha r n_0'-cr k_0''/2}{h_\rho}.
\]
The coefficient of \(y\) is
\(k_t^{\,\mathrm{old}}-r h_t^{\,\mathrm{old}}/h_\rho
=(r\rho+k_0)_t\).
This verifies both the formal coefficient differentiation and
the change of field partials used in (9).

At \(X=0\), (6) and (3) give the exact scalar equation
\[
 \delta z\in L^*,\qquad
 \delta=\partial_t^{\,h}+F_U(y)\partial_h,\qquad
 \delta z=-\frac{a_E^3\rho_h}{\Gamma}.
\tag{10}
\]
Indeed the old determinant is
\(h_\rho z_t^{\,\mathrm{old}}
 -(p_t+h_t^{\,\mathrm{old}})z_\rho\).
Using (8) and \(p_t=-F_U\) gives (10).
The right side is independent of \(y\), but may at this stage
depend on \(h\). It is not replaced by a rational cube.

## 3. Scalarity forces the reciprocal coefficient to be constant

The coefficient of \(y^7\) in \(\delta z\), computed from (9),
is \(4rD^2\rho_{hh}\). Thus
\[
 \rho=\lambda h+\kappa,\qquad
 \lambda,\kappa\in K,\quad \lambda\ne0,\qquad
 T=r\lambda\in K^*,\qquad u=(r\kappa+k_0)' .
\tag{11}
\]
This follows by two explicit primitive subtractions with
\(\partial_h\). In these terms,
\[
 z=TDy^4+TF_3y^3+(6t^2+TF_2)y^2+(T'h+u)y+z_0 .
\]
The \(y^4\) and \(y^3\) scalar equations give, in order,
\[
 DT'+\alpha T=0,\qquad
 (z_0)_h=b:=-\frac{TF_3'+4T'F_3}{4D}\in K,\qquad
 z_0=bh+g_0,\quad g_0\in K.
\tag{12}
\]
The remaining two positive coefficients are
\[
 12t+TF_2'+3T'F_2+3F_3b=0,\qquad
 T''h+u'+2F_2b=0 .
\tag{13}
\]
Every coefficient other than \(h\) in the last equation lies in
\(K\). Since \(h\) is transcendental over \(K\), it gives \(T''=0\).
Differentiating the first equation in (12) now gives
\(6\alpha T'=0\).
If \(\alpha\ne0\), this says \(T'=0\), and the undifferentiated
equation would give \(\alpha T=0\), a contradiction.
Hence
\[
 \alpha=0,\quad
 \beta\in\mathbb C^*,\quad r=1/\beta\in\mathbb C^*,\quad
 T\in\mathbb C^*,\quad
 \lambda=T/r\in\mathbb C^* .
\tag{14}
\]
In particular the original reciprocal-linear branch is now
constant. This conclusion did not use rationality of \(K\),
a power-law ansatz, or a normalization of \(\Gamma=Ny\).

With (14), equations (12)--(13) become
\[
 b=-\frac{TF_3'}{4\beta},\qquad
 TF_2'+12t+3F_3b=0,\qquad u'+2F_2b=0,\qquad
 \delta z=b'h+g_0'\ne0 .
\tag{15}
\]

## 4. Actual field return forces the last line coefficient to be constant

Equations (6), (9), and (11)--(12) show that every coefficient
of \(z,w\), as polynomials in \(y\), lies in \(K[h]\).
The actual equality in (2) gives
\[
 L(y)=\mathbb C(y,z,w)\subset K(h)(y)\subset L(y).
\]
Intersecting with \(L\), since \(y\) is transcendental over \(L\),
proves \(L=K(h)\).
Set
\[
 \mathcal W=w+cz=h+p(y).
\]
The coefficient \(c\) is complex, so replacing \(w\) by
\(\mathcal W\) preserves the field generated over \(\mathbb C\).
Then
\[
\begin{gathered}
 K(y,\mathcal W)=\mathbb C(y,\mathcal W,z),\qquad
 z=b\mathcal W+g(y),\\
 g(y)=T\beta y^4+TF_3y^3+(6t^2+TF_2)y^2+uy+g_0-bp(y)
       \in K[y].
\end{gathered}
\tag{16}
\]
The elements \(y,\mathcal W\) are algebraically independent over \(K\).

We spell out the precise polynomial-pencil fact needed here.
If \(K/\mathbb C\) is a one-variable function field,
\(s_1,s_2\) are independent over \(K\), and
\(Z_*= \sum c_{ij}s_1^is_2^j\in K[s_1,s_2]\) satisfies
\[
 K(s_1,s_2)=\mathbb C(s_1,s_2,Z_*),
\]
then for any nonconstant coefficient \(b_*\in K\) of \(Z_*\),
\[
 K=\mathbb C(b_*),\qquad c_{ij}\in\mathbb C+\mathbb C b_* .
\tag{17}
\]
To prove this, take the nonsingular projective complex curve of \(K\).
At each of its points, the pole order of \(Z_*\), after extending
the constants to \(\mathbb C(s_1,s_2)\), is the largest pole order
among its coefficients. There is no cancellation: the residues
of the terms with that order form a nonzero polynomial in the
independent \(s_1,s_2\).
Let \(\mathfrak D\) be the maximum of the coefficient pole divisors.
The pole divisor of \(Z_*\) is precisely its base extension.
Its degree is one, because the displayed field equality says
that the map defined by \(Z_*\) has degree one.
Thus \(\mathfrak D\) is one complex point with multiplicity one.
Every nonconstant coefficient has that unique simple pole,
so \(K=\mathbb C(b_*)\); in this rational coordinate every other
coefficient has at most the same simple pole, making it affine
in \(b_*\). This proves (17).

The curve-degree inputs and the no-cancellation argument are the
same as the explicitly stated pole-degree lemma in
[cover-collapse189](weight-four-absent-zero-r-cover-collapse-pass189-working.md).
Its standard inputs are
[Stacks 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
[0AYZ](https://stacks.math.columbia.edu/tag/0AYZ), and
[02NY](https://stacks.math.columbia.edu/tag/02NY).
Here the coefficients are polynomials in both independent
parameters, so their maximum pole divisor is exact, not merely
a lower bound. No assumption \(K=\mathbb C(t)\) has entered.

Write \(g_j=[y^j]g\), so \(g_0\) in (16) is its constant term.
Direct differentiation, using \(p_t=-F_U\) and (15), gives
\[
 g_4=T\beta\in\mathbb C^*,\qquad
 g_3'=4\beta t\,b',\qquad
 g_2'=-[U^2]p\,b',\qquad g_1'=-[U]p\,b'.
\tag{18}
\]
If \(b\notin\mathbb C\), then \(b'\ne0\).
Apply (17) to (16), with coefficient \(b_*=b\).
It gives \(g_3=\lambda_0+\lambda_1b\), where
\(\lambda_0,\lambda_1\in\mathbb C\).
Differentiating and comparing (18) would give
\(4\beta t=\lambda_1\), impossible because \(t\) is transcendental.
Therefore
\[
 b\in\mathbb C,\qquad
 g(y)=G(y)+g_0,\quad G\in\mathbb C[y],\quad G(0)=0,\quad
 g_0'\ne0,\qquad K=\mathbb C(g_0).
\tag{19}
\]
The last field equality follows again from (16): with the other
coefficients complex, it is
\(K(y,\mathcal W)=\mathbb C(g_0)(y,\mathcal W)\).
Intersect with \(K\). The inequality \(g_0'\ne0\) follows from
(15) and the nonzero scalar determinant.
It is not inferred from a generic rational-coordinate choice.

## 5. Two actual polynomial shears remove the coefficient variable

We now return to the original coordinates. All four constants
\(r,T,c,b\) below are complex, with \(r,T\ne0\).
The exact \(h\)-derivatives of their actual chart expressions are
\[
\begin{gathered}
 X_h=Y_h=0,\qquad Z_h=b+TX=:B_0(X),\\
 \vartheta_h=b/r-cT,\qquad
 W_h=1-cb+(b/r-cT)X+(T/r)X^2
     =1+\lambda_0(X)B_0(X),\\
 \lambda_0(X)=X/r-c .
\end{gathered}
\tag{20}
\]
For example \(z_h=b\), \(k_h=r\rho_h=T\), and
\(n_h=cr^2\rho_h=crT\).
The formula
\(\vartheta=(z-6t^2y^2-k_0'y-n)/r\) proves the middle identity.
Thus (20) is obtained from actual coefficients, not a formal
identification with an original coordinate partial.

Define original polynomials
\[
 J=W-\lambda_0(X)Z,\qquad
 I_*=Z-B_0(X)J .
\tag{21}
\]
These are two triangular polynomial changes of the bad coordinates.
They satisfy \(J_h=1\), \((I_*)_h=0\).
Every actual chart entry belongs to \(K[h,X,y]\), so
\(I_*\in K[X,y]\).
At \(X=0\), equations (16)--(19) give
\[
 J|_{X=0}=\mathcal W,\qquad
 I_*|_{X=0}=z-b\mathcal W=G(y)+g_0 .
\tag{22}
\]

The determinant is the precise remaining descent gate.
The change from \((t,\rho,y)\) to \((t,y,h)\) in (3)
multiplies by \(-\rho_h=-T/r\).
The two changes in (21) have determinant one in the last two
coordinates, with \(X\) fixed.
Consequently
\(\det\partial(Y,I_*,J)/\partial(t,y,h)\) is independent of \(X\).
Since \(Y=y+tX\), \((I_*)_h=0\), and \(J_h=1\), this determinant is
\[
 X(I_*)_y-(I_*)_t .
\]
At \(X=0\), (22) evaluates it to \(-g_0'\).
Therefore
\[
 (\partial_t-X\partial_y)I_*=g_0',\qquad
 Q(X,y):=I_*-g_0\in K[X,y],\qquad
 (\partial_t-X\partial_y)Q=0 .
\tag{23}
\]
This uses the full actual determinant, not only its value at \(X=0\).
It retains the factor \(T/r=\rho_h\) and the original \(\Gamma\);
their numerical value need not be one.

Substitute \(y=Y-tX\). Coefficientwise differentiation at fixed
\(X,Y\) in (23) shows
\[
 Q_0(X,Y):=Q(X,Y-tX)\in\mathbb C[X,Y],\qquad
 I=I_*-Q_0(X,Y)=g_0 .
\tag{24}
\]
Indeed its coefficients are elements of \(K\) killed by the
prime derivative, whose constant field is \(\mathbb C\).
This is exact coefficient transport. No denominator in an
original ring was inverted.

The complete original polynomial map and inverse are
\[
\begin{aligned}
 J&=W-\lambda_0(X)Z,&
 I&=Z-B_0(X)J-Q_0(X,Y),\\
 Z&=I+Q_0(X,Y)+B_0(X)J,&
 W&=J+\lambda_0(X)\big(I+Q_0(X,Y)+B_0(X)J\big).
\end{aligned}
\tag{25}
\]
They fix \(X,Y\). Substitution in either order cancels \(J\),
then \(I\), or reverses those two triangular operations.
Thus \(B=\mathbb C[X,Y,I,J]\).
Since \(I\in B\) equals \(g_0\in K\subset\operatorname{Frac}\mathcal A\),
one has \(EI=0\) in the original domain.
This proves that \(I\) is an actual invariant ambient coordinate,
not merely a generic parameter.

## 6. Published endpoint and exact scope

The derivation \(E\) is now a nonzero \(\mathbb C[I]\)-linear
LND on \(\mathbb C[I,X,Y,J]\).
Its kernel \(\mathcal A\) is regular:
\(\mathcal A\simeq B/(u)\), and \(Eu=1\) expresses one as a
polynomial combination of the four original partial derivatives
of \(u\). Hence the hypersurface \(u=0\) is smooth.

Bhatwadekar--Gupta--Lokhande Theorem 3.5 therefore gives
\[
 \mathcal A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]} .
\tag{26}
\]
The exact primary statement and its displayed proof were freshly read:
[Some K-theoretic properties of the kernel of a locally nilpotent
derivation on \(k[X_1,\ldots,X_4]\)](https://arxiv.org/html/1501.01438v1),
Theorem 3.5. Its nonzero-derivation, invariant-coordinate and
regular-kernel hypotheses have been supplied above.
No recursive reproof of that published theorem is asserted.

This recognizes the nonzero-\(R\), nonconstant-\(y\) case under
the full actual setup (1).
The independent
[constant-projection exclusion188](weight-four-absent-variable-constant-projection-exclusion-pass188-working.md)
excludes the other \(y\) case when \(R\ne0\).
Together they handle the supplied absent-variable nonzero-\(R\) branch.
The zero-\(R\) branch is the subject of separate190 arguments.

The proof does not establish entry into this time profile, treat
every initial form, or solve unrestricted cancellation.
All coefficient-field changes used in the proof precede a
separately justified original polynomial inverse.
No189 or earlier artifact was edited, and no checker was executed,
imported or compiled. This is a working proof with published inputs,
not human expert review, proof-assistant certification, historical
novelty clearance or a public submission.

