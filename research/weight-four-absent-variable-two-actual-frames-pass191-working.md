# Two actual frames for the absent-variable quartic initial relation

**Status: working explicit nonvacuity examples, separate from the190 recognition packet.**

Both the zero-\(R\) and nonzero-\(R\) branches of the supplied
absent-variable chart occur in actual polynomial frames.
The constructions below have exact time profile \((1,1,2,2)\),
full weighted initial kernel
\((\mathsf X^2\mathsf Z-\mathsf Y^4)\), and a global slice.
Every inverse is polynomial and verified in both orders.
These examples do not assert that this profile is minimal over
all polynomial frames. In fact their displayed invariant
coordinates immediately give other frames with a time-zero slot.

Throughout \(E=\partial_x\) on the indicated source polynomial
ring, so \(x\) is a global slice. The target letters \(X,Y,Z,W\)
will be shown to form a polynomial coordinate system.
Initial forms use weights \((1,1,2,2)\) and the ordinary
\(E\)-time degree. The examples require no recognition theorem
or formal determinant realization assumption.

## 1. A zero-R frame

Start with independent \(x,y,t,n\) and
\(\mathcal B_0=\mathbb C[x,y,t,n]\).
Define
\[
\begin{aligned}
X&=x,&Y&=y+tx,\\
Z&=n+6t^2y^2+4t^3yx+t^4x^2,&
W&=t-y^4-4ty^3x+nx^2.
\end{aligned}
\tag{1}
\]
The binomial expansion of \(Y^4\) gives the exact identity
\[
 I_0:=W-X^2Z+Y^4=t .
\tag{2}
\]
Indeed the coefficients of \(x,x^2,x^3,x^4\) cancel separately.

For independent target variables set
\[
\begin{aligned}
 x&=X,\qquad t=I_0=W-X^2Z+Y^4,\\
 y&=Y-I_0X,\\
 n&=Z-6I_0^2y^2-4I_0^3yX-I_0^4X^2,
\end{aligned}
\tag{3}
\]
with \(y\) on the last line replaced by its preceding polynomial
formula. These are polynomials in the target variables.

Composing (1) with (3) returns \(x,t,y\) using (2), then
returns \(n\) directly from the definition of \(Z\).
For the reverse composition, the reconstructed \(X,Y,Z\)
return by definition. The reconstructed \(W\) is
\[
\begin{aligned}
 t-y^4-4ty^3X+nX^2
 &=t+X^2Z-(y+tX)^4\\
 &=I_0+X^2Z-Y^4=W .
\end{aligned}
\]
Thus both compositions are the identity, and
\(\mathcal B_0=\mathbb C[X,Y,Z,W]\).
In particular (2) is an invariant ambient coordinate, with
the simpler target-coordinate inverse
\(W=I_0+X^2Z-Y^4\) while \(X,Y,Z\) are fixed.

The four exact time-leading coefficients are
\[
 \deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
 \operatorname{lc}_E(X,Y,Z,W)=(1,t,t^4,n).
\tag{4}
\]
The nonzero coefficients \(t,t^4,n\) are polynomials in
independent source variables. No specialization of them to
particular complex values is being used.

## 2. The literal selected partial in the zero-R frame

Let \(T_Z\) denote the original coordinate partial \(\partial_Z\),
holding \(X,Y,W\) fixed. Differentiating the inverse (3) yields
\[
 T_Zx=0,\qquad T_Zt=-x^2,\qquad
 T_Zy=x^3,\qquad T_Zn=1+12ty^2x^2 .
\tag{5}
\]
For the last identity, differentiate
\(n=Z-6t^2y^2-4t^3yX-t^4X^2\).
The two cubic terms cancel, as do the two quartic terms.
Equivalently,
\[
 T_Z=-x^2\partial_t+x^3\partial_y
             +(1+12ty^2x^2)\partial_n .
\tag{6}
\]
This polynomial derivation takes \(X,Y,W\) to zero and \(Z\)
to one, so it is exactly the original coordinate partial,
not a chosen derivation with only the same leading action.

