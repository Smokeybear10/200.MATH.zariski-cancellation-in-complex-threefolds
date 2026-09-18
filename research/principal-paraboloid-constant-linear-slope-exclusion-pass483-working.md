# A constant first slope is excluded on the variable-coupling projected line

Working theorem: retain EVERY actual hypothesis of264, variable
coupling \(m=k_s\notin\mathbb C\), and the birational projected-line
hypothesis of325 with nonconstant sigma. Write the affine intrinsic
data as
\[
y=\lambda\sigma+r_{\rm old},\qquad
\theta=\mu\sigma+h.
\]
Then
\[
\boxed{\lambda\notin\mathbb C.}
\tag{1}
\]
The proof uses an actual coordinate fiber, an elementary lemma for
a plane locally nilpotent derivation, and the full original scalar.
It does not promote an intrinsic parameter or a generic invariant
to an actual coordinate. It does not exclude noncomplex lambda,
constant sigma, nonlinear projected curves, or arbitrary chart entry.

## 1. Actual hypotheses and the constant-slope normalization

Retain the complete actual input of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and calibrated scalar of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the birational projected-line reduction of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the FULL initial kernel},\\
0\ne N=[u^4]\partial_Z|_A\in\operatorname{LND}(A),\quad
Na_0=Nt=Ns=0,\quad L=\operatorname{Frac}\ker_A N,\\
[L:\mathbb C(t,s)]<\infty,\quad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w_{\rm int}],\quad Nv=1,\\
K:=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w_{\rm int}),\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The exact coefficient partials commute and have joint constant
field \(\mathbb C\). The original slice, selected partial and both
returns are retained. No rationality of L or normality of a projected
plane is assumed.

By325 all three intrinsic functions are affine. Thus
\(P=\sigma\) is a polynomial parameter of O and
\[
NP=\rho\in L^*,\qquad
w_{\rm int}=\omega P^2+bP+c,\qquad
\lambda,\mu,r_{\rm old},h,\omega,b,c\in L.
\tag{3}
\]
The expression for the W-intercept follows from the full second
potential. Both slopes may initially vanish. The scalar in this
intrinsic parameter is \(-a_0^4/\rho\), not the scalar obtained by
setting \(NP=1\).

Suppose \(\lambda\in\mathbb C\). If also
\(\omega\in\mathbb C\), the fully read held
[477](principal-paraboloid-variable-coupling-complex-slope-exclusion-pass477-working.md)
already excludes the branch, including zero values. It remains to
treat \(\omega\notin\mathbb C\). Use the ACTUAL polynomial map
\[
X_*=X+\lambda,\qquad Y_*=Y,\qquad Z_*=Z,\qquad W_*=W.
\tag{4}
\]
Its inverse subtracts the same complex constant from X. The fully
read transport
[426](general-coupling-normalization-obstruction-pass426-working.md)
preserves the exact time profile, entire initial ideal, original
slice and kernel, literal selected partial, both returns and scalar.
The relevant coefficient transport is
\[
\begin{gathered}
t_*=t,\quad s_*=s,\quad k_*=k+2\lambda t^2,\quad m_*=m,\quad
N_*=N,\\
P_*=P-2\lambda t,\quad y_*=r_{\rm old}+\lambda^2t,\quad
\lambda_*=0,\quad \omega_*=\omega,\quad \mu_* =\mu.
\end{gathered}
\tag{5}
\]
The last equality concerns the slope after theta is expressed in
the new parameter; its intercept changes. Nonconstant sigma and
the birational projected-line condition persist. Drop stars and
write \(y=r\in L\) from now on. The normalized literal rows are
\[
\begin{aligned}
Y&=r+PX+tX^2,\\
Z&=P^2+aP+G+(2tP+k)X+t^2X^2,\\
W&=\omega P^2+bP+c+(\mu P+h)X+sX^2,\\
a&=k_t+m\mu,\qquad G=2tr+mh+n.
\end{aligned}
\tag{6}
\]
Here \(\omega\notin\mathbb C\). All coefficients in (6) are
the actual264 coefficients in the normalized frame, not assigned
formal functions.

## 2. An elementary equal-degree lemma for a plane derivation

