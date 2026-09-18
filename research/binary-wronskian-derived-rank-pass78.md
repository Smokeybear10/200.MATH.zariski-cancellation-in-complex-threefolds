# A binary Wronskian forces a fourth direction

In the nonlinear ternary-cone branch with a supplied good partial,
the original action, its supplied good partial, the derived field,
and the next bracket have generic rank four. Consequently the second
coordinate iterate of the derived field is not even rationally
parallel to that field. In particular that derived field is not nice
in the original coordinates.

This is a restricted original-frame conclusion, not a primitive
freeness theorem or a bound on third or higher coordinate iterates.
The binary parameters may be dependent, and their ideal may be the
unit ideal. No proper-parameter hypothesis is needed here.
The determinant proof below does not require algebraic parameter
derivatives to be regular at the parameter zero locus.

## 1. Exact original hypotheses and the inherited rank gate

Let
\[
B=\mathbb C[x_1,x_2,x_3,w],\quad K=\operatorname{Frac}B,
\quad E=P\cdot\partial\in\operatorname{LND}(B),\quad
E(s)=1,\quad E(P)=0,\quad T=\partial_w,
\quad [E,[E,T]]=0.
\tag{1}
\]
Assume the distinguished velocity cone is the nonlinear ternary
cone in the [pass76 omission theorem](nice-good-direction-invariant-omission-pass76.md).
Take its actual binary parameters from
[pass77 descent](nice-binary-parameter-descent-pass77.md):
\[
P_i=h_i(p,q)\ (i\le3),\qquad p,q\in\ker E,\qquad
\gcd_B(p,q)=1,\qquad p,q\ne0,\qquad
\deg h_i=e\ge2.
\tag{2}
\]
The three homogeneous binary forms \(h_i\) have one degree and
are linearly independent over \(\mathbb C\). Otherwise their
constant linear relation would make the transverse cone planar.
These are actual polynomials, not two newly chosen rational
coordinates. They are not assumed algebraically independent. At
least one is nonconstant: otherwise the first three velocity entries
would be constant and the full Jacobian could have rank at most one,
contrary to the rank-two gate below.

Write \(J=\operatorname{Jac}P\) and assume the non-square-zero
branch \(J^2\ne0\), as in those predecessor notes. The complete
[nice sliced rank argument](nice-slice-adjoint-rank-pass74.md),
Sections 1--2, supplies
\[
J^3=0,\quad \operatorname{rank}_KJ=2,\quad
\operatorname{rank}_KJ^2=1,\quad JP=0,\quad
P\notin\operatorname{im}_KJ.
\tag{3}
\]
For the last assertion, the nilpotent partition is \((3,1)\), so
\(\operatorname{im}J\cap\ker J=\operatorname{im}J^2\).
If \(P\) belonged to \(\operatorname{im}J\), its line would
equal \(\operatorname{im}J^2\). A nonzero second adjoint of an
actual coordinate partial would then be parallel to \(E\), contrary
to the [highest-vertical-adjoint exclusion](vertical-top-exclusion-pass69.md).
Thus the last assertion in (3) is not inferred from rank alone.

Set \(Q=[T,E]\) and \(Z=[T,Q]\); use \(Q(x)\) and \(Z(x)\)
for their four-entry original coefficient columns. Goodness implies
\([E,Q]=0\). Differentiating \(E(P)=0\) by the actual constant
partial \(T\) and comparing that commutator gives
\[
Q(x)=T(P)=Je_4,\qquad JQ(x)=Q(P)=0,\qquad E(Q(x))=0,
\qquad Z(x)=T^2(P).
\tag{4}
\]
Indeed the differentiated nice identity is \(E(Q(x))+JQ(x)=0\),
while the commuting identity is \(E(Q(x))-JQ(x)=0\).

The field \(Q\) is also an actual LND. One direct justification
uses an invariant indeterminate \(u\): on \(B[u,u^{-1}]\), the
actual conjugate \(u\exp(E/u)T\exp(-E/u)=uT-Q\) is an LND.
It preserves \(B[u]\), so its restriction and then its quotient
at \(u=0\) give the LND \(-Q\). No arbitrary commuting rational
field is declared locally nilpotent here.

