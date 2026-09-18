# Actual shears close the classified three-output cubic residual

The new relative-plane relation in the degree-five residual admits
an actual polynomial coordinate shear that reduces its rational nice
symmetry to two output directions. One genuine good partial survives
the shear. That is enough for the denominator and coordinate-descent
argument, even when the rational symmetry itself is not polynomial.

This is a recognition proof for the supplied frame, using the complete
[relation classification](three-output-cubic-speed-pass41.md) stated
in Section 2. It does not assert that every
sliced action admits the supplied one-cubic frame, and it does not
solve general threefold cancellation. The relation classification
and this deduction have separate proof and source obligations.

## 1. A recognition lemma requiring only one good partial

Let
\[
B=\mathbb C[u,v,a,b],\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1,
\quad 0\ne g\in\ker E.
\tag{1}
\]
Suppose an actual LND of \(B_g\) has the form
\[
Z=\partial_b+F\partial_a,\qquad Z^2a=0,
\qquad [E,Z]=0,
\qquad g^N Z(B)\subset B
\tag{2}
\]
for some integer \(N\ge0\). Assume the single actual coordinate
partial \(P_a=\partial_a\) satisfies
\[
[E,[E,P_a]]=0.
\tag{3}
\]
Then \(E\) fixes an actual coordinate of \(B\), and
\(\ker E\simeq\mathbb C^{[3]}\).

This extracts precisely the ingredients used in the
[two-output proof](two-output-cubic-closure-pass40.md). It does not
require three good partials in the new frame.

### The actual flow and the denominator invariant

Because \(Z^2a=0\), its genuine localized flow is
\((u,v,a,b)\mapsto(u,v,a+tF,b+t)\). Its Jacobian determinant is
\(1+tF_a\). The determinant is a unit of \(B_g[t]\); units do
not depend on \(t\), and its value at zero is one. Thus
\(F_a=0\). The identity \(ZF=0\) now gives \(F_b=0\), so
\[
F\in\mathbb C(u,v).
\tag{4}
\]
This uses the actual inverse flow, not a Jacobian criterion for a
proposed coordinate map.

Put \(S=\mathbb C[u,v]\), and write \(F=N_0/D\) with
coprime \(N_0,D\in S\), \(D\ne0\). When \(F=0\), take
\(N_0=0,D=1\). Polynomiality in (2) gives \(D\mid g^N\)
in the UFD \(B\). Factorial closure of \(\ker E\) gives
\(E(D)=0\). Consequently
\[
W_0=DZ=D\partial_b+N_0\partial_a,
\quad [E,W_0]=0,
\quad J=Da-N_0b.
\tag{5}
\]
The polynomial derivation \(W_0\) is primitive, nice and locally
nilpotent. No unit-ideal conclusion is inferred from coprimality.

### Exact kernel contraction and the descended good partial

One has
\[
R:=\ker W_0=S[J]\simeq\mathbb C^{[3]}.
\tag{6}
\]
After inverting \(D\), this is the ordinary coordinate calculation
with \(a=(J+N_0b)/D\). For each irreducible \(\pi\mid D\),
the substitution \(J\mapsto-\overline{N_0}b\) induces an
injection
\[
(S/(\pi))[J]\longrightarrow (S/(\pi))[a,b],
\]
since \(\overline{N_0}\ne0\). An element of \(S_D[J]\cap B\)
with a minimal positive pole at \(\pi\) contradicts this injection
after multiplication by that pole and reduction. Localizing away
from \(\pi\) allows the argument to remove every denominator,
including repeated factors. This proves (6).

Commutation lets \(L=E|_R\) act as an LND on the actual polynomial
three-ring \(R\). The partial \(P_a\) commutes with \(W_0\)
and restricts to \(D\partial_J\). Because \(L(D)=0\), (3)
gives, after cancellation of \(D\ne0\),
\[
[L,[L,\partial_J]]=0.
\tag{7}
\]
If \(L=0\), \(u\) is already an invariant ambient coordinate.
Assume below that \(L\ne0\), and put \(U=[L,\partial_J]\).
The actual conjugation
\(\exp(tL)\partial_J\exp(-tL)=\partial_J+tU\) is an LND
on \(R[t]\). For any fixed polynomial, the top coefficient in
a sufficiently high iterate proves local nilpotence of \(U\).
Also \([L,U]=0\).

### The independent and dependent commuting cases

If \(L,U\) are independent over \(\operatorname{Frac}R\),
Maubach's commuting-LND theorem gives
\[
\ker L\cap\ker U=\mathbb C[p],
\quad p\text{ a coordinate of }R.
\tag{8}
\]
Its hypotheses are the actual polynomial three-ring and commuting
independent LNDs.[^commuting]

