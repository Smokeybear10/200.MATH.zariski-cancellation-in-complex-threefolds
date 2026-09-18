# The invariant contact branch is incompatible with the full scalar

Working result: under the full actual affine projected-line hypotheses of474,
retain the nonzero-direction contact reduction of482. If lambda, omega and
the contact parameter tau are noncomplex, and
\(\mathcal D\tau=0\), the original calibrated scalar cannot be nonzero.
Thus the necessary coefficient family of484 has no realization in this
actual branch. This note does not treat constant tau or
\(\mathcal D\tau\ne0\), and makes no general recognition claim.

## 1. Actual hypotheses and the exact input from484

Retain the full actual264 entry, the genuine296 levels and their evaluated
minor units, and the nonconstant-sigma birational projected-line hypothesis
of325, as stated in
[474](principal-paraboloid-variable-coupling-affine-line-high-gates-pass474-working.md).
In particular the original polynomial four-ring and original global slice
remain in place, with the full initial kernel, literal selected partial,
both original-ring returns and calibrated scalar. Write
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=A[u_{\rm glob}],\qquad E u_{\rm glob}=1,
\qquad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
[L:\mathbb C(t,s)]<\infty,\qquad m=k_s\notin\mathbb C,\\
P=\sigma,\qquad O=L[P],\qquad NP=\rho\in L^*,\\
y=\lambda P+r_{\rm old},\qquad\theta=\mu P+h,
\qquad w_{\rm int}=\omega P^2+w_1P+w_0,\\
J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{1}
\]
Here the J notation always means the determinant of the three literal
rows Y,Z,W with respect to the listed parameters, at fixed X. The coefficient
partials commute, with joint constants exactly \(\mathbb C\). Neither P
nor any coefficient parameter below is promoted to an ambient coordinate.
The intercept \(x_0\) is not set to zero, and a0 is not assumed to be a unit
of the original polynomial ring.

Let \(\mathcal D=\partial_t+\mu\partial_s\), and let
\(\beta=\mathcal Dm\ne0\). The contact notation of the fully read
[482](principal-paraboloid-nonzero-direction-contact-reduction-pass482-working.md)
is
\[
a_{\rm ct}=\beta/B_2,\qquad \tau=t+a_{\rm ct},\qquad
\mathcal H=\beta a_{\rm ct}-m,
\qquad 2d\lambda=\mathcal H\,d\omega.
\tag{2}
\]
In addition to \(\lambda,\omega\notin\mathbb C\), assume throughout
\(\tau\notin\mathbb C\) and \(\mathcal D\tau=0\).
The complete
[484](principal-paraboloid-invariant-contact-parameter-reduction-pass484-working.md)
was read at SHA
`9c7ef1c4a7971fc668a1b4627d7c9a19d6474242596c11bdb368facae567dc5e`.
It proves that \((t,\omega)\) is a separating coefficient basis and that
\[
F=\ker_L\mathcal D
\quad\hbox{is finite over }\mathbb C(\omega).
\tag{3}
\]
In Sections2--5 a dot means \(\mathcal D=\partial_t|_\omega\), and a
prime on F means \(\partial_\omega\). Its constants in F are exactly
\(\mathbb C\). Put \(u=-2\lambda'\in F^*\); this u is an effective
coupling, not the global slice or the actual m. There are elements
\(M,\chi,A_1,\phi,\tau\in F\) such that
\[
\begin{gathered}
s=\omega t^2+Mt+\chi,\qquad \mu=2\omega t+M,
\qquad k=-2\lambda t^2+A_1t+\phi,\\
\lambda'=-u/2,\qquad \tau'\ne0,\qquad
\gamma:=A_1'-uM'\in F^*,\\
A_1'=uM'+\gamma,\qquad
\chi'=-\tau(\tau+M'),\qquad
\phi'=(\gamma-u\tau)(\tau+M'),\\
m=u-\frac{\gamma}{\tau-t},\qquad
\beta=-\frac{\gamma}{(\tau-t)^2},\qquad
s_\omega=(t-\tau)(t+\tau+M')\ne0.
\end{gathered}
\tag{4}
\]
In particular \(\gamma\ne0\) is part of the exact input, not a generic
restriction. This is not the zero-direction family of481. No individual
derivative of M, chi or phi is assumed nonzero, and no rationality of F
or equality \(L=F(t)\) is assumed.

