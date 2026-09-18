# The independent preceding layers lie in a polynomial two-ring

The independent-defect, nonconstant high-top branch has more structure
than its highest power law alone records. Its last two relevant layers
fit in an actual polynomial two-ring inside the original four-ring.
When the good constant direction kills the top parameter, this lowers
the explicit denominator-clearing exponent of the commuting repair by
one. Neither result identifies that two-ring as an ambient coordinate
plane or removes the exceptional divisor.

## 1. Actual hypotheses and two-row rank

Retain the hypotheses and notation of the
[full independent companion proof](two-quadratic-top-line-pass42.md).
Thus the actual four-ring is \(B=\mathbb C[x_1,x_2,x_3,x_4]\),
the sliced LND is \(E\), the actual good partials have second adjoint
zero, and the two independent bad defects have third adjoint zero.
In the nonzero preceding-bad branch,
\[
E^m x=cg^m,\qquad z=E^{m-1}x,\qquad
L_0z=\lambda g^{m-1},\qquad 3\le m\le5,
\tag{1}
\]
where \(c\ne0\) is a constant good vector, \(\lambda\ne0\)
is a constant two-vector, and \(g\in\ker E\setminus\mathbb C\).
Write
\[
b=L_0E^{m-2}x.
\tag{2}
\]
The full companion \(M\) has one Jordan block of size \(m+1\);
the remaining blocks have total size \(5-m\). Therefore
\(\operatorname{rank}M^{m-1}=2\), including the possible extra
size-two block when \(m=3\). Its four base columns are exactly
\[
\frac1{(m-1)!}
\begin{pmatrix}\operatorname{Jac}z\\
(m-1)\operatorname{Jac}b\end{pmatrix}.
\tag{3}
\]
The lower block follows by multiplying once on the left by the
constant selector \(L_0\). No variable multiplier row is used here.
It follows that \(\operatorname{rank}\operatorname{Jac}(z,b)\le2\).

Choose a good index \(j\) with \(c_j\ne0\), and put
\[
\tau=z_j/c_j,\qquad k=z-c\tau.
\tag{4}
\]
Then \(E\tau=g^m\), \(Ek=0\). A nonzero component of
\(L_0z=\lambda g^{m-1}\) shows that \(dg\) belongs to the
row space in (3). The forms \(d\tau,dg\) are independent:
evaluate on \(E\) and use \(dg\ne0\). Consequently the row
space in (3) is exactly their span.

Since \(Eb=\lambda g^{m-1}\), for a rational two-vector
\(\omega\) we have
\[
db=(\lambda/g)d\tau+\omega\,dg.
\tag{5}
\]
Thus the polynomial two-vector
\[
q=gb-\lambda\tau
\tag{6}
\]
satisfies \(dq_i\wedge dg=0\). All \(dk_i\) likewise belong
to the one-dimensional subspace annihilating \(E\). Hence
\[
\operatorname{trdeg}_{\mathbb C}
\mathbb C[g,k_1,k_2,k_3,k_4,q_1,q_2]=1.
\tag{7}
\]

## 2. A genuine polynomial two-parameter normal form

