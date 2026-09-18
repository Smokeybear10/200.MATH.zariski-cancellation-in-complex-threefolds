# Fifth-root reduction for a nondegenerate projected conic

Working necessary result: retain the full actual principal chart264,
assume \(m=k_s\) is variable with \(m_s=0\), and let sigma be affine
nonconstant on the intrinsic line. Suppose theta has exact degree two,
\(S=\sigma^2+k_t\sigma+m\theta\) has exact degree two, and
\(m_{tt}\ne0\). Then there are complex constants
\(\tau,d,C\), with \(C\ne0\), and an EXISTING coefficient element u
such that
\[
\boxed{
u^5=t-\tau,\qquad
m=d(t-\tau)+Cu^4,\qquad
[\sigma^2]\theta=-\frac5{Cu^4}.
}
\tag{1}
\]
This is a necessary coefficient family, not an ambient normalization,
an actual realization, recognition, or an exclusion of this family.
The \(m_{tt}=0\) branch and the degree-drop case \(\deg S<2\)
are outside the result. No factorization of the genuine surface
level is assumed.

## 1. Full actual input and the precise unsolved subcase

Retain the actual hypotheses of the completely read
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine fourth potential and unit-minor theorem of the
completely read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the degree sector of the completely read
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad
E=\partial_{u_{\rm glob}},\qquad X=a_0u_{\rm glob}+x_0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(X^2Z-Y^2)\ \hbox{is the full initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\qquad
Na_0=Nt=Ns=0,\qquad [L:\mathbb C(t,s)]<\infty,\\
L=\operatorname{Frac}\ker_A N,\qquad
O=L[v],\ Nv=1,\qquad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{2}
\]
The actual whole return is \(L[y,z,w]=L[y,\sigma,\theta]=O\);
the all-X return retained in327 is \(L[X,Y,Z,W]=L[X,v]\).
The original slice, literal selected partial, both returns and
nonzero calibrated scalar are not replaced by a formal polynomial
parametrization.

Assume
\[
m=k_s\ne0,\quad m_s=0,\quad m\notin\mathbb C,\quad
p=m_t,\quad q=m_{tt}\ne0,\quad j=m_{ttt}.
\tag{3}
\]
The exact joint constants in L are C, so \(p\ne0\).
Write \(P=\sigma\); since sigma is affine nonconstant in v,
\[
O=L[P],\qquad NP=\rho\in L^*.
\]
The changes from v to P are coefficient and intrinsic parameter
changes only. Coefficient derivatives on L are still the original
commuting \(\partial_t,\partial_s\), extended to fix P when forming
the moving-parameter determinant.

Write
\[
\theta=aP^2+bP+c,\qquad a\ne0,\qquad
\delta=1+ma\ne0.
\tag{4}
\]
The last condition is precisely \(\deg_P S=2\).
The parity criterion327 and its monic-surface degree bound give
\[
y=-\frac p2\theta+\lambda P+r,\qquad
\lambda,r\in L.
\tag{5}
\]
Indeed327 first forces the cubic coefficient of y to vanish when
\(m_s=0\), and forces its quadratic coefficient to be \(-pa/2\).
Subtracting \(-p\theta/2\) then leaves an affine polynomial in P.
This argument does not select a surface factor.

The previously read306,323,324 already handle the reducible-surface
genuine-conic sector. Their reciprocal-coupling formulas are NOT used
here. In particular the argument below applies to the remaining
irreducible-level case, without assuming that irreducibility supplies
any additional coefficient equation.

## 2. Full literal rows and reconstructible scalar coefficients

All lower coefficient functions and their moving derivatives are
retained. The literal264 map is
\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{6}
\]
Its second potential, after only (5), reads
\[
w=\frac1m\left[
 \left(\frac{pk_t}{2}-n_s\right)\theta
 -(2\lambda+k_{tt}/2)P^2
 -(2r+k_t\lambda+n_t)P+\ell-k_tr
\right].
\tag{7}
\]
In particular its entire P-cubed coefficient cancels. This explains
why every literal coordinate in (6) has P-degree at most two, but
does not supply any new actual invariant coordinate.

Define J by taking the FULL derivative matrix of (6), with columns
\((\partial_t|_{s,P},\partial_s|_{t,P},\partial_P)\), including all
derivatives of \(a,b,c,\lambda,r,n,\ell,k\). The exact scalar is
\[
J(X,P)=-\frac{a_0^4}{\rho}\in L^*.
\tag{8}
\]
Every coefficient of a positive X or P power is therefore zero.
No coefficient-field derivative of this scalar is set to zero.

