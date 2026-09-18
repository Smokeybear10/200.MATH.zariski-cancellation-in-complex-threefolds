# An invariant linear suspension in a sliced polynomial fourfold

An invariant of the form \(wz-g(y,t)\), with \(w\) moving
linearly under a sliced locally nilpotent derivation, is an
actual polynomial coordinate. There is no degree bound on
\(g\). The proof uses the classical homotopy-dimension bound
for smooth affine varieties, plane-line rectification, and
normality of the actual polynomial ring.

## 1. Statement and the constant boundary

Suppose
\[
\begin{gathered}
B=\mathbb C[w,y,t,z]=A[u],\qquad
E\in\operatorname{LND}(B),\qquad A=\ker E,\qquad Eu=1,\\
I=wz-g(y,t)\in A,\qquad
E^2w=0,\qquad a:=Ew\ne0,\qquad g\in\mathbb C[y,t].
\end{gathered}
\tag{1}
\]
The four displayed generators of \(B\) are actual polynomial
coordinates. Then \(g\) is a coordinate of \(\mathbb C[y,t]\),
\(I\) is a coordinate of \(B\), and
\(A\simeq\mathbb C^{[3]}\).
No bound on the \(E\)-degrees of \(y,t,z\) is imposed.

If \(g\) were constant, \(wz=I+g\) would belong to \(\ker E\).
Additivity of locally nilpotent degree in a domain implies
that each nonzero factor of an invariant product is invariant.
This would give \(Ew=0\). Thus the hypotheses themselves
exclude constant \(g\).

For every \(\lambda\in\mathbb C\), the polynomial
\(I-\lambda=wz-g(y,t)-\lambda\) is irreducible in \(B\).
Indeed \(g+\lambda\ne0\), and the coefficients \(w\) and
\(-g-\lambda\) are coprime in \(\mathbb C[w,y,t]\).
The polynomial is primitive and linear in \(z\), so Gauss's
lemma applies. This does not assume that any fiber of \(g\)
is irreducible.

## 2. The homology of a smooth plane fiber

Choose \(\lambda\) outside the finite set for which
\(D_\lambda=\{g(y,t)+\lambda=0\}\) is singular.
That exceptional set is finite: the critical locus of \(g\)
has finitely many irreducible components, and \(g\) is
constant on each positive-dimensional component because
its differential vanishes there in characteristic zero.
The isolated critical points also give finitely many values.
The smooth fiber \(D_\lambda\) may be disconnected.

Put
\[
\begin{gathered}
X_\lambda=\{I=\lambda\}=\{wz=g(y,t)+\lambda\},\\
Z_\lambda=X_\lambda\cap\{w=0\}
     \simeq D_\lambda\times\mathbb C,\qquad
U_\lambda=X_\lambda\setminus Z_\lambda
     \simeq\mathbb C^*\times\mathbb C^2,\\
X_\lambda\simeq Y_\lambda\times\mathbb C,\qquad
Y_\lambda=\operatorname{Spec}(A/(I-\lambda)).
\end{gathered}
\tag{2}
\]
The last isomorphism uses the actual equality \(B=A[u]\)
and \(I\in A\), not an assertion that the slice \(u\)
is an ambient coordinate.

The hypersurface \(X_\lambda\) is smooth. Its four partial
derivatives are \(z,-g_y,-g_t,w\), and their simultaneous
vanishing would give a singular point of \(D_\lambda\).
Regularity descends along the polynomial extension in (2),
so \(Y_\lambda\) is a smooth affine complex surface.
It is of finite type since \(A\simeq B/(u)\).

A smooth affine complex variety of dimension two has the
homotopy type of a CW complex of real dimension at most
two. We use the affine form of the Andreotti--Frankel bound,
as proved in Milnor, *Morse Theory*, Section 7,
Theorems 7.1 and 7.2, printed pages 39--41.[^1]
Consequently, with ordinary singular homology and rational
coefficients,
\[
H_3(X_\lambda;\mathbb Q)
 =H_3(Y_\lambda;\mathbb Q)=0,\qquad
H_3(U_\lambda;\mathbb Q)=H_2(U_\lambda;\mathbb Q)=0.
\tag{3}
\]

Here \(Z_\lambda\) is a closed smooth complex divisor in
\(X_\lambda\). The differential \(dw\) identifies its normal
complex line bundle with the trivial line bundle:
at \(w=0\), the nonzero differential of \(g\) makes \(dw\)
surjective on the tangent space of \(X_\lambda\).
A tubular neighborhood therefore identifies the relevant
pair with the trivial normal bundle and its deleted zero
section. Excision and relative Künneth give
\[
\begin{aligned}
H_3(X_\lambda,U_\lambda;\mathbb Q)
&\simeq H_3(Z_\lambda\times\mathbb C,
                  Z_\lambda\times\mathbb C^*;\mathbb Q)\\
&\simeq H_1(Z_\lambda;\mathbb Q)
 \simeq H_1(D_\lambda;\mathbb Q),\\
H_1(D_\lambda;\mathbb Q)
&\simeq H_3(X_\lambda;\mathbb Q)=0.
\end{aligned}
\tag{4}
\]
The relative homology of \((\mathbb C,\mathbb C^*)\)
is one-dimensional in degree two and zero otherwise,
which explains the shift. The final isomorphism is the
long exact sequence of the pair and (3).
This is ordinary relative homology, not Borel--Moore
homology or compactly supported cohomology.
The same tubular-neighborhood homology identification is
recorded in Goresky--Hingston, Appendix B.1, equation
(B.1.2).[^2]

