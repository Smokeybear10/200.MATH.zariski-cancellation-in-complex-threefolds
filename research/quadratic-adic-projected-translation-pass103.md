# The projected bad partial is a translation on every finite base thickening

In the collapsed quadratic fibers covered by102, the zeroth
u-coefficient of the original bad partial induces a locally
nilpotent derivation on every finite base-adic neighborhood of
the intrinsic fiber. It has a compatible slice there. This is
an actual lift beyond the whole fiber, not an assumption that
the zeroth coefficient of a locally nilpotent derivation is
globally locally nilpotent.

The resulting invariant rings and translations are compatible
under reduction. Their inverse limit must not be replaced by
an ordinary polynomial ring over the inverse limit of the
invariants. No uniform nilpotence exponent or global recognition
is supplied.

## 1. The actual ideal and the projected derivation

Retain the whole collapsed double or mixed (2,1) setting with
L(m) nonzero from
[degree-module rigidity102](quadratic-degree-module-fiber-rigidity-pass102.md).
Let T be the actual original coordinate partial in z. Write
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\qquad E=\partial_u,
\quad Ez=q_0u,\quad q_0\in\mathbb C^*,\\
J=\mathfrak mA,\qquad I=\mathfrak mB=JB,
\qquad T(I)\subseteq I,\qquad Tu\in I,\\
\pi_u:B\longrightarrow A,\qquad \pi_u(u)=0,
\qquad D_0=\pi_u\circ T|_A,\\
\boxed{\quad D_0(J^j)\subseteq J^j\quad(j\ge0).\quad}
\end{gathered}
\tag{1}
\]
Here J denotes the whole fiber ideal in A, not the second-image
ideal from the earlier filtration program. The original partial
preserves I because
[whole-plane-fiber99](quadratic-whole-plane-fiber-pass99.md)
gives I=(ell,H(Y)) with both generators independent of z.
The additional membership Tu in I is the whole-fiber conclusion102.
It is not asserted that T kills u in B.

The map D0 is a complex derivation of A, since pi_u is an
algebra homomorphism fixing A. Preservation of I implies
preservation of every power I to the j by the Leibniz rule.
For a in J to the j, its image Ta is therefore in J to the j
times B. The coefficients of a polynomial in u belonging to
that extended ideal all lie in J to the j. In particular its
constant coefficient D0a does. This proves (1), without an
assertion that T preserves S or A themselves.

## 2. The graded derivation is genuinely locally nilpotent

The polynomial extension gives an exact graded-ring identification,
with u in degree zero:
\[
\begin{gathered}
\operatorname{gr}_I B\simeq(\operatorname{gr}_J A)[u],\\
\operatorname{gr}_I T\text{ is a locally nilpotent derivation},
\qquad (\operatorname{gr}_I T)(u)=0,\\
\boxed{\quad
\operatorname{gr}_J D_0
\text{ is the induced locally nilpotent derivation on }
(\operatorname{gr}_I B)/(u).
\quad}
\end{gathered}
\tag{2}
\]
T preserves the filtration, so it induces a degree-zero
derivation. Given any homogeneous class, choose an actual
representative in B. A sufficiently high T-iterate of that
representative is zero because T is an original coordinate
partial. Its graded iterate is then zero too. A general graded
element is a finite sum of homogeneous classes, so taking the
maximum of the finitely many exponents proves local nilpotence
on the full graded ring.

The middle assertion uses Tu in I: the image of Tu in degree
zero is zero. Consequently the ideal (u) in the graded ring is
stable, and its quotient inherits an LND. On a class represented
by a in J to the j, this quotient sends the class to the
constant u-coefficient of Ta modulo J to the j+1. That is
exactly the class of D0a. This proves the final identification.
No claim that the ideal (u) is T-stable in the original B is
needed or made.

## 3. Finite filtration gives an LND on every neighborhood

For an integer k at least one, let
\[
\begin{gathered}
\mathcal A_k=A/J^k,\qquad
D_k\text{ is the derivation induced by }D_0,\\
\boxed{\quad D_k\text{ is locally nilpotent for every }k.\quad}
\end{gathered}
\tag{3}
\]
Start with any element of A and its degree-zero J-adic class.
By (2), some D0-iterate lies in J. Apply (2) to the degree-one
class of that new element to make a further iterate lie in J
squared. Continue through the finitely many degrees below k.
The sum of the chosen exponents puts the original element in
J to the k. This proves (3) for every element of A_k.

The exponents may depend on the element and on k. No single
exponent valid for all k follows, and local nilpotence is not
being asserted for the completed derivation.

The exact global slice for D0 is the centered original bad
coordinate, denoted r rather than the specified relative
generator c:
\[
\begin{gathered}
r=z-\frac{q_0}{2}u^2\in A,\qquad
\boxed{\quad D_0r=\pi_u(1-q_0uTu)=1.\quad}\\
r_k=r\bmod J^k,\qquad D_kr_k=1.
\end{gathered}
\tag{4}
\]
This is the global coefficient identity already present in
[three-good-frame87](constant-acceleration-three-good-frame-pass87.md),
now combined with (3). The specified c satisfies
c=r+q0 h squared/2 and need not be a slice for D0 globally.
Write \(\mathcal D=\mathbb C[G]/(H(G))\) for the whole
Artin coefficient ring from102, so \(A/J=\mathcal D[c]\).
Modulo J the exact relation is r=c-q0 hbar squared/2, with
\(\bar h\in\mathcal D\). Its shift can have a nonzero nilpotent part.
It still gives \(\mathcal D[c]=\mathcal D[r]\); replacing
that shift by its reduced component values would discard information.

