# Actual field return excludes an extra quadratic graph factor

Status: working proof pending independent review of this saved artifact.
Under the retained actual cusp hypotheses, a quadratic graph in the
fixed projected axes cannot have a nonconstant extra factor in the
potential relation. This is not recognition of the remaining quadratic
graph, an unrestricted entry theorem, or a novelty claim.

## 1. Actual hypotheses and the proposed extra factor

Retain [the actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md):
\(B=A[u]=\mathbb C[X,Y,Z,W]\), \(E=\partial_u\), exact time degrees
\((1,1,2,2)\), and full weighted initial kernel \((XZ-Y^3)\).
Let \(N=[u^3](\partial_Z|_A)\), \(L=\operatorname{Frac}(\ker_A N)\).
The actual projected coordinates satisfy
\[
\begin{gathered}
\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\qquad
L[y,\vartheta]=L[v],\qquad L/\mathbb C(\tau,\rho)\text{ finite},\\
z=3\tau y^2+k_\tau y+r\vartheta+n,\qquad r=k_\rho\ne0,\\
rw+y^3+\tfrac12k_{\tau\tau}y^2+k_{\tau\rho}y\vartheta
+\tfrac12k_{\rho\rho}\vartheta^2+n_\tau y+n_\rho\vartheta=\ell .
\end{gathered}
\tag{1}
\]
The extended coefficient partials commute and have joint constants
\(\mathbb C\).

Assume \(\vartheta=P(y)\), where
\(P(U)=p_2U^2+p_1U+p_0\in L[U]\), \(p_2\ne0\).
Then \(L[y]=L[v]\), so \(y\) is an affine parameter over \(L\).
Its selected equation is \(G=V-P(U)\).
If the potential has a nonconstant extra cofactor, the exact remainder
in [the selected-factor proof159](cusp-generic-selected-factor-reduction-pass159-working.md)
gives
\[
\Phi-m=\lambda G+\kappa G^2,\qquad \lambda,\kappa\in L^* .
\tag{2}
\]
Indeed the remainder multiplying \(G^2\) is constant by
\(\deg\Phi\le4\), and the selected unit gradient makes \(\lambda\ne0\).
We prove that (2) is impossible for an actual chart.

## 2. Coefficient equations and a fifth-power normal form

The quartic part of \(\Phi\) is
\(-U^3(r_\tau U+r_\rho V)/r\). Comparison with (2) gives
\(r_\rho=0\), \(r'\ne0\), and \(\kappa p_2^2=-r'/r\), where a
prime denotes \(\partial_\tau\).
Put \(K=\ker_L\partial_\rho\), so \(r\in K\).
Minimal-polynomial differentiation gives
\([K:\mathbb C(\tau)]<\infty\) and
\(\ker_K\partial_\tau=\mathbb C\).
In detail the monic minimal polynomial of a \(\rho\)-constant over
\(\mathbb C(\tau,\rho)\) has coefficient derivatives zero, hence
coefficients in \(\mathbb C(\tau)\). Linear independence persists
after adjoining the transcendental \(\rho\), bounding the degree by
\([L:\mathbb C(\tau,\rho)]\). In particular \(\rho\) is
transcendental over \(K\). Rationality of \(K\) is not assumed.

