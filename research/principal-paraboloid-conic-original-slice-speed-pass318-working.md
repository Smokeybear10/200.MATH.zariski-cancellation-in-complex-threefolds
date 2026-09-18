# The original-slice and generic-plane consequences of conic scalar rigidity

Working result: retain the full actual reciprocal-conic hypotheses and
conclusions of316. Then both the original speed and the affine generic
parameter speed are units of the exact curve field:
\[
a=EX\in\mathcal F^*,\qquad h=N\sigma=\sigma_v\in\mathcal F^*.
\tag{1}
\]
Moreover the actual polynomial ring, after adjoining that coefficient
field, is exactly a three-variable polynomial ring:
\[
\mathcal F[\mathcal B]=\mathcal F[X,s,\sigma],
\qquad
\mathcal F[A]=\mathcal F[s,\sigma].
\tag{2}
\]
These are subrings of the original fraction field. No normality
assumption on a field-adjoined ring is used to obtain (2).

This is not descent to an original coordinate or recognition of A.
In particular a unit of \(\mathcal F\) is not asserted to be a unit
of the original ring A or \(\mathcal B\).

## 1. Exact hypotheses and polynomial inclusion

Retain the complete actual hypotheses of
[316](principal-paraboloid-conic-factor-unit-scalar-rigidity-pass316-working.md),
not only its scalar identity. In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad a=EX\ne0,\quad Ea=0,\\
0\ne N\in\operatorname{LND}(A),\quad Na=Nt=Ns=0,\quad
L=\operatorname{Frac}\ker_A N,\quad Nv=1,\\
\mathcal F=\ker_L\partial_s,\quad
[\mathcal F:\mathbb C(t)]<\infty,\quad
L=\mathcal F(s),\quad K=\mathcal F(s,\sigma),\quad
L[v]=L[\sigma].
\end{gathered}
\tag{3}
\]
The original generators have exact E-profile \((1,2,2,2)\), and
the full initial kernel is \((X^2Z-Y^2)\). The actual coordinate
expansions and original calibrated determinant are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}&=-a^4 .
\end{aligned}
\tag{4}
\]
All the displayed coefficients are E-invariant. The affine parameter
sigma need not initially belong to the original ring.

Write
\[
\mathscr R=\mathcal F[\mathcal B],\qquad
\mathscr N=\mathcal F[X,s,\sigma].
\]
The polynomial coefficient result316 gives
\[
\mathscr R\subseteq\mathscr N,\qquad
\operatorname{Frac}\mathcal B=\mathcal F(X,s,\sigma),\qquad
\mathcal J:=\det\frac{\partial(y,z,w)}{\partial(t,s,\sigma)}
       =-\frac{a^4}{\sigma_v}\in\mathcal F^* .
\tag{5}
\]
X,s,sigma are algebraically independent over \(\mathcal F\).
No equality or integral extension of the rings in (5) is initially
assumed.

## 2. The original global slice forces a coefficient-field unit

The speed a belongs to \(L=\mathcal F(s)\) by the actual condition
\(Na=0\). It also belongs to \(\mathcal B\subseteq\mathscr N\).
Polynomial independence of X,sigma gives the elementary intersection
\[
\mathscr N\cap\mathcal F(s)=\mathcal F[s].
\tag{6}
\]
For example compare the coefficients of X and sigma over
\(\mathcal F(s)\); then compare the remaining polynomial in s.
Thus \(a\in\mathcal F[s]\).

The original derivation kills \(\mathcal F,s,\sigma\) and sends X
to a. Its extension to the ring \(\mathscr N\) is consequently the
explicit locally nilpotent derivation
\[
E=a(s)\partial_X .
\tag{7}
\]
This conclusion uses polynomiality of a, not any abstract theorem
about extending derivations to normalizations.

Crucially, the original global slice u belongs to
\(\mathcal B\subseteq\mathscr N\). Its defining identity becomes
\[
1=Eu=a(s)\,\partial_Xu
\qquad\text{inside }\mathscr N .
\tag{8}
\]
Hence a is a unit of the polynomial ring \(\mathscr N\), whose units
are exactly \(\mathcal F^*\). This proves the first assertion of (1).
Equation (5) then proves
\[
h=\sigma_v=-a^4/\mathcal J\in\mathcal F^*.
\tag{9}
\]
No slice of a restriction or of the selected derivation N has been
substituted for the original u in (8).

## 3. Actual derivatives prove equality of the coefficient-adjoined rings

The ring \(\mathscr R\) is E-stable: its field coefficients belong
to \(K=\ker E\), and E preserves the original ring. Since \(a^{-1}\)
and t belong to \(\mathcal F\), the literal derivatives of (4) give
\[
s=\frac{E^2W}{2a^2}\in\mathscr R,\qquad
\sigma=\frac{EY}{a}-2tX\in\mathscr R .
\tag{10}
\]
Here \(E^2W=2a^2s\) and \(EY=a(\sigma+2tX)\) use \(Ea=0\).
Since X is already in \(\mathscr R\), (10) proves the reverse
inclusion in (5), and hence the first equality in (2).

