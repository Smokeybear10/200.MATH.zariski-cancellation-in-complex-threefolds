# Differential and divided-difference obstructions for all specializations

Working result: in the actual coupled chart of264, the all-X polynomial
return of325 gives an exact unit ideal of v-derivatives. Its useful
univariate consequence is
\[
\gcd(S_v,H_U(y,\sigma,\theta))
 =\gcd(\sigma_v,\theta_v),
\qquad S=\sigma^2+k_t\sigma+m\theta,
\tag{1}
\]
where both gcds are monic and the polynomial on the right is squarefree.
This includes the possible failure of immersion of the projected plane
curve. An unsaturated assertion that the left-hand gcd is always one
would be false.

The same algebra has a finite divided-difference version, including
off-diagonal pairs. A formal family from290 has an explicit all-X
polynomial inverse and arbitrarily large intrinsic degrees, while
failing the full calibrated Jacobian. Thus neither all-X embedding
nor these differential tests alone supplies a uniform degree bound or
recognition theorem.

## 1. Retained actual inputs and derivative conventions

Retain the complete actual nonzero-coupling hypotheses of the fully
read [264](principal-one-affine-paraboloid-chart-pass264-working.md)
and [325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular L is the exact coefficient field, m=k_s belongs to L*,
and
\[
\begin{gathered}
O=L[v]=L[y,\sigma,\theta],\qquad
L[X,Y,Z,W]=L[X,v],\\
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2,\\
z=2ty+\sigma^2+k_t\sigma+m\theta+n,\qquad
mw=\ell-(2\sigma+k_t)y-F(\sigma,\theta).
\end{gathered}
\tag{2}
\]
Here all intercept functions belong to O, and k,n,ell,t,s belong to L.
The full actual calibrated determinant remains J(X)=-a^4 in L*.
That assumption is not being replaced by the conditions proved below.

The quadratic polynomial and the monic surface relation are
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+m_tPV+\frac{m_s}2V^2+n_tP+n_sV,\\
H(U,P,V)-h_0&=U^2+A_1(P,V)U+A_0(P,V),\\
A_1&=F_P-\frac{(2P+k_t)F_V}{m},\qquad
H(y,\sigma,\theta)=h_0\in L.
\end{aligned}
\tag{3}
\]
The degree bounds for A1,A0 are not needed for (1).
All v-derivatives in this note kill L and hold X fixed. Formal
U,P,V partials are taken before evaluation. Define in O
\[
\gamma=2\sigma+k_t,\quad
\lambda=F_V(\sigma,\theta)/m,\quad
D=H_U(y,\sigma,\theta)
 =2y+F_P(\sigma,\theta)-\gamma\lambda .
\tag{4}
\]
The symbol D here is a polynomial, not a derivation or a new coordinate.
No surface reducibility or two-generator plane return is assumed.

## 2. The exact derivative identity and unit ideal

The first potential gives
\[
Z_v-2tY_v=S_v,\qquad
S_v=\gamma\sigma_v+m\theta_v,\qquad
Y_v=y_v+X\sigma_v .
\tag{5}
\]
Differentiating the second potential in v gives
\[
mw_v=-\gamma y_v-(2y+F_P)\sigma_v-F_V\theta_v.
\]
Adding the full X-dependent terms and collecting yields
\[
\boxed{
mW_v+\gamma Y_v-(X-\lambda)S_v=-\sigma_v D.
}
\tag{6}
\]
This is an identity in O[X]. It retains the lower terms of F;
there is no coefficient derivative or derivative of a moving X.

By (2), v is a polynomial over L in X,Y,Z,W. Differentiate this
polynomial identity in v, holding X fixed. The chain rule makes
1 an O[X]-linear combination of Y_v,Z_v,W_v. The invertible
row operations (5),(6), using m in L*, therefore prove the exact
ideal equality
\[
\boxed{
(Y_v,Z_v,W_v)\,O[X]
 =(y_v+X\sigma_v,\ S_v,\ \sigma_v D)\,O[X]
 =O[X].
}
\tag{7}
\]
This ideal statement is stronger than checking a single X value.

At a geometric parameter v0 with S_v(v0)=0 and sigma_v(v0) nonzero,
put X0=-y_v(v0)/sigma_v(v0). Then (5) makes Y_v and Z_v vanish
there, while (6) gives precisely
\[
mW_v(X_0,v_0)=-\sigma_v(v_0)D(v_0).
\tag{8}
\]
Thus D(v0) cannot vanish. This verifies the sign and the claimed
infinitesimal obstruction.

