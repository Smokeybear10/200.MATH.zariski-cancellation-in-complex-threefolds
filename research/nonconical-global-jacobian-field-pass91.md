# The highest bad adjoint has a global primitive Jacobian factor

In the actual nonconical constant-acceleration frame, the highest
bad-coordinate adjoint equals \(2\Omega\) times an explicitly oriented
polynomial Jacobian derivation. This factor is itself a global LND,
not just a field on \(D(\Omega)\). It has no divisorial fixed locus.
Its remaining fixed points lie over finitely many closed points of
the actual invariant plane; they are not excluded here.

## 1. Actual hypotheses and orientation

Retain the actual setting and highest fields of
[cyclic-fiber90](nonconical-cyclic-fiber-omission-pass90.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad E=\partial_u,\quad
u=Ez/q,\quad q=E^2z\in\mathbb C^*,\quad E^2x_i=0\ (i\le3),\\
S=\ker(W|A)=\mathbb C[s_1,s_2],\quad Wu=0,\quad
b=(Ex_1,Ex_2,Ex_3)^t\in S^3,\quad
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0 .
\end{gathered}
\tag{1}
\]
The four displayed coordinates of B are original coordinates.
The retained intrinsic quotient theorem gives faithful flatness
of \(S\to A\), with purely one-dimensional nonempty fibers.
The common kernel S is factorially closed in the UFD B, so every
irreducible of S remains prime in both B and A. No additional
smoothness or reducedness of all closed fibers is assumed.

Write \(P=(b,qu)^t\), \(J=\operatorname{Jac}_xP\),
\(T=\partial_z\), and \(H=[E,[E,T]]\). The retained actual-flow
and highest-adjoint arguments give
\[
J^4=0,\quad JP=qe_4,\quad
H(x)=2J^2e_4=\frac2qJ^3P\ne0,\quad
[E,H]=0,\quad H(u)=0,\quad \ker(H|A)=S.
\tag{2}
\]
Here H is an actual LND, by highest-coefficient degeneration of
the conjugates of the original partial T. The nonconical condition
makes J regular nilpotent and H nonzero. This is not a statement
that the lower commutator \([E,T]\) is an LND.

Define the polynomial derivation N with the following fixed order:
\[
N(f)=\det\frac{\partial(s_1,s_2,u,f)}
 {\partial(x_1,x_2,x_3,z)}.
\tag{3}
\]
In particular N kills S and u. Its coefficient column is nonzero,
since \(s_1,s_2,u\) are algebraically independent in characteristic
zero. All the determinants in (3) are taken in B.

## 2. Cauchy--Binet gives the exact global factor

Put \(L=b_{s_1}\times b_{s_2}\), so \(L^tb=\Omega\), and factor
\[
U=[(b_{s_1},0)^t,(b_{s_2},0)^t,e_4],\qquad
V_0=\begin{pmatrix}ds_1\\ds_2\\du\end{pmatrix},\qquad
J=U\operatorname{diag}(1,1,q)V_0.
\tag{4}
\]
The coefficient \(N_i\) is
\((-1)^{4+i}\det(V_0\text{ with column }i\text{ omitted})\).
The signed minors \((-1)^j\det(U\text{ with row }j\text{ omitted})\)
are exactly the four entries of \((-L,0)^t\). Applying
Cauchy--Binet to each three-by-three minor of J therefore gives
\[
\operatorname{adj}(J)=-q\,N(x)(L,0),\qquad
J^3=-\operatorname{adj}(J),\qquad
\boxed{\ H=2\Omega N\ }.
\tag{5}
\]
The middle identity follows by comparing the adjugate polynomial
for the characteristic polynomial \(t^4\). The last identity follows
from \(J^3P=q\Omega N(x)\) and (2). Thus the positive sign in (5)
uses precisely the row order in (3); it is not chosen from an example.

