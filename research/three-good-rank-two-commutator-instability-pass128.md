# A first-commutator obstruction in an actual unit rank-two frame

## 1. Statement and scope

For a supplied three-good frame of speed rank two, the first
commutator of the action with the original bad partial need not
preserve the intrinsic speed plane. This remains false with a
unit speed row, a nonzero nonconical determinant, a quadratic
last coordinate, and nonconstant acceleration.

The example below is an actual translation with two-sided
polynomial inverse formulas. It is not a cancellation counterexample
or a hypothetical minimal-degree frame. In fact its quadratic
last coordinate can be reduced by an explicitly displayed shear.
Sections 6--7 isolate the exact structural and fixed-good-shear
boundaries, rather than infer a general recognition theorem.
No file through pass127 is changed.

## 2. The actual frame and both inverse orders

Start with \(B=\mathbb C[a,b,c,u]\), \(E=\partial_u\), and
\(A=\ker E=\mathbb C[a,b,c]\). Put \(h=c-2ab\) and define the
ordered original coordinates
\[
\begin{gathered}
Y=b+(a+1)u,\qquad Z=c+a^2u,\qquad
W=a+b^2-hu,\qquad V=u+Y^2 .
\end{gathered}
\tag{1}
\]
Their polynomial inverse is
\[
\begin{gathered}
u=V-Y^2,\qquad y_0=Y-u,\qquad
a=uZ-y_0^2+W,\\
b=Y-(a+1)u,\qquad c=Z-a^2u .
\end{gathered}
\tag{2}
\]
Here \(y_0\) is only an intermediate polynomial, not a fifth
independent coordinate. Substitution of (1) in (2) gives
\(y_0=b+au\) and
\[
u(c+a^2u)-(b+au)^2+(a+b^2-(c-2ab)u)=a,
\]
then recovers \(b,c,u\). Conversely (2) gives
\(Y=b+(a+1)u\), \(Z=c+a^2u\), and
\(W=a-uZ+y_0^2=a+b^2-(c-2ab)u\), followed by \(V=u+Y^2\).
Thus both compositions are polynomial identities.

This is the retained conic translation control75, with
\(x=u,\ y=b+au,\ z=c+a^2u,\ w=a+b^2-hu\), followed by
the two elementary changes \(Y=y+x\) and \(V=x+Y^2\).
The reconstruction above verifies the actual inverse independently;
it does not rely on a unit Jacobian as a substitute for an inverse.

## 3. The full rank-two and quadratic hypotheses

Write \(k=a(a+2)\). Direct differentiation gives
\[
\begin{gathered}
EY=a+1,\qquad EZ=a^2,\qquad EW=-h,\qquad
E^2Y=E^2Z=E^2W=0,\\
EV=1+2(a+1)Y,\qquad E^2V=2(a+1)^2\ne0,\qquad E^3V=0,\\
\mathbb C(EY,EZ,EW)=\mathbb C(a,h),\qquad
1=EZ-(a-1)EY,\\
\det[\mathbf a,\partial_a\mathbf a,\partial_h\mathbf a]
 =-a(a+2)=-k\ne0,\qquad
\mathbf a=(a+1,a^2,-h)^t .
\end{gathered}
\tag{3}
\]
The pair \(a,h\) is algebraically independent because
\((a,b,c)\leftrightarrow(a,b,h)\) is polynomial with inverse
\(c=h+2ab\). Thus the good speed rank is exactly two.
The displayed ideal identity is in the actual ring, and
already in \(\mathbb C[a,h]\).

The three speeds are independent over \(\mathbb C\):
a constant relation first has zero coefficient on \(h\),
then zero coefficients on \(a^2\) and \(a+1\).
The nonconical determinant is generically nonzero; it is not
asserted to be an everywhere invertible function.
The acceleration is nonconstant.

## 4. The selected partial, its intrinsic top, and the commutator

Let \(T=\partial_V\), with \(Y,Z,W\) fixed. Formula (2) gives
\[
\begin{gathered}
Tu=1,\qquad Ta=Z+2y_0=c+2b+ku=:L,\\
Tb=-(a+1)-uL,\qquad Tc=-a^2-2auL,\\
T=L\partial_a+(-(a+1)-uL)\partial_b
                   +(-a^2-2auL)\partial_c+\partial_u .
\end{gathered}
\tag{4}
\]
This is an actual locally nilpotent coordinate partial.
Its exact shift for the \(u\)-filtration is two: \(Tb,Tc\)
have nonzero quadratic coefficients, \(Ta\) is affine in \(u\),
and \(Tu=1\). Put \(Q=[E,T]\) and \(R=[E,Q]/2\), with the
bracket convention \([D_1,D_2]=D_1D_2-D_2D_1\). Then
\[
\begin{gathered}
N=[u^2]T|_A=-k(\partial_b+2a\partial_c)\in\operatorname{LND}(A),\qquad
R=N,\qquad [E,R]=0,\qquad [E,[E,[E,T]]]=0,\\
Q(a)=k,\quad
Q(b)=-(c+2b)-2ku,\quad
Q(c)=-2a(c+2b)-4aku,\quad Q(u)=0,\\
N_0=\partial_b+2a\partial_c,\qquad
S=\ker_A N=\ker_A N_0=\mathbb C[a,h].
\end{gathered}
\tag{5}
\]
In the actual coordinates \((a,b,h)\) of \(A\), \(N_0=\partial_b\).
This proves the kernel equality directly. Multiplication by
the nonzero invariant \(-k\) does not change it.
In this example \(R\) equals the intrinsic \(N\) extended to
kill \(u\); this equality is checked, not assumed for general
filtered derivations.

