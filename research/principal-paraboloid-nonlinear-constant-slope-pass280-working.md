# Nonlinear paraboloid components have a constant parameter slope

In the nonlinear projected-plane part of the actual branch271, the
affine restriction277 improves to \(H=hn+c\), with
\(h\in\mathbb C^*\) and \(c\in F\). The second potential level is
affine in \(n\). A complete quartic coefficient table then excludes
the genuine quartic graph shape and restricts the other genuine
quartic to a specific quadratic-over-quadratic presentation.

This is a conditional reduction, not recognition of those nonlinear
components. The remaining projected lines are outside this note.

## 1. Exact retained entry

Retain all actual hypotheses, exact fields and coefficient derivatives
of [271](principal-paraboloid-nonconstant-intercept-plane-reduction-pass271-working.md)
and the conclusion of
[277](principal-paraboloid-affine-parameter-restriction-pass277-working.md).
Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
\text{full initial kernel }(X^2Z-Y^2),\qquad
\operatorname{shift}(\partial_Z)=4,\qquad k_s=0,\quad n_s\ne0,\\
F=\ker_L\partial_n,\quad [F:\mathbb C(t)]<\infty,\quad
[L:F(n)]<\infty,\quad \ker(\partial_t|_F)=\mathbb C,\\
K=\mathbb C(y,z,w)=L(v),\quad L[y,\sigma]=L[v],\quad
H=b n+c,\qquad b\in F^*,\quad c,k\in F.
\end{gathered}
\tag{1}
\]
The exact parameter \(n\) is transcendental over \(F\).
The coefficient derivations commute and fix \(v\); primes denote
the induced t-derivative on \(F\).

Let \(G\) be the full irreducible plane relation of \((y,\sigma)\).
Assume throughout this note that it is nonlinear:
\[
g=\deg G=\max(\deg_vy,\deg_v\sigma)\ge2.
\tag{2}
\]
The pure-top theorem and the nonzero calibrated Jacobian of271 give
\[
G_g=c_0\Lambda^g,\qquad
Q-q_0=\eta G+G^2R,\quad \eta\in L^*,\quad \deg Q\le6.
\tag{3}
\]
These are retained exact statements, not claims based on examples
of polynomial curves or a nonsingular plane fiber.

## 2. The complete quartic top kills two coefficient derivatives

