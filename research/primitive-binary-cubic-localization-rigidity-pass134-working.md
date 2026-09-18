# Pure-cube leading rigidity after invariant localization

The statement below is a working mathematical result with the listed dependencies.

The binary-cubic argument extends from a constant leading speed to
an arbitrary nonzero invariant leading speed. The localization is
at that speed, and the resulting ring is explicitly a polynomial
ring in the moving good coordinate over a localized three-variable
polynomial ring. Its Jacobian units cannot depend on that coordinate.

Consequently, the primitive alternative of the
leading dichotomy has, after the permitted constant good changes
and quadratic bad shear, the form \(XW-\gamma Y^3\).
Neither correction gate is asserted to pass, and no nonconstant
leading speed is asserted to become a unit in the original ring.

## 1. Actual normalized hypotheses

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u_0],\qquad
E=\partial_{u_0},\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad
s=EX\ne0,\quad t=EY,\quad r=EZ,\\
E^3W=0,\qquad q=E^2W\ne0,\qquad
s q=2C(t,r),\qquad 0\ne C\in\mathbb C[T,R]_3,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,r)=2,
\qquad s\tau,t\tau,r\tau
\text{ algebraically independent over }\mathbb C.
\end{gathered}
\tag{1}
\]
The four original generators are actual polynomial coordinates,
and \(\tau\) is an independent indeterminate.
The conclusion is
\[
C(T,R)=\gamma(\alpha T+\beta R)^3,\qquad
\gamma\in\mathbb C^*,\quad(\alpha,\beta)\ne(0,0).
\tag{2}
\]

These hypotheses arise from any primitive mixed relation
\(L(a)q=2F_3(a)\) in the supplied dense quadratic class.
Make a constant good change with \(X=L(x)\), and write
\(F_3(X,Y,Z)=XJ_2(X,Y,Z)+C(Y,Z)\).
The actual shear \(W=z-J_2(x)\) gives (1); primitivity gives
\(C\ne0\). Existence of this primitive relation when the
acceleration is outside the quadratic speed span is the separate
leading-dichotomy theorem.[^1]
No lower correction is used here.

## 2. The actual localized polynomial presentation

Localize at the nonzero invariant \(s\), and put \(D=E/s\).
This is locally nilpotent on \(B_s\), with the same invariant
ring \(A_s\), because multiplication by the invariant unit
\(s^{-1}\) and localization at \(s\) preserve its iterates.
Now \(DX=1\). If \(b=X-su_0\in A\), then
\[
B_s=A_s[u_0]=A_s[X],\qquad
\widehat t=t/s,\quad \widehat r=r/s,\quad
D^2W=q/s^2=2C(\widehat t,\widehat r).
\tag{3}
\]
The last equality uses homogeneity of \(C\).
The two ratios \(\widehat t,\widehat r\) are algebraically
independent: any polynomial relation between them homogenizes
to a nonzero homogeneous relation between \(s,t,r\).

Set \(s_0(Y,Z,W)=s(0,Y,Z,W)\) in the original coordinates.
Quotienting the actual localization by \(X\) gives
\[
\begin{gathered}
A_s\simeq B_s/(X)
 \simeq\mathbb C[Y,Z,W]_{s_0},\\
A_s=\mathbb C[y,z,w]_{s_0(y,z,w)},\qquad
s=s_0(y,z,w),\\
Y=y+\widehat t X,\qquad Z=z+\widehat r X,\qquad
W=w+dX+C(\widehat t,\widehat r)X^2,\quad d\in A_s.
\end{gathered}
\tag{4}
\]
Here \(y,z,w\) are the images of \(Y,Z,W\) under the finite
Taylor projection for the slice \(X\) of \(D\).
In particular \(y,z,w\) are algebraically independent.
The quotient is nonzero because \(B_s=A_s[X]\), so \(s_0\ne0\).
The equality for \(s\) follows either from this quotient
identification or by applying the Taylor projection to the
invariant polynomial \(s(X,Y,Z,W)\).

