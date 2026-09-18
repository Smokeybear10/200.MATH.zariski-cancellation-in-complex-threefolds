# Recognizing the moving cubic graph when the normalized transverse speed varies

The nonconstant-transverse-speed subcase of the moving cubic graph
is recognized. The extra step is not descent of a polynomial
quotient across an invariant denominator. Instead, the actual
graph's field-generation equality forces an invariant polynomial
to be affine-linear in the remaining original coordinate.
The actual good-partial identity then supplies an invariant
ambient coordinate.

The constant nonzero normalized transverse speed is not covered
by this argument. That case has an actual coordinate local slice,
but not the four-element field-generation equality used below.

## 1. Precise retained moving hypotheses

Retain all original hypotheses (1)--(3) of
[the coordinate-local-slice proof](moving-cubic-coordinate-local-slice-pass68.md).
Thus \(B=k[Q_1,Q_2,X,Y]\), \(k=\mathbb C\), has its original
sliced LND \(E\), the supplied good/bad adjoint bounds, independent
defects, and
\[
E^3x=e_1g^3,\qquad L_0E^2x=(1,0)^tg^2,\qquad
g\in\ker E\setminus k,\qquad
\operatorname{rank}(E,V_X,V_Y)=3.
\tag{1}
\]
On \(B_g\), \(\delta=E/g\). The original common kernel is the
actual polynomial curve ring \(k[t]\), with \(g=g_0(t)\), and
\[
\sigma=\delta X,\quad\delta\sigma=1,\qquad
\delta Y=G(t)\in k(t).
\]
Assume in this note that
\[
G\notin k.
\tag{2}
\]
The graph proof already establishes, with complex constants
\(b_0,\kappa,a_2,n_0,l_0\), \(l_0\ne0\), and \(d\in k(t)\),
\[
S=\frac{Q_2-b_0X-\kappa Y^2/2-a_2Y-n_0}{l_0}
 =\sigma+2d(t),\qquad ES=g,
\tag{3}
\]
and the exact field equality
\[
\operatorname{Frac}B=k(t,\sigma,X,Y).
\tag{4}
\]
The coordinate \(S\) on the left of (3) is global and triangular
in the original coordinates. The rational expression on the right
does not alone establish that fact.

## 2. A coordinate-field lemma

Let \(B_0=k[q,z_1,z_2,z_3]\), and let \(D\) be a derivation.
Suppose an actual polynomial \(t\in B_0\) satisfies
\[
\operatorname{Frac}B_0=k(t,z_1,z_2,z_3),\qquad
Dt=0,\qquad Dz_i=v_i(t)\in k[t],\qquad
D(\partial_qt)=0.
\tag{5}
\]
Then \(D\) fixes an actual ambient coordinate of \(B_0\).
No local nilpotence or slice of \(D\) is required for this lemma.

To prove it, put \(R=k[z_1,z_2,z_3]\), \(F=\operatorname{Frac}R\).
Equality (5) says \(F(q)=F(t)\), with \(t\in F[q]\).
For a nonconstant polynomial \(t(q)\), the rational-function
extension has degree \(\deg_qt\). One direct proof is that
\(t(q)-T\) is irreducible in \(F[q,T]\), and remains irreducible
over \(F(T)\) by Gauss's lemma: it is the defining equation of
the polynomial graph \(T=t(q)\), and is primitive over \(F[T]\).
Its \(q\)-degree is therefore the extension degree.
Thus
\[
t=A(z)q+B(z),\qquad A,B\in R,\quad A\ne0.
\tag{6}
\]
The two coefficients lie in \(R\), not just \(F\), because \(t\)
was an actual polynomial in the displayed original coordinate \(q\).
In particular \(t\) is transcendental over \(F\).

The last premise of (5) is \(DA=0\). Expand the three polynomials
\(v_i(T)\) as a finite vector sum
\[
(v_1(T),v_2(T),v_3(T))
=\sum_{j\ge0}c_jT^j,\qquad c_j\in k^3.
\]
Applying \(D\) to the actual polynomial \(A(z)\) gives
\[
0=DA=\sum_{j\ge0}T_{c_j}(A)t^j.
\tag{7}
\]
Transcendence of \(t\) over \(F\) makes every coefficient vanish.
If the vectors \(c_j\) span \(k^3\), all ordinary partials of
\(A\) vanish. Thus \(A\in k^*\), and (6) makes \(t\) a genuine
coordinate, with inverse \(q=(t-B(z))/A\).

