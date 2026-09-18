# A low-weight cusp invariant forces a nonzero constant parameter

**Status: working necessary condition and actual boundary.**

In the fixed actual cusp chart159, a nonconstant invariant of
original coordinate weight at most three can exist only if
\(r=k_\rho\) is a nonzero complex constant. In particular,
the zero-\(r\) and nonconstant-\(r\) branches cannot be
recognized by uniformly asserting the existence of such an
invariant. The actual zero-\(r\) example160 has minimum
nonconstant invariant weight exactly four in its displayed frame.

This is a restriction on one proposed invariant-lift strategy,
not an obstruction to recognition by other coordinate changes.
No sufficiency statement for constant \(r\) is asserted.

## 1. Fixed actual hypotheses and the meaning of weight

Assume all actual hypotheses of chart159:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad d=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\eta,b\eta,e\eta^2,d\eta^2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z-\mathsf Y^3).
\end{gathered}
\tag{1}
\]
Here the four displayed generators are actual polynomial
coordinates, and the ideal in (1) is the full initial kernel.
The source of \(\theta_0\) has weights \((1,1,2,2)\),
with \(\eta\) independent over \(A\).

For an element of \(B\), its *original coordinate weight*
means the weighted degree of its unique polynomial expression
in \(X,Y,Z,W\), using those weights. This is not its
\(E\)-degree: every invariant has \(E\)-degree zero,
but can have arbitrarily large original coordinate weight.
Nor is this a minimum over changes of the displayed frame.

Set \(F=XZ-Y^3\). The actual localization and coefficient
recurrences159 give a field \(L\), algebraically independent
\(\tau=b/a,\rho=d/a^2\), and
\[
\begin{gathered}
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
A_L=L[v],\qquad B_a=A_a[X],\qquad E=a\partial_X,\\
Y=y+\tau X,\qquad
Z=z+\sigma X+\tau^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
\sigma=3\tau^2y+k,\qquad
z=3\tau y^2+k_\tau y+k_\rho\vartheta+n,
\qquad k,n\in L,\\
F=-y^3+(k_\tau y+k_\rho\vartheta+n)X+kX^2,
\qquad r:=k_\rho .
\end{gathered}
\tag{2}
\]
The variable \(X\) is a genuine polynomial variable over
\(A_a\), and hence over \(L[v]\). All its displayed
coefficients are invariant under \(E\).
The coefficient derivative \(\partial_\rho\) on \(L\)
is the unique extension of that on \(\mathbb C(\tau,\rho)\);
it fixes \(\tau\) and the complex constants.
Only the early chart identities (2) are used below.
The later nongraph exclusion161 is not an input.

## 2. The possible low-weight invariant and the nonzero fourth-coordinate term

Suppose \(I\in A\setminus\mathbb C\) has original
coordinate weight at most three. Its top weighted polynomial
is nonzero and lies in \(\ker\theta_0\): its highest positive
\(u\)-coefficient must vanish because \(EI=0\).
The generator in (1) has weight three, so the weight of
\(I\) is exactly three and its top is \(\lambda F\)
for \(\lambda\in\mathbb C^*\). All remaining monomials
have weight at most two. Consequently
\[
I=\lambda F+\alpha Z+\beta W+Q(X,Y),\qquad
\lambda\in\mathbb C^*,\quad \alpha,\beta\in\mathbb C,
\quad Q\in\mathbb C[X,Y],\quad\deg Q\le2,
\qquad \beta\ne0.
\tag{3}
\]

The last assertion is the precise retained invariant-exclusion
gate158, not a consequence of the initial relation alone.
Here is its application. If \(\beta=0\), translate
\(x=X+\alpha/\lambda\) and divide
\(\lambda^{-1}Q(x-\alpha/\lambda,Y)\) by \(x\):
it equals \(xL_1(x,Y)+q(Y)\), with \(L_1\) affine and
\(\deg q\le2\). The actual polynomial shear
\(z=Z+L_1(x,Y)\) then gives
\(I/\lambda=xz-P(Y)\), where \(P(Y)=Y^3-q(Y)\)
is monic of degree three. Its inverse is
\(X=x-\alpha/\lambda\), \(Z=z-L_1(x,Y)\), with
\(Y,W\) unchanged.

One still has \(Ex=a\ne0\) and \(E^2x=E^2Y=0\).
Section 1 of158 excludes an invariant \(xz-P(Y)\) under
exactly these hypotheses. Its finite local-slice expansion
makes the intercept \(Y-(EY/Ex)x\) integral over the
normal original ring, and then original \(z\)-degree
would satisfy \(1=3\deg_z(Y-(EY/Ex)x)\).
Thus \(\beta\ne0\). No recognition theorem or global
descent conclusion from158 is needed here.

## 3. The quadratic time coefficient forces r to be constant

Let \(Q_2\) be the homogeneous quadratic part of \(Q\),
possibly zero. Substitute the actual identities (2) into (3).
Since \(E=a\partial_X\) and \(a\ne0\), invariance
makes every positive \(X\)-coefficient vanish. In particular,
\[
0=[X^2]I=\lambda k+\alpha\tau^3+\beta\rho+Q_2(1,\tau),
\qquad
k=-\frac\alpha\lambda\tau^3
  -\frac\beta\lambda\rho
  -\frac{Q_2(1,\tau)}\lambda .
\tag{4}
\]
The term \(Q_2(1,\tau)\) is correct even when the
projected intercept \(y\) is nonconstant: replacing
\(Y\) by \(y+\tau X\) contributes to \(X^2\)
only through the homogeneous quadratic part.
All terms in (4) belong to the coefficient field \(L\),
not merely its polynomial extension by \(v\).

