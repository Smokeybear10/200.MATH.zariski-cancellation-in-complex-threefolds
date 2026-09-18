# The genuine cubic excludes the remaining degree-(4,6) intercept pair

Working result: in365's complete actual chart with k=s and n_ss
nonzero, the intrinsic pair (deg sigma,deg theta)=(4,6) is
impossible. The normal form of370 gives the exact ideal of the
polynomial line. Its degree-three elements have a restricted
highest homogeneous part, incompatible with the literal fourth
potential of369.

The argument includes zero and nonzero centered quadric levels.
It uses no projective saturation, coefficient-field rationality,
or promotion of an L-valued change to an actual polynomial map.
It does not settle any other intrinsic degree pair.

## 1. Full actual entry and the genuine cubic support

Retain all actual hypotheses of
[365](principal-paraboloid-nonlinear-intercept-unequal-degree-gate-pass365-working.md),
not merely its abstract quadric relation:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
a_0=EX\ne0,\qquad N=[u^4]\partial_Z|_A,\\
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\qquad
Nv=1,\qquad O=L[v]=L[y,\sigma,\theta]=L[y,z,w],\\
K=L(v)=\mathbb C(y,z,w),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
The selected partial is the literal actual Z-partial. Assume k=s,
n_ss nonzero, and, for contradiction,
\[
(\deg_v\sigma,\deg_v\theta)=(4,6).
\tag{2}
\]

The actual complex polynomial changes of
[369](principal-paraboloid-nonlinear-intercept-linear-coefficient-normalization-pass369-working.md)
preserve every gate in(1), the pair(2), and the literal selected
partial. They first replace t by t-tau and then remove the
complex linear-coefficient constants. We may therefore use its
actual normalized chart
\[
n=-\frac{s^2}{4t^2}+f,\qquad
f\in F:=\ker_L\partial_s,\qquad [F:\mathbb C(t)]<\infty.
\tag{3}
\]
No assertion that L=F(s) or F=C(t) is needed. In particular t is
a nonzero element of L. All the further changes in this note
are only changes of formal variables over L.

Use the coefficient notation of365 and369:
\[
\begin{gathered}
\nu=n_s,\quad b=n_{ts},\quad A=n_{tt}/2-\nu^2,\quad
C=\ell_s+\nu^2,\quad \bar h=h_0-\nu\ell+n_t^2/4,\\
\zeta=U+n_t/2-\nu P+V/(2t),\quad
R=\zeta-tbP+tC,\quad \Omega=A+t^2b^2\ne0,\\
\Lambda=2t^2bC+\ell_t,\qquad D=t^2C^2-\bar h .
\end{gathered}
\tag{4}
\]
Here U,P,V evaluate to y,sigma,theta. The capital R is a formal
affine linear expression, not a coordinate of the actual four-ring.
By365, its evaluated degree is two. In the independent formal
variables P,R,V the complete third level is
\[
\begin{aligned}
\mathsf H:=H-h_0
&=\Omega P^2+2tbPR+R^2-\frac{RV}{t}
       -\Lambda P-2tCR+D,\\
\mathsf H_2
&=\Omega P^2+2tbPR+R^2-\frac{RV}{t}.
\end{aligned}
\tag{5}
\]
The subscript denotes the highest homogeneous part for ordinary
total degree in these three formal variables.

Let Q be the genuine fourth potential, with evaluated level q0,
and use the modification already verified in369:
\[
\widetilde Q=(Q-q_0)+\frac Pt\mathsf H .
\tag{6}
\]
It vanishes on the actual line. Its complete cubic part is
\[
\widetilde Q_3=E_0P^3+\frac1tPR^2,\qquad
E_0=\frac{n_{ttt}}6-tb^2-2b\nu+\frac At.
\tag{7}
\]
All other terms have total degree at most two. In particular its
total degree is exactly three. Before the actual removal of the
linear coefficient B in n, the same formula has the additional
term D0 P^2 V, where D0=(t^2B)''/(2t^2). The proof below would
also allow that term, but(3) makes it zero.

