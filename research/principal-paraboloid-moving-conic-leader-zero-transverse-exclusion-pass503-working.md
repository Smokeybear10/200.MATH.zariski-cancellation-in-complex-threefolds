# A moving conic leader cannot have zero transverse linear slope

Working bounded exclusion: retain the FULL actual q=0 nonlinear-conic
hypotheses of496. Write its linear moving-frame row as
\(V=v_1P+V_0\). Then
\[
\boxed{a_t\ne0\quad\Longrightarrow\quad (v_1)_s=b_s-pa\ne0.}
\tag{1}
\]
The proof uses the complete moving connection and actual complex
normalizations, followed by original scalar coefficients. It covers
the zero constant-H case, zero constant roots, and repeated moving
roots without discarding them. It does not exclude the remaining
moving-a, nonzero-transverse-slope case or recognize the full conic
sector.

## 1. Actual hypotheses and the exact q=0 reduction

Retain every assumption of
[496](principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md),
including its entire actual264/296/327/494 inputs. Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad O=L[P],\quad P=\sigma,\quad NP=\rho\in L^*,\\
O=L[y,z_0,w_{\rm int}]=L[y,\sigma,\theta],\quad
\operatorname{Frac}A=L(P)=\mathbb C(y,z_0,w_{\rm int}),\\
\theta=aP^2+bP+c,\quad a(1+ma)\ne0,\quad
m=k_s=pt+d,\quad p\in\mathbb C^*,\ d\in\mathbb C,\\
J(X,P)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
             =-a_0^4/\rho\in L^*.
\end{gathered}
\tag{2}
\]
The original slice, literal selected partial, both returns, full
genuine moving H and Q levels and their unit minors are retained.
There is no unit assumption on a0 in A and no replacement of rho
by one. The exact commuting coefficient partials have joint
constant field C.

