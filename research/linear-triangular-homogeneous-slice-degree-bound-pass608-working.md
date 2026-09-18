# A slice-degree bound for linear-triangular homogeneous bases

## Status and exact scope

This is a bounded working proof about extensions of a three-variable
locally nilpotent derivation. It does not prove an entry theorem for arbitrary
sliced derivations on four variables, a coordinate-descent theorem, or
threefold cancellation. No novelty claim is made.

Let \(R=\mathbb C[x,y,z]\). For a nonzero locally nilpotent derivation \(H\),
write \(\deg_H F=\max\{i:H^iF\ne0\}\) for \(F\ne0\).
Ordinary homogeneity always means the standard grading with all three
variable weights equal to one. A derivation has ordinary degree \(d\) when
it sends the ordinary degree-\(e\) piece into degree \(e+d\).
Irreducibility means that its three coefficient polynomials have no
nonconstant common factor.

**Theorem.** Suppose \(H\) is an irreducible ordinary-homogeneous locally
nilpotent derivation of degree \(d>0\), triangular in a linear coordinate
system of \(R\). Let \(\psi\ne0\) be ordinary homogeneous of degree
\(\ell>d\). Put
\[
 E=H+(1+\psi)\partial_t,\qquad q=\ell-d,\qquad
 N=\max\{\deg_H L:L\in R\text{ is linear and nonconstant}\}.
 \tag{1}
\]
If \(E\) has a polynomial slice in the whole ring \(R[t]\), then
\[
                     \deg_H\psi+1\le qN.
 \tag{2}
\]

The same conclusion holds if \(H\) is polynomially triangularizable,
under the other hypotheses just stated, by Ghosh's linear-triangularization
lemma cited and explained in Section 7. This is not a claim that every
homogeneous rank-two derivation is triangularizable.

The proof is direct. It constructs two formal integral endpoints on the
same \(E\)-orbit whose connecting time has a pole whenever (2) fails.
It retains all lower coefficients of both \(H\) and \(\psi\).

## 1. Linear normalization and the maximum linear degree

In a linear triangular frame, ordinary homogeneity gives
\[
 Hx=0,\qquad Hy=\alpha x^j,\qquad Hz=B_j(x,y),
 \qquad j=d+1\ge2,
 \tag{3}
\]
where \(B_j\) is homogeneous of degree \(j\).
The constant \(\alpha\) is nonzero. Indeed, if \(Hy=0\), irreducibility of
\(B_j\partial_z\) would force \(B_j\) to be a nonzero constant, contrary
to \(d>0\). Irreducibility also gives
\(\gcd(x^j,B_j)=1\), so \(B_j(0,y)=\beta y^j\) for a nonzero complex
constant \(\beta\).

Replace \(y\) by \(y/\alpha\) and \(z\) by \(z/(\beta\alpha^j)\).
After renaming these linear coordinates,
\[
 H=x^j\partial_y+P_j(x,y)\partial_z,\qquad
 P_j(0,y)=y^j.
 \tag{4}
\]
This uses only a linear base-coordinate change. It preserves ordinary
homogeneity, the existence of a whole polynomial slice for the transported
extension, and the maximum \(H\)-degree of a linear polynomial.

The exact degrees in this frame are
\[
 \deg_H x=0,\qquad \deg_H y=1,\qquad
 \deg_H z=j+1=:N.
 \tag{5}
\]
For the last equality, \(Hz=P_j\), and on \(\mathbb C[x,y]\) the
derivation is \(x^j\partial_y\). The \(y^j\) coefficient of \(P_j\) is one.
Every linear polynomial has degree at most \(N\), and \(z\) attains it.
Thus this \(N\) is exactly the quantity in (1). Also
\[
              \ell\ge j,\qquad q=\ell-j+1\ge1.
 \tag{6}
\]

## 2. Why the high raw weight has a unique monomial

Write the complete homogeneous polynomial as
\[
 \psi=\sum_{a+b+c=\ell}\gamma_{abc}x^a y^b z^c.
 \tag{7}
\]
Only nonzero coefficients need be included. In a domain of characteristic
zero, locally nilpotent degree is additive under products, by the Leibniz
formula for the highest nonzero derivative. Consequently the monomial
in (7) has exact \(H\)-degree
\[
                              r=b+Nc.
 \tag{8}
\]

