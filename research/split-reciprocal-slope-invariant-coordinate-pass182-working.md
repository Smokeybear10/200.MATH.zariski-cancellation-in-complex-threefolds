# An actual invariant coordinate in the reciprocal split-slope branch

**Status: conditional working recognition for all nonlinear graph degrees.**

Under the normalized nonlinear split chart178, assume the nonzero
coefficient slope has the reciprocal form
\(m_\rho=d^2/(t+\nu)\), with \(\nu\in\mathbb C\).
An explicit original-ring coordinate is invariant. Thus the regular-kernel
theorem of Bhatwadekar--Gupta--Lokhande gives
\(A\simeq\mathbb C^{[3]}\) in this branch.

The reciprocal-form premise is separate from this construction. No
argument here assumes that the determinant is a rational cube, that
\(Ny=1\), or that a generic coordinate automatically descends.

## 1. Actual hypotheses and the reciprocal normalization

Retain the actual assumptions and equations of
[the nonlinear coefficient note178](split-affine-graph-coefficient-normal-form-pass178-working.md).
In particular,
\[
\begin{gathered}
B=A[u]=\mathbb C[X,Y,Z,W],\qquad E=\partial_u,\qquad Eu=1,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\\
a=EX,\quad N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}(\ker_A N),\quad K=\ker_L\partial_\rho,\\
[K:\mathbb C(t)]<\infty,\qquad \ker_K\partial_t=\mathbb C,\qquad
L=K(\rho),\\
y=\gamma v+\eta,\quad \gamma=Ny\in L^*,\qquad
\vartheta=P(y),\quad 2\le\deg P\le4,\\
r=0,\quad k,n_0,\ell\in K,\quad n=d\rho+n_0,\quad d\in\mathbb C^*,\\
m=A_1\rho+B_0,\qquad A_1=\frac{d^2}{t+\nu},\quad
B_0\in K,\quad \nu\in\mathbb C .
\end{gathered}
\tag{1}
\]
All coefficient derivatives are the actual commuting extensions
from \(\mathbb C(t,\rho)\). The field \(K\) is not assumed rational.

The following is an actual linear coordinate change:
\[
\widetilde X=X,\qquad
\widetilde Y=Y+\nu X,\qquad
\widetilde Z=Z-\nu W,\qquad
\widetilde W=W .
\tag{2}
\]
Its inverse subtracts \(\nu\widetilde X\) from \(\widetilde Y\)
and adds \(\nu\widetilde W\) to \(\widetilde Z\), fixing the other
two coordinates. It preserves \(H=XZ+YW\) exactly. The new
ratios and projected entries are
\[
\widetilde t=t+\nu,\quad \widetilde\rho=\rho,\quad
\widetilde y=y,\quad \widetilde z=z-\nu w,\quad
\widetilde w=w,\quad \widetilde\vartheta=\vartheta,\quad
\widetilde\sigma=\sigma-\nu\vartheta .
\tag{3}
\]
Thus \(\widetilde z+\widetilde t\,\widetilde w=z+tw\).
The normalized coefficients \(k,n_0,\ell,m\) are unchanged,
now considered as functions of \(\widetilde t,\rho\).
The normalized potential equations are unchanged as well:
\(\partial_{\widetilde t}=\partial_t\) on \(K\).
The partial \(\partial_{\widetilde Z}\) equals the original
\(\partial_Z\), so \(N,L\), and \(\gamma=Ny\) are unchanged.
The full split initial ideal and the exact degree profile are preserved.

Drop tildes. The additional premise is now simply \(A_1=d^2/t\).

## 2. Exact Euler equations give finite Laurent expressions

