# Finite converse to the midpoint saturation criterion

Working result: when the first-potential polynomial is nonconstant,
the midpoint saturation condition is equivalent to the full all-X
polynomial return. A unit divided-difference ideal makes a finite
inclusion a ring epimorphism; its residue fibers then force equality
by Nakayama's lemma.

The polarization identity, divided-difference necessity, and exceptional
zero-slope analysis are already in the completely read
[326, Sections 2--4](principal-paraboloid-all-specializations-differential-obstruction-pass326-working.md).
They are reproduced to specify the converse, not claimed as new
obstructions. The converse is an elementary finite-map argument;
no novelty claim is made. Two controls distinguish immersion from the
global criterion and show why finiteness matters.

## 1. Abstract hypotheses and statement

Let L be any field of characteristic zero. Fix scalars
m,k1,k2,p,h,nt,ns,ell in L with m nonzero, and set
\[
\mathcal F(P,V)=\frac{k_2}{2}P^2+pPV+\frac h2V^2+n_tP+n_sV.
\tag{1}
\]
These labels are scalars in the abstract theorem, not assumptions about
derivations on L. Let y,sigma,theta,w belong to L[v], and assume
\[
L[y,\sigma,\theta]=L[v],\qquad
mw=\ell-(2\sigma+k_1)y-\mathcal F(\sigma,\theta).
\tag{2}
\]
For an independent variable X define
\[
\begin{gathered}
a_X=y+X\sigma,\qquad b=\sigma^2+k_1\sigma+m\theta,
\qquad c_X=w+X\theta,\\
R=L[X,a_X,b,c_X]\subseteq T=L[X,v].
\end{gathered}
\tag{3}
\]
The letter T in (3) denotes a ring, not a divided difference.
For independent u,v, write
\[
[q]=\frac{q(u)-q(v)}{u-v}\in L[u,v],\quad
S=[\sigma],\quad Y_d=[y],\quad T_d=[\theta],\quad B_d=[b].
\tag{4}
\]
These are polynomials on the diagonal as well as off it. Bars below
mean arithmetic means of the two function values. Define
\[
\begin{aligned}
\Gamma&=\sigma(u)+\sigma(v)+k_1,\qquad
\nu_c=\mathcal F_V(\bar\sigma,\bar\theta)/m,\\
f_c&=2\bar y+\mathcal F_P(\bar\sigma,\bar\theta)-\Gamma\nu_c,\\
I&=(B_d,\,Y_d+XS,\,Sf_c)\subseteq L[X,u,v].
\end{aligned}
\tag{5}
\]

**Finite-converse theorem.** If b is nonconstant, the following are
equivalent:
\[
\begin{aligned}
&R=T;\qquad I=L[X,u,v];\\
&(B_d,f_c):S^\infty=L[u,v];\qquad
S^N\in(B_d,f_c)\text{ for some integer }N\geq0.
\end{aligned}
\tag{6}
\]
The saturation is the union of (B_d,f_c):S^N for N nonnegative.
If S is identically zero, it is the unit ideal and the last condition
holds with N=1. That case is handled directly, without a fraction
with zero denominator. The equivalence between the last three
conditions does not need b nonconstant. The converse to R=T is where
finiteness is used.

## 2. Existing polarization and the zero-S boundary

Quadratic polarization in (1), applied to (2), gives
\[
\begin{aligned}
B_d&=\Gamma S+mT_d,\\
m([w]+XT_d)&=-\Gamma(Y_d+XS)-Sf_c+(X-\nu_c)B_d.
\end{aligned}
\tag{7}
\]
No derivative of a coefficient or a moving X occurs. Consequently
\[
([a_X],\,[b],\,[c_X])=I
\quad\text{as ideals of }L[X,u,v].
\tag{8}
\]
This is exactly the finite identity of326 in the present notation.
It does not need a surface-level equation.

Choose a polynomial expression for v in y,sigma,theta using (2),
subtract its values at u and v, and divide by u-v. Telescoping
polynomial monomials gives
\[
(Y_d,S,T_d)=L[u,v],\qquad (Y_d,S,B_d)=L[u,v].
\tag{9}
\]
The second equality uses m nonzero and (7). Thus a common geometric
zero of B_d and S cannot also annihilate Y_d. This covers distinct
pairs and diagonal tangents.

