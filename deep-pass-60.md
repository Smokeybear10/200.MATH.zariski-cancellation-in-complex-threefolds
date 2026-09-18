# Coordinate compatibility and excluded speed degenerations

The working question is complex-threefold cancellation:
\(A[s_*]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
This is the unconfirmed interpretation of the professor's dimensionally
inconsistent pasted statement. The unrestricted conjecture is not
proved here. The results below retain an additional supplied
coordinate-frame hypothesis throughout.


Under the full independent-defect quadratic-frame hypotheses, the
two bad-coordinate speeds cannot have a common zero at which their
Jacobian on the invariant plane is invertible. This excludes the
entire local sector in which those speeds generate the maximal
ideal, without any assumption on the intrinsic second-image ideal.

The argument uses the actual good-column graph equations. It does
not apply to arbitrary quadratic generators over an invariant base.
It leaves ramified isolated zeros, common divisor components, and
the unrestricted frame-selection problem open.

## 1. Hypotheses and statement

Retain the full actual setup of
[the generic bad-pair theorem](research/generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad Es_*=1,
\]
\[
C=\mathbb C[a,b]\subseteq A,\quad L=\operatorname{Frac}C,
\quad B_L=L[X,Y],\quad X=x_3,\quad Y=x_4,
\]
\[
E=f\partial_X+g\partial_Y,\qquad
f,g\in C,\qquad \operatorname{trdeg}_{\mathbb C}\mathbb C(f,g)=2.
\tag{1}
\]
Writing \(T_i=\partial_{x_i}\), the supplied bounds are
\(E^3x_i=0\) for every \(i\),
\(\operatorname{ad}_E^2T_i=0\) for \(i=1,2\), and
\(\operatorname{ad}_E^3T_i=0\) for \(i=3,4\).
The two top fields \(V_i=\operatorname{ad}_E^2T_i\),
\(i=3,4\), are independent, and their two-by-two
bad-coordinate projection has rank two. The invariant plane and the equality
\(B\cap L=C\) are inherited actual conclusions, not assumptions
about four arbitrary generators.

The two uniquely extended field partials \(\partial_f,\partial_g\)
commute on the finite separable extension \(L/\mathbb C(f,g)\).
Put \(\mathscr H=f\partial_f+g\partial_g\). The actual graph has
\[
h_i=E^2x_i\in C,\quad k_i,\ell_i\in L,\qquad
\mathscr Hh_i=2h_i,\quad \mathscr Hk_i=k_i,
\]
\[
x_i=\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)
                  \binom X Y
       +(\nabla_{f,g}k_i)\binom X Y+\ell_i,\qquad i=1,2.
\tag{2}
\]
These precise Hessian, gradient, and weight equations are the
relevant consequences of the true ambient good partials.

For a closed point \(P\) of \(\operatorname{Spec}C\), write
\(R=C_{\mathfrak m_P}\), \(\mathfrak m=\mathfrak m_PR\), and
\(\mathcal B=B_R\).

**Theorem.** If \(f(P)=g(P)=0\), then
\[
\boxed{\det\frac{\partial(f,g)}{\partial(a,b)}(P)=0.}
\tag{3}
\]
Equivalently, \((f,g)R=\mathfrak m\) is impossible at a
common zero in the actual setup (1)--(2).

No hypothesis about the intrinsic image ideal \(J\), first
correction jets, or the multiplicity of the primitive plinth
is added.

## 2. Regular Euler eigenfunctions at a simple zero

Suppose temporarily that
\[
f,g\in\mathfrak m,\qquad (f,g)R=\mathfrak m.
\tag{4}
\]
Their initial linear forms are a basis of
\(\mathfrak m/\mathfrak m^2\). Thus the ordinary two-by-two
Jacobian in the actual invariant coordinates \(a,b\) has
unit determinant in \(R\). Inverting that matrix expresses
\(\partial_f,\partial_g\) as \(R\)-linear combinations of
\(\partial_a,\partial_b\). These derivations preserve \(R\)
and have the prescribed values on \(f,g\), so they agree
with the unique field extensions used in (2).

