# Conditional recognition when theta is affine or constant

Working scoped synthesis: under EVERY actual hypothesis of264,
\[
\boxed{\deg_v\theta\le1\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
The zero polynomial theta is included. Sigma may have any degree;
zero and constant sigma are included. The conclusion retains the stated
historical recognition dependencies of473 and478. It is not a
theorem that an arbitrary cancellation candidate admits this chart.

If sigma is nonconstant, the argument moreover forces m=k_s to
belong to C. That extra conclusion must NOT be extended to constant
sigma:478 treats a variable-coupling line instead.

## 1. Actual input, not a formal parametrization

Retain the complete construction of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
X=a_0u+x_0,\quad a_0\ne0,\quad
0\ne N=[u^4]\partial_Z|_A,\quad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad L[A]=L[v],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\quad J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The original global slice, literal selected partial, both strong
returns and every actual entry condition remain required. The
symbol z_int denotes the literal Z-intercept. The partials on
L are its exact commuting extensions from C(t,s), not partials
on a presumed rational coefficient field.

When m is nonzero,264 also gives
\[
L[y,\sigma,\theta]=L[v],\qquad
H(y,\sigma,\theta)=h_0,
\tag{3}
\]
where H-h0 is monic quadratic in its first formal variable U.
The genuine296 levels and535 unit multiplier are used only in
the nonzero-m branches where their hypotheses hold.

If m belongs to C, including m=0, apply the retained
[473](principal-paraboloid-complete-constant-coupling-recognition-pass473-working.md)
endpoint immediately. Its two complex-coupling cases are separately
proved there. No division by m is used in this branch. It remains
to consider noncomplex m, which in particular is nonzero.

## 2. Constant theta, including theta zero

Suppose theta belongs to L. If sigma also belongs to L, the monic
relation in (3) would make y algebraic over L. A nonconstant
polynomial in v is transcendental over L, so y would belong to L
as well. This contradicts the whole polynomial return in (3).

Otherwise put d=deg_v(sigma)>0. Equation (3) gives
\[
L(v)=L(\sigma,y),\qquad [L(v):L(\sigma)]\le2.
\tag{4}
\]
The inequality follows from the monic quadratic relation in y
over L(sigma); theta is already a coefficient.

For completeness, [L(v):L(sigma)] equals d. The ring L[v] is
free of rank d over L[sigma], with basis 1,v,...,v^(d-1).
The leading coefficient of sigma is a nonzero field element, so
polynomial reduction generates this module. Independence follows
because the nonzero terms a_i(sigma)*v^i have distinct highest
degrees modulo d. Localizing over the fraction field L(sigma)
gives a finite domain over a field, hence a field, namely L(v).
This proves the claimed degree without assuming a splitting or
rationality of the coefficient field.

Thus d is one or two. If d=1, the retained complete
[affine-sigma synthesis534](principal-paraboloid-complete-affine-sigma-recognition-pass534-working.md)
forces m in C, contradicting the standing assumption. If d=2,
the projected algebra is L[sigma,theta]=L[sigma] and its
function-field projection has exact degree two. These are exactly
the nonconstant-sigma hypotheses of
[303, Section3](principal-paraboloid-double-cover-line-obstruction-pass303-working.md),
which force m in C*. This is again a contradiction. Its
constant-sigma double-cover branch is not being used here.
Consequently no noncomplex-m case with constant theta remains.

## 3. Nonconstant affine theta and every sigma degree

Now deg_v(theta)=1, so L[theta]=L[v]. First suppose sigma is
in L. The projected plane equation is P-sigma=0, a line, and
\[
L(\sigma,\theta)=L(v).
\tag{5}
\]
Thus the projected-line and degree-one projection assumptions of
[478](principal-paraboloid-constant-sigma-variable-coupling-recognition-pass478-working.md)
are supplied, not added without proof. Under the standing noncomplex
m it gives m_s=m_tt=0, m=a*t+d with a in C* and d in C, and
recognizes the actual kernel. Its earlier475 and published
recognition dependencies are retained explicitly. In particular,
this branch does not force m complex.

If sigma is nonconstant, there are three exhaustive degree cases:

- Degree one:534 forces m complex, for every theta degree.
- Degree two: the complete
  [542](principal-paraboloid-quadratic-affine-recognition-synthesis-pass542-working.md)
  forces m complex through the full537/539/540/541 case split.
- Degree at least three: the new
  [543](principal-paraboloid-higher-sigma-affine-theta-exclusion-pass543-working.md)
  excludes noncomplex m in every degree, including the cubic boundary.

Each contradicts the noncomplex-m assumption. The last argument
is uniform in the degree, not a finite enumeration or a use of
an assumed coefficient-function bound. This proves (1), and the
additional complex-m conclusion when sigma is nonconstant.

## 4. Verification and exact remaining scope

The root author read complete current264,303,473,478,534,542 and
the corrected final543 before this synthesis. Sources539--543
have complete separate AI source audits.543's review corrected
one omitted subleading support term and clarified which whole
polynomial groups were being bounded; neither correction changes
the strict all-degree inequalities. The final held source, not
the superseded draft, is the dependency here.

The directly used historical sources are retained at their stated
scopes, not recursively re-certified.473 includes the separate
zero-coupling268/294 and nonzero-coupling422/457 endpoints.478
retains475's actual-coordinate construction and its published
nice-derivation and regular-kernel inputs. This note does not
replace any actual-coordinate hypothesis with an intrinsic or
localized coordinate assertion.

The higher-degree scalar and polynomial calculations were
independently reconstructed in fresh unsaved5f52e0,0fc15d,078c77.
The new work here is the exhaustive composition and the explicit
constant-theta/constant-sigma boundary check, not a new proof of
the classical polynomial function-field degree formula.

Theta degree at least two is outside this theorem, as are other
entire initial kernels, time profiles and arbitrary chart entry.
Luo's intended field and dimension remain unconfirmed. General
complex-threefold cancellation is still unsolved by this project.
No novelty, expert approval, Lean certificate or publication
readiness is claimed. All saved checkers remain frozen; none
was executed, imported, compiled or rerun. No external contact,
submission, posting or git mutation occurred. A separate complete
source review of this synthesis is required before acceptance.
