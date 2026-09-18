# Actual-frame compatibility for the two constant-top residuals

The full auxiliary rows of the cubic companion matrix, together with the
commuting coordinate partials, force an additional affine relation that
is not obtained from its determinant alone. It yields a commuting
generator-wise nice field with a constant value on the fourth coordinate.
This field is polynomial in the degree-six case. In the rescaled
degree-five case it is initially rational, and the original polynomial
slice is essential to control the inverted invariant.

This note records the common algebra for both residuals. The complete
polynomial degree-six recognition is in the
[separate proof](cubic-degree-six-pass40.md). Rational compatibility
alone is not asserted to provide global coordinates.

## 1. Actual action and the rescaling identity

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), and let \(E\) be an LND
with a polynomial slice \(s_*\). Take \(0\ne g\in\ker E\), and
put \(\delta=g^{-1}E\) on \(B_g\). It is an LND there, since
\(\delta^j=g^{-j}E^j\). The constant coordinate partials extend
as derivations of \(B_g\); they need not be LNDs of that localization.

For any \(f\in\ker E\) in the fraction field and any derivation \(T\),
the exact identity is
\[
(\operatorname{ad}(fE))^kT
=f^k(\operatorname{ad}E)^kT
-k f^{k-1}\bigl((\operatorname{ad}E)^{k-1}T\bigr)(f)\,E.
\tag{1}
\]
For \(k=1\) this is the bracket product rule. Induction proves the
formula: differentiating the coefficient in the second term contributes
the additional \(k f^k((\operatorname{ad}E)^kT)(f)E\), because
\(E(f)=0\). Thus if the good first commutators and the cubic top
field kill \(g\), their double and fourth adjoint bounds survive
the rescaling. No highest-coefficient LND assertion about the
localized partials is used.

The calculation below assumes the surviving top field is nonzero and
the following actual identities:
\[
\operatorname{ad}_{\delta}^2T_i=0\ (i\le3),\qquad
\operatorname{ad}_{\delta}^4T_4=0,\qquad
h_m=c\ne0,\quad (h_{m-2})_4=\lambda\ne0,\quad h_{m+1}=0,
\tag{2}
\]
where \(h_j=\delta^j x\), \(m\in\{5,6\}\), and \(c,\lambda\)
are complex constants. Here \(c_4=0\), as follows from the highest
coefficient identities in the
[one-cubic-partial proof](whole-frame-recognition-pass39.md).
The polynomial degree-six case takes \(g=1\).

## 2. The auxiliary rows retain one invariant parameter

Set \(r=m-1\), \(J=\operatorname{Jac}(\delta x)\),
\(u=(\operatorname{ad}_{\delta}^2T_4)(x)\), and
\(v=(\operatorname{ad}_{\delta}^3T_4)(x)\ne0\). The actual
inverse-flow Jacobian and companion are
\[
C(t)=I-tJ+(t^2u/2+t^3v/6)e_4^{\mathsf t},\qquad
M=\begin{pmatrix}J&-u/2&-v/6\\e_4^{\mathsf t}&0&0\\0&1&0\end{pmatrix}.
\tag{3}
\]
They satisfy \(M^6=0\) and
\((M^j)_{\rm UL}=\operatorname{Jac}h_j/j!\), as in the prior
proof. The determinant is one also on \(B_g[t]\): the Jacobian
is a unit there and specializes to one at \(t=0\), while a unit
of this polynomial ring cannot depend on \(t\).

The left and right kernels of \(M\) contain no nonzero vector
supported only in its last two positions. Thus a rank-one last
nonzero power cannot have zero upper-left block. In degree five this
gives \(M^5=0\) but \(M^4\ne0\); in degree six it gives
\(M^6=0\) but \(M^5\ne0\). Their Jordan types are respectively
\((5,1)\) and \((6)\). In both cases
\[
\operatorname{rank}M^r=1,\qquad
\operatorname{rank}M^{r-1}=2.
\tag{4}
\]

