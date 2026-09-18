# Reconciled height bounds and one cubic bad partial

The apparent remaining whole-height-one recognition problem was already
closed by the saved height-eight theorem. The pass 38 two-direction
criterion is valid but weaker, so it must not be counted as a new
improvement of the project's cancellation threshold.

After that reconciliation, this note treats a genuine next pattern:
three double-bracket bounds and one fourth-bracket bound. It proves
recognition when the flow has degree at most four, and reduces the
other cases to specified highest-coefficient configurations. It does
not close this entire height-ten pattern or the general cancellation
problem. No novelty or expert-verification claim is made.

## 1. Which earlier conclusions actually dominate

The complete [height-eight proof](height-eight-algebra-pass.md) has
exactly the hypothesis
\[
[E,[E,\partial_i]]=0\quad(1\le i\le4).
\]
It proves an invariant ambient polynomial coordinate even without a
slice. Its highest-iterate rank-one reduction, nonhomogeneous
quasi-translation theorem, and cone-preserving homogenization were
reconstructed in this pass. The primary nonhomogeneous theorem really
has the needed scope.[^rankone] Its existing seven-method checker was
read completely and independently rerun: seven methods passed in
0.221 seconds. These are existing methods, not new ones.

The later [pass 13 theorem](../deep-pass-13.md) also closes the mixed
bounds \((2,2,2,3)\) on iterated adjoints under the slice hypothesis.
The complete report and its
[rational-rescaling audit](height-nine-rational-rescale-independent-audit.md)
were read, including the invariant-denominator and positive-weight
fixed-locus gates. Thus the saved threshold is \(H\le9\), not merely
\(H\le8\). The earliest patterns not already covered by that
threshold are
\[
(q_i)=(0,2,2,2),\qquad(1,1,1,3),\qquad(1,1,2,2),
\]
where \(q_i\) are the slice-filtration derivation degrees and
\(H=\sum(q_i+1)\). None is being asserted realizable with a
nonpolynomial quotient.

In particular the \(q\ge3\) branch of
[actual-frame-pass38.md](actual-frame-pass38.md), where that note uses
\(q\) for an augmented matrix rank rather than a filtration degree,
is not a remaining polynomiality gap. The older height-eight theorem
already decides it. The investigation below changes the actual
hypothesis to the next one-cubic-partial bound.

## 2. Exact hypothesis and companion matrix

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\ne0\) be an LND
with a slice, and put \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i\le3),\qquad
\operatorname{ad}_E^4T_4=0.
\tag{1}
\]
If \(\operatorname{ad}_E^3T_4=0\), the pass 13 theorem applies.
Otherwise set
\[
P=E(x),\quad J=\operatorname{Jac}P,\quad
U=\operatorname{ad}_E^2T_4,\quad V=\operatorname{ad}_E^3T_4,
\quad u=U(x),\quad v=V(x)\ne0.
\tag{2}
\]
The good constant space is
\(G=\operatorname{span}_{\mathbb C}(T_1,T_2,T_3)\).
No local-nilpotence assertion about the middle field \(U\) is used.

For \(F_t=\exp(tE)x\), conjugation of the actual coordinate
partials gives the coefficient matrix
\[
C(t)=I-tJ+\frac{t^2}{2}u e_4^{\mathsf t}
                 +\frac{t^3}{6}v e_4^{\mathsf t},\qquad
\operatorname{Jac}(F_t)C(t)=I.
\tag{3}
\]
Indeed the conjugated partial applied to each component of \(F_t\)
returns the corresponding Kronecker delta. The polynomial flow has
Jacobian determinant one, so \(\det C(t)=1\), and both orders of
the inverse identity hold.

The six-by-six linearization is
\[
M=\begin{pmatrix}
J&-u/2&-v/6\\
e_4^{\mathsf t}&0&0\\
0&1&0
\end{pmatrix}.
\tag{4}
\]
Eliminating the lower \(2\times2\) block of \(I-tM\) gives
the Schur complement \(C(t)\). Consequently
\(\det(I-tM)=1\), and Cayley-Hamilton gives \(M^6=0\).
The upper-left block of \((I-tM)^{-1}\) is \(C(t)^{-1}\).
Writing \(h_r=E^r x\), comparison of coefficients yields
\[
\frac{\operatorname{Jac}h_r}{r!}=(M^r)_{1:4,1:4},\qquad
h_6\in\mathbb C^4,\quad h_7=0.
\tag{5}
\]
Thus the flow degree is at most six. These are time-degree bounds,
not ordinary polynomial-degree bounds.

