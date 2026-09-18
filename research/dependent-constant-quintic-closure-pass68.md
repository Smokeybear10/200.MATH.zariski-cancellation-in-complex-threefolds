# Dependent defects with a constant quintic flow top

The dependent-defect constant-top quintic sector is recognized under
the supplied actual \((1,1,2,2)\) frame and absence of a complex
constant defect relation. The first two full companion images give
the same two residual-curve alternatives as in the quartic proof.
In the final constant-residual alternative, the polynomial
three-direction correction is nice: its square kills every actual
coordinate.

This is an exact degree-five theorem. It is not a statement about
moving tops, a frame for arbitrary sliced actions, or unrestricted
threefold cancellation.

## 1. Actual data and the first full image

Let
\[
B=k[x_1,x_2,X,Y],\quad k=\mathbb C,\quad
E\in\operatorname{LND}_k(B),\quad Es_*=1,\quad A=\ker E.
\]
The four displayed generators are actual polynomial coordinates.
For their actual partials assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0,
\]
\[
V_3=aD,\quad V_4=bD,\quad [E,D]=0,\qquad
a,b\in\ker E\cap\ker D,
\]
\[
a,b\text{ have no nonzero complex constant relation},\qquad
h_5:=E^5x=c\in k^4\setminus\{0\},\quad h_6=0.
\tag{1}
\]
Here \(D\) is the actual nonzero primitive LND of the established
dependent-defect decomposition; it is not supplied a new slice.

Write \(h_j=E^jx\), \(P=h_1\), \(J=\operatorname{Jac}P\),
\(d=D(x)\), and \(\ell=(0,0,a,b)\). The actual weighted companion
from [pass43](dependent-defect-top-line-pass43.md) is
\[
M=\begin{pmatrix}J&-d/2\\\ell&0\end{pmatrix},\qquad M^5=0,
\qquad
\mathcal C(z)=I-zJ+\frac{z^2}{2}d\ell.
\]
Its complete upper and lower identities are
\[
(M^j)_{\rm UL}=\frac{\operatorname{Jac}h_j}{j!},\qquad
M^j\binom P0=\frac1{j!}\binom{h_{j+1}}{j\ell h_j},
\]
\[
j!M^j\big|_{\rm base}
=\binom{\operatorname{Jac}h_j}
       {j\ell\operatorname{Jac}h_{j-1}}.
\tag{2}
\]
The variable row \(\ell\) is never differentiated in the lower
identity. In particular it is not replaced by a constant projection.

Since the upper component of \(M^4(P,0)^t\) is \(c/24\ne0\),
\[
\operatorname{Jordan}(M)=(5),\qquad
\operatorname{rank}M^4=1,\qquad\operatorname{rank}M^3=2.
\tag{3}
\]
The rank-preserving block lemma for a matrix killed on both sides
by \(M\) shows that \(\operatorname{Jac}h_4\) has rank one.
This also follows from the actual full-image line and its nonzero
upper vector \(c=(\operatorname{Jac}h_4)P\).

The full velocity identity is
\[
\mathcal C(z)\left(P+zh_2+\frac{z^2}{2}h_3+
                         \frac{z^3}{6}h_4+\frac{z^4}{24}c\right)=P.
\]
Its \(z^6\) coefficient gives \(\ell c=0\).
As \(c\) is constant and \(a,b\) have no constant relation,
\(c_3=c_4=0\). Thus \(T_c\) is a nonzero constant good partial.

Every ordinary derivative of \(h_4\) is proportional to \(c\).
Choose \(c_j\ne0\) and put \(\sigma=(h_4)_j/c_j\).
Comparing all four actual derivatives gives
\[
h_4=c\sigma+e,\qquad
\sigma\in B,\quad e\in k^4,\qquad E\sigma=1.
\tag{4}
\]
Write \(e_B=(e_3,e_4)\) and \(\rho=\ell e=ae_3+be_4\).
The full image of \(M^4\) is the line \(K(c,4\rho)^t\),
where \(K=\operatorname{Frac}B\). Its base columns therefore give
\[
\ell\operatorname{Jac}h_3=\rho\,d\sigma.
\tag{5}
\]
Here \(d\sigma\) denotes the ordinary differential row; it is
distinct from the vector \(d=D(x)\).

Set
\[
r=h_3-\frac{c\sigma^2}{2}-e\sigma.
\]
Then \(Er=0\), and (5) gives the actual bad residual relation
\[
(h_3)_B=e_B\sigma+(r_3,r_4),\qquad
a\,dr_3+b\,dr_4=0.
\tag{6}
\]
No coordinate status is asserted for these polynomial functions.

