# Excluding the exceptional quadratic equal-degree direction

Working exclusion under the complete supplied actual264 chart, with
k=s and n_ss nonzero. The exceptional direction delta=beta=0 in407
cannot occur. This is an exclusion of that specific remaining
quadratic branch, not of the nonexceptional higher-degree profiles.

The proof first uses the actual all-X polynomial return to fix an
affine offset. Several coefficients of the full calibrated scalar
then force an exact finite family whose literal determinant is not
a coefficient scalar. No coefficient-field parameter is promoted to
an original coordinate, and no degree-one conductor theorem is used.

## 1. Complete actual input and the exceptional family

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the exceptional conclusion of
[407, Sections4--6](principal-paraboloid-equal-degree-higher-rank-split-pass407-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A_0[u_0],\qquad E=\partial_{u_0},
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\qquad
0\ne N=[u_0^4]\partial_Z|_{A_0},\\
L=\operatorname{Frac}\ker_{A_0}N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Nv_0=1,\quad a_0=EX\in L^*,\\
O=L[v_0]=L[y,\sigma,\theta]=L[y,z,w],\qquad
K=L(v_0)=\mathbb C(y,z,w),\\
J_{t,s,v_0}(X)=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
All genuine levels, their full evaluated unit ideals, and the exact
coefficient partials are retained. These partials commute and have
joint constants C. The original notation w in the intercept return
will not be used for the coefficient difference introduced below.

The exceptional branch has
\[
\begin{gathered}
\deg\sigma=\deg\theta=2,\quad
\lambda=\nu=n_s=:\xi,\quad \beta=n_{ts}+n_{ss}\mu=0,\quad
e=n_{ss}\ne0,\\
u_1=y-\xi\sigma,\qquad v_1=\theta-\mu\sigma,\qquad
O=L[u_1,v_1],\qquad \max(\deg u_1,\deg v_1)=1.
\end{gathered}
\tag{2}
\]
Use the exact separating basis(t,xi), with dot denoting the t
partial at fixed xi and prime the xi partial at fixed t. Thus
dot=old partial_t+mu*old partial_s, and prime=e^{-1}old partial_s.
Let F=ker(dot). From407 there are A,B in F with
\[
\begin{gathered}
s=-2\xi t^2-A't-B',\qquad \mu=-4\xi t-A',\\
n=-\xi^2t^2+(A-\xi A')t+B-\xi B',
\qquad a:=n_t^{\rm old}=2\xi^2t+A .
\end{gathered}
\tag{3}
\]
The field F is stable under primes; t is transcendental over F.
No equality F=C(xi) or L=F(t) is assumed.

Write the existing functions in407 as
\[
\begin{gathered}
u=(A''-\omega)/4,\quad v=(A''+\omega)/4,\quad
\varepsilon=v-u=\omega/2\ne0,\\
T_-=t+u,\quad T_+=t+v,\qquad
e=-\frac1{2T_-T_+},\quad
j=\frac{J}{T_-^2},\\
J,\omega\in F^*,\quad u,v\in F,\qquad
A''=2(u+v),\quad B''=2uv .
\end{gathered}
\tag{4}
\]
Here u,v are coefficient functions, not u0 or v0. They may be
zero. Both T signs are nonzero because t is transcendental over F.
The full third level is
\[
j\sigma+u_1^2+a u_1+\frac e2v_1^2-Cv_1+\xi\ell-h_0=0,
\qquad C=\ell_s^{\rm old}+\xi^2.
\tag{5}
\]
The line equation supplied by407 is
u1+v1/(2Tplus)=r0 for some r0 in L. Both u1 and v1 are therefore
affine, nonconstant intrinsic functions. The scalar j is nonzero.
Also j=-dot(ell)-mu*xi^2. Subtracting an explicit primitive gives
\[
\ell=2\xi^3t^2+\xi^2A't+\frac J{T_-}+\Lambda,
\qquad \Lambda\in F .
\tag{6}
\]
This is an identity of existing field elements, not an assumption
that arbitrary antiderivatives remain in L.

The necessary all-degree reduction
[413](principal-paraboloid-higher-degree-characteristic-zero-reduction-pass413-working.md)
is consistent with this branch. No degree-one scalar conclusion
from403 or405 is imported.

## 2. Actual all-X return fixes the affine offset

First record the exact polynomial-ring license. By264(4),
L[A0]=O inside K. Since X=a0*u0+b0 with a0 in L* and b0 in O,
\[
L[\mathcal B]=O[u_0]=O[X]=L[X,v_1].
\tag{7}
\]
Consequently every X0 in L gives
L[Y(X0),Z(X0),W(X0)]=L[v1]. This is specialization in a
coefficient-adjoined polynomial ring. It is not an ambient
coordinate change or a normality claim about an adjoined field.

Here is the divided-difference calculation needed for this branch.
Put h=v1 and write
\[
\sigma=p(h)=p_2h^2+p_1h+p_0,\qquad
y=\xi p+\alpha h+r_0,\qquad
\theta=\mu p+h,\quad
\alpha=-\frac1{2T_+}\ne0,\quad g=2r_0+a .
\tag{8}
\]
The coefficient p2 is nonzero. For two formal values h1,h2 put
S=h1+h2 and L1=p2*S+p1. If L1 is nonzero, specialize
X0=-xi-alpha/L1. The divided differences of the full literal
rows, after cancelling h1-h2, are
\[
\begin{aligned}
\Delta Y&=0,\\
\Delta Z&=L_1(p(h_1)+p(h_2)+\mu)+1,\\
\Delta W&=-L_1(g+\alpha S)
 -(2\xi L_1+\alpha)\bigl(p(h_1)+p(h_2)+\mu+L_1^{-1}\bigr).
\end{aligned}
\tag{9}
\]
These identities use both full potentials
z=2ty+sigma^2+theta+n and
w=ell-2sigma*y-a*sigma-xi*theta, with the actual X rows of264.

Suppose L1 were nonzero at S=-g/alpha. Since p2 is nonzero,
choose the product h1*h2 so that p(h1)+p(h2)=-mu-1/L1.
The two resulting roots exist over an algebraic closure of L.
If they are distinct, (9) makes all three specialized coordinate
values coincide, contradicting the equality in(7). If they
coincide, (9) instead says that all three specialized derivatives
vanish there. Differentiating a polynomial expression for h in
those three generators gives 1=0. The equality of polynomial
rings persists under this field extension. Thus
\[
p_2g=\alpha p_1.
\tag{10}
\]
This argument includes the repeated-root boundary; it does not
assume the chosen two points are distinct.

From(5),
p2=-(alpha^2+e/2)/j and p1=-(alpha*g-C)/j. Equation(10) gives
e*g+2alpha*C=0, or g=-2Tminus*C. Define the affine intrinsic
parameter
\[
q=\frac{v_1-C/e}{2T_+}.
\]
Then u1=-q-a/2 and v1=2Tplus*q+C/e. Completing the two squares
in(5) proves, with an unrestricted d0 in L,
\[
\boxed{\quad
\sigma=\frac{\varepsilon T_-}{J}q^2+d_0,\qquad
y=\xi\sigma-q-a/2,\qquad
\theta=\mu\sigma+2T_+q+C/e .
\quad}
\tag{11}
\]
In particular the actual level h0 and the affine offset have
not been discarded: their remaining freedom is contained in d0.
The relation O=L[q] is exact.

Let rho=Nq in L*. The coefficient and intrinsic parameter change
has determinant e*rho from(t,s,v0) to(t,xi,q). Therefore the full
new scalar satisfies
\[
\widehat J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,\xi,q)}
=-\frac{a_0^4}{e\rho}\in L^* .
\tag{12}
\]
All coefficient derivatives in this determinant hold the new
intrinsic q fixed. X remains the actual independent coordinate.

