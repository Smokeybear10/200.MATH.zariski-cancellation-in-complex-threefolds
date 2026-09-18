# The cubic potential excludes a nondegenerate ruled velocity metric

In the supplied actual framework90, a ruled velocity whose cubic tensor
annihilates the ruling direction cannot have a generically nondegenerate
radial metric in the exact cubic relative branch. The obstruction is the
coefficient of the third power of the generic fiber coordinate in the
actual unit-volume determinant. A globally unimodular polynomial
velocity can satisfy all the preceding metric identities; an explicit
example below separates those identities from the decisive potential
and volume conditions.

The argument allows a polynomial ruling parameter \(w=H(s,t)\),
without assuming a polynomial inverse to that base map. It does not
infer the coordinate hypothesis on s from an arbitrary rational first
integral and does not establish entry for an arbitrary sliced action.

## 1. Actual hypotheses and the rational ruling parameter

Retain the complete original-coordinate, slice, potential and unit
volume hypotheses of [cubic-relation90](nonconical-cubic-relation-pass90.md).
Write the nonzero constant original acceleration as \(q_0\), to
distinguish it from the ruling vector. Suppose additionally that
\[
\begin{gathered}
S=\mathbb C[s,t],\qquad K=\mathbb C(s,t),\qquad
w=H(s,t),\quad H\in S,\quad H_t\ne0,\\
b=p(s)+wq(s),\qquad p,q\in\mathbb C(s)^3,\qquad
D_w=H_t^{-1}\partial_t,\quad
D_s=\partial_s-(H_s/H_t)\partial_t,\\
[D_s,D_w]=0,\qquad \ker(D_w|K)=\mathbb C(s),\qquad
\Omega=\det[b,D_sb,D_wb]\ne0,\\
T(D_w,-,-)=0,
\qquad \deg_YF=3 .
\end{gathered}
\tag{1}
\]
The last line concerns the actual cubic tensor and relative relation,
not a freely chosen formal polynomial. The claim is that the associated
two-by-two radial coefficient matrix G is degenerate over K.

The rational fields and coordinate volume survive this change exactly
as in [polynomial-pullback118, Section2](cubic-polynomial-pullback-exclusion-pass118.md).
Indeed the two derivations commute on the transcendence basis s,w,
and hence on its separable algebraic extension K. Their constants
claim follows from \(D_w=H_t^{-1}\partial_t\). Replacing the
original relative vector by its components in
\([b,D_sb,D_wb]\) is invertible over K and preserves the total
degree of the relative relation. The original determinant changes by
a base factor in \(K^*\). The actual generic algebra remains
\(K[v,u]\); no v-dependent element is inverted. Primes below mean
ordinary s-derivatives on \(\mathbb C(s)\).

## 2. The actual tensor forces the ruled connection

