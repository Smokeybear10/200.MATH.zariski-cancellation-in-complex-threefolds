# Recognition of the moving-intercept nonconstant-slope line

Under the complete actual hypotheses of288, this note recognizes the
nonconstant affine-b line branch whose intercept has nonzero n-derivative.
A compatibility identity makes that derivative reciprocal affine.
After an actual t-translation, a literal W shear gives a polynomial
pencil. Its zero-slope case supplies an actual stable three-ring. In the
other case, the exact pencil return and monic polynomial division give
an invariant actual coordinate.

The constant-intercept-derivative branch is outside the conclusion.
No rational line parameter or coefficient-field coordinate is presumed
to be an ambient polynomial coordinate.

## 1. Actual entry and the remaining coefficient identities

Retain all actual hypotheses and conclusions of the completely read
[288](principal-paraboloid-projected-line-polynomial-reduction-pass288-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
\text{full initial kernel }(X^2Z-Y^2),\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
F/\mathbb C(t)\text{ finite},\quad \ker(\partial_t|_F)=\mathbb C,
\quad L=F(n),\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=F(n,\sigma),\quad
L[\sigma]=L[v],\quad \sigma_v\in L^*.
\end{gathered}
\tag{1}
\]
The coefficient derivations commute. All coefficient integrations below
take place in the exact field F.

Use the notation of288, with the additional assumptions
\[
\begin{gathered}
y=a\sigma+rn+d_0,\quad a,d_0,r\in F,\quad
\ell=4a+k''\ne0,\quad r=a'/\ell\ne0,\\
H=bn+c,\quad b=\beta t+b_0,\quad
\beta\in\mathbb C^*,\quad b_0\in\mathbb C,\quad c,k\in F,\\
T=pn+q,\quad
\omega=-3\beta r n^2/2+v_1n+v_0,\quad p,q,v_i\in F.
\end{gathered}
\tag{2}
\]
Thus this note assumes both nonconstant b and \(r\ne0\).
The scalar restriction and two top gradient identities from288 are
\[
\begin{aligned}
0\ne\delta&=(2r^2-r')n+2rd_0+ak'r-d_0'-a^2,\\
bk''''+4\beta k'''&=0,\qquad
p'=-\frac{bk'''+3\beta(4a+k'')}{4},\\
v_1&=-3\beta d_0-\beta ak'-\frac{k'p'}2
-\frac{abk''}2-ap-\frac{pk''}2+\frac{c''}2 .
\end{aligned}
\tag{3}
\]
The actual maps remain
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,
&z&=2ty+\sigma^2+k'\sigma+n,\\
W&=w+\theta X+HX^2.
\end{aligned}
\tag{4}
\]
Write \(a_0=EX\ne0\); the actual determinant is
\(-a_0^4b\), and the selected primitive gradients have the unit
cofactor \(\eta\in L^*\) used in288.

