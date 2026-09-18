# A cubic divided-pair unit condition and its longitudinal exclusion

Working bounded result: retain the FULL actual264/296/535 chart,
with noncomplex m, quadratic intrinsic sigma and cubic theta.
For arbitrary y of degree at most four, the entire all-X polynomial
return gives the explicit unit condition below. Its degenerate
vertical component is retained, not removed by a denominator.

As a consequence, the excess-degree case deg y=4 cannot have
h=m_s=0. This excludes precisely the longitudinal excess family
retained in554. It does not exclude the h nonzero excess families
or the cases deg y at most three, and supplies no recognition or
general chart-entry theorem.

## 1. Full actual inputs and the all-X return

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular the actual data include
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u_{\rm glob}],
\quad E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,
\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
N=[u_{\rm glob}^4]\partial_Z|_{\mathcal A}\ne0,
\quad Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,
\quad [L:\mathbb C(t,s)]<\infty,\quad L[\mathcal A]=L[v],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),
\quad L[y,z_{\rm int},w]=L[v],\quad m=k_s\notin\mathbb C.
\end{gathered}
\tag{1}
\]
The intercept z_int is the literal original Z-intercept. The
original global slice, selected literal partial, both returns,
genuine moving levels and full scalar remain required. In
particular m is nonzero.

Use the finite intrinsic normalization of
[553](principal-paraboloid-quadratic-sigma-higher-theta-degree-bound-pass553-working.md).
Thus in L'=L(rho), with rho squared in L*,
x=rho(v-v0) and
\[
\begin{gathered}
\sigma=x^2+c,\quad\theta=ax^3+bx^2+dx+e,\quad a\ne0,\\
y=r_4x^4+r_3x^3+r_2x^2+r_1x+r_0,\qquad r_i\in L',\\
Nx=\rho,\qquad J_{t,s,x}(X)=-a_0^4/\rho,\qquad
\kappa=\kappa_v/\rho^2\in(L')^*.
\end{gathered}
\tag{2}
\]
The coefficients r4,r3 and every lower coefficient may vanish.
The zero y polynomial is included. All coefficient partials are
the exact commuting extensions from C(t,s), extended to fix x.
No rationality of L' or descent of rho is assumed, and x is not
promoted to an actual coordinate. Source553 supplies deg y at most
four in the present cubic-theta sector.

There is an ALL-X whole polynomial return, not only a return at
one fiber. Indeed \(\mathcal B_{a_0}=\mathcal A_{a_0}[X]\).
Since a0 is in L*, adjoining L makes its inverse available on both
sides. Using L[A]=L[v] and then extending coefficients to L' gives
\[
\boxed{L'[X,Y,Z,W]=L'[X,x].}
\tag{3}
\]
All rings in (3) are the displayed subrings of the same coefficient
overring; no arbitrary coefficient-field map is substituted for
the actual four-ring. The polynomial inverse for x supplied by (3)
will be the source of the divided-pair unit ideal.

Write p=m_t, h=m_s, k1=k_t, k2=k_tt, and use mathfrak n for the
potential n. The complete actual rows and second potential are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_1\sigma+m\theta+\mathfrak n
                                      +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_1)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=k_2P^2/2+pPV+hV^2/2+
                                    \mathfrak n_tP+\mathfrak n_sV.
\end{aligned}
\tag{4}
\]
No constant or lower coefficient in these rows is discarded.

## 2. The complete divided-pair identity

Introduce independent x1,x2, keep the SAME actual X for both,
and write u=x1+x2 and z=x1*x2. In this source u is solely this
pair-sum variable, not the original global slice. For a polynomial
f in x define its polynomial divided difference
\(f^{[1]}=(f(x_1)-f(x_2))/(x_1-x_2)\). This is a polynomial
identity, including x1=x2, where it takes the derivative value.
We never invert x1-x2.

