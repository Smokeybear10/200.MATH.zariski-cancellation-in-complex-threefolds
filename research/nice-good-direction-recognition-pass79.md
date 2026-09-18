# Recognition with one supplied good direction

The nonlinear supplied-good branch now has a written recognition
argument. The original coordinate partial preserves the divisor of
the coefficient of Z in the relative quadratic equation. Its local
nilpotence makes that coefficient invariant. The invariant-omission
theorem then makes it a nonzero constant, so the relation eliminates
Z globally.

This is a restricted theorem, conditional on the actual nice frame
and supplied constant good direction. It does not prove that either
exists for an arbitrary polynomial cylinder action.

## 1. The restricted theorem

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=\sum_iP_i\partial_{x_i}\in\operatorname{LND}(B),
\qquad E(s_*)=1,\qquad E^2(x_i)=0\quad(1\le i\le4).
\tag{1}
\]
Assume there is a nonzero constant vector c for which the actual
constant derivative T_c satisfies
\[
[E,[T_c,E]]=0.
\tag{2}
\]
Then, using the retained published inputs and the written reductions
specified below,
\[
\boxed{\ker E\simeq\mathbb C^{[3]}.}
\tag{3}
\]
Here “nice” is exactly the last condition in (1). “Good” is exactly
(2). Neither means that E has already been made a coordinate partial.
No restriction is imposed on the ordinary spatial degrees of the P_i.

The proof below closes the only new case. The
[sliced nice-rank argument74](nice-slice-adjoint-rank-pass74.md)
gives J cubed zero for J=Jac P. If J squared is zero, the earlier
all-double-adjoint recognition applies. Otherwise the velocity-cone
reduction76 applies. If its defining homogeneous polynomial is
linear, it supplies an actual invariant ambient linear coordinate,
and the retained slice/invariant-coordinate theorem recognizes the
kernel. These previously recognized cases are separate from the
nonlinear proof below.

## 2. Inputs in the remaining nonlinear branch

Make a constant linear change so that the given nonzero direction
is T=partial_w. Write x_tr=(x1,x2,x3). All original niceness and
slice identities survive this actual coordinate change.

The complete chain
[omission76](nice-good-direction-invariant-omission-pass76.md),
[binary descent77](nice-binary-parameter-descent-pass77.md),
[unit-parameter exclusion78](binary-normal-syzygy-exclusion-pass78.md),
[relative generation78](binary-relative-hypersurface-pass78.md), and
[quadratic generation79](relative-quadratic-generation-pass79.md)
gives the following actual presentation:
\[
\begin{gathered}
A=\ker E,\qquad B=A[\sigma],\qquad E\sigma=1,\\
Q=[T,E],\quad 0\ne\delta=Q|_A,\quad
S=\ker\delta=\mathbb C[u,v],\\
A\simeq S[Y,Z]/(F),\qquad
F=aZ+bY^2+dY+e,\qquad a,b,d,e\in S,\quad a\ne0.
\end{gathered}
\tag{4}
\]
The letters d,e here are coefficients, not derivations or the binary
degree. Y,Z are the actual generators in A as well as their formal
presentation symbols. The determinant-one reconstruction over S is
\[
x_{\rm tr}=H\sigma+VY+Wc_0,\qquad
w=Z+P_4\sigma,\qquad c_0,P_4\in S,
\quad[H,V,W]\in\operatorname{SL}_3(S).
\tag{5}
\]
Most importantly, the actual-generation determinant is a complex
unit kappa. Its exact cofactors, with the orientations fixed in
quadratic generation79, are
\[
Tu=-\kappa^{-1}a\ell_v,
\qquad Tv=\kappa^{-1}a\ell_u,
\qquad\ell_u,\ell_v\in S[Y],\quad\kappa\in\mathbb C^*.
\tag{6}
\]
These are regular equalities in the original polynomial ring B.
They do not describe a merely rational field or a formal derivation
on an unrelated hypersurface.

