# Correction to301: a scalar exclusion of the constant-first branch

This note replaces Section3 of
[301](principal-paraboloid-affine-second-potential-reduction-pass301-working.md).
The original source is preserved unchanged as an audit record. Its
equation(10) incorrectly states that the actual auxiliary derivation
fixes Y, so its relative-UFD argument does not prove the constant-first
exclusion. The direct scalar argument below supplies that exclusion
under the same actual hypotheses, without any auxiliary fixed-ring
assertion.

The correction restores the uses of301's conclusion(12) in its later
sections. It does not enlarge301's recognition claim beyond
\(k=s,n=0,\ell_s\ne0,\ell_{ss}=0\). The genuinely quartic sector
\(\ell_{ss}\ne0\) remains open subject to301's degree-pair restrictions.

## 1. Exact flaw and scope of the replacement

Retain the actual globally sliced chart264 and the exact hypotheses
of301(1)--(3). In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
[L:\mathbb C(t,s)]<\infty,\qquad K=L(v),\qquad Nv=1,\\
K=\mathbb C(y,z,w),\qquad L[y,z,w]=L[v],\qquad
J(X)=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The selected N and all these identities come from the literal actual
partial in264, not an arbitrarily chosen coefficient derivation.
Assume \(k=s,n=0,\ell_s\ne0\), and temporarily suppose \(y\in L\).
Write \(a_1=\ell_t,b_0=\ell_s\). The third potential gives
\(\theta=(y^2-a_1\sigma-h)/b_0\), with \(h\in L\).
It follows that
\[
L[v]=L[y,\sigma]=L[\sigma],\qquad N\sigma\in L^*.
\tag{2}
\]

For \(\mathcal P=a_0N-(NX)E\) and \(\tau=a_0N\sigma\),
the correct literal rows are
\[
\begin{aligned}
\mathcal PX&=0,&\mathcal PY&=\tau X,\\
\mathcal PZ&=\tau(2\sigma-a_1/b_0+2tX),&
\mathcal PW&=\tau(-2y-(a_1/b_0)X).
\end{aligned}
\tag{3}
\]
The nonzero Y-row follows immediately by applying the derivation,
which fixes X, to \(Y=y+\sigma X+tX^2\). Therefore neither
\(\mathcal P\) nor its nonzero primitive division fixes
\(\mathbb C[X,Y]\). The claimed application of the two-variable
relative-UFD lemma over that ring in301 Section3 is invalid.
We withdraw that whole fixed-ring argument, rather than retaining
it after changing only one displayed row.

## 2. Exact coefficient change and the scalar

Use the coefficient parameter \(r=\ell\) and write
\[
s=H(t,r),\qquad H_r=1/\ell_s\ne0,\qquad
\mathcal L=H_rh,
\qquad c=y\in L.
\tag{4}
\]
The field L is finite over \(\mathbb C(t,r)\). The extended
coefficient partials \(\partial_t,\partial_r\) commute on L;
all partials in the rest of this note refer to these new parameters.
No equality \(L=\mathbb C(t,r)\) is asserted or needed.

Put \(P=\sigma\). By(2), P is affine in the original v and
\(P_v\in L^*\). The literal intercepts are
\[
z=P^2+H_tP+H_rc^2+2tc-\mathcal L,\qquad
w=r-2cP.
\tag{5}
\]
The scalar is still nonzero after this moving-parameter change:
\[
J_P:=\det\frac{\partial(c,z,w)}{\partial(t,r,P)}
       =-\frac{a_0^4H_r}{P_v}\in L^*.
\tag{6}
\]
Indeed the coordinate-change determinant from \((t,r,P)\) to
\((t,s,v)\) is \(H_r/P_v\). The possible t,r dependence of P
does not add terms to this determinant. Equation(6) is the X=0
coefficient of the full actual calibration in(1), and is independent
of the formal variable P.

The corrected fourth potential in301(8), obtained from296, is
\[
Q(U,P)=\frac{H_{rr}}2U^4+H_{tr}U^2P+\frac{H_{tt}}2P^2
       +2UP+H_tU-\mathcal L_rU^2-\mathcal L_tP,
\qquad Q(c,P)=q_0\in L.
\tag{7}
\]
Comparison in the polynomial ring \(L[P]\) gives
\[
\boxed{H_{tt}=0,\qquad
\mathcal L_t=H_{tr}c^2+2c.}
\tag{8}
\]
For this branch, only evaluation of the fourth potential is used.
Neither the plane cofactor-unit theorem nor a classification of
plane curves is needed.

Directly expanding the literal determinant in(5), before imposing
either equality in(8), gives the exact identity
\[
\begin{aligned}
J_P={}&-c_t\{2(1+cH_{tr})P+H_t
                  +2c(H_{rr}c^2-\mathcal L_r)\}\\
&+2c c_r\{H_{tt}P+H_{tr}c^2+2c-\mathcal L_t\}.
\end{aligned}
\tag{9}
\]
For example, the expansion along the c-row is
\(J_P=2c(c_rz_t-c_tz_r)-c_t(2P+H_t)\), which yields(9)
after inserting the two coefficient derivatives of z. Thus all
moving-coefficient terms are retained in the displayed residual.

## 3. Contradiction and restored conditional conclusions

After(8), equation(9) reduces to
\[
J_P=-c_t\{2(1+cH_{tr})P+H_t
                  +2c(H_{rr}c^2-\mathcal L_r)\}.
\tag{10}
\]
Since(6) is nonzero, \(c_t\ne0\). Since it is independent of P,
the P-coefficient in(10) gives
\[
cH_{tr}=-1.
\tag{11}
\]
In particular \(H_{tr}\ne0\). Differentiate(11) in t. The
commutation of exact coefficient partials and \(H_{tt}=0\) give
\(H_{ttr}=0\), hence
\(c_tH_{tr}=0\), a contradiction. Therefore
\[
\boxed{y\notin L.}
\tag{12}
\]

This is exactly the conclusion formerly claimed in301(12), now
proved from the actual scalar and the corrected fourth potential.
Sections1--2 and4--6 of the held301 source do not use the false
fixed-ring assertion except through that conclusion. Replacing
its Section3 by this proof therefore restores its scoped endpoint:
\[
k=s,\quad n=0,\quad\ell_s\ne0,\quad\ell_{ss}=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]},
\tag{13}
\]
subject to the explicit actual degree-lowering maps and the retained
working recognition input257 used in301 Section5. The remaining
\(\ell_{ss}\ne0\) degree pairs remain only the necessary list
\((1,2),(1,4),(2,4)\), not a recognition or existence claim.

The original source hash is
`f706d6b9c270b0640a971dc442f93bafe2ecabcbd499ad7048adc363405a83fe`.
Its complete hostile peer read identified the nonzero Y-row before
promotion. Fresh unsaved symbolic calculation rebuilt(9) with
arbitrary H, \(\mathcal L\), c and verified both coefficients
in(8). That finite check supplements the displayed determinant
proof; it is not a certificate for the exact-field or actual-frame
assumptions. No saved checker was executed, imported or compiled,
and the original301 source was not edited.
