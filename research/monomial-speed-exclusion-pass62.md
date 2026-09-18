# Exact monomial speeds with gcd at most two are excluded

Under the full actual quadratic-frame hypotheses, exact monomial
bad speeds \(f=a^p,\ g=b^q\) in genuine coordinates of
\(C=\mathbb C[a,b]\) cannot occur when \(\gcd(p,q)\le2\).

The proof extends the square-speed argument without treating
\(a^{p/d},b^{q/d}\) as coordinates. A primitive weighted monomial
gives the actual rational invariant field, which is the missing
gate in a direct substitution into the square-speed proof.

This concerns exact global monomials with positive integer
exponents. It does not cover their initial forms, monomials
multiplied by arbitrary units, general ramified germs, or an
unspecified algebraic extension of the invariant field.

## 1. Actual setup and the statement

Retain the full hypotheses and actual conclusions of
[the generic bad-pair theorem](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,X,Y]=\mathcal A[s_*],\qquad Es_*=1,
\]
\[
C=\mathbb C[a,b],\qquad L=\mathbb C(a,b),\qquad
B_L=L[X,Y],\qquad B\cap L=C,
\]
\[
f=EX=a^p,\qquad g=EY=b^q,\qquad
E=f\partial_X+g\partial_Y\quad\hbox{on }B_L,
\quad p,q\in\mathbb Z_{>0}.
\tag{1}
\]
In particular \(X,Y\) are the actual bad coordinates, not a
chosen pair of generators over \(C\). The true good-column
equations give
\[
Q_i=x_i=
\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)\binom XY
+(\nabla_{f,g}k_i)\binom XY+\ell_i,
\]
\[
h_i=E^2x_i\in C,\qquad k_i,\ell_i\in L,\qquad
\mathscr Hh_i=2h_i,\qquad \mathscr Hk_i=k_i,
\tag{2}
\]
where the unique extended field partials are
\[
\partial_f=\frac{1}{p a^{p-1}}\partial_a,\qquad
\partial_g=\frac{1}{q b^{q-1}}\partial_b,
\qquad
\mathscr H=f\partial_f+g\partial_g
=\frac ap\partial_a+\frac bq\partial_b.
\tag{3}
\]
The actual Schur condition and the actual coordinate field are
\[
Q_{(f,g)},\ Q_{(f,g)}^{-1}
 \in\operatorname{Mat}_2(L[X,Y]),\qquad
\det Q_{(f,g)}\in L^*,
\]
\[
\mathbb C(Q_1,Q_2,X,Y)=\operatorname{Frac}B=L(X,Y).
\tag{4}
\]
The polynomial inverse condition follows from the true
ambient partials. The fraction-field equality uses the
original complex polynomial coordinates. Neither is inferred
from an arbitrary four-generator quadratic presentation.

**Theorem.** The data (1)--(4) are inconsistent if
\[
d=\gcd(p,q)\in\{1,2\}.
\tag{5}
\]

The original supplied slice is retained throughout. There is no
second-image-ideal, plinth, closed-fiber, or affine-slice premise.

## 2. The exact weighted field and its polynomial eigenfunctions

Write
\[
p=du,\qquad q=dv,\qquad \gcd(u,v)=1,\qquad
U=a^u,\quad V=b^v,\quad r=V/U.
\tag{6}
\]
Thus \(f=U^d,\ g=V^d\). The elements \(U,V\) are algebraically
independent polynomials but need not be coordinates of \(C\).
In particular \(L=\mathbb C(U,r)\) is not asserted.

Choose integers \(m,n\) with
\(vm+un=1\), and put \(z=a^m b^n\in L\).
Negative exponents are permitted in this rational field.
Direct substitution gives
\[
a=r^{-n}z^v,\qquad b=r^m z^u,\qquad
L=\mathbb C(r,z),
\]
\[
\mathscr Hr=0,\qquad
\mathscr Hz=\frac{z}{duv},\qquad
\mathscr H=\frac{z}{duv}\partial_z
\quad\hbox{at fixed }r.
\tag{7}
\]
The inverse monomial identities show that \(r,z\) are a
rational coordinate pair in the actual field \(L\), not
merely in a subfield of it. Hence
\[
\boxed{\ker_L\mathscr H=\mathbb C(r).}
\tag{8}
\]
Indeed a rational function of \(z\) over the characteristic-zero
field \(\mathbb C(r)\) with zero derivative is constant in \(z\).
This proves the kernel statement without adjoining unrecorded
roots or using a curve parametrization theorem.