If \(D\) is a unit, \(B=R[b]\) with the explicit inverse
\(a=D^{-1}(J+N_0b)\). Thus \(p\) is already an ambient
coordinate. If \(D\) is nonconstant, \(L,U\) both kill \(D\),
so \(D=H(p)\) for a nonconstant complex polynomial \(H\).
Since \(D\in S\), comparison of degrees in \(J\) forces
\(p\in S\). Now \(S[J]=\mathbb C[p]^{[2]}\) as
\(\mathbb C[p]\)-algebras. Hamann's relative cancellation
theorem gives \(S=\mathbb C[p]^{[1]}\).[^hamann] Thus \(p\)
is an actual coordinate of \(S\), hence of \(B\).

If instead \(U=hL\) over the fraction field, including \(U=0\),
the equality \(U=-\partial_J L\) shows that every nonzero ratio
of coefficients of \(L\) lies in \(\operatorname{Frac}S\).
Divide the coefficient vector of \(L\) by its polynomial gcd.
The resulting primitive derivation \(L_0\) is an LND with the
same kernel. Clear the coefficient ratios in \(S\), remove
their gcd there, and compare valuations with this primitive vector
in \(S[J]\). Primitivity forces the proportionality factor to be
a global unit, hence complex constant. All coefficients of
\(L_0\) therefore lie in \(S\).

It follows that \(L_0\) preserves \(S\). If the restriction
is zero, use \(u\). Otherwise Rentschler's theorem supplies
a coordinate \(p\) of \(S\) killed by the restriction.[^plane]
It is killed by \(L\) and is an ambient coordinate of \(B\).
This dependent case does not need the nonconstant invariant \(D\).

In all cases \(E\) fixes an actual ambient coordinate. Its
kernel is regular because \(B=(\ker E)[s_*]\) is regular.
The regular-kernel theorem of Bhatwadekar, Gupta and Lokhande
then gives \(\ker E\simeq\mathbb C^{[3]}\).[^regular]
The argument never transfers a slice from \(E\) to \(W_0\)
or to \(E|_R\).

## 2. Exact classified inputs for the three-output residual

Use the genuine degree-five notation from
[pass 40](cubic-degree-five-pass40.md), in the remaining case
that \(c,d,e\) are independent. The constant invariant-for-\(Z\)
linear coordinate \(w\), together with actual linear coordinates
\((a,b,z)\), is normalized so that
\[
T_c=\partial_a,\quad T_d=\partial_b,\quad T_e=\partial_z,
\quad x_4=\lambda z,
\quad
Z=\partial_z+\frac\sigma3\partial_b+
\left(\frac{\sigma^2}{12}+\frac{\tau}{3\lambda}\right)\partial_a.
\tag{9}
\]
Here \(\delta=E/g\), \(\delta\sigma=1\), \(\delta\tau=0\),
\(Z\sigma=Z\tau=Zw=Zg=0\), and \(\tau\) is nonconstant.
The original-slice unit lemma makes \(Z\) an actual LND of
\(B_g\), and \(g^4Z\) is polynomial and commutes with \(E\).
The partials \(\partial_a,\partial_b,\partial_w\) are all
good constant directions for \(E\).

The [relative relation classification](three-output-cubic-speed-pass41.md)
supplies
\(\delta w=\nu\sigma+\kappa\), with complex \(\nu,\kappa\)
not both zero, and the following exhaustive alternatives:

1. If \(\nu\ne0\), then, for a complex constant \(a_0\),
   \[
   \tau=\frac\lambda{2\nu}
       \left(w-\kappa\sigma-\frac\nu2\sigma^2\right)+a_0.
   \tag{10}
   \]
2. If \(\nu=0\) and the quadratic coefficient in the relative
   relation is nonzero, then \(\kappa\ne0\) and
   \[
   \tau=-\frac\lambda4\left(\sigma-\frac w\kappa\right)^2
          +b_0\left(\sigma-\frac w\kappa\right)+a_0
   \tag{11}
   \]
   for complex constants \(a_0,b_0\).
3. If that quadratic coefficient is zero, then
   \(\kappa\ne0\) and \(\sigma=w/\kappa+\eta\),
   with \(\eta\in\mathbb C\).

Only these exact algebraic alternatives, not a presumed polynomial
quotient or an unproved division \(g\mid E\), are used below.

## 3. Nonconstant first speed: an actual shear preserves a good partial

