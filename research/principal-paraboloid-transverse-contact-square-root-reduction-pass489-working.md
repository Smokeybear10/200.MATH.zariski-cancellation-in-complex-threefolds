# Transverse contact parameter: an exact square-root reduction

Working necessary reduction: retain the full actual affine
projected-line branch of474, with variable coupling, noncomplex
lambda and omega, and nonzero beta. If the contact parameter tau
is noncomplex and \(\mathcal D\tau\ne0\), the high system forces
its contact function to be a complex quadratic. An actual426
reframe then gives the coefficient family
\[
\boxed{\begin{aligned}
s&=r^2/2,&\quad \omega&=w^2/2,&\quad \mu&=-rw,\\
\lambda&=h_0w^2/4+c_1w/2+\lambda_0,\\
k&=-h_0r^2/2+(c_1t+c_0)r-2\lambda_0t^2+Ct+E.
\end{aligned}}
\tag{1}
\]
Here r and w are existing coefficient-field elements, not ambient
coordinates, and all displayed lower-case indexed parameters and
C,E are complex constants. The exact derivative condition
\(\mathcal D\tau=-r\mathcal Dw/w^2\ne0\) is retained.
This is not an exclusion, an actual realization, or a solution of
the remaining full scalar.

## 1. Retained actual scope and the two coefficient fields

Retain every actual264 hypothesis, the genuine296 levels and
primitive minor, and the birational projected-line hypothesis
of325, in the form of the fully read
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
Thus
\[
\begin{gathered}
[L:\mathbb C(t,s)]<\infty,\qquad
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\\
y=\lambda P+r_{\rm old},\quad \theta=\mu P+h,\quad
w_{\rm int}=\omega P^2+w_1P+w_0^{\rm int},\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{2}
\]
The original polynomial four-ring, global slice with
\(X=a_0u_{\rm glob}+x_0\), full initial kernel, selected literal
partial and both returns remain hypotheses. The coefficient
partials commute and have joint constants C. Throughout assume
\[
m=k_s\notin\mathbb C,\qquad
\lambda,\omega\notin\mathbb C,\qquad
\beta=\mathcal Dm\ne0,\qquad
\mathcal D=\partial_t+\mu\partial_s.
\tag{3}
\]
Retain the frozen sums \(\mathcal K_j,\mathcal M_j,\mathcal N_1\)
of474, in particular
\[
B_2=\mathcal M_2/2+m_s\omega,\qquad
C_3=\omega\mathcal N_1+\mathcal M_3/6,
\quad B_2^2=\beta C_3,
\quad \mathcal K_2=-4\lambda-2m\omega.
\tag{4}
\]
They are frozen directional sums, not unrestricted powers of
\(\mathcal D\). The full high system also retains its third and
fourth level coefficients and both differential one-forms.

The fully read
[482](principal-paraboloid-nonzero-direction-contact-reduction-pass482-working.md)
proves that \(q=B_2/\beta\ne0\), and supplies the exact identities
\[
\begin{gathered}
a=1/q,\quad \tau=t+a,\quad
\mathfrak v=\mu+2a\omega,\quad
\mathfrak b=s+a\mu+a^2\omega,\quad
\mathcal H=\beta a-m,\\
2d\lambda=\mathcal H\,d\omega,\qquad
d\mathfrak b=\mathfrak v\,d\tau,\qquad
d\mathfrak v\wedge d\tau=0,\\
d\tau\wedge d\omega
       =\frac{\mathcal D\tau}{a^2}\,dt\wedge ds.
\end{gathered}
\tag{5}
\]
For this note impose exactly
\[
\tau\notin\mathbb C,\qquad \mathcal D\tau\ne0.
\tag{6}
\]
Equation (5) now licenses the separating basis \((\tau,\omega)\).
Neither \((t,\tau)\) nor \((t,\omega)\) is presumed separating.
Let its commuting extended partials be \(\partial_\tau\) and
\(\partial_\omega\), and put
\[
F_\tau=\ker_L\partial_\omega,\qquad
F_\omega=\ker_L\partial_\tau.
\tag{7}
\]
These are exact finite extensions of \(\mathbb C(\tau)\) and
\(\mathbb C(\omega)\), respectively. One proof is to differentiate
the monic minimal polynomial of a constant over
\(\mathbb C(\tau,\omega)\). Minimality forces every coefficient
to be constant for the corresponding derivative. Degrees of finite
constant subextensions are bounded by the degree of L over the
rational two-variable field, since the other parameter remains
transcendental. Their union is therefore finite. The remaining
derivative in each one-variable field has constants exactly C.
No rationality of either field or of L is assumed.

