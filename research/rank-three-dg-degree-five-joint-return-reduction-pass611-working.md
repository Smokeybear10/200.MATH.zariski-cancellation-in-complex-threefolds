# Degree-five DG coefficients constrained by two whole return families

Date: 2026-09-17

Status: bounded working proof, pending independent saved-source review.
This note proves a necessary reduction for one fixed base and ordinary
degree five. It does not determine the residual invariant family, prove
a general degree bound, or make a cancellation or novelty claim.

## 1. Statement and whole base

Let R=C[x,y,z] and define

\[
f=xz-y^2,\qquad r=x^3+yf,\qquad
g=zf^2+2x^2yf+x^5,\qquad H=\operatorname{Jac}(f,g,\cdot).
\tag{1}
\]

For an arbitrary complex-coefficient homogeneous polynomial psi in R_5,
including psi=0, put

\[
E=H+(1+\psi)\partial_t\quad\text{on }R[t].
\tag{2}
\]

**Necessary reduction.** If E has a polynomial slice, then

\[
\psi\in\mathbb Cg+H(R_1).
\tag{3}
\]

Consequently there are lambda_0 in C and a homogeneous linear polynomial
L_1 in R such that the actual polynomial coordinate change
t_new=t-L_1 gives

\[
E=H+(1+\lambda_0g)\partial_{t_{\rm new}}.
\tag{4}
\]

No assertion about sliceness of (4) is needed or made here. The proof
does not assume rational coefficients for psi. It uses all four
primitive fifth roots in its second return family.

The entire Jacobian identities are

\[
Hf=Hg=0,\quad Hr=-fg,\quad Hx=-2fr,\quad
Hy=6x^2r-g,
\]
\[
Hz=2x(5x^3y+x^2z^2+3xy^2z-4y^4).
\tag{5}
\]

Inverting f and g gives the exact equality

\[
R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r],\qquad
x=\frac{f^3+r^2}{g},\quad y=\frac{r-x^3}{f},\quad
z=\frac{g-2x^2r+x^5}{f^2},\quad H=-fg\partial_r.
\tag{6}
\]

Thus H is locally nilpotent, with ordinary derivation degree four and
H-degrees (2,6,10) on (x,y,z). The triangular extension E is locally
nilpotent as well. All flows below are its finite polynomial flows,
evaluated over a Laurent-series field when required.

The first return is the complete family already proved in
[609](rank-three-dg-orbit-return-obstruction-boundary-pass609-working.md).
Its formulas and the finite computations needed here are printed below.
The second family is derived directly from (6); no other return source
or residual-family result is a dependency.

## 2. First return: all degree-five equations

For A=u^2-1 set

\[
X=\lambda^2A,\qquad
Y=-\lambda u+\lambda^4A^3,\qquad
Z=1-2\lambda^3uA^2+\lambda^6A^5.
\tag{7}
\]

The full base orbit with endpoints (0,v,w) and (0,-v,w) is
w(X,Y,Z), where lambda=v/w and u runs from -1 to 1. Its time is
2/(wv^3). Define the polynomial antiderivative evaluation

\[
P_\psi(\lambda)=\int_{-1}^{1}\psi(X,Y,Z)\,du.
\tag{8}
\]

The complete t-displacement is
[2+w^5 P_psi(v/w)]/(wv^3). If P_psi has degree K>5, substitute
w=s^K, v=s^(K-5)V(s). The equation for zero t-displacement has
constant part 2+p_K V^K, with a nonzero simple root. Formal coefficient
recursion gives a unit V(s) in C[[s]]. Both endpoints are integral,
whereas the time has pole order 4K-15. Evaluating a hypothetical whole
slice at the endpoints is impossible. Therefore

\[
E\text{ sliced}\quad\Longrightarrow\quad \deg P_\psi\le5,
\tag{9}
\]

where P_psi=0 is allowed. This implication uses the entire return, not
just its highest orbit-degree term.

Write psi=sum c_i M_i in the following fixed order:

