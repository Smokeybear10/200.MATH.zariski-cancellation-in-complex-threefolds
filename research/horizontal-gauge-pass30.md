# Horizontal gauges and the obstruction to preserving the canonical action

Every horizontal LND fixing only \(x\) in the explicit canonical
polynomial model admits a constructive polynomial gauge to the
horizontal coordinate partial. This uses the already established
ambient coordinate \(\lambda\), not a new cancellation theorem.

However, that gauge cannot in general preserve even the scalar line
of the canonical vertical action. A genuine sliced horizontal action
cannot be brought into the pass-29 auxiliary-plane-fixing family by
any gauge fixing \(x,\lambda\) and normalizing the vertical action.
The obstruction is visible on the actual reduced fixed locus.

Thus a gauge of the horizontal action alone is not a valid reduction
of a classification for a fixed pair of actions. Both the positive
algorithm and this negative boundary are exact.

## 1. Fixed model and the two different gauge problems

Use the unchanged canonical input and modification:
\[
R=\mathbb C[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad r=y,\quad p=x^2,\quad d=x,
\]
\[
B=R[\lambda,w]/((1+\lambda x)w-y)
 =\mathbb C[x,\lambda,w,z],
\qquad v=1+\lambda x,
\]
\[
\Delta x=\Delta\lambda=0,\qquad
\Delta w=x^2,\qquad \Delta z=2v^2w.
\tag{1}
\]
The full nonunit plinth and primitivity were verified in
[pass 28](canonical-top-pass28.md). Put
\[
S=\mathbb C[x],\qquad F=2xz-w^2.
\]
The enlarged set of horizontals is
\[
\mathcal H_x=\{\delta\in\operatorname{LND}(B):
                       \delta x=0,\ \delta\lambda=1\}.
\tag{2}
\]

An unrestricted relative gauge is an element of
\(\operatorname{Aut}_{S[\lambda]}B\). It fixes the actual
parameter \(\lambda\), but can change \(\Delta\).
In contrast, the canonical-pair-preserving gauge group considered
here is
\[
N_\Delta=\{\phi\in\operatorname{Aut}_{S[\lambda]}B:
       \phi^{-1}\Delta\phi=\gamma\Delta
       \text{ for some }\gamma\in\mathbb C^*\}.
\tag{3}
\]
The scalar rescaling in (3) is allowed. The negative result is not
an artifact of requiring strict commutation.

## 2. A complete constructive gauge for the horizontal action alone

**Proposition.** For every \(\delta\in\mathcal H_x\), there is
a unique \(\phi\in\operatorname{Aut}_{S[\lambda]}B\) satisfying
\[
\phi\equiv\operatorname{id}\pmod\lambda,
\qquad \delta\phi=\phi\partial_\lambda.
\tag{4}
\]
It is obtained from finite exact differentiation, with no assumption
about polynomiality of an unknown quotient.

Define the slice projection
\[
\rho(f)=\sum_{j\ge0}\frac{(-\lambda)^j}{j!}\delta^j(f).
\tag{5}
\]
Each sum is finite by local nilpotence. The map \(\rho\) is a
ring homomorphism: first form the polynomial exponential
\(\sum T^j\delta^j/j!\) with a separate indeterminate \(T\),
then substitute \(T=-\lambda\). The Leibniz rule proves
multiplicativity of the exponential. Differentiating (5) gives
a finite telescoping sum, so \(\delta\rho(f)=0\).
Also \(\rho\lambda=0\), \(\rho x=x\), and
\(\rho f\equiv f\pmod\lambda\).

Set
\[
U=\rho(w),\qquad V=\rho(z),\qquad
\phi(x)=x,\quad\phi(\lambda)=\lambda,
\quad\phi(w)=U,\quad\phi(z)=V.
\tag{6}
\]
Since the original ring is exactly \(S[\lambda,w,z]\),
multiplicativity gives the explicit substitution identity
\[
\rho(f)=f(0,x,U,V).
\tag{7}
\]
Every invariant is fixed by \(\rho\); hence
\(\ker\delta=S[U,V]\). Algebraic independence over \(S\)
follows by reducing a putative relation modulo \(\lambda\),
where \(U,V\) become the independent original variables \(w,z\).

There is a complete polynomial reconstruction:
\[
f=\sum_{j\ge0}\frac{\lambda^j}{j!}\rho(\delta^j f).
\tag{8}
\]
Expanding its right side as a double finite sum, the coefficient
of \(\lambda^k\delta^k f\) is
\(\sum_{j=0}^k(-1)^{k-j}/(j!(k-j)!)\), equal to zero for
\(k>0\) and one for \(k=0\). Therefore the actual inverse
coordinate formulas are
\[
\begin{split}
w&=\sum_{j\ge0}\frac{\lambda^j}{j!}
          (\delta^j w)(0,x,U,V),\\
z&=\sum_{j\ge0}\frac{\lambda^j}{j!}
          (\delta^j z)(0,x,U,V).
\end{split}
\tag{9}
\]
Together with \(x,\lambda\), the variables \(U,V\) thus form
a polynomial coordinate system. The expressions on the right of
(9), with \(U,V\) replaced by the formal \(w,z\), are the
inverse images \(\phi^{-1}(w),\phi^{-1}(z)\).
Equation (4) follows from \(\delta U=\delta V=0\).

For uniqueness, an invariant is determined by its residue modulo
\(\lambda\): by (7), an invariant with zero residue is zero.
Any normalized gauge in (4) must send \(w,z\) to invariant
lifts of precisely those residues, so it must be (6).

This is an algorithm on the stipulated input. Given verified
coordinatewise nilpotence bounds for \(\delta\), compute finitely
many derivatives of \(w,z\), then use (5) and (9). Without given
bounds, the same loops terminate when \(\delta\) is already
known to be an LND. This is not an algorithm deciding whether an
arbitrary polynomial derivation is locally nilpotent, nor an
efficiency or universal degree-bound claim.

The crucial premise is the established presentation
\(B=S[\lambda,w,z]\). If instead only \(B=A[\lambda]\simeq
\mathbb C^{[4]}\) is known, with no ambient coordinate system
containing \(\lambda\), equation (7) cannot be asserted with
three independent remaining ambient variables. Identifying
\(B/(\lambda)=A\) with a polynomial ring would then be the
unresolved cancellation step. The fact that \(S=\mathbb C[x]\)
is Dedekind is not used to hide this distinction.

## 3. What a canonical normalizer must do on the exceptional divisor

Let \(\phi\in N_\Delta\). Because it fixes \(x\), it induces
an automorphism \(\bar\phi\) of
\[
\bar B=B/(x)=\mathbb C[\lambda,w,z],\qquad
\bar\Delta=2w\partial_z.
\tag{10}
\]
The normalization identity descends. In particular \(\bar\phi\)
preserves the exact kernel \(\mathbb C[\lambda,w]\) of
\(\bar\Delta\). Its inverse does too. Since \(\lambda\)
is fixed, a polynomial automorphism of this one-variable algebra
over \(\mathbb C[\lambda]\) has the form
\[
\bar\phi(w)=a w+b(\lambda),\qquad a\in\mathbb C^*.
\tag{11}
\]
Indeed polynomial degrees force degree one, and its leading
coefficient must be a unit of \(\mathbb C[\lambda]\), hence
a nonzero constant.

The identity \(\Delta\phi=\gamma\phi\Delta\), evaluated
on \(z\) and reduced modulo \(x\), reads
\[
2w\partial_z\bar\phi(z)=2\gamma(aw+b(\lambda)).
\tag{12}
\]
Its left side is divisible by \(w\), so \(b=0\). It follows
further that
\[
\bar\phi(w)=aw,\qquad
\bar\phi(z)=\gamma a z+P(\lambda,w)
\tag{13}
\]
for some polynomial \(P\). This is a necessary residue form,
not a claim that every such residue map lifts to a global
normalizer. No restriction of \(P\) to a constant is assumed.

For any \(\delta\in\mathcal H_x\), put
\(\delta'=\phi^{-1}\delta\phi\). Reduction modulo \(x\)
and (13) give
\[
\overline{\delta'(w)}
 =a\bar\phi^{-1}(\overline{\delta(w)}).
\tag{14}
\]
Consequently the exact property
\[
\boxed{\delta(w)\in xB}
\tag{15}
\]
is invariant under all canonical normalizing gauges (3).

## 4. A decisive obstruction to the proposed auxiliary-plane reduction

Every \(\delta'\in\mathcal H_x\) fixing \(F\) satisfies
\[
0=\delta'F=2x\delta'z-2w\delta'w.
\]
Modulo \(x\), the polynomial domain \(\bar B\) has \(w\)
as a nonzero divisor. Therefore such a horizontal must satisfy
(15). This is also explicit in the all-parameter
[pass-29 classification](horizontal-selection-pass29.md).

Now take the actual sliced coordinate LND
\[
\delta_1=\partial_\lambda+\partial_w.
\tag{16}
\]
It fixes \(x\), has slice \(\lambda\), and belongs to
\(\mathcal H_x\). But \(\delta_1w=1\notin xB\).
Thus no \(\phi\in N_\Delta\) can make
\(\phi^{-1}\delta_1\phi\) fix \(F\). Explicitly (14) gives
\[
\overline{\delta'(w)}=a,\qquad
\overline{\delta'F}=-2aw\ne0.
\tag{17}
\]
This is an obstruction to every polynomial normalizing gauge,
not a failure of a bounded search or of a selected shear.

The unrestricted normalized gauge from Section 2 nevertheless
exists and is elementary:
\[
\phi(w)=w-\lambda,\qquad\phi(z)=z.
\]
It sends \(\delta_1\) to \(\partial_\lambda\), which fixes
\(F\). But it transforms the vertical action into
\[
(\phi^{-1}\Delta\phi)(w)=x^2,\qquad
(\phi^{-1}\Delta\phi)(z)=2v^2(w+\lambda).
\tag{18}
\]
This is not a constant rescaling of (1): the first coefficient
would force that scalar to be one, and the second then differs.
The pass-29 theorem concerns the fixed action (1), so it cannot
simply be applied to the transformed pair in (18).

## 5. The intrinsic fixed-locus version of the obstruction

There is also a coordinate-free necessary condition applicable to
other normalizer-restricted gauge problems. For a derivation
\(\Theta\) of an affine algebra \(A\), let
\[
J_\Theta=(\Theta(f):f\in A),\qquad
Z_\Theta=V(\sqrt{J_\Theta}).
\]
If \(\phi^{-1}\Theta\phi\) is a nonzero constant multiple
of \(\Theta\), then \(\phi\) preserves both
\(J_\Theta\) and its radical. Hence tangency to the reduced
fixed locus,
\[
\delta(\sqrt{J_\Theta})\subseteq\sqrt{J_\Theta},
\tag{19}
\]
is unchanged under \(\delta\mapsto\phi^{-1}\delta\phi\).
This follows directly by applying the automorphism to the image
ideal and conjugating the displayed containment.

In the actual canonical model,
\[
J_\Delta=(x^2,2v^2w)=(x^2,w),\qquad
\sqrt{J_\Delta}=(x,w).
\tag{20}
\]
For the nontrivial equality, \(v^2\) is a unit modulo \(x^2\):
\((1-2\lambda x)v^2=1-3\lambda^2x^2-2\lambda^3x^3\).
Every auxiliary-plane-fixing horizontal is tangent to \((x,w)\),
whereas \(\delta_1w=1\) is not. This independently reconstructs
the obstruction in Section 4 using the actual fixed locus.

In a different model, (19) gives an obstruction only if that
fixed locus and the tangency conditions are nontrivial and
established. No assertion is made that every rank-three input
has the needed geometry. The argument does not constrain
arbitrary gauges which transport the vertical action and its
fixed locus as well.

## 6. Verification, attribution, and stopping boundary

The finite slice projection and reconstruction are the ordinary
characteristic-zero slice identities, proved above rather than
treated as a new relative-plane theorem. They build on the actual
presentation from [pass 28](canonical-top-pass28.md), while
the target family is exactly [pass 29](horizontal-selection-pass29.md).
The normalizer obstruction is an elementary fixed-locus and
polynomial-divisibility deduction. No new external classification
theorem is invoked and no novelty claim is made.

The standalone checker uses only unittest and SymPy. It verifies
full gauges and polynomial inverses for actual horizontal LNDs,
the transformed vertical action, nontrivial exact normalizing
gauges, their residue constraints, and the fixed-ideal identity.
The universal normalizer argument is the written proof, not
an extrapolation from those finite controls.

~~~sh
/opt/anaconda3/bin/python research/horizontal_gauge_checks_pass30.py
~~~

All eight methods passed in 0.409 seconds in the final recorded run.
The first checker run compared an expanded polynomial with an equal
factored expression structurally; expanding the expected expression
fixed that test assertion without changing any mathematical formula.

A second agent independently reconstructed the normalized gauge,
the full inverse formula, and the residue-normalizer obstruction
without finding a correction.

The remaining unknown problem is not to gauge an already supplied
horizontal action in an already established parameter-preserving
polynomial frame. It is to obtain the necessary geometry and a
usable horizontal action for the unknown cylinder, and to control
what happens to the vertical action under any proposed reduction.
No universal selection algorithm, cancellation solution, expert
review, or proof-assistant verification is asserted. No old file
or metadata is changed.
