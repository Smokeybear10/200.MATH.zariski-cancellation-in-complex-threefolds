# Recognition audit for a rank-three sliced extension

## 1. Result and limits

This bounded audit did not locate a primary theorem or a published ambient
automorphism proving that the supplied slice below is a coordinate of the
whole four-variable polynomial ring. This is a non-match within the sources
checked, not a claim that the slice is noncoordinate, that its recognition
status is unknown throughout the literature, or that cancellation fails.

The positive conclusions established here are narrower. The displayed
polynomial is a slice and hence is automatically a one-stable coordinate.
A natural localized automorphism sends the old extension coordinate to
this slice, but it has a genuine pole on another old coordinate. Thus that
particular map does not supply an ambient completion. The relevant primary
theorems retain additional hypotheses that have not been established for
this extension.

The base derivation's rank-three and local-slice properties are retained
primary inputs. The polynomial calculations, stable-coordinate observation,
and failed-lift calculation below have direct proofs. No result about an
arbitrary sliced fourfold is asserted.

## 2. Exact candidate and the smaller polynomial certificate

Work over \(\mathbb C\), with
\[
 R=\mathbb C[x,y,z],\qquad B=R[t],\qquad
 f=xz-y^2,\qquad r=x^5+yf^2,
 \qquad g=\frac{f^5+r^2}{x}.
\tag{1}
\]
The last expression is polynomial. For example, the terms not visibly
divisible by \(x\) combine as
\(f^5+y^2f^4=f^4(f+y^2)=xz f^4\).
Define
\[
 H=\operatorname{Jac}(f,g,\mathord\cdot),\qquad
 E=H+(1-fgr)\partial_t,
\tag{2}
\]
where the initial extension of \(H\) to \(B\) kills \(t\).
The exact identities needed below are
\[
 Hf=Hg=0,\qquad Hr=-f^2g,\qquad Hx=-2f^2r,
 \qquad xg=f^5+r^2.
\tag{3}
\]
Dasgupta--Gaifullin's family \(E(m,n,F)\), with
\((m,n,F)=(2,2,t_1^4)\), is exactly this \(H\). Their
Theorem 5.7 establishes that it is an irreducible rank-three LND and that
\(r\) is a minimal local slice; their local-slice construction gives
\(\ker H=\mathbb C[f,g]\). See
[Dasgupta--Gaifullin, Section 5, especially Corollary 5.6 and Theorem 5.7](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10094&wshow=paper).
This is a theorem on \(R\), not a conclusion about \(\ker E\).

The extension \(E\) is locally nilpotent. On base generators this is local
nilpotence of \(H\); on \(t\), the successive derivatives after the first
are the successive \(H\)-derivatives of \(1-fgr\), which terminate.
Local nilpotence on generators implies it on their polynomial ring.

For clarity, the following construction holds more generally. Let
\(a,b\in\ker H\) be nonzero and suppose \(Hr=a^2b\). Set
\[
 E=H+(1+abr)\partial_t,\qquad
 v=at-r^2/2,\qquad q=abv-r,
 \qquad u=t-brv+\frac{ab^2}{2}v^2.
\tag{4}
\]
Then, in the whole domain \(R[t]\),
\[
 Ev=a,\qquad Eq=0,\qquad au=v+q^2/2,
 \qquad Eu=1.
\tag{5}
\]
Indeed, the first two identities follow by differentiating (4). Expanding
\(q^2\) gives the third; differentiating it and cancelling the nonzero
\(a\) gives the fourth. This does not invert \(a\) or delete its zero
fiber.

For (1)--(2), take \(a=f\) and \(b=-g\). In particular the supplied
slice is the whole polynomial
\[
 v=ft-r^2/2,\qquad q=-fgv-r,\qquad
 u=t+grv+\frac{fg^2}{2}v^2.
\tag{6}
\]
The abstract two-variable map in (4) has a polynomial inverse over
\(S=\mathbb C[a,b]\):
\[
 v=au-q^2/2,\qquad r=abv-q,
 \qquad t=u-bqv+\frac{ab^2}{2}v^2.
\tag{7}
\]
Both substitution orders are identities. In the concrete case,
\(f,g,r\) are algebraically independent, since \(r\) is a local slice
over \(\ker H=\mathbb C[f,g]\). Therefore (7) really identifies
\(\mathbb C[f,g][r,t]\) with \(\mathbb C[f,g][q,u]\).
It does not identify \(R[t]\) with a polynomial ring in \(f,g,r,t\).
In particular, \(y=(r-x^5)/f^2\) involves the additional ambient
coordinate \(x\) and a denominator. Extending (7) across these ambient
relations is a separate problem.

