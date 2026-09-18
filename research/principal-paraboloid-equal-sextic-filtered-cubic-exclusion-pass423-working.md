# The genuine fourth potential excludes the equal-sextic profile

Working result under the complete supplied actual264 chart with
k=s and n_ss nonzero: the remaining profile
(deg R,deg v1,deg sigma)=(2,4,6) is impossible.
The abstract normal form of370 determines the entire intrinsic
curve ideal. Its degree-three elements have a restricted highest
part, incompatible with the genuine cubic tensor of419.

The argument includes zero and nonzero centered quadric levels.
All affine changes, rescalings and the polynomial ideal calculation
below are over the exact coefficient field L. None is promoted to
an original polynomial change of X,Y,Z,W. This note excludes only
the indicated profile and does not assert arbitrary-chart entry,
original-ring recognition, or unrestricted cancellation.

## 1. Full actual hypotheses and the sextic profile

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the necessary frontier of
[417](principal-paraboloid-equal-quadratic-exclusion-synthesis-pass417-working.md),
and the full-potential conclusions of
[419](principal-paraboloid-higher-degree-curvature-evolution-pass419-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\qquad
E=\partial_{u_0},\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\qquad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad Nv_0=1,\qquad a_0=EX\in L^*,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\qquad
K=L(v_0)=\mathbb C(y,z,w),\\
J_{t,s,v_0}(X)=-a_0^4\in L^*,\qquad k=s,\qquad e=n_{ss}\ne0.
\end{gathered}
\tag{1}
\]
The global slice, original localization, literal selected partial,
both returns, full calibrated scalar, genuine potential levels and
their evaluated unit ideals remain imposed. The exact coefficient
partials commute and have joint constants C.

Use the following coefficient and intrinsic notation:
\[
\begin{gathered}
a=n_t,\quad \nu=n_s,\quad b=n_{ts},\quad C=\ell_s+\nu^2,\\
\lambda=[v_0^6]y/[v_0^6]\sigma,\qquad
\mu=[v_0^6]\theta/[v_0^6]\sigma,\qquad
u_1=y-\lambda\sigma,\quad v_1=\theta-\mu\sigma,\\
\delta=\lambda-\nu,\qquad \beta=b+e\mu,\qquad
j=\delta a-\ell_t-C\mu,\qquad
\mathcal K=\beta^2+2e\delta^2,\qquad
R=2\delta u_1+\beta v_1+j .
\end{gathered}
\tag{2}
\]
The symbol v1 is a lower intrinsic function, not the parameter v0.
For contradiction, assume the profile
\[
(\deg R,\deg v_1,\deg\sigma)=(2,4,6).
\tag{3}
\]
The preceding frontier and419 give
\[
\begin{gathered}
\delta\ne0,\qquad \mathcal K\ne0,\qquad \beta\ne0,\\
\mathscr D=\partial_t+\mu\partial_s,\qquad
\mathscr D\lambda=0,\qquad \mathscr D\mu=-4\lambda,\\
\mathscr D\beta=-\frac{2\beta^2}{\delta},\qquad
\mathscr De=-\frac{3e\beta}{\delta}
                 -\frac{\beta^3}{2\delta^3}.
\end{gathered}
\tag{4}
\]
No assumption that lambda is nonzero or noncomplex is added.
The beta-zero case has already been excluded in419, Section5,
for every retained profile, including this one.

## 2. Exact affine quadric transport and its inverse

