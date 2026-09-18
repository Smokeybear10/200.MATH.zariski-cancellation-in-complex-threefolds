# Projective plane recognition and its construction gap

For a locally nilpotent derivation on an actual polynomial coordinate
plane inside affine space, it is enough that the direction of its two
coefficients descend to that plane. An invariant common multiplier is
not necessary. This is an application of the published quasi-extension
lemma, not a new general recognition theorem. The outstanding global
step is to construct such a coordinate plane from the intrinsic or
highest-flow data.

The invariant-denominator argument in
[the rational-rescale pass, Section 6](height-nine-rational-rescale-pass.md)
is a useful special case. The formulation below removes its invariant
rescaling hypothesis and records exact tests and countercontrols.

## 1. A fixed coordinate plane: equivalent recognition conditions

Let
\[
B=\mathbb C[a,b,z_1,z_2],\qquad R=\mathbb C[z_1,z_2],
\qquad F=\operatorname{Frac}R,
\]
and let \(E\) be an LND of \(B\). The assertion that \(R\) is an
actual coordinate plane means the displayed equality \(B=R[a,b]\),
not just an abstract isomorphism \(R\cong\mathbb C^{[2]}\).
Write \(f_i=E(z_i)\). The following are equivalent:

1. Either \(f_1=f_2=0\), or the projective pair \([f_1:f_2]\) is
   defined over \(F\).
2. There exist \(h\in B\setminus\{0\}\) and \(p,q\in R\),
   allowing both to vanish in the zero case, with
   \(f_1=hp\) and \(f_2=hq\).
3. \(R\cap\ker E\ne\mathbb C\).
4. \(R\) contains a polynomial coordinate of \(R\) killed by \(E\).

