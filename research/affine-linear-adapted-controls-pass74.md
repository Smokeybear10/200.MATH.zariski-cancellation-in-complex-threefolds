# Exact adapted-coordinate controls for affine-linear actions

The separate [standalone checker](affine_linear_adapted_checks_pass74.py)
contains two bounded methods. Unlike the preceding formal companion
controls, its two positive examples are actual sliced affine-linear
LNDs on a polynomial four-ring. Finite examples do not prove the
general affine-linear degree bound or its sharpness.

## Actual flows, projections, and inverse maps

The first method uses the length-four nilpotent chain
\[
E=\partial_{x_0}+x_0\partial_{x_1}
  +x_1\partial_{x_2}+x_2\partial_{x_3}
\]
and a second example with two length-two chains, transported by a
specified invertible linear map and a nonzero translation. The latter
checks the affine coefficient formula \(p'=Ap-N'q\), rather than
only actions already in a preferred linear frame.

For each example, the checker verifies \(N^4=0\),
\(\ell N=0\), \(\ell p=1\), and \(p\notin\operatorname{im}N\).
It calculates the actual finite flow
\[
\Phi_t(x)=\sum_{j=0}^3\frac{t^j}{j!}N^jx
          +\sum_{j=0}^3\frac{t^{j+1}}{(j+1)!}N^jp
\]
and verifies its differential equation, group law, and
\(w(\Phi_t(x))=w(x)+t\) for \(w=\ell x\).
The maximal chain has a genuinely nonzero fourth time coefficient.

The projection \(\pi(x)=\Phi_{-w(x)}x\) is checked to land in
\(\ker\ell\), to be invariant under both the derivation and flow,
and to satisfy \(\Phi_w(\pi(x))=x\). Its degree is at most four
in both cases. A specified linear section
\(\iota(U)\in\ker\ell\) identifies the three invariant
coordinates \(u\).

The supplied slice in these tests is genuinely different from the
linear slice: \(s_*=w+u_1^2+u_2\). The checker computes, rather
than merely stipulating,
\[
h(U)=s_*(\iota(U)),\qquad \deg h\le\deg s_*=d.
\]
It verifies both polynomial inverse orders for
\[
F(x)=(u(x),s_*(x)),\qquad
G(U,S)=\Phi_{S-h(U)}\iota(U),
\]
and verifies that the transported derivation is the fourth coordinate
partial. The measured degrees satisfy
\(\deg F\le\max(4,d)\) and \(\deg G\le4d\).
These examples test the formulas independently; the all-action degree
estimate requires the separate written argument.

## Necessary hypotheses

The second method takes a nilpotent \(N\) with \(p=Nq\).
The actual vector field vanishes at \(-q\), and the linear equations
\(\ell N=0,\ell p=1\) have no solution. A polynomial probe also
has zero derivative there. The reason no polynomial slice exists is
the general evaluation argument at that fixed point, not a conclusion
from finitely many probes.

Conversely, the actual affine field
\(E=x_0\partial_{x_0}+\partial_{x_1}\) has linear slice \(x_1\)
and \(p\notin\operatorname{im}N\), but is not locally nilpotent:
\(E(x_0)=x_0\ne0\). This exact eigenfunction identity proves
nonvanishing of all its iterates by induction. The control prevents
dropping the LND premise from the affine argument.

## Verification and scope

The first completed two-method run passed in **2.354 seconds**,
exit zero. Only `unittest` and SymPy are imported. No previous
checker, research solver, source classification, or full regression
runner is imported or executed. The complete saved checker and this
note received author EOF self-review; independent reviews are separate.

The bounded local search found earlier affine-coordinate and
universal inverse-pair arguments, but did not locate this exact
adapted \(4d\) degree estimate. That search is not a literature or
novelty verdict. No uniform parameter-space section, nonlinear
recognition theorem, universal frame, or general cancellation result
is supplied by the tests. No pass73 or earlier file or shared metadata
was changed.
