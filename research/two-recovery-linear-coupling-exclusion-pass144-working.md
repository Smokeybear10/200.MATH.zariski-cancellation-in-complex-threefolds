# A two-recovery coupling cannot return to the three-good profile

The displayed three-shear construction is a polynomial automorphism
for every choice of its coefficients. If the intended third good
coordinate is square-zero under the slice derivation, however, its
first coupling must vanish. This holds in every last-coordinate
degree and for every nonconstant polynomial good speed \(P(a)\).

The surviving frames are precisely the recovered-invariant family
classified in143, whose dense first tails are primitive. This is a
restriction on one larger construction lane, not a classification
of all three-good frames or a cancellation theorem.

## 1. Actual coordinates before imposing the degree condition

Let \(u,v,a,b\) be independent over \(\mathbb C\), let
\(E=\partial_u\), and fix
\(P\in\mathbb C[a]\setminus\mathbb C\) and
\(F\in\mathbb C[t]\) with \(\deg F\ge2\).
Choose arbitrary polynomials
\(H\in\mathbb C[u,Y]\) and
\(\Psi\in\mathbb C[u,Y,A]\).
Define
\[
\begin{gathered}
Y=v+P(a)u,\qquad A=a+bH(u,Y),\\
W=b+\Psi(u,Y,A),\qquad
Z=A-F(Y)+uW,\\
\mathcal B=\mathbb C[u,v,a,b]
          =\mathbb C[u,Y,Z,W],\qquad
E^2u=E^2Y=0 .
\end{gathered}
\tag{1}
\]
The equality of rings in (1) does not assume \(E^2Z=0\).
Indeed \((u,Y,a,b)\) is already a coordinate system, and
the successive replacements \(a\mapsto A\), \(b\mapsto W\),
and \(A\mapsto Z\) are elementary shears. Their inverse is
\[
A=Z+F(Y)-uW,\qquad
b=W-\Psi(u,Y,A),\qquad
a=A-bH(u,Y),\qquad
v=Y-P(a)u .
\tag{2}
\]
All expressions are polynomial. Substituting the forward tuple
in (2) recovers \(A,b,a,v\) successively. Conversely, start
with independent \(u,Y,Z,W\) and define \(A,b,a,v\) by (2).
The forward formula for \(Y\) recovers \(Y\); the formula
\(a+bH=A\) recovers \(A\); then \(b+\Psi=W\), and finally
\(A-F(Y)+uW=Z\). Thus both inverse orders hold, including
the fiber \(u=0\).

Write \(\Delta_F(s,v,u)\) for the polynomial divided difference
defined by
\[
u\Delta_F(s,v,u)=F(v+su)-F(v).
\]
The quotient is polynomial even at \(u=0\), by the binomial
expansion. The exact profile classification is
\[
\boxed{\quad
E^2Z=0
\ \Longleftrightarrow\
\begin{cases}
H=0,\\
\Psi(u,Y,A)=
 \Delta_F(P(A),Y-P(A)u,u)+G(A,Y-P(A)u)
\end{cases}
\quad}
\tag{3}
\]
for some \(G\in\mathbb C[A,v]\).
There is no hypothesis on the \(E\)-degree of \(W\).

## 2. A highest-degree argument reduces a nonzero coupling

In the coordinates \((u,Y,a,b)\), the derivation is
\[
E=\partial_u+P(a)\partial_Y,\qquad Ea=Eb=0.
\]
For any \(Q\in\mathbb C[u,Y]\),
\[
E^2Q=Q_{uu}+2P(a)Q_{uY}+P(a)^2Q_{YY}=0
\quad\Longleftrightarrow\quad
Q\in\mathbb C+\mathbb C u+\mathbb C Y .
\tag{4}
\]
The nonconstant \(P(a)\) is transcendental over
\(\mathbb C(u,Y)\). Hence its three coefficients in (4)
vanish separately, and all second partials of \(Q\) are zero.
The converse is immediate.

