# An actual sharp dense-tail family with nonconstant first speed

A constant linear reframe of the retained divided-difference family129
attains the bounds for the projected coordinates and both tails in139.
Both projected good coordinates have degree \(m+1\), the primitive line equation has degree \(m+1\),
and the second tail polynomial has degree \(m+2\). Its first speed is
a nonconstant invariant. Moreover, the particular second tail does not
complete the primitive equation to a plane automorphism.

This is an actual polynomial family, not a realization inferred from a
Jacobian condition. It has a linear combination of good coordinates as
a slice and is already a translation. It does not obstruct recognition
or furnish a cancellation counterexample. The construction is explicitly
a reframe of129, with no historical novelty claim.[^1]

## 1. Polynomial construction and both inverse orders

Let \(F(t)=\sum_{k=0}^d c_kt^k\in\mathbb C[t]\), with
\(d\ge2\) and \(c_d\ne0\). In
\(B=\mathbb C[u,a,b,v]\), use \(E=\partial_u\) and the polynomial
\[
\Delta_F(a,v,u)=\sum_{k=1}^d c_k\sum_{j=1}^k
\binom kj v^{k-j}a^ju^{j-1},\qquad
u\Delta_F=F(v+au)-F(v).
\tag{1}
\]
In particular no denominator is being inverted at \(u=0\).
Define the original coordinate frame by
\[
\begin{gathered}
X=v+au,\qquad Y=a-F(v)+(b+1)u,\\
Z=a-F(v)+(b+2)u,\qquad W=b+\Delta_F(a,v,u),\\
u=Z-Y,\quad a=2Y-Z-(Z-Y)W+F(X),\quad
v=X-au,\quad b=W-\Delta_F(a,v,u).
\end{gathered}
\tag{2}
\]
The last line is the polynomial inverse, with the quantities on the
right recovered successively. Substitution of the forward map gives
\(2Y-Z=a-F(v)+bu\); then (1) recovers \(a\), followed by \(v,b\).
Conversely the inverse definitions recover \(X,W\) directly, and
\(a-F(v)+bu=a+uW-F(X)=2Y-Z\). Together with \(u=Z-Y\), this
recovers \(Y,Z\). These are both inverse compositions on the whole
affine space.

Equivalently, from the129 frame
\((x_0,y_0,z_0,w_0)=(u,v+au,a-F(v)+bu,b+\Delta_F)\), take
\((X,Y,Z,W)=(y_0,z_0+x_0,z_0+2x_0,w_0)\). That constant good-slot
change has determinant one. The full Jacobian relative to
\((u,a,b,v)\) is also one.

## 2. Actual sliced dense data and the selected partial

The three good speeds and the last-coordinate degree are
\[
\begin{gathered}
(EX,EY,EZ)=(a,b+1,b+2),\qquad E^2X=E^2Y=E^2Z=0,\\
EZ-EY=1,\qquad Z-Y=u,\qquad \ker E=\mathbb C[a,b,v],\\
\det[\mathbf a,\partial_a\mathbf a,\partial_b\mathbf a]=1,
\quad \mathbf a=(a,b+1,b+2)^t,\qquad
m=\deg_E W=d-1 .
\end{gathered}
\tag{3}
\]
The speeds generate \(\mathbb C[a,b]\), so have rank two. Their
homogeneous cone is dense: the cone map \((t,a,b)\mapsto t\mathbf a\)
has nonzero Jacobian \(t^2\). Their ideal is the unit ideal even on
\(a=0\), but the first speed \(s=a\) is a nonunit. The last
coordinate has leading \(u\)-coefficient \(c_da^d\ne0\).