Here the rank-one descent used for the earlier five-by-five matrix
still works. The right kernel of \(M\) has zero intersection with
the span of the last two coordinate vectors: applying \(M\) to
\((0,a,b)\) first forces \(a=0\), then \(v b=0\), so \(b=0\).
The left kernel has the analogous property, because
\((0,a,b)M=(a e_4^{\mathsf t},b,0)\).
If \(M^{r+1}=0\), \(\operatorname{rank}M^r\le1\), and its
upper-left block vanishes, an outer-product expression for a
nonzero \(M^r\) would put one of these kernel vectors wholly
in the auxiliary coordinates. Hence \(M^r=0\).

For a nilpotent matrix of size six, the fifth power has rank at
most one. After its vanishing, the fourth power has rank at most
one; after the fourth vanishes, the third has rank at most one.
This follows directly by listing the possible Jordan block sizes.
Using (5) and the preceding descent proves:
\[
\text{if the highest nonzero }h_m\text{ is nonconstant and }m\ge3,
\quad m\in\{3,4,5\},\quad\operatorname{rank}\operatorname{Jac}h_m=1.
\tag{6}
\]
The possible rank-two square of a \((3,3)\) nilpotent matrix
does not invalidate (6). The action's additional top identities
close the time-degree-two case separately.

## 3. The highest coefficients, including the low-time cases

Let \(m\) be the greatest index with \(h_m\ne0\). The flow
identity also gives \(C(t)P(F_t)=P\). For \(m\ge2\), its
coefficients of degrees \(m+2\) and \(m+1\) imply
\[
(h_m)_4=0,\qquad (h_{m-1})_4=0.
\tag{7}
\]
The nonzero column \(v\) is essential. If \(m=1\), the cubic
coefficient directly gives \(P_4=0\). If \(m=2\), (7) gives
the same conclusion. Therefore \(x_4\) is an invariant ambient
coordinate whenever \(m\le2\), and the regular-kernel theorem
recognizes \(\ker E\simeq\mathbb C^{[3]}\).[^kernel]

For \(m\ge3\), put
\[
h=h_m,\qquad l=(h_{m-2})_4,\qquad
A_m=\frac{(m-1)(m-2)}6,\quad B_m=\frac{m(m-1)}6.
\]
The next coefficient of \(C(t)P(F_t)=P\), and the coefficient
of degree \(m+1\) in \(C(t)\operatorname{Jac}(F_t)=I\), give
\[
Jh=A_m l v,\qquad
J\operatorname{Jac}h=B_m v\operatorname{Jac}l.
\tag{8}
\]
Also \(E(h)=E(l)=0\). These factors are not the ones in the
old quadratic-bad-column argument; the extra Taylor coefficient
changes \(m-1\) there to \(m-2\) here.

For completeness, the good first commutators \(W_i=[E,T_i]\)
and the highest bad field \(V\) kill both \(h\) and \(l\).
Compare the highest coefficients when their conjugated partials
act on \(F_t(x)\) and on \(F_t(x_4)\). Equations (7) make the
latter polynomial have degree at most \(m-2\), which is why
its highest coefficient is precisely \(l\). This assertion does
not say that \(U\) kills them or is locally nilpotent.

If \(h=c\) is a nonzero constant vector, the second identity
in (8) forces \(l\) constant. When \(l=0\), the first identity
gives \(Jc=0\). The constant translation \(c\cdot\partial\)
then commutes with \(E\). Its coordinate-three-ring kernel
inherits a nonzero good partial, and the previously proved
three-variable single-partial lemma gives an invariant ambient
coordinate. If the restriction of \(E\) to that three-ring is
zero, any of its coordinates is already such an invariant.
This argument uses only \(\dim G=3\), not a bound
on the fourth partial.[^single]

For a nonconstant \(h\), (6) and the second identity in (8)
make the joint map \((h,l)\) have Jacobian rank one. The
polynomial curve-factorization theorem therefore gives
\[
h=H(a),\qquad l=L(a),\qquad a\in B,
\quad H\in\mathbb C[T]^4,\ L\in\mathbb C[T].
\tag{9}
\]
The parameter is polynomial, not asserted to be an ambient
coordinate.[^curve] In particular \(E(a)=0\).

## 4. The corrected coefficient-curve argument

Define the polynomial vector and its derivation
\[
w(a)=(m-2)L(a)H'(a)-mL'(a)H(a),\qquad
W=w(a)\cdot\partial.
\tag{10}
\]
By (8), \(Jw=0\). Also \(E(w)=0\), so \([E,W]=0\).
Commuting with the actual iterate \(h=E^m x\) gives
\(W(h)=E^m(Wx)=E^m(w(a))=0\). A nonconstant component of
\(H\) implies \(W(a)=0\). Thus \(W(w)=0\): if \(w\ne0\),
this is a nice LND whose coefficient Jacobian has rank at most
one.

