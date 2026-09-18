# Nice recognition under a nondegenerate quadratic velocity relation

An actual nice sliced action on complex four-space is recognized if
its velocity satisfies a nondegenerate homogeneous quadratic relation.
The proof does not require a constant good partial. The quadratic
relation instead makes a relative generation determinant produce a
semisimple affine derivation. Its only stable irreducible plane curves
that can be polynomial lines are affine lines.

This is a conditional theorem. It does not prove that every remaining
velocity cone is a quadric, or that an arbitrary sliced action admits
a nice frame. Any incidence-theoretic reduction to the present
quadratic premise is a separate proof obligation.

## 1. The actual action and extra quadratic hypothesis

Assume
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=P\cdot\partial\in\operatorname{LND}(B),\qquad
E(s_*)=1,\qquad E(P)=0,\qquad J=\operatorname{Jac}_xP,
\quad J^2\ne0.
\tag{1}
\]
Suppose, in addition, there is a constant invertible symmetric matrix
\(C\in\operatorname{Mat}_4(\mathbb C)\) such that
\[
P^tCP=0.
\tag{2}
\]
Invertibility is essential here. In particular (2) is the hypothesis
of a rank-four quadratic velocity cone, not just an arbitrary
quadratic relation of smaller rank.

The [common-top theorem79](nice-common-top-normal-identity-pass79.md)
supplies an actual polynomial LND R commuting with E, with nonzero
intrinsic restriction, and the exact plane
\[
A=\ker E,\quad B=A[s_*],\quad
S=A\cap\ker R=\mathbb C[u,v],\quad
P\in S^4,\quad (P_1,P_2,P_3,P_4)S=S.
\tag{3}
\]
The inclusions \(S\subset A\subset B\) are faithfully flat, and
the intrinsic fibers over S are nonempty curves. Furthermore
\(\operatorname{rank}J=2\), \(P\notin\operatorname{im}J\),
and \(R(x)\in\operatorname{im}J\).
None of this uses a supplied good direction.

## 2. An actual relative frame from the quadratic form

By elementary linear algebra over \(\mathbb C\), an invertible
quadratic form in four variables is equivalent to the determinant
form. Make that genuine constant change of the original four
coordinates. Niceness, the slice, the common-plane conclusions,
and recognition are unchanged. We may therefore arrange that
\(P_1P_4-P_2P_3=0\) and use its polar form
\(\langle a,b\rangle=a_1b_4+a_4b_1-a_2b_3-a_3b_2\).
Its constant symmetric matrix is denoted C from now on.

The elementary [Segre frame construction](quadric-segre-frame-pass80.md)
gives
\[
\begin{pmatrix}P_1&P_2\\P_3&P_4\end{pmatrix}=p q^t,
\qquad (p_1,p_2)S=(q_1,q_2)S=S,
\qquad \det[p,p']=\det[q,q']=1.
\tag{4}
\]
For completeness, divide a nonzero column of the rank-one matrix
by its coefficient gcd to obtain a primitive p. Reduced-denominator
divisibility puts every other column multiplier in S, giving q.
The ideal of the four P entries is the product of the two pair
ideals. Its being the unit ideal makes each pair unimodular.
Actual Bezout identities then supply p' and q'. This does not infer
a unit ideal from gcd one over the plane.