Each connected component \(C\) of \(D_\lambda\) is
therefore an algebraic affine line. To see this, let
\(\overline C\) be its smooth projective completion,
with genus \(\gamma\) and \(r\ge1\) omitted points.
Then \(\dim_{\mathbb Q}H_1(C;\mathbb Q)=2\gamma+r-1\).
Its vanishing forces \(\gamma=0,r=1\), so
\(C\simeq\mathbb A^1\).

## 3. One rectified component determines the whole polynomial

Choose a component \(C_0\) of one smooth generic fiber.
It is a closed embedded affine line in the \((y,t)\)-plane.
The Abhyankar--Moh--Suzuki theorem gives polynomial plane
coordinates \((h,k)\) for which \(C_0=\{h=0\}\).
We use the exact closed-embedding statement over
\(\mathbb C\); a proof is given in Vistoli, printed page 2.[^3]

Let \(C\) be a component of any other smooth generic
fiber. The curves \(C\) and \(C_0\) are disjoint, so
\(h|_C\) has no zero. Since \(C\simeq\mathbb A^1\),
its only invertible regular functions are nonzero constants.
Thus \(h|_C=c\in\mathbb C^*\). A closed irreducible curve
contained in the line \(\{h=c\}\) is the whole line.

Infinitely many distinct fiber values provide infinitely
many distinct such constants \(c\). The polynomial
\(\partial g/\partial k\) vanishes on every one of these
lines. Expanding it in powers of \(k\), each coefficient
has infinitely many roots as a polynomial in \(h\);
therefore
\[
\frac{\partial g}{\partial k}=0,\qquad
g=P(h)\quad\text{for some }P\in\mathbb C[T]\setminus\mathbb C,
\qquad \mathbb C[y,t]=\mathbb C[h,k].
\tag{5}
\]
This argument does not require generic irreducibility of
the fibers of \(g\), a polynomial Stein factorization,
or a choice of rational first-integral field.

## 4. Normality excludes a nontrivial composition

Since \(a=Ew\) is invariant and nonzero, the actual
polynomial flow satisfies \(\exp(sE)w=w+sa\).
Evaluate its polynomial identities at the rational time
\(s=-w/a\). Define
\[
r=\left.\exp(sE)h\right|_{s=-w/a}\in B[1/a]
      \subset\operatorname{Frac}(B),\qquad
I=-P(r).
\tag{6}
\]
Local nilpotence makes \(\exp(sE)h\) a finite polynomial
in \(s\), with no degree condition on \(h\) under \(E\).
The identity for \(I\) follows from its invariance and
the vanishing of the transformed \(w\).
Substituting this rational time is used only in polynomial
identities; it is not asserted to define an automorphism
of \(B\).

The leading coefficient of \(P\) is a nonzero complex
constant. After dividing by it, \(P(T)+I\) is a monic
polynomial over \(B\) satisfied by \(r\). Normality of
the polynomial ring \(B\) therefore gives \(r\in B\).
Also \(r\) is nonconstant, since \(I\) is nonconstant.

If \(m=\deg P\ge2\), choose \(\lambda\) so that
\(P(T)+\lambda\) has distinct roots \(c_1,\ldots,c_m\).
Then
\[
I-\lambda=-\bigl(P(r)+\lambda\bigr)
 =-\operatorname{lc}(P)\prod_{j=1}^{m}(r-c_j)
\tag{7}
\]
is a product of at least two nonunits in \(B\).
This contradicts the irreducibility proved in Section 1.
Hence \(\deg P=1\), and \(g\) is a plane coordinate.

## 5. The actual coordinate inverse and kernel recognition

Choose \(r_0\in\mathbb C[y,t]\) with
\(\mathbb C[y,t]=\mathbb C[g,r_0]\). Then
\[
B=\mathbb C[w,r_0,z,I],\qquad g=wz-I.
\tag{8}
\]
This equality comes with a polynomial inverse: recover
\(g=wz-I\), then recover \(y,t\) from the plane inverse
of \((g,r_0)\). Thus \(I\) is an actual invariant ambient
coordinate, not merely an element with polynomial quotient.

