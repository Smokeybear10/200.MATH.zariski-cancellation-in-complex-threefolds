# The affine factor is necessarily selected in a reducible conic surface

Working result: in the actual genuine-conic alternative of302, the
surface factor that vanishes on the polynomial line is the affine
factor, not the quadratic factor. Moreover the coupling necessarily is
\[
m=k_s=d+\frac{c}{t-\tau},\qquad d,c,\tau\in\mathbb C,\quad c\ne0.
\tag{1}
\]
The reciprocal constraint follows already from the full surface
factorization, independently of which factor is selected. The fourth
potential then excludes selection of the quadratic factor.

This removes the selection restriction from the coefficient conclusion
of305. It is not recognition of the ambient kernel, a construction of
an actual example, or a claim that a coefficient-field operation is an
ambient coordinate change.

## 1. Actual entry and factor labels

Retain the complete actual nonzero-coupling chart of264, the two-gradient
minor-unit theorem of the fully read
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the genuine-conic reduction of the fully read
[302](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md).
Thus
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2),\quad a=EX\ne0,\quad
[L:\mathbb C(t,s)]<\infty,\\
O=L[v]=L[y,\sigma,\theta],\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{gathered}
\tag{2}
\]
The coefficient partials commute, hold v fixed, and have joint
constants exactly \(\mathbb C\). Formal partials in U,P,V hold every
coefficient fixed. In particular a coefficient derivative before
evaluation is not a moving-point derivative.

Write the two levels as \(H_0=H-h_0\), \(Q_0=Q-q_0\). In this
sector302 gives
\[
\begin{gathered}
H_0=U^2+A_1U+A_0=(U+A)(U+B),\qquad
A+B=A_1,\quad AB=A_0,\\
\deg A_1\le2,\quad\deg A_0\le3,\qquad
m_s=0,\quad p:=m_t\ne0,\\
O=L[\sigma],\quad\deg_v\sigma=1,\quad
\theta\in L[\sigma],\quad\deg_\sigma\theta=2.
\end{gathered}
\tag{3}
\]
Let G generate the full projected kernel in \(L[P,V]\). Its quadratic
top is a nonzero multiple of \(P^2\), and \(G_V\in L^*\).

Here and throughout this note, A denotes the quadratic factor
coefficient and B the affine one:
\[
\deg A=2,\qquad B=b_PP+b_VV+b_0.
\tag{4}
\]
These are degree labels, not selection labels. At least one factor is
affine because their product has degree at most three; exactly one is
quadratic because their sum has the nonzero quadratic part
\(-2pP^2/m\). Either selection is initially allowed.

Exactly one evaluated factor vanishes. The other evaluated factor is
a unit in \(O=L[v]\), since it divides every evaluated derivative of
H0 and that gradient ideal is a unit. Consequently the difference of
the two factors, minus a nonzero coefficient-field constant, is a
nonzero scalar multiple of G. This is the retained302 factor argument;
it does not assume either level is irreducible.

## 2. Rebuild the raw surface coefficients

Since \(m_s=0\), the literal formulas296 reduce to
\[
\begin{aligned}
F&=\frac{k_{tt}}2P^2+pPV+n_tP+n_sV,\\
D&=\frac{2P+k_t}{m},\qquad
\lambda=\frac{pP+n_s}{m},\\
A_1&=-\frac{2p}{m}P^2+pV+uP+w,\\
u&=k_{tt}-\frac{k_tp+2n_s}{m},\qquad
w=n_t-\frac{k_tn_s}{m},\\
A_0&=\frac{(pP+n_s)(\ell-F)}m
      +H_3(k)+H_2(n)-\ell_tP-\ell_sV-h_0.
\end{aligned}
\tag{5}
\]
The Taylor polynomials use factorial denominators. No lower coefficient
of n, ell, h0 or b0 has been set to zero.