For a monomial satisfying \(r\ge qN\), substituting
\(\ell=a+b+c\), \(q=\ell-j+1\), and \(N=j+1\) gives
\[
                          Na+jb\le j^2-1.
 \tag{9}
\]
In particular \(0\le b\le j-1=N-2\). Such a monomial also has \(c\ge1\):
if \(c=0\), then \(a+b=\ell\ge j\), and
\(Na+jb=j\ell+a\ge j^2\), a contradiction.
Moreover,
\[
 jc-a\ge j^2-Na-jb\ge1.
 \tag{10}
\]

For fixed \(\ell\) and \(r\ge qN\), there is at most one monomial.
Indeed, \(b\) is the residue of \(r\) modulo \(N\) in the interval
\([0,N-2]\); then \(c=(r-b)/N\) and \(a=\ell-b-c\).

Suppose (2) fails, and put \(k=\deg_H\psi\), so \(k\ge qN\).
The largest raw weight in (7) is at least \(k\). At that largest weight
there is exactly one monomial by the preceding argument, so its highest
nonzero derivative cannot cancel. Therefore the largest raw weight is
exactly \(k\), and its monomial, denoted \((a_0,b_0,c_0)\), is unique.
All other raw weights are strictly smaller than \(k\). Finally,
\[
               k\ge qN>\ell,\qquad
               qN-\ell=j(\ell-j)+1>0.
 \tag{11}
\]
These statements concern the entire \(\psi\), not a monomial approximation.

## 3. The base return and the first formal implicit solve

Choose the polynomial primitive
\[
 Q(x,y)=\int_0^y P_j(x,v)\,dv,\qquad
 Q_y=P_j,\qquad Q(0,y)=\frac{y^N}{N}.
 \tag{12}
\]
It is homogeneous of degree \(N\), and \(x^jz-Q(x,y)\) is \(H\)-invariant.
On the open set \(x\ne0\), the base orbit starting at \((x,v,0)\) has
\[
 y=v+x^j\tau,\qquad
 z=\frac{Q(x,y)-Q(x,v)}{x^j}.
 \tag{13}
\]
The expression in (13) is a polynomial in the time \(\tau\), including
before localization: substitute \(y=v+x^j\tau\) and divide the polynomial
difference. Localization is used only to describe its endpoints.

Let \(\omega\) be a primitive \(N\)-th root of unity. In particular
\(\omega\ne1\). Define
\[
 A(\varepsilon,w)=Q(\varepsilon,w)-Q(\varepsilon,1).
 \tag{14}
\]
Then \(A(0,w)=(w^N-1)/N\), and
\(\partial_w A(0,\omega)=\omega^j\ne0\).
There is a unique formal power series
\[
 \Omega(\varepsilon)\in\mathbb C[[\varepsilon]],\qquad
 \Omega(0)=\omega,\qquad A(\varepsilon,\Omega(\varepsilon))=0.
 \tag{15}
\]
This is the elementary formal implicit construction: after the constant
term has been chosen, each next coefficient is determined by a linear
equation with coefficient \(\omega^j\). No convergence is needed.

With \(\varepsilon=x/v\) and \(w=y/v\), homogeneity gives
\[
 z=\frac{v^N}{x^j}A(\varepsilon,w).
 \tag{16}
\]
Thus \(y_{\rm end}=v\Omega(\varepsilon)\) returns exactly to \(z=0\).
When \(P_j\) has lower \(x\)-terms, the return multiplier is the full
series \(\Omega(\varepsilon)\), not the constant \(\omega\).

## 4. The entire \(t\)-displacement

For every pair of exponents \(b,c\) in (7), set
\[
 C_{bc}(\varepsilon)=
 \int_1^{\Omega(\varepsilon)}
             w^b A(\varepsilon,w)^c\,dw
 \in\mathbb C[[\varepsilon]].
 \tag{17}
\]
The integral means evaluation of a polynomial antiderivative in \(w\)
at the displayed formal upper endpoint. It is not an analytic path
integral.

