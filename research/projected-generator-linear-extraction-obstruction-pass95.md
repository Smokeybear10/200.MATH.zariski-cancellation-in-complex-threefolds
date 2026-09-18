# Linear extraction from the actual slice projection can fail completely

A specified polynomial slice does not guarantee that any nonzero
constant linear combination of its four projected original coordinates
is an invariant ambient coordinate. An actual tame translation below
has the stronger property that every such combination has a critical
point on its polynomial kernel. Consequently none supplies an
affine-plane fibration of that kernel either.

This is a decisive obstruction to one proposed universal bridge, not
a counterexample to cancellation. A different slice and explicit
nonlinear combinations recover invariant coordinates in the example.

## 1. The proposed bridge and the quantifiers

For an arbitrary sliced action, retain
\[
B=\mathbb C[x_0,x_1,x_2,x_3]=A[s],\qquad Es=1,\qquad
\pi(g)=\sum_{j\ge0}\frac{(-s)^j}{j!}E^j(g),\qquad
A=\mathbb C[\pi(x_0),\pi(x_1),\pi(x_2),\pi(x_3)].
\tag{1}
\]
The sums are finite. The generator and retraction assertions are the
retained slice theorem, not new results here. The attractive additional
claim would be: for every specified pair (E,s) in (1), some nonzero
constant coefficient vector gives an ambient coordinate
\(h=\sum_i\alpha_i\pi(x_i)\). An invariant coordinate would activate
the existing recognition theorem. A weaker possible claim would ask
that this h make A an affine-plane fibration over \(\mathbb C[h]\).
Both claims fail for the same actual pair below.

The [universal-frame audit52](universal-frame-reduction-audit-pass52.md)
and [degree-scope audit58](coordinate-slice-degree-scope-pass58.md)
were read completely before this attempt, as was the latest
[checkpoint94](checkpoint-pass94-working.json). The tangent-projection
controls in [pass22](nonlinear-frame-pass22.md) concern curvature and
projected derivations. The [quadratic-projection theorem74](quadratic-slice-projection-pass74.md)
has a separate ordinary-degree bound on the retraction. Neither is
being re-presented as a new arbitrary-frame theorem here.

## 2. An actual polynomial automorphism and its projection

Start with genuine coordinates \(s,a,b,c\), set
\[
\begin{gathered}
F=\frac{a^2}{2}+\frac{b^3}{3}+\frac{c^5}{5},\\
x_0=s+F,\qquad x_1=a+x_0^2,\qquad
x_2=b+x_0^3,\qquad x_3=c+x_0^4,\\
a=x_1-x_0^2,\qquad b=x_2-x_0^3,\qquad
c=x_3-x_0^4,\qquad s=x_0-F(a,b,c),\\
E=\partial_s
 =\partial_{x_0}+2x_0\partial_{x_1}
       +3x_0^2\partial_{x_2}+4x_0^3\partial_{x_3}.
\end{gathered}
\tag{2}
\]
The forward and inverse identities are exact polynomial identities
in both orders. They are successive shears, not merely a map with
unit Jacobian. Thus E is an actual LND, the displayed s is an actual
global slice, and \(A=\ker E=\mathbb C[a,b,c]\).

For this specified slice, \(\pi\) is evaluation at s=0. Hence
\[
\begin{gathered}
(f_0,f_1,f_2,f_3):=(\pi(x_0),\pi(x_1),\pi(x_2),\pi(x_3))
 =(F,a+F^2,b+F^3,c+F^4),\\
a=f_1-f_0^2,\qquad b=f_2-f_0^3,\qquad c=f_3-f_0^4.
\end{gathered}
\tag{3}
\]
These four generators have distinct ordinary degrees 5,10,15,20
in a,b,c. Every nonzero constant linear combination is therefore
nonconstant, even after adding a constant term.

## 3. Every constant linear combination has a critical point

Fix any \(\alpha=(\alpha_0,\alpha_1,\alpha_2,\alpha_3)\ne0\)
and put
\[
\begin{gathered}
h=\alpha_0F+\alpha_1(a+F^2)+\alpha_2(b+F^3)+\alpha_3(c+F^4),\\
T(Z)=\alpha_0+2\alpha_1Z+3\alpha_2Z^2+4\alpha_3Z^3,\\
(h_a,h_b,h_c)
 =(\alpha_1+aT(F),\ \alpha_2+b^2T(F),
                         \alpha_3+c^4T(F)).
\end{gathered}
\tag{4}
\]
If \(\alpha_1=\alpha_2=\alpha_3=0\), the origin is a critical
point, since \(\alpha_0\ne0\) and \(dF(0)=0\).

