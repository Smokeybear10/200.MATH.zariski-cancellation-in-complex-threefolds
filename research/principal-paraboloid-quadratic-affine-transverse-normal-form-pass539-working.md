# An actual transverse normal form and two residual quadratic-affine branches

Working necessary reduction: retain the FULL actual264 chart and the
quadratic-sigma, nonconstant-affine-theta sector of537, with noncomplex
coupling \(m=k_s\). A complex polynomial change of the actual coordinate
frame preserves every264 entry hypothesis and arranges
\[
k_t=0,\qquad y=r\in L,\qquad m_t=0,\qquad h=m_s\ne0.
\tag{1}
\]
After a separate intrinsic centering, the remaining equations split into
two disjoint branches. Their necessary restrictions are
\[
\begin{array}{ll}
\nu_0=0,\ C_0\ne0:
 &3h h_{ss}-5h_s^2=0,\quad (\lambda_s/h)_s=0,\\[2pt]
C_0=0,\ \nu_0\ne0:
 &h_s=0,\quad \lambda_s=0.
\end{array}
\tag{2}
\]
All symbols are defined below. Neither branch is excluded or recognized
here. In particular a square root introduced to center sigma need not
belong to the original fraction field. No square-based contradiction is
claimed.

## 1. Full actual hypotheses and the input from537

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and unit ideals of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the complete conclusions of
[537](principal-paraboloid-quadratic-sigma-affine-theta-longitudinal-exclusion-pass537-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\qquad Na_0=Nt=Ns=0,\\
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad
L[A]=L[v],\quad Nv=1,\\
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w),\qquad
L[y,z_{\rm int},w]=L[v],\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{3}
\]
The symbol \(z_{\rm int}\) always means the literal Z-intercept,
not its difference with \(2ty\).
Assume \(m=k_s\notin\mathbb C\), \(\deg_v\sigma=2\), and
\(\deg_v\theta=1\). In particular \(m\ne0\).

Result537 gives \(m_t=0\). Since the joint constants of the exact
coefficient partials are \(\mathbb C\), it follows that \(h=m_s\ne0\).
It also gives
\[
a:=k_{tt}\in\mathbb C,\qquad y+(a/4)\sigma\in L.
\tag{4}
\]
The latter follows from its centered expression
\(y=-a x^2/4+C,\ \sigma=x^2+c\); the expression on the left belongs
to the original \(L[v]\) and is killed by N, hence belongs to L.
No centered square root is needed for (4).

## 2. A complex actual coordinate map

The element
\[
b_0=k_t-at
\]
has both coefficient derivatives zero: its t derivative is \(k_{tt}-a\),
and its s derivative is \(m_t\). Hence \(b_0\in\mathbb C\).
Put \(q=a/4\) and define the ACTUAL coordinates
\[
X^*=X-q,\qquad Y^*=Y+(b_0/2)X^*,\qquad Z^*=Z,\qquad W^*=W.
\tag{5}
\]
The inverse is
\[
X=X^*+q,\qquad Y=Y^*-(b_0/2)X^*,\qquad Z=Z^*,\qquad W=W^*.
\tag{6}
\]
All coefficients are complex; both a and \(b_0\) are allowed to vanish.
This is a polynomial automorphism of determinant one and a particular
member of the completely checked filtered family
[426](general-coupling-normalization-obstruction-pass426-working.md).
The needed licenses are also verified directly here.

The original derivation E, slice u, and kernel A do not change.
One has \(X^*=a_0u+(x_0-q)\), so \(a_0^*=a_0\).
Only terms of strictly smaller E-degree were added to X and Y.
Thus ALL four initial forms are identical to the original ones.
Consequently the exact profile, entire initial kernel, and parameters
\(t^*=t,\ s^*=s\) are unchanged, not merely one initial relation.

The literal coordinate partial is unchanged:
\[
\partial_{Z^*}=\partial_Z.
\tag{7}
\]
Indeed X and Y in (6) do not involve \(Z^*\).
Thus the selected coefficient in the ORIGINAL slice remains the same
N, with the same L, v, and relations \(Na_0=Nt=Ns=0\).
No rescaling or replacement of that selected partial is made.

Expanding the full literal rows at fixed \(X^*\) gives
\[
\begin{aligned}
\sigma^*&=\sigma+at/2+b_0/2,&
\theta^*&=\theta+as/2,\\
y^*&=y+(a/4)\sigma+a^2t/16,&
k^*&=k-at^2/2-b_0t,\\
z_{\rm int}^*&=z_{\rm int}+(a/4)(2t\sigma+k)+a^2t^2/16,&
w^*&=w+(a/4)\theta+a^2s/16.
\end{aligned}
\tag{8}
\]
Therefore \(y^*\in L,\ k_t^*=0,\ m^*=k_s^*=m\), and the original
intrinsic degrees of sigma and theta remain two and one.
All new intercept and slope coefficients lie in \(A_{a_0}\).

