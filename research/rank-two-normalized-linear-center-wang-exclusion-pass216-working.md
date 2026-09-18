# Wang's alternatives exclude the normalized linear rank-two center

Status: bounded working exclusion. The remaining normalized linear-center
chart from215 cannot be an actual globally sliced exact1122 frame with
full initial kernel \((\mathsf Z\mathsf W-\mathsf X^4)\).
Wang's alternatives are applied over \(\mathbb C(X)\), and the final
contradiction uses only a constant translation of an original coordinate.
No coefficient-field parameter is declared to be an ambient coordinate.

## 1. Exact normalized actual input

Retain the full actual hypotheses and the proved normalization in
[linear-center reduction215](rank-two-linear-center-affine-reduction-pass215-working.md),
freshly read through EOF. Together with
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md),
these give
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\qquad
q=1/\rho,\quad [L:\mathbb C(t,\rho)]<\infty,\\
N=[u^3](\partial_Z|_A)\ne0,\quad A_L=L[v],\quad Nv=1,
\quad L[y,z,w]=L[v],\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+\rho^{-1}X^2,\quad
\sigma=-\rho^{-2}\vartheta+k,\\
k_t=-c/\rho,\quad n_{tt}=0,\quad c\in\mathbb C^*,\quad
\deg_v\vartheta=1,\\
y=\frac{\vartheta^2}{c\rho^2}+p_1\vartheta+p_0,\quad
w=\lambda\vartheta+\omega,\quad z=\kappa\vartheta+\zeta .
\end{gathered}
\tag{1}
\]
All lower coefficients in (1) lie in the exact field \(L\).
The independent coefficient partials \(\partial_t,\partial_\rho\)
commute, extend those on \(\mathbb C(t,\rho)\), and have joint
constant field \(\mathbb C\), by the minimal-polynomial argument
in215. No identification of either one-partial constant field with
a rational function field is made.

The normalization in215 used actual complex-coefficient shears,
preserving the full initial kernel and the literal original
\(\partial_Z\), hence \(N,L,t,\rho\). The whole-line equality
in (1) and the nonzero calibrated determinant come from that
actual frame. They are not assumed for an arbitrary formal ansatz.

## 2. Lower identities forced by the full potentials

