# A global invariant coordinate in the nonzero-s, zero-r cusp branch

Status: complete working proof with separate saved-source AI reviews of
this note and both coefficient and field-forcing inputs. This is not
human expert review or proof-assistant verification.
The construction below treats the actual cusp branch \(k_\rho=0\),
\(n_\rho\ne0\). It returns a coordinate to the original polynomial
four-ring, including the genuinely quadratic coefficient cover
exhibited in171. It neither assumes that this cover is trivial nor
that the selected intrinsic derivation has a global slice.

## 1. Exact hypotheses and coefficient inputs

Retain the complete actual sliced cusp setup159:
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),
\qquad\ker\theta_0=(XZ-Y^3).
\tag{1}
\]
The initial ideal is the full weighted initial kernel. Let
\(N=[u^3](\partial_Z|_A)\), \(L=\operatorname{Frac}(\ker_A N)\),
and retain \(A_L=L[v]\), \(Nv=1\). Write \(a_E=EX\ne0\),
\(t=EY/a_E\), and \(\rho=(E^2W/2)/a_E^2\).
The variables \(t,\rho\) are independent over \(\mathbb C\), and
\(L/\mathbb C(t,\rho)\) is finite separable.

Assume \(k_\rho=0\) and \(s=n_\rho\ne0\).
The actual zero-r reduction160 gives an affine parameter \(y\)
for \(L[v]\) and the chart
\[
\begin{gathered}
Y=y+tX,\qquad
Z=n+3ty^2+k'y+(3t^2y+k)X+t^3X^2,\\
W=R(y)+P(y)X+\rho X^2,\qquad
L(y)=\operatorname{Frac}A=\mathbb C(y,z,w),\\
z=n+3ty^2+k'y,\qquad w=R(y).
\end{gathered}
\tag{2}
\]
Here the coefficient derivatives of \(k\) agree with the derivative
on \(K=\ker_L\partial_\rho\). This field is finite over
\(\mathbb C(t)\) and has exact derivative-constant field
\(\mathbb C\). No assertion \(K=\mathbb C(t)\) is needed.

