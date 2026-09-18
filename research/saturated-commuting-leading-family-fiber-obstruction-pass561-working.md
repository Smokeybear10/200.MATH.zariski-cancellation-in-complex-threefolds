# A saturated commuting leading family can lose rank on a polynomial fiber

**Status: bounded elementary obstruction in an explicit translation.**

Invariant-field saturation does not force fiberwise independence of a
commuting family of locally nilpotent derivations. This remains false
when the entire family is obtained simultaneously as the intrinsic
leading fields of all four coordinate partials in an actual sliced
complex four-ring, with every supplied coordinate of positive time
degree. The quotient fibers in the example are all polynomial planes.

The example is already a translation with an explicit invariant
coordinate. It is not a cancellation counterexample, a result about
globally minimizing frames, or a claim of historical novelty.

## 1. Two commuting primitive fields

Work over the complex numbers and put
\[
A=\mathbb C[a,b,c],\qquad
D_1=\partial_b,\qquad D_2=a\partial_c+c\partial_b.
\tag{1}
\]
Both fields are nonzero locally nilpotent derivations. For \(D_1\)
this is immediate. For \(D_2\), give \(a,c,b\) weights \(0,1,2\),
respectively. Each nonzero derivative lowers this nonnegative weight
by one. Equivalently, on generators,
\[
D_2(a)=0,\quad D_2(c)=a,\quad D_2^2(c)=0,\quad
D_2(b)=c,\quad D_2^2(b)=a,\quad D_2^3(b)=0.
\tag{2}
\]
The Leibniz rule then proves local nilpotence on every polynomial.
Since the coefficients of \(D_2\) do not depend on \(b\),
\([D_1,D_2]=0\).

Here primitive means that no nonunit divides every value of the
derivation. The field \(D_1\) has the value one. The values of \(D_2\)
include \(a,c\), which have gcd one, so \(D_2\) is primitive as well.
Primitivity is not an assertion that its values generate the unit
ideal. In fact \(D_2(A)\subset(a,c)\), so \(D_2\) has no slice.

Their common kernel and generic rank are
\[
\ker_A D_1\cap\ker_A D_2=\mathbb C[a],\qquad
\operatorname{rank}_{\operatorname{Frac}A}\{D_1,D_2\}=2.
\tag{3}
\]
Indeed \(\ker D_1=\mathbb C[a,c]\), and the restriction of \(D_2\)
there is \(a\partial_c\), whose kernel is \(\mathbb C[a]\).
The coefficient minor in the \((b,c)\) columns is \(a\ne0\).

## 2. Exact invariant-field saturation

The coefficient field in this section is specifically the fraction
field \(\mathbb C(a)\) of the common kernel, not \(\operatorname{Frac}A\).
Define the intersection inside \(\operatorname{Der}_{\mathbb C}
(\operatorname{Frac}A)\):
\[
\mathcal M=
\bigl(\mathbb C(a)D_1+\mathbb C(a)D_2\bigr)
\cap\operatorname{Der}_{\mathbb C}(A).
\tag{4}
\]
Then
\[
\boxed{\mathcal M=\mathbb C[a]D_1\oplus\mathbb C[a]D_2.}
\tag{5}
\]
To prove this, let \(L=g_1(a)D_1+g_2(a)D_2\) be regular on \(A\),
where \(g_i\in\mathbb C(a)\). Its values are
\[
L(a)=0,\qquad L(c)=a g_2(a),\qquad
L(b)=g_1(a)+c g_2(a).
\tag{6}
\]
Polynomiality of the last expression, compared coefficientwise in
the independent variable \(c\) over \(\mathbb C(a)\), forces both
\(g_1,g_2\) to belong to \(\mathbb C[a]\). More explicitly,
\(A\cap\mathbb C(a)[c]=\mathbb C[a,c]\), and its constant and
linear coefficients in \(c\) are polynomial in \(a\).
Conversely polynomial coefficients plainly give a derivation of \(A\).
The sum is direct by the independence in (3).

Every element of \(\mathcal M\) is an LND, including zero, and any
two of its elements commute. Their coefficients in \(\mathbb C[a]\)
are killed by both original fields; commuting invariant multiples
preserve commutation and local nilpotence of their sum. Alternatively,
the values in (6) give the same triangular weight argument directly.

## 3. Rank loss without a bad quotient fiber

