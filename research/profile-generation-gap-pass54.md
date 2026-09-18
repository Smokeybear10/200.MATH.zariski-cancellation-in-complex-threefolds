# The projected degree-five bridge is a slice-selection problem

The supplied quadratic frame does not bound the projected intrinsic
degrees for an arbitrary original slice. There is an actual polynomial
replica automorphism producing arbitrarily high such degrees in every
instance of the genuine degree-two setup, without assuming its kernel
is a polynomial ring.

The relevant minimum is different. A single original-coordinate
projection is bounded by \(F_5\) exactly when it is bounded by \(F_4\).
At an actual reduced zero-first-jet obstruction, the already proved
quartic algebra theorem excludes every such projected list.
A generating set unrelated to one slice is a separate question.
No upper bound of five for that minimum is proved or disproved here.

## 1. The full supplied frame and two different degrees

Retain the actual independent degree-two setting of the
[generic bad-coordinate theorem](generic-bad-pair-pass44.md) and the
[open-set generation theorem](frame-filtration-generation-pass49.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\quad
Es_*=1,\quad A=\ker E,
\]
\[
C=\ker D\simeq\mathbb C^{[2]},\quad
L=\operatorname{Frac}C,\quad
B_L=L[x_3,x_4],\quad A_L=L[j],
\quad j=gx_3-fx_4.
\tag{1}
\]
Here \(D\) is the actual primitive intrinsic LND and
\[
Ex_3=f,\quad Ex_4=g,\quad E^2x_i=h_i\quad(i=1,2),
\qquad f,g,h_i\in C.
\]
The two bad speeds are algebraically independent. The actual generic
graph is
\[
x_i=\mathcal Q_i(x_3,x_4),\qquad
\mathcal Q_i\in L[X_3,X_4],\quad \deg\mathcal Q_i\le2,
\tag{2}
\]
and at least one \(h_i\ne0\).
The frame has the stipulated actual adjoint bounds
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0,
\]
with two independent highest quadratic fields.
No existence of such a frame for every sliced action is assumed.

Fix an actual invariant localization \(R\) of \(C\), including
\(R=C_{\mathfrak m}\), and write
\[
\mathcal A=A_R,\quad\mathcal B=B_R,\quad
F_n=\ker(D^{n+1}:\mathcal A\longrightarrow\mathcal A).
\]
Since \(Dj\in L^*\), the intrinsic \(D\)-degree on
\(\mathcal A\subset L[j]\) is precisely its \(j\)-degree.

An original slice is not an element of \(\mathcal A\).
Its transverse degree below refers to its invariant difference
from a fixed affine generic slice. This avoids silently choosing
an extension of \(D\) to \(\mathcal B\).

## 2. An exact affine-coset obstruction to choosing a bounded slice

Choose an affine generic \(E\)-slice \(\sigma_0\), for example
\(x_3/f\), in \(B_L\).
Every actual slice \(s\in\mathcal B\) has a unique expression
\[
s=\sigma_0+H(j),\qquad H\in L[j].
\tag{3}
\]
Fix one actual supplied slice
\(s_*=\sigma_0+H_*(j)\).
Two actual slices differ by an element of \(\ker E=\mathcal A\),
so the set of all possible \(H\)'s is exactly
\[
\boxed{H_*+\mathcal A\subset L[j].}
\tag{4}
\]
The converse is literal: adding any element of \(\mathcal A\)
to \(s_*\) gives another actual polynomial slice.

For an integer \(N\ge1\), the condition for an actual slice with
\(\deg_j H\le N\) is therefore
\[
\boxed{
H_*\in\mathcal A+L[j]_{\le N}.
}
\tag{5}
\]
This is an additive-module membership condition in the actual
embedded ring. It is not a consequence of generic polynomiality,
nor does it replace \(\mathcal A\) by a conic subalgebra.
The class
\[
[H_*]\in L[j]/\bigl(\mathcal A+L[j]_{\le N}\bigr)
\tag{6}
\]
is independent of the initially supplied actual slice.
It is also independent of an affine generic slice choice for
\(N\ge1\): two such choices differ by an affine polynomial in \(j\).
Changing the generator of \(L[j]\) makes an affine substitution
with coefficients in \(L\), which preserves all these degree
conditions. The same invariance is not asserted for the cutoff
\(N=0\).

This isolates a genuine selection obligation. Generic coordinates
alone do not put a low-degree representative of (4) in the actual
ring.

## 3. Why a projected \(F_5\) list is already an \(F_4\) list

