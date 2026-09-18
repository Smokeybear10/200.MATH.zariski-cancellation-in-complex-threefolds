# Excluding a cubic/quadratic projection at a quadratic rank-two center

Status: bounded working exclusion. In the actual rank-two
\(q=1/\rho\) chart, a squarefree quadratic center cannot have
projected degrees \((\deg_vy,\deg_v\vartheta)=(3,2)\).
The proof uses the exact conductor of a cubic/quadratic plane ring,
the actual evaluated-cofactor bound, and a comparison of two center
polynomials. It makes no normality or original-coordinate claim for
the projected plane ring.

## 1. Retained actual inputs

Retain the full hypotheses of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md)
and [center pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md),
freshly read through EOF. In particular
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\quad q=1/\rho,
\quad [L:\mathbb C(t,\rho)]<\infty,\\
O=L[v],\quad C=L[y,\vartheta]\subset O,\quad
\operatorname{Frac}C=L(v),\quad Nv=1,\\
\mathcal R(V)=2\rho^{-3}V+k_\rho,
\quad R=\mathcal R(\vartheta)\ne0,
\quad RO\subset C .
\end{gathered}
\tag{1}
\]
The capital letters are actual polynomial coordinates, the initial
ideal is the full kernel, and the selected original partial gives
the displayed exact coefficient field. No rationality of \(L\)
is assumed.

Use the full sextic eliminant of212 and its selected monic plane
factor, denoted by \(\mathcal H\) and \(G\). The actual field return
and scalar determinant \(J_0=-a^3\in L^*\) in212 give
\[
\begin{gathered}
\mathcal H=GQ_1,\quad
0\ne Q_1(y,\vartheta)\mid R^3\text{ in }O,\\
\deg\mathcal H=6,
\quad \mathcal H_6=-\rho^{-11}V^6,
\quad [U^4]\mathcal H=\frac{k_{tt}^2}{4\rho^3},\\
V_c=-\rho^3k_\rho/2,\quad
\mathcal H(U,V_c)=\rho^{-3}p(U)^2,
\quad p(U)=S(U,V_c)-\ell .
\end{gathered}
\tag{2}
\]
The cofactor is a nonzero evaluated polynomial; it is not assumed
to be a unit. Both its support and the conductor inclusion in (1)
are actual consequences of the full potentials. We do not impose
them on an arbitrary polynomial pair without those hypotheses.

Assume for contradiction that
\[
\deg_vy=3,\quad \deg_v\vartheta=2,\quad
p\text{ is squarefree of degree two},\quad
h:=k_{tt}\ne0,
\quad [U^2]p=h/2 .
\tag{3}
\]
The last two facts follow directly from the U-quadratic term of
\(S\). The monic normalization in213 gives \(\deg_U G=2\),
while212 gives \(\deg G=3\). Hence \(\deg Q_1=3\).

## 2. Exact-field cubic/quadratic normalization and conductor

Complete the square in \(\vartheta\) by an affine change of the
line parameter over \(L\), without rescaling it or adjoining a
square root. For \(x=v-v_0\), \(v_0\in L\), write
\[
\vartheta=A_2x^2+c_0,\quad
y=a_3x^3+a_2x^2+a_1x+a_0,\quad
A_2a_3\ne0,\qquad c_1=a_1/a_3 .
\tag{4}
\]
All coefficients lie in \(L\), and \(Nx=1\).
Subtracting the even part of \(y\) shows both ring inclusions in
\(C=L[x^2,x^3+c_1x]\). Put \(s=x^2\). The exact even/odd
decompositions are
\[
O=L[s]\oplus xL[s],\qquad
C=L[s]\oplus x(s+c_1)L[s],\qquad
\mathfrak c_{C/O}=(s+c_1)O .
\tag{5}
\]
For the middle equality, the right side is a ring: the product of
two odd terms is \(s(s+c_1)^2\) times a polynomial in \(s\).
It contains both generators and is contained in their ring.

For completeness, the conductor assertion means
\(\mathfrak c_{C/O}=\{b\in O:bO\subset C\}\).
Write \(b=f(s)+xg(s)\). Since \(O\) is generated as an
\(L[s]\)-module by \(1,x\), the condition is equivalent to
\(b,bx\in C\). By the two decompositions this says precisely
that both \(f,g\) are divisible by \(s+c_1\), proving (5).
Also \(\dim_L(O/C)=1\); in particular the plane ring is proper.
The argument covers \(c_1=0\) as well as \(c_1\ne0\).

