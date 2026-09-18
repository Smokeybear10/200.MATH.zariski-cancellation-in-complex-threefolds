# Actual normalization of complex quadratic coefficient data

Working result: the explicit polynomial map of302 and the exact transport
of332 compose without a surface-factorization assumption. This recognizes
a larger coefficient family through the retained working theorem330 and
isolates a nonzero quadratic residual in the other cases. It does not
normalize arbitrary principal charts or solve cancellation.

## 1. Retained hypotheses and the coefficient family

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
the full initial ideal, selected shift-four derivation, both field and
whole-ring returns, and calibrated scalar determinant. Write the kernel
as A0, its actual polynomial extension as B=A0[u]=C[X,Y,Z,W], and
E=partial_u. The actual E-degree profile is1222. In particular

\[
\begin{gathered}
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
a_0=EX\ne0,\quad N=[u^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=\operatorname{Frac}A_0=\mathbb C(y,z,w)=L(v),\qquad
L[y,z,w]=L[y,\sigma,\theta]=O,\qquad J=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]

The exact coefficient partials commute, fix v, and have joint constant
field C. Assume the following identities in that exact field L:

\[
\begin{aligned}
k&=m_0s+\frac{\kappa}{2}t^2+bt+d,\qquad m_0\in\mathbb C^*,\qquad
\kappa,b,d\in\mathbb C,\\
n&=(B+\kappa/2)k+Dt^2+At+C,\qquad A,B,C,D\in\mathbb C,\\
\Delta&=D-B^2.
\end{aligned}
\tag{2}
\]

Here capital A,B,C in formulas are scalar coefficients, not rings.
No condition on ell or on reducibility of the third potential is imposed.
All divisions by these constants below are explicitly restricted to
nonzero constants.

## 2. The combined polynomial map and its inverse

First use the actual302 reframe
\(W_1=m_0W+\kappa Z/2+bY+dX^2\), fixing X,Y,Z. Its literal formulas are

\[
\begin{aligned}
s_1&=k,&k_1&=s_1,&
\theta_1&=m_0\theta+(\kappa t+b)\sigma+\kappa k/2,\\
n_1&=n-\kappa k/2=Bs_1+Dt^2+At+C,\\
\ell_1&=\ell+\kappa n/2+\kappa Bk/2.
\end{aligned}
\tag{3}
\]

The calculation in302 Section3 uses only the displayed complex
coefficients of k and the literal first two potentials. The earlier
reducibility argument in that note was one way of obtaining such k;
reducibility is not required for the polynomial map or its transport.
Here (2) supplies the coefficient hypothesis directly.

Now apply332 to the first frame. The composite is

\[
\boxed{
X_*=X+B,\qquad Y_*=Y+A/2,\qquad Z_*=Z-C,\qquad
W_*=m_0W+(\kappa/2+2B)Z+bY+dX^2.}
\tag{4}
\]

Its inverse, as polynomial expressions in the starred coordinates, is

\[
\begin{aligned}
X&=X_*-B,&Y&=Y_*-A/2,&Z&=Z_*+C,\\
W&=\frac{W_*-(\kappa/2+2B)(Z_*+C)
                 -b(Y_*-A/2)-d(X_*-B)^2}{m_0}.
\end{aligned}
\tag{5}
\]

These are actual maps over C, not maps with moving coefficients in L.
The resulting leading ratios and potentials are

\[
\boxed{
\begin{aligned}
t_*&=t,&s_*&=k+2Bt^2,&k_*&=s_*,&n_*&=\Delta t^2,\\
\ell_*&=\ell_1+B^2k+2BC-2B\Delta t^2.
\end{aligned}}
\tag{6}
\]

Every expression on the right is initially in the old L. The new exact
partials are

\[
\partial_{s,*}=m_0^{-1}\partial_s,\qquad
\partial_{t,*}=\partial_t-
       \frac{(\kappa+4B)t+b}{m_0}\partial_s.
\tag{7}
\]

In particular \((n_*)_{s,*}=0\) and \((n_*)_{t,*}=2\Delta t\).
Equations (3),(6) retain all of ell, not only its leading terms.

## 3. Why the entire actual chart survives

The leading map of (4) fixes X,Y,Z and makes the invertible weighted
change
\(W\mapsto m_0W+(\kappa/2+2B)Z+bY+dX^2\). It fixes the full
principal initial ideal, which is independent of W. Since m0 is
nonzero, t and s* remain independent and the new W leader does not
vanish. Thus all four E-degrees remain1222 and \(EX_*=a_0\).

The new literal partial is

\[
\partial_{Z_*}=\partial_Z-
                  \frac{\kappa/2+2B}{m_0}\partial_W.
\tag{8}
\]

The old W-partial has shift at most three by the actual omitted-triple
gate of264, as used in302 and332. Hence (8) has exactly the old
shift-four leading derivation N. L, O and the chosen normalization
Nv=1 are unchanged.

Both stages have invertible affine maps over L on the three intrinsic
generators. For the stronger return over C, reapply the actual quotient:
\(B_{a_0}=(A_0)_{a_0}[X_*]\). Evaluation at X*=0 in the actual
starred polynomial frame gives

\[
K=\mathbb C(y_*,z_*,w_*),\qquad
L[y_*,z_*,w_*]=O.
\tag{9}
\]

This is the actual264 quotient argument. The equality over C is not
deduced from invertibility over the larger coefficient field.
Finally the fixed-X row map has determinant m0, while the coefficient
change (t,s) to (t,s*) has determinant m0 and therefore contributes
the inverse factor in the horizontal Jacobian. Translation of X is
by the complex constant B. The calibrated determinant remains
\(J_*(X_*)=J(X_*-B)=-a_0^4\).

## 4. Recognition and the nonzero residual

If Delta=0, the starred frame has precisely k*=s*, n*=0. The retained
working result
[330](principal-paraboloid-normalized-potential-family-recognition-pass330-working.md),
including298 and mandatory-corrected301, applies. Thus

\[
\boxed{\text{Under (1),(2),}\quad D=B^2\quad\Longrightarrow\quad
A_0\cong\mathbb C^{[3]}.}
\tag{10}
\]

For Delta nonzero,332 gives a further actual polynomial frame1123.
It also recognizes the case in which the linear coefficient of its
new degree-one coordinate is complex. The exact coefficient in the
fully normalized frame satisfies

\[
\ell_*+\Delta s_*=\ell_1+Dk+2BC.
\tag{11}
\]

Consequently a second sufficient condition is

\[
\boxed{\Delta\ne0,\quad
\ell+\kappa n/2+(D+\kappa B/2)k\in\mathbb C
\quad\Longrightarrow\quad A_0\cong\mathbb C^{[3]}.}
\tag{12}
\]

This uses332's actual invariant-coordinate endpoint. Otherwise the
remaining residual is the nonzero complex multiple Delta*t squared.
The frame1123 transfer has total degree sum seven, just like1222;
it is not a strict descent proof or a general recognition theorem.
Neither the line frontier nor the quadratic primitive of
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md)
is silently declared an original-coordinate endpoint here.

