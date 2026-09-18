# A commuting constant direction forces a quadratic invariant correction

For an actual dense three-good quadratic frame, a commuting constant
ambient direction gives more than an invariant coordinate somewhere
in the polynomial ring. It forces an invariant obtained by adding
a polynomial of degree at most two in the good coordinates to the
bad coordinate itself. Consequently its acceleration belongs to the
constant quadratic speed span, and no primitive mixed-cubic relation
can occur.

This sharpens the coefficient information in the retained
commuting-partial recognition argument.[^1] It uses the same
three-variable classification, not a new classification of
locally nilpotent derivations. No global slice is assumed.

## 1. Statement and exact scope

Let \(k\) be a field of characteristic zero and assume
\[
\begin{gathered}
B=k[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}_k(B),\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad E^3z=0,\qquad q=E^2z,\\
P(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }
P\in k[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
All four generators in (1) are actual polynomial coordinates.
Suppose a nonzero constant derivation
\[
D=\sum_{i=1}^3 v_i\partial_{x_i}+\kappa\partial_z,
\qquad v_i,\kappa\in k,\qquad [E,D]=0
\tag{2}
\]
exists. Then there is a polynomial \(K\in k[x_1,x_2,x_3]\)
of ordinary degree at most two such that
\[
E(z+K)=0,\qquad
q=-2K_2(a_1,a_2,a_3)
\in W_2:=\operatorname{span}_k\{a_i a_j: i\le j\},
\tag{3}
\]
where \(K_2\) is the homogeneous quadratic part of \(K\).
The replacement \(z'=z+K\) is an actual elementary change
of coordinates, with inverse \(z=z'-K\).

In particular, if \(q\ne0\), this same fixed-good shear
lowers the bad coordinate's \(E\)-degree from two to zero,
not merely to one. The theorem assumes neither a unit
good-speed ideal nor a constant-speed good coordinate.

## 2. Reduction to a commuting good-coordinate partial

First suppose the good projection \(v=(v_1,v_2,v_3)\) is
nonzero. Choose a \(k\)-linear good coordinate \(X\) with
\(DX=1\), and complete it by good linear coordinates \(y_1,y_2\)
annihilated by \(D\). Put \(z_0=z-\kappa X\).
Then
\[
B=k[X,y_1,y_2,z_0],\qquad
D=\partial_X,\qquad
R:=\ker D=k[y_1,y_2,z_0],\qquad E(R)\subset R.
\tag{4}
\]
The coordinate change is invertible and linear. It preserves
the dense homogeneous cone of good speeds, the three
second-iterate vanishings, and \(E^3z_0=0\). Moreover
\(E^2z_0=q\). Let \(\mathcal E=E|_R\).

This is a locally nilpotent derivation of an actual polynomial
three-ring. It cannot be zero: otherwise both retained good
speeds would be zero, contradicting density.

The case \(v=0\) is impossible under (1).
Indeed \(D=\kappa\partial_z\), with \(\kappa\ne0\), would make
all \(a_i\) elements of \(k[x_1,x_2,x_3]\). For a nonzero
polynomial \(H\) in this good ring of total degree \(d\),
\[
E^dH=d!\,H_d(a_1,a_2,a_3)\ne0,\qquad E^{d+1}H=0,
\tag{5}
\]
where \(H_d\) is its highest homogeneous part.
This follows by the Leibniz formula and \(E^2x_i=0\);
density prevents cancellation of the top coefficient.
Thus every invariant in the good ring is constant.
Since \(Ea_i=0\), all \(a_i\) would be constants, which
necessarily satisfy a nonzero homogeneous linear relation.
This contradicts (1).

## 3. Primitive reduction in the actual three-ring

Let \(h\) be a greatest common divisor of the three
coefficients of \(\mathcal E\) in \(R\).
Then \(\mathcal E(h)=0\). To see this, let \(p\) be an
irreducible factor of \(h\). Every coefficient of
\(\mathcal E\) is divisible by \(p\), so
\(\mathcal E(p)\in pR\).
For a locally nilpotent derivation in a characteristic-zero
domain, \(p\mid\mathcal E(p)\) implies \(\mathcal E(p)=0\):
otherwise the additivity of the derivation degree on products
would contradict
\(\deg_{\mathcal E}\mathcal E(p)=\deg_{\mathcal E}p-1\).
Applying this to every factor proves the assertion for \(h\).

Consequently \(\mathcal E_0=\mathcal E/h\) is a derivation
of \(R\), is irreducible, and is locally nilpotent.
More explicitly,
\(\mathcal E^n(f)=h^n\mathcal E_0^n(f)\) for all \(f\in R\).
This also proves
\(\mathcal E_0^2y_1=\mathcal E_0^2y_2=0\) and
\(\mathcal E_0^3z_0=0\).
This division is justified inside \(R\); it is not an
unsupported assertion of local nilpotence after localization.

## 4. The cubic derivative bound sharpens Wang's alternatives

Apply Wang's two-quasi classification in the exact form
of Dasgupta--Gupta, Theorem 4.1.[^2]
Its first alternative supplies an invariant nonzero
\(k\)-linear form in \(y_1,y_2\).
Multiplication by \(h\) shows that the corresponding
constant linear combination of their actual \(E\)-speeds
is zero. Density excludes this alternative.

In the second alternative there is an invariant coordinate
\(V\) retaining both \(y_1,y_2\), and polynomials \(f,g\in k[V]\),
such that
\[
\begin{gathered}
R=k[V,y_1,y_2],\qquad
V=\lambda z_0+P(y_1,y_2),\quad
\lambda\in k^*,\quad P\in k[y_1,y_2],\\
\mathcal E_0 V=0,\qquad
\mathcal E_0 y_1=f(V),\qquad
\mathcal E_0 y_2=g(V).
\end{gathered}
\tag{6}
\]
The expression for \(V\) follows from
\(k[y_1,y_2,V]=k[y_1,y_2,z_0]\):
mutually inverse polynomials in the single variable \(z_0\)
over \(k[y_1,y_2]\) have degree one and unit leading coefficient.

Neither \(f\) nor \(g\) is zero, and \(f/g\) is not a
constant in \(k\), since otherwise the actual speeds
\(hf,hg\) satisfy a constant linear relation.
Thus \(f/g\), a nonconstant rational function of \(V\),
is transcendental over \(k\). In particular
\(f^3,f^2g,fg^2,g^3\) are linearly independent over \(k\).

Taking three derivatives of (6) gives
\[
0=\mathcal E_0^3P
=f^3P_{111}+3f^2gP_{112}+3fg^2P_{122}+g^3P_{222}.
\tag{7}
\]
Here \(P_{112}\), for example, means
\(\partial_{y_1}^2\partial_{y_2}P\).
The three variables \(V,y_1,y_2\) are independent.
Compare each monomial in \(y_1,y_2\) in (7).
The stated linear independence in \(k[V]\) forces all
four third partial derivatives of \(P\) to vanish.
In characteristic zero, this is equivalent to \(\deg P\le2\).

This last degree bound is the additional information beyond
the retained commuting-partial recognition argument.

## 5. The actual quadratic invariant and covariance

Since \(E(V)=h\mathcal E_0(V)=0\),
the actual bad replacement
\[
z_0+\lambda^{-1}P(y_1,y_2)
=z-\kappa X+\lambda^{-1}P(y_1,y_2)
\tag{8}
\]
is invariant. Its added polynomial is of degree at most
two in the original goods. Taking its second derivative
proves (3), including the sign.
This also supplies the polynomial inverse of the
coordinate change directly.

The reduction in Section 2 is why the assertion is about
all constant ambient directions, not only a particular
list of coordinate partials. Constant good linear changes
and the affine bad correction used there preserve the
quadratic speed span. No constancy of the speed of the
omitted good coordinate was used.

## 6. Exclusion of a primitive mixed relation

Suppose in addition there were a relation
\[
L(a)q=2F_3(a),\qquad
L\ne0\text{ homogeneous linear},\qquad
F_3\text{ homogeneous cubic},\qquad \gcd(L,F_3)=1.
\tag{9}
\]
Equation (3) gives \(q=Q_2(a)\) for a homogeneous quadratic
\(Q_2\) over \(k\). Density applied to the homogeneous cubic
\(LQ_2-2F_3\) makes that polynomial identically zero.
Hence \(L\mid F_3\), contradicting primitivity.

Therefore an actual primitive dense quadratic three-good
frame has no nonzero constant ambient direction commuting
with \(E\). This is a necessary restriction on such frames,
not a proof that their two correction gates pass or fail.
The absence of a constant commuting direction is not
claimed to be sufficient for any recognition conclusion.

With a global slice, the older argument already recognizes
the kernel in a commuting-partial case.[^1]
The contribution here is the sharper low-degree invariant
and constant quadratic-span restriction. It does not
produce an arbitrary three-good frame, establish existence
of a primitive relation, or settle general cancellation.

## Sources

1. [Common leading kernels and the commuting-partial recognition gate](three-good-common-leading-kernel-boundary-pass126.md),
   Section 3. This retained argument divides the coefficient gcd
   and invokes the same exact three-variable classification.
   Its recognition endpoint is not needed for the proof above.
2. Nikhilesh Dasgupta and Neena Gupta. *Nice derivations over
   principal ideal domains*. arXiv:1701.03635v1, Theorem 4.1,
   printed p. 9. [Primary text](https://arxiv.org/pdf/1701.03635v1).
   The theorem attributes the characteristic-zero two-quasi
   classification to Z. Wang, Theorem 4.7 and Remark 5.
   The input here is the exact alternative retaining the two
   good coordinates, not a relative statement over an arbitrary ring.

[^1]: [Retained commuting-partial recognition126](three-good-common-leading-kernel-boundary-pass126.md), Section 3.
[^2]: Dasgupta--Gupta, Theorem 4.1, printed p. 9, [primary statement](https://arxiv.org/pdf/1701.03635v1).
