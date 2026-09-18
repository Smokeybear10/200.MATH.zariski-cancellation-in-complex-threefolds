# Polynomial correction for every normalized generic graph

In a supplied dense three-good frame, suppose the generic embedded
line is a graph in the axes furnished by the leading normalization153.
Then the leading mixed relation has an actual invariant polynomial
correction in every minimum degree \(m\ge2\). The correction is an
ambient coordinate and can be put in the form
\(I=X_0W_0-F(Y)-\delta Z\), where \(F\) has degree \(m+1\) and
\(\delta\in\mathbb C^*\).

The separate normalized-suspension recognition proof153 then gives
\(\ker E\simeq\mathbb C^{[3]}\). The graph hypothesis is essential
to this proof. A generic embedded line need not be a graph in these
fixed axes, and no arbitrary-coordinate entry is established here.

## 1. Exact normalized data and the additional graph hypothesis

Use the actual leading normalization153 and chart139:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad \deg_EW=\mu=m\ge2,\qquad d=m+1,\\
s=EX\ne0,\quad \tau=EY/s,\quad \rho=EZ/s,\quad
L/\mathbb C(\tau,\rho)\text{ finite separable},\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad A_L=L[v]=L[y,z],\\
f_m=\gamma\tau^d,\quad \gamma\in\mathbb C^*,\qquad
\ker\theta=(\mathsf X\mathsf W-\gamma\mathsf Y^d).
\end{gathered}
\tag{1}
\]
The original weights are \((1,1,1,m)\). All displayed original
coordinates and coordinate changes are actual. The last equation
is the full initial-map kernel, not the full associated graded ring.
The fixed-good minimum is unchanged by the shears below.

The canonical signed tails from139, with independent formal \(U,V\),
satisfy
\[
\begin{gathered}
\Phi=-\sum_{j=0}^m H_{j+1}(f_j;U,V)-f_{-1},\qquad
\Phi(y,z)=0,\quad \Phi_d=-\gamma U^d,\\
\Psi=-\sum_{j=0}^m H_{j+2}(f_j;U,V)-H_1(f_{-1};U,V),\\
\Psi(y,z)=v+c_0,\qquad
(\Psi_U,\Psi_V)=(\Phi_\tau,\Phi_\rho),\qquad
\Phi\in L^*g.
\end{gathered}
\tag{2}
\]
Here \(H_r\) denotes the homogeneous order-\(r\) coefficient Taylor
polynomial, including its factorial denominators. The association
to the whole generic kernel generator \(g\) is theorem145.

Assume additionally \(\deg_v y=1\). Equivalently in these fixed axes,
\[
\Phi=\lambda V+P(U),\qquad \lambda\in L^*,\quad
\deg P=d,\quad [U^d]P=-\gamma .
\tag{3}
\]
Indeed \(L[y]=L[v]\) then makes \(z\) a polynomial in \(y\); the
exact prime equation is its graph. Conversely a graph equation
gives \(L[y,z]=L[y]\), so a polynomial \(y(v)\) generating \(L[v]\)
has degree one. No coefficient-dependent plane change is being
substituted for this hypothesis.

## 2. The graph slope is a complex constant

Since \(f_m=\gamma\tau^d\), its derivatives of order \(d+1\) vanish.
All other terms of \(\Psi\) in (2) have degree at most \(d\).
Thus \(\deg\Psi\le d\), an improvement of the general bound \(d+1\).

The quotient value \(\Psi(y,z)=v+c_0\) is affine in \(y\).
Consequently, in the polynomial ring \(L[U,V]\),
\[
\Psi=\alpha U+\beta+c\Phi,\qquad
\alpha\in L^*,\quad \beta,c\in L.
\tag{4}
\]
The difference is divisible by the exact kernel \(\Phi\). Its
degree is at most \(d=\deg\Phi\), so the quotient is constant,
including the possibility \(c=0\).

