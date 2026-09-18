# The non-null cubic with more than one root is excluded

Under the supplied actual non-null cubic hypotheses, a cubic scalar
with two or three distinct roots is impossible. The proof is an
elementary polynomial differential and degree argument. It uses the
radical divisor restriction122, not a logarithmic surface classification.

The triple-root scalar was excluded separately123 using the stronger
pole bound. Thus the two arguments together exclude the whole non-null
cubic alternative in the supplied framework. They do not establish
entry of an arbitrary cancellation instance into that framework.

## 1. The exact polynomial hypotheses

Retain the actual non-null cubic scalar form, after the allowed
constant reciprocal equivalence122, and the necessary radical
restriction of
[the divisor theorem122](cubic-nonnull-divisor-restriction-pass122.md).
The polynomial data used below are

\[
\begin{gathered}
S=\mathbb C[s,t],\quad g,P,Y\in S,\quad Y\ne0,\quad
h=P/Y\notin\mathbb C,\quad
\Omega=\det[b,b_s,b_t]\ne0,\quad b=(g,P,Y)^t,\\
D(z)=d_3z^3+d_2z^2+d_1z+d_0,\quad d_i\in\mathbb C,\quad d_3\ne0,\\
g^2-D(P/Y)Y^2=1,\qquad
p\mid Y\ \Longrightarrow\ p\mid(g^2-1)
 \quad\text{for every irreducible }p\in S .
\end{gathered}
\tag{1}
\]

Assume that D is not a constant multiple of the cube of one linear
polynomial. We will contradict (1).

Let F3(P,Y)=d3 P cubed+d2 P squared Y+d1 PY squared+d0 Y cubed.
Clearing the norm gives Y(g squared-1)=F3(P,Y). Therefore every
irreducible factor of Y divides P, since reduction modulo that factor
leaves d3 P cubed zero. The radical restriction also gives gcd(g,Y)=1.
The speed g is nonzero, since an identically zero first component
would make Omega zero.

## 2. Divisibility of the polynomial two-form along Y

Put j=Jac_(s,t)(P,Y), so that dP wedge dY=j ds wedge dt.
Fix an irreducible p dividing Y and write P=p^a U, Y=p^b V,
where a,b are positive integers and U,V are p-units. Expansion gives

\[
\begin{gathered}
dP\wedge dY
 =p^{a+b-1}
 \bigl[aU\,dp\wedge dV+bV\,dU\wedge dp
                         +p\,dU\wedge dV\bigr],\\
\nu_p(j)\ge a+b-1\ge b=\nu_p(Y),\qquad
Y\mid j .
\end{gathered}
\tag{2}
\]

All coefficients of the bracket are polynomial. The statement is
valid even when some derivative vanishes or causes further
cancellation. Taking all irreducible factors proves the final
divisibility with full multiplicities, not only its radical.

## 3. The norm identifies the other factor of the two-form

Write H2(P,Y)=F3(P,Y)/Y as a rational homogeneous function of
degree two in two formal variables, before evaluating in S.
The norm says g squared=1+H2(P,Y). Euler's identity and
differentiation in the actual source ring give

\[
\begin{gathered}
P(H_2)_P+Y(H_2)_Y=2H_2,\qquad
2g\,dg=(H_2)_P\,dP+(H_2)_Y\,dY,\\
\Omega\,ds\wedge dt
 =g\,dP\wedge dY-P\,dg\wedge dY+Y\,dg\wedge dP
 =\frac1g\,dP\wedge dY,\\
g\Omega=j,\qquad gY\mid j,\qquad
\frac{\Omega}{Y}=\frac{j}{gY}\in S\setminus\{0\}.
\end{gathered}
\tag{3}
\]

The middle equality follows by substituting the first line: its
coefficient is g-H2/g=1/g. Thus g divides j automatically because
the speed determinant Omega is polynomial. Combining this with
(2) and gcd(g,Y)=1 proves the last line. These are rational
identities whose final divisibility is in S.

One can also check the g-divisibility directly at its prime factors.
For F=Y(g squared-1)-F3(P,Y), Euler gives
P F_P+Y F_Y=-2Y(g squared-1) on the surface. At a prime dividing
g this is a unit, since Y is a unit there. Hence F_P or F_Y
is a unit. Wedging dF=0 with dY or dP then exhibits j as
2gY times a regular local coefficient. This confirms full
multiplicity at every such prime without a smoothness assumption
on the entire cubic surface.

