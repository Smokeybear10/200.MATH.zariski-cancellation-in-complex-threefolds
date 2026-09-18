# Zero-R recognition for the supplied Z-squared minus X-cubed Y configuration

Status: bounded working proof, pending independent saved-source review.
For the supplied actual full initial kernel \(Z^2-X^3Y\), the branch
\(k_\rho=0\) has an invariant coordinate in the original polynomial
four-ring. The proof uses exact field return to exclude two otherwise
valid algebraic coefficient possibilities. It does not assert that the
coefficient square root of \(t\) is an original coordinate.

## 1. Actual hypotheses and the general zero-R reduction

Assume the actual hypotheses of
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
with the specific full weighted initial kernel
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=\mathcal A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
q^2=t,\qquad R=k_\rho=0.
\end{gathered}
\tag{1}
\]
The displayed ideal is the entire kernel, not one necessary relation.
All coordinates and the global slice are actual. The occurring Z-pivot
supplies the intrinsic derivation, exact fields, and calibrated chart
\[
\begin{gathered}
N=[u^3](\partial_Z|_{\mathcal A})\ne0,\qquad
L=\operatorname{Frac}(\ker_{\mathcal A}N),\qquad
\mathcal A_L=L[v],\quad Nv=1,\\
\mathfrak a=EX\in L^*,\quad
t=EY/\mathfrak a,\quad \rho=(E^2W/2)/\mathfrak a^2,\quad
q=(E^2Z/2)/\mathfrak a^2,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}
 =-\mathfrak a^3\in L^* .
\end{gathered}
\tag{2}
\]
The last determinant is independent of \(X\). The variables \(t,\rho\)
are independent. Their extended coefficient partials commute and
initially fix \(v\). Since \(q^2=t\), differentiation in \(\rho\)
gives \(q\in K\). The element \(q\), not a branch chosen analytically,
is the given leading ratio. In particular
\[
q'=\frac1{2q},\qquad
Q:=q''/2=-\frac1{8q^3},\qquad
d:=q'''/6=\frac1{16q^5},\qquad
h:=k''/2,\qquad Q'=3d\ne0.
\tag{3}
\]
Writing powers \(t^{1/2}\) below means this algebraic coefficient
element. It does not impose rationality of \(K\) or a unit speed in \(B\).

The general-q zero-R derivation in Sections 1--3 of
[zero-R192](weight-four-split-zero-r-coordinate-recognition-pass192-working.md)
uses only \(q_\rho=0\) and \(q'''\ne0\) before specializing its coefficient
equations to the split form. Those are the properties in (3).
Here are the relevant actual and coefficient gates explicitly.