If sigma_v(v0)=S_v(v0)=0, equation (5) instead gives theta_v(v0)=0.
The whole return O=L[y,sigma,theta] implies that y_v(v0) is nonzero:
differentiating a polynomial expression for v would otherwise give
1=0. Therefore Y_v(X,v0)=y_v(v0) is nonzero for every X. These
points cause no failure of actual immersion and must not be discarded.

When sigma_v is a nonzero polynomial, (8) equivalently gives
\[
(S_v,D)\,O[1/\sigma_v]=O[1/\sigma_v],
\qquad (S_v,D):(\sigma_v)^\infty=O .
\tag{9}
\]
Indeed a common irreducible factor of S_v and D away from sigma_v
would have a geometric root contradicting (8). Conversely the
absence of such factors gives the displayed localized Bezout identity.
When sigma_v is identically zero, no localization at that polynomial
is used; the preceding direct argument handles the exceptional case.

## 3. The exact gcd and its multiplicity

The polynomials sigma_v,theta_v are not both zero. Otherwise sigma
and theta would be constant, and the monic equation (3) would make
y constant, contradicting O=L[v]. Put
\[
T=\gcd(\sigma_v,\theta_v)\quad\text{monic in }L[v].
\tag{10}
\]
At any geometric root v0 of T, the previous section gives y_v(v0)
nonzero. Differentiating H(y,sigma,theta)=h0 once therefore gives
D(v0)=0. Differentiating D=2y+A1(sigma,theta) gives
\[
D_v(v_0)=2y_v(v_0)\ne0.
\tag{11}
\]
Thus every such root is a simple root of D.

The polynomial T is also squarefree. If v0 were a common root of
sigma_v,theta_v of multiplicity at least two, then sigma_vv and
theta_vv would both vanish there. Differentiating the surface
relation twice at v0, using D(v0)=0 and (11), gives
\[
0=2y_v(v_0)^2
   +H_P(y,\sigma,\theta)(v_0)\,\sigma_{vv}(v_0)
   +H_V(y,\sigma,\theta)(v_0)\,\theta_{vv}(v_0),
\tag{12}
\]
which is impossible in characteristic zero under that assumption.
Hence at least one projected derivative has exactly a simple zero.

By (5), roots of T are roots of S_v. Conversely if S_v and D vanish
at a geometric point, (8) forces sigma_v to vanish there, and then
(5) forces theta_v to vanish. Thus their common root set is exactly
the root set of T. Equation (11) makes the common-root multiplicities
on the left equal to one, and the previous paragraph does the same
on the right. This proves (1) over L.

The gcd on the left is well-defined: S_v and D cannot both be
identically zero. If they were, (7) would make y_v+X sigma_v a unit
of O[X], forcing sigma_v=0 and y_v in L*. Then S_v=0 gives
theta_v=0, contradicting the monic relation as above.

In particular a projected immersion has gcd(S_v,D)=1. If sigma is
affine nonconstant, this coprimality follows automatically from (1).
No numerical degree bound on the remaining generators follows from
coprimality alone.

## 4. The exact finite divided-difference version

For independent variables v1,v2 define
\[
\partial_{12}f=\frac{f(v_1)-f(v_2)}{v_1-v_2}\in L[v_1,v_2].
\tag{13}
\]
This notation denotes polynomial divided difference, including its
well-defined value on the diagonal. Use bars for arithmetic means
of function values at v1,v2, and set
\[
\Gamma=\sigma(v_1)+\sigma(v_2)+k_t,\quad
\lambda_{12}=F_V(\bar\sigma,\bar\theta)/m,\quad
C=y(v_1)+y(v_2)+F_P(\bar\sigma,\bar\theta)-\Gamma\lambda_{12}.
\tag{14}
\]
Quadratic polarization of F and the second potential give the
polynomial identity
\[
\begin{aligned}
&m(\partial_{12}w+X\partial_{12}\theta)
 +\Gamma(\partial_{12}y+X\partial_{12}\sigma)
 -(X-\lambda_{12})\partial_{12}S\\
&\hspace{40mm}=-(\partial_{12}\sigma)C .
\end{aligned}
\tag{15}
\]
On the diagonal this is (6), with C becoming D.
Off the diagonal, C is exactly325's midpoint collision expression.

Subtract the polynomial inverse expression for v in (2) at v1 and
v2 and divide by v1-v2. Polynomial telescoping shows that 1 belongs
to the ideal generated by the divided differences of Y,Z,W.
The same invertible row operations prove
\[
\boxed{
(\partial_{12}y+X\partial_{12}\sigma,\,
 \partial_{12}S,\,
 (\partial_{12}\sigma)C)\,
 L[X,v_1,v_2]=L[X,v_1,v_2].
}
\tag{16}
\]
This is the simultaneous finite and infinitesimal condition.
Away from a nonzero polynomial partial12 sigma it implies the
localized unit ideal generated by partial12 S and C. To see this
algebraically, substitute
X=-partial12 y/partial12 sigma in (16) in that localized ring.