For a polynomial monomial \(a^i b^j\), its Euler weight is
\((vi+uj)/(duv)\). If it has positive integral weight
\(e\in\{1,2\}\), then
\[
vi+uj=eduv.
\]
Reducing modulo \(u\) and modulo \(v\) gives
\(u\mid i\) and \(v\mid j\), respectively. Thus
\[
i=uI,\quad j=vJ,\quad I,J\ge0,\quad I+J=ed.
\]
Since \(\mathscr H\) is diagonal on polynomial monomials,
coefficient comparison proves
\[
\{c\in C:\mathscr Hc=e c\}=\mathbb C[U,V]_{ed},
\qquad e=1,2.
\tag{9}
\]
Here the subscript denotes exact homogeneous degree; the zero
element is included. Positivity of both weights also gives
\[
\{c\in C:\mathscr Hc=0\}=\mathbb C.
\tag{10}
\]

For rational \(k\in L\) with \(\mathscr Hk=k\), division
by the nonzero weight-one element \(f\) and (8) give
\[
k=f\,d_0(r),\qquad d_0(r)\in\mathbb C(r).
\tag{11}
\]
This conclusion is rational. It does not put \(k\) in \(C\).

Finally,
\([\mathscr H,\partial_f]=-\partial_f\) and
\([\mathscr H,\partial_g]=-\partial_g\), either directly
from (3) or by their actions on the finite separable speed
field extension. Thus the Hessian coefficients in (2) and
the gradient coefficients there have weight zero and belong
to \(\mathbb C(r)\).

## 3. Coprime exponents: all graph coefficients become regular

Suppose \(d=1\). Formula (9) makes each actual acceleration
\[
h_i\in\mathbb C[U,V]_2=\mathbb C[f,g]_2.
\]
Therefore its Hessian in \(f,g\) has constant complex
entries and its gradient lies in \(C^2\).

The rational \(k_i\) must first be recovered from the
actual velocity. Differentiating (2) by \(E\) gives
\[
EQ_i=\frac12(\nabla_{f,g}h_i)\binom XY+k_i.
\tag{12}
\]
For this calculation, Euler differentiation gives
\(\operatorname{Hess}(h_i)(f,g)^{\mathsf t}=\nabla h_i\),
and \((\nabla k_i)(f,g)^{\mathsf t}=k_i\).
The displayed actual difference in (12) shows
\(k_i\in B\cap L=C\). Now (9) with \(e=1\) gives
\(k_i\in\mathbb C[f,g]_1\), so \(\nabla k_i\) is
constant. Subtracting both regular graph parts in (2)
then gives \(\ell_i\in C\).

Let \(R=C_{(a,b)}\). All four actual generators now lie in
\(R[X,Y]\), and hence
\[
B_R=R[X,Y].
\tag{13}
\]
But \(E(B_R)\subseteq(f,g)R[X,Y]\). The original
\(Es_*=1\), followed by evaluation at \(X=Y=0\), would
put \(1\) in the proper ideal \((a^p,b^q)R\).
This contradiction proves the theorem for \(d=1\).

It uses no claim that \(f,g\), \(U,V\), or any primitive
weighted monomial are coordinates of the invariant plane.

## 4. The gcd-two graph and the full determinant lemma

Now suppose \(d=2\). Then
\[
f=U^2,\qquad g=V^2,\qquad h_i\in\mathbb C[U,V]_4.
\tag{14}
\]
On \(\mathbb C(U,V)\), the actual field partials restrict
to the square partials:
\[
\partial_fU=\frac1{2U},\quad \partial_fV=0,\qquad
\partial_gU=0,\quad \partial_gV=\frac1{2V}.
\]
Their action on the full \(L\) remains the actual unique
extension, not an assumed equality of fields.

Write the odd quartic coefficient vectors as
\[
h_i=c_{i0}U^4+\alpha_iU^3V+c_{i2}U^2V^2
+\beta_iUV^3+c_{i4}V^4.
\]
The even part is in \(\mathbb C[f,g]_2\), so its graph
contribution is a complex quadratic polynomial in \(X,Y\).
Subtracting it is a genuine polynomial good-coordinate shear.
Constant invertible changes of the good coordinates are also
allowed. They retain the graph equations, determinant condition,
and actual coordinate generation used below. No preservation
of every original bad-adjoint bound is claimed.

By (8) and the coefficient weights, after these changes write
\[
Q=S(r;X,Y)+\ell,\qquad
S\in\mathbb C(r)[X,Y]^2,
\tag{15}
\]
where \(S\) contains only the linear and quadratic terms
and \(\ell\in L^2\) remains arbitrary.

