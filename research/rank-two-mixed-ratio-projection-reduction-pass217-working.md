# Whole-plane projection for the mixed rank-two leading ratio

Status: bounded working actual-chart reduction, not original-ring
recognition. For a supplied exact1122 frame with full initial kernel
\(ZW-X^2Y^2\), the branch \(R\ne0\) has
\(L[y,\vartheta]=L[v]\). Its plane component is a line or a conic.
In the conic case both original projected entries have degree two,
while \(y-(t/\rho)\vartheta\) has degree one.

The proof retains the full \(q_t\ne0\) universal potentials. A sextic
with three distinct leading lines gives a preliminary degree bound;
the actual scalar determinant and a degree-five gap then exclude
the cubic and quartic components. The coefficient-field combination
\(y-(t/\rho)\vartheta\) is not asserted to be an ambient coordinate.

## 1. Supplied actual frame and exact coefficient field

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2),\\
a=EX\ne0,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(a s,b s,e_0s^2,h_0s^2).
\end{gathered}
\tag{1}
\]
The capital letters are actual polynomial coordinates, and the
displayed ideal is the full initial kernel. The variable \(s\) in
the leading map is independent.

Use the original pivot \(\partial_Z\). The freshly read
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
provides
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=t^2/\rho,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\qquad W=w+\vartheta X+\rho X^2,\qquad
Z=z+\sigma X+(t^2/\rho)X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad J_0=-a^3\in L^*.
\end{gathered}
\tag{2}
\]
The ratios \(t,\rho\) are algebraically independent. Their partials
extend uniquely and commute on the finite separable field \(L\),
then fix \(v\). In particular \(t,\rho\ne0\). The field \(L\) is
not assumed rational, and the original speed \(a\) is not assumed
to be a unit in \(B\).

The proof below assumes \(R\ne0\), with \(R\) defined in (5).
This is not an assertion that \(R\) has no roots. No change of
the original pivot or ambient generators is used.

## 2. Exact specialized potentials

For \(c\in L\), put
\(H_j(c;U,V)=\sum_{i=0}^j
c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\), with independent formal
variables \(U,V\). Write \(J=\rho U-tV\). Direct differentiation
of \(q=t^2/\rho\) gives
\[
H_2(q)=\frac{J^2}{\rho^3},\qquad
H_3(q)=-\frac{VJ^2}{\rho^4},\qquad
H_4(q)=\frac{V^2J^2}{\rho^5}.
\tag{3}
\]
Universal184 supplies \(k,n,\ell,m\in L\). Define
\[
\begin{aligned}
f&=J^2/\rho^3+k_tU+k_\rho V+n,
&\mathcal R&=f_V=-2tJ/\rho^3+k_\rho,\\
S&=-VJ^2/\rho^4+H_2(k)+H_1(n),
&T&=\ell-S,\\
c_0&=f_\rho
 =-\frac{(\rho U-3tV)J}{\rho^4}
   +k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Q&=V^2J^2/\rho^5+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m .
\end{aligned}
\tag{4}
\]
Every coefficient derivative in this display fixes \(U,V\).
The four exact integrated identities are
\[
\begin{gathered}
\sigma=(2t/\rho)y-(t^2/\rho^2)\vartheta+k,\qquad
z=-(t^2/\rho^2)w+f(y,\vartheta),\\
R w=T(y,\vartheta),\qquad
\frac{t^2}{\rho^3}w^2+c_0(y,\vartheta)w+Q(y,\vartheta)=0,\qquad
R=\mathcal R(y,\vartheta)\ne0.
\end{gathered}
\tag{5}
\]
In particular the quadratic term in \(w\) is present and has a
nonzero scalar coefficient.

Eliminating \(w\) without dividing in the line ring gives
\[
\mathcal H=\frac{t^2}{\rho^3}T^2+\mathcal R c_0T+\mathcal R^2Q,
\qquad \mathcal H(y,\vartheta)=0.
\tag{6}
\]
The three degree-six contributions are, respectively,
\(t^2V^2J^4/\rho^{11}\),
\((2tVJ^5-4t^2V^2J^4)/\rho^{11}\), and
\(4t^2V^2J^4/\rho^{11}\). Hence
\[
\boxed{\deg\mathcal H=6,\qquad
\mathcal H_6=\frac{t}{\rho^{11}}V(\rho U-tV)^4(2\rho U-tV).}
\tag{7}
\]
The three displayed lines are distinct over \(L\). Their
multiplicities are one, four, and one. No lower potential affects
this nonzero top part.

## 3. Full gradients, actual cofactor, and conductor

Use evaluated expressions
\[
\begin{gathered}
B_1=S_U+\mathcal R_Uw=f_t+q_{t\rho}w,
\qquad C_1=S_V+\mathcal R_Vw=f_\rho+q_{\rho\rho}w,\\
q_{t\rho}=-2t/\rho^2,\qquad q_{\rho\rho}=2t^2/\rho^3,\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_i(y,\vartheta)w,
\qquad i=t,\rho,\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho.
\end{gathered}
\tag{8}
\]
Here, as in (4), subscripts on formal polynomials differentiate
coefficients before evaluation. In particular \(B_1\) contains
the nonzero mixed-derivative contribution \(q_{t\rho}w\).

