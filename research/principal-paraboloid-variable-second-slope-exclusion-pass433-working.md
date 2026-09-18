# The remaining variable second-potential slope is impossible

Working necessary result: retain every actual hypothesis of264 and
the complete430 plane reduction. Assume
\[
k=s+f,\quad f_s=n_s=0,\quad f'''\ne0,\quad
e=\ell_s\ne0,\quad \ell_{ss}=0.
\]
Then \(\ell_{ts}=0\). Together with431 this says that, in this
specified nonlinear-time subcase, the second-potential slope
\(\ell_s\) must be a nonzero complex constant.

This is not recognition of the remaining constant-slope family.
It neither constructs an original coordinate nor supplies entry
from an arbitrary sliced polynomial four-ring.

## 1. Exact inputs and the whole-ring specialization

Retain the full actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
not merely formal solutions of its potential identities:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\qquad Nv=1,\qquad
O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
J_{t,s,v}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
Here the bracket \(L[A]\) means the specified actual localization.
The coefficient partials commute, fix \(v\), and have joint
constant field \(\mathbb C\). Put
\(\mathbb F=\ker_L\partial_s\), which is finite over \(\mathbb C(t)\).
We do not identify it with the rational field. Primes on \(f,n\)
are exact \(t\)-derivatives in this field.

The specialized assumptions are
\[
k=s+f,\quad f,n\in\mathbb F,\quad
f'''\ne0,\quad e=\ell_s\ne0,\quad e_s=\ell_{ss}=0 .
\tag{2}
\]
In particular \(e\in\mathbb F^*\). Write
\(e'=\partial_t e=\ell_{ts}\); we shall exclude \(e'\ne0\).

The literal rows and the first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n'\sigma .
\end{aligned}
\tag{3}
\]
Every coefficient and level is retained as an element of \(L\);
no level is silently declared constant in \(s\) or \(t\).

The original slice licenses a stronger return than fraction-field
generation. Since \(X=a_0u+x_0\), with \(x_0\in A\) and
\(a_0\in L^*\), localization of the actual ring gives
\[
L[\mathcal B]=L[A][u]=L[v,u]=L[v,X]
             =L[X,Y,Z,W].
\]
Consequently, for every \(\lambda\in L\), evaluation at \(X=\lambda\)
gives
\[
\boxed{L[Y(\lambda),Z(\lambda),W(\lambda)]=L[v].}
\tag{4}
\]
This is evaluation of a polynomial-ring identity over \(L\).
It does not assert that \(X-\lambda\) is an original complex
coordinate, or that denominators in \(L\) belong to \(A\).

## 2. The complete plane primitive