In particular, \(\mathscr H\) preserves \(R\) and every
\(\mathfrak m^n\). On
\[
\operatorname{gr}_{\mathfrak m}R
  =\mathbb C[\operatorname{in}(f),\operatorname{in}(g)],
\qquad
\operatorname{gr}_{\mathfrak m}^n(\mathscr H)=n\operatorname{Id}.
\tag{5}
\]
The induced derivation multiplies every homogeneous
degree-\(n\) element by \(n\), because
\(\mathscr Hf=f\) and \(\mathscr Hg=g\).

Here the graded-ring description can be checked directly:
the initial linear terms of \(f,g\) are an invertible
linear change from \(a-a(P),b-b(P)\), and hence their
degree-\(n\) monomials are a basis of the degree-\(n\)
initial forms. There is no assumption that \(f,g\)
generate \(C\) globally.

**Eigenfunction lemma.** If \(r\in R\) and
\(\mathscr Hr=d r\), for an integer \(d\ge0\), then
\[
r=\sum_{i+j=d}c_{ij}f^ig^j,\qquad c_{ij}\in\mathbb C.
\tag{6}
\]
The zero element is included.

For a nonzero \(r\), its order \(n\) at \(P\) is finite:
write it as a polynomial numerator divided by a
denominator not vanishing at \(P\). Comparing the initial
form in its eigenvalue equation and using (5) gives
\((n-d)\operatorname{in}(r)=0\), so \(n=d\).
Choose the homogeneous polynomial \(q(f,g)\) of degree
\(d\) having that initial form. Then
\[
\mathscr H(r-q)=d(r-q),\qquad r-q\in\mathfrak m^{d+1}.
\]
If this difference were nonzero, the same finite-order
argument would give it order exactly \(d\), a contradiction.
Thus \(r=q\), proving (6).

This is an exact local-germ argument, not a finite jet
approximation. One can equivalently work in
\(\widehat R=\mathbb C[[f,g]]\), where Euler's equation
kills all coefficients outside degree \(d\), but completion
or a convergence assertion is not required.[^1]

## 3. The actual velocities make the linear terms regular

Apply (6) with \(d=2\) to the actual \(h_i\in R\).
Each \(h_i\) is a homogeneous quadratic polynomial in
\(f,g\) with complex coefficients. Therefore
\[
\nabla_{f,g}h_i\in R^2,\qquad
\operatorname{Hess}_{f,g}(h_i)\in\operatorname{Mat}_2(\mathbb C).
\tag{7}
\]
The \(k_i\) were only known to be rational, so applying
the lemma to them at this point would be unjustified.

Instead differentiate the actual graph (2) by \(E\).
This action kills its base-field coefficients. Euler's
identities give
\(\operatorname{Hess}(h_i)(f,g)^{\mathsf t}=\nabla h_i\)
and \((\nabla k_i)(f,g)^{\mathsf t}=k_i\), hence
\[
Ex_i=\frac12(\nabla_{f,g}h_i)\binom X Y+k_i.
\tag{8}
\]
Both \(Ex_i\) and the displayed linear term belong to
\(\mathcal B\). Thus \(k_i\in\mathcal B\cap L=R\).
The intersection follows from \(B\cap L=C\) by clearing
the inverted invariant denominators.

Now apply (6) with \(d=1\). Each \(k_i\) is a complex
linear combination of \(f,g\), so \(\nabla k_i\) has
constant complex entries. Subtracting the quadratic
and linear terms in (2) from the actual \(x_i\) gives
\(\ell_i\in\mathcal B\cap L=R\). Consequently
\[
x_1,x_2\in R[X,Y],\qquad
\boxed{\mathcal B=R[X,Y].}
\tag{9}
\]
The second conclusion uses that the original four
coordinates generate \(\mathcal B\) over \(R\).
Algebraic independence of \(X,Y\) is inherited from
the actual generic ring, so this is a polynomial
extension, not a quotient presentation.

## 4. The supplied slice gives the contradiction

On the whole ring in (9),
\[
E(\mathcal B)\subseteq(f,g)R[X,Y].
\]
The actual supplied slice \(s_*\) remains in \(\mathcal B\),
and \(Es_*=1\). Evaluating the resulting polynomial
ideal identity at \(X=Y=0\) yields
\[
1\in(f,g)R=\mathfrak m,
\tag{10}
\]
which is impossible. This proves (3).

