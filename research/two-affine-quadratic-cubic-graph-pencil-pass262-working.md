# A polynomial-pencil endpoint for the quadratic-cubic graph

In the actual maximal height-two chart258, assume zero coupling,
nonzero \(\nu=n_\lambda\), and \(q'''\ne0\). Then the original
polynomial ring has an invariant coordinate, and its globally
sliced kernel is \(\mathbb C^{[3]}\). The coefficient \(\nu\) may
depend on both coefficient parameters and need not be a complex unit.

The proof replaces the coefficient parameter \(\lambda\) by \(n\),
without an ambient coordinate change. Three exact scalar coefficients
force a polynomial presentation over a curve field. The actual field
return then makes this a degree-one generic pencil. Finally, the
full calibrated determinant proves that a correction initially
constructed over that curve field has complex coefficients.

This is a conditional endpoint for the specified branch of258,
not recognition of every quadratic-cubic frame or an entry theorem.

## 1. Actual chart and exact fields

Use the fully read
[quadratic-cubic frontier258](two-affine-quadratic-cubic-frontier-pass258-working.md).
In particular, assume
\[
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\quad a=EX\ne0.
\tag{1}
\]
The full weighted initial kernel has height two, the good leading
ratio \(t\) is nonconstant, and the literal selected partial
\(\partial_Z\) has exact shift three. Its intrinsic LND supplies
\[
[L:\mathbb C(t,\lambda)]<\infty,\quad K=L(v),\quad Nv=1,
\quad L[y,z,w]=L[v],\quad K=\mathbb C(y,z,w).
\tag{2}
\]
The last equality is essential. Whole-line return after adjoining
\(L\) alone does not imply the pencil argument below.

The actual fixed-\(X\) expansions and calibration are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}&=-a^3\in L^*.
\end{aligned}
\tag{3}
\]
Here \(q,r\) are algebraic over \(\mathbb C(t)\), and the
commuting coefficient partials on \(L\) initially fix \(v\).
Assume \(m=k_\lambda=0\). Set
\[
F=\ker_L\partial_\lambda.
\qquad [F:\mathbb C(t)]<\infty,\quad
\ker_F(d/dt)=\mathbb C,\quad q,r,k\in F.
\tag{4}
\]
Primes mean the extended \(t\)-derivative on \(F\).
To justify (4), differentiate the monic minimal polynomial of an
element of \(\ker_L\partial_\lambda\) over
\(\mathbb C(t,\lambda)\). Minimality forces every coefficient
derivative to vanish, so the polynomial has coefficients in
\(\mathbb C(t)\). Thus \(F/\mathbb C(t)\) is algebraic.
Finite subextensions have bounded degree, since adjoining the
transcendental \(\lambda\) preserves those degrees and puts them
inside the given finite extension \(L/\mathbb C(t,\lambda)\).
This proves finiteness. The same minimal-polynomial argument for
the prime derivative gives its constant field \(\mathbb C\).
No equality \(F=\mathbb C(t)\) is assumed.

The zero-coupling branch of258 with \(\nu\ne0\) gives
\[
\begin{aligned}
\nu&=n_\lambda\ne0,\qquad
f(U)=q''U^2/2+k'U+n,\qquad B_1(U)=f_t(U),\\
P(U)&=q'''U^3/6+(k''-r''\nu)U^2/2+n_tU,\\
G_{\mathrm{old}}(U)&=(\ell-P(U))/\nu,\qquad
z=f(y),\quad\theta=G_{\mathrm{old}}(y),\\
w&=\sum_{j=1}^6w_jy^j+w_0,\qquad
\partial_U\left(\sum_{j=1}^6w_jU^j\right)
  =(G_{\mathrm{old}})_t-(B_1/\nu)(G_{\mathrm{old}})_\lambda,
\qquad w_0\in L.
\end{aligned}
\tag{5}
\]
All formal coefficient partials hold \(U\) fixed. Whole-line
return forces \(y\) affine in \(v\), with \(y_v\in L^*\).
Changing only that coefficient-field parameter, the full chain
rule gives
\[
\mathcal J_\lambda:=
 \det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,y)}
 =-a^3/y_v\in L^*,
