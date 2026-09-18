# Leading derivations: the diagonal-descent gate and loss of properness

Leading-symbol extraction does give intrinsic locally nilpotent
derivations, but that fact and its rank-loss examples were already
established in the project. This pass isolates two further exact
limitations of the proposed transport route:

- Conjugating with an independent translation parameter and then
  identifying that parameter with the slice is a legitimate quotient
  action only when the original derivation already fixes the slice.
- Even a primitive intrinsic leading derivation of an ambient
  coordinate partial can have fixed points and no slice. Properness
  can disappear in an everywhere polynomial leading degeneration.

Both failures occur with a known polynomial quotient. They are
obstructions to specific inference rules, not cancellation
counterexamples or a proof that every nonlinear extraction fails.

## 1. The existing leading-symbol theorem is not new progress

Let B=A[s] be an affine domain over a characteristic-zero field,
with E=partial_s. For an LND T that moves A, write

\[
T|_A=\sum_{j=0}^{q}s^jD_j,\qquad D_q\ne0,
\qquad T(s)=h(s)=\sum_jh_js^j.
\tag{1}
\]

The integer q exists by finite generation of A. No universal bound on
q is assumed. The associated-graded derivation is locally nilpotent.
Its value on s cannot be a nonzero multiple of s: if an LND L on a
characteristic-zero domain satisfies L(s)=sg nonzero, its additive
LND degree gives the contradiction

\[
\deg_L(s)-1=\deg_L(Ls)=\deg_L(s)+\deg_L(g).
\]

Consequently deg_s h<=q, and the top derivation is s^q D_q with
D_q a nonzero LND on A. Commuting original coordinate partials give
commuting intrinsic top derivations. These facts, the possibility of
generic rank one, and nonunit-plinth examples are already in the
[intrinsic-action proof](intrinsic-actions-pass.md) and
[filtration controls](filtration-obstruction-pass.md).

The filtration input is established literature, not a new theorem of
this pass. Alhajjar's Proposition 2.2 states the associated-graded LND
result, attributing it to Daigle; Proposition 3.4 and its proof apply
it to a one-variable extension of a rigid domain.[^filtration]
Thus existence of some intrinsic LND is not the missing bridge here.
The missing conclusion is a sufficiently strong action or family of
actions, rather than merely nonzero leading coefficients.

## 2. Exact criterion for variable-time diagonal descent

Introduce an independent indeterminate z. Extend E and T to B[z]
by killing z, and let theta_z=exp(zE). This is a genuine polynomial
automorphism, with theta_z(s)=s+z and theta_z(a)=a for a in A.
Its inverse is theta_{-z}. The conjugate

\[
F_z=\theta_{-z}\,T\,\theta_z
\tag{2}
\]

is an LND of B[z] that kills z. In the notation (1),

\[
F_z|_A=\sum_j(s-z)^jD_j,\qquad F_z(s)=h(s-z).
\tag{3}
\]

**Diagonal-descent lemma.** The derivation F_z descends through
B[z]/(z-s) if and only if T(s)=0.

**Proof.** A derivation descends through a quotient precisely when
it preserves the defining ideal. Here

\[
F_z(z-s)=-h(s-z),\qquad
F_z(z-s)\pmod{z-s}=-h_0.
\tag{4}
\]

Thus ideal preservation is equivalent to h_0=0, which is equivalent
to s dividing T(s). The LND-degree argument in Section 1 makes that
equivalent to T(s)=0. Conversely this condition visibly preserves
the ideal, so the quotient is indeed an LND. This proof does not
assume a coordinate of B belongs to A.

One can always substitute z=s into the coefficients of F_z restricted
to B. This gives a derivation

\[
\mathcal P(T)=D_0+h_0\partial_s
\tag{5}
\]

of B, with no poles. It commutes with E. But unless (4) vanishes,
it is not a quotient of the LND F_z. Regularity of its coefficients
therefore does not inherit local nilpotence from that family.

This distinguishes three operations often confused in the proposed
argument. Translation by an independent z is invertible. The finite
variable-time Taylor map

\[
g\longmapsto\sum_{j\ge0}\frac{(-s)^j}{j!}E^j(g)
\tag{6}
\]

is the retraction g(a,s)->g(a,0), so it is not invertible and cannot
be used as a conjugating automorphism. Substituting z=s into the
coefficients of a transported derivation is regular but gives (5),
whose quotient interpretation has exactly the gate (4).

For commuting T_i,T_j, the constant horizontal coefficient of their
commutator gives the useful defect formula

\[
[D_{i,0},D_{j,0}]
=h_{j,0}D_{i,1}-h_{i,0}D_{j,1}.
\tag{7}
\]

Thus projecting a commuting ambient frame need not give a commuting
intrinsic frame. If both original derivations fix s, their quotient
derivations are commuting LNDs, but that is an additional hypothesis,
not a conclusion of variable-time transport.

## 3. A regular diagonal projection loses both required properties

Take A=C[a,b,c], and use actual polynomial coordinates on B=A[s]

\[
u=s+a^2,\qquad v=a+u^2,\qquad b,c.
\tag{8}
\]

Their inverse is a=v-u^2 and s=u-(v-u^2)^2. The two coordinate
partials are

\[
T_u=-2(s+a^2)\partial_a+
       (1+4a(s+a^2))\partial_s,
\qquad T_v=\partial_a-2a\partial_s.
\tag{9}
\]

They are commuting LNDs and have their usual coordinate slices.
The first transported family is

\[
F_z=-2(s-z+a^2)\partial_a+
          (1+4a(s-z+a^2))\partial_s.
\tag{10}
\]

It is a coordinate partial over C[z]: it sends s-z+a^2 to one
and kills a+(s-z+a^2)^2. Every coefficient is polynomial in z.
Nevertheless its diagonal value is

