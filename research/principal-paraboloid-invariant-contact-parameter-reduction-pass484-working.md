# An invariant contact parameter: exact necessary coefficient family

Working result: retain the actual affine projected-line hypotheses
of474 and the contact reduction of482. Suppose that lambda, omega
and the contact parameter tau are noncomplex, that
\(\beta=\mathcal Dm\ne0\), and that \(\mathcal D\tau=0\).
Then both \((t,\tau)\) and \((t,\omega)\) are separating coefficient
bases. Over the exact field \(F=\ker_L\mathcal D\), the coupling
and its potential have the necessary form
\[
m=m_\circ+\frac{\mathscr K}{\tau-t},\qquad
s=\omega t^2+Mt+\chi,\qquad
k=-2\lambda t^2+A_1t+\phi,
\qquad \mathscr K\in F^*.
\tag{1}
\]
All coefficient relations are recorded below. In particular the
transverse coefficient \(\gamma=A_1'-m_\circ M'\) is nonzero.
This note does not impose or solve the remaining full scalar.

## 1. Retained actual entry and high equations

Retain the complete actual264 entry, the genuine296 levels and
minor units, and the birational projected-line hypothesis of325,
in the form stated in the fully read
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
Thus the original polynomial four-ring, global slice, full initial
kernel, literal selected partial, both original-ring returns and
nonzero calibrated scalar remain hypotheses. In particular,
\[
\begin{gathered}
[L:\mathbb C(t,s)]<\infty,\qquad m=k_s\notin\mathbb C,\\
P=\sigma,\qquad O=L[P],\qquad
y=\lambda P+r,\quad \theta=\mu P+h,\quad NP=\rho\in L^*,\\
w_{\rm int}=\omega P^2+w_1P+w_0,\qquad
J_{t,s,P}(X)=-\frac{a_0^4}{\rho}\in L^*.
\end{gathered}
\tag{2}
\]
The coefficient partials commute and have joint constants
\(\mathbb C\). The intrinsic P is not an actual ambient coordinate
or the original global slice. The original relation
\(X=a_0u_{\rm glob}+x_0\) retains its intercept.

Write \(\mathcal D=\partial_t+\mu\partial_s\), and retain the
frozen Taylor sums of474:
\[
\begin{aligned}
\mathcal K_j&=\sum_{i=0}^j\binom ji\mu^i k_{t^{j-i}s^i}
                                      &&(j=2,3,4),\\
\beta&=m_t+\mu m_s,\qquad
\mathcal M_2=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\\
\mathcal M_3&=m_{ttt}+3\mu m_{tts}+3\mu^2m_{tss}+\mu^3m_{sss},\\
\mathcal N_1&=m_{ts}+\mu m_{ss},\qquad
B_2=\mathcal M_2/2+m_s\omega,\quad
C_3=\omega\mathcal N_1+\mathcal M_3/6.
\end{aligned}
\tag{3}
\]
These are frozen powers of mu, not iterates of \(\mathcal D\).
The high coefficients give
\[
\begin{gathered}
2\lambda+\mathcal K_2/2+m\omega=0,\quad
\beta\omega+\mathcal K_3/6=0,\\
\mathcal K_4/24+\omega\mathcal M_2/2+m_s\omega^2/2=0,\\
2d\lambda+m\,d\omega+\beta(d\mu-2\omega\,dt)
                         +B_2(ds-\mu\,dt)=0,\\
\beta\,d\omega+B_2(d\mu-2\omega\,dt)
                         +C_3(ds-\mu\,dt)=0,\qquad
B_2^2=\beta C_3.
\end{gathered}
\tag{4}
\]
Assume explicitly throughout this note
\[
\lambda,\omega\notin\mathbb C,\qquad \beta\ne0.
\tag{5}
\]
If \(B_2=0\), (4) gives \(C_3=0\) and then \(d\omega=0\),
contrary to (5). Thus \(q=B_2/\beta\ne0\). Put
\[
a=\frac1q,\quad \tau=t+a,\quad
\mathfrak v=\mu+2a\omega,\quad
\mathfrak b=s+a\mu+a^2\omega,\quad
\mathcal H=\beta a-m.
\tag{6}
\]
The fully read
[482](principal-paraboloid-nonzero-direction-contact-reduction-pass482-working.md)
proves directly from (4) that
\[
\begin{gathered}
2d\lambda=\mathcal H\,d\omega,\qquad
d\mathfrak b=\mathfrak v\,d\tau,\qquad
d\mathfrak v\wedge d\tau=0,\\
d\tau\wedge d\omega
       =\frac{\mathcal D\tau}{a^2}\,dt\wedge ds.
\end{gathered}
\tag{7}
\]
The additional branch assumptions here are exactly
\[
\tau\notin\mathbb C,\qquad \mathcal D\tau=0.
\tag{8}
\]
Neither the constant-tau branch nor the branch
\(\mathcal D\tau\ne0\) is treated.

## 2. The separating basis and its exact constant field

