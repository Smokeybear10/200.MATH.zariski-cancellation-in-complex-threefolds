# Independent audit of the simple common-speed-zero exclusion

The complete
[simple-speed-zero proof](simple-speed-zero-exclusion-pass60.md)
was read through its final scope paragraph and reconstructed
independently. No mathematical correction is requested.
This is an AI proof and scope audit, not human expert review
or a formal proof-assistant verification.

## 1. The local eigenfunction argument

The hypothesis \((f,g)R=\mathfrak m\) is used on the actual
smooth invariant surface. It makes the speed Jacobian in
the invariant coordinates a unit and therefore makes the
unique field partials \(\partial_f,\partial_g\) preserve
the local ring. It does not make \(f,g\) global polynomial
coordinates.

The Euler derivation acts as multiplication by \(n\) on
the degree-\(n\) associated-graded piece. Every nonzero
local rational germ has finite order, since its denominator
is a local unit and its numerator is a nonzero polynomial.
Consequently an eigenfunction of integer weight \(d\)
has order exactly \(d\). Subtracting its homogeneous
degree-\(d\) initial polynomial in the actual functions
\(f,g\) leaves an eigenfunction of greater order, which
must vanish. This proves an exact equality of germs,
not merely a statement about a finite Taylor jet.

No completion, convergence, global equality
\(L=\mathbb C(f,g)\), or unstated polynomial-coordinate
inverse is needed.

## 2. Actual recovery of the rational linear terms

The proof applies the eigenfunction lemma first to the
actual accelerations \(h_i\in R\), making their Hessians
constant and their gradients regular. It does not apply
the lemma prematurely to the initially rational \(k_i\).

The actual identity
\[
Ex_i=\tfrac12(\nabla h_i)(X,Y)^{\mathsf t}+k_i
\]
puts \(k_i\) in \(\mathcal B\cap L=R\). The weight-one
lemma is then applicable. The constants \(\ell_i\) are
recovered only after the now-regular quadratic and
linear terms have been subtracted from actual generators.

Thus the full equality \(\mathcal B=R[X,Y]\) uses every
original ambient coordinate, rather than replacing the
actual ring by a generic parametrization. The supplied
arbitrary slice is used afterward. Evaluation of its
derivative ideal at \(X=Y=0\) is legitimate at this
stage and contradicts \((f,g)R=\mathfrak m\).

## 3. Exact scope of the consequences

The Jacobian radical inclusion follows from vanishing
at every complex common speed zero. The isolated-zero
corollary is also exact: a reduced Artinian local
quotient would be the residue field and would force
\((f,g)R=\mathfrak m\). The proof does not eliminate
nonreduced isolated zeros or assert that common
divisor components are nonreduced.

The extra parameter-speed premise in
[pass55, Sections 4--5](slice-leading-image-obstruction-pass55.md)
was reread directly. That earlier sector imposed
\((f,g)R=\mathfrak m\) separately from
\(JR=\mathfrak m\) and the zero-first-jet conditions.
The new theorem excludes that entire stronger sector.
It does not exclude a reduced intrinsic second-image
point from \(JR=\mathfrak m\) alone. The earlier
conditional lower-bound implication remains valid,
but is not evidence that such a full-frame point exists.

The ramified base control in the new proof has the
stated Euler weights, rank-two accelerations, and
Hessian/gradient poles. It is expressly not an actual
full graph or an action satisfying all frame hypotheses.
The nonlinear unramified control correctly shows that
a nontrivial global algebraic speed-field extension
does not invalidate the local theorem.

## 4. Independent checker read and run

The complete
[two-method checker](simple_speed_zero_checks_pass60.py)
was read before execution. Both methods passed
independently in **0.060 seconds**, exit zero:

- the nonlinear unramified speed coordinates use the
  actual rational field partials and produce the
  displayed constant Hessians;
- the ramified speed coordinates retain the weights
  while their actual partials produce the stated poles.

These checks are exact symbolic boundary controls.
They do not prove the universal eigenfunction lemma
or construct an actual frame. No additional methods
or example-grid counts were introduced by this audit.

## 5. Discarded tangent-control provenance

During the preceding divisor investigation, the proposed
base example
\[
f=a,\quad g=a+a^2b,\quad
h=(g-f)^3/f=a^5b^3
\]
was initially considered as a possible Hessian-pole
control. Direct differentiation showed that inference
was false: for example \(h_{gg}=6ab\), and every
Hessian entry is regular at \(a\). That candidate was
discarded, not used in either theorem.

The separate pass59 note instead uses
\(g=a+a^3b^2\), \(h_2=a^3b\), whose actual extended
field derivative has \(h_{2,gg}=-1/(4a^3b^3)\).
The pass60 proof has its own explicitly ramified
square-speed control. The discarded candidate is
recorded here only as mathematical search provenance,
not as a failed assertion in the successful checker
or a correction to the final pass60 argument.

