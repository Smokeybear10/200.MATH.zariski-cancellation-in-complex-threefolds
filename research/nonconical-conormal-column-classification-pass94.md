# Polynomial conormal columns and the remaining double-component intersection

In the varying-column sector of the actual quadratic frame, the
quotient conormal column has only two polynomial shapes after constant
base changes: the span of 1,c, or the span of t,t^k with k at least
two and t an affine component parameter. The latter has exactly one
quotient-rank-zero point on the component. At multiplicity two that
point must meet a second fixed fiber component, and that companion
cannot itself be collapsed.

These are restrictions on actual components, not a recognition
theorem or a proof that the two-component configuration exists.

## 1. The centered generators and varying column

Retain the actual quadratic nonconical frame and the
[weighted conormal theorem94](nonconical-weighted-conormal-rigidity-pass94.md).
Let the collapsed rank-one fixed component have ideal \(\mathfrak q\).
Assume the first normal action of N is nonzero generically. The
constant-row conclusion permits a constant change of the original
good normal coordinates so that
\[
\begin{gathered}
\mathfrak qB=(X,Y),\qquad
F=X-uEX,\quad G=Y-uEY,\qquad \mathfrak q=(F,G)A,\\
N^3F=N^3G=0,\qquad A/\mathfrak q=\mathbb C[\bar c],\\
(s_1-s_1(m),s_2-s_2(m))^t
 \equiv(\ell_1(c),\ell_2(c))^t F\pmod{\mathfrak q^2}.
\end{gathered}
\tag{1}
\]
The polynomial column \(\ell\) has nonconstant projective direction.
In particular its two entries are linearly independent over
\(\mathbb C\). Make a constant base change so \(\ell_1\ne0\).

At the generic point, take \(x=s_1-s_1(m)\), \(y=G\), and the actual
coefficient field \(\mathbb C(c)\). These are valid local parameters:
the first normal coefficient of x is \(\ell_1F\), with
\(\ell_1\) nonzero in the residue field. Put \(f=s_2-s_2(m)\).
The weighted proof, with weights \(\mu,1\) on x,y, gives
\[
\begin{gathered}
f_*=\alpha(c)x+a(c)y^\mu,\qquad
\alpha=\ell_2/\ell_1,\quad a\ne0,\quad \mu\ge2,\\
D_*=(\gamma x+\rho y^\mu)\partial_y+
            \lambda y^{\mu-1}\partial_c,\\
\gamma=-\epsilon_0\alpha'\ne0,\qquad
\rho=-\epsilon_0a',\qquad
\lambda=\mu\epsilon_0a\ne0,\qquad D_*^3y=0.
\end{gathered}
\tag{2}
\]
All these coefficients are rational functions of c. The last
identity uses the exact N-degree bound on the actual generator
G, not local nilpotence on a completed field.

## 2. The two surviving coefficients

Direct differentiation gives
\[
\begin{gathered}
D_*^2y=C_0xy^{\mu-1}+K_0y^{2\mu-1},\\
C_0=\lambda\gamma'+\mu\gamma\rho,\qquad
K_0=\lambda\rho'+\mu\rho^2.
\end{gathered}
\tag{3}
\]
The coefficient of \(x^2y^{\mu-2}\) in \(D_*^3y\) is
\((\mu-1)\gamma C_0\), so C0 is zero. After imposing this, the
coefficient of \(xy^{2\mu-2}\) is \((2\mu-1)\gamma K_0\), so K0
is zero too. Thus \(D_*^2y=0\), only on the associated graded ring.

Set \(k_1=\epsilon_0\alpha'/a\) and \(k_2=\epsilon_0a'/a\).
Substituting the exact coefficients from (2) gives
\[
\begin{gathered}
C_0=-\mu\epsilon_0a^2k_1',\qquad
K_0=-\mu\epsilon_0a^2k_2',\\
k_1\in\mathbb C^*,\quad k_2\in\mathbb C,\qquad
a=r\alpha+s,\quad r=k_2/k_1,\quad s\in\mathbb C,\\
D_*y=-k_1(rf_*+s x),\qquad D_*^2y=0.
\end{gathered}
\tag{4}
\]
The constants follow because the derivative constants of
\(\mathbb C(c)\) are exactly \(\mathbb C\). The affine relation
uses \(a'=r\alpha'\). It does not assert \(N^2G=0\) in A:
higher-weight terms remain in the actual derivation.

## 3. The original volume makes the column equation polynomial

The unit factor \(\epsilon_0\) in (2) is constrained by the actual
coordinate volume. Write \(\omega_A\wedge du\) for the original
four-dimensional volume, with the harmless constant orientation
factor included in \(\omega_A\). The threefold volume is a global
generator of its canonical module: this follows from the polynomial
cylinder and the slice decomposition.

Along the entire component, dF,dG form a normal basis and dc is
a tangent basis, since \(\mathfrak q=(F,G)\) and
\(A/\mathfrak q=\mathbb C[\bar c]\). The ratio of
\(dF\wedge dG\wedge dc\) to \(\omega_A\) restricts to a polynomial
in c that is nonzero at every complex point. It is therefore a
complex constant \(\nu\ne0\). This can also be read directly in
the original plane coordinates: modulo \((X,Y)\), the normal
matrix of (F,G) is \(I-uM\), whose determinant is one, while
\(c=z-qW^2/2+\text{constant}\) and \(u=W\) give a constant
nonzero tangent determinant.

