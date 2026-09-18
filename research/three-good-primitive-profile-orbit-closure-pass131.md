# Primitive cubic corrections along profile-preserving elementary words

A successful primitive mixed-cubic correction stays successful
under every finite elementary coordinate word that remains in
the dense three-good quadratic class at every intermediate
frame. More precisely, the corrected invariant changes only
by a nonzero constant scale and an additive constant.
This is a stability statement along elementary words in the specified class,
not a universal assertion that the correction tests pass.

## 1. The class and the exact scope of a step

Fix a sliced locally nilpotent derivation, and consider actual
polynomial coordinate frames satisfying
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
E\in\operatorname{LND}(B),\quad A=\ker E,\quad Eu=1,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad
q=E^2z\ne0,\qquad E^3z=0,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3]=2,
\qquad
P(a_1,a_2,a_3)\ne0
\ \text{for every nonzero homogeneous }P.
\end{gathered}
\tag{1}
\]
The last condition is density of the cone over the speed
image. In particular each good coordinate has exact
\(E\)-degree one.

An elementary step replaces one current coordinate \(v\)
by \(\kappa v+G\), where \(\kappa\in\mathbb C^*\) and
\(G\) is a polynomial in the other three current coordinates,
which are fixed. Relabeling coordinates is harmless.
Every frame before and after every step must satisfy (1).
A word with a temporary extra quadratic coordinate, a higher
time degree, or loss of cone density is outside the assertion.

Call a frame successful and primitive if it has
\[
\begin{gathered}
L(a)q=2F_3(a),\qquad
0\ne L\text{ homogeneous linear},\quad
F_3\text{ homogeneous cubic},\quad \gcd(L,F_3)=1,\\
I=(L(x)+\rho)z-F_3(x)-G_2(x)-G_1(x)-G_0\in A,
\end{gathered}
\tag{2}
\]
where \(\rho,G_0\) are constants and \(G_j\) is homogeneous
of degree \(j\). This is exactly passage of the two
derivative correction tests in the mixed-cubic criterion.
That criterion gives \(q\notin W_2\), where
\(W_2=\operatorname{span}_{\mathbb C}\{a_i a_j\}\), and
uniqueness of a successful primitive lift up to scale
and addition of a constant.[^1]

**Claim.** Starting from (2), every word with the stated
intermediate-frame restriction remains successful and
primitive. The subring \(\mathbb C[I]\subset B\) is
unchanged along the word.

## 2. Normalizing a successful lift without leaving the class

The automatic recognition theorem for invariant linear
suspensions makes \(I\) an actual invariant coordinate.[^2]
Its more precise plane conclusion supplies a useful normal
form. Put \(X=L(x)+\rho\), complete it by affine-linear
good coordinates \(Y_0,Z_0\), and write
\(I=Xz-g(X,Y_0,Z_0)\), with \(\deg g\le3\).
Write \(g=XJ+g_0(Y_0,Z_0)\).
The change \(W=z-J\) is an actual fixed-good shear of degree
at most two, and \(g_0\) is a plane coordinate.

Primitivity makes the degree-three restriction
\(F_3|_{\ker L}\) nonzero, so \(g_0\) has exact degree three.
The degree-three plane-coordinate criterion gives an
affine-linear plane change taking \(g_0\) to
\(F(Y)+\delta Z\), where \(\delta\ne0\) is constant and
\(F\in\mathbb C[T]\) has degree three.[^1]
We have therefore reached
\[
\begin{gathered}
I=XW-F(Y)-\delta Z,\qquad
F(T)=\gamma T^3+f_2T^2+f_1T+f_0,\qquad
\gamma\delta\ne0,\\
s=EX,\qquad t=EY,\qquad r=EZ,\qquad
s\,E^2W=2\gamma t^3.
\end{gathered}
\tag{3}
\]
No assertion that \(s\) is a unit or that \(X\) is a slice
has been made. The final identity follows by applying
\(E^3\) to \(I\).