Let \(F_0=\ker_L\partial_s\), finite over C(t), with exact
t-derivative constants C. Primes refer to this derivative.496 gives
\[
\begin{gathered}
k=ms+f,\qquad
n=p^2s^2/4+(pf'/2-h)s+n_0,\qquad f,h,n_0\in F_0,\\
a\in F_0^*,\quad y=-p\theta/2+\lambda P+r,
\quad f''''=6ah'',\\
A_c=(ph-mh')/(2p),\quad B_c=-f''/4+mf'''/(12p),\\
\lambda=A_ca+B_c,\qquad
r=A_cb+(-paA_c/2+pB_c/2+h'/2)s+r_0,
\quad r_0\in F_0.
\end{gathered}
\tag{3}
\]
Neither coefficient field is assumed rational. The letter h here
is a coefficient of n, not the third level.

Suppose for contradiction that
\[
a'\ne0,\qquad (v_1)_s=b_s-pa=0.
\tag{4}
\]
The multiplier494 remains nonzero; in this boundary it equals
\(ma'/(2p)\). No zero multiplier is being admitted.

## 2. The complete moving connection first forces h to be affine

Use exactly the frame and polynomial rows of496:
\[
\begin{aligned}
U&=Z+2dY/p=P^2+uP+U_0,\\
V&=-2Y/p-aU=v_1P+V_0,\\
T&=W+2(X+h'/p)Y/p+f'''U/(6p)=w_1P+T_0.
\end{aligned}
\tag{5}
\]
Here \(u=ps+u_F\), with \(u_F\in F_0[X]\),
\(v_1\in F_0[X]\) by (4), and
\(w_1\in F_0[X]\) has exact X degree two and leading coefficient
\(2/p\). In particular w1 is not the zero polynomial; no assertion
that it is an actual unit is made.

The ENTIRE scalar and the integrated cubic coefficient496 are
\[
\begin{aligned}
J&=\frac p2\det(dU,dV+a'U\,dt,dT+(h''/p)V\,dt),\\
T_0&=\frac p2w_1s+\frac{(w_1)_t}{a'}v_1
                    +\frac{h''}{2pa'}v_1^2+C_0,
\qquad C_0\in F_0[X].
\end{aligned}
\tag{6}
\]
Both hold at fixed original X; all moving-coefficient corrections
remain in the first line.

For this calculation abbreviate \(v=v_1,w=w_1\) and put
\[
\xi=P+u/2,\qquad
\alpha=\frac{h''}{2pa'},\quad \beta=\frac{w_t}{a'}.
\tag{7}
\]
This is only a horizontal change over L(X), with determinant one
in (t,s,P) while X is held fixed. It is not an ambient coordinate
or an assertion that xi lies in A. In particular no statement
\(N\xi=\rho\) for the original extension of N is used.
After absorbing the element \(-wu_F/2\) into a new C in F0[X],
the complete rows take the form
\[
U=\xi^2+\overline U,\qquad
V=v\xi+\overline V,\qquad
T=w\xi+\alpha v^2+\beta v+C.
\tag{8}
\]
All s derivatives of v,w,alpha,beta,C vanish. Define
\[
\Lambda=2\alpha v+\beta,\qquad
M=\alpha'v^2+\beta'v+C'+2a'\alpha\overline V.
\tag{9}
\]
Writing coefficient t derivatives at fixed s,X, the corrected
matrix in (6), now in (t,s,xi), is EXACTLY
\[
\begin{pmatrix}
\overline U_t&\overline U_s&2\xi\\
a'\xi^2+v_t\xi+\overline V_t+a'\overline U
                      &\overline V_s&v\\
a'\Lambda\xi+\Lambda v_t+M&0&w
\end{pmatrix}.
\tag{10}
\]
The identities \(w_t=a'\beta\) and \(h''/p=2a'\alpha\) explain
both terms in the last row.

Before the factor p/2, its complete xi-squared coefficient is
\[
-a'(2\Lambda\overline V_s+w\overline U_s)=0.
\tag{11}
\]
If \(\overline V_s=0\), this gives \(\overline U_s=0\), and
the entire s column in (10) vanishes. That contradicts (2).
Thus \(\overline V_s\ne0\). Substitute
\(\overline U_s=-2\Lambda\overline V_s/w\) in the COMPLETE
linear-xi coefficient. It becomes
\[
-2\overline V_s\left(M+\frac{a'\Lambda^2v}{w}\right)=0.
\tag{12}
\]
These divisions occur only in L(X), where the nonzero polynomial w
is invertible. No value of X is specialized in (11),(12).
The right side of \(M=-a'\Lambda^2v/w\) is in F0(X).
Differentiating it in s therefore gives
\(2a'\alpha\overline V_s=0\). The proved nonzero factors force
\[
\boxed{h''=0,\qquad f''''=0.}
\tag{13}
\]
The second assertion uses (3). This did not divide by h'', v,
\(A_c\), or a root of w. Consequently h is complex affine and f
is complex cubic in t, by successive subtraction in the exact F0.

## 3. Actual normalization remains valid for nonconstant a

We now use only complex polynomial maps of the fully read
[426](general-coupling-normalization-obstruction-pass426-working.md).
They are the maps also used in499, but the following transport
explicitly does NOT assume that a is constant.

First set \(\tau=d/p\) and take
\[
X_1=X,\quad Y_1=Y+\tau X^2,\quad
Z_1=Z+2\tau Y+\tau^2X^2,\quad W_1=pW.
\tag{14}
\]
Then \(t_1=t+\tau\), \(s_1=ps\), and
\(k_1=t_1s_1+F(t_1)\), with F a complex cubic or lower-degree
polynomial. Write \(F=c_3t_1^3+c_2t_1^2+c_1t_1+c_0\), retaining
all zero coefficients. Next take
\[
X_2=X_1,\quad Y_2=Y_1,\quad Z_2=Z_1-c_0X_1,
\quad W_2=W_1+c_3Z_1+c_2Y_1+c_1X_1^2.
\tag{15}
\]
The old Z1, not Z2, occurs in W2. The new parameters satisfy
\(t_2=t_1\), \(s_2=s_1+c_3t_1^2+c_2t_1+c_1\), \(k_2=t_2s_2\).

The first-potential function h remains complex affine. To verify
this without assuming a constant conic leader, for the general
shear \(W^*=W+B_mY+C_mZ\), with complex constants Bm,Cm, direct
potential transport gives
\[
\begin{gathered}
s^*=s+B_mt+C_mt^2,\quad f^*=f-m(B_mt+C_mt^2),\quad
n^*=n-mC_mk,\\
h^*=h-\frac{pmB_m}{2}+dmC_m,
\end{gathered}
\tag{16}
\]
where all old expressions are pulled back before substituting s.
The last expression is affine in t when h is affine. The preceding
time shift and W scaling divide h by p and translate its argument,
also preserving that property. A Z-linear shift changes no
s-linear coefficient of n.

In the resulting k=ts frame write \(h=h_1t+H\), with h1,H complex.
Put \(x=h_1/2\) and take
\[
X_*=X_2+x,\qquad Y_*=Y_2,\qquad Z_*=Z_2,
\qquad W_*=W_2+2xY_2.
\tag{17}
\]
Here \(s_*=s_2+2xt_2\), \(t_*=t_2\), \(k_*=t_*s_*\).
The direct first-potential identity before substituting s2 is
\(n_*=n_2+3xs_2t_2+3x^2t_2^2\); hence \(h_*=h-2xt_2=H\).
That identity holds for arbitrary y,theta and thus for moving a.

For an explicit polynomial inverse of the entire composite, first
set \(X=X_*-x\), and then recover
\[
\begin{aligned}
Y&=Y_*-\tau X^2,\\
Z&=Z_*+c_0X-2\tau Y-\tau^2X^2,\\
W&=\{W_*-2xY_*-c_3(Z_*+c_0X)-c_2Y_*-c_1X^2\}/p.
\end{aligned}
\tag{18}
\]
Both orders are polynomial inverses, dividing only by complex p.
The leading relation is preserved exactly.426's selected-partial
transport preserves the nonzero N, because its extra W partial has
shift at most three. It preserves both actual returns and the full
initial kernel, not just the leading relation's membership.

There is also an explicit check of the hypotheses (4). In pullback
notation the composite gives
\[
\begin{aligned}
a_*&=pa,\\
b_*&=pb+c_2+2c_3t_1+2x+4xt_1pa,\\
s_*&=ps+c_3t_1^2+c_2t_1+c_1+2xt_1,
\qquad P_*=P-2xt_1.
\end{aligned}
\tag{19}
\]
Since \(a_s=0\), these imply
\((b_*)_{s_*}-a_*=b_s-pa=0\) and
\((a_*)_{t_*}=pa'\ne0\). The new coupling slope is one.
The bad-row determinant and coefficient-parameter determinant are
both p. Also \(N_*=N\), \(NP_*=\rho\) and \(a_{0,*}=a_0\).
Thus the calibrated scalar remains the nonzero value in (2), with
the original global slice retained. No replacement by X/a0 occurs.

Drop stars and rename the exact lower coefficient functions. The
normalized data are
\[
\begin{gathered}
m=t,\quad k=ts,\quad h=H\in\mathbb C,\quad
a\in F_0^*,\ a'\ne0,\quad \delta=1+at\ne0,\\
b=as+b_0,\quad \lambda=aH/2,\quad
r=aHs/4+Hb_0/2+r_0,\\
n=s^2/4-Hs+n_0,
\qquad b_0,r_0,n_0\in F_0.
\end{gathered}
\tag{20}
\]
Reapplication of496 to this actual frame supplies these identities.
It does not make a or any lower F0 function rational.

## 4. Complete normalized rows and the remaining centered scalar

Let
\[
K=(2r_0+n_0')/t\in F_0,\qquad
w=2X(X+\lambda)-K,\qquad v=b_0-2\delta(X+\lambda),
\quad F=\ell+Hc-sr.
\tag{21}
\]
K is unrelated to the coupling notation in501 and may vanish.
The full normalized literal map used below is
\[
\begin{aligned}
\theta&=aP^2+(as+b_0)P+c,\qquad y=-\theta/2+\lambda P+r,\\
w_{\rm int}&=\{H\theta-2\lambda P^2
                     -(2r+s\lambda+n_0')P+\ell-sr\}/t,\\
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+sP+t\theta+n+(2tP+ts)X+t^2X^2,\\
W&=w_{\rm int}+\theta X+sX^2.
\end{aligned}
\tag{22}
\]
All c,ell and their derivatives are present here.

Now U=Z and T=W+2XY are actual polynomial coordinates, while
\(V=-2Y-aU\) remains only a moving coefficient-field row. Their
complete constant-P row is
\[
T_0=F/t+2rX+sX^2+2tX^3.
\tag{23}
\]
The cubic-X term is retained.496's cubic scalar coefficient, with
\(a'\ne0\), \(v_s=0\) and \(h''=0\), gives \((T_0)_s=w/2\).
Since \(r_s=\lambda/2\), (23) is equivalent to
\[
F=-tKs/2+tL_0,\qquad L_0\in F_0,
\quad\ell=-tKs/2+tL_0-Hc+sr.
\tag{24}
\]
This integration uses no rationality and no division by K or H.

Use the horizontal parameter
\(\xi=P+s/2+t(X+\lambda)\), again at fixed X with determinant one.
Then U,V,T have the form
\[
U=\xi^2+\overline U,\qquad V=v\xi+\overline V,
\qquad T=w\xi+\overline T,
\tag{25}
\]
where the complete relevant expressions are
\[
\begin{aligned}
\overline U={}&-Hs+Ht b_0+2tr_0+n_0-2t^2\lambda X-t^2\lambda^2,\\
u={}&s+2t(X+\lambda),\\
\overline V={}&c-2r-2tX^2-a(\overline U+u^2/4)-vu/2,\\
\overline T={}&-4t\lambda X^2+
       (Hb_0+2r_0-2t\lambda^2+tK)X+L_0+tK\lambda,\\
\overline U_s={}&-H,\qquad
\overline V_s=X+c_s-b/2+aH,\qquad \overline T_s=0.
\end{aligned}
\tag{26}
\]
In particular \(\overline V_s\) is never the zero polynomial in X,
as its X coefficient is one.

The ENTIRE corrected scalar in these parameters is
\[
J=\frac12\det
\begin{pmatrix}
\overline U_t&-H&2\xi\\
a'\xi^2+v_t\xi+\overline V_t+a'\overline U
                         &\overline V_s&v\\
w_t\xi+\overline T_t&0&w
\end{pmatrix}.
\tag{27}
\]
It is still \(-a_0^4/\rho\), with no X or xi dependence. Its
quadratic-xi coefficient gives the polynomial identity
\[
\left(HX-\frac{K'}{a'}\right)\overline V_s=\frac H2 w.
\tag{28}
\]
No root of w has been specialized in obtaining this equation.

## 5. The entire H=0 boundary has zero scalar

Suppose H=0. Equation (28) and the nonzero polynomial
\(\overline V_s\) force \(K'=0\). In this case (26) reads
\[
\overline U=2tr_0+n_0,\qquad
\overline T=(2r_0+tK)X+L_0.
\tag{29}
\]
The complete determinant (27), with c still arbitrary, is
\[
J=\frac{\overline V_s}{2}
              (\overline U_t w-2\xi\overline T_t).
\tag{30}
\]
Its linear-xi coefficient makes \(\overline T_t=0\). The full
polynomial in (29) then gives \(2r_0'+K=0\), \(L_0'=0\).
Using \(n_0'=tK-2r_0\), one obtains
\(\overline U_t=t(2r_0'+K)=0\). Thus (30) is identically zero,
contradicting the nonzero calibration. No condition on c_s or
\(\overline V_s\) beyond its proved nonvanishing was added.

## 6. H nonzero leaves two exact coefficient alternatives

Now suppose \(H\ne0\). The polynomial \(HX-K'/a'\) is nonzero
and belongs to F0[X]. Differentiating (28) in s shows that
\(\overline V_{ss}=0\). Hence
\[
\begin{gathered}
\overline V_s=X+C_1,\qquad C_1\in F_0,\\
c=as^2/4+(b_0/2-aH+C_1)s+c_0^{\rm low},
\qquad c_0^{\rm low}\in F_0.
\end{gathered}
\tag{31}
\]
The lower function \(c_0^{\rm low}\) is not the complex map
constant c0 used earlier. Comparison of the linear and constant X
coefficients in (28) gives
\[
\frac{K'}{a'}=HC_1-\frac{aH^2}{2},\qquad
K=2C_1^2-aHC_1.
\tag{32}
\]
No division by K, K' or C1 occurs. Differentiate the second identity
and use the first. The resulting factorization is
\[
(4C_1-aH)(C_1'-Ha'/2)=0.
\tag{33}
\]
Because F0 is a field, the two alternatives below are exhaustive.

## 7. The constant-root alternative contradicts the full scalar

If \(C_1'=Ha'/2\), exact constant-field integration gives
\[
C_1=Ha/2+C_*,\quad C_*\in\mathbb C,
\qquad K=HaC_*+2C_*^2.
\tag{34}
\]
Cstar may be zero. The polynomial w factors as
\(w=2(X-C_*)(X+C_*+\lambda)\), so at the COMPLEX value
\(X=C_*\) both w and its fixed-X t derivative vanish.
Specialize ONLY the polynomial matrix (27) at this value.
None of the earlier expressions dividing w is specialized.
The complete result is
\[
J\big|_{X=C_*}
 =-\frac{\overline T_t|_{X=C_*}}2
              \{(4C_*+Ha)\xi+Hv(C_*)\}.
\tag{35}
\]
The coefficient \(4C_*+Ha\) cannot vanish as a field element:
its derivative would be \(Ha'\ne0\). Thus independence of xi
forces \(\overline T_t|_{X=C_*}=0\). Equation (35) then gives
zero for the entire specialized scalar, contrary to (2).
This argument does not promote any generic invariant to a coordinate,
and does not require a simple root or a nonzero Cstar.

## 8. The repeated-moving-root alternative has incompatible coefficients

The other factor in (33) gives
\[
C_1=aH/4,\qquad K=-a^2H^2/8.
\tag{36}
\]
In particular \(w=2(X+aH/4)^2\), whose root moves with t.
No specialization at that moving root is needed.
Use the full ORIGINAL normalized rows (22), substituting (20),
(24), (31) and (36), and retaining every lower function. For
compactness put
\[
\mathcal D=7H^2a^2+2H^2aa't+16r_0'.
\tag{37}
\]
Exact expansion of that complete determinant gives
\[
[X^2P]J=-\frac{\mathcal D}{8},\qquad
\partial_s\bigl([X^2P^0]J\bigr)
             =-\frac{\mathcal D+12H^2a'}{16}.
\tag{38}
\]
The symbol \([X^2P^0]\) means the simultaneous X-squared,
constant-P coefficient, which is still a function of t,s.
All normalized lower coefficients \(b_0,r_0,n_0,L_0,c_0^{\rm low}\)
remain arbitrary elements of F0 subject only to the displayed
identities. In differentiating the rows one uses
\(n_0'=tK-2r_0\) and its exact t derivative. Terms involving
these lower coefficients cancel in the indicated difference;
none is set to zero.

Both coefficients on the left of (38) vanish: they come from a
positive power of X in the calibrated scalar. Therefore their
combination gives
\[
0=\partial_s([X^2P^0]J)-\frac12[X^2P]J
                         =-\frac34H^2a',
\tag{39}
\]
which is impossible because H and a' are nonzero. This does NOT
differentiate the possibly moving coefficient-field value of J:
it differentiates a positive-X coefficient already known to be zero.

Sections5,7,8 exhaust every case under (4). This proves (1).

## 9. Verification and scope

The complete held496 source, full current426 and full499 source
were read before reusing the normalization pattern. The extension
to moving a is proved explicitly in (16),(19), not inferred from
499's constant-a statement. Fresh unsaved133574 reconstructs the
two pre-normalization scalar coefficients (11),(12), including the
zero s-column alternative. Fresh5edf43 checks both orders of the
full composite actual inverse, the leading relation, the row
determinant, and the two arbitrary-coefficient h/n transports.

Fresh6f8e57 reconstructs the complete normalized literal determinant,
including both branches of (33). A separate ordinary-function
differentiation64e11e confirms both coefficients in (38), their
entire difference (39), and the full H-zero determinant (30).
Independent outline reconstruction8e5501,19b7ce,a71940 checks the
same coefficient chain, complete centered rows, actual normalization
and terminal factorizations. The written source requires a separate
complete saved-source review.

The conclusion excludes only \(a_t\ne0,(v_1)_s=0\) in the specified
q=0 conic sector. It neither excludes \(a_t\ne0,(v_1)_s\ne0\) nor
asserts that this remaining case occurs. It makes no delta-zero,
arbitrary projected-curve, general entry or unrestricted cancellation
claim. All coefficient-field and horizontal changes were kept
distinct from the explicit complex ambient automorphisms. All saved
checkers remain frozen: none was executed, imported, compiled or
rerun. No earlier source or canonical file was edited.
