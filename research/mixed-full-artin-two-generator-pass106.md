# The full Artin branch has a two-generator fourth-image defect

When the second-degree residue image is the full three-dimensional
Artin algebra, the remaining fourth-image obstruction has an exact
two-generator form. The third image is principal, but the fourth
image is its multiple by a proper complete-intersection ideal.
The degree-lowering operator relates these ideals and improves their
orders to three and four, respectively. These are necessary conditions
for the specified mixed fiber, not its exclusion.

## 1. Actual hypotheses and the new input

Use the actual collapsed mixed quadratic frame with nonzero speed
normal from [rank-defect105](mixed-cubic-rank-defect-pass105.md).
In particular, R=S_m is the regular local invariant plane,
with maximal ideal n and residue field C. The algebra A_R is
faithfully flat over R, and the full kernel of the locally nilpotent
derivation N is R. Write M_j=(ker N^(j+1))_R and I_j=N^j(M_j).
Each M_j is free of rank j+1. The whole fiber is
D[c], where D=C[G]/(G²(G−1)). Here impose the additional condition

\[
\mathcal W_2=\mathcal D,\qquad
\mathcal W_3=\mathcal D,\qquad
I_2\subseteq\mathfrak n^2,\qquad
I_4\text{ is not principal}.
\tag{1}
\]

The first equality is the branch under study, the second is105,
and the third is [Artin-image104, Section 5](mixed-degree-module-artin-image-pass104.md).
The final input is the separate
[nonprincipality theorem106](mixed-fourth-image-nonprincipal-pass106.md).
It uses the generalized projection boundary, not this argument.
In particular no circular inference from the following order bounds
is used to prove nonprincipality.

## 2. Two compatible free complements

Choose three actual elements of M_2 with independent whole-fiber
residues. They are an R-basis of M_2. Their classes remain independent
in M_j/nM_j for j=3,4: a dependence there would give a dependence
after mapping to the whole fiber. An independent set in the residue
of a finite free module over a local ring extends to a basis.
Consequently one can choose elements t,u,v with

\[
M_3=M_2\oplus Rt,\qquad
M_4=M_2\oplus Ru\oplus Rv,\qquad
t=a u+b v+H,\quad H\in M_2,\quad a,b\in R.
\tag{2}
\]

The choices of complements need not agree. The term H is retained
precisely for that reason. Since t has degree three on the generic
line, g=N³t is nonzero. Applying N³ to the first splitting gives
I_3=Rg. This does not imply that M_3 splits off M_4.

The quotient M_4/M_3 is I_4 under N⁴, hence torsion free.
After quotienting (2) by M_2, it is R²/R(a,b). Therefore a,b
have no nonunit common divisor. For if d divided both, the class
of (a/d,b/d) would be a nonzero torsion element killed by d.
It is nonzero because (a,b) is not the zero vector and R is a domain.
The ring R, being a localization of a polynomial plane, is a UFD.

Neither a nor b can be a unit. If one were a unit, R(a,b)
would split off R² and its quotient would be free of rank one.
Then I_4 would be a free rank-one ideal, thus principal, contrary
to (1). Coprimality also excludes either a or b being zero now.
It follows that

\[
J=(a,b)\subseteq\mathfrak n,\qquad
\gcd_R(a,b)=1,\qquad
\sqrt J=\mathfrak n,\qquad
a,b\text{ is a regular sequence}.
\tag{3}
\]

Indeed no height-one prime of the two-dimensional local UFD can
contain J; J is nonzero and proper, so its only containing prime
is n. Also a is a nonzerodivisor, and if bq belongs to (a),
coprimality makes a divide q. Thus b is a nonzerodivisor modulo a.
This directly proves the regular-sequence assertion. It agrees
with the standard Cohen--Macaulay dimension criterion.[^regular]
The ideal J need not equal n, nor need a,b be regular parameters.

## 3. The exact degree-lowering matrix

Since N(M_4) is contained in M_3, there are unique coefficients
sigma,tau in R and P,Q in M_2 such that
Nu=sigma t+P and Nv=tau t+Q. Differentiating the final relation
in (2), and using Nt and NH in M_2, gives a sigma+b tau=0.
Coprimality supplies theta in R with sigma=theta b and
tau=−theta a. Theta is nonzero, since otherwise N(M_4)
would be contained in M_2 and the generic fourth-degree part
would disappear. Thus

\[
\begin{gathered}
Nu=\theta b t+P,\qquad Nv=-\theta a t+Q,\qquad
\theta\in R\setminus\{0\},\quad P,Q\in M_2,\\
\overline N_{M_4/M_2}
=\theta\begin{pmatrix}ab&-a^2\\ b^2&-ab\end{pmatrix},
\qquad \overline N_{M_4/M_2}^{2}=0.
\end{gathered}
\tag{4}
\]

This is an induced R-linear operator on a quotient of degree
modules, not the derivation on A/nA. The quotient is N-stable
because M_2 is. Substituting (2) into the two derivatives gives
the displayed columns, including the cancellation of the H term
modulo M_2. Its entries lie in n², so there is also the actual
module containment N(M_4) contained in M_2+n²M_4.

