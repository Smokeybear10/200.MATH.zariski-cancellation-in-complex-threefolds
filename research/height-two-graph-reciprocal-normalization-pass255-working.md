# Actual reciprocal normalization of the remaining height-two cubic graph

The affine graph left by252 either has a complex quadratic leading
ratio and is recognized by156, or admits actual polynomial changes
putting its leading ratio into \(q=t^3\) and making
\(\nu=n_\lambda\) a nonzero complex constant.
The changes preserve the chosen shift-two partial up to a nonzero
complex scalar, and their full determinant calibration is explicit.

This is a normalization of the remaining graph branch, not its
original-ring recognition. In particular the final nonzero constant
\(\nu\) is retained; it is not silently set equal to one.

## 1. Exact retained branch and constant fields

Use the complete actual [chart250](height-two-shift-two-cubic-chart-pass250-working.md)
and [projection reduction252](height-two-cubic-plane-projection-reduction-pass252-working.md).
After the actual shear at the end of252, every still-unrecognized
branch has the following data:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
N=[u^2](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad A_{\ker_A N\setminus\{0\}}=L[v],
\quad Nv=1,\\
[L:\mathbb C(t,\lambda)]<\infty,\quad
q,\rho\in C_0,\quad [C_0:\mathbb C(t)]<\infty,\quad
m=k_\lambda=0,\quad \nu=n_\lambda\ne0,\\
y=\Gamma v+\eta,\quad \Gamma\in L^*,\qquad L[y]=L[v].
\end{gathered}
\tag{1}
\]
The full initial ideal has height two and the good speeds are not
proportional. The field \(L\), the actual selected partial, and its
parameter belong to this frame, not to an unrelated formal solution.

The commuting \(t,\lambda\) partials fix \(v\). Put
\(K=\ker_L\partial_\lambda\). This is a finite extension of
\(\mathbb C(t)\). Indeed, for an element of \(K\), differentiating
its monic minimum polynomial over \(\mathbb C(t,\lambda)\) shows
that all coefficients are \(\lambda\)-constant. Thus the element
is algebraic over \(\mathbb C(t)\).
The degree of any finite collection of these elements is bounded
by \([L:\mathbb C(t,\lambda)]\), because adjoining a transcendental
\(\lambda\) preserves their degree. This proves the finiteness
asserted for \(K\).
Its \(t\)-derivative constants are \(\mathbb C\), by the same
minimum-polynomial argument and algebraic closedness of \(\mathbb C\).
In particular \(q,\rho,k\in K\). No rationality of \(K\) is assumed.

