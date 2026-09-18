# Slices for the invariant-coefficient extension of the fixed DG base

## Status and bounded conclusion

For the explicit base \(H\) defined below, this note completely resolves
the one-parameter family
\[
                    E_\lambda=H+(1+\lambda g)\partial_t,
                    \qquad \lambda\in\mathbb C.
 \tag{1}
\]
It has a whole polynomial slice if and only if \(\lambda=0\).
For \(\lambda=0\), an entire polynomial automorphism explicitly rectifies
it to a translation. For every nonzero \(\lambda\), an exact formal
return with a pole in its time excludes a polynomial slice.
An independent algebraic proof of the latter conclusion is also given.

This is only a classification of (1). No reduction of all homogeneous
degree-five coefficients to (1) is assumed or proved here. No unfinished
source is an input. There is no general rank-three recognition,
coordinate-entry, cancellation, or novelty claim.

## 1. The whole base and exact orbit coordinates

In \(R=\mathbb C[x,y,z]\), set
\[
 \begin{split}
 f&=xz-y^2,\\
 r&=x^3+yf,\\
 g&=zf^2+2x^2yf+x^5
     =zf^2+2x^2r-x^5,
 \end{split}
 \qquad
 H(F)=\det\frac{\partial(f,g,F)}{\partial(x,y,z)}.
 \tag{2}
\]
The following are entire polynomial identities:
\[
 \begin{split}
 xg&=r^2+f^3,\\
 Hf&=Hg=0,\qquad Hr=-fg,\\
 Hx&=-2fr,\qquad Hy=6x^2r-g,\\
 Hz&=10x^4y+f(8xy^2+2x^2z).
 \end{split}
 \tag{3}
\]
In particular \(f,g,r\) are algebraically independent: their Jacobian
is \(-fg\ne0\). The localization is
\[
 R_{fg}=\mathbb C[f,f^{-1},g,g^{-1},r],
 \qquad
 \begin{split}
 x&=\frac{r^2+f^3}{g},\\
 y&=\frac{r-x^3}{f},\\
 z&=\frac{g-2x^2r+x^5}{f^2},
 \end{split}
 \qquad H=-fg\,\partial_r.
 \tag{4}
\]
The three coordinate polynomials in (4) have respective \(r\)-degrees
\(2,6,10\). Thus \(H\) is locally nilpotent on the original ring.
Equation (1) is also a whole locally nilpotent derivation because
\(1+\lambda g\) is \(H\)-invariant. In particular its \(t\)-flow is
exactly
\[
                        t\longmapsto t+(1+\lambda g)\tau.
 \tag{5}
\]
All localization calculations below describe this original polynomial
flow; localized slices are not substituted for whole slices.

## 2. The zero parameter is explicitly rectified

Extend \(H\) to \(R[t]\) by \(Ht=0\). Then \(tH\) is locally nilpotent.
Define the whole polynomials
\[
 \xi_x=\exp(-tH)x,\qquad
 \xi_y=\exp(-tH)y,\qquad
 \xi_z=\exp(-tH)z.
 \tag{6}
\]
Each exponential is a finite sum. Here it really is the exponential
of the derivation \(-tH\), since \(H\) kills \(t\).
The automorphisms \(\exp(-tH)\) and \(\exp(tH)\) are mutual inverses.
Equivalently, in independent variables \((\xi_x,\xi_y,\xi_z,T)\) the
inverse is
\[
 (x,y,z)=\Phi_T(\xi_x,\xi_y,\xi_z),\qquad t=T,
 \tag{7}
\]
where \(\Phi_T\) is the finite polynomial \(H\)-flow.
The flow group law verifies both substitution orders.

For \(E_0=H+\partial_t\), differentiation of (6) gives
\[
                     E_0\xi_x=E_0\xi_y=E_0\xi_z=0,
                     \qquad E_0t=1.
 \tag{8}
\]
Consequently
\[
 R[t]=\mathbb C[\xi_x,\xi_y,\xi_z,t],\qquad
 E_0=\partial_t\ \hbox{in these coordinates},\qquad
 \ker E_0=\mathbb C[\xi_x,\xi_y,\xi_z].
 \tag{9}
\]
This is an actual polynomial rectification, not only a quotient-field
description.

