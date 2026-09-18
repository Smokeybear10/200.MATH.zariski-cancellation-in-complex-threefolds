# Polynomial speed divisors in the remaining non-null cubic case

In the supplied actual non-null cubic framework, every irreducible
divisor of the third speed Y must divide g squared minus one, where
g is the constant-axis speed. Its multiplicity in Y is strictly less
than three times its multiplicity in the second speed P. In particular
g is nonconstant, and at least one of g-1 and g+1 must be reducible.

This is a global necessary restriction, not an exclusion of the whole
non-null case. A polynomial, unimodular speed control below satisfies
it. The missing original-coordinate realization cannot be supplied
by that control alone.

## 1. Actual data and rational base derivatives

Retain the original-coordinate hypotheses90, the non-null scalar
classification121, and the
[constant reciprocal-to-cubic equivalence122](cubic-nonnull-reciprocal-equivalence-pass122.md).
After an allowed constant ambient change, the remaining data are

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad E=\partial_u,\quad
S=\ker(N|A)=\mathbb C[s,t],\quad K=\operatorname{Frac}S,\\
b=(g,P,Y)^t\in S^3,\quad \Omega=\det[b,b_s,b_t]\ne0,
\quad h=P/Y,\quad Y\ne0,\\
L/\mathbb C(h)\text{ finite},\qquad
D=a_3h^3+a_2h^2+a_1h+a_0,\quad a_i\in\mathbb C,\quad a_3\ne0,\\
g^2-DY^2=1,\quad D\ne0,\quad \det Q\ne0,\qquad
x_{\rm tr}=b(u+\rho)+b_hv+b_YR .
\end{gathered}
\tag{1}
\]

Here v,R are the actual relative generators, with v of degree one
and R of degree three, in the commuting rational h,Y frame. The
full potential and base-only unit-volume statements are retained.
The polynomial g is nonzero because its identically zero first
component would make Omega zero. The element Y is transcendental
over L: otherwise g and Y would be algebraic over L, hence in L
by relative algebraic closedness, contradicting Omega nonzero.
Thus K is finite separable over L(Y), with commuting h and Y
derivatives and full Y-constant field L. Neither is assumed to be
a polynomial base coordinate.

