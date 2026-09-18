# Constant projection is impossible in the nonzero-R absent-variable branch

**Status: working exclusion under the supplied actual quartic chart.**

For the full initial relation \(X^2Z-Y^4\), the branch
\(y\in L,\ R=k_\rho\ne0\) cannot occur. The argument constructs
an actual commuting locally nilpotent derivation from the selected
one. Its primitive part has affine coefficients in \(X,Y\).
Both possible coefficient ideals give a polynomial three-variable
kernel, and Wang's two-coordinate theorem contradicts the original
time-leading relation in every case.

In particular the unit-ideal case is not merely recognized here.
It too is excluded by the leading coefficients. The proof displays
its actual coordinate inverse, but does not need the regular-kernel
recognition theorem.

## 1. Supplied actual data and constant projection

Retain the complete actual universal chart184 for
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4),\qquad a^2e=b^4 .
\end{gathered}
\tag{1}
\]
The displayed coordinates are actual, the slice is global, and
the initial ideal is the full weighted initial kernel, with weights
\((1,1,2,2)\). Set
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
N(a)=N(b)=N(e)=N(h)=0,\quad a\in L^*,\qquad
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2=t^4 .
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent, and
\(L/\mathbb C(t,\rho)\) is finite separable.
The selected derivation \(N\) is an actual LND of \(A\), not
just a derivation of its fraction field.

The retained projection and its first identities are
\[
\begin{gathered}
B_a=A_a[X],\qquad
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
\sigma=4t^3y+k,\qquad
z=6t^2y^2+k_t^{\rm old}y+k_\rho^{\rm old}\vartheta+n,\quad k,n\in L,\\
L[y,z,w]=L[v],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a^3\in L^* .
\end{gathered}
\tag{3}
\]
The determinant holds \(X\) fixed. The old coefficient partials
extend to \(L[v]\) fixing \(v\), and \(E=a\partial_X\) on this chart.

Assume precisely
\[
y\in L,\qquad R:=k_\rho^{\rm old}\ne0 .
\tag{4}
\]
The first potential is
\[
Rw+4ty^3+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)=\ell,\qquad \ell\in L.
\tag{5}
\]
At fixed \(y\in L\), it gives a polynomial of degree at most two
for \(w\) in \(\vartheta\). The formula for \(z\) and \(R\in L^*\)
then give
\[
z=R\vartheta+A_0,\quad A_0\in L,\qquad
w=\alpha\vartheta^2+\beta\vartheta+g,\quad \alpha,\beta,g\in L,\qquad
L[\vartheta]=L[v],\quad \gamma:=N\vartheta\in L^* .
\tag{6}
\]
The whole-line assertion follows directly from \(L[y,z,w]=L[v]\)
and \(\vartheta\in L[v]\). No separate plane-embedding assertion is used.

## 2. The quadratic coefficient has an exact complex ratio

The old derivative \(y_\rho^{\rm old}\) is nonzero. Otherwise
the first row of (3)'s determinant would be
\((X+y_t^{\rm old},0,0)\), contradicting its nonzero constant value.
Thus \(t,y\) are algebraically independent and
\(L/\mathbb C(t,y)\) is finite separable.

Use its commuting coefficient partials, now fixing \(X,\vartheta\).
The parameter-change determinant is
\(y_\rho^{\rm old}\gamma\in L^*\), so the new determinant is
still a nonzero element of \(L\), independent of \(X,\vartheta\).
These two coefficient partials have joint constant field \(\mathbb C\):
differentiate the monic minimal polynomial of a joint constant over
\(\mathbb C(t,y)\), then use minimality and algebraic closedness.

In the rest of this section all \(t,y\) subscripts are these new
partials. Write \(K_0=\sigma\in L\). The literal matrix is
\[
\begin{pmatrix}
X&1&0\\
R_t\vartheta+A_{0,t}+K_{0,t}X+4t^3X^2&
R_y\vartheta+A_{0,y}+K_{0,y}X&R\\
w_t+\rho_tX^2&w_y+\rho_yX^2&w_\vartheta+X
\end{pmatrix}.
\tag{7}
\]
Its determinant is
\[
\begin{aligned}
\mathcal J={}&(2\alpha\vartheta+\beta+X)
 \{-R_t\vartheta-A_{0,t}
       +X(R_y\vartheta+A_{0,y}-K_{0,t})
       +X^2(K_{0,y}-4t^3)\}\\
&+R(w_t-Xw_y+\rho_tX^2-\rho_yX^3)\in L^* .
\end{aligned}
\tag{8}
\]
The coefficients of \(\vartheta^2\) at \(X=0\), and of
\(X\vartheta^2\), give
\[
R\alpha_t-2\alpha R_t=0,\qquad
R\alpha_y-2\alpha R_y=0 .
\]
Since \(R\ne0\), the joint constant field implies
\[
\alpha=cR^2,\qquad c\in\mathbb C .
\tag{9}
\]
This includes \(c=0\); no division by \(\alpha\) is made.