The same nonlinear supplied-good hypotheses give
\[
\ker E\cap\ker T=\mathbb C.
\tag{7}
\]
This is exactly omission76 equation (6). Its source is de Bondt's
Theorem 5.1(iv), applied to the actual five-variable homogenization,
with component gcd one, the required fifth-output independence,
and exactly one linear invariant, namely the homogenizing variable.
The polynomial a in (4) is within its scope; no assertion about
rational constants is required.[^omission]

## 3. The coefficient cannot have a divisor

Because a is a polynomial in u,v, ordinary differentiation and (6)
give an exact self-divisibility identity in B:
\[
T(a)=a_uTu+a_vTv
=\frac{a}{\kappa}(-a_u\ell_v+a_v\ell_u)\in aB.
\tag{8}
\]
The actual T is the original coordinate derivative partial_w.
If its value on the nonzero polynomial a were nonzero, that value
would have w-degree one less than a. A nonzero multiple of a has
w-degree at least that of a. Hence (8) forces T(a)=0.
Equivalently this is the self-divisibility property for an LND.

Also E(a)=0 because a belongs to S, a subring of A. Equation (7)
therefore applies and yields
\[
\boxed{a\in\mathbb C^*.}
\tag{9}
\]
This is not a conclusion from gcd one, a generic fiber, or
smoothness of the total space. Both the original coordinate LND
in (8) and the invariant-omission statement in (7) are essential
to this argument.

## 4. Global elimination and the primitive slice

The nonzero constant in (9) gives the actual polynomial equality
\[
Z=-a^{-1}(bY^2+dY+e),\qquad
\boxed{A=S[Y]=\mathbb C[u,v,Y].}
\tag{10}
\]
The quotient by the displayed linear polynomial is isomorphic to
S[Y], not just birational to it. Alternatively, generation follows
from elimination and algebraic independence follows from
trdeg_C A=3. This proves (3) in the remaining case.

Together with (5), equation (10) gives actual polynomial coordinate
generation B=C[u,v,Y,sigma]. The originally supplied slice s_* can
differ from sigma by an element of A; its existence has not been
replaced by a localized slice.

There is also a concrete conclusion for the primitive intrinsic
action. In the normalization of the
[relative Jacobian theorem79](relative-jacobian-primitive-pass79.md),
\[
D_F(Y)=a,\qquad D_F(Z)=-(2bY+d),\qquad
D_F(Y/a)=1.
\tag{11}
\]
Thus it has a global slice and no fixed points. A primitive D
is a nonzero constant multiple of D_F, so rescaling the slice
gives one for D too. The unnormalized delta may still have a
nonconstant invariant replica factor. No slice for that replica,
or a slice common to every original field, is inferred.

## 5. What has and has not been closed

Within the supplied-good nice branch, primitive recognition is no
longer an open proof obligation in this packet. The two-generator
and quadratic reductions alone did not settle it; the original
partial's divisibility identity supplies the final step.

The original complex-threefold cancellation objective remains
unresolved. Given only A[s]=C^[4], a nice frame satisfying (1)
has not been constructed. Even among supplied nice frames,
the constant good-direction space may be zero; its nonemptiness
has not been proved. Those are separate remaining gates.

The retained Weitzenbock hypersurface uZ-Y squared-v has a
nonconstant coefficient of Z, and known exotic quadratic
modifications provide further controls on weaker assumptions.
None has been supplied with every hypothesis (4)--(7).
The present proof does not classify all quadratic modifications
or show that every intrinsic quotient is a polynomial line bundle.

The derivation is a written working theorem with independent AI
reconstructions. A finite symbolic checker can verify displayed
matrix identities and retained examples, not the entire theorem
or its published prerequisites. No human expert review, formal
proof-assistant verification, historical novelty certification,
external contact or publication is claimed.

[^omission]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), Theorem 5.1(iv), printed pp. 22--25, [published article](https://doi.org/10.1007/s13366-017-0358-2). The complete selected theorem statement and proof, including both cases of (iv), were freshly read in the retained primary text for this endpoint. The exact homogenization hypotheses and descent are written in omission76. This is not a fresh reconstruction of every result cited by that paper.
