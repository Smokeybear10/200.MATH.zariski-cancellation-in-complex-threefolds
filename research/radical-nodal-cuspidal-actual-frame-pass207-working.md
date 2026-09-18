# Actual radical frames with a nodal or cuspidal projected plane

Status: working explicit actual examples, not a cancellation obstruction.
The possible node and cusp defects isolated in
[the conductor reduction206](radical-projection-conductor-cubic-reduction-pass206-working.md)
both occur in globally sliced polynomial frames with exact time profile
\((1,1,2,2)\) and full initial kernel
\((\mathsf X^2\mathsf Z-\mathsf W^2)\).
The whole original map has a polynomial inverse. Its selected generic
plane ring is nevertheless proper. Thus the actual differential and
Jacobian hypotheses do not exclude these defects universally.

The example has the unit speed \(EX=1\), so its invariant ring is
already a polynomial three-ring. It makes no assertion about a
true minimum profile or recognition of every nonzero-R frame.

## 1. A uniform actual polynomial family

Fix any \(\mu\in\mathbb C\). Start with independent variables
\(u,x,t,\rho\), and put
\[
B=\mathbb C[u,x,t,\rho],\qquad E=\partial_u,\qquad
A=\ker E=\mathbb C[x,t,\rho],\qquad
\vartheta=\frac{x^2-\mu}{2},\qquad j=\vartheta+\rho u.
\tag{1}
\]
Define four elements of this original polynomial ring by
\[
\begin{aligned}
X&=u,\qquad Y=2\rho-x^3+\mu x+tu,\\
Z&=t+2\rho x+j^2,\qquad W=x+uj.
\end{aligned}
\tag{2}
\]
The next section proves that these are polynomial coordinates,
not merely four formal chart expressions.

For independent coordinates \(X,Y,Z,W\), define
\[
\begin{gathered}
I=W^2+XY-X^2Z,\qquad J=\frac{I-\mu}{2},\\
\widehat x=W-XJ,\qquad
\widehat\rho=\frac{Y-XZ+2WJ-XJ^2}{2},\qquad
\widehat t=Z-2\widehat\rho\widehat x-J^2,\qquad
\widehat u=X.
\end{gathered}
\tag{3}
\]
Every expression in (3) is polynomial over \(\mathbb C\).
Only nonzero complex constants are divided; no coordinate or
nonconstant polynomial is inverted.

## 2. Both polynomial inverse orders

First substitute (2) in (3). Using
\(Y=2\rho-2x\vartheta+tu\), one obtains
\[
W^2+XY-X^2Z=x^2+2u\rho=\mu+2j.
\tag{4}
\]
Thus \(J=j\) and \(\widehat x=x\). Moreover
\[
Y-XZ+2WJ-XJ^2
=Y-u(t+2\rho x+j^2)+2(x+uj)j-uj^2
=2\rho.
\]
It follows that \(\widehat\rho=\rho\), \(\widehat t=t\)
and \(\widehat u=u\). This is one complete inverse order.

Conversely, start with independent \(X,Y,Z,W\) and use (3).
The definitions give the exact polynomial identity
\[
2(J-\widehat\rho X)=\widehat x^2-\mu.
\tag{5}
\]
Indeed, expand both sides using \(\widehat x=W-XJ\) and
\(2J=W^2+XY-X^2Z-\mu\).
Consequently the value of \(\vartheta\) reconstructed from
\(\widehat x\) is \(J-\widehat\rho X\), and the reconstructed
\(j\) is \(J\). The formulas
\(W=\widehat x+XJ\) and
\(Z=\widehat t+2\widehat\rho\widehat x+J^2\) now follow
directly from (3). Finally,
\[
\begin{aligned}
2\widehat\rho-2\widehat x(J-\widehat\rho X)+\widehat tX
&=2\widehat\rho-2\widehat xJ+XZ-XJ^2\\
&=Y.
\end{aligned}
\]
This reconstructs all four coordinates and proves the reverse
inverse order. Hence \(B=\mathbb C[X,Y,Z,W]\).

