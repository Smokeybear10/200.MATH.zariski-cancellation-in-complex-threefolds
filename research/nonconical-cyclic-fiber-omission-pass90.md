# The nonconical frame has no common rational invariant with the last partial

In the actual three-good-coordinate constant-acceleration frame, a
nonzero velocity determinant makes four concrete derivations independent
over the original rational-function field. Consequently the action and
the original last coordinate partial have no common nonconstant rational
invariant. This also excludes collapse of both relative generators on
any whole generic divisor fiber of the invariant plane.

These are necessary properties of the nonconical frame. They do not
identify the kernel as a polynomial three-ring.

## 1. Actual hypotheses and the cyclic vector

Use the actual constructions in
[invariant-plane88](constant-acceleration-invariant-plane-pass88.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad Eu=1,\\
P=E(x_1,x_2,x_3,z)^t=(b,qu)^t,\quad q\in\mathbb C^*,\\
S=\ker(W|A)=\mathbb C[s_1,s_2],\quad Wu=0,\quad b\in S^3,\quad
\Omega=\det[b,b_{s_1},b_{s_2}]\ne0 .
\end{gathered}
\tag{1}
\]
Here the displayed four coordinates are original polynomial coordinates,
and E and W are actual locally nilpotent derivations. The retained
[three-good-frame proof87](constant-acceleration-three-good-frame-pass87.md)
gives \(J^4=0\), \(JP=qe_4\), and
\(\operatorname{ad}_E^j(T_i)(x)=(-1)^j j!J^j e_i\), where J is the
Jacobian of P in those original coordinates.

Write \(F=\operatorname{Frac}(B)\). The chain rule factors J through
the three columns \((b_{s_1},0)^t,(b_{s_2},0)^t,e_4\) and the three
rows \(ds_1,ds_2,q\,du\). Both factors have rank three over F:
\(\Omega\ne0\) gives independence of the columns, and \(s_1,s_2,u\)
are algebraically independent in characteristic zero. Therefore
\[
\operatorname{rank}_F J=3,\qquad
\operatorname{im}_F J
=\operatorname{span}_F\{(b_{s_1},0)^t,(b_{s_2},0)^t,e_4\},
\qquad P\notin\operatorname{im}_F J .
\tag{2}
\]
The last assertion follows from independence of \(b,b_{s_1},b_{s_2}\).

A nilpotent four-by-four matrix of rank three has one Jordan block
of length four. Every vector outside its image is cyclic. This can
be checked in a Jordan basis: the component on the last vector of
the Jordan chain is nonzero, so successive images form a basis.
Thus \(P,JP,J^2P,J^3P\) are independent over F.

## 2. Four actual fields and their common rational kernel

Let \(T=\partial_z\) be the original coordinate partial and use the
commutator convention \([D_1,D_2]=D_1D_2-D_2D_1\). Set
\[
Q=[E,T],\qquad H=[E,Q],\qquad
Q(x)=-Je_4,\quad H(x)=2J^2e_4,\qquad
\det(E(x),T(x),Q(x),H(x))
=-\frac{2}{q^3}\det(P,JP,J^2P,J^3P)\ne0 .
\tag{3}
\]
The determinant formula uses \(e_4=JP/q\). It proves generic
independence, not a unit determinant or pointwise independence.

If \(f\in F\) satisfies \(Ef=Tf=0\), both Q and H also kill f by
the definition of a commutator. Its row of four original partial
derivatives annihilates the invertible matrix in (3), and hence is
zero. In a characteristic-zero rational-function field over
\(\mathbb C\), a function with all four partial derivatives zero
belongs to \(\mathbb C\). In particular,
\[
\boxed{\quad
\ker(E|F)\cap\ker(T|F)=\mathbb C,\qquad
A\cap\mathbb C[x_1,x_2,x_3]=\mathbb C .
\quad}
\tag{4}
\]
This argument does not require Q to be locally nilpotent.
The [actual commutator control90](nonconical-higher-commutator-control-pass90.md)
shows that Q need not be locally nilpotent even in this frame.

For completeness H is a nonzero actual highest adjoint of T.
Indeed \(J^3e_4=J^4P/q=0\), whereas \(J^2e_4=J^3P/q\ne0\).
The highest-adjoint degeneration in invariant-plane88 therefore
proves local nilpotence of H. Also \([E,H]=0\), \(H(P)=0\), and
\(H(u)=0\). Its coefficient column and that of the chosen W are
nonzero vectors in the same one-dimensional space \(\ker_F J\).
They are nonzero rational multiples of one another, so their
kernels on A coincide with S. None of these facts makes Q an LND.

