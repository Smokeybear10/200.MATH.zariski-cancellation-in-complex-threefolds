# Constant-p quartics in the paraboloid chart are impossible

The \(p'=0\) genuine quartic branch remaining after the corrected281
reduction is impossible. The complete coefficient integrations give
a quartic relation for a field element \(S\), with coefficients in
the actual intercept field. That relation is irreducible of degree
four, contradicting the strong field return.

This proof uses the corrected scalar and discriminant integrations
of281. It requires neither an ambient lift of \(S\) nor a rationality
assumption on the finite coefficient field \(F\).

## 1. Supplied actual branch and corrected inputs

Retain all actual hypotheses of
[280](principal-paraboloid-nonlinear-constant-slope-pass280-working.md)
and the corrected
[281](principal-paraboloid-quartic-exact-field-reduction-pass281-working.md).
They include
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(X^2Z-Y^2)\text{ is the full initial kernel},\quad
\operatorname{shift}(\partial_Z)=4,\quad k_s=0,\quad n_s\ne0,\\
K=\mathbb C(y,z,w)=L(v),\quad Nv=1,\quad L[y,\sigma]=L[v],\\
[F:\mathbb C(t)]<\infty,\quad
F=\ker_L\partial_n,\quad\ker(\partial_t|_F)=\mathbb C.
\end{gathered}
\tag{1}
\]
The selected projected component is genuinely quartic with
\(\deg_v y=4\), \(\deg_v\sigma=2\), not a lower-degree component.
The coefficient field and commuting derivatives are those of the
literal selected chart, with its nonzero calibrated Jacobian.
Primes denote the extended \(t\)-derivative on \(F\).

Write the coefficients as in281:
\[
\begin{gathered}
H=hn+c,\quad h\in\mathbb C^*,\quad T=pn+q,\quad
\omega=v_1n+v_0,\quad c,k,p,q,v_1,v_0\in F,\\
B=hk''/2+p,\quad a_2=B'+p',\quad
a_1=pk''-c''+k'p'+2v_1,\quad
a_0=-np'+k'v_1-q',\\
x=2By+a_2\sigma^2+a_1\sigma+a_0,\qquad
x^2=d\sigma+f,\qquad x_v\in L^*.
\end{gathered}
\tag{2}
\]
The symbol \(B\) is a coefficient, not the original polynomial ring.
The corrected281 scalar gives
\[
d\in F^*,\quad f\in F,\quad L=F(n),\quad K=F(n,x),\qquad
J_x=-d/(8B^2)\in F^*.
\tag{3}
\]
In particular the former, incorrect powers \(B^5\) and \(v_*^5/t^2\)
from the first draft of281 are not inputs here.

Assume henceforth precisely
\[
p'=0,\qquad p\in\mathbb C.
\tag{4}
\]
Then \(a_2=B'\ne0\), \(v_1'=0\), and \(v_1\in\mathbb C\).
The leading coefficient identity gives
\[
BB''=3(B')^2,\qquad B^{-2}=\alpha t+\kappa,\qquad
\alpha\in\mathbb C^*,\quad\kappa\in\mathbb C,\qquad
B'=-\alpha B^3/2.
\tag{5}
\]
All integrations below take place inside the exact field \(F\);
their integration constants are complex by (1). No assertion
\(F=\mathbb C(B)\) is made.

## 2. Exact integration of every coefficient used in the endpoint

The full corrected scalar ledger of281 specializes to
\[
\begin{aligned}
a_1'&=3B'a_1/B,&
a_0'&=(a_1^2+2B'a_0)/(2B),\\
d'&=4B'd/B,&
Bf'&=2B'f+a_1d .
\end{aligned}
\tag{6}
\]
Integrate these equations successively using (5). There exist
\(\beta,\gamma,\phi\in\mathbb C\) and \(\delta\in\mathbb C^*\) such that
\[
\boxed{
a_1=\beta B^3,\quad
a_0=\gamma B-\frac{\beta^2}{2\alpha}B^3,\quad
d=\delta B^4,\quad
f=\phi B^2-\frac{\beta\delta}{\alpha}B^4.}
\tag{7}
\]
For example
\[
(a_0/B)'=\beta^2B^4/2
          =\left(-\frac{\beta^2B^2}{2\alpha}\right)',
\qquad
(f/B^2)'=\beta\delta B^4
          =\left(-\frac{\beta\delta B^2}{\alpha}\right)'.
\]
The constant \(\delta\) is nonzero because \(d\ne0\).

