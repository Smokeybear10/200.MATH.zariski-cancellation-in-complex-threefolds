# Polynomial coefficient classification and the remaining cancellation gap

## Result

For one canonical primitive rank-three derivation, every extension whose
added coefficient is polynomial in the two invariants and a chosen local
slice now has an exact classification. Two monic polynomial remainders
decide whether a slice exists. Every positive case has an explicit finite
construction of global polynomial coordinates. The negative cases are
excluded in every slice degree, not by a bounded search.

A separate result reduces the number of generators of the fixed pinched
surface from five to four. Two proposed ways to reach unrestricted
cancellation are also resolved at their precise failure points: a
canonical deformation's chosen natural horizontal derivation need not be
locally nilpotent, and restriction of an ambient locally nilpotent derivation
to the slice section requires an invariance condition that is not automatic.

These are working mathematical results with written proofs and independent
model reconstructions. They do not prove
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
The professor has not yet confirmed this corrected interpretation of
the originally pasted statement. Mathematical priority, human review,
and proof-assistant verification remain unresolved.

In plain terms, the completed classification handles every member of
one specified class. The missing cancellation argument would have to
show that every possible variety in (1) can be handled, including those
that need not admit this particular presentation.

## 1. An exact decision rule for the larger coefficient class

Let R=C[x,y,z], fix n>=1, and define
\[
\begin{gathered}
f=xz-y^2,\qquad a=f^n,\qquad \nu=2n+1,\\
r=x^3+ay,\qquad h=a^2z+2ax^2y+x^5,\\
D=-\operatorname{Jac}(f,h,\cdot),\qquad p=ah.
\end{gathered}
\tag{2}
\]
The established canonical construction gives
\[
\ker D=\mathbb C[f,h],\qquad Dr=p,\qquad Dx=2ar,\qquad
xh=r^2+f^\nu.
\tag{3}
\]
The base construction and its known n=1 degree-module description
are inherited results, not claimed as new.[^1]

For any b in C[f,h,r], put
\[
E=D+b\partial_t,\qquad
F(f,h,r)=\int_0^r b(f,h,v)\,dv,\qquad c=b(0,0,0).
\tag{4}
\]
Here the integral is just a polynomial antiderivative with zero
r-constant term. The derivation E is locally nilpotent.

**Classification.** E has a polynomial slice if and only if c is
nonzero and its monic remainders satisfy
\[
\begin{aligned}
F(0,h,r)\bmod(r^5-h^3)&=cr+H_f(h),\\
F(f,0,r)\bmod(r^2+f^\nu)&=cr+H_h(f).
\end{aligned}
\tag{5}
\]
The coefficient of r must be the same constant c in both tests.
No other positive powers of r may remain in the first test.
All positive cases have polynomial kernel C^[3].

The [complete proof](research/polynomial-local-slice-coefficients-pass23.md)
contains both necessity arguments and both directions of the global
coordinate construction. This strictly enlarges the preceding
local-slice-linear coefficient class without claiming a classification
of all b in R.

Some exact consequences make the distinction visible:

| Coefficient b | Decision from (5) |
| --- | --- |
| 1+q(f,h)r | A slice exists exactly when f divides q. |
| b(f,h) | A slice exists exactly when b is a nonzero constant modulo fh. |
| 1+fr^2 | No slice: the second r-coefficient is 1-f^(nu+1)/3. |
| 1+fr^3 | Both tests pass, so global polynomial coordinates exist. |

The previous exact affine, quadratic, and adjacent cubic minimum-degree
regimes for 1+qr remain valid. No all-degree minimum-slice formula is
claimed for the enlarged class.

### Why either failed remainder excludes every slice

If c=0, E vanishes on x=y=0, so no polynomial can have derivative one.
For c nonzero, each failed remainder produces a curve of two integral
points on one orbit whose translation parameter has a pole.

