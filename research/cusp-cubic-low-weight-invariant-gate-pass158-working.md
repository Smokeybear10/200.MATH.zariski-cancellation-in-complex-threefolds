# A cusp-cubic invariant lift must use the fourth coordinate

**Status: working obstruction and conditional recognition gate.**

In an actual sliced E-time \((1,1,2,2)\) frame with full initial
kernel \((XZ-Y^3)\), a nonconstant invariant of source weight at
most three, if one exists, is an actual polynomial coordinate.
Consequently its kernel is a polynomial three-ring by the
regular-kernel theorem cited below.

The existence clause is essential. This note does not construct
an invariant lift of the initial relation or recognize every
cusp-cubic frame. Its elementary obstruction uses an integral
intercept and degree in an original coordinate, not an isolated
critical point.

## 1. An invariant suspension cannot have a moving affine first coordinate

Let \(B=\mathbb C[X,Y,Z,W]\), with the displayed generators actual
polynomial coordinates. Let \(E\) be a locally nilpotent derivation
such that
\[
a:=EX\ne0,\qquad E^2X=E^2Y=0,\qquad
P\in\mathbb C[T]\ \text{monic of degree }d\ge2 .
\tag{1}
\]
Then
\[
E\bigl(XZ-P(Y)\bigr)\ne0 .
\tag{2}
\]
There is no assumed bound on \(E^jZ\) or \(E^jW\), beyond local
nilpotence, and no global slice is required for this lemma.
A polynomial \(P\) with any nonzero constant leading coefficient
can be reduced to the monic case by a constant scaling of \(Z\).

Suppose otherwise, and write \(H=XZ-P(Y)\in A:=\ker E\),
\(b=EY\in A\), and \(K=\operatorname{Frac}A\).
Since \(a\in A\setminus\{0\}\), the derivation remains locally
nilpotent on \(B_a\), and \(t=X/a\) satisfies \(Et=1\).
For completeness, its finite Taylor projection and expansion are
\[
\begin{gathered}
\pi(f)=\sum_{j\ge0}\frac{(-t)^j}{j!}E^j f,\qquad
E\pi(f)=0,\qquad
f=\sum_{j\ge0}\frac{t^j}{j!}\pi(E^j f),\\
B_a=A_a[t]\subset K[t],\qquad
X=at,\qquad Y=y+bt,\qquad
y:=Y-\frac ba X\in A_a .
\end{gathered}
\tag{3}
\]
All sums are finite. Differentiating the first sum telescopes,
and substituting it in the second leaves only its zeroth term
by the binomial identity. Invariants of \(B_a\) are \(A_a\)
because the denominator \(a\) is invariant. The element \(t\)
is transcendental over \(K\): differentiating a monic relation
of least positive degree would give a relation of smaller
degree in characteristic zero.
Thus (3) is a polynomial expansion in a genuine indeterminate,
not an evaluation at a possibly missing point of \(\operatorname{Spec}B\).

The invariant \(H\) is constant as an element of \(K[t]\).
The expansion of \(Z\) belongs to \(K[t]\), so evaluating the
identity \(H=atZ-P(y+bt)\) at \(t=0\) gives
\[
H=-P(y).
\tag{4}
\]
Here \(y\in\operatorname{Frac}B\). Equation (4) makes \(y\)
integral over \(B\), since it satisfies the monic polynomial
\(P(T)+H\in B[T]\). The original polynomial ring is integrally
closed, hence \(y\in B\).

Now take degree in the original coordinate \(Z\), over the
domain \(\mathbb C[X,Y,W]\). If \(y\) is independent of \(Z\),
then \(P(y)\) has \(Z\)-degree zero, unlike \(H\). Otherwise
the leading term of \(P(y)\) cannot cancel with any lower
power of \(y\), so
\[
1=\deg_ZH=\deg_ZP(y)=d\,\deg_Zy,
\tag{5}
\]
which is impossible for \(d\ge2\).
This proves (2). Neither normality of a generic fiber nor
regularity of a rational coefficient model is being used:
normality is applied to \(B\) itself.

## 2. Exact normalization of a cusp lift with no fourth-coordinate term

Suppose \(E\) is locally nilpotent on the same actual four-ring,
\(EX\ne0\), and \(E^2X=E^2Y=0\).
For constants \(\lambda\ne0,\alpha\in\mathbb C\) and
\(Q\in\mathbb C[X,Y]\) of ordinary degree at most two, put
\[
H=\lambda(XZ-Y^3)+\alpha Z+Q(X,Y).
\tag{6}
\]
Then \(EH\ne0\).

Indeed set \(x=X+\alpha/\lambda\), retaining \(Y,Z,W\).
Write
\[
\begin{gathered}
\widetilde Q(x,Y)
 :=\lambda^{-1}Q(x-\alpha/\lambda,Y)
 =xL(x,Y)+q(Y),\\
\deg L\le1,\qquad \deg q\le2,\qquad
z=Z+L(x,Y),\qquad P(Y)=Y^3-q(Y),\\
H/\lambda=xz-P(Y).
\end{gathered}
\tag{7}
\]
This is polynomial division by the formal variable \(x\):
\(q(Y)=\widetilde Q(0,Y)\), and
\(\widetilde Q-q\) is divisible by \(x\) as a polynomial.
There is no localization at \(x\).
The complete actual inverse is
\(X=x-\alpha/\lambda\), \(Z=z-L(x,Y)\), with \(Y,W\)
unchanged, and substitution checks both inverse orders.
The polynomial \(P\) is monic of degree three.
Also \(Ex=EX\ne0\), \(E^2x=E^2Y=0\), so the lemma applies
in the actual coordinate system \((x,Y,z,W)\).