## 3. Both generators cannot collapse on a whole divisor fiber

Retain the actual completed relative reconstruction:
\[
\begin{gathered}
[b,v_2,v_3]\in\operatorname{GL}_3(S),\qquad
x_{\rm tr}=b(u-h)+v_2A_1+v_3A_2,\\
R=S[A_1,A_2],\quad A=R[c],\quad h\in A,\qquad
z=c+\frac q2(u^2-h^2).
\end{gathered}
\tag{5}
\]
The [universal-pencil proof88](universal-generator-pencil-pass88.md)
establishes that \(h\otimes1-1\otimes h\) is nilpotent in
\(A\otimes_R A\), with no reducedness assumption.

Let \(p\in S\) be irreducible, \(D=S_{(p)}\), and
\(k=\operatorname{Frac}(S/(p))\). The whole generic divisor fiber
\(\overline A=A_D/pA_D\) is a nonzero domain of dimension one.
Here are the required gates. The common LND kernel
\(S=\ker E\cap\ker W\) is factorially closed in the UFD B, so p
remains irreducible and hence prime in B. The presentation \(B=A[u]\)
makes \(pA\) prime too. Faithful flatness of \(S\to A\) and its
purely one-dimensional fibers, established in invariant-plane88,
give nonemptiness and the stated dimension after localization.

Suppose both residues \(\overline A_1,\overline A_2\) were algebraic
over k. Their generated domain \(k'=k[\overline A_1,\overline A_2]\)
is a finite field extension of k. Since \(\overline A=k'[\overline c]\)
has dimension one, \(\overline c\) is transcendental over k'.
Thus \(\overline A\) is the polynomial ring \(k'[\overline c]\),
not merely a selected component of the divisor fiber.

The natural map from \(A\otimes_R A\) to
\(\overline A\otimes_{k'}\overline A=k'[c_1,c_2]\) carries the
nilpotent tensor difference of h to zero, because this target is a
domain. A polynomial in c whose evaluations at two independent
variables agree is constant. Hence \(\overline h\in k'\).

Now \(\overline B=k'[c,u]\). Applying its k'-derivation
\(\partial_c\) to the reconstruction (5) gives
\(\partial_c\overline x_i=0\) for \(i\le3\) and
\(\partial_c\overline z=1\). Thus for every polynomial in the four
original coordinates, this derivative equals its original
z-derivative followed by reduction. Since p reduces to zero,
\(Tp\in pB_D\). The prime \(pB\) is disjoint from the inverted
elements of \(S\setminus(p)\), so \(Tp\in pB\) before localization.
Ordinary z-degree, or local-nilpotent self-divisibility, then implies
\(Tp=0\). This contradicts (4), since \(Ep=0\) and p is nonconstant.
We have proved
\[
\boxed{\quad
\operatorname{trdeg}_{\,k}
 k[\overline A_1,\overline A_2]=1
\quad\text{for every irreducible }p\in S .
\quad}
\tag{6}
\]

This extends the whole-fiber argument of
[pole-support89](constant-acceleration-pole-support-pass89.md)
to the actual three-relative-generator case. It does not say that
both residues are transcendental, or that the residue field k'
in an intermediate argument would have to equal k.

## 4. What is still missing

Equation (6) concerns the image of R in the whole A-divisor fiber.
It does not identify that image with \(R_D/pR_D\): the kernel can
be larger than \(pR_D\). In particular it does not prove that pR
is prime, that all components of an R-fiber are hit, that R is
normal, or that \(R\to A\) is finite or faithfully flat.

The [quadratic-potential proof90](nonconical-quadratic-potential-pass90.md)
separately proves \(A_\Omega=R_\Omega\). On the remaining divisor
\(\Omega=0\), the noncollapse in (6) is additional control, not
descent across that divisor or recognition of A.

Root supplied the cyclic-vector and whole-fiber arguments.
Jet independently reconstructed the determinant and common rational
kernel before this note was saved. The extension to the three-generator
whole fiber is written out here for separate full-file review.
The cited predecessor proofs were read through EOF for their actual-ring
hypotheses. No new external classification result, numerical proof,
novelty claim, or edit to pass89 or earlier files is part of this note.
