# Whole-plane cofactors and coupling reduction in the quadratic-cubic chart

In the nonzero-coupling branch of the actual height-two chart258,
the cofactor of the selected irreducible plane component is a unit
on the whole generic line. Consequently, for an irreducible
generator \(G\) of that plane ideal,
\(\mathcal H=\eta G+G^2R\), with \(\eta\in L^*\).

This identity treats reducible quartic equations and lower-degree
selected components without assuming that \(\mathcal H\) is
irreducible. Together with an original-ring auxiliary derivation,
it forces \(m_\lambda=0\) whenever \(q'''\ne0\). A constant first
projection is recognized by an actual commuting-slice endpoint.
The genuine quartic graph and two-stage quadratic embedding remain
open, with additional exact coefficient restrictions stated below.

## 1. Supplied actual chart

Use the fully read
[quadratic-cubic frontier258](two-affine-quadratic-cubic-frontier-pass258-working.md).
Its hypotheses here are
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
A=\ker E,\quad K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\\
a=EX\ne0,\quad t=EY/a\notin\mathbb C,
\end{gathered}
\tag{1}
\]
with full weighted initial kernel of height two and literal
quadratic-slot partial \(\partial_Z\) of exact shift three.
The resulting intrinsic LND and exact field satisfy
\[
\begin{gathered}
N\ne0,\quad Nv=1,\quad L=\operatorname{Frac}\ker_A N,\quad
K=L(v),\quad [L:\mathbb C(t,\lambda)]<\infty,\\
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\\
W=w+\theta X+(r'y+\lambda)X^2+rX^3,\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}
       =-a^3\in L^* .
\end{gathered}
\tag{2}
\]
All intercept coefficients lie in \(L[v]\), and
\(L[y,z,w]=L[v]\). The commuting coefficient partials on
\(L\) initially fix \(v\). The elements \(q,r\) are algebraic
over \(\mathbb C(t)\). Set
\[
m=k_\lambda\ne0,\qquad d=r'',\qquad
f(U)=\frac{q''-dm}{2}U^2+k_tU+n .
\tag{3}
\]
Primes on \(q,r\) denote the extended \(t\)-derivative.
The retained potentials are
\[
\begin{aligned}
z&=m\theta+f(y),\\
w&=g(y,\theta),\qquad
g(U,V)=\frac{\ell-P(U)-m_\lambda V^2/2-f_\lambda(U)V}{m},\\
P(U)&=\frac{d^2m_\lambda}{8}U^4
 +\frac{q'''-r'''m-3dm_t}{6}U^3
 +\frac{k_{tt}-dn_\lambda}{2}U^2+n_tU .
\end{aligned}
\tag{4}
\]
In particular the whole projected ring is
\(L[y,\theta]=L[v]\). The coefficient-field shear
\(\psi=\theta-dy^2/2\) also has
\(L[y,\psi]=L[v]\); it is not declared an ambient shear.

The exact potential of258 supplies a nonzero polynomial
\(\mathcal H(U,V)\) of total degree at most four with
\(\mathcal H(y,\psi)=0\). Its quartic part is
\[
\mathcal H_4=U^3(\alpha U+\beta V),\qquad
\alpha=\frac{q''''-mr''''-4q'''m_t/m}{24},
\quad \beta=-\frac{q'''m_\lambda}{6m}.
\tag{5}
\]
This expression may vanish or be reducible. Let
\(G\in L[U,V]\) generate the full evaluation kernel of
\((U,V)\mapsto(y,\psi)\), chosen irreducible.
No identification \(G=\mathcal H\) is assumed.

## 2. The scalar determinant makes the evaluated cofactor a unit

Here is the precise gradient calculation behind the cofactor gate.
Before the shear, write
\[
B_1=m_tV+f_t(U),\qquad C_1=m_\lambda V+f_\lambda(U),
\]
and put
\[
\mathcal A=-mg_t+mdU g_\lambda+C_1g_U,\qquad
\mathcal B=-mg_\lambda+C_1g_V.
\tag{6}
\]
These are the exact two formal gradient entries of the third
potential in258. Its shear satisfies
\[
\mathcal H_U(U,V)=
  (\mathcal A+dU\mathcal B)(U,V+dU^2/2),\qquad
\mathcal H_V(U,V)=\mathcal B(U,V+dU^2/2).
\tag{7}
\]
To check how the scalar enters, its \(X=0\) exterior form is
\[
dy\wedge(m\,d\theta+B_1\,dt+C_1\,d\lambda)\wedge dg .
\]
Its three coefficients on
\(dy\wedge dt\wedge d\lambda\),
\(dy\wedge dt\wedge d\theta\), and
\(dy\wedge d\lambda\wedge d\theta\), respectively, are
\[
\frac{C_1}{m}\mathcal A+g_U\mathcal B,\qquad
\mathcal A+d\,y\,\mathcal B,\qquad
\mathcal B .
\tag{8}
\]
In the middle coefficient \(d\,y\) means the product
\(d\cdot y\), not a differential.
For example the first coefficient also equals
\(B_1g_\lambda-C_1g_t\), by
\(mg_U=-B_1+dUC_1\) and \(mg_V=-C_1\).
Thus (8) follows directly from the literal differential rows.

All substitutions and their coefficient derivatives belong to
\(L[v]\), and \(m\) is a unit of that coefficient ring.
Equations (7),(8) show
\[
-a^3\in
\bigl(\mathcal H_U(y,\psi),\mathcal H_V(y,\psi)\bigr)L[v].
\tag{9}
\]
Write \(\mathcal H=GQ\). Evaluation of its gradients makes the
right side divisible by \(Q(y,\psi)\). The left side is a unit
of \(L[v]\). Therefore
\[
Q(y,\psi)=\eta\in L^*.
\qquad
\boxed{\mathcal H=\eta G+G^2R,\quad R\in L[U,V].}
\tag{10}
\]
Indeed \(Q-\eta\) lies in the full evaluation ideal \((G)\).
In particular the selected component has multiplicity one in
\(\mathcal H\). The other components need not disappear.

## 3. A nonzero mixed quartic coefficient leaves only a constant first entry

We use the plane-degree fact proved in the fully reread
[leading-sextic220, Section 5](rank-two-binary-quartic-leading-sextic-pass220-working.md):
if \(L[p(v),q(v)]\) has fraction field \(L(v)\), its irreducible
relation has degree \(\max(\deg p,\deg q)\) and its top form is
a pure power of a linear form.
One proof makes \(\deg p=i<j=\deg q\) by a linear change, and
uses the characteristic polynomial of multiplication by \(p\)
on the free rank-\(j\) \(L[q]\)-module \(L[v]\). Birationality
makes it the minimal polynomial. Its coefficient of the first
variable to power \(j-r\) has second-variable degree at most
\(\lfloor ir/j\rfloor<r\), by the \(j\) formal roots at infinity.
Hence its top form is the first variable to power \(j\).
The recursive simple-root expansions used for that bound may
be checked after algebraic extension and yield identities over
the original field. A constant first entry is the immediate
degree-one exception.

Apply this fact to the whole ring \(L[y,\psi]=L[v]\).
Suppose for the moment that \(q'''m_\lambda\ne0\), so
\(\beta\ne0\) in (5), and \(\deg\mathcal H=4\).
The top form has \(U\) as its only repeated linear factor,
of multiplicity three.

