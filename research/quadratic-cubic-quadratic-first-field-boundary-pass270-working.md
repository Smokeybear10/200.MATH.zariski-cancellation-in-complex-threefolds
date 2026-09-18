# Coefficient polynomiality for the quadratic-first quartic component

The genuine quadratic-first quartic component in263 has a smaller
coefficient-field frontier than its initial description suggests.
Its remaining potential is a polynomial of degree at most three
in the selected parameter. The discriminant first locates the
possible finite field extension in its constant term. An odd-part
coefficient of the scalar determinant then makes that constant
polynomial too, proving that the exact coefficient field is
\(L=F(\lambda)\).

This is a conditional reduction, not recognition. In particular,
polynomial dependence on two invariant parameters is not the
curve-field polynomial entry required by266.

## 1. Actual chart and precise selected branch

Use the actual chart of
[258](two-affine-quadratic-cubic-frontier-pass258-working.md)
and the evaluated-cofactor reduction of
[263](two-affine-quadratic-cubic-whole-plane-cofactor-pass263-working.md).
The full assumptions are
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\\
\operatorname{ht}I_{\rm initial}=2,\quad
\operatorname{shift}(\partial_Z)=3,\quad
Nv=1,\quad L=\operatorname{Frac}\ker_A N,\quad K=L(v),\\
[L:\mathbb C(t,\lambda)]<\infty,\qquad
L[y,\psi]=L[v],\quad \psi=\theta-r''y^2/2.
\end{gathered}
\tag{1}
\]
Here the initial ideal is the full weighted initial kernel, and
\(N\) denotes the selected intrinsic derivation. Below we use
\(N_2\), not \(N\), for a coefficient of a polynomial.
The actual expansions are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}
  &=-a^3\in L^*,\qquad a=EX\ne0.
\end{aligned}
\tag{2}
\]
In this chart \(K=\mathbb C(y,z,w)\). This is the strong
actual field return, not merely the displayed whole-line equality
over \(L\).

Assume the genuine quadratic-first quartic branch:
\[
q'''\ne0,\quad m=k_\lambda\ne0,\quad
\deg G=4,\quad \deg_v y=2,\quad \deg_v\psi=4.
\tag{3}
\]
The irreducible projected relation \(G\) is the selected
component. No irreducibility of the initially constructed
polynomial \(\mathcal H\) was assumed. The evaluated-unit
cofactor theorem in263 gives \(\mathcal H=\eta G\),
\(\eta\in L^*\), in degree four.

By263, \(m_\lambda=0\). Put
\(F=\ker_L\partial_\lambda\). The exact constant-field
argument in262 gives \([F:\mathbb C(t)]<\infty\), with
constants \(\mathbb C\) for its extended \(t\)-derivative.
Primes on elements of \(F\) denote that derivative. On \(L\),
subscripts \(t,\lambda\) are the original commuting coefficient
partials, holding the other parameter fixed. Thus
\[
\begin{gathered}
q,r,m,k_0\in F,\quad m\ne0,\quad k=m\lambda+k_0,\\
n=N_2\lambda^2/2+n_1\lambda+n_0,
\qquad N_2\in F^*,\quad n_1,n_0\in F,\qquad
\nu:=n_\lambda=N_2\lambda+n_1.
\end{gathered}
\tag{4}
\]
There is no assumption \(F=\mathbb C(t)\) or \(L=F(\lambda)\).

## 2. The full discriminant coefficient that forces polynomiality

Use formal variables \(U,V\), independent of the coefficient
field, and write the complete258 relation in this branch as
\[
\mathcal H(U,V)=\frac{N_2}{2}V^2+
     (M U^2+b_1U+b_0)V+C_4(U),\qquad
C_4(U)=\sum_{j=0}^4c_jU^j.
\tag{5}
\]
The coefficients needed here, with no omitted parameter
derivatives, are
\[
\begin{aligned}
M&=m''/2-(m')^2/m,\\
b_1&=n_{t\lambda}-2\nu m'/m,
&b_0&=-\ell_\lambda-\nu^2/m,\\
c_4&=\frac{q''''-mr''''-4q'''m'/m}{24},\\
c_2&=n_{tt}/2-k_{tt}\nu/(2m)-n_tm'/m,\\
c_1&=\ell m'/m-\ell_t-\nu n_t/m.
\end{aligned}
\tag{6}
\]
In particular \(c_4\in F^*\). The coefficients \(c_0\)
and hence the discriminant constant are not presumed to lie
in \(F[\lambda]\).

