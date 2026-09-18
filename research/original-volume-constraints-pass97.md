# Original-coordinate constraints on a noncollapsed double fiber

In the supplied actual nonconical quadratic frame, the cylinder over
a noncollapsed fixed component is an actual quadratic graph in the
original affine four-space. After a constant affine change of the three
good coordinates, it has ideal
\((L,z-qW^2/2-R(U))\), where R has degree at most two and the canonical
slice restricts to W.

This is stronger than an abstract affine-plane identification: the first
equation is an original affine-linear good function, and subtracting the
displayed quadratic from the original bad coordinate is a genuine
triangular automorphism. Slice evaluation gives two global invariant
generators for the component ideal in A. An actual triangular translation
also commutes with E on this surface, but global commutation is not proved.

## 1. The actual frame and its retained volume bound

Retain the actual quadratic setup of
[the frontier96](quadratic-fiber-recognition-frontier-pass96.md).
Use the canonical slice u and the literal reconstruction
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
Eu=1,\qquad q=E^2z\in\mathbb C^*,\qquad E^2x_i=0,\\
S=\mathbb C[s_1,s_2]=\ker(N|_A),\qquad Nu=0,\quad [E,N]=0,\\
A=S[A_1,A_2,c],\qquad A_K=K[v],\quad K=\operatorname{Frac}S,\\
x_{\rm tr}=b(u-h)+v_2A_1+v_3A_2,\qquad
z=c+\frac q2(u^2-h^2),\qquad
[b,v_2,v_3]\in\operatorname{GL}_3(S),\\
\deg_v A_i,\ \deg_v h\le2,\qquad \deg_v c\le4 .
\end{gathered}
\tag{1}
\]
All h,c,A_i lie in A. The bound on h is not inferred from its
polynomiality. The actual volume identity88 gives
\(\Omega h\in S+SA_1+SA_2\) with \(0\ne\Omega\in S\);
the quadratic branch bounds the generic degrees of the two A_i.
The bound on c is the actual quadratic-potential consequence90.
These are also recorded explicitly in
[closed-fiber92, equation (2)](nonconical-closed-fiber-multiplicity-pass92.md).

Let \(\mathfrak q\) be a noncollapsed fixed component over the closed
base point \(\mathfrak m\). The results95--96 give whole multiplicity
two and an entire reduced line \(A/\mathfrak q=\mathbb C[\bar U_0]\).
Here U_0 is a surviving constant linear combination of the actual A_i,
and both their residues are affine-linear in \(\bar U_0\).
The component is the whole reduced fiber by compatibility96.
No first-normal-action hypothesis is imposed.

## 2. Degree specialization also applies to h and c

The component-degree proof92 applies to any actual \(f\in A\) with
nonconstant residue, not only to the three chosen generators.
For precision, \(f\notin K\), since \(A\cap K=S\) has constant
residue at the closed base point. Thus \(S[f]\) is a polynomial
three-ring and
\[
\begin{gathered}
T_f=(S[f])_{\mathfrak mS[f]}\longrightarrow O=A_{\mathfrak q}
\text{ is a local injection of regular two-dimensional rings},\\
O\text{ is flat over }T_f,\qquad
O\otimes_{T_f}K(f)=K(v),\\
2[\mathbb C(\bar U_0):\mathbb C(\bar f)]
\le [K(v):K(f)]=\deg_v f .
\end{gathered}
\tag{2}
\]
The contraction of \(\mathfrak q\) is exactly \(\mathfrak mS[f]\),
because \(\bar f\) is transcendental over \(\mathbb C\).
The closed local fiber is zero-dimensional. Regularity of the
source, Cohen--Macaulayness of the target, and \(2=2+0\)
therefore give flatness.[^flat]

For the inequality, lift a residue basis of
\(O/\mathfrak mO\) over \(\mathbb C(\bar f)\).
Its dimension is the whole Artinian length two times the
residue-field degree in (2). Flatness identifies its tensor
product with each graded piece of \(T_f\) with the corresponding
\(\mathfrak mO\)-adic graded piece of O. A linear relation between
the lifts over \(K(f)\), after clearing denominators and taking
least source-adic order, would contradict residue independence.
Hence the number of lifts is at most the generic rank.
The generic localization is the displayed field because the
nonconstant polynomial f makes \(K[v]\) finite over \(K[f]\).
This is the retained proof92 with f substituted throughout;
no finite-module assertion or localization of an LND is used.