At an exceptional geometric pair where partial12 sigma and
partial12 S both vanish, partial12 theta vanishes too. The whole
return O=L[y,sigma,theta], applied by the same telescoping argument,
forces partial12 y nonzero there. Thus the first entry in (16)
remains nonzero. No division by a zero divided difference is needed.

Ramification information on the diagonal does not imply that
off-diagonal forbidden pairs exist. Equation (16), not such an
implication, is the proved relation between the two tests.

## 5. An unbounded formal family passes every all-X test

The following is the formal boundary family in the completely read
[290, Section5](principal-paraboloid-nonzero-coupling-projection-pass290-working.md),
with an additional explicit all-X inverse. Work in
L=C(t,s), let j be any positive integer, and put
\[
\begin{gathered}
k=s,\quad m=1,\quad n=0,\quad \ell=t,\quad h_0=s,\\
y=v,\quad \sigma=v^2-s,\quad
\theta=v^{2j+1}+6sv^2-s^2+s,\\
z=2tv+\sigma^2+\theta,\qquad w=t-2\sigma v.
\end{gathered}
\tag{17}
\]
The two literal potentials hold with F=0, and the full monic
surface is H=U^2-P, so H(y,sigma,theta)=s. Also
O=L[y,sigma,theta]=L[v]. Even the complex intercept return holds:
\[
s=z-2yw-5y^4-y^{2j+1},\qquad
t=w+2y^3-2sy.
\tag{18}
\]
Thus C[y,z,w]=C[t,s,v]. These are explicit algebraic identities,
not claims of an actual original frame for the full X-dependent map.

Form Y,Z,W by (2), and define their coefficient-field polynomial
combinations
\[
\begin{aligned}
f&=Y-tX^2=v+X\sigma,\\
g&=Z-2tY-sX+t^2X^2=\sigma^2+\theta,\\
h&=W-t-sX^2=-2\sigma v+X\theta.
\end{aligned}
\tag{19}
\]
Direct multiplication gives
\[
f^2+Xh-X^2g=v^2,\qquad
\boxed{v=f-X(f^2+Xh-X^2g-s).}
\tag{20}
\]
Therefore L[X,Y,Z,W]=L[X,v] in this formal family for every j.
It passes all polynomial-generation, immersion and collision
conditions of Sections2--4, not just the diagonal gcd test.

For the latter specifically,
\[
\begin{aligned}
S&=v^4+4sv^2+v^{2j+1}+s,\qquad D=2v,\\
S_v&=4v^3+8sv+(2j+1)v^{2j},\\
\sigma_v&=2v,\qquad
\theta_v=(2j+1)v^{2j}+12sv,\\
\gcd(S_v,D)&=\gcd(\sigma_v,\theta_v)=v .
\end{aligned}
\tag{21}
\]
This also shows why the exceptional sigma_v=0 case cannot be replaced
by the false unsaturated assertion gcd(S_v,D)=1.

Crucially the literal full determinant is
\[
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
 =-1-\bigl(12sv+(2j+1)v^{2j}+1\bigr)X.
\tag{22}
\]
Its constant coefficient is the unit -1, but its X coefficient is
nonzero. Thus this family fails the full actual calibration in (2).
The coordinates have the formal time-degree pattern and initial
paraboloid relation, but no actual globally sliced derivation on the
four generated coordinates satisfying the chart assumptions is
supplied. This is not a cancellation counterexample.

The exact surface is irreducible, the intrinsic degrees of theta
are unbounded, and (20) is still valid. Consequently all-X polynomial
return, even together with these first three potentials and strong
intercept return, cannot replace the missing full calibration.
The fourth-potential and independent-gradient inputs used for299's
degree bound are not certified by this family.

## 6. Scope and verification boundary

The actual conclusions are the derivative unit ideal (7), the
squarefree exact gcd (1), and the divided-difference unit ideal (16).
The formal family isolates their insufficiency. No general
off-diagonal-existence theorem, classification of the degree-bounded
frontier, original-coordinate descent or cancellation theorem is
claimed.

Complete saved325 and264 were freshly read before use; complete290
was read through its final boundary discussion. A new unsaved symbolic
calculation reconstructed (6),(15),(20) and the full determinant
(22), retaining an arbitrary polynomial q(v) in place of v^(2j+1)
for the last two identities. All residuals were zero. Finite gcd
fixtures supplemented, but did not prove, the uniform formula (21).
No saved checker was executed, imported, compiled or rerun by this
author, and no retained proof, checker, index or packet was edited.
