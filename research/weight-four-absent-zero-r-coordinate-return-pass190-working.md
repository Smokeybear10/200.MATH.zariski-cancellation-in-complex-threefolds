# Conditional original-ring coordinate return in the absent-variable zero-R branch

Status: working conditional coordinate-return proof. The coefficient gates
listed below are additional inputs, not conclusions imported from189.
The construction is in the original polynomial four-ring and has an
explicit polynomial inverse. It does not by itself prove that every
zero-R chart meets the gates, or recognize the nonzero-R branch.

## 1. Actual setup and the exact additional gates

Retain the full actual setup and zero-R conclusions of
[reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md)
and [cover-collapse189](weight-four-absent-zero-r-cover-collapse-pass189-working.md).
In particular,
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\mathcal A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4),\\
L=K(n),\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\qquad
\rho=bn+c,\quad b\in\mathbb C^*,\quad c,k\in K.
\end{gathered}
\tag{1}
\]
Here \(b\) is the constant coefficient-cover slope, not \(EY\).
The elements \(n,y,X\) are algebraically independent over \(K\).
The derivative \(\partial_t\) on \(K(n)(y,X)\) extends that on \(K\)
and fixes \(n,y,X\). Primes on coefficients refer to this derivative.
The original LND acts in the actual chart as \(E=a_E\partial_X\),
fixing \(K(n,y)\), with \(a_E=EX\ne0\). No original-ring unit
assumption is made about \(a_E\).

