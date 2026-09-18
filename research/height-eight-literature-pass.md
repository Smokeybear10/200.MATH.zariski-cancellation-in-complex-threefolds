# Literature boundary for the height-eight double-bracket system

The reduced square-zero, rank-two quasi-translation case closes by a
short consequence of de Bondt's homogenization construction and the
Gordan-Noether rank-two theorem. Its image is a cone, so homogenization
preserves Jacobian rank two even though it adds a fifth variable. The
published homogeneous theorem then forces an invariant linear coordinate
in the original four variables. Section 6 gives the complete argument.

The other nearby literature results below retain their stated hypothesis
limits. This note does not identify a published theorem stating the entire
double-bracket criterion verbatim or make a novelty claim about it.

Let

\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B),\qquad E(s)=1,
\qquad [E,[E,\partial_{x_i}]]=0\quad\text{for all }i.
\tag{1}
\]

Write \(b=(E(x_i))_i\), \(J=\operatorname{Jac}(b)\). The previously audited
identities are

\[
E(J)=J^2,\qquad J^4=0,\qquad
\operatorname{Jac}(\exp(tE)x)=(I-tJ)^{-1}
=I+tJ+t^2J^2+t^3J^3.
\tag{2}
\]

They imply \(E^4(x_i)\in\mathbb C\), hence \(E^5(x_i)=0\): the flow is
polynomial of degree at most four in its group parameter. They do not
assert that the vector field \(b\) has ordinary total degree at most four.
The first brackets \(W_i=[E,\partial_{x_i}]\) are commuting LNDs and commute
with \(E\), as proved in [height-seven-audit.md](height-seven-audit.md).

## 1. Quasi-translations have a different defining identity