Write
\[
k=-ct/\rho+f,\qquad n=gt+h,\qquad
f_t=g_t=h_t=0,
\tag{2}
\]
by taking \(f=k+ct/\rho\), \(g=n_t\), and \(h=n-tn_t\).
Primes in this section denote the coefficient rho-partial.
Thus \(k_\rho=ct/\rho^2+f'\),
\(k_{\rho\rho}=-2ct/\rho^3+f''\), and
\(k_{t\rho}=c/\rho^2\).

Let \(b=n_t-\rho^3k_\rho k_{t\rho}/2\) be the center slope.
The full coefficient identity (9) of215, in the normalized chart,
reads \(p_1=\rho k_\rho/c+2(b+\rho b')/c^2\).
Since \(b=g-c^2t/(2\rho)-c\rho f'/2\), this gives the explicit
identity
\[
p_1=\frac t\rho-\frac{\rho f'}c-\frac{\rho^2f''}c
                         +\frac{2(g+\rho g')}{c^2} .
\tag{3}
\]
In particular \((p_1)_t=1/\rho\). This conclusion is derived
from the full potentials, not a choice of an integration gauge.

The V-squared coefficient of the third potential
\(\mathcal Rw+S(y,V)-\ell=0\), with
\(\mathcal R=2\rho^{-3}V+k_\rho\), is
\(2\rho^{-3}\lambda+(c/\rho^2)p_1+k_{\rho\rho}/2
 +g/(c\rho^2)=0\).
The second potential
\(z=-\rho^{-2}w+\rho^{-3}V^2+k_ty+k_\rho V+n\)
then gives \(\kappa=-\rho^{-2}\lambda-cp_1/\rho+k_\rho\).
Substituting (3) yields
\[
\begin{aligned}
\lambda&=\frac{\rho^2f'}2+\frac{\rho^3f''}4
                      -\frac{\rho(3g+2\rho g')}{2c},\\
M:=\kappa-\rho^{-2}\lambda
       &=\frac{g}{c\rho}+f'+\frac{\rho f''}2 .
\end{aligned}
\tag{4}
\]
Both \(\lambda\) and \(\kappa\) therefore have t-partial zero;
their rho-dependence is not suppressed.

One more coefficient of the fourth potential is essential.
Its exact expression in212 is
\(\rho^{-3}w^2+c_0(y,V)w+Q(y,V)=0\), where
\[
\begin{aligned}
c_0(U,V)&=-3\rho^{-4}V^2+k_{t\rho}U
                         +k_{\rho\rho}V+n_\rho,\\
Q(U,V)&=\rho^{-5}V^4+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\qquad
H_j(a)=\sum_{i=0}^j\frac{a_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\end{aligned}
\tag{5}
\]
After substituting (1), the leading V-fourth terms in \(Q\)
cancel. The coefficient of V-cubed in the complete fourth potential
is
\[
-\frac{2\lambda}{\rho^4}-\frac{cp_1}{\rho^3}
 +\frac{ct}{\rho^4}+\frac{f'''}6+\frac{g'}{c\rho^2}
 =\frac{g+\rho g'}{c\rho^3}+\frac{f''}{2\rho}+\frac{f'''}6=0 .
\tag{6}
\]
For clarity, the first term comes from the V-squared coefficient
\(-2\rho^{-4}\) of \(c_0(y,V)\) times \(\lambda V\).
The next terms come respectively from
\(k_{t\rho\rho}yV^2/2\), \(k_{\rho\rho\rho}V^3/6\), and
\(n_{t\rho}yV\). Terms involving \(p_0,h,\ell,m,\omega\)
have degree at most two and cannot affect this identity.

Multiply (6) by \(c\rho^3\). It is precisely the derivative
of \(\rho g+(c/6)\rho^3f''\). That expression also has
t-partial zero, so joint constants give
\[
\rho g+\frac c6\rho^3f''=\epsilon\in\mathbb C,
\qquad
M=\frac{\epsilon}{c\rho^2}+f'+\frac{\rho f''}3 .
\tag{7}
\]
All steps so far are exact identities in \(L\).

## 3. The actual auxiliary derivation and Wang's alternatives

The original polynomial LND from215 is
\(\mathcal P=aN-(NX)E\), where \(a=EX\ne0\) and \(N\)
is extended to \(A[u]\) by \(Nu=0\). On
\(B_a=A_a[X]\), it fixes \(X\) and restricts to \(aN\);
this proves its local nilpotence on the preserved original ring.
Put \(\tau=aN\vartheta\in L^*\). Its exact original actions are
\[
\begin{gathered}
\mathcal PX=0,\quad
\mathcal PY=\tau\left(\frac{2\vartheta}{c\rho^2}+p_1\right),\quad
\mathcal PZ=\tau(\kappa-\rho^{-2}X),\quad
\mathcal PW=\tau(X+\lambda),\\
\mathcal P^2Y=\frac{2\tau^2}{c\rho^2}\ne0,
\qquad \mathcal P^2Z=\mathcal P^2W=\mathcal P^3Y=0 .
\end{gathered}
\tag{8}
\]
The products in (8) are actual polynomials. This does not assert
that \(\tau\) or \(\rho\) is globally regular.

Let \(\Delta\) be a gcd of the nonzero polynomial coefficients
of \(\mathcal P\), and let \(D=\mathcal P/\Delta\).
Since \(\mathcal P\Delta=\Delta D\Delta\), LND-degree
additivity forces \(\mathcal P\Delta=0\): a nonzero derivative
would have degree one less than \(\Delta\), while its divisibility
by \(\Delta\) would give at least that degree.
Thus \(D\Delta=0\), and \(\mathcal P^j=\Delta^jD^j\) proves
that \(D\) is a polynomial LND with the same coordinate degrees.
It is irreducible by construction. It stays irreducible after
localization to \(K[Y,Z,W]\), where \(K=\mathbb C(X)\):
a nonconstant common factor there would yield a common primitive
polynomial factor of the original coefficients by Gauss's lemma.
Both \(DZ,DW\) are nonzero and have second iterate zero.

We use the exact Theorem4.1 in
[Dasgupta--Gupta, *Nice derivations over principal ideal domains*](https://arxiv.org/html/1701.03635v1),
freshly read as the authors' restatement of Wang. For an irreducible
LND of a polynomial three-ring over a characteristic-zero field,
with two coordinates of second iterate zero, it gives either an
invariant nonzero linear form in those two coordinates, or an
invariant coordinate \(F\) such that
\(K[Y,Z,W]=K[F,Z,W]\). In the second alternative it also places
\(DZ,DW\) in \(K[F]\), although that extra conclusion will not
be needed here. No direct reading of Wang's original paper is claimed.

Set \(s=\rho^{-2}\), which is transcendental over \(\mathbb C\).
The ratio
\[
\frac{DZ}{DW}=\frac{\kappa-sX}{X+\lambda}
\tag{9}
\]
is transcendental over \(K\), not merely outside \(K\).
Indeed, suppose it satisfied a nonzero polynomial relation with
coefficients in \(\mathbb C[X]\), after clearing denominators.
Let \(n\) be the largest X-degree of those coefficients.
Divide by \(X^n\) and take the constant term in the expansion
at \(X=\infty\). The ratio in (9) has constant term \(-s\),
so this produces a nonzero complex polynomial vanishing at \(-s\).
The polynomial is nonzero because at least one coefficient had
degree \(n\); its separate powers of the ratio give separate
powers of \(-s\). This contradicts transcendence of \(s\).

Wang's first alternative is therefore impossible. In the second,
an automorphism in the single variable \(Y\) over \(K[Z,W]\)
has degree one and a unit leading coefficient. Scaling \(F\)
by that nonzero element of \(K\), write
\[
F=Y+Q(Z,W),\qquad Q\in K[Z,W],\qquad DF=0 .
\tag{10}
\]
The ordinary degree of \(Q\) is exactly two. To justify this,
for a nonzero homogeneous leading part \(Q_j\) the value
\(Q_j(DZ,DW)\) is nonzero by (9), and
\(D^jQ=j!Q_j(DZ,DW)\). Higher terms are absent and lower terms
have j-th iterate zero. A degree greater than two contradicts
\(D^3Y=0\) and \(DF=0\); a degree less than two contradicts
\(D^2Y\ne0\).

Write the quadratic part as
\(\alpha(X)Z^2+\beta(X)ZW+\gamma(X)W^2\).
Apply \(D^2\) to (10), then divide the resulting equality in the
fraction field by \(2(\tau/\Delta)^2\ne0\). Equation (8) gives
\[
\frac{s}{c}+\alpha(X)(\kappa-sX)^2
 +\beta(X)(\kappa-sX)(X+\lambda)
 +\gamma(X)(X+\lambda)^2=0,
\qquad \alpha,\beta,\gamma\in\mathbb C(X).
\tag{11}
\]
This step does not require either factor of the divided expression
to be an original unit or polynomial.

## 4. Laurent coefficients force a finite rational list

Expand the three rational coefficient functions at \(X=\infty\).
Let \(m\) be their largest nonzero Laurent exponent. Their terms
of degree \(m+2\) in (11) have coefficient
\(\alpha_m s^2-\beta_m s+\gamma_m\).
This is nonzero because \(1,s,s^2\) are linearly independent
over \(\mathbb C\), and at least one of the three coefficients
is nonzero. It follows from (11) that \(m=-2\): a larger
exponent cannot cancel the constant \(s/c\), and a smaller
one cannot cancel it either. The constant coefficient in (11)
then determines
\[
\begin{gathered}
\alpha=\alpha_{-3}X^{-3}+O(X^{-4}),\quad
\beta=c^{-1}X^{-2}+\beta_{-3}X^{-3}+O(X^{-4}),\\
\gamma=\gamma_{-3}X^{-3}+O(X^{-4}),\\
M=\kappa-s\lambda=m_0+m_1s+m_2s^2,
\quad m_i\in\mathbb C .
\end{gathered}
\tag{12}
\]
For the last line compare the coefficient of \(X^{-1}\): it is
\(M/c+\alpha_{-3}s^2-\beta_{-3}s+\gamma_{-3}\).
Thus \(m_0=-c\gamma_{-3}\),
\(m_1=c\beta_{-3}\), \(m_2=-c\alpha_{-3}\).

Combine (7) and (12). The equation for \(f\) is
\[
\rho f''+3f'
 =3m_0+3(m_1-\epsilon/c)\rho^{-2}+3m_2\rho^{-4} .
\tag{13}
\]
This equation integrates exactly in the finite field \(L\),
without presuming rationality. Multiply it by \(\rho^2\), so
the left side is \((\rho^3f')'\). Integrate the explicit powers
on the right, then integrate once more. Each integration constant
has rho-partial zero and also t-partial zero because \(f_t=0\).
Hence both constants are complex. The complete result is
\[
\begin{gathered}
f=m_0\rho+\frac{b_*}{\rho}+\frac{d_*}{\rho^2}
                      +\frac{m_2}{\rho^3}+e_*,\qquad
b_*=3(\epsilon/c-m_1),\quad d_*,e_*\in\mathbb C,\\
g=\frac{cm_1}{\rho}-\frac{cd_*}{\rho^2}-\frac{2cm_2}{\rho^3}.
\end{gathered}
\tag{14}
\]
For the second equality use the first identity in (7).
Substitution of (14) into (4), with no remaining lower datum
discarded, gives
\[
\lambda=\frac{m_0/s-m_1-3m_2s}{2},\qquad
\kappa=\frac{3m_0+m_1s-m_2s^2}{2} .
\tag{15}
\]
The coefficients \(b_*,d_*,e_*\) have canceled from these two
slopes; they have not been normalized away by a field change.

## 5. The exact quadratic identity removes both extreme modes

Because \(s\) and \(X\) are algebraically independent over
\(\mathbb C\), substitute (15) into (11) and regard the result
as a rational-function identity in \(s\) over \(\mathbb C(X)\).

If \(m_0\ne0\), then at \(s=0\), \(X+\lambda\) has principal
part \(m_0/(2s)\), while \(\kappa-sX\) has nonzero constant
term \(3m_0/2\). The coefficient of \(s^{-2}\) in (11) forces
\(\gamma=0\). The coefficient of \(s^{-1}\) then forces
\(\beta=0\). Its constant coefficient forces \(\alpha=0\).
This leaves \(s/c=0\), a contradiction. Therefore \(m_0=0\).

If \(m_2\ne0\), the highest s-degrees of
\(\kappa-sX\) and \(X+\lambda\) are two and one, with
coefficients \(-m_2/2\) and \(-3m_2/2\).
The degree-four coefficient in (11) forces \(\alpha=0\),
the degree-three coefficient then forces \(\beta=0\), and
the degree-two coefficient forces \(\gamma=0\).
Again \(s/c\) cannot vanish. Thus
\[
m_0=m_2=0,\qquad
\lambda=-m_1/2\in\mathbb C,
\qquad \kappa=-\rho^{-2}\lambda .
\tag{16}
\]
This conclusion used the full rational identity (11), not only
its initial Laurent coefficients.

## 6. An actual constant translation contradicts whole-line return

Make the actual polynomial coordinate change
\[
X_*=X+\lambda,\qquad Y_*=Y,\quad Z_*=Z,\quad W_*=W .
\tag{17}
\]
Its inverse subtracts the complex constant \(\lambda\) from
\(X_*\); both inverse orders are the identity.
The exact E-degrees and all four leading coefficients are unchanged,
so the full initial kernel, \(t,\rho,q,a\), are unchanged.
Also \(\partial_{Z_*}=\partial_Z\), and therefore the selected
\(N\) and \(L\) are literally the same.

The new projected entries, obtained by substituting
\(X=X_*-\lambda\) in (1), are
\[
\begin{aligned}
\vartheta_*&=\vartheta-2\rho\lambda,
&y_*&=y-\lambda t,\\
w_*&=w-\lambda\vartheta+\rho\lambda^2
      =\omega+\rho\lambda^2\in L,\\
z_*&=z-\lambda\sigma+\rho^{-1}\lambda^2
      =\zeta-\lambda k+\rho^{-1}\lambda^2\in L .
\end{aligned}
\tag{18}
\]
The last equality uses (16). In particular
\(\deg_v\vartheta_*=1\), and \(\deg_v y_*=2\); its nonzero
quadratic coefficient is unchanged. No assertion about regularity
of any displayed coefficient in \(L\) is needed for the actual
change (17), whose only coefficient is \(\lambda\in\mathbb C\).

The new actual coordinates must still have whole-line return:
\[
L[y_*,z_*,w_*]=L[v] .
\tag{19}
\]
One can see this directly as well as from212. The ring obtained by
adjoining \(L\) to the original polynomial ring is
\(L[v][X_*]=L[X_*,Y_*,Z_*,W_*]\), since \(a\in L^*\) and
\(X_*\) is an affine slice coordinate over \(L[v]\).
Quotienting by \(X_*\) gives precisely (19).
But (18) makes its left side \(L[y_*]\), while \(y_*\) has
degree two in \(v\). Every nonconstant polynomial in \(y_*\)
has even positive v-degree, so it cannot contain \(v\).
This contradiction excludes the normalized chart (1).

## 7. Exact conclusion and verification boundary

The remaining normalized nonconstant-second linear-center branch
of215 is impossible under the supplied actual hypotheses.
The proof did not require a global slice for the auxiliary \(D\),
an invariant coordinate produced by Wang over the original base,
or a polynomial contraction of \(K[F]\). Its only final original
coordinate change was the explicit constant translation (17).
The known zero-return and constant-second recognition branches
remain separate inputs to any larger synthesis.

The complete saved215 input and the relevant212 and214 sources
were read before this argument. The exact primary Wang restatement
was freshly checked. The lower coefficients (3)--(7) and slope
identities (14)--(15) were independently reconstructed, with new
unsaved symbolic arithmetic used by separate agents as supporting
checks. This is not a claim of an executed saved verification suite.
No saved checker was executed, imported or compiled; no earlier
source, index or packet was changed. No unrestricted cancellation,
arbitrary coordinate-entry, formal certification, or historical
novelty claim is made.
