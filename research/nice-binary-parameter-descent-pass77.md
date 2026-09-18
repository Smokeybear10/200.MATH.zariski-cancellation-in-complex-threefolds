# Exact binary parameters and their transverse zero locus

The nonlinear ternary-cone branch with a supplied constant good
direction admits a binary-form description by actual polynomial
invariants. The parameters descend with gcd one. The parametrization
alone does not make their ideal the unit ideal, but it identifies
their zero locus with the transverse velocity zero locus and gives
explicit ideal containments in both the original ring and its kernel.

## 1. Retained actual assumptions and the source input

Retain
\[
B=\mathbb C[x_1,x_2,x_3,w],\qquad E=P\cdot\partial,\qquad
E(s)=1,\qquad E(P)=0,\qquad
J^2\ne0,\qquad \operatorname{ad}_E^2\partial_w=0.
\tag{1}
\]
Assume the distinguished image-cone polynomial F is nonlinear.
The [pass76 apex theorem](nice-leading-apex-pass76.md) then makes
F an irreducible homogeneous polynomial in the three transverse
variables. Put \(A=\ker E\).
All coordinates and the slice in (1) are actual, with only the
constant change used to select the supplied good direction.

Let \(d=\max_i\deg P_i\), introduce z, and order the homogeneous
coordinates as \((x_1,x_2,x_3,z,w)\):
\[
H=(z^dP_1(x/z),z^dP_2(x/z),z^dP_3(x/z),0,z^dP_4(x/z)).
\tag{2}
\]
As in the [pass76 omission proof](nice-good-direction-invariant-omission-pass76.md),
this is a homogeneous quasi-translation with component gcd one.
Its image closure is \(V(F)\times\{z=0\}\times\mathbb A^1_w\).
Thus H5 is algebraically independent of the first four outputs,
their joint transcendence degree is two, and z is the sole
independent linear invariant.
The same proof gives the full transverse content
\[
\gcd(H_1,H_2,H_3,H_4)=c z^r
\qquad(c\in\mathbb C^*,\ r\ge0).
\tag{3}
\]
This is the full gcd, not an unidentified representation factor.

The parametrization input cited in de Bondt's Theorem 5.1(i)
has an explicit formulation in his thesis, Theorem 4.3.1:
a homogeneous polynomial tuple of transcendence degree at most
two is its full component gcd times homogeneous binary forms
evaluated on coprime homogeneous parameters of equal degree.
The complete selected proof was read.[^param]
Apply this to the five-variable tuple
\((H_1,H_2,H_3,H_4,0)\). The extra zero makes the input literally
a square polynomial tuple as in the thesis statement; it
changes neither its field nor its gcd. Absorbing c into the
binary forms yields
\[
H_i=z^r h_i(\pi,\chi)\ (1\le i\le3),\qquad
\gcd(\pi,\chi)=1,\qquad
\deg\pi=\deg\chi=n>0,\qquad
\deg h_i=e,\qquad d=r+en.
\tag{4}
\]
Zero binary forms are allowed in a general statement; in this
branch the three transverse outputs have no nonzero constant
linear relation, so the three forms are linearly independent.
In particular \(e\ge2\). No nilpotent-Jacobian hypothesis is
applied to the four-output tuple: the cited parametrization
requires only homogeneity and transcendence degree.

For clarity, the selected source proof first applies rational
Luroth to the field of output ratios. It clears a common binary
denominator and removes common binary factors. Comparing the
lowest and highest homogeneous parts of the two parameters then
forces equal homogeneous degree. The optional irreducible choice
of parameters uses a further Bertini statement; it is not needed
or claimed here.

## 2. Binary coprimality and invariant parameters

The forms in (4) can and do have
\(\gcd(h_1,h_2,h_3)=1\). Indeed (3) says their evaluations have
gcd one. If a nonconstant common binary factor existed, one of
its linear factors over \(\mathbb C\) would evaluate to a
nonconstant common factor. Every nonzero linear combination of
\(\pi,\chi\) is nonzero of degree n. Indeed the pair is coprime
of the same positive homogeneous degree, so its ratio is
nonconstant. Scaling then shows that this ratio and either
nonzero parameter are algebraically independent. In particular
the two parameters are not constant-proportional.

The parameters can also be taken invariant under H, as in
Theorem 5.1(ii). Here is the direct gate for the present choice.
All components H_i and their gcd \(z^r\) are invariant, so every
polynomial factor of each \(h_i(\pi,\chi)\) is invariant by the
locally nilpotent degree function. The union of the linear
factors of the binary h_i contains two independent forms:
otherwise their gcd would not be one and their span would have
dimension at most one. Evaluating these two forms gives two
independent constant linear combinations of \(\pi,\chi\) that
are invariant. Hence both parameters are invariant.