In the quadratic-time application this shear even preserves
the second acceleration of \(Z\), since \(L\) is affine in
the two good coordinates. The lemma itself does not need
that additional property.

## 3. The full initial-kernel hypothesis gives a conditional coordinate

Now assume the retained actual157 profile and its normalized
cusp initial ideal:[^1]
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\theta:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\eta,b\eta,e\eta^2,h\eta^2),\qquad
\ker\theta=(\mathsf X\mathsf Z-\mathsf Y^3).
\end{gathered}
\tag{8}
\]
The source of \(\theta\) is the formal complex polynomial
four-ring with weights \((1,1,2,2)\); \(\eta\) is independent
over \(A\), and \(a,b,e,h\) are the ordinary leading
coefficients. In particular \(a=EX\ne0\).
The ideal in (8) is the full initial kernel, not merely
one relation among the four leading coefficients.

Let \(H\in A\setminus\mathbb C\) have source weighted degree
at most three. Its top weighted polynomial lies in
\(\ker\theta\), because its positive top \(u\)-coefficient
vanishes. The generator in (8) has weight three, so the
top must be a nonzero complex scalar multiple of that
generator. Consequently
\[
H=\lambda(XZ-Y^3)+\alpha Z+\beta W+Q(X,Y),
\qquad
\lambda\in\mathbb C^*,\quad
\alpha,\beta\in\mathbb C,\quad \deg Q\le2 .
\tag{9}
\]
If \(\beta=0\), Section 2 contradicts \(EH=0\).
Therefore \(\beta\ne0\). Replacing \(W\) by \(I=H\)
is an actual polynomial coordinate change: its inverse is
\[
W=\beta^{-1}
 \{I-\lambda(XZ-Y^3)-\alpha Z-Q(X,Y)\}.
\]
The constants are the only denominators, and this displayed
substitution verifies both inverse orders.
Thus \(B=\mathbb C[I,X,Y,Z]\) with \(EI=0\).

The global slice makes \(A\) regular. Indeed \(A\simeq B/(u)\),
and \(Eu=1\) expresses \(1\) as a polynomial combination of
the four partial derivatives of \(u\). The hypersurface \(u=0\)
is smooth over \(\mathbb C\).
Apply Bhatwadekar--Gupta--Lokhande Theorem 3.5 to the nonzero
\(\mathbb C[I]\)-linear LND on \(B=\mathbb C[I]^{[3]}\);
its regular kernel is \(\mathbb C[I]^{[2]}\).[^2]
This recognizes \(A\) under the stated existence hypothesis.
Alternatively the actual coordinates \(I,X,Y\) are three
goods, supplying the retained recognition156 hypotheses.[^3]

## 4. What the critical locus does not prove

For \(H=xz-P(Y)\), the critical equations are
\(x=z=0\) and \(P'(Y)=0\), with \(W\) free.
Thus the reduced critical set is a finite union of lines,
not an isolated point. A derivation with a global slice
could translate these lines: \(\partial_W\) fixes \(H\)
and has slice \(W\).
There is no contradiction from the critical locus alone.
This example has \(EX=0\), so it does not meet (1).

The degree restriction on \(P\) also matters. For \(P(Y)=Y\),
the triangular LND \(\partial_X+Z\partial_Y\) fixes
\(XZ-Y\), has slice \(X\), and satisfies \(E^2X=E^2Y=0\).
It is excluded precisely by \(d\ge2\).

The present result does not force a nonconstant element in
the invariant space of weight at most three. If that space
contains only constants, the cusp frame remains outside
this conditional gate. Higher-weight invariants, the
split-cubic correction problem, weight-four initial
relations, smaller initial rank, and arbitrary coordinate
entry are not settled here.

## Sources and scope

1. [The actual cubic normal forms157](two-linear-cubic-normal-forms-pass157-working.md),
   Section 3, and
   [the two-linear/two-quadratic initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md).
   These supply the normalized actual coordinates and the
   full initial ideal used only in Section 3.
2. S. M. Bhatwadekar, N. Gupta and S. A. Lokhande,
   [Some K-theoretic properties of the kernel of a locally nilpotent derivation
   on \(k[X_1,\ldots,X_4]\)](https://arxiv.org/html/1501.01438v1),
   Theorem 3.5. Its exact statement and displayed short proof
   were freshly inspected for the regular invariant-coordinate
   endpoint. No recursive audit of its cited inputs is claimed.
3. [All-degree three-good recognition156](three-good-all-degree-recognition-pass156-working.md),
   retained as an alternative working endpoint, not needed
   for the direct Theorem 3.5 application.

The finite local-slice expansion, integral-intercept argument,
normalization and degree contradiction are proved above.
They are not claimed as historically new. This is a private
working proof, not human expert review, proof-assistant
certification or a conclusion from finite controls.
No157 or earlier artifact is changed.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
