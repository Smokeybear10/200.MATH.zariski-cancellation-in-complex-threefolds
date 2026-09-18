# Recognition of the supplied normalized potential family

Working result: in the actual principal chart264 with \(k=s,n=0\),
the three degree pairs left by corrected301 when \(\ell_{ss}\ne0\)
are impossible. The new exclusions are \((1,2),(1,4),(2,4)\) for
\((\deg_v y,\deg_v\sigma)\). Consequently every supplied actual
chart with \(k=s,n=0\) is recognized, by combining these exclusions
with the already retained endpoints298 and corrected301.

No argument puts arbitrary k,n into this form. The conclusion is not
recognition of every principal1222 chart or unrestricted cancellation.
The actual all-X polynomial return is essential in the first exclusion;
the other two use the exact quartic plane primitive and whole plane return.

## 1. Actual entry and the exact plane primitive

Retain the full actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\qquad a_0=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
K=\operatorname{Frac}A=L(v),\\
K=\mathbb C(y,z,w),\qquad
L[y,z,w]=L[y,\sigma,\theta]=L[v]=:O,\qquad
J(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
N is the actual shift-four leading derivation of the literal Z-partial;
\(Na_0=Nt=Ns=0\). The coefficient partials extend uniquely to L,
commute, and fix v. All intercepts and L are killed by E.

Assume \(k=s,n=0\). For now also assume \(\ell_s\ne0\).
The actual formulas are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta,&w&=\ell-2\sigma y,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{2}
\]
The third level is \(y^2-\ell_t\sigma-\ell_s\theta=h\in L\).
Since \(\ell_s\ne0\), it solves theta polynomially in y,sigma and gives
the genuine whole plane return \(L[y,\sigma]=O\).

Use the coefficient parameter \(r=\ell\), and denote
\[
s=H(t,r),\qquad H_r=1/\ell_s\ne0,\qquad
\mathcal L=H_rh.
\tag{3}
\]
The field L is finite over \(\mathbb C(t,r)\), not assumed equal to
that rational field. Derivatives below are the exact new coefficient
partials on L. The complete formulas from301 are
\[
\begin{aligned}
\theta&=H_ry^2+H_t\sigma-\mathcal L,\\
z&=\sigma^2+H_t\sigma+H_ry^2+2ty-\mathcal L,
\qquad w=r-2\sigma y,\\
Q(U,P)&=\frac{H_{rr}}2U^4+H_{tr}U^2P+\frac{H_{tt}}2P^2
       +2UP+H_tU-\mathcal L_rU^2-\mathcal L_tP,\\
Q(y,\sigma)&=q_0\in L.
\end{aligned}
\tag{4}
\]
Here U,P are independent formal variables. The primitive follows from
the full scalar determinant, not an arbitrary plane-curve ansatz.
Its evaluated gradient is a unit ideal, by296's two-gradient minor
identity and the unit V-coefficient of the third potential.

Throughout, the reference to
[301](principal-paraboloid-affine-second-potential-reduction-pass301-working.md)
means its Sections1--2 and4--6 together with the mandatory
[constant-first correction](principal-paraboloid-affine-second-potential-pass301-correction-working.md).
The invalid auxiliary fixed-ring argument in the original Section3 is
not used. Its replacement proves \(y\notin L\) from the complete scalar.

## 2. Why only three pairs need to be excluded

This section records the precise retained frontier before adding new
arguments. Suppose \(\ell_{ss}\ne0\), equivalently \(H_{rr}\ne0\).
Let G be the full irreducible plane equation of \(L[y,\sigma]=L[v]\).
The unit-gradient conclusion gives
\[
Q-q_0=\eta G+G^2R,\qquad \eta\in L^*,\quad R\in L[U,P].
\tag{5}
\]
Indeed the cofactor of G evaluates to a unit; subtracting that unit
puts its difference in the full ideal \((G)\). The whole plane return
also gives
\(\deg G=\max(\deg_v y,\deg_v\sigma)\), with a pure-power leading
homogeneous form. These facts hold over the exact field L.

The top of Q is the nonzero multiple \(H_{rr}U^4/2\). A selected
degree three is impossible in (5). A selected line would have top U,
forcing y constant, excluded by the corrected scalar argument. The
remaining degrees are two and four, with top proportional to a power
of U, so
\(0<\deg_v y<\deg_v\sigma=\deg G\).

