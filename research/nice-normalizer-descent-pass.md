# Nice normalizers: exact descent and a nonprojectable control

A locally nilpotent derivation normalizing a slice derivation actually
commutes with it. This holds without a nice-coordinate hypothesis.
For a nice field of the specific form
\(p(x,y)\partial_a+q(x,y)\partial_b\), a nonconstant coefficient gcd
then gives a height-independent invariant-coordinate theorem. The
primitive row case is different: its abstract polynomial quotient need
not be a coordinate factor, and commutation does not force projectability
onto the displayed plane \(\mathbb C[x,y]\).

An explicit polynomial-coordinate control below proves the last
distinction. It has a slice, a nonzero commuting nice field, coefficient
gcd one, and a non-unimodular coefficient row. Its kernel is polynomial,
so it is not a cancellation counterexample. The general nice-normalizer
bridge is not proved here.

## 1. Normalization of a slice forces commutation

Let \(B\) be a characteristic-zero domain, let \(E\) be an LND with
a slice \(s\), and put \(K=\ker E\). Thus \(B=K[s]\) and
\(E=\partial_s\). Let \(Z\) be another LND and suppose
\[
[Z,E]=\rho E
\tag{1}
\]
for \(\rho\in B\). Then
\[
\rho=0.
\tag{2}
\]

Indeed, (1) implies \(Z(K)\subseteq K\). Therefore
\(\Phi_t=\exp(tZ)\) preserves \(K[t]\), and its restriction there
is an automorphism, with inverse \(\exp(-tZ)|_{K[t]}\).
Compose \(\Phi_t\) with the extension of that inverse which fixes
\(s\). This is a \(K[t]\)-automorphism of the one-variable polynomial
ring \(K[t][s]\), so its image of \(s\) has degree one in \(s\),
with leading coefficient a unit of \(K[t]\).

Undoing the base automorphism gives
\[
\Phi_t(s)=u(t)s+b(t),\qquad u(t)\in K[t]^*,\quad b(t)\in K[t].
\]
Units of \(K[t]\) are units of \(K\), because \(K\) is a domain.
The identity \(\Phi_0(s)=s\) therefore gives \(u(t)=1\).
It follows that \(E\) commutes with \(\Phi_t\) on both \(K\) and
\(s\), hence on \(B\). Taking the coefficient of \(t\) proves
\([Z,E]=0\), and then (2) follows because \(E\ne0\).

For \(B=\mathbb C^{[4]}\), allowing \(\rho\) initially to lie in
\(\operatorname{Frac}B\) does not change the statement. In any
polynomial frame \(w\), the slice gives
\[
1=E(s)=\sum_i s_{w_i}E(w_i).
\]
Polynomiality of \(\rho E(w_i)=[Z,E](w_i)\) therefore implies
\(\rho\in B\).

The LND premise on \(Z\) matters. For example,
\(E=\partial_s\) and \(Z=s\partial_s\) satisfy
\([Z,E]=-E\), but \(Z\) is not locally nilpotent.

## 2. Polynomial plane direction is enough without invariant rescaling

