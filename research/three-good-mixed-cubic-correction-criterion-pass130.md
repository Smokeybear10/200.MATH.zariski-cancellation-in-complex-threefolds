# Correcting a mixed cubic relation to an invariant coordinate

A supplied mixed cubic leading relation has two exact derivative
tests: remove its second derivative and remove its remaining
speed. Passing both tests automatically produces an actual
invariant coordinate and recognizes the kernel as a polynomial
threefold. The automatic step is the
[invariant linear-suspension theorem](invariant-linear-suspension-recognition-pass130.md).
The two tests are invariant under affine changes and fixed-good
quadratic shears. For a primitive cubic relation the corrections
are unique, apart from an additive constant.
An exact plane-residue coordinate test remains a useful finite
diagnostic, but is not a third independent obstruction here.

These are conditional criteria for a specified relation in an
actual three-good frame. Neither existence of that relation nor
passage of the tests is assumed to be universal.

## 1. The actual frame and the first derivative obstruction

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
E\in\operatorname{LND}(B),\qquad A=\ker E,\qquad Eu=1,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad
E^2z=q\ne0,\qquad E^3z=0,\qquad
\operatorname{trdeg}_{\mathbb C}\mathbb C[a_1,a_2,a_3]=2.
\end{gathered}
\tag{1}
\]
All four displayed generators are polynomial coordinates.
Suppose that the cone over the speed image is dense in
\(\mathbb A^3\), meaning that no nonzero homogeneous polynomial
over \(\mathbb C\) vanishes on \(a=(a_1,a_2,a_3)\).
This is the nonconical hypothesis used below. A unit speed ideal
can additionally be imposed, but none of the criteria uses it.

Write \(R=\mathbb C[x_1,x_2,x_3]\), let \(R_j\) be its homogeneous
degree-\(j\) subspace, and put
\(W_1=\operatorname{span}_{\mathbb C}\{a_i\}\) and
\(W_2=\operatorname{span}_{\mathbb C}\{a_i a_j:i\le j\}\).
Evaluation \(G\mapsto G(a)\) is injective on every \(R_j\).
Indeed this is exactly the homogeneous-density assumption.
Also \(\deg_E G=\deg G\) for every nonconstant \(G\in R\):
writing \(x_i=b_i+a_i u\), its highest coefficient is \(G_{\deg G}(a)\).

Let \(L\in R_1\setminus\{0\}\) and \(F_3\in R_3\) satisfy
\[
\begin{gathered}
L(a)q=2F_3(a),\qquad H=L(x)z-F_3(x),\qquad E^3H=0,\\
\sigma:=E^2H
=qL(x)+2L(a)Ez-\operatorname{Hess}F_3(x)[a,a]\in A.
\end{gathered}
\tag{2}
\]
Here \(\operatorname{Hess}F_3(x)[a,a]=
\sum_{i,j}(F_3)_{ij}(x)a_i a_j\).
The product rule gives the second line. A third derivative
gives \(3L(a)q-6F_3(a)=0\), which proves the first line's
degree assertion. In particular \(L(a)\ne0\) and \(F_3\ne0\).
The expression \(H\) has not been assumed to be a coordinate.

## 2. The two correction tests and their exact meaning

Seek constants \(\rho,G_0\in\mathbb C\), \(G_2\in R_2\), and
\(G_1\in R_1\). Set \(K=H+\rho z-G_2(x)\). Then
\[
\begin{gathered}
\text{first test:}\quad
\sigma+\rho q=2G_2(a),\\
\text{second test:}\quad EK=G_1(a),\\
I=H+\rho z-G_2(x)-G_1(x)-G_0\in A
\quad\Longleftrightarrow\quad
\text{both tests hold}.
\end{gathered}
\tag{3}
\]
The first equality is precisely \(E^2K=0\).
After it holds, \(EK\in A\), and the second equality is
precisely \(E(K-G_1)=0\). Conversely an invariant \(I\)
of this form has both equalities after differentiation.
The first test is equivalent to \(\sigma\in\mathbb Cq+W_2\),
not to \(\sigma\in W_2\).

Equivalently, (3) asks whether the affine coset
\(\mathcal C_H=H+\mathbb Cz+R_{\le2}\) meets \(A\).
This interpretation does not depend on choices of homogeneous
pieces after translating the good variables.
It involves seven unknown constants in the first test
and three in the second, with equations obtained by polynomial
coefficient comparison. The constant \(G_0\) is unrestricted.
Every resulting \(I\) is nonconstant: its original total-degree
three part is \(-F_3\), which cannot be canceled by the allowed
lower-degree corrections.

