# Excluding the quartic-sextic-octic profile by the primitive minor

Working exclusion: under the entire actual264 moving-slope chart of441,
the normalized-quadric profile (deg p,deg x,deg q)=(4,6,8) is impossible
in both the resonant and nonresonant regimes. Whole polynomial-line
generation and the genuine evaluated gradient-minor unit make one minor
a constant multiple of p'. Exact substitutions in the full fourth
equation force that minor to vanish, a contradiction.

The result concerns only this supplied profile. It does not recognize
the other profiles or make a coefficient-field change into an original
complex coordinate change. No further all-parameter return or newly
normalized scalar formula is needed beyond the actual minor-unit input.

## 1. Full actual input and the genuine polynomial

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md)
and
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md).
These include the original polynomial four-ring B=C[X,Y,Z,W]=A[u],
the global polynomial slice E=partial_u, exact E-degrees (1,2,2,2),
the ENTIRE weighted initial kernel mathsf X^2*mathsf Z-mathsf Y^2,
the literal selected nonzero derivation N, both actual returns, exact
coefficient localization and the full nonzero calibrated scalar.

Assume the moving-slope conditions
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F=\ker_L\partial_s,\qquad b=\nu'\ne0.
\tag{1}
\]
Here L is finite over C(t,s), F is finite over C(t), and neither is
assumed rational. All formal polynomial gradients below fix L. The
intrinsic derivative denoted by a prime on x,p,q fixes L as well and
is differentiation in v. No coefficient derivative is used in the proof.

The exact polynomial substitution and monic division of441 give
\[
O=L[v]=L[x,p,q],\qquad \mathcal H=x^2+bpq-d=0,\qquad d\in L.
\tag{2}
\]
Let tau denote the inverse polynomial substitution from441(8). Use
precisely its transformed genuine fourth equation
\[
\Phi=\tau\bigl(Q-q_0-f''(H-h)/2\bigr),
\tag{3}
\]
with the complete438 primitive Q and both derivatives of the moving
level h retained. Its entire support is
\[
\begin{aligned}
\Phi={}&\delta p^4+\alpha p^2x+\kappa p^3+\epsilon p^2q
          +bxq+u_1px+\gamma q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00},\\
