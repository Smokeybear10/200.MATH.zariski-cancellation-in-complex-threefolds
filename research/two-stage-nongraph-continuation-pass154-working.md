# Fixed-axis two-stage nongraphs cannot occur in the normalized actual frame

**Status: complete working proof under the stated hypotheses.**
This new154 note extends the nested-quartic argument153 to every
fixed-axis two-stage placement specified below. It is not part of
checkpoint153. The separate
[semiprime-degree corollary154](semiprime-generic-degree-recognition-pass154-working.md)
derives this placement in particular for nongraph generic degree six.

The exclusion requires an exact two-stage equation in the
already normalized formal axes. No general plane-coordinate classification
or arbitrary coefficient-dependent change of those axes is supplied.
No earlier artifact is changed. Finite symbolic controls do not
replace the universal argument or its explicit retained inputs.

## 1. Exact hypotheses and the additional placement

Retain the actual normalized dense chart153:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX\ne0,\quad
\deg_EW=m=\mu\ge2,\quad d=m+1,\\
f_m=\gamma\tau^d,\quad
\tau=EY/s,\quad \rho=EZ/s,\quad \gamma\in\mathbb C^*,\\
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
A_L=L[v],\qquad L[y,z]=L[v],\\
Y=y+\tau X,\quad Z=z+\rho X,\qquad
\deg\Phi=d,\quad \Phi_d=-\gamma U^d,\\
\Phi\in L^*g,\quad
\ker(L[U,V]\longrightarrow L[v])=(g),\\
\Psi(y,z)=v+\beta_0,\quad \beta_0\in L,\qquad
\Psi_U=\Phi_\tau,\quad \Psi_V=\Phi_\rho,\quad \deg\Psi\le d.
\end{gathered}
\tag{1}
\]
The last degree bound follows because the possible degree \(m+2\)
term differentiates the degree-\(m+1\) complex polynomial \(f_m\).
The coefficient partials commute through the finite extension and
have exact joint constant field \(\mathbb C\). These are retained
actual chart, primitivity and normalization inputs, not premises
inferred from arbitrary formal jets.[^1]

The additional placement requirement, not proved for a general
nongraph, is the literal fixed-axis equation
\[
\begin{gathered}
R=V-\mathcal A(U),\qquad
\Phi=\mathcal B(R)+\ell U+n,\\
\mathcal A\in L[U],\quad \deg\mathcal A=r\ge2,\qquad
\mathcal B\in L[T],\quad \deg\mathcal B=q\ge2,\\
d=rq,\qquad \ell\in L^*,\quad n\in L .
\end{gathered}
\tag{2}
\]
The variables \(U,V\) are exactly those of (1).
An arbitrary automorphism over \(L\) cannot be used to assert (2).
This equation gives \(L[U,V]/(\Phi)=L[R]\): solve
\(U=-(\mathcal B(R)+n)/\ell\), then \(V=R+\mathcal A(U)\).
Thus \(R(y,z)\) is an affine-linear parameter of \(L[v]\).

Translate \(R\) by a coefficient of \(L\), changing only the constant
term of \(\mathcal A\), to remove the outer coefficient of \(T^{q-1}\).
Absorb the outer constant coefficient into \(n\). This rewrites
the same \(\Phi\), not an original-coordinate change. Keep all
derivatives of the changed coefficients. Now
\[
\mathcal B(T)=\kappa T^q+\sum_{j=1}^{q-2}b_jT^j,\quad
\kappa\in L^*,\qquad
\Psi=\alpha R+\beta+c\Phi,\quad
\alpha\in L^*,\quad\beta,c\in L .
\tag{3}
\]
Indeed \(\Psi-\alpha R-\beta\) is divisible by the entire primitive
\(\Phi\). Its degree is at most \(d\), so its quotient is a
coefficient \(c\in L\).

## 2. Differential restrictions and complex constants

