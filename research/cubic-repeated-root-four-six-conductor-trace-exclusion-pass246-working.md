# The quartic first and sextic second projections are impossible

In the supplied actual chart \(q=\rho^2-t^3\), the projected degree
pair \((4,6)\) cannot occur. A trace-dual computation identifies the
conductor exactly. Its degree bound forces a particular polynomial
approximation at infinity, and the missing linear centered coefficient
then contradicts birationality.

The proof is over the exact characteristic-zero coefficient field.
The changes of projected parameters and formal plane variables below
are not asserted to lift to original polynomial coordinates.

## 1. Actual input and the scalar cofactor

Assume the globally sliced exact1122 frame of
[rebuilt237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md),
with entire supplied initial kernel
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=\mathscr A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0\tau,b_0\tau,e_0\tau^2,h_0\tau^2)\bigr)
 =(\mathsf X^2\mathsf Z-\mathsf W^2+\mathsf X\mathsf Y^3),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2 .
\end{gathered}                                                     \tag{1}
\]
The literal new \(Z\) pivot is rebuilt after the actual coordinate
interchange in237. Its coefficient field is
\(L=\operatorname{Frac}(\ker_{\mathscr A}N)\), with
\(\mathscr A_L=L[v]\), \(Nv=1\), and
\([L:\mathbb C(t,\rho)]<\infty\).
The independent ratios \(t,\rho\), projected entries, and whole-line
calibration satisfy
\[
\begin{gathered}
q=\rho^2-t^3,\quad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad J(X)=-a_0^3\in L^*,\\
\deg_vy=4,\qquad \deg_v\theta=6,\qquad
R=2\theta+k_\rho\ne0 .
\end{gathered}                                                     \tag{2}
\]
The degree pair in (2) is the branch to be excluded.

The complete potentials in
[centered239](radical-minus-polynomial-centered-eliminant-pass239-working.md)
give
\[
\begin{gathered}
\mathcal C=L[y,\theta]\subset\mathcal O=L[v],\qquad
\mathcal O=\mathcal C+\mathcal Cw,\quad
R\mathcal O\subset\mathcal C,\quad
\operatorname{Frac}\mathcal C=L(v),\\
\psi_0=\theta+k_\rho/2,\qquad \deg_v\psi_0=6,\qquad
R=2\psi_0,\\
\mathcal H_c(y,\psi_0)=0,\quad
\deg\mathcal H_c=6,\quad(\mathcal H_c)_6=U^6,\quad
[\zeta]\mathcal H_c(U,\zeta)=0 .
\end{gathered}                                                     \tag{3}
\]
The last equality is the entire coefficient polynomial of the linear
centered variable, not only a leading-form statement.
The polynomial \(\mathcal H_c\) is the full eliminant after
\(\zeta=V+k_\rho/2\), with every lower potential retained.

Birationality and the polynomial degrees imply that the irreducible
relation of \((y,\psi_0)\) has total degree six, as in
[frontier240](cubic-repeated-root-projection-frontier-pass240-working.md).
Consequently its cofactor in \(\mathcal H_c\) is a nonzero element
of \(L\). We may make the following exact-field normalizations.
Translate \(v\) to remove the cubic coefficient of \(y\); scale and
translate the formal first variable to make
\[
y=(x^2+A/2)^2+Bx,\qquad A,B\in L .
\tag{4}
\]
More explicitly, after the parameter translation a monic scalar
multiple of the old \(y\) has the form
\(x^4+Ax^2+Bx+C\). Subtracting \(C-A^2/4\) gives (4).
No root extraction is used. Scale \(\psi_0\) by its nonzero leading
coefficient to obtain a monic degree-six polynomial \(\psi\).
Do not translate \(\psi\).

