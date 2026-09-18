# Polynomial entry for the genuine quartic graph in the quadratic-cubic chart

The genuine degree-four graph component left by263 is recognized.
An actual complex-coefficient shear isolates a new coefficient
parameter. The scalar determinant then makes the intercept \(z\)
polynomial in that parameter; a coefficient of the full determinant
makes the old parameter \(\lambda\) affine in it. This produces
polynomial entry over an invariant curve field, exactly as required
by266, and hence an actual invariant coordinate.

The statement is restricted to the affine-first quartic graph.
The quadratic-first quartic embedding and lower-degree selected
components are not included.

## 1. Actual hypotheses and retained graph restrictions

Use the complete actual chart258 and its
[whole-plane reduction263](two-affine-quadratic-cubic-whole-plane-cofactor-pass263-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,
\quad K=\operatorname{Frac}A,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\quad a=EX\ne0,\\
\operatorname{ht} I_{\mathrm{initial}}=2,\quad
\operatorname{shift}(\partial_Z)=3,\quad
N\ne0,\quad Nv=1,\quad L=\operatorname{Frac}\ker_A N,\\
K=L(v),\quad [L:\mathbb C(t,\lambda)]<\infty,\quad
L[y,\psi]=L[v],\quad \psi=\theta-r''y^2/2.
\end{gathered}
\tag{1}
\]
The initial ideal in (1) is the full weighted initial kernel.
The actual expansions and calibration are
\[
\begin{aligned}
Y&=y+tX,\\
Z&=z+(q'y+k)X+qX^2,\\
W&=w+\theta X+(r'y+\lambda)X^2+rX^3,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,\lambda,v)}
   &=-a^3\in L^* .
\end{aligned}
\tag{2}
\]
The coefficient partials on \(L\) commute and initially fix \(v\);
\(q,r\) are algebraic over \(\mathbb C(t)\).

Assume precisely the present branch:
\[
m=k_\lambda\ne0,\quad q'''\ne0,\qquad
\deg G=4,\quad \deg_v y=1,\quad
\psi=P_4(y),\quad P_4\in L[U],\quad\deg P_4=4,
\tag{3}
\]
where \(G\) is the irreducible generator of the projected
evaluation ideal. The polynomial \(\mathcal H\) of258 was not
assumed irreducible. Its evaluated-unit cofactor from263 gives
\(\mathcal H=\eta G\) in this degree-four branch.

Let \(F=\ker_L\partial_\lambda\). The exact finite-field argument
of262 gives
\([F:\mathbb C(t)]<\infty\), with prime constants \(\mathbb C\).
The restrictions already proved in263 are
\[
\begin{gathered}
m_\lambda=0,\qquad e:=1/m=\alpha t+\beta,\qquad
\nu:=n_\lambda=\gamma m^2,\\
k=m\lambda+k_0,\qquad n=\nu\lambda+n_0,\qquad
k_0,n_0\in F,\quad \alpha,\beta,\gamma\in\mathbb C.
\end{gathered}
\tag{4}
\]
The affine function \(e\) is nonzero, while \(\gamma\) may vanish.
Primes henceforth mean the unique \(t\)-derivative on \(F\).
No rationality of \(F\) is assumed.

The quartic coefficient and the constant \(V\)-derivative of
\(\mathcal H\) are
\[
a_4=\frac{q''''-mr''''-4q'''m'/m}{24}\ne0,\qquad
\mathcal H_V=-\ell_\lambda-\nu^2/m\ne0.
\tag{5}
\]
The first assertion follows because \(\deg\mathcal H=4\).
The second follows from \(G\sim V-P_4(U)\).
Also \(y_v\in L^*\), and
\[
z=mP_4(y)+q''y^2/2+k_ty+n
\]
has degree exactly four in \(y\).

## 2. An actual shear and its full literal coefficients

For a coefficient-field variable \(U\), the first two potentials
specialized using \(m_\lambda=0\) are
\[
\begin{aligned}
f(U)&=(q''-r''m)U^2/2+k_tU+n,\\
P(U)&=(q'''-mr'''-3r''m')U^3/6
          +(k_{tt}-r''\nu)U^2/2+n_tU,\\
z&=m\theta+f(y),\qquad
mw=\ell-(m'y+\nu)\theta-P(y).
\end{aligned}
\tag{6}
\]
Define elements of the exact coefficient fields by
\[
R=r-eq,\qquad
\Lambda=\gamma q-ek_0,\qquad
K_0=\gamma k_0-en_0,\qquad
S=e\ell+\gamma^2m^2\lambda .
\tag{7}
\]
The first three belong to \(F\); \(S\) initially belongs only
to \(L\). Use the following two polynomials over \(F\):
\[
\begin{aligned}
B_0(U)&=\frac{R'''}6U^3+\frac{\Lambda''}2U^2+K_0'U+\gamma n_0,\\
C_1(U)&=\frac{R''}2U^2+\Lambda'U+K_0 .
\end{aligned}
\tag{8}
\]
Here \(B_0\) is a polynomial label, not the original ambient ring.
The coefficient identities needed later include
\[
(B_0)_U=(C_1)_t,\qquad
b_3:= [U^3]B_0=R'''/6,\qquad
b_3'=R''''/6=-4e a_4\ne0.
\tag{9}
\]

The shear
\[
\boxed{J=W-(\alpha Y+\beta X-\gamma)Z}
\tag{10}
\]
is an actual polynomial coordinate change over \(\mathbb C\).
It retains \(X,Y,Z\), and its inverse is
\(W=J+(\alpha Y+\beta X-\gamma)Z\).
Substitution in either direction is the identity.

The complete literal expansion of this new coordinate is
\[
\boxed{
J=S+B_0(y)+C_1(y)X+(R'y+\Lambda)X^2+RX^3 .
}
\tag{11}
\]
Here are explicit checks that retain every old coefficient.
From (4), \(m'=-\alpha m^2\) and \(\nu'=-2\alpha\gamma m^3\).
Eliminating \(\theta\) from (6) first gives
\[
w=(\alpha y-\gamma)z+S+B_0(y).
\tag{12}
\]
To verify its cancellation in \(\lambda\), write
\[
f=f_0+\lambda m^2(\gamma-\alpha U),\qquad
f_0=(q''-r''m)U^2/2+k_0'U+n_0.
\]
The coefficient of \(\lambda\) in
\((\gamma-\alpha U)f-P/m\) is
\[
m^2(\gamma-\alpha U)^2-\frac{m''}{2m}U^2-\frac{\nu'}mU
=\gamma^2m^2.
\]
This is exactly the term included in \(S\).
The remaining coefficients in (12) are
\[
\begin{aligned}
[U^3]B_0&=(r'''-eq'''-3\alpha q'')/6,\\
[U^2]B_0&=\gamma q''/2-\alpha k_0'-ek_0''/2,\\
[U]B_0&=\gamma k_0'-\alpha n_0-en_0',\qquad
[1]B_0=\gamma n_0,
\end{aligned}
\tag{13}
\]
which agree with (8).

Substituting the literal \(Y,Z,W\) of (2) into (10), its
coefficient of \(z\) is
\((\alpha y-\gamma)+eX=\alpha Y+\beta X-\gamma\).
The remaining coefficient of \(X\) is \(C_1(y)\):
\[
C_1(U)=\frac{R''}{2}U^2+
 (\gamma q'-ek_0'-\alpha k_0)U+\gamma k_0-en_0 .
\]
At \(X^2\), the term \(-ek\) cancels \(+\lambda\), leaving
\(R'y+\Lambda\). The cubic coefficient is \(R\).
This proves (11) without omitting any \(\lambda\)-dependent term.

For future reference define a polynomial over the curve field by
\[
\mathscr P(X,Y)=B_0(Y-tX)+C_1(Y-tX)X+
        \{R'(Y-tX)+\Lambda\}X^2+RX^3 .
\tag{14}
\]
Then (11) is the actual identity \(J=S+\mathscr P(X,Y)\).
It does not by itself give polynomial entry over \(F\):
at this point \(S\) is a second coefficient parameter.
Nor is \(\mathscr P\) claimed to have complex coefficients.

## 3. The exact new parameter and its calibrated determinant

Equation (5) gives
\[
S_\lambda=e\ell_\lambda+\gamma^2m^2
          =-e\mathcal H_V\ne0 .
\tag{15}
\]
Hence \(S\) is transcendental over \(F\), \(L/F(S)\) is finite,
and the commuting new coefficient partials are
\[
\partial_S=S_\lambda^{-1}\partial_\lambda,\qquad
\partial_t^{\,S}
  =\partial_t^{\,o}-\frac{S_t^{\,o}}{S_\lambda}\partial_\lambda,
\qquad \ker_L\partial_S=F .
\tag{16}
\]
This follows exactly as in262: they are the unique extended
partials on the finite separable extension of \(\mathbb C(t,S)\).
On \(F\), the new \(t\)-derivative is the old prime derivative.
From now on subscripts \(t,S\) use these new partials, with
the formal polynomial parameter \(y\) held fixed.

The actual shear (10) has determinant one on the fixed-\(X\)
three rows. The changes from \(v\) to \(y\) and then from
\(\lambda\) to \(S\) give
\[
\mathfrak J:=
\det\frac{\partial(Y,Z,J)}{\partial(t,S,y)}
 =-\frac{a^3}{S_\lambda y_v}\in L^* .
\tag{17}
\]
It is independent of \(X,y\); it need not be a complex constant.
The shear may change the literal selected partial, but no old
maximal-shift claim is applied to the new coordinate frame.
We use only the already proved identities (2),(6),(11),(17).

## 4. The scalar coefficient makes \(z\) polynomial in \(S\)

Write \(B_0(U)=\sum_{i=0}^3b_iU^i\), with all \(b_i\in F\),
and write the quartic intercept as
\[
z=\sum_{i=0}^4 z_i y^i,\qquad z_i\in L,\quad z_4\ne0 .
\]
At \(X=0\), the first row is \((0,0,1)\) and
\(J=S+B_0(y)\). Thus (17) gives
\[
\mathfrak J=z_t-(B_0)_t z_S .
\tag{18}
\]
Its coefficients of \(y^7,y^6,y^5\), successively, are
\[
-b_3'(z_4)_S,\qquad
-b_3'(z_3)_S-b_2'(z_4)_S,\qquad
-b_3'(z_2)_S-b_2'(z_3)_S-b_1'(z_4)_S .
\tag{19}
\]
They vanish. Since \(b_3'\ne0\) by (9), exact constant fields
in (16) give \(z_4,z_3,z_2\in F\).
The next two coefficients are
\[
z_4'-b_3'(z_1)_S=0,\qquad
z_3'-b_3'(z_0)_S-b_2'(z_1)_S=0 .
\tag{20}
\]
Therefore \((z_1)_S,(z_0)_S\in F\).
Subtract their explicit linear primitives and use
\(\ker_L\partial_S=F\). We obtain
\[
\boxed{z\in F[S,y],\quad z_4,z_3,z_2\in F,\quad
          z_1,z_0\in F+FS.}
\tag{21}
\]
No equality \(L=F(S)\) was assumed to justify these integrations.

## 5. One full-\(X\) coefficient makes \(\lambda\) affine in \(S\)

Let \(H=\lambda\in L\), now viewed over \(F(S)\). The other
literal coordinate is
\[
Z=z+(q'y+k_0+mH)X+qX^2 .
\tag{22}
\]
Use the full rows of \(Y=y+tX\), (22), and (11), with
columns \(t,S,y\). Direct expansion of the determinant gives
\[
\begin{aligned}
[X]\mathfrak J={}&mH_t+m'H-m(B_0)_tH_S-z_y+q''y+k_0'\\
&+z_S\{(B_0)_y-(C_1)_t\}.
\end{aligned}
\tag{23}
\]
For example the determinant itself is
\(X(Z_SJ_y-Z_y)+Z_t-Z_SJ_t\), since \(J_S=1\) and
the first row is \((X,0,1)\).
Equation (9) cancels the last line of (23).
Since \(\mathfrak J\) is independent of \(X\), its coefficient
of \(Xy^3\) is zero:
\[
-mb_3'H_S-4z_4=0,\qquad
H_S=-\frac{4z_4}{mb_3'}\in F^* .
\tag{24}
\]
The nonzero assertion uses \(m,b_3',z_4\ne0\).
Exact integration in the field \(L\) now yields
\[
\boxed{\lambda=H=h_1S+h_0,\qquad h_1\in F^*,\ h_0\in F.}
\tag{25}
\]
This is the needed polynomial parameter transport, not a
rational-field assumption.

## 6. Actual polynomial entry and recognition

In the actual coordinate frame \((X,Y,Z,J)\), put
\[
\widehat y=Y-tX,\qquad
\widehat S=J-\mathscr P(X,Y).
\]
Equations (14),(21),(22),(25) give the explicit polynomial
membership
\[
\boxed{
Z=\sum_{i=0}^4z_i(\widehat S)\widehat y^{\,i}
 +\{q'\widehat y+k_0+m(h_1\widehat S+h_0)\}X+qX^2
 \ \in F[X,Y,J].
}
\tag{26}
\]
The coefficients \(z_i(\widehat S)\) are polynomial by (21).
Every other coefficient in (26) belongs to \(F\).
The field \(F\) is a finitely generated invariant curve field
inside \(\operatorname{Frac}A\).

Apply the fully read
[curve-field polynomial-entry criterion266](curve-field-polynomial-entry-criterion-pass266-working.md),
with \(Z\) as its dependent actual coordinate and \(X,Y,J\)
as its other three coordinates. It supplies
\(P_0\in\mathbb C[X,Y,J]\) such that
\[
I=Z-P_0(X,Y,J)\in A,\qquad
B=\mathbb C[X,Y,J,I],\qquad A\simeq\mathbb C^{[3]} .
\tag{27}
\]
The combined inverse to the actual coordinate changes is
\[
Z=I+P_0(X,Y,J),\qquad
W=J+(\alpha Y+\beta X-\gamma)
                \{I+P_0(X,Y,J)\},
\tag{28}
\]
with \(X,Y\) retained. Substituting (10),(27) into (28)
returns \(Z,W\); substituting (28) into (10),(27) returns \(J,I\).
Thus the conclusion is in the original polynomial ring.
No coefficient of \(\mathscr P\) was prematurely forced to
be complex, and neither \(S\) nor a parameter of \(F\) was
declared to be an ambient coordinate.

## 7. Boundary and verification

This recognizes exactly the genuine quartic graph component
in (3), with all chart and actual hypotheses in (1),(2).
The condition \(R''''\ne0\) is essential in the degree argument
used here and follows from genuine quartic degree, not from
an assumption that a lower graph cannot occur.
The quadratic-first quartic embedding and lower-degree selected
components remain separate. Nothing here supplies arbitrary
entry into the maximal-pivot chart or recognizes all1123 frames.

The complete258,263 and266 sources were read.
Unsaved direct substitution independently rebuilt the actual
shear (11), the identity \((B_0)_y=(C_1)_t\), the complete
coefficient (23), and its \(y^3\) coefficient (24), retaining
arbitrary coefficient functions before their proved restrictions.
These checks do not prove the exact-field integrations or the
polynomial-entry theorem. No previous source, packet or index
was edited, and no saved checker was executed, imported or
compiled. No historical novelty, human expert certification
or unrestricted cancellation result is claimed.

