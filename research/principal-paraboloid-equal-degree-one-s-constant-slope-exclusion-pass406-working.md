# A nonconstant degree-one slope cannot be s-constant

Working scoped exclusion: retain the full actual264 chart with k=s,
n_ss nonzero, and equal intrinsic degree one. If the affine y/sigma
slope lambda is nonconstant and lambda_s=0, the full scalar condition
is impossible. The proof first derives a necessary coefficient family
from the zero-safe401 high equations. Its lower scalar coefficients
then force 3K_z=0 although K_z must be nonzero.

This does not classify slopes with lambda_s nonzero, remove arbitrary
coupling, or prove entry of a general cancellation candidate.

## 1. Complete actual entry and licensed nonzero gates

Keep every actual264 hypothesis, the degree-one presentation and
notation of
[401](principal-paraboloid-equal-degree-one-delta-zero-necessary-family-pass401-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,
\quad a_0=EX\ne0,\quad\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full kernel},\quad
N=[u^4]\partial_Z|_{A_0}\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad[L:\mathbb C(t,s)]<\infty,
\quad K=L(P)=\mathbb C(y,z,w),\\
O=L[P]=L[y,\sigma,\theta]=L[y,z,w],\quad P=\sigma,\quad
\rho=NP\in L^*,\\
y=\lambda P+r,\quad\theta=\mu P+h,\quad\mu\in L^*,
\quad k=s,
\quad J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
All actual potentials, their unit conditions, both returns, the
literal selected partial and original global slice remain required.
The exact coefficient partials commute and have joint constants C.

Write nu=n_s, e=n_ss nonzero, b=n_ts, c=n_tt, and
\[
\delta=\lambda-\nu,\quad
\mathscr D=\partial_t+\mu\partial_s,\quad
\beta=\mathscr D\nu=b+e\mu,\quad
\kappa=\mathscr D\mu,\quad\mathcal K=\kappa+4\lambda.
\tag{2}
\]
The symbol Kcal is not the function field K. The scoped exclusion
[403](principal-paraboloid-delta-zero-conductor-exclusion-pass403-working.md)
already gives delta nonzero in this degree-one setting.

Assume for contradiction
\[
\lambda_s=0,\qquad\lambda\notin\mathbb C.
\tag{3}
\]
Then lambda_t is nonzero, since otherwise lambda is a joint complex
constant. Also Dscript(lambda)=lambda_t. The genuine H top and two
high scalar equations of401 become
\[
\begin{gathered}
c+2b\mu+e\mu^2+2\lambda^2-4\nu\lambda=0,\\
2\delta\lambda_t+\beta\mathcal K=0,\qquad
(\beta-\delta\mu_s)\lambda_t=0.
\end{gathered}
\tag{4}
\]
Thus beta and Kcal are both nonzero, and
\[
v:=\mu_s\ne0,\quad\beta=\delta v,\qquad
\lambda_t=-v\mathcal K/2.
\tag{5}
\]
The letter v in this note means mu_s, not a previously normalized
intrinsic parameter. All uses of it below are coefficient-field uses.

## 2. The coefficient compatibility forces mu to be affine in s

Let S=ker_L(partial_s). It is stable under partial_t. Every
integration below first produces an element of this exact field;
it is made complex only after its t derivative also vanishes.

Differentiate the last equality of (5) in s. Since lambda_ts=0 and
Kcal_s=Dscript(v)+v^2, this gives
\[
\mathscr Dv+v^2=-\mathcal K v_s/v.
\tag{6}
\]
Next differentiate the first equation of (4) in s. The Hessian
identities c_s=b_t and b_s=e_t imply
\[
\mathscr D\beta=\mathcal K e-2v\beta.
\tag{7}
\]
For verification, Dscript(beta)=c_s+2mu*b_s+mu^2*e_s+kappa*e;
the s derivative of the H equation replaces its first three terms
by 4lambda*e-2v*beta. On the other hand beta=delta*v and
Dscript(delta)=lambda_t-beta give
\[
\delta(\mathscr Dv+v^2)=\mathcal K(e+v^2/2).
\tag{8}
\]
Combining (6),(8), using Kcal nonzero, gives
\[
e=-\delta v_s/v-v^2/2,\qquad
f:=\delta/v-\mu/2\in S.
\tag{9}
\]
Indeed delta_s=-e and differentiating the defining f yields zero.

Put U=mu+2f. Then U_s=v and delta=vU/2, so U is nonzero and
transcendental over S. The latter follows by differentiating a
separable minimal polynomial if U were algebraic over S.
Use Dscript(delta)=lambda_t-delta*v, the identity
Dscript(U)=Kcal-4lambda+2f_t, and (6) to obtain
\[
U v_s=2v^2+C v^3,\qquad
C=(2\lambda-f_t)/\lambda_t\in S.
\tag{10}
\]
This calculation divides only by already nonzero v,Kcal,lambda_t.
For example multiplying the delta derivative by two gives
U(Dscript(v)+v^2)=-2v*Kcal+2v(2lambda-f_t), which proves (10).

