# Constant good directions are exactly the apex directions of the velocity cone

In the square-nonzero branch of a nice sliced action on complex
four-space, the distinguished homogeneous factor from the
[leading-boundary theorem](nice-leading-boundary-pass76.md)
determines the entire constant good-direction space. A direction is
good exactly when the factor is independent of that direction.
This is an identity of spaces, not an existence theorem for either.

## 1. Precise setting and generic nonvanishing

Retain the actual polynomial ring, nice action and original slice:
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=P\cdot\partial,\qquad E(s)=1,\qquad E(P)=0,
\qquad J=\operatorname{Jac}P,\qquad J^2\ne0.
\tag{1}
\]
Let \(K=\operatorname{Frac}B\). The previous theorem supplies
\(\operatorname{rank}_KJ=2\), \(J^3=0\),
\(\operatorname{rank}_K[J\mid P]=3\), and an irreducible
homogeneous polynomial \(F\in\mathbb C[x_1,x_2,x_3,x_4]\).
The cone over the velocity image is the hypersurface \(V(F)\),
and
\[
F(P)=0,\qquad \nabla F(P)\ne0\text{ in }K^4.
\tag{2}
\]
Here the second assertion requires proof. If every partial derivative
of F vanished at P, homogeneity would make each of those derivatives
vanish on the entire image cone and hence on \(V(F)\).
Irreducibility would then make F divide every \(\partial_iF\).
Their smaller degrees force all these derivatives to be zero.
In characteristic zero that would make F constant, a contradiction.
This argument uses density of the cone over P's image, not a claim
that P itself dominates the three-dimensional cone.

## 2. The exact row-space identification

Factor the rank-one matrix over K as \(J^2=v\ell\), where v is a
nonzero column and \(\ell\) is a nonzero row. The identities
\(J^3=0\) and \(JP=0\) give \(\ell J=0\) and \(\ell P=0\).
On the other hand, differentiation of \(F(P)=0\) and the homogeneous
Euler identity give
\[
(\nabla F(P))^tJ=0,\qquad
(\nabla F(P))^tP=(\deg F)F(P)=0.
\tag{3}
\]
The annihilator of \(\operatorname{im}J+KP\) has dimension one,
because that space has dimension three. Both rows in (3) and the
preceding factorization are nonzero rows in this annihilator.
Thus
\[
\ker_KJ^2=\ker_K(\nabla F(P))^t.
\tag{4}
\]
No polynomial or unit multiplier between the rows is asserted.

For a constant vector \(c\in\mathbb C^4\), put
\(T_c=\sum c_i\partial_{x_i}\). The actual nice adjoint formula is
\((\operatorname{ad}_E^2T_c)(x)=2J^2c\).
Consequently, for the constant good space,
\[
\begin{aligned}
G_2
&=\{c\in\mathbb C^4:J^2c=0\}\\
&=\{c\in\mathbb C^4:(T_cF)(P)=0\}\\
&=\{c\in\mathbb C^4:T_cF=0\}.
\end{aligned}
\tag{5}
\]
For the last equality, \(T_cF\) is homogeneous of degree below
\(\deg F\). Its vanishing at P extends to the image cone.
It therefore belongs to the prime ideal (F), and its smaller degree
forces it to be the zero polynomial. The reverse implication is
immediate.

## 3. Geometric meaning and exact dimension alternatives

Define the translation-apex space of \(V(F)\) to consist of vectors c
such that \(V(F)+tc=V(F)\) for all \(t\in\mathbb C\).
It equals \(\{c:T_cF=0\}\). One implication follows by exponentiating
the constant derivative. Conversely, invariance of the hypersurface
makes \(T_cF\) vanish on \(V(F)\); divisibility by F and the degree
bound again force \(T_cF=0\). Therefore (5) identifies G2 with this
apex space in the original constant coordinate directions.

If F is linear, its apex space has dimension three. If F is
nonlinear and its apex space had dimension at least two, an actual
constant linear coordinate change would express F as a homogeneous
polynomial in at most two variables. Over \(\mathbb C\) every
nonconstant homogeneous binary polynomial factors into linear forms.
Irreducibility would force F to be linear, a contradiction. Hence
\[
\dim_{\mathbb C}G_2\in\{0,1,3\}\quad(J^2\ne0),\qquad
\dim_{\mathbb C}G_2\ge2\Longleftrightarrow \deg F=1.
\tag{6}
\]
For \(J^2=0\), separately, G2 is all of \(\mathbb C^4\).
The dimension-two possibility is thus excluded for nice sliced
four-variable actions, not merely recognized conditionally.

In particular, if an actual good partial is already supplied and F
is nonlinear, that partial spans the sole constant good direction.
After the corresponding genuine constant coordinate change, F omits
that exact coordinate and is an irreducible homogeneous ternary
polynomial. This does not bound its degree by two.

## 4. The recognized conic control prevents a stronger inference

Reuse the retained nice sliced action
\[
a=xz-y^2+w,\qquad
P=(1,a,a^2,-a^2x+2ay-z)^t.
\tag{7}
\]
Its homogeneous velocity cone has equation \(F=xz-y^2\):
the first three entries of P satisfy that relation, and their
homogeneous cone together with the independent fourth velocity
has dimension three. Equivalently the exact image-cone dimension
from the preceding theorem and the irreducible quadratic relation
identify its equation.
Thus (5) gives \(G_2=\mathbb Ce_w\), as independently computed
in the [pass74 control](nice-slice-adjoint-rank-pass74.md).
But \(E(F)=-E(w)\ne0\). The polynomial F is not an invariant
merely because its apex gives a good partial. This is a recognized
translation under nonlinear coordinates, not a counterexample to
recognition.

## 5. The checked apex theorem does not force another direction

De Bondt's Corollary 3.10 has a relevant implication: under its
homogeneous rank and zero-set dimension hypotheses, absence of
a nonzero apex makes the image closure properly contained in a
four-dimensional linear subspace. Its complete displayed proof
was read.[^apex]
For the homogenization used here, that conclusion is already
provided by the zero fifth component and image dimension three.
It gives no contradiction when G2 is zero. Taking its contrapositive
to produce an apex would require failure of containment in every
four-dimensional linear subspace, which is expressly false here.

Likewise the later no-linear-invariant five-variable branch is not
an apex-existence theorem applicable to this homogenization:
the homogenizing coordinate is already invariant. Neither a
Hessian representation of P nor any additional singular-Hessian
hypothesis is available from (1).

The new result is therefore the exact reduction (5), with the
dimension alternative (6). The geometric question of a nonzero
apex, and the fixed-point ideal of a primitive derived intrinsic
action when one is supplied, remain separate. No new numerical
method, general cancellation claim, historical novelty, human
expert review or formal verification is asserted. All passes
through 75 and shared metadata are unchanged.

[^apex]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), Definition 3.9 and Corollary 3.10, printed pages 16--18, including the complete displayed proof, freshly read in the [retained primary text](../tmp/pdfs/bondt-1501.04845v3.txt). The argument of Sections 1--3 is given above and uses the image-cone theorem through the separate leading-boundary note, not an unstated apex-existence conclusion.
