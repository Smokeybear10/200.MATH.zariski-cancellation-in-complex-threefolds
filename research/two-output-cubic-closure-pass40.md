# The two-output degree-five branch has a polynomial kernel

The degree-five residual closes when its two constant good-direction
vectors are linearly dependent. The argument does not make a coprime
coefficient pair into a unimodular pair. Instead, a denominator that
cannot be removed supplies an invariant of a genuine polynomial
three-ring. The commuting-derivation theorem and relative
one-variable cancellation then descend an invariant coordinate to the
original ambient four-ring.

This is a conditional recognition theorem for the actual frame studied
in the [degree-five proof](cubic-degree-five-pass40.md). It does not
establish such a frame for an arbitrary sliced polynomial cylinder.

## 1. Exact input and conclusion

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), and let \(E\) be an LND
with a polynomial slice. Assume the complete degree-five hypotheses
and notation of the linked proof. In particular the three good
partials have vanishing second iterated adjoint, and that proof gives
\[
Z=T_e+\frac{\sigma}{3}T_d+
 \left(\frac{\sigma^2}{12}+\frac{\tau}{3\lambda}\right)T_c,
\qquad Z(g)=0,\quad [E,Z]=0,\quad Z^2x_i=0,
\tag{1}
\]
where \(Z\) is an LND on \(B_g\), \(0\ne g\in\ker E\),
\(c\ne0\), \(c_4=d_4=0\), and \(e_4=\lambda\ne0\).
Its polynomial replica is \(\mathcal W=g^4Z\).

**Theorem.** If \(d\in\mathbb Cc\), then \(\ker E\)
contains an actual coordinate of \(B\), and
\(\ker E\simeq\mathbb C^{[3]}\).

The conclusion allows nonconstant \(g\). It does not assert that
the rational field \(Z\) itself extends polynomially.

## 2. The actual localized flow removes two variables

Write \(d=\kappa c\). Since \(c,e\) are independent constant
directions, choose a complex linear coordinate system
\((u,v,a,b)\) with
\[
T_c=\partial_a,\qquad T_e=\partial_b,\qquad
Z=\partial_b+F\partial_a,
\quad
F=\frac{\kappa\sigma}{3}+\frac{\sigma^2}{12}
                  +\frac{\tau}{3\lambda}.
\tag{2}
\]
The original good space contains \(\partial_a\), because
\(c_4=0\). Put \(S=\mathbb C[u,v]\).

The original-slice unit lemma in the degree-five proof is needed
before this next step: it gives a genuine polynomial-in-time
automorphism \(\exp(tZ)\) of \(B_g[t]\). By niceness its
coordinate map is exactly
\[
(u,v,a,b)\longmapsto(u,v,a+tF,b+t).
\tag{3}
\]
Its Jacobian determinant is \(1+tF_a\). The determinant of this
actual automorphism is a unit of \(B_g[t]\), whose value at zero
is one. Since this polynomial ring is a domain, its units cannot
depend on \(t\). Therefore \(F_a=0\). Also \(ZF=0\), so
\(F_b=0\). Consequently
\[
F\in\mathbb C(u,v).
\tag{4}
\]
This argument uses the actual inverse flow, not a bare unit-Jacobian
criterion for a proposed coordinate map.

Choose coprime \(N,D\in S\), \(D\ne0\), with \(F=N/D\).
For \(F=0\), take \(N=0,D=1\). The coefficient of
\(\partial_a\) in \(g^4Z\) is polynomial, so coprimality in
the UFD \(B=S[a,b]\) gives
\[
D\mid g^4\quad\hbox{in }B.
\tag{5}
\]
Factorial closure of \(\ker E\), applied to the divisor \(D\)
of \(g^4\), gives \(E(D)=0\). Define
\[
W_0=D Z=D\partial_b+N\partial_a,
\qquad J=Da-Nb.
\tag{6}
\]
This is a primitive polynomial nice LND. It commutes with \(E\)
because \(E(D)=0\) and \([E,Z]=0\). No simultaneous
Bézout identity for \(D,N\) has been used.

## 3. A polynomial kernel and the inherited good partial

