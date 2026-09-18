# The actual degree-two module eliminates parameter-dependent slice corrections

For a whole collapsed double fiber or a mixed (2,1) fiber with
nonzero speed normal, the slice difference is independent of the
component parameter even on the entire nonreduced fiber. In the
zero-first-normal case, this follows from the actual degree-two
module, an intrinsic conic identity, and the first base-adic
coefficient equations of that identity.

Thus the original bad partial preserves the intrinsic whole-fiber
subring and commutes there with E. No global commutation, global
preservation of A, or recognition of A is asserted.

## 1. Actual setting and the remaining coefficient

Retain the actual nonconical quadratic frame and the whole-fiber
hypotheses of
[whole-fiber actions100](quadratic-whole-fiber-actions-pass100.md).
In particular
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\qquad E=\partial_u,
\qquad E^2x_i=0,\qquad E^2z=q_0\in\mathbb C^*,\\
N\ne0\text{ is the actual canonical LND},\qquad
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad A_K=K[v],
\quad K=\operatorname{Frac}S,\\
\mathfrak m\subset S\text{ is closed},\qquad
L(\mathfrak m)\ne0,\qquad
\mathcal A_0=A/\mathfrak mA=D_0[c],
\quad D_0=\mathbb C[G]/(H(G)),\\
H(t)=t^2\text{ or }t^2(t-1),\qquad
h=\eta+\epsilon\beta(c)\text{ in }\mathcal A_0,
\quad \beta\in\mathbb C[c],\\
N^3G=N^3h=0\text{ in }A,\qquad
NG=Nh=0\text{ in }\mathcal A_0.
\end{gathered}
\tag{1}
\]
The invariant inclusion S into A is faithfully flat, and A is a
domain. The actual N commutes with E and kills u. On the double
factor, epsilon is the class of G, with epsilon squared zero;
the constant part eta restricts to a complex constant eta2.
In the mixed case the double projection is the quotient by G
squared, while eta may have a different constant value on the
simple factor. All these are whole-scheme statements from100.

The global third-iterate identity for h follows there by applying
N cubed to the original-volume identity for Omega times h and
canceling the nonzero invariant Omega in the domain A. It does
not come from a quotient calculation or division at m.

When the first normal action is nonzero,100 already proves that
beta is constant. We prove the same conclusion when that action
is zero. The specified c and G are retained throughout.

## 2. Finite locally free degree modules under the actual flat inclusion

For every integer i at least zero, set
\[
\begin{gathered}
F_i=\ker(N^{i+1}:A\longrightarrow A),\qquad F_0=S,\\
0\longrightarrow F_{i-1}\longrightarrow F_i
\xrightarrow{\ N^i\ }I_i\longrightarrow0,
\qquad I_i=N^i(F_i)\subset S\quad(i\ge1),\\
\boxed{\quad F_i\text{ is finite locally free over }S,
\qquad\operatorname{rank}_S F_i=i+1.\quad}
\end{gathered}
\tag{2}
\]
Each Ii is an ideal in the Noetherian ring S. The exact sequences
therefore prove finiteness by induction. Every Fi is torsion free
as a submodule of A, and localization at invariants commutes with
the kernels. On the generic line N is a nonzero constant multiple
of partial v, so its degree-i module has dimension i+1 over K.

Here is an elementary local freeness argument without assumptions about
principality of the image ideals. At a closed base point let R be
the regular local ring of S and let x,t be regular parameters.
Write M=(Fi)R and A_R=A tensor S R. If xH belongs to M with H
in A_R, then x times N to the i+1 of H is zero. The domain and
invariance of x give H in M. Thus M intersect xA_R equals xM,
and M/xM embeds into A_R/xA_R. Flatness makes t a
nonzerodivisor on A_R/xA_R, hence also on M/xM. The latter
finite module over the DVR R/xR is therefore torsion free and
free. Lift a basis to a map \(R^d\to M\). Its finite
cokernel vanishes modulo x, so it is zero by Nakayama.
Let K0 be the finite kernel. Since x is a nonzerodivisor on M,
tensoring the kernel sequence with R/xR is still left exact.
The chosen basis makes the reduced map an isomorphism, so
K0/xK0 is zero. Nakayama gives K0 zero. Thus M is free.
At height one, finite torsion-free modules over the base DVR
are free directly; at height zero the statement is immediate.
Generic rank gives d=i+1, proving (2).

