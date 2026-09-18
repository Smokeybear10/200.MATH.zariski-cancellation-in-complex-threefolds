# Polynomial curve velocities cannot support the exact cubic branch

In the supplied actual constant-acceleration framework, the exact cubic
relative branch cannot have velocity \(b=(a(s),H(s,t),f(s))^t\), where
\(S=\mathbb C[s,t]\), a and f are polynomials in s, and \(H_t\ne0\).
Neither a nor H is required to be a polynomial coordinate. This removes
the additional first-component coordinate assumption in the
[polynomial-pullback exclusion118](cubic-polynomial-pullback-exclusion-pass118.md).

The proof has two separate parts. Formal expansions force the projected
polynomial curve to be a cubic graph after a constant linear change of
the original good coordinates. The irreducibility of an original
affine-linear coordinate then prevents a global realization. These are
conditional deductions in the retained actual framework, not a solution
of cancellation or a claim of historical novelty.

## 1. Precise hypotheses and the degree normalization

Retain the original-coordinate, intrinsic-kernel, potential, and volume
hypotheses of [potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md), and
[pullback118](cubic-polynomial-pullback-exclusion-pass118.md). In particular,

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=q_0u,\quad q_0\in\mathbb C^*,\\
S=\mathbb C[s,t]=\ker(N|A),\quad Nu=0,\quad
K=\mathbb C(s,t),\quad Ex_{\rm tr}=(a(s),H(s,t),f(s))^t,\\
a,f\in\mathbb C[s],\quad H\in S,\quad H_t\ne0,
\quad \det[b,b_s,b_t]\ne0,\\
A_K=K[y_1,y_2]=K[v],\qquad
\deg_Y\ker(K[Y_1,Y_2]\longrightarrow A_K)=3 .
\end{gathered}
\tag{1}
\]

The last degree means the degree of a generator of the principal
relative evaluation ideal. The derivation N is the actual intrinsic
locally nilpotent derivation, with the full kernel specified above.
The actual original-coordinate Jacobian is a unit in K[v,u], not merely
a nonzero rational function.

If a nonzero constant linear combination of a and f is zero, the frame
determinant in (1) vanishes. If such a combination is a nonzero constant,
b lies in a fixed affine plane. Applying its constant normal row to
\(b_{ij}=G_{ij}b+\sum C^l_{ij}b_l\) gives G=0, hence T=0,
incompatible with an exact cubic potential relation. These cases are
therefore excluded. In all other cases a constant invertible linear
change of the first and third original coordinates puts their degrees
in the order

\[
0<n:=\deg a<m:=\deg f .
\tag{2}
\]

Indeed, if the two degrees are equal, subtracting the leading-coefficient
multiple makes one smaller. A resulting constant or zero was just
excluded. A swap then gives (2). This is a constant ambient coordinate
change, not a base-dependent matrix or a polynomial reparametrization.
We keep the symbols a,f,x1,x3 for the new pair.

## 2. A commuting rational frame without a base inverse

Put x=a(s) and w=H(s,t). On K define