Let \(g=\deg G\). If \(g\ge3\), degree in (10) forces \(R=0\).
Then \(\mathcal H=\eta G\) has degree four, so \(g=4\)
and its top would be a fourth power, contrary to (5).
If \(g=2\), (10) makes \(R\) constant; its nonzero quartic
top would again be a pure fourth power.
If \(g=1\), its linear top squared divides \(\mathcal H_4\).
It must therefore be proportional to \(U\). These alternatives
prove
\[
q'''m_\lambda\ne0\quad\Longrightarrow\quad
G\sim U-y_0,\quad y=y_0\in L,\quad
\theta\text{ affine in }v .
\tag{11}
\]
The affine assertion follows from whole-line return, not just
from birationality of a finite plane map.

## 4. The constant-first entry has an original-ring endpoint

In this section assume \(y\in L\) and \(q'''\ne0\), but do not
initially assume anything about \(m_\lambda\).
Then \(L[\theta]=L[v]\), so \(\theta\) is affine.
By (4), \(z=m\theta+f(y)\) is affine in \(\theta\), and
\[
w_{\theta\theta}=-m_\lambda/m .
\tag{12}
\]
Extend \(N\) to \(A[u]\) by \(Nu=0\), and define the actual
polynomial derivation
\(\mathcal P=aN-(NX)E\). It fixes \(X,L\), commutes with \(E\),
and is locally nilpotent: on \(B_a=A_a[X]\) it is \(aN\)
on \(A_a\) and fixes \(X\). Put \(\tau=aN\theta\in L^*\).
The literal coordinate components are
\[
\begin{gathered}
\mathcal PX=\mathcal PY=0,\qquad
\mathcal PZ=\tau m,\qquad
\mathcal PW=\tau(X+w_\theta),\\
\mathcal P^2Z=0,\quad \mathcal P^3W=0,\quad
\mathcal P^2W=-\tau^2m_\lambda/m .
\end{gathered}
\tag{13}
\]

