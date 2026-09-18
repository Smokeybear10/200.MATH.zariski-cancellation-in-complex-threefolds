# A squarefree double-cover obstruction for a weight-four initial relation

**Status: complete elementary working proof, pending saved-source review.**

Suppose a supplied actual two-linear/two-quadratic frame has full
weighted initial kernel
\[
(F),\qquad F=\mathsf Z^2+H_4(\mathsf X,\mathsf Y).
\]
If the binary quartic \(H_4\) is squarefree, this configuration is
impossible. The proof is a rational-function obstruction in the
ambient polynomial ring. It does not assume that the invariant
ring or its coefficient surface is rational.

This is the rank-one quadratic-bad form in which the other bad
variable is absent, once that placement has been justified by an
actual coordinate transformation. It is not an exclusion of a
rank-two form such as \(\mathsf Z\mathsf W+H_4(\mathsf X,\mathsf Y)\).

## 1. Precise actual hypotheses

Use the actual setup of
[the initial-bound proof157](two-linear-two-quadratic-initial-bound-pass157-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad Eu=1,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\qquad
a,b,e,h\in A\setminus\{0\},\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,h\eta^2),\qquad
\ker\theta_0=(\mathsf Z^2+H_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
Here \(\eta\) is independent over \(A\), the weights are
\((1,1,2,2)\), and the four original generators are actual
polynomial coordinates. The binary form is homogeneous of
ordinary degree four.

The full-kernel assumption makes \(F\) irreducible. It also
prevents any nonzero complex linear relation between \(a,b\):
such a relation would put a weight-one polynomial in \((F)\).
In particular
\[
t=b/a\notin\mathbb C,\qquad q=e/a^2,\qquad
q^2+H_4(1,t)=0
\quad\text{in }\operatorname{Frac}B=\mathbb C(X,Y,Z,W).
\tag{2}
\]
Nonconstancy of \(t\), not rationality of \(A\), is the essential
input in the argument below.

## 2. A rational-function obstruction with four simple branch values

We prove the following elementary assertion. Let
\(a,b,e\) be polynomials in an arbitrary complex polynomial ring,
with \(a\ne0\) and \(b/a\notin\mathbb C\). There cannot be an identity
\[
e^2+H_4(a,b)=0
\tag{3}
\]
when the homogeneous binary quartic \(H_4\) has four distinct
projective roots.

First make an invertible complex linear change of the pair \(a,b\)
so that the projective point at infinity for the new ratio is
not a root of the transformed binary form. This is possible
because there are only four roots. More explicitly, choose the
new first linear form so that its zero in \(\mathbb P^1\) is
outside that finite root set, and complete it to an invertible
pair. The transformed first coefficient is nonzero and the
transformed ratio is nonconstant, because \(a,b\) are not
proportional. Rename the new pair \(a,b\). Then
\[
p(T):=-H_4(1,T)
\]
has degree four, nonzero leading coefficient and four distinct
complex roots. Equation (3) becomes \(q^2=p(t)\).

In the actual application this linear change of \(a,b\) is
induced by the same invertible constant linear change of \(X,Y\),
fixing \(Z,W\). Its inverse is the inverse constant matrix.
All new good-coordinate speeds are nonzero by the full initial
kernel, so the time profile and the displayed type of kernel
are preserved. No coefficient-field change is being treated as
an original coordinate transformation.

Next choose two points \(P_0,P_1\) in the ambient affine space
such that \(a(P_i)\ne0\) and \(t(P_0)\ne t(P_1)\).
Such points exist: if \(t\) were constant on the nonempty
denominator-open subset \(a\ne0\), equality of rational functions
on this dense open set would make \(t\) constant.
Restrict all polynomials to the affine line
\[
P(s)=P_0+s(P_1-P_0).
\tag{4}
\]
The restricted denominator \(a(P(s))\) is nonzero at both
\(s=0,1\), hence is not the zero polynomial.
The rational function \(t(s)\) is nonconstant by its distinct
values at those parameters. The polynomial identity (3) survives
restriction, so in \(\mathbb C(s)\) we have
\[
q(s)^2=p(t(s)),\qquad t(s)\notin\mathbb C .
\tag{5}
\]
Also \(q(s)\ne0\); otherwise \(t(s)\) would satisfy a nonzero
complex polynomial and would be constant. Thus no unspecified
generic-line or dominant-map theorem is needed.

## 3. The differential has no possible pole

Consider on \(\mathbb P^1_s\) the rational differential
\[
\omega=\frac{dt(s)}{q(s)} .
\tag{6}
\]
It is nonzero because \(t(s)\) is nonconstant and the
characteristic is zero. We check its order at every point,
using a local coordinate there. These local coordinates include
\(z=1/s\) at infinity.

If \(t\) is regular and its value is not a root of \(p\),
then \(q\) is a unit and \(dt\) has no pole.

If \(t\) takes a root \(\alpha\) of \(p\), write
\(\operatorname{ord}(t-\alpha)=m>0\).
The root is simple, so (5) gives
\(m=2k\) and \(\operatorname{ord}q=k\) for an integer \(k\ge1\).
Differentiating the first nonzero local term in characteristic
zero gives
\[
\operatorname{ord}\omega=(2k-1)-k=k-1\ge0 .
\tag{7}
\]
There is no cancellation of that leading derivative.

Finally suppose \(t\) has a pole of order \(m\ge1\).
Since \(p\) has degree four and nonzero leading coefficient,
\(\operatorname{ord}p(t)=-4m\), hence
\(\operatorname{ord}q=-2m\).
The leading derivative has order \(-m-1\), so
\[
\operatorname{ord}\omega=(-m-1)-(-2m)=m-1\ge0 .
\tag{8}
\]
All points fall into one of these three cases. Thus \(\omega\)
has no pole anywhere on \(\mathbb P^1\).

For completeness, this is impossible by an elementary rational
differential calculation, without a genus formula. Write
\(\omega=R(s)\,ds\). If it has no finite pole, the denominator
of the reduced rational function \(R(s)\) has no complex root,
so \(R(s)\) is a polynomial. If it is nonzero of degree \(j\ge0\),
then in \(z=1/s\) the differential
\(-R(1/z)z^{-2}\,dz\) has order \(-j-2<0\) at infinity.
This contradicts (7)--(8). It proves the assertion following (3)
and hence excludes the squarefree case of (1).

Only rational functions in the actual ambient field were used.
In particular the squarefree obstruction itself does not require
a global slice, local nilpotence, or normality of the invariant
ring, once the nonconstant polynomial ratios in (3) are supplied.
Those stronger assumptions enter the present application through (1).

## 4. The exact repeated-root remainder and one integral coefficient

There is also a bounded consequence for the nonsquarefree
case of (1). Because \(F\) is irreducible, \(H_4\ne0\) and
\(H_4\) is not a square in \(\mathbb C[\mathsf X,\mathsf Y]\),
up to a nonzero complex scalar. Indeed a square would factor
\(\mathsf Z^2+H_4\) over \(\mathbb C\).

A nonzero binary quartic factors into four projective linear
factors counted with multiplicity. The multiplicity partitions
\(4\) and \(2+2\) are squares and hence impossible.
The partition \(1+1+1+1\) has just been excluded.
The only remaining possibilities are \(3+1\) and \(2+1+1\).
In either case one can write
\[
H_4=L_1^2Q_2,\qquad
Q_2\text{ a nonzero scalar times two distinct linear forms},
\qquad
c:=\frac{e}{L_1(a,b)},\qquad c^2+Q_2(a,b)=0 .
\tag{9}
\]
The denominator is nonzero by the full-kernel assumption.

Here \(c\) belongs to the actual invariant ring \(A\), not merely
its fraction field. The slice gives \(A\simeq B/(u)\).
The identity \(Eu=1\) expresses one as a polynomial combination
of the four partial derivatives of \(u\), so this hypersurface
is smooth. Thus \(A\) is normal. Equation (9) is a monic
polynomial equation over \(A\) for \(c\in\operatorname{Frac}A\);
normality implies \(c\in A\).

This is an integral coefficient restriction:
\(e=L_1(a,b)c\) and \(a,b,c\) satisfy the quadratic relation in (9).
It does not imply that \(c\) is a coordinate, that
\(L_1(X,Y)\) divides the actual polynomial \(Z\), or that
division by it is a polynomial automorphism.
Neither repeated-root type is excluded or recognized here.

## Scope and source boundary

The complete saved initial-bound157 was read for its exact
ordinary-coefficient convention and full-kernel hypotheses.
The bad-rank classification and any polynomial completion of
a general weight-four form are separate work. This note applies
only after the absent-\(W\) placement in (1) is justified.

The rational differential proof is written out and uses no
unproved rationality of an invariant surface, no Riemann--Hurwitz
formula, and no claim that a smooth double cover has a polynomial
parametrization. It does not address the rank-two product form
\(\mathsf Z\mathsf W+H_4\), other rank-one forms with a nonzero
\(\mathsf W\) coefficient, or rank-zero bad-quadratic forms.

No checker was executed, imported or compiled. No earlier
artifact, packet, or index was changed. This is a restricted
working proof, not human expert certification, formal verification,
historical novelty clearance, arbitrary coordinate entry, or
unrestricted complex-threefold cancellation.
