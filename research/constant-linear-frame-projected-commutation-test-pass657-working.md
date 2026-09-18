# A finite linear test for the complementary projected-frame criterion

Date: September 18, 2026. Private working consequence. Novelty: UNKNOWN.

For a FIXED principal polynomial retraction, the criterion656 can be
tested over ALL constant linear ambient frame changes by one finite
affine-linear system. No search over nonlinear coordinates or slices
is included. This operational consequence does not supply a successful
frame for every cancellation candidate.

## 1. Exact setup and test

Let k be a characteristic-zero field and let
\[
B=k[X_0,\ldots,X_n],\quad n\ge1,\qquad
\rho:B\longrightarrow A\subseteq B,\quad
\rho|_A=\mathrm{id},\quad \ker\rho=uB\ne0.
\tag{1}
\]
All maps are k-algebra maps. Set
\[
r_i=\rho X_i,\quad e_i=\rho\bigl((X_i-r_i)/u\bigr),\qquad
D_i=\rho\partial_{X_i}|_A,\quad B_{ij}=[D_i,D_j].
\tag{2}
\]
The r_i generate A. As established in654 and used in656, the
surjection A^{n+1} to Der_k(A) given by the D_i has kernel Ae,
where e=(e_0,...,e_n)^T is unimodular.

Seek constants lambda_0,...,lambda_n in k satisfying
\[
\sum_{i=0}^n\lambda_i e_i=1,
\tag{3}
\]
and, for every i<j<k and every 0<=l<=n,
\[
\lambda_i B_{jk}(r_l)-\lambda_j B_{ik}(r_l)
       +\lambda_k B_{ij}(r_l)=0.
\tag{4}
\]
For n=1 there are no triple equations, as expected for one selected
field.

**Exact assertion.** The system (3)--(4) has a solution if and only if
there is a constant linear ambient coordinate frame Y=S X in which
the complementary projected fields
rho partial_{Y_1}|_A,...,rho partial_{Y_n}|_A form a commuting
A-basis of Der_k(A). Such a solution therefore gives A=k^{[n]}
by656, with these fields an actual coordinate-partial frame on A.
No separate local-nilpotence assumption is required.

This conclusion recognizes A abstractly. It does not assert that the
supplied image gives B=A[u] unless that product is already an input.
In the actual-cylinder case, recognition does give
B=k[w_1,...,w_n,u].

## 2. Exterior-algebra proof and frame construction

Let V=k^{n+1} be the vector space of constant ambient directions and
define the alternating, derivation-valued form
\[
\beta(v,w)=\left[\sum_i v_iD_i,\sum_j w_jD_j\right].
\tag{5}
\]
The coefficients v_i,w_j are constants, so this is genuinely
k-bilinear. Regard lambda as a covector on V. Equation (3) makes
lambda nonzero. Equation (4), tested on every algebra generator,
is precisely the identity lambda wedge beta=0. Testing on the r_l
is sufficient because a derivation of A vanishing on its algebra
generators vanishes on A.

For any nonzero covector lambda,
\[
\lambda\wedge\beta=0
\quad\Longleftrightarrow\quad
\beta|_{\bigwedge^2\ker\lambda}=0.
\tag{6}
\]
Indeed choose v_0 with lambda(v_0)=1. Evaluating the left side on
(v_0,v,w), v,w in ker lambda, gives beta(v,w). Conversely decompose
V=kv_0 direct-sum ker lambda. By trilinearity and alternation it
suffices to evaluate on three vectors in ker lambda or on v_0 and
two such vectors. Both expressions vanish when the right side of
(6) holds. This works for any
k-vector-space-valued alternating form, including Der_k(A).

Choose a basis v_1,...,v_n of ker lambda and let M have columns
v_0,v_1,...,v_n. Then S=M^{-1} has first row lambda. In the frame
Y=S X, the constant direction partial_{Y_j} is the jth column of M,
and the new normal vector is
\[
e^Y=S e,\qquad e^Y_0=\lambda(e)=1.
\tag{7}
\]
The complementary projected fields commute by (6). Their omitted
normal component is a unit, so the exact relation-module computation
in656 makes them an A-basis. This proves sufficiency and constructs
the required constant matrix.

Conversely, let Y=S X have a commuting complementary projected
A-basis. Its omitted normal component e^Y_0 is a unit of A, hence
a scalar c in k*. Rescale the first row of S by c^{-1}. This does
not change its complementary ambient directions and makes
lambda(e)=1. Those directions span ker lambda, so (6) gives (4).
This proves necessity. Allowing constant translations Y=S X+d
does not change e^Y or the partials, hence does not change this test.

## 3. Finiteness and exact effectiveness

Every e_i and B_{ij}(r_l) is a specific polynomial in the original X
variables. For example, rho is computed by substituting the finite
polynomial list r_0,...,r_n, and
\[
B_{ij}(r_l)=
\rho\partial_{X_i}(\rho\partial_{X_j}r_l)
-\rho\partial_{X_j}(\rho\partial_{X_i}r_l).
\tag{8}
\]
Expand (3)--(4) in the finitely many monomials appearing in these
polynomials. Vanishing in A is the same as vanishing of its embedded
polynomial in B. Thus coefficient comparison gives a finite
affine-linear system over k in just n+1 unknown constants lambda_i.
There are no products of the unknowns and no hidden invertibility
condition: (3) already guarantees lambda is nonzero.

