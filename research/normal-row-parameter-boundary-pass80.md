# Proper primitive normals can pass the local jet restriction

Unimodularity of the parameter velocity, augmented rank three and the
lowest-normal-span bound from pass79 do not by themselves make the
primitive normal ideal the unit ideal. Two explicit polynomial
parameter rows show this. A formal factorization even satisfies the
nice and nilpotent matrix identities with no constant good direction,
but fails the commuting-partial equations required of an actual
Jacobian.

These are parameter and matrix controls. Neither is an actual nice
sliced action on four-space, and neither is a cancellation example.
The second row removes the first row's constant-velocity shortcut,
but not its missing actual-action hypotheses.

## 1. Two unimodular parameter rows

Work in the actual polynomial plane S=C[u,v]. For epsilon=0 or 1,
put
\[
P_\epsilon=(1+\epsilon u^2,u,v^2,uv)^t,\qquad
\lambda_\epsilon=(1,-\epsilon u,0,0),\qquad
\lambda_\epsilon P_\epsilon=1.
\tag{1}
\]
Define U=[P_u,P_v]. The signed normal is fixed by
Nq=det[P,P_u,P_v,q]. Direct minors give
\[
N_\epsilon=
(uv^2,-2v^2,-u(1-\epsilon u^2),2v(1-\epsilon u^2)),
\qquad N_\epsilon[P,P_u,P_v]=0.
\tag{2}
\]
The row is primitive: its second and third entries have gcd one.
It is nonzero, so the augmented matrix has rank three over Frac S.
The ordinary derivative matrix U has rank two as well. All four
entries of N are linearly independent over C in either case,
as is seen by their distinct monomials.

The normal ideal is nevertheless proper. Its complete zero set is
\[
\begin{aligned}
V(N_0)&=\{(0,0)\},\\
V(N_1)&=\{(0,0),(1,0),(-1,0)\}.
\end{aligned}
\tag{3}
\]
Indeed N2=-2v squared forces v=0 at a zero, and N3 then forces
u(1-epsilon u squared)=0. Conversely these equations make every
entry vanish. This determines the zero set, not a radicalization
of the displayed ideal.

At the origin the minimum order is one and the four leading
terms are (0,0,-u,2v). At u=1 or -1 in the epsilon=1 case,
write u=u0+xi and v=eta. Only the third entry has a linear term,
namely 2xi. Thus the ranks of the first nonzero normal terms are
\[
2\text{ at }(0,0),\qquad
1\text{ at }(1,0),(-1,0)\text{ for }\epsilon=1.
\tag{4}
\]
Both controls pass the necessary local bound in
[common-top79](nice-common-top-normal-identity-pass79.md), at every
proper zero of their normals. That bound therefore cannot be
replaced by a purely parameter-theoretic unit-normal assertion.

For epsilon=0, P1=1 would supply an actual linear slice in any
genuine realization, already recognizing its kernel. For epsilon=1,
no nonzero constant linear combination of the four entries is even
constant. Comparing the coefficients of u squared,u,v squared,uv
proves this directly. The stronger control therefore does not have
that particular recognition shortcut at the parameter level.

## 2. Formal nilpotence is compatible with a false derivative matrix

Abbreviate h=1-epsilon u squared, and define the two-by-four
polynomial matrix
\[
L_\epsilon=
\begin{pmatrix}
-v^2&2\epsilon uv^2&h&0\\
uv^2&-2v^2&-uh&2vh
\end{pmatrix}.
\qquad
LP=0,\qquad LU=\begin{pmatrix}0&2vh\\0&0\end{pmatrix}.
\tag{5}
\]
For the formal four-by-four product J=UL, it follows exactly that
\[
JP=0,\qquad
J^2=2vh\,P_uN\ne0,\qquad J^3=0,\qquad
\operatorname{rank}J=2,\quad\operatorname{rank}J^2=1.
\tag{6}
\]
The first component of P_u may be nonzero, but its second component
is one, so P_u is primitive as a polynomial vector. Constant linear
independence of the entries of N makes the constant kernel of J
squared zero. Thus these matrices pass that formal analogue of the
no-good-direction condition too.

The crucial failed premise is that L is the matrix of the original
coordinate derivatives of two invariant polynomials. To prove the
failure, interpret its columns as actual polynomial derivations
D_i=L_{1i} partial_u+L_{2i} partial_v of S. Then
\[
D_4u=0,\qquad D_1u=-v^2,\qquad D_4v=2vh,
\qquad [D_4,D_1]u=-4v^2h\ne0.
\tag{7}
\]
If L were Jac_x(u,v) for algebraically independent actual polynomial
invariants u,v, every original partial would preserve S because the
entries of L lie in S. Their restrictions would be these D_i and
would commute. Equation (7) contradicts that requirement.

There is a separate local-nilpotence failure: D4 fixes h and takes
v to 2hv, hence D4 to the nth power takes v to (2h) to the nth
power times v for every positive n. It is not an LND. A restriction
of an actual coordinate partial to its preserved polynomial
subalgebra would be an LND. This is another reason the displayed L
cannot be substituted for the actual original partial data.

This excludes the specific derivative matrices (5), not every
possible actual action whose parameter velocity has one of the
forms (1). The products J and JP in (6) are formal matrix products;
they are not silently called the Jacobian and niceness identity of
an action on an unspecified original coordinate ring.

## 3. The implicit homogeneous cones are singular