Put
\[
h=k''/2,\qquad F(U)=4tU^3+hU^2,\qquad
\delta_U=\partial_t-F_U(U)\partial_n .
\tag{2}
\]
The actual coordinate expressions are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=n+6t^2y^2+k'y+(4t^3y+k)X+t^4X^2,\\
W&=\mathcal W(y)+P(y)X+\rho X^2.
\end{aligned}
\tag{3}
\]
The exact identities retained from189 are
\[
\begin{gathered}
P=\rho' U-bF+M,\qquad M=M_1n+M_0,\qquad M_1,M_0\in K,\\
\mathcal W
=-bU^4-\frac{bh'}3U^3+\frac{c''}2U^2
 +(M_1'n+M_0')U-M_1F+W_0,\\
\mathcal W_U=\delta_U P,\qquad
\delta_U\mathcal W\in L^*,\qquad
\delta_U\rho=P_U.
\end{gathered}
\tag{4}
\]
Scalarity here means independence of \(U\); initially the scalar
may depend on \(n\). The last identity follows directly from
\(P_U=c'-bF_U\).

The additional coefficient gates for this lemma are exactly
\[
M_1=\alpha t+\beta,\qquad
W_0=Dn+g_0,\qquad
\alpha,\beta,D\in\mathbb C,\quad g_0\in K.
\tag{5}
\]
No rationality assertion \(K=\mathbb C(t)\) or \(K=\mathbb C(g_0)\)
is required. No separate ordinary-degree formula for \(h\) is needed.
In particular, this note does not assume the other proposed
coefficient-normal-form formulas merely because they would be
compatible with (5).

Since \(F_U(0)=0\), evaluation of the scalar identity in (4) at
\(U=0\) gives
\[
\delta_U\mathcal W=g_0'\in K^*.
\tag{6}
\]
Here \(D'=0\) is essential. Without that gate the value would be
\(D'n+g_0'\), and the argument below would not have its stated form.

## 2. A field derivation with exact original-coordinate identities

Define on \(K(n)(y,X)\)
\[
\mathcal T=\partial_t-X\partial_y-F_U(y)\partial_n .
\tag{7}
\]
This is only asserted to be a field derivation. It is not assumed
to be locally nilpotent or polynomial on the original ring.
Direct differentiation of (3) gives
\[
\mathcal T X=\mathcal T Y=\mathcal T Z=0,\qquad
\mathcal T W=g_0'.
\tag{8}
\]
For \(Z\), the complete cancellation is
\[
(\partial_t-X\partial_y)Z=12ty^2+k''y=F_U(y),
\qquad \partial_n Z=1.
\]
The coefficients of \(X\) and \(X^2\) cancel separately. In particular,
this computation uses the actual \(t^4X^2\) term, not a cusp formula.

Writing \(\delta=\partial_t-F_U(y)\partial_n\), the calculation for
\(W\) uses all three identities in (4):
\[
\begin{aligned}
\mathcal T W
 &=\delta\mathcal W(y)
   +X\{\delta P(y)-\mathcal W_U(y)\}
   +X^2\{\delta\rho-P_U(y)\}\\
 &=g_0'.
\end{aligned}
\tag{9}
\]
The expressions in braces are zero over the exact coefficient field.

## 3. Remove the n coefficient by an actual polynomial shear

Equation (4) and the gates (5) show that \(W\) has degree at most
one in the independent \(n\), with
\[
[n]W
 =bX^2+(\alpha t+\beta)X+\alpha y+D
 =bX^2+\beta X+\alpha Y+D
 =:A_0(X,Y)\in\mathbb C[X,Y].
\tag{10}
\]
Also \([n]Z=1\). Consequently the already original polynomial
\[
I_*=W-A_0(X,Y)Z\in B
\]
satisfies
\[
Q(X,y):=I_*-g_0\in K[X,y],\qquad
(\partial_t-X\partial_y)Q=0.
\tag{11}
\]
There is no hidden denominator removal in this conclusion: the
coefficient of \(n\) cancels literally, all other chart coefficients
belong to \(K\), and \(\mathcal T I_*=g_0'\) by (8).

Now substitute \(y=Y-tX\). Holding \(X,Y\) fixed gives
\[
Q_0(X,Y):=Q(X,Y-tX)\in K[X,Y],\qquad
\partial_tQ_0=0.
\]
Comparison of the independent monomials \(X^iY^j\), followed by
\(\ker_K\partial_t=\mathbb C\), proves
\[
Q_0(X,Y)\in\mathbb C[X,Y],\qquad
I:=W-A_0(X,Y)Z-Q_0(X,Y)=g_0.
\tag{12}
\]
This is coefficient transport, not the assertion that a generic
rational coordinate automatically descends. It also does not assume
in advance that \(\mathcal T/g_0'\) is the original \(\partial_W\).

Since \(I\in B\) and \(g_0\in L\subset\operatorname{Frac}\mathcal A\),
the equality in the common fraction field implies \(EI=0\) in the
domain \(B\). The polynomial map and inverse are
\[
\begin{aligned}
(X,Y,Z,W)&\longmapsto
 (X,Y,Z,\ W-A_0(X,Y)Z-Q_0(X,Y)),\\
(X,Y,Z,I)&\longmapsto
 (X,Y,Z,\ I+A_0(X,Y)Z+Q_0(X,Y)).
\end{aligned}
\tag{13}
\]
Both compositions cancel term by term with \(X,Y,Z\) fixed.
Thus \(B=\mathbb C[X,Y,Z,I]\), and \(I\) is a nonconstant actual
invariant ambient coordinate. This conclusion does not require
the projected coordinate \(g_0\) to have been known polynomial.

## 4. Conditional recognition and its boundary

The original derivation is now a nonzero
\(\mathbb C[I]\)-linear LND of \(\mathbb C[I]^{[3]}\).
Its kernel \(\mathcal A\) is regular because
\(\mathcal A\simeq B/(u)\) and \(Eu=1\): writing \(E\) in original
coordinate partials expresses one as a polynomial combination of
the four partial derivatives of \(u\). The hypersurface \(u=0\)
is therefore smooth.

Bhatwadekar--Gupta--Lokhande Theorem 3.5 applies and yields
\[
\mathcal A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.
\tag{14}
\]
The primary statement and its displayed proof were freshly checked:
[Some K-theoretic properties of the kernel of a locally nilpotent
derivation on \(k[X_1,\ldots,X_4]\)](https://arxiv.org/html/1501.01438v1),
Theorem 3.5. This is a published input with its actual invariant
coordinate and regular-kernel hypotheses supplied above.

This recognizes the zero-R branch only when the additional gates
(5) are established. Their proof is separate; they are not contained
in the frozen189 cover-collapse conclusion. The earlier
[cusp return173](cusp-zero-r-global-coordinate-pass173-working.md)
was read as a template, but every needed identity here was recomputed
for \(q=t^4\). No cusp coefficient formula is imported.

The note does not recognize the nonzero-R branch, prove arbitrary
entry into the supplied frame, solve unrestricted cancellation,
or certify historical novelty. No checker was executed, imported or
compiled. All189 and earlier artifacts are unchanged. This is not
human expert review or proof-assistant verification.

