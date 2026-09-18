# Recognition for the complete one-cubic-column family

The remaining three-output case in the one-cubic-column family has a
polynomial-coordinate recognition argument. A relation over a moving
rational parameter first restricts the parameter's speed. The full
coordinate identities exclude one apparent possibility. Each surviving
possibility admits an explicit polynomial shear that retains one useful
coordinate partial. An invariant-denominator argument then produces an
invariant coordinate of the original four-variable polynomial ring.

Combined with the preceding degree reductions, this proves a conditional
recognition statement for the entire supplied one-cubic-column family.
It does not show that an arbitrary cancellation problem admits such a
coordinate frame. The unrestricted working question remains
\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
This question is not solved here. The complex-threefold interpretation
is a correction and specialization of the supplied conjecture, not a
field and dimension confirmed by its author. Novelty and expert review
are not established.

## 1. The conditional theorem

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be a locally
nilpotent derivation, and suppose it has a polynomial slice
\(s_*\), meaning \(E(s_*)=1\). Write
\(T_i=\partial_{x_i}\) and
\(\operatorname{ad}_E T=[E,T]\).

**Conditional recognition theorem.** If the displayed actual coordinate
frame satisfies
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2,3),
\qquad \operatorname{ad}_E^4T_4=0,
\tag{2}
\]
then \(\ker E\) contains an actual coordinate of \(B\), and
\(\ker E\simeq\mathbb C^{[3]}\).

The statement includes lower adjoint heights. The slice theorem gives
\(B=(\ker E)[s_*]\), but does not alone identify the kernel as a
polynomial ring.[^1] The additional coordinate in the conclusion is
obtained before the regular-kernel recognition theorem is used.

The proof is distributed across the following complete derivations:

- [Flow-degree bound and the previously closed branches](research/whole-frame-recognition-pass39.md).
- [The constant-top degree-six case](research/cubic-degree-six-pass40.md).
- [Degree-five identities and the original-slice unit argument](research/cubic-degree-five-pass40.md).
- [Dependent output directions](research/two-output-cubic-closure-pass40.md).
- [The moving-parameter classification](research/three-output-cubic-speed-pass41.md).
- [Actual shears and global coordinate recognition](research/three-output-cubic-closure-pass41.md).

The new argument is presented below with its global assumptions visible.

## 2. Why the listed cases exhaust this family

If \(\operatorname{ad}_E^3T_4=0\), the previously proved mixed
\((2,2,2,3)\) theorem applies. This is the earlier
[height-nine argument](deep-pass-13.md), not an assertion about four
arbitrary quadratic-height columns.

Otherwise put \(V=\operatorname{ad}_E^3T_4\ne0\). The actual
inverse-flow Jacobian has a six-dimensional companion matrix. Its
nilpotence bounds the coordinate flow degree by six. Here the flow
degree is the greatest \(j\) for which some \(E^j(x_i)\ne0\),
not the ordinary degree of the coefficients of \(E\).

Flow degrees at most four were already recognized. For larger degrees,
the coefficient-curve argument either produces a useful commuting field
or leaves exactly
\[
\begin{aligned}
\text{degree five: }&E^5x=cg^5,\qquad E^3x_4=\lambda g^3,\\
\text{degree six: }&E^6x=c,\qquad E^4x_4=\lambda,
\end{aligned}
\quad c\ne0,\quad c_4=0,\quad\lambda\in\mathbb C^*.
\tag{3}
\]
In degree five, \(0\ne g\in\ker E\). In degree six, the top
vector is necessarily constant. Its zero secondary-constant case was
already closed by a commuting translation; (3) is the nonzero case.
That case has a polynomial nice commuting field with an actual
coordinate slice and was closed separately. No example realizing either
highest residual degree is asserted.

For degree five, constant \(g\) and dependent constant output
directions were already closed. The only additional case required by
exhaustion is the three-output situation treated next. This case split
does not discard the zero locus of \(g\).

## 3. The genuine localized symmetry

