# Equal intrinsic degrees one and two are excluded in the supplied chart

Working synthesis of411 and414--416, retaining every actual264
hypothesis, with k=s and n_ss nonzero. No candidate in this
restricted setup can have common intrinsic degree one or two.
Every remaining candidate has degree three through six and belongs
to one of the six nonexceptional profiles below.

This statement is conditional on the full supplied actual chart.
It is not an entry theorem for an arbitrary cancellation candidate,
an original-coordinate construction, or a proof of cancellation.

## 1. Complete scope and necessary frontier

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
not just the displayed subset below:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\qquad
E=\partial_{u_0},\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
0\ne N=[u_0^4]\partial_Z|_{A_0},\qquad
L=\operatorname{Frac}\ker_{A_0}N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Nv_0=1,\qquad a_0=EX\in L^*,\qquad
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\\
K=L(v_0)=\mathbb C(y,z,w),\qquad
J_{t,s,v_0}(X)=-a_0^4\in L^*,\qquad k=s,\quad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The original global slice, actual localization, literal selected
partial, full initial kernel, both returns, genuine potential
levels, their evaluated unit ideals and calibrated scalar remain
imposed. Coefficient partials commute and have joint constants C.

The previously reviewed400/411 give equal intrinsic degrees
\(2\le d=\deg\sigma=\deg\theta\le6\), with \(\deg y\le d\).
For those degrees define
\[
\begin{gathered}
\lambda=\frac{[v_0^d]y}{[v_0^d]\sigma},\qquad
\mu=\frac{[v_0^d]\theta}{[v_0^d]\sigma},\qquad
\nu=n_s,\quad \delta=\lambda-\nu,\quad
\beta=n_{ts}+e\mu,\\
\mathscr D=\partial_t+\mu\partial_s,\qquad
u_1=y-\lambda\sigma,\quad v_1=\theta-\mu\sigma,\\
m=\max(\deg u_1,\deg v_1),\qquad
j=\delta n_t-\ell_t-(\ell_s+\nu^2)\mu,\qquad
R=2\delta u_1+\beta v_1+j,\quad r=\deg R.
\end{gathered}
\tag{2}
\]
In particular lambda is zero if deg(y)<d; no ratio of unequal
leading degrees is intended.

The new necessary frontier is
\[
\boxed{\begin{gathered}
3\le d=\deg\sigma=\deg\theta\le6,\qquad \deg y\le d,\\
\mu\notin\mathbb C+\mathbb C t,\qquad
\mathscr D\lambda=0,\qquad \mathscr D\mu=-4\lambda,\\
\delta\ne0,\qquad \beta^2+2e\delta^2\ne0,\qquad
R\ne0,\qquad 1\le r<m<d,\quad d+r=2m.
\end{gathered}}
\tag{3}
\]
The precise necessary degree list is
\[
(r,m,d)\in
\{(1,2,3),(1,3,5),(2,3,4),(2,4,6),(3,4,5),(4,5,6)\}.
\tag{4}
\]
No entry in this list is asserted to occur.

## 2. Exhaustion of the quadratic cases

Assume d=2. The leading coefficient lambda either belongs to C
or does not.

If lambda is complex, the
[complex-slope exclusion414](principal-paraboloid-equal-quadratic-complex-slope-exclusion-pass414-working.md)
applies. The actual complex polynomial automorphism licensed by384
sets lambda to zero without canceling the theta leader. Actual
all-X polynomial generation then forces an affine lower slope
and offset to vanish. The full scalar and genuine fourth potential
give two incompatible formulas for dot(e). This excludes the
entire complex-lambda quadratic case, including lambda=0.

If lambda is noncomplex and (delta,beta) is not (0,0), the
[nonconstant-slope exclusion416](principal-paraboloid-nonconstant-slope-quadratic-collision-exclusion-pass416-working.md)
applies. The rank result407 supplies an affine intrinsic parameter.
A divided-difference collision forces its lower y slope to vanish,
hence beta=0. The exact coefficient family of413 then forces
delta=0, contradicting the nonexceptional case.

The only other possibility is delta=beta=0. The
[exceptional exclusion415](principal-paraboloid-exceptional-quadratic-leading-direction-exclusion-pass415-working.md)
excludes this branch. It fixes the affine offset by actual all-X
polynomial generation, retains the arbitrary remaining coefficient
function, and uses full scalar coefficients to force an exact
finite family. Its final literal determinant has a nonzero
intrinsic linear term and cannot be a coefficient scalar.

These alternatives exhaust d=2. The already reviewed degree-one
synthesis411 supplies the earlier exclusion, and no degree-one-only
scalar calculation has been applied to higher-degree remainders.
Thus d>=3 under(1).

The collision arguments include coincident roots: then all three
intrinsic derivatives vanish, contradicting polynomial generation.
They do not assume distinct roots or infer an actual coordinate
from a coefficient-field parameter.

## 3. The exceptional direction and zero-delta boundary also disappear

By407, delta=beta=0 at any equal degree at least two already forces
d=2. The preceding exclusion therefore removes that direction
throughout the surviving range.

There is no remaining case delta=0 with beta nonzero. In413,
alpha=Dscript(lambda) is zero at every remaining degree. If delta=0,
lambda=nu, hence beta=Dscript(nu)=alpha=0, the exceptional direction
just excluded. Therefore delta is nonzero.

The nonexceptional conclusions407 now give nonzero curvature,
R nonzero, d+r=2m and r<m<d. Its r=0 alternative forces
(r,m,d)=(0,1,2), also excluded. Removing that one entry from407
gives precisely(4). The slope restriction is400 and the
characteristic equations are413. No new exclusion of a higher
profile follows merely by collecting these facts.

## 4. Verification and limits

The three new component notes414--416 contain full written
arguments and fresh unsaved symbolic reconstructions. Root read
414 through EOF in28d098+cac4b6, and its independent7ffbbd checks
reconstructed the full intercept scalar and genuine-Q coefficients.
Jet independently reviewed the corrected complete414 at hash
b5768cd4bd064d2c21bf4d39298a3e9c88ee4274489dc87cc3ebe3e405c5a42c
in1fcac6, with fresh exact controls a126a4.

Root read415 through EOF in9e7551+079198 and independently rebuilt
its final determinant directly from the original rows in008f4b,
completed on the original process86770 in6cb1a0. The full residual
was zero. An earlier Root check7f3054 omitted the offset
xi*t+A'/2 when restoring sigma from the shifted coefficient d.
That failed check is not evidence for the proof. The saved415
distinguishes d0 and d explicitly; the corrected check retains
both terms. Separate General reconstruction f05044 also matches.

Root's complete416 read is9a98fa; its earlier independent full
Jet review is40e6b1 with final held-source check12140f and exact
controls33d08b. Root reread407 through cc9145+077f6d+7cc2cb and
413 through07d5e0+1b73de when assembling this synthesis.
The final source reviews, metadata and any corrections are
recorded in the research ledger. This synthesis itself requires
a separate complete source audit before canonical acceptance.

No saved checker was executed, imported, compiled or rerun.
This note does not prove n_ss=0, exclude any surviving d>=3
profile, handle general coupling k, exclude other initial kernels,
establish arbitrary-chart entry, or recognize A0 as C^[3].
The professor has not confirmed the intended field and dimension
of the original question. There is no claim of unrestricted
cancellation, novelty, human-expert review or formal certification.

