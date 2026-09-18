# Recognition with at most cubic longitudinal coupling

Working recognition corollary, with the inherited recognition
dependencies retained explicitly: under EVERY actual hypothesis of264,
\[
\boxed{k_s\in\mathbb C^*,\qquad k_{tttt}=0
\quad\Longrightarrow\quad n_{ss}=n_{ts}=0,\quad n_s\in\mathbb C,
\quad A\simeq\mathbb C^{[3]}.}
\tag{1}
\]
There is no additional hypothesis on either potential n or ell.
This extends the earlier at-most-quadratic longitudinal case422 to
at most cubic dependence. It is a theorem inside the supplied chart,
not a proof that arbitrary cancellation candidates enter that chart.

## 1. Exact scope and notation

Retain the ENTIRE actual setup of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
the polynomial ring B=C[X,Y,Z,W]=A[u], E=partial_u, exact E-degrees
(1,2,2,2), full weighted initial kernel mathsf X^2*mathsf Z-mathsf Y^2,
and nonzero literal selected N=[u^4]partial_Z restricted to A.
The exact coefficient field L, finite over C(t,s), whole and strong
returns, original slice X=a0*u+x0 and calibrated scalar -a0^4 in L*
are all required, as are the remaining localization and genuine
potential conditions. No partial list of formal equations replaces
this actual input.

The coefficient partials commute and have joint constants C. Put
\[
m=k_s\in\mathbb C^*,\qquad \mathbb F=\ker_L\partial_s.
\tag{2}
\]
The field mathbb F is finite over C(t), not presumed rational.
The literal coordinate rows are
\[
Y=y+\sigma X+tX^2,\qquad
Z=z+(2t\sigma+k)X+t^2X^2,\qquad
W=w+\theta X+sX^2.
\tag{3}
\]

For interpretation only, exact subtraction writes k=ms+f with
f in mathbb F. If k_tttt=0, joint constants successively give
\[
f=c_3t^3/6+c_2t^2/2+c_1t+c_0,
\qquad c_0,c_1,c_2,c_3\in\mathbb C.
\tag{4}
\]
For example f''' is a joint constant, then f''-f'''t is a joint
constant, and the next two subtractions give the remaining constants.
This is a consequence of the exact derivatives, not an assumed
rational coefficient ansatz. No cubic normalization to k=s is used.

## 2. The only actual normalization needed

Use the ACTUAL complex polynomial scaling
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=mW,
\qquad t_*=t,\quad s_*=ms.
\tag{5}
\]
Its inverse divides W* by the complex nonzero constant m.
The full initial kernel is unchanged because its defining relation
uses only X,Y,Z; all four exact degrees are preserved. The literal
Z partial, selected N, coefficient field L and global slice are
unchanged. The intercepts and slopes transform by
\[
y_*=y,\quad z_*=z,\quad w_*=mw,\quad
\sigma_*=\sigma,\quad\theta_*=m\theta,
\quad k_*=k,
\tag{6}
\]
so both whole-ring and fraction-field returns are preserved.
The actual row determinant gains a factor m, while the parameter
change s*=ms contributes 1/m; their product is one. Thus the full
calibrated scalar is still -a0^4. No moving coefficient or original
slice has been normalized away.

The first two264 potentials give exactly
\[
n_*=n,\quad \ell_*=\ell,\qquad
(k_*)_{s_*}=1,\qquad
(n_*)_{s_*s_*}=n_{ss}/m^2,
\quad (n_*)_{t_*s_*}=n_{ts}/m.
\tag{7}
\]
To see that no transverse assumption on n is hidden, the first
potential is z=2ty+sigma^2+k_t*sigma+m*theta+n. Replacing m*theta
by theta* leaves n unchanged. In the second potential, k_ts=k_ss=0
because m is constant; n_s*theta becomes (n_s/m)*theta*, unchanged.
The leading term mw becomes w*, so ell is unchanged as well.

Consequently the normalized chart has
\[
k_*=s_*+f_*,\quad (f_*)_{s_*}=0,\quad
(f_*)_{t_*t_*t_*t_*}=k_{tttt}=0.
\tag{8}
\]
The t-derivative is unchanged because t*=t and s*=ms with m complex.
This scaling is the same fully licensed initial scaling in457;
it does not require n_ss=0 in advance.

## 3. Exhaustive split and recognition

First suppose k_ttt=0. The ORIGINAL chart satisfies precisely
the hypotheses of the retained recognition synthesis
[422](principal-paraboloid-constant-coupling-recognition-synthesis-pass422-working.md).
It gives n_ss=n_ts=0 and A isomorphic to C^[3]. Since both exact
derivatives of n_s vanish, joint constants give n_s in C.
No new component argument is needed on this branch.

Now suppose k_ttt is nonzero. In the scaled chart, f*''' is nonzero.
If n_ss were nonzero, (7) would make n*_{s*s*} nonzero as well.
All hypotheses of the balanced-frontier synthesis
[468](principal-paraboloid-nonlinear-first-balanced-frontier-pass468-working.md)
would hold. Its necessary balanced coefficient condition is
f*'''' nonzero. This contradicts (8). Therefore
\[
n_{ss}=0.
\tag{9}
\]
Return to the ORIGINAL chart. It now satisfies all hypotheses of
[457](principal-paraboloid-affine-first-potential-recognition-pass457-working.md):
constant nonzero coupling and n_ss=0, with no restriction on k_ttt,
n_ttt or ell. That theorem gives n_ts=0, n_s in C and
A isomorphic to C^[3]. This proves (1) on the second branch too.
The two branches are exhaustive because k_ttt is an element of a field.

## 4. Recognition dependencies and verification limits

The new implication in the nonzero-k_ttt branch is n_ss=0, obtained
from the complete strict exclusion and the mandatory balanced
f'''' condition. Its proof does not require classifying or realizing
any remaining balanced coefficient functions.

The actual recognition endpoints are RETAINED working theorems.
For the zero-k_ttt branch,422 uses363 and then348/346. For the other
branch,457 uses436, whose endpoints retain348/346,427, and the
specified actual invariant-coordinate entry266 with its regularity
and recognition conditions. This note does not replace those
original-ring arguments by an intrinsic polynomial change over L.
Nor does it recursively re-certify their full proof pedigree or
newly verify their published recognition inputs.

Root freshly read the complete422 and457 in20e933 and revalidated
their hashes in27d5c9. Geometry separately read both,264 and436,
and reconstructed the complete arbitrary-n scaling, both potentials,
mixed derivatives and scalar factor in fresh134ecf. Root's unsaved
afbd08 supplied additional transport and cubic-derivative checks.
The written exact-constant argument proves (4); testing a cubic
polynomial alone would not prove that representation.

The independent held-source reviews of468 and this note belong in
the research ledger. Earlier recognition dependencies remain explicit
retained inputs. No historical novelty, external expert review or
formal proof-assistant certification is claimed.

The full cancellation conjecture remains unsolved. The restrictions
to a supplied actual chart, constant nonzero coupling and vanishing
fourth longitudinal derivative are not proved for arbitrary candidates.
Variable or zero coupling, other initial kernels and time-degree
profiles, and arbitrary actual-frame entry remain outside this result.
No saved checker was executed, imported, compiled or rerun. No external
contact, publication, submission, paid service or automation occurred.
