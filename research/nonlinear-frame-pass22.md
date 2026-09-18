# Nonlinear frames: a curvature obstruction and the missing completeness step

The invariant projection does not inherit the ambient flat connection.
There is an explicit coordinate translation whose projected connection
has nonzero curvature. A second coordinate translation has a projected
connection that is flat and torsion-free, but has no polynomial
horizontal frame. Both failures occur on ordinary polynomial three-space.

This note gives the exact general projection formula, independently
checked negative controls, and a useful conditional improvement: a
commuting derivation basis needs only one locally nilpotent member to
produce an intrinsic slice when the first algebraic de Rham group
vanishes. It does not construct that basis for an arbitrary cancellation
kernel. These are elementary structural reconstructions, not novelty
claims or a proof of general cancellation.

## 1. The canonical tangent projection

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s],\qquad
E=\partial_s,\quad A=\ker E.
\]
Identify \(A\) with \(B/(s)\). Its invariant retraction is
\[
\pi(g)=\sum_{j\ge0}\frac{(-s)^j}{j!}E^j(g).
\tag{1}
\]
The sum is finite. Put
\[
e_i=\pi(E x_i),\quad \lambda_i=\pi(\partial_{x_i}s),
\quad e=(e_i)_{i=1}^4,\quad \lambda=(\lambda_i)_{i=1}^4.
\]
Here \(e\) is a column and \(\lambda\) a row. The identity
\(E(s)=1\) gives \(\lambda e=1\). Therefore
\[
P=I_4-e\lambda,\qquad P^2=P,\qquad
\operatorname{im}P=\ker\lambda.
\tag{2}
\]
If \(\overline{x_i}\) denotes the image in \(B/(s)\), the map
\[
j:\operatorname{Der}_{\mathbb C}(A)\longrightarrow A^4,
\quad j(V)=(V\overline{x_i})_i
\]
identifies the tangent module with \(\ker\lambda\). Indeed, a
derivation of the hypersurface quotient is exactly a vector annihilating
the defining relation. The slice makes that hypersurface smooth.

For an ambient coordinate partial define
\(\delta_i=\pi\partial_{x_i}|_A\). These four derivations
generate \(\operatorname{Der}(A)\) as an \(A\)-module, and
\[
j(\delta_i)=P\varepsilon_i.
\tag{3}
\]
To verify (3), differentiate (1) for \(g=x_k\) and reduce modulo
\(s\). Only the terms with \(j=0,1\) remain, giving
\(\delta_i(\overline{x_k})=\delta_{ik}-\lambda_i e_k\).
No Lie-algebra or local-nilpotence assertion follows from this module
projection.

## 2. A general projected-connection formula

Differentiate the coefficients of vectors in \(A^4\) using
\(V\in\operatorname{Der}(A)\). Define a connection by
\[
j(\nabla_V W)=P\,V(j(W)).
\tag{4}
\]
It satisfies the connection Leibniz rules and is torsion-free, because
\(V(j(W))-W(j(V))=j([V,W])\).

The connection need not be flat. Define its scalar second fundamental
form and tangent normal derivative by
\[
\mathrm{II}(V,W)=\lambda\,V(j(W)),\qquad
S(V)=P\,V(e).
\tag{5}
\]
Both are tensors, and \(\mathrm{II}\) is symmetric. Using the
curvature convention
\(R(V,W)U=\nabla_V\nabla_WU-\nabla_W\nabla_VU-
\nabla_{[V,W]}U\), direct differentiation gives
\[
j(R(V,W)U)
=\mathrm{II}(V,U)S(W)-\mathrm{II}(W,U)S(V).
\tag{6}
\]
For completeness, decompose
\(V(j(U))=j(\nabla_VU)+e\,\mathrm{II}(V,U)\).
Apply \(W\), subtract the expression with \(V,W\) exchanged,
and project with \(P\). The ambient coefficient connection has zero
curvature, leaving exactly (6). This is the hypersurface Gauss formula
in the specified algebraic splitting, proved here without assuming
that the induced connection is flat.

Thus automatic flatness would require a new identity making the right
side of (6) vanish. Neither \(P^2=P\) nor freeness of the tangent
module supplies that identity.

