# Nonlinear cross-frame saturation recovers the full intrinsic LND span

Date: 2026-09-13.

Under the full hypothesis
\[
B=A[s]=\mathbb C[x_1,x_2,x_3,x_4],\qquad E=\partial_s,
\tag{1}
\]
the leading coordinate actions from **all** nonlinear ambient frames
detect exactly the intrinsic Makar-Limanov invariant. More strongly,
start with any one nonzero intrinsic field obtained by this extraction.
Its conjugates under intrinsic additive actions already span, over
\(\operatorname{Frac}(A)\), every intrinsic locally nilpotent direction.

Consequently the three-field determinant certificate of
[pass 32](stable-polynomial-invariants-pass32.md) exists if and only if
\(\operatorname{ML}(A)=\mathbb C\). The previously missing necessity is
proved below. This does **not** show that either condition always holds.
A finite rank-augmentation step is proved, but its input includes an
intrinsic LND outside the current span. Producing that input from (1)
alone is still unresolved.

No cancellation, novelty, expert-review, or proof-assistant claim is made.
The leading-filtration, replica, and algebraically generated group
mechanisms have the inherited credit recorded in Section 7.

## 1. The extracted family and its nonzero seed

Call a derivation \(T\) an actual coordinate LND if some genuine
polynomial coordinate system on \(B\), with a polynomial inverse, makes
\(T\) one of its coordinate partials. All polynomial frames are allowed,
not only affine-linear changes of a prescribed one.

For such \(T\), let \(q\geq0\) be its largest nonzero adjoint order and put
\[
K_T=\frac{1}{q!}(\operatorname{ad}E)^qT,
\qquad h_T=K_T|_A.
\tag{2}
\]
The polynomial conjugate
\(\exp(tE)T\exp(-tE)\), for an independent parameter \(t\), proves that
\(q\) is finite. Its highest coefficient \(K_T\) is an LND: in a
sufficiently high iterate on any element, the coefficient of the highest
possible power of \(t\) is the corresponding iterate of \(K_T\), so it
vanishes. Also \([E,K_T]=0\), hence \(h_T\) is an LND on \(A\), possibly
zero. Define
\[
\mathcal H_E=\{h_T\ne0:T\text{ is an actual coordinate LND on }B\}.
\tag{3}
\]

It is important to prove that this set is nonempty. Some original
coordinate partial moves \(A\), because their common kernel is
\(\mathbb C\), whereas \(\dim A=3\). For such a \(T\), choose finite
algebra generators \(a_j\) of \(A\), and put
\(e=\max_j\deg_sT(a_j)\geq0\). We claim
\[
\deg_sT(s)\leq e.
\tag{4}
\]
If instead \(\deg_sT(s)=m\geq e+1\), the highest derivation for the
\(s\)-filtration has degree \(m-1\geq0\) and sends \(s\) to
\(c s^m\ne0\), with \(c\in A\). This contradicts the characteristic-zero
LND rule that \(u\mid D(u)\) forces \(D(u)=0\). The associated-graded
derivation is an LND by the inherited filtration theorem.[^filtration]
Thus (4) holds. Its ordinary largest adjoint order is \(e\), and some
\(a_j\) has a nonzero coefficient of that degree. Therefore \(h_T\ne0\).

This reasoning is intrinsic to the actual polynomial cylinder. It does
not assume that \(A\) is polynomial or that an ambient coordinate is
already \(E\)-invariant.

## 2. A general replica-conjugation lemma

Let \(A\) now be any finitely generated complex domain,
\(F=\operatorname{Frac}(A)\), and let \(\mathcal N\) be a nonempty set of
nonzero LNDs on \(A\). Suppose that \(\mathcal N\) is closed under
conjugation by the **full** group \(\operatorname{SAut}(A)\), generated
by every intrinsic LND flow. Then
\[
\operatorname{span}_F\mathcal N
=\operatorname{span}_F\operatorname{LND}(A).
\tag{5}
\]
No smoothness, factoriality, finite generation of an LND kernel, or
finite-dimensional Lie algebra is needed for this lemma.