Changing from F,G,c to x,y,c multiplies the volume by
\(\ell_1(c)\). The exact local Jacobian formula consequently gives
\[
\epsilon_0=\nu\ell_1(c),\qquad
\operatorname{Wr}(\ell_1,\ell_2)
 =\ell_1\ell_2'-\ell_2\ell_1'
 =\frac{k_1}{\nu}\bigl(r\ell_2+s\ell_1\bigr).
\tag{5}
\]
There is no unproved normalization of a rational unit to a constant.
The constant \(\nu\) comes from the actual volume along the full
affine line. Since the projective direction varies, the Wronskian
is nonzero.

## 4. Classification of the polynomial span

Here is the elementary polynomial lemma used in (5). If two
linearly independent polynomials span a space V and their nonzero
Wronskian belongs to V, then a constant basis change puts V into
one of the forms
\[
\boxed{\qquad
V=\operatorname{span}_{\mathbb C}\{1,c\}
\quad\text{or}\quad
V=\operatorname{span}_{\mathbb C}\{t,t^k\},
\quad t=c-c_0,\quad k\ge2.
\qquad}
\tag{6}
\]
Changing the basis only multiplies the Wronskian by a nonzero
constant. Cancel leading terms to choose a basis v,w of degrees
n and m with \(m>n\). Its Wronskian has degree \(m+n-1\):
the leading coefficient is multiplied by \(m-n\ne0\).
Since it lies in V, this degree is at most m, so \(n\le1\).

If n=0, normalize v=1. The equation \(w'=a+bw\) first forces
b=0 by degree, and then m=1. This gives the first case.
If n=1, normalize v=t. The equation
\(tw'-w=a t+bw\) forces \(b=m-1\); hence
\(tw'-mw=a t\). Coefficient comparison yields
\(w=A t^m-a t/(m-1)\), with \(A\ne0\). This gives the second
case. This proof does not require a priori coprimality of v,w.

Applying the lemma to (5) proves that the original polynomial
column in (1), after constant base changes, has these spans.
The ambient quotient differential along the component has rank
zero exactly where both entries vanish. Therefore it is rank
one everywhere in the first case and has exactly one rank-zero
point \(c=c_0\) in the second. This is the quotient differential,
not the original E-velocity Jacobian.

## 5. A rank drop on a double component requires a companion

Assume now \(\mu=2\). In the actual local Hamiltonian coordinates,
the linear terms of \(f_c,f_y\) have coefficient determinant
\(2a\alpha'\ne0\). Thus the fixed-scheme ideal \(I=N(A)A\) is
generically reduced along this component:
\[
I A_{\mathfrak q}=\mathfrak qA_{\mathfrak q}.
\tag{7}
\]
The [fixed-scheme theorem92](nonconical-fixed-scheme-structure-pass92.md)
makes \(A/I\) Cohen--Macaulay of pure dimension one, with no
embedded primes.

Suppose a closed point p of this component lies on no other
fixed component. After localization at p, the fixed scheme has
only one minimal prime and is generically reduced by (7).
A ring with no embedded associated primes injects into the
product of its localizations at minimal primes: a nonzero kernel
would have an associated prime not detected at any minimal prime.
Here the single generic localization is reduced, so the ring is
reduced. Consequently \(I_p=\mathfrak q_p\).

If the quotient differential had rank zero at p, every coefficient
of \(ds_1,ds_2\) in a local differential basis would lie in the
closed maximal ideal. Their two-by-two minors, which generate I
up to the retained local unit factor, would lie in its square.
But the actual smooth component has two independent normal
linear generators at p, so \(\mathfrak q_p\) is not contained in
that square. This contradicts \(I_p=\mathfrak q_p\). We conclude
\[
\boxed{\quad
\mu=2,\ \alpha'\ne0,\
\text{quotient rank zero at }p\in V(\mathfrak q)
\quad\Longrightarrow\quad
p\text{ lies on another fixed component}.
\quad}
\tag{8}
\]

Each fixed component is an entire closed-fiber component of
multiplicity at least two. The quadratic total bound is four.
Thus the second shape in (6), if it occurs for a double component,
forces exactly two whole-fiber components, both fixed and both
of multiplicity two, with no further component.

The companion cannot also be collapsed. For every collapsed
component over the same base point, the actual-plane theorem92
gives an original affine plane whose direction is the fixed
two-space spanned by \(b(m)\) and the z-direction. Distinct such
planes are parallel and disjoint. Components meeting at p have
cylinders meeting above p, so they cannot both be collapsed.
This proves the further necessary configuration
\[
\boxed{\quad
\text{double component with column span }\{t,t^k\}
\quad\Longrightarrow\quad
(2,2)\text{ fiber with a noncollapsed fixed companion}.
\quad}
\tag{9}
\]
This is not a construction or an exclusion of that configuration.

## 6. Scope and provenance

The polynomial Wronskian classification uses the original global
volume, the actual centered generators, and their exact degree
bounds. The associated-graded identity cannot be substituted for
an identity on the full ring. The first-normal-action-zero sector
is outside the varying-column classification.

The companion argument uses both multiplicity two and the pure
Cohen--Macaulay fixed-scheme theorem. At higher multiplicity,
generic fixed-scheme reducedness need not hold. No such conclusion
is asserted there.

The elementary coefficient identities and polynomial ODE are
proved above. Their local input is the newly saved weighted proof,
whose completion source is stated there. The CM and actual-plane
inputs retain their exact hypotheses from92. No historical
novelty, human expert review, formal verification, actual-frame
construction, or general cancellation result is claimed.