## 2. Nonzero angular derivative without parameter regularity

Define
\[
\tau_p=Tp,\qquad \tau_q=Tq,\qquad
\omega=p\tau_q-q\tau_p.
\tag{5}
\]
We first prove \(\omega\ne0\) directly. If it were zero,
coprimality in the actual UFD \(B\) would give \(p\mid Tp\)
and \(q\mid Tq\). Degree in the original variable \(w\)
forces both derivatives to vanish: any nonzero \(w\)-derivative
has strictly smaller \(w\)-degree than the original polynomial.
But at least one of \(p,q\) is then a nonconstant polynomial killed
by both \(E\) and the nonzero constant partial \(T\), contrary to the supplied
nonlinear-cone omission theorem. Hence
\[
\omega\ne0,\qquad \zeta=q/p\in K\setminus\mathbb C,
\qquad T\zeta=\omega/p^2.
\tag{6}
\]
This proves the required nonzero angular derivative without the
independent-parameter hypothesis used in the
[binary Euler reduction](binary-euler-reduction-pass78.md).
It uses the original partial and actual polynomial coprimality,
not a regularity assertion on \(\partial_p\) or \(\partial_q\).

## 3. The complete determinant and its sign

Put \(f(\zeta)=h(1,\zeta)\), viewed as a three-entry polynomial
column, and write \(\rho=p^e\). Homogeneity gives
\(P_{\rm tr}=\rho f(\zeta)\). Applying the original derivation
\(T\) twice in the field gives the exact columns
\[
\begin{aligned}
T(P_{\rm tr})
 &= (T\rho)f+\rho(T\zeta)f',\\
T^2(P_{\rm tr})
 &= (T^2\rho)f+
       \bigl(2(T\rho)(T\zeta)+\rho T^2\zeta\bigr)f'
       +\rho(T\zeta)^2f''.
\end{aligned}
\tag{7}
\]
All primes in this section are ordinary derivatives of the one-variable
polynomials \(f_i\). No lower term has been dropped before taking
the determinant.

