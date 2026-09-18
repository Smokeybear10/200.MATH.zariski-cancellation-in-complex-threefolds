# Conditional recognition for quadratic sigma and nonconstant affine theta

Working scoped synthesis: retain EVERY actual hypothesis of264. If
the original intrinsic degrees are
\[
\deg_v\sigma=2,\qquad \deg_v\theta=1,
\]
then the coupling \(m=k_s\) is complex constant. In particular the
retained constant-coupling recognition473 implies
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
The new part is exclusion of noncomplex m in this specified profile.
The final recognition retains473's historical dependencies; this
note does not recursively certify those dependencies anew. Neither
an arbitrary cancellation candidate nor another nonlinear degree
profile is assumed to enter this chart.

## 1. Exact scope and dependencies

The actual chart is
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original weighted initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\quad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad L[A]=L[v],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The full original global-slice, localization and selected-partial
hypotheses of [264](principal-one-affine-paraboloid-chart-pass264-working.md)
remain required, not just an abstract polynomial parametrization
obeying some equations in (2). The intercept z_int is literal.
For nonzero m, the genuine296 potentials and535 cleared multiplier
are used with their proved levels and unit conditions.

The directly composed sources are:

- [537](principal-paraboloid-quadratic-sigma-affine-theta-longitudinal-exclusion-pass537-working.md):
  in this profile and for m nonzero, deg y is at most two and m_t=0;
  if m is noncomplex, k_tt is complex and y+(k_tt/4)sigma belongs to L.
- [539](principal-paraboloid-quadratic-affine-transverse-normal-form-pass539-working.md):
  an actual complex coordinate normalization preserving EVERY entry
  condition, followed by an exhaustive two-branch necessary split.
- [540](principal-paraboloid-quadratic-affine-constant-midpoint-exclusion-pass540-working.md):
  exclusion of the first branch, including both h_s cases.
- [541](principal-paraboloid-quadratic-affine-zero-midpoint-exclusion-pass541-working.md):
  exclusion of the second branch in the original field.
- [473](principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md):
  the retained recognition endpoint for every complex m, including zero.

There is no restriction here on deg y, on a lower coefficient of
sigma or theta, or on either derivative of m beyond what these
actual hypotheses prove. The zero-coupling branch does not use an
identity that divides by m.

## 2. Exhaustion of the noncomplex-coupling case

Suppose for contradiction that m is not complex. In particular m
is nonzero. By537, m_t=0 and h=m_s is nonzero; the latter follows
because the joint exact constants of L are C. Put q=k_tt/4 and
b0=k_t-4qt. Both q and b0 are complex. The actual map539
\[
X^*=X-q,\qquad Y^*=Y+(b_0/2)X^*,\qquad Z^*=Z,\qquad W^*=W
\tag{3}
\]
has a complex polynomial inverse, preserves the original slice,
selected literal Z-partial, entire initial kernel, and exact
profile, and gives k*_t=0 and y*=r in L. Its actual fiber argument
preserves both strong intercept returns. The full scalar remains
-a0^4. Adding intrinsic constants to sigma and theta preserves
their exact degrees two and one. Thus all subsequent uses of the
normalized chart have their actual licenses.

Drop stars. In the finite intrinsic normalization of539, write
sigma=x^2+c and theta=d*x+e. Only d^2, c, e are required to lie
in the original L; d and x need not. Put
\[
\lambda=n_t,\qquad
\nu_0=(he+n_s)/m,\qquad C_0=2r+\lambda+hd^2/2.
\tag{4}
\]
The exact all-X divided-difference return forces
\(C_0+dm\nu_0/u\) to be a nonzero Laurent monomial. Thus the
possibilities are exactly
\[
\nu_0=0,\ C_0\ne0,
\qquad\text{or}\qquad
C_0=0,\ \nu_0\ne0.
\tag{5}
\]
This includes repeated-point divided differences. Both quantities
cannot vanish, and neither can both be nonzero. Source539 also
proves (d^2)_t is nonzero, rather than dividing by an unverified
coefficient derivative.

