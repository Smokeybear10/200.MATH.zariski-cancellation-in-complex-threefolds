# A nonzero normalized offset is impossible for a moving conic leader

Working exclusion: under the FULL actual conic hypotheses of496,
there is no branch with
\[
a_t\ne0,\qquad (v_1)_s=b_s-pa\ne0,\qquad h''=0
\]
whose licensed503 normalization has \(h=H\in\mathbb C^*\).
The proof uses the entire original scalar, including its moving
row connection. Both values of an auxiliary determinant are
treated. In the nonzero case, the lower scalar forces the genuine
unit multiplier494 to vanish.

This is the H-nonzero counterpart of507. No h''-zero conclusion is
inferred for the remaining general moving-frame problem, and no
result about arbitrary conic entry or cancellation is asserted.

## 1. Retained actual hypotheses and the exact normalized frame

Retain every assumption of
[496](principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md),
including the full actual264/296/327 hypotheses, the genuine
moving H,Q levels, both actual returns, and the nonzero multiplier
of494. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\quad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
The original global slice and selected partial remain literal.
There is no assumption that a0 or rho is an actual unit.
Exact coefficient derivatives commute, with joint constants C.

Write \(F_0=\ker_L\partial_s\), finite over C(t), with exact
t-derivative constants C. Before normalization,496 gives
\(m=pt+d_0\), \(p\in\mathbb C^*\), \(d_0\in\mathbb C\), and
\(f''''=6ah''\). The EXTRA assumption h''=0 makes h complex affine
and f complex cubic or lower degree, by exact-field subtraction.

Use the actual complex normalization of
[503 Section3](principal-paraboloid-moving-conic-leader-zero-transverse-exclusion-pass503-working.md),
also written with its full inverse in
[507 Section1](principal-paraboloid-moving-conic-zero-normalized-offset-exclusion-pass507-working.md).
It first applies the time shift \(\tau=d_0/p\) and W scaling:
\[
(X,Y,Z,W)\longmapsto
(X,Y+\tau X^2,Z+2\tau Y+\tau^2X^2,pW).
\tag{2}
\]
For the remaining complex polynomial
\(F(t_1)=\sum_{i=0}^3c_it_1^i\), it next applies
\[
(X_1,Y_1,Z_1,W_1)\longmapsto
(X_1,Y_1,Z_1-c_0X_1,W_1+c_3Z_1+c_2Y_1+c_1X_1^2).
\tag{3}
\]
The old Z1 occurs in the W row. Finally, when the resulting h is
h1*t+H, the paired map \(X_*=X_2+h_1/2\),
\(W_*=W_2+h_1Y_2\) makes h constant. All coefficients of these
maps are complex. Their polynomial inverses and the selected-
partial/return licenses are the full426/503 ones, not inverses
over a coefficient field.

Their general transport, before imposing either zero or nonzero
transverse slope, is
\[
a_*=pa,\quad (a_*)_{t_*}=pa',\quad
(b_*)_{s_*}-a_*=b_s-pa,\quad N_*=N,\quad NP_*=\rho.
\tag{4}
\]
The row and coefficient-parameter determinants are both p;
a0 and the original slice are retained. Thus the nonzero slope
assumptions and calibration survive. No use is made of503's
zero-transverse-slope conclusion in this nonzero-slope case.

Drop stars and retain the ADDED boundary \(H\in\mathbb C^*\).
Set \(\mathfrak a=a'\), to distinguish this coefficient from the
actual kernel ring A. The complete normalized data are
\[
\begin{gathered}
m=t,\quad k=ts,\quad h=H\in\mathbb C^*,\quad
a\in F_0^*,\quad\mathfrak a\ne0,\quad\delta=1+ta\ne0,\\
z=b-as,\quad z_s\ne0,\quad\lambda=aH/2,\quad
n=s^2/4-Hs+n_0,\\
r=Hz/2+aHs/4+r_0,\qquad r_0,n_0\in F_0,\\
\theta=aP^2+(as+z)P+c,\quad
y=-\theta/2+\lambda P+r,\quad c\in L.
\end{gathered}
\tag{5}
\]
The symbol z denotes this coefficient-field element, not an
intrinsic generator of264.

## 2. Complete literal rows and moving connection

Use the exact separating basis(t,z), and write S=s in that basis.
Then \(S_z=1/z_s\ne0\), its z-constant field is F0, and
\[
J_{t,z,P}(X)=-a_0^4S_z/\rho\in L^*.
\tag{6}
\]
No claim L=F0(z) or F0=C(t) is made. A prime still denotes the
exact derivative on F0; it is unchanged by this coefficient basis.
The value in (6) can depend on t and z.

The ENTIRE original rows are
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+SP+t\theta+n+(2tP+tS)X+t^2X^2,\\
W&=w_{\rm int}+\theta X+SX^2,\\
tw_{\rm int}&=H\theta-2\lambda P^2
 -(2r+S\lambda+n_0')P+\ell-Sr.
\end{aligned}
\tag{7}
\]
All lower c,ell and their moving derivatives remain. Set
\[
U=Z,\qquad V=-2Y-aZ,\qquad T=W+2XY.
\tag{8}
\]
U,T are actual rows, whereas V is generally only a moving
coefficient-field row. The exact496 connection is
\[
J=\frac12\det(dU,dV+\mathfrak a U\,dt,dT).
\tag{9}
\]
It would be incorrect to replace this by the determinant of the
three uncorrected differentials.

At fixed X center only horizontally:
\[
\xi=P+S/2+t(X+\lambda),\qquad q=S-tz.
\tag{10}
\]
The parameter determinant is one, so (6) remains the full scalar.
This is not an assertion that xi is an actual coordinate or that
its original N speed equals rho.

Define coefficient functions in F0 by
\[
\begin{gathered}
K=(2r_0+n_0')/t,\quad
v_0=-aH\delta,\quad v_{10}=2Hat\delta,\\
u_0=2tr_0+n_0-a^2H^2t^2/4,\quad
B=2r_0-a^2H^2t/2+tK,\quad \eta=K'/\mathfrak a.
\end{gathered}
\tag{11}
\]
The full centered rows have the form
\[
\begin{aligned}
U&=\xi^2+\overline U,&
\overline U&=-Hq-aHt^2X+u_0,\\
V&=v\xi+\overline V,&
v&=z-2\delta X+v_0,\\
\overline V&=at^2X^2+(q+v_{10})X+R,&
w&=2X^2+aHX-K,\\
T&=w\xi+\overline T,&
\overline T&=-2aHtX^2+(Hz+B)X-\eta z+C.
\end{aligned}
\tag{12}
\]
Here C belongs to F0. R is the ENTIRE constant-X coefficient of
the moving intercept, explicitly
\[
R=c-2r_0-a(2tr_0+n_0)+\frac{H^2a^2t\delta}{2}
 +HaS-\frac{3Hat z}{2}-Hz-\frac{aS^2}{4}-\frac{Sz}{2}.
\tag{13}
\]
Initially R can be any element of L consistent with these data.
The constant-X part of T in (12) uses exactly the integrated
cubic scalar coefficient496(29). Before that integration it is
\((\ell+Hc-Sr)/t+KS/2+tK\lambda\). Thus the retained ell is
reconstructible from
\[
\ell=t(-\eta z+C-KS/2-tK\lambda)-Hc+Sr.
\tag{14}
\]
No lower function has been assigned a special value. The actual
uncentered T constant term contains 2tX^3; its centering, not its
deletion, gives (12).

## 3. Exact integration of the quadratic intrinsic coefficient

The full corrected matrix is
\[
\begin{pmatrix}
\overline U_t&\overline U_z&2\xi\\
\mathfrak a\xi^2+v_t\xi+\overline V_t+\mathfrak a\overline U
 &\xi+\overline V_z&v\\
w'\xi+\overline T_t&H X-\eta&w
\end{pmatrix},
\qquad w'=\mathfrak a(HX-\eta).
\tag{15}
\]
Its determinant times one half is (6). In particular the xi in
the middle row's z entry is present.

Put
\[
A_1=aH^2/2+\eta,\qquad
M_1=B'-Hv_0'-2\delta'\eta.
\tag{16}
\]
The COMPLETE xi-squared coefficient, compared in X and integrated
in z by subtraction, is exactly
\[
\begin{aligned}
A_1q-HR&=\mathcal R_2:=\frac{M_1}{\mathfrak a}z+k_1,\\
-\frac{HK}{2}q+\eta R&=\mathcal R_3:=
 -\frac{\eta'}{2\mathfrak a}z^2
 +\frac{C'+\eta v_0'}{\mathfrak a}z+k_0,
\qquad k_0,k_1\in F_0.
\end{aligned}
\tag{17}
\]
The integration constants are existing differences with zero
z derivative. No rational antiderivative or algebraic closure is
used. These equations also retain eta=0.

Define the auxiliary determinant
\[
\Delta=\eta^2+\frac{aH^2\eta}{2}-\frac{H^2K}{2}\in F_0.
\tag{18}
\]
It is distinct from the nonzero conic coefficient delta. Eliminating
R from (17), without dividing by Delta, gives
\[
\Delta q=H\mathcal R_3+\eta\mathcal R_2.
\tag{19}
\]
The element z is transcendental over F0: otherwise its nonzero
s derivative would contradict characteristic-zero algebraicity.
Polynomial comparison in z with coefficients in F0 is therefore
licensed.

## 4. The zero determinant branch has an actual complex root

Suppose Delta=0. The z-squared coefficient in (19) is
\(-H\eta'/(2\mathfrak a)\), so eta'=0 and eta is complex.
The definition of eta gives \(K'=\eta a'\); subtraction, followed
by (18), yields
\[
K=a\eta+2\eta^2/H^2,\qquad \eta\in\mathbb C.
\tag{20}
\]
Thus the COMPLEX number \(X_c=\eta/H\) satisfies
\(w(X_c)=w'(X_c)=0\). Also
\(\overline T_z(X_c)=HX_c-\eta=0\), so its value is in F0.
No moving or rational root is being declared an actual coordinate.

Evaluate the ENTIRE polynomial matrix (15) at this fixed complex
X. Its last row is \((\overline T_t(X_c),0,0)\), hence
\[
J(X_c)=\frac{\overline T_t(X_c)}2
 \{\overline U_z(X_c)v(X_c)
                     -2\xi(\xi+\overline V_z(X_c))\}.
\tag{21}
\]
Its xi-squared coefficient forces \(\overline T_t(X_c)=0\), and
then its full value is zero, contradicting (6). The argument
includes eta=0 and Xc=0. No denominator involving w was specialized.

## 5. A quadratic z term is impossible when Delta is nonzero

Now Delta is nonzero. Equations (17),(19) imply directly
\[
q=q_2z^2+q_1z+q_0,\qquad
R=r_2z^2+r_1z+R_0,\qquad q_i,r_i,R_0\in F_0,
\tag{22}
\]
with
\[
q_2=-\frac{H\eta'}{2\mathfrak a\Delta},\qquad
r_2=(aH/2+\eta/H)q_2.
\tag{23}
\]
No assertion L=F0(z) is needed. These are identities for the
existing q,R only.

Let \(J_0=[\xi^0]J\). Direct expansion of the ENTIRE matrix (15),
with every lower coefficient in (22) and its derivative retained,
and using (23) together with its exact t derivative, gives
\[
\begin{aligned}
[X^2z^3]J_0&=-q_2^2(\mathfrak a H^2-2\eta'),\\
[Xz^3]J_0&=-\frac H2
 \{(\mathfrak a H^2-2\eta')a q_2^2-Hq_2'\}.
\end{aligned}
\tag{24}
\]
All these coefficients vanish: they have positive X degree in
the scalar (6). There is no assertion that its X-constant value
has zero z derivative.

If q2 is nonzero, (24) forces \(\eta'=H^2a'/2\) and \(q_2'=0\).
Exact integration in F0 gives
\[
\eta=H^2a/2+e_0,\quad
K=H^2a^2/4+e_0a+k_*,\quad e_0,k_*\in\mathbb C.
\tag{25}
\]
The constants can vanish. Equation (23) becomes
\(q_2=-H^3/(4\Delta)\), so Delta'=0. But (18),(25) give
\[
\Delta=\frac{3H^4a^2}{8}+H^2e_0a+e_0^2-\frac{H^2k_*}{2},
\qquad
\Delta'=(3H^4a/4+H^2e_0)a'.
\tag{26}
\]
Its vanishing would make a complex, contradicting a' nonzero.
Consequently
\[
q_2=0,\quad \eta'=0,\quad
\eta=e\in\mathbb C,\quad K=ea+k_*,\quad k_*\in\mathbb C,
\quad r_2=0.
\tag{27}
\]
The case q2=0 has not been discarded by division. Eta'=0 follows
from (23) with its already nonzero H,a',Delta factors.

## 6. The remaining affine z terms annihilate the genuine multiplier

Now \(q=q_1z+q_0\) and \(R=r_1z+R_0\). The next COMPLETE scalar
coefficients, before assigning the lower functions, are
\[
[Xz^2]J_0=H^2q_1'/2,\qquad
[Xz\xi]J=H(r_1'-3H a'q_1/2)\quad\text{after }q_1'=0.
\tag{28}
\]
Thus
\[
q_1\in\mathbb C,\qquad
r_1=3Hq_1a/2+c_1,\qquad c_1\in\mathbb C.
\tag{29}
\]
Both complex constants can be zero. The functions q0 and R0
remain arbitrary elements of F0 at this stage.

For an explicit reconstruction of the final coefficient, the
xi-squared identities (17) now give
\[
\begin{aligned}
B'&=Hv_0'+2e\delta'
       +a'\{q_1(e-aH^2)-Hc_1\},\\
C'&=-ev_0'+a'\{-HKq_1/2+er_1\},\\
v_0'&=-H(a'\delta+a\delta'),\qquad \delta'=a+ta'.
\end{aligned}
\tag{30}
\]
The definitions (11), with K'=ea', give the independent literal
coefficient identity
\[
u_0'=tB'-a'et^2+H^2aa't^2/2.
\tag{31}
\]
These formulas retain the moving derivatives of every coefficient.
Substituting only (27)--(31) into the FULL matrix (15) yields
\[
\boxed{[X^2z]J_0=
 \frac{H^2}{2}(t+q_1)\{a'(t+q_1)+2a\}=0.}
\tag{32}
\]
The lower q0,R0 and their derivatives cancel in this particular
coefficient; they were not set to zero. The same coefficient is
obtained directly from the complete original rows (7).

Since q=S-tz, equations (22),(27),(29) give
\[
S=(t+q_1)z+q_0,\qquad S_z=t+q_1\ne0,\qquad
z_s=\frac1{t+q_1}.
\tag{33}
\]
The nonzero derivative is part of the exact basis license, not an
extra root exclusion. Equation (32) therefore implies
\(a'(t+q_1)+2a=0\).

The FULL unit multiplier494, retained in496(7), is
\[
\kappa=\frac t2(a'-2a^2+2ab_s)
       =ta\left(z_s+\frac{a'}{2a}\right)
       =\frac{t\{a'(t+q_1)+2a\}}{2(t+q_1)}.
\tag{34}
\]
It must belong to \(L^*\), whereas (32)--(34) give kappa=0.
This contradiction excludes the nonzero-Delta branch and completes
the stated normalized H-nonzero exclusion.

## 7. Independent reconstruction and exact remaining scope

The full496 and actual503 normalization were read and revalidated
before this argument. The source does not apply the zero-slope
conclusion of503 to the present nonzero-slope case. The common
actual normalization is valid before either slope specialization.

Fresh ce88fb reconstructs the entire corrected determinant with
arbitrary lower coefficient jets and verifies both coefficients
(24). Fresh827d47 reconstructs (30)--(32). Fresh ecca32 instead
starts with the ORIGINAL Y,Z,W, keeps the exact n0 derivative
constraint, and independently verifies the full coefficient (32).

Jet's independent eda06c, completed954ce6, rebuilds every original
and centered row and both derivative identities underlying (17).
Fresh5d29c7 independently checks (24) and the whole fixed-complex-
root determinant (21). Fresh2c258b verifies both gates (28), the
literal identity (31), and the entire terminal coefficient (32),
with arbitrary lower q0,R0 retained. All corresponding residuals
are zero. Root's independent57cc20 reconstructs the full affine-z
matrix, both preceding terminal gates, the xi-squared identities
(30), and (31),(32). Independent5f5c4b reconstructs both coefficients
(24), the complete complex-root scalar (21), and the exact Delta
derivative contradiction, again with zero residuals. Full
saved-source review is recorded separately.

This proves only the added h''=0, normalized H-nonzero boundary
exclusion under the FULL496 actual hypotheses, with a' and
transverse slope nonzero. Together with507 it eliminates the
normalized h''-zero moving-a sector, but no claim about the
h''-nonzero sector is imported here. Other conic boundaries,
arbitrary actual entry, and general cancellation remain outside
this statement. No historical novelty, human expert review or
proof-assistant certification is claimed. All saved checkers remain
frozen: none was executed, imported, compiled or rerun. No earlier
mathematical source or canonical file was edited.
