# Primitive Euler transversality excludes a divisor obstruction

In the actual independent degree-two frame, a divisor transverse
to the primitive Euler direction has no poles in the generic
quadratic or linear graph coefficients. The whole localized
four-ring is then the polynomial ring in the two actual bad
coordinates, and the supplied slice gives an actual affine slice.

Consequently every genuine primitive plinth divisor, and every
common divisor of the two bad speeds, must have constant reduced
projective bad-speed direction. The statement is at a height-one
DVR, not a claim about simultaneous closed-point gluing.

Normalized tangency is a real remaining case. A polynomial
rank-two homogeneous base example below has a ramified algebraic
speed field and a Hessian pole at such a tangent divisor. It is
not an actual full-frame example.

## 1. The actual graph and its Euler weights

Retain the complete supplied independent-defect degree-two frame
of [the actual generic graph theorem](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad Es_*=1,
\]
\[
C=\ker D=\mathbb C[a,b],\quad L=\operatorname{Frac}C,\quad
B_L=L[x_3,x_4],\quad
E=f\partial_{x_3}+g\partial_{x_4}.
\tag{1}
\]
Here \(D\) is the actual primitive intrinsic LND, the speeds
\(f,g\in C\) are algebraically independent, and \(a,b\) are
coordinates of the invariant plane, not ambient coordinates
or the two bad speeds. The full plinth is \(pC\).

The field \(L\) is finite separable over \(\mathbb C(f,g)\).
The commuting field partials \(\partial_f,\partial_g\) extend
uniquely to \(L\). Write
\[
\mathscr H=f\partial_f+g\partial_g.
\tag{2}
\]
The good-partial Schur calculation in pass44 gives actual
accelerations \(h_i=E^2x_i\in C\), elements \(k_i,\ell_i\in L\),
and
\[
\mathscr H h_i=2h_i,\qquad \mathscr H k_i=k_i,
\]
\[
x_i=\frac14
\begin{pmatrix}x_3&x_4\end{pmatrix}
\operatorname{Hess}_{f,g}(h_i)
\binom{x_3}{x_4}
+(\nabla_{f,g}k_i)\binom{x_3}{x_4}+\ell_i,
\qquad i=1,2.
\tag{3}
\]
These are the complete quadratic and linear coefficient
identities, not just the equations \(E^2x_i=h_i\).
Their source uses the true good coordinate partials, their
adjoint bounds, and the rank assumptions of the actual frame.

The commutator formulas
\[
[\mathscr H,\partial_f]=-\partial_f,\qquad
[\mathscr H,\partial_g]=-\partial_g
\tag{4}
\]
hold on \(L\): they hold on \(f,g\), and a derivation on
a separable algebraic field extension is determined by its
restriction to the base field. Applying (4) to (3) shows
\[
\mathscr H(\partial_r\partial_s h_i)=0,\qquad
\mathscr H(\partial_r k_i)=0
\quad(r,s\in\{f,g\}).
\tag{5}
\]
Thus every quadratic and linear graph coefficient is an
Euler-invariant rational function. No such weight condition
is asserted for the constant \(\ell_i\).

## 2. Normalize the Euler field at one prime

Fix an irreducible \(\pi\in C\), and set
\[
R=C_{(\pi)},\quad \kappa=\operatorname{Frac}(C/\pi C),
\quad \mathcal B=B_R,\quad\mathcal A=A_R.
\]
Use the valuation \(\nu=\nu_\pi\), with \(\nu(0)=+\infty\),
and put
\[
m=\min\{\nu(\mathscr H a),\nu(\mathscr H b)\}\in\mathbb Z,
\qquad
\mathscr H_0=\pi^{-m}\mathscr H.
\tag{6}
\]
The integer is finite because \(\mathscr H\ne0\).
In the actual invariant coordinates,
\[
\mathscr H_0
=(\pi^{-m}\mathscr H a)\partial_a
 +(\pi^{-m}\mathscr H b)\partial_b.
\]
Both coefficients belong to \(R\), and at least one is a
unit. The coordinate derivations \(\partial_a,\partial_b\)
preserve \(R\): differentiating a fraction with denominator
outside \((\pi)\) leaves its denominator a unit of the DVR.
Therefore
\[
\mathscr H_0(R)\subseteq R.
\tag{7}
\]
This is a regular primitive derivation of the DVR induced
by the rational Euler field. The normalization is not a
rescaling of the original LND \(E\) or of the intrinsic \(D\).