The pair (3,4) cannot have the whole plane return: the monic minimal
polynomial of sigma over \(L(y)\) has degree three and coefficients
in \(L[y]\), by integrality and normality of that polynomial ring.
Thus \(L[y,\sigma]\) is spanned over \(L[y]\) by
\(1,\sigma,\sigma^2\). Their nonzero polynomial multiples have
leading degrees in distinct residue classes modulo three and cannot
combine to give a polynomial of degree one. This contradicts v in O.
Consequently the retained necessary list is
\[
(\deg_v y,\deg_v\sigma)\in\{(1,2),(1,4),(2,4)\}.
\tag{6}
\]
The following arguments exclude every pair in (6). They do not assume
that the cubic surface of264 is reducible.

## 3. The pair (1,2): all-X generation removes the linear coefficient

Suppose \(\deg_v y=1\), \(\deg_v\sigma=2\). The original intercept y
is an affine parameter, so \(O=L[y]\). Write, without translating y,
\[
\sigma=A_2y^2+A_1y+A_0,\qquad A_i\in L,\quad A_2\ne0.
\tag{7}
\]
Formula (4) makes theta quadratic or lower in y. Therefore the full W
in (2) has exact y-degree three, with coefficient \(-2A_2\), for every
fixed X in any coefficient-field extension.

Actual E-stability supplies an equality stronger than a field return:
\[
\boxed{L[\mathcal B]=L[X,Y,Z,W]=L[X,y].}
\tag{8}
\]
For the nontrivial inclusion, \(\sigma=EY/a_0-2tX\) belongs to
\(L[\mathcal B]\), since E preserves the original polynomial ring
and kills L. Then \(y=Y-\sigma X-tX^2\) also belongs to it. The
opposite inclusion follows from (2),(4),(7). This is the actual
all-specializations gate of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md),
not a statement about an arbitrary formal map.

If \(A_1\ne0\), evaluate (8) at the coefficient-field value
\(X=x_0=-1/A_1\in L^*\). Denote the three resulting polynomials
by \(Y_0,Z_0,W_0\). Then
\[
Y_0=-\frac{A_2}{A_1}y^2+A_0x_0+tx_0^2,
\qquad [y^3]W_0=-2A_2\ne0.
\tag{9}
\]
The first two actual potentials imply the exact identity
\[
Y^2+XW-X^2Z=y^2+rX.
\tag{10}
\]
Consequently
\[
Z_0=\frac{Y_0^2+x_0W_0-y^2-rx_0}{x_0^2}.
\]
All divisions here are by units of the fixed coefficient field. Using
(9) in both directions, specialization of (8) therefore gives
\[
L[y]=L[Y_0,Z_0,W_0]=L[y^2,W_0].
\tag{11}
\]
This is impossible. Subtract the even part of the cubic W0; its odd
part is \(y(ay^2+b)\) with \(a=-2A_2\ne0\). The generated algebra is
exactly
\(L[y^2]\oplus y(ay^2+b)L[y^2]\), whose odd part cannot contain y.
This is the elementary degree-two/three obstruction of323.
No original ambient evaluation or differentiation of x0 was used.

It follows that \(A_1=0\). Substitute
\(P=A_2U^2+A_0\) into the **complete** Q in (4). All terms are even
in U except
\[
2A_2U^3+(2A_0+H_t)U.
\tag{12}
\]
The cubic coefficient is nonzero. Since y is transcendental over L,
this polynomial cannot evaluate to the coefficient-field constant q0.
Thus the pair (1,2) is excluded.

## 4. The pair (1,4): three successive coefficients

Again y is the original affine parameter. Write
\[
\sigma=A_4y^4+A_3y^3+A_2y^2+A_1y+A_0,
\qquad A_i\in L,\quad A_4\ne0.
\tag{13}
\]
Substitute the corresponding polynomial P into Q(U,P). The successive
highest relevant coefficients, imposing each preceding vanishing, are
\[
\begin{aligned}
[U^8]Q&=H_{tt}A_4^2/2,\\
[U^6]Q\bigm|_{H_{tt}=0}&=H_{tr}A_4,\\
[U^5]Q\bigm|_{H_{tt}=H_{tr}=0}&=2A_4.
\end{aligned}
\tag{14}
\]
Constancy of Q(y,sigma) forces the first two to vanish, while the
third cannot vanish. After those two gates all other terms in (4)
have U-degree at most four. There are no derivatives of the Ai in
this formal substitution. This excludes (1,4), without another
specialization argument.

## 5. The pair (2,4): the whole odd module and a cubic obstruction