Direct expansion of this matrix gives
\[
\begin{aligned}
[X^2P^3]J&=-a\{ap^2-2a n_{ss}-2q\},\\
[XP^5]J&=a a_s q.
\end{aligned}
\tag{9}
\]
Thus, using only the proved nonzero a and assumed nonzero q,
\[
n_{ss}=\frac{p^2}{2}-\frac qa,\qquad a_s=0.
\tag{10}
\]
The second equality is not asserted in the separate \(q=0\) branch.

For an economical record of the next two FULL scalar coefficients put
\[
\mathcal R=
3ak_tp^2-3ak_{tt}mp+6am n_{ts}-6a n_sp
                   -3k_{tt}p+mk_{ttt}.
\tag{11}
\]
After (10), the same complete determinant gives
\[
\begin{aligned}
[X^2P^2]J&=\frac{\mathcal R-3bmq-12p\lambda}{2m},\\
[XP^4]J&=
\frac q{2m}\{ma_t+2am b_s-2ap(1+ma)\}
                      +\frac{4ap}{m}\lambda_s.
\end{aligned}
\tag{12}
\]
All displayed derivatives are of the actual coefficient functions.
Equations (6),(7) define the entire determinant, including its
unprinted lower coefficients; no lower potential has been specialized.

The first equation of (12) gives a genuine identity
\(12p\lambda=\mathcal R-3bmq\). Differentiate it in s.
Because \(a_s=m_s=p_s=q_s=0\), and coefficient derivatives commute,
\[
\begin{aligned}
\mathcal R_s
={}&3ap^3-3ampq+6am(n_{ss})_t-6ap n_{ss}-3pq+mj\\
={}&3ampq-5mj+6mq\,a_t/a+3pq,\\
12p\lambda_s&=\mathcal R_s-3mq b_s.
\end{aligned}
\tag{13}
\]
Substitution into the second equation of (12) gives exactly
\[
[XP^4]J=\frac56(3q a_t-2aj),\qquad
3q a_t-2aj=0.
\tag{14}
\]
This is differentiation of a field identity, not an unsupported
comparison of coefficients in the moving variable s. It implies
\((a^3/q^2)_t=(a^3/q^2)_s=0\), hence \(a^3/q^2\in\mathbb C^*\).

## 3. The genuine primitive minor supplies the second equation

Use independent formal variables U,P,V. In the present \(m_s=0\)
case the full296 objects are
\[
\begin{aligned}
F&=k_{tt}P^2/2+pPV+n_tP+n_sV,\qquad
g=\{\ell-(2P+k_t)U-F\}/m,\\
H&=U^2+F_PU+F_Vg+H_3(k;P,V)+H_2(n;P,V)
                                -\ell_tP-\ell_sV,\\
H(y,P,\theta)&=h_0,\qquad Q(y,P,\theta)=q_0,\\
Q_U&=H_P-\frac{2P+k_t}{m}H_V+\frac{pP+n_s}{m}H_U,\qquad
Q_V=H_s-h_{0,s}.
\end{aligned}
\tag{15}
\]
The factorial-denominator Taylor polynomials are those of264.
Formal coefficient derivatives in the last line hold U,P,V fixed.
In particular the moving level derivative \(h_{0,s}\) is retained.

Let \(h_U,h_P,h_V\) and the Q partials denote their evaluations on
the intrinsic line. Both gradients are perpendicular to
\((y_P,1,\theta_P)\). Their cross product is consequently
\(\psi(y_P,1,\theta_P)\) for some \(\psi\in L[P]\).
The unit-minor conclusion296 and the middle tangent component 1
give \(\psi\in L^*\). In particular
\[
\mathcal W:=h_U Q_V^{\rm ev}-h_V Q_U^{\rm ev}\in L^*.
\tag{16}
\]
Its sign relative to the middle cross-product component is immaterial
to this nonzero-unit conclusion.

Differentiate the ACTUAL H level in s and P, fixing P for the
s derivative. With
\(\nu_f=(pP+n_s)/m\) and \(D_f=(2P+k_t)/m\), (15) becomes the
exact evaluated polynomial identity
\[
\mathcal W
=(\theta_P+D_f)h_V^2
 +(y_P-\theta_s-\nu_f)h_Uh_V-y_s h_U^2.
\tag{17}
\]
This uses \(Q_V^{\rm ev}=-h_Uy_s-h_V\theta_s\) and
\(h_P=-h_Uy_P-h_V\theta_P\). Thus no moving level or lower
gradient term is dropped.