The following criterion is the known quasi-extension lemma of
[Freudenburg and Moser-Jauslin, Section 2.1, Lemma 2.1](https://moser.perso.math.cnrs.fr/adjoinedroots.pdf),
followed by plane-coordinate recognition. Its elementary proof is
included to make the multiplier hypothesis explicit. The source's
complete lemma was checked in its indexed text; direct PDF retrieval
timed out. Let \(B=R[a,b]\), \(R=\mathbb C[x,y]\), and let \(E\) be
an LND of \(B\), not necessarily a slice derivation. Suppose
\[
E(x)=h p(x,y),\qquad E(y)=h q(x,y)
\tag{3}
\]
with \(0\ne h\in B\) and \(p,q\in R\), not both zero. Then the
plane derivation
\[
D=p\partial_x+q\partial_y
\]
is locally nilpotent. No assumption \(E(h)=0\) is needed.

For nonzero \(f\in B\), write \(\deg_E f\) for the greatest
\(j\) with \(E^j f\ne0\). In characteristic zero this degree is
additive on products. Whenever \(f\in R\) and \(Df\ne0\), (3)
gives
\[
\deg_E(Df)=\deg_E f-\deg_E h-1<\deg_E f.
\tag{4}
\]
Repeated application to \(f,Df,D^2f,\ldots\), all in \(R\), forces
one iterate to vanish. Thus \(D\) is an LND on \(R\).
Rentschler's theorem, in the exact form recalled in
[Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510),
supplies a plane coordinate killed by \(D\), hence by \(E\).

If the ratio \(E(x):E(y)\) is defined over \(\operatorname{Frac}R\),
choose a primitive plane pair \((p,q)\) in that direction. Its gcd
remains one in the UFD \(R[a,b]\). Prime valuations show that the
common multiplier \(h\) in (3) is polynomial. This is a gcd argument,
not a multivariable Bezout assertion.

In particular, if \(E\) kills any nonconstant polynomial \(d\in R\),
then it kills a coordinate of \(R\). If both \(E(x),E(y)\) vanish,
this is immediate. Otherwise
\(d_xE(x)+d_yE(y)=0\) gives the required projective direction over
\(\operatorname{Frac}R\), and the preceding argument applies.

If \(E\) also has a slice on \(\mathbb C^{[4]}\), any ambient
invariant coordinate closes its kernel. The slice makes the kernel
regular, and
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
then identifies it with \(\mathbb C^{[3]}\).

## 3. A common factor in a nice plane row closes the slice kernel

Now let \(B=\mathbb C[x,y,a,b]\), let \(E\) be a slice LND, and
assume the nonzero normalizing field has the specific form
\[
Z=p(x,y)\partial_a+q(x,y)\partial_b.
\tag{5}
\]
Such \(Z\) is nice in this frame. By Section 1, it commutes with
\(E\). Write
\[
d=\gcd(p,q),\qquad p=dp_0,\quad q=dq_0,
\qquad Z=dZ_0,
\qquad Z_0=p_0\partial_a+q_0\partial_b.
\]
Zeros among \(p,q\) are allowed, with the usual gcd convention.
The commutator equation is
\[
[E,Z_0]=-\frac{E(d)}dZ_0.
\tag{6}
\]
The left side is polynomial. For every prime divisor of a reduced
denominator of \(E(d)/d\), at least one of the primitive coefficients
\(p_0,q_0\) has valuation zero. Equation (6) consequently gives
\(E(d)/d\in B\). LND divisibility forces
\[
E(d)=0,\qquad [E,Z_0]=0.
\tag{7}
\]

If \(d\) is nonconstant, it belongs to the displayed coordinate plane
\(R\). Section 2 supplies an invariant plane coordinate, and the
slice kernel is \(\mathbb C^{[3]}\). This conclusion uses no mixed
commutator bound for \(E\), and no unimodularity of \((p,q)\).

The condition that the coefficients in (5) lie in a coordinate plane is
part of this theorem. No claim is made here that every nice field with
two-dimensional image span automatically has exactly this form without
an additional factor depending on \(a,b\).

## 4. What a primitive row actually supplies

Assume henceforth \(\gcd(p,q)=1\), and put
\[
v=qa-pb.
\]
Then
\[
\ker Z=R[v]\cong\mathbb C^{[3]}.
\tag{8}
\]
For example, after inverting \(p\), the slice \(a/p\) gives
\((\ker Z)_p=R_p[v]\); after inverting \(q\), one similarly gets
\(R_q[v]\). Inside \(\operatorname{Frac}R[v]\), coprimality gives
\(R_p[v]\cap R_q[v]=R[v]\). The cases with one zero coefficient
reduce to a constant nonzero other coefficient and are immediate.

Commutation makes (8) an \(E\)-stable polynomial three-ring. Its
embedding into \(B\) requires a separate check.

If \((p,q)=R\), choose \(\alpha p+\beta q=1\). Then
\[
t=\alpha a+\beta b,\qquad
a=pt+\beta v,\qquad b=qt-\alpha v
\tag{9}
\]
give \(B=R[v,t]\), \(Z=\partial_t\). Hence \(\ker Z\) is an
actual coordinate three-ring, and
\[
E=D+f\partial_t,
\qquad D\in\operatorname{LND}(R[v]),\quad f\in R[v].
\tag{10}
\]
This does not itself give an invariant coordinate of the three-ring.
An arbitrary nonzero LND on \(\mathbb C^{[3]}\) has an abstract
polynomial two-ring kernel, but its rank can be three. The known kernel
theorem must not be silently strengthened to ambient-coordinate
recognition. In particular, the earlier single-good-partial proof cannot
be reused here without that extra hypothesis. No general closure of
(10) from the slice premise alone is supplied by this note.

If \((p,q)\ne R\), their common-zero set \(\Sigma\subset\mathbb A^2\)
is finite and nonempty. The quotient map associated with (8) is
\[
\pi(x,y,a,b)=(x,y,qa-pb).
\]
Over \((x,y)\notin\Sigma\) its fibers are affine lines. Over
\(e\in\Sigma\), only the value \(v=0\) occurs, and that fiber is
an affine plane. Thus
\[
\mathbb A^3\setminus\pi(\mathbb A^4)
=\coprod_{e\in\Sigma}\{(e,v):v\ne0\}.
\tag{11}
\]
In particular \(\ker Z\) is not a coordinate three-factor of \(B\):
a coordinate projection is surjective. Coprimality did not imply the
unit ideal, and (8) did not imply (9).

There is nevertheless an exact restriction on the induced LND
\(D=E|_{R[v]}\). Its flow preserves the image of \(\pi\), hence the
complement (11). A connected additive group cannot permute its finitely
many components. Each component is \(\mathbb C^*\), which has no
nontrivial algebraic additive-group action. Thus each punctured line
is pointwise fixed. By density its whole line is fixed, so
\[
D(x),D(y),D(v)\in\bigcap_{e\in\Sigma}\mathfrak m_e R[v].
\tag{12}
\]
This is a fixed-line restriction on a three-variable LND. It does not
say that \(D(x),D(y)\) are independent of \(v\).

## 5. A commuting slice need not have projectable base direction

Take
\[
Z=x\partial_a+y\partial_b,\qquad v=ya-xb.
\]
Its row has gcd one, but generates the proper ideal \((x,y)\).
Define
\[
Q=x+vy,\qquad U=vx+(1+v^2)y,
\]
\[
S=a+vb,\qquad T=va+(1+v^2)b.
\tag{13}
\]
These are polynomial coordinates. Indeed,
\[
v=US-QT,
\]
and the exact polynomial inverse is
\[
x=(1+v^2)Q-vU,\qquad y=-vQ+U,
\]
\[
a=(1+v^2)S-vT,\qquad b=-vS+T.
\tag{14}
\]
The same determinant-one matrix is applied to \((x,y)\) and \((a,b)\),
preserving their determinant \(v\).

Let \(E=\partial_S\) in the frame \((Q,U,S,T)\). Thus \(E\) is
a polynomial LND with slice \(S\), and
\[
Z=Q\partial_S+U\partial_T,
\qquad [Z,E]=0.
\]
In the original frame, the exact coefficient vector is
\[
\begin{aligned}
E(x)&=U\bigl(vx+(v^2-1)y\bigr),\\
E(y)&=-U(x+vy),\\
E(a)&=1+v^2+U\bigl(va+(v^2-1)b\bigr),\\
E(b)&=-v-U(a+vb).
\end{aligned}
\tag{15}
\]
In particular \(E(v)=U\), and
\[
\frac{E(x)}{E(y)}=-v+\frac{y}{x+vy}.
\tag{16}
\]
This ratio is not in \(\mathbb C(x,y)\). Treating \(v\) as the
transcendental fiber invariant, its derivative with respect to \(v\)
is \(-1-y^2/(x+vy)^2\ne0\). Equivalently its derivative with respect
to \(a\) at fixed \(x,y,b\) is
\[
-y\left(1+\frac{y^2}{(x+vy)^2}\right)\ne0.
\]
Thus neither preservation of the displayed plane nor even projectability
of its direction follows from a slice and a commuting nice row.
Also no nonconstant constant-linear combination of \(x,y\) is
\(E\)-invariant: in \(\alpha E(x)+\beta E(y)\), the coefficient of
\(v^2\) first forces \(\alpha=0\), then \(\beta=0\).

The example does preserve the different coordinate plane
\(\mathbb C[Q,U]\), and \(\ker E=\mathbb C[Q,U,T]\).
It therefore refutes only the asserted implication for the displayed
plane, not the possible existence of some other invariant coordinate
plane. All original hypotheses are retained: \(Z\ne0\) is nice,
\(E\) is a slice LND, and they commute. Eighteen inline exact symbolic
checks verified the inverse, bracket, slice, niceness, and nonprojectable
ratio in 0.209 seconds. These checks concern the example, not the
general lemmas above.

## 6. Precise boundary of the height-independent bridge

The normalization factor is completely eliminated. A nonconstant
coefficient gcd in the specified plane-row form gives an invariant
ambient coordinate and a polynomial slice kernel. A primitive
unimodular row gives an \(E\)-stable coordinate three-ring, while a
primitive non-unimodular row gives only the abstract three-ring (8)
with the fixed-line restriction (12).

The missing assertion is coordinate recognition from an arbitrary
commuting nice field, or even a proof that a primitive non-unimodular
row forces a suitable different coordinate plane to be preserved.
The control shows that this cannot be obtained just by declaring the
original row base projectable. No failure of cancellation, no general
height bound, and no novelty claim follows from this pass.