Suppose \(\deg_v y=2\), \(\deg_v\sigma=4\). An affine translation of
the polynomial parameter over L, with no extraction of a square root,
gives
\[
y=a x^2+h_c,\qquad a\in L^*,\quad h_c\in L,
\qquad O=L[x].
\tag{15}
\]
This is a coefficient-field parameter, not an ambient coordinate
change; y remains the original intercept. The even part of sigma
is a polynomial \(\Pi(y)=Ay^2+By+D\), with \(A\ne0\), and its
odd part has the form \(xR(x^2)\), with \(R(T)\in L[T]\).
Because \(L[y]=L[x^2]\), the whole return reads
\[
L[x]=L[y,\sigma]=L[x^2,xR(x^2)]
     =L[x^2]\oplus xR(x^2)L[x^2].
\tag{16}
\]
The equality on the right holds since the square of the odd generator
belongs to the even ring. To contain x, its odd coefficient R must be
a nonzero unit of \(L[x^2]\). Hence
\[
\boxed{\sigma=\Pi(y)+Cx,
\quad \Pi(y)=Ay^2+By+D,\quad A,C\in L^*,\quad B,D\in L.}
\tag{17}
\]
This rules out a cubic odd part by the full polynomial-ring equality,
not just birationality.

Take the odd part in x of the literal identity Q(y,sigma)=q0.
Since y is even, it is exactly
\[
Cx\{H_{tr}y^2+H_{tt}\Pi(y)+2y-\mathcal L_t\}=0.
\tag{18}
\]
The domain property and transcendence of y over L give
\[
H_{tr}+H_{tt}A=0,\qquad H_{tt}B+2=0,
\qquad H_{tt}D-\mathcal L_t=0.
\tag{19}
\]
In particular \(H_{tt}\ne0\). Use (18) to combine the terms linear
in the even polynomial Pi with its square in the even part of Q.
Using \(x^2=(y-h_c)/a\), the remaining identity is
\[
\frac{H_{rr}}2y^4-\frac{H_{tt}}2\Pi(y)^2
 +H_ty-\mathcal L_ry^2
 +\frac{H_{tt}C^2}{2a}(y-h_c)=q_0.
\tag{20}
\]
Its y-cubic coefficient is
\[
-H_{tt}AB=2A\ne0
\tag{21}
\]
by (19). None of the other terms in (20) has degree three. This is
the required contradiction. No moving-coefficient derivative was
discarded: (18)--(21) are polynomial substitutions in the already
derived primitive over L.

## 6. Exhaustive conclusion within the supplied subfamily

Sections3--5 exclude every pair in (6). Therefore the actual chart
cannot have \(k=s,n=0,\ell_s\ne0,\ell_{ss}\ne0\).
The remaining alternatives are already recognized:

| Coefficient case in the supplied chart | Retained endpoint |
| --- | --- |
| \(\ell_s=0\) |298, including its separate constant-first and nonlinear-potential arguments |
| \(\ell_s\ne0,\ell_{ss}=0\) |301 with its mandatory correction, followed by its actual degree-lowering map |
| \(\ell_s\ne0,\ell_{ss}\ne0\) |Excluded by the three new arguments above |

Both earlier endpoints retain their stated recognition dependencies.
In particular301 uses257 only after constructing an actual coordinate
frame of profile1122 or an invariant coordinate. We conclude
\[
\boxed{\text{Under the complete actual264 hypotheses,}\quad
        k=s,\ n=0\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{22}
\]
Every actual frame in this supplied subfamily also satisfies
\(\ell_{ss}=0\). This necessity does not assert that every such
formal coefficient family is realized.

The \(\ell_s=0\) input is
[298](principal-paraboloid-one-variable-potential-recognition-pass298-working.md).
The other input is explicitly corrected301, not its withdrawn
auxiliary fixed-ring argument. The special complex-affine calculation329
is not needed for this composition and adds no separate parameter coverage.

## 7. Verification and scope boundary

The complete sources264,296,301 and its correction,298,323,325 and257
were read before this composition. Fresh unsaved algebra reconstructed
the formal odd parts, the three sequential quartic coefficients, and
the final cubic coefficient with arbitrary retained lower jets.
These checks supplement the displayed algebra, not the whole-ring or
exact-field proofs. No saved checker was executed, imported, compiled,
or rerun. No earlier proof, canonical index, or ledger was edited.

No surface factorization, rationality of L, or original-coordinate
status of x or y is assumed. The specializations in Section3 are over
the fixed exact coefficient field and preserve polynomial generation.
The note does not normalize a general nonzero k_s chart to k=s,n=0,
recognize arbitrary1222 frames, or solve unrestricted cancellation.