Neither \(\Psi_U=\alpha+cP_U\) nor \(\Psi_V=c\lambda\) has a term
in \(V\). Comparing with the two coefficient derivatives in (2)
therefore gives \(\lambda_\tau=\lambda_\rho=0\).
The common constant field of the two derivations on \(L\) is
\(\mathbb C\): differentiating a minimal polynomial over
\(\mathbb C(\tau,\rho)\) proves that a common constant is algebraic
over \(\mathbb C\), which is algebraically closed.
Write
\[
\lambda=-\delta,\qquad \delta\in\mathbb C^*.
\tag{5}
\]
This is coefficient comparison before localization at any divisor.

## 3. Removing the polynomial mixed coefficients by actual shears

Put \(K=\ker(\partial_\rho:L\to L)\). It is finite over
\(\mathbb C(\tau)\). To see this, the monic minimal polynomial
of any \(\partial_\rho\)-constant over \(\mathbb C(\tau,\rho)\)
has coefficients in \(\mathbb C(\tau)\), by differentiation and
minimality. Conversely separable algebraicity over
\(\mathbb C(\tau)\) forces \(\partial_\rho\)-constancy.
Linear independence persists after adjoining the transcendental
\(\rho\); the finite degree of \(L/\mathbb C(\tau,\rho)\) bounds
the resulting algebraic constant extension. In particular
\(\operatorname{trdeg}_{\mathbb C}K=1\), and \(\partial_\tau\)
preserves \(K\).

For \(1\le j<m\), the homogeneous degree \(j+1\) part of (3)
contains no monomial involving \(V\). Therefore every mixed
derivative of total order \(j\) of \(\partial_\rho f_j\) vanishes.
An element of \(L\) with all order-\(j\) partial derivatives zero
is a complex polynomial in \(\tau,\rho\) of degree at most \(j-1\).
Here is an elementary induction: its order-\((j-1)\) derivatives
are common constants; subtract the homogeneous polynomial with
those prescribed constant derivatives, and repeat at lower orders.
The case \(j=1\) is the common-constant assertion just proved.

Integrating that complex polynomial in \(\rho\) gives a polynomial
\(q_j\in\mathbb C[\tau,\rho]\) of total degree at most \(j\), with
\(\partial_\rho q_j=\partial_\rho f_j\).
The expression
\[
Q_j(X,Y,Z)=X^j q_j(Y/X,Z/X)\in\mathbb C[X,Y,Z]
\tag{6}
\]
is a homogeneous complex polynomial of ordinary degree \(j\).
Its apparent denominators cancel monomial by monomial.
Its exact Taylor expression is \(X^j\Theta(q_j)\) and has no
negative powers of \(X\). Replacing \(W\) by
\(W-\sum_{j=1}^{m-1}Q_j\) is thus an actual polynomial shear.
It replaces exactly \(f_j\) by \(f_j-q_j\) at those indices;
the other canonical coefficients and both negative tails are
unchanged. It preserves the initial relation and degree \(m\).

Rename the sheared coordinate \(W\). Using primes for
\(\partial_\tau\) on \(K\), the coefficients now have the form
\[
f_j=h_j\in K\ (1\le j\le m),\qquad
h_m=\gamma\tau^d,\qquad f_0=\delta\rho+h_0,\quad h_0\in K.
\tag{7}
\]
The last assertion follows from \(\Phi_V=-\delta=-f_{0,\rho}\).

The highest-degree part of \(\Psi\) in (2) is now
\(-h_{m-1}^{(d)}U^d/d!\). Comparison with (4) gives
\[
c=\frac{h_{m-1}^{(d)}}{\gamma d!}\in K.
\tag{8}
\]
This also holds when that derivative and \(c\) are zero.
Since all higher coefficients in (7) are killed by
\(\partial_\rho\), and \(\delta\) is constant,
\(\Psi_V=-f_{-1,\rho}\). Equations (4)--(5) then give
\[
f_{-1}=c\delta\rho+h_{-1},\qquad h_{-1}\in K.
\tag{9}
\]

## 4. An exact weight-\(d\) equation over the one-variable field

