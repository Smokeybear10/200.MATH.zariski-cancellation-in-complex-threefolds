# Independent defects with a higher constant flow top

For the supplied two-quadratic coordinate frame, the independent-defect
constant-top sectors of flow degrees four through six are recognized.
Two consecutive full companion images give a polynomial second-layer
normal form. That form supplies a global commuting locally nilpotent
derivation with a genuine ambient coordinate slice. Its kernel is an
actual polynomial three-ring on which the original action still has
a slice.

This is a conditional supplied-frame result. Neither a moving highest
vector nor universal coordinate-frame existence is addressed here.

## 1. Actual hypotheses and first full-image input

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B),\qquad E(s_*)=1,\qquad A=\ker E,
\]
and let \(T_i\) be the actual coordinate partials. Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Write \(h_j=E^jx\), \(P=h_1\), \(J=\operatorname{Jac}P\),
and let \(\mathcal V\) be the four-by-two matrix of the actual
defects \(V_3,V_4\). Assume its fraction-field rank is two and
\[
h_m=c\in\mathbb C^4\setminus\{0\},\qquad h_{m+1}=0,
\qquad 4\le m\le6.
\tag{2}
\]
The upper bound six is the inherited actual companion bound.
Let \(L\) select the last two coordinates, and put
\[
M=\begin{pmatrix}J&-\mathcal V/2\\ L&0\end{pmatrix}.
\]
All ranks of this matrix are over \(\operatorname{Frac}B\).
The complete [constant-top full-row refinement](two-quadratic-top-line-pass42.md#6-a-separate-constant-top-full-row-refinement)
gives
\[
M^m=0,\qquad M^{m-1}\ne0,\qquad Lc=0,
\]
\[
h_{m-1}=c\sigma+d,\qquad E\sigma=1,
\qquad Lh_{m-2}=\ell\sigma+\mu,
\tag{3}
\]
where \(\sigma\in B\) is an actual polynomial and
\(d\in\mathbb C^4\), \(\ell,\mu\in\mathbb C^2\),
with \(Ld=\ell\). No coordinate assertion about \(\sigma\)
is part of that input.

For every applicable \(j\), the actual-flow identities are
\[
M^j\binom P0=\frac1{j!}
\binom{h_{j+1}}{jLh_j},\qquad
j!M^j\big|_{\text{base columns}}=
\binom{\operatorname{Jac}h_j}{j\operatorname{Jac}(Lh_{j-1})}.
\tag{4}
\]
These retain the auxiliary rows; an upper-block rank statement
alone would not give the argument below.

## 2. A commuting coordinate-section lemma

Suppose a global polynomial LND \(Z\) of \(B\) commutes with
\(E\), has a slice \(z\) that is an actual ambient coordinate,
and fixes a polynomial \(\sigma\) with \(E\sigma=1\).
Then \(A\simeq\mathbb C^{[3]}\).

Indeed, the slice theorem and the actual coordinate quotient give
\[
R=\ker Z\simeq B/(z)\simeq\mathbb C^{[3]},\qquad B=R[z].
\tag{5}
\]
Commutation makes \(E_0=E|_R\) an LND, and \(\sigma\in R\)
is its slice. Thus \(R=C[\sigma]\), where \(C=\ker E_0\).
Cancellation of one variable from a polynomial three-ring, the
established complex surface cancellation theorem, gives
\(C\simeq\mathbb C^{[2]}\).[^surface]

Moreover \(h=Ez\in R=C[\sigma]\), since \(Z(Ez)=0\).
Characteristic zero permits a polynomial primitive
\(H\in C[\sigma]\) with \(E_0H=h\). Then
\[
z'=z-H,\qquad Ez'=0,\qquad
B=C[\sigma,z'],\qquad \ker E=C[z']\simeq\mathbb C^{[3]}.
\tag{6}
\]
This uses an actual slice of \(Z\), and an actual \(Z\)-invariant
slice of \(E\). It does not transfer an arbitrary original slice
to a quotient or invoke threefold cancellation as an input.

## 3. The zero and collinear bad-layer alternatives

The highest actual velocity identity and (3)--(4) give
\[
Jc=\frac{m-1}{2}\mathcal V\ell,\qquad
Jd=\frac{c}{m-1}-\frac{\sigma}{2}\mathcal V\ell
       +\frac{m-2}{2}\mathcal V\mu.
\tag{7}
\]
For the second identity, apply \(M\) to
\((h_{m-1},(m-2)Lh_{m-2})^t\) and use (4).

If \(\ell=0\), then the genuine constant partial \(T_c\)
commutes with \(E\). Applying commutation to
\(h_{m-1}=c\sigma+d\) gives
\(cT_c\sigma=E^{m-1}(T_cx)=0\), so \(T_c\sigma=0\).
There is a complex linear coordinate \(z\) with \(T_cz=1\).
The lemma in Section 2 applies to \(Z=T_c\).

Suppose \(\ell\ne0\) and \(\mu=\lambda\ell\) for a complex
constant \(\lambda\). Put
\[
Z=T_d+\frac{\sigma-(m-2)\lambda}{m-1}T_c.
\tag{8}
\]
Here \(T_v\) denotes differentiation in a genuine constant
direction \(v\), so \([E,T_v](x)=-Jv\). Equation (7) and
\(E\sigma=1\) prove \([E,Z]=0\).
Since \(m-1\ge3\), applying commutation to \(h_{m-1}\)
forces \(Z\sigma=0\). Thus \(Z^2x=0\), which proves
global local nilpotence by the Leibniz rule.

The constant vectors \(c,d\) are independent, as
\(Lc=0\) and \(Ld=\ell\ne0\). A complex linear coordinate
\(z\) can therefore be chosen with \(T_dz=1\), \(T_cz=0\).
It has \(Zz=1\). Section 2 again recognizes the original kernel.

## 4. The second companion image gives two exact polynomial layers

It remains to consider independent constant vectors
\(\ell,\mu\in\mathbb C^2\). In particular \(\ell\ne0\).
The Jordan form of the six-dimensional \(M\) has a block of size
\(m\); all remaining blocks have total size \(6-m\le2\).
For \(m=4\), their \((m-2)\)-th powers already vanish; the
same holds for \(m=5,6\). Consequently
\[
\operatorname{rank}M^{m-2}=2.
\tag{9}
\]
Equation (4) puts both
\[
v=\binom{c}{(m-1)\ell},\qquad
u_0=\binom{c\sigma+d}{(m-2)(\ell\sigma+\mu)}
\]
in \(\operatorname{im}M^{m-2}\). Subtract \(\sigma v\) to get
\[
w=\binom d{(m-2)\mu-\sigma\ell}.
\tag{10}
\]
The upper bad components of \(v,w\) are respectively \(0,\ell\),
so these two vectors are independent and span the image in (9).

Each base column in (4), for \(j=m-2\), is therefore a combination
of \(v,w\). Its upper bad row is
\(\ell\,\partial_i\sigma\) by (3). This forces its coefficient
of \(w\) to be exactly \(\partial_i\sigma\). Hence there is
a one-form \(\alpha\) with
\[
d h_{m-2}=c\alpha+d\,d\sigma.
\tag{11}
\]
Here an initial \(d\) before an expression denotes ordinary
differentiation; the unadorned vector \(d\) is the constant in (3).
Choose a nonzero component of \(c\). Equation (11) defines an
actual polynomial \(\tau\) by that component of
\(h_{m-2}-d\sigma\), divided by a nonzero complex constant.
Every ordinary partial then kills the remaining differences, so
\[
h_{m-2}=c\tau+d\sigma+e,\qquad
e\in\mathbb C^4,\qquad Le=\mu,\qquad E\tau=\sigma.
\tag{12}
\]
The coefficient form in (11) is \(d\tau\), not an assumed
integrable rational form.

The auxiliary rows of those same columns now give
\[
(m-2)d(Lh_{m-3})=(m-1)\ell\,d\tau
 +\bigl((m-2)\mu-\sigma\ell\bigr)d\sigma.
\]
Integrating all four actual partials yields a complex constant
pair \(\nu\) and the exact polynomial identity
\[
Lh_{m-3}=\ell\left(\frac{m-1}{m-2}\tau
                    -\frac{\sigma^2}{2(m-2)}\right)
             +\mu\sigma+\nu.
\tag{13}
\]
The integration constants in (12)--(13) really are complex constants,
not arbitrary invariants of \(E\).

Set
\[
q=\tau-\frac{\sigma^2}{2},\qquad Eq=0,\qquad
\nu=\nu_1\ell+\nu_2\mu,
\quad \nu_1,\nu_2\in\mathbb C.
\tag{14}
\]
The last expression uses independence of the two constant bad
vectors. Neither \(q\) nor \(\sigma\) is presumed to be an
ambient coordinate.

## 5. The full velocity supplies a global three-direction correction

Apply \(M\) to the actual velocity column for power \(m-3\)
in (4). Its upper part says
\[
Jh_{m-2}-\frac{m-3}{2}\mathcal V Lh_{m-3}
=\frac{h_{m-1}}{m-2}.
\tag{15}
\]
Insert (7), (12)--(14), retaining both bad directions. The result is
\[
Je=\frac{c\sigma}{(m-1)(m-2)}+\frac d{m-2}
 -\frac{(m-1)q}{2(m-2)}\mathcal V\ell
 -\frac\sigma2\mathcal V\mu
 +\frac{m-3}{2}\mathcal V\nu.
\tag{16}
\]
This is a polynomial identity. No denominator other than a nonzero
complex integer has been introduced.

Define the constant \(b_0\) and polynomial coefficients
\[
b_0=-\frac{m-3}{m-2}\nu_2,\qquad
\beta=\frac\sigma{m-2}+b_0,
\]
\[
\gamma=\frac{\sigma^2}{(m-1)(m-2)}
       +\frac{b_0\sigma}{m-1}
       +\frac q{m-2}-\frac{m-3}{m-1}\nu_1.
\tag{17}
\]
Put
\[
Z=T_e+\beta T_d+\gamma T_c.
\tag{18}
\]
Using \([E,T_v](x)=-Jv\), equations (7),(16)--(17) show
\[
[E,Z]=0,
\qquad Zx=e+\beta d+\gamma c.
\tag{19}
\]
Explicitly, the coefficient of \(T_d\) is
\(-1/(m-2)+E\beta=0\), and that of \(T_c\) is
\(-\sigma/((m-1)(m-2))-\beta/(m-1)+E\gamma=0\).
The \(\mathcal V\ell\) and \(\mathcal V\mu\) coefficients
then cancel by the displayed choices of \(b_0\) and the constant
term in \(\gamma\), together with \(\nu=\nu_1\ell+\nu_2\mu\).

Commutation has established a polynomial derivation, not yet an LND.
That remaining property is proved next.

## 6. Global local nilpotence and an actual coordinate slice

All coefficients in (19) have \(E\)-degree at most two.
Since \(m-1\ge3\), commutation and (3) give
\[
cZ\sigma=Z(h_{m-1})=E^{m-1}(Zx)=0,
\qquad Z\sigma=0.
\tag{20}
\]
Next use (12). Since \(Z\sigma=0\), its left side under \(Z\)
is \(cZq\). On the other hand
\(Z(h_{m-2})=E^{m-2}(Zx)\). Equation (17) therefore yields
\[
Zq=\begin{cases}1/3,&m=4,\\0,&m=5,6.\end{cases}
\tag{21}
\]
For \(m=4\), this gives \(Z\beta=0\), \(Z\gamma=1/6\),
so \(Z^2x=c/6\) and \(Z^3x=0\). For \(m=5,6\), it gives
\(Z\beta=Z\gamma=0\), so \(Z^2x=0\).
The Leibniz rule proves local nilpotence on every polynomial of
\(B\). In particular this is a global LND, not a rational field
or a field asserted locally nilpotent merely because it commutes
with \(E\).

The constant vectors \(c,d,e\) are independent. Projecting a
constant relation to the bad plane first kills its \(d,e\)
coefficients because \(Ld=\ell\), \(Le=\mu\) are independent;
then \(c\ne0\) kills the last coefficient. Complete these vectors
to a constant ambient basis. A dual complex linear coordinate
\(z\) satisfies
\[
T_ez=1,\qquad T_dz=T_cz=0,
\qquad Zz=1.
\tag{22}
\]
Thus \(z\) is simultaneously a genuine ambient coordinate and
a slice for the now-proved global LND \(Z\). By (20), \(Z\)
fixes the actual polynomial \(\sigma\), whose original derivative
is one. Section 2 proves \(A\simeq\mathbb C^{[3]}\).

Sections 3--6 exhaust all constant pairs \(\ell,\mu\), proving
the stated independent higher constant-top theorem.

## 7. Scope and verification obligations

The new matrix step uses the entire six-dimensional companion and
both auxiliary rows, not formal Jordan data alone. The slice of
the second action is a complex linear coordinate constructed after
global local nilpotence is proved. The original action restricts
to its actual kernel, and its slice \(\sigma\) is proved to lie
there. These are the exact points needed for the coordinate-section
lemma; omitting any of them would invalidate that endpoint.

This note is a new working proof beyond the frozen pass67 packet.
Outline reconstructions and complete saved-file audits are to be
recorded separately. The earlier finite regression does not check
this theorem or its new formulas. No formal proof, historical
novelty certification, human expert review, universal frame theorem,
general cancellation solution, external contact or submission is
claimed.

## Sources

[^surface]: Complex surface cancellation: if \(C[t]\simeq\mathbb C^{[3]}\), then \(C\simeq\mathbb C^{[2]}\). The source scope is retained from [the complete coordinate-descent proof](commuting-coordinate-descent-pass43.md#source-gates): Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), author manuscript dated October 5, 2001, PDF p. 2, states CP(3) and cites Takao Fujita, [*On Zariski problem*](https://doi.org/10.3792/pjaa.55.106), Proceedings of the Japan Academy, Series A 55 (1979), 106-110. This established dimension-two theorem is the external recognition input. It is not the dimension-three conjecture under investigation, and the original Fujita proof is not claimed freshly reconstructed here.
