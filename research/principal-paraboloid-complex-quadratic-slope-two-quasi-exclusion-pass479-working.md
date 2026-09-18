# Complex quadratic W-slope: an actual two-quasi exclusion

Working result: retain the full actual264 hypotheses, variable
coupling \(m=k_s\notin\mathbb C\), a birational projected line,
and nonconstant sigma. The quadratic coefficient \(\omega\) of
the intrinsic W-intercept cannot belong to \(\mathbb C\).

The proof uses both alternatives of the field two-quasi theorem.
Its rank-one alternative is not promoted to an actual coordinate
over \(\mathbb C[X]\). Instead its generic quadratic invariant
forces coefficient identities, and the full original calibrated
determinant then has a nonconstant complex-X factor. This is a
scoped exclusion, not an unrestricted cancellation theorem.

## 1. Actual entry and the accepted coefficient input

Retain the entire actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and minor units of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the birational projected-line hypothesis of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\qquad Na_0=Nt=Ns=0,\qquad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta]=L[y,z,w_{\rm int}],\quad Nv=1,\qquad
K=L(v)=\mathbb C(y,z,w_{\rm int}).
\end{gathered}
\tag{1}
\]
The commuting exact coefficient partials have joint constants
\(\mathbb C\). The original global slice is retained, including
\(X=a_0u+x_0\) with its original intercept \(x_0\in A\).

By325, \(P=\sigma\) is an affine intrinsic parameter, with
\(NP=\rho\in L^*\). Write
\[
y=\lambda P+r,\qquad \theta=\mu P+h,\qquad
w_{\rm int}=\omega P^2+bP+c,\qquad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{2}
\]
Here the coefficient derivatives fix P and agree with the original
partials on L. Neither \(\rho=1\) nor \(P=u\) is assumed.

Suppose \(\omega\in\mathbb C\). The actual map
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W-\omega Z
\tag{3}
\]
has a polynomial inverse and is licensed by the complete transport
of [426](general-coupling-normalization-obstruction-pass426-working.md).
It gives \(t_*=t,\ s_*=s-\omega t^2,\ k_*=k,\ m_*=m\),
\(P_*=P,\ \lambda_*=\lambda,\ \omega_*=0\), and
\(\mu_*=\mu-2\omega t\). It retains the full initial ideal,
both actual returns and scalar. The literal identity
\(\partial_{Z_*}=\partial_Z+\omega\partial_W\), together with
the retained shift-at-most-three bound for \(\partial_W\),
retains the selected N. All ensuing formulas use the normalized
coefficient parameters; drop the stars.

The complex-lambda case is excluded by the completely read
[477](principal-paraboloid-variable-coupling-complex-slope-exclusion-pass477-working.md).
Thus \(\lambda\notin\mathbb C\). The completely read and independently
accepted
[480](principal-paraboloid-variable-coupling-zero-quadratic-slope-reduction-pass480-working.md)
supplies
\[
\begin{gathered}
\mathcal D=\partial_t+\mu\partial_s,\qquad
\beta=\mathcal Dm\ne0,\quad \kappa=\mathcal D\mu\ne0,\qquad
2d\lambda+\beta\,d\mu=0,\\
m=At+Bs+C,\qquad
k=-2\lambda_0t^2+Ats+\frac B2s^2+Cs+Dt+E_0,\\
\lambda=\lambda_0-\frac A2\mu-\frac B4\mu^2,\qquad
A,B,C,D,E_0,\lambda_0\in\mathbb C,\quad (A,B)\ne(0,0).
\end{gathered}
\tag{4}
\]
In particular mu is noncomplex. This note uses480's full scalar
exclusion of \(\kappa=0\), not merely its high-jet calculation.
The exact field L has not been identified with a rational field.

The normalized actual rows, before any further change, are
\[
\begin{aligned}
Y&=(X+\lambda)P+r+tX^2,\\
Z&=P^2+(2t\lambda+k_t+m\mu+2tX)P\\
 &\hspace{14mm}+2tr+mh+n+kX+t^2X^2,\\
W&=(b+\mu X)P+c+hX+sX^2.
\end{aligned}
\tag{5}
\]
All lower coefficient functions remain in these rows.