The polynomial curve-factorization theorem, applied only after (7),
gives an actual nonconstant \(u\in B\) and univariate polynomials
\(G,K_i,Q_i\) such that
\[
g=G(u),\quad k=K(u),\quad q=Q(u).
\tag{8}
\]
Its conclusion also gives
\(\mathbb C(u)\cap B=\mathbb C[u]\).[^curve]
Every derivation killing \(g\) kills \(u\), since
\(G'(u)\ne0\). In particular \(Eu=V_3u=V_4u=0\).
The vanishing of the defects on \(g\) is part of the inherited
highest-coefficient identities, not a consequence of a coordinate
claim about \(u\).

Choose an index \(i\) with \(\lambda_i\ne0\), and define the
actual polynomial
\[
v=b_i/\lambda_i,\qquad r(u)=Q_i(u)/\lambda_i.
\tag{9}
\]
Then
\[
\tau=g v-r(u),\qquad Ev=g^{m-1}.
\tag{10}
\]
For any component of \(b\), (6) and (10) give
\[
b_\ell-\lambda_\ell v
=\frac{Q_\ell(u)-\lambda_\ell r(u)}{G(u)}
\in B\cap\mathbb C(u)=\mathbb C[u].
\tag{11}
\]
There is therefore a univariate vector \(L\) with \(L_i=0\),
and a univariate good/bad four-vector \(F=K-cr\), such that
\[
\boxed{\quad
g=G(u),\qquad z=cG(u)v+F(u),\qquad b=\lambda v+L(u).
\quad}
\tag{12}
\]
The elements \(u,v\) are algebraically independent: \(Eu=0\)
whereas \(Ev=G(u)^{m-1}\ne0\), so differentiating a minimal
algebraic equation for \(v\) over \(\mathbb C(u)\) would
contradict characteristic zero. Thus \(\mathbb C[u,v]\) is an
actual polynomial two-ring containing the two displayed layers.

Neither \(u\) nor \(v\) is asserted to be an ambient coordinate.
In particular, (12) is not a proof that \(B\) is polynomial over
\(\mathbb C[u,v]\), nor that a special fiber of their inclusion
is reduced or irreducible.

## 3. A lower-exponent polynomial commuting repair

Now assume \(T_cg=0\), put \(a=(m-1)/2\), and use the
global fields from the
[Heisenberg construction](quadratic-heisenberg-repair-pass43.md):
\[
W=[E,T_\lambda],\quad V=[E,W]\ne0,\quad
Y=gT_c+2aW,
\qquad [E,Y]=aV,\quad [E,V]=[Y,V]=0.
\tag{13}
\]
All three fields are polynomial LNDs; \(Eg=Vg=Yg=0\).
The same next-to-top identity gives \(V\tau=0\).
By (8), \(Vu=Yu=0\). Consequently (10) implies \(Vv=0\)
and \(Y\tau=gYv\).

On the actual invariant localization \(B_g\), set
\[
\delta=E/g,\quad L'=Y/g,\quad C'=aV/g^2,\qquad
\sigma=v/g^{m-2}.
\tag{14}
\]
These are LNDs, \([\delta,L']=C'\) is central,
\(\delta\sigma=1\), and \(C'\sigma=0\). The already proved
compatible Heisenberg projection is therefore an LND
\[
D_0=L'-\sigma C'-(L'\sigma)\delta.
\]
It kills \(g\). Clearing by \(g^m\), rather than
\(g^{m+1}\), gives the polynomial LND
\[
\boxed{\quad
\mathcal R_1=g^{m-1}Y-a vV-(Yv)E.
\quad}
\tag{15}
\]
Restriction from \(B_g\) proves local nilpotence on \(B\),
and the same construction gives
\[
[E,\mathcal R_1]=[V,\mathcal R_1]=0,\qquad
\mathcal R_1g=\mathcal R_1v=0.
\tag{16}
\]
The previously constructed field satisfies the exact comparison
\[
\mathcal R_{43}=g\mathcal R_1+a r(u)V.
\tag{17}
\]
The correction in (17) is an invariant multiple of the same central
direction. Thus the new field has the same fraction-field rank as
the old one modulo \(E,V\). It cannot by itself repair the rank-two
case. It also need not be primitive or free.

For the original action, (10) gives the compatible localized slice
\(v/g^{m-1}\), improving the explicit displayed power by one.
It still inverts \(g\). This is a smaller denominator, not removal
of the common divisorial support of the slice obstruction.

## Verification and remaining boundary

The proof uses the entire base-column matrix in (3), ordinary
differentials, a source-gated curve factorization, and the previously
proved global Heisenberg projection. Formal Jordan matrices are only
rank controls, not examples realizing the polynomial action.
No additional independent intrinsic direction, primitive freeness,
ambient coordinate, or unrestricted frame-existence assertion is made.
The complex threefold cancellation target remains open in this work.
No novelty or human or proof-assistant review is claimed.

[^curve]: Michiel de Bondt,
[*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046v4),
Corollary 3.2 with proof and Lemma 3.3, PDF pp. 20--21.
The actual theorem gives a polynomial parameter inside the original
ring and the intersection identity used in (11); it does not give
ambient coordinate status.
