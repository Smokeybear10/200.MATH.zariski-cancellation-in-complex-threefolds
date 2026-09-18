# A square-root coefficient field occurs in an actual zero-r cusp frame

**Status: complete working boundary and necessary-condition argument.**

The condition \(s_\rho=0\) does not follow from actualness in the
zero-r cusp branch. The polynomial frame below has a global slice,
the full cusp initial kernel, and \(s_\rho\ne0\). Its coefficient
field is genuinely quadratic over the ratio field. Its invariant
ring is nevertheless already a polynomial three-ring, and an
invariant coordinate has an explicit polynomial expression.

The general determinant restriction from160 also has an exact
interpretation: rho is a polynomial of degree at most two in \(n\)
over \(K=\ker_L\partial_\rho\). This statement does not identify
the entire coefficient field with \(K(n)\).

## 1. The retained zero-r condition

Retain the actual chart and field hypotheses of
[cusp reductions159](cusp-generic-chart-first-reductions-pass159-working.md)
and the branch \(r=k_\rho=0\), \(s=n_\rho\ne0\) of
[the zero-r reduction160](cusp-zero-r-generic-graph-pass160-working.md).
Write \(t=\tau\). In particular, \(L/\mathbb C(t,\rho)\) is
finite and separable, its coefficient partials commute, and the
actual projected ring is \(L[v]\). The retained conclusion gives
\[
\begin{gathered}
\vartheta=P(y),\qquad w=R(y),\qquad L[y]=L[v],\\
P(U)=\frac{\ell-U^3-k_{tt}U^2/2-n_tU}{s},\\
R_U=P_t+P_UP_\rho,\qquad
R_t+P_UR_\rho\in L^*,\qquad
\partial_\rho^2(1/s^2)=0 .
\end{gathered}
\tag{1}
\]
All coefficient derivatives in (1) fix the formal variable \(U\).
The last identity follows from the highest coefficient in the
second polynomial identity, not from a rationality assumption on
\(L\). We use that proved identity, not a classification of all
solutions of (1).

## 2. The exact quadratic relation in the general branch

Set \(K=\ker_L\partial_\rho\), \(q=1/s\), and define the
derivation \(D_n=q\partial_\rho\) on \(L\). Then \(D_n n=1\)
and \(\ker D_n=K\). Direct differentiation gives
\[
D_n^2q
 =q\bigl(q_\rho^2+q q_{\rho\rho}\bigr)
 =\frac q2\partial_\rho^2(q^2)=0 .
\tag{2}
\]
Thus \(A:=D_nq\in K\), and \(B:=q-An\in K\).
Since \(D_n\rho=q\), another primitive subtraction gives
\[
q=An+B,\qquad
\rho=\frac A2n^2+Bn+C,\qquad A,B,C\in K .
\tag{3}
\]
No antiderivative has been adjoined. Each constant in (3) is
defined by subtraction inside the original \(L\).

Here \(A=q q_\rho=-s_\rho/s^3\). Consequently \(A=0\) is
exactly the subcase \(s_\rho=0\); then \(B=q\ne0\) and the
relation is linear. If \(A\ne0\), the relation is genuinely
quadratic. Rho is transcendental over \(K\), since a derivation
killing \(K\) cannot take the value one on a separable algebraic
element over \(K\). The discriminant
\(B^2-2A(C-\rho)\) has order one at its linear prime in
\(K[\rho]\), and is not a square in \(K(\rho)\). Hence
\([K(n):K(\rho)]=2\) in this case. There can still be a further
extension from \(K(n)\) to \(L\); (3) does not rule it out.

## 3. An actual polynomial frame

Fix \(c\in\mathbb C^*\). In the polynomial ring
\(B=\mathbb C[x,t,n,y]\), take \(E=\partial_x\) and define
\[
\begin{gathered}
X=x,\qquad Y=y+tx,\\
Z=n+3ty^2+3t^2yx+t^3x^2,\\
H=XZ-Y^3=nx-y^3,\qquad W=t+cH^2 .
\end{gathered}
\tag{4}
\]
These are polynomial coordinates, not merely algebraically
independent functions. For independent target variables
\(X,Y,Z,W\), put \(H=XZ-Y^3\) and define
\[
\begin{gathered}
x=X,\qquad t=W-cH^2,\qquad y=Y-tX,\\
n=Z-3ty^2-3t^2yX-t^3X^2 .
\end{gathered}
\tag{5}
\]
Forward substitution of (4) into (5) recovers \(x,t,y,n\),
using \(H=nx-y^3\). Conversely, start with the target variables
and define the source variables by (5). The definitions of
\(y\) and \(n\) give
\[
nX-y^3
 =XZ-3ty^2X-3t^2yX^2-t^3X^3-y^3
 =XZ-(y+tX)^3=H.
\]
Thus the forward formula for \(W\) gives
\(t+c(nX-y^3)^2=W\); the other three formulas recover
\(X,Y,Z\) directly. This proves both compositions.

In particular \(E\) is a globally sliced locally nilpotent
derivation, with \(EX=1\), and
\(\ker E=\mathbb C[t,n,y]\). The expression \(t=W-cH^2\)
is an actual coordinate of \(B\), as certified by (5), not just
an invariant polynomial or a generic coordinate.

## 4. Exact time degrees and the full initial kernel

