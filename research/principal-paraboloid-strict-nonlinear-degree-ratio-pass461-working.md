# The strict nonlinear first-slope degree ratio is exactly two

Working necessary result: under EVERY actual hypothesis of264, let
k=s+f, f_s=0, n_ss nonzero and f''' nonzero. In the nonconstant-sigma
strict alternative of460, write a=deg(sigma) and
r=deg(y)=deg(theta), so 2r>3a. Then
\[
\boxed{r=2a.}
\tag{1}
\]
Together with460, the nonconstant-sigma degree ratios are therefore
r=3a/2 or r=2a. This note does not bound a, exclude either remaining
ratio, treat arbitrary actual-frame entry, or recognize the original
invariant ring. The proof uses the complete genuine fourth support
and its primitive tangent minor, not a bounded search.

## 1. Exact actual hypotheses and the strict input

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md)
and
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md).
In particular the original ring B=C[X,Y,Z,W]=A[u] is globally sliced
by E=partial_u, the exact E-degrees are (1,2,2,2), and the ENTIRE
weighted initial kernel is mathsf X^2*mathsf Z-mathsf Y^2.
The literal selected nonzero N, its exact coefficient field L,
both original returns, coefficient localization and the full calibrated
scalar -a0^4 remain required. No original slice normalization is made:
X=a0*u+x0 with x0 in A, not necessarily zero.

The coefficient partials commute and have joint constants C. Assume
\[
k=s+f,\quad f\in F=\ker_L\partial_s,\quad
e=n_{ss}\ne0,\quad f'''\ne0,
\quad a=\deg_v\sigma>0.
\tag{2}
\]
The exact field F need not be rational. Primes on f denote its exact
t-derivatives. A formal P-derivative will be distinguished below.

Use the affine intrinsic centering of460, with P=sigma after evaluation.
It gives
\[
\begin{gathered}
O=L[v]=L[x,P,q],\qquad
\mathcal H=x^2+\frac e2q^2+T(P)=0,\qquad
\deg T=3,\quad t_3:=[P^3]T=f'''/6\ne0,\\
\deg_vx=\deg_vq=r=\deg_vy=\deg_v\theta,
\qquad 2r>3a.
\end{gathered}
\tag{3}
\]
Here q=theta+(bP-C0)/e, b=n_ts, C0=ell_s+(n_s)^2; thus the
centering of q changes theta only by an affine polynomial in P.
The full polynomial T, including its moving level, is460(8).

The strict coefficient conclusions of460 give
\[
\eta=\frac{\operatorname{lc}_v x}{\operatorname{lc}_v q}\in L^*,
\qquad e=-2\eta^2,\qquad e_t=-8\eta^3,\qquad e_s=0.
\tag{4}
\]
Only these exact identities, not an integration ansatz for eta, are
needed below.

## 2. A linear shear and the entire reduced fourth support

Put
\[
z=x-\eta q,\qquad m=\deg_v z<r.
\tag{5}
\]
This is an invertible linear change over L, not a complex ambient
coordinate change. It gives the entire third level
\[
\mathcal H=z^2+2\eta zq+T(P)=0,
\qquad O=L[z,P,q].
\tag{6}
\]
The polynomial z is not zero, since T(P) is nonconstant. Its degree
m is nonnegative. In(6), the degree of zq is m+r, strictly greater
than 2m, so its nonzero leading term must balance T(P). Hence
\[
\boxed{m+r=3a,\qquad r\le3a.}
\tag{7}
\]

For clarity, before this shear the COMPLETE fourth level460(11),(12),
using(4), is
\[
\begin{aligned}
\Phi={}&x\{T'(P)+D(P)q\}
 +\frac{f''''}{24}P^4+K_3(P)+J_2(P)q
 +(-4\eta^3P+c_0)q^2,\\
D(P)&=d_0+4\eta^2P,\qquad d_0=b-ef',\qquad
\deg K_3\le3,\quad\deg J_2\le2.
\end{aligned}
\tag{8}
\]
The prime on T is its formal P-derivative. All lower coefficients
are the exact ones defined by460 and the genuine458 potential.
In particular c0,d0 belong to L and do not depend on the intrinsic
parameter. No moving-level term is deleted.