Use the original coordinate order \((x_1,x_2,x_3,w)\) and the
column order \((P,e_4,Q(x),Z(x))\). Expansion along the second
column has sign \((-1)^{4+2}=+1\). Multilinearity applied to (7)
therefore gives
\[
\begin{aligned}
\det\bigl(P,e_4,Q(x),Z(x)\bigr)
 &=\det\bigl(P_{\rm tr},TP_{\rm tr},T^2P_{\rm tr}\bigr)\\
 &=\rho^3(T\zeta)^3\det(f,f',f'')\\
 &=p^{3e-6}\omega^3\mathcal W(\zeta),\qquad
\mathcal W(t)=\det(f(t),f'(t),f''(t)).
\end{aligned}
\tag{8}
\]
The constant linear independence of the homogeneous \(h_i\)
implies that the three polynomials \(f_i(t)=h_i(1,t)\) are
linearly independent. Their polynomial Wronskian \(\mathcal W\)
is nonzero. For an elementary proof, replace them by a constant
invertible linear combination having distinct increasing degrees
\(d_1<d_2<d_3\). The leading determinant coefficient is the
product of their leading coefficients times the nonzero
Vandermonde product \(\prod_{i<j}(d_j-d_i)\), at degree
\(d_1+d_2+d_3-3\). An invertible constant row change only
multiplies the determinant by a nonzero constant.

Since \(\zeta\) is nonconstant in a complex field extension,
it is transcendental over \(\mathbb C\); hence
\(\mathcal W(\zeta)\ne0\). The other factors in (8) are
nonzero by (2) and (6). We conclude
\[
\boxed{\operatorname{rank}_K(E,T,Q,[T,Q])=4.}
\tag{9}
\]
Equation (8) is an equality in \(K\), with its left side an
actual polynomial. It neither asserts that the displayed factors
are units nor excludes their vanishing on the parameter zero scheme.

## 4. The exact preimage and nonparallel second iterate

In particular \(Q(x)\ne0\). Equations (3)--(4) and the
partition \((3,1)\) show
\(KQ(x)=\operatorname{im}J\cap\ker J=\operatorname{im}J^2\).
The inverse image of this line under \(J:K^4\to K^4\) has
dimension \(2+1=3\). It contains \(\operatorname{im}J\) and
\(P\); (3) makes their sum three-dimensional. It also contains
\(P,e_4,Q(x)\), which are independent by (9), since
\(JP=JQ(x)=0\) and \(Je_4=Q(x)\). Thus the precise equality is
\[
J^{-1}(KQ(x))
 =KP+\operatorname{im}J
 =\operatorname{span}_K\{P,e_4,Q(x)\}.
\tag{10}
\]
Here \(J^{-1}\) denotes the full inverse image of a subspace,
not an inverse matrix. In derivation notation the last space is
\(\operatorname{span}_K\{E,T,Q\}\).

Differentiate \(JQ(x)=0\) by the original constant partial.
Ordinary mixed coordinate derivatives commute, so
\(TJ=\operatorname{Jac}Q(x)\). Consequently
\[
JZ(x)=-(TJ)Q(x)
      =-(\operatorname{Jac}Q(x))Q(x)
      =-Q^2(x).
\tag{11}
\]
If \(Q^2(x)\) belonged to \(KQ(x)\), equation (11) would
place \(Z(x)\) in the three-dimensional space (10), contrary
to (9). Therefore
\[
\boxed{Q^2(x)\notin KQ(x).}
\tag{12}
\]
In particular \(Q^2(x)\ne0\), so the actual derived LND is
not nice in this original frame. The assertion is stronger than
nonvanishing of one second iterate, but makes no claim about
\(Q^3(x)\), a supplied-slice adjustment, primitive division or
niceness after another polynomial coordinate change.

## 5. The retained conic seed attains the determinant identity

In the original coordinates \((x,y,z,w)\), the already retained
nice sliced action has
\[
\begin{gathered}
a=xz-y^2+w,\qquad
P=(1,a,a^2,-a^2x+2ay-z)^t,\qquad T=\partial_w,\\
p=1,\quad q=a,\quad h=(p^2,pq,q^2),\quad
\omega=1,\quad \mathcal W=2,\\
\det(P,e_4,Q(x),Z(x))=2,\qquad Q^2(x,y,z,w)=(0,0,0,2)^t.
\end{gathered}
\tag{13}
\]
Here \(Q(x)=(0,1,2a,-2ax+2y)^t\) and
\(Z(x)=(0,0,2,-2x)^t\), so both calculations in (13) follow
directly. This explicitly includes dependent binary parameters and
a unit parameter ideal, unlike the separate proper-parameter Euler
reduction.

For the actual action and inverse, put \(u=y-xa\) and
\(v=z-xa^2\). The coordinates \((x,a,u,v)\) have inverse
\(y=u+xa\), \(z=v+xa^2\),
\(w=a-xv+u^2+2xau\), and \(E=\partial_x\) in them.
This is the recognized conic seed from
[pass74](nice-slice-adjoint-rank-pass74.md), not a newly constructed
family or an example of a primitive fixed point. Its third derived
iterate happens to vanish, but (13) supplies no universal third-
iterate conclusion.

## 6. Verification and the remaining boundary

The proof was reconstructed from the actual hypotheses and the
selected predecessor statements above. Its determinant computation,
Wronskian argument and three-dimensional inverse-image calculation
are written in full. On the independent-parameter part of this
branch, the binary Euler note gives a compatible generic factorization
of \(J^2\); no regularity at \(p=q=0\) is imported from that
calculation. The present theorem covers the full supplied-good
nonlinear ternary-cone branch of the binary descent theorem, but
does not classify actions outside those precise hypotheses.

The original-slice distinction remains essential in (3). A local
slice without local nilpotence of the coordinate partial would
not supply the vertical exclusion used there. The generic rank-four
conclusion does not settle the primitive intrinsic fixed locus,
and the non-nice conclusion does not answer the separate universal
third-iterate question. No numerical suite, historical novelty,
human expert review, formal proof certificate or general cancellation
claim is made. All files through pass77 and shared metadata remain
unchanged.