Flatten two-by-two matrices row by row and set
\[
V=\operatorname{vec}(p(q')^t),\quad
W=\operatorname{vec}(p'q^t),\quad
H_0=\operatorname{vec}(p'(q')^t),\qquad
M=[P,V,W,H_0]\in\operatorname{SL}_4(S),\qquad
G=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}.
\tag{5}
\]
The matrix map is multiplication on the left by \([p,p']\) and
on the right by \([q,q']^t\), so its determinant is one and
both inverse matrices have entries in S. The polar determinant
pairings are \(\langle P,H_0\rangle=1\) and
\(\langle V,W\rangle=-1\), with all other pairings zero except
the symmetric counterparts. Thus G is the Gram matrix on V,W.
This explicit frame removes any projective-module completion input.

Put \(N=P^tC\), a unimodular row over S by (3).

The row N annihilates P, \(P_u\), and \(P_v\), by (2).
As \(\operatorname{im}J=\operatorname{span}_{\operatorname{Frac}B}
\{P_u,P_v\}\), it also annihilates R(x). Hence
\(k=Nx\) belongs to the actual S. Define \(\sigma,Y,Z,k\) by
\(M^{-1}x\), in that order. The first row of \(M^{-1}\) is
\(H_0^tC\), and the last is N. All its entries are in S. Thus
\[
E\sigma=1,\quad EY=EZ=0,\quad
x=P\sigma+VY+WZ+H_0k,\quad k\in S,
\qquad B=S[\sigma,Y,Z]=A[\sigma],\quad A=S[Y,Z].
\tag{6}
\]
For the last equality, evaluate at \(\sigma=0\) in the actual
slice presentation. These are ring-generation statements. The
matrix M has coefficients in the actual invariant subring S;
it has not been called a constant or ambient coordinate change.

The presentation map from the polynomial ring \(S[\mathsf Y,\mathsf Z]\)
to A has a height-one prime kernel. Choose its irreducible generator
F. Then \(A=S[Y,Z]/(F)\), with F primitive over S. A local slice
for \(R|_A\) gives, for \(K=\operatorname{Frac}S\),
\[
A_K=K[Y,Z]/(F)=K[t].
\tag{7}
\]
In particular F remains irreducible over K, and every element of
\(A_K\) algebraic over K belongs to K. The latter assertion follows
from the degree of a nonconstant polynomial in t. This is a generic
polynomial-line conclusion from the actual intrinsic LND, not a
claim about arbitrary plane curves.

## 3. The entire generation determinant

Use the polynomial five-ring \(S[Y,Z,\tau]\), and lift the four
original coordinates as
\(X=P\tau+VY+WZ+H_0k\). Modulo F they become the actual x, with
\(\tau\) becoming \(\sigma\). The conormal exact sequence and
the fact that the four actual \(dx_i\) form a basis give
\[
\det\frac{\partial(X_1,X_2,X_3,X_4,F)}
{\partial(u,v,Y,Z,\tau)}\equiv\kappa\pmod F,
\qquad \kappa\in\mathbb C^*.
\tag{8}
\]
For clarity, the conormal kernel is exactly the free B-line generated
by dF. It is a free line because some partial of irreducible F is
nonzero modulo F in characteristic zero. The lifts of the actual
\(dx_i\), together with dF, are a basis of the free five-module.
The determinant is therefore a unit of the actual polynomial B,
whose units are \(\mathbb C^*\). This is the same conormal gate
as [quadratic generation79](relative-quadratic-generation-pass79.md),
not a claim that F is already an ambient coordinate.

For i=u,v, write the derivative vector uniquely as
\(P_i=\alpha_iP+b_iV+c_iW\); its \(H_0\)-coefficient is zero by
\(NP_i=0\). Multiplying the already calculated first four
Jacobian rows in (8) by \(M^{-1}\) gives the matrix
\[
\begin{pmatrix}
A_u&A_v&0&0&1\\
B_u&B_v&1&0&0\\
C_u&C_v&0&1&0\\
\ell_u&\ell_v&0&0&0\\
F_u&F_v&F_Y&F_Z&0
\end{pmatrix},\qquad
\begin{cases}
B_i=b_i\tau+B_i^0(Y,Z),\\
C_i=c_i\tau+C_i^0(Y,Z),\\
\ell_i=-(b_i,c_i)G\binom{Y}{Z}+k_i-\alpha_i k.
\end{cases}
\tag{9}
\]
The superscript-zero expressions are affine-linear over S. In the
last equality use
\(N V_i=-\langle P_i,V\rangle\),
\(N W_i=-\langle P_i,W\rangle\), and
\(N(H_0k)_i=k_i-\alpha_i k\).
The row \(\ell\) is independent of \(\tau\).
No derivative of M is omitted: its derivatives are already present
in the original X-derivatives before the row multiplication.

The determinant of (9), with the displayed orientation, is
\[
\ell_uF_v-\ell_vF_u
 +(B_u\ell_v-B_v\ell_u)F_Y
 +(C_u\ell_v-C_v\ell_u)F_Z.
\tag{10}
\]
The first row's two unspecified entries do not enter it. Since
F is independent of \(\tau\), comparison of its coefficient
in (8) yields \(\mathscr L(F)\in(F)\), where
\[
\mathscr L=
(b_u\ell_v-b_v\ell_u)\partial_Y
 +(c_u\ell_v-c_v\ell_u)\partial_Z.
\tag{11}
\]
This is a K-linear affine derivation on \(K[Y,Z]\). It is not
asserted to be locally nilpotent.

Set \(\Delta=b_uc_v-b_vc_u\). The rank-three condition on
\([P,P_u,P_v]\) gives \(\Delta\ne0\). The linear part of
\(\mathscr L\) is exactly
\[
\Delta\begin{pmatrix}-G_{12}&-G_{22}\\G_{11}&G_{12}\end{pmatrix}
=\Delta\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad \operatorname{tr}=0,\qquad
\det=\Delta^2\det G\ne0.
\tag{12}
\]
An affine translation over K removes its constant part and puts it
in the form \(\Delta(\mathsf U\partial_{\mathsf U}
-\mathsf V\partial_{\mathsf V})\).
Only this field calculation is used in the next step.

## 4. The polynomial generic fiber excludes a hyperbola

Since \(\mathscr L\) does not increase total degree and
\(\mathscr L(F)\in(F)\), the transformed irreducible F is an
eigenpolynomial for the displayed diagonal derivation, including
the possible eigenvalue zero. Every monomial in it has the same
integer difference of \(\mathsf U\)- and \(\mathsf V\)-degrees.
For a positive difference, F has a factor \(\mathsf U\), and
irreducibility makes it a scalar multiple of \(\mathsf U\).
A negative difference similarly gives \(\mathsf V\).
For difference zero write it as \(f(\mathsf U\mathsf V)\),
with \(f\in K[T]\) nonconstant and irreducible. The image of
\(\mathsf U\mathsf V\) is algebraic over K in the actual generic
quotient (7), so belongs to K. Consequently f has degree one,
and F is a scalar multiple of \(\mathsf U\mathsf V-\gamma\)
for \(\gamma\in K\). The value \(\gamma=0\) is reducible;
if \(\gamma\ne0\), its quotient has the
nonconstant unit \(\mathsf U\), contradicting (7).

Only an affine line remains. Affine changes preserve total degree,
so F has total \((Y,Z)\)-degree one over K and hence over
the original S. Write
\[
F=aY+bZ+c,\quad a,b,c\in S,\qquad
(a,b)S=S,\qquad
\boxed{A\simeq_S S[t]\simeq\mathbb C^{[3]}.}
\tag{13}
\]
For the unit-row assertion, a maximal ideal of S containing a,b
would give either an empty fiber or a two-dimensional fiber,
according to the residue of c. Both contradict the actual
nonempty intrinsic curve fibers in (3).
Choose \(r,s\in S\) with \(ar+bs=1\). The two rows
\((a,b)\) and \((-s,r)\) have determinant one. Therefore F and
\(-sY+rZ\) are affine S-coordinates of \(S[Y,Z]\), and quotienting
by F proves the exact polynomial equality in (13).

The argument uses actual original coordinate generation, the
original slice, and the common-plane quotient. It neither treats
a generic affine change as global nor infers coordinates from a
unimodular row of unrelated functions.

## 5. Scope and verification

The extra relation (2), with C invertible, is the precise additional
input. This note does not derive it from an apex-free cone, apply
a theorem about gradient maps, or assert an apex exists. The
singular quadratic case is not covered by the nonsingular linear
part calculation (12).

An inline exact SymPy check verified (10) and the sign and determinant
in (12), with output in tool chunk `a4e0a4`. It is not a new test
suite or an actual-action realization. The complete written proof,
including the generic Darboux classification, is separate from
that finite check. No full regression, historical novelty,
human expert review or formal proof certification is claimed.
All files through pass79 and shared metadata remain unchanged.
The intrinsic plane and flat-fiber input remains the fully specified
[intrinsic quotient theorem](intrinsic-quotient-surface-pass.md).
