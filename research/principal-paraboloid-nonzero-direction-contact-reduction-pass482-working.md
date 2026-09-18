# Nonzero-direction contact reduction and exact high-equation controls

Working result: within the full actual affine projected-line branch
of474, assume that \(\omega\) is noncomplex and
\(\beta=(\partial_t+\mu\partial_s)m\ne0\). Its high system gives
the exact contact identity
\[
d\mathfrak b=\mathfrak v\,d\tau,
\qquad
\tau=t+\frac1q,\quad
\mathfrak v=\mu+\frac{2\omega}{q},\quad
\mathfrak b=s+\frac{\mu}{q}+\frac{\omega}{q^2},
\qquad q=\frac{B_2}{\beta}\ne0.
\tag{1}
\]
The zero-\(d\tau\) branch is retained. Two explicit formal controls
satisfy the complete high system but prevent stronger conclusions
about constant lambda or separating parameters from that system
alone. Neither control is an actual-chart realization.

## 1. Retained actual scope and the zero-safe quotient

Retain the complete actual264 hypotheses, the genuine296 levels
and evaluated minor units, and the birational projected-line
assumption of325, as in the fully read
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
In particular the original polynomial four-ring, global slice,
literal selected partial, full initial kernel, both returns and
nonzero calibrated scalar remain required. Here
\[
P=\sigma,\qquad
y=\lambda P+r,\qquad \theta=\mu P+h,\qquad
w_{\rm int}=\omega P^2+w_1P+w_0,\qquad NP\in L^*,
\tag{2}
\]
with \([L:\mathbb C(t,s)]<\infty\). The two coefficient partials
commute and have joint constant field \(\mathbb C\).
The intrinsic parameter is not an ambient coordinate.
Assume explicitly
\[
m=k_s\notin\mathbb C,\qquad
\omega\notin\mathbb C,\qquad \beta\ne0.
\tag{3}
\]
No exclusion of beta zero is needed as a dependency for this note.

Write \(\mathcal D=\partial_t+\mu\partial_s\) and retain474's
frozen Taylor expressions
\[
\begin{aligned}
\mathcal K_j&=\sum_{i=0}^j\binom ji
       \mu^i k_{t^{j-i}s^i}\quad(j=2,3,4),\\
\mathcal M_2&=m_{tt}+2\mu m_{ts}+\mu^2m_{ss},\\
\mathcal M_3&=m_{ttt}+3\mu m_{tts}+3\mu^2m_{tss}+\mu^3m_{sss},\\
\mathcal N_1&=m_{ts}+\mu m_{ss},\\
B_2&=\mathcal M_2/2+m_s\omega,\qquad
C_3=\omega\mathcal N_1+\mathcal M_3/6.
\end{aligned}
\tag{4}
\]
These are frozen powers of mu, not iterates of \(\mathcal D\).
The complete high constraints used below are
\[
\begin{gathered}
2\lambda+\mathcal K_2/2+m\omega=0,\qquad
\beta\omega+\mathcal K_3/6=0,\\
\mathcal K_4/24+\omega\mathcal M_2/2+m_s\omega^2/2=0,\\
2d\lambda+m\,d\omega+\beta(d\mu-2\omega\,dt)
                      +B_2(ds-\mu\,dt)=0,\\
\beta\,d\omega+B_2(d\mu-2\omega\,dt)
                      +C_3(ds-\mu\,dt)=0,\qquad B_2^2=\beta C_3.
\end{gathered}
\tag{5}
\]
The differential forms are identities over the exact field L.
They retain the genuine-potential origin established in474.

If \(B_2=0\), the minor relation and \(\beta\ne0\) give \(C_3=0\).
The second form would then give \(d\omega=0\), contradicting(3).
Thus \(q=B_2/\beta\ne0\), and \(C_3=\beta q^2\).
Dividing only by these proved nonzero quantities gives
\[
\begin{aligned}
2d\lambda&=\mathcal H\,d\omega,\qquad
               \mathcal H=\frac{\beta}{q}-m,\\
d\omega+q\,d\mu+q^2(ds-\mu\,dt)-2q\omega\,dt&=0.
\end{aligned}
\tag{6}
\]
There is no division by lambda, \(\mathcal H\), a derivative of
omega, or a derivative of q.

## 2. The contact identity and its two branches