In independent formal variables(P,U1,V1), evaluating to
(sigma,u1,v1),407 gives the complete third level
\[
\mathsf H:=H-h_0
=P(2\delta U_1+\beta V_1+j)
+U_1^2+aU_1+\frac e2V_1^2-CV_1+\nu\ell-h_0.
\tag{5}
\]
Replace U1 by(R-beta*V1-j)/(2delta). Hereafter(P,R,V1)
are independent formal variables; their evaluations are the
intrinsic functions denoted by the same letters.
Set
\[
\begin{gathered}
\mathcal A=\frac{\mathcal K}{4\delta^2}\in L^*,\qquad
\mathcal B_1=\frac{\beta j}{2\delta^2}
                    -\frac{a\beta}{2\delta}-C,\\
\mathcal C_0=\frac{j^2}{4\delta^2}-\frac{aj}{2\delta}
                    +\nu\ell-h_0,\\
p_{\rm old}=R,\qquad
x_{\rm old}=V_1+\frac{\mathcal B_1}{2\mathcal A},\\
q_{\rm old}=P+\frac{R}{4\delta^2}
             -\frac{\beta V_1}{2\delta^2}
             -\frac{j}{2\delta^2}+\frac a{2\delta}.
\end{gathered}
\tag{6}
\]
This is precisely the affine transport in
[421, Section2](principal-paraboloid-equal-degree-geometric-profile-reduction-pass421-working.md).
Its complete inverse is
\[
\begin{aligned}
V_1&=x_{\rm old}-\frac{\mathcal B_1}{2\mathcal A},\\
U_1&=\frac{p_{\rm old}-\beta V_1-j}{2\delta},\\
P&=q_{\rm old}-\frac{p_{\rm old}}{4\delta^2}
       +\frac{\beta V_1}{2\delta^2}
       +\frac{j}{2\delta^2}-\frac a{2\delta}.
\end{aligned}
\tag{7}
\]
Every coefficient belongs to L, and all denominators used in
this inverse are nonzero by(4).

Direct substitution gives
\[
\boxed{\quad
\frac{\mathsf H}{\mathcal A}
=x_{\rm old}^2+\frac1{\mathcal A}p_{\rm old}q_{\rm old}-d_0,
\qquad
d_0=\frac{\mathcal B_1^2}{4\mathcal A^2}
                         -\frac{\mathcal C_0}{\mathcal A}.
\quad}
\tag{8}
\]
The centered level d0 is arbitrary, including zero. After
evaluation, the inverse and(3) give
\[
O=L[p_{\rm old},x_{\rm old},q_{\rm old}],\qquad
(\deg p_{\rm old},\deg x_{\rm old},\deg q_{\rm old})=(2,4,6).
\tag{9}
\]
The only degree-six term in q_old is P. The constant shift in
x_old does not change its degree four.

The complete fourth level Q-q0 has total degree three, evaluates
to zero, and its evaluated gradient minors with H generate O.
An invertible affine substitution over L and the field-unit
scaling in(8) preserve this unit ideal. Consequently the
transformed fourth level is not a multiple of the quadric:
such a multiple would have gradient proportional to the
quadric gradient along the line and all these minors would vanish.
These are exactly the abstract inputs of370. No coefficient
derivative of the formal substitution is taken.

## 3. The abstract normal form and all rescalings

Use only Sections1--5 of
[370](principal-paraboloid-degree-two-four-six-odd-part-normal-form-pass370-working.md).
Their hypotheses are(8),(9) and a degree-at-most-three
nonmultiple relation, just established. They do not require
the strict theta-dominant coefficient identities or the actual
normalization used in370's separate application.

Write
p_old=alpha*v0^2+alpha1*v0+alpha0, with alpha in L*.
Define
\[
\begin{gathered}
v=v_0+\frac{\alpha_1}{2\alpha},\qquad
\Delta=\frac{\alpha_1^2-4\alpha\alpha_0}{4\alpha^2},\\
p=p_{\rm old}/\alpha=v^2-\Delta,\qquad
x=x_{\rm old},\qquad q=\frac{\alpha}{\mathcal A}q_{\rm old}.
\end{gathered}
\tag{10}
\]
The translating coefficient is N-invariant, so Nv=1. No
coefficient square root is introduced. The quadric becomes
x^2+pq=d0, and the whole generated ring is still L[v].

The surviving Type I conclusion of370 is
\[
\begin{gathered}
K_1(p)=a_2p+b_2,\qquad a_2,\varepsilon\in L^*,\quad b_2\in L,\\
p=v^2-\Delta,\qquad x=pK_1(p)+\varepsilon v,\\
q=-pK_1(p)^2-2\varepsilon vK_1(p)-\varepsilon^2,\qquad
d_0=\varepsilon^2\Delta .
\end{gathered}
\tag{11}
\]
For the precise reuse boundary, the parity decomposition there
first gives x=E(p)+vF(p). Whole return yields Type I or its
Type II with nonzero constant even part. Type II has two ruling
degrees two and four on a smooth quadric and cannot be contained
in a nonmultiple cubic section. That argument is abstract and
does not depend on which original intrinsic function had degree
six. Type I and(11) include d0=Delta=0; no smooth-quadric argument
is applied to that boundary.