Compare the gradient identities in the independent variables \(U,R\):
\[
\begin{aligned}
0={}&\mathcal B_\tau(R)
+\mathcal B'(R)(c\mathcal A_U-\mathcal A_\tau)
+\ell_\tau U+n_\tau+\alpha\mathcal A_U-c\ell,\\
0={}&\mathcal B_\rho(R)
+\mathcal B'(R)(-\mathcal A_\rho-c)
+\ell_\rho U+n_\rho-\alpha .
\end{aligned}
\tag{4}
\]
Here \(\mathcal B_\tau,\mathcal B_\rho\) differentiate its coefficients.
For example
\(\Phi_\tau=\mathcal B_\tau(R)-\mathcal B'(R)\mathcal A_\tau+
\ell_\tau U+n_\tau\).

The \(R^q\) coefficients give \(\kappa_\tau=\kappa_\rho=0\).
The \(R^{q-1}\) coefficients, using the centering, give
\(\mathcal A_\tau=c\mathcal A_U,\ \mathcal A_\rho=-c\).
Remaining positive powers give \((b_j)_\tau=(b_j)_\rho=0\).
Consequently
\[
\begin{gathered}
\mathcal B\in\mathbb C[T],\quad \kappa\in\mathbb C^*,\qquad
\mathcal A_\tau=c\mathcal A_U,\quad\mathcal A_\rho=-c,\\
\ell_\tau U+n_\tau=-\alpha\mathcal A_U+c\ell,\qquad
\ell_\rho U+n_\rho=\alpha .
\end{gathered}
\tag{5}
\]
The first constant-in-\(R\) identity has left degree at most one
in \(U\). Since \(\alpha\ne0\), it forces \(r\le2\).
Thus \(r>2\) is already incompatible with the exact identities.

For \(r=2\), write \(\mathcal A=aU^2+bU+d_{\rm var}\).
Coefficient comparison and mixed partials give
\[
\begin{gathered}
a,\alpha\in\mathbb C^*,\qquad c\in\mathbb C,\\
b=2ac\tau+b_0,\qquad
d_{\rm var}=ac^2\tau^2+b_0c\tau-c\rho+d_0,\\
\ell=-2a\alpha\tau+\ell_0,\qquad
n=\alpha\rho-2a\alpha c\tau^2+
       (c\ell_0-\alpha b_0)\tau+n_0,\\
b_0,d_0,\ell_0,n_0\in\mathbb C .
\end{gathered}
\tag{6}
\]
In detail \(a_\tau=a_\rho=0,\ b_\tau=2ac,\ b_\rho=0\)
first give \(c_\rho=0\). Compatibility of
\((d_{\rm var})_\tau=cb,\ (d_{\rm var})_\rho=-c\)
then gives \(c_\tau=0\).
Next \(\ell_\tau=-2a\alpha,\ell_\rho=0\) give
\(\alpha_\rho=0\); compatibility of
\(n_\rho=\alpha,\ n_\tau=-\alpha b+c\ell\) gives
\(\alpha_\tau=0\).
These integrations use exact joint constants, not
\(L=\mathbb C(\tau,\rho)\).

## 3. An allowed translation and exact literal-tail identification