Here is the recognition argument with its dependency gates made
explicit. A nonzero constant \(w\) gives the constant commuting
translation just used. For nonconstant \(w\), de Bondt's
nonhomogeneous rank-one quasi-translation theorem applies.[^rankone]
Its linear normal form has output-span dimension at most three.
If that span is one, \(w=f c\) and \(Jw=0\) give \(Jc=0\).
If it is three, its components depend on one ambient linear
coordinate; \(E(w)=0\) makes that coordinate invariant.

For span two, take linear coordinates \(z_1,\ldots,z_4\) with
\(W=f(z_1,z_2)\partial_{z_3}+k(z_1,z_2)\partial_{z_4}\).
Factor this coefficient curve inside \(\mathbb C[z_1,z_2]\):
there is \(b\) in that plane with \(f,k\in\mathbb C[b]\) and
\(E(b)=0\). Dividing the univariate gcd gives
\(W_0=p(b)\partial_{z_3}+q(b)\partial_{z_4}\), still commuting
with \(E\), with \(\alpha p+\beta q=1\) in \(\mathbb C[b]\).
The actual coordinates
\[
v_0=qz_3-pz_4,\qquad \rho=\alpha z_3+\beta z_4
\]
have inverse \(z_3=p\rho+\beta v_0\),
\(z_4=q\rho-\alpha v_0\). Thus \(W_0=\partial_\rho\)
and its coordinate-three-ring kernel is \(E\)-stable.
The good constant space \(G\) intersects the two-dimensional
output plane in a nonzero constant direction. Its restriction
is \((\gamma q-\delta p)\partial_{v_0}\), with a nonzero,
\(E\)-invariant coefficient, because the two output components
were complex-linearly independent. That factor cancels from its
double-bracket equation. The single-partial lemma on the
coordinate three-ring again supplies an invariant ambient
coordinate. No multivariable Bézout assertion has been made.

If \(L=0\), (8) gives \(Jh=J\operatorname{Jac}h=0\).
The same commuting-iterate argument makes \(h\cdot\partial\)
a rank-one nice LND, so the preceding recognition applies.
Consequently an unrecognized nonconstant-top case must have
\(L\ne0\) and \(w=0\).

Put \(e=\gcd(m,m-2)\). The equations
\((m-2)LH_i'=mL'H_i\) give constant ratios of the nonzero
\(H_i\), and at every root give
\((m-2)\operatorname{ord}H_i=m\operatorname{ord}L\).
Factoring the univariate polynomials over \(\mathbb C\) yields
\[
h=c g^{m/e},\qquad l=\lambda g^{(m-2)/e},\qquad
c\in\mathbb C^4\setminus\{0\},\ c_4=0,\quad
\lambda\in\mathbb C^*,\quad E(g)=0.
\tag{11}
\]
Here \(g\) is a nonconstant polynomial. The changed gcd is
essential; consecutive-power reasoning from pass 13 cannot be
copied unchanged.

## 5. Complete low-time closure by actual shears