Now \(RO\subset C\) implies \(R\in\mathfrak c_{C/O}\).
Both \(R\) and the conductor generator have degree two in \(x\).
Their quotient must therefore be a nonzero scalar of \(L\).
Comparing the leading coefficient and the constant term gives
\[
R=2\rho^{-3}A_2(x^2+c_1),\qquad
V_c=c_0-A_2c_1,
\qquad y_c:=a_0-a_2c_1\in L .
\tag{6}
\]
At every geometric root of \(R\), one has \(x^2=-c_1\), so
\(y=y_c\) and \(\vartheta=V_c\). In the cusp case there is one
double root; in the other case there are two distinct roots over
an algebraic closure. The stated values hold in both cases.

## 3. The monic center fiber, including its multiplicity

The fiber calculation can be made completely explicit. Define
\[
J(V)=a_0+\frac{a_2}{A_2}(V-c_0),\qquad
G(U,V)=(U-J(V))^2
       -\frac{a_3^2}{A_2^3}(V-c_0)(V-V_c)^2 .
\tag{7}
\]
Indeed \(y-J(\vartheta)=a_3x(x^2+c_1)\), and (6) makes (7)
vanish at \((y,\vartheta)\). This monic U-quadratic is
irreducible over \(L(V)\): its discriminant has odd valuation at
\(V=c_0\), either one or three according as \(V_c\ne c_0\)
or \(V_c=c_0\). It is therefore not a square in \(L(V)\).
Gauss's lemma identifies (7) with the selected monic relation.
It follows without any reduced-fiber assumption that
\[
G(U,V_c)=(U-y_c)^2 .
\tag{8}
\]
Thus the double value is an identity of monic polynomials over the
exact field \(L\), not just a statement about geometric points.

By (2) and (8), \((U-y_c)^2\) divides \(p(U)^2\), so \(p(y_c)=0\).
Since \(p\) is quadratic and squarefree, its other root \(y_s\)
also lies in \(L\), and differs from \(y_c\). Write
\[
p(U)=\frac h2(U-y_c)(U-y_s),\qquad
A_0:=\frac{h^2}{4\rho^3}\ne0,
\qquad Q_1(U,V_c)=A_0(U-y_s)^2 .
\tag{9}
\]
The cofactor identity follows by polynomial division of the exact
center identity in (2), not by dividing values at its roots.

## 4. Cofactor support contradicts the squarefree center

At every geometric root of \(R\), (6) and (9) give
\(Q_1(y,\vartheta)=A_0(y_c-y_s)^2\ne0\).
Thus the polynomials \(Q_1(y,\vartheta)\) and \(R\) have no common
root over an algebraic closure and are coprime in \(L[v]\).
The divisibility in (2) consequently forces
\[
Q_1(y,\vartheta)=\beta\in L^*.
\tag{10}
\]

The full plane evaluation ideal is \((G)\), so
\(Q_1-\beta\in(G)\) in \(L[U,V]\).
Both \(Q_1\) and \(G\) have total degree three, and subtracting a
constant does not change that degree. Total degrees add under
multiplication in the polynomial domain; therefore the quotient
is a nonzero scalar \(\alpha\in L^*\). In particular
\[
Q_1=\alpha G+\beta,
\qquad \mathcal H=\alpha G^2+\beta G,
\qquad \alpha=A_0 .
\tag{11}
\]
The last equality compares the U-fourth coefficients, since \(G\)
is monic of U-degree two and the U-fourth coefficient in (2) is
exactly \(A_0\), independent of \(V\).

Specialize (11) at \(V=V_c\), using (8) and (9):
\[
A_0(U-y_s)^2=A_0(U-y_c)^2+\beta .
\tag{12}
\]
Comparison of the coefficients of \(U\), in characteristic zero
and with \(A_0\ne0\), forces \(y_s=y_c\). This contradicts the
squarefree assumption. The degree pair (3) is excluded.

## 5. Consequence and scope

Together with the separate
[degree-six/four exclusion214](rank-two-quadratic-center-six-four-exclusion-pass214-working.md),
this leaves only \((d,e)=(2,1)\) from the quadratic-center list213.
This note does not decide that remaining pair or make any assertion
about the linear center. It does not infer an ambient invariant
coordinate from the node/cusp description of \(C\).

The scalar determinant enters only through the actual cofactor
support proved in212. No additional Jacobian identity, guessed
lower potential, rationality of \(L\), or original-ring descent is
assumed here. The exact conductor and the nonreduced center fiber
have both been proved in the note.
No saved checker was executed, imported or compiled, and no earlier
source, index or verification packet was changed. This bounded
exclusion is not a proof of unrestricted cancellation, arbitrary
coordinate entry, or historical novelty.
