# The normalized nested quartic cannot occur in an actual dense frame

The nested quartic alternative for the generic embedded line is
incompatible with an actual dense three-good frame of minimum
last-coordinate time degree three. The exact tail equations first
produce complex coefficients and a polynomial invariant of weight
five. An explicit Nagata-type automorphism makes two original-ring
coordinates invariant. The remaining good-coordinate identity then
makes a nonzero linear coordinate polynomial a rational square,
contradicting its prime valuation.

This excludes the nested alternative only. Recognition of the
quartic graph alternative and exhaustion of those alternatives are
separate statements. No arbitrary three-good entry, full cancellation,
or historical novelty conclusion is asserted.

## 1. Actual normalized hypotheses and the nested alternative

Assume the actual dense three-good setting, already put in the
leading normalization153 with \(m=\mu=3\):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX\ne0,\quad t=EY,\quad b_{\rm sp}=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b_{\rm sp})=2,
\quad\text{with dense homogeneous speed cone},\\
\deg_EW=3,\qquad f_3=\gamma\tau^4,\qquad
\tau=t/s,\quad\rho=b_{\rm sp}/s,\quad \gamma\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
All four displayed generators are actual complex polynomial
coordinates, and \(u\) is a global polynomial slice. The reduction
to (1) uses actual constant good reframing and fixed-good shears,
not a coordinate change over the coefficient field.[^1]

Use the exact dense chart and signed tails139/145:
\[
\begin{gathered}
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
A_L=L[v],\qquad L[y,z]=L[v],\\
Y=y+\tau X,\quad Z=z+\rho X,\qquad
\Phi\in L^*g,\quad \deg\Phi=4,\quad
\Phi_4=-\gamma U^4,\\
\ker(L[U,V]\longrightarrow L[v])=(g),\qquad
\Psi(y,z)=v+\beta_0,\quad\beta_0\in L,\\
\Psi_U=\Phi_\tau,\qquad\Psi_V=\Phi_\rho,\qquad
\deg\Psi\le4 .
\end{gathered}
\tag{2}
\]
The last degree bound improves the general bound five because
the only possible degree-five term is \(-H_5(f_3)\), which
vanishes for the quartic complex polynomial in (1).
The coefficient partials in (2) fix the independent formal
variables \(U,V\). They commute and have exact joint constant
field \(\mathbb C\), even through the finite extension.[^2]

The nested alternative considered here is
\(\deg_v y=2,\ \deg_v z=4\). The degree normalization of \(v\)
is immaterial. This note does not need a plane-embedding theorem
to derive the normal form within that alternative.

## 2. The nested form in the fixed formal axes

Complete the square in the quadratic polynomial \(y(v)\) by an
affine change of its parameter over \(L\), so that
\(y=A_2r_0^2+A_0\), with \(A_2\ne0\). This is only a description
of the generic parametrization, not an original-coordinate change.
Subtract from \(z\) a quadratic polynomial in \(y\), canceling its
fourth-, second-, and zeroth-degree terms. The remainder has the
form \(r_0(c_3r_0^2+c_1)\).

The generated ring is
\(L[r_0^2,r_0(c_3r_0^2+c_1)]\).
Its odd part over \(L[r_0^2]\) is
\(r_0(c_3r_0^2+c_1)L[r_0^2]\), since the square of the odd
generator lies in the even ring. Equality with \(L[r_0]\)
therefore forces \(c_3=0\) and \(c_1\ne0\).
Thus the remainder is a linear parameter.

Write that remainder as \(V-aU^2-bU-d\), with \(a\ne0\).
The image of \(U\) is quadratic in it. Completing the square
in that quadratic expression changes only \(d\), and gives
the following identity in the same formal \(U,V\) axes:
\[
\begin{gathered}
R=V-aU^2-bU-d,\qquad
\Phi=\kappa R^2+lU+n,\qquad
\kappa a l\ne0,\qquad \kappa a^2=-\gamma,\\
a,b,d,\kappa,l,n\in L,\qquad
\Psi=\alpha R+\beta+c\Phi,\qquad
\alpha\ne0,\quad \alpha,\beta,c\in L .
\end{gathered}
\tag{3}
\]
Indeed \(R(y,z)\) is affine-linear in \(v\); the parameter
identity for \(\Psi\) in (2) gives
\(\Psi-\alpha R-\beta\in(\Phi)\).
Its degree is at most four, whereas \(\deg\Phi=4\).
The quotient is therefore a coefficient \(c\in L\).
No assertion that \((\Phi,\Psi)\) is a plane automorphism is made.

## 3. The exact coefficient differential equations

