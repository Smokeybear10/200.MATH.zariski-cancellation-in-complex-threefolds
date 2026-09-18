# A second-return no-slice test for the fixed DG base

## Status and scope

This note proves a second-section return criterion for one explicit
homogeneous three-variable locally nilpotent derivation. It applies that
criterion to the whole polynomial \(Q_{17}\) below and proves that its
four-variable extension has no polynomial slice.

The conclusion is not a general degree bound for rank-three bases. In
particular, it does not say that every coefficient missed by a different
return section is sliced or unsliced. No novelty, coordinate-entry, or
general cancellation claim is made. No neighboring working source is
used as a proof input.

## 1. The actual base and its localized orbit coordinates

In \(R=\mathbb C[x,y,z]\), put
\[
 \begin{split}
 f&=xz-y^2,\\
 r&=x^3+yf,\\
 g&=zf^2+2x^2yf+x^5
    =zf^2+2x^2r-x^5.
 \end{split}
 \tag{1}
\]
The identity \(xg=r^2+f^3\) holds in the whole polynomial ring.
Use the Jacobian orientation
\[
 H(F)=\det\frac{\partial(f,g,F)}{\partial(x,y,z)}.
 \tag{2}
\]
Direct polynomial differentiation gives
\[
 \begin{split}
 Hf&=Hg=0,\qquad Hr=-fg,\\
 Hx&=-2fr,\\
 Hy&=6x^2r-g,\\
 Hz&=10x^4y+f(8xy^2+2x^2z).
 \end{split}
 \tag{3}
\]
These are entire identities, not formal gradients evaluated after a
coordinate substitution.

The localization has the explicit presentation
\[
 R_{fg}=\mathbb C[f,f^{-1},g,g^{-1},r],
 \qquad
 \begin{split}
 x&=\frac{r^2+f^3}{g},\\
 y&=\frac{r-x^3}{f},\\
 z&=\frac{g-2x^2r+x^5}{f^2}.
 \end{split}
 \tag{4}
\]
The Jacobian identity \(Hr=-fg\ne0\) also shows that \(f,g,r\) are
algebraically independent. In (4), \(H=-fg\,\partial_r\).
Each original coordinate is a polynomial in \(r\) with coefficients in
\(\mathbb C[f^{\pm1},g^{\pm1}]\). Thus (3) is locally nilpotent on \(R\),
with exact degrees
\[
                 \deg_H(x,y,z)=(2,6,10).
 \tag{5}
\]
Its ordinary homogeneous derivation degree is \(4\). The localization is
used for exact orbit calculations, not to substitute localized
sliceness for a whole polynomial slice.

For any ordinary homogeneous \(\psi\in R\) of positive degree \(\ell\),
consider
\[
                   E=H+(1+\psi)\partial_t
                   \quad\hbox{on }R[t].
 \tag{6}
\]
This is a whole locally nilpotent derivation: its restriction to \(R\)
is \(H\), and \(E^it=H^{i-1}(1+\psi)\) for \(i\ge1\).

## 2. The second return section and its exact endpoint

Take a starting point
\[
                     (x,y,z)=(X,0,X\lambda).
 \tag{7}
\]
Its invariant values and initial \(r\)-value are
\[
 f=X^2\lambda,\qquad
 g=X^5(1+\lambda^3),\qquad r=X^3.
 \tag{8}
\]
Write \(r=X^3v\) along the orbit, and define
\[
 \begin{split}
 A(v,\lambda)&=\frac{\lambda^3+v^2}{1+\lambda^3},\\
 B(v,\lambda)&=\frac{v-A(v,\lambda)^3}{\lambda},\\
 C(v,\lambda)&=\frac{1+\lambda^3-2vA(v,\lambda)^2+
                                 A(v,\lambda)^5}{\lambda^2}.
 \end{split}
 \tag{9}
\]
The exact base coordinates are \((XA,XB,XC)\). Indeed, these are (4)
with the values (8); they satisfy
\[
 AC-B^2=\lambda,\qquad
 A^3+\lambda B=v,\qquad
 \lambda^2C+2A^2v-A^5=1+\lambda^3.
 \tag{10}
\]
At \(v=1\), they give \((A,B,C)=(1,0,\lambda)\).