Use the [coefficient normal form173](cusp-zero-r-coefficient-normal-form-pass173-working.md)
and the [field-forcing proof173](cusp-zero-r-field-forcing-pass173-working.md).
Their conclusions needed here are as follows. A prime now denotes
the extension of differentiation on \(K\) that fixes \(n\):
\[
\begin{gathered}
L=K(n),\quad k\in K,\quad
\rho=a n^2+b n+c,\quad a\in\mathbb C,\ b,c\in K,\quad
q=2an+b\ne0,\quad h=k''/2,\\
F(U)=U^3+hU^2,\qquad
P(U)=\rho' U-qF(U)+m,\\
m=-\frac{2a}{3}h'n^2+M_1n+M_0,\qquad
a h''=0,\qquad M_1,M_0\in K,\\
R(U)\in K[n,U],\qquad
[n^2]R(U)=\gamma:=a(h')^2/9\in\mathbb C,\qquad
\delta_U R(U)=g_0'\in K^*,\\
\delta_U:=\partial_t-F_U(U)\partial_n,\qquad
g_0\in K,\qquad K=\mathbb C(g_0).
\end{gathered}
\tag{3}
\]
In particular \(R\) has degree at most two in \(n\). The nonvanishing
of \(g_0'\) is the nonzero constant determinant after the field-forcing
step. The construction below only needs \(g_0\in K\), not the final
rationality assertion in (3).

The same normal form retains the two exact polynomial identities
\[
R_U=\delta_U P,\qquad
\delta_U\rho=P_U.
\tag{4}
\]
The second follows directly from the displayed formula for \(P\):
\(P_U=\rho'-qF_U\) and \(\partial_n\rho=q\).
All these identities hold over the exact coefficient field.
In particular the field-forcing input, not a choice of antiderivative,
has made \(\delta_U R\) independent of \(n\).

## 2. A coefficient derivation fixing the first three original coordinates

On \(K(n,y,X)\), extend \(\partial_t\) to fix \(n,y,X\), and put
\[
\mathcal T=\partial_t-X\partial_y-F_U(y)\partial_n.
\tag{5}
\]
This is a derivation of the field. It is not asserted to be locally
nilpotent or a polynomial derivation of the original ring.
The actual coordinates in (2) satisfy
\[
\mathcal T X=\mathcal T Y=\mathcal T Z=0,\qquad
\mathcal T W=g_0'.
\tag{6}
\]
For \(Y\) this is \(X-X=0\). For \(Z\), before the last term of
(5) is applied, direct differentiation gives
\[
(\partial_t-X\partial_y)Z=3y^2+k''y=F_U(y),
\qquad \partial_n Z=1.
\]
This proves its asserted vanishing, without any condition on the
ordinary degree of \(k\) in \(t\).

For \(W\), write \(\delta=\partial_t-F_U(y)\partial_n\).
Equations (2) and (4) give the entire cancellation
\[
\begin{aligned}
\mathcal T W
 &=\delta R+X\delta P+X^2\delta\rho-XR_y-X^2P_y\\
 &=\delta R=g_0'.
\end{aligned}
\tag{7}
\]
Thus every polynomial in the original \(X,Y,Z\) is killed by
\(\mathcal T\). This fact is the reason the corrections below
can be returned to the original coordinate ring.

## 3. Remove the quadratic n coefficient using an original polynomial

If \(a\ne0\), the identity \(a h''=0\) and the exact constant
field imply \(h'=u_0\in\mathbb C\). Set \(\lambda=u_0/3\).
If \(a=0\), set \(\lambda=0\); this choice does not assume
that \(h'\) is constant in that branch.
In either case \(\lambda\in\mathbb C\), and (2)--(3) give
\[
[n^2]W
 =\gamma-\frac{2a}{3}h'X+aX^2
 =a(X-\lambda)^2,\qquad [n]Z=1 .
\tag{8}
\]
Here the \(n^2\) coefficient of \(P\) is \(-2a h'/3\), since
\(a'=0\); its other displayed terms have degree at most one in \(n\).

Therefore the actual polynomial
\[
J_*=W-a(X-\lambda)^2Z^2\in B
\tag{9}
\]
has degree at most one in \(n\) in the exact chart:
\[
J_*=\mathcal A(X,y)n+\mathcal B(X,y),
\qquad \mathcal A,\mathcal B\in K[X,y].
\tag{10}
\]
This is an identity in independent variables over \(K\), not a
comparison in a field where \(n\) might be algebraic over \(K\).
The normal-form theorem establishes that \(n\) is transcendental
over \(K\), and \(X,y\) are independent over \(L\).

Since \(\mathcal T\) fixes \(X,Z\), equations (6) and (9) yield
\(\mathcal T J_*=g_0'\). The coefficient of \(n\) in (10)
therefore satisfies
\[
(\partial_t-X\partial_y)\mathcal A=0.
\tag{11}
\]
The additional term \(-F_U(y)\partial_n J_*\) has no \(n\)
coefficient, which is essential for this comparison.

Substitute \(y=Y-tX\) and define
\[
A_0(X,Y):=\mathcal A(X,Y-tX).
\]
It is a polynomial in \(X,Y\) with coefficients in \(K\).
Holding \(X,Y\) fixed, the derivative of each coefficient
vanishes by (11). Exactness of the constant field gives
\[
A_0(X,Y)\in\mathbb C[X,Y].
\tag{12}
\]
This argument proves complex polynomial coefficients; it is not
an assertion that an arbitrary rational generic correction descends.

## 4. Remove the remaining n coefficient and finish the descent

Set \(J_{**}=J_*-A_0(X,Y)Z\). This belongs to \(B\), and its
coefficient of \(n\) vanishes by (10)--(12) and \([n]Z=1\).
Consequently
\[
J_{**}=g_0+\mathcal Q(X,y),\qquad \mathcal Q\in K[X,y].
\tag{13}
\]
The right side only uses the equality of fields for its
description; the left side is already an original polynomial.
By (6), \(\mathcal T J_{**}=g_0'\). Since \(\mathcal Q\)
is independent of \(n\), this says
\[
(\partial_t-X\partial_y)\mathcal Q=0.
\]
The identical coefficient argument from Section 3 gives
\[
Q_0(X,Y):=\mathcal Q(X,Y-tX)\in\mathbb C[X,Y].
\tag{14}
\]
It follows that
\[
I=W-a(X-\lambda)^2Z^2-A_0(X,Y)Z-Q_0(X,Y)
  =g_0\in A\cap L .
\tag{15}
\]
Indeed \(I\in B\) by construction, and \(E\) kills \(g_0\in L\).
The equality holds in a common fraction field, so \(EI=0\)
holds in the domain \(B\). No denominator from a projected
coordinate has been declared a global unit.

The inverse is explicitly polynomial:
\[
W=I+a(X-\lambda)^2Z^2+A_0(X,Y)Z+Q_0(X,Y),
\qquad B=\mathbb C[X,Y,Z,I].
\tag{16}
\]
Both composition orders are immediate with \(X,Y,Z\) fixed.
In particular \(I\) is a nonconstant actual ambient coordinate,
not merely an invariant with a nonzero differential.
The case \(a=0\) has the same inverse with the quadratic term absent.

## 5. Recognition and limits

Now \(E\) is a nonzero \(\mathbb C[I]\)-linear LND on
\(B=\mathbb C[I]^{[3]}\). Its kernel \(A\simeq B/(u)\) is
regular: the identity \(Eu=1\) expresses one as a polynomial
combination of the partial derivatives of \(u\), so its zero
hypersurface is smooth over \(\mathbb C\).
Bhatwadekar--Gupta--Lokhande Theorem 3.5 therefore gives
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.
\tag{17}
\]
The exact theorem statement and its displayed proof were freshly
checked in the primary paper. It is an imported published theorem,
not a new proof or a claim of formal certification.

This recognizes the stated actual branch \(r=0,\ n_\rho\ne0\),
subject to the coefficient and field-forcing proofs cited above.
It does not exclude the actual quadratic-cover example171;
that example is included and already has a polynomial kernel.
Combining with the separate zero-second-coefficient exclusion172
would cover the zero-r branch of this cusp chart. It does not
cover the nonzero-r, constant-y branch, other initial configurations,
or arbitrary coordinate entry into the cusp setup.

## Sources and verification boundary

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md) and [zero-r generic reduction160](cusp-zero-r-generic-graph-pass160-working.md).
2. [Coefficient normal form173](cusp-zero-r-coefficient-normal-form-pass173-working.md) and [field forcing173](cusp-zero-r-field-forcing-pass173-working.md), with their exact hypotheses.
3. [Square-root boundary171](cusp-zero-r-square-root-actual-boundary-pass171-working.md), a positive actual boundary, not an exclusion.
4. [Zero-r constant-projection exclusion172](cusp-zero-r-constant-projection-exclusion-pass172-working.md), separate from this construction.
5. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]](https://arxiv.org/html/1501.01438v1), Theorem 3.5.

The new descent proof is algebraic and includes an original-ring
inverse. Finite symbolic checks do not prove all its coefficient
inputs or the published endpoint. There is no human expert review,
proof-assistant verification, recursive dependency certification,
or historical novelty clearance. All172 and earlier mathematical
artifacts are unchanged.
