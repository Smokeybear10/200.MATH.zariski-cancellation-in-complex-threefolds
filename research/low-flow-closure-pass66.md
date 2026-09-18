# Low-flow cancellation and the remaining cubic obligations

Every sliced action satisfying the supplied two-quadratic coordinate
frame is now recognized when its coordinate flow has degree at most
two. The last possible dependent-defect rank-three configuration is
excluded by a five-dimensional matrix argument. Two separate cubic
reductions give more explicit normal forms, but do not finish those
higher-flow cases.

The unrestricted complex-threefold cancellation conjecture remains
unsolved. None of these results proves that an arbitrary sliced action
admits the coordinate frame used below.

## 1. The conditional theorem

The working question is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\]
The dimension in the professor's pasted conclusion has been corrected,
and the field and dimension specialized to the complex threefold case.
The professor has not confirmed that interpretation.

Transporting \(\partial_{s_*}\) gives a locally nilpotent derivation
\(E\) of the actual polynomial ring
\(B=\mathbb C[x_1,x_2,X,Y]\), with \(E(s_*)=1\) and \(A=\ker E\).
Let \(T_1,T_2,T_X,T_Y\) be the genuine partial derivatives in these
coordinates.

**Conditional low-flow theorem.** If
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0,
\qquad E^3(x_1,x_2,X,Y)=0,
\tag{1}
\]
then \(A\simeq\mathbb C^{[3]}\).

The last condition bounds the degree in the action's flow parameter.
It does not bound the ordinary polynomial degree of the coefficients
of \(E\). The coordinate-partial assumptions are substantive and cannot
be replaced by a rational vector-field basis.

## 2. The new rank cap

Write
\[
V_X=\operatorname{ad}_E^2T_X,\quad
V_Y=\operatorname{ad}_E^2T_Y,\quad W_i=[E,T_i].
\]
In the dependent-defect case with no complex constant relation, the
primitive decomposition has the form
\[
V_X=aD,\qquad V_Y=bD,\qquad
[E,D]=0,\qquad a,b\in\ker E\cap\ker D.
\]
The [new rank theorem](rank-three-speed-curve-pass66.md) proves, at
flow degree two,
\[
\operatorname{rank}_{\operatorname{Frac}B}
\{E,W_1,W_2,D\}\le2.
\tag{2}
\]
No bad-speed Jacobian-rank or projective-direction assumption is needed
for this stronger conclusion.

Here is the decisive mechanism. Put \(P=Ex\), \(J=\operatorname{Jac}P\),
\(d=D(x)\), and \(\ell=(0,0,a,b)\). The actual weighted companion is
\[
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}.
\tag{3}
\]
Its exact inverse-Jacobian identities give \(M^3=0\). A hypothetical
joint rank of three forces \(M\) to have Jordan type \((3,2)\).
The span of the highest vector and all its ordinary derivative columns,
together with the complete velocity equations, then gives a
three-dimensional horizontal space \(T\) with
\[
M(T)\subset\operatorname{im}M^2.
\]
For this Jordan type,
\[
M^{-1}(\operatorname{im}M^2)=\operatorname{im}M.
\tag{4}
\]
Both sides have dimension three. Consequently \(T=\operatorname{im}M\)
would be horizontal. That contradicts the nonzero auxiliary image
required by \(\ell\ne0\).

The proof retains the entire last row. An upper-left Jacobian rank
alone would miss the contradiction. The rank proof uses polynomial
differentiation and exact finite-dimensional linear algebra; it does
not require a polynomial-curve classification or a presentation of an
invariant ring.

The initial proof used nonconstant projective speeds to finish with
a Wronskian contradiction. Equation (4) removes that extra premise.
The original narrower argument was valid; the final result is stronger.
A further derivative-column argument removes the curve-factorization
input from this rank theorem entirely.

## 3. Exhaustion of all low-flow cases

The new rank cap completes, rather than replaces, the
[previous low-flow case map](low-flow-synthesis-pass65.md).

| Actual case under (1) | Recognition or exclusion |
| --- | --- |
| The two defects have a complex constant relation | A constant coordinate recombination supplies the already recognized mixed frame. This includes zero defects. |
| Independent defects | The complete degree-two graph theorem recognizes the original kernel. The degree-one alternative is excluded by the companion calculation. |
| Dependent defects without a constant relation, flow degree one | Both bad coordinates are invariant by the highest-column argument. |
| Dependent defects without a constant relation, flow degree two | Equation (2) bounds the leading rank by two. The established independent-speed, constant-projective-speed, and speed-curve proofs cover every speed alternative. |

The sources for this composition are the
[dependent low-flow theorem](dependent-low-flow-pass65.md),
[one-parameter graph theorem and projection corollary](dependent-speed-curve-graph-pass65.md),
[actual independent-defect graph theorem](actual-quadratic-graph-cancellation-pass64.md),
and the new rank theorem.
Their coordinate-generation and established classification hypotheses
remain part of the proof.

This is a theorem about the original sliced kernel \(A\), not merely
a localization, a generic fiber, or a formal coordinate change.
It does not assert that a chosen intrinsic action has a global slice
or that every particular quotient map is a product.

