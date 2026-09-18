# The first two negative Taylor coefficients in a dense chart

The negative Taylor tail supplies a nonzero polynomial equation for
the generic embedded line, followed by an explicit polynomial slice
for its intrinsic derivative. The respective degree bounds are
\(m+1\) and \(m+2\), where \(m\) is the original bad coordinate's
degree in the fixed good slice coordinate.

This is a consequence of the exact chart and formal-annihilation
premises below. It does not construct an original polynomial inverse,
descend a coefficient-field equation to complex coefficients, or
recognize an arbitrary sliced fourfold.

## 1. Exact premises and the formal Laurent ring

Use the actual dense-chart construction139, with the following
specific conclusions as inputs.[^1] Its characteristic-zero coefficient
field \(L\) has commuting derivations
\(\partial_\tau,\partial_\rho\); in that construction it is finite
separable over \(\mathbb C(\tau,\rho)\). Put
\[
\begin{gathered}
F=L(v),\qquad y,z\in L[v],\qquad N'=\partial_v,\qquad
\ker(\partial_v|_F)=L,\\
T=D_0+X D_1+X^2\partial_v,\qquad T(X)=0,\qquad
W\in L[v][X],\quad \deg_X W=m\ge0,\quad T(W)=1 .
\end{gathered}
\tag{1}
\]
Here \(X\) is transcendental over \(F\), and \(D_0,D_1\) are
derivations of \(F\). The coefficient derivatives on \(L\) extend
to \(F\) by fixing \(v\). We do not assume that \(T\) preserves
\(L\), or that any of its displayed coefficient derivations preserve
\(L\).

Work in \(F((X^{-1}))\), the formal Laurent series with exponents of
\(X\) bounded above. The operator in (1) extends coefficientwise
to this ring. Each output coefficient uses at most three input
coefficients, and multiplication by \(X^2\) shifts order by a fixed
finite amount. All operations below are formal; no analytic
convergence is involved.

For \(f\in L\), define its Taylor series and homogeneous pieces by
\[
\begin{gathered}
\Theta(f)=\sum_{d=0}^{\infty}H_d(f;y,z)X^{-d},\\
H_d(f;U,V)=
\sum_{\substack{a,b\ge0\\a+b=d}}
\frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}\,U^aV^b
\in L[U,V],\qquad H_0(f)=f .
\end{gathered}
\tag{2}
\]
The variables \(U,V\) in the second line are independent formal
polynomial variables. They are evaluated at \(y,z\) only where
explicitly indicated.

Two further inputs are the exact annihilation and peeling identities:
\[
T\Theta(f)=0\quad(f\in L),\qquad
f_0,\ldots,f_m\in L,\qquad
\mathscr S=\sum_{j=0}^m X^j\Theta(f_j),\qquad
W=(\mathscr S)_{\ge0}.
\tag{3}
\]
The last operation retains the nonnegative powers of \(X\), after
evaluation at \(y,z\). These identities, including their signs,
are established by the separate actual-chart argument. In
particular, polynomiality of arbitrary coefficients or realizability
of formal Taylor data is not being inferred here.

The tail proof itself needs only (1)--(3). The finite extension
description of \(L\) explains the geometric input, but is not an
additional ingredient in the algebraic argument.

## 2. The first tail coefficient is an actual relation

Set
\[
\begin{gathered}
\mathscr R=W-\mathscr S
=-\sum_{j=0}^m\sum_{d>j}
H_d(f_j;y,z)X^{j-d},\qquad T\mathscr R=1,\\
R_1(U,V)=-\sum_{j=0}^m H_{j+1}(f_j;U,V),\qquad
[X^{-1}]\mathscr R=R_1(y,z),\qquad
\deg R_1\le m+1 .
\end{gathered}
\tag{4}
\]
The tail has no nonnegative powers of \(X\).
Its \(X^1\) coefficient after applying \(T\) is therefore exactly
\(\partial_v R_1(y,z)\): the terms \(D_0\) and \(XD_1\)
cannot reach that exponent. Since \(T\mathscr R=1\), this coefficient
vanishes. Thus
\[
R_1(y,z)=f_{-1}\in L,\qquad
Q(U,V):=R_1(U,V)-f_{-1},\qquad
Q(y,z)=0,\qquad \deg Q\le m+1 .
\tag{5}
\]
It remains essential to prove that \(Q\) is not the zero formal
polynomial. Evaluation at \(y,z\) is not injective, and will not
be treated as such.

Suppose \(Q=0\) in \(L[U,V]\). Every term of \(R_1\) has positive
degree, so its constant coefficient gives \(f_{-1}=0\), and
\(R_1=0\). Its homogeneous part of degree \(j+1\) is precisely
\(-H_{j+1}(f_j;U,V)\), with no contribution from a different
index. Independence of formal monomials, together with characteristic
zero, yields
\(\partial_\tau^a\partial_\rho^b f_j=0\) for every \(a+b=j+1\).

All higher mixed derivatives of \(f_j\) then vanish. Indeed any
higher multi-index contains one of total order \(j+1\), and the
two coefficient derivations commute. Thus \(\Theta(f_j)\)
truncates after order \(j\). Each \(X^j\Theta(f_j)\) has only
nonnegative powers, so (3) gives \(W=\mathscr S\).
But \(T\mathscr S=0\) by (3), contradicting \(T(W)=1\).
Consequently \(Q\ne0\).

This argument includes \(m=0\). Then
\(R_1=-f_{0,\tau}U-f_{0,\rho}V\); a formally zero relation
would make \(\Theta(f_0)=f_0=W\) invariant under \(T\), giving
the same contradiction. No division by \(m\) or a positive-degree
assumption is used.

