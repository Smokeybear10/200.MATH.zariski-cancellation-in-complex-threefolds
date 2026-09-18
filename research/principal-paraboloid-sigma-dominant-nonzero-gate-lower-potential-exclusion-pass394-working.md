# The nonzero quadratic-cubic gate contradicts the lower genuine potential

Working exclusion: in the complete actual sigma-dominant pair
(deg theta,deg sigma)=(2,3), the explicit nonzero-E high-coefficient
normal form below is impossible. The r4 coefficient fixes the last
quadratic coefficient. The r3 coefficient and actual polynomial
return first leave one differential mode, then contradict it.

Entry into the displayed high-coefficient normal form is supplied by
the separately retained actual theorem392. No assertion is made that
the intrinsic degree pair without the full actual hypotheses implies
it. The zero-E case, other profiles and recognition of the original
invariant ring are outside this argument.

## 1. Actual hypotheses and precise high-coefficient input

Retain every actual264 hypothesis and the strict sigma-dominant
entry385/387, after the actual constant Y translation removes the
complex term gamma*t from n, and retain the high-coefficient conclusion
of [392](principal-paraboloid-sigma-cubic-nonzero-gate-normal-form-pass392-working.md).
This is the map Y*=Y+gamma/2 with
X,Z,W fixed, with its polynomial inverse and actual gates proved in
[389](principal-paraboloid-affine-theta-constant-t-intercept-exclusion-pass389-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E_0=\partial_u,\quad
\deg_{E_0}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=E_0X\ne0,\quad N=[u^4]\partial_Z|_{A_0}\ne0,\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,\quad
K=L(r)=\mathbb C(y,z,w),\\
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\quad Nr=\rho\in L^*,\\
k=s,\quad n=f\in S:=\ker_L\partial_t,\quad
\nu=f_s\ne0,\quad e=f_{ss}\ne0 .
\end{gathered}
\tag{1}
\]
All original slice, literal partial, polynomial/field return and
higher-potential conditions remain in force. Exact coefficient
partials commute and have joint constants C. They preserve S under
partial_s, and t is transcendental over S. No equality S=C(s) is
assumed.

Put
\[
\mathcal E=\frac{e_s}{6}-\frac{e^2}{2\nu}\in S^*.
\tag{2}
\]
The nonzero-E high-coefficient input consists of
\[
\begin{gathered}
F\in S^*,\quad B,D\in S,\quad
\ell=\tfrac12Ft^2+Bt+D,\quad p=\ell_t=Ft+B,\quad C=\ell_s+\nu^2,\\
a=\frac{32\nu^2\mathcal E}{e^2F}\in S^*,\qquad
b=\beta t+\beta_0,\\
\beta=8-\frac{8\nu F_s}{eF},\qquad
\beta_0=\frac{8B}{F}-\frac{8\nu B_s}{eF},\qquad
\frac{\mathcal E}{F^4}\in\mathbb C^*.
\end{gathered}
\tag{3}
\]
These equations retain zero values of F_s, B, B_s, D and beta.
The final condition is equivalently
\(\mathcal E_s/\mathcal E=4F_s/F\).
It is not assumed that every coefficient of L is rational in t.