All these normalizations preserve (1).
Affine good changes act invertibly on the speed vector.
A fixed-good quadratic shear changes the acceleration
by an element of \(W_2\), and cannot cancel it because
the original acceleration is outside \(W_2\).
They preserve the existence of a primitive successful
lift and its subring \(\mathbb C[I]\), by the covariance
calculation in the mixed-cubic criterion.[^1]

## 3. Faithful leading coordinates and a pole lemma

Let \(\tau\) be the degree-one symbol for the \(u\)-filtration.
The three good initials
\[
\mathsf X=s\tau,\qquad
\mathsf Y=t\tau,\qquad
\mathsf Z=r\tau,\qquad
\operatorname{in}_E(W)=
        \gamma\frac{\mathsf Y^3}{\mathsf X}
\tag{4}
\]
are algebraically independent in their first three entries.
Indeed the coefficient of each power of \(\tau\) in a
polynomial relation would be a homogeneous relation among
\(s,t,r\), contrary to (1).
Likewise the ratios \(a=t/s\), \(b=r/s\) are algebraically
independent: homogenizing a relation between \(a,b\)
would give a homogeneous relation between \(s,t,r\).
The rational notation in (4) is used only for leading
comparisons in a fraction field.

Return to an arbitrary frame obtained by the normalizing
changes of Section 2, and consider a good-coordinate
elementary step there. In the normalized coordinates,
the two held good coordinates generate the ring of two
independent affine-linear forms, and the held bad coordinate
has the form
\(\kappa W+J_2(X,Y,Z)+J_1(X,Y,Z)+J_0\), with
\(\kappa\ne0\).
Constants in the held good forms can be subtracted.
Write their linear parts as \(\ell_1,\ell_2\).

Its three initials are
\(\ell_1,\ell_2,\kappa\gamma\mathsf Y^3/\mathsf X+J_2\),
viewed in the rational field
\(\mathbb C(\mathsf X,\mathsf Y,\mathsf Z)\).
If they are algebraically independent, no polynomial in
the held coordinates can have cancellation of its
highest weighted part, with weights \(1,1,2\).
Its \(E\)-affine elements are consequently just constants
and constant linear combinations of the two held goods.

Suppose instead that these three initials are dependent.
Let \(D\ne0\) be the constant direction annihilating
\(\ell_1,\ell_2\).
The rational field is
\(\mathbb C(\ell_1,\ell_2)(v)\) for a third linear coordinate.
A nonconstant rational function of \(v\) is transcendental
over \(\mathbb C(\ell_1,\ell_2)\); hence dependence is
equivalent to
\[
\begin{gathered}
D\left(\kappa\gamma\frac{\mathsf Y^3}{\mathsf X}
                     +J_2\right)=0,\\
\kappa\gamma
\bigl(3\mathsf X\mathsf Y^2D\mathsf Y
          -\mathsf Y^3D\mathsf X\bigr)
          +\mathsf X^2 DJ_2=0,\\
D\mathsf X=D\mathsf Y=DJ_2=0.
\end{gathered}
\tag{5}
\]
For the last line, first reduce the middle line modulo
\(\mathsf X\) to get \(D\mathsf X=0\).
Divide the remaining identity by \(\mathsf X\), and
reduce again modulo \(\mathsf X\), obtaining
\(D\mathsf Y=0\). The final equality follows.

Thus \(D\) is a nonzero multiple of \(\partial_{\mathsf Z}\),
the held good forms span \(X,Y\), and \(J_2\) is independent
of \(Z\). Subtracting polynomials in the held goods and
scaling the held bad coordinate reduces its actual
polynomial ring, not merely its initial field, to
\(\mathbb C[X,Y,W+\beta Z]\) for some constant \(\beta\).
This also accounts for the possible \(Z\)-term in \(J_1\).

## 4. Both exact excluded-slot normal forms

Put
\[
\begin{gathered}
W_\beta=W+\beta Z,\qquad
H_\beta=XW_\beta-F(Y)
       =(\delta+\beta X)Z+I,\qquad
R_\beta=\mathbb C[X,Y,W_\beta],\\
\ker(E^2)\cap R_\beta=
\begin{cases}
\mathbb C\oplus\mathbb CX\oplus\mathbb CY
                  \oplus\mathbb CH_0,&\beta=0,\\
\mathbb C\oplus\mathbb CX\oplus\mathbb CY,&\beta\ne0.
\end{cases}
\end{gathered}
\tag{6}
\]
Here the notation \(\ker(E^2)\cap R_\beta\) means the
polynomials killed by the second iterate; it does not
assert that \(E\) preserves \(R_\beta\).

