# Recognition with constant coupling and a transversely affine first potential

Working synthesis, with the recognition dependencies stated below:
under EVERY actual hypothesis of264,
\[
\boxed{k_s=m\in\mathbb C^*,\quad n_{ss}=0
\quad\Longrightarrow\quad n_{ts}=0,\quad n_s\in\mathbb C,
\quad A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
There is no added condition on k_ttt, n_ttt or ell. The new exclusion
is that the first-potential slope cannot vary in t when it is already
constant in s. The recognition endpoint is the retained theorem436.
Neither the constant coupling nor the condition n_ss=0 is established
for an arbitrary chart. No theorem here puts an arbitrary cancellation
candidate in this chart.

## 1. Actual input and the normalized moving-slope question

Retain the complete original-ring input of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\quad\hbox{is the ENTIRE weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\qquad Nv=1,\\
O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
All actual localization, genuine-potential and original-slice
hypotheses of264 remain imposed, not just the displayed consequences.
The original slice satisfies X=a0*u+x0, with x0 in A. No normalization
u=X/a0 is made.

The coefficient partials commute, fix v initially, and have joint
constant field C. Let F=ker_L(partial_s), a finite extension of C(t).
Neither F nor L is assumed rational. The literal rows are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{3}
\]

First assume m=1. Exact subtraction, without coefficient integration,
gives
\[
f=k-s\in F,\qquad \nu=n_s\in F,\qquad n_0=n-\nu s\in F,
\qquad k=s+f,\quad n=\nu s+n_0.
\tag{4}
\]
Indeed n_ss=0 is exactly what is needed for nu_s=0 and (n0)_s=0.
Put b=nu_t. We prove that b cannot be nonzero.

## 2. The complete finite split when b is nonzero

Suppose b is nonzero. The full fourth-potential derivation
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md)
and the polynomial quadric change
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md)
give exact intrinsic polynomials x,p,q with
\[
O=L[v]=L[x,p,q],\qquad \mathcal H=x^2+bpq-d=0,
\qquad p\notin L,
\tag{5}
\]
where d belongs to L. The direct constant-sigma exclusion
[440](principal-paraboloid-arbitrary-longitudinal-moving-first-slope-constant-sigma-exclusion-pass440-working.md)
justifies the last condition before any degree argument.
The intrinsic transformation and its inverse are polynomial over L;
they do not divide by an evaluated nonunit.

The ENTIRE transformed fourth level has support
\[
\begin{aligned}
\Phi={}&\alpha p^2x+bxq+u_1px+\delta p^4+\kappa p^3
 +\epsilon p^2q+\gamma q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00}=0,
