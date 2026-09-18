# Recognition in the supplied constant-coupling principal chart

Working synthesis, conditional on the retained proof dependencies.
Under EVERY supplied actual hypothesis of264, the normalized
coupling k=s forces n_ss=0. Combined with the earlier recognition
theorem363, this recognizes the original kernel as C^[3]. An
actual complex polynomial normalization extends the conclusion to
k_s in C* and k_ttt=0, without an initial assumption on n.

This is a restricted-chart working theorem. It does not put an
arbitrary cancellation candidate in that chart, normalize general
k, certify the inherited arguments recursively, or solve the
unrestricted cancellation problem. Independent review of this
synthesis and its new components is recorded in the ledger.

## 1. Full scope and statement

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including, but not limited to,
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
J_{t,s,v_0}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The actual global slice and localization, the literal selected
partial, both returns, exact commuting coefficient partials with
joint constants C, genuine potential levels and evaluated unit
ideals are retained. A formal tuple satisfying selected displayed
equations is not a substitute for this entire input.

The literal coordinate expansions are
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{2}
\]
We prove the new exclusion
\[
\boxed{\text{Under every actual hypothesis of264,}\quad
k=s\quad\Longrightarrow\quad n_{ss}=0.}
\tag{3}
\]
With363's retained recognition inputs, it gives
\[
\boxed{\text{Under every actual hypothesis of264,}\quad
k_s\in\mathbb C^*,\quad k_{ttt}=0
\quad\Longrightarrow\quad
n_{ss}=n_{ts}=0,\quad A_0\cong\mathbb C^{[3]}.}
\tag{4}
\]
There is no extra initial condition on the first potential n or
the second potential ell. The scope condition264 is substantial.

## 2. Contradiction setup and the exhaustive six profiles

Assume k=s and e:=n_ss is nonzero. The reviewed
[synthesis417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md)
exhausts the earlier constant, strict-degree, degree-one,
quadratic and exceptional-direction possibilities. Its necessary
frontier is
\[
3\le d=\deg\sigma=\deg\theta\le6,\quad \deg y\le d,
\quad \mu\notin\mathbb C+\mathbb C t,
\quad \mathscr D\lambda=0,\quad \mathscr D\mu=-4\lambda,
\tag{5}
\]
where all degrees are intrinsic over L and
\[
\begin{gathered}
\lambda=[v_0^d]y/[v_0^d]\sigma,\qquad
\mu=[v_0^d]\theta/[v_0^d]\sigma,\qquad
\mathscr D=\partial_t+\mu\partial_s,\\
\nu=n_s,\quad \delta=\lambda-\nu\ne0,\quad
\beta=n_{ts}+e\mu,\quad
\mathcal K=\beta^2+2e\delta^2\ne0,\\
u_1=y-\lambda\sigma,\quad h=\theta-\mu\sigma,\quad
j=\delta n_t-\ell_t-(\ell_s+\nu^2)\mu,\\
R=2\delta u_1+\beta h+j,\quad
r=\deg R,\quad m=\max(\deg u_1,\deg h).
\end{gathered}
\tag{6}
\]
In particular lambda is zero if deg(y)<d. We have
\[
1\le r<m<d,\quad d+r=2m,\qquad
(r,m,d)\in\{(1,2,3),(1,3,5),(2,3,4),
                 (2,4,6),(3,4,5),(4,5,6)\}.
\tag{7}
\]
The list is a necessary exhaustive list under the contrary
assumption, not a list of realized examples.

## 3. Universal coefficient restrictions and four geometric exclusions

