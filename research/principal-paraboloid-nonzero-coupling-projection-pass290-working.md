# Nonzero-coupling projection and smoothness in the principal paraboloid chart

Status: a bounded structural reduction of the \(k_s\ne0\) branch of
the actual chart264. The three projected generators are retained.
The cubic surface is nonsingular along the generic polynomial line,
and the projection to its last two functions has degree at most two.
A degree-two projection has an exact normal form over the original
coefficient field. A birational projection can still have singularities.

A separate explicit countercontrol satisfies all three retained
potentials, the full polynomial intercept return, and a nonzero
constant Jacobian coefficient. Its remaining \(X\)-coefficient is
nonzero. Thus it is not an actual polynomial coordinate frame.
It rules out deducing projected-plane smoothness or a degree bound
from the proved surface and return gates alone.

No retained source is changed. This note does not recognize or
exclude the entire nonzero-coupling sector.

## 1. Exact actual inputs

Use the complete actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
In particular,
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),
\]
and the full weighted initial kernel is
\((\mathsf X^2\mathsf Z-\mathsf Y^2)\).
The selected intrinsic derivation is the exact shift-four leading
part of the literal \(Z\)-partial. With \(a=EX\),
\[
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
O=A\otimes_{\ker N}L=L[v],\quad Nv=1,\quad K=L(v).
\tag{1}
\]
The coefficient partials \(t,s\) extend to \(L\) and fix \(v\).

The literal fixed-\(X\) map and its actual returns are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
K&=\mathbb C(y,z,w),\qquad L[y,z,w]=O .
\end{aligned}
\tag{2}
\]
Here \(y,z,w,\sigma,\theta\in O\), \(k\in L\), and the complete
calibrated determinant is
\[
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
=-a^4\in L^* .
\tag{3}
\]
This is a polynomial identity in \(O[X]\), not merely its constant
coefficient.

Assume \(m=k_s\ne0\). Retain the notation
\[
\begin{aligned}
F(P,V)&=\frac{k_{tt}}2P^2+k_{ts}PV+\frac{k_{ss}}2V^2
                         +n_tP+n_sV,\\
\gamma&=2P+k_t,\qquad
g(U,P,V)=\frac{\ell-\gamma U-F(P,V)}m .
\end{aligned}
\tag{4}
\]
The first two potentials give
\[
z=2ty+\sigma^2+k_t\sigma+m\theta+n,\qquad
w=g(y,\sigma,\theta),\qquad
O=L[y,\sigma,\theta].
\tag{5}
\]
The monic surface polynomial from264 is
\[
\begin{aligned}
\mathcal H={}&U^2+F_PU+F_Vg+
 H_3(k;P,V)+H_2(n;P,V)-\ell_tP-\ell_sV,\\
\mathcal H(y,\sigma,\theta)&=h_0\in L,\\
\mathcal H_U&=2U+F_P-\gamma F_V/m,\\
\mathcal H_P&=-m g_t+F_Vg_P,\qquad
\mathcal H_V=-m g_s+F_Vg_V .
\end{aligned}
\tag{6}
\]
Coefficient derivatives in these formulas fix \(U,P,V\).
The polynomial \(\mathcal H-h_0\) has total degree at most three
and is monic quadratic in \(U\).

## 2. A gradient unit from the full scalar determinant

Every formal expression in this section is evaluated at
\((y,\sigma,\theta)\) when used as an element of \(O\).
Set
\[
b_1=2y+F_P,\qquad c_1=F_V,\qquad
\lambda=c_1/m\in O .
\tag{7}
\]
After the determinant-preserving middle-row subtraction of264,
the differential rows at fixed \(X\) are
\[
\begin{aligned}
A_X&=dy+X\,d\sigma+X^2dt,\\
B_X&=\gamma\,d\sigma+m\,d\theta+b_1dt+c_1ds
                         +X(\gamma dt+m ds),\\
C_X&=dg+X\,d\theta+X^2ds.
\end{aligned}
\tag{8}
\]
Here \(dg\) is the total differential of the evaluated polynomial.
Its chain rule, with coefficient derivatives kept, is
\[
dg=-\frac{\gamma}{m}dy-\frac{b_1}{m}d\sigma
      -\frac{c_1}{m}d\theta+g_tdt+g_sds .
\]