\qquad
\mathcal J_\lambda=B_1(y)w_\lambda-\nu w_t.
\tag{6}
\]
This determinant is independent of both \(X\) and \(y\).
The right-hand expression is its value at \(X=0\), with the
partial derivatives now holding \(y\) fixed.

If \(q'''=0\), exact integration over (4) makes \(q\) a complex
quadratic polynomial. Its homogenization \(\widehat q_2(X,Y)\)
gives an actual elementary correction
\(Z\mapsto Z-\widehat q_2(X,Y)\) of time degree at most one,
with polynomial inverse. The proof below assumes \(q'''\ne0\)
and does not rely on a recognition theorem for that lower profile.

## 2. Replace the coefficient parameter by \(n\), not an ambient variable

Write the old coefficient derivatives on \(L\) as
\(\partial_t^{\,o},\partial_\lambda\). Since \(n_\lambda\ne0\),
the element \(n\) is transcendental over \(F\): otherwise
separability of its minimal polynomial over \(F\) would force
\(n_\lambda=0\). The field \(L\) is finite over \(F(n)\), and
also finite over \(\mathbb C(t,n)\). Indeed these extensions are
algebraic and finitely generated, since \(t,n\) form a
transcendence basis of \(L/\mathbb C\).

Define on this exact field
\[
\partial_n=\nu^{-1}\partial_\lambda,\qquad
\partial_t=\partial_t^{\,o}
              -\frac{\partial_t^{\,o}n}{\nu}\partial_\lambda.
\qquad
\ker_L\partial_n=F.
\tag{7}
\]
These are the unique extensions of the two partials on
\(\mathbb C(t,n)\). They commute: their bracket is zero on
\(\mathbb C(t,n)\), and a derivation of a finite separable
extension that kills the base field is zero. On \(F\), the new
\(\partial_t\) is the same prime derivative as in (4).

