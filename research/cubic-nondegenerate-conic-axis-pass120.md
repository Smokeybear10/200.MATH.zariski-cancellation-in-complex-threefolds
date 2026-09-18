# A nondegenerate cubic conic has a constant ambient axis

In the supplied actual exact cubic framework, suppose Q has rank three
and its restriction to the plane ker n has rank two. Then there is a
nonzero constant vector v0 in C cubed such that n transposed v0=0 and
Qv0 is a nonzero constant covector. Thus the varying plane normals all
annihilate one fixed ambient direction. This is a necessary restriction,
not an exclusion of the nondegenerate conic case.

The argument uses the highest three coefficients of the actual cubic
unit-volume determinant, together with exactness of the linear part
of the potential. A finite algebraic constant-field extension splits
the conic. No exponential change of frame is assumed or introduced.

## 1. Actual hypotheses and a finite algebraic splitting field

Retain the full actual framework of
[potential90](nonconical-quadratic-potential-pass90.md),
[cubic-relation90](nonconical-cubic-relation-pass90.md), and
[moving-frame118](cubic-moving-frame-constraint-pass118.md). Write the
nonzero original acceleration as q0. In particular,

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z_0]=A[u],\quad Eu=1,
\quad Ez_0=q_0u,\quad q_0\in\mathbb C^*,\\
S=\mathbb C[s_1,s_2],\quad K=\operatorname{Frac}S,
\quad b=E(x_1,x_2,x_3)^t\in S^3,\quad
\det[b,b_{s_1},b_{s_2}]\ne0,\\
L=\ker(V|K)=\mathbb C(H),\quad Q\in\operatorname{Sym}_3(L),
\quad n\in L^3,\quad Q_H=\kappa n n^t\ne0,\\
n^tb=0,\quad b^tQb=-1,\quad
\operatorname{rank}Q=3,\quad \operatorname{rank}(Q|_{\ker n^t})=2,
\quad \deg_YF=3 .
\end{gathered}
\tag{1}
\]

L is relatively algebraically closed in K, by differentiating a
separable minimal polynomial with V. Over a finite algebraic extension
L' of L, split the binary form on W=ker n transposed and choose its
isotropic basis p,q with Q(p,q)=-1/2. Put r0=Q inverse n. The scalar
h0=n transposed Q inverse n is nonzero because the restriction on W
is nondegenerate. Adjoin its square root, put r=r0/sqrt(h0), and
replace n by n/sqrt(h0). After absorbing this rescaling into kappa,

\[
\begin{gathered}
Q(p,p)=Q(q,q)=0,\quad Q(p,q)=-\tfrac12,\qquad
Q(r,r)=1,\quad Q(p,r)=Q(q,r)=0,\\
n^tp=n^tq=0,\quad n^tr=1,\quad Qr=n,\qquad
b=pw+q/w\quad\text{for }w\in K':=KL' .
\end{gathered}
\tag{2}
\]

The last formula follows by expressing b in p,q: the product of its
two coefficients is one. Only square roots and algebraic operations
were used to choose this basis. The derivative d/dH has a unique
extension to L'; its constant field is C. Indeed a nonconstant element
of L' killed by it would make L' algebraic over the field generated
by that element, forcing the derivative to be zero, contrary to H'=1.

Here are the scalar-extension gates. Relative algebraic closedness and
characteristic zero make K tensor_L L' a field: a nontrivial factor
over K of a separable irreducible polynomial over L would have monic
factor coefficients algebraic over L, hence in L. The same argument
over all finite extensions makes K tensor_L algebraic-closure(L) a
domain. After base extension this proves L' is relatively algebraically
closed in K'. Otherwise the tensor product of a nontrivial finite
subextension with that algebraic closure, a product of fields in
characteristic zero, would inject into this domain. This is impossible.

w is transcendental over L'. If not, b would lie in L' cubed and V
would kill it, contradicting the moving-frame determinant. Consequently
K' is finite separable over L'(w). The commuting derivations D_H,D_w
are defined by the extended d/dH on L', D_Hw=0, D_w(L')=0 and D_ww=1.
Their commutator kills L' and w. Their uniqueness on the finite
separable extension makes it zero on K'. Moreover ker D_w=L': a
transcendental extra constant would again force D_w to vanish on K'.
Primes below mean D_H, and subscripts w mean D_w.