Differentiate (3), retaining every derivative of its coefficients.
Comparison in the independent variables \(U,R\), using (2), gives
\[
\begin{array}{c|cc}
 &\partial_\tau&\partial_\rho\\ \hline
\kappa&0&0\\
a&0&0\\
b&2ca&0\\
d&cb&-c\\
l&-2a\alpha&0\\
n&-\alpha b+cl&\alpha .
\end{array}
\tag{4}
\]
For example, the \(\rho\) identity is
\[
\kappa_\rho R^2
-2\kappa R(a_\rho U^2+b_\rho U+d_\rho)
+l_\rho U+n_\rho
=\alpha+2c\kappa R.
\]
The \(\tau\) identity has right side
\(\alpha(-2aU-b)+c(2\kappa R(-2aU-b)+l)\).
Their coefficients give all entries of (4), without first
treating a coefficient-dependent axis change as constant.

Thus \(\kappa,a\in\mathbb C^*\). Compatibility for \(b\) gives
\(c_\rho=0\); compatibility for \(d\) then gives \(c_\tau=0\).
Hence \(c\in\mathbb C\), including \(c=0\).
Compatibility for \(l\) gives \(\alpha_\rho=0\), and that for
\(n\) gives \(\alpha_\tau=0\).
Therefore \(\alpha\in\mathbb C^*\).
Integrating (4) yields
\[
\begin{gathered}
b=2ca\tau+b_0,\qquad
d=c^2a\tau^2+cb_0\tau-c\rho+d_0,\\
l=-2a\alpha\tau+l_0,\qquad
n=\alpha\rho-2ca\alpha\tau^2
 +(cl_0-\alpha b_0)\tau+n_0,\\
b_0,d_0,l_0,n_0\in\mathbb C,\qquad
\kappa a^2=-\gamma .
\end{gathered}
\tag{5}
\]
These integrations use the exact joint constants of \(L\);
they do not assume \(L=\mathbb C(\tau,\rho)\).

## 4. Recovering the complex peeling coefficients

The homogeneous part of degree \(j+1\) in the first tail is
\(-H_{j+1}(f_j;U,V)\), and its constant term is \(-f_{-1}\).
Expanding \(\kappa R^2+lU+n\), and using (5), therefore
determines each \(f_j\) up to a complex polynomial of total
degree at most \(j\). This last assertion is the finite-extension
jet lemma141: all mixed derivatives of order \(j+1\) vanish
for the difference, so that difference is precisely such a
complex polynomial.[^2]

Remove those differences for \(j=0,1,2\) by actual fixed-good
shears \(W\mapsto W-\sum_{j=0}^2X^jP_j(Y/X,Z/X)\).
Each summand is a homogeneous complex polynomial of degree \(j\);
there is no denominator in this coordinate change, and its
inverse adds the same polynomial. These shears preserve
\(\Phi,\Psi,y,z\), the selected partial, and the top coefficient
\(f_3\).

With \(W\) renamed after this shear, the exact coefficients are
\[
\begin{aligned}
f_3={}&-\kappa a^2\tau^4,\\
f_2={}&-\kappa ca^2\tau^4-2\kappa ab_0\tau^3
       +2\kappa a\tau^2\rho,\\
f_1={}&-\kappa c^2a^2\tau^4-2\kappa cab_0\tau^3
       -\kappa(b_0^2+2ad_0)\tau^2\\
     &+2\kappa ac\tau^2\rho+2\kappa b_0\tau\rho-\kappa\rho^2,\\
f_0={}&-\kappa c^3a^2\tau^4-2\kappa c^2ab_0\tau^3
       +[a\alpha-\kappa c(b_0^2+2ad_0)]\tau^2\\
     &-(2\kappa b_0d_0+l_0)\tau
       +2\kappa c^2a\tau^2\rho+2\kappa cb_0\tau\rho
       +2\kappa d_0\rho-\kappa c\rho^2,\\
f_{-1}={}&-\kappa d^2-n .
\end{aligned}
\tag{6}
\]
The last line uses the coefficient polynomials \(d,n\) in (5).
For direct checks on the integrations, \(H_3(f_2)\) is the
negative cubic part \( -2\kappa ab\,U^3+2\kappa a\,U^2V\);
\(H_2(f_1;U,V)\) is the negative quadratic part of \(\Phi\);
and \((f_{0,\tau},f_{0,\rho})=(-(2\kappa bd+l),2\kappa d)\).
These identities verify (6) before the permitted lower-degree
differences are removed.

## 5. Finite Taylor cancellation gives an actual invariant

