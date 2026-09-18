# A known smooth factorial threefold with a squared cuspidal plinth

Smoothness and factoriality of the ambient threefold do not force
normality of the pullback of a sole squared plinth prime. A member
of the established second-kind Koras--Russell family gives an exact
control, including its entire LND filtration and all image ideals.

This is a scoped calculation in a known nonpolynomial threefold.
It does not construct such an action on \(\mathbb C^{[3]}\), establish
a polynomial cylinder, or settle the prime-square rank-three case.
No novelty is claimed for the variety or its additive action.

## 1. The actual algebra and action

Put
\[
A=\mathbb C[a,b],\qquad f=b^2-a^3,\qquad
B=A[s,t]/(f^2t-s^5+b).
\tag{1}
\]
The same letters denote the residue classes in \(B\). Define
\[
D(a)=D(b)=0,\qquad D(s)=f^2,\qquad D(t)=5s^4.
\tag{2}
\]
Then \(B\) is a smooth affine UFD of dimension three, \(D\) is a
primitive nonzero LND, and
\[
\ker D=A,\qquad \ker D^2=A\oplus As,\qquad
\operatorname{pl}(D)=f^2A.
\tag{3}
\]
The irreducible reduced plinth curve \(V_A(f)\) is the cusp
\(b^2=a^3\). Its actual pullback is integral and nonnormal:
\[
B/fB\simeq\mathbb C[a,s,t]/(s^{10}-a^3).
\tag{4}
\]
Thus the distinction between the reduced plinth curve and its
normalization is present in this actual action, not only in an
abstract proposed finite curve map.

## 2. Domain, smoothness, and factoriality

In the UFD \(A[s]\), the elements \(f^2\) and \(s^5-b\) have
greatest common divisor one. The polynomial in (1), viewed as
a polynomial in \(t\), is primitive and linear over
\(\operatorname{Frac}(A[s])\). It is therefore irreducible and
prime in \(A[s,t]\). This also gives the actual inclusion
\[
B\hookrightarrow A_f[s],\qquad t=(s^5-b)/f^2,
\qquad B_f=A_f[s].
\tag{5}
\]
In particular, \(A\) embeds in \(B\), and \(B\) is a
three-dimensional domain.

For the defining polynomial \(F=f^2t-s^5+b\),
\[
F_t=f^2,\qquad F_b=1+4bf t,
\qquad F_a=-6a^2f t,\qquad F_s=-5s^4.
\tag{6}
\]
At every point with \(f\ne0\), \(F_t\ne0\). At every point
with \(f=0\), \(F_b=1\). The Jacobian criterion proves
smoothness at every point, including the entire fiber over the
base cusp.

Reducing (1) modulo \(f\) eliminates \(b=s^5\) and gives (4).
The polynomial \(s^{10}-a^3\) is irreducible, since \(3\) and
\(10\) are coprime. More explicitly, the map
\[
\mathbb C[a,s]\longrightarrow\mathbb C[\lambda],\qquad
a\longmapsto\lambda^{10},\quad s\longmapsto\lambda^3
\tag{7}
\]
has kernel \((s^{10}-a^3)\): reduction to degree less than three
in \(a\) leaves monomials with distinct exponents modulo three.
Consequently \(fB\) is prime. The localization \(B_f\) in (5)
is a UFD. Nagata's factoriality criterion now proves that \(B\)
is a UFD.[^nagata]

## 3. The whole action and its full degree modules

The ambient triangular derivation in (2) annihilates \(F\), so
it induces a derivation of \(B\). Its exponential is the
polynomial action fixing \(a,b\) and sending
\[
\begin{aligned}
s&\longmapsto s+f^2T,\\
t&\longmapsto t+5s^4T+10s^3f^2T^2+10s^2f^4T^3
                  +5sf^6T^4+f^8T^5.
\end{aligned}
\tag{8}
\]
Substitution preserves \(f^2t-s^5+b\) exactly. Equivalently,
\(D^2s=0\), \(D^6t=0\), and \(D^5t=5!f^8\ne0\).
Thus \(D\) is a nonzero LND. Its image ideal in \(B\) is
\((f^2,5s^4)B\). Since \(f\) is prime and does not divide
\(s\), these coefficients have no common nonunit divisor.
This proves primitivity.

The equation \(s^5=b+f^2t\) is monic in \(s\), so every
element of \(B\) has a unique finite expression
\[
\sum_{q\ge0}\sum_{0\le i<5}c_{iq}s^it^q,
\qquad c_{iq}\in A.
\tag{9}
\]
On the localization (5), \(D=f^2\partial_s\), and
\(s^it^q=s^i(s^5-b)^q/f^{2q}\) has exact \(s\)-degree
\(i+5q\). Distinct pairs in (9) have distinct such degrees.
Their leading coefficients cannot cancel. Hence (9) gives the
full degree filtration, not only an upper bound on chosen generators:
\[
F_j:=\ker D^{j+1}
=\bigoplus_{i+5q\le j,\ 0\le i<5}A s^it^q.
\tag{10}
\]
In particular \(F_0=A\) and \(F_1=A\oplus As\), proving
all of (3).

For completeness, define the higher image ideal
\(I_j=D^j(F_j)\subseteq A\), with \(I_0=A\). Write uniquely
\(j=i+5q\), \(0\le i<5\). The unique degree-\(j\) basis
element has
\[
D^j(s^it^q)=j!f^{2j-2q}.
\]
All lower-degree basis elements are killed by \(D^j\). Therefore
\[
I_j=f^{\,2(j-\lfloor j/5\rfloor)}A
\qquad(j\ge0).
\tag{11}
\]
All these image ideals are principal. Neither their principality
nor the existence of the explicit adapted basis (9) forces a
normal plinth pullback in this smooth factorial setting.