Define polynomials over \(K\) by
\[
\begin{gathered}
H(X,y)=\sum_{j=0}^m\sum_{a=0}^j
             \frac{h_j^{(a)}}{a!}\,y^aX^{j-a},\\
G(y)=\sum_{j=0}^m
             \frac{h_j^{(j+1)}}{(j+1)!}\,y^{j+1}.
\end{gathered}
\tag{10}
\]
The actual nonnegative Taylor part and first relation are
\(W=\delta\rho+H(X,y)\) and
\(G(y)+\delta z+c\delta\rho+h_{-1}=0\).
Substitute \(y=Y-\tau X,\ z=Z-\rho X\) and eliminate
\(\delta\rho=W-H(X,y)\). This gives the actual identity
\[
\mathcal F=
\delta Z-(X-c)W+(X-c)H(X,Y-\tau X)
       +G(Y-\tau X)+h_{-1}=0.
\tag{11}
\]
Regard \(\mathcal F\) also as a polynomial in four independent
formal coordinates over \(K\). It is irreducible because its
\(Z\)-coefficient is the nonzero field constant \(\delta\).
Its weight is exactly \(d\), with highest part
\[
\operatorname{in}_{\rm wt}\mathcal F=-XW+\gamma Y^d.
\tag{12}
\]
Indeed the \(j=m\) terms satisfy
\(XH_m(X,y)+\gamma y^d=\gamma(\tau X+y)^d\)
by the binomial theorem. Every other term in (11) has smaller
weight. The notation \(\mathcal F=0\) is an evaluated identity;
the formal polynomial \(\mathcal F\) is nonzero.

## 5. Exact-field descent makes the correction polynomial

The field \(K\subset\operatorname{Frac}A\) is a
transcendence-degree-one subfield of
\(\operatorname{Frac}B=\mathbb C(X,Y,Z,W)\).
The classical generalized Lüroth theorem gives \(K=\mathbb C(a)\).
Write \(a=p/q\) with \(p,q\in A\) and remove their common
ambient polynomial factors. Factorial closure of \(A\) keeps
both resulting coprime polynomials in \(A\).

Over exactly \(K\), the kernel of formal-coordinate evaluation
into \(\operatorname{Frac}B\) is generated by \(p-aq\).
For clarity, introducing an independent parameter \(T\),
\(p-Tq\) is primitive and irreducible in
\(\mathbb C[X,Y,Z,W,T]\); its ideal misses
\(\mathbb C[T]\setminus\{0\}\). Localization to \(\mathbb C(T)\)
therefore gives the exact prime kernel. This is the elementary
rational-pencil argument134, not a selected factor over an
enlarged coefficient field.

Since \(\mathcal F\) is irreducible and evaluates to zero, it
is a \(K^*\)-multiple of \(p-aq\). The coordinate support of
\(p-Tq\) is the union of the supports of \(p,q\), because \(T\)
is transcendental over \(\mathbb C\). Thus
\[
\max(\operatorname{wt}p,\operatorname{wt}q)=d.
\tag{13}
\]
At least one of \(p,q\) is a nonconstant invariant. Equation (1)
implies that no such invariant has weight below \(d\), and every
weight-\(d\) invariant has top a scalar multiple of
\(XW-\gamma Y^d\). Hence, for one such \(I_0\),
\(\mathcal F_dA=\mathbb C\oplus\mathbb CI_0\).
Writing \(p,q\) in that two-dimensional space and comparing (12)
shows that the coefficient of \(I_0\) in \(\mathcal F\) is a
nonzero complex constant. All coefficients of nonconstant
coordinate monomials in \(\mathcal F\) are consequently complex.
In particular \(c\in\mathbb C\).

Discarding the constant coordinate monomial in \(\mathcal F\)
therefore gives an actual invariant
\[
J=\delta Z-(X-c)W+P_0(X,Y)\in A,\qquad
P_0\in\mathbb C[X,Y],\quad
\operatorname{in}_{\rm wt}P_0=\gamma Y^d.
\tag{14}
\]
Its coefficient of \(Z\) is a complex unit, so \(J\) is an
ambient coordinate. Divide \(P_0\), as a polynomial in \(X\),
by \(X-c\):
\[
P_0=(X-c)Q(X,Y)+F(Y),\qquad
X_0=X-c,\quad W_0=W-Q(X,Y),\quad I=-J.
\tag{15}
\]
Then \(I=X_0W_0-F(Y)-\delta Z\), with
\(\deg F=d\), leading coefficient \(\gamma\), and
\(\deg Q\le m\). These are actual elementary polynomial
changes. They preserve the three good second derivatives and
give \(\deg_EW_0\le m\); minimality makes it exactly \(m\).
In fact the top \(\gamma Y^d\) has no \(X\), so the quotient
does not introduce a higher leading term.

