# Commuting projected translations recognize a coordinate hypersurface

For a polynomial retraction with nonzero principal kernel, commutation
of ALL projected coordinate partials forces its kernel generator to
have a linear coordinate complement. In particular its image is an
abstract polynomial ring. Local nilpotence of the projected fields
need not be assumed; it follows from the resulting coordinates.

This is a sufficient, exactly testable condition, not a proof that
an arbitrary cancellation kernel admits such a frame. There are
actual coordinate hypersurfaces for which no retraction with that
kernel meets the condition in the fixed ambient linear frame.
Novelty is UNKNOWN. The proof refines the retained projection
matrix from22; it does not claim a new general cancellation theorem.

## 1. Statement and the exact relation module

Let k be a characteristic-zero field, n>=1, and
\[
B=k[X_0,\ldots,X_n],\qquad \rho:B\longrightarrow A\subset B,
\quad \rho|_A=\mathrm{id},\quad\ker\rho=uB\ne0.
\]
Thus u is a nonzero nonunit and A is a finitely generated domain,
isomorphic to B/(u). We do NOT assume B=A[u]. Define
\[
D_i=\rho\partial_{X_i}|_A,\quad r_i=\rho(X_i),\quad
q_i=(X_i-r_i)/u,\quad e_i=\rho(q_i),\quad
h_i=\rho(\partial_{X_i}u).
\tag{1}
\]
The following conditions on this retraction are equivalent:

1. All n+1 projected derivations D_i commute pairwise.
2. The entire vector e=(e_0,...,e_n) belongs to k^{n+1}.

Under either condition the constant translation
T=sum e_i*partial_{X_i} satisfies T(u)=1. There are linear
coordinates Y_1,...,Y_n,t on B such that
\[
T=\partial_t,\qquad u=t+F(Y_1,\ldots,Y_n),\qquad
B=k[Y_1,\ldots,Y_n,u],\qquad A=k[\rho Y_1,\ldots,\rho Y_n].
\tag{2}
\]
In particular A is abstractly k^[n]. The last equality is inside B;
it does NOT assert B=A[u] for the supplied embedded image.

Here is the exact module calculation. Polynomial Taylor expansion
at X=r+u q, together with u(r)=rho(u)=0, gives
\[
u=u\sum_i q_i(\partial_{X_i}u)(r)+u^2 H
\]
for H in B. Cancel u and apply rho to obtain
\[
\sum_i h_i e_i=1.
\tag{3}
\]
Differentiate X_j=r_j+u q_j and then apply rho:
\[
D_i(r_j)=\delta_{ij}-h_i e_j.
\tag{4}
\]
The map phi:A^{n+1} to Der_k(A), sending alpha to sum alpha_i D_i,
is surjective. Indeed a derivation V of A extends to the rho-derivation
V*rho:B to A; the polynomial chain rule gives
V=sum V(r_i)D_i. Formula (4) then shows exactly
\[
\ker\phi=Ae.
\tag{5}
\]
In detail, a relation applied to every r_j gives
alpha_j=(sum alpha_i h_i)e_j, and (3)--(4) give the converse.
The r_j generate A. No abstract tangent-module freeness or assumed
nilpotence is used here.

## 2. Commutation forces the normal vector to be constant

The relation sum e_i D_i=0 and pairwise commutation imply, for each j,
\[
\sum_i D_j(e_i)D_i=0.
\]
By (5), D_j(e)=lambda_j e for some lambda_j in A. Choose an index
ell with e_ell nonzero. In K=Frac(A) it follows that every D_j
kills every ratio e_i/e_ell. By surjectivity of phi, every derivation
of A kills these ratios. Every k-derivation of K becomes a derivation
of A after multiplying by a suitable nonzero element of A, by
clearing denominators on its finitely many generators. Thus all
k-derivations of K kill the ratios.

In characteristic zero this makes each ratio algebraic over k:
a transcendental element can be included in a transcendence basis,
and the corresponding partial derivation extends across the finite
separable field extension. Since K is a subfield of k(X_0,...,X_n),
the elements of K algebraic over k belong to k. Hence e_i=c_i e_ell
with c_i in k. Equation (3) makes e_ell a unit of A. All units of
A are in k*, since they remain units of B. Therefore every e_i is
constant, proving condition2.

