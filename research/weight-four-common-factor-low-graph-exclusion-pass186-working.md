# The constant and linear graph branches of the common-factor quartic

**Status: working restricted proof, pending independent saved-source review.**

For the actual common-factor quartic chart below, an affine projected
line parameter \(y\) cannot have a constant or linear graph
\(\vartheta=P(y)\). The obstruction is the highest homogeneous part of
the exact eliminant. It does not require an evaluated-unit cofactor.

## 1. Actual hypotheses and retained inputs

Assume the actual sliced frame of
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\!\left(\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow\operatorname{gr}_E B\right)
 =(\mathsf X^2\mathsf Z+\mathsf X\mathsf Y\mathsf W-\mathsf Y^4).
\end{gathered}
\tag{1}
\]
Here the map is the weighted initial map for weights \((1,1,2,2)\).
Retain the selected nonzero derivation
\(N=[u^3](\partial_Z|_A)\), its exact coefficient field
\(L=\operatorname{Frac}(\ker_A N)\), and \(A_L=L[v]\), \(Nv=1\).
Write
\[
a=EX\in L^*,\qquad t=EY/a,\qquad
\rho=(E^2W/2)/a^2,\qquad q=-t\rho+t^4.
\tag{2}
\]
The coefficient partials on the finite separable extension
\(L/\mathbb C(t,\rho)\) are those of the retained chart.

The whole-plane and
[selected-component184](weight-four-bad-linear-selected-component-pass184-working.md)
proofs give \(L[y,\vartheta]=L[v]\) and show that \(y\) is either
constant in \(v\) or affine with nonzero slope. This note assumes the
latter branch. Thus
\[
y=\gamma v+\eta,\quad \gamma\in L^*,\quad \eta\in L,\qquad
\vartheta=P(y),\quad P\in L[U].
\tag{3}
\]
In particular \(y\) is transcendental over \(L\), and the complete
evaluation kernel \(L[U,V]\to L[v]\) is
\((G)\), where \(G=V-P(U)\). This assertion concerns the actual
generic line, not a merely rational parametrization.

For clarity, \(H_j(f;U,V)\) denotes
\((U\partial_t+V\partial_\rho)^j f/j!\), with \(U,V\) held fixed.
The exact potentials of the actual chart are
\[
\begin{gathered}
R=k_\rho-U,\qquad
S=4tU^3+H_2(k;U,V)+H_1(n;U,V),\\
A_1=H_1(k_\rho;U,V)+n_\rho,\qquad
T=U^4+H_3(k;U,V)+H_2(n;U,V),\\
\mathcal H=
R\{T-\ell_tU-\ell_\rho V-m\}+A_1(\ell-S),
\qquad k,n,\ell,m\in L.
\end{gathered}
\tag{4}
\]
They give \(\mathcal H(y,\vartheta)=0\). The only term of total degree
five in (4) is \(-U\cdot U^4\), so
\(\deg\mathcal H=5\) and \(\mathcal H_5=-U^5\).
Consequently \(G\mid\mathcal H\). No assertion that \(\mathcal H=G\)
is used.

## 2. Complete exclusion of the two low graph degrees

Suppose \(P(U)=p_1U+p_0\), with arbitrary \(p_0,p_1\in L\).
This includes the zero polynomial and all constant graphs.
The polynomial \(G=V-p_1U-p_0\) has total degree one, with highest
homogeneous part \(V-p_1U\).

Write \(\mathcal H=GQ\). Since \(L[U,V]\) is a domain,
the highest homogeneous parts of a nonzero product multiply.
Thus \(Q\) has total degree four and
\[
-U^5=(V-p_1U)Q_4.
\tag{5}
\]
Evaluating (5) at \(V=p_1U\) gives the false polynomial identity
\(-U^5=0\) in \(L[U]\). This contradiction applies equally to
\(p_1=0\) and \(p_1\ne0\).

Therefore no actual frame satisfying (1) can lie in the affine-\(y\)
branch (3) with a constant or linear projected graph.

## 3. Exact scope of the reduction

The proof uses the actual eliminant and its complete graph relation,
but not the stronger unit-selected-cofactor conclusion. In particular
it does not replace that conclusion in the higher graph branches.
It places no nonvanishing restriction on \(p_0\) or \(p_1\), assumes
neither \(K=\mathbb C(t)\) nor global invertibility of \(a\), and makes
no claim that the literal quartic in (1) is invariant.

The separate
[high-graph185 proof](weight-four-common-factor-high-graph-recognition-pass185-working.md)
recognizes the affine-\(y\) branch with graph degree at least three.
Together with that proof, this leaves only graph degree two within
the affine-\(y\) branch. The constant-\(y\) branch is logically
separate and is not addressed or presumed complete here.

This is a restricted statement about a supplied actual frame. It
does not produce such a frame from an arbitrary action, settle the
other weight-four normal forms, or prove unrestricted cancellation.
No tests were executed, no frozen artifact was changed, and no
historical novelty or formal-certification claim is made.
