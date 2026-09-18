# Scalar rigidity of the remaining reciprocal conic factor unit

Working result: in the full actual genuine-conic sector of315, the
nonvanishing evaluated surface factor is independent of the coefficient
parameter s. More precisely,
\[
\eta,\mathcal C\in\mathcal F^*,\qquad
L=\mathcal F(s),\qquad
\left(\frac{\eta}{m}\right)_t\ne0 .
\tag{1}
\]
Here \(\mathcal F=\ker_L\partial_s\) is the exact finite extension of
\(\mathbb C(t)\) from315. The nonzero coefficient \(\mathcal C\) is
defined below from the restricted fourth gradient.

The proof reconstructs the constant scalar Jacobian after the legitimate
coefficient-field change from v to the affine parameter sigma. It does
not turn sigma, s, eta or a coefficient of \(\mathcal F\) into an
original polynomial coordinate.

## 1. Full actual inputs and parameter conventions

Retain the complete actual hypotheses of
[315](principal-paraboloid-conic-polynomial-coefficient-return-pass315-working.md),
together with its direct inputs306 and296. In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad a=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
[L:\mathbb C(t,s)]<\infty,\quad
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(\sigma),\quad
L[v]=L[\sigma],\quad\deg_v\sigma=1 .
\end{gathered}
\tag{2}
\]
The coefficient partials commute, have joint constants \(\mathbb C\),
and extend uniquely to L. Their common use below on elements of L is
unaffected by replacing v with sigma. Derivatives of the polynomial
intercepts after that replacement, however, hold sigma fixed.

Let \(H_0=H-h_0\). The affine factor is selected:
\[
\begin{gathered}
H_0=(U+A(P,V))(U+B(P,V)),\qquad
B=b_PP+b_VV+b_0,\quad \deg A=2,\\
y=-B(\sigma,\theta),\qquad
\Psi=A-B,\qquad \Psi(\sigma,\theta)=\eta\in L^* .
\end{gathered}
\tag{3}
\]
Formal variables U,P,V are always independent of all coefficients.
A formal coefficient derivative is taken before substitution.

Use the coupling and coefficients already proved in315:
\[
\begin{gathered}
m=k_s=d+\frac{c}{t-\tau},\quad c,d,\tau\in\mathbb C,\quad c\ne0,\qquad
p=m_t\ne0,\quad q=m_{tt}\ne0,\\
k=ms+f,\quad f\in\mathcal F,\quad
n\in\mathcal F[s]_{\le2},\quad
\ell\in\mathcal F[s]_{\le3},\\
b_P=\frac{k_{tt}}4-\frac{m k_{ttt}}{12p}
 \in\mathcal F[s]_{\le1},\qquad
b_V=\frac p2-\frac{mq}{4p}\in\mathcal F,\\
\delta=p-2b_V=\frac{mq}{2p}\in\mathcal F^*,\\
\mu=k_{tt}-\frac{k_t p+2n_s}{m},\qquad
\nu=n_t-\frac{k_tn_s}{m},\\
b_0=\frac{m}{2p}\left((\mu-b_P)b_P-\frac{n_{tt}}2+
                \frac{p n_t+n_s k_{tt}/2}{m}\right)
       \in\mathcal F[s]_{\le2}.
\end{gathered}
\tag{4}
\]
The field \(\mathcal F\) is finite over \(\mathbb C(t)\), and its
t-constant field is \(\mathbb C\). No rationality of \(\mathcal F\)
is assumed.

It is convenient to abbreviate
\[
\alpha=\frac{2p}{m},\qquad
\beta=2b_P-\mu,\qquad
\chi=2b_0-\nu,\qquad
\Psi=\delta V-\alpha P^2-\beta P-\chi .
\tag{5}
\]
These alpha and beta are not the original speed a or the affine
parameter speed \(\sigma_v\). Evaluation solves the conic exactly:
\[
\theta=\frac{\eta+\alpha P^2+\beta P+\chi}{\delta},
\qquad P=\sigma .
\tag{6}
\]

## 2. Lower coefficients and restricted fourth gradients

