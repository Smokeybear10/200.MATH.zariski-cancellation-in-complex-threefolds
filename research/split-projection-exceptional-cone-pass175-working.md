# The actual split chart has no whole-line projection defect

**Status: working proof under the full actual split-chart hypotheses.**

The two projected polynomials \(y,\vartheta\) generate the whole
generic parameter ring, including points where \(k_\rho-y\) vanishes.
The argument combines the two coefficient potentials with the
calibrated Jacobian. A squarefree center is handled by a finite
integral extension argument. The only remaining nonzero center is a
repeated quadratic, where the vertex-free cone lemma applies.

This establishes a polynomial plane embedding of degree at most four
over the exact coefficient field. It does not produce a coordinate
of the original complex polynomial four-ring or recognize its kernel.

## 1. Actual hypotheses and the precise conclusion

Retain the complete hypotheses and constructions of
[chart175](split-cubic-generic-chart-pass175-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\qquad
a=EX\ne0,\qquad N=[u^3](\partial_Z|_A)\ne0,\\
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1.
\end{gathered}
\tag{1}
\]
The formal weights are \((1,1,2,2)\), the initial ideal is the
full kernel, and \(\partial_Z\) fixes the original \(X,Y,W\).
The ratios \(t=EY/a\) and \(\rho=(E^2W/2)/a^2\) are independent,
and \(L/\mathbb C(t,\rho)\) is finite separable. Coefficient
partials extend uniquely to \(L\), commute, and fix \(v\).

The [zero-R proof175](split-zero-R-exclusion-pass175-working.md)
and [quartic bound175](split-cubic-projected-quartic-bound-pass175-working.md)
give
\[
\begin{gathered}
r=k_\rho\in L,\qquad R=r-y\ne0\text{ in }L[v],\\
L[y,\vartheta,w]=L[v],\qquad L(y,\vartheta)=L(v),\\
d:=\max(\deg_v y,\deg_v\vartheta)=\deg G\le4,
\end{gathered}
\tag{2}
\]
where \(G\) generates the prime kernel of
\(L[U,V]\to L[v]\), \(U\mapsto y,\ V\mapsto\vartheta\).
At least one of these two projected polynomials is nonconstant.
The nonzero \(R\) is not assumed to be a unit.

The conclusion of this note is
\[
L[y,\vartheta]=L[v].
\tag{3}
\]
Thus \(\operatorname{Spec}L[v]\to\mathbb A_L^2\) is a closed
embedding, with relation \(G\) of total degree \(d\le4\).
In particular a constant \(y\) makes \(\vartheta\) an affine
parameter, and a constant \(\vartheta\) makes \(y\) an affine
parameter. No assumption that either is constant is needed for (3).

## 2. The integral extension and its two return coefficients

Use the polynomial potentials from chart175 in independent \(U,V,W_0\):
\[
\begin{gathered}
f=H_2(k;U,V)+H_1(n;U,V),\qquad
g_3=H_3(k;U,V)+H_2(n;U,V),\\
\mathcal P=(r-U)W_0+f-\ell,\qquad
\Psi=f_VW_0+g_3-\ell_tU-\ell_\rho V,\\
\mathcal P(y,\vartheta,w)=0,\qquad
\Psi(y,\vartheta,w)=m,\qquad k,n,\ell,m\in L .
\end{gathered}
\tag{4}
\]
Here \(\deg f\le2\) and \(\deg g_3\le3\).
To avoid confusing the original invariant ring \(A\) with a
coefficient, write
\[
C=L[y,\vartheta]\subset O=L[v]=C[w],\qquad
F=f_V(y,\vartheta)\in C.
\]
Both potential equations in (4) are needed:
\[
Rw=\ell-f(y,\vartheta)\in C,\qquad
Fw=m-g_3(y,\vartheta)+\ell_t y+\ell_\rho\vartheta\in C .
\tag{5}
\]

The extension \(C\subset O\) is finite integral. Indeed choose
a nonconstant \(p(v)\) among \(y,\vartheta\), of degree \(e\)
and leading coefficient \(p_e\in L^*\). The equation
\[
T^e+\frac{p_{e-1}}{p_e}T^{e-1}+\cdots+
\frac{p_0-p(v)}{p_e}=0\quad\text{at }T=v
\]
is monic over \(L[p(v)]\subset C\).
Consequently \(O=C[v]\) is finite over \(C\), and in particular
\(w\) satisfies a monic polynomial over \(C\).
This does not presume normality of \(C\).

## 3. The center polynomial and its squarefree case

Define a polynomial of degree at most two over the exact field:
\[
\begin{aligned}
q(V)&=f(r,V)-\ell\\
&=\frac{r_\rho}{2}V^2+(r_t r+n_\rho)V
  +\frac{k_{tt}}2r^2+n_t r-\ell .
\end{aligned}
\tag{6}
\]
Division in \(L[V][U]\) by the monic polynomial \(U-r\) gives
a polynomial \(D(U,V)\), of total degree at most one, such that
\[
f(U,V)-\ell=q(V)+(U-r)D(U,V).
\tag{7}
\]
The first potential and the explicit formula for \(f_V\) yield
\[
q(\vartheta)=R\{D(y,\vartheta)-w\},\qquad
q'(\vartheta)=F+r_tR .
\tag{8}
\]
The first identity is in \(O\). It does not place
\(q(\vartheta)\) in the ideal \(RC\) before \(w\in C\) is proved.

