# Homogeneous DG top-degree removal and the selected-coordinate minimum

Date: 2026-09-17

Status: bounded working proof, held only after complete author reread.
Independent saved-source review is required before canonical acceptance.

## 1. Result and scope

For the specific homogeneous Daigle–Freudenburg family below, the top
locally nilpotent degree in the proposed first-shift profile is always
removable by a homogeneous polynomial in the original three-ring.
The correcting polynomial is a complex multiple of a power of the
original coordinate \(z\).

Write \(R_j\) for the ordinary homogeneous degree-\(j\) part of

\[
R=\mathbb C[x,y,z],\qquad
\mathcal F_j=\ker H^{j+1}\quad(j\geq0).
\tag{1}
\]

For every \(n\geq1\), put \(d=4n\) and \(N=8n+2\), with \(H\) defined
in Section 2. For every integer \(q\geq1\), set

\[
\ell=q+d,\qquad k=qN-1.
\tag{2}
\]

The exact vector-space statement is

\[
R_\ell\cap\mathcal F_k
=\mathbb C\,H(z^q)\ \oplus
  \bigl(R_\ell\cap\mathcal F_{k-1}\bigr).
\tag{3}
\]

In particular, if a homogeneous \(\psi\in R_\ell\) has
\(\deg_H\psi=k\), there is a nonzero \(P\in\mathbb C z^q\subset R_q\)
such that \(\deg_H(\psi-HP)<k\). The proof gives the coefficient of
\(P\) explicitly. If \(\psi\) already has smaller \(H\)-degree, one
may take \(P=0\).

This is weaker than demanding
\(\psi\in H(R)+\ker H\), which fails for the sliced examples in
[pass 598](homogeneous-sliced-first-shift-image-kernel-counterexample-pass598-working.md).
It makes no assertion for arbitrary homogeneous LNDs. The degree
reduction in Section 6 applies to specified actual polynomial frames;
it does not supply arbitrary coordinate entry, general cancellation,
or a novelty claim. No image theorem from the literature is needed
for the proof.

## 2. The whole polynomial derivation and its exact degree

Set

\[
\begin{gathered}
a=2n+1,\qquad M=4n+1=2a-1,\qquad N=2M,\\
f=xz-y^2,\qquad r=x^a+yf^n,\\
g=\frac{f^a+r^2}{x}
 =zf^{2n}+2x^{a-1}yf^n+x^{2a-1},\\
H(P)=\det J(f,g,P).
\end{gathered}
\tag{4}
\]

The quotient defining \(g\) is the displayed whole polynomial. The
Jacobian convention is the ordered row convention \(f,g,P\). Direct
differentiation gives the complete coordinate identities

\[
\begin{aligned}
Hx&=-2f^nr,\\
Hy&=2a x^{a-1}r-g,\\
Hz&=2x^{a-2}\bigl(f^{n+1}+Myr\bigr),\\
Hf&=Hg=0,\qquad Hr=-f^ng.
\end{aligned}
\tag{5}
\]

In particular \(H\) is ordinary homogeneous of derivation degree

\[
d=4n,\qquad \deg f=2,\quad\deg r=a,\quad\deg g=M.
\tag{6}
\]

The same base family is used in
[pass 597](homogeneous-first-shift-degree-condition-unsliced-boundary-pass597-working.md).
The following explicit localization proves every degree assertion
needed here, without requiring a classification of its kernel:

\[
\begin{gathered}
R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r],\\
x=\frac{f^a+r^2}{g},\qquad
y=\frac{r-x^a}{f^n},\qquad
z=\frac{g-2x^{a-1}r+x^M}{f^{2n}}.
\end{gathered}
\tag{7}
\]

Both inclusions in the ring equality follow from the displayed
formulas. Transcendence degree then proves that \(f,g,r\) are
algebraically independent. In this actual Laurent polynomial ring,

\[
H=-f^ng\,\partial_r.
\tag{8}
\]

This derivation is locally nilpotent there and preserves \(R\) by
(5), so it is an LND of the original polynomial ring. For every
nonzero element of \(R\), its \(H\)-degree equals its polynomial
degree in \(r\) over \(\mathbb C(f,g)\). Formula (7) therefore gives

\[
\deg_H(x,y,z,r)=(2,\,2a,\,2M,\,1)
                 =(2,\,4n+2,\,N,\,1).
\tag{9}
\]

For example, the highest \(r\)-terms in \(y\) and \(z\) come uniquely
from \(-x^a/f^n\) and \(x^M/f^{2n}\), respectively. This includes
\(n=1\), when \(a=3\) and \(M=5\). We use
\(\deg_H0=-\infty\).

## 3. A valuation in the projective two-ring

On \(\mathbb C(f,g)(r)=\operatorname{Frac}R\), let
\(\nu=-\deg_r\), with \(\nu(0)=+\infty\). This is the valuation
at infinity of the rational variable \(r\). It satisfies
\(\nu(AB)=\nu(A)+\nu(B)\) and
\(\nu(A+B)\geq\min(\nu(A),\nu(B))\), with equality when the two
values differ. On nonzero polynomials of \(R\), it is
\(-\deg_H\).

