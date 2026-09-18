# Audit of the arbitrary polynomial-curve coordinate lift

Sections 4-6 of [the polynomial-curve note](polynomial-curve-lift-pass18.md)
survive this audit. The lower coefficients of the arbitrary monic
polynomial do not introduce an unhandled denominator: their terms
in the homogenization have a factor \(f^n\), and the requisite
scaling differences have a separate factor \(h\). Both forward
and inverse divisibility are polynomial statements before reduction
modulo \(f^n\).

The root specialization proving that the independently reconstructed
\(h\) is nonzero is valid, including when \(F(0)\ne0\).
The coordinate composition is global and does not rely on a
fiberwise-to-global inference or an assumed cancellation theorem.

This audit checks the coordinate construction under the base
identities and coefficient hypotheses of the note. Necessity of
those coefficient hypotheses for an arbitrary slice uses the
separate geometric affine-replacement theorem. No human peer
review, formal proof-assistant verification, or novelty is claimed.

## 1. Notation and the lower terms

Write

\[
F(Y)=\sum_{j=0}^d a_jY^j,\qquad a_d=1,
\qquad S=f^n,
\qquad G(R,S)=\sum_{j=0}^d a_jR^jS^{d-j}.
\tag{A1}
\]

Thus \(G(R,S)\equiv R^d\pmod S\), but the proof cannot
simply divide this congruence by \(h\). The source note correctly
uses the additional coefficient condition \(B\equiv1\pmod h\)
to obtain divisibility by both factors before performing that
division.

The assumed base identities are
\(xh=G(r,S)+fS^d\), \(r=xP(x,f)+yS\), and
\(\delta r=Sh\). Normalize the nonzero residue constant in
\(B\) to one by scaling the whole derivation, hence both its
coefficients. Choose

\[
AShU+BV=1,
\qquad\rho=Br-ASht,
\qquad s=Ur+Vt.
\tag{A2}
\]

The determinant is exactly one. Its inverse gives
\(r=V\rho+AShs\) and \(t=-U\rho+Bs\). In particular
\(E\rho=0\) and \(Es=1\). Reducing the Bézout identity
modulo \(h\) gives \(V\equiv1\pmod h\), since
\(B\equiv1\pmod h\).

## 2. Forward divisibility without canceling in a quotient

First, \(\rho-r\in hR[t]\), so

\[
X=\frac{G(\rho,S)+fS^d}{h}
\tag{A3}
\]

is polynomial, using \(xh=G(r,S)+fS^d\). To verify the
stronger congruence \(X\equiv B^dx\pmod S\), expand its
numerator difference as

\[
\begin{aligned}
&G(Br-ASht,S)-B^dG(r,S)+(1-B^d)fS^d\\
={}&G(Br-ASht,S)-G(Br,S)\\
&+\sum_{j=0}^{d-1}a_j(B^j-B^d)r^jS^{d-j}
 +(1-B^d)fS^d.
\end{aligned}
\tag{A4}
\]

The first difference is divisible by \(Sh\), because its two
first arguments differ by \(-ASht\). Every term in the sum
has a positive power of \(S\), and \(B^j-B^d\) is divisible
by \(h\). The final term is divisible by \(Sh\) as well.
Thus (A4) belongs to \(ShR[t]\). After dividing this genuine
polynomial multiple by \(h\), one obtains

\[
X\equiv B^dx\pmod S,
\qquad X\equiv x\pmod f.
\tag{A5}
\]

This checks explicitly the constant coefficient \(a_0\), all
intermediate coefficients, and terms involving \(t\). No monomial
assumption on \(F\) was inserted.

## 3. The same finite jet gives polynomial \(Y\)

The Taylor formula for \(h\) has only one term surviving modulo
\(S\), namely \(x^{d-1}P(x,f)^d\). Together with (A5),
the residue relations are

\[
r=xP,\quad h=x^{d-1}P^d,\quad
\rho=BxP,\quad X=B^dx
\quad\text{in }R[t]/(S).
\tag{A6}
\]

The update
\(H\mapsto b_H^{1-d}P(b_H^{-d}X,f)\), with
\(b_H=B(f,X^{d-1}H^d)\), improves congruence by one power
of \(f\). Indeed \(B(f,h)-1\) is divisible by \(f\),
and differences in its second argument consequently gain that
factor. Negative powers are finite powers of a unit in the
nilpotent quotient. This proves the stated finite convergence
and uniqueness after specialization.

In (A6), the element \(H_*=B^{1-d}P(B^{-d}X,f)\) satisfies
\(X^{d-1}H_*^d=h\), and so is a fixed point. It has the
required initial residue \(P(X,0)\). Therefore the specialized
finite jet equals \(H_*\) and \(\rho-XH\in SR[t]\).
Thus \(Y=(\rho-XH)/S\) is polynomial.

