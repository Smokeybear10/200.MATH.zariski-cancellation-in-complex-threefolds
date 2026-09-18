# Independent audit of the rational-rescaling closure

The argument in
[height-nine-rational-rescale-pass.md](height-nine-rational-rescale-pass.md)
closes the remaining power-law
cases under the slice hypothesis, provided its two elementary edge cases
are included: a vanishing rescaled bad commutator and a constant reduced
denominator. This audit checks the localization, affine-line argument,
denominator classification, and both final cases independently. It does
not treat coordinate partials as LNDs after localization.

Use the established power-law input for \(m\in\{3,4\}\):
\[
E^m x=cg^m,\quad E^{m-1}x_4=\lambda g^{m-1},\quad E(g)=0,
\quad c\ne0,\ c_4=0,\ \lambda\ne0.
\]
The ring is \(B=\mathbb C^{[4]}\), and \(E\) has a polynomial slice
\(s_*\). The three good partials have vanishing second commutators,
and the fourth has vanishing third commutator. The previously proved
coefficient identities also give \(W_i(g)=0\) for \(i\le3\) and
\(V(g)=0\), where \(W_i=[E,T_i]\), \(V=[E,W_4]\).

## 1. The rescaled algebraic identities are valid

Set \(\delta=E/g\) on \(B_g\). Since \(E(g)=0\), this is an LND
of the localized ring and
\(\delta^j(f)=g^{-j}E^j(f)\). Put \(g_i=T_i(g)\). Directly,
\[
[\delta,T_i]=\frac{W_i}{g}+\frac{g_i}{g}\delta.
\]
For a good partial, \(E(g_i)=W_i(g)=0\), so the second commutator
vanishes. For the fourth partial, the second commutator is
\[
\widetilde V=\frac{V}{g^2}
+\frac{2E(g_4)}{g^2}\delta.
\]
Its next bracket with \(\delta\) vanishes because
\(V(g)=0\) and \(E^2(g_4)=V(g)=0\). These are identities of
derivations of \(B_g\). No local-nilpotence assertion about \(T_i\)
on that ring is used.

The localized flow is polynomial in time and fixes \(g\). Its
Jacobian determinant is one: equivalently, use
\(\operatorname{div}\delta=(\operatorname{div}E)/g-E(g)/g^2=0\),
or the chain rule for its inverse together with the units of \(B_g[t]\)
and evaluation at \(t=0\). Thus the same companion-matrix algebra
applies over \(\operatorname{Frac}B\).

If \(\widetilde V=0\), coefficient comparison gives
\(J_\delta c=0\). For the nonzero good constant direction
\(A=c\cdot\partial\), this means
\[
[E,A]=-\frac{A(g)}gE.
\]
Applying the bracket to \(s_*\) shows that \(A(g)/g\) is polynomial.
The constant partial \(A\) is an LND of \(B\), so divisibility
\(g\mid A(g)\) forces \(A(g)=0\). Hence \(A\) commutes with
\(E\), and the existing constant-direction closure applies.

## 2. The constant-top line argument survives localization

Assume \(\widetilde V\ne0\). One has
\(\delta^m x=c\) and \(\delta^{m-1}x_4=\lambda\).
The companion-matrix descent gives
\(\operatorname{rank}\operatorname{Jac}(\delta^{m-1}x)\le1\).
The rank is nonzero because applying \(\delta\) gives \(c\ne0\).

The coefficient map is a morphism on \(\operatorname{Spec}B_g\),
not necessarily on all of affine four-space. This suffices: the
\(\delta\)-action preserves that open set and moves the coefficient
map by translation through \(tc\). Its irreducible curve image closure
therefore contains an affine line and equals that line. Extracting a
parameter by a constant linear functional gives an element of \(B_g\).
The subsequent coefficient comparison normalizes it exactly to
\[
\sigma=\frac{\delta^{m-2}x_4}{\lambda}
=\frac{E^{m-2}x_4}{\lambda g^{m-2}}.
\]
Thus, with \(r=m-1\), there is a constant vector \(d\), \(d_4=\lambda\),
such that \(\delta^{m-1}x=c\sigma+d\), and
\[
D_0=rT_d+\sigma T_c,\qquad [\delta,D_0]=0.
\]
The directions \(T_c,T_d\) are independent. Also
\(D_0(x_4)=r\lambda\), and commutation gives
\(D_0(\sigma)=0\) because \(m-2\ge1\). This is an algebraic
flow and image-dimension argument. It uses no coordinate-recognition
theorem or polynomial-parameter theorem over the localized ring.

## 3. Reduced rational Burgers solutions

Choose linear coordinates with \(T_c=\partial_a\),
\(T_d=\partial_b\), and let \(R=\mathbb C[z_1,z_2]\). Write
\(\sigma=N/D\) in lowest terms in \(R[a,b]\). Its differential
equation is
\[
r\sigma_b+\sigma\sigma_a=0.
\]
Clearing denominators and reducing modulo \(D\) gives \(D\mid D_a\),
so \(D_a=0\) by degree. Dividing once by \(D\) and reducing modulo
\(N\) then gives \(N\mid N_b\), so \(N_b=0\). The remaining
identity is \(N_a=rD_b\). Its two sides depend on disjoint variables
over \(R\), hence
\[
N=\alpha a+\beta,\qquad D=\alpha b/r+\gamma,
\quad\alpha,\beta,\gamma\in R.
\tag{1}
\]