This is not a claim that \(A\) itself has those three generators.
It is an actual description of the localized ring, with its
denominators tracked. Write \(R_0=\mathbb C[y,z,w]_{s_0}\).
The transformation in (4) and its Taylor inverse are inverse
isomorphisms between localized polynomial rings. Their Jacobian
matrices therefore have inverse determinants in \(R_0[X]\).
Consequently the Jacobian determinant from \((X,y,z,w)\) to
\((X,Y,Z,W)\) is a unit of \(R_0[X]\).
Since \(R_0\) is a domain, every such unit belongs to \(R_0^*\)
and is independent of \(X\). At \(X=0\), the last three output
coordinates equal \(y,z,w\), so the determinant is \(1\).
Thus the actual localized Jacobian is identically \(1\).

## 3. The intrinsic leading derivation survives the localization

Let \(T=\partial_W\) in the actual original coordinates.
The dense cofactor theorem and the intrinsic leading construction
give
\(T(A)\subset A[u_0]_{\le2}\), with nonzero locally nilpotent
quadratic coefficient \(N\) on \(A\), and \(N(s)=N(t)=N(r)=0\).[^2]
Re-expand in \(X=su_0+b\). The new quadratic coefficient on
\(A_s\) is
\[
N'=[X^2]T|_{A_s}=s^{-2}N,\qquad
N'\in\operatorname{LND}(A_s)\setminus\{0\},\qquad
N'(\widehat t)=N'(\widehat r)=0.
\tag{5}
\]
Indeed \(N\) localizes at its invariant \(s\), and multiplying
it by the invariant unit \(s^{-2}\) preserves local nilpotence.
The coefficient identity on fractions follows from the quotient
rule. It is not necessary, and is not asserted, that the
localized derivation \(T\) is locally nilpotent: \(T(s)\) need
not vanish. Only the original \(T\) and the actual leading
derivation are used for that property.

