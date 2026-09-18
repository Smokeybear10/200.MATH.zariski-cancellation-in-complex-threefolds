# The actual slice gives strict acceleration containment

In the actual rank-one quadratic sliced setting, the acceleration has
a power in the next power of the good-speed ideal. If the supplied
slice has degree D in the three good coordinates, then for a proper
speed ideal and nonzero acceleration, D>=2 and one may take
N=(D-1) squared. This strengthens the pass83 integral-closure result
without using a valuative criterion or Briancon--Skoda.

The conclusion is strict, or inner, integral containment.[^terminology] It does not
in general imply membership in the original ideal. No actual
counterexample to that membership is constructed here.

## 1. Actual hypotheses and a return fixing the fourth coordinate

Retain the actual polynomial coordinates and the original supplied
polynomial slice:
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\qquad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Write a_i=E(x_i), b=E(z), and I=(a_1,a_2,a_3)B. When q=0 or
I=B, the ideal conclusions are immediate. Assume henceforth q is
nonzero and I is proper. The slice equation gives
\[
1=\sum_{i=1}^3a_i\partial_i s+b\partial_zs,
\qquad b\in(B/I)^*.
\tag{2}
\]
In particular b is a nonzero polynomial. No reduction of B/I is made.

The actual flow is Phi_t=(x+t a,z+t b+t squared q/2). Substitute
the rational time -2b/q into its polynomial identities, now without
specializing z. This produces the rational map
\[
\rho(x,z)=\left(x-\frac{2b}{q}a,z\right),\qquad
a(\rho)=a,\quad q(\rho)=q,\quad b(\rho)=-b,\quad
s(\rho)-s=-\frac{2b}{q}.
\tag{3}
\]
The identities use E(a_i)=E(q)=0, E(b)=q, and E(s)=1. In
particular rho fixes the original coordinate z exactly and squares
to the identity as a rational map. This does not make rho regular
on q=0, and does not declare a rationally rescaled derivation to be
locally nilpotent.

## 2. The stronger monic equation from the supplied slice

Let D be the degree of s as a polynomial in x_1,x_2,x_3 over
the coefficient ring C[z]. For 1<=k<=D define frozen directional
Taylor coefficients
\[
H_k=\sum_{i_1,\ldots,i_k=1}^3
a_{i_1}\cdots a_{i_k}
\partial_{i_1}\cdots\partial_{i_k}s\in I^k,
\qquad U=1-H_1=b\partial_zs.
\tag{4}
\]
The derivatives act only on s, holding z fixed. The a_i are
evaluated at the original point; derivatives of them do not enter
H_k. These coefficients are not iterates of sum a_i partial_i.

If D=0, the final identity in (3) is impossible. If D=1, its
Taylor expansion gives H_1=1, contradicting properness of I.
Thus D>=2. Expanding (3) in the good variables, dividing by
the nonzero rational time, and clearing the remaining q powers gives
\[
Uq^{D-1}
=\sum_{k=2}^{D}\frac{(-2b)^{k-1}}{k!}
H_kq^{D-k},\qquad U\equiv1\pmod I.
\tag{5}
\]
The last congruence means that localization at U does not lose any
point of the speed scheme. It does not assert U is a unit of B.

Put m=D-1 and J=IB_U. Dividing (5) by U gives a monic degree-m
equation of the form
\[
q^m=\sum_{j=1}^{m}c_jq^{m-j},\qquad
c_j=\frac{(-2b)^j}{(j+1)!U}H_{j+1}\in J^{j+1}.
\tag{6}
\]
The additional ideal power, j+1 instead of j, is the point of using
the actual slice identity. Equation (6) is obtained in the actual
localized polynomial ring, not in a formal quotient model.

## 3. A uniform finite reduction and descent

Set N=m squared. Repeatedly use (6) to reduce q^N to a sum of
terms with remaining q exponent r<m. A substitution using c_j
reduces that exponent by j, where 1<=j<=m, and contributes at least
j+1 powers of J to its coefficient.

For any resulting term, the total exponent reduction is N-r and
the number L of substitutions satisfies mL>=N-r. Since
N-r>=m squared-m+1, one has L>=m. The coefficient therefore
belongs to J to the power N-r+L, which is at least N+1.
The remaining factor q^r belongs to B_U and causes no loss of ideal
membership. Consequently q^N belongs to J^(N+1).