The residue of each actual function is a polynomial in \(\bar U_0\).
A polynomial of positive degree k has function-field degree k.
Applying (2) to h or c when its residue is nonconstant, and
including constant residues separately, gives
\[
\begin{gathered}
\bar A_i=\alpha_i\bar U_0+\beta_i,\qquad
(\alpha_1,\alpha_2)\ne(0,0),\\
\bar h=H(\bar U_0),\quad \deg H\le1,\qquad
\bar c=C(\bar U_0),\quad \deg C\le2,\qquad
H,C\in\mathbb C[T].
\end{gathered}
\tag{3}
\]
This is a whole reduced-line conclusion. It is not just an
identity in a rational coefficient field.

## 3. A constant good-coordinate change gives the exact quadratic graph

Put \(b_0=b(\mathfrak m)\) and
\[
\begin{gathered}
d=\alpha_1v_2(\mathfrak m)+\alpha_2v_3(\mathfrak m),\qquad
e=\beta_1v_2(\mathfrak m)+\beta_2v_3(\mathfrak m),\\
B/\mathfrak qB=\mathbb C[u,\bar U_0],\qquad
\bar x_{\rm tr}=b_0\bigl(u-H(\bar U_0)\bigr)+d\bar U_0+e .
\end{gathered}
\tag{4}
\]
The two constant columns \(b_0,d\) are independent, because
the completed three-column matrix in (1) remains invertible
at \(\mathfrak m\) and \((\alpha_1,\alpha_2)\ne0\).
Complete these two columns to a constant basis of \(\mathbb C^3\).
Its dual affine coordinates on \(x_{\rm tr}-e\) may be called
X,U,L, with restrictions \(X=u-H(\bar U_0)\), \(U=\bar U_0\),
and \(L=0\). They are genuine affine-linear coordinates in
the original good three-ring.

Set \(W=X+H(U)\). Since H is affine, W,U,L are still an
affine-linear coordinate system in that original three-ring.
Define the polynomial R and the actual bad-coordinate shear K_0 by
\[
\begin{gathered}
R(T)=C(T)-\frac q2H(T)^2,\qquad \deg R\le2,\qquad
K_0=z-\frac q2W^2-R(U),\\
\boxed{\quad
\mathfrak P:=\mathfrak qB=(L,K_0),\qquad
B/\mathfrak P=\mathbb C[W,U],\qquad \bar u=W .
\quad}
\end{gathered}
\tag{5}
\]
Indeed both equations vanish under (4) and (3), and
\(B/(L,K_0)\to B/\mathfrak qB\) is the isomorphism of
polynomial planes taking W to u and U to \(\bar U_0\).
This proves equality of ideals, not merely containment.

Moreover \(W,U,L,K_0\) are actual polynomial coordinates of B.
Their inverse recovers the original good coordinates by the
inverse constant affine change and recovers
\(z=K_0+qW^2/2+R(U)\). This inverse uses no coefficients
from an unrecovered subring. The contrast with bridge96 is
therefore an actual original-coordinate distinction.

## 4. Two global invariant generators for the component ideal

Let \(\pi_E:B=A[u]\to A\) be evaluation at the canonical u=0.
The ideal \(\mathfrak P=\mathfrak qB\) is preserved by this
retraction and has image \(\mathfrak q\).
Since W,U,L are original affine-linear good functions and
K_0 is the original z minus a quadratic in good functions,
\(E^3K_0=0\). Thus the two invariant projections are explicitly
\[
\begin{gathered}
F=\pi_E(L)=L-uEL,\qquad
G=\pi_E(K_0)=K_0-uEK_0+\frac{u^2}{2}E^2K_0,\\
\boxed{\quad \mathfrak q=(F,G)A,\qquad
A/(F,G)=\mathbb C[\bar U_0].\quad}\\
N^3F=0,\qquad N^5G=0 .
\end{gathered}
\tag{6}
\]
For the last line, N kills u and commutes with E, so it commutes
with \(\pi_E\). The good affine functions have N-degree at most
two by (1), while z and the quadratic terms of K_0 have N-degree
at most four. These assertions are in B and A themselves,
by injection into \(A_K[u]\), not assertions of local nilpotence
on a completed local ring.

The pair F,G generates the height-two prime globally.
It is a regular sequence since A is regular and the generated
ideal has height two. This gives a global complete-intersection
description of the component in A. It does not make F or G a
global coordinate. An actual lift
\(U_A=\pi_E(U)=U-uEU\) has residue \(\bar U_0\).
Consequently \(dF,dG,dU_A\) form a cotangent basis at every
point of this smooth component, by its regular embedding and
the coordinate parameter on its reduced line. No assertion
that they form a basis away from the component is made.