Define the actual polynomials
\[
p=\pi(x,1),\qquad q=\chi(x,1).
\]
Setting z=1 in (4), and using the homogeneous chain rule for the
invariant parameters, gives
\[
P_i=h_i(p,q)\ (1\le i\le3),\qquad
p,q\in A,\qquad \gcd_B(p,q)=1.
\tag{5}
\]
To verify the last assertion, any nonconstant common divisor
of p and q would homogenize to a common divisor of \(\pi,\chi\)
after powers of z are cleared. Its homogenization is not
divisible by z, so it would already divide both parameters,
contradicting (4). Neither p nor q is zero: dehomogenization is
injective on the space of homogeneous polynomials of fixed degree.
One of them may become a nonzero constant.
Their gcd in A is one as well: any nonunit divisor in A would
remain a nonunit in \(B=A[s]\).

Dehomogenization does not preserve algebraic independence of
the parameter pair. No assertion
\(A=\mathbb C[p,q]^{[1]}\), or equality of their field with the
full invariant field, has been made.

## 3. Exact control of the parameter and velocity ideals

In the binary polynomial ring \(\mathbb C[u,v]\), the three
homogeneous forms h_i have no common zero on \(\mathbb P^1\).
Their only common affine zero is therefore the origin.
There is also an explicit bound:
\[
(u,v)^{2e-1}\ \subseteq\ (h_1,h_2,h_3)\
\subseteq\ (u,v)^e.
\tag{6}
\]
For the first inclusion, choose a nonzero degree-e form f in
their span. Its projective zero set is finite. A second form g
in the span can avoid every one of those points, since the
system has no base point and \(\mathbb C\) is infinite.
Thus f and g are coprime. The map
from pairs of forms of degree e-1 to forms of degree 2e-1,
\((a,b)\mapsto af+bg\), is injective: coprimality would make
f divide b in any relation, which is impossible by degree
unless both coefficients vanish. Both spaces have dimension
2e, so the map is surjective. Multiplying by monomials gives
the entire first inclusion in (6).

For either \(R=A\) or \(R=B\), set
\(I_R=(p,q)R\) and \(L_R=(P_1,P_2,P_3)R\).
Substitution in (6) gives the scheme-theoretic bounds
\[
I_R^{\,2e-1}\subseteq L_R\subseteq I_R^e,\qquad
\sqrt{L_R}=\sqrt{I_R},\qquad
L_R=R\ \Longleftrightarrow\ I_R=R.
\tag{7}
\]
In particular the exact set-theoretic identity in the actual
four-space is
\[
V_B(P_1,P_2,P_3)=V_B(p,q).
\tag{8}
\]
Equality of the two unreduced ideals is not asserted.
The original slice gives
\[
(L_B,P_4)B=B,\qquad P_4\text{ is a unit in }B/L_B.
\tag{9}
\]
Indeed \(E(s)=\sum_iP_i\partial_i s=1\). Thus at a transverse
zero the original velocity is nonzero and lies in the supplied
constant good direction. This is not a proof that such a zero
cannot occur.

The same elementary binary reduction also proves
\(\mathbb C[u,v]\) is finite over \(\mathbb C[h_1,h_2,h_3]\).
The monomials of degree below 2e-1 generate: (6) expresses any
higher-degree monomial as forms of lower degree times h_i, and
induction decreases degree by e. Evaluation consequently makes
\(\mathbb C[p,q]\) finite over
\(\mathbb C[P_1,P_2,P_3]\). This finite-subalgebra assertion does
not identify either ring with A or with a normalized quotient.

## 4. What the parametrization does not settle

The recognized conic control permits \(p=1,q=a\), with
\(a=xz-y^2+w\), and
\((h_1,h_2,h_3)=(u^2,uv,v^2)\). Its actual transverse
velocities are \((1,a,a^2)\). The descended pair is dependent
and unimodular, even though the homogeneous parameters had
equal positive degree and were algebraically independent.

Conversely, the bare binary data
\(p=x_1,q=x_2\) and
\((h_1,h_2,h_3)=(u^2,uv,v^2)\)
have gcd one but a proper parameter ideal. They only demonstrate
the logical limit of gcd and binary parametrization. They are
not asserted to extend to a nice sliced four-coordinate action
with the required image cone.

The new usable reduction is (5)--(9). To exclude the proper
parameter ideal, one must still use the original action and
slice at its common zero locus. Neither p or q is assumed to
be a coordinate, and no constant value for \(\partial_w p\) or
\(\partial_w q\) follows here.
There is no new numerical method, regression, historical
novelty, human expert review or formal verification claim.
Frozen passes through76 and shared metadata are unchanged.

[^param]: Michiel de Bondt, [*Homogeneous Keller maps*](https://webdoc.ubn.ru.nl/mono/b/bondt_m_de/homokema.pdf), doctoral thesis, 2009, Theorem 4.3.1 and its complete displayed proof, printed pages 87--89. Its rational Luroth input is stated as Theorem 4.3.2; no new full re-audit of Igusa's cited proof is claimed. The relevant application and parameter invariance are also explicitly stated and proved in [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), Theorem 5.1(i)--(ii), printed pages 22--23, whose complete theorem proof was read in pass76 and the selected portion reread here. The thesis states additional irreducibility refinements, which are unused; only the complex coprime equal-degree conclusion is invoked.