There is also a positive grading with weights \((1,1,1,8)\) on the old
coordinates \((x,y,z,t)\). Since \(\deg f=2\), \(\deg r=5\), and
\(\deg g=9\), the components
\[
 \partial_t,\qquad H-fgr\partial_t
\tag{8}
\]
have weights \(-8\) and \(8\), and commute. Each is an LND by the
same extension argument. This grading is not asserted to be the Euler
grading weighted by the actual \(E\)-degrees of a coordinate frame.
Commutation alone does not establish an ambient slice completion.

## 3. What sliceness and one-stability already imply

Let \(A=\ker E\). The slice theorem applied to (5) gives
\[
 B=A[u],\qquad A\cong B/(u).
\tag{9}
\]
Consequently \(u\) is an ambient coordinate in \(B\) if and only if
\(A\cong\mathbb C^{[3]}\). The forward implication takes the quotient
by that coordinate; the reverse uses polynomial generators of \(A\)
together with \(u\).

Every slice of a polynomial ring is automatically one-stably coordinate.
Here, for a new indeterminate \(w\),
\[
 B[w]=A[u,w]=A[w][u],\qquad
 A[w]\cong A[u]=B\cong\mathbb C^{[4]}.
\tag{10}
\]
The isomorphism in the middle fixes \(A\) and renames the indeterminate.
Thus \(u\) is a coordinate after adjoining \(w\). This proves only
one-stability. Removing the additional variable is exactly the missing
unstable conclusion, not a consequence of (10).

## 4. Exact primary-theorem comparisons

### 4.1. Invariant-coefficient extensions