Equation (10) integrates without assuming rationality of L:
\[
\partial_s(U^2/v+C U^2/2)=0.
\tag{11}
\]
Consequently there are p0,p1,p2 in S with
\[
s=p_0U+p_1/U+p_2,\qquad
v^{-1}=p_0-p_1/U^2,
\qquad p_0=-C/2.
\tag{12}
\]
To justify the first equality, write U^2/v+C U^2/2=J in S.
Take p1=-J. The s derivative of p0*U+p1/U is then one, so
their difference from s defines p2 in S.

The pair t,U is a separating coefficient basis because U_s=v
is nonzero. Differentiate (12) at fixed U, leaving p0,p1,p2
with their ordinary t derivatives. Combining mu=U-2f with the
last equality of (5) gives the rational identity
\[
\begin{aligned}
U-2f-[(p_0)_tU+(p_1)_t/U+(p_2)_t]
={}&-2\lambda_t(p_0-p_1/U^2)^2\\
&-(4\lambda-2f_t)(p_0-p_1/U^2).
\end{aligned}
\tag{13}
\]
Since U is transcendental over S, compare Laurent coefficients.
The coefficient of U^{-4} gives -2lambda_t*p1^2=0. Thus p1=0.
The coefficient of U then gives (p0)_t=1. As p0 belongs to S,
\[
p_0=T:=t-\tau,\qquad\tau\in\mathbb C.
\tag{14}
\]
In particular T is nonzero. It follows from (12) that
\[
\mu=s/T+B_1,\quad B_1\in S,\qquad\mu_s=1/T.
\tag{15}
\]
The last equality of (5), with (15), is
(T B1+2T^2 lambda)_t=0. Its s derivative is already zero, so
there is a complex b0 with
\[
\boxed{\mu=(s+b_0)/T-2T\lambda.}
\tag{16}
\]
No unknown function in S has been silently replaced by a complex
constant: each complex constant above is killed by both partials.

## 3. The necessary potential and an actual normalization

Equation (9), with v=1/T and v_s=0, gives e=-1/(2T^2).
Put S0=s+b0. Using beta=delta/T in (5) gives
\[
\nu=\eta/T-S_0/(2T^2),\qquad\eta\in\mathbb C.
\tag{17}
\]
In detail, nu+S0/(2T^2) has zero s derivative. Substitution in
Dscript(nu)=(lambda-nu)/T makes the t derivative of
T[nu+S0/(2T^2)] zero as well, proving (17).

Integrating n_s and then using the first H equation of (4) yields
\[
\boxed{n=-S_0^2/(4T^2)+\eta S_0/T+\gamma t+c_0,
\qquad\gamma,c_0\in\mathbb C.}
\tag{18}
\]
Indeed the difference from the two displayed rational terms is
s-constant. Direct substitution of (16),(17) into H makes its second
t derivative zero; its affine coefficients are therefore joint
complex constants. This calculation permits eta=0 and imposes no
rationality on the s-constant lambda.

Use the following ACTUAL complex polynomial change of the original
four coordinates, with s0=-b0:
\[
\begin{aligned}
X^*&=X,\qquad Y^*=Y-\tau X^2+\gamma/2,\\
Z^*&=Z-2\tau Y+\tau^2X^2-s_0X-(\gamma\tau+c_0),\\
W^*&=W-s_0X^2.
\end{aligned}
\tag{19}
\]
Although the same map was used in398 for constant theta, no such
constant-theta hypothesis is used here. Its inverse is
X=X*, Y=Y*+tau*X*^2-gamma/2,
Z=Z*+2tau*Y*+tau^2*X*^2+s0*X*+c0,
W=W*+s0*X*^2. Both Jacobians are one. Its exact coefficient
transport is t*=T, s*=S0, sigma*=sigma, theta*=theta,
y*=y+gamma/2, z*=z-2tau*y-(gamma*tau+c0), w*=w,
n*=n-gamma*t-c0, ell*=ell.

These formulas hold for arbitrary intrinsic y and theta. The weighted
leading map fixes the entire ideal (X^2Z-Y^2), and the new exact
leaders are a0, a0^2*T, a0^2*T^2 and a0^2*S0, all nonzero.
The inverse gives partial_Z*=partial_Z, so N and L are unchanged.
The intrinsic return is unchanged because sigma,theta are unchanged
and y is translated by a complex constant. The intercept return
is retained by the displayed invertible complex affine map of
y,z,w. The coefficient-base and output Jacobians are one, so the
full scalar remains calibrated. Thus every actual hypothesis is
preserved, not just the potential (18).

Drop stars only after this check. The necessary normalized family is
\[
n=-s^2/(4t^2)+\eta s/t,\qquad
\mu=s/t-2t\lambda,\qquad
\lambda_s=0,\quad\lambda_t\ne0.
\tag{20}
\]
The normalization leaves the nonconstant slope and its derivative
properties intact. It is not a coefficient-dependent ambient shear.