The new full-potential argument
[419](principal-paraboloid-higher-degree-curvature-evolution-pass419-working.md)
applies to every profile in(7). It proves
\[
\begin{gathered}
\beta\ne0,\quad
\delta\mathscr D\beta+2\beta^2=0,\quad
\mathscr De+3e\beta/\delta+\beta^3/(2\delta^3)=0,\\
\kappa:=\mathcal K/\beta^2\ne0,\qquad
\boxed{\mathscr D\kappa=-(\beta/\delta)\kappa\ne0.}
\end{gathered}
\tag{8}
\]
The two differential equations come from the uniquely highest
coefficient, then the next pair of tied coefficients, of the
genuine fourth potential. The inequalities in(7), particularly
r>=1, put every lower quadratic term below those comparisons.
The beta=0 case is excluded separately before dividing beta.

The affine formal transport in
[421](principal-paraboloid-equal-degree-geometric-profile-reduction-pass421-working.md)
places the full third level in the form
\[
x^2+\gamma pq-\Delta=0,\quad \gamma\in L^*,\quad
O=L[p,x,q],\quad (\deg p,\deg x,\deg q)=(r,m,d).
\tag{9}
\]
The genuine cubic and both evaluated gradient/minor unit ideals
survive that invertible affine change over L. It is not an
ambient coordinate change over C. The proof separately treats
Delta=0 by polynomial parity and Delta nonzero by the smooth
projective quadric, ruling intersections and genus. It excludes
\[
(2,3,4),\quad(1,3,5),\quad(3,4,5),\quad(4,5,6).
\tag{10}
\]
Only(1,2,3) and(2,4,6) remain. Neither is ruled out by geometry
alone, and no cone is treated as a smooth projective quadric.

## 4. The cubic profile is impossible

For(r,m,d)=(1,2,3),
[420](principal-paraboloid-equal-cubic-collision-curvature-ratio-pass420-working.md)
uses actual all-X polynomial generation and divided differences
to prove
\[
\kappa\in\left\{-1,\ 2+\sqrt3,\ 2-\sqrt3,
                     \frac{-4+3i}{5},\ \frac{-4-3i}{5}\right\}
\subset\mathbb C^*.
\tag{11}
\]
Its elimination includes the vanishing elimination denominator
and coincident pair of intrinsic parameters. A coincident pair
would make all three intrinsic derivatives vanish, which also
contradicts generation of the whole polynomial line.

The needed all-X license is actual: X=a0*u0+bX with a0 in L*
and bX in A0 gives
\[
L[\mathcal B]=L[A_0][u_0]=L[X,v_0].
\tag{12}
\]
Consequently specializing any X value over an algebraic closure
of L retains generation by the three original remaining
coordinates. A rational-field return would not suffice.

Since the exact derivation kills C, equation(11) gives
Dscript(kappa)=0, contradicting(8). This handles both complex
and noncomplex leading lambda. The separate complex-lambda
reduction418 is consistent additional evidence but is not needed
for this implication.

## 5. The sextic profile is impossible

For(r,m,d)=(2,4,6), the exact ideal argument in
[423](principal-paraboloid-equal-sextic-filtered-cubic-exclusion-pass423-working.md)
completes the exclusion. Here is the coefficient obstruction
and the precise geometric input that permits its use.

Write P for the independent formal sigma slot, R for the
independent transformed slot in(6), h for the lower theta slot,
and Acal=Kcal/(4delta^2). The complete third level has top
homogeneous form
\[
H_2=RP+\frac{R^2}{4\delta^2}
       -\frac{\beta Rh}{2\delta^2}+\mathcal A h^2.
\tag{13}
\]
Using both gates in(8), the genuine fourth potential has entire
cubic homogeneous form
\[
Q_3=-\frac\beta\delta P^2R
    -\frac{\beta\mathcal A}{\delta}Ph^2
    -\frac e\delta PRh+\frac{e_s}{6}h^3.
\tag{14}
\]
These are the literal equal-degree coefficient formulas, not
those from an earlier strict-degree orientation.