We prove (6), including possible leading cancellations.
The relation \(XW_\beta=H_\beta+F(Y)\) gives normal
monomials
\[
\begin{gathered}
X^iY^jH_\beta^k\quad(i,j,k\ge0),
\qquad
Y^jH_\beta^kW_\beta^l\quad(j,k\ge0,\ l\ge1),\\
e=\deg_E H_\beta=
\begin{cases}1,&\beta=0,\\2,&\beta\ne0,\end{cases}\\
\begin{array}{c|c|c}
 &d=\text{\(E\)-degree}&
 (p,k)=\text{exponents of \(a,b\) in its leading coefficient}\\
X^iY^jH_\beta^k&i+j+ek&(j,k)\\
Y^jH_\beta^kW_\beta^l&j+ek+2l&(j+3l,k).
\end{array}
\end{gathered}
\tag{7}
\]
They span by repeatedly replacing a factor \(XW_\beta\).
Equivalently they are the monomials avoiding \(XW_\beta\)
for the monic relation
\(XW_\beta-H_\beta-F(Y)\), ordered with that leading monomial.

For \(\beta=0\), the initial of \(H_0\) is \(\delta r\tau\).
For \(\beta\ne0\), it is \(\beta sr\tau^2\).
After removing the common nonzero factor \(s^d\), every
leading coefficient in (7) is a nonzero constant times
\(a^p b^k\).
In the first family \(p+ek\le d\); in the second
\(p+ek=d+l>d\).
The families therefore have disjoint leading monomials
at fixed degree. Within either family, \(d,p,k\)
uniquely recover all indices. Independence of \(a,b\)
prevents any cancellation of the highest \(E\)-degree
in a nonzero normal form, and also proves uniqueness
of that form.
The monomials of degree at most one are exactly those
listed in (6).

## 5. The only nonlinear good replacement rescales the invariant

