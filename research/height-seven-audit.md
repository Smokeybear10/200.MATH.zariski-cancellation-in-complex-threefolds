# Height seven and a single double-commutator criterion

Update: the later [height-eight proof](height-eight-algebra-pass.md)
closes the all-one pattern left in Section 5. Its constant-direction
argument also strengthens the earlier observation about \(E^4(x)\).
The three-variable lemma and low-height arguments below remain valid.

The height-at-most-six argument in
[coordinate-frame-minimization-pass.md](coordinate-frame-minimization-pass.md),
Sections 1 and 2, survives an independent audit. The next pattern
\((0,1,1,1)\) also closes. In fact, the argument gives the stronger statement

\[
\text{one }q_i=0\text{ and another }q_j=1
\quad\Longrightarrow\quad K\simeq\mathbb C^{[3]}.
\tag{1}
\]

Here \(B=K[s]=\mathbb C^{[4]}\), \(E=\partial_s\), and the \(q_i\) are
the derivation degrees of a polynomial coordinate frame for the
\(s\)-degree filtration. No upper bound on the other two degrees is needed.
The argument below establishes (1) from a three-variable lemma and known
theorems. It does not claim that this formulation is new in the literature.

## 1. Audit of the existing low-height argument

The finite-generation point is legitimate: \(K\cong B/(s)\) is an affine
domain. For a finite generating set of \(K\), together with \(s\), the
maximum degree shift bounds the derivation on every polynomial in those
generators. It is therefore finite and attained. A nonzero derivation has
degree at least \(-1\), because it either moves \(K\) or moves \(s\).

If a coordinate partial \(T\) has degree \(-1\), then \(T(K)=0\) and
\(T(s)=f\in K\), so \(T=fE\). Its coordinate slice \(x\) gives
\(1=T(x)=fE(x)\). Thus \(f\) is a unit of \(B\), hence a nonzero complex
constant, and \(K=\ker T\cong\mathbb C^{[3]}\). This conclusion is stronger
than merely obtaining a slice for an intrinsic leading derivation.

For \(q\geq0\), the leading homogeneous derivation of \(T\) is locally
nilpotent. Its value on \(s\), if nonzero, is divisible by \(s\), which is
impossible for an LND on a characteristic-zero domain. Consequently

\[
\deg_s T(s)\leq q,
\qquad
T(K)\subseteq\bigoplus_{r=0}^{q}Ks^r.
\tag{2}
\]

In particular \(q=0\) implies \([E,T]=0\), by checking \(K\) and \(s\).
Two such coordinate partials have a common kernel equal to a polynomial
coordinate-plane algebra. It is \(E\)-stable, and the restricted LND either
vanishes or has an invariant plane coordinate by Rentschler's theorem.
The resulting element is an ambient coordinate of \(B\), not merely a
generator of an abstract invariant algebra. The precise plane statement is
recalled in [Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).

The final kernel-recognition theorem applies without assuming the desired
conclusion. Regularity descends from \(K[s]\) to \(K\); for example, use
faithfully flat descent of regularity for this Noetherian polynomial
extension. After the invariant ambient coordinate is named \(p\),
\(E\neq0\) is a \(\mathbb C[p]\)-linear LND of
\(\mathbb C[p]^{[3]}\). The regular-kernel hypothesis is exactly the one
needed in [Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1):
it gives \(K=\mathbb C[p]^{[2]}\).

Finally, if no degree is \(-1\), then \(H\leq6\) means
\(\sum_iq_i\leq2\), forcing at least two zeros. No gap was found in this
count or in its geometric closure. Well-ordering alone still does not
provide a height-decreasing coordinate change.

## 2. A single-partial lemma in three variables

**Lemma.** Let \(R=\mathbb C[x,y,z]\), let
\(D\in\operatorname{LND}(R)\), and suppose

\[
[D,[D,\partial_x]]=0.
\tag{3}
\]

Then \(\ker D\) contains a coordinate of \(R\). Equivalently, a nonzero
such \(D\) has rank at most two.

**Proof.** The case \(D=0\) is immediate. Put \(P=\partial_x\) and
\(W=[D,P]\). Equation (3) says that \(D\) and \(W\) commute.

First, \(W\) is locally nilpotent. This cannot be inferred from an arbitrary
bracket of LNDs. Extend the derivations to \(R[t]\) by killing \(t\).
Conjugation by the polynomial automorphism \(\exp(tD)\) gives the LND

\[
Q=\exp(tD)P\exp(-tD)=P+tW,
\tag{4}
\]