For the f-divisor, let P(u)=F(0,u^5,u^3). A failed first test means
P(u) is not cu^3 plus a polynomial in u^5. For a nontrivial fifth root
epsilon, the polynomial
(P(u)-P(epsilon*u))/u^3 has nonzero constant and positive degree.
Choose a nonzero root. The two equations
\[
\begin{gathered}
x_1^5+f^\nu/x_1=x_2^5+f^\nu/x_2=h,\\
F(f,h,x_1^3)=F(f,h,x_2^3)
\end{gathered}
\tag{6}
\]
define a curve through the corresponding limiting pair and not contained
in f=0. Normalization produces a discrete valuation ring. Both points
(x_i,0,f/x_i,0) are integral, but their orbit parameter
(x_2^3-x_1^3)/(f^n h) is not.

For the h-divisor, write the second remainder A(f)+rB(f). If B is
nonconstant, B(0)=c ensures a nonzero root. Set x=1 and choose opposite
local-slice values r,-r with r^2=h-f^nu. The zero of the odd part of F
again gives a curve with equal t-values, integral physical endpoints,
and orbit parameter -2r/(f^n h) of negative valuation.

A polynomial slice would have integral difference between these
endpoints, yet its difference must equal that nonintegral parameter.
This contradiction is independent of its degree. Both curve arguments
allow multiple roots; neither uses an unsupported simple-root premise.
Their dimension and normalization inputs are standard.[^2]

### Why passing both tests produces polynomial coordinates

The essential gauge identity is
\[
r^5-h^3-f^{2\nu}r
=p\bigl[-h(x^2y+az)-2xf^{n+1}r\bigr].
\tag{7}
\]
Work in S_0=C[f,h,x,r]/(xh-r^2-f^nu), which embeds in R.
Both f and h are prime in S_0, and (f) intersect (h)=(fh).
Using (7), the two remainder conditions give actual polynomials g in R
and ell in fS_0 with
\[
F-cr-H_f(h)-H_h(f)-pg=h\ell.
\tag{8}
\]
Differentiating and changing t to (t-g)/c reduce the coefficient to
1+delta_0(ell/c), where delta_0=2r*partial_x+h*partial_r.
This is a genuine polynomial change of the original ring.

After absorbing c in ell, define
\[
L=\ell-f^nt,\qquad \rho=r+hL,\qquad
X=x+2rL+hL^2,\qquad \sigma_0=-L/f^n.
\tag{9}
\]
The functions rho and X are invariants, EL=-f^n, and E(sigma_0)=1.
The map has an explicit inverse after inverting f. Modulo f^n,
its x,r part is the identity modulo the nilpotent ideal (f), so
its inverse is a finite polynomial sum. That inverse supplies an
invariant correction making sigma_0 polynomial. Injectivity modulo
f^n then removes every denominator from the inverse.

This still concerns the auxiliary surface presentation. The final
physical-ring step matters: on its parametrized curve, write
\[
v=\ell(f,u^5,u,u^3),\quad
U=(1+u^2v)^2,\quad W=u^2(1+u^2v),\quad \psi=uU.
\tag{10}
\]
All are taken modulo f^n. Since v is divisible by f, U and the
polynomial substitution psi are invertible there. The transported
curve function Ptilde=(W/U) composed with psi^-1 gives
\[
Y=\frac{\rho-X\widetilde P}{f^n},\qquad
Z=\frac{h-2\widetilde P Yf^n-X\widetilde P^2}{f^{2n}}.
\tag{11}
\]
The full curve congruences clear Y. Multiplying the Z numerator by X
and using the quadratic relation clears Z by primality of f, and gives
f=XZ-Y^2. The independent inverse satisfies the corresponding old-curve
congruences, so both old denominators clear too. The two maps are inverse
after localization, hence globally. This uses established affine
modification principles with the particular full congruences checked
explicitly.[^3]

The scope boundary is real: modulo f the subring C[f,h,r] maps to
C[x^5,x^3], whereas y remains an independent variable after localizing x
on R/(f). Thus y does not belong to this coefficient subring. No
reduction of every b in R to it modulo D(R) is supplied.