Define the complete symmetric sums
\[
\begin{aligned}
S_\sigma&=u^2-2z+2c,\\
S_\theta&=a(u^3-3uz)+b(u^2-2z)+du+2e,\\
S_y&=r_4(u^4-4u^2z+2z^2)+r_3(u^3-3uz)
                         +r_2(u^2-2z)+r_1u+2r_0,\\
Y_d&=r_4(u^3-2uz)+r_3(u^2-z)+r_2u+r_1,\\
\overline F_P&=k_2S_\sigma/2+pS_\theta/2+\mathfrak n_t,\qquad
\overline F_V=pS_\sigma/2+hS_\theta/2+\mathfrak n_s.
\end{aligned}
\tag{5}
\]
Thus Yd is y's divided difference, not that of the whole Y row.
The bars in (5) denote exact midpoint polarization of the quadratic
potential, not evaluation at an independently chosen midpoint.

Set
\[
\begin{gathered}
D(u)=2u+ma,\qquad q_0=2c+k_1,\\
N(u)=u^3+ma u^2+(q_0+mb)u+md,\qquad
P(u,z)=N(u)-D(u)z,\\
\mathcal E(u,z)=S_y+\overline F_P
                        -{S_\sigma+k_1\over m}\overline F_V.
\end{gathered}
\tag{6}
\]
Expansion of ALL three literal rows (4) gives
\[
\begin{aligned}
Y^{[1]}&=Y_d+uX,\\
Z^{[1]}-2tY^{[1]}&=P,\\
mW^{[1]}\big|_{X=-Y_d/u}+u\mathcal E
 &=-P\left(Y_d/u+\overline F_V/m\right).
\end{aligned}
\tag{7}
\]
The last identity is in the localization u nonzero and holds
BEFORE P is set to zero. For example the second-potential
difference is
\((S_\sigma+k_1)Y_d+uS_y+u\overline F_P+
\theta^{[1]}\overline F_V\), with its negative sign in mw.
Together with \(P=u(S_\sigma+k_1)+m\theta^{[1]}\), this proves
the last line of (7). It verifies the sign and every lower term.

## 3. The necessary unit and its faithful pair lift

The polynomial inverse x=Psi(X,Y,Z,W) from (3) implies
\[
(Y^{[1]},Z^{[1]},W^{[1]})
                 L'[X,x_1,x_2]=L'[X,x_1,x_2].
\tag{8}
\]
Indeed telescope the difference of Psi with the same X, divide
the resulting polynomial identity by x1-x2, and obtain 1 as a
polynomial combination of the three displayed differences.
This is stronger than injectivity on distinct pairs; diagonal
pairs are explicitly retained.

Work first on u nonzero. The symmetric coefficient ring is
S=L'[u,u inverse,z], and the full pair ring is
\[
S[x_1]/(x_1^2-u x_1+z),\qquad x_2=u-x_1.
\tag{9}
\]
It is finite FREE of rank two over S, including at the discriminant
zero. In particular it is faithfully flat. Eliminate X using the
first line of (7), then use the other two lines and the units m,u.
Equation (8) says that (P,E) becomes the unit ideal in (9).
Faithful flatness therefore gives (P,E)=S. Equivalently
\[
\boxed{\mathcal E\text{ is a unit of }
       R=S/(N-Dz).}
\tag{10}
\]
Only the polynomial inverse, not a rational inverse or generic
point-separation assertion, is used here. No actual coordinate
has been specialized to a moving root.

There is also a simple retained condition on the omitted u=0
boundary. There theta's divided difference is d-az, and Yd is
r1-r3*z. At z=d/a, simultaneous vanishing would make every row
difference in (4) vanish for every X, including W by its complete
second potential. Every such (u,z) lifts after scalar extension by
the same monic quadratic presentation BEFORE u is inverted, so
(8) rules this out. Thus
\[
ar_1-dr_3\ne0.
\tag{11}
\]
This boundary observation uses the same monic quadratic pair lift
before u is inverted; its diagonal case is allowed. It is not
needed for the exclusion in Section6.

## 4. Complete rational numerator and the nondegenerate case

