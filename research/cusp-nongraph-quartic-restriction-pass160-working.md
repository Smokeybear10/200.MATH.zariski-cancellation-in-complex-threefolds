# The nongraph cusp branch has a quartic curve and a fifth-power coefficient

**Status: working necessary restriction over the exact generic field.**

In the \(r=k_\rho\ne0\) branch of the actual cusp chart159,
suppose the first projected coordinate \(y\) is neither constant
nor an affine linear parameter on the generic intrinsic line.
Then the whole chart relation is irreducible, its degree is four,
and the fixed projected coordinates have degrees \((2,4)\).
The coefficient \(r\), although initially allowed in a finite
algebraic extension of \(\mathbb C(\tau,\rho)\), must satisfy
\[
\frac1r=C_0+C_1(\tau-C_2)^5,
\qquad C_0,C_2\in\mathbb C,\quad C_1\in\mathbb C^*.
\tag{1}
\]
This is a necessary restriction, not an existence theorem or an
exclusion of this remaining branch. It does not descend generic
coordinates or construct an integral invariant correction in the
original four-ring. No159 or earlier artifact is edited.

## 1. Actual inherited hypotheses and the nongraph condition

Retain the actual sliced E-time \((1,1,2,2)\) cusp chart159:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3),\\
T=\partial_Z,\quad N=[u^3]T|_A,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
a=EX,\quad \tau=EY/a,\quad \rho=(E^2W/2)/a^2,\quad
L/\mathbb C(\tau,\rho)\text{ finite separable},\\
Y=y+\tau X,\quad Z=z+\sigma X+\tau^3X^2,\quad
W=w+\vartheta X+\rho X^2,\quad
J=\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}=-a^3.
\end{gathered}
\tag{2}
\]
The original coordinates and full initial-kernel assertion are
actual. The two coefficient partials extend through the exact
field \(L\) and fix \(v\). Their commutation and all statements
in (2) are retained from the complete chart proof, not inferred
from a formal determinant ansatz.[^1]

Its first integrations supply \(k,n,\ell\in L\). Put
\(r=k_\rho\ne0\), and for independent formal \(U,V\) define
\[
\begin{gathered}
H_j(c;U,V)=\sum_{i=0}^j
 \frac{c_{\tau^i\rho^{j-i}}U^iV^{j-i}}{i!(j-i)!},\qquad
f=U^3+H_2(k;U,V)+H_1(n;U,V),\\
\Phi=f_V\frac{\ell-f}{r}+H_3(k;U,V)+H_2(n;U,V)
 -\ell_\tau U-\ell_\rho V,\\
L[y,\vartheta]=L[v],\qquad
\Phi(y,\vartheta)=m\in L,\qquad
0\ne\Phi-m\in L[U,V],\qquad \deg\Phi\le4,\\
\ker\{L[U,V]\longrightarrow L[v]\}=(G),\qquad
\Phi_4=-\frac{U^3(r_\tau U+r_\rho V)}r .
\end{gathered}
\tag{3}
\]
The evaluation sends \((U,V)\) to \((y,\vartheta)\), and
\(G\) is irreducible. Its selected gradient is a unit ideal
by the constant determinant in (2).

The additional hypothesis in this note is
\(\deg_v y\ge2\). Thus "nongraph" concerns these fixed
projected axes: it excludes both \(y\in L\) and
\(L[y]=L[v]\), and is not an assertion about every possible
plane-coordinate description.
The selected-factor reduction159 then gives
\(\Phi-m\in L^*G\).[^2]
In particular whole-polynomial association is established
before applying any degree or plane-embedding argument.

## 2. Implicit degree and the unique point at infinity

