# A quartic pair-unit restriction in the transverse cubic excess branch

Working necessary reduction: retain the FULL actual264/296/535
chart and the surviving noncomplex-T0, v1=0 family of555--557.
The complete divided-pair numerator U has degree at most four.
Its fourth coefficient separates two necessary branches. A nonzero
fourth coefficient fixes U to a single monomial and gives two
explicit possibilities for the linear theta coefficient. A zero
fourth coefficient forces an exact differential equation and an
existing eleventh-power identity in the coefficient field.

Both delta cases remain in the zero-fourth-coefficient branch.
In particular the implication proved here is delta=0 implies
U4=0, NOT its converse. This note neither excludes nor realizes
either branch and supplies no recognition or general chart entry.

## 1. Full actual input and the retained transverse family

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md).
In particular retain
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_{\mathcal A},\quad
Na_0=Nt=Ns=0,\quad Nv=1,\\
L=\operatorname{Frac}\ker_{\mathcal A}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
L[\mathcal A]=L[v]=L[y,\sigma,\theta],\\
\operatorname{Frac}\mathcal A=L(v)=\mathbb C(y,z_{\rm int},w),\quad
L[y,z_{\rm int},w]=L[v],\qquad m=k_s\notin\mathbb C.
\end{gathered}
\tag{1}
\]
Here z_int is the literal original Z-intercept. The original global
slice, selected literal partial, both returns, genuine moving levels
and full scalar are retained, not replaced by leading data.

