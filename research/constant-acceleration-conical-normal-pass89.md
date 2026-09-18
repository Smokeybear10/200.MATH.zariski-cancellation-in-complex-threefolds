# A rank-two conical unit speed row has a unit polynomial normal

The normal-unit premise in the
[conical good-direction reduction88](constant-acceleration-conical-good-direction-pass88.md)
is automatic under that note's rank-two conical hypotheses.
A retained binary-parametrization theorem applies inside the actual
invariant plane. Its primitive scalar and the original unit speed row
make the binary parameters unimodular. The primitive binary normal
then has no projective base point, and its substitution is a unit row.

The resulting conclusion is two-generator algebra generation of the
original kernel over its actual invariant plane. It is not a coordinate
presentation over that plane or recognition of the remaining branch.

## 1. Exact hypotheses and the source decomposition

Retain the actual setup of the
[invariant-plane lemma88](constant-acceleration-invariant-plane-pass88.md):
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
Ex_i=b_i\in S=\mathbb C[s_1,s_2],\qquad
Ez=qu,\quad Eu=1,\quad q\in\mathbb C^*,\qquad
(b_1,b_2,b_3)S=S.
\tag{1}
\]
The plane is \(S=\ker(W|A)\) for an actual nonzero highest-adjoint
LND \(W\), and \(Wu=0\). Assume
\[
\operatorname{rank}[b_{s_1},b_{s_2}]=2,\qquad
\det[b,b_{s_1},b_{s_2}]=0.
\tag{2}
\]
These ranks can be computed over \(\operatorname{Frac}(S)\) or
\(\operatorname{Frac}(B)\), with the same answer.

Let \(t\) be a new indeterminate. The Jacobian of the triple \(tb\)
in \(s_1,s_2,t\) has columns \(t b_{s_1},t b_{s_2},b\), of rank two.
The characteristic-zero differential criterion for transcendence
degree therefore gives \(\operatorname{trdeg}_{\mathbb C}\mathbb C(tb)=2\).
In particular the following source is applied to polynomials in
\(S=\mathbb C[s_1,s_2]\), not merely to the larger four-variable ring.

De Bondt, Theorem 2.7(i)--(v), states that for a rational tuple \(H\)
over any field \(k\), if \(\operatorname{trdeg}_k k(tH)\le2\), there
are a nonzero rational scalar \(g\), a homogeneous primitive binary
tuple \(h\) (or the zero tuple), and a primitive nonconstant
polynomial pair \((p_0,p_1)\), such that \(H=g h(p_0,p_1)\).
Its part (v) further states that \(h(p_0,p_1)\) is primitive when
\(H\ne0\). Here primitive means no nonunit common polynomial divisor;
it does not mean a unit ideal.[^binary]

For the present nonzero speed tuple the source gives
\[
b=\gamma\,h(f_0,f_1),\qquad
\gamma\in\operatorname{Frac}(S)^*,\qquad f_0,f_1\in S,
\qquad h\in\mathbb C[\xi,\eta]^3
\text{ homogeneous and primitive},
\qquad \gcd_S h(f_0,f_1)=1.
\tag{3}
\]
The same source gives a primitive pair \((f_0,f_1)\). We will need,
and prove, the stronger unit-ideal property below.

## 2. The rational scalar is constant and the parameters are unimodular

Write \(\gamma=a/d\) in lowest terms in the UFD \(S\). Since each
\(a h_i(f_0,f_1)/d\) is polynomial and \(a,d\) are coprime,
every irreducible factor of \(d\), with its full multiplicity,
divides every \(h_i(f_0,f_1)\). Primitivity in (3) makes \(d\)
a unit. Thus \(\gamma\in S\).

Now every \(b_i\) is divisible by \(\gamma\), and the \(b_i\) generate
the unit ideal in \(S\). Consequently \(\gamma\) is a unit of \(S\),
which means a nonzero complex constant. Also the degree of \(h\)
is positive: degree zero would make \(b\) constant, contrary to (2).
Homogeneity therefore puts every \(h_i(f_0,f_1)\) in \((f_0,f_1)S\).
Since these substituted components generate the unit ideal by
\(\gamma\in\mathbb C^*\), we obtain
\[
\gamma\in\mathbb C^*,\qquad
e:=\deg h\ge1,\qquad
(f_0,f_1)S=S.
\tag{4}
\]
This upgrade uses the original unit speed row, not just coprimality
of either tuple in the source statement.

The chain rule in (3) now reads
\([b_{s_1},b_{s_2}]=
\gamma[h_\xi(f),h_\eta(f)]\,\operatorname{Jac}(f_0,f_1)\).
Its rank two implies that both factors have rank two over the
fraction field. Thus \(f_0,f_1\) are algebraically independent
and the binary cross product \(h_\xi\times h_\eta\) is nonzero.
In particular neither a rank-one binary image nor a constant
parametrization has entered the argument.

## 3. The primitive binary normal has no base point

Each nonzero component of the cross product is homogeneous of
degree \(2e-2\). Divide all components by their common homogeneous
gcd \(\rho\), choosing any nonzero complex normalization:
\[
C=h_\xi\times h_\eta\ne0,\qquad
N_0=C/\rho\in\mathbb C[\xi,\eta]^3,\qquad
\gcd(N_{0,1},N_{0,2},N_{0,3})=1.
\tag{5}
\]
The entries of \(N_0\) are homogeneous of one common nonnegative
degree. A common zero at any nonzero pair \((\xi,\eta)\) would give
a point of the projective line where every entry vanishes. The
linear form defining that point would then divide every entry,
contrary to their gcd. Zero entries cause no exception. If their
degree is zero, at least one entry is already a nonzero constant.
Thus \(N_0\) has no common zero on the projective line.