For completeness the following elementary facts apply to any
pair \(p,q\in L[v]\) generating \(L[v]\), with irreducible
implicit equation \(G_0\).
First
\[
\deg G_0=\max(\deg_v p,\deg_v q).
\tag{4}
\]
Adjoin an independent \(\lambda\) and put \(Q=q+\lambda p\).
If \(D=\deg G_0\), the irreducible polynomial
\(G_0(U,Q-\lambda U)\) has \(U\)-degree \(D\), since its
coefficient of \(U^D\) is \((G_0)_D(1,-\lambda)\ne0\).
Gauss's lemma over \(L(\lambda)(Q)\) identifies the degree
of \(L(\lambda)(v)/L(\lambda)(Q)\) with \(D\).
The same field degree equals the polynomial degree of \(Q(v)\),
which is the maximum in (4). The latter degree formula follows
also by applying Gauss's lemma to \(Q(T)-Q_0\), primitive and
linear in an independent \(Q_0\). This is the generic-projection
proof139, using only the whole-line equality.[^3]

Second, the projective closure of this polynomially parametrized
curve has exactly one geometric point at infinity, defined over
\(L\). To see this, homogenize \((p(v),q(v),1)\) to the
maximum degree in (4). It defines a morphism from \(\mathbb P^1\)
with no base point: the third coordinate is nonzero off infinity,
and at least one leading coefficient is nonzero at infinity.
Its proper image is the projective closure, and only the source
point at infinity can map to the target line at infinity.
After scalar extension the same argument holds. Consequently
the highest homogeneous form of \(G_0\) is a scalar times
one \(L\)-linear form to the power \(\deg G_0\).
This conclusion needs no root extraction in \(L\).

In particular, if that highest form is proportional to \(U^D\),
then in the unchanged axes
\(\deg_v q=D\) and \(\deg_v p<D\). This follows directly
from the homogeneous parametrization's value \([0:1:0]\)
at infinity.

## 3. Degree drops leave exactly the nested quartic

Set \(D=\deg G=\deg\Phi\le4\).
Degree one is impossible under \(\deg_v y\ge2\) by (4).
If \(D=4\), the unique-point conclusion and (3) force
\(r_\rho=0\), \(r_\tau\ne0\), and \(G_4\sim U^4\).
Indeed for \(r_\rho\ne0\) the displayed quartic has two
distinct linear factors.

To exclude smaller degrees one must also inspect the leading
forms after \(\Phi_4\) vanishes.
Then \(r_\tau=r_\rho=0\), and direct expansion of (3) gives
\[
\begin{gathered}
\Phi_3=\left(\frac{k_{\tau\tau\tau}}6-
             \frac{n_\rho}{r}\right)U^3,\\
\Phi_3=0\ \Longrightarrow\ n_{\rho\rho}=0,\qquad
\Phi_2=\left(\frac{n_{\tau\tau}}2-
             \frac{n_\rho k_{\tau\tau}}{2r}\right)U^2
             +n_{\tau\rho}UV .
\end{gathered}
\tag{5}
\]
For the implication, \(\Phi_3=0\) says
\(n_\rho=rk_{\tau\tau\tau}/6\); its \(\rho\) derivative
vanishes because \(k_\rho=r\) and both partials kill \(r\).
These formulas retain the coefficient derivatives in the
exact field, including possible algebraic coefficients.

If \(D=2\), its nonzero form in (5) has one geometric zero
on the line at infinity only if it is proportional to \(U^2\).
Thus \(\deg_v\vartheta=2\) and \(\deg_v y<2\), a contradiction.
If \(D=3\), its nonzero cubic form is proportional to \(U^3\).
Hence \(\deg_v\vartheta=3\) and \(0<\deg_v y<3\).
The characteristic-zero Abhyankar--Moh--Suzuki degree theorem
applied to \(L[y,\vartheta]=L[v]\) says that one of the two
positive degrees divides the other. Its field hypothesis is
exactly satisfied over \(L\), not only over an algebraic
closure.[^4] It forces \(\deg_v y=1\), again a contradiction.