For \(\lambda\in\mathbb C\), let
\(A_\lambda=A/(a-\lambda)=\mathbb C[b,c]\). The induced fields are
\[
\overline D_1=\partial_b,\qquad
\overline D_2=\lambda\partial_c+c\partial_b.
\tag{7}
\]
Their rank over \(\operatorname{Frac}A_\lambda\) is two if
\(\lambda\ne0\), and one if \(\lambda=0\). At zero the exact
dependence is \(\overline D_2=c\overline D_1\), while
\(\overline D_1\ne0\). Thus
\[
\{\lambda:\overline D_1,\overline D_2
\text{ are dependent over }A_\lambda\}=\{0\},\qquad
\{\lambda:A_\lambda\not\simeq\mathbb C^{[2]}\}=\varnothing.
\tag{8}
\]
These ranks concern derivations over the fiber ring or its fraction
field. They are not dimensions of the abstract module
\(\mathcal M/a\mathcal M\), which has complex dimension two.
After extending coefficients to \(\mathbb C[b,c]\), evaluation in
the fiber derivation module has the relation \((-c,1)\).

For clarity, the associated action can be written without any
classification theorem:
\[
(s,t)\cdot(a,b,c)
=\bigl(a,\ b+s+t c+t^2a/2,\ c+t a\bigr).
\tag{9}
\]
The group law follows by substitution. On \(a=0\) it is a faithful,
fixed-point-free action on the plane, but each point has the
one-dimensional stabilizer \(s+t c=0\). Hence fixed-point-free is
not free here. For \(a\ne0\), its stabilizers are trivial.

Allowing a larger coefficient field would change the problem:
\[
\frac{D_2-cD_1}{a}=\partial_c.
\tag{10}
\]
This identity does not contradict (5), because \(c\notin\mathbb C(a)\).
Indeed \(\partial_c\) does not commute with \(D_2\): their bracket,
in that order, is \(\partial_b\). The ordinary translation pair
\(\partial_b,\partial_c\) certainly exists on this already polynomial
ring, but it is not a basis change inside the specified module.

## 4. Realization by all four actual coordinate partials

Now put
\[
\mathcal B=A[u]=\mathbb C[a,b,c,u],\qquad E=\partial_u,
\qquad Eu=1,\qquad\ker E=A.
\tag{11}
\]
Introduce auxiliary polynomial coordinates
\[
A_0=a,\qquad B_0=b+c u+a u^2/2,\qquad
C_0=c+a u,\qquad U_0=u,
\tag{12}
\]
and then the actual supplied coordinates
\[
q_1=A_0+B_0,\qquad q_2=B_0,\qquad
q_3=C_0+B_0,\qquad q_4=U_0+B_0.
\tag{13}
\]
Their complete polynomial inverse is obtained in the following order:
\[
\begin{aligned}
a&=q_1-q_2,& u&=q_4-q_2,\\
c&=q_3-q_2-a u,&
b&=q_2-c u-a u^2/2.
\end{aligned}
\tag{14}
\]
The symbols \(a,u,c\) on the right of later expressions denote the
preceding polynomial expressions. Thus (14) is a polynomial map.
Substituting (13) into it gives \(a,u,c,b\). In the reverse direction,
(14) gives \(B_0=q_2\), \(C_0=q_3-q_2\), \(A_0=q_1-q_2\) and
\(U_0=q_4-q_2\), which recover all four \(q_i\) in (13).
Both inverse orders are therefore exact, not inferred from a Jacobian.

All four coordinates have the same nonzero leading coefficient:
\[
\deg_E q_i=2,\qquad [u^2]q_i=a/2\ne0\quad(1\le i\le4).
\tag{15}
\]
The coefficient may vanish on \(a=0\); E-degree in (15) is computed
in the original domain, before such specialization.

Let \(T_i=\partial_{q_i}\). Differentiation of the complete inverse
gives the entire table below, expressed in \((a,b,c,u)\):

| Partial | \(T_i(a)\) | \(T_i(b)\) | \(T_i(c)\) | \(T_i(u)\) | \(k_i\) |
| --- | --- | --- | --- | --- | --- |
| \(T_1\) | \(1\) | \(u^2/2\) | \(-u\) | \(0\) | \(2\) |
| \(T_2\) | \(-1\) | \(c-u^2/2+u+1\) | \(a+u-1\) | \(-1\) | \(2\) |
| \(T_3\) | \(0\) | \(-u\) | \(1\) | \(0\) | \(1\) |
| \(T_4\) | \(0\) | \(-c\) | \(-a\) | \(1\) | \(0\) |

These are simultaneously actual coordinate partials, so they are
commuting LNDs and satisfy \(T_i(q_j)=\delta_{ij}\). The table also
allows direct verification of every pairing and bracket.