Write \(V=\operatorname{span}_F\mathcal N\). For \(L\in\operatorname{LND}(A)\)
and \(h\in\mathcal N\), the family
\[
h(t)=\exp(tL)h\exp(-tL)
\tag{6}
\]
is polynomial in \(t\) as a derivation: check it on a finite set of algebra
generators and use the finite exponential formulas. Every complex-time
value lies in \(\mathcal N\). If its degree is at most \(m\), interpolation
at \(m+1\) distinct scalar times expresses every coefficient as a complex
linear combination of those values. In particular
\[
[L,h]\in V.
\tag{7}
\]
For every \(g\in\ker L\), the replica \(gL\) is again an LND, so the
same reasoning gives \([gL,h]\in V\).

Suppose for a contradiction that \(L\notin V\), and fix any nonzero
\(h\in\mathcal N\). There is \(g\in\ker L\) with \(h(g)\ne0\). Indeed,
otherwise \(h\) kills \(F_L=\operatorname{Frac}(\ker L)\). The local-slice
theorem gives \(F=F_L(r)\), and the space of \(F_L\)-derivations of this
one-variable rational function field is one-dimensional over \(F\).
It follows that \(h\) is a nonzero rational multiple of \(L\), contradicting
\(h\in V\) and \(L\notin V\).

Finally the exact identity
\[
[gL,h]-g[L,h]=-h(g)L
\tag{8}
\]
has its left side in \(V\). Since \(h(g)\ne0\) in the domain, it follows
that \(L\in V\), the required contradiction. The other inclusion in
(5) follows from \(\mathcal N\subseteq\operatorname{LND}(A)\).

The full-group hypothesis cannot be replaced silently by conjugation
under the subgroup generated by \(\mathcal N\) itself. For example the
all-degree family \(\{f(x)\partial_y:f\in\mathbb C[x],f\ne0\}\) on
\(\mathbb A^2\) is closed under its own flows and replicas but has generic
rank one. It is not invariant under the full special automorphism group.
This distinction agrees with the published definition of a saturated
set and its shear example, which uses the self-generated group.[^orbits]

## 3. Application to every nonlinear ambient frame, or just one seed orbit

Every \(\psi\in\operatorname{SAut}(A)\) extends to \(\widetilde\psi\in
\operatorname{Aut}(B)\) by fixing \(s\). Such extensions are actual
polynomial automorphisms of the ambient \(\mathbb C^{[4]}\), with inverses
obtained by reversing the finite flows. They commute with \(E\).

If \(T\) is an actual coordinate partial, then
\(\widetilde\psi T\widetilde\psi^{-1}\) is an actual coordinate partial
in the transformed frame. Its largest adjoint order is unchanged, and
\[
K_{\widetilde\psi T\widetilde\psi^{-1}}
=\widetilde\psi K_T\widetilde\psi^{-1},
\qquad
h_{\widetilde\psi T\widetilde\psi^{-1}}
=\psi h_T\psi^{-1}.
\tag{9}
\]
Thus \(\mathcal H_E\) satisfies the hypothesis of Section 2.

More strongly, choose **any** \(h_0=h_{T_0}\ne0\) and use only
\[
\mathcal O(h_0)=\{\psi h_0\psi^{-1}:\psi\in\operatorname{SAut}(A)\}.
\tag{10}
\]
This set also satisfies that hypothesis and is a subset of
\(\mathcal H_E\). Hence
\[
\operatorname{span}_F\mathcal O(h_0)
=\operatorname{span}_F\mathcal H_E
=\operatorname{span}_F\operatorname{LND}(A).
\tag{11}
\]
In particular the equalities of common kernels are exact, both on the
ring and on the fraction field:
\[
\bigcap_{h\in\mathcal H_E}\ker_Ah
=\bigcap_{h\in\mathcal O(h_0)}\ker_Ah=\operatorname{ML}(A),
\tag{12}
\]
\[
\bigcap_{h\in\mathcal H_E}\ker_Fh
=\bigcap_{h\in\mathcal O(h_0)}\ker_Fh=\operatorname{FML}(A).
\tag{13}
\]
For example, if an element is killed by every member of \(\mathcal H_E\),
then (11) makes every intrinsic LND kill it. No interchange of an
infinite intersection and a localization is used here.