Use formal independent variables \(U,P\). The fully retained
[430 reduction](principal-paraboloid-arbitrary-longitudinal-plane-reduction-pass430-working.md)
gives
\[
\begin{aligned}
S(U,P)&=U^2+(f''P+n')U+\frac{f'''}6P^3
                 +\frac{n''}2P^2-\ell_tP-h,\\
Q_0(U,P)&=\frac{f''}2U^2+
 \left\{\frac{f'''}2P^2+(n''+2e)P+f'e-\ell_t\right\}U\\
&\quad+\frac{f''''}{24}P^4+\frac{n'''}6P^3
       +\frac{f''e-\ell_{tt}}2P^2+(n'e-h_t)P,\\
\Phi(U,P)&=Q_0(U,P)-\frac{e'P+h_s}{e}S(U,P).
\end{aligned}
\tag{5}
\]
Here \(h\) is the genuine third level. The absence of a term
\(-\ell_{ss}S^2/(2e^2)\) uses the explicit hypothesis in(2),
not a discarded coefficient. The genuine fourth level is \(q\in L\).
The necessary consequences from430 are
\[
\theta=S(y,\sigma)/e,\qquad
L[y,\sigma]=L[v],\qquad
\Phi(y,\sigma)=q,\qquad
(\Phi_U(y,\sigma),\Phi_P(y,\sigma))L[v]=L[v].
\tag{6}
\]
The last equality uses the complete two-gradient minor identity
from296 and the actual calibrated scalar. It is not inferred just
from the nonvanishing of \(H_V=-e\).

Assume henceforth, for contradiction, that \(e'\ne0\).
Collecting the \(U\)-powers in(5) gives
\[
\Phi(U,P)=A(P)U^2+B(P)U+C(P),
\tag{7}
\]
where
\[
\begin{aligned}
A(P)&=\frac{f''}{2}-\frac{e'P+h_s}{e},\\
B(P)&=\frac{f'''}2P^2+(n''+2e)P+f'e-\ell_t
       -\frac{e'P+h_s}{e}(f''P+n').
\end{aligned}
\tag{8}
\]
Thus \(\deg A=1\), its leading coefficient is \(-e'/e\),
\(\deg B\le2\), and \(\deg C\le4\).
The lower polynomial \(C\) is exactly the constant-in-\(U\) part
of(5); it is not set to zero.

## 3. A constant sigma contradicts the gradient unit

Suppose \(\sigma=p_0\in L\). By(6), \(L[y]=L[v]\), so \(y\)
has degree one in \(v\). Since it is transcendental over \(L\),
\(\Phi(y,p_0)=q\) implies the formal identity
\(\Phi(U,p_0)=q\). In particular \(A(p_0)=B(p_0)=0\) and
\(\Phi_U(y,p_0)=0\).

On the other hand, \(\Phi_P(U,p_0)\) has exact \(U\)-degree two:
its leading coefficient is \(A'(p_0)=-e'/e\ne0\).
After substituting the affine parameter \(y\), it is a nonconstant
polynomial of degree two in \(v\). It is not a unit of \(L[v]\).
This contradicts the last identity of(6).

## 4. Monicity leaves only an affine sigma parameter

Suppose now that \(\sigma\) is nonconstant, of degree \(r\) in \(v\).
The equation for \(\sigma(v)\), divided by its nonzero leading
coefficient, makes \(v\) integral over \(L[\sigma]\).
Hence \(y\in L[v]\) is integral over the same ring.

As \(L[P]\) is integrally closed, the monic minimal polynomial
of \(y\) over \(L(\sigma)\), identifying \(P\) with \(\sigma\),
is a polynomial \(G(U,P)\in L[P][U]\), monic in \(U\).
It generates the complete plane kernel: division by this monic
polynomial leaves a lower-\(U\)-degree relation, which must vanish
by minimality.

The whole return in(6) implies \(L(y,\sigma)=L(v)\), and therefore
\[
\deg_U G=[L(v):L(\sigma)]=r .
\tag{9}
\]
For completeness, the last degree formula follows directly from
the polynomial equation for \(v\): it gives degree at most \(r\).
The elements \(1,v,\ldots,v^{r-1}\) are independent over
\(L(\sigma)\), because after clearing denominators any relation
would have summands with distinct degrees modulo \(r\).
This proves equality.

Since \(G\) divides the nonzero relation \(\Phi-q\), and(7) has
exact \(U\)-degree two, \(r\) is one or two.
If \(r=2\), monicity gives
\[
\Phi-q=A(P)G.
\]
On the actual line, both components of the evaluated gradient
of \(\Phi\) are multiples of \(A(\sigma)\).
But \(A(\sigma)\) has degree two in \(v\), so is not a unit.
This again contradicts(6). Thus \(r=1\).

It follows that \(L[\sigma]=L[v]\) and \(y=g(\sigma)\) for
some \(g\in L[P]\). The identity
\(\Phi(g(P),P)=q\) gives
\(\Phi_P(g(P),P)=-g'(P)\Phi_U(g(P),P)\).
The gradient ideal in(6) is consequently generated by
\(\Phi_U(g(P),P)\) alone. Units in \(L[P]\) are precisely \(L^*\),
so
\[
2A(P)g(P)+B(P)=\eta,\qquad \eta\in L^* .
\tag{10}
\]
If \(g\) had degree at least two, \(2Ag\) would have strictly
larger degree than \(B\), contradicting(10). Thus
\(g(P)=\alpha P+\beta\), allowing \(\alpha=0\), with
\(\alpha,\beta\in L\). The \(P^2\) coefficient of(10) is
\[
-\frac{2\alpha e'}{e}+\frac{f'''}2-\frac{e'f''}{e}=0,
\qquad
\boxed{\alpha=\frac{ef'''}{4e'}-\frac{f''}{2}.}
\tag{11}
\]
No division by \(\alpha\), \(y\), or a possibly zero level occurs.

## 5. An actual specialization forces an impossible degree pair

Apply(4) at \(\lambda=-\alpha\). The first row in(3) becomes
\[
Y(-\alpha)=\beta+t\alpha^2\in L .
\tag{12}
\]
By(5),(6),(11), \(\theta=S(\alpha\sigma+\beta,\sigma)/e\)
has exact degree three in \(\sigma\), with leading coefficient
\(f'''/(6e)\). In \(Z(-\alpha)\) every term other than
\(\theta\) has degree at most two. Thus
\[
\deg_\sigma Z(-\alpha)=3,\qquad
[\sigma^3]Z(-\alpha)=\frac{f'''}{6e}\ne0 .
\tag{13}
\]
In \(W(-\alpha)+\alpha Z(-\alpha)\), the cubic \(\theta\)
terms cancel exactly. Using all rows of(3), its quadratic
coefficient is
\[
[\sigma^2]\{W(-\alpha)+\alpha Z(-\alpha)\}
       =-\alpha-\frac{f''}{2}
       =-\frac{ef'''}{4e'}\ne0 .
\tag{14}
\]
All its other terms have degree at most one. Therefore(4) would
express the whole \(L[\sigma]\) as the algebra generated by a
polynomial of exact degree two and one of exact degree three.

Here is an elementary proof that this cannot happen over a
characteristic-zero field. Extend scalars to an algebraic closure;
an asserted generating identity would remain valid there.
An affine change of parameter, followed by scaling and subtracting
a constant from the quadratic, puts it in the form \(z^2\).
Subtracting a multiple of this quadratic and a constant from the
cubic, then scaling, puts the cubic in the form \(z^3+c z\).
These operations preserve the generated algebra.

If \(c\ne0\), choose \(z_0\ne0\) with \(z_0^2=-c\).
The distinct points \(z_0,-z_0\) have equal values of both
generators. No polynomial in those generators can be \(z\).
If \(c=0\), both generators have derivative zero at the origin.
Every polynomial in them has derivative zero there, whereas
the derivative of \(z\) is one. This also precludes generation.
Thus both possible cases give a contradiction.

## 6. Conclusion and precise remaining boundary

All possibilities for constant or nonconstant \(\sigma\) have
been exhausted under the supposition \(e'\ne0\). Hence
\[
\boxed{\text{Under(1),(2), }\quad \ell_{ts}=0.}
\tag{15}
\]
The separately reviewed
[431 exclusion](principal-paraboloid-nonlinear-time-weighted-plane-exclusion-pass431-working.md)
forces \(\ell_{ss}=0\) before this proof when \(f'''\ell_s\ne0\).
Together they give
\[
\boxed{
k=s+f,\ f_s=n_s=0,\ f'''\ell_s\ne0
\quad\Longrightarrow\quad \ell_s\in\mathbb C^*,
}
\tag{16}
\]
always under the full actual264 hypotheses.
Indeed both coefficient derivatives of \(e=\ell_s\) vanish,
and their joint constant field is \(\mathbb C\).
Equivalently, \(\ell=e s+\ell_0\) with
\(e\in\mathbb C^*\) and \(\ell_0\in\mathbb F\).

The surviving nonzero constant-slope family is not recognized
here. The \(\ell_s=0\) family is separate from this proof and
is handled by427 under its stated hypotheses. This note neither
forces \(n_s=0\) for a general candidate nor makes \(k_s\)
constant. The field, full initial kernel, exact profile, actual
localization and arbitrary-entry gaps remain as stated.
No existence of actual examples in the new sector is asserted.

## 7. Verification record

Root completely read430 in fcbab8 and freshly read430/431 through
EOF in d3c338. Root had completely read296 in ba693e and264 in
fe70a9 for this continuation. The fresh unsaved calculations
92a19a and f6c185 independently checked the complete coefficients
in(8), the forced slope(11), the constant-sigma derivative,
and every specialization and leading coefficient in(12)--(14).
All reported residuals were zero.

Before this saved draft, General independently checked the
monicity and whole-ring argument, with fresh identities73db6f.
Jet independently checked the complete coefficient gates92bd5c.
Geometry separately checked every branch of the conceptual
argument. These outline checks are not a substitute for a
complete saved-source review, which is recorded separately
in the research ledger when completed.

The elementary final degree-pair obstruction is proved above;
this note does not need an additional plane-embedding theorem.
431's separate use of the primary Abhyankar--Moh--Suzuki theorem
is retained as its own dependency.

No saved checker was executed, imported, compiled or rerun.
The exact identity computations do not verify all mathematical
arguments by themselves. No human-expert certification, Lean
proof, historical novelty clearance, unrestricted cancellation
solution, publication or external contact is claimed.