Choose a primitive fifth root of unity \(\omega\), and solve
\[
 W^6-(1+\lambda^3)W+\lambda^3=0,\qquad W(0)=\omega.
 \tag{11}
\]
The derivative with respect to \(W\) at \((\lambda,W)=(0,\omega)\)
is \(6\omega^5-1=5\). Consequently there is a unique
\(W(\lambda)\in\mathbb C[[\lambda]]\) with the stated properties.
Equivalently, writing \(L=\lambda^3\), there is a series
\(\widehat W(L)\) such that
\[
 W(\lambda)=\widehat W(\lambda^3),\qquad
 \widehat W(L)=\omega+\frac{\omega-1}{5}L+O(L^2).
 \tag{12}
\]
This is the first formal implicit solve. Coefficient recursion gives
it directly, since each new coefficient has nonzero multiplier \(5\).

At \(v=W(\lambda)^3\), the exact equation (11) gives
\[
             A=W,\qquad B=0,\qquad C=\lambda/W.
 \tag{13}
\]
For the last equality one may use (10), since \(W\) is a unit.
Thus the endpoint is
\[
                       (XW,0,X\lambda/W).
 \tag{14}
\]
No leading-term truncation is used in this endpoint equality.

Since \(Hr=-fg\), the time differential and the full connecting time are
\[
 d\tau=-\frac{X^{-4}}{\lambda(1+\lambda^3)}\,dv,\qquad
 \tau=-\frac{X^{-4}(W^3-1)}{\lambda(1+\lambda^3)}.
 \tag{15}
\]
For a homogeneous coefficient of degree \(\ell\), define the Laurent
series
\[
 I_\psi(\lambda)=
 \int_1^{W(\lambda)^3}
       \psi(A(v,\lambda),B(v,\lambda),C(v,\lambda))\,dv.
 \tag{16}
\]
This notation means a polynomial antiderivative in \(v\), with rational
coefficients in \(\lambda\), evaluated at the indicated formal endpoint.
It involves no analytic integration or convergence assumption.

The entire \(t\)-displacement from \(t=0\) is exactly
\[
 \Delta t=
 -\frac{X^{-4}}{\lambda(1+\lambda^3)}
       \left[W(\lambda)^3-1+X^\ell I_\psi(\lambda)\right].
 \tag{17}
\]
Homogeneity supplies the factor \(X^\ell\). All coefficients of \(\psi\)
are retained in (16)--(17).

## 3. A precise second-section pole criterion

**Proposition.** In the setting (1)--(6), suppose that for some primitive
fifth root \(\omega\) and the corresponding branch (11),
\[
 I_\psi(\lambda)=\lambda^{-K}J(\lambda),\qquad
 K>0,\qquad J\in\mathbb C[[\lambda]],\qquad J(0)\ne0.
 \tag{18}
\]
Then \(E\) has no polynomial slice in \(R[t]\).

To prove this, introduce an independent formal parameter \(s\) and put
\[
                  \lambda=s^\ell,\qquad X=s^K V(s).
 \tag{19}
\]
The bracket in (17) becomes
\[
             W(s^\ell)^3-1+V(s)^\ell J(s^\ell).
 \tag{20}
\]
Choose a nonzero complex \(V_0\) satisfying
\[
                   V_0^\ell J(0)=-(\omega^3-1).
 \tag{21}
\]
This is possible because \(\ell>0\), \(J(0)\ne0\), and
\(\omega^3-1\ne0\).
The derivative of (20) with respect to \(V\) at \((s,V)=(0,V_0)\)
is the nonzero number \(\ell V_0^{\ell-1}J(0)\).
A second formal coefficient recursion therefore supplies a unit
\(V(s)\in\mathbb C[[s]]\) making (20) identically zero.

