# Exclusion of the zero leading gate in the quadratic-cubic profile

Working result: the E=0 alternative of372 is impossible under its
complete actual chart hypotheses. The proof uses the genuine lower
fourth-potential equations and one coefficient of the literal scalar
Jacobian. It does not assume that either exact coefficient field is
rational. A rational expression for one auxiliary coefficient is
derived, and only that coefficient is subsequently shown to be a
polynomial.

The E nonzero alternative of372 is not treated. No earlier source,
checker, index, or ledger is changed, and no ambient coordinate or
kernel recognition is inferred from a coefficient-field reframe.

## 1. Exact retained entry and the exceptional family

Retain all the actual hypotheses of the fully read
[372](principal-paraboloid-quadratic-cubic-leading-coefficient-gates-pass372-working.md),
including its direct365/369 inputs. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E_{\rm slice}=\partial_u,
\qquad \deg_{E_{\rm slice}}(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},
\qquad a_0=E_{\rm slice}X\ne0,\\
N=[u^4]\partial_Z|_{A_0},\qquad L=\operatorname{Frac}\ker_{A_0}N,
\qquad [L:\mathbb C(t,s)]<\infty,\\
O=L[r]=L[y,\sigma,\theta]=L[y,z,w],\qquad
Nr=\rho\in L^*,\qquad L(r)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
Here r is the degree-one intrinsic remainder of372. It is not an
original coordinate. The exact commuting coefficient partials on L
have joint constants C. Write F=ker_L partial_s, finite over C(t),
with t-derivative constants C. In particular s is transcendental
over F. Neither F=C(t) nor L=F(s) is assumed.

The actual normalization369 and the E=0 conclusions of372 give
\[
\begin{aligned}
g&=\frac c{t^3},\qquad
n=-\frac{s^2}{4t^2}+\frac ct+c_1t+c_0,\\
\ell&=-\frac{s^3}{4t^4}+\frac{cs}{t^3}
       +\frac{(c_0-G_0)s}{2t^2}+l(t),\\
\sigma&=A r^2+B r+e,\qquad
A=\frac{2}{t l''+2l'}\in F^*,\qquad B,e\in L,
\end{aligned}
\tag{2}
\]
where c is a nonzero complex constant, c0,c1,G0 are complex,
and l belongs to the exact field F. Primes denote partial_t on F.
Uppercase B is the linear coefficient of sigma, not the eliminated
linear-in-s coefficient of n in369. No derivative of A or l is
assumed nonzero.

For completeness the third-level parametrization used below is
\[
\begin{gathered}
\nu=-\frac{s}{2t^2},\qquad
C=\ell_s+\frac{s^2}{4t^4},\qquad
\Lambda=\frac{2sC}{t}+\ell_t,\\
\theta=\frac tr\left\{g(\sigma^2-e^2)
       -\Lambda(\sigma-e)+\frac{2sr\sigma}{t^2}
       +r^2-2tCr\right\},\\
y=r-\frac{\theta}{2t}+\frac{s\sigma}{2t^2}
       -\frac{n_t}{2}-tC,\qquad
h=t^2C^2-\Lambda e+g e^2+\nu\ell-\frac{n_t^2}{4}.
\end{gathered}
\tag{3}
\]
The numerator defining theta is divisible by r. All expressions
in (3) are in L[r], including at r=0; there is no discarded fiber.

The literal intercepts, actual map and calibration are
\[
\begin{aligned}
z&=2ty+\sigma^2+\theta+n,\qquad
w=\ell-2\sigma y-n_t\sigma-n_s\theta,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s)X+t^2X^2,\\
W&=w+\theta X+sX^2,\qquad
J_{t,s,r}(X)=-a_0^4/\rho\in L^*.
\end{aligned}
\tag{4}
\]
The parameter change from the original intrinsic v to r has
Jacobian rho, even when its coefficients move in t,s. Thus (4)
is the exact scalar, not an unspecified nonzero function of r.
All derivatives below hold the independent r fixed.

## 2. A full scalar coefficient makes B affine in s