Expansion of (4) gives
\[
\begin{gathered}
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
(a,b,e,d)=(1,t,t^3,cn^2),\qquad
\tau=t,\quad\rho=cn^2 .
\end{gathered}
\tag{6}
\]
These are ordinary leading coefficients; the quadratic entries
are \(E^2Z/2\) and \(E^2W/2\). None of the displayed leading
coefficients is the zero polynomial.

For an independent variable \(\eta\), the weighted initial map is
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(\eta,t\eta,t^3\eta^2,cn^2\eta^2),\qquad
\ker\theta=(\mathsf X\mathsf Z-\mathsf Y^3).
\tag{7}
\]
Indeed the stated irreducible polynomial vanishes. The three
initials \(\eta,t\eta,cn^2\eta^2\) are algebraically independent:
their fraction field contains \(\eta,t,n^2\), which are
algebraically independent. The image therefore has transcendence
degree three, so the prime kernel has height one and equals the
displayed principal prime. This verifies the full initial-kernel
premise, not just one leading relation.

## 5. The selected derivation and its exact coefficient field

Let \(T=\partial_Z\) in the actual target frame, holding
\(X,Y,W\) fixed. Differentiating the inverse (5), so that
\(TH=X\), gives
\[
Tx=0,\qquad
Tt=-2cHX,\qquad
Ty=2cHX^2,\qquad
Tn=1+6cHy^2X .
\tag{8}
\]
For the last formula, substitute the first two differentiated
entries into the derivative of the expression for \(n\) in
(5). The terms of degrees three in \(X\) cancel.
Now \(X=x\), \(H=nx-y^3\), and \(A=\ker E=\mathbb C[t,n,y]\).
The intrinsic cubic coefficient is therefore
\[
N=[x^3](T|_A)=2cn\,\partial_y,\qquad
S=\ker_A N=\mathbb C[t,n],\qquad
L=\operatorname{Frac}S=\mathbb C(t,n).
\tag{9}
\]
The coefficient \(2cn\) is nonzero, so the kernel assertion
follows directly in the domain \(A\). Its primitive derivation
is \(\partial_y\), which already has a global slice.

The ratio field is \(\mathbb C(t,cn^2)\). The element
\(\rho/c\) is not a square in \(\mathbb C(t,\rho)\), as its
rho valuation is odd. Thus the exact coefficient field in (9)
has degree two over that ratio field. The normalized parameter
\(v=y/(2cn)\) satisfies \(Nv=1\) and \(A_L=L[v]\).
These statements do not identify the ratio field with \(L\).

## 6. The zero-r chart and determinant normalization

The actual entries, written as polynomials in \(X\), are
\[
\begin{gathered}
Y=y+tX,\qquad
Z=z+3t^2yX+t^3X^2,\qquad z=n+3ty^2,\\
W=w+\vartheta X+\rho X^2,\qquad
w=t+cy^6,\quad\vartheta=-2cny^3,\quad\rho=cn^2,\\
k=0,\quad r=0,\quad\ell=0,\qquad
s=n_\rho=\frac1{2cn},\quad
s_\rho=-\frac1{4c^2n^3}\ne0 .
\end{gathered}
\tag{10}
\]
The coefficient derivatives here fix \(t\), or fix rho,
as prescribed by the finite separable extension. In particular
\(\partial_\rho=(2cn)^{-1}\partial_n\) on \(L\), and
\(K=\ker_L\partial_\rho=\mathbb C(t)\).

The exact polynomials in (1) are
\[
P(U)=-2cnU^3,\qquad R(U)=t+cU^6,\qquad
P_t=0,\quad P_\rho=-U^3/n,\qquad
R_U=P_UP_\rho=6cU^5,\quad R_t+P_UR_\rho=1 .
\tag{11}
\]
Also \(y^3+s\vartheta=0\), as required by the second-tail
coefficient. Here \(q=1/s=2cn\), so the general form (3)
has \(A=2c\), \(B=C=0\). Its genuinely quadratic case
therefore occurs in an actual polynomial frame.

The determinant normalization can be checked without inferring
it from the mere existence of an inverse. At fixed \(X\),
the rows of the Jacobian with respect to \((t,n,y)\) are
\[
\begin{pmatrix}
X&0&1\\
3(y+tX)^2&1&6ty+3t^2X\\
1&2cHX&-6cHy^2
\end{pmatrix}.
\]
Its determinant is
\(-1+2cHX\{3(y+tX)^2-3y^2-X(6ty+3t^2X)\}=-1\).
Furthermore
\(\det\partial(t,\rho,v)/\partial(t,n,y)=1\), because
\(\rho=cn^2\) and \(v=y/(2cn)\). Consequently
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-1=-a^3 .
\tag{12}
\]
All these calculations take place over the exact field \(L\)
where the normalized parameter is defined.

## Scope

The example disproves a universal claim that actualness forces
\(s_\rho=0\) in the nonzero-s, zero-r branch. It also prevents
replacing the exact coefficient field by the ratio field in that
branch. The general statement (3) is a necessary normal form,
not a solution of all remaining determinant equations.

The example has the actual slice \(X\) and the invariant
coordinate \(t\). It is not a counterexample to cancellation,
to polynomial invariant-ring recognition, or to any statement
requiring a globally minimal time profile. It does not establish
that every zero-r frame has a comparable polynomial inverse or
an integral good-coordinate correction. No historical novelty,
human expert verification, or formal proof certification is
claimed. Earlier sources and their canonical executions are
unchanged.