\alpha&=f'''/3-2b,\qquad \gamma=-\ell_{ss}/2.
\end{aligned}
\tag{4}
\]
All coefficients in(4) are elements of L, defined by the complete
expression(3), not chosen as an auxiliary polynomial of the curve.
In particular gamma is a coefficient-field element, not a polynomial
in p. The coefficient of xq is the same b as in(2). No normalization
of p or scaling of either equation is made in this note.

The evaluated components of the gradient wedge of mathcal H and Phi
generate O, by438/441. This follows from the full actual scalar. The
polynomial substitution in441 and subtraction in(3) preserve that
unit ideal. Neither equation is being used merely as a set-theoretic
equation of a guessed curve.

Suppose, for a contradiction, that
\[
\deg_vp=4,\qquad \deg_vx=6,\qquad \deg_vq=8.
\tag{5}
\]
For zero polynomials in degree comparisons use degree minus infinity.
All zero intermediate functions are therefore included.

## 2. The evaluated minor has degree exactly three

The whole return O=L[x,p,q] supplies a polynomial expression for v in
x,p,q. Differentiate it to obtain polynomials a1,a2,a3 in O such that
\[
a_1x'+a_2p'+a_3q'=1.
\tag{6}
\]
Thus the component ideal of the tangent vector (x',p',q') is the unit
ideal. Differentiate the two level equations in(2),(3); both evaluated
formal gradients annihilate this tangent vector.

The minor-unit condition gives rank two for these gradients over L(v).
Their cross product, in the formal order (x,p,q), is therefore
psi*(x',p',q') for some psi in L(v). Equation(6) expresses psi as an
O-linear combination of the cross-product components, so psi belongs
to O. Since those components generate O, psi is a unit. Hence
\[
\psi\in O^*=L^*,\qquad
(\nabla\mathcal H\mathbin{\times}\nabla\Phi)_{\rm ev}
       =\psi(x',p',q').
\tag{7}
\]
This is the primitive-tangent argument also used in454; it is proved
here to specify the exact whole-generation and unit-ideal licenses.

Define the particular evaluated minor
\[
W=(2x\Phi_q-bp\Phi_x)_{\rm ev}=-\psi p'.
\tag{8}
\]
The sign is because this is minus the second cross-product component.
Characteristic zero and deg p=4 imply
\[
W\ne0,\qquad \deg_vW=3.
\tag{9}
\]
Direct differentiation of the entire polynomial(4), followed by
the quadric identity, gives the exact evaluated expression
\[
\boxed{
W=3bx^2+2\epsilon p^2x+4\gamma xq+2c_{11}px+2c_{01}x
       -b\alpha p^3-bu_1p^2-bd.}
\tag{10}
\]
As an identity before evaluation, the right side of(10) is
2x*Phi_q-bp*Phi_x+b*mathcal H. Thus the use of the level equation
in(10) is explicit. No coefficient derivative or new minor is being
introduced.

## 3. The highest degrees and the zero-gamma boundary

Put
\[
z=\frac{\operatorname{lc}_v(q)}{\operatorname{lc}_v(p)^2}\in L^*.
\tag{11}
\]
The leading coefficient of the quadric says that the degree-twelve
leading terms of x^2 and -bz*p^3 agree. The degree-sixteen coefficient
of Phi and degree-fourteen coefficient of W respectively give
\[
\delta+\epsilon z+\gamma z^2=0,
\qquad \epsilon+2\gamma z=0.
\tag{12}
\]
For the second equality the only degree-fourteen terms in(10) are
2epsilon*p^2*x and 4gamma*x*q. Their common nonzero leading factors
can be cancelled. All remaining terms there have degree at most twelve.

If gamma=0, equations(12) give epsilon=delta=0. Now the degree-fourteen
coefficient of the full Phi is proportional to alpha+bz, while the
degree-twelve coefficient of W is proportional to alpha+3bz. Thus
both would vanish. Their difference contradicts bz nonzero. This
excludes gamma=0 without any assumption on alpha.

Consequently
\[
\gamma\ne0,\qquad \epsilon=-2\gamma z,\qquad
\delta=\gamma z^2\ne0.
\tag{13}
\]
Define R=q-zp^2. Its degree is at most seven, because its leading
degree-eight terms cancel. Equation(10) becomes
\[
W=3bx^2+4\gamma xR+2c_{11}px+2c_{01}x
          -b\alpha p^3-bu_1p^2-bd.
\tag{14}
\]
If deg R were seven, the xR term would have degree thirteen, uniquely
highest. This would contradict(9), since gamma is nonzero. Therefore
\[
\deg_vR\le6.
\tag{15}
\]

The complete fourth polynomial after this substitution is
\[
\begin{aligned}
0=\Phi_{\rm ev}={}&\gamma R^2+bxR+(\alpha+bz)p^2x+u_1px
 +(\kappa+c_{11}z)p^3\\
&+(c_{20}+c_{01}z)p^2+c_{11}pR+c_{01}R+c_{10}p+c_{00}.
\end{aligned}
\tag{16}
\]
By(15), every term in(16) has degree at most twelve except the
displayed p^2*x term, whose degree is fourteen. Hence
\[
\alpha=-bz\ne0.
\tag{17}
\]
In particular the resonant case alpha=0 is already impossible.
To exclude the profile in general, continue with the necessary
identity(17), without any derivative restriction on its coefficients.

## 4. Two exact substitutions and their degree constraints

Set
\[
S=R+\frac{b}{2\gamma}x=q-zp^2+\frac{b}{2\gamma}x,
\qquad \deg_vS\le6.
\tag{18}
\]
Define the following coefficients in L:
\[
\begin{aligned}
D_*&=c_{11}+\frac{b^3}{4\gamma},&
A_*&=u_1-\frac{bD_*}{2\gamma},\\
K_*&=\kappa+c_{11}z+\frac{b^3z}{4\gamma},&
C_*&=c_{20}+c_{01}z,\\
C_0^*&=c_{00}-\frac{b^2d}{4\gamma}.
\end{aligned}
\tag{19}
\]
Substitution in the FULL Phi+b^2*mathcal H/(4gamma) gives the evaluated
polynomial identity
\[
\begin{aligned}
0={}&\gamma S^2+D_*pS+A_*px+K_*p^3+C_*p^2+c_{01}S
       -\frac{bc_{01}}{2\gamma}x+c_{10}p+C_0^*.
\end{aligned}
\tag{20}
\]
The same substitution in the original formal minor in(8), using(17),
gives the exact identity
\[
\boxed{W=x(4\gamma S+2D_*p+2c_{01})-b^2pS-bu_1p^2.}
\tag{21}
\]
Here and below W always means the original minor(8). It is not a minor
recomputed in the new variables. Equations(20),(21) retain all lower
coefficients and the level d.

If S had degree five or six, the term 4gamma*x*S in(21) would be
uniquely highest: its degree is 6+deg S, while the p*S term has degree
4+deg S, the p*x term degree ten, and all other terms degree at most
eight. Thus
\[
\deg_vS\le4.
\tag{22}
\]
Now K_*p^3 in(20) is uniquely of degree twelve unless K_*=0; every
other term has degree at most ten. Therefore K_*=0.

Put
\[
T=S+\frac{D_*}{2\gamma}p.
\tag{23}
\]
Initially deg T<=4. Equation(21) has x coefficient 4gamma*T+2c01.
If T had degree four, its x*T term would have degree ten while
the p*S and p^2 terms have degree at most eight. Hence deg T<=3.

After K_*=0, the entire relation(20) becomes
\[
\begin{aligned}
0={}&\gamma T^2+
 \left(A_*p-\frac{bc_{01}}{2\gamma}\right)x
 +\left(C_*-\frac{D_*^2}{4\gamma}\right)p^2\\
&+\left(c_{10}-\frac{c_{01}D_*}{2\gamma}\right)p
 +c_{01}T+C_0^*.
\end{aligned}
\tag{24}
\]
The degree bound on T makes A_*p*x uniquely of degree ten, so A_*=0.
The p^2 term is then uniquely of degree eight, so
\[
A_*=0,\qquad C_*=\frac{D_*^2}{4\gamma}.
\tag{25}
\]
These comparisons include T=0 and all zero lower coefficients.

## 5. The minor must vanish

Before imposing A_*=0, the exact substitution(23) in(21) gives
\[
W=T(4\gamma x-b^2p)+2c_{01}x-bA_*p^2.
\tag{26}
\]
With(25), suppose T is nonconstant. Its degree is between one and
three. Then x*T has degree 6+deg T, greater than both p*T of degree
4+deg T and the remaining x term of degree six. Its coefficient
4gamma is nonzero, contradicting deg W=3. Thus T belongs to L.

Write T=t0 in L. Equation(26) reduces to
\[
W=(4\gamma t_0+2c_{01})x-b^2t_0p.
\tag{27}
\]
Since x has degree six and p has degree four, while W has degree
exactly three, the two coefficients must vanish in order. First
4gamma*t0+2c01=0, then b^2*t0=0. As b is nonzero, t0=0 and c01=0.
Equation(27) now says W=0, contradicting(9).

This proves the (4,6,8) exclusion in both regimes. No division by an
evaluated polynomial was made. Coefficient divisions use only the
nonzero leading coefficients defining z, b, and gamma after its zero
branch was excluded.
The centered level d and every unused lower coefficient were unrestricted.

## 6. Verification and retained scope

The complete current438 and441 sources, the primitive-tangent argument
of454, and the writing guide were read before authoring. Fresh unsaved
calculation ce4927 rebuilt every full polynomial identity used in the
degree descent: the initial W identity modulo mathcal H, the entire
R-shift expression(16), the entire shifted Phi plus quadric(20), the
exact minor(21), and both T-shift formulas(24),(26). Every identity
residual was zero. The degree comparisons and unit-tangent argument
are the written proofs, not numerical evidence.

The full actual hypotheses and genuine-minor input of438/441 remain
retained dependencies. The proof uses no all-parameter collision return,
new coefficient-field integration, rationality assumption, additional
scalar normalization or original-coordinate promotion. It does not
assert a recursive certification of the retained dependency history.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited. No remaining-profile recognition,
arbitrary chart entry, unrestricted cancellation, actual realization,
historical novelty or formal-certification claim is made.