## 2. The actual derivation and both field-theorem alternatives

Extend N to \(\overline N\) on \(A[u]\) by
\(\overline Nu=0\), and define the actual derivation
\[
\Delta=a_0\overline N-(\overline NX)E.
\tag{6}
\]
It fixes X. On \(\mathcal B_{a_0}=A_{a_0}[X]\), it is
\(a_0N\) acting on the coefficients while fixing X, hence is
locally nilpotent. Its restriction to \(\mathcal B\) is therefore
also locally nilpotent. It kills L, and, with
\(\tau=a_0\rho\in L^*\), its exact velocities are
\[
\begin{aligned}
\Delta Y&=(X+\lambda)\tau,&
\Delta W&=(b+\mu X)\tau,\\
\Delta Z&=(2P+2t\lambda+k_t+m\mu+2tX)\tau,&
\Delta^2Z&=2\tau^2\ne0,\quad \Delta^3Z=0.
\end{aligned}
\tag{7}
\]
In particular \(\Delta^2Y=\Delta^2W=0\).

Localize the ACTUAL polynomial ring at the nonzero elements of
\(\mathbb C[X]\):
\[
\mathcal R=\mathbb C(X)[Y,W,Z],\qquad k_X=\mathbb C(X).
\]
Take a gcd g of the three coefficients of \(\Delta\) in this UFD.
Since \(g\mid\Delta g\), local nilpotence forces \(\Delta g=0\):
otherwise additive \(\Delta\)-degree of \(g\cdot(\Delta g/g)\)
contradicts \(\deg_\Delta(\Delta g)=\deg_\Delta g-1\).
Thus \(D_0=\Delta/g\) is an irreducible nonzero LND of \(\mathcal R\),
with the same kernel and velocity ratios. Its relevant second and
third vanishing conditions in (7) remain true.