We say it is transverse at \(\pi\) when
\[
\mathscr H_0(\pi)\in R^*.
\tag{8}
\]
Equivalently,
\[
\nu(\mathscr H\pi)=m,\qquad
\nu(\mathscr H\pi/\pi)=m-1.
\tag{9}
\]
The criterion is unchanged by replacing \(\pi\) with an
associate or by an invertible change of invariant
coordinates. If (8) fails, (7) gives
\(\mathscr H_0(\pi)\in\pi R\), so the normalized field
is tangent to the divisor.

## 3. The signed-valuation lemma

Assume (8). If \(0\ne c\in L\) and \(\mathscr Hc=0\),
write \(c=\pi^n u\), with \(n\in\mathbb Z\) and \(u\in R^*\).
Because \(\mathscr H_0c=0\), differentiation in the fraction
field gives
\[
0=n u\,\mathscr H_0\pi+\pi\,\mathscr H_0u.
\tag{10}
\]
This formula is valid for every integer \(n\), including
negative valuations. Its two terms belong to \(R\).
If \(n\ne0\), reduction modulo \(\pi\) gives a product
of three nonzero elements: the characteristic-zero integer
\(n\), the residue of \(u\), and the residue of
\(\mathscr H_0\pi\). This is impossible. Consequently
\[
0\ne c\in\ker_L\mathscr H
\quad\Longrightarrow\quad \nu(c)=0.
\tag{11}
\]
In particular no nonzero invariant rational coefficient
can have a pole or a zero at a transverse prime.

## 4. Actual coefficient regularity and the whole local ring

Apply (11) to (5). Every entry of the two Hessians and
the two gradients in (3) belongs to \(R\); a zero entry
causes no exception. Subtract their quadratic and linear
terms from the actual element \(x_i\in\mathcal B\).
The remainder is \(\ell_i\in\mathcal B\cap L=R\).
Thus all coefficients in the two actual graph polynomials
belong to \(R\).

The original four coordinates generate \(\mathcal B\)
over \(R\). Equation (3) now proves the full ring equality
\[
\boxed{\mathcal B=R[x_3,x_4].}
\tag{12}
\]
The argument uses the actual constant-field intersection
and the original generators, not just a rational
parametrization or regularity of selected coefficients.

On this polynomial ring, every \(E\)-derivative belongs
to \((f,g)R[x_3,x_4]\). Since \(Es_*=1\), faithful ideal
contraction for the polynomial extension gives
\[
(f,g)R=R.
\tag{13}
\]
Choose \(\alpha,\beta\in R\) with \(\alpha f+\beta g=1\).
Then
\[
\sigma=\alpha x_3+\beta x_4,\qquad
j=gx_3-fx_4
\]
have the inverse formulas
\[
x_3=f\sigma+\beta j,\qquad
x_4=g\sigma-\alpha j.
\tag{14}
\]
Therefore
\[
\mathcal B=R[\sigma,j],\quad E\sigma=1,\quad
\mathcal A=R[j].
\tag{15}
\]
This is an actual affine generic slice and a polynomial
local intrinsic ring. It is not a global recognition claim.

The original primitive \(D\) restricts to a nonzero
\(R\)-linear LND on \(R[j]\), hence \(D=c\partial_j\)
with \(0\ne c\in R\). If \(\pi\mid c\), every value of
\(D\) on a finite set of actual generators of \(A\) is
divisible by \(\pi\) after localization. Invariant
denominators outside \((\pi)\) are not divisible by \(\pi\)
in the factorial actual ring, so clearing them makes
\(\pi\) a common divisor of those values in \(A\).
This contradicts primitivity. Thus \(c\) is a unit in \(R\).

Invariant localization commutes with the full plinth:
a local preimage is a fraction with invariant denominator,
and clearing that denominator gives a global plinth value.
It follows from (15) and the unit \(c\) that
\[
pR=R.
\tag{16}
\]
This last conclusion uses the actual primitive \(D\),
not a freely chosen replica of a derivation on \(R[j]\).

Combining (8)--(16), a genuine plinth prime, or a prime
dividing both bad speeds, cannot be transverse to
\(\mathscr H_0\).

## 5. The reduced projective bad-speed direction is constant

Suppose \(\mathscr H_0\) is tangent at \(\pi\).
It induces a derivation \(\overline{\mathscr H}_0\) of
\(\kappa=R/\pi R\). This derivation is nonzero: if it
vanished, both \(\mathscr H_0a\) and
\(\mathscr H_0b\) would lie in \(\pi R\), contradicting
the normalization in (6).

