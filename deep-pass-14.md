# Coordinate-plane recognition and the nonlinear construction gap

The unrestricted complex threefold cancellation conjecture is not
resolved. A complete obstruction now excludes a specific proposed
shortcut: even an explicitly trivial slice action on affine four-space
can have no nonconstant invariant in any affine-linear coordinate
plane. Any universal plane-construction argument must accommodate
genuinely nonlinear changes of coordinates.

The sufficient recognition criterion is already known. If an LND's
direction on an actual coordinate plane depends only on that plane,
quasi-extension descent and Rentschler's theorem supply an invariant
coordinate. Freudenburg's published intersection theorem gives the
equivalent invariant-polynomial formulation. These are prior results,
not a new solution.[^1][^2][^3]

The useful additional reductions below remove rational normalizing
factors and settle a common-factor subcase of commuting plane-row
actions. Explicit examples identify what those reductions do not give.
The preceding mixed-commutator working theorem is unchanged; no
universal height bound or coordinate-descent operation is established.

## 1. Exact target

The working geometric question is
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
Equivalently, write \(B=\mathbb C[x_1,x_2,x_3,x_4]=K[s]\).
The translation derivation \(E=\partial_s\) is locally nilpotent:
every polynomial is killed by a sufficiently high iterate of \(E\).
It has a slice, meaning \(E(s)=1\). The question is whether
\(K=\ker E\) must be a polynomial three-ring.

Conversely, a slice LND on \(B\) gives \(B=(\ker E)[s]\), so this
formulation does not discard any instance of (1). An invariant ambient
coordinate means an element killed by \(E\) which belongs to a full
polynomial coordinate system of \(B\), not merely a nonconstant
invariant or a generator of a rational subfield.

The introduction of the November 2025 revision of *Relative
Cancellation* explicitly records characteristic-zero polynomial-ring
cancellation in dimension at least three as open.[^4] This is a dated
literature statement, not a certification that every subsequent
manuscript has been checked. No verified general resolution is supplied
here. The corrected complex-threefold interpretation of the original
email remains unconfirmed by the professor.

## 2. The known fixed-plane criterion

Fix an actual polynomial decomposition
\[
B=R[a,b],\qquad R=\mathbb C[z,w].
\tag{2}
\]
Let \(f=E(z)\), \(g=E(w)\). Apart from the immediate case
\(f=g=0\), suppose their projective direction is defined over
\(F=\mathbb C(z,w)\). Equivalently, when \(g\ne0\),
\(f/g\in F\). Take a primitive pair \(p,q\in R\) in that
direction. Unique factorization in the polynomial extension gives
\[
f=hp,\qquad g=hq,\qquad 0\ne h\in B.
\tag{3}
\]
Indeed, \(qf=pg\), and coprime plane polynomials remain coprime
in \(B\). This is prime divisibility, not an assertion that a
coprime pair generates the unit ideal.

Put \(D=p\partial_z+q\partial_w\). Then \(E|_R=hD\), a
quasi-extension. Freudenburg and Moser-Jauslin's Lemma 2.1 implies
that \(D\) is locally nilpotent, without requiring \(E(h)=0\).[^1]
The elementary degree calculation makes that distinction explicit.
For nonzero \(u\), let \(\nu(u)=\max\{j:E^ju\ne0\}\).
Whenever \(Du\ne0\),
\[
\nu(Du)=\nu(u)-\nu(h)-1.
\tag{4}
\]
Successive nonzero \(D\)-iterates would strictly lower a nonnegative
integer. Thus they terminate. Rentschler gives a coordinate of the
plane killed by \(D\), hence by \(E\).[^3]

For this fixed coordinate plane the following conditions are
equivalent: the projective direction descends; the plane contains a
nonconstant invariant; and it contains an invariant plane coordinate.
For the reverse implication, differentiating any nonconstant plane
invariant \(u\) gives \(u_zf+u_wg=0\), which determines the ratio
unless a displayed coordinate is already invariant. The
invariant-polynomial-to-coordinate implication is exactly the published
Corollary 5.43, not merely a nearby result.[^2]