Let k be any characteristic-zero field and let
\(\delta\in\operatorname{LND}_k(k[Z,W])\). Suppose Z and W
have the same positive delta degree d. Put
\[
\alpha=\delta^dZ/d!,\qquad \gamma=\delta^dW/d!.
\]
Both are nonzero invariant polynomials. Then
\[
\boxed{\gamma/\alpha\in k.}
\tag{7}
\]
Indeed, if both are already in k there is nothing to prove.
Otherwise choose one of them that is not in k and call it F.
It is a nonconstant invariant polynomial. Let \(F_D\) be its
nonzero highest ordinary homogeneous part, of degree \(D>0\).
The exponential identity
\[
F(\exp(T\delta)Z,\exp(T\delta)W)=F(Z,W)
\]
has \(T^{dD}\) coefficient \(F_D(\alpha,\gamma)=0\),
because the two coordinate exponentials have exact T-degree d
and leading coefficients alpha,gamma. Dividing by \(\alpha^D\)
gives the nonzero polynomial equation
\(F_D(1,\gamma/\alpha)=0\) over k.

The field k is relatively algebraically closed in \(k(Z,W)\).
For an elementary characteristic-zero proof, if a rational function
is algebraic over k, differentiate its separable minimal polynomial
with respect to Z and W. Both rational partials vanish, and hence
the function lies in k. Applying this to \(\gamma/\alpha\)
proves (7). No algebraic closure of k, irreducibility of delta,
classification of plane actions, or coordinate-invariant theorem
is used. We will apply only the case \(d=2\).

## 3. The actual X fiber gives omega in C(r)

Extend N to the original ring \(A[u]\) by \(Nu=0\), and define
the polynomial derivation
\[
\Delta=a_0N-(NX)E.
\tag{8}
\]
It fixes X, kills L in the fraction field, and commutes with E.
It is locally nilpotent: on
\(\mathcal B_{a_0}=A_{a_0}[X]\) it is exactly \(a_0N\) at
fixed X, with \(Na_0=0\). This localized derivation is locally
nilpotent and restricts to the displayed polynomial derivation
of the original ring. Therefore its restriction is locally nilpotent
as well. Neither \(EX\) nor any parameter speed is declared an
actual unit.

Let \(\ell_0=a_0\rho\in L^*\). From the ORIGINAL rows (6),
\[
\begin{gathered}
\Delta Y=\ell_0X,\qquad
\Delta^2Z=2\ell_0^2,\qquad
\Delta^2W=2\omega\ell_0^2,\\
\Delta^3Z=\Delta^3W=0.
\end{gathered}
\tag{9}
\]
These are identities in the original fraction field whose left
sides are actual polynomials. The two second derivatives belong
to \(\mathcal B\cap K=A\), and are nonzero. We next check that
they do not vanish on the actual fiber X=0.

The ideal \((X)\) is prime in \(\mathcal B\), since X is an
actual coordinate. It has zero contraction to A. In fact a nonzero
identity \(f=Xg\) with \(f\in A\) and \(g\in\mathcal B\)
would contradict the additive locally nilpotent degree:
\(0=\deg_Ef=1+\deg_Eg\). Consequently every nonzero element
of \(K=\operatorname{Frac}A\) has X-adic valuation zero.
Residue therefore defines an injective field map
\[
\iota:K\hookrightarrow
\operatorname{Frac}(\mathcal B/(X))=\mathbb C(\overline Y,
                                                    \overline Z,
                                                    \overline W).
\tag{10}
\]
For precision this is the residue map in the discrete valuation
ring \(\mathcal B_{(X)}\): all elements of K are in that ring,
and every nonzero one is a unit. Thus there is no unlicensed
specialization of a coefficient-field denominator.

All coefficients in the fixed-X rows are in K, so those rows give
\[
\iota(r)=\overline Y,\qquad
\iota(z)=\overline Z,\qquad
\iota(w_{\rm int})=\overline W.
\tag{11}
\]
In particular r is noncomplex. The strong return in (2) also
identifies the two fields in (10), although only injectivity and
the first equality of (11) are needed below.

