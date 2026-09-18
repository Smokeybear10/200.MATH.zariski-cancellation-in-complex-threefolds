# Dependent defects with a constant quartic flow top

The dependent-defect constant-top quartic sector is recognized under
the supplied two-quadratic coordinate frame. The first full image
gives the next-layer analogue of the pass67 correction. If its
denominator is not yet controlled, the second full companion image
supplies another polynomial layer. This yields either an invariant
curve denominator or a global three-direction LND with an actual
coordinate slice.

The theorem concerns constant fourth flow derivative and dependent
defects with no complex constant relation. It does not address a
moving top, higher dependent flow degrees, or universal frame
existence.

## 1. Actual hypotheses and the full companion

Let
\[
B=k[x_1,x_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad Es_*=1,\qquad A=\ker E.
\]
The four generators are actual coordinates with partials \(T_i\).
Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0,
\tag{1}
\]
\[
V_3=aD,\quad V_4=bD,\quad [E,D]=0,\quad
a,b\in\ker E\cap\ker D,
\]
\[
a,b\ \text{have no nonzero complex constant relation},\qquad
h_4:=E^4x=c\in k^4\setminus\{0\},\qquad h_5=0.
\tag{2}
\]
Here \(D\) is the actual nonzero primitive LND of the established
dependent-defect decomposition. No slice on \(D\) is assumed.

