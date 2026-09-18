# Multifiber descent under a full embedded residual-line hypothesis

This note gives a finite, whole-ring alternating-shear certificate under
an explicit residual-line premise. It does not prove that premise for an
arbitrary stably polynomial threefold. Under the premise, the original
pair already has no joint fixed point: every shear below preserves the
joint fixed locus. Thus this is not a mechanism for removing existing
joint fixed points, nor a recognition regime asserted to be broader than
the separate no-joint-fixed-point route.

The construction uses the primitive Jacobian normalization in
[637](intrinsic-primitive-jacobian-normalization-pass637-working.md),
the actual intrinsic quotient and plinth results in
[the quotient note](intrinsic-quotient-surface-pass.md) and
[27](intrinsic-plinth-boundary-pass27.md), and the classical
Abhyankar-Moh-Suzuki degree theorem. The use of 637 is explicit; its
independent source audit is a separate dependency. No unfinished
companion source has been read for this note. There is no novelty claim.

## 1. Actual input and exact conclusion

Let \(A\) be an affine complex domain with an actual isomorphism

\[
A[u]\simeq\mathbb C^{[4]}.
\tag{1}
\]

Let \(P,Q\in\operatorname{LND}(A)\) be nonzero, commuting,
primitive, and independent over \(\operatorname{Frac}A\), with actual
kernel planes and common kernel

\[
\ker P=\mathbb C[f,g],\qquad
\ker Q=\mathbb C[f,h],\qquad
\ker P\cap\ker Q=\mathbb C[f].
\tag{2}
\]

The cross-values are nonzero elements of \(\mathbb C[f]\).
By 637 they are constant associates. Scale one derivation so that

\[
P(h)=Q(g)=d(f)\ne0.
\tag{3}
\]

One may instead include (3) directly in the input. The later use of
637 to preserve primitivity is still required. Let \(\Sigma\) be the
finite set of distinct roots of \(d\); root multiplicities are retained
in \(d\), but do not enter the interpolation polynomials.

For \(c\in\Sigma\), write \(F_c=f-c\) and
\(A_c=A/F_cA\). These are domains, as proved below. Bars at that
fiber denote actual residue classes. The additional hypothesis is that
there is \(t_c\in A_c\), transcendental over \(\mathbb C\), such that

\[
\mathbb C[\bar g,\bar h]=\mathbb C[t_c],\qquad
\operatorname{Frac}\ker(\bar P:A_c\to A_c)=\mathbb C(t_c).
\tag{4}
\]

Thus (4) specifies both the embedded joint polynomial line and its full
residual invariant function field. Merely having an abstractly normal
joint ring, or a polynomial subring with a smaller function field, is
not the hypothesis. The same full field is the invariant field of
\(\bar Q\); the argument in Section 2 proves this.

**Conditional conclusion.** Finitely many explicit invariant-dependent
shears, supported separately at the fibers in \(\Sigma\), produce a
primitive commuting pair with the same cross-value \(d\), whole kernel
planes, and at least one degree-one residual kernel generator at every
bad fiber. Polynomial coefficients in \(f\) then give a free intrinsic
LND. Consequently

\[
A=\mathbb C[f,v,s],\qquad A[u]=\mathbb C[f,v,s,u].
\tag{5}
\]

Here the coordinates \(v,s\) are an existence consequence of the slice
and plane theorems, not the output of an implemented coordinate solver.
The finite shear list and the free-action combination are explicit
once the data in (4) are supplied. No global
\(\mathbb C[f]\)-polynomial presentation of \(A\) is assumed.

## 2. Whole-ring and residual-field preliminaries

The cylinder in (1) makes \(A\) smooth, factorial, and contractible,
with units \(\mathbb C^*\). Its nonzero intrinsic LNDs have actual
plane kernels and principal full plinth ideals by the cited quotient
and plinth notes. These facts do not assume that \(A\) is already a
polynomial threefold.

For \(S=\ker P=\mathbb C[f,g]\), factorial closure makes every
\(F_c\) prime in \(A\). It is a nonunit because it is a nonunit in
the factorially closed subring \(S\). Moreover

\[
S\cap F_cA=F_cS.
\tag{6}
\]

