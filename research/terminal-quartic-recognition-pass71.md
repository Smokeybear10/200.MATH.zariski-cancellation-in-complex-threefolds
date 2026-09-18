# Original-kernel recognition for the terminal dependent moving quartic

The terminal quartic symmetry can be reduced to two output directions
by an actual polynomial coordinate change. A linear invariant of its
global nice replica first forces proportional original speed along
the surviving coordinate. Comparing coefficients over the original
constant field then supplies the needed shear. In the branch where
the shear mixes a bad direction with a good one, their second
adjoints cancel exactly.

This completes the terminal case under its supplied-frame hypotheses.
It does not establish that arbitrary sliced actions admit that frame,
recognize the independent moving quartic or quintic cases, or solve
unrestricted complex-threefold cancellation.

## 1. Exact original-ring hypotheses

Let
\[
B=k[a,b,z,w],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad E(s_*)=1,
\qquad 0\ne g\in\ker E.
\tag{1}
\]
All four displayed generators are actual polynomial coordinates.
Write \(\delta=E/g\) on \(\operatorname{Frac}B\), and suppose
there are rational functions \(\beta,\kappa\) such that
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a,
\qquad Sg=S\beta=S\kappa=Sw=0,
\]
\[
[\delta,S]=0,\qquad
\delta\beta=\frac12,\qquad
\delta\kappa=\frac\beta3,\qquad E^2w=0.
\tag{2}
\]
Assume that the cleared coefficients
\[
N=g\beta\in B,\qquad U=3g\kappa\in B
\tag{3}
\]
are actual polynomials. Finally put
\(W_a=[E,\partial_a]\) and \(V_b=\operatorname{ad}_E^2\partial_b\),
and assume the actual coordinate-partial identities
\[
\operatorname{ad}_E^2\partial_a=0,\qquad
gW_a=-\frac32 V_b.
\tag{4}
\]
The theorem allows \(V_b=0\), although it is nonzero in the
terminal quartic application.

**Theorem.** Under (1)--(4), \(E\) fixes an actual ambient
coordinate of \(B\), and
\[
\boxed{\ker E\simeq\mathbb C^{[3]}.}
\tag{5}
\]
The [parabolic terminal form](terminal-quartic-parabolic-form-pass71.md)
proves all these hypotheses for the residual dependent moving
quartic. Its equations (13), (16), and (21) give (3)--(4).
Its polynomial coordinate changes leave the original derivation
and original slice unchanged. The theorem does not assume its
changed coordinate profile still has two quadratic bad directions.

## 2. A polynomial coefficient relation and proportional speed

Equations (2)--(3) give the actual polynomial nice derivation
\[
T=gS=\frac U3\partial_a+N\partial_b+g\partial_z,
\quad Tg=TN=TU=Tw=0,
\]
\[
Eg=0,\qquad EN=\frac{g^2}{2},\qquad EU=gN.
\tag{6}
\]
It is locally nilpotent because its polynomial coefficients are
fixed by it, and it is nonzero because \(Tz=g\ne0\).
Only \(T\), not \(E\), is extended as a \(k(w)\)-linear
derivation of \(k(w)[a,b,z]\).

The established three-variable nice-derivation linear-invariant
theorem supplies, after clearing denominators, a relation
\[
A(w)U+B_0(w)N+C(w)g=0,
\quad A,B_0,C\in k[W],\quad(A,B_0,C)\ne(0,0,0).
\tag{7}
\]
Here \(B_0\) denotes a polynomial coefficient, not the ring \(B\).
The precise source is Wang's result as stated in Dasgupta--Gupta,
Theorem 3.1(i), for every characteristic-zero field.[^nice]
There is no irreducibility premise in the part used here.

Set \(p=Ew\), so \(Ep=0\). The full
[weighted-leading-coefficient lemma](nice-chain-speed-proportionality-pass71.md)
applies to (6)--(7). It proves
\[
p=0\quad\hbox{or}\quad p=\lambda g
\quad\text{with }\lambda\in k^*.
\tag{8}
\]
In brief, the top coefficient after applying \(\exp(tE)\)
to (7) is a nonzero homogeneous complex quadratic relation in
\(g,p\). Thus \(p/g\) is algebraic over the algebraically
closed field \(k\). The linked lemma supplies the complete
argument, including zero coefficients and weighted degrees zero
and one.