## 3. Primitivity, uniqueness, and changes of frame

Call the mixed leading relation primitive when
\(\gcd(L,F_3)=1\) in \(R\).
In this case \(q\notin W_2\). For otherwise
\(q=2J_2(a)\) for some \(J_2\in R_2\), and (2) plus
homogeneous injectivity gives \(F_3=LJ_2\), a contradiction.
Consequently any two first corrections have
\((\rho-\widetilde\rho)q=2(G_2-\widetilde G_2)(a)\);
first \(\rho=\widetilde\rho\), then \(G_2=\widetilde G_2\).
The second correction \(G_1\) is also unique.
Thus a fixed primitive \(H\) has at most one invariant
lift modulo constants.

There is at most one mixed relation up to nonzero scalar
when \(q\notin W_2\). For two pairs \((L_i,F_i)\),
evaluation gives \(L_2F_1=L_1F_2\) as a homogeneous identity.
If \(L_1,L_2\) were independent, they would be coprime,
forcing \(F_1=L_1J_2\) and then \(q=2J_2(a)\).
Therefore the two \(L_i\), and then the two \(F_i\),
are proportional. When it exists and passes (3), the invariant
is consequently unique up to nonzero scalar and additive constant.

For a good translation \(x'=x+c\), transport the same
homogeneous forms to the new variables. Taylor expansion gives
\[
\begin{gathered}
H'=H+L(c)z-
 \bigl(F_3(x+c)-F_3(x)\bigr),\\
\sigma'=\sigma+L(c)q-2\,dF_3(a)[c].
\end{gathered}
\tag{4}
\]
The parenthesized polynomial has good degree at most two,
and \(dF_3(a)[c]\in W_2\).
Thus \(\mathcal C_{H'}=\mathcal C_H\).
For a bad affine shear \(z'=z+\ell(x)+e\), the difference
is \(H'-H=L\ell+eL\in R_{\le2}\), and
\(\sigma'-\sigma=2L(a)\ell(a)\in W_2\).
Invertible linear changes of the good variables simply
reexpress all these spaces. Scaling the bad variable can
be compensated by scaling \(L\).

The same coset statement holds for a fixed-good quadratic
shear \(z'=z+J_2+J_1+J_0\): use
\(F_3'=F_3+LJ_2\), so
\(H'-H=LJ_1+LJ_0\in R_{\le2}\).
The acceleration changes by \(2J_2(a)\), and \(W_2+\mathbb Cq\)
is unchanged. These transformations preserve both correction
tests, their invariant lifts, and the coordinate property
of those lifts.

They exhaust the polynomial frame changes that keep the good
ring \(R\) fixed and preserve the three-good quadratic profile.
Indeed new good generators in \(R\) must be affine-linear by
degree preservation. An alternative polynomial generator of
\(B=R[z]\) is \(\kappa z+G(x)\), with
\(\kappa\in R^*=\mathbb C^*\). Degree preservation forces
\(\deg G\le2\) if its \(E\)-degree is at most two.
No invariance under arbitrary changes involving a new good
ring is asserted.

## 4. Where the corrections lie in the intrinsic quotient

Let \(T=\partial_z\). The
[intrinsic-speed construction](three-good-intrinsic-speed-quotient-pass125.md)
and [rank-sensitive cofactor bound](three-good-flow-cofactor-bounds-pass126.md)
give an exact shift \(0\le d\le2\) with
\[
\begin{gathered}
T(A)\subset A[u]_{\le d},\qquad Tu\in A[u]_{\le d},\qquad
N(f)=[u^d]T(f)\quad(f\in A),\\
0\ne N\in\operatorname{LND}(A),\qquad
S=\ker_A N\simeq\mathbb C^{[2]},\qquad a_i,q\in S.
\end{gathered}
\tag{5}
\]
The polynomial-plane identification is the retained
intrinsic quotient theorem, not a consequence of the rank
calculation alone.
Here \(d\ne0\): otherwise \([E,T]=0\), so \(T(a_i)=0\)
and \(a_i\in R\). Since \(Ea_i=0\), degree preservation
would make every \(a_i\) constant, contrary to rank two.
Thus \(d=1\) or \(2\).

The identity \(TH=L(x)\) has \(E\)-degree at most one.
Write \(H=h_0+h_1u+\sigma u^2/2\). Its possible coefficient
of \(u^{d+2}\) under \(T\) is \(N(\sigma)/2\), because
\(\deg_u Tu\le d\). Hence \(N(\sigma)=0\).
If the first correction succeeds, write
\(K=k_0+\eta u\), with \(\eta=EK\).
Now \(TK=L(x)+\rho\); its coefficient of \(u^{d+1}\)
is \(N(\eta)\). Since \(d\ge1\), it also vanishes.
Therefore \(\sigma,\eta\in S\).
This last comparison would not justify \(N(\eta)=0\)
in an arbitrary shift-zero frame.

For a fully corrected invariant \(I\), set \(Q=[E,T]\).
The exact further identities are
\[
\begin{gathered}
TI=L(x)+\rho,\qquad QI=L(a),\\
d=2\ \Longrightarrow\ NI=0\ \text{ and }I\in S,\\
d=1\ \Longrightarrow\ NI=L(a)\ne0,\qquad N^2I=0.
\end{gathered}
\tag{6}
\]
They follow by comparing the coefficients of \(u^2\) or
\(u\) in \(T|_A\), respectively, and by applying \(E\)
to \(TI\). In the second case \(I\) is an explicit local
slice for \(N\), not necessarily a global slice.

## 5. The automatic coordinate conclusion and its diagnostic

Suppose (3) holds. Put \(w=L(x)+\rho\), and complete it
by two affine-linear good coordinates \(y,t\).
Then for a polynomial \(g\) of total degree at most three,
\[
I=wz-g(w,y,t),\qquad g_0(y,t)=g(0,y,t),\qquad
I\text{ is a coordinate of }B
\quad\Longleftrightarrow\quad
g_0\text{ is a coordinate of }\mathbb C[y,t].
\tag{7}
\]
In the present sliced frame, the right-hand side of (7)
is automatic once (3) holds. Indeed write \(g=wJ+g_0\)
and make the actual triangular shear \(z_1=z-J(w,y,t)\).
Then \(I=wz_1-g_0(y,t)\), while
\(E^2w=0\) and \(Ew=L(a)\ne0\).
The
[invariant linear-suspension theorem](invariant-linear-suspension-recognition-pass130.md)
proves that \(g_0\) is a plane coordinate and that \(I\)
is an ambient coordinate. That theorem needs no bound on
the new bad coordinate's \(E\)-degree.
This application does not use primitivity or the intrinsic
quotient construction in Section 4.

For clarity, (7) is also an exact algebraic diagnostic
without this automatic argument.
For necessity, an ambient coordinate \(I\) gives
\(B/(I)\simeq\mathbb C^{[3]}\).
Bhatwadekar--Gupta--Lokhande, Corollary 4.5 with exponent
one, identifies this with the plane-coordinate condition
in (7). Its statement imposes no prior irreducibility
assumption on \(g_0\). [Corollary 4.5](https://arxiv.org/pdf/1501.01438)

The converse has an explicit inverse. Write \(g=wJ+g_0\),
set \(z_1=z-J(w,y,t)\), and choose plane coordinates
\((v,r)=(g_0(y,t),r(y,t))\). Now
\(I=wz_1-v\), so \((w,r,z_1,I)\) are actual coordinates:
recover \(v=wz_1-I\), apply the polynomial plane inverse
to recover \(y,t\), and recover \(z=z_1+J(w,y,t)\).
No division by \(w\) is used.

For \(\deg g_0\le3\), the plane test itself is equivalent to
\[
\exists\,\mu,\nu\in\mathbb C:\quad
\mu(g_0)_y+\nu(g_0)_t=1.
\tag{8}
\]
This is the elementary degree-three plane-curve lemma in
[the cubic linear-variable criterion, Section 2](cubic-linear-variable-pass.md).
Briefly, a coordinate's zero fiber is an embedded affine
line of degree at most three. Its parametrization degrees
can be reduced by an affine-linear plane change; the only
case without a linear parameter would have degrees
\((3,2)\), reducible to \((\alpha s^3+\beta s,s^2)\).
If \(\beta\ne0\), two nonzero opposite parameters coincide
in the image; if \(\beta=0\), the differential vanishes
at zero. Both contradict an embedding. The fiber is
therefore an affine-linear graph, giving a constant
nonzero direction, which can be normalized to (8).
Conversely (8) integrates in affine-linear coordinates
to \(g_0=v+P(r)\), giving a polynomial plane inverse.
A zero or constant \(g_0\) correctly fails this diagnostic;
the automatic theorem excludes it after both tests in (3)
have passed under the actual hypotheses.

Once (7) succeeds, \(E\) fixes an actual ambient coordinate.
The ring \(A\) is regular because \(A[u]\) is polynomial.
The regular-kernel coordinate theorem then gives
\(A\simeq\mathbb C^{[3]}\).
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/pdf/1501.01438)
Thus both derivative tests suffice for recognition here,
using the cited topological and plane-curve inputs in the
automatic theorem and the regular-kernel theorem at the
final step. Corollary 4.5 is needed for the independent
necessity statement in the diagnostic (7), not for the
automatic implication.

## 6. Actual controls separating the tests

First take the inverse-verified cubic frame
[from129](three-good-cubic-acceleration-span-obstruction-pass129.md)
and translate its good slice coordinate by \(c\ne0\):
\[
\begin{gathered}
X=u+c,\quad Y=v+au,\quad Z=a-v^3/2+bu,\\
z=b+3av^2/2+3a^2vu/2+a^3u^2/2,\qquad q=a^3,\\
H=Xz-Y^3/2=Z-a+cz,\qquad \sigma=ca^3\notin W_2.
\end{gathered}
\tag{9}
\]
This is an actual affine change of129; its polynomial
inverse is obtained by using \(u=X-c\) in that inverse.
The speeds remain \((1,a,b)\), and \(W_2\) consists of
polynomials of degree at most two in \(a,b\).
The first test succeeds uniquely with \(\rho=-c,G_2=0\).
The second uses \(G_1=Z\), and the invariant is \(-a\).
Thus raw \(\sigma\notin W_2\) is an origin-dependent
obstruction, not failure of the invariant correction test.

The second test is genuinely additional for a fixed
nonprimitive relation. In \(\mathbb C[a,b,c,u]\) take
\[
\begin{gathered}
X=u,\quad Y=a+bu,\quad Z=c+au,\quad z=b+u^2/2,\\
b=z-X^2/2,\quad a=Y-bX,\quad c=Z-aX,\quad u=X,\\
(EX,EY,EZ)=(1,b,a),\quad q=1,\quad
H=Yz-YX^2/2=bY,\quad \sigma=0.
\end{gathered}
\tag{10}
\]
The displayed inverse verifies both orders directly.
Every first correction is \(G_2=\rho X^2/2\).
Its remaining speed is \(E(bY+\rho b)=b^2\), outside
\(\operatorname{span}_{\mathbb C}\{1,b,a\}\).
Thus no allowed second correction works for this fixed \(H\).
Here \(L=Y\) divides \(F_3=YX^2/2\), and \(q\in W_2\).
This example does not refute the primitive-cubic case
or existence of some other useful relation; indeed the
bad quadratic itself is removable.

Finally the exact residue test is stronger than testing
constant ambient directional derivatives of \(I\).
In129 replace its bad coordinate \(W\) by \(W'=W+Z^2\).
Both inverse orders remain polynomial, using \(W=W'-Z^2\).
The primitive relation and corrected invariant are
\[
\begin{gathered}
q'=a^3+2b^2,\qquad
H'=XW'-(Y^3/2+XZ^2),\qquad I=H'-Z=-a,\\
w=X,\quad g=Y^3/2+XZ^2+Z,\quad
g_0=Y^3/2+Z.
\end{gathered}
\tag{11}
\]
Both correction tests pass, and the plane residue is a
coordinate because its \(Z\)-derivative is one.
The four derivatives of \(I\), in the order
\((X,Y,Z,W')\), are
\(W'-Z^2,-3Y^2/2,-2XZ-1,X\).
Comparing the coefficients of \(W',Y^2,XZ,X\) proves
that no nonzero constant ambient direction has a
nonzero constant derivative on \(I\).
Nevertheless the inverse in Section 5 applies directly:
\(z_1=W'-Z^2,\ v=Y^3/2+Z,\ r=Y,\ I=Xz_1-v\).
Thus replacing the residue test by that directional
certificate would lose actual positive cases.

The two derivative tests concern the specified mixed relation
and the invariant it can produce. They give no
universal existence theorem for a mixed cubic leading
relation, no assertion that both tests pass in the
primitive class, and no unrestricted frame-entry or
cancellation conclusion.
