# Equal quadratic intrinsic degrees contradict the full all-X return

Working exclusion: in the full actual moving-slope chart349, the
normalized intrinsic profile \((\deg p,\deg x,\deg q)=(2,2,2)\)
cannot occur. The proof uses the literal polynomial map and its full
all-X ring equality. A quadratic equation selects a coefficient-field
specialization where the generators either identify two distinct
points or all have zero derivative at one point.

No coefficient differential equation, primitive derivation theorem,
or ambient normalization is required. In particular the resonance
identities for this pattern in354 need not be assumed separately.
The result does not recognize the remaining affine-sigma families.

## 1. Actual hypotheses and quadric coordinates

Retain the full hypotheses of
[349](principal-paraboloid-variable-intercept-slope-quadric-reduction-pass349-working.md)
and its literal264 chart:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v]=L[y,\sigma,\theta],\quad Nv=1,\\
K=L(v)=\mathbb C(y,z,w),\quad J(X)=-a_0^4\in L^*,\\
k=s,\quad n=Bs+f,\quad B,f\in F=\ker_L\partial_s,
\quad b=B'\ne0.
\end{gathered}
\tag{1}
\]
The exact finite coefficient field and the selected literal partial are
unchanged. All coefficient derivatives have their retained meanings.

Write \(u_1=n_t\), \(A_2=n_{tt}/2-B^2\),
\(C_2=\ell_s+B^2\), \(T=\ell_t\), and use349's affine changes over L:
\[
\begin{aligned}
x&=y+u_1/2-B\sigma,\qquad p=\sigma-C_2/b,\\
q&=\theta+(A_2/b)\sigma+A_2C_2/b^2-T/b.
\end{aligned}
\qquad
x^2+bpq=d_0\in L,\quad O=L[x,p,q].
\tag{2}
\]
These are formal coefficient-field changes only. Assume for contradiction
\[
\deg_vp=\deg_vx=\deg_vq=2.
\tag{3}
\]
This is exactly the equal quadratic case isolated in
[354](principal-paraboloid-moving-slope-intrinsic-degree-patterns-pass354-working.md).

## 2. The whole-line quadratic form without adjoining square roots

A translation of the polynomial parameter v removes the linear term
of p. Thus for some \(\alpha\in L^*\), \(\delta_0\in L\), and affine
parameter \(\xi\) with \(O=L[\xi]\), write
\[
p=\alpha(\xi^2-\delta_0),\qquad
x=\lambda p+\varepsilon\xi+e_0,
\qquad\lambda\in L^*.
\tag{4}
\]
Only translation is needed; neither \(\alpha\) nor \(\delta_0\) needs
a square root. The coefficient \(\lambda\) is nonzero by (3).

The coefficient \(\varepsilon\) cannot vanish. If it did, x and p
would be even in \(\xi\), and the identity
\(q=(d_0-x^2)/(bp)\), already polynomial, would make q even too.
This contradicts \(L[x,p,q]=L[\xi]\). Reducing
\(d_0-x^2\) modulo p gives the remainder
\(d_0-\varepsilon^2\delta_0-e_0^2-2\varepsilon e_0\xi\).
Since p divides that polynomial, \(\varepsilon\ne0\) forces
\[
e_0=0,\qquad d_0=\delta_0\varepsilon^2,
\qquad
q=-\frac{\lambda^2}{b}p-\frac{2\lambda\varepsilon}{b}\xi
       -\frac{\varepsilon^2}{\alpha b}.
\tag{5}
\]
This includes \(\delta_0=0\). Conversely the parameter is recovered
polynomially as \(\xi=(x-\lambda p)/\varepsilon\).

Put \(\sigma_0=C_2/b-\alpha\delta_0\). In terms of the original
intercepts, (2),(5) give the exact expressions
\[
\begin{aligned}
\sigma&=\alpha\xi^2+\sigma_0,\\
y&=j\sigma+\varepsilon\xi+k_0,\qquad j=\lambda+B,
       \quad k_0=-u_1/2-\lambda C_2/b,\\
\theta&=r\sigma+d_1\xi+e_1,\\
r&=-(\lambda^2+A_2)/b,\qquad d_1=-2\lambda\varepsilon/b,\\
e_1&=(\lambda^2-A_2)C_2/b^2+T/b-\varepsilon^2/(\alpha b).
\end{aligned}
\tag{6}
\]
In particular \(\alpha,\varepsilon,\lambda,b\) are all nonzero.
No restriction on \(r,j,k_0,e_1\) is imposed or needed.

## 3. The full polynomial ring survives every X specialization

The full literal map is
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+\theta+n+(2t\sigma+s)X+t^2X^2,\\
W&=\ell-2\sigma y-u_1\sigma-B\theta+\theta X+sX^2.
\end{aligned}
\tag{7}
\]
It gives the inclusion \(L[\mathcal B]\subset L[X,\xi]\).
Conversely E preserves \(L[\mathcal B]\), kills L, and a0 belongs to
\(L^*\). Therefore
\[
\sigma=EY/a_0-2tX,\qquad \theta=EW/a_0-2sX
\tag{8}
\]
belong to \(L[\mathcal B]\); so do y, x, p and then \(\xi\) by (5).
Consequently
\[
L[X,Y,Z,W]=L[X,\xi].
\tag{9}
\]
Extend coefficients to an algebraic closure \(\Omega\) of L. For every
\(X_0\in\Omega\), quotienting by \(X-X_0\) gives
\[
\Omega[Y_{X_0}(\xi),Z_{X_0}(\xi),W_{X_0}(\xi)]=\Omega[\xi].
\tag{10}
\]
This is a consequence of equality (9), not an assumption about
generators of a projected subring. Such a coefficient-field
specialization is not presented as an ambient complex-coordinate map.