After swapping \(f,g\) if necessary, assume
\(\nu(f)\le\nu(g)\). Then
\[
\varphi=g/f\in R,\qquad \mathscr H_0\varphi=0.
\]
If its residue \(\bar\varphi\in\kappa\) were nonconstant
over \(\mathbb C\), the one-variable function field
\(\kappa\) would be finite separable over
\(\mathbb C(\bar\varphi)\). A derivation killing that
base field must vanish on its separable algebraic
extension, contrary to the preceding paragraph.
Hence
\[
\bar\varphi\in\mathbb C.
\tag{17}
\]
No rational-curve parametrization theorem is needed.

If \(n=\min\{\nu(f),\nu(g)\}\), the pair
\((\pi^{-n}f,\pi^{-n}g)\) has at least one unit entry
in \(R\). Equation (17) says that its projective residue
is one constant point of \(\mathbb P^1(\mathbb C)\).
Thus
\[
\boxed{
\pi\mid p\ \hbox{or}\ \pi\mid\gcd(f,g)
\quad\Longrightarrow\quad
\text{the reduced primitive bad-speed direction at }\pi
\text{ is constant}.}
\tag{18}
\]
Equivalently, a nonconstant projective residue forces
transversality and the conclusions (12)--(16).
Constant projective residue is only a necessary condition
for a surviving divisor, not a sufficient construction.

## 6. A tangent ramified base control

The tangent case cannot be removed just by assuming
polynomial homogeneous accelerations of rank two.
On \(C=\mathbb C[a,b]\), take
\[
f=a,\qquad g=a+a^3b^2,\qquad
\mathscr H=a\partial_a-b\partial_b,
\]
\[
h_1=a^2,\qquad h_2=a^3b,\qquad k_1=k_2=0.
\tag{19}
\]
The speeds are algebraically independent; their Jacobian
determinant in \(a,b\) is \(2a^3b\ne0\). Directly,
\[
\mathscr Hf=f,\quad\mathscr Hg=g,\quad
\mathscr Hh_i=2h_i,\quad
\det\operatorname{Jac}_{a,b}(h_1,h_2)=2a^4\ne0.
\tag{20}
\]
Thus the Euler field is exactly the unique field
derivation (2) for these speeds.

At \(\pi=a\), the coefficient \(-b\) is a DVR unit,
so \(m=0\) and \(\mathscr H_0=\mathscr H\) is tangent.
The primitive projective ratio satisfies
\[
g/f=1+a^2b^2\equiv1\pmod a.
\]
Nevertheless the actual extended field derivative is
\[
\partial_g=\frac1{2a^3b}\partial_b
\quad\hbox{with }f=a\text{ fixed},
\]
and
\[
\partial_g h_2=\frac1{2b},\qquad
\partial_g^2h_2=-\frac1{4a^3b^3}.
\tag{21}
\]
The last coefficient has a third-order pole at \(a\).
It is Euler invariant, consistent with (5), because
the normalized Euler direction is tangent, not transverse.

Here \(L=\mathbb C(a,b)\) is a quadratic extension of
\(\mathbb C(f,g)\), since \((ab)^2=g/f-1\).
The pole therefore involves an allowed algebraic
ramification in the speed field. The zero choices
of \(k_i\) satisfy their weight-one equations, but
no full Schur complement, actual graph ring, supplied
slice, or ambient adjoint frame is claimed for (19).
This is only a control of the Euler/rank hypotheses.

## 7. Scope and deduplication

Pass44 supplies the complete graph, Euler, and gradient
identities; they are not reproved as a new classification.
Pass49 already selects affine slices when a bad speed
or an acceleration is a unit. The added criterion here
forces coefficient regularity and that unit alternative
from primitive Euler transversality.

For the faithful control of pass57 at \(\pi=a\), its
speed field has \(\mathscr H=a\partial_a\) with the ratio
variable held fixed. Normalization gives
\(\mathscr H_0=\partial_a\), which is transverse.
This does not contradict the control: its quadratic
generators fail the full actual graph identities used
in (3), as already exposed in pass58.

The conclusion is local at a single invariant divisor.
It does not patch centers, classify tangent divisors,
settle closed-point affine-slice ideals, or prove a
universal frame bound. No new standalone numerical
suite is required for the valuation argument.

