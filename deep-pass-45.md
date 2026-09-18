# Zero-motion recognition and quadratic divisor models

## Result and scope

The nonconstant high-flow zero-motion cases of the supplied two-quadratic coordinate
frame admit invariant ambient coordinates. The dependent-defect case
uses the whole gradient of its preceding-layer parameter. The
independent-defect case uses only the two good-coordinate derivatives,
together with the established theorem on invariants in an actual
two-variable polynomial ring. These are conditional recognition
results, not a proof that every sliced action admits the required frame.

The degree-two residual has a separate local description. Near an
invariant prime where an actual linear local slice is available, its
entire intrinsic quotient is either a polynomial line over a discrete
valuation ring or an explicit quadratic model. The quadratic alternative
is compatible with a polynomial global threefold. Its occurrence cannot
be treated as a counterexample to cancellation.

The working cancellation problem remains
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
It is not solved here. The original email's conclusion has a dimension
mismatch for general \(r\); the complex-threefold interpretation used
in (1) has not been confirmed by the professor. No historical novelty,
human expert review or proof-assistant verification is asserted.

## Actual-coordinate framework

Write \(B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*]\), where
\(E\) is the original locally nilpotent derivation, \(E(s_*)=1\),
and \(A=\ker E\). A locally nilpotent derivation is a polynomial
vector field whose repeated action eventually kills every polynomial.
The slice gives an actual polynomial translation direction.

The supplied frame consists of the ordinary coordinate partials
\(T_i=\partial_{x_i}\), with
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{2}
\]
Set \(W_i=[E,T_i]\) and \(V_i=[E,W_i]\).
The first two coordinate directions are called good because their
second commutators vanish. The terminology describes (2), not an
arbitrary rational change of basis.

Every coordinate argument below retains actual generation of a
polynomial ring. A generic parameter, a polynomial with nonzero
differential, or a rational direction is not automatically a coordinate.
Once an invariant ambient coordinate has been established, the original
slice makes \(A\) regular and the fixed-coordinate kernel theorem gives
\(A\simeq\mathbb C^{[3]}\).[^1]

## Dependent defects with zero parameter motion

The complete hypotheses are recorded in the
[dependent zero-motion proof](research/rotating-zero-motion-closure-pass45.md).
The nonconstant highest layer and its preceding layer have the form
\[
E^mx=cq,\quad z=E^{m-1}x,\quad q=Q(u),\quad
Eu=Du=0,\quad m\in\{3,4\},
\tag{3}
\]
where \(c\) is a nonzero constant good vector, \(Q\) is nonconstant,
and the two bad defects are invariant multiples of the same primitive
nonzero LND \(D\). The inherited identities include
\[
Dz=ct,\qquad [E,T_c]=-\alpha rD,\qquad
\alpha=(m-1)/2,\quad r\ne0,
\tag{4}
\]
with \(r\in\ker E\cap\ker D\) and \(E,D\) independent.
Assume \(T_cu=0\).

The trace identity forces \(t=0\). The next bad-column identities
then show that all four \(W_i\) kill \(u\). Commutativity of the
original partials persists after conjugation. Its first coefficient is
\[
[T_c,W_i]+[W_c,T_i]=0.
\tag{5}
\]
Applying (5) to \(u\), using (4), proves \(D(T_i u)=0\).
Also \(E(T_i u)=W_i u=0\). Therefore
\[
F=\mathbb C[u,T_1u,T_2u,T_3u,T_4u]
\subset C:=\ker E\cap\ker D,
\qquad T_cF=0.
\tag{6}
\]
The fraction field of \(C\) has transcendence degree two, by the
original slice and the nonzero induced intrinsic derivation.