Thus extraction from all frames loses no *generic intrinsic LND
directions*. It can still lose every ambient direction that does not
descend intrinsically. Equation (11) does not identify its common span
with all of \(\operatorname{Der}_{\mathbb C}(F)\).

## 4. Exact necessity of the pass-32 determinant certificate

The ring \(A\) in (1) is a UFD with constant units. For completeness,
factor an element of \(A\) in the UFD \(A[s]\). Since its \(s\)-degree is
zero, every factor has degree zero, so all factors lie in \(A\).

For a UFD there is the inherited reduced-fraction identity
\[
\operatorname{FML}(A)=\operatorname{Frac}(\operatorname{ML}(A)).
\tag{14}
\]
Indeed, write a rational invariant as \(a/b\) with \(a,b\) coprime. For
each intrinsic LND \(D\), the equation \(bD(a)=aD(b)\) gives
\(a\mid D(a)\) and \(b\mid D(b)\). The LND divisibility rule makes both
derivatives zero. The same numerator and denominator work for all
\(D\). The reverse inclusion is immediate. This proof does not apply
to arbitrary nonfactorial domains.

The published orbit theorem identifies trivial FML with an open
\(\operatorname{SAut}(A)\)-orbit, and identifies its tangent space with
the span of the LND directions.[^orbits] Therefore, if
\(\operatorname{ML}(A)=\mathbb C\), the common span in (11) has dimension
three over \(F\). Three members of \(\mathcal O(h_0)\) form a basis.
Their actual ambient coordinate sources \(T_1,T_2,T_3\) satisfy
\[
\det(E,K_{T_1},K_{T_2},K_{T_3})\ne0
\tag{15}
\]
in any fixed ambient coordinates. Conversely (15) forces ML triviality
by the pass-32 gradient argument. Hence
\[
\operatorname{ML}(A)=\mathbb C
\quad\Longleftrightarrow\quad
\text{three actual coordinate LNDs satisfy (15).}
\tag{16}
\]
Even when (16) holds, no pairwise commutation, constant determinant,
intrinsic slice, full flexibility, or affine-space recognition follows
from this argument. The auxiliary conjugating group is not asserted
finite-dimensional or algebraic.

## 5. A finite augmentation step, with its required input explicit

Suppose \(h_1,\ldots,h_r\in\mathcal O(h_0)\) are \(F\)-independent and
\(U\) is their span. Supply an intrinsic LND \(L\notin U\). Fix any
\(h=h_j\); as in Section 2 choose \(g\in\ker L\) with \(h(g)\ne0\).
If \([L,h]\notin U\), take \(J=L\). Otherwise take \(J=gL\): identity
(8) ensures \([gL,h]\notin U\).

The polynomial curve
\[
\exp(tJ)h\exp(-tJ)
\tag{17}
\]
has its first coefficient outside \(U\). Let \(m\) be an actual upper
bound for its degree on finite algebra generators. Not all its values
at \(t=0,1,\ldots,m\) lie in \(U\), by the same interpolation argument.
One of those finitely many values therefore increases the rank.
It remains in \(\mathcal O(h_0)\), and (9) supplies a genuine transformed
ambient coordinate source for it.

If the full intrinsic rank is three, this reaches rank three from one
seed after at most two successful rank increases. This is a bound on
the number of increases, **not** a degree bound, runtime bound, or an
algorithm that finds the needed \(L\) from (1). If no outside LND has
been found, failure of a finite search cannot certify that none exists.

There is also a target-specific form. Given \(f\in A\) and an intrinsic
LND \(L\) with \(L(f)\ne0\), either \(h_0(f)\ne0\) already, or one
conjugation family of the form (17), with \(J=L\) or a replica of \(L\),
has a finite scalar-time value moving \(f\). In the latter case choose
\(g\in\ker L\) with \(h_0(g)\ne0\). If \([L,h_0](f)=0\), then
\[
[gL,h_0](f)=-h_0(g)L(f)\ne0;
\tag{18}
\]
otherwise use \(L\) itself. Interpolation applied to the polynomial
value on \(f\) finishes. Again this transfers an already available
intrinsic direction into an extracted coordinate direction; it does
not manufacture a direction moving a genuine ML invariant.

## 6. What this changes, and what remains unproved

