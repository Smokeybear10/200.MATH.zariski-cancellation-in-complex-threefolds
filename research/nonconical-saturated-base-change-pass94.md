# Saturation gives the actual base change and linear reduced components

In the cubic actual frame, a closed fiber of total multiplicity six
has more structure than its finite local normalization alone. The
finite semilocal ring is already the actual base change. Every
reduced component is an affine line in the three relative generators,
and the whole, possibly nonreduced fiber is finite free of rank six
over a generic linear projection. At every generically rank-zero
component of that fiber, the two collapsed relative generators are
regular parameters at its generic point.

These are restrictions on a saturated fiber. They do not exclude
that fiber, make the intermediate exceptional curve normal, or
recognize the unrestricted threefold.

## 1. Exact inherited hypotheses

Retain the actual nonconical cubic frame of
[frontier93](nonconical-second-normal-frontier-pass93.md), including
the specified highest-adjoint invariant plane, the polynomial
cylinder and the actual relative generators. Write
\[
\begin{gathered}
S=\mathbb C[s_1,s_2],\qquad K=\operatorname{Frac}S,\qquad
A=S[A_1,A_2,c],\qquad A_K=K[v],\\
\deg_v A_i\le3,\qquad \deg_v c\le6,\qquad
\sum_{i=1}^{h}\mu_i=6,\\
\mathfrak q_i\in\operatorname{Min}(mA),\qquad
\mu_i=\operatorname{length}_{A_{\mathfrak q_i}}
           (A_{\mathfrak q_i}/mA_{\mathfrak q_i}).
\end{gathered}
\tag{1}
\]
Here m is one closed point of S, A is smooth of dimension three,
and A is faithfully flat over S. All components of its closed
fiber are included in (1), not just fixed components.

Call a complex linear combination
\(U=\lambda_1A_1+\lambda_2A_2+\lambda_3c\) admissible if its
restriction to every reduced component is nonconstant. The
inadmissible triples lie in a finite union of proper complex
linear subspaces. For each admissible U, the
[total bound92](nonconical-total-fiber-multiplicity-pass92.md) and
[saturated-rank proof93](nonconical-saturated-flat-rank-pass93.md)
give
\[
\begin{gathered}
T=(S[U])_{mS[U]},\qquad
\mathcal M=A\setminus\bigcup_i\mathfrak q_i,\qquad
O'=\mathcal M^{-1}A,\\
[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)]=1
\text{ for every }i,\qquad
\deg_vU=6,\qquad O'\simeq T^6\text{ as a T-module}.
\end{gathered}
\tag{2}
\]
The last statement includes finiteness. It was not assumed when
the semilocal ring was constructed. These assertions hold for
every admissible U, which is important below.

## 2. No further localization remains after saturation