Substitute x=z+eta*q, then subtract D(P)*Hcal/(2eta). Define
\[
\begin{aligned}
C&=c_0+\eta d_0,\\
B(P)&=\eta T'(P)+J_2(P)=B_2P^2+B_1P+B_0,\\
F(P)&=\frac{f''''}{24}P^4+K_3(P)-\frac{D(P)}{2\eta}T(P)
       =F_4P^4+F_3P^3+F_2P^2+F_1P+F_0.
\end{aligned}
\tag{9}
\]
Here C is a coefficient, not the complex field. The resulting ENTIRE
fourth relation is
\[
\boxed{\Psi=Cq^2+B(P)q+zT'(P)-\frac{D(P)}{2\eta}z^2+F(P)=0.}
\tag{10}
\]
All divisions are by eta in L*. The Pq^2 terms cancel exactly by(4).
The coefficient F4 is f''''/24-2eta*t3, but its differential form
is not needed in the degree argument.

## 3. The exact minor degree survives both operations

The evaluated gradient minors of Hcal and Phi generate O by460.
The invertible linear shear preserves that ideal. Subtracting the
polynomial multiple D(P)*Hcal/(2eta) also preserves it on the curve:
the derivative of the multiplier is multiplied by Hcal and evaluates
to zero, while the remaining added gradient is a multiple of grad Hcal.
Both new level equations vanish on the whole polynomial line.

Whole generation O=L[z,P,q] differentiates to a polynomial combination
of (z',P',q') equal to one. The primitive tangent argument of460
therefore gives, for some psi in L*,
\[
W:=(\mathcal H_z\Psi_q-\mathcal H_q\Psi_z)_{\rm ev}
     =-\psi P',\qquad \deg_v W=a-1.
\tag{11}
\]
Primes in(11) are intrinsic v-derivatives fixing L. In formal order
(z,P,q), this minor is minus the second cross-product component.
In fact it equals the previous such component after evaluation, but
only the exact degree in(11) is needed.

Differentiating the ENTIRE(10) gives
\[
\boxed{
\begin{aligned}
W&=(2z+2\eta q)(2Cq+B(P))
       -2\eta z\{T'(P)-D(P)z/\eta\}\\
 &=4Czq+4\eta Cq^2+2B(P)z+2\eta B(P)q
       -2\eta zT'(P)+2D(P)z^2.
\end{aligned}}
\tag{12}
\]
No coefficient of F contributes to these two partials. It remains
present in the level relation and will be removed only when a
specific degree comparison forces its coefficient to vanish.

## 4. The constant-z endpoint r=3a is impossible

If r=3a, (7) gives z=z0 in L*, since z cannot vanish. Equation(6)
expresses q=-(z0^2+T(P))/(2eta*z0) in L[P], and hence x in L[P].
Whole generation gives O=L[P], so a=1 and r=3.

Recall zeta=theta+P^2+f'P from458. Since q differs from theta by
an affine polynomial in P, r=3 implies deg(zeta)=3. Now P is an
affine intrinsic parameter. The exact all-parameter return458(33)
and the equal-degree collision lemma
[459, Section3](principal-paraboloid-affine-sigma-arbitrary-first-potential-reduction-pass459-working.md)
exclude deg(x)=deg(zeta)=3 in that parameter.
This includes both distinct colliding points and the derivative-zero
boundary, as proved in459. No scalar extension is promoted to an
original coordinate. Therefore the remaining strict range is
\[
\frac32a<r<3a,\qquad m=3a-r>0.
\tag{13}
\]

## 5. Degrees above r=2a are impossible

Suppose 2a<r<3a. Compare the complete terms of(10), using m=3a-r:
\[
\begin{array}{c|c}
\text{term}&\text{degree when its coefficient is nonzero}\\ \hline
Cq^2&2r\\
B_2P^2q&2a+r\\
B_1Pq&a+r\\
B_0q&r\\
zT'&m+2a=5a-r\\
-D z^2/(2\eta)&a+2m=7a-2r\\
F_jP^j&ja.
\end{array}
\tag{14}
\]
The zT' and Pz^2 leading coefficients never vanish: t3 and eta
are nonzero. Within this open interval, successive uniquely highest
terms force, in order,
\[
C=0,\quad B_2=0,\quad F_4=0,\quad B_1=0,\quad F_3=0.
\tag{15}
\]
Indeed the first two degrees are 2r and 2a+r, both above4a in
the indicated order. Then4a exceeds a+r because r<3a. Next a+r
exceeds3a because r>2a. Finally3a exceeds r,5a-r and7a-2r.
These comparisons do not presume any of the listed coefficients
was initially nonzero.

After(15), zT' has degree5a-r, strictly greater than both 2a and
7a-2r. Its only possible competitor is B0*q. Therefore
\[
B_0\ne0,\qquad r=5a-r,\qquad r=5a/2.
\tag{16}
\]
Let P*,Q*,Z* be the nonzero leading coefficients of P,q,z. The top
level identity in(10) now says
\[
B_0Q_*+3t_3P_*^2Z_*=0.
\tag{17}
\]
In(12), the only degree-r terms are 2eta*B0*q and -2eta*z*T'.
Every other term has degree at most2a<r. Using(17), their sum has
leading coefficient
\[
2\eta B_0Q_*-6\eta t_3P_*^2Z_*
=-12\eta t_3P_*^2Z_*\ne0.
\tag{18}
\]
Thus W has degree r, not a-1, a contradiction. The entire interval
2a<r<3a is excluded.

## 6. Degrees below r=2a are impossible

Suppose 3a/2<r<2a. The uniquely highest term of(10) is initially
F4*P^4, so F4=0. For example 7a-2r<4a uses the strict lower
inequality r>3a/2. This is why the balanced boundary is not included.

### 6.1. The interval 3a/2<r<5a/3

The mandatory Pz^2 term has degree7a-2r. It exceeds2a+r,2r,
5a-r and3a throughout this interval. These bound every remaining
term of(10). Its nonzero leading coefficient -2eta*P*Z*^2 cannot
cancel, so the interval is impossible.

### 6.2. The boundary r=5a/3

Here only B2*P^2*q can balance the mandatory Pz^2 term, both of
degree11a/3. Thus B2 is nonzero and the top level gives
\[
B_2P_*^2Q_*=2\eta P_*Z_*^2.
\tag{19}
\]
The only terms of W of this degree are 2eta*B2*P^2*q and
2D*z^2. Their combined coefficient, using(19), is
\[
2\eta B_2P_*^2Q_*+8\eta^2P_*Z_*^2
=12\eta^2P_*Z_*^2\ne0.
\tag{20}
\]
All other terms have degree at most10a/3. This contradicts(11).

### 6.3. The interval 5a/3<r<2a

Now B2*P^2*q is uniquely highest unless B2=0, so this coefficient
vanishes. The mandatory Pz^2 term still has degree7a-2r, strictly
greater than5a-r, a+r, r and3a. Its only possible competitor is
Cq^2. Thus C is nonzero and
\[
2r=7a-2r,\qquad r=7a/4.
\tag{21}
\]
The level identity gives C*Q*^2=2eta*P*Z*^2. In(12) the only
degree-2r terms are 4eta*Cq^2 and 2D*z^2. Their combined leading
coefficient is
\[
4\eta C Q_*^2+8\eta^2P_*Z_*^2
=16\eta^2P_*Z_*^2\ne0.
\tag{22}
\]
For example zT' has smaller degree5a-r=13a/4, and zq has degree3a.
The required exact degree a-1 is again impossible.

This exhausts the open interval below2a. Together with Sections4--5,
the only strict alternative is r=2a, proving(1). The balanced
alternative r=3a/2 from460 is not used or excluded by this argument.

## 7. Verification and retained scope

Root read the complete held459 in3ac375 and460 in31cbbf+c40c8f,
and revalidated both hashes in1c1d4a before authoring. Their actual
inputs458/264/296 remain retained, as do the precise all-parameter
licenses of459. No recursive certification of every historical
recognition dependency is claimed.

Fresh unsaved89a0b8 independently reconstructed the entire strict
subtraction(8)--(10), with every lower polynomial coefficient free,
and the full formal minor(12). All residuals were zero. It also
reconstructed the three nonzero coefficients(18),(20),(22), including
the potentially competing r=5a/3 boundary. The written inequalities
and whole-ring endpoint argument, not finite numerical enumeration,
prove that the alternatives are exhaustive.

A separate saved-source audit and final held hash belong in the
ledger. Every degree comparison includes zero lower coefficients.
The level terms remain in T and F, and no evaluated polynomial
was inverted. This is an intrinsic degree restriction, not original
coordinate recovery, an actual realization, or cancellation.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited while composing this note.
No historical novelty, expert review, external contact or formal
certification is claimed.