The full H expression in (15), together with (10), gives
\[
[P^2]h_U=-2p/m,\qquad
[P^2]h_V=-q/2-p^2/m.
\tag{18}
\]
Both evaluated gradients have degree at most two. Since \(a_s=0\),
the three prefactors in (17) have degree at most one. In particular
the degree-five coefficient is determined without any lower
truncation of Q:
\[
\begin{aligned}
[P^5]\mathcal W
={}&2(a+1/m)(-q/2-p^2/m)^2\\
 &+(-pa-b_s-p/m)(-2p/m)(-q/2-p^2/m)\\
 &-(\lambda_s-pb_s/2)(-2p/m)^2\\
={}&\frac{3a^2mq^2+10ajp+3aq^2-12a_tpq}{6am}\\
={}&\frac{2pj+3q^2(1+ma)}{6m}.
\end{aligned}
\tag{19}
\]
The second equality uses the differentiated identity (13); the last
uses (14). Since (16) is a coefficient-field unit,
\[
2pj+3q^2(1+ma)=0.
\tag{20}
\]
The two equations (14),(20) are therefore licensed respectively by
the complete literal scalar and by the genuine two-gradient minors.

## 4. Integration in the exact one-variable field

Let \(F_0=\ker_L\partial_s\). It is finite over C(t), and the constants
of its t derivation are exactly C. One way to check finiteness is
to differentiate the monic minimal polynomial of an s-constant
over C(t,s): minimality forces its coefficients into C(t).
Degrees of constant subextensions are bounded by
\([L:\mathbb C(t,s)]\), since s remains transcendental over each
of them. Their union is therefore finite.
This does not assert \(F_0=\mathbb C(t)\).

By (3),(10), \(m,p,q,a\in F_0\). Put \(h=1/a\).
Equations (14),(20) give, without dividing by delta,
\[
h_t=\frac{q(h+m)}p,\qquad
\left(\frac{h+m}{p}\right)_t=1.
\tag{21}
\]
Thus the following are existing elements of \(F_0\):
\[
T=\frac{h+m}{p}=t-\tau,\quad \tau\in\mathbb C,\qquad
h=pT-m,\quad h_t=Tq,\quad q^2h^3\in\mathbb C^*.
\tag{22}
\]
Here T is nonzero because t is transcendental over C.
The invariant is the inverse of the nonzero constant
\(a^3/q^2\) obtained after (14).

Choose \(c_*\in\mathbb C^*\) with \(c_*^2=q^2h^3\).
No field extension is needed for the following square root:
\[
\zeta=\frac{qh^2}{c_*}\in F_0,\qquad
\zeta^2=h,\qquad q\zeta^3=c_*.
\tag{23}
\]
Consequently \(2\zeta\zeta_t=Tq\) and exact subtraction gives
\[
\zeta^5=\alpha T^2+d_*,\qquad
\alpha=5c_*/4\in\mathbb C^*,\quad d_*\in\mathbb C.
\tag{24}
\]
Only nonzero m,p,q,a,c_* and T have been divided out so far.
No coefficient-field root has been declared an ambient polynomial
coordinate or an ambient unit.

## 5. Algebraic exactness forces the extra constant to vanish

Suppose \(d_*\ne0\). In the exact finite one-variable function field
\(F_0\), differentiation of (24) gives the equality of differentials
\[
dp=q\,dT=\frac{c_*}{\zeta^3}\,dT
                         =\frac{2\zeta}{T}\,d\zeta.
\tag{25}
\]
This nonzero differential is regular at every place of \(F_0\).
Here is a direct valuation proof, including places in further finite
extensions rather than assuming the displayed plane field is all
of \(F_0\).

At a finite place for T, (24) makes zeta finite too. If T is nonzero
in the residue field, the last expression in (25) is regular. If T
vanishes, (24) and \(d_*\ne0\) make zeta a unit, so the middle
expression in (25) is regular. This includes zeros of zeta in the
first alternative.

At a place where T has a pole, (24) gives
\(5\operatorname{ord}\zeta=2\operatorname{ord}T\).
Write
\[
\operatorname{ord}\zeta=-2e,\qquad
\operatorname{ord}T=-5e,\qquad e\ge1.
\tag{26}
\]
In characteristic zero a local uniformizer expansion gives
\(\operatorname{ord}(d\zeta)=-2e-1\). Hence the last expression
of (25) has order \(e-1\ge0\). These arguments apply to every
discrete place of the finite field \(F_0\); their residue fields
are C.

