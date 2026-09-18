# Quadratic-branch recognition and the remaining cubic problem

The exact quadratic relative branch in the supplied nonconical
constant-acceleration frame reduces to a nice polynomial frame.
The new reduction has an explicit polynomial inverse. Combined
with the retained working nice-slice theorem80, it recognizes the
kernel in that branch as a polynomial three-ring.

This is not the general cancellation theorem. The actual
constant-acceleration frame and invariant-plane construction are
hypotheses supplied by earlier conditional work, not available
for every polynomial cylinder. The relative cubic branch also
remains untreated at this checkpoint.

## The short reduction

The full statement and proof are in
[quadratic velocity shear117](quadratic-velocity-shear-pass117.md).
In its notation the actual original-coordinate volume is a unit
in K[v,u]. The relative relation F has degree two, while the
potential Phi has degree at most three. Writing Phi-zeta=HF,
factoring the gradient row of the volume determinant, and using
the units of K[v,u] proves H(y) is a nonzero element of K.
The degree-two evaluation kernel then proves H itself is constant.

Consequently the symmetric cubic tensor T vanishes. For the
moving frame C=[b,b_s1,b_s2] and its connection coefficients G,
the matrix Q=C^(-t) diag(-1,G) C^(-1) has both base derivatives
zero. It is a constant complex symmetric matrix satisfying
b^t Q b=-1. No invertibility of G or Q is required.

The substitution z'=z+(q/2)x_tr^t Q x_tr fixes the other three
original coordinates and has the displayed reverse subtraction
as its inverse. Every new original coordinate is killed by E^2.
The original slice u remains a polynomial slice. This is the
exact input of [working recognition80](nice-slice-recognition-pass80.md).

The new argument needs the actual volume/invariant-plane
framework90 and, for recognition only, the separately retained
theorem80. The global conic and exceptional-fiber arguments91
through116 are not premises. Their earlier quadratic recognition
obligation is superseded by this shorter route; those frozen
notes remain a record of the investigation.

## What the checks establish

The saved proof has independent full-file AI reconstructions by
General and Geometry, including the distinction between formal
H and its evaluation, base-only localization, all signs in the
moving-metric derivative, and the actual global shear inverse.
These are separate readings, not independent human reviews.

[Checker117](quadratic_velocity_shear_checks_pass117.py) has two
methods: the formal connection identity and a nonplanar polynomial
velocity example with constant Q, shear acceleration and inverse
substitutions. The velocity example is coefficient algebra only.
No actual four-coordinate cancellation input is claimed for it.

The [canonical capture117](verification-pass117-working.json)
records three suites and seven passing methods: two new methods
and five retained controls. The reproducible command is:

```sh
/opt/anaconda3/bin/python -m unittest -v \
  research.quadratic_velocity_shear_checks_pass117 \
  research.nonconical_quadratic_potential_checks_pass90 \
  research.normal_row_parameter_checks_pass80
```

The tests do not establish the original-frame hypotheses, the
general degree argument, source-dependent geometric recognition,
or general cancellation. The retained theorem80 has written
AI-audited dependencies but no human expert or formal proof
verification. Historical novelty is unestablished.

## Remaining mathematical obligations

For an exact cubic relation, the same unit argument makes its
multiplier constant but does not remove the cubic part of Phi.
A new argument is required there. The next bounded investigation
examines the affine cubic graph, the remaining volume coefficients
and compatibility of the actual base derivatives.

Even recognizing both relative-degree branches would still leave
the arbitrary-frame entry problem. Transporting a cylinder
derivative supplies a locally nilpotent derivation and a slice,
but not the special acceleration pattern. The original field
and intended dimension in Luo's email are also unconfirmed.

No publication, submission, external contact or public novelty
claim has been made. The full cancellation goal remains unsolved.
