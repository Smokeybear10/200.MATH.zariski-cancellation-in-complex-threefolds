# Recognition of a line component for the mixed rank-two ratio

Status: bounded working original-ring recognition. Under the supplied
full initial kernel \(ZW-X^2Y^2\), exact time profile \((1,1,2,2)\),
and \(R\ne0\), a projected plane component of degree one forces
\(A\simeq\mathbb C^{[3]}\). One possible line direction is excluded;
the other two have a constant second projection either already or
after an actual good-coordinate swap. The full potentials and scalar determinant force
the constant slope needed for an actual elementary invariant.

This does not address the conic component or the branch \(R=0\).
It is not an arbitrary-entry or unrestricted cancellation theorem.

## 1. Exact actual input and the three line directions

Retain the supplied hypotheses and constructions of the completely read
[mixed-ratio reduction217](rank-two-mixed-ratio-projection-reduction-pass217-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2),\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(as,bs,e_0s^2,h_0s^2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
N=[u^3](\partial_Z|_A)\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=t^2/\rho,
\quad [L:\mathbb C(t,\rho)]<\infty .
\end{gathered}
\tag{1}
\]
The four capital letters are actual polynomial coordinates, \(s\) is
independent, and the displayed ideal is the full initial kernel.
The independent coefficient partials on \(L\) commute and have joint
constants \(\mathbb C\). We do not assume that \(L\) is rational.

The actual projection, with the literal original pivot, has
\[
\begin{gathered}
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+(t^2/\rho)X^2,\\
\sigma=(2t/\rho)y-(t^2/\rho^2)\vartheta+k,\quad k\in L,\\
L[y,z,w]=L[v],\qquad J_0=-a^3\in L^*,\\
R=k_\rho-\frac{2t}{\rho^2}\left(y-\frac t\rho\vartheta\right)\ne0,
\qquad L[y,\vartheta]=L[v].
\end{gathered}
\tag{2}
\]
Assume additionally that the irreducible plane relation \(G\) of
\((y,\vartheta)\) has total degree one. The degree theorem in217
makes both projected entries affine in \(v\), with at least one
nonconstant. The top of \(G\) divides
\(V(\rho U-tV)^4(2\rho U-tV)\). Consequently the complete list of
line directions is
\[
\begin{cases}
\vartheta\in L,\quad \deg_v y=1;\\
y=(t/\rho)\vartheta+\nu,\quad \deg_v\vartheta=1;\\
y=(t/(2\rho))\vartheta+\nu,\quad \deg_v\vartheta=1,
\end{cases}
\qquad \nu\in L.
\tag{3}
\]
In particular a constant \(y\) is not a further case. The ratios
\(t,\rho\) are nonzero by their algebraic independence.

We use the full specialized polynomials \(f,S,Q\) of217, with
independent formal arguments \(U,V\). Equivalently,
\[
\begin{gathered}
J=\rho U-tV,\quad
f=J^2/\rho^3+k_tU+k_\rho V+n,\\
S=-VJ^2/\rho^4+H_2(k)+H_1(n),\\
Q=V^2J^2/\rho^5+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
z=-(t^2/\rho^2)w+f(y,\vartheta),\quad
Rw+S(y,\vartheta)=\ell,\quad
\frac{t^2}{\rho^3}w^2+f_\rho(y,\vartheta)w+Q(y,\vartheta)=0.
\end{gathered}
\tag{4}
\]
Here \(H_j\) denotes the coefficient Taylor polynomial defined in
universal184; \(n,\ell,m\in L\). All formal coefficient derivatives
are taken before evaluation.

## 2. The actual auxiliary derivation

Extend \(N\) to \(A[u]\) by \(Nu=0\) and put
\[
\mathcal P=aN-(NX)E.
\tag{5}
\]
This is an original polynomial derivation. The selected construction
gives \(Na=Nb=Ne_0=Nh_0=0\). Hence \(\mathcal PX=0\),
\([E,\mathcal P]=0\), and \(\mathcal P\) kills \(L\).
On \(B_a=A_a[X]\), it fixes \(X\) and restricts to \(aN\) on
\(A_a\). Since \(Na=0\), that restriction is locally nilpotent;
therefore \(\mathcal P\) is locally nilpotent on the preserved
original polynomial ring. No inversion of \(a\) is asserted in \(B\).