An exact computational test, when the pair is nonzero, is
\[
g\partial_a f-f\partial_a g=0,
\qquad g\partial_b f-f\partial_b g=0.
\tag{5}
\]
It checks descent of a rational direction, not preservation of the
plane by the original field. The full equivalence, degeneracies and
denominator checks are in
[the fixed-plane derivation](research/pass14-projective-plane-recognition.md).

## 3. Why constructing the plane is still the central problem

For a slice LND on \(B\), its kernel is regular because
\(B=K[s]\) is regular. If an ambient invariant coordinate \(u\)
exists, Bhatwadekar, Gupta and Lokhande's Theorem 3.5 gives
\(K=\mathbb C[u]^{[2]}\).[^5]

Consequently the following existence statements are equivalent here:

| Existence statement | Reason it suffices |
| --- | --- |
| A coordinate plane with projectable direction | Section 2 produces an invariant coordinate. |
| A coordinate plane containing a nonconstant invariant | The published intersection criterion applies. |
| An ambient invariant coordinate | Regular-kernel recognition gives a polynomial kernel. |
| A polynomial basis of the kernel | Together with the slice it is an ambient coordinate frame. |

The final row also proves the reverse implications: if
\(K=\mathbb C[u,v,w]\), then \(u,v,w,s\) are ambient coordinates.
Thus a universal existence assertion for the required plane is not
an already-solved or automatically weaker replacement for cancellation.

The embedding hypothesis matters. For example,
\(\mathbb C[z,zw]\subset\mathbb C[z,w,a,b]\) is abstractly a
polynomial plane, but not a coordinate factor. Its fraction field
contains \(w\), an ambient polynomial absent from that subring.
An actual coordinate factor \(R\subset R[a,b]\) instead satisfies
\(B\cap\operatorname{Frac}R=R\).

## 4. Primitive rational normalizers commute

Here is a general elementary reduction with no dimension or slice
bound. Let \(B=k[x_1,\ldots,x_n]\), with characteristic zero,
let \(E\) be an LND, and let \(U_0\ne0\) be a polynomial
derivation whose coefficient gcd is one. If
\[
[E,U_0]=qU_0,\qquad q\in\operatorname{Frac}B,
\tag{6}
\]
then \(q=0\).

