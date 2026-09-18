# Constant acceleration does not force strong Jacobian nilpotence

An actual three-good, constant-acceleration frame can have a velocity
Jacobian that is nilpotent at each point but is not strongly nilpotent
under independent evaluations. The two-point calculation below makes
one proposed published triangularization route unavailable from these
hypotheses alone. The action used is already polynomially conjugate to
a translation, so this is not an obstruction to nonlinear recognition.

The frame is retained from103. The new deduction is its failure of the
strong-nilpotence condition isolated in the source audit90, not a new
family or a claim of historical novelty.

## 1. The precise source gate

Write X=(x1,x2,x3,z) for an actual polynomial coordinate system and
suppose E is a locally nilpotent derivation with
\[
\begin{gathered}
E^2x_i=0\ (i\le3),\qquad E^2z=q\in\mathbb C^*,\qquad
u=Ez/q,\quad Eu=1,\\
P=E(X),\quad J=\operatorname{Jac}_X(P),\qquad
\Phi_\tau(X)=X+\tau P+\frac q2\tau^2e_4,\\
JP=qe_4\ne0,\qquad EJ=-J^2,\qquad J^4=0.
\end{gathered}
\tag{1}
\]
These are the actual identities proved in
[frame87](constant-acceleration-three-good-frame-pass87.md).
They do not bound the ordinary degrees of P.