There is also a direct original-ring automorphism explanation.
On \(\mathbb C[X,Y,Z,W]\), the locally nilpotent derivation
\[
\delta=X\partial_W-2W\partial_Y
\quad\text{fixes }X,Z,I,J.
\tag{6}
\]
Its replica \(J\delta\) is locally nilpotent because
\(\delta J=0\). The finite exponential \(\exp(-J\delta)\)
sends
\[
W\longmapsto W-XJ,\qquad
Y\longmapsto Y+2WJ-XJ^2,
\]
and fixes \(X,Z\). Its inverse is \(\exp(J\delta)\).
After this automorphism, replacing the second displayed coordinate
by \(\widehat\rho=(Y'-XZ)/2\) is an invertible triangular
change. In these coordinates,
\(J=(\widehat x^2-\mu)/2+\widehat\rho X\) is independent of
\(Z\), so replacing \(Z\) by \(\widehat t\) in (3) is another
triangular change. This explains the polynomial inverse without
promoting a generic field parameter to an original coordinate.

## 3. Exact profile and the entire initial kernel

The slice is the actual coordinate \(u=X\), and the leading
time coefficients of (2) are
\[
a=EX=1,\qquad b=EY=t,\qquad
e=E^2Z/2=\rho^2,\qquad h=E^2W/2=\rho.
\tag{7}
\]
All are nonzero polynomials. Thus the four time degrees are
exactly \((1,1,2,2)\), not merely upper bounds.

For a new indeterminate \(\tau\), the initial evaluation map is
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(\tau,t\tau,\rho^2\tau^2,\rho\tau^2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2).
\tag{8}
\]
To prove fullness, the fraction field of the image contains
\(\tau,t,\rho\), recovered using its first, second and fourth
entries. They are algebraically independent, so the prime kernel
has height one. The displayed relation is primitive and linear
in \(\mathsf Z\) over
\(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\): its coefficients
\(\mathsf X^2,-\mathsf W^2\) are coprime. Gauss's lemma therefore
makes it irreducible. This proves the entire kernel assertion.
The field divisions used in this height computation are not
used in the actual polynomial inverse.

## 4. Literal selected derivation and exact calibration

The radical pivot is the current \(\partial_Z\); its initial
relation is precisely the bad-swapped convention in
[the nonzero-R eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md).
Differentiate the actual inverse (3) with respect to this original
\(Z\), then substitute the forward coordinates (2). The results are
\[
\begin{aligned}
\partial_Zx&=u^3/2,\\
\partial_Z\rho&=-u/2-xu^2/2,\\
\partial_Zt&=1+xu+(x^2+\vartheta)u^2.
\end{aligned}
\tag{9}
\]
Thus coefficient extraction on the actual invariant ring gives
\[
N=[u^3](\partial_Z|_A)=\tfrac12\partial_x,\qquad
S=\ker_A N=\mathbb C[t,\rho],\qquad
L=\mathbb C(t,\rho),\qquad v=2x,
\quad Nv=1,\quad A_L=L[v].
\tag{10}
\]
There is no unidentified auxiliary derivation in (10).
In particular \(N\) kills all four coefficients (7).

At \(X=0\), the projected coordinates are
\[
y=2\rho-x^3+\mu x,\qquad
z=t+2\rho x+\vartheta^2,\qquad w=x.
\tag{11}
\]
They give both actual projected returns: \(L[y,z,w]=L[x]\),
and \(\mathbb C(y,z,w)=\mathbb C(t,\rho,x)=L(v)\).
Indeed \(x=w\),
\(\rho=(y+x^3-\mu x)/2\), and
\(t=z-2\rho x-((x^2-\mu)/2)^2\).
These projected inverse expressions are polynomial as well.

The three-by-three determinant at fixed \(X\) is
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,x)}=-2,
\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-1=-a^3.
\tag{12}
\]
For the first identity at \(X=0\), the last row is \((0,0,1)\),
while the first two rows begin with \((0,2)\) and \((1,2x)\).
The determinant is therefore \(-2\). It is the same for every
\(X\), either by expanding (2), or by the actual automorphism
and its constant Jacobian. Its full four-by-four Jacobian in
the order \((u,x,t,\rho)\) is also \(-2\).
The factor \(v=2x\) in (12) is necessary; the unnormalized
\(x\)-determinant is not \(-a^3\).

## 5. Every universal potential and the selected cubic