In target coordinates (X,Y,Z,W), the homogeneous equations of the
two parameter cones are
\[
F_0=XW^2-Y^2Z,\qquad
F_1=XZW^2-Y^2Z^2-W^4.
\tag{8}
\]
They have degrees three and four, respectively. Substitution of
P_epsilon gives zero. Each is irreducible: viewed as a polynomial
of degree one in X, its leading coefficient and constant coefficient
are coprime in C[Y,Z,W], so Gauss's lemma applies. The map
(t,u,v) to t P_epsilon(u,v) has generic differential rank three
by the augmented-rank calculation. Thus its irreducible image
closure is precisely the corresponding hypersurface in (8).

The gradient entries of either F are C-linearly independent, so
neither hypersurface has a nonzero constant translation direction.
Both are singular at the nonzero point (1,0,1,0). Their actual
parameter gradients satisfy
grad F0(P0)=u N0 and grad F1(P1)=uv squared N1, with the same
normal orientation as (2).

These statements exhibit further geometry of the parameter controls.
They do not assert that these singular cones satisfy every global
incidence property imposed by an actual homogeneous quasi-translation.
Any application of such an additional source theorem needs its own
proof and hypothesis check. No conclusion from it is presumed here.

## 4. A separate formal determinant control for the quadric investigation

At Root's request the same checker includes a distinct formal
five-row determinant needed in the concurrent quadric calculation:
\[
\begin{aligned}
&\det\begin{pmatrix}
\alpha_u&\alpha_v&0&0&1\\
\beta_u&\beta_v&1&0&0\\
\gamma_u&\gamma_v&0&1&0\\
\ell_u&\ell_v&0&0&0\\
F_u&F_v&F_Y&F_Z&0
\end{pmatrix}\\
&=\ell_uF_v-\ell_vF_u+
(\beta_u\ell_v-\beta_v\ell_u)F_Y+
(\gamma_u\ell_v-\gamma_v\ell_u)F_Z.
\end{aligned}
\tag{9}
\]
If beta_i=b_i sigma+beta_i0 and gamma_i=c_i sigma+gamma_i0,
the coefficient of sigma is the last two terms with beta_i,gamma_i
replaced by b_i,c_i. Let G be a symmetric two-by-two matrix and
ell_i=-(b_i,c_i)G(Y,Z) to the transpose+d_i. The resulting
two-entry affine vector field has linear part
\[
\Delta\begin{pmatrix}0&-1\\1&0\end{pmatrix}G,
\qquad\Delta=b_uc_v-b_vc_u,
\qquad\operatorname{tr}=0,
\qquad\det=\Delta^2\det G.
\tag{10}
\]
The checker verifies the complete signs and coefficients. It does
not prove that a determinant in (9) is a unit in an actual quotient,
that Delta and det G are nonzero in an application, or that every
invariant affine-line curve of the field is an eigenline. These
are separate written-proof obligations in that investigation.

## 5. An explicit Segre frame control

The fourth method checks the separate construction in
[the Segre frame note](quadric-segre-frame-pass80.md). It uses the
nonconstant determinant-one matrices L=((1+u squared,u),(u,1)) and
K=((1,v),(v,1+v squared)), in row order. Their tensor-product matrix
M gives the four flattened columns (pq transpose,pq' transpose,
p'q transpose,p'q' transpose). The method verifies both polynomial
inverse orders, determinant one, the determinant polar pairing,
and that its normal row is exactly row four of M inverse.

It also multiplies the first columns of L and K by independent
scalar parameters. On this scaffold the resulting tensor determinant
is the square of their product and the polar form scales by their
product. The general formula for arbitrary matrices is proved in
the written frame note, not inferred from this scaffold. Finally,
the specialization ell_i=c_i Y+b_i Z+d_i gives the exact diagonal
linear field with entries Delta and minus Delta.

These are genuine polynomial coordinate maps over C[u,v]. They are
not a construction of an original four-variable nice sliced action,
and do not themselves establish the geometric or generation premises.

## 6. Exact checks and limits

The standalone [checker](normal_row_parameter_checks_pass80.py) has
four methods and imports only unittest and SymPy. They check the
parameter rows, normal ideals and jets; formal nilpotence and its
mixed-partial failure, together with the implicit cones; and the
separate formal determinant and symmetric-matrix identity; and the
explicit Segre frame and its polynomial inverse.
No solver/research module or random numerical sampling is used.

The initial three-method file passed in 0.661 seconds, exit zero,
with full output in tool chunk `b75db0`. Removing an unused dead
conditional from the normal-minor construction changed no executed
calculation. That three-method file passed in 0.321 seconds,
exit zero, with full output in tool chunk `521a73`. There were no
failed test runs. These versions are the same three methods,
not six methods. After the distinct Segre method was added, the
final four-method file passed in 0.392 seconds, exit zero, with full
output in tool chunk `432775`. The final checker SHA-256 is
`c77a2ebbf789ad6e161abd0d434cc84c7f23575848200a7a7bdfa680712f55bf`.

The author read the complete final checker and this note through EOF
and checked whitespace. No canonical runner or capture, full regression,
shared metadata, or frozen pass79-and-earlier file was changed by
this work. The finite checks do not prove the general normal-unit
question, construct a simultaneous actual frame, certify a source
theorem, or settle cancellation. No historical novelty, human expert
review or formal proof-certificate claim is made.