We will use this derivation in the given original coordinates.
Being affine over \(L\) alone is not invoked as an ambient
coordinate change.

## 3. Excluding the direction \(y=(t/\rho)\vartheta+\nu\)

Put \(\mu=t/\rho\). In this direction \(\rho y-t\vartheta=\rho\nu\)
is constant in the line parameter, and \(R\in L^*\).
The third potential in (4) has \(S(y,\vartheta)\) of degree at most
two in \(\vartheta\), so \(w\) has degree at most two.
The polynomial \(f_\rho(y,\vartheta)\) has degree at most one:
its highest-\(q\) term is
\(-(\rho y-3t\vartheta)(\rho y-t\vartheta)/\rho^4\).
Also \(Q(y,\vartheta)\) has degree at most three. Thus the
coefficient of \(\vartheta^4\) in the last identity of (4) is
exactly \(t^2w_2^2/\rho^3\), where \(w_2=[\vartheta^2]w\).
It follows that \(w_2=0\). The second potential in (4) then makes
\(z\) affine as well.

Write \(w=\lambda\vartheta+\omega\),
\(z=\kappa\vartheta+\zeta\) over \(L\), and
\(\tau=aN\vartheta\in L^*\). The original actions are
\[
\mathcal PY=\tau\mu,\qquad
\mathcal PZ=\tau(\mu^2X+\kappa),\qquad
\mathcal PW=\tau(X+\lambda),\qquad
\mathcal P^2Y=\mathcal P^2Z=\mathcal P^2W=0.
\tag{6}
\]
These are actual polynomial actions; the individual displayed
coefficient \(\tau\) need not be an original unit.