Let c initially be an arbitrary element of L. The literal intrinsic
parametrization, with r affine nonconstant on the whole line, is
\[
\begin{aligned}
U=y&=r-\frac{p}{2\nu},\qquad V=\theta=ar^2+br+c,\\
P=\sigma&=\frac{ea^2}{4\nu}r^3+\frac{eab}{2\nu}r^2\\
&\quad+\left(\frac1{2\nu}+\frac{e(b^2+2ac)}{4\nu}
                  -\frac{Ca}{2\nu}\right)r
-\frac{p}{2\nu^2}+\frac{ebc-Cb}{2\nu}.
\end{aligned}
\tag{4}
\]
The third level is
\[
h=\frac{p^2}{4\nu^2}+\nu\ell+\frac e2c^2-Cc.
\tag{5}
\]
The full evaluated fourth polynomial, not an arbitrary cubic, is
\[
\begin{aligned}
Q={}&(2\ell_sP-2ePV-p)U+\frac{e_s}{6}V^3
-\frac F2P^2-\ell_{ts}PV-\frac{\ell_{ss}+2\nu e}{2}V^2\\
&-h_tP+(e\ell+\nu\ell_s-h_s)V .
\end{aligned}
\tag{6}
\]
It is constant in r. Derivatives of h in (6) are the actual exact
coefficient derivatives of (5). In particular
\[
\begin{aligned}
h_t&=\frac{pF}{2\nu^2}+\nu p+(ec-C)c_t-\ell_{ts}c,\\
h_s&=\frac{p\ell_{ts}}{2\nu^2}-\frac{p^2e}{2\nu^3}
 +e\ell+\nu\ell_s+\frac{e_s}{2}c^2\\
&\qquad-(\ell_{ss}+2\nu e)c+(ec-C)c_s .
\end{aligned}
\tag{7}
\]
The full actual scalar is the one obtained from
\[
\begin{gathered}
z=2ty+\sigma^2+\theta+f,\qquad
w=\ell-2\sigma y-\nu\theta,\\
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+s)X+t^2X^2,\quad
W=w+\theta X+sX^2,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,r)}
=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{8}
\]
All coefficient derivatives now fix r and the actual X.

## 2. The r4 gate fixes c with only known nonzero denominators

The relations (3) give
\[
F=\frac{32\nu^2\mathcal E}{ae^2},\qquad
\ell_{ts}=\frac{pe}{\nu}-\frac{4\nu\mathcal E b}{ea}.
\tag{9}
\]
These are the r6 and r5 gates of the genuine Q. Substituting them
and e_s=6E+3e^2/nu in (6) makes those two coefficients zero.
The next coefficient is exactly
\[
[r^4]Q=-\frac a{2e\nu}
\left(2\mathcal Eace\nu-8\mathcal EaC\nu+8\mathcal E\nu
-3ae^2\ell_s+ae\ell_{ss}\nu+2e^2\right).
\tag{10}
\]
Neither h_t nor h_s contributes to this coefficient: their factors
P,V have r degrees three and two.

Since a,e,nu,E are all nonzero, the coefficient equation uniquely gives
\[
\boxed{
c=\frac{4C}{e}
 +\frac{3e\ell_s/\nu-\ell_{ss}}{2\mathcal E}
 -\frac{4\mathcal E\nu+e^2}{ae\nu\mathcal E}.
}
\tag{11}
\]
No p, b, c or F_s was divided out. All right-hand coefficients lie
in S[t], of degree at most two. Write
\[
c=c_2t^2+c_1t+c_0,\qquad c_i\in S,
\quad
c_2=\frac{2F_s}{e}
       +\frac{3eF_s/\nu-F_{ss}}{4\mathcal E}.
\tag{12}
\]
For precision,
\[
\begin{aligned}
c_1&=\frac{4B_s}{e}
       +\frac{3eB_s/\nu-B_{ss}}{2\mathcal E},\\
c_0&=\frac{4(D_s+\nu^2)}e
       +\frac{3eD_s/\nu-D_{ss}}{2\mathcal E}
       -\frac{4\mathcal E\nu+e^2}{ae\nu\mathcal E}.
\end{aligned}
\tag{13}
\]
The lower functions B,D and these lower coefficients remain arbitrary
unless further literal equations constrain them.

We can now apply the fully read conditional polynomial-return theorem
[393](principal-paraboloid-sigma-dominant-polynomial-return-degree-gate-pass393-working.md).
Its explicit hypothesis is exactly the polynomial form (3),(4),(12)
together with the actual entry (1),(8). It proves
\[
L=S(t),\qquad S[A_0]=S[t,r]=S[t,y],\qquad
S[y,z,w]=S[t,y],
\tag{14}
\]
and, using the actual original slice and the polynomial-line
degree theorem after localization at S(y), the necessary gate
\[
\deg_t\sigma\le2
\quad\text{when }r=y+\frac{Ft+B}{2\nu}\text{ and y is held fixed}.
\tag{15}
\]
These are retained actual-ring consequences, not deductions from
rational field return alone. We do not infer (15) from an abstract
constant determinant or declare y an original polynomial coordinate.

## 3. The complete r3 coefficient and its two top modes

