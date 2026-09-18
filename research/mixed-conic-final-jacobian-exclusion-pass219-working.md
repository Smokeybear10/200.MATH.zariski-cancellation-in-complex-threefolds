# The remaining mixed conic forces a forbidden polynomial relation

Status: new restricted working exclusion. Under the supplied actual
mixed-quartic frame hypotheses and the established218 identities, no
normalized conic remains. The two next Jacobian coefficients force
finite-constant formulas. Those formulas make the original coordinates
algebraically dependent, which is impossible.

This is not arbitrary frame entry or unrestricted cancellation. All
coefficient-field changes below are calculations inside the retained
exact field, not newly asserted original polynomial coordinates.

## 1. Actual hypotheses and the completed lower identities

Assume the actual globally sliced frame
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(ZW-X^2Y^2).
\tag{1}
\]
The displayed initial ideal is the whole weighted evaluation kernel.
Assume the normalized case-II conic of
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md).
Its possible actual good-coordinate interchange is completed before
this argument, with all chart quantities rebuilt.
This covers both conic branches of217: branch II is already normalized.
The stated interchange makes every intercept at most quadratic in
branch I. On rebuilding its chart, branch I would again force the
nonzero cubic w coefficient given in217, contradicting that bound.
The rebuilt conic must therefore be in branch II.

Use the exact coefficient field L finite over C(h,r), with r=rho
and h=t/rho, and its commuting derivatives
D=partial_r at fixed h and partial_h at fixed r. Write
L0=ker(D). The field of joint constants is C. In particular r,h
are nonzero, but L0 is not presumed equal to C(h).
The [lower-potential proof218](mixed-conic-lower-potential-radial-restrictions-pass218-working.md)
and the independent [zero-M exclusion218](mixed-conic-zero-M-jacobian-exclusion-pass218-working.md)
give
\[
\begin{gathered}
C\in\mathbb C^*,\quad F,\delta,n_0\in L_0,\qquad
G=g_0+g_1h+g_2h^2,\quad g_i\in\mathbb C,\\
k=C/r+Fr+G,\quad
\alpha=r/C,\quad
b=(G_hr+2h\delta r^2)/C,\quad
M=hF_h-F-2h^2\delta\ne0,\quad
\epsilon=\delta_h,\\
c_0=\delta-F_{hh}/3+G_h^2/(4C)+\kappa,\qquad
\kappa\in\mathbb C .
\end{gathered}
\tag{2}
\]
Division by M below uses the actual exclusion, not an omission of
its zero-factor branch.

For complete reconstruction, the remaining coefficients are
\[
\begin{gathered}
c=2hr\delta_h+G_{hh}/2+h^2\delta^2r^3/C
                    +h\delta G_hr^2/C+c_0r,\\
A_*=\delta(hF_h-F)-h^2\delta^2,\qquad
B_*=\delta-F_{hh}/2-c_0,\\
n=A_*r-CB_*/r+CG_{hh}/(2r^2)+n_0,\\
R_0=F-hF_h-hG_h/r-C/r^2,\\
f=\frac r{2h}
\left\{R_0(b\delta+\delta_h)
 +(2Cb/r^3-G_h/r^2)c+bn_r+n_h/r\right\}.
\end{gathered}
\tag{3}
\]
All h and r derivatives in this note are the commuting new partials.
Only R0 is written using the evaluated old partial k_rho; its explicit
formula in (3) prevents a convention ambiguity.

