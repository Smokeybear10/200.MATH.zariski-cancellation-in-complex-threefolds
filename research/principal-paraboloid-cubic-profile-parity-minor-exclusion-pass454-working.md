# A parity identity excludes the profile (2,3,4) in both regimes

Working exclusion: under the complete actual264 moving-slope chart
of441, the normalized-quadric profile (deg p,deg x,deg q)=(2,3,4)
cannot occur, with NO resonance assumption. The entire genuine fourth
polynomial and its evaluated gradient-minor unit give a short parity
contradiction. This strengthens450's resonance-only exclusion without
extending its all-parameter collision argument beyond its hypotheses.

The proof uses whole polynomial-line generation, not merely equality
of fraction fields. All normalizations remain over the exact coefficient
field. No original complex coordinate is constructed or promoted.

## 1. Actual hypotheses and the exact support needed

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md) and
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md):
the original polynomial four-ring B=C[X,Y,Z,W]=A[u], global polynomial
slice E=partial_u, exact E-degrees (1,2,2,2), ENTIRE weighted initial
kernel mathsf X^2*mathsf Z-mathsf Y^2, literal selected nonzero derivation,
both actual returns, coefficient localization and full calibrated scalar.
In particular impose the moving-slope conditions
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F=\ker_L\partial_s,\qquad b=\nu'\ne0.
\tag{1}
\]
The exact field L is finite over C(t,s); F is finite over C(t),
and neither is assumed rational. No condition f'''=6b or f'''!=6b
is imposed.

The polynomial intrinsic change of441 gives
\[
O=L[v]=L[x,p,q],\qquad
\mathcal H=x^2+bpq-d=0,\qquad d\in L.
\tag{2}
\]
The ENTIRE transformed fourth equation is441(10),(11), defined
from the full genuine H,Q and their levels. Its support can be
grouped, without dropping any coefficient, as
\[
\boxed{\Phi=F_0(p)+xR(p)+bxq+L_0(p)q+\gamma q^2,}
\tag{3}
\]
where
\[
\begin{aligned}
F_0(p)&=\delta p^4+\kappa p^3+c_{20}p^2+c_{10}p+c_{00},\\
R(p)&=\alpha p^2+u_1p,\\
L_0(p)&=\epsilon p^2+c_{11}p+c_{01},\qquad
\gamma=-\ell_{ss}/2\in L.
\end{aligned}
\tag{4}
\]
The symbols F0,L0 are polynomial names, not coefficient fields or
potential levels. The fact that gamma is a FIELD ELEMENT, rather
than a nonconstant polynomial in p, will be essential.

Both equations vanish on the whole line, and the evaluated components
of their gradient wedge generate O. This is the genuine scalar
consequence from438/441. It also implies that the evaluated gradient
of Hcal generates O. These properties are not inferred merely from
the displayed quadric relation.

Suppose for a contradiction that the degrees are (2,3,4).

## 2. A normalization which keeps the two b coefficients identical

Center the quadratic p by an affine change of v over L. Write the
old polynomial as p_old=a*(v^2+c), with a in L*. Set p=p_old/a
and b_new=a*b_old. The quadric (2) then retains its form.
At the same time replace the fourth equation by
\[
\Phi_{\rm new}(x,p,q)=a\,\Phi_{\rm old}(x,ap,q).
\tag{5}
\]
Its xq coefficient is b_new, exactly the coefficient in the
new quadric. The support (3) is unchanged, with new polynomials
F0,R,L0 and constant gamma_new=a*gamma_old. The invertible
linear substitution and nonzero scalar multiplication preserve
the evaluated gradient-minor ideal.

Reuse notation after this licensed normalization:
\[
p=v^2+c,\qquad b\ne0,\qquad \deg_vx=3.
\tag{6}
\]
No square root or coefficient-field extension was required, and
no ambient complex coordinate change was asserted.

Divide x by the monic p:
\[
x=p(Av+B)+rv+h,\qquad A\ne0.
\tag{7}
\]
Polynomiality of q=(d-x^2)/(bp) forces
\[
rh=0,\qquad d=h^2-cr^2,\qquad
q=-\{p(Av+B)^2+2(Av+B)(rv+h)+r^2\}/b.
\tag{8}
\]
All coefficients in (7),(8) belong to L. If r=h=0, then x,p,q
are all multiples of the nonconstant p. The evaluated gradient
(2x,bq,bp) cannot generate a unit ideal, a contradiction.

If h=0 and r is nonzero, the even parts of x,q belong to L[p],
and their odd parts are v(Ap+r) and -2Bv(Ap+r)/b. Since the square
of the odd generator belongs to L[p], their entire generated ring is
\[
L[p,x,q]=L[p]\mathbin{\oplus}v(Ap+r)L[p].
\tag{9}
\]
This cannot contain v: Ap+r is a nonunit because A is nonzero.
Whole generation O=L[v] rules it out. The sole remaining form is
therefore
\[
x=p(Av+B)+h,\qquad
q=-\{p(Av+B)^2+2h(Av+B)\}/b,\qquad Ah\ne0.
\tag{10}
\]
The coefficient B and the constant c may both vanish. This reduction
does not use resonance or the all-T collision return.

## 3. Whole generation turns the gradient wedge into a constant tangent