Assume \(\nu\ne0\), and set
\[
A(w)=\frac w{6\nu}+\frac{a_0}{3\lambda},\qquad
a'=a+\frac\kappa{2\nu}b-A(w)z.
\tag{12}
\]
This is an actual polynomial coordinate change, with inverse
\(a=a'-\kappa b/(2\nu)+A(w)z\), fixing \(w,b,z\).
Equation (10) gives
\[
\frac{\sigma^2}{12}+\frac\tau{3\lambda}
   =A(w)-\frac\kappa{6\nu}\sigma.
\tag{13}
\]
Consequently \(Za'=Zw=0\), and in the genuine coordinates
\((w,a',b,z)\),
\[
Z=\partial_z+\frac\sigma3\partial_b.
\tag{14}
\]
This derivation remains nice on these generators. Polynomiality
of \(g^4Z\) survives the polynomial coordinate change, as do
commutation and the genuine localized LND property.

Most importantly, the new coordinate partial in (14) is
\[
\partial_b\big|_{w,a',z}
=\partial_b\big|_{w,a,z}
 -\frac\kappa{2\nu}\partial_a\big|_{w,b,z}.
\tag{15}
\]
This is a constant combination of original good partials, so
its second iterated \(E\)-adjoint vanishes. The lemma in
Section 1 applies with base \(\mathbb C[w,a']\), fiber variables
\((b,z)\), and coefficient \(\sigma/3\). It proves polynomiality
of the original kernel without assuming that \(\sigma\) or
\(Z\) is globally polynomial.

## 4. Constant first speed: one alternative is impossible, the other shears

Suppose \(\nu=0\), so \(\delta w=\kappa\ne0\).
For any original good constant partial \(T_i\), put
\(W_i=[\delta,T_i]\). Since \(w\) is a linear coordinate,
\(T_iw\) is constant, and therefore \(W_iw=0\).
The actual good-column identities already give
\[
W_i\sigma=0,\qquad W_i\tau=-\frac\lambda2T_i\sigma.
\tag{16}
\]
In alternative (11), \(W_i\) kills \(\sigma-w/\kappa\),
hence kills \(\tau\). Thus every good \(T_i\sigma=0\).
The rational cubic-field argument in pass 40 proves that at least
one such derivative is nonzero. Alternative (11) is impossible.

In the remaining alternative, \(\sigma=w/\kappa+\eta\) is
polynomial. Make the actual shear
\[
b'=b-\frac\sigma3z,
\quad b=b'+\frac\sigma3z.
\tag{17}
\]
It fixes \(w,a,z\), and \(Zb'=Zw=0\). Hence in the genuine
coordinates \((w,b',a,z)\),
\[
Z=\partial_z+
\left(\frac{\sigma^2}{12}+\frac\tau{3\lambda}\right)\partial_a.
\tag{18}
\]
The new fiber partial \(\partial_a\) is exactly the original
good \(T_c\), because (17) is independent of \(a\).
The recognition lemma applies with base \(\mathbb C[w,b']\).
This closes the last classified alternative.

## 5. Scope and verification boundary

Combining the complete relative relation classification with the
actual shears above, every
three-output degree-five residual in (9) has polynomial original
kernel. Together with the previously proved constant-factor and
two-output cases, this closes the degree-five part of the supplied
one-cubic frame. The degree-six branch was handled separately.

The proof uses an actual inverse shear and retains one exact good
partial. It does not infer coordinates from a unit Jacobian, replace
the original kernel by an auxiliary kernel, or discard the divisor
\(g=0\). The residual classification and this global recognition
argument require independent mathematical audits; finite algebraic
controls alone do not prove their universal quantifiers.

No novelty, human expert review, Lean verification, universal frame
existence, or general cancellation solution is claimed.

## Exact controls and independent proof audits

The complete proof was independently reconstructed by both the
other algebra investigator and the geometry investigator. Both
audits were clean, including the one-good-partial quantifier,
all denominator factors, the independent and dependent commuting
cases, and both exact coordinate shears. The source gates were
read separately from the finite controls.

The standalone
[three_output_cubic_closure_checks_pass41.py](three_output_cubic_closure_checks_pass41.py)
uses only `unittest` and `sympy`. Its six methods verify the two
universal shear inverses and transported partials, two actual
rational nice models with both localized flow inverses, a genuine
sliced action whose good partials survive both shears, and a
repeated-denominator nonunimodular kernel illustration. The first
run passed all six methods in 0.128 seconds with no assertion
failure. No example is claimed to realize the full degree-five
residual. These finite controls do not verify Hamann's theorem,
the global kernel-contraction quantifier, or the complete source
classification by machine.

## Primary recognition inputs

[^commuting]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 3.6 and its proof, with Proposition 3.5, PDF pp. 4-5. These were directly reread from the retained author manuscript. The theorem concerns commuting polynomially independent LNDs of the actual complex three-variable polynomial ring.

[^hamann]: Hamann's relative cancellation theorem, stated with its attribution as Theorem 2.6 in Dasgupta and Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), PDF p. 4. The complete statement was directly reread: the base is any ring containing the rationals, and the displayed polynomial isomorphism must be over that base. Here the base is exactly \(\mathbb C[p]\).

[^plane]: Rentschler's theorem, stated as Theorem 2.7 in Dasgupta and Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), PDF p. 6. The complete statement was directly reread and is applied only to a nonzero polynomial LND of the actual plane \(S\).

[^regular]: Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and its complete proof, PDF p. 11, directly reread. An invariant ambient coordinate and a regular original kernel are established before this theorem is applied.