Normalize \(\delta=E/g\) on \(B_g\). The degree-five identities
produce \(\sigma,\tau\in B_g\) and constant vectors \(c,d,e\)
such that
\[
\begin{gathered}
Z=T_e+\frac\sigma3T_d+
 \left(\frac{\sigma^2}{12}+\frac\tau{3\lambda}\right)T_c,\\
\delta\sigma=1,\qquad\delta\tau=0,\qquad
[E,Z]=0,\qquad Zg=Z\sigma=Z\tau=0.
\end{gathered}
\tag{4}
\]
Here \(c_4=d_4=0\) and \(e_4=\lambda\). The derivation
\(Z\) is an actual LND of \(B_g\), and \(g^4Z\) is polynomial
and nice on \(B\). Nice means that its second iterate kills each
displayed coordinate generator.

The LND assertion needs the original polynomial slice. Generator-wise
niceness alone would not prove local nilpotence on the localized ring.
The earlier unit argument makes both \(g\) and \(g^{-1}\) have
finite \(Z\)-iterates. Their finite exponential polynomials are
inverses over a field, and therefore constant in the time parameter.
This proves \(Zg=0\) and legitimizes the localized flow.

Assume \(c,d,e\) are independent. Choose actual linear coordinates
\((w,a,b,z)\) so that \(w\) annihilates their span and
\[
T_c=\partial_a,\quad T_d=\partial_b,\quad T_e=\partial_z,
\quad x_4=\lambda z,\quad Zw=0,\quad\delta^3w=0.
\tag{5}
\]
The three partials other than \(\partial_z\) remain constant
combinations of the original good partials.

## 4. The moving parameter has restricted speed

Over \(K=\mathbb C(w)\), the polynomial nice field \(g^4Z\)
acts on an actual three-variable polynomial ring. Wang's nice-derivation
theorem, as stated by Dasgupta and Gupta, gives a nonzero linear
invariant over \(K\).[^2] Therefore
\[
A(w)+B(w)\sigma+C(w)
 \left(\frac{\sigma^2}{12}+\frac\tau{3\lambda}\right)=0,
\qquad (A,B,C)\ne(0,0,0).
\tag{6}
\]
These coefficients are rational functions of a moving parameter.
They are not assumed invariant under \(E\). Indeed \(\delta w=0\)
would make two successive differentiations force \(C=B=A=0\).

When \(C=0\), equation (6) puts \(\sigma\) in \(\mathbb C(w)\).
Integrating \(\delta^3w=0\) in this rational field writes \(w\)
as a polynomial of degree at most two in \(\sigma\), with complex
coefficients. Equality of the two rational fields excludes degree two.
Thus \(w=\kappa\sigma+\mu\), with \(\kappa\ne0\).

When \(C\ne0\), normalize the relation as
\[
\tau=a(w)+b(w)\sigma-\frac\lambda4\sigma^2,
\qquad
\delta w=\frac{\ell\sigma-b(w)}{a'(w)+b'(w)\sigma},
\quad \ell=\lambda/2.
\tag{7}
\]
The pair \((w,\sigma)\) is algebraically independent. This follows
from independence of \((\sigma,\tau)\): \(\tau\) is a nonconstant
invariant, and \(\delta\sigma=1\). The denominator in (7) cannot
vanish identically.