If \(F\) has transcendence degree one, polynomial curve
factorization supplies an actual \(v\in B\) with
\(u=P(v)\), \(T_i u=P_i(v)\), and
\(B\cap\mathbb C(v)=\mathbb C[v]\).[^2]
Differentiation gives \(T_i v=P_i(v)/P'(v)\in\mathbb C[v]\).
An LND of a one-variable polynomial ring has constant coefficient.
All four ordinary derivatives of \(v\) are consequently constants.
Thus \(v\) is a nonconstant affine-linear invariant coordinate.

If \(F\) has transcendence degree two, characteristic zero and
algebraicity of \(\operatorname{Frac}C/\operatorname{Frac}F\)
give \(T_cC=0\). The previously proved rank-three case is already
recognized. In the remaining rank-two case, the other good top also
annihilates \(C\). This permits the following actual descent.

### The three-variable descent mechanism

Make a constant linear change of the good coordinates:
\[
B=R_0[a],\qquad R_0=\mathbb C[b,y,z],\qquad
T_c=\partial_a,\quad S=\partial_b,\quad C\subset R_0.
\tag{7}
\]
For \(f\in C\), the rank-two condition gives \(E(Sf)=0\).
Also \(T_c(Sf)=0\). Applying (4) to \(Sf\) yields
\(D(Sf)=0\), so \(S(C)\subset C\).

The horizontal part of \(E\) is nonzero. Let \(d\) be the largest
degree in \(a\) of \(E(b),E(y),E(z)\), and let
\(k=\deg_a E(a)\). The leading weighted derivation of an LND
is an LND. If \(k\ge d+1\), its value on \(a\) is nonzero and
divisible by \(a\), contradicting the LND divisibility lemma.
Consequently \(k\le d\), and the leading derivation is
\[
\overline E=a^dL,\qquad 0\ne L\in\operatorname{LND}(R_0).
\tag{8}
\]
Coefficient comparison gives \(C\subset\ker L\). Equal
transcendence degrees and algebraic closedness under the original
derivations give the exact equality \(\ker L=C\).

Divide the common polynomial factor of the coefficients of \(L\).
The resulting primitive LND \(L_0\) has the same kernel.
Translation \(\Phi_t=\exp(tS)\) preserves \(C[t]\).
Thus \(L_0\) and \(\Phi_tL_0\Phi_t^{-1}\) have the same
kernel and are rationally proportional. Both coefficient vectors are
primitive in \(R_0[t]\). The numerator and denominator of the ratio
must be units; evaluation at \(t=0\) gives ratio one. Hence
\[
[S,L_0]=0.
\tag{9}
\]
The coefficients of \(L_0\) are independent of \(b\).
Its restriction to the actual plane \(\mathbb C[y,z]\) is an LND.
If this restriction is zero, \(y\) is already an invariant coordinate.
Otherwise the plane invariant-coordinate theorem supplies one.[^3]
Since \(\ker L_0=C\), that coordinate is also killed by \(E\).

This closes the dependent nonzero-\(r\), nonconstant-highest case
with \(T_cu=0\), including its former rank-two residual. It applies
to the common-power alternative as well as the rotating alternative.
In the rotating notation of the preceding report,
\(R_1\nmid Q'\) now gives recognition without an additional rank
hypothesis. Nonzero parameter motion is still outside the conclusion.

## Independent defects with zero top-parameter motion

The independent highest-layer normal form is
\[
E^mx=cg^m,\qquad L_0E^{m-1}x=\lambda g^{m-1},\qquad
3\le m\le5,\quad g\notin\mathbb C.
\tag{10}
\]
Here \(L_0\) denotes the original bad-coordinate selector, not the
primitive derivation in (9). The vectors \(c\) and \(\lambda\)
are nonzero constant good and bad vectors. Assume \(T_cg=0\).
The inherited identity is
\[
g[E,T_c]=-\alpha V_\lambda,\qquad V_\lambda\ne0.
\tag{11}
\]
The independent proof is in
[the zero-motion transfer note](research/independent-zero-motion-closure-pass45.md).

After the established commuting rank-three cases are removed, all
good tops and both bad defects lie in the rank-two distribution
generated by \(E,V_\lambda\). Its common invariant ring has
transcendence degree two. The highest good-column identities and the
mixed identity (5) show
\[
F_g=\mathbb C[g,T_1g,T_2g]\subset C,\qquad T_cF_g=0.
\tag{12}
\]
Only these two derivatives are claimed to be jointly invariant.
The bad-coordinate derivatives need not be.

If \(\operatorname{trdeg}F_g=2\), algebraicity gives \(T_cC=0\).
Equation (11), applied after multiplying by \(g\), gives the same
kernel-preserving other partial and descent (7)--(9).
It produces an invariant ambient coordinate.

If \(\operatorname{trdeg}F_g=1\), write \(g=P(v)\) by curve
factorization. The good derivatives of \(v\) are constants and
\(T_cv=0\). A nonzero derivative in the other good direction
makes \(v\) an actual triangular coordinate. If both derivatives
vanish, \(v\) belongs to the actual bad plane
\(\mathbb C[x_3,x_4]\). It is nonconstant and killed by \(E\).
The established binary-invariant theorem then supplies an invariant
coordinate of that plane, whether or not \(E\) preserves the plane
itself.[^4]

Thus the independent nonconstant high-flow, nonzero preceding-bad
branch with \(T_cg=0\) is recognized. No compatible global slice
for the auxiliary action is needed. The local compatibility obstruction
discussed below can remain nonzero without invalidating this route.

## Full quotient rings at invariant divisors

For the independent degree-two residual, retain the preceding
generic graph and actual generation:
\[
B_L=L[x_3,x_4],\quad A_L=L[j],\quad
x_i=\mathcal Q_i(x_3,x_4),\quad \deg\mathcal Q_i\le2,\quad i=1,2,
\tag{13}
\]
where \(C\simeq\mathbb C^{[2]}\), \(L=\operatorname{Frac}C\),
\(f=Ex_3\), \(g=Ex_4\), and \(j=gx_3-fx_4\).
The common base and faithful flatness are inherited, not assumed from
the desired polynomiality of \(A\).

Fix an irreducible \(\pi\in C\), let \(R=C_{(\pi)}\), and
write \(\kappa=R/\pi R\). If \(f\) is a unit in \(R\),
the actual localized slice \(\sigma=x_3/f\) gives
\[
x_3=f\sigma,\quad x_4=g\sigma-j/f,\quad
A_R=R[j,q_1(j),q_2(j)],\quad \deg q_i\le2.
\tag{14}
\]
The last equality is slice projection of the entire actual generating
set. It is stronger than identifying the image of the bad coordinates.
The case where \(g\) is a unit is symmetric.

The [full divisor classification](research/quadratic-divisor-classification-pass45.md)
uses \(A_R\cap L=R\) and the nonzero domain fiber
\(A_R/\pi A_R\). DVR elimination of quadratic leading coefficients,
then linear leading coefficients, gives either \(A_R=R[t]\) or
\[
A_R=R[t,z]\simeq R[T,Z]/(\pi^n Z-P(T)),\quad
n\ge1,\quad\deg P\le2.
\tag{15}
\]
Minimality of \(n\) makes the relation primitive. Gauss's lemma
and localization show that this presentation is saturated and exact.
The residue polynomial \(\overline P\) is irreducible and nonconstant.

### Linear and quadratic residue alternatives

If \(\deg\overline P=1\), its residue root lifts modulo \(\pi^n\)
by finitely many corrections in \(R\). After shifting \(T\), write
\(\pi^n(z-c)=bT+aT^2\), where \(b\) is a unit and \(a\in\pi R\).
The finite geometric sum
\(L(T)=b^{-1}\sum_{k=0}^{n-1}(-aT/b)^k\) satisfies
\((b+aT)L=1+\pi^nK\). Therefore
\[
w=T/\pi^n=(z-c)L-TK\in A_R,\quad
T=\pi^n w,\quad z=c+bw+a\pi^n w^2.
\tag{16}
\]
This proves \(A_R=R[w]\) by an actual polynomial inverse.
Neither a formal series nor Henselianity is required.

If \(\deg\overline P=2\), completing the square gives
\[
A_R\simeq R[T,Z]/(\pi^nZ-T^2+\eta),\quad
\eta\in R^*,\quad\overline\eta\notin\kappa^{*2}.
\tag{17}
\]
Its full special fiber is
\(\kappa(\sqrt{\overline\eta})[Z]\), which splits into two
lines after algebraic closure of the residue field.

A primitive intrinsic LND with kernel \(C\) has the exact local
form \(u(\pi^n\partial_T+2T\partial_Z)\), with \(u\in R^*\).
The contraction \(A_R\cap(L+LT)=R+RT\), proved by independence
of \(1,\overline T\), gives its exact local plinth \(\pi^nR\).
In the polynomial-line alternative the primitive local plinth is \(R\).

### Acceleration slices and the determinant bound

The [acceleration extension](research/acceleration-divisor-extension-pass45.md)
also applies (15)--(17) when both speeds vanish modulo \(\pi\),
provided one good acceleration \(h_i=E^2x_i\) is a unit in \(R\).
The actual slice \(Ex_i/h_i\) is affine-linear in the generic
bad pair. Its slice projection preserves degree at most one for the
bad generators and at most two for the good generators. The same
full-generation DVR elimination therefore applies.

The intrinsic primitive plinth is principal, say \(pC\), by the
inherited faithfully-flat factorial result. Its subtraction argument
is credited to Daigle--Kaliman.[^5] Let \(d=\gcd(f,g)\) in \(C\),
and put \(f_0=f/d\), \(g_0=g/d\), \(j_0=g_0x_3-f_0x_4\).
The global determinant fields satisfy
\[
K_3j_0=f_0\Delta,\quad K_4j_0=g_0\Delta,\qquad
p\mid\Delta.
\tag{18}
\]
For the divisibility, both restrictions are actual invariant multiples
of the primitive intrinsic derivation: denominator contraction follows
from the gcd of its values on algebra generators. Their displayed
values lie in \(pC\); unique factorization and
\(\gcd(f_0,g_0)=1\) give (18). This does not assert that
\((f_0,g_0)\) is the unit ideal.

Every classified quadratic exponent consequently obeys
\(1\le n\le v_\pi(\Delta)\). The unresolved local prime set is
reduced to simultaneous divisors of \(p,f,g,h_1,h_2\): where \(p\)
is a unit locally, an actual intrinsic slice already gives a polynomial line.
Even a classification at every prime would still require a global
recognition or gluing argument.

The familiar polynomial ring \(\mathbb C[X,Y,Z]\), with
\(D=X\partial_Y+2Y\partial_Z\) and invariant
\(H=XZ-Y^2\), already gives (17) at the prime \(X\), with
\(\eta=-H\). A quadratic residue extension alone is therefore
not evidence that the global threefold is nonpolynomial.

## A genuine coordinate partial does not ensure compatibility

The [actual-partial countercontrol](research/actual-partial-obstruction-pass45.md)
works in genuine physical coordinates \((x,y,z,t)\):
\[
E=x\partial_y+2y\partial_z+(1+xz+2y^2)\partial_t,\quad
s=t-yz,\quad E(s)=1.
\tag{19}
\]
For the actual constant partial \(T_c=\partial_z\), set
\(U=[E,T_c]=-x\partial_t\), \(Y=xy\partial_t\), and \(g=x\).
Then \([E,U]=[Y,U]=0\), \([E,Y]=-gU\), and the three fields
have rank two. All of them, and \(T_c\), kill \(g\).

The polynomial slice invariants are
\(\eta=y-xs\) and \(\zeta=z-2ys+xs^2\), giving
\(A=\mathbb C[x,\eta,\zeta]\). On this ring,
\[
U|_A=xD_0,\quad D_0=x\partial_\eta+2\eta\partial_\zeta,\quad
\ker D_0=\mathbb C[x,v],\quad v=x\zeta-\eta^2.
\tag{20}
\]
The primitive action has plinth \(x\mathbb C[x,v]\), and the
actual induced action has plinth \(x^2\mathbb C[x,v]\).
A compatible original slice would require \(U(f)=x\) for
\(f\in A\). The obstruction class \([-x]\) has exact
annihilator \((x)\). It is nonzero even at the generic divisor.

The example has exact supplied heights \((1,1,2,2)\) after an
actual constant good-plane change. However, its highest flow direction
is \(\partial_t\), not the obstructed \(\partial_z\), and its
preceding bad projection is zero. It also fails the required normalized
constant second-direction identity (11). Thus it refutes an automatic
compatible-slice shortcut, not either zero-motion recognition theorem
and not cancellation. The induced action in (20) is nonprimitive.

## Remaining mathematical obligations

| Part of the problem | Present conclusion | Remaining obligation |
| --- | --- | --- |
| Dependent nonconstant high flow, nonzero multiplier | Zero parameter motion is recognized | Handle nonzero parameter motion |
| Independent nonconstant high flow, nonzero preceding bad projection | Zero top-parameter motion is recognized | Handle nonzero top-parameter motion |
| Degree-two independent residual | Full local line/quadratic models where a speed or acceleration is a unit | Treat simultaneous vanishing primes and global recognition |
| Auxiliary compatible slices | Actual coordinate commutator does not suffice by itself | Use extra canonical identities when compatibility is needed |
| Supplied frame classification | Previously complete profiles remain complete | Finish the entire supplied \((1,1,2,2)\) profile |
| Unrestricted cancellation | No universal reduction is proved | Produce and verify an actual frame reduction or another global route |

These obligations cannot be replaced by more finite examples. The
local descriptions require their all-degree written algebra; the
recognition results require their actual-coordinate and source
hypotheses. A test suite checks explicit identities and countercontrols,
not all polynomial actions or the truth of (1).

## Sources

[^1]: S. M. Bhatwadekar, N. Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), 2015 preprint, Theorem 3.5 and proof, PDF p. 11; Proposition 3.3 supplies the local regular-kernel argument. Used only after obtaining an invariant actual coordinate.

[^2]: M. de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4), Corollary 3.2 and Lemma 3.3, PDF pp. 20--21. The polynomial parameter and exact intersection statement are distinct from ambient coordinate status.

[^3]: S. Kuroda, [*The automorphism theorem and additive group actions on the affine plane*](https://arxiv.org/pdf/1604.04070v1), 2016, Theorem 1.1 and proof, PDF pp. 1--3. The characteristic-zero plane theorem is credited there to Rentschler.

[^4]: S. Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313v2), version 2 dated May 1, 2013, Proposition 3.2 and following discussion, PDF p. 8. It records the characteristic-zero binary-invariant result credited to Daigle--Freudenburg and points to Freudenburg's 1996 paper and 2006 monograph. The theorem concerns an actual coordinate two-ring inside the larger polynomial ring.

[^5]: D. Daigle and S. Kaliman, [*A note on locally nilpotent derivations and variables of k[X,Y,Z]*](https://www.math.miami.edu/~kaliman/library/canada.daigle-kaliman.pdf), 2009, Theorem 1.5, p. 539. The principal-plinth mechanism is inherited through the [earlier plinth audit](research/intrinsic-plinth-boundary-pass27.md); no new attribution is made for the gcd subtraction.