Extending the actual generic ring K[v,u] to K'[v,u] preserves its unit
volume and its cubic graph relation. The rational base differential
change has determinant in K' nonzero. A K'-affine choice of the generic
coordinate v also changes volume by a base scalar only. No function
of v is inverted, and no global original inverse is inferred from
the new rational or algebraic base variables.

## 2. The normalized ambient and radial connections

Differentiate every pairing in (2), using that Q' annihilates p and q.
There are a,c,d,e in L' with

\[
\begin{gathered}
p'=ap+cr,\qquad q'=-aq+dr,\qquad
r'=2dp+2cq+er,\qquad Q'=-2e n n^t,\quad e\ne0,\\
Z=cw+d/w,\qquad \ell=Z_w/Z,\qquad Z\ne0,\qquad
b_H=aw b_w+Zr,\quad b_w=p-q/w^2 .
\end{gathered}
\tag{3}
\]

In particular differentiating Q(r,r)=1 gives kappa+2e=0. The frame
determinant in the basis p,q,r is 2Z/w, so Z is nonzero. The parameters
c,d cannot both vanish.

Expanding the actual second derivatives in b,b_H,b_w gives the radial
matrix G and the connection coefficients below. Let C1 stand for
C111 only to keep the last expression short.

\[
\begin{gathered}
G_{11}=a^2+Z^2,\quad G_{12}=a/w,\quad G_{22}=1/w^2,\\
C^1_{11}=C_1=e+Z'/Z+aw\ell,\quad
C^1_{12}=\ell,\quad C^1_{22}=0,\\
C^2_{11}=w(a'-aC_1)-w^2ZZ_w,\quad
C^2_{12}=-aw\ell,\quad C^2_{22}=-1/w,\\
T_{111}=\tau=2eZ^2\ne0,\qquad
T_{112}=T_{122}=T_{222}=0 .
\end{gathered}
\tag{4}
\]

For example b_ww=b/w squared-b_w/w gives the final-column coefficients.
The other entries follow from (3). The cubic tensor can also be checked
from T_ijk=-b_j transposed Q_i b_k: Q_w=0 and n transposed b_H=Z
give exactly (4). The actual tensor remains symmetric in this commuting
frame.

## 3. Cubic potential and the highest volume coefficients

The only cubic potential monomial is q0 tau Y1 cubed/6. As in119, the
generic generating-curve lemma90 forces y1 to have degree one. Take
v=y1 and write y2=R=sum r_i v to the power i, with r3 nonzero. The
sixth and fourth potential coefficients force the two entries B22
and B12 of its quadratic array to vanish. Thus

\[
\begin{gathered}
R=r_0+r_1v+r_2v^2+r_3v^3,\qquad
r_3=-q_0\tau/(6L_2)\ne0,\quad r_1=-L_1/L_2,\\
L_i=D_i(\chi+q_0\rho^2/2),\qquad (L_1)_w=L_2',\\
\frac{\mathcal J}{\Omega L_2}
=R'+R_vR_w+C^2_{11}v+C^2_{12}R
 +(C^2_{12}-C_1)vR_v
 +(C^2_{22}-\ell)RR_v-\ell vR_v^2\ \in K'^* .
\end{gathered}
\tag{5}
\]

To verify the last line, the three-by-three determinant has gradient
L2(-R_v,1). Dividing by L2 gives K21+R_v(K22-K11)-R_v squared K12.
Here K12=ell v, K11=rho+C1v+ell R,
K21=R'+C211v+C212R, and K22=rho+R_w+C212v+C222R.
Substitution cancels rho and the orbit coordinate u and yields (5).

The fifth and fourth powers of v in (5) successively imply

\[
\begin{gathered}
(r_3)_w=(1/w+4\ell)r_3,\qquad
(r_2)_w=(1/w+3\ell)r_2,\\
r_3=k Z^4w,\quad r_2=j Z^3w,
\qquad k\in L'^*,\quad j\in L',\\
L_2=l_0/(wZ^2),\qquad l_0=-q_0e/(3k)\in L'^*,\\
0=r_3'/r_3+3(r_1)_w-(3/w+6\ell)r_1
                   +4C^2_{12}-3C_1 .
\end{gathered}
\tag{6}
\]

The last line is the coefficient of v cubed. Its terms involving
r2 squared cancel using the second equation. Each integrated constant
in (6) is justified by ker D_w=L', for instance
D_w(r3/(wZ to the power4))=0. The expressions for r3 and tau then give
L2 exactly as displayed. No logarithmic primitive is being assumed.

Exactness in (5) gives
(r1)_w=-L2'/L2-r1(L2)_w/L2. Since
(L2)_w/L2=-1/w-2ell, the r1 terms cancel from the last line of (6).
Substituting (4) and (6) leaves

\[
\begin{gathered}
0=e'/e-4l_0'/l_0-3e+7\frac{Z'-awZ_w}{Z},\\
\frac{Z'-awZ_w}{Z}
=\frac{(c'-ac)w^2+(d'+ad)}{cw^2+d},\qquad
\boxed{c'd-cd'-2acd=0.}
\end{gathered}
\tag{7}
\]

All terms outside the displayed fraction lie in L'. Differentiating
it with D_w gives 2w(c'd-cd'-2acd)/(cw squared+d) squared. Therefore
its w derivative must vanish, proving the boxed identity. This is the
only part of the remaining volume coefficients needed below; no claim
is made that it suffices for full volume or actual-frame realization.

## 4. A finite algebraic gauge gives a genuinely constant direction

Suppose cd is nonzero. Adjoin theta with theta squared=c/d if necessary.
Equation (7) gives theta'/theta=a exactly. Set
P=p/theta, U=theta q and new w=theta times the old w. These operations
preserve the conic parametrization and Q(P,U)=-1/2. Their derivatives
are P'=kr and U'=kr for k=c/theta=theta d. Hence

\[
\begin{gathered}
v_0=P-U\in\mathbb C^3\setminus\{0\},\qquad
Q(v_0,v_0)=1,\qquad n^tv_0=0,\\
(Qv_0)'=Q'v_0=0,\qquad
Qv_0\in\mathbb C^3\setminus\{0\} .
\end{gathered}
\tag{8}
\]

The constants remain C in every finite algebraic extension of L.
Thus v0 is a constant vector in the original ambient complex space,
not merely a vector constant along the w direction. The square root
used here is algebraic. No solution of an exponential differential
equation is inserted as an unverified coordinate change.

If c=0, then d is nonzero and p'=ap. Divide p by any nonzero component
of p. Every resulting component ratio has zero derivative, so the
normalized vector v0 lies in C cubed and is nonzero. It is isotropic,
n transposed v0=0, and again Qv0 is a nonzero constant covector.
If d=0, the same argument uses q. These cases exhaust the alternatives
because Z is nonzero. Thus the claimed constant direction exists in
every case, though its Q-norm can be zero.

In particular a constant ambient change can make v0 the first basis
vector. Then n has first entry zero, and the first row and column of
Q are constant. This statement is a restriction on the velocity
geometry, not a diagonalization by a base-dependent ambient map.

## 5. Scope and remaining work

The nondegenerate coefficient control in
[field-gates119, Section 4](cubic-first-integral-polynomial-gates-pass119.md)
already has a constant direction and a constant first column of Q.
Consequently this theorem does not exclude that control or establish
an original-frame inverse for it. The lower volume coefficients,
global polynomial reconstruction, and the original-coordinate
constraints still have to be used in the remaining case.

[The conic checker120](cubic_conic_axis_checks_pass120.py) is limited
to exact connection, tensor, determinant-coefficient and finite-gauge
identities. The finite-extension, constant-field, generic relation and
actual unit-volume gates are written arguments, not conclusions from
a numerical model. There is no general cancellation or novelty claim.