For orientation, the raw cubic part before the affine substitution
and modification is
\[
Q_3=-2bP^2U-2n_{ss}PVU+
\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V+
\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3.
\tag{8}
\]
Substitute U=(tb+nu)P+R-V/(2t)-tC-n_t/2.
Here n_ss=-1/(2t^2), n_tss=1/t^3, n_sss=0.
The PV^2 terms cancel. The P^2R and PRV coefficients before
adding(P/t)H are -2b and 1/t^2; the addition cancels both and
supplies precisely PR^2/t. This recovers(7) from the literal
potential, rather than identifying Q with an arbitrary cubic.

## 2. The surviving normal form supplies the entire curve ideal

The affine L-change of
[367](principal-paraboloid-nonlinear-intercept-geometric-degree-exclusions-pass367-working.md)
is, in the present notation,
\[
\begin{gathered}
p_{\rm old}=R,\qquad
x=P+\frac{tb}{\Omega}R-\frac{\Lambda}{2\Omega},\\
q_{\rm old}=V-\frac{tA}{\Omega}R-
                 \frac{t^2b\Lambda}{\Omega}+2t^2C,\qquad
\beta=-\frac1{t\Omega},\\
\frac{\mathsf H}{\Omega}=x^2+\beta p_{\rm old}q_{\rm old}-d,
\qquad d=\frac{\Lambda^2}{4\Omega^2}-\frac D\Omega .
\end{gathered}
\tag{9}
\]
Its affine inverse is explicit in367. Whole return gives
O=L[p_old,x,q_old], with degrees(2,4,6). The transformed genuine
fourth potential has unit evaluated gradient minors with the
quadric, so is not a multiple of it.

These are exactly the hypotheses of the fully read
[370](principal-paraboloid-degree-two-four-six-odd-part-normal-form-pass370-working.md).
Its Type II is excluded there by the two ruling degrees. Type I
therefore holds after translating the parameter over L and
rescaling p_old and q_old by inverse nonzero field constants.
Write p=p_old/alpha and q=alpha*beta*q_old, with alpha in L*.
Then
\[
\begin{gathered}
p=v^2-\delta,\qquad K(p)=a p+c,\qquad a,\varepsilon\in L^*,\\
x=pK(p)+\varepsilon v,\qquad
q=-pK(p)^2-2\varepsilon vK(p)-\varepsilon^2,\qquad
d=\varepsilon^2\delta.
\end{gathered}
\tag{10}
\]
The letter c in K is unrelated to the coefficient C in(4).
Neither delta nor d is required to be nonzero.

In the formal ring L[p,x,q], put
\[
H_c=x^2+pq-d,\qquad
G_c=q+2K(p)x-pK(p)^2+\varepsilon^2.
\tag{11}
\]
Both vanish on(10). They generate the entire kernel of the
evaluation map, not just an ideal with the same generic component.
To see this, use the formal polynomial automorphism
\[
p_1=p,\quad x_1=x-pK,\quad q_1=q+2Kx-pK^2,
\tag{12}
\]
whose inverse is p=p1, x=x1+p1K, q=q1-2Kx1-p1K^2.
It preserves x^2+pq and sends the two equations to
\[
H_c=x_1^2+p_1q_1-d,\qquad G_c=q_1+\varepsilon^2.
\tag{13}
\]
Eliminate q1 using its monic linear equation. The quotient is
\[
L[p_1,x_1]/(x_1^2-\varepsilon^2p_1-d)
\simeq L[x_1],\qquad
p_1=(x_1^2-d)/\varepsilon^2.
\tag{14}
\]
Its map to O is x1 maps to epsilon*v, an isomorphism because
epsilon is nonzero. This proves the exact kernel assertion
without localization, saturation, radical replacement, or a
restriction to d nonzero.

Pull Gc back through the invertible affine map(9) and the constant
rescalings to obtain G in L[P,R,V]. Since p=R/alpha and x,q are
affine in P,R,V, its cubic part comes only from -pK^2:
\[
\ker\bigl(L[P,R,V]\longrightarrow O\bigr)=(\mathsf H,G),
\qquad G_3=\gamma R^3,\qquad
\gamma=-a^2/\alpha^3\in L^*.
\tag{15}
\]
The harmless factor Omega relating Hc and H in(9) is a field
unit. Formula(5) and Omega nonzero give
\[
\gcd(\mathsf H_2,G_3)=1,
\tag{16}
\]
because R does not divide H2. All uses of(12) remain confined to
the formal L-algebra; it is not an actual ambient automorphism.

