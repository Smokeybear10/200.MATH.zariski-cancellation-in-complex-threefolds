# The actual minimum horizontal degree is one

In the fixed canonical polynomial model, the minimum relative degree
over **all** horizontal LNDs fixing \(x\) is one, not two. An explicit
polynomial inverse attains it, and a parity obstruction excludes zero
without assuming that the horizontal preserves the old invariant plane.

There is also a full description of the degree-one minimizers in the
sector preserving the original triangular subalgebra. Their primitive
tops are sliced. Some of these minimizers are not tangent to the
canonical fixed locus, so canonical normalizing gauges cannot reduce
them to the auxiliary-plane-fixing sector from pass 29.

It remains unproved that every degree-one minimizer in the unrestricted
\(x\)-fixing sector has a sliced primitive top. None of the statements
below presupposes that conclusion.

## 1. The unchanged model and the degree being minimized

Keep the actual canonical construction from
[pass 28](canonical-top-pass28.md):
\[
R=\mathbb C[x,y,z],\quad D=x^2\partial_y+2y\partial_z,
\quad r=y,\quad p=x^2,\quad d=x,
\]
\[
B=R[\lambda,w]/((1+\lambda x)w-y)
  =\mathbb C[x,\lambda,w,z],\qquad v=1+\lambda x,
\]
\[
\Delta x=\Delta\lambda=0,\quad
\Delta w=x^2,\quad \Delta z=2v^2w.
\tag{1}
\]
In particular the input is primitive, its full plinth is nonunit,
and \(d\in\sqrt{p\ker D}\) while \(p\nmid d\).

Let
\[
\mathcal H_x=\{\delta\in\operatorname{LND}_{\mathbb C}(B):
                     \delta x=0,\ \delta\lambda=1\}.
\tag{2}
\]
For each supplied member, the normalized slice coordinates of
[pass 30](horizontal-gauge-pass30.md) give
\[
B=\mathbb C[x,b,c][\lambda],\qquad \delta=\partial_\lambda,
\qquad \Delta=\sum_{j=0}^{q}\lambda^jD_j,
\tag{3}
\]
where the nonzero highest coefficient acts on \(\mathbb C[x,b,c]\).
Define \(q=q(\delta)\) by (3). Equivalently it is the largest
integer with \((\operatorname{ad}\delta)^q\Delta\ne0\).
This makes the degree independent of the choice of invariant
coordinates. In particular \(q=0\) is exactly
\([\delta,\Delta]=0\).

The established coordinate presentation in (1) is essential. The
slice-coordinate argument is not being applied to an unknown
translation quotient to assume that it is polynomial.

## 2. Zero is impossible for every member of the full sector

**Proposition.** No \(\delta\in\mathcal H_x\) commutes with \(\Delta\).

First the exact canonical kernel is
\[
\ker\Delta=\mathbb C[x,\lambda,I],\qquad
I=x^2z-v^2w^2.
\tag{4}
\]
Indeed after inverting \(x\), \(w/x^2\) is a slice and the kernel
is \(\mathbb C[x,x^{-1},\lambda,I]\). To contract it, a putative
highest \(x\)-pole has a numerator whose residue is
\(Q(\lambda,-w^2)\). The substitution
\(\mathbb C[\lambda,I]\longrightarrow\mathbb C[\lambda,w]\),
\(I\mapsto-w^2\), is injective. It cannot cancel that pole.
This proves (4) in the original polynomial ring.

Suppose that \([\delta,\Delta]=0\). Commutation itself, not an
extra plane-preservation assumption, implies that \(\delta\)
preserves (4). Put
\[
\beta=\delta w\in\mathbb C[x,\lambda,I],\qquad
g=\delta I\in\mathbb C[x,\lambda,I].
\]
Differentiating the actual invariant in (4) gives
\[
g=x^2\delta z-2xv w^2-2v^2w\beta.
\tag{5}
\]
Modulo \(x\), its left side is even in \(w\), whereas its right
side is \(-2w\beta(0,\lambda,-w^2)\), which is odd. Hence
both residues vanish. The same injectivity gives
\(\beta=x\beta_1\) and \(g=xg_1\), with coefficients still in
\(\mathbb C[x,\lambda,I]\).

Divide (5) by \(x\), then reduce modulo \(x\):
\[
g_1(0,\lambda,-w^2)
 =-2w^2-2w\beta_1(0,\lambda,-w^2).
\tag{6}
\]
Even and odd parts now give
\[
\beta_1(0,\lambda,I)=0,\qquad g_1(0,\lambda,I)=2I.
\tag{7}
\]