For completeness, the entire original intrinsic parametrization
is recovered without discarding any coefficient function:
\[
\begin{aligned}
R&=\alpha p,\\
v_1&=pK_1(p)+\varepsilon v-\frac{\mathcal B_1}{2\mathcal A},\\
u_1&=\frac{\alpha p-\beta v_1-j}{2\delta},\\
\sigma&=\frac{\mathcal A}{\alpha}
       \bigl(-pK_1(p)^2-2\varepsilon vK_1(p)-\varepsilon^2\bigr)
       -\frac{\alpha p}{4\delta^2}
       +\frac{\beta v_1}{2\delta^2}
       +\frac{j}{2\delta^2}-\frac a{2\delta},\\
y&=\lambda\sigma+u_1,\qquad \theta=\mu\sigma+v_1 .
\end{aligned}
\tag{12}
\]
In particular no coefficient in(11),(12) is asserted complex,
rational in t,s, or polynomial in the original four-ring.

## 4. The entire curve ideal, including zero centered level

In the formal polynomial ring L[p,x,q], put
\[
F_c=x^2+pq-d_0,\qquad
G_c=q+2K_1(p)x-pK_1(p)^2+\varepsilon^2.
\tag{13}
\]
Both vanish on(11). The polynomial automorphism
\[
\begin{gathered}
p_1=p,\qquad x_1=x-pK_1(p),\qquad
q_1=q+2K_1(p)x-pK_1(p)^2,\\
p=p_1,\qquad x=x_1+p_1K_1(p_1),\qquad
q=q_1-2K_1(p_1)x_1-p_1K_1(p_1)^2
\end{gathered}
\tag{14}
\]
preserves x^2+pq. In the new formal variables, the two equations
are x1^2+p1*q1-d0 and q1+epsilon^2. Therefore
\[
L[p,x,q]/(F_c,G_c)
\simeq L[p_1,x_1]/(x_1^2-\varepsilon^2p_1-d_0)
\simeq L[x_1].
\tag{15}
\]
The second isomorphism eliminates p1 using epsilon nonzero.
Evaluation sends x1 to epsilon*v, an isomorphism onto L[v].
Hence(13) generates the entire evaluation kernel. This argument
uses neither saturation nor radical replacement, and it remains
valid at d0=0.

Pull Gc back using(6),(10) to a polynomial G in L[P,R,V1].
Since p=R/alpha and x,q are affine formal expressions, its
degree-three part comes only from -p*K1(p)^2. Consequently
\[
\begin{gathered}
\ker\bigl(L[P,R,V_1]\longrightarrow O\bigr)=(\mathsf H,G),\\
G_3=\gamma R^3,\qquad \gamma=-\frac{a_2^2}{\alpha^3}\in L^*,\\
\mathsf H_2=RP+\frac{R^2}{4\delta^2}
                 -\frac{\beta RV_1}{2\delta^2}+\mathcal A V_1^2,
\qquad \gcd(\mathsf H_2,G_3)=1.
\end{gathered}
\tag{16}
\]
The quadric differs from Fc only by the field unit Acal.
Coprimality follows because R does not divide H2: its V1^2
coefficient is the nonzero Acal.

## 5. Finite filtered-degree descent

We repeat the algebraic lemma of
[373, Sections2--3](principal-paraboloid-degree-four-six-filtered-cubic-exclusion-pass373-working.md),
not that note's strict theta-dominant literal coefficients.
If f,g have degrees two and three with coprime highest forms,
every nonzero T of degree at most three in(f,g) has a
representation
\[
T=L_1f+\eta g,\qquad \deg L_1\le1,\qquad \eta\in L.
\tag{17}
\]

Indeed start with any representation T=A f+B g and let
M=max(deg A+2,deg B+3), using degree minus infinity for zero.
If M>deg T, both products have degree M and their highest
forms cancel. Coprimality gives
A_top=C_*g3 and B_top=-C_*f2, where C_* is homogeneous
of degree M-5. Such cancellation is impossible for M<5.
Replace A by A-C_*g and B by B+C_*f. The represented
polynomial is unchanged, while both leading terms cancel and
M strictly decreases. Repeating terminates with M<=deg T<=3,
which gives(17). This is finite polynomial degree reduction,
not an assumption that an arbitrary initial representation
already has bounded multipliers.