## 4. The complete scalar in a moving parameter

Put q=s/t and zeta=q+2t*lambda. At fixed actual X use
\[
R=P+tX+q/2,\qquad
\det\frac{\partial(t,s,P)}{\partial(t,\zeta,R)}=t.
\tag{21}
\]
The pair t,zeta is a separating coefficient basis: its s derivative
is 1/t, and lambda_s=0. Write dots and primes for its exact commuting
t and zeta partials. Then lambda'=0 and dot(lambda)=lambda_t is
nonzero. These are field and intrinsic parameter changes, not
original coordinate maps.

Define coefficient elements
\[
\begin{aligned}
K_0&=2tr+h+\eta q-q^2/2,\\
G&=r-\lambda q/2,\\
V&=\ell+r q-\nu h-\eta\lambda q,
\qquad\nu=(\eta-q/2)/t.
\end{aligned}
\tag{22}
\]
The subscript in K0 distinguishes it from the function field and
the earlier Kcal. The definitions are invertible in the coefficient
field: solve successively for r,h,ell. Substitution in the FULL
literal401 rows gives
\[
\begin{aligned}
Y&=(X+\lambda)R-\zeta X/2+G,\\
Z&=R^2+K_0,\\
W&=-2\lambda R^2+(\zeta X-2G+2\eta\lambda)R
                      +(K_0-\eta\zeta)X+V.
\end{aligned}
\tag{23}
\]
Their exact determinant Jtilde in (t,zeta,R) equals
t*J=-t*a0^4/rho, a nonzero coefficient scalar independent of X,R.
Its X-squared coefficient is
\[
[X^2] \widetilde J=(\zeta-2\eta)\dot K_0/2.
\tag{24}
\]
As zeta is transcendental over C, zeta-2eta is nonzero. Hence
dot K0=0. Also K0' cannot vanish: otherwise the Z differential
row would be (0,0,2R), making the calibrated scalar vanish at R=0.
Thus
\[
\dot K_0=0,\qquad K_0'\ne0.
\tag{25}
\]

After (25), the complete determinant has only the following terms:
\[
\begin{aligned}
[XR]\widetilde J&=2\eta\dot G-2\eta K_0'\dot\lambda
                              +\zeta K_0'\dot\lambda-\dot V,\\
[X]\widetilde J&=K_0'(\zeta\dot G-\dot V),\\
[R^2]\widetilde J&=-2\dot\lambda(V'+\lambda K_0'-2\eta G'),\\
[R]\widetilde J&=-2(GK_0'\dot\lambda+\dot G K_0'\lambda
                                          +\dot G V'-G'\dot V),\\
[1]\widetilde J&=K_0'(-2G\dot G+2\eta\lambda\dot G-\lambda\dot V).
\end{aligned}
\tag{26}
\]
All four nonconstant coefficients must vanish. The X and XR terms
first give
\[
\dot V=\zeta\dot G,\qquad\dot G=K_0'\dot\lambda.
\tag{27}
\]
The divisions use only K0' and zeta-2eta, already nonzero. The
R-squared equation gives V'=2eta*G'-lambda*K0'. Substitute this
and (27) into the R equation to get
\[
G+(2\eta-\zeta)G'=0.
\tag{28}
\]
Here the canceled factor K0'*dot(lambda) is nonzero.

Differentiate V'+lambda*K0'-2eta*G'=0 by dot. Commutation,
(25),(27), and lambda'=0 give
\[
2K_0'+(\zeta-2\eta)K_0''=0.
\tag{29}
\]
Differentiate (28) by dot and use the same identities to get
\[
K_0'-(\zeta-2\eta)K_0''=0.
\tag{30}
\]
The sum says 3K0'=0, contradicting (25) in characteristic zero.
No integration or rationality assumption about K0,G,V is needed.
This excludes (20) and, through the actual normalization, every
case (3) under the retained actual hypotheses.

## 5. Evidence and limits

Root's complete401 and403 reads are12882f and6a3b6f. Freshcc81ec
independently reconstructed the Hessian and slope compatibilities
behind (6)--(9). Fresh4fe01b substituted arbitrary lambda(t) into
the normalized family (20) and obtained zero for the entire high H,
high Q and both high scalar equations. This is a consistency check,
not a converse realization claim.

Fresh10431d independently reconstructed every literal row in (23)
from the complete401 formulas, the parameter determinant t, the
X-squared coefficient, every coefficient in (26), and the final
zero-safe elimination. All residuals were zero. The exact-field
integrations, Laurent comparison and actual normalization license
are written arguments above. This draft requires separate saved-
source review before canonical acceptance.

Only lambda_s=0 with noncomplex lambda is excluded here. Complex
constant slopes, other characteristic branches, higher degrees,
general coupling and arbitrary-chart entry are not settled by this
note. No saved checker was executed, imported, compiled or rerun;
no held source was changed. No unrestricted cancellation, novelty,
human-expert review or formal certification is claimed.