Over an exact computable coefficient field, such as Q or a specified
algebraic extension, ordinary exact linear algebra decides consistency
and constructs M and S as above. The same holds with a supplied exact
coefficient-equality and linear-algebra oracle. No effective algorithm
is asserted for arbitrary unrepresented complex constants. The finite
linear equivalence itself holds over every characteristic-zero field.

An inconsistent system excludes ALL constant linear frame choices
for the fixed rho. It excludes neither nonlinear ambient changes nor
a different retraction or slice. It is not an obstruction to A being
polynomial.

## 4. A positive instance not detected by the all-fields criterion

Use the two successive shears from654--656:
\[
v=y+x^2,\quad u=x+v^2,\qquad
x=u-v^2,\quad y=v-(u-v^2)^2.
\tag{9}
\]
Keep z,t unchanged, let E=partial_u in this whole frame, and let rho
be evaluation at u=0. Then A=k[v,z,t] and, in the order (x,y,z,t),
\[
e=(1,2v^2,0,0),\qquad
D_x=-2v^2\partial_v,\quad D_y=\partial_v,\quad
D_z=\partial_z,\quad D_t=\partial_t.
\tag{10}
\]
Equation (3) forces lambda_x=1 and lambda_y=0. Among i<j the only
nonzero commutator is B_{xy}=4v partial_v. Applying (4) to the triples
(x,y,z) and (x,y,t) forces lambda_z=lambda_t=0. Thus the exact
solution is lambda=(1,0,0,0). Its complementary triple is the
coordinate frame (partial_v,partial_z,partial_t).

As proved in654--656, no retraction with this kernel makes all four
projected partials commute in the original frame: no constant
translation T has T(u)=1. The present test succeeds nonetheless.
This is a calibration on a known polynomial cylinder, not a new
existence theorem.

There is also a nontrivial linear-selection version of this control.
Replace (x,y,z,t) by the constant frame Y=S(x,y,z,t)^T, where the
four rows of S are (1,j,j^2,j^3), j=1,2,3,4. Its Vandermonde
determinant is 12, and all four new normal components are
1+2jv^2, hence nonconstant. Nevertheless the finite test has the
unique solution lambda=(4,-6,4,-1): direct multiplication gives
lambda S=(1,0,0,0). Uniqueness follows by transporting a solution
back to the already computed original system. Thus the test really
can recover a successful constant linear frame even when no listed
normal component is a unit. The projected-field transformation is
D^Y=S^{-T}D, consistent with the column convention in Section2.

## 5. A negative instance on an actual polynomial cylinder

Use the retained curvature control22:
\[
u=t-x^2,\quad E=y\partial_x+(1+2xy)\partial_t,\qquad
a=x-yu,\quad b=y,\quad c=z.
\tag{11}
\]
The whole inverse is x=a+bu, y=b, z=c, t=u+(a+bu)^2.
Consequently E=partial_u, A=k[a,b,c], and its zero-slice normal is
\[
e=(b,0,0,1+2ab).
\tag{12}
\]
Already (3) is impossible. It reads
lambda_x b+lambda_t(1+2ab)=1; comparison of the constant term gives
lambda_t=1, while the coefficient of ab gives 2lambda_t=0.
Characteristic zero yields a contradiction.

Thus this fixed retraction has no successful complementary commuting
projected basis after ANY constant linear ambient frame change.
The base is nevertheless polynomial, and the displayed nonlinear
frame (a,b,c,u) succeeds. The negative result is exactly a limit of
the fixed-retraction linear-frame test, not a cancellation obstruction.

## 6. Antecedents and verification scope

The exact relation module and normal-vector transformation are already
in654;656 supplies the complementary-basis recognition theorem.
The negative control and its complete nonlinear inverse are already
in22, and the positive control is already in654--656. The bounded
archive comparison also included coordinate-frame-minimization and649.
No identical linear system was found in that targeted comparison.
This note records an exterior-algebra consequence of those inputs,
not a literature novelty clearance or a newly recognized family.

The author checked the controls and all-dimension exterior argument
directly without executing a script. The complete223-line saved source
at SHA256 2a7a24bad4f1e054d0438f3ea7434c8d406ac4a511d550465c1f7a0ebaa748f1
then passed separate Jet and Geometry saved-source reviews. Full EOF
reads were f413d8 and25bc9f/e68e06; unchanged final hashes/counts were
a64837 and a8ae94. Both reported CLEAN. Root read the complete saved
source in67eac5 and independently reconstructed the criterion.

Root's fresh unsaved904764 and Jet's independent06dc94 checked the
original positive, negative, and constant-r0 systems. Root's a56df8
checked the mixed Vandermonde frame. Jet's independent a64837 tested
the equations on the actual r_l, both curved inverse orders, and an
explicit reconstructed frame. Finite controls supplement the universal
written proof; they do not establish its all-frame quantifier.
Status: internally checked operational consequence; novelty UNKNOWN.
No saved checker was executed, imported, compiled, or changed.
AI reviews are not human expert or proof-assistant certification.

For a general cancellation cylinder, a successful nonlinear frame or
other recognition argument is still missing. Failure of this finite
test does not settle that existence question. General cancellation
remains UNSOLVED.