Suppose \(q\ne0\) and \(\gcd(q,q')=1\). This includes a nonzero
constant \(q\), as well as nonconstant squarefree polynomials.
Choose \(h,j\in L[V]\) with \(hq+jq'=1\).
After evaluation and (8), the identity has the form
\[
\begin{gathered}
1=i_0+i_1w,\qquad i_0,i_1\in I:=(R,F)C,\\
i_0=R\,h(\vartheta)D(y,\vartheta)
       +j(\vartheta)F+r_tR\,j(\vartheta),\qquad
i_1=-R\,h(\vartheta).
\end{gathered}
\tag{9}
\]
Here is an elementary integral contraction argument, avoiding
any inference from a unit ideal only after normalization.
Let \(w^s+b_{s-1}w^{s-1}+\cdots+b_0=0\) be a monic relation
over \(C\). Multiply it by \(i_1^s\) and substitute
\(i_1w=1-i_0\). Every resulting term belongs to \(C\), and
the equality holds there because \(C\subset O\) is injective.
Modulo \(I\), its leading term is one and all other terms are
zero. Therefore \(C/I=0\), so \(I=C\).
Write \(1=c_RR+c_FF\) with \(c_R,c_F\in C\). Equation (5) gives
\(w=c_R(Rw)+c_F(Fw)\in C\), which proves (3) in this case.
No inverse of \(R\) or \(F\) has been declared polynomial.

If \(q=0\) identically, (4) and (7) instead give
\[
R\{w-D(y,\vartheta)\}=0 .
\tag{10}
\]
The domain \(O\) and \(R\ne0\) imply \(w=D(y,\vartheta)\in C\).
Thus (3) also holds in this separate case.

## 4. The remaining repeated center is a vertex-free cone

Only a nonzero, nonsquarefree \(q\) remains. Characteristic zero
and \(\deg q\le2\) force
\[
q(V)=\kappa(V-\vartheta_0)^2,\qquad
\kappa=r_\rho/2\in L^*,\qquad
\vartheta_0=-\frac{r_t r+n_\rho}{r_\rho}\in L .
\tag{11}
\]
In particular the repeated root is in \(L\) itself; no extension
of the coefficient field is needed to complete the square.
Equations (7) and (11) put the first potential into the form
\[
\mathcal P=(r-U)\{W_0-D(U,V)\}
                  +\kappa(V-\vartheta_0)^2 .
\tag{12}
\]
This is precisely the form hypothesis of
[the vertex-free cone lemma175](split-vertex-free-quartic-cone-lemma-pass175-working.md),
not an extra assumption on this remaining branch.

For completeness, set
\[
P_c=R,\qquad Q_c=\vartheta-\vartheta_0,\qquad
S_c=-\{w-D(y,\vartheta)\}/\kappa .
\tag{13}
\]
Then \(P_cS_c=Q_c^2\), \(P_c\ne0\), and the formulas recover
\(y,\vartheta,w\) polynomially over \(L\). Hence
\(L[P_c,Q_c,S_c]=O\), and (2) gives
\(\deg P_c,\deg Q_c\le4\).

The actual determinant supplies the last necessary hypothesis,
that the cone vertex is avoided. Write \(B_1=f_U(y,\vartheta)-w\).
From (12), the evaluated formal gradient has components
\[
B_1=-\{w-D(y,\vartheta)\}-R D_U,\qquad
F=2\kappa Q_c-R D_V,\qquad R .
\tag{14}
\]
At any common zero of \(P_c,Q_c,S_c\) over an algebraic closure
of \(L\), all three components would vanish. The calibrated identity
\[
\left[
dy\wedge(R\,d\vartheta+B_1dt+F\,d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}=-a^3\in L^*
\tag{15}
\]
would then have a zero middle row, a contradiction. This evaluates
a polynomial coefficient identity after its derivatives have been
formed; it does not differentiate the alleged root.
Thus \((P_c,Q_c,S_c)O=O\).

All hypotheses of the cone lemma now hold. It gives
\[
L[P_c,Q_c]=L[v],\qquad\text{hence }L[y,\vartheta]=L[v].
\tag{16}
\]
Together with Section 3, this exhausts every polynomial \(q\)
of degree at most two and proves (3).

## 5. Exact scope of the completed projection argument

There is no remaining projection-normality assumption in the
actual split chart175. The first potential recovers \(w\)
off \(R=0\); the second and the finite integral extension handle
the squarefree center; the constant determinant and degree bound
handle the repeated center. The identically zero center is included.
The formal nodal example in the cone note explains why a
birational field equality and degree bound alone were insufficient.

The conclusion is over \(L\), not automatically over
\(\mathbb C\) or the unlocalized invariant ring \(A\).
No polynomial automorphism carrying \(G\) to a variable,
global invariant coordinate, or three-good original frame is
constructed here. The selected extra factor of the quartic
eliminant is not newly proved to be a unit. Split-case recognition,
other initial profiles, and unrestricted cancellation remain open.

The complete current chart, zero-R, quartic and cone notes were
read for this proof. The contraction argument is written above,
and the cone note gives its own elementary proof and exact-field
descent. No new external theorem is invoked. Separate symbolic
controls can check finite identities but not the universal
integrality, degree-case exhaustion, or original-ring recognition.
No historical novelty, human expert review or proof-assistant
certification is claimed. No frozen174 or earlier file was changed.