Now T=sum e_i partial_i is a nonzero constant locally nilpotent
derivation. Equation (3) says rho(Tu)=1, so
\[
T(u)=1+uQ\qquad(Q\in B).
\tag{6}
\]
T(u) cannot be zero, since u is a nonunit. Put d=deg_T(u)>=1.
If Q were nonzero, the right side of (6) would have T-degree
d+deg_T(Q)>=d, while the left has degree d-1. Thus Q=0.
Choose linear coordinates with T=partial_t. The equality T(u)=1
gives u=t+F(Y), proving the ambient assertions of (2).
The isomorphism B/(u) to A sends each Y_i to rho(Y_i), so it also
proves the image assertion and algebraic independence in (2).

Conversely suppose e is constant. The preceding T-degree argument
does not use commutation and gives (2) again. In the linear frame
(Y,t), formula (4) gives
\[
(\rho\partial_{Y_i}|_A)(\rho Y_j)=\delta_{ij},\qquad
(\rho\partial_t|_A)(\rho Y_j)=0.
\]
Thus these projected fields are exactly coordinate partials and zero.
Changing back by a constant invertible matrix proves that all the
original D_i commute. In fact each is a constant linear combination
of commuting intrinsic coordinate LNDs.

## 3. The exact fixed-embedding existence boundary

For a nonzero nonunit u in B, there exists a principal-kernel
retraction with commuting projected partials IF AND ONLY IF some
constant translation T has T(u)=1. Necessity was just proved.
For sufficiency write u=t+F(Y) and use the retraction fixing Y and
sending t to -F(Y). Its image is k[Y] and its projected fields commute.

This is stronger than merely asking whether u is an ambient
coordinate. For example in k[x,y,z,t] put
\[
v=y+x^2,\qquad u=x+v^2.
\]
The pair (u,v) is polynomial coordinates, with inverse
x=u-v^2, y=v-(u-v^2)^2. Nevertheless for a constant translation
T=alpha*partial_x+beta*partial_y+gamma*partial_z+delta*partial_t,
\[
T(u)=\alpha+v(4\alpha x+2\beta).
\]
Since x,v are algebraically independent, this cannot equal one:
the coefficient of v forces alpha=beta=0, contradicting the constant
term. Therefore NO retraction with kernel (u) has all projected
partials commuting in this fixed linear frame, even though u really
is a coordinate. A nonlinear change of the ambient coordinate frame
can of course use (u,v,z,t) itself.

## 4. Application to a supplied slice, and all slice shifts can fail

For an actual sliced LND E on B with E(u)=1 and B=A[u], the
retraction is the finite Taylor map
\[
\rho(f)=\sum_{m\ge0}\frac{(-u)^m}{m!}E^m(f),
\qquad A=\ker E.
\]
Its normal vector in (1) is e_i=rho(E X_i). Thus the theorem is
a finite exact recognition certificate in the supplied data E,u:
test that these n+1 polynomials are constants, or equivalently
test every bracket [D_i,D_j] on the finite generating set r_k.
No separately assumed LND condition on the D_i is needed.
If the certificate succeeds, (2) supplies intrinsic coordinates
a_i=rho(Y_i); the ALREADY GIVEN product B=A[u] then gives
B=k[a_1,...,a_n,u]. It also supplies n independent commuting
intrinsic LNDs partial_{a_i}. This conclusion does not construct
a successful certificate when the test fails.

Even changing the slice cannot always help in a fixed ambient frame.
On B=k[x,y,z,t] take
\[
E=y\partial_x+\partial_t,\quad
A=k[a=x-yt,b=y,c=z],\quad u=t.
\]
The entire inverse is x=a+bu,y=b,z=c,t=u. The four projected fields are
\[
D_x=\partial_a,\quad D_y=\partial_b,\quad
D_z=\partial_c,\quad D_t=-b\partial_a.
\]
Here [D_y,D_t]=-partial_a and e=(b,0,0,1), so the criterion fails.
Every other polynomial slice of THIS E is u'=t+h(a,b,c). Since
E(X_i)=(b,0,0,1) already belongs to ker E, retraction at ANY such
slice leaves e unchanged. Consequently no polynomial slice choice
repairs all projected commutators in this fixed frame. The actual
adapted frame (a,b,c,t) succeeds. This is an all-h statement, not
a bounded slice-shift search.