If B_d=0 and S is nonzero at a geometric pair, the unique possible
collision parameter is X=-Y_d/S, and (7) reduces the remaining
equation to f_c=0. If B_d=S=0, a collision would instead require
Y_d=0, which (9) excludes. On the diagonal these are derivative
tests; they do not say that diagonal tests alone detect all collisions.

## 3. Saturation and the unit divided-difference ideal

Suppose first that S is not the zero polynomial. In the quotient by
I, equation (9), together with B_d=0 and Y_d=-XS, makes S a unit.
The equation Sf_c=0 then gives f_c=0. Eliminating X gives
\[
L[X,u,v]/I\ \simeq
\bigl(L[u,v]/(B_d,f_c)\bigr)_S,
\qquad X\longmapsto-Y_d/S.
\tag{10}
\]
Conversely these substitutions annihilate every generator of I, and
the maps are inverse because S is already a unit on the left. The
zero ring is allowed on either side. The localization on the right
is zero exactly when some S^N belongs to (B_d,f_c), equivalently
when the saturation is the unit ideal. No algebraic closure or
Nullstellensatz is needed.

If S is identically zero, (9) gives (B_d,Y_d)=L[u,v] directly. Thus
I is the unit ideal, as the saturation convention in (6) requires.
This proves the last three equivalences without finiteness.

## 4. The finite converse and every residue fiber

Necessity is already in326. If R=T, express v as a polynomial in
X,a_X,b,c_X, subtract at u and v with X fixed, and divide by u-v.
Telescoping proves that the ideal (8) contains 1.

For sufficiency suppose b is nonconstant and I is the unit ideal.
The polynomial b(Z)-b(v) in R[Z] has a nonzero leading coefficient
in L. Dividing by that scalar makes it monic with root v. Hence
\[
T=R[v]\quad\text{is a finite R-module}.
\tag{11}
\]
The ring R is a finitely generated L-algebra, and its inclusion in T
is injective by definition. Identifying the two copies of X, and then
the other three generators of R, gives the tensor presentation
\[
\begin{aligned}
T\otimes_R T
&\simeq L[X,u,v]/
 (a_X(u)-a_X(v),\ b(u)-b(v),\ c_X(u)-c_X(v))\\
&=L[X,u,v]/((u-v)I)\simeq L[X,v]=T.
\end{aligned}
\tag{12}
\]
The last isomorphism is multiplication. Thus the finite inclusion
is a ring epimorphism in this concrete tensor sense.

To prove equality, let \(\mathfrak m\) be any maximal ideal of R and
\(\kappa=R/\mathfrak m\). Integrality and lying-over give a prime of T
over \(\mathfrak m\), so the finite-dimensional \(\kappa\)-algebra
\[
T_{\mathfrak m}^{\mathrm{fib}}=T/\mathfrak mT
\tag{13}
\]
is nonzero. Its dimension n is a positive integer, whether or not
this fiber is reduced. Base change of (12) gives
\[
T_{\mathfrak m}^{\mathrm{fib}}\otimes_\kappa
T_{\mathfrak m}^{\mathrm{fib}}
\simeq T_{\mathfrak m}^{\mathrm{fib}},\qquad n^2=n.
\tag{14}
\]
Thus n=1, and the unital map from the field \(\kappa\) to this nonzero
one-dimensional algebra is an isomorphism.

The finite R-module Q=T/R consequently has \(Q/\mathfrak m Q=0\):
this is the cokernel after tensoring the right-exact sequence
\(R\longrightarrow T\longrightarrow Q\longrightarrow0\) with
\(\kappa\). Nakayama gives \(Q_{\mathfrak m}=0\) at
every maximal ideal. A nonzero finite module has a maximal ideal
in its support, so Q=0 and R=T. This proves (6) without reduced-fiber,
algebraic-closure, or coefficient-field rationality assumptions.

## 5. Immersion does not suffice when b is nonconstant

Over C take
\[
\begin{gathered}
m=1,\quad k_1=1,\quad\mathcal F(P,V)=P,\quad\ell=0,\\
y=v,\quad\sigma=v^2,\quad\theta=0,\quad
w=-2v^3-v^2-v,\quad b=v^4+v^2.
\end{gathered}
\tag{15}
\]
Both assumptions (2) hold. For every fixed complex X the derivatives
of a_X,b,c_X do not vanish simultaneously: b'=2v(2v^2+1); at v=0,
a_X'=1; at v^2=-1/2, c_X'=2-2v is nonzero, independently of X.
The argument also works over every algebraically closed extension.