Put \(q=m_{tt}\) and \(j=m_{ttt}\). The only cubic coefficients in
A0 are
\[
[P^3]A_0=\frac{k_{ttt}}6-\frac{pk_{tt}}{2m},\qquad
[P^2V]A_0=\frac q2-\frac{p^2}{m}.
\tag{6}
\]
Comparing these with the cubic part of \((A_1-B)B\) gives
\[
b_P=\frac{k_{tt}}4-\frac{mk_{ttt}}{12p},\qquad
b_V=\frac p2-\frac{mq}{4p},\qquad
a_V:=A_V=p-b_V=\frac p2+\frac{mq}{4p}.
\tag{7}
\]
The difference of the two V-slopes is
\[
a_V-b_V=\frac{mq}{2p}\ne0.
\tag{8}
\]
Indeed it is, up to a nonzero scalar and sign, the V-coefficient of G.
Thus \(q\ne0\). All subsequent divisions by m,p,q are therefore in
nonzero elements of L.

## 3. The lower factorization coefficients force the reciprocal equation

The raw V-squared and PV comparisons in \(AB=A_0\) are
\[
\frac{n_{ss}}2=a_Vb_V,\qquad
n_{ts}-\frac{2pn_s}{m}
   =ub_V+(a_V-b_V)b_P.
\tag{9}
\]
For clarity, \([V^2]A_0=n_{ss}/2\), while
\([PV]A_0=n_{ts}-2pn_s/m\). The two contributions to the latter
negative term both come from the literal product in (5).

Define
\[
f:=\frac{p^2}{2}-\frac{m^2q^2}{8p^2}.
\tag{10}
\]
The first equation of (9) is \(n_{ss}=f\).
All s-derivatives of m,p,q,j vanish. Commuting the coefficient
partials, without evaluating P or V, gives
\[
(b_P)_s=\frac q4-\frac{mj}{12p},\qquad
(a_V)_s=(b_V)_s=0,\qquad
u_s=q-\frac{p^2}{m}-\frac{2f}{m}.
\tag{11}
\]
The term \(-p^2/m\) here is essential: it is the s-derivative of
\(-k_tp/m\).

Differentiate the second equation of (9) in s and replace
\(n_{tss}\) by \(f_t\). Its entire residual is
\[
\begin{aligned}
0&=f_t-\frac{2a_Vf}{m}
       -b_V\left(q-\frac{p^2}{m}\right)
       -(a_V-b_V)\left(\frac q4-\frac{mj}{12p}\right)\\
 &=-\frac{5m^2q(2pj-3q^2)}{48p^3}.
\end{aligned}
\tag{12}
\]
The second equality is direct substitution of (7),(10), using
\(m_t=p,p_t=q,q_t=j\). Because \(m,p,q\ne0\), this proves
\[
2pj-3q^2=0.
\tag{13}
\]
This compatibility used both raw coefficients in (9). It did not use
the fourth potential, the identity of the selected factor, or a
rational-field ansatz.

To integrate exactly, put \(r=q/(2p)\ne0\). Equation (13) gives
\(r_t=r^2\), while \(r_s=0\). Thus
\(\tau=t+1/r\) is killed by both coefficient partials and belongs to
\(\mathbb C\). Set \(T=t-\tau\). Then \(r=-1/T\) and
\[
c_0=T^2p\in\mathbb C^*,\qquad
d=m+\frac{c_0}{T}\in\mathbb C.
\tag{14}
\]
Both assertions follow by differentiating in t and s. Taking
\(c=-c_0\) proves (1), within L itself. In particular no prior equality
\(L=\mathbb C(t,s)\) was used, and no denominator was inverted in
the ambient polynomial ring.

## 4. The quadratic-selected alternative has another necessary slope

Suppose for contradiction that the quadratic factor is selected:
\[
y=-A(\sigma,\theta),\qquad
(B-A)(\sigma,\theta)=\eta\in L^*.
\tag{15}
\]
Restrict the fourth level formally to this factor:
\(\widetilde Q(P,V)=Q_0(-A(P,V),P,V)\). It vanishes on the projected
curve, hence \(\widetilde Q=GT\) for a polynomial T. The evaluated
chain rule reads
\[
\widetilde Q_P^{\rm ev}=Q_P^{\rm ev}-A_P^{\rm ev}Q_U^{\rm ev},
\qquad
\widetilde Q_V^{\rm ev}=Q_V^{\rm ev}-a_VQ_U^{\rm ev}.
\tag{16}
\]
The first gradient is \(\eta(1,A_P^{\rm ev},a_V)\). Its two minors
involving U are eta times the quantities in (16); the third is their
O-linear combination. By296 these two quantities generate the unit
ideal of O. In particular \(\widetilde Q\) cannot be zero.