The coefficient definition of \(a_1\) in (2) now gives
\[
(c'-pk'-2tv_1)'=-\beta B^3
                      =(2\beta B/\alpha)'.
\]
Thus, with \(\ell_0\in\mathbb C\),
\[
c'-pk'-2tv_1=2\beta B/\alpha+\ell_0,\qquad
q'=v_1k'-a_0.
\tag{8}
\]
The discriminant's linear coefficient is
\(d=2a_1a_0+4B\omega_t\). Since \(v_1\) is complex,
\(\omega_t=v_0'\). Substitution of (7) therefore gives
\[
v_0'=\frac{\delta-2\beta\gamma}{4}B^3
                         +\frac{\beta^3}{4\alpha}B^5.
\]
Using (5) once more yields
\[
v_0=-\frac{\delta-2\beta\gamma}{2\alpha}B
       -\frac{\beta^3}{6\alpha^2}B^3+\omega_0,
\qquad \omega_0\in\mathbb C.
\tag{9}
\]
These formulas retain all their complex constants, including
\(\beta,\gamma,\phi,\ell_0,\omega_0\). None has been set to zero
by a coefficient-field change.

## 3. A literal intercept identity

Define field elements
\[
\xi=x/B,\qquad S=B(\sigma-\beta/\alpha),\qquad
Y_0=y+\gamma/2,\qquad
W_0=w-v_1z+hy^2-\ell_0y-\omega_0 .
\tag{10}
\]
They all belong to \(K\). Since \(\sigma\) is nonconstant on the
generic line and \(B\in F^*\), the element \(S\) is nonzero.
The expressions \(Y_0,W_0\) are only changes of the actual intercept
generators at this stage; they are not declared ambient coordinates.

Use \(a_2=B'=-\alpha B^3/2\) in the first completion in (2).
Together with (7), it gives
\[
\boxed{Y_0=\xi/2+\alpha S^2/4,\qquad
       \xi^2-\phi=\delta B S.}
\tag{11}
\]
Both equalities are direct polynomial identities: for the first,
complete the square in \(\sigma-\beta/\alpha\); for the second,
divide \(x^2=d\sigma+f\) by \(B^2\).

We derive the last required identity from the literal potentials,
rather than infer it from (11). The actual intercept formulas are
\[
\begin{aligned}
z&=2ty+\sigma^2+k'\sigma+n,\\
w&=v_1n+v_0
 -p\{(2\sigma+k')y+k''\sigma^2/2\}
 -h\{y^2+k''\sigma y+k'''\sigma^3/6\}\\
&\hspace{9mm}+c'y+c''\sigma^2/2+q'\sigma .
\end{aligned}
\tag{12}
\]
Here \(p'=0\) has been used, not an assumption that the other
coefficient functions are constant. Also
\(hk''=2(B-p)\) and \(hk'''=2B'=-\alpha B^3\).

Subtract the complex corrections in (10) from (12). The coefficient
of \(y\) is exactly \(-2B(\sigma-\beta/\alpha)y=-2Sy\), by (8).
The remaining cubic, quadratic, and linear terms in \(\sigma\) are
\[
\frac{\alpha B^3}{6}\sigma^3
 -\frac{\beta B^3}{2}\sigma^2
 +\left(-\gamma B+\frac{\beta^2B^3}{2\alpha}\right)\sigma
 +v_0-\omega_0.
\tag{13}
\]
Substitute \(\sigma=S/B+\beta/\alpha\) and (9). The terms in
\(\beta^3B^3\) and \(\beta\gamma B\) cancel exactly, leaving
\[
W_0=-2S(y+\gamma/2)+\alpha S^3/6-\delta B/(2\alpha).
\]
With (11), this is
\[
\boxed{
W_0=-2SY_0+\alpha S^3/6
                    -\frac{\xi^2-\phi}{2\alpha S}.}
\tag{14}
\]
The division by \(S\) is only in \(K\), where it is legitimate.
It will be cleared in the polynomial relation below.
No element of \(F\) has been promoted to an ambient coordinate.

## 4. Irreducibility in the actual returned field

Eliminate \(\xi=2Y_0-\alpha S^2/2\) between (11),(14), and multiply
by \(12\). The result is the exact polynomial identity
\[
\boxed{\alpha^2 S^4-24\alpha Y_0S^2-24\alpha W_0S
                              -48Y_0^2+12\phi=0.}
\tag{15}
\]
We prove that it cannot hold in the field required by (1).

For independent formal variables \(U,V,T\), put
\[
\mathscr R(U,V,T)=
\alpha^2T^4-24\alpha UT^2-24\alpha VT-48U^2+12\phi.
\tag{16}
\]
As a polynomial in \(V\) over the UFD \(\mathbb C[U,T]\), its
coefficient is \(-24\alpha T\). This is relatively prime to its
constant term: reduction of the latter modulo \(T\) is
\(-48U^2+12\phi\), a nonzero polynomial not divisible by \(T\).
Consequently \(\mathscr R\) is primitive and linear in \(V\),
so it is irreducible in \(\mathbb C[U,V,T]\).

Viewed instead as a polynomial in \(T\), it is primitive over
\(\mathbb C[U,V]\) and remains irreducible over \(\mathbb C(U,V)\).
Its degree in \(T\) is exactly four because \(\alpha\ne0\).
Irreducibility persists after adjoining an independent transcendental
variable \(Z_0\): equivalently, apply Gauss's lemma in \(Z_0\) over
the field \(\mathbb C(U,V)\), or note that any polynomial factorization
over its rational function extension clears to one over that field.
Thus
\[
\mathscr R\text{ is irreducible of degree four in }
                   \mathbb C(U,Z_0,V)[T].
\tag{17}
\]

Finally the intercept change in (10) has the explicit complex
polynomial inverse
\[
y=Y_0-\gamma/2,\qquad
w=W_0+v_1z-h(Y_0-\gamma/2)^2
                      +\ell_0(Y_0-\gamma/2)+\omega_0.
\tag{18}
\]
Both orders of these three-generator substitutions are the identity.
It follows from the strong actual return in (1) that
\[
K=\mathbb C(Y_0,z,W_0).
\tag{19}
\]
Its three generators are algebraically independent over \(\mathbb C\),
because \(K\) has transcendence degree three and they generate it.
Therefore the specialization
\((U,Z_0,V)=(Y_0,z,W_0)\) identifies the coefficient field in (17)
with \(K\). But \(S\in K\) is a root by (15), contradicting
irreducibility of degree four. This excludes the supplied \(p'=0\)
genuine quartic.

## 5. Scope and verification

The contradiction uses only the actual strong field return, exact
coefficient integrations, and the explicit intercept identities.
It does not require an ambient-coordinate assertion for \(S\),
\(\xi\), \(Y_0\), or \(W_0\). It does not address the \(p'\ne0\)
genuine quartic branch or any lower-degree selected component.

The corrected281 source was completely reread before this note.
Fresh unsaved symbolic calculation retained arbitrary
\(h,p,v_1,\alpha,\beta,\gamma,\delta,\phi,\ell_0,\omega_0\) and the
complex constants in \(k\). It reconstructed the literal potentials
(12), verified the integrations (7)--(9), both identities leading
to (14), and the cleared relation (15), all with zero residuals.
The exact finite-field integrations and irreducibility over the full
three-generator coefficient field are written arguments, not inferred
from those finite controls. No retained source was edited and no saved
checker was executed, imported, or compiled. No unrestricted result
or historical novelty is claimed.