The slice equality \(A[u]=B\) makes \(A\) regular.
Applying Bhatwadekar--Gupta--Lokhande, Theorem 3.5,
to the nonzero \(\mathbb C[I]\)-linear LND on
\(\mathbb C[I,w,r_0,z]\) yields
\(A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}\).[^4]

## 6. The low-degree option and the mixed-cubic application

When \(\deg g\le3\), one may replace the all-degree
plane-line rectification in Section 3 by the elementary
argument in
[the cubic plane-curve lemma, Section 2](cubic-linear-variable-pass.md).
If infinitely many fibers are reducible, each has a line
component, and disjointness forces infinitely many parallel
lines; this again gives \(g=P(h)\), now with affine-linear
\(h\). Otherwise choose a smooth irreducible generic fiber.
Section 2 makes it an affine line. The degree-three
parametrization argument excludes the sole nonlinear
degree pair \((3,2)\), so that fiber is an affine-linear
graph and \(g\) is already a plane coordinate.
Thus the cubic application does not need the full
Abhyankar--Moh--Suzuki theorem.

In the
[mixed-cubic correction criterion](three-good-mixed-cubic-correction-criterion-pass130.md),
passing both derivative tests gives
\(I=wz-\widetilde g(w,y,t)\in A\), where
\(w=L(x)+\rho\), \(E^2w=0\), and \(Ew=L(a)\ne0\).
Write
\(\widetilde g=wJ+g_0(y,t)\) and make the actual triangular
change \(z_1=z-J(w,y,t)\).
Then \(I=wz_1-g_0(y,t)\) satisfies (1).
The theorem proves automatically that \(g_0\) is a plane
coordinate, \(I\) is an ambient coordinate, and
\(A\simeq\mathbb C^{[3]}\).
This application uses neither primitivity of the leading
relation nor the intrinsic-plane construction. Primitivity
is needed there for uniqueness, not for recognizing a lift
once both derivative tests have passed.

## 7. Why the hypotheses cannot simply be removed

Three explicit triangular derivations separate the main
assumptions:

- Without the global slice, take
  \(E=t\partial_w+z\partial_y\) and \(I=wz-yt\).
  Then \(E^2w=0\), \(Ew=t\ne0\), and \(EI=0\), but
  \(g=yt\) is not a plane coordinate.
  There is no slice, because \(E(B)\subset(t,z)B\).
- Without \(Ew\ne0\), take \(E=\partial_t\) and
  \(I=wz-y^2\). The derivation has the slice \(t\), but
  \(g=y^2\) is not a plane coordinate.
- Without \(E^2w=0\), take
  \(E=\partial_t+z\partial_y+2y\partial_w\) and
  \(I=wz-y^2\). This is a locally nilpotent derivation
  with slice \(t\), \(EI=0\), and \(Ew=2y\ne0\), but
  \(E^2w=2z\ne0\) and again \(g=y^2\) is not a coordinate.

Local nilpotence in these examples follows directly from
their triangular form. The displayed noncoordinate plane
polynomials have critical points, whereas a plane coordinate
has a nowhere-vanishing differential.

This is a recognition theorem for the displayed invariant
presentation and moving linear coordinate. It does not
assert that an arbitrary sliced fourfold admits that
presentation, or that an arbitrary mixed cubic relation
passes its two derivative correction tests.

## Sources

1. John Milnor. *Morse Theory*. Princeton University Press, 1963,
   Section 7, Theorems 7.1--7.2, pp. 39--41.
   [Text](https://luis.impa.br/aulas/topdif/Milnor_MorseTheory.pdf).
2. Mark Goresky and Nancy Hingston. *Loop products and closed geodesics*.
   arXiv:0707.3486v1, 2007, Appendix B.1, equation (B.1.2).
   [Text](https://arxiv.org/pdf/0707.3486v1).
3. Angelo Vistoli. *On the minimal normal compactification of a polynomial
   in two variables*. arXiv:math/9904035v3, 1999, Section 3,
   the Suzuki--Abhyankar--Moh theorem over \(\mathbb C\), printed p. 2.
   [Text](https://arxiv.org/pdf/math/9904035v3).
4. S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande.
   *Some K-theoretic properties of the kernel of a locally nilpotent
   derivation on k[X1, ..., X4]*. arXiv:1501.01438v1, 2015,
   Theorem 3.5. [Text](https://arxiv.org/html/1501.01438v1).

[^1]: Milnor, *Morse Theory*, Section 7, pp. 39--41.
    [Source](https://luis.impa.br/aulas/topdif/Milnor_MorseTheory.pdf).
[^2]: Goresky--Hingston, Appendix B.1, equation (B.1.2).
    [Source](https://arxiv.org/pdf/0707.3486v1).
[^3]: Vistoli, Section 3, printed p. 2.
    [Source](https://arxiv.org/pdf/math/9904035v3).
[^4]: Bhatwadekar--Gupta--Lokhande, Theorem 3.5.
    [Source](https://arxiv.org/html/1501.01438v1).