Let \(S=\ker_A N\), \(L=\operatorname{Frac}S\).
The kernels of \(N\) and \(N'\) have the same fraction field.
A normalized local slice \(v\) gives
\(A_L=L[v]\), \(N'v=1\), and
\(F=\operatorname{Frac}A=L(v)\).
The extension \(L/\mathbb C(\widehat t,\widehat r)\) is finite
and separable. The proof is the same transcendence-basis argument
as in the constant-speed case: adjoining the independent \(v\)
preserves linear independence, and \(F\) is finitely generated.[^3]
Extend the two coordinate derivations through this finite
extension and fix \(v\). They commute, while
\(\ker\partial_v=L\).

Put \(p=(y,z)^T\), \(a=(\widehat t,\widehat r)^T\), and
\(M=\partial p/\partial a\).
Let \(j(X)\) be the Jacobian of \((Y,Z,W)\) with respect to
\((\widehat t,\widehat r,v)\), holding \(X\) fixed.
The localized unit Jacobian from Section 2 gives
\(j(X)=j(0)=j_0\in F^*\).
Since \(T(X)=0\), Cramer's rule gives
\[
T(v)=\frac{\det(M+XI_2)}{j_0},\qquad
[X^2]T(v)=\frac1{j_0}=N'v=1,\qquad j(X)=1.
\tag{6}
\]
This is the actual normalized volume computation, not an
assumed constant generic denominator.

## 4. The generic cubic and the complementary factor

For readability write \(a=(a_1,a_2)\) for
\((\widehat t,\widehat r)\) within this section.
The identical block determinant calculation from the
constant-speed proof now applies over \(L[v]\).[^3]
Its \(X^3,X^2,X\) coefficients give
\[
\begin{gathered}
d=\nabla C(a)^Tp+k,\qquad
w=\tfrac12p^T\operatorname{Hess}C(a)p+\nabla k^Tp+\ell,\\
G(U,V)=C(U,V)+\tfrac12(U,V)\operatorname{Hess}k\,(U,V)^T
                  +\nabla\ell^T(U,V)^T-m,\\
G(p)=0,\qquad
1=-\nabla G(p)^T\operatorname{adj}M\,p_v,\qquad
k,\ell,m\in L.
\end{gathered}
\tag{7}
\]
Gradients and Hessians of coefficients use \(a\).
The constants \(k,\ell,m\) are obtained by subtraction and
the equality \(\ker\partial_v=L\), not by assuming integrals
exist in \(L\).

The localization in (4) is harmless for the generic fiber:
\(s\in S\) becomes a field element in \(L\), so
\(A_L=L[y,z,w]\). The quadratic expression for \(w\) in
(7) therefore gives \(A_L=L[y,z]=L[v]\).
Let \(P\) generate the kernel of \(L[U,V]\to L[v]\), and
write \(G=PR\). The last identity of (7) makes \(R(p)\)
a unit of \(L[v]\). Thus \(R(p)\in L^*\).
One must not instead assume that the whole cubic is irreducible.

The component alternatives are exactly those proved in the
constant-speed calculation.[^3] A degree-two \(P\) would
have a nonconstant linear complementary factor, which cannot
be constant modulo \(P\). A degree-three \(P\) defines a
closed embedded affine line, whose cubic leading form is a
pure cube by the reproduced elementary degree-three argument.
For degree one, \(R(p)\in L^*\) implies \(G=cP+P^2Q\).
The leading line of \(P\) is therefore a repeated constant
factor of \(C\). Only the noncube double-root case remains.

## 5. Rational slopes still give a forbidden Jacobian factor

Normalize that case by a constant linear good change to
\(C(T,R)=\gamma T^2R\), \(\gamma\ne0\), and write the
line component as \(U=f\). Thus \(y=f\in L\).
The line identity and the unit complementary factor give
\[
k_{a_2a_2}=0,\qquad
k_{a_1a_2}=-2\gamma f,\qquad
f_{a_2}=0.
\tag{8}
\]
These are the same coefficient comparisons as before;
commutativity of the two extended derivations gives the
last equality.

Differentiating the monic minimal polynomial of \(f\)
over \(\mathbb C(a_1)(a_2)\) shows that \(f\) is algebraic
over \(\mathbb C(a_1)\).
The actual localized coordinate \(y=f\) is nonconstant,
so \(a_1=\widehat t\) is algebraic over \(\mathbb C(y)\).
Now the fraction field of (4) is
\(F=\mathbb C(y,z,w)\). Relative algebraic closedness of
\(\mathbb C(y)\) in this purely transcendental extension
gives
\(\widehat t\in\mathbb C(y)\).
It is a nonconstant rational function of \(y\), since
\(\widehat t,\widehat r\) are independent.

The correct conclusion is rationality in \(y\), not
polynomiality in \(y\). Nevertheless \(\widehat t\in R_0\),
and differentiation in \(y\) preserves \(R_0\).
Thus \(\widehat t'(y)\in R_0\) is nonzero.
From \(Y=y+\widehat t(y)X\), the first two rows of the
localized Jacobian make its determinant divisible in
\(R_0[X]\) by
\(1+X\widehat t'(y)\).
That polynomial has positive \(X\)-degree and is not a
unit of \(R_0[X]\). This contradicts the unit Jacobian
proved in Section 2. The double-root case is excluded,
establishing (2).

## 6. Leading consequence and the remaining correction gap

Combining (2) with the leading dichotomy gives the following
working reduction inside the actual dense three-good quadratic
class. If the acceleration is not removable by a fixed-good
quadratic shear, there is a primitive relation. After constant
good changes and a quadratic bad shear, its leading polynomial
can be taken to be \(XW-\gamma Y^3\), with \(\gamma\ne0\).
The leading speed \(EX=s\) can still be nonconstant.

There is no inference from this leading polynomial to an
invariant lift. Both lower correction conditions remain
separate. The argument also does not provide an admissible
frame for an arbitrary sliced action or prove general
cancellation.

## Sources

1. [A quadratic-or-primitive-cubic dichotomy for actual coordinate initials](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 2--4. Leading-relation existence in the supplied dense class.
2. [Dense three-good speeds force exact bad-partial adjoint degree two](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5, and [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. The actual quadratic coefficient and its invariant localization.
3. [A constant leading speed forces a pure-cube binary residue](constant-speed-binary-cubic-rigidity-pass134-working.md),
   Sections 2--5. Complete block-coefficient calculation, complementary-factor
   argument, and elementary degree-three embedded-line proof. The present note
   supplies the additional localized-ring and rational-slope steps rather than
   assuming its global polynomial presentation.

[^1]: [Leading dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md), Sections 2--4.
[^2]: [Dense cofactor theorem132](dense-three-good-adjoint-degree-pass132.md), Sections 2--5; [Intrinsic-speed construction125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^3]: [Constant-speed binary-cubic proof134](constant-speed-binary-cubic-rigidity-pass134-working.md), Sections 2--5.
