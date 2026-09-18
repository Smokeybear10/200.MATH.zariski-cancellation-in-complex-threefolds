# Two translation quotients preserve the fixed scheme

For a slice extension \(E=D+f\partial_t\), the intrinsic action
induced by \(\partial_t\) does not remove the fixed points of \(D\).
In fact their fixed-point schemes are canonically isomorphic over the
common invariant ring, including nilpotents. Their plinth ideals have
the same radical. Thus, for a rank-three base derivation, trying to
prove that this particular intrinsic action is free cannot close the
kernel: that action is necessarily nonfree.

This is a comparison theorem for the given commuting pair. It neither
precludes a different free action on the kernel nor identifies an
exotic kernel. The fixed-scheme result uses the two actual slice
presentations and does not assume that the kernel is polynomial.

## 1. Setup and notation

Let
\[
R=\mathbb C[x_1,x_2,x_3],\qquad B=R[t],
\qquad 0\ne D\in\operatorname{LND}(R),
\]
and let
\[
E=D+f\partial_t\quad(f\in R),\qquad U=\partial_t.
\tag{1}
\]
Suppose \(E\) has a polynomial slice \(s\). Set
\[
K=\ker E,\qquad C=\ker D,
\qquad d=U|_K,\qquad q=U(s).
\]
Commutation gives
\[
B=K[s],\qquad q\in K,\qquad U=d+q\partial_s,
\qquad \ker d=K\cap R=C.
\tag{2}
\]
The common invariant ring \(C\cong\mathbb C^{[2]}\) is supplied
by Miyanishi's theorem for the nonzero base LND, as recalled in
[Dasgupta and Gaifullin, Theorem 2.8](https://arxiv.org/pdf/2306.00510).
No identification of \(C\) with an ambient coordinate plane is made.

For a derivation \(L\) of an algebra \(A\), write
\[
I_L=(L(A))A.
\]
For an LND in characteristic zero, \(\operatorname{Spec}(A/I_L)\)
is its scheme-theoretic fixed locus: the higher coefficients of
\(\exp(\tau L)(a)-a\) already belong to this ideal. Thus put
\[
F_D=\operatorname{Spec}(R/I_D),\qquad
F_d=\operatorname{Spec}(K/I_d).
\]
These schemes may be empty or nonreduced.

## 2. The full rank-drop ideal is independent of the presentation

Define an ideal in \(B\), without choosing generators of \(K\), by
\[
J=(E(a)U(b)-U(a)E(b):a,b\in B)B.
\tag{3}
\]
This is the coefficient ideal of \(E\wedge U\), or equivalently
the ideal obtained by evaluating that alternating biderivation on
all pairs of Kähler differentials.

In \(B=R[t]\), terms involving \(f\partial_t\) cancel, and
\[
E(a)U(b)-U(a)E(b)
=D(a)\partial_t b-(\partial_t a)D(b),
\]
where \(D\) is extended by \(D(t)=0\). Each term belongs to
\(I_D B\). Taking \(a=r\in R\), \(b=t\) gives \(D(r)\),
so \(J=I_D B\).

In \(B=K[s]\), extend \(d\) by \(d(s)=0\). The \(q\)-terms
likewise cancel, giving
\[
E(a)U(b)-U(a)E(b)
=(\partial_s a)d(b)-d(a)\partial_s b.
\]
This belongs to \(I_dB\). Taking \(a=s\), \(b=k\in K\)
gives \(d(k)\). Consequently
\[
\boxed{I_D R[t]=J=I_dK[s].}
\tag{4}
\]
This proves the equality of ideals, not only equality of their zero
sets. It uses neither a polynomial coordinate system on \(K\) nor
a section of \(\operatorname{Spec}K\to\operatorname{Spec}C\).
In particular, \(d\ne0\), since otherwise (4) would force \(D=0\).

At once,
\[
(R/I_D)[t]\cong (K/I_d)[s]
\tag{5}
\]
as \(C\)-algebras. The fixed schemes have isomorphic cylinders.
The slice supplies more than this stable comparison.

## 3. The fixed schemes themselves are canonically isomorphic

Let \(\overline B=B/J\), and view
\(\overline R=R/I_D\) and \(\overline K=K/I_d\) as subrings
of \(\overline B\). Their embeddings follow from the polynomial
presentations in (4). Both \(E\) and \(U\) preserve \(J\).
If \(J=B\), both fixed schemes are empty and the comparison is
immediate; otherwise use the following calculation.

In \(\overline B=\overline R[t]\), the induced derivation is
\[
\overline E=\overline f\partial_t,
\]
because every \(D(r)\) vanishes in \(\overline R\).
The original slice gives
\[
\overline f\,\partial_t\overline s=1.
\tag{6}
\]
Comparing constant terms as polynomials in \(t\) proves that
\(\overline f\) is a unit of \(\overline R\), even if this ring
has nilpotents. Equation (6) then implies
\[
\overline s=\overline f^{-1}t+\overline h,
\qquad \overline h\in\overline R.
\tag{7}
\]
Every positive integer is invertible, so no higher power of \(t\)
can occur. In particular
\(\ker\overline E=\overline R\).

On the other hand, \(\overline B=\overline K[\overline s]\)
and \(\overline E=\partial_{\overline s}\), whence
\(\ker\overline E=\overline K\). Therefore the two embedded
subrings agree:
\[
\boxed{R/I_D\cong K/I_d\quad\text{as }C\text{-algebras}.}
\tag{8}
\]
The isomorphism is the one induced by their equality inside
\(B/J\); it is independent of any choice of curve-cancellation
theorem. This proof is why (8), unlike a general cancellation of
the variables in (5), is justified.

Thus all scheme structure of the fixed locus is retained: reducedness,
dimension, irreducible and connected components, their intersections,
and nilpotent multiplicities. Its scheme-theoretic image in the common
base is also identical, since
\[
I_D\cap C=J\cap C=I_d\cap C.
\tag{9}
\]
On the common fixed scheme, \(\overline q=\overline f^{-1}\).
Geometrically the two nonvanishing ambient fields become proportional
there, with reciprocal unit coefficients. The original slice only
forces \(f\) to be invertible on \(F_D\); it does not remove
\(F_D\).

## 4. A rank-three base makes this intrinsic action nonfree

For an additive action over \(\mathbb C\), a nontrivial stabilizer
is the whole group, since \(\mathbb G_a\) has no nontrivial finite
algebraic subgroups. Thus absence of fixed points is equivalent to
freeness. Equation (8), or already (4) and faithful flatness of
polynomial extensions, gives
\[
d\text{ is free}\quad\Longleftrightarrow\quad D\text{ is free}.
\tag{10}
\]

The precise primary input for the base is
[Kaliman, *Free C+-actions on C3 are translations*, Theorem 1](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf):
every free algebraic additive action on \(\mathbb C^3\) is a
translation in a polynomial coordinate system. It applies to the
actual base \(\operatorname{Spec}R=\mathbb A^3\), not to an
unrecognized threefold. Such a \(D\) has rank one.

Consequently,
\[
\operatorname{rank}D=3\quad\Longrightarrow\quad F_D\ne\varnothing
\quad\Longrightarrow\quad F_d\ne\varnothing.
\tag{11}
\]
This conclusion is independent of \(f\) and of the chosen slice.
It rules out the proposed step of making this induced \(d\) free
by analyzing the properness of the \(E\)-action. It does not rule
out a different free action on \(K\), nor does it imply that \(K\)
is nonpolynomial.

## 5. The plinth ideals have identical reduced support

Define ideals in the common invariant ring by
\[
P_D=D(R)\cap C,
\qquad P_d=d(K)\cap C.
\]
Then
\[
\boxed{\sqrt{P_D}=\sqrt{P_d}\quad\text{in }C.}
\tag{12}
\]

For a nonzero \(g=D(r)\in P_D\), the local slice theorem gives
\[
R_g=C_g[\rho],\qquad \rho=r/g,\qquad D(\rho)=1.
\]
Write \(f\in C_g[\rho]\), and integrate it as a polynomial in
\(\rho\): choose \(F\in C_g[\rho]\) with \(D(F)=f\).
Then
\[
v=t-F,\qquad E(v)=0,\qquad U(v)=1,
\]
and
\[
B_g=C_g[\rho,v],\qquad K_g=C_g[v],\qquad d(v)=1.
\tag{13}
\]
Clearing an invariant power of \(g\) in \(v\in K_g\) gives
\(k\in K\) with \(d(k)=g^N\) for some \(N\ge0\).
Thus \(g\in\sqrt{P_d}\).

Conversely, for nonzero \(h=d(k)\in P_d\), write
\(K_h=C_h[\eta]\) with \(d\eta=1\). In
\(B_h=C_h[\eta,s]\), integrate \(q\in C_h[\eta]\) to obtain
\(Q\) with \(dQ=q\). The element \(w=s-Q\) satisfies
\(U(w)=0\) and \(E(w)=1\), so
\(R_h=C_h[w]\) and \(D(w)=1\). Clearing denominators gives
a power of \(h\) in \(P_D\), proving the other containment.

This compares the base opens on which the specified actions are
translations. It does not identify the two plinth ideals with their
multiplicities, and it does not identify them with the fixed-image
ideal in (9). Those ideals can differ even for elementary examples.

## 6. Quotient fibers: what the common cylinder does preserve

For every closed point \(p\in\operatorname{Spec}C\), set
\[
A_p=R\otimes_C\kappa(p),\qquad L_p=K\otimes_C\kappa(p).
\]
Base change of the two polynomial presentations gives an exact
scheme-theoretic comparison
\[
A_p[t]\cong L_p[s].
\tag{14}
\]
In this setting the fibers are nonempty curves. For the polynomial
base this follows from
[Kaliman and Saveliev, Lemma 2.1(1)](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
applied to the smooth contractible threefold \(\mathbb A^3\).
Miracle flatness over the smooth plane \(\operatorname{Spec}C\)
then gives faithful flatness of \(C\to R\): the source is regular
and the fiber dimension is one. The exact local criterion is
[Stacks Project, Lemma 10.128.1](https://stacks.math.columbia.edu/tag/00R4).
Flatness of \(C\to K\) descends from \(B=R[t]=K[s]\), and
surjectivity follows from (14).

Equation (14) preserves reducedness, regularity, connectedness, and
the number and dimensions of irreducible components. It also preserves
the generic length on each component: at a minimal prime, adjoining
a polynomial variable gives a flat local extension with residue-field
extension, which retains the length of the zero-dimensional local
ring. Thus one cannot use the new quotient to make a multiple fiber
reduced, or a disconnected fiber connected.

No general isomorphism \(A_p\cong L_p\) is asserted here. Unlike
the fixed-scheme calculation, the induced \(D\) need not vanish
on an entire quotient fiber, so the proof of (8) cannot simply be
repeated. No section of either quotient morphism is assumed.

## 7. Proper ambient slices allow disconnected and multiple fibers

Take the elementary base derivation
\[
D=x\partial_y+2y\partial_z,
\qquad C=\mathbb C[x,v],\qquad v=xz-y^2,
\]
and let \(E=D+\partial_t\), with slice \(s=t\). Its invariant
coordinates are
\[
X=x,\qquad Y=y-xt,\qquad Z=z-2yt+xt^2.
\tag{15}
\]
Their inverse is \(x=X\), \(y=Y+Xt\),
\(z=Z+2Yt+Xt^2\). Thus \(K=\mathbb C[X,Y,Z]\), and
\[
d=-X\partial_Y-2Y\partial_Z,
\qquad v=XZ-Y^2.
\]
Here the base plinth ideal is \((x)\), while the fixed-image ideal
is \((x,v)\). For the first assertion, the plinth ideal is principal
by the exact statement recalled in
[Dasgupta and Gaifullin, Theorem 2.10(ii)](https://arxiv.org/pdf/2306.00510);
it contains \(D(y)=x\), and cannot be the unit ideal because the
action has fixed points. The second assertion follows by reducing
\(C=\mathbb C[x,v]\) modulo \(I_D=(x,y)\).
The fixed schemes are \(\operatorname{Spec}\mathbb C[z]\) and
\(\operatorname{Spec}\mathbb C[Z]\), and (8) identifies \(z\)
with \(Z\). At base points \(x=0,v=\beta\ne0\), each quotient
fiber is two disjoint affine lines. At \(x=v=0\), each is a
double affine line, with ring \(\mathbb C[y,z]/(y^2)\) or its
\((Y,Z)\) counterpart.

Here \(E\) is explicitly a translation, hence its action is proper,
while the specified intrinsic action has fixed points and the quotient
has disconnected and nonreduced fibers. This is not a rank-three
example, but the nonfreeness issue persists in that exact scope:
for any rank-three \(D\), taking \(f=1\) gives polynomial invariant
coordinates \(\exp(-tD)(x_i)\). Under this isomorphism of \(K\)
with \(R\), the induced \(d\) is \(-D\), so it is still rank
three and nonfree. No expansion of a particular rank-three flow is
needed for that certificate.

## 8. Remaining action and verification boundary

The next action cannot be to prove that \(U|_K\) is free for a
rank-three base. Equations (8) and (11) disprove that premise for
every extension in the stated class. A successful further argument
must instead produce a different intrinsic action, an ambient invariant
coordinate, or a gluing/embedding theorem that recognizes \(K\)
despite the retained exceptional fibers and fixed scheme.

The fixed scheme, its base image, the reduced plinth support, and the
stable fiber geometry now have explicit comparison laws. They constrain
the given pair but do not by themselves construct the missing ambient
coordinate. There is no general cancellation or novelty claim.

An independent inline SymPy run with `/opt/anaconda3/bin/python`
passed 12 grouped exact checks in 0.044 seconds. The controls verify
the two-sided gauge inverse, ambient and intrinsic derivations, common
quotient function, all six rank-drop minors, equality of the pulled-back
fixed ideals, the actual fixed-line identification, and the two special
fiber rings. A separate nonreduced fixed-scheme control uses
\(D=x^2\partial_y\), \(f=1+xy\), and the coordinate slice from
[the arbitrary-coefficient pass](arbitrary-coefficients-pass.md).
Modulo \(x^2\), it verifies \(\overline f^{-1}=1-xy\), the affine
formula (7), and the two-sided change
\(\overline Y=y+xy^2/2\), \(y=\overline Y-x\overline Y^2/2\).
These checks do not substitute for the arbitrary-kernel ideal proof.
