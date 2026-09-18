# Residue-independent finite pieces of a flat module are pure

The needed contraction is valid for every ideal, including a
nonreduced parameter ideal. The ambient flat module need not be
finite. In the actual full-Artin branch this permits coefficient
extraction modulo J squared, not merely modulo the square of
the maximal ideal.

## 1. The local module statement

Let (R,m) be any local ring with residue field k. Let M be an
arbitrary flat R-module and let f_1,...,f_n in M have linearly
independent images in M/mM. Then
\[
\begin{gathered}
F=\sum_{i=1}^n Rf_i\simeq R^n,\qquad
M/F\text{ is flat over }R,\\
F\cap JM=JF\quad\text{for every ideal }J\subseteq R.
\end{gathered}
\tag{1}
\]
No Noetherian, dimension, regularity or algebra structure is
required in this statement.

By [Lazard's theorem](https://stacks.math.columbia.edu/tag/058G),
write M as a directed colimit of finite free modules P_i.
Lift all the finitely many f_i to one stage P_i0. For each later
stage j let alpha_j:R^n to P_j send the standard basis to the
transition images of these lifts. Its reduction modulo m is
injective: any dependence would map to a dependence of the
specified independent classes in M/mM.

An injective matrix over k has a nonzero maximal minor. The
corresponding minor over local R is a unit, so the columns of
alpha_j extend to a basis of P_j. Thus alpha_j is split
injective and P_j/alpha_j(R^n) is finite free. The transition
maps preserve the labeled images of R^n, so they induce maps
on these quotients. Passing to the cofinal tail j>=i0 gives
\[
M/F\simeq
\operatorname*{colim}_{j\ge i_0}
\bigl(P_j/\alpha_j(R^n)\bigr).
\tag{2}
\]
Filtered colimits preserve exact sequences and flatness.
This proves both the injectivity of R^n into M and flatness
of the quotient. No compatible choice of splittings at the
individual stages is needed. In particular the argument does
not assert that M or M/F is a finite module.

Tensor the exact sequence 0 to F to M to M/F to 0 with R/J.
Flatness of the last term makes F/JF to M/JM injective. Its
kernel is (F intersect JM)/JF, proving the final assertion
of (1). In fact the inclusion remains injective after tensoring
with every R-module, which is the module-theoretic purity
assertion. A global R-linear splitting of M to F is not
claimed or used.

## 2. Application to an arbitrary parameter ideal

Suppose A is flat over the local base R and F is the finite
free submodule with basis 1,z,w whose images are independent
in A/mA. For arbitrary a,b,theta,B_1,B_2,gamma in R suppose
the following identity holds in A:
\[
\begin{gathered}
r=az+bw,\qquad J=(a,b),\\
\theta r^2-2B_2z+2B_1w=\gamma .
\end{gathered}
\tag{3}
\]
The quadratic term lies in J squared times A. Hence
gamma+2B_2z-2B_1w lies in both F and J squared times A.
Apply (1) with the ideal J squared and use the specified
free basis. If two is a unit in R, the exact conclusion is
\[
\boxed{\quad B_1,\ B_2,\ \gamma\in J^2.\quad}
\tag{4}
\]
Neither J=m nor reducedness of R/J is needed. Theta need not
be a unit. More generally every linear combination of the
specified basis which belongs to JA has every coefficient
in J.

In the actual mixed full-Artin branch, the earlier proofs
supply precisely a rank-three F_2 with independent whole-fiber
residues and a flat ambient A_R. Thus this coefficient argument
applies whenever the conic relation has the form (3) in that
same actual module. It does not supply such a relation or any
subsequent recognition argument by itself. In particular no
claim that m squared is contained in J squared is involved.

## 3. Why the residue hypothesis cannot be suppressed

Over R=C[a,b]_(a,b), take M=R^2 and F=R(a,b). Both modules are
free, but the residue map of F is zero. Then F is contained
in mM, so F intersect mM is F rather than mF. The quotient
is isomorphic to the nonprincipal ideal (a,b), via
(x,y) mapping to bx-ay, and is not flat over the local ring.
This is the finite elementary obstruction to applying (1) to
every free degree module indiscriminately.

The actual conclusion therefore uses the proved full residue
image of F_2, not just its rank or abstract freeness. It does
not assert purity of an unrelated F_j whose map to A/mA has
a kernel.

## Source and verification scope

The complete displayed statement and proof of Stacks
[Lazard's theorem, 058G](https://stacks.math.columbia.edu/tag/058G)
and the complete supporting
[Section 10.81, 058C](https://stacks.math.columbia.edu/tag/058C)
were read for this argument. The section includes the finite
factorization criterion and the construction of the cofinal
finite free system. Its deeper equational-flatness and
filtered-colimit foundations were not freshly rebuilt.
The application and matrix-splitting argument above are written
out to expose the nonfinite-module gate.

This is a standard purity consequence, not a new classification
theorem or a cancellation result. No numerical method is needed
to establish it. All files through106 remain unchanged.