Assume \(E^2Z=0\) and \(H\ne0\). Expand
\(\Psi=\sum_{j=0}^{e}c_j(u,Y)A^j\), allowing \(\Psi=0\).
If \(e\ge2\), the coefficient of \(b^e\) in \(Z\) is
\(u c_eH^e\). There are no competing terms of that degree:
\(A=a+bH\), and the remaining terms of \(Z\) have
\(b\)-degree at most one. Since \(E\) kills \(b\),
\[
E^2(u c_eH^e)=0.
\]
Equation (4) makes \(u c_eH^e\) affine in \(u,Y\).
It is divisible by \(u\), so \(c_eH^e\) must be a nonzero
complex constant.

If \(H\) is nonconstant, this is impossible in the polynomial
ring \(\mathbb C[u,Y]\). Therefore in that case \(e\le1\).

If \(H\) is a nonzero constant, it instead follows that
\(c_e\in\mathbb C\). Only in this constant-\(H\) case
does \(EA=0\). We may then subtract \(c_eA^e\) from
\(\Psi\): the corresponding change to \(Z\) is
\(-u c_eA^e\), whose second \(E\)-derivative is zero.
Repeating this finite reduction removes every term of
\(A\)-degree at least two. It retains \(E^2Z=0\).
No invariant subtraction is made when \(H\) is nonconstant.

Thus, if any nonzero \(H\) is possible, there is also a
polynomial of the form
\(\Psi=p(u,Y)A+q(u,Y)\) with the same \(H\) and with
\(E^2Z=0\). For this reduced polynomial put
\[
\begin{gathered}
M=1+up,\qquad R=uq-F(Y),\\
Z=aM+b(HM+u)+R,\qquad HM+u
   \in\mathbb C+\mathbb C u+\mathbb C Y,\\
aM_{uu}+2aP(a)M_{uY}+aP(a)^2M_{YY}
 +R_{uu}+2P(a)R_{uY}+P(a)^2R_{YY}=0 .
\end{gathered}
\tag{5}
\]
The middle assertion follows by applying (4) to the
coefficient of \(b\). The last identity is the coefficient
of \(b^0\), expanded as a polynomial in the independent
variable \(a\).

## 3. Every nonzero coupling contradicts the nonlinear profile

First suppose \(n=\deg P\ge2\). In the last line of (5),
the term \(aP(a)^2M_{YY}\) has the uniquely highest possible
\(a\)-degree \(2n+1\). Thus \(M_{YY}=0\).
After removing that term, \(P(a)^2R_{YY}\) has degree
\(2n>n+1\), greater than every remaining term, so
\(R_{YY}=0\). Setting \(u=0\) gives
\(F''(Y)=0\), contrary to \(\deg F\ge2\).
This rules out \(H\ne0\) when \(n\ge2\).

