# Slice descent for a central arrangement coefficient

Let \(\ell_0,\ldots,\ell_{d-1}\in\mathbb C[x,y]\) be pairwise
nonproportional homogeneous linear forms, with \(d\geq3\). Let
\[
P=\prod_{i=0}^{d-1}\ell_i^{m_i},\qquad m_i\geq1,
\qquad F=Pu+H(x,y,z).
\]
There is no degree restriction on \(H\). Then
\[
\boxed{D(F)=1\text{ for an LND of }\mathbb C[x,y,z,u]
\quad\Longrightarrow\quad F\text{ is a coordinate}.}
\tag{1}
\]
The same proof includes \(d=2\), whose separate derivation is in
[the repeated-crossing slice theorem](repeated-crossing-slice-descent.md).
Concurrency at a different point is handled by translation.

Two different conclusions are used. A nonconstant restriction to the
common \(z\)-axis gives an explicit coordinate under the weaker stable
hypothesis. In the constant-axis branch, stability determines the plane
residues, and a prior theorem about residual planes makes each fiber
affine three-space. The original LND slice hypothesis then identifies
that fiber ring with the kernel. This does not assert general
stable-coordinate descent in the constant-axis branch.

The affine-space fiber conclusion is an application of the existing
Kaliman--Vénéreau--Zaidenberg residual-plane theorem, not a new
residual-plane descent theorem. The topology and algebra below spell
out its hypotheses for concurrent factors of arbitrary multiplicity.

## 1. The arrangement complement and generic closed curves

Write \(L_i=V(\ell_i)\subset\mathbb A^2\), and let \(t_i\) be a linear
coordinate on \(L_i\). Put
\[
h(z)=H(0,0,z),\qquad q_i(t_i,z)=H|_{L_i\times\mathbb A^1_z}.
\]
Assume temporarily that \(F\) is a stable coordinate. Every fiber
\(X_\lambda=V(F-\lambda)\) is smooth and contractible: its product with
an affine space is an affine space. Thus its ordinary integral
cohomology vanishes in positive degrees, and its compactly supported
integral cohomology is \(\mathbb Z\) in degree six and zero otherwise.

On \(P\ne0\), the equation determines \(u\) uniquely, so
\[
U=X_\lambda\cap\{P\ne0\}
\cong\left(\mathbb A^2\setminus\bigcup_iL_i\right)\times\mathbb A^1_z.
\]
Choose coordinates with \(\ell_0=x\), and rescale the other forms to
\(\ell_j=y-\alpha_jx\), where the \(\alpha_j\) are distinct.
With \(w=y/x\), this becomes
\[
U\cong\mathbb C^*\times
\left(\mathbb C\setminus\{\alpha_1,\ldots,\alpha_{d-1}\}\right)
\times\mathbb A^1.
\tag{2}
\]
The integral groups needed below are
\[
H^1(U)=\mathbb Z^d,\qquad H^2(U)=\mathbb Z^{d-1},
\qquad H^j(U)=0\quad(j\geq3),
\]
and
\[
H_c^4(U)=\mathbb Z^{d-1},\qquad
H_c^5(U)=\mathbb Z^d,\qquad H_c^6(U)=\mathbb Z.
\tag{3}
\]
All other compact-support groups vanish.

Every \(q_i\) is nonconstant. Otherwise, if \(q_i=b_i\), a fiber with
\(\lambda\ne b_i\) has \(\ell_i\) as a nonconstant algebraic unit.
It is nonconstant on the open set (2), contradicting stability.

Choose a generic \(\lambda\) for which all the nonempty curves
\[
C_i=V(q_i-\lambda)\subset L_i\times\mathbb A^1_z
\]
are smooth. Their reduced union \(C\) gives the closed complement
\[
Z=X_\lambda\setminus U=C\times\mathbb A^1_u.
\]
The closed-open sequence and (3) give
\[
H_c^1(C)=\mathbb Z^{d-1},\qquad H_c^2(C)=\mathbb Z^d.
\tag{4}
\]
The curves meet only on the common axis and have finite intersections,
if any. Therefore
\[
H_c^2(C)=\bigoplus_i H_c^2(C_i).
\]
Each \(C_i\) is nonempty, and there are \(d\) of them. Equation (4)
makes every \(C_i\) connected, hence irreducible. Multiplicities \(m_i\)
do not enter these computations of reduced closed subsets.