On the actual invariant ring
\(\mathcal A_0=\ker E=\mathbb C[y,t,n]\), its leading coefficient is
\[
 N_0=[x^3](T_Z|_{\mathcal A_0})=\partial_y,\qquad
 L_0=\operatorname{Frac}(\ker_{\mathcal A_0}N_0)
       =\mathbb C(t,n),\qquad v=y,\quad N_0v=1 .
\tag{7}
\]
The leading partial degree is exactly three.
Here \(a_E=EX=1\), \(EY/a_E=t\), and
\(\rho=(E^2W/2)/a_E^2=n\).
The projected chart data are
\[
\begin{gathered}
 y=v,\quad z=n+6t^2y^2,\quad w=t-y^4,\quad
 \sigma=4t^3y,\quad \vartheta=-4ty^3,\quad q=t^4,\\
 k=0,\quad R=k_\rho=0,\quad
 n_{\rm chart}=\rho,\quad \ell=0,\quad m=t .
\end{gathered}
\tag{8}
\]
The symbol \(n_{\rm chart}\) identifies the coefficient called
\(n\) in the universal potentials; here it agrees with the
source variable \(n=\rho\).
For example the first potential becomes
\(4ty^3+\vartheta=0\), and the second becomes \(w+y^4=t\).
The literal projected determinant is
\[
 \det\frac{\partial(y,z,w)}{\partial(t,n,y)}=-1=-a_E^3.
\tag{9}
\]
The projected ring also has an explicit inverse:
\(t=w+y^4\), \(n=z-6(w+y^4)^2y^2\).
Thus \(\mathbb C[y,z,w]=\mathbb C[y,t,n]\), not merely an
equality of their fraction fields.

## 3. A nonzero-R frame

Use a different source ring with independent \(x,y,t,h\):
\(\mathcal B_1=\mathbb C[x,y,t,h]\).
Define
\[
\begin{aligned}
 X&=x,\qquad Y=y+tx,\\
 Z&=y^4+t+(4t^3y+h)x+t^4x^2,\\
 W&=h-4ty^3+4t^3y
       +(y^4+t-6t^2y^2+t^4)x+hx^2 .
\end{aligned}
\tag{10}
\]
Its invariant coordinate and a companion are
\[
 I_1=(1+X^2)Z-XW-Y^4=t,\qquad J=W-XZ.
\tag{11}
\]
To verify these and the inverse without a formal-to-actual
inference, introduce the source polynomial
\[
 J=h-4ty^3+4t^3y+(-6t^2y^2+t^4)x
                  -4t^3yx^2-t^4x^3 .
\tag{12}
\]
The source-to-intermediate map
\((x,y,t,h)\mapsto(X,Y,I_1,J)\) is triangular in stages:
\(X=x\), \(I_1=t\), \(Y=y+tX\), and then (12) is \(h\)
plus a known polynomial. Its polynomial inverse is
\[
\begin{aligned}
 x&=X,\qquad t=I_1,\qquad y=Y-I_1X,\\
 h&=J+4I_1y^3-4I_1^3y
       +(6I_1^2y^2-I_1^4)X+4I_1^3yX^2+I_1^4X^3 .
\end{aligned}
\tag{13}
\]
Each forward stage cancels its inverse in either order.

The intermediate-to-target transformation is
\[
 Z=I_1+Y^4+XJ,\qquad W=J+XZ.
\tag{14}
\]
Its inverse is exactly (11): \(J=W-XZ\) followed by
\(I_1=Z-XJ-Y^4\). Both compositions cancel with \(X,Y\)
fixed. Substituting \(Y=y+tx\) and (12) into (14) gives
precisely (10), by the binomial expansion of \(Y^4\).
This proves the two original inverse orders and
\(\mathcal B_1=\mathbb C[X,Y,Z,W]\).
Equations (11), (13) give the explicit inverse in the original
target variables by polynomial substitution.

The time profile and coefficients are
\[
 \deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
 \operatorname{lc}_E(X,Y,Z,W)=(1,t,t^4,h).
\tag{15}
\]

## 4. The literal selected partial in the nonzero-R frame

Differentiate the actual inverse with respect to \(Z\).
One obtains
\[
\begin{gathered}
 T_Zx=0,\qquad T_Zt=1+x^2,\qquad
 T_Zy=-x(1+x^2),\\
 T_Zh=4y(y^2-3t^2)(1+x^2)-x,\\
 T_Z=(1+x^2)\partial_t-x(1+x^2)\partial_y
       +\big(4y(y^2-3t^2)(1+x^2)-x\big)\partial_h .
\end{gathered}
\tag{16}
\]
For a direct check, these values give \(T_ZX=T_ZY=0\)
and \(T_ZZ=1\) upon substituting (10).
Differentiating the literal identity (11) then gives
\(xT_ZW=0\), and the domain property gives \(T_ZW=0\).
Thus (16) is the actual selected original partial.
The displayed value of \(T_Zh\) is polynomial; no inversion
of \(x\) is used to define the derivation.

