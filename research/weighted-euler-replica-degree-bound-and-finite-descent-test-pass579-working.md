# Slice-replica degree bounds and an exact finite scalar search

## 1. Scope and actual hypotheses

Work over \(\mathbb C\). Let

\[
B=\mathbb C[X_1,\ldots,X_n]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,
\qquad d_i=\deg_E X_i>0.
\tag{1}
\]

Here \(u\) is an actual slice, and the \(X_i\) are an actual polynomial
coordinate frame, not coefficients promoted from a field. Put
\(S=\sum_i d_i\) and let \(D=\sum_i d_iX_i\partial_{X_i}\) be its weighted
Euler derivation. Assume its exact all-ring \(E\)-filtration shift is
\(\delta>0\). Retained 576 and 577 supply a nonzero locally nilpotent
derivation \(N\) of \(A\), with extension \(\widetilde N\) to \(B=A[u]\)
that kills \(u\) and commutes with \(E\). In particular 577 recovers it
from actual derivations and the given slice:

\[
\widetilde N=
\frac{\operatorname{ad}_E^\delta D-
 (\operatorname{ad}_E^\delta D)(u)E}{\delta!}.
\tag{2}
\]

We suppress the tilde below. The degree bounds themselves need only a
nonzero LND \(N\) of \(A\) extended by \(N(u)=0\); they do not need its
Euler provenance. No polynomial presentation of \(A\) is assumed.

For \(g\ne0\), \(\deg_E g\) is its degree in the genuine polynomial ring
\(A[u]\), and \(\deg_E0=-\infty\). The shift of a nonzero derivation
\(T\) is the least integer \(q\) such that
\(\deg_E T(g)\le\deg_E g+q\) for every nonzero \(g\in B\).

This note proves a finite bound on the slice degree of replicas that do
not increase the sum of coordinate degrees. For parameters in
\(\mathbb C[u]\), it also gives an exact finite constructible existence
test, including a decrease of Euler shift at unchanged degree sum. It
does not prove that this test has a solution for an arbitrary frame.
Invariant coefficients enlarge the family, but are not covered by a
finite-dimensional complex parameter search without an additional bound.

Direct inputs, completely read before writing, are:

- 576, `weighted-euler-positive-shift-and-homogeneous-initial-rank-pass576-working.md`,
  SHA `27019aa84bd06a0fd28794bab43478454eb4185e66439f9dae9a46f218111723`;
- 577, `weighted-euler-commutator-recovery-and-zero-shift-test-pass577-working.md`,
  SHA `87be12a6c8029b5008cf2d6178600997f3b7a4b1e87ae8ad5d56f5da016bafde`;
- 578, `weighted-euler-primitive-nonsliced-actual-control-pass578-working.md`,
  SHA `68ce00ec1b82d02eb66ccf7515991241166ddc88217bbd075e562c555d9554e5`.

These contracts are retained, not a recursive recertification of their
historical dependencies. No claim of novelty is made.

## 2. Actual replicas and the unique-leading-term bound

Put \(R_0=\ker_A N\). For any \(f\in R_0[u]\), the derivation \(fN\) is
locally nilpotent, since \(N(f)=0\) and
\((fN)^r(g)=f^rN^r(g)\). Thus

\[
\Phi_f=\exp(fN),\qquad
\Phi_f^{-1}=\Phi_{-f},\qquad
\Phi_f\Phi_g=\Phi_{f+g}\quad(f,g\in R_0[u])
\tag{3}
\]

are actual polynomial automorphisms of \(B\), all fixing \(u\).
They need not commute with \(E\) when \(f\) depends on \(u\).

Write the entire finite expansions

\[
X_i=\sum_{j=0}^{d_i}a_{ij}u^j,\qquad
\exp(TN)X_i=
\sum_{j=0}^{d_i}\sum_{r\ge0}
\frac{N^r(a_{ij})}{r!}\,u^jT^r.
\tag{4}
\]

All coefficients belong to the domain \(A\). Define the active set
\(I=\{i:N(X_i)\ne0\}\). It is nonempty: otherwise \(N\) kills the
coordinate generators of \(B\) and is zero. Inactive coordinates are
fixed by every \(\Phi_f\).

