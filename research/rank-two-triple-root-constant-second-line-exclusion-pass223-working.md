# The triple-root constant-second line is impossible

Status: working exclusion of one actual projected-line type for
the binary quartic root partition \(3+1\). The normalized ratio is
\(q=t/\rho\), the second projection is constant, and the first is
affine. A scalar-Jacobian split followed, in one branch, by an
actual two-variable derivation argument excludes it.

Together with the local cubic-line argument221, this excludes the
projected lines for partition \(3+1\). Projected components of
degrees two and three are not treated in this note. No arbitrary
frame-entry or unrestricted cancellation theorem is asserted.

## 1. The actual normalized chart

Assume a globally sliced actual polynomial frame with the entire
initial kernel
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z\mathsf W-\mathsf X^3\mathsf Y).
\end{gathered}
\tag{1}
\]
Here \(T\) is independent. The actual selected construction in
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
gives
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\qquad
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=t/\rho,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\vartheta,\sigma\in L[v],\quad L[y,z,w]=L[v],\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
 =J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
The determinant holds \(X\) fixed. The field \(L\) lies in
\(\operatorname{Frac}A\), so \(E\) kills \(L\); the ratios \(t,\rho\)
are algebraically independent. Also \(Na=Nb=Ne_0=Nh_0=0\).
Extend \(N\) to \(A[u]\) by \(Nu=0\).

The additional line hypotheses in this note are
\[
\vartheta\in L,\qquad \deg_v y=1.
\tag{3}
\]
Thus \(L[y]=L[v]\). Using \(y\) as a parameter for calculation
changes the calibrated determinant to
\[
j=\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,y)}
 =J_0/y_v\in L^*.
\tag{4}
\]
This is a parameter substitution over \(L\), not an original
coordinate change. Coefficient derivatives still agree with the
fixed extensions of \(\partial_t,\partial_\rho\) on \(L\).

## 2. All projected entries are affine

Use the universal Taylor polynomials \(H_i\) and coefficients
\(k,n,\ell\in L\). The first three potentials are
\[
\begin{gathered}
\sigma=q_ty+q_\rho\vartheta+k,\\
z=q_\rho w+H_2(q;y,\vartheta)+k_ty+k_\rho\vartheta+n,\\
Rw+H_3(q;y,\vartheta)+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)=\ell,\\
R=q_{t\rho}y+q_{\rho\rho}\vartheta+k_\rho
 =-y/\rho^2+2t\vartheta/\rho^3+k_\rho .
\end{gathered}
\tag{5}
\]
Here \(H_i(c;U,V)=\sum_{j=0}^i
c_{t^j\rho^{i-j}}U^jV^{i-j}/(j!(i-j)!)\), with coefficient
derivatives taken before evaluation.
The return is degree one in \(y\). Since \(q_{ttt}=0\), the
third potential has degree at most two on its right side after
solving for \(Rw\). Thus \(w\) is affine in \(y\).
Since \(q_{tt}=0\), the second potential makes \(z\) affine too:
\[
\begin{gathered}
w=\lambda y+\omega,\qquad z=\kappa y+\zeta,\qquad
\lambda,\omega,\kappa,\zeta\in L,\\
\kappa=k_t-\frac{\vartheta+t\lambda}{\rho^2},\qquad
\sigma=\frac{y}{\rho}-\frac{t\vartheta}{\rho^2}+k .
\end{gathered}
\tag{6}
\]
In particular \(\lambda\) need not yet be complex or nonzero.

## 3. Scalar coefficients separate the two slope branches

The complete actual map is
\[
\begin{aligned}
Y&=y+tX,\\
Z&=\kappa y+\zeta+
   (y/\rho-t\vartheta/\rho^2+k)X+(t/\rho)X^2,\\
W&=\lambda y+\omega+\vartheta X+\rho X^2 .
\end{aligned}
\tag{7}
\]
Define
\[
\eta=\lambda-\vartheta_t,\qquad
H=-\vartheta/\rho^2-t\vartheta_t/\rho^2+k_t-\kappa
 =t\eta/\rho^2 .
\tag{8}
\]
The last equality uses precisely the second-potential formula
for \(\kappa\) in (6).