[Dasgupta--Gupta, Theorem4.1](https://arxiv.org/html/1701.03635v1)
states the field two-quasi alternatives used here: either a
\(k_X\)-linear form in Y,W is invariant, or there is a coordinate
system \((\mathcal V,Y,W)\) with \(D_0\mathcal V=0\) and
\(D_0Y,D_0W\in k_X[\mathcal V]\). Both alternatives are retained.
The theorem concerns an irreducible LND over a characteristic-zero
field, exactly as arranged above.

First, even independently of the theorem's labelling, the ratio
\[
\frac{\Delta W}{\Delta Y}
 =\frac{b+\mu X}{\lambda+X}
\tag{8}
\]
cannot belong to \(k_X\). Indeed clear a complex polynomial
denominator of such a rational function and evaluate the resulting
identity at \(X=-\lambda\) in L. Since lambda is noncomplex,
it is transcendental over the algebraically closed field
\(\mathbb C\); the cleared denominator does not vanish there.
It follows that \(b=\mu\lambda\), and then (8) equals mu.
The intersection \(L\cap\mathbb C(X)=\mathbb C\) makes mu complex,
contradicting (4). This includes a zero numerator. Since
\(\Delta Y\ne0\), an invariant nonzero linear form in Y,W would
give exactly the forbidden ratio (8). Therefore alternative I
is impossible.

## 3. The rank-one alternative gives a quadratic generic invariant

Retain alternative II, without claiming that its coordinate descends
to a coordinate over \(\mathbb C[X]\). Because its coordinate
system retains Y,W, the one-variable polynomial automorphism over
\(k_X[Y,W]\) has the form
\[
\mathcal V=\mathfrak a(X)Z+\mathcal F(X,Y,W),
\qquad \mathfrak a\in k_X^*,\quad
\mathcal F\in k_X[Y,W].
\tag{9}
\]
For completeness, the degrees in Z of this automorphism and its
inverse multiply to one, and the leading coefficient is a unit of
\(k_X[Y,W]\), hence belongs to \(k_X^*\).

Write \(D_0Y=f(\mathcal V)\), \(D_0W=g_1(\mathcal V)\), where
f is nonzero. Their ratio is nonconstant in \(\mathcal V\), by (8).
The independent coordinates \(\mathcal V,Y,W\), together with
\(D_0^3Z=0\), give
\[
0=f^3\mathcal F_{YYY}
+3f^2g_1\mathcal F_{YYW}
+3fg_1^2\mathcal F_{YWW}
+g_1^3\mathcal F_{WWW}.
\tag{10}
\]
After dividing by \(f^3\), the nonconstant rational function
\(g_1/f\in k_X(\mathcal V)\) is transcendental over \(k_X\).
Independence of \(\mathcal V,Y,W\) therefore forces all four
third partials in (10) to vanish. Characteristic zero gives
\(\deg_{Y,W}\mathcal F\le2\).

The quadratic part is nonzero, because the P-squared coefficient
of Z in (5) is one. If its coefficients are denoted by
\(q_{20},q_{11},q_{02}\in k_X\), invariance of \(\mathcal V\)
means that its polynomial expression in P is constant. Its
P-squared coefficient is
\[
\mathfrak a
+q_{20}(X+\lambda)^2
+q_{11}(X+\lambda)(b+\mu X)
+q_{02}(b+\mu X)^2=0.
\tag{11}
\]
Here \(\mathfrak a\ne0\), while none of the three q-coefficients
is assumed individually nonzero.

## 4. Exact rationality of b, not of the coefficient field

We prove \(b\in\mathbb C[\mu]\) from (11) and the polynomial
formula for lambda in (4). This assertion concerns only b;
no rationality of L follows or is used.

If \(q_{02}=0\), first suppose \(q_{11}=0\).
Equation (11) would make \(X+\lambda\) algebraic over \(k_X\),
contrary to algebraic independence of X and the noncomplex lambda.
If \(q_{11}\ne0\), solve (11) for b:
\[
b=-\mu X-\frac{q_{20}}{q_{11}}(X+\lambda)
       -\frac{\mathfrak a}{q_{11}(X+\lambda)}.
\tag{12}
\]
This puts b in \(L\cap\mathbb C(\mu)(X)=\mathbb C(\mu)\).
The intersection follows, for example, by taking the X derivative
that fixes L: constants of that derivative on
\(\mathbb C(\mu)(X)\) are \(\mathbb C(\mu)\).
Write b as a reduced complex rational function of mu.
Over an algebraic closure of \(k_X\), the nonconstant polynomial
\(\lambda(\mu)+X\) has a root. None of its roots is a root of
the complex denominator of b, since such a root would be complex
and would make X complex. Evaluating (11) at that root gives
\(\mathfrak a=0\), a contradiction. Thus
\[
q_{02}\ne0.
\tag{13}
\]

Choose a complex X value avoiding the finitely many coefficient
poles and zeros of \(q_{02}\). Equation (11) is then a monic
quadratic equation for b over \(\mathbb C[\mu]\), after division
by a nonzero complex constant. Consequently b is integral over
\(\mathbb C[\mu]\), and algebraic of degree at most two over
\(\mathbb C(\mu)\).

If b is not rational over \(\mathbb C(\mu)\), choose a distinct
conjugate \(b'\) in an algebraic closure. Subtract its copy of
(11). With \(R(X)=-q_{11}/q_{02}\), this gives
\[
b+b'=R(X)(X+\lambda)-2\mu X.
\]
The left side is independent of X. The free X derivative is
\[
0=R'(X)(X+\lambda)+R(X)-2\mu.
\tag{14}
\]
If lambda has degree two in mu, its quadratic coefficient forces
\(R'=0\); then (14) says \(R=2\mu\), impossible.
If \(\lambda=l_1\mu+l_0\), with \(l_1\in\mathbb C^*\), the
mu and constant coefficients give
\[
l_1R'=2,\qquad (X+l_0)R'+R=0.
\]
Differentiating the second equation and using the first gives
\(4/l_1=0\), again impossible. These are all possibilities,
since lambda is the nonconstant polynomial of degree at most two
in (4). Thus b belongs to \(\mathbb C(\mu)\). Its integrality
and the normality of the polynomial PID \(\mathbb C[\mu]\) now give
\[
b\in\mathbb C[\mu].
\tag{15}
\]

## 5. The binary quadratic must have rank one

View (11) over an algebraic closure of \(k_X\), with mu still a
transcendental polynomial variable. If its binary quadratic form
has rank two, it splits into two independent linear forms.
Their values at \((X+\lambda,b+\mu X)\) are polynomials in mu
whose product is the nonzero constant \(-\mathfrak a\).
Both are units, hence constant in mu. Independence of the two
linear forms would make \(X+\lambda\) constant in mu, impossible.

Thus the nonzero binary quadratic has rank one. Some nonzero
linear form \(u(X)Y+v(X)W\), possibly first over the algebraic
closure, has value constant in mu on the two velocities in (11).
Here \(v\ne0\), since lambda is nonconstant. Comparing degrees
first gives \(\deg_\mu b\le2\). If the quadratic coefficient
of lambda is nonzero, its comparison with that of b makes
\(u/v\) complex constant. The linear coefficient would then
require \(u\lambda_1/v+b_1+X=0\), impossible. Therefore the
quadratic coefficient of lambda vanishes. Formula (4) now gives
\[
B=0,\qquad A\in\mathbb C^*,\qquad
\lambda=\lambda_0-\frac A2\mu,\qquad
b=b_1\mu+b_0,\quad b_1,b_0\in\mathbb C.
\tag{16}
\]
This argument includes \(b_1=0\), \(b_0=0\), and their simultaneous
vanishing. It has not asserted that the generic invariant itself
is an actual ambient coordinate.

## 6. A full actual normalization of this remaining family

In (4),(16) set \(a=C/A\), \(e_0=D/A\), and
\(\epsilon=E_0-DC/A\), all complex. The actual polynomial map
\[
\begin{aligned}
X_*&=X+\lambda_0,\\
Y_*&=Y+aX_*^2,\\
Z_*&=Z+2aY+a^2X_*^2-\epsilon X_*,\\
W_*&=W+e_0X_*^2
\end{aligned}
\tag{17}
\]
has the polynomial inverse
\[
\begin{aligned}
X&=X_*-\lambda_0,\qquad
Y=Y_*-aX_*^2,\\
Z&=Z_*-2aY_*+a^2X_*^2+\epsilon X_*,\qquad
W=W_*-e_0X_*^2.
\end{aligned}
\tag{18}
\]
It is the composition of426's X translation, time translation,
s translation and a linear Z shear. Pulling back its coefficients,
\[
\begin{gathered}
t_*=t+C/A,\qquad s_*=s+D/A,\qquad k_*=A t_*s_*,
\qquad m_*=A t_*,\\
P_*=P-2\lambda_0t,\qquad
\mu_*=\mu,\quad \lambda_*=-A\mu/2,\qquad
b_*=(b_1-\lambda_0)\mu+b_0.
\end{gathered}
\tag{19}
\]
The exact partials in t,s are unchanged by the constant translations,
so the normalized \(\kappa\) remains nonzero.

Every map and inverse has the original filtered weights of426.
The full initial relation is retained, not just its vanishing.
Here the literal Z partial is unchanged, so \(N_*=N\);
\(a_{0,*}=a_0\) and \(NP_*=\rho\). The actual localized quotient
argument in426 retains both field and whole-ring returns and the
scalar calibration. This is an actual change, unlike the generic
coordinate of (9). Reset notation, including renaming \(b_1-\lambda_0\)
as \(b_1\). We now have
\[
k=Ats,\quad m=At,\quad
\lambda=-A\mu/2,\quad b=b_1\mu+b_0,\quad
A\in\mathbb C^*,\quad \kappa\ne0.
\tag{20}
\]
The functions r,h,c,n remain arbitrary except for the identities
derived next.

## 7. The entire lower P coefficient of the generic invariant

The existence of (9) persists under (17), or follows again by
applying the same two-quasi alternative in this actual frame.
The changes in (17) are affine in Y,W,Z over \(k_X\), so the
generic invariant still has a quadratic polynomial part in Y,W.
Define the auxiliary ACTUAL polynomial
\[
\mathcal U=W+\frac{2(X+b_1)}A\,Y,\qquad
H(X)=\frac{2X(X+b_1)}A+b_0.
\tag{21}
\]
Its intrinsic P coefficient is H. The unique linear direction
of the rank-one quadratic part is proportional to \(\mathcal U\):
this follows by setting the mu coefficient of its velocity to zero.
Its quadratic coefficient is therefore
\(-\mathfrak a\,\mathcal U^2/H^2\), by (11).
Here H is a nonzero polynomial of degree two, and only generic
rational identities divide by H.

Write \(\mathcal U=HP+U_0\), where
\[
U_0=c+hX+sX^2+\frac{2(X+b_1)}A(r+tX^2).
\]
The P coefficient of Z in (20)'s actual rows is \(2tX+As\).
The remaining part of the generic invariant is linear in Y and
\(\mathcal U\). Its full P coefficient thus forces
\[
2U_0-H(2tX+As)\ \in\ \mathbb C(X)+\mathbb C(X)\mu.
\tag{22}
\]
The left side is exactly
\[
X\left(2h+\frac{4r}A-2b_0t-2b_1s\right)
 +\left(2c+\frac{4b_1r}A-Ab_0s\right).
\tag{23}
\]
Each of its two coefficients belongs to \(\mathbb C+\mathbb C\mu\).
For example evaluate (22) at two distinct regular complex X values
and invert their complex Vandermonde matrix. This argument uses
neither a rationality assertion for L nor a normalization of a
coefficient-field function to an ambient coordinate.

There are consequently complex constants
\(\alpha_1,\alpha_0,\beta_1,\beta_0\), allowed to vanish, such that
\[
\begin{aligned}
h&=-\frac{2r}A+b_0t+b_1s+\frac{\alpha_1\mu+\alpha_0}{2},\\
c&=-\frac{2b_1r}A+\frac{Ab_0s}{2}
                           +\frac{\beta_1\mu+\beta_0}{2}.
\end{aligned}
\tag{24}
\]
No lower coefficient was set to zero in this comparison.

## 8. The complete original scalar has a forbidden complex-X factor

At fixed X introduce the moving intrinsic center and coefficients
\[
\begin{aligned}
R&=P+tX+\frac{As}{2},&
\chi&=\mu t-s,&
\varrho&=r+\frac{A^2\mu s}{4},\\
\mathcal K&=2tr+Ath+n-\frac{A^2s^2}{4},&
F(X)&=\alpha_1X+\beta_1.
\end{aligned}
\tag{25}
\]
Direct substitution in the ORIGINAL rows (5), with (20),(24),
gives the three complete rows
\[
\begin{aligned}
Y&=(X-A\mu/2)R+\varrho+\frac A2\chi X,\\
Z&=R^2+\mathcal K,\\
\mathcal U&=H(X)R+\frac{F(X)\mu}{2}
                            +\frac{\alpha_0X+\beta_0}{2}.
\end{aligned}
\tag{26}
\]
The change from P to R has parameter Jacobian one, including its
moving t,s terms. Replacing the W row by \(\mathcal U\) is a row
operation of determinant one at fixed X. Hence the determinant of
(26) in \((t,s,R)\) is exactly the scalar in (2).
We do not assert that the auxiliary \(\mathcal U\), whose time
degree can be three, supplies another1222 chart.

Put \(\{f,g\}=f_tg_s-f_sg_t\), at fixed R. On coefficient
functions these are the same t,s partials, and
\(\{\chi,\mu\}=\mu_t+\mu\mu_s=\kappa\). The entire determinant is
\[
J=R J_1+J_0,
\tag{27}
\]
where
\[
\begin{aligned}
J_1={}&-\frac A2H\,\{\mu,\mathcal K\}
       -F\,\{\varrho,\mu\}-\frac A2XF\,\kappa,\\
J_0={}&H\left(\{\varrho,\mathcal K\}
                    +\frac A2X\{\chi,\mathcal K\}\right)
       +\frac12(X-A\mu/2)F\,\{\mathcal K,\mu\}.
\end{aligned}
\tag{28}
\]
For a direct full reconstruction, the derivative matrix is
\[
\begin{pmatrix}
-A\mu_tR/2+\varrho_t+A\chi_tX/2&
-A\mu_sR/2+\varrho_s+A\chi_sX/2&X-A\mu/2\\
\mathcal K_t&\mathcal K_s&2R\\
F\mu_t/2&F\mu_s/2&H
\end{pmatrix}.
\tag{29}
\]
Its possible R-squared coefficient cancels by
\(d\mu\wedge d\mu=0\). Expansion gives exactly (27),(28).

The three coefficients of \(J_1=0\), in descending X order, are
\[
\begin{aligned}
\{\mu,\mathcal K\}&=-\frac{A\alpha_1\kappa}{2},\\
\alpha_1\{\varrho,\mu\}
 &=\frac{A\kappa}{2}(b_1\alpha_1-\beta_1),\\
\beta_1\{\varrho,\mu\}
 &=\frac{A^2b_0\alpha_1\kappa}{4}.
\end{aligned}
\tag{30}
\]
If \(\alpha_1=0\), the second equation and \(A\kappa\ne0\)
force \(\beta_1=0\). Then F is zero, and (27),(28) make the
entire determinant divisible by the nonconstant polynomial H.
It cannot equal the nonzero coefficient scalar (2).

If \(\alpha_1\ne0\), set \(\zeta=\beta_1/\alpha_1\in\mathbb C\).
The last two equations of (30) give
\[
\zeta(b_1-\zeta)=\frac{Ab_0}{2},\qquad
H(X)=\frac2A(X+\zeta)(X+b_1-\zeta),\qquad
F(X)=\alpha_1(X+\zeta).
\tag{31}
\]
Every term of the COMPLETE determinant (27),(28) is a multiple
of H or F. It is therefore divisible by \(X+\zeta\) in
\(L[R,X]\), again contradicting (2).
This also covers \(\zeta=0\), \(b_0=0\), and a repeated root of H.
No division by a root difference or a value of H was used at the
endpoint. Equivalently, direct evaluation at the permitted complex
value \(X=-\zeta\) makes the full determinant zero.

Both alternatives of the two-quasi theorem are now excluded.
Together with477's complex-lambda case and the actual initial
normalization (3), this proves the stated complex-omega exclusion.

## 9. Scope and verification record

The conclusion concerns the full actual264 chart, variable coupling,
a birational projected line and nonconstant sigma. It imposes no
claim on a noncomplex omega, constant sigma, other projected curves,
or entry into such a chart from arbitrary ambient coordinates.
The retained ancestor statements264,296,325,426,474,477 and480 are
used with their actual hypotheses. No recursive certification of
their entire earlier ancestry is asserted.

The current426 and474 were completely reread before this proof.
The held480 was completely read through EOF in1b1e20/e865de;
its SHA is
d2c1d6c56a90ad75c31c6c1861b20b186bd3aeaed89278a041e6148597a4499f.
The current477 had previously received a complete independent
saved-source audit through c67097/50a98d, with final hash c52b4ad2
ending91f3933. The primary Theorem4.1, both its alternatives,
and its actual-ring descent warning were freshly inspected in the
linked author source, retrieval turn4675view0/1. The writing guide
was completely reread in328f19.

Fresh unsaved674386 reconstructs every original-to-compact row
in (26), the whole determinant (27),(28), all three coefficients
(30), the moving parameter Jacobian and (31); all residuals vanish.
Fresh unsaved a88726 reconstructs both inverse compositions
(17),(18), exact normalized coupling and slopes, and the complete
weighted initial-relation transport. The field intersections,
conjugate argument, binary-form alternatives and all vanishing
branches are proved explicitly above, rather than inferred from
those symbolic calculations.

No saved checker was executed, imported, compiled or rerun.
No earlier or canonical source was edited. Independent source review
is separate from this author verification. No historical novelty,
human-expert certification, proof-assistant certificate or public
submission is claimed.
