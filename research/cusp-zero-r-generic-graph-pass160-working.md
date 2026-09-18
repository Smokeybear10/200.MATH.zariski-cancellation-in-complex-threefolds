# The zero-r cusp branch has an affine generic parameter

**Status: working generic reduction, not integral recognition.**

In the actual cusp chart159, the branch \(k_\rho=0\) has no
nongraph generic embedding left. If \(n_\rho\ne0\), the next
determinant coefficient forces \(y\) to be an affine parameter.
If \(n_\rho=0\), the earlier argument instead makes \(w\) an
affine parameter. Both conclusions are over the exact coefficient
field \(L\). Neither constructs a global polynomial slice.

## 1. Retained actual chart

Retain all hypotheses and constructions of
[the actual chart159](cusp-generic-chart-first-reductions-pass159-working.md),
including its actual polynomial four-frame, sliced derivation,
full cusp initial kernel, finite separable field
\(L/\mathbb C(\tau,\rho)\), commuting coefficient derivatives,
and \(L[y,z,w]=L[v]\) with \(\partial_v=N\).
Work only in the branch \(k_\rho=0\). The chart gives
\[
\begin{gathered}
Y=y+\tau X,\qquad
Z=z+\sigma X+\tau^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
\sigma=3\tau^2y+k,\qquad
z=3\tau y^2+k_\tau y+n,\\
y^3+\tfrac12 k_{\tau\tau}y^2+n_\tau y+n_\rho\vartheta=\ell,\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}
       =-a^3\in L^* .
\end{gathered}
\tag{1}
\]
Here \(a=EX\ne0\) is an element of \(L\). All coefficient
derivatives fix the independent formal variable used below.
The whole-line equality and constant determinant in (1) come
from the actual chart, not from a chosen formal ansatz.

## 2. The missing coefficient when s is nonzero

Put \(s=n_\rho\) and assume \(s\ne0\). For a formal variable
\(U\), define
\[
P(U)=\frac{\ell-U^3-\tfrac12 k_{\tau\tau}U^2-n_\tau U}{s},
\qquad
B(U)=3U^2+k_{\tau\tau}U+n_\tau=-sP_U(U).
\tag{2}
\]
Then \(\vartheta=P(y)\). Also \(z\in L[y]\), so (1) implies
\(L[y,w]=L[v]\).

The determinant-preserving row subtraction from chart159 gives,
with \(X\) fixed and all differentials over \(\mathbb C\),
\[
dY=dy+X\,d\tau,\qquad
dZ_{\rm red}=B(y)\,d\tau+s\,d\rho,\qquad
dW=dw+X\,d\vartheta+X^2\,d\rho .
\tag{3}
\]
The coefficient of \(X\) in their wedge is
\[
\begin{aligned}
&dy\wedge(B\,d\tau+s\,d\rho)\wedge d\vartheta
       +s\,d\tau\wedge d\rho\wedge dw\\
&\quad=
d\tau\wedge d\rho\wedge
\bigl(s\,dw+(B P_\rho-sP_\tau)(y)\,dy\bigr).
\end{aligned}
\]
Indeed \(d\vartheta=P_U(y)\,dy+P_\tau(y)\,d\tau
+P_\rho(y)\,d\rho\), and the term containing \(P_Udy\)
vanishes in the first wedge. Taking scalar coefficients gives
\[
0=[X]J
=s\left[w_v-
 \bigl(P_\tau+P_U P_\rho\bigr)(y)y_v\right].
\tag{4}
\]
This step does not divide by \(y_v\).

Choose the unique polynomial \(Q\in L[U]\) with \(Q(0)=0\)
and
\[
Q_U=P_\tau+P_U P_\rho,\qquad \deg Q\le6.
\tag{5}
\]
It exists by termwise integration in the formal variable \(U\)
in characteristic zero. No antiderivative in the coefficient
field with respect to \(\tau\) or \(\rho\) is required.
Equations (4)--(5) say
\(\partial_v(w-Q(y))=0\), hence \(w=Q(y)+h\) for \(h\in L\).
Consequently
\[
L[v]=L[y,w]=L[y],\qquad
y=\alpha v+\gamma,\quad \alpha\in L^*,\quad\gamma\in L.
\tag{6}
\]
For the final assertion, express \(v\) as a polynomial in \(y\).
Neither is constant, and multiplication of polynomial degrees
forces \(\deg_v y=1\). This uses the whole affine line in (1),
not merely a birational parametrization.