## 3. Constructing an actual commuting LND

Extend the actual \(N\) from \(A\) to \(B=A[u]\) by \(Nu=0\).
Then \([E,N]=0\). Also \(NX\in A\), because
\(E(NX)=N(EX)=N(a)=0\).
Define on the original ring
\[
\mathscr P=aN-(NX)E .
\tag{10}
\]
It has polynomial coefficients, fixes \(X\), and on \(A\) equals
\(aN\). Since \(N(a)=0\), on \(B_a=A_a[X]\) this is the LND
which fixes \(X\) and acts as \(aN\) on coefficients.
Thus its restriction to \(B\) is locally nilpotent as well.
This is not an assertion that \(N\), extended by \(Nu=0\), fixes \(X\).

The relation \(Y=y+tX\), with \(Ny=Nt=0\), gives \(\mathscr P Y=0\).
Also \([E,\mathscr P]=0\): both \(a\) and \(NX\) are killed by \(E\).
The derivation \(\mathscr P\) kills \(L\) and each original leading
coefficient \(a,b,e,h\). Its exact chart form and iterates are
\[
\begin{gathered}
\mathscr P=a\gamma\partial_\vartheta
 \quad\text{on }L[X,\vartheta],\\
\mathscr P Z=a\gamma R\ne0,\qquad
\mathscr P W=a\gamma(2\alpha\vartheta+\beta+X),\\
\mathscr P^2Z=0,\quad \mathscr P^3W=0,\qquad
\frac{\mathscr P^2W}{(\mathscr P Z)^2}
 =\frac{2\alpha}{R^2}=2c .
\end{gathered}
\tag{11}
\]
The last identity is in the actual fraction field. It uses
iterates of an actual derivation, not a substitution of a
generic derivative for the original \(\partial_Z\).

Let \(\Delta\) be the polynomial gcd of the coefficients of
\(\mathscr P\), and write \(\mathscr P=\Delta D\).
The standard LND-degree argument is elementary here:
if \(\mathscr P\Delta=\Delta D\Delta\ne0\), the left side has
\(\mathscr P\)-degree \(\deg_{\mathscr P}\Delta-1\), while the
right side has degree at least \(\deg_{\mathscr P}\Delta\).
Thus \(\mathscr P\Delta=D\Delta=0\).
It follows that \(D\) is a nonzero irreducible LND and
\(\mathscr P^j f=\Delta^jD^j f\). In particular
\[
DX=DY=0,\quad DZ\ne0,\quad D^2Z=0,\quad D^3W=0,\qquad
\frac{D^2W}{(DZ)^2}=2c,\qquad D(a)=D(b)=D(e)=D(h)=0 .
\tag{12}
\]

Primitive division also preserves commutation with \(E\).
Indeed
\[
0=[E,\mathscr P]=(E\Delta)D+\Delta[E,D].
\]
Comparing original polynomial coefficients and using their gcd
one for \(D\), prime by prime in the UFD \(B\), proves
\(\Delta\mid E\Delta\).
An LND cannot take a nonzero element to a nonzero multiple of
itself, by the same degree argument. Consequently
\[
E\Delta=0,\qquad [E,D]=0 .
\tag{13}
\]

## 4. A two-variable theorem and time degrees remove the quadratic term