The pure cubic tensor is -D'''Y squared times (dh) cubed divided
by two. Consequently the same actual generating-curve argument121
gives B22=B12=0 in this frame. Primes below denote the extended
h-derivative.

## 2. The potential determines the form of rho

From g squared=1+DY squared one obtains gh=D'Y squared/(2g)
and gY=DY/g. Expanding the two relevant second derivatives of b
in (b,bh,bY) gives

\[
\begin{gathered}
G_{22}=D/g^2,\quad C^1_{22}=0,\quad C^2_{22}=-DY/g^2,\\
G_{12}=D'Y/(2g^2),\quad C^1_{12}=1/Y,\quad
C^2_{12}=-D'Y^2/(2g^2),\\
\mathsf B_{22}=\frac{D\rho-DY\rho_Y-g^2\rho_{YY}}{g^2}=0,\\
C_0:=g(\rho-Y\rho_Y)\in L,\quad
a:=g^2\rho_Y-DY\rho\in L,\quad
\rho=C_0g+aY,\\
\mathsf B_{12}=C_0'/(Yg)=0,\qquad C_0\in\mathbb C .
\end{gathered}
\tag{2}
\]

There is no unproved differential integration in (2). The Y
derivatives of C0 and a are respectively Yg times B22 and minus
g squared times B22. Hence they lie in the full constant field L,
and their displayed formulas directly reconstruct rho. Substitution
in B12 gives its last expression; the h-constant field of L is C.

## 3. Global reconstruction and contraction

The last two original rows give v=(x2-hx3)/Y and
u+rho=(x3-R)/Y. Since gY-g/Y=-1/(gY), eliminating those two
quantities from the first row yields
2R=-2gYx1+D'Y squared x2+(2g squared-hD'Y squared)x3.
Use the norm identity to clear the cubic denominator. The result is

\[
\begin{gathered}
2R=-2gYx_1+(3a_3P^2+2a_2PY+a_1Y^2)x_2\\
\hspace{20mm}+(3-g^2+a_2P^2+2a_1PY+3a_0Y^2)x_3,
\qquad R\in A,\\
F_0:=aY^2=x_3-Yu-R-C_0gY\in A\cap K=S,\\
K_0:=P^3/Y=
\frac{g^2-1-a_2P^2-a_1PY-a_0Y^2}{a_3}\in S .
\end{gathered}
\tag{3}
\]

The first row has only polynomial coefficients and actual original
coordinates, so the relative E-invariant R is global. The third
coordinate and (2) then put F0 in A intersect K. Since N kills K
and has full kernel S in A, this is exactly S, as in the null
reconstruction122. No rational inverse or constant relative Jacobian
has been substituted for the actual generation hypotheses.

Use the actual global N of
[the oriented Jacobian construction91](nonconical-global-jacobian-field-pass91.md).
The invariant plane S is factorially closed in B: it is the
intersection of the kernels of the two actual locally nilpotent
derivations E and N. The usual additive degree identity for each
locally nilpotent derivation proves that any two factors of an
invariant product are invariant. Therefore an irreducible p of S
is irreducible, hence prime, in the polynomial UFD B. Also
pB intersect S=pS, by applying the full kernels to a quotient.
This controls the reductions and cancellation in the next step.

## 4. A divisor with a unit cubic ratio is impossible

Y is nonconstant. If it were a nonzero constant, the norm identity
would make g algebraic over C(P), so the speed would have differential
rank at most one and Omega would vanish. Let p be any irreducible
divisor of Y. The equality P cubed=YK0 first gives p dividing P and
nu_p(Y) at most three times nu_p(P).

Suppose equality holds. Then K0 is a unit of S_(p), and the
finite-place lemma of
[global null reconstruction122](cubic-null-global-reconstruction-pass122.md)
applies as follows:

\[
\begin{gathered}
\nu_p(Y)=3\nu_p(P),\quad \nu_p(h)=-2\nu_p(P)<0,\quad
\frac{a}{h^3}=\frac{F_0}{K_0}\in L\cap S_{(p)},\\
\overline{a/h^3}=\lambda\in\mathbb C,\qquad
\overline{K_0}=(\overline{g}^{2}-1)/a_3\ne0,\qquad
\overline{F_0}=\lambda(\overline{g}^{2}-1)/a_3,\\
2\overline R=(3-\overline{g}^{2})\overline{x_3},\quad
\overline{x_3}-\overline R=\overline{F_0},\qquad
\frac{\overline{g}^{2}-1}{2}\overline{x_3}
   =\lambda\frac{\overline{g}^{2}-1}{a_3} .
\end{gathered}
\tag{4}
\]

The first two lines are initially residue-field identities. Since
F0 and K0 are polynomials and lambda is complex, they give a true
identity in S/(p), which embeds in B/pB. The latter is a domain
and the displayed factor g squared minus one is nonzero there.
Cancellation in its last line forces x3 congruent to 2lambda/a3
modulo pB. The original affine-linear coordinate x3-2lambda/a3
is irreducible and divisible by the nonunit p. Applying E to the
resulting association contradicts Ex3=Y nonzero and Ep=0.

Thus equality in the valuation bound is impossible. Equivalently,

\[
0<\nu_p(Y)<3\nu_p(P),\qquad
p\mid K_0,\qquad p\mid(g^2-1)
\quad\text{for every irreducible }p\mid Y .
\tag{5}
\]

The last condition says the squarefree product of the factors of
Y divides g squared minus one. It need not say that Y itself
divides that polynomial with all its multiplicities.

## 5. The axis speed must have a reducible special fiber

If g were constant and g squared minus one nonzero, (5) would force
Y to be a unit, already excluded. Constant g=1 or g=-1 would
contradict DY squared nonzero in (1). Therefore g is nonconstant.

If both g-1 and g+1 were irreducible in S, their disjoint supports
and (5) would give Y=c(g-1)^r(g+1)^s for a complex unit c and
nonnegative integers r,s. Thus Y would belong to C[g]. The cubic
identity in (3) would make P algebraic over C(g), since its leading
coefficient as a polynomial in P is a3 nonzero. In characteristic
zero the differentials of g,P,Y then have rank at most one over K,
again contradicting Omega. Consequently at least one of g-1 and
g+1 must be a reducible polynomial. Repeated nonconstant factors
count as reducibility in this statement.

In particular, the remaining case is impossible if g is an actual
polynomial coordinate of S, whose two indicated fibers are both
irreducible. No such coordinate property is assumed generally.

## 6. A control satisfying the new divisor restriction

The following speed-only control shows that (5) is not yet a
complete non-null exclusion. In S=C[s,t], set

\[
\begin{gathered}
H=st,\quad U=H^2+2,\quad
g=H^2+1,\quad P=st^2U,\quad Y=st^4U^2,\quad
h=\frac1{t^2U},\quad D(h)=h^3,\\
g^2-D(h)Y^2=1,\quad
1=g^2-sP,\quad (g,P,Y)S=S,\\
\Omega=4st^5U^2\ne0,\qquad
g^2-1=s^2t^2U .
\end{gathered}
\tag{6}
\]

The factors s,t and the two distinct factors st plus or minus
i sqrt(2) are precisely the irreducible supports of Y. Their
valuation comparisons in (5) are respectively 1<3, 4<6 and
2<3. Each divides g squared minus one. Here g-1=s squared t
squared is indeed reducible, as required by Section5.

The canonical non-null metric with D=h cubed also has nonzero
determinant -3h to the fourth power divided by four and nonzero
cubic tensor. These follow from the normal form and the norm
identity just as for the121 controls. This example therefore
survives the stated speed, metric, unit-row and divisor conditions.
No actual potential, full original polynomial frame or inverse is
assigned. It is not a cancellation counterexample.

The two non-null speed controls121, by contrast, have the factor
st-1 in Y without that factor dividing g squared minus one.
They cannot extend to the supplied actual cubic frame, by (5).

## 7. Verification scope

The finite reconstruction checker tests the connection, rho
identities, polynomial row and its residual norm certificate,
as well as the new polynomial control. The full kernel contraction,
finite-place lemma, cancellation in the actual quotient, and
coordinate-prime contradiction are written proof obligations,
not conclusions obtained by testing examples. The full non-null
cubic case and arbitrary-frame entry remain open. Files through121
are unchanged.
