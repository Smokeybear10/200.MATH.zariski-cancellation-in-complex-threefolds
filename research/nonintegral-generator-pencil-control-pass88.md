# A universal generator pencil need not give integrality

The universal pencil in the
[preceding algebra lemma](universal-generator-pencil-pass88.md)
does not by itself make its slope integral over the coefficient
ring. The following algebra-only control has an even stronger
tensor property: the two slope images agree before reduction.
The missing faithful-flat and actual-action hypotheses remain
substantive.

## 1. Exact relative generation in a Laurent ring

Take
\[
R=\mathbb C[v^2,v^3],\qquad
c=v^{-2},\qquad h=v^{-1},\qquad
A=R[c]=\mathbb C[v,v^{-1}]
       =R[(v^2)^{-1}].
\tag{1}
\]
For example v=v cubed times c and v inverse=v cubed times c
squared belong to R[c], proving the claimed equality; the opposite
inclusion is immediate. With an independent polynomial parameter
tau set d=c+tau h. Then the following are exact Laurent identities:
\[
v=v^3d-\tau v^2,\qquad
h=vd-\tau=v^3d^2-\tau v^2d-\tau,\qquad c=h^2.
\tag{2}
\]
The occurrences of v squared and v cubed on the right are in R.
Thus both Laurent generators v,h lie in R[tau,d], and (2) proves
\[
A[\tau]=R[\tau,c+\tau h].
\tag{3}
\]
This is a relative subalgebra equality. It is not an endomorphism
of A over R sending c to d, since that substitution need not
preserve the relations of c over the embedded coefficient ring.

## 2. No integrality, even with exact tensor agreement

Let ord_v be the order of a nonzero rational function at v=0.
Every nonzero element of R has nonnegative order and ord_v(h)=-1.
If h satisfied a monic equation of degree n over R, its leading
term h to the n would have order -n, while each other nonzero term
would have order at least -(n-1). A unique lowest-order term cannot
cancel. Therefore h is not integral over R.

The localization in (1) has a simple tensor square:
\[
A\otimes_R A\simeq A,
\qquad c\otimes1=1\otimes c,
\qquad h\otimes1=1\otimes h.
\tag{4}
\]
For clarity, both copies of v squared equal the same element of R
in the tensor product. Their inverses consequently agree, so the
two copies of c agree. Since h=v cubed times c squared, their
copies of h agree too. Equivalently multiplication is the usual
isomorphism from the tensor square of a localization to itself.
Thus even exact agreement on the tensor square, stronger than
the nilpotent-difference conclusion of the preceding lemma, does
not descend h into R here.

The extension R to A is flat but not faithfully flat: the proper
ideal (v squared,v cubed) becomes the unit ideal after localizing.
It is also not finite, since finiteness would imply integrality of
h. No claim is made that the actual extension R to A in the
three-good-coordinate problem has these properties.

This control is not an actual kernel in that problem. It already
has the nonconstant unit v, whereas an actual A with A[u]=C to
the fourth has only nonzero constant units. Taking a product with
an affine plane would give a smooth factorial three-dimensional
ring, but would retain this same unit obstruction and would not
give the required contractible kernel or original coordinate frame.
The example only rules out integrality arguments based on the
abstract pencil or its tensor consequence alone.

## 3. Finite control and provenance

The standalone
[one-method Laurent checker](nonintegral_generator_pencil_checks_pass88.py)
checks the exact recovery identities, the localization presentation,
and the valuation pattern for the specified element. Its finite
checks do not prove the arbitrary-degree monic contradiction,
which is the written order argument above, or construct an actual
action. It imports only unittest and SymPy.

Root supplied this control. Jet independently reconstructed the
relative recovery, nonintegrality argument, and tensor localization
boundary. These are separate new pass88 files; the earlier cusp
proof and checker, and all pass87 or older files, are unchanged.
The author's actual one-method run passed in 0.029 seconds,
exit zero, with the full stdout retained in tool chunk b0121c.
The complete proof and code were read through EOF afterward,
with no correction. Final hashes are reported separately.
No runner, full regression, or actual-action realization was added.