With primes denoting the \(t\)-derivative and other subscripts
coefficient partials, the actual formulas are
\[
\begin{gathered}
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\quad
W=w+(\rho'y+\lambda)X+\rho X^2,\\
z=\frac{q''}{2}y^2+k'y+n,\\
w=-\frac{q'''}{6\nu}y^3
 +\left(\frac{\rho''}{2}-\frac{k''}{2\nu}\right)y^2
 -\frac{n_t}{\nu}y+\frac{\ell}{\nu},\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}=-a^2,
\quad a=EX\ne0 .
\end{gathered}
\tag{2}
\]
The equality of determinants holds for every \(X\).
When \(y\) is used in place of \(v\), the change of parameters has
determinant \(\Gamma\). At \(X=0\) this gives the nonzero scalar
\[
J:=\det\frac{\partial(y,z,w)}{\partial(t,\lambda,y)}
   =z_tw_\lambda-z_\lambda w_t
   =-\frac{a^2}{\Gamma}\in L^* .
\tag{3}
\]
The subscripts in the middle expression hold \(y\) fixed.
The notation for the first row means the function \(y\) itself,
whose row is \((0,0,1)\). All coefficients of positive powers of
the independent line parameter \(y\) in (3) vanish.

## 2. The complete scalar coefficient gates

If \(q'''=0\), the derivative-constant argument in Section 1
gives \(q=c_2t^2+c_1t+c_0\) with complex coefficients.
Then \(Z-c_2Y^2-c_1XY-c_0X^2\) is an actual coordinate killed by
\(E^2\), with the inverse obtained by adding the same quadratic.
The two good coordinates are also killed by \(E^2\), so156
recognizes the kernel. Hence assume \(q'''\ne0\).

Before restricting the \(\lambda\)-dependence of \(n,\ell\), the
highest coefficient of the literal scalar expression (3) is
\[
[y^5]J=\frac{(q''')^2\nu_\lambda}{12\nu^2}.
\tag{4}
\]
It follows that \(\nu_\lambda=0\). Subtracting the explicit
primitive \(\nu\lambda\), rather than assuming a rational field,
gives
\[
\nu\in K^*,\qquad n=\nu\lambda+n_0,\qquad n_0\in K .
\tag{5}
\]
The coefficients of \(y^5,y^4\) now vanish identically.
The next two coefficients, still with unrestricted \(\ell\in L\),
are
\[
\begin{aligned}
[y^3]J&=\frac{q''''\nu-4q'''\nu'}{6\nu},\\
[y^2]J&=\frac{q'''\ell_\lambda-\nu^2\rho'''
                      +\nu k'''-3k''\nu'}{2\nu}.
\end{aligned}
\tag{6}
\]
These formulas follow directly by inserting (2) into
\((q'''y^2/2+k''y+n_t)w_\lambda-\nu w_t\).
No differentiated graph relation is substituted before forming
this fixed-parameter Jacobian.

The second equality in (6) implies
\[
\mu:=\frac{\nu^2\rho'''-\nu k'''+3k''\nu'}{q'''}\in K,\qquad
\ell=\mu\lambda+\ell_0,\quad \ell_0\in K .
\tag{7}
\]
Again the last assertion follows by subtracting a literal
\(\lambda\)-primitive.
For completeness, the two remaining coefficients are
\[
\begin{aligned}
[y]J={}&
\frac{\nu\nu''-2(\nu')^2}{\nu}\lambda
 +n_0''-\frac{2\nu'n_0'}{\nu}+\frac{k''\mu}{\nu},\\
[1]J={}&
\left(\frac{2\mu\nu'}{\nu}-\mu'\right)\lambda
 +\frac{\mu n_0'+\ell_0\nu'}{\nu}-\ell_0'.
\end{aligned}
\tag{8}
\]
The first line is zero. The variable \(\lambda\) is transcendental
over \(K\): if it were algebraic, the unique extension of the zero
derivation of \(K\) would kill it, contradicting
\(\partial_\lambda\lambda=1\).
Consequently
\[
\nu\nu''-2(\nu')^2=0,\qquad
n_0''-\frac{2\nu'n_0'}{\nu}+\frac{k''\mu}{\nu}=0 .
\tag{9}
\]
The second line of (8) is the scalar in (3); it is not required
to be constant in \(\lambda\). The factors \(a,\Gamma\) can depend
on the coefficient field. Thus no additional zero coefficient
is inferred from that last line.

## 3. Exact integration in the finite coefficient field

The first identity in (9) is equivalent to \((1/\nu)''=0\).
The first identity in (6) is equivalent to
\((q'''/\nu^4)'=0\). The derivative constants of \(K\) therefore give
\[
D=\alpha t+\beta=\frac1\nu,\qquad
\alpha,\beta\in\mathbb C,\quad (\alpha,\beta)\ne(0,0),\qquad
q'''=\chi D^{-4},\quad \chi\in\mathbb C^* .
\tag{10}
\]
These conclusions hold in the exact field, with no rational-function
ansatz and no omitted algebraic homogeneous solution.

If \(\alpha=0\), put \(c=\chi/(6\beta^4)\ne0\).
Successive integration gives
\[
q=c t^3+Q_2(t),\qquad Q_2\in\mathbb C[t],\quad \deg Q_2\le2,
\qquad \nu=1/\beta\in\mathbb C^* .
\tag{11}
\]
If \(\alpha\ne0\), use
\((D^{-1})'''=-6\alpha^3D^{-4}\). For
\(c=-\chi/(6\alpha^3)\ne0\), the complete answer is
\[
q=\frac cD+Q_2(t),\qquad Q_2\in\mathbb C[t],\quad\deg Q_2\le2,
\qquad \nu=D^{-1}.
\tag{12}
\]
Completeness follows by subtracting the displayed particular
solution and applying the derivative-constant argument three times.

## 4. An actual quadratic shear removes the common remainder

Write \(Q_2(t)=c_2t^2+c_1t+c_0\), and define the homogeneous
quadratic
\[
\widehat Q_2(X,Y)=c_2Y^2+c_1XY+c_0X^2 .
\]
Set \(Z_0=Z-\widehat Q_2(X,Y)\), fixing \(X,Y,W\).
The inverse is \(Z=Z_0+\widehat Q_2(X,Y)\), so both orders hold
in the original polynomial ring.
Its complete projected transformation is
\[
q_0=q-Q_2,\qquad
z_0=z-c_2y^2=\frac{q_0''}{2}y^2+k'y+n,\qquad
\sigma_0=q_0'y+k .
\tag{13}
\]
Thus \(k,n,\lambda\) are unchanged, not merely the leading ratio.
The literal partial \(\partial_{Z_0}=\partial_Z\); the shift,
\(N,L,v\), and calibration in (2) are unchanged.
In (11) or (12), \(q_0\ne0\), so \(Z_0\) still has exact time
degree two. All other slots keep their exact degrees.

## 5. Constant reciprocal denominator

In case (11), the further actual change \(Z_*=Z_0/c\), with
inverse \(Z_0=cZ_*\), fixes \(X,Y,W\). It gives
\[
q_*=t^3,\quad k_*=k/c,\quad n_*=(\nu\lambda+n_0)/c,\quad
\nu_*=\nu/c\in\mathbb C^*,\quad
N_*=cN,\quad v_*=v/c,\quad L_*=L .
\tag{14}
\]
Here the new selected derivation follows from
\(\partial_{Z_*}=c\partial_{Z_0}\), using the same global \(u\).
It satisfies \(N_*v_*=1\), and \(y\) stays affine in \(v_*\).
The actual coordinate determinant contributes \(1/c\), while
the parameter substitution \(v=cv_*\) contributes \(c\).
Their product is one, giving the calibrated scalar
\(-a^2\) in \((t,\lambda,v_*)\), for every \(X\).

## 6. Nonconstant reciprocal denominator: full actual inverse and chart

Suppose \(\alpha\ne0\), so \(q_0=c/D\).
After the shear in Section 4 make the actual polynomial change
\[
X_*=\alpha Y+\beta X,\quad Y_*=X,\quad
Z_*=Z_0/c,\quad W_*=W .
\tag{15}
\]
Its full inverse, including the preceding shear, is
\[
X=Y_*,\quad Y=(X_*-\beta Y_*)/\alpha,\quad
Z=cZ_*+\widehat Q_2\!\left(Y_*,(X_*-\beta Y_*)/\alpha\right),
\quad W=W_* .
\tag{16}
\]
Substitution in either order returns all four original variables.
The only denominators in these actual inverses are the nonzero
complex constants \(\alpha,c\). No original polynomial \(D\)
or speed has been inverted.

The new good speed and coefficient-field parameters are
\[
a_*=EX_*=aD=\alpha b+\beta a\ne0,\qquad
t_*=\frac1D,\qquad
y_*=-\frac{\alpha}{D}y,\qquad
\rho_*=\frac{\rho}{D^2},\qquad \lambda_*=\frac{\lambda}{D}.
\tag{17}
\]
The equality \(X_*=DX+\alpha y\) proves the formula for \(y_*\).
In the fixed-\(X_*\) chart one can use
\(X=X_*/D+y_*\).
Expanding the entire \(W\) expression in (2), rather than just
its leading part, gives
\[
\begin{gathered}
w_*=w+(\rho'y+\lambda)y_*+\rho y_*^2,\\
\theta_*=\frac{\rho'y+\lambda+2\rho y_*}{D}
        =\rho_*'y_*+\lambda_*,\qquad
\rho_*'=-\rho'/\alpha+2\rho/D .
\end{gathered}
\tag{18}
\]
The prime on a starred function now denotes differentiation in
\(t_*\) at fixed \(\lambda_*\).

For the other bad slot, direct expansion uses
\(q_0'=-c\alpha/D^2,\ q_0''=2c\alpha^2/D^3\).
It gives
\[
\begin{gathered}
q_*=\frac{q_0}{cD^2}=t_*^3,\qquad
k_*=\frac{k}{cD},\qquad
n_*=\frac{n}{c}=\frac{\lambda_*+n_0}{c},\\
Z_*=z_*+(q_*'y_*+k_*)X_*+q_*X_*^2,\\
z_*=\frac{q_*''}{2}y_*^2+k_*'y_*+n_*,
\qquad \nu_*=(n_*)_{\lambda_*}=1/c\in\mathbb C^* .
\end{gathered}
\tag{19}
\]
To check the linear coefficient in \(z_*\), its unscaled value
is \(k-Dk'/\alpha\); this equals
\(\partial_{t_*}(k/D)\).
Here \(k\) has no \(\lambda\)-dependence, so the partial is
indeed taken at fixed \(\lambda_*\).
The constant part is \(n\), and \(n=\lambda/D+n_0\) from (5),(10).

The parameter change has the field inverse
\(t=(1/t_*-\beta)/\alpha,\ \lambda=\lambda_*/t_*\).
The constants of its \(\lambda_*\)-partial are the same \(K\),
because \(\partial_{\lambda_*}=D\partial_\lambda\) on \(L\).
Thus \(k_*,n_0/c\) are \(\lambda_*\)-constant.
In particular this transformation genuinely preserves \(m=0\).
It is only these coefficient-field formulas that use rational
expressions in \(D\); the ambient maps remain (15)--(16).

The actual new selected partial is
\(\partial_{Z_*}=c\partial_Z\), with \(X_*,Y_*,W_*\) fixed.
Consequently \(N_*=cN,\ v_*=v/c,\ L_*=L\).
The first projection \(y_*\) is still affine with nonzero
parameter slope. Since \(t_*\) is transcendental and \(q_*\ne0\),
the two new good slots and the new \(Z_*\) have exact degrees
one, one and two; \(W_*\) is unchanged.
Every ambient operation used is homogeneous for weights1122
with a homogeneous inverse. The full height-two initial ideal
is therefore transported, not replaced by one necessary relation.

Finally the full calibration can be checked before returning to
the normalized chart theorem. The actual coordinate determinant
of (15), including the earlier determinant-one shear, is
\(-\alpha/c\).
The change \((t,\lambda,v)\mapsto(t_*,\lambda_*,v_*)\) has determinant
\(-\alpha/(cD^3)\). Since
\(X_*=DX+\alpha y\), the four-parameter change has determinant
\(-\alpha/(cD^2)\). The full chain rule gives
\[
\det\frac{\partial(Y_*,Z_*,W_*)}{\partial(t_*,\lambda_*,v_*)}
 =D^2(-a^2)=-(a_*)^2
\quad\hbox{for every }X_* .
\tag{20}
\]
This calculation includes the change in the selected parameter.
It does not treat a nonconstant coefficient-field unit as an
original-ring unit.

## 7. Normalized output and remaining obligation

Drop stars only after the actual transformations above.
Every branch not already recognized by the quadratic-ratio gate
has an actual chart of250 with
\[
q=t^3,\quad k_\lambda=0,\quad
n=\nu\lambda+n_0,\quad \nu\in\mathbb C^*,\quad
y=\Gamma v+\eta,\quad \Gamma\in L^* .
\tag{21}
\]
The leading ratio \(\rho\) and the remaining coefficients may
still belong to an algebraic extension of \(\mathbb C(t)\).
No rationality of their exact constant field is asserted.

Applying the already-derived scalar identities in this new chart
also records, without solving the final recognition problem,
\[
\begin{gathered}
\ell=\mu\lambda+\ell_0,\qquad
\mu=(\nu^2\rho'''-\nu k''')/6,\\
n_0''+k''\mu/\nu=0,\qquad
J=-\mu'\lambda+\mu n_0'/\nu-\ell_0'\in L^* .
\end{gathered}
\tag{22}
\]
These are the remaining exact coefficients, not a replacement
for actual field return or a polynomial inverse in the final
unrecognized graph branch.

The original-ring endpoint for (21)--(22), the selected-shift
pair \((1,1)\), arbitrary entry and higher time profiles are
separate obligations. This note does not close any of them.

## Verification and scope

The complete250 and252 inputs and the retained156 recognition
statement were read. An independent unsaved symbolic expansion
checks (4), all four residual coefficients (6),(8), and the
particular reciprocal primitive in (12). The actual inverse,
coefficient transport and four-variable determinant factors are
derived above in the original coordinates.
Finite algebra does not certify finite-field integration,
actual entry or the retained recognition theorem.
No saved checker was executed, imported or compiled; no earlier
source, index or verification packet was edited.
No human expert review, proof-assistant certification, historical
novelty or unrestricted cancellation conclusion is claimed.