Introduce rational functions only for this calculation:

\[
\alpha=\frac{x}{z},\quad
\beta=\frac{y}{z},\quad
\phi=\frac{f}{z^2}=\alpha-\beta^2,\quad
\rho=\frac{r}{z^a},\quad
\sigma=\phi^n+\beta^M.
\tag{10}
\]

They are not promoted to ambient polynomial coordinates. From (9),

\[
\begin{aligned}
\nu(\beta)&=M-1=4n, & \nu(\phi)&=4M,\\
\nu(\alpha)&=2M-2, &
\nu(\rho)&=aN-1=M^2+M-1.
\end{aligned}
\tag{11}
\]

The key cancellation is computed without discarding any terms:

\[
\rho=\alpha^a+\beta\phi^n
 =\beta\sigma+
  \sum_{i=1}^{a}\binom ai\beta^{2a-2i}\phi^i.
\tag{12}
\]

The \(i\)-th summand in the tail has valuation

\[
(2a-2i)(M-1)+4Mi.
\tag{13}
\]

At \(i=1\), this is \((M+1)^2=M^2+2M+1\), strictly larger
than \(\nu(\rho)\). Each succeeding value increases by
\(2M+2>0\). Thus the entire tail has greater valuation than
\(\rho\). It follows from (12), including possible tail
cancellation, that

\[
\nu(\sigma)=M^2,\qquad
\operatorname{in}_\nu(\rho)
 =\operatorname{in}_\nu(\beta\sigma).
\tag{14}
\]

Here \(\operatorname{in}_\nu\) denotes the first nonzero term at the
specified valuation. Equality of these initials means that their
difference has strictly greater valuation.

## 4. The complete polynomial normal form and its low values

The rational functions \(\alpha,\beta\) are algebraically independent,
and

\[
\mathbb C[\alpha,\beta]=\mathbb C[\phi,\beta]
 =\bigoplus_{j=0}^{n-1}\phi^j\mathbb C[\beta,\sigma].
\tag{15}
\]

The last equality is a free-module decomposition, not merely a
generating list. Existence follows by repeatedly replacing
\(\phi^n\) with \(\sigma-\beta^M\). For uniqueness, expand any
putative relation in powers of \(\phi\). The largest exponent
arising from a nonzero term \(\phi^j A_j(\beta,\sigma)\) is
\(j+n\deg_\sigma A_j\); these exponents are distinct modulo \(n\)
for distinct \(j\). Its coefficient cannot cancel. This also proves
the algebraic independence of \(\beta,\sigma\).

Consequently every polynomial in this two-ring has a unique finite
expansion with complex coefficients in the monomials

\[
\beta^i\phi^j\sigma^e,
\qquad i,e\geq0,\quad0\leq j<n.
\tag{16}
\]

Their exact valuations, by multiplicativity and (11), (14), are

\[
4ni+4Mj+M^2e.
\tag{17}
\]

Put

\[
L=dN+1=2M^2-2M+1<2M^2.
\tag{18}
\]

