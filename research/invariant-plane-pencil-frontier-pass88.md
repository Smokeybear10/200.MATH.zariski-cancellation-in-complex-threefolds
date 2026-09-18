# Invariant-plane generators and the remaining descent obstruction

The restricted constant-acceleration problem now has an actual
polynomial invariant plane, a universal identity for its relative
generators, and a global bound on the denominator of a slice
difference. An explicit polynomial-ring example shows why these
algebraic identities alone do not imply descent. The original
coordinate hypothesis remains essential.

The full working target is still the unconfirmed interpretation
of Luo's email: a complex threefold ring A whose polynomial
cylinder is C to the fourth should itself be C to the third.
The intended field and dimension have not been confirmed. The
work below does not prove that full statement, does not cover
every sliced action, and has no human expert or formal review.
Historical novelty has not been established.

## 1. The precise restricted setting

Assume an actual polynomial coordinate system and an actual
globally sliced locally nilpotent derivation E satisfy
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,
\qquad Ex_i=b_i\in A,\qquad Ez=qu,\qquad Eu=1,
\qquad q\in\mathbb C^*.
\tag{1}
\]
Thus the first three original coordinates have E-degree at most
one, and the last has nonzero constant acceleration. There is no
proof that an arbitrary sliced action admits this frame. That
coordinate-reduction obligation is separate from recognizing A
under (1).

The [preceding frame proof](constant-acceleration-three-good-frame-pass87.md)
establishes, for P=(b_1,b_2,b_3,qu) transposed and its original
Jacobian J, the identities J to the fourth=0 and JP=q e_4.
Every actual partial has adjoint column (-1) to the j times
j factorial times J to the j applied to its constant column.
An actual example has rank J three, so the nice-action rank cap
cannot be used here.

Choose a nonzero column in the highest nonzero J-power. Its
corresponding highest adjoint W is an LND, commutes with E,
and kills every component of P. In particular Wu=0, Wb_i=0,
and W restricts nontrivially to A. This is proved by actual
Laurent conjugation, invariant scaling and specialization, not
by treating a formal vector field as an action.

## 2. The actual invariant plane and relative generators

The [invariant-plane proof](constant-acceleration-invariant-plane-pass88.md)
checks the retained quotient theorem's hypotheses for this W.
Its conclusion is
\[
S=\ker(W|A)\simeq\mathbb C^{[2]},\qquad
S\longrightarrow A\longrightarrow B\text{ faithfully flat},
\qquad b_i\in S,\qquad (b_1,b_2,b_3)S=S.
\tag{2}
\]
The unit-row argument is elementary once the same S is fixed.
A simultaneous zero of the b_i would give an E-orbit whose
three good coordinates are constant and whose last coordinate
is quadratic. Two distinct orbit parameters would then have
identical original coordinates but different u-values. This
contradicts Eu=1. Faithful-flat ideal contraction puts the unit
ideal in S itself.

Quillen--Suslin permits a completion M in GL_3(S) with Mb=e_1.
Applying this matrix to the three original good coordinates
gives actual elements sigma,A_1,A_2. An inverse matrix gives an
algebra-generation equality, not an ambient automorphism.
Slice evaluation then gives
\[
E\sigma=1,\qquad R=S[A_1,A_2],\qquad A=R[c],\qquad
h=u-\sigma,\qquad
c=z-qu\sigma+\frac q2\sigma^2.
\tag{3}
\]
No independence of A_1,A_2,c over S is asserted. The distinction
between a free-module basis and polynomial coordinates is one
of the main safeguards in this reduction.

The quotient and module inputs retain their specific source
gates. Kaliman--Saveliev is used on the actual smooth,
contractible threefold, with the affine-three-space domination
hypothesis verified. Quillen--Suslin is used only over the actual
polynomial plane S. Neither source makes R to A faithfully flat.[^plane]

## 3. A universal polynomial pencil

The algebra equality B=R[sigma,z], together with (3), yields
an identity over an independent polynomial parameter tau:
\[
A[\tau]=R[\tau,c+\tau h].
\tag{4}
\]
The [pencil proof](universal-generator-pencil-pass88.md) gives
h in Frac(R). In the algebraic-c case, distinct conjugate values
of h would allow a parameter value at which two conjugates of
c+tau h collide, contradicting generation of the entire finite
separable algebra. In the transcendental-c case, polynomial
degree and specialization force h to have degree zero in c.

The latter case closes a genuine branch of the actual problem.
If c is transcendental over Frac(R), then R and S both have
transcendence degree two. Every element of R is algebraic over
Frac(S), hence is killed by W in characteristic zero. Therefore
R=S and A=S[c] is a polynomial three-ring.

There is also a tensor constraint. Write delta(c) and delta(h)
for left-minus-right differences in D=A tensor_R A. Since A=R[c],
delta(h)=g delta(c). A polynomial inverse to (4) shows that
1+tau g is proved to be a unit after passing to D/Ann(delta(c)).
Its nonconstant coefficient is nilpotent, which proves that
delta(h) is nilpotent in D. Cancellation in D itself would be
invalid. The [source gate](pencil-descent-source-gate-pass88.md)
identifies this as a relative weak-normalization condition and
keeps the missing integrality and descent hypotheses explicit.

## 4. Original volume controls a specific denominator