On \(\mathcal A_1=\ker E=\mathbb C[y,t,h]\), the only cubic
coefficient in (16) is the negative \(\partial_y\) term:
\[
 N_1=[x^3](T_Z|_{\mathcal A_1})=-\partial_y,\qquad
 L_1=\mathbb C(t,h),\qquad v=-y,\quad N_1v=1 .
\tag{17}
\]
In particular \(\Gamma=N_1y=-1\), not one.
Here \(\rho=h\), \(q=t^4\), and the projected data are
\[
\begin{gathered}
 z=y^4+t,\quad w=h-4ty^3+4t^3y,\quad
 \sigma=4t^3y+h,\quad
 \vartheta=y^4+t-6t^2y^2+t^4,\\
 k=\rho,\quad R=k_\rho=1,\quad
 n_{\rm chart}=-t^4,\quad \ell=\rho,\quad m=-t-t^4 .
\end{gathered}
\tag{18}
\]
The first potential is
\(w+4ty^3-4t^3y=h\).
The second is
\(y^4-6t^2y^2-\vartheta=-t-t^4\).
The determinant in the unnormalized parameter \(y\) is \(1\);
using \(v=-y\) gives
\[
 \det\frac{\partial(y,z,w)}{\partial(t,h,v)}=-1=-a_E^3 .
\tag{19}
\]
The projected ring again has a polynomial inverse:
\(t=z-y^4\) and \(h=w+4ty^3-4t^3y\).
Thus \(\mathbb C[y,z,w]=\mathbb C[y,t,h]\).

This example lies in the surviving quartic graph of189 with
\(r=1,\alpha=0,\beta=1,c=0\).
In the notation of the nonzero-\(R\) return190,
\(T=1,b=0\), \(J=W-XZ\), and
\(I_*=Z-XJ\), with correction \(Q_0=Y^4\).
These identifications are checks of the explicit frame; the
existence of the frame was already proved by (12)--(14).

## 5. The full initial kernel in both examples

Let \(s\) denote the third invariant coefficient, namely
\(n\) in the first example and \(h\) in the second.
Both full initial homomorphisms are
\[
\begin{aligned}
\Theta:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
   &\longrightarrow \mathbb C[y,t,s][\xi],\\
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
   &\longmapsto(\xi,t\xi,t^4\xi^2,s\xi^2).
\end{aligned}
\tag{20}
\]
The target variable \(\xi\) records the \(E\)-time degree.
The image has fraction field exactly
\(\mathbb C(\xi,t,s)\): recover \(t\) as
\(\Theta(\mathsf Y)/\Theta(\mathsf X)\) and \(s\) as
\(\Theta(\mathsf W)/\Theta(\mathsf X)^2\).
This field has transcendence degree three.
Hence \(\ker\Theta\) is a height-one prime.

The weighted-homogeneous polynomial
\(\mathsf X^2\mathsf Z-\mathsf Y^4\) vanishes under (20).
It is irreducible: over the UFD
\(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\), its two coefficients
as a polynomial in \(\mathsf Z\) are relatively prime;
over the fraction field it is an irreducible linear polynomial.
Gauss's lemma applies. A height-one prime containing this
irreducible element must therefore equal its principal ideal:
\[
 \ker\Theta=(\mathsf X^2\mathsf Z-\mathsf Y^4).
\tag{21}
\]
This proves the full initial ideal, not just a vanishing relation
or a special-fiber identity.

## Scope

The examples independently realize \(R=0\) and \(R=1\), with
literal original coordinate partials and their normalized top
LNDs. They therefore establish nonvacuity of both branches of
this particular initial configuration.

Their invariant coordinates \(I_0=t\) and \(I_1=t\) make no
minimum-profile claim possible from these examples alone.
They are not counterexamples to cancellation, proofs of
arbitrary entry, or substitutes for the field/descent arguments
in the restricted recognition proofs.
No checker was executed, imported or compiled. All190 and
earlier sources remain unchanged. The examples carry no
historical-novelty, expert-review or formal-certification claim.