Indeed, if an invariant is \(F_ca\), applying \(P\) gives \(P(a)=0\).
The same argument applies to the other kernel. In particular both
\(\bar g\) and \(\bar h\) are nonconstant. For example,
\(g-\alpha\in F_cA\) would, by (6), imply divisibility by
\(f-c\) in the actual polynomial plane \(\mathbb C[f,g]\).

Primitivity makes both induced LNDs on \(A_c\) nonzero. At a bad
fiber they kill both residues in (4). A nonzero LND on a domain of
dimension two has a transcendence-degree-one invariant field. The
constant field of a derivation in characteristic zero is relatively
algebraically closed in the ambient fraction field: differentiating
the minimal polynomial of an algebraic element proves this. Therefore
the full field \(\mathbb C(t_c)\) in (4) is relatively algebraically
closed in \(\operatorname{Frac}A_c\). Any other nonzero residual LND
that kills \(t_c\) has exactly this invariant field. This proves the
assertion about \(\bar Q\) and will also apply to every later pair.

The local-slice theorem gives the exact generic chart

\[
A_d=\mathbb C[f,d^{-1},g,h],\qquad
P=d\partial_h,\qquad Q=d\partial_g.
\tag{7}
\]

For instance \(h/d\) is a slice for \(P\) after localization. If
\(d\) is a nonzero constant, (7) already proves (5), and the rest
of the algorithm is empty. Henceforth allow \(\Sigma\ne\varnothing\).

## 3. A single fiberwise degree reduction lifts globally

The exact published input is the characteristic-zero degree theorem:
if two nonconstant one-variable polynomials generate the entire
one-variable polynomial ring, one of their degrees divides the other.
It is stated at the beginning of Makar-Limanov's
[primary proof of the AMS theorem](https://arxiv.org/pdf/1212.0163v1).
We use its degree statement, followed by leading-coefficient
cancellation, not a claim about an unknown global plane over
\(\mathbb C[f]\).

At a selected fiber \(c\), suppose both current residue degrees exceed
one. If \(\deg\bar h=m\deg\bar g\), choose \(a\in\mathbb C^*\)
so that subtracting \(a\bar g^m\) cancels the highest term of
\(\bar h\). Put

\[
F(T)=aT^m,\qquad
\ell_c(f)=\prod_{b\in\Sigma\setminus\{c\}}\frac{f-b}{c-b}.
\tag{8}
\]

The empty product is one. Define whole elements and whole derivations

\[
g'=g,\quad h'=h-\ell_cF(g),\qquad
P'=P,\quad Q'=Q+\ell_cF'(g)P.
\tag{9}
\]

Direct differentiation gives

\[
Q'(h')=0,\quad P'(g')=0,\quad
P'(h')=Q'(g')=d,\quad [P',Q']=0.
\tag{10}
\]

In (7), \(g,h'\) are polynomial coordinates and \(Q'=d\partial_g\)
with \(h'\) fixed. Thus \(Q'\) is locally nilpotent on \(A_d\).
It preserves \(A\), because (9) has whole coefficients. Every element
of \(A\) is therefore killed by some iterate already in \(A_d\), hence
in \(A\). Independence persists on (7). No extension of a formal
leading field is being promoted to an actual LND.

If the other degree divides instead, use the symmetric operation

\[
g'=g-\ell_cF(h),\quad h'=h,\qquad
P'=P+\ell_cF'(h)Q,\quad Q'=Q.
\tag{11}
\]

At \(c\), (9) is an elementary automorphism of the two residue
generators and strictly lowers their degree sum. At every other root
of \(d\), their residues are unchanged. The joint embedded ring in
(4) is unchanged everywhere. The changed residue cannot be constant
when the unchanged one has degree greater than one, because a single
polynomial of degree greater than one does not generate
\(\mathbb C[t_c]\). We stop at a fiber as soon as one degree is one;
we do not continue until a residue becomes constant.

## 4. Entire kernels, primitivity, and unchanged bad support