Put \(a=1/q\), so \(a\ne0\). Multiplying the second form in(6)
by \(a^2\) gives
\[
ds=(\mu+2a\omega)\,dt-a\,d\mu-a^2d\omega.
\tag{7}
\]
Define existing elements of L by
\[
\tau=t+a,\qquad
\mathfrak v=\mu+2a\omega,\qquad
\mathfrak b=s+a\mu+a^2\omega.
\tag{8}
\]
Differentiating the last expression and using(7) gives exactly
\[
d\mathfrak b=\mathfrak v\,d\tau,\qquad
d\mathfrak v\wedge d\tau=0.
\tag{9}
\]
The second identity is the exterior derivative of the first.
These transformations are coefficient-field expressions only.

If \(d\tau=0\), the joint constants give
\[
\tau=\tau_0\in\mathbb C,\qquad
q=\frac1{\tau_0-t},\qquad
\mathfrak b=b_0\in\mathbb C.
\tag{10}
\]
Equation(9) gives no constancy conclusion for \(\mathfrak v\).
The denominator in(10) is nonzero because it equals a.
The exact remaining expressions are
\[
\mu=\mathfrak v-2(\tau_0-t)\omega,\qquad
s=b_0-(\tau_0-t)\mathfrak v+(\tau_0-t)^2\omega.
\tag{11}
\]
The second control below shows why the missing constancy assertion
for \(\mathfrak v\) cannot be added from the high equations.

Now suppose \(d\tau\ne0\). Choose \(x\) from \(\{t,s\}\) such
that \(dx\wedge d\tau\ne0\). Then \((x,\tau)\) is a separating
basis and \(L/\mathbb C(x,\tau)\) is finite. Let
\[
F_\tau=\ker_L(\partial_x|_\tau).
\]
This field is finite over \(\mathbb C(\tau)\). To see this,
differentiate the monic minimal polynomial of an x-constant over
\(\mathbb C(x,\tau)\): minimality forces all coefficients to be
x-constant, hence in \(\mathbb C(\tau)\). Degrees of finite
constant subextensions are bounded by \([L:\mathbb C(x,\tau)]\),
since x remains transcendental over their algebraic constant
extension. Their union is therefore finite as well.
The other extended partial preserves this field by commutation.

Equations(9) now imply
\[
\mathfrak b,\mathfrak v\in F_\tau,\qquad
\frac{d\mathfrak b}{d\tau}=\mathfrak v.
\tag{12}
\]
The equality is in the exact finite function field, not necessarily
the rational field \(\mathbb C(\tau)\). Thus(8) can be written
\[
\mu=\mathfrak b'(\tau)-2(\tau-t)\omega,\qquad
s=\mathfrak b(\tau)-(\tau-t)\mathfrak b'(\tau)
                              +(\tau-t)^2\omega,
\tag{13}
\]
where the notation denotes existing elements of \(F_\tau\).
It neither chooses a new antiderivative nor asserts that
\((t,\tau)\) is a separating basis.

For an explicit additional basis test, (8),(9) give
\[
d\tau\wedge d\omega
       =\frac{\mathcal D\tau}{a^2}\,dt\wedge ds.
\tag{14}
\]
Indeed differentiate \(s=\mathfrak b-a\mathfrak v+a^2\omega\),
wedge with \(d\tau\), and use \(da=d\tau-dt\) and(9).
Consequently \((\tau,\omega)\) is separating precisely when
\(\mathcal D\tau\ne0\). No such nonzero condition has been
established in general.

## 3. Lambda and the second auxiliary coefficient

The first form in(6), followed by its exterior derivative, gives
\[
d\lambda\wedge d\omega=0,\qquad
d\mathcal H\wedge d\omega=0.
\tag{15}
\]
Since omega is noncomplex, the same separating-basis argument as
in Section2 defines a finite field \(F_\omega/\mathbb C(\omega)\)
containing both lambda and \(\mathcal H\), with
\[
2\,\frac{d\lambda}{d\omega}=\mathcal H.
\tag{16}
\]
In particular
\[
\lambda\in\mathbb C\quad\Longleftrightarrow\quad\mathcal H=0.
\tag{17}
\]
This is a necessary equivalence, not an exclusion of that branch.
Also \(m+\mathcal H=\beta/q\ne0\). Neither q nor
\(\mathcal H\) is known to be noncomplex, so neither can
automatically be chosen as a coefficient parameter.

