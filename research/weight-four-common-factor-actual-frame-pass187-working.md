# An actual frame realizing the common-factor quartic

**Status: working explicit example, pending independent saved-source review.**

The full weighted initial relation \(X^2Z+XYW-Y^4\) is realized by
an actual polynomial coordinate frame of exact time degrees
\((1,1,2,2)\). The inverse is polynomial everywhere. The example
is already a globally sliced translation, so it validates
nonvacuity of the recognized branch, not a new recognition theorem.

## 1. The forward polynomial map

Start with independent coordinates \(x,y,t,\rho\) and put
\[
\begin{gathered}
w=t-y^4,\qquad \vartheta=yw-4ty^3,\\
z=-tw+6t^2y^2-y\vartheta+\rho,\qquad
\sigma=(-\rho+4t^3)y-t\vartheta,\qquad q=-t\rho+t^4,\\
X=x,\qquad Y=y+tx,\qquad
Z=z+\sigma x+qx^2,\qquad W=w+\vartheta x+\rho x^2 .
\end{gathered}
\tag{1}
\]
These are polynomials in the independent source variables.
They specialize the normalized common-factor chart to
\(a=d=1\), \(k=n_0=\ell=0\), and \(m=t\), but the proof below
does not infer invertibility from that coefficient specialization.

Define polynomials in the target variables
\[
I=(1-XY)W-X^2Z+Y^4,\qquad
J=(1+XY)Z+Y^2W.
\tag{2}
\]
For a compact expression for their forward values, write
\[
\begin{gathered}
Z_0(x,y,t)=-tw+6t^2y^2-y\vartheta
              +(4t^3y-t\vartheta)x+t^4x^2,\\
W_0(x,y,t)=w+\vartheta x,\qquad Y_0=y+tx,\\
\Gamma(x,y,t)=(1+xY_0)Z_0+Y_0^2W_0 .
\end{gathered}
\tag{3}
\]
Here \(w,\vartheta\) have the source-polynomial meanings in (1).
In particular \(\Gamma\in\mathbb C[x,y,t]\); no elimination or
rational definition is hidden in (3).

The forward formulas become
\[
Z=Z_0+\rho(1-xY_0),\qquad W=W_0+\rho x^2,
\qquad I=t,\qquad J=\rho+\Gamma(x,y,t).
\tag{4}
\]
Indeed the \(\rho\) coefficient of \(I\) cancels, while that of
\(J\) is
\((1+xY_0)(1-xY_0)+Y_0^2x^2=1\).
For the remaining assertion \(I=t\), expand
\((1-xY_0)W_0-x^2Z_0+Y_0^4\) in \(x\).
Its constant coefficient is \(w+y^4=t\); its coefficients of
\(x,x^2,x^3,x^4\), respectively, are
\[
\begin{gathered}
\vartheta-yw+4ty^3,\qquad
-tw-y\vartheta-(-tw+6t^2y^2-y\vartheta)+6t^2y^2,\\
-t\vartheta-(4t^3y-t\vartheta)+4t^3y,\qquad -t^4+t^4.
\end{gathered}
\tag{5}
\]
Each vanishes by its displayed definition.

## 2. Both polynomial inverse orders

The target change \((X,Y,Z,W)\mapsto(X,Y,I,J)\) itself is a
polynomial automorphism. Its linear matrix in \(Z,W\), after
subtracting \(Y^4\) from \(I\), is
\[
\begin{pmatrix}-X^2&1-XY\\1+XY&Y^2\end{pmatrix},
\qquad \det=-1.
\]
Both inverse orders follow by multiplying this matrix and its
inverse; explicitly
\[
Z=(1-XY)J-Y^2(I-Y^4),\qquad
W=(1+XY)(I-Y^4)+X^2J.
\tag{6}
\]

In these target coordinates, (4) identifies the forward map with
the triangular polynomial map
\[
(x,y,t,\rho)\longmapsto
(x,\ y+tx,\ t,\ \rho+\Gamma(x,y,t)).
\tag{7}
\]
Its polynomial inverse, and hence the inverse of (1) in the
original target variables, is
\[
x=X,\qquad t=I,\qquad y=Y-IX,\qquad
\rho=J-\Gamma(X,Y-IX,I).
\tag{8}
\]
Substituting (1) into (8) returns \(x,t,y,\rho\) by (4).
Conversely, (8) followed by (7) returns \(X,Y,I,J\):
the added and subtracted \(\Gamma(X,Y-IX,I)\) cancel exactly.
Equation (6) then returns the original \(Z,W\).
This proves the other inverse order in the polynomial ring,
including at \(X=0\) and \(1-XY=0\); neither expression is inverted.