Define one auxiliary element of L by
\[
q=cs+2ct e-t^4l',\qquad
e=\frac{q}{2ct}-\frac{s}{2t}+\frac{t^3l'}{2c}.
\tag{5}
\]
This q is not the fourth-potential level, which will be denoted q0.
No root, rationality, or nonvanishing condition on q is imposed yet.

Take the literal determinant at X=0,
J0=det partial(y,z,w)/partial(t,s,r). Substituting (2),(3),(5),
then using l''=2/(tA)-2l'/t, gives the exact coefficient
\[
[r^5]J_0=
\frac{A}{t^3}\left(3cA B_s+2t^2 A'-6tA\right).
\tag{6}
\]
It is computed by differentiating the complete intercepts in (4),
not by treating a moving level or a root as fixed. One useful
independent simplification in this expansion is
\[
z=\left(\sigma+\frac{s}{2t}\right)^2+2tr+G_0,
\tag{7}
\]
but the w row still comes from its full literal potential in (4).
Equation (6) has no q-dependent remainder.

The calibrated scalar has no positive r powers. Dividing (6)
only by c,A,t, which are nonzero, proves
\[
B_s=\frac{2t}{c}-\frac{2t^2A'}{3cA}=:\beta_1\in F,
\qquad B=\beta_1s+\beta_0,\quad\beta_0\in F.
\tag{8}
\]
The last assertion follows by subtracting beta1*s and using the
exact constant field of partial_s. It does not identify L with F(s).

## 3. The three lower fourth-potential equations

We use the full primitive365(7), not an arbitrary cubic through
the intrinsic line. With independent formal variables U,P,V it is
\[
\begin{aligned}
Q={}&[(n_{tt}+2\ell_s)P+n_{ts}V-2n_{ts}P^2
            -2n_{ss}PV-\ell_t]U\\
&+\frac{n_{ttt}}6P^3+\frac{n_{tts}}2P^2V
 +\frac{n_{tss}}2PV^2+\frac{n_{sss}}6V^3\\
&-\frac{\ell_{tt}+2n_{ts}n_t}{2}P^2
 -(\ell_{ts}+n_sn_{ts}+n_{ss}n_t)PV
 -\frac{\ell_{ss}+2n_sn_{ss}}{2}V^2\\
&+(n_{ts}\ell+n_t\ell_s-h_t)P
 +(n_{ss}\ell+n_s\ell_s-h_s)V,
\qquad Q(y,\sigma,\theta)=q_0\in L.
\end{aligned}
\tag{9}
\]
The derivatives h_t,h_s use the full h in (3), including the
moving coefficient e. Substitute (2),(3),(5) into (9), retaining
q_t,q_s, and use the already proved relation for l''. The three
remaining positive coefficients used here are
\[
\begin{aligned}
[r^3]Q&=-\frac{N_3}{2t^7},\qquad
N_3=-4ct^4A+2t^6B+A^2q q_s,\\
[r^2]Q&=\frac{N_2}{2ct^7A},\qquad
[r]Q=-\frac{qN_1}{2ct^8A},
\end{aligned}
\tag{10}
\]
where the exact numerators are
\[
\begin{aligned}
N_2={}&4c^2t^4AB+cst^5A-2ct^6B^2
 -2cA^2Bq q_s-2stA^2q q_s\\
&+t^9A l'-t^5Aq-t^2A^2q q_t+2tA^2q^2,\\
N_1={}&-2ct^4A+ctAB^2q_s+2st^2ABq_s+2t^6B
 +t^4Aq_s\\
&+t^3ABq_t-2t^2ABq+A^2q q_s.
\end{aligned}
\tag{11}
\]
These are polynomial expansions in the intrinsic r; coefficient
partials occur only inside L. In particular no derivative of q is
dropped when its relation to e is substituted.

First q is nonzero. Otherwise q_s=q_t=0. The equation N3=0
would give B=2cA/t^2. Substitution in N2 then gives
N2=A t^5(cs+t^4l'), nonzero since its s coefficient is Ac t^5.
This contradicts (10). We may consequently divide by q.

All of N3,N2,N1 vanish. Solving the first two equations for q_s
and q_t gives
\[
\begin{aligned}
q_s&=\frac{4ct^4A-2t^6B}{A^2q},\\
q_t&=\frac{2A^2q^2-4ABc^2t^3-7Acs t^4+A l't^8
              -Aqt^4+2B^2ct^5+4Bs t^6}{A^2qt}.
\end{aligned}
\tag{12}
\]
Substitution in N1 and clearing the already nonzero denominators
is precisely the identity
\[
\boxed{K(Aq+2t^4)=ABt^2(cs+t^4l'),\qquad K=t^2B-2cA.}
\tag{13}
\]
If K were zero, B=2cA/t^2 would be nonzero and (13) would force
cs+t^4l'=0, impossible over F. Thus K is nonzero.

## 4. Only the auxiliary coefficient becomes polynomial

By (8), B and K belong to F[s], of degree at most one. Equation
(13), with K nonzero, therefore gives q in F(s). Meanwhile N3=0
and (8) give
\[
\partial_s(q^2)=\frac{8ct^4}{A}-\frac{4t^6B}{A^2}\in F[s]_{\le1}.
\tag{14}
\]
Subtract its explicit polynomial primitive in F[s]. The difference
belongs to ker_L partial_s=F. Hence q^2 is in F[s], of degree at
most two.

This does not exclude a quadratic field extension by assumption.
Rather, (13) has already put this particular q in F(s). Write it
as a reduced fraction p1/p2 with p1,p2 in F[s]. If q^2 is a
polynomial, p2^2 divides p1^2; coprimality makes p2 a unit.
Consequently
\[
q\in F[s],\qquad \deg_s q\le1.
\tag{15}
\]
No assertion about the other elements of L or rationality of F
has been made.

Suppose first that beta1=0 in (8), so B belongs to F. Since
q q_s belongs to F by N3=0, writing q=q1*s+q2 in (15) gives
q1^2=0, hence q_s=0. The left side of (13) now belongs to F;
its right side has s coefficient ABt^2c. Thus B=0. But N3=0
then gives 4ct^4A=0, a contradiction. Therefore beta1 is nonzero.

When beta1 is nonzero, the coefficient of s^2 in (13) is
A t^2 beta1 times the slope of q on the left, and
A t^2 beta1*c on the right. Hence
\[
q=cs+v,\qquad v\in F.
\tag{16}
\]
In particular q is transcendental over F. Substituting q_s=c
in N3=0 now determines
\[
B=\frac{2cA}{t^2}-\frac{A^2c q}{2t^6}.
\tag{17}
\]
Finally replace B by (17) and s by (q-v)/c in (13). Its left
side minus its right side is exactly
\[
2A^2c(v-t^4l')
 +q\left\{\frac{A^3c}{2}\left(l'-\frac v{t^4}\right)
                      -3A^2c\right\}=0.
\tag{18}
\]
Because q is transcendental over F, its constant coefficient gives
v=t^4l'. The coefficient of q is then -3A^2c, which is nonzero
in characteristic zero. This is the required contradiction.

## 5. Scope and verification record

Thus the entire E=0 alternative of372 is excluded. The proof
retains all complex integration constants and allows arbitrary
finite exact fields F and L until the identities force the single
element q into F[s]. It divides neither by A', l', nor beta1 before
the beta1=0 case has been separately contradicted.

The E nonzero alternative of372, other remaining nonlinear
profiles, arbitrary actual-chart entry, and the unrestricted
cancellation problem are not settled here. No polynomial-kernel
claim or coefficient-field-to-ambient promotion is made.

The complete372 source was read through EOF in0998d4. Its exact
held hash and complete365/369 sources were read inb3bc1b. Fresh
unsaved algebra fa3b19 independently rebuilt the full raw fourth
polynomial and verified both generic high gates of372, its E=0
fourth coefficient, and the full Z identity. The complete lower
coefficient expansion (10),(11) was reconstructed in7cc028;
separate algebra d9ed7a verified the elimination (12),(13), and
347f01 verified the final identity (18). A separate literal
intercept determinant reconstruction ba20be verified (6).

These finite exact identities supplement the written algebraic
arguments. No saved checker was executed, imported, compiled or
rerun by this author. No novelty, human-expert verification, or
proof-assistant certification is claimed.