All three speeds and the acceleration in (3) belong to this
same actual plane \(S\). The selected second adjoint is
nonzero, so its adjoint degree is exactly two.

## 5. The first commutator does not preserve that plane

The decisive identities are
\[
\begin{gathered}
T(h)=k-2b(c+2b+ku),\qquad
Q(h)=-2bk,\qquad N(Q(h))=2k^2\ne0,\\
R^2(W)=2k^2\ne0,\qquad Q(S)\not\subset S .
\end{gathered}
\tag{6}
\]
They follow by differentiating \(h=c-2ab\), or from
\(W=a+b^2-hu\) and (5). Thus the first commutator improves
the degree drop enough that \(Q(h)\in A\), but not enough
to put it in \(S\).

The example also shows why the rank-one content proof127
cannot be transferred by treating this \(Q\) as an LND.
Here \(Q(a)=a(a+2)\) is a nonzero multiple of \(a\).
LND degree additivity in a domain forbids that identity
for a locally nilpotent \(Q\). Hence this first commutator
is not locally nilpotent, even though \(E,T,R\) are.
Only the highest nonzero selected commutator was guaranteed
to be locally nilpotent in the rank-two argument.

The action remains recognized: \(u=V-Y^2\) is an actual
coordinate slice with the inverse in (2), and its kernel
was explicitly \(\mathbb C[a,b,c]\) from the start.
None of (5)--(6) obstructs recognition by another argument.

## 6. An exact normalizer criterion for the missing stability

For the general supplied rank-two, selected-shift-two setup,
write \(T|_A=D_0+uD_1+u^2N\), coefficientwise on \(A\).
Each coefficient is a derivation of \(A\), and
\(Q|_A=D_1+2uN\). Let \(N_0\) be the primitive LND obtained
from \(N\) by dividing its coefficient gcd, with the same
kernel \(S\). Then
\[
Q(S)\subset A,\qquad
Q(S)\subset S
\quad\Longleftrightarrow\quad
[N_0,D_1]=gN_0\text{ for some }g\in A .
\tag{7}
\]
For \(s\in S\), \(Q(s)=D_1(s)\), and therefore stability in
\(S\) is equivalent to \([N_0,D_1]\) killing \(S\).
After inverting the nonzero elements of \(S\), the local-slice
theorem gives \(A\otimes_S\operatorname{Frac}S
=\operatorname{Frac}S[t]\). A derivation killing \(S\)
is consequently a rational multiple of \(N_0\) on
\(\operatorname{Frac}A\).

That multiple lies in \(A\). Indeed \(A\) is a UFD since
\(A[u]\) is a polynomial UFD, and primitivity of \(N_0\)
rules out a pole of the multiplier at every prime of \(A\):
such a pole would have to divide every coefficient of \(N_0\).
The converse in (7) follows by applying the bracket to \(S\).
No local nilpotence is claimed for that bracket, and there
is no conclusion \(g\in S\).

In the control, \(D_1=Q|_A\) evaluated at \(u=0\) has
\(D_1(h)=-2bk\), and
\([N_0,D_1](h)=-2k\ne0\).
The obstruction is therefore an actual transverse bracket,
not merely a failure to select a convenient generator of \(S\).
This formulation uses only the retained primitive-LND/local-slice
facts, as in [the common-kernel proof126](three-good-common-leading-kernel-boundary-pass126.md),
not a proposed new quotient-recognition theorem.

## 7. Which good-only changes and quadratic shears remain possible

There is an independent elementary restriction on the next
coordinate-change strategy. In any actual three-good frame
\(x_i=b_i+a_i u\), suppose the cone over the good speed image
is dense in \(\mathbb A^3\). Equivalently, no nonzero
homogeneous polynomial with complex coefficients vanishes
on \((a_1,a_2,a_3)\).
For a nonconstant \(F\in\mathbb C[x_1,x_2,x_3]\) of total
degree \(d\), its highest \(u\)-coefficient is exactly
\(F_d(a_1,a_2,a_3)\ne0\). Thus
\[
\deg_EF=\deg F,\qquad
\ker(E^2)\cap\mathbb C[x_1,x_2,x_3]
 =\mathbb C\oplus
   \operatorname{span}_{\mathbb C}\{x_1,x_2,x_3\}.
\tag{8}
\]
If three replacement good coordinates all belong to this old
good polynomial ring, they are affine-linear by (8).
Their algebraic independence makes their linear coefficient
matrix invertible, so they retain the same good ring and
the same speed rank. A nonlinear reduction of the good
coordinates must involve the old bad coordinate.

