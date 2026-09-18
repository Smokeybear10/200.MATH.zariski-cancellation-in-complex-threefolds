# A transverse cubic cannot have an affine or constant first intercept

In the FULL actual264 chart with affine nonconstant intrinsic sigma,
the following hypotheses are inconsistent:
\[
 P=\sigma,\qquad m=k_s\ne0,\qquad h=m_s\ne0,\qquad
 \deg_P\theta=3,\qquad \deg_Py\le1.
\tag{1}
\]
The zero polynomial y is included. The proof uses only the complete
first two potential identities and the all-X polynomial return.
It reduces that return to two generators of degrees three and five,
then rules them out by an explicit divided-difference resultant.

No third-level coefficient gate, universal multiplier, normalization
of m or h, or plane-embedding classification is needed. The result
is only this specified affine-sigma, cubic-theta, low-intercept sector.

## 1. Full actual input and the all-X return

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
In particular, with notation distinguishing the original global
slice from the intrinsic parameter, retain
\[
 \begin{gathered}
 \mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
 E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
 \deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
 I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
 \text{ is the FULL initial kernel},\\
 N=[u_{\rm glob}^4]\partial_Z|_A\ne0,\qquad
 L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
 Na_0=Nt=Ns=0,\qquad
 A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad
 P=\sigma,\quad \deg_v\sigma=1,\quad NP=\rho\in L^*.
 \end{gathered}
\tag{2}
\]
The coefficient partials are the exact commuting extensions from
C(t,s) to L. No rationality of this finite extension is presumed.
All original actual hypotheses, the selected literal Z-partial,
and both strong returns remain retained. In the latter, z_int is
the literal original Z-intercept, not the corrected expression
z_int-2ty:
\[
 \operatorname{Frac}A=L(P)=\mathbb C(y,z_{\rm int},w),\qquad
 L[y,z_{\rm int},w]=L[P].
\tag{3}
\]

We will use the stronger all-X polynomial equality
\[
 L[X,Y,Z,W]=L[X,P].
\tag{4}
\]
Here is its localization license. Localizing the actual equality
B=A[u_glob] at the nonzero elements of ker N gives L[P][u_glob].
Since a0 is a nonzero element of ker N and x0 lies in A,
the exact expression X=a0*u_glob+x0 makes this ring equal to
L[P][X]. Localizing the actual coordinate presentation on the
other side gives L[X,Y,Z,W]. This proves (4), without identifying
the original slice with X/a0 or promoting an intrinsic parameter
to an ambient coordinate.

Write p=m_t. The entire literal rows from the first two potentials
are
\[
 \begin{aligned}
 Y&=y+PX+tX^2,\\
 Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2,\\
 mw&=\ell-(2P+k_t)y-\frac{k_{tt}}2P^2
       -pP\theta-\frac h2\theta^2-n_tP-n_s\theta.
 \end{aligned}
\tag{5}
\]
All k,n,ell and their indicated derivatives lie in L. These are
the complete polynomials, including every moving lower coefficient.
The full chart also retains its nonzero scalar
J_(t,s,P)(Y,Z,W)=-a0^4/rho; no coefficient of that scalar is
discarded or set to zero in this proof.

## 2. A coefficient-field specialization of the complete rows

Write
\[
 y=lP+r,\qquad \theta=aP^3+bP^2+cP+d,\qquad
 l,r,b,c,d\in L,\quad a\in L^*.
\tag{6}
\]
The choices l=0 or r=0, including y=0, need no separate division.
We do not need to prove that l is complex or constant under either
coefficient derivative.

Apply the L-algebra evaluation X=-l to (4). Its legitimacy is
the equality of polynomial rings over L, not an actual complex
ambient fiber assertion. Denote the three evaluated rows by
Y_bar,Z_bar,W_bar. Then
\[
 \begin{aligned}
 Y_{\rm bar}&=r+tl^2\in L,\\
 S_2(P)&=P^2+k_tP+2tr+n-kl+t^2l^2,\\
 Z_{\rm bar}&=m\theta+S_2(P),\qquad
 L[Z_{\rm bar},W_{\rm bar}]=L[P].
 \end{aligned}
\tag{7}
\]
In particular Z_bar has exact degree three and leader ma, which
is nonzero. The t²l² in S2 comes from the literal t²X² term.

Inside this coefficient-field polynomial return only, put
\[
 V_{\rm bar}=W_{\rm bar}+\frac{h}{2m^3}Z_{\rm bar}^2.
\tag{8}
\]
This operation has the polynomial inverse
W_bar=V_bar-h Z_bar²/(2m³) over L. The denominator is nonzero
because m is. We make no claim that h/m³ is complex or that
(8) is an actual ambient coordinate transformation.

Substitution of the ENTIRE rows (5) gives the identity
\[
 \begin{aligned}
 V_{\rm bar}={}&
 \left(\frac{hS_2}{m^2}-\frac{pP+n_s}{m}-l\right)\theta
       +\frac{hS_2^2}{2m^3}\\
 &+\frac{\ell-(2P+k_t)(lP+r)-k_{tt}P^2/2-n_tP}{m}
       +sl^2.
 \end{aligned}
\tag{9}
\]
The two theta-squared terms cancel exactly. The coefficient of
theta in (9) has exact degree two, with leader h/m². Every term
outside that product has degree at most four. Consequently
\[
 \deg_P Z_{\rm bar}=3,\qquad \deg_P V_{\rm bar}=5,\qquad
 \operatorname{lc}_P Z_{\rm bar}=ma,\qquad
 \operatorname{lc}_P V_{\rm bar}=ha/m^2,
 \qquad L[Z_{\rm bar},V_{\rm bar}]=L[P].
\tag{10}
\]
Both leaders are nonzero by (1),(6). No lower coefficient, including
ell, n, r, l or any displayed derivative, was specialized away.