Let \(H=\lambda\), viewed as an element of \(L\) over \(F(n)\),
and put
\[
c=q'''\ne0,\quad b=k'',\quad d=r'',\quad
T=H_n\ell,\quad h(U)=cU^2/2+bU.
\qquad H_n=\nu^{-1}\ne0.
\tag{8}
\]
Subscripts from this point mean the new commuting \(t,n\)
derivatives, with formal \(U\) fixed. In particular,
\(\partial_t^{\,o}n=-H_t/H_n\).
Substitution into (5) gives exactly
\[
\begin{aligned}
G(U)&=T+H_tU+\frac{d-H_nb}{2}U^2-\frac{H_nc}{6}U^3,
       \qquad \theta=G(y),\\
w_U&=G_t-hG_n,\\
\mathcal J_n:=
 \det\frac{\partial(Y,Z,W)}{\partial(t,n,y)}
 &=\mathcal J_\lambda/\nu
   =-\frac{a^3}{\nu y_v}\in L^*,
\qquad \mathcal J_n=h(y)w_n-w_t .
\end{aligned}
\tag{9}
\]
Here \(w_U\) denotes the derivative of its formal polynomial
representative, and the determinant remains independent of
\(X,y\). For the middle identity, the old \(G_t\) becomes
\(G_t-(H_t/H_n)G_n\), while
\(B_1=h-H_t/H_n\) and \(G_\lambda=G_n/H_n\).
The two \(H_t/H_n\) contributions cancel. The parameter-change
Jacobian from \((t,\lambda,y)\) to \((t,n,y)\) is \(\nu\);
no speed is silently set equal to one.

## 3. Three scalar coefficients force polynomiality over \(F\)

Formal integration of the middle identity in (9), with zero
constant term, gives the complete coefficient list
\[
\begin{aligned}
w_1&=T_t,\\
w_2&=(H_{tt}-bT_n)/2,\\
w_3&=(-3bH_{nt}-cT_n-H_nb'+d')/6,\\
w_4&=(3b^2H_{nn}-4cH_{nt}-H_nc')/24,\\
w_5&=bcH_{nn}/12,\qquad w_6=c^2H_{nn}/72,
\end{aligned}
\quad
w(U)=w_0+\sum_{j=1}^6w_jU^j .
\tag{10}
\]
No restriction on \(H,T,w_0\in L\) has been imposed in this list.
Multiplying its formal coefficients in \(\mathcal J_n=hw_n-w_t\)
first gives
\[
[U^8]\mathcal J_n=c^3H_{nnn}/144.
\tag{11}
\]
Consequently \(H_{nnn}=0\). Exact integration using
\(\ker_L\partial_n=F\) gives
\[
H=\frac{A_2(t)}2 n^2+A_1(t)n+A_0(t),\qquad A_i\in F.
\tag{12}
\]
For example, \(H_{nn}\in F\); subtracting its quadratic
primitive leaves an element with zero second derivative,
and two further constant-field steps give (12).
There is no claim yet that \(L=F(n)\), and \(A_2\) may vanish.
The condition \(H_n\ne0\) only rules out both \(A_2,A_1\) being zero.

After (12), another literal coefficient of the same scalar is
\[
[U^5]\mathcal J_n
=-\frac{3A_2bc'+4A_2cb'+12bcA_2'+2c^2T_{nn}}{24}.
\tag{13}
\]
It follows that \(T_{nn}\in F\), and the same exact integration
argument proves \(T\in F[n]\), of degree at most two. Finally,
\[
[U^2]\mathcal J_n
=-\frac{n^2A_2'''+2nA_1'''+2A_0'''
             -6bT_{nt}-2T_nb'-2c(w_0)_n}{4}.
\tag{14}
\]
Since \(c\ne0\), this makes \((w_0)_n\) a polynomial in \(n\)
over \(F\), of degree at most two. Subtract its polynomial
primitive inside \(F[n]\); the remaining element of \(L\) is
in \(F\). Hence \(w_0\in F[n]\), of degree at most three.

All entries of (10) now belong to \(F[n]\). We obtain the exact,
uniform conclusion
\[
H,T\in F[n],\quad \deg_n H,\deg_n T\le2,\qquad
w\in F[n,y]=F[y,z],\quad z=q''y^2/2+k'y+n.
\tag{15}
\]
This includes both \(\nu_\lambda=0\) and the algebraic
square-root mode in the old parameter. It does not discard
either by a rational ansatz or an unjustified integration.

By the actual return in (2), (15) supplies both inclusions in
\[
\boxed{K=F(y,z)=\mathbb C(y,z)(w),\qquad w=\mathcal P(y,z),
       \quad \mathcal P\in F[U,V].}
\tag{16}
\]
The elements \(y,z\) are independent over \(F\). Indeed \(n\)
is transcendental over \(F\), \(y\) is transcendental over \(L\),
and \(F(y,z)=F(y,n)\). Only at this stage could one additionally
deduce \(L=F(n)\), by taking constants of the derivation on
\(K=L(y)=F(n,y)\) that kills \(L\) and sends \(y\) to one.
This equality was not used to derive (12)--(15).

## 4. A generic polynomial pencil has one simple pole

Here is the curve-field lemma needed for arbitrary finite
polynomials, rather than only the four-term pencil in the
fully read [256](height-two-canonical-cubic-pencil-recognition-pass256-working.md).
Suppose \(F/\mathbb C\) is a one-variable function field,
\(U,V\) are independent over \(F\), and
\[
F(U,V)=\mathbb C(U,V)(\mathcal P(U,V)),\qquad
\mathcal P=\sum_{(i,j)\in S}c_{ij}U^iV^j\in F[U,V],
\tag{17}
\]
with a finite set of distinct exponent pairs. Then
\[
F=\mathbb C(\alpha),\qquad
\mathcal P=P_0+\alpha P_1,\qquad
P_0,P_1\in\mathbb C[U,V],\quad P_1\ne0
\tag{18}
\]
for some \(\alpha\in F\).