Let \(f\ne0\) have positive \(u\)-degree \(k\), with leading coefficient
\(\lambda\in R_0\setminus\{0\}\). Fix an active \(i\) and suppose
\(k>d_i\). For two distinct pairs \((j,r)\) occurring in (4), the numbers
\(j+kr\) are distinct: an equality would give
\(k(r-r')=j'-j\), whose right side has absolute value at most \(d_i<k\).
Consequently the largest such number occurs only once. If

\[
r_i=\deg_N X_i\ge1,\qquad
j_i=\deg_u N^{r_i}(X_i),
\]

that largest number is \(kr_i+j_i\). Its coefficient after \(T=f(u)\)
is \(\lambda^{r_i}N^{r_i}(a_{ij_i})/r_i!\), which is nonzero in the
domain. Lower coefficients of \(f\) cannot reach that degree. Hence

\[
k>d_i\quad\Longrightarrow\quad
\deg_E\Phi_f(X_i)=kr_i+j_i\ge k>d_i
\qquad(i\in I).
\tag{5}
\]

This uses the complete polynomial (4), including all possible lower
coefficients and cancellations. It does not assert (5) when \(k\le d_i\).

It follows that every nonconstant parameter satisfying coordinatewise
nonincrease obeys

\[
\deg_E\Phi_f(X_i)\le d_i\ (\forall i)
\quad\Longrightarrow\quad
\deg_u f\le\min_{i\in I}d_i.
\tag{6}
\]

The bound needed for the lexicographic complexity with degree sum first
is the weaker, more general statement

\[
\sum_i\deg_E\Phi_f(X_i)\le S
\quad\Longrightarrow\quad
\deg_u f\le M:=\max_{i\in I}d_i\le\max_i d_i.
\tag{7}
\]

Indeed, if \(k>M\), every active degree increases strictly by (5), and
every inactive degree is unchanged. Their sum then increases strictly.
Some individual degrees may increase in (7); none are discarded by the
argument. Both (6) and (7) hold for the full parameter ring \(R_0[u]\),
not only for \(\mathbb C[u]\). They are necessary bounds, not existence
statements.

## 3. Constant parameters do not change either complexity component

For \(c\in R_0\), \(\Phi_c\) commutes with \(E\). Its inverse has the
same property, so it preserves the \(E\)-degree of every element exactly.
For any actual frame \(Y\), its weighted Euler derivation is transported
to the weighted Euler derivation of \(\Phi_c(Y)\) by conjugation with
\(\Phi_c\). Since this automorphism and its inverse preserve the entire
filtration, that conjugation preserves the exact shift too.

For general \(f\in R_0[u]\), (3) gives

\[
\Phi_f=\Phi_{f(0)}\Phi_{f-f(0)}.
\tag{8}
\]

The two resulting frames therefore have the same degree tuple and Euler
shift. There is no loss for either complexity component in imposing
\(f(0)=0\). This includes the zero parameter: all constant replicas have
the original tuple and shift, and do not give a strict improvement.

## 4. An exact finite search for complex-coefficient replicas

Now restrict to \(f\in\mathbb C[u]\). By (7) and (8), every replica that
can improve the lexicographic pair \((S,\delta)\) has an equivalent
parameter in the finite-dimensional family

\[
f_{\lambda}(u)=\sum_{j=1}^{M}\lambda_j u^j,
\qquad \lambda=(\lambda_1,\ldots,\lambda_M)\in\mathbb C^M,
\qquad Y_i(\lambda)=\Phi_{f_\lambda}(X_i).
\tag{9}
\]

The exponential and inverse are finite polynomial expressions in the
actual coordinates and \(\lambda\). In particular their coefficient
supports are finite uniformly over this parameter space.

Enumerate the finitely many nonnegative integer tuples
\(e=(e_1,\ldots,e_n)\) with \(\sum e_i\le S\). On the exact-profile locus
for \(e\), impose

\[
E^{e_i+1}Y_i(\lambda)=0,
\qquad E^{e_i}Y_i(\lambda)\ne0
\quad(1\le i\le n).
\tag{10}
\]

The all-zero tuple has empty locus, since otherwise \(E\) kills all
coordinate generators \(Y_i\). Zero entries are allowed and explicitly
record coordinates in \(\ker E\). If only all-positive target frames are
being considered, enumerate instead \(e_i\ge1\), in which case
\(e_i\le S-n+1\). This positive restriction must not silently remove the
zero-degree boundary in a search for arbitrary improvements.

Each equality in (10) is a finite set of coefficient equations in
\(\lambda\), using the actual polynomial coordinates of \(B\). Each
inequality means at least one of finitely many coefficients is nonzero.
Thus (10) is an exact constructible condition, not a generic leading-term
approximation. It includes degree drops caused by special cancellations.

### 4.1 Correct Euler derivation after a degree-profile change

For a fixed candidate profile \(e\), put

\[
D_e=\sum_i e_iX_i\partial_{X_i},\qquad
D_{e,\lambda}=\Phi_{f_\lambda}D_e\Phi_{f_\lambda}^{-1}.
\tag{11}
\]

On the locus (10), this is exactly the weighted Euler derivation of the
actual frame \(Y_i(\lambda)\), with its new \(E\)-degrees as weights.
Formula (11) is a polynomial derivation with finite coefficient support
in the actual coordinates and \(\lambda\). Its construction also works
when some \(e_i=0\). Only for \(e=d\) is it the conjugate of the old
weighted Euler derivation \(D\). For a changed profile, conjugating the
old \(D\) would compute the wrong shift.

### 4.2 A finite exact shift test without a kernel presentation

The given actual slice supplies the finite Taylor projection

\[
\pi(g)=\sum_{r\ge0}\frac{(-u)^r}{r!}E^r(g),\qquad
\alpha_i=\pi(X_i).
\tag{12}
\]

In the identity \(B=A[u]\), this is evaluation at \(u=0\), hence a ring
retraction onto \(A\). Therefore \(A=\mathbb C[\alpha_1,\ldots,\alpha_n]\).
These are actual, possibly redundant and algebraically dependent,
polynomial generators. They are not asserted to be coordinates.

For every nonzero derivation \(T\) of \(B\), the exact shift is

\[
\deg_E T=
\max\left\{\max_i\deg_E T(\alpha_i),\ \deg_E T(u)-1\right\}.
\tag{13}
\]

Zero images contribute \(-\infty\). The upper bound follows by the
Leibniz rule on \(A[u]\) using the displayed generators. The reverse
bound follows by applying the definition to each \(\alpha_i\in A\) and
to \(u\). Constant or zero \(\alpha_i\) contribute no spurious bound.

Because the old \(\delta\) is a positive integer, (13) gives the finite
polynomial criterion

\[
\deg_E D_{e,\lambda}<\delta
\quad\Longleftrightarrow\quad
\begin{cases}
E^\delta D_{e,\lambda}(\alpha_i)=0&\text{for every }i,\\
E^{\delta+1}D_{e,\lambda}(u)=0.&
\end{cases}
\tag{14}
\]

This remains valid at zero-degree target coordinates, without importing
a positive-Euler theorem outside its hypotheses. The test uses only
actual \(E,N,u,X_i\), finite exponentials, and polynomial coefficient
equalities. It does not require previously known generators of \(A\).

For \(\sum e_i<S\), retain all parameters satisfying (10). For
\(\sum e_i=S\), retain those satisfying both (10) and (14). Their finite
union is nonempty if and only if some scalar-polynomial replica strictly
decreases the lexicographic complexity \((\sum_i\deg_E X_i,\deg_E D)\)
without increasing its first component. This is a finite algebraic
existence criterion. It is not a theorem that the union is nonempty,
nor a practical bound on the cost of deciding its nonemptiness.

For the coordinatewise version one may use (6) and enumerate only
\(e_i\le d_i\). That smaller search is not interchangeable with the
sum-nonincreasing search above.

## 5. Invariant coefficients: the same slice-degree bound, a larger search

For \(f\in R_0[u]\), (7) and constant-term removal still hold. Thus only
finitely many powers of \(u\) are needed. The coefficients of those
powers, however, are arbitrary elements of \(R_0\). No bound on their
polynomial complexity in \(A\) follows from (5). They cannot be treated
as finitely many complex scalars, and a derivation such as \(D_e\) can
differentiate them. Consequently Section 4 does not establish a
finite-dimensional complex search for this enlarged family.

A retained polynomial control illustrates that invariant coefficients
can give legitimate moves. In 576, on \(\mathbb C[a,b,c,u]\), consider

\[
X=a+u^4,\quad Y=b+u^5,\quad Z=c+a^2u^6+u^3,\quad
W=u+Y^2-XZ.
\tag{15}
\]

The inverse starts with \(u=W-Y^2+XZ\), then recovers \(a,b,c\) from the
first three rows, so this is an actual frame. Its degree tuple is
\((4,5,6,10)\). The recovered derivation is \(72a\partial_c\). Dividing
only by the nonzero complex constant 72 gives the equivalent replica
direction \(N_0=a\partial_c\). The invariant parameter
\(f=-au^6\in(\ker N_0)[u]\) sends \(c\) to \(c-a^2u^6\), and gives
the degree tuple \((4,5,3,10)\), decreasing the sum from 25 to 22.
For the raw recovered derivation use \(f=-au^6/72\).
This example makes no assertion about the absence of scalar-parameter
moves in that frame.

## 6. Sharpness and a boundary on degree-decrease claims

### 6.1 The bound is sharp in actual positive Euler frames

For an integer \(d\ge2\), the retained 577 frame is

\[
(X_1,X_2,X_3,X_4)
=(a+u^d+u^{d-1},\ b+u,\ c+u,\ u).
\tag{16}
\]

Its inverse subtracts the displayed powers of \(X_4=u\). Its exact
Euler shift is \(d-1\), and its recovered derivation is \(N=\partial_a\).
The only active coordinate is \(X_1\), so both bounds (6) and (7) equal
\(d\). The parameter \(f=-u^d\) gives the actual frame
\((a+u^{d-1},b+u,c+u,u)\), lowering the tuple from
\((d,1,1,1)\) to \((d-1,1,1,1)\). Thus equality in the slice-degree bound
is genuinely needed. Its cancellation is precisely outside the strict
inequality \(k>d_i\) used in (5).

### 6.2 No degree-sum decrease need exist, but shift may still decrease

In the accepted 578 control let

\[
N=a\partial_b+b\partial_c,\qquad
(X,Y,Z,W)=
\left(u,\ a+u^2,\ b+au+u^4,
c+bu+\frac12au^2+u^6\right).
\tag{17}
\]

This actual frame has tuple \((1,2,4,6)\), and Euler shift 1 with
recovered derivation \(N\). Its inverse successively recovers \(u,a,b,c\).
Let \(I=(a,b)\subset A=\mathbb C[a,b,c]\). Since \(N(B)\subset IB\),
every invariant-coefficient replica \(\Phi_f\), \(f\in R_0[u]\), is the
identity modulo \(IB\). Modulo that ideal the four rows are

\[
(u,\ u^2,\ u^4,\ c+u^6).
\tag{18}
\]

The quotient map cannot increase \(u\)-degree. Hence every transformed
coordinate has degree at least its original degree. No such replica can
strictly decrease the degree sum in this frame, even with invariant
coefficients. This is an actual boundary, not an abstract assigned
degree tuple.

Nevertheless \(f=-u\) gives

\[
\Phi_{-u}(X,Y,Z,W)=(u,\ a+u^2,\ b+u^4,\ c+u^6).
\tag{19}
\]

The degree tuple is unchanged. The new weighted Euler derivation is
\(u\partial_u+2a\partial_a+4b\partial_b+6c\partial_c\), whose exact
shift is zero. Thus the same family does decrease \((S,\delta)\).
The fixed-ideal obstruction proves only the absence of degree-sum
decrease; it does not prove absence of full lexicographic descent.

## 7. Verification and boundary of the result

Fresh unsaved algebra checked the entire replica rows in (17), the
fixed-ideal reduction, (19) and its whole Euler derivation, the old and
new tuples in (15), and (16) for \(d=2,4,7\). No saved checker was run,
imported, or compiled. The unique-leading-term proof was independently
challenged on the full coefficient support, including invariant
coefficients and constant parameters.

The conclusions are finite slice-degree bounds, an exact finite scalar
parameter criterion, and explicit polynomial controls. There is no
general assertion that a replica improves the frame, that repeated
replicas terminate, that an arbitrary globally minimizing frame has a
coordinate in \(\ker E^2\), or that these moves settle cancellation.
No globally minimality claim is made for any displayed control.

This is a bounded working source, held only after complete author
rereading. It changes no canonical record or earlier source.