Apply Theorem3.1(i) of
[Dasgupta--Gupta](https://arxiv.org/html/1701.03635v1) over the
field \(\mathbb C(X)\). A nonzero nice LND of the polynomial
three-ring fixes a nonzero linear form. Clearing its rational
coefficients gives \(l,m,n\in\mathbb C[X]\), not all zero, with
\[
l(X)\mu+m(X)(\mu^2X+\kappa)+n(X)(X+\lambda)=0.
\tag{7}
\]
The use of this part of the theorem does not require primitive
division. Set
\(d=\max\{\deg l,\deg m+1,\deg n+1\}\), ignoring zero entries.
The coefficient of \(X^d\) in (7) is a nonzero complex linear
combination of \(\mu,\mu^2,1\); the terms \(m\kappa,n\lambda\)
have lower X-degree. But \(\mu=t/\rho\) is transcendental over
\(\mathbb C\). This contradiction excludes this line direction.

## 4. The other nonconstant direction is an actual good-slot swap

Suppose \(y=(t/(2\rho))\vartheta+\nu\). Make the actual constant
linear change
\[
X_*=Y,\qquad Y_*=X,\qquad Z_*=Z,\qquad W_*=W.
\tag{8}
\]
It is its own inverse. The full initial equation is unchanged,
and the exact degrees stay \((1,1,2,2)\). The literal original
\(\partial_Z\) is unchanged, so the selected \(N\) and \(L\)
are unchanged as well. The new ratios are
\(t_*=1/t,\ \rho_*=\rho/t^2,\ q_*=1/\rho=t_*^2/\rho_*\).

In the localized actual projection, substitute
\(X=(X_*-y)/t\). This gives
\[
y_*=-y/t,\qquad
\vartheta_*=\vartheta/t-2\rho y/t^2=-2\rho\nu/t^2\in L.
\tag{9}
\]
The new \(y_*\) is still affine nonconstant in \(v\).
The newly evaluated \(R_*\) is nonzero because its y-coefficient
is \(-2t_*/\rho_*^2\ne0\), while \(\vartheta_*\in L\).
We have not assumed that an arbitrary change preserves the
old zero/nonzero return branch. Formula (9) proves the exact
constant-second hypotheses in the new actual frame.

It therefore suffices to recognize the first case of (3).
In the rest of the proof drop the stars and use that actual frame.

## 5. Full scalar identities force a complex slope

Write \(h=\vartheta\in L\). Since \(y\) is affine nonconstant,
we may use \(y\) as a parameter in the line ring for calculation.
This is not an ambient coordinate assertion. Its change from
\(v\) has nonzero Jacobian \(y_v\in L^*\); the determinant in
columns \(t,\rho,y\) is \(j=J_0/y_v\in L^*\). The coefficient
partials still agree with the original ones on \(L\).

Now \(R\) has degree one in \(y\), and \(S(y,h)\) has degree at
most two. The third potential makes \(w\) affine. The second gives
\[
w=\lambda y+\omega,\qquad
z=y^2/\rho+\kappa y+\zeta,\qquad
\kappa=k_t-2th/\rho^2-t^2\lambda/\rho^2,
\quad \lambda,\omega,\kappa,\zeta\in L.
\tag{10}
\]
Allow \(\lambda=0\). The precise y-squared coefficient of the
third potential and y-cubed coefficient of the fourth are
\[
\frac{\rho^2k_{tt}-4t\lambda-2h}{2\rho^2}=0,\qquad
\frac{\rho^2k_{ttt}-6\lambda}{6\rho^2}=0.
\tag{11}
\]
For the second equality, the y-cubed term of \(f_\rho(y,h)w\)
is \(-\lambda y^3/\rho^2\), and that of \(Q(y,h)\) is
\(k_{ttt}y^3/6\). All other terms have degree at most two.
Differentiate the first equality with respect to \(t\), and
use the second, to obtain \(h_t=\lambda-2t\lambda_t\).

At \(X=0\), the exact determinant in the new parameter is
\[
j=(\kappa_t y+\zeta_t)(\lambda_\rho y+\omega_\rho)
 -(-y^2/\rho^2+\kappa_\rho y+\zeta_\rho)
       (\lambda_t y+\omega_t)\in L^*.
\tag{12}
\]
Its y-cubed coefficient gives \(\lambda_t=0\).
Equation (11) then gives \(h_t=\lambda\) and, by differentiating
(10), \(\kappa_t=0\). The y-squared coefficient of (12) is now
\(\omega_t/\rho^2\), so \(\omega_t=0\). Finally its linear and
constant coefficients give
\[
\zeta_t\lambda_\rho=0,\qquad
j=\zeta_t\omega_\rho\ne0.
\tag{13}
\]
Thus \(\lambda_\rho=0\). The exact joint-constant field yields
\(\lambda\in\mathbb C\). No assumption about the one-partial
constant field or rationality of the lower functions was used.

## 6. An actual auxiliary slice and polynomial kernel

Set \(U=W-\lambda Y\). This is an original polynomial coordinate:
the inverse shear is \(W=U+\lambda Y\), fixing \(X,Y,Z\).
Put \(\tau=aNy\). Equations (5) and (10) imply
\[
\begin{gathered}
\mathcal PX=\mathcal PU=0,\qquad \mathcal PY=\tau\ne0,\qquad
\mathcal P^2Y=0,\\
\mathcal PZ=\tau(2y/\rho+\kappa+(2t/\rho)X),\qquad
\mathcal P^2Z=2\tau^2/\rho\ne0,\qquad \mathcal P^3Z=0.
\end{gathered}
\tag{14}
\]
Here \(\tau=\mathcal PY\) is an actual E-invariant polynomial,
since \([E,\mathcal P]=0\) and \(\mathcal P(EY)=\mathcal Pb=0\).

Let \(\Delta\) be the gcd of the nonzero original coefficients
of \(\mathcal P\), and put \(D=\mathcal P/\Delta\).
The divisibility \(\mathcal P\Delta=\Delta D\Delta\) and
additivity of LND-degree force \(\mathcal P\Delta=0\).
Thus \(D\Delta=0\) and \(\mathcal P^j=\Delta^jD^j\); \(D\) is
an irreducible polynomial LND with the degrees in (14).
Moreover \(\Delta\mid\mathcal PY\in\ker E\), so factorial closure
of \(\ker E\) gives \(E\Delta=0\). Therefore \([E,D]=0\).

Apply Lemma2.3(i) in
[Dasgupta--Gupta](https://arxiv.org/html/1701.03635v1) over the UFD
\(\mathbb C[X,U]\), with the two remaining polynomial variables
\(Y,Z\). Its precise hypotheses hold: \(D\) fixes the base, is
irreducible, and \(D^2Y=0\). It gives
\[
DY\in\mathbb C[X,U],\qquad DZ\in\mathbb C[X,U,Y].
\tag{15}
\]
Also \(E(DY)=D(EY)=0\). To use this actual invariant, assign
weights one and two to \(X,U\). Their E-leading coefficients
are \(a\) and \(h_0=a^2\rho\). A nonzero homogeneous polynomial
of weight \(n\) has leading value
\(a^n\sum_j c_j\rho^j\ne0\), since \(\rho\) is transcendental
over \(\mathbb C\). Thus every nonconstant polynomial in
\(\mathbb C[X,U]\) has positive E-degree. This does not require
algebraic independence of the raw speed \(a\) from other leaders.
Equation (15) consequently gives \(DY=d\in\mathbb C^*\).

Since \(D^3Z=0\), (15) now has
\(DZ=f(X,U)Y+g(X,U)\). Define
\[
H=Z-\frac{f(X,U)}{2d}Y^2-\frac{g(X,U)}dY.
\tag{16}
\]
Then \(DH=0\). The forward coordinates \((X,U,H,Y)\) have
the explicit inverse
\(W=U+\lambda Y\) and
\(Z=H+f(X,U)Y^2/(2d)+g(X,U)Y/d\), with \(X,Y\) fixed.
Substitution in either order cancels both added terms and both
shears. Hence these are actual polynomial coordinates, and
\[
B=\mathbb C[X,U,H,Y],\qquad
D=d\,\partial_Y,\qquad \ker D=\mathbb C[X,U,H].
\tag{17}
\]
The kernel has three variables, not two. The actual auxiliary
slice is \(Y/d\).

## 7. The original recognition endpoint

Commutation makes \(E_0=E|_{\ker D}\) a locally nilpotent derivation
of the actual polynomial three-ring in (17).
It is nonzero because \(E_0X=a\ne0\), and \(E_0^2X=0\).
Divide its coefficients by their gcd in that three-ring if necessary.
The same LND-degree argument used above puts the gcd in its kernel;
the primitive restriction has the same invariant ring and still
has nonzero first and zero second derivative on the coordinate \(X\).
Daigle's theorem, stated exactly as Theorem4.8 in
[Dasgupta--Gupta](https://arxiv.org/html/1701.03635v1), supplies an
invariant polynomial coordinate of this three-ring.
By (17) it is also an ambient coordinate of \(B\), fixed by the
original \(E\).

Finally \(A\simeq B/(u)\) is regular: \(Eu=1\) makes the hypersurface
smooth. The exact regular-kernel theorem
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1),
applied over the ring generated by the actual invariant coordinate,
gives \(A\simeq\mathbb C^{[3]}\). This completes recognition of all
three line directions in (3), one by exclusion and two by the
actual reduction and recognition above.

The full saved217 reduction and universal184 were read before this
argument. The exact DG statements were freshly checked. New unsaved
symbolic calculations independently checked (11)--(13), the swap,
and the slice correction; these finite identities are not substitutes
for the primitive, weighted-degree, or published theorem arguments.
No saved checker was executed, imported or compiled, and no earlier
source or index was changed. No original regularity of \(\rho\),
generic-coordinate descent, unrestricted cancellation, or historical
novelty claim is made. The conic and \(R=0\) branches remain outside
this particular proof.