Set
\[
A_0=\ell_{(f,g)},\qquad
\lambda=\nabla_{f,g}r
=\left(-\frac{r}{2f},\frac1{2fr}\right).
\]
Then
\[
Q_{(f,g)}=A_0+S_r\lambda.
\]
Its determinant in \(L^*\), evaluated at \(X=Y=0\),
makes \(A_0\) invertible. The rank-one determinant identity
gives \(\lambda A_0^{-1}S_r=0\).
Since \(\ker\lambda=L(f,g)^{\mathsf t}\), this says
\[
\boxed{\det[\,\mathscr H\ell\mid S_r\,]=0,\qquad
\mathscr H\ell=A_0(f,g)^{\mathsf t}\ne0.}
\tag{16}
\]
In particular every coefficient vector, both quadratic and
linear, of \(S_r\) lies on the line through \(\mathscr H\ell\).
This uses the full determinant, not only its highest coefficient.

The two square identities that enter the rank split are
\[
F_1=\frac{3rX^2+6XY/r-Y^2/r^3}{16},\qquad
F_2=\frac{-r^3X^2+6rXY+3Y^2/r}{16},
\]
\[
(F_1)_r=\frac3{16}(X-Y/r^2)^2,\qquad
(F_2)_r=-r^2(F_1)_r.
\tag{17}
\]
They are the Hessian graph pieces for \(U^3V\) and \(UV^3\).
They are computed in the subfield \(\mathbb C(U,V)\), where
the actual partials have exactly the required values.

## 5. Two independent odd coefficients: the full field contradiction

If the matrix with rows \((\alpha_i,\beta_i)\) has rank two,
a constant good-output change puts the odd pair at
\((U^3V,UV^3)\). Equations (16)--(17) imply
\[
\mathscr H\ell_2=-r^2\mathscr H\ell_1,\qquad
\mathscr H\ell_1\ne0.
\]
The actual kernel (8), not a subfield kernel, therefore gives
\[
\ell_2+r^2\ell_1=I(r),\qquad I(r)\in\mathbb C(r).
\]
Combining the two rows of the graph yields
\[
Q_2=-r^2Q_1+
 \frac{r^3X^2+6rXY+Y^2/r}{8}
 +A(r)X+B(r)Y+I(r),
\quad A,B\in\mathbb C(r).
\tag{18}
\]

The independence argument must use (7). The coefficients of
\(S\) are killed by \(\mathscr H\), so
\(\mathscr HQ_1=\mathscr H\ell_1\ne0\).
Since \(L=\mathbb C(r,z)\) and
\(\mathscr H=z\partial_z/(duv)\), the element \(Q_1\) is
a nonconstant rational function of the transcendental \(z\)
over \(\mathbb C(r,X,Y)\). It is therefore transcendental
over that field. Explicitly, a nonconstant rational function
of \(z\) makes \(z\) algebraic over the field it generates;
if that function were algebraic over the coefficient field,
\(z\) would be algebraic there as well, a contradiction.

Thus \(Q_1,r,X,Y\) are algebraically independent.
Put \(K=\mathbb C(Q_1,X,Y)\).
Equation (18) is a rational function of \(r\) over \(K\)
with a pole of order at least three at infinity and at
least one at zero. These lower bounds are forced by
\(r^3X^2/8\) and \(Y^2/(8r)\), respectively. The arbitrary
rational additions are at most linear in the independent
\(X,Y\), while \(-r^2Q_1\) is linear in the independent
\(Q_1\). They cannot cancel either indicated quadratic
monomial in the Laurent coefficients. Additional poles
can only increase the degree.

Consequently
\[
[K(r):K(Q_2)]\ge4.
\tag{19}
\]
For clarity, the field-degree fact is elementary. For reduced
nonconstant \(P(r)/T(r)\), let \(\theta\) be an indeterminate.
The polynomial \(P(Z)-\theta T(Z)\) is irreducible in
\(K[Z,\theta]\): a factor independent of \(\theta\) would
divide both \(P,T\). Gauss's lemma gives degree
\(\max(\deg P,\deg T)\) over \(K(\theta)\), equal to the
total pole degree. The two distinct poles just found sum
to at least four.

On the other hand actual generation (4) gives, with
\(M=L(X,Y)\),
\[
M=K(Q_2),\qquad
K(Q_2)\subseteq K(r)\subseteq M.
\tag{20}
\]
The second inclusion uses \(r\in L\), not
\(L=\mathbb C(U,r)\). Both inclusions must be equalities,
contradicting (19). This excludes the rank-two odd sector
even when \(L/\mathbb C(U,V)\) is a proper finite extension.

