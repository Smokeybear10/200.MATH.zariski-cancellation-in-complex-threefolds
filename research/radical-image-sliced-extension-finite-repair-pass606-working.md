# Finite repair from radical divisibility of the image

Date: 2026-09-17

Status: bounded working proof. Separate complete saved-source review is
required before canonical acceptance.

## 1. The result and its limits

Let \(R=\mathbb C[x_1,\ldots,x_m]\), let \(D\) be a locally nilpotent
derivation of \(R\), and let \(0\ne a\in\ker D\). Let \(b\) be a product
of the distinct irreducible factors of \(a\), with \(b=1\) if \(a\) is
a unit. For \(P\in R\), consider the whole triangular extension

\[
B=R[t],\qquad E=aD+(1+DP)\partial_t.
\tag{1}
\]

We prove the following sufficient condition without any homogeneity
assumption:

\[
DP\in bR
\quad\Longrightarrow\quad
B=\mathbb C[Z_1,\ldots,Z_m,U],\quad
EZ_i=0,\quad EU=1.
\tag{2}
\]

The proof gives finite polynomial formulas and proves both inverse
directions. In particular,
\(\ker E=\mathbb C[Z_1,\ldots,Z_m]\). It does not require \(P\in bR\),
and it does not invert \(a\) in the final coordinate ring.

There is also an exact criterion in a stated homogeneous subclass.
Suppose \(a\) is nonconstant ordinary homogeneous, and suppose \(DP=0\)
or \(DP\) is ordinary homogeneous of strictly positive degree. Then

\[
\begin{split}
DP\in bR
&\quad\Longleftrightarrow\quad E\text{ has no zero on }\mathbb A^{m+1}\\
&\quad\Longleftrightarrow\quad E\text{ has a polynomial slice}\\
&\quad\Longleftrightarrow\quad
E\text{ is polynomially conjugate to }\partial_U.
\end{split}
\tag{3}
\]

Neither \(D\) nor \(P\) needs to be homogeneous in the sufficient
condition or this necessity proof; the explicitly stated grading
hypotheses concern \(a\) and \(DP\).

The necessity direction has a larger scope: if \(a\) is homogeneous
nonconstant and \(\psi\) is any positive-degree homogeneous polynomial,
a slice for \(aD+(1+\psi)\partial_t\) forces \(\psi\in bR\).
No membership in \(D(R)\) is used for that implication. The sufficiency
proved here, however, requires the supplied presentation \(\psi=DP\).

This concerns coefficients already presented as \(DP\). It does not
assert that every sliced coefficient of an extension belongs to \(D(R)\),
even modulo \(\ker D\). It is not a general cancellation theorem or an
entry theorem for arbitrary sliced derivations.

## 2. Invariant factors and finite evaluated flows

Every irreducible factor of \(a\) is \(D\)-invariant. For instance,
the \(D\)-degree of a product in a characteristic-zero domain is the
sum of its factors' \(D\)-degrees. Since \(Da=0\), each factor has
degree zero. Thus

\[
Da=Db=0,\qquad b^K\in aR
\quad\text{for some positive integer }K.
\tag{4}
\]

One can take \(K\) to be the maximum multiplicity of a factor of \(a\).
Multiplicative complex units do not affect the ideal condition.
The unit case will be separated below.

For \(Q\in R\), define \(\Theta_w(Q)\) by first forming the finite
independent-parameter flow

\[
\Theta_T(Q)=\sum_{j\geq0}\frac{T^jD^jQ}{j!}\in R[T],
\tag{5}
\]

and then substituting \(T=w\). For a polynomial parameter \(w\), this
substitution is a ring homomorphism on \(R\). It must not be identified
with the exponential of the variable-coefficient derivation \(wD\):
that derivation need not be locally nilpotent.

The extension \(E\) in (1) is locally nilpotent. Its restriction to
\(R\) is the invariant replica \(aD\), and
\[
E^jt=(aD)^{j-1}(1+DP)\qquad(j\geq1)
\tag{6}
\]
terminates. These assertions on the algebra generators imply local
nilpotence on \(B\).

## 3. Inverting the base map modulo a nonreduced divisor

Assume \(a\) is not a unit and \(DP\in bR\). Set

\[
\phi(Q)=\Theta_P(Q),\qquad \eta(Q)=\Theta_{-P}(Q)
\quad(Q\in R).
\tag{7}
\]