For clarity, both exclusions return to the ORIGINAL parameter
\(\xi=\theta-e\), so that L[xi]=L[v] and
\(\sigma=a\xi^2+c\), where a=1/d^2 lies in L*. They then prove
r_t is nonzero, giving a separating coefficient basis (r,m).
Its exact scalar is
\[
J_{r,m,\xi}(X)=-a_0^4/(r_t h D)\in L^*,\qquad D=\xi_v\in L^*.
\tag{6}
\]
This is a coefficient-field unit, not a chosen complex constant.
Neither r nor m is promoted to an actual ambient coordinate, and
L is only finite over C(r,m), not asserted equal to it.

In the first branch540, the entire actual X=0 rows have the form
\[
Y=r,\qquad Z=a^2\xi^4+2ac\xi^2+m\xi+G,
\qquad W=\gamma\xi^2+w_0,
\tag{7}
\]
with gamma nonzero. The full determinant's quadratic coefficient
is 2gamma-m*gamma_m, with m differentiation at fixed r. All
lower jets cancel out of this coefficient. The necessary ODEs539
give two exhaustive cases:

- If h_s=0, then gamma is a nonzero function of r with complex
  coefficients, so the quadratic scalar coefficient is 2gamma.
- If h_s is nonzero, then h=chi*(m-mu)^3 for complex chi nonzero
  and complex mu. The strong intercept field return excludes mu=0.
  Here gamma=(m-mu)^2 times a nonzero function of r, so the
  coefficient is -2mu*gamma/(m-mu), again nonzero.

Both contradict (6). This includes vanishing integration constants
and the zero leading-r coefficient, which540 treats by the strong
field return before dividing by it.

In the second branch541, a belongs to C(r)* and the actual X=0
rows instead have W=-nu0*xi+w0. The actual localized polynomial
three-ring and its nonzero LND force nu0 to be algebraic over C(r).
Consequently both a and nu0 have zero m partial at fixed r.
The ENTIRE determinant has cubic coefficient -4a^2*(w0)_m;
its vanishing forces (w0)_m=0. Its linear coefficient is then
-nu0, contradicting this branch's nonzero nu0. Algebraicity is
sufficient; no rationality of nu0 or the derivative-constant
field is asserted.

These two contradictions exhaust (5). Therefore m is complex.
This conclusion is independent of the retained recognition endpoint.

## 3. Recognition and exact boundaries

Apply473 only AFTER the conclusion m in C. Its nonzero-complex
branch retains422/457 and their specified recognition ancestors;
its zero branch retains268/294. Both possibilities are expressly
covered in473. Hence (1) follows subject to those retained working
recognition dependencies.

Nothing in this composition uses537--541 when m=0, and no extra
claim about deg y or the second potential is made for m=0. Theta
constant, theta degree at least two, or sigma of another degree
are not cases of this theorem. The affine-sigma synthesis534 and
the earlier constant-theta result303 are separate results, not
silent extensions of (1).

The supplied chart is highly restrictive. Entry from an arbitrary
A[u]=C^[4], other entire initial kernels and other exact time
profiles remain unresolved. Even complete recognition of this
chart would not by itself solve general cancellation. Luo has not
confirmed the field and dimension intended in the pasted email.

## 4. Verification record

Root read the complete current264,473,537,539,540 and541 through
EOF before this composition. The held hashes and separate complete
AI reviews of539--541 are recorded in the ledger. These are source
and exact-algebra audits, not human expert review or proof-assistant
certification. The entire historical dependency chain is not
recursively re-certified by this synthesis.

Fresh unsaved28580f independently reconstructed the ENTIRE two
terminal scalar determinants with arbitrary lower jets, the full
539 coefficient Jacobian, the integrated mu derivative, and both
nonzero quadratic-coefficient formulas. Every identity residual
was zero. The actual-ring, invariant, field and exhaustion steps
are written arguments, not conclusions from numerical samples.

No saved checker was executed, imported, compiled or rerun. No
external message, submission, publication, automation or git
mutation occurred. No novelty or publication-readiness claim is
made. A complete separate source review of this synthesis remains
required before canonical acceptance.