If their span has dimension at most two, choose a nonzero
constant linear functional \(\lambda\) annihilating that span.
Then
\[
w=\lambda_1z_1+\lambda_2z_2+\lambda_3z_3
\]
is a genuine linear coordinate of the polynomial three-ring
\(R\), and \(Dw=0\). It remains a coordinate of \(B_0=R[q]\).
This proves the lemma in every rank alternative.

## 3. The moving graph satisfies every lemma premise globally

Let \(f=EX\). Since \(\sigma=f/g\), equation (3) gives
\[
v(t):=2g\,d(t)=gS-f\in B\cap k(t)=k[t].
\]
Similarly the actual bad speed gives
\[
p(t):=EY=gG(t)\in B\cap k(t)=k[t].
\tag{8}
\]
These are contractions of complete actual polynomials to the
proved curve field. Regularity of \(d\) or \(G\) separately is
not assumed.

Perform the further actual triangular shear
\[
X_0=X-\frac{S^2}{2}.
\]
The elements \((Q_1,S,X_0,Y)\) are genuine polynomial
coordinates: first undo \(X=X_0+S^2/2\), then undo (3) to recover
\(Q_2\). Crucially both changes fix the original partial
\(T_1=\partial_{Q_1}\). Their other coordinates do not depend
on the old \(Q_1\).
The original velocities are now
\[
E(S,X_0,Y)=\bigl(g(t),-v(t),p(t)\bigr).
\tag{9}
\]
Also (3)--(4), with \(\sigma=S-2d(t)\) and
\(X=X_0+S^2/2\), give
\[
\operatorname{Frac}B=k(t,S,X_0,Y).
\tag{10}
\]
This is the field-generation premise of (5), not merely a
generic chart guessed from the three displayed velocities.

The original highest good-column identity is \(W_1g=0\).
Because \(g=g_0(t)\) is nonconstant in characteristic zero,
\[
W_1t=0,\qquad E(T_1t)=[E,T_1]t+T_1(Et)=0.
\tag{11}
\]
The actual \(t\) is still fixed by \(E\). Equations (8)--(11)
verify all of (5) for
\[
q=Q_1,\qquad (z_1,z_2,z_3)=(S,X_0,Y),\qquad D=E.
\]
The coordinate-field lemma therefore produces a global ambient
coordinate \(I\in B\) with \(EI=0\).

## 4. Recognize the original kernel, not the divided quotient

Since \(I\) is an actual coordinate, \(B=k[I]^{[3]}\).
The original \(E\) is a locally nilpotent \(k[I]\)-derivation
of that polynomial three-ring and retains the supplied slice
\(s_*\), with \(Es_*=1\). The base \(k[I]\) is a Dedekind
domain containing the rationals.
Derksen, van den Essen and van Rossum, Theorem 4.4, applies in
exactly those hypotheses and gives
\[
\boxed{A=\ker E\simeq k[I]^{[2]}\simeq k^{[3]}.}
\tag{12}
\]
The same original-slice source gate was checked in the
[actual quadratic graph proof](actual-quadratic-graph-cancellation-pass64.md).
No statement that \(A_g\simeq k^{[3]}\) descends to \(A\) is used.
No slice is transferred from \(\delta\) to \(E\).

## 5. Exact remaining boundary

This recognizes the original independent moving cubic sector
satisfying (1) and nonconstant normalized \(G=\delta Y\).
The \(G=0\) case already has the original invariant coordinate
\(Y\). When \(G\in k^*\), the original coordinate \(Y/G\)
satisfies \(E(Y/G)=g\), but it is dependent on \(Y\).
One cannot substitute it for \(S\) in (10) and then invoke the
coordinate-field lemma.

Indeed in that constant case the exact rational common kernel
instead gives
\[
\sigma-Y/G\in k(t),\qquad
EX=(g/G)Y+v_0(t),\quad EY=Gg,\qquad v_0\in k[t].
\tag{13}
\]
These are genuine further necessary identities, not a polynomial
four-coordinate generation theorem.
The nonzero constant \(G\) branch and the original joint-rank-two
branch remain outside the recognition proved here.

## Verification and source scope

This note adds the written coordinate-field lemma and its exact
application to the already established moving graph. The graph
coefficients are inherited from the separate coordinate-local-slice
note; no new numerical checker or method count is asserted.
An outline reconstruction by the parent preceded this saved
transcription. Full saved-file reviews must be recorded separately.

The external recognition input is Harm Derksen, Arno van den Essen
and Peter van Rossum, *The Cancellation Problem in Dimension Four*,
[author-uploaded primary manuscript](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four),
Nijmegen Report 0022, October 2000, Theorem 4.4 and Corollary 4.5,
printed pp. 8--9. The exact theorem hypotheses and complete selected
proofs were directly audited in pass64. This note reuses that
source gate without claiming a fresh full-paper source read.
