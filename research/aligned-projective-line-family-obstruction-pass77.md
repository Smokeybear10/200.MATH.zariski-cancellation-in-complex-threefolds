# An aligned projective parameter cannot give the proposed nonlinear cone

This note excludes one explicit class in the line-family construction.
It does not classify all three-variable maps with nilpotent Jacobian,
or prove that a general velocity cone is a conic. The important extra
condition is that the projective direction depends on a particular
original linear coordinate, and that its velocity component in that
same direction is used to normalize the vector.

## 1. The aligned-parameter obstruction

Let x,y,z be independent variables, let A be a nonzero polynomial in
C[x,y,z], and let f,g belong to C(y). Suppose that the three entries of

\[
H=A h,\qquad h=(f(y),1,g(y))^t
\tag{1}
\]

are polynomials, and that K=Jac H is nilpotent over C(x,y,z).
Then either rank K is at most one, or the image of H is contained in
a linear plane through zero. In particular this class cannot have
rank two and a nonlinear conical image.

All the following calculations are over the actual fraction field;
no polynomiality of f or g is initially assumed. Define

\[
D_0=f\partial_x+\partial_y+g\partial_z,\qquad
D_1=f'\partial_x+g'\partial_z.
\tag{2}
\]

The product rule factors the full Jacobian as

\[
K=[h\mid A h']\binom{dA}{dy},\qquad
\binom{dA}{dy}[h\mid A h']
=\begin{pmatrix}D_0A&A D_1A\\1&0\end{pmatrix}.
\tag{3}
\]

If UV is nilpotent, then VU is nilpotent: for a sufficiently large
n, (VU)^(n+1)=V(UV)^nU=0. Thus the displayed two-by-two matrix has
trace and determinant zero. Since A is nonzero, this gives
D0A=D1A=0. Its two annihilating derivations also give

\[
[D_0,D_1]A=(f''\partial_x+g''\partial_z)A=0.
\tag{4}
\]

If f'g''-f''g' is nonzero, equations D1A=0 and (4) imply Ax=Az=0.
Then D0A=0 gives Ay=0. Hence A is a nonzero complex constant, and
H depends only on y, so rank K is at most one.

If f'g''-f''g'=0, the functions 1,f,g are linearly dependent over C.
Indeed, when f'=0, f is constant. Otherwise (g'/f')'=0, so
g'=c f' and g=c f+d for complex constants c,d. Here the constants
of the rational derivative on C(y) are C, as follows directly by
differentiating a reduced rational fraction. Multiplying the resulting
constant linear relation on h by A gives a linear relation on H.
This proves the assertion.

The theorem is covariant under simultaneous constant linear changes
of source and target. It does not justify a nonlinear change making
a general source parameter equal to y: such a change need not
preserve the original Jacobian nilpotence condition.

## 2. What the actual line-family inverse would add

For a polynomial H in three variables, consider

\[
\Psi(s,y)=(s,y+sH(y)).
\tag{5}
\]

As proved in [pass75, Section1](nice-good-direction-construction-boundary-pass75.md),
an actual polynomial inverse makes the transported derivation
E=Psi_*(partial_s) a nice polynomial LND with original coordinate
slice s. The inverse also forces K to be nilpotent. The exact
constant-good-direction test is K^2(v-cH)=0 for a constant vector
(c,v). Thus the original partial partial_s is good precisely when
K^2H=0.

If rank K=2 and the image closure of H is a two-dimensional cone,
then H is generically in im K. To see this, the generic image is
smooth in characteristic zero, im K is its tangent plane, and the
radial vector H is tangent to a cone. A rank-two nilpotent matrix of
size three has K^3=0, so H in im K implies K^2H=0. This explains
the proposed construction route. Section1 blocks it only when (1)
holds; it does not prove that every such cone has an aligned
projective parameter.

Neither this tangent calculation nor nilpotence constructs the
polynomial inverse of (5). That requirement remains separate.

## 3. An actual inverse control and the missing good-slice condition

The standard nilpotent-Jacobian example recorded by Chamberland and
van den Essen is H=(a,z+2xa,-a^2), where a=y-x^2.[^cv]
Its entire family (5) has an explicit inverse. Writing its outputs
as (s,X,Y,Z), set

\[
\begin{aligned}
 a&=Y-X^2-sZ,\\
 x&=X-sa,\qquad z=Z+sa^2,\qquad y=a+x^2.
\end{aligned}
\tag{6}
\]

Substitution verifies both orders against
X=x+sa, Y=y+s(z+2xa), Z=z-sa^2. This is an actual inverse,
not a Jacobian-determinant argument. Its image is the nonconical
parabolic cylinder H3=-H1^2. Direct multiplication gives
K^2H=a^2(1,2x,-2a)^t, which is nonzero, while
K^2=(1,2x,-2a)^t(2a,0,1). Consequently the induced nice action's
original partial partial_s is not good. Its constant good space
is exactly the original y direction, since
-c a^2+2a v_x+v_z=0 forces c=v_x=v_z=0.

This is an already recognized action with a linear slice and a
single good direction. It is not a nonlinear conical-image example
for H and does not pass the proposed good-slice gate.
More precisely, it is the retained conic seed, not a new family:
in the actual output coordinates make the constant change
(x_seed,y_seed,z_seed,w_seed)=(s,X,-Z,Y). Then
a=w_seed-y_seed^2+x_seed z_seed and its velocity is exactly
(1,a,a^2,-a^2 x_seed+2a y_seed-z_seed).

## 4. Source and unresolved scope

The selected Chamberland--van den Essen statements concern graph
components H3=h(H1,H2), with additional source-variable restrictions
in their main classification. They do not automatically cover the
nonlinear cone sought here. In fact a rank-two image which is a
polynomial graph through zero and also a cone must be a linear
plane: scaling its graph equation forces h(tu,tv)=t h(u,v).

The retained [de Bondt Theorem4.3](https://arxiv.org/html/1501.06046v4)
assumes (Jac H)H=(trace Jac H)H in addition to transcendence degree
at most two of C(tH). With nilpotence this requires KH=0, not
merely the K^2H=0 obtained above. Its quasi-translation classification
is therefore not applied to the unresolved case.

The remaining construction question is an actual polynomial inverse
for (5), together with a nilpotent rank-two K and nonlinear conical
image, without the aligned parameter (1). No such example, or a
general exclusion, is supplied here. The source parametrization in
[the binary descent note](nice-binary-parameter-descent-pass77.md)
does not make its parameters original linear coordinates or give
the alignment in (1).

Verification: the author read the complete saved proof through EOF.
The inverse control and its K^3, K^2H identities were checked in a
bounded inline symbolic calculation, with both inverse orders zero.
No standalone suite or numerical method was added. This is not a
historical novelty claim. The full general cancellation and actual
frame-existence questions are unchanged.

[^cv]: Marc Chamberland and Arno van den Essen, [*Nilpotent Jacobians in dimension three*](https://chamberland.math.grinnell.edu/papers/essen.pdf), the example on printed p.4, Theorem2.1 on p.5, and Proposition3.3 on pp.10--11. The primary PDF was downloaded to `/tmp/chamberland-essen-pass77.pdf`; these statements, the introductory scope, and the complete displayed proof of Proposition3.3 were read. No complete proof audit of every classification dependency is claimed. The new elementary argument in Section1 does not use that classification.