The equation \(E(\sigma)=g\) gives \(D\mid E(D)\). Since \(E\)
is an LND of \(B\),
\[
E(D)=0,\qquad E(N)=gD.
\tag{2}
\]
Reduced denominators in the displayed formula for \(\sigma\) also give
\(D\mid g^{m-2}\) in \(B\).

The polynomial field
\[
Z=DD_0=N\partial_a+rD\partial_b
\]
satisfies
\[
[Z,E]=\kappa E,\qquad \kappa=Z(g)/g.
\tag{3}
\]
In particular \(\kappa\) is polynomial: apply (3) to the original
slice to get \(\kappa=-E(Z(s_*))\). This avoids a separate
primitivity argument, though that argument also works.

## 4. The affine numerator case contradicts a slice

Suppose \(\alpha\ne0\). The field \(Z\) preserves degree in
\((a,b)\), and its highest-degree part is \(\alpha\) times the
Euler field. From \(Z(g)=\kappa g\), degree first forces
\(\kappa\in R\), and then comparison of top homogeneous components
gives \(\kappa=n\alpha\), where \(n=\deg_{a,b}g\). Moreover
\(n\ge1\), because the denominator \(D\), which has positive
\(b\)-degree, divides \(g^{m-2}\).

Applying \(E\) to \(Z(g)=n\alpha g\), using (3) and \(E(g)=0\),
gives \(E(\alpha)=0\). Localize at \(\alpha\), and center the two
coordinates:
\[
a'=a+\beta/\alpha,\qquad b'=b+r\gamma/\alpha.
\]
Then \(Z=\alpha(a'\partial_{a'}+b'\partial_{b'})\), and (3) becomes
\[
[a'\partial_{a'}+b'\partial_{b'},E]=nE.
\]
Relative to the grading with \(a',b'\) of degree one and \(R_\alpha\)
of degree zero, \(E\) has positive degree \(n\). Its images of
\(z_1,z_2\) lie in degree \(n\), and those of \(a',b'\) lie in
degree \(n+1\). All generator images therefore belong to the proper
ideal \((a',b')\). The image of every element of \(B_\alpha\),
including the polynomial slice, lies in that ideal, a contradiction.
This argument is algebraic and does not require a proper action.

## 5. The base-only denominator case gives an invariant plane coordinate

Suppose \(\alpha=0\). Then \(N,D\in R\). If \(D\) is constant,
\(D_0\) is a polynomial nice LND. Equation (3) makes \(D_0(g)/g\)
polynomial, so LND divisibility forces \(D_0(g)=0\). Thus \(D_0\)
commutes with \(E\); its triangular straightening preserves the good
constant direction \(T_c\). The existing single-partial closure applies.

Take \(D\) nonconstant. The pair \(N,D\) is algebraically independent:
otherwise their Jacobian rows in the plane are dependent, and
\(E(D)=0\) would force \(E(N)=0\), contrary to (2). Solving the two
Jacobian equations \(\delta(D)=0\), \(\delta(N)=D\) shows
\[
\delta(z_1),\delta(z_2)\in\operatorname{Frac}R.
\]
Choose their reduced common denominator \(h\in R\), with numerators
\(p_1,p_2\in R\) satisfying \(\gcd(h,p_1,p_2)=1\). Since
\(E(z_i)=gp_i/h\in B=R[a,b]\), the same prime-valuation argument
in the polynomial extension gives \(h\mid g\). It does not assert
that coprime multivariable polynomials generate the unit ideal.

Factorial closure of \(\ker E\) gives \(E(h)=0\), so
\(\Delta=h\delta\) preserves \(R\). It is locally nilpotent there:
\[
\Delta^j(f)=h^jg^{-j}E^j(f)\quad(f\in R),
\]
and the right side is eventually zero. This equality is justified by
\(E(g)=E(h)=0\), not by arbitrary rescaling of an LND. Also
\(\Delta(D)=0\), and \(\Delta(N)=hD\ne0\).

Rentschler's plane theorem supplies a coordinate of \(R\) killed by
\(\Delta\), hence by \(E\). It is an actual ambient coordinate of
\(B\). The exact plane theorem is recalled in
[Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).
Regularity of the original slice kernel and
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
then give \(\ker E\simeq\mathbb C^{[3]}\).

No counterexample to these restricted steps was found. The proof uses
the slice precisely where a normalizing rational factor must be
polynomial and where the positive-degree case is excluded. The earlier
non-slice controls therefore do not contradict it.

The full source note was read after this independent derivation. Its
constant-denominator and vanishing-rescaled-field cases are explicit,
and no mathematical correction was needed. The accompanying
[mixed_height_checks.py](mixed_height_checks.py) suite was rerun without
changes by this audit; its expanded set of 22 tests passed.