\[
\mathcal P(T_u)=-2a^2\partial_a+(1+4a^3)\partial_s.
\tag{11}
\]

For every n>=1,

\[
\mathcal P(T_u)^n(a)=(-2)^n n!a^{n+1}\ne0.
\tag{12}
\]

So this regular diagonal value is not locally nilpotent, even though
it commutes with E. Subtracting its vertical term leaves the same
non-LND horizontal field. The ideal calculation is explicit:
F_z(z-s) reduces to -(1+4a^3), not zero.

Commutation is also lost:

\[
[\mathcal P(T_u),\mathcal P(T_v)]
=4a\partial_a-8a^2\partial_s\ne0,
\tag{13}
\]

whereas [T_u,T_v]=0. The intrinsic horizontal bracket is
[-2a^2*partial_a,partial_a]=4a*partial_a, agreeing with (7).
The coordinate example in (8) was already used in the earlier
filtration note to refute constant-coefficient local nilpotence.
Here it also verifies the exact diagonal-descent obstruction and
the commutation defect; it is not presented as a newly discovered
cancellation example.

## 4. A regular leading degeneration need not preserve properness

There is an everywhere polynomial realization of the top symbol in
(1). Add an independent lambda and define an A[s,lambda] derivation
killing lambda by

\[
\begin{split}
T_\lambda|_A&=\sum_{j=0}^{q}
  \lambda^{q-j}s^jD_j,\\
T_\lambda(s)&=\sum_{j=0}^{q}
  \lambda^{q+1-j}s^jh_j.
\end{split}
\tag{14}
\]

All exponents are nonnegative. Over lambda invertible, this is
lambda^q times the conjugate of T by the scaling s->s/lambda.
Consequently it is locally nilpotent there. Its iterates on a finite
set of generators then vanish already in the unlocalized domain,
so it is an LND on the whole polynomial family. At lambda=0 it
specializes to s^qD_q.

If T was a coordinate partial, every nonzero complex lambda fiber
is a coordinate translation after rescaling its slice. But nothing
in this construction makes the special action proper. For q>0 its
entire divisor s=0 is fixed. Dividing the known common factor s^q
gives the intrinsic D_q as a globally polynomial derivation, not a
rational field with poles. That valid division still does not prove
that D_q is proper, fixed-point-free or sliced.

The following primitive example shows why merely removing common
factors cannot repair the conclusion.

## 5. A primitive intrinsic symbol can still have a fixed locus

Let A=C[a,b,c] and

\[
D=a\partial_b+b\partial_c,
\qquad T=D+\partial_s\quad\text{on }A[s].
\tag{15}
\]

The following are genuine polynomial coordinates:

\[
\alpha=a,\qquad \beta=b-as,\qquad
\gamma=c-bs+as^2/2,\qquad s,
\tag{16}
\]

with inverse

\[
a=\alpha,\quad b=\beta+\alpha s,\quad
c=\gamma+\beta s+\alpha s^2/2.
\tag{17}
\]

In this frame T is partial_s. It also commutes with the original
E=partial_s in the frame a,b,c,s. Its filtration degree is zero,
and its intrinsic leading derivation is exactly D.

The derivation D is primitive: its nonzero coefficients a,b have
gcd one. However, its image is contained in the proper ideal (a,b),
and its fixed locus is the line a=b=0. It therefore has no slice.
Its additive action is not proper: the stabilizer at each fixed
point is the nonproper group Ga, whereas a fiber of the action
graph of a proper action would be proper. This failure remains
after removal of every possible common polynomial coefficient.

In this case (14) is simply

\[
T_\lambda=D+\lambda\partial_s.
\tag{18}
\]

For lambda nonzero, use s/lambda in (16) and take that as the slice.
This gives explicit coordinate translations, with rational-in-lambda
coordinate formulas. At lambda=0 the polynomial vector field is D,
whose fixed locus on four-space is a=b=0. The vector field extends
regularly; its translation coordinates need not extend across that
parameter divisor. Properness does not follow from regularity of
the family or primitivity of its intrinsic special symbol.

This control does not say that every leading direction from every
ambient frame is bad. The quotient in the example is already
polynomial and other coordinate directions can recover it. It
refutes the automatic properness of an extracted primitive direction,
not all possible nonlinear frame-selection algorithms.

## 6. Verification, primary source and exact remaining gap

An independent inline SymPy calculation checked (16)--(17) in both
directions, their coordinate-partial identities, primitivity and the
fixed-locus coefficient vanishing, the coordinate formulas for (18)
after lambda localization, the transported coordinate identities in
(10), and eight instances of (12). It completed in 0.040 seconds of
measured script time. A separate exact check verified [T_u,T_v]=0
and the nonzero projected bracket (13). The universal recurrence
and the descent and degeneration lemmas have written proofs above.
No new regression methods or test suite are being counted.

A separate model audit independently reconstructed the diagonal
ideal calculation, the LND-degree implication, the primitive
coordinate control and its nonproper special fiber. No defect was
found. No registry, public posting, or expert-contact action occurred.

The genuinely general top-symbol theorem remains available, with
finite polynomial coefficients and commuting top actions. This pass
does not strengthen it to a proper intrinsic action. It identifies
an exact obstruction to the proposed variable-time descent, and
shows that even primitiveness does not promote a valid top symbol
to the required action. A successful universal argument still needs
a new selection or construction that supplies properness, enough
independent directions, or another valid recognition hypothesis.

[^filtration]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2 on printed p. 4, and Proposition 3.4 with its complete proof on printed p. 7, read directly in the primary manuscript. These support the established associated-graded and one-cylinder arguments, not a properness theorem or the new project-specific inference tests. No absence-based novelty assertion follows from this bounded source check.