On the other hand, the restriction of \(\delta\) to its stable
kernel subalgebra (4), localized over \(\mathbb C(x)\), is an LND
of the polynomial plane of the form
\[
\partial_\lambda+g(\lambda,x,I)\partial_I.
\tag{8}
\]
An LND of this form must have \(g\) independent of \(I\). Here is
the elementary degree argument, also used in pass 29. If the
\(I\)-degree is \(m\ge2\), the successive degrees on \(I\) are
\(1+j(m-1)\), with nonzero leading coefficients. If
\(g=A(\lambda)I+B(\lambda)\) and \(A\ne0\), the coefficient
of \(I\) in successive iterates satisfies
\(a_0=1,\ a_{j+1}=a_j'+Aa_j\). Its degree is
\(j\deg A\), with nonzero leading coefficient, including when
\(A\) is a nonzero constant. Neither case is locally nilpotent.

Since \(g=xg_1\) is independent of \(I\), so is \(g_1\).
This contradicts (7), proving the proposition. The argument
establishes the quantifier for all of (2), not just a normalizer
subclass.

## 3. An actual degree-one horizontal and its full inverse

Take
\[
\delta_* =\partial_\lambda+2\lambda w^2\partial_z,
\qquad b=w,\quad c=z-\lambda^2w^2.
\tag{9}
\]
The full polynomial inverse is \(w=b,\ z=c+\lambda^2b^2\),
with \(x,\lambda\) unchanged. Thus (9) is an actual coordinate
LND with slice \(\lambda\). Directly from (1),
\[
\Delta b=x^2,\qquad
\Delta c=2(1+\lambda x)^2b-2\lambda^2x^2b
        =2b+4\lambda xb.
\tag{10}
\]
Therefore \(q(\delta_*)=1\). Combined with Section 2 this proves
the full-sector equality
\[
\boxed{\min_{\delta\in\mathcal H_x}q(\delta)=1.}
\tag{11}
\]
The highest coefficient is \(4xb\partial_c\), whose primitive
part is \(\partial_c\), with slice \(c\). The actual coefficient
itself has a nonunit multiplier and is not sliced.

The old horizontal \(\partial_\lambda\) has degree two. Thus the
degree-two minimum proved for the pointwise \(F=2xz-w^2\)-fixing
sector in pass 29 is not the minimum in (2). Indeed (9) does not
fix \(F\).

## 4. Complete degree-one classification in the triangular sector

Consider the precisely restricted sector
\[
\mathcal T_x=\{\delta\in\mathcal H_x:
       \delta(\mathbb C[x,\lambda,w])
           \subseteq\mathbb C[x,\lambda,w]\}.
\tag{12}
\]
No pointwise fixing of \(w\), or of \(F\), is imposed.
This sector and the old \(F\)-fixing sector are not claimed to
contain one another; both lie in the full sector (2).

Every member has unique normalized triangular slice coordinates
\[
b=w-J(\lambda,x),\qquad
c=z-K(\lambda,x,b),\qquad J(0,x)=K(0,x,b)=0.
\tag{13}
\]
To prove this covers all of (12), apply the elementary gate from
Section 2 to the restriction over \(\mathbb C(x)[\lambda,w]\).
It forces \(\delta w\in\mathbb C[x,\lambda]\), which has a
polynomial antiderivative \(J\) with zero constant term. After
putting \(b=w-J\), localize over \(\mathbb C(x,b)\) and apply
the same gate to \((\lambda,z)\). It forces \(\delta z\) to
be independent of \(z\) in this frame, giving the antiderivative
\(K\). Conversely every pair of normalized polynomials \(J,K\)
gives an actual LND through the complete inverse
\[
w=b+J(\lambda,x),\qquad z=c+K(\lambda,x,b).
\tag{14}
\]

In these coordinates the fixed vertical action is exactly
\[
\Delta b=x^2,\qquad
\Delta c=2v^2(b+J)-x^2K_b.
\tag{15}
\]
Put \(j(x)=[\lambda]J\). The necessary and sufficient conditions
for \(q=1\) are
\[
J\equiv\lambda j-2x\lambda^2j\pmod{x^2},
\tag{16}
\]
and
\[
K=\lambda A(x,b)+\lambda^2b^2
   +\frac{2(v^2J-\lambda j)}{x^2}\,b+C(\lambda,x),
\tag{17}
\]
where \(A\in\mathbb C[x,b]\) is arbitrary and
\(C\in\lambda^2\mathbb C[x,\lambda]\) is arbitrary.
The quotient in (17) is a polynomial by (16). There is no
division in the coordinate ring left unjustified.

For necessity, all \(\lambda\)-coefficients of degree at least
two in (15) must vanish. The contribution \(2v^2b\) of such
degrees is divisible by \(x^2\). Hence every coefficient of
degree at least two in \(v^2J\) must also be divisible by \(x^2\).
Since \(J(0)=0\), this says
\(v^2J\equiv\lambda j\pmod{x^2}\). Multiplication by the
inverse \(1-2\lambda x\) modulo \(x^2\) is exactly (16).
Solving the remaining coefficient equations for \(K_b\), then
integrating in \(b\), gives (17). Its linear coefficient is
\(A=[\lambda]K\); the residual scalar polynomial \(C\) has no
constant or linear term. Conversely substitution of (17) into
(15) gives
\[
\Delta c=2b+\lambda\bigl(4xb+2j-x^2A_b\bigr).
\tag{18}
\]
The displayed coefficient cannot vanish identically: that would
make \(x^2\) divide \(4xb+2j\), while its coefficient of \(b\)
is \(4x\). Thus the degree is exactly one, not merely at most one.

Every minimizer in (12) therefore has primitive highest
coefficient \(\partial_c\). In fact any member of (12) has
sliced primitive highest coefficient: \(\Delta b=x^2\) is
constant in \(\lambda\), and Section 2 rules out degree zero,
so its nonzero top is always a polynomial multiple of
\(\partial_c\).

## 5. A minimizer outside every old normalizer reduction

The following instance of (16)-(17) moves \(w\) even on the
exceptional divisor:
\[
J=\lambda-2x\lambda^2,\qquad A=C=0,
\]
\[
K=\lambda^2b^2-6\lambda^3b-4x\lambda^4b.
\tag{19}
\]
Indeed
\(v^2J=\lambda-3x^2\lambda^3-2x^3\lambda^4\).
The inverse is exactly (14), and its horizontal is
\[
\delta\lambda=1,\quad\delta x=0,\quad
\delta w=1-4x\lambda,
\]
\[
\delta z=
  2\lambda(w-J)^2-18\lambda^2(w-J)
                    -16x\lambda^3(w-J).
\tag{20}
\]
Both expressions in (13) are annihilated by (20), so local
nilpotence is established by the polynomial inverse, not just
by observing the slice. Formula (18) becomes
\[
\Delta b=x^2,\qquad
\Delta c=2b+\lambda(4xb+2).
\tag{21}
\]

The actual fixed-locus ideal of \(\Delta\) has radical
\((x,w)\), as proved directly in pass 30. Here
\(\delta w\equiv1\pmod x\), so this horizontal is not tangent
to that locus. Every \(F\)-fixing horizontal is tangent to it.
Tangency is unchanged by any automorphism fixing \(x,\lambda\)
and conjugating \(\Delta\) to a nonzero constant multiple of
itself. Therefore (20) cannot be brought into the pass-29
\(F\)-fixing sector by any such canonical normalizing gauge.

This shows why the new minimum cannot be explained by silently
reducing the enlarged family to the previously classified one.
It is not an obstruction to an unrestricted gauge that also
changes the vertical action.

## 6. The remaining minimum-selection gap

Equation (11) is a statement about all supplied horizontals in
(2). The sliced-top classification in Section 4 is only a
statement about (12). These quantifiers must not be combined
into an unproved universal sliced-top assertion.

For a general degree-one pair in (3), one has
\(\Delta=D_0+\lambda D_1\), with \(D_1\) an actual LND.
The primitive part need not be treated as sliced merely because
the original action has principal plinth. A sufficient condition
would be a relative coordinate frame
\(\ker\delta=\mathbb C[x,b,c]\) having \(\Delta b=x^2\):
then \(D_1b=0\), and the companion coordinate \(c\) gives
the argument from (15).
The triangular sector has exactly this additional coordinate.
Its existence for every minimizer in (2) has not been established.

Nothing here selects a horizontal action on an unknown polynomial
cylinder or proves cancellation. The canonical input already has
rank two and an established parameter-preserving polynomial frame.
No novelty, expert review, or proof-assistant verification is claimed.

## Verification and attribution

The standalone checker uses only unittest and SymPy. It tests
the actual canonical action, both polynomial coordinate inverses,
the exact degree-one coefficients, the parity and degree negative
controls, and coefficient recovery in the full triangular family.
The universal zero-degree exclusion and the all-parameter
classification are the written proofs, not finite extrapolations.

~~~sh
/opt/anaconda3/bin/python research/minimal_horizontal_checks_pass31.py
~~~

The initial completed checker run passed all ten methods in 0.724
seconds. An independent agent reconstructed the complete triangular
coefficient criterion and the nontangent example without finding a
correction; the parent independently reconstructed the full-sector
zero-degree contradiction. The first note save had inline-TeX escaping
damage, which was corrected before this handoff without changing a
mathematical formula.

The model and primitive-top convention are inherited from
[pass 28](canonical-top-pass28.md), the elementary planar degree
gate from [pass 29](horizontal-selection-pass29.md), and the
normalized slice-coordinate and fixed-locus arguments from
[pass 30](horizontal-gauge-pass30.md). No external structural
theorem is invoked for the new minimum or triangular criterion.
