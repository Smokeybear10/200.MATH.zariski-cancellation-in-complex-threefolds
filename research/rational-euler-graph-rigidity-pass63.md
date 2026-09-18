# Rational Euler graph rigidity and exclusion of all exact monomial speeds

A two-row graph whose nonconstant coefficients lie in one rational
Euler-invariant field cannot both satisfy the full Schur determinant
condition and generate the actual coordinate field, unless its
coefficients are constant. This statement requires that the actual
base ring have no nonconstant Euler invariants.

The conclusion gives a polynomial-ring equality and an affine slice
under those explicit hypotheses. It excludes every exact positive
monomial speed pair, with no restriction on the greatest common
divisor of the exponents. It does not supply a universal coordinate
frame or resolve unrestricted cancellation.

## 1. An abstract statement with the actualness requirements exposed

All fields and rings contain \(k=\mathbb C\). Let \(R\) be a domain
with fraction field \(L\) of transcendence degree two over \(k\).
Choose algebraically independent \(f,g\in R\). Their field partials
extend uniquely to the algebraic separable extension \(L/k(f,g)\).
Write
\[
\mathscr H=f\partial_f+g\partial_g.
\tag{1}
\]
Suppose that for some transcendental \(r\in L\),
\[
\ker_L\mathscr H=k(r),\qquad R\cap k(r)=k,
\qquad \lambda=(\partial_f r,\partial_g r)\ne0.
\tag{2}
\]
The last two conditions concern the actual ring and field. They
are not conclusions from a formal change of variables.

Let \(X,Y\) be algebraically independent over \(L\), and let
\[
R[X,Y]\subseteq B_R\subseteq L[X,Y],\qquad B_R\cap L=R.
\]
Suppose that two actual elements \(Q_1,Q_2\in B_R\) satisfy
\[
B_R=R[Q_1,Q_2,X,Y],\qquad
k(Q_1,Q_2,X,Y)=L(X,Y),
\tag{3}
\]
and admit the exact graph
\[
Q=\ell+S(r;X,Y),\qquad \ell\in L^2,\qquad
S\in k(r)[X,Y]^2,\quad S(r;0,0)=0.
\tag{4}
\]
No degree bound on \(S\) is needed. Its constant term has simply
been assigned to \(\ell\). In particular neither \(\ell\) nor
the coefficients of \(S\) are initially assumed to belong to \(R\).

Holding \(X,Y\) fixed, assume the whole base Jacobian satisfies
\[
\det Q_{(f,g)}\in L^*.
\tag{5}
\]
This is stronger than a condition on its highest homogeneous part.

**Graph rigidity theorem.** Conditions (1)--(5) force
\[
S\in k[X,Y]^2,\qquad \ell\in R^2,\qquad B_R=R[X,Y].
\tag{6}
\]
If, in addition, the original derivation on this ring is
\[
E|_R=0,\qquad EX=f,\qquad EY=g,\qquad Es_*=1
\quad\hbox{for some }s_*\in B_R,
\tag{7}
\]
then
\[
(f,g)R=R.
\tag{8}
\]
In particular these hypotheses are inconsistent at a common
speed zero, where \((f,g)R\) is proper.

The subscript in \(B_R\) permits application to a localization
of the original polynomial ring. The field equality in (3)
remains over \(k\), not merely over \(R\) or \(L\).

## 2. The full determinant forces a single coefficient direction

Set \(A_0=\ell_{(f,g)}\). Differentiating (4) gives
\[
Q_{(f,g)}=A_0+S_r\lambda.
\tag{9}
\]
The update has rank at most one. Because \(S_r(r;0,0)=0\),
condition (5) gives \(\det A_0=\det Q_{(f,g)}\ne0\).
The elementary rank-one determinant identity therefore implies
\[
\lambda A_0^{-1}S_r=0.
\]
Since \(\mathscr Hr=0\), the kernel of the nonzero row
\(\lambda\) is the one-dimensional line \(L(f,g)^{\mathsf t}\).
Consequently every coefficient vector of \(S_r\) is collinear with
\[
\mathscr H\ell=A_0(f,g)^{\mathsf t}\ne0.
\tag{10}
\]
The inequality uses invertibility of \(A_0\), not a regularity claim.

