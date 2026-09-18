# Recognition of the quartic with nonzero p-derivative

Status: the remaining genuine quartic component of the actual
paraboloid chart281 is recognized when \(p'\ne0\). The argument
includes the degeneration \(A_2=0\) in that note's integrated
coefficient family.

The main step is an exact generic-pencil consequence of actual
field return. It forces one coefficient to be complex. A subsequent
actual triangular coordinate change and the slice condition make
the original derivation preserve a polynomial three-ring. A
three-variable preslice theorem then supplies an invariant ambient
coordinate. No completion of the remaining coefficient ODEs or
descent of the completed-square parameter is asserted.

## 1. Actual input and the corrected coefficient field

Retain every actual hypothesis and the corrected conclusions of the
completely read
[281](principal-paraboloid-quartic-exact-field-reduction-pass281-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
\ker_F\partial_t=\mathbb C,\quad L=F(n),\\
K=F(n,x)=\mathbb C(y,z,w),\qquad
\sigma=(x^2-f)/d,\quad d\in F^*,\quad f\in F.
\end{gathered}
\tag{1}
\]
The original generic-line parameter of271 is not renamed \(x\)
as an ambient coordinate. Here \(x\in K\) is the affine generic-line
parameter obtained by completing the plane equation in281.
The coefficient \(h\) below is a nonzero complex constant.

Assume \(p'\ne0\). Apply the actual weighted automorphism already
proved in281 to translate \(t\) by a complex constant and arrange
\[
r:=p'\ne0,\qquad B=-tr,\qquad
hk'+2tp=\kappa\in\mathbb C,\qquad a_2=-tr'\ne0.
\tag{2}
\]
This \(B\) is a coefficient, not the polynomial ring \(\mathcal B\).
The normalization uses
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W
\]
for a complex \(\tau\). Its inverse sends
\(Y_*\) to \(Y_*+\tau X_*^2\) and
\(Z_*\) to \(Z_*+2\tau Y_*+\tau^2X_*^2\).
It preserves \(X^2Z-Y^2\), the literal selected partial and the
exact fields; after relabeling its new ratio, (2) holds.

The corrected integrated family of281 reads
\[
r^{-2}=\alpha+\delta/t^2,\quad
\alpha\in\mathbb C,\quad\delta\in\mathbb C^*,\qquad
\zeta=t/r,\quad\zeta^2=\alpha t^2+\delta,\qquad
d=d_0r^4/t,\quad d_0\in\mathbb C^*.
\tag{3}
\]
Both \(\alpha\ne0\) and \(\alpha=0\) are allowed.
We do not replace \(F\) by the subfield \(\mathbb C(t,\zeta)\).
The proof below uses the exact field equality in (1), not the
incorrect first-version scalar or integration powers of281.

Write all remaining coefficient functions as
\[
H=hn+c,\quad T=pn+q,\quad \omega=v_1n+v_0,
\qquad c,k,p,q,v_1,v_0\in F,
\tag{4}
\]
and set
\[
a_1=pk''-c''+k'r+2v_1.
\tag{5}
\]
The literal chart is
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+HX^2,\\
z&=2ty+\sigma^2+k'\sigma+n,\\
\theta&=pn+q+c'\sigma
       -h\{(2\sigma+k')y+k''\sigma^2/2\},\\
w&=v_1n+v_0-p\{(2\sigma+k')y+k''\sigma^2/2\}\\
 &\quad-h\{y^2+k''\sigma y+k'''\sigma^3/6\}
       +c'y+c''\sigma^2/2+(rn+q')\sigma .
\end{aligned}
\tag{6}
\]
The genuine quartic has \(\deg_v\sigma=2,\deg_vy=4\).
It is essential that the full field return in (1) is part of this
actual chart, rather than an inference from a scalar determinant.

## 2. Eliminating n gives a generic linear pencil

The completed-square equation of281 gives
\[
n=-2ty+N_0(x),\qquad
N_0(x)=\frac{-x+a_2\sigma^2+a_1\sigma+k'v_1-q'}{r}
                                                        \in F[x].
\tag{7}
\]
Thus
\[
K=F(y,x),\qquad y,x\text{ algebraically independent over }F.
\tag{8}
\]
The equality follows from both inclusions in (1) and (7).
Algebraic independence also follows from \(K=F(n,x)\) and the
nonzero coefficient \(-2t\) in (7).

Substitute (7) in the formula for \(z\):
\[
z=\left(1-\frac{tr'}r\right)\sigma^2
 +(k'+a_1/r)\sigma-\frac xr+\frac{k'v_1-q'}r\in F[x].
\tag{9}
\]
In the formula for \(w\), use
\(hk''=-2(p+tr)\), obtained by differentiating (2).
Its entire \(y\)-dependence becomes
\[
w=-hy^2+\Lambda y+\Omega(x),\qquad
\Lambda=c'-pk'-2tv_1\in F,\quad \Omega\in F[x].
\tag{10}
\]
For example, the coefficient of \(\sigma y\) is
\(-2p-hk''-2tr=0\). All other \(y\)-terms are the two displayed
terms. No property of the unspecified lower coefficient functions
is used in this cancellation.

Now use the actual complex triangular change
\[
J=W+hY^2+\kappa XY,\qquad
W=J-hY^2-\kappa XY.
\tag{11}
\]
Both compositions are the identity, so
\((X,Y,Z,J)\) is an actual polynomial coordinate system.
Put
\[
M=F(X,x).
\]
Since \(X\) is transcendental over \(K\), (8) and
\(Y=y+\sigma X+tX^2\) give
\[
\operatorname{Frac}\mathcal B=M(Y),\qquad
Y\text{ transcendental over }M.
\tag{12}
\]

In these expressions \(Z\in F[X,x]\). Moreover substitution of the
full map (6), not just its \(X=0\) intercept, gives
\[
J=\Lambda Y+\Omega_X,\qquad \Omega_X\in F[X,x].
\tag{13}
\]
Here \(\Omega_X\) denotes a polynomial depending on \(X\), not a
derivative. One direct check of (13) differentiates the raw map
with respect to \(y\), holding \(F,X,x\) fixed. From (7),
\[
n_y=-2t,\quad
\theta_y=-2tp-h(2\sigma+k')=-\kappa-2h\sigma,\quad
H_y=-2ht.
\]
Together with (10) these give
\[
\frac{\partial J}{\partial y}
=(-2hy+\Lambda)+(-\kappa-2h\sigma)X-2htX^2
 +2hY+\kappa X=\Lambda.
\]
Since every expression before differentiating is polynomial in
\(y\) over \(F[X,x]\), (13) follows.

The degree of \(Z\) in \(x\) is important. Differentiate (3) to obtain
\(r'=\delta r^3/t^3\), and hence
\[
1-tr'/r=\alpha r^2.
\]
Equation (9) and the full \(Z\) row in (6) therefore give
\[
Z=\alpha r^2\sigma^2+
 (k'+a_1/r+2tX)\sigma-\frac xr+
 \frac{k'v_1-q'}r+kX+t^2X^2.
\tag{14}
\]
Because \(\sigma=(x^2-f)/d\), its degree over \(F(X)\) is
\[
e:=\deg_x Z=
\begin{cases}
4,&\alpha\ne0,\\
2,&\alpha=0.
\end{cases}
\tag{15}
\]
For the second case the coefficient
\((k'+a_1/r+2tX)/d\) of \(x^2\) is nonzero:
\(X\) is transcendental over \(F\), and \(t\ne0\).
Thus the actual generic-\(X\) map retains degree two even if the
\(X=0\) intercept \(z\) happens to have degree one. This is why the
degeneration \(\alpha=0\) cannot be discarded or treated only at \(X=0\).

## 3. A generic-pencil lemma over a nonclosed field

We use the following elementary consequence of pole degrees.

Let \(k_0\) be a characteristic-zero field, \(M/k_0\) a finitely
generated extension of transcendence degree one, and \(T\)
transcendental over \(M\). Suppose \(\lambda,\omega\in M\) and
\[
M(T)=k_0(T)(\lambda T+\omega).
\tag{16}
\]
If \(\lambda\) is transcendental over \(k_0\), then
\[
[M:k_0(\lambda)]\le1.
\tag{17}
\]
Here no initial algebraic-closure assumption on \(k_0\) inside
\(M\) is required.

To prove this, the right side of (16) is a rational function field
in two algebraically independent variables over \(k_0\).
The generator \(\lambda T+\omega\) must be transcendental over
\(k_0(T)\) because \(M(T)/k_0(T)\) has transcendence degree one.
Consequently \(k_0\) is relatively algebraically closed in \(M\).
In characteristic zero this gives a regular one-variable function
field, with a smooth projective geometrically integral curve model.

The curve/function-field model is the standard equivalence in
[Stacks, Theorem 53.2.6](https://stacks.math.columbia.edu/tag/0BY1).
For a nonconstant rational function on a normal projective curve,
the degree of its pole divisor equals the field degree of its map
to the projective line. This follows by pulling back the point at
infinity using
[Stacks, Lemma 33.44.11](https://stacks.math.columbia.edu/tag/0AYZ).

Under the purely transcendental extension \(k_0\subset k_0(T)\),
a closed point with residue field \(\kappa(P)\) has residue field
\(\kappa(P)(T)\), with the same degree over the new base.
At any pole of \(\lambda\) or \(\omega\), their leading polar
coefficients in \(\lambda T+\omega\) cannot cancel, since \(T\)
is transcendental over \(\kappa(P)\). Its pole order is exactly
the larger of their pole orders, with zero also allowed.
There are no other poles. Thus its pole-divisor degree is at least
the pole-divisor degree of \(\lambda\).

By (16), the former degree is
\([M(T):k_0(T)(\lambda T+\omega)]=1\).
The latter is \([M:k_0(\lambda)]\), proving (17).
This argument neither assumes that all closed points are rational
nor passes silently to a different algebraic constant field.

## 4. Actual field return makes the slope complex

Set \(k_0=\mathbb C(X,Z)\), a subfield of \(M=F(X,x)\).
The field \(M\) has transcendence degree one over \(k_0\), since
\(Z\) is nonconstant in \(x\) by (15). The actual coordinate system
(11), together with (12),(13), supplies the exact equality
\[
M(Y)=\mathbb C(X,Z)(Y)(\Lambda Y+\Omega_X).
\tag{18}
\]
This is where actual field return, rather than merely polynomial
identities or a nonzero Jacobian, enters the argument.

Suppose \(\Lambda\notin\mathbb C\). Since \(F/\mathbb C\) is a
one-variable function field, \(F/\mathbb C(\Lambda)\) is finite.
Also \(X,Z\) are algebraically independent over \(F\), by (15),
so \(\Lambda\) is transcendental over \(k_0\). The exact tower is
\[
\begin{aligned}
[M:k_0(\Lambda)]
&=[F(X,x):F(X,Z)]\,
  [F(X,Z):\mathbb C(\Lambda)(X,Z)]\\
&=e\,[F:\mathbb C(\Lambda)]\ge2.
\end{aligned}
\tag{19}
\]
The first factor is the degree of the polynomial (14), and the
second is unchanged by adjoining independent \(X,Z\).
The generic-pencil lemma applied to (18) contradicts (19).
Therefore
\[
\boxed{\Lambda\in\mathbb C.}
\tag{20}
\]

This conclusion does not make \(t,x\), or any arbitrary element of
\(F\), an ambient polynomial coordinate. It makes precisely one
coefficient in the actual triangular map complex.

## 5. The slice condition forces an actual three-ring restriction

Use (20) to make one more actual triangular change:
\[
J_*=J-\Lambda Y=W+hY^2+\kappa XY-\Lambda Y.
\tag{21}
\]
Its inverse is
\(W=J_*-hY^2-\kappa XY+\Lambda Y\), with \(X,Y,Z\) fixed.
Define the actual polynomial three-ring
\[
S=\mathbb C[X,Z,J_*],\qquad \mathcal B=S[Y].
\tag{22}
\]
Equation (13) gives \(J_*=\Omega_X\in M\).
By (12),(18),(20),
\[
M(Y)=\operatorname{Frac}(S)(Y),\qquad
\operatorname{Frac}(S)\subset M.
\]
For any fields \(D\subset M\) and a variable \(Y\) transcendental
over \(M\), \(M\cap D(Y)=D\), as follows by comparing polynomial
coefficients of a rational expression in \(Y\).
Consequently
\[
\boxed{M=\operatorname{Frac}(S).}
\tag{23}
\]

Let \(a=EX\ne0\). Since \(K=\ker(E|_{\operatorname{Frac}\mathcal B})\)
and \(\operatorname{Frac}\mathcal B=K(X)\), the derivation \(E/a\)
is the \(X\)-partial with \(K\) fixed. The identities
\(Z\in F[X,x]\), \(J_*=\Omega_X\in F[X,x]\), and
\(Y=y+\sigma X+tX^2\) show that
\[
\frac{EX}{a}=1,\qquad
\frac{EZ}{a},\quad\frac{EJ_*}{a},\quad
\frac{EY}{a}=\sigma+2tX
\quad\text{all belong to }\operatorname{Frac}(S).
\tag{24}
\]
This is only a fraction-field conclusion so far.

We now use the actual slice to remove the common multiplier.
The ring \(S\) is a UFD. Choose a primitive vector
\((b_1,b_2,b_3,b_4)\in S^4\), of gcd one, proportional over
\(\operatorname{Frac}(S)\) to the vector of ratios in (24).
There is a common multiplier \(g\in\operatorname{Frac}(S)[Y]\) such that
\[
(EX,EZ,EJ_*,EY)=g(b_1,b_2,b_3,b_4).
\tag{25}
\]
All left-side entries belong to \(S[Y]\).
For every prime of \(S\), at least one \(b_i\) is not divisible
by it. Thus no coefficient of \(g\) can have that prime in its
denominator; equivalently, the Gauss content argument gives
\(g\in S[Y]\).

In the actual coordinate system \((X,Z,J_*,Y)\), the slice \(u\)
is a polynomial. The chain rule and \(Eu=1\) now show that \(g\)
divides \(1\). Hence \(g\in\mathbb C^*\), and (25) proves
\[
\boxed{EX,EZ,EJ_*,EY\in S,\qquad E(S)\subset S.}
\tag{26}
\]
This uses primitivity supplied by the actual global slice, not an
assumption that a coefficient-field scalar is a unit of \(\mathcal B\).

## 6. Actual invariant coordinate and recognition

The restriction \(E_0=E|_S\) is a nonzero LND, because \(EX\ne0\).
It retains
\[
E_0^2X=0.
\tag{27}
\]
It need not initially be irreducible. Let \(\Delta\) be the gcd in
\(S\) of its three coordinate values. Then \(\Delta\mid E_0\Delta\),
because all the coefficients of \(E_0\) are divisible by \(\Delta\).
Local nilpotence implies \(E_0\Delta=0\): otherwise the
\(E_0\)-degree of \(E_0\Delta\) would be one less than that of
\(\Delta\), contradicting divisibility and additivity of degree.
Therefore
\[
D=E_0/\Delta
\]
is an irreducible LND of \(S\), with the same kernel, \(DX\ne0\),
and \(D^2X=0\). Local nilpotence follows explicitly from
\(D^m f=E_0^m f/\Delta^m\).

Apply the exact three-variable preslice theorem of Daigle, in the
restatement
[Dasgupta--Gupta, Theorem 4.8](https://arxiv.org/html/1701.03635v1).
For this irreducible LND on \(S=\mathbb C^{[3]}\), the actual
coordinate \(X\) has nonzero first derivative and zero second
derivative. The theorem supplies actual coordinates \(I,X,V\)
of \(S\) with \(DI=0\). Thus \(EI=0\), and adjoining the existing
coordinate \(Y\) gives
\[
\mathcal B=\mathbb C[I,X,V,Y].
\tag{28}
\]
No generic-field coordinate has been lifted by assertion.

Finally \(A\) is affine and regular because
\(\mathcal B=A[u]\) is a polynomial four-ring.
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies to the nonzero LND \(E\) fixing the actual coordinate \(I\).
It yields
\[
\boxed{A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.}
\tag{29}
\]

## 7. Boundary and verification

The conclusion recognizes the genuine quartic component with
\(p'\ne0\) under the complete actual hypotheses of281. It includes
both \(\alpha\ne0\) and \(\alpha=0\), without an assumption that
\(F=\mathbb C(t,\zeta)\). It does not assert that such a component
is realized, nor does it alone settle the other components of271,
the three-generator branch264, or unrestricted cancellation.

The final corrected281 source was fully reread before this proof.
Fresh unsaved algebra reconstructed the cancellation in (9),(10),
the full actual pencil (13), the polynomial (14), and its degree-two
degeneration. The generic-pencil, field-intersection, content,
local-nilpotence and original-coordinate steps are proved separately
above. No saved checker was executed, imported, or compiled.
No earlier source was changed.

