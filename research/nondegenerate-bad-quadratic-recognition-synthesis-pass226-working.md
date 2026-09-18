# Recognition for the supplied nondegenerate bad-quadratic sector

Status: restricted working synthesis. The strict cofactor obstruction225
closes the last binary-quartic root pattern left by the previous exclusions.
Consequently every supplied full weight-four initial kernel whose quadratic
part in the two degree-two slots is nondegenerate reduces to the retained
fourth-power recognition theorem216.

This is not an entry theorem for an arbitrary sliced action, and it does
not prove the unrestricted complex-threefold cancellation conjecture.
The remaining fourth-power hypothesis class is not asserted to be nonempty.

## 1. Exact statement

Let the named capital letters be actual polynomial coordinates, and assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\theta_0:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]\longrightarrow A[T],
\quad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(aT,bT,eT^2,hT^2),\\
\ker\theta_0=(F).
\end{gathered}
\tag{1}
\]
Here \(T\) is independent. The polynomial \(F\) is irreducible and
homogeneous of weight four for weights \((1,1,2,2)\). Write it as
\[
F=Q_2(\mathsf Z,\mathsf W)
  +A_2(\mathsf X,\mathsf Y)\mathsf Z
  +B_2(\mathsf X,\mathsf Y)\mathsf W
  +C_4(\mathsf X,\mathsf Y),
\qquad \operatorname{rank}Q_2=2.
\tag{2}
\]
The subscripts on \(A_2,B_2,C_4\) denote homogeneous degrees in the good
variables, and zero terms are allowed. The full kernel equality in (1)
cannot be replaced by the single identity \(F(a,b,e,h)=0\).

**Working theorem.** Under (1)--(2), actual homogeneous polynomial
automorphisms put the full initial kernel into
\[
(\mathsf Z\mathsf W-\mathsf X^4).
\tag{3}
\]
In particular the retained recognition theorem216 applies:
\[
E \text{ fixes an ambient polynomial coordinate},\qquad
A\simeq\mathbb C^{[3]}.
\tag{4}
\]
The coordinate changes used to obtain (3) are complex linear changes of
the good slots, complex linear changes of the bad slots, and homogeneous
quadratic translations of the bad slots. No coefficient-field coordinate
is lifted to the original ring.

## 2. Completing the product is an actual automorphism

The classification in
[positive-bad-rank184](weight-four-positive-bad-rank-normal-forms-pass184-working.md)
gives a concrete reduction, recalled here. Over \(\mathbb C\), a
nondegenerate binary quadratic is a nonzero multiple of the product of two
independent linear forms. A constant invertible linear change of \(Z,W\),
and multiplication of the equation by a nonzero complex scalar, therefore
make the quadratic part \(ZW\).

Using the newly named coefficient forms, the equation is
\[
ZW+A_2(X,Y)Z+B_2(X,Y)W+C_4(X,Y)
=(Z+B_2)(W+A_2)-P_4,
\quad P_4=A_2B_2-C_4.
\tag{5}
\]
The actual change
\[
Z'=Z+B_2(X,Y),\qquad W'=W+A_2(X,Y)
\tag{6}
\]
fixes \(X,Y\). Its inverse subtracts the same two quadratics. Thus it
preserves the original polynomial ring, not merely its fraction field.
It transforms the equation into \(Z'W'-P_4(X,Y)\).
Irreducibility forces \(P_4\ne0\), since \(P_4=0\) would factor the
transformed equation.

Every new coordinate in these transformations is a nonzero homogeneous
source polynomial of weight one or two. Its image under the initial
evaluation cannot vanish: otherwise it would be a nonzero element of
the ideal \((F)\) with weight below four. A nonzero polynomial multiple
of the homogeneous polynomial \(F\) has no term of such a weight.
Consequently every transformed coordinate retains its exact E-degree,
and the profile remains \((1,1,2,2)\).

More precisely, a weight-preserving automorphism \(\psi\) of the formal
source ring gives the new initial map by composition with \(\psi\).
Its kernel is therefore \(\psi^{-1}((F))\). This transports the entire
ideal, not just the displayed relation. The global slice and the action
on the underlying ring have not changed.

The resulting actual frame hence satisfies
\[
\ker\theta'_0=(\mathsf Z\mathsf W-P_4(\mathsf X,\mathsf Y)),
\qquad P_4\ne0 .
\tag{7}
\]
The selected partial derivative, auxiliary derivation, coefficient field
and return polynomial need not equal those of the preceding frame.
Whenever a chart argument is used below it is rebuilt from the transformed
actual frame. No previous chart branch is transported without proof.

## 3. Exhausting the binary quartic

