# Common intrinsic quotient and the remaining variable-acceleration problem

The supplied three-good-coordinate class now has a common intrinsic
additive quotient containing every good speed. If the remaining coordinate
is quadratic along the original action, its acceleration belongs to that
same quotient. In dimension four this is an actual polynomial plane,
and it gives an unconditional square-membership result that was previously
left open at embedded critical points.

The full cancellation question is not solved. No argument here makes an
arbitrary sliced action admit three good coordinates, recognizes every
action that does admit them, or verifies historical novelty.

## 1. The precise progress

In the actual sliced frame
\[
 B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
 E=\partial_u,\qquad E^2x_i=0,
 \qquad a_i=Ex_i,
 \tag{1}
\]
assume some \(a_i\ne0\). The
[common intrinsic quotient proof](three-good-intrinsic-speed-quotient-pass125.md)
produces a nonzero \(N\in\operatorname{LND}(A)\) with
\[
 N(a_i)=0,\qquad S=\ker N\simeq\mathbb C^{[2]},
 \qquad S\subset A\subset B\text{ faithfully flat}.
 \tag{2}
\]
There is no degree assumption on \(z\). When its time degree is positive,
\(N\) also kills its leading coefficient. In particular, if
\(E^2z=q\in A\), then \(q\in S\).

The construction is the highest \(u\)-degree part of the actual partial
\(T=\partial_z\). The general leading-LND mechanism is published and
already used in this project. The additional coefficient identity says
that this chosen intrinsic action fixes the specified speeds and leading
acceleration, rather than merely establishing that some action exists.
The [separate volume proof](three-good-speed-rank-bound-pass125.md)
independently proves the weaker consequence
\(\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3]\le2\).
It is not counted as a second independent structural advance.

For the quadratic case put \(J=(a_1,a_2,a_3)S\) and \(I=JB\).
The [square proof](three-good-acceleration-square-pass125.md) now gives
\[
 \boxed{q^2\in J,\qquad q^2\in(a_1,a_2,a_3)A,\qquad q^2\in I.}
 \tag{3}
\]
The proof contracts the earlier strict return certificate to the same
polynomial plane and applies dimension-two Briancon-Skoda. A separate
support reconstruction shows why the old possible square-defect lines
cannot survive a faithfully flat quotient with two-dimensional ambient
fibers. Both arguments retain nilpotents and embedded components.

The published inputs are separately scoped in the
[source audit](source-audit-pass125.md) and the square proof's source
section. In particular, polynomiality and flatness of the quotient are
the retained Kaliman--Saveliev application, not consequences of algebraic
dependence alone. No new homogenization or Briancon-Skoda theorem is claimed.

## 2. Where first-power failure would have to occur

First-power membership \(q\in J\) is still unproved. There is a useful
precise description of its possible support. Assume \(q\ne0\) and
\(J\) proper, and put
\[
 M_1=S\bar q\subset S/J,
 \qquad M_1\simeq S/(J:q).
 \tag{4}
\]
The return certificate gives \(q\in\overline J\). At a height-one
prime of \(S\), the localized ring is a discrete valuation ring and
every ideal is integrally closed. Thus \(M_1\) vanishes there, and
also at the generic point. Since \(S\) is a two-dimensional affine
ring and \(M_1\) is finite, its support is a finite set of closed points.

There is no defect at a point where \(J\) contains a function with
nonzero linear part. Indeed such an element \(f\) is part of a regular
system of parameters of the regular local ring \(R=S_{\mathfrak m}\).
The quotient \(R/(f)\) is a discrete valuation ring. The image of
\(q\) is integral over the image of \(J\), as seen by reducing a
monic equation. Every ideal of this quotient is integrally closed,
including its zero ideal. Thus that image lies in the image ideal,
and \(q\in JR\), since \(f\in J\).