Therefore \(D=4\). Applying the same theorem now gives
\(\deg_v y=1\) or two. The hypothesis excludes the first,
so the precise conclusions are
\[
\Phi-m\in L^*G,\qquad
\deg G=4,\qquad (\deg_v y,\deg_v\vartheta)=(2,4),\qquad
r_\rho=0,\quad r_\tau\ne0 .
\tag{6}
\]
No coefficient-dependent change of the original coordinates
has been used to get these degrees.

## 4. The literal quadratic nesting in the fixed axes

Complete the square in the quadratic polynomial \(y(v)\)
by an affine description of its parameter over \(L\):
\(y=A t^2+B\), with \(A\in L^*\).
Subtract from \(\vartheta\) a quadratic polynomial
\(Q(y)\) cancelling its terms of degrees four, two and zero
in \(t\). This is possible using coefficients in \(L\),
and \(\deg Q=2\). The remainder is
\(t(c_3t^2+c_1)\).

The generated ring is
\(L[t^2,t(c_3t^2+c_1)]\). Its even part is \(L[t^2]\)
and its odd part is
\(t(c_3t^2+c_1)L[t^2]\), since the square of the odd
generator is even. Equality with \(L[t]\) forces
\(c_3=0\) and \(c_1\ne0\).
Thus \(\vartheta-Q(y)=c_1t\) is a linear parameter.

The resulting implicit equation is quadratic in that parameter.
Whole-polynomial association in (6) gives, in the same formal
\(U,V\) axes,
\[
\Phi=\kappa\{V-Q(U)\}^2+\lambda U+\nu,
\qquad \kappa\lambda\ne0,\quad \deg Q=2,
\qquad \kappa,\lambda,\nu\in L,\quad Q\in L[U].
\tag{7}
\]
The constant \(m\) is absorbed in \(\nu\).
For example the parameter equation before scaling is
\((V-Q(U))^2-(c_1^2/A)(U-B)=0\), whose linear coefficient
in \(U\) is nonzero.
The argument establishes (7) over the exact field without a
square root and without transporting any generic change to
the original four-ring. It is an elementary description of
the degree alternative in (6), not an assumed classification.

## 5. Expanding the chart potential and comparing the top coefficients

