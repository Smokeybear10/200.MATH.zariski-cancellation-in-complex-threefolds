# A fourth potential and birational projection with moving transverse slope

Working result: retain every actual hypothesis of264, and suppose
\(k=s+f\), \(f_s=0\), and
\(n=\nu s+n_0\), where \(\nu,n_0\in\ker_L\partial_s\) and
\(b=\nu'\ne0\). The complete genuine fourth potential is displayed
below, including both derivatives of its moving third level.
Its unit gradient-minor condition excludes projection degree two.
Thus the actual polynomial line is finite and birational over
\(L[\sigma,\theta]\).

This conclusion uses division by the nonzero coefficient \(b\),
not division by \(H_V=bP-\ell_s-\nu^2\). The latter need not be
a unit on the line. The note also records the precise polynomial
return and coefficient restrictions when the linear remainder
vanishes on the actual line. These are necessary conditions, not
recognition or realization statements.

## 1. Complete actual input and exact coefficient fields

Retain the full supplied chart of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the corrected genuine fourth-potential construction of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\qquad A=\ker E,\qquad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
a_0=EX\ne0,\qquad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full weighted initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad
[L:\mathbb C(t,s)]<\infty,\quad Na_0=Nt=Ns=0,\\
Nv=1,\quad O=L[A]=L[v]=L[y,z,w]=L[y,\sigma,\theta],\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here \(L[A]\) is the specified actual coefficient localization.
The coefficient partials commute and fix the original intrinsic
parameter \(v\); their joint constants are \(\mathbb C\).
Let \(\mathbb F=\ker_L\partial_s\), the exact finite extension
of \(\mathbb C(t)\). It is not assumed rational. Primes on its
elements denote their exact \(t\)-derivatives.

Assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in\mathbb F,\qquad b=\nu'\ne0.
\tag{2}
\]
The second potential \(\ell\in L\) is arbitrary. In particular
\[
n_t=bs+n_0',\quad n_{tt}=b's+n_0'',\quad
n_{ttt}=b''s+n_0''',\quad n_{ts}=b,\quad n_{ss}=0.
\tag{3}
\]
No term proportional to \(s\) in (3) is dropped.
There is no condition on \(f'''\), \(\ell_s\), or \(\ell_{ss}\).

The complete literal rows and the first two potentials are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n_t\sigma-\nu\theta.
\end{aligned}
\tag{4}
\]
All formal variables below are independent over \(L\).

## 2. The complete third and fourth potentials