The rank-one map \(h_r\) satisfies \(\delta h_r=c\).
Its image closure is an affine line: every actual flow orbit maps
onto a line parallel to \(c\), and its irreducible image closure
has dimension one. Consequently \(h_r=c\sigma_0+d_0\), with
\(\delta\sigma_0=1\) and \(d_0\) constant.

The last auxiliary row of \(M^r\), restricted to its first four
columns, is \(\operatorname{Jac}(h_{r-2})_4/(r-2)!\).
Its rank-one relation with \(\operatorname{Jac}h_r\), evaluated
on \(\delta\), makes the proportionality coefficient constant.
After shifting \(\sigma_0\) by a constant, one has
\[
\sigma=(h_{r-2})_4/\lambda,\qquad h_r=c\sigma+d,\qquad
\delta\sigma=1,\quad d_4=0.
\tag{5}
\]

Now the base-restricted rows of \(M^{r-1}\) contain
\[
\operatorname{Jac}h_{r-1}/(r-1)!,\quad
\lambda\operatorname{Jac}\sigma/(r-2)!,\quad
\operatorname{Jac}q/(r-3)!,\qquad q=(h_{r-3})_4.
\tag{6}
\]
Their joint rank is at most two by (4). Put
\[
\tau=q-\lambda\sigma^2/2,\qquad
k=h_{r-1}-c\sigma^2/2-d\sigma.
\tag{7}
\]
Both \(\tau\) and \(k\) are \(\delta\)-invariant. Since
\(\delta\sigma=1\), (6) gives
\(\operatorname{rank}\operatorname{Jac}(k,\tau)\le1\).
This rank statement uses the auxiliary rows, not only the upper-left
block of the companion.

## 3. The actual good partials force an affine relation

Let \(W_i=[\delta,T_i]\), \(i\le3\). Comparing coefficients when
\((T_i+tW_i)\) acts on \(\exp(t\delta)x\) and on its fourth
component gives
\[
W_i\sigma=0,\qquad
W_i k=-\frac c r T_i\sigma,\qquad
W_i\tau=-\frac{\lambda}{r-2}T_i\sigma.
\tag{8}
\]
At least one \(T_i\sigma\) is nonzero, even when \(\sigma\) is
rational. Otherwise \(\sigma\in\mathbb C(x_4)\).
The equation \(\delta\sigma=1\) makes \(\delta\) preserve that
field and have constant field \(\mathbb C\). Repeated integration
of \(\delta^{r-1}x_4=\lambda\) then expresses \(x_4\) as a
polynomial of degree \(r-1\ge3\) in \(\sigma\).
But \(\sigma\in\mathbb C(x_4)\) makes
\(\mathbb C(x_4)=\mathbb C(\sigma)\), contradicting that polynomial
degree. This is a rational function-field argument, not a claim
that \(\sigma\) has no poles.

Choose such a good index. Then \(W_i\tau\ne0\), so
\(\operatorname{Jac}\tau\ne0\). Rank at most one in (7) gives
\(dk_j=R_j\,d\tau\) over the fraction field. Evaluating on this
one \(W_i\) and using (8) forces
\(R_j=(r-2)c_j/(r\lambda)\). Thus
\[
k=\frac{r-2}{r\lambda}c\tau+e,\qquad
e\in\mathbb C^4,\quad e_4=\lambda.
\tag{9}
\]
No polynomial curve-factorization theorem is needed here.
The constant direction \(e\) is outside the original good
three-plane, since its fourth component is nonzero.

## 4. A commuting corrected field