From this point a prime denotes \(\partial_\tau\), with
the other coefficient variable held fixed. Since \(r_\rho=0\)
and \(k_\rho=r\), all higher derivatives commute as before.
Set
\(\Delta=r''/2-r'^2/r\) and \(\mathcal N=n_{\rho\rho}\).
Expanding the actual polynomial (3), not differentiating (7)
as though its coefficients were constant, gives
\[
\begin{gathered}
\Phi=\frac{\mathcal N}{2}V^2+\mathcal B(U)V+\mathcal C(U),\\
\mathcal B(U)=\Delta U^2+b_1U+b_0,\qquad
b_1=n_{\tau\rho}-2r'n_\rho/r,\quad
b_0=-n_\rho^2/r-\ell_\rho,\\
\mathcal C(U)=c_4U^4+c_3U^3+\text{terms of degree at most two},\\
c_4=-r'/r,\qquad
c_3=k'''/6-r'k''/(2r)-n_\rho/r .
\end{gathered}
\tag{8}
\]
For instance \(f_V=r'U+n_\rho\), the \(V\) coefficient
of \(f\) is the same polynomial, and the \(U^2V\)
coefficient of \(H_3(k)\) is \(r''/2\).
These observations account for both terms in \(\Delta\).

Equation (7) implies \(\mathcal N=2\kappa\ne0\), and
its nonzero quadratic \(Q\) implies \(\Delta\ne0\).
Completing the square in \(V\) in (8) shows that
\(\mathcal C-\mathcal B^2/(2\mathcal N)\) is affine in
\(U\), with nonzero linear coefficient. In particular its
coefficients of \(U^4\) and \(U^3\) vanish:
\[
\mathcal N=-\frac{r\Delta^2}{2r'},\qquad
\mathcal N_\rho=0,\qquad
c_3=\frac{\Delta b_1}{\mathcal N},\qquad
r\,r'\,\Delta\,\mathcal N\ne0 .
\tag{9}
\]
The denominators here are nonzero elements of the field \(L\).
The second assertion follows from the first and \(r_\rho=0\).
The vanishing quadratic coefficient and nonzero affine
coefficient give further conditions; they are not being
replaced by (9) as sufficient data.

## 6. A coefficient derivative gives the exact third-order equation

Take \(\partial_\rho\) of the cubic equation in (9).
Because \(k_\rho=r\), the derivatives of its two sides are
\[
\frac{r'''}6-\frac{r'r''}{2r}-\frac{\mathcal N}{r}
 =\frac{\Delta}{\mathcal N}
    \left(\mathcal N'-\frac{2r'\mathcal N}{r}\right).
\tag{10}
\]
Here \((n_{\tau\rho})_\rho=\mathcal N'\), and all
\(\rho\) derivatives of \(r,\Delta,\mathcal N\) vanish.
This differentiates the actual coefficient identity, without
changing the meaning of the fixed formal axes.

The logarithmic derivative of the first formula in (9) is
\(\mathcal N'/\mathcal N=r'/r+2\Delta'/\Delta-r''/r'\).
Substitution in (10), including
\(-\mathcal N/r=\Delta^2/(2r')\), yields
\[
\begin{gathered}
\frac{r'''}6-\frac{r'r''}{2r}+\frac{\Delta^2}{2r'}
 =2\Delta'-\frac{\Delta r''}{r'}-\frac{\Delta r'}r,\\
4r'r'''-\frac{12r'^2r''}{r}+\frac{12r'^4}{r^2}-3r''^2=0 .
\end{gathered}
\tag{11}
\]
For an explicit expansion check, the first line's left side
minus right side, multiplied by \(6r'\), becomes
\(-5r'r'''+15r'^2r''/r-15r'^4/r^2+15r''^2/4\)
after using \(\Delta=r''/2-r'^2/r\).
Multiplication by \(-4/5\) gives the second line.

## 7. Finite algebraic coefficient fields give only the fifth-power solutions

Put \(\chi=1/r\). A direct derivative substitution gives
\[
\begin{gathered}
\chi_\rho=0,\qquad \chi'\ne0,\qquad
4\chi'\chi'''-3\chi''^2
=r^{-4}\left(4r'r'''-\frac{12r'^2r''}{r}
                  +\frac{12r'^4}{r^2}-3r''^2\right)=0,\\
\Delta=-\frac{\chi''}{2\chi^2}\ne0 .
\end{gathered}
\tag{12}
\]
Choose a fourth root \(h\) of \(\chi'\) in a finite
algebraic extension \(L_1/L\). This auxiliary extension is
used only to solve the coefficient differential equation.
Both coefficient partials extend uniquely and commute.
Differentiating \(h^4=\chi'\) in \(\rho\) gives
\(h_\rho=0\), since \(h\ne0\).
Twice differentiating in \(\tau\) rewrites the zero in
(12) as \(16h^7h''\); hence \(h''=0\).

The exact joint constant field of \(L_1\) is \(\mathbb C\).
Indeed, for an element killed by both partials, differentiate
its monic minimal polynomial over \(\mathbb C(\tau,\rho)\).
Each resulting polynomial has smaller degree and still
vanishes at that element, so all coefficient derivatives
are zero. The coefficients therefore lie in \(\mathbb C\),
and algebraic closedness of \(\mathbb C\) gives the claim.
Finiteness of \(L_1/\mathbb C(\tau,\rho)\) is inherited
from (2) and the single algebraic adjunction.

Since \(h''=0\) and \(h_\rho=0\), it follows that
\(h=A\tau+B\), with \(A,B\in\mathbb C\).
If \(A=0\), then \(\chi'=B^4\ne0\), so \(\chi\)
is affine in \(\tau\), and \(\Delta=0\), a contradiction.
Thus \(A\ne0\). Integrating \(\chi'=(A\tau+B)^4\)
and using the same joint-constant argument gives
\[
\begin{gathered}
\chi=C_0+\frac{(A\tau+B)^5}{5A}
      =C_0+C_1(\tau-C_2)^5,\\
C_0,C_2\in\mathbb C,\qquad C_1=A^4/5\in\mathbb C^*,\\
r=\frac{1}{C_0+C_1(\tau-C_2)^5},\qquad
\mathcal N=\frac{10C_1(\tau-C_2)^2}
 {[C_0+C_1(\tau-C_2)^5]^3} .
\end{gathered}
\tag{13}
\]
The last expression follows from
\(\mathcal N=\chi''^2/(8\chi^3\chi')\), which is (9)
in reciprocal notation.
In particular both \(r\) and \(n_{\rho\rho}\) actually lie
in \(\mathbb C(\tau)\), despite the permitted finite field
extension. This does not prove that all of \(L\), or the
remaining coefficients, are rational over that base.

The constant \(C_0\) may be zero. No pole of (13) is removed
or declared impossible by this argument.
Conversely the nonconstant shifted fifth-power expressions
solve the differential equation in (12) and have
\(\chi''\ne0\). This converse is about the equation alone,
not about existence of \(k,n,\ell\) satisfying every chart
identity or an actual polynomial inverse.

## 8. Degeneracies and the remaining actual problem

The proof covers only \(r\ne0\) and \(\deg_v y\ge2\).
The cases \(y\in L\), \(\deg_v y=1\), and \(r=0\)
are not excluded. Degree drops in \(\Phi\) were treated
before differentiating or dividing by \(r'\), \(\Delta\)
or \(\mathcal N\). In the present branch their nonvanishing
comes from the whole quartic nested equation, not an extra
genericity assumption.

The conclusion leaves the remaining lower coefficient
conditions in the square completion, the actual determinant
constraints and integral descent to be analyzed.
Neither the auxiliary fourth-root extension nor the affine
description of the generic parameter is an allowed original
coordinate change without an additional proof.
The earlier dense three-good nested exclusion153 cannot be
applied to this two-good frame: its canonical tail-gradient
identities are different.
There is no recognition, arbitrary-entry, unrestricted
cancellation or historical novelty claim here.

## Sources and verification scope

1. [First actual cusp-chart reductions159](cusp-generic-chart-first-reductions-pass159-working.md),
   especially Sections 1--5. These supply the exact coefficient
   field, actual determinant, whole line and potential (3).
2. [Selected-factor reduction159](cusp-generic-selected-factor-reduction-pass159-working.md).
   Its complete degree-drop argument supplies whole-polynomial
   association under the nongraph hypothesis.
3. [Generic degree proof139](dense-generic-embedded-line-pass139-working.md),
   Section 3. The elementary projection proof is reproduced
   in Section 2 with no use of its three-good chart theorem.
4. Leonid Makar-Limanov,
   [*A new proof of the Abhyankar-Moh-Suzuki Theorem*](https://arxiv.org/pdf/1212.0163v1),
   AMS Theorem, printed p. 1. Its characteristic-zero field
   statement was freshly inspected for the two degree-divisibility
   uses in Section 3. Only that statement is imported, not a
   recursive audit of its proof dependencies.
5. [Nested quartic description153](nested-quartic-exclusion-pass153-working.md),
   Section 2, contains the elementary odd-part mechanism
   reconstructed here. Its subsequent actual exclusion theorem
   is not invoked.

The fixed-axis extraction, coefficient expansion, differential
equation and finite-field integration are proved above.
Finite algebra controls cannot replace these universal steps.
No human expert review or proof-assistant certification is claimed.

[^1]: Source 1, with its actual-frame and selected-partial inputs.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4. Source 5 supplies a separate comparison for
    the elementary fixed-axis extraction in Section 4.