Factor \(P_4\) into four complex linear root forms, counted with
multiplicity. The five possible partitions of four have these dispositions:

| Root multiplicities | Complete retained working conclusion |
| --- | --- |
| \(1+1+1+1\) | Excluded by [cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md), independently of the earlier line proof221. |
| \(2+1+1\) | Excluded by the full cofactor and actual line argument222. |
| \(2+2\) | Excluded by [mixed nonrealizability220](mixed-quartic-line-nonrealizability-pass220-working.md), with its retained zero-return and conic inputs. |
| \(3+1\) | Excluded by [strict cofactor225](rank-two-strict-return-cofactor-obstruction-pass225-working.md), together with the precise [cubic frontier223](rank-two-triple-root-cubic-frontier-pass223-working.md). |
| \(4\) | Recognized by [synthesis216](rank-two-initial-kernel-recognition-synthesis-pass216-working.md) after the actual normalization below. |

These are exclusions of supplied actual frames with the full initial
kernel, not exclusions of formal leading data satisfying one equation.
For the mixed row, actual good linear changes and a constant bad scaling
reduce \(c\,l^2m^2\) to \(X^2Y^2\), where \(l,m\) are independent.
The exact-degree and full-ideal argument of Section2 applies to those
changes as well. The other exclusion statements already allow their
arbitrary projective root configurations.

The new step in the \(3+1\) row is worth separating from the older degree
comparison. In its exact coefficient field \(L\), the selected plane
component has an evaluated cofactor \(q_1\) and a return polynomial
\(R\ne0\). The full gradients and nonzero calibrated determinant give
\[
q_1\mid \frac{R^3}{\operatorname{rad}R}\quad\hbox{in }L[v],
\tag{8}
\]
where \(\operatorname{rad}R\) is the monic squarefree part.
The last surviving cubic would require \(\deg R=3\) and
\(q_1=cR^3\), \(c\in L^*\), contradicting (8). This is a polynomial
root-order proof, not a grid calculation or an assumption that the
projected curve is smooth. The saved225 proof records all cancellations.

The only remaining possibility is \(P_4=c\,l^4\), with \(c\ne0\) and
a nonzero complex linear form \(l\). Choose a constant linear complement
to \(l\), set the first new good coordinate equal to \(l(X,Y)\), and
use that complement as the second good coordinate. Divide \(Z\) by
the complex scalar \(c\), leaving \(W\) fixed. The actual inverse uses
the inverse constant good matrix and multiplication of \(Z\) by \(c\).
Equation (7) becomes (3). No root of a function-field coefficient
is extracted. Exact degrees and the full initial ideal remain preserved.

## 4. What supplies the original-ring conclusion

The conclusion (4) is precisely the retained theorem216 for the full
kernel \((ZW-X^4)\), not an inference from the rationality of a projected
curve. That synthesis treats the zero-return and constant-second branches
by original-ring recognition. It excludes the nonconstant-second branches
using the complete lower potentials, actual auxiliary derivations and
original coordinate changes.

Its final published endpoint requires a locally nilpotent derivation of
a polynomial four-variable ring to fix an ambient coordinate and to have
a regular kernel. These hypotheses, not just rationality, are essential.
Regularity here follows from \(B=A[u]\): equivalently \(A=B/(u)\),
and \(Eu=1\) makes that hypersurface smooth. The precise endpoint is
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1),
which was checked against the primary source during this synthesis.
The retained216 construction supplies the invariant coordinate before
this theorem is applied.

No independent reconstruction of every historical216 dependency is
claimed in this new note. This is an explicit composition of those
retained working results and the new225 obstruction.

## 5. Verification and the actual remaining gap

The positive-bad-rank184 normalization was read completely. Its actual
inverses, leading-degree preservation and full-ideal transport were
reconstructed here and checked separately by General.
The complete216 synthesis,222 cofactor source,223 cubic frontier and225
strict cofactor proof were reviewed for their statements and composition.
The mixed220 consequence was checked with its explicitly named
predecessor inputs. Earlier proofs are not silently expanded in scope.

This synthesis does not recognize quadratic bad rank zero or one,
height-two initial ideals, or higher E-time profiles. It does not prove
that every sliced action admits the supplied exact1122 frame. In
particular an algebraic normal form for a chosen full initial ideal is
not an existence theorem for such an ideal in an arbitrary action.

The remaining fourth-power sector is conditionally recognized, not
constructed. Thus this note neither asserts a nonempty new family of
examples nor a new historical theorem. Separate AI proof reconstructions
and finite algebra checks are not human expert review or proof-assistant
certification. No external contact, publication or submission is made.