First \(\tau_s\ne0\). Otherwise (8) gives \(\tau_t=0\) as
well, contradicting the joint constant field and noncomplex tau.
Therefore \((t,\tau)\) is algebraically independent and separating,
and \(L/\mathbb C(t,\tau)\) is finite. Its exact extended partials
are
\[
\dot{\ }=\partial_t|_\tau=\mathcal D,
\qquad {}'=\partial_\tau|_t=\tau_s^{-1}\partial_s,
\qquad F=\ker_L\mathcal D.
\tag{9}
\]
They commute by uniqueness of extension through a finite separable
field extension. The field F is finite over \(\mathbb C(\tau)\).
Indeed, for a dot-constant, differentiation of its monic minimal
polynomial over \(\mathbb C(t,\tau)\) gives a polynomial of smaller
degree; minimality forces all coefficients to be dot-constant,
hence in \(\mathbb C(\tau)\). Degrees of finite constant
subextensions are bounded by \([L:\mathbb C(t,\tau)]\): t is
transcendental over every algebraic constant extension and adjoining
t preserves its degree. Their union is consequently finite.
The prime derivative preserves F, and its constants in F are
exactly \(\mathbb C\). In particular t is transcendental over F.
No equality \(F=\mathbb C(\tau)\) or \(L=F(t)\) is asserted.

