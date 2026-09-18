# Recognition of dependent defects under the supplied frame

The written proof chain now recognizes every sliced action in the
supplied two-quadratic coordinate frame whose two quadratic defects
are dependent over the fraction field. The new terminal-quartic
endpoint closes the last case in that dependent sector.

The actual frame and original polynomial slice remain hypotheses.
This is neither recognition of the entire supplied frame nor a
solution of unrestricted complex-threefold cancellation.

## 1. Exact conditional statement

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad E(s_*)=1,\qquad A=\ker E.
\]
The four displayed generators are actual polynomial coordinates.
For their genuine partials assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Put \(V_X=\operatorname{ad}_E^2T_X\),
\(V_Y=\operatorname{ad}_E^2T_Y\), and \(K=\operatorname{Frac}B\).
Then
\[
\boxed{\quad
\operatorname{rank}_K(V_X,V_Y)\le1
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\quad}
\tag{2}
\]
The rank condition includes zero defects and a constant relation.
It is not an assumption that the original action and the common
defect direction have joint rank one.

Write \(x=(Q_1,Q_2,X,Y)^t\), and let \(m\) be the largest integer
with \(E^mx\ne0\). Such an integer exists by local nilpotence,
and \(m\ge1\) because of the original slice. It measures degree
in the flow parameter, not ordinary polynomial coefficient degree.

## 2. The exhaustive reduction to a moving quartic

If \(\lambda V_X+\mu V_Y=0\) for some nonzero complex pair
\((\lambda,\mu)\), a constant change within the actual bad
coordinate pair produces a third good partial. The resulting
frame has three second-adjoint bounds and one third-adjoint
bound. The complete [mixed slice theorem](../deep-pass-13.md),
Section 1, recognizes the original kernel. This includes rank
zero and the case of one zero defect.

Otherwise (2)'s rank premise is exactly rank one with no complex
constant relation. The established
[primitive decomposition](dependent-quadratic-defects-pass42.md)
gives
\[
V_X=\alpha D,\qquad V_Y=\beta D,\qquad
[E,D]=0,\qquad \alpha,\beta\in\ker E\cap\ker D,
\tag{3}
\]
where \(D\) is an actual nonzero primitive polynomial LND.
Primitivity means coefficient gcd one, not a unit coefficient
ideal, and no slice on \(D\) is assumed.

The full weighted five-dimensional companion in
[the highest-vector proof](dependent-defect-top-line-pass43.md),
Section 1, gives \(M^5=0\) and
\((M^j)_{\rm UL}=\operatorname{Jac}(E^jx)/j!\).
Thus \(E^5x\) is constant, \(E^6x=0\), and \(m\le5\).
The lower row is variable and is retained in the subsequent
full-image arguments.

| Case without a complex constant defect relation | Complete recognition input |
| --- | --- |
| \(m\le3\), with either constant or nonconstant highest vector | The [supplied-frame cubic theorem](cubic-frame-closure-pass70.md), including the complete low-flow theorem. |
| \(m\ge4\) and \(E^mx\) is constant | Necessarily \(m=4\) or \(5\); the [dependent constant quartic](dependent-constant-quartic-closure-pass68.md) and [dependent constant quintic](dependent-constant-quintic-closure-pass68.md) theorems cover both. |
| \(m\ge4\) and \(E^mx\) is nonconstant | Necessarily \(m=4\); Sections 3--4 below complete this case. |

The last row follows directly from constancy of \(E^5x\).
There is no unexamined dependent higher flow degree.
The [constant-highest synthesis](constant-and-moving-closure-pass68.md)
records the upstream constant-top exhaustion, but this proof uses
only its dependent quartic and quintic cases.

## 3. Every remaining moving quartic has actual common powers

In the last row, the complete
[dependent highest-vector argument](dependent-defect-top-line-pass43.md)
supplies
\[
E^4x=cq,\qquad z=E^3x,\qquad
0\ne c\in k^4,\quad c_X=c_Y=0,\qquad
q\in(\ker E\cap\ker D)\setminus k,
\]
\[
\rho=\alpha z_X+\beta z_Y=qr,\qquad
r\in\ker E\cap\ker D,\qquad
[E,T_c]=-\frac32rD.
\tag{4}
\]
If \(r=0\), the actual constant good partial \(T_c\) commutes
with \(E\), and the recognition branch in that proof applies.
If \(r\ne0\), its original-slice argument forces \(E,D\) to
be fraction-field independent.

