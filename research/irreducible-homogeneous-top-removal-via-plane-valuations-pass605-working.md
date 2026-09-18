# Irreducible homogeneous top removal through a plane valuation

Date: 2026-09-17

Status: working proof. Not canonically accepted until complete root and
separate saved-source review. This note uses the precise published results
listed below. It claims neither general cancellation nor novelty.

## 1. Proposed general conclusion

Let R=C[x,y,z] with its ordinary grading, and let H be a nonzero
irreducible homogeneous locally nilpotent derivation of ordinary
derivation degree d>0. Here irreducible means that the three coordinate
coefficients of H have no nonconstant common divisor. Choose an original
linear coordinate z with maximal H-degree N. For every q>=1 put

\[
\ell=d+q,\qquad k=qN-1,\qquad \mathcal F_j=\ker H^{j+1}.
\tag{1}
\]

The conclusion is

\[
R_\ell\cap\mathcal F_k
=\mathbb C H(z^q)\ \oplus\ (R_\ell\cap\mathcal F_{k-1}).
\tag{2}
\]

Thus every homogeneous coefficient psi of this ordinary degree and exact
H-degree k admits a unique scalar lambda such that psi-H(lambda z^q)
has strictly smaller H-degree. For smaller-degree psi use lambda=0.
The primitive is a whole polynomial in the original coordinates.

The statement covers arbitrary irreducible ordinary-homogeneous H, not
just the DG family in601/602. The invariant replicas in603/604 do not
satisfy irreducibility. No division by a replica factor inside a given
four-variable extension is allowed by this result.

## 2. Published inputs and their precise roles

The following are imported theorems, not new assertions of this note.