For a direct check of every later polynomial assertion, the full
potential representatives are
\[
\begin{aligned}
\mathscr A&=(2P+k')U+k''P^2/2,\qquad
\mathscr C=U^2+k''PU+k'''P^3/6,\\
g&=pn+q+(\beta n+c')P-b\mathscr A,\\
\mathscr W&=\omega-(\beta P+p)\mathscr A-b\mathscr C
 +(\beta n+c')U+c''P^2/2+(p'n+q')P,\\
\theta&=g(y,\sigma),\qquad w=\mathscr W(y,\sigma),\\
Q_U&=(2P+k')\mathscr W_n-\mathscr W_P,\qquad
Q_P=(2U+k''P)\mathscr W_n-\mathscr W_t.
\end{aligned}
\tag{5}
\]
Formal derivatives precede moving-line evaluation. These are retained
potentials, not freely chosen polynomial maps.

## 2. Compatibility and an actual translation of t

The constant-P gradient identity is
\(Q_P(aP+rn+d_0,P)=-aQ_U(aP+rn+d_0,P)\).
Its constant coefficient, using (3), gives
\[
\omega_t=-3\beta r^2n^2+
 (-6\beta d_0r-3\beta k'ar-ap')n+w_0(t),
\qquad w_0(t)\in F.
\tag{6}
\]
For example, before substituting \(\omega_n=-3\beta rn+v_1\),
the right side is
\[
3\beta d^2+dp k''+dp'k'-dc''+2d\omega_n
+a\{2dp+dbk''+2\beta dk'-p'n-q'+k'\omega_n\},
\quad d=rn+d_0.
\]
This displays the constant-gradient origin of (6) and keeps both
\(\omega\) derivatives.

Comparison of the n-squared and n coefficients of the derivative of
\(\omega\) in (2) with (6) gives
\[
r'=2r^2,\qquad
v_1'=-6\beta d_0r-3\beta k'ar-ap'.
\tag{7}
\]
Since \(r\ne0\), exact integration of \((1/r)'=-2\) gives
\(r=-1/(2(t-\tau))\), with \(\tau\in\mathbb C\).

The normalization \(t_*=t-\tau\) is implemented by an actual map:
\[
X_*=X,\quad Y_*=Y-\tau X^2,\quad
Z_*=Z-2\tau Y+\tau^2X^2,\quad W_*=W.
\tag{8}
\]
Its polynomial inverse is
\[
Y=Y_*+\tau X_*^2,\quad
Z=Z_*+2\tau Y_*+\tau^2X_*^2,\quad X=X_*,\quad W=W_*.
\]
Moreover
\(X_*^2Z_*-Y_*^2=X^2Z-Y^2\).
The new leaders have ratios \(t-\tau,(t-\tau)^2\), so their exact
degrees are unchanged. The literal selected Z-partial is unchanged.
In the literal expansions, \(y_*=y,\sigma_*=\sigma,n_*=n,k_*=k\),
with t shifted; \(z_*=z-2\tau y\). Thus all actual returns and
coefficient fields in (1) are retained.

Rename the new chart. Then
\[
r=-\frac1{2t},\quad
y=a\sigma-\frac n{2t}+d_0,\quad
n=-2ty+2t(a\sigma+d_0),\quad
2ta'+4a+k''=0.
\tag{9}
\]
The scalar condition becomes the nonzero element of F
\[
\delta=-d_0'-d_0/t-a^2-ak'/(2t)\ne0.
\tag{10}
\]
In particular (1),(9) give
\[
K=F(y,\sigma),\qquad
\operatorname{Frac}\mathcal B=F(X,\sigma)(Y).
\tag{11}
\]
Both changes are invertible over the specified coefficient field,
with coefficient \(-1/(2t)\ne0\). They are not asserted ambient
coordinate changes.

## 3. Complex coefficient gates and the complete actual pencil

Differentiate the middle identity of (3) and use its first gradient
identity. This gives \(p''=-3\beta a'\). Define
\[
\begin{aligned}
D&=\beta k'-2p-bk''-2tp',\\
L_0&=c'-pk'-2tv_1,\qquad
E_1=-bk'+2\beta k-2tp,\\
C_1&=2ta+k',\qquad C_0=2td_0 .
\end{aligned}
\tag{12}
\]
Here D denotes a coefficient, not a derivation.
The identities (3),(7),(9) give
\[
D'=0,\quad E_1'=D,\quad L_0'=-aD,\quad C_1'=-2a,
\quad (k-tC_1)'=0.
\tag{13}
\]
For clarity, \(D'=-bk'''-4p'-2tp''
=3\beta(4a+k''+2ta')=0\).
To check the less immediate third identity, insert
\[
v_1'=3\beta d_0/t+3\beta k'a/(2t)-ap'
\]
from (7), and then the formula for \(v_1\) in (3), into
\(L_0'=c''-p'k'-pk''-2v_1-2tv_1'\).
It reduces exactly to \(-aD\).

The constants of F are complex, so write
\[
D\in\mathbb C,\quad E_1=Dt+E_0,\quad
w_c=k-tC_1\in\mathbb C,\qquad E_0\in\mathbb C.
\tag{14}
\]
The letter \(w_c\) is unrelated to the function \(w_0(t)\) in (6).

Make the actual triangular change
\[
\boxed{J=W+b_0Y^2+2\beta YZ-E_0XY.}
\tag{15}
\]
It fixes X,Y,Z, and its inverse subtracts the same displayed
polynomial from J. In particular
\(\mathcal B=\mathbb C[X,Y,Z,J]\).

Here is its full X-dependent form, not merely its X=0 intercept:
\[
\begin{aligned}
Z&=\sigma^2+C_1\sigma+C_0+(2t\sigma+k)X+t^2X^2,\\
J&=\Lambda Y+\Omega_X,\qquad
\Lambda=D(\sigma+tX)+L_0,\qquad
\Omega_X\in F[X,\sigma].
\end{aligned}
\tag{16}
\]
To verify (16) directly, substitute
\(y=Y-\sigma X-tX^2\) and
\(n=2t(a\sigma+d_0-Y+\sigma X+tX^2)\)
into (4),(5). All terms are polynomial in \(Y,X,\sigma\) over F.
The Y-squared coefficient of \(W+b_0Y^2+2\beta YZ\) is zero;
its Y coefficient is
\[
D\sigma+L_0+E_1X.
\]
Equation (14) and (15) give (16), leaving a Y-independent polynomial
\(\Omega_X\). This proves the claimed polynomial membership.
It does not use or assume that F is rational.

Set \(M=F(X,\sigma)\). The field return (11) and the actual
coordinates (15) give
\[
M(Y)=\mathbb C(X,Z)(Y)(\Lambda Y+\Omega_X).
\tag{17}
\]
The element Y is transcendental over M. Also Z has exact
degree two in \(\sigma\) over \(F(X)\), so
\(k_0=\mathbb C(X,Z)\subset M\) has transcendence degree one
less than M.

## 4. The case D=0: an actual stable polynomial three-ring

If \(D=0\), (13) gives \(L_0\in\mathbb C\). The actual coordinate
\[
J_*=J-L_0Y,\qquad S=\mathbb C[X,Z,J_*],\qquad
\mathcal B=S[Y]
\tag{18}
\]
has a polynomial inverse, and \(J_*=\Omega_X\in M\).
Equation (17) gives \(M(Y)=\operatorname{Frac}(S)(Y)\).
Since Y is transcendental over M, coefficient comparison in rational
expressions in Y shows
\(M\cap\operatorname{Frac}(S)(Y)=\operatorname{Frac}(S)\).
Consequently \(M=\operatorname{Frac}(S)\).

The derivation \(E/a_0\), with \(a_0=EX\), is the X-partial
with K fixed. Equation (16), and the original expression for Y,
give
\[
(EX,EZ,EJ_*,EY)/a_0
=(1,\partial_X Z,\partial_X\Omega_X,\sigma+2tX)
\in\operatorname{Frac}(S)^4.
\tag{19}
\]
This is initially only a fraction-field assertion.

Choose a primitive common-denominator vector \(f_i\in S\), of
gcd one, proportional to (19). The actual coordinate derivatives
are \(g f_i\) for a common \(g\in\operatorname{Frac}(S)[Y]\).
They all belong to \(S[Y]\). For each prime of S, at least one
\(f_i\) is prime-to-it; Gauss content therefore gives \(g\in S[Y]\).
The actual polynomial slice satisfies \(Eu=1\), so the chain rule
makes g divide 1. Thus \(g\in\mathbb C^*\), and every coordinate
derivative is in S. In particular \(E(S)\subset S\).

The nonzero LND \(E_0=E|_S\) has \(E_0^2X=0\).
Divide its three coefficients by their gcd \(\Delta\).
Since \(\Delta\mid E_0\Delta\), local nilpotence implies
\(E_0\Delta=0\). The primitive derivation \(E_0/\Delta\) is an LND,
has the same kernel, and still has a nonzero first and zero second
derivative on the actual coordinate X.
[Daigle's theorem as restated in Dasgupta--Gupta, Theorem4.8](https://arxiv.org/html/1701.03635v1)
therefore supplies an invariant polynomial coordinate of S.
It is also an ambient coordinate of \(S[Y]\).
The regular-kernel theorem
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives \(A\cong\mathbb C^{[3]}\).
This repeats the precise content and slice argument, rather than
assuming that the rational ratios in (19) were polynomial.

## 5. The case D nonzero: a quadratic coefficient relation

Now assume \(D\in\mathbb C^*\). Put
\[
u_c=\frac{DC_1-2L_0}{D^2},\qquad
v_c=C_0+\frac{L_0^2}{D^2}-\frac{C_1L_0}{D}.
\tag{20}
\]
From (13),(10),
\[
u_c'=0,\quad u_c\in\mathbb C,\qquad
v_c'=C_0'+aC_1=-2t\delta\ne0.
\tag{21}
\]
Thus \(v_c\in F\subset K\) is nonconstant and invariant under E,
and \(F/\mathbb C(v_c)\) is finite. Completing the square in
(16) gives the exact relation
\[
\boxed{Z=w_cX+\Lambda^2/D^2+u_c\Lambda+v_c.}
\tag{22}
\]
There is no original-ring polynomiality assertion about \(\Lambda\)
or \(v_c\) at this point.

Since \(D\ne0\), \(M=F(X,\Lambda)\).
The variables X and \(\Lambda\) are algebraically independent over F.
The nonconstant \(v_c\) and (22) show that X,Z,\(\Lambda\) are
algebraically independent over \(\mathbb C\), so \(\Lambda\)
is transcendental over \(k_0=\mathbb C(X,Z)\).

We record the function-field argument used with (17). If a
one-variable characteristic-zero function field M over \(k_0\)
satisfies
\[
M(Y)=k_0(Y)(\lambda Y+\omega),\qquad Y\text{ transcendental over }M,
\]
and \(\lambda\) is transcendental over \(k_0\), then
\[
M=k_0(\lambda),\qquad \omega\in k_0+k_0\lambda.
\tag{23}
\]
Indeed the displayed right field is rational of transcendence degree
two over \(k_0\), which first makes \(k_0\) relatively algebraically
closed in M. Characteristic zero supplies a regular curve field.
On its smooth projective model, the generic function
\(\lambda Y+\omega\) has at each point the maximum pole order of
\(\lambda,\omega\): their leading polar coefficients cannot cancel
over the transcendental variable Y. Residue-field degrees are retained
by this base change. Its pole-divisor degree is 1 by the field equality,
so the pole degree of \(\lambda\) is at most 1.
Therefore \([M:k_0(\lambda)]=1\).
On \(M=k_0(\lambda)\), \(\lambda\) has exactly the single simple
rational pole at infinity. The same maximum-pole statement leaves
\(\omega\) with no other poles and at most that simple pole, proving
the last assertion of (23).

The curve model and pole-degree facts are the primary results
[Stacks, Theorem53.2.6](https://stacks.math.columbia.edu/tag/0BY1)
and [Stacks, Lemma33.44.11](https://stacks.math.columbia.edu/tag/0AYZ).
This argument does not assume closed base field or rationality of F.

Apply (23) to (17). There are \(\alpha,\gamma\in\mathbb C(X,Z)\) with
\[
M=\mathbb C(X,Z,\Lambda),\qquad
\Omega_X=\alpha(X,Z)\Lambda+\gamma(X,Z).
\tag{24}
\]
Equation (22) identifies this last field with
\(\mathbb C(X,\Lambda,v_c)\). Since X,\(\Lambda\) are independent
over F, the exact extension degree in (24) is
\([F:\mathbb C(v_c)]\). Hence
\[
\boxed{F=\mathbb C(v_c).}
\tag{25}
\]
The conclusion uses the actual pencil return, not only the quadratic
relation or the calibrated Jacobian.

## 6. Monic division makes the pencil corrections polynomial

We prove, rather than presume, that the two coefficients in (24)
are polynomial:
\[
\boxed{\alpha,\gamma\in\mathbb C[X,Z].}
\tag{26}
\]
By (16),(25),
\(\Omega_X\in\mathbb C(v_c)[X,\sigma]\).
Moreover
\(\sigma=(\Lambda-L_0(v_c))/D-t(v_c)X\), so
\(\Omega_X\in\mathbb C(v_c)[X,\Lambda]\).
Clear the finitely many coefficient denominators to write
\[
\Omega_X=\frac{N(X,v_c,\Lambda)}{d(v_c)},\qquad
N\in\mathbb C[X,v_c,\Lambda],\quad
0\ne d\in\mathbb C[v_c].
\]
Substitute (22), with X,Z,\(\Lambda\) independent. The denominator
\[
d\bigl(Z-w_cX-\Lambda^2/D^2-u_c\Lambda\bigr)
\]
is a polynomial in \(\Lambda\) over \(\mathbb C[X,Z]\) whose
leading coefficient is a nonzero complex number. If d is constant
there is nothing to prove. Otherwise multiply numerator and
denominator by a complex unit to make that denominator monic.

Perform polynomial division of the substituted numerator by this
monic denominator over the ring \(\mathbb C[X,Z]\).
Its quotient and remainder belong to
\(\mathbb C[X,Z,\Lambda]\). By (24), division over the fraction
field \(\mathbb C(X,Z)\) has zero remainder, because \(\Omega_X\)
is already a polynomial in \(\Lambda\) there. Uniqueness of monic
division makes the original remainder zero. Thus
\(\Omega_X\in\mathbb C[X,Z,\Lambda]\).
Its degree is at most one by (24), proving (26).
No general intersection rule for unrelated polynomial rings is used.

## 7. A reduced invariant denominator gives an actual coordinate

Use (26) to make the actual polynomial changes
\[
P_*=Y+\alpha(X,Z),\qquad Q_*=J-\gamma(X,Z).
\tag{27}
\]
Together with X,Z these are polynomial coordinates: the inverse is
\(Y=P_*-\alpha(X,Z)\), \(J=Q_*+\gamma(X,Z)\), followed by the
explicit inverse of (15). In particular \(P_*,Q_*\) are coprime
in the original polynomial ring.

Equations (16),(24) give the literal rational equality
\(Q_*=\Lambda P_*\). Use this in (22):
\[
v_c=
\frac{(Z-w_cX)P_*^2-u_cQ_*P_*-Q_*^2/D^2}{P_*^2}.
\tag{28}
\]
The numerator modulo \(P_*\) is \(-Q_*^2/D^2\), so it is prime-to
\(P_*\). Since \(Ev_c=0\), differentiating (28) and reducing modulo
\(P_*\) shows \(P_*\mid EP_*\).
Local nilpotence forces \(EP_*=0\): otherwise the E-degree of
\(EP_*\) would be one smaller than that of \(P_*\), while
divisibility would make it at least as large.

Thus \(P_*\), not the rational function \(\Lambda\), is the
invariant ambient polynomial coordinate. The kernel A is regular
because \(\mathcal B=A[u]\) is a polynomial ring. The same
Bhatwadekar--Gupta--Lokhande Theorem3.5 applied with coordinate
\(P_*\) gives
\[
\boxed{A\cong\mathbb C^{[3]}.}
\tag{29}
\]

## 8. Scope and verification boundary

The two cases \(D=0\) and \(D\ne0\) exhaust the line branch (2)
with \(\beta\ne0,r\ne0\). No assumption that F was rational,
that \(\sigma\) was ambient, or that a fraction-field coordinate
descended automatically was made. The nonconstant-b branch with
r=0 remains outside this note, as do arbitrary entry into271 and
unrestricted cancellation.

Fresh unsaved expansions checked (6), the coefficient identities
behind (13), and the complete full-X pencil (16), with all lower
coefficient functions retained. The field return, pole degrees,
monic division, primitive-content and invariant-denominator steps
are mathematical arguments above, not finite-checker conclusions.
No saved checker was executed, imported or compiled, and no earlier
source, packet or index was edited. The directly used sources288
and the generic-pencil/content proof285 were read; older retained
proof chains are not recursively certified here. No novelty, human
certification or unrestricted solution is asserted.