## 3. The next coefficient is a polynomial intrinsic slice

Subtract the entire annihilated Taylor term of the first coefficient:
\[
\begin{gathered}
\mathscr R^{(2)}=\mathscr R-X^{-1}\Theta(f_{-1}),\qquad
T\mathscr R^{(2)}=1,\qquad
\mathscr R^{(2)}\in X^{-2}F[[X^{-1}]],\\
R_2(U,V)=
-\sum_{j=0}^m H_{j+2}(f_j;U,V)
-H_1(f_{-1};U,V),\\
[X^{-2}]\mathscr R^{(2)}=R_2(y,z),\qquad
\deg R_2\le m+2 .
\end{gathered}
\tag{6}
\]
The cancellation of the \(X^{-1}\) coefficient uses the evaluated
identity in (5), not a formal polynomial identity in \(U,V\).
The correction term in \(R_2\) has the explicit negative sign
\(-f_{-1,\tau}U-f_{-1,\rho}V\).

Because the adjusted tail begins at exponent \(-2\), the constant
coefficient of \(T\mathscr R^{(2)}\) comes only from
\(X^2\partial_v\) acting on that first coefficient. Therefore
\[
\partial_v R_2(y,z)=1,\qquad
R_2(y,z)=v+c\quad(c\in L),\qquad
L[y,z]=L[v].
\tag{7}
\]
For the middle equality, subtract \(v\) and use
\(\ker(\partial_v|_F)=L\). For the last one,
\(R_2(y,z)\in L[y,z]\) puts \(v\) in that ring. The opposite
inclusion uses the initial actual-chart membership \(y,z\in L[v]\).

That membership matters. A rational parametrization alone would
not rule out extra functions with poles in \(L[y,z]\). Here the
polynomial slice explicitly recovers the whole generic affine
line. The chart's preceding polynomial-coefficient argument also
gives this equality; the tail supplies an independent recovery
with an explicit degree-bounded slice.

## 4. Embedded-line equation and its residual factor

The evaluation map now has image \(L[v]\), so
\[
L[U,V]\longrightarrow L[v],\quad (U,V)\longmapsto(y,z),
\qquad
\ker=(P),\quad P\text{ irreducible},\qquad
1\le\deg P\le m+1 .
\tag{8}
\]
Its kernel is a height-one prime in the two-variable polynomial
ring over \(L\), hence principal. The nonzero polynomial \(Q\)
in (5) belongs to it. Since total degree adds under multiplication
of nonzero polynomials over a field, \(P\mid Q\) gives the bound.
No assertion that \(Q\) itself is irreducible is needed.

The two tail polynomials satisfy a useful formal differential identity.
Differentiate the homogeneous Taylor polynomials in (2) term by term:
\[
\partial_U H_{d+1}(f;U,V)=H_d(\partial_\tau f;U,V),\qquad
\partial_V H_{d+1}(f;U,V)=H_d(\partial_\rho f;U,V).
\quad
(R_{2,U},R_{2,V})=(Q_\tau,Q_\rho).
\tag{9}
\]
On the right, the coefficient derivatives fix \(U,V\).
The last equality includes the derivatives of \(f_{-1}\), with
the signs from (5)--(6).

Differentiate \(Q(y,z)=0\) in the coefficient directions, holding
\(v\) fixed, and combine the results with
\(\partial_v R_2(y,z)=1\). This gives
\[
\begin{aligned}
1={}&-Q_U(y,z)\bigl(y_\tau y_v+y_\rho z_v\bigr)
      -Q_V(y,z)\bigl(z_\tau y_v+z_\rho z_v\bigr),\\
Q=PH\quad&\Longrightarrow\quad H(y,z)\in L[v]^*=L^* .
\end{aligned}
\tag{10}
\]
Every displayed coefficient in the first line belongs to \(L[v]\):
the coefficient derivations preserve that polynomial ring because
they fix \(v\). Thus the ideal generated by the two evaluated
partial derivatives of \(Q\) is the unit ideal in \(L[v]\).
If \(Q=PH\), then \(P(y,z)=0\) gives
\(Q_U(y,z)=H(y,z)P_U(y,z)\), and similarly for \(V\).
The first line of (10) makes \(H(y,z)\) a unit, proving the
second.

In particular the exact kernel generator \(P\) occurs in \(Q\)
with multiplicity one. This does not make \(H\) constant in
\(L[U,V]\): a nonconstant polynomial can restrict to a constant
unit on the embedded line. Nor does it prove that \(Q\) is a
plane coordinate. No plane-embedding classification is used.

## 5. Exact scope

Thus the actual generic embedded line has both a bounded-degree
equation and a bounded-degree polynomial expression for its
intrinsic parameter. This does not make \(P\), \(R_2\), or \(c\)
complex polynomials in the original coordinate ring. The
coefficient field can be a nontrivial finite algebraic extension,
and no polynomial generator for it has been asserted.

Neither a global invariant coordinate nor a cancellation conclusion
follows from these tail statements alone. In particular, the
formal relation has not been replaced by a selected factor over
a larger field, and no denominator has been silently removed.

## Sources

1. [Dense all-degree Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md).
   Actual localized polynomial membership, selected partial
   normalization, exact Taylor annihilation, and nonnegative-part
   peeling. Those are the premises of this tail argument.

The proof after the stated premises is complete and uses no
additional external theorem beyond elementary polynomial-ring
and derivation facts. No historical novelty claim is made.

[^1]: [Actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
    the localized coefficient-field, formal-annihilation and
    peeling constructions.