Write \(T_c=c\cdot\partial\), and similarly \(T_d,T_e\).
The successive coefficients of
\(C(t)(\delta x)(\exp(t\delta)x)=\delta x\) give
\[
Jc=\frac{r(r-1)}6\lambda v,
\]
\[
Jd=\frac c r+\frac{r-1}{2}\lambda u
-\frac{r-1}{3}\lambda\sigma v,
\]
\[
Je=\frac{c\sigma}{r(r-1)}+\frac d{r-1}
-\frac{\lambda\sigma}{2}u
+\left(\frac{\lambda\sigma^2}{6}-\frac{r-2}{3}\tau\right)v.
\tag{10}
\]
These formulas retain the middle field \(u\); it is not presumed
locally nilpotent. Define
\[
Z=T_e+\frac{\sigma}{r-1}T_d+
\left(\frac{\sigma^2}{r(r-1)}
+\frac{2(r-2)}{r(r-1)\lambda}\tau\right)T_c.
\tag{11}
\]
Using \(\delta\sigma=1\), \(\delta\tau=0\), and (10), every
coefficient of \([\delta,Z]\) cancels. Also \(Z(x_4)=\lambda\).
The definitions in (5) and (7), together with commutation, imply
\[
Z\sigma=0,\qquad Zq=0,\qquad Z\tau=0,\qquad Z^2(x_i)=0.
\tag{12}
\]
The derivative orders used for \(\sigma,q\) are positive for
both \(r=4\) and \(r=5\).

For \(m=5\), (11) is
\(Z=T_e+(\sigma/3)T_d+(\sigma^2/12+\tau/(3\lambda))T_c\).
For \(m=6\), it is
\(Z=T_e+(\sigma/4)T_d+(\sigma^2/20+3\tau/(10\lambda))T_c\).

## 5. The original slice repairs the localized unit gate

Equations (12) alone do not establish that a rational field is
an LND of \(B_g\). The inverse \(g^{-1}\) must also be controlled.
The original polynomial slice provides exactly that control.

Generator-wise niceness makes sufficiently high \(Z\)-iterates
vanish on every polynomial of \(B\), even though their intermediate
images lie in the fraction field. In particular this holds for
\(g\) and \(s_*\). Since \(\delta(s_*)=1/g\) and
\([\delta,Z]=0\), it also gives
\[
Z^N(g^{-1})=\delta Z^N(s_*)=0
\tag{13}
\]
for sufficiently large \(N\). The finite exponential polynomials
of \(g\) and \(g^{-1}\) multiply to one in
\(\operatorname{Frac}(B)[t]\). Its units are constant in \(t\),
so \(Z(g)=0\).

Thus \(Z\) really is an LND of \(B_g\), and \([E,Z]=0\).
This does not yet make its coefficients polynomial in \(B\),
nor does clearing a denominator preserve its coordinate slice.
Those global issues must be checked separately in the rescaled
degree-five branch.

When \(g=1\), all coefficients in (11) are polynomial and
\(x_4/\lambda\) is an actual ambient coordinate slice for \(Z\).
The projection
\(z_i=x_i-(x_4/\lambda)Z(x_i)\), \(i\le3\), gives polynomial
coordinates together with \(x_4/\lambda\); its inverse is obtained
by substituting \(x_4=0\) in the invariant coefficients of \(Z\).
The complete degree-six proof checks this inverse and the subsequent
commuting-action recognition, using the classical three-variable
LND kernel theorem in its exact scope.

## Verification and attribution

The full-row rank and affine relation were reconstructed independently
across the degree-five and degree-six investigations. The
slice-based unit argument is an additional compatibility lemma,
not an inference from a rational unit Jacobian.

The [degree-six checker](cubic_degree_six_checks_pass40.py) supplies
bounded independent controls for the auxiliary-row identities, the
constants in (10)–(11), the differential ratio, and the actual
polynomial straightening and commuting split used downstream.
It does not construct an actual degree-six model or machine-check
the universal matrix and function-field arguments.
All five methods passed in the initial run in 0.396 seconds.

The algebra above extends the already proved companion identities in
the [pass 39 source proof](whole-frame-recognition-pass39.md).
No new external classification, novelty conclusion, or general
cancellation theorem is asserted by this compatibility note.