After (9), the localized kernel is
\(\mathbb C[f,d^{-1},h']\). To recover the whole kernel, take an
element of \(A\cap\mathbb C[f,d^{-1},h']\), and write it with a
minimal denominator consisting of powers of the \(F_b\).
If \(F_b\) occurs, its polynomial numerator lies in \(F_bA\).
Reduction modulo \(F_b\) gives a polynomial relation over
\(\mathbb C\) in the nonconstant residue \(\bar h'\). Since that
residue is transcendental, every coefficient vanishes. The numerator
is divisible by \(F_b\) already in \(\mathbb C[f,h']\), contradicting
minimality. Consequently

\[
\ker Q'=\mathbb C[f,h'],\qquad \ker P'=\mathbb C[f,g'].
\tag{12}
\]

The proof for (11) is identical. This also shows that no extra kernel
generators or new denominator support have been hidden by localization.
The intersection of the two whole kernels is still \(\mathbb C[f]\),
as is seen first on (7) and then by contraction.

Here is the precise 637 license used to keep the raw actions primitive.
Fix a global volume form and define \(J(f,a)\) by
\(\iota_{J(f,a)}\omega=df\wedge da\). The companion result says
that an LND with actual plane kernel \(\mathbb C[f,a]\) has a
primitive Jacobian \(J(f,a)\), and a primitive such LND is a nonzero
constant multiple of it. Equal cross-values in (3) therefore give

\[
P=\gamma J(f,g),\qquad Q=-\gamma J(f,h),
\qquad\gamma\in\mathbb C^*.
\tag{13}
\]

Equation (9) gives \(Q'=-\gamma J(f,h')\); (11) gives
\(P'=\gamma J(f,g')\). With the actual kernels (12), 637 makes
each of these primitive. In particular no division by a content
factor, and no subsequent renormalization of cross-values, is needed.

Each action continues to have a principal plinth generator dividing
\(d(f)\), because the opposite kernel generator has derivative \(d\).
In a polynomial kernel plane, every divisor of \(d(f)\) is itself a
polynomial in \(f\), up to a constant. All exceptional plinth support
thus remains among the original roots \(\Sigma\).

Finally, (9) and (11) are invertible elementary changes of the ordered
pair of derivations with determinant one over \(A\). Thus

\[
(P(A),Q(A))A=(P'(A),Q'(A))A.
\tag{14}
\]

Their joint fixed locus is unchanged, including at bad fibers. This
is an exact limitation of the method, not just a property of the example.

## 5. Finite termination and a free direction on each entire fiber

At every stage all residues remain in their original
\(\mathbb C[t_c]\), the joint ring remains that whole ring, and
both residue generators remain nonconstant. Hence the positive integer

\[
\mathcal C=\sum_{c\in\Sigma}
 \bigl(\deg_{t_c}\bar g+\deg_{t_c}\bar h\bigr)
\tag{15}
\]

strictly decreases at each operation. The other fibers' terms do not
change. The AMS step applies whenever a fiber is not yet finished,
so finitely many steps leave at least one degree-one residue at every
fiber. Multiple roots of \(d\) do not affect this termination argument.

Consider a finished fiber where \(\bar g\) has degree one. The
current \(P\) is primitive, so \(\bar P\ne0\). It kills \(t_c\).
The relative algebraic-closure argument of Section 2 shows that its
full invariant field is still exactly \(\mathbb C(t_c)\), whereas
its whole kernel plane has residual fraction field
\(\mathbb C(\bar g)=\mathbb C(t_c)\). The boundary invariant
degree of [27, Section 3](intrinsic-plinth-boundary-pass27.md) is
therefore one, so \(F_c\) does not divide the plinth of \(P\).
The same assertion holds for \(Q\) if \(\bar h\) has degree one.

For clarity, the direction of the plinth criterion needed here can be
checked with a whole minimal local slice. If \(P(r)=\rho\),
\(P(A)\cap\ker P=\rho\ker P\), and \(F_c\mid\rho\), then
\(\bar r\) is invariant. Boundary degree one permits \(a,b\in\ker P\),
\(F_c\nmid b\), with \(br-a=F_cz\). Differentiation gives
\(P(z)=b\rho/F_c\), contradicting minimality of \(\rho\).
This uses the full residual field, not only the joint residue ring.

The plinth generator is a polynomial \(\rho(f)\) dividing \(d(f)\).
Its nonzero value \(\rho(c)\) is the derivative of an actual element
at every point of the fiber. Thus the selected action has no fixed
point on the **entire** fiber, not just on a dense open subset.

## 6. Global free action and recognition

Partition \(\Sigma=\Sigma_P\sqcup\Sigma_Q\) by choosing, at each
fiber, an action just proved to be free there. If both work, choose
either one. Set

\[
a(f)=\prod_{c\in\Sigma_Q}(f-c),\qquad
b(f)=\prod_{c\in\Sigma_P}(f-c),\qquad
L=a(f)P+b(f)Q.
\tag{16}
\]

Empty products are one. The polynomials \(a,b\) are coprime.
The two summands are commuting LNDs with common-invariant coefficients,
so their sum is an LND, by the binomial iterate formula. On a selected
fiber it is a nonzero scalar multiple of the selected free action.
Off \(\Sigma\), equation (7) and coprimality make it nowhere zero.
Therefore \(L\) is a free intrinsic additive action.

The cylinder in (1) supplies smoothness and contractibility. The
intrinsic quotient theorem supplies the actual plane \(\ker L\).
Kaliman-Saveliev's
[Corollary 2.8(1)](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf)
then identifies the free action with translation on the product of its
quotient and a line. In particular \(L(s)=1\) for some whole \(s\),
and \(A=(\ker L)[s]\).

The restriction of \(P\) to the actual plane \(\ker L\) is a
nonzero LND: \(P,L\) are independent since \(b\ne0\). Its kernel
is exactly \(\ker P\cap\ker L=\mathbb C[f]\), because
\(L\) restricts to \(bQ\) on \(\ker P\). The plane LND theorem
of Rentschler, as used in the retained intrinsic notes, makes \(f\)
a coordinate of \(\ker L\). Thus \(\ker L=\mathbb C[f,v]\),
which proves (5). This is not an application of threefold cancellation.

The final pair has no joint fixed point, by its fiberwise construction
and by (7) off the bad fibers. Equation (14) proves the stronger
retrospective statement that the **original** pair already had no
joint fixed point. Accordingly the separate no-joint-fixed-point
geometric recognition route, if applied, is sufficient for recognition
on this input as well. The distinct output here is the finite
alternating-shear certificate and the explicit free action (16).

## 7. Whole polynomial control and exact limits

The accepted [634 control](saturated-pencil-no-free-direction-pass634-working.md)
illustrates a nontrivial step on the actual polynomial ring
\(A=\mathbb C[x,y,z]\). Put

\[
P_0=x\partial_y+2y\partial_z,\quad g=xz-y^2,\quad
h=2y-g^2,\quad Q_0=gP_0+\partial_z,
\quad P=P_0/2,\quad Q=Q_0.
\tag{17}
\]

These are whole primitive commuting LNDs with kernels
\(\mathbb C[x,g]\), \(\mathbb C[x,h]\) and equal cross-value \(x\).
At \(x=0\), the embedded joint ring is \(\mathbb C[y]\), the full
residual invariant field is \(\mathbb C(y)\), and the degrees are
\((2,4)\). With \(F(T)=-T^2\), the single step (9) gives

\[
h'=h+g^2=2y,\qquad Q'=Q-2gP=\partial_z.
\tag{18}
\]

The degree pair becomes \((2,1)\), and \(z\) is a whole slice. In 634
every member of the saturated \(\mathbb C[x]\)-span of the original
pair has a fixed point on \(x=0\); the coefficient \(g\) in (18) is
outside that restricted coefficient ring. This example licenses the
stated shear, not an automatic residue-line theorem.

The classical degree reduction, invariant-dependent shears, intrinsic
plinth criterion, and free-action recognition are not claimed as new.
In particular, the global-plane premise in modified-chain theorems over
a coefficient ring is not inserted into the unknown \(A\) here.
The archive's fixed-pivot and saturated-pencil failures remain valid.
This proof is conditional on (4), does not establish its necessity,
and does not supply it for arbitrary commuting actions or arbitrary
slice LNDs on four-space. A joint fixed point cannot disappear under
the permitted shears. General cancellation remains unsolved; priority
or novelty of this particular conditional formulation is not asserted.

## 8. Author verification and source boundary

The multifiber interpolation and endpoint were coordinated with the
parent investigation; this note supplies the whole kernel contraction,
residual-field persistence, and terminating certificate in one place.
Its main new input relative to an arbitrary commuting pair is expressly
the hypothesis (4), not a conclusion inferred from generic rank.

Author verification consists of a complete saved-source read through
this final paragraph and fresh unsaved algebra for (9)-(11), both
inverse coordinate shears on the actual localized chart, the Jacobian
update in (13), the interpolation values, and the entire control
(17)-(18). No saved checker is executed, imported, or modified. No
canonical file is changed. A HELD handoff requires independent review
of this source and the separate 637 dependency; it is not acceptance.
