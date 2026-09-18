# A formal extra branch can change the base speed ratio

The coefficient field can equal the tail-generated field, and an
extra active component can have no enlarged algebraic constants,
without that component being the selected one. The missing condition
is that source substitution must fix the two speed ratios.

The example below satisfies the full formal Taylor and determinant
system. It is not an actual polynomial-coordinate frame: its original
Jacobian is nonconstant and its target function field has index two.
It refutes a formal shortcut, not cancellation or actual primitivity.

## 1. Polynomial source tuple and exact normalization

Let \(a,\rho,q,X\) be independent over \(\mathbb C\). Define
\[
\begin{gathered}
L=K=\mathbb C(a,\rho),\qquad \tau=a,\qquad v=-2a q,\\
y=q=-v/(2a),\qquad z=a,\qquad w_0=-2a\rho,\\
Y=q+aX,\qquad Z=a+\rho X,\qquad
W=-2a\rho-\rho^2X,\\
\mathbb C(y,z,w_0)=\mathbb C(q,a,\rho)=L(v),\qquad
L[y,z]=L[v].
\end{gathered}
\tag{1}
\]
The source-field equality follows from
\(q=y,\ a=z,\ \rho=-w_0/(2z)\).
There is no polynomial source-ring equality with
\(\mathbb C[q,a,\rho]\): recovering \(\rho\) requires dividing
by \(a\).

At fixed \(X\), a direct determinant calculation gives
\[
\det\frac{\partial(Y,Z,W)}{\partial(a,\rho,q)}=-2a,
\qquad
\det\frac{\partial(Y,Z,W)}{\partial(a,\rho,v)}=1.
\tag{2}
\]
Indeed the first matrix has rows
\((X,0,1)\), \((1,X,0)\),
\((-2\rho,-2a-2\rho X,0)\).
Changing from \(q\) to \(v=-2a q\) multiplies this determinant
by \(-1/(2a)\), proving the second identity for every \(X\).
This relative normalization does not turn the first determinant
into a polynomial automorphism certificate.

## 2. Both formal tails and the two components

The coefficient partials are the ordinary \(a,\rho\) partials
on \(L\), extended by fixing \(v\). Take \(m=1\) and
\[
\begin{gathered}
f_0=0,\qquad f_1=-\rho^2,\qquad f_{-1}=a^2,\\
\Omega(U,V)=-2\rho V,\qquad
\Phi(U,V)=V^2-a^2,\qquad
\Psi(U,V)=-2a U,\\
g=V-a,\qquad h=V+a,\qquad
\Phi=gh,\qquad \Psi(y,z)=v .
\end{gathered}
\tag{3}
\]
These follow directly from the signed Taylor definitions139:
\(H_1(f_1)=-2\rho V\),
\(H_2(f_1)=-V^2\), and \(H_3(f_1)=0\).
Thus the nonnegative part of \(X\Theta(f_1)\) is exactly the
polynomial \(W\) in (1), and the first evaluated negative
coefficient is \(a^2\).

Both components have coordinate ring \(L[U]\), with
\(\Psi=-2a U\) transcendental over \(L\). The component
persistence theorem141 therefore supplies the full formal
cofactor and Laurent identities on each one.[^1]
The factors are distinct and comaximal because \(2a\in L^*\).
In particular each component has algebraic constant field exactly
\(L\). Also \(L_0=K(f_0,f_1,f_{-1})=L\) here.

The source rational expressions for the two base parameters are
\(\tau=z\) and \(\rho=-w_0/(2z)\). On the extra component
\((y_h,z_h,w_{0h})=(U,-a,2a\rho)\), so
\[
\sigma_h(\tau)=-a\ne a=\tau,\qquad
\sigma_h(\rho)=\rho .
\tag{4}
\]
The component is not base-compatible, despite its unchanged
algebraic constant field. Hence neither the coefficient-degree
bound nor the conditional stabilizer theorem143 excludes it.
The latter explicitly requires the two base identities.[^2]

## 3. Exact failure of the actual inverse premise

Write \(M=\mathbb C(X,Y,Z,W)\) for the target field and
\(H=\mathbb C(X,q,a,\rho)\) for the source field.
The nonzero determinant in (2) proves that the four target
functions are algebraically independent. The exact identities
\[
Z^2+XW=a^2,\qquad
H=M(a),\qquad
\rho=(Z-a)/X,\qquad q=Y-aX,\qquad [H:M]=2
\tag{5}
\]
follow as follows. The first identity is direct expansion and
the next two formulas recover the source after adjoining \(a\).
In the polynomial ring on the independent target variables,
\(Z^2+XW\) is irreducible. As a polynomial in \(W\), its
coefficients \(X,Z^2\) are coprime, and it is linear over
\(\mathbb C(X,Y,Z)\); Gauss's lemma applies.
Its valuation as a prime divisor of the target field is one,
so it is not a square in \(M\).
Consequently \(T^2-(Z^2+XW)\) is irreducible over \(M\),
which proves the degree assertion in (5).

Thus there is no rational inverse over the target field, and
in particular no polynomial inverse. The nonunit Jacobian
in (2) is a separate obstruction to an actual coordinate frame.
The relative determinant and full formal recurrences do not
repair either failure.

This example isolates a different missing condition from the
formal cubic's enlarged constant field: here the constants
remain \(L\), but the base speed value changes. It gives no
actual extra-factor example and no cancellation conclusion.

## Sources

1. [Signed negative-tail definitions139](dense-negative-tail-relations-pass139-working.md)
   and [formal component persistence141](dense-tail-component-persistence-pass141-working.md).
   These supply the definitions and the formal-only implication.
2. [Tail coefficient-field degree143](tail-coefficient-field-degree-pass143-working.md)
   and [base-compatible stabilizer143](dense-base-compatible-component-stabilizer-pass143-working.md).
   Their separate hypotheses are the two boundaries distinguished here.

All displayed identities and the degree-two inverse-field obstruction
are proved directly above. No actual realization, historical novelty,
or external classification result is asserted.

[^1]: Source 1. Activity holds on both components; actual inverse
    hypotheses do not.
[^2]: Source 2.