The same basis makes \(B\) a free, hence faithfully flat,
\(A\)-module. Thus even faithful flatness of the actual quotient
is available in the control.

## 4. The actual nonnormal divisor and its quotient fibers

Equation (7) identifies the divisor ring as
\[
B/fB=\mathbb C[\lambda^3,\lambda^{10},t]
\subset\mathbb C[\lambda,t].
\tag{12}
\]
The rational element \(\lambda=a/s^3\) belongs to its fraction
field and is integral, since \(\lambda^3=s\). It does not
belong to the ring in (12): exponent one is not in the numerical
semigroup generated by three and ten. Its normalization is
\(\mathbb C[\lambda,t]\). The surface is nonnormal along the
whole line \(a=s=0\), as also follows from its Jacobian ideal.

The reduced plinth curve has normalization
\[
a=\mu^2,\qquad b=\mu^3.
\]
Since \(b=s^5\) on the pullback, the normalized curve map in
this example is exactly
\[
\mathbb A^1_\lambda\longrightarrow\mathbb A^1_\mu,
\qquad \mu=\lambda^5.
\tag{13}
\]
The surface (4) is a cylinder over the singular curve
\(s^{10}=a^3\). Over a nonzero point of \(V_A(f)\), the
actual quotient fiber consists of five disjoint affine lines,
corresponding to the five roots of \(s^5=b\). Over the cusp
point \((a,b)=(0,0)\), the full scheme fiber is
\[
\operatorname{Spec}\mathbb C[s,t]/(s^5),
\tag{14}
\]
a nonreduced fiber whose reduction is one affine line. The
action fixes that reduced line. Away from \(f=0\), (5) gives
the affine-line product quotient.

Thus a smooth total space, an irreducible reduced boundary,
affine-line normalizations, and a finite normalized curve map
coexist with the base cusp and the nonnormal pullback. The
normalized map (13) is finite; no properness of the full
threefold quotient is asserted or used.

## 5. Established Koras--Russell provenance and the exact boundary

Petitjean's primary paper treats the second-kind family
\[
x+y(x^d+z^{\alpha_2})^\ell+t_P^{\alpha_3}=0,
\quad d\ge2,\quad\ell\ge1,\quad
2\le\alpha_2\le\alpha_3,
\quad\gcd(\alpha_2,d)=\gcd(\alpha_2,\alpha_3)=1.
\tag{15}
\]
Our equation is literally this equation under
\[
x=b,\quad y=t,\quad z=-a,\quad t_P=-s,
\qquad (d,\ell,\alpha_2,\alpha_3)=(2,2,3,5).
\tag{16}
\]
All parameter hypotheses hold. The paper records smooth
topological contractibility and \(\operatorname{ML}(B)=\mathbb C[x,z]
=A\), and gives the primitive action
\(\alpha_3t_P^{\alpha_3-1}\partial_y
-(x^d+z^{\alpha_2})^\ell\partial_{t_P}\), which becomes
exactly (2).[^petitjean] In particular \(B\not\simeq\mathbb C^{[3]}\),
since the latter has Makar--Limanov invariant \(\mathbb C\).
These classification and topological statements are imported
known facts, not consequences newly proved by the calculations here.

The family and its action-classification boundary were already
retained in [intrinsic rank pass34](intrinsic-rank-pass34.md),
Section 5 and its second-kind source note, and
[literature scope pass34](literature-scope-pass34.md).
This note isolates the exact squared plinth, its nonnormal
pullback, and the full image-ideal calculation relevant to the
current normality question. It does not claim a new variety,
a new Koras--Russell action, or priority for these computations.

The original target still assumes the much stronger condition
that the ambient ring itself is \(\mathbb C^{[3]}\). The example
does not meet that condition, and no claim about a polynomial
cylinder or stable polynomiality is made. What it rules out is
an automatic-normality argument based only on smoothness,
factoriality, faithful flatness, contractibility, primitivity,
a single squared plinth prime, or the principal higher images
in (11). A successful polynomial-threefold argument needs
additional information.

## 6. Verification scope

The domain, smoothness, primitivity, exact filtration, image
ideals, and divisor normalization are proved above. Fresh
unsaved exact algebra independently checked the entire defining
equation under (8), its infinitesimal tangency, the nonzero
last derivative of \(t\), and the residue equation (4).
No saved checker was executed or imported. These finite checks
support, but do not replace, the uniform basis proof of (10)--(11).
The author read this source completely through EOF before its
HELD handoff. Independent saved-source review is still required.

[^nagata]: [Stacks Project, Lemma 10.120.7, Nagata's criterion for factoriality](https://stacks.math.columbia.edu/tag/0AFU), full statement and proof directly read. It applies to the Noetherian domain \(B\), localization at powers of its prime element \(f\), and the UFD in (5).

[^petitjean]: Charlie Petitjean, [*Automorphism groups of Koras--Russell threefolds of the second kind*](https://arxiv.org/pdf/1507.06087), Introduction and Section 2, printed pp. 1--4, directly read. The Introduction states the parameter range and smooth contractibility; Section 2 records the Makar--Limanov invariant and the displayed primitive LND. Only those assertions, with the exact parameter match (16), are imported here. No cancellation conclusion is drawn from the paper's introductory discussion.