The positive-\(y\) determinant coefficients in178 become
\[
k''''+\frac4t k'''=0,\qquad
n_0'''+\frac3t n_0''=0,\qquad
\ell''=\frac d t k''-\frac2t\ell' .
\tag{4}
\]
Here and below primes mean \(\partial_t\) on \(K\).
Since \((t^4k''')'=0\) and \((t^3n_0'')'=0\), the
exact constant field gives complex constants with
\[
\begin{aligned}
k&=k_2t^2+k_1t+k_0+\frac q t,\\
n_0&=n_1t+n_{00}+\frac p t,\\
\ell&=d k_2t+\ell_0+\frac e t+\frac{dq}{t^2}.
\end{aligned}
\tag{5}
\]
For the first two assertions, subtract the displayed explicit
primitives of \(k'''=-6q/t^4\) and \(n_0''=2p/t^3\).
The remainders have third and second derivative zero, respectively,
and hence are the displayed polynomials with complex coefficients.
For the last assertion, multiply its equation in (4) by \(t^2\):
\((t^2\ell')'=dtk''\). The expression in (5) satisfies it;
successive explicit primitive subtraction leaves a complex constant.
This neither integrates an arbitrary algebraic function nor assumes
\(K=\mathbb C(t)\). Coefficients may vanish. The fourth and third
coefficients of \(\vartheta\) are \(q/(d^2t^4)\) and
\(-p/(d^2t^3)\). If \(p=q=0\), its quadratic coefficient is
\(-e/(d^2t^2)\). Thus the nonlinear graph-degree assumption requires
at least one of \(p,q,e\) to be nonzero. The same construction covers
degree two, including \(p=q=0,\ e\ne0\).

## 3. A polynomial with a coefficient-field value

The actual chart is
\[
\begin{gathered}
Y=y+tX,\quad Z=z+\sigma X-t\rho X^2,\quad
W=w+\vartheta X+\rho X^2,\quad \sigma=-t\vartheta-\rho y+k,\\
H=yw+(k'y+d\rho+n_0)X+kX^2,\\
d\vartheta=yw-\frac{k''}{2}y^2-n_0'y+\ell,\qquad
dw=m-\frac{k'''}6y^3-\frac{n_0''}2y^2+\ell'y,\\
z=k'y-y\vartheta+d\rho+n_0-tw,\qquad
m=\frac{d^2}{t}\rho+B_0 .
\end{gathered}
\tag{6}
\]
These are literal projected identities in the actual injective
localization, not an independently prescribed formal map.

