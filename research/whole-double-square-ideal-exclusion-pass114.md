# The first coefficient cannot lie in the square of the residual ideal

In the actual proper whole-double branch, h does not belong to J squared,
where J=(a,b). This conclusion does not require either generator to be
smooth. The proof lifts a factorization over the Artinian ring Rhat/J,
including its nilpotents, and contradicts the one-prime support of P.

Together with the separate smooth-a exclusion, it also forces b to be
singular. Thus every surviving proper branch has a,b in m squared and
h in m squared but outside J squared. The full branch is not excluded.

## 1. Actual input and the complete-intersection filtration

Work over the completed regular local base Rhat and write R for it in
this note. Its residue field is C. The actual coefficient restrictions
from [product-index112](whole-double-product-index-pass112.md) and the
analytic-prime conclusion of [ramified113](whole-double-ramified-completion-descent-pass113.md)
give

\[
\begin{gathered}
J=(a,b)\text{ is }\mathfrak m\text{-primary},\quad a,b\ne0,\\
b^2=s h+a^2u+abv\quad(s,u,v\in R),\\
B_2\in\mathfrak m(h)+\mathfrak m(a^2)
          +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
P=ah+bB_2=w p^e\ne0,
\quad w\in R^*,\quad p\text{ prime in }R,\quad e\ge1.
\end{gathered}
\tag{1}
\]

All these identities hold after completing the base. In particular p
being prime here is the separately proved analytic-irreducibility input,
not a claim that algebraic irreducibility always survives completion.
The proof below is an algebraic consequence of (1). It does not use a
completed derivation or construct an actual threefold from coefficients.

Because R is a regular local surface and J is m-primary, a,b is a
regular sequence. Put C0=R/J, with maximal ideal n=m/J. This is a local
Artinian ring, possibly nonreduced. The regular-sequence associated
graded algebra is

\[
\operatorname{gr}_J R=C_0[A,B],\qquad
A=\operatorname{in}_J(a),\quad B=\operatorname{in}_J(b).
\tag{2}
\]

Each homogeneous degree-d coefficient is therefore unique over C0.
This is the regular-immersion/conormal-algebra fact, not an assumption
that C0 is a field.[^graded] The J-adic and m-adic topologies are
equivalent, so R is complete also for J. No section C0 into R is assumed.

## 2. A square-ideal assumption forces a unit coefficient

Suppose h belongs to J squared. Write h2 for its class in J squared
modulo J cubed. In degree two of (1), comparison of the coefficient of
B squared gives 1=s0 h02 in C0, where s0 is the image of s and h02
is that coefficient in h2. Consequently s and h02 are units. In
particular h has J-order exactly two. Conversely, if any presentation
in (1) has s a unit, it immediately puts h in J squared.

The bound on B2 now gives B2 in mJ squared. Let P3 be the class of P
in J cubed modulo J fourth, and let bars indicate reduction of C0 to
its residue field. Then

\[
\begin{gathered}
h\in J^2\quad\Longleftrightarrow\quad s\in R^*,\qquad
h_{02}\in C_0^*,\qquad B_2\in\mathfrak mJ^2,\\
P_3\in C_0[A,B]_3,\qquad
\overline{P_3}=A\overline{h_2},\qquad
\overline{h_2}(0,1)\ne0.
\end{gathered}
\tag{3}
\]

The equivalence concerns a presentation satisfying (1); in the forward
direction its coefficient s must be a unit for every such presentation.
The last nonvanishing also shows that P has J-order exactly three.

## 3. Factor the initial cubic over the Artinian coefficient ring

Consider F(T)=P3(T,1) in C0[T]. Its residue has a simple root at zero:
Fbar(0)=0 and Fbar prime(0)=h2bar(0,1) is nonzero. This root lifts to
some rho in n with F(rho)=0. For completeness, choose any lift of zero
and repeatedly replace it by rho minus F(rho)/F prime(rho). The
derivative stays a unit, and the error is squared at each step. Since
n is nilpotent, finitely many corrections give an exact root. This
argument does not need F to be monic.[^hensel]

Monic polynomial division by T-rho and homogenization now give

\[
\begin{gathered}
P_3=L_1 Q_2,\qquad L_1=A-\rho B,\quad
Q_2\in C_0[A,B]_2,\\
Q_2(\rho,1)=F'(\rho)\in C_0^*,\\
(L_1,Q_2)\supseteq (A,B)^2
\quad\text{in }C_0[A,B].
\end{gathered}
\tag{4}
\]

Indeed reduction modulo L1 sends Q2 to a unit times B squared. Thus
B squared lies in (L1,Q2); expressing A=L1+rho B then puts AB and
A squared there too. This works with nilpotent coefficients and uses
neither a gcd calculation over a field nor a reduced associated graded
algebra. Every homogeneous polynomial of degree at least two is in
the displayed ideal.