The third polynomial of264 specializes to
\[
\begin{aligned}
H(U,P,V)={}&U^2+\{(f''-2\nu)P+n_t-\nu f'\}U\\
&+\frac{f'''}6P^3+\frac{n_{tt}-\nu f''}{2}P^2
 -(\nu n_t+\ell_t)P+\nu\ell\\
&+(bP-\ell_s-\nu^2)V,
\qquad H(y,\sigma,\theta)=h\in L.
\end{aligned}
\tag{5}
\]
In particular \(H-h\) is monic quadratic in \(U\).
The formal derivative \(H_V=bP-\ell_s-\nu^2\) is not assumed
nonzero after evaluation, much less invertible in \(O\).

In296's notation, \(m=1\), \(\lambda=\nu\),
\(D=2P+f'\), and \(\beta=2U+f''P+n_t\).
The corrected closed gradient therefore is
\[
\boxed{
\begin{aligned}
Q_U&=H_P-(2P+f')H_V+\nu H_U,\\
Q_P&=H_t-h_t-(2U+f''P+n_t)H_V+\nu H_P,\\
Q_V&=H_s-h_s.
\end{aligned}}
\tag{6}
\]
Coefficient partials of \(H\) hold \(U,P,V\) fixed.
The two derivatives \(h_t,h_s\) in (6) are derivatives of the
actual third level, not formal-variable derivatives.

A primitive normalized by \(Q(0,0,0)=0\) is
\[
\boxed{
\begin{aligned}
Q={}&\frac{f''}{2}U^2\\
&+\left\{\left(\frac{f'''}2-2b\right)P^2
 +(n_{tt}+2\ell_s-bf')P+bV+f'\ell_s-\ell_t\right\}U\\
&+\frac{f''''}{24}P^4+\frac{n_{ttt}-3bf''}{6}P^3
 +\frac{f''\ell_s-\ell_{tt}-2bn_t}{2}P^2\\
&+(b\ell+n_t\ell_s-h_t)P
 +\frac{b'}2P^2V-(\nu b+\ell_{ts})PV\\
&+(\nu\ell_s-h_s)V-\frac{\ell_{ss}}2V^2.
\end{aligned}}
\tag{7}
\]
For a short direct integration check, (6) gives
\[
\begin{aligned}
Q_U={}&f''U+\left(\frac{f'''}2-2b\right)P^2
 +(n_{tt}+2\ell_s-bf')P+bV+f'\ell_s-\ell_t,\\
Q_V={}&bU+\frac{b'}2P^2-(\nu b+\ell_{ts})P
             +\nu\ell_s-h_s-\ell_{ss}V,\\
Q_P(0,P,0)={}&\frac{f''''}{6}P^3
 +\frac{n_{ttt}-3bf''}{2}P^2
 +(f''\ell_s-\ell_{tt}-2bn_t)P+b\ell+n_t\ell_s-h_t.
\end{aligned}
\tag{8}
\]
Integrating these compatible components yields every term in (7).
Direct differentiation verifies all three equations (6), including
the \(s\)-terms of (3). Thus (7) is the genuine corrected
primitive, not an arbitrary polynomial vanishing on the curve.
By296 and the actual \(X\)-linear scalar coefficient,
\[
Q(y,\sigma,\theta)=q\in L.
\tag{9}
\]
The full constant scalar further gives the evaluated unit ideal
\[
\boxed{
(H_UQ_P-H_PQ_U,\ H_UQ_V-H_VQ_U,\ H_PQ_V-H_VQ_P)\,O=O.}
\tag{10}
\]
This is precisely296's minor statement. Its proof uses the actual
nonzero scalar in (1) and makes no division by a component of
\(\nabla H\). In particular (10) remains available at every zero
of the evaluated \(H_V\).

## 3. Monic reduction with exact V coefficient

Write
\[
d=f''-2\nu,\qquad a=n_t-\nu f',\qquad
H-h=U^2+(dP+a)U+C_0(P,V),
\tag{11}
\]
where (5) explicitly defines \(C_0\), including its term \(-h\).
Let \(L_0(P,V)=Q(0,P,V)\), all the \(U\)-independent terms of (7).
Division by the monic third relation gives the polynomial identity
\[
Q-q-\frac{f''}{2}(H-h)=R(P,V)U+S(P,V),
\qquad S=L_0-q-\frac{f''}{2}C_0,
\tag{12}
\]
with
\[
\begin{aligned}
R={}&bV+r_2P^2+r_1P+r_0,\\
r_2={}&\frac{f'''}2-2b,\\
r_1={}&n_{tt}+2\ell_s-bf'-\frac{f''(f''-2\nu)}2,\\
r_0={}&f'\ell_s-\ell_t-\frac{f''(n_t-\nu f')}2.
\end{aligned}
\tag{13}
\]
In particular \(R_V=b\in L^*\), regardless of any evaluated
gradient. All moving levels remain in \(S\). Set
\[
\psi(P)=-\frac{r_2P^2+r_1P+r_0}{b},\qquad
G(P,V)=V-\psi(P),\qquad R=bG.
\tag{14}
\]
These are coefficient-field polynomials, not ambient coordinate
changes. Their only new denominator is \(b\ne0\).

## 4. The unit cofactor excludes projection degree two

Put \(C=L[\sigma,\theta]\) and \(M=\operatorname{Frac}C\).
By (5), \(y\) is integral of degree at most two over \(C\), and
\[
O=C[y]=C+Cy.
\tag{15}
\]
Consequently \(C\) has transcendence degree one over \(L\),
the extension \(M\subset L(v)\) is finite, and its degree is one
or two. These facts also rule out \(\sigma,\theta\in L\)
simultaneously.

Suppose the field degree is two. Evaluating (12) and using the
linear independence of \(1,y\) over \(M\) gives
\[
R(\sigma,\theta)=S(\sigma,\theta)=0.
\tag{16}
\]
Equation (14) gives \(\theta=\psi(\sigma)\), so \(C=L[\sigma]\).
Here \(\sigma\notin L\): otherwise \(C=L\), contrary to its
transcendence degree. Evaluation \(L[P]\to L[\sigma]\) is
therefore injective.

Divide \(S(P,V)\) by the monic polynomial \(G=V-\psi(P)\).
Its remainder is \(S(P,\psi(P))\in L[P]\). By (16) and the
injectivity just noted this remainder vanishes identically. Thus
\[
S=GT,\quad T\in L[P,V],\qquad
Q-q=\frac{f''}{2}(H-h)+G(bU+T).
\tag{17}
\]
Take formal gradients in \((U,P,V)\), then evaluate on the line.
Since \(G(\sigma,\theta)=0\), all three gradient minors of
\(H,Q\) are the corresponding minors of \(H,G\) multiplied by
\[
\chi=b y+T(\sigma,\theta)\in O.
\]
Their unit ideal (10) forces \(\chi\) to be a unit of
\(O=L[v]\), hence \(\chi\in L^*\). As \(b\in L^*\),
\[
y=\frac{\chi-T(\sigma,\theta)}b\in C.
\tag{18}
\]
This contradicts field degree two. We have proved
\[
\boxed{[L(v):\operatorname{Frac}L[\sigma,\theta]]=1.}
\tag{19}
\]
The proof neither requires irreducibility of \(H-h\) nor extracts
unit-gradient information from a sliced factorization. The exact
global identity (17) and the full genuine minors are used.