The implication from condition 3 to condition 4 is already the exact
coordinate-plane statement in
[Freudenburg, Corollary 5.43](https://doi.org/10.1007/978-3-662-55350-3_5).
Its surrounding Theorem 5.41 treats a more general factorially closed
polynomial two-ring. We give the elementary coefficient proof to make
the hypotheses and the computational tests explicit.

Suppose first that \(f_1,f_2\) are both nonzero. For condition 1,
choose a reduced pair \(p,q\in R\) with
\(f_1/f_2=p/q\). Irreducibles of \(R\) remain prime in
\(B=R[a,b]\), so \(p,q\) remain coprime in \(B\).
The identity \(qf_1=pf_2\) gives
\[
f_1=hp,\qquad f_2=hq,\qquad h\in B.
\tag{1}
\]
This uses prime valuations, not an assertion that two coprime
multivariable polynomials generate the unit ideal. If just one \(f_i\)
vanishes, use the primitive pair \((0,1)\) or \((1,0)\).

Put \(D=p\partial_{z_1}+q\partial_{z_2}\). Then
\[
E(f)=hD(f)\quad(f\in R).
\tag{2}
\]
The quasi-extension lemma says that \(D\) is locally nilpotent when
\(E\) is. It requires neither \(E(h)=0\) nor finite generation of
the ambient domain: see
[Freudenburg and Moser-Jauslin, Lemma 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf),
published in *Michigan Mathematical Journal* 62 (2013), 227–258,
[DOI 10.1307/mmj/1370870372](https://doi.org/10.1307/mmj/1370870372).

Here is the degree argument. For nonzero \(f\in B\), let
\(\nu_E(f)=\max\{j:E^j(f)\ne0\}\). Product degrees add in a
characteristic-zero domain. Whenever \(Df\ne0\), equation (2) gives
\[
\nu_E(Df)=\nu_E(f)-\nu_E(h)-1.
\tag{3}
\]
Every nonzero successive iterate of \(D\) therefore strictly lowers
a nonnegative integer, proving local nilpotence. More precisely,
\(\nu_D(f)\le\lfloor\nu_E(f)/(\nu_E(h)+1)\rfloor\) for
nonzero \(f\in R\).

Rentschler's theorem supplies a plane coordinate \(u\) killed by
the nonzero \(D\), hence by \(E\); its exact triangularization
statement is recalled in
[Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510).
If \(D=0\), either displayed plane coordinate works. Conversely,
an invariant \(u\in R\setminus\mathbb C\) gives
\[
u_{z_1}f_1+u_{z_2}f_2=0.
\]
At least one derivative is nonzero. If both \(f_i\) are nonzero,
this expresses their ratio in \(F\); if one vanishes, condition 1
is immediate. This proves all four equivalences.

For the primitive pair in (1), the plane LND \(D\) is irreducible.
Rentschler then makes \(D\) a nonzero constant multiple of a coordinate
partial. In particular \((p,q)=R\) is a consequence of local
nilpotence and primitivity, not an input to the argument. If \(E\)
does not vanish on \(R\), the same argument gives
\(R\cap\ker E=\mathbb C[u]\).

## 2. Exact projectability and rescaling tests

For the nonzero pair \((f_1,f_2)\), condition 1 is equivalent to
\[
f_2\partial_a f_1-f_1\partial_a f_2=0,
\qquad
f_2\partial_b f_1-f_1\partial_b f_2=0.
\tag{4}
\]
When one coefficient is zero these equations and condition 1 both hold.
Otherwise they say that \(f_1/f_2\) is killed by both vertical
partials. The common constant field of these partials on
\(F(a,b)\) is exactly \(F\).

Equivalently, for \(T=\partial_a,\partial_b\), the horizontal
coefficient pair of \([T,E]\) is proportional to that of \(E\)
over \(\operatorname{Frac}B\). Thus
\([T,E]-\lambda_T E\) is vertical for some rational \(\lambda_T\).
This is projectability of a direction, not preservation of \(R\)
by \(E\). Local nilpotence supplies the polynomial integration in
Section 1; a separate Frobenius assertion is unnecessary for this
already-given coordinate plane.

For a prescribed nonzero invariant \(g\in\ker E\), the stronger
condition
\[
\delta=E/g\text{ preserves }F
\tag{5}
\]
is equivalent to \(f_i/g\in F\), or to the four equations
\[
g\partial_a f_i-f_i\partial_a g=0,
\qquad
g\partial_b f_i-f_i\partial_b g=0
\quad(i=1,2).
\tag{6}
\]
It implies (4), but the converse need not hold even for some choice
of invariant \(g\), as Section 4 shows.

One can recover the original denominator proof directly. Write
\[
\delta z_i=p_i/d,\qquad p_i,d\in R,
\qquad \gcd(d,p_1,p_2)=1.
\]
For each prime factor of \(d\), some numerator has valuation zero.
Polynomiality of \(E(z_i)=gp_i/d\) therefore gives \(d\mid g\)
in \(B\), with multiplicity. Factorial closure of \(\ker E\)
implies \(E(d)=0\). Hence the polynomial plane derivation
\(\Delta=d\delta|_R\) satisfies
\[
\Delta^j f=d^jg^{-j}E^jf\quad(f\in R)
\]
and is locally nilpotent. This is sufficient, but Section 1 shows
that invariant denominator clearing is not necessary for recognition.

## 3. The slice consequence and the exact global gap

If \(E\) has a slice \(s\), put \(K=\ker E\). The slice theorem
gives \(B=K[s]\), and \(K\) is regular. An ambient invariant
coordinate \(u\) puts \(E\) in
\(\operatorname{LND}_{\mathbb C[u]}(\mathbb C[u]^{[3]})\).
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
then gives \(K=\mathbb C[u]^{[2]}\cong\mathbb C^{[3]}\).

For a slice derivation on \(\mathbb C^{[4]}\), the following existence
statements are therefore equivalent:

- Some actual coordinate plane has projectable coefficient direction.
- Some actual coordinate plane contains a nonconstant invariant.
- \(E\) kills an ambient polynomial coordinate.
- \(\ker E\cong\mathbb C^{[3]}\).

The reverse of the last implication uses \(B=K[s]\): polynomial
generators of \(K\), together with \(s\), are ambient coordinates.
An invariant ambient coordinate can always be extended to a coordinate
plane. Thus constructing a suitable plane for every slice derivation
is not an automatically weaker substitute for the recognition goal.

An abstract polynomial subring or an integrable rational distribution
does not by itself provide the required embedding. For example,
\(\mathbb C[z,zw]\subset\mathbb C[z,w,a,b]\) is abstractly a plane
ring but is not a coordinate factor: its fraction field contains
\(w\in B\) although \(w\notin\mathbb C[z,zw]\). A coordinate
factor \(R\subset R[a,b]\) satisfies \(B\cap\operatorname{Frac}R=R\).
This elementary example is not meant to model every additional
factorial-closure or flatness property of an intrinsic quotient.

The unresolved construction needs actual polynomial complementary
coordinates, or a theorem producing an ambient coordinate directly.
Ranks of coefficient maps, abstract polynomial kernels, and commuting
intrinsic LNDs cannot simply be substituted for that input.

## 4. Projectable direction without any invariant rescaling

In \(B=\mathbb C[a,b,z_1,z_2]\), take
\[
E=\partial_a+a\partial_{z_1}+az_1\partial_{z_2}.
\tag{7}
\]
This is triangular and has slice \(a\). On the displayed plane,
\[
E|_R=aD,\qquad D=\partial_{z_1}+z_1\partial_{z_2},
\]
so its direction descends, but its multiplier does not satisfy
\(E(a)=0\). The plane coordinate
\(v=z_2-z_1^2/2\) is invariant. In fact
\[
u=z_1-a^2/2,\qquad v=z_2-z_1^2/2,
\qquad B=\mathbb C[u,v,b,a],
\]
with inverse \(z_1=u+a^2/2\), \(z_2=v+(u+a^2/2)^2/2\).

There is no nonzero invariant polynomial \(g\) for which \(E/g\)
preserves \(\operatorname{Frac}R\). Indeed \(a/g\in F\) would
force \(g=ar\) with \(r\in R\): intersect \(B\) with the
one-dimensional \(F\)-space \(aF\). Then
\[
E(g)=r+a^2D(r),
\]
whose constant term as a polynomial in \(a\) is \(r\ne0\).
Thus invariant rescaling is genuinely a stronger fixed-plane condition.

## 5. A commuting nice partial does not pick the right plane

In physical coordinates \((a,b,z,w)\), put
\[
v=a-bz,\qquad
Z=z\partial_a+\partial_b,
\qquad
E=bv\partial_a+v\partial_z+\partial_w.
\tag{8}
\]
The actual coordinates \((v,b,z,w)\), with inverse \(a=v+bz\),
give \(Z=\partial_b\) and \(E=v\partial_z+\partial_w\).
Both fields are nice LNDs, both have slices, and they commute.
The row of \(Z\) is primitive and even unimodular.

Nevertheless, on the displayed complementary plane \(R=\mathbb C[z,w]\),
\[
\frac{E(z)}{E(w)}=a-bz,
\qquad \partial_a\left(\frac{E(z)}{E(w)}\right)=1.
\]
Thus this plane fails the direction criterion. No rescaling can make
its two coefficients belong to \(F\): since \(E(w)=1\), such a
scale would itself lie in \(F\), while \(v\notin F\).
The example still fixes the ambient coordinate \(b\), so another
plane works. It refutes an automatic displayed-plane construction,
not the possible existence of a different plane.

The separate
[nice-normalizer descent note](nice-normalizer-descent-pass.md)
also treats a primitive non-unimodular row. Its quotient can be an
abstract polynomial three-ring without being a coordinate three-factor.
These embedding distinctions survive even when commutation is proved.

## 6. Highest coefficients do not make their parameter a coordinate

For any integer \(N\ge1\), consider
\[
E_N=\partial_a+a^Nzw\partial_b
\quad\text{on }\mathbb C[a,b,z,w].
\tag{9}
\]
It is a primitive slice LND. Its highest nonzero flow iterate, in
degree \(N+1\), is
\[
E_N^{N+1}(a,b,z,w)=(0,N!zw,0,0).
\]
The invariant parameter \(zw\) is not an ambient coordinate, because
its gradient vanishes along \(z=w=0\). Thus even a one-dimensional
highest-coefficient image does not make a displayed parameter a
coordinate. Here an invariant plane exists for the independent reason
that \(z,w\) are fixed.

In general, division of a highest-coefficient vector by a common factor
also requires a fresh commutator check. The primitive quadratic control
in [the power-law pass](height-nine-power-law-pass.md) explicitly shows
that the resulting constant direction need not commute with \(E\).

## 7. Independent audit of the all-affine-linear-plane control

The following control was constructed in the parent pass. Begin with
coordinates \((A,B_0,C,s)\) and set
\[
x_1=A+s^2,\quad x_2=B_0+s^3,\quad x_3=C+s^4,
\quad x_4=s+x_1x_2.
\tag{10}
\]
The inverse is \(s=x_4-x_1x_2\) followed by subtraction of its powers.
Consequently \(E=\partial_s\) in the original frame is a slice LND
with polynomial kernel and displayed coefficients
\[
(Ex_1,Ex_2,Ex_3,Ex_4)
=(2s,3s^2,4s^3,1+2x_2s+3x_1s^2).
\tag{11}
\]
No plane generated by two independent affine-linear forms in the
displayed \(x\)-frame has projectable direction.

If the forms avoid \(x_4\), their coefficient images under \(E\)
are independent combinations of \(s,s^2,s^3\), so their ratio is
a nonconstant rational function of \(s\). Varying \(x_4\) fixes
the plane coordinates but varies \(s\) freely, which excludes
projectability.

Otherwise choose a basis of affine-linear plane generators of the form
\[
U=x_4+\alpha x_1+\beta x_2+\gamma x_3+\epsilon,
\quad V=\ell_1x_1+\ell_2x_2+\ell_3x_3+\eta,
\]
where the vector \(\ell\) is nonzero. The ratio \(EU/EV\) has a
pole along the prime \(s=0\), since \(EU\equiv1\pmod{s}\)
and \(EV\ne0\) is divisible by \(s\). If this ratio belonged to
\(\mathbb C(U,V)\), some nonzero polynomial denominator \(Q(U,V)\)
would vanish modulo \(s\).

But on \(s=0\), the two restrictions are
\[
U_0=x_1x_2+\alpha x_1+\beta x_2+\gamma x_3+\epsilon,
\quad V_0=\ell_1x_1+\ell_2x_2+\ell_3x_3+\eta.
\]
They are algebraically independent. If they were dependent, the linear
coordinate \(V_0\) would force \(U_0\in\mathbb C[V_0]\).
Its degree-two part would then be a scalar multiple of the square
of a linear form, whereas \(x_1x_2\) is a quadratic form of rank two.
Hence no such denominator vanishes, a contradiction.

This audit confirms the parent argument, including its pole orientation.
By Section 1, it also excludes every nonconstant invariant polynomial
in every affine-linear plane algebra in this frame. It does not exclude
nonlinear coordinate planes: the original \(A,B_0,C\) are explicit
invariant ambient coordinates.

The separate [linear-plane obstruction audit](linear-plane-obstruction-audit.md)
gives the shorter direct invariant proof. It checks all three symbolic
Jacobian minors of \((U_0,V_0)\), then uses \(EU|_{s=0}=1\) and
\(EV|_{s=0}=0\) to force any invariant polynomial \(P(U,V)\) to
be constant. No finite-grid check of plane coefficients is used.

## 8. Verification boundary

The general proofs above are algebraic arguments and applications of
the cited theorems. Symbolic controls verify polynomial identities and
chosen examples; they are not a search over all coordinate planes or
a proof that an arbitrary slice derivation admits one.

An independent inline SymPy run using `/opt/anaconda3/bin/python`
passed 18 grouped exact checks in 0.153 seconds. They cover the
two-sided inverses, LND degrees and degree decrement, the failed
invariant-rescale identity, both commuting nice fields, the
nonprojectable ratio, the highest coefficient and its critical
parameter, and the all-affine-linear-plane control's coefficient and
Jacobian-minor identities. No research-module code was imported.