There is the following exact covector identity:
\[
\boxed{
C_\lambda+\frac{\gamma}{m}A_\lambda
=-\frac1m\left[
 \mathcal H_U(d\sigma+\lambda dt)+
 \mathcal H_Pdt+\mathcal H_Vds\right].
}
\tag{9}
\]
For example, the \(d\sigma\) coefficient is
\((-b_1+\gamma\lambda)/m=-\mathcal H_U/m\).
The \(dt\) coefficient follows from
\(\mathcal H_P=-m g_t-c_1b_1/m\), and the \(ds\) coefficient from
\(\mathcal H_V=-m g_s-c_1^2/m\).
The \(dy,d\theta\) coefficients cancel as displayed.

In (9), \(X=\lambda\) means polynomial evaluation in (8).
It does not mean replacing the actual coordinate \(X\) and then
differentiating that replacement. In particular there is no
\(d\lambda\) term.

Taking determinants in (9) and using (3) yields
\[
-a^4
=-\frac1m\det\left(
 A_\lambda,B_\lambda,
 \mathcal H_U(d\sigma+\lambda dt)+
 \mathcal H_Pdt+\mathcal H_Vds\right).
\tag{10}
\]
All entries of these covectors in the basis \(dt,ds,dv\) lie in
\(O\). Thus
\[
\boxed{
(\mathcal H_U(y,\sigma,\theta),
 \mathcal H_P(y,\sigma,\theta),
 \mathcal H_V(y,\sigma,\theta))\,O=O .
}
\tag{11}
\]
Consequently the surface \(\mathcal H=h_0\) is nonsingular at
every point of the parametrized generic line, also after extending
\(L\) to an algebraic closure. This statement concerns the surface,
not the projected plane curve \(L[\sigma,\theta]\).

One additional consequence is safe without any principal
curve-kernel assumption. Factor \(\mathcal H-h_0\) in
\(L[U,P,V]\). Exactly one irreducible factor vanishes identically
on the parametrized line, and that factor occurs with multiplicity
one. Otherwise all three evaluated partial derivatives would
vanish. If \(G\) is that factor and
\(\mathcal H-h_0=GQ\), then
\[
Q(y,\sigma,\theta)\in O^*=L^* .
\tag{12}
\]
Indeed every evaluated derivative is divisible by this cofactor,
and (11) is the unit ideal. The kernel of the three-generator map
still has height two. In particular (12) does not imply
\(\mathcal H-h_0=\eta G+G^2R\).

## 3. A finite projection of degree at most two

Put
\[
C=L[\sigma,\theta]\subset O .
\]
Write
\[
\mathcal H-h_0=U^2+A_1(P,V)U+A_0(P,V),
\tag{13}
\]
where explicitly
\[
\begin{aligned}
A_1&=F_P-\gamma F_V/m,\\
A_0&=F_V(\ell-F)/m+H_3(k)+H_2(n)
                         -\ell_tP-\ell_sV-h_0 .
\end{aligned}
\]
We have \(\deg A_1\le2\), \(\deg A_0\le3\).
The actual three-generator return in (5) and the monic relation
give the stronger module equality
\[
\boxed{O=C[y]=C+Cy.}
\tag{14}
\]
In particular the projection to \((\sigma,\theta)\) is finite.

At least one of \(\sigma,\theta\) is nonconstant in \(v\).
Otherwise (13) makes \(y\) algebraic over \(L\), hence constant
as a polynomial in \(v\), contradicting \(O=L[v]\).
It follows that \(C\) has transcendence degree one over \(L\),
and
\[
\boxed{
d=[L(v):\operatorname{Frac}C]\in\{1,2\}.
}
\tag{15}
\]
This establishes neither \(d=1\) nor \(C=O\).