These changes preserve \(\mathcal C,\mathcal O\), their common fraction
field and the conductor inclusion; the return polynomial becomes a
nonzero \(L\)-multiple of \(\psi\) and retains degree six. They also
preserve the vanishing of the linear coefficient of the centered
relation, because only a scaling of that formal variable is made.
For the normalized pair, therefore,
\[
\begin{gathered}
\mathcal C=L[y,\psi],\quad\mathcal O=L[x],\quad
L(y,\psi)=L(x),\quad \deg_xy=4,\quad\deg_x\psi=6,\\
R\mathcal O\subset\mathcal C,\quad\deg_xR=6,\qquad
G(U,\zeta)=\zeta^4-e_1(U)\zeta^3+e_2(U)\zeta^2-e_3(U)\zeta+e_4(U),\\
G(y,\psi)=0,\qquad e_3(U)=0 .
\end{gathered}                                                     \tag{5}
\]
Here \(G\) is the monic minimal polynomial of \(\psi\) over \(L(y)\).
It belongs to \(L[U,\zeta]\), since multiplication by \(\psi\) on
the free module \(L[x]\) over \(L[y]\) has a polynomial
characteristic matrix. The fraction-field equality makes its degree
four and makes that characteristic polynomial equal to its minimum.
Gauss's lemma identifies it with the plane relation. Thus the scalar
cofactor conclusion from (3) indeed gives the final equality in (5).

## 2. An exact conductor formula from trace duality

Set \(S=L[y]\), \(K=L(y)\), and \(F=L(x)\).
Both \(\mathcal O=S[x]\) and \(\mathcal C=S[\psi]\) are free
rank-four \(S\)-modules, with bases \(1,x,x^2,x^3\) and
\(1,\psi,\psi^2,\psi^3\), respectively.
For \(\mathcal O\), the monic relation \(y(x)-y=0\) spans the module,
and distinct degrees modulo four prove independence.
For \(\mathcal C\), its monic degree-four minimum supplies both facts.
Define the trace dual of a full free module \(M\subset F\) by
\[
M^\vee=\{z\in F:\operatorname{Tr}_{F/K}(zM)\subset S\}.
\tag{6}
\]