There is no cancellation between distinct monomials in (16) whose
valuations are at most \(L\). Indeed such monomials have \(e=0\) or
\(e=1\). Those two cases have values congruent to \(0\) and \(1\)
modulo \(4\), respectively, since \(M\) is odd. For fixed \(e\),
equality of two values implies
\(n(i-i')+M(j-j')=0\). Since \(\gcd(n,M)=1\) and
\(|j-j'|<n\), it forces \(j=j'\) and \(i=i'\).
Terms with \(e\geq2\) have valuation strictly greater than \(L\)
and cannot affect this assertion.

There is exactly one monomial in (16) of value \(L\). Its exponent
must satisfy \(e=1\), followed by

\[
ni+Mj=4n^2.
\tag{19}
\]

Reducing modulo \(n\) forces \(j=0\), and then \(i=4n\). Thus it is
\(\beta^{4n}\sigma\). In particular, if a polynomial in this
two-ring has valuation at least \(L\), all normal-form coefficients
of smaller value vanish, and its valuation-\(L\) initial is a
complex multiple of that one monomial's initial. If its coefficient
is zero, the polynomial has valuation strictly greater than \(L\),
or is zero. This conclusion uses the entire normal form, including
arbitrarily high terms, not a finite list of test polynomials.

## 5. The coefficient of the correcting polynomial

For \(\psi\in R_\ell\), ordinary homogeneity gives
\(\psi/z^\ell\in\mathbb C[\alpha,\beta]\). If
\(\deg_H\psi\leq k\), then

\[
\nu(\psi/z^\ell)\geq\ell N-k=dN+1=L.
\tag{20}
\]

Let \(c\in\mathbb C\) be the coefficient of
\(\beta^{4n}\sigma\) in its unique normal form (16). Section 4
identifies the complete initial of (20), not merely a selected
term of its original expression.

To match the coefficient, use the entire \(Hz\) formula in (5):

\[
\frac{Hz}{z^{d+1}}
 =2\alpha^{a-2}\bigl(\phi^{n+1}+M\beta\rho\bigr).
\tag{21}
\]

Since \(\alpha=\beta^2+\phi\) and
\(\nu(\phi)>\nu(\beta^2)\), its initial is that of
\(\beta^2\). Moreover,
\(\nu(\phi^{n+1})-\nu(\beta\rho)=M+2>0\).
Using (14) in (21) therefore gives

\[
\operatorname{in}_\nu\left(\frac{Hz}{z^{d+1}}\right)
 =N\operatorname{in}_\nu(\beta^{4n}\sigma).
\tag{22}
\]

The exact rational identity
\(H(z^q)/z^{q+d}=qHz/z^{d+1}\) now proves that the choice

\[
P=\frac{c}{qN}\,z^q
\tag{23}
\]

has \(\nu((\psi-HP)/z^\ell)>L\). Equivalently,
\(\deg_H(\psi-HP)<k\). The denominator \(qN\) is a nonzero
complex number. If \(\psi\) has exact degree \(k\), then \(c\ne0\).
Otherwise \(c=0\) and (23) gives \(P=0\).

Also \(\deg_H H(z^q)=qN-1\), so its span intersects
\(\mathcal F_{k-1}\) trivially. This proves (3). Every
\(P_0\in R_q\) has \(\deg_H P_0\leq qN\), since all three
original coordinate degrees are at most \(N\). Hence the equivalent
image statement is exactly

\[
R_\ell\cap\mathcal F_k
=H(R_q)+\bigl(R_\ell\cap\mathcal F_{k-1}\bigr).
\tag{24}
\]

No case was divided away at \(q=1\) or \(n=1\). When \(n=1\), the
free-module basis in (15) consists only of \(1\); the value and
uniqueness arguments are unchanged. Zero polynomials and all lower
degree elements are covered by \(c=0\).

## 6. The actual selected-frame degree reduction

Let \(B=R[t]\), and suppose

\[
E=H+(1+\psi)\partial_t,\qquad
\psi\in R_{q+d},\quad\deg_H\psi=qN-1.
\tag{25}
\]

This triangular derivation is locally nilpotent: the derivative
sequence of \(t\) terminates, as do those of \(x,y,z\), and these
elements generate \(B\). Its exact coordinate degrees are

\[
\deg_E(x,y,z,t)=(2,4n+2,N,qN).
\tag{26}
\]

Take \(P\) from (23). The actual whole polynomial shear and inverse
are

\[
T=t-P(x,y,z),\qquad t=T+P(x,y,z),
\tag{27}
\]

with \(x,y,z\) fixed. It has determinant one and gives
\(ET=1+\psi-HP\). Since \(\psi-HP\) is homogeneous of the
positive degree \(q+d\), it cannot equal \(-1\). Consequently

\[
1\leq\deg_E T\leq qN-1<\deg_E t.
\tag{28}
\]

The other three actual coordinate degrees are unchanged. The same
shear lowers the last degree in the uniform actual frame
\((x+z,y+z,z,t)\), whose degree profile is
\((N,N,N,qN)\). Its inverse is explicit: recover \(z\), subtract
it from the first two coordinates, and then use (27).

Thus neither selected frame can minimize the sum of actual
\(E\)-degrees among all polynomial coordinate frames. More narrowly,
its chosen \(t\) cannot already be degree-minimal even among base
shears with \(P\in R_q\). A claim that such a globally minimizing
frame has entered (25) would contradict this explicit competing
frame.

This conclusion does not assert that arbitrary sliced derivations
can be placed in (25), or that the new frame retains a specified
Euler shift. Any Euler derivation assigned to the new frame must
use its new actual degree profile. The strict decrease of the sum
in (28) requires no claim about that new shift, a supplied slice,
or recognition of the invariant ring. It does not reverse the
image-plus-kernel counterexample in598.

## 7. Verification and remaining boundary

The proof is uniform in \(n,q\). Its decisive inputs are the whole
identities (5), (7), (12), and (21), the monic normal form (15), and
the exact valuation separation below (18).

Fresh unsaved algebra separately checked the full leading
multinomial calculation for \(\sigma\) at \(1\leq n\leq6\), the
all-parameter exponent identities, the entire coordinate Jacobian
and the short identities (12), (21) for \(1\leq n\leq3\), and exact
homogeneous vector spaces for \(n=1,1\leq q\leq8\) and
\(n=2,1\leq q\leq4\). These checks support the written identities;
they are not substitutes for the general proof. No saved checker
was executed, imported, or compiled, and no canonical file was
edited in preparing this note.

The result removes this one top-degree obstruction in the original
DG base. Further coordinate recognition, an arbitrary-entry
theorem, and general cancellation remain outside its scope.