Nevertheless, at X=1 the two distinct roots of v^2+v+1 have
\[
a_1=b=c_1=-1.
\tag{16}
\]
At this pair S=u+v=-1, f_c=u+v+1=0, and B_d=0. The saturation
detects the collision; its diagonal restriction does not.

This is an abstract first-two-potentials control, not an actual chart.
It lifts to coefficient data k=t+s,n=t,ell=0 over C(t,s). The
associated formal surface is H(U,P,V)=U^2+U, whose value at y=v
is not in the coefficient field. It fails the genuine H-level
condition; no full calibrated scalar or actual sliced frame is claimed.

## 6. Failure of the converse when b is constant

Over L=C(t,s), take coefficient derivatives from
\[
k=s,\quad m=1,\quad n=-t,\quad\ell=0,
\qquad y=0,\quad\sigma=v,\quad\theta=-v^2,\quad w=v.
\tag{17}
\]
Here \(\mathcal F=-P\). The second potential is \(mw=-\mathcal F=v\),
the projected return is L[sigma]=L[v], and b=0. The formal third
potential is H(U,P,V)=U^2-U, so even its level condition holds.

The normalized rows and divided differences are
\[
a_X=Xv,\quad b=0,\quad c_X=v-Xv^2,\qquad
[a_X]=X,\quad[c_X]=1-X(u+v).
\tag{18}
\]
Their ideal is the unit ideal because 1=[c_X]+(u+v)[a_X]. Also
S=1 and f_c=-1, so the midpoint saturation is the unit ideal.
Each fixed-X map is a polynomial embedding: for X nonzero use
v=a_X/X, and at X=0 use v=c_X.

Despite this, R=L[X,Xv,v-Xv^2] is proper in T. With independent
symbols A,C its presentation is
\[
R\simeq L[X,A,C]/(XC-A+A^2).
\tag{19}
\]
The displayed polynomial vanishes under A=Xv,C=v-Xv^2. The images
of X,A are algebraically independent: a polynomial relation among
X and Xv has each distinct power of v with zero coefficient. Thus
R has transcendence degree two and the presentation kernel has
height one. As a polynomial in C over the UFD L[X,A], XC-A+A^2
is primitive because X and A^2-A are coprime. It is irreducible over
L(X,A), having degree one in C, hence irreducible in L[X,A,C]. Its
principal prime ideal is exactly that height-one kernel. Therefore
\[
R/(X)\simeq L[A,C]/(A(A-1))\simeq L[C]\times L[C],
\qquad T/(X)\simeq L[v].
\tag{20}
\]
The first ring is not a domain, while the second is. Equality R=T
would identify these quotients, so R is proper. In particular the
inclusion is not finite, by Section 4. The constant-b boundary
cannot enter (6) without a replacement finiteness hypothesis.

This example is not an actual full chart. Its literal original
Z-intercept is z_int=-t, so C(y,z_int,w)=C(t,v) does not recover s.
Its literal Y=vX+tX^2 vanishes at X=0; the full (t,s,v) Jacobian
therefore vanishes at X=0 and cannot equal a nonzero coefficient-field
constant. Neither the strong complex intercept return nor full
scalar calibration holds. The example refutes only the abstract
nonfinite converse, while retaining the specified potentials and H-level.

## 7. Application scope and verification record

In the complete actual nonzero-coupling chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the scalar labels k1,k2,p,h,nt,ns in (1) mean k_t,k_tt,m_t,m_s,n_t,n_s.
Remove X-only terms from Y,W and replace Z by
Z-2tY-kX+t^2X^2-n. These coefficient-adjoined operations produce
exactly (3); they are not asserted to be ambient-coordinate operations
over C. The projected return and both potentials are retained inputs.

When b is nonconstant, (6) is an exact test for that coefficient-adjoined
all-X return. Since the chart already supplies the return, this is
not a new exclusion or recognition theorem. It does not replace the
genuine H/Q conditions or full scalar calibration, and makes no entry
claim for an arbitrary sliced four-space.

The complete saved326 was read through EOF before writing, to identify
the duplicated necessity and polarization. Fresh unsaved algebra
reconstructed both entire generic identities in (7), before division
by u-v, and verified both controls: their potentials, collision
residues, critical derivative, the relation (19), and the unit
divided-difference identity.
The converse and finite-fiber steps are the written algebraic proof,
not conclusions from test cases. No saved checker was executed,
imported, compiled, or rerun. No earlier source or canonical record
was edited.
