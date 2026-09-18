# Polynomial base pullbacks cannot restore the cubic cylinder branch

In the supplied actual nonconical constant-acceleration frame, the exact
cubic relative branch cannot have velocity
\(b=(s,p(s,t),f(s))^t\), where s,t are polynomial coordinates of the
actual invariant plane, \(p_t\ne0\), and \(f\in\mathbb C[s]\).
This includes polynomial pullbacks whose speed row is unimodular.
The endpoint uses the irreducibility of an actual affine-linear original
coordinate, not just the unit-speed-row contradiction for a literal
cylinder velocity.

No general cubic frame has been reduced to this form. Entry of an
arbitrary sliced derivation into the supplied framework, recognition
outside this velocity class, and general cancellation remain unproved
here. This is a written mathematical deduction, not a novelty claim or
a formal or human-expert certificate.

## 1. Exact hypotheses and a rational commuting frame

Retain the full actual invariant-plane and volume hypotheses of
[invariant-plane88](constant-acceleration-invariant-plane-pass88.md),
[potential90](nonconical-quadratic-potential-pass90.md), and
[cubic-relation90](nonconical-cubic-relation-pass90.md). In particular,
S is the full kernel on A of the actual intrinsic LND W, and W kills u.
The new velocity hypothesis is

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\mathbb C[s,t]=\ker(W|A),\qquad K=\mathbb C(s,t),\\
Ex_{\rm tr}=b=(s,p(s,t),f(s))^t,\qquad
p\in S,\quad p_t\ne0,\quad f\in\mathbb C[s],\\
\Lambda=f-sf'\ne0,\qquad
\Omega=\det[b,b_s,b_t]=p_t\Lambda\ne0.
\end{gathered}
\tag{1}
\]

Assume the exact degree of the relative evaluation kernel90 is three.
No polynomial inverse to the base map (s,t) to (s,p) is assumed.
On K define