The extension \(E\) is locally nilpotent: its restriction to \(R\) is
\(H\), and \(E^i t=H^{i-1}(1+\psi)\) for \(i\ge1\).
Along its orbit, \(dt/d\tau=1+\psi\) and \(d\tau=dy/x^j\).
Using (16), the exact \(t\)-displacement from \(t=0\), up to the base
return in (15), is
\[
 \Delta t=\frac{v}{x^j}\left[
  \Omega(\varepsilon)-1+
  x^\ell\sum_{a+b+c=\ell}
    \gamma_{abc}(v/x)^{b+Nc}C_{bc}(\varepsilon)
 \right].
 \tag{18}
\]
Indeed the monomial factor in the integral is
\(x^{a-jc}v^{b+Nc}=x^\ell(v/x)^{b+Nc}\).
Formula (18) includes all coefficients of \(\psi\) and all coefficients
of \(P_j\).

The constant coefficient of (17) is explicit:
\[
 C_{bc}(0)=
 \frac{(-1)^c c!\,(\omega^{b+1}-1)}
      {\prod_{\nu=0}^{c}(b+1+N\nu)}.
 \tag{19}
\]
To verify this, expand \((w^N-1)^c/N^c\), integrate its terms, use
\(\omega^N=1\), and apply
\[
 \sum_{\nu=0}^{c}
 \frac{(-1)^{c-\nu}\binom c\nu}{B+N\nu}
 =\frac{(-1)^c c!N^c}{\prod_{\nu=0}^{c}(B+N\nu)},
 \qquad B=b+1.
 \tag{20}
\]
Identity (20) follows by partial fractions, or by induction on \(c\).
All its denominators are nonzero. For the unique top monomial,
\(0\le b_0\le N-2\), so \(\omega^{b_0+1}\ne1\). Hence
\[
           A_k:=\gamma_{a_0b_0c_0}C_{b_0c_0}(0)\ne0.
 \tag{21}
\]

## 5. The second implicit solve and the pole-time contradiction

Introduce a formal parameter \(s\), and seek endpoints of the form
\[
 x=s^k,\qquad v=s^{k-\ell}V(s),\qquad
 \varepsilon=\frac{s^\ell}{V(s)},\qquad V(0)\ne0.
 \tag{22}
\]
Because \(k>\ell\), both \(x\) and \(v\) will have positive order.
Substitution into the bracket in (18) gives the complete expression
\[
 \mathcal B(s,V)=
 \Omega(s^\ell/V)-1+
 \sum_{a+b+c=\ell}\gamma_{abc}
 s^{\ell(k-r)}V^r C_{bc}(s^\ell/V),\qquad r=b+Nc.
 \tag{23}
\]
Every exponent \(k-r\) is nonnegative. Choose \(V_0\ne0\) satisfying
\[
                         A_kV_0^k=-(\omega-1).
 \tag{24}
\]
In the complete local ring \(\mathbb C[[s,V-V_0]]\), \(V\) is a unit, so
all compositions in (23) are defined. The uniqueness of the top monomial
gives
\[
 \mathcal B(0,V)=\omega-1+A_kV^k,\qquad
 \partial_V\mathcal B(0,V_0)=kA_kV_0^{k-1}\ne0.
 \tag{25}
\]
The same elementary coefficient recursion as in Section 3 now gives
a unit \(V(s)\in\mathbb C[[s]]\) with
\(\mathcal B(s,V(s))=0\). This is a second, separate implicit solve.

Let \(v(s)\) and \(\varepsilon(s)\) be as in (22). The two points
\[
 \begin{split}
 p_s&=(s^k,v(s),0,0),\\
 q_s&=(s^k,v(s)\Omega(\varepsilon(s)),0,0)
 \end{split}
 \tag{26}
\]
belong to \(\mathbb C[[s]]^4\). The first implicit identity returns the
base \(z\)-coordinate to zero. The second returns the full \(t\)-coordinate
to zero. Therefore the polynomial \(E\)-flow at the Laurent-series time
\[
 \tau(s)=
 \frac{v(s)}{s^{jk}}\bigl(\Omega(\varepsilon(s))-1\bigr)
 \tag{27}
\]
sends \(p_s\) exactly to \(q_s\). All these assertions hold in
\(\mathbb C((s))\). Since the flow is a finite polynomial flow, substituting
a Laurent-series time is legitimate.