First, the left side is polynomial. A prime in a reduced denominator
of \(q\) would divide every coefficient of \(U_0\), contrary
to primitivity. Thus \(q\in B\). The conjugate
\[
U_t=\exp(tE)U_0\exp(-tE)
\]
has polynomial coefficients in \(t\), because the exponentials
terminate on each of the finitely many generators. Differentiation
of this conjugation gives
\[
U_t'=\exp(tE)(q)U_t.
\tag{7}
\]
Choose any nonzero coefficient \(P(t)\) of \(U_t\). Over
\(\operatorname{Frac}B[t]\), equation (7) is
\(P'=\exp(tE)(q)P\). A nonzero derivative has smaller degree
than \(P\), whereas a nonzero polynomial multiple cannot. If
\(P\) is constant, the conclusion is immediate as well. Hence
\(\exp(tE)(q)=0\), and evaluation at zero gives \(q=0\).

If a nonzero polynomial LND \(U\) is rationally normalized by
\(E\), divide its coefficient gcd \(d\) to obtain \(U=dU_0\).
Because \(d\mid U(d)\), LND degree forces \(U(d)=0\).
Therefore \(U_0\) is an LND, since
\(U^j(f)=d^jU_0^j(f)\), and it commutes with \(E\) by the
preceding proof. This does not imply that \(E(d)=0\) unless the
original fields already commute.

A useful special case reverses the two fields: an LND normalizing a
slice derivation must commute with it, because the slice makes that
derivation primitive. A separate proof over any characteristic-zero
slice domain appears in
[the normalizer note](research/nice-normalizer-descent-pass.md).
No novelty claim is made for either elementary observation.

## 5. What a commuting plane row does and does not provide

Suppose \(E\) has a slice and is normalized by the nonzero nice field
\[
Z=p(z,w)\partial_a+q(z,w)\partial_b.
\tag{8}
\]
Here nice means that the square of the derivation kills every displayed
generator. Section 4 makes \(Z\) commute with \(E\). Write
\(Z=dZ_0\) using the plane coefficient gcd. Then
\([E,Z_0]=-(E(d)/d)Z_0\). Primitivity makes \(E(d)/d\)
polynomial; LND divisibility forces \(E(d)=0\).

If \(d\) is nonconstant, it is an invariant in the actual plane
\(\mathbb C[z,w]\). Sections 2 and 3 recognize the kernel of
\(E\) as a polynomial three-ring. This is a height-independent
sufficient subcase, conditional on the displayed plane-row form.

If \(\gcd(p,q)=1\), put \(v=qa-pb\). Then
\[
\ker Z=\mathbb C[z,w,v].
\tag{9}
\]
To prove (9), localize separately at \(p\) and \(q\), where a
slice is available, and intersect the resulting coefficient rings.
Coprimality gives \(R_p[v]\cap R_q[v]=R[v]\). The cases with
one zero coefficient reduce to a nonzero constant other coefficient.

If \((p,q)=R\), choose \(\alpha p+\beta q=1\). The coordinates
\(v=qa-pb\), \(t=\alpha a+\beta b\) give
\(a=pt+\beta v\), \(b=qt-\alpha v\), so the quotient is an
actual coordinate three-factor. Commutation then writes
\[
E=D+f\partial_t,\qquad
D\in\operatorname{LND}(\mathbb C[z,w,v]),\quad
f\in\mathbb C[z,w,v].
\tag{10}
\]
It does not prove that \(D\) kills an ambient coordinate of that
three-ring. Such recognition requires an additional argument.

If the primitive row is not unimodular, its common-zero set
\(\Sigma\subset\mathbb A^2\) is finite and nonempty. The map
\((z,w,a,b)\mapsto(z,w,qa-pb)\) omits every point
\((e,v)\) with \(e\in\Sigma\), \(v\ne0\). It therefore
cannot be a coordinate projection. The induced \(E\)-action fixes
these punctured lines: a connected additive group cannot permute the
finite components, and has no nontrivial algebraic action on
\(\mathbb C^*\). By density the entire lines are fixed.
This gives a restriction on the induced action, not plane projectability.

## 6. A uniform obstruction to every affine-linear plane

Take \(B=\mathbb C[a,b,c,s]\), \(E=\partial_s\), and introduce
\[
x_1=a+s^2,\quad x_2=b+s^3,\quad x_3=c+s^4,\quad
x_4=s+x_1x_2.
\tag{11}
\]
The inverse is
\[
s=x_4-x_1x_2,\quad a=x_1-s^2,\quad b=x_2-s^3,\quad
c=x_3-s^4.
\tag{12}
\]
Thus this is an explicitly trivial action with kernel
\(\mathbb C[a,b,c]\). In the displayed frame,
\[
E(x_1,x_2,x_3,x_4)
=(2s,3s^2,4s^3,1+2x_2s+3x_1s^2).
\tag{13}
\]

**Proposition.** If \(U,V\) are affine-linear forms in the displayed
\(x\)'s with independent linear parts, then
\(\ker E\cap\mathbb C[U,V]=\mathbb C\).

If the plane does not involve \(x_4\), its polynomials belong to
\(\mathbb C[x_1,x_2,x_3]\). The equation
\(Ef=2s f_{x_1}+3s^2 f_{x_2}+4s^3 f_{x_3}=0\) forces all three
partial derivatives to vanish, because \(x_1,x_2,x_3,s\) are
independent coordinates. Thus \(f\) is constant.

Otherwise change the affine basis of the plane so that
\[
U=x_4+\alpha x_1+\beta x_2+\gamma x_3+u_0,
\quad V=l_1x_1+l_2x_2+l_3x_3+v_0,
\tag{14}
\]
where \(l=(l_1,l_2,l_3)\ne0\). On \(s=0\), their restrictions
are \(U_0=x_1x_2+\alpha x_1+\beta x_2+\gamma x_3+u_0\)
and \(V_0=V\). They are algebraically independent: their Jacobian
minors include
\[
M_{12}=(x_2+\alpha)l_2-(x_1+\beta)l_1,
\quad M_{13}=(x_2+\alpha)l_3-\gamma l_1.
\tag{15}
\]
Identical vanishing of these minors would force first
\(l_1=l_2=0\), then \(l_3=0\). Hence substitution into
\((U_0,V_0)\) is injective.

For an invariant \(F(U,V)\), restrict its derivative to \(s=0\).
Formula (13) gives \(EU=1\), \(EV=0\) there, hence
\(F_U(U_0,V_0)=0\). Injectivity forces \(F_U=0\), so
\(F\) is a polynomial in \(V\) alone. But
\(EV=2l_1s+3l_2s^2+4l_3s^3\ne0\); the domain property then
forces \(F_V=0\). This proves the proposition for all complex
parameters, without sampling them.

The known fixed-plane criterion consequently excludes projectable
direction in every affine-linear plane of this frame. Nevertheless
\(\mathbb C[a,s]\) is a successful nonlinear coordinate plane.
The field even commutes with \(\partial_{x_3}\), so a commuting
coordinate partial does not repair the linear-plane search.

The same proof works with any three distinct integer exponents at least
two in (11). The complete statement and all boundary cases are in
[the obstruction note](research/linear-plane-obstruction-pass.md), with
[a separate reconstruction](research/linear-plane-obstruction-audit.md).
No novelty or cancellation-counterexample claim is made.

## 7. Further controls on the symmetry argument

A displayed plane can fail even for commuting nice coordinate actions.
In coordinates \((a,b,z,w)\), set \(v=a-bz\) and
\[
Z=z\partial_a+\partial_b,\qquad
E=bv\partial_a+v\partial_z+\partial_w.
\tag{16}
\]
In the actual frame \((v,b,z,w)\), these are
\(Z=\partial_b\), \(E=v\partial_z+\partial_w\). They are
nice, commute, and have slices. The row of \(Z\) is unimodular.
Yet \(E(z)/E(w)=v\notin\mathbb C(z,w)\). The corresponding
non-unimodular determinant-one control and its full inverse are in
[the normalizer note](research/nice-normalizer-descent-pass.md).

Nor does a free ambient action necessarily descend freely. On
\(\mathbb C[s,x,y,z]\), take
\[
E=\partial_s,\qquad U=\partial_s+x\partial_y.
\tag{17}
\]
Both have slice \(s\), commute, and are coordinate LNDs. On
\(\ker E=\mathbb C[x,y,z]\), however, the second induces
\(x\partial_y\), fixing the divisor \(x=0\). Thus two free
commuting ambient actions do not supply a free intrinsic action.

Finally, the full derivation centralizer of a nonzero LND has maximal
generic rank. With a slice it is the semidirect sum of kernel
multiples of the slice derivation and derivations of the kernel.
These are the precise conclusions of Bedratyuk, Chapovskyi and
Petravchuk's Proposition 2 and Theorem 4.[^6] They do not assert that
the constructed independent derivations are locally nilpotent or
mutually commuting. A full-rank derivation centralizer cannot substitute
for a family of additive actions with the necessary quotient geometry.

The remaining coordinate-partial subclass is itself nontrivial. In
(10), a slice need not have degree at most one in the fixed variable
\(t\). Even when a slice is affine in \(t\), its leading
coefficient need not be a constant or reducible to one by a shear fixing
the base. The [coordinate-partial audit](research/commuting-coordinate-partial-pass.md)
gives exact countercontrols to both shortcuts. They have polynomial
kernels and therefore do not refute the possible recognition theorem.

## 8. Verification and remaining proof obligation

The independent checker
[projective_plane_checks.py](research/projective_plane_checks.py)
contains 25 test methods. They verify two-sided coordinate inverses,
the translation pushforward, slice identities, the symbolic Jacobian
minors for arbitrary plane parameters, normalizer controls, both
plane-row examples, and the fixed-divisor quotient. It imports no
research derivation or solver module. Its command is

```sh
/opt/anaconda3/bin/python research/projective_plane_checks.py
```

The full regression, including the preceding 282 tests, is recorded in
[verification-pass-14.json](verification-pass-14.json). Finite symbolic
tests support the displayed algebra. They do not formally verify the
general source theorems or all polynomial coordinate changes. Separate
model reconstructions are not human expert review.

The current missing step is constructive: for an arbitrary slice LND,
produce an ambient invariant coordinate, or produce an actual
coordinate plane satisfying (5), with its polynomial complements
proved. Section 3 shows why merely restating that existence is not a
proof. Section 6 excludes restricting the search to affine-linear planes.
Section 7 excludes inferring the needed quotient behavior from
commutation alone.

The [mixed-frame theorem](deep-pass-13.md) retains its original
coordinate hypotheses. Its sufficient slice-filtration bound remains
\(H\le9\); the hypothetical minimum-height obstruction remains
\(H_{\min}\ge10\), with the height defined in that report. No
arbitrary slice has been reduced to such a frame. The unrestricted
problem, novelty assessment and human expert review remain unfinished.

## Sources

1. Gene Freudenburg and Lucy Moser-Jauslin. *Locally nilpotent derivations
   of rings with roots adjoined*. Michigan Mathematical Journal 62(2)
   (2013), 227–258. [Author preprint, §2.1, Lemma 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf);
   [published DOI](https://doi.org/10.1307/mmj/1370870372). The author
   preprint is dated July 28, 2010. Indexed original text was accessible;
   direct PDF download failed, and published numbering was not compared.
2. Gene Freudenburg. *Algebraic Theory of Locally Nilpotent Derivations*,
   second edition (2017), [Chapter 5 Appendix, Theorem 5.41 and
   Corollaries 5.42–5.43](https://doi.org/10.1007/978-3-662-55350-3_5).
   The appendix credits its general theorem and proof to Daigle and
   Freudenburg; it identifies Freudenburg's 1996 *A note on the kernel
   of a locally nilpotent derivation*, Theorem 2, as the earlier source.
3. Nikhilesh Dasgupta and Sergey Gaifullin. [*On locally nilpotent
   derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510)
   (2023), Theorem 2.7, recalling Rentschler's plane theorem.
4. Hongdi Huang, Zahra Nazemian, Yanhua Wang and James J. Zhang.
   [*Relative Cancellation*](https://arxiv.org/html/2503.10083v3),
   November 9, 2025 revision, Introduction. Used only for its explicit
   dated status of classical polynomial-ring cancellation.
5. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande.
   [*Some K-theoretic properties of the kernel of a locally nilpotent
   derivation on k[X1,…,X4]*](https://arxiv.org/html/1501.01438v1)
   (2015), Theorem 3.5. Nonzero LND, characteristic zero, an invariant
   ambient variable and a regular kernel are required.
6. L. Bedratyuk, Y. Chapovskyi and A. Petravchuk.
   [*Centralizers of linear and locally nilpotent derivations*](https://arxiv.org/pdf/2302.02441)
   (2023), Proposition 2 and Theorem 4. The centralizer consists of
   arbitrary derivations, not exclusively LNDs.

[^1]: Freudenburg and Moser-Jauslin, [author preprint, Lemma 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf).
[^2]: Freudenburg, [Chapter 5 Appendix, Corollary 5.43](https://doi.org/10.1007/978-3-662-55350-3_5).
[^3]: Rentschler's theorem as recalled in [Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).
[^4]: Huang, Nazemian, Wang and Zhang, [*Relative Cancellation*, Introduction](https://arxiv.org/html/2503.10083v3).
[^5]: Bhatwadekar, Gupta and Lokhande, [Theorem 3.5](https://arxiv.org/html/1501.01438v1).
[^6]: Bedratyuk, Chapovskyi and Petravchuk, [Proposition 2 and Theorem 4](https://arxiv.org/pdf/2302.02441).
