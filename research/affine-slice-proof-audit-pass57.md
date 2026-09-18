# Independent audit of the affine-slice module and faithful boundary

Both complete current proofs,
[the affine-slice module](affine-slice-module-pass57.md) and
[the faithful quadratic boundary](faithful-quadratic-slice-boundary-pass57.md),
have been independently read through their ends and reconstructed.
No mathematical correction is requested. The boundary distinguishes
actual generation over the invariant base from an actual ambient
coordinate frame at a concrete surviving point.

## 1. The finite module and its exact ideal

The three second-derivative kernel equations recover exactly the
affine-linear generic functions. The actual determinant fields then
put all three coefficients of \(\Delta F\) in \(R\), including
the constant coefficient. Thus the stated coefficient lattice is
finite of rank three and is isomorphic to \(V\). The full
\(\Delta\)-multiplicities remain in its membership condition.

Localization of these actual kernel equations gives the correct
height-one modules. Intersecting them inside the generic affine
space gives exactly \(V\), by the inherited actual-ring
intersection. I directly read the complete statements and proofs
of [Stacks Tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) and
[Stacks Tag 0B3N](https://stacks.math.columbia.edu/tag/0B3N) in this
audit. Their hypotheses give reflexivity and then freeness of this
finite rank-three module over the regular local surface.

Faithful flatness is used in the precise next step:
\(1\notin\mathfrak mV\), because otherwise the actual closed
fiber of \(\mathcal B\) would be empty. This extends \(1\) to
an actual module basis \(1,u,v\). It does not prove that
\((Eu,Ev)\) is the unit ideal.

The image of \(E\) on \(V\) is a base ideal because its values
are both actual and generically constant. The displayed lattice
formula, the inclusion of the bad speeds and good accelerations,
and the exact kernel \(F_1(\mathcal A)\) all follow with their
stated actual hypotheses. Hence unitness of this ideal is exactly
affine generic slice selection, not a consequence of freeness or
of the existence of an arbitrary supplied slice.

## 2. The faithful control and the all-slices minimum

For
\[
R=\mathbb C[a,v]_{(a,v-1)},\qquad
\mathcal A=R[t,z]/(t^2-v-az),\qquad
\mathcal B=\mathcal A[s],
\]
the invariant localization description and injectivity of the
base embedding are valid. The monic basis \(1,t\) over \(R[z]\)
proves faithful flatness. Since \(v\) is a unit, the relative
Jacobian ideal \((a,2t)\) is the unit ideal; this proves the stated
relative smoothness. The two-component closed fibers are nonempty.

The same monic decomposition proves \(\ker D=R\) and
\(F_1=R\oplus Rt\) for \(D=a\partial_t+2t\partial_z\).
Its full plinth and second image are both \(aR\). Therefore this
example has no second-image obstruction point. The fact that the
derivative ideal is the unit ideal does not turn the nonunit full
plinth into a slice.

Both identities
\(aq=tw-vz\) and \(vs=tq-zw\) are exact in the actual ring.
They give the supplied slice using only the unit \(v\), not the
nonunit \(a\). All inverse generator formulas and both generic
quadratic expressions check. The bad speeds \(a,av\) are
algebraically independent over \(\mathbb C\); their common factor
\(a\) is not removed. Both good accelerations are exactly \(2a^2\).

Every actual slice is \(s+H\) with \(H\in\mathcal A\), so its
gauge relative to \(w/a\) belongs to the full coset
\(-tz/a+\mathcal A\). Odd-part extraction from a hypothetical
degree-at-most-two gauge would put
\(t(-z/a-\lambda)\) in \(\mathcal A\). The monic basis then
requires \(-z/a-\lambda\in R[z]\), contradicting the coefficient
\(-1/a\). This excludes all actual slices of that gauge degree,
not merely a selected replica family. The supplied gauge has
degree three, proving the exact minimum.

For every gauge of degree \(n\ge3\), the projected first good
generator has degree exactly \(2n\), from its nonzero square term.
The remaining projections have degree at most \(2n\). Thus this
particular projected list has minimum six, although the intrinsic
algebra already has degree-one and degree-two generators \(t,z\).

Finally, comparison of coefficients in \(\mathcal A[s]\), then
in its monic \(1,t\) decomposition, proves exactly
\(V=R\oplus Rt\oplus Rw\) and \(E(V)=aR\). This is an actual
proper affine-slice ideal with a free rank-three module and a
supplied slice outside that module.

## 3. The decisive frame boundary and verification scope

At the surviving actual point \((a,t,z,s)=(0,1,0,0)\), the four
listed differentials are
\[
dQ_1=dz,\qquad dQ_2=ds,\qquad dX=dz,\qquad dY=dz+dt.
\]
Their rank is three. Hence the selected list is not even a local
coordinate system, despite being four actual generators over
\(R\) in an invariant localization of polynomial affine
four-space. The missing ambient-frame condition is disproved for
this list, rather than silently assumed from generation.

An independent inline exact SymPy calculation checked the two
polynomial identities, both accelerations, and the ambient
Jacobian. This adds no standalone suite, reusable test method, or
full regression. The all-slices minimum and the module conclusions
are established by the written algebra, not inferred from that
finite calculation.

Neither audited note proves that an actual second-image obstruction
exists, that the full supplied adjoint frame can be replaced by the
weaker quadratic-generator data, or that complex-threefold
cancellation is settled.
