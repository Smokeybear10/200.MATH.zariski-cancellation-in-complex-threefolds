# A cubic reduction and smaller frontier in the balanced branch

Working necessary result: retain EVERY actual hypothesis of264 and
the sector
\[
k=s+f,\qquad f_s=0,\qquad e=n_{ss}\ne0,\qquad f'''\ne0.
\tag{1}
\]
In the balanced alternative of460, write
\[
\deg\sigma=2c,\qquad \deg y=\deg\theta=3c,\qquad c\ge1.
\tag{2}
\]
The genuine fourth level reduces to a cubic without changing the
evaluated minor-unit ideal. Consequently \(3c\le9\). After the
separate exclusion470, the remaining balanced degree pairs are
\[
\boxed{(\deg\sigma,\deg y)=(4,6)\quad\hbox{or}\quad(6,9).}
\tag{3}
\]
Additional exact remainder restrictions are proved below.
Neither pair in(3) is excluded or realized here. The result concerns
this balanced branch only and does not require the strict-branch
results465--468.

## 1. Retained actual inputs and notation

Retain the original globally sliced polynomial ring
\(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\), the exact E-degrees
\((1,2,2,2)\), and the ENTIRE weighted initial kernel
\(\mathsf X^2\mathsf Z-\mathsf Y^2\) from
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
The literal selected nonzero N, exact coefficient field L, both
actual returns, localization, and full calibrated scalar remain
required. The original slice satisfies \(X=a_0u+x_0\), \(x_0\in A\);
it is not normalized to \(X/a_0\).

Use the full arbitrary-n potentials of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md)
and the centered support of
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md).
All coefficient partials are the exact commuting partials on L.
The exact field \(\ker_L\partial_s\) is not identified with
\(\mathbb C(t)\).

Write \(P=\sigma\), and use460's affine intrinsic variables x,q.
Then
\[
\begin{gathered}
O=L[v]=L[x,P,q],\qquad
\deg_v P=2c,\quad \deg_vx=\deg_vq=3c,\\
\mathcal H=x^2+\frac e2q^2+T(P)=0,\qquad
T=t_3P^3+t_2P^2+t_1P+t_0,\quad t_3=f'''/6\ne0.
\end{gathered}
\tag{4}
\]
The complete fourth level and its primitive tangent component are
\[
\begin{aligned}
\Phi&=x\{T'+Dq\}+K_0+Jq+E_1q^2=0,\\
D&=d_0-2eP,\qquad E_1=e_tP/2+c_0,\\
J&=j_2P^2+j_1P+j_0,\qquad
K_0=f''''P^4/24+K_3(P),\quad\deg K_3\le3,\\
W&=2Dx^2-eDq^2+2xJ+4E_1xq-eqT'=-\psi P_v,
\qquad \psi\in L^*.
\end{aligned}
\tag{5}
\]
Thus \(\deg_vW=2c-1\). A prime on T is the formal P-derivative,
not a coefficient derivative. All lower coefficients and moving
levels in(4),(5) are the exact ones of460, not newly chosen equations.
The evaluated gradient minors of \(\mathcal H,\Phi\) generate O.

Let
\[
\eta=\frac{\operatorname{lc}_v x}{\operatorname{lc}_v q}\in L^*,
\qquad \gamma=\eta^2+e/2.
\]
The balanced conclusions460(26),(30),(33) give
\[
\gamma\ne0,\qquad
e_t=2e\eta-e^2/\eta,\qquad
f''''=-24e\,t_3/\eta.
\tag{6}
\]
Only these balanced identities are used. In particular none of
the strict Riccati identities is imported.

## 2. The complete fourth level becomes cubic

Make the linear intrinsic shear
\[
R=x-\eta q,\qquad \deg_vR<3c,\qquad
\mathcal H=\gamma q^2+2\eta Rq+R^2+T(P).
\tag{7}
\]
The degree of a zero R is understood as minus infinity.
This change is invertible over L and gives \(O=L[R,P,q]\).
It is not an actual complex ambient coordinate map.

Define exact coefficients and polynomials
\[
\begin{gathered}
\ell_*=\frac{\eta d_0+c_0}{\gamma},\qquad
d=d_0-2\eta\ell_*,\qquad M(P)=eP/\eta-\ell_*,\\
\mathcal B(P)=\eta T'(P)+J(P),\\
\mathcal F(P)=K_0(P)+(eP/\eta-\ell_*)T(P).
\end{gathered}
\tag{8}
\]
The symbol \(\ell_*\) is just this coefficient, not a transported
second potential. Likewise d is a coefficient, not an intrinsic degree.
The balanced identity(6) cancels the sole quartic coefficient:
\[
[P^4]\mathcal F=f''''/24+e t_3/\eta=0,
\qquad \deg\mathcal F\le3.
\tag{9}
\]
Substitute \(x=\eta q+R\) into the ENTIRE(5), then subtract the
polynomial multiple \((\ell_*-eP/\eta)\mathcal H\). The exact result is
\[
\boxed{
\Psi=(\mathcal B+dR)q+RT'+M(P)R^2+\mathcal F(P)=0.}
\tag{10}
\]
For example the old q-squared coefficient is
\(\eta D+E_1=\gamma(\ell_*-eP/\eta)\).
After its subtraction, the coefficient of Rq is the constant d,
which verifies the cancellation of its P-dependent part.
Every monomial of(10) has total degree at most three in the
independent formal variables R,P,q.

The invertible linear shear preserves the evaluated gradient-minor
ideal. Subtracting the displayed polynomial multiple preserves it
as well: on the curve, its differential is a multiple of
\(d\mathcal H\), because \(\mathcal H=0\).
Thus the two degree-at-most-three levels \(\mathcal H,\Psi\)
still vanish on the whole polynomial line and have a minor UNIT.
Neither is the zero formal polynomial, since their minor ideal is
the unit ideal.

## 3. The elementary degree bound improves to nine

Apply the elementary argument in Sections1--4 of
[299](principal-paraboloid-generic-degree-bound-pass299-working.md)
to the new generators R,P,q and the two cubic levels.
For clarity, its common-factor and whole-return steps are retained here.

Let G be their polynomial gcd, and write
\(\mathcal H=Gf_0,\ \Psi=Gg_0\), with \(f_0,g_0\) coprime.
If G evaluated to zero on the line, both evaluated gradients would
be multiples of the evaluated gradient of G, contradicting the
minor unit. Therefore its evaluation is nonzero and
\(f_0,g_0\) both vanish. The original minors are then \(G^2\)
times the reduced minors, so the evaluated G is a unit of \(O\).
The two reduced polynomials are nonconstant, of degrees
\[
1\le d_1=\deg f_0\le3,\qquad
1\le d_2=\deg g_0\le3.
\tag{11}
\]

Homogenize to these exact degrees. The homogeneous polynomials
are coprime: neither has a factor equal to the homogenizing variable,
and any other common homogeneous factor would dehomogenize to a
nonconstant common factor. The two injective multiplication sequences
in the four-variable polynomial ring give, for sufficiently large n,
\[
\dim_L\bigl(L[T_0,R,P,q]/(f_0^h,g_0^h)\bigr)_n
=d_1d_2n+\frac{d_1d_2(4-d_1-d_2)}2.
\tag{12}
\]
Evaluation maps this homogeneous quotient onto the span \(V_n\)
of evaluated polynomials of total degree at most n in R,P,q.
Extra components of the intersection do not affect this surjection.

The largest intrinsic degree of the generators is \(D_{\max}=3c\),
attained by q. Whole generation supplies polynomial expressions
for \(1,v,\ldots,v^{D_{\max}-1}\) in R,P,q with some common degree
bound C. Thus the \(D_{\max}(n-C+1)\) elements
\[
q^jv^i,\qquad 0\le i<D_{\max},\quad 0\le j\le n-C,
\]
belong to \(V_n\) and have pairwise distinct intrinsic degrees.
Comparing their number with(12) for arbitrarily large n proves
\[
\boxed{3c=D_{\max}\le d_1d_2\le9.}
\tag{13}
\]
This is the polynomial gcd and dimension proof, not the projective
argument in299 Section5. It assumes neither that the two levels
generate the entire curve ideal nor that their intersection is
irreducible. No rationality of L is used.

Therefore \(c\in\{1,2,3\}\). The separate complete parity exclusion
[470](principal-paraboloid-balanced-quadratic-sigma-parity-exclusion-pass470-working.md)
removes \(c=1\), yielding exactly(3).

## 4. A first remainder bound and its exact leading coefficient

The following gates use the full minor, independently of the
finite enumeration in(13). First,
\[
\deg_vR\le2c.
\tag{14}
\]
Indeed the P-dependent quadratic part of W in(5) factors by(6) as
\[
P(-4ex^2+2e_txq+2e^2q^2)
=-4ePR\left(x+\frac{e}{2\eta}q\right)
=-4ePR\left(R+\frac{\gamma}{\eta}q\right).
\tag{15}
\]
The last parenthesis has exact degree \(3c\), because
\(\gamma/\eta\ne0\) and \(\deg R<3c\).
If \(\deg R>2c\), (15) has degree \(5c+\deg R>7c\).
All remaining constant-coefficient quadratic terms of W have
degree at most \(6c\), and \(2xJ-eqT'\) has degree at most \(7c\).
The uniquely highest term cannot cancel. This contradicts
\(\deg W=2c-1\), proving(14), including R zero or constant.

In the complete cubic(10), the only possible degree-\(7c\) term
is \([P^2]\mathcal B\,P^2q\); all remaining terms have degree
at most \(6c\), using(14). Consequently
\[
j_2=-3\eta t_3,\qquad
[P^2](2\eta J-eT')=-6\gamma t_3.
\tag{16}
\]
No lower coefficient is discarded in deriving this gate.

For the next comparison put
\[
b_1=-4e\gamma/\eta\ne0,\qquad
b_0=4\gamma\ell_*+4\eta d,\qquad
\mathcal L(P)=2\eta J-eT'.
\]
Directly from(5)--(8), before evaluating the third level,
\[
\boxed{
W+2d\mathcal H=
q\{(b_1P+b_0)R+\mathcal L(P)\}
+(2D+2d)R^2+2JR+2dT.}
\tag{17}
\]
On the line, its right side is exactly W.

Write \(R=\rho_0P+S\), with \(\deg S<2c\);
choose \(\rho_0=0\) if \(\deg R<2c\).
The degree-\(7c\) coefficient in(17) forces
\(b_1\rho_0-6\gamma t_3=0\). Hence
\[
\boxed{
\rho:=\rho_0=-\frac{3\eta t_3}{2e}\ne0,\qquad
R=\rho P+S,\qquad \deg S<2c.}
\tag{18}
\]
In particular R has exact degree \(2c\); its previously allowed
zero or constant possibilities are now excluded by this calculation.

## 5. The second remainder has exact half degree

After(16),(18), the entire evaluated identity(17) can be written
\[
\begin{aligned}
W={}&q\{b_1PS+A_1P+b_0S+A_0\}\\
&+2dt_3P^3+6\eta t_3P^2S-4ePS^2+Q_2(P,S),
\qquad \deg_{\rm total}Q_2\le2,
\end{aligned}
\tag{19}
\]
where
\[
A_1=b_0\rho+[P]\mathcal L,\qquad A_0=[P^0]\mathcal L.
\]
All coefficients of Q2 are defined by expansion of(17); its full
untruncated non-q expression is
\[
(2D+2d)(\rho P+S)^2+2J(\rho P+S)+2dT.
\tag{20}
\]
Its P-cubed coefficient is \(2dt_3\), since
\(-4e\rho^2+2j_2\rho=0\). Its other total-degree-three
coefficients are exactly \(6\eta t_3P^2S-4ePS^2\).

If \(\deg S>c\), the term \(b_1PSq\) in(19) has degree
\(5c+\deg S>6c\) and is uniquely highest.
Indeed \(P^2S\) has degree \(4c+\deg S\), \(PS^2\) has
degree \(2c+2\deg S<5c+\deg S\), and the other terms are
bounded by these or by \(6c\). Therefore
\[
\deg S\le c.
\tag{21}
\]

Suppose next that S is constant, including zero.
Then \(O=L[R,P,q]=L[P,q]\), and(7) is monic quadratic in q
after division by \(\gamma\in L^*\). Thus
\([L(v):L(P)]\le2\).
For any nonconstant polynomial P of degree D, the elements
\(1,v,\ldots,v^{D-1}\) form a free \(L[P]\)-basis of \(L[v]\):
the leading coefficient of P permits successive degree reduction,
and distinct degrees modulo D prove independence.
Localizing gives \([L(v):L(P)]=D\).
This argument works over the exact field L without any assumption
about its rationality over \(\mathbb C\).
Here it gives \(2c\le2\). Thus S cannot be constant when \(c>1\).

If \(0<\deg S<c\), the uniquely highest term of(19) is initially
\(2dt_3P^3\), of degree \(6c\); hence d must vanish.
After d vanishes, \(b_1PSq\) is uniquely highest, of degree
\(5c+\deg S>5c\). All non-q terms have smaller degree, as do
the other three terms multiplying q. This is another contradiction.
We conclude, for every higher balanced profile \(c>1\),
\[
\boxed{\deg S=c,\qquad d\ne0.}
\tag{22}
\]
The nonvanishing of d follows from the two degree-\(6c\) terms
in(19): if d were zero, \(b_1PSq\) alone would survive.

For later use, let \(P_*,Q_*,S_*\) be the nonzero intrinsic
leading coefficients. The leading third and minor identities give
\[
\gamma Q_*^2+t_3P_*^3=0,\qquad
b_1P_*S_*Q_*+2dt_3P_*^3=0.
\tag{23}
\]
In particular
\[
\frac{S_*^2}{P_*}
=-\frac{\eta^2d^2t_3}{4e^2\gamma}\ne0.
\tag{24}
\]
This is only a relation between leading coefficients. It does
not prove \(P\in L[S]\), a polynomial inverse, or an exclusion
of either remaining profile.

## 6. Evidence and scope boundary

The complete current460 was freshly read through116cbe+c866b8,
and the full299 through b565f9 at SHA
b1de58a725dce4156e2ae54cc385cdb0f59a00091bf32f34f40384b2c58652ab.
Only299 Sections1--4 enter the degree bound. The held470 hash
b6f266fcfd5115185d8170254c2bab63a3698d8f922204bc63b5498556576779
was revalidated in b565f9 after its complete author read and
independent saved-source review.

Fresh unsaved819c94 reconstructed the entire cubic reduction,
the exact quartic cancellation, the full minor identity(17),
and every cubic monomial in(19),(20). Fresh001b51 checked the
expanded coefficient in(16) and the leading ratio(24).
Every stated residual was zero. Independent reconstructions by
General in d7f875 and Jet in88b9cb agree with these full identities.
The written degree comparisons and polynomial-basis argument
handle the zero and constant remainders; coefficient identities
alone are not substituted for those arguments.

The result is the smaller balanced frontier(3), with the exact
necessary restrictions(18),(22)--(24). The two remaining profiles
are not asserted to exist or to be excluded. No intrinsic shear
is promoted to a complex ambient coordinate change.
There is no new recognition or unrestricted cancellation claim,
and no recursive certification of retained historical dependencies.

No saved checker was executed, imported, compiled, or rerun.
No earlier source or canonical index was edited. No historical
novelty, human-expert review, or formal certification is claimed.