If \(y\in L\), the factorized actual determinant makes
\(n_\rho=0\), \(\vartheta\in L\), and \(w\) affine over \(L\).
Actual field return then gives \(L=\mathbb C(y,z)\).
The field derivative fixing \(L,X\) and sending \(w\) to one is the
original \(\partial_W\); it commutes with \(E\). Thus \(E\) restricts
to an LND of the actual ring \(\mathbb C[X,Y,Z]\), with two good
coordinates. Primitive division preserves its kernel, local nilpotence,
and the two second-iterate vanishings.
Wang's two-coordinate theorem, in
[Dasgupta--Gupta Theorem 4.1](https://arxiv.org/pdf/1701.03635v1),
gives either an invariant nonzero complex linear form in \(X,Y\), or an
invariant coordinate \(cZ+H(X,Y)\), \(c\in\mathbb C^*\).
The former contradicts transcendental \(t\). The latter requires
\(cq+H_2(1,t)=0\), contrary to \(q'''\ne0\).
This is the actual constant-projection argument of zero-R187/192,
not an inference from the second potential alone.

Consequently \(y\notin L\). The cubic potential forces
\(s:=n_\rho\ne0\), and the other projected entries are polynomials in
\(y\). The whole-line identity in (2) therefore makes \(y\) affine in
\(v\), with \(\Gamma=Ny\in L^*\).
Write \(\vartheta=P(y)\) and \(w=\mathcal W(y)\).
The exact determinant identities are
\[
\mathcal W_U=P_t+P_UP_\rho,\qquad
\mathcal W_t+P_U\mathcal W_\rho
 =\frac{\mathfrak a^3}{s\Gamma}\in L^* .
\tag{4}
\]
All derivatives in (4) are coefficient derivatives before evaluation.
The speed and affine-parameter factor have not been normalized to one.

## 2. General coefficient cover, integral, and exact field return

The \(U^8\) coefficient in (4) gives
\((s^{-2})_{\rho\rho}=0\). Set \(\eta=s^{-1}\) and
\(\partial_n=\eta\partial_\rho\), so \(\partial_n n=1\).
Explicit polynomial primitive subtraction yields
\[
\rho=a n^2+b n+c,\qquad \eta=2an+b,\qquad a,b,c\in K.
\tag{5}
\]
The letter \(a\) in this formula is a cover coefficient, not
the speed \(\mathfrak a\).
The element \(n\) is transcendental over \(K\); initially \(L/K(n)\)
can be a proper finite extension. Extend the derivative on \(K\)
fixing \(n\), then across that separable extension, and denote it
by a prime or \(\nabla\). Put
\[
F(U)=dU^3+hU^2,\quad M=\eta\ell,\quad
P(U)=\rho'U-\eta F(U)+M,\quad
\delta=\nabla-F_U\partial_n.
\tag{6}
\]
The old derivatives are
\(\partial_\rho=\eta^{-1}\partial_n\) and
\(\partial_t^{\rm old}=\nabla-(\rho'/\eta)\partial_n\).
Equation (4) becomes \(\mathcal W_U=\delta P\) and
\(\delta\mathcal W=\mathfrak a^3/(s\Gamma)\in L^*\).
Integrating only in the polynomial variable \(U\) gives
\[
\mathcal W
 =aF^2-\eta'UF
 -\eta\left(\frac{d'}4U^4+\frac{h'}3U^3\right)
 +\frac{\rho''}2U^2+M'U-M_nF+W_0,\qquad W_0\in L.
\tag{7}
\]
The \(d'\) term is retained. No algebraic coefficient primitive is
adjoined. For \(\mathcal W_j=[U^j]\mathcal W\), its scalar equation
has coefficient recurrence
\[
[U^j]\delta\mathcal W
 =\mathcal W_j'-3d\,\partial_n\mathcal W_{j-2}
                  -2h\,\partial_n\mathcal W_{j-1}.
\tag{8}
\]
The top equations and the \(U^2\) equation give
\[
\begin{gathered}
2da'+ad'=0,\qquad
\mu:=M_{nn}=\frac{ahd'}{d^2}-\frac{4ah'}{3d},\qquad
M=\frac{\mu}{2}n^2+M_1n+M_0,\quad M_1,M_0\in K,\\
3d(W_0)_n=\frac{a'''}2n^2+
 \left(\frac{b'''}2-h'\mu-3h\mu'\right)n+
 \frac{c'''}2-h'M_1-3hM_1',\\
W_0\in K[n],\qquad [n^3]W_0=\gamma:=\frac{a'''}{18d}.
\end{gathered}
\tag{9}
\]
These are the general identities, not the specialized \(d=4t\)
or split \(d=t^{-4}-1\) formulas. Polynomial subtraction and
\(\ker_L\partial_n=K\) justify the integrations in (9).

Now \(z=n+Qy^2+k'y\) and \(w=\mathcal W(y)\) belong to \(K[n,y]\).
Using the actual field equality in (2), and then intersecting
fields after clearing a denominator in the independent \(y\), gives
\[
L=K(n),\qquad
K(y)(z)=\mathbb C(y,z,w),\qquad
n=z-Qy^2-k'y.
\tag{10}
\]
Thus \(y,z\) are independent over \(K\). This actual field-return
condition will do work not supplied by the scalar equations.

## 3. Pole degree excludes the quadratic cover

Suppose \(a\ne0\). Equation (9) and (3) give
\[
\frac{a'}a=\frac5{4t},\qquad
a=A t^{5/4},\qquad
\gamma=-\frac{5A}{24}t^{3/4},\qquad A\in\mathbb C^* .
\tag{11}
\]
The powers can be formed in a finite extension of \(K\); their
constant ratios follow from the exact constant field. Equivalently,
one can make the following valuation calculation entirely in \(K\).
Choose a place over \(t=\infty\), with pole order \(e>0\) for \(t\).
The leading exponent \(5/4\) of \(a\) forces \(4\mid e\).
Its third derivative has nonzero coefficient
\((5/4)(1/4)(-3/4)\); division by \(18d\) makes \(\gamma\) have
pole order \(3e/4\ge3\).

All terms in (7) other than \(W_0\) have \(n\)-degree at most two.
After the shift in (10), \(w\) is therefore a cubic polynomial in
\(z\) with leading coefficient \(\gamma\).
Extend the chosen coefficient-curve valuation by independent \(y,z\).
The valuation of a polynomial in \(z\) is the minimum of its
coefficient valuations: independent \(z\)-monomials cannot cancel
the leading residue polynomial. Hence \(w\) has a pole of order
at least three there.

The degree of the pole divisor of a nonconstant function equals its
function-field map degree. The exact equality in (10) would give
degree one over \(\mathbb C(y,z)\), a contradiction.
This is the same pole-degree argument recorded, with its primary
curve inputs, in Section 3 of
[coefficient lemmas191](weight-four-split-coefficient-ode-lemmas-pass191-working.md).
Here the lower bound is three rather than nine. We conclude \(a=0\).

## 4. The other linear-cover power is also excluded

Now \(b\ne0\), \(\mu=0\), \(M=M_1n+M_0\).
The \(U^4\) recurrence is
\[
10db''+5d'b'+d''b=0
\quad\Longleftrightarrow\quad
b''-\frac5{4t}b'+\frac7{8t^2}b=0.
\tag{12}
\]
With \(\Theta=t\,d/dt\), it is
\((\Theta-\tfrac12)(\Theta-\tfrac74)b=0\).
Over a finite extension containing \(t^{1/4}\), two successive
first-order subtractions and the exact constant field give
\[
b=Aq+B t^{7/4},\qquad A,B\in\mathbb C,\qquad
\gamma_2:=[n^2]W_0=\frac{b'''}{12d}
 =\frac A2-\frac{7B}{16}t^{5/4}.
\tag{13}
\]
This is the full algebraic solution space of (12), not just a list
of example solutions. For instance applying
\(\Theta-\tfrac12\) first isolates a constant multiple of \(t^{7/4}\);
subtracting it leaves a constant multiple of the given \(q\).

If \(B\ne0\), (13) and \(q\in K\) put \(t^{7/4}\) in \(K\), and
then \(t^{1/4}=t^2/t^{7/4}\) also belongs to \(K\).
At a place over infinity \(4\mid e\), and \(\gamma_2\) has pole
order \(5e/4\ge5\). The polynomial \(w\), shifted as in (10),
has \(z\)-degree two and coefficient \(\gamma_2\) on \(z^2\).
The same independent-monomial and pole-degree argument contradicts
the degree-one field equality in (10). Therefore
\[
b=\lambda q,\qquad \lambda\in\mathbb C^*,\qquad
W_0=\frac{\lambda}{2}n^2+D n+g_0,\qquad D,g_0\in K.
\tag{14}
\]
This is not the earlier split slope \(\lambda t\).
The surviving quadratic coefficient in \(W_0\) is constant, not zero.

## 5. Residual scalar equations and the projected linear pencil

For clarity, before using (14), the remaining coefficients in (7) are
\[
\begin{gathered}
\mathcal W_4=-b'd-bd'/4,\qquad
\mathcal W_3=-b'h-bh'/3-dM_1,\\
\mathcal W_2=b''n/2+c''/2-hM_1,\qquad
\mathcal W_1=M_1'n+M_0',\\
D=\frac{c'''}{6d}-\frac{h'M_1}{3d}-\frac{hM_1'}d .
\end{gathered}
\tag{15}
\]
The \(U^3,U\) equations, using (14), yield
\[
\begin{gathered}
\mathcal W_3'=3dM_1'+hb'',\qquad
M_1''=\lambda k'',\qquad M_0''=2hD,\\
M_1=\lambda k+\alpha t+\beta,\quad \alpha,\beta\in\mathbb C,\qquad
\delta\mathcal W=D'n+g_0'\ne0 .
\end{gathered}
\tag{16}
\]
No constancy of \(D\) has yet been inferred.

Make the complex polynomial change of projected entries
\(\widetilde w=w-\lambda z^2/2\).
Substitute \(n=z-Qy^2-k'y\) into (7). Since \(b''/2=\lambda Q\),
it gives
\[
\begin{gathered}
\widetilde w=(\alpha y+D)z+G(y)+g_0,\\
G(U)=g_4U^4+g_3U^3+g_2U^2+g_1U,\\
g_4=\mathcal W_4-\lambda Q^2/2=0,\\
g_3=\mathcal W_3-\lambda Qk'-\alpha Q,\\
g_2=c''/2-hM_1-\lambda(k')^2/2-DQ-\alpha k',\qquad
g_1=M_0'-Dk',\\
g_3'=0,\qquad g_2'=-QD',\qquad g_1'=-k'D'.
\end{gathered}
\tag{17}
\]
The identity \(g_4=0\) follows directly from (3):
\(\mathcal W_4=\lambda/(128q^6)=\lambda Q^2/2\).
For \(g_3'\), use the first equation of (16), \(Q'=3d\),
\(k''=2h\), and \(M_1'=\lambda k'+\alpha\).
For \(g_2'\), the terms other than \(-QD'\) are
\(c'''/2-h'M_1-3hM_1'-3dD=0\).
For \(g_1'\), they are \(M_0''-2hD=0\).

If \(D\notin\mathbb C\), apply the exact linear-pencil lemma of
Section 3 of
[field normal form190](weight-four-absent-zero-r-field-normal-form-pass190-working.md)
to (10) and (17), over \(\mathbb C(y)\), with independent parameter
\(z\). Removing the complex polynomials \(\lambda z^2/2+\alpha yz\)
does not change the returned field.
The lemma gives \(G(y)+g_0\in\mathbb C(y)+\mathbb C(y)D\).
Clearing a common denominator in \(\mathbb C[y]\) and comparing a
complex basis of the finite coefficient span makes each coefficient
belong to \(\mathbb C+\mathbb CD\).
In particular \(g_2=u+vD\), \(u,v\in\mathbb C\).
Its derivative and (17) would imply \(v=-Q\), since \(D'\ne0\),
contrary to \(Q'=3d\ne0\).
Thus
\[
D\in\mathbb C,\qquad G\in\mathbb C[U],\qquad
g_0'\ne0,\qquad K=\mathbb C(g_0).
\tag{18}
\]
The scalar inequality is from (16).
For the final field equality, (17) now supplies the projected
polynomial inverse between \((y,z,w)\) and \((y,z,g_0)\);
intersecting its fraction fields with \(K\) proves the assertion.
This is still not an original-ring coordinate claim.

## 6. Actual polynomial transport and both inverse orders

All actual chart entries are in \(K[n,y,X]\). The coefficient of
\(n\) in \(Z\) is one, while that of \(n^2\) in \(W\) is \(\lambda/2\).
Using \(P=\rho'U-bF+M\), equations (14) and (16) give
\[
[n]\{W-\lambda Z^2/2\}
 =\alpha y+D+(\alpha t+\beta)X
 =\alpha Y+\beta X+D=:A_0(X,Y)\in\mathbb C[X,Y].
\tag{19}
\]
The \(n^2\) term has already canceled.
Indeed the \(X^2\) coefficient in this comparison is
\(b-\lambda q=0\), and the extra \(Xy\) coefficient is
\(b'-\lambda q'=0\). Therefore
\[
I_*:=W-\frac{\lambda}{2}Z^2-A_0(X,Y)Z\in B\cap K[X,y],
\qquad I_*|_{X=0}=G(y)+g_0.
\tag{20}
\]

On the coefficient field and polynomial chart, use the exact derivation
\(\mathscr T=\nabla-X\partial_y-F_U(y)\partial_n\).
It kills \(X,Y,Z\), using \(Q'=3d\), \(k''=2h\), and \(q''=2Q\).
Moreover \(\delta\rho=P_U\) and \(\mathcal W_U=\delta P\), so
literal differentiation of the original \(W\) gives
\[
\mathscr T W
 =\delta\mathcal W+
 X(\delta P-\mathcal W_U)+X^2(\delta\rho-P_U)
 =g_0'.
\tag{21}
\]
The complex polynomial \(A_0(X,Y)\) is also killed by \(\mathscr T\).
Thus \(\mathcal Q=I_*-g_0\in K[X,y]\) satisfies
\((\nabla-X\partial_y)\mathcal Q=0\).
Substitute \(y=Y-tX\). This polynomial change makes that derivation
coefficient differentiation at fixed \(X,Y\).
The exact constant field of \(K\) gives
\(Q_0(X,Y):=\mathcal Q(X,Y-tX)\in\mathbb C[X,Y]\).

We obtain the original invariant coordinate and its inverse
\[
\begin{aligned}
I&=W-\frac{\lambda}{2}Z^2
       -(\alpha Y+\beta X+D)Z-Q_0(X,Y)=g_0,\\
W&=I+\frac{\lambda}{2}Z^2
       +(\alpha Y+\beta X+D)Z+Q_0(X,Y).
\end{aligned}
\tag{22}
\]
Both maps fix \(X,Y,Z\). Each composition cancels the same three
complex-coefficient polynomials, so both are polynomial inverses in
the original ring, with no division by a coordinate or by \(q\).
Since the right side \(g_0\) lies in \(K\subset\operatorname{Frac}\mathcal A\),
the polynomial \(I\) satisfies \(EI=0\).

The global slice makes \(\mathcal A\simeq B/(u)\) regular:
\(Eu=1\) expresses one as a combination of the original partials of
\(u\). In the actual coordinates of (22), \(E\) is a nonzero
\(\mathbb C[I]\)-linear LND of a polynomial three-ring over
\(\mathbb C[I]\). The exact regular-kernel statement of
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
therefore gives
\[
\mathcal A=\mathbb C[I]^{[2]}\cong\mathbb C^{[3]} .
\tag{23}
\]
The published theorem is an explicit retained input, not a result
purportedly certified by finite symbolic controls.

## Scope

This proof treats only the supplied full initial kernel in (1) and
its zero-R branch. The nonzero-R branch, other positive bad-rank forms,
height-two initial kernels, higher minimum profiles, arbitrary entry,
and unrestricted cancellation remain outside this note.
In particular the power-law coefficients allowed by the scalar equation
were excluded through the actual field equality, not by claiming those
formal solutions do not exist.

The proof was derived after complete source reads of universal184,
the general-d zero-R reduction192, and the coefficient-curve lemmas191.
The published BGL endpoint was freshly read in the current review chain.
No checker was authored, executed, imported, or compiled for this note;
no194 or earlier source was changed. This is a working proof, not human
expert review, proof-assistant certification, historical novelty clearance,
public submission, or completion of the unrestricted objective.