## 4. A control with both q and the auxiliary coefficient constant

Let d be any complex constant and use the exact finite extension
\[
L=\mathbb C(t,z),\qquad s=z^2,\qquad
\partial_t=\partial/\partial t,\qquad
\partial_s=\frac1{2z}\partial/\partial z.
\]
Its commuting partials have joint constants \(\mathbb C\).
Set
\[
k=ds+2z,\quad m=d+\frac1z,\quad
\mu=-2s,\quad \lambda=-\frac{ds}{2},\quad \omega=s.
\tag{18}
\]
Here m and omega are noncomplex and \(\beta=1/z\ne0\).
Direct differentiation gives the complete relevant jet ledger
\[
\begin{array}{c|cccccccc}
 &\mathcal K_2&\mathcal K_3&\mathcal K_4&
 \mathcal M_2&\mathcal M_3&\mathcal N_1&B_2&C_3\\ \hline
\text{value}&-2z&-6z&-30z&3/z&15/z&-3/(2z^3)&1/z&1/z .
\end{array}
\tag{19}
\]
It follows directly that the definition of omega, both high levels,
the minor identity and all four differential-form components in(5)
vanish exactly. There is no restriction on d needed for those
identities. The contact and auxiliary quantities are
\[
q=1,\quad a=1,\quad \mathcal H=-d,\quad
\tau=t+1,\quad \mathfrak v=0,\quad \mathfrak b=0.
\tag{20}
\]
For \(d=0\), lambda is a complex constant while omega is not.
For \(d\ne0\), lambda is noncomplex, but both q and
\(\mathcal H\) remain complex constants. Even though tau is
noncomplex, \((t,\tau)\) is algebraically dependent.
Thus all three proposed automatic parameter licenses fail at
the level of(5).

## 5. A constant-tau control with nonconstant contact derivative

Use \(L=\mathbb C(t,s)\) with its usual partials, and put
\[
k=s+\frac{s}{t},\quad m=1+\frac1t,\quad
\mu=\frac{s}{t}+t^2,\quad
\lambda=-\frac t2,\quad \omega=t.
\tag{21}
\]
These are exact field elements; t is nonzero. Here
\[
\begin{array}{c|ccccccccc}
 &\beta&\mathcal K_2&\mathcal K_3&\mathcal K_4&
 \mathcal M_2&\mathcal M_3&\mathcal N_1&B_2&C_3\\ \hline
\text{value}&-1/t^2&-2&6/t&-24/t^2&
 2/t^3&-6/t^4&0&1/t^3&-1/t^4 .
\end{array}
\tag{22}
\]
Substitution again verifies every equation and every form component
in(5). The derived quantities are
\[
q=-1/t,\quad a=-t,\quad \mathcal H=-1,\quad
\tau=0,\quad \mathfrak b=0,\quad
\mathfrak v=\frac{s}{t}-t^2.
\tag{23}
\]
In particular \(\mathfrak v\) is noncomplex despite constant tau
and constant \(\mathfrak b\). Also \(\omega_s=0\), so
\((t,\omega)\) is not separating; neither is \((t,q)\).
No transverse nonzero derivative has been silently assumed.

## 6. What these controls do not show

Sections4--5 construct exact solutions of the displayed high
coefficient system only. They do not specify n, ell, either moving
level, the affine intercepts, the lower genuine potential equations,
or the required nonzero original scalar. They do not construct
complex polynomial coordinates, a global slice, the prescribed
full initial kernel, the selected locally nilpotent derivation,
or either original-ring return. Thus they are not counterexamples
to an exclusion proved using any of those additional actual
hypotheses, and are not realizations of the present chart.

The positive conclusion of this note is the exact contact and
finite-field reduction (9)--(17), with both zero and nonzero
\(d\tau\) cases retained. It does not settle the remaining actual
nonzero-beta branch or give a global cancellation claim.

The complete474 source was read before this work. Fresh unsaved
reconstruction efe573 verifies the universal contact identity and,
for each control, the definition of omega, both high levels, the
minor, all four high one-form components, and both components
of the contact identity. The controls are exact identities, not
finite numerical sampling. The coefficient-field proofs above
give the separating and constant-field licenses.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. No actual realization,
formal certification or historical-novelty claim is made.