Fix polynomial coordinates s_1,s_2 on S. Center the original
good coordinates by a=x-bu and put
\[
L=b_{s_1}\times b_{s_2},\qquad
\Omega=L\cdot b,\qquad
\kappa=L\cdot a\in S,\qquad
\Omega h=(L\cdot v_2)A_1+(L\cdot v_3)A_2-\kappa\in R,
\tag{5}
\]
where [b,v_2,v_3]=M inverse. These are global identities in the
original rings. The [volume proof](constant-acceleration-volume-descent-pass88.md)
extracts the cubic u coefficient of the actual preserved original
coordinate volume. Contracting the resulting differential form
with W puts L dot a in its original kernel S. No local-slice
denominator remains.

Consequently h belongs to R localized at Omega whenever Omega
is nonzero. If Omega is a nonzero constant, h belongs to R.
Neither membership asserts coordinate recognition or completes
the generation problem for A.

In the remaining algebraic-c case, the
[generic-degree criterion](constant-acceleration-generic-degree-pass88.md)
also proves
\[
\Omega\ne0\quad\Longrightarrow\quad
\operatorname{Frac}(R)=\operatorname{Frac}(A).
\tag{6}
\]
Over Frac(S), an intrinsic local slice makes A a one-variable
polynomial ring. The precisely stated polynomial-factorization
theorem of de Bondt would turn a proper intermediate field into
a polynomial map of degree at least two. At a critical point of
that map, all centered good-coordinate derivatives vanish.
The original localized coordinate Jacobian is a unit; its
quadratic u coefficient then forces Omega=0, a contradiction.[^curve]

When the derivative of b has rank two and Omega=0, the
[conical-branch proof](constant-acceleration-conical-good-direction-pass88.md)
instead puts P in the image of J, so J squared e_4=0. Thus the
original z-partial has vanishing second E-adjoint. It also obtains
a polynomial normal relation N dot x in S. If a suitable normal
row is unimodular, its conditional conclusion is two relative
generators A=S[Y,c]. That extra normal-row hypothesis is not
discharged in this packet.

Rank-zero speeds give an actual coordinate slice immediately.
Rank-one speeds also give the good z-partial by nilpotent matrix
rank, but no unconditional recognition of that whole case is
asserted here. The older recognition theorem for four nice
coordinates does not apply to Ez=qu; the two-output theorem
requires an actual coordinate plane, not merely the S-plane.

## 5. The strongest algebra-only control

The [normal-ring control](normal-generator-pencil-coordinate-boundary-pass88.md)
takes
\[
S=\mathbb C[a,t],\quad R=S[a^2c],\quad A=S[c],\quad h=ac,\qquad
c=(1-\tau a)(c+\tau h)+\tau^2(a^2c).
\tag{7}
\]
Both R and A are normal polynomial three-rings with constant
units, S to A is polynomial and faithfully flat, and (4) holds.
Nevertheless h is not integral over R. With b=a squared times c,
it is the rational function b/a in Frac(R)=C(a,t,b), and it has
a pole at a=0.

There is even an actual sliced cylinder with u=sigma+ac and
z=c+2a sigma c+sigma squared, satisfying Ez=2u and B=R[sigma,z].
But z is not an ambient coordinate: its zero fiber has the
nonconstant unit 1+2a sigma. Its explicit inverse is
1-2a sigma-4a squared c. The original-coordinate hypothesis
therefore excludes this example for a concrete reason.

Two simpler controls separate other invalid inferences. The cusp
has a nonzero square-zero tensor difference. The
[Laurent example](nonintegral-generator-pencil-control-pass88.md)
has exact tensor agreement but nonintegrality and nonfaithful
localization. These examples refute proposed proof steps, not
the cancellation conjecture.

## 6. Verification and next proof obligation

The [targeted capture](verification-pass88-working.json) passes
four standalone exact methods: cusp, Laurent and normal-ring
pencils, plus the formal coordinate-volume coefficients. The
normal example deliberately fails the coordinate hypothesis.
The checks are not universal action or recognition proofs.
The written results have separate AI reconstructions, whose
scope is recorded in the [proof audit](proof-audits-pass88-working.md).
No full regression or exhaustive action search ran in this pass.

~~~sh
/opt/anaconda3/bin/python research/run_targeted_pass88.py
~~~

The immediate next task is to control the zero locus Omega=0,
including the identically-zero conical case, or prove a stronger
actual-coordinate consequence. The
conical normal row is a specific bounded candidate. Even a
successful local or conical reduction must still be connected
to global polynomial recognition, and the original arbitrary
coordinate-reduction problem remains outside (1).

The [checkpoint](checkpoint-pass88-working.json) records exact
artifacts and outstanding obligations. This is a completed bounded
research packet, not completion of the persistent goal. No
publication, expert outreach or submission has occurred.

## Sources

[^plane]: S. Kaliman and N. Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Lemma 2.1 and Corollary 2.8; the exact additive-action application is set out in the linked invariant-plane proof. For module freeness, D. Quillen, [*Projective modules over polynomial rings*](https://doi.org/10.1007/BF01390008), 1976, with the accessible statement in W. Dicks, [*Seminar on Quillen's proof of the Quillen--Suslin theorem*](https://arxiv.org/pdf/2112.02272), Theorem 6. Source-reading limits are in the proof audit.

[^curve]: M. de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 and Lemma 3.3, printed pages 20--21. The arbitrary-field statement, rather than an assumed algebraically closed coefficient field, is used over Frac(S).