## 4. Taylor's identity checks every coefficient of \(Z\)

For arbitrary symbols, homogenized Taylor expansion gives

\[
G(XH+YS,S)
=\sum_{k=0}^d
\frac{F^{(k)}(Y)}{k!}X^kH^kS^{d-k}.
\tag{A7}
\]

Subtract the terms with \(k\ge1\) from
\(Xh=G(\rho,S)+fS^d\). With the note's \(S_F\), the
result is exactly

\[
X(h-S_F)=S^d(F(Y)+f).
\tag{A8}
\]

The constant term \(a_0\), for example, is included in
\(F(Y)\), not lost by the derivative sum. The polynomial
\(f=xz-F(y)\) is prime: it is primitive linear in \(z\)
and irreducible over \(\mathbb C(x,y)\). It does not divide
\(X\), by (A5), since it does not divide \(x\). Therefore
the UFD property gives \(f^{nd}\mid h-S_F\). This proves
polynomiality of \(Z\) and the relation \(f=XZ-F(Y)\).

## 5. The independent inverse ring

In \(T=\mathbb C[X,Y,Z,s]\), define \(f,\rho,h\) as
in the note. Taylor identity (A7) again gives
\(Xh=G(\rho,S)+fS^d\). Pick a complex root \(\alpha\)
of the nonconstant monic \(F\), and specialize
\(Y=\alpha,Z=0\). Then \(f=S=0\), and the only term
of \(S_F\) that survives is the monic top term:

\[
h\big|_{Y=\alpha,Z=0}
=X^{d-1}P(X,0)^d\ne0.
\tag{A9}
\]

This proves that \(h\) is nonzero in \(T\), without assuming
that zero is a root of \(F\). Repeated roots cause no change
because \(F^{(d)}(\alpha)/d!=1\) always.

The divided difference used for \(x\) is the polynomial

\[
\Delta_G(r,\rho,S)=
\sum_{j=1}^d a_jS^{d-j}
\sum_{i=0}^{j-1}r^{j-1-i}\rho^i.
\tag{A10}
\]

There is no division by a possibly zero \(r-\rho\). Since
\(r-\rho=hW\), the definition \(x=X+W\Delta_G\) gives
\(xh=G(r,S)+fS^d\) as a polynomial identity.

Modulo \(S\), the lower coefficients in (A10) disappear and
\(r\equiv V\rho\). Consequently

\[
x\equiv X+\frac{V^d-1}{h}\rho^d\pmod S.
\tag{A11}
\]

The coefficient \((V^d-1)/h\) is already a polynomial before
specializing. Also \(\rho^d-hX\) is divisible by \(S\),
by (A1) and the reconstructed identity. Multiplying this
divisibility by that polynomial coefficient proves
\(x\equiv V^dX\pmod S\). It is not an illicit cancellation
of \(h\) in \(T/(S)\).

Since \(BV\equiv1\pmod S\) and
\(h\equiv X^{d-1}H^d\pmod S\), the finite-jet identity gives
\(H\equiv V^{d-1}P(V^dX,f)\pmod S\). Hence
\(r\equiv xP(x,f)\pmod S\), proving polynomiality of the
reconstructed \(y\). Apply (A7) with \(x,P(x,f),y\) to
obtain

\[
x\bigl(h-S_F(x,P(x,f),y,f)\bigr)
=S^d(f+F(y)).
\tag{A12}
\]

Here \(f=XZ-F(Y)\) is prime in \(T\) and
\(x\equiv X\pmod f\), so \(f\nmid x\). Thus the
reconstructed numerator for \(z\) is divisible by \(f^{nd}\).
All four inverse expressions are polynomial in independent
\(X,Y,Z,s\).

## 6. Composition and scope

After substituting the forward coordinates, the reconstructed
\(f,\rho,h\) are their originals by their defining polynomial
identities. The inverse matrix recovers \(r,t\). The identity
\(xh=G(r,S)+fS^d\), with nonzero \(h\), then recovers
\(x\); the definitions recover \(y,z\). Thus the forward
four coordinates generate the original polynomial four-ring.
A surjective homomorphism between these two four-dimensional
polynomial domains has prime kernel of height zero, hence kernel
zero. This proves the coordinate conclusion.

No assumption on distinctness of roots, vanishing of the constant
term, or homogeneity of \(F\) entered the checked argument.
Monicity ensures the top term used in (A6), (A9), and (A10),
while \(n\ge1\) ensures every lower homogeneous term vanishes
modulo \(S\). The coefficient criterion in Section 4 remains
conditional on the separately documented affine-replacement input
when it is used as a necessary condition for arbitrary slices.

The audit establishes no extension from this two-chart family to
arbitrary primitive rank-three LNDs. It also makes no assertion
that the resulting isomorphism preserves the original presentation
of the full common invariant plane.
