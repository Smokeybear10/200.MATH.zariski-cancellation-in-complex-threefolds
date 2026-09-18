# Only the cubic and degree-six profiles survive the geometric transfer

Working necessary reduction under the complete actual264 chart with
k=s and n_ss nonzero, after417. An explicit affine transformation
over the coefficient field transports407's rank-three quadric and
genuine cubic to precisely the geometric hypotheses used in367.
Four of the six remaining profiles are therefore impossible. The
only profiles retained here are(r,m,d)=(1,2,3) and(2,4,6).

The zero centered level is treated separately. No smooth-quadric
argument is applied to a cone. The affine transformation is over L,
not an original polynomial reframe. This note does not use a new
cubic collision theorem, exclude either retained profile, or claim
an arbitrary entry or cancellation result.

## 1. Complete actual input and the rank-three profile

Retain EVERY supplied actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the current necessary frontier in
[417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\quad E=\partial_{u_0},
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\quad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Nv_0=1,\quad a_0=EX\in L^*,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=L(v_0)=\mathbb C(y,z,w),\quad
J_{t,s,v_0}(X)=-a_0^4\in L^*,\\
k=s,\qquad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The global slice, both actual returns, literal partial, full scalar,
genuine potential levels and their evaluated unit ideals remain
imposed. All coefficient partials are the exact commuting partials
on L, with joint constants C.

Use407's coefficient notation
\[
\begin{gathered}
a=n_t,\quad \nu=n_s,\quad b=n_{ts},\quad
C=\ell_s+\nu^2,\\
\lambda=[v_0^d]y/[v_0^d]\sigma,\quad
\mu=[v_0^d]\theta/[v_0^d]\sigma,\quad
u_1=y-\lambda\sigma,\quad v_1=\theta-\mu\sigma,\\
\delta=\lambda-\nu\ne0,\quad \beta=b+e\mu,\quad
j=\delta a-\ell_t-C\mu,\quad
\mathcal K=\beta^2+2e\delta^2\ne0,\\
R=2\delta u_1+\beta v_1+j,\qquad
(r,m,d)=(\deg R,\max(\deg u_1,\deg v_1),\deg\sigma).
\end{gathered}
\tag{2}
\]
The symbol v1 is a lower intrinsic function, not the intrinsic
parameter v0. By417, every remaining candidate satisfies
\[
1\le r<m<d,\qquad d+r=2m,\qquad
(r,m,d)\in\{(1,2,3),(1,3,5),(2,3,4),
                 (2,4,6),(3,4,5),(4,5,6)\}.
\tag{3}
\]
In particular delta and Kcal are already nonzero before any
division below. No assertion that beta is nonzero is needed.

The full shifted third level, in independent formal variables
(P,U1,V1), is
\[
H-h_0=P\mathcal R+U_1^2+aU_1+\frac e2V_1^2-CV_1+\nu\ell-h_0,
\qquad \mathcal R=2\delta U_1+\beta V_1+j.
\tag{4}
\]
Evaluation is(P,U1,V1)=(sigma,u1,v1). This is407(5), not just
its homogeneous part. The complete fourth level Q-q0 is a
polynomial of exact total degree three in these variables.
Indeed before shifting it has the nonzero cubic term -2e*P*V*U
in the literal365 formula; the initial affine substitution is
invertible. Its evaluated two-gradient minors with H generate O.

## 2. Exact affine normalization, inverse and degree transport

Define the coefficient elements
\[
\mathcal A=\frac{\mathcal K}{4\delta^2}\ne0,\qquad
\mathcal B_1=\frac{\beta j}{2\delta^2}
                   -\frac{a\beta}{2\delta}-C,\qquad
\mathcal C_0=\frac{j^2}{4\delta^2}-\frac{aj}{2\delta}
                   +\nu\ell-h_0.
\tag{5}
\]
Here B1 is a coefficient, not the original four-ring Bcal.
The affine transformation over L is
\[
\begin{aligned}
p&=\mathcal R,\\
x&=V_1+\frac{\mathcal B_1}{2\mathcal A},\\
q&=P+\frac{p}{4\delta^2}-\frac{\beta V_1}{2\delta^2}
                  -\frac{j}{2\delta^2}+\frac a{2\delta}.
\end{aligned}
\tag{6}
\]
Its Jacobian determinant for the ordered variables(P,U1,V1)
to(p,x,q) is 2delta, and its complete affine inverse is
\[
\begin{aligned}
V_1&=x-\frac{\mathcal B_1}{2\mathcal A},\\
U_1&=\frac{p-\beta V_1-j}{2\delta},\\
P&=q-\frac p{4\delta^2}+\frac{\beta V_1}{2\delta^2}
                   +\frac j{2\delta^2}-\frac a{2\delta}.
\end{aligned}
\tag{7}
\]
The earlier variables are recovered by U=lambda*P+U1 and
V=mu*P+V1. Every inverse coefficient belongs to L; this is not
an assertion that it is a polynomial in the original coordinates.

Substituting U1=(p-beta*V1-j)/(2delta) in(4) gives
\[
H-h_0=pq+\mathcal A V_1^2+\mathcal B_1V_1+\mathcal C_0.
\]
Completing the square therefore proves
\[
\boxed{
\frac{H-h_0}{\mathcal A}
=x^2+\gamma pq-\Delta=:H_* ,\qquad
\gamma=\mathcal A^{-1}\in L^*,\quad
\Delta=\frac{\mathcal B_1^2}{4\mathcal A^2}
                    -\frac{\mathcal C_0}{\mathcal A}.}
\tag{8}
\]
The centered level Delta may be zero; it is distinct from delta.

After evaluation, the inverse and the degree inequalities give
\[
\boxed{
O=L[p,x,q],\qquad (\deg p,\deg x,\deg q)=(r,m,d),\qquad
(2x,\gamma q,\gamma p)O=O.}
\tag{9}
\]
To justify the middle degree, deg(v1)=m: otherwise, since delta
is nonzero, p=2delta*u1+beta*v1+j and r<m would also force
deg(u1)<m. Hence x has degree m. The only degree-d term in q
is P; all added terms have degrees at most m or r. This proves
all exact degrees without a generic-leading-coefficient assumption.

Let Phi be the polynomial obtained by substituting(7) into the
complete fourth level Q-q0. It has exact total degree three and
\[
\Phi(p(v_0),x(v_0),q(v_0))=0,\qquad
\bigl((H_*)_i\Phi_j-(H_*)_j\Phi_i:i<j\bigr)O=O.
\tag{10}
\]
Formal gradients transform by the invertible constant-over-L
matrix of(6),(7); scaling H by the nonzero element Acal is
also invertible over L. This proves both unit-ideal assertions.
No coefficient partial of the change is used here. Phi is the
same genuine polynomial under substitution, not a new primitive
constructed by differentiating the transformed coefficient functions.

Equations(8)--(10) are exactly the abstract input to Sections2--6
of [367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md).
Nothing from its strict theta-dominant coefficient family is used.
The four profiles to remove are
\[
(r,m,d)=(2,3,4),\ (1,3,5),\ (3,4,5),\ (4,5,6).
\tag{11}
\]
The geometric arguments are reconstructed below to keep this reuse
boundary and the zero centered level explicit.

## 3. Zero centered level: the cone has separate algebraic obstructions

Suppose Delta=0. A common irreducible factor of p and q would
also divide x, since x^2=-gamma*p*q, contradicting(9).
Thus gcd(p,q)=1. Unique factorization in L[v0] gives
\[
p=cR_0^2,\qquad x=cR_0S_0,\qquad
q=-\frac c\gamma S_0^2,
\quad c\in L^*,\quad \gcd(R_0,S_0)=1.
\tag{12}
\]
For example take p=c*R0^2 first and define S0=x/(cR0);
the equation supplies the third identity. No coefficient square
root is adjoined. This is the exact factorization in351, Section3.
Whole return becomes L[R0^2,R0*S0,S0^2]=L[v0].

For(1,3,5) and(3,4,5), the odd degree of p is immediately
incompatible with(12).

For(2,3,4), the degrees of R0,S0 are one and two. Use R0 as
an affine parameter zeta and write
S0=a*zeta^2+b*zeta+c0, with a,c0 nonzero, the second by
coprimality. Direct multiplication gives
\[
L[R_0^2,R_0S_0,S_0^2]
=L[\zeta^2,\zeta(a\zeta^2+c_0)]
=L[\zeta^2]\oplus\zeta(a\zeta^2+c_0)L[\zeta^2].
\tag{13}
\]
Indeed the odd generator squared is even, and the formulas for
R0*S0 and S0^2 recover both inclusions. The odd module misses
zeta because the nonconstant polynomial a*zeta^2+c0 does not
divide one. This contradicts whole return.

For(4,5,6), the square-root degrees are two and three. Whole
return first implies L[R0,S0]=L[v0]. Complete the square in
R0 by an affine change of v0. Then R0 generates zeta^2 over L.
Subtracting the even part of the cubic S0 leaves
zeta(a3*zeta^2+c3), with a3 nonzero. Its generated ring again
has the odd-module form in(13), with a nonconstant odd factor,
and cannot contain zeta. This is a contradiction.

Thus all four profiles in(11) are excluded at Delta=0, without
using the geometry of a smooth quadric.

## 4. Nonzero centered level and the precise projective input

Now Delta is nonzero. Extend scalars to an algebraic closure Omega
of L. Whole return and both unit identities survive. The affine
curve is consequently an embedded smooth copy of A1, not merely
a curve with a rational function field. Its projective closure C0
lies on the smooth quadric
\[
\mathcal S:\ x^2+\gamma pq-\Delta z^2=0
\ \subset\mathbb P^3_\Omega,
\qquad [z:p:x:q].
\tag{14}
\]
Homogenizing(1,p(v0),x(v0),q(v0)) to degree d gives a
base-point-free morphism P1 to C0: the first coordinate prevents
a finite basepoint and the degree-d leader of q prevents one at
infinity. It is birational by whole return, hence the normalization.
Its pulled-back hyperplane bundle has degree d. There is precisely
one point of C0 at infinity, namely[0:0:0:1], and just one point
of the normalization over it. In the q-chart the orders are
\[
\operatorname{ord}_\infty(z/q)=d,\qquad
\operatorname{ord}_\infty(p/q)=d-r,\qquad
\operatorname{ord}_\infty(x/q)=d-m.
\tag{15}
\]
In particular deg(C0)=d. When d-m=1, C0 is smooth at infinity.
Indeed x/q has nonzero linear term in the normalization parameter.
The completed local curve ring embeds into its normalization ring
Omega[[w]], and contains all series in x/q; those series constitute
Omega[[w]]. Thus the rings are equal. The affine part was already
smooth, so in this case C0 is P1.

The cubic Phi cannot vanish identically on S: otherwise its affine
restriction is divisible by H*, and every minor in(10) vanishes.
Its homogenization therefore cuts an effective divisor Dcal of
class(3,3) on S=P1 x P1, of projective degree six. The multiplicity
of C0 in Dcal is one. Any larger multiplicity would make the
restricted cubic differential vanish on the affine curve, against
the unit minors. No residual component can meet C0 at an affine
point either: the local product of a curve equation and a vanishing
residual equation again has zero restricted differential there.

For clarity, the geometric facts used are the Segre description
with two ruling classes F1,F2, the intersections F1^2=F2^2=0 and
F1.F2=1, and the hyperplane class F1+F2. They are given in
[Vakil, Foundations, Section5.1, PDF page154](https://virtualmath1.stanford.edu/~vakil/0708-216/216fall0708.pdf).
Degree under the birational normalization and additivity/restriction
of intersections are
[Stacks, Lemmas33.45.5--33.45.8](https://stacks.math.columbia.edu/tag/0BEL).
For a smooth curve of class(a,b), adjunction gives
g=(a-1)(b-1), using K_S=(-2,-2); see
[Chao Li, Intersection Theory, Example15](https://www.math.columbia.edu/~chaoli/docs/IntersectionTheory.html).
Equivalently this genus computation follows from
0 -> O_S(-a,-b) -> O_S -> O_C -> 0 and
chi(O_S(i,j))=(i+1)(j+1).

Every residual support line through infinity is one of the two
ruling lines there. Its local equation on S is
\[
x/q-\epsilon\sqrt{\Delta}\,z/q=0,\qquad \epsilon=1,-1.
\tag{16}
\]
The p/q equation follows from the quadric equation. The order of
(16) on the normalization is d-m, since its two summands have
the unequal orders d-m and d.

This is also the local intersection length when C0 is singular
at infinity. Write A for its local ring and Abar for its finite
normalization DVR. There is one branch, with residue field Omega,
and Abar/A has finite length. Multiplication by the nonzero ruling
equation in 0 -> A -> Abar -> Abar/A -> 0 gives
length(A/fA)=length(Abar/fAbar), because the kernel and cokernel
on the finite-length quotient have equal lengths. The latter
length is exactly the order in(15). No smoothness is presumed
in this local length argument.

## 5. The four nonzero-level contradictions

For(2,3,4), d-m=1, so C0 is smooth rational of degree four.
Its positive bidegrees sum to four and satisfy(a-1)(b-1)=0.
Hence its class is(1,3) or(3,1). A zero bidegree would instead
give a single ruling fiber, impossible at degree four.
The residual divisor has class(2,0) or(0,2), so is the sum of
two fibers of the same ruling, with repetition allowed. Every
support line intersects C0 with total intersection number three.
All intersections must be at infinity, but a line there has local
intersection length one by(16); a line missing infinity has none.
Both possibilities contradict the number three.

For(1,3,5) or(3,4,5), the cubic divisor has residual degree one,
so the residual is one reduced ruling line. The class of C0 is
(2,3) or(3,2), according to its ruling, and its intersection with
that residual line is three. The only permitted location is
infinity. Formula(16) and the local length argument give lengths
two and one, respectively. Neither equals three. This treats the
possibly singular degree-five closure in the first profile without
applying a smooth-curve genus formula to it.

For(4,5,6), d-m=1 again gives a smooth rational projective closure.
It has degree six, equal to the entire cubic divisor degree.
Every effective component has positive degree, and C0 has
multiplicity one, so Dcal=C0. Its class is therefore(3,3), whose
genus is four, contradicting C0=P1.

Together with Section3 these exclude every profile in(11).

## 6. Remaining scope and evidence

Removing(11) from the six-profile list(3) gives precisely
\[
\boxed{(r,m,d)\in\{(1,2,3),(2,4,6)\}.}
\tag{17}
\]
This is a necessary frontier under the full supplied actual chart.
Neither surviving profile is excluded or realized here. In
particular the zero-level square-root degrees for(2,4,6) are
(1,3), not the obstructed(1,2) or(2,3) pairs. The formal boundary
control367(23)--(24) satisfies the abstract quadric/cubic/unit-minor
conditions at(2,4,6), including zero centered level. Additional
literal identities are therefore needed beyond this transfer.

The only geometric reuse from367 is its abstract input(9)--(11)
and Sections2--6, reproduced here. Its strict theta-dominant
coefficient identities and original map are not hypotheses of421.
No ruling, square root or affine coefficient-field variable has
been promoted to an original four-ring coordinate.

The complete367 was freshly read incab4b4; its direct355/356 inputs
were fully read in650772, and351 in3eef79. The complete407 had
been freshly read ine591f3+19e10f,264 in6d6ef8, and417 in18837f.
Primary Segre, genus and intersection statements were freshly
checked in turn4608view0 and turn4609view0--2. The writing guide
was read in22ed91 before authoring.

Fresh unsaveddd8de6 independently reconstructed(8), the exact
Jacobian determinant2delta, and both inverse orders in(6),(7).
Every residual was zero. These controls support the affine
identities, not the projective, unit-ideal or parity arguments,
which are written above.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. This source
is held for independent review. It makes no unrestricted
cancellation, arbitrary-entry, novelty, human-expert verification
or formal-proof certification claim.
