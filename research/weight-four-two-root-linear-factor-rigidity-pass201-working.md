# Algebraic rigidity of the two-root linear differential factor

Status: bounded working differential proof, pending independent
saved-source review. For \(q^2=t(1-t)\), every algebraic solution of
the linear factor specified below is a complex constant multiple
of \(q\). The first square-completion differential equation then
holds automatically.

This note classifies the stated differential branch. It does not
derive the full second-gate factorization, treat its other factor,
normalize lower potentials, construct an actual frame, or recognize
an invariant ring.

## 1. Exact field and statement

Let \(t\) be transcendental over \(\mathbb C\), and let \(K\) be
any finite extension of \(\mathbb C(t)\) containing \(q\) with
\[
q^2=t(1-t).
\tag{1}
\]
The derivative \(\partial_t\) extends uniquely to \(K\), since the
extension is separable. A prime denotes this derivative.
The ambient field \(K\) is not assumed rational.

Put
\[
p=t(1-t)=q^2,\qquad s=1-2t,\qquad
d=\frac{s}{16q^5},\qquad
D(f)=\frac{d'f}{4}+df'.
\tag{2}
\]
Consider the linear expression
\[
\begin{aligned}
\mathscr L(f)
&=(2t-1)f+t(1-t)f'
       +2t^2(t-1)^2(2t-1)f''\\
&=-sf+pf'-2p^2sf'' .
\end{aligned}
\tag{3}
\]
The conclusion is
\[
\boxed{\quad
f\in K,\ \mathscr L(f)=0
\quad\Longleftrightarrow\quad
f=cq\ \text{for some }c\in\mathbb C .
\quad}
\tag{4}
\]
For these solutions the first square-completion gate
\[
\mathscr E(f)=20D(f)f'''-3d(f'')^2-12f''D(f)'=0
\tag{5}
\]
also holds. The usual nondegenerate requirement \(ff''D(f)\ne0\)
is equivalent to \(c\ne0\).

The intended coefficient-field application is the two-root leading
ratio in the actual universal chart. For that application (3) is
an explicit additional differential hypothesis. Nothing here silently
asserts that every actual frame must lie in this factor.

## 2. Reduction to a logarithmic differential

The elementary derivative identities are
\[
p'=s,\qquad s'=-2,\qquad
s^2+4p=1,\qquad
q'=\frac{s}{2q},\qquad
q''=-\frac1{4q^3},\qquad
q'''=\frac{3s}{8q^5}.
\tag{6}
\]
In particular \(\mathscr L(q)=0\).
For any \(h\in K\), applying the product rule gives the exact identity
\[
\begin{aligned}
\mathscr L(qh)
&=pq\{(1-2s^2)h'-2psh''\}\\
&=-2p^2(qs h')'.
\end{aligned}
\tag{7}
\]
For the second equality use
\((qs)'=(2s^2-1)/(2q)\) and \(p=q^2\).
All factors divided below are nonzero field elements: \(t\) is
transcendental, so \(p,q,s\) are not identically zero.
No assertion of invertibility in an original polynomial ring is made.

The derivative constants of \(K\) are exactly \(\mathbb C\).
Here is an algebraic justification. If \(u'\!=0\), differentiate
the monic minimal polynomial of \(u\) over \(\mathbb C(t)\).
The resulting polynomial in \(u\) has smaller degree, so each
coefficient derivative is zero by minimality. The original
coefficients are therefore in \(\mathbb C\), and \(u\) is algebraic
over the algebraically closed field \(\mathbb C\). Thus \(u\in\mathbb C\).

For \(\mathscr L(f)=0\), set \(h=f/q\).
Equation (7) consequently gives
\[
qs h'=C,\qquad C\in\mathbb C,\qquad
dh=C\,\frac{dt}{qs}.
\tag{8}
\]
The right side is a logarithmic differential. Its nonzero residues
exclude \(C\ne0\) even in a proper finite algebraic coefficient field.

## 3. Trace prevents an algebraic primitive

Work first in the subfield \(F=\mathbb C(t,q)\subseteq K\).
It is rational for an explicitly proved reason: put \(r=t/q\).
Then
\[
t=\frac{r^2}{1+r^2},\qquad
q=\frac{r}{1+r^2},\qquad
s=\frac{1-r^2}{1+r^2},\qquad
F=\mathbb C(r).
\tag{9}
\]
These identities follow from \(r^2=t/(1-t)\).
They identify only the subfield \(F\), not the ambient field \(K\).
The normalized differential is
\[
\frac{dt}{qs}=\frac{2\,dr}{1-r^2}.
\tag{10}
\]
It has residue \(-1\) at \(r=1\) and residue \(1\) at \(r=-1\).
For example
\(\lim_{r\to1}(r-1)2/(1-r^2)=-1\).

Let \(n=[K:F]\). The trace
\(H=\operatorname{Tr}_{K/F}(h)\) belongs to \(F=\mathbb C(r)\).
Derivation commutes with this trace. Indeed, in a finite normal
closure the trace is the sum of the \(F\)-embeddings of \(h\);
the unique extension of \(\partial_r\) commutes with each embedding.
Taking the trace of (8), with (10), gives
\[
dH=nC\,\frac{2\,dr}{1-r^2}.
\tag{11}
\]
The derivative of a rational function has zero residue at every point.
This can be seen directly from its finite principal Laurent part:
the coefficient of \((r-r_0)^{-1}dr\) in
\(\sum_j j a_j(r-r_0)^{j-1}dr\) is zero, since the only possible
index is \(j=0\).
At \(r=1\), equation (11) therefore forces \(-nC=0\).
Characteristic zero and \(n>0\) imply \(C=0\).

Returning to (8), \(h'=0\); the constant-field argument above gives
\(h=c\in\mathbb C\). Hence \(f=cq\).
Conversely \(\mathscr L(q)=0\) and linearity prove that every \(cq\)
satisfies (3). This proves (4), with no rational ansatz for \(f\)
and no assumption \(K=F\).

Equivalently, one could pull (10) to a finite covering curve:
the nonzero simple-pole residues multiply by ramification and
cannot become the residues of an exact differential.
The trace argument already gives the complete algebraic obstruction,
so no choice of a covering model is needed here.

## 4. First gate and all nonzero conditions

For \(f=cq\), direct differentiation of (2) and (6) gives
\[
\begin{gathered}
d'=-\frac{1+4s^2}{32q^7},\qquad
D(f)=-\frac{c}{128q^6},\qquad
D(f)'=\frac{3cs}{128q^8},\\
f''=-\frac{c}{4q^3},\qquad
f'''=\frac{3cs}{8q^5},\qquad
ff''D(f)=\frac{c^3}{512q^8}.
\end{gathered}
\tag{12}
\]
The three summands in (5), in their stated order, are
\[
-\frac{15c^2s}{256q^{11}},\qquad
-\frac{3c^2s}{256q^{11}},\qquad
\frac{18c^2s}{256q^{11}}.
\tag{13}
\]
They sum to zero. Thus the complete algebraic solution list for
(3) and (5) under \(ff''D(f)\ne0\) is precisely
\[
f=cq,\qquad c\in\mathbb C^* .
\tag{14}
\]
Zeros of individual rational functions at particular points do not
invalidate these field identities; the required nonzero conditions
are nonvanishing as field elements.

## Scope and verification

The classification is stronger than using both equations:
the linear equation alone already has only the solutions (4)
in every allowed finite algebraic field. The first nonlinear gate
then imposes no further restriction except the nondegenerate
constant condition.

This note does not prove the full second-gate factorization or
classify its other factor. It does not normalize actual lower
potentials or imply actual realization, recognition, a global
coordinate equal to \(q\), or unrestricted cancellation.
No prior saved artifact has been changed.

Independent new inline exact arithmetic in the rational parameter
\(r\) checked (7), (10), (12), (5), and both residues.
No saved checker was executed, imported, compiled, or edited.
The finite arithmetic does not prove the trace or residue argument,
which is written above. This is a bounded working proof, not
human expert certification, formal verification, or a novelty claim.