Apply Dasgupta--Gupta Lemma 2.3(i) over the UFD
\(R_0=\mathbb C[X,Y]\) to the irreducible \(R_0\)-linear LND
\(D\) of \(R_0[Z,W]\), with \(D^2Z=0\).
Its conclusion used here is
\(DZ=B_0(X,Y)\in R_0\) and \(DW\in R_0[Z]\).
The polynomial \(B_0\) is nonzero by (12).
Now differentiation in \(Z\) is legitimate within this proved
triangular presentation:
\(D^2W=B_0\,\partial_Z(DW)\).
Equation (12) therefore yields
\[
DZ=B_0(X,Y)\ne0,\qquad
DW=2cB_0(X,Y)Z+C_0(X,Y).
\tag{14}
\]
No unproved identification of coefficient-field and original
partials is used to reach this identity.

Since \(D\) commutes with \(E\) and kills \(e,h\), one has
\[
E^2 B_0=D(E^2Z)=0,\qquad E^2(DW)=D(E^2W)=0 .
\tag{15}
\]
For every nonconstant polynomial \(Q(X,Y)\), its ordinary and
\(E\)-degrees agree: its highest homogeneous part evaluates to
\(a^jQ_j(1,t)\ne0\) because \(t\) is transcendental.
Hence \(B_0\) is affine in \(X,Y\).

Suppose \(c\ne0\), and let \(j=\deg B_0\in\{0,1\}\).
The product \(B_0Z\) has time degree \(j+2\).
For the second assertion in (15) to hold, \(C_0\) must have
ordinary degree \(j+2\), with leading coefficient satisfying
\[
2c\,B_{0,j}(1,t)t^4+C_{0,j+2}(1,t)=0 .
\tag{16}
\]
The first nonzero term has degree at least four in \(t\);
the second has degree at most \(j+2\le3\). This is impossible.
Thus \(c=0\), and (15) also makes \(C_0\) affine or zero:
\[
D=B_0(X,Y)\partial_Z+C_0(X,Y)\partial_W,\qquad
\deg B_0\le1,\quad \deg C_0\le1,\quad
\gcd(B_0,C_0)=1 .
\tag{17}
\]
The convention permits \(C_0=0\); then primitivity makes
\(B_0\) a nonzero complex constant.

## 5. The polynomial kernel in both affine-coefficient cases

Put
\[
F=B_0W-C_0Z .
\tag{18}
\]
There are exactly two possibilities for the affine coefficients
in (17).

If their ideal in \(R_0\) is the unit ideal, there are complex
constants \(\lambda,\mu\) with
\(\lambda B_0+\mu C_0=1\).
Indeed a nonzero constant coefficient gives this immediately.
Otherwise both are nonconstant affine polynomials; if their
linear parts were independent, they would have a common zero.
Their linear parts are therefore proportional, and primitivity
makes their constant difference nonzero, again giving such a
constant linear combination.

In this unit-ideal case define \(T=\lambda Z+\mu W\).
There are actual two-sided inverse formulas
\[
T=\lambda Z+\mu W,\quad F=B_0W-C_0Z,\qquad
Z=B_0T-\mu F,\quad W=C_0T+\lambda F .
\tag{19}
\]
The coefficient matrix has determinant one. Thus
\(B=R_0[T,F]\), \(DT=1\), \(DF=0\), and
\(\ker_BD=R_0[F]\).
In particular \(F\) really is an ambient coordinate here,
although it has not been asserted invariant under \(E\).

If the coefficient ideal is not the unit ideal, both linear
parts must be independent. A proportional pair of nonconstant
affine polynomials is either a common-factor pair or has a
nonzero constant combination; both alternatives have already
been excluded in this case.
Therefore \(B_0,C_0\) form an affine coordinate pair of \(R_0\).
After inverting \(B_0\),
\[
B_{B_0}=R_{0,B_0}[F,Z],\qquad D=B_0\partial_Z,\qquad
\ker D|_{B_{B_0}}=R_{0,B_0}[F].
\]
Modulo \(B_0\), the map
\((R_0/(B_0))[F]\to(R_0/(B_0))[Z,W]\), \(F\mapsto-\overline C_0Z\),
is injective, since \(\overline C_0\ne0\) in that domain.
Thus contraction removes a least possible denominator power of
\(B_0\), giving \(\ker_BD=R_0[F]\) also in this case.
No ambient-coordinate assertion for \(F\) is needed here.

In both cases, therefore,
\[
C:=\ker_BD=\mathbb C[X,Y,F]
\quad\text{is an actual polynomial three-ring stable under }E.
\tag{20}
\]
Its displayed generators are algebraically independent, as is
already seen in either localized polynomial presentation.

