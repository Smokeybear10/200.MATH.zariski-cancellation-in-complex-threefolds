# Nonlinear conical speeds are excluded at every last-coordinate degree

A sliced polynomial fourfold with three coordinates affine under its
additive action cannot have a nonlinear homogeneous rank-two relation
among their speeds. No bound on the fourth coordinate's degree under
the action is required. The proof combines an actual-coordinate
determinant recurrence with a weighted polynomial-coefficient lemma.

This is a working restricted theorem. It does not put an arbitrary
cylinder into the required three-coordinate profile. The unrestricted
complex-threefold cancellation problem is not resolved by this argument.

## 1. Precise statement

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
\ker\bigl(\mathbb C[S,T,V]\longrightarrow A\bigr)=(H),
\end{gathered}
\tag{1}
\]
where the map sends \((S,T,V)\) to \((s,t,b)\) and \(H\) is
irreducible homogeneous of degree at least two.
The displayed four generators must be actual polynomial coordinates.
The slice \(u\) is not assumed to be an ambient coordinate.

The conclusion is that (1) is impossible. In the intermediate
contradiction argument, let \(\ell=\deg_u W\), which is finite by local
nilpotence. It produces an invariant coordinate
\[
I=W+P(X,Y,Z),\qquad P\in\mathbb C[X,Y,Z],\qquad
\deg P\le 2\ell .
\tag{2}
\]
The degree assertion is an intermediate implication in a class then
excluded, not an assertion that examples attain the bound.
If \(\ell=0\), \(W\) is already invariant and Section 4 applies directly.

## 2. The actual-coordinate recurrence

The selected-partial argument gives a nonzero LND
\(N=[u](\partial_W)|_A\) fixing \(s,t,b\). The complete leading-term
proof uses the original polynomial partial before localization and has
no restriction on \(\ell\). It does not imply that \(N\) kills every
coefficient of \(W\).[^1]