If \(p=0\), \(w\) is already an invariant ambient coordinate.
The original slice gives \(B=(\ker E)[s_*]\), so \(\ker E\)
is regular. The inherited invariant-coordinate regular-kernel
theorem proves (5).[^regular]

For the rest of the proof assume \(p=\lambda g\ne0\). Then
\(\delta w=\lambda\). This is not an original coordinate
slice: \(E(w/\lambda)=g\), which need not be one.

## 3. Coefficient comparison over the constant field

Define
\[
h=3\kappa-\beta^2,\qquad f=\frac{w}{2\lambda},
\qquad u=\beta-f.
\tag{9}
\]
Equations (2) and (8) imply
\[
\delta h=Sh=0,\qquad \delta u=Su=0,\qquad Sf=0.
\tag{10}
\]
Let \(F\) be the constant field of \(\delta\) on
\(\operatorname{Frac}B\). The coordinate \(w\) is
transcendental over \(F\). Indeed, a minimal polynomial over
\(F\), if one existed, would after differentiation give
\(\lambda P'(w)=0\). In characteristic zero a minimal
polynomial is separable, contradicting \(\lambda\ne0\).

Dividing (7) by \(g\) and substituting (9) yields
\[
A(w)(\beta^2+h)+B_0(w)\beta+C(w)=0,
\]
\[
A(w)(u^2+h)+(2A(w)f+B_0(w))u
 +A(w)f^2+B_0(w)f+C(w)=0.
\tag{11}
\]
This is a polynomial identity in the transcendental element
\(w\) over \(F\), since \(u,h\in F\) and
\(f=w/(2\lambda)\). Its coefficients can therefore be
compared individually. This comparison occurs in a field, but
the coordinate changes produced below have polynomial
coefficients over \(k\).

## 4. The branch with a nonzero quadratic coefficient

Assume \(A\ne0\). Choose any coefficient \(A_j\ne0\)
of \(W^j\) in \(A(W)\). Comparing that coefficient in
(11) and dividing by the nonzero complex number \(A_j\)
gives complex constants \(\alpha,\gamma\) with
\[
u^2+h=\alpha u+\gamma.
\tag{12}
\]
This does not assert that \(u\), or \(h\), is constant.
It gives precisely the following linear expression in \(\beta\):
\[
\kappa=L(w)\beta+R(w),\qquad
L=\frac{2f+\alpha}{3},\qquad
R=\frac{-f^2-\alpha f+\gamma}{3}.
\tag{13}
\]
Both \(L,R\) are polynomials in \(w\) over \(k\).

Make the actual polynomial coordinate change
\[
b'=b-fz,\qquad a'=a-Lb-Rz,\qquad z'=z,\qquad w'=w.
\tag{14}
\]
Its explicit polynomial inverse is
\[
b=b'+fz',\qquad
a=a'+Lb'+(Lf+R)z',\qquad z=z',\qquad w=w'.
\tag{15}
\]
Here the coefficient polynomials are evaluated at the unchanged
coordinate \(w'=w\). There is no division by a nonconstant
polynomial in this coordinate change.

Since \(Sw=0\), equations (9), (13), and (14) give
\[
Sa'=0,\quad Sb'=u,\quad Sz'=1,\quad Sw'=0,
\qquad S=\partial_{z'}+u\partial_{b'}.
\tag{16}
\]
The coefficient obeys \(Su=\delta u=0\).
The genuine new partial, as computed from the inverse, is
\[
\partial_{b'}=\partial_b+L\partial_a,
\qquad EL=\frac g3,\qquad E^2L=0.
\tag{17}
\]
The adjoint product rule and (4) now give
\[
\begin{aligned}
\operatorname{ad}_E^2\partial_{b'}
 &=V_b+(E^2L)\partial_a
       +2(EL)W_a+L\operatorname{ad}_E^2\partial_a\\
 &=V_b+\frac{2g}{3}W_a=0.
\end{aligned}
\tag{18}
\]
This equality creates a good actual partial; it is not a
claim that a rationally rescaled vector is a coordinate partial.

Apply the [rational two-direction recognition theorem](rational-two-direction-recognition-pass69.md)
with fixed base coordinates \((a',w')\), good output coordinate
\(b'\), translation coordinate \(z'\), and rational coefficient
\(u\). Its constant coefficient derivative is zero. Its
commutation assumption remains \([\delta,S]=0\), and it
uses the same original polynomial slice \(s_*\).
Equations (1), (10), and (16)--(18) verify every remaining
hypothesis. It supplies an invariant ambient coordinate and (5).

## 5. The branch with no quadratic coefficient

Assume \(A=0\). Then \(B_0\ne0\), since otherwise (7)
would imply \(C(w)g=0\) with \(C\ne0\). Equation (11)
gives \(\beta=-C(w)/B_0(w)\in k(w)\).
The restriction of \(\delta\) to \(k(w)\) is
\(\lambda\,d/dw\). Since \(\delta\beta=1/2\), the
constant field of ordinary differentiation on \(k(w)\) gives
\[
\beta=f+u_0,\qquad u_0\in k.
\tag{19}
\]
In particular \(\beta\) is a polynomial in the actual
coordinate \(w\), despite its initially rational expression.

Put
\[
P(w)=\frac{w^2}{12\lambda^2}+\frac{u_0w}{3\lambda},
\qquad \chi=\kappa-P(w).
\tag{20}
\]
Then \(\delta P=\beta/3\), while \(SP=0\), so
\(\delta\chi=S\chi=0\).
Make the actual polynomial shears
\[
b'=b-\beta(w)z,\qquad a'=a-P(w)z,
\qquad z'=z,\qquad w'=w.
\tag{21}
\]
The inverse adds the same corrections, with \(w,z\)
unchanged. Direct evaluation gives
\[
Sb'=0,\quad Sa'=\chi,\quad Sz'=1,\quad Sw'=0,
\qquad S=\partial_{z'}+\chi\partial_{a'},
\quad\partial_{a'}=\partial_a.
\tag{22}
\]
The last partial is genuine and good by (4). The two-direction
theorem applies with fixed base \((b',w')\), good output
\(a'\), translation coordinate \(z'\), and rational
coefficient \(\chi\), again with constant derivative zero.
The original slice, invariant nonzero \(g\), and commutation
are unchanged. This proves (5) in the remaining branch.

## 6. Scope of the endpoint

The branches exhaust any nonzero relation (7). They require
only the linear-invariant part of the nice-derivation theorem,
not its rank-one normal form or a relative polynomial-kernel
conclusion. No global slice for \(T\) or \(S\) is used.
In the nonzero-speed case the only scalar divisions in the
actual shears are by nonzero complex constants.

The terminal quartic inputs come from the original supplied
frame, but its transformed profile is allowed to change.
The required single good output is checked anew in (18) or
(22). Thus the argument never reapplies the original
two-quadratic-frame theorem to a frame that no longer has
those bounds.

This is a complete written conditional deduction using the
linked proof chain and established source gates. Review and
exact-control outcomes must be recorded separately after they
occur. No human review, formal proof-assistant verification,
historical novelty, unrestricted cancellation, or professor
confirmation is asserted.

## Sources

[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), arXiv:1701.03635v1, January 13, 2017, Theorem 3.1(i), PDF p. 5. The statement over every characteristic-zero field is read directly; it is attributed there to Z. Wang, Proposition 4.6. The original Wang article's complete proof has not been freshly accessed. The [leading-speed lemma](nice-chain-speed-proportionality-pass71.md) records the exact source qualification.

[^regular]: S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. This endpoint uses its invariant-coordinate and regular-original-kernel case, with the inherited source audit documented in [the one-good-output recognition lemma](three-output-cubic-closure-pass41.md), Section 1. The original slice provides regularity. No fresh full historical-proof reconstruction is claimed here.