The last identity of (7), together with (8), gives
\(\dot\omega=0\). The first then gives \(\dot\lambda=0\).
The contact identities also give
\(\dot{\mathfrak b}=\dot{\mathfrak v}=0\). Thus
\[
\lambda,\omega,\mathfrak b,\mathfrak v\in F,
\qquad \mathfrak b'=\mathfrak v,
\qquad \Omega:=\omega'\ne0,
\qquad \lambda'\ne0.
\tag{10}
\]
The two nonzero derivatives follow from (5) and the prime constant
field of F. In this basis (7) gives
\[
\mathcal H=\frac{2\lambda'}{\Omega}\in F,
\qquad m_\circ=-\mathcal H=-\frac{2\lambda'}{\Omega}\in F^*.
\tag{11}
\]
Although nonzero here, \(m_\circ\) need not be noncomplex.

## 3. The coupling and the coefficient quadratics

By definition of \(\mathcal H\),
\(a\dot m=m-m_\circ\). Since \(\dot a=-1\), the existing
element
\[
\mathscr K=a(m-m_\circ)=a^2\beta
\tag{12}
\]
has zero dot derivative. It lies in \(F^*\), not just F, by
\(a\ne0\) and \(\beta\ne0\). Consequently
\[
m=m_\circ+\frac{\mathscr K}{a},\qquad
\beta=\frac{\mathscr K}{a^2},\qquad
B_2=\frac{\mathscr K}{a^3},\qquad
C_3=\frac{\mathscr K}{a^4},\qquad a=\tau-t.
\tag{13}
\]
For the last two equalities use \(q=1/a\) and
\(B_2^2=\beta C_3\). No derivative of \(m_\circ\) or of
\(\mathscr K\) is divided out.

Solving (6) and expanding in t gives existing coefficients of F:
\[
\begin{aligned}
M&=\mathfrak v-2\tau\omega,&
\chi&=\mathfrak b-\tau\mathfrak v+\tau^2\omega,\\
s&=\omega t^2+Mt+\chi,&
\mu&=2\omega t+M.
\end{aligned}
\tag{14}
\]
In particular \(\kappa:=\mathcal D\mu=2\omega\).
Actual differentiation of k gives
\(\mathcal D^2k=\mathcal K_2+m\kappa\), so the first
equation of (4) yields \(\mathcal D^2k=-4\lambda\).
Define
\(A_1=\mathcal Dk+4\lambda t\) and
\(\phi=k+2\lambda t^2-A_1t\). Both have zero dot derivative.
This proves, without choosing an external antiderivative,
\[
k=-2\lambda t^2+A_1t+\phi,
\qquad A_1,\phi\in F.
\tag{15}
\]

For a complete coefficient comparison set
\(Z_0=2\omega-\mathfrak v'\in F\). The contact derivative and
the original identity \(k_s=m\) become
\[
\begin{aligned}
\chi'&=-\tau M'-\tau^2\Omega,\\
s'&=a(a\Omega+Z_0)
   =a[-\Omega(t+\tau)-M']\ne0,\\
k'&=m s'.
\end{aligned}
\tag{16}
\]
The nonzero derivative is also \(s'=1/\tau_s\). Both factors
in its displayed factorization are nonzero: a is nonzero, and
\(a\Omega+Z_0\) is a nonzero affine polynomial in t over F,
since \(\Omega\ne0\).

Now expand the last equality of (16) in powers of \(a=\tau-t\):
\[
\begin{aligned}
k'={}&-2\lambda'a^2+(4\tau\lambda'-A_1')a
              -2\tau^2\lambda'+\tau A_1'+\phi',\\
m s'={}&m_\circ\Omega a^2
             +(m_\circ Z_0+\mathscr K\Omega)a+\mathscr K Z_0.
\end{aligned}
\tag{17}
\]
Comparison is valid because t is transcendental over F. The
quadratic coefficient is (11). The other two give exactly
\[
\boxed{\begin{aligned}
2\lambda'+m_\circ\Omega&=0,\\
\chi'&=-\tau M'-\tau^2\Omega,\\
A_1'&=m_\circ M'-\mathscr K\Omega,\\
\phi'&=m_\circ\chi'-\mathscr K(M'+\tau\Omega).
\end{aligned}}
\tag{18}
\]
In particular
\[
\gamma_\tau:=A_1'-m_\circ M'=-\mathscr K\Omega\ne0.
\tag{19}
\]
There is no assumption that \(M',\chi',A_1',\phi'\) are nonzero.

## 4. The omega basis, with derivative notation kept distinct

Equation (10) licenses a second separating basis: the Jacobian
of \((t,\omega)\) against \((t,\tau)\) is \(\Omega\ne0\).
The dot derivative remains \(\mathcal D\). Write
\[
\partial_\omega|_t=\Omega^{-1}\partial_\tau|_t,
\qquad F=\ker_L\mathcal D.
\tag{20}
\]
The same finite-constant-field argument proves that F is finite
over \(\mathbb C(\omega)\). It need not be that rational field.
In this section only, put a subscript omega on this new derivative.
Then
\[
\begin{gathered}
\tau_\omega=\Omega^{-1}\ne0,\qquad
m_\circ=-2\lambda_\omega\ne0,\qquad
\gamma_\omega:=A_{1,\omega}-m_\circ M_\omega
                  =-\mathscr K\ne0,\\
\chi_\omega=-\tau(\tau+M_\omega),\qquad
A_{1,\omega}=m_\circ M_\omega+\gamma_\omega,\\
\phi_\omega=(\gamma_\omega-m_\circ\tau)(\tau+M_\omega).
\end{gathered}
\tag{21}
\]
Here \(\gamma_\omega=\gamma_\tau/\Omega\); neither notation
denotes a derivative of gamma. The same quadratics (14),(15)
remain valid, and their basis derivative is
\[
s_\omega=(t-\tau)(t+\tau+M_\omega)\ne0.
\tag{22}
\]
No division by \(m_{\circ,\omega}\), \(M_\omega\), or either
individual coefficient derivative is licensed or needed.

## 5. Forward high-equation checks and the retained boundary

The formulas above verify the whole high system, not only the
contact equation. To make the check reproducible, use
\(\partial_s=(s')^{-1}\partial_\tau|_t\) and
\(\partial_t|_s=\mathcal D-\mu(s')^{-1}\partial_\tau|_t\).
Equation (17) gives \(k_s=m\), and (14) gives
\(\mathcal D\mu=2\omega\). For the frozen derivatives one has
\[
\begin{aligned}
\mathcal K_2&=-4\lambda-2m\omega,\\
\mathcal K_3&=\mathcal D\mathcal K_2-2\kappa\beta,
&\mathcal K_4&=\mathcal D\mathcal K_3-3\kappa\mathcal M_2,\\
\mathcal M_2&=\mathcal D\beta-\kappa m_s,
&\mathcal M_3&=\mathcal D\mathcal M_2-2\kappa\mathcal N_1,
\qquad \mathcal N_1=\mathcal Dm_s.
\end{aligned}
\tag{23}
\]
Thus \(B_2=\mathcal D\beta/2=\mathscr K/a^3\) and
\(C_3=\mathcal D B_2/3=\mathscr K/a^4\). Substitution in
(4) verifies both high levels and the minor. The dt components
of both forms vanish because \(\mathcal D\lambda=\mathcal D\omega=0\),
\(\mathcal Ds=\mu\), and \(\mathcal D\mu=2\omega\).
Their remaining components are
\[
\begin{aligned}
2\lambda'+m\Omega+\beta\mu'+B_2s'&=0,\\
\beta\Omega+B_2\mu'+C_3s'&=0.
\end{aligned}
\tag{24}
\]
They follow by direct substitution from (13),(14),(16),(18).
These forward identities are statements in the exact field only.

The coefficient changes preserve a nonzero scalar calibration,
not its unscaled value. At fixed intrinsic P and formal X,
\[
J_{t,\tau,P}=s'J_{t,s,P}
        =-\frac{a_0^4s'}{\rho}\in L^*,\qquad
J_{t,\omega,P}=-\frac{a_0^4s_\omega}{\rho}\in L^*.
\tag{25}
\]
Neither this necessary nonzero condition nor the lower coefficients
of the genuine H and Q levels have been solved here. In particular
n, ell, the moving levels, affine intercepts and the lower scalar
remain required. No coefficient-field basis or polynomial in t
has been promoted to an actual complex polynomial coordinate.
The constant-tau and nonzero-\(\mathcal D\tau\) cases remain
outside this note, and no actual realization or recognition is
claimed.

The complete474 and482 sources were read for this reduction.
Fresh unsaved reconstruction514433 checks (16),(17),(19), all
three fractions in (13), the definition of omega, both high levels,
the minor and both transverse one-form components, with every
residual zero. The written argument supplies the separating-basis,
constant-field and zero-denominator licenses; no generic rational
ansatz is used. No saved checker was executed, imported, compiled
or rerun. No earlier source or canonical file was edited.