The last step does not construct a new slice or assume
that the original slice was affine in the generic pair.
The original arbitrary slice is used only after full
local polynomial equality (9) has been proved.

## 5. Exact consequences and the remaining zero schemes

The theorem says that every common speed zero is a
critical point of the speed map on the actual invariant
plane. Equivalently, by the complex Nullstellensatz,
\[
\det\frac{\partial(f,g)}{\partial(a,b)}
\in\sqrt{(f,g)C}.
\tag{11}
\]
This is a necessary ideal constraint, not a converse
realization of a frame.

If a common zero is isolated, its local zero scheme
cannot be reduced. Indeed, a reduced zero-dimensional
local quotient of \(R\) is its residue field
\(\mathbb C\), which would imply \((f,g)R=\mathfrak m\),
already excluded. The theorem does not say that
positive-dimensional common-zero components are
nonreduced, nor does it eliminate nonreduced isolated
zeros.

The parameter-speed sector of
[the conditional leading-image bound](research/slice-leading-image-obstruction-pass55.md)
assumed \((f,g)R=\mathfrak m\) in addition to conditions
on \(J\) and the first jets. Under the full inherited
graph assumptions, that entire sector is now excluded.
Its earlier lower-bound implication remains logically
valid but no longer describes a possible surviving
full-frame point. The distinct reduced condition
\(JR=\mathfrak m\) does not imply the speed-ideal
condition and is not excluded by this theorem.

## 6. Why ramified speed coordinates are different

Correct Euler weights and independent polynomial
accelerations alone do not allow (6) to be used at a
ramified zero. A base-only control is
\[
f=a^2,\quad g=b^2,\qquad
\mathscr H=\tfrac12(a\partial_a+b\partial_b),\qquad
h_1=a^4,\quad h_2=a^3b,\quad k=ab.
\tag{12}
\]
Then \(\mathscr Hf=f,\mathscr Hg=g\),
\(\mathscr Hh_i=2h_i\), \(\mathscr Hk=k\), and
\(\det\operatorname{Jac}_{a,b}(h_1,h_2)=4a^6\ne0\).
The isolated speed zero at the origin is nonreduced.
The actual field derivatives are
\(\partial_f=(2a)^{-1}\partial_a\) and
\(\partial_g=(2b)^{-1}\partial_b\), so
\[
\partial_f^2h_2=\frac{3b}{4a},\qquad
\partial_g^2h_2=-\frac{a^3}{4b^3},\qquad
\nabla_{f,g}k=\left(\frac b{2a},\frac a{2b}\right).
\tag{13}
\]
These have genuine poles. This is a control of the
Euler and rank assumptions, not an example satisfying
the full actual graph, Schur complement, and slice
hypotheses.

Conversely, a nontrivial algebraic speed-field
extension is not automatically an obstruction to the
proof: \(f=a+a^2,g=b\) still has a simple zero at the
origin and a unit local speed Jacobian. Only the local
unramifiedness used in (4) is required, not global
polynomial coordinates or equality \(L=\mathbb C(f,g)\).

The theorem excludes a subcase of an already supplied
frame. It proves neither recognition of every remaining
supplied frame nor a universal way to choose such a
frame for an arbitrary cancellation problem.


## 7. A separate divisor exclusion from primitive Euler transversality

Fix an irreducible \(\pi\in C\), and now let
\(R_\pi=C_{(\pi)}\) be the height-one DVR, not the
closed-point local ring used above. Write \(\nu=\nu_\pi\)
and normalize the rational Euler field in the actual
invariant coordinates:
\[
m=\min\{\nu(\mathscr Ha),\nu(\mathscr Hb)\},\qquad
\mathscr H_0=\pi^{-m}\mathscr H.
\tag{14}
\]
Both coefficients of \(\mathscr H_0\) are regular in
\(R_\pi\), and at least one is a unit. The ordinary
coordinate derivations preserve this DVR, so
\(\mathscr H_0(R_\pi)\subseteq R_\pi\). This normalization
does not rescale the original sliced derivation \(E\)
or the primitive intrinsic derivation \(D\).

