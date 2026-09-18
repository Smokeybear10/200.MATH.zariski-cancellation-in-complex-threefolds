# Recognition in the zero-coupling, scalar-intercept paraboloid branch

Status: an actual recognition result for the subcase \(k_s=n_s=0\)
of the principal exact1222 paraboloid chart264. The proof uses the actual
field return and the entire scalar Jacobian, not just its leading
coefficients. It does not recognize the remaining branches of264.

No earlier source or frozen packet is changed. No saved checker is
executed, imported, or compiled.

## 1. Actual setup and the retained chart

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad \deg_E(X,Y,Z,W)=(1,2,2,2).
\tag{1}
\]
Write \(a=EX\), \(b=E^2Y/2\), \(c=E^2Z/2\), and \(e=E^2W/2\).
Assume the full weighted initial kernel is
\[
\ker\{\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\to A[T]\}
=(\mathsf X^2\mathsf Z-\mathsf Y^2),
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\mapsto(aT,bT^2,cT^2,eT^2).
\tag{2}
\]
In particular \(t=b/a^2\) and \(s=e/a^2\) are algebraically independent.

Use the literal \(Z\)-partial and all the actual entry, localization, and
volume conclusions of the fully read
[principal chart264](principal-one-affine-paraboloid-chart-pass264-working.md).
Its exact horizontal shift is four. Its intrinsic leading derivation
\(N\) is a nonzero locally nilpotent derivation of \(A\), with
\[
Na=Nt=Ns=0,\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\qquad
A\otimes_{\ker N}L=L[v],\quad Nv=1.
\tag{3}
\]
Put \(K=\operatorname{Frac}A=L(v)\). The coefficient derivations
\(\partial_t,\partial_s\) extend uniquely to \(L\), commute there,
and fix \(v\). At fixed actual \(X\),
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,
\end{aligned}
\qquad k\in L,\quad y,z,w,\sigma,\theta\in L[v].
\tag{4}
\]
The actual returns and calibrated determinant are
\[
K=\mathbb C(y,z,w),\qquad L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\tag{5}
\]
Thus the determinant is independent of \(X\). These assertions use the
actual polynomial four-ring and the full initial kernel, not just a
formal parametrization.

The first two potentials of264 are
\[
\begin{aligned}
z&=2ty+\sigma^2+k_t\sigma+k_s\theta+n,\\
k_sw+(2\sigma+k_t)y+
\frac{k_{tt}}2\sigma^2+k_{ts}\sigma\theta+
\frac{k_{ss}}2\theta^2+n_t\sigma+n_s\theta&=\ell,
\end{aligned}
\qquad n,\ell\in L.
\tag{6}
\]
This note assumes precisely
\[
\boxed{k_s=0,\qquad n_s=0.}
\tag{7}
\]
The conclusion is \(A\cong\mathbb C^{[3]}\). Neither \(k_s\ne0\) nor
\(k_s=0,\ n_s\ne0\) is included.

## 2. The exact coefficient curve field

Set \(F=\ker_L\partial_s\). It contains \(\mathbb C(t)\), is preserved
by \(\partial_t\), and is finite over \(\mathbb C(t)\).
Here is the finite-field justification.

For \(\alpha\in F\), differentiate its monic minimal polynomial over
\(\mathbb C(t,s)\) by \(\partial_s\). Since \(\partial_s\alpha=0\),
the resulting polynomial vanishes at \(\alpha\); its degree is strictly
smaller unless it is zero. Minimality therefore makes every coefficient
of the original polynomial \(s\)-constant. Those coefficients belong to
\(\mathbb C(t)\). Thus each \(\alpha\in F\) is algebraic over
\(\mathbb C(t)\). The relative algebraic closure of \(\mathbb C(t)\)
in the finitely generated field \(K\) is finite, giving the assertion.
Commutation of the two extended derivations proves the preservation
under \(\partial_t\).

In particular
\[
k,n,k_t,k_{tt},n_t\in F,\qquad NF=0,\qquad s\notin F.
\tag{8}
\]
The final inequality follows either from \(\partial_s s=1\), or from
the independence of \(t,s\) and the finiteness of \(F/\mathbb C(t)\).
No rational parameter for the curve field \(F\) is assumed.

Under (7), the two potentials reduce to
\[
z=2ty+\sigma^2+k_t\sigma+n,\qquad
(2\sigma+k_t)y+\frac{k_{tt}}2\sigma^2+n_t\sigma=\ell.
\tag{9}
\]