Since \(N\Omega=0\), repeated application to any element of B gives
\(H^m f=(2\Omega)^mN^m f\). The ring is a domain and H is locally
nilpotent, so N is locally nilpotent on all of B. Also
\([E,H]=2\Omega[E,N]=0\), since \(E\Omega=0\). Hence
\[
N\in\operatorname{LND}(B),\qquad [E,N]=0,\qquad Nu=0,\qquad
0\ne N|_A\in\operatorname{LND}(A),\qquad \ker(N|_A)=S.
\tag{6}
\]
None of these conclusions requires inverting \(\Omega\).

## 3. The Jacobian factor has no coefficient divisor

Let g be a gcd in B of the four coefficient entries of N,
omitting zero entries, and write \(N=gD\) with D polynomial and
coefficient gcd one. The inclusion \(N(B)\subseteq gB\) implies
\(N(g)\in gB\), so local-nilpotent self-divisibility gives \(Ng=0\).
The identity \([E,N]=0\) gives
\(E(g)D_i+g[E,D]_i=0\) in every original coordinate. Coprimality
of the entries of D forces \(g\mid E(g)\). The same LND fact for
E gives \(Eg=0\). Consequently \(g\in\ker N\cap\ker E=S\).

Suppose an irreducible \(p\in S\) divides g. Then p remains prime
in B, and all three-by-three minors of \(V_0\) vanish modulo p.
We show that this is impossible at the generic point of that
divisor. Choose \(\ell\) to be \(s_1\) or \(s_2\) such that
\[
dp\wedge d\ell=\epsilon\,ds_1\wedge ds_2,
\qquad \epsilon\in S\setminus(p).
\tag{7}
\]
Such a choice exists because at least one base partial derivative
of the nonconstant irreducible p is nonzero modulo p. With this
choice, the residue of \(\ell\) is transcendental over C in
\(\operatorname{Frac}(S/(p))\). Otherwise p would be a constant
multiple of \(\ell-\alpha\), contradicting the choice in (7).

Set \(K_p=\operatorname{Frac}(B/pB)\). The injection \(S/(p)\to A/pA\)
and \(B/pB=(A/pA)[u]\) show that the residues of \(\ell,u\) are
algebraically independent. Their differentials are therefore
independent in \(\Omega_{K_p/\mathbb C}\). The ambient conormal
sequence at this generic point has kernel \(K_p\,dp\), and dp is
nonzero: in characteristic zero an irreducible polynomial p in
the original coordinates does not divide all its own partials.
It follows that \(dp,d\ell,du\) are independent in
\(\Omega_{B/\mathbb C}\otimes_B K_p\). Equation (7) now contradicts
the vanishing of \(ds_1\wedge ds_2\wedge du\) modulo p.

Thus g is a complex unit. In particular N has no divisorial fixed
locus in B. Its restriction to A is primitive as well: if a prime
of the UFD A divided every value on A, it would divide every value
on \(B=A[u]\), since Nu=0, contrary to the coefficient gcd just proved.
This does not say that the coefficient or value ideal is the unit ideal.

## 4. Fixed points can occur only over finitely many base points

Fix an irreducible \(p\in S\), put \(V=S_{(p)}\) and
\(k=\operatorname{Frac}(S/(p))\). The whole generic divisor fiber
\(\bar A=A_V/pA_V\) is a nonzero one-dimensional affine k-domain.
The induced derivation \(\bar N\) is nonzero. Otherwise all values
on A would belong to \(pA_V\cap A=pA\), and then p would divide
all original coefficient entries of N, contrary to Section 3.