Pass 32 left open whether its cross-frame certificate could fail even
when ML was trivial. Equations (11)-(16) remove that separate gap.
All intrinsic nonlinear flows and their replicas are enough to recover
the full generic intrinsic span from any nonzero seed. Sections 2 and 5
are complete all-degree arguments, not extrapolations from a finite
example.

The principal cancellation-related gap is now precisely to rule out
\(\operatorname{ML}(A)\ne\mathbb C\) under (1), or independently produce
an intrinsic LND outside every current proper generic span. The
published cylinder comparison still has only the inclusion
\(\operatorname{ML}^*(A[s])\subseteq\operatorname{ML}(A)\), not its
reverse.[^comparison] None of the conjugation arguments reverses it.

In particular, ambient coordinate translations moving a proposed
invariant cannot replace the intrinsic input \(L\) in Section 5:
their flows need not commute with \(E\), so (9) is not available.
Treating their conjugates as though their intrinsic top were transported
by (9) would assume the missing descent. The prior one-frame controls
are not rerun here, and no nonpolynomial-cylinder example is being used
as a counterexample to the full hypothesis (1).

## 7. Source and verification scope

The replica-conjugation proof (5)-(8), its one-seed application, and the
finite augmentation are explicitly reconstructed here. They use
standard LND and saturation mechanisms, not a claim of unrecognized
priority. The comparison is statement-level: the sources below do not
automatically establish ML triviality under (1). No conclusion about
the absence of other literature is drawn.

In particular, the open-orbit one-seed spanning conclusion already
follows from AFKKZ Theorem 4.2 and Remark 2.7(1): isotropy on an open
SAut orbit acts as the full special linear group on its tangent space,
so conjugates of a field nonzero at a point span there. The argument
above reconstructs a fraction-field version without an open-orbit
assumption and records a conditional finite augmentation, not a new
flexibility theorem. See the [bounded primary comparison](literature-scope-pass33.md).

An independent agent reconstructed the key span argument, its
conjugation/interpolation step, and the nonzero-seed qualification.
The proofs quantify over arbitrary intrinsic LNDs and their full
polynomial flows. No finite sample suite is presented as verification
of those universal quantifiers.

### Independent finite controls

The standalone [cross_frame_saturation_checks_pass33.py](cross_frame_saturation_checks_pass33.py)
imports only unittest and SymPy. Its six methods check the replica
bracket identity, finite polynomial conjugation and Vandermonde
reconstruction, two replica-shear rank increases from \(\partial_c\),
the actual transformed coordinate inverses, the distinction between
self-generated and full-group saturation, and both target-recovery
bracket choices. The rank-three example has determinant \(6c^3\), so
the controls explicitly do not assert a unit determinant or pairwise
commutation. The initial targeted run passed all six methods in
0.067 seconds. These exact controls do not prove the all-LND orbit
quantifier, invariant-field equality, or the cited orbit theorem.

```
/opt/anaconda3/bin/python research/cross_frame_saturation_checks_pass33.py
```

[^filtration]: Bachar Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2, PDF p. 4, credits the associated-graded LND theorem to Daigle. Proposition 3.4 and its complete proof, PDF p. 7, use the divisibility step for one-variable cylinders. Both statements were directly reread. Their use here is inherited from the earlier intrinsic-action notes.

[^orbits]: Arzhantsev, Flenner, Kaliman, Kutzschebauch and Zaidenberg, [*Flexible Varieties and Automorphism Groups*](https://arxiv.org/pdf/1011.5375), version 2. Proposition 1.8 and proof identify orbit tangent spans; Theorem 1.13, Corollary 1.14, and Proposition 5.1 give the rational-invariant/open-orbit equivalence. Definition 2.1 and the following shear example distinguish self-generated saturation from full-group invariance. These passages were directly read. They supply the inherited orbit and replica framework, not the unproved implication from (1) to an open intrinsic orbit.

[^comparison]: Dasgupta and Gupta, [*An Algebraic Characterization of the Affine Three Space*](https://arxiv.org/pdf/1709.00169), version 2, Lemma 3.1 and full proof, PDF p. 5, directly reread. Its one-sided cylinder comparison remains exactly as used in pass 32. An ambient slice is not an intrinsic slice of the coefficient ring.