Set \(H=a'+b'\sigma\), \(V=\delta w\), and
\(\mathcal D=\partial_\sigma+V\partial_w\). The identity
\(\delta^3w=0\) is \(\mathcal D^2V=0\). The coefficient of
\(\sigma^5\) in the polynomial \(H^5\mathcal D^2V\) is
\[
\ell^3\bigl(3(b'')^2-b'b'''\bigr).
\tag{8}
\]
For a rational function \(v\), the equation
\(vv''-3(v')^2=0\) forces \(v\) constant: for a finite pole use
its valuation \(n<0\), and for a polynomial use its degree \(n>0\).
In either case the leading term has nonzero factor \(-n(2n+1)\).
Applying this to \(v=b'\), and then to the remaining coefficients,
gives the full alternatives in the linked classification. No bound on
the degrees of the rational coefficients is imposed.

One algebraic possibility has constant \(\delta w=\kappa\) and
\(\tau\) a quadratic in \(\sigma-w/\kappa\). It is impossible
for the actual frame. With \(W_i=[\delta,T_i]\), the full identities
give
\[
W_i\sigma=0,\qquad
W_i\tau=-\frac\lambda2T_i\sigma,
\qquad T_i\sigma\ne0\text{ for some }i\le3.
\tag{9}
\]
Constant speed and linear \(w\) also give \(W_iw=0\). They
would therefore make every \(W_i\tau=0\), contradicting (9).

The actual alternatives are exactly
\[
\begin{array}{ll}
\text{I:}&\sigma=w/\kappa+\eta,\quad\kappa\in\mathbb C^*;\\[2pt]
\text{II:}&\delta w=\nu\sigma+\kappa,\quad\nu\in\mathbb C^*,\\
&\displaystyle\tau=\frac\lambda{2\nu}
 (w-\kappa\sigma-\nu\sigma^2/2)+a_0.
\end{array}
\tag{10}
\]
All unspecified coefficients in (10) are complex constants.

## 5. The coordinate changes are polynomial with explicit inverses

In case II define
\[
A_0(w)=\frac w{6\nu}+\frac{a_0}{3\lambda},\qquad
a'=a+\frac\kappa{2\nu}b-A_0(w)z.
\tag{11}
\]
The inverse is \(a=a'-\kappa b/(2\nu)+A_0(w)z\).
Relation (10) gives \(Za'=0\), so in the actual coordinates
\((w,a',b,z)\),
\[
Z=\partial_z+\frac\sigma3\partial_b,
\qquad
\partial_b\big|_{w,a',z}
=T_d-\frac\kappa{2\nu}T_c.
\tag{12}
\]
The surviving fiber partial is a constant combination of good
partials, not a coefficient-dependent combination whose adjoint
identity could change.

In case I, \(\sigma\) is already polynomial in \(w\). Define
\[
b'=b-\frac\sigma3z,
\qquad b=b'+\frac\sigma3z.
\tag{13}
\]
Now \(Z\) fixes \(w,b'\) and has only the two fiber directions
\(\partial_z,\partial_a\). The new \(\partial_a\) is exactly
the original good \(T_c\). Both changes preserve the genuine
localized action and polynomiality of its replica.

In fact the classification strengthens denominator clearing: \(gZ\)
is already polynomial. In case II,
\(g\sigma=(Ew-\kappa g)/\nu\in B\); in case I, both \(\sigma\)
and \(g\tau=Ex_4-\lambda g\sigma^2/2\) are polynomial.
This improvement does not turn \(g\) into a unit or supply a global
slice for \(Z\).

## 6. The denominator is retained in the global proof

The remaining general lemma concerns actual coordinates
\(B=\mathbb C[u,v,a,b]\) and an LND
\(Z=\partial_b+F\partial_a\) of \(B_g\), with \(Z^2a=0\),
commuting with the original sliced \(E\), with a polynomial replica and
\([E,[E,\partial_a]]=0\).

The actual flow has Jacobian \(1+tF_a\), a unit polynomial in
\(t\). Hence \(F_a=0\), and \(ZF=0\) then gives \(F_b=0\).
Write \(F=N/D\) with coprime \(N,D\in S=\mathbb C[u,v]\).
The polynomial replica makes \(D\) divide a power of \(g\),
so factorial closure of \(\ker E\) gives \(ED=0\). Set
\[
W_0=D\partial_b+N\partial_a,
\qquad J=Da-Nb,
\qquad R=\ker W_0=S[J].
\tag{14}
\]
The last equality is exact, including over \(D=0\). At each
irreducible factor \(\pi\mid D\), reduction sends \(J\) to
\(-\overline N b\), inducing an injection over \(S/(\pi)\).
A minimal positive pole of an element in \(S_D[J]\cap B\)
contradicts this injection. Repeating removes all multiplicities.

For \(L=E|_R\), the good partial restricts to \(D\partial_J\).
Since \(LD=0\), its adjoint equation gives
\([L,[L,\partial_J]]=0\). If \(L=0\), an invariant ambient
coordinate is immediate. Otherwise \(U=[L,\partial_J]\) is an
LND, by the top coefficient of the actual conjugate
\(\partial_J+tU\), and it commutes with \(L\).

For an independent pair \(L,U\), the commuting-derivation theorem
gives a joint invariant \(p\) that is a coordinate of \(R\).[^3]
If \(D\) is a unit, the explicit presentation \(B=R[b]\) makes
\(p\) ambient. Otherwise \(D=H(p)\) with nonconstant \(H\).
Comparison of degrees in \(J\) puts \(p\) in \(S\). The relative
isomorphism \(S[J]=\mathbb C[p]^{[2]}\), followed by Hamann's
two-variable relative cancellation theorem, gives
\(S=\mathbb C[p]^{[1]}\).[^2] Thus \(p\) is ambient in this
case as well.

For a dependent pair, the coefficient ratios of \(L\) are independent
of \(J\). Removing their polynomial gcd gives a primitive LND with
all coefficients in \(S\). Its restriction either vanishes or is a
nonzero planar LND. Rentschler's theorem then provides an invariant
coordinate of \(S\).[^1] The argument neither transfers a slice
to \(R\) nor assumes that an arbitrary coordinate of \(R\) is
ambient.

Finally the original slice makes \(\ker E\) regular. Its newly
proved ambient invariant coordinate supplies the remaining hypothesis
of the regular-kernel theorem, which yields
\(\ker E\simeq\mathbb C^{[3]}\).[^4]

## 7. The remaining obstruction to unrestricted cancellation

The conditional theorem closes the profile \((1,1,1,3)\) at
slice-filtration height ten. The other first unresolved profiles are
\((0,2,2,2)\) and \((1,1,2,2)\). Thus the previously proved
all-profile threshold remains \(H\le9\); it has not become
\(H\le10\).

More fundamentally, no theorem here produces a bounded frame for an
arbitrary sliced LND. A proof that every such action has an invariant
ambient coordinate, or an effective reduction to the recognized
profiles, would still require new mathematics. The special-family
result must not be substituted for that obligation.

Recent Lie-algebra rigidity work requires local finiteness of every
element of a generated Lie algebra, not merely its generators.[^5]
The existing actual cubic example already violates that premise:
one middle commutator \(U\) satisfies
\(U^n(g)=(-1)^n n!g^{n+1}\), whose values are linearly independent.
The source therefore does not automatically supply the missing
universal frame or coordinate theorem.

The next mathematical target is the genuine two-quadratic-defect
profile, retaining its actual coordinate identities and its known
rank-two and fixed-locus obstructions. A parallel global reduction
argument remains necessary for the full question.

## 8. Verification boundary

The classification and global recognition have complete written
derivations and separate AI reconstructions. Their finite exact
controls check rational coefficients, shear inverses and inherited
partials. Such controls do not prove the all-degree pole argument,
the global denominator contraction, or the cited recognition theorems.

The separate [proof and process audit](research/proof-audits-pass41.md)
records commands, actual test outcomes, corrections, and source scope.
There is no human expert review, formal proof-assistant verification,
novelty certification, or unrestricted cancellation proof.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), Theorems 2.5, 2.7 and 2.8, PDF pp. 5-6. Slice, planar triangularization and three-variable kernel inputs.

[^2]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Theorem 3.1(i), PDF p. 5, attributed to Z. Wang, and Theorem 2.6, PDF p. 4, attributed to E. Hamann. The linear-invariant theorem is used over \(\mathbb C(w)\); relative cancellation is used over \(\mathbb C[p]\). Published in *Journal of Pure and Applied Algebra* 222 (2018), 4161-4172, [DOI](https://doi.org/10.1016/j.jpaa.2018.02.025).

[^3]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), author manuscript dated October 5, 2001, Proposition 3.5 and Theorem 3.6, PDF pp. 4-5. A coordinate generator for the joint kernel of two commuting independent LNDs on \(\mathbb C^{[3]}\).

[^4]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and proof, PDF p. 11. It requires an invariant ambient coordinate and regular original kernel.

[^5]: Mohamed Ali Belabbas, [*Rigidity for Lie algebras of locally finite derivations*](https://arxiv.org/html/2608.12567v1), submitted August 12, 2026, Theorem A and Corollary A-prime. A preprint whose elementwise local-finiteness hypothesis is not automatic here; not an input to the conditional recognition proof.