Write \(k=r\rho+k_0\), \(k_0\in K\), and
\(\Delta=r''/2-r'^2/r\). The coefficients of \(V^2,U^2V,UV\)
in the literal potential give
\[
\begin{gathered}
\kappa=n_{\rho\rho}/2,\qquad -2\kappa p_2=\Delta,\qquad
-2\kappa p_1=n_{\tau\rho}-2r'n_\rho/r,\\
\kappa=-\frac{r\Delta^2}{4r'},\qquad
p_2=\frac{2r'}{r\Delta},\qquad \kappa,p_2\in K^*,\\
n=\kappa\rho^2+s\rho+n_0,\quad s,n_0\in K,\\
p_1=\alpha\rho+b,\qquad
\alpha=2r'/r-\kappa'/\kappa,\qquad
b=-s'/(2\kappa)+r's/(r\kappa).
\end{gathered}
\tag{3}
\]
Thus \(\Delta\ne0\). Membership of \(\kappa,p_2\) in \(K\) has
been proved, not presumed for the two factors separately.

Using \(y\) as the third separating parameter, the actual determinant
is \(-\lambda\mathcal S=-a^3/y_v\in L^*\), with \(a=EX\) and
\[
\mathcal S=P_\tau+P_U P_\rho+
\frac{(r'U+2\kappa\rho+s)P_U+3U^2+(r''\rho+k_0'')U+
r'P+\kappa'\rho^2+s'\rho+n_0'}r\in L^*.
\tag{4}
\]
Here the evaluated gradient of (2) is \(\lambda(-P_U,1)\).
The normalization does not identify \(y\) with the intrinsic slice.

The \(U^2\) coefficient of (4) is
\(p_2'+2\alpha p_2+3(r'/r)p_2+3/r=0\).
Put \(\chi=1/r\). Equation (3) becomes
\[
\begin{gathered}
\chi',\chi''\ne0,\qquad
p_2=4\chi\chi'/\chi'',\qquad
\kappa=\chi''^2/(16\chi'\chi^3),\\
\alpha=\chi'/\chi+\chi''/\chi'-2\chi'''/\chi'',\\
0=p_2'+2\alpha p_2+3(r'/r)p_2+3/r
=-\frac{5\chi}{\chi''^2}(4\chi'\chi'''-3\chi''^2).
\end{gathered}
\tag{5}
\]
The last equality follows by logarithmically differentiating \(p_2\).
It needs no further potential coefficient or classification theorem.

To solve it over the exact field, set \(q=\chi''/\chi'\ne0\).
Then \(q'=-q^2/4\), so \((1/q)'=1/4\).
Exact constants give \(q=4/(\tau-C_2)\), \(C_2\in\mathbb C\).
Thus \((\chi'/(\tau-C_2)^4)'=0\).
Subtracting explicit primitives yields
\[
\begin{gathered}
\zeta=\tau-C_2,\qquad F=C_0+C_1\zeta^5,\qquad
C_0,C_2\in\mathbb C,\quad C_1\in\mathbb C^*,\\
r=1/F,\qquad \kappa=5C_1\zeta^2/F^3,\qquad
p_2=\zeta F,\qquad \alpha=F'/F-2/\zeta .
\end{gathered}
\tag{6}
\]
There is no root extraction or algebraic field enlargement.
The value \(C_0=0\) remains allowed.

## 3. Polynomial rho dependence and its two leading coefficients

The \(U\) coefficient of (4) makes \((p_0)_\rho\) affine in
\(\rho\), with coefficients in \(K\). Subtract its explicit quadratic
primitive to obtain \(p_0=d_2\rho^2+e\rho+d\), \(e,d\in K\), where
\[
d_2=-\frac{\alpha'+\alpha^2+2(r'/r)\alpha+
4\kappa p_2/r+r''/r}{4p_2}
=-\frac{F'}{\zeta^2F^2}-\frac3{2\zeta^3F}.
\tag{7}
\]
For the second equality put \(D=F'/F\), so
\(D'=4D/\zeta-D^2\).

The coefficient of \(U^2\) independent of \(V\) in the potential is
\[
\frac{n_{\tau\tau}}2-\frac{r'n_\tau}r
-\frac{n_\rho k_{\tau\tau}}{2r}
=\kappa(p_1^2+2p_2p_0)-\lambda p_2 .
\tag{8}
\]
All other terms belong to \(K[\rho]\) of degree at most two, and
\(p_2\in K^*\). Hence \(\lambda\in K[\rho]_{\le2}\).
Its quadratic coefficient is
\[
\lambda_2=
\frac{\kappa(\alpha^2+2p_2d_2)-\mathcal B}{p_2}=0,\qquad
\mathcal B=\kappa''/2-(r'/r)\kappa'-\kappa r''/r .
\tag{9}
\]
For a direct verification valid for all \(C_0\), equation (6) gives
\[
\kappa'/\kappa=2/\zeta-3D,\quad
\kappa''/\kappa=2/\zeta^2-24D/\zeta+12D^2,\quad
r''/r=2D^2-4D/\zeta.
\]
Both \(\mathcal B/\kappa\) and \(\alpha^2+2p_2d_2\) therefore equal
\(1/\zeta^2-6D/\zeta+D^2\), proving (9).

The coefficient of \(V\) independent of \(U\) in (2) gives
\[
\ell_\rho=2\kappa p_0-\lambda-(2\kappa\rho+s)^2/r,\qquad
\ell\in K[\rho]_{\le3},\qquad
\ell_3=(2\kappa d_2-4\kappa^2/r)/3 .
\tag{10}
\]
Here \(\ell_3=[\rho^3]\ell\). Membership in \(K[\rho]\) follows
by subtracting an explicit polynomial primitive, leaving a
\(\rho\)-constant. Arbitrary algebraic antiderivatives are not assumed.

Now (1) puts \(z,w\) in \(K[y,\rho]\), with exact degrees two and
three in \(\rho\) over \(K(y)\):
\[
\begin{gathered}
a_2:=[\rho^2]z=rd_2+\kappa=-\frac3{2\zeta^3F^2}\ne0,\\
b_3:=[\rho^3]w=(\ell_3-2\kappa d_2)/r
=-\frac{4\kappa}{3r}\left(d_2+\frac\kappa r\right)
=\frac{10C_1}{\zeta F^3}\ne0,\\
\gamma=b_3^2/a_2^3=-\frac{800}{27}C_1^2\zeta^7 .
\end{gathered}
\tag{11}
\]
After \(r_\rho=0\), the only possibly cubic terms of \(w\) are
\(\ell/r\) and \(-n_\rho P(y)/r\); the terms involving
\(r'yP(y)\), \(n_\tau y\), and \(k_{\tau\tau}y^2/2\) have degree
at most two in \(\rho\). This verifies (11) without dropping
projected-parameter terms.

Every coefficient of \(k,n,P,\ell\) is now in \(K[\rho]\).
The actual projected field equality therefore gives
\[
\mathbb C(y,z,w)=L(y)=K(\rho)(y),\qquad L=K(\rho).
\tag{12}
\]
The last equality is intersection with \(L\), since \(y\) is
transcendental over it. A proper projected subfield would not supply
(12); this is the essential original polynomial-inverse input.

## 4. An elementary weighted residue-field lemma

Let \(k\subset M\) be fields, let \(R\) be transcendental over \(M\),
and take \(z_2,w_3\in M[R]\) of exact degrees two and three, with
leading coefficients \(a,b\in M^*\). Suppose \(b^2/a^3\) is
transcendental over \(k\). Use the degree-at-infinity valuation,
whose ring consists of rational functions with numerator degree
no larger than denominator degree. The residue field on \(M(R)\)
is \(M\), by taking leading-coefficient quotients at equal degrees.
Its residue field on the subfield \(k(z_2,w_3)\) is exactly
\[
k(b^2/a^3).
\tag{13}
\]

Give formal \(Z,W\) weights \(2,3\). For a nonzero polynomial over
\(k\), choose one monomial \(Z^iW^j\) in its highest weighted part.
Every other monomial of that weight has exponent difference
\((3m,-2m)\), \(m\in\mathbb Z\). After factoring \(a^ib^j\), the
leading sum is a nonzero Laurent polynomial in \(b^2/a^3\).
Transcendence prevents its vanishing. Evaluation at \(z_2,w_3\)
therefore has exactly the weighted degree, and is injective.

For a quotient with valuation zero, numerator and denominator
have equal weighted degrees. The same exponent calculation shows
that the leading-coefficient quotient belongs to \(k(b^2/a^3)\).
Positive valuation gives residue zero. Conversely \(w_3^2/z_2^3\)
has residue \(b^2/a^3\). This proves both inclusions in (13).

The transcendence hypothesis is essential. With \(k=\mathbb C\),
\(M=\mathbb C(t)\), \(z_2=R^2\), \(w_3=R^3+t\), the leading ratio
is one. Nevertheless \((w_3^2-z_2^3)/w_3\) has residue \(2t\).
Cancellation can recover coefficient information when the leading
ratio is algebraic, unlike the situation in (11).

## 5. The actual field equality is impossible

Apply the lemma with \(k=\mathbb C(y)\), \(M=K(y)\), \(R=\rho\),
and the actual projected \(z,w\). Their leading ratio in (11) is
a nonzero complex multiple of \(\zeta^7\), transcendental over
\(\mathbb C(y)\): \(\zeta\in K\) is transcendental over \(\mathbb C\),
and \(y\) is transcendental over \(K\).
The lemma gives residue field \(\mathbb C(y,\zeta^7)\).
But (12) identifies the ambient subfield \(\mathbb C(y,z,w)\)
itself with \(K(y)(\rho)\), whose
degree-at-\(\rho\)-infinity residue field is \(K(y)\). Thus
\[
K(y)=\mathbb C(y,\zeta^7),\qquad K=\mathbb C(\zeta^7).
\tag{14}
\]
The second equality follows by intersecting with \(K\), using the
transcendence of \(y\). It is impossible because \(\zeta\in K\)
but \(\zeta\notin\mathbb C(\zeta^7)\). Indeed the automorphism
\(\zeta\mapsto\omega\zeta\) of \(\mathbb C(\zeta)\), for a primitive
seventh root of unity \(\omega\), fixes \(\mathbb C(\zeta^7)\)
and does not fix \(\zeta\).

This contradiction excludes (2). For an actual quadratic graph in
the stated chart, the whole potential is associated to its selected
graph equation; the nonconstant extra factor cannot occur.
The argument does not construct an invariant coordinate for that
remaining graph, exclude extra factors when \(y\) is constant, or
resolve other cusp and initial-kernel branches. No unit selected
speed or polynomial description of the whole invariant surface
has been assumed.

## Sources and verification scope

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md), for the actual projected field, determinant, potential and orientation.
2. [Selected-factor reduction159](cusp-generic-selected-factor-reduction-pass159-working.md), for the full unit-cofactor remainder yielding (2).

The reciprocal differential equation, its solution over the exact
field, polynomial coefficient return, and residue-field lemma are
proved here. No external classification or finite symbolic test
substitutes for them. Independent AI reviews are not expert
verification, proof-assistant certification, or novelty clearance.
Earlier artifacts are not edited.