Let \(D=A\otimes_{S[U]}T\). This is the actual localization of
A by \(S[U]\setminus mS[U]\), hence is a domain. The retained
contractions \(\mathfrak q_i\cap S[U]=mS[U]\) give embeddings
\(T\subset D\subset O'\), and O' is a further localization
of D by the images of \(\mathcal M\).

Because O' is a finite T-module and T is Noetherian, its
T-submodule D is finite too. More directly, every element of O'
is integral over T and therefore integral over D. An integral
localization of a domain cannot invert any new element: if
\(d^{-1}\) satisfies a monic equation with coefficients in D,
multiplication by the appropriate power of d shows \(1\in dD\).
Apply this to each denominator defining O'. Thus
\[
\boxed{\quad
A\otimes_{S[U]}T=D=O',\qquad
D\text{ is finite free of rank six over }T.
\quad}
\tag{3}
\]
In particular this actual base change is the full integral
closure of T in K(v), by the normality argument already proved
in saturated-rank93. This is still a localization on the base;
it is not global finiteness of A over S[U].

## 3. A rational-function lemma for all linear projections

Here is an elementary consequence of the field degrees in (2).
Let \(C_0=\mathbb C[f_1,f_2,f_3]\) be a one-dimensional affine
domain. Suppose a nonempty Zariski-open set of coefficient triples
has
\[
[\operatorname{Frac}C_0:
  \mathbb C(\lambda_1f_1+\lambda_2f_2+\lambda_3f_3)]=1.
\tag{4}
\]
Choose one such triple, so \(\operatorname{Frac}C_0=\mathbb C(t)\).
View each \(f_j\) as a rational function of t. On the projective
t-line, form the effective divisor whose order at a point is the
maximum pole order among the three functions. It has finite
support. At each point with a pole, cancellation of the maximal
principal part in a linear combination imposes one proper
complex linear condition on the coefficients. Avoid all those
finitely many hyperplanes, as well as the closed complement of
the set in (4).

For the chosen combination, its pole divisor is exactly that
common maximum divisor. The degree of this divisor equals its
function-field degree. To see this without a normalization
theorem, write the function as a coprime quotient P(t)/Q(t).
The polynomial \(P(T)-zQ(T)\) is irreducible over
\(\mathbb C(z)\): in \(\mathbb C[T,z]\), a factor independent
of z would divide both P and Q, and the degree in z is one.
Gauss's lemma then applies. Its T-degree is
\(\max(\deg P,\deg Q)\), which is also the total pole order,
including the pole at infinity.

Equation (4) therefore makes the common pole divisor have degree
one. It is a single simple pole. Choose a fractional-linear
coordinate \(\tau\) with that point as its pole. Every \(f_j\)
is affine-linear in \(\tau\); at least one is nonconstant.
Consequently \(C_0=\mathbb C[\tau]\), and its given embedding in
affine three-space is a line. No assumed normality of C0 entered
this proof.

## 4. Every reduced component is a relative affine line

For each component of (1), specialize the three actual generators.
Its coordinate ring is
\(A/\mathfrak q_i=\mathbb C[\bar A_{1,i},\bar A_{2,i},\bar c_i]\).
The admissible triples from Section 1 give (4) simultaneously
for all components. The lemma proves
\[
\boxed{\quad
A/\mathfrak q_i=\mathbb C[\tau_i],\qquad
\bar A_{1,i},\bar A_{2,i},\bar c_i
\in\mathbb C+\mathbb C\tau_i
\quad\text{for every }i.
\quad}
\tag{5}
\]
These are actual affine lines in the relative
\((A_1,A_2,c)\)-space. Distinct component primes give distinct
lines, since the three specialized generators generate the whole
fiber ring. The lines may meet. The argument does not assert
that a noncollapsed component has an affine-linear cylinder in
the original four coordinates. That stronger original-plane
statement still requires the separate collapse hypotheses of92.

### Multiplicity-one companions are disjoint

Let N be the retained primitive intrinsic LND with kernel S.
Its additive action preserves the fiber and each of its reduced
components. Indeed the image of the product of the connected
additive group with one irreducible component has irreducible
closure containing that component at the identity; maximality
of the component makes this closure that same component.
Thus N restricts to an LND on each ring in (5).

For \(\mu_i=1\), the generic whole-fiber algebra
\(A_{\mathfrak q_i}/mA_{\mathfrak q_i}\) is the field
\(\kappa(\mathfrak q_i)\). The componentwise conclusion of
[primitive-fiber54](primitive-fiber-nonvanishing-pass54.md),
with the retained primitivity and flatness hypotheses, makes
its induced derivation nonzero. Therefore the restriction of N
to \(\mathbb C[\tau_i]\) is nonzero. An LND on this polynomial
one-ring is a constant multiple of \(\partial_{\tau_i}\):
a coefficient of positive degree would give nonzero iterated
derivatives of \(\tau_i\) indefinitely. Its action is consequently
a nontrivial translation on the entire line.

Two distinct relative lines have a finite intersection. That
intersection is stable under the action because both components
are stable. A nontrivial translation has no nonempty finite
invariant subset. Hence every multiplicity-one component is
disjoint from all other components. In particular the relative
lines in the total-six profiles (5,1) and (4,1,1) are pairwise
disjoint. More generally an intersection can involve only
components on whose reduced lines N is zero. This does not
separate their images under the intermediate map to Z, make Z
normal, or exclude any of these profiles.

## 5. The whole nonreduced fiber is finite free over a line

Let \(C=A/mA\), retaining all nilpotents, and choose any admissible
U. By (5), its restriction to each component is a nonconstant
affine-linear function of \(\tau_i\). Each of the three
generators of C is consequently affine-linear in U on each
reduced component, with possibly different coefficients on
different components.

For a fixed generator, multiply its finitely many monic linear
relations, one for each component. Evaluation of that product
lies in the nilradical of C. This ideal is nilpotent because C
is Noetherian. A sufficiently large power of the product is
therefore an actual monic equation over \(\mathbb C[U]\).
All three generators are integral, so C is finite over that ring.

The two parameters generating m form a regular sequence on A
by faithful flatness over S. Their quotient C is a pure
one-dimensional Cohen--Macaulay ring, since A is regular.
It has no embedded associated primes. Every nonzero polynomial
in U avoids its minimal primes by admissibility and is therefore
a nonzerodivisor. The finite \(\mathbb C[U]\)-module C is
torsion-free, hence free because \(\mathbb C[U]\) is a PID.
Its rank is the dimension of the generic Artinian fiber already
computed in (2). Thus
\[
\boxed{\quad A/mA\simeq\mathbb C[U]^6
\text{ as a module, for every admissible }U.\quad}
\tag{6}
\]
This is a statement about the entire closed fiber, including its
nonreduced structure, rather than only its generic local rings.
It does not identify the algebra structure with a product or a
truncated polynomial algebra. This module conclusion by itself
does not imply disjointness of the reduced lines; the preceding
corollary uses the actual primitive additive action.

## 6. Rank-zero components have the actual relative parameters

Let \(\mathfrak q\) be any generically rank-zero component of
the total-six fiber. The individual degree bound92 forces both
relative generators to collapse there, and its collapsed-plane
proof gives \(A/\mathfrak q=\mathbb C[\bar c]\) and
\(\bar A_i=a_i\in\mathbb C\).

One can choose an admissible U of the form
\(c+\lambda_1A_1+\lambda_2A_2\). On a component where both
Ai are constant, c is nonconstant, so no choice is excluded.
On every other component, constancy excludes at most a proper
affine-linear subset of the coefficient plane. Avoid these
finitely many subsets. In particular \(\bar U\) on the selected
component differs from \(\bar c\) by a complex constant.

Since c can be recovered from U and the two Ai, (3) now gives
\(D=O'=T[A_1,A_2]\). Let \(O=A_{\mathfrak q}\) be its
further localization at the chosen component and put
\(\mathfrak n=\mathfrak qO\). The corresponding maximal ideal
of D is generated by mT and the two centered Ai: after imposing
these relations the quotient is exactly
\(T/mT=\mathbb C(\bar U)=\mathbb C(\bar c)\).
Consequently \(\mathfrak n=(A_1-a_1,A_2-a_2)O+mO\).

Rank zero gives \(mO\subset\mathfrak n^2\). Nakayama applied
to the finitely generated module \(\mathfrak n\) now proves
\[
\boxed{\quad
\mathfrak n=(A_1-a_1,A_2-a_2)O,
\qquad A_1-a_1,A_2-a_2
\text{ are a regular system of parameters of }O.
\quad}
\tag{7}
\]
The ring O is regular of dimension two. Thus the two generators
are independent in its conormal space; this is stronger than
their previously known constant residues. It applies to the
rank-zero component in each of the total-six profiles
(6), (5,1), (4,2), and (4,1,1), whenever that fiber exists.
It is a local statement at the generic component, not a global
coordinate assertion in A or B.

In the sole-component case, U=c itself is admissible and no
further component localization is needed: then
\(O=T[A_1,A_2]\) directly. This last equality without the
additional localization is not asserted in the reducible cases.

## 7. Remaining local and geometric gates

The retained branch degrees two and three remain necessary for
the sole multiplicity-six rank-zero case. Nothing above makes
the intermediate finite curve Z normal or separates its
normalization points. For reducible total-six profiles, (5)
constrains the actual relative fiber components but does not
identify them with the branch points of Z.

Nor does length six and the presence of quadratic/cubic equations
force a homogeneous transverse complete intersection. For example,
over any characteristic-zero field k,
\[
\operatorname{length}\frac{k[[x,y]]}{(x^2,xy+y^3)}=6,
\qquad
\{1,y,y^2,y^3,y^4,x\}\text{ is a k-basis}.
\tag{8}
\]
The relations give \(xy=-y^3\) and \(y^5=0\); the three
leading relations \(x^2,xy,y^5\) give exactly the displayed
standard monomials. Its maximal-ideal Hilbert function is
\((1,2,1,1,1)\), not that of \((x^2,y^3)\). This is an
Artinian algebra control, not an actual nonconical frame.
In particular the cleared global quadratic and cubic relations
have not been proved to generate the full localized presentation.

The new arguments here use the complete retained total-multiplicity
and saturated-flat-rank proofs, elementary integral localization,
rational-function poles and finite-module algebra. Those retained
proofs were reread through EOF in pass94. The disjointness corollary
also uses the componentwise primitive-fiber54 proof, reread through
EOF for that application, with its retained socle-theorem dependency.
No fresh primary-source proof, numerical run, new checker,
original-action construction, normality assertion for Z, or
cancellation theorem is claimed.
All pass93 and earlier files remain unchanged.