Assume for a contradiction that G is nondegenerate. Since
\(D_w^2b=0\), one has \(G_{22}=0\), so \(G_{12}\ne0\).
Initially put
\(\Omega_0=\det[p,p',q]\),
\(\Omega_1=\det[p,q',q]\), and
\(N=\det[q',p',q]\). Direct moving-frame coefficient extraction
gives
\[
\begin{gathered}
\Omega=\Omega_0+w\Omega_1,\qquad
G_{12}=N/\Omega,\qquad C^1_{12}=\Omega_1/\Omega,\\
T_{212}=-D_wG_{12}+G_{12}C^1_{12}
       =2G_{12}\Omega_1/\Omega=0,\\
\Omega_1=0,\qquad \Omega=\Omega_0\ne0,\qquad
q'=a p+\beta q,\quad a=G_{12}\in\mathbb C(s)^*,
\quad \beta\in\mathbb C(s).
\end{gathered}
\tag{2}
\]
Here all second-derivative coefficients with both indices 2 vanish.
In particular the first formula for \(T_{212}\) is the actual
definition90, including its sign. The nonzero determinant now makes
p,p',q a basis. Write \(p''=f p+c p'+h q\) over \(\mathbb C(s)\).
The remaining tensor condition \(T_{211}=0\) gives
\(-a'+a\beta+ac=0\). Expanding the two derivatives of b therefore
yields the exact arrays
\[
\begin{gathered}
c=a'/a-\beta,\qquad p''=f p+c p'+h q,\\
G=\begin{pmatrix}f+2a\beta w-a^2w^2&a\\a&0\end{pmatrix},
\qquad C^1_{11}=c+aw,\quad C^1_{12}=C^1_{22}=0,\\
C^2_{12}=\beta-aw,\quad C^2_{22}=0,\\
C^2_{11}=h+(\beta'+2\beta^2-f-a'\beta/a)w
                  -3a\beta w^2+a^2w^3,\\
T_{111}=\tau=-f'+2fc+2ah\in\mathbb C(s),\qquad
T_{112}=T_{122}=T_{222}=0,\quad \tau\ne0.
\end{gathered}
\tag{3}
\]
For example, before imposing c, the radial entry is
\(G_{11}=f+(a'+a\beta-ac)w-a^2w^2\).
Substitution in \(T_{211}\) gives the displayed value. Substitution
of the resulting full arrays in \(T_{111}\) cancels every positive
power of w. The nonzero assertion follows from the exact cubic
relation: the degree-at-most-three potential relation is a scalar
multiple of that irreducible cubic, so its cubic part cannot vanish.

## 3. The cubic potential and closed linear coefficient

Let \(\mathsf B_{ij}\) denote the symmetric quadratic array90,
and let \(L_i=\chi_i+q_0\rho\rho_i\), where derivatives now
mean \(D_s,D_w\). The potential has only one cubic monomial,
\(q_0\tau Y_1^3/6\).

The curve lemma90 gives maximum generic degree three. The first
relative generator cannot have degree three, because its ninth-degree
contribution to the potential could not cancel. If it had degree two,
the other would have degree three, the impossible generating pair
(2,3). A constant first generator cannot generate the line together
with a degree-three second generator. Thus it has degree one. Take
this actual generic coordinate to be \(v=y_1\), and write
\(y_2=R(s,w,v)\), with coefficients in K. This only scales the
volume unit by an element of \(K^*\).

The sixth and fourth powers of v in the potential first force
\(\mathsf B_{22}=\mathsf B_{12}=0\). Its remaining relation gives
\[
\begin{gathered}
R=r_0+r_1v+r_2v^2+r_3v^3
 =\frac{\zeta-L_1v-(q_0/2)\mathsf B_{11}v^2
                     -(q_0/6)\tau v^3}{L_2},\\
L_2\ne0,\qquad r_3=-q_0\tau/(6L_2)\ne0,\qquad
r_1=-L_1/L_2,\\
L_i=D_i(\chi+q_0\rho^2/2),\qquad D_wL_1=D_sL_2 .
\end{gathered}
\tag{4}
\]
If L2 were zero, the remaining nonzero cubic would be a relation on
the transcendental element v alone. The last equality is exactness
of the linear part of the actual potential, not an additional
condition on arbitrary coefficient data.

## 4. A nonzero cubic coefficient cannot disappear

In the two-by-two block of the original determinant90, (3) gives
\(K_{12}=0\),
\(K_{11}=\rho+(c+aw)v\),
\(K_{21}=D_sR+C^2_{11}v+(\beta-aw)R\), and
\(K_{22}=\rho+D_wR+(\beta-aw)v\).
The evaluated potential gradient is \(L_2(-R_v,1)\).
Consequently the actual volume imposes
\[
\frac{\mathcal J}{\Omega L_2}
=D_sR+R_vD_wR+(\beta-aw)R+C^2_{11}v
                 +(\beta-c-2aw)vR_v\ \in K^* .
\tag{5}
\]
There is no u-term, and rho cancels from the difference of the diagonal
entries. Comparing its fifth, fourth and third powers of v gives
\[
\begin{gathered}
3r_3D_wr_3=0,\qquad 3r_3D_wr_2=0,\\
0=D_sr_3+3r_3D_wr_1+(4\beta-3c-7aw)r_3,\\
L_2,r_3\in\mathbb C(s),\qquad
D_wr_1=-L_2'/L_2\in\mathbb C(s),\\
0=r_3'+3r_3D_wr_1+(7\beta-3a'/a)r_3-7ar_3w .
\end{gathered}
\tag{6}
\]
For the penultimate line, \(D_wr_3=0\), \(\tau\in\mathbb C(s)^*\)
and (4) first give \(L_2\in\mathbb C(s)\); exactness in (4)
then gives the derivative of r1. Every coefficient in the last line
belongs to \(\mathbb C(s)\), and w is transcendental over that
field. Its w-coefficient is \(-7ar_3\ne0\), a contradiction.
This proves the claimed degeneracy of G. Equivalently the associated
ambient matrix Q cannot have rank three, since it is congruent to
\(\operatorname{diag}(-1,G)\) in the actual moving frame.

## 5. Metric and unit-speed conditions alone do not prove it

Here is an exact polynomial coefficient control over \(\mathbb C[s,t]\).
It is not supplied with four original polynomial coordinates or an
original sliced derivation. Set
\[
\begin{gathered}
a=s^2-1,\qquad p=(0,s,s^2+1)^t,\qquad
q=(1,s^4/4-s^2/2,s^5/5-s)^t,\qquad b=p+tq,\\
q'=ap,\qquad \Omega=\det[b,b_s,b_t]=a,\qquad
p''=(-2/a)p+(2s/a)p',\\
b_3-sb_2-(q_3-sq_2)b_1=1 .
\end{gathered}
\tag{7}
\]
The ruling direction varies: q1 is one and q' is nonzero, so q' is
not proportional to q. Direct moving-frame calculation gives
\[
\begin{gathered}
G=\begin{pmatrix}-2/a-a^2t^2&a\\a&0\end{pmatrix},\qquad
\det G=-a^2\ne0,\\
T_{111}=-12s/a^2\ne0,\qquad
T_{112}=T_{122}=T_{222}=0,\\
\mathcal C=[b,b_s,b_t],\qquad
Q=\mathcal C^{-t}\operatorname{diag}(-1,G)\mathcal C^{-1},
\qquad Q_t=0,\quad \det Q=1,\quad b^tQb=-1 .
\end{gathered}
\tag{8}
\]
The last line follows either by direct multiplication or by the exact
metric derivative identity118 and the tensor values just computed.
Thus globally unimodular speed, nondegenerate metric and nonzero
rank-one cubic tensor coexist. They cannot be completed to the actual
cubic potential and unit-volume data of (1), by (6). This identifies
the additional geometric hypothesis used by the exclusion rather
than treating a coefficient tuple as an original-frame example.

## Verification scope

[The two-method checker119](cubic_ruled_checks_pass119.py) checks the
conditional ruled connection, tensor and volume-coefficient identities
symbolically, and independently computes the explicit polynomial
control from its vector b. Those checks do not establish the generic
field transfer, the all-coordinate potential premise, the plane-curve
generation lemma90, or recognition of any unknown original frame.
No smoothness, nondegeneracy or cubic-volume premise is inferred from
the mere existence of a unit speed row.

The author ran both methods once in execution `ca4ba6`: both passed
in 0.479 seconds of unittest time, 0.728378584 seconds of command wall
time, exit zero. Complete saved proof and code reads were `72889d`
and `1e6bd6`; `801ef5` checked both hashes, eight sequential equation
tags, two AST methods and clean trailing whitespace. This final
paragraph records that evidence without adding numerical coverage.
