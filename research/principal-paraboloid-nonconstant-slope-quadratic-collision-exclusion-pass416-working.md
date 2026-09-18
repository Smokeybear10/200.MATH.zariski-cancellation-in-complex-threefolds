# A quadratic collision excludes the nonconstant-slope nonexceptional case

Working exclusion under every actual264 hypothesis, with k=s and
n_ss nonzero. In the nonexceptional degree profile (r,m,d)=(0,1,2)
of407, a noncomplex leading y/sigma slope is impossible. The
argument uses the actual polynomial ring after adjoining L, not
just the intercept field or a nonzero Jacobian.

The collision lemma also records a necessary condition for the
exceptional quadratic case. It does not exclude that case by itself.
No polynomial parameter over L is declared an original coordinate.

## 1. The actual all-X polynomial return

Retain the complete actual chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the equal-degree frontier of407 and the leading coefficient
constraints of413. Write the original polynomial ring as
\[
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u],\qquad E=\partial_u,
\quad a_0=EX\ne0,
\]
with the full initial kernel and time degrees prescribed by264.
Its selected derivation gives
\[
L=\operatorname{Frac}\ker_{A_0}N,\qquad
L[A_0]=A_0\otimes_{\ker N}L=O=L[v],\quad a_0\in L^*.
\tag{1}
\]
Because X has time degree one, X=a0*u+bX with bX in A0.
Therefore the actual localization equality is
\[
\boxed{L[\mathcal B]=L[A_0][u]=L[v][u]=L[X,v].}
\tag{2}
\]
This is stronger than a statement about the X=0 intercepts.
If h is an affine intrinsic parameter, then O=L[h] and (2) says
\[
L[X,Y,Z,W]=L[X,h].
\tag{3}
\]
After extending L to its algebraic closure and setting X=x0 for
any x0 in that closure, the three specialized polynomials Y,Z,W
must generate the entire polynomial ring in h.

Two distinct h values therefore cannot have all three polynomial
values equal. Nor can all three h derivatives vanish at one point:
differentiating a polynomial expression for h in the three generators
would give 1=0 there. These are obstructions to an actual polynomial
identity, not applications of a generic injectivity or Jacobian criterion.

## 2. A full quadratic divided-difference lemma

Suppose, over the retained coefficient field, that
\[
\begin{gathered}
p=\sigma=p_2h^2+p_1h+p_0,\quad p_2\ne0,\\
y=\lambda p+a h+b,\qquad\theta=\mu p+h,\qquad
\delta=\lambda-\nu,\quad\nu=n_s,\quad g=2b+n_t.
\end{gathered}
\tag{4}
\]
The symbol a is the lower y-slope, not the original a0.
The complete literal rows are
\[
\begin{aligned}
Y&=(X+\lambda)p+a h+b+tX^2,\\
Z&=p^2+(2t\lambda+\mu+2tX)p+2t(ah+b)+h+n+sX+t^2X^2,\\
W&=-2\lambda p^2+(\mu X-g-\nu\mu)p-2ahp
                                      +(X-\nu)h+\ell+sX^2.
\end{aligned}
\tag{5}
\]
Here n_t means the original fixed-s coefficient derivative.

For two parameter values h1,h2 write
\[
S=h_1+h_2,\qquad L_S=p_2S+p_1,\qquad
P_\Sigma=p(h_1)+p(h_2).
\tag{6}
\]
Every divided difference below is first a polynomial identity,
so it also has a diagonal value equal to the derivative.
The complete formulas are
\[
\begin{aligned}
\Delta Y&=(X+\lambda)L_S+a,\\
\Delta Z&=(P_\Sigma+2t\lambda+\mu+2tX)L_S+2ta+1,\\
\Delta W&=[-2\lambda P_\Sigma+\mu X-g-\nu\mu-aS]L_S
                                -aP_\Sigma+X-\nu.
\end{aligned}
\tag{7}
\]
For the last identity, the divided difference of h*p(h) is
(S*LS+Psum)/2. Thus the lower cubic term in W has been retained.

If LS is nonzero, the first two differences vanish for
\[
X=-\lambda-a/L_S,\qquad P_\Sigma=-\mu-1/L_S.
\tag{8}
\]
After these substitutions the third difference is exactly
\[
\Delta W=-F(S),\qquad
F(S)=(p_2S+p_1)(aS+g-\delta\mu)-\delta.
\tag{9}
\]

Any root S of F with LS nonzero obstructs (3). Choose Psum from
(8), and set
\[
H=\frac{p_2S^2+p_1S+2p_0-P_\Sigma}{2p_2}.
\tag{10}
\]
Let h1,h2 be the roots of z^2-Sz+H over the algebraic closure.
Their sum and product give exactly the prescribed Psum.
If distinct, (7)--(9) give a collision. If equal, the common
value has all three derivatives zero, by the diagonal polynomial
identities in (7). Section1 excludes both. No division by h1-h2
is used after choosing the diagonal case.