Suppose \(\mathscr H_0\pi\) is a unit. If
\(c\ne0\) is an Euler-invariant rational function,
write \(c=\pi^n u\), with \(u\in R_\pi^*\) and any
integer \(n\). The equation \(\mathscr H_0c=0\) gives
\[
0=n u\,\mathscr H_0\pi+\pi\,\mathscr H_0u.
\tag{15}
\]
Reduction modulo \(\pi\), in characteristic zero,
forces \(n=0\). This handles poles and zeros, not
just one sign of the valuation.

The Euler commutators with the uniquely extended
base partials imply
\[
\mathscr H(\partial_r\partial_s h_i)=0,\qquad
\mathscr H(\partial_r k_i)=0
\quad(r,s\in\{f,g\}).
\tag{16}
\]
Every quadratic and linear graph coefficient is
therefore regular at a transverse divisor. Subtracting
the corresponding terms from the actual good
generators places their constants \(\ell_i\) in
\(B_{R_\pi}\cap L=R_\pi\). The original generators
then give \(B_{R_\pi}=R_\pi[X,Y]\).

The supplied slice forces \((f,g)R_\pi=R_\pi\).
Choose \(\alpha f+\beta g=1\) in the DVR and put
\[
\sigma=\alpha X+\beta Y,\qquad j=gX-fY.
\]
The inverse formulas
\[
X=f\sigma+\beta j,\qquad Y=g\sigma-\alpha j
\tag{17}
\]
give an actual affine slice and
\(A_{R_\pi}=R_\pi[j]\). The original primitive
intrinsic \(D\) is a unit multiple of
\(\partial_j\) there: a nonunit multiplier would
give a common invariant prime divisor of all its
actual values, contradicting primitivity. Thus its
full plinth \(pC\) is a unit at \(\pi\).

There is also a geometric form of this test.
If \(\mathscr H_0\) is tangent to \(\pi\), it
induces a nonzero derivation of
\(\kappa=\operatorname{Frac}(C/\pi C)\). After
swapping the speeds to make \(g/f\) regular,
that residue derivation kills \(\overline{g/f}\).
A nonconstant such residue would make \(\kappa\)
finite separable over \(\mathbb C(\overline{g/f})\),
forcing the derivation to be zero. Hence
\[
\boxed{\pi\mid p\ \text{or}\ \pi\mid\gcd(f,g)
\ \Longrightarrow\
\text{constant reduced projective speed direction at }\pi.}
\tag{18}
\]
A nonconstant direction is excluded, but a constant
direction does not itself construct a surviving
frame. The [complete divisor proof](research/primitive-euler-divisor-pass59.md)
retains the actual primitivity and invariant-localization
steps.

Tangency cannot be removed from the coefficient lemma
using Euler weights and rank alone. For example
\(f=a,\ g=a+a^3b^2\), with
\(\mathscr H=a\partial_a-b\partial_b\), has the
polynomial weight-two functions \(a^2,a^3b\) of
rank two. At \(\pi=a\) the normalized field is
tangent and \(g/f\equiv1\), but
\[
\partial_g^2(a^3b)=-\frac1{4a^3b^3}.
\tag{19}
\]
This is a base-field control, not an actual
coordinate-frame realization.

## 8. The actual Jacobian and the affine-slice ideal

At a closed invariant-base point, the exact module
of actual functions affine in the generic bad pair is
\[
V=B_R\cap L[X,Y]_{\le1}=R\cdot1\oplus Ru\oplus Rv,
\qquad \mathfrak s_{\rm aff}=E(V)=(Eu,Ev)R.
\tag{20}
\]
Its finite freeness is established in the
[preceding module proof](research/affine-slice-module-pass57.md).
In this paragraph the module-basis element \(v\)
is not a speed, a base coordinate, or an asserted
ambient coordinate. The unit-ideal condition on
\(\mathfrak s_{\rm aff}\) is exactly existence of
an affine actual slice.

