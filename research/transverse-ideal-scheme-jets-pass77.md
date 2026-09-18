# The transverse velocity ideal as a scheme and its first jets

For an actual nice sliced action with a supplied good coordinate
partial, the common transverse velocity scheme is a cylinder in
that coordinate. Its intrinsic quotient is explicitly the same
three-variable quotient that defines the cylinder. This statement
retains nilpotents; it is not cancellation of a polynomial variable.
The good-partial field vanishes on this scheme and raises its ideal
filtration. Neither assertion implies that its primitive intrinsic
quotient has a fixed point or is fixed-point-free.

## 1. Hypotheses and the two ideals

Work in the actual polynomial coordinates
\[
B=\mathbb C[x_1,x_2,x_3,w]=B_0[w],\qquad
E=\sum_{i=1}^4 P_i\partial_i,\qquad
E(s)=1,\qquad E(P_i)=0,
\qquad T=\partial_w,
\qquad [E,[E,T]]=0.
\tag{1}
\]
Here \(E\) is a global LND, \(\partial_4=T\), and the slice
\(s\) is in the original ring. Put
\[
A=\ker E,\quad Q=[T,E],\quad
I=(P_1,P_2,P_3)B,\quad
I_0=I\cap B_0,\quad
J=(P_1,P_2,P_3)A.
\tag{2}
\]
The generators defining \(J\) belong to \(A\) by niceness.
If \(I=B\), the transverse scheme is empty. The discussion of
its quotient below concerns \(I\ne B\). No radical or reduced
quotient is substituted for any displayed ideal.

The ordinary velocity Jacobian will be denoted by \(\mathcal N\),
to distinguish it from the intrinsic ideal \(J\). The complete
[nice-slice rank proof](nice-slice-adjoint-rank-pass74.md),
Sections 1--2, gives
\[
E(\mathcal N)=-\mathcal N^2,\qquad
\mathcal N^3=0,\qquad
\text{every two-by-two minor of }\mathcal N^2\text{ is zero},
\qquad Q(P)=\mathcal N^2 e_4=0.
\tag{3}
\]
The last equality uses the actual good partial in (1), since
\((\operatorname{ad}_E^2T)(x)=2\mathcal N^2e_4\).
The minor assertion follows over \(\operatorname{Frac}B\) from
the nilpotent four-dimensional partitions with cube zero, and
then holds in the domain \(B\). The cube-zero input uses the
original slice and the complete
[highest-vertical-adjoint exclusion](vertical-top-exclusion-pass69.md).
It is not a statement for an arbitrary invariant localization.

## 2. Scheme stability and an explicit quotient identification

In \(B/I\), the slice equation gives
\[
\overline{P_4}\,\overline{T(s)}=1.
\tag{4}
\]
Thus \(\overline{P_4}\) is a unit, including if the quotient
has nilpotents. For every \(i=1,2,3,4\), the identity
\(E(P_i)=0\) gives \(P_4T(P_i)\in I\). Cancelling the
unit in (4) proves
\[
T(P_i)\in I\quad(1\le i\le4),\qquad
T(I)\subseteq I,\qquad Q(B)\subseteq I.
\tag{5}
\]

In characteristic zero a \(\partial_w\)-stable ideal in
\(B_0[w]\) extends from \(B_0\). Indeed, if
\(f=\sum_{j=0}^n f_jw^j\in I\), then
\(T^nf/n!=f_n\in I_0\). Subtract \(f_nw^n\) and repeat.
This proves the equality for every coefficient, not just for
the radical. Set \(R=B_0/I_0\). Then
\[
I=I_0B=JB,\qquad B/I=R[w],\qquad
\overline{P_4}=v\in R^*,\qquad
\overline E=v\partial_w,\qquad
\overline s=v^{-1}w+b\quad(b\in R).
\tag{6}
\]
Here \(I=JB\) follows directly from the common generators.
To justify that \(v\) is independent of \(w\), use (5) with
\(i=4\). It says \(T(\overline{P_4})=0\) in \(R[w]\),
whose coefficientwise derivative kernel is \(R\). We do not
use the false assertion that every unit of a polynomial ring
over a nonreduced ring is constant. The formula for \(\overline s\)
likewise follows by coefficientwise integration of (4).

The original slice identity is \(B=A[s]\). Consequently
\(I=J[s]\), \(I\cap A=J\), and
\(B/I=(A/J)[\overline s]\). Its induced derivation is
\(\partial_{\overline s}\), whose kernel is \(A/J\), again
coefficientwise even for a nonreduced coefficient ring. Taking
the kernel instead in (6) gives
\[
\boxed{A/J\ \simeq\ R=B_0/I_0.}
\tag{7}
\]
More explicitly, the map sends the residue of an invariant to
its \(w\)-independent image in \(R[w]\). It is onto because
the two descriptions in (6) differ by the actual affine variable
change \(\overline s=v^{-1}w+b\). Thus (7) is an explicit
identification inside the same quotient, not an invocation of
cancellation and not a polynomial-ring assertion about \(A/J\).

If additionally \(\gcd(P_1,P_2,P_3)=1\), a proper \(I_0\)
has no height-one prime containing it: such a prime in the UFD
\(B_0\) would supply a common factor in \(B\). Hence
\(\dim R\le1\). This does not assert that \(I_0\) is radical
or that \(I_0=B_0\).

## 3. The intrinsic field raises the ideal filtration