Suppose, toward a contradiction, that \(S_r\ne0\). Swap the two
good rows if necessary so that some coefficient of \((S_1)_r\)
is nonzero. Write that coefficient as \(s_{1\nu}'(r)\), with
the corresponding second coefficient \(s_{2\nu}'(r)\).
Collinearity in (10) makes \(\mathscr H\ell_1\ne0\) and gives
\[
\rho(r)=\frac{s_{2\nu}'(r)}{s_{1\nu}'(r)}
       =\frac{\mathscr H\ell_2}{\mathscr H\ell_1}\in k(r),
\qquad (S_2)_r=\rho(S_1)_r.
\tag{11}
\]
Because \(\mathscr H\rho=0\), equation (2) now shows
\[
I=\ell_2-\rho\ell_1\in k(r).
\]
Put \(D=S_2-\rho S_1\). Thus
\[
Q_2=\rho Q_1+D(r;X,Y)+I(r),\qquad
D_r=-\rho_r S_1.
\tag{12}
\]
The second identity is differentiation in the one rational
variable \(r\). It retains every coefficient of the graph.

## 3. The actual field requires a rational function of degree one

Extend \(\mathscr H\) to \(L(X,Y)\) by fixing \(X,Y\).
It kills \(k(r,X,Y)\), while
\[
\mathscr HQ_1=\mathscr H\ell_1\ne0.
\]
Therefore \(Q_1\) is transcendental over \(k(r,X,Y)\).
Indeed, if it were algebraic, differentiating its separable
minimal polynomial over the field killed by \(\mathscr H\)
would force \(\mathscr HQ_1=0\). Characteristic zero is used here.

It follows that \(Q_1,r,X,Y\) are algebraically independent.
Set \(K=k(Q_1,X,Y)\). Formula (12) places \(Q_2\) in \(K(r)\).
The actual field equality (3), together with \(r\in L\), gives
\[
K(Q_2)\subseteq K(r)\subseteq L(X,Y)=K(Q_2).
\tag{13}
\]
Every inclusion is an equality. In particular \(Q_2\), viewed
as a rational function \(\mathcal R(r)\) over \(K\), has degree one.

For completeness, if \(\mathcal R=P/T\) is a nonconstant reduced
rational function over any field \(K\), then
\[
[K(r):K(\mathcal R)]=\max(\deg P,\deg T).
\tag{14}
\]
To prove this, introduce an indeterminate \(w\).
The polynomial \(P(Z)-wT(Z)\) is irreducible in \(K[Z,w]\):
since it has degree one in \(w\), a nontrivial factor independent
of \(w\) would divide both \(P\) and \(T\). Gauss's lemma then
gives its irreducibility over \(K(w)\). Its degree in \(Z\)
is \(\max(\deg P,\deg T)\). This also equals the total degree
of the pole divisor, including the point at infinity.

This step uses actual coordinate-field generation. A nonzero
Jacobian, or a polynomial inverse over \(L[X,Y]\), cannot
replace (13).

## 4. Nonconstant directions contradict the pole divisor

Write the positive-degree monomial expansion
\[
D(r;X,Y)=\sum_{\nu\ne(0,0)}d_\nu(r)X^{\nu_1}Y^{\nu_2}.
\]
The rational function in (12) is
\[
\mathcal R(r)=
\rho(r)Q_1+\sum_{\nu\ne(0,0)}d_\nu(r)X^{\nu_1}Y^{\nu_2}+I(r).
\tag{15}
\]
At every point of \(\mathbb P^1(k)\), its pole order is the
maximum of the pole orders of the coefficient functions
\(\rho,d_\nu,I\), with zero included in the maximum.

Here is the precise noncancellation argument. All coefficient
functions are rational over \(k\), so their poles, including
infinity, are \(k\)-rational. In a local parameter at any such
point, take the most negative Laurent order among the
coefficient functions. The coefficient of that order in (15)
is a nonzero \(k\)-linear combination of distinct monomials
\[
Q_1,\quad X^{\nu_1}Y^{\nu_2},\quad 1.
\]
These monomials are linearly independent because \(Q_1,X,Y\)
are algebraically independent over \(k\). Thus the leading
Laurent coefficient cannot cancel. Passing to the larger
coefficient field \(K\) does not change this conclusion.
There are no other poles, since a common denominator in
\(k[r]\) suffices for every term of (15).

Suppose \(\rho\) is nonconstant. By (13)--(14), the entire
pole divisor of \(\mathcal R\) has degree one. The coefficientwise
maximum just proved implies that \(\rho\) has that same
single simple pole, and every \(d_\nu\) has at most that pole.

A nonconstant rational function with one simple pole has
degree one, hence is a fractional-linear coordinate on
\(\mathbb P^1\). Every rational function with at most the
same pole is consequently affine in \(\rho\):
\[
d_\nu=A_\nu+B_\nu\rho,\qquad A_\nu,B_\nu\in k.
\tag{16}
\]
This elementary statement can also be checked directly:
move the one permitted pole to infinity by a fractional-linear
change, after which the functions are polynomials of degree
at most one.

Comparison of coefficients in the differentiated identity
\(D_r=-\rho_r S_1\) from (12) now gives
\[
B_\nu\rho_r=-\rho_r s_{1\nu},\qquad s_{1\nu}=-B_\nu.
\tag{17}
\]
Since \(\rho\) is nonconstant in characteristic zero,
\(\rho_r\ne0\). Every coefficient of \(S_1\) is therefore
constant. This contradicts the chosen nonzero coefficient
of \((S_1)_r\).

This proof does not require an explicit lower bound such as
four on the field degree. It rules out degree one directly,
for any finite polynomial support in \(X,Y\).

## 5. Constant directions contradict actual coordinate independence

Suppose instead that \(\rho\in k\). Equation (11) gives
\[
D_r=0,\qquad D\in k[X,Y].
\]
Equation (12) then expresses
\[
I=Q_2-\rho Q_1-D(X,Y)\in B_R\cap L=R.
\]
But \(I\in k(r)\), so the actual invariant-ring condition
in (2) gives \(I\in k\). Thus \(Q_2\) is a polynomial in
\(Q_1,X,Y\) over \(k\), contradicting the algebraic independence
of the four generators in (3).

Both alternatives for \(\rho\) are impossible. Hence \(S_r=0\).
A rational function of \(r\) with zero derivative is constant,
so \(S\in k[X,Y]^2\). The actual differences \(Q_i-S_i\)
then put \(\ell_i\) in \(B_R\cap L=R\).
Finally (3) gives \(B_R=R[X,Y]\), proving (6).

On this whole polynomial ring the derivation in (7) has image
inside \((f,g)R[X,Y]\). Applying it to the supplied slice and
evaluating at \(X=Y=0\) yields \(1\in(f,g)R\), proving (8).
The slice was arbitrary; no affine-slice premise was used.

## 6. The resulting slice and kernel are explicit

Choose \(u_0,v_0\in R\) with \(u_0f+v_0g=1\). Then
\[
\sigma=u_0X+v_0Y,\qquad j=gX-fY
\]
satisfy
\[
E\sigma=1,\qquad Ej=0,\qquad
X=f\sigma+v_0j,\qquad Y=g\sigma-u_0j.
\tag{18}
\]
These formulas prove, without a projective-module theorem,
\[
B_R=R[\sigma,j],\qquad \ker(E|_{B_R})=R[j].
\tag{19}
\]
The kernel equality follows by expanding a polynomial in
\(\sigma\) over the characteristic-zero domain \(R[j]\).

For the global actual base \(R=C\simeq k^{[2]}\), this gives
\(\ker E\simeq k^{[3]}\) under (1)--(5) and (7).
For a localized base it is only a localized kernel equality.
Neither conclusion removes the hypotheses on the Euler
constants or the supplied actual graph.

## 7. Application to every exact positive monomial pair

Return to the actual setup of
[the generic bad-pair theorem](generic-bad-pair-pass44.md),
with \(C=k[a,b]\), \(L=k(a,b)\), and exact speeds
\[
f=a^p,\qquad g=b^q,\qquad p,q\in\mathbb Z_{>0}.
\tag{20}
\]
The actual good graph is quadratic, with Hessian coefficients
of weight-two accelerations and gradient coefficients of
weight-one potentials. The identities
\[
[\mathscr H,\partial_f]=-\partial_f,\qquad
[\mathscr H,\partial_g]=-\partial_g
\]
show that all of these positive-degree graph coefficients
are killed by \(\mathscr H\). The argument does not require
the potentials to be regular.

Set \(d=\gcd(p,q)\), \(p=du\), \(q=dv\), and
\[
r=b^v/a^u.
\]
Choose integers \(m,n\) with \(vm+un=1\), and put \(z=a^mb^n\).
Then
\[
a=r^{-n}z^v,\qquad b=r^mz^u,\qquad
L=k(r,z),\qquad
\mathscr H=\frac{z}{duv}\partial_z.
\tag{21}
\]
Consequently \(\ker_L\mathscr H=k(r)\).
Also \(\mathscr H=(a/p)\partial_a+(b/q)\partial_b\).
Positive monomial weights imply
\(C\cap\ker_L\mathscr H=k\).
Finally
\[
\lambda=\left(-\frac{r}{df},\frac{r}{dg}\right)\ne0.
\tag{22}
\]
Every hypothesis of the graph rigidity theorem is now supplied
by the actual graph, the whole Schur condition, and actual
coordinate generation. It forces \((a^p,b^q)C=C\), which is
false by evaluation at \(a=b=0\).

Thus **all exact positive monomial speed pairs are excluded
under the full actual frame assumptions**, including every
\(d\ge3\). This supersedes the exponent restriction in
[the gcd-at-most-two proof](monomial-speed-exclusion-pass62.md);
that proof remains a valid, separately reconstructed special case.
No monomial support enumeration enters the present argument.

## 8. Dependence, scope, and remaining work

The inherited actual hypotheses are those of
[pass44](generic-bad-pair-pass44.md). The full-determinant
alignment and actual-field comparison were isolated in
[the square-speed proof](square-speed-schur-generation-pass61.md).
The primitive weighted-field identities were also proved in
[pass62](monomial-speed-exclusion-pass62.md).

The new argument is the coefficientwise pole-divisor step
(15)--(17), which removes the finite quartic rank split.
The rank-one determinant identity and rational-function
degree statement have been proved directly here.

The theorem requires the exact rational constant field,
trivial intersection of that field with the actual base ring,
the whole determinant condition, and actual coordinate-field
generation. A formal model, an arbitrary rational graph, or
initial monomial terms alone do not supply those assumptions.
In particular a nonconstant regular Euler invariant is an
unresolved alternative, not something excluded by this proof.

The abstract statement permits local base rings, but their
intersection and constant-field hypotheses need their own
proof. This note does not automatically adjoin local roots,
replace the actual field, normalize all ramified germs, or
prove that the requisite low-degree coordinate frame always
exists.

The argument is a written conditional theorem, not a Lean
formalization or an expert-reviewed result. No novelty claim
or solution of unrestricted complex threefold cancellation
is made. The jet and geometry agents independently read the
complete proof and reconstructed all 22 numbered equations
without finding a mathematical gap. Both identified one
precision issue in the abstract opening: transcendence degree
alone gives an algebraic separable extension, not immediately
a finite one. The wording was corrected accordingly, and the
jet agent verified the correction. The affine agent subsequently
read the complete saved proof and independently reconstructed
all equations, cases, and the explicit inverse without a gap. These are AI
audits, not external expert review or formal verification.