We use the selected actual Gauss calculation145, not an inference
from a formal Jacobian. In the common Taylor field write
\[
\begin{gathered}
\mathsf X=\varepsilon^{-1},\qquad
\mathsf Y=\tau\varepsilon^{-1},\qquad
\mathsf Z=\rho\varepsilon^{-1},\\
\mathsf W=f_3\varepsilon^{-3}+f_2\varepsilon^{-2}
 +f_1\varepsilon^{-1}+f_0+f_{-1}\varepsilon+\varepsilon^2\zeta,
\qquad \zeta\text{ transcendental over }L .
\end{gathered}
\tag{7}
\]
Strictly, the coefficient field here is an abstract copy of \(L\).
The selected embedding maps each coefficient through its Taylor
homomorphism and maps \(\zeta\) to \(\Psi(y,z)+O(\varepsilon)\).
The latter has transcendental residue over \(L\).
Consequently the Gauss valuation of any nonzero complex polynomial
in the four elements (7) is the negative of the actual \(E\)-degree
of that polynomial in \(B\). This is the selected noncancellation
argument145, which uses the actual coordinate inverse.[^3]

In the original polynomial ring, define
\[
\begin{gathered}
x=X-c,\qquad R_0=Z-aY^2-b_0Y-d_0,\qquad L_0=l_0Y+n_0,\\
H=xW+\kappa R_0^2+L_0,\qquad I=xH+\alpha R_0 .
\end{gathered}
\tag{8}
\]
Substitution of (6) into (7) gives
\[
\begin{gathered}
H(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
=a\alpha\tau^2\varepsilon^{-1}
 +ca\alpha\tau^2+\alpha b_0\tau-\alpha\rho+O(\varepsilon),\\
I(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)=O(1),\qquad
\deg_EH=1,\qquad EI=0 .
\end{gathered}
\tag{9}
\]
Here \(O(1)\) means nonnegative powers of \(\varepsilon\).
For an explicit coefficient check, put
\[
\begin{aligned}
P_3(\tau,\rho)&=-2\kappa ab_0\tau^3+2\kappa a\tau^2\rho,\\
P_2(\tau,\rho)&=-\kappa(b_0^2+2ad_0)\tau^2
                 +2\kappa b_0\tau\rho-\kappa\rho^2,\\
P_1(\tau,\rho)&=-(2\kappa b_0d_0+l_0)\tau+2\kappa d_0\rho .
\end{aligned}
\]
Then (6) gives \(f_2-cf_3=P_3\),
\(f_1-cf_2=P_2\), and
\(f_0-cf_1=a\alpha\tau^2+P_1\).
Also
\(f_{-1}-cf_0+\kappa d_0^2+n_0
=ca\alpha\tau^2+\alpha b_0\tau-\alpha\rho\).
These identities give the first line of (9).
Multiplication by \(\mathsf X-c\) gives just two possible
negative terms, which are canceled by \(\alpha R_0\).
This proves the second line using the actual Gauss rule.

The polynomial \(I\) is nonzero and nonconstant, since the
actual selected partial satisfies \(TI=x^2\ne0\).
No claim that the first leading relation itself already lifts
to an invariant of weight four is used. The polynomial in (8)
has weight five for the normalized weights \((1,1,1,3)\).

## 6. A polynomial change exposes two invariant coordinates

All constants in (8) are complex, with \(\alpha\ne0\).
The first triangular coordinate changes are
\[
\begin{gathered}
R_1=R_0+xL_0/\alpha,\qquad
W_1=W-2\kappa R_1L_0/\alpha+\kappa xL_0^2/\alpha^2,\\
R_0=R_1-xL_0/\alpha,\qquad
W=W_1+2\kappa R_1L_0/\alpha-\kappa xL_0^2/\alpha^2,\\
X=x+c,\qquad Z=R_0+aY^2+b_0Y+d_0,\\
B=\mathbb C[x,Y,R_1,W_1],\qquad
H_1:=xW_1+\kappa R_1^2=H-L_0,\qquad
I=\alpha R_1+xH_1,\qquad \deg_EH_1\le1 .
\end{gathered}
\tag{10}
\]
The displayed formulas prove both inverse orders directly.
The last degree bound uses (9) and the fact that \(L_0\)
has \(E\)-degree at most one.

On this actual coordinate ring put
\(\Delta=x\partial_{R_1}-2\kappa R_1\partial_{W_1}\).
It is triangular and locally nilpotent, with \(\Delta H_1=0\).
Its invariant multiple \((H_1/\alpha)\Delta\) is also an LND.
The corresponding polynomial automorphism has coordinates
\[
\begin{gathered}
r=R_1+xH_1/\alpha=I/\alpha,\\
J=W_1-2\kappa R_1H_1/\alpha-\kappa xH_1^2/\alpha^2,\qquad
H_1=xJ+\kappa r^2,\\
R_1=r-xH_1/\alpha,\qquad
W_1=J+2\kappa rH_1/\alpha-\kappa xH_1^2/\alpha^2,\\
B=\mathbb C[x,Y,r,J].
\end{gathered}
\tag{11}
\]
The inverse changes the flow sign; because \(H_1\) is fixed,
the inverse formulas in (11) are polynomial in \(x,Y,r,J\)
and verify both orders. This is an explicit automorphism,
not a Jacobian-conjecture inference.

By (9), \(Er=0\). Since \(Ex=s\ne0\), the polynomial \(x\)
has \(E\)-degree one. If \(EJ\ne0\), then the product \(xJ\)
has degree \(1+\deg_EJ\ge2\) in the actual domain \(A[u]\).
It cannot cancel its leading term against the invariant
\(\kappa r^2\). This contradicts \(H_1=xJ+\kappa r^2\)
and \(\deg_EH_1\le1\). Therefore
\[
Er=EJ=0,\qquad E^2x=E^2Y=0 .
\tag{12}
\]
It would already be possible to recognize the kernel using
these two invariant coordinates. The original third-good
identity gives a sharper contradiction without any further
classification theorem.

## 7. The third good coordinate forces an impossible square

The inverse formulas (10)--(11) give the original third good as
\[
\begin{gathered}
Z=r-\frac{x(xJ+\kappa r^2+l_0Y+n_0)}{\alpha}
       +aY^2+b_0Y+d_0,\\
0=E^2Z
 =2a t^2-\frac{2}{\alpha}(Js^2+l_0st),\qquad
s=Ex\ne0,\quad t=EY,\\
\boxed{\ (2\alpha a t-l_0s)^2
        =(l_0^2+4\alpha aJ)s^2\ } .
\end{gathered}
\tag{13}
\]
In taking the second derivative, use \(Er=EJ=0\),
\(E^2x=E^2Y=0\), and hence \(Es=Et=0\).
No assertion about the coefficient subring containing \(s,t\)
is needed.

The polynomial \(l_0^2+4\alpha aJ\) is a nonconstant affine-linear
polynomial in the actual coordinate \(J\), because
\(\alpha a\ne0\). It is irreducible and prime in the polynomial
UFD \(\mathbb C[x,Y,r,J]=B\).
Its order on the right of (13) is \(1+2\operatorname{ord}(s)\),
an odd integer. A nonzero square has even order.
The right side is nonzero because \(s\ne0\), so the zero-square
case cannot occur either. This is a contradiction.

Thus the normalized actual dense cubic-minimum frame cannot
have the nested generic degree pair \((2,4)\).

## 8. Exact scope

The coefficient-field plane description in (3) is derived from
the assumed degree pair, and every change in the original
four-ring later in the proof has complex polynomial formulas
and an explicit inverse. They are not the same kind of change.
The final prime is an actual coordinate prime in \(B\), not
a prime asserted to remain irreducible after an unchecked
coefficient specialization.

The proof uses the full signed canonical tails and the actual
selected Gauss rule. A formal quartic coordinate, a quotient
parameter, or a unit relative Jacobian alone does not supply
these hypotheses. No actual nested counterexample is claimed.

Exhaustion of all quartic generic degree patterns is not proved
here, and the quartic graph alternative is not treated here.
Consequently this note alone is not recognition for all
\(\mu=3\) frames. It also says nothing about arbitrary sliced
actions without the supplied dense three-good frame.
No historical novelty, human expert verification, formal proof
certification, or unrestricted cancellation result is asserted.

## Sources

1. [All-degree leading normalization153](dense-all-degree-leading-normalization-pass153-working.md),
   Sections 1--6. The actual minimizing shear, constant good
   reframing, and \(f_3=\gamma\tau^4\).
2. [Dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [signed negative tails139](dense-negative-tail-relations-pass139-working.md),
   and [fixed-good shears and coefficient jets141](dense-shear-minimal-tail-pass141-working.md).
   Exact field and ring hypotheses, both tail signs and formal
   gradient identities, and the finite-extension joint-constant
   and vanishing-jet arguments. The relevant full proofs were
   reread before this calculation.
3. [Common Taylor integrality and primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Sections 1--3 and 7--9. The selected actual Gauss valuation
   and the association of the entire first tail with the
   generic embedded-line equation. A hypothetical branch
   chosen after specialization cannot replace these inputs.
4. [Generic embedded-line degrees139](dense-generic-embedded-line-pass139-working.md),
   Sections 1--3. The exact whole-line generation and equality
   of implicit degree and maximum parametrization degree.
   The classical plane-embedding classification mentioned in
   that note is not used to prove the stated nested alternative
   here; the odd-part calculation in Section 2 is elementary.

[^1]: Source 1, with its retained actual cofactor and minimum inputs.
[^2]: Source 2.
[^3]: Source 3.