Equation (3) says that \(Q\) kills all four velocity entries.
Combining this with \(Q(B)\subseteq I\), the product rule gives
\[
Q(I^r)\subseteq I^{r+1}\quad(r\ge1).
\tag{8}
\]
For example, write an element of \(I^r\) as a sum of coefficient
polynomials times products of \(r\) of its displayed invariant
generators. Only the coefficient differentiates, and its image
is in \(I\). The same reasoning applies to every \(r\).

Goodness gives \([E,Q]=0\), so \(\delta=Q|_A\) is defined.
Contracting (5) and using the actual equality \(I\cap A=J\)
gives \(\delta(A)\subseteq J\). Since \(\delta(P_i)=0\),
the analogous product argument gives
\[
\delta(A)\subseteq J,\qquad
\delta(J^r)\subseteq J^{r+1}\quad(r\ge1).
\tag{9}
\]
The supplied-slice-fixing extension
\(Q_0=Q-Q(s)E\) has the same restriction to \(A\), also
satisfies \(Q_0(B)\subseteq I\), and kills the generators of
\(I\); therefore (8) holds with \(Q_0\) as well. These are
identities of polynomial derivations and ideals. Dividing the
intrinsic field by its common factor need not preserve either
containment. The example below makes this loss explicit.

## 4. The exact first-jet table over the nonreduced cylinder

Write a bar for reduction to \(R[w]\). Since the last column
of \(\mathcal N\) is \(Q(x)\), (5) and (3) give
\[
\overline{\mathcal N}
 =\begin{pmatrix}C&0\\ d&0\end{pmatrix},\qquad
v\partial_w\overline{\mathcal N}
 =-\overline{\mathcal N}^{\,2},\qquad
\overline{\mathcal N}^{\,3}=0.
\tag{10}
\]
Here \(C\) is a three-by-three matrix and \(d\) a one-by-three
row over \(R[w]\). In particular, the auxiliary fourth row
has not been discarded.

The product rule in (10), using the central unit \(v\), shows
\(\partial_w(\overline{\mathcal N}^{\,2})=0\).
Let \(N_0=\overline{\mathcal N}|_{w=0}\). Coefficientwise
integration then gives the complete formula
\[
\overline{\mathcal N}=N_0-wv^{-1}N_0^2,\qquad
\overline{\operatorname{Jac}Q}
 =\partial_w\overline{\mathcal N}
 =-v^{-1}N_0^2.
\tag{11}
\]
For the Jacobian identity, ordinary coordinate differentiation
commutes before reduction, and \(T\) descends to the quotient
by (5). Equation (11) states an equality of matrices over
\(R[w]\), not a choice of Jacobian coordinates on the quotient
scheme. This distinction matters if \(R\) is singular or
nonreduced.

The square of the final matrix in (11) is zero, and every
two-by-two minor is zero by (3). These scheme-level identities
are stronger than merely saying that its rank is at most one
at each closed point. They still leave its possible nonzero
first normal jet and the effect of primitive division unresolved.

## 5. An actual linear-cone boundary with a free primitive field

In actual coordinates \((a,b,c,w)\), take
\[
E=a\partial_b+(b-aw)\partial_c+\partial_w,
\qquad T=\partial_w,\qquad
Q=[T,E]=-a\partial_c.
\tag{12}
\]
There are explicit two-sided polynomial inverse coordinates
\[
U=b-aw,\qquad V=c-bw+aw^2,\qquad
(a,U,V,w)\longleftrightarrow
(a,b=U+aw,c=V+Uw,w).
\tag{13}
\]
In these coordinates \(E=\partial_w\). In the original
coordinates it is nice, and \([E,Q]=0\), so the selected
original \(T\) is good. The supplied original slice is \(w\).
The exact ideals and intrinsic derivation are
\[
I=(a,b)B,\qquad I_0=(a,b)\mathbb C[a,b,c],\qquad
A=\mathbb C[a,U,V],\qquad J=(a,U)A,\qquad
\delta=-a\partial_V.
\tag{14}
\]
Thus \(A/J=\mathbb C[V]\simeq\mathbb C[c]=B_0/I_0\),
\(v=1\), and the entire common transverse scheme is an actual
\(T\)-cylinder. The field \(Q\) vanishes there, yet its
primitive intrinsic quotient is \(-\partial_V\), with slice
\(-V\), and is everywhere free. Its common factor \(a\)
is precisely what prevents primitive division from preserving (9).

Direct differentiation also gives a nonzero square of the original
velocity Jacobian, with sole nonzero entry
\((\mathcal N^2)_{3,1}=1\), and
\((\operatorname{Jac}Q)_{3,1}=-1\), exactly as in (11).
This example is linearly triangular and has the linear velocity
relation \(P_1=0\). It is therefore outside the nonlinear
ternary-cone branch. It is a boundary control for the deductions
above, not an example of a primitive fixed point in the remaining
branch and not a new recognition theorem.

## 6. Verification and remaining scope

The argument is exact polynomial and quotient-ring algebra. The
scheme stability and quotient identification do not require an
appeal to a source excluding the apex line from the actual image.
The first-jet table uses the already proved sliced rank cap (3).
The new proof was checked against Sections 1--2 of the saved
nice-slice74 proof and the complete saved vertical69 proof; this
is a written-proof reconstruction, not a fresh complete review of
every primary theorem cited by those notes.

Root supplied the quotient-identification formulation; Geometry
supplied the ideal-filtration observation and independently
emphasized the nonreduced unit distinction. The displayed boundary
is an explicit previously excluded triangular construction. No
new numerical suite or method, full regression, novelty audit,
human expert verification, formal certificate, or general
primitive-freeness result is claimed. Frozen passes through76 and
shared metadata are unchanged.