## 4. Lift the factorization through powers of J

Lift L1 and Q2 to elements L in J and H in J squared of R. Their
product agrees with P modulo J fourth. Suppose it agrees modulo J to
the d for d at least four. By (4), the degree-d class of P-LH can be
written

\[
\begin{gathered}
\operatorname{in}_{J,d}(P-LH)=L_1 V_{d-1}+Q_2 U_{d-2},\\
L\longmapsto L+\widetilde U_{d-2},\qquad
H\longmapsto H+\widetilde V_{d-1},\\
\widetilde U_{d-2}\in J^{d-2},\quad
\widetilde V_{d-1}\in J^{d-1},\qquad
P-LH\in J^{d+1}\text{ after the correction}.
\end{gathered}
\tag{5}
\]

The tildes are arbitrary coefficient lifts, not a ring section of C0.
The product of the two corrections has J-order at least 2d minus three,
which is greater than d. The higher-order tails of the old factors
also contribute only above degree d. Thus the correction improves the
agreement by one order. Completeness gives limiting factors, still
denoted L,H, with P=LH and unchanged initial forms L1,Q2.

It remains to show that these two factors do not share a prime. Initial
generation in (4) gives J squared contained in (L,H)+J cubed. On the
finite module M=(J squared+(L,H))/(L,H), this says M=JM. Nakayama's
lemma gives M=0. Therefore

\[
P=LH,\qquad L\in J,\quad H\in J^2,\qquad
J^2\subseteq(L,H),\qquad \sqrt{(L,H)}=\mathfrak m.
\tag{6}
\]

Both factors are nonunits. In the regular local UFD R, (1) would make
each a unit times a positive power of p. Then (L,H) would lie in the
height-one ideal (p), contrary to (6). This contradiction excludes
h in J squared. The argument does not infer coprimality from initial
forms over the nonreduced C0; the Nakayama step is indispensable.

## 5. Both residual generators must be singular

The independently proved [smooth-a theorem114](whole-double-smooth-a-exclusion-pass114.md)
gives a in m squared, and113 already gives h in m squared. If b were
smooth, b squared would have nonzero ordinary quadratic initial form.
In (1), a squared has order at least four and ab has order at least
three. The quadratic term must therefore come from s h. This forces
s to be a unit, contradicting (3) and the exclusion just proved. Thus

\[
\boxed{\begin{gathered}
h\notin J^2,\qquad a,b\in\mathfrak m^2,\qquad
0\ne h\in\mathfrak m^2\setminus J^2,\\
J\subseteq\mathfrak m^2,\qquad
\operatorname{length}(R/J)\ge4.
\end{gathered}}
\tag{7}
\]

For the length bound, the first two ordinary graded pieces of R/J have
dimensions one and two. The quadratic initial forms of its two ideal
generators span at most a two-dimensional subspace of m squared modulo
m cubed, which has dimension three. At least one further dimension
survives. This proves the bound without an intersection-multiplicity
formula. No interchange of a and b is used.

## Scope and sources

The separate [smooth-second-generator proof](whole-double-smooth-second-generator-exclusion-pass114.md)
obtains the b-smooth exclusion by weighted factorization and allowed
basis changes. It is an independent reconstruction of that corollary,
not an additional resolution of the remaining branch. The present
square-ideal exclusion also treats many cases with neither generator
smooth. The remaining singular coefficient configurations, actual
formal-parameter existence and general cancellation stay unresolved.

The proof uses the actual112 coefficient relations and113 analytic-prime
support, plus standard commutative algebra explicitly isolated below.
No finite computation proves the universal ideal-adic factorization.
AI reconstruction is not human expert review, formal verification or
novelty clearance. All files through113 are unchanged.

[^graded]: The Stacks Project,
    [regular and quasi-regular immersions063L](https://stacks.math.columbia.edu/tag/063L),
    [conormal characterization063M](https://stacks.math.columbia.edu/tag/063M),
    and [the symmetric conormal-algebra map0632](https://stacks.math.columbia.edu/tag/0632).
    Complete selected statements and displayed proofs or equation were
    read. The regular sequence a,b defines the regular immersion here;
    the conormal basis consists of their classes. Deeper cited proofs
    were not all reconstructed afresh.

[^hensel]: The finite nilpotent Newton argument is given in full above.
    Compare The Stacks Project,
    [complete local rings are Henselian04GM](https://stacks.math.columbia.edu/tag/04GM),
    whose displayed statement and proof were read. The argument here
    uses a unit derivative directly, rather than asserting a nonmonic
    polynomial satisfies a theorem stated only for monic polynomials.