## 2. Four generators for the same pinched surface

Keep the exact surface and all branch identifications from the
[preceding construction](research/nodal-generators-pass22.md).
In its uniform normalized coordinates,
\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\qquad
A(u)=(u-1)(u-i),\qquad d=u^4-1.
\tag{12}
\]
Let R_pin be the fixed subring obtained by identifying the specified
three pairs of branch lines. Its conductor is I=dB=(d,du)R_pin,
and R_pin/I=C[t]^3.

Define
\[
\begin{gathered}
b(u)=(1-i)(u+1)(u+i)/4,\qquad
a(u)=-(i/2)A(u)\bigl(u+(1+i)/2\bigr),\\
q(u)=-u b(u)^2,\qquad r(u)=iuA(u)/8,\\
e=du,\qquad g=a(u)+b(u)y,\qquad h_{\rm pin}=q(u)z+r(u)y.
\end{gathered}
\tag{13}
\]
These coefficient letters are local to this surface statement, not
the invariants or derivation from (2). The four elements
d,e,g,h_pin generate R_pin.

On the three conductor pairs their (g,h_pin) values are respectively
(0,t), (1,-t), and (i,-t). Explicit polynomial Bezout identities
recover y and z from u,g,h_pin. Therefore B=S[u] for
S=C[d,e,g,h_pin], and u^4=d+1 makes B finite over S.
The ring R_pin is finite over S too.

There is a short global proof that S=R_pin. The values just listed
give S surjecting onto R_pin/I. Thus the finite S-module
M=R_pin/S satisfies M=(d,e)M. Off d, u=e/d makes M zero.
At every maximal ideal containing d, the relation
e^4=d^4(d+1) also forces e into that maximal ideal. Nakayama's lemma
then makes M zero there. Hence M=0 everywhere.

The [full proof and elimination presentation](research/nodal-elimination-pass23.md)
also give an independent point-and-cotangent reconstruction. This is a
closed embedding in A^4. The minimum number of algebra generators is
now between three and four. No triple retaining both d and du can
work, since the quotient C[t]^3 cannot be generated by one element.
Other triples are not excluded, and no required ambient LND quotient
is constructed.

## 3. What the two general routes now require

### A smooth, stably polynomial family is not yet a trivialization

For a general nonzero LND D on R=C^[3], choose a local slice r with
0!=p=Dr in ker(D) and p nonunit, and choose d in the radical of
p*ker(D). The unit-p case is treated separately by the slice lemma.
The canonical family
\[
\mathcal B=R[\lambda,w]/((1+\lambda d)w-r)
\tag{14}
\]
connects the original R fiber to the principal modification R[r/(1+d)].
It is smooth over C[lambda], stably polynomial over that base,
and trivial modulo every positive power of lambda.

The [complete deformation analysis](research/presentation-homotopy-pass23.md)
constructs these statements by finite formulas. It also shows that
the natural invariant-preserving horizontal derivation is not locally
nilpotent when d is nonzero, even in an example whose total ring is
already polynomial.

Polynomial triviality over C[lambda] is equivalent here to the
existence of some LND sending lambda to one. That derivation need
not preserve the old invariants. Formal triviality alone is insufficient:
an explicit smooth family with central A^3 and all trivial finite jets
has nonconstant units in its noncentral fibers. That control is not
stably polynomial, so it is not a counterexample to the stronger package
satisfied by (14).

Published residual-variable criteria become applicable if the required
fiberwise polynomial variables are first established. Smoothness,
stable polynomiality, and central formal triviality do not themselves
verify that premise.[^4]

### An ambient action does not automatically descend to the section

Write a sliced ring as B=A[s], with E=partial_s. For an ambient LND T,
write T|A=sum s^j D_j and Ts=h(s). A variable-time conjugation
with an independent parameter z replaces s by s-z. It descends to
the quotient z=s exactly when
\[
h(0)=0
\quad\Longleftrightarrow\quad s\mid T(s)
\quad\Longleftrightarrow\quad T(s)=0.
\tag{15}
\]
The last equivalence is the usual LND degree argument in a domain.
Hence this construction produces a descended action only when T
already preserves the slice section.