## 2. Nonconstant axis: a complete stable-coordinate criterion

Suppose \(h\) is nonconstant of degree \(e\). Choose \(\lambda\) also
so that \(h-\lambda\) has \(e\) distinct roots. Each pair of curves
\(C_i,C_j\) meets in the same set \(S\) of these \(e\) axis points.
Gluing the \(d\) curves at this common finite set gives the exact sequence
\[
0\longrightarrow\mathbb Z^{e(d-1)}
\longrightarrow H_c^1(C)
\longrightarrow\bigoplus_iH_c^1(C_i)
\longrightarrow0.
\tag{5}
\]
For example, (5) follows from the exact constant-sheaf sequence whose
map at each point of \(S\) takes the \(d-1\) differences between the
values on the first branch and the other branches. The degree-zero
compact-support groups of the affine curves vanish.

All terms on the right are free abelian. Equations (4)--(5), and
\(d-1>0\), imply \(e=1\) and \(H_c^1(C_i)=0\) for every \(i\).
Thus each \(C_i\) is an affine line and \(h(z)=az+b\), with \(a\ne0\).

The plane-line rectification theorem and its relative-coordinate
consequence, recorded with proof and source in
[the two-factor nonconstant-axis argument](crossing-nonconstant-pass.md),
give
\[
q_i(t_i,z)=az+B_i(t_i),\qquad B_i(0)=b.
\tag{6}
\]
Let \(Q=\prod_i\ell_i\) and \(B(x,y)=H(x,y,0)\). The polynomial
\(H-az-B\) vanishes on every plane \(L_i\times\mathbb A^1_z\).
The distinct linear forms are relatively prime as irreducible factors
in a UFD, so their product divides this polynomial. Therefore
\[
\boxed{H=az+B(x,y)+Q(x,y)R(x,y,z),\qquad a\ne0.}
\tag{7}
\]

Conversely, (7) always makes \(F\) a coordinate. Indeed, if
\(N=\max_i m_i\), then \(Q^N\in(P)\). Over \(\mathbb C[x,y]\), the
polynomial \(az+B+QR\) has a finite compositional inverse modulo \(P\):
start with \(I_0(T)=(T-B)/a\) and update
\[
I_{j+1}(T)=\frac{T-B-QR(x,y,I_j(T))}{a}.
\]
After \(N-1\) updates, both inverse congruences hold modulo \(P\).
The companion and inverse are
\[
V=\frac{z-I(F)}P,\qquad
z=I(T)+PV,\qquad
u=\frac{T-H(x,y,I(T)+PV)}P.
\tag{8}
\]
They are polynomial, and both compositions are identities. The complete
divisibility proof is the finite-inverse lemma in
[the repeated-crossing note](repeated-crossing-pass.md); it needs only
that the perturbation is nilpotent modulo the coefficient and that
the coefficient of \(z\) is a unit.

Thus (7) is the exact stable-coordinate criterion in the nonconstant-axis
branch, for every central arrangement and every positive multiplicity.

## 3. Constant axis: the integral residue map limits every curve

Now suppose \(h=b\) is constant, and take a generic \(\lambda\ne b\).
The curves \(C_i\) are disjoint and avoid \(t_i=0\). Equation (4)
implies
\[
\sum_i\operatorname{rank}H^1(C_i;\mathbb Z)=d-1.
\tag{9}
\]
The equality of the ordinary and compact-support ranks here follows
from the usual genus-and-punctures formula for a smooth affine curve.
Equation (9) alone does not bound the individual ranks by one.

Set \(Z_i=C_i\times\mathbb A^1_u\). These are disjoint smooth divisors
in \(X=X_\lambda\). Moreover, \(\ell_i\) vanishes to order one along
\(Z_i\), since
\[
\mathcal O(X)/(\ell_i)
=\mathbb C[t_i,z,u]/(q_i-\lambda)
\]
is reduced at the chosen regular value. Every \(\ell_j\) with \(j\ne i\)
is a unit on \(Z_i\). Its restriction is a nonzero scalar multiple of
the radial coordinate \(t_i\).

The ordinary integral Gysin sequence gives an isomorphism
\[
\operatorname{res}:H^2(U;\mathbb Z)
\xrightarrow{\ \sim\ }
\bigoplus_iH^1(Z_i;\mathbb Z),
\tag{10}
\]
because \(H^2(X)=H^3(X)=0\).