In this basis (5) implies
\[
\mathfrak b,\mathfrak v\in F_\tau,\quad
\mathfrak b_\tau=\mathfrak v,\qquad
\lambda,\mathcal H\in F_\omega,\quad
2\lambda_\omega=\mathcal H.
\tag{8}
\]
For H the field assertion follows by taking the exterior derivative
of \(2d\lambda=\mathcal H d\omega\). Subscripts from now through
Section3 denote these exact partials, unless marked otherwise.

## 2. A closed two-variable system forced by the high coefficients

Define
\[
Z_0=2\omega-\mathfrak v_\tau,
\qquad H_j=\partial_\omega^j\mathcal H\ (j=1,2,3),
\qquad \mathscr K=a(m+\mathcal H)=a^2\beta.
\tag{9}
\]
Both a and \(\mathscr K\) are nonzero. Also \(Z_0\ne0\),
since \((Z_0)_\omega=2\). Solving the contact expressions and
differentiating gives
\[
\begin{gathered}
\mu=\mathfrak v-2a\omega,\qquad
s=\mathfrak b-a\mathfrak v+a^2\omega,\qquad
da=d\tau-dt,\\
ds-\mu\,dt=aZ_0\,d\tau+a^2d\omega,\qquad
\mathcal D\omega=-\frac{Z_0}{a}\mathcal D\tau\ne0,\\
\kappa:=\mathcal D\mu=2\omega-a\mathcal D\omega.
\end{gathered}
\tag{10}
\]
The second line is evaluated on \(\mathcal D\) for its derivative
identity; \(\mathcal Ds=\mu\) and \(\mathcal Dt=1\).

The exact moving-direction relation
\(\mathcal D\beta=\mathcal M_2+\kappa m_s\), together with
\(B_2=\beta/a\), yields
\[
\mathcal D\beta-\frac{2\beta}{a}
                         +a\mathcal D\omega\,m_s=0.
\tag{11}
\]
Here \(m_s\) is the ORIGINAL fixed-t s derivative. On the other
hand \(\beta=(m+\mathcal H)/a\) gives
\[
\mathcal D\beta=\frac{\beta(2-\mathcal D\tau)}a
                          +\frac{H_1\mathcal D\omega}a.
\tag{12}
\]
Substitute (10),(12) in (11), using only the proved nonzero
\(\mathcal D\tau,a,Z_0\). The result is
\[
m+\mathcal H+Z_0H_1+a^2Z_0m_s=0.
\tag{13}
\]
To retain both differential components, use
\(dm=\beta\,dt+m_s(ds-\mu\,dt)\) in the differential of
\(\mathscr K=a(m+\mathcal H)\). Its dt terms cancel because
\(a\beta=m+\mathcal H\). Equation (13) gives exactly
\[
\boxed{\quad
d\mathscr K=-Z_0H_1\,d\tau-\frac{\mathscr K}{Z_0}\,d\omega,
\qquad
\mathscr K_\tau=-Z_0H_1,\quad
\mathscr K_\omega=-\mathscr K/Z_0.
\quad}
\tag{14}
\]
No derivative of H or of the contact function has been divided out.

## 3. The contact function is a complex quadratic

Commuting the two derivatives in (14) gives
\[
\mathscr K\,\mathfrak v_{\tau\tau}
               =Z_0^2(3H_1+Z_0H_2).
\tag{15}
\]
Differentiate this equality in omega and replace
\(\mathscr K_\omega\) by (14). Equivalently, multiply the
derivative of its zero residual by \(Z_0\) and add the residual
itself. Since \((Z_0)_\omega=2\), cancellation gives
\[
15H_1+10Z_0H_2+Z_0^2H_3=0.
\tag{16}
\]
This calculation does not divide by \(\mathfrak v_{\tau\tau}\)
or by any \(H_j\).

Suppose \(\mathfrak v_{\tau\tau}\ne0\). Then
\(\mathfrak v_\tau\) is transcendental over \(F_\omega\).
Indeed, if it were algebraic, apply \(\partial_\tau\) to its
minimal polynomial over \(F_\omega\). Those coefficients are
killed by \(\partial_\tau\), and separability would force
\(\mathfrak v_{\tau\tau}=0\). Thus (16) is a polynomial
identity in \(Z_0=2\omega-\mathfrak v_\tau\), transcendental
over \(F_\omega\). Its coefficients force
\(H_3=H_2=H_1=0\). Equation (15) then contradicts
\(\mathscr K\ne0\) and \(\mathfrak v_{\tau\tau}\ne0\).
It follows that
\[
\mathfrak v_{\tau\tau}=0,\qquad
\mathfrak v=2w_0\tau+v_0,\qquad
\mathfrak b=w_0\tau^2+v_0\tau+b_0,
\qquad w_0,v_0,b_0\in\mathbb C.
\tag{17}
\]
The constants follow by subtraction in the exact \(F_\tau\),
not by assuming it is a rational field.