We spell out the monogenic dual computation. If \(F_0(T)\in S[T]\)
is monic, separable over \(K\), of degree \(n\), and \(\alpha\)
generates its degree-\(n\) field extension, then
\[
\operatorname{Tr}\left(\frac{\alpha^j}{F_0'(\alpha)}\right)
 =\begin{cases}0&0\le j<n-1,\\1&j=n-1.\end{cases}
\tag{7}
\]
This follows by splitting \(F_0\) over an algebraic closure of \(K\)
and comparing the coefficient of \(T^{n-1}\) in the Lagrange
interpolation formula for \(T^j\).
For larger \(j\), first reduce \(T^j\) by the monic polynomial
\(F_0\), leaving coefficients in \(S\).
Thus the trace-pairing matrix between
\(\alpha^i\) and \(\alpha^j/F_0'(\alpha)\), for
\(0\le i,j<n\), is zero when \(i+j<n-1\), one when \(i+j=n-1\),
and has entries in \(S\) everywhere. Its determinant is a unit.
This proves the equality of trace-dual modules, not just an inclusion:
\[
\mathcal O^\vee=\frac1{y_x}\mathcal O,\qquad
\mathcal C^\vee=\frac1{G_\zeta(y,\psi)}\mathcal C .
\tag{8}
\]
The derivatives in (8) are polynomial derivatives with coefficients
fixed. Separability follows from characteristic zero.

The inclusion \(\mathcal C\subset\mathcal O\) reverses under duality.
By (8), it implies
\[
f\mathcal O\subset\mathcal C,\qquad
f:=\frac{G_\zeta(y,\psi)}{y_x}\in\mathcal O .
\tag{9}
\]
In particular \(f\) is an actual polynomial in \(x\), not merely
a quotient in \(F\). Double trace duality is exact for these free
modules, so for \(b\in\mathcal O\) we have
\[
\begin{aligned}
b\mathcal O\subset\mathcal C
&\iff b\mathcal C^\vee\subset\mathcal O^\vee\\
&\iff (b/f)\mathcal C\subset\mathcal O
 \iff b/f\in\mathcal O .
\end{aligned}
\]
The last equivalence uses \(1\in\mathcal C\subset\mathcal O\).
Combining this with (9) gives the exact conductor formula
\[
\boxed{(\mathcal C:\mathcal O)=
       \frac{G_\zeta(y,\psi)}{y_x}\,\mathcal O.}
\tag{10}
\]
All nonzero factors here are in the same field \(F\).

Since \(R\mathcal O\subset\mathcal C\), equation (10) gives
\(R=fh\) for a polynomial \(h\in L[x]\).
Now \(\deg_xR=6\) and \(\deg_xy_x=3\), hence
\[
\boxed{\deg_x G_\zeta(y,\psi)\le9.}
\tag{11}
\]
This is where the actual conductor input is used.

## 3. What the bound forces at the unique polynomial infinity

There is a unique formal Laurent series \(x(z)\in L((z^{-1}))\)
with leading term \(z\) and
\[
y(x(z))=z^4 .
\tag{12}
\]
For a direct construction put \(x=z\,h(z^{-1})\).
The resulting formal equation has \(h(0)=1\) and derivative
four with respect to \(h\) at that point. Its coefficients can
therefore be solved recursively in \(L\).
The four roots of \(y(T)=z^4\) are
\(x(z),x(iz),x(-z),x(-iz)\). They are distinct by their leading
terms, and \(i\in\mathbb C\subset L\).

For a nonzero Laurent series let its pole degree denote its greatest
exponent of \(z\). Substitution \(x=x(z)\) preserves the degree of
every nonzero polynomial in \(x\).
Because \(\psi\) is monic of degree six, its differences against
the two branches \(x(iz),x(-iz)\) each have pole degree six.
The derivative of its minimal polynomial is the product of all
three conjugate differences:
\[
G_\zeta(y(x(z)),\psi(x(z)))
 =\prod_{\omega\in\{i,-1,-i\}}
       \{\psi(x(z))-\psi(x(\omega z))\}.
\tag{13}
\]
Birationality in (5) makes these conjugates distinct, so none of
the factors is zero. Equations (11)--(13) therefore imply
\[
\psi(x(z))-\psi(x(-z))=O(z^{-3}).
\tag{14}
\]
This uses formal Laurent series only, not an analytic asymptotic
assertion.

For \(0\le j\le6\), let \(P_j(x)\) be the polynomial part of the
formal expansion \(y(x)^{j/4}\) with leading term \(x^j\).
Each \(P_j\) is monic of degree \(j\); they are a triangular
\(L\)-basis for the polynomials of degree at most six. Also
\[
P_j(x(z))=z^j+O(z^{-1}).
\tag{15}
\]
Expand the monic polynomial \(\psi\) in this basis.
The absence of the positive odd powers \(z^5,z^3,z\) in (14)
forces precisely their three basis coefficients to vanish:
\[
\psi=P_6+dP_4+sP_2+e,\qquad d,s,e\in L .
\tag{16}
\]

For a general monic quartic
\(x^4+Ax^2+Bx+C\), binomial expansion gives
\[
[x^{-1}]y^{3/2}=\frac{3B(4C-A^2)}{16},\qquad
[x^{-1}]y^{1/2}=B/2.
\tag{17}
\]
The normalization (4) is exactly \(C=A^2/4\).
Thus the coefficient of \(z^{-1}\) in \(P_6(x(z))-z^6\)
is zero, while in \(P_2(x(z))-z^2\) it is \(-B/2\).
Terms of order \(x^{-2}\) or lower cannot contribute to
\(z^{-1}\), since \(x(z)\) has leading term \(z\).
Moreover \(P_4=y\) exactly.
The remaining forbidden odd term in (14) consequently gives
\[
sB=0 .
\tag{18}
\]

Write \(H_0=x^2+A/2\). The polynomial parts are explicit:
\[
P_2=H_0,\quad P_4=y,\quad
P_6=H_0^3+\frac{3B}{2}xH_0+\frac{3B^2}{8}.
\tag{19}
\]
If \(B=0\), equations (16) and (19) make both \(y\) and \(\psi\)
even polynomials in \(x\), contrary to \(L(y,\psi)=L(x)\).
Hence \(B\ne0\), and (18) forces \(s=0\). We have proved, over
the exact field \(L\), the required normal form
\[
\boxed{\psi=\Phi+d\,y+e,\quad
\Phi=H_0^3+\frac{3B}{2}xH_0+\frac{3B^2}{8},\quad B\ne0.}
\tag{20}
\]
Only projected and formal changes were used to derive it.

## 4. The missing centered coefficient contradicts this normal form

Compute traces over \(L(y)\), writing \(U\) for \(y\).
In the basis \(1,x,x^2,x^3\), multiplication by \(x\) is
\[
M=
\begin{pmatrix}
0&0&0&U-A^2/4\\
1&0&0&-B\\
0&1&0&-A\\
0&0&1&0
\end{pmatrix}.
\tag{21}
\]
Let \(I\) be the identity matrix and \(H_M=M^2+(A/2)I\).
The multiplication matrix for \(\Phi\) is the explicit polynomial
\[
M_\Phi=H_M^3+\frac{3B}{2}M H_M+\frac{3B^2}{8}I .
\]
Multiplication using \(M^4+AM^2+BM+(A^2/4-U)I=0\) gives
\[
\begin{gathered}
\operatorname{Tr}\Phi=0,\\
T(U):=\operatorname{Tr}(\Phi^2)
       =4U^3+\frac{3AB^2}{2}U+\frac{3B^4}{16},\\
\operatorname{Tr}(\Phi^3)=\frac{3B^6}{64}.
\end{gathered}                                                     \tag{22}
\]
Equations (21)--(22) are finite polynomial matrix identities and
give every trace needed below.

Put \(h=dU+e\). Then \(\psi=\Phi+h\), so
\[
\operatorname{Tr}\psi=4h,\quad
\operatorname{Tr}(\psi^2)=T+4h^2,\quad
\operatorname{Tr}(\psi^3)=3B^6/64+3hT+4h^3 .
\]
The third elementary coefficient of the monic degree-four minimum
is therefore, by the exact Newton identity,
\[
\begin{aligned}
e_3(U)
&=\frac{(\operatorname{Tr}\psi)^3
       -3\operatorname{Tr}\psi\,\operatorname{Tr}(\psi^2)
       +2\operatorname{Tr}(\psi^3)}6\\
&=\boxed{4(dU+e)^3-(dU+e)
       \left(4U^3+\frac{3AB^2}{2}U+\frac{3B^4}{16}\right)
                                   +\frac{B^6}{64}.}
\end{aligned}                                                     \tag{23}
\]
In particular its coefficient of \(U^4\) is \(-4d\), and
its coefficient of \(U^3\) is \(4(d^3-e)\).
But (5) requires \(e_3(U)=0\). These two coefficients first
give \(d=0\) and then \(e=0\); the remaining constant in (23)
is \(B^6/64\ne0\). This is the desired contradiction.

## 5. Scope and verification boundary

The argument excludes \((4,6)\) in the supplied cubic repeated-root
chart. It uses the actual whole-line conductor and the complete
centered eliminant, not merely a freely chosen pair of polynomials.
The trace-dual derivation, formal-series recursion and trace matrices
are written explicitly; no rationality assumption on \(L\), genus
formula or unproved lifting of a coefficient-field coordinate is used.

This source does not itself classify every possible initial kernel
or provide arbitrary-frame entry. Other projected branches require
their separate proofs. Unrestricted cancellation, historical novelty,
proof-assistant certification and human expert review are not claimed.

The complete relevant centered and frontier sources were read before
this argument. A separate fresh unsaved matrix calculation reconstructed
(22)--(23), but those identities are also specified by the literal
matrix (21). No saved checker was executed, imported or compiled.
No earlier proof, index or packet was edited.