\[
\begin{gathered}
D_w=H_t^{-1}\partial_t,\qquad
D_x=(a')^{-1}\bigl(\partial_s-(H_s/H_t)\partial_t\bigr),\\
[D_x,D_w]=0,\quad D_xx=D_ww=1,\quad D_xw=D_wx=0,\\
\ker(D_w|K)=\mathbb C(s)=:k,\qquad
D_x|_k=\delta:=(a')^{-1}d/ds,\quad k^\delta=\mathbb C,\\
F=f(s),\quad F'=\delta F,\quad
\Gamma=F-xF'\ne0,\quad
\det[b,D_xb,D_wb]=\Gamma .
\end{gathered}
\tag{3}
\]

The field K is finite separable over C(x,w). The displayed derivations
commute because their commutator kills that transcendence basis. Their
kernel and constant assertions follow directly from their nonzero
multipliers of the usual derivatives. In particular, k need not equal
C(x). Subsequent primes on elements of k mean delta, not d/ds.

If the old tangent components were y1old,y2old, the new ones are
\(y_1=a'y_1^{\rm old}\) and
\(y_2=H_sy_1^{\rm old}+H_ty_2^{\rm old}\).
This is a GL2(K) change, preserves the exact degree of the relative
relation, and leaves the radial coefficient rho unchanged. The base
differential volume changes by \(a'H_t\in K^*\). The generic ring
is still the actual K[v,u]; no element involving v is inverted.
Extending D_x,D_w by killing v,u therefore preserves all the actual
potential and unit-volume calculations used in118.

The radial connection in this frame is
G11=g=F''/Gamma, with only C111=-xg and C211=-wg nonzero. Its only
possibly nonzero cubic component is tau=-g'-2xg squared. The scalar
argument of [cylinder118, Sections 2--3](cubic-cylinder-velocity-exclusion-pass118.md)
then gives the following necessary identities:

\[
\begin{gathered}
g=F''/\Gamma,\qquad \tau=-g'-2xg^2\ne0,\\
\rho=A(s)+c_0w,\qquad A\in k,\quad c_0\in\mathbb C,\\
h=-\frac14\left(3xg+\frac{\tau'}{\tau}\right),\qquad
\mathcal R(F):=h'+h^2+xgh-g=0 .
\end{gathered}
\tag{4}
\]

Here are the constant-field details needed to use that argument over k.
The unique cubic monomial makes y1 have generic degree one by the
degree-at-most-three generating-curve lemma90. Taking v=y1, the sixth
and fourth powers of v in the potential force
\(D_w^2\rho=D_xD_w\rho=0\). Thus D_w rho is in k and is killed
by delta, so is a complex constant. Subtracting c0w gives A in k.
Writing y2=R=r0+r1v+r2v squared+r3v cubed, the fifth and fourth volume
coefficients put r3,r2 in k. The next two make r1,r0 affine in w over k.
Exactness of \(L_i=D_i(\chi+q_0\rho^2/2)\) supplies
\(h=-L_2'/L_2\), while \(r_3=-q_0\tau/(6L_2)\).
The third and first volume coefficients give (4), exactly as in118.
Each integration uses ker D_w=k, and each w-coefficient comparison
uses the transcendence of w over k. None requires K=C(x,w).

## 3. The formal expansion field and the first degree restriction

These asymptotics are identities of formal Laurent series, not analytic
limits or numerical fits. Write z=1/s and
\(a(s)=a_nz^{-n}(1+O(z))\). Choose one nth root of the nonzero
complex number a_n. The binomial series
\(\xi=x^{-1/n}=a_n^{-1/n}z(1+O(z))\) has a nonzero linear term,
so possesses a unique compositional inverse z=z(xi). Consequently
k embeds in C((xi)), where x=xi to the power -n and delta acts as d/dx.
For any nonzero polynomial P(s), its leading term in this field is
\(\gamma x^{\deg(P)/n}\), followed by strictly smaller exponents.
This construction only uses binomial series and recursive formal
series inversion; no general Puiseux theorem is needed.

Let r=m/n>1. Since F has leading term kappa x to the power r, (4)
gives

\[
\begin{gathered}
g\sim-rx^{-2},\qquad \tau\sim-2r(r+1)x^{-3},\qquad
h\sim\frac{3(r+1)}{4x},\\
\mathcal R(F)
=-\frac{(3r-1)(r-3)}{16}x^{-2}
  +\text{terms of strictly smaller exponent} .
\end{gathered}
\tag{5}
\]

The leading coefficient must vanish. Under r>1 this forces r=3,
so m=3n. Set lambda equal to the ratio of the leading coefficients
of f and a cubed. Then lambda is nonzero and
\(f=\lambda a^3+P\), with P=0 or deg P<3n.

## 4. A first-variation calculation excludes every lower remainder

Multiplying F by a nonzero constant, or adding mu x for a constant mu,
leaves g, tau and the residual unchanged. Normalize lambda to one for
this step. For an auxiliary square-zero parameter epsilon and any
rational exponent r, substitute F=x cubed+epsilon x to the power r.
The coefficients of epsilon are

\[
\begin{gathered}
g=-3x^{-2}+\epsilon A_r x^{r-5},\qquad
A_r=-\tfrac12(r-1)(r-3),\\
\tau=-24x^{-3}+\epsilon A_r(17-r)x^{r-6},\\
h=3x^{-1}+\epsilon B_r x^{r-4},\qquad
B_r=\frac{(r-1)(r-3)(r^2-20r+123)}{192},\\
\mathcal R(x^3+\epsilon x^r)
=\epsilon\frac{(r-9)(r-7)(r-5)(r-3)(r-1)}{192}x^{r-5} .
\end{gathered}
\tag{6}
\]

For a direct reconstruction, if the perturbation is P, quotient
differentiation gives
\(\dot g=-(x^2P''-3xP'+3P)/(2x^5)\).
Then \(\dot\tau=-\dot g'+12\dot g/x\) and
\(\dot h=-[3x\dot g+(\dot\tau/\tau_0)']/4\), where
\(\tau_0=-24x^{-3}\). The residual's first variation is
\(\dot h'+3\dot h/x+2\dot g\).
For P=x to the power r this has coefficient
\((r-1)B_r+2A_r\), whose factorization is (6).
This also checks every sign and numerical factor without expanding a
high-degree rational numerator.

To apply (6) to an actual remainder rather than an infinitesimal one,
write F=x cubed(1+e), and set D=x d/dx. The quantities x squared g,
x cubed tau, xh and x squared R are rational expressions in
e,De,D squared e, and finitely many further D derivatives. Their
denominators at e=0 are nonzero constants, namely those arising from
Gamma/x cubed=-2 and x cubed tau=-24. They thus have formal power
series expansions in these small quantities. If e has leading order
x to the power r-3 with r<3, each term of degree at least two has
exponent at most 2(r-3), strictly below r-3. Applying D does not
increase exponents. Therefore, if the leading coefficient in (6) is
nonzero, it is exactly the leading nonzero coefficient of the full
residual. Smaller terms in e cannot change it.

If P is nonzero of degree d<3n, its normalized leading exponent is
r=d/n, with 0<=r<3. Among the five roots in (6), only r=1 is in
that interval. Thus (4) forces d=n. Choose mu so that subtracting
mu a cancels that leading term. Invariance of (4) under adding a
linear term shows that the new remainder must satisfy the same
condition. If nonzero, its degree is less than n, so 0<=r<1, where
(6) has no root. This is impossible. Restoring lambda gives

\[
f(s)=\lambda a(s)^3+\mu a(s),\qquad
\lambda\in\mathbb C^*,\quad\mu\in\mathbb C,\qquad
\rho=A(s)+c_0H(s,t) .
\tag{7}
\]

This proves the all-degree polynomial-curve restriction. In particular,
it does not merely test a bounded collection of degrees for a or f.

## 5. A root divisor contradicts an actual original coordinate

Let X=x3-mu x1. The reconstruction in the rational frame gives
x1=a(u+rho)+y1 and X=lambda a cubed(u+rho)+3lambda a squared y1.
Eliminating y1 yields

\[
X=3\lambda a^2x_1-2\lambda a^3u-2\lambda a^3\rho,
\qquad a^3\rho\in B\cap K=S,
\qquad T(s):=a^3A(s)\in\mathbb C[s] .
\tag{8}
\]

The intersection equality is essential. An element of B lying in K
is killed by E and hence lies in A. It is also killed by N; its full
kernel on A is the actual embedded S. Conversely S lies in both rings.
Subtracting c0a cubed H in S from a cubed rho now puts a cubed A in
S intersect C(s)=C[s], by comparison of t-coefficients. This does not
assert that A itself is polynomial.

Choose a complex root s0 of the nonconstant polynomial a and set
h0=-2lambda T(s0). All the terms of X-h0 in (8), with rho replaced
by A+c0H, are divisible by s-s0 in B. Thus

\[
X-h_0\in(s-s_0)B,\qquad
E(X-h_0)=\lambda a(s)^3\ne0,\qquad E(s-s_0)=0 .
\tag{9}
\]

But X-h0 is an actual affine-linear original coordinate, hence an
irreducible element of the polynomial four-ring B. The embedded
nonconstant s-s0 is a nonunit of B. Divisibility therefore makes it
associate to X-h0, with a nonzero complex constant as multiplier.
Applying E contradicts (9). This excludes (1) in the exact cubic
branch. Multiplicity of the root s0 is irrelevant, and a itself was
never required to be a base coordinate or irreducible.

## 6. Scope and independent checking

The [three-method checker119](cubic_polynomial_curve_checks_pass119.py)
checks the indicial and first-variation identities, selected genuinely
ramified rational-frame transfers and root-divisor reconstructions,
and selected fractional-exponent residual controls. It does not prove
formal series inversion, the all-degree leading-term comparison, the
full-kernel intersection, or original-coordinate irreducibility.
Those steps are written arguments above and require proof review.

The coefficient conclusion (7) is compatible with the principal-open
examples118. The contradiction only occurs when their expressions
are required to be global original polynomial coordinates with the
actual slice and full invariant kernels. No general rational first
integral is made polynomial or coordinate here. The geometric line
reduction needed to apply this result is a separate premise in
[line/rank119](cubic-coordinate-first-integral-line-pass119.md).
No new external classification theorem is used by this proof.