Expansion along the first row \((X,0,1)\) gives
\[
\begin{aligned}
j&=(Z_t-XZ_y)W_\rho+Z_\rho(XW_y-W_t)\\
&=(\kappa_t y+\zeta_t+HX)W_\rho
             +Z_\rho(\eta X-\lambda_t y-\omega_t),\\
W_\rho&=\lambda_\rho y+\omega_\rho+\vartheta_\rho X+X^2,\\
Z_\rho&=\kappa_\rho y+\zeta_\rho+
 \left(-y/\rho^2+2t\vartheta/\rho^3
                   -t\vartheta_\rho/\rho^2+k_\rho\right)X
                   -(t/\rho^2)X^2 .
\end{aligned}
\tag{9}
\]
Coefficients here are extracted from the entire polynomial in
the independent variables \(X,y\). In particular,
\[
\begin{aligned}
[Xy^2]j&=\lambda_t/\rho^2,\\
[X^2y]j&=\kappa_t+t\lambda_t/\rho^2-\eta/\rho^2,\\
[y^2]j&=\kappa_t\lambda_\rho-\kappa_\rho\lambda_t .
\end{aligned}
\tag{10}
\]
Since \(j\in L^*\), these give
\[
\lambda_t=0,\qquad
\kappa_t=\eta/\rho^2,\qquad
\kappa_t\lambda_\rho=0.
\tag{11}
\]

If \(\lambda_\rho\ne0\), then \(\kappa_t=\eta=H=0\).
The whole determinant in (9) reduces to
\[
j=\zeta_tW_\rho-\omega_tZ_\rho,\qquad
[Xy]j=\omega_t/\rho^2,\qquad
[X^2]j=\zeta_t+t\omega_t/\rho^2 .
\tag{12}
\]
These coefficients force \(\omega_t=\zeta_t=0\), and hence
\(j=0\), contradicting (4).

In the only remaining branch, \(\lambda_\rho=0\), so both
coefficient partials kill \(\lambda\). This implies
\[
\lambda\in\mathbb C .
\tag{13}
\]
For completeness, take its monic minimal polynomial over
\(\mathbb C(t,\rho)\). Differentiating it by either partial
gives a polynomial of smaller degree vanishing at \(\lambda\);
minimality forces every coefficient derivative to vanish.
Those rational coefficients therefore lie in \(\mathbb C\).
Since \(\mathbb C\) is algebraically closed, (13) follows.
This argument does not assume \(L=\mathbb C(t,\rho)\).

## 4. An actual nice derivation over a two-variable UFD

Now the shear
\[
U=W-\lambda Y,\qquad W=U+\lambda Y
\tag{14}
\]
is an actual polynomial coordinate change in both directions,
fixing \(X,Y,Z\). Put
\[
\mathcal P=aN-(NX)E,\qquad \tau=aNy.
\tag{15}
\]
It preserves the original ring, fixes \(X\), kills \(L\), and
commutes with \(E\). On \(B_a=A_a[X]\) it restricts to \(aN\)
on \(A_a\) and fixes \(X\). Since \(Na=0\), that localization is
locally nilpotent, so its restriction to the preserved ring \(B\)
is locally nilpotent as well.

Equations (6)--(7), differentiated in the line parameter, give
\[
\begin{gathered}
\mathcal PX=\mathcal PU=0,\qquad
\mathcal PY=\tau\ne0,\qquad
\mathcal PZ=\tau(\kappa+X/\rho),\\
\mathcal P^2Y=\mathcal P^2Z=0,\qquad E\tau=0 .
\end{gathered}
\tag{16}
\]
In particular \(\tau=\mathcal PY\) is an actual polynomial.
Its invariance follows also from
\(E(\mathcal PY)=\mathcal P(EY)=\mathcal Pb=0\).
No regularity of \(\rho\) or \(\kappa\) individually is asserted.

Let \(\Delta\) be the gcd of the components of \(\mathcal P\)
in the actual coordinates \(X,U,Y,Z\), and put \(D=\mathcal P/\Delta\).
The identity
\(\mathcal P\Delta=\Delta D\Delta\) and additivity of LND degree
force \(\mathcal P\Delta=0\): otherwise the two sides have,
respectively, degree \(\deg_{\mathcal P}\Delta-1\) and at least
\(\deg_{\mathcal P}\Delta\).
Thus \(D\Delta=0\), and
\(D^nf=\mathcal P^nf/\Delta^n\). Consequently \(D\) is a
nonzero irreducible polynomial LND, still killing \(X,U\),
with \(D^2Y=D^2Z=0\).

Moreover \(\Delta\mid\tau\in\ker E\), so additivity of
\(E\)-degree forces both \(E\Delta=0\) and \(E(\tau/\Delta)=0\).
In particular
\[
[E,D]=0,\qquad DY=\tau/\Delta\ne0,\qquad E(DY)=0 .
\tag{17}
\]
This is the needed actual primitive invariance gate.
It has not been inferred merely from a rational expression.