\[
\begin{array}{c|rrrrrrr}
i&0&1&2&3&4&5&6\\
M_i&z^5&yz^4&y^2z^3&y^3z^2&y^4z&y^5&xz^4\\[2pt]
i&7&8&9&10&11&12&13\\
M_i&xyz^3&xy^2z^2&xy^3z&xy^4&x^2z^3&x^2yz^2&x^2y^2z\\[2pt]
i&14&15&16&17&18&19&20\\
M_i&x^2y^3&x^3z^2&x^3yz&x^3y^2&x^4z&x^4y&x^5.
\end{array}
\tag{10}
\]

Here and in the next table all unspecified entries are zero. The
coefficient of lambda^k in (8), multiplied by a nonzero rational number
to give a primitive integer row, is the indicated linear form:

| k | Primitive coefficient equation |
|---|---|
| 6 | 640c0+88c3-176c7+99c10-132c13+792c15=0 |
| 8 | 48c2-195c5+1920c6+234c9-624c12-143c17+1144c18=0 |
| 10 | 256c1+51c4-68c8-408c11-51c14+170c16-221c20=0 |
| 12 | 1280c0-48c3-504c7-114c10+209c13+532c15-323c19=0 |
| 14 | 624c2+230c5+1728c6-253c9-736c12+483c17+483c18=0 |
| 16 | 16c1-2c4-7c8-12c11+5c14+5c16=0 |
| 18 | 5280c0-1147c3-2046c7+899c10+899c13+899c15=0 |
| 20 | 71c2-33c5+104c6-33c9-33c12=0 |
| 22 | 112c1-37c4-37c8-37c11=0 |
| 24 | 160c0-41c3-41c7=0 |
| 26 | c2+c6=0 |
| 28 | c1=0 |
| 30 | c0=0 |

There are no other powers greater than five with nonzero coefficient.
Each table entry is reproducible by expanding the finite polynomials
(7) and applying the exact rule

\[
\int_{-1}^{1}\sum_{i,j}b_{ij}\lambda^iu^j\,du
=\sum_{i,\ j\text{ even}}\frac{2b_{ij}}{j+1}\lambda^i.
\tag{11}
\]

For a rank certificate, the displayed 13 by 21 integer matrix has the
following nonzero minor, with columns in their displayed order:

\[
\begin{aligned}
\mathcal J&=(0,1,2,3,4,5,6,7,8,9,10,11,13),\\
\det M_{\mathcal J}&=12714700334390833038975\ne0.
\end{aligned}
\tag{12}
\]

Its kernel therefore has dimension eight. An explicit basis, normalized
at the free coefficients c12,c14,c15,c16,c17,c18,c19,c20, is

\[
\begin{aligned}
V_0={}&x^2yz^2-\frac{1168}{1541}xy^3z
 +\frac{693}{1541}xz^4+\frac{320}{1541}y^5
 -\frac{693}{1541}y^2z^3,\\
V_1={}&x^2y^3-\frac{10}{13}x^2z^3
 +\frac{33}{13}xy^2z^2-\frac{23}{13}y^4z,\\
V_2={}&x^3z^2+\frac{92}{59}x^2y^2z-\frac{32}{59}xy^4
 +\frac{119}{59}xyz^3-\frac{119}{59}y^3z^2,\\
V_3={}&x^3yz+\frac{3}{13}x^2z^3
 +\frac{7}{13}xy^2z^2-\frac{10}{13}y^4z,\\
V_4={}&x^3y^2+\frac{3347}{4623}xy^3z
 -\frac{154}{1541}xz^4-\frac{3809}{4623}y^5
 +\frac{154}{1541}y^2z^3,\\
V_5={}&x^4z-\frac{2395}{4623}xy^3z
 -\frac{847}{1541}xz^4-\frac{146}{4623}y^5
 +\frac{847}{1541}y^2z^3,\\
V_6={}&x^4y+\frac{17}{59}x^2y^2z-\frac{204}{295}xy^4
 -\frac{119}{295}xyz^3+\frac{119}{295}y^3z^2,\\
V_7={}&x^5-x^2z^3+2xy^2z^2-y^4z.
\end{aligned}
\tag{13}
\]

Direct substitution in the table gives zero for every V_i. Their eight
specified free coefficients form the identity matrix, so (12) proves
that no first-return solutions are omitted. Hence every sliced
coefficient has the unique representation psi=sum q_i V_i with q_i in C.

## 3. The second whole orbit and its necessary regularity

Use a new scale b and start at (b,0,lambda b). Put L=lambda^3 and