Use the exact potential from271, with independent formal variables
\(U,P\). Write
\[
\begin{aligned}
\mathscr A&=(2P+k')U+k''P^2/2,\qquad
\mathscr C=U^2+k''PU+k'''P^3/6,\\
\mathscr W&=\omega-(b'P+T_n)\mathscr A-b\mathscr C
 +(b'n+c')U+(b''n+c'')P^2/2+T_tP,\\
Q_U&=(2P+k')\mathscr W_n-\mathscr W_P,\qquad
Q_P=(2U+k''P)\mathscr W_n-\mathscr W_t,
\end{aligned}
\tag{4}
\]
where \(T,\omega\in L\). All formal derivatives precede any
substitution of actual projected coefficients.

Because \(H_{nn}=0\), the degree-six and degree-five parts of \(Q\)
vanish. Differentiating the following expression gives the complete
degree-three homogeneous parts of both gradients in (4):
\[
\boxed{
Q_4=P^2\left\{-2T_{nn}U^2+(b''-T_{nn}k'')UP+
 \frac{b k''''+4b'k'''+6b''k''-3T_{nn}(k'')^2}{24}P^2\right\}.
}
\tag{5}
\]
In particular \(\deg Q\le4\).

If \(T_{nn}\ne0\), the quadratic factor in braces is not divisible
by \(P\). Every linear factor of \(Q_4\), even over an algebraic
closure, has multiplicity at most two. The pure-top statement gives
\(g\le2<4\), and (3) then makes \(\Lambda^{2g}\) divide \(Q_4\).
Thus \(g=1\), contrary to (2). Therefore \(T_{nn}=0\).

If now \(b''\ne0\), the nonzero quartic top in (5) is
\(P^3(b''U+dP)\). Its distinct factors have multiplicities three
and one. Again (3) forces \(g=1\), a contradiction. Hence
\[
\boxed{T_{nn}=0,\qquad b''=0,\qquad T=p n+q,\quad p,q\in F.}
\tag{6}
\]
The integration uses precisely \(F=\ker_L\partial_n\).
The statement \(b''=0\) at this stage allows \(b\) to be a
nonconstant complex affine function of \(t\).

## 3. Whole-line generation forces b to be constant

After (6), direct integration of (4) gives the U-squared coefficient
\[
[U^2]Q=3b'P+\frac{bk''}{2}+p+b'k'.
\tag{7}
\]
The quartic top is now
\[
Q_4=\frac{b k''''+4b'k'''}{24}P^4.
\tag{8}
\]
We prove \(b'=0\), keeping both possibilities for (8).

First suppose \(Q_4\ne0\). Equation (3) and (2) allow only
\(g=2\) or \(g=4\): \(g=3\) cannot have a nonzero square-cofactor
term of degree at most four, and then \(Q=\eta G+q_0\) would
have degree three rather than four.

If \(g=2\), its pure top is \(P^2\). As in277, the full relation
is \(G=U-rP^2-sP-C\) with \(r\ne0\), after multiplication by
a unit. Its U-coefficient is nonzero by irreducibility and
whole-line generation. Since \(R\) in (3) is constant,
\([U^2]Q=R\) is independent of \(P\). Equation (7) gives \(b'=0\).

For \(g=4\), (3) gives \(Q-q_0=\eta G\). Suppose \(b'\ne0\).
Then (7) shows that the U-degree of \(G\) is exactly two.
The actual whole-line equality implies
\[
[L(v):L(\sigma)]=\deg_v\sigma=\deg_U G=2.
\tag{9}
\]
Also \(\deg_v y=4\), since the top of \(G\) is \(P^4\).
We recall the exact quadratic whole-line classification in this
specific situation. Center the polynomial parameter to write
\(\sigma=a_2 x^2+d_2\), with \(a_2\in L^*\).
Split \(y\) into even and odd parts:
\[
y=P_2(\sigma)+x B(x^2),\qquad \deg P_2=2.
\]
The odd part of \(L[\sigma,y]\) is exactly
\(xB(x^2)L[x^2]\), because products of two odd factors are even.
Equality with \(L[x]\) forces \(B\) to be a nonzero scalar.
Consequently the full relation can be chosen as
\[
G=(U-P_2(P))^2-\lambda_0(P-d_2),\qquad \lambda_0\in L^*.
\tag{10}
\]
Its U-squared coefficient is constant, contradicting (7) and
\(Q-q_0=\eta G\) when \(b'\ne0\).

It remains to consider \(Q_4=0\). If \(b'\ne0\), (7) makes
\(Q\) have degree exactly three. Its degree-three part is
\[
Q_3=P\{3b'U^2+d_1UP+d_0P^2\}
\tag{11}
\]
for some \(d_i\in L\); the formula follows from (4),(6).
This is not a pure cube: its factor \(P\) would force the
cube's linear form to be \(P\), but its \(PU^2\) coefficient
is nonzero. Hence \(g=3\) is impossible in (3).
If \(g=2\), the square-cofactor term would have degree at least
four, so it vanishes and \(Q-q_0=\eta G\) would have degree two,
also impossible. No larger \(g\) can divide \(Q-q_0\).
This contradicts the nonlinear assumption (2).

All cases prove
\[
\boxed{b=h\in\mathbb C^*,\qquad H=hn+c,\qquad T=pn+q,
\quad c,k,p,q\in F.}
\tag{12}
\]
No rationality of \(F\), equality \(L=F(n)\), or actual
coordinate assertion follows just from (12).

## 4. The complete remaining coefficient table

In the setting (12), the exact normalized primitive is
\[
\boxed{
Q=B U^2+(C_2P^2+C_1P+C_0)U
       +D_4P^4+D_3P^3+D_2P^2+D_1P,
}
\tag{13}
\]
where
\[
\begin{aligned}
B&=hk''/2+p,& C_2&=hk'''/2+2p',\\
C_1&=pk''-c''+k'p'+2\omega_n,
& C_0&=-np'+k'\omega_n-q',\\
D_4&=hk''''/24,
& D_3&=(pk'''-c'''+3k''p')/6,\\
D_2&=-np''/2+k''\omega_n/2-q''/2,
& D_1&=-\omega_t .
\end{aligned}
\tag{14}
\]
The symbol B in (13)--(14) denotes a coefficient, not the original
four-variable ring in (1).
Differentiating (13) reconstructs both formal gradients in (4);
the normalization \(Q(0,0)=0\) is retained. In particular
\(\omega\) has not yet been specialized or integrated.

Suppose now that the selected relation is genuinely quartic,
\(g=4\). Then \(Q-q_0=\eta G\), \(D_4\ne0\), and \(G\) has
pure top \(P^4\). Its U-degree cannot be zero: a relation in P
alone would make sigma constant over L, contrary to a nonlinear
whole-line relation. If \(B=0\), the U-degree of \(G\) is one,
so \(\sigma\) is affine in \(v\) by whole-line generation.
Then \(G\) has the graph form \(U-P_4(P)\).
Its U-coefficient, and hence \(C_2P^2+C_1P+C_0\), must be
a nonzero scalar. But \(B=0\) implies \(p=-hk''/2\), so
\(C_2=-hk'''/2\). Thus \(k'''=0\), contrary to \(D_4\ne0\).
The genuine quartic graph is excluded.

Therefore every remaining genuine quartic in this nonlinear branch
has
\[
B\ne0,\quad \deg_v\sigma=2,\quad \deg_v y=4,
\quad G\text{ of the form (10)}.
\tag{15}
\]
The U-discriminant of \(Q-q_0\) is a nonconstant linear
polynomial in \(P\):
\[
(C_2P^2+C_1P+C_0)^2
 -4B(D_4P^4+D_3P^3+D_2P^2+D_1P-q_0).
\tag{16}
\]
Its degree-four and degree-three coefficients give
\[
C_2^2=4BD_4=\frac{Bh k''''}{6}\ne0,\qquad
C_1=\frac{2BD_3}{C_2}\in F.
\tag{17}
\]
Since every other term in \(C_1\) belongs to \(F\), (14) proves
\(\omega_n\in F\). Exact integration gives
\[
\omega=v_1n+v_0,\qquad v_1,v_0\in F.
\tag{18}
\]

The degree-two coefficient of (16) is
\(C_1^2+2C_2C_0-4BD_2=0\).
Using (14),(18), its n-coefficient is
\(-2C_2p'+2Bp''\). Transcendence of \(n\) over \(F\) therefore gives
\[
Bp''=C_2p'=(B'+p')p'.
\tag{19}
\]
This includes \(p'=0\). If \(p'\ne0\), exact differentiation yields
\[
(B/p')'=\frac{B'p'-Bp''}{(p')^2}=-1.
\]
The exact prime constants of \(F\) give a complex \(\tau\) such that
\[
\boxed{p'=0\quad\text{or}\quad B=(\tau-t)p',
\qquad \tau\in\mathbb C.}
\tag{20}
\]
This is a necessary coefficient restriction, not an existence claim
for either family.

## 5. Scope and verification

The constant-slope conclusion (12) applies to every nonlinear selected
component in the actual271 branch. Equations (15)--(20) concern only
its genuine degree-four component. Selected conics, cubics and lines
have not been silently assigned those additional restrictions.
No ambient coordinate change or invariant coordinate is constructed here.
In particular neither full principal1222 recognition nor unrestricted
cancellation follows from this note.

Root completely read the retained271 and277 sources. Fresh unsaved
algebra reconstructed (5), the coefficient (7), and every coefficient
of the primitive (13), with commuting coefficient derivatives retained.
The whole-line odd-module argument and constant-field integrations
are written above rather than inferred from those finite identities.
No completed saved checker was rerun, imported or compiled.
No novelty, human expert review or proof-assistant certification is claimed.