## 6. Wang's alternatives exclude both cases

The restriction \(E_0=E|_C\) is a nonzero LND, since
\(E_0X=a\ne0\), and \(E_0^2X=E_0^2Y=0\).
Divide its coefficient gcd to obtain an irreducible LND with
the same kernel and the same two second-iterate identities.
The invariant-gcd proof is the one given before (12), applied
now to \(E_0\).

Wang's two-coordinate theorem over \(\mathbb C\) has two alternatives.
The first gives an invariant nonzero complex linear form in \(X,Y\),
contradicting the transcendence of \(t=b/a\).
The second gives an invariant \(\xi\) with
\(C=\mathbb C[X,Y,\xi]\).
Comparing inverse one-variable polynomial presentations over
\(\mathbb C[X,Y]\) gives
\[
\xi=c_0F+Q(X,Y),\qquad c_0\in\mathbb C^*,\quad
Q\in\mathbb C[X,Y],\qquad E\xi=0 .
\tag{21}
\]
We exclude this using the exact leading ratios \(q=t^4,\rho\).
Write \(B_{0,1},C_{0,1}\) for the homogeneous linear parts,
allowing either to be zero.

If \(\deg B_0=1\), then
\[
\deg_E F=3,\qquad
[u^3]F=a^3\{B_{0,1}(1,t)\rho-C_{0,1}(1,t)t^4\}.
\tag{22}
\]
This is nonzero because \(t,\rho\) are algebraically independent.
Invariance forces \(Q\) to have ordinary degree three.
Its leading cancellation would force the nonzero
\(B_{0,1}(1,t)\) to be the zero coefficient of \(\rho\), a contradiction.

If \(B_0\) is constant and \(\deg C_0=1\), then \(F\) has time
degree three with leading coefficient
\(-a^3C_{0,1}(1,t)t^4\).
A cubic \(Q\) cannot cancel it: the corresponding polynomial
in \(t\) has degree at least four, versus at most three from \(Q\).

Finally, if both coefficients are constant, \(B_0\ne0\) and
\(F\) has time degree two with leading coefficient
\(a^2(B_0\rho-C_0t^4)\).
A quadratic \(Q\) cannot cancel its nonzero \(\rho\) coefficient.
These cases include \(C_0=0\) and exhaust (17).

Thus (21) is impossible in both coefficient-ideal cases.
The assumed constant-projection branch cannot occur:
\[
\boxed{\quad y\in L,\ k_\rho\ne0
\quad\text{is impossible under (1)--(3).}\quad}
\tag{23}
\]

## Sources and scope

The actual chart, intrinsic LND, fixed leading coefficients and
calibration are retained from
[universal-chart184](weight-four-universal-chart-potentials-pass184-working.md).
The separately saved
[zero-R reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md)
addresses \(k_\rho=0\); it is not an input to the nonzero-R proof above.
Together the two branch exclusions rule out constant \(y\) in this
specific supplied quartic chart, but they do not settle its
nonconstant-projection branches.

The exact primary statements used here were freshly read in
N. Dasgupta and N. Gupta,
[Nice derivations over principal ideal domains](https://arxiv.org/pdf/1701.03635v1):
Lemma 2.3(i), printed page 3, for an irreducible LND of a
two-variable polynomial ring over a UFD containing \(\mathbb Q\);
and Theorem 4.1, printed page 9, for an irreducible LND of a
polynomial three-ring over a characteristic-zero field.
The paper attributes these results to Wang. The present proof
retains their published statements, not a new proof or a recursive
audit of their original references.

The decisive strengthening over a possible recognition route is
Section 6: even the explicit coordinate \(F\) in the unit-ideal
case cannot lead to an \(E\)-invariant of the required form.
No Bhatwadekar--Gupta--Lokhande endpoint is needed.
No corresponding assertion for an arbitrary rational \(q(t)\)
is made; the comparisons in (16) and (22) use the literal \(t^4\).

No speed was made into an original-ring unit, no generic coordinate
was silently made polynomial, and no original partial was inferred
from a formal derivative ratio. The nonzero-R nonconstant-y branch,
other initial forms, arbitrary coordinate entry, and unrestricted
cancellation remain open here. No test was executed, imported or
compiled, and no187 or earlier source was changed. No historical
novelty, human expert certification, proof-assistant verification,
public submission or external contact is asserted.