De Bondt's Proposition 1.3 identifies strong nilpotence of a polynomial
matrix over an infinite field with similarity by a constant matrix to
a strictly triangular polynomial matrix. Its complete displayed proof
chooses a nonzero product one factor below a minimal vanishing length,
extracts a constant kernel column, and inducts on matrix size. In four dimensions the
criterion is equivalent to vanishing of every product of four
independently evaluated matrices.
[Primary Proposition 1.3, printed p.3](https://arxiv.org/pdf/1601.00579v4).

The same paper's Theorems 3.2 and3.3 require ordinary quadratic
polynomial maps, together with respectively Jacobian rank at most two
or square-zero Jacobian. Those hypotheses are not supplied by (1).
The two-point obstruction below is stronger than merely observing
that their hypotheses have not been proved.

Quasi-translation classification has another exact gate: de Bondt's
Proposition 1.3 and Remark 1.4 in the separate quasi-translation paper
require Jac(H)H=0, equivalently that the associated derivation square
kill every coordinate. The nonzero vector JP in (1) fails that condition.
The complete displayed proof and preceding Lemmas 1.1--1.2 were read.
[Primary criterion and derivation interpretation, printed pp.3--5](https://arxiv.org/pdf/1501.05168v1).

## 2. The unchanged actual frame and its inverse

Start with independent coordinates s,a,v,p and E=partial_s. The
[actual103 control](three-good-projected-partial-obstruction-pass103.md)
has the following forward and inverse maps:
\[
\begin{gathered}
x_1=s,\qquad x_2=v+a^2s,\qquad x_3=a+v^2+ps,\\
z=2a^2v-p+a^4s+\frac{s^2}{2},\\
s=x_1,\qquad
a=x_1\left(z-\frac{x_1^2}{2}\right)-x_2^2+x_3,\\
v=x_2-a^2x_1,\qquad
p=2a^2x_2-a^4x_1-z+\frac{x_1^2}{2}.
\end{gathered}
\tag{2}
\]
Substitution in the inverse expression for a cancels every s-term
and leaves a. The other inverse expressions then recover s,v,p.
Conversely, after defining s,a,v,p from the last three lines,
x1 and x2 recover directly. Substitution gives
a+v^2+ps=a+x2^2-x1(z-x1^2/2)=x3, and the expression for z
also recovers z. These are both polynomial inverse orders, not
an inference from a constant Jacobian determinant.

Consequently this is an actual sliced polynomial action, and
\[
\begin{gathered}
P=(1,a^2,p,s+a^4)^t,\qquad u=s+a^4,\qquad q=1,\\
E^2x_1=E^2x_2=E^2x_3=0,\qquad E^2z=1,\\
\ker E=\mathbb C[a,v,p],\qquad
\mathbf b=(1,a^2,p)^t,\qquad
\det[\mathbf b,\mathbf b_a,\mathbf b_p]=2a\ne0.
\end{gathered}
\tag{3}
\]
The determinant is nonconstant and the speed map has generic rank
two. Its interpretation using the actual highest-field quotient
S=C[a,p] is already proved in103, not reconstructed from a proposed
speed parametrization. The example has a coordinate slice x1=s.

## 3. Two points rule out every strong nilpotence bound

All derivatives in this section are in the original coordinates X.
Set xi0=(0,0,0,0) and xi1=(0,0,1,0). Their a-values are zero
and one. Differentiating (2)--(3) gives
\[
J(\xi_0)=
\begin{pmatrix}
0&0&0&0\\0&0&0&0\\0&0&0&-1\\1&0&0&0
\end{pmatrix},\qquad
J(\xi_1)=
\begin{pmatrix}
0&0&0&0\\0&0&2&0\\-1&2&0&-1\\1&0&4&0
\end{pmatrix}.
\tag{4}
\]
For example, da at xi0 is dx3 and at xi1 is also dx3.
At xi1, dp=2dx2-dx1-dz and du=dx1+4dx3, which verify
the last two rows. The zero row for d(a squared) at xi0 and
the row 2dx3 at xi1 verify the remaining nonzero entries.

Their product is
\[
\begin{gathered}
M=J(\xi_0)J(\xi_1)
=\begin{pmatrix}
0&0&0&0\\0&0&0&0\\-1&0&-4&0\\0&0&0&0
\end{pmatrix},\\
\operatorname{tr}M=-4,\qquad
M^2=-4M,\qquad M^n=(-4)^{n-1}M\ne0\quad(n\ge1).
\end{gathered}
\tag{5}
\]
The last equality follows by induction, so it is not an extrapolation
from finite matrix samples. It gives nonzero alternating evaluation
products of arbitrarily large even length. If a strong nilpotence
bound existed, every longer product would vanish too. Hence no such
bound exists; already the four-factor product in (5) is nonzero.

It follows directly that no constant simultaneous similarity makes
all J(X) strictly triangular. Indeed, products of four strictly
triangular four-by-four matrices vanish. The same obstruction rules
out affine-linear triangularization of the velocity field: an affine
change replaces J by a constant conjugate evaluated at the inverse
affine point, so the set of evaluation products is unchanged up to
conjugation. Nonlinear polynomial conjugation is not covered by this
obstruction and is explicitly available in (2).

There is also no nonzero constant common kernel column. If a constant
direction C kills all entries of P, then C(a squared)=0 gives C(a)=0
in the domain, and C(s+a^4)=0 gives C(x1)=0. Formula (2) then gives
\[
0=C(a)=-2x_2C(x_2)+C(x_3)+x_1C(z)
\quad\Longrightarrow\quad C=0.
\tag{6}
\]
Thus even the first constant-kernel step in the selected source proof
cannot be deduced from (1). This provides an independent symbolic
check of the precise failed premise.

## 4. What the bounded literature check changes

The updated Dasgupta--Lahiri manuscript still defines (1) as a
three-quasi-nice frame, not necessarily strictly three-quasi-nice.
Its Lemma 2.12 assumes an actual two-variable polynomial algebra over
a fixed UFD, and its Theorem 2.13 assumes a nice three-variable
polynomial algebra over a PID. These statements do not manufacture
an invariant ambient coordinate in the four-variable setting (1).
The current v6 record, Definitions 2.2--2.3, and these stated
presentations were checked, without rereading the original Wang
proofs or the manuscript's filtration proofs.
[Primary v6, Definitions 2.2--2.3 and Lemma 2.12/Theorem 2.13](https://arxiv.org/pdf/2302.13787v6).

The bounded search also reencountered the time-polynomial flow-box
and quasi-nice sources already separated in
[the time-degree addendum](mixed-time-degree-literature-addendum.md),
[flow-box81](quadratic-flow-box-source-boundary-pass81.md), and
[source scope90](homogeneous-speed-recognition-source-scope-pass90.md).
Those retained notes were reread through EOF. Their local analytic,
fixed-base, and ordinary-degree restrictions are not new109 findings.
No newly checked primary theorem supplies the requested global
invariant coordinate or nonlinear triangularization under (1) alone.
This bounded outcome is not an exhaustive absence claim.

The new actionable conclusion is narrower: do not pursue automatic
strong Jacobian nilpotence as a universal consequence of the actual
constant-acceleration identities. It is false even for a recognized
action with nonconstant Omega. A restricted exceptional branch might
impose additional conditions, but those would require their own
proof. This example has no stable closed fiber in the intrinsic
quotient, as103 shows, and is not a model of the mixed fixed sector.

## Verification and provenance

The complete103 proof was reread and its actual inverse and velocities
reconstructed before the new evaluation calculation. An exact inline
SymPy calculation independently differentiated the original P and
checked the matrices, trace and relation M squared=-4M, exit zero,
output9535ae. It ran no unittest methods and is not a new suite.
The all-n assertion is the written induction in (5).

The second method of the later shared
[two-method checker](mixed_divisor_determinant_checks_pass109.py)
also checks both polynomial inverse orders, the actual coordinate
second derivatives, the independently differentiated two-point
Jacobians, and finite instances of the product recurrence. Its first
method concerns the separate divided-conic determinant proofs.
The complete checker was independently read through EOF here, without
execution. Neither method proves the source criterion or the universal
geometric inputs, and the finite recurrence checks do not replace
the induction. The historical inline calculation above remains a
distinct execution, not an additional unittest method.

The new primary proof read for the triangularization gate is the
complete displayed Lemma1.2 and Proposition1.3 of de Bondt1601.00579v4;
its ordinary quadratic Theorems3.2--3.3 were checked for their exact
hypotheses. The quasi-translation criterion was read with its complete
displayed proof and preceding two lemmas in the retained primary text.
No whole-paper, deeper cited-dependency, visual-PDF or novelty audit
is claimed. No files through108, shared indexes, or old tests were
changed. Independent AI reconstruction is not expert certification.