## 5. Abstract recognition does not straighten an embedded retraction

The retained648 family has
\[
B=k[x,y,z,t],\quad F_g=x+y+x^{2g}y^2,\quad
\rho(x)=F_g,\ \rho(y)=0,\ \rho(z)=z,\ \rho(t)=t,
\qquad g\ge1.
\]
Its image is A=k[F_g,z,t] and its kernel is (y). Direct projection
gives D_x=D_y=partial_{F_g}, D_z=partial_z, D_t=partial_t and
e=(-1,1,0,0). All projected fields commute, as the present theorem
permits. But648 proves B is not A[y]. For example over k(y,z,t),
the polynomial F_g has x-degree2g, so
[Frac(B):Frac(A)(y)]=2g. Its compatible-action obstruction is stronger
still. The constant T=-partial_x+partial_y satisfies T(y)=1 but
does not kill the embedded image A. Neither this theorem nor its
proof may substitute T for the supplied retraction's kernel action.

## 6. Verification, antecedents, and the remaining goal

The exact matrix and projected-connection facts already occur in22,
and the first-jet commutator defect is in23. This note derives the
stronger all-projected-fields criterion from that matrix and extends
it to principal retractions without a cylinder premise. A targeted
archive check of22,23,26,74,648,649 found no identical stated criterion;
that is not a literature novelty audit. The principal-retraction
countercontrol648 is explicitly reused, not claimed as new here.

Jet proposed the all-projected-fields criterion, root proposed the
principal-retraction extension and fixed-embedding/all-slice tests,
and General independently reconstructed the entire argument.
Root's fresh unsaved129454 checked the whole simple slice control,
its inverse and projected bracket, sample slice shifts, and the
648 projection formulas. The all-degree assertions have the written
proofs above; finite controls are not their proof.
The complete 230-line saved source at SHA256
c44f15f2c3a4dd2b769cdab33dc3dfa7775eced3111b69085598cc695c78bc6e
passed separate General and Jet reviews. Their complete EOF reads
were d251db and 09827d; unchanged final hashes were checked in
353830 and ebed6c. Both reported CLEAN, including arbitrary-field
constants, the converse, all slice shifts, and the embedded-image
boundary. Jet's independent fresh c77884 checked the full controls.
Root reread the complete saved source in eb3b16 and independently
checked both inverse orders and the constant-translation obstruction
of Section3 in fresh unsaved764d11. These checks supplement rather
than replace the uniform written arguments.

A bounded primary-source comparison read Liu--Sun, *Retracts that
are kernels of locally nilpotent derivations*, Theorem2.5 and
Remark2.6, including the complete proof (root turn5768view0):
https://dml.cz/bitstream/handle/10338.dmlcz/149581/CzechMathJ_72-2022-1_11.pdf
Their product theorem assumes the supplied image is already the
kernel of a nonzero ambient LND; the cited alternative assumes a
generic polynomial fiber. Neither hypothesis follows from the
commuting projected regular fields here, as Section5 demonstrates.
This is a scope distinction, not an originality determination.
Status: internally checked conditional theorem; novelty UNKNOWN.
No saved checker was executed, imported, compiled, or edited.

For the cancellation problem, a successful ambient frame with this
constant-normal property is still NOT supplied. The examples show
why neither fixed-coordinate retraction changes nor slice changes
alone guarantee it. The full goal remains UNSOLVED. AI reviews
are not expert review, proof-assistant certification, or novelty evidence.

Subsequent [criterion656](three-commuting-projected-partials-unit-normal-recognition-pass656-working.md)
weakens the requirement to a commuting complementary A-basis. It
succeeds on Section3's nonlinear coordinate in the SAME fixed frame.
Thus this note's failure of the all-fields test must not be read
as failure of every projected-field recognition criterion.