The raw original coordinates are
\[
\begin{gathered}
\vartheta=\alpha\xi^2+b\xi+c,\quad
y=h\vartheta+\xi,\quad
w=\alpha\delta\xi^2+(b\delta+\delta_h)\xi+f,\\
z=-h^2w+\xi^2/r+(F_h+G_h/r)\xi+(F-C/r^2)\vartheta+n,\\
Y=y+hrX,\quad
Z=z+(h^2\vartheta+2h\xi+k)X+h^2rX^2,\quad
W=w+\vartheta X+rX^2 .
\end{gathered}
\tag{4}
\]
Here X is the actual first coordinate and is independent of L.
The actual scalar calibration from the literal selected partial is
\[
\det\frac{\partial(Y,Z,W)}{\partial(h,r,\xi)}
 =j=-a^3r/\xi_v\in L^*,\qquad a=EX .
\tag{5}
\]
All determinant entries fix X. Thus this identity is constant in
both independent polynomial variables X and xi over L.

## 2. Centered columns and the full coefficient formula

Center only the line parameter:
\[
s=\xi+\frac b{2\alpha}=\xi+G_h/2+h\delta r.
\tag{6}
\]
The change from (h,r,xi) to (h,r,s) has determinant one, including
derivatives of its field-dependent coefficients. Hence (5) remains
the same constant polynomial determinant. No ambient coordinate
change is used.

Let Q=(Y,Z,W) as a column and set
\[
\mathbf c=
\begin{pmatrix}h\\F+h^2(X-\delta)\\X+\delta\end{pmatrix},
\qquad
T_0=X+\kappa+2h\delta_h-F_{hh}/3.
\tag{7}
\]
Equations (2)--(4) give
\[
Q=A_2s^2+A_1s+A_0,\qquad
A_2=(r/C)\mathbf c,\quad A_1=\mathbf c_h,\quad
A_0=rT_0\mathbf c+(C/r)\mathbf u+\mathbf e_0 ,
\tag{8}
\]
where the two explicit remaining columns are
\[
\mathbf u=
\begin{pmatrix}
0\\
X-hF_{hhh}/12-3h\delta_h/2-\delta+F_{hh}/2\\
(F_{hhh}-6\delta_h)/(12h)
\end{pmatrix}
\tag{9}
\]
and
\[
\mathbf e_0=
\begin{pmatrix}
-g_1/2\\
g_0X+g_1hF_{hh}/4-g_1F_h/2
 +g_2h^2F_{hh}/2-g_2hF_h+g_2F-h(n_0)_h/2+n_0\\
g_2X-(g_1+2g_2h)F_{hh}/(4h)+(n_0)_h/(2h)
\end{pmatrix}.
\tag{10}
\]
These identities retain every constant term in the raw map. They
follow by substituting xi=s-b/(2 alpha) in (4), using (3), and
collecting powers of s. In particular (A0)_Y=rhT0-g1/2.

Write J_d for the coefficient of s^d in the determinant (5).
The complete coefficient rule is
\[
J_d=
\sum_{\substack{0\le i,l\le2,\ 1\le k\le2\\i+l+k-1=d}}
\det\bigl((A_i)_h,(A_l)_r,kA_k\bigr).
\tag{11}
\]
This is just multilinearity of the determinant. It makes explicit
all contributions, including those from the constant column.
Every positive-degree J_d must vanish by (5).

## 3. The cubic coefficient gives a complex integration constant

For d=3 the five contributions in (11) are
\[
\begin{aligned}
J_3={}&2\det((A_2)_h,(A_0)_r,A_2)
 +2\det((A_1)_h,(A_1)_r,A_2)
 +2\det((A_0)_h,(A_2)_r,A_2)\\
 &+\det((A_2)_h,(A_1)_r,A_1)
 +\det((A_1)_h,(A_2)_r,A_1).
\end{aligned}
\tag{12}
\]
Here (A1)_r=0 and (A2)_r=A2/r, so the second, third and fourth
terms vanish for the indicated reasons. Substituting (7)--(10)
in the two remaining terms gives
\[
J_3=\frac{M}{6Ch}
       \left(6h\delta_{hh}-F_{hhh}+6\delta_h\right).
\tag{13}
\]
Equations (7)--(12) are explicit entries and the full expansion
for checking this finite identity; it is not a degree-only guess.
Since M,C,h are nonzero, J3=0 yields
\[
(F_{hh}-6h\delta_h)_h=0,\qquad
F_{hh}-6h\delta_h=\lambda\in\mathbb C .
\tag{14}
\]
The last conclusion uses membership in L0 and the exact joint
constant field, not a rational-function assumption.
It also makes T0=X+kappa-lambda/3 independent of h.