\[
\mathcal A=\frac{L+u^2}{1+L},\qquad
\mathcal B=\frac{u-\mathcal A^3}{\lambda},\qquad
\mathcal C=\frac{1+L-2u\mathcal A^2+\mathcal A^5}{\lambda^2}.
\tag{14}
\]

Here (x,y,z)=b(mathcal A,mathcal B,mathcal C), with invariants
f=lambda b^2, g=(1+lambda^3)b^5 and r=b^3u. Formula (6) proves
these whole identities. The actual time differential is

\[
d\tau=-\frac{du}{\lambda(1+\lambda^3)b^4}.
\tag{15}
\]

Let omega be any of the four primitive fifth roots. There is a unique
formal W(L) with W(0)=omega satisfying

\[
W^6-(1+L)W+L=0,
\tag{16}
\]

because its W-derivative at (0,omega) is five. At u=W^3 the second
base endpoint is (bW,0,lambda b/W). Define

\[
I_{\psi,\omega}(\lambda)
=\int_1^{W(\lambda^3)^3}
 \psi(\mathcal A,\mathcal B,\mathcal C)\,du.
\tag{17}
\]

The integral is again a polynomial-antiderivative evaluation in u,
followed by substitution of the formal endpoint. It lies in C((lambda)).
The exact t-displacement is

\[
-\frac{W^3-1+b^5 I_{\psi,\omega}(\lambda)}
 {\lambda(1+\lambda^3)b^4}.
\tag{18}
\]

If I has a pole of order K>=1 and leading coefficient c nonzero, set
lambda=s^5 and b=s^K V(s). Its zero-return equation has constant
part omega^3-1+cV^5. Since omega^3 differs from one, this has a nonzero
simple root. A unit formal V(s) makes the entire numerator in (18)
zero. Both endpoints are integral formal arcs, while the actual time
has pole order 5+4K. The polynomial-slice endpoint identity again
gives a contradiction. Therefore sliceness implies, separately for
every one of the four roots,

\[
I_{\psi,\omega}\in\mathbb C[[\lambda]].
\tag{19}
\]

This proof includes all negative Laurent coefficients. Neither a
truncated endpoint nor a leading-only t cancellation suffices for it;
the formal simple-root construction solves (18) exactly.

## 4. Reproducible finite negative-power certificate

For a monomial x^a y^b z^c in R_5, put rho=b+2c and D=a+3b+5c.
The entire numerator in its integrand is

\[
\begin{aligned}
N_{abc}(L,u)={}&(u^2+L)^a
 \bigl[u(1+L)^3-(u^2+L)^3\bigr]^b\\
&\cdot\bigl[(1+L)^6-2u(u^2+L)^2(1+L)^3
 +(u^2+L)^5\bigr]^c.
\end{aligned}
\tag{20}
\]

Expand this finite polynomial as sum n_ij L^i u^j. Then its exact
return contribution is

\[
\lambda^{-\rho}(1+L)^{-D}
 \sum_{i,j}\frac{n_{ij}L^i}{j+1}
 \bigl(W(L)^{3(j+1)}-1\bigr),\qquad L=\lambda^3.
\tag{21}
\]

This is a finite formula for every matrix entry used below. Since
rho<=10, a negative lambda power can only come from L^k with k<=3.
It is therefore enough, and exact for the entire negative part, to use

\[
\begin{aligned}
W(L)={}&\omega+\frac{\omega-1}{5}L
 +\frac{8+\omega+3\omega^2+3\omega^3}{25}L^2\\
&-\frac{58+27\omega+33\omega^2+47\omega^3}{125}L^3
 +O(L^4),\\
(1+L)^{-D}={}&\sum_{k=0}^{3}(-1)^k
 \binom{D+k-1}{k}L^k+O(L^4).
\end{aligned}
\tag{22}
\]

All reductions of omega powers are modulo
Phi_5(omega)=omega^4+omega^3+omega^2+omega+1. Substituting (22)
in (16) gives zero through L^3; omitted terms in (22) cannot affect
any negative lambda coefficient in (21).

For psi=sum q_i V_i, four rows of the negative part suffice. For each
listed lambda power, reduce its coefficient to a polynomial in omega
of degree at most three and take the coefficient of omega^0.
After nonzero rational normalization, the resulting rows are:

| lambda power | Necessary coefficient equation |
|---|---|
| -5 | 9q0-2q4-11q5=0 |
| -4 | 5q2-q6=0 |
| -3 | q1+q3=0 |
| -2 | 17905q0-1753q4-19658q5=0 |

Equations (13) and (20)--(22) specify every entry independently of any
software or saved checker. These rows are extracted from the whole
integrand, not a leading monomial of psi.

It is essential here that (19) holds for **all four roots**. The q_i
are arbitrary complex numbers. One cannot infer four rational-basis
coefficient equations merely from vanishing at one fixed complex
omega. Instead the reduced polynomial of degree at most three must
vanish at four distinct complex roots. It is therefore the zero
polynomial over C, which licenses each displayed omega^0 equation.

The first and fourth rows both annihilate (q0,q4,q5)=(1,-1,1).
Their minor in columns q0,q4 is

\[
\det\begin{pmatrix}9&-2\\17905&-1753\end{pmatrix}
=20033\ne0.
\tag{23}
\]

Together with the other two rows, this proves

\[
q_5=q_0,\qquad q_4=-q_0,\qquad
q_1=-q_3,\qquad 5q_2=q_6.
\tag{24}
\]

No division by an unknown coefficient, root-dependent coefficient,
or leading coefficient of psi has been made. In particular all zero
coefficient cases are retained.

## 5. Exact space, H-degree, and actual shear

The following identities hold as entire polynomials in R:

\[
\begin{aligned}
V_0-V_4+V_5&=fr,\\
V_3-V_1&=g-x^2r,\\
V_6+V_2/5&=Hz/10,\\
V_7&=2x^2r-g.
\end{aligned}
\tag{25}
\]

Thus (24) gives exactly

\[
\operatorname{span}_{\mathbb C}\{g,fr,x^2r,Hz\}
=\mathbb Cg+H(R_1),
\tag{26}
\]

where the equality uses Hx=-2fr and Hy=6x^2r-g. These four
polynomials are independent, for example by their distinct H-degrees
0,1,5,9. This also proves the full H-degree-at-most-nine consequence,
not just a bound on either integrated return.

For completeness, every member of (26) really satisfies both linear
return conditions, although those conditions alone are not asserted
to imply sliceness. On the first orbit, g=lambda^4 is invariant, and
the integral of H(L_1) is lambda^3 times the difference of the endpoint
values of L_1, since du/dtau=lambda^3 at scale one. That difference is
a constant multiple of lambda, so the return degree is at most four.
On the second orbit, the g contribution to (17) is
(1+lambda^3)(W^3-1), which is regular. For H(L_1), the endpoint
difference is a linear combination of W-1 and lambda(W^(-1)-1).
Multiplication by du/dtau=-lambda(1+lambda^3) gives its integral,
which is also regular. Thus (26) is exactly the joint kernel of both
linear return tests, not merely an upper bound obtained from four
selected rows. The necessary implication (3) does not require the
converse assertion that passing the tests produces a slice.

Writing psi=lambda_0 g+H(L_1), the map

\[
(x,y,z,t)\longmapsto(x,y,z,t-L_1(x,y,z))
\tag{27}
\]

has polynomial inverse obtained by adding L_1, and determinant one.
It preserves the base derivation H and gives (4) by direct
differentiation. This is an actual whole coordinate change, not an
intrinsic parameter substitution. Sliceness is preserved under it.

## 6. Verification and scope

Two fresh unsaved exact pipelines were used. One expands the whole
integrand modulo L^4 before integration. The other forms the entire
polynomial numerator (20), integrates in u, evaluates at W^3, and
only then takes the necessary L-jets. Both recover the four rows and
the first-return kernel printed above. The complete generic orbit
(7) separately computes H-degrees, using the finite injective
invariant-field extension f=-v^2,g=wv^4 as in 609.

This source proves only the necessary form (3) for the fixed base
(1) and ordinary degree five. It does not use a result for the
residual invariant coefficient, assert that arbitrary coefficients
in (26) are sliced, or extend the conclusion to other degrees or
other rank-three bases. No cancellation, general-entry, termination,
or novelty claim is made.

No saved checker was executed, imported, or compiled. No canonical
file or another author's source was changed.