Let
\(\mathcal K(U,V,W_0)=t^2W_0^2/\rho^3+c_0W_0+Q\).
The formal identities
\((c_0)_U=\mathcal R_t\), \((c_0)_V=\mathcal R_\rho\),
\(Q_U=S_t-\ell_t\), and \(Q_V=S_\rho-\ell_\rho\) give
\[
\begin{gathered}
(\mathcal RW_0+S-\ell)_{U,V,W_0}=(B_1,C_1,R),\qquad
\mathcal K_{U,V,W_0}=(-\Lambda_t,-\Lambda_\rho,C_1),\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho).
\end{gathered}
\tag{9}
\]
The first two triples are evaluated at \((y,\vartheta,w)\).
For the last line one can differentiate
\(\mathcal H=\mathcal R^2\mathcal K(U,V,T/\mathcal R)\) in the
fraction field, then clear denominators. This uses both equations
in (5), not an assertion about the whole formal hypersurface.

The exact universal determinant is
\(J_0=[dy\wedge(Rd\vartheta+B_1dt+C_1d\rho)\wedge dw]
_{dt\wedge d\rho\wedge dv}\).
Substitution of (8) and expansion give
\[
\begin{gathered}
R^3J_0=D_U\mathcal H_U(y,\vartheta)+D_V\mathcal H_V(y,\vartheta),\\
D_U=R(y_v\vartheta_\rho-y_\rho\vartheta_v)+C_1y_v,\qquad
D_V=R(y_t\vartheta_v-y_v\vartheta_t)-B_1y_v.
\end{gathered}
\tag{10}
\]
These are identities from the full universal chart; they do not
require \(q_t=0\).

Put \(C=L[y,\vartheta]\) and \(O=L[v]\). The second equation in
(5) and the actual whole-line return in (2) give \(O=C[w]\).
The last equation in (5) is quadratic with unit leading coefficient,
and the third equation gives \(Rw\in C\). Consequently
\[
O=C+Cw,\qquad \operatorname{Frac}C=L(v),\qquad
C_R=O_R,\qquad RO\subset C.
\tag{11}
\]
Thus \(O\) is the finite normalization of \(C\). The module
generators \(1,w\) are not asserted to be a free basis.

Let \(G\in L[U,V]\) generate the height-one evaluation kernel
\((U,V)\mapsto(y,\vartheta)\). It divides \(\mathcal H\).
Equation (10), with \(R\ne0\) and \(J_0\in L^*\), excludes a
repeated selected factor. For \(\mathcal H=GQ_1\), it proves
\[
0\ne Q_1(y,\vartheta)\mid R^3\quad\hbox{in }L[v].
\tag{12}
\]
In particular this cofactor cannot have arbitrarily large degree
after evaluation. It need not yet be a unit.

## 4. The pure leading line over the exact field

We use the following elementary polynomial-plane fact. If
\(F[P(v),Q(v)]\subset F[v]\) is birational over a characteristic-zero
field, its irreducible relation has total degree
\(\max(\deg P,\deg Q)\), and its top homogeneous part is a pure
power of one linear form.

Here is a proof retaining the coefficient field. Make an invertible
linear change of the pair so that \(Q\) has degree \(j>0\) and
\(P\) has degree \(i<j\). If \(P\) is constant, birationality
forces \([F(v):F(Q)]=j=1\). Otherwise \(i>0\).
The module \(F[v]\) is free of rank \(j\) over \(F[Q]\), with
basis \(1,v,\ldots,v^{j-1}\). The characteristic polynomial of
multiplication by \(P\) is its minimal polynomial, because
\(F(P,Q)=F(v)\); it is a monic relation of U-degree \(j\) with
coefficients in \(F[V]\).

Over an algebraic closure set \(V=s^{-j}\). The equation
\(Q(v)=s^{-j}\) has \(j\) formal roots
\(v=s^{-1}(\beta_\zeta+O(s))\): after multiplication by \(s^j\)
the constant equation has \(j\) distinct nonzero roots, so its
solutions lift recursively. Every \(P(v)\) then has pole order
at most \(i\). The coefficient of \(U^{j-r}\) in the monic
relation has V-degree at most \(\lfloor ri/j\rfloor\).
For \(r>0\), this is strictly less than \(r\), so every such
term has total degree less than \(j\). The top is \(U^j\).
Undoing the linear change proves the stated fact. This temporary
field extension proves polynomial coefficient identities over the
original field; it does not change the given function field.

Apply the fact to \(C\). Write \(g=\deg G\). Also
\(\deg_U G=\deg_v\vartheta\) and
\(\deg_V G=\deg_v y\) when the respective entries are
nonconstant. These equalities follow from
\([L(v):L(p(v))]=\deg p\) and birationality; the elementary
irreducibility of \(p(T)-Z_0\) proves that field-degree identity.
If one entry is constant, birationality already gives \(g=1\).