Write the generic graph using \((j,\sigma_0)\):
\[
x_i=\frac{h_i}{2}\sigma_0^2+
      A_i(j)\sigma_0+B_i(j),\qquad
\deg A_i\le1,\quad\deg B_i\le2.
\tag{7}
\]
For the actual slice in (3), its projection is
\[
\rho_s(x_i)=\frac{h_i}{2}H^2-A_iH+B_i.
\tag{8}
\]
Each bad projection has degree at most \(\max(1,\deg H)\).
If \(n=\deg H\ge2\), choose a good index with \(h_i\ne0\).
The first term in (8) has degree \(2n\), while the other two
have degrees at most \(n+1\) and two. Hence
\[
\boxed{
\max_{1\le i\le4}\deg_D\rho_s(x_i)=2n
\quad(n\ge2).
}
\tag{9}
\]
The leading coefficient is nonzero in \(L\), so no cancellation
at that degree is possible.
For \(\deg H\le1\), all four degrees are at most two.

It follows exactly that
\[
\begin{aligned}
&\exists s\in\mathcal B,\ Es=1,\
       \rho_s(x_i)\in F_5\text{ for all }i\\
\Longleftrightarrow\quad&
H_*\in\mathcal A+L[j]_{\le2}\\
\Longleftrightarrow\quad&
\exists s\in\mathcal B,\ Es=1,\
       \rho_s(x_i)\in F_4\text{ for all }i .
\end{aligned}
\tag{10}
\]
More generally, for a single chosen slice and every \(k\ge1\),
a bound \(F_{2k+1}\) on all four projections is equivalent
to the bound \(F_{2k}\).

The actual projection \(\rho_s:\mathcal B\to\mathcal A\) is
surjective and fixes \(R\). Since the four original coordinates
generate \(\mathcal B\) over \(R\), they give
\[
\mathcal A=R[\rho_s(x_1),\ldots,\rho_s(x_4)].
\tag{11}
\]
Thus (10) would imply \(\mathcal A=R[F_4]\), not merely
generation by \(F_5\).

At an actual reduced zero-first-jet obstruction,
the [exact quartic algebra theorem](quartic-fiber-gate-pass52.md)
already proves
\[
R[F_4]\ne\mathcal A.
\tag{12}
\]
Consequently (5) fails for \(N=2\) there. Every actual slice
then has transverse degree at least three, and the maximum
intrinsic degree in its projected original list is at least six.
This conditional conclusion uses no new existence assertion
for an obstruction point.

The later [quintic velocity theorem](quintic-fiber-velocity-pass53.md)
concerns the entire algebra \(R[F_5]\), not just these special
four-element lists. Its structural consequences must be
established separately. The statement (12) alone does not
exclude a different generating set contained in \(F_5\).

## 4. Arbitrarily high slice degrees in the same actual frame

There is an all-instance version of the explicit control already
recorded in pass 49.
Choose an actual intrinsic local slice \(r\in A\) with
\[
Dr=p\ne0,\qquad Er=0.
\]
Over \(L[j]\), write
\[
r=\alpha j+\beta,\qquad \alpha\in L^*,\quad\beta\in L.
\tag{13}
\]
For any integer \(N\ge2\), the replica flow
\[
\Phi_N=\exp(r^N E)
\tag{14}
\]
is an actual polynomial automorphism of the original four-ring.
It fixes \(A\), in particular \(r\), and its inverse is
\(\exp(-r^N E)\).
Since \(E^3x_i=0\), its original-coordinate formulas are
\[
\Phi_N(x_i)=x_i+r^NEx_i+\frac{r^{2N}}2E^2x_i.
\tag{15}
\]
For the bad coordinates the last term is zero.
The inverse uses the negative sign in the linear term and the
same quadratic term. In both compositions \(r\) stays fixed.
Thus (14)--(15) do not assume a polynomial coordinate system
for \(A\), a Jacobian-only inverse, or cancellation.

It sends the actual slice to
\[
s_N=\Phi_N(s_*)=s_*+r^N.
\tag{16}
\]
If \(N>\max(1,\deg H_*)\), its new generic gauge
\(H_*+r^N\) has degree exactly \(N\).
Equation (9) gives exact maximum projected degree \(2N\).
The action \(E\) and the supplied original coordinate frame
have not changed at all.

Therefore even the full actual profile does not give a bound
on an arbitrary supplied slice's projected degrees. This is
a quantifier statement valid within every actual instance,
not an example whose weak hypotheses have been mistaken for
the target.