A nonzero LND of a one-dimensional affine characteristic-zero
k-domain has a slice. Indeed, choose a local-slice element a with
\(D^2a=0\) and \(Da\ne0\). The nonzero invariant Da is algebraic
over k, so its inverse is a polynomial in Da over k and already
lies in the domain. Thus \(a/(Da)\) is a slice. The slice theorem
identifies the domain with \(k'[t]\), where the invariant field
k' is finite over k, since it is an algebraic finitely generated
k-algebra. In particular \(\bar N\) has no fixed points on this
whole generic divisor fiber. The generic fiber has the same property.

Let \(Z\subset\operatorname{Spec}A\) be the closed fixed locus of
N. The generic point of each of its finitely many irreducible
components must map to a height-two prime of S: the fibers over
the generic point and every height-one point have just been excluded.
Its entire component therefore lies over that closed point. We obtain
\[
\gcd_B N(x)=1,\qquad
N|_A\text{ primitive},\qquad
\operatorname{image}(Z\longrightarrow\operatorname{Spec}S)
\text{ is a finite set of closed points}.
\tag{8}
\]
The image may be empty. No bound on its cardinality and no exclusion
of positive-dimensional fixed sets inside those closed fibers is asserted.

This finite set is contained in \(V(\Omega)\). Indeed, the actual
fixed-point-free LND D from
[open-free90](nonconical-open-free-derivation-pass90.md) acts on
\(A_\Omega\) with kernel \(S_\Omega\). On \(A_K=K[v]\), where
\(K=\operatorname{Frac}S\), both D and N are nonzero K-LNDs and hence
constant translations. Thus \(D=\lambda N\) with \(\lambda\in K^*\).
Primitivity of N in the localized UFD \(A_\Omega\) forces
\(\lambda\in A_\Omega\): an irreducible denominator would divide
every value of N. Its kernel membership then gives
\(\lambda\in A_\Omega\cap K=S_\Omega\). The unit value ideal of D
forces \(\lambda\) to be a unit and the value ideal of N to be the
unit ideal as well. Consequently N itself is fixed-point-free on
\(A_\Omega\), not only a rational multiple of a free field there.

The general whole-scheme nonvanishing statement was already proved
in [primitive-fiber54](primitive-fiber-nonvanishing-pass54.md),
including its stronger closed-fiber result using the transverse socle
theorem. That complete retained note was reread here. It is not a
new lemma of this pass, and its selected original source proofs are
not freshly audited here. Nonzero action on a nonreduced closed
fiber must not be promoted to nonzero action on its reduction.

For the retained boundary, use \(A_0=\mathbb C[x,y,z]\),
\(S_0=\mathbb C[x,xz-y^2]\), \(B_0=A_0[u]\), and
\(N_0=x\partial_y+2y\partial_z\). It is exactly the Jacobian field
of \(x,xz-y^2,u\) in the order \(x,y,z,u\). Its coefficient gcd is
one, but its fixed line \(x=y=0\) lies over the origin of S0.
The whole origin fiber is \(\mathbb C[y,z]/(y^2)\), where
\(\bar N_0(z)=2y\ne0\); every point of the reduced fiber is fixed.
This reused quotient example is not asserted to realize an original
three-good-coordinate constant-acceleration frame.

## 5. Verification and scope

Root proposed the exact global factor and the generic-divisor
translation consequence. Jet reconstructed the cofactor orientation,
global LND transfer, and coefficient-gcd proof. General independently
checked the conormal outline before the complete note was saved.
The new content is the identification of this particular global
primitive field in the actual frame. The general curve-LND and
primitive-fiber facts are not claimed as novel.

The separate [checker](nonconical_global_jacobian_checks_pass91.py)
tests the formal Cauchy--Binet sign, the actual retained inverse frame,
and the reused fixed-line boundary. These finite identities do not
certify the arbitrary-ring arguments or prove freeness. Its first
standalone run passed one method in 0.145 seconds, exit zero, with
complete output in tool chunk 888037. No assertion failed. The first
saved-file reread caught lost inline math delimiters and one escaped
thin-space in the prose; these transcription issues were corrected
before independent saved-file review, with all eight displayed
equations unchanged. No general
recognition, source novelty, full regression or changes to pass90
and earlier files are claimed.
