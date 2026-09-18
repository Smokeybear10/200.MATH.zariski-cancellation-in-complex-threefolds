# Quartic cusp graphs: coefficient rigidity and a field-return boundary

**Status: working generic restrictions, not integral recognition.**

In the actual nonzero-\(r\) cusp chart159, suppose \(y\)
is an affine generic parameter and \(\vartheta\) has degree
four in that parameter. Then the reciprocal of \(r\) is
complex-affine in \(\tau\). The coefficient of \(V\) in
the whole implicit relation, as well as \(n_\rho\), is a
complex constant multiple of \(r^2\). The full constant
determinant imposes the lower coefficient equations below.

Those equations are consistent over the generic field. An
explicit solution has the whole intrinsic line and constant
relative determinant, but its projected coordinate field has
index two in the source field. Thus it is not an actual
polynomial frame. This separates the remaining actual inverse
condition from the generic coefficient equations.

## 1. The fixed-axis graph and its whole relation

Retain all actual cusp hypotheses and notation of159:
\(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\),
exact time degrees \((1,1,2,2)\), and full weighted initial
kernel \((\mathsf X\mathsf Z-\mathsf Y^3)\).
In particular, the exact coefficient field \(L\) is finite
separable over \(\mathbb C(\tau,\rho)\), its coefficient
partials commute, and \(A_L=L[v]\) with \(Nv=1\).
Work in the branch \(r=k_\rho\ne0\), and assume
\[
\deg_v y=1,\qquad \vartheta=P(y),\qquad
P\in L[U],\quad \deg P=4,\qquad L[y,\vartheta]=L[v].
\tag{1}
\]
This is a condition on the fixed projected axes, not a
coefficient-dependent change of the original four coordinates.