because the second iterated bracket vanishes. For each \(f\in R\), choose
\(N\) with \(Q^N(f)=0\). The coefficient of \(t^N\) in this expression is
\(W^N(f)\), so \(W^N(f)=0\). This proves the assertion without any
specialization argument or uniform nilpotency bound.

If \(D,W\) are linearly independent over \(R\), the known commuting-LND
theorem gives a coordinate \(p\) with
\(\ker D\cap\ker W=\mathbb C[p]\). The exact complex-field source is
[Maubach, Theorem 3.6](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf).
It requires commuting, polynomially independent LNDs on the three-variable
polynomial ring, but no irreducibility hypothesis on either derivation.
The equivalent distinct-kernel formulation is also explicitly stated in
[Dasgupta and Gaifullin, Proposition 2.14](https://arxiv.org/pdf/2306.00510).
This handles the independent case.

Suppose instead that \(W=hD\) over \(\operatorname{Frac}R\); this includes
\(W=0\). Write

\[
D=b_1\partial_x+b_2\partial_y+b_3\partial_z,
\qquad (b_1,b_2,b_3)\ne0.
\]

Since \(W=-\sum_j(\partial_xb_j)\partial_j\), choosing \(b_k\ne0\) gives

\[
\partial_x(b_j/b_k)=0,
\qquad b_j/b_k\in\mathbb C(y,z).
\tag{5}
\]

Let \(g=\gcd(b_1,b_2,b_3)\) and \(D_0=D/g\), whose coefficient vector
\(c=(c_1,c_2,c_3)\) is primitive in the UFD \(R\). The derivation \(D_0\)
is polynomial. Moreover \(D(g)=gD_0(g)\); local nilpotence and the usual
LND-degree argument imply \(D(g)=0\). Thus \(D_0(g)=0\), and

\[
D^m(f)=g^mD_0^m(f)
\]

proves that \(D_0\) is locally nilpotent as well. It has the same kernel
as \(D\).

Here is the denominator check needed to use (5). Put \(A=\mathbb C[y,z]\).
Clearing the denominators of the ratios in (5), and then removing their
gcd in \(A\), produces a primitive vector \(a\in A^3\) proportional to
\(c\). Thus \(c=ta\) for some \(t\in\operatorname{Frac}R\). The vector
\(a\) remains primitive in \(A[x]=R\): a common irreducible factor of its
nonzero entries cannot depend on \(x\). For every irreducible \(\pi\in R\),
one of the entries of \(a\) has \(\pi\)-valuation zero. Since all entries
of \(c\) are polynomial, it follows that \(v_\pi(t)\geq0\). Hence
\(t\in R\). Primitivity of \(c\) then makes \(t\) a unit of \(R\), so
\(t\in\mathbb C^*\). In particular

\[
c_1,c_2,c_3\in\mathbb C[y,z].
\tag{6}
\]

Consequently \(D_0\) preserves the coordinate-plane algebra \(A\).
If its restriction is zero, \(y\) is an invariant ambient coordinate.
Otherwise Rentschler's theorem supplies a coordinate \(p\) of \(A\)
annihilated by that restriction. Such \(p\) remains a coordinate of
\(R=A[x]\), and \(D(p)=gD_0(p)=0\). This completes the proof. \(\square\)

The primitive-normalization step is essential in the dependent case.
Equation (5) alone does not say that the original coefficients \(b_j\)
are independent of \(x\). No claim that their gcd generates their full
coefficient ideal is used: the argument is in terms of prime valuations,
not a nonexistent multivariable Bezout identity.

## 3. Application to the slice filtration

Suppose \(q_0=0\) and \(q_1=1\), and write the corresponding coordinate
frame as \((x_0,x_1,x_2,x_3)\). The identity
\([E,\partial_{x_0}]=0\) makes

\[
R=\ker\partial_{x_0}=\mathbb C[x_1,x_2,x_3]
\]

stable under \(E\). Its restriction \(D=E|_R\) is an LND.
For \(T=\partial_{x_1}\), equation (2) gives
\(T(K)\subseteq K+Ks\) and \(T(s)\in K+Ks\). Hence

\[
[E,[E,T]](k)=E^2T(k)=0\quad(k\in K),
\qquad
[E,[E,T]](s)=E^2T(s)=0.
\]

The double bracket therefore vanishes on \(B=K[s]\). Since \(T\) also
preserves \(R\), restriction gives
\([D,[D,\partial_{x_1}|_R]]=0\). The lemma supplies a coordinate \(p\)
of \(R\) killed by \(D\). It is an ambient coordinate of \(B=R[x_0]\)
killed by \(E\). Applying the regular-kernel theorem as in Section 1 gives
\(K=\mathbb C[p]^{[2]}\), proving (1).

In particular,

\[
H\leq7\Longrightarrow K\simeq\mathbb C^{[3]},
\qquad
K\not\simeq\mathbb C^{[3]}\Longrightarrow H_{\min}(E)\geq8.
\tag{7}
\]

Indeed, without a degree \(-1\), height seven means \(\sum q_i=3\).
There are either two zero degrees, already handled, or the pattern
\((0,1,1,1)\). More generally, a hypothetical nonpolynomial kernel can
have only frames with either all \(q_i\geq1\), or exactly one zero and
the other three degrees at least two. Thus the only unclosed pattern at
height eight is

\[
(q_i)=(1,1,1,1).
\tag{8}
\]

This is a restriction on a hypothetical counterexample, not evidence that
such a counterexample exists. The closure gives an adapted height-three
frame existentially after recognizing \(K\). It does not yet give an
explicit elementary descent from the original frame or a bound on the
degrees of the coordinate change.

## 4. Audit of the Riccati detour

For completeness, suppose all three coordinate partials on
\(\mathbb C[x_1,x_2,x_3]\) satisfy the double-bracket identity, and write
\(b=(D(x_j))_j\), \(J=(\partial_i b_j)_{j,i}\). Then

\[
D(J)=J^2,\qquad D^r(J)=r!J^{r+1}.
\]

Local nilpotence on the finitely many entries of \(J\) makes \(J\)
nilpotent. As a three-by-three matrix over a domain it satisfies \(J^3=0\).
Ordinary differentiation gives

\[
\operatorname{Jac}(Db)=2J^2,
\qquad
\operatorname{Jac}(D^2b)=6J^3=0.
\]

Therefore every \(D^3(x_i)\) is constant. If one is nonzero, then
\(D^2(x_i)/D^3(x_i)\) is a slice. Otherwise \(D^3\) kills the three
coordinate generators. This reduction is valid, but the single-partial
lemma closes both branches without a classification of quadratic-degree
additive actions.

The identities do not force an invariant linear form in the original
coordinates. For example,

\[
D=\partial_a+a\partial_b+(b+a^2/2)\partial_c
\]

is triangular and satisfies all three double-bracket identities. It has
\(D^3(c)=2\) and no nonconstant invariant affine-linear polynomial: the
derivative of \(Aa+Bb+Cc\) is \(A+Ba+C(b+a^2/2)\). Nevertheless
\(b-a^2/2\) is an invariant ambient coordinate. This distinguishes the
proved coordinate conclusion from a false linearization shortcut.

## 5. Exact identities left at height eight at this checkpoint

For the unclosed pattern \((1,1,1,1)\), put
\(W_i=[E,T_i]\) in the four-variable ambient ring. The conjugation argument
above proves that every \(W_i\) is an LND and \([E,W_i]=0\). Since the
coordinate partials commute, applying \(\operatorname{ad}_E^2\) to
\([T_i,T_j]=0\) gives

\[
0=2[W_i,W_j].
\]

Thus \(E,W_1,\ldots,W_4\) are mutually commuting LNDs. If their generic
rank is four, their additive-group action has an open orbit; closedness
of unipotent orbits on an affine variety makes it transitive. The acting
commutative unipotent group modulo its stabilizer is a four-dimensional
vector group, with \(E\) a nonzero translation direction. Consequently
\(K\cong\mathbb C^{[3]}\) in that full-rank case. This is the same
closed-orbit mechanism already used in
[intrinsic-actions-pass.md](intrinsic-actions-pass.md), not a proof that
full rank occurs.

The four-by-four Riccati calculation similarly gives \(J^4=0\) and
\(E^4(x_i)\in\mathbb C\). A nonzero such constant displays a slice,
but the subsequent argument extracts more from the whole vector:
\(c=E^4(x)\ne0\) satisfies \(Jc=0\), giving a constant commuting
translation and an invariant ambient coordinate by the three-variable
lemma. The later [height-eight proof](height-eight-algebra-pass.md)
also closes the zero-top-constant and lower-group-rank branches by
rank-one quasi-translations and rank-preserving homogenization.
There is still no ordinary polynomial-degree bound. At height nine
the only degree pattern not already excluded is \((1,1,1,2)\);
no claim of closure is made for it.