## 2. Centering the intrinsic parameter in the original rows

At fixed formal X set
\[
\begin{aligned}
\xi&=P+t(X-\lambda),& R&=r_{\rm old}+\lambda^2t,\\
G&=2tr_{\rm old}+mh+n+\lambda tA_1-\lambda^2t^2,
&b&=w_1+2\omega\lambda t,\\
c&=w_0+\lambda t w_1+\omega\lambda^2t^2,
&H&=h-tw_1+M\lambda t.
\end{aligned}
\tag{5}
\]
Substitution in the literal264 rows, without changing any original
coordinate, gives exactly
\[
\boxed{\begin{aligned}
Y&=(X+\lambda)\xi+R,\\
Z&=\xi^2+A_1\xi+G+\phi X,\\
W&=\omega\xi^2+(b+MX)\xi+c+HX+\chi X^2.
\end{aligned}}
\tag{6}
\]
The variables X and xi are algebraically independent over L: the original
slice makes X transcendental over the fraction field of A, and P is the
polynomial-line parameter over L. The replacement of P by xi has parameter
Jacobian one at fixed X. Since \(\omega_s\ne0\), the actual scalar is
\[
J_{t,\omega,\xi}=-\frac{a_0^4}{\rho\omega_s}\in L^*.
\tag{7}
\]
It must be independent of X and xi, but it need not be constant as a
function of coefficient parameters. The full derivative matrix of (6),
with columns \((t,\omega,\xi)\), is
\[
\begin{pmatrix}
\dot R&-u\xi/2+R_\omega&X+\lambda\\
\dot G&A_1'\xi+G_\omega+\phi'X&2\xi+A_1\\
\dot b\xi+\dot c+\dot H X&
\xi^2+(b_\omega+M'X)\xi+c_\omega+H_\omega X+\chi'X^2&
2\omega\xi+b+MX
\end{pmatrix}.
\tag{8}
\]
This retains all moving intercept derivatives. Its \(\xi^3\) coefficient
is \(-2\dot R-u\dot b\), so
\[
\dot b=-2\dot R/u,\qquad b=B-2R/u\quad\hbox{for some }B\in F.
\tag{9}
\]
The second statement is obtained by differentiating the existing element
\(b+2R/u\); no antiderivative has been adjoined.

## 3. The zero moving-intercept derivative is impossible

Suppose first that \(\dot R=0\). Then (9) gives \(\dot b=0\).
Expansion of (8), first at \(X\xi^2\) and then at \(\xi^2\), gives
\[
\dot H=\dot G/u,\qquad
\dot c=(\lambda+u\omega)\dot G/u.
\tag{10}
\]
The \(X^2\xi\) coefficient becomes
\[
M'\dot G-A_1'\dot H=-\gamma\dot G/u.
\tag{11}
\]
Because \(u\gamma\ne0\), this forces \(\dot G=0\), and (10) gives
\(\dot H=\dot c=0\). The entire first column of (8) then vanishes.
This contradicts (7). Thus \(\dot R\ne0\); no case with zero
\(\dot G\) was discarded in reaching this conclusion.

## 4. The exact R basis and the first scalar integrations

The nonzero Jacobian \(\dot R\) licenses the separating basis
\((R,\omega)\). Its first derivative is
\(\partial_R=\mathcal D/\dot R\), with constant field still F. Its
second derivative agrees on F with the prime already used in (4).
These exact extended partials commute, and their joint constants remain
\(\mathbb C\). In particular R is transcendental over F. The scalar is
now
\[
J:=J_{R,\omega,\xi}
       =-\frac{a_0^4}{\rho\omega_s\dot R}\in L^*.
\tag{12}
\]
Here and until Section6, an omega derivative on an element outside F is
taken at fixed R. After (9), the complete matrix becomes
\[
\begin{pmatrix}
1&-u\xi/2&X+\lambda\\
G_R&A_1'\xi+G_\omega+\phi'X&2\xi+A_1\\
-2\xi/u+c_R+H_RX&
\xi^2+(B'+2Ru'/u^2+M'X)\xi+c_\omega+H_\omega X+\chi'X^2&
2\omega\xi+B-2R/u+MX
\end{pmatrix}.
\tag{13}
\]
Its two \(\xi^2\) coefficients give
\[
\begin{aligned}
H_R&=G_R/u+2\gamma/u^2,\\
c_R&=\frac{\lambda+u\omega}{u}G_R
 +\frac{2A_1'(\lambda+u\omega)}{u^2}
 -\frac{2B'}u-\frac{4Ru'}{u^3}.
\end{aligned}
\tag{14}
\]
After (14), the entire \(X^2\xi\) coefficient is
\[
-\frac{\gamma}{u^2}\bigl(u(G_R-2\tau)+2\gamma\bigr).
\tag{15}
\]
It follows that \(G_R=V:=2\tau-2\gamma/u\in F\). Integrating only
by subtracting explicit existing elements gives
\[
\begin{aligned}
G&=VR+G_0,\qquad H=2\tau R/u+H_0,\\
c&=\frac{2((\lambda+u\omega)(\tau+M')-B')}{u}R
                    -\frac{2u'}{u^3}R^2+C_0,
\qquad G_0,H_0,C_0\in F.
\end{aligned}
\tag{16}
\]
Thus all entries of the determinant are now polynomial in R over F.
Coefficient comparison in R is licensed for every coefficient with
positive X or xi degree, because that coefficient must vanish. We do not
set the coefficient of \(X^0\xi^0\) to zero or assume it is independent
of R. Neither (15) nor (16) divides by \(\tau+M'\) or V.

## 5. Four high coefficients, including the zero u-prime case

Direct expansion of the full matrix (13) after (16) gives the following
four required vanishing coefficients:
\[
\begin{aligned}
[R^2\xi]J&=\frac{4(uu''-3u'^2)}{u^4},\\
[R^2X]J&=\frac{4u'V'}{u^3}
                         &&\text{after }uu''-3u'^2=0,\\
[RX\xi]J&=\frac4{u^3}
 \bigl(\gamma u'+u(2\tau+M')u'-u\gamma'\bigr),\\
[RX^2]J&=\frac4{u^3}
 \bigl(\gamma\tau u'-\gamma u\tau'+\gamma M'u'
       -2\tau^2uu'-\tau uM'u'+\tau u\gamma'\bigr).
\end{aligned}
\tag{17}
\]
These are coefficients of the original determinant, not an independent
formal replacement for the scalar. Equations (8),(13),(14),(16), with
the three exact contact derivatives (4), provide a complete expansion
recipe. All lower functions \(G_0,H_0,C_0,B\) and their derivatives are
retained in that recipe; they cancel from (17).

If \(u'=0\), the third line of (17) is \(-4\gamma'/u^2\), so
\(\gamma'=0\). The fourth line is then \(-4\gamma\tau'/u^2\),
which is nonzero by (4). This case is impossible. Hence \(u'\ne0\).
The first two lines of (17) now imply
\[
\frac{u'}{u^3}=\frac1\alpha,\qquad
\alpha\in\mathbb C^*,\qquad V=v\in\mathbb C.
\tag{18}
\]
Indeed the derivative of \(u'/u^3\) is zero, and F has prime constants
\(\mathbb C\). The constant v may be zero. The definition of V gives
\(\gamma=u(\tau-v/2)\). Substituting this identity into the third
line of (17) yields
\[
u\tau'=(2\tau+M')u'.
\tag{19}
\]
We need no further equation from the fourth line in the nonzero-u-prime
case.

## 6. Passing to the exact u parameter, without a rational-field ansatz

Because \(u'\ne0\), u is noncomplex and is a separating parameter of
the one-variable field F. Thus F is finite over \(\mathbb C(u)\).
The basis \((R,u)\) is separating in L, with the same first derivative
\(\partial_R\) and constant field F. From this section onward, a prime
means \(d/du\) on F, not the omega derivative. The scaled scalar is
\[
J_*:=J_{R,u,\xi}
 =-\frac{a_0^4}{\rho\omega_s\dot R\,u_\omega}\in L^*.
\tag{20}
\]
No equality \(F=\mathbb C(u)\) or \(L=F(R)\) is used. The constants
of this new derivative in F are still exactly \(\mathbb C\).

Equations (18),(4) integrate by direct subtraction to
\[
\omega=\omega_0-\frac\alpha{2u^2},\qquad
\lambda=\lambda_0+\frac\alpha{2u},
\qquad \omega_0,\lambda_0\in\mathbb C.
\tag{21}
\]
Put \(p=\tau/u\in F\). This p is a coefficient function, not P.
Neither p nor \(p'\) will be divided out. Rewriting (19) in the new
derivative gives \(M_\omega=u\tau_u-2\tau\), hence
\(M_u=\alpha(\tau/u^2)_u=\alpha(p/u)_u\).
The remaining contact equations (4) then give
\[
\begin{aligned}
M&=M_0+\alpha p/u,&
A_1&=A_0+\alpha p+\alpha v/(2u),\\
\chi&=\chi_0-\alpha p^2/2,&
\phi&=\phi_0-\alpha vp/2,
\qquad M_0,A_0,\chi_0,\phi_0\in\mathbb C.
\end{aligned}
\tag{22}
\]
For example \((A_1)_u=\alpha p'-\alpha v/(2u^2)\),
\(\chi_u=-\alpha pp'\), and \(\phi_u=-\alpha vp'/2\).
Each displayed constant is the derivative-zero difference of elements
already in F. These statements remain valid when \(v=0\) or \(p'=0\).

Equations (16) become
\[
\begin{aligned}
G&=vR+G_0,\qquad H=2pR+H_0,\qquad b=B-2R/u,\\
c&=\left(2u(\lambda_0+u\omega_0)p'
                 -\frac{2u^2B'}\alpha\right)R
                 -\frac2\alpha R^2+C_0.
\end{aligned}
\tag{23}
\]
The entire \(R\xi\) coefficient of the determinant in the new basis,
before any choice of B, is
\[
[R\xi]J_*=
\frac{4u}{\alpha}
\left[uB-\alpha(\lambda_0+u\omega_0)p\right]''.
\tag{24}
\]
Its vanishing says that the bracket has constant first derivative.
Subtracting that constant times u, its remaining derivative is zero as
well. Consequently
\[
B=B_0-B_1/u+\alpha(\omega_0+\lambda_0/u)p,
\qquad B_0,B_1\in\mathbb C,
\tag{25}
\]
with no special ansatz for B. In particular (23) simplifies to
\[
c=2(\lambda_0p-B_1/\alpha)R-2R^2/\alpha+C_0.
\tag{26}
\]

## 7. An identity for the entire remaining determinant

All functions \(p,G_0,H_0,C_0\) remain arbitrary elements of F at this
stage. The constants \(v,\lambda_0,\omega_0,M_0,A_0,\chi_0,\phi_0,
B_0,B_1\) are arbitrary complex numbers, subject only to the retained
earlier conditions. Among these complex constants, the identity below
requires only \(\alpha\ne0\); it also retains \(u\in F^*\).
Define
\[
\begin{aligned}
T&=A_0+\alpha p-\lambda_0v,\\
\mathcal E&=\alpha B_0/2+B_1\lambda_0
                    +(\alpha^2\omega_0/2-\alpha\lambda_0^2)p,\\
\mathcal R_G&=G_0'-\alpha T p'/2,\\
\mathcal R_H&=H_0'-(B_1+\alpha M_0/2-2\alpha\lambda_0p)p',\\
\mathcal R_C&=C_0'-\mathcal E p',\\
\Xi&=2\left(\omega_0+\frac{X+\lambda_0}{u}\right)\xi
 +B_0+M_0X+\alpha\omega_0p-2p(X+\lambda_0)^2
 +\frac{(2B_1+4R)(X+\lambda_0)}\alpha.
\end{aligned}
\tag{27}
\]
The symbol T here is only the displayed coefficient function and is not
the contact parameter tau. Substituting (21),(22),(23),(25),(26) into
the three original rows (6) gives the following exact identity for their
full derivative determinant, with columns \((R,u,\xi)\):
\[
\boxed{\displaystyle
J_* =\mathcal R_G\,\Xi
          +(X\mathcal R_H+\mathcal R_C)(vX-2\xi-T).}
\tag{28}
\]
This identity includes the coefficient of \(X^0\xi^0\). No equation
for that coefficient has been imposed. To reconstruct it directly,
differentiate (6) using
\(R_R=1\), \(u_R=0\), the derivative of every displayed rational
power of u, and the four unrestricted jets
\(p',G_0',H_0',C_0'\). The first row is
\((1,-\alpha\xi/(2u^2),X+\lambda)\); expansion in its entries and
collection of those four jets yields precisely (27),(28).

Since the actual scalar is independent of X and xi, first compare the
coefficient of X as a polynomial in R over F in (28). Its R coefficient
is
\[
[RX]J_*=4\mathcal R_G/\alpha.
\tag{29}
\]
Thus \(\mathcal R_G=0\). The coefficient \([X\xi]J_*\) is now
\(-2\mathcal R_H\), and the coefficient \([\xi]J_*\) is then
\(-2\mathcal R_C\). They force
\(\mathcal R_H=\mathcal R_C=0\). Equation (28) therefore gives
\(J_*=0\) identically, contradicting (20).

This last argument divides by neither v nor \(p'\), so their zero cases
are included. It also does not divide by any of the lower functions,
their derivatives, or the calibration's coefficient-dependent value.
The contradiction uses the full original determinant and not merely
the high potential equations.

## 8. Scope, dependencies and reconstruction evidence

The result excludes exactly the noncomplex-tau, invariant-contact branch
\(\mathcal D\tau=0\) of484 under its full actual hypotheses. It does not
assert an exclusion in the constant-tau branch, in the branch
\(\mathcal D\tau\ne0\), or outside the birational projected-line entry.
No intrinsic or coefficient-field variable was made into a complex
ambient coordinate, no original slice was replaced, and no rationality
of an exact finite coefficient field was assumed.

The retained entry is actual264/296/325 through474 and482; the necessary
contact family used here is the fully read484, not a forward formal
realization. The proof is a new full-scalar obstruction to that family.
It does not recursively certify the earlier entry or make a cancellation
or novelty claim.

Fresh unsaved calculations independently reconstruct the literal rows,
the full raw matrix, the zero-dot-R branch, (14)--(17), and the change
of coefficient parameter. In particular the checks recorded as18dc9d,
c5f22b,01f68d,990896 and175724 have zero residuals. The entire final
identity (28), before imposing its three residual equations, was checked
in4880b3;88ed43 also retains the zero-v and zero-p-prime cases. Independent
reconstructions by the other lanes include9bc9f3,d8a0a9,d4e829 for the
high chain,be5725 for (24), and3d23de and a7d376 for the whole terminal
identity. These checks supplement the displayed exact derivation. No
saved checker was executed, imported, compiled or rerun. No earlier
source or canonical file was edited.
