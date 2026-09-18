# Cubic velocity exclusions and the local-to-global obstruction

The exact cubic branch has a new global exclusion under the supplied
nonconical constant-acceleration frame. Its velocity cannot be
b=(s,p(s,t),f(s)), where s,t are actual polynomial coordinates of
the intrinsic invariant plane, p_t is nonzero and f is polynomial
in s. The exclusion applies even when a polynomial pullback makes
the speed row globally unimodular.

There is also a necessary condition for the general cubic branch:
its leading relative coefficient defines a rational direction on
the base with a nonconstant rational first integral. Neither result
recognizes every cubic branch or puts an arbitrary cancellation
input into the special frame. General complex-threefold cancellation
remains unsolved.

## The polynomial-pullback exclusion

The complete [pullback proof](cubic-polynomial-pullback-exclusion-pass118.md)
retains the actual original coordinates, a polynomial slice and
the intrinsic invariant plane from88--90. It does not assume that
(s,t) to (s,p) has a global polynomial inverse, or even that
C(s,t)=C(s,p). Instead it uses the commuting rational derivations
D_p=(p_t)^(-1)partial_t and
D_s=partial_s-(p_s/p_t)partial_t.

Their exact constant field is the decisive transfer gate:
ker D_p=C(s). The relative generators undergo an invertible
K-linear change, and the original volume changes by a base unit.
Consequently the whole coefficient calculation of the
[cylinder proof](cubic-cylinder-velocity-exclusion-pass118.md)
remains valid. The two potential and volume expressions for a
scalar slope give a rational differential equation. Laurent
coefficients force f=a s^3+c s and rho=A(s)+c0 p.

The global step is short. The original affine-linear coordinate
X=x3-cx1 equals
3a s^2x1-2a s^3u-2a s^3rho.
The full invariant-kernel intersection puts s^3rho in S, and
then s^3A(s) is polynomial in s. It follows that X has a complex
constant residue modulo s. Thus the nonconstant invariant s
divides an irreducible affine-linear coordinate X-h0 in the
actual polynomial four-ring. They must be constant associates,
contradicting EX=a s^3 and Es=0.

This last argument uses original-coordinate irreducibility, not
just a generic Jacobian or a nonvanishing speed row. The literal
cylinder exclusion is a prerequisite scalar argument, not an
additional independent solved branch.

## A constraint that does not require that velocity form

The [moving-frame proof](cubic-moving-frame-constraint-pass118.md)
treats an arbitrary exact cubic relative relation inside framework90.
A K-affine fiber change writes its two relative generators as
y=D+vX+v^3V. The base vector fields X,V need not commute.

All positive coefficients of the actual unit volume determinant
give explicit connection conditions. Comparing the cubic potential
gives a nonzero rank-one tensor T=tau ell^3. The corresponding
quadratic velocity form Q obeys
partial_i Q=-tau ell_i n n^t.
It is constant along V, but not in both base directions.

A nonconstant entry of Q is therefore a rational first integral
of V. Its invariant field L has transcendence degree one.
After normalizing one component, the normal vector also lies
over L. Over that field the velocity lies in a fixed plane and
the fixed quadratic level b^tQb=-1.

The proof does not make L=C(s) for an actual polynomial base
coordinate, make V locally nilpotent, or show that an allowed
original-coordinate change puts b in the excluded pullback form.
Those are missing deductions, not consequences of the word
"rational" or of a rank-one tensor.

## An exact local example prevents an invalid shortcut

The [principal-open control](cubic-principal-open-frame-control-pass118.md)
has b=(s,t,s^3), an exact cubic relation, constant original-coordinate
Jacobian -2 and a complete inverse after s is inverted. The slice
equals (3 Sigma^2 X1-X3)/(2 Sigma^3), where
Sigma=X2-ZX3+X1^3/2. At an explicit point of Sigma=0 its
numerator is nonzero, so the transported action does not preserve
the original polynomial ring.

The pullback t_old=st-1 makes the speed row globally unimodular.
Its localized inverse and cubic compatibility remain valid, and
the slice retains its pole. Thus even these stronger local
conditions do not imply a global sliced polynomial frame.
The new pullback theorem excludes this entire velocity form by
a global argument; it does not invalidate the localized example.

This is not a cancellation counterexample. It is an exact
counterexample to promoting the listed local conditions alone
to global polynomiality.

## Verification and dependency review

The [canonical capture118](verification-pass118-working.json)
records four suites and seven passing methods, four new and
three retained. Two new checker files separate the
[cubic coefficient and open-model controls](cubic_moving_frame_checks_pass118.py)
from [rational-base transfer controls](cubic_pullback_transfer_checks_pass118.py).
The latter includes a generically degree-two base map, not only
a birational substitution. Reproduce the capture with:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.cubic_pullback_transfer_checks_pass118 \
  research.cubic_moving_frame_checks_pass118 \
  research.quadratic_velocity_shear_checks_pass117 \
  research.nonconical_quadratic_potential_checks_pass90
```

The new written proofs have independent full-file AI
reconstructions. The symbolic checks verify identities and
explicit examples. They do not verify the universal constant-field
argument, global kernel intersections, irreducibility endpoint,
entire retained geometric theorems or the full conjecture.

The separate [adversarial dependency audit](nice-recognition-adversarial-dependency-audit-pass118.md)
rechecks selected no-apex, quadric and good-direction routes of
working theorem80 against primary de Bondt and Kaliman--Saveliev
statements and proof passages.[^bondt][^ks] No invalidating gap
was found in those reconstructed portions. Deeper and separately
retained dependencies remain explicitly outside that new audit.
The cubic exclusions do not invoke theorem80.

The quadratic reduction117 still uses theorem80 for recognition,
with its working-result qualification. A search for nearby
centroaffine classification did not supply an applicable substitute:
the inspected Hildebrand abstract requires nondegeneracy and
Levi-Civita parallelism, neither established here.[^hildebrand]
No comprehensive novelty clearance, human expert review or formal
verification has been completed.

## Next mathematical task

The first-integral theorem should now be used to study the
remaining velocity geometry and its bad divisors. A useful next
test is whether the invariant field can have a polynomial base
coordinate and what the plane/quadratic constraint then forces
for a globally unimodular polynomial velocity. Any argument must
retain the distinction between a rational base change and an
actual original-coordinate automorphism.

The explicit principal-open countermodel makes a repeated
generic-volume-only attempt insufficient. A proposed extension
must identify and prove its global gate, or produce a decisive
counterexample to that extension.

Even a full cubic-frame recognition theorem would leave the
arbitrary-frame entry problem. Luo's intended field and dimension
remain unconfirmed. No publication, submission, public novelty
claim, paid resource or external contact has been undertaken.

[^bondt]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*,
arXiv:1501.04845v3](https://arxiv.org/html/1501.04845v3), Definition3.7,
Theorems3.8(i) and5.1(iv). Exact selected proof-read scope is in
the dependency audit, not a claim to have re-proved every source input.

[^ks]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible
threefolds*, author-hosted final paper](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
Lemma2.1, Theorem2.7 and Corollary2.8. The audit distinguishes these
reads from their deeper topology and surface-classification inputs.

[^hildebrand]: Roland Hildebrand, [*Centro-affine hypersurface immersions
with parallel cubic form*, arXiv:1208.1155v4](https://arxiv.org/abs/1208.1155v4),
revised January4,2013. Primary abstract/version history checked
only for the applicability boundary.