## 5. The nonvanishing and vanishing remainder branches

Write \(r=R(\sigma,\theta)\in C\). If \(r\ne0\), evaluating
(12) gives \(r y=-S(\sigma,\theta)\in C\). Together with
(15),(19) this proves
\[
rO\subset C,\qquad O[r^{-1}]=C[r^{-1}].
\tag{20}
\]
In particular \(O\) is the finite normalization of \(C\), and
the conductor contains \(rO\). This is not an equality assertion
for the conductor. It does not say that \(C\) itself is normal
or that \(C=O\) before localization.
Indeed \(O\) is finite over \(C\), has the same fraction field,
and is integrally closed. Any element of that field integral over
\(C\) is also integral over \(O\), and therefore belongs to \(O\).

If \(r=0\), (12) also gives \(S(\sigma,\theta)=0\). The proof
of (17),(18) still applies, without any assumption about field
degree. Thus in this branch
\[
\boxed{O=C=L[\sigma],\qquad \deg_v\sigma=1,
\qquad \theta=\psi(\sigma).}
\tag{21}
\]
The whole polynomial ring, not just its fraction field, is used
to conclude that \(\sigma\) is an affine intrinsic parameter.

Here there are additional exact necessary coefficient conditions.
Center only the formal first variable by
\(x=U+(dP+a)/2\), so that
\[
H-h=x^2+C_0(P,V)-\frac{(dP+a)^2}{4}.
\tag{22}
\]
After substituting \(V=\psi(P)\), the polynomial after \(x^2\)
has degree at most three, and its cubic coefficient is
\[
\frac{f'''}6+b\left(2-\frac{f'''}{2b}\right)
                 =2b-\frac{f'''}3.
\tag{23}
\]
By (21), the evaluated centered function belongs to \(L[P]\).
Its square cannot have exact degree three. Therefore
\[
f'''=6b,\qquad f''-6\nu\in\mathbb C,
\qquad \deg_\sigma\left(y+\frac{d\sigma+a}{2}\right)\le1.
\tag{24}
\]
The constant statement follows because the exact \(t\)- and
\(s\)-derivatives of \(f''-6\nu\) both vanish. It does not
assume rationality of \(\mathbb F\). Equation (14) now has
leading term \(-P^2\), so \(\theta\) has exact degree two in
\(\sigma\), while \(y\) has degree at most one.

Finally \(S(P,\psi(P))=0\) is an identity of polynomials in
\(P\). Differentiating the first equality of (24) gives
\(f''''=6b'\). The coefficient of \(P^4\) in that identity is
\[
\frac{f''''}{24}-\frac{b'}2-\frac{\ell_{ss}}2
            =-\frac{b'+2\ell_{ss}}4.
\tag{25}
\]
Indeed the three displayed contributions come respectively from
\(P^4\), \(P^2V\), and \(V^2\) in (7); all other terms of
\(S\) have degree at most three after substitution. Hence
\[
\boxed{\ell_{ss}=-b'/2\quad\text{if }R(\sigma,\theta)=0.}
\tag{26}
\]
Neither (24) nor (26) is asserted sufficient for the full actual
scalar or for realization. This branch is not excluded here.

## 6. Verification and scope

The complete264 and296 sources were freshly read before this
derivation. Fresh unsaved calculation87759c rebuilt (5)--(8) with
arbitrary \(f(t),\nu(t),n_0(t),\ell(t,s),h(t,s)\). All three
corrected-gradient residuals were zero. It also reconstructed
(13), the exact cubic coefficient (23), and the quartic
coefficient (25), keeping every coefficient derivative in (3).
The unit-factor and finite-ring arguments are written algebraic
arguments, not consequences of numerical sampling.

The result supplies a complete potential and a finite birational
projection, not a global plane-coordinate recognition theorem.
It makes no claim that \(H_V\) is a unit, that the projected
curve is globally normal, or that coefficient-field changes are
original complex polynomial automorphisms. The entire genuine
scalar, strong and whole returns, global slice, full initial
kernel and selected derivation remain required hypotheses.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. No unrestricted
cancellation, arbitrary-entry, novelty, actual-existence or formal
certification claim is made.