Apply(17) to the complete nonzero fourth level Q-q0 in(16).
Its homogeneous cubic part must lie in
\[
Q_3\in
\mathsf H_2\,L[P,R,V_1]_1+L\,R^3,
\tag{18}
\]
where the subscript 1 means homogeneous linear forms.
The genuine polynomial is used here, including all its lower
coefficients; only after this ideal membership is established
do we compare highest parts.

## 6. The literal cubic violates the required highest part

The entire shifted cubic tensor in419, equation(10), is
\[
-2\beta P^2U_1+\frac{\mathscr D\beta}{2}P^2V_1
-2ePU_1V_1+\frac{\mathscr De}{2}PV_1^2
+\frac{e_s}{6}V_1^3.
\tag{19}
\]
Substitute U1=(R-beta*V1-j)/(2delta) and use both exact
gates in(4). The resulting cubic part is
\[
\boxed{\quad
Q_3=-\frac{\beta}{\delta}P^2R
       -\frac{\beta\mathcal A}{\delta}PV_1^2
       -\frac e\delta PRV_1+\frac{e_s}{6}V_1^3 .
\quad}
\tag{20}
\]
In particular the P^2*V1 coefficient is zero, and
e*beta/delta+(Dscript e)/2=-beta*Acal/delta.
All j terms and actual level derivatives h0_t,h0_s belong to
the full polynomial of total degree at most two. They have not
been set to zero or replaced by freely chosen coefficients.

If(18) held, write the required linear multiplier as
lP*P+lR*R+lV*V1. Comparing P^2*R, P*R^2 and P*R*V1,
respectively, forces it to be exactly
\[
L_{\rm top}
=-\frac{\beta}{\delta}P+\frac{\beta}{4\delta^3}R
                              -\frac{2\mathcal A}{\delta}V_1.
\tag{21}
\]
Here R^3 cannot affect any of these comparisons. Subtracting
this forced multiple from the entire cubic gives
\[
\begin{aligned}
Q_3-L_{\rm top}\mathsf H_2
={}&-\frac{\beta}{16\delta^5}R^3
  +\frac{\beta^2+e\delta^2}{4\delta^5}R^2V_1\\
&-\frac{5\beta\mathcal K}{16\delta^5}RV_1^2
  +\left(\frac{e_s}{6}
                   +\frac{2\mathcal A^2}{\delta}\right)V_1^3 .
\end{aligned}
\tag{22}
\]
The coefficient of R*V1^2 is nonzero by(4). But(18) requires
the remainder to be a scalar multiple of R^3. This is a
contradiction in the independent polynomial ring L[P,R,V1].

No division by e_s, the centered level d0, Delta, b2, or any
coefficient in the remainder has occurred. The nonzero factors
used are delta, beta, Kcal, alpha, a2 and epsilon, each licensed
before use.

## 7. Exact conclusion and verification scope

The equal-sextic profile(3) cannot occur under(1). Its formal
Type I quadric line is not itself impossible:370 constructs a
cubic Gc with the required whole return and unit minors.
The contradiction is that this intrinsic line cannot carry
the genuine fourth potential whose highest part is(20).

The only reused parts of373 are the abstract entire-kernel
argument and finite degree descent, both repeated here.
Its strict theta-dominant coefficient family and its PR^2/t
literal cubic coefficient are not inputs to this proof.
No coefficient-field affine map or polynomial automorphism
has been promoted to an original-coordinate change.
This note does not exclude the separate cubic profile or
compose an unrestricted sector-recognition statement.

The complete421 source was freshly read in848073+afeef4 at
24d127c19589b859490bd078c12f9d7581c74f200215f6ba90ab4a2376bd20a3.
Complete370 and373 were freshly read and rehashed in
d708ab and54cc63. Complete419 was freshly reread in0c1a82 at
2d74703f1409f8cf87d3a1eddaa3b593089ce17932c88aa21dba204d962b537c.
The writing guide was read completely in336bb6 before authoring.

Fresh unsaved4d922d independently reconstructed the affine
quadric transport, the Type I quadric and cubic identities,
both equation transports in(14),(15), the pure-R^3 pullback,
the cubic tensor after both419 gates, and the complete
remainder(22). Every residual was zero, including the exact
critical coefficient -5*beta*Kcal/(16delta^5). These calculations
check identities; the full-kernel and finite-descent claims are
proved in the text and are not inferences from finite sampling.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. This source
is held for independent review, without claims of unrestricted
cancellation, arbitrary entry, novelty, human-expert verification
or formal-proof certification.
