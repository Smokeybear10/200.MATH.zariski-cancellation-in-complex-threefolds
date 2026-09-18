# A constant conic leader is excluded by the actual two-quasi frame

Working exclusion: under the FULL actual principal-chart hypotheses,
the nonlinear conic sector with
\[
m=k_s\notin\mathbb C,\quad m_s=m_{tt}=0,\quad
\deg_v\sigma=1,\quad \theta=a\sigma^2+b\sigma+c,
\quad a(1+ma)\ne0
\]
cannot have \(a_t=0\).

The proof uses the complete necessary reduction496, both alternatives
of the field two-quasi theorem, and the remaining full scalar.
The generic invariant is used only to derive coefficient identities.
It is not promoted to a coordinate over C[X]. The final contradiction
occurs in a genuinely actual complex-X fiber. The moving-a and
delta-zero branches are not covered.

## 1. Actual input and the constant-a consequence of496

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine potentials and unit minors of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
the parity result327, and the completely read
[494](principal-paraboloid-unit-tangent-multiplier-pass494-working.md)
and
[496](principal-paraboloid-affine-coupling-conic-moving-frame-pass496-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad O=L[v]=L[y,z_0,w_{\rm int}]
=L[y,\sigma,\theta],\\
\mathcal K=\operatorname{Frac}A=L(v)=\mathbb C(y,z_0,w_{\rm int}).
\end{gathered}
\tag{1}
\]
Both returns, the literal selected partial and the original slice
remain required. The coefficient partials commute, with joint
constants C. No unit assumption on a0 in A is added.

Use the intrinsic affine parameter
\[
P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\qquad
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\tag{2}
\]
The exact field \(F_0=\ker_L\partial_s\) is finite over C(t),
and its t-derivative constants are C. This does not identify it
with C(t), or L with \(F_0(s)\).