The all-degree chart reconstruction gives the following precise
objects and identities.[^2] Put \(L=\operatorname{Frac}\ker_A N\).
There are coefficient parameters \(\tau=t/s,\xi=s\) for which
\(L/\mathbb C(\tau,\xi)\) is finite separable,
\(\rho=b/s\) is algebraic over \(\mathbb C(\tau)\), and
\(r=\rho''\ne0\).
On the actual localization at \(s\),
\[
\begin{gathered}
B_s=A_s[X],\qquad A_s=\mathbb C[y,z,w_0]_{s_0},\qquad
A_L=L[v]=L[y,z,w_0],\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=\sum_{j=0}^{\ell}w_jX^j,\quad w_j\in L[v],\\
N'=[X](\partial_W)|_{A_s}=N/s,\qquad N'v=1 .
\end{gathered}
\tag{3}
\]
The actual Taylor chart and its inverse make its Jacobian independent
of \(X\). The cofactor of the invariant speed \(\xi=s\), together with
the coefficient \(N'v=1\), forces
\[
z=\rho' y+k,\quad k\in L,\qquad J_0=k_\xi=\beta\ne0.
\tag{4}
\]
This uses only the first two rows of the selected cofactor matrix;
it does not require an acceleration parameter.

Set \(\alpha=r y+k_\tau\) and \(C=\beta y_\tau-\alpha y_\xi\).
With all these coefficient derivatives initially holding \(v\) fixed,
the exact remaining determinant equation is
\[
\beta=(C+\beta X)W_v+y_v(\alpha W_\xi-\beta W_\tau).
\tag{5}
\]
Its highest \(X\)-coefficient gives \((w_\ell)_v=0\), hence
\(w_\ell\in L\). If \(w_j=F_j(y)\) with \(F_j\in L[y]\), the
coefficient of \(X^j\), including all chain-rule terms, gives
\[
(w_{j-1})_v
=y_v\left(\partial_\tau-\frac{r y+k_\tau}{k_\xi}
                \partial_\xi\right)F_j(y).
\tag{6}
\]
On the right, the derivatives act on coefficients while holding the
formal \(y\) fixed. Integrating the polynomial in that formal variable
and subtracting in \(L[v]\) proves \(w_{j-1}\in L[y]\).
Induction gives \(\deg_y w_j\le2(\ell-j)\).
This step does not first assume that \(y\) generates the generic line.

Now (3)--(4) imply \(L[v]=L[y]\), so \(y_v\in L^*\).
Reparameterize by \(\kappa=k\):
\[
\partial_\kappa=k_\xi^{-1}\partial_\xi,\qquad
\partial_\tau^{\rm new}
=\partial_\tau^{\rm old}-\frac{k_\tau}{k_\xi}\partial_\xi .
\tag{7}
\]
These are the commuting coefficient partials of the separating
transcendence basis \((\tau,\kappa)\). From now on \(\partial_\tau\)
means the new partial. Equation (5) becomes
\[
\mathcal P(X,y):=\sum_jF_j(y)X^j\in L[X,y],\qquad
\left(X\partial_y-\partial_\tau+r y\partial_\kappa\right)\mathcal P
=1/y_v\in L^* .
\tag{8}
\]
The whole-line argument, rather than a generic rational parametrization,
is what justifies the constant-in-\(y\) right side here.

## 3. Weighted polynomiality and descent to an original-ring coordinate

Let \(K=\ker(\partial_\kappa|_L)\). Commuting partials make \(K\)
stable under \(\partial_\tau\). Differentiation of the monic minimal
polynomial over \(\mathbb C(\tau,\kappa)\) shows that
\[
K=\overline{\mathbb C(\tau)}^{\,L},\qquad
[K:\mathbb C(\tau)]<\infty,\qquad \tau,\rho,\rho',r\in K .
\tag{9}
\]
Indeed a \(\partial_\kappa\)-constant has minimal-polynomial
coefficients killed by that derivative, so those coefficients lie in
\(\mathbb C(\tau)\). The reverse inclusion follows by separability.
Finiteness follows from finiteness of \(L/\mathbb C(\tau,\kappa)\).

The separate weighted-coefficient lemma applies to (8).[^3]
Give \(X\) weight two and \(y\) weight one. The operator
\(\delta_0=X\partial_y+r y\partial_\kappa\) raises that weight by
one, while \(\partial_\tau\) preserves it. Descending the positive
weight equations forces every coefficient of \(\mathcal P\) into
\(K[\kappa]\) by subtracting polynomial primitives in \(\kappa\).
It does not assume \(L=K(\kappa)\).

More precisely, maximum weighted degree \(n\) gives ordinary total
degree at most \(n\) in \((\kappa,X,y)\). The bound in Section 2
gives \(n\le2\ell\). Thus
\[
\mathcal P\in K[\kappa,X,y]_{\le2\ell},\qquad
y=Y-\tau X,\qquad
\kappa=Z-\rho'Y+(\tau\rho'-\rho)X,
\qquad W=G_K(X,Y,Z),\quad\deg G_K\le2\ell .
\tag{10}
\]
The substitutions are linear over \(K\), so the degree bound survives.

The exact monic rational-pencil lemma applies because
\(K\subset\operatorname{Frac}A\) has transcendence degree one and
(10) is monic in the original \(W\).[^4]
Its field-rationality input is the classical Lüroth-Igusa theorem:
such a subfield of a complex rational function field has one rational
generator.[^5] For a reduced invariant \(a=p/q\), local nilpotence
and coprimality make \(p,q\) invariant. The exact generic equation
over \(\mathbb C(a)\) is \(p-aq\); comparison with the monic
\(W-G_K\) forces at least one of \(p,q\) to have the form
\(cW+P_0(X,Y,Z)\), \(c\in\mathbb C^*\).
Dividing by \(c\) proves (2).
This is descent in the exact coefficient field, not selection of a
factor after an algebraic extension.

## 4. The slice gives a contradiction