Because \(\Delta X=0\), Delta induces a locally nilpotent
derivation \(\overline\Delta\) on the ACTUAL polynomial
three-ring \(\mathcal B/(X)=\mathbb C[\overline Y,\overline Z,\overline W]\).
Equation (9) and the valuation argument show that it kills
\(\overline Y\), while
\[
\overline\Delta^{\,2}\overline Z=2\iota(\ell_0^2)\ne0,
\quad
\overline\Delta^{\,2}\overline W
          =2\iota(\omega\ell_0^2)\ne0,
\quad
\overline\Delta^{\,3}\overline Z
 =\overline\Delta^{\,3}\overline W=0.
\tag{12}
\]
For the first assertion, write \(\ell_0=g/h\) with
\(g,h\in A\), \(h\ne0\). The polynomial identity
\(h\Delta Y=Xg\) reduces to
\(\overline h\,\overline\Delta\overline Y=0\).
Since \(\overline h\ne0\) and the quotient is a domain,
\(\overline\Delta\overline Y=0\). This does not presume that
the speed itself was polynomial merely from its notation.
For the nonzero assertions the second derivatives are nonzero
elements of A and hence survive the quotient. Omega is nonzero
because it is noncomplex.

Localize this actual quotient at
\(\mathbb C[\overline Y]\setminus\{0\}\). Its derivation is
a nonzero LND of the plane over \(k=\mathbb C(\overline Y)\),
and its two coordinates have exact degree two by (12). Lemma (7)
therefore gives \(\iota(\omega)\in\mathbb C(\overline Y)\).
Using (10),(11), this pulls back to
\[
\boxed{\omega\in\mathbb C(r)\setminus\mathbb C.}
\tag{13}
\]
This is only a coefficient restriction. It is not an assertion
that r or P is an actual coordinate of A, nor a descent of an
arbitrary generic-field invariant coordinate.

## 4. A moving intrinsic center and the first scalar gates

Choose an element q of \(\{t,s\}\) for which \((r,q)\) is
a separating coefficient basis. Such a choice exists because r
is noncomplex and the joint constants of the original partials
are \(\mathbb C\). Write
\(\Lambda=\det\partial(r,q)/\partial(t,s)\ne0\).
The extension \(L/\mathbb C(r,q)\) is finite, and its exact
coefficient partials commute. Put
\(F=\ker_L\partial_q|_r\). Its r derivative is denoted by a
prime. In particular \(\omega\in F\) and
\[
\omega'\ne0.
\tag{14}
\]
This follows directly from (13) in characteristic zero. It does
not require a rationality assertion about F or L.

At fixed actual X make only the intrinsic change
\[
\xi=P+tX,\qquad
\phi=k-ta,\quad M=\mu-2\omega t,\quad
C=c,\quad H=h-tb,\quad \chi=s-\mu t+\omega t^2.
\tag{15}
\]
Together with the unchanged definition of G in (6), the entire
ORIGINAL rows become
\[
\begin{aligned}
Y&=r+X\xi,\\
Z&=\xi^2+a\xi+G+\phi X,\\
W&=\omega\xi^2+(b+MX)\xi+C+HX+\chi X^2.
\end{aligned}
\tag{16}
\]
This identity retains every intercept and every coefficient of X.
It is not a replacement of actual coordinates by L-valued ones.
The original slice makes X transcendental over K, and the affine
change \(P\leftrightarrow\xi\) is invertible over \(L[X]\).
Hence X and xi are algebraically independent over L.