Set
\[
d=ec-C,\qquad
M=-8\mathcal Eab\nu^2+a^2e^2(p-\nu c_t).
\tag{16}
\]
Direct substitution of the actual h_t from (7), followed by the r4
identity (11), gives the COMPLETE coefficient
\[
\boxed{
[r^3]Q=
\frac{dM+8\mathcal Eb\nu^2+4ae^2p+4be^2\nu}{4e\nu^2}.
}
\tag{17}
\]
Here h_s contributes nothing to r3 because it multiplies V. No
derivative of c was silently suppressed; c_t occurs in M.

Let
\[
d_2=[t^2]d=ec_2-F_s/2,\qquad
M_1=[t]M=-8\mathcal Ea\beta\nu^2
                    +a^2e^2(F-2\nu c_2).
\tag{18}
\]
Both d and M are polynomials in t over S, of degree at most two
and one respectively. The last three terms of (17) have degree at
most one. Thus its t3 coefficient is d2*M1/(4e*nu^2).
It must vanish because [r3]Q=0 and t is transcendental over S.

This gives two exhaustive necessary modes in the field S:
\[
\begin{array}{c|c|c}
&c_2&F_{ss}\\ \hline
\mathrm I&
F_s/(2e)&(3e/\nu+6\mathcal E/e)F_s\\
\mathrm {II}&
F_s/e-F/(2\nu)&
(3e/\nu+4\mathcal E/e)F_s+2\mathcal EF/\nu .
\end{array}
\tag{19}
\]
For mode II, solve M1=0 using the known nonzero a,e,nu, then use
beta in (3). The displayed differential equations follow from (12).
The modes may overlap at this stage. No F_s division was used.

Introduce dimensionless coefficient functions and an operator
\[
q=\frac{\nu F_s}{eF},\qquad
k_1=\frac{\nu\mathcal E}{e^2}\ne0,\qquad
\mathcal D=\frac{\nu}{e}\partial_s.
\tag{20}
\]
This operator is only a convenient multiple of the exact coefficient
partial, not an actual locally nilpotent derivation. From (2),(3),
\[
\mathcal Dk_1=k_1(4q-5-12k_1).
\tag{21}
\]
A direct differentiation of q using (19), without dividing by q
or F_s, gives respectively
\[
\mathrm I:\quad \mathcal Dq=q(1-q),\qquad
\mathrm {II}:\quad \mathcal Dq=(1-q)(q+2k_1).
\tag{22}
\]

## 4. Actual polynomial return leaves only one of these modes

The coefficient of t3 in sigma after fixing y as in (15) depends
only on the leading coefficients. Put
\[
m=\frac{aF}{2\nu}+\beta=8(1+2k_1-q).
\tag{23}
\]
Expanding the complete (4), including its constant term, gives
\[
[t^3]\sigma\big|_y
=\frac m{4\nu}\left(\frac{eFm}{2\nu}+2d_2\right).
\tag{24}
\]
The coefficient B in p, and all lower coefficients of b,c, contribute
only smaller t degree. In the two modes this becomes
\[
\begin{aligned}
\mathrm I:\quad &[t^3]\sigma\big|_y
=\frac{8Fe}{\nu^2}(1+2k_1-q)^2,\\
\mathrm {II}:\quad &[t^3]\sigma\big|_y
=\frac{2Fe}{\nu^2}(1+2k_1-q)(3+8k_1-3q).
\end{aligned}
\tag{25}
\]
Every prefactor displayed in (25) is nonzero.

In mode I, the actual gate (15) forces q=1+2k1. Differentiate this
identity by D and use (21),(22). The difference
Dq-2Dk1 becomes 4k1^2, a nonzero element. Hence mode I is impossible.

In mode II, (15) gives q=1+2k1 or q=1+8k1/3. For the second root,
Dq-(8/3)Dk1 becomes -80k1^2/9, again nonzero. Only the first root
can remain. We have therefore proved the necessary identities
\[
\boxed{
q=1+2k_1,\quad
\frac{F_s}{F}=\frac e\nu+\frac{2\mathcal E}{e},\quad
c_2=\frac F{2\nu}+\frac{2\mathcal EF}{e^2},\quad
\beta=-\frac{16\nu\mathcal E}{e^2}.
}
\tag{26}
\]
This argument treats all overlaps and zero F_s boundaries as field
identities; it does not select roots at particular points.