Let
\[
\delta_V=\det\operatorname{Jac}_{x_1,x_2,x_3,x_4}(a,b,u,v).
\]
The actual generic graph and its invariant
determinant put this nonzero determinant in \(R\).
The true ambient adjugate identity, applied to \(E\),
gives \(\delta_V Ex_i\in(Eu,Ev)B_R\) for every
original coordinate. Multiplication by the partials
of the supplied slice \(s_*\) and faithful ideal
contraction yield
\[
\boxed{\delta_V\in\mathfrak s_{\rm aff}.}
\tag{21}
\]
This is full ideal membership, not merely radical
membership. No inverse of a nonunit Jacobian is used.

For the coefficient lattice
\[
\Gamma=\{(\gamma,\alpha,\beta)\in R^3:
          \gamma+\alpha X+\beta Y\in\Delta B_R\},
\]
choose the basis corresponding to \(1,u,v\), with
matrix \(G\). If
\(\delta_C=\det\operatorname{Jac}_x(a,b,X,Y)\),
the exact determinants satisfy
\[
\Delta^3\delta_V=\delta_C\det G,\qquad
\delta_C\det G\in\Delta^3\mathfrak s_{\rm aff}.
\tag{22}
\]
The [complete cofactor proof](research/actual-frame-affine-ideal-pass58.md)
checks the powers and basis changes. A unit
\(\delta_V\) supplies a slice, but the necessary
containment alone does not force unitness.

## 9. Exhausting the quadratic functions of the faithful control

The distinction between an actual coordinate frame
and four generators over the invariant base remains
essential. In the faithful control, use
\[
R=\mathbb C[a,v]_{(a,v-1)},\qquad
\mathcal B=R[t,z,s]/(t^2-v-az),\qquad E=\partial_s,
\]
\[
X=as+tz,\quad T=t,\quad Y=vX+T,\quad q=ts+z^2.
\tag{23}
\]
Here \(v\) is a base unit, not the module element
in (20). The ring is an invariant localization of
a polynomial cylinder with smooth, nonempty, faithfully
flat fibers. Its earlier exact minimum-three
slice-gauge result is retained.

Generically
\[
z=(T^2-v)/a,\qquad
q=XT/a-v(T^2-v)/a^2.
\]
Every actual quadratic, not just an invertible
change of two chosen generators, has the unique form
\[
\boxed{\mathcal B\cap L[X,T]_{\le2}
=R\oplus RT\oplus RX\oplus RX^2\oplus Rz\oplus Rq.}
\tag{24}
\]
For necessity, write a generic quadratic as
\(A X^2+BXT+CT^2+DX+JT+F_0\). Substitution of
\(X=as+tz,\ T=t\), followed by monic reduction, gives
\[
\begin{aligned}
&a^2As^2+s(2aAtz+aBt+aD)\\
&\quad+aAz^3+(vA+aB)z^2+(vB+aC)z+vC+F_0
+t(Dz+J).
\end{aligned}
\tag{25}
\]
Comparison in the actual free monic basis first
gives \(aB\in R\), then \(vA+aB\in R\), so the
unit \(v\) forces \(A\in R\). The other coefficients
give \(D,J,aB,aC+vB,F_0+vC\in R\), exactly (24).
Generic monomial comparison proves independence.

For an actual quadratic written as
\(Q=A X^2+DX+JT+F+cz+bq\), the speed Euler
field is \(a\partial_a\), holding \(v\) fixed.
The actual necessary weight-two and Hessian equations
force
\[
A\in S=\mathbb C[v]_{(v-1)},\qquad
b=aA',\qquad c=vA'+\frac a2A''.
\tag{26}
\]
Substitution shows that \(Q\in R[X,T]\), including
the constant correction \(-vA''/2\).
The linear-gradient identities further give the
complete normal form
\[
Q=A(v)X^2+A'(v)XT+\frac{A''(v)}2T^2
+D(v)X+D'(v)T+\ell(a,v),
\quad A,D\in S,\quad\ell\in R.
\tag{27}
\]
Conversely these functions satisfy the specified
graph equations. That converse is not a realization
of the full ambient frame.