Now \(Z_0=2(\omega-w_0)\) is independent of tau. Equation
(14) implies \(\mathscr K_{\tau\tau}=0\). The existing elements
\(L_1=\mathscr K_\tau\) and
\(L_0=\mathscr K-\tau\mathscr K_\tau\) belong to \(F_\omega\).
Comparing coefficients of tau gives
\[
\mathscr K=L_1\tau+L_0,\qquad
(L_i)_\omega=-L_i/Z_0\ (i=0,1),\qquad
H_1=-L_1/Z_0.
\tag{18}
\]
This comparison is licensed since \(\partial_\tau\tau=1\),
so tau cannot be algebraic over \(F_\omega\).

At least one \(L_i\) is nonzero. For any nonzero one,
\((L_i^2Z_0)_\omega=0\), so \(L_i^2Z_0=d^2\) for some
\(d\in\mathbb C^*\). The EXISTING element \(w=d/L_i\in F_\omega\)
therefore satisfies \(w^2=Z_0\). No root is adjoined to L.
Moreover \(w_\omega=1/w\), and each \(L_iw\) is complex.
Consequently there are complex constants \(c_1,c_0,h_0,\lambda_0\)
with
\[
\begin{gathered}
w^2=2(\omega-w_0),\quad w\ne0,\qquad
\mathscr K=\frac{c_1\tau+c_0}{w},\qquad
\mathcal H=h_0+\frac{c_1}{w},\\
\lambda=\frac{h_0\omega}{2}+\frac{c_1w}{2}+\lambda_0,\qquad
(c_1,c_0)\ne(0,0),\qquad (h_0,c_1)\ne(0,0).
\end{gathered}
\tag{19}
\]
The first nonzero pair follows from \(\mathscr K\ne0\); the
second follows from noncomplex lambda. Zero \(c_1\) or zero
\(h_0\) is individually permitted. These formulas follow from
existing elements and their derivatives in \(F_\omega\), which
is still not asserted to equal \(\mathbb C(w)\).

## 4. An explicit coefficient basis and the full coupling potential

Set \(r=aw\in L^*\), distinct from the affine intercept
\(r_{\rm old}\) in (2). Equations (10),(17),(19) give
\[
\begin{aligned}
r^2&=2(s-w_0t^2-v_0t-b_0),&
\tau&=t+r/w,\\
\mu&=2w_0t+v_0-rw,&
m&=-h_0+\frac{c_1t+c_0}{r}.
\end{aligned}
\tag{20}
\]
In particular the original \(r_s=1/r\ne0\). Thus \((t,r)\)
is a separating basis and \(L/\mathbb C(t,r)\) is finite.
The exact derivative changes are
\[
\partial_s=\frac1r\partial_r|_t,\qquad
\partial_t|_s=\partial_t|_r-\frac{2w_0t+v_0}{r}\partial_r|_t,
\qquad \mathcal D=\partial_t|_r-w\partial_r|_t.
\tag{21}
\]
These are coefficient-field changes only. They make no claim about
an ambient coordinate r or a rational field L.

Using (20) in \(k_s=m\), subtraction shows that
\(f:=k+h_0s-(c_1t+c_0)r\) is killed by the original s derivative.
Put \(F(t)=f-h_0(w_0t^2+v_0t+b_0)\) for this calculation.
Then
\(k=-h_0r^2/2+(c_1t+c_0)r+F\). Differentiating by (21),
without treating w as a constant, gives
\[
\begin{aligned}
\kappa&=2\omega-r\mathcal Dw,\\
\mathcal K_2&=F_{tt}-2c_1w+2h_0w_0
                           -2\omega(c_1t+c_0)/r,\\
2\lambda+\mathcal K_2/2+m\omega
             &=F_{tt}/2+h_0w_0+2\lambda_0.
\end{aligned}
\tag{22}
\]
Here F is already a function-field constant for \(\partial_r|_t\);
its displayed t derivatives are unambiguous. The defining high
equation forces \(f_{tt}=-4\lambda_0\). Since \(f_s=0\),
exact subtraction and the joint constant field give
\[
k=-h_0s+(c_1t+c_0)r-2\lambda_0t^2+Ct+E,
\qquad C,E\in\mathbb C.
\tag{23}
\]
No primitive outside L and no rationality of \(\ker\partial_s\)
was needed.

## 5. Actual normalization of the quadratic contact function