## 5. Actual translations and original partial identities on the surface

The original \(T=\partial_z\), keeping the three good coordinates
fixed, remains \(\partial_{K_0}\) after the shear. In particular
\(T K_0=1\): it is transverse to the surface and does not preserve
\(\mathfrak P\). This differs from the collapsed plane92, whose
two equations involved only good coordinates.

There is instead an actual triangular LND on the original B,
\[
\begin{gathered}
D=\partial_U+R'(U)\partial_z
\quad\text{in the coordinates }W,U,L,z,\\
DW=DL=DK_0=0,\qquad DU=1,\qquad
D\mathfrak P\subset\mathfrak P,\\
\bar E=\partial_W,\qquad \bar D=\partial_U
\text{ on }B/\mathfrak P=\mathbb C[W,U],\qquad
[E,D](B)\subset\mathfrak P .
\end{gathered}
\tag{7}
\]
Its polynomial flow is \(U\mapsto U+\tau\),
\(z\mapsto z+R(U+\tau)-R(U)\), fixing W,L; the inverse uses
\(-\tau\). The last assertion follows because both actions
preserve the actual ideal and induce commuting translations.
It is only a quotient commutator identity.

The un-sheared coordinates \(W,U,L,z\) differ from the original
ones by a constant affine change in the good variables. Write
\(P=(EW,EU,EL,qu)^t\) and let J be its Jacobian in this order.
Along the surface P restricts to \((1,0,0,qW)^t\).
Differentiating this restriction along its two actual tangent
translations gives the original-column constraints
\[
\boxed{\quad
J e_U+R'(U)J e_z\equiv0,\qquad
J e_W+qWJ e_z\equiv q e_z
\pmod{\mathfrak P}.
\quad}
\tag{8}
\]
These are identities of polynomial columns on the entire surface,
not only at its generic point. The first tangent is D. The
second is \(\partial_W+qW\partial_z\), which becomes
\(\partial_W\) in W,U,L,K_0 and is the induced E there.
Equation (8) therefore uses the actual original Jacobian; it
does not treat the nonlinear bad-coordinate shear as a constant
matrix conjugation of J.

There is also a pointwise nilpotence improvement on this whole surface.
The component is fixed by N, so the two base differentials have rank
at most one there; the everywhere-rank theorem95 makes their rank
exactly one. Each of the first three velocity functions is a function
of the base, hence the first three rows of J have rank at most one.
The final row is q times the differential of u, so J has rank at most
two at every surface point. The actual original J is nilpotent.
A nilpotent four-by-four matrix of rank at most two has no Jordan
block of size four, and therefore its cube is zero. Since the surface
ring is reduced, this proves the polynomial congruences
\(J^3\equiv0\) and, using the actual identity \(JP=q e_z\),
\(J^2e_z\equiv0\pmod{\mathfrak P}\). These are degenerations on
the surface, not identities on the original four-space.

## 6. Remaining scope and provenance

This deduction uses the original volume bounds to make the
residue correction affine and the residue center quadratic.
The actual original inverse then turns their graph into the
coordinate ideal (5), which permits the global retraction (6).
Neither an arbitrary polynomial proposed tuple nor an abstract
Weitzenbock quotient would justify that original-coordinate step.

The result supplies exact normal equations and partial constraints
for the remaining irreducible noncollapsed double fiber. It does
not exclude that fiber, prove \(T\mathfrak q\subset\mathfrak q\),
upgrade (7) to global commutation, or recognize A.
In particular an invariant complete-intersection ideal does not
supply an invariant ambient coordinate. Arbitrary sliced actions
are still not known to enter this supplied frame.

The complete retained volume-descent88, cubic relation90,
open-free90, closed-fiber92 and the relevant plane92 and
noncollapsed95 arguments were reread for this derivation.
No theorem has been inferred from a proposed coordinate frame.
The proof has no new numerical method or frozen-file edit.

[^flat]: The Stacks Project,
[miracle flatness, Lemma 10.128.1, tag 00R4](https://stacks.math.columbia.edu/tag/00R4).
The complete displayed statement and proof were freshly read.
Only the regular-source, Cohen--Macaulay-target local dimension
criterion is used in (2); its deeper flatness references were not
freshly reconstructed.
