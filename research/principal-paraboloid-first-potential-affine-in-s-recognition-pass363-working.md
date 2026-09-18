# Recognition with a first potential affine in the second parameter

Working synthesis, retaining the dependencies of348: in the full actual
principal chart264, the conditions
\[
k_s\in\mathbb C^*,\qquad k_{ttt}=0,\qquad n_{ss}=0
\tag{1}
\]
force n_ts=0 and recognize the original sliced kernel as C^[3].
The hypothesis n_ts=0 in348 is therefore unnecessary. There is no
bound on n_ttt and no extra condition on the second potential ell.

This is a conditional result inside a supplied actual chart, not a
normalization theorem for an arbitrary cancellation candidate. Its
recognition conclusion retains348 and346's working dependencies.

## 1. Exact input and the normalized obstruction

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad A=\ker E,\quad a_0=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the entire initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad L=\operatorname{Frac}\ker_A N,
\quad [L:\mathbb C(t,s)]<\infty,\quad Na_0=Nt=Ns=0,\\
Nv=1,\quad K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\qquad
J_{t,s,v}(X)=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The coefficient partials extend uniquely from C(t,s) to L, commute,
fix v, and have joint constant field C. The literal coordinate map is
\[
Y=y+\sigma X+tX^2,\quad
Z=z+(2t\sigma+k)X+t^2X^2,\quad
W=w+\theta X+sX^2.
\tag{3}
\]
These are the literal expansions of the original polynomial coordinates
in the prescribed localized chart, not an arbitrary rational map with
a nonzero Jacobian.

First suppose k=s and n_ss=0. If n_ts were nonzero, the full
reduction in
[361](principal-paraboloid-moving-first-slope-affine-line-reduction-pass361-working.md)
would apply. It exhausts the nonlinear intrinsic-degree alternatives
and reduces to the two necessary coefficient families of353:

* B is a nonconstant complex affine polynomial in t.
* B is a complex constant plus a nonzero simple reciprocal pole.

Here n=B(t)s+f(t), initially with B,f in the exact finite field
ker_L partial_s, not in a prescribed rational-function ansatz.
The first family is impossible by
[360](principal-paraboloid-affine-moving-slope-family-exclusion-pass360-working.md);
the second is impossible by
[362](principal-paraboloid-reciprocal-moving-slope-exclusion-pass362-working.md).
Both proofs retain the complete scalar and use actual complex
polynomial automorphisms before changing coefficient-field parameters.
Every residual constant, including zero constants, is covered.

Consequently
\[
\boxed{\text{Under(2),}\quad k=s,\ n_{ss}=0
\quad\Longrightarrow\quad n_{ts}=0.}
\tag{4}
\]
This is the new obstruction. The affine-line conclusion of361 alone
would not prove it; both final family exclusions are necessary.

## 2. Actual normalization with arbitrary first potential

Now assume(1) and put m=k_s in C*. Both coefficient partials kill
k_tt, so k_tt=gamma belongs to C. Exact subtraction gives
\[
k=ms+\frac\gamma2t^2+bt+d,\qquad
m\in\mathbb C^*,\quad\gamma,b,d\in\mathbb C.
\tag{5}
\]
No integration of n has been used. Define the actual polynomial map
\[
X_1=X,\quad Y_1=Y,\quad Z_1=Z,\quad
W_1=mW+\frac\gamma2Z+bY+dX^2.
\tag{6}
\]
Its inverse fixes X,Y,Z and is
\[
W=\frac{W_1-\gamma Z/2-bY-dX^2}{m}.
\tag{7}
\]
The only denominator is a nonzero complex constant. As in the
arbitrary-n computation of
[302, Section3](principal-paraboloid-reducible-surface-conic-reduction-pass302-working.md),
direct full substitution gives
\[
\begin{aligned}
t_1&=t,&s_1&=k,&k_1&=s_1,\\
y_1&=y,&\sigma_1&=\sigma,&z_1&=z,\\
\theta_1&=m\theta+k_t\sigma+\gamma k/2,
&w_1&=mw+\gamma z/2+by,\\
n_1&=n-\gamma k/2,
&\ell_1&=\ell+\gamma n/2+(\gamma k/2)(n_s/m-\gamma/2).
\end{aligned}
\tag{8}
\]
For completeness, the old second potential is
mw+(2sigma+k_t)y+gamma sigma^2/2+n_t sigma+n_s theta=ell.
Substituting(8) into
w1+2sigma1 y1+(n1)_t1 sigma1+(n1)_s1 theta1
cancels its sigma and theta coefficients and gives ell1 exactly.
This uses no reducibility assumption from302. Only its literal
normalization, now justified directly from(5), is being applied.