It does not give a lower bound on the minimum generating degree:
the shifts (16) differ from the original slice by actual elements
of \(A\), so they have the same obstruction class (6).
The explicit already-polynomial example in pass 49 has these
unbounded lists while \(A=C[F_1]\). That example remains a
countercontrol only for an arbitrary-list bound.

## 5. The bounded original flow is a different invariant

The adjoint profile also gives the inherited original time-degree
bound from
[pass 39, Section 2](two-quadratic-defects-pass39.md#2-the-six-dimensional-linearization).
Let \(F_t=\exp(tE)x\), and let \(C(t)\) be the coefficient matrix
of \(\exp(tE)T_i\exp(-tE)\). Applying those fields to \(F_t\) gives
\[
\operatorname{Jac}(F_t)C(t)=I,\qquad \det C(t)=1.
\tag{17}
\]
Its four column degrees are bounded by \((1,1,2,2)\).
Each three-column cofactor has time degree at most five, so
\[
\deg_t\operatorname{Jac}(F_t)\le5,\qquad
E^6x\in\mathbb C^4,\qquad E^7x=0.
\tag{18}
\]
The cofactor argument does not require independent quadratic tops.
The stronger companion calculation, under independence, was
already written in pass 39. No new flow-bound result is claimed.

If some \(E^6x_j\ne0\), (18) provides the actual slice
\(E^5x_j/E^6x_j\).
It does not force this coefficient to be nonzero.
In the present genuine degree-two residual it is identically
zero, so the suggestion gives no slice at all. More generally
the finite time degree of \(E\) is not the transverse degree
of an arbitrary slice in Section 4.

There is also an exact exclusion of a proposed constant-iterate
shortcut in the present rank-two leading distribution.
Suppose \(E^dx_j=c\in\mathbb C^*\), and
\(V_i=\operatorname{ad}_E^2T_i\) with
\(\operatorname{ad}_E^3T_i=0\).
Write \(W_i=[E,T_i]\).
For \(d\ge2\), reordering gives
\[
0=-dE^{d-1}W_i(x_j)+\binom d2E^{d-2}V_i(x_j).
\]
Apply \(E\), and compare with the reordered equation for
\(T_iE^{d+1}x_j=0\). Subtraction yields
\[
E^{d-1}V_i(x_j)=0.
\]
The case \(d=1\) follows directly.
Since \(V_i\) commutes with \(E\), it kills the slice
\(E^{d-1}x_j/c\).
But the present actual degree-two result already gives
\(E\in\operatorname{span}_{\operatorname{Frac}B}(V_3,V_4)\).
Thus both independent tops cannot kill an \(E\)-slice.
This is a consequence of the already proved leading-plane
identity, not a new recognition theorem for other branches.

## 6. The minimum-generation gap is not settled by a large slice

Let the minimum generating degree mean the least \(M\) for which
\[
\mathcal A=R[F_M].
\]
It exists because \(\mathcal A\) is finitely generated as an
\(R\)-algebra and every element has finite intrinsic \(D\)-degree.
It is no larger than the maximum degree of any projected
original-coordinate generating list. The reverse implication
is not automatic: a low-degree generating set need not be the
four projections of any one slice.

The actual graph proves the exact implication (10)--(11).
It does not, by itself, prove the selection condition (5),
nor generation by a different degree-five set.
At a reduced zero-first-jet obstruction, (12) already makes
the former condition impossible. The independent structural
analysis of \(R[F_5]\) is therefore necessary to discuss the
latter condition.

That separate analysis is now supplied by the
[whole-fiber nonvanishing theorem](primitive-fiber-nonvanishing-pass54.md).
Combined with the pass53 velocity calculation, it proves
\(R[F_5]\ne\mathcal A\) in this same conditional sector.
Thus its minimum generating degree is at least six, independently
of the single-slice criterion. A universal upper bound of five
from the actual profile would exclude the sector; proving such
a bound is a substantive additional theorem, not a consequence
of the supplied generic graph. No actual occurrence of the sector
has thereby been constructed.

In particular, neither the original time-degree bound six nor
the existence of an arbitrary polynomial \(E\)-slice supplies
an upper bound of five on the intrinsic generating degree.
This sentence records a missing implication in the stated
arguments; it does not assert a realized actual-frame example
whose minimum exceeds five.

No degree-six enumeration or new finite suite is used here.
The replica inverse, affine-coset criterion and exact degree
comparison are the written deductions. Files from pass 53
and earlier remain unchanged.

An independent full-file audit reconstructed the affine-coset
criterion, every degree comparison, both replica inverse signs,
and the deduplicated constant-iterate and cofactor arguments.
No new numerical suite was added.
