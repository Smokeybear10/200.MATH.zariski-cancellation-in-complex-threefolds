# The binary parameter ideal and the order of the derived field

The binary parametrization gives more than a common zero set. Its
parameters are common invariants of the original nice action and its
derived good-partial field. Their derivatives in the good direction
vanish to a controlled power of the parameter ideal. A proper parameter
ideal must also come from two algebraically independent parameters.
These restrictions do not yet exclude that ideal or its primitive
fixed points.

## 1. Actual setting and common invariants

Use the nonlinear ternary-cone setting of the
[binary descent theorem](nice-binary-parameter-descent-pass77.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\qquad A=\ker E,\qquad
Es=1,\quad E(P_i)=0,\quad T=\partial_w,\quad [E,[T,E]]=0,\\
P_i=h_i(p,q)\ (i\le3),\quad p,q\in A,\quad
\gcd_B(p,q)=1,\quad\deg h_i=e\ge2,\\
I_A=(p,q)A,\qquad I_B=I_AB.
\end{gathered}
\tag{1}
\]
The h_i are homogeneous binary forms of one degree with gcd one.
The descent proof gives finiteness of C[p,q] over C[P1,P2,P3].
Let Q=[T,E]. Because T is constant, Qx_i=T(P_i). Differentiating
E(P_i)=0 along T gives Q(P_i)+E(Qx_i)=0. The good-direction
identity gives [E,Q]x_i=E(Qx_i)-Q(P_i)=0. In characteristic zero
both terms vanish. Therefore
\[
Q(P_i)=0\ (1\le i\le4),\qquad Qp=Qq=0,\qquad
E(Tp)=E(Tq)=E(TP_4)=0.
\tag{2}
\]
For Qp=Qq=0, extend Q to Frac B. Each parameter is algebraic
over C(P1,P2,P3), a field killed by Q. Differentiating its minimal
polynomial forces its Q-derivative to vanish, because the algebraic
extension is separable. This argument does not require the descended
parameters to be algebraically independent or assume that either is
a coordinate. The last three identities follow from [E,T]=-Q.

## 2. Conormal stationarity from the original slice

The actual slice identity is 1=sum_i P_i partial_i s. Since every
transverse P_i lies in I_B^e, the class of P4 is a unit in B/I_B^e.
Apply E to p and use Ep=0. The three transverse terms are in I_B^e,
so P4 Tp lies there. Invert its class in that quotient to obtain
Tp in I_B^e. The same argument applies to q and to the invariant
P4 itself. By (2), all three derivatives belong to A; and
I_B^e intersect A=I_A^e because B=A[s]. Hence
\[
Tp,Tq,TP_4\in I_A^e.
\tag{3}
\]
This is a statement in the original kernel, not merely after
localizing by P4. The use of the quotient unit is valid even if
I_A or I_A^e is nonreduced. Since e>=2, T preserves I_B and
kills the displayed generator classes p,q in I_B/I_B^2.
This does not say that T is zero on the entire conormal module:
on a class fp+gq it still differentiates the coefficient classes
f,g. It is not zero on B/I_B either, where it remains the
actual derivative of w.

The chain rule for homogeneous h_i now gives
\[
Qx_i=(h_i)_u(p,q)Tp+(h_i)_v(p,q)Tq\in I_A^{2e-1}
\quad(i\le3),\qquad Qw=TP_4\in I_A^e.
\tag{4}
\]
All the coordinate values of Q in (4) are E-invariant; this
is the exact good-partial consequence, not a property assumed
for an arbitrary commuting auxiliary derivation.

## 3. Orders of the wedge and the remaining primitive ambiguity

Let W_ij=P_i Qx_j-P_j Qx_i, using x4=w. Equations (1) and (4)
give the ideal containments in A
\[
W_{ij}\in I_A^{3e-1}\quad(i,j\le3),\qquad
W_{i4}\in I_A^{2e-1}\quad(i\le3).
\tag{5}
\]
The second term in W_i4 contains the unit-mod-I_B factor P4,
so it need not have the higher order 3e-1. No equality of orders
or noncancellation of leading coefficients is asserted.