## 3. The exact degree-three/degree-five obstruction

We prove the needed elementary statement over any characteristic-zero
field F: if f,g belong to F[P] with degrees three and five, then
F[f,g] is not F[P]. We may pass to an algebraic closure M of F,
since equality would persist there and both degrees are unchanged.
Write their nonzero leaders as u and v, respectively.

If M[f,g]=M[P], there is a polynomial T(A,B) over M satisfying
T(f(P),g(P))=P. For independent variables P,Q define the
polynomial divided differences
\[
 D_f(P,Q)=\frac{f(P)-f(Q)}{P-Q},\qquad
 D_g(P,Q)=\frac{g(P)-g(Q)}{P-Q}.
\tag{11}
\]
These quotients are polynomials. Subtract the two identities for
P and Q and telescope the polynomial T in its two arguments.
This gives C_f,C_g in M[P,Q] with
\[
 1=C_f(P,Q)D_f(P,Q)+C_g(P,Q)D_g(P,Q).
\tag{12}
\]
Thus the two divided differences could have no common zero.

Their degrees in P are always two and four, with respective
constant nonzero leaders u,v, independently of Q. Their total
highest homogeneous forms are
\[
 \begin{aligned}
 (D_f)_{[2]}&=u(P^2+PQ+Q^2),\\
 (D_g)_{[4]}&=v(P^4+P^3Q+P^2Q^2+PQ^3+Q^4).
 \end{aligned}
\tag{13}
\]
Let R(Q)=Res_P(D_f,D_g). The Sylvester determinant gives
deg_Q R<=8, with degree-eight coefficient the homogeneous
resultant in (13). For an explicit check of this bound, under
P=T/epsilon, Q=1/epsilon the polynomials
epsilon² D_f(T/epsilon,1/epsilon) and
epsilon⁴ D_g(T/epsilon,1/epsilon) have coefficients polynomial
in epsilon. Their resultant in T equals epsilon⁸ R(1/epsilon).
This proves the bound and identifies its constant term with the
resultant of (13) at Q=1.

The entire homogeneous resultant is
\[
 \operatorname{Res}_P(P^2+PQ+Q^2,
          P^4+P^3Q+P^2Q^2+PQ^3+Q^4)=Q^8.
\tag{14}
\]
Indeed reduction of the second polynomial modulo the first is
Q³(P+Q). Taking the resultant gives Q⁶ times the first
polynomial evaluated at P=-Q, namely Q⁸. Therefore
\[
 \deg_Q R=8,\qquad [Q^8]R=u^4v^2\ne0.
\tag{15}
\]
There is a root q0 in M. At Q=q0, neither P-leading coefficient
vanishes, so the specialized resultant is the resultant of
polynomials of exact degrees two and four. Its vanishing supplies
a common FINITE root p0 in M. There is no loss of degree or
root-at-infinity substitution. Evaluating (12) at (p0,q0) is the
contradiction 1=0.

This reasoning also permits p0=q0. On that diagonal the divided
differences evaluate to f'(q0),g'(q0), and (12) still excludes
their simultaneous vanishing. No separate injectivity-only
assumption or unproved immersion hypothesis is being used.

## 4. Conclusion, boundaries and verification

Apply Section3 to the exact pair in (10), with F=L. Its asserted
polynomial return contradicts (15). This proves (1).

The proof never divides by l, r, p, a derivative of h/m³, a
gradient, or a moving level. Its only field divisions involve
the nonzero m, the characteristic-zero constants, and the
nonzero polynomial leaders in the resultant argument. It includes
every constant and zero choice of y. The hypotheses h!=0 and
deg theta=3 are essential to the specific degree pair used here;
no other theta degree or h=0 branch is asserted to be excluded.

The complete actual264 input was read through EOF5f600e+3ce6a4,
with SHA59d9c34f95cf473b28a67bcb532599adadc07d700b219a0f24cd4d8fc6576a75
confirmed in58a02b. Its earlier entry dependencies are retained,
not recursively re-certified by this note. The localization
needed for the all-X equality is explicitly repeated above.

Fresh unsaved fffed0 rebuilt the COMPLETE original Y,Z,W rows
with unrestricted lower coefficients, specialized X=-l, and
checked (7),(9), cancellation of degree six, and both leaders in
(10). All six residuals were zero. It also checked the entire
homogeneous resultant (14) and the scaled value u⁴v²Q⁸.
The lower-coefficient independence and finite-root argument are
the symbolic proof above, not a finite-grid test.

No Abhyankar-Moh theorem or other plane-embedding classification
is a dependency of this proof. No coefficient-field substitution
is promoted to an actual ambient coordinate. No saved checker
was executed, imported, compiled or rerun, and no earlier source
or canonical file was edited. This is a bounded exclusion inside
the supplied chart, not recognition of all charts or an assertion
about unrestricted cancellation.