The coordinate shear (2) preserves the goods, and its inverse is
\(W=I-P(X,Y,Z)\). Hence
\(B=\mathbb C[I,X,Y,Z]\), \(EI=0\).
Applying \(E\) to the original polynomial slice in these coordinates
shows \((s,t,b)B=B\).

Over \(F_0=\mathbb C(I)\), \(E\) is a nonzero nice LND on the actual
polynomial ring \(F_0[X,Y,Z]\).
Wang's linear-invariant theorem, as stated in Dasgupta and Gupta,
Theorem 3.1(i), supplies a nonzero \(F_0\)-linear relation among
\(s,t,b\).[^6] This theorem is used only after the invariant
coordinate has been obtained.

Dividing that relation by \(s\) gives an affine line through
\((\tau,\rho)\). The irreducible nonlinear curve
\(H(1,T,V)=0\) remains irreducible over \(F_0\); its intersection
with this line is zero-dimensional. Thus \(\tau,\rho\) are algebraic
over \(F_0\), and therefore belong to \(F_0\), which is relatively
algebraically closed in \(F_0(X,Y,Z)\).
Clear denominators and divide the gcd to write
\[
(s,t,b)=h(f_0(I),f_1(I),f_2(I)),\qquad
f_i\in\mathbb C[I],\quad \gcd(f_0,f_1,f_2)=1 .
\tag{11}
\]
The PID Bézout identity first gives \(h\in B\).
It then gives \((s,t,b)B=(h)B=B\), so \(h\in\mathbb C^*\).
All speeds lie in \(\mathbb C[I]\), contradicting their
transcendence degree two. This completes the restricted argument.

## 5. Remaining mathematical scope

The quadratic restriction has been removed for the nonlinear conical
rank-two branch, not for the entire supplied three-good class.
The higher-last-degree case with no homogeneous speed relation still
requires a different argument. The existing quadratic case coverage
uses separate dense-speed proofs that do not automatically extend.

More fundamentally, there is no argument here producing three
\(E\)-affine polynomial coordinates from an arbitrary sliced
polynomial fourfold. That coordinate-entry problem remains separate
from the degree question.
The working target is still the unconfirmed corrected statement
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).

The slice hypothesis is substantive. An explicit polynomial-coordinate
family with a nonunit common speed factor realizes nonlinear conical
speeds and arbitrarily large fourth-coordinate degree without a
slice.[^7] It is not a cancellation counterexample.
Finite exact identities do not establish the universal field lemmas
or replace human expert review. Formal proof-assistant verification
and historical novelty determination remain outstanding.

## Sources

1. [Conical selected-partial reduction135](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4. Actual leading LND and selected degree, without a
   last-coordinate degree bound.
2. [All-degree conical chart138](all-degree-conical-chart-pass138-working.md).
   Actual localization, whole generic line, cofactor identities and recurrence.
3. [Weighted coefficient polynomiality138](weighted-coefficient-polynomiality-pass138.md).
   Abstract differential-field proof and degree bound.
4. [Exact monic descent and invariant-coordinate obstruction136](conical-nonradial-quartic-coordinate-pass136-working.md),
   Sections 3 and 5. Both general lemmas have no acceleration hypothesis.
5. Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4),
   arXiv:1501.06046v4, November 2, 2017, Theorem 1.1, printed p. 4.
6. Nikhilesh Dasgupta and Neena Gupta,
   [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1),
   arXiv:1701.03635v1, January 13, 2017, Theorem 3.1(i), printed p. 5,
   attributing the statement to Z. Wang, Proposition 4.6.
7. [Higher-degree omitted-slice family138](higher-degree-no-slice-boundary-pass138.md).
   Explicit elementary shears of the actual137 boundary example.

[^1]: Source 1, Sections 2--4.
[^2]: Source 2, complete actual-ring reconstruction.
[^3]: Source 3, weighted descent and coefficient degree bound.
[^4]: Source 4, Section 3.
[^5]: Source 5, Theorem 1.1.
[^6]: Source 6, Theorem 3.1(i); the detailed obstruction is Source 4, Section 5.
[^7]: Source 7.