## 4. The quadratic coefficient forces finite polynomial data

For d=2, equation (11), (A1)_r=0, and (A2)_r=A2/r leave
\[
J_2=\det((A_2)_h,(A_0)_r,A_1)
    +\det((A_0)_h,(A_2)_r,A_1)
    +2\det((A_1)_h,(A_0)_r,A_2).
\tag{15}
\]
Use (14) and its derivatives to replace derivatives of delta.
The complete result of (15) is
\[
\begin{aligned}
J_2=-\frac{M}{12Ch^3r}
\bigl[&
C(-h^2F_{hhhh}+2hF_{hhh}+2\lambda-2F_{hh})\\
&+r\{3g_1h^2F_{hhh}-3g_1hF_{hh}
       +6g_2h^3F_{hhh}
       -6h^2(n_0)_{hh}+6h(n_0)_h\}\bigr].
\end{aligned}
\tag{16}
\]
This expansion has no remaining X dependence. It follows from the
three displayed determinants, without dropping their constant-column
derivatives.

The bracket in (16) is U+rV with U,V in L0. Since J2=0 and M
is nonzero, radial differentiation first gives V=0 and then U=0.
Thus
\[
\begin{gathered}
h^2F_{hhhh}-2hF_{hhh}+2F_{hh}-2\lambda=0,\\
3g_1h^2F_{hhh}-3g_1hF_{hh}+6g_2h^3F_{hhh}
       -6h^2(n_0)_{hh}+6h(n_0)_h=0 .
\end{gathered}
\tag{17}
\]

Here is an exact integration of the first equation. Set
H=F_hh-lambda and H=hU1. Its equation becomes h^3(U1)_hh=0.
Hence (U1)_h is a joint constant, and subtracting that linear term
makes U1 a joint constant. Denote the two complex constants by nu
and mu. Integrating twice more in L0, and using (14), gives
\[
\begin{gathered}
F=f_0+f_1h+\lambda h^2/2+\mu h^3/6+\nu h^4/12,\\
\delta=d_0+\mu h/6+\nu h^2/12,\qquad
f_0,f_1,d_0,\mu,\nu\in\mathbb C .
\end{gathered}
\tag{18}
\]
All integrations can equivalently be checked by subtracting the
displayed primitives and testing their derivatives. No logarithmic
or algebraic branch has been silently discarded.

After (18), the second equation of (17) is
\[
h(n_0)_{hh}-(n_0)_h
 =-g_1\lambda/2+(g_1\nu/2+g_2\mu)h^2+2g_2\nu h^3.
\tag{19}
\]
Subtract the particular polynomial formed from the linear, cubic
and quartic terms below. For the difference q, (19) says
(q_h/h)_h=0. Consequently q=N0+N2 h^2 with complex constants.
The complete result is
\[
n_0=N_0+g_1\lambda h/2+N_2h^2
           +(g_1\nu/2+g_2\mu)h^3/3+g_2\nu h^4/4,
\qquad N_0,N_2\in\mathbb C .
\tag{20}
\]
This proves completeness of the finite-constant formulas in the
original exact field. They are not a polynomial ansatz.

## 5. Structural factorization and the forbidden ambient relation