Take the nonsingular projective model of \(F\), provided by
[Stacks, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1).
Let \(D\) be the coefficientwise maximum polar divisor of the
\(c_{ij}\). After base change to \(\Omega=\mathbb C(U,V)\), its
top polar coefficient at any point of positive multiplicity is
a nonzero complex linear combination of the distinct monomials
\(U^iV^j\). It cannot vanish. The coefficients are regular off
the original finite support, so there are no other poles.
Thus \(\operatorname{Pole}(\mathcal P)=D_\Omega\).

For a nonconstant function on a nonsingular projective curve,
the degree of its pole divisor equals its function-field degree.
The pole divisor is the pullback of infinity; the equality follows
from [the pullback-degree formula, tag 0AYZ](https://stacks.math.columbia.edu/tag/0AYZ)
and [the field definition of degree, tag 02NY](https://stacks.math.columbia.edu/tag/02NY).
These exact primary statements were freshly read.
Equation (17) therefore gives \(\deg D=1\). It consists of one
simple complex point. Some coefficient is nonconstant, since
otherwise (17) would generate only \(\Omega\). Choose that
coefficient as \(\alpha\). Its single simple pole gives
\(F=\mathbb C(\alpha)\) by the same degree formula.
Every other coefficient has at most the same simple pole and
no others. As a rational function of \(\alpha\), it is affine.
This proves (18), without specialization of \(U,V\) or a prior
rationality assumption.

## 5. The scalar determinant makes the pencil direction constant

Apply Section 4 to (16), writing
\(w=P_0(y,z)+\alpha P_1(y,z)\), with \(\alpha'\ne0\) by (4).
In the new coefficient variables, \(z_n=1\) and \(z_t=h(y)\).
Cancellation of the common chain-rule terms gives
\[
\mathcal J_n=-\alpha'P_1(y,z).
\tag{19}
\]
Differentiate in \(y\) at fixed \(t,n\). The scalar is
independent of \(y\), so
\[
(P_1)_U+(q''U+k')(P_1)_V=0\quad\hbox{in }F[U,V].
\tag{20}
\]
This is a polynomial identity: substituting
\(V=q''y^2/2+k'y+n\) identifies \(F[U,V]\) with \(F[y,n]\).
Now differentiate (20) in \(t\), holding formal \(U,V\) fixed.
Because \(P_1\) has complex coefficients, this gives
\((q'''U+k'')(P_1)_V=0\). The assumption \(q'''\ne0\)
therefore makes \(P_1\) a nonzero complex constant.
Absorbing it into the curve parameter yields
\[
\boxed{w=P_0(y,z)+C(t),\quad P_0\in\mathbb C[U,V],\quad
C\in F,\quad C'\ne0,\quad \mathcal J_n=-C'.}
\tag{21}
\]
Here \(C(t)\) denotes an element of the exact finite curve field,
not necessarily a rational function of \(t\).
No coefficient-field parameter has yet been promoted to an
ambient polynomial coordinate.

## 6. The full determinant supplies the actual complex correction

Inside the formal polynomial ring \(F[X,Y,Z]\), define
\[
\begin{aligned}
\widehat y&=Y-tX,\\
\widehat z&=Z-(q'\widehat y+k)X-qX^2,\\
\widehat n&=\widehat z-q''\widehat y^2/2-k'\widehat y,\\
\widetilde P(X,Y,Z)&=P_0(\widehat y,\widehat z)
 +G(\widehat y,\widehat n)X
 +(r'\widehat y+H(\widehat n))X^2+rX^3.
\end{aligned}
\tag{22}
\]
Both \(H\) and \(G\) are now polynomials in \(n\) over \(F\),
the latter also polynomial in its formal projection variable,
by (9),(12),(15). Hence (22) is polynomial over \(F\).
The literal expansions (3) give
\[
W=C+\widetilde P(X,Y,Z).
\tag{23}
\]

It remains to prove that the coefficients of this correction
are complex. For fixed \(X\), the first two literal rows give
\[
\det\frac{\partial(t,Y,Z)}{\partial(t,n,y)}=-1.
\tag{24}
\]
Indeed the first row is \((1,0,0)\), and \(Y_n=0\), \(Y_y=1\),
\(Z_n=1\). The other entries contain moving coefficients but
do not contribute to this determinant.
By (9),(21), the full determinant of \((Y,Z,W)\) with respect
to \((t,n,y)\) is \(-C'\) for every \(X\), not just at \(X=0\).
Its determinant with respect to \((t,Y,Z)\) is
\(\partial_t W|_{X,Y,Z}\), with positive sign.
The chain rule therefore gives
\[
\left.\partial_t W\right|_{X,Y,Z}=C',
\qquad
\left.\partial_t\widetilde P\right|_{X,Y,Z}=0.
\tag{25}
\]

The three elements \(X,Y,Z\) are independent over \(F\).
In fact (22) and the first two rows of (3) are inverse
triangular polynomial maps between \(F[X,Y,Z]\) and
\(F[X,y,n]\); these last three variables are independent over
\(F\). Thus (25) kills every coefficient of \(\widetilde P\).
By (4), \(\widetilde P\in\mathbb C[X,Y,Z]\).

We have constructed the actual invariant coordinate
\[
I=W-\widetilde P(X,Y,Z)=C\in B\cap\operatorname{Frac}A,\quad
EI=0,\qquad B=\mathbb C[X,Y,Z,I].
\tag{26}
\]
The polynomial inverse is \(W=I+\widetilde P(X,Y,Z)\), with
\(X,Y,Z\) retained. Substitution in either order returns all
four coordinates. The field computations do not impose a
nonconstant denominator on this final actual map.

The kernel \(A\) is regular, since \(A[u]=B\) is regular
and regularity descends along this faithfully flat polynomial
extension. It is finitely generated, since \(A\simeq B/(u)\).
Apply the freshly read
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
to the nonzero LND on \(\mathbb C[I,X,Y,Z]\) fixing \(I\)
and having regular kernel. It gives
\[
\boxed{A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.}
\tag{27}
\]

## 7. Scope and provenance

This proves the actual endpoint when \(m=k_\lambda=0\),
\(\nu=n_\lambda\ne0\), and \(q'''\ne0\) in the supplied
maximal height-two quadratic-slot chart258. It includes both
affine and quadratic \(\lambda=H(t,n)\), without assuming
\(\nu\) constant or discarding a square-root mode in the old
parameter. The observation for \(q'''=0\) gives a separate
actual degree-lowering map; any recognition of the resulting
lower profile is a retained input, not proved here.

Other height-two shifts, nonzero coupling, principal initial
kernels and arbitrary-coordinate entry remain outside this
note. The full equality \(K=\mathbb C(y,z,w)\), the exact
finite coefficient field and the scalar calibration for every
\(X\) are essential. None can be replaced by just a generic
plane presentation or a scalar computation at \(X=0\).

The complete258 and256 sources were reread. Unsaved independent
coefficient calculations reconstructed every entry of (10) and
the three scalar coefficients (11),(13),(14) directly from (9).
Such calculations do not certify the curve-field argument or
the published recognition theorem. The primary curve-degree
facts and the exact regular-kernel theorem were freshly read.
No earlier source or packet was edited, and no saved checker
was executed, imported or compiled. No historical novelty,
human expert certification, arbitrary-entry theorem or
unrestricted cancellation result is claimed.

