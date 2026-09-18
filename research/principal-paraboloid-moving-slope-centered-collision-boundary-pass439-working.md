# Centered collisions with a moving transverse slope

Working necessary reduction: in the supplied full actual264 chart,
let \(k=s+f\), \(f_s=0\), and
\(n=\nu s+n_0\), where \(\nu,n_0\) are killed by
\(\partial_s\) and \(\nu'\ne0\).
For nonconstant \(\sigma\), the full third potential has a
polynomial centering which preserves all three line generators.
The actual all-\(X\) polynomial-ring return then gives a useful
one-parameter family of three-generator identities.

The exact collision equations have an exceptional average
coefficient which cannot be divided away. A formal example
satisfies both the centered surface relation and the entire
one-parameter generation condition, while its proposed two-generator
plane ring is proper. These ingredients alone therefore do not
give plane return or an exclusion.

No original-coordinate recognition or realization is asserted.
The finite birational normalization statement at the end is
conditional on birationality; the separate fourth-potential
exclusion of the degree-two alternative is not proved here.

## 1. Actual hypotheses and exact coefficient derivatives

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad Na_0=Nt=Ns=0,\\
O=L[A]=L[v],\qquad Nv=1,\qquad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
L[y,z,w]=L[y,\sigma,\theta]=O,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
       =-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
The coefficient partials extend to \(L\), commute, and fix \(v\).
Let \(\mathbb F=\ker_L\partial_s\), the exact finite extension
of \(\mathbb C(t)\). Assume
\[
k=s+f,\qquad
n=\nu s+n_0,\qquad f,\nu,n_0\in\mathbb F,\qquad
b:=\nu'\ne0,\qquad \sigma\notin L.
\tag{2}
\]
A prime denotes the exact \(t\)-derivative in \(\mathbb F\),
not differentiation in an assumed rational parametrization.
In particular,
\[
n_t=\nu's+n_0',\qquad
n_{tt}=\nu''s+n_0'',\qquad n_{ts}=\nu',\qquad n_{ss}=0 .
\tag{3}
\]
Neither \(n_t\) nor \(n_{tt}\) is silently made \(s\)-constant.
We impose no zero or nonzero condition on \(f'''\) or on
\(\ell_s+\nu^2\).

The full literal rows and first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n_t\sigma-\nu\theta .
\end{aligned}
\tag{4}
\]
The genuine higher potentials and full calibration remain
restrictions on any actual candidate. The calculations below
do not replace them by a freely chosen formal surface.

## 2. Complete third potential and the nonunit obstruction

Use formal independent variables \(U,P,V\), and set
\[
\begin{gathered}
\alpha=f''-2\nu,\qquad \beta=n_t-\nu f',\qquad
c=n_{tt}-\nu f'',\qquad d=\nu n_t+\ell_t,\\
\epsilon=\ell_s+\nu^2,\qquad D(P)=bP-\epsilon .
\end{gathered}
\tag{5}
\]
The symbol \(\epsilon\) is not the derivation \(E\), and can vanish.
The raw264 Taylor formula gives exactly
\[
\boxed{
H=U^2+(\alpha P+\beta)U+
       \frac{f'''}6P^3+\frac c2P^2-dP+\nu\ell+D(P)V,
\qquad H(y,\sigma,\theta)=h\in L .
}
\tag{6}
\]
Indeed in264's notation
\[
F=\frac{f''}{2}P^2+n_tP+\nu V,\qquad
g=\ell-(2P+f')U-F,
\]
and
\(H=U^2+F_PU+F_Vg+H_3(k)+H_2(n)-\ell_tP-\ell_sV\).
Here \(H_3(k)=f'''P^3/6\) and
\(H_2(n)=n_{tt}P^2/2+\nu'PV\).
These terms give(6) without omitting any mixed derivative.
For reference its three formal gradients are
\[
\begin{aligned}
H_U&=2U+\alpha P+\beta,\\
H_P&=\alpha U+\frac{f'''}2P^2+cP-d+bV,\\
H_V&=bP-\epsilon .
\end{aligned}
\tag{7}
\]