But \(p_t=q\ne0\), so p is nonconstant. The finite extension
\(F_0/\mathbb C(p)\) has a place over the pole of p. At that place,
if \(\operatorname{ord}p=-n<0\), characteristic zero gives
\(\operatorname{ord}(dp)=-n-1<0\). This contradicts the regularity
just proved. Therefore
\[
d_*=0.
\tag{27}
\]
The contradiction uses algebraic exactness of dp, not rationality
of \(F_0\), a numerical sample, or an assumed elementary
antiderivative.

## 6. The existing fifth root and the remaining coefficient family

With (27), differentiation of (24),(23) gives
\(j/q=-6/(5T)\). Therefore
\[
d=p+5Tq\in\mathbb C,\qquad
m=dT-5\zeta^2,\qquad a=\zeta^{-2}.
\tag{28}
\]
The displayed d is unrelated to the now-zero integration constant
\(d_*\). Its t derivative is \(6q+5Tj=0\), and its s derivative
also vanishes, proving that it is complex. To check the middle
identity, use \(qT^2=4\zeta^2/5\) in \(m=pT-\zeta^2\).

Choose \(e_*\in\mathbb C^*\) with \(e_*^5=\alpha^3\), and define
another EXISTING coefficient element
\[
u=\frac{\zeta^3}{e_*T}\in F_0,\qquad u^5=T.
\tag{29}
\]
Then \((\zeta^2/u^4)^5=\alpha^2\), so algebraic closedness of C
makes \(\zeta^2/u^4\) a nonzero complex constant. Put
\(C=-5\zeta^2/u^4\in\mathbb C^*\). Equations (28),(29) prove (1).

For clarity the resulting exact derivatives and the retained degree
condition are
\[
p=d+\frac{4C}{5u},\quad
q=-\frac{4C}{25u^6},\quad
j=\frac{24C}{125u^{11}},\quad
\delta=-4-\frac{5d}{C}u.
\tag{30}
\]
The value \(d=0\) is permitted and gives \(\delta=-4\).
For \(d\ne0\), delta is also nonzero because u is transcendental
over C. The family thus retains the originally required degree-two
S rather than creating a discarded delta-zero boundary.

Equation (10) also gives the necessary lower coefficient condition
\[
n_{ss}=\frac{d^2}{2}+\frac{4dC}{5u}
                         +\frac{36C^2}{125u^2}\in F_0.
\tag{31}
\]
Consequently exact subtraction in s gives
\(n=n_{ss}s^2/2+N_1s+N_0\), with \(N_1,N_0\in F_0\).
Similarly \(k=ms+f\), with \(f\in F_0\).
These formulas do not solve the remaining genuine H and Q levels,
the lower full scalar coefficients, or the actual polynomial-entry
and return conditions.

## 7. Scope and verification record

The conclusion is a necessary fifth-root reduction only in the stated
\(a q\delta\ne0\) sector. Neither the \(q=0\) sector nor
\(\delta=0\) was divided away as though excluded. No conclusion
about either is made here. There is no actual coordinate change in
this proof, and \(u^5=t-\tau\) is a coefficient identity, not a
complex polynomial ambient normalization.

An abandoned theorem shortcut is not used: the degree bound
\(\Delta^3(Y,Z,W)=0\) for the actual auxiliary intrinsic derivation
does not provide the two actual coordinates with square-zero
derivative required by the two-quasi theorem used elsewhere.
Coefficient-field leading vectors cannot supply that actual
linear reframe without a separate proof.

Complete327,264,296,306,323 and324 sources were read through EOF,
and their hashes revalidated before this work. Fresh unsaved595eed,
completed509368, reconstructed the full literal determinant from
(6),(7), including all moving lower functions. Freshbba332 checked
the exact differentiated coefficient reduction (13),(14).
Freshfc9b4f checked the degree-five minor calculation (19).
Fresh88b8f3 independently rebuilt the full H leading coefficients
and checked the final fifth-root family against both differential
gates and (22). The valuation and exact-field proofs are written
above; symbolic checks are not substitutes for them.

No saved checker was executed, imported, compiled or rerun. No earlier
source, checker or canonical record was edited while authoring this
bounded result.