When \(P(a)=\alpha a+\beta\), with \(\alpha\ne0\), make
the invertible affine replacements
\[
a'=P(a),\quad b'=\alpha b,\quad
A'=\alpha A+\beta,\quad W'=\alpha W,\quad Z'=\alpha Z+\beta .
\]
The construction becomes
\[
A'=a'+b'H,\qquad
W'=b'+\alpha\Psi(u,Y,(A'-\beta)/\alpha),\qquad
Z'=A'-\alpha F(Y)+uW',
\]
and \(EY=a'\). The condition \(E^2Z'=0\) is equivalent
to \(E^2Z=0\). Thus it suffices to handle \(P(a)=a\).

In that case the last line of (5), compared coefficientwise
in \(a\), gives
\[
M_{YY}=0,\qquad
2M_{uY}+R_{YY}=0,\qquad
M_{uu}+2R_{uY}=0,\qquad
R_{uu}=0 .
\tag{6}
\]
Since \(R=uq-F(Y)\), the last identity makes \(q\)
independent of \(u\). The first makes
\(p=p_0(u)+p_1(u)Y\).
Differentiating the second identity with respect to \(Y\)
then gives
\(u q'''(Y)-F'''(Y)=0\).
Thus \(F\) is quadratic and \(q\) has degree at most two.
Write
\[
F''=2\gamma,\quad \gamma\in\mathbb C^*,\qquad
q=q_2Y^2+q_1Y+q_0 .
\]
The second identity of (6) becomes
\((up_1)'=\gamma-q_2u\).
Polynomiality gives \(p_1=\gamma-q_2u/2\).
The coefficient of \(Y\) in the third identity is then
\(3q_2=0\). Therefore \(q_2=0\), and its constant
coefficient gives
\(p_0=\kappa-q_1u\) for some \(\kappa\in\mathbb C\).

Consequently
\[
M=1+\kappa u-q_1u^2+\gamma uY
\]
has total degree exactly two. For any nonzero polynomial
\(H\), the product \(HM\) has degree \(\deg H+2\ge2\).
Adding \(u\) cannot remove its leading part.
This contradicts the affine constraint in (5).
The linear-\(P\) case also forces \(H=0\).

## 4. Exact integration of the surviving case

Now \(H=0\), so \(A=a\). Return to the invariant
coordinates \(u,v,a,b\), where \(Y=v+P(a)u\).
At \(u=0\), the value and first derivative of \(Z\) are
\[
Z|_{u=0}=a-F(v),\qquad
EZ|_{u=0}=b+\Psi(0,v,a)-P(a)F'(v).
\]
Thus \(E^2Z=0\) is equivalent to
\[
\begin{gathered}
Z=a-F(v)+u(b+G(a,v)),\qquad
G(a,v)=\Psi(0,v,a)-P(a)F'(v),\\
\Psi(u,v+P(a)u,a)
 =\Delta_F(P(a),v,u)+G(a,v).
\end{gathered}
\tag{7}
\]
To obtain the second line, compare the first with
\(Z=a-F(v+P(a)u)+u[b+\Psi(u,v+P(a)u,a)]\)
and cancel \(u\) in the polynomial domain.
The change \(Y=v+P(a)u\) is a polynomial automorphism,
so this is exactly the \(\Psi\)-identity in (3).
Conversely that identity gives the first line of (7)
and hence \(E^2Z=0\). This proves both directions of (3).

The surviving tuple is
\[
u,\qquad Y=v+P(a)u,\qquad
Z=a-F(v)+(b+G(a,v))u,\qquad
W=b+G(a,v)+\Delta_F(P(a),v,u).
\]
After the invariant triangular replacement
\(b\mapsto b+G(a,v)\), this is precisely the dense
family143.[^1] Its exact last degree and fixed-good minimum
are \(\deg F-1\); its first tail is primitive, including
the chart with varying selected speed \(P(a)\).
These are inherited family conclusions, not a new
general first-tail theorem.

## 5. Scope and hypotheses

Unlike the single-recovery template143, (1) is an actual
polynomial automorphism for arbitrary \(H,\Psi\).
The obstruction here concerns return to the three-good
differential profile, not failure of the original inverse.
The degree of the bad coordinate is unrestricted throughout.

Both principal assumptions matter. If \(P=p\) is constant,
take \(H=Y-pu\) and
\(\Psi=\Delta_F(p,Y-pu,u)\).
Then \(A=a+bv\) is invariant and
\(Z=a+bv-F(v)+ub\) is E-affine despite \(H\ne0\);
the speed rank is only one. If \(F\) is affine, take
\(H=1,\Psi=0\). The formula
\(Z=a+b-F(Y)+ub\) is E-affine for every nonconstant
\(P\), again with \(H\ne0\).

The proof does not cover arbitrary nonlinear dependence
on \(b\) in the first replacement \(A=a+R(u,Y,b)\),
longer words that leave and return to the profile,
or arbitrary supplied frames. It supplies no actual extra
first-tail factor and makes no cancellation or novelty claim.

## Sources

1. [Rigidity of a recovered-invariant divided-difference template143](recovered-invariant-template-rigidity-pass143-working.md),
   Sections 1--3. The surviving family, both inverse orders,
   calibrated intrinsic parameter, exact primitive tails,
   and the fixed-good minimum. The new obstruction to
   \(H\ne0\) is proved directly above.

No external classification result is used for the
two-recovery exclusion.

[^1]: Source 1. The current construction allows two successive
    recovery identities before imposing E-affinity.
    Its surviving \(H=0\) frame belongs to the already
    classified family.