The constant formal coefficient in \(H_0=(A_1-B)B+UA_1+U^2\)
gives an additional polynomial coefficient bound:
\[
h_0=\frac{n_s\ell}{m}-b_0(\nu-b_0)
       \in\mathcal F[s]_{\le4}.
\tag{7}
\]
Indeed the constant formal coefficient in the literal surface296 is
\(n_s\ell/m-h_0\), while that of its product is
\((\nu-b_0)b_0\). Thus the normalized fourth potential296 has
coefficients in \(\mathcal F[s]\). This observation retains the level
derivatives in that potential.

Define, before evaluation,
\[
\begin{gathered}
F=\frac{k_{tt}}2P^2+pPV+n_tP+n_sV,\qquad
\gamma=2P+k_t,\quad D=\gamma/m,\quad
\lambda=(pP+n_s)/m,\\
\mathscr B=-2B+F_P
  =\delta V+(k_{tt}-2b_P)P+n_t-2b_0,\\
\mathcal C=B_s-b_V(b_P-D b_V+\lambda),\\
\mathcal T=B_t-\frac{b_V}{m}\mathscr B-b_P^2+b_Pb_VD .
\end{gathered}
\tag{8}
\]
The symbol F in this display is the polynomial potential, not the field
\(\mathcal F\). Derivatives of B in (8) fix P,V.

Let \(\widetilde Q(P,V)=Q(-B(P,V),P,V)\), where Q is the normalized
fourth potential296. Its corrected gradient identities are
\[
Q_U=(H_0)_P-D(H_0)_V+\lambda(H_0)_U,\quad
Q_P=(H_0)_t-\frac{2U+F_P}{m}(H_0)_V+\lambda(H_0)_P,\quad
Q_V=(H_0)_s .
\]
Restricting the full factorization to \(U=-B\) therefore gives
\[
\widetilde Q_P=\Psi\mathcal T,\qquad
\widetilde Q_V=\Psi\mathcal C .
\tag{9}
\]
For example, the chain rule for the second expression subtracts
\(b_VQ_U\). No derivative of eta is present in (9).

The reciprocal coupling gives the exact identities
\[
(b_P)_s=(b_V)_t=\frac{b_V\delta}{m},\qquad
(b_V)_s=0 .
\tag{10}
\]
Consequently
\(\mathcal C_P=\mathcal C_V=\mathcal T_V=0\), and
\(\mathcal C\in\mathcal F[s]_{\le1}\).
Equality of the two formal mixed derivatives in (9) now proves
\[
\delta\mathcal T=\mathcal C\Psi_P .
\tag{11}
\]
In particular \(\mathcal C\ne0\). Otherwise both restricted gradients
would be zero, and all evaluated minors of the surface and fourth
gradients would vanish, contrary to296. Since \(\eta,\delta\ne0\),
the evaluated restricted V-gradient is the nonzero unit
\(\eta\mathcal C\in L^*\).

Equations (9),(11) also integrate formally, without a new coefficient
field integration:
\[
\widetilde Q=\frac{\mathcal C}{2\delta}\Psi^2+K_0,\qquad
K_0\in\mathcal F[s],\qquad
q_0=\frac{\mathcal C}{2\delta}\eta^2+K_0 .
\tag{12}
\]
First integrate in V; (11) then makes the remaining P-derivative zero.

## 3. Exact differential rows and scalar orientation

Replace v by \(P=\sigma\) only within the generic coefficient chart.
Since \(\sigma_v\in L^*\), the triangular parameter-change Jacobian
gives
\[
\mathcal J:=\det\frac{\partial(y,z,w)}{\partial(t,s,P)}
       =-\frac{a^4}{\sigma_v}\in L^* .
\tag{13}
\]
In (13), t,s derivatives of the intercepts hold P fixed. In particular
theta is differentiated from (6), including all its coefficient
derivatives.

At \(X=0\), introduce the two one-forms
\[
\mathscr M=dz-2t\,dy
     =\gamma\,dP+m\,d\theta+\mathscr B\,dt+(pP+n_s)\,ds,
\qquad
\mathscr A=dP+b_Pdt+b_Vds .
\tag{14}
\]
The literal first and second potentials315 give the exact contact row
\[
m\,dw+\gamma\,dy+\lambda\mathscr M=-\eta\mathscr A .
\tag{15}
\]
One way to check its signs is to use296's
\(H_U=2y+F_P-\gamma\lambda\),
\(H_P=-m g_t-\lambda(2y+F_P)\),
\(H_V=-m g_s-m\lambda^2\).
On the selected factor these are respectively
\(\eta,\eta b_P,\eta b_V\).