In fact no nonconstant invariant rational function can be
extracted from that good ring alone. Write
\(R_{\mathrm{good}}=\mathbb C[x_1,x_2,x_3]\).
Then \(A\cap R_{\mathrm{good}}=\mathbb C\) and
\(\operatorname{Frac}A\cap\operatorname{Frac}R_{\mathrm{good}}
=\mathbb C\). For the field assertion, express a nonzero
element of the intersection as \(P/Q\) with nonzero coprime
\(P,Q\in R_{\mathrm{good}}\). They remain coprime in
\(B=R_{\mathrm{good}}[z]\). The identity
\(Q\,EP-P\,EQ=0\) therefore implies \(P\mid EP\) and
\(Q\mid EQ\) in \(B\). Self-divisibility for the actual
LND \(E\) gives \(EP=EQ=0\), and (8) forces \(P,Q\) to
be constants. The zero rational function causes no exception.

When the speeds are polynomial in independent parameters
\(s,t\), the map
\((\lambda,s,t)\mapsto\lambda\mathbf a(s,t)\) has Jacobian
determinant
\(\lambda^2\det[\mathbf a,\mathbf a_s,\mathbf a_t]\).
In characteristic zero, nonzero determinant is equivalent
to dominance. This verifies the projective-density premise
from the usual nonconical condition, and in particular
from (3). No parameter is being promoted to an ambient
coordinate in this argument.

There is a sharp fixed-good-shear consequence. Under the
same density premise, suppose \(E^3z=0\) and
\(q=E^2z\ne0\). An actual triangular change \(z\mapsto z-F\),
with \(F\) in the old good polynomial ring, lowers its
\(E\)-degree to at most one exactly as follows:
\[
\begin{gathered}
\deg_E(z-F)\le1
\quad\Longleftrightarrow\quad
F=F_2+F_1+F_0,\quad q=2F_2(a_1,a_2,a_3),\\
\exists F\in\mathbb C[x_1,x_2,x_3]\ 
  \deg_E(z-F)\le1
\quad\Longleftrightarrow\quad
q\in\operatorname{span}_{\mathbb C}\{a_i a_j:1\le i\le j\le3\}.
\end{gathered}
\tag{9}
\]
On the right, \(F_j\) is homogeneous of degree \(j\) in the
old good coordinates; the final membership is the equivalent
existence criterion for such an \(F\). To verify (9),
any \(F\) of degree greater than two has higher \(E\)-degree
than \(z\) by (8), so cancellation is impossible.
For degree at most two, \(E^2F=2F_2(a)\), with affine parts
irrelevant. Every such shear has the actual inverse
\(z=(z-F)+F\), because it fixes the good coordinates.

The present control has \(q=2(EY)^2=2(a+1)^2\) and is reduced
by \(V\mapsto V-Y^2=u\). It therefore does not refute a
stability assertion with the additional hypothesis that
the chosen quadratic last coordinate cannot be reduced
by a fixed-good shear. No such minimality hypothesis has
been proved available in every frame, and a fixed-good
shear criterion is not global coordinate-frame minimality.

General found the first-commutator failure by reselecting a
partial in the retained conic75 control. Root supplied the
two elementary changes giving the stronger unit/quadratic
version, and the good-only degree and quadratic-shear
criteria, including the rational-intersection corollary.
Geometry supplied the normalizer formulation (7).
All displayed identities and both inverse orders were
independently reconstructed. This note makes no unrestricted
entry or cancellation claim and no historical novelty claim.
No numerical execution or new primary-source proof read is
claimed by this author.

## 8. Bounded comparison with published centralizer results

Root separately read the statements and complete displayed proofs
in Section 4 of Bedratyuk, Chapovskyi and Petravchuk,
[Centralizers of linear and locally nilpotent derivations](https://arxiv.org/html/2302.02441v1)
(arXiv v1, February 2023). Lemma 6 records kernel preservation
under actual commutation with an LND. Proposition 2 describes the
centralizer in the presence of a slice; Theorem 4 gives its full
fraction-field rank among ordinary derivations.

These results do not place the prescribed middle commutator in
that centralizer or make its elements locally nilpotent. Our
identity \([N_0,D_1](h)=-2k\) explicitly violates the relevant
commutation premise. This is a comparison of hypotheses, not
another classification input, an exhaustive literature review,
or a claim of historical novelty. No recursive audit of the
paper's earlier dependencies is claimed.

## 9. Finite verification and its limits

The two-method
[finite checker128](three_good_unit_rank_two_boundary_checks_pass128.py)
tests both inverse orders in the symbolic constant-shift
family, the exact partials and normalizer obstruction, four
good-only degree controls, and both orders of the removing
quadratic shear. Its separate \(a^5\) coefficient-rank test
is explicitly not an actual acceleration construction.
General and Jet performed complete source-only reviews.
Root's separate [canonical capture128](verification-pass128-working.json)
records successful execution of two new methods and five
retained127 methods, with unchanged checker hashes.
These finite controls do not replace the all-polynomial
arguments in (7)--(9), or prove recognition of a
shear-minimal frame.