The kernel of evaluation \((U,V)\mapsto(y,\vartheta)\)
is exactly \((V-P(U))\). Indeed \(y\) is transcendental
over \(L\), so polynomial division by \(V-P(U)\)
leaves a remainder in \(L[U]\) which must be zero.
The nonzero potential159 has degree at most four and
\(\Phi(y,\vartheta)=m\in L\). Degree therefore gives
\[
\Phi-m=\lambda\{V-P(U)\},\qquad \lambda\in L^*,
\qquad
\Phi_4=-\frac{U^3(r_\tau U+r_\rho V)}r.
\tag{2}
\]
No extra-factor hypothesis is needed: the selected graph
already has total degree four. Comparison of the top terms
gives \(r_\rho=0\) and \(r':=r_\tau\ne0\).

Use primes for coefficient \(\tau\) derivatives and put
\(s=n_\rho\), \(\delta=r''/2-r'^2/r\).
Expanding the literal potential159, with \(r_\rho=0\),
gives
\[
\begin{gathered}
\Phi=\tfrac12 n_{\rho\rho}V^2+
 \{\delta U^2+b_1U+b_0\}V+C(U),\\
b_1=n_{\tau\rho}-2r'n_\rho/r,
\qquad b_0=-n_\rho^2/r-\ell_\rho,\\
C_4=-r'/r,\qquad
C_3=k'''/6-r'k''/(2r)-s/r,\\
C_2=n''/2-r'n'/r-sk''/(2r),\qquad
C_1=(r'\ell-sn')/r-\ell',\qquad C_0=s\ell/r .
\end{gathered}
\tag{3}
\]
Here \(C_j=[U^j]C\). The letter \(s\) in this note
means \(n_\rho\), not the selected good speed
\(a=EX\). Comparison with (2) forces
\[
n_{\rho\rho}=0,\qquad \delta=0,\qquad b_1=0,
\qquad \lambda=b_0\ne0,
\qquad P(U)=\{m-C(U)\}/\lambda .
\tag{4}
\]

## 2. The reciprocal affine coefficient and exact constants

The joint constants of \(\partial_\tau,\partial_\rho\)
in \(L\) are exactly \(\mathbb C\). To see this, take
an element killed by both derivatives and differentiate its
monic minimal polynomial over \(\mathbb C(\tau,\rho)\).
Each resulting relation has smaller degree, so every
coefficient of the minimal polynomial is a joint constant
of the rational base field. Those constants are complex.
The element is then algebraic over the algebraically closed
field \(\mathbb C\), and therefore belongs to it.

Set \(\chi=1/r\). Equation (4) says \(\chi''=0\),
while \(\chi_\rho=0\). Thus \(\chi'\) and
\(\chi-\tau\chi'\) are joint constants. Also \(r'\ne0\).
Since \(s_\rho=0\) and \(b_1=0\), the quotient
\(s/r^2\) is killed by both coefficient derivatives.
Consequently
\[
\chi=A\tau+B,\quad r=\frac1{A\tau+B},\quad
A\in\mathbb C^*,\ B\in\mathbb C,\qquad
s=C r^2,\quad C\in\mathbb C .
\tag{5}
\]
The case \(C=0\) is allowed. These are identities in the
original exact coefficient field. No change of its derivations
or of the original polynomial coordinates has been made.
Writing \(\tau+B/A\) is only a notational translation of
the rational formula for \(r\).

Put \(\alpha=r'/r\). Then
\(\alpha'=\alpha^2\ne0\),
\(r''=2\alpha^2r\), and \(r'''=6\alpha^3r\).
Let \(K=\ker_L\partial_\rho\), which is preserved by
\(\partial_\tau\). Direct subtraction of polynomial
primitives gives
\(k=r\rho+k_0\), \(n=s\rho+n_0\), with
\(k_0,n_0\in K\). There is no assumption that elements
of \(K\) are rational functions of \(\tau\).

## 3. The full determinant in the affine parameter y

Extend the coefficient partials from \(L\) to fix \(y\),
rather than the earlier normalized parameter \(v\).
Their restrictions to \(L\) do not change. If
\(q=y_v\in L^*\), the actual determinant159 becomes
\(J_y=-a^3/q\in L^*\).
The constant wedge identity of that source has
\(C_U=P_\rho+(r'U+s)/r\) and
\(C_V=-P_\tau-(3U^2+k''U+r'P+n')/r\) after
evaluation \(U=y\). Since
\(\Phi_U=-\lambda P_U\) and \(\Phi_V=\lambda\),
it yields
\[
\begin{gathered}
\mathcal S(U)=P_\tau+P_U P_\rho+
 \frac{P_U(r'U+s)+3U^2+k''U+r'P+n'}r,
\qquad \mathcal S\in L[U],\\
J_y=-\lambda\mathcal S(y)=-a^3/q,
\qquad \mathcal S(U)=a^3/(q\lambda)\in L^* .
\end{gathered}
\tag{6}
\]
The last equality is an identity in \(L[U]\) because
\(y\) is a transcendental parameter. It does not follow
from merely evaluating a polynomial on an algebraic point.

Write \(P=p_4U^4+p_3U^3+p_2U^2+p_1U+p_0\), so
\(p_4=\alpha/\lambda\ne0\). The unique contribution
to \([U^7]\mathcal S\) is \(4p_4(p_4)_\rho\).
All terms other than \(P_U P_\rho\) have degree at most
four. Thus \((p_4)_\rho=0\), and \(\lambda_\rho=0\).
By \(\lambda=-s^2/r-\ell_\rho\) this also gives
\(\ell_{\rho\rho}=0\). Write
\[
\ell=\ell_1\rho+\ell_0,\qquad
\ell_1=-\lambda-s^2/r,\qquad \ell_0,\ell_1\in K.
\tag{7}
\]

The coefficients in (3) satisfy
\[
(C_3)_\rho=r'''/6-\alpha r''/2=0,\qquad
(C_2)_\rho=s''/2-\alpha s'-sr''/(2r)=0,
\]
using (5), \(s'=2\alpha s\), and \(s''=6\alpha^2s\).
Hence \((p_3)_\rho=(p_2)_\rho=0\).
For the linear coefficient, differentiate (3) and substitute
(7):
\((C_1)_\rho=\alpha\ell_1-ss'/r-\ell_1'
=\lambda'-\alpha\lambda\).
It follows that
\[
(p_1)_\rho=\alpha-\lambda'/\lambda=p_4'/p_4,
\qquad
[U^4]\mathcal S
=p_4'+4p_4(p_1)_\rho+5\alpha p_4
=5p_4\{(p_1)_\rho+\alpha\}=0.
\tag{8}
\]
Here the two summands involving \(r'\) in (6) contribute
\(4\alpha p_4\) and \(\alpha p_4\), respectively.
Thus \(\lambda'/\lambda=2\alpha\).
Together with \(\lambda_\rho=0\), the joint-constant
argument proves the additional rigidity
\[
\lambda=D r^2,\qquad D\in\mathbb C^*,\qquad
(p_1)_\rho=-\alpha .
\tag{9}
\]

## 4. The exact lower coefficient equations

For clarity the remaining polynomial content of (6) can be
written over \(K\). The coefficient of \(U^3\) first
gives
\(p_3'+\alpha p_3+4p_4\{(p_0)_\rho+s/r\}=0\).
Since its other coefficients lie in \(K\),
\(e:=(p_0)_\rho\in K\). Direct subtraction now shows
\[
\begin{gathered}
p_1=-\alpha\rho+b,\qquad p_0=e\rho+d,
\qquad b,d,e\in K,\qquad h=e+s/r\in K,\\
p_3'+\alpha p_3+4p_4h=0,\\
p_2'+\alpha p_2+3p_3h+3/r=0,\\
b'+\alpha b+2p_2h+k_0''/r=0,\\
\mathcal S=h'\rho+d'+\alpha d+hb+n_0'/r\in L^* .
\end{gathered}
\tag{10}
\]
The second and third equations are the coefficients of
\(U^2\) and \(U\) in (6). In the third, the
\(\rho\) terms cancel because
\(r''/r=2\alpha^2\).
For the constant coefficient use
\(p_0'+h p_1+\alpha p_0+n'/r\).
Its \(\rho\) coefficient is
\(e'-\alpha s/r+s'/r=e'+\alpha s/r=h'\).

The coefficients in (10) retain their definitions from
the literal potential (3)--(4). They are not arbitrary
free data. Subject to those definitions and (5), (7), (9),
these equations are exactly the remaining requirement that
\(\mathcal S\) be a nonzero constant in its formal variable.
They do not assert that a solution has a polynomial inverse
in the original ring. Polynomial primitive subtraction in
\(\rho\) has been used, not an unproved coefficient-field
antiderivative in \(\tau\).

## 5. An exact generic solution which fails the actual field-return condition

Let \(L=\mathbb C(\tau,\rho)\), with the ordinary
commuting coefficient derivatives, and let \(v\) be
transcendental over \(L\). Set
\[
\begin{gathered}
r=1/\tau,\quad k=\rho/\tau,\quad n=\tau^2,
\quad \ell=-\rho/\tau^2,\quad s=0,\quad \lambda=\tau^{-2},\\
P(U)=-\tau U^4-3\tau^2U^2+(\rho/\tau)U,
\qquad y=v,\qquad \vartheta=P(v),\\
z=\tau^2-v^4,\qquad
w=-v^5-4\tau v^3-2\tau^2v-\rho/\tau,
\qquad \sigma=3\tau^2v+\rho/\tau .
\end{gathered}
\tag{11}
\]
These are generic rational coefficient data, not a claimed
actual four-coordinate frame. Their literal potentials are
\[
\begin{gathered}
f(U,V)=U^3+(\rho/\tau^3)U^2-UV/\tau^2+2\tau U,\\
\Phi(U,V)=V/\tau^2+U^4/\tau+3U^2-\rho U/\tau^3
 =\lambda\{V-P(U)\},\qquad m=0,\\
rw+f(y,\vartheta)=\ell,\qquad
\mathcal S(U)=2\tau^2,\qquad J_y=-2 .
\end{gathered}
\tag{12}
\]
For example, in (10) one has
\(p_4=-\tau,p_3=0,p_2=-3\tau^2,b=d=e=h=0\),
\(k_0=0,n_0=\tau^2\), and \(\alpha=-1/\tau\).
The two nontrivial lower equations are
\(-6\tau+3\tau+3\tau=0\) and
\(\mathcal S=n_0'/r=2\tau^2\).
Thus all positive powers in (6) vanish, not just its top
coefficient. The potential in (12) follows directly by
expanding (3) or the Taylor definition159.

For the full polynomial-in-\(X\) chart, use
\(Y=y+\tau X\), \(Z=z+\sigma X+\tau^3X^2\), and
\(W=w+\vartheta X+\rho X^2\), with independent \(X\).
The identities for \(\sigma,z\), \(rw+f=\ell\), and
\(\Phi=m\) make the \(X^4,X^3,X^2,X\) determinant
coefficients zero by the algebraic identities159.
Its constant coefficient can also be computed without those
recurrences: \(y_v=1\), \(z_\tau=2\tau\),
\(z_\rho=0\), \(w_\rho=-1/\tau\), so
\(\det\partial(y,z,w)/\partial(\tau,\rho,v)=-2\).
The whole intrinsic line condition holds, since
\(L[y,\vartheta]=L[v]\).
Even the numerical form \(J=-a^3\) can be obtained by
choosing a nonzero complex number \(a\) with \(a^3=2\);
it does not repair the failure below.

Put \(M=\mathbb C(y,z,w)\) inside
\(F=\mathbb C(\tau,\rho,v)\). The explicit formulas give
\[
v=y,\qquad \tau^2=z+y^4,\qquad
\rho=-\tau\{w+y^5+4\tau y^3+2\tau^2y\},
\qquad F=M(\tau),\qquad [F:M]=2 .
\tag{13}
\]
Indeed \(F=M(\tau)\) and the quadratic relation first
imply \(\operatorname{trdeg}_{\mathbb C}M=3\).
Thus the three generators \(y,z,w\) are algebraically
independent. In the corresponding polynomial ring,
\(z+y^4\) is irreducible because it is monic linear in
\(z\). Its prime valuation is one, so it is not a square
in \(M\). The quadratic for \(\tau\) is irreducible,
proving the exact degree in (13).

An actual chart159 has
\(A_a=\mathbb C[y,z,w]_{a_0}\), hence
\(\operatorname{Frac}A=\mathbb C(y,z,w)\).
Equation (13) violates that necessary field equality.
There is consequently no actual polynomial inverse for
this generic solution in the stated source field.
The index remains two after adjoining independent \(X\).
This is a failure of actualness, not an example of an actual
cusp frame with nonpolynomial invariant ring.

## Scope and sources

The conclusions (5), (9), (10) are necessary restrictions
for the specified fixed-axis actual quartic graph.
They allow finite algebraic coefficient extensions and do
not use a generic shear as an integral polynomial map.
The exact generic example proves that the constant relative
determinant and whole intrinsic line alone cannot replace
the actual projected field-return condition. It neither
proves nor disproves the existence of an actual quartic
graph satisfying all inverse requirements.

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 1--5, for the actual field, literal potential,
   constant wedge, and projected-ring equality.
2. [Cusp selected-factor reduction159](cusp-generic-selected-factor-reduction-pass159-working.md),
   for the distinction between the selected factor and the
   whole potential. Section 1 above resolves that issue
   here directly by the degree-four graph condition.

The displayed rational example is an algebraic control only.
No test execution, arbitrary-entry theorem, full cancellation
result, historical novelty clearance, human expert review,
or proof-assistant certification is claimed. No162 or earlier
artifact is changed.
