# Dense good speeds have no common invariant divisor

In an actual fixed-point-free polynomial action, dense affine-in-time
good-coordinate speeds have greatest common divisor one. The good-speed
ideal need not be the unit ideal: codimension-two common zeros remain
possible. There is no bound on the time degree of the remaining coordinate,
and a global slice is sufficient but unnecessary.

## 1. Actual hypotheses

Let \(k\) be a characteristic-zero field and assume
\[
\begin{gathered}
B=k[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}_k(B),\qquad
E^2x_i=0,\qquad a_i=Ex_i,\\
(E(B))B=(a_1,a_2,a_3,Ez)B=B,\\
F(a_1,a_2,a_3)\ne0
\quad\text{for every nonzero homogeneous }F\in k[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
All displayed generators are actual polynomial coordinates.
The middle equality is the algebraic fixed-point-free condition;
over an algebraically closed field it means that the action has no
fixed point. If \(Eu=1\) for some \(u\in B\), it follows immediately.
The conclusion is
\[
\gcd_B(a_1,a_2,a_3)=1.
\tag{2}
\]

The gcd conclusion is a direct dense-cone corollary of the retained
speed-ideal theorem: its coefficient gcd already belongs to the
actual good ring and to \(\ker E\).[^1] That proof does not use
the last-coordinate quadratic bound. The primewise reconstruction
below makes the fixed-point-free hypothesis sufficient without a
slice. No rank-one factorization of the speeds is used.

## 2. Proof by an actual original-coordinate derivative

For a nonzero \(H\in k[x_1,x_2,x_3]\) of total degree \(d\),
let \(H_d\) denote its highest homogeneous part. Since \(E(a_i)=0\),
\[
E^dH=d!\,H_d(a),\qquad E^{d+1}H=0,\qquad
\deg_E H=d.
\tag{3}
\]
The first value is nonzero by (1). Consequently
\(\ker E\cap k[x_1,x_2,x_3]=k\).
This degree identity needs neither a slice nor a bound on \(E(z)\).

Suppose an irreducible polynomial \(p\in B\) divides all three \(a_i\).
The kernel of an LND on a characteristic-zero domain is factorially
closed: the largest nonzero iterate defines an additive degree on
nonzero products. Since each \(a_i\) is invariant, \(Ep=0\).
By the middle condition in (1), the class of \(c=Ez\) is a unit
modulo \(p\). In the actual original coordinates,
\[
0=Ep=\sum_{i=1}^3 a_i\,p_{x_i}+c\,p_z,
\qquad p\mid p_z.
\tag{4}
\]
If \(p_z\ne0\), its degree in the actual variable \(z\) over
\(k[x_1,x_2,x_3]\) is strictly smaller than that of \(p\).
This contradicts the divisibility in (4). Hence \(p_z=0\),
so \(p\in k[x_1,x_2,x_3]\). It is invariant and nonconstant,
contrary to (3). This proves (2), with no localization.

In particular, if the speeds lie in a common intrinsic kernel,
they have no nonunit common divisor there either. A divisor in
that subring would still be a divisor in \(B\).

## 3. A related restriction on invariant divisors

The same density assumption, even without fixed-point freeness,
implies that every nonconstant irreducible invariant \(p\in B\)
satisfies
\[
(p)B\cap k[x_1,x_2,x_3]=0.
\tag{5}
\]
Indeed each prime factor of a nonzero polynomial in the good ring
remains prime on adjoining the independent variable \(z\).
If \(p\) divided such a polynomial, it would therefore be associated
to a polynomial in the good ring. That polynomial would be a
nonconstant invariant, again contradicting (3).

Thus the three actual good coordinates remain algebraically
independent modulo every invariant prime divisor. This does not
make the good speeds independent modulo that divisor, and does
not prevent an individual speed from vanishing there.

## 4. The good ideal can still be proper

The retained actual inverse family supplies the precise boundary.[^2]
In independent coordinates \((a,b,c,u)\), put \(h=b-a^2\) and
\[
\begin{gathered}
X=a+uh,\qquad Y=b+u(c+2ah),\qquad
Z=c-uh^2,\qquad W=u,\\
u=W,\qquad h=Y-X^2-WZ,\qquad
a=X-Wh,\qquad c=Z+Wh^2,\qquad b=h+a^2.
\end{gathered}
\tag{6}
\]
These recovery formulas give both polynomial inverse orders.
For \(E=\partial_u\), the good speeds are
\((h,c+2ah,-h^2)\). Their ideal is the proper height-two ideal
\((h,c)\), while their gcd is one.
Writing \(j=c+2ah\), the speed functions \((h,j,-h^2)\)
have rank two and dense homogeneous cone: their radial
Jacobian determinant with respect to \((h,j)\) is \(h^2\ne0\).
The action has the actual slice \(W\).

Accordingly (2) excludes divisorial common zeros only. It does
not force a unit good-speed ideal, make the leading linear speed
of a primitive cubic constant, or prove either correction test.
The invariant-divisor restriction (5) likewise does not recognize
an arbitrary sliced action.

## Sources

1. [Exact speed-ideal structure in the rank-one acceleration case](rank-one-acceleration-divisorial-ideal-pass82.md),
   Sections 2--4. The entire speed ideal is extended from the actual
   good ring, and its coefficient gcd belongs to that ring and
   to \(\ker E\). The final paragraph of Section 4 explicitly removes
   the last-coordinate quadratic bound from this argument. Here
   “rank-one acceleration” does not mean rank-one speed image.
2. [An aligned projective parameter cannot give the proposed nonlinear cone](aligned-projective-line-family-obstruction-pass77.md),
   Section 3, equation (6). The actual inverse family above is the
   retained nilpotent-Jacobian control, not a new construction.

[^1]: [Exact speed-ideal structure82](rank-one-acceleration-divisorial-ideal-pass82.md), Sections 2--4.
[^2]: [Actual inverse control77](aligned-projective-line-family-obstruction-pass77.md), Section 3.