For comparison, the same saturation proves depth two and gives
the reflexive-module route through
[Stacks 0AVB](https://stacks.math.columbia.edu/tag/0AVB) and
[Stacks 0B3N](https://stacks.math.columbia.edu/tag/0B3N).
The direct argument above does not depend on that route.
Neither argument asserts that the image ideals Ii are
locally free. The retained
[second-module proof47](second-image-vector-bundle-pass47.md)
proved local freeness under its stronger plinth and divisor
hypotheses. Those extra hypotheses are not imported here.

## 3. A nonconstant beta supplies a basis with an injective fiber map

Assume for contradiction that beta is nonconstant. Put
R=S_m, n=mR, A_R=A tensor S R and w=h-eta2. The three
elements 1,G,w belong to (F2)R. Under reduction and then
projection to the double factor their images are
\[
\begin{gathered}
1,\quad\epsilon,\quad\epsilon\beta(c)
\quad\text{in }\mathbb C[c,\epsilon]/(\epsilon^2),\\
\boxed{\quad (F_2)_R=R\oplus RG\oplus Rw,\qquad
(F_2)_R\cap\mathfrak nA_R=\mathfrak n(F_2)_R.\quad}\\
N((F_2)_R)\subseteq\mathfrak n(F_2)_R.
\end{gathered}
\tag{3}
\]
The three displayed residues are complex-linearly independent:
a relation has zero constant part, then its epsilon coefficient
is a constant linear polynomial in the nonconstant beta(c).
Since (F2)R is free of rank three by (2), their residue classes
are a basis and Nakayama gives the actual R-basis in (3).
The map from its three-dimensional module fiber into A_R/nA_R
is injective, as already seen after the double projection.
This gives the intersection statement. It is not a general
purity assertion for every Fi.

By (1), N kills the whole-fiber residues of G and w and fixes
all coefficients in R. Its images remain in F2. The last line
of (3) follows from the intersection statement. Restriction to
the double factor is used only to prove independence, so the
argument applies equally to a mixed fiber.

## 4. A local conic without a unit coefficient or reduced image ideal

The element 1 is unimodular in the free rank-two module (F1)R:
otherwise 1 would belong to nA_R, contrary to faithful flatness.
Extend it to a basis 1,r. Subtract an invariant from r to write
\[
\begin{gathered}
(F_1)_R=R\oplus Rr,\qquad r=aG+bw,\qquad
Nr=p\in R\setminus\{0\},\qquad\gcd_R(a,b)=1,\\
NG=\theta b r+B_1,\qquad
Nw=-\theta a r+B_2,\qquad
p=aB_1+bB_2,\quad \theta\in R\setminus\{0\},\\
Q=\theta(aG+bw)^2-2B_2G+2B_1w\in R.
\end{gathered}
\tag{4}
\]
To justify coprimality, the localized quotient (F2)R/(F1)R
embeds into R by N squared and is torsion free. A nonunit
common divisor of a,b would make
the class of r divided by that divisor a nonzero torsion class
in the quotient of the free basis (3) by R plus Rr. This is
impossible. The regular local ring R is a UFD.

Both NG and Nw belong to F1. Write their r coefficients as
A1,A2 and their constant coefficients as B1,B2. Applying N to
r=aG+bw and comparing 1,r gives aA1+bA2=0 and
aB1+bB2=p. Coprimality yields A1=theta b and
A2=-theta a with theta in R. Theta cannot be zero, since
otherwise N squared would vanish on the entire rank-three F2,
contradicting its generic rank. Differentiating the expression
for Q in (4) gives zero, so it belongs to ker N on A_R, namely R.

No assertion makes theta a unit. No equality J=n for a second
image ideal, quadratic divisor presentation, or auxiliary conic
generation theorem is needed. These are precisely additional
gates in the older47--54 results that are not being assumed.

## 5. Flat first coefficients force the constant terms into the base square

Expand (4) in the basis (3). Its last line and the zero residue
matrix in (3) give
\[
\begin{gathered}
B_1,B_2,\ \theta a^2,\ \theta ab,\ \theta b^2
\in\mathfrak n,\qquad Q\in\mathfrak n,\\
\boxed{\quad B_1,B_2,Q\in\mathfrak n^2.\quad}
\end{gathered}
\tag{5}
\]
For Q, its defining expression has all coefficients in n,
so Q belongs to nA_R intersect R, which is n by faithful
flatness. Every coefficient of the conic relation is therefore
in n before taking any initial coefficient.

Flatness provides the exact identification
\[
\mathfrak nA_R/\mathfrak n^2A_R
\simeq(\mathfrak n/\mathfrak n^2)
\otimes_{\mathbb C}(A_R/\mathfrak nA_R).
\tag{6}
\]
Reduce the conic identity through (6), take each coefficient
in a complex basis of n/n squared, and project to the double
factor. The three quadratic monomials G squared, Gw and w
squared all vanish there. For each base coefficient the
remaining equation is
minus twice the B2 coefficient times epsilon, plus twice the
B1 coefficient times epsilon beta(c), minus the Q coefficient,
equal to zero. The independence proved in (3) forces each of
these three coefficients to vanish. This proves the boxed line
of (5), retaining the nilpotents rather than passing to the
reduced line.

This is the lowest-coefficient argument of
[initial conic48](initial-conic-fiber-pass48.md), applied to the
actual flat ring with its present basis. It does not compare
higher coefficients after merely evaluating a lower coefficient
on the fiber. The vanishing now proved is in the base ring.

## 6. Contradiction with the actual weighted leading derivative

Assume the first normal action is zero. The exact normal
coordinates and constant transverse coefficient from
[volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md)
give invariant base parameters x,t=f-a0 x and, at the generic
double component, an actual completed chart over C(c). With
y=G the relevant weighted data are
\[
\begin{gathered}
\operatorname{wt}(x)=2,\qquad\operatorname{wt}(y)=1,
\qquad\operatorname{wt}\mathbb C(c)=0,\qquad
\mathfrak n=(x,t)R,\\
t_*=b_0y^2,\qquad b_0\in\mathbb C^*,\qquad
N_*=\lambda y\partial_c,\qquad\lambda\in\mathbb C^*,\\
w_*^{(1)}=\beta(c)y,\qquad
(Nw)_*^{(2)}=\lambda\beta'(c)y^2,\\
Nw=B_2-\theta a^2G-\theta abw
\quad\text{has weight at least three by (3)--(5).}
\end{gathered}
\tag{7}
\]
Every element of n has weight at least two, hence every
element of n squared has weight at least four. The coefficients
theta a squared and theta ab belong to n, while G and w
have weight at least one. The final line follows without any
estimate on a,b or theta separately.

For the leading derivative, N star has operator weight one.
The remainder of the actual derivation has strictly greater
operator weight; terms of w beyond beta(c)y have weight at
least two. Thus neither remainder can alter the displayed
weight-two term. These are the same actual coefficient-field
and strict-weight gates used in100, not an assumption that N
kills C(c) or that a completed derivation is locally nilpotent.

Equation (7) forces lambda beta prime to vanish. Since lambda
is nonzero, beta is constant, contradicting its assumed
nonconstancy. This excludes affine as well as quadratic
nonconstant beta without using the older quartic-generation
obstruction.

## 7. Whole-fiber conclusion and remaining scope

Combining this zero-action proof with the nonzero-action result100
gives, for either collapsed profile in (1),
\[
\begin{gathered}
\boxed{\quad\beta\in\mathbb C,\qquad
\bar h\in D_0=\mathbb C[G]/(H(G)).\quad}\\
T=\partial_z\text{ in the original coordinates},\qquad
T\bar G=0,\quad T\bar u=0,\quad T\bar c=1,\\
T(A/\mathfrak mA)\subseteq A/\mathfrak mA,\qquad
[E,T]=0\text{ on }B/\mathfrak mB.
\end{gathered}
\tag{8}
\]
The second line follows from the exact whole-fiber formulas100
after setting h_c to zero. It is not a new formula for the
original derivations before quotienting. In particular this
does not prove Tu=0 or [E,T]=0 in B itself, nor that T preserves
A globally. The sector L(m)=0 is not treated by this argument.

The Artin-only inverse in100 remains a valid polynomial fiber
control. What it lacks is the actual flat degree-module lift and
conic coefficient argument above. The intrinsic polynomial
family101 has its separate exact module proof; no assertion
identifies the actual frame with that family.

## Dependencies and proof scope

Root and Geometry independently reconstructed the finite/depth
argument, basis implication and weighted comparison. Jet supplied
the elementary DVR basis-lifting proof of local freeness, which
Root and Geometry independently reconstructed. Geometry
derived the conic first-coefficient step without a unit theta;
Root independently reconstructed it before this proof was saved.
The generic-line, flatness, actual normal chart and whole-fiber
inputs are the retained theorems cited above.

Root and Geometry freshly read the complete displayed statements
and proofs of Stacks0AVB and0B3N as the comparison above. Their
deeper commutative-algebra dependencies were not freshly
reconstructed and are not needed by the direct proof. The conic
and coefficient mechanism is related to47--48, but the stronger
plinth, image-ideal and divisor-model premises of that program
are not silently transferred. No numerical computation certifies
this actual theorem, and no global cancellation or recognition
claim is made. All files through101 remain unchanged.

The [standalone symbolic control](quadratic_degree_module_checks_pass102.py)
has one method. It checks the conic and matrix identities with
nonunit theta allowed, whole/mixed double projection, finite
coefficient ranks distinguishing nonconstant from constant beta,
and sample weight comparisons. It does not prove flatness,
local freeness, an original-coordinate frame or the universal
theorem. Geometry's complete saved-code review was read-only;
execution evidence is recorded separately.