For clarity, primitive division preserves both actions.
Let \(\Delta\) be the gcd of the nonzero original components
of \(\mathcal P\), and \(D=\mathcal P/\Delta\).
The divisibility
\(\mathcal P\Delta=\Delta D\Delta\), together with the degree
function of an LND, gives \(\mathcal P\Delta=0\).
Consequently \(D\) is an irreducible LND.
Writing \(\mathcal PX_i=\Delta g_i\), with \(\gcd(g_i)=1\),
commutation gives
\[
(E\Delta)g_i+\Delta E(g_i)=\Delta D(EX_i).
\tag{14}
\]
Unique factorization implies \(\Delta\mid E\Delta\), hence
\(E\Delta=0\) by the same LND degree argument.
Thus \([E,D]=0\). In \(L[v][X]\), the two original actions
are \(a\partial_X,a\partial_v\), so their common kernel is \(L\).
In particular \(\Delta\in L^*\), with no assertion that it is
an original-ring unit. Set \(\delta=\tau/\Delta\in L^*\).

Over the actual UFD \(S=\mathbb C[X,Y]\), the ring is \(S[Z,W]\).
The irreducible \(S\)-linear LND \(D\) satisfies \(D^2Z=0\).
The exact UFD conclusion of
[Dasgupta--Gupta, Lemma 2.3(i)](https://arxiv.org/html/1701.03635v1)
therefore gives \(DZ\in S\), \(DW\in S[Z]\).
For every nonconstant polynomial in \(S\), its \(E\)-degree is
its ordinary total degree: a top homogeneous part \(P_j\) has
nonzero leading coefficient \(a^jP_j(1,t)\).
Thus \(S\cap\ker E=\mathbb C\). Since \(DZ=\delta m\ne0\)
is \(E\)-fixed, and \(D^3W=0\), we obtain
\[
DZ=d_0\in\mathbb C^*,\qquad
DW=A_0Z+B_0(X,Y),\qquad
A_0=\frac{D^2W}{d_0}\in\mathbb C .
\tag{15}
\]
Here \(DW\) has \(Z\)-degree at most one because \(DZ=d_0\ne0\).
Also \(D^2W=-\delta^2m_\lambda/m\) is \(E\)-fixed and belongs
to \(S\), giving the last constant assertion.

The literal formula \(DW=\delta(X+w_\theta)\) has exact
\(E\)-degree one. If \(A_0\ne0\), (15) forces
\(\deg B_0\le2\), and cancellation of degree two gives
\[
A_0q+B_{0,2}(1,t)=0 .
\tag{16}
\]
This makes \(q\) a complex polynomial of degree at most two,
contrary to \(q'''\ne0\). Thus \(A_0=0\), and (12),(15) imply
\(m_\lambda=0\). This contradicts the exceptional case (11).
We have proved the uniform necessary condition
\[
\boxed{q'''\ne0,\ m\ne0\quad\Longrightarrow\quad m_\lambda=0.}
\tag{17}
\]

There is also recognition, not just a restriction, when \(y\in L\).
Now \(DW=B_0(X,Y)\), and the actual elementary coordinate
\[
J=W-\frac{B_0(X,Y)}{d_0}Z
\tag{18}
\]
satisfies \(DJ=0\).
The inverse is \(W=J+B_0(X,Y)Z/d_0\); both compositions retain
\(X,Y,Z\). Hence \(\ker_BD=\mathbb C[X,Y,J]\), with slice \(Z/d_0\),
and this three-variable polynomial ring is \(E\)-stable.
The restriction of \(E\) is nonzero, with \(EX=a\ne0,E^2X=0\).
After dividing its coefficients by their gcd, factorial closure
or the LND degree argument keeps that gcd invariant.
The primitive restriction still has the nonfixed degree-one
coordinate \(X\). Daigle's theorem, in the freshly checked
[Dasgupta--Gupta Theorem 4.8](https://arxiv.org/html/1701.03635v1),
supplies an invariant coordinate of this actual three-ring.
It remains an ambient coordinate on adjoining \(Z\).
Regularity of \(A\), supplied by \(A[u]=B\), then permits
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1):
\(A\simeq\mathbb C^{[3]}\).
No PID slice assertion or coefficient-field coordinate descent
was used.

## 5. Genuine quartics: two legitimate shapes and further coefficient gates