Define polynomials in the original coordinates with complex
coefficients:
\[
\begin{aligned}
F_3(X,Y)&=k_2Y^3+k_1XY^2+k_0X^2Y+qX^3,\\
F_2(X,Y)&=n_1Y^2+n_{00}XY+pX^2,\\
F_1(X,Y)&=(dk_1-\ell_0)Y+(dk_0-e)X,\qquad
F=F_3+F_2+F_1,\\
U&=-X^2Z+(d-XY)W,\qquad
J=(d+XY)Z+Y^2W=dZ+YH,\qquad I=J-F(X,Y).
\end{aligned}
\tag{7}
\]
To check the entire polynomial identity, expand \(J=dZ+YH\)
in \(X\), holding \(L[y]\) fixed. Its coefficients are
\[
\begin{aligned}
[X^3]J&=tk,\\
[X^2]J&=(k+tk')y+tn_0,\\
[X]J&=dk-t\ell+
       \left(k'+\frac{t k''}{2}\right)y^2+(n_0+tn_0')y,\\
[X^0]J&=d^2\rho-tm+dn_0+
 (dk'-\ell-t\ell')y+
 \frac{3k''+tk'''}6y^3+
 \frac{2n_0'+tn_0''}2y^2 .
\end{aligned}
\tag{8}
\]
For the constant coefficient, substitute both potentials in (6)
into \(dz+y^2w\). For the other coefficients, multiply the
displayed literal \(H\) by \(y+tX\) and add \(dZ\).

Substituting (5) into (8) gives
\[
\begin{gathered}
k+tk'=3k_2t^2+2k_1t+k_0,\qquad
k'+tk''/2=3k_2t+k_1,\\
n_0+tn_0'=2n_1t+n_{00},\qquad
dk-t\ell=(dk_1-\ell_0)t+dk_0-e,\\
(3k''+tk''')/6=k_2,\quad
(2n_0'+tn_0'')/2=n_1,\quad
dk'-\ell-t\ell'=dk_1-\ell_0 .
\end{gathered}
\tag{9}
\]
The positive-\(X\) coefficients of \(J\) are therefore exactly
those of \(F(X,y+tX)\). The constant coefficient differs by
\[
I=d^2\rho-tm+dn_0=dn_0-tB_0\in K\subset L .
\tag{10}
\]
In particular \(EI=0\) in the actual chart because \(E\) kills
\(L\). The polynomial \(I\) was already constructed in \(B\),
and the localization is injective, so \(EI=0\) in \(B\).
This is an integral return of a particular explicit expression.
It is not the descent of an unspecified projected coordinate.

## 4. An original-ring coordinate with both inverse orders

The pair \(U,J\) satisfies
\[
\begin{pmatrix}U\\J\end{pmatrix}
=
\begin{pmatrix}-X^2&d-XY\\d+XY&Y^2\end{pmatrix}
\begin{pmatrix}Z\\W\end{pmatrix},\qquad
\det=-d^2\in\mathbb C^* .
\tag{11}
\]
Consequently \(X,Y,U,I\) are polynomial coordinates.
For independent target variables \(x,y_1,u_1,i\), put
\(j=i+F(x,y_1)\). The inverse is the polynomial map
\[
X=x,\quad Y=y_1,\quad
Z=\frac{(d-xy_1)j-y_1^2u_1}{d^2},\qquad
W=\frac{(d+xy_1)u_1+x^2j}{d^2}.
\tag{12}
\]
The denominators are nonzero complex constants, not functions
of original coordinates. Substituting (11) into (12) recovers
\(Z,W\) from
\[
(d-XY)J-Y^2U=d^2Z,\qquad
(d+XY)U+X^2J=d^2W .
\tag{13}
\]
Conversely, substituting (12) into the rows of (11) gives
\(U=u_1,J=j\); subtracting \(F(x,y_1)\) gives \(I=i\).
This verifies both inverse orders, including on \(X=0\) and
\(Y=0\). Composing with the inverse of (2) gives an equally
polynomial inverse before reciprocal normalization.

## 5. Recognition and precise scope

We have proved \(B=\mathbb C[I][X,Y,U]\) and \(EI=0\).
The global slice gives \(A=B/(u)\). The equation \(Eu=1\)
expresses one as a polynomial combination of the partial
derivatives of \(u\), so this hypersurface is smooth and
\(A\) is regular.

The original \(E\) is a nonzero \(\mathbb C[I]\)-linear
locally nilpotent derivation of a polynomial three-ring over
\(\mathbb C[I]\). Applying
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
gives
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]} .
\tag{14}
\]
Its exact characteristic-zero, nonzero-derivation, invariant-variable,
and regular-kernel hypotheses have all been checked. The published
statement and its short proof were freshly read; this note does not
re-prove all of its cited prerequisites.

This recognizes only the branch with the additional reciprocal-slope
premise in (1). The separate
[reciprocal-rigidity proof180](split-nonzero-rho-slope-reciprocal-rigidity-pass180-working.md)
supplies that premise for every nonzero-\(m_\rho\) nonlinear graph
of degree two, three or four, including the degree-two coefficient-field
argument not previously covered by178's higher-degree field return.
The zero-slope branch has the distinct
[construction179](split-rho-constant-potential-coordinate-pass179-working.md).
Neither note treats the graph of degree at most one, other initial
configurations, or unrestricted entry. No speed or \(Ny\) was
declared a global unit. No tests have been run for this note at
authoring; written and finite symbolic checks are not expert review,
formal verification, or historical novelty clearance.