Let pdeg=deg(P), ydeg=deg(Y), and gdeg=deg(g), using total
polynomial degree. Since j is nonzero, P and Y are nonconstant.
The degree of a nonzero derivative drops by at least one, so (3)
forces

\[
\deg j\le p_{\deg}+y_{\deg}-2,\qquad
\deg j\ge g_{\deg}+y_{\deg},\qquad
g_{\deg}\le p_{\deg}-2 .
\tag{4}
\]

We now show that the norm instead forces gdeg at least pdeg,
after at most one allowed constant change of P.

## 4. The degree comparison when P has at least the degree of Y

The exact cubic norm makes P cubed/Y polynomial:
it equals (g squared-1-d2P squared-d1PY-d0Y squared)/d3.
If pdeg>ydeg, its degree 3pdeg-ydeg is strictly greater than
the degrees of all the other terms in that norm. Thus

\[
p_{\deg}>y_{\deg}
\quad\Longrightarrow\quad
2g_{\deg}=3p_{\deg}-y_{\deg}>2p_{\deg}.
\tag{5}
\]

Here g squared-1 is nonzero: otherwise D(h)=0 would make h
a constant root, contrary to (1). Its degree is 2gdeg, also
when g is a constant different from 1 and -1. Equation(5)
contradicts (4).

Suppose pdeg=ydeg=m. Let Pm and Ym be their nonzero leading
homogeneous forms. If F3(Pm,Ym) is nonzero, the cleared norm
has degree 3m on its right side and degree 2gdeg+m on its left,
so gdeg=m, again contradicting (4). The only other possibility is

\[
F_3(P_m,Y_m)=0
\quad\Longrightarrow\quad
D(P_m/Y_m)=0
\quad\Longrightarrow\quad
P_m=rY_m
\quad\text{for some root }r\in\mathbb C\text{ of }D .
\tag{6}
\]

The last implication uses only that C is algebraically closed:
a rational function satisfying a nonzero complex polynomial is
complex constant. Put Pnew=P-rY. Its degree is strictly less
than ydeg. Its Jacobian with Y is still j, so it is nonconstant.
The norm now uses Dnew(z)=D(z+r), which is still an exact cubic
without a triple root.

This change is an actual constant ambient transformation in the
supplied frame: x2 is replaced by x2-rx3, with the inverse addition.
It fixes g,Y and leaves Omega and j unchanged. The prime support
and gcd properties in Sections1--3 persist. It is not a matrix
over S or a rational change asserted to be a polynomial automorphism.

## 5. A lower-degree P contradicts the same differential bound

We are left with pdeg<ydeg, either originally or after the
constant shift in Section4. Reuse P,D for these data. Let k be
the smallest exponent with nonzero coefficient in D. Because D
is a cubic without a triple root, k is one of 0,1,2.

In the norm g squared-1=sum d_i P to power i times Y to
power 2-i, the nonzero terms have strictly decreasing degrees
as i increases: their degrees are i*pdeg+(2-i)*ydeg. The
i=3 term is polynomial by the norm, as observed above. Hence
the term with i=k has strictly greatest degree and cannot
cancel. It follows that

\[
2g_{\deg}=k p_{\deg}+(2-k)y_{\deg}\ge2p_{\deg},
\qquad k\in\{0,1,2\},\quad p_{\deg}<y_{\deg}.
\tag{7}
\]

This also contradicts (4). All possible degree relations have
been exhausted, proving the nontriple exclusion.

## 6. Combined scope

The argument needs only the exact cubic norm, the nonzero speed
determinant, and the radical divisor gate in (1). It does not
need the stronger inequality Y squared divides P cubed, the
vertical-divisor statement, or the remaining scalar differential
relation. No resolution of singularities, logarithmic two-form
extension theorem, polynomial abc theorem, or generic-fiber
classification was imported.

The separate
[triple-root exclusion123](cubic-nonnull-triple-root-exclusion-pass123.md)
uses the stronger pole bound to exclude exactly the scalar type
omitted in Section5. Together the two results exclude the entire
non-null cubic scalar under the retained actual assumptions.
They are not two independent counts of the same resolved case.

The supplied-frame and actual original-coordinate hypotheses were
needed upstream to prove the radical and stronger pole bounds.
Nothing here supplies such a frame for a general algebra satisfying
A[u] isomorphic to a polynomial four-ring. The unrestricted
cancellation entry problem therefore remains separate.

No new numerical method or primary source is required for this
all-polynomial proof. All files through122 remain unchanged.

