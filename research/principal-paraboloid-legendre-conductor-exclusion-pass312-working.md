# The Legendre projected-line branch is excluded by its conductor

Working result: the actual reducible projected-line branch of310,
with \(\sigma_v\ne0\) and \(m_s=0\) before its actual normalization,
cannot occur. The polynomial normalization found there carries the
original locally nilpotent derivation explicitly. Its conductor must
be invariant, but the original coordinate identities make that
invariance impossible.

This is an exclusion of the supplied branch, not recognition of all
projected lines or the unrestricted cancellation problem. No
polynomial-entry theorem is used.

## 1. Exact retained ring and field gates

Retain the complete actual hypotheses and deductions of the fully read
[310](principal-paraboloid-line-legendre-field-reduction-pass310-working.md).
The actual complex reframe in its Section1 has already been performed.
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
a=EX\ne0,\\
L=\mathcal F(\eta),\qquad a\in L^*,\qquad
[\mathcal F:\mathbb C(r)]<\infty,\qquad
\eta\in L^*,\qquad t\in\mathcal F(\eta),\\
\operatorname{Frac}\mathcal B=\mathcal F(X,S,\eta).
\end{gathered}
\tag{1}
\]
The retained selected derivation N kills the leader a, so
\(a\in L=\operatorname{Frac}\ker_A N\), as recorded in (1).
The elements X,S,eta are algebraically independent over the exact
curve field \(\mathcal F\). All of \(\mathcal F,\eta,t,a\) lie
in the fraction-field kernel of E. The normalized actual coefficients
satisfy \(k=s\). The coefficient change, full scalar and exact
strong field return that establish (1) are retained inputs, not
inferred from the polynomial formulas below alone.