The [finite-root theorem](dependent-algebraic-root-top-pass70.md)
then proves, rather than assumes, an actual polynomial invariant
\(g\) with
\[
q=g^4,\qquad
z=c\tau+e g^3,\qquad
\tau\in B,\quad e\in k^4,\quad(e_X,e_Y)\ne(0,0),\qquad
g\in(\ker E\cap\ker D)\setminus k.
\tag{5}
\]
Its proof first adjoins a root in a finite algebraic field
extension. The extended original partials provide the chain
rule and full inverse matrices, without being assumed locally
nilpotent on the adjoined ring. The normalized companion forces
the transverse preceding layer to be constant. A nonzero bad
component then recovers \(g\) in \(K\), and normality of the
original polynomial ring gives \(g\in B\).

Consequently the rotating alternatives of the older weaker
differential equations cannot survive this actual full frame.
Constant changes within the good and bad pairs normalize the
two nonzero constant directions in (5), while preserving the
needed original hypotheses. This gives exactly the input of
the [common-power moving-quartic reduction](common-power-moving-quartic-reduction-pass70.md).

## 4. Exhaustion of the quartic residual pairs

That reduction uses \(\delta=E/g\) and both full companion
images, with the variable auxiliary row unchanged. It does not
apply a polynomial-four-ring theorem to \(B_g\).

Its first residual pair \((F,G)\) satisfies the full ordinary
differential relation \(dF+\eta\,dG=0\). If \(G\) is nonconstant
or zero, an exact rational two-direction symmetry recognizes
the original kernel. Otherwise \(G\in k^*\), and the relation
forces \(F\in k\); the constant first pair is transverse.
The second full image produces another residual pair. If it
is nonconstant, the same original-ring recognition theorem
applies. The only case left is its constant second pair.

The [parabolic terminal form](terminal-quartic-parabolic-form-pass71.md)
treats precisely that last case. Its explicit actual coordinate
changes preserve a good output partial and give a rational
symmetry with a one-power polynomial nice replica:
\[
S=\partial_z+\beta_0\partial_b+\kappa_0\partial_a,\qquad
T=gS=(U/3)\partial_a+N\partial_b+g\partial_z,
\]
\[
N=g\beta_0\in B,\quad U=3g\kappa_0\in B,\qquad
EN=g^2/2,\quad EU=gN,\qquad
g[E,\partial_a]=-\frac32\operatorname{ad}_E^2\partial_b.
\tag{6}
\]
The coordinate labels in (6) are those of the actual terminal
change, not the original defect multipliers in (3).
The original slice and derivation have not been replaced.

The [leading-speed lemma](nice-chain-speed-proportionality-pass71.md)
uses the known nice three-variable linear-invariant theorem over
\(k(w)\) and the original \(E\)-flow to prove \(Ew=0\) or
\(Ew=\lambda g\), \(\lambda\in k^*\).
The complete [terminal recognition proof](terminal-quartic-recognition-pass71.md)
handles both possibilities. In the nonzero case it uses polynomial
shears with complex coefficients to reduce \(S\) to two output
directions. The needed new good partial is either retained or
proved good by the exact second-adjoint cancellation in (6).
The [rational two-direction theorem](rational-two-direction-recognition-pass69.md)
then applies to the original sliced action.

This is the missing global recognition step. It does not infer
a global polynomial three-ring from the earlier localized
coordinate section or give an original slice to \(S\) or \(T\).
All first-pair, second-pair, and terminal alternatives are now
covered. This completes the last row of the table and proves (2).

## 5. Remaining scope and verification limits

Together with the earlier constant-highest and cubic theorems,
(2) leaves the independent-defect moving sectors of coordinate
flow degrees four and five under the supplied frame, after
their existing individual recognition criteria. It does not
close those sectors or show that an arbitrary sliced action
admits the actual frame (1). No universal frame-height bound,
unrestricted cancellation result, or professor confirmation of
the working field and dimension follows.

This is a synthesis of complete written conditional deductions,
not a new numerical method. The terminal endpoint was independently
reconstructed through EOF before being used here; its actual
coordinate inverses, good-partial cancellation, and rational
recognition hypotheses were checked against the full pass69
statement. The upstream case bounds and theorem scopes were
reread for this exhaustion. Separate audit records must distinguish
author self-review from independent reviews.

Established recognition sources remain those scoped in the linked
proofs. The new source step is Wang's linear-invariant statement as
given in Dasgupta--Gupta, Theorem 3.1(i), over every characteristic-zero
field, with no irreducibility premise in that part. Its statement was
read directly; no fresh complete read of Wang's original proof is
claimed. The constant-top proofs retain the established surface
cancellation endpoint, and rational69 retains its plane and
regular-original-kernel source gates.

No full regression is claimed by this synthesis. Finite controls,
file integrity and AI proof reconstruction are distinct evidence;
none is human expert review, proof-assistant verification or a
historical novelty verdict. Frozen predecessors and shared metadata
are unchanged by this note.