The full expression E in (6) has degree at most two in z. Here is an
explicit support formula retaining every coefficient. Put
\[
S_0=u^2+2c,\quad T_0=au^3+bu^2+du+2e,\quad
v_0=3au+2b,\quad Q_0=S_0+k_1,\quad
V_0=pS_0/2+hT_0/2+\mathfrak n_s.
\tag{12}
\]
These are temporary polynomials in u, not new line parameters.
Then E=E0+E1*z+E2*z squared, with
\[
\begin{aligned}
E_0={}&r_4u^4+r_3u^3+r_2u^2+r_1u+2r_0
                    +k_2S_0/2+pT_0/2+\mathfrak n_t-Q_0V_0/m,\\
E_1={}&-4r_4u^2-3r_3u-2r_2-k_2-pv_0/2
                        +\{Q_0(p+hv_0/2)+2V_0\}/m,\\
E_2={}&2r_4-(2p+hv_0)/m.
\end{aligned}
\tag{13}
\]
Let u_star=-ma/2, which is NONZERO because m and a are nonzero,
and put
\[
\delta=N(u_*)=
m\{d-aq_0/2-mab/2+m^2a^3/8\}.
\tag{14}
\]
First assume delta nonzero. Then D and N are coprime. A Bezout
identity for them shows that D is a unit in R, since N=Dz there.
Consequently the exact ring is
\[
R\simeq L'[u,u^{-1},D^{-1}],\qquad z=N/D.
\tag{15}
\]
Define the full polynomial numerator
\[
\mathcal U(u)=E_0D^2+E_1DN+E_2N^2,
\qquad \mathcal E(u,N/D)=\mathcal U(u)/D^2.
\tag{16}
\]
Despite the possible degree-seven terms in the three summands,
they cancel identically. The complete expression satisfies
\[
\begin{gathered}
\deg_u\mathcal U\le6,\qquad
[u^6]\mathcal U=-2r_4-ha^2/2,\\
\mathcal U(u_*)=E_2(u_*)\delta^2,\qquad
E_2(u_*)=2r_4-2p/m+3ha^2/2-2hb/m.
\end{gathered}
\tag{17}
\]
No nonvanishing of these coefficients is presumed in the general
unit statement. Formula (16) itself is the full numerator, not a
selected-leading truncation.