Here is an explicit integral basis calculation of its image. For the
coordinates in (2), let \(\omega_i\in H^1(U;\mathbb Z)\) be the pullback
of the standard circle class by \(\ell_i\). If \(\sigma\) is that
class from the \(\mathbb C^*\) factor and \(\tau_j\) is the class
around \(w=\alpha_j\), then
\[
\omega_0=\sigma,\qquad \omega_j=\sigma+\tau_j.
\]
Consequently the \(d-1\) classes
\[
\omega_0\smile\omega_j=\sigma\smile\tau_j,
\qquad 1\leq j\leq d-1,
\]
are an integral basis of \(H^2(U)\).

Write \(\eta_i=t_i^*H^1(\mathbb C^*;\mathbb Z)\), meaning the image
of its positive generator in \(H^1(Z_i;\mathbb Z)\). Up to the consistent
orientation signs of normal circles, the residue of the \(j\)-th basis
element has \(\eta_0\) in component zero, \(-\eta_j\) in component
\(j\), and zero in the other components. The order-one vanishing above
is essential to this formula.

Thus the projection of the image of (10) to \(H^1(Z_i)\) lies in the
cyclic subgroup \(\mathbb Z\eta_i\). Surjectivity of (10) forces
\[
H^1(C_i;\mathbb Z)=\mathbb Z\eta_i
\quad\text{for each }i.
\tag{11}
\]
These groups are free, so their ranks are at most one. A connected
smooth affine curve with rank zero is \(\mathbb A^1\), and one with
rank one is \(\mathbb C^*\). Equations (9)--(11) now prove that exactly
one \(C_i\) is an affine line and the other \(d-1\) are punctured lines.