Otherwise choose complex numbers \(\beta,\gamma\) with
\(\beta^2=-\alpha_2\), \(\gamma^4=-\alpha_3\), and consider
the actual polynomial curve
\[
\begin{gathered}
a=-\alpha_1 t^4,\qquad b=\beta t^2,\qquad c=\gamma t,\\
F(t)=\frac{\alpha_1^2}{2}t^8
        +\frac{\beta^3}{3}t^6+\frac{\gamma^5}{5}t^5,\\
(h_a,h_b,h_c)\big|_{(a,b,c)=(-\alpha_1t^4,\beta t^2,\gamma t)}
 =(\alpha_1,\alpha_2,\alpha_3)\bigl(1-t^4T(F(t))\bigr).
\end{gathered}
\tag{5}
\]
At least one coefficient of F(t) is nonzero. Its possible degrees
8,6,5 are distinct, so F(t) is nonconstant. The polynomial T is
nonconstant too, because at least one of its positive-degree
coefficients is nonzero. Thus \(1-t^4T(F(t))\) is a nonconstant
polynomial with constant term one. Over \(\mathbb C\) it has a
root \(t_*\ne0\). Substituting that root in (5) gives a critical
point of h.

This is an all-coefficient proof. It includes vanishing entries of
\(\alpha\), and it does not extrapolate from generic coefficients
or a finite list of test vectors.

## 4. Coordinate and fibration consequences, with the slice boundary

The critical point of h on \(A=\mathbb C[a,b,c]\) remains critical
on \(B=A[s]\): h has zero s-derivative as well. Its differential
therefore vanishes at the whole corresponding s-line. The polynomial
inverse (2) transfers this to the original x-coordinate space.
A polynomial coordinate has nowhere-vanishing differential, as
follows by differentiating its full inverse map. Consequently
\[
\boxed{\quad
\text{for every }\alpha\ne0,\quad
\sum_{i=0}^3\alpha_i\pi(x_i)
\text{ is neither a coordinate of A nor a coordinate of B}.
\quad}
\tag{6}
\]
An added constant does not change this conclusion. At a critical
point p the nonconstant equation \(h-h(p)\) belongs to the square
of the three-dimensional regular local maximal ideal. Its hypersurface
quotient is not regular: it has dimension two but cotangent dimension
three. Thus this whole scheme fiber is not a polynomial plane.
In particular A is not an affine-plane fibration over
\(\mathbb C[h]\). The analogous fiber in B is also singular and is
not a polynomial three-space.

The obstruction is tied to constant linear extraction from the
projection for the specified slice s. It is not quantified over all
possible slices. In fact \(x_0\) itself is another E-slice, and its
projection gives the invariant coordinates a,b,c directly.
Alternatively, the nonlinear identities (3) recover them while
retaining s. The quadratic expression \(f_1-f_0^2=a\) shows that
the failure of every linear extraction is sharp as a lower bound
on the degree of at least one coordinate-extraction polynomial in
these four generators.

## 5. Verification and relevance to the general target

The [standalone control](projected_generator_extraction_checks_pass95.py)
checks both actual inverse orders, the transported field, the
projection and nonlinear recovery identities, and the symbolic
gradient restriction (5). Its one method does not numerically
prove the existence statement for all coefficient vectors; that
statement is the elementary polynomial-root argument above.

The first author execution of the standalone checker passed its
one method in 0.098 seconds, exit zero, with complete output in
chunk 0a1763. No assertion failed. This finite control does not
replace the universal coefficient argument or test cancellation.

This new failed bridge uses the full original polynomial-coordinate
condition, not only a quotient module, a nonnormal test ring, a
formal jet, or a tuple with a nonunit Jacobian. The kernel is already
polynomial, so it is neither an exotic factor nor an unrecognized
action. It disproves the proposed linear-retraction shortcut only.
It supplies no universal bound on coordinate changes, no general
frame reduction, no cancellation result, and no historical novelty
claim. All pass94 and earlier files remain unchanged.
