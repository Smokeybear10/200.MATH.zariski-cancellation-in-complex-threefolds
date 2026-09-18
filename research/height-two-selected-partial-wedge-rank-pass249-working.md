# Selected-partial wedge rank and the shift-zero endpoint

Status: bounded structural reduction for an actual globally sliced
E-time \((1,1,2,2)\) frame. The two selected intrinsic LNDs commute.
Their wedge is nonzero exactly when their shifts add to one.
A selected shift zero gives an invariant actual ambient coordinate,
and hence recognizes the sliced invariant ring by the stated
three-variable and regular-kernel theorems.

Consequently the still-unrecognized height-two branch has both shifts
in \(\{1,2\}\), and its selected intrinsic LNDs are proportional over
their common invariant field. This is not recognition of that branch,
nor a descent of the proportionality coefficient to the good-ratio
field. No earlier proof, checker, or packet is changed.

## 1. Actual frame and retained selected-partial input

Let
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W],\qquad E\in\operatorname{LND}(B),\qquad
Eu=1,\qquad A=\ker E,\qquad B=A[u],\qquad K=\operatorname{Frac}A,\\
X=x_0+au,\quad Y=y_0+bu,\quad
Z=z_0+z_1u+eu^2,\quad W=w_0+w_1u+hu^2,\\
a,b,e,h\in A\setminus\{0\},\qquad t=b/a\notin\mathbb C.
\end{gathered}
\tag{1}
\]
All lowercase coefficients belong to \(A\). The last condition is
the nonproportional-good-speed branch. If it fails, a constant linear
combination of \(X,Y\) is an invariant actual coordinate, so the
regular-kernel endpoint in Section 5 already applies.

Write \(T_Z=\partial_Z\) and \(T_W=\partial_W\), the literal partials
in the displayed actual polynomial coordinates. The complete
[initial-bound proof157](two-linear-two-quadratic-initial-bound-pass157-working.md),
Sections 2, 3 and 8, supplies
\[
\begin{gathered}
k_i\in\{0,1,2,3\},\qquad
T_i(A)\subset A[u]_{\leq k_i},\qquad
\deg_uT_i(u)\leq k_i,\\
0\ne N_i=[u^{k_i}]T_i|_A\in\operatorname{LND}(A),\qquad
N_i(a)=N_i(b)=N_i(e)=N_i(h)=0,\qquad i=Z,W.
\end{gathered}
\tag{2}
\]
The shift \(k_i\) is exact: it is attained on an element of \(A\).
It is not a numerical upper bound substituted for an actual shift.
In the height-two initial-kernel case, the same proof gives
\(k_Z,k_W\leq2\). The arguments below through Section 5 do not need
that final height-two bound.

For clarity, the intrinsic LND assertion in (2) comes from the actual
partial on \(A[u]\), its degree filtration, and specialization of its
Laurent-rescaled conjugate. The specialization's value on \(u\)
is divisible by \(u\), so local nilpotence makes that value zero.
This gives both the nonzero top LND on \(A\) and the stated bound on
\(T_i(u)\). No localization at an element moved by \(T_i\) is being
declared locally nilpotent.

## 2. A horizontal volume in the original good coordinate

Since \(a\ne0\), use \(X\) as the transcendental variable over \(K\):
\[
\begin{gathered}
K(u)=K(X),\qquad u=(X-x_0)/a,\\
Y=y+tX,\qquad Z=z+\sigma X+qX^2,\qquad
W=w+\theta X+\rho X^2,\\
y=y_0-tx_0,\quad q=e/a^2,\quad \rho=h/a^2,\quad
z,\sigma,w,\theta\in K .
\end{gathered}
\tag{3}
\]
This is a field presentation. It does not make \(X\) a slice or make
the coefficient expressions polynomial ambient coordinates.

Choose a separating transcendence basis
\(\xi_1,\xi_2,\xi_3\) of \(K/\mathbb C\), and put
\(\omega=d\xi_1\wedge d\xi_2\wedge d\xi_3\).
All horizontal differentials in this section hold \(X\) fixed.
The actual invariant-volume calculation gives
\[
d_XY\wedge d_XZ\wedge d_XW=J\,\omega,
\qquad J\in K^*.
\tag{4}
\]
Here is the independence-of-\(X\) check. In the original slice
presentation the coefficient of
\(\omega\wedge du\) in \(dX\wedge dY\wedge dZ\wedge dW\)
is a nonzero element \(J_0\in K\), independent of \(u\):
the flow \(\exp(cE)\) has actual-coordinate Jacobian one and sends
\(u\) to \(u+c\). With the order of forms just specified,
\(J_0=-aJ\). Thus \(J=-J_0/a\in K^*\).
No complex-constant assertion about either volume coefficient is used.