## 6. Recognition, including every prime generic degree

The given slice makes \(E\) fixed-point free. The separate
[all-degree normalized-suspension proof](normalized-suspension-recognition-pass153-working.md)
applies to (15): \(EX_0\in\mathbb C^*\), and it supplies explicit
polynomial generators of \(A\). Thus the additional generic graph
hypothesis yields global recognition in every minimum degree.
The general divisor estimates152 are not needed for this route.

There is an unconditional degree corollary within the supplied
dense frame. If \(d=\mu+1\) is prime, the graph hypothesis follows.
The normalized leading equation \(-\gamma U^d\) has its unique
infinity point at \([0:1:0]\). The polynomial parametrization and
degree equality139 therefore give
\[
\deg_v z=d,\qquad 0<\deg_v y<d.
\tag{16}
\]
If \(y\) were constant, the whole curve equation would have degree
one, contrary to \(d\ge3\). The Abhyankar--Moh--Suzuki degree
divisibility theorem, over the exact characteristic-zero field
\(L\), says that one of the two parametric degrees divides the
other. Primality of \(d\) now forces \(\deg_v y=1\).
No plane coordinate change over \(L\) is needed for this deduction.
For example it includes minimum \(\mu=4\), as well as the
already recognized \(\mu=2\).

The remaining quartic case is also exhausted. If \(\mu=3\), then
\(d=4\) and the same degree argument gives
\(\deg_v y\in\{1,2\}\), with \(\deg_v z=4\).
The first possibility is the graph handled above.
The second is excluded by the independent
[nested-quartic proof153](nested-quartic-exclusion-pass153-working.md).
Consequently every supplied actual dense frame of minimum
\(\mu=3\) has \(A\simeq\mathbb C^{[3]}\) as well.
This exhaustion uses degree divisibility, not a claim that
every quartic plane coordinate is a graph.

## 7. The remaining nongraph and entry problems

This proof does not apply a coefficient-dependent plane change
to turn an arbitrary embedded line into a graph. Such a change
need not come from an allowed original-coordinate transformation.
Other nongraph degrees and the arbitrary three-good entry
problem remain outside this conclusion. No assertion of historical
novelty, expert review, complete dependency audit, or formal
proof-assistant verification is made.

## Sources and independent inputs

1. [All-degree leading normalization153](dense-all-degree-leading-normalization-pass153-working.md):
   actual normalized leading coefficient and full weighted initial kernel.
2. [Actual chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [signed tails139](dense-negative-tail-relations-pass139-working.md),
   and [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md):
   canonical coefficients, whole generic line and exact gradient identities.
3. [Rational-pencil weight descent134](rational-pencil-weight-descent-pass134-working.md):
   the exact-field prime-kernel argument and polynomial weight bound.
   The graph descent also extends the method of
   [the quadratic correction proof134](primitive-cubic-correction-existence-pass134-working.md).
4. Michiel de Bondt, [arXiv:1501.06046v4](https://arxiv.org/pdf/1501.06046v4),
   Theorem 1.1, printed p. 4: the classical rationality theorem for
   a transcendence-degree-one subfield of a rational field.
   This field theorem is an external input, not a new rationality claim.
5. Leonid Makar-Limanov,
   [*A new proof of the Abhyankar-Moh-Suzuki Theorem*](https://arxiv.org/pdf/1212.0163v1),
   AMS Theorem, printed p. 1: divisibility of the degrees of two
   polynomials generating a one-variable polynomial ring in
   characteristic zero. Only that statement is invoked for (16).