The exact whole-line shape established in263 is
\[
y=a_2x_0^2+c_2^*,\qquad
\psi=P_2(y)+\beta_0x_0,\qquad
a_2,\beta_0\in L^*,\quad c_2^*\in L,\quad
P_2\in L[U],\quad \deg P_2=2.
\tag{7}
\]
The symbol \(c_2^*\) in (7) is a parameter-center coefficient,
not the coefficient \(c_2\) in (5),(6).
The variable \(x_0\) is obtained by an affine parameter change
over the exact field \(L\); it is not an ambient coordinate.
Equation (7), together with \(\mathcal H=\eta G\), proves
that the discriminant
\[
\mathscr D(U):=(M U^2+b_1U+b_0)^2-2N_2C_4(U)
                 =D_1U+D_0
\tag{8}
\]
has degree exactly one. Its linear coefficient is nonzero.
Indeed comparison of the monic \(V\)-relations gives
\(\mathscr D(U)=N_2^2\beta_0^2(U-c_2^*)/a_2\).

The \(U^4\) coefficient of (8), already used in263, is
\[
M^2=2N_2c_4.
\tag{9}
\]
Thus \(M\in F^*\), so division by \(M\) below is justified.
The complete \(U^2\) coefficient of (8) is
\[
\begin{aligned}
0&=b_1^2+2Mb_0-2N_2c_2\\
 &=b_1^2-2M\ell_\lambda-2M\nu^2/m-2N_2c_2.
\end{aligned}
\tag{10}
\]
Consequently
\[
\boxed{\ell_\lambda=
\frac{b_1^2-2M\nu^2/m-2N_2c_2}{2M}
          \in F[\lambda],\qquad \deg_\lambda\ell_\lambda\le2.}
\tag{11}
\]
For the degree assertion, \(b_1,\nu,k_{tt}\) have degree
at most one in \(\lambda\), while \(n_t,n_{tt}\) have
degree at most two. All divisions in (11) are by nonzero
elements of \(F\).

Integrate the polynomial on the right of (11) term by term
over \(F\), keeping \(t\) fixed. The difference from \(\ell\)
has zero \(\lambda\)-derivative and therefore belongs to
the exact kernel \(F\). Hence
\[
\boxed{\ell\in F[\lambda],\qquad\deg_\lambda\ell\le3.}
\tag{12}
\]
This includes the integration constant and does not rely on
rationality of the finite extension \(L/F(\lambda)\).

## 3. The nonzero linear discriminant coefficient

Equations (4),(6),(12) now imply
\[
b_1\in F[\lambda]_{\le1},\qquad
b_0\in F[\lambda]_{\le2},\qquad
c_1\in F[\lambda]_{\le3}.
\]
Here the subscript is only a polynomial degree bound.
Taking the \(U\) coefficient of (8) gives
\[
\boxed{D_1=2b_1b_0-2N_2c_1
              \in F[\lambda]_{\le3}\setminus\{0\},
\qquad D_0=b_0^2-2N_2c_0\in L.}
\tag{13}
\]
The nonvanishing is the exact whole-line conclusion from (7),
not a claim that a generic cubic coefficient is nonzero.
No polynomiality of \(D_0\) is obtained here.

Define the actual field element
\[
x=N_2\psi+My^2+b_1y+b_0.
\tag{14}
\]
Completing the square in (5) and evaluating \(\mathcal H=0\)
gives
\[
\boxed{x^2=D_1y+D_0,\qquad
y=\frac{x^2-D_0}{D_1},\qquad
\psi=\frac{x-My^2-b_1y-b_0}{N_2}.}
\tag{15}
\]
Comparison in (7) shows
\(MU^2+b_1U+b_0=-N_2P_2(U)\), so
\(x=N_2\beta_0x_0\). In particular \(x\) is affine in
the original line parameter \(v\), with nonzero slope:
\[
L[x]=L[v],\qquad K=L(x),\qquad
x\text{ is transcendental over }L.
\tag{16}
\]
These are coefficient-field parameter facts. Neither (14)
nor division by \(D_1\) is promoted to an ambient change.

## 4. Exact field return with one remaining discriminant constant