## 3. A finite degree-reduction lemma

Let f,g belong to a polynomial ring over a field, with exact
degrees two and three and coprime highest forms f2,g3.
If a nonzero polynomial F of degree at most three lies in(f,g),
then
\[
F=L_1f+\eta g,\qquad \deg L_1\le1,\quad \eta\in L.
\tag{17}
\]

Here is an elementary finite proof. Start with any representation
F=A0 f+B0 g, interpreting the degree of zero as minus infinity,
and set M=max(deg A0+2,deg B0+3). If M>deg F, neither term can
be the unique term of degree M. Thus their product degrees are
equal and their top forms cancel:
A0_top*f2+B0_top*g3=0.
Coprimality in the polynomial UFD implies
A0_top=C0*g3 and B0_top=-C0*f2, for a homogeneous polynomial
C0 of degree M-5. In particular such cancellation is impossible
if M<5. Replace the multipliers by
\[
A_1=A_0-C_0g,\qquad B_1=B_0+C_0f.
\tag{18}
\]
The represented polynomial F is unchanged, and the leading parts
of both multipliers cancel. Consequently the new maximum product
degree is strictly smaller than M. Repeat only while M>deg F.
The nonnegative integer M strictly decreases, so the process
terminates. At termination M<=deg F<=3, giving deg A<=1 and
deg B<=0. This proves(17), including the possibility B=0.
No infinite division, completion, or assumption about arbitrary
representations with already bounded multipliers has been used.

## 4. The literal cubic has an impossible highest part

Apply the lemma to(15),(16) and the nonzero degree-three element
Qtilde of the kernel. There are an affine L1 and eta in L with
\[
\widetilde Q=L_1\mathsf H+\eta G.
\tag{19}
\]
Write the linear homogeneous part of L1 as lP P+lR R+lV V.
Comparing cubic parts in the independent formal variables gives
\[
E_0P^3+\frac1tPR^2
=(l_PP+l_RR+l_VV)
  \left(\Omega P^2+2tbPR+R^2-\frac{RV}{t}\right)
  +\eta\gamma R^3.
\tag{20}
\]
The RV^2 coefficient gives -lV/t=0, hence lV=0.
With lV zero, the PRV coefficient gives -lP/t=0, hence lP=0.
With both zero, the R^2V coefficient gives -lR/t=0, hence lR=0.
The right side is now a scalar multiple of R^3, while the left
side has nonzero PR^2 coefficient 1/t. This is a contradiction.

The same comparison would work with a D0 P^2V term on the left:
that monomial does not alter any of the three vanishing comparisons
or the final PR^2 coefficient. Thus the obstruction is the genuine
cubic support itself, not a division by a potentially zero E0,
d, delta, b, or D0. The nonzero gates used are precisely t,
Omega, alpha, a, and epsilon, each established above.

## 5. Exact conclusion and remaining scope

The assumed actual pair(2) is impossible. Equivalently, the
formal degree-(2,4,6) Type I normal form allowed by whole return,
a quadric, and some transverse cubic cannot carry the literal
fourth potential of the current actual chart.

This does not contradict370's formal example: its auxiliary
cubic Gc has pure R^3 highest part after the affine pullback,
not the obligatory PR^2/t term of Qtilde. Nor does it normalize
general k, assume rationality of the coefficient field, recognize
the invariant three-ring, or settle365's other degree sectors.
The pairs(1,2) and(2,3) are not addressed by this note.

The complete369,370,367 sources were read for this composition.
Fresh unsaved algebra independently checked the exact quotient
relation, both equation transports in(13), and every coefficient
comparison in(20). The ideal and finite degree-descent proofs are
the written arguments, not finite-test consequences. No saved
checker was executed, imported or compiled, and no retained source
or canonical index was edited. No actual realization, unrestricted
cancellation, novelty, human-expert or proof-assistant certification
claim is made.