## 3. Curvature already occurs for an explicit translation

In \(B=\mathbb C[x,y,z,t]\), take
\[
s=t-x^2,\qquad E=y\partial_x+(1+2xy)\partial_t.
\tag{7}
\]
The following are genuine polynomial coordinates:
\[
a=x-y(t-x^2),\quad b=y,\quad c=z,\quad s=t-x^2,
\]
with inverse
\[
x=a+bs,\quad y=b,\quad z=c,\quad t=s+(a+bs)^2.
\tag{8}
\]
Consequently \(E(s)=1\), \(E(a)=E(b)=E(c)=0\), and
\(A=\mathbb C[a,b,c]\). The zero-slice embedding, normal,
and conormal are
\[
\iota(a,b,c)=(a,b,c,a^2),\qquad
e=(b,0,0,1+2ab)^T,\qquad
\lambda=(-2a,0,0,1).
\tag{9}
\]
The only nonzero coordinate coefficient of (4) is
\[
\nabla_{\partial_a}\partial_a=-2b\partial_a.
\tag{10}
\]
Indeed \(j(\partial_a)=(1,0,0,2a)^T\), its ambient
\(a\)-derivative is \((0,0,0,2)^T\), and projection
subtracts \(2e\), yielding \(-2b\,j(\partial_a)\).
All other derivatives of the coordinate tangent columns vanish.
It follows that
\[
R(\partial_a,\partial_b)\partial_a=2\partial_a\ne0.
\tag{11}
\]
This refutes flatness of the particular projected connection even when
the desired polynomial kernel and nonlinear inverse are already known.
It does not refute existence of a different flat connection on \(A\).

The projected ambient partials themselves are
\[
\delta_x=(1+2ab)\partial_a,\quad
\delta_y=\partial_b,\quad \delta_z=\partial_c,\quad
\delta_t=-b\partial_a.
\tag{12}
\]
The first is not locally nilpotent, because for every \(k\ge1\),
\[
\delta_x^k(a)=(2b)^{k-1}(1+2ab)\ne0.
\]
A successful nonlinear repair exists here:
\(\delta_x+2a\delta_t=\partial_a\). But finding one such
repair in a known coordinate example does not construct repairs for
arbitrary \(A\). The curvature in (11) also cannot be removed just
by changing the module frame of that same connection.

## 4. Flat and torsion-free still need not give a polynomial frame

On the same polynomial ring \(A=\mathbb C[a,b,c]\), consider
the algebraic connection \(\nabla^0\) defined by
\[
\nabla^0_{\partial_a}\partial_a=\partial_a,
\qquad \nabla^0_{\partial_i}\partial_j=0
\quad\text{for all other pairs}.
\tag{13}
\]
It is torsion-free. Its connection matrices are the constant diagonal
matrix \(\operatorname{diag}(1,0,0)\) in the \(a\)-direction
and zero in the other directions, so its curvature is zero.

This is itself an actual connection of the form (4), not an arbitrary
flat connection unrelated to the slice setup. Take
\[
s=t-x^2,\qquad E_0=-\tfrac12\partial_x+(1-x)\partial_t,
\qquad a=x+s/2,\quad b=y,\quad c=z.
\]
The polynomial inverse is
\(x=a-s/2\), \(t=s+(a-s/2)^2\), \(y=b\), \(z=c\).
Thus \(E_0=\partial_s\) in this frame. On the zero slice,
\(e=(-1/2,0,0,1-a)^T\) and \(\lambda=(-2a,0,0,1)\).
The projection of \((0,0,0,2)^T\) is now
\((1,0,0,2a)^T=j(\partial_a)\), giving precisely (13).

A horizontal polynomial field
\(V=F\partial_a+G\partial_b+H\partial_c\) must satisfy
\[
\partial_a F+F=0,\qquad
\partial_b F=\partial_c F=0,
\]
and every partial derivative of \(G,H\) is zero. Comparing the
highest degree in \(a\) gives \(F=0\), while \(G,H\) are
constants. Hence the horizontal fields span only a two-dimensional
complex vector space and cannot form a polynomial tangent frame.