By (7), a pure-power top of multiplicity at least two must use
the line \(\rho U-tV\), and its multiplicity is at most four.
Thus either \(g=1\), or
\[
\begin{gathered}
2\le g=\deg_v y=\deg_v\vartheta\le4,\qquad
G_g=\gamma(\rho U-tV)^g,\quad \gamma\in L^*,\\
\xi=y-(t/\rho)\vartheta,\qquad
1\le d_0:=\deg_v\xi<g,\qquad
R=k_\rho-(2t/\rho^2)\xi.
\end{gathered}
\tag{13}
\]
The strict degree drop follows by evaluating the top relation.
If \(\xi\) were constant, \(C=L[\vartheta]\) and birationality
would instead force \(g=1\). Throughout, \(\xi\) is only a
polynomial in \(v\) with coefficients in \(L\).

## 5. Exclusion of degree three and degree four

There is one short consequence of the conductor before using
the cofactor. The pair \((d_0,g)=(3,4)\) is impossible.
Indeed \(O\) is free of rank three over \(L[\xi]\), and the
minimal polynomial of \(\vartheta\) over \(L(\xi)\) has degree
three by birationality. Its monic characteristic polynomial has
coefficients in \(L[\xi]\). Hence
\[
C=L[\xi]\oplus L[\xi]\vartheta\oplus L[\xi]\vartheta^2
\quad\hbox{if }(d_0,g)=(3,4).
\tag{14}
\]
The leading degrees of the three summands are respectively
\(0,4,8\) modulo three. They cannot cancel one another. Every
nonzero element of \(C\) therefore has degree in the semigroup
\(\langle3,4\rangle\), which omits five. But \(Rv^2\in C\)
by (11), and its degree is five. This is a contradiction over
the exact field \(L\).

For the remaining comparison make the formal, invertible
\(L\)-linear substitution \(U=\Xi+(t/\rho)V\). Use hats for
polynomials after this substitution. Equation (7) becomes
\[
\widehat{\mathcal H}_6
 =\frac{t}{\rho^7}\Xi^4V(2\rho\Xi+tV),\qquad
\widehat G_g=\widehat\gamma\Xi^g.
\tag{15}
\]
Evaluation is now \((\Xi,V)=(\xi,\vartheta)\); the evaluated
cofactor and \(R\) are unchanged. This substitution is not an
ambient coordinate map and is not used to transform partials.

Suppose first \(g=3\). Then \(\widehat Q_1\) has total degree
three and its top part is
\(\eta\Xi V(2\rho\Xi+tV)\), with \(\eta\in L^*\).
Here \(d_0=1\) or two. The term \(\Xi V^2\) evaluates with
degree \(d_0+6\). The other top term has degree \(2d_0+3\),
and all lower-total-degree terms have evaluated degree at most
six. Thus the highest term is unique, and (12) would imply
\[
d_0+6=\deg_v Q_1(y,\vartheta)
\le3\deg_vR=3d_0,
\tag{16}
\]
which is impossible for \(d_0<3\).

Suppose next \(g=4\). The degree-five gap has excluded \(d_0=3\),
so \(d_0\le2\). The cofactor now has total degree two and top
\(\eta V(2\rho\Xi+tV)\). Its unique highest evaluated term
is \(\eta t\vartheta^2\), of degree eight. The mixed term has
degree at most six and the lower terms degree at most four.
Again (12) gives the contradiction
\[
8=\deg_v Q_1(y,\vartheta)\le3d_0\le6.
\tag{17}
\]
No assumption about the roots or multiplicity of a center
polynomial was needed in either exclusion.

## 6. Exact conclusion and the remaining original-ring question

Only \(g=1\) or \(g=2\) remains. A birational polynomial line
component has an affine polynomial parameter, so \(g=1\) gives
\(C=O\). For \(g=2\), (13) forces \(d_0=1\), and
\(L[\xi]=L[v]\). Consequently
\[
\begin{gathered}
\boxed{R\ne0\ \Longrightarrow\ L[y,\vartheta]=L[v],\qquad
\deg G\le2.}\\
\deg G=2\ \Longrightarrow
\begin{cases}
\deg_v y=\deg_v\vartheta=2,\\
\deg_v(y-(t/\rho)\vartheta)=1.
\end{cases}
\end{gathered}
\tag{18}
\]
The same cofactor-degree argument cannot discard the conic: its
top term \(\Xi^2V^2\) has evaluated degree six, which can also
be contributed by a lower-total-degree term \(V^3\).

This proves neither an ambient invariant coordinate nor a
polynomial inverse in the original ring. The coefficients
\(t/\rho\) and those expressing the affine parameter belong to
\(L\), and no descent of these coefficients to original units
has been shown. The branch \(R=0\) remains outside this note;
the t-independent zero-return theorem205 does not apply to this
new \(q\) without additional work.

The conclusion is restricted to the supplied actual frame (1).
It gives no minimum-profile or arbitrary-entry theorem and does
not settle unrestricted cancellation. The written proof and the
independent inline algebra used to check its formulas are not
human expert review, formal certification, or novelty clearance.
No saved checker was executed in authoring this note, and no
earlier source or index was changed.