1. Daigle, *On kernels of homogeneous locally nilpotent derivations of
   k[X,Y,Z]*, Osaka J. Math.37 (2000),689--699,
   [original paper](https://ir.library.osaka-u.ac.jp/repo/ouka/all/10628/ojm37_03_09.pdf):
   Facts1.6--1.7 give homogeneous polynomial kernel generators and the
   irreducible Jacobian derivation with that kernel. Fact1.9, or the
   introductory corollary, gives coprime generator degrees for weights
   (1,1,1). Lemma1.5 gives proportionality of derivations with that kernel.

2. Galindo--Monserrat, *Finite Families of Plane Valuations: Value
   Semigroup, Graded Algebra and Poincare Series*,
   [author-hosted paper](https://www.singacom.uva.es/Uploads/2012/4f10d4d746165.pdf),
   Theorem5.3: for a primitive plane divisorial valuation on a regular
   two-dimensional local ring over C, its graded Poincare series is

   \[
   H_{\operatorname{gr}_\nu}(t)
   =\left(\sum_{s\in S_\nu}t^s\right)/(1-t^B),
   \tag{3}
   \]

   where B is its final maximal contact value. Consequently every graded
   piece of value less than B has dimension at most one.

3. Galindo--Monserrat--Moyano-Fernandez, *Minimal plane valuations*,
   [Section2.5--2.6](https://arxiv.org/pdf/1609.05236):
   B=1/vol(nu), muhat(nu)>=sqrt(B), with equality defining minimality.
   The normalization here is the primitive integer valuation, not the
   valuation rescaled to give the maximal ideal value one.

4. Galindo--Monserrat--Moreno-Avila--Moyano-Fernandez,
   *On the valuative Nagata conjecture*,
   [Proposition3.19 and its preceding definition](https://link.springer.com/article/10.1007/s40687-025-00500-2):
   a nonminimal divisorial valuation of P2 has a unique integral
   supraminimal curve. Such a curve has nu(C)/deg(C)=muhat(nu).
   This is a theorem, not an assumption of the Nagata conjecture.

Only these statements are used. In particular, this proof assumes no
classification of all homogeneous rank-three derivations and no
conjecture about very general valuations.

## 3. Kernel degrees and the generic orbit degree

Choose ordinary-homogeneous generators f,g for ker H=C[f,g], and write
a=deg f, b=deg g. They have positive degrees and are algebraically
independent. They are irreducible and nonassociate in R: factorial
closure of an LND kernel transfers any factorization in R to the
polynomial ring C[f,g]. The cited kernel results give

\[
\gcd(a,b)=1,\qquad
H=\gamma\operatorname{Jac}(f,g,\cdot),\quad
\gamma\in\mathbb C^*,\qquad d=a+b-3.
\tag{4}
\]

Indeed the cited Jacobian is itself irreducible, and proportionality
together with irreducibility of H makes the factor a complex unit.

Set K=C(f,g). A homogeneous local slice r gives
K tensor_(C[f,g]) R=K[r], with H=(Hr) partial_r and Hr in K*.
Thus the generic fiber of (f,g):A3->A2 is an affine line embedded by
the three coordinate polynomials x(r),y(r),z(r). Their maximum degree
in r is exactly N.

Its projective closure has degree ab. To check this without an extra
orbit-degree assumption, homogenize the two generic-fiber equations
in P3_K:

\[
f(X,Y,Z)-f W^a=0,\qquad g(X,Y,Z)-g W^b=0.
\tag{5}
\]

These define a complete-intersection curve. There is no curve component
inside W=0, since f and g have no common homogeneous factor. The
affine part is the reduced irreducible generic affine line; a complete
intersection is unmixed, so no extra embedded component at infinity
changes its cycle. Bezout therefore gives its degree ab.

On the other hand the parametrization by r extends to P1_K using
homogeneous forms of degree N: W=S^N and, for example,
X=S^N x(T/S). These forms have no common zero, including S=0,
since one coordinate has degree N. The map is birational onto its
image because K[x(r),y(r),z(r)]=K[r]. Pullback of a hyperplane has
degree N, hence the same projective curve has degree N. We obtain

\[
N=ab.
\tag{6}
\]

The same argument would compute N for a nonzero invariant replica;
the relation between d and a,b in(4) is where irreducibility matters.

## 4. An actual primitive plane divisorial valuation

Extend -deg_H to Frac R=K(r), where it is the valuation at r=infinity.
Restrict it to the ordinary-degree-zero field

\[
L=\mathbb C(x/z,y/z),\qquad U=x/z,\quad V=y/z.
\tag{7}
\]

Call the restricted valuation nu. For any p(U,V) of total degree e,
its whole homogenization p^h=z^e p(x/z,y/z) satisfies

\[
\nu(p)=eN-\deg_H(p^h)\ge0,
\qquad \nu(p)\le eN.
\tag{8}
\]

The first inequality uses deg_H(p^h)<=eN, by the maximal choice of
z. Thus nu is centered on the affine chart C[U,V]. It has a closed
point center: the dehomogenizations

\[
F=f/z^a,\qquad G=g/z^b
\tag{9}
\]

are coprime and both have positive valuation, namely aN and bN.
The prime center contains (F,G), a zero-dimensional ideal in this
two-variable chart, and is therefore maximal.

Here F,G are nonconstant irreducible polynomials of exact degrees a,b.
For example, if deg F<a, every term of f is divisible by z; irreducibility
would imply f is associated to z, impossible since Hz is nonzero.
Localization and dehomogenization preserve the asserted irreducibility
and nonassociation because neither original polynomial is divisible by z.

There is no hidden normalization factor in nu. Choose integers u,v with
au+bv=1 and put h=f^u g^v. This is a rational invariant of ordinary
degree one. We may choose the homogeneous local slice
r=H^(N-1)z, of ordinary degree e_r=1+(N-1)d. Then

\[
w=f^b/g^a,\qquad s=r/h^{e_r},\qquad
L=\mathbb C(w,s),\qquad \nu(s)=-1,\quad \nu(w)=0.
\tag{10}
\]

To verify the field equality, the integral monomial transformation
(f,g)->(w,h) has determinant bv+au=1, so K=C(w,h).
Consequently Frac R=C(w,h,s). Ordinary scalar dilation fixes w,s
and scales h with weight one. Its invariant field is exactly C(w,s),
which is also L. The valuation on that field is the ordinary s-infinity
valuation over C(w). It has primitive value group Z and residue field
C(w). It is a divisorial valuation, represented by s=infinity on a
birational ruled surface, and centered at the closed smooth point just
identified on P2. The plane-valuation theorems in Section2 apply to
the regular local ring O_(P2,p).

## 5. Why the first higher-dimensional graded piece occurs at N squared

Equation(8) proves muhat(nu)<=N for the projective-line degree bound.
The irreducible F and G attain the bound, so muhat(nu)=N. If nu were
nonminimal, their distinct projective closures would both be
supraminimal curves. This contradicts the uniqueness theorem in
Section2. Hence nu is minimal and

\[
B=1/\operatorname{vol}(\nu)=\widehat\mu(\nu)^2=N^2.
\tag{11}
\]

This is minimality of this particular plane valuation. It is unrelated
to choosing a globally degree-minimizing polynomial coordinate frame
for a four-variable derivation.

By(3), every local graded piece of valuation less than N^2 has complex
dimension at most one. The inclusion of C[U,V] in O_(P2,p), with the
induced valuation filtration, injects its graded pieces into the local
ones. The same upper bound therefore holds for the polynomial chart.

## 6. Apply the graded bound to the desired coefficient

For psi in the left side of(2), ordinary homogeneity and(1) give

\[
\nu(\psi/z^\ell)\ge\ell N-k=dN+1=:L_*.
\tag{12}
\]

The critical value is strictly below N^2. Indeed(4)--(6) give

\[
N^2-L_*=N\big((a-1)(b-1)+2\big)-1>0.
\tag{13}
\]

Both psi/z^ell and H(z^q)/z^ell are polynomials in U,V.
The second has valuation exactly L_*, since
deg_H H(z^q)=qN-1 in characteristic zero. It spans the at-most-one-
dimensional graded piece supplied by Section5. There is therefore a
unique complex lambda such that

\[
\nu\big((\psi-\lambda H(z^q))/z^\ell\big)>L_*.
\tag{14}
\]

This is exactly deg_H(psi-H(lambda z^q))<k. The scalar is zero
when psi already has smaller H-degree. Since H(z^q) has exact degree
k, its span intersects F_(k-1) trivially. This proves(2), subject to
the independent review of every imported hypothesis and argument above.

## 7. Actual degree descent and remaining cancellation gap

For E=H+(1+psi)partial_t on R[t], assume psi has exact degree k.
Then deg_E(t)=qN. The whole shear T=t-lambda z^q, with its evident
polynomial inverse, satisfies ET=1+psi-H(lambda z^q). Its nonconstant
part remains ordinary homogeneous of positive degree ell, so ET is
not zero. Thus

\[
1\le\deg_E(T)<qN.
\tag{15}
\]

All original base degrees are unchanged. This is an actual degree-sum
decrease in that supplied frame, and in any already supplied all-positive
base-linear variant. It makes no claim about the Euler shift of the new
frame. No iteration is licensed after losing the relation k=qN-1.

An arbitrary sliced LND on C^[4] has not been placed in this triangular
extension form with an irreducible ordinary-homogeneous restriction and
the critical degree relation, especially not in an actual minimizing
frame. The theorem, even if accepted, does not supply that missing entry
argument. Invariant replicas cannot be silently divided out:603/604
exhibit the fixed-base obstruction and distinguish it from rectification.

No saved checker was executed, imported or compiled for this note.
No expert review, Lean certification, publication claim or external
contact is implied. The general cancellation problem remains unsolved.