Write the necessary identities496 as
\[
\begin{gathered}
m=pt+d,\quad p\in\mathbb C^*,\ d\in\mathbb C,
\quad k=ms+f,\quad f\in F_0,\\
\theta=aP^2+bP+c,\qquad
y=-p\theta/2+\lambda P+r,\qquad a_s=0,\\
n=p^2s^2/4+(pf'/2-h)s+n_0,\qquad h,n_0\in F_0,\\
A_c=(ph-mh')/(2p),\quad B_c=-f''/4+mf'''/(12p),\\
\lambda=A_ca+B_c,\quad f''''=6ah'',\\
r=A_cb+(-paA_c/2+pB_c/2+h'/2)s+r_0,
\qquad r_0\in F_0.
\end{gathered}
\tag{3}
\]
Primes here are the original exact t derivative on F0.
Suppose \(a_t=0\). Then \(a\in\mathbb C^*\).
The full multiplier494 and the complete moving-frame coefficient496
give
\[
b_s-pa\ne0,\qquad h''=0,\qquad f''''=0.
\tag{4}
\]
In particular h is complex affine in t and f is complex cubic in t.
This follows by successive subtraction and the exact constant field,
not by assuming rationality. The proof below does not use the
separate fifth-root result493.

## 2. Actual normalization to k=ts and constant h

All maps in this section are members or compositions of the actual
filtered maps in the fully read
[426](general-coupling-normalization-obstruction-pass426-working.md).
Their coefficients are complex. We describe the maps sequentially,
and only then rename the normalized parameters.

First put \(\tau=d/p\) and use
\[
X_1=X,\quad Y_1=Y+\tau X^2,\quad
Z_1=Z+2\tau Y+\tau^2X^2,\quad W_1=pW.
\tag{5}
\]
Then \(t_1=t+\tau\), \(s_1=ps\), and
\(k_1=t_1s_1+F(t_1)\), with F a complex polynomial of degree at
most three. The inverse recovers X, then Y, then Z, and W by
division only by p. Its new coupling derivative is \(m_1=t_1\).
The conic coefficient becomes \(a_1=pa\), still complex nonzero,
and \(1+m_1a_1=1+ma\).

Write \(F(t_1)=c_3t_1^3+c_2t_1^2+c_1t_1+c_0\), allowing all
four constants to vanish. Use
\[
X_2=X_1,\quad Y_2=Y_1,\quad Z_2=Z_1-c_0X_1,
\quad W_2=W_1+c_3Z_1+c_2Y_1+c_1X_1^2.
\tag{6}
\]
Its inverse first recovers \(Z_1=Z_2+c_0X_2\), then W1.
The transported parameters satisfy
\[
t_2=t_1,\quad s_2=s_1+c_3t_1^2+c_2t_1+c_1,
\qquad k_2=t_2s_2.
\tag{7}
\]
The quadratic intrinsic theta coefficient is unchanged by (6).
Reapply the necessary identities496 in this actual frame. They give
\(n=s^2/4-h(t)s+n_0(t)\), with \(h=h_1t+H\) complex affine.

Finally, in this intermediate frame, put \(x=h_1/2\) and take
\[
X_*=X+x,\quad Y_*=Y,\quad Z_*=Z,\quad W_*=W+2xY.
\tag{8}
\]
The inverse subtracts x from X* and \(2xY_*\) from W*.
The parameter transport is \(t_*=t\), \(s_*=s+2xt\),
\(k_*=ts_*\). For a direct check of the first potential, the
pullback before substituting \(s=s_*-2xt\) is
\[
n_*=n+3xst+3x^2t^2.
\tag{9}
\]
Thus its s*-linear coefficient is \(-h+2xt=-H\).
The conic coefficient a remains complex nonzero.

The complete inverses and the filtered leading maps preserve the
ENTIRE initial kernel. The exact E-profile remains (1,2,2,2).
The literal selected-partial transport is426(15); any W-partial
contribution has shift at most three, so the selected N remains the
stated nonzero scalar multiple. The actual localized quotient proves
both returns, as in426(17)--(18), and426(19) preserves the calibrated
scalar with the appropriate nonzero factors. The original global
slice is not replaced by X/a0. These are actual ambient maps, unlike
the later changes of coefficient or intrinsic parameters.

Drop stars and rename the lower coefficient functions. The normalized
necessary data are now
\[
\begin{gathered}
m=t,\quad k=ts,\quad a,H\in\mathbb C,\quad a\ne0,
\quad\delta=1+at\ne0,\quad \lambda=aH/2,\\
n=s^2/4-Hs+n_0,\quad n_0\in F_0,\\
z=b-as,\quad z_s\ne0,\qquad
r=\lambda s/2+Hz/2+R,\quad R\in F_0.
\end{gathered}
\tag{10}
\]
The z in this note is the transverse coefficient, not the original
Z intercept. No root of a coefficient polynomial in X was removed.

## 3. The actual two-quasi frame and its complete constant row

Use the ACTUAL polynomial coordinate frame
\[
U=Z,\qquad V=-2Y-aZ,\qquad T=W+2XY.
\tag{11}
\]
Its inverse is \(Z=U\), \(Y=-(V+aU)/2\),
\(W=T+X(V+aU)\), with X unchanged. Hence
\(\mathcal B=\mathbb C[X,U,V,T]\).
This auxiliary frame need not retain the old E-profile: T contains XY.

Set \(C_X=X+\lambda\). The complete indicated rows from496 are
\[
\begin{aligned}
U&=P^2+uP+U_0,&u&=s+2tC_X,\\
V&=v_1P+V_0,&v_1&=z-2\delta C_X,\\
T&=w_1P+T_0,&w_1&=2XC_X-K,\\
K&=(2R+n_0')/t\in\mathbb C,&
T_0&=F/t+2rX+sX^2+2tX^3,\\
F&=\ell+Hc-sr.&
\end{aligned}
\tag{12}
\]
Here \(w_1\in\mathbb C[X]\) is the constant-frame conclusion496.
Since its leading coefficient is 2, it is never the zero polynomial.
Its finite complex roots are retained. The term \(2tX^3\) in T0
is essential and remains in all subsequent equations.
Neither F nor c nor z is assumed rational or polynomial in s.

Extend the original N to \(A[u_{\rm glob}]\) by
\(Nu_{\rm glob}=0\), and use the actual derivation
\[
\Delta=a_0N-(NX)E.
\tag{13}
\]
As proved directly in496, it preserves the polynomial ring, fixes X,
is locally nilpotent and kills L. On the injective overring L[X,P],
it is \(g_0\partial_P|_X\), with \(g_0=a_0\rho\in L^*\).
Consequently
\[
\Delta V=g_0v_1,\quad \Delta T=g_0w_1,\quad
\Delta^2V=\Delta^2T=0,\quad
\Delta^2U=2g_0^2\ne0,\quad\Delta^3U=0.
\tag{14}
\]

## 4. Both published field-theorem alternatives

Localize the ACTUAL polynomial ring at C[X] minus zero:
\(\mathcal R=k_X[U,V,T]=k_X^{[3]}\), where \(k_X=\mathbb C(X)\).
Take a gcd g of the three coefficients of Delta in this UFD.
It divides \(\Delta g\). If \(\Delta g\ne0\), additivity of
Delta-degree in a product contradicts
\(\deg_\Delta(\Delta g)=\deg_\Delta g-1\).
Thus \(\Delta g=0\), and \(D_0=\Delta/g\) is an irreducible
nonzero LND, with the same kernel and velocity ratios. Its iterates
are \(D_0^j=\Delta^j/g^j\), so (14) is retained.

The primary
[Dasgupta--Gupta, Theorem4.1](https://arxiv.org/html/1701.03635v1)
gives two alternatives for these actual field coordinates. Either
a nonzero kX-linear form in V,T is invariant, or there is an
invariant coordinate I with \(\mathcal R=k_X[I,V,T]\) and
\(D_0V,D_0T\in k_X[I]\). The theorem requires characteristic zero
and irreducibility, both arranged above. Its second alternative
does not assert descent of I to a coordinate over C[X].

The first alternative is impossible. Indeed
\[
\frac{\Delta V}{\Delta T}=\frac{v_1}{w_1}\notin k_X,
\tag{15}
\]
because \((v_1)_s=z_s\ne0\), while w1 is nonzero and has zero
s derivative. Also \(\Delta T\ne0\), so an invariant linear form
with zero V coefficient cannot avoid this contradiction.

In the second alternative, the automorphism retaining V,T has the
form \(I=A(X)U+\mathcal F(V,T)\), with \(A\in k_X^*\) and
\(\mathcal F\in k_X[V,T]\). This follows by comparing the U-degrees
of the map and its polynomial inverse over kX[V,T].
Write \(D_0V=f(I)\), \(D_0T=g_1(I)\). Here g1 is nonzero and
\(f/g_1\) is nonconstant by (15), so it is transcendental over kX.
The equation \(D_0^3U=0\) gives
\[
f^3\mathcal F_{VVV}+3f^2g_1\mathcal F_{VVT}
 +3fg_1^2\mathcal F_{VTT}+g_1^3\mathcal F_{TTT}=0.
\tag{16}
\]
The independent coordinates I,V,T and the transcendence of f/g1
force all four third derivatives to vanish. Thus \(\mathcal F\) has total degree
at most two in V,T.

After dividing I by A, compare its P-squared coefficient.
The element v1 is transcendental over kX: differentiating a minimal
polynomial would contradict \((v_1)_s\ne0\). The quadratic
coefficients therefore force precisely
\[
I=U-\frac{T^2}{w_1^2}+\alpha(X)V+\beta(X)T+\gamma(X),
\qquad \alpha,\beta,\gamma\in k_X.
\tag{17}
\]
All divisions in this argument occur in the generic field kX, not
by actual polynomial units. No specialization of (17) at a root
of w1 will be used.

## 5. Exact consequences of the invariant's P coefficient

The P coefficient of (17) is zero:
\[
u-2T_0/w_1+\alpha v_1+\beta w_1=0.
\tag{18}
\]
Differentiate in s at fixed t,P,X, using the FULL T0 in (12).
Since \(r_s=\lambda/2+Hz_s/2\), this gives
\[
\alpha=\frac{2(HX+\eta)}{w_1},\qquad
\eta=\frac{(F/t)_s+K/2}{z_s}\in\mathbb C.
\tag{19}
\]
To justify the last assertion, the displayed identity puts eta in
both L and C(X). Since actual X is transcendental over \(\mathcal K\) containing L,
their intersection is C. Equivalently a rational function of X that
equals an element of L must be complex constant.

Differentiate (18) in t, multiply by w1/2, and retain the t derivative
of \(2tX^3\). The COMPLETE identity is
\[
C_Xw_1-(F/t)_t-2R'X+\eta z_t
             -2a(HX+\eta)C_X-2X^3=0.
\tag{20}
\]
The cubic and quadratic X coefficients cancel, not contradict each
other. The remaining coefficients, together with (19), give
\[
\begin{gathered}
R=R_0+r_1t,\qquad r_1=-\lambda^2-K/2-a\eta,\\
F/t=\eta z-Ks/2-\lambda(K+2a\eta)t+F_*,\\
n_0=(\lambda^2+K+a\eta)t^2-2R_0t+N_0,
\qquad R_0,F_*,N_0\in\mathbb C.
\end{gathered}
\tag{21}
\]
The first integration is in the exact F0 of Section1, and the second
uses both coefficient derivatives. These assertions do not require
rationality of either field. The additive complex constant \(F_*\)
is distinct from the coefficient field \(F_0\).

## 6. Complete lower scalar in a licensed separating basis

Since \(z_s\ne0\), \((t,z)\) is an exact separating basis of L.
Write \(S=s\) as its element in this basis, so
\(S_z=1/z_s\ne0\). Make the intrinsic affine substitution
\[
\Pi=P+s/2,\qquad C=c-as^2/4-zs/2.
\tag{22}
\]
Neither S nor C is assumed rational in t,z. The Jacobian from
(t,s,P) to (t,z,Pi) is z_s, and \(N\Pi=\rho\).
The actual row operation \((Y,Z,W)\mapsto(Y,U,T)\), with X fixed,
has determinant one. Consequently
\[
\mathcal J=\det\frac{\partial(Y,U,T)}{\partial(t,z,\Pi)}
                   =-\frac{a_0^4}{\rho z_s}\in L^*.
\tag{23}
\]
It has no X or Pi dependence, but its coefficient-field value is
not assumed complex or independent of t,z.

Here are the COMPLETE rows after (21),(22):
\[
\begin{aligned}
Y={}&-a\Pi^2/2+(X+\lambda-z/2)\Pi-C/2+Hz/2
          +R_0+r_1t-XS/2+tX^2,\\
U={}&\Pi^2+2t(X+\lambda)\Pi+H(tz-S)
                +t^2(X^2-\lambda^2-a\eta)+N_0,\\
T={}&w_1\Pi+(HX+\eta)z+tD(X)+2R_0X+F_*,\\
D(X)={}&2X^3+2r_1X-\lambda(K+2a\eta).
\end{aligned}
\tag{24}
\]
The cubic-X term is still present. The constants R0,F*,N0 have
not been set to zero; their derivatives simply vanish in (23).
For the following ledger put
\(J_{ij}=[X^i\Pi^j]\mathcal J\).
Every \(J_{ij}\) with \((i,j)\ne(0,0)\) is zero by (23).

### 6.1 The complete H=0 boundary

Here \(\lambda=0\). Direct expansion of (24) gives
\[
\begin{aligned}
J_{21}&=2a\eta(S_z-t),\\
J_{11}&=\eta(2aC_z+S_t-z),\\
J_{20}&=\eta t(S_t-z),\\
J_{10}&=\eta t(KaS_z+K+C_t).
\end{aligned}
\tag{25}
\]
If \(\eta\ne0\), these equations force, in order,
\(S_z=t\), \(S_t=z\), \(C_z=0\), and
\(C_t=-K(1+at)\). The remaining Pi coefficient is then
\[
J_{01}=2a\eta^2(1+at)\ne0,
\tag{26}
\]
contradicting (23). All divisions used nonzero a,eta,t.
The nonzero delta was retained in the original assumptions.

If \(\eta=0\), the full determinant from (24) is identically zero.
This can also be seen without expansion: U equals
\((\Pi+tX)^2+N_0\), and T equals
\((2X^2-K)(\Pi+tX)+2R_0X+F_*\). Their differentials at fixed X
are proportional. This contradicts the nonzero scalar (23).
Thus every H=0 case is excluded.

### 6.2 The H-nonzero coefficient certificate

Suppose \(H\ne0\), and put the COMPLEX constants
\[
q=\eta/H,\qquad g=K+2\lambda q-2q^2.
\tag{27}
\]
This q is not \(m_{tt}\), which is zero throughout the note.
The case q=0 is retained. Since \(a\ne0\), also
\(\lambda=aH/2\ne0\).

The two equations \(J_{21}=J_{11}=0\), expanded from the full rows,
solve exactly as
\[
\begin{aligned}
C_z={}&-(\lambda+q)S_z+qt,\\
C_t={}&-(\lambda+q)S_t+(2\lambda+q)z-agS_z
            -K-4\lambda q-2aq(2\lambda+q)t.
\end{aligned}
\tag{28}
\]
These equations divide only by a and H, not by g or q.
After (28), two further full coefficients are
\[
\begin{aligned}
J_{01}&=-\frac{Hg}{2}
       \{z-S_t-2a(\lambda-q)S_z-2aqt\},\\
J_{20}&=aHS_z
       \{H(z-2q)+(g-4\lambda q)t-gS_z\}.
\end{aligned}
\tag{29}
\]

Assume for contradiction that \(g\ne0\). Because \(S_z\ne0\),
(29) then gives
\[
S_z=\frac{H(z-2q)+(g-4\lambda q)t}{g},\qquad
S_t=z-2a(\lambda-q)S_z-2aqt.
\tag{30}
\]
Substitution of precisely (28),(30) in the remaining X coefficient,
with no differential or scalar-level specialization, gives
\[
J_{10}=-aH^2S_z
       \{(\lambda-2q)z+(K+2q^2)(1+at)\}.
\tag{31}
\]
Thus the expression in braces vanishes. The coefficient basis
(t,z) is separating, so differentiating it in z gives
\(\lambda=2q\). Then \(1+at\ne0\) gives \(K=-2q^2\).
But these equalities make g zero, contradicting this branch.
Consequently the remaining necessary condition is
\[
\boxed{g=0,\qquad K=2q^2-aHq.}
\tag{32}
\]
No conclusion was obtained by dividing by g in its zero branch.

## 7. The surviving constants contradict an actual complex-X fiber

Under (32), evaluate the full T row (24) at the COMPLEX value
\(X=-q\). Its Pi coefficient is
\[
w_1(-q)=2q^2-aHq-K=0.
\]
Its z coefficient is \(-Hq+\eta=0\). Direct substitution of
\(r_1=-\lambda^2-K/2-aHq\) in D gives \(D(-q)=0\).
Therefore the complete identity is
\[
T\big|_{X=-q}=F_*-2qR_0\in\mathbb C.
\tag{33}
\]
This specializes the actual polynomial T, not the rational generic
invariant (17). In particular no denominator w1 is specialized.
The result is complex constant, not merely a constant for N or for
one coefficient derivative.

Here is the original-ring justification of this specialization.
The ideal \((X+q)\) is prime in the actual coordinate ring
\(\mathcal B=\mathbb C[X,U,V,T]\).
It does not contain a0: otherwise, additivity of E-degree would give
\(\deg_Ea_0\ge\deg_E(X+q)=1\), contrary to \(Ea_0=0\).
The original slice relation, without deleting x0, gives
\[
\mathcal B_{a_0}=A_{a_0}[X].
\tag{34}
\]
Evaluation at X=-q in this polynomial ring is legitimate and has
kernel \((X+q)\mathcal B_{a_0}\). The injection
\(A_{a_0}\hookrightarrow\mathcal K=L(P)\) identifies it with the literal
coefficient evaluation used in (33).
Thus (33) puts \(T-(F_*-2qR_0)\) in that localized ideal.
Primality and \(a_0\notin(X+q)\) make its contraction exactly
\((X+q)\mathcal B\).

This is impossible in the actual polynomial frame (11): modulo
X+q, T remains an independent polynomial variable of C[U,V,T],
and cannot equal a complex constant. The contradiction includes
q=0, K=0 and multiple roots of w1.

Together with Section6.1, this excludes every constant-a case
under the retained hypotheses.

## 8. Verification and precise boundary

The held496 source was completely read through EOF and revalidated
at SHA55552b3859862962a4573b91a9792854873eac527bf0403f4cfbb7d84a501565.
The full494 and426 sources were also read, and the primary field
theorem and its irreducibility definitions were checked directly.
Fresh45b6ab verifies both orders of the composite actual inverses,
the entire weighted initial relation, both coupling identities,
and the auxiliary-frame inverse. Fresh4963db verifies (9).
Freshc13989 reconstructs all seven indicated original-row coefficients
with the complete cubic-X term. Fresh400f9b verifies every identity
(28)--(31), all five H-zero coefficient steps and the entire
H=eta=0 determinant, with zero residuals.

An earlier unsaved candidate omitted 2tX^3 from T0. That candidate
was withdrawn before any source was written; its proposed cubic-X
contradiction is not used here. Equation (20) explicitly records
the cancellation, and the actual lower-coefficient and fiber proof
above supplies the result instead.

The conclusion is only the constant-a part of the actual q=0
nonlinear-conic sector. The moving-a branch, delta-zero degree drop,
arbitrary nonlinear projected curves and arbitrary chart entry
remain outside this note. No unrestricted cancellation result or
descent of a generic field coordinate to an ambient coordinate is
asserted. No saved checker was executed, imported, compiled or
rerun. No earlier source or canonical record was edited.
