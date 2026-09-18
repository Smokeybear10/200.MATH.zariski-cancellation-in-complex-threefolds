# The remaining product-radical conic forces an original-coordinate relation

Status: working exact-field exclusion. Review and execution evidence
is recorded separately in the ledger. This note addresses the
degree-at-most-two branch of the conic left by232. It does not assume
that the coefficient field is rational. The endpoint is an explicit
nonzero polynomial relation in the four original coordinates.

## 1. The precise actual chart

Assume the full supplied globally sliced exact1122 hypotheses of
[232](product-radical-conic-nonzero-square-root-mode-exclusion-pass232-working.md):
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),
\]
and the entire initial kernel is \((Z^2-XYW)\).
The actual selected coefficient derivation gives the exact field
\(L/\mathbb C(t,s)\), finite in characteristic zero, with
\(q=st,\rho=s^2t\). Its two extended coefficient partials commute
and have joint constant field \(\mathbb C\).
The affine conic parameter \(h=\rho y-t\theta\) has \(h_v\in L^*\).
Here \(h\) is not the original leading coefficient of \(W\).

The complete literal map from232 is
\[
\begin{aligned}
Y&=y+tX,\\
Z&=\frac{w}{2s}+k_ty-\frac{h^2}{8s^3t^3}
 -\frac{k_sh}{2st^2}+n+
 \left(sy-\frac{h}{2st}+k\right)X+stX^2,\\
W&=w+(s^2y-h/t)X+s^2tX^2,\\
R&=\frac{h+2s^2t k_s}{4s^3t^2},\qquad
J=\det\frac{\partial(Y,Z,W)}{\partial(t,s,h)}
   =-\frac{2st(EX)^3}{h_v}\in L^*.
\end{aligned}                                                    \tag{1}
\]
All coefficient derivatives in this note use \(t,s\), not the old
\(t,\rho\) partials. The determinant keeps \(X\) fixed and is independent
of \(X,h\). A parameter change in \(L[h]\) is never promoted to an
ambient polynomial coordinate change.

By232, it suffices to handle
\[
y=A h^2+B h+C,\qquad w=E_2 h^2+Fh+G,\qquad A\ne0.                 \tag{2}
\]
The conic theorem231 also applies: its return root is simple and
\(y_h\ne0\) there. We will derive a contradiction.

## 2. Leading coefficients and the nonvertex condition

The leading third-potential and scalar-determinant equations of232,
with cubic coefficient of \(w\) zero, give
\[
A=\frac{\alpha}{t},\qquad
k=-\frac1{8s^3\alpha t}+bt+d,\qquad
\alpha_t=b_t=d_t=0,\quad\alpha\ne0.                              \tag{3}
\]
Do not initially assume that \(\alpha,b,d\) are rational in \(s\).
The coefficient of \(h^5\) in (1) is
\[
-\frac{\alpha(t(E_2)_t+E_2)(2s^2\alpha b_s-tE_2)}
        {s^2t^3}.
\]
Either factor vanishes. If the second factor vanishes, it too implies
\(t(E_2)_t+E_2=0\), because its other coefficients are killed by
\(\partial_t\). Thus \(E_2=e/t\), where \(e_t=0\).
Next \([X^2h^2]J=0\) and \([Xh^4]J=0\) give successively
\[
B=4s^2\alpha d_s+2te+
           \frac{2s\alpha_s+5\alpha}{2s^2t\alpha},
\qquad s\alpha_s+2\alpha=0.
\]
The first raw coefficient is
\[
\frac{3(8s^4t\alpha^2d_s+4s^2t^3E_2\alpha
 -2s^2tB\alpha+2s\alpha_s+5\alpha)}{8s^4t^4\alpha};
\]
after these substitutions the second is
\(-5(s\alpha_s+2\alpha)/(8s^4t^6)\).
Consequently \(\alpha=c/s^2\), with \(c\in\mathbb C^*\), and
\[
\begin{gathered}
A=\frac{c}{s^2t},\quad E_2=\frac et,\quad
k=-\frac1{8cst}+bt+d,\quad
B=4c d_s+2te+\frac1{2s^2t},\\
h_R=-2s^2t k_s,\qquad
y_h(h_R)=2tK,\qquad K=e-2c b_s\ne0 .
\end{gathered}                                                   \tag{4}
\]
The final inequality is exactly231's nonvertex condition, with
\(\chi=-h/t\). It is not an extra genericity assumption.