[Freudenburg, Section 7.1, Proposition 7.1](https://arxiv.org/pdf/2108.12021)
starts with \(D\in\operatorname{LND}(B_0)\), writes
\(A_0=\ker D\), and extends by \(D'(t)=c\) for
\(0\ne c\in A_0\). Its kernel description additionally assumes
\(cA_0\cap I_n=cI_n\) for the image ideals \(I_n\).
The Extension Theorem 7.6 in the same paper assumes a fundamental pair
and \(c\) in its degree-zero invariant subring.

The present vertical coefficient fails the shared invariant-coefficient
premise directly:
\[
 H(1-fgr)=f^3g^2\ne0.
\tag{11}
\]
No choice of the notation for the added variable removes this failure in
the supplied presentation. A new ambient coordinate change might produce
a different presentation, but none has been proved here. These theorems
therefore cannot be applied directly to (2).

### 4.2. Residual coordinates and Vénéreau-type constructions

[Lewis, *Strongly residual coordinates over \(A[x]\)*, Theorems 3--4](https://arxiv.org/pdf/1304.1765)
requires an actual polynomial presentation over \(A[x]\), together with
a specified elementary factorization over \(A[x,x^{-1}]\) and the
stated scaled-subalgebra and congruence conditions. Corollary 5 constructs
one-stable coordinates for Vénéreau-type polynomials using explicit
elementary maps. The related sufficient coordinate criterion in
[Lewis, *Vénéreau-type polynomials as potential counterexamples*, Theorem 13](https://arxiv.org/pdf/1007.2230)
also requires its particular polynomial form and actual coordinate maps.

No such factorization or identification with that polynomial form has
been supplied for (6). In particular, replacing the coordinate parameter
in those theorems by \(f=xz-y^2\) is not licensed. The actual quotient
\[
 B/(f)=\mathbb C[x,y,z,t]/(xz-y^2)
\tag{12}
\]
is singular along \(x=y=z=0\). Thus \(B\) is not a polynomial
three-variable algebra over \(\mathbb C[f]\), since that would make
(12) isomorphic to \(\mathbb C^{[3]}\). The smaller polynomial ring
\(\mathbb C[f,g][r,t]\) is not a replacement for \(B\).
Moreover, a conclusion of one-stability alone would not improve (10).
This rules out these proposed direct applications, not every possible
use of a residual-coordinate theorem after additional work.

### 4.3. Regular kernels with an invariant ambient coordinate

[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
proves that a regular kernel of a nonzero LND on
\(k[X_1,X_2,X_3,X_4]\) is polynomial over \(k[X_1]\) when the
derivation kills the actual variable \(X_1\).
Regularity is available here: \(Eu=1\) implies that the partial
derivatives of \(u\) generate the unit ideal, so the hypersurface
\(u=0\), whose ring is \(A\), is smooth.

The missing premise is an ambient coordinate in \(\ker E\).
The known invariants \(f,g,q\) have not been proved to supply one.
Rank three of \(H\) does not rule out a coordinate involving \(t\)
in \(\ker E\); conversely, it does not produce one. This remains a
genuine sufficient route to recognition rather than a theorem already
applicable from the displayed data.

## 5. A specific localized lift has a genuine ambient pole

The following calculation explains concretely why the smaller inverse
(7) cannot simply be asserted to lift by the natural local-slice flow.
Localize the whole ring only for this calculation, and define on \(B_f\)
\[
 L=\frac{H}{f}-gr\partial_t,
 \qquad v=ft-r^2/2.
\tag{13}
\]
Since \(Hf=0\), \(H/f\) is an LND on \(R_f\), and its extension
\(L\) is locally nilpotent on \(B_f\). Directly,
\[
 Lv=0,\quad Lt=-gr,\quad L^2t=fg^2,\quad L^3t=0,
 \qquad Lr=-fg,\quad Lx=-2fr,\quad L^2x=2f^2g.
\tag{14}
\]
Hence \(-vL\) is a locally nilpotent derivation of \(B_f\), and
\(\Phi=\exp(-vL)\) is a genuine automorphism of that localized ring,
with inverse \(\exp(vL)\). It fixes \(f,g\), and
\[
 \Phi(t)=u,\qquad r_1:=\Phi(r)=r+fgv,
 \qquad x_1:=\Phi(x)=x+2frv+f^2gv^2.
\tag{15}
\]
Thus this is a particularly natural candidate completion. Its failure
occurs on an actual base generator, not merely on a chosen expression
for a rational function:
\[
 \Phi(y)=\frac{r_1-x_1^5}{f^2}.
\tag{16}
\]
The numerator \(P=r_1-x_1^5\) belongs to \(B\). Expanding modulo
\(f^2B\), while retaining the exact dependence of \(v\), gives
\[
 P=f^2y+f(g-10x^4r)v\pmod{f^2B}.
\tag{17}
\]
In particular \(P\in fB\). Reduction in the integral domain
\(B/(f)\) gives
\[
 r\equiv x^5,\qquad g\equiv x^9,\qquad
 v\equiv-\frac{x^{10}}2\pmod f,
 \qquad
 \frac{P}{f}\equiv\frac92x^{19}\ne0\pmod f.
\tag{18}
\]
Here \(g\equiv x^9\) follows from its polynomial expansion in (1).
The polynomial \(f=xz-y^2\) is irreducible, and \(x\) is nonzero
in its quotient, so the final nonvanishing is a domain statement.
It follows that \(P\notin f^2B\), and therefore
\[
 \Phi(y)\in f^{-1}B\setminus B.
\tag{19}
\]
The pole is exactly simple along \(f=0\). In particular \(\Phi\)
does not restrict to an endomorphism, much less an automorphism, of
the original \(B\). There is no contradiction with (7): that smaller
map controls \(r,t\), whereas (16) tests a further ambient generator.

This proves failure of this specific completion only. It does not
exclude another automorphism having \(u\) as a component, another
coordinate in \(\ker E\), or another recognition theorem.

## 6. Audit endpoint

The proved certificate is \(Eu=1\), so \(A[u]\cong\mathbb C^{[4]}\)
and \(u\) is one-stably coordinate. Ambient coordinateness of \(u\),
equivalently \(A\cong\mathbb C^{[3]}\), is not established in this
audit. The primary comparisons identify missing premises rather than
an exhaustive absence of theorems. The pole calculation blocks one
explicit tempting lift rather than proving a nonpolynomial kernel.

The source set is restricted to the four groups of primary inputs
above. No further browsing was performed while writing this note.
Fresh unsaved algebra independently checked (3) and the full first
\(f\)-coefficient and nonzero residue in (17)--(18); the slice and
inverse identities are polynomial identities with the direct proofs
given here. No saved checker was executed, imported or compiled, and
no canonical file was edited. Final HELD status is issued separately
after complete author rereading through EOF and an exact hash.