The full parameter determinant from \((t,s,P)\) to
\((r,q,\xi)\), including the moving tX term, is Lambda. Thus
\[
J_{r,q,\xi}(X)=-\frac{a_0^4}{\rho\Lambda}\in L^*.
\tag{17}
\]
All coefficient derivatives now fix the displayed intrinsic
parameter. Expanding the full derivative matrix of (16), its
\(X\xi^3\) coefficient is exactly \(-\omega'a_q\).
Calibration and (14) force \(a_q=0\), so \(a\in F\).

At X=0 the ENTIRE determinant is then
\[
-2b_q\xi^2+(2\omega G_q-a b_q-2C_q)\xi+bG_q-aC_q.
\tag{18}
\]
It must still be the nonzero scalar (17). Therefore
\[
b_q=0,\quad C_q=\omega G_q,\quad
(b-a\omega)G_q\ne0.
\tag{19}
\]
In particular \(b\in F\) and \(G_q\ne0\). This includes and
excludes the possible zero G-speed case before a new basis is
chosen. No division by a, b or either of their derivatives is used.

## 5. Two lower coefficients contradict nonconstant omega

Use the exact separating basis \((r,G)\). Its second partial is
\(\partial_G|_r=(\partial_q|_r)/G_q\), so its kernel is still F.
Its r derivative agrees on F with the earlier prime derivative.
The exact scalar is
\[
J:=J_{r,G,\xi}(X)
   =-\frac{a_0^4}{\rho\Lambda G_q}\in L^*,
\qquad J=b-a\omega\ne0.
\tag{20}
\]
The second equality follows from (18),(19); it is not a new
normalization of the speed. Since \(C_G=\omega\), there is an
existing element \(C_0\in F\) with \(C=\omega G+C_0\).

With a,b,omega in F, direct expansion of the FULL determinant
of (16) gives its entire xi-squared coefficient as
\[
[\xi^2]J
 =-X(2M_G+\omega')
    +X^2(a'M_G-\omega'\phi_G).
\tag{21}
\]
The two coefficients and (14) give, successively,
\[
M_G=-\omega'/2,\qquad \phi_G=-a'/2,
\quad M=-\omega'G/2+M_0,\quad
\phi=-a'G/2+\phi_0,\quad M_0,\phi_0\in F.
\tag{22}
\]
If \(a'=0\), the same calculation gives \(\phi_G=0\);
no zero derivative of a was divided out.

For complete inspection of all moving terms, the derivative
matrix after these gates, with columns \((r,G,\xi)\), is
\[
\begin{pmatrix}
1&0&X\\
a'\xi+\phi_rX&1-a'X/2&2\xi+a\\
\omega'\xi^2+(b'+M_rX)\xi+\omega'G+C_0'+H_rX+\chi_rX^2&
-\omega'X\xi/2+\omega+H_GX+\chi_GX^2&
2\omega\xi+b+MX
\end{pmatrix}.
\tag{23}
\]
Here \(\phi_r=-a''G/2+\phi_0'\) and
\(M_r=-\omega''G/2+M_0'\); those derivatives, and every
derivative of H and chi, remain in the matrix.
Two exact coefficients of its determinant are
\[
\begin{aligned}
[X\xi]J&=\frac{a\omega'-4H_G-2b'}2,\\
[X\xi^0]J&=
\frac{-3G\omega'+2M_0-2aH_G-ba'-2C_0'}2.
\end{aligned}
\tag{24}
\]
The first must vanish, so
\(H_G=a\omega'/4-b'/2\in F\).
The second must also vanish. Differentiating this zero identity
with respect to G kills every term except its displayed linear
G term, and yields
\[
0=-3\omega'/2,
\tag{25}
\]
contrary to (14). Thus the normalized branch \(\lambda=0\),
\(\omega\notin\mathbb C\) is empty. Together with the complex
omega branch of477 and the actual map (4), this proves (1).

## 6. Exact scope and verification

The actual fiber is essential to (13). A generic rank theorem
alone would not identify omega as a rational function of r,
and the coefficient functions in (16) are not assumed to be
actual coordinates. The residue map used only the actual
coordinate X, its positive E-degree, and the original kernel
A. It did not require a global unit speed, a slice for the
fiber derivation, or a normality assumption about an intrinsic
plane algebra.

The proof covers every constant lambda, including zero, within
the stated variable-coupling birational projected-line entry.
The theorem477 is used only when omega is complex. The new
argument does not rely on the beta-zero exclusion481 or on
the omega-complex reduction480. No new recognition endpoint,
realization, or unrestricted cancellation conclusion is asserted.

The complete264,296,325,426 and477 sources were read directly,
and the writing guide was reread before authoring. Fresh unsaved
algebra reconstructs the original-to-centered identities (16),
the full original cubic scalar coefficient, (18),(21), the
complete moving matrix (23), and both terminal coefficients
(24). The written arguments prove the fiber specialization,
plane lemma, exact coefficient-basis changes and all zero cases.
No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical file was edited. No historical
novelty, human-expert verification, or formal certification is claimed.