The exact kernel is
\[
R:=\ker W_0=S[J]=\mathbb C[u,v,J].
\tag{7}
\]
Here is the denominator check. After inverting \(D\), the actual
coordinates \((J,b)\) give \(\ker W_0=S_D[J]\). Let
\(\pi\) be an irreducible factor of \(D\). Reduction modulo
\(\pi\) sends \(J\) to \(-\bar N b\), with
\(\bar N\ne0\) in the domain \(S/(\pi)\). Thus the map
\((S/(\pi))[J]\to(S/(\pi))[a,b]\) is injective.
If an element of \(S_D[J]\cap B\) had a pole at \(\pi\),
localize away from \(\pi\), multiply by its minimal positive
power of \(\pi\), and reduce modulo \(\pi\). The same
injectivity after this localization contradicts the claimed
minimality. All irreducible factors of \(D\), including their
multiplicities, are removed in this way. This proves (7).
It also follows from the established relative-plane nice-LND
kernel theorem, with no fixed-point-free hypothesis.[^nice]

Commutation makes \(E\) preserve \(R\). Write
\(L=E|_R\). Since \(\partial_a\) commutes with \(W_0\), it
also restricts to \(R\), and its restriction is
\[
\partial_a|_R=D\partial_J.
\tag{8}
\]
The original good-partial identity restricts as well. Using
\(L(D)=0\) twice and cancelling the nonzero element \(D\)
in this domain gives
\[
[L,[L,\partial_J]]=0.
\tag{9}
\]
If \(L=0\), either \(u\) or \(v\) is already an invariant
ambient coordinate, and the final recognition step below applies.
Hence assume \(L\ne0\).

## 4. A unit denominator is the genuine coordinate-section case