Both maps fix \(a\) and \(b\), and therefore induce endomorphisms on
\(R/aR\) and \(R/bR\). The derivation \(D\) descends to these quotients.
On \(R/bR\), the class \(\bar P\) belongs to \(\ker\bar D\).
Here, and only after this invariance is established, the evaluated
maps in (7) are the genuine exponentials
\(\exp(\bar P\bar D)\) and \(\exp(-\bar P\bar D)\). They are mutual
inverses. This statement is valid for this possibly reducible quotient:
the finite exponential identities hold over any characteristic-zero
algebra with a locally nilpotent derivation.

Consequently the whole endomorphisms

\[
\sigma=\phi\circ\eta,\qquad \tau=\eta\circ\phi,\qquad
\Delta=\sigma-\mathrm{id},\qquad \Delta'=\tau-\mathrm{id}
\tag{8}
\]

satisfy

\[
\Delta(R),\Delta'(R)\subset bR,\qquad
\Delta(b^jR),\Delta'(b^jR)\subset b^{j+1}R
\quad(j\geq0).
\tag{9}
\]

The latter inclusions use that both compositions fix \(b\) exactly,
not just modulo \(a\). By (4), their induced additive differences on
\(R/aR\) have \(K\)-th powers zero. Thus the induced \(\sigma\) and
\(\tau\) are bijective ring maps. Their inverses as additive maps are
the finite geometric sums
\(\sum_{j=0}^{K-1}(-\Delta)^j\) and
\(\sum_{j=0}^{K-1}(-\Delta')^j\), respectively. An additive inverse to
a bijective ring homomorphism is automatically a ring homomorphism.

It follows that \(\phi\) itself induces an automorphism of \(R/aR\).
Explicitly, \(\eta\sigma^{-1}\) is its right inverse and
\(\tau^{-1}\eta\) is its left inverse; a map with both is bijective.
This uses both compositions and does not infer invertibility from only
a formal first-order approximation.

In particular, the finite whole polynomial

\[
h=\eta\!\left(\sum_{j=0}^{K-1}(-\Delta)^j(P)\right)\in R
\tag{10}
\]

satisfies

\[
\phi(h)\equiv P\pmod{aR}.
\tag{11}
\]

Indeed \(\phi(h)=\sigma\sum_{j<K}(-\Delta)^j(P)\), whose difference
from \(P\) is a signed \(\Delta^K(P)\in aR\).
Any other whole lift with property (11) works as well.

The difference \(\phi-\mathrm{id}\) need not raise powers of \(b\).
For example, with \(D=\partial_r\), \(P=g+fr^2\), and \(b=f\),
the induced map modulo \(f\) translates \(r\) by \(g\). It is the
compositions in (8), not \(\phi\) alone, to which (9) applies.

## 4. Whole repaired coordinates and both inverse directions

Put

\[
W=P-at,\qquad Z_i=\Theta_W(x_i),\qquad
T=t-\frac Pa=-\frac Wa\in B_a.
\tag{12}
\]

The \(Z_i\) are whole polynomials. The finite-flow chain rule gives

\[
EW=-a,\qquad EZ_i=0,\qquad ET=1,\qquad
a(Z)=a,\qquad b(Z)=b.
\tag{13}
\]

Modulo \(a\), the tuple \(Z\) is \(\phi(x)\). By (11),
\(h(Z)-P\in aB\), so

\[
U=t+\frac{h(Z)-P}{a}
  =T+\frac{h(Z)}a\in B,\qquad EU=1.
\tag{14}
\]

The displayed division is exact polynomial divisibility.

The map \((x,t)\mapsto(Z,T)\) is an automorphism of \(B_a\).
In independent target symbols \((X,\lambda)\), its inverse is

\[
x_*=\Theta_{a(X)\lambda}(X),\qquad
t_*=\lambda+\frac{P(x_*)}{a(X)}.
\tag{15}
\]

In the forward-then-inverse composition the flow parameters are
\(W\) and \(aT=-W\). In the reverse composition,
\(P(x_*)-at_*=-a\lambda\), so the two flow parameters again cancel.
The flow fixes \(a\), which licenses both substitutions. Thus these
are both entire localized inverse identities.

The repaired map \(\mathcal F:(x,t)\mapsto(Z,U)\) is the preceding
map followed by \(T\mapsto T+h(Z)/a\). It fixes \(a\). Its full
localized inverse, now in independent symbols \((X,U)\), is

\[
\begin{aligned}
\lambda_*&=U-\frac{h(X)}{a(X)},\\
x_*&=\Theta_{a(X)U-h(X)}(X),\\
t_*&=U+\frac{P(x_*)-h(X)}{a(X)}.
\end{aligned}
\tag{16}
\]

Both compositions equal the identity by (15) and the inverse shear.
The entries \(x_*\) in (16) are already polynomial. The remaining
denominator also clears, as follows.

On \(B/aB\), the derivation in (1) is

\[
\bar E=(1+\overline{DP})\partial_t.
\tag{17}
\]

Since \(DP\in bR\) and \(b^K\in aR\), the element
\(\overline{DP}\) is nilpotent. Thus \(1+\overline{DP}\) is a unit.
From \(EU=1\),
\[
\partial_t\bar U=(1+\overline{DP})^{-1}.
\tag{18}
\]
Characteristic zero now implies that \(\bar U\) is affine in \(t\),
with a unit leading coefficient in \(R/aR\). Together with the base
automorphism induced by \(\phi\), this proves that the entire induced
\(\bar{\mathcal F}\) is an automorphism of \((R/aR)[t]\). No
reducedness of \(R/aR\), or irreducibility of \(a\), has been used.

For any \(v\in B\), write
\(\mathcal F_a^{-1}(v)=Q/a^j\) with \(j\geq0\) minimal.
If \(j>0\), then \(\mathcal F(Q)=a^jv\), since \(\mathcal F(a)=a\).
Injectivity modulo \(a\) forces \(Q\in aB\), contradicting
minimality. Hence all localized inverse images lie in \(B\).
Injectivity of \(\mathcal F\) follows from the localized inverse
and \(B\hookrightarrow B_a\). Thus (16) gives both whole polynomial
inverse directions, and

\[
E\mathcal F=\mathcal F\partial_t,\qquad
B=\mathbb C[Z_1,\ldots,Z_m,U],\qquad
\ker E=\mathbb C[Z_1,\ldots,Z_m].
\tag{19}
\]

If \(a\) is a nonzero complex unit, (12) and (15) are already
polynomial maps on \(B\). Taking \(U=T\) proves (2) directly;
the condition \(DP\in bR=R\) is then vacuous.
The case \(DP=0\) is also included without an exception.

## 5. Necessity for any homogeneous positive coefficient

Assume \(a\) is nonconstant ordinary homogeneous. Let \(\psi\in R\)
be any ordinary homogeneous polynomial of degree \(e>0\), and set
\(E_\psi=aD+(1+\psi)\partial_t\). Suppose a polynomial \(u\in B\)
satisfies \(E_\psi u=1\). There is no assumption \(\psi\in D(R)\)
in this necessity argument.

Each irreducible factor \(p\) of \(a\) is homogeneous and
\(D\)-invariant. Reducing the whole identity modulo \(p\) gives

\[
1=(1+\bar\psi)\partial_t\bar u
\quad\text{in }(R/pR)[t].
\tag{20}
\]

Thus \(1+\bar\psi\) is a unit of \(R/pR\). This quotient is an
ordinary connected positively graded domain, whose units are precisely
\(\mathbb C^*\): the highest degrees in a product of two nonzero
polynomials add, so a nonconstant element cannot have a polynomial
inverse. But \(\bar\psi\) is homogeneous of degree \(e>0\), or is
zero. Therefore it must be zero. This holds for every prime factor
of \(a\), and distinct prime factors are coprime in the UFD \(R\).
Consequently \(\psi\in bR\).

The same necessary divisibility follows if \(E_\psi\) merely has no
zero. If some homogeneous prime factor \(p\) of \(a\) does not divide
\(\psi\), there is a complex point \(v\in V(p)\) with \(\psi(v)\ne0\).
Choose \(\lambda\in\mathbb C^*\) with
\(\lambda^e\psi(v)=-1\). Homogeneity gives
\(a(\lambda v)=0\) and \(\psi(\lambda v)=-1\), so every coefficient
of \(E_\psi\) vanishes at \((\lambda v,t)\), for any \(t\).
This contradicts the absence of zeros.

Conversely, in the image subclass \(\psi=DP\), radical divisibility
also excludes zeros directly. At a zero of \(E\), one would have
\(DP=-1\). The identity
\(DP=\sum_i(\partial P/\partial x_i)D(x_i)\) implies that some
\(D(x_i)\) is nonzero there. Then \(aD(x_i)=0\) forces \(a=0\),
which, by \(DP\in bR\), forces \(DP=0\), a contradiction.
This direct converse uses the image presentation.

Together with Section 4 these facts prove every equivalence in (3).
The case \(DP=0\) satisfies radical divisibility immediately.
Polynomiality of the kernel is a conclusion of the rectification,
not a separate equivalent condition asserted without a slice.

## 6. Whole controls and assumption boundaries

A small example exhibits the strict distinction between \(P\) and \(DP\).
Take

\[
R=\mathbb C[x,y,z],\qquad
D=x\partial_y+y\partial_z,\qquad a=x^2,\qquad P=y.
\tag{21}
\]

Here \(P\notin xR\), but \(DP=x\in\operatorname{rad}(aR)\).
One may use the simple lift \(h=(1-x)y\), since
\(\phi(h)=(1-x^2)y\equiv y\pmod{x^2}\).
Write \(W=y-x^2t\). The entire repaired coordinates are

\[
\begin{aligned}
X&=x,&Y&=y+xW,&Z&=z+yW+\frac{xW^2}{2},\\
U&=(1-x+x^2)t-y.
\end{aligned}
\tag{22}
\]

For their entire inverse put \(V=X^2U-(1-X)Y\). Then

\[
x=X,\qquad y=Y+XV,\qquad
z=Z+YV+\frac{XV^2}{2},\qquad t=(1+X)U+Y.
\tag{23}
\]

The two full compositions are identities; directly,
\(EX=EY=EZ=0\) and \(EU=1\). This is a nonlinear two-step base
derivation, not just the one-variable translation case.

The positive-degree condition in Section 5 cannot simply be dropped.
For \(D=\partial_z\), \(a=x^2\), and \(P=z\), one has \(DP=1\),
not divisible by \(x\), while
\[
E=x^2\partial_z+2\partial_t,\qquad u=t/2
\tag{24}
\]
is sliced and polynomially rectified by
\((x,y,z-x^2t/2,t/2)\).

The homogeneity of \(a\) also has a genuine role in necessity, even
when \(DP\) has positive homogeneous degree. Set

\[
D=\partial_z,\quad a=(1+x)y-1,\quad P=xz,\quad
E=a\partial_z+(1+x)\partial_t.
\tag{25}
\]

Then \(DP=x\notin aR=\operatorname{rad}(aR)\), but the whole coordinates

\[
u=yt-z,\qquad v=(1+x)z-at,\qquad
t=v+(1+x)u,\qquad z=yv+au
\tag{26}
\]

satisfy \(Eu=1\), \(Ev=0\), and give a polynomial inverse with \(x,y\)
fixed. Here \(1+x\) is a nonconstant unit modulo \(a\). This is
exactly the possibility excluded by the connected homogeneous quotient
in Section 5.

## 7. Evidence and scope

Fresh unsaved algebra checked both whole inverse orders in (22)--(23),
the entire nonlinear correction for \(D=\partial_r\),
\(a=f^2\), \(P=g+fr^2\), and the necessity boundaries above.
For the nonlinear correction, inverse compositions were evaluated in
their polynomial dependency order, preserving their entire identities.
The written finite argument, not a grid of examples, proves (2)--(3).

The finite inverse-denominator mechanism extends the argument written
in [pass 603](homogeneous-replica-top-removal-sliced-counterexample-pass603-working.md),
whose earlier internal precedent is
[pass 22](radical-noninvariant-pass22.md), Section 2.
The new point here is to use both compositions in (8) when \(P\) itself
does not vanish modulo the radical. No novelty or exhaustive literature
claim is made.

Nothing above puts an arbitrary coefficient into the image of \(D\),
divides an invariant replica out of a supplied extension, or recognizes
arbitrary sliced derivations on four-space. In particular, the
point-free-to-slice implication is restricted to the exact subclass
in (3), not all additive actions. No global degree-minimum
claim follows. No canonical file was edited, and no saved checker was
executed, imported, or compiled.