Suppose \(d=2\). The nontrivial automorphism of the separable
quadratic extension \(L(v)/\operatorname{Frac}C\) fixes \(C\) and
sends \(y\) to \(-A_1(\sigma,\theta)-y\). By (14) it preserves
\(O\) in both directions. Every \(L\)-automorphism of \(L[v]\)
is affine: polynomial inverse degrees multiply to one. Its
nontrivial order-two form is therefore \(v\mapsto-v+\beta\).
Set \(x=v-\beta/2\), so the involution is \(x\mapsto-x\).

We now have \(C\subset L[x^2]\) and a unique decomposition
\[
y=A(x^2)+xB(x^2),\qquad A,B\in L[T],\quad B\ne0 .
\]
Taking odd parts in (14) gives
\(L[x^2]=C\,B(x^2)\).
In particular \(1=cB(x^2)\) for some \(c\in C\), so
\(B\in L^*\), and then \(C=L[x^2]\). We have proved the exact
coefficient-field normal form
\[
\boxed{
C=L[r],\quad r=x^2,\quad
\sigma=P(r),\quad\theta=Q(r),\quad
L[P,Q]=L[r],\quad y=A(r)+c x,\quad c\in L^* .
}
\tag{16}
\]
No algebraic closure, rationality of \(L/\mathbb C\), or ambient
coordinate change has been used. Also \(Nx=1\).

For the formal discriminant
\(\Delta=A_1^2-4A_0\), of total degree at most four, the trace
of (13) and (16) give
\[
2A(r)=-A_1(P(r),Q(r)),\qquad
\Delta(P(r),Q(r))=4c^2r .
\tag{17}
\]
Thus the degree-two projection has the single simple ramification
point \(x=0\), lying above \(r=0\). Its image plane curve is normal and isomorphic
to the affine line over \(L\).

## 4. What is still allowed in the birational case

If \(d=1\), then \(O\) is the normalization of \(C\): it is finite
over \(C\), has the same fraction field, and is integrally closed.
This does not force \(C\) to be normal.

Two useful restrictions nevertheless follow from the same module
and monic relation. Work over an algebraic closure of \(L\).
Every geometric fiber of \((\sigma,\theta)\) has at most two
points. The values of \(y\) in such a fiber are roots of the same
monic quadratic (13). Distinct points cannot have equal \(y\),
since \(y,\sigma,\theta\) generate the entire polynomial ring.

At a two-point fiber the two roots of this quadratic are distinct,
so \(\mathcal H_U\ne0\) at both points. Both branches are immersed
in the plane. Indeed if \(\sigma_v=\theta_v=0\) at either point,
differentiating (13) gives \(y_v=0\); differentiating the polynomial
expression of \(v\) in the three generators then gives \(1=0\).

At a point where the normalization is not immersed, the same
generator argument gives \(y_v\ne0\), while (13) gives
\(\mathcal H_U=0\). Moreover
\[
\frac{d}{dv}\mathcal H_U=2y_v\ne0,\qquad
\Delta(\sigma,\theta)=\mathcal H_U^2 .
\tag{18}
\]
Hence an element of the plane ring has vanishing order exactly
two there. Since \(\sigma_v=\theta_v=0\), all elements of the
plane local ring's maximal ideal have order at least two. Every nonimmersed
normalized branch therefore has multiplicity exactly two.
No bound on tangency, conductor degree, or delta invariant follows.

## 5. A boundary family with exact polynomial intercept return