Adjoining \(\mathcal F\subseteq K\) to the actual decomposition
\(\mathcal B=A[u]\) gives
\(\mathscr R=\mathcal F[A][u]\), with E acting as \(\partial_u\).
Therefore its E-kernel is \(\mathcal F[A]\). On the other hand,
(7),(8) and the proved equality \(\mathscr R=\mathscr N\) give
\[
\ker(E|_{\mathscr R})=\mathcal F[s,\sigma].
\]
This proves the second equality in (2) inside K. The argument
does not infer either equality from rational-field membership alone.

## 4. The original auxiliary derivation and its exact degree profile

Extend N to the actual ring \(A[u]\) by \(Nu=0\). It then commutes
with E. Define
\[
\mathscr P=aN-(NX)E .
\tag{11}
\]
Both coefficients lie in the original ring. Also
\(E(NX)=N(EX)=Na=0\), so
\([\mathscr P,E]=0\) and \(\mathscr PX=0\).

For completeness, localize only to verify local nilpotence.
Since \(X-au\in A\) and a is a nonzero N-invariant,
\(\mathcal B_a=A_a[X]\). On this presentation \(\mathscr P\)
fixes X and restricts to \(aN\) on \(A_a\), which is locally
nilpotent. Since \(\mathscr P\) preserves \(\mathcal B\), it is
a locally nilpotent derivation of that original ring as well.
This use of localization is not an original coordinate claim.

On the now explicitly identified larger ring, it has the simple form
\[
\mathscr P=(ah)\partial_\sigma
       \quad\text{on }\mathscr R=\mathcal F[X,s,\sigma].
\tag{12}
\]
Indeed it kills \(\mathcal F,s,X\), while
\(\mathscr P\sigma=aN\sigma=ah\). The coefficient ah is a unit of
\(\mathcal F\), although not asserted to be a unit of \(\mathcal B\).
Thus both \(\partial_X\) and \(\partial_\sigma\) preserve
\(\mathscr R\) by coefficient-field rescaling of actual derivations.

Here are the resulting degree bounds with their nonzero coefficients
retained. Write \(T=t-\tau\) and
\(m=d+c/T\), where \(c,d,\tau\in\mathbb C\) and \(c\ne0\), as in316.
The literal conic substitution315 gives
\[
[\sigma^2]\theta=\frac{2cT}{(c+dT)^2},\qquad
[\sigma^2]y=-\frac{dc}{(c+dT)^2},\qquad
[\sigma^3]w=\frac{2c}{(c+dT)^2}.
\tag{13}
\]
For example the last coefficient is
\(-2p/m^2\): in
\[
mw=-\delta\,\sigma\theta+(k_tb_V-n_s)\theta
 +(2b_P-k_{tt}/2)\sigma^2
 +(k_tb_P+2b_0-n_t)\sigma+k_tb_0+\ell
\]
only the first term supplies degree three.
The coefficient of sigma squared in the full actual Z is
\[
z_2=1-\frac{2tdc}{(c+dT)^2}+\frac{2c}{c+dT}\in\mathcal F^*.
\tag{14}
\]
It is nonzero: for \(d=0\) it equals 3; for \(d\ne0\), its
numerator as a polynomial in T has nonzero leading coefficient
\(d^2\).

Because \(\mathscr P\) kills all coefficient-field factors and X,
(13),(14) give the exact auxiliary profiles
\[
\deg_{\mathscr P}(X,Y,Z,W)=
\begin{cases}
(0,2,2,3),&d\ne0,\\
(0,1,2,3),&d=0 .
\end{cases}
\tag{15}
\]
In the second case \(b_V=0\), \((b_P)_s=0\), and the true first
component is
\[
\mathscr PY=ah(X-b_P),\qquad \mathscr P^2Y=0 .
\tag{16}
\]
It is nonzero because X is independent of the coefficient field.
In particular \(\mathscr P\) does not fix the original ring
\(\mathbb C[X,Y]\). No relative two-variable derivation theorem
over that ring is justified by (16).

## 5. Scope

The conclusions are the two coefficient-field units (1), the proved
generic polynomial-plane equalities (2), and the actual commuting
auxiliary derivation with profiles (15). A polynomial coordinate of
\(\mathscr R\) or \(\mathcal F[A]\) has not been promoted to an
original coordinate of \(\mathcal B\) or A.

The degree-one Y in the \(d=0\) auxiliary profile is a possible
further entry point. No global coordinate descent or recognition
follows here solely from this profile or from (2). The reciprocal
conic sector remains subject to the further original-ring endpoint.

The held316 source supplies the exact scalar and polynomial inclusion;
the original expansions and selected derivation are retained from264.
The auxiliary construction was independently rechecked by the explicit
localized presentation above. No saved checker was executed, imported,
compiled or rerun, and no held proof, index or packet was edited.