For completeness, the strong complex-field return must be rederived
from the actual fiber, not inferred from an affine map over L.
The actual equality
\(\mathcal B_{a_0}=A_{a_0}[X^*]\) holds. The coordinate prime \(X^*\)
does not divide \(a_0\): otherwise additivity of E-degree would
contradict \(\deg_E a_0=0,\ \deg_E X^*=1\).
Hence \(\mathcal B/(X^*)\) injects into its \(a_0\)-localization.
Evaluating the actual frame at \(X^*=0\) gives
\[
A_{a_0}
 =\mathbb C[y^*,z_{\rm int}^*,w^*]_{a_0},\qquad
\operatorname{Frac}A=\mathbb C(y^*,z_{\rm int}^*,w^*),\qquad
L[y^*,z_{\rm int}^*,w^*]=L[v].
\tag{9}
\]
Here \(a_0\) itself is a polynomial in these three intercepts:
evaluate its polynomial expression in the starred actual coordinates.
Since \(a_0\in L^*\), localization disappears after adjoining L.

At fixed \(X^*\), the three bad-coordinate differential rows in
\((t,s,v)\) are the old rows evaluated at \(X=X^*+q\). The added
\((b_0/2)X^*\) has zero such differential. Thus
\[
J^*_{t,s,v}(X^*)=J_{t,s,v}(X^*+q)=-a_0^4.
\tag{10}
\]
Every actual264 input has now been verified. The new first, second,
third and fourth potentials are those derived from this actual new
chart, not independently assigned coefficient functions.
We drop stars from now on.

## 3. Intrinsic centering and its exact field boundary