## 5. The lower part of the SAME r3 coefficient is contradictory

No further giant coefficient expansion is needed. Use the complete
identity (17), still retaining arbitrary B,D,c1,c0.

Under (26), its coefficients (18) satisfy
\[
d_2=\frac{\mathcal EF}{e}\ne0,\qquad M_1=0.
\tag{27}
\]
Thus M is a t-constant element M0 of S. The t2 coefficient of (17)
is d2*M0/(4e*nu^2), with no contribution from its other terms.
Since [r3]Q=0, the known nonzero d2 forces M0=0.

Consequently all of the term dM is zero, including its lower
coefficients. The coefficient of t in the remaining expression (17) is
\[
\begin{aligned}
[t\,r^3]Q
&=\frac{8\mathcal E\beta\nu^2+4ae^2F+4\beta e^2\nu}{4e\nu^2}\\
&=\frac{16\mathcal E}{e}
                  \left(1-\frac{2\nu\mathcal E}{e^2}\right).
\end{aligned}
\tag{28}
\]
It must also vanish. Since E and e are nonzero, this forces
k1=1/2. But (21),(26) imply
\[
\mathcal Dk_1=-k_1(1+4k_1).
\tag{29}
\]
The left side is zero for the complex constant k1=1/2; the right
side is -3/2. This is impossible in characteristic zero.

Equivalently, writing d1=[t]d, the independent elimination identity is
\[
[t\,r^3]Q-\frac{d_1}{d_2}[t^2r^3]Q
=\frac{16\mathcal E(e^2-2\mathcal E\nu)}{e^3}
\tag{30}
\]
after the surviving mode. The division by d2 is licensed by (27).
No division by an unknown lower coefficient is needed.

Therefore no actual chart satisfies all of (1)--(8). This excludes
the nonzero-E high-coefficient normal form of the sigma-dominant
quadratic-cubic pair, conditional only on its explicitly retained
entry and high scalar/potential gates.

## 6. Boundaries and verification record

The crucial polynomial degree bound is the actual theorem393, whose
proof uses the original global slice, selected derivation, both exact
ring returns, and the one-variable embedding-line theorem. It is not
a consequence of the two formal relations alone. Entry into (3)
is supplied by the separately retained high-coefficient theorem392;
this note does not infer it from the intrinsic degree pair alone.

The proof retains the exact field S throughout. No equality S=C(s)
is assumed, no original coordinate is constructed, and no recognition
of A0 or arbitrary-chart normalization is claimed. The zero-E branch
is not covered. No conclusion about equal intrinsic degrees or a
theta-constant boundary is imported.

The complete held393 source was independently read through EOF in
afaa1b at SHAba11c9f5bd57f6358ca3dad827d5e6f6e52475af748e58b40975782caa93a116.
The complete held392 source was read through EOF in8f8530 at
SHA454440efc1b4fbf2100ed2b8509938ef3194f8bd2a47e94cfb09670bc227b426.
The earlier complete385/387 input and the actual constant translation
have also been read and checked directly.

Fresh unsaved7eab38 reconstructed r6,r5,r4 and (11).
Fresh54f073 retained both actual derivatives (7) while computing the
lower coefficients. Fresh39dc94 independently rebuilt the r3*t3
factor, both highest-r2 differentiated-mode cancellations, the full
fixed-y sigma3 coefficient, and every dimensionless root comparison.
The latter r2 cancellations are not needed for the proof and do not
claim that the complete r2 coefficient vanishes.

Most importantly, a separate full literal reconstruction03a2ae,
completed on its original handle14714 in f14322, gave zero for the
entire difference between Q[r3] and (17), not merely its highest term.
It then independently verified (27),(30) while keeping all lower
functions free. These finite identities supplement the exact-field,
degree and actual-ring arguments; they do not certify those arguments.

No saved checker was executed, imported, compiled or rerun.
No held source, canonical index or ledger was edited. No unrestricted
cancellation, novelty, human-expert review, publication or
proof-assistant certification is claimed.