## 4. The third and fourth image ideals are linked

Apply N³ to the first line of (4). Since N³P=N³Q=0,
one obtains N⁴u=theta b g and N⁴v=−theta a g. They generate
I_4, since N⁴ kills M_2. Next differentiate (2) once to get
Nt=aP+bQ+NH, and twice more. The retained H contributes N³H=0.
Therefore

\[
\boxed{\begin{gathered}
I_3=(g),\qquad
I_4=\theta g(a,b)=\theta gJ,\\
g=aN^2P+bN^2Q\in JI_2,\qquad
\mu_R(I_4)=2.
\end{gathered}}
\tag{5}
\]

All coefficients are in the actual local base ring. The formula
does not divide by theta, g, a or b in A_R. In particular theta
has not been assumed a unit. The number of generators is exactly
two because J is proper and coprime, so cannot be principal.
Multiplication by the nonzero element theta g preserves that
minimal number.

Every invariant height-one prime with constant-field degree one
has a polynomial local slice by105. There I_3 and I_4 both
localize to the unit ideal. Hence all irreducible factors of g
and theta, if present, lie on the degree-two constant-cover
curves. Conversely, [admissible-boundary106, equation (8)](mixed-admissible-quartic-boundary-pass106.md)
puts I_3 inside pR for every degree-two constant-cover divisor p.
Thus the reduced divisor support of g is exactly the union of those
degree-two divisor germs through m. No multiplicities are fixed.
This does not remove the residual ideal J, which becomes the unit
ideal at every height-one prime.

## 5. Stronger base orders and the actual selected generator

The relation g in JI_2, together with J in n and I_2 in n²,
has the exact consequences

\[
\boxed{\qquad I_3\subseteq\mathfrak n^3,
\qquad I_4\subseteq\mathfrak n^4,
\qquad N^4c\in\mathfrak n^4.\qquad}
\tag{6}
\]

The fourth-order inclusion follows from I_4=theta gJ and theta in R.
It is stronger than the order-three bound for the specified
N⁴c in104, and stronger than the first ideal-wide order-three
bound in nonprincipality106. These are containments, not equality
of orders or a vanishing theorem. For the original global element
N⁴c in S, contraction gives membership in m⁴S as well: S/m⁴
is local Artinian, so every denominator outside m is a unit there.

The complement can if desired be chosen with u=c. Indeed the
whole residue of c is independent of the three Artin basis
residues. Their classes in M_4/nM_4 therefore extend to a basis
containing c. With this choice (4)--(5) express the actual
selected derivative as N⁴c=theta b g, but b still lies in n
and is not asserted to be a coordinate or an irreducible element.

## 6. Multiplication imposes additional ideal constraints

For f,h in M_2, their product belongs to M_4. Leibniz's formula
leaves only the middle term after four differentiations, so
N⁴(fh)=6N²f N²h. For f in M_1 and h in M_3 the corresponding
identity is N⁴(fh)=4Nf N³h. Characteristic zero allows these
nonzero constants to be divided in R. Consequently

\[
\boxed{\qquad I_2^2\subseteq\theta gJ,
\qquad I_1I_3\subseteq I_4,
\qquad I_1\subseteq\theta J.\qquad}
\tag{7}
\]

The last inclusion cancels the nonzero principal generator g of
I_3 in the domain R. These are constraints from multiplication
in the actual algebra, beyond the free-module rank pattern.
They still do not imply J=R.

For example let k be the n-adic order of I_2, j the order of J,
and t0 the order of theta. Orders are finite since these objects
are nonzero. The associated graded ring of the regular local
plane is a polynomial domain, so the order of a product of
nonzero ideals is the sum of their orders. From g in JI_2 and
I_2² contained in theta gJ one obtains k at least t0+2j.
This is a necessary inequality, not a contradiction: k at least
two and j at least one remain compatible with t0 zero.

## 7. What this does not settle

Nonprincipal rank-one ideals are possible quotients of free
modules over a regular local surface. The exact pattern here
leaves a point-supported defect J even when every divisorial
localization is understood. Freeness of the M_j cannot erase it.
Nor does a fourth-order zero force a polynomial to vanish.

The new compatibility g in JI_2 is a sharper target for the next
argument. One would still need actual multiplication, divisor
orders, or original-coordinate geometry to prove that this
pattern cannot occur. No such exclusion is established here.
The two-dimensional W_2 branch does not inherit (2)--(7).
Whole-double fibers, zero speed normal and entry from an arbitrary
sliced action also remain outside this lemma.

## Sources

The mathematical inputs are the linked actual degree-module and
fiber proofs102,104,105, and the separate generalized boundary and
nonprincipality proofs106. All modules and ideals in (1)--(7)
are from that same actual local algebra. The derivation of the
matrix and image relations is elementary and written above.

[^regular]: The Stacks Project, [Lemma 10.106.3, regular local rings](https://stacks.math.columbia.edu/tag/00NQ) and [Lemma 10.104.2, regular sequences in Cohen--Macaulay rings](https://stacks.math.columbia.edu/tag/02JN), consulted September 14, 2026. The direct UFD proof in Section 2 supplies the needed instance without a deeper dependency audit.