By its cross-product definition and the Euler identity
\(e h=\xi h_\xi+\eta h_\eta\), it satisfies
\(N_0h_\xi=N_0h_\eta=N_0h=0\). Substitute the actual pair in (4):
\[
N:=N_0(f_0,f_1)\in S^3,\qquad
(N_1,N_2,N_3)S=S,\qquad
N\cdot b=N\cdot b_{s_1}=N\cdot b_{s_2}=0.
\tag{6}
\]
For the unit assertion, at every closed point of the affine plane
the pair \((f_0,f_1)\) is nonzero by (4). The absence of a
projective common zero for \(N_0\) makes \(N\) nonzero at that
point. The Nullstellensatz therefore gives the displayed unit
ideal. This is a closed-point argument in the actual polynomial
plane, not an inference that a general coprime row is unimodular.
The derivative annihilations follow directly by the chain rule.

## 4. Actual normal invariant and two relative generators

The original chain-rule factorization of \(J\) in conical88 puts
the transverse highest column \(W(x)_{\rm tr}\) in the span of
\(b_{s_1},b_{s_2}\). Since \(N\in S^3\), the identities (6) give
\[
c_0:=N\cdot x_{\rm tr}\in A,\qquad
W(c_0)=0,\qquad c_0\in S.
\tag{7}
\]
Here \(E(c_0)=N\cdot b=0\) gives the first membership and the
exact intrinsic kernel gives the last. No localized invariant is
promoted to a polynomial without this actual kernel argument.

The now-unconditional unit normal supplies the premise of Section 4
of conical88. For completeness, choose \(\ell\in S^3\) with
\(\ell b=1\). The kernel of \(N:S^3\to S\) is projective of rank
two, and restriction of \(\ell\) splits off \(Sb\). Its rank-one
complement is free over the actual polynomial plane by the retained
Quillen--Suslin input. Choose its generator \(V\), and choose
\(U_0\) with \(NU_0=1\). Then \([b,V,U_0]\) is an invertible
matrix over \(S\), and its actual inverse coefficients define
\[
x_{\rm tr}=b\sigma+VY+U_0c_0,\qquad
E\sigma=1,\quad EY=0,\qquad
B=S[\sigma,Y,z],\qquad
A=S[Y,c],\quad
c=z-qu\sigma+\frac q2\sigma^2.
\tag{8}
\]
The inverse matrix proves the subalgebra equality for \(B\);
\(c_0\) is already in \(S\). Evaluating at \(\sigma=0\) in the
actual slice presentation \(B=A[\sigma]\) proves the last equality.
These are algebra-generation statements, not free polynomial
presentations over \(S\).

If \(Y\) is algebraic over \(\operatorname{Frac}(S)\), the actual
derivation \(W\) kills it by separable minimal-polynomial
differentiation. Thus \(Y\in S\), and (8) then recognizes
\(A=S[c]\simeq\mathbb C^{[3]}\) by transcendence degree.
Otherwise \(S[Y]\) is a polynomial three-ring. In that remaining
case, neither its normality nor the generator pencil by itself
places the slice difference \(u-\sigma\) in \(S[Y]\):
the [normal-ring pencil control88](normal-generator-pencil-coordinate-boundary-pass88.md)
separates those weaker algebraic properties from the still essential
original-coordinate hypotheses. No recognition of that remaining
case is claimed here.

This note discharges the unit-normal premise using a source-backed
binary decomposition. It does not infer a global slice for \(W\),
an actual ambient coordinate plane, or a new unrestricted
cancellation theorem. No numerical test or pass88 integration
artifact is added.

## 5. Source access and provenance

Root proposed the unit-normal route through a projective
parametrization. General identified the exact retained Theorem 2.7
as a way to make that parametrization inside \(S\), independently
proved the scalar and unit-ideal upgrades, and reconstructed the
normal and actual-generation consequences.

The selected source access for this deduction is the complete
displayed statement of Theorem 2.7 and its displayed proof through
parts (i)--(viii), in the retained primary text. The source's
Lüroth and homogeneous-gcd dependencies are inherited theorem
inputs, not newly audited full proofs here. Part (ix) and its
minimality refinement are unused. The retained PDF SHA-256 is
\(\texttt{75b598e2e8cad4ec07e9e97ba027c89df659999137e70b22c96596b6003d7698}\);
the layout-text SHA-256 is
\(\texttt{aff7b6b02c41b507f58e37a15a6ecab34565f0606fdf10178e1f3963de86d7f5}\).
Both were independently rechecked for this note.

[^binary]: Michiel de Bondt, [*Rational maps \(H\) for which \(K(tH)\) has transcendence degree 2 over \(K\)*](https://arxiv.org/pdf/1501.06046v4), Theorem 2.7(i)--(v), printed pages 16--17. Exact retained inputs: [primary PDF](../tmp/pdfs/bondt-1501.06046v4.pdf) and [layout text](../tmp/pdfs/bondt-1501.06046v4.txt). The decomposition applies to an arbitrary tuple length and does not require a quasi-translation, a supplied invariant coordinate, or homogeneity of the original tuple.