## 4. Exact two-point divided differences

For a fixed value of X, set \(R=X+j\). Assume temporarily \(R\ne0\).
Let \(\xi_1,\xi_2\in\Omega\) be two possibly equal parameters, and put
\[
S=\xi_1+\xi_2,\qquad H_\sigma=\sigma(\xi_1)+\sigma(\xi_2).
\tag{11}
\]
For any polynomial in \(\xi\), its divided difference is the
polynomial \((F(\xi_1)-F(\xi_2))/(\xi_1-\xi_2)\). It remains defined
when the two parameters agree, where it is the derivative.

Since \(Y=R\sigma+\varepsilon\xi+k_0+tX^2\), its divided difference
vanishes when
\[
S=-\frac{\varepsilon}{\alpha R}.
\tag{12}
\]
Under (12), the divided difference of \(\sigma\) is \(-\varepsilon/R\).
Expanding Z in (7) by (6), its divided difference is then
\[
d_1-\frac{\varepsilon}{R}(H_\sigma+r).
\tag{13}
\]
Thus the first two divided differences vanish if, in addition,
\[
H_\sigma=d_1R/\varepsilon-r.
\tag{14}
\]

The product term in W obeys
\[
\frac{\sigma(\xi_1)\xi_1-\sigma(\xi_2)\xi_2}{\xi_1-\xi_2}
=\frac{H_\sigma+\alpha S^2}{2}.
\tag{15}
\]
Use this identity and (12),(14) in the literal W expression. Its
divided difference simplifies, with all t-terms already cancelled, to
\[
\lambda d_1+
 \frac{\varepsilon(2k_0+u_1-\lambda r)}{R}
 -\frac{\varepsilon^3}{\alpha R^2}
=\frac{\varepsilon}{R^2}\,\mathcal F(R),
\tag{16}
\]
where (6) gives the exact polynomial
\[
\boxed{\mathcal F(R)=
-\frac{2\lambda^2}{b}R^2
+\frac{\lambda(\lambda^2+A_2-2C_2)}{b}R
-\frac{\varepsilon^2}{\alpha}.}
\tag{17}
\]
For example the first equality of (16) follows by expanding
\(W=-2j\sigma^2-2\varepsilon\sigma\xi+
\{(X-B)r-2k_0-u_1\}\sigma+(X-B)d_1\xi+\text{constant}\).
It uses \(j-B=\lambda\). Neither a coefficient derivative nor an
intrinsic derivative is substituted for a divided difference here.

## 5. Both the collision and repeated-point boundaries contradict (10)

The leading and constant coefficients of \(\mathcal F\) are
\(-2\lambda^2/b\ne0\) and \(-\varepsilon^2/\alpha\ne0\).
Hence it has a root \(R_0\in\Omega^*\). Put \(X_0=R_0-j\), and
prescribe S and \(H_\sigma\) by (12),(14) at \(R_0\).
Choose \(\xi_1,\xi_2\) as the roots of
\[
z^2-Sz+P_0=0,\qquad
P_0=\frac12\left(S^2-\frac{H_\sigma-2\sigma_0}{\alpha}\right).
\tag{18}
\]
These roots always exist in \(\Omega\), and satisfy (11), since
\(\sigma=\alpha\xi^2+\sigma_0\). Thus all three divided differences
of the specialized Y,Z,W vanish by (12)--(17).

If \(\xi_1\ne\xi_2\), the three generators take identical values at
two distinct points. Every polynomial in them does too, contrary to
the membership of \(\xi\) in the generated ring (10).

If \(\xi_1=\xi_2\), all three generator derivatives vanish at that
point. The chain rule then makes the derivative of every polynomial in
them vanish there. This again contradicts (10), since \(d\xi/d\xi=1\).
The repeated-root case is therefore not lost by division by a parameter
difference. A repeated root of \(\mathcal F\) itself causes no problem
either; only one nonzero root \(R_0\) was needed.

These contradictions exclude (3), including the zero-level quadric
boundary \(d_0=0\). The proof does not divide by \(d_0,r,j,b'\), or
any coefficient not explicitly known to be nonzero.

## 6. Scope and verification

This is an exclusion of the equal quadratic normalized profile in the
supplied actual chart. It complements the other degree-pattern analyses
but does not alone compose them into a full moving-slope recognition
claim. In particular no existence or recognition of the remaining
affine-sigma coefficient families is inferred.

The complete354 source was freshly read, with the complete349,264,296
inputs already read. Fresh unsaved symbolic reconstruction checked the
quadric form, recovery of \(\xi\), and all three literal divided
differences in (12)--(17); all residuals were zero. The repeated-point
and full-ring arguments are given above rather than inferred from a
finite test. No saved checker was executed, imported, compiled or
rerun, no earlier source or canonical record was edited, and no
unrestricted cancellation or novelty claim is made.