For \(m=3\), equation (11) reads
\(h=cg^3\), \(E(x_4)=\lambda g\). With
\(A=c\cdot\partial\in G\), use the polynomial shear
\[
y=x-\frac{c}{6\lambda^3}x_4^3.
\tag{12}
\]
Its inverse changes the minus to plus, since \(c_4=0\).
The first three partials stay unchanged, and the new fourth is
\(T'_4=T_4+x_4^2A/(2\lambda^3)\).
The first identity in (8) gives
\(g^2Jc=\lambda v/3\). Since
\(\operatorname{ad}_E^2A=0\) and \(E(g)=0\), the Leibniz
formula for three brackets gives
\[
\operatorname{ad}_E^3T'_4
=V+\frac{3g^2}{\lambda}[E,A]
=V-\frac{3g^2}{\lambda}(Jc)\cdot\partial=0.
\tag{13}
\]
This is a polynomial identity, including on \(g=0\). The
known mixed slice theorem now applies to the actual new frame.

For \(m=4\), (11) instead reads
\(h=cg^2\), \(E^2(x_4)=\lambda g\), \(E^3(x_4)=0\).
The shear is
\[
y=x-\frac{c}{6\lambda^2}x_4^2,
\qquad T'_4=T_4+\frac{x_4}{3\lambda^2}A.
\tag{14}
\]
Now (8) gives \(gJc=\lambda v\), and
\[
\operatorname{ad}_E^3T'_4
=V+\frac g\lambda[E,A]=0.
\tag{15}
\]
It again reduces to the already proved mixed theorem. A constant
top with \(m=4\) and \(l=\lambda\ne0\) is covered by exactly
the same calculation with \(g=1\). For a constant top with
\(m=3\) and \(l=\lambda\ne0\), \(x_4/\lambda\) is already
an ambient coordinate slice. The cases \(l=0\) were treated
in Section 3.

Combining all branches proves the bounded conclusion
\[
\boxed{\text{Under (1) and the slice hypothesis, }E^5x=0
\Longrightarrow\ker E\simeq\mathbb C^{[3]}.}
\tag{16}
\]
The displayed condition is on the given four generators, not
on all polynomials. It means flow degree at most four.

## 6. An actual cubic control and the precise remaining cases

In physical coordinates \(a,b,c,d\), put
\[
g=b+c-d^3/6,\qquad
E=\partial_a+g\bigl(\partial_d+(d^2/2)\partial_c\bigr).
\tag{17}
\]
Here \(E(g)=0\) and \(E(a)=1\). With \(r=d-ag\), its
actual inverse presentation is
\[
\ker E=\mathbb C[b,g,r],\qquad
d=r+ag,\quad c=g-b+(r+ag)^3/6.
\]
Thus it is a genuine polynomial cylinder, not an abstract matrix
example. The frame \((a,b,c-a,d)\) has exact adjoint profile
\((1,1,1,3)\), and \(E^3x=g^3e_c\), \(E^4x=0\).
The cubic shear in (12) is the actual coordinate replacement
\(c\mapsto c-d^3/6\), reducing the bad profile.

Nevertheless the middle bad coefficient \(U\) need not be an
LND. In coordinates \(a,b,g,d\), it is
\[
U=2gd\partial_d-g^2\partial_g,\qquad
U^n(g)=(-1)^n n!g^{n+1}\ne0.
\tag{18}
\]
The highest field is \(V=3g^2\partial_d\), which is an LND.
Also the highest coefficient field \(g^3\partial_c\) is not
nice: it sends \(g\) to \(g^3\). These failures do not
contradict the corrected field in (10) or the actual shear.

After all proved branches, the only configurations still
unrecognized by this argument are:

- \(m=5\), with \(h_5=cg^5\), \((h_3)_4=\lambda g^3\),
  where \(g\in\ker E\setminus\{0\}\) may also be constant;
- \(m=6\), with \(h_6=c\ne0\) and \((h_4)_4=\lambda\ne0\)
  constant.

In both cases \(c_4=0\), and (7) and the full differential
identities still apply. These are necessary residual
highest-coefficient descriptions, not constructed counterexamples
or normal forms for every coefficient of \(E\).
No argument here closes them, forces a frame satisfying (1),
or raises the unconditional saved threshold beyond \(H\le9\).

## Sources and verification boundary

The existing height-eight and pass 13 theorems are credited as
previous work in this project, not new pass 39 conclusions.
The present extension retains their established recognition
inputs and verifies the changed cubic-column factors explicitly.
The full original complex threefold cancellation problem remains
open in this project.

The standalone [eight-method exact checker](one_cubic_defect_checks_pass39.py)
imports only `unittest` and `sympy`. Its first run passed all eight
methods in 0.808 seconds. It reconstructs an actual coordinate
inverse and exact profile, both flow-Jacobian inverse orders, the
six-dimensional companion and iterate blocks, the changed top
factors, the non-LND middle field, and the actual repairing shear.
The final method separately checks both Taylor-Leibniz factors.
These finite controls do not prove the universal curve
factorization or recognition theorems used above.

[^rankone]: Michiel de Bondt, [*Quasi-translations and singular Hessians*](https://arxiv.org/pdf/1501.05168), Theorem 5.5, PDF p. 19, complete statement and proof directly read. It applies to nonhomogeneous polynomial quasi-translations of Jacobian rank one and gives the stated dependence on zero-component coordinates. Theorem 5.3, PDF p. 16, supplies the homogeneous rank-two result used in the older height-eight proof; its statement was also directly checked.

[^single]: The fully read [three-variable single-partial proof](height-seven-audit.md), Section 2. Its independent commuting-LND branch uses the complex three-variable theorem explicitly recalled as Proposition 2.14 in Dasgupta and Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510). Their Theorem 2.7 states the planar triangularization used in its dependent branch. Both primary statements were directly read in this pass.

[^curve]: Michiel de Bondt, [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046), Corollary 3.2 and its proof, PDF pp. 20–21, directly read. A transcendence-degree-one subalgebra of a polynomial ring lies in a polynomial parameter algebra inside that same ring. The parameter is not automatically a coordinate; the separate [source note](polynomial-curve-factorization-source.md) records this distinction.

[^kernel]: Bhatwadekar, Gupta and Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1), Theorem 3.5, directly read. The nonzero derivation fixes an actual ambient coordinate, and the slice makes its kernel regular.