[De Bondt, *Quasi-translations and singular Hessians*, Proposition 1.3](https://arxiv.org/pdf/1501.05168)
identifies the quasi-translation condition for \(x+H\) with
\(\operatorname{Jac}(H)H=0\), equivalently \(H(x+tH)=H(x)\).
For \(E=H\cdot\partial_x\), this is \(E^2(x_i)=0\) for every coordinate:
the flow is \(x+tH\).

Corollary 5.6(ii) applies to homogeneous quasi-translations in dimension
at most four. In dimension four, the image of \(H\) has linear span of
dimension at most two. Corollary 5.9 gives the linearly conjugate form

\[
H=(0,0,bg,ag),\quad
a,b\in\mathbb C[x_1,x_2],\quad
g\in\mathbb C[x_1,x_2,ax_3-bx_4].
\]

The homogeneity hypothesis is substantive. Example 4.3 constructs a
nonhomogeneous four-dimensional quasi-translation without a nonconstant
linear invariant. It is polynomially conjugate to a simpler action, so it
is not a counterexample to polynomial coordinate recognition. No claim
that this example has a slice or satisfies (1) is being made.

For comparison with (1), differentiate \(Jb=0\). It gives
\(E(J)+J^2=0\). Thus an action satisfying both the quasi-translation
identity and (1) must have

\[
J^2=0,\qquad E(J)=0.
\tag{3}
\]

The sign matters: the Riccati identity alone does not put our action in
the quasi-translation class. Even when (3) holds, \(E^2(x_i)\) can be
nonzero constants; quasi-translation requires their vanishing.

## 2. Nice derivations do not remove the invariant-coordinate premise

[Dasgupta and Gupta, *Nice derivations over principal ideal domains*, Theorem 3.6](https://arxiv.org/pdf/1701.03635)
concerns an irreducible \(R\)-LND of \(R[X,Y,Z]\), where \(R\) is a PID
containing \(\mathbb Q\), satisfying
\(D^2X=D^2Y=D^2Z=0\). It proves rank at most two over \(R\) and a kernel
\(R^{[2]}\).

The exact four-variable consequence, Corollary 3.8, assumes
\(D(X_1)=0\) as well as \(D^2(X_i)=0\) for \(i=2,3,4\), and concludes
\(\ker D\cong K^{[3]}\). The first hypothesis is an invariant ambient
coordinate, not merely an element of the kernel or a slice. In our case
irreducibility follows from the slice, but neither the invariant
coordinate nor the second-power vanishing follows from (2). Thus the
corollary cannot supply the missing premise.

## 3. Strong nilpotence gives an exact conditional target

[De Bondt, *The strong nilpotency index of a matrix*, Theorem 2.1 and Corollary 2.2](https://arxiv.org/pdf/1203.6615)
characterize strong nilpotence by constant linear similarity to a strictly
block-triangular matrix. For a polynomial Jacobian, the hypothesis is

\[
J(y^{(r)})J(y^{(r-1)})\cdots J(y^{(1)})=0
\tag{4}
\]

for independent tuples of indeterminates. If it holds, one can take
\(r\leq4\) here. It is stronger than the same-point identity \(J(x)^4=0\).

Theorem 4.1 specializes to quasi-translations. In that class,
\(J(x)J(y)=0\) is equivalent to \(J(x)H(y)=0\), and to a linear conjugacy
with \(H_i=0\) for \(i\leq r\) and all remaining \(H_i\) depending only
on those first \(r\) variables, for some \(0\leq r<4\).

For (1), establishing (4) would therefore be a genuine sufficient
certificate. Constant linear triangularization of \(J\) triangularizes
the coefficient map \(b\), up to its constants, and hence \(E\).
If the first triangular coefficient is zero, there is an invariant
ambient coordinate, and the regular-kernel theorem closes. If it is a
nonzero constant, that first coordinate is a slice, and triangular
integration constructs three invariant coordinates. This uses the
already checked kernel-recognition endpoint in
[height-seven-audit.md](height-seven-audit.md).

Nothing checked here proves the mixed-point identity (4) from (1).
Replacing a polynomial matrix by its Jordan form over the fraction field
does not prove constant linear triangularization.

## 4. Low-rank quadratic Jacobians require ordinary degree two

[De Bondt, *Quadratic polynomial maps with Jacobian rank two*, Theorem 3.2](https://arxiv.org/pdf/1601.00579)
states that a quadratic polynomial map \(H\) with nilpotent Jacobian and
\(\operatorname{rank}\operatorname{Jac}(H)\leq2\) has a Jacobian similar
over the ground field to a triangular matrix. Theorem 3.3 gives that
conclusion for quadratic \(H\) under \(\operatorname{Jac}(H)^2=0\),
without the rank assumption. In characteristic zero it also gives a
mixed product of length three equal to zero, or length two when \(H\)
is homogeneous.

Here “quadratic” concerns the ordinary polynomial degree of \(H\), so
the entries of its Jacobian have degree at most one. It does not refer
to the degree of \(\exp(tE)x\) in \(t\). Even a separate proof of
\(\operatorname{rank}J\leq2\) would leave this ordinary-degree premise
unchecked. The theorem would apply to the conditional subcase
\(\deg b\leq2\) and \(\operatorname{rank}J\leq2\), or
\(\deg b\leq2\) and \(J^2=0\), and would close it by Section 3.

## 5. An exact all-ones control separates the degree notions

The following direct calculation satisfies the full system (1), with
arbitrarily large ordinary coefficient degree. Choose any
\(h\in\mathbb C[x]\) with \(h'\ne0\), and put

\[
E=\partial_w+h(x)\partial_y
\quad\text{on }\mathbb C[x,y,z,w],\qquad s=w.
\]

Then

\[
\ker E=\mathbb C[x,z,a],\qquad a=y-wh(x),\qquad
\exp(tE)(x,y,z,w)=(x,y+th(x),z,w+t).
\]

Its flow has parameter degree one, while \(\deg h\) is arbitrary.
Its Jacobian has a single possible nonzero entry, so
\(E(J)=J^2=0\). Now take the ambient linear coordinate frame

\[
(X_1,X_2,X_3,X_4)=(x-y-z-w,y,z,w).
\]

The four coordinate partials are

\[
T_1=\partial_x,\quad
T_2=\partial_x+\partial_y,\quad
T_3=\partial_x+\partial_z,\quad
T_4=\partial_x+\partial_w.
\]

In the cylinder coordinates \((x,z,a,w)\), each partial has derivation
degree exactly one, with the same leading intrinsic direction
\(-h'(x)\partial_a\). Thus this is an actual frame of height eight and
pattern \((1,1,1,1)\), not just an unrelated low-flow-degree action.
Moreover all four brackets equal \(-h'(x)\partial_y\), so
\(E,W_1,\ldots,W_4\) have generic rank two rather than four.

The kernel is explicitly polynomial in this control. It disproves
neither cancellation nor recognition under (1). It does show that the
all-ones pattern supplies neither an ordinary degree bound nor the
full-rank hypothesis of the additive-group orbit argument. Its minimum
height is three despite this particular frame having height eight.

## 6. The reduced rank-two case closes by homogenization

Suppose now that the remaining case has

\[
E^2(x_i)=0\quad\text{for all }i,\qquad J^2=0,
\qquad \operatorname{rank}J=2.
\tag{5}
\]

Then \(x+b\) is a quasi-translation. Let \(S\) be the Zariski closure of
the image of \(b:\mathbb A^4\to\mathbb A^4\). It is an irreducible surface.
At general \(x\), with \(b(x)\) a smooth point of \(S\),

\[
T_{b(x)}S=\operatorname{im}J(x)=\ker J(x).
\]

The first equality uses dominance and rank two; the second uses \(J^2=0\)
and dimension four. Since \(Jb=0\), the radial vector \(b(x)\) belongs to
this tangent space. Thus the Euler derivation
\(\mathcal R=\sum_i y_i\partial_{y_i}\) preserves the prime ideal
\(I(S)\). Explicitly, if \(P(b)=0\), then
\((\mathcal RP)(b)=0\) on a dense open set and hence everywhere.
Every homogeneous component of \(P\) is obtained by a polynomial in
\(\mathcal R\) applied to \(P\), using interpolation among the finitely
many integer degrees appearing in \(P\). Consequently \(I(S)\) is
homogeneous, and \(S\) is a cone.

Choose \(d\geq\max_i\deg b_i\) and homogenize:

\[
\widetilde b(x,t)=\bigl(t^d b(x/t),0\bigr)
\quad\text{on }\mathbb A^5.
\tag{6}
\]

[De Bondt, Proposition 5.1](https://arxiv.org/pdf/1501.05168)
gives a homogeneous quasi-translation \((x,t)+\widetilde b\).
The general proposition allows the Jacobian rank to rise by one, but it
does not rise here. For \(t\ne0\), the image in (6) lies in \(S\times\{0\}\)
because \(S\) is a cone. Polynomiality extends that containment to \(t=0\).
At \(t=1\) the image contains \(b(\mathbb A^4)\times\{0\}\). Therefore

\[
\overline{\operatorname{im}\widetilde b}=S\times\{0\},
\qquad \operatorname{rank}\operatorname{Jac}(\widetilde b)=2.
\tag{7}
\]

[De Bondt, Theorem 5.3](https://arxiv.org/pdf/1501.05168)
applies to homogeneous quasi-translations of Jacobian rank two in
arbitrary dimension \(n\), and bounds their image's linear span by
\(n-2\). Apply it with \(n=5\). Equations (6) and (7) imply

\[
\dim_{\mathbb C}\operatorname{span}S\leq3.
\]

There is therefore a nonzero \(\lambda\in\mathbb C^4\) with
\(\sum_i\lambda_i b_i=0\). The nonconstant linear polynomial
\(p=\sum_i\lambda_i x_i\) is an ambient coordinate and satisfies
\(E(p)=0\). Since the original \(E\) has a slice, its kernel is regular;
the already checked regular-kernel theorem yields
\(\ker E\cong\mathbb C^{[3]}\).

Neither a gcd condition on \(b\) nor a classification of arbitrary
nonhomogeneous four-dimensional quasi-translations is needed. The cone
argument is the reason that the published homogeneous theorem reaches
this nonhomogeneous case. No assertion that square-zero Jacobians are
always strongly nilpotent is used.

## 7. Scope of the literature result

The search covered four primary papers and targeted polynomial-flow
terminology. Section 6 is a proved consequence of exact published
statements, not a quotation of an already located theorem formulated
with the double brackets in (1). The reduction from the general Riccati
system to (5), handled separately in the main pass, is not replaced by
a literature assertion here.

The quadratic-Jacobian theorems still cannot be invoked from a bound on
flow degree alone. The exact all-ones control in Section 5 remains a
guardrail against that inference and against a supposed automatic
full-rank orbit argument. Those cautions do not obstruct the distinct
cone-and-homogenization proof for the reduced case.