Use the curve-field coefficients \(f,g,c,d,T,r\) of310, with
\(T=-f''/4\in\mathcal F\) and \(d'=c\). Its full original map is
\[
\begin{aligned}
Y&=(X+r)S+(\eta-f)/2,\\
Z&=S^2-f'S-g'X+c+\eta T,\\
W&=(X-r)Z-(X+r)S^2-\eta S-gX+d.
\end{aligned}
\tag{2}
\]
Here \(S=\omega+tX\), with \(E\omega=0\). Consequently
\[
EX=a,\qquad ES=at,\qquad E\eta=0,\qquad E\mathcal F=0
\tag{3}
\]
as identities of fraction fields. Neither a nor at has yet been
assumed polynomial in eta.

Define the two subrings of the actual fraction field
\[
\mathcal R=\mathcal F[X,Y,Z,W],\qquad
\mathcal N=\mathcal F[X,S,\eta]=\mathcal F[X,Y,S].
\tag{4}
\]
The last equality and its exact polynomial inverses are
\[
\eta=2Y-2(X+r)S+f,\qquad
Y=(X+r)S+(\eta-f)/2.
\tag{5}
\]
Thus X,Y,S are also algebraically independent over \(\mathcal F\).
The ring \(\mathcal R\) contains \(\mathcal B\) and is stable under E.
Indeed E kills \(\mathcal F\), and its action on the actual generators
is polynomial in the original coordinates. It is locally nilpotent
on \(\mathcal R\), since every element is a finite sum of products
of such generators with E-invariant coefficients.

## 2. The original derivation extends explicitly to the normalization

Since \(a=EX\in\mathcal B\subset\mathcal R\subset\mathcal N\) and
\(a\in\mathcal F(\eta)\), independence of X,S over that field gives
\[
a\in \mathcal N\cap\mathcal F(\eta)=\mathcal F[\eta].
\tag{6}
\]
Differentiating the first actual identity in (2) gives
\[
EY=aS+(X+r)at.
\tag{7}
\]
The left side belongs to \(\mathcal B\subset\mathcal N\).
The first term on the right is polynomial in \(\mathcal N\) by (6).
Regard the remainder as a polynomial in X over
\(\mathcal F(S,\eta)\). Its X-coefficient is at, so
\[
at\in\mathcal F[S,\eta]\cap\mathcal F(\eta)=\mathcal F[\eta].
\tag{8}
\]
This uses an actual coordinate derivative, not an inference that every
coefficient of the original field chart is regular.

Write \(b=at\in\mathcal F[\eta]\). Equations (3),(6),(8) show that
the original derivation restricts on \(\mathcal N\) to
\[
E=a(\eta)\partial_X+b(\eta)\partial_S,\qquad E\eta=0.
\tag{9}
\]
It is a nonzero locally nilpotent \(\mathcal F\)-derivation there:
each application lowers the total degree in X,S. No general theorem
about extension to an integral closure is needed. Nor does the proof
need a choice of primitive auxiliary derivation or a new slice.

## 3. The normalization and its conductor as exact free modules

Put \(\mathcal C=\mathcal F[X,Y,Z]\), and introduce the coefficients
of310:
\[
\begin{aligned}
A_X&=f'+2T(X+r),&
B_{X,Y}&=2TY+Tf-g'X+c,\\
D&=(X+r)A_X-(2Y+f),&
E_0&=-(X+r)B_{X,Y}-gX+d.
\end{aligned}
\tag{10}
\]
In particular \(D\in\mathcal F[X,Y]\) has exact Y-coefficient
\(-2\); it is nonzero and not a unit. The actual triangular shear
and its inverse are
\[
\mathcal V=W-2XZ,\qquad W=\mathcal V+2XZ.
\tag{11}
\]
The full map (2) is equivalent to
\[
Z=S^2-A_XS+B_{X,Y},\qquad \mathcal V=DS+E_0.
\tag{12}
\]
As in310, X,Y,Z are algebraically independent over \(\mathcal F\).
The first equation in (12) is monic quadratic in S, and gives the
exact free module decomposition
\[
\mathcal N=\mathcal C\oplus\mathcal C S,\qquad
S^2=A_XS+(Z-B_{X,Y}).
\tag{13}
\]
One way to see independence is to work over
\(\mathcal F(X,Y,Z)\): the discriminant
\(A_X^2-4B_{X,Y}+4Z\) has exact degree one in the independent
variable Z and is not a rational square. The same equation gives
spanning by monic division. Equivalently, the presentation obtained
by eliminating Z is the polynomial ring \(\mathcal F[X,Y,S]\).

The second equation of (12) now gives
\[
\mathcal R=\mathcal C[DS]
          =\mathcal C\oplus D\mathcal C S.
\tag{14}
\]
For completeness, the indicated right-hand module is closed under
multiplication. In the product of two terms with an S-factor,
\(D^2S^2=D^2(Z-B_{X,Y})+D^2A_XS\) has its S-coefficient
divisible by D. The right-hand module contains \(\mathcal C\)
and DS, and every element of it is generated by these, proving (14).

The ring \(\mathcal N\) is finite and birational over
\(\mathcal R\). Finiteness follows from (13), and birationality from
\(S=(\mathcal V-E_0)/D\). Since \(\mathcal N\) is a polynomial
ring over a field, it is the normalization of \(\mathcal R\).
The proof does not assume that \(\mathcal R\) itself is normal.

The conductor is, by definition,
\(\mathfrak c=\{z\in\mathcal N:z\mathcal N\subseteq\mathcal R\}\).
We claim the exact ideal equality
\[
\mathfrak c=D\mathcal N.
\tag{15}
\]
Write \(z=u_0+u_1S\) uniquely with \(u_0,u_1\in\mathcal C\).
The condition \(z\in\mathcal R\) is \(u_1\in D\mathcal C\).
Also
\[
zS=u_1(Z-B_{X,Y})+(u_0+A_Xu_1)S.
\tag{16}
\]
Given the first condition, \(zS\in\mathcal R\) is equivalent to
\(u_0\in D\mathcal C\). These two conditions suffice for
\(z\mathcal N\subseteq\mathcal R\), by (13).
This proves (15), including both inclusions, without a reduced-fiber
or generic smoothness assertion.

## 4. Stability of the conductor forces its generator to be invariant

Both \(\mathcal R\) and \(\mathcal N\) are E-stable. For
\(z\in\mathfrak c\) and \(c_0\in\mathcal N\),
\[
(Ez)c_0=E(zc_0)-zE(c_0)\in\mathcal R.
\tag{17}
\]
The first term belongs to \(\mathcal R\) because
\(zc_0\in\mathcal R\); the second does because z is in the
conductor and \(E(c_0)\in\mathcal N\). Thus
\(E\mathfrak c\subseteq\mathfrak c\). In particular (15) implies
\[
ED\in D\mathcal N.
\tag{18}
\]

For a locally nilpotent derivation on a characteristic-zero domain,
a nonzero element dividing its own derivative must be invariant.
Indeed, if \(Ef=hf\ne0\), the E-degree satisfies
\(\deg_E(Ef)=\deg_E f-1\), whereas product additivity gives
\(\deg_E(hf)=\deg_E h+\deg_E f\ge\deg_E f\), a contradiction.
Product additivity follows from the nonvanishing highest binomial
term in an iterated derivative over the domain. Apply this elementary
lemma to the nonzero D and the LND (9). Equation (18) forces
\[
ED=0.
\tag{19}
\]

## 5. The full actual action contradicts conductor invariance

Substitute (5) in the explicit D of (10). As a polynomial in the
independent variables X,S,eta over \(\mathcal F\), it is
\[
D=(X+r)\bigl(f'+2T(X+r)-2S\bigr)-\eta.
\tag{20}
\]
The original action (9), which fixes r,f',T,eta, gives
\[
ED=a\bigl(f'-2S+4T(X+r)\bigr)-2b(X+r).
\tag{21}
\]
Since \(a,b\in\mathcal F[\eta]\), its coefficient of S is exactly
\(-2a\ne0\). Thus \(ED\ne0\) in \(\mathcal N\), contrary to (19).

This excludes every actual frame in the precise310 branch.
In particular the finite birational normalization exhibited in310
cannot occur together with the original locally nilpotent
derivation and its actual coordinate action. No assertion that the
normalization equals \(\mathcal R\) was required.

## 6. Scope and independence of verification

The conclusion uses the complete310 entry, including its actual
normalization, nonconstant factor difference, nonzero sigma slope,
Legendre coefficient change, full-X scalar, and exact field return.
It does not treat \(m_s\ne0\), the sigma-constant projected-line
branch, or irreducible cubic surfaces.

The old sliced-kernel hypothesis remains part of the actual entry.
This final conductor step itself requires only the explicit nonzero
LND, its stability on the two displayed rings, and the original
coordinate identities. It uses neither a regular-kernel recognition
theorem nor an assumption that a fraction-field parameter is an
actual coordinate.

The module and conductor calculation and the action (21) were
independently reconstructed by Root before this source was saved.
No saved checker was executed, imported, compiled or rerun. No
retained proof, checker, index or packet was changed, and no
unrestricted cancellation, novelty or formal-verification claim is
made.