Since \(b\ne0\) and \(\sigma\) is nonconstant in \(L[v]\),
\(D(\sigma)\) is a nonzero nonunit of \(O\).
Solving(6) for \(\theta\) places it in \(L(y,\sigma)\),
but does not place it in \(L[y,\sigma]\).
Polynomiality of this quotient in the larger ring \(O\) does
not repair that missing inclusion.
If the constant-\(\sigma\) boundary were considered instead,
one would have to separate \(D(\sigma)\ne0\) from
\(D(\sigma)=0\); this note does not divide in that latter case.

## 3. A polynomial centering retaining all three generators

Define, only over the coefficient field,
\[
x=y+\frac{\alpha\sigma+\beta}{2},\qquad
\zeta=\theta+\sigma^2+f'\sigma .
\tag{8}
\]
The inverse substitutions are polynomial over \(L\):
\[
y=x-\frac{\alpha\sigma+\beta}{2},\qquad
\theta=\zeta-\sigma^2-f'\sigma.
\]
Thus
\[
O=L[x,\sigma,\zeta].
\tag{9}
\]
This is not a two-generator return and is not an actual
polynomial automorphism of the original four-ring.

Substituting(8) in(6) gives the exact centered relation
\[
\boxed{x^2+(b\sigma-\epsilon)\zeta+\mathcal R(\sigma)=0,}
\tag{10}
\]
where the complete polynomial, including its constant term, is
\[
\begin{aligned}
\mathcal R(P)={}&
\left(\frac{f'''}6-b\right)P^3\\
&+\left(\frac c2-\frac{\alpha^2}{4}+\epsilon-bf'\right)P^2\\
&+\left(-d-\frac{\alpha\beta}{2}+\epsilon f'\right)P
 +\nu\ell-h-\frac{\beta^2}{4}.
\end{aligned}
\tag{11}
\]
The degree can drop when \(f'''=6b\), and no leading coefficient
in(11) is inverted. No derivative of a moving line parameter
is used to obtain this identity.

## 4. The exact all-T polynomial-ring return

The original slice gives \(X=a_0u+x_0\), with \(x_0\in A\) and
\(a_0\in L^*\). Hence
\[
L[\mathcal B]=O[u]=L[v,X]=L[X,Y,Z,W].
\tag{12}
\]
The coefficient changes below are invertible over \(L[X]\).
Put \(T=X-\alpha/2\), and define
\[
\begin{aligned}
Y_c&=Y-tX^2+\beta/2,\\
Z_c&=Z-2tY-n-kX+t^2X^2,\\
W_c&=-W+(X-\nu)(Z-2tY)-f'Y+C_W(X),\\
C_W(X)&=\ell+(s+tf')X^2
               -(X-\nu)(n+kX-t^2X^2).
\end{aligned}
\tag{13}
\]
Direct substitution of all rows(4) gives
\[
\boxed{
Y_c=x+T\sigma,\qquad Z_c=\zeta,\qquad
W_c=2\sigma x+T\sigma^2 .
}
\tag{14}
\]
For completeness, a polynomial inverse to(13), with \(X\)
fixed, is
\[
\begin{aligned}
Y&=Y_c+tX^2-\beta/2,\\
Z&=Z_c+2tY+n+kX-t^2X^2,\\
W&=-W_c+(X-\nu)Z_c-f'Y_c
                         +\ell+sX^2+f'\beta/2 .
\end{aligned}
\tag{15}
\]
Both orders of composition are identities over \(L[X]\).
They license a coefficient-adjoined ring change, not an
ambient change with complex coefficients.

After any field extension \(M/L\), specialize
\(X=T_0+\alpha/2\) for an arbitrary \(T_0\in M\).
Equations(12)--(15) prove
\[
\boxed{
M[x+T_0\sigma,\ \zeta,\ 2\sigma x+T_0\sigma^2]=M[v]
\quad\text{for every }T_0\in M.
}
\tag{16}
\]
This is stronger than equality of fraction fields or generic
generation in \(T_0\). Specializing an element of \(M\) is
legitimate because the generated-polynomial-ring identity
holds before evaluation. No claim that \(\alpha/2\) is complex
or an original coordinate is made.

## 5. Complete collision identities and the exceptional factor

Work over any extension \(M/L\), and choose two values \(v_1,v_2\)
of the original line parameter. Write \(p_i=\sigma(v_i)\),
\(u_i=y(v_i)\), and \(\vartheta_i=\theta(v_i)\).
For distinct points assume \(p_1\ne p_2\), and put
\[
\Sigma=p_1+p_2,\quad \Pi=p_1p_2,\quad
L_1=\frac{u_1-u_2}{p_1-p_2},\qquad X_0=-L_1 .
\tag{17}
\]
Normalize all differences by \(p_1-p_2\), denoting them by
a superscript \([1]\). For repeated \(v_1=v_2=v_0\), the same
identities mean derivatives in \(v\) divided by
\(\sigma_v(v_0)\), provided \(\sigma_v(v_0)\ne0\).
Every derivative holds the chosen \(X_0\) fixed.
Pairs with equal sigma values, or repeated points at which
\(\sigma_v=0\), are not covered by this division and are not
silently discarded in an exhaustion claim.

Define
\[
\begin{aligned}
\mathcal F&=u_1+u_2+\frac{\alpha}{2}\Sigma+\beta
                         =x(v_1)+x(v_2),\\
\mathcal G&=\frac{f'''}6(\Sigma^2-\Pi)
 +\left(\frac c2-\frac{\alpha^2}{4}\right)\Sigma
 -d-\frac{\alpha\beta}{2}\\
&\quad-\left(\frac b2\Sigma-\epsilon\right)(\Sigma+f')
              +\frac b2(\vartheta_1+\vartheta_2).
\end{aligned}
\tag{18}
\]
The literal rows(4), at \(X=X_0\), give
\[
\begin{aligned}
Y^{[1]}&=0,\qquad
Z^{[1]}=\theta^{[1]}+\Sigma+f',\\
W^{[1]}-(X_0-\nu)Z^{[1]}&=-\mathcal F .
\end{aligned}
\tag{19}
\]
The full third-potential difference is
\[
\boxed{
0=(L_1+\alpha/2)\mathcal F+\mathcal G+
             (b\Sigma/2-\epsilon)Z^{[1]} .
}
\tag{20}
\]
To check(20) directly, the divided difference of
\(y^2+(\alpha\sigma+\beta)y\) is
\[
L_1\mathcal F+\frac{\alpha}{2}(u_1+u_2).
\]
The divided difference of \(D(\sigma)\theta\) is
\((b\Sigma/2-\epsilon)\theta^{[1]}
+b(\vartheta_1+\vartheta_2)/2\).
The remaining terms of(6) give the other summands in(18),(20).
The level \(h\) cancels because it is in \(L\).

Thus if \(\mathcal F=\mathcal G=0\) and
\(b\Sigma/2-\epsilon\ne0\), the remaining two coordinate
differences vanish.
If this average coefficient is zero, (20) alone gives no
information about \(Z^{[1]}\). The exceptional sum
\(\Sigma=2\epsilon/b\) must remain a separate case.

There is a direct formulation in the centered outputs which
does not divide by the exceptional average coefficient. For any pair
covered by(17), or its stated diagonal version, choosing
\(T_0=-x^{[1]}\) makes \(Y_c^{[1]}=0\), while
\[
Z_c^{[1]}=\zeta^{[1]},\qquad
W_c^{[1]}=x(v_1)+x(v_2)=\mathcal F .
\tag{21}
\]
Consequently the exact collision conditions in this region are
\(\mathcal F=0\) and \(\zeta^{[1]}=0\), not merely
\(\mathcal F=\mathcal G=0\) at the exceptional sum.
For distinct points they contradict injectivity forced by(16);
for repeated points they make every generator derivative zero
and contradict the derivative of \(v\) being one.
Equation(21) is a criterion for such a forbidden pair, not a
proof that a pair exists.

## 6. A formal example marking the limit of these inputs

Let \(M\) be a characteristic-zero field and let \(v\) be
transcendental. Set
\[
\sigma=v^2,\qquad x=v^3+1,\qquad \zeta=v .
\tag{22}
\]
These polynomials satisfy a relation of the exact shape(10):
\[
x^2-2\sigma\zeta-\sigma^3-1=0.
\tag{23}
\]
Here \(b=-2\ne0\), \(\epsilon=0\), and
\(\mathcal R(P)=-P^3-1\).
For every \(T_0\), over every coefficient extension, the middle
generator \(\zeta=v\) already proves the entire generation
identity(16).

Nevertheless
\[
M[x,\sigma]=M[v^3,v^2]\ne M[v].
\tag{24}
\]
For example every polynomial in \(v^2,v^3\) has zero derivative
at zero, while \(v\) has derivative one there.
Their fraction fields are equal, so this is exactly a
polynomial-ring obstruction, not a transcendence-degree issue.
The factor \(D(\sigma)=-2v^2\) in(23) is a nonunit.

More generally, choosing arbitrary coefficient values
\(\alpha,\beta,\varphi\in M\) and setting
\[
y=x-\frac{\alpha\sigma+\beta}{2},\qquad
\theta=\zeta-\sigma^2-\varphi\sigma
\]
does not change the proper equality
\(M[y,\sigma]=M[x,\sigma]\ne M[v]\).
The projection ring \(M[\sigma,\theta]\), in contrast, is the
whole \(M[v]\), since it recovers \(\zeta\).

This is only an example for the centered algebraic relation and
the all-parameter generation property. No original four-ring,
global slice, commuting coefficient derivatives, actual
calibration or genuine fourth potential has been constructed.
In particular the displayed coefficient values are not asserted
to solve all differential compatibilities implicit in(2)--(6).
The example cannot be used as an actual264 realization or as a
counterexample to a conclusion using those additional hypotheses.
It shows why these two algebraic ingredients alone are insufficient.

## 7. The finite projection and the remaining birational boundary

Independently of this example, return to the actual hypotheses.
Let \(\mathscr P=L[\sigma,\theta]\). Since \(\sigma\) is
nonconstant, \(\mathscr P\) has fraction field of transcendence
degree one over \(L\). The monic equation(6) makes \(y\)
integral of degree at most two over \(\mathscr P\). Therefore
\[
O=\mathscr P[y]\text{ is finite over }\mathscr P,\qquad
[L(v):\operatorname{Frac}\mathscr P]\in\{1,2\}.
\tag{25}
\]
This finite-degree assertion does not require division by \(D\).

Conditional on the degree being one, \(O=L[v]\) is exactly
the finite normalization of \(\mathscr P\) in its fraction field:
it is integral over \(\mathscr P\), has the same fraction field,
and is integrally closed. Conversely any element integral over
\(\mathscr P\) is integral over \(O\), hence lies in \(O\).
There is still no conclusion \(\mathscr P=O\).
Neither does this imply \(L[y,\sigma]=O\).

An exclusion of the degree-two alternative by the full
fourth-potential cofactor is a separate argument, not supplied
by(10) or(16). After such an exclusion, the remaining
problem is precisely the finite birational projection, together
with the genuine higher potential and full scalar conditions.
This note neither removes its possible nonnormality nor produces
an original invariant coordinate.

The raw third potential and all its formal gradients were checked
in fresh unsaved \(f8cf0a\), with all \(s\)-dependent terms retained.
Fresh \(60c9b6\) reconstructed(10),(11),(14),(19),(20) from the
full original rows. Both orders of the coefficient-field inverse
(13),(15) were independently checked in \(32adab\).
The formal example was checked in \(f6cf57\).
All reported residuals were zero.
These exact calculations supplement, rather than replace, the
written field, whole-ring and exceptional-factor arguments.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited.
No unrestricted cancellation, arbitrary-entry, actual-existence,
historical novelty or formal-certification claim is made.