This section constructs formal data, not an actual coordinate frame.
Fix an integer \(j\ge1\) and work in the polynomial ring
\[
R=\mathbb C[t,s,x,X],\qquad L=\mathbb C(t,s).
\]
Set
\[
\begin{gathered}
k=s,\quad m=1,\quad n=0,\quad \ell=t,\quad h_0=s,\\
y=x,\qquad \sigma=x^2-s,\qquad
\theta=x^{2j+1}+6sx^2-s^2+s,\\
w=t-2\sigma x,\qquad z=2tx+\sigma^2+\theta .
\end{gathered}
\tag{19}
\]
Here \(F=0\), \(g=t-2PU\), and
\[
\mathcal H=U^2-P,\qquad
\mathcal H(y,\sigma,\theta)=s,\qquad
(\mathcal H_U,\mathcal H_P,\mathcal H_V)=(2U,-1,0).
\tag{20}
\]
Thus both first potentials, the monic third potential, and the
gradient-unit conclusion all hold literally.

There is even a full polynomial inverse at \(X=0\):
\[
x=y,\qquad
s=z-2yw-5y^4-y^{2j+1},\qquad
t=w+2y^3-2sy .
\tag{21}
\]
To verify both directions, substitute
\(w=t-2x^3+2sx\) and
\(z=2tx+x^4+4sx^2+x^{2j+1}+s\).
In particular
\[
\mathbb C[y,z,w]=\mathbb C[t,s,x],\qquad
L[y,z,w]=L[x],\qquad
C=L[\sigma,\theta]=L[x^2,x^{2j+1}].
\tag{22}
\]
The birational projected plane is singular. Its missing monomials
are \(x,x^3,\ldots,x^{2j-1}\), so
\(\dim_L(L[x]/C)=j\). Both its singularity complexity and
\(\deg_x\theta\) are unbounded in this family.

Form the literal polynomials with the same template as (2):
\[
\widehat Y=y+\sigma X+tX^2,\quad
\widehat Z=z+(2t\sigma+s)X+t^2X^2,\quad
\widehat W=w+\theta X+sX^2 .
\tag{23}
\]
Their degrees in \(X\), together with \(X\), are exactly
\((1,2,2,2)\). The formal leading map has full kernel
\((\mathsf X^2\mathsf Z-\mathsf Y^2)\):
its leading fraction field is
\(\mathbb C(t,s)(T)\), of transcendence degree three, and the
displayed irreducible relation therefore generates its height-one
kernel.

Nonetheless direct differentiation of the complete map gives
\[
\boxed{
\det\frac{\partial(\widehat Y,\widehat Z,\widehat W)}
              {\partial(t,s,x)}
=-1-\bigl(12sx+(2j+1)x^{2j}+1\bigr)X .
}
\tag{24}
\]
One can verify (24) uniformly by replacing \(x^{2j+1}\) in
(19) with an arbitrary polynomial \(q(x)\); the result is
\(-1-(12sx+q'(x)+1)X\).
All higher coefficients vanish and the constant coefficient is
the unit \(-1\), exactly as (19)--(21) predict. The remaining
\(X\)-coefficient is nonzero.

The full four-variable Jacobian is thus not a unit of \(R\).
Consequently these four polynomials are not a polynomial
coordinate frame of \(R\). In particular this family is not an
actual counterexample to recognition, nor is a locally nilpotent
derivation on their generated polynomial ring being asserted.

## 6. Scoped conclusion

For the actual nonzero-coupling chart, the surface gradient is a
unit ideal and the projected-plane map is finite of degree one
or two. Degree two forces the explicit smooth-plane normal form
(16). In degree one, fibers have at most two points, any two-point
fiber is immersed, and every nonimmersed branch has multiplicity
two. Singularities of the projected plane have not been excluded.

The boundary family retains the first three potentials, exact
polynomial intercept return, all the structural conclusions above,
and even a nonzero scalar constant determinant coefficient.
It fails precisely the unused linear coefficient. Thus the
remaining full scalar identity, not an assumed two-generator
return or projected-plane smoothness, must supply any further
closure.

The complete retained264 source was freshly read before this work.
Fresh unsaved algebra checked the covector identity (9) and the
uniform determinant (24); neither computation is a universal proof
of field return. No saved checker was executed, imported, or
compiled, and no earlier source was edited.