Continue with \(q'''\ne0\), and discard only the recognized
constant-first case. By (17), \(m_\lambda=0\).
Let \(F=\ker_L\partial_\lambda\); the exact constant-field
argument of262 gives \(F/\mathbb C(t)\) finite and prime
constants \(\mathbb C\). In particular
\[
m\in F^*,\qquad k=m\lambda+k_0,\quad k_0\in F.
\tag{19}
\]
The complete coefficient table in258 now has \(V\)-degree at
most two. Its relevant coefficients are
\[
\begin{aligned}
[V^2]\mathcal H&=n_{\lambda\lambda}/2,\\
[U^2V]\mathcal H&=m''/2-(m')^2/m,\\
[UV]\mathcal H&=n_{t\lambda}-2n_\lambda m'/m,\\
[U^4]\mathcal H&=\alpha .
\end{aligned}
\tag{20}
\]
There are no \(UV^2\) or \(V^3\) terms.
For a nonconstant \(y\), the \(V\)-degree of the irreducible
relation is exactly \([L(v):L(y)]=\deg_v y\).
Thus (20) proves \(\deg_v y\le2\), without any quartic
irreducibility assumption.

If the selected component has degree four, (10) gives
\(\mathcal H=\eta G\) and \(\alpha\ne0\). Its top is \(U^4\),
so \(\deg_v\psi=4>\deg_v y\).
There are two legitimate whole-line shapes:

1. If \(y\) is affine, \(\psi=P_4(y)\) for a polynomial
   \(P_4\in L[U]\) of degree four.
2. If \(\deg_v y=2\), center the parameter over the exact field
   to write \(y=a_2x^2+c_2\), with \(a_2\in L^*\).
   Split \(\psi\) into its even and odd parts:
   \(\psi=P_2(y)+xB(x^2)\).
   The ring it generates with \(y\) has odd module
   \(xB(x^2)L[x^2]\). Whole-line return forces \(B=\beta_0\in L^*\).
   Therefore
   \[
   y=a_2x^2+c_2,\qquad
   \psi=P_2(y)+\beta_0x,\qquad \deg P_2=2.
   \tag{21}
   \]
   All changes in this description are coefficient-field
   parameter operations, not ambient automorphisms.

The graph in case 1 makes the \(V^2,U^2V,UV\) coefficients
of \(\mathcal H\) vanish. With \(\nu=n_\lambda\), this gives
\[
n=\nu\lambda+n_0,\quad \nu,n_0\in F,\qquad
(1/m)''=0,\quad (\nu/m^2)'=0.
\]
Exact integration over \(F\) yields
\[
1/m=\alpha_1t+\alpha_0,\qquad
\nu=\gamma m^2,\qquad \alpha_0,\alpha_1,\gamma\in\mathbb C .
\tag{22}
\]
The constant \(\gamma\) may be zero.

In case 2 the exact relation may be chosen as
\[
G=(V-P_2(U))^2-\frac{\beta_0^2}{a_2}(U-c_2).
\tag{23}
\]
It is irreducible and has \(V\)-degree two.
Writing \(\mathcal H=A_2V^2+B_2(U)V+C_4(U)\), its
\(V\)-discriminant is a nonzero scalar multiple of \(U-c_2\).
Here \(A_2=n_{\lambda\lambda}/2\) is nonzero, while the leading
coefficients of \(B_2(U)\) and \(C_4(U)\) are
\(m''/2-(m')^2/m\) and \(\alpha\), both in \(F\).
Vanishing of the discriminant's \(U^4\) coefficient gives
\[
\left(m''/2-(m')^2/m\right)^2
       =2n_{\lambda\lambda}\alpha.
\qquad
n_{\lambda\lambda}\in F^*,\quad n\in F[\lambda],\quad
\deg_\lambda n=2 .
\tag{24}
\]
The last polynomiality follows by subtracting explicit
primitives and using \(\ker_L\partial_\lambda=F\).
It does not imply that the other coefficients or \(L\)
are rational in \(\lambda\).

Neither (21) nor the graph in case 1 is excluded by whole-line
generation. Examples \(y=v,\psi=v^4\) and
\(y=v^2,\psi=v^4+v\) already demonstrate that geometric point.
They are examples of plane presentations, not actual258 frames.

For lower-degree selected components, (10) remains the boundary:
degree three forces \(\mathcal H=\eta G\);
degree two permits \(\mathcal H=\eta G+\gamma_0G^2\),
with \(\gamma_0\in L\);
degree one permits \(R\) of degree at most two.
They have not been discarded or recognized by the quartic
shape analysis.

## 6. Scope and provenance

The new conclusions are the evaluated-unit cofactor (10),
the forced coupling derivative (17), recognition of the
constant-first branch, and the exact restrictions
(19)--(24). They do not settle the nonconstant-first
whole-plane branch or every actual1123 frame.

If \(q'''=0\), the actual elementary quadratic correction
to \(Z\) lowers its time degree, as explained in262.
Recognition after that degree lowering is a separate retained
input, not needed in the present proof.

The complete258,262,220 and228 sources were read for their
explicitly used chart, plane-degree and original-ring gates.
The exact UFD Lemma 2.3(i) and Daigle theorem were freshly
checked in the primary Dasgupta--Gupta statement; no PID
claim was imported. The finite coefficient-field changes
were not treated as ambient maps.
No previous source, packet or index was edited, and no saved
checker was executed, imported or compiled.
No historical novelty, human expert certification,
arbitrary-entry theorem or unrestricted cancellation claim
is made.