## 3. A pole-time return for every nonzero parameter

Fix \(\lambda\ne0\), and put
\[
                         c=-1/\lambda\ne0.
 \tag{10}
\]
On the invariant fiber \(g=c\), the entire \(t\)-velocity (5) is zero.
Choose \(a\in\mathbb C^*\) with \(a^5=c\), and choose a primitive fifth
root of unity \(\omega\). Let \(s\) be an independent formal parameter.

The equation
\[
                         X^6-cX+s^3=0
 \tag{11}
\]
has two formal roots \(X_1(s),X_2(s)\in\mathbb C[[s]]\) specified by
\[
                         X_1(0)=a,\qquad X_2(0)=\omega a.
 \tag{12}
\]
Indeed its derivative in \(X\) at either initial root is \(5c\ne0\).
Coefficient recursion gives a unique root for each initial value;
both are units. In particular
\[
 X_1(s)=a-\frac{s^3}{5c}+O(s^6),\qquad
 X_2(s)=\omega a-\frac{s^3}{5c}+O(s^6).
 \tag{13}
\]
No convergence or algebraicity of a chosen parametrization is needed
for the formal evaluation argument.

Consider the two whole-coordinate points
\[
                  p_i(s)=(X_i(s),\,0,\,s/X_i(s),\,0),
                  \qquad i=1,2.
 \tag{14}
\]
Both belong to \(\mathbb C[[s]]^4\). Equations (2) and (11) give the
exact invariant and orbit-coordinate values
\[
                  f(p_i)=s,\qquad
                  g(p_i)=X_i^5+s^3/X_i=c,\qquad
                  r(p_i)=X_i^3.
 \tag{15}
\]
Thus they lie on the same localized \(H\)-orbit. Since \(Hr=-fg\), its
connecting time is
\[
                 \tau(s)=
                 -\frac{X_2(s)^3-X_1(s)^3}{sc}.
 \tag{16}
\]
It has exact order \(-1\): its leading coefficient is
\[
                         -\frac{a^3(\omega^3-1)}{c}\ne0.
 \tag{17}
\]

This time connects all three base coordinates, not merely \(r\).
Indeed, over \(\mathbb C((s))\), the values \(f=s\) and \(g=c\) are
nonzero. Formula (4) reconstructs each of \(x,y,z\) uniquely from
these invariant values and \(r\). The finite \(H\)-flow sends
\(r=X_1^3\) to \(r=X_2^3\) at (16), so it sends the full first base
point to the second. Equation (5) adds no \(t\)-displacement because
\(1+\lambda c=0\). Hence
\[
                     \Phi^{E_\lambda}_{\tau(s)}(p_1(s))=p_2(s)
 \tag{18}
\]
is an exact whole four-coordinate identity over \(\mathbb C((s))\).
The finite polynomial flow can be evaluated at a Laurent-series time.

If \(u\in R[t]\) were a polynomial slice, its finite flow identity would
imply
\[
                            u(p_2(s))-u(p_1(s))=\tau(s).
 \tag{19}
\]
The left side is in \(\mathbb C[[s]]\); the right side has the nonzero
pole (17). This contradiction proves that \(E_\lambda\) is unsliced for
every \(\lambda\ne0\).

The obstruction concerns whole polynomial slices. Neither the existence
of a local trivialization nor the vanishing of the \(t\)-velocity on
the fiber would alone suffice; the exact return and its time pole do.

## 4. Independent algebraic fiber proof

The same conclusion can be obtained without formal endpoints. Retain
\(c=-1/\lambda\ne0\), and let
\[
                              S=R/(g-c).
 \tag{20}
\]
The derivation \(H\) descends to \(S\), since it kills \(g\).

First, \(f\) is regular on \(S\). The polynomial \(f=xz-y^2\) is
irreducible: regard it as a primitive linear polynomial in \(z\) over
\(\mathbb C[x,y]\), and use its degree one over \(\mathbb C(x,y)\).
Also \(g\) reduces to \(x^5\) modulo \(f\), and \(x^5-c\) is nonzero
in \(R/(f)\). For instance, evaluation at \(y=z=0\) leaves the
nonzero polynomial \(x^5-c\).
Thus \(\gcd(f,g-c)=1\) in the UFD \(R\).
If \(fP\in(g-c)\), unique factorization then gives \(P\in(g-c)\),
proving the asserted regularity.