## 5. A derivative-only test for this coefficient family

The input (2), with arbitrary complex D, is equivalently specified by

\[
k_s=m_0\in\mathbb C^*,\qquad k_{ttt}=0,\qquad
n_{ss}=n_{ts}=n_{ttt}=0.
\tag{13}
\]

Here is the exact-field integration, with no rationality assumption.
Since both partials kill ktt, it is a complex constant kappa.
Subtract kappa*t squared/2 and m0*s from k. Its t-derivative is a
joint constant b; subtract bt and the remainder is a joint constant d.
Likewise ns is a joint constant nu, and ntt is a joint constant rho.
Put

\[
c=\nu/m_0,\qquad B=c-\kappa/2,\qquad
D=(\rho-c\kappa)/2.
\tag{14}
\]

The expression n-c*k-D*t squared has both s-derivative and second
t-derivative zero. Its t-derivative is a joint constant A, and the
remaining constant is C. This proves (2). Conversely direct
differentiation of (2) gives (13).

Under (13), the residual is therefore the complex scalar

\[
\boxed{\Delta=\frac{n_{tt}}2-
\left(\frac{n_s}{m_0}\right)^2+
\frac{\kappa n_s}{2m_0}-\frac{\kappa^2}{4}.}
\tag{15}
\]

This is an invariant of the specified normalization procedure and332's
translation/shear family, not a proved invariant of all polynomial
automorphisms. Conditions (13) have not been proved for arbitrary
actual charts. A nonzero value of (15) does not obstruct cancellation;
it only records the term this map leaves behind.

## 6. Verification status

Root read the complete sources264 and302 in5bdbec,330 and the formula
version of332 in61d9b0, and333 in3faacf before this composition.
The proof is the displayed actual map, its coefficient transport, and
the explicitly retained recognition inputs. This is a conditional
working corollary with new parameter coverage, not an independently
certified proof of all those inputs. Independent saved-source review
and any new finite identity checks must be recorded separately in the
ledger. No earlier checker was executed, imported, compiled or rerun.
No general normalization, human expert review, novelty clearance, or
unrestricted cancellation conclusion is claimed.