Make the actual complex affine good change \(x=X-c\).
The intercepts become \(y_0=y+c\tau,\ z_0=z+c\rho\);
speeds, ratios and \(L\) do not change.
Substituting \(U-c\tau,V-c\rho\) in (2) and (6) gives
\[
\begin{gathered}
A_0(U)=aU^2+b_0U+d_0,\qquad
C(U,V)=\mathcal B(V-A_0(U))+\ell_0U+n_0\in\mathbb C[U,V],\\
\Phi^{\,0}(U,V)=C(U,V)+\alpha\{\rho-\tau A_0'(U)\}.
\end{gathered}
\tag{7}
\]
The superscript denotes the first tail in the translated actual
chart, not a new hypothetical polynomial.

To justify that identification, the substituted old first tail
is irreducible, vanishes on \(y_0,z_0\), and still has leading
form \(-\gamma U^d\). The new canonical first tail is associated
with the same whole generic kernel by145. Its leading form is
also \(-\gamma U^d\): a constant translation of \(X\) leaves
\(f_m\) unchanged. The scalar of association is therefore one.
This uses no unproved binomial covariance of canonical coefficients.

All further notation refers to this chart. Rename \(y_0,z_0\)
as \(y,z\) and \(\Phi^0\) as \(\Phi\).
Thus \(Y=y+\tau x,\ Z=z+\rho x,\ Ex=s\ne0\).

## 4. Return of the canonical peeling coefficients

Write \(C=\sum_{k=0}^d C_k\) in complex homogeneous parts.
The signed first-tail formula is
\(\Phi=-\sum_{j=0}^mH_{j+1}(f_j;U,V)-f_{-1}\).
For \(j\ge1\), the degree-\(j+1\) part of (7) is \(C_{j+1}\).
Hence all derivatives of order \(j+1\) of
\(f_j+C_{j+1}(\tau,\rho)\) vanish. The finite-extension jet
lemma141 makes this difference a complex polynomial of degree
at most \(j\). The linear part gives
\(f_0=-C_1(\tau,\rho)+a\alpha\tau^2\) up to a complex constant.

Subtract the actual bad shear
\(\sum_{j=0}^{m-1}x^jP_j(Y/x,Z/x)\), using exactly those
lower-degree complex differences.
Every summand is a homogeneous polynomial of degree \(j\);
its apparent denominator cancels. The inverse adds it back.
By141 it changes just the corresponding canonical coefficient
and leaves the literal negative tails unchanged.
The top \(f_m=\gamma\tau^d=-C_d(\tau,\rho)\) needs no shear.
The normalized list is
\[
f_j=-C_{j+1}(\tau,\rho)\ (1\le j\le m),\qquad
f_0=-C_1(\tau,\rho)+a\alpha\tau^2,\qquad
f_{-1}=-C_0-\alpha\rho+\alpha b_0\tau .
\tag{8}
\]
These are statements about actual canonical coefficients,
not replacements of formal data merely sharing a leading term.
The literal translation argument and allowed shears are essential.[^2]

## 5. Actual selected Gauss cancellation and polynomial inverse

After the shear, define in the original polynomial ring
\[
R_0=Z-A_0(Y),\quad L_0=\ell_0Y+n_0,\qquad
H=xW+\mathcal B(R_0)+L_0,\quad I=xH+\alpha R_0 .
\tag{9}
\]
Use the selected common Taylor model145:
\[
\mathsf x=\varepsilon^{-1},\quad
\mathsf Y=\tau\varepsilon^{-1},\quad
\mathsf Z=\rho\varepsilon^{-1},\qquad
\mathsf W=\sum_{j=0}^mf_j\varepsilon^{-j}
 +f_{-1}\varepsilon+\varepsilon^2\zeta .
\]
The coefficient field is an abstract copy of \(L\), and
\(\zeta\) is transcendental over it. The selected embedding
Taylor-transports the coefficients and sends \(\zeta\) to an
element with transcendental residue over \(L\).
Thus Gauss order equals minus actual \(E\)-degree for nonzero
complex coordinate polynomials, by the actual inverse input145.[^3]

Equation (8) telescopes:
\[
\begin{gathered}
H(\mathsf x,\mathsf Y,\mathsf Z,\mathsf W)
 =a\alpha\tau^2\varepsilon^{-1}
       +\alpha b_0\tau-\alpha\rho+\varepsilon\zeta,\\
R_0(\mathsf x,\mathsf Y,\mathsf Z)
 =-a\tau^2\varepsilon^{-2}
       +(\rho-b_0\tau)\varepsilon^{-1}-d_0,\\
I(\mathsf x,\mathsf Y,\mathsf Z,\mathsf W)=\zeta-\alpha d_0,
\qquad \deg_EH=1,\quad EI=0 .
\end{gathered}
\tag{10}
\]
The leading coefficient \(a\alpha\tau^2\) is nonzero.
The polynomial \(I\) is nonconstant, also witnessed by
the actual selected partial \(TI=x^2\).

The actual triangular LND
\(\Delta=x\partial_{R_0}-\mathcal B'(R_0)\partial_W\)
on \(\mathbb C[x,Y,R_0,W]\) kills \(H\), including \(L_0\).
Its invariant multiple's flow \(\exp((H/\alpha)\Delta)\) gives
the generalized Nagata automorphism:
\[
\begin{gathered}
r_*=R_0+xH/\alpha=I/\alpha,\qquad
J=W-\frac{\mathcal B(r_*)-\mathcal B(R_0)}{x},\\
H^*=xJ+\mathcal B(r_*)+L_0=H,\\
R_0=r_*-xH^*/\alpha,\qquad
W=J+\frac{\mathcal B(r_*)-\mathcal B(R_0)}{x},\qquad
B=\mathbb C[x,Y,r_*,J].
\end{gathered}
\tag{11}
\]
Both quotients are polynomials because the two arguments differ
by a multiple of \(x\). The inverse uses
\(H^*=xJ+\mathcal B(r_*)+L_0\) in the new coordinates.
Either composition preserves \(H\) and restores \(R_0,W\).
Division by \(\alpha\) uses a nonzero complex constant;
there is no localization at \(x\).

Now \(Er_*=0\). If \(EJ\ne0\), \(xJ\) has actual time degree
at least two. It cannot cancel against the invariant
\(\mathcal B(r_*)\) and the degree-at-most-one \(L_0\) in
\(H=xJ+\mathcal B(r_*)+L_0\). Thus \(EJ=0\).

## 6. Contradiction

The original third good would satisfy
\[
\begin{gathered}
Z=r_*-\frac{x\{xJ+\mathcal B(r_*)+\ell_0Y+n_0\}}{\alpha}
       +aY^2+b_0Y+d_0,\\
0=E^2Z=2a t^2-\frac{2}{\alpha}(Js^2+\ell_0st),
\qquad s=Ex\ne0,\quad t=EY,\\
(2\alpha a t-\ell_0s)^2=(\ell_0^2+4\alpha aJ)s^2 .
\end{gathered}
\tag{12}
\]
This uses \(Er_*=EJ=0\) and \(E^2x=E^2Y=0\), not descent of
\(s,t\) into a smaller coefficient ring.
Since \(\alpha a\ne0\), the linear factor in \(J\) is prime in
the actual coordinate UFD (11). Its order on the nonzero right
side is odd; a nonzero square has even order. This is the
contradiction for \(r=2\), independently of \(q\).

Together with (5), this excludes all placements (2).
The literal post-translation tail, coefficient-return shears and
selected Gauss application are essential actual-coordinate steps.
Formal coefficient identities alone cannot replace them.

## 7. Exact remaining scope

Longer coordinate compositions, arbitrary coefficient-dependent
reframing, and entry into the dense three-good profile are outside
its scope. Formal two-stage equations without all actual inputs
(1) are not being excluded by an actual inverse argument.
No new finite-test result, historical novelty clearance, human
review, or formal proof certification is claimed.

## Sources and retained inputs

1. [Leading normalization153](dense-all-degree-leading-normalization-pass153-working.md),
   [dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [signed tails139](dense-negative-tail-relations-pass139-working.md),
   and [primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md).
   These supply exactly (1), including the complex leading coefficient,
   whole generic line and literal signed derivative identities.
2. [Fixed-good shears and coefficient jets141](dense-shear-minimal-tail-pass141-working.md).
   Only complex polynomial bad shears and the exact finite-extension
   joint-constant argument are used.
3. [Common Taylor integrality145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Sections 1--3 and 7--9. Only the selected actual Gauss rule is used;
   an arbitrary formal component cannot replace it.
4. [Nested-quartic exclusion153](nested-quartic-exclusion-pass153-working.md).
   Its full saved proof was independently read before this continuation.
   The degree-four result is a precedent, not proof of arbitrary
   outer degree or fixed-axis applicability.

[^1]: Source 1. Exact joint constants also use Source 2.
[^2]: Sources 1 and 2, with each original-ring change displayed above.
[^3]: Source 3.