For each row, \(k_i\) is the maximum \(u\)-degree of its nonzero
values on the generators \(a,b,c\) of \(A\). The derivation rule
bounds all images of \(A\) by that maximum, which is attained on
\(b\). Moreover \(\deg_u T_i(u)\le k_i\), with zero having degree
\(-\infty\). Applying the rule to \(\sum f_j u^j\) proves the exact
all-ring shift statement
\[
\deg_E T_i(f)\le\deg_E f+k_i\quad(T_i(f)\ne0),
\qquad (k_1,k_2,k_3,k_4)=(2,2,1,0).
\tag{16}
\]
Their intrinsic leading fields, extracted on \(A\), are consequently
\[
\begin{aligned}
N_1&=[u^2]T_1|_A=D_1/2,&
N_2&=[u^2]T_2|_A=-D_1/2,\\
N_3&=[u]T_3|_A=-D_1,&
N_4&=[u^0]T_4|_A=-D_2.
\end{aligned}
\tag{17}
\]
All four are nonzero primitive LNDs. They commute, and their entire
\(\mathbb C[a]\)-span is precisely the already saturated module (5).
Their generic rank is two, but their entire fiber family has rank
one on \(a=0\). Adding every original coordinate partial's leading
field has therefore not removed the exceptional rank loss.

No assertion about an unknown kernel has entered: this example has
\(A=\mathbb C[a,b,c]\) from the start, and
\[
a=q_1-q_2
\tag{18}
\]
is already an actual invariant coordinate. Replacing \(q_1\) by
\(q_1-q_2\) is an invertible linear coordinate change and gives
degree zero. In particular, (13) is not a globally minimal positive
frame.

## 5. Arbitrary finite exceptional sets for the intrinsic pair

For the intrinsic statement alone, replace (1) by
\[
D_1=\partial_b,\qquad
D_{2,F}=F(a)\partial_c+c\partial_b,
\qquad 0\ne F\in\mathbb C[a].
\tag{19}
\]
The same weight proof gives local nilpotence and commutation.
Primitivity follows from \(\gcd(F(a),c)=1\), including when \(F\)
is a nonzero constant. The common kernel remains \(\mathbb C[a]\).
Comparison of the constant and linear coefficients in
\((g_1D_1+g_2D_{2,F})(b)=g_1+c g_2\) again proves saturation.
The fiber coefficient minor is now \(F(\lambda)\), so the rank-loss
set is exactly the finite zero set of \(F\), while every quotient
fiber remains \(\mathbb C[b,c]\). Repeated roots cause no exception;
a nonzero constant gives an empty rank-loss set.
Thus any prescribed finite subset of \(\mathbb C\) occurs.
The actual frame calculation above is asserted only for \(F(a)=a\).

## 6. Exact literature boundary and use of this control

The older primary manuscript [*A commuting derivations theorem on
UFDs*, arXiv:0806.2038](https://arxiv.org/html/0806.2038), after
Lemma 3.7, asks whether invariant-field saturation makes the
rank-loss fibers exactly the nonpolynomial fibers. Equations
(5)--(8) give a negative answer to that literal question.
This does not contradict its Theorem 2.1 or Lemma 3.7, which do not
assert that converse. It is not a claim that the question remained
open, that this answer is new, or that a present-day literature search
establishes priority.

The successor [arXiv:1002.4181](https://arxiv.org/abs/1002.4181)
identifies itself as containing part of that older submission.
In the published *Unipotent group actions on affine varieties*,
Journal of Algebra 336 (2011), 200--208,
[Example 4, printed p. 202](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.35.pdf)
already gives exactly the plane action in (9) at \(a=0\), after
renaming \((x,y)=(c,b)\) and interchanging the two group parameters.
The published Theorem 3, printed p. 206, distinguishes generic
polynomial fibers from the additional fiberwise independence
hypothesis that yields global coordinates. The old question is not
being attributed to that published theorem.

The elementary proof here is independent of those classification
results. Their relevant primary statements were checked directly;
the published special-fiber action is explicitly acknowledged.
Earlier internal rank-collapse and coefficient-recombination controls
remain retained, including
[the filtration note](filtration-obstruction-pass.md) and
[pass25](commuting-leading-pass25.md).

The specific failed implication is now precise: simultaneous leading
origin from all actual coordinate partials, positivity, generic rank
two, primitivity, and invariant-field saturation do not force
independence on every quotient fiber. The example says nothing against
a different coordinate frame, a repair that leaves this saturated
module, or an additional condition imposed by true frame minimality.
It gives no arbitrary coordinate-entry or cancellation theorem.

Only this source was created. Fresh unsaved differentiation checked
both inverse orders, the complete partial table, all coordinate
pairings, all commutators, and the exact shifts. No saved checker was
executed, imported, or compiled, and no canonical record was edited.