The constants \(w_0,v_0,b_0\) in (17) can be removed by the
ACTUAL complex polynomial map
\[
X_*=X,\quad Y_*=Y,\quad Z_*=Z,\qquad
W_*=W-v_0Y-w_0Z-b_0X^2.
\tag{24}
\]
Its inverse adds the same displayed polynomial in X,Y,Z to W*.
This is the filtered map of the fully read
[426](general-coupling-normalization-obstruction-pass426-working.md),
with all diagonal scalings one. Its exact transport is
\[
\begin{gathered}
t_*=t,\quad s_*=s-v_0t-w_0t^2-b_0,\quad k_*=k,\quad P_*=P,\\
\lambda_* =\lambda,\qquad
\omega_* =\omega-w_0,\qquad
\mu_* =\mu-v_0-2w_0t,\qquad m_*=m,\quad \mathcal D_* =\mathcal D.
\end{gathered}
\tag{25}
\]
For example the intercept z has leading P coefficient of degree
two equal to one, so subtracting \(w_0Z\) subtracts precisely
\(w_0\) from the quadratic slope of \(w_{\rm int}\).
The literal new partial is
\(\partial_{Z_*}=\partial_Z+w_0\partial_W\), not merely the
old Z partial. The retained shift bound on the W partial gives
\(N_*=N\), so L and rho are unchanged. The full initial ideal,
both actual returns and the calibrated scalar survive by426.
This uses an actual polynomial inverse, not a coefficient-valued
substitution in an ambient frame.

Also \(\beta_* =\beta\), \(\kappa_* =\kappa-2w_0\), and
\((\mathcal M_2)_*=\mathcal M_2+2w_0m_s\). Hence
\((B_2)_*=B_2\), \(q_*=q\), and \(a_*=a,\tau_* =\tau\).
The contact functions transform to
\[
\mathfrak v_* =\mathfrak v-v_0-2w_0\tau=0,\qquad
\mathfrak b_* =\mathfrak b-v_0\tau-w_0\tau^2-b_0=0.
\tag{26}
\]
The existing r and w are unchanged, with \(r^2=2s_*\) and
\(w^2=2\omega_*\). To state the normalized coupling correctly,
the other constants change by
\[
\lambda_{0,*}=\lambda_0+h_0w_0/2,\qquad
C_*=C-h_0v_0,\qquad E_*=E-h_0b_0.
\tag{27}
\]
The constants \(h_0,c_1,c_0\) are unchanged. Dropping stars gives
exactly (1). Formula (1) is not asserted in the old frame without
these transformations.

## 6. Forward high equations and the unsolved scalar

Both before and after (24), the exact directional quantities are
\[
\begin{gathered}
\beta=\frac{c_1r+(c_1t+c_0)w}{r^2}\ne0,\qquad
B_2=\beta\frac wr,\quad C_3=\beta\frac{w^2}{r^2},\quad q=w/r,\\
\mathcal D\tau=-\frac r{w^2}\mathcal Dw\ne0,
\qquad \mathcal D\omega=w\mathcal Dw\ne0,
\qquad \mathcal Dw=w_t-w w_r.
\end{gathered}
\tag{28}
\]
The last t and r derivatives fix the other new coefficient
parameter. All nonzero restrictions in (19),(20),(28) remain
part of the necessary family. They are not automatic properties
of an unspecified arbitrary w. In fact with the nonzero pair
\((c_1,c_0)\), the condition \(\mathcal Dw\ne0\) already
precludes beta zero: if \(c_1=0\), its numerator is \(c_0w\ne0\);
otherwise beta zero would give \(w=-c_1r/(c_1t+c_0)\), whose
displayed directional derivative is zero. No such division is
used when \(c_1=0\).

Direct differentiation of the full family with the ORIGINAL
partials (21) verifies the definition of omega, the third and
fourth high levels, \(B_2^2=\beta C_3\), and all four components
of474's two one-forms. These identities hold algebraically for
arbitrary coefficient w; membership in the present branch still
requires (28). The actual Jacobian condition, however, is only
transported, not solved:
\[
J_{t,r,P}(X)=rJ_{t,s,P}(X)
                       =-\frac{r a_0^4}{\rho}\in L^*.
\tag{29}
\]
The lower potentials, n, ell, moving levels, affine intercepts and
full scalar are not constructed or shown consistent. The required
original-ring returns cannot be inferred from the coefficient
family. Thus no actual realization, recognition, exclusion of this
branch or global cancellation conclusion is claimed.

The complete474,482 and426 sources were read for this reduction.
Fresh unsaved8b2adf rebuilds all fourteen forward residuals,
including the complete high system, the contact expression and
the exact directional derivative of tau. Every residual is zero.
Fresh a62f01 checks the mixed-derivative certificate (15),(16),
both orders of the actual inverse (24), and both contact transports
(26), all zero. The written proof supplies the finite-field,
existing-square-root, nonzero-factor and basis licenses. No saved
checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited while authoring this note.