## 3. A block-Jacobian obstruction using the actual field return

We isolate the field argument used twice below. Suppose \(h\in K\)
satisfies \(Nh\ne0\), and suppose the first two actual expressions
in (4) belong to \(F[h,X]\), with \(y,z\in F[h]\).

Because \(F,h,w\subset K\), the actual field return in (5) gives both
inclusions
\[
K=\mathbb C(y,z,w)\ \subset\ F(h,w)\ \subset\ K.
\tag{10}
\]
Only at this point may one conclude \(K=F(h,w)\). As
\(\operatorname{trdeg}_{\mathbb C}F=1\) and
\(\operatorname{trdeg}_{\mathbb C}K=3\), the elements \(h,w\) are
algebraically independent over \(F\).

Thus \(t,h,w\) are a separating transcendence basis of \(K/\mathbb C\).
The partial derivatives in \(h,w\) fix \(F\); the \(t\)-partial extends
the unique derivation of the finite separable extension \(F/\mathbb C(t)\).
The change from \((t,s,v)\) to \((t,h,w)\) has nonzero Jacobian in
\(K\) and is independent of \(X\). Consequently (5) implies
\[
0\ne
\det\frac{\partial(Y,Z,W)}{\partial(t,h,w)}
\in K^*,
\quad\text{independently of }X.
\tag{11}
\]
Since \(Y,Z\) are independent of \(w\) in these coordinates, the
determinant factors as
\[
J_2(X)\bigl(1+\theta_wX+s_wX^2\bigr),\qquad
J_2(X)=\det\frac{\partial(Y,Z)}{\partial(t,h)}
\in K[X].
\tag{12}
\]
The subscripts in (12) refer to the new separating basis, not the
original coefficient partials. The product is a nonzero scalar by
(11), so \(J_2(X)\) is nonzero and each of the two polynomial factors
has degree zero. The second factor has constant term one. In
particular \(s_w=0\).

The constants of \(\partial_w\) in the rational function field
\(F(h,w)\) are exactly \(F(h)\), hence \(s\in F(h)\).
But \(NF=0\), \(Ns=0\), and \(Nh\ne0\). The chain rule on \(F(h)\)
therefore gives \(0=Ns=(Nh)s_h\), so \(s_h=0\). The constants of
the one-variable rational derivative are exactly \(F\), giving
\(s\in F\), contrary to (8).

We have proved: under the actual field return (5), no such \(h\)
can exist. This is an obstruction in the actual rational function
field. It is not a claim that \((t,h,w)\) are ambient polynomial
coordinates, or that a coefficient-field linear change lifts to \(B\).

## 4. The two cases for the first linear coefficient

First suppose \(\sigma\notin L\), equivalently \(N\sigma\ne0\).
The second identity of (9) can be divided formally by
\(2\sigma+k_t\). Polynomial division in a formal indeterminate gives
\[
\begin{aligned}
y&=-\frac{k_{tt}}4\sigma+\frac{k_{tt}k_t}{8}-\frac{n_t}{2}
+\frac{\ell-k_{tt}k_t^2/8+n_tk_t/2}{2\sigma+k_t}.
\end{aligned}
\tag{13}
\]
Every term is an element of \(L(v)\), and \(y,\sigma\in L[v]\).
If the constant remainder in the numerator were nonzero, the
nonconstant polynomial \(2\sigma+k_t\) would divide a nonzero constant
in \(L[v]\). This is impossible. Therefore
\[
\ell=\frac{k_{tt}k_t^2}{8}-\frac{n_tk_t}{2}\in F,\qquad
y=-\frac{k_{tt}}4\sigma+\frac{k_{tt}k_t}{8}-\frac{n_t}{2}
\in F[\sigma].
\tag{14}
\]
The first identity of (9) then gives \(z\in F[\sigma]\).
Since \(2t\sigma+k\in F[\sigma]\), both \(Y,Z\) belong to
\(F[\sigma,X]\). Section3 with \(h=\sigma\) is a contradiction.
This argument also covers \(k_{tt}=0\); it never assumes \(y\)
is nonconstant.

It remains that \(\sigma\in L\). Put \(\gamma=2\sigma+k_t\).
If \(\gamma\ne0\), the second identity of (9) makes \(y\in L\),
and the first makes \(z\in L\).

If \(\gamma=0\), then \(\sigma=-k_t/2\in F\), and
\[
z=2ty+n-\frac{k_t^2}{4}.
\tag{15}
\]
If \(Ny\ne0\), this time \(y,z\in F[y]\) and
\(Y,Z\in F[y,X]\). Section3 applies with \(h=y\), again a
contradiction. Thus \(Ny=0\), and (15) gives \(Nz=0\).