## 4. Compatible slices and surjective invariant transitions

Put C_k=ker D_k. For each a in A_k define the finite slice
projection and reconstruction by
\[
\begin{gathered}
P_k(a)=\sum_{j\ge0}\frac{(-r_k)^j}{j!}D_k^j(a)\in C_k,
\qquad P_k|_{C_k}=\mathrm{id},\qquad P_k(r_k)=0,\\
a=\sum_{j\ge0}\frac{r_k^j}{j!}P_k(D_k^j a),\qquad
\boxed{\quad \mathcal A_k=C_k[r_k]\simeq C_k[t].\quad}
\end{gathered}
\tag{5}
\]
Both sums are finite by (3). Differentiating the first one
cancels consecutive terms and proves invariance. Expanding
the second and collecting binomial coefficients gives the
reconstruction. Uniqueness follows by applying D_k to the
highest power of r_k in a hypothetical polynomial relation:
its leading coefficient is multiplied by a nonzero factorial.
This is valid in the possibly nonreduced ring C_k because
the complex factorials are units. Thus (5) is a ring
isomorphism, not merely a spanning assertion.

The quotient maps A_(k+1) to A_k commute with the derivations,
the slices, and the finite projections P_k. Given an invariant
b in C_k, lift it to any a in A_(k+1). The invariant
P_(k+1)(a) maps to P_k(b)=b. Consequently every transition
C_(k+1) to C_k is surjective, and the polynomial presentations
in (5) are compatible with these maps and t mapping to t.

In particular there are compatible actual complex additive-group
actions on all the finite neighborhoods, and compatible slice
projections onto their own invariant rings. They are not
asserted to be actions over \(S/\mathfrak m^k\): D0 has not been
proved to annihilate S. Nothing here identifies C_k with that
specified base quotient.

Let Ahat be the J-adic completion and Dhat the continuous
derivation induced by D0. The precise inverse-limit statement is
\[
\begin{gathered}
\widehat A=\varprojlim_k\mathcal A_k
\simeq\varprojlim_k C_k[t],\qquad
\ker\widehat D=\varprojlim_k C_k,\\
\widehat D\text{ induces an LND on each finite quotient,}
\quad\text{not necessarily on }\widehat A.
\end{gathered}
\tag{6}
\]
The kernel equality is componentwise. The first limit in (6)
must not be rewritten as (limit C_k)[t] without an additional
bound on polynomial degrees. Such degrees can grow with k.
Likewise the compatible finite exponential maps need not give
an ordinary algebraic additive-group action on Spec Ahat with
values in Ahat[t]. These distinctions are relevant to any
attempt at global recognition.

## 5. An exact boundary to global or completed local nilpotence

There is an elementary polynomial control for this last gap:
\[
\begin{gathered}
R_0=\mathbb C[x,c],\qquad J_0=(x),\qquad
D=\partial_c+x^2\partial_x,\qquad Dc=1,\\
D^n x=n!x^{n+1}\ne0\quad(n\ge0),\qquad
D\text{ is LND on every }R_0/(x^k).
\end{gathered}
\tag{7}
\]
The iterate formula follows by induction. On the finite quotient,
a sufficiently high iterate kills x and the second iterate
kills c; the Leibniz rule then kills each polynomial. Nevertheless
no iterate kills x in R0 or in its x-adic completion. This
separates exactly the finite statement (3) from the unjustified
global or completed statement.

The formal invariant y=x/(1+cx) can be expanded to any finite
x-adic order and is compatible with the finite slice projections.
The inverse x=y/(1-cy) gives a continuous formal change between
C[c][[x]] and C[c][[y]]. In the latter presentation D is partial c,
whose kernel is C[[y]]. But x is the series
sum over n at least zero of c to the n times y to the n+1.
Its c-degree is unbounded, so it does not lie in C[[y]][c].
This verifies the inverse-limit distinction in (6) within the
control itself, not merely by a possible-degree warning.

This two-variable control is not an original constant-acceleration
four-coordinate frame and does not realize an unresolved fixed
fiber. It only shows why compatible finite nilpotence and a
slice do not logically imply global or completed nilpotence.
An actual-frame countercontrol requires its own inverse and
hypothesis verification.

## Scope and proof dependencies

Geometry derived the graded projection and finite-filtration
argument from the actual102 ideal and commutation conclusion.
Root and Jet independently reconstructed those steps before
this note was saved. Root supplied the slice-projection and
inverse-limit refinement and the last intrinsic control.
The slice identities are proved above and use no classification
theorem. The original partial is locally nilpotent because it
is an actual coordinate partial, not because it is a coefficient
or a bracket of other locally nilpotent fields.

This proof gives all finite base-adic intrinsic translations in
the stated sector. It does not improve the order of [E,T] as a
derivation of B, make the original or projected actions globally
commute, produce a global intrinsic LND from D0, or recognize A.
All files through102 remain unchanged.