Use the finite intrinsic normalization and family of
[555](principal-paraboloid-cubic-pair-unit-and-longitudinal-exclusion-pass555-working.md),
[556](principal-paraboloid-cubic-transverse-degree-profile-restriction-pass556-working.md)
and
[557](principal-paraboloid-cubic-transverse-conic-and-differential-restriction-pass557-working.md).
In the finite coefficient extension L'=L(rho), x is affine in v and
\[
\begin{gathered}
\sigma=x^2+c,\qquad Nx=\rho\in(L')^*,\\
\theta=ax^3+b_2x^2+dx+e,\qquad
y=rx^4+q_3x^3+y_2x^2+y_1x+y_0,\\
F_0=\ker_{L'}\partial_s,\qquad a,r\in F_0^*,\qquad
h=m_s=-4r/a^2\in F_0^*,\qquad m=hs+m_0,\quad m_0\in F_0,\\
p=m_t,\qquad p_s=h_t,\qquad T_0=2t+1/r\notin\mathbb C.
\end{gathered}
\tag{2}
\]
The coefficient partials are the exact commuting extensions from
C(t,s), extended to fix x. Moving-center and moving-scale terms
are therefore retained. F0 is finite over C(t), not assumed
rational, and its t constants are C. No square root or intrinsic
parameter is promoted to an actual polynomial coordinate.

Write w_i=[x^i]w. The retained necessary identities are
\[
\begin{gathered}
w_5=0,\quad w_4\ne0,\quad (w_4)_s=0,\qquad
2q_3+a(p+hb_2)=0,\\
h_t=-a^2h^2/8\ne0,\qquad r=2h_t/h,\\
w_4=rb_2/2-p_t/(2h),\qquad
(b_2)_s=h_{tt}/(hr)=h_{tt}/(2h_t).
\end{gathered}
\tag{3}
\]
All other conclusions and unused equations of the input sources
remain required. No restriction here presumes a nonzero p, b2,
d or any other lower coefficient.

For reference, with mathfrak n denoting the potential n, the
complete original rows and second potential are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=2ty+\sigma^2+k_t\sigma+m\theta+\mathfrak n
                                  +(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2\sigma+k_t)y-\mathcal F(\sigma,\theta),\\
\mathcal F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2
                              +\mathfrak n_tP+\mathfrak n_sV,\\
J_{t,s,x}(Y,Z,W)&=-a_0^4/\rho\in(L')^*.
\end{aligned}
\tag{4}
\]
The calibrated scalar is independent of x and X, but need not be
constant under either coefficient partial.

## 2. The complete pair expression and its unit license

Put k1=k_t and k2=k_tt. For independent x1,x2 define
u=x1+x2 and z=x1*x2. The symbol u in the rest of this source is
the pair sum, not the original global slice. Define
\[
\begin{aligned}
S_\sigma&=u^2-2z+2c,\\
S_\theta&=a(u^3-3uz)+b_2(u^2-2z)+du+2e,\\
S_y&=r(u^4-4u^2z+2z^2)+q_3(u^3-3uz)
                         +y_2(u^2-2z)+y_1u+2y_0,\\
Y_d&=r(u^3-2uz)+q_3(u^2-z)+y_2u+y_1,\\
\overline F_P&=k_2S_\sigma/2+pS_\theta/2+\mathfrak n_t,\qquad
\overline F_V=pS_\sigma/2+hS_\theta/2+\mathfrak n_s,\\
\mathcal E(u,z)&=S_y+\overline F_P
                        -(S_\sigma+k_1)\overline F_V/m.
\end{aligned}
\tag{5}
\]
These are the entire symmetric expressions, including all lower
coefficients of y, theta and the genuine potentials. Put
\[
\begin{gathered}
D(u)=2u+ma,\quad q_0=2c+k_1,\\
N(u)=u^3+ma u^2+(q_0+mb_2)u+md,\qquad P(u,z)=N-Dz,\\
u_*=-ma/2\ne0,\qquad
\delta=N(u_*)=m\{d-a(q_0+mb_2)/2+m^2a^3/8\}.
\end{gathered}
\tag{6}
\]
Here P is a pair-locus polynomial, not an intrinsic coordinate.

The complete555 unit argument applies without any new entry
assumption. Briefly, the actual all-X return gives
\[
L'[X,Y,Z,W]=L'[X,x].
\tag{7}
\]
The polynomial inverse for x makes the divided differences of
the three whole rows generate the unit ideal. With the SAME X
in both rows, their exact identities are
\[
\begin{aligned}
Y^{[1]}&=Y_d+uX,\qquad Z^{[1]}-2tY^{[1]}=P,\\
mW^{[1]}\big|_{X=-Y_d/u}+u\mathcal E
  &=-P\{Y_d/u+\overline F_V/m\}.
\end{aligned}
\tag{8}
\]
The last line holds before setting P to zero. Divided differences
are polynomials; x1-x2 is never inverted. On u nonzero the ordered
pair lift of L'[u,u inverse,z] is the finite free rank-two algebra
obtained by adjoining x1 with x1 squared-u*x1+z=0. It is faithfully
flat even on the diagonal. Elimination of X in (8) and faithful
descent therefore prove
\[
\boxed{\mathcal E\in
 \big(L'[u,u^{-1},z]/(N-Dz)\big)^*.}
\tag{9}
\]
No moving coefficient-field root is used as an actual coordinate
specialization. On the omitted u=0 boundary, the same whole
divided-difference argument retains555's necessary condition
\[
\boxed{a y_1-dq_3\ne0.}
\tag{10}
\]
Indeed at u=0 the two relevant differences are d-az and
y1-q3*z; if they both vanished, so would all three whole row
differences. The monic ordered-pair lift also includes this case.

## 3. Entire numerator, cancellation of its top two coefficients

For an explicit complete support formula, set
\[
S_0=u^2+2c,\quad T_c=au^3+b_2u^2+du+2e,\quad
v_c=3au+2b_2,\quad Q_0=S_0+k_1,\quad
V_0=pS_0/2+hT_c/2+\mathfrak n_s.
\tag{11}
\]
The temporary Tc is not T0 from (2). Write
E=E0+E1*z+E2*z squared, where the FULL coefficients are
\[
\begin{aligned}
E_0={}&ru^4+q_3u^3+y_2u^2+y_1u+2y_0
          +k_2S_0/2+pT_c/2+\mathfrak n_t-Q_0V_0/m,\\
E_1={}&-4ru^2-3q_3u-2y_2-k_2-pv_c/2
               +\{Q_0(p+hv_c/2)+2V_0\}/m,\\
E_2={}&2r-(2p+hv_c)/m.
\end{aligned}
\tag{12}
\]
Define the whole polynomial numerator, without any truncation,
\[
\mathcal U(u)=E_0D^2+E_1DN+E_2N^2,
\qquad \mathcal E(u,N/D)=\mathcal U/D^2.
\tag{13}
\]
Before the transverse substitutions, direct expansion of (12)
has degree at most seven and gives
\[
\begin{aligned}
[u^7]\mathcal U&=0,\\
[u^6]\mathcal U&=-(a^2h+4r)/2,\\
[u^5]\mathcal U&=-am(a^2h+4r)-a(p+hb_2)-2q_3.
\end{aligned}
\tag{14}
\]
Thus (2),(3) cancel all coefficients above degree four, with no
condition on the unused lower functions. The next entire
coefficient and the evaluation identities are
\[
\boxed{\begin{gathered}
\deg_u\mathcal U\le4,\qquad
U_4:=[u^4]\mathcal U
       =-\frac m2(2a^2mr+a^2p-4b_2r),\\
E_2(u_*)=\frac{4U_4}{a^2m^2},\qquad
\mathcal U(u_*)=E_2(u_*)\delta^2.
\end{gathered}}
\tag{15}
\]
The last identity follows from D(u*)=0 even when delta is zero.
Equations (12)--(15) concern the complete E and U, not selected
pieces of the scalar or independently assigned potentials.

If delta is nonzero, N and D are coprime and the pair ring in (9)
is exactly L'[u,u inverse,D inverse]. Its units, and the fact that
U is a polynomial, give
\[
\mathcal U=\lambda u^iD^j,\qquad
\lambda\in(L')^*,\quad i,j\ge0,\quad i+j\le4.
\tag{16}
\]
The two polynomials u,D are nonassociate because u* is nonzero.
If delta is zero, the vertical component in (9) must instead be
retained, as done below. No conclusion (16) is imported into
that case.

## 4. Nonzero U4 forces two precise linear-theta choices

Suppose U4 is nonzero. Then E2(u*) is nonzero by (15). If delta
were zero, the quotient u=u* of the pair ring would be L'[z],
and E would be a quadratic polynomial with nonzero quadratic
coefficient there. Such a polynomial is not a unit, contradicting
(9). Hence delta is nonzero.

Now U(u*) is nonzero. Formula (16) forces j=0. The exact degree
of U is four, so i=4 and lambda=U4. Consequently
\[
\boxed{\mathcal U=U_4u^4,\qquad
              \delta^2=a^6m^6/64.}
\tag{17}
\]
For the second equation evaluate the first at u*, use (15), and
cancel the proven nonzero U4. Since u*=-ma/2, the resulting
identity is u* to the fourth=4delta squared/(a squared*m squared).

Substitute the exact delta from (6). The difference of squares
factors as
\[
\delta^2-\frac{a^6m^6}{64}
=m^2\left(d-\frac{a(q_0+mb_2)}2\right)
     \left(d-\frac{a(q_0+mb_2)}2+\frac{a^3m^2}{4}\right).
\tag{18}
\]
The coefficient field is a domain and m is nonzero. Thus the two
precise alternatives in this branch are
\[
\boxed{d=\frac{a(2c+k_t+mb_2)}2
\quad\text{or}\quad
d=\frac{a(2c+k_t+mb_2)}2-\frac{a^3m^2}{4}.}
\tag{19}
\]
No individual lower coefficient in either alternative is presumed
nonzero. These are necessary alternatives, not realization data.

## 5. Zero U4 gives an exact differential restriction

Suppose U4=0. Because a,m,r are nonzero, (15) is equivalent to
\[
\boxed{b_2=\frac{a^2m}{2}+\frac{a^2p}{4r}.}
\tag{20}
\]
Differentiate genuinely in s. Using a_s=r_s=0 and p_s=h_t gives
\[
(b_2)_s=\frac{a^2h}{2}+\frac{a^2h_t}{4r}
                         =-\frac{5h_t}{h}.
\tag{21}
\]
The last equality uses h=-4r/a squared and r=2h_t/h from the
retained full H gates. Compare with (3). Since h and h_t are
nonzero, this proves
\[
\boxed{hh_{tt}+10h_t^2=0.}
\tag{22}
\]
There is no division by p or any unused lower coefficient.

For completeness, the exact integration requires no rationality
of F0. The t derivative of h to the tenth times h_t is
h to the ninth times the left side of (22), hence zero. Its s
derivative is zero because h_s=0 and the partials commute. Exact
joint constants in L' are C, so h to the tenth times h_t is a
nonzero complex constant. Subtracting a complex multiple of t
from h to the eleventh then gives
\[
\boxed{h^{11}=c_1t+c_0,\qquad
             c_1\in\mathbb C^*,\quad c_0\in\mathbb C.}
\tag{23}
\]
Here c1=11h to the tenth times h_t. This is an identity for the
existing h in F0, not permission to choose a new root or make an
ambient coordinate change.

## 6. Both delta cases remain when U4 is zero

Substituting (20) into the entire E2 in (12) yields the useful
polynomial identity
\[
\boxed{E_2(u)=\frac{6r}{am}D(u).}
\tag{24}
\]
In particular E2(u*)=0, but this does NOT force delta=0.

If delta is nonzero, the exact pair ring and unit law (16) apply.
The degree of U is now at most three, and U(u*)=0 by (15).
Since U is nonzero by the unit condition, one obtains precisely
the additional necessary restrictions
\[
\boxed{\mathcal U=\lambda u^iD^j,\qquad
\lambda\in(L')^*,\quad i\ge0,\quad j\ge1,\quad i+j\le3.}
\tag{25}
\]
No assertion is made here that any particular exponent pair can
occur in an actual chart.

If delta is zero, exact polynomial division gives
\[
N=DM,\qquad
M(u)=u^2/2+ma u/4+(q_0+mb_2)/2-m^2a^2/8.
\tag{26}
\]
The pair ring is the union of the graph z=M(u) and the vertical
line u=u*, with their common point retained. As in555, it is the
fiber product of L'[u,u inverse] and L'[z] over their value at
that point. Its unit condition is therefore equivalent to both
restrictions being units. The vertical restriction must be a
nonzero constant; (24) has already removed its quadratic term.
The remaining vertical requirements and graph restriction are
\[
\boxed{\begin{gathered}
E_1(u_*)=0,\qquad E_0(u_*)\ne0,\\
\mathcal E(u,M(u))=\lambda u^i,\qquad
\lambda\in(L')^*,\qquad i\in\{0,1\}.
\end{gathered}}
\tag{27}
\]
To justify the sharper graph exponent, (13),(26) give the entire
identity U=D squared*E(u,M(u)). Since deg U<=3 and D has degree
one, the nonzero graph polynomial has degree at most one.
The graph units in L'[u,u inverse] are scalar monomials, and this
expression is a polynomial, so i is zero or one. Its value at
u* automatically agrees with E0(u*) and is nonzero.

The original u=0 guard in fact removes i=0. This uses the COMPLETE
graph expression, not a leading approximation. Substitute (20),
delta=0 and the identities h=-4r/a squared and
q3=-a(p+hb2)/2 into (12). Direct expansion, before imposing
the vertical linear condition, gives the division-free identity
\[
4a\,[u]\mathcal E(u,M(u))-4(a y_1-dq_3)
                                 -a^2mE_1(u_*)=0.
\tag{28}
\]
Thus E1(u*)=0 gives
\[
[u]\mathcal E(u,M(u))
       =y_1-dq_3/a=\frac{a y_1-dq_3}{a}\ne0.
\tag{29}
\]
This coefficient identity retains c,e,k1,k2,p,mathfrak n_t,
mathfrak n_s,y1,y0 and every contribution to the graph constant.
Its last inequality is precisely (10), using a nonzero. Thus the
linear graph polynomial is not constant. Its unit condition forces
its constant coefficient to vanish and strengthens (27) to
\[
\boxed{\begin{gathered}
E_1(u_*)=0,\qquad
\mathcal E(u,M(u))=\lambda u,\qquad
\lambda=\frac{a y_1-dq_3}{a}\in(L')^*,\\
E_0(u_*)=\lambda u_*\ne0.
\end{gathered}}
\tag{30}
\]
The last line retains the original vertical nonzero condition; it
also follows from the graph value at the common point because
u* is nonzero. Equivalently the entire numerator is
\(\mathcal U=\lambda uD^2\). There is no contradiction claimed in (30).

Equations (20)--(30) retain both delta cases. In the full family,
delta=0 implies U4=0 by the vertical quadratic coefficient in
(15), but no converse has been proved. In every branch the
original u=0 condition (10) and all other actual hypotheses remain.

## 7. Verification and exact scope

The target was checked absent before creation. Complete held555
was freshly read through EOF in53801c+f36821, complete556 in
8b735d+8ad352, and complete557 in c3fbed+d77754 at its held hash
b7767894ef7915ca4dcd3ee2ada71720be2a99d4cdd33bb4c546a1eb5bbd6c5b.
The source inputs are retained at their stated scopes; no earlier
recognition or arbitrary-entry endpoint is strengthened.

Fresh unsaved d67f54 reconstructed the COMPLETE E and numerator
(13) with unrestricted lower y, theta and potential coefficients.
It verified (15) and the root evaluation with all residuals zero.
Fresh f22c47 separately checked the three generic top coefficients
(14). Fresh7dd0c1 checked the exact difference of the two b2_s
expressions, the first-integral derivative, the factorization (18),
and the full E2 identity (24), again with zero residuals.
Fresh79459d rebuilt the entire delta-zero graph after the safe
E1 elimination, checked its exact slope (29), and verified the
graph/vertical value compatibility, all with zero residuals.
Fresh97ec17 directly checked the full division-free identity (28)
without eliminating y2. Root's
independent412f5c reconstructs the whole E/U and these gates;
General's715829 independently supplied the quartic numerator
reduction. Root's separate ed687a and8ca051 independently check
the graph-slope strengthening, and Jet's58928c independently
checks the division-free identity (28). These checks supplement
the polynomial-return and unit
arguments, not finite point samples in place of them.

This is a necessary pair-unit and differential restriction only.
Neither branch is excluded or realized. The full scalar, unused
genuine H coefficients, actual returns, finite coefficient extension,
diagonal pairs and critical points remain in force. No rational
coefficient field, ambient intrinsic parameter, or deletion of the
delta-zero vertical component is assumed.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. Separate full saved-
source review remains required after author hold. No novelty,
recognition, general chart entry or unrestricted cancellation
claim is made.
