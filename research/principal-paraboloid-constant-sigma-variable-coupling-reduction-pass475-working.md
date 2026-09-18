# Constant sigma and variable coupling: an actual-ring reduction

Working result: retain every actual hypothesis of264, suppose the
projected plane curve is a line with function-field projection degree
one, and assume
\[
m=k_s\notin\mathbb C,\qquad \sigma\in L.
\]
Then
\[
\boxed{m_s=0,\qquad
y=-\frac{m_t}{2}\theta+r,\quad r\in L,\qquad n_{ss}=\frac{m_t^2}{2}.}
\tag{1}
\]
If \(m_{tt}=0\), the sliced kernel is a polynomial three-ring. The
remaining necessary family, which is not recognized here, is
\[
k=ms+f,\qquad
n=\frac{m_t^2}{4}s^2+n_1s+n_0,\qquad
m,f,n_1,n_0\in F:=\ker_L\partial_s,\quad m_tm_{tt}\ne0.
\tag{2}
\]
In particular this note excludes the entire \(m_s\ne0\) alternative
under its constant-sigma projected-line assumptions. No factorization
of the third surface potential is assumed.

## 1. Actual entry, exact fields, and the affine parameter

Retain the complete
[264 chart](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine fourth-potential and full-scalar identities of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the projected-line conclusion of
[325](principal-paraboloid-all-specializations-affine-line-profile-pass325-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
a_0=EX\ne0,\quad X=a_0u+x_0,\quad x_0\in A,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
0\ne N=[u^4]\partial_Z|_A\in{\rm LND}(A),\qquad
Na_0=Nt=Ns=0,\qquad L=\operatorname{Frac}\ker_A N,\\
[L:\mathbb C(t,s)]<\infty,\qquad
O=L[v],\quad Nv=1,\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
O=L[y,z,w]=L[y,\sigma,\theta].
\end{gathered}
\tag{3}
\]
The coefficient partials commute and have joint constants \(\mathbb C\).
Every actual return in(3) is retained. A generic parametrization alone
is not a replacement for these assumptions.

Since the projected equation is a line and its projection is
birational,325 gives \(L[\sigma,\theta]=O\) and all three projected
generators are intrinsic-affine. Write
\[
p=\sigma\in L,\qquad V=\theta,\qquad
y=\lambda V+r,\quad \lambda,r\in L,\qquad N\theta\in L^*.
\tag{4}
\]
The coefficient \(\lambda\) may be zero. The parameter \(V\) is not an
ambient coordinate and is not normalized to have \(NV=1\). Changing
from \(v\) to \(V\) gives the exact calibration
\[
J_V(X):=\det\frac{\partial(Y,Z,W)}{\partial(t,s,V)}
       =-\frac{a_0^4}{N\theta}\in L^*.
\tag{5}
\]
All coefficient derivatives below agree with the given derivatives
on \(L\); the displayed intrinsic parameter is held fixed.

The field \(F=\ker_L\partial_s\) is finite over \(\mathbb C(t)\),
relatively algebraically closed in \(L\), and preserved by
\(\partial_t\). For example, differentiating the minimal polynomial
of an \(s\)-constant over \(\mathbb C(t,s)\) shows that its coefficients
lie in \(\mathbb C(t)\). Finite subextension degrees are bounded by
\([L:\mathbb C(t,s)]\), proving finiteness of the full constant field.
Separability proves relative algebraic closedness. Its \(t\)-constants
are the joint constants \(\mathbb C\). No equality \(F=\mathbb C(t)\)
or \(L=F(s)\) is presumed.

## 2. The first scalar factors, including zero slopes

Put \(\gamma=2p+k_t\). The first two potentials give the literal rows
\[
\begin{aligned}
Y&=\lambda V+r+pX+tX^2,\\
Z&=(2t\lambda+m)V+2tr+p^2+k_tp+n+(2tp+k)X+t^2X^2,\\
W&=-\frac{m_s}{2m}V^2+
 \left(X-\frac{\gamma\lambda+m_tp+n_s}{m}\right)V+w_0+sX^2,\\
w_0&=\frac{\ell-\gamma r-k_{tt}p^2/2-n_tp}{m}.
\end{aligned}
\tag{6}
\]
In particular no coefficient derivative of \(p,r,\lambda\) is
discarded. The \(V^3,V^2\) coefficients of the third potential are
\[
\begin{aligned}
[V^3]H(y,p,V)&=\frac{mm_{ss}-3m_s^2}{6m},\\
[V^2]H(y,p,V)&=
\lambda^2+\left(m_t-\frac{\gamma m_s}{m}\right)\lambda
-\frac{3m_s(m_tp+n_s)}{2m}
+\frac{m_{ts}p+n_{ss}}2.
\end{aligned}
\tag{7}
\]
Both vanish. Equivalently the first expression is one third of
\([X^2V^2]J_V\), and the second is one half of \([X^2V]J_V\).
These are consequences of the full actual scalar, not a formal
surface-only assumption.

Define
\[
\eta=-\frac{2m_s}{m^3},\qquad h=\frac1m.
\tag{8}
\]
The first gate in(7) says \(\eta_s=0\), so \(\eta\in F\). After that
gate, direct expansion of the full determinant gives
\[
[V^3]J_V
=-\frac{(\lambda m_s-m\lambda_s)
 (4\lambda m_s-mm_{ts}+3m_sm_t)}{2m^2}.
\tag{9}
\]
If \(m_s\ne0\), the second factor equals
\(m^4(\eta_t-4\eta\lambda/m)/2\). If it vanishes then
\(\lambda/m=\eta_t/(4\eta)\in F\); if the first factor vanishes the
same membership follows directly.

If \(m_s=0\), then \(m_{ts}=0\), and the full determinant instead gives
\[
[XV^2]J_V=-\lambda_s(2\lambda+m_t).
\tag{10}
\]
Either factor's vanishing implies \(\lambda_s=0\), because \(m_t\in F\).
Thus in every case
\[
c:=\lambda/m\in F.
\tag{11}
\]
No division by \(\lambda\) occurred.

## 3. Compact rows and the exceptional scalar column

Use the affine parameter \(R=mV\). Write
\[
B=p^2+k_tp+n,\qquad
j=-\gamma c h-(m_tp+n_s)h^2.
\]
Here \(B\) is a coefficient function, not the ambient ring. The exact
rows and calibration become
\[
\begin{aligned}
Y&=cR+r+pX+tX^2,\\
Z&=(1+2tc)R+2tr+B+(2tp+k)X+t^2X^2,\\
W&=\frac{\eta}{4}R^2+(hX+j)R+w_0+sX^2,\\
\widehat J(X)&=\det\frac{\partial(Y,Z,W)}{\partial(t,s,R)}
             =-\frac{a_0^4}{mN\theta}\in L^* .
\end{aligned}
\tag{12}
\]
The moving-parameter Jacobian is \(mN\theta\), not one. Formal
differentiation of these rows holds \(X,R\) fixed. From the definitions
and the second gate of(7),
\[
\begin{aligned}
h_s&=\frac{\eta}{2h},\\
B_s&=\gamma(p_s-c/h)-j/h^2,\\
j_s&=(2c-h_t/h)(c-hp_s)-\frac{\eta j}{2h^2},\\
[XR^2]\widehat J&=\frac{(\eta_t-4\eta c)(p_s-c/h)}4.
\end{aligned}
\tag{13}
\]

The vanishing of \(p_s-c/h\) requires a separate argument. Suppose
\(p_s=c/h\), and put
\[
\epsilon=r_s+\frac{cj}{h^2},\qquad
\Omega=(w_0)_s+\frac{j^2}{h^2}.
\]
Subtract \(X/h-j/h^2\) times the \(R\)-column from the \(s\)-column
of the full matrix in(12). Equation(13) gives the exact residual
column
\[
(\epsilon,\,2t\epsilon,\,\Omega)^{\mathsf T}.
\tag{14}
\]
The \(X^2\) coefficient of the determinant is
\(-\Omega-\epsilon\gamma h\). Hence
\(\Omega=-\epsilon\gamma h\). If \(\epsilon=0\), the residual
column is zero and the full determinant vanishes. Therefore
\(\epsilon\ne0\). The remaining \(XR\) coefficient is
\[
\epsilon\left(h_t-2ch-\frac{\eta\gamma}{2}\right).
\tag{15}
\]
Its vanishing, differentiated in \(s\) using(13) and
\(\gamma_s=2c/h-h_t/h^2\), gives
\(\eta_t=4\eta c\).
If \(p_s-c/h\ne0\), the same equality follows from(13).
Consequently
\[
\boxed{\eta_t=4\eta c.}
\tag{16}
\]
This includes \(\eta=0\).

For later use, after(16) the complete \(R^2\) coefficient is
\[
[R^2]\widehat J
=-(2c^2-c_t)(p_s-c/h)
       \left(2ch-h_t+\frac{\eta\gamma}{2}\right).
\tag{17}
\]
The coefficient is from the original scalar after the displayed
parameter change, not from a restricted determinant in which moving
coefficient terms were omitted.

## 4. When eta is nonzero, the exceptional column is impossible

Assume \(\eta\ne0\). The following integrations are explicit
subtractions of existing field elements:
\[
h^2=\eta s+b,\qquad
k=\frac{2h}{\eta}+f,\qquad b,f\in F.
\tag{18}
\]
Suppose \(p_s=c/h\). By(15),
\[
p=\frac{2ch}{\eta}-\frac{f_t}{2}.
\tag{19}
\]
Indeed substituting the second formula of(18) into
\(h_t-2ch-\eta(2p+k_t)/2=0\) proves(19).

In this section a prime denotes \(\partial_t\) on \(F\), while every
partial \(t\)-derivative of an element of \(L\) continues to fix \(s\).
Define
\[
d=\frac{b'-4cb}{\eta}\in F,\qquad
h_t=2ch+\frac{\eta d}{2h},\qquad \gamma=d/h.
\]
By(13), \((jh)_s=0\), so \(j=J/h\) for an existing \(J\in F\).
The equation \(B_s=-j/h^2\) similarly gives
\[
B=\frac{2J}{\eta h}+B_0,\qquad B_0\in F.
\tag{20}
\]
No formal antiderivative in \(F\) has been introduced.

Retain the nonzero \(\epsilon\) from(14). After the already proved
upper scalar gates, the full \(X\) and \(R\) coefficients of
\(\widehat J/\epsilon\) are respectively
\[
\begin{aligned}
C_X&=\gamma h p_t-\gamma^2ch-h(2r+B_t)-\gamma j,\\
C_R&=j_t-2cj+\gamma h(c_t-2c^2)-\eta(2r+B_t)/2 .
\end{aligned}
\tag{21}
\]
Both must vanish. Substituting(19),(20) into \(C_X=0\) gives
\[
\begin{aligned}
r&=r_0+r_1/h,\\
r_0&=\frac{d(c'-2c^2)}{\eta}-\frac{B_0'}2,\\
r_1&=-\frac{df''}{4}-\frac{J'-6cJ}{\eta}.
\end{aligned}
\tag{22}
\]
Substitution into the other coefficient gives exactly
\[
C_R=\frac{J'-4cJ+\eta df''/4}{h}.
\tag{23}
\]
Thus \(r_1=2cJ/\eta\). But now
\[
\epsilon=r_s+cj/h^2
=\frac{-\eta r_1/2+cJ}{h^3}=0,
\]
contradicting(14). This proves, whenever \(\eta\ne0\),
\[
p_s-c/h\ne0.
\tag{24}
\]
The proof allows \(c=0\), \(d=0\), \(J=0\), and \(r_1=0\).

Put
\(\chi=p-2ch/\eta+f'/2\). Equations(18) imply
\(\chi_s=p_s-c/h\) and
\(2ch-h_t+\eta\gamma/2=\eta\chi\).
If \(2c^2-c_t\ne0\), equation(17) and(24) force \(\chi=0\),
contradicting \(\chi_s\ne0\). Therefore
\[
c_t=2c^2.
\tag{25}
\]

The zero solution \(c=0\) still needs exclusion. In that case(16)
makes \(\eta\in\mathbb C^*\). Put
\[
Y_t=r_t+p_tX+X^2,\qquad Y_s=r_s+p_sX,\qquad
L_0=\eta\gamma/2-h_t,\quad K_0=\eta(2r+B_t)/2-j_t.
\]
Using(13), the full \(R\) coefficient of the determinant is
\[
[R]\widehat J=L_0p_sY_t-(L_0X+K_0)Y_s.
\tag{26}
\]
The polynomial \(Y_s\) cannot vanish identically: otherwise the full
determinant has the nonunit monic quadratic factor \(Y_t\).
If \(L_0\ne0\) and \(p_s=0\), equation(26) immediately contradicts
\(Y_s\ne0\). If \(L_0p_s\ne0\), the root of the linear \(Y_s\)
is also a root of \(Y_t\); at that \(X\) the entire first
differential row vanishes, since \(Y_R=c=0\).
The nonzero constant determinant forbids this too. Thus \(L_0=0\).
By(18), this says \(p=-f'/2\), hence \(p_s=0=c/h\), contradicting(24).

For the remaining nonzero solution of(25),
\[
T=t-\tau,\qquad
c=-\frac1{2T},\qquad
\eta=\frac{\eta_0}{T^2},\qquad
\tau\in\mathbb C,\quad \eta_0\in\mathbb C^*.
\tag{27}
\]
For example \(\tau=t+1/(2c)\) and \(\eta_0=\eta T^2\) are existing
elements killed by both partials. This is exact finite-field
integration, not a rational-field ansatz.

## 5. An actual plane-nice lemma and denominator contraction

Extend \(N\) to \(\mathcal B=A[u]\) by \(Nu=0\), and define the
actual polynomial derivation
\[
\mathcal D=a_0N-(NX)E.
\tag{28}
\]
It fixes \(X\), commutes with \(E\), and on
\(\mathcal B_{a_0}=A_{a_0}[X]\) acts as \(a_0N\) at fixed \(X\).
It is locally nilpotent there, because \(Na_0=0\), and hence on
the stable original ring. In particular it kills \(L\) on the
fraction field and \(\mathcal DR=a_0mN\theta\ne0\).
No division by this speed in the original ring is asserted.

Here is the precise plane lemma. Suppose a polynomial LND on an
actual four-ring fixes an actual coordinate pair \(X,Z_*\), and its
square kills the other coordinates \(Y_*,W_*\), with
\(\mathcal DY_*\ne0\). Then
\[
\frac{\mathcal DW_*}{\mathcal DY_*}\in\mathbb C(X,Z_*).
\tag{29}
\]
To prove this, localize at the fixed-pair fraction field and pass to
its algebraic closure. Every nonzero orbit in the remaining plane
is the entire affine line
\((Y_*,W_*)+u(\mathcal DY_*,\mathcal DW_*)\):
the exponential truncates, and both velocities are constant on it.
Two such nonparallel lines intersect. At the intersection the
velocity must equal each line's constant velocity, a contradiction.
Thus the ratio is constant on the plane and belongs to the original
coefficient field. The argument allows the second velocity to be
zero and uses only the dense open set where the first is nonzero.
One can alternatively take a primitive gcd and use
[Dasgupta--Gupta, Lemma2.3(ii)](https://arxiv.org/html/1701.03635v1).

Suppose in addition that the ratio in(29) belongs to \(L[X]\), and
every nonconstant polynomial in the fixed pair has positive
\(E\)-degree. Write the ratio in reduced form \(P/Q\) over
\(\mathbb C[X,Z_*]\). Membership in
\(L[X]\subset\operatorname{Frac}(A)[X]=(A\setminus0)^{-1}\mathcal B\)
clears a denominator \(a\in A\setminus0\). Each irreducible factor of
\(Q\) remains prime in the actual four-ring, is coprime to \(P\),
and therefore divides \(a\). Additivity of locally nilpotent degree
forces that factor to have \(E\)-degree zero, a contradiction.
Consequently
\[
\frac{\mathcal DW_*}{\mathcal DY_*}\in\mathbb C[X,Z_*].
\tag{30}
\]
This argument does not invert \(EX\) or the velocity as an ambient
unit, and does not presume that adjoining a field preserves normality.

## 6. Exclude the last nonzero-eta family in an actual frame

Under(27), make the complex polynomial automorphism
\[
Y_*=Y-\tau X^2,\qquad
Z_*=Z-2\tau Y+\tau^2X^2,\qquad
W_*=W-\eta_0Y_*^2,
\tag{31}
\]
fixing \(X\). Its explicit inverse is
\[
Y=Y_*+\tau X^2,\qquad
Z=Z_*+2\tau Y_*+\tau^2X^2,\qquad
W=W_*+\eta_0Y_*^2.
\tag{32}
\]
The final shear can raise the \(E\)-degree of \(W_*\) to four.
We do not claim it preserves the full1222 chart or its four-generator
initial kernel. Only the actual frame and the fixed-pair leading
injection below are needed.

The \(R\)-coefficients of \(Y_*,Z_*\) are \(c,0\).
The quadratic \(R\)-coefficient of \(W_*\) vanishes because
\(\eta/4=\eta_0c^2\). Thus
\(\mathcal D\) fixes \(X,Z_*\), has \(\mathcal DY_*\ne0\), and
\(\mathcal D^2Y_*=\mathcal D^2W_*=0\). Direct substitution gives
\[
\frac{\mathcal DW_*}{\mathcal DY_*}
=\frac{hX+j}{c}-2\eta_0(r+pX+TX^2)\in L[X],
\qquad [X^2]=-2\eta_0T\ne0.
\tag{33}
\]

The leading forms of \(X,Z_*\) are \(a_0u\) and
\(T^2(a_0u)^2\). Their polynomial map over \(\mathbb C\) is
injective, since \(T\) is transcendental over \(\mathbb C\).
Hence every nonconstant fixed-pair polynomial has positive
\(E\)-degree, and its \(E\)-degree equals its weighted degree for
weights \((1,2)\). Equations(29),(30) now show that the ratio in(33)
is a complex polynomial in \(X,Z_*\) of weighted degree two. It is
therefore
\(\alpha Z_*+\beta X^2+\gamma_1X+\gamma_0\), with complex constants.
Comparing its literal \(X^2\) coefficient yields
\[
\alpha T^2+\beta=-2\eta_0T,
\tag{34}
\]
impossible for transcendental \(T\) and \(\eta_0\ne0\).
Together with Sections4--5, this excludes every \(\eta\ne0\)
case. By(8),
\[
m_s=0.
\tag{35}
\]

## 7. The surviving t-only coupling and its Riccati boundary

Now \(m\in F\). Since it is not complex, \(m_t\ne0\).
If \(c=0\), formula(26) remains valid with \(\eta=0\), and the same
nonunit-factor/common-root proof forces \(L_0=-h_t=0\).
This contradicts \(m_t\ne0\). Thus \(c\ne0\).

Equation(17) now reads
\[
(2c^2-c_t)(c-hp_s)(2c-h_t/h)=0.
\tag{36}
\]
If \(p_s=c/h\), equation(15) and its nonzero \(\epsilon\) still
force \(2c-h_t/h=0\). Therefore the exhaustive necessary split is
\[
c_t=2c^2\qquad\text{or}\qquad
2c-h_t/h=0.
\tag{37}
\]
In the second case \(\lambda=mc=-m_t/2\) already.

In the first case, \(c\ne0\) gives \(c=-1/(2T)\) with
\(T=t-\tau\), \(\tau\in\mathbb C\). Use the first two actual changes
in(31), but keep \(W_*=W\); here \(\eta=0\).
Again \(\mathcal D\) fixes \(X,Z_*\), and its square kills
\(Y_*,W\). This time
\[
\frac{\mathcal DW}{\mathcal DY_*}=\frac{hX+j}{c}\in L[X]
\tag{38}
\]
has exact \(X\)-degree one. The same plane and denominator arguments
make it \(\alpha X+\beta\), with \(\alpha\in\mathbb C^*\) and
\(\beta\in\mathbb C\). Hence
\[
m=-\frac{2T}{\alpha},\qquad
\lambda=-m_t/2,\qquad
u_0:=j/h=\beta/\alpha\in\mathbb C.
\tag{39}
\]
Thus both cases of(37) prove the slope assertion in(1).
Substituting it into(7) gives \(n_{ss}=m_t^2/2\).
Subtracting the indicated polynomials in \(s\) gives exactly(2),
except for the \(m_{tt}\ne0\) restriction handled next.

## 8. Recognition when m is complex affine

Suppose \(m_{tt}=0\). Then \(m=at+d\), with
\(a,d\in\mathbb C\) and \(a\ne0\), because \(m\) is variable.
The proved slope makes \(c=-a/(2m)\), so \(c_t=2c^2\).
The argument of(38),(39) applies and supplies \(u_0\in\mathbb C\).
With \(\tau_0=a_0N\theta\in L^*\), the full actual velocity row is
\[
\mathcal DX=0,\quad
\mathcal DY=-a\tau_0/2,\quad
\mathcal DZ=d\tau_0,\quad
\mathcal DW=(X+u_0)\tau_0.
\tag{40}
\]
This was derived without a reducible-surface hypothesis.

Set
\[
U_0=Z+2dY/a,\qquad V_0=W+2(X+u_0)Y/a .
\tag{41}
\]
These are actual complex polynomial coordinates together with \(X,Y\):
the inverse solves \(Z=U_0-2dY/a\) and
\(W=V_0-2(X+u_0)Y/a\). The derivation fixes
\(S=\mathbb C[X,U_0,V_0]\), and its only remaining coordinate velocity
is nonzero. Hence \(\ker_{\mathcal B}\mathcal D=S\).
Commutation implies \(E(S)\subset S\), with
\(EX=a_0\ne0\), \(E^2X=0\).

For completeness, divide the restriction \(E|_S\) by the gcd of its
three coordinate coefficients. The gcd divides \(a_0\); additive
locally nilpotent degree makes it invariant. The resulting derivation
is polynomial, irreducible, locally nilpotent, and still has the
genuine coordinate \(X\) as a nonzero degree-one element.
[Dasgupta--Gupta Theorem4.8](https://arxiv.org/html/1701.03635v1)
then supplies an invariant coordinate of \(S\), which is an actual
coordinate of \(\mathcal B=S[Y]\). The global slice makes \(A\)
affine and regular, so
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
gives \(A\cong\mathbb C^{[3]}\).
These are the same precise endpoint steps as
[313, Sections5--6](principal-paraboloid-constant-sigma-reducible-line-recognition-pass313-working.md);
only that source's general actual-ring endpoint is used, not its
factorization assumptions or its derivation of(40).

## 9. Scope and verification boundary

The conclusion is(1), recognition of its \(m_{tt}=0\) subcase, and the
remaining necessary family(2). The case \(m_{tt}\ne0\) is not excluded
or recognized. No rationality of \(F\), no equality \(L=F(s)\), and no
ambient coordinate status of \(\theta,R,h,p\) is asserted.
Neither the full genuine fourth potential nor any lower scalar
constraint is replaced by a freely chosen polynomial relation.
The proof extracts necessary coefficients from the actual determinant.

Complete264,296,325 and313 were read through EOF. The writing guide
was reread before authoring. Fresh unsaved reconstruction30cc3d/96d812
checks the raw determinant coefficients; f34f06 and d73290 check the
compact scalar and every zero-slope factor; bf9a69 checks both complete
lower exceptional-column equations and their final contradiction.
The independent reconstruction6257ad checks the actual shears, fixed
coordinates, squared-derivation identities, velocity ratios and their
leading coefficients. The primary statements cited in Section8 and
the alternative plane lemma were freshly inspected.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical file was edited. This is a bounded
working result, not a realization claim, an arbitrary-coordinate
entry theorem, an unrestricted cancellation solution, or a claim
of novelty or formal certification.