## 6. Rank one and rank zero: delayed actual regularity

Suppose the odd coefficient matrix has rank one.
A constant good-output change puts the nonzero odd part
in row one and zero in row two. Its quadratic \(r\)-derivative
is
\[
(\alpha-\beta r^2)(F_1)_r,\qquad
(\alpha,\beta)\ne(0,0),
\]
which is nonzero. Equation (16) forces
\(\mathscr H\ell\) to the first coordinate line, and then
forces every linear coefficient vector of \(S_r\) to that
line as well. Therefore
\[
\mathscr H\ell_2=0,\qquad (S_2)_r=0.
\]
The second row has no quadratic part. Its two linear
coefficients belong to \(\mathbb C(r)\) and have zero
\(r\)-derivative, so they are complex constants. Thus
\[
Q_2=c_1X+c_2Y+\ell_2,\qquad c_1,c_2\in\mathbb C.
\]
Only now does actualness show \(\ell_2\in B\cap L=C\).
Equation (10) then makes \(\ell_2\) constant. This
contradicts independence of the actual coordinate list.

Finally suppose the odd rank is zero. After the even
quadratic shears,
\[
Q_i=(\nabla_{f,g}k_i)\binom XY+\ell_i,\qquad
EQ_i=k_i\in B\cap L=C.
\tag{21}
\]
Actual velocities supply regularity of \(k_i\) before
the polynomial weight argument is used. Formula (9)
now says
\[
k_i=A_iU^2+\mu_iUV+B_iV^2,\qquad A_i,\mu_i,B_i\in\mathbb C.
\]
Subtract the actual linear bad-coordinate terms
\(A_iX+B_iY\), leaving
\[
Q_i=\frac{\mu_i}{2}(rX+Y/r)+\ell_i.
\tag{22}
\]
If the vector \(\mu\) is nonzero, normalize it to the first
coordinate line. Its nonzero linear \(S_r\) in (16)
forces \(\mathscr H\ell\) onto that line. Hence
\(Q_2=\ell_2\in C\), \(\mathscr H\ell_2=0\), and (10)
makes \(Q_2\) constant, again impossible.

If \(\mu=0\), every transformed good coordinate is in
\(B\cap L=C\). Over \(R=C_{(a,b)}\), actual generation
gives \(B_R=R[X,Y]\). The original \(Es_*=1\) now
contradicts
\[
E(B_R)\subseteq(a^p,b^q)R[X,Y]
\]
by evaluation at \(X=Y=0\), exactly as in Section 3.
This completes all ranks and proves the theorem.

## 7. Dependence on previous work and exact boundaries

The actual graph, weights, Schur condition, and generator
equalities are inherited from
[pass44](generic-bad-pair-pass44.md).
The rank split and pole-degree mechanism extend
[the exact square-speed proof](square-speed-schur-generation-pass61.md).
The additional gate here is (7)--(10): it gives the full
weighted rational kernel and the actual polynomial
eigenfunctions for the genuine field \(\mathbb C(a,b)\).

The monomials \(U,V\) were never promoted to coordinates.
Their field can be a proper subfield of \(L\), and the proof
explicitly uses the primitive Laurent monomial \(z\) for
independence. In particular the rank-two step requires only
the proved \(Q_1,r,X,Y\) independence, \(r\in M\), and
actual equality \(M=K(Q_2)\). It does not discard a finite
extension by assumption.

The use of a zero-weight rational kernel is also distinct
from polynomial regularity. The linear potentials remain
rational until (12) or (21) makes them actual invariants.
Likewise the lower-rank constant term becomes polynomial
only after the other terms have been proved actual.

The result excludes \(d=1,2\), not \(d\ge3\). It gives
no realization in the latter range and no result for a
general perturbation with these monomial initial terms.
No new theorem about arbitrary algebraic extensions,
ambient invariant coordinates, frame existence, or
unrestricted cancellation is asserted.

This note is a bounded extension of the prior proof, not
a new external classification result. Its algebraic field
steps are proved above. The jet agent independently read
the complete proof through EOF and reconstructed all
weighted field, rank, pole, and actualness gates cleanly.
This is an AI proof audit, not external expert review.

A scratch exact calculation checked the primitive monomial
inverses and both inherited odd Hessians for
\((u,v)=(2,3),(3,2),(1,4),(5,3)\). These are transcription
controls, not the proof of the general exponent statement.
They add no suite or test-method count. During self-audit,
the dummy indeterminate in the rational-function degree
argument was renamed to \(\theta\) to avoid colliding with
the already fixed integer \(u\); no formula changed.
