# An actual rank-two frame whose bad partial moves the speed plane

## 1. The precise failed inference

The existence of a common intrinsic polynomial-plane quotient does
not imply that the selected original bad partial preserves that
plane, or even sends its elements into the original action's kernel.
The following actual polynomial coordinate frame has speed rank
two, a unit speed row, three complex-linearly-independent speeds,
nonzero nonconical determinant, and selected bad adjoint degree two.
Nevertheless the indicated stability fails.

This is a recognized translation action with an explicit inverse.
It is not a cancellation counterexample or an example showing
that rank-two recognition is impossible.

## 2. The original coordinates and their polynomial inverse

Start with the polynomial ring in adapted coordinates
\(B=\mathbb C[a,b,c,u]\), the translation \(E=\partial_u\), and
its actual kernel \(A=\mathbb C[a,b,c]\). Define
\[
Y=b+au,\qquad Z=c+a^2u,\qquad
W=a+Y^2,\qquad X=u+YZ-aW .
\tag{1}
\]
These are actual polynomial coordinates, with inverse
\[
a=W-Y^2,\qquad u=X-YZ+(W-Y^2)W,\qquad
b=Y-au,\qquad c=Z-a^2u .
\tag{2}
\]
Both orders are direct identities. Substituting (1) into (2)
recovers \(a\), then \(u\), then \(b,c\). Conversely, the latter
two formulas make the reconstructed \(Y,Z\) equal the given
ones; then \(a+Y^2=W\), and \(u+YZ-aW=X\).
No localization, rational inverse, or proposed coefficient-only
realization occurs.

Equivalently, first use the actual frame
\((u,Y,Z,W)\), whose inverse is the first, third, and fourth
formulas of (2) with \(u\) retained. Then apply the elementary
shear \(X=u+YZ-(W-Y^2)W\), which fixes \(Y,Z,W\).
The Jacobian with respect to \((a,b,c,u)\) is the constant
\(-1\), since the preliminary frame has that determinant and
the final shear has determinant one.

## 3. Rank, unit row, full span, and the nonconical determinant

Put \(h=c-ab\). The change \((a,b,c)\leftrightarrow(a,b,h)\)
is polynomial, so \(a,h\) are algebraically independent. Direct
differentiation in \(u\) gives
\[
\begin{gathered}
EX=1+ah,\qquad EY=a,\qquad EZ=a^2,\qquad
EW=2aY,\qquad E^2W=2a^2,\qquad E^3W=0,\\
E^2X=E^2Y=E^2Z=0,\qquad
\mathbb C(EX,EY,EZ)=\mathbb C(a,h),\\
1=EX-h\,EY,\qquad
\det\bigl[\mathbf a,\partial_a\mathbf a,\partial_h\mathbf a\bigr]
=a^3\ne0,\quad
\mathbf a=(1+ah,a,a^2)^t .
\end{gathered}
\tag{3}
\]
For the speed-field equality, \(a=EY\) and
\(h=(EX-1)/a\) give one inclusion in fraction fields; the other
is immediate. This does not identify the speed algebra with
\(\mathbb C[a,h]\). In fact the displayed speed algebra is
\(\mathbb C[a,ah]\).

The exact Bézout identity in (3) proves that the good speeds
generate the unit ideal in \(B\), and already in
\(\mathbb C[a,h]\). They are linearly independent over
\(\mathbb C\): a constant relation among \(1+ah,a,a^2\)
first has zero coefficient on \(ah\), then zero coefficients
on \(a,a^2\). Thus there is no invariant nonzero constant
linear form in the three good coordinates.

The determinant in (3) is the standard nonconical speed
determinant in the actual independent parameters \(a,h\).
It is generically nonzero, not everywhere invertible.
The acceleration \(2a^2\) is nonconstant. None of these facts
asserts a constant-acceleration frame.

## 4. The actual bad partial and its leading intrinsic kernel

Let \(T=\partial_W\), holding the other original coordinates
\(X,Y,Z\) fixed. Differentiating the explicit inverse (2) gives
\[
\begin{gathered}
Ta=1,\qquad Tu=a+W=2a+(b+au)^2=:V,\\
Tb=-u-aV,\qquad Tc=-2au-a^2V,\\
T=\partial_a+(-u-aV)\partial_b
                   +(-2au-a^2V)\partial_c+V\partial_u .
\end{gathered}
\tag{4}
\]
It is an actual locally nilpotent coordinate partial because
(2) is a polynomial inverse. Its exact shift for the
\(u\)-degree filtration is two: its values on \(b,c\) have
nonzero quadratic coefficients, while its value on \(u\)
has degree two and therefore contributes shift one.

Its homogeneous leading field and the full second adjoint
are different:
\[
\begin{gathered}
H=u^2N,\qquad
N=-a^3(\partial_b+a\partial_c)\in\operatorname{LND}(A),\\
S=\ker N=\mathbb C[a,h],\qquad h=c-ab,\\
[E,[E,T]]=2N+2a^2\partial_u\ne0,\qquad
[E,[E,[E,T]]]=0 .
\end{gathered}
\tag{5}
\]
Indeed \(N\) fixes \(a,h\), and in the coordinates
\((a,b,h)\) its primitive direction is \(\partial_b\).
Multiplication by the nonzero invariant \(-a^3\) does not
change that kernel. Thus the polynomial-plane quotient here
is completely explicit; no quotient-recognition theorem is
needed to identify it.

All three speeds, and also the quadratic acceleration in (3),
belong to this same \(S\). Formula (5) verifies exact selected
bad adjoint degree two, rather than merely the upper bound.
It also retains the distinction between the intrinsic top
field \(N\), which kills \(u\) on extension, and the second
commutator, which need not do so.

## 5. Failure of quotient stability and its limits

Despite all these properties, the selected original partial
satisfies
\[
T(h)=Tc-a\,Tb-b\,Ta=-b-au=-Y,\qquad
E(T(h))=-a\ne0,\qquad
T(S)\not\subset A,\quad T(S)\not\subset S .
\tag{6}
\]
Thus actual speed containment in the intrinsic plane does
not make that plane stable under the original bad partial.
Nor does the intrinsic top's vanishing on the plane imply
vanishing of the lower \(u\)-coefficients of that partial.

The common-kernel and degree-drop conclusions of
[125](three-good-intrinsic-speed-quotient-pass125.md) and
[126](three-good-flow-cofactor-bounds-pass126.md) remain valid:
here \(T(h)\) has precisely the permitted degree \(2-1=1\).
This control rules out strengthening that conclusion to
preservation of \(A\) or \(S\) without a new argument.
It does not disprove a recognition theorem for speed rank
two, and it does not supply a hypothetical nonpolynomial
kernel. The given \(E=\partial_u\) has the explicit polynomial
kernel \(A=\mathbb C[a,b,c]\) from the start.

General constructed this frame by an elementary shear of
the actual curve control126; Root independently checked the
inverse, speed row, leading field, and instability identity.
The fifth method of the shared
[finite checker127](three_good_speed_curve_checks_pass127.py)
checks both inverse orders, the actual coordinate partial,
the extracted top, the unit/rank-two row, and
\(T(h)=-Y,\ E(T(h))=-a\). The kernel equality and the stated
logical boundary are justified in the written proof, not by
a finite test. The checker was independently read through
its full original four methods and the complete fifth-method
delta without execution by this author.
This is a finite algebraic control, not an all-rank-two
classification. No numerical run or new primary-source read
is claimed here, and no file through pass126 is changed.