The leading coefficient of the numerator in (27) is
\(V_0(\omega-1)\ne0\), and
\[
                    \operatorname{ord}_s\tau
                    =-\ell-(j-1)k<0.
 \tag{28}
\]
If a polynomial \(u\in R[t]\) satisfied \(Eu=1\), its finite flow identity
would give
\[
                         u(q_s)-u(p_s)=\tau(s).
 \tag{29}
\]
The left side lies in \(\mathbb C[[s]]\), whereas the right side has a
pole. This contradiction excludes every \(k\ge qN\), proving (2).
The endpoints need only be formal integral points. The argument does not
assert their convergence or replace them by a numerical grid.

## 6. Boundaries of the conclusion

The proof gives a necessary condition for a whole polynomial slice.
It does not construct a slice when (2) holds, nor show that a particular
polynomial shear lowers a coordinate degree. It makes no assumption that
the supplied slice is an ambient coordinate.

The positive condition \(q=\ell-d\ge1\) is used in (9), (11), and the
two formal substitutions. It must not be dropped. For example,
\[
 H=x^2\partial_y+y^2\partial_z,\qquad
 \psi=x,\qquad u=y+(1-x)t
 \tag{30}
\]
satisfy \(Eu=1\), although \(d=\ell=1\), \(q=0\), and
\(\deg_H\psi+1=1>qN=0\). This boundary is outside the theorem.

Irreducibility is used in the normalization (4). No assertion is made
for arbitrary invariant replicas of \(H\). The argument does not extend
itself to nontriangularizable homogeneous rank-two derivations or to
arbitrary rank-three bases.

## 7. The precise primary-source corollary

Parnashree Ghosh, *A note on homogeneous rank 2 locally nilpotent derivations
on \(k[X,Y,Z]\)*, arXiv:2206.05906v4, Lemma 2.5, states that an
ordinary-homogeneous triangularizable locally nilpotent derivation admits
a linear triangular coordinate system:
[primary text, Lemma 2.5 and its proof](https://arxiv.org/html/2206.05906v4).

The lemma and proof were read directly for this note. Its proof takes the
linear parts of a polynomial triangular coordinate system. These linear
parts form an invertible frame; homogeneity makes their derivation images
triangular. Applied over \(\mathbb C\), it supplies exactly the linear
frame needed in Section 1.

Consequently (2) holds under the theorem's hypotheses with
“triangular in a linear coordinate system” replaced by “polynomially
triangularizable.” Ordinary degree, irreducibility, slicedness, and the
maximum \(H\)-degree of the linear space are preserved by the resulting
linear transport. No rank-two triangularizability theorem is being
imported: the cited paper also discusses nontriangularizable homogeneous
rank-two examples.

## 8. Verification and status limits

Fresh unsaved symbolic calculations checked the entire orbit and return
formulas before imposing the implicit return equation. In particular:

- For \(j=2\), the full base polynomial was
  \(P_2=y^2+Axy+Bx^2\), with unrestricted symbols \(A,B\).
- For \(j=3\), it was
  \(P_3=y^3+2xy^2+3x^2y+5x^3\).
- In both cases, the tested \(\psi\) contained every ordinary degree-\(j\)
  monomial with nonzero coefficients. The entire \(t\)-displacement,
  entire \(z\)-return, and derivative giving the first implicit solve
  agreed with (13)--(18).
- Separate exact checks verified (19)--(20) for \(j=2,\ldots,6\),
  \(0\le b<2N\), and \(0\le c\le4\), and the high-weight uniqueness
  inequalities for several complete ordinary-degree ranges.

The uniform proof is Sections 1--5, not those finite checks. No saved
checker was executed, imported, or compiled. No unfinished neighboring
source is a proof input. The only external theorem used for the optional
corollary is the primary lemma identified in Section 7.

This source is ready for independent saved-source review only after its
author has read the entire saved text and issued a final HELD hash.
There is no claim of independent acceptance, novelty, arbitrary four-ring
entry, or a solution of cancellation.