Apply \(\partial_\rho\) to (4). It gives
\[
\lambda r+\beta=0,\qquad
r=-\beta/\lambda\in\mathbb C^* .
\tag{5}
\]
This holds over the exact finite algebraic field \(L\);
there is no rationality assumption on its other elements.
It uses the nonzero \(\beta\) proved in Section 2.
Equation (5) is necessary, not sufficient: the lower
\(X\)-coefficients of \(I\) impose further conditions.

## 4. An actual zero-r frame has minimum invariant weight four

Take the retained160 frame in the polynomial ring
\(\mathbb C[x,t,p,v]\), with \(E=\partial_x\):
\[
\begin{gathered}
X=x,\qquad Y=v+tx,\\
Z=p+3tv^2+3t^2vx+t^3x^2,\qquad
W=t-v^3x+px^2,\qquad F=XZ-Y^3=px-v^3,\\
t=W-XF,\qquad v=Y-Xt,\qquad
p=Z-3tv^2-3t^2vX-t^3X^2,\qquad x=X.
\end{gathered}
\tag{6}
\]
The last line is a polynomial inverse. In the forward order,
\(F=px-v^3\) directly recovers \(t,v,p,x\).
In the reverse order the formulas for \(v,p\) give
\(Y=v+tX\), \(F=pX-v^3\); then \(t=W-XF\)
recovers the stated \(W\). Both compositions are the
identity, including at \(X=0\).

The exact \(E\)-degrees are \((1,1,2,2)\), with
ordinary leading coefficients \((1,t,t^3,p)\).
The initials \(\eta,t\eta,p\eta^2\) are algebraically
independent: their fraction field contains \(\eta,t,p\).
Thus the initial image has transcendence degree three.
The irreducible relation \(\mathsf X\mathsf Z-\mathsf Y^3\)
vanishes and generates the full height-one initial kernel.
Irreducibility follows by regarding it as a primitive linear
polynomial in \(\mathsf Z\) over
\(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\).
The chart parameters are \(\tau=t,\rho=p,y=v,k=0,n=\rho\),
so \(r=0\), as in160.

For a direct lower-weight check, write any possible invariant
of weight at most three in the polynomial form of (3),
without using \(\beta\ne0\), and set
\(Q=q_{20}X^2+q_{11}XY+q_{02}Y^2+q_{10}X+q_{01}Y+q_{00}\).
Substitution of (6) gives
\[
\begin{aligned}
[x^2]I&=\alpha t^3+\beta p+q_{20}+q_{11}t+q_{02}t^2,\\
[x]I&=\lambda p+q_{10}+q_{01}t
\quad\text{after the first coefficient has vanished}.
\end{aligned}
\tag{7}
\]
Since \(t,p\) are independent, the first identity forces
\(\alpha=\beta=q_{20}=q_{11}=q_{02}=0\).
The second then forces \(\lambda=q_{10}=q_{01}=0\).
Only \(q_{00}\) remains. This proves directly that there
is no nonconstant invariant of weight at most three.

On the other hand \(t=W-X(XZ-Y^3)\) is a nonconstant
invariant and has exact original coordinate weight four:
its top weighted polynomial is
\(-\mathsf X(\mathsf X\mathsf Z-\mathsf Y^3)\ne0\).
There is no cancellation of this polynomial with the
weight-two term \(W\). Therefore, for this fixed frame,
\[
\min\{\operatorname{wt}_{(1,1,2,2)} I:
 I\in\ker E\setminus\mathbb C\}=4.
\tag{8}
\]
The initial evaluation of that nonzero top polynomial does
vanish, as it must for an invariant. Original polynomial
weight and evaluated \(E\)-degree are different notions.

## Scope and retained sources

The condition \(r\in\mathbb C^*\) concerns the normalized
fixed frame and selected coefficient chart in (1)--(2).
It is not asserted invariant under arbitrary changes of the
four original coordinates. No low-weight invariant is produced
when \(r\) is constant. The example has the original coordinate
slice \(X=x\), and \(\ker E=\mathbb C[t,p,v]\) is already
polynomial. Equation (8) is not a minimum of the displayed
time profile over all coordinate frames and not a cancellation
counterexample.

The zero-\(r\) and nonconstant-\(r\) branches therefore need
something other than a uniform invariant of original weight
at most three. Higher-weight invariants, suitable actual
shears, and other recognition arguments are not excluded.

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 1--3, for the precise actual hypotheses and (2).
2. [Cusp invariant gate158](cusp-cubic-low-weight-invariant-gate-pass158-working.md),
   Sections 1--3, for the full initial-kernel form and the
   necessary nonzero fourth-coordinate coefficient.
3. [Zero-r generic reduction160](cusp-zero-r-generic-graph-pass160-working.md),
   Section 4, for the actual boundary repeated in (6).

These are retained working inputs, not a recursive audit of
all external dependencies. The coefficient comparison and
both inverse orders are explicit above. No novelty clearance,
human expert review, proof-assistant certification, or full
cancellation result is claimed. No161 or earlier source is changed.