Taking constant coefficients without that condition can destroy both
local nilpotence and commutation. Explicit coordinate translations
in the [full gate analysis](research/leading-derivation-pass23.md)
demonstrate both failures. Passing to leading coefficients does recover
intrinsic LNDs under the stated filtration hypotheses, but that is
established machinery, and it need not preserve freeness or a slice.[^5]
The primitive example a*partial_b+b*partial_c has a fixed line although
adding partial_s gives an actual coordinate translation.

These calculations isolate missing implications. They do not disprove
cancellation, prove that every coordinate frame fails, or turn an
unproved fiberwise hypothesis into an input theorem.

## 4. Evidence, priority, and next proof obligation

The coefficient theorem has two independent written reconstructions:
the [first audit](research/polynomial-coefficients-audit-pass23.md)
and [second audit](research/polynomial-coefficients-second-audit-pass23.md).
The surface result has a [separate independent audit](research/nodal-four-generator-audit-pass23.md).
The [verification record](research/proof-audits-pass23.md) separates
universal arguments, finite exact controls, and repeated runs.

The final regression counts and artifact hashes are recorded in
[verification-pass-23.json](verification-pass-23.json) and
[consistency-pass-23.json](consistency-pass-23.json). Neither test
success nor model agreement is human expert review or Lean verification.

The [statement-level priority comparison](research/priority-comparison-pass23.md)
retains credit for canonical local-slice constructions, finite
modifications, and leading-derivation machinery. Proper triangular
actions and actions preserving an ambient coordinate have strong
published triviality results, but their hypotheses must be proved
for the physical four-variable ring before they can be applied.[^6]
For example b=1+5hr^4 passes (5), but the raw five-variable auxiliary
derivation fixes points with f=0, h=1, r^4=-1/5. Thus physical slice
existence does not even transfer automatically to that auxiliary action.
No novelty claim follows from a missing search match.

The main unresolved task is still a general reduction or recognition
theorem. On the coefficient route it would require controlling
coefficients outside C[f,h,r] and ultimately an arbitrary sliced
four-variable derivation. On the deformation route it would require
an actual horizontal LND or justified residual variables. On the
surface route, an A^3 embedding would still have to be compatible
with the required global ambient quotient. None is a consequence
of the partial results proved here.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7; G. Freudenburg, [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Section 8.2.

[^2]: The Stacks Project, [Lemma 10.60.12](https://stacks.math.columbia.edu/tag/0BBZ), [Lemma 10.60.13](https://stacks.math.columbia.edu/tag/00KW), [finite normalization](https://stacks.math.columbia.edu/tag/0BXR), and [local rings of normal curves](https://stacks.math.columbia.edu/tag/0B8Y).

[^3]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Proposition 2.1 and Corollary 2.2. The exact inherited full-ideal framework is detailed in the [earlier application audit](research/priority-boundary-pass20.md).

[^4]: P. Das and A. K. Dutta, [*A Note on Residual Variables of an Affine Fibration*](https://arxiv.org/pdf/2002.02128), definitions and Corollary 3.8. The arXiv upload is from 2020; the listed journal publication is from 2014.

[^5]: B. Alhajjar, [*LND-Filtrations and Semi-Rigid Domains*](https://arxiv.org/pdf/1501.00445), Proposition 2.2, crediting Daigle for the associated-graded result, and Proposition 3.4. This is not a new leading-coefficient principle.

[^6]: A. Dubouloz, D. Finston and I. Jaradat, [*Proper triangular Ga-actions on A^4 are translations*](https://arxiv.org/abs/1303.1032); S. Kaliman, [*Proper Ga-actions on C4 preserving a coordinate*](https://msp.org/ant/2018/12-2/ant-v12-n2-p01-s.pdf), Theorem 0.1.