Put \(h_j=E^jx\), \(P=h_1\), \(J=\operatorname{Jac}P\),
\(d=D(x)\), and \(\ell=(0,0,a,b)\). The actual weighted companion is
\[
M=\begin{pmatrix}J&-d/2\\\ell&0\end{pmatrix},\qquad
\mathcal C(z)=I-zJ+\frac{z^2}{2}d\ell.
\]
The full actual identities from
[pass43](dependent-defect-top-line-pass43.md#1-actual-hypotheses-and-the-weighted-companion)
are
\[
M^5=0,\qquad (M^j)_{\rm UL}
=\frac{\operatorname{Jac}h_j}{j!},\qquad
\mathcal C(z)^{-1}=\operatorname{Jac}(\exp(zE)x).
\tag{3}
\]
For \(j\ge1\) the applicable velocity and base-column identities are
\[
M^j\binom P0
=\frac1{j!}\binom{h_{j+1}}{j\ell h_j},
\qquad
j!M^j\big|_{\rm base}
=\binom{\operatorname{Jac}h_j}{j\ell\operatorname{Jac}h_{j-1}}.
\tag{4}
\]
The ordinary derivative of the variable row \(\ell\) is not inserted
into the lower row of (4).

Since \(d,\ell\ne0\), the rank-preserving block lemma applies to
matrices killed on both sides by \(M\). The upper-left block of
\(M^4\) is zero because \(h_4=c\) is constant, so \(M^5=0\)
implies \(M^4=0\). Equation (4) gives
\[
M^3\binom P0=\binom{c/6}{\ell h_3/2}\ne0.
\]
Consequently
\[
\operatorname{Jordan}(M)=(4,1),\qquad
\operatorname{rank}M^3=1,\qquad \operatorname{rank}M^2=2.
\tag{5}
\]
These are actual companion consequences, not assumptions about a
formal matrix model.

## 2. The first image and its residual bad pair

The coefficient of \(z^5\) in
\[
\mathcal C(z)\left(P+zh_2+\frac{z^2}{2}h_3+\frac{z^3}{6}c\right)=P
\]
gives \(\ell c=0\). The absence of a constant defect relation forces
\(c_3=c_4=0\). Thus \(T_c\) is a nonzero actual constant good partial.

By (3)--(5), \(\operatorname{Jac}h_3\) has rank one. Its image
contains \(c=(\operatorname{Jac}h_3)P\), so comparison of all
ordinary partials gives
\[
h_3=c\sigma+e,\qquad
\sigma\in B,\quad e\in k^4,\qquad E\sigma=1.
\tag{6}
\]
For example choose \(c_j\ne0\), take \(\sigma=(h_3)_j/c_j\),
and differentiate \(h_3-c\sigma\). All four partials kill it.

Write \(e_B=(e_3,e_4)\) and \(\rho=\ell e=ae_3+be_4\).
The image line of \(M^3\) is
\(K(c,3\rho)^t\), where \(K=\operatorname{Frac}B\).
The base columns in (4) therefore give
\[
\ell\operatorname{Jac}h_2=\rho\,d\sigma.
\tag{7}
\]
Here \(d\sigma\) is the ordinary differential row, not \(D(x)\).

Define the actual \(E\)-invariant vector
\[
r=h_2-\frac{c\sigma^2}{2}-e\sigma.
\]
Since \(\ell c=0\), equation (7) gives
\[
(h_2)_B=e_B\sigma+(r_3,r_4),\qquad
Er_3=Er_4=0,\qquad a\,dr_3+b\,dr_4=0.
\tag{8}
\]
All statements concern actual polynomial functions. In particular,
the residual pair in (8) has transcendence degree at most one.

The remaining full velocity coefficients are
\[
Jc=\frac32\rho d,\qquad
Jh_3=\frac c3+(\ell h_2)d,\qquad
Jh_2=\frac{h_3}{2}+\frac{\ell P}{2}d.
\tag{9}
\]
Their factors follow respectively from the \(z^4,z^3,z^2\)
coefficients of the same actual velocity identity.

If \(e_B=0\), then \(\rho=0\), so \(T_c\) commutes with \(E\).
Commutation applied to (6) gives \(T_c\sigma=0\). The constant
partial has a complex linear coordinate slice, and the
[commuting coordinate-section lemma](independent-higher-constant-closure-pass68.md#2-a-commuting-coordinate-section-lemma)
recognizes \(A\simeq k^{[3]}\).

Below assume \(e_B\ne0\). Then \(\rho\ne0\) by the absence of a
constant relation between \(a,b\).

## 3. A provisional rational correction

Put
\[
s_0=ar_3+br_4,\qquad \lambda=s_0/\rho,\qquad
\beta=\frac{\sigma-2\lambda}{3},\qquad
S=T_e+\beta T_c.
\tag{10}
\]
Initially these are rational functions and a rational derivation.
The denominator \(\rho\) is killed by \(E\), so the expressions
define a derivation on \(B_\rho\), and \(E\beta=1/3\).

Equations (6),(8)--(9) give
\[
Je=\frac c3+\left(s_0-\frac{\rho\sigma}{2}\right)d.
\]
Consequently
\[
[E,T_c]=-\frac32\rho D,\qquad
[E,T_e]=-\frac13T_c+\frac32\beta\rho D,\qquad [E,S]=0.
\tag{11}
\]
No local-nilpotence conclusion follows yet.

Since \(Sx=e+\beta c\) and \(E^2\beta=0\), commutation gives
\[
Sh_3=E^3(Sx)=0,\qquad S\sigma=0,
\]
\[
Sh_2=E^2(Sx)=0,\qquad S(r_3,r_4)=0.
\tag{12}
\]
The last equality uses (8) and \(c_B=0\).
The same commutation also gives
\[
S(P_B)=E(Sx_B)=E(e_B)=0.
\tag{13}
\]

The task is to prove \(S\beta=0\) and exhibit a denominator actually
killed by \(S\). Merely knowing that \(\rho\) is \(E\)-invariant
does not establish either property.

## 4. Nonconstant or collinear first residual pairs

Suppose \((r_3,r_4)\) is nonconstant. The finite polynomial-curve
input already used in passes66--67 applies to \(k[r_3,r_4]\).
It gives an actual polynomial \(u\) and \(p,q\in k[U]\) with
\[
r_3=p(u),\qquad r_4=q(u),\qquad
Eu=Su=0,\qquad ap'(u)+bq'(u)=0.
\tag{14}
\]
Here the invariance of \(u\) follows by differentiating a nonconstant
member of the pair, using (8),(12). Both derivatives are nonzero.

Define
\[
\Delta(U)=e_3q'(U)-e_4p'(U),\qquad
N(U)=p(U)q'(U)-q(U)p'(U).
\]
As in the exact pass67 denominator calculation,
\[
\rho q'=a\Delta,\qquad \rho p'=-b\Delta,\qquad
s_0\Delta=\rho N.
\]
Thus \(\Delta(u)\ne0\), \(\lambda=N(u)/\Delta(u)\), and the
new denominator \(g=\Delta(u)\) is killed by both \(E\) and \(S\).
It follows from (10),(12),(14) that
\[
S\beta=0,\qquad S^2x=0,\qquad
S\in\operatorname{LND}(B_g),\qquad gS(B)\subset B.
\tag{15}
\]
Local nilpotence follows on the polynomial generators and the
fixed element \(g^{-1}\). No coprimality, comaximality, or loss
of repeated denominator factors is used.

The independent constant vectors \(c,e\) can be completed to an
actual constant frame in which \(S=\partial_b+\beta\partial_a\)
and \(\partial_a=T_c\) is good. The complete
[one-good-output recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
applies with the original slice, proving \(A\simeq k^{[3]}\).

Suppose instead that the first residual pair is a constant
\(\mu=(\mu_1,\mu_2)\). If \(\mu=\lambda_0e_B\) with
\(\lambda_0\in k\), then \(\lambda=\lambda_0\) and (10) is
polynomial. Equation (12) immediately makes \(S\beta=0\), so \(S\)
is a global nice LND. A linear coordinate dual to \(e\) and
annihilated by \(T_c\) is its actual slice.
It fixes \(\sigma\), so the coordinate-section lemma recognizes
this case too.

The only remaining first-layer alternative is
\[
(r_3,r_4)=\mu\in k^2,\qquad e_B,\mu
\text{ linearly independent over }k.
\tag{16}
\]
In particular, \(\lambda=s_0/\rho\) need not yet have an
\(S\)-invariant polynomial denominator.

## 5. The second image gives a further actual polynomial layer

Retain (16), so \(s_0=a\mu_1+b\mu_2\).
The image of \(M^3\) lies in that of \(M^2\), and (4) gives
\[
v=\binom c{3\rho},\qquad
2M^2\binom P0=\binom{c\sigma+e}{2(\rho\sigma+s_0)}.
\]
Subtract \(\sigma v\) from the second vector:
\[
w=\binom e{2s_0-\sigma\rho}.
\tag{17}
\]
Both \(v,w\) lie in \(\operatorname{im}M^2\).
Their upper components \(c,e\) are independent because
\(c_B=0\) and \(e_B\ne0\). Equation (5) therefore makes them a
basis of the entire second image.

Each base column of \(2M^2\) is a combination of these vectors.
Its upper bad part is \(e_B\,\partial_i\sigma\), by (8),(16).
Thus its coefficient of \(w\) is exactly \(\partial_i\sigma\).
Choosing a nonzero constant component of \(c\) and integrating
all four ordinary partials yields
\[
h_2=c\tau+e\sigma+v_0,\qquad
\tau\in B,\quad v_0\in k^4,\quad (v_0)_B=\mu,\quad E\tau=\sigma.
\tag{18}
\]
Concretely, a component of \(h_2-e\sigma\), divided by the
corresponding nonzero \(c_j\), defines \(\tau\); every remaining
difference has zero ordinary gradient. Thus no integrability of an
arbitrary rational form is being assumed.

The lower components of the same base columns give
\[
\ell J=\frac{3\rho}{2}\,d\tau+
       \left(s_0-\frac{\sigma\rho}{2}\right)d\sigma.
\tag{19}
\]
Set
\[
u_0=\tau-\frac{\sigma^2}{2},\qquad Eu_0=0,
\]
\[
z_B=P_B-e_B\left(\frac{3\tau}{2}-\frac{\sigma^2}{4}\right)
          -\mu\sigma.
\tag{20}
\]
These are actual polynomials. Since \(E\tau=\sigma\) and
\(EP_B=(h_2)_B=e_B\sigma+\mu\),
\[
Ez_B=0,\qquad a\,d(z_B)_1+b\,d(z_B)_2=0.
\tag{21}
\]
The differential relation is exactly (19), with the displayed
polynomial derivatives subtracted. The variable row \(\ell\)
has not been differentiated or replaced by constants.

The provisional field \(S\) still satisfies (12)--(13).
Applying \(Sh_2=0\) to (18), and using \(S\sigma=0\), gives
\(S\tau=Su_0=0\). Equation (13) then gives
\[
Sz_B=0.
\tag{22}
\]

If the second residual pair \(z_B\) is nonconstant, apply the
same finite polynomial-curve theorem:
\[
z_B=(p_1(w_0),q_1(w_0)),\qquad
Ew_0=Sw_0=0,\qquad ap_1'(w_0)+bq_1'(w_0)=0.
\]
The first constant pair \(\mu\), not the new residual pair, occurs
in \(s_0\). Accordingly the exact denominator formulas now are
\[
\Delta_1=e_3q_1'-e_4p_1',\qquad
N_1=\mu_1q_1'-\mu_2p_1',\qquad
\lambda=\frac{N_1(w_0)}{\Delta_1(w_0)}.
\tag{23}
\]
Again \(\Delta_1(w_0)\ne0\) follows from \(\rho q_1'=a\Delta_1\).
The field \(S\) fixes this denominator and its coefficient.
It is a genuine nice LND on this explicitly invariant localization,
with one-power polynomial denominator clearing.
The same actual one-good-output lemma recognizes \(A\).

Thus only a constant second residual pair remains.

## 6. Constant second residual: a global three-direction LND

Suppose \(z_B=\nu\in k^2\). Since \(e_B,\mu\) are independent,
write
\[
\nu=\nu_1e_B+\nu_2\mu,\qquad \nu_1,\nu_2\in k.
\tag{24}
\]
Equations (18),(20) become
\[
h_2=c\tau+e\sigma+v_0,\qquad
P_B=e_B\left(\frac{3\tau}{2}-\frac{\sigma^2}{4}\right)
       +\mu\sigma+\nu.
\]
Insert them into the last identity in (9), using (11)'s formula
for \(Je\). A direct calculation gives
\[
Jv_0=\frac{c\sigma}{6}+\frac e2
       -\frac{3u_0\rho}{4}d-\frac{\sigma s_0}{2}d
       +\frac{\nu_1\rho+\nu_2s_0}{2}d.
\tag{25}
\]
Only divisions by nonzero complex integers occur.

Define the polynomial coefficients
\[
\beta_3=\frac{\sigma-\nu_2}{2},\qquad
\gamma_3=\frac{\sigma^2}{6}-\frac{\nu_2\sigma}{6}
             +\frac{u_0}{2}-\frac{\nu_1}{3},
\]
and the global polynomial derivation
\[
S_3=T_{v_0}+\beta_3T_e+\gamma_3T_c.
\tag{26}
\]
Using \([E,T_v](x)=-Jv\), equations (9),(11),(25) give
\[
[E,S_3]=0,\qquad S_3x=v_0+\beta_3e+\gamma_3c.
\tag{27}
\]
For an explicit sign check, the \(T_e\) coefficient is
\(-1/2+E\beta_3=0\), and the \(T_c\) coefficient is
\(-\sigma/6-\beta_3/3+E\gamma_3=0\).
The coefficient of \(s_0D\) is
\(\sigma/2-\nu_2/2-\beta_3=0\), and that of \(\rho D\) is
\[
\frac{3u_0}{4}-\frac{\nu_1}{2}
       +\frac{\beta_3\sigma}{2}-\frac{3\gamma_3}{2}=0.
\]

At this stage \(S_3\) has not yet been assumed locally nilpotent.
Its coefficient functions have \(E\)-degree at most two, so
commutation with \(h_3=c\sigma+e\) gives \(S_3\sigma=0\).
Commutation with (18), using \(E^2\gamma_3=1/3\), then gives
\[
S_3\tau=S_3u_0=\frac13,\qquad
S_3\beta_3=0,\qquad S_3\gamma_3=\frac16.
\]
Consequently
\[
S_3^2x=\frac c6,\qquad S_3^3x=0,\qquad
S_3\in\operatorname{LND}(B).
\tag{28}
\]
The last conclusion follows for every polynomial by the Leibniz
rule. This field is global, with no localization.

The constant vectors \(c,e,v_0\) are independent:
their bad projections are \(0,e_B,\mu\), with the last two
independent, and \(c\ne0\). A constant ambient coordinate \(z\)
dual to \(v_0\) and annihilated by \(T_c,T_e\) therefore has
\[
S_3z=1,\qquad S_3\sigma=0,\qquad E\sigma=1.
\tag{29}
\]
The original action commutes with \(S_3\).
All hypotheses of the commuting coordinate-section lemma are met,
so this final alternative also has \(A\simeq k^{[3]}\).

For completeness, the endpoint uses
\(\ker S_3\simeq B/(z)\simeq k^{[3]}\), not an assumed quotient
presentation. The restriction of \(E\) has the actual slice
\(\sigma\) in that kernel. Complex surface cancellation identifies
its kernel as \(k^{[2]}\). The polynomial \(Ez\) lies in
\(\ker S_3\); integrating it in \(\sigma\) makes an \(E\)-invariant
replacement \(z-H\). This gives the original kernel as the resulting
polynomial two-ring with one additional variable.
It does not invoke cancellation in the unknown dimension three.

## 7. Why the denominator and second-image steps cannot be skipped

In the constant-pair alternative (16),
the original linear bad coordinate \(e_4X-e_3Y\) has a nonzero
constant second \(E\)-derivative. This alone does not make that
coordinate an \(E\)-slice. The proof instead uses the second image
and, when necessary, the actual coordinate slice for \(S_3\).

Likewise, a rational field that kills its own coefficient and is
nice on polynomial generators need not be locally nilpotent on
the chosen localization. Here is an exact weaker-premise control.
On \(k[\sigma,x,y,z]\), let
\[
E_0=\partial_\sigma+\frac y3\partial_x,\qquad
Z_0=\partial_y+\frac xy\partial_x
\quad\text{on }k[\sigma,x,y,z]_y.
\]
Then
\[
E_0\sigma=1,\qquad [E_0,Z_0]=0,\qquad
E_0(x/y)=1/3,\qquad Z_0\sigma=Z_0(x/y)=0,
\]
and \(Z_0^2\) kills all four polynomial generators. But \(y\)
is a unit with \(Z_0y=1\), so \(Z_0\) is not an LND of the
localization. Indeed its iterates on \(y^{-1}\) never vanish.

This is a polynomial-ring sliced action used only to test the
localization inference. Its displayed frame has flow degree one,
not the quartic hypotheses (1)--(2), and it is not a counterexample
to the theorem. It explains why (14)--(15) and (22)--(23) prove
invariance of the actual chosen denominator separately.
The global construction in Section 6 avoids this issue altogether.

## 8. Exact conclusion and dependencies

Sections 2, 4, 5 and 6 exhaust the alternatives for the two successive
actual residual pairs. Thus
\[
\boxed{\text{Under (1)--(2), }\ker E\simeq\mathbb C^{[3]}.}
\tag{30}
\]

The first-image construction extends the actual weighted-companion
argument in the frozen dependent cubic note, rather than importing
a constant-row formula into a variable-row setting. The new
second-image step retains that variable row and only produces
the differential relation (21), not a constant residual pair
without proof. The polynomial-curve alternatives use the same
finite-subalgebra theorem and source gates as
[pass66](dependent-constant-cubic-pass66.md#sources-and-verification-scope).
Its parameter and all new slice polynomials remain actual functions,
not presumed ambient coordinates.

The localized branches invoke the complete pass41 one-good-output
lemma with its original-slice and surviving-actual-partial hypotheses.
The global branches invoke the independently written
[coordinate-section lemma](independent-higher-constant-closure-pass68.md#2-a-commuting-coordinate-section-lemma);
its complete proof was read before using it here.
Its external input is the established complex surface cancellation
theorem retained in
[pass43's source scope](commuting-coordinate-descent-pass43.md#source-gates),
not the target threefold cancellation statement.

The polynomial three-direction construction was suggested by root's
independent higher-constant calculation. Its dependent variable-row
application, the additional residual-curve branch, and all displayed
coefficients are proved separately here.
Outline reconstructions and full-file audits are distinct evidence.
No new numerical suite, metadata edit, human expert review,
proof-assistant verification, novelty certification, or unrestricted
cancellation solution is claimed. Stable pass67 and frozen earlier
proofs are unchanged.