Assume Q is independent of E. The
[intrinsic primitive test](primitive-good-quotient-scope-pass75.md)
identifies the ideal of these wedge entries in B with the extended
image ideal of delta=Q|A. Contracting (5) gives the first
containment below. Since delta kills p and q, differentiation
of an element of I_A^r acts only on the coefficients in an
expression in their degree-r products, giving the second.
Write delta=hD for its exact content h in A and primitive
intrinsic LND D. If D were fixed-point-free, the wedge ideal
would be hB. By (5), it is contained in I_B^(2e-1), so
\[
\begin{gathered}
\delta(A)\subseteq I_A^{2e-1},\qquad
\delta(I_A^r)\subseteq I_A^{r+2e-1}\quad(r\ge0),\\
D\text{ fixed-point-free}\quad\Longrightarrow\quad
h\in I_A^{2e-1}.
\end{gathered}
\tag{6}
\]
Here contraction from B to A is again justified by the actual
polynomial extension. The last implication is only a necessary
condition for primitive freeness when I_A is proper. The two
filtration containments concern delta and need not survive
division by h. Dividing the wedge by h
can remove all or only part of its vanishing. Neither (5) nor
(6) proves that the divided ideal is the unit ideal, and no
unproved bound on h is used to produce a counterexample.

## 4. A proper parameter ideal requires independence

Suppose instead that p,q are algebraically dependent. If one is
a nonzero constant, I_A=A immediately. Otherwise homogenize
the finite tuple (p,q,1) to their common maximum degree d in a
new variable z. Zero-pad the tuple to match the number of input
variables. It is homogeneous with component gcd one: its third
component is z^d, while at least one other component is not
divisible by z. A homogenized relation gives transcendence
degree at most two.

Apply the same full-gcd binary parametrization theorem used in
the descent note. The third component z^d is a homogeneous
binary form in equal-degree coprime parameters pi,chi. Factor
that binary form over C. Each evaluated nonzero linear factor
is homogeneous of the parameters' positive degree n and divides
z^d. Thus at least one constant linear combination of pi,chi
is c z^n for c nonzero. Make that combination the second
parameter by a constant invertible two-by-two matrix. At z=1,
the two original polynomials become
\[
p=f(a),\qquad q=g(a),\qquad
a\in B,\quad f,g\in\mathbb C[t].
\tag{7}
\]
The parameter a is nonconstant because p is nonconstant.
From Ep=f'(a)Ea=0 and characteristic zero, a belongs to A.
If f,g had a nonconstant common univariate factor, its evaluation
at a would be a nonunit common divisor of p,q in B. Their
coprimality excludes this. A univariate Bezout identity therefore
gives 1 in (p,q)A. In conclusion,
\[
I_A\ne A\quad\Longrightarrow\quad
\operatorname{trdeg}_{\mathbb C}\mathbb C(p,q)=2
=\operatorname{trdeg}_{\mathbb C}\mathbb C(P_1,P_2,P_3).
\tag{8}
\]
The last equality uses the finite extension from Section 1.
This finite-pair argument uses the selected homogeneous
parametrization directly. It does not assume that a belongs
to C[p,q], that it is a coordinate, or that the entire kernel
is a polynomial extension of C[a]. It makes no inference from
the minimum degree of a polynomial in a possibly nonnormal
subalgebra.[^finite]

## 5. Why conormal stationarity alone is insufficient

There are polynomial parameters for an actual constant partial
whose derivatives have exactly the type of high ideal order
in (3), while their common zero ideal remains proper. For example,
\[
T=\partial_w,\qquad p=x,\quad q=y+x^2w,
\qquad (p,q)=(x,y),\quad Tp=0,\quad Tq=p^2.
\tag{9}
\]
The inverse change is y=q-p^2w. This control has an actual
partial and a proper stationary ideal. It is not asserted to
extend to the required nice four-variable action or nonlinear
velocity cone. In fact p already omits a constant direction,
so it cannot be a nonconstant E-invariant in the supplied-good,
nonlinear-cone setting of the pass76 omission theorem.

The completed restrictions are the common invariants, (3)--(6),
and the independence reduction (8). They narrow the possible
codimension-two obstruction but do not resolve it. Historical
novelty, human expert review and formal proof verification are
not claimed. Frozen passes through76 are unchanged.

[^finite]: Michiel de Bondt, [*Homogeneous Keller maps*](https://webdoc.ubn.ru.nl/mono/b/bondt_m_de/homokema.pdf), Theorem4.3.1 and its complete displayed proof, printed87--89, freshly read in the retained primary text. The finite-pair specialization is proved in Section4 above. The source's separate Theorem4.3.5 is not needed for this specialization, nor is any unproved conclusion about its minimum-degree argument used.