If delta and a are nonzero, F has degree two, with leading
coefficient p2*a. Every root has LS nonzero because F at LS=0
equals -delta. If a=0 but g-delta*mu is nonzero, F is instead
nonconstant linear and the same argument applies. Therefore
\[
\boxed{\delta\ne0\quad\Longrightarrow\quad
a=0,\qquad g=\delta\mu}
\tag{11}
\]
is necessary for (3), not sufficient.

There is also a useful exceptional boundary. If delta=0 and a
is nonzero, use the root S=-g/a of the second factor of F.
To avoid an LS-nonzero root it must have LS=0. Thus
\[
\boxed{\delta=0,\ a\ne0\quad\Longrightarrow\quad p_2g=a p_1.}
\tag{12}
\]
This statement does not divide by delta.

## 3. Applying the lemma to the nonexceptional quadratic profile

Assume the complete actual hypotheses with
\[
d=2,\qquad\lambda\notin\mathbb C,\qquad
(\delta,\beta)\ne(0,0),\quad\beta=n_{ts}+n_{ss}\mu.
\tag{13}
\]
The high equations412 imply delta=0 would force beta=0, as proved
in413, Section2. Hence delta is nonzero. By407 the quadratic profile
has m=1,r=0. Put rlow=y-lambda*sigma and h=theta-mu*sigma.
The complete evaluated linear coefficient
\[
2\delta\,r_{\rm low}+\beta h+j
\tag{14}
\]
is a coefficient constant. If h were constant, (14) and delta
nonzero would make rlow constant, contrary to m=1. Thus h is
affine intrinsic, O=L[h], and rlow=a*h+b with
\[
2\delta a+\beta=0.
\tag{15}
\]
Sigma is quadratic in h. The all-X collision lemma applies, so
(11) gives a=0 and then (15) gives beta=0.

This contradicts the noncomplex-slope coefficient family of413.
Put xi=lambda, use dot=Dscript and prime at fixed t, and let
F=ker(dot). That family gives
\[
\begin{gathered}
\mu=\zeta-4\xi t,\quad
s=-2\xi t^2+\zeta t+S_0,\quad
n=-\xi^2t^2+At+B,\qquad\zeta,S_0,A,B\in F,\\
D=s'=-2t^2+\zeta't+S_0'\ne0,\qquad
\nu=\frac{-2\xi t^2+A't+B'}D,\\
\delta=\frac{(\xi\zeta'-A')t+\xi S_0'-B'}D.
\end{gathered}
\tag{16}
\]
Primes preserve F. Since dot(xi)=0,
beta=dot(nu)=-dot(delta). If beta=0, delta belongs to F.
Multiplying (16) by D would then give a polynomial identity in t
over F with quadratic coefficient -2delta on the left and degree
at most one on the right. The element t is transcendental over F,
since dot(t)=1 and differentiation of a separable algebraic relation
over F would contradict that. Thus delta=0, impossible. We conclude
\[
\boxed{\text{The supplied nonexceptional }d=2\text{ chart
cannot have a noncomplex leading slope }\lambda.}
\tag{17}
\]
No higher-degree remainder was treated as a coefficient constant.

## 4. Verification and limits

Root read the complete direct actual264 source through EOF in20ad23.
Its Eq4 and the original global slice license (1)--(3).
The retained inputs407/413 and canonical state were revalidated
in c8588b. The writing guide was fully read in2ee263 before drafting.

Fresh unsaved ec686a rebuilt all three divided differences from
the original full rows, the residual after (8), and simultaneous
vanishing of the three derivatives at a repeated-root control.
All residuals were zero. It also checked the final -2delta
coefficient. The all-X localization, algebraic-root argument and
constant-field transcendence are separate written proofs.

Jet independently read264 in a908a7 and checked the alternative
all-X argument325 in a63e86. Its fresh33d08b independently
reconstructed all differences, the prescribed product and diagonal
derivatives. The outline audit found no missing zero case.
Full saved-source review is still required.

An earlier exploratory scalar expansion be5bf1, completed on its
original process29220 inee066b, was not needed for this proof.
It was fresh and unsaved; no accepted claim depends on a still-
running computation.

This does not exclude complex leading lambda, the exceptional
delta=beta=0 quadratic branch, or any d>=3 case. It does not prove
arbitrary-chart entry, general coupling, original-ring recognition,
unrestricted cancellation, novelty, human-expert review or formal
certification. No saved checker was executed, imported, compiled
or rerun, and no earlier source or canonical index was changed.