In every remaining actual case we have proved
\[
Ny=Nz=N\sigma=N(2t\sigma+k)=0.
\tag{16}
\]

## 5. Descent to an actual invariant coordinate

Extend \(N\) to \(B=A[u]\) by \(Nu=0\). Define the actual polynomial
derivation
\[
P=aN-(NX)E.
\tag{17}
\]
It satisfies \(PX=0\), and \(P|_A=aN\), so \(P\ne0\).
Moreover \(Na=0\), and \(E(NX)=N(EX)=Na=0\), whence
\([E,P]=0\). Each coefficient in (4) lies in \(K=\ker_{\operatorname{Frac}B}E\);
therefore \(P\) acts on it as \(aN\). Using (16) and \(Nt=0\)
in (4) proves \(PY=PZ=0\).

As \(X,Y,Z,W\) are actual coordinates, it follows that
\[
P=f\,\partial_W\quad\text{for some }0\ne f\in B,\qquad
\ker_B P=\mathbb C[X,Y,Z]=:S.
\tag{18}
\]
This conclusion uses only that \(P\) is a nonzero derivation fixing
three actual coordinates. It does not require \(P\) to be locally
nilpotent, or \(f\) to be invariant. The commutation \([E,P]=0\)
makes \(S\) stable under \(E\).

Let \(\delta=E|_S\). This is a nonzero locally nilpotent derivation
of the actual polynomial three-ring \(S\); its actual coordinate
\(X\) satisfies \(\delta X=a\ne0\) and \(\delta^2X=0\).
Take the greatest common divisor \(\Delta\) of its three coefficients
in \(S\). Since \(\Delta\mid\delta X\in\ker\delta\), factorial
closure of the kernel of a locally nilpotent derivation gives
\(\delta\Delta=0\). Hence \(D=\delta/\Delta\) is an irreducible
locally nilpotent derivation, with
\[
DX\ne0,\qquad D^2X=0.
\tag{19}
\]
Local nilpotence follows explicitly from
\(D^j(f)=\delta^j(f)/\Delta^j\) in \(\operatorname{Frac}S\);
the quotients are in \(S\) because \(D\) is a polynomial derivation.

Theorem4.8 in Dasgupta--Gupta's
[primary account](https://arxiv.org/html/1701.03635v1),
attributed there to Daigle, applies to this irreducible derivation
of a three-variable polynomial ring with an actual coordinate
satisfying (19). It supplies an invariant coordinate \(I\in S\)
and a third coordinate \(H\) such that
\(S=\mathbb C[I,X,H]\). In particular \(EI=\delta I=0\), and
\[
B=\mathbb C[I,X,H,W].
\tag{20}
\]
Thus \(E\) is an actual \(\mathbb C[I]\)-linear locally nilpotent
derivation of a polynomial three-ring over \(\mathbb C[I]\).

The ring \(A\) is an affine regular ring: it is an algebra retract
of \(B=A[u]\), hence affine, and regularity descends from the
polynomial extension \(A[u]\). Theorem3.5 of Bhatwadekar--Gupta--Lokhande's
[primary paper](https://arxiv.org/html/1501.01438v1)
therefore applies to \(E\) in (20), and gives
\[
\boxed{A\cong\mathbb C[I]^{[2]}\cong\mathbb C^{[3]}.}
\tag{21}
\]
The published inputs are used only after an actual invariant
coordinate has been obtained. No generic-field coordinate is
descended by assertion.

## 6. Scope and boundary

This result recognizes precisely the additional subcase (7) of264.
The actual field return in (5) is indispensable in Section3:
formal potentials, or even a scalar Jacobian in a larger function
field, do not justify (10). Similarly, the product in (12) is
nonzero before the degree argument is made.

The remaining alternatives \(k_s\ne0\) and \(k_s=0,\ n_s\ne0\)
are not resolved here. In particular the actual paraboloid
translation control retained in259 has \(k_s=0,\ n_s=1\), so
nothing in this note declares the supplied full-kernel sector
empty. No unrestricted exact1222 or general cancellation claim,
and no novelty claim, is made.

The complete264 source and the curve-field entry criterion266
were read before this argument. The block-Jacobian obstruction
here is distinct from266's polynomial-entry hypothesis. The
precise published three-variable and regular-kernel endpoints
were freshly checked in the primary sources cited above.