The two irreducibles u and D are nonassociate since u_star is
nonzero. The units of (15), together with the fact that U is a
polynomial, show that (10) is exactly the necessary restriction
\[
\boxed{\mathcal U=\lambda u^iD^j,\quad
\lambda\in(L')^*,\quad i,j\ge0,\quad i+j\le6.}
\tag{18}
\]
Equivalently E=lambda*u to the i*D to the (j-2). In particular
the exponent at u cannot be negative for this full rational
expression. If E2(u_star) is nonzero, (17) further forces j=0.
If it vanishes, no such conclusion is made. U identically zero
is impossible because E must be a unit.

## 5. Delta zero retains a complete vertical component

Now assume delta=0. Exact polynomial division gives
\[
N=D M,\qquad
M(u)=u^2/2+ma u/4+(q_0+mb)/2-m^2a^2/8.
\tag{19}
\]
Thus P=D(M-z), and the pair curve on u nonzero is the union
of the graph z=M(u) and the vertical line u=u_star. These meet
at (u_star,M(u_star)); neither component can be discarded.

Algebraically the two component ideals (D) and (z-M) in S have
intersection their product, and their sum is the maximal ideal
(D,z-M). The ring R is their fiber product over L' at that point.
A pair of restrictions is a unit exactly when both restrictions
are units, since their inverse values still agree at the
intersection. Therefore (10) requires, and is equivalent on this
pair curve to, BOTH conditions
\[
\boxed{\begin{gathered}
E_2(u_*)=E_1(u_*)=0,\qquad E_0(u_*)\ne0,\\
\mathcal E(u,M(u))=\lambda u^i,
\quad\lambda\in(L')^*,\quad 0\le i\le4.
\end{gathered}}
\tag{20}
\]
The first line says that the polynomial on the full vertical
line is a nonzero constant. The second uses the units of
L'[u,u inverse]. Its exponent is nonnegative because the graph
expression is a polynomial in u, of degree at most four by
(16)--(19). The values at the intersection agree automatically;
in particular lambda*u_star to the i=E0(u_star).

This case includes vanishing E2, E1, r4, r3, p or h whenever
consistent with the other retained identities. A nonconstant
vertical polynomial is never a unit, even if it has no root over
the initial coefficient field. Scalar extension, or equivalently
the maximal-ideal criterion, retains its algebraic roots.

## 6. Excluding h=0 in the excess-degree profile

Now impose r4 nonzero and h=0 as a coefficient-field identity.
In particular h_s=h_t=0. The complete held source
[554](principal-paraboloid-cubic-excess-leading-families-pass554-working.md)
was read through EOF. Its required next-coefficient argument is
briefly reproduced here so that no transverse formula is imported.

The full H degree-eight coefficient and the full degree-seven
coefficient after using it give
\[
r_4=2p/m,\qquad p\ne0,\qquad
r_4r_3+a(p^2/m+p_t/2)=0.
\tag{21}
\]
The first comes from r4 squared-2p*r4/m=0, with r4 nonzero.
Set lambda0=-p/2-mp_t/(4p), so r3=lambda0*a. All of m,p,r4
and lambda0 are killed by partial_s. The full B multiplier
coefficient of degree six gives aa_s=-8p/m squared. The full
A multiplier coefficient of degree six, with all lower jets
present, is
\[
4(r_4)_t+6a(r_3)_s+16r_4^2
                       =20(mp_t+4p^2)/m^2=0.
\tag{22}
\]
For h=0 the formal H_V has degree at most four, which forces
this positive coefficient to vanish. Thus p_t=-4p squared/m,
and the needed leading identities are
\[
\boxed{r_4=2p/m\ne0,\qquad r_3=pa/2.}
\tag{23}
\]
This proof does not need554's subsequent fifth-root integration.
All partials used in (21)--(22) are the genuine fixed-x
coefficient partials, not independently chosen leading jets.

In the present h=0 case (13),(16) simplify at their top to
\[
E_2=2r_4-2p/m=2p/m\ne0,
\quad [u^6]\mathcal U=-2r_4\ne0,
\quad [u^5]\mathcal U=-4ma r_4-2r_3-pa=-10pa\ne0.
\tag{24}
\]
These are coefficients of the COMPLETE rational numerator (16).
In particular the u-fifth coefficient has no unretained lower
y, theta or potential contribution.

If delta=0, the first condition in (20) contradicts E2 nonzero.
If delta is nonzero, (17) shows U(u_star) nonzero, so j=0 in
(18). Since U has exact degree six, (18) then forces
U=lambda*u to the sixth. Its u-fifth coefficient would be zero,
contrary to (24). Both cases are impossible. This proves the
bounded exclusion h=0 when theta is cubic and y has degree four.

## 7. Verification and scope

The full264/296/535 sources and the complete formal-support input521
were freshly read before this continuation, and complete553 was
independently audited. Complete554 was read through EOF at its
held hash33c560b3a9edd9519c9d2545b68311edf7ade237a3c5673b9e2e0428ef4f7e54.
Its separate source acceptance is not replaced by this bounded
use and rederivation of (21)--(23).

Fresh unsaved d4f527 begins with ALL literal Y,Z,W rows, forms
their exact polynomial divided differences, and reduces the
full pair ring by x1 squared-u*x1+z. It checks all three identities
(7), the entire E0/E1/E2 decomposition, the full numerator support,
its evaluation at u_star, the exact quotient (19), and both
coefficients used in (24). Eight whole-expression residuals are
zero. Root's independent cfa5f9 reconstructs the same complete
numerator and top coefficients. These algebra checks supplement
the written polynomial-return, faithful-flatness and unit proofs;
they do not replace them with finite point samples.
Fresh83e9e7 separately reconstructs the entire h=0 formal H and
its formal H_V, the full A/B leading coefficients with unrestricted
lower jets, and the substitution in (22). Its five residuals are
zero and the formal-gradient degree is four. General's independent
408f14 also reconstructs the full pair identity and both numerator
coefficients, without reading this source before its hold.

The generic lemma (10),(18),(20) is necessary for the whole
all-X return, not a sufficient realization criterion. It imposes
conditions on a pair locus over the coefficient field, not a new
actual coordinate transformation. Diagonal pairs, u=0 via (11),
and the delta-zero vertical component have all been retained.
The only exclusion proved is the h=0 cubic excess case (23).
The h nonzero excess families and every lower-y case still require
their other genuine equations and actual return conditions.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. This source requires
separate full saved-source review before acceptance. No novelty,
recognition, unrestricted cancellation or general entry is claimed.