Set \(S=\mathbb C[X,U]\). We have the actual presentation
\(B=S[Y,Z]\), where \(S\) is a UFD containing \(\mathbb Q\).
Apply exactly Lemma2.3(ii) in
[Dasgupta--Gupta](https://arxiv.org/html/1701.03635v1#S2.Lem3),
with these two remaining polynomial variables. Its assumptions
are precisely that \(D\) is an irreducible \(S\)-linear LND and
that \(D^2Y=D^2Z=0\). Its needed conclusion is
\[
DY,\ DZ\in S.
\tag{18}
\]
This is the UFD statement, not a slice theorem over a PID.

## 5. Exact weighted degree produces the contradiction

The actual \(E\)-degrees of \(X,U\) are one and two. Indeed
\(U=W-\lambda Y\) with complex \(\lambda\), so its quadratic
leader is still \(h_0=a^2\rho\).
Give \(X,U\) the weights one and two. A nonzero homogeneous
polynomial of weight \(n\) has evaluated leading term
\[
\sum_j c_j a^{n-2j}(a^2\rho)^j
 =a^n\sum_jc_j\rho^j\ne0.
\tag{19}
\]
Distinct monomials have distinct powers of \(\rho\), and \(\rho\)
is transcendental over \(\mathbb C\). It follows that the exact
\(E\)-degree of every nonzero element of \(S\) is its weighted
degree. In particular \(S\cap\ker E=\mathbb C\), without any
assumption that the raw speed \(a\) is independent of \(\rho\).

Combining (17)--(19) gives \(DY=d\in\mathbb C^*\). Dividing the
\(\mathcal PZ\) identity in (16) by \(\Delta\) now yields
\[
DZ=d(\kappa+X/\rho),\qquad
E(DZ)=da/\rho\ne0,\qquad E^2(DZ)=0.
\tag{20}
\]
The equality is in the fraction field, but \(DZ\) is an actual
polynomial in \(S\) by (18). Its exact \(E\)-degree is one.
The weighted-degree conclusion therefore forces
\[
DZ=c_1X+c_0,\qquad c_1\in\mathbb C^*,\quad c_0\in\mathbb C .
\tag{21}
\]
Comparing (20)--(21) as polynomials in \(X\) over \(L\) gives
\(d/\rho=c_1\). This contradicts the transcendence of \(\rho\).
Thus the constant-slope branch is impossible as well.

## 6. Relation to the triple-root pair directions

For a general root partition \(3+1\), write
\(F_4=c\,l^3m\) with independent complex linear forms \(l,m\)
and \(c\ne0\). If the selected component is a line, its leading
factor in220 corresponds either to two copies of \(l\), or to
the pair \(l,m\).

For the first type, the actual constant linear change
\(X_*=l(X,Y),Y_*=m(X,Y)\), followed by \(Z_*=Z/c\),
normalizes the full kernel to that in (1).
The projection transport in Section2 of
[line221](rank-two-squarefree-quartic-line-exclusion-pass221-working.md)
gives, for \(l(t)=l(1,t)\),
\[
\vartheta_*=\vartheta/l-2\rho l' y/l^2,\qquad
l^2\vartheta-2\rho ll'y=l^3\vartheta_* .
\tag{22}
\]
The old pair line therefore makes \(\vartheta_*\) constant.
The invertible projected linear transformation preserves \(L[v]\),
so \(y_*\) is affine nonconstant.
The good change preserves the literal quadratic pivot, and the
constant bad-coordinate scaling multiplies its selected \(N\)
by \(c\), leaving \(L\) unchanged. The local slice may be rescaled
by \(1/c\). Exact degrees and the entire initial ideal transform
by these actual automorphisms. The new chart satisfies all
assumptions used above.

For the distinct-pair line instead take \(X_*=m,Y_*=l\).
After a constant bad-coordinate rescaling, \(q=t^3/\rho\), and
the exact pair transport in line221 gives
\(y=(t/\rho)\vartheta+\nu\).
The local argument in its Sections3--5 still applies: it only
uses the nonzero cubic coefficient \(\alpha_0\), and in this
specialization \(\alpha_0=1,\beta_0=\gamma_0=0\).
Its return coefficient is \(-t^3/\rho^3\ne0\), its quadratic
projected coefficient is \((t/\rho)^3\), and the same primitive
Wang/Laurent contradiction excludes that line.
No squarefree assumption enters those local steps once the
line and its direction are supplied.

Hence partition \(3+1\) has no actual projected line of either
pair type. This does not exclude its degree-two or degree-three
projected components or prove recognition for the full partition.

The complete retained actual sources and exact primary UFD
statement were freshly read before use. New unsaved algebra checked
the literal determinant, the three high coefficients, the potential
identity for \(H\), and the remaining two coefficients in (12).
No saved checker was executed, imported or compiled. No prior
source, index or packet was edited. This is a bounded working
argument, not human expert review, proof-assistant certification,
historical novelty clearance or an unrestricted cancellation result.