If \(D\in\mathbb C^*\), normalize \(D=1\). Equation (6)
has the explicit polynomial inverse
\[
(u,v,J,b)\longmapsto(u,v,J+N(u,v)b,b).
\tag{10}
\]
Thus \(B=R[b]\) is an actual polynomial coordinate presentation.
The three-variable single-partial lemma, with (9), supplies a
coordinate of \(R\) annihilated by \(L\). Because of (10),
this is an actual coordinate of \(B\), not merely a coordinate
of an abstract subring. The complete proof of that lemma, including
both cases of its commuting pair, is in the
[earlier audit](height-seven-audit.md#2-a-single-partial-lemma-in-three-variables).

## 5. A nonunit denominator supplies the missing descent invariant

Now suppose \(D\) is nonconstant. Put \(P=\partial_J\) and
\(U=[L,P]\). Equation (9) says \([L,U]=0\). The field \(U\)
is an LND: on \(R[t]\), the actual conjugation
\(\exp(tL)P\exp(-tL)=P+tU\) is locally nilpotent. For each
element of \(R\), the top power of \(t\) in a sufficiently
high iterate is its corresponding \(U\)-iterate, which must
vanish. Also
\[
L(D)=P(D)=U(D)=0.
\tag{11}
\]

### Independent commuting pair

If \(L,U\) are linearly independent over \(\operatorname{Frac}R\),
the three-variable commuting-LND theorem gives
\(\ker L\cap\ker U=\mathbb C[z]\), where \(z\) is a
coordinate of \(R\).[^commuting] By (11),
\(D=H(z)\) for a nonconstant \(H\in\mathbb C[T]\).
Since \(D\in S\) and \(R=S[J]\), comparison of degrees in
\(J\) gives \(z\in S\): a nonconstant polynomial in an
element of positive \(J\)-degree cannot have degree zero.

We now use relative cancellation in precisely two variables, not
three-variable cancellation. Set \(R_0=\mathbb C[z]\) and
regard \(S\) as an \(R_0\)-algebra. The fact that \(z\) is a
coordinate of \(R\) says
\[
S[J]=R=R_0^{[2]}
\quad\hbox{as }R_0\hbox{-algebras}.
\tag{12}
\]
Hamann's theorem gives \(S=R_0^{[1]}\).[^hamann]
Thus \(z\) is an actual coordinate of the original plane
\(S\), and therefore of \(B=S[a,b]\). It is annihilated by
\(E\).

### Dependent commuting pair

Suppose instead \(U=hL\) over the fraction field, including
\(U=0\). Write the coefficients of \(L\) in the ordered
coordinates \((J,u,v)\) as \((\ell_1,\ell_2,\ell_3)\).
Because \(U=-\partial_J(L)\), all nonzero coefficient ratios
\(\ell_i/\ell_j\) lie in \(\operatorname{Frac}S\).

Divide \(L\) by the polynomial gcd \(k\) of its coefficients.
The LND factor lemma gives \(L(k)=0\); consequently
\(L_0=L/k\) is a primitive polynomial LND with the same kernel.
The ratios just found force every coefficient of \(L_0\) to lie
in \(S\). Explicitly, clear their denominators in \(S\) and
remove their gcd there to get a primitive vector in \(S^3\).
It stays primitive in \(S[J]\). Comparing prime valuations
with the primitive coefficient vector of \(L_0\) makes the
proportionality factor a global unit, hence a complex constant.

Therefore \(L_0\) preserves \(S\). If its restriction is zero,
\(u\) is an invariant ambient coordinate. Otherwise the
two-variable triangularization theorem gives a coordinate \(z\)
of \(S\) killed by \(L_0|_S\).[^plane] It is also killed by
\(L\), and is an ambient coordinate of \(B\).

These two cases reconstruct the earlier single-partial proof,
with the extra nonconstant invariant \(D\) used to make its
independent-case coordinate descend to \(S\). They do not
assume that every coordinate of \(R\) is automatically an
ambient coordinate.

## 6. Recognition and exact scope

In every case there is an actual coordinate \(z\) of \(B\)
with \(E(z)=0\). Let \(A=\ker E\). The original slice gives
\(B=A[s_*]\), so \(A\) is a regular affine ring: regularity
descends along this polynomial extension. The established
four-variable regular-kernel theorem now gives
\[
A=\mathbb C[z]^{[2]}\simeq\mathbb C^{[3]}.
\tag{13}
\]
Its hypothesis is an actual invariant ambient coordinate and a
regular kernel, both obtained before it is applied.[^regular]

This closes the \(d\in\mathbb Cc\) degree-five branch without
claiming that \(Z\) is polynomial or that \((D,N)=S\).
The three-output case \(c,d,e\) linearly independent is not
covered. The theorem also does not supply an admissible whole
frame for an arbitrary sliced LND.

## Verification and attribution

The two-output reduction and the denominator invariant were derived
from the actual residual formulas. The shorter Jacobian proof of
(4), the relative-cancellation gate, and the complete case split
were independently reconstructed across the active algebra audits.
The proof uses established theorems with their hypotheses recorded
below; it is not a Lean proof, an expert review, or a novelty claim.
No finite checker is represented as verifying the source theorems
or the global denominator and coordinate-descent quantifiers.

[^nice]: Dasgupta and Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Lemma 2.3(ii), PDF p. 3. The stated base is a UFD containing the rationals. Its complete statement was directly read; (7) also has the independent denominator proof above.

[^commuting]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 3.6, PDF p. 5, with its proof and Proposition 3.5 directly read. Both fields here are commuting polynomial LNDs on the actual three-variable ring and are polynomially independent.

[^hamann]: Hamann's relative cancellation theorem, stated as Theorem 2.6 in [Dasgupta and Gupta](https://arxiv.org/pdf/1701.03635v1), PDF p. 4, attributed there to Hamann, Theorem 2.8. The complete statement was directly read. Its base here is exactly \(\mathbb C[z]\), and (12) is an isomorphism over that base.

[^plane]: Rentschler's two-variable triangularization theorem, stated as Theorem 2.7 in [Dasgupta and Gaifullin](https://arxiv.org/pdf/2306.00510v2), PDF p. 6, complete statement directly read. It is applied only to the nonzero restriction of a polynomial LND to the actual plane \(S\).

[^regular]: Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1), Theorem 3.5, complete statement and proof directly read. The four-variable derivation is nonzero and fixes the displayed ambient coordinate; its kernel is regular by the original slice.