The independent-initial case of Section 3 and the
\(\beta\ne0\) case of (6) permit only affine good changes.
These are already covered by covariance.
The remaining case has held ring \(\mathbb C[X,Y,W]\).
Reducing the held bad generator to \(W\) by a scaling
and polynomials in \(X,Y\) is allowed covariance on both
endpoints; it does not assume that the original step
fixed the normalized generator \(W\).
After harmless affine changes in the good coordinates,
every permitted replacement has the form
\[
\begin{gathered}
Z'=\kappa Z+\zeta H_0+\lambda X+\mu Y+\nu,
\qquad \kappa\ne0,\qquad
\theta=\kappa+\delta\zeta,\\
EZ'=\theta r+\lambda s+\mu t,\qquad \theta\ne0,\\
I':=H_0-\frac{\delta}{\theta}
       \bigl(Z'-\lambda X-\mu Y-\nu\bigr)
       =\frac{\kappa}{\theta}I.
\end{gathered}
\tag{8}
\]
The nonvanishing of \(\theta\) is forced by cone density:
otherwise the new three speeds would satisfy a nonzero
constant homogeneous linear relation.
Speed rank alone would not justify this conclusion.

The new leading relation is still
\((EX)(E^2W)=2\gamma(EY)^3\),
so its homogeneous pair is \(L=X,F_3=\gamma Y^3\),
which is primitive. More explicitly its first correction
subtracts \(f_2Y^2\), and the remaining linear terms in
(8) supply its second correction. Thus \(I'\) is a
successful primitive lift in the new actual frame.
It is a nonzero constant multiple of \(I\).
The good-speed vector changes by an invertible constant
matrix.

## 6. Bad replacements and induction along the word

For a bad-coordinate step, the good ring is fixed.
Cone density gives
\(\deg_E G(x_1,x_2,x_3)=\deg G\) for nonconstant \(G\).
Thus replacing \(z\) by \(\kappa z+G\) and retaining
exact degree two forces \(\deg G\le2\).
This is precisely a bad scaling and fixed-good quadratic
shear from the correction criterion.
It preserves a successful primitive lift up to scale
and addition of a constant.[^1]

Sections 3--5 apply to a good-coordinate step in any
successful frame, not only the normalized one: the
held-coordinate ring after normalization was treated with
arbitrary affine good forms and arbitrary quadratic and
linear bad shear terms.
Consequently one step satisfying the intermediate-frame
restriction preserves success, primitivity, and
\(\mathbb C[I]\).
Induction proves the claim for any finite word.

This rules out finding a primitive correction failure
by elementary changes from a successful seed while keeping
every intermediate frame inside (1).
Such a search must instead leave the specified class at
some step or start in another elementary component.
The result does not classify those components, guarantee
an elementary path between arbitrary frames, or settle
the missing correction tests in every actual primitive
frame. It gives no unrestricted frame-entry or
cancellation conclusion.

## 7. An exact word showing why the intermediate restriction matters

Take the actual divided-difference frame with
\(F(T)=T^3/2\), whose inverse is polynomial in both orders.[^3]
Write
\(\Delta(A,V,X)=3AV^2/2+3A^2VX/2+A^3X^2/2\).
Starting in its current slots \((X,Y,Z,W)\), perform
\[
\begin{array}{rll}
1.&Z\leftarrow Z-XW+Y^3/2,\\
2.&Y\leftarrow Y-ZX,\\
3.&W\leftarrow W-\Delta(Z,Y,X),\\
4.&Z\leftarrow Z+W,\\
5.&W\leftarrow W+\Delta(Z,Y,X),\\
6.&Y\leftarrow Y+ZX,\\
7.&Z\leftarrow Z+XW-Y^3/2.
\end{array}
\tag{9}
\]
Each step adds a polynomial independent of the changed
current slot, so it has an elementary polynomial inverse.
The first three steps give \((u,v,a,b)\).
The fourth gives \((u,v,a+b,b)\), and the last three
are the reverse reconstruction of the divided-difference
frame with \(a\) replaced by \(a+b\).
This also proves both inverse orders of the complete word.
The total automorphism commutes with \(E\): in the adapted
coordinates \((u,v,a,b)\), its middle shear fixes \(u\)
and changes only invariant variables.

Both endpoints satisfy (1) and have successful primitive
lifts. The original lift is \(-a\); the final lift is
\(-(a+b)\). Since \(a,b\) are independent polynomial
variables, \(\mathbb C[a]\ne\mathbb C[a+b]\).
There is no contradiction to the stability result:
the first step makes \(Z\) invariant and destroys cone
density, and the third makes the bad coordinate invariant.
Thus the invariant subring need not be preserved by an
arbitrary elementary word even between successful
endpoints. This example is not a primitive gate failure.

## Sources

1. [Correcting a mixed cubic relation to an invariant coordinate](three-good-mixed-cubic-correction-criterion-pass130.md).
   Sections 2--3 give the two correction tests, primitive
   uniqueness, and fixed-good covariance. Section 5 gives
   the degree-three plane-coordinate normalization.
2. [An invariant linear suspension in a sliced polynomial fourfold](invariant-linear-suspension-recognition-pass130.md).
   Sections 1--6 prove automatic coordinate recognition
   after both derivative tests, including its classical
   topological and plane-curve inputs.
3. [Cubic acceleration outside the fixed-good quadratic span](three-good-cubic-acceleration-span-obstruction-pass129.md).
   Sections 1--4 give the actual divided-difference frame,
   its two-sided polynomial inverse, and its selected profile.

[^1]: [Mixed-cubic correction criterion](three-good-mixed-cubic-correction-criterion-pass130.md),
    Sections 2, 3, and 5.
[^2]: [Invariant linear-suspension recognition](invariant-linear-suspension-recognition-pass130.md),
    especially Section 6 for the mixed-cubic application.
[^3]: [The divided-difference frame](three-good-cubic-acceleration-span-obstruction-pass129.md),
    Sections 1--4.