To contract this statement, U=1-H_1 is a unit modulo I^(N+1):
the finite geometric sum of powers of H_1 gives an inverse there.
Hence I^(N+1)B_U intersects B in exactly I^(N+1). We obtain
\[
\boxed{
q^{(D-1)^2}\in I^{(D-1)^2+1}.
}
\tag{7}
\]
This is a direct ideal-power statement in B. No transfer of a
representative modulo I is involved. Such a transfer would be
insufficient: adding an arbitrary element of I can destroy a strict
power property.

In particular, if the supplied slice has good-variable degree two,
then q belongs to I squared. If D<=1 and I is proper, the
nonzero-acceleration branch is impossible. The degree used here is
the good-variable degree of the actual supplied slice, not the
coordinate time degree, spatial degree of E, or an optimized degree
after an unproved coordinate change.

## 4. Valuation interpretation and its exact limitation

For any valuation v of Frac(B) nonnegative on B, (7) implies
\[
v(I)>0\quad\Longrightarrow\quad v(q)>v(I).
\tag{8}
\]
Indeed N v(q)>N v(I) follows from
N v(q)>=(N+1)v(I)>N v(I), in any ordered value group.
This interpretation requires no theorem characterizing which
valuations suffice for integral closure.

It can also be checked directly from (3). If v(I)>0, (2) makes
b a valuation unit. If 0<v(q)<=v(I), every component of rho is
valuation-integral, whereas s(rho)-s=-2b/q has negative value.
If v(q)=0<v(I), rho is congruent to the identity modulo the
valuation maximal ideal, so the same polynomial difference has
positive value while its prescribed value is a unit. Both cases
are impossible. This independent check uses the original polynomial
slice, not an arbitrarily chosen local flow parameter.

There is a stronger divisorial consequence than pass82's q in (g),
where g is the coefficient gcd of the nonzero good-speed ideal.
For any irreducible p dividing g, put e=ord_p(g)>0. Equation (7)
gives ord_p(q)>=e+ceil(e/N), in particular ord_p(q)>=e+1.
Thus q is divisible by g times the product of its distinct
irreducible factors. If g is a unit this asserts nothing new.
The actual [pass81 control](rank-one-acceleration-shear-boundary-pass81.md),
after renaming its last coordinate z, has
E=a squared partial_x+(1+ax)partial_z, g=a squared and q=a cubed.
Its full polynomial inverse and supplied slice are proved there.
It attains the one-additional-copy bound for that gcd; no sharpness
claim is made for every multiplicity or slice degree.

The strict conclusion alone cannot prove first-power membership.
For an elementary bare ideal control, in C[u,v,w] take
\[
K=(u^3,v^3),\qquad h=u^2v^2.
\qquad h^3=u^6v^6\in K^4,\qquad h\notin K.
\tag{9}
\]
The last assertion is monomial ideal membership. The zero set is
a line, not an isolated point, and h squared already belongs to K.
Thus this control is compatible with the known cubic and square
ideal-power bounds as abstract ideal data. It supplies no original
action, slice, or return identity realizing these polynomials as
actual speeds and acceleration.

## 5. Relation to the preceding work

The [pass83 return note](rank-one-return-map-integral-closure-pass83.md)
used the velocity sign change to prove ordinary ideal-integrality,
then applied the precisely scoped Briancon--Skoda theorem. Here the
additional original-slice identity yields the stronger coefficient
orders in (6), and the finite reduction proves (7) elementarily.
The [embedded-support note](rank-one-square-embedded-support-pass84.md)
gives a separate conditional square-membership statement; this proof
does not remove its possible embedded critical support in general.

Geometry identified the slice return identity and strict valuation
inequality. Root proposed applying the return map directly on B,
fixing the original z, which removes an invalid representative
transfer. Geometry derived the finite m-squared reduction bound.
All arguments above are ordinary polynomial, localization, and
ideal computations, with no new classification or source theorem.

This is an AI-checked working proof, not a human expert audit,
formal verification, or novelty finding. No numerical suite,
actual counterexample to q in I, coordinate-lowering construction,
or general cancellation result is claimed. All pass83 and earlier
files remain unchanged.

[^terminology]: Epstein and Hochster, [*Continuous Closure, Axes Closure,
    and Natural Closure*](https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/08/CnClTAMS.pdf),
    printed pp. 20--21: the definition immediately before Theorem 5.4
    and condition (3) identify this power property with inner integral
    closure, denoted I_{>1}. The exact definition and the complete
    displayed statement and proof of Theorem 5.4 were read for
    terminology. Its equivalence theorem and preceding valuation
    dependencies are not inputs to the elementary proof above.