Since \(z\notin R[X,T]\), no collection of such
compatible quadratics generates \(\mathcal B\)
with the fixed bad pair. This strengthens the
earlier invertible-row repair obstruction to all
actual functions of the specified degree.
The [complete classification](research/faithful-quadratic-module-pass59.md)
and [separate audit](research/faithful-quadratic-module-audit-pass59.md)
preserve that fixed-pair scope.

An ordinary repair of a single Jacobian value also
fails to solve compatibility. In the family
\(Q_1=z+ca+X^2,\ Q_2=q+Y^2\), the actual
Jacobian determinant on \(a=0,t=1,z=0\) is
\(s-c\). Where it is nonzero, the true dual good
partial has
\[
[E,[E,\widetilde T_1]]
=\frac{2}{(c-s)^3}(\partial_a-c\partial_z)\ne0
\quad\text{on that line}.
\tag{28}
\]
The [full local calculation](research/faithful-frame-rank-obstruction-pass58.md)
uses the actual Jacobian inverse. A nonzero
Jacobian at one point does not supply the full
adjoint identities.

## 10. Published time-degree results and verification scope

For an actual LND with coordinate time degree two,
Zygadło's theorem gives the coordinate-map identities
\[
F^{\circ3}-3F^{\circ2}+3F-\operatorname{Id}=0,\qquad
F^{-1}=3\operatorname{Id}-3F+F^{\circ2},
\quad F=\exp(E)x.
\tag{29}
\]
These do not assert a cube-zero operator on every
element of the coordinate ring, nor an affine generic
slice.[^2] The same finite-difference calculation
works on a finite noncoordinate list killed by \(E^3\).

Freudenburg's degree-module algorithm stabilizes a
specified module for a specified LND using saturation
by an actual local-slice value. It does not give a
uniform stabilization bound or transfer a degree
condition between distinct derivations.[^3]
The sliced-image equivalence likewise concerns
the image ideals of the sliced derivation itself,
not \(E(V)\) for the separate module in (20).[^4]
The [source-scope note](research/coordinate-slice-degree-scope-pass58.md)
keeps these distinctions explicit.

The exact identity checks support the coefficient
expansions, actual Jacobian calculations and the
unramified/ramified controls. They do not prove the
universal regular-eigenfunction argument, all-function
membership statements, or any omitted classification
theorem. The [verification record](verification-pass-60.json)
and [proof audit](research/proof-audits-pass60-working.md)
separate those forms of evidence.

## 11. Remaining mathematical obligations

The simple-zero theorem and the transverse-divisor
theorem eliminate specified actual degenerations.
They do not prove that the common speed zero scheme
is empty. Ramified isolated zeros and constant-direction
divisors are not eliminated by this checkpoint.

The faithful fixed-pair example is completely excluded
as a source of compatible quadratic good generators.
It does not classify different bad pairs or prove a
universal low-degree slice theorem. The normalized
Jacobian containment remains necessary without an
argument forcing its ideal to be the unit ideal.

Even complete recognition of every frame of the
supplied profile would leave the unrestricted
frame-reduction problem. No human expert review,
formal proof-assistant verification, completed
historical novelty audit, professor confirmation,
or solution of general complex-threefold cancellation
is claimed.

## Sources

[^1]: The Stacks Project, [Lemma 10.160.10, Tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S), complete statement and proof. Used only for the optional coefficient-compatible completion description, not the finite-order proof.
[^2]: Jakub Zygadło, [*Minimal polynomial of an exponential automorphism of Cn*](https://arxiv.org/pdf/0801.0616), arXiv:0801.0616v1, 4 January 2008, main theorem and proof; the PDF identifies the version. The whole preprint was read. The final publisher text was not compared line by line.
[^3]: Gene Freudenburg, [*Canonical factorization of the quotient morphism for an affine Ga-variety*](https://arxiv.org/pdf/1602.08786v3), arXiv:1602.08786v3, Lemmas 4.1 and 4.3 and Theorem 4.4 with complete proofs.
[^4]: Nikhilesh Dasgupta and Animesh Lahiri, [*On image ideals of nice and quasi-nice derivations on R[X1,X2]*](https://arxiv.org/pdf/2302.13787v6), arXiv:2302.13787v6, 24 July 2026, Lemma 2.9 with proof, used only for positive-index sliced-image equivalence.