After inverting \(f\), the value \(g=c\) is already a unit, so (4) gives
\[
                 S_f=\mathbb C[f,f^{-1},r],
                 \qquad H|_{S_f}=-cf\,\partial_r.
 \tag{21}
\]
Regularity embeds \(S\) in this domain, so \(S\) itself is a domain.
The localized invariant ring is \(\mathbb C[f,f^{-1}]\).
In fact its contraction to \(S\) is exactly
\[
                              \ker(H|_S)=\mathbb C[f].
 \tag{22}
\]

Here is the contraction argument, including its nonunit boundary.
The special fiber is
\[
 \begin{split}
 S/fS
 &\simeq
 \mathbb C[x,y,z]/(xz-y^2,x^5-c)\\
 &\simeq
 \prod_{\alpha^5=c}\mathbb C[y].
 \end{split}
 \tag{23}
\]
There are five distinct nonzero roots \(\alpha\). The Chinese remainder
theorem separates them, and in each factor \(x=\alpha\) and
\(z=y^2/\alpha\). Thus \(S/fS\ne0\), and it is not a domain.

If a Laurent invariant belonging to \(S\) had a pole at \(f=0\), write
it as \(f^{-k}A(f)\), with \(k\ge1\), \(A\in\mathbb C[f]\), and
\(A(0)\ne0\). The equality \(f^k v=A(f)\) in \(S\), reduced modulo
\(fS\), would say that the nonzero complex number \(A(0)\) is zero in
the nonzero \(\mathbb C\)-algebra (23). This is impossible.
It proves (22); no rationality assumption on a kernel is inserted.

Suppose \(H|_S\) had a slice \(v\). The elementary slice identity gives
\[
                            S=(\ker H|_S)[v]=\mathbb C[f][v].
 \tag{24}
\]
For completeness, if a locally nilpotent derivation \(\delta\) has
\(\delta v=1\), the finite operator
\(\pi(a)=\sum_i(-v)^i\delta^i(a)/i!\) takes values in \(\ker\delta\),
and
\(a=\sum_i v^i\pi(\delta^i a)/i!\).
These identities follow by finite binomial expansion. Differentiating
a putative polynomial relation in \(v\) shows that \(v\) is
algebraically independent over the kernel in a characteristic-zero
domain. This proves (24).

But (24) would make \(S/fS\simeq\mathbb C[v]\) a domain, contradicting
(23). Thus \(H|_S\) has no slice.

Finally a polynomial \(E_\lambda\)-slice would reduce modulo \(g-c\)
to a polynomial in \(S[t]\) with derivative one under the derivation
that is \(H|_S\) on \(S\) and kills \(t\).
Taking its constant coefficient in \(t\) would give a slice of
\(H|_S\), just excluded. This is an independent algebraic proof of
the nonzero-parameter conclusion.

## 5. Exact verification and limits

Fresh unsaved algebra checked the entire localized finite flow, not a
selected leading term. It verified that the time (16) sends all three
coordinate expressions (4) to their endpoint values modulo
\(X_2^6-cX_2+s^3\), and that the full \(t\)-displacement is zero for
\(\lambda=-1/c\).
The two formal-root derivatives and their first coefficients were
checked exactly modulo
\(\omega^4+\omega^3+\omega^2+\omega+1\), as was the nonzero pole
coefficient. The original Jacobian and identities (3) were also
reconstructed independently from (2).

The proof does not infer slicing from absence of zeros, local
trivializations, plinth data, or a quotient-field presentation. For the
zero parameter, actual polynomial automorphisms give the rectification.
For the nonzero parameter, either Section 3 or Section 4 rules out a
whole slice.

The result remains only the residual family (1). Any broader
degree-five classification must independently justify the claimed
reduction to this family and its whole-coordinate shear. No such
reduction is used here. No general cancellation or novelty claim
follows.

No saved checker was executed, imported, or compiled. No prior source
or canonical record was edited. This note requires its own independent
saved-source review after full author review and a final HELD hash.