The two points
\[
 \begin{split}
 p_s&=(X(s),0,X(s)s^\ell,0),\\
 q_s&=(X(s)W(s^\ell),0,X(s)s^\ell/W(s^\ell),0)
 \end{split}
 \tag{22}
\]
are integral over \(\mathbb C[[s]]\). The exact base endpoint identities
and (20) show that the full \(E\)-flow connects them. Its time has order
\[
                          \operatorname{ord}_s\tau=-4K-\ell<0.
 \tag{23}
\]
Its leading coefficient is
\(-V_0^{-4}(\omega^3-1)\ne0\).

All orbit computations are legitimate in \(\mathbb C((s))\): \(X\),
\(\lambda\), and \(1+\lambda^3\) are nonzero there, and the original
\(E\)-flow is a finite polynomial flow. If a whole polynomial \(u\)
satisfied \(Eu=1\), its finite flow identity would give
\[
                           u(q_s)-u(p_s)=\tau(s).
 \tag{24}
\]
The left side belongs to \(\mathbb C[[s]]\), while (23) is a pole.
This proves the proposition. It is a sufficient obstruction, not an
assertion that absence of a pole implies slicedness.

## 4. The full coefficient \(Q_{17}\)

Take
\[
 Q_{17}=-43x^3yz+4x^2y^3-13x^2z^3
                   -13xy^2z^2+26y^4z.
 \tag{25}
\]
It is ordinary homogeneous of degree \(5\).
The subscript records its actual \(H\)-degree, which can be verified
without iterating a truncated polynomial. Using \(y^2=xz-f\) and (1)
gives the exact localized identity
\[
 Q_{17}
 =\frac{z}{f}\left(39x^3r-39xg+26f^3\right)-4x^2r+4x^5.
 \tag{26}
\]
In the polynomial-in-\(r\) presentation (4), the first displayed
product has unique highest degree \(10+7=17\).
Its leading coefficient is
\[
                             \frac{39}{f^3g^8}\ne0.
 \tag{27}
\]
All other terms have lower \(r\)-degree. Thus \(\deg_HQ_{17}=17\),
and \(\deg_E t=18\) for \(\psi=Q_{17}\).
Here \(d=4\), \(\ell=5\), \(q=\ell-d=1\), and the maximum linear
\(H\)-degree is \(N=10\). These degree statements alone are not the
no-slice proof; the exact return calculation follows.

## 5. Why the apparent order-six pole vanishes identically

For this calculation let \(L=\lambda^3\) and abbreviate
\[
 a=\frac{L+v^2}{1+L},\qquad
 b=v-a^3,\qquad
 c=1+L-2va^2+a^5.
 \tag{28}
\]
Thus the normalized coordinates (9) are \((a,b/\lambda,c/\lambda^2)\).
The complete numerator of the apparent pole of order six is
\[
 \begin{split}
 \mathcal N(L,v)
 &:=
 \lambda^6 Q_{17}(a,b/\lambda,c/\lambda^2)\\
 &=L(-43a^3bc+4a^2b^3)
                 -13a^2c^3-13ab^2c^2+26b^4c.
 \end{split}
 \tag{29}
\]
It is regular as a formal power series in \(L\), with polynomial
coefficients in \(v\).
At \(L=0\),
\[
                  a=v^2,\qquad
                  b=v(1-v^5),\qquad c=(1-v^5)^2.
 \tag{30}
\]
Consequently the last three terms in (29) become
\[
       (-13-13+26)v^4(1-v^5)^6=0.
 \tag{31}
\]
Thus the order-six numerator vanishes identically as a polynomial in
\(v\), before integration and before choosing any endpoint.
There is no reliance on cancellation merely at a fifth root.