## 3. The constant coefficient remains a constraint

Write \(R(U)=Q(U)+h\). The constant coefficient in (3) is
\[
J(0)=
-s\,\bigl(R_\tau+P_U R_\rho\bigr)(y)y_v=-a^3.
\]
Since \(y\) is affine, evaluation \(L[U]\to L[v]\) is injective.
Thus the actual chart also satisfies the polynomial identity
\[
R_U=P_\tau+P_U P_\rho,\qquad
R_\tau+P_U R_\rho=\frac{a^3}{s\alpha}\in L^* .
\tag{7}
\]
These equations are necessary. Arbitrary choices of \(P,R\)
satisfying them have not been shown to arise from an actual
global frame.

One further necessary restriction follows without solving (7).
Let \(A_3=-1/s\), the leading coefficient of \(P\). The
coefficient of \(U^6\) in \(R\) is \(A_3(A_3)_\rho/2\),
because \(P_\tau\) has degree at most three. The coefficient
of \(U^8\) in the second equation of (7) is therefore
\[
\frac32 A_3\bigl((A_3)_\rho^2+
                   A_3(A_3)_{\rho\rho}\bigr)=0,\qquad
\partial_\rho^2(A_3^2)=0 .
\tag{8}
\]
This conclusion also covers vanishing leading coefficients
of \(R\); they are treated as zero, not as a claimed exact
degree six. If \(L_0=\ker_L\partial_\rho\), equation (8)
implies \(A_3^2=c_1\rho+c_0\) with \(c_0,c_1\in L_0\):
take \(c_1=\partial_\rho(A_3^2)\) and
\(c_0=A_3^2-c_1\rho\). This does not assert that these
constants are complex numbers.

## 4. The s-zero branch and an actual nonzero-s boundary

If \(s=n_\rho=0\), the monic cubic in (1) makes \(y\in L\).
Then \(z,\sigma\in L\). Chart159, Section 6, factors the
determinant as a polynomial in \(X\) to show
\(\vartheta\in L\) and \(w_v\in L^*\).
Thus this other branch also has an affine generic parameter,
but it is \(w\), not \(y\).

The branch \(s\ne0\) is not empty. In the polynomial ring
\(\mathbb C[x,t,p,v]\), take \(E=\partial_x\) and define
\[
\begin{gathered}
X=x,\qquad Y=v+tx,\\
Z=p+3tv^2+3t^2vx+t^3x^2,\qquad
W=t-v^3x+px^2,\qquad H=XZ-Y^3 .
\end{gathered}
\tag{9}
\]
These are actual polynomial coordinates. A polynomial inverse is
\[
t=W-XH,\qquad v=Y-Xt,\qquad
p=Z-3tv^2-3t^2vX-t^3X^2,\qquad x=X .
\tag{10}
\]
For the forward substitution, \(H=px-v^3\), so (10)
recovers \(t,v,p,x\). For the reverse substitution,
\(Y=v+tX\) and the defining formula for \(p\) first give
\(H=pX-v^3\); then \(t=W-XH\) recovers the displayed \(W\).
This proves both compositions, not just a nonzero Jacobian.

The time degrees are exactly \((1,1,2,2)\), with leading
tuple \((1,t,t^3,p)\). The initial map has full kernel
\((\mathsf X\mathsf Z-\mathsf Y^3)\): this irreducible
relation vanishes and the initials
\(\eta,t\eta,p\eta^2\) are algebraically independent.
The chart has \(a=1,\tau=t,\rho=p,y=v,k=0,n=\rho,\ell=0\),
\(\vartheta=-v^3,w=\tau\). In particular \(r=0,s=1\),
\(P=-U^3\), \(Q=0\), \(h=\tau\), \(J=-1\).
The actual selected partial has
\(\partial_Zt=-X^2,\partial_Zv=X^3\), calibrating \(Nv=1\).
The example already has the coordinate slice \(X\). It is
neither a cancellation counterexample nor evidence of
minimality of its displayed time degrees.

## Scope

All divisions take place over the exact \(L\) with the
specified nonzero \(s\). The polynomial primitive and affine
parameter do not clear denominators in \(A\), identify
\(\ker_A N\) with a polynomial plane, or provide the
low-weight invariant required by the recognition gate158.
Full cancellation and arbitrary coordinate entry remain open.
No novelty clearance, human expert review or formal proof
certification is claimed. The exact identities and actual
boundary can be checked finitely; their universal conclusions
depend on the written argument.