## 4. Dependent constant-top cubic normal form

The [new dependent cubic reduction](dependent-constant-cubic-pass66.md)
assumes \(E^3x=c\ne0\) is a complex constant vector and the two defects
have rank one without a complex constant relation.
The bad components of \(c\) vanish.

The five-dimensional companion now has a rank-one square, and its
complete velocity column forces
\[
E^2x=c\sigma+e,\qquad
c,e\in\mathbb C^4,\qquad E\sigma=1,
\tag{5}
\]
with an actual polynomial \(\sigma\in B\).
In particular \(EX=f,EY=g\) satisfy
\[
Ef=e_3,\qquad Eg=e_4.
\]
After defining \(F=f-e_3\sigma\), \(G=g-e_4\sigma\), the exact lower
matrix row gives
\[
EF=EG=0,\qquad a\,dF+b\,dG=0.
\tag{6}
\]
Thus a nonconstant residual pair has the actual polynomial form
\[
F=p(u),\qquad G=q(u),\qquad
a\,p'(u)+b\,q'(u)=0.
\tag{7}
\]
The tangent ratio \(p'/q'\) is nonconstant. The parameter \(u\)
and the slice \(\sigma\) are not asserted to be ambient coordinates.

Two endpoints are recognized: zero bad acceleration \((e_3,e_4)=0\),
and a constant residual pair \(F,G\).
What remains is the nonzero bad-acceleration case with the nonconstant
tangent curve (7). The reduction does not prove that this remaining
formal alternative is realized.

## 5. Independent constant-top cubic good fields

The separate [independent cubic refinement](constant-top-cubic-good-fields-pass66.md)
retains the previous actual ring
\(\ker(V_X,V_Y)=\mathbb C[t,f]\), with \(Et=0,Ef=1\), and
\[
E^2x=(f-F(t),U(t),1,0)^t,\qquad EY=G(t).
\]
In its retained branch \(U,G\) are nonconstant. The full reverse
inverse-Jacobian equation proves
\[
U'(t)W_2+F'(t)V_X+G'(t)V_Y=0.
\tag{8}
\]
Together with \(W_1=-V_X\), this identifies the two good leading
fields as an independent basis of the defect distribution. Their
actual common kernel is also \(\mathbb C[t,f]\).

The corrected Heisenberg field \(R\) has a representation
\[
R=\alpha(t)V_X+\beta(t)V_Y,\qquad
\alpha,\beta\in\mathbb C(t).
\tag{9}
\]
Polynomiality of \(R\) does not separately make these two coefficients
polynomial. The earlier proposed nonzero parameter motion remains
excluded: the original full coefficients force \(Rt=Rf=0\).

A sufficient next step is to prove that a nonzero constant good
partial preserves \(\mathbb C[t,f]\). That would produce either
an ambient invariant coordinate or an omitted constant direction,
both recognized by existing theorems. What is known at present is
only that its derivatives of \(t,f\) are \(E\)-invariant. Their
annihilation by both defects is still missing.

## 6. Verification and remaining work

The [exact checker](dependent_low_flow_rank_checks_pass66.py)
tests the five-dimensional Jordan alternatives and full companion
preimages. Its actual-model test uses the already established
rank-two frame from pass42. That model has matrix rank three but
joint leading rank two, so the checker explicitly prevents those
two notions of rank from being conflated.

The [regression runner](run_regression_pass66.py) combines the frozen
full60 suite set with all distinct working61--66 additions.
The [captured run](verification-pass66-working.json) records the
actual method counts, process exits and outputs.
The completed run passed 1008 methods across 130 suites. This includes
the historical 1000 methods in 126 suites and eight distinct later
methods in four suites. Three methods in one suite are new in pass66.
Numerical checks do not prove the all-instance argument or the
external classification theorems.
The [proof audit](proof-audits-pass66-working.md) records independent
AI reconstructions and exact source-reading scope.

The remaining mathematical obligations are now:

- The dependent and independent cubic problems stated in Sections 4--5.
- Other higher constant-top and moving-top cases in the supplied
  two-quadratic frame.
- A universal construction of an applicable coordinate frame, or a
  different unrestricted recognition argument.

The complete low-flow theorem does not finish the entire profile
\((1,1,2,2)\). The all-profile height threshold therefore remains
\(H\le9\), not \(H\le10\).
The [earlier higher-flow dependency map](post-graph-closure-scope-pass64.md)
remains relevant with its old low-flow gap replaced by Section 3.

There is no human expert review, proof-assistant verification,
historical novelty certification, public submission, external
contact, or general cancellation solution. The conditional proofs
are private working mathematics awaiting further scrutiny.

## Established source gates

The exact finite-curve input is de Bondt's
[Corollary 3.2 and Lemma 3.3](https://arxiv.org/pdf/1501.06046v4).
The endpoint for an actual invariant coordinate and regular original
kernel is Bhatwadekar, Gupta and Lokhande's
[Theorem 3.5](https://arxiv.org/pdf/1501.01438v1).
These are established results, not new claims of this packet.
The earlier graph and one-good-output proofs retain their separately
recorded intrinsic quotient, relative-plane, commuting-derivation
and Dedekind-base source obligations.