Here is the precise tangent argument needed below. The vector
\[
\mathbf d=(x',p',q')\in O^3
\]
uses ordinary polynomial derivatives in v with the field L fixed.
Because O=L[x,p,q], a polynomial expression for v in x,p,q can
be differentiated. It gives polynomials a1,a2,a3 in O with
\[
a_1x'+a_2p'+a_3q'=1.
\tag{11}
\]
In particular the derivative vector is nonzero and its component
ideal is the unit ideal.

Let Cvec be the evaluated cross product of the formal gradients
of Hcal and Phi, in the order of variables (x,p,q). Both gradients
annihilate d by differentiating the two level identities. The
minor-unit condition makes their cross product nonzero. Linear
algebra over Frac(O) therefore gives Cvec=psi*d for some psi
in Frac(O). Equation (11) shows
psi=a1*Cvec_1+a2*Cvec_2+a3*Cvec_3, so psi actually belongs to O.
Every cross-product component lies in (psi), and their ideal is
O. Thus
\[
\psi\in O^*=L^*,\qquad \mathbf C=\psi(x',p',q').
\tag{12}
\]
No smoothness or normality theorem was inserted in this step.

Consider specifically the evaluated minor
\[
W=(2x\Phi_q-bp\Phi_x)_{\rm ev}.
\tag{13}
\]
It is minus the second cross-product component. Since p'=2v,
equation (12) gives W=-2psi*v. Consequently its even part is zero:
\[
\operatorname{Even}(W)=0.
\tag{14}
\]
This conclusion uses the full minor UNIT, not just its nonvanishing.

## 4. The complete parity identity and its contradiction

In (10) put
\[
X_0=Bp+h,\qquad
C_0=A^2p^2+(B^2-A^2c)p+2Bh.
\tag{15}
\]
Then, as polynomials in v,
\[
x=X_0+Apv,\qquad q=-(C_0+2AX_0v)/b,\qquad v^2=p-c.
\tag{16}
\]
For a polynomial H(v), define Even(H)=(H(v)+H(-v))/2 and
Odd(H)=(H(v)-H(-v))/2. Define the polynomial in L[p]
\[
\mathcal O=\frac{\operatorname{Odd}(\Phi_{\rm ev})}{Av}.
\tag{17}
\]
Odd polynomials are divisible by v and A is a nonzero field element.
This is exact polynomial division, not localization away from v=0.
All subsequent identities remain polynomial identities at that point.

Using the ENTIRE expression (3), the odd coefficient is
\[
\mathcal O=pR(p)-pC_0-2X_0^2
 -\frac{2X_0L_0(p)}b+\frac{4\gamma C_0X_0}{b^2}.
\tag{18}
\]
The polynomial F0 drops out only because it is even. From
Phi_x=R+bq and Phi_q=bx+L0+2gamma*q, the complete minor (13)
has even part
\[
\operatorname{Even}(W)=
2bh^2+3bpC_0+2X_0L_0
-\frac{4\gamma}{b}X_0\{C_0+2A^2p(p-c)\}
-bpR.
\tag{19}
\]
Adding b times (18) cancels R, L0 and the other mixed terms.
Since h^2+p*C0-X0^2=A^2*p^2*(p-c), it gives the exact identity
\[
\boxed{
\operatorname{Even}(W)+b\mathcal O
=\frac{2A^2}{b}p(p-c)\{b^2p-4\gamma(Bp+h)\}.}
\tag{20}
\]
All lower coefficients in (3) were retained in this calculation.

The level identity Phi_ev=0 gives Ocal=0, while (14) gives
Even(W)=0. The polynomial p(p-c) is nonzero in the domain L[v],
also when c=0. Cancelling it in the polynomial identity (20) gives
\[
b^2p-4\gamma(Bp+h)=0.
\tag{21}
\]
The nonconstant polynomial p is transcendental over L. Its constant
coefficient in (21) forces gamma*h=0. Since h is nonzero, gamma=0.
Its p coefficient then forces b^2=0, contradicting b nonzero.

Thus the profile (2,3,4) is excluded in both parameter regimes.
The proof did not divide by B, c, gamma, a moving derivative, or
an evaluated nonunit. Zero centered constants were addressed before
the nonzero h form was used.

## 5. Verification and scope

The proof uses441's full support and minor unit as inherited actual
inputs. The exact normalization (5) is necessary: rescaling p alone
would give different b coefficients in the quadric and fourth
polynomial. The full scalar itself is not recalculated after that
intrinsic change, and no coefficient derivative is used in the proof.

Fresh unsaved ff608a independently rebuilt (18), (20) and the entire
quadric identity from (16), with zero residuals. Its final coefficient
comparison returned b^2-4B*gamma and -4gamma*h. It retained arbitrary
polynomials R,L0 and all F0 coefficients, rather than a sampled
parameter choice. Earlier exploratory linear systems a4a63b and
c9a62b suggested the obstruction but are NOT the proof: their generic
linear algebra introduced parameter denominators. The written parity
identity and (7)--(21) cover all B,c and remainder boundaries directly.

The whole-generation tangent lemma is proved in Section3, not inferred
from numerical rank or a guessed curve ideal. A separate saved-source
review and held hash belong in the ledger. This result strengthens450
by different hypotheses and reasoning; it does not retroactively make
450's resonance-dependent collision proof valid in nonresonance.

No saved checker was executed, imported, compiled or rerun.
No arbitrary-entry theorem, remaining-profile recognition, unrestricted
cancellation, actual realization, historical novelty, external expert
review or formal certification is claimed.
