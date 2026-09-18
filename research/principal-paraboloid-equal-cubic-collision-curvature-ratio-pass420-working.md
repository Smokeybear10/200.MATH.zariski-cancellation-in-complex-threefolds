# An all-X collision gate for the equal-cubic profile

Working necessary lemma in the complete actual264 chart, with k=s
and n_ss nonzero. In the surviving profile (r,m,d)=(1,2,3), assume
the directional coefficient beta is nonzero. Then the curvature
ratio (beta^2+2n_ss*delta^2)/beta^2 belongs to a set of five complex
constants. This is a coefficient-field restriction, not by itself
an exclusion of the cubic profile or an original-coordinate result.

The proof uses a finite divided-difference elimination. Its exceptional
leading-coefficient and repeated-root cases are included explicitly.
It does not use a Bezout existence assertion or assume that the exact
coefficient field is rational.

## 1. Actual assumptions and the cubic intrinsic parameter

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
and the necessary frontier in
[417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\quad E=\partial_{u_0},
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
0\ne N=[u_0^4]\partial_Z|_{A_0},\quad
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\\
Nv_0=1,\quad a_0=EX\in L^*,\quad
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\\
\operatorname{Frac}A_0=L(v_0)=\mathbb C(y,z,w),\quad
J_{t,s,v_0}(X)=-a_0^4\in L^*,\quad k=s,\quad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The full genuine potentials, their evaluated unit ideals and every
coefficient of the actual scalar remain imposed. The proof below
does not replace these assumptions by a formal parametrized curve.

Use the exact definitions of
[407](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md):
\[
\begin{gathered}
\lambda=\frac{[v_0^3]y}{[v_0^3]\sigma},\quad
\mu=\frac{[v_0^3]\theta}{[v_0^3]\sigma},\quad
a=n_t,\quad \nu=n_s,\quad C=\ell_s+\nu^2,\\
\delta=\lambda-\nu,\quad \beta=n_{ts}+e\mu,\quad
\mathcal K=\beta^2+2e\delta^2,\quad
j=\delta a-\ell_t-C\mu,\\
u=y-\lambda\sigma,\quad h=\theta-\mu\sigma,\quad
R=2\delta u+\beta h+j.
\end{gathered}
\tag{2}
\]
The numerator defining lambda is zero if deg(y)<3. The present
profile and nonzero gates are
\[
\deg\sigma=\deg\theta=3,\quad
\max(\deg u,\deg h)=2,\quad \deg R=1,\quad
\delta\beta\mathcal K\ne0.
\tag{3}
\]
All intrinsic degrees are over L. Since R is affine in v0, put
x=R; then O=L[x]. The cancellation in R and delta*beta nonzero
force both u and h to have degree two. Write
\[
h=H x^2+L_1x+h_c,\quad H\in L^*,\qquad
u=\frac{x-\beta h-j}{2\delta},\qquad p=\sigma\in L[x].
\tag{4}
\]
Here x,u,h are coefficient-field functions, not original polynomial
coordinates or a replacement for the actual global slice u0.

## 2. The shifted third level determines a compressed cubic

The full third-potential identity in407 is
\[
xp+q(u,h)=0,\qquad
q(u,h)=u^2+au+\frac e2h^2-Ch+\nu\ell-h_{\rm lev},
\tag{5}
\]
where h_lev is the actual third-potential level. In particular the
constant coefficient of q(u(x),h(x)) is zero. Introduce only for
the algebra below
\[
G=\delta a-\beta h_c-j,\qquad
F=-\beta G+2\delta^2(eh_c-C),\qquad K=\mathcal K.
\tag{6}
\]
Expanding (5) gives the complete cubic, not just its leading part:
\[
\boxed{
p(x)=-\frac{
Kx(Hx+L_1)^2-2\beta x(Hx+L_1)+x
       +2F(Hx+L_1)+2G}{4\delta^2}.}
\tag{7}
\]
For example, subtracting the constant term of q before division by
x is valid because that term is already zero by (5). If
p=p3*x^3+p2*x^2+p1*x+p0, the coefficients are
\[
\begin{aligned}
p_3&=-\frac{KH^2}{4\delta^2}\ne0,&
p_2&=-\frac{H(KL_1-\beta)}{2\delta^2},\\
p_1&=-\frac{KL_1^2-2\beta L_1+1+2FH}{4\delta^2},&
p_0&=-\frac{FL_1+G}{2\delta^2}.
\end{aligned}
\tag{8}
\]
No derivative or rationality of F,G,H,L1 is assumed.

## 3. Actual all-X generation and exact collision equations

The actual derivation E kills L and all intrinsic coefficients.
It preserves L[B], and differentiation of the original rows gives
\[
\sigma=\frac{EY}{a_0}-2tX,\qquad
\theta=\frac{EW}{a_0}-2sX,\qquad
y=Y-\sigma X-tX^2\quad\text{in }L[\mathcal B].
\tag{9}
\]
Whole return in (1) and the literal formulas therefore prove
\[
L[X,Y,Z,W]=L[\mathcal B]=L[X,x].
\tag{10}
\]
The reverse containment follows because every displayed actual row
has coefficients in L[x]. The variables X,x are independent over L:
X=a0*u0+c_X is transcendental over Frac(A0), whereas x is an affine
parameter for L(v0). This is the direct all-X argument of
[325, Section2](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
Consequently (10) survives every field extension L'/L and every
specialization X=X0 in L'. No coefficient function is thereby made
an original coordinate.

Holding X and the coefficient field fixed, the complete actual rows
in the parameter x are
\[
\begin{aligned}
Y={}&(X+\lambda)p+u+tX^2,\\
Z={}&p^2+(2t(X+\lambda)+\mu)p+2tu+h+n+sX+t^2X^2,\\
W={}&-2\lambda p^2+[\mu(X-\nu)-a]p-2pu
                         +(X-\nu)h+\ell+sX^2.
\end{aligned}
\tag{11}
\]
For two formal parameters x1,x2 use the polynomial divided difference
Df=(f(x1)-f(x2))/(x1-x2), defined also on the diagonal. Put
S=x1+x2 and T=x1*x2, and define
\[
\begin{aligned}
L_p&=p_3(S^2-T)+p_2S+p_1,\qquad L_h=HS+L_1,\\
P_+&=p_3(S^3-3ST)+p_2(S^2-2T)+p_1S+2p_0,\\
H_*&=H(S^2-2T)+L_1S,\\
\mathscr A(S,T)&=(P_++\mu)L_p+L_h,\\
\mathscr B(S,T)&=\delta P_+
                      +\frac{S-\beta H_*+2G}{2\delta}.
\end{aligned}
\tag{12}
\]
Thus Lp=Dp, Lh=Dh, P+=p(x1)+p(x2), and
Bscript=delta*P++u(x1)+u(x2)+a. The exact row differences are
\[
DY=(X+\lambda)L_p+Du,\qquad
DZ-2tDY=\mathscr A,\qquad
2\delta Du+\beta L_h=1.
\tag{13}
\]
If Lp is nonzero, set X0=-lambda-Du/Lp. At a common zero of
Ascript,Bscript the remaining difference is
\[
DW\big|_{X=X_0,\,\mathscr A=0}=-L_p\mathscr B=0.
\tag{14}
\]
To verify (14), use D(pu)=(P+*Du+(u(x1)+u(x2))*Lp)/2 in (11),
and then Lh=-(P++mu)*Lp. These are polynomial divided-difference
identities before any diagonal specialization.

Such a common zero with Lp nonzero is impossible over an algebraic
closure of L. Choose x1,x2 as the roots of Zeta^2-S*Zeta+T.
If they are distinct, all three specialized coordinates in (11)
agree, contradicting the polynomial inverse for x supplied by (10).
If the roots coincide, their divided differences are intrinsic
derivatives; (13),(14) make Y_x,Z_x,W_x all zero. Differentiating
that polynomial inverse would give 1=0. X0 is held fixed in this
derivative; it is not a moving-root differentiation.

The Lp=0 boundary is also explicit. A simultaneous zero of DY and
DZ would require Du=0 and Lh=0. This contradicts the last identity
in (13). In particular, a common zero of Ascript,Bscript with
Lh nonzero automatically has Lp nonzero, because Ascript at Lp=0
is Lh.

## 4. A zero-safe elimination polynomial has only one root

Expand (12) in the pair product T:
\[
\mathscr B=b_1(S)T+b_0(S),\quad
\mathscr A=a_2(S)T^2+a_1(S)T+a_0(S),\qquad
\mathscr E=a_2b_0^2-a_1b_0b_1+a_0b_1^2.
\tag{15}
\]
These formulas define the elimination polynomial completely. No
resultant theorem is required. Direct expansion of (8),(12) gives
\[
\begin{aligned}
b_1&=\frac{HK(3HS+4L_1)}{4\delta},\\
a_2&=-\frac{H^3K(4\beta-3HKS-4KL_1)}{16\delta^4},\\
a_2\big|_{b_1=0}&=-\frac{\beta H^3K}{4\delta^4}
                  =\frac{\beta H p_3}{\delta^2}\ne0.
\end{aligned}
\tag{16}
\]
Suppose Escript(S0)=0 and H*S0+L1 is nonzero. If b1(S0) is
nonzero, T0=-b0/b1 makes both Ascript and Bscript zero, by (15).
If b1(S0)=0, (16) and (15) force b0(S0)=0. Bscript is then
identically zero in T, while Ascript is a genuine quadratic.
It has a finite root over the algebraic closure. In either case
Lh is nonzero, so Lp is nonzero and Section3 gives a contradiction.
There is no root lost at the zero of the elimination leading
coefficient.

Put omega=HS+L1. Direct expansion of (15) yields
\[
\mathscr E(S)=-\frac{HK}{64\delta^6}\,\omega\,\mathcal Q(\omega),
\quad \deg\mathcal Q=5,\quad
[\omega^5]\mathcal Q=\beta K^2,\quad
[\omega^4]\mathcal Q=-K(3\beta^2-\beta KL_1+3K).
\tag{17}
\]
In particular Escript has exact degree six and leading coefficient
-beta*H^7*K^3/(64delta^6), which is nonzero. Every root must be
the single point omega=0 by the preceding argument. Factoring a
polynomial over the algebraic closure therefore proves
\[
\mathcal Q(\omega)=\beta K^2\omega^5,\qquad
L_1=\frac{3(\beta^2+K)}{\beta K}.
\tag{18}
\]
No assertion is needed about whether the forced root omega=0 itself
corresponds to a collision. Its role is only to contain every root
not already prohibited.

## 5. Coefficient ledger and a division-free final certificate

For a short expansion ledger define
\[
f=FH,\qquad z_*=(\delta^2\mu-G)H,\qquad
V_*=\delta^4H,\qquad k=K/\beta^2\ne0.
\tag{19}
\]
All are coefficient-field elements; f and V* are not the potential
functions or intrinsic variables. After the L1 equation in (18),
the next coefficient of the polynomial defined by (15),(17) is
\[
[\omega^3]\mathcal Q=
\frac{-12\beta^4-2\beta^2Kf-11\beta^2K
                +6\beta K^2z_*-12K^2}{\beta}.
\tag{20}
\]
Its vanishing fixes
\[
z_*=\frac{12\beta^4+2\beta^2Kf+11\beta^2K+12K^2}
                  {6\beta K^2}.
\tag{21}
\]
After this substitution the omega-squared coefficient is
\[
[\omega^2]\mathcal Q=-\frac{\beta^2}{k}
 (36V_*k^2+22fk^2+10fk-48k^3-41k^2-44k-12).
\tag{22}
\]
Thus V*=-(22fk^2+10fk-48k^3-41k^2-44k-12)/(36k^2).
No quantity other than an already nonzero beta or K has been divided
out in these coefficient comparisons.

With (18),(21),(22) imposed, the last two coefficients are
\[
[\omega]\mathcal Q=-\frac{\beta}{k^2}r_1,\qquad
[1]\mathcal Q=-\frac1{k^3}r_0,
\tag{23}
\]
where the explicit polynomials are
\[
\begin{aligned}
r_1={}&4f^2k^2-32fk^3-38fk^2-32fk
                 +33k^4+82k^3+120k^2+82k+33,\\
r_0={}&2(k+1)(10f^2k^2-32fk^3-35fk^2-32fk
                 +24k^4+55k^3+81k^2+55k+24).
\end{aligned}
\tag{24}
\]
Equations (15),(17) and (8),(12) are also a compact prescription
for checking every entry in this ledger without any elimination
software: expand in T first and then in omega.

Both r1 and r0 vanish. Put
\[
L_*=8k(4k^2+5k+4),\qquad
B_*=39k^4+100k^3+146k^2+100k+39.
\tag{25}
\]
The exact polynomial identity
\[
r_0-5(k+1)r_1=3(k+1)(L_*f-B_*)
\tag{26}
\]
first separates k=-1. Otherwise it gives L*f=B*, without dividing
by L*. Multiply r1 by L*^2 and replace each occurrence of L*f
by B*. Direct expansion gives
\[
L_*^2r_1=-12k^2(k+1)^4(k^2-4k+1)(5k^2+8k+5)
\quad\text{when }L_*f=B_*.
\tag{27}
\]
This substitution is a polynomial identity modulo (L*f-B*),
including L*=0. Since k is nonzero, (26),(27) prove
\[
\boxed{
\frac{\beta^2+2e\delta^2}{\beta^2}
\in\left\{-1,\ 2+\sqrt3,\ 2-\sqrt3,
                  \frac{-4+3i}{5},\frac{-4-3i}{5}\right\}
\subset\mathbb C^*.}
\tag{28}
\]
Indeed the corresponding polynomial splits over C, and L is a
field containing C. This is not a deduction that L is rational
or equal to a smaller coefficient field. The retained e,delta
nonzero also imply k is not one, consistently with (28).

## 6. Verification and limits

The complete writing guide and actual264 were freshly read in
324fcb/6e4af7/6bd954;407 in65d9f6/2ba789;325 in dee964;
and the complete417 in51806a before this note was written.
The proof of (10) is repeated here rather than inferred solely
from equality of the three intercept rings at X=0.

Fresh unsaved d065c1 reconstructed (7) from the entire shifted
third level and (14) from the literal W row, with zero residuals.
Fresh unsaved 913fe2 reconstructed the two coefficients in (16)
and (17) from the pair polynomials. Fresh unsaved 4264cf reconstructed
the compact elimination expression in (15), every coefficient
gate (18)--(24), and both exact final certificates (26),(27),
with zero residuals. These are finite algebra checks; the
field-extension, polynomial-inverse, repeated-root and zero-safe
elimination arguments are written separately above.

Only beta nonzero is addressed here. This note does not exclude
the cubic profile by itself, assert realizability of a root in
(28), classify the other five profiles of417, or make x an
original polynomial coordinate. No original-ring recognition,
arbitrary-chart entry, unrestricted cancellation, novelty,
human-expert verification or formal certification is claimed.
No saved checker was executed, imported, compiled or rerun by
this author, and no earlier source or canonical index was edited.