Since \(\widetilde Q=GT\), their evaluations are divisible by
\(T^{\rm ev}\), which must be in \(O^*=L^*\).
Using \(G_V\in L^*\) gives the specific unit
\[
\widetilde Q_V^{\rm ev}=G_VT^{\rm ev}\in L^*.
\tag{17}
\]
This argument does not replace the full projected ideal by an
arbitrarily chosen component or assume T is formally constant.

The exact corrected gradients296 are
\[
Q_U=(H_0)_P-D(H_0)_V+\lambda(H_0)_U,\qquad
Q_V=(H_0)_s.
\tag{18}
\]
Differentiate the full factorization first, then apply (15).
The result of (16),(18) is
\[
\widetilde Q_V^{\rm ev}
 =\eta\{A_s-a_V(A_P-Da_V+\lambda)\}^{\rm ev}.
\tag{19}
\]
The braces have total degree at most one in P,V and no V-term.
Indeed the quadratic coefficient of A is \(-2p/m\), whose
s-derivative is zero, and \((a_V)_s=0\).
Since sigma is an affine nonconstant parameter, (17) forces the
P-coefficient in braces to vanish.

Expanding from (5),(7), before using (9), that coefficient is
\[
C=\frac{p^2-2n_{ss}}m+2q+\frac{mj}{12p}
                      +\frac{mq^2}{8p^2}.
\tag{20}
\]
One can obtain it directly as
\(u_s-(b_P)_s+(3pa_V+2a_V^2)/m\).
After the V-squared equation \(n_{ss}=f\), it becomes
\[
0=C=\frac{2mpj+9mq^2+48p^2q}{24p^2}.
\tag{21}
\]
All constant terms, including \(b_{0,s}\), disappear from this
necessary coefficient identity; they were not specialized.

## 5. The two differential constraints are incompatible

Combine (13) with (21). Since q is nonzero, this gives
\[
0=\frac{q(mq+4p^2)}{2p^2},\qquad mq+4p^2=0.
\tag{22}
\]
Differentiating the latter exact field identity gives
\(mj+9pq=0\). But substitution of
\(q=-4p^2/m\) and \(j=3q^2/(2p)\) gives instead
\[
mj+9pq=-\frac{12p^3}{m}\ne0.
\tag{23}
\]
This contradiction excludes (15). Thus the selected factor is the
affine B, and the other factor is quadratic.

## 6. Precise strengthened frontier

In the genuine-conic alternative of the actual reducible surface,
\[
\boxed{
y=-B(\sigma,\theta),\quad \deg B\le1,\quad
m=d+\frac{c}{t-\tau},\quad
d,c,\tau\in\mathbb C,\ c\ne0.
}
\tag{24}
\]
The degree conclusions of302 remain
\(\deg_v\sigma=1,\deg_v\theta=2,\deg_vy\le2\).
The affine-selected reciprocal lemma305 is therefore now applicable
without an additional selection choice, while (12) supplies an
independent lower-factorization route to its differential equation.

The projected-line cases and the irreducible-surface sector are not
addressed. No coordinate recognition, realization, arbitrary
cancellation result, or coefficient regularity in the original ring
is inferred. In particular the reciprocal expression is a coefficient
identity, not an authorized actual change of variables.

The held302 and305 sources were read completely before this note was
saved;296 is the fully read retained fourth-potential input. Fresh
unsaved symbolic reconstruction started from the literal A0,A1 with
arbitrary n,ell and affine-factor intercept b0. It verified both raw
cubic coefficients, V-squared and PV coefficients, the differentiated
compatibility, and the entire degree bound and P-coefficient in (19).
An independent Root calculation obtained the same two residuals.
These are exact algebra controls, not universal theorem verification.
No saved checker was executed, imported, compiled or rerun, and no
retained source, index or packet was changed.