The abstract degree(2,4,6) normal form370 and its exact quotient
description provide the ENTIRE intrinsic curve ideal(H-h0,G),
with G of degree three and G3 a nonzero multiple of R^3.
The normal form covers zero centered level. Since H2 is not
divisible by R, the highest forms H2 and G3 are coprime.
A finite top-syzygy descent therefore gives, for every degree
at most three element of this ideal, a representation with
an affine-linear multiplier of H-h0 and a constant multiplier
of G. Applying it to the genuine fourth level forces
\[
Q_3=(l_PP+l_RR+l_hh)H_2+\eta R^3.
\tag{15}
\]
Comparison of P^2R, PR^2 and PRh uniquely gives
\[
l_P=-\beta/\delta,\quad l_R=\beta/(4\delta^3),
\quad l_h=-2\mathcal A/\delta.
\]
But the remaining coefficient is
\[
\boxed{[Rh^2]\bigl(Q_3-(l_PP+l_RR+l_hh)H_2\bigr)
=-\frac{5\beta\mathcal K}{16\delta^5}\ne0.}
\tag{16}
\]
It cannot occur in eta*R^3. This is the contradiction. The
full423 proof establishes the ideal and descent before this
coefficient comparison; a check of(16) alone is not that proof.

## 6. Exhaustion and recognition

Sections3--5 remove all six profiles in(7), which were exhaustive
under k=s and n_ss nonzero. The contrary assumption is impossible.
This proves(3) relative to the retained dependencies.

In the normalized chart, the fully read working theorem
[363](principal-paraboloid-first-potential-affine-in-s-recognition-pass363-working.md)
now applies and gives n_ts=0. Its actual normalization348 and
one-variable recognition346 give A0 isomorphic to C^[3].
Those recognition dependencies remain part of this working
corollary; this synthesis does not recursively re-prove them.

For the broader statement(4), let m=k_s in C* and k_ttt=0.
Exact joint constants give
\[
k=ms+\gamma t^2/2+bt+d,\quad \gamma,b,d\in\mathbb C.
\]
Sections2--3 of363 supply the ACTUAL complex polynomial map
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z,\quad
W_1=mW+\gamma Z/2+bY+dX^2,
\tag{17}
\]
with polynomial inverse obtained by division by m only.
This normalization does not require n_ss=0. It preserves every
actual chart condition and gives
\[
k_1=s_1=k,\quad t_1=t,\quad n_1=n-\gamma k/2,
\quad (n_1)_{s_1s_1}=n_{ss}/m^2.
\tag{18}
\]
Apply(3) to this chart. Equation(18) forces the original n_ss=0.
The ORIGINAL chart then satisfies all hypotheses of363,
which gives n_ts=0 and recognizes A0. This proves(4).
The arbitrary-n mixed derivative is
(n1)_t1s1=n_ts/m-k_t*n_ss/m^2; no premature cancellation of
its second term is used.

## 7. Verification boundary and what remains open

The new inputs are419,420,421 and423;417 is the held earlier
exhaustive frontier. Root read all current components completely.
Separate agents reconstructed the new arguments and checked
their finite coefficient identities. Root's additional fresh
unsaved06c160 recovers the three forced multipliers and the
nonzero coefficient(16) directly in the original(P,R,h) slots.
Exact hash and source-review outcomes are recorded in the ledger.
No saved checker was run, imported, compiled or rerun.

For the corollary, Root completely reread363 in434958 and
348/346 in51c331. General separately read all three, checked
their held hashes and earlier review records, and reconstructed
the arbitrary-n normalization in fresh unsavedb92f8f. That audit
found no new composition gap. It is not a recursive certification
of every earlier recognition dependency.

The remaining global obligations include general coupling k,
other full initial kernels and degree profiles, and entry from
an arbitrary sliced polynomial four-ring. No argument here shows
that these are finitely many easy cases, or that the present
restricted chart represents every cancellation candidate.

The intended field and dimension in Luo's email are still
unconfirmed. This note claims no unrestricted cancellation proof,
historical novelty, human-expert review, publication readiness
or proof-assistant certification. No external contact or
submission has occurred.