Differentiating \(y=-B\) and using (8) yields another exact row:
\[
dy+\frac{b_V}{m}\mathscr M+(b_P-b_VD)\mathscr A
       =-\mathcal T\,dt-\mathcal C\,ds .
\tag{16}
\]
All covectors in (14)--(16) use the basis \(dt,ds,dP\).
Write their middle row as
\[
\begin{gathered}
g_1=\frac{\Psi_P}{\delta}
       =-\frac{2\alpha P+\beta}{\delta},\\
M_P=\gamma-mg_1,\qquad
M_t=\frac{m\eta_t}{\delta}+\mathscr B-\frac{m\Psi_t}{\delta},\qquad
M_s=\frac{m\eta_s}{\delta}+pP+n_s-\frac{m\Psi_s}{\delta}.
\end{gathered}
\tag{17}
\]
Here the formal \(\Psi_t,\Psi_s\) are evaluated using (6) only after
differentiation. In particular their V terms are not omitted.

Wedging (15),(16) in the stated order, and then using (11), gives
\[
\begin{aligned}
\mathcal J
 &=-\frac{\eta}{m}
    \{\mathcal C(M_t-b_PM_P)-\mathcal T(M_s-b_VM_P)\}\\
 &=-\frac{\eta\mathcal C}{m}\,
       \Pi(P),\\
\Pi(P)&=M_t-g_1M_s+(b_Vg_1-b_P)M_P .
\end{aligned}
\tag{18}
\]
This establishes the scalar orientation directly from the literal
intercept map.

## 4. The full coefficient cancellation

For reproducibility, the exact coefficient ledger needed to expand
(18) is recorded here. It comes from (4), the raw PV and P-squared
surface coefficients306/315, and the P and constant coefficients of
(11):
\[
\begin{aligned}
b_V&=(p-\delta)/2,&
m_{tt}&=2p\delta/m,&
\delta_t&=\delta(p+\delta)/m,\\
n_{ss}&=(p^2-\delta^2)/2,&
n_{ts}&=2pn_s/m+\mu b_V+\delta b_P,\\
k_{ttt}&=3pk_{tt}/m-12pb_P/m,\\
(b_P)_t&=b_Vk_{tt}/m-4b_Pb_V/m
                         -2\alpha\mathcal C/\delta,\\
(b_0)_s&=\mathcal C+b_Vb_P-b_V^2k_t/m+b_Vn_s/m,\\
(b_0)_t&=b_V(n_t-2b_0)/m+b_P^2-b_Pb_Vk_t/m
                         -\beta\mathcal C/\delta,\\
n_{tt}&=2(\mu-b_P)b_P-4pb_0/m+2pn_t/m+n_sk_{tt}/m .
\end{aligned}
\tag{19}
\]
For instance (11)'s P coefficient is
\((b_P)_t-b_Vk_{tt}/m+4b_Pb_V/m
 =-2\alpha\mathcal C/\delta\).
Its constant coefficient is the stated formula for \((b_0)_t\).
Thus no lower potential coefficient has been suppressed in (19).

The polynomial \(\Pi(P)\) has degree at most two. Expansion of
(17),(18), followed by (19) and the derivatives of (5), gives
\[
[P^2]\Pi=0,\qquad
[P]\Pi=\frac{4p\eta_s}{\delta^2},\qquad
[1]\Pi=\frac{m\eta_t-p\eta}{\delta}
                   +\frac{\beta m\eta_s}{\delta^2}.
\tag{20}
\]
To make the consequential cancellation explicit, before these
substitutions the numerator of \([P]\Pi\), with denominator
\(\delta^2\), is
\[
\begin{aligned}
&-4\alpha\beta b_Vm-2\alpha b_P\delta m
 -2\alpha b_V\delta k_t
 +2\alpha\chi_s m+2\alpha\delta n_s+2\alpha m\eta_s\\
&+\beta\beta_s m-2\beta b_V\delta+\beta\delta^2
 +\beta\delta p-\beta\delta_t m-4b_P\delta^2
 +\beta_t\delta m+\delta^2 k_{tt}.
\end{aligned}
\tag{21}
\]
Use
\(\beta_s=2(b_P)_s-\mu_s\),
\(\beta_t=2(b_P)_t-\mu_t\),
\(\chi_s=2(b_0)_s-\nu_s\), with the definitions of mu,nu in (4).
Every term of (21) except \(2\alpha m\eta_s=4p\eta_s\)
then cancels by (19). The constant coefficient similarly uses
\(\chi_t=2(b_0)_t-\nu_t\) and the last equation of (19).
This proves (20) by polynomial coefficient comparison; it does not
assume a rational ansatz for eta.

