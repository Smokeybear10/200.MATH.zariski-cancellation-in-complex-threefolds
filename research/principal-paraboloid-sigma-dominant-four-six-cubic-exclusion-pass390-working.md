# The literal cubic excludes the sigma-dominant degree pair (4,6)

Working exclusion: in the full actual385 chart after387, the pair
(deg theta,deg sigma)=(4,6) is impossible. The exact intrinsic
degree-(2,4,6) normal form of370 and the finite filtered-ideal
argument of373 do transfer, but the literal cubic must be rebuilt.
Its new highest part is not obtained by interchanging sigma and
theta in the earlier exclusion.

The sole original-coordinate change below is a complex translation
of Y. All later changes are in polynomial rings over the exact
coefficient field L. No rationality, original-coordinate descent,
or recognition of the remaining profiles is claimed.

## 1. Actual entry and a legitimate constant translation

Retain every actual hypothesis of
[385](principal-paraboloid-nonlinear-sigma-dominant-degree-reduction-pass385-working.md)
and the established conclusion of
[387](principal-paraboloid-sigma-dominant-coefficient-integrability-pass387-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_{A_0},\\
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\quad
K=L(v)=\mathbb C(y,z,w),\\
k=s,\quad n_{ss}\ne0,\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The original partial, exact coefficient partials, strong field
return, whole ring return and full calibration are all retained.
Assume for contradiction that
\[
(\deg_v\theta,\deg_v\sigma)=(4,6).
\tag{2}
\]
By387 the leading ratio lambda is zero and
n=gamma*t+f, where gamma is complex and f belongs to
S=ker_L(partial_t). We do not assume S=C(s).

Make the actual polynomial change
\[
X^*=X,\quad Y^*=Y+\gamma/2,\quad Z^*=Z,\quad W^*=W.
\tag{3}
\]
Its inverse subtracts gamma/2 from Y*. The literal coefficients are
t*=t, s*=s, sigma*=sigma, theta*=theta,
y*=y+gamma/2, z*=z and w*=w. The two defining potentials give
\[
n^*=n-\gamma t=f,\qquad \ell^*=\ell.
\tag{4}
\]
Indeed z=2t*y*+sigma^2+theta+f, and
w+2sigma*y*+f_s*theta equals the old
w+2sigma*y+gamma*sigma+n_s*theta.

The actual Jacobian and coefficient parameter change have determinant
one. The exact time degrees and full initial ideal are unchanged,
because only a constant was added. The literal Z-partial and its
selected coefficient N are identical. The intercept transformation
is a complex translation, so both returns in(1) remain true, and
the full determinant is unchanged. We may drop stars and use
\[
n_t=0,\quad n=f\in\mathcal S,\quad
\nu=n_s\ne0,\quad e=n_{ss}\ne0,
\quad n_{ts}=0.
\tag{5}
\]
The nonvanishing of nu follows from nu_s=e. The constant translation
does not alter either degree in(2).

## 2. Rebuild the literal quadric and cubic

Let U,P,V be independent formal variables, evaluating respectively
to y,sigma,theta. Put C=ell_s+nu^2. The complete third level is
\[
\mathsf H=U^2-2\nu PU+\frac e2V^2-\ell_tP-CV+\nu\ell-h_0.
\tag{6}
\]
The complete genuine fourth level, with its evaluated constant
subtracted, is
\[
\begin{aligned}
\mathsf Q={}&(2\ell_sP-2ePV-\ell_t)U+\frac{e_s}{6}V^3
 -\frac{\ell_{tt}}2P^2-\ell_{ts}PV\\
&-\frac{\ell_{ss}+2\nu e}{2}V^2-(h_0)_tP
 +(e\ell+\nu\ell_s-(h_0)_s)V-q_0.
\end{aligned}
\tag{7}
\]
These are direct substitutions of(5) into385's full polynomials.
In particular no derivative of h0 or coefficient of ell has been
discarded. They both vanish on the intrinsic polynomial line and
retain the unit ideal of evaluated gradient minors.

Define the affine formal variable
\[
R=U+\frac{\ell_t}{2\nu},\qquad
D=\frac{\ell_t^2}{4\nu^2}+\nu\ell-h_0.
\tag{8}
\]
In the independent formal variables R,P,V,
\[
\mathsf H=R^2-2\nu PR+\frac e2V^2
              -\frac{\ell_t}{\nu}R-CV+D.
\tag{9}
\]
By385's remainder degree relation, its evaluated R has degree two:
deg sigma+deg R=2deg theta. Thus the three degrees of R,V,P are
(2,4,6), and in particular y also has degree two in this case.

For ordinary total degree in R,P,V, the exact highest parts are
\[
\boxed{
\mathsf H_2=R^2-2\nu PR+\frac e2V^2,\qquad
\mathsf Q_3=-2ePVR+\frac{e_s}{6}V^3.
}
\tag{10}
\]
The shift of U by a coefficient in L contributes only lower-degree
terms to(7). The term -2ePVR makes Q have exact total degree three,
whether or not e_s vanishes. This is the new literal support used
below; it is different from373's PR^2/t support.

## 3. The exact degree-(2,4,6) lemma applies over L

The affine coefficient-field transformation
\[
\begin{gathered}
p_{\rm old}=R,\qquad x=V-C/e,\qquad
q_{\rm old}=P-\frac R{2\nu}+\frac{\ell_t}{2\nu^2},\\
\beta=-\frac{4\nu}{e}\ne0,\qquad
d=\frac{C^2}{e^2}-\frac{2D}{e}
\end{gathered}
\tag{11}
\]
has explicit inverse
\[
R=p_{\rm old},\quad V=x+C/e,\quad
P=q_{\rm old}+\frac{p_{\rm old}}{2\nu}
                 -\frac{\ell_t}{2\nu^2},\quad
U=p_{\rm old}-\frac{\ell_t}{2\nu}.
\tag{12}
\]
Direct substitution gives
\[
\frac{2\mathsf H}{e}=x^2+\beta p_{\rm old}q_{\rm old}-d,
\quad O=L[p_{\rm old},x,q_{\rm old}],\quad
(\deg p_{\rm old},\deg x,\deg q_{\rm old})=(2,4,6).
\tag{13}
\]
These degrees are unchanged by the lower-degree affine additions.
The transformed genuine Q is a cubic vanishing on the line and is
not a multiple of the quadric: such a multiple would make every
evaluated two-gradient minor zero. The unit-minor statement persists
under the invertible formal affine change, with coefficient elements
held fixed during formal differentiation.

These are exactly the abstract inputs of the fully read
[370](principal-paraboloid-degree-two-four-six-odd-part-normal-form-pass370-working.md).
That proof uses the two possible parity forms, excludes its Type II
by ruling degrees (2,4) versus a cubic section (3,3), and retains
Type I for both zero and nonzero centered level d. It does not
require the earlier theta-dominant reciprocal formula for n.
Therefore, after a parameter translation and unit rescalings over L,
write p=R/alpha and q=alpha*beta*q_old, with alpha in L*, to obtain
\[
\begin{gathered}
p=v_1^2-\delta,\qquad K_1(p)=A p+B,\quad A,\varepsilon\in L^*,\\
x=pK_1(p)+\varepsilon v_1,\qquad
q=-pK_1(p)^2-2\varepsilon v_1K_1(p)-\varepsilon^2,
\qquad d=\varepsilon^2\delta.
\end{gathered}
\tag{14}
\]
This use of370 is a transfer of its checked abstract hypotheses,
not an exchange of the original sigma and theta coordinates.

## 4. The complete curve ideal and bounded cubic multipliers

In L[p,x,q] put
\[
H_c=x^2+pq-d,\qquad
G_c=q+2K_1(p)x-pK_1(p)^2+\varepsilon^2.
\tag{15}
\]
The exact ideal computation in373 applies to(14). For completeness,
the formal polynomial change
p1=p, x1=x-pK1, q1=q+2K1*x-pK1^2 preserves x^2+pq and has inverse
p=p1, x=x1+p1K1, q=q1-2K1*x1-p1K1^2.
It sends Gc to q1+epsilon^2. Eliminating q1 leaves
L[p1,x1]/(x1^2-epsilon^2*p1-d), which is L[x1]. Its evaluation
x1=epsilon*v1 is an isomorphism to O. Hence Hc,Gc generate the
entire evaluation kernel, without localization or saturation.

Pull Gc back through(11) and the rescalings. The resulting G has
\[
\ker\bigl(L[R,P,V]\longrightarrow O\bigr)=(\mathsf H,G),
\qquad G_3=\gamma_0R^3,\quad
\gamma_0=-A^2/\alpha^3\ne0.
\tag{16}
\]
Only -pK1^2 contributes degree three to Gc; the other terms have
degree at most two. Since e is nonzero, R does not divide H2 in(10),
so the two highest forms H2 and G3 are coprime.

The finite filtered-degree lemma of the fully read
[373](principal-paraboloid-degree-four-six-filtered-cubic-exclusion-pass373-working.md)
now gives, for the actual cubic Q in this exact ideal,
\[
\mathsf Q=L_1\mathsf H+\eta G,
\qquad \deg L_1\le1,\quad \eta\in L.
\tag{17}
\]
Its justification is elementary: in any representation, a cancellation
above degree three between the products of degrees two and three has
top multipliers divisible by the opposite coprime highest forms.
Subtract the corresponding multiple of G from the first multiplier
and add the same multiple of H to the second. Both multiplier top
degrees fall. Repetition terminates in a representation of the
bounded degrees in(17). This does not assume the initial multipliers
were already bounded.

## 5. The new literal support contradicts the complete ideal

Let the linear part of L1 be lP*P+lR*R+lV*V. The degree-three part
of(17) is the exact identity in independent formal variables
\[
-2ePVR+\frac{e_s}{6}V^3
=(l_PP+l_RR+l_VV)
  \left(R^2-2\nu PR+\frac e2V^2\right)+\eta\gamma_0R^3.
\tag{18}
\]
The P^2R coefficient forces -2nu*lP=0, hence lP=0.
The PR^2 coefficient then forces -2nu*lR=0, hence lR=0.
The R^2V coefficient forces lV=0. The right side is now a scalar
multiple of R^3, whereas the left side has PRV coefficient -2e,
which is nonzero. This is a contradiction.

Neither the possible zero e_s nor any lower coefficient of ell was
divided out. The argument also retains d=0 and delta=0. Its nonzero
gates are nu,e and the units alpha,A,epsilon from370, each established
before use. Consequently
\[
\boxed{\text{Under the complete actual385 and387 hypotheses,}
\quad(\deg_v\theta,\deg_v\sigma)\ne(4,6).}
\tag{19}
\]
This does not settle the remaining pairs(1,2) or(2,3), and gives no
assertion about equal degrees or arbitrary coupling k.

## 6. Scope and evidence

The whole-ring degree-(2,4,6) quadric controls in370 remain valid:
they carry some transverse cubic, but not the literal cubic(7).
Every formal automorphism and field rescaling after(3) is used only
inside a coefficient-field polynomial ring. No resulting generator
is declared to lie in the original invariant ring as a coordinate.

The full385 source was read through EOF in ce41c6. The complete370
and373 sources were read through EOF in156e62 before their lemmas
were used. Their abstract hypotheses and the new actual translation
are verified explicitly above.

Fresh unsaved cfe198 reconstructed the complete literal H,Q under
(5), both highest parts(10), the quadric identity and affine inverse
in(11)--(13), the ordered monomial coefficients in(18), and both
potential identities under the actual translation(3). Every residual
was zero. These identities supplement the written whole-ideal and
finite-degree arguments; they do not certify them by finite testing.

No saved checker was executed, imported, compiled or rerun by this
author. No earlier source or canonical index was edited. No broader
recognition, unrestricted cancellation, novelty, human-expert review
or proof-assistant certification is claimed.