In this normalized actual frame write, in the ORIGINAL parameter,
\[
\sigma=A_\sigma(v-v_0)^2+c,\qquad
\theta=D(v-v_0)+e,\qquad
A_\sigma,D\in L^*,\quad v_0,c,e\in L.
\tag{11}
\]
Choose \(\rho^2=A_\sigma\) in the finite extension \(L'=L(\rho)\), and put
\[
x=\rho(v-v_0),\qquad
\sigma=x^2+c,\qquad\theta=dx+e,\qquad d=D/\rho\in L'^*.
\tag{12}
\]
These are intrinsic expressions only. The coefficient partials extend
uniquely to \(L'\) and are then extended to fix x.
The original intrinsic speed and scalar become
\[
Nx=\rho,\qquad J_{t,s,x}=-a_0^4/\rho\in L'^*.
\tag{13}
\]
The whole all-X return becomes
\(L'[X,Y,Z,W]=L'[X,x]\); this does not identify the original actual
three-ring or its fraction field with a polynomial ring over \(L'\).

The denominator-free multiplier of
[535](principal-paraboloid-nonlinear-sigma-unit-multiplier-pass535-working.md)
transports exactly as established in537:
\[
\kappa=\kappa_v/\rho^2=\kappa_v/A_\sigma\in L^*,\qquad
\tau_x=\rho\tau_v.
\tag{14}
\]
In particular the centered multiplier descends to L, although d need not.
The invariant square
\[
z:=d^2=D^2/A_\sigma\in L^*
\tag{15}
\]
also descends. In later equations z means (15), not a coordinate
or a literal intercept.

The finite extension is essential: \(A_\sigma\) need not be a square
in L. Neither x nor d is asserted to belong to the original
\(\operatorname{Frac}A=L(v)\).
The conjugation \(\rho\mapsto-\rho\), when nontrivial, changes both
x and d by a sign and leaves every actual row unchanged.
All equations below are equivariant under this conjugation.
A displayed square in \(L'(X)(x)\) is not automatically a square
in the original actual fraction field. No prime-square obstruction
or ambient coordinate claim may be inferred from such a display here.

## 4. Complete literal rows, potential and multiplier coefficients

Use \(y=r\in L,\ \lambda=n_t\), and \(h=m_s\ne0\), with
\(m_t=k_t=0\). Define
\[
\nu_0=\frac{he+n_s}{m},\qquad C_0=2r+\lambda+\frac{hd^2}{2}.
\tag{16}
\]
Both belong to L by (15).
The ENTIRE normalized rows are
\[
\begin{aligned}
Y&=r+\sigma X+tX^2,\\
Z&=2tr+\sigma^2+m\theta+n+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
w&=-\frac{C_0}{m}x^2-d\nu_0x+w_0,\qquad
w_0=\frac{\ell-(2r+\lambda)c-he^2/2-n_se}{m}.
\end{aligned}
\tag{17}
\]
No coefficient of the actual constant row has been set to a complex
constant or discarded.

The full genuine third potential restricted to \(U=r\), with
formal P,V still independent, is
\[
\begin{aligned}
H(r,P,V)={}&r^2+\lambda r+(hV+n_s)
 \frac{\ell-(2r+\lambda)P-hV^2/2-n_sV}{m}\\
&+\frac{h_s}{6}V^3+\frac{n_{tt}}2P^2+\lambda_sPV
 +\frac{n_{ss}}2V^2-\ell_tP-\ell_sV.
\end{aligned}
\tag{18}
\]
It evaluates to its moving coefficient-field level \(h_0\).
Its exact top coefficients are
\[
[x^4](H^{\rm ev}-h_0)=n_{tt}/2,\qquad
[x^3](H^{\rm ev}-h_0)
 =d\left(-\frac{hC_0}{m}+\frac{h_s d^2}{6}+\lambda_s\right).
\tag{19}
\]
Thus
\[
n_{tt}=0,\qquad \lambda_t=0,\qquad
\frac{hC_0}{m}=\frac{h_s d^2}{6}+\lambda_s.
\tag{20}
\]
No rationality of \(F=\ker(\partial_t|_L)\) is assumed.

For clarity, the complete evaluated \(f=H_U^{\rm ev}\) and
the two cleared535 expressions are
\[
\begin{aligned}
f={}&-\frac{2hd}{m}x^3-2\nu_0x^2-\frac{2hdc}{m}x
                                     +2r+\lambda-2c\nu_0,\\
\mathcal B_\beta={}&4d_t x^3+
 (4e_t+4C_0/m+2dd_s)x^2
 +2d(e_s+\nu_0-c_t)x-c_sd^2,\\
\mathcal A_\beta={}&4r_t x^2+2dr_sx,\qquad \beta=2x,\\
\mathcal B_\beta&=-\kappa f,\qquad
\mathcal A_\beta=\kappa H_V^{\rm ev}.
\end{aligned}
\tag{21}
\]
In particular the cubic coefficient gives the crucial nonzero speed
\[
d_t=\frac{\kappa h d}{2m}\ne0,\qquad
z_t=\frac{\kappa h z}{m}\ne0.
\tag{22}
\]
All quantities in the second equation belong to L.
Hence z is transcendental over F: an element algebraic over the
constants of a characteristic-zero derivation is killed by it.

## 5. The exact all-X split

The complete Laurent collision expression of537 specializes here to
\[
\mathcal L(u)=C_0+\frac{dm\nu_0}{u}.
\tag{23}
\]
The all-X whole return makes it a nonzero Laurent monomial.
For recall, a nonzero root u lifts to a finite pair of intrinsic
points on the divided first-potential fiber; setting X from the
divided Y equation makes all three divided rows vanish. The whole
polynomial inverse prohibits this, including when the pair is
diagonal. The identically zero Laurent polynomial is also forbidden.
Consequently precisely one of \(C_0,\nu_0\) is zero:
\[
(\nu_0=0,\ C_0\ne0)\quad\text{or}\quad
(C_0=0,\ \nu_0\ne0).
\tag{24}
\]
This argument uses polynomial specialization after all actual rows
are formed. It does not differentiate a moving pair or replace a
coefficient-field value of X by an actual coordinate.

## 6. The branch nu0 equals zero

Assume \(\nu_0=0\), so \(e=-n_s/h\).
Since \(h_t=0\), equation (20) gives
\[
e_t=-\lambda_s/h,\qquad
r=R_0+R_1z,\quad
R_0=\frac{m\lambda_s}{2h}-\frac{\lambda}{2},\quad
R_1=\frac{mh_s}{12h}-\frac h4.
\tag{25}
\]
The \(x^2\) coefficient of
\(\mathcal B_\beta+\kappa f=0\) in (21) gives, without dividing
by \(h_s,R_1\), or r,
\[
d_s=-\frac{h_s d}{3h},\qquad z_s=-\frac{2h_s z}{3h}.
\tag{26}
\]
Put
\[
a_\lambda=\lambda_s/h,\qquad b_h=h_s/(6h),\qquad
C_0/m=a_\lambda+b_hz.
\tag{27}
\]
The coefficients \(m,h,\lambda,a_\lambda,b_h,R_0,R_1\) are killed
by \(\partial_t\). The exact Jacobian is
\[
\det\frac{\partial(r,C_0/m)}{\partial(t,s)}
=z_t\left(-\frac{h(a_\lambda)_s}{4}
          +\frac{5h_s^2-3hh_{ss}}{72h}\,z\right).
\tag{28}
\]
This identity includes the derivatives of both integrated equations
in (25),(26).

Here is why the left side must vanish, using an ACTUAL ring rather
than a coefficient-field polynomial presentation.
As in537, the derivation
\(\Delta=a_0N-(NX)E\) is a nonzero LND fixing X on
\[
\mathcal R=\mathbb C(X)[Y,Z,W],\qquad
\operatorname{Frac}\mathcal R=L(X)(v).
\tag{29}
\]
It has nonconstant polynomial invariants and extends on the finite
coefficient extension as \(a_0\rho\partial_x\).
Use only the localized coordinate shear
\[
Z_1=Z-Y^2/X^2
   =m\theta+n+kX-\frac{2r\sigma}{X}-\frac{r^2}{X^2}.
\tag{30}
\]
Its inverse over \(\mathbb C(X)\) is polynomial in Y,Z1,W.
It is not asserted to be a polynomial automorphism over \(\mathbb C\).

If the Jacobian in (28) were nonzero, r and \(C_0/m\) would be
algebraically independent over \(\mathbb C\), and in particular
\(r\ne0\). Since \(C_0\ne0\) in this branch, the exact intrinsic
profile of \((Y,Z_1,W)\) would be \((2,2,2)\), with initials
\[
XT^2,\qquad -2rT^2/X,\qquad -(C_0/m)T^2.
\tag{31}
\]
Their ratios recover the two independent coefficient functions.
Together with the independent degree variable T they are algebraically
independent over \(\mathbb C(X)\).
But a nonconstant actual Delta-invariant has intrinsic degree zero;
its positive weighted highest part gives a nonzero relation among
these initials, a contradiction.
If \(r=0\) from the outset, the Jacobian in (28) is already zero.
Thus no zero-r or dropped-Z1-degree case was discarded.

Using \(z_t\ne0\) and the transcendence of z over F in (28) proves
\[
\boxed{3hh_{ss}-5h_s^2=0,\qquad (\lambda_s/h)_s=0.}
\tag{32}
\]
In particular \(a_\lambda\) has both coefficient derivatives zero,
so \(a_\lambda\in\mathbb C\), and exact subtraction gives
\(\lambda=a_\lambda m+\lambda_0\) with \(\lambda_0\in\mathbb C\).
Neither \(h_s=0\) nor \(R_1=0\) has been excluded, and no division
by either occurred.

## 7. The branch C0 equals zero

Assume \(C_0=0,\ \nu_0\ne0\).
Equation (20) becomes
\[
\lambda_s+h_s z/6=0.
\tag{33}
\]
Both \(\lambda_s\) and \(h_s\) belong to F, whereas \(z_t\ne0\).
Differentiating (33) in t therefore gives \(h_s z_t=0\).
It follows without dividing by \(\lambda_s\) or \(h_s\) that
\[
\boxed{h_s=0,\qquad\lambda_s=0.}
\tag{34}
\]
Consequently \(h\in\mathbb C^*,\ \lambda\in\mathbb C\), and
\[
m=hs+\mu,\quad \mu\in\mathbb C,\qquad
r=-\lambda/2-hz/4.
\tag{35}
\]
The nonzero \(\nu_0\) and the remaining lower scalar coefficients
are not solved here. In particular (35) is not a realization
or a recognition theorem.

## 8. Verification and precise remaining scope

The full actual264/296 inputs,535,537, and the complete filtered
transport426 were read before using them.
Fresh unsaved e0da1d reconstructed all three full transported rows,
the inverse map, and determinant one for (5).
The original-slice, full-initial-kernel, selected-partial, exact
fiber-return, and scalar arguments are supplied in Section2.

Fresh unsaved2da897 reconstructed the entire restricted genuine H,
the full w and B expressions, both high potential coefficients,
and the complete Jacobian identity (28); every residual was zero.
Independent outline calculations supplied by Jet checked the same
unrestricted lower coefficients and both branch deductions.
Those checks are not a claim of independent saved-source review.

The new conclusions are the ACTUAL normalization (1), the exact
two-way split (24), and the necessary branch equations (32),(34).
The finite extension in Section3 was never descended by assuming
its square root lies in L. Formal squares after that extension do
not establish any actual-coordinate prime obstruction.
No branch exclusion, recognition, nonlinear-sigma-wide result,
arbitrary chart entry, unrestricted cancellation, novelty, or
external certification is claimed.

Only this source was authored. No saved checker was executed,
imported, compiled, or rerun; no earlier source or canonical record
was edited. Complete independent saved-source review remains a
separate step.