The actual partial fixing \(X,Y,Z\) is
\[
T=\partial_W=-u\partial_a+(1+uF'(v))\partial_b+u^2\partial_v,
\quad Tu=0,\qquad
N=[u^2]T|_{\ker E}=\partial_v,\quad L=\mathbb C(a,b).
\tag{4}
\]
Indeed it kills each of the three goods in (2). Applying it to (1)
gives \(T\Delta_F=-uF'(v)\), so \(T(W)=1\). Since the frame is
an actual polynomial coordinate system, those four values identify
the original coordinate partial.

## 3. Exact localized normalization and the projected line

Use the actual first coordinate \(X\) on \(B_a\). The intrinsic
normalization and speed ratios are
\[
\begin{gathered}
N'=N/a^2=a^{-2}\partial_v,\qquad r=a^2v,\qquad N'r=1,\\
\tau=(b+1)/a,\quad \rho=(b+2)/a,\quad
a=1/(\rho-\tau),\quad b=(2\tau-\rho)/(\rho-\tau),\\
\partial_\tau|_L=a^2\partial_a+a(b+2)\partial_b,\qquad
\partial_\rho|_L=-a^2\partial_a-a(b+1)\partial_b .
\end{gathered}
\tag{5}
\]
Thus \(L=\mathbb C(\tau,\rho)\) in this particular family.
The parameter \(r\), not the old adapted \(v\), has normalized
intrinsic derivative one. Extending the coefficient partials to fix
\(r\) adds respectively \(-2av\partial_v\) and
\(2av\partial_v\) to the last line of (5).
No global inverse involving division by \(a\) is being asserted.

Projection to \(X=0\), where \(u=-v/a\), gives
\[
\begin{gathered}
y=a-F(v)-(b+1)v/a,\qquad
z=a-F(v)-(b+2)v/a,\\
y-z=v/a=r/a^3,\qquad L[y,z]=L[r],\qquad
\deg_r y=\deg_r z=d=m+1,\\
Y=y+\tau X,\quad Z=z+\rho X,\qquad
W=b+a\frac{F(X)-F(v)}{X-v}.
\end{gathered}
\tag{6}
\]
The last quotient is polynomial in \(X,v\); it is a divided
difference, not a new localization. Both projected degrees are
exactly \(d\) because their leading coefficient in \(v\) is
\(-c_d\). The nonzero rescaling \(r=a^2v\) over \(L\) preserves
those degrees. Thus both individual bounds from139 are sharp.[^2]
The relative determinant in \((\tau,\rho,r)\), with \(X\) fixed,
is one. Indeed the determinant of \((X,\tau,\rho,r)\) with respect
to \((u,a,b,v)\) is one; compare it with the actual frame Jacobian
from Section 1. Also \(T(r)=X^2-4vX+3v^2\), which verifies the
normalized coefficient \([X^2]T(r)=1\) directly.

## 4. Exact Taylor peeling for arbitrary \(F\)

Let \(U,V\) be independent variables, put \(D=U-V\), and use the
positive Taylor convention from139.[^3] Formula (5) gives the rational
generating series
\[
\begin{gathered}
\Theta(a)=\frac{a}{1-a(y-z)/X},\qquad
\Theta(b)=b+\frac{a((b+2)y-(b+1)z)}{X-a(y-z)},\\
C(X)=\frac{F(X)-c_0}{X}\in\mathbb C[X],\qquad
\mathscr S=\Theta(b)+C(X)\Theta(a)
=\sum_{j=0}^{m}X^j\Theta(f_j),\\
f_0=b+c_1a,\qquad f_j=c_{j+1}a\ (1\le j\le m),\qquad
\mathscr R=W-\mathscr S=\frac{a(c_0-a)}{X-v},
\qquad f_{-1}=a(c_0-a).
\end{gathered}
\tag{7}
\]
These identities are interpreted as Laurent series at \(X=\infty\).
To check the last line directly, use \(a(y-z)=v\) and
\((b+2)y-(b+1)z=a-F(v)\) in the first line, then use (6).
Thus the \(f_j\) in (7) are the exact peeling coefficients,
not fitted data from a finite Taylor truncation.

Define the formal plane coordinate
\[
G(U,V)=(b+2)U-(b+1)V+F(aD)-a.
\]
The first two Taylor-tail polynomials are exactly
\[
\begin{gathered}
\Phi=-aG,\qquad \Psi=a^3D-a^2DG,\qquad
\Phi(y,z)=0,\qquad \Psi(y,z)=a^2v=r,\\
\deg\Phi=\deg G=d=m+1,\qquad
\deg\Psi=d+1=m+2 .
\end{gathered}
\tag{8}
\]
For an independent coefficient check, the homogeneous Taylor pieces
are \(H_j(a)=a^{j+1}D^j\) and
\(H_j(b)=a^jD^{j-1}((b+2)U-(b+1)V)\) for \(j\ge1\).
Substitution into
\(R_1=-\sum_jH_{j+1}(f_j)\), followed by subtraction of
\(f_{-1}\), gives \(\Phi\). Substitution into
\(\Psi=-\sum_jH_{j+2}(f_j)-H_1(f_{-1})\) gives the second
formula in (8), including its sign. The highest homogeneous terms
are nonzero because \(c_d\ne0\), which proves both exact degrees.

## 5. A primitive first tail, but the second tail is not a complement

The pair \((D,G)\) is a plane coordinate system over \(L\), with
explicit inverse
\[
\begin{gathered}
U=G+a-(b+1)D-F(aD),\qquad
V=G+a-(b+2)D-F(aD),\\
\det\frac{\partial(G,\Psi)}{\partial(U,V)}=a^2(G-a).
\end{gathered}
\tag{9}
\]
The first line verifies both inverse orders by subtraction and then
the definition of \(G\). In particular \(G\) is irreducible and
generates the kernel of \(L[U,V]\to L[r]\). The first tail
\(\Phi=-aG\) has no extra factor except the coefficient-field unit.
This is a fact about this family, not a universal primitivity claim.

The last determinant is nonconstant, so \((G,\Psi)\) is not a
plane automorphism, even though \(\Psi\) generates the quotient
parameter and has intrinsic derivative one there. The same failure
holds for \((\Phi,\Psi)\), since \(-a\in L^*\).
Thus the distinction in139 between an unspecified complement and
the particular tail polynomial already occurs in actual sliced
dense frames, not only in bare plane-coefficient controls.

## Verification and scope

The [standalone checker140](sharp_dense_tail_controls_pass140.py)
uses \(F(t)=t^d/2+t+2\), \(d=2,3,4\). It checks both actual
inverse orders and the selected partial, independently differentiates
the coefficient-field Taylor pieces, verifies the normalized relative
Jacobian and both plane inverse orders, and checks the nonconstant
tail-pair determinant. Those finite samples are not a proof for all
\(F\); the identities (1)--(9) supply that proof.
A separate fourth method treats another actual coefficient-field-cover
family. It is not used in the argument above.

The example has the actual linear-good slice \(Z-Y=u\) and unit
speed ideal. It does not test an obstruction to that unit ideal or
the missing descent for general dense frames. It proves sharpness
and a precise failed-complement implication, while preserving the
polynomial inverse and the localization boundaries throughout.

## Sources

[^1]: [Divided-difference family129](three-good-cubic-acceleration-span-obstruction-pass129.md),
    Sections 1--3. The all-\(F\) actual inverse and selected partial
    are reproduced here after an explicit constant linear good-slot change.

[^2]: [Dense generic embedded line139](dense-generic-embedded-line-pass139-working.md),
    Sections 1, 3--4. Generic degree bounds and the distinction between
    a primitive equation and the chosen quotient parameter.

[^3]: [Actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
    Sections 5--6, and [negative tails139](dense-negative-tail-relations-pass139-working.md),
    Sections 2--4. These supply the Taylor-sign, peeling and tail conventions.
    No fresh external source audit is claimed for this explicit family.