Both \(T_Z\) and \(T_W\) kill \(X\). Their restrictions to \(K\)
therefore extend as derivations of \(K[X]\) fixing \(X\).
In the basis \(\partial_{\xi_1},\partial_{\xi_2},\partial_{\xi_3}\),
these are polynomial vector fields in \(X\), of exact degrees
\(k_Z,k_W\), with leading terms
\[
T_i|_K=a^{-k_i}N_iX^{k_i}
       +\text{terms of smaller \(X\)-degree}.
\tag{5}
\]
Indeed replacing \(u\) by \((X-x_0)/a\) preserves every nonzero
polynomial's degree and gives its indicated leading coefficient.
The degree bounds extend from \(A\) to \(K\) by the quotient rule.
Conversely, exactness on \(A\) prevents a smaller degree on \(K\).

## 3. Exact degree of the selected bivector

The two partials are dual to \(d_XZ,d_XW\) and both kill \(Y\).
Contracting (4) first by \(T_Z\) and then by \(T_W\) gives
\[
\boxed{\ 
\iota_{T_W}\iota_{T_Z}\omega
   =J^{-1}d_XY=J^{-1}(dy+X\,dt).
\ }
\tag{6}
\]
For the sign, contraction of
\(d_XY\wedge d_XZ\wedge d_XW\) first by \(T_Z\) is
\(-d_XY\wedge d_XW\); contraction by \(T_W\) is then \(d_XY\).

The map from bivectors to one-forms given by contraction with
\(\omega\) is a \(K\)-linear isomorphism, extended coefficientwise
to \(K[X]\). Since \(t\notin\mathbb C\), it is transcendental over
\(\mathbb C\), and \(dt\ne0\) in \(\Omega^1_{K/\mathbb C}\).
Thus (6) has exact \(X\)-degree one. It follows that
\[
\begin{gathered}
\deg_X\bigl(T_Z|_K\wedge T_W|_K\bigr)=1,\qquad k_Z+k_W\geq1,\\
\boxed{\ N_Z\wedge N_W\ne0
       \ \Longleftrightarrow\ k_Z+k_W=1.\ }
\end{gathered}
\tag{7}
\]
In fact the coefficient of degree \(k_Z+k_W\) on the left is
\(a^{-(k_Z+k_W)}N_Z\wedge N_W\). If the sum exceeds one it
must vanish; if it equals one it is the nonzero top coefficient.
In particular \((k_Z,k_W)=(0,0)\) is impossible.

This proof does not infer dependence from the transcendence degree
of the field generated by \(a,b,e,h\). It also covers the case where
that field has transcendence degree only one.

## 4. Commutativity and the exact proportionality field

The literal partials commute, and they fix \(X\). Hence the coefficient
of \(X^{k_Z+k_W}\) in their commutator on \(K[X]\) is
\[
[a^{-k_Z}N_Z,a^{-k_W}N_W]
  =a^{-(k_Z+k_W)}[N_Z,N_W]=0.
\tag{8}
\]
The second equality uses \(N_Z(a)=N_W(a)=0\), already in (2).
There are no derivatives of \(X\) in this computation. Thus the
two intrinsic LNDs commute in every case under consideration.

Suppose \(k_Z+k_W>1\). By (7), there is a unique \(f\in K^*\) with
\(N_W=fN_Z\) as derivations of \(K\). Equation (8) implies
\(N_Z(f)=0\). The two derivations have the same kernel in \(A\), and
\[
L:=\operatorname{Frac}(\ker_A N_Z)
  =\operatorname{Frac}(\ker_A N_W),\qquad f\in L^*,
\qquad \operatorname{trdeg}_{\mathbb C}L=2 .
\tag{9}
\]
For the equality of the constant field on \(K\) with the fraction
field of the kernel, take a local slice for \(N_Z\), invert its
nonzero invariant derivative, and apply the slice theorem. After
further localization at all nonzero invariants one obtains
\(A_L=L[v]\), \(N_Zv=1\), and \(K=L(v)\).
Its rational constants are exactly \(L\).

All four leaders belong to \(L\). There is no conclusion
\(f\in\mathbb C(t)\), nor any claim that \(L\) is rational over
\(\mathbb C\). In particular (9) does not authorize cancellation of
the tops by a \(\mathbb C[X,Y]\)-linear row of actual partials.

## 5. A selected shift zero recognizes the original invariant ring

Assume first that \(k_Z=0\). From (2),
\(T_Z(A)\subset A\) and \(T_Z(u)\in A\). The commutator
\([E,T_Z]\) vanishes on both \(A\) and \(u\), so it is zero on \(B\).
Consequently all actual-coordinate coefficients of \(E\) are
independent of \(Z\). The actual three-variable polynomial subring
\[
S=\mathbb C[X,Y,W]
\quad\text{is \(E\)-stable},\qquad
\delta=E|_S\ne0,\qquad \delta^2X=0,\quad \delta X=a\ne0.
\tag{10}
\]
The equality \(\delta X=a\in S\) follows from commutativity with
\(\partial_Z\), not from any coefficient-field descent.