Set T=X+kappa-lambda/3, and introduce three columns over C[X]:
\[
v_0=\begin{pmatrix}0\\f_0\\X+d_0\end{pmatrix},\qquad
v_1=\begin{pmatrix}1\\f_1\\\mu/6\end{pmatrix},\qquad
v_2=\begin{pmatrix}0\\X+\lambda/2-d_0\\\nu/12\end{pmatrix}.
\tag{21}
\]
By (18), c=v0+h v1+h^2 v2 and c_h=v1+2h v2.
Substituting (18)--(20) in the explicit columns (9)--(10) gives
u=v2 and
\[
\mathbf e=
\begin{pmatrix}
-g_1/2\\
g_0X+N_0-g_1f_1/2+g_2f_0\\
g_2X+N_2-g_1\mu/4-g_2\lambda/2
\end{pmatrix}
 \in\mathbb C[X]^3 .
\tag{22}
\]
In particular the h-dependent terms of e0 cancel; no coefficient
function has been removed by an unauthorized shear.
Define three elements of the localized parameter ring:
\[
\mathsf A=r(s^2/C+T),\qquad
\mathsf B=h\mathsf A+s,\qquad
\mathsf D=h^2\mathsf A+2hs+C/r .
\tag{23}
\]
Equations (8) and (21)--(22) are now the exact factorization
\[
\boxed{Q=\mathbf e+v_0\mathsf A+v_1\mathsf B+v_2\mathsf D},
\qquad
\boxed{\mathsf B^2-\mathsf A\mathsf D=-CT}.
\tag{24}
\]
The second identity expands to s^2-(C/r)A=-CT, so it is a
literal algebraic relation rather than a numerical observation.

Let V(X) be the matrix with columns v0,v1,v2. Its determinant is
\[
\Delta(X)=(X+d_0)(X+\lambda/2-d_0)-f_0\nu/12 .
\tag{25}
\]
This is monic of degree two in the independent original X, hence
nonzero. The matrix is invertible over K=C(X).
Therefore the three affine-linear functions
V(X)^{-1}(Q-e) are algebraically independent over K if Y,Z,W are.
But (24) identifies them with A,B,D, which satisfy the nonzero
quadratic polynomial B^2-AD+CT=0 over K. This contradicts
B=C[X,Y,Z,W].

For an explicit denominator-free version, put
\[
(U_0,U_1,U_2)^{\mathsf T}
   =\operatorname{adj}(V(X))(Q-\mathbf e).
\]
These are original polynomials. The forced relation is
\[
U_1^2-U_0U_2+CT\Delta(X)^2=0 .
\tag{26}
\]
It is a nonzero polynomial in four independent indeterminates:
over K the affine-linear substitution is invertible and the
quadratic B^2-AD+CT is nonzero. Thus clearing denominators has
not turned the contradiction into the zero polynomial.
This argument uses only an invertible generic linear map to exhibit
an algebraic relation; it asserts no polynomial inverse over C[X].

## 6. Conclusion and verification boundary

The normalized actual mixed conic is impossible. The complete218
inputs, the positive-degree scalar equations J3=J2=0, exact-field
integration and the structural relation suffice. It is unnecessary
to assume or solve the still-lower fourth-potential coefficients:
they could only impose additional conditions on an already impossible
actual chart.

Together with the actual conic reduction and line recognition217,
this removes the conic obstruction in that supplied full mixed
initial-kernel sector. The full cancellation conjecture still lacks
arbitrary frame entry and treatment of unrestricted initial kernels.
The supplied-frame result must not be substituted for that objective.

Root fresh inline f2703d reconstructed (13); 02a750 completed through
the original session23456 in2f00fb and gave (16). That session is
terminal, not pending. A separate raw finite-constant calculation
a4b142 gave zero for the remaining full determinant coefficients.
Independent generic-function calculations reconstructed both (13)
and (16), and independent raw expansions verified all of (24),
including the nonzero determinant (25). The structural proof above
explains those zeros instead of treating a symbolic zero as a proof
of the exact-field integration.

No saved checker has executed this note at authoring time. No218
or earlier frozen source or packet was changed. This is a working
proof with AI reconstruction, not formal verification, human expert
review, novelty clearance, a submission, or a solution of the full
conjecture.