## 3. Complete compact rows with arbitrary remaining offset

Put
\[
\mathcal C=\frac J{T_-}+\Lambda,\qquad
d=d_0-\xi t-A'/2,\qquad
R=\sigma+tX-\xi t-A'/2
=\frac{\varepsilon T_-}{J}q^2+d+tX .
\tag{13}
\]
The letter R is a moving polynomial, not a replacement coefficient
parameter. The determinant remains in the basis(t,xi,q). Literal
substitution of(3),(6),(11) into the original three rows gives
\[
\begin{aligned}
Y={}&(X+\xi)(R+A'/2)-q-A/2,\\
Z={}&R^2+2v q+\mathcal C'+B-\xi B'-\xi^2B''
 -(A')^2/4-B'X,\\
W={}&-2\xi R^2+\bigl(2q-A'(X+\xi)\bigr)R
 +\bigl(A'+2v(X-\xi)\bigr)q-B'X^2\\
&+\bigl(\mathcal C'-\xi^2B''-(A')^2/2\bigr)X
 +\mathcal C-\xi\mathcal C'+\xi^3B'' .
\end{aligned}
\tag{14}
\]
Primes in this display act on the complete rational expression
J/(t+u), including u'. No derivative of a moving root is taken.

For an economical determinant expansion set
\[
\begin{aligned}
\mathcal T:=W+2\xi Z+A'Y
={}&2q\bigl(R+v(X+\xi)\bigr)-B'(X+\xi)^2\\
&+\bigl(\mathcal C'-\xi^2B''\bigr)(X+\xi)
 +\mathcal C+2\xi B-\xi^2B'-A'A/2 .
\end{aligned}
\tag{15}
\]
The third differential row can be replaced by
dTcal-(2Z+A''Y)d(xi), after adding 2xi times the Z row and
A' times the Y row. The subtraction is essential: Tcal has
coefficient functions, so it is not a constant row operation.
This identity together with(13)--(15) gives the coefficient
ledger below by direct differentiation.

## 4. Three scalar coefficients make u,v,J complex constants

Initially all u,v,J and Lambda are arbitrary elements of F subject
only to(4). The exact coefficient of X^0*q^4 is
\[
[X^0q^4]\widehat J
=\frac{2\varepsilon}{J^2T_-}
\left\{T_-\bigl[J(u'+v')+3J'\varepsilon\bigr]
       -5Ju'\varepsilon\right\}.
\tag{16}
\]
It must vanish. Comparing the t coefficient and constant over F
is valid because t is transcendental over F. Since J and epsilon
are nonzero, this gives
\[
u'=0,\qquad u\in\mathbb C,\qquad
v'=-3J'\varepsilon/J,\qquad
\varepsilon'=-3J'\varepsilon/J .
\tag{17}
\]
No division by u or v occurs. From this point write T=t+u;
because u is now complex, the exact prime and dot partials are
also the partials at fixed T and fixed xi respectively.

Keep d, dot(d), d' unrestricted. Define the full coefficient
\[
\begin{aligned}
M={}&TJ\left\{
A'(u+v)-2\varepsilon(T\dot d-d)-\Lambda''
 +(4u^2+6u\varepsilon)\xi
\right\}\\
&-6TJ'u\varepsilon\xi^2-JJ'' .
\end{aligned}
\tag{18}
\]
After precisely(17), with its derivative u''=0, the two
independent scalar coefficients are
\[
\boxed{\quad
[X^0q^3]\widehat J
=-\frac{2\varepsilon}{TJ^2}\bigl(M+4(J')^2\bigr),
\qquad
[Xq]\widehat J=-\frac{2(T+\varepsilon)}{T^2J}M .
\quad}
\tag{19}
\]
Both must vanish. The elements T and T+epsilon=Tplus are nonzero.
The second coefficient forces M=0; the first then forces J'=0.
Since J belongs to F, the joint-constant field gives J in C*.
Equation(17) then gives v'=0. Consequently
\[
u,v\in\mathbb C,\qquad J\in\mathbb C^*,\qquad
\varepsilon=v-u\in\mathbb C^* .
\tag{20}
\]
This comparison retains all coefficient-field derivatives until
they are forced to vanish. It is not a rational ansatz for F.

## 5. Exact lower integrations and the final full determinant

With(20), the next scalar coefficient is
\[
[X^0q^2]\widehat J
=-\frac{2\varepsilon}{T}(d'+v).
\tag{21}
\]
Thus d'=-v. Also A''=2(u+v), B''=2uv integrate exactly to
\[
A=(u+v)\xi^2+c_A\xi+d_A,\qquad
B=uv\xi^2+c_B\xi+d_B,
\quad c_A,d_A,c_B,d_B\in\mathbb C .
\tag{22}
\]
For example the first derivative of the difference between A and
its displayed quadratic is a joint constant. This proves(22)
inside the exact field, without identifying that field as rational.

Define the existing element f=d+v*xi, so f'=0. Now M=0 in(18)
reduces exactly to
\[
\Lambda''=12uv\xi+c_A(u+v)
                -2\varepsilon(T\dot f-f).
\tag{23}
\]
The first three terms and Lambda'' belong to F, so
k0:=T*dot(f)-f has zero dot derivative. It also has zero prime
derivative because f'=0 and T'=0. Hence k0 is complex.
The existing element (f+k0)/T is likewise killed by both
partials. Calling it c_f gives
\[
\begin{gathered}
d=-v\xi+c_fT-k_0,\qquad c_f,k_0\in\mathbb C,\\
\Lambda=2uv\xi^3+
\left(\frac{c_A(u+v)}2-\varepsilon k_0\right)\xi^2
 +c_\Lambda\xi+d_\Lambda,\qquad c_\Lambda,d_\Lambda\in\mathbb C .
\end{gathered}
\tag{24}
\]
The last integration is again obtained by subtracting the
displayed polynomial and taking exact derivatives. Neither an
antiderivative existence assumption nor F=C(xi) is used.
For reconstruction, the FULL coefficient sigma is
epsilon*T*q^2/J-v*xi+c_f*T-k0+xi*t+A'/2.
The last two terms restore d0 from the shifted d in(13);
they must not be omitted when using the original rows.

Substitute(20),(22),(24) into the literal original rows, with
sigma and d0 as in(11),(13). Their complete determinant, in the
basis(T,xi,q), is
\[
\boxed{\quad
\widehat J(X)
=-\frac{2\varepsilon(k_0+\varepsilon\xi)}{T^2}
\left(2T(k_0+\varepsilon\xi)q-J\right).
\quad}
\tag{25}
\]
This is the full determinant, not only its value at X=0.
It also follows directly by differentiating(14), using the
differential row identity following(15).
In particular its q coefficient is
-4epsilon*(k0+epsilon*xi)^2/T.
The coefficient xi=n_s is noncomplex since n_ss is nonzero.
As epsilon is a nonzero complex constant, k0+epsilon*xi cannot
vanish. Thus(25) is not a coefficient scalar, contradicting(12).

All zero boundaries of the integrated family remain in this
calculation: u or v may be zero, as may any of c_A,d_A,c_B,d_B,
c_f,k0,c_Lambda,d_Lambda. Only J and epsilon were required to
be nonzero, for reasons already proved in407 and(19).

## 6. Scope and verification

This excludes exactly the exceptional delta=beta=0 direction
under the complete supplied actual264 hypotheses with k=s,
n_ss nonzero and equal intrinsic degrees at least two.
The reduction to the quadratic affine-lower-function case is407,
not a new assumption on arbitrary equal degrees. The
nonexceptional profiles in407/413 are not addressed here.
There is no use of the degree-one conductor exclusions403/404,
no arbitrary entry theorem, no unrestricted cancellation
conclusion, and no original-coordinate construction.

The actual polynomial return is used in Section2, rather than
replaced by equality of rational fields. Every later parameter
change is a stated exact coefficient or affine intrinsic change.
The original full initial kernel, literal selected partial,
strong field return and full genuine levels are retained even
where a later step needs only their already proved consequences.

The complete407 source was reread through eed0ec+5a4c1a,413
through1e6444, and264 through880778. The writing guide was read
throughc68202 before authoring. Fresh unsaved2f0281 reconstructed
every divided-difference identity in(9), including its sign.
Fresh dcb1cf reconstructed the complete compact rows(14) from
the literal potentials.

Fresh unsaved7df8d7 first expanded the differential row identity.
The generic scalar coefficients were obtained in786d18/e724fd.
A separate literal-original-row reconstruction17047c retained
arbitrary d,dot(d),d' and all field jets, and returned zero
residuals for(16),(19). Fresh96a451 independently differentiated
the full original Y,Z,W after(24) and returned exactly(25).
These finite identities support the written algebra; the actual
ring specialization and exact-field arguments are proved above.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. This is a
scoped working exclusion, not a novelty claim, human-expert
review or formal certification.