## 3. The sliced action, time degrees, and selected pivot

Through this automorphism, identify
\[
B=\mathbb C[X,Y,Z,W]=\mathbb C[x,y,t,\rho],\qquad
E=\partial_x,\qquad
A=\ker E=\mathbb C[y,t,\rho],\qquad EX=1.
\tag{9}
\]
Thus \(E\) is an actual polynomial locally nilpotent derivation
with global slice \(X\). In the source coordinates its values
on the target generators are
\[
EX=1,\qquad EY=t,\qquad EZ=\sigma+2qx,\qquad
EW=\vartheta+2\rho x.
\tag{10}
\]
The inverse (8) makes every coefficient in (10) an original-ring
polynomial. Since \(t,\rho\) are independent and
\(q=-t\rho+t^4\ne0\), the exact time degrees are
\((1,1,2,2)\). Their ordinary leading coefficients are
\((1,t,q,\rho)\). In particular the factors \(1/2\) in
\(E^2Z/2=q\) and \(E^2W/2=\rho\) are retained.

The selected pivot can also be computed from the actual inverse,
without relying on a formal chart realization. Expanding (3) gives
\[
\begin{aligned}
\Gamma={}&-t^2+5ty^4+6t^2y^2
 +(4t^3y+10t^2y^3)x\\
&+(t^4+10t^3y^2)x^2+5t^4yx^3+t^5x^4,
\end{aligned}
\]
so \(\Gamma_t-x\Gamma_y=5y^4+12ty^2-2t\).
Differentiate (8) by the original coordinate partial \(\partial_Z\),
holding \(X,Y,W\) fixed, and then substitute (1). The result is
\[
\begin{gathered}
\partial_Zx=0,\qquad \partial_Zy=x^3,\qquad \partial_Zt=-x^2,\\
\partial_Z\rho
 =1+xy+x^2(5y^4+12ty^2-t),\\
N=[x^3](\partial_Z|_A)=\partial_y,\qquad
\ker_A N=\mathbb C[t,\rho],\qquad L=\mathbb C(t,\rho).
\end{gathered}
\tag{11}
\]
Thus \(y\) is the normalized generic-line parameter \(Ny=1\).
The second projection is the graph
\(\vartheta=-y^5-4ty^3+ty\), of exact degree five over \(L\).
This places the example in the high-graph recognition branch,
with the selected coefficient field itself verified.

## 4. The full weighted initial kernel

Let \(\tau\) be an additional independent initial-form variable,
not the coefficient \(t\). The weighted initial map is
\[
\begin{aligned}
\Theta:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 &\longrightarrow \mathbb C[y,t,\rho,\tau],\\
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 &\longmapsto(\tau,t\tau,(-t\rho+t^4)\tau^2,\rho\tau^2).
\end{aligned}
\tag{12}
\]
Its image has fraction field exactly \(\mathbb C(t,\rho,\tau)\):
\(\tau\) is the image of \(\mathsf X\), while the ratios
\(\Theta(\mathsf Y)/\Theta(\mathsf X)\) and
\(\Theta(\mathsf W)/\Theta(\mathsf X)^2\) recover \(t,\rho\).
The opposite inclusion follows directly from (12).
Independence of \(t,\rho,\tau\) therefore makes
\(\ker\Theta\) a height-one prime ideal.

The polynomial
\[
F_b=\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4
\tag{13}
\]
vanishes under (12). It is irreducible: as a polynomial of degree
one in \(\mathsf Z\) over the UFD
\(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\), its two coefficients
\(\mathsf X^2\) and \(\mathsf X\mathsf Y\mathsf W-\mathsf Y^4\)
are relatively prime. Their only possible common prime would be
\(\mathsf X\), which does not divide the latter coefficient.
Gauss's lemma and linear irreducibility over the fraction field
apply. Hence the height-one prime just obtained is exactly
\[
\ker\Theta=(F_b).
\tag{14}
\]
This proves the full kernel, not merely one relation satisfied by
the leading coefficients.

## Scope and verification

The example has a polynomial invariant ring from the outset and
an original coordinate slice. It does not demonstrate that
\((1,1,2,2)\) is a minimum among all possible coordinate frames:
the independent source coordinates already have time degrees
\((1,0,0,0)\). It realizes the supplied exact profile and full
initial form used in the restricted recognition proofs.

The companion finite controls check the displayed identities and
inverse stages. They do not replace the dimension and
irreducibility argument establishing the full initial kernel.
No checker has been executed, imported or compiled by the author,
no earlier artifact has been changed, and no new recognition,
historical novelty, or unrestricted-solution claim is made.