\qquad \alpha=f'''/3-2b.
\end{aligned}
\tag{6}
\]
All coefficients are the exact ones obtained from438/441, including
the lower coefficients and moving levels. The evaluated minors of
the formal gradients of Hcal and Phi generate O. In particular
neither generic rank nor the quadric gradient alone replaces this
unit-ideal hypothesis.

The two-equation degree argument in441 bounds the three intrinsic
degrees by eight. The nonresonant classification441 and the separate
[resonant classification442](principal-paraboloid-moving-slope-resonance-degree-profiles-pass442-working.md)
then exhaust the following branches.

- If q is a nonzero constant,441 Section5 excludes it when alpha
  is nonzero;442 Section3 excludes it when alpha=0.
- If q=0,442 Section3 forces alpha=0. The complete zero-remainder
  argument[445](principal-paraboloid-moving-slope-zero-remainder-scalar-exclusion-pass445-working.md)
  excludes this case, including both possible conic levels. It uses
  the actual scalar and original slice, not just the quadric.
- Otherwise p,x,q all have positive degree. Their exhaustive
  degree lists and matching exclusions are in the following table.

Here R denotes resonance alpha=0 and N denotes nonresonance alpha!=0.
An empty entry means that the corresponding classification does not
list that triple, not that an additional exclusion is being inferred.
Triples are always ordered (deg p,deg x,deg q).

| Triple | R: exclusion | N: exclusion |
| --- | --- | --- |
| (1,1,1) | [447](principal-paraboloid-affine-resonant-profile-scalar-exclusion-pass447-working.md) | [453](principal-paraboloid-nonresonant-affine-minor-scalar-exclusion-pass453-working.md) |
| (1,2,3) | [446](principal-paraboloid-affine-sigma-resultant-collision-pass446-working.md) | [446](principal-paraboloid-affine-sigma-resultant-collision-pass446-working.md) |
| (2,2,2) | [448](principal-paraboloid-quadratic-resonant-profile-scalar-exclusion-pass448-working.md) | [451](principal-paraboloid-nonresonant-quadratic-cofactor-exclusion-pass451-working.md) |
| (2,3,4) | [454](principal-paraboloid-cubic-profile-parity-minor-exclusion-pass454-working.md) | [454](principal-paraboloid-cubic-profile-parity-minor-exclusion-pass454-working.md) |
| (2,4,6) | [449](principal-paraboloid-quadratic-sigma-resultant-collision-pass449-working.md) | [449](principal-paraboloid-quadratic-sigma-resultant-collision-pass449-working.md) |
| (3,2,1) | [444](principal-paraboloid-cubic-profiles-quadratic-cofactor-exclusion-pass444-working.md) | |
| (3,3,3) | [444](principal-paraboloid-cubic-profiles-quadratic-cofactor-exclusion-pass444-working.md) | |
| (3,4,5) | [455](principal-paraboloid-tangent-minor-intermediate-profile-exclusions-pass455-working.md) | [455](principal-paraboloid-tangent-minor-intermediate-profile-exclusions-pass455-working.md) |
| (3,5,7) | | [455](principal-paraboloid-tangent-minor-intermediate-profile-exclusions-pass455-working.md) |
| (4,4,4) | [443](principal-paraboloid-equal-quartic-two-quadric-exclusion-pass443-working.md) | |
| (4,5,6) | [455](principal-paraboloid-tangent-minor-intermediate-profile-exclusions-pass455-working.md) | |
| (4,6,8) | [456](principal-paraboloid-quartic-sextic-octic-minor-exclusion-pass456-working.md) | [456](principal-paraboloid-quartic-sextic-octic-minor-exclusion-pass456-working.md) |

There are eleven R entries and eight N entries, exactly the two
necessary lists, not a numerical grid. No constant or zero boundary
is included implicitly in a positive-degree row. In particular the
resonance-only collision proof450 is not used for nonresonant(2,3,4).
The different parity/minor argument454 covers both regimes.

Every alternative is impossible. Thus b=nu_t=0. Since nu_s=0 as
well, joint exact constants imply
\[
\boxed{n_{ts}=0,\qquad n_s=\nu\in\mathbb C.}
\tag{7}
\]

## 3. Why the last exclusions need the genuine gradient condition

The key new device is the primitive tangent argument of454--456.
Whole generation in(5) differentiates to a polynomial combination
of x',p',q' equal to one. The cross product of the two evaluated
gradients is therefore psi*(x',p',q'), with psi in O. The minor-unit
condition forces psi in O*=L*. Here the primes mean intrinsic
v-derivatives, not the coefficient derivatives used in(4).
Consequently the specific evaluated minor satisfies
\[
\begin{aligned}
W&=2x\Phi_q-bp\Phi_x=-\psi p',\qquad \deg_vW=\deg_vp-1,\\
W&=3bx^2+2\epsilon p^2x+4\gamma xq+2c_{11}px+2c_{01}x
       -b\alpha p^3-bu_1p^2-bd.
\end{aligned}
\tag{8}
\]
The first degree is exact. It rules out cancellation patterns that
the two level identities alone would permit. In456, two exact
polynomial shifts in the full fourth relation ultimately force
W=0, contrary to(8).

The formal control
[452](principal-paraboloid-cubic-quartic-quintic-all-parameter-control-pass452-working.md)
explains a different boundary: even the quadric, whole generation,
its single gradient unit and every all-T ring return allow an abstract
(3,4,5) example. It fails the genuine fourth potential. Thus the
new exclusions do not follow from an unproved geometric shortcut.
452 is a strategy obstruction, not an additional case in the table.

## 4. Nonzero complex coupling and the recognition endpoint

For general m in C*, make the ACTUAL complex polynomial scaling
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=mW,
\qquad t_*=t,\quad s_*=ms.
\tag{9}
\]
Its inverse is W=W*/m. The first potential in264(11) shows directly
that k*=k, n*=n, sigma*=sigma and theta*=m*theta, so
\[
(k_*)_{s_*}=1,\quad (n_*)_{s_*s_*}=n_{ss}/m^2=0,
\quad (n_*)_{t_*s_*}=n_{ts}/m.
\tag{10}
\]
This scaling does not require n_s to be complex in advance.

All actual entry licenses persist. The weighted map fixes X,Y,Z
and rescales only W, hence preserves the full initial kernel and
the four exact degrees. The selected partial is unchanged, so N,L,v
are unchanged. Both ring and fraction-field returns are preserved
by w*=m*w and theta*=m*theta. The original scalar determinant acquires
a factor m from the row change and a factor 1/m from the coefficient
parameter change, so it is still -a0^4. The global slice and its
kernel A are unchanged. These are also the initial scaling licenses
of436 Section2; no later translation by a possibly moving slope is
being imported.

Apply(7) to the scaled chart. Equation(10) gives n_ts=0 in the
original chart. Along with n_ss=0, this gives n_s in C. We now meet
exactly the hypotheses of the retained recognition synthesis
[436](principal-paraboloid-constant-first-slopes-recognition-pass436-working.md):
k_s in C* and n_s in C, with no condition on ell_s or either
longitudinal third derivative. It concludes A is isomorphic to C^[3].
This proves(1) with436's stated recognition dependencies.

The recognition endpoint is not supplied by an intrinsic polynomial
change over L.436 retains348/346 for its zero-k_ttt branch,427 for
its zero second-potential slope branch, and430,431,433--435,437 with
the actual polynomial-entry criterion266 for the other branch.
Its actual invariant-coordinate and regularity conditions remain
essential. This synthesis does not recursively recertify those
earlier recognition arguments or their published theorem inputs.

## 5. Evidence and the remaining full-goal gap

Before composing this synthesis, Root read the complete current264
in1fa175,441 in6ce105,442 inf05005,436 inb54df5+26160f,455 inadfb0e,
456 ina5d192 and452 in1363fc. The unchanged held451/453/454 and436
hashes were revalidated in52935e; their earlier full reviews are
recorded in the ledger. The independent coverage audit read441/442
through9b5b6e/ebada4 and checked all boundary branches and table
entries. Its scope is exhaustive coverage, not recursive ancestor
certification.

Fresh root3f932a independently reconstructed the complete minor,
the full R/S/T shifts in456 and the final minor reduction, all with
zero residuals. Fresh rootb1a8e6 checked452's whole inverse,
collision factors and the exact -80 fourth-potential obstruction.
The component notes carry their own written proofs and independent
AI reviews. A separate saved-source review and final held hash of
this synthesis belong in the ledger.

The remaining chart question includes n_ss nonzero when k_ttt is
nonzero. Variable or zero coupling, other initial kernels and time
profiles, and entry from an arbitrary sliced polynomial four-ring
are also not settled. None of(1)--(10) supplies those missing
reductions. The full cancellation conjecture remains unsolved here.

The intended field and dimension of Luo's pasted question remain
unconfirmed. This is private, AI-reviewed working mathematics, not
expert-reviewed or Lean-certified mathematics and not a novelty
claim. All saved checkers remain frozen. No external contact,
submission, publication, paid service or automation occurred.