The remaining needed velocity coefficients, at orders \(5,4,3\),
are
\[
Jc=2\rho d,\qquad
Jh_4=\frac c4+\frac32(\ell h_3)d,\qquad
Jh_3=\frac{h_4}{3}+(\ell h_2)d.
\tag{7}
\]

If \(e_B=0\), then \(\rho=0\) and \(T_c\) commutes with \(E\).
Applying commutation to \(h_4\) gives \(T_c\sigma=0\).
The actual constant partial has a linear coordinate slice.
The [commuting coordinate-section lemma](independent-higher-constant-closure-pass68.md#2-a-commuting-coordinate-section-lemma)
then recognizes \(A\simeq k^{[3]}\).

Henceforth assume \(e_B\ne0\). Then \(\rho\ne0\) by (1), and
the constant directions \(c,e\) are independent.

## 2. The provisional correction and the first residual curve

Put
\[
s_0=ar_3+br_4,\qquad \lambda=s_0/\rho,\qquad
\beta=\frac{\sigma-3\lambda}{4},\qquad
S=T_e+\beta T_c.
\tag{8}
\]
Initially this is a rational field on \(B_\rho\).
Since \(E\rho=Es_0=0\), it has \(E\beta=1/4\).
Equations (4),(6),(7) give
\[
Je=\frac c4+
       \left(\frac32s_0-\frac{\rho\sigma}{2}\right)d.
\]
Consequently
\[
[E,T_c]=-2\rho D,\qquad
[E,T_e]=-\frac14T_c+2\beta\rho D,\qquad [E,S]=0.
\tag{9}
\]
At this point \(S\) is not yet asserted locally nilpotent.

Its values on the actual coordinates are \(Sx=e+\beta c\),
with \(E^2\beta=0\). Hence
\[
Sh_4=Sh_3=Sh_2=0,\qquad S\sigma=0,\qquad
S(r_3,r_4)=0.
\tag{10}
\]
For later use the same commutation gives \(SP_B=0\).
The issue is still to find a denominator actually killed by \(S\)
and to prove \(S\beta=0\); \(E\rho=0\) does not do this.

If \((r_3,r_4)\) is nonconstant, (6) and the finite
polynomial-curve theorem give
\[
r_3=p(u),\quad r_4=q(u),\quad u\in B,\quad p,q\in k[U],
\qquad Eu=Su=0,\qquad ap'(u)+bq'(u)=0.
\tag{11}
\]
The parameter is actual, not presumed a coordinate. Its
\(E,S\)-invariance follows by differentiating a nonconstant
member of the pair. Both derivatives are nonzero: otherwise
(11) and the nonzero \(a,b\) would make the pair constant.

Define
\[
\Delta=e_3q'-e_4p',\qquad N=pq'-qp'.
\]
The exact identities
\[
\rho q'=a\Delta,\qquad
\rho p'=-b\Delta,\qquad s_0\Delta=\rho N
\tag{12}
\]
show that \(\Delta(u)\ne0\) and
\(\lambda=N(u)/\Delta(u)\). The actual denominator
\(g=\Delta(u)\) is fixed by both \(E\) and \(S\). Thus
\[
S\beta=0,\quad S^2x=0,\quad
S\in\operatorname{LND}(B_g),\quad gS(B)\subset B.
\tag{13}
\]
This proves local nilpotence on the actual polynomial generators
and the additional fixed generator \(g^{-1}\).
No gcd-to-Bezout step or deletion of repeated factors is involved.

Complete the independent constant vectors \(c,e\) to an actual
constant coordinate frame. In it
\(S=\partial_b+\beta\partial_a\) and \(\partial_a=T_c\) is
still a good actual partial. The complete
[one-good-output lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
applies with the original slice, and gives \(A\simeq k^{[3]}\).

If instead the first residual pair is a constant
\(\mu=(\mu_1,\mu_2)\), and \(\mu=\lambda_0e_B\) for
\(\lambda_0\in k\), then (8) is polynomial with
\(S\beta=0\) by (10). This is a global nice LND, with a
linear coordinate slice dual to \(e\) and killed by \(T_c\).
It fixes \(\sigma\), so the coordinate-section lemma recognizes
this case.

Only the alternative
\[
(r_3,r_4)=\mu\in k^2,\qquad e_B,\mu
\text{ independent over }k
\tag{14}
\]
remains. Here \(\lambda=s_0/\rho\) need not yet have the required
invariant denominator.

## 3. The second full image gives another polynomial layer

Assume (14), so \(s_0=a\mu_1+b\mu_2\).
The image of \(M^4\) lies in that of \(M^3\).
Using (2), the latter contains the two vectors
\[
v=\binom c{4\rho},\qquad
6M^3\binom P0-\sigma v
=\binom e{3s_0-\sigma\rho}=:w.
\tag{15}
\]
Their upper vectors \(c,e\) are independent. By (3), they
therefore form a basis of the entire image of \(M^3\).

Each base column of \(6M^3\) has upper bad component
\(e_B\,\partial_i\sigma\), by (6),(14). Its \(w\)-coefficient
is therefore exactly \(\partial_i\sigma\).
Comparing the remaining upper components gives
\[
h_3=c\tau+e\sigma+v_0,\qquad
\tau\in B,\quad v_0\in k^4,\quad (v_0)_B=\mu,\quad
E\tau=\sigma.
\tag{16}
\]
For actual polynomiality, take a component of \(h_3-e\sigma\),
divide by the corresponding nonzero constant \(c_j\), and compare
all four ordinary partials of the other components.
There is no integration of an arbitrary rational form.

The lower components of the same base columns give
\[
\ell\operatorname{Jac}h_2
 =\frac{4\rho}{3}\,d\tau+
             \left(s_0-\frac{\rho\sigma}{3}\right)d\sigma.
\tag{17}
\]
Define
\[
u_0=\tau-\frac{\sigma^2}{2},\qquad
z_B=(h_2)_B-e_B\left(\frac{4\tau}{3}
                                  -\frac{\sigma^2}{6}\right)
                   -\mu\sigma.
\tag{18}
\]
Equations (6),(16),(17) imply
\[
Eu_0=0,\qquad Ez_B=0,\qquad
a\,d(z_B)_1+b\,d(z_B)_2=0.
\tag{19}
\]
The row \((a,b)\) was not differentiated.
These are exact identities of actual polynomials and their ordinary
differentials.

The provisional \(S\) fixes \(h_3,h_2,\sigma\) by (10).
Equation (16) then gives \(S\tau=Su_0=0\), and (18) gives
\[
Sz_B=0.
\tag{20}
\]

If this second residual pair is nonconstant, apply the same finite
polynomial-curve theorem:
\[
z_B=(p_1(w_0),q_1(w_0)),\quad w_0\in B,\quad
Ew_0=Sw_0=0,\quad ap_1'(w_0)+bq_1'(w_0)=0.
\]
The ratio in (8) still involves the first constant pair \(\mu\).
The correct denominator and numerator therefore are
\[
\Delta_1=e_3q_1'-e_4p_1',\qquad
N_1=\mu_1q_1'-\mu_2p_1',\qquad
\lambda=\frac{N_1(w_0)}{\Delta_1(w_0)}.
\tag{21}
\]
In particular this numerator is not \(p_1q_1'-q_1p_1'\).
As before, \(\rho q_1'=a\Delta_1\) proves
\(\Delta_1(w_0)\ne0\).
The chosen denominator and \(\lambda\) are both fixed by \(S\).
Thus \(S\) is a genuine nice LND on \(B_{\Delta_1(w_0)}\)
with one-power polynomial denominator clearing. The surviving
good direction \(T_c\) gives the same original-slice recognition
endpoint.

Only a constant second residual pair remains.

## 4. The final constant residual gives a global nice symmetry

Suppose
\[
z_B=\nu=\nu_1e_B+\nu_2\mu,\qquad \nu_1,\nu_2\in k.
\]
The constants exist uniquely because of (14). The two layer
identities now read
\[
h_3=c\tau+e\sigma+v_0,\qquad
(h_2)_B=e_B\left(\frac{4\tau}{3}
                           -\frac{\sigma^2}{6}\right)
                  +\mu\sigma+\nu.
\]
Insert these into the last velocity identity in (7). Using the
formulas for \(Jc,Je\) and \(u_0=\tau-\sigma^2/2\) gives
\[
Jv_0=\frac{c\sigma}{12}+\frac e3
       -\frac{2u_0\rho}{3}d-\frac{\sigma s_0}{2}d
       +(\nu_1\rho+\nu_2s_0)d.
\tag{22}
\]
All denominators in this identity are nonzero complex integers.

Set
\[
\beta_3=\frac{\sigma-2\nu_2}{3},\qquad
\gamma_3=\frac{\sigma^2}{12}-\frac{\nu_2\sigma}{6}
                           +\frac{u_0}{3}-\frac{\nu_1}{2},
\qquad
S_3=T_{v_0}+\beta_3T_e+\gamma_3T_c.
\tag{23}
\]
This is a global polynomial derivation, not an assumed LND.
Equations (7),(9),(22) give
\[
[E,S_3]=0,\qquad S_3x=v_0+\beta_3e+\gamma_3c.
\tag{24}
\]
For a coefficient check, the \(T_e,T_c\) coefficients are
\[
-\frac13+E\beta_3=0,\qquad
-\frac{\sigma}{12}-\frac{\beta_3}{4}+E\gamma_3=0.
\]
The \(s_0D\) and \(\rho D\) coefficients are, respectively,
\[
\frac{\sigma}{2}-\nu_2-\frac32\beta_3=0,\qquad
\frac{2u_0}{3}-\nu_1+\frac{\beta_3\sigma}{2}-2\gamma_3=0.
\]
These calculations do not assume that \(a,b\) are constants.

The coefficient functions of \(S_3x\) have \(E\)-degree at most
two. Hence commutation with \(h_4=c\sigma+e\) gives
\(S_3\sigma=0\). Commutation with (16) gives
\[
S_3h_3=E^3(S_3x)=0,\qquad
S_3\tau=S_3u_0=0.
\]
It follows that
\[
S_3\beta_3=S_3\gamma_3=0,\qquad S_3^2x=0,\qquad
S_3\in\operatorname{LND}(B).
\tag{25}
\]
Unlike the degree-four construction, there is no nonzero
\(S_3u_0\) term: here the relevant original layer is \(h_3\),
not \(h_2\).

The constant directions \(c,e,v_0\) are independent, because
their bad projections are \(0,e_B,\mu\).
Choose an actual linear coordinate \(z\) dual to \(v_0\)
and annihilated by \(T_c,T_e\). Then
\[
S_3z=1,\qquad S_3\sigma=0,\qquad E\sigma=1,\qquad [E,S_3]=0.
\tag{26}
\]
The coordinate-section lemma now recognizes the original kernel.

For clarity, its endpoint is global. The slice theorem gives
\(R=\ker S_3\simeq B/(z)\simeq k^{[3]}\) and \(B=R[z]\).
The restriction of \(E\) to \(R\) has the actual slice \(\sigma\).
Complex surface cancellation identifies its kernel as \(k^{[2]}\).
Moreover \(Ez\in R\); integration in the polynomial variable
\(\sigma\) produces \(H\in R\) with \(EH=Ez\).
Then \(z-H\) is \(E\)-invariant, and the original kernel is
that polynomial two-ring with one extra variable.
This uses the established lower-dimensional theorem, not the
unknown threefold cancellation statement.

## 5. Exhaustion, failure boundaries, and verification scope

The successive cases exhaust all actual residual pairs.
Thus the precise conclusion is
\[
\boxed{\text{Under (1), }\ker E\simeq\mathbb C^{[3]}.}
\tag{27}
\]

The first correction is only rational until one of its two
polynomial-curve alternatives supplies an \(S\)-invariant
denominator, or its coefficients become global polynomials.
The weaker localization control in
[the quartic note](dependent-constant-quartic-closure-pass68.md#7-why-the-denominator-and-second-image-steps-cannot-be-skipped)
still applies: being nice on the polynomial generators does not
make a derivation an LND of a localization whose inverted element
moves. Likewise a linear coordinate with constant nonzero
higher \(E\)-derivative has not been promoted to an \(E\)-slice.
The argument instead proves the actual action and coordinate slice
of the commuting field that it uses.

The full weighted-row identities are inherited from the actual
dependent companion. The finite polynomial-curve theorem and
its exact scope are the same as in the frozen
[dependent cubic reduction](dependent-constant-cubic-pass66.md#sources-and-verification-scope):
they give actual polynomial parameters for the two finite curve
subalgebras, not ambient coordinates. The localized recognition
uses the complete pass41 one-good-output proof. The global endpoint
uses the independently written, fully read coordinate-section
lemma in the higher-constant pass68 note and its retained complex
surface cancellation source gate.

This proof extends the second-image mechanism of the separate
dependent quartic note, with all changed quintic coefficients
displayed above. The polynomial three-direction construction
originated in root's independent higher-constant argument;
its variable-row application is proved here.
There is no new numerical suite or method count, fresh complete
primary-source reread, metadata edit, human expert review,
proof-assistant certificate, historical novelty verdict, or
unrestricted cancellation claim. Frozen and stable earlier files
are unchanged.