Let \(\Gamma\in S\setminus\{0\}\) be a gcd of the three coordinate
coefficients of \(\delta\), and set \(D=\delta/\Gamma\).
Because \(\Gamma\mid\delta X\ne0\) and \(\delta X\in\ker\delta\),
factorial closure of the LND kernel gives \(\delta\Gamma=0\).
Thus \(D\) preserves \(S\), is locally nilpotent and irreducible,
and has
\[
DX\ne0,\qquad D^2X=0,\qquad \ker D=\ker\delta .
\tag{11}
\]
For example local nilpotence follows directly from
\(\delta^j=\Gamma^jD^j\) on \(S\).

Daigle's theorem, as precisely restated in Dasgupta--Gupta
Theorem 4.8, says that an irreducible LND of a characteristic-zero
polynomial three-ring having a nonfixed coordinate of derivation
degree one admits an invariant coordinate in a completion of that
same coordinate. Applied to \(D\) and the actual coordinate \(X\)
of \(S\), it supplies \(F,H\in S\) such that
\[
S=\mathbb C[F,X,H],\qquad DF=0 .
\tag{12}
\]
Hence \(EF=0\) and \(B=S[Z]=\mathbb C[F,X,H,Z]\):
\(F\) is an invariant actual ambient coordinate.
This application is over \(\mathbb C\), not over a coefficient
field followed by an unproved descent.
The case \(k_W=0\) is identical, using
\(S=\mathbb C[X,Y,Z]\).

Finally \(A\) is affine and regular. Affineness follows from the
slice theorem; regularity follows from \(A[u]=B\) being regular
(equivalently compare dimension and embedding dimension at
\((\mathfrak m,u)\) for each maximal ideal \(\mathfrak m\) of \(A\)).
Bhatwadekar--Gupta--Lokhande Theorem 3.5 states that the regular
kernel of a nonzero \(\mathbb C[F]\)-linear LND on
\(\mathbb C[F]^{[3]}\) is \(\mathbb C[F]^{[2]}\). Therefore
\[
\boxed{\ \min(k_Z,k_W)=0\quad\Longrightarrow\quad
          A\simeq\mathbb C^{[3]}.\ }
\tag{13}
\]
Both external theorems are applied only after their actual
polynomial-ring hypotheses have been established.

## 6. Height-two consequence and the existing actual countercontrol

For height-two full initial kernel, combine the bound \(k_i\leq2\)
from157 with (7)--(13). Every case not already recognized by
Section 5 has
\[
(k_Z,k_W)\in\{(1,1),(1,2),(2,1),(2,2)\},\qquad
[N_Z,N_W]=0,\qquad N_W=fN_Z,\quad f\in L^* .
\tag{14}
\]
This is an exact intrinsic-derivation statement, not a bound on
the weights of generators of the height-two initial ideal.

The [actual countercontrol212](height-two-no-quadratic-relation-actual-control-pass212-working.md)
has \((k_Z,k_W)=(2,1)\) and \(N_W=-N_Z\), in agreement with (14).
In its family with arbitrary \(f_0(t)\), the literal coefficient
columns give \(T_Z+XT_W=\partial_z\) in its original
\((u,t,y,z)\) presentation. This particular row is an actual LND:
the capital partials kill \(X\), so its coefficients are invariant
under both partials. It is also the coordinate partial with respect
to \(Z\) after replacing \(W\) by \(W-XZ\).
This illustrates a possible cancellation, not a universal one.
That transformation need not retain the exact1122 time profile.

The field ratio in (9) has not been shown to arise as a ratio of
leading coefficients of polynomials in the two original good
coordinates. A general minimal-row or original-ring descent
statement remains an additional problem. No global slice for an
intrinsic LND, rationality of its invariant field, or recognition of
all height-two frames is claimed here.

## Sources and exact use

1. [Initial-bound proof157](two-linear-two-quadratic-initial-bound-pass157-working.md),
   fully read, for the actual selected shifts, intrinsic LNDs and
   the height-two bound. Its volume argument is reconstructed here.
2. [Actual height-two control212](height-two-no-quadratic-relation-actual-control-pass212-working.md),
   fully read, for the scope check and its actual row cancellation.
3. N. Dasgupta and N. Gupta,
   [Nice derivations over principal ideal domains, Theorem 4.8](https://arxiv.org/html/1701.03635v1),
   the authors' explicit restatement of Daigle's theorem. The stated
   theorem was freshly read; this does not claim a fresh reading of
   the original Daigle proof.
4. S. M. Bhatwadekar, N. Gupta and S. A. Lokhande,
   [Some K-theoretic properties of the kernel of a locally nilpotent derivation on \(k[X_1,\ldots,X_4]\), Theorem 3.5](https://arxiv.org/html/1501.01438v1),
   freshly read for the regular-kernel recognition endpoint.

No saved checker was executed, imported or compiled for this note.