The first derivatives of (28) at \(L=0\) are
\[
 \begin{split}
 a_L&=1-v^2,\\
 b_L&=-3v^4(1-v^2),\\
 c_L&=1-4v^3(1-v^2)+5v^8(1-v^2).
 \end{split}
 \tag{32}
\]
Differentiating all terms of (29), and substituting (30)--(32), gives
the exact polynomial identity
\[
                 \mathcal N_L(0,v)=39v^2(v^5-1)^3.
 \tag{33}
\]
In particular the normalized whole coefficient has the expansion
\[
 Q_{17}(A,B,C)
       =39\lambda^{-3}v^2(v^5-1)^3+O(1).
 \tag{34}
\]
Here the remainder belongs to
\(\mathbb C[v][[\lambda^3]]\). No pole orders four or five are omitted:
the whole numerator depends on \(\lambda\) only through \(L=\lambda^3\).

## 6. The nonzero integral coefficient and the exact no-slice result

The endpoint satisfies \(W(\lambda)=\omega+O(\lambda^3)\).
Since the order-six integrand is identically zero, there is no endpoint
correction from that order. Equations (16) and (34) give
\[
 I_{Q_{17}}(\lambda)
 =39\lambda^{-3}\int_1^{\omega^3}v^2(v^5-1)^3\,dv+O(1).
 \tag{35}
\]
The antiderivative is
\[
 39\left(\frac{v^{18}}{18}
       -\frac{3v^{13}}{13}
       +\frac{3v^8}{8}
       -\frac{v^3}{3}\right).
 \tag{36}
\]
At \(v=\omega^3\), all four powers in (36) equal \(\omega^4\).
Moreover
\[
 39\left(\frac1{18}-\frac3{13}+\frac3{8}-\frac1{3}\right)
                         =-\frac{125}{24}.
 \tag{37}
\]
Therefore
\[
 I_{Q_{17}}(\lambda)
       =\frac{125}{24}(1-\omega^4)\lambda^{-3}+O(1).
 \tag{38}
\]
The leading coefficient is nonzero for every primitive fifth root
\(\omega\). This is an exact cyclotomic calculation, not a numerical
evaluation.

Apply the proposition with \(K=3\) and \(\ell=5\). Explicitly, set
\[
 J(\lambda)=\lambda^3I_{Q_{17}}(\lambda),\qquad
 \lambda=s^5,\qquad X=s^3V(s),
 \tag{39}
\]
and choose
\[
 V_0^5\frac{125}{24}(1-\omega^4)=-(\omega^3-1).
 \tag{40}
\]
The second implicit solve makes
\(W(s^5)^3-1+V(s)^5J(s^5)=0\) exactly.
The endpoints in (22) then have coordinate orders at least \(3\) in
\(x\) and at least \(8\) in \(z\), with \(y=t=0\).
The exact nonzero connecting time has
\[
                             \operatorname{ord}_s\tau=-17.
 \tag{41}
\]
The polynomial slice identity (24) is impossible. Hence
\[
                     H+(1+Q_{17})\partial_t
                     \quad\hbox{has no polynomial slice.}
 \tag{42}
\]

## 7. Verification and retained limits

Fresh unsaved symbolic calculations independently reconstructed the
Jacobian in (2), all identities in (3), the whole localized polynomial
\(Q_{17}\), its degree \(17\), and its leading coefficient (27).
They also checked all three normalized coordinate differential equations
and all exact return identities modulo
\(W^6-(1+\lambda^3)W+\lambda^3\).

A separate complete numerator calculation checked (29)--(33), including
the identically zero constant coefficient and the full polynomial
\(39v^2(v^5-1)^3\), and reduced the integral coefficient modulo
\(\omega^4+\omega^3+\omega^2+\omega+1\). The proof of the two implicit
solves and the pole-time contradiction is given directly above.
No finite grid or bounded slice search is substituted for that proof.

This result closes the slice question for the specific coefficient
(25). The proposition can be applied to other coefficients only after
its exact Laurent-pole hypothesis has been established. It does not
prove a rank-three slice-degree window in general, recognize arbitrary
sliced extensions, or supply a cancellation counterexample.

No saved checker was executed, imported, or compiled. No prior source
or canonical record was edited. This working source requires its own
independent saved-source review after the author's full read and final
HELD hash.