Hereafter primes on functions killed by \(\partial_t\) mean
\(\partial_s\). All equations are in the exact coefficient field.

## 3. Complete integration of the next three unknown coefficients

Direct coefficient extraction from (1) gives
\[
[h^4]J=-\frac{K}{4s^4t^4}
 \left(8cs^2t e d'-4ct^2F_t-2ctF+
                     12s^2t^2e^2+se'+e\right).
                                                                  \tag{5}
\]
Since \(K\ne0\), it follows that
\[
F_t+\frac F{2t}=
 \frac{2s^2e d'}t+\frac{3s^2e^2}{c}+\frac{se'+e}{4ct^2}.
\]
If necessary extend the coefficient field by \(r^2=t\).
The full solution is
\[
F=4s^2e d'+\frac{2s^2e^2t}{c}
       -\frac{se'+e}{2ct}+\frac{\gamma}{r},
\qquad \gamma_t=0.                                                \tag{6}
\]
This retains the possible algebraic square-root mode: multiplying the
homogeneous equation by \(r\) makes its derivative zero. The algebraic
extension does not change the joint constants, since \(\mathbb C\)
is algebraically closed.

For clarity, the next two raw coefficients are
\([Xh^3]J=U/(4s^4t^5)\) and
\([X^2h]J=V/(16cs^4t^4)\), where
\[
\begin{aligned}
U={}&16c^2st^3n_t+8cs^2t^3e b'+2cst b''
 -4ct^3F_t+2ctC_t-2ctb'-4cC+4s^2t^3e^2+te,\\
V={}&64c^2s^3t^4n_t+32cs^4t^4e b'
 -32cs^4t^3e d'+8cs^3t^2b''+8cs^3t d''\\
 &+16cs^2t^3F-8cs^2t^2b'-8cs^2tC+8cs^2t d'
 -32s^4t^4e^2+4s^2t^2e-1.
\end{aligned}                                                     \tag{7}
\]
Eliminating \(n_t\) between these equations and using (6) gives
\[
C_t-\frac Ct=4s^2t e d'+\frac{s d''+d'}t+
 \gamma r+\frac{2s^2t^2e^2}{c}-\frac1{8cs^2t^2}.
\]
Its complete solution and the resulting complete solution for \(n\) are
\[
\begin{aligned}
C={}&4s^2e d't^2+\frac{s^2e^2t^3}{c}+2\gamma r^3
 -(s d''+d')+\frac1{16cs^2t}+jt,\\
N_2={}&\frac{-s b''+b'+j}{8cs}+\frac{e'}{8c^2}
                                      +\frac e{16c^2s},\\
n={}&\frac{s e(e-4cb')t}{8c^2}-\frac{N_2}{t}
 +\frac{s d''+d'}{8cs t^2}-\frac1{128c^2s^3t^3}+n_0,
\qquad j_t=(n_0)_t=0 .
\end{aligned}                                                     \tag{8}
\]
For example, the \(n_t\) equation is
\[
n_t=\frac{s e(e-4cb')}{8c^2}+\frac{N_2}{t^2}
 -\frac{s d''+d'}{4cs t^3}+\frac3{128c^2s^3t^4}.
\]
After subtracting the displayed primitives, the homogeneous freedoms
are precisely \(jt\) and \(n_0\). No logarithmic or unrecorded
algebraic mode is discarded.

## 4. Two residual coefficients remove the square-root mode

In the coordinates \(r,s,h\), the scalar determinant is
\(J_r=2rJ\). Its coefficient \([X^2]J_r\) is linear in \(G\)
with nonzero coefficient \(1/(rs^2)\).
Solving it gives
\[
\begin{aligned}
G={}&G_0+\gamma\left[
 \left(-2s^2b'+\frac{4s^2e}{c}\right)r^3
                       +2s^2d'r-\frac1{4cr}\right],\\
G_0={}&\frac{t^3s^4e^3}{c^2}
 +\frac{4t^2s^4e^2d'}c
 +t\left(\frac{s^2ej}c-\frac{s^3ee'}{2c^2}
                              -\frac{s^2e^2}{c^2}\right)\\
 &+2s^3b''d'-2s^2b'd'+2s^2n_0'
                         -\frac{s^3d'e'}c-\frac{s^2ed'}c\\
 &+\frac1t\left(2s^3d'd''+2s^2(d')^2+\frac{s^2b'''}{4c}
  -\frac{s j'}{4c}-\frac{s^2e''}{4c^2}
                    -\frac{se'}{4c^2}+\frac e{16c^2}\right)
 +\frac{s^2d'''+3s d''}{4ct^2}.
\end{aligned}                                                     \tag{9}
\]
Define the three residuals, all killed by \(\partial_t\),
\[
\mathcal D=s d'''+3d'',\qquad
\mathcal E=3s e''+6e'-2cs b''',\qquad
\mathcal I=j'-8cs^2d'd''-8cs(d')^2-\frac{e'}{2c}.
                                                                  \tag{10}
\]
Substitution of (6),(8),(9) into the literal determinant gives
\[
\begin{aligned}
[Xh^2]J_r
 &=\frac{-24csK\gamma r^7-(2\mathcal E+6c\mathcal I)r^2
                                      +10c\mathcal D}{8cr^9s^3},\\
[h^3]J_r
 &=\frac{12csK^2\gamma r^7-2cK\gamma' r^3
       +K(\mathcal E+2c\mathcal I)r^2-4cK\mathcal D}{4cr^9s^3}.
\end{aligned}                                                     \tag{11}
\]
The element \(r\) is transcendental over the \(\partial_t\)-constant
field: a polynomial relation of least degree, differentiated and
reduced, would contradict characteristic zero and \(r_t=1/(2r)\).
Equivalently its distinct integer powers have distinct eigenvalues
for \(r\partial_r\). Coefficient comparison in (11), with \(K\ne0\),
therefore gives
\[
\gamma=0,\qquad \mathcal D=\mathcal E=\mathcal I=0.                \tag{12}
\]
In particular the extension by \(r\) has introduced no surviving mode.

These differential equations integrate exactly:
\[
\begin{gathered}
d=d_0+d_1s+d_2/s,\qquad
j=4cs^2(d')^2+\frac e{2c}+j_0,\\
3se-2csb'+4cb=\lambda s+\mu ,
\qquad d_0,d_1,d_2,j_0,\lambda,\mu\in\mathbb C .
\end{gathered}                                                     \tag{13}
\]
Indeed \(\mathcal D=0\) is \((s^3d'')'=0\);
\(\mathcal I=0\) is the derivative of the asserted formula for \(j\);
and \(\mathcal E=0\) is the second derivative of
\(3se-2csb'+4cb\). All integration constants are also killed by
\(\partial_t\), so joint constancy makes them complex. This proves
completeness in the finite field, not only in its rational subfield.

Under (12), the last two terms of \(G_0\) simplify: its \(t^{-2}\)
coefficient is zero and its \(t^{-1}\) coefficient is
\[
\frac{s^2b'''}{12c}+\frac{se'}{8c^2}+\frac e{16c^2}
       =\frac{2s^2e''+6se'+e}{16c^2}.                             \tag{14}
\]
All other terms of (9) remain unchanged.

## 5. The final differential functions are rational with constant coefficients

After (13), the next two coefficients of the original \(J\) are
\[
[Xh]J=\frac{\mathcal N}{48cs^2t^4},\qquad
[h^2]J=-K[Xh]J,
\]
where
\[
\begin{aligned}
\mathcal N={}&s b''''+4b'''\\
 &+24ct\left(d_1s^2b'''+2d_1s b''-2d_1b'
                 -d_2b'''+s n_0''+2n_0'\right).
\end{aligned}                                                     \tag{15}
\]
Comparison of the constant and linear powers of \(t\) gives
\[
\begin{gathered}
b=b_0+b_1s+b_2s^2+b_3/s,\\
n_0=d_1b_1s-d_2b_3/s^3+n_1/s+n_2,\qquad
b_0,b_1,b_2,b_3,n_1,n_2\in\mathbb C,\\
e=e_0+e_1/s-2cb_3/s^2,\qquad
e_0=(\lambda-2cb_1)/3,\quad e_1=(\mu-4cb_0)/3 .
\end{gathered}                                                     \tag{16}
\]
For completeness, the first equation being integrated is
\((s^4b''')'=0\). Substituting its complete solution in the second
gives \((s^2n_0')'=2d_1b_1s-6d_2b_3/s^3\).
Subtracting the displayed primitives accounts for every integration
constant. The formula for \(e\) follows from (13).

## 6. An explicit contradiction in the original polynomial ring

The endpoint does not require a further large determinant expansion.
Introduce, only in the coefficient-field fraction ring, the parameter
\[
\upsilon=\frac{h+2s^2t d'+s^2t^2e/c+1/(4c)}{st}.
\]
Completing the square in (2),(8), and using (13), gives
\[
y=ct\upsilon^2-2d_1+j_0t,\qquad
\overline Y:=Y+2d_1=t(X+j_0+c\upsilon^2).                         \tag{17}
\]
Define the following actual original-coordinate polynomials:
\[
\begin{aligned}
\mathfrak a&=X+e_0/c,&
\mathfrak p&=X+b_1+e_0/(2c),\\
Z_1&=Z-(b_0+e_1/(2c))\overline Y-d_0X
                                  +2b_0d_1+2b_2d_2-n_2,\\
W_1&=W+2b_3\overline Y+2d_2X
                                  -2b_1d_2-6b_3d_1+2n_1 .
\end{aligned}                                                     \tag{18}
\]
All their coefficients are complex, as proved above.
Direct substitution of the complete formulas (4),(6),(8),(9),(16)
into the literal map (1) yields
\[
\begin{gathered}
\mathcal V=s\overline Y-\upsilon/2,\qquad
\mathcal T=s^2\overline Y-s\upsilon+\frac1{4ct},\\
Z_1=\mathfrak p\,\mathcal V+b_2\mathcal T,\qquad
W_1=\mathfrak a\,\mathcal T+(e_1/c)\mathcal V,\\
\overline Y\,\mathcal T
                  =\mathcal V^2+\frac{X+j_0}{4c}.
\end{gathered}                                                     \tag{19}
\]
The last identity follows immediately from (17), so it also checks
the constant term in the completed square.

Set \(\delta=\mathfrak p\mathfrak a-b_2e_1/c\), a monic quadratic
polynomial in \(X\). The two linear equations in (19) imply
\[
\delta\mathcal V=\mathfrak a Z_1-b_2W_1,\qquad
\delta\mathcal T=\mathfrak p W_1-(e_1/c)Z_1 .
\]
Multiplying the last equation of (19) by \(\delta^2\) therefore gives
the original-coordinate identity
\[
\boxed{\;
\delta\overline Y\bigl(\mathfrak p W_1-(e_1/c)Z_1\bigr)
 -(\mathfrak a Z_1-b_2W_1)^2
 -\frac{\delta^2(X+j_0)}{4c}=0 .
\;}                                                               \tag{20}
\]
This is a nonzero polynomial in \(\mathbb C[X,Y,Z,W]\): its coefficient
of \(Z^2\) is \(-\mathfrak a^2=-(X+e_0/c)^2\), which is nonzero.
The other terms have degree at most one in \(Z\). Equation (20)
contradicts algebraic independence of the actual four coordinates.
It is not merely a relation between generic-field substitutes for
original coordinates.

Thus the degree-at-most-two \(w\) conic cannot occur.

## 7. Consequence and verification boundary

The conic exclusions232 and this note, together with227--230, exclude
every branch for the precisely supplied globally sliced exact1122
frame whose entire initial kernel is \((Z^2-XYW)\). This is an
impossibility statement for that hypothesis class, not a nonempty new
family of cancellation examples.

The calculations above are identities with arbitrary lower coefficient
functions before their displayed equations are imposed. They are
obtained from the complete scalar determinant, not from numeric
samples or a finite grid. Exact-field integration and the original-ring
contradiction are explicit written steps. The ledger records the
independent raw reconstructions and complete saved-source reviews.
No claim of formal proof-assistant certification, human expert review,
historical novelty, unrestricted frame entry or full cancellation is
made. The full cancellation question remains unresolved.