The literal first two potentials, retaining all lower terms, are
\[
\begin{aligned}
f(U)&=(q''-r''m)U^2/2+k_tU+n,\\
P(U)&=(q'''-mr'''-3r''m')U^3/6
       +(k_{tt}-r''\nu)U^2/2+n_tU,\\
z&=m\theta+f(y),\qquad
mw=\ell-(m'y+\nu)\theta-P(y),\qquad
\theta=\psi+r''y^2/2.
\end{aligned}
\tag{17}
\]
Thus (4),(12) give
\[
z=m\psi+q''y^2/2+k_ty+n,\qquad
w=\frac{\ell}{m}
 -\frac{m'y+\nu}{m^2}\{z-f(y)\}-\frac{P(y)}m
       \in F[\lambda,y,z].
\tag{18}
\]
Let \(T=F(\lambda,D_0)\subset L\). Equations (13),(15),(18)
put each of \(y,z,w\) in \(T(x)\). The actual strong return
from (1),(2) therefore gives one inclusion; all its displayed
generators already lie in \(K\), giving the other:
\[
K=\mathbb C(y,z,w)\ \subset\ T(x)\ \subset\ K.
\tag{19}
\]
Hence \(K=T(x)=L(x)\). Since \(T\subset L\) and \(x\)
is transcendental over \(L\), one has
\(L\cap T(x)=T\). Explicitly, if
\(a=P(x)/Q(x)\in L\), with \(P,Q\in T[x]\) and \(Q\ne0\),
then \(P-aQ=0\) as a polynomial over \(L\). Comparing a
coefficient for which \(Q\) is nonzero gives \(a\in T\).
Intersecting (19) with \(L\) proves
\[
\boxed{L=F(\lambda,D_0).}
\tag{20}
\]
In particular the entire finite extension of \(F(\lambda)\)
is generated by this single discriminant constant. At this
stage no descent of \(D_0\) to \(F(\lambda)\) or
\(F[\lambda]\) has been proved. The next section supplies it.

## 5. Scalar parity removes the finite field extension

The line parameter \(x\) from (14) is affine in \(v\).
Changing to \((t,\lambda,x)\), and then setting \(X=0\)
in the literal calibration (2), gives
\[
\mathfrak J:=\det\frac{\partial(y,z,w)}{\partial(t,\lambda,x)}
       =-a^3/x_v\in L^*.
\tag{21}
\]
This is independent of \(x\). Moving coefficients in the
affine parameter change do not alter this chain-rule factor.
In this section parameter partials hold \(x\) fixed unless
a different fixed variable is explicitly indicated.

For clarity put \(d=D_1,c=D_0,e=1/m,h=m/N_2\), and use
\(U\) as a formal copy of \(y\). Equations (15),(18) give
\[
\begin{aligned}
y&=(x^2-c)/d,\qquad z=h x+P_z(y),\\
P_z(U)&=pU^2+uU+v_0,\\
p&=q''/2-hM\in F,\quad
u=k_t-hb_1\in F[\lambda]_{\le1},\quad
v_0=n-hb_0\in F[\lambda]_{\le2},\\
w&=A_w(y)z+B_w(y),\\
A_w(U)&=e'U+a_0,\qquad
a_0=-\nu e^2=-N_2e^2\lambda-n_1e^2,\\
B_w(U)&=e\ell-A_w(U)f(U)-eP(U).
\end{aligned}
\tag{22}
\]
The \(P(U)\) in the last line is the potential in (17), not
the newly labeled polynomial \(P_z\).
The coefficient bounds are
\[
[U^i]P_z\in F[\lambda]_{\le2-i}\ (0\le i\le2),\qquad
[U^i]B_w\in F[\lambda]_{\le3-i}\ (0\le i\le3).
\tag{23}
\]
For the second assertion use the displayed formula in (22):
the cubic coefficient belongs to \(F\), the quadratic one
is at most linear in \(\lambda\), and the remaining two
have degrees at most two and three. These follow directly
from (4),(12),(17).

Define, with all coefficient derivatives holding the formal
variable \(U\) fixed,
\[
V_0=(B_w)_\lambda-N_2e^2P_z,\qquad
T_0=(e''U+(a_0)_t)P_z+(B_w)_t.
\tag{24}
\]
Their coefficient bounds are respectively \(2-i\) and \(3-i\)
in degree \(U^i\). Also \((A_w)_\lambda=-N_2e^2\),
\((A_w)_t=e''U+(a_0)_t\), and
\(N_2e^2h=e\).

Here is a direct reconstruction of the odd part of (21).
Temporarily differentiate while holding \(y\) fixed. The
identity \(x^2=dy+c\) gives
\[
x_t=\frac{d_ty+c_t}{2x},\qquad
x_\lambda=\frac{d_\lambda y+c_\lambda}{2x}.
\]
Writing \(z_t,z_\lambda\) for these fixed-\(y\) derivatives,
the determinant and the formula for \(w\) give
\[
\mathfrak J=\frac{2x}{d}
 \left\{z_t\big((A_w)_\lambda z+(B_w)_\lambda\big)
       -z_\lambda\big((A_w)_t z+(B_w)_t\big)\right\}.
\tag{25}
\]
For example this also follows by replacing the first two
columns by the corresponding fixed-\(y\) columns; the first
row then becomes \((0,0,2x/d)\).
Insert
\[
z_t=h'x+\frac{h(d_ty+c_t)}{2x}+(P_z)_t(y),\qquad
z_\lambda=\frac{h(d_\lambda y+c_\lambda)}{2x}
                      +(P_z)_\lambda(y)
\]
into (25), and reduce \(x^2\) to \(dy+c\). The odd part
is exactly \((2x/d)\mathcal O(y)\), where
\[
\begin{aligned}
\mathcal O(U)={}&(P_z)_tV_0-(P_z)_\lambda T_0
 -\frac{h^2}{2}(e''U+(a_0)_t)(d_\lambda U+c_\lambda)\\
&-\frac{eh}{2}(d_tU+c_t)-eh'(dU+c).
\end{aligned}
\tag{26}
\]
This computation retains both \(c_t\) and \(c_\lambda\).
It is a rational calculation in a function field, so the
temporary divisions by \(x\) are legitimate. The resulting
even/odd identity is polynomial in \(x\).

Since (21) is independent of \(x\), its odd part vanishes.
Even and odd polynomials in \(x\) are independent over \(L\),
and substitution \(U=(x^2-c)/d\) is injective on \(L[U]\).
Thus \(\mathcal O(U)=0\). Its linear coefficient is
\[
0=-eh'd-\frac{ehd_t}{2}
  +[U]\big((P_z)_tV_0-(P_z)_\lambda T_0\big)
  -\frac{h^2}{2}\big(e''c_\lambda+(a_0)_td_\lambda\big).
\tag{27}
\]
The coefficients \(c,c_t\) occur only in the constant term
of (26), so they do not enter (27).
Moreover
\[
e''=-2e^2M\ne0.
\]
Every other term in (27) belongs to \(F[\lambda]_{\le3}\).
For the product term this follows from (23),(24): in
\([U](P_z)_tV_0\), the degrees are at most \(1+2\) and
\(2+1\); in \([U](P_z)_\lambda T_0\), they are at most
\(0+3\) and \(1+2\). The remaining terms use
\(d\in F[\lambda]_{\le3}\) and
\((a_0)_t\in F[\lambda]_{\le1}\).
Consequently (27), followed by exact-kernel integration as
in (12), proves
\[
\boxed{D_{0,\lambda}\in F[\lambda]_{\le3},\qquad
D_0\in F[\lambda]_{\le4},\qquad L=F(\lambda).}
\tag{28}
\]
The field equality is the composition of (28) with (20),
not an assumption used in the parity calculation.

## 6. Actual two-parameter polynomiality and the remaining gap

The same calculation gives a useful actual-ring identity, but
not yet the needed one-variable coefficient-field entry.
In (2) replace the intercepts by
\[
\widehat y=Y-tX,\qquad
\widehat z=Z-(q'\widehat y+m\lambda+k_0)X-qX^2.
\]
Use (18) to write \(\widehat w\) as a polynomial in
\(\lambda,\widehat y,\widehat z\) over \(F\), and set
\(\widehat\theta=(\widehat z-f(\widehat y))/m\).
The third literal expansion gives
\[
\boxed{W=\widehat w+\widehat\theta X+
           (r'\widehat y+\lambda)X^2+rX^3
           \in F[\lambda,X,Y,Z],\qquad\deg_\lambda\le3.}
\tag{29}
\]
The degree bound follows directly: \(f,P\) have parameter
degree at most two, \(m'\widehat y+\nu\) at most one,
\(\ell\) at most three, and \(\widehat z\) at most one.
All denominators used in (18),(29) belong to \(F^*\).

The invariant field \(F(\lambda)\) has transcendence degree
two over \(\mathbb C\). Thus (29) does not satisfy the
one-variable coefficient-field hypothesis of the
[polynomial-entry criterion266](curve-field-polynomial-entry-criterion-pass266-working.md).
The established polynomiality of \(D_0\) and the equality
\(L=F(\lambda)\) do not remove \(\lambda\) from (29).
The parameter reconstruction \(y=(x^2-D_0)/D_1\) also
still involves division by the nonzero polynomial \(D_1\).
Additional full-determinant constraints or an actual coordinate
change must supply that missing step. The graph recognition267
uses a different scalar-parameter shear and is not imported here.

## 7. Scope and verification

The conclusions (12),(13),(20),(28),(29) use all actual hypotheses
in (1)--(3), especially the genuine selected quartic component,
the evaluated-unit cofactor, whole-line generation, and strong
field return. They do not apply to an arbitrary formal
quadratic relation or to a lower-degree selected component.
They do not recognize this branch or all exact1123 frames.

The retained258 and263 sources were read for the literal
coefficient table and exact selected-shape gates. An independent
unsaved symbolic expansion verified the complete right side
of (11) and its parameter degree; a separate source/hand audit
checked (6),(10),(13) and both inclusions in (19).
The odd-part gate (26),(27) was independently derived by Jet,
Root and the author from the literal scalar determinant, and
checked against an unrestricted coefficient expansion.
The exact-field integration and intersection proof above are
written arguments, not conclusions of those finite calculations.
No older source, packet or index was changed. No saved checker
was executed, imported or compiled. No historical novelty,
unrestricted entry or general cancellation theorem is claimed.