The new coefficient partials on L are
\[
\partial_{s_1}=m^{-1}\partial_s,\qquad
\partial_{t_1}=\partial_t-(k_t/m)\partial_s.
\tag{9}
\]
Therefore
\[
\begin{aligned}
(n_1)_{s_1}&=n_s/m-\gamma/2,\\
(n_1)_{s_1s_1}&=n_{ss}/m^2=0,\\
(n_1)_{t_1s_1}&=n_{ts}/m-k_t n_{ss}/m^2=n_{ts}/m.
\end{aligned}
\tag{10}
\]
The last equality uses the stated n_ss=0; it is not valid for
arbitrary n. Holding the old s fixed would give the wrong transport.

## 3. All actual entry conditions survive

The invertible weighted leading transformation in(6) fixes X,Y,Z
and hence fixes the entire ideal X^2Z-Y^2. The new leading ratio
s1=k is algebraically independent of t because m is nonzero. Thus the four exact
E-degrees remain(1,2,2,2), and EX1=a0.

The literal new selected partial is
\[
\partial_{Z_1}=\partial_Z-\frac\gamma{2m}\partial_W.
\tag{11}
\]
The old W-partial has horizontal shift at most three, since its
omitted leading triple X,Y,Z is dependent. The original Z-partial
has exact shift four. Hence its leading N, constant field L, whole
line O and Nv=1 are unchanged. This uses264's retained occurring-pivot
input, not a supposition about a different auxiliary derivation.

Equation(8) is invertible affine over L in y,sigma,theta, so it
preserves their whole O-return. The stronger complex intercept field
return is rebuilt separately from the actual ring:
\[
\mathcal B_{a_0}=A_{a_0}[X_1].
\tag{12}
\]
Evaluation at X1=0 in the actual polynomial frame gives K=C(y1,z1,w1)
and, on localizing by the N-constants, L[y1,z1,w1]=O, exactly as in264.
An invertible change over L alone would not justify the first equality.

At fixed X the bad-slot row determinant in(6) equals m; the
coefficient determinant from (t,s) to (t1,s1) also equals m. They
cancel in the chain rule, retaining
\[
J_{t_1,s_1,v}(X_1)=-a_0^4.
\tag{13}
\]
Thus(4) legitimately applies to the new chart. By(10) it yields
(n1)_t1s1=0, hence n_ts=0 in the original chart as well.

## 4. Recognition and the exact remaining frontier

The original chart now satisfies all the coefficient hypotheses of
[348](principal-paraboloid-constant-coupling-general-first-normalization-pass348-working.md).
Its actual two-stage normalization and retained one-variable theorem346
give
\[
\boxed{\text{Under every actual hypothesis(2),}\quad
k_s\in\mathbb C^*,\quad k_{ttt}=0,\quad n_{ss}=0
\quad\Longrightarrow\quad n_{ts}=0,\quad A\cong\mathbb C^{[3]}.}
\tag{14}
\]
No new restriction on ell or n_ttt has entered the argument.
When k=s, this says that an arbitrary affine-in-s first potential
has constant s-slope, and the original kernel is recognized.

This does not show n_ss=0 for a general first potential. It does not
make variable k_s constant, remove k_ttt, change other full initial
ideals to this one, or place an arbitrary sliced polynomial four-ring
in an exact1222 frame. Each is outside the present implication.
In particular the actual cancellation conjecture remains unsolved.

## 5. Verification status

Root completely read264,302,346,348,360,361 and362 before composing
this note. Earlier complete reads and separate reviews of361's direct
inputs are recorded in the ledger. The only additional mathematical
composition here is(4), the explicitly transported derivatives(10),
and the application of348; its retained recognition dependencies have
not been recursively formalized by this note.

Separate saved-source review and finite-checker outcomes are recorded
in the ledger only when they occur. Exact algebra checks do not certify
all field, polynomial-return or inherited recognition statements.
No human expert review, proof-assistant certification, historical
novelty, public submission or general cancellation solution is claimed.