Consequently
\[
 \operatorname{Supp}M_1\subseteq
 \{\mathfrak m\in V(J):J S_{\mathfrak m}
                          \subseteq\mathfrak m^2S_{\mathfrak m}\}.
 \tag{5}
\]
This is a necessary condition for a defect, not the assertion that
every such critical point supports one. If \(J\) is principal,
normality of \(S\) already gives \(q\in J\); the issue concerns
nonprincipal ideals at these points.

Flat base change identifies the ambient first-power defect with
\(M_1\otimes_S B\). If \(M_1\ne0\), its support contains the entire
nonempty two-dimensional ambient fiber over each base support point.
This does not contradict the previously known codimension-two bound:
that bound permits support of dimension two in \(B\). The argument
which settled the square case therefore stops at exact dimensional
compatibility for the first power.

The bare ideal example \(J_0=(s^3,t^3)\), \(h=s^2t^2\), confirms
that strict integral containment and (3) do not formally settle this
step. Its defect occurs at the critical origin and \(h^3\in J_0^4\),
but \(h\notin J_0\). It is not an actual coordinate action. Any use
of it as a cancellation example would discard the strongest hypotheses.

## 3. Recognition remains a separate obligation

The common intrinsic derivation need not be free merely because it was
extracted from a coordinate translation. The new argument proves neither
freeness of \(N\) nor freeness after primitive invariant-factor division.
The general leading-symbol fixed-point controls were already known;
they are not automatically controls satisfying all three-good hypotheses.

Likewise the speed row need not be a unit row. The actual sliced control
\(E=a^2\partial_x+(1+ax)\partial_y\) has good speeds \((0,a^2,0)\)
and acceleration \(a^3\). Its exact inverse is recorded in81 and
checked again here. It has a proper speed ideal and even
\(q\notin I^2\), while \(q\in I\) and its kernel is polynomial.
Do not confuse \(q^2\in I\) with \(q\in I^2\).

Even first-power membership would not alone produce an allowed
coordinate change: the fixed-good-coordinate shear equation is
\(E^2F=q\) for \(F\in\mathbb C[x_1,x_2,x_3]\), whose left side
lies in \(I^2\). That much stronger membership and the polynomial
equation itself are additional requirements. The actual control just
given rules out this shear while admitting a different full inverse.

The next bounded mathematical task is to exploit the original coordinate
and slice identities over the finite critical base set in (5), or to
prove freeness of an appropriate intrinsic action. Either task must
retain the global polynomial inverse requirements. A formal quotient
model or a generic-field parametrization does not suffice.

In parallel, unrestricted entry remains a distinct major issue. Under
the retained working recognition results, the first possible minimum
coordinate-degree profile of a hypothetical counterexample is
\((2,1,1,1)\), but larger minimum degrees remain possible. This pass
constrains that first profile; it does not reduce the full problem to it.

## 4. Exact verification scope

The three proof notes have full-file independent AI reconstructions.
The rank proof has seven numbered equations, the common-quotient proof
eight, and the square proof eight. These are written proofs relying on
explicitly stated published inputs, not formal proof-assistant certificates.

The [new control suite](three_good_controls_pass125.py) has three methods:
an actual nonconstant-acceleration frame with a proper speed ideal and
degree-zero leading extraction; an actual three-good family with last
time degrees two, three and five and positive leading shift; and a
square-zero quotient inverse plus an ideal-only first-power boundary.
The actual frames are checked in both inverse orders. These examples
test formulas and scope distinctions, not the universal theorem.

The canonical targeted run is

```sh
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python -m unittest \
  research.three_good_controls_pass125 \
  research.strict_slice_checks_pass84 \
  research.embedded_square_controls_pass84 -v
```

It passed six methods in three suites: three new methods and three
retained methods. The retained methods check actual rational-return
certificates and non-realizable ideal controls. Their repeated passage
is not new coverage. All three source hashes were unchanged before and
after the run. Exact execution evidence is in
[verification125](verification-pass125-working.json).

The previous user check-in was a status read, not mathematical progress.
This pass adds the common-quotient application and removes the square
defect. Full cancellation remains unsolved. Human expert review,
formal verification and historical novelty clearance have not occurred.
No external contact, submission, public posting or automation was made.