Here \(q=\rho^2\), \(q_t=0\), \(q_{\rho\rho}=2\), and the
coefficient choices are
\[
k=0,\qquad n=t,\qquad\ell=2\rho,\qquad m=\mu,
\qquad \sigma=2\rho\vartheta,
\qquad R=2\vartheta=x^2-\mu\ne0.
\tag{13}
\]
The second universal potential is
\(z-2\rho w=\vartheta^2+t\).
The third and fourth potentials, including their lower terms, are
\[
Rw+y=2\rho,\qquad w^2-2\vartheta=\mu.
\tag{14}
\]
Together with \(\sigma=2\rho\vartheta\), these are all four
integrated identities. No equation is checked only at its top degree.

In the notation of eliminant206, one has
\(S(U,V)=U\), \(b_0=0\), \(Q=-2V-\mu\),
and \(T=2\rho-U\). The literal eliminant is
\[
\mathcal H=(U-2\rho)^2-4V^2(2V+\mu).
\tag{15}
\]
It is irreducible: its discriminant as a quadratic in \(U\)
has the nonsquare factor \(2V+\mu\); when \(\mu=0\) the
resulting odd power of \(V\) still prevents a square.
Thus it is the simple selected component itself, up to a scalar,
with evaluated cofactor a unit. Its center is the squarefree
linear polynomial \(p(U)=U-2\rho\).

The actual scalar determinant can be seen directly from (14).
Here the quantities in the calibrated wedge are
\(B_1=1\), \(C_1=2x\), and
\[
\left[dy\wedge(R\,d\vartheta+dt+2x\,d\rho)\wedge dx
\right]_{dt\wedge d\rho\wedge dx}=-2.
\tag{16}
\]
In particular the same nonzero scalar occurs at both branches
of the node when \(\mu\ne0\); comparison at the two moving
branches cannot yield a universal contradiction to calibration.

## 6. A genuine projected defect and its scope

The projected plane ring is exactly
\[
C=L[y,\vartheta]=L[x^2,x^3-\mu x]
 =L[x^2]\oplus x(x^2-\mu)L[x^2]\subsetneq L[x],
\quad \dim_L(L[x]/C)=1,
\quad\mathfrak c=(x^2-\mu)L[x].
\tag{17}
\]
The even/odd decomposition proves every assertion in (17): the
missing odd class is represented by \(x\), and membership of
both \(f\) and \(xf\) in \(C\) characterizes the displayed
conductor. Also \(O=C+Cw\), \(Rw\in C\), and
\(\operatorname{Frac}C=L(x)\), since
\(x=(x^3-\mu x)/(x^2-\mu)\) in that fraction field.

For \(\mu=0\), (17) is the actual cuspidal ring \(L[x^2,x^3]\).
For \(\mu\ne0\), the two distinct points \(x=\pm\sqrt\mu\)
have the same plane values \((y,\vartheta)=(2\rho,0)\), but
their \(w\)-values are distinct. Thus the normalization has the
node described in conductor206. This is an actual-frame example,
not just the formal boundary polynomial appearing there.

It does not threaten cancellation: \(A=\mathbb C[x,t,\rho]\)
from the outset, and \(EX=1\) makes an original coordinate a
slice. In particular recognition is already elementary through
\(A\simeq B/(X)\simeq\mathbb C^{[3]}\), independently of the
replica description. It instead rules out any proposed argument that every
actual radical nonzero-R projected plane must already be normal.
The original replica in Section2 also illustrates how an actual
coordinate return can coexist with a generic plane defect.
It does not refute an exclusion that additionally assumes
nonunit \(a\), absence of any invariant ambient coordinate, or
a genuinely minimum frame. Those stronger hypotheses fail here.

There is no claim of global degree minimality, arbitrary coordinate
entry, recognition of every radical branch, or unrestricted
cancellation. Two fresh unsaved algebra calculations checked both
polynomial inverse orders, the full determinant and the literal
selected partial: the first used \(\mu=1\), the second retained
an arbitrary constant \(\mu\). They were not saved checker runs
and are not a proof of the field or full-kernel assertions.
No earlier source, checker, index or packet was changed. No
historical novelty, human expert certification, or proof-assistant
verification is claimed.