This example has free projective modules and vanishing positive-degree
algebraic de Rham cohomology. Even the trace connection form \(da\)
is exact. These properties do not produce the missing exponential
\(e^{-a}\) as a polynomial. Thus an appeal to de Rham acyclicity
cannot replace a proof of algebraic triviality of a flat connection.

## 5. A closed coframe and the actual local-nilpotence threshold

Here is a useful general conditional statement, requiring less than
three locally nilpotent members.

**Lemma.** Suppose \(A\) is a smooth affine complex domain of
dimension three, \(H^1_{\mathrm{dR}}(A)=0\), and
\(D_1,D_2,D_3\) is a commuting \(A\)-basis of
\(\operatorname{Der}(A)\). There are \(u_1,u_2,u_3\in A\)
with \(D_i(u_j)=\delta_{ij}\). In particular, every locally
nilpotent member of that basis has an intrinsic polynomial slice.

**Proof.** Let \(\omega_j\) be the dual coframe. For every
\(i,k\),
\[
d\omega_j(D_i,D_k)
=D_i(\delta_{jk})-D_k(\delta_{ji})-\omega_j([D_i,D_k])=0.
\]
Because the \(D_i\) form a basis, \(d\omega_j=0\).
The assumed first cohomology vanishing gives
\(\omega_j=du_j\). Duality now proves the identities.

If all three \(D_i\) are locally nilpotent, repeated finite Taylor
projection gives
\[
A=\left(\bigcap_i\ker D_i\right)[u_1,u_2,u_3].
\tag{14}
\]
For example the commuting finite operators
\(\sum_{m\ge0}(-u_i)^mD_i^m/m!\) project onto the respective
kernels, and their product yields the common-kernel expansion.
The common kernel is \(\mathbb C\), since every derivation of
\(A\) kills an element of it and the characteristic is zero.
The slice identities also prove algebraic independence of the \(u_i\).
Thus (14) explicitly reconstructs polynomial coordinates.

For the original stable threefold, one locally nilpotent member already
supplies an intrinsic slice by the lemma. Such an action is proper, so
[Gurjar--Masuda--Miyanishi, *Affine Space Fibrations*, Theorem 4.1.1,
printed p. 44](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download)
applies. Its statement was read directly: a stably affine threefold
with a proper additive action is affine three-space. The
[intrinsic-action note](intrinsic-actions-pass.md) records the same
application. This is a conditional reduction to finding a commuting
frame containing a known intrinsic LND, not a construction of that frame.

Finally, omitting local nilpotence at the last step conceals a separate
recognition problem. For any polynomial map
\(F=(F_1,F_2,F_3)\) with nonzero constant Jacobian determinant,
the exact forms \(dF_i\) are a polynomial coframe on
\(\mathbb C^{[3]}\). Their dual derivations form a commuting
polynomial basis: their commutators kill every \(F_i\), and the
invertible Jacobian makes such a derivation zero. Declaring these
primitives to be polynomial coordinates from those facts alone would
prove the three-variable Jacobian conjecture. Its standard formulation
is [Wright, *The Jacobian Conjecture as a problem in combinatorics*,
Conjecture 1.1](https://arxiv.org/pdf/math/0511214), read directly.
No such inference is established here.

## 6. Verification and exact remaining gap

Actual standalone SymPy calculations checked the slice and invariant
identities in (7)--(8), both inverse coordinate identities, the projection
matrix, the tangent inclusion, the curvature matrix
\(\operatorname{diag}(2,0,0)\), all projected fields (12),
the nonlinear repair, seven instances of the iterate formula, and the
flatness and torsion of (13). A second exact calculation verified the
actual slice, polynomial inverse, and projection realizing (13).
The all-\(k\) iterate formula and the
absence of a polynomial horizontal frame have written proofs.
An independent model audit reconstructed the curvature calculation
with the displayed sign convention. No new test suite is added.

The universal input gives a split tangent module and a canonical
projection, but the path to commuting locally nilpotent coordinates
still requires additional work. The projected connection can have
curvature. A replacement flat torsion-free connection can lack a
polynomial horizontal frame. A commuting polynomial frame still needs
local-nilpotence or another valid coordinate-recognition argument.
None of these failures excludes a different successful nonlinear
construction for an arbitrary slice. No registry edits, human expert
review, or general cancellation claim are part of this pass.