Since \(\mathcal J\) is independent of P, and
\(p,\eta,\mathcal C,m,\delta\) are nonzero, (18),(20) force
\[
\eta_s=0,\qquad \eta\in\mathcal F^* .
\tag{22}
\]
The remaining scalar is exactly
\[
\boxed{\displaystyle
\mathcal J=
 -\frac{\eta\mathcal C}{m\delta}(m\eta_t-p\eta)
 =-\frac{\eta\mathcal C m}{\delta}
               \left(\frac{\eta}{m}\right)_t .}
\tag{23}
\]
It is nonzero by (13), so the derivative asserted in (1) is nonzero.

## 5. The restricted coefficient is also an exact t-field element

Although \(\mathcal C\in\mathcal F[s]_{\le1}\) sufficed in the scalar
argument, its possible linear term vanishes. Put \(T=t-\tau\);
this is merely a coefficient notation, not an ambient reframe.
The reciprocal formulas give
\[
b_V=\frac d{2T},\quad
\delta=-\frac{c+dT}{T^2},\quad
(b_P)_s=-\frac d{2T^2},\quad
n_{ss}=-\frac{d(2c+dT)}{2T^3}.
\]
Substitution of these leading s-coefficients in the full b0 formula
(4) gives
\[
b_0=-\frac{d^2}{4T^3}s^2+u_1s+u_0,\qquad u_0,u_1\in\mathcal F,
\qquad
(b_0)_{ss}=-\frac{d^2}{2T^3}
                =\frac{2b_V^2\delta}{m}.
\tag{24}
\]
Lower coefficients of k and n cannot affect this s-squared coefficient.

From (8),(10), and \(n_{ss}=(p^2-\delta^2)/2\),
\[
\mathcal C_s=(b_0)_{ss}-\frac{2b_V^2\delta}{m}=0 .
\tag{25}
\]
Thus \(\mathcal C\in\mathcal F^*\), including when \(d=0\).
Equation (23) consequently puts the full calibrated scalar
\(\mathcal J\) itself in \(\mathcal F^*\).

## 6. Exact field consequence and remaining ring boundary

The strong return315 was \(L=\mathcal F(s,\eta)\).
Combining it with (22) proves \(L=\mathcal F(s)\) inside the original
fraction field, without assuming that \(\mathcal F=\mathbb C(t)\).
The original polynomial expansions315 now give the sharper inclusion
\[
\mathcal F[X,Y,Z,W]\subseteq\mathcal F[X,s,\sigma],\qquad
\operatorname{Frac}\mathcal B=\mathcal F(X,s,\sigma).
\tag{26}
\]
The right side of the inclusion is a polynomial ring over the field
\(\mathcal F\): X,s,sigma are algebraically independent over it by
the exact field return and the global slice. Equation (26) does not
assert equality of these rings, normality of the left side, or an
actual coordinate among s,sigma or eta.

This note proves scalar rigidity, rationality of the remaining
s-extension over the exact curve field, polynomial coefficient entry
into the displayed larger ring, and the nonzero derivative in (1).
It does not prove recognition of this sector or an unrestricted
cancellation statement.

The complete315 and296 sources were read afresh before writing;
306's full relevant coefficient derivation was also reread.
Fresh unsaved symbolic coefficient calculations checked (20),(24),
retaining the mixed and lower jets in (19). The covector argument,
exact-field reasoning and actual calibration are written above,
not certified by finite samples. No saved checker was executed,
imported, compiled or rerun. No previous proof, index or packet
was edited, and no novelty or external expert certification is claimed.