\[
\begin{gathered}
D_p=p_t^{-1}\partial_t,\qquad
D_s=\partial_s-(p_s/p_t)\partial_t,\qquad [D_s,D_p]=0,\\
D_s(s)=1,\ D_s(p)=0,\ D_p(s)=0,\ D_p(p)=1,\qquad
\ker(D_p|K)=\mathbb C(s),\\
D_sb=(1,0,f')^t,\qquad D_pb=(0,1,0)^t,\qquad
\det[b,D_sb,D_pb]=\Lambda.
\end{gathered}
\tag{2}
\]

The commutator follows directly by differentiating the displayed
coefficients, or by its vanishing on the transcendence basis s,p:
K is algebraic and separable over \(\mathbb C(s,p)\), so a derivation
killing that field is zero on K. The asserted kernel is simply the
kernel of \(\partial_t\) on \(\mathbb C(s,t)\), since its scalar
multiplier is nonzero. On \(\mathbb C(s)\), D_s is the usual
s-derivative. These statements do not replace K by \(\mathbb C(s,p)\).

## 2. Why the actual potential and volume survive this change

Let \(y^{\rm old}\) be the two actual relative variables90, defined
using \(b,b_s,b_t\). Their new tangent components are

\[
\begin{gathered}
y_1=y^{\rm old}_1,\qquad
y_2=p_s y^{\rm old}_1+p_t y^{\rm old}_2,\\
x_{\rm tr}=b(u+\rho)+(D_sb)y_1+(D_pb)y_2,\quad \rho\in K,\\
K[y_1,y_2]=A_K=K[v],\qquad
\ker\bigl(K[Y_1,Y_2]\longrightarrow A_K\bigr)=(F),\quad \deg_YF=3.
\end{gathered}
\tag{3}
\]

The two-by-two matrix here is invertible over K, so it preserves both
the algebra generated and the exact total degree of its plane relation.
The radial coefficient rho is unchanged. Equivalently, the new
three-column frame differs from the old one by a block-diagonal change
fixing the radial column. No ambient automorphism is inferred from
this matrix identity.

Extend D_s,D_p to K[v,u] by killing v,u. They commute. All of90's
mixed-derivative, potential, and row-operation calculations therefore
apply with these two derivations. They use actual derivatives of b,
not arbitrary connection arrays. The quadratic radial coefficients
and rho-derivative terms transform compatibly, or can be recomputed
directly by the same determinant calculation. In particular there is
a scalar \(\chi\in K\) and the same symmetric potential formula
as in90 in this new frame.

The decisive unit property also survives. The differential bases
(du,ds,dt,dv) and (du,ds,dp,dv) differ by determinant p_t in K*.
Thus the original-coordinate determinant in the latter basis is the
former divided by p_t, still in K*. The actual ring after passage to K
is K[v,u]; no function involving v is inverted. Changing its generic
coordinate v by a K-affine transformation likewise multiplies the
determinant only by an element of K*. These are the exact hypotheses
needed in the scalar coefficient argument below.

## 3. The cylinder differential argument is unchanged

Use \(g=f''/\Lambda\) and \(\tau=-g'-2sg^2\). Relative to
D_s,D_p, the radial array has only G11=g nonzero; the only nonzero
connection entries are \(C^1_{11}=-sg\) and \(C^2_{11}=-pg\).
The cubic tensor has only T111=tau nonzero. The proof of
[cylinder118, Sections 2--4](cubic-cylinder-velocity-exclusion-pass118.md)
now applies with p in place of its second coordinate, for the following
explicit reasons.

The unique cubic monomial makes y1 have generic degree one, by the
same actual K[y1,y2]=K[v] argument. Put v=y1 and write y2=R, cubic in
v. The v-six and v-four potential coefficients give
\(D_p^2\rho=D_sD_p\rho=0\). By (2), these imply
\(\rho=A(s)+c_0p\), with \(A\in\mathbb C(s)\) and
\(c_0\in\mathbb C\). Indeed D_p rho lies in C(s), and D_s
annihilates it; subtracting its constant multiple of p leaves an
element of ker D_p.

The unit determinant is
\(D_sR+R_vD_pR+sgvR_v-pgv\in K^*\).
Its v-five and v-four coefficients put the leading two coefficients
of R in C(s). Its v-three and v-two coefficients make the remaining
two coefficients affine in p over C(s). Since p is transcendental
over C(s), comparing the p-coefficient of the v-one term is valid.
The potential then gives the same independent expression for that
affine slope h. Thus

\[
\rho=A(s)+c_0p,\quad A\in\mathbb C(s),\ c_0\in\mathbb C,
\qquad
h=-\frac14\left(3sg+\frac{\tau'}{\tau}\right),\qquad
h'+h^2+sg h-g=0.
\tag{4}
\]

All integrations just used are justified by ker D_p=C(s), not by an
unstated triviality of the finite extension K/C(s,p). The rational
function h and all its derivatives in (4) belong to C(s).

The all-degree Laurent argument in cylinder118 therefore gives

\[
f(s)=a s^3+c s,\qquad a\in\mathbb C^*,\ c\in\mathbb C,
\qquad \rho=A(s)+c_0p(s,t).
\tag{5}
\]

For completeness, degree at most one would make tau zero. For degree
n at least two the residual in (4) has leading coefficient
\(-(3n-1)(n-3)/16\) at s inverse squared, forcing n=3. For a cubic
\(a s^3+b s^2+c s+d\), the next two residual coefficients are
\(35b/(64a)\), and after b=0, \(-315d/(64a)\). These force (5).
No unit-row conclusion is used at this stage.

## 4. Global coordinate irreducibility gives the contradiction

Let \(X=x_3-cx_1\). The actual reconstruction (3) and (5) imply
\(x_1=s(u+\rho)+y_1\) and
\(X=a s^3(u+\rho)+3a s^2y_1\). Eliminating y1 gives

\[
X=3a s^2x_1-2a s^3u-2a s^3\rho,
\qquad s^3\rho\in B\cap K=S.
\tag{6}
\]

Here the intersection equality has actual invariant content. An
element of B lying in K is killed by E, hence belongs to A. It is
also killed by W, whose full kernel on A is S. Conversely S belongs
to both rings. Thus the displayed equality follows without faithful
flatness of any newly introduced base map.

Using rho from (5), (6) gives
\(s^3A(s)=s^3\rho-c_0s^3p\in S\cap\mathbb C(s)=\mathbb C[s]\).
The last intersection is literal for S=C[s,t], as follows by comparing
t-coefficients. Write \(T(s)=s^3A(s)\in\mathbb C[s]\) and
\(h_0=-2aT(0)\). Then (6) gives

\[
X-h_0\in sB,\qquad
E(X-h_0)=f(s)-cs=a s^3\ne0,
\qquad E(s)=0.
\tag{7}
\]

But X-h0 is an actual affine-linear coordinate of the original
polynomial ring B, so it is irreducible there. The embedded base
coordinate s is nonconstant and therefore a nonunit in B, whose only
units are complex constants. The divisibility in (7) consequently
makes X-h0 a nonzero constant multiple of s. Applying E contradicts
the two derivative identities in (7). This proves the exclusion.

## 5. Scope and verification boundary

The [principal-open example118](cubic-principal-open-frame-control-pass118.md)
and its pullback with \(p=st-1\) satisfy the complete local potential
and volume identities. The latter has a globally unimodular polynomial
speed row, so the earlier literal-cylinder unit-row endpoint cannot
exclude it. The present original-coordinate irreducibility argument
explains why it still cannot extend to the required global polynomial
frame. Its explicit slice pole is a concrete manifestation of that
failure, not an assumption in this proof.

The coordinate hypothesis on s is retained in (1). This note does not
infer it from a rational first integral or from a rank-one cubic tensor.
Nor does it perform a global inverse to (s,t) to (s,p). A birational
or finite base change by itself supplies no ambient coordinate system.

The proof uses the earlier cylinder118 scalar calculation as a
prerequisite, but replaces its endpoint. It needs no recognition
theorem80, global conic presentation, or completed-fiber analysis.
Its new algebraic steps are the commuting rational-frame transfer,
the full-kernel intersection, and irreducibility of an original
coordinate. No new primary theorem or numerical execution was used.
The shared finite [checker118](cubic_moving_frame_checks_pass118.py)
tests the local examples and selected scalar identities, not this
all-degree transfer or the existence of any global original frame.
The separate one-method [transfer checker118](cubic_pullback_transfer_checks_pass118.py)
checks rational-derivation, moving-frame reconstruction and scalar-residue
identities for \(p=st-1\) and \(p=t^2+st\), the latter a genuinely
degree-two generic base map. Its residue test uses a finite polynomial
T. Neither checker proves the rational constant field, the all-degree
Laurent argument, the full-kernel intersection, or coordinate
irreducibility. Both code files were read through EOF here without an
additional execution; author runs and the canonical capture remain
separate evidence.