On a punctured-line stratum, its radial unit has the form
\(t_i=c_i'v_i^{n_i}\). The exponent is nonzero: a constant radial
coordinate would force the closed curve to be a vertical affine line.
Equation (11) makes the class primitive, so \(|n_i|=1\). The radial
map \(t_i:C_i\to\mathbb C^*\) is therefore an isomorphism. In particular,
no higher covering degree can pass the integral residue test.

### One distinguished line and all the other plane restrictions

There are infinitely many regular generic values and finitely many
planes. One plane supplies the affine-line stratum for infinitely many
values. On each such stratum its radial coordinate is an invertible
regular function, hence constant. These are infinitely many distinct
vertical lines, forcing the corresponding polynomial to be independent
of \(z\). Connectedness of its generic fibers then makes it linear in
the radial coordinate.

Choose coordinates so this distinguished line is \(x=0\), and write
the others as \(y=\alpha_jx\). The necessary restrictions are precisely
of the following form:
\[
\begin{aligned}
H(0,y,z)&=ay+b,\qquad a\ne0,\\
H(x,\alpha_jx,z)&=c_jx^{k_j}z+B_j(x),
\qquad c_j\ne0,\ k_j\geq1,\ B_j(0)=b.
\end{aligned}
\tag{12}
\]
To justify the second line, fix a generic level of one of its
punctured-line curves. Its projection to \(x\ne0\) is an isomorphism,
so for a general \(x\), its equation has exactly one simple root in
\(z\). The defining polynomial therefore has degree one in \(z\).
Its leading coefficient has no nonzero root, since such a root would
give an empty fiber or a whole vertical line. Hence the coefficient
is a nonzero scalar times \(x^{k_j}\). The constant axis imposes
\(k_j\geq1\).

The restrictions in (12) belong to the given polynomial \(H\).
No claim is needed that arbitrary independently chosen tuples
\((a,c_j,k_j,B_j)\) extend to such an \(H\); compatibility of restrictions
at a multiple intersection is not being discarded.

## 4. Every fiber satisfying (12) is affine three-space

Up to a nonzero scalar absorbed into \(u\), write
\[
P=x^{m_0}\prod_{j=1}^{d-1}(y-\alpha_jx)^{m_j}.
\tag{13}
\]
Assume only (12), without stability or a slice. Then for every
\(\lambda\in\mathbb C\),
\[
\mathbb C[x,y,z,u]/(Pu+H-\lambda)
\cong\mathbb C[x]^{[2]}.
\tag{14}
\]

First work over \(S=\mathbb C[x,x^{-1},y]\). Put
\(v_j=y-\alpha_jx\). The ideals \((v_j^{m_j})\) are pairwise comaximal
in \(S\), because \(v_i-v_j=(\alpha_j-\alpha_i)x\) is a unit.
Modulo \(v_j\), (12) makes \(H\) affine in \(z\) with unit leading
coefficient \(c_jx^{k_j}\). Write
\[
H=c_jx^{k_j}z+B_j(x)+v_jR_j(x,y,z).
\]
The finite inverse lemma constructs both compositional inverse
congruences modulo \(v_j^{m_j}\). The Chinese remainder theorem joins
these inverses into a single \(I(T)\in S[T]\) satisfying
\[
H(x,y,I(T))\equiv T\pmod P,
\qquad I(H(x,y,z))\equiv z\pmod P.
\]
Here the factor \(x^{m_0}\) of \(P\) is already a unit. The companion
\(V=(z-I(F))/P\) and inverse (8) now give
\[
\mathbb C[x,x^{-1},y,z,u]
=\mathbb C[x,x^{-1},y,F,V].
\tag{15}
\]
This checks all nonzero closed base fibers and the generic fiber over
\(\mathbb C(x)\) by one construction. At \(x=0\), (12) eliminates
\(y\), leaving \(\mathbb C[z,u]\) in every fiber \(F=\lambda\).

Therefore \(F\) is a residual \(x\)-plane in the exact sense of
Kaliman--Vénéreau--Zaidenberg: for every \(\gamma\in\mathbb C\), the
quotient by \(F(\gamma,y,z,u)\) is a polynomial plane. Their Theorem
4.23 applies because \(P\in\mathbb C[x,y]\) and
\(H\in\mathbb C[x,y,z]\). It gives (14), and in fact gives the same
conclusion for \(F-\lambda(x)\) with any
\(\lambda(x)\in\mathbb C[x]\).[^kvz]

There is also the classical affine-plane-fibration verification. The
polynomial \(Pu+H-\lambda\) is primitive and linear in \(u\): none of
the factors \(\ell_i\) of \(P\) divides \(H-\lambda\), by (12).
Its quotient ring is thus a domain containing \(\mathbb C[x]\), and
is flat over this PID because it is torsion free. It is finitely
presented. Equation (15), and the explicit plane at zero, verify the
polynomial fibers at every prime. Sathaye plus Bass--Connell--Wright
then give (14), using the exact published PID consequence sourced in
[the repeated-crossing slice proof](repeated-crossing-slice-descent.md).
This alternate route does not assume triviality over the
two-dimensional base \(\mathbb C[x,F]\).

## 5. The original slice hypothesis completes the proof

Let \(D(F)=1\) for an LND on the original ring
\(T=\mathbb C[x,y,z,u]\), and let \(K=\ker D\). The slice theorem gives
\[
T=K[F].
\tag{16}
\]
As explained in the linked slice proof, this also makes \(F\) a
one-stable coordinate, so Sections 1--3 apply.

In the nonconstant-axis branch, Section 2 directly proves coordinate
descent. In the constant-axis branch, (12)--(14) give
\(T/(F-\lambda)\cong\mathbb C^{[3]}\). But (16) identifies that same
quotient with \(K\). Thus \(K\cong\mathbb C^{[3]}\), and
\(T=K[F]\) exhibits \(F\) as a coordinate. This proves (1).

No assumption that the LND fixes the chosen base coordinate \(x\)
is needed. An LND slice on a stabilized ring would not supply (16)
for this original ring, which is why the last argument does not claim
the stronger stable-coordinate implication in the constant-axis branch.

The theorem covers \(P=xy(x+y)\), with arbitrary positive multiplicities
of its three factors, and every larger finite arrangement of distinct
concurrent lines. It does not cover nonconcurrent arrangements, curved
coefficient divisors, or slices without the displayed linear-in-\(u\)
presentation. The individual-rank bound in Section 3 comes from the
image of the integral residue map, not from its total rank or from
Euler characteristic alone.

## Source

[^kvz]: Shulim Kaliman, Stéphane Vénéreau, and Mikhail Zaidenberg,
[*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/html/math/0104204v2),
definition 4.19, Theorem 4.23, and proof 4.26. The theorem covers
residual \(x\)-planes \(f(x,y)u+g(x,y,z)\); proof 4.26 explicitly
gives the polynomial quotient over \(\mathbb C[x]\), including shifts
by an arbitrary polynomial in \(x\). This is the prior theorem used
for the fiber conclusion, with no novelty assertion.
